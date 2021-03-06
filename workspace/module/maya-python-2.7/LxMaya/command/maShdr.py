# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscMtdCore, bscObjects, bscMethods
#
from LxPreset import prsConfigure, prsOutputs
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr
#
from LxDatabase import dtbMtdCore
#
from LxDatabase.data import datHash
#
from LxMaya.command import maUtils, maAttr, maUuid, maTxtr
#
none = ''
#
DEF_mya_default_shading_engine_list = [
    'initialShadingGroup',
    'initialParticleSE',
    'defaultLightSet',
    'defaultObjectSet'
]


#
def materialNodeTypeConfig():
    dic = bscMtdCore.orderedDict()
    #
    majorTypes = [
        'texture',
        'shader',
        'utility'
    ]
    for majorType in majorTypes:
        nodeTypes = cmds.listNodeTypes(majorType)
        for nodeType in nodeTypes:
            dic[nodeType] = majorType
    return dic


#
def _getNodeShadingEngineNodeStringList(nodepathString):
    lis = []
    #
    shapePath = maUtils._dcc_getNodShapeNodepathStr(nodepathString, 1)
    if not shapePath:
        shapePath = nodepathString
    #
    outputNodes = maUtils._getNodeTargetNodeStringList(shapePath, appCfg.DEF_mya_type_shading_engine)
    if outputNodes:
        [lis.append(i) for i in outputNodes if i not in DEF_mya_default_shading_engine_list]
    return lis


#
def getObjectsShadingEngineLis(objectLis):
    lis = []
    if objectLis:
        for nodepathString in objectLis:
            shadingEngineLis = _getNodeShadingEngineNodeStringList(nodepathString)
            if shadingEngineLis:
                [lis.append(i) for i in shadingEngineLis if i not in lis]
    return lis


#
def getObjectMaterials(nodepathString):
    # List [ <Material Info Nde_Node> ]
    materials = []
    shadingEngineLis = _getNodeShadingEngineNodeStringList(nodepathString)
    if shadingEngineLis:
        for shadingEngine in shadingEngineLis:
            inputNodes = maUtils._getNodeTargetNodeStringList(shadingEngine, 'materialInfo')
            if inputNodes:
                for inputNode in inputNodes:
                    if not inputNode in materials:
                        materials.append(inputNode)
    return materials


#
def getObjectsMaterials(objectLis):
    # List [ <Shading Engine Nde_Node> ]
    materials = []
    if objectLis:
        for nodepathString in objectLis:
            subMaterials = getObjectMaterials(nodepathString)
            for material in subMaterials:
                if not material in materials:
                    materials.append(material)
    return materials


# Get Nde_ShaderRef Nodes
def getConnectionNodes(material):
    # Sub Method
    def getBranch(node):
        inputNodes = maUtils._getNodeSourceNodeStringList(node)
        if inputNodes:
            for node in inputNodes:
                if node:
                    if not node in nodes:
                        nodes.append(node)
                        getBranch(node)
    # List [ < File Nde_Node > ]
    nodes = [material]
    # Loop
    getBranch(material)
    #
    return nodes


#
def getMaterialNodes(material):
    exceptObjectTypes = ['mesh', 'nurbsSurface', 'nurbsCurve', 'pgYetiMaya', 'nurbsHair']
    exceptNodeTypes = ['groupId', 'colorManagementGlobals']
    #
    materialNodes = []
    connectionNodes = getConnectionNodes(material)
    for node in connectionNodes:
        objectType = maUtils._getNodeShapeCategoryString(node)
        nodeType = maUtils._getNodeCategoryString(node)
        if not objectType in exceptObjectTypes and not nodeType in exceptNodeTypes:
            materialNodes.append(node)
    return materialNodes


#
def getTextureNodeLisByObject(objectLis):
    textureNodes = []
    shadingEngineLis = getObjectsShadingEngineLis(objectLis)
    if shadingEngineLis:
        for shadingEngine in shadingEngineLis:
            nodes = getConnectionNodes(shadingEngine)
            if nodes:
                for node in nodes:
                    nodeType = maUtils._getNodeCategoryString(node)
                    if nodeType in appCfg.MaTexture_NodeTypeLis:
                        if not node in textureNodes:
                            textureNodes.append(node)
    return textureNodes


