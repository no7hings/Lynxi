# coding=utf-8
import os
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscMtdCore, bscMethods, bscObjects

from LxPreset import prsConfigure, prsOutputs, prsMethods
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr
#
from LxDatabase import dbGet, dbBasic
#
from LxMaya.command import maUtils, maGeom, maAttr, maFur, maShdr, maTxtr, maUuid
#
none = ''


# Get Poly Mesh Evaluate ( Method )
def getMeshObjectEvaluate(objectLis, vertex, edge, face, triangle, uvcoord, area, worldArea, shell, boundingBox, showMode):
    # Dict { <Evaluate Name>: <Evaluate Data> }
    dic = bscMtdCore.orderedDict()
    used = [vertex, edge, face, triangle, uvcoord, area, worldArea, shell, boundingBox]
    # View Progress
    progressExplain = '''Read Mesh Evaluate Data'''
    maxValue = sum(used)
    progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
    # >>>> 01
    if vertex:
        progressBar.update('Vertex')
        dic['vertex'] = cmds.polyEvaluate(objectLis, vertex=1)
    # >>>> 02
    if edge:
        progressBar.update('Edge')
        dic['edge'] = cmds.polyEvaluate(objectLis, edge=1)
    # >>>> 03
    if face:
        progressBar.update('Face')
        dic['face'] = cmds.polyEvaluate(objectLis, face=1)
    # >>>> 04
    if triangle:
        progressBar.update('Triangle')
        dic['triangle'] = cmds.polyEvaluate(objectLis, triangle=1)
    # >>>> 05
    if uvcoord:
        progressBar.update('UV')
        dic['uvcoord'] = cmds.polyEvaluate(objectLis, uvcoord=1)
    # >>>> 06
    if area:
        progressBar.update('Area')
        dic['area'] = cmds.polyEvaluate(objectLis, area=1)
    # >>>> 07
    if worldArea:
        progressBar.update('World Area')
        dic['worldArea'] = cmds.polyEvaluate(objectLis, worldArea=1)
    # >>>> 08
    if shell:
        progressBar.update('Shell')
        dic['shell'] = cmds.polyEvaluate(objectLis, shell=1)
    # >>>> 09
    if boundingBox:
        progressBar.update('Bounding Box')
        dic['boundingBox'] = cmds.polyEvaluate(objectLis, boundingBox=1)
    return dic


#
def getAssetIndex(assetName):
    string = none
    #
    rootGroup = prsMethods.Asset.rootName(assetName)
    #
    if maUtils._isAppExist(rootGroup):
        data = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicIndexAttrLabel)
        if data:
            string = data
    return string


#
def getAssetInfo():
    lis = []
    keyword = prsOutputs.Util.basicUnitRootGroupLabel + prsOutputs.Util.basicGroupLabel
    rootGroups = cmds.ls('*%s' % keyword)
    if rootGroups:
        for rootGroup in rootGroups:
            if maUtils._isAppExist(rootGroup):
                if rootGroup.startswith(prsOutputs.Util.Lynxi_Prefix_Product_Asset):
                    assetCategory = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicClassAttrLabel)
                    assetName = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicNameAttrLabel)
                    assetVariant = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicVariantAttrLabel)
                    assetStage = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicStageAttrLabel)
                    assetIndex = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicIndexAttrLabel)
                    if assetIndex is not None:
                        data = assetIndex, assetCategory, assetName, assetVariant, assetStage
                        #
                        print '''assetIndex = '{}'\nassetCategory = '{}'\nassetName = '{}'\nassetVariant = '{}'\nassetStage = '{}'\n'''.format(
                            assetIndex,
                            assetCategory, assetName, assetVariant, assetStage
                        )
                        lis.append(data)
    return lis


# Get Nde_Geometry ( Data )
def getAstMeshObjects(assetName, key=0, namespace=none):
    # List [ <Nde_Geometry(Transfer)> ]
    meshObjects = []
    astModelGroup = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    #
    root = none
    if key == 0 and maUtils._isAppExist(astModelGroup):
        root = astModelGroup
    elif key == 0 and not maUtils._isAppExist(astModelGroup) and maUtils._isAppExist(astUnitModelProductGroup):
        root = astUnitModelProductGroup
    elif key == 1 and maUtils._isAppExist(astUnitModelProductGroup):
        root = astUnitModelProductGroup
    #
    if maUtils._isAppExist(root):
        meshObjects = maGeom.getMeshObjectsByGroup(root)
    return meshObjects


#
def getAstGeometryObjects(assetName, namespace=none):
    astModelGroup = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
    return maGeom.getGeometryObjectsByGroup(astModelGroup)