#
def getObjectsMaterialNodesRenameDic(objectLis, assetName, assetVariant, assetStage):
    dic = bscMtdCore.orderedDict()
    if objectLis:
        explain = u'''Get Object's Material Rename Data'''
        maxValue = len(objectLis)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for objSeq, nodepathString in enumerate(objectLis):
            progressBar.update()
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            materials = getObjectMaterials(nodepathString)
            index = 0
            if materials:
                for matlSeq, material in enumerate(materials):
                    nodes = getMaterialNodes(material)
                    if nodes:
                        for nodSeq, node in enumerate(nodes):
                            seq = str(index)
                            hierarchyName = maUtils.getAttrDatum(nodepathString, prsOutputs.Util.basicHierarchyAttrLabel)
                            if hierarchyName is None:
                                hierarchyName = assetStage + '_' + objectType + '_' + str(objSeq)
                            nodeType = maUtils._getNodeCategoryString(node)
                            #
                            nodeName = '{0}_{1}_{2}_{3}_{4}_{5}'.format(
                                prsOutputs.Util.Lynxi_Prefix_Product_Asset, assetName, assetVariant,
                                hierarchyName,
                                nodeType, seq
                            )
                            dic[node] = nodeName
                            #
                            index += 1
    return dic


#
def setObjectsMaterialNodesRename(objectLis, assetName, assetVariant, assetStage):
    exceptObjectTypes = ['mesh', 'pgYetiMaya', 'nurbsHair', 'aiAOV']
    exceptNodeLis = ['time1', 'lambert1', 'defaultColorMgtGlobals', 'layerManager', 'renderLayerManager', assetPr.astUnitModelBridgeGroupName(assetName)]
    #
    renameDataArray = []
    renameDic = getObjectsMaterialNodesRenameDic(objectLis, assetName, assetVariant, assetStage)
    if renameDic:
        for node, nodeName in renameDic.items():
            objectType = maUtils._getNodeShapeCategoryString(node)
            if not objectType in exceptObjectTypes:
                if not node in exceptNodeLis:
                    if not node == nodeName:
                        renameDataArray.append((node, nodeName))
    #
    if renameDataArray:
        # View Progress
        explain = u'''Rename Material - Nde_Node'''
        maxValue = len(renameDataArray)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for node, nodeName in renameDataArray:
            progressBar.update(nodeName)
            print node, nodeName
            maUtils.setNodeRename(node, nodeName)


#
def getAovNodesRenameDic(aovNodes, assetName, assetVariant):
    dic = bscMtdCore.orderedDict()
    if aovNodes:
        explain = u'''Get AOV's Rename Data'''
        maxValue = len(aovNodes)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for aovSeq, aov in enumerate(aovNodes):
            progressBar.update()
            nodes = getMaterialNodes(aov)
            if nodes:
                for nodSeq, node in enumerate(nodes):
                    seq = '{0}{1}'.format(
                        str(aovSeq + 1).zfill(3), str(nodSeq + 1).zfill(3)
                    )
                    nodeType = maUtils._getNodeCategoryString(node)
                    nodeName = '{0}_{1}_{2}_{3}'.format(
                        assetName, assetVariant,
                        nodeType, seq
                    )
                    dic[node] = nodeName
    return dic


#
def setRenameAovNodes(aovNodes, assetName, assetVariant):
    exceptObjectTypes = ['mesh', 'pgYetiMaya', 'nurbsHair', 'aiAOV', 'aiAOVDriver', 'aiAOVFilter']
    exceptNodeLis = [
        'time1',
        'lambert1',
        'defaultColorMgtGlobals',
        'layerManager',
        'defaultArnoldDriver', 'defaultArnoldFilter'
    ]
    #
    renameDataArray = []
    renameDic = getAovNodesRenameDic(aovNodes, assetName, assetVariant)
    if renameDic:
        for node, nodeName in renameDic.items():
            objectType = maUtils._getNodeShapeCategoryString(node)
            if not objectType in exceptObjectTypes:
                if not node in exceptNodeLis:
                    if not node == nodeName:
                        renameDataArray.append((node, nodeName))
    #
    if renameDataArray:
        # View Progress
        explain = u'''Rename AOV Nde_Node'''
        maxValue = len(renameDataArray)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for node, nodeName in renameDataArray:
            progressBar.update(nodeName)
            maUtils.setNodeRename(node, nodeName)


# Nde_Node Data
def getMaterialNodeData(material):
    nodesDataArray = []
    nodes = getMaterialNodes(material)
    if nodes:
        for node in nodes:
            # Filter Unused Nde_Node Type
            nodeType = maUtils._getNodeCategoryString(node)
            definedAttrData = maAttr.getNodeDefAttrDatumLis(node)
            customAttrData = maAttr.getNodeUserDefAttrData(node)
            nodesDataArray.append((node, nodeType, definedAttrData, customAttrData))
    return nodesDataArray