# Get Instance In Check Objects( Data )
def getInstanceObjectLis(objectLis):
    # Mark for Fix Later 2020 0114
    lis = []
    return lis


#
def getMeshesIsNormalLock(meshObjects):
    lis = [i for i in meshObjects if maGeom.getMeshObjectIsNormalLocked(i)]
    return lis


# Get Poly Meshes's Evaluate ( Data )
def getMeshObjectsEvaluateDic(objectLis, showMode=0):
    # Dict { <Poly Mesh> :
    #        List [ <Evaluate Info> ] }
    dic = bscMtdCore.orderedDict()
    if objectLis:
        count = len(objectLis)
        data = getMeshObjectEvaluate(
            objectLis,
            vertex=1, edge=1, face=1, triangle=1, uvcoord=1, area=1, worldArea=1, shell=1, boundingBox=1,
            showMode=showMode
        )
        box = data['boundingBox']
        #
        dic['geometries'] = count
        dic['vertex'] = data['vertex']
        dic['edge'] = data['edge']
        dic['face'] = data['face']
        dic['triangle'] = data['triangle']
        dic['uvcoord'] = data['uvcoord']
        dic['area'] = data['area']
        dic['worldArea'] = data['worldArea']
        dic['shell'] = data['shell']
        dic['axisX'] = box[0][1] + box[0][0]
        dic['horz'] = box[1][0]
        dic['widthX'] = box[0][1] - box[0][0]
        dic['heightY'] = box[1][1] - box[1][0]
        dic['widthZ'] = box[2][1] - box[2][0]
    return dic


#
def getMaterialEvaluateData(objectLis, showMode=0):
    dic = bscMtdCore.orderedDict()
    if objectLis:
        evaluateData = maShdr.getMaterialEvaluateData(objectLis)
        #
        textureNodeLis = maShdr.getTextureNodeLisByObject(objectLis)
        textures = maTxtr.getTextureByTextureNodes(textureNodeLis)
        subEvaluateData = {'textureNode': len(textureNodeLis), 'texture': len(textures), 'averagePixel': 2048}
        #
        dic = evaluateData.copy()
        dic.update(subEvaluateData)
    return dic


# Get Objects Transformation (Data)
def getObjectNonZeroTransAttrDic(objectLis):
    dic = bscMtdCore.orderedDict()
    #
    channelLabel = [
        'translate',
        'rotate',
        'scale',
        'pivot'
    ]
    channelSet = [
        '.translate',
        '.rotate',
        '.scale',
        '.rotatePivot'
    ]
    if objectLis:
        for nodepathString in objectLis:
            subDic = bscMtdCore.orderedDict()
            for seq, channel in enumerate(channelSet):
                subDic[channelLabel[seq]] = cmds.getAttr(nodepathString + channel)[0]
                dic[nodepathString] = subDic
    return dic


#
def filterObjectHistoryNodeDic(objectLis):
    dic = bscMtdCore.orderedDict()
    if objectLis:
        for nodepathString in objectLis:
            stringLis = cmds.listHistory(nodepathString, pruneDagObjects=1)
            if stringLis:
                for i in stringLis:
                    typeData = cmds.ls(i, showType=1, long=1)
                    dic.setdefault(nodepathString, []).append(typeData)
    return dic


# List [ <Output Connection Nde_Node> ]
def getOutputNode(node, assetCategory=none):
    outputNodes = cmds.listConnections(node, destination=1, source=0, type=assetCategory)
    return outputNodes


# Get Arnold's Aov
def getArnoldAovNodeLis():
    # List [ <Aov> ]
    arnoldAovs = []
    if maUtils.isRedshiftEnable():
        arnoldAovs = maUtils._getNodeSourceNodeStringList('defaultArnoldRenderOptions', 'aiAOV')
    return arnoldAovs


# Get Redshift's Aov
def getRedshiftAovNodes():
    # List [ <Aov> ]
    redshiftAovs = []
    if maUtils.isRedshiftEnable():
        redshiftAovs = maUtils.getNodeLisByType('RedshiftAOV')
    return redshiftAovs


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


# Get Objects Shading Group
def getShadingGroupsByObjects(objectLis):
    # List [ <Shading Engine> ]
    lis = []
    DEF_mya_default_shading_engine_list = ['initialShadingGroup', 'initialParticleSE', 'defaultLightSet', 'defaultObjectSet']
    for nodepathString in objectLis:
        shape = maUtils._dcc_getNodShapeNodepathStr(nodepathString, 1)
        shadingGroups = getOutputNode(shape, 'shadingEngine')
        if shadingGroups:
            [lis.append(shadingGroup) for shadingGroup in shadingGroups if shadingGroup not in DEF_mya_default_shading_engine_list]

    lisR = bscMethods.List.cleanupTo(lis)
    lisR.sort()
    return lisR


#
def getAstUnitModelExtraData(assetName, namespace=none):
    extraData = {
        prsConfigure.Product.DEF_key_info_attribute: getAstUnitModelBridgeAttrData(assetName, namespace),
        prsConfigure.Product.DEF_key_info_connection: getAstUnitModelReferenceConnectionData(assetName, namespace)
    }
    return extraData


#
def getAstUnitModelBridgeAttrData(assetName, namespace=none):
    def getBranch(nodepathString):
        objectDefinedAttrData = maAttr.getNodeDefAttrDatumLis(nodepathString)
        objectCustomAttrData = maAttr.getNodeUserDefAttrData(nodepathString)
        dic[astUnitModelBridgeGroup + nodepathString.split(astUnitModelBridgeGroup)[-1]] = objectDefinedAttrData, objectCustomAttrData
    #
    dic = {}
    #
    astUnitModelBridgeGroup = assetPr.astUnitModelBridgeGroupName(assetName, namespace)
    if maUtils._isAppExist(astUnitModelBridgeGroup):
        getBranch(astUnitModelBridgeGroup)
    return dic


#
def getAstUnitModelReferenceConnectionData(assetName, namespace=none):
    def getBranch(nodepathString):
        objectShape = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
        outputConnectLis = maUtils.getNodeOutputConnectionLis(objectShape)
        if outputConnectLis:
            for sourceAttr, targetAttr in outputConnectLis:
                if sourceAttr.endswith('.message') and targetAttr.endswith('.referenceObject'):
                    dic.setdefault(nodepathString.split(astUnitRoot)[-1], []).append((sourceAttr, targetAttr))
        #
        objectShapeName = maUtils._nodeString2nodename_(objectShape)
        maUtils.setAttrStringDatumForce_(nodepathString, prsConfigure.Product.DEF_key_attribute_shapename, objectShapeName)
    #
    dic = {}
    #
    astUnitRoot = prsMethods.Asset.rootName(assetName)
    astUnitModelReferenceGroup = assetPr.astUnitModelReferenceGroupName(assetName, namespace)
    #
    objectLis = maUtils.getChildObjectsByRoot(astUnitModelReferenceGroup, appCfg.DEF_mya_type_mesh)
    if objectLis:
        # View Progress
        progressExplain = u'''Read Connection Data'''
        maxValue = len(objectLis)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for i in objectLis:
            progressBar.update()
            getBranch(i)
    return dic


#
def getAstUnitRigExtraData(assetName):
    astUnitRigBridgeGroup = assetPr.astUnitRigBridgeGroupName(assetName)
    alembicAttrData = getAstAlembicAttrData(astUnitRigBridgeGroup)
    extraData = {
        prsConfigure.Product.DEF_key_info_abcattribute: alembicAttrData
    }
    return extraData


#
def getAstAlembicAttrData(root):
    lis = []
    children = maUtils.getRootCompose(root)
    if children:
        for i in children:
            data = maAttr.getNodeUserDefAttrNameLis(i)
            if data:
                lis.extend(data)
    return lis


#
def getFurObjects(assetName, namespace=none):
    lis = []
    yetiObjects = getYetiObjects(assetName, namespace)
    lis.extend(yetiObjects)
    pfxHairObjects = getPfxHairObjects(assetName, namespace)
    lis.extend(pfxHairObjects)
    nurbsHairObjects = getAstCfxNurbsHairObjects(assetName, namespace)
    lis.extend(nurbsHairObjects)
    return lis


#
def getAstFurShaderObjects(assetName, namespace=none):
    lis = []
    yetiObjects = getYetiObjects(assetName, namespace)
    lis.extend(yetiObjects)
    nurbsHairObjects = getAstCfxNurbsHairObjects(assetName, namespace)
    lis.extend(nurbsHairObjects)
    return lis


# Get Yeti Nde_Node
def getYetiObjects(assetName, namespace=none):
    maGroup = assetPr.yetiNodeGroupName(assetName, namespace)
    yetiObjects = maUtils.getChildObjectsByRoot(maGroup, 'pgYetiMaya', fullPath=True)
    return yetiObjects


# Get Yeti Nde_Node
def getYetiShapeLis(assetName, namespace=none):
    maGroup = assetPr.yetiNodeGroupName(assetName, namespace)
    yetiNodes = maUtils.getChildShapesByRoot(maGroup, 'pgYetiMaya', 1)
    return yetiNodes