#
def getMaterialComponentData(material):
    composeDataArray = []
    nodes = getMaterialNodes(material)
    if nodes:
        for node in nodes:
            # Filter Unused Nde_Node Type
            nodeType = maUtils._getNodeCategoryString(node)
            composeDataArray.append(nodeType)
    return composeDataArray


#
def getMaterialAttributeData(material):
    attributeDataArray = []
    nodes = getMaterialNodes(material)
    if nodes:
        for node in nodes:
            # Filter Unused Nde_Node Type
            nodeType = maUtils._getNodeCategoryString(node)
            definedAttrData = maAttr.getNodeDefAttrDatumLis(node)
            customAttrData = maAttr.getNodeUserDefAttrData(node)
            attributeDataArray.append(
                (nodeType, getNodeAttrDataReduce(definedAttrData), getNodeAttrDataReduce(customAttrData))
            )
    return attributeDataArray


#
def getNodeAttrDataReduce(attrDatas):
    attrDataArray = []
    MaTexture_AttrNameLis = maTxtr.MaTexture_AttrNameLis
    if attrDatas:
        for data in attrDatas:
            attrName, data, attrType, lock = data
            if attrName in MaTexture_AttrNameLis:
                isTexture = maTxtr.isOsTextureExist(data)
                if isTexture:
                    data = bscMethods.OsFile.basename(data)
                if not isTexture:
                    data = none
            attrDataArray.append((attrName, data))
    return attrDataArray


# Nde_Node Data
def getMaterialsNodeData(materials):
    dic = bscMtdCore.orderedDict()
    if materials:
        for material in materials:
            uniqueId = maUuid._getNodeUniqueIdString(material)
            shaderNodeData = getMaterialNodeData(material)
            if shaderNodeData:
                dic[uniqueId] = shaderNodeData
    return dic


#
def getMaterialRelationData(material):
    MaAttrNameLis_ShaderExcept = [
        '.groupNodes',
        '.dagSetMembers'
    ]
    #
    connectionArray = []
    nodes = getConnectionNodes(material)
    if nodes:
        for node in nodes:
            subConnectionArray = maAttr.getNodeConnectionsDataArray(node)
            for sourceAttr, targetAttr in subConnectionArray:
                isCollection = True
                for exceptAttrName in MaAttrNameLis_ShaderExcept:
                    if exceptAttrName in targetAttr:
                        isCollection = False
                if isCollection:
                    connectionArray.append((sourceAttr, targetAttr))
    return connectionArray


# Nde_Node Data
def getMaterialsRelationData(materials):
    dic = bscMtdCore.orderedDict()
    if materials:
        for material in materials:
            uniqueId = maUuid._getNodeUniqueIdString(material)
            nodeConnectionData = getMaterialRelationData(material)
            if nodeConnectionData:
                dic[uniqueId] = nodeConnectionData
    return dic


#
def getMaterialComponentInfo(material):
    materialComponentData = getMaterialComponentData(material)
    return datHash.getStrHashKey(materialComponentData)


#
def getMaterialAttributeInfo(material):
    materialAttributeData = getMaterialAttributeData(material)
    return datHash.getStrHashKey(materialAttributeData)


#
def getMaterialRelationInfo(material):
    connections = getMaterialRelationData(material)
    relationData = getNodeConnectionDataReduce(connections)
    return datHash.getStrHashKey(relationData)


#
def getNodeConnectionDataReduce(connections):
    connectionArray = []
    if connections:
        for sourceAttr, targetAttr in connections:
            if not sourceAttr.endswith('.message'):
                connectionArray.append((sourceAttr, targetAttr))
    return connectionArray


#
def getMaterialsInformationData(materials):
    dic = bscMtdCore.orderedDict()
    if materials:
        for material in materials:
            uniqueId = maUuid._getNodeUniqueIdString(material)
            dic[uniqueId] = \
                getMaterialComponentInfo(material), \
                getMaterialAttributeInfo(material), \
                getMaterialRelationInfo(material)
    return dic


#
def setCreateCompMaterialsNodes(materialsNodeData):
    if materialsNodeData:
        for uniqueId, nodeDataArray in materialsNodeData.items():
            if nodeDataArray:
                keyNodeData = nodeDataArray[0]
                setCreateMaterialNode(keyNodeData)
                material = keyNodeData[0]
                maUuid.setMayaUniqueId(material, uniqueId)
                for subNodeData in nodeDataArray[0:]:
                    setCreateMaterialNode(subNodeData)


#
def setCreateCompMaterialsUniqueId(materialsNodeData):
    if materialsNodeData:
        for uniqueId, nodeDataArray in materialsNodeData.items():
            if nodeDataArray:
                keyNodeData = nodeDataArray[0]
                setCreateMaterialNode(keyNodeData)
                material = keyNodeData[0]
                maUuid.setMayaUniqueId(material, uniqueId)


#
def setCreateCompAovsNodes(materialsNodeData):
    if materialsNodeData:
        for uniqueId, nodeDataArray in materialsNodeData.items():
            if nodeDataArray:
                keyNodeData = nodeDataArray[0]
                setCreateMaterialNode(keyNodeData)
                aovNode = keyNodeData[0]
                maUuid.setMayaUniqueId(aovNode, uniqueId)
                setCreateAovNodeLink(aovNode)
                for subNodeData in nodeDataArray[0:]:
                    setCreateMaterialNode(subNodeData)


#
def setCreateMaterialNode(materialNodeData):
    node, nodeType, definedAttrData, customAttrData = materialNodeData
    #
    setCreateNode(node, nodeType, definedAttrData)
    # Set User Attribute
    maAttr.setObjectUserDefinedAttrs(node, customAttrData, lockAttribute=False)


#
def setCreateNode(node, nodeType, definedAttrData):
    shaderNodeTypeDic = materialNodeTypeConfig()
    # Filter Exists
    if not cmds.objExists(node):
        isShader = nodeType in shaderNodeTypeDic.keys()
        # Filter is Nde_ShaderRef Nde_Node
        if not isShader:
            cmds.createNode(nodeType, name=node)
        #
        if isShader:
            majorType = shaderNodeTypeDic[nodeType]
            if majorType == 'texture':
                cmds.shadingNode(nodeType, name=node, asTexture=1)
            elif majorType == 'shader':
                cmds.shadingNode(nodeType, name=node, asShader=1)
            elif majorType == 'utility':
                cmds.shadingNode(nodeType, name=node, asUtility=1)
    # Set Nde_Node Attribute
    maAttr.setNodeDefAttrByData(node, definedAttrData, lockAttribute=False)


#
def setCreateMaterialsConnections(connectionData):
    if connectionData:
        for uniqueId, connectionArray in connectionData.items():
            maAttr.setCreateConnections(connectionArray)


#
def getMaterialEvaluateData(objectLis):
    exceptObjectTypes = [
        'mesh',
        'pgYetiMaya',
        'nurbsHair'
    ]
    #
    exceptNodeLis = [
        'time1',
        'lambert1',
        'defaultColorMgtGlobals'
    ]
    #
    dic = bscMtdCore.orderedDict()
    totalMaterials = []
    totalNodes = []
    totalConnections = []
    if objectLis:
        for nodepathString in objectLis:
            shadingEngineLis = _getNodeShadingEngineNodeStringList(nodepathString)
            if shadingEngineLis:
                for shadingEngine in shadingEngineLis:
                    if not shadingEngine in totalMaterials:
                        totalMaterials.append(shadingEngine)
                    # Nde_Node
                    nodes = getMaterialNodes(shadingEngine)
                    if nodes:
                        for node in nodes:
                            objectType = maUtils._getNodeShapeCategoryString(node)
                            if not objectType in exceptObjectTypes:
                                if not node in exceptNodeLis:
                                    if not node in totalNodes:
                                        totalNodes.append(node)
                    # Connection
                    connectionArray = getMaterialRelationData(shadingEngine)
                    if connectionArray:
                        for connection in connectionArray:
                            if not connection in totalConnections:
                                totalConnections.append(connection)
    dic['material'] = len(totalMaterials)
    dic['node'] = len(totalNodes)
    dic['connection'] = len(totalConnections)
    return dic


#
def getObjectsMaterialRelinkData(objectLis):
    shaderObjectTypes = ['mesh', 'pgYetiMaya', 'nurbsHair']
    dic = bscMtdCore.orderedDict()
    for nodepathString in objectLis:
        linkDatumLis = []
        shape = maUtils._dcc_getNodShapeNodepathStr(nodepathString, fullPath=1)
        shadingEngineLis = maUtils._getNodeTargetNodeStringList(shape, appCfg.DEF_mya_type_shading_engine)
        if shadingEngineLis:
            for shadingEngine in shadingEngineLis:
                elementSetData = cmds.sets(shadingEngine, query=1)
                if elementSetData:
                    elementSetFullPathData = [i for i in cmds.ls(elementSetData, leaf=1, noIntermediate=1, long=1)]
                    for data in elementSetFullPathData:
                        # Object Group
                        if data.startswith(nodepathString):
                            showType = cmds.ls(data, showType=1)[1]
                            if showType in shaderObjectTypes:
                                linkData = none, shadingEngine
                                if not linkData in linkDatumLis:
                                    linkDatumLis.append(linkData)
                            # Component Object Group
                            if showType == 'float3':
                                componentObjectIndex = data.split('.')[-1]
                                linkData = '.' + componentObjectIndex, shadingEngine
                                if not linkData in linkDatumLis:
                                    linkDatumLis.append(linkData)
        dic[nodepathString] = linkDatumLis
    return dic