#
def getPfxHairObjects(assetName, namespace=none):
    maGroup = assetPr.astPfxHairNodeGroupName(assetName, namespace)
    pfxHairObjects = maUtils.getChildObjectsByRoot(maGroup, 'pfxHair', fullPath=True)
    return pfxHairObjects


#
def getAstCfxGrowSourceObjectLis(assetName, namespace=none):
    groupName = assetPr.astUnitCfxGrowSourceObjectGroupName(assetName, namespace)
    return maUtils.getNodeChildLis(groupName)


#
def getAstCfxGrowSourceConnectionDic(assetName, namespace=none):
    dic = bscMtdCore.orderedDict()
    objectPathLis = getAstCfxGrowSourceObjectLis(assetName, namespace)
    if objectPathLis:
        for nodepathString in objectPathLis:
            sourceObject = maUtils.getAttrDatum(nodepathString, 'growSource')
            dic[sourceObject] = nodepathString
    return dic


#
def getAstSolverGrowSourceObjectLis(assetName, namespace):
    groupName = assetPr.astUnitSolverGrowSourceObjectGroupName(assetName, namespace)
    return maUtils.getNodeChildLis(groupName)


#
def getAstSolverGrowSourceConnectionDic(assetName, namespace=none):
    dic = bscMtdCore.orderedDict()
    objectPathLis = getAstSolverGrowSourceObjectLis(assetName, namespace)
    if objectPathLis:
        for nodepathString in objectPathLis:
            sourceObject = maUtils.getAttrDatum(nodepathString, 'growSource')
            dic[sourceObject] = nodepathString
    return dic


# Get Yeti Nde_Node Data
def getYetiNodeData(assetCategory, assetName):
    dic = bscMtdCore.orderedDict()
    yetiObjects = getYetiObjects(assetName)
    if yetiObjects:
        for yetiObject in yetiObjects:
            subDic = bscMtdCore.orderedDict()
            groomObjects = maUtils.getYetiGroomDic(yetiObject)
            if groomObjects:
                for groomObject in groomObjects:
                    subDic.setdefault('groom', []).append(groomObject)
            # Grow
            growObjects = maUtils.getYetiGrowDic(yetiObject)
            if growObjects:
                for growObject in growObjects:
                    subDic.setdefault('grow', []).append(growObject)
                    # Reference
                    referenceObjects = maUtils.getYetiRefObject(growObject)
                    if referenceObjects:
                        for referenceObject in referenceObjects:
                            subDic.setdefault('reference', []).append('%s|%s' % (growObject, referenceObject))
            # Map
            mapObjects = maUtils.getYetiMapDic(yetiObject)
            if mapObjects:
                for mapObject in mapObjects:
                    subDic.setdefault('map', []).append(mapObject)
            dic[yetiObject] = subDic
    return dic


#
def getAstCfxNurbsHairObjects(assetName, namespace=none):
    maGroup = assetPr.astCfxNurbsHairNodeGroupName(assetName, namespace)
    return maUtils.getChildObjectsByRoot(maGroup, appCfg.MaNodeType_Plug_NurbsHair)


#
def getAstCfxNurbsHairSolverCheckData(assetName, namespace=none):
    dic = bscMtdCore.orderedDict()
    objectPaths = getAstCfxNurbsHairObjects(assetName, namespace)
    if objectPaths:
        for objectPath in objectPaths:
            dic[objectPath] = maFur.isNhrHasSolGuideObject(objectPath)
    return dic


#
def getAstUnitSolverNhrGuideObjects(assetName, namespace=none):
    groupStr = assetPr.astUnitRigSolNhrGuideObjectGroupName(assetName, namespace)
    if maUtils._isAppExist(groupStr):
        maUtils.setNodeOutlinerRgb(groupStr, 1, .5, 1)
    return maUtils.getChildObjectsByRoot(groupStr, prsOutputs.Util.maNurbsHairInGuideCurvesNode, fullPath=True)


#
def getAstUnitCfxNhrGuideObjects(assetName, namespace=none):
    groupStr = assetPr.astUnitCfxNhrGuideObjectGroupName(assetName, namespace)
    if maUtils._isAppExist(groupStr):
        maUtils.setNodeOutlinerRgb(groupStr, 1, .25, .25)
    return maUtils.getChildObjectsByRoot(groupStr, [appCfg.DEF_mya_type_mesh, appCfg.DEF_mya_type_nurbs_surface, appCfg.DEF_mya_type_nurbs_curve], fullPath=True)


#
def getAstSolverFurGuideCurveGroups(assetName, namespace=none):
    maGroup = assetPr.astUnitRigSolNhrCurveObjectGroupName(assetName, namespace)
    return maUtils.getChildGroupLisByGroup(maGroup, fullPath=True)