#
def getMaterialShadingEngine(uniqueId):
    material = maUuid.getObject(uniqueId)
    if material:
        shadingEngineLis = maUtils._getNodeSourceNodeStringList(material, appCfg.DEF_mya_type_shading_engine)
        if shadingEngineLis:
            return shadingEngineLis[0]


#
def getShadingEngineMaterialUniqueId(shadingEngine):
    materials = maUtils._getNodeTargetNodeStringList(shadingEngine, 'materialInfo')
    if materials:
        material = materials[0]
        return maUuid._getNodeUniqueIdString(material)


#
def getShaderObjectsObjSetDic(objectLis):
    dic = bscMtdCore.orderedDict()
    for nodepathString in objectLis:
        compIndex = maUuid._getNodeUniqueIdString(nodepathString)
        linkDatumLis = getShaderObjectObjSetSub(nodepathString)
        dic[compIndex] = linkDatumLis
    return dic


#
def getShaderObjectObjSetSub(nodepathString):
    shaderObjectTypes = ['mesh', 'pgYetiMaya', 'nurbsHair']
    #
    lis = []
    #
    shadingEngineLis = _getNodeShadingEngineNodeStringList(nodepathString)
    if shadingEngineLis:
        for shadingEngine in shadingEngineLis:
            compMaterialIndex = getShadingEngineMaterialUniqueId(shadingEngine)
            elementSetData = cmds.sets(shadingEngine, query=1)
            if elementSetData:
                elementSetFullPathData = [i for i in cmds.ls(elementSetData, leaf=1, noIntermediate=1, long=1)]
                for data in elementSetFullPathData:
                    # Object Group
                    if data.startswith(nodepathString):
                        showType = cmds.ls(data, showType=1)[1]
                        if showType in shaderObjectTypes:
                            linkData = none, compMaterialIndex
                            if not linkData in lis:
                                lis.append(linkData)
                        # Component Object Group
                        if showType == 'float3':
                            componentObjectIndex = data.split('.')[-1]
                            linkData = '.' + componentObjectIndex, compMaterialIndex
                            if not linkData in lis:
                                lis.append(linkData)
    return lis


# Link Material
def setLinkObjectsMaterial(data, objectNamespace=none, materialNamespace=none):
    if data:
        # View Progress
        explain = u'''Link / Relink Material'''
        maxValue = len(data)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for nodepathString, linkDatumLis in data.items():
            # In Progress
            progressBar.update()
            #
            usedObject = \
                [nodepathString, maUtils.getObjectPathJoinNamespace(nodepathString, objectNamespace)][objectNamespace != none]
            #
            if linkDatumLis:
                # Clear >>> 01
                setObjectCleanTransformShadingEngine(usedObject)
                setObjectCleanShapeShadingEngine(usedObject)
                # Link >>> 02
                isComponentLink = len(linkDatumLis) > 1
                #
                if not isComponentLink:
                    componentObjectIndex, shadingEngine = linkDatumLis[0]
                    usedShadingEngine = [shadingEngine, maUtils.getNodeJoinNamespace(shadingEngine, materialNamespace)][materialNamespace != none]
                    setObjectAssignMaterial(usedObject, none, usedShadingEngine)
                #
                if isComponentLink:
                    for componentObjectIndex, shadingEngine in linkDatumLis:
                        usedShadingEngine = [shadingEngine, maUtils.getNodeJoinNamespace(shadingEngine, materialNamespace)][materialNamespace != none]
                        setObjectAssignMaterial(usedObject, componentObjectIndex, usedShadingEngine)


# Link Material
def setMaterialsObjectSetsConnect(datumDic):
    if datumDic:
        # View Progress
        explain = u'''Connect Material's Object Set(s)'''
        maxValue = len(datumDic)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for compIndex, linkDatumLis in datumDic.items():
            progressBar.update()
            #
            setMaterialObjectSetConnect(compIndex, linkDatumLis)


#
def setMaterialObjectSetConnect(compIndex, linkDatumLis):
    nodepathString = maUuid.getObject(compIndex, fullPath=1)
    if nodepathString:
        # Clear >>> 01
        if linkDatumLis:
            setObjectCleanTransformShadingEngine(nodepathString)
            setObjectCleanShapeShadingEngine(nodepathString)
            # Link >>> 02
            isComponentLink = len(linkDatumLis) > 1
            #
            if not isComponentLink:
                componentObjectIndex, compMaterialIndex = linkDatumLis[0]
                shadingEngine = getMaterialShadingEngine(compMaterialIndex)
                setObjectAssignMaterial(nodepathString, None, shadingEngine)
            #
            else:
                for componentObjectIndex, compMaterialIndex in linkDatumLis:
                    shadingEngine = getMaterialShadingEngine(compMaterialIndex)
                    setObjectAssignMaterial(nodepathString, componentObjectIndex, shadingEngine)


#
def setObjectCleanShadingEngine(nodepathString):
    setObjectCleanTransformShadingEngine(nodepathString)
    setObjectCleanShapeShadingEngine(nodepathString)


#
def setObjectCleanShapeShadingEngine(nodepathString):
    shape = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
    shapeShadingEngines = maUtils._getNodeTargetNodeStringList(shape, appCfg.DEF_mya_type_shading_engine)
    if shapeShadingEngines:
        [cmds.sets(shape, remove=i) for i in shapeShadingEngines]


#
def setObjectCleanTransformShadingEngine(nodepathString):
    outputConnections = maUtils.getNodeOutputConnectionLis(nodepathString)
    if outputConnections:
        for sourceAttr, targetAttr in outputConnections:
            if sourceAttr.endswith('instObjGroups'):
                maUtils.setAttrDisconnect(sourceAttr, targetAttr)


#
def setObjectDefaultShadingEngine(nodepathString):
    shape = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
    shadingEngineLis = maUtils._getNodeTargetNodeStringList(shape, appCfg.DEF_mya_type_shading_engine)
    if not shadingEngineLis:
        cmds.sets(shape, forceElement='initialShadingGroup')


#
def setObjectsDefaultShadingEngine(componentObjectIndexes):
    for componentObjectIndex in componentObjectIndexes:
        nodepathString = maUuid.getObject(componentObjectIndex)
        setObjectDefaultShadingEngine(nodepathString)


#
def setObjectAssignMaterial(nodepathString, componentObjectIndex, shadingEngine):
    if componentObjectIndex is None:
        linkObject = maUtils._dcc_getNodShapeNodepathStr(nodepathString, 1)
    else:
        linkObject = nodepathString + componentObjectIndex
    #
    if maUtils._isAppExist(linkObject):
        if maUtils._isAppExist(shadingEngine):
            cmds.sets(linkObject, forceElement=shadingEngine)
            setCreateLightLink(shadingEngine)
        else:
            cmds.sets(linkObject, forceElement='initialShadingGroup')


#
def setCreateLightLink(shadingEngine):
    def getUsedConnectionIndex():
        for i in range(5000):
            if isUsedPartitionConnectionIndex(i) \
                    and isUsedObjectLinkConnectionIndex(i) \
                    and isUsedShadowObjectLinkConnectionIndex(i) \
                    and isUsedLightLinkConnectionIndex(i) \
                    and isUsedShadowLightLinkConnectionIndex(i):
                return i
    #
    def isUsedConnection(connection):
        boolean = False
        if cmds.objExists(connection):
            if not cmds.connectionInfo(connection, isDestination=1):
                boolean = True
        return boolean
    #
    def isUsedPartitionConnectionIndex(index):
        connection = appCfg.MaRenderPartition + '.sets[%s]' % index
        return isUsedConnection(connection)
    #
    def isUsedObjectLinkConnectionIndex(index):
        connection = appCfg.MaNodeName_LightLink + '.link[%s].object' % index
        return isUsedConnection(connection)
    #
    def isUsedShadowObjectLinkConnectionIndex(index):
        connection = appCfg.MaNodeName_LightLink + '.shadowLink[%s].shadowObject' % index
        return isUsedConnection(connection)
    #
    def isUsedLightLinkConnectionIndex(index):
        connection = appCfg.MaNodeName_LightLink + '.link[%s].light' % index
        return isUsedConnection(connection)
    #
    def isUsedShadowLightLinkConnectionIndex(index):
        connection = appCfg.MaNodeName_LightLink + '.shadowLink[%s].shadowLight' % index
        return isUsedConnection(connection)
    #
    def setMain():
        index = getUsedConnectionIndex()
        if index:
            # Debug ( Repeat )
            if not cmds.connectionInfo(shadingEngine + '.partition', isSource=1):
                cmds.connectAttr(shadingEngine + '.partition', appCfg.MaRenderPartition + '.sets[%s]' % index)
                cmds.connectAttr(shadingEngine + '.message', appCfg.MaNodeName_LightLink + '.link[%s].object' % index)
                cmds.connectAttr(shadingEngine + '.message', appCfg.MaNodeName_LightLink + '.shadowLink[%s].shadowObject' % index)
                cmds.connectAttr(appCfg.MaNodeName_DefaultLightSet + '.message', appCfg.MaNodeName_LightLink + '.link[%s].light' % index)
                cmds.connectAttr(appCfg.MaNodeName_DefaultLightSet + '.message', appCfg.MaNodeName_LightLink + '.shadowLink[%s].shadowLight' % index)
    #
    setMain()