#
def getAstSolverGuideCheckData(assetName, namespace=none):
    dic = bscMtdCore.orderedDict()
    nhrGuideObjects = getAstUnitSolverNhrGuideObjects(assetName, namespace)
    if nhrGuideObjects:
        for nhrGuideObject in nhrGuideObjects:
            dic[nhrGuideObject] = maFur.getNhrObjectsByGuide(nhrGuideObject)
    return dic


#
def getAstUnitRigSolExtraData(assetName, namespace=none):
    dic = {
        prsConfigure.Product.DEF_key_info_connection: getAstUnitSolverConnectionData(assetName, namespace),
        prsConfigure.Product.DEF_key_info_nhrconnection: getAstUnitSolverNhrConnectionData(assetName, namespace)
    }
    return dic


#
def getAstUnitSolverConnectionData(assetName, namespace=none):
    def getBranch(nodepathString):
        objectShape = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
        inputConnections = maUtils.getNodeInputConnectionLis(objectShape)
        if inputConnections:
            for sourceAttr, targetAttr in inputConnections:
                dic.setdefault(nodepathString.split(astUnitRoot)[-1], []).append((sourceAttr, targetAttr))
        #
        outputConnectLis = maUtils.getNodeOutputConnectionLis(objectShape)
        if outputConnectLis:
            for sourceAttr, targetAttr in outputConnectLis:
                dic.setdefault(nodepathString.split(astUnitRoot)[-1], []).append((sourceAttr, targetAttr))
    #
    dic = {}
    #
    astUnitRoot = prsMethods.Asset.rootName(assetName)
    #
    nodepathStrings = getAstUnitSolverNhrGuideObjects(assetName, namespace)
    if nodepathStrings:
        # View Progress
        progressExplain = u'''Read Connection Data'''
        maxValue = len(nodepathStrings)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for i in nodepathStrings:
            progressBar.update()
            getBranch(i)
    return dic


#
def getAstUnitSolverNhrConnectionData(assetName, namespace=none):
    def getBranch(nodepathString):
        objectShape = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
        outputConnectLis = maUtils.getNodeOutputConnectionLis(objectShape)
        if outputConnectLis:
            for sourceAttr, targetAttr in outputConnectLis:
                if sourceAttr.endswith('.message') and targetAttr.endswith('.scatterObj'):
                    dic.setdefault(nodepathString.split(astUnitRoot)[-1], []).append((sourceAttr, targetAttr))
    #
    dic = {}
    #
    astUnitRoot = prsMethods.Asset.rootName(assetName)
    #
    nodepathStrings = getAstUnitCfxNhrGuideObjects(assetName, namespace)
    if nodepathStrings:
        # View Progress
        progressExplain = u'''Read Connection Data'''
        maxValue = len(nodepathStrings)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for i in nodepathStrings:
            progressBar.update()
            getBranch(i)
    #
    return dic


#
def getAstUnitRigSolAttributeData(assetName, namespace=none):
    def getBranch(nodepathString):
        shapePath = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
        shapeDefinedAttrData = maAttr.getNodeDefAttrDatumLis(shapePath)
        shapeCustomAttrData = maAttr.getNodeUserDefAttrData(nodepathString)
        dic[rigSolLinkGroup + nodepathString.split(rigSolLinkGroup)[-1]] = shapeDefinedAttrData, shapeCustomAttrData
    #
    dic = bscMtdCore.orderedDict()
    rigSolLinkGroup = assetPr.astUnitRigSolFurSubGroupName(assetName)
    #
    objectPaths = getAstUnitSolverNhrGuideObjects(assetName, namespace)
    if objectPaths:
        [getBranch(i) for i in objectPaths]

    return dic