#
def getAovNodeLis(renderer):
    aovNodes = []
    if renderer == prsConfigure.Utility.DEF_value_renderer_arnold:
        aovNodes = getArnoldAovNodeLis()
    elif renderer == prsConfigure.Utility.DEF_value_renderer_redshift:
        aovNodes = getRedshiftAovNodes()
    return aovNodes


# Get Arnold's Aov
def getArnoldAovNodeLis():
    lis = []
    if maUtils.isArnoldEnable():
        lis = maUtils._getNodeSourceNodeStringList('defaultArnoldRenderOptions', 'aiAOV')
    return lis


# Get Redshift's Aov
def getRedshiftAovNodes():
    lis = []
    if maUtils.isRedshiftEnable():
        lis = maUtils.getNodeLisByType('RedshiftAOV')
    return lis


#
def getAovNodesData(renderer):
    aovNodesData = bscMtdCore.orderedDict()
    if renderer == 'Arnold':
        aovNodesData = getArnoldAovNodesData()
    if renderer == 'Redshift':
        aovNodesData = getRedshiftAovNodesData()
    return aovNodesData


#
def getArnoldAovNodesData():
    dic = bscMtdCore.orderedDict()
    aovNodes = getArnoldAovNodeLis()
    if aovNodes:
        for aovNode in aovNodes:
            aovName = maUtils.getAttrDatum(aovNode, 'name')
            dic[aovNode] = aovName
    return dic


#
def getRedshiftAovNodesData():
    dic = bscMtdCore.orderedDict()
    aovNodes = getRedshiftAovNodes()
    if aovNodes:
        for aovNode in aovNodes:
            aovName = maUtils.getAttrDatum(aovNode, 'name')
            dic[aovNode] = aovName
    return dic


# noinspection PyUnresolvedReferences
def getArnoldOption():
    if prsMethods.Project.isMayaUsedArnoldRenderer():
        try:
            import mtoa.core as core
            #
            core.createOptions()
        except:pass


#
def setCreateAovNodeLink(aovNode, maxDepth=50):
    def getAovListAttr():
        aovListAttrs = ['%s.aovList[%s]' % ('defaultArnoldRenderOptions', i) for i in range(0, maxDepth)]
        for aovListAttr in aovListAttrs:
            if maUtils._isAppExist(aovListAttr):
                if not maAttr.isAttrDestination(aovListAttr):
                    return aovListAttr
    #
    def setMain():
        aovMessageAttr = aovNode + '.message'
        if maUtils._isAppExist(aovMessageAttr):
            if not maAttr.isAttrSource(aovMessageAttr):
                aovListAttr = getAovListAttr()
                if aovListAttr:
                    cmds.connectAttr(aovMessageAttr, aovListAttr)
    #
    setMain()


@dtbMtdCore.fncThreadSemaphoreModifier
def setRepairAovNodesLink():
    getArnoldOption()
    aovs = maUtils.getNodeLisByType('aiAOV')
    if aovs:
        [setCreateAovNodeLink(i) for i in aovs]


#
def setRepairArnoldAov(aovNodes=None):
    if not aovNodes:
        aovNodes = cmds.ls(type='aiAOV')
    #
    defDriverAttr = 'defaultArnoldDriver.message'
    defFilterAttr = 'defaultArnoldFilter.message'
    if aovNodes:
        for aovNode in aovNodes:
            outputDriverAttr = aovNode + '.outputs[0].driver'
            outputFilterAttr = aovNode + '.outputs[0].filter'
            inputConnections = maUtils.getNodeInputConnectionLis(aovNode)
            for inputAttr, outputAttr in inputConnections:
                if outputAttr == outputDriverAttr:
                    if inputAttr != defDriverAttr:
                        maUtils.setAttrDisconnect(inputAttr, outputAttr)
                        maUtils.setAttrConnect(defDriverAttr, outputDriverAttr)
                #
                if outputAttr == outputFilterAttr:
                    if inputAttr != defFilterAttr:
                        maUtils.setAttrDisconnect(inputAttr, outputAttr)
                        maUtils.setAttrConnect(defFilterAttr, outputFilterAttr)
            else:
                if not cmds.isConnected(defDriverAttr, outputDriverAttr):
                    cmds.connectAttr(defDriverAttr, outputDriverAttr)
                #
                if not cmds.isConnected(defFilterAttr, outputFilterAttr):
                    cmds.connectAttr(defFilterAttr, outputFilterAttr)


#
def getObjectsAttrData(objectLis):
    dic = bscMtdCore.orderedDict()
    #
    if objectLis:
        for nodepathString in objectLis:
            objectShape = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            renderAttrData = maAttr.getNodeRenderAttrData(objectShape)
            plugAttrData = maAttr.getNodePlugAttrData(objectShape)
            customAttrData = maAttr.getNodeUserDefAttrData(objectShape)
            dic[uniqueId] = renderAttrData, plugAttrData, customAttrData
    return dic


#
def setObjectsAttrsCreate(datumDic):
    if datumDic:
        # View Progress
        explain = u'''Set Material's Object Attribute(s)'''
        maxValue = len(datumDic)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for uniqueId, attrData in datumDic.items():
            progressBar.update()
            #
            nodepathString = maUuid.getObject(uniqueId)
            if nodepathString:
                setObjectAttrsCreate(nodepathString, attrData)


#
def setObjectAttrsCreate(nodepathString, attrData):
    if attrData:
        objectShape = maUtils._dcc_getNodShapeNodepathStr(nodepathString, 1)
        renderAttrData, plugAttrData, customAttrData = attrData
        if renderAttrData:
            maAttr.setNodeDefAttrByData(objectShape, renderAttrData)
        if plugAttrData:
            maAttr.setNodeDefAttrByData(objectShape, plugAttrData)
        if customAttrData:
            maAttr.setObjectUserDefinedAttrs(objectShape, customAttrData)


#
def setRefreshTextureColorSpace(textureNodes):
    if textureNodes:
        for i in textureNodes:
            colorSpace = maUtils.getAttrDatum(i, 'colorSpace')
            if not colorSpace == 'sRGB':
                maUtils.setAttrDatumForce_(i, 'ignoreColorSpaceFileRules', 1)


#
def setArnoldShaderCovert(nodepathString, texturePath):
    nodeTypeLis = [
        'aiStandardSurface'
    ]
    shadingEngineLis = _getNodeShadingEngineNodeStringList(nodepathString)
    if shadingEngineLis:
        for shadingEngine in shadingEngineLis:
            targetAttr0 = maUtils._toNodeAttr([shadingEngine, 'surfaceShader'])
            stringLis = maUtils.getInputNodeLisByAttr(targetAttr0)
            if stringLis:
                nodeName = stringLis[0]
                nodeType = maUtils._getNodeCategoryString(nodeName)
                if nodeType in nodeTypeLis:
                    sourceAttr0 = maUtils._toNodeAttr([nodeName, 'outColor'])
                    targetAttr1 = maUtils._toNodeAttr([shadingEngine, 'aiSurfaceShader'])
                    #
                    cmds.disconnectAttr(sourceAttr0, targetAttr0)
                    #
                    if not cmds.isConnected(sourceAttr0, targetAttr1):
                        cmds.connectAttr(sourceAttr0, targetAttr1)
                    #
                    colorShaderNodeName = shadingEngine + 'cls_colorShader'
                    if not cmds.objExists(colorShaderNodeName):
                        cmds.shadingNode('blinn', n=colorShaderNodeName, asShader=True)
                    #
                    sourceAttr2 = maUtils._toNodeAttr([colorShaderNodeName, 'outColor'])
                    cmds.connectAttr(sourceAttr2, targetAttr0)
                    #
                    if nodeType == 'aiStandardSurface':
                        inputAttr = maUtils._toNodeAttr([nodeName, 'baseColor'])
                        stringLis = maUtils.getInputAttrByAttr(inputAttr)
                        if stringLis:
                            textureNodeName = shadingEngine + 'CLS_color'
                            #
                            texture = texturePath + '/' + textureNodeName + '.jpg'
                            attr = stringLis[0]
                            cmds.convertSolidTx(
                                attr,
                                name=textureNodeName,
                                resolutionX=1024, resolutionY=1024,
                                samplePlane=1,
                                fileImageName=texture,
                                fileFormat='jpg'
                            )
                            #
                            cmds.connectAttr(textureNodeName + '.outColor', colorShaderNodeName + '.color')