#
def getTextureDatumLis(textureNode, textureString, texturePathDic, textureNodeDic, textureMtimestampDic):
    if textureString:
        textureFilePath = bscMethods.OsFile.dirname(textureString)
        #
        textureFileBasename = bscMethods.OsFile.basename(textureString)
        # Texture Path
        texturePathDic.setdefault(textureFilePath, []).append(textureFileBasename)
        #
        if '<udim>' in textureString.lower():
            subTextureFileLis = maTxtr.getOsTextureUdimLis(textureString)
            if subTextureFileLis:
                subTextureDatumLis = []
                for subTextureFile in subTextureFileLis:
                    subTextureFileBasename = os.path.basename(subTextureFile)
                    timestamp = bscMethods.OsFile.mtimestamp(subTextureFile)
                    if not (subTextureFileBasename, timestamp) in subTextureDatumLis:
                        subTextureDatumLis.append((subTextureFileBasename, timestamp))
                #
                textureMtimestampDic[textureFileBasename] = subTextureDatumLis
            else:
                textureMtimestampDic[textureFileBasename] = None
        elif '<f>' in textureString.lower():
            subTextureFileLis = maTxtr.getOsTextureSequenceLis(textureString)
            if subTextureFileLis:
                subTextureDatumLis = []
                for subTextureFile in subTextureFileLis:
                    subTextureFileBasename = os.path.basename(subTextureFile)
                    timestamp = bscMethods.OsFile.mtimestamp(subTextureFile)
                    if not (subTextureFileBasename, timestamp) in subTextureDatumLis:
                        subTextureDatumLis.append((subTextureFileBasename, timestamp))
                #
                textureMtimestampDic[textureFileBasename] = subTextureDatumLis
            else:
                textureMtimestampDic[textureFileBasename] = None
        else:
            if bscMethods.OsFile.isExist(textureString):
                timestamp = bscMethods.OsFile.mtimestamp(textureString)
                textureMtimestampDic[textureFileBasename] = timestamp
            else:
                textureMtimestampDic[textureFileBasename] = None
        # Texture Nde_Node
        textureNodeDic.setdefault(textureFileBasename, []).append(textureNode)


# Get Texture's Datum List Link
def getTextureStatisticsDic(objectLis):
    dic = bscMtdCore.orderedDict()
    #
    texturePathDic = bscMtdCore.orderedDict()
    #
    textureMtimestampDic = bscMtdCore.orderedDict()
    textureNodeDic = bscMtdCore.orderedDict()
    #
    textureNodeLis = maShdr.getTextureNodeLisByObject(objectLis)
    if textureNodeLis:
        # View Progress
        progressExplain = '''Read Data'''
        maxValue = len(textureNodeLis)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for textureNode in textureNodeLis:
            # In Progress
            progressBar.update()
            textureString = maTxtr.getTextureNodeAttrData(textureNode)
            getTextureDatumLis(textureNode, textureString, texturePathDic, textureNodeDic, textureMtimestampDic)
    #
    for k, v in texturePathDic.items():
        for i in bscMethods.List.cleanupTo(v):
            dic.setdefault(k, []).append((i, textureMtimestampDic[i], textureNodeDic[i]))
    return dic


# Str <Object's Volume>
def getVolume(nodepathString):
    box = cmds.polyEvaluate(nodepathString, boundingBox=1)
    volume = (box[0][1] - box[0][0]) * (box[1][1] - box[1][0]) * (box[2][1] - box[2][0])
    return volume


#
def getMeshObjectsConstantDic(assetName, namespace=none):
    infoConfig = ['hierarchy', 'geometry', 'geometryShape', 'map', 'mapShape']
    dic = bscMtdCore.orderedDict()
    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    meshesInformation = maGeom.getGeometryObjectsInfo(astUnitModelProductGroup)
    for seq, i in enumerate(infoConfig):
        dic[i] = meshesInformation[seq]
    return dic


#
def getMeshConstant(uniqueId, localInfoDic, serverInfoDic):
    pathCheck = False
    geomCheck = False
    geomShapeCheck = False
    mapCheck = False
    mapShapeCheck = False
    if uniqueId in localInfoDic.keys() and uniqueId in serverInfoDic:
        localInfos = localInfoDic[uniqueId]
        serverInfos = serverInfoDic[uniqueId]
        pathCheck = localInfos[0] == serverInfos[0]
        geomCheck = localInfos[1] == serverInfos[1]
        geomShapeCheck = localInfos[2] == serverInfos[2]
        mapCheck = localInfos[3] == serverInfos[3]
        mapShapeCheck = localInfos[4] == serverInfos[4]
    return pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck


#
def getAstGeometryObjectsConstantData(assetIndex, assetCategory, assetName, namespace):
    totalArray = []
    pathChangedArray = []
    geomChangedArray = []
    geomShapeChangedArray = []
    mapChangedArray = []
    mapShapeChangedArray = []
    #
    meshRoot = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
    if maUtils._isAppExist(meshRoot):
        localInfoDic = maGeom.getGeometryObjectsInfoDic(meshRoot)
        #
        serverInfoDic = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        #
        if localInfoDic and serverInfoDic:
            unionUniqueInfoDic = localInfoDic.copy()
            unionUniqueInfoDic.update(serverInfoDic)
            # View Progress
            progressExplain = '''Read Asset ( Mesh ) Data'''
            maxValue = len(unionUniqueInfoDic)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for uniqueId in unionUniqueInfoDic:
                progressBar.update()
                #
                totalArray.append(uniqueId)
                pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck = getMeshConstant(uniqueId, localInfoDic, serverInfoDic)
                if not pathCheck:
                    pathChangedArray.append(uniqueId)
                if not geomCheck:
                    geomChangedArray.append(uniqueId)
                if not geomShapeCheck:
                    geomShapeChangedArray.append(uniqueId)
                if not mapCheck:
                    mapChangedArray.append(uniqueId)
                if not mapShapeCheck:
                    mapShapeChangedArray.append(uniqueId)
    #
    return totalArray, pathChangedArray, geomChangedArray, geomShapeChangedArray, mapChangedArray, mapShapeChangedArray


#
def getAstMeshObjectsConstantData(assetIndex, assetCategory, assetName, namespace):
    totalArray = []
    pathChangedArray = []
    geomChangedArray = []
    geomShapeChangedArray = []
    mapChangedArray = []
    mapShapeChangedArray = []
    #
    meshRoot = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
    if maUtils._isAppExist(meshRoot):
        localInfoDic = maGeom.getMeshObjectsInfoDic(meshRoot)
        #
        serverInfoDic = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        #
        if localInfoDic and serverInfoDic:
            unionUniqueInfoDic = localInfoDic.copy()
            unionUniqueInfoDic.update(serverInfoDic)
            # View Progress
            progressExplain = '''Read Asset ( Mesh ) Data'''
            maxValue = len(unionUniqueInfoDic)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for uniqueId in unionUniqueInfoDic:
                progressBar.update()
                #
                totalArray.append(uniqueId)
                pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck = getMeshConstant(uniqueId, localInfoDic,
                                                                                                serverInfoDic)
                if not pathCheck:
                    pathChangedArray.append(uniqueId)
                if not geomCheck:
                    geomChangedArray.append(uniqueId)
                if not geomShapeCheck:
                    geomShapeChangedArray.append(uniqueId)
                if not mapCheck:
                    mapChangedArray.append(uniqueId)
                if not mapShapeCheck:
                    mapShapeChangedArray.append(uniqueId)
    #
    return totalArray, pathChangedArray, geomChangedArray, geomShapeChangedArray, mapChangedArray, mapShapeChangedArray


#
def getObjectSetDic(data):
    dic = bscMtdCore.orderedDict()
    if data:
        for objectUniqueId, linkDataArray in data.items():
            for objIndex, materialUniqueId in linkDataArray:
                dic.setdefault(materialUniqueId, []).append(objectUniqueId + objIndex)
    return dic


#
def getLocalMeshSetData(objectLis):
    data = maShdr.getShaderObjectsObjSetDic(objectLis)
    return getObjectSetDic(data)


#
def getServerMeshSetData(projectName, assetName, assetVariant):
    assetIndex = getAssetIndex(assetName)
    uniqueIds = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
    modelIndexKey = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    directory = prsOutputs.Database.assetMaterialObjectSet
    data = dbBasic.dbCompDatumDicRead(uniqueIds, modelIndexKey, directory)
    return getObjectSetDic(data)


#
def setMaterialConstant(uniqueId, localInfoDic, serverInfoDic, localMeshSetData, serverMeshSetData):
    composeCheck = False
    attributeCheck = False
    relationCheck = False
    objectSetCheck = False
    if uniqueId in localInfoDic.keys() and uniqueId in serverInfoDic:
        localInfos = localInfoDic[uniqueId]
        serverInfos = serverInfoDic[uniqueId]
        composeCheck = localInfos[0] == serverInfos[0]
        attributeCheck = localInfos[1] == serverInfos[1]
        relationCheck = localInfos[2] == serverInfos[2]
    if uniqueId in localMeshSetData.keys() and uniqueId in serverMeshSetData:
        localMeshSet = localMeshSetData[uniqueId]
        serverMeshSet = serverMeshSetData[uniqueId]
        localMeshSet.sort()
        serverMeshSet.sort()
        objectSetCheck = localMeshSet == serverMeshSet
    return composeCheck, attributeCheck, relationCheck, objectSetCheck


#
def getMaterialsConstantData(assetIndex, projectName, assetCategory, assetName, assetVariant, namespace=none):
    totalArray = []
    composeChangedArray = []
    attributeChangedArray = []
    relationChangedArray = []
    objectSetChangedArray = []
    #
    shaderGeomObjects = getAstMeshObjects(assetName, 1)
    materials = maShdr.getObjectsMaterials(shaderGeomObjects)
    localInfoDic = maShdr.getMaterialsInformationData(materials)
    modelIndexKey = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
    serverInfoDic = dbGet.getDbMaterialIndexData(modelIndexKey)
    localMeshSetData = getLocalMeshSetData(shaderGeomObjects)
    serverMeshSetData = getServerMeshSetData(projectName, assetName, assetVariant)
    #
    if localInfoDic and serverInfoDic:
        unionUniqueInfoData = localInfoDic.copy()
        unionUniqueInfoData.update(serverInfoDic)
        # View Progress
        progressExplain = '''Read Data'''
        maxValue = len(unionUniqueInfoData)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for uniqueId in unionUniqueInfoData:
            progressBar.update()
            #
            totalArray.append(uniqueId)
            composeCheck, attributeCheck, relationCheck, objectSetCheck = setMaterialConstant(uniqueId, localInfoDic, serverInfoDic, localMeshSetData, serverMeshSetData)
            if not composeCheck:
                composeChangedArray.append(uniqueId)
            if not attributeCheck:
                attributeChangedArray.append(uniqueId)
            if not relationCheck:
                relationChangedArray.append(uniqueId)
            if not objectSetCheck:
                objectSetChangedArray.append(uniqueId)
    #
    return totalArray, composeChangedArray, attributeChangedArray, relationChangedArray, objectSetChangedArray


#
def getErrorTransforms(assetName):
    lis = []
    #
    group = prsMethods.Asset.modelLinkGroupName(assetName)
    #
    transforms = maUtils.getChildTransformLisByGroup(group)
    for transform in transforms:
        mainShapes = maUtils.getMainShapes(transform)
        if not mainShapes:
            lis.append(transform)
    return lis


#
def getMeshesCompIndexForce(assetIndex, meshObjects):
    uniqueIds = []
    if meshObjects:
        for mesh in meshObjects:
            uniqueId = maUuid._getNodeUniqueIdString(mesh)
            uniqueIds.append(uniqueId)
    #
    if uniqueIds:
        nonExistsUniqueIds = dbGet.getNonExistsDbMeshCompIndex(assetIndex, uniqueIds)
        if nonExistsUniqueIds:
            for currentUniqueId in nonExistsUniqueIds:
                newUniqueId = maUuid.getUuid()
                if currentUniqueId != newUniqueId:
                    maUuid.setRefreshMayaUniqueId(currentUniqueId, newUniqueId)


#
def getFurCompIndexForce(dbSubIndex, furObjects):
    uniqueIds = []
    if furObjects:
        for furObject in furObjects:
            uniqueId = maUuid._getNodeUniqueIdString(furObject)
            uniqueIds.append(uniqueId)
    #
    if uniqueIds:
        nonExistsUniqueIds = dbGet.getNonExistsDbFurCompIndex(dbSubIndex, uniqueIds)
        if nonExistsUniqueIds:
            for currentUniqueId in nonExistsUniqueIds:
                newUniqueId = maUuid.getUuid()
                if currentUniqueId != newUniqueId:
                    maUuid.setRefreshMayaUniqueId(currentUniqueId, newUniqueId)


#
def getMaterialCompIndexesForce(subIndex, materials):
    uniqueIds = []
    if materials:
        for material in materials:
            uniqueId = maUuid._getNodeUniqueIdString(material)
            uniqueIds.append(uniqueId)
    #
    if uniqueIds:
        nonExistsUniqueIds = dbGet.getNonExistsDbMaterialComp(subIndex, uniqueIds)
        if nonExistsUniqueIds:
            for currentUniqueId in nonExistsUniqueIds:
                newUniqueId = maUuid.getUuid()
                if currentUniqueId != newUniqueId:
                    maUuid.setRefreshMayaUniqueId(currentUniqueId, newUniqueId)


#
def getAovCompIndexesForce(subIndex, aovs):
    uniqueIds = []
    if aovs:
        for aov in aovs:
            uniqueId = maUuid._getNodeUniqueIdString(aov)
            uniqueIds.append(uniqueId)
    #
    if uniqueIds:
        nonExistsUniqueIds = dbGet.getNonExistsDbAovComp(subIndex, uniqueIds)
        if nonExistsUniqueIds:
            for currentUniqueId in nonExistsUniqueIds:
                newUniqueId = maUuid.getUuid()
                if currentUniqueId != newUniqueId:
                    maUuid.setRefreshMayaUniqueId(currentUniqueId, newUniqueId)


#
def getAstMeshConstantData(assetName, namespace=none):
    dic = bscMtdCore.orderedDict()
    #
    geometryObjects = getAstMeshObjects(assetName, 1, namespace)
    if geometryObjects:
        dic = getMeshObjectsEvaluateDic(geometryObjects)
        subData = getMeshObjectsConstantDic(assetName, namespace)
        for k, v in subData.items():
            dic[k] = v
    return dic
