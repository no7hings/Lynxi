# coding=utf-8
import glob
# noinspection PyUnresolvedReferences
import maya.mel as mel
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscMtdCore, bscMethods, bscObjects
#
from LxCore.config import appCfg
#
from LxPreset import prsOutputs, prsMethods
#
from LxCore.preset.prod import assetPr
#
from LxMaya.command import maUtils, maFile, maUuid, maAttr, maObj, maGeom, maGeomCache
#
from LxDatabase.data import datHash
#
inShapeLabel = prsOutputs.Util.inShapeLabel
#
astCfxGrowSourceGroupLabel = prsOutputs.Util.astCfxGrowSourceGroupLabel
astCfxGrowSourceAttrLabel = prsOutputs.Util.astCfxGrowSourceAttrLabel
#
cacheAttrLabel = prsOutputs.Util.cacheAttrLabel
cacheUpdateAttrLabel = prsOutputs.Util.cacheUpdateAttrLabel
assetAttrLabel = prsOutputs.Util.assetAttrLabel
assetUpdateAttrLabel = prsOutputs.Util.assetUpdateAttrLabel
#
mayaVersion = maUtils.getMayaVersion()
#
origLabel = 'Orig'
basicSetLabel = 'Set'
#
none = ''


#
def getFurNodeName(furObject):
    splitKey = '_'
    if maUtils.getTransformType(furObject) == 'pgYetiMaya':
        splitKey = prsOutputs.Util.astYetiNodeGroupLabel
    if maUtils.getTransformType(furObject) == 'pfxHair':
        splitKey = prsOutputs.Util.astPfxHairGroupLabel
    furNodeName = (furObject.split('|')[-1].split(':')[-1]).split(splitKey)[-1][1:]
    return furNodeName


#
def getFurMapAttrData(furMapNode):
    string = none
    nodeType = maUtils._getNodeCategoryString(furMapNode)
    if nodeType == appCfg.MaNurbsHairCacheType:
        attr = furMapNode + '.' + 'cacheFile'
        string = maUtils.getAttrDatum(attr) or none
    #
    return string


#
def setFurMapAttrData(furMapNode, furMapFile):
    nodeType = maUtils._getNodeCategoryString(furMapNode)
    if nodeType == appCfg.MaNurbsHairCacheType:
        if bscMethods.OsFile.isExist(furMapFile):
            ext = bscMethods.OsFile.ext(furMapFile)
            if ext != '.nhr':
                base, ext = bscMethods.OsFile.toExtSplit(furMapFile)
                newFurMapFile = base + '.nhr'
                # Use Copy
                bscMethods.OsFile.copyTo(furMapFile, newFurMapFile)
            else:
                newFurMapFile = furMapFile
            #
            maUtils.setAttrDatumForce_(furMapNode, appCfg.MaNurbsHairCacheModeAttrName, appCfg.MaNurbsHairSolverModeIndexDic['Read'])
            maUtils.setAttrStringDatum(furMapNode, appCfg.MaNurbsHairCacheFileAttrName, newFurMapFile)


#
def getFurObjectLabel(furObjectPath, assetName):
    furNodeName = (furObjectPath.split('|')[-1].split(':')[-1]).split(assetName)[-1][1:]
    return furNodeName


#
def getYetiGuideHairSystems(yetiObject):
    lis = []
    yetiNode = maUtils._getNodeShapeNodeString(yetiObject)
    guideSets = maUtils.getInputObjectsByAttrName(yetiNode, '.guideSets')
    if guideSets:
        for guideSet in guideSets:
            if maUtils._isAppExist(guideSet):
                curves = maUtils.getInputObjectsByAttrName(guideSet, '.dagSetMembers')
                for curve in curves:
                    if maUtils._isAppExist(curve):
                        curvePath = maUtils._getNodeFullpathNameString(curve)
                        curveShape = maUtils._getNodeShapeNodeString(curvePath, 1)
                        follicles = maUtils.getInputObjectsByAttrName(curveShape, '.create')
                        if follicles:
                            follicle = follicles[0]
                            follicleShape = maUtils._getNodeShapeNodeString(follicle, 1)
                            #
                            hairSystems = maUtils.getInputObjectsByAttrName(follicleShape, '.currentPosition')
                            for hairSystem in hairSystems:
                                if not hairSystem in lis:
                                    lis.append(hairSystem)
    return lis


#
def setYetiNodeWriteCache(fileString_, yetiNode, startFrame, endFrame, sample=3, isUpdateViewport=True, isGeneratePreview=True):
    bscMethods.OsFile.createDirectory(fileString_)
    # Turn off Use Cache
    maUtils.setAttrDatumForce_(yetiNode, 'fileMode', False)
    #
    cmds.pgYetiCommand(
        yetiNode,
        writeCache=fileString_,
        range=(startFrame, endFrame),
        samples=sample,
        updateViewport=isUpdateViewport,
        generatePreview=isGeneratePreview
    )
    #
    maUtils.setCurrentFrame(startFrame)


#
def setYetiObjectsWriteCache(yetiObjects, yetiCaches, startFrame, endFrame, sample=3, isUpdateViewport=True, isGeneratePreview=True):
    dic = {}
    [bscMethods.OsFile.createDirectory(i) for i in yetiCaches]
    [cmds.setAttr(i + '.' + 'fileMode', 0) for i in yetiObjects]
    yetiShapePathLis = [maUtils._getNodeShapeNodeString(i) for i in yetiObjects]
    cmds.select(yetiShapePathLis)
    dic['nodes'] = ' '.join([i for i in yetiShapePathLis])
    dic['files'] = '"' + '|'.join(yetiCaches) + '"'
    dic['range'] = '%s %s' % (startFrame, endFrame)
    dic['samples'] = str(sample)
    dic['updateViewport'] = str(isUpdateViewport).lower()
    dic['generatePreview'] = str(isGeneratePreview).lower()
    contents = 'pgYetiCommand -writeCache %(files)s -range %(range)s -samples %(samples)s -updateViewport %(updateViewport)s -generatePreview %(generatePreview)s'
    mel.eval(contents % dic)
    #
    maUtils.setCurrentFrame(startFrame)
    #
    for seq, yetiShapePath in enumerate(yetiShapePathLis):
        setYetiConnectCache(yetiShapePath, yetiCaches[seq])


#
def getNurbsHairSolverCurves(nurbsHairSolverNode):
    return maUtils.getInputObjectsByAttrName(nurbsHairSolverNode, ['.inGuideCurves'])


#
def getNurbsHairMapNodes(nurbsHairObject):
    def getConnectionNodes(node):
        attr = node + '.' + 'inHairGrp'
        if maUtils._isAppExist(attr):
            inputNodes = cmds.listConnections(attr, destination=0, source=1, shapes=1)
            if inputNodes:
                for i in inputNodes:
                    if maUtils._getNodeCategoryString(i) == appCfg.MaNurbsHairCacheType:
                        lis.append(i)
                    #
                    getConnectionNodes(i)
    #
    lis = []
    shapePath = maUtils._getNodeShapeNodeString(nurbsHairObject)
    getConnectionNodes(shapePath)
    return lis


#
def setYetiConnectCache(yetiNode, fileString_):
    maUtils.setAttrDatumForce_(yetiNode, 'fileMode', 1)
    maUtils.setAttrStringDatum(yetiNode, 'cacheFileName', fileString_)


#
def setYetiObjectInGroom():
    pass


#
def setOutYetisCache(directory, furNodes, startFrame, endFrame, sample=3, isUpdateViewport=True, isGeneratePreview=True):
    if furNodes:
        # View Progress
        progressExplain = '''Set Fur ( Yeti ) Cache'''
        maxValue = len(furNodes)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for yetiNode in furNodes:
            # In Progress
            progressBar.update()
            if maUtils._isAppExist(yetiNode):
                subFolder = none
                if ':' in yetiNode:
                    subFolder = '_'.join(yetiNode.split('|')[-1].split(':')[:-1])
                furNodeName = getFurNodeName(yetiNode)
                fileString_ = '%s/%s/%s' % (directory, furNodeName, furNodeName)
                if subFolder:
                    fileString_ = '%s/%s/%s/%s' % (directory, subFolder, furNodeName, furNodeName)
                #
                usedFile = fileString_ + '.%04d.fur'
                if endFrame == startFrame:
                    usedFile = fileString_ + '.' + str(startFrame).zfill(4) + '.fur'
                #
                setYetiNodeWriteCache(usedFile, yetiNode, startFrame, endFrame, sample, isUpdateViewport, isGeneratePreview)
                #
                setYetiConnectCache(yetiNode, usedFile)


#
def getYetiRootNode(yetiNode):
    return cmds.pgYetiGraph(yetiNode, getRootNode=1)


#
def setYetiRootNode(yetiNode, node):
    cmds.pgYetiGraph(yetiNode, setRootNode=node)


#
def getYetiGraphData(yetiObject):
    yetiNode = maUtils._getNodeShapeNodeString(yetiObject, fullPath=1)
    graphRootNode = getYetiRootNode(yetiNode)
    #
    graphNodes = cmds.pgYetiGraph(yetiNode, listNodes=1)
    #
    graphNodeDataArray = []
    if graphNodes:
        for graphNode in graphNodes:
            paramDataArray = []
            graphNodeType = cmds.pgYetiGraph(yetiNode, node=graphNode, nodeType=1)
            nodeParams = cmds.pgYetiGraph(yetiNode, node=graphNode, listParams=1)
            for nodeParam in nodeParams:
                paramType = cmds.pgYetiGraph(yetiNode, node=graphNode, param=nodeParam, paramType=1)
                paramValue = cmds.pgYetiGraph(yetiNode, node=graphNode, param=nodeParam, getParamValue=1)
                isParamConstant = cmds.pgYetiGraph(yetiNode, node=graphNode, param=nodeParam, isParamConstant=1)
                #
                paramDataArray.append((nodeParam, paramValue, paramType, isParamConstant))
            #
            graphNodeDataArray.append((graphNode, graphNodeType, paramDataArray))
    return graphRootNode, graphNodeDataArray


#
def setCloseYetiGraphPanel():
    panel = 'pgYetiGraphPanel'
    if cmds.panel(panel, query=1, exists=1):
        window = panel + 'Window'
        if cmds.window(window, query=1, exists=1):
            cmds.deleteUI(window, window=1)


#
def setRenameYetiGraph(yetiObject):
    def setMain(nameSet):
        yetiNode = maUtils._getNodeShapeNodeString(yetiObject, fullPath=1)
        #
        graphNodes = cmds.pgYetiGraph(yetiNode, listNodes=1)
        #
        if graphNodes:
            setCloseYetiGraphPanel()
            graphRootNode = getYetiRootNode(yetiNode)
            graphRootNodeName = graphRootNode
            for seq, graphNode in enumerate(graphNodes):
                graphNodeType = cmds.pgYetiGraph(yetiNode, node=graphNode, nodeType=1)
                nodeName = graphNodeType + '_' + str(seq).zfill(4) + nameSet
                #
                if graphNode == graphRootNode:
                    graphRootNodeName = nodeName
                #
                if not nodeName == graphNode:
                    cmds.pgYetiGraph(yetiNode, node=graphNode, rename=nodeName)
            #
            setYetiRootNode(yetiNode, graphRootNodeName)
    #
    setMain('_temp')
    setMain('')


#
def setCreateYetiGraph(yetiObject, graphData):
    yetiNode = maUtils._getNodeShapeNodeString(yetiObject, fullPath=1)
    if graphData:
        graphRootNode, nodeDataArray = graphData
        # Create Nde_Node
        for graphNode, graphNodeType, paramDataArray in nodeDataArray:
            node = cmds.pgYetiGraph(yetiNode, type=graphNodeType, create=1)
            # Nde_Node Name
            if not graphNode == node:
                cmds.pgYetiGraph(yetiNode, node=node, rename=graphNode)
            # Nde_Node Param
            if paramDataArray:
                # Set Param Value
                for nodeParam, paramValue, paramType, isParamConstant in paramDataArray:
                    if paramType == 'boolean':
                        cmds.pgYetiGraph(yetiNode, node=graphNode, param=nodeParam, setParamValueBoolean=paramValue)
                    if paramType == 'float' or paramType == 'int':
                        cmds.pgYetiGraph(yetiNode, node=graphNode, param=nodeParam, setParamValueScalar=paramValue)
                    if paramType == 'vector':
                        cmds.pgYetiGraph(yetiNode, node=graphNode, param=nodeParam, setParamValueVector=paramValue)
                    if paramType == 'string':
                        if not isParamConstant:
                            cmds.pgYetiGraph(yetiNode, node=graphNode, param=nodeParam, setParamValueString=paramValue)
                        if isParamConstant:
                            cmds.pgYetiGraph(yetiNode, node=graphNode, param=nodeParam, setParamValueExpr=paramValue)
        # Set Root Nde_Node
        setYetiRootNode(yetiNode, graphRootNode)


#
def setYetiObjectCloseSolver(yetiObject):
    hairSystemObjects = maUtils.getYetiGuideHairSystems(yetiObject)
    if hairSystemObjects:
        for hairSystemObject in hairSystemObjects:
            hairSystem = maUtils._getNodeShapeNodeString(hairSystemObject, 1)
            #
            cmds.setAttr(hairSystem + '.simulationMethod', 1)
            cmds.setAttr(hairSystem + '.displayQuality', 5)
            cmds.setAttr(hairSystem + '.active', 0)


#
def setYetisGuideSet(yetiObjects, parentSet):
    if yetiObjects:
        for yetiObject in yetiObjects:
            sets = maUtils.getYetiGuideSets(yetiObject)
            for mSet in sets:
                maUtils.setElementSet(mSet, parentSet)


#
def setSolverGroup(assetName, namespace=none):
    solverGroup = assetPr.astUnitModelSolverGroupName(assetName, namespace)
    forHides = maUtils.getNodeLisByType('mesh', 1, solverGroup)
    [maUtils.setHide(maUtils._getNodeTransformNodeString(i)) for i in forHides]


#
def setScAstCfxDisplayLayer(assetName, namespace=none, scAstCfxDisplayLayer=None):
    scCfxGroup = prsMethods.Asset.groomLinkGroupName(assetName, namespace)
    lis = maUtils.getChildObjectsByRoot(scCfxGroup, [appCfg.DEF_mya_type_mesh, appCfg.DEF_mya_type_nurbs_surface, appCfg.DEF_mya_type_nurbs_curve])
    #
    if scAstCfxDisplayLayer:
        if not maUtils._isAppExist(scAstCfxDisplayLayer):
            maUtils.setCreateDisplayLayer(scAstCfxDisplayLayer)
        #
        maUtils.setDisplayLayerColor(scAstCfxDisplayLayer, color=(1, 1, .25))
        maUtils.setDisplayLayerVisible(scAstCfxDisplayLayer, False)
        maUtils.setAddObjectToDisplayLayer(scAstCfxDisplayLayer, lis)
    else:
        [maUtils.setHide(i) for i in lis]


#
def setScAstCfxGrowSourceConnectToModel(assetName, scAstModelNamespace, scAstCfxNamespace):
    scAstCfxContainer = assetPr.astCfxContainerName(assetName, scAstCfxNamespace)
    if not maUtils._isAppExist(scAstCfxContainer):
        astCfxContainer = assetPr.astCfxContainerName(assetName)
        if not maUtils._isAppExist(astCfxContainer):
            maUtils.setCreateContainer(astCfxContainer)
        #
        maUtils.setContainerNamespace(astCfxContainer, scAstCfxNamespace)
    #
    astCfxGrowSourceGroup = assetPr.astUnitCfxGrowSourceObjectGroupName(assetName, scAstCfxNamespace)
    #
    growSourceObjectLis = maUtils.getNodeChildLis(astCfxGrowSourceGroup, 1)
    nodeLis = []
    if growSourceObjectLis:
        for growSourceObject in growSourceObjectLis:
            if growSourceObject.endswith(astCfxGrowSourceGroupLabel):
                attrData = maUtils.getAttrDatum(growSourceObject, astCfxGrowSourceAttrLabel)
                if attrData:
                    sourceObject = scAstModelNamespace + ':' + attrData
                    if maUtils._isAppExist(sourceObject):
                        blendShapeNode = attrData + astCfxGrowSourceGroupLabel + inShapeLabel
                        # Transform
                        maUtils.setObjectTransferInputConnections(sourceObject, growSourceObject)
                        maUtils.setObjectTransferTransformation(sourceObject, growSourceObject)
                        maUtils.setObjectTransferVisibility(sourceObject, growSourceObject)
                        # Shape
                        if not maUtils._isAppExist(blendShapeNode):
                            maUtils.setNodeBlendCreate(sourceObject, growSourceObject, blendShapeNode)
                            #
                            nodeLis.append(blendShapeNode)
                            inOrig = growSourceObject + '|' + maUtils._getNodeShapeNodeString(growSourceObject, 1).split(':')[-1] + origLabel
                            #
                            if maUtils._isAppExist(inOrig):
                                nodeLis.append(inOrig)
                            #
                            inShapeSet = blendShapeNode + basicSetLabel
                            nodeLis.append(inShapeSet)
                        else:
                            sourceShapePath = maUtils._getNodeShapeNodeString(sourceObject)
                            sourceAttrName0 = '.worldMesh[0]'
                            targetAttrName0 = '.inputTarget[0].inputTargetGroup[0].inputTargetItem[6000].inputGeomTarget'
                            sourceAttr0, targetAttr0 = sourceShapePath + sourceAttrName0, blendShapeNode + targetAttrName0
                            maUtils.setAttrConnect(sourceAttr0, targetAttr0)
                            #
                            growSourceShapePath = maUtils._getNodeShapeNodeString(growSourceObject)
                            sourceAttrName1 = '.outputGeometry[0]'
                            targetAttrName1 = '.inMesh'
                            sourceAttr1, targetAttr1 = blendShapeNode + sourceAttrName1, growSourceShapePath + targetAttrName1
                            maUtils.setAttrConnect(sourceAttr1, targetAttr1)
    # Add Nodes
    maUtils.setContainerAddNodes(scAstCfxContainer, nodeLis)


#
def setScAstSolverGrowSourceConnectToModel(assetName, scAstModelNamespace, scAstSolverNamespace):
    scAstSolverContainer = assetPr.astSolverContainerName(assetName, scAstSolverNamespace)
    if not maUtils._isAppExist(scAstSolverContainer):
        astSolverContainer = assetPr.astSolverContainerName(assetName)
        if not maUtils._isAppExist(astSolverContainer):
            maUtils.setCreateContainer(astSolverContainer)
        #
        maUtils.setContainerNamespace(astSolverContainer, scAstSolverNamespace)
    #
    astCfxGrowSourceGroup = assetPr.astUnitSolverGrowSourceObjectGroupName(assetName, scAstSolverNamespace)
    #
    growSourceObjects = maUtils.getNodeChildLis(astCfxGrowSourceGroup, 1)
    nodeLis = []
    if growSourceObjects:
        for growSourceObject in growSourceObjects:
            if growSourceObject.endswith(astCfxGrowSourceGroupLabel):
                attrData = maUtils.getAttrDatum(growSourceObject, astCfxGrowSourceAttrLabel)
                if attrData:
                    sourceObject = scAstModelNamespace + ':' + attrData
                    if maUtils._isAppExist(sourceObject):
                        inShapeNode = attrData + astCfxGrowSourceGroupLabel + inShapeLabel
                        # Transform
                        maUtils.setObjectTransferInputConnections(sourceObject, growSourceObject)
                        maUtils.setObjectTransferTransformation(sourceObject, growSourceObject)
                        maUtils.setObjectTransferVisibility(sourceObject, growSourceObject)
                        # Shape
                        maUtils.setNodeBlendCreate(sourceObject, growSourceObject, inShapeNode)
                        #
                        nodeLis.append(inShapeNode)
                        inOrig = growSourceObject + '|' + maUtils._getNodeShapeNodeString(growSourceObject, 1).split(':')[-1] + origLabel
                        #
                        if maUtils._isAppExist(inOrig):
                            nodeLis.append(inOrig)
                        #
                        inShapeSet = inShapeNode + basicSetLabel
                        nodeLis.append(inShapeSet)
    # Add Nodes
    maUtils.setContainerAddNodes(scAstSolverContainer, nodeLis)


#
def setScAstSolverGuideConnectToCfx(connectionDic, scAstCfxNamespace, scAstSolverNamespace):
    def setBranch(nodepathString, connectionLis):
        objectName = maUtils._nodeString2nodename_(nodepathString)
        scObjectName = maUtils.getObjectStringJoinNamespace(objectName, scAstSolverNamespace)
        if maUtils._isAppExist(scObjectName):
            scObjectShapePath = maUtils._getNodeShapeNodeString(scObjectName)
            scObjectShapeName = maUtils._nodeString2nodename_(scObjectShapePath, useMode=1)
            for sourceAttr, targetAttr in connectionLis:
                if scObjectShapeName in sourceAttr:
                    sourceAttr = maUtils.getObjectStringJoinNamespace(sourceAttr, scAstSolverNamespace)
                else:
                    if sourceAttr.endswith('.outHairGrp'):
                        sourceAttr = maUtils.getObjectStringJoinNamespace(sourceAttr, scAstCfxNamespace)
                #
                if scObjectShapeName in targetAttr:
                    targetAttr = maUtils.getObjectStringJoinNamespace(targetAttr, scAstSolverNamespace)
                else:
                    if targetAttr.endswith('.inHairGrp'):
                        targetAttr = maUtils.getObjectStringJoinNamespace(targetAttr, scAstCfxNamespace)
                #
                if maUtils._isAppExist(sourceAttr) and maUtils._isAppExist(targetAttr):
                    if not maUtils.isAttrConnected(sourceAttr, targetAttr):
                        maUtils.setAttrConnect(sourceAttr, targetAttr)
    #
    if connectionDic:
        progressExplain = '''Connect Solver Guide'''
        maxValue = len(connectionDic)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for k, v in connectionDic.items():
            progressBar.update()
            setBranch(k, v)


#
def setScAstCfxConnectToSolver(connectionDic, scAstCfxNamespace, scAstSolverNamespace):
    def setBranch(nodepathString, connectionLis):
        objectName = maUtils._nodeString2nodename_(nodepathString)
        scObjectName = maUtils.getObjectStringJoinNamespace(objectName, scAstCfxNamespace)
        if maUtils._isAppExist(scObjectName):
            for sourceAttr, targetAttr in connectionLis:
                sourceAttr = maUtils.getObjectStringJoinNamespace(sourceAttr, scAstCfxNamespace)
                targetAttr = maUtils.getObjectStringJoinNamespace(targetAttr, scAstSolverNamespace)
                if maUtils._isAppExist(sourceAttr) and maUtils._isAppExist(targetAttr):
                    maUtils.setAttrConnect(sourceAttr, targetAttr)
    #
    if connectionDic:
        progressExplain = '''Connect Nurbs Hair Guide'''
        maxValue = len(connectionDic)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for k, v in connectionDic.items():
            progressBar.update()
            setBranch(k, v)


#
def setScAstSolverCurveConnectToSolverCache(assetName, scAstSolverNamespace, scAstSolverCacheNamespace):
    def setBranch(nodepathString):
        objectName = maUtils._nodeString2nodename_(nodepathString, useMode=1)
        sourceObjectName = maUtils.getObjectStringJoinNamespace(objectName, scAstSolverCacheNamespace)
        targetObjectName = maUtils.getObjectStringJoinNamespace(objectName, scAstSolverNamespace)
        if maUtils._isAppExist(sourceObjectName):
            sourceShapePath = maUtils._getNodeShapeNodeString(sourceObjectName)
            inputConnectionLis = maUtils.getNodeInputConnectionLis(sourceShapePath)
            if inputConnectionLis:
                if maUtils._isAppExist(targetObjectName):
                    blendShapeNode = objectName + '_blendShape'
                    if not maUtils._isAppExist(blendShapeNode):
                        cmds.blendShape(sourceObjectName, targetObjectName, name=blendShapeNode, weight=(0, 1), origin='world', before=1)
                    else:
                        sourceAttrName = '.worldSpace'
                        targetAttrName = '.inputGeomTarget'
                        #
                        sourceAttr = sourceObjectName + sourceAttrName
                        targetAttr = blendShapeNode + targetAttrName
                        #
                        maUtils.setAttrConnect(sourceAttr, targetAttr)
        else:
            errorLis.append(sourceObjectName)
    #
    errorLis = []
    #
    scSolverCacheGroup = assetPr.astUnitSolverBridgeGroupName(assetName, scAstSolverCacheNamespace)
    if maUtils._isAppExist(scSolverCacheGroup):
        maUtils.setNodeOutlinerRgb(scSolverCacheGroup, 0, .5, 1)
        #
        nurbsCurveObjects = maUtils.getChildObjectsByRoot(scSolverCacheGroup, appCfg.DEF_mya_type_nurbs_curve)
        if nurbsCurveObjects:
            progressExplain = '''Connect Solver Cache'''
            maxValue = len(nurbsCurveObjects)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for i in nurbsCurveObjects:
                progressBar.update()
                #
                setBranch(i)
    #
    return errorLis


#
def setScAstCfxFurGrowConnect__(assetName, astRootNamespace, astCfxNamespace):
    astUnitGroup = prsMethods.Asset.rootName(assetName, astRootNamespace)
    #
    astCfxGroup = prsMethods.Asset.groomLinkGroupName(assetName, astCfxNamespace)
    astCfxContainer = assetPr.astCfxContainerName(assetName)
    #
    astCfxGrowSourceGroup = assetPr.astUnitCfxGrowSourceObjectGroupName(assetName, astCfxNamespace)
    #
    growSourceObjects = maUtils.getNodeChildLis(astCfxGrowSourceGroup, 1)
    nodeLis = []
    if growSourceObjects:
        for growSourceObject in growSourceObjects:
            if growSourceObject.endswith(astCfxGrowSourceGroupLabel):
                attrData = maUtils.getAttrDatum(growSourceObject, astCfxGrowSourceAttrLabel)
                sourceObject = astRootNamespace + ':' + attrData
                if maUtils._isAppExist(sourceObject):
                    inShapeNode = attrData + astCfxGrowSourceGroupLabel + inShapeLabel
                    # Transform
                    maUtils.setObjectTransferInputConnections(sourceObject, growSourceObject)
                    maUtils.setObjectTransferTransformation(sourceObject, growSourceObject)
                    maUtils.setObjectTransferVisibility(sourceObject, growSourceObject)
                    # Shape
                    maUtils.setNodeBlendCreate(sourceObject, growSourceObject, inShapeNode)
                    #
                    nodeLis.append(inShapeNode)
                    inOrig = maUtils._getNodeShapeNodeString(growSourceObject, 1) + origLabel
                    #
                    if int(mayaVersion) >= 2015:
                        inOrig = growSourceObject + '|' + maUtils._getNodeShapeNodeString(growSourceObject, 1).split(':')[-1] + origLabel
                    #
                    if maUtils._isAppExist(inOrig):
                        nodeLis.append(inOrig)
                    #
                    inShapeSet = inShapeNode + basicSetLabel
                    nodeLis.append(inShapeSet)
    # Container
    maUtils.setInContainer(astCfxContainer, nodeLis)
    #
    if not maUtils.isReferenceNode(astUnitGroup):
        maUtils.setObjectParent(astCfxGroup, astUnitGroup)
        maUtils.setObjectParent(astCfxContainer, astUnitGroup)
    #
    elif maUtils.isReferenceNode(astUnitGroup):
        tempCfxGroup = assetPr.scAstCfxTempGroupName(assetName, astRootNamespace)
        #
        maUtils.setObjectParent(astCfxGroup, tempCfxGroup)
        maUtils.setObjectParent(astCfxContainer, tempCfxGroup)
    #
    maUtils.setContainerNamespace(astCfxContainer, astCfxNamespace)


#
def setScAstNurbsHairSolverConnectToTime(assetName, astCfxNamespace, startFrame):
    def setConnectToTime(objectPath):
        shapePath = maUtils._getNodeFullpathNameString(objectPath)
        #
        maUtils.setAttrDatumForce_(shapePath, 'startTime', startFrame)
        #
        outputTimeAttr = 'time1.outTime'
        inputTimeAttr = shapePath + '.currentTime'
        if not maUtils.isAttrConnected(outputTimeAttr, inputTimeAttr):
            maUtils.setAttrConnect(outputTimeAttr, inputTimeAttr)
    #
    astCfxNurbsHairSolverGroup = assetPr.astUnitRigSolNhrSolGuideObjectGroupPath(assetName, astCfxNamespace)
    if maUtils._isAppExist(astCfxNurbsHairSolverGroup):
        objectPaths = maUtils.getChildObjectsByRoot(astCfxNurbsHairSolverGroup, prsOutputs.Util.maNurbsHairInGuideCurvesNode, fullPath=True)
        if objectPaths:
            for i in objectPaths:
                setConnectToTime(i)


#
def getYetiSolverMode(yetiObject):
    shapePath = maUtils._getNodeShapeNodeString(yetiObject, 1)
    data = maUtils.getAttrDatum(shapePath, 'fileMode')
    return appCfg.MaYetiSolverModeLis[data]


#
def getYetiCacheFile(yetiObject):
    shapePath = maUtils._getNodeShapeNodeString(yetiObject, 1)
    string = maUtils.getAttrDatum(shapePath, 'cacheFileName')
    return string


#
def getHairSystemSolverMode(hairSystemObject):
    shapePath = maUtils._getNodeShapeNodeString(hairSystemObject, 1)
    data = maUtils.getAttrDatum(shapePath, 'simulationMethod')
    return appCfg.MaHairSystemSolverModeLis[data]


#
def getNurbsHairSolverMode(nurbsHairSolverObject):
    shapePath = maUtils._getNodeShapeNodeString(nurbsHairSolverObject, 1)
    data = maUtils.getAttrDatum(shapePath, appCfg.MaNurbsHairCacheModeAttrName)
    return appCfg.MaNurbsHairSolverModeLis[data]


#
def getNurbsHairCacheFile(nurbsHairObject):
    shapePath = maUtils._getNodeShapeNodeString(nurbsHairObject, 1)
    string = maUtils.getAttrDatum(shapePath, appCfg.MaNurbsHairCacheFileAttrName)
    return string


#
def getExistsYetiCache():
    pass


#
def getYetiCacheInfo(yetiObject):
    def getFrame(cacheFilePerFrame):
        string = cacheFilePerFrame[-8:-4]
        if string.isdigit():
            frame = int(string)
            return frame
    #
    keyword = '.%04d.fur'
    ext = '.fur'
    #
    cache = none
    solverMode = getYetiSolverMode(yetiObject)
    startFrame = 0
    endFrame = 0
    #
    cacheFile = getYetiCacheFile(yetiObject)
    if cacheFile:
        if cacheFile.endswith(ext):
            if cacheFile.endswith(keyword):
                base = cacheFile[: -len(keyword)]
                caches = glob.glob(base + '.[0-9][0-9][0-9][0-9]' + ext)
                if caches:
                    cache = cacheFile
                    startCache = caches[0]
                    startFrame = getFrame(startCache)
                    #
                    endCache = caches[-1]
                    endFrame = getFrame(endCache)
    #
    return cache, solverMode, startFrame, endFrame


#
def getYetiCacheFrameRange(yetiObject):
    def getFrame(cacheFilePerFrame):
        string = cacheFilePerFrame[-8:-4]
        if string.isdigit():
            frame = int(string)
            return frame
    #
    keyword, ext = '.%04d.fur', '.fur'
    #
    startFrame, endFrame = 0, 0
    #
    cacheFile = getYetiCacheFile(yetiObject)
    if cacheFile:
        if cacheFile.endswith(ext):
            if cacheFile.endswith(keyword):
                base = cacheFile[: -len(keyword)]
                cacheLis = glob.glob(base + '.[0-9][0-9][0-9][0-9]' + ext)
                if cacheLis:
                    startCache = cacheLis[0]
                    startFrame = getFrame(startCache)
                    #
                    endCache = cacheLis[-1]
                    endFrame = getFrame(endCache)
    #
    return startFrame, endFrame


#
def getGeomCacheExists(hairSystemObject):
    cache = none
    solverMode = getHairSystemSolverMode(hairSystemObject)
    startFrame = 0
    endFrame = 0
    #
    hairSystem = maUtils._getNodeShapeNodeString(hairSystemObject, 1)
    #
    cacheFiles = maGeomCache.getGeomCacheFiles(hairSystem)
    if cacheFiles:
        xmlFile, cacheFile = cacheFiles
        cache = xmlFile
        #
        startFrame, endFrame, solverIndex, cacheType, cacheFormat = maGeomCache.getGeometryCacheXmlData(xmlFile)
    #
    return cache, solverMode, startFrame, endFrame


#
def getNhrCacheInfo(nurbsHairObject):
    def getFrame(cacheFilePerFrame):
        string = cacheFilePerFrame[-8:-4]
        if string.isdigit():
            frame = int(string)
            return frame
    #
    keyword = '####.nhr'
    ext = '.nhr'
    #
    cache = none
    solverMode = getNurbsHairSolverMode(nurbsHairObject)
    startFrame = 0
    endFrame = 0
    #
    cacheFile = getNurbsHairCacheFile(nurbsHairObject)
    if cacheFile:
        if cacheFile.endswith(ext):
            if cacheFile.endswith(keyword):
                base = cacheFile[: -len(keyword)]
                caches = glob.glob(base + '[0-9][0-9][0-9][0-9]' + ext)
                if caches:
                    cache = cacheFile
                    startCache = caches[0]
                    startFrame = getFrame(startCache)
                    #
                    endCache = caches[-1]
                    endFrame = getFrame(endCache)
    #
    return cache, solverMode, startFrame, endFrame


#
def getNhrCacheFrameRange(nurbsHairObject):
    def getFrame(cacheFilePerFrame):
        string = cacheFilePerFrame[-8:-4]
        if string.isdigit():
            frame = int(string)
            return frame
    #
    keyword, ext = '####.nhr', '.nhr'
    #
    startFrame, endFrame = 0, 0
    #
    cacheFile = getNurbsHairCacheFile(nurbsHairObject)
    if cacheFile:
        if cacheFile.endswith(ext):
            if cacheFile.endswith(keyword):
                base = cacheFile[: -len(keyword)]
                cacheLis = glob.glob(base + '[0-9][0-9][0-9][0-9]' + ext)
                if cacheLis:
                    startCache = cacheLis[0]
                    startFrame = getFrame(startCache)
                    #
                    endCache = cacheLis[-1]
                    endFrame = getFrame(endCache)
    #
    return startFrame, endFrame


#
def getPfxHairSimMode(pfxHairObject):
    pfxHairNode = maUtils._getNodeShapeNodeString(pfxHairObject)
    hairSystemObjects = maUtils.getPfxHairSystemObjects(pfxHairNode)
    if hairSystemObjects:
        hairSystemObject = hairSystemObjects[0]
        hairSystem = maUtils._getNodeShapeNodeString(hairSystemObject, 1)
        solverMode = cmds.getAttr(hairSystem + '.simulationMethod')
        return appCfg.MaHairSystemSolverModeLis[solverMode]


#
def setOutGeometryCache(cachePath, cacheName, hairSystem, startFrame, endFrame, sample, cacheType='OneFile', cacheFormat='mcx'):
    maGeomCache.setOutGeometryCache(
        hairSystem, cachePath, cacheName,
        startFrame, endFrame,
        sample=sample, format=cacheType, cacheFormat=cacheFormat
    )


#
def setOutExistsGeometryCache(cachePath, cacheName, hairSystem):
    cacheFiles = maGeomCache.getGeomCacheFiles(hairSystem)
    if cacheFiles:
        xmlFile, cacheFile = cacheFiles
        if bscMethods.OsFile.isExist(xmlFile):
            base, ext = bscMethods.OsFile.toExtSplit(xmlFile)
            targetXmlFile = cachePath + '/' + cacheName + ext
            bscMethods.OsFile.copyTo(xmlFile, targetXmlFile)
        if bscMethods.OsFile.isExist(cacheFile):
            base, ext = bscMethods.OsFile.toExtSplit(cacheFile)
            targetCacheFile = cachePath + '/' + cacheName + ext
            bscMethods.OsFile.copyTo(cacheFile, targetCacheFile)


#
def setGeometryObjectInCache(cachePath, cacheName, hairSystem, simulationMode=None):
    #
    solverModeIndex = appCfg.MaHairSystemSolverModeIndexDic[simulationMode]
    cmds.setAttr(hairSystem + '.simulationMethod', solverModeIndex)
    cmds.setAttr(hairSystem + '.active', 1)
    #
    attrNames = ['hairCounts', 'vertexCounts', 'positions']
    channelArray = getChannelName(cachePath, cacheName)
    attrArray = [hairSystem + '.' + attrName for attrName in attrNames]
    maGeomCache.setGeometryObjectInCache(hairSystem, cachePath, cacheName, channelArray, attrArray)


#
def setOutPfxHairCache(cachePath, cacheName, hairSystem, startFrame, endFrame, sample, simulationMode, cacheMode='OneFile', cacheFormat='mcx'):
    if simulationMode in appCfg.MaHairSystemNeedUploadModeLis:
        maGeomCache.setOutGeometryCache(
            hairSystem, cachePath, cacheName,
            startFrame, endFrame, sample=sample, format=cacheMode, cacheFormat=cacheFormat)


#
def getExistsPfxHairCache(pfxHairObject, cacheFormat='mcx'):
    pfxHairNode = maUtils._getNodeShapeNodeString(pfxHairObject)
    hairSystemObjects = maUtils.getPfxHairSystemObjects(pfxHairNode)
    if hairSystemObjects:
        hairSystemObject = hairSystemObjects[0]
        hairSystem = maUtils._getNodeShapeNodeString(hairSystemObject, 1)
        cacheFiles = maGeomCache.getGeomCacheFiles(hairSystem)
        return cacheFiles


#
def setUploadExistsGeometryCache(cachePath, cacheName, hairSystem):
    cacheFiles = maGeomCache.getGeomCacheFiles(hairSystem)
    if cacheFiles:
        xmlFile, cacheFile = cacheFiles
        if bscMethods.OsFile.isExist(xmlFile):
            base, ext = bscMethods.OsFile.toExtSplit(xmlFile)
            targetXmlFile = cachePath + '/' + cacheName + ext
            #
            bscMethods.OsFile.copyTo(xmlFile, targetXmlFile)
        if bscMethods.OsFile.isExist(cacheFile):
            base, ext = bscMethods.OsFile.toExtSplit(cacheFile)
            targetCacheFile = cachePath + '/' + cacheName + ext
            #
            bscMethods.OsFile.copyTo(cacheFile, targetCacheFile)


#
def setNurbsHairConnectCache(nurbsHairObject, cacheFile):
    shapePath = maUtils._getNodeShapeNodeString(nurbsHairObject)
    #
    maUtils.setAttrDatumForce_(shapePath, appCfg.MaNurbsHairCacheModeAttrName, 2)
    maUtils.setAttrStringDatum(shapePath, appCfg.MaNurbsHairCacheFileAttrName, cacheFile)
    #
    outputTimeAttr = 'time1.outTime'
    inputTimeAttr = shapePath + '.currentTime'
    if not maUtils.isAttrConnected(outputTimeAttr, inputTimeAttr):
        maUtils.setAttrConnect(outputTimeAttr, inputTimeAttr)


#
def getNurbsHairCaches(nurbsHairObject):
    keyword = '####.nhr'
    ext = '.nhr'
    #
    caches = []
    #
    cacheFile = getNurbsHairCacheFile(nurbsHairObject)
    if cacheFile:
        if cacheFile.endswith(ext):
            if cacheFile.endswith(keyword):
                base = cacheFile[: -len(keyword)]
                caches = glob.glob(base + '[0-9][0-9][0-9][0-9]' + ext)
            else:
                caches = [cacheFile]
    #
    return caches


#
def setUploadExistsNurbsHairCache(cachePath, cacheName, nurbsHairObject):
    def getFrame(cacheFilePerFrame):
        string = cacheFilePerFrame[-8:-4]
        if string.isdigit():
            return string
    #
    ext = '.nhr'
    caches = getNurbsHairCaches(nurbsHairObject)
    if caches:
        for sourceFile in caches:
            frame = getFrame(sourceFile)
            if frame:
                targetFile = '{}/{}'.format(cachePath, cacheName + '.' + frame + ext)
                bscMethods.OsFile.copyTo(sourceFile, targetFile)


#
def setIgnorePfxHairCache(hairSystem, simulationMode):
    if simulationMode in appCfg.MaHairSystemSolverModeIndexDic:
        mode = appCfg.MaHairSystemSolverModeIndexDic[simulationMode]
        cmds.setAttr(hairSystem + '.simulationMethod', mode)
        cmds.setAttr(hairSystem + '.active', 0)


#
def setPfxHairObjectCloseSolver(pfxHairObject):
    hairSystemObjects = maUtils.getPfxHairSystemObjects(pfxHairObject)
    if hairSystemObjects:
        for hairSystemObject in hairSystemObjects:
            hairSystem = maUtils._getNodeShapeNodeString(hairSystemObject, 1)
            #
            cmds.setAttr(pfxHairObject + '.visibility', 1)
            #
            cmds.setAttr(hairSystem + '.simulationMethod', 1)
            cmds.setAttr(hairSystem + '.displayQuality', 5)
            cmds.setAttr(hairSystem + '.active', 0)


#
def getHtmlFile(cachePath, cacheName):
    return cachePath + '/' + cacheName + '.xml'


#
def getChannelName(cachePath, cacheName):
    htmlFile = getHtmlFile(cachePath, cacheName)
    channelArray = []
    htmlData = bscMethods.OsFile.readlines(htmlFile)
    for line in htmlData:
        if 'ChannelName' in line:
            channel = line.split('"')[1]
            channelArray.append(channel)
    return channelArray


#
def setPfxHairInCache(cachePath, cacheName, hairSystem, simulationMode):
    mode = appCfg.MaHairSystemSolverModeIndexDic[simulationMode]
    cmds.setAttr(hairSystem + '.simulationMethod', mode)
    if simulationMode in appCfg.MaHairSystemNeedUploadModeLis:
        cmds.setAttr(hairSystem + '.active', 1)
        attrNames = ['hairCounts', 'vertexCounts', 'positions']
        channelArray = getChannelName(cachePath, cacheName)
        attrArray = [hairSystem + '.' + attrName for attrName in attrNames]
        maGeomCache.setGeometryObjectInCache(hairSystem, cachePath, cacheName, channelArray, attrArray)
    elif not simulationMode in appCfg.MaHairSystemNeedUploadModeLis:
        cmds.setAttr(hairSystem + '.active', 0)


#
def getPfxHairCacheEnable(pfxHairObject):
    enable = False
    pfxHairNode = maUtils._getNodeShapeNodeString(pfxHairObject)
    hairSystemObjects = maUtils.getPfxHairSystemObjects(pfxHairNode)
    if hairSystemObjects:
        hairSystemObject = hairSystemObjects[0]
        hairSystem = maUtils._getNodeShapeNodeString(hairSystemObject, 1)
        cacheNode = maGeomCache.getGeomCacheNodeLis(hairSystem)
        if cacheNode:
            enable = True
    return enable


#
def setCreateFurObjectsUniqueId(pathData):
    if pathData:
        for uniqueId, path in pathData.items():
            maUuid.setMayaUniqueId(path[1:], uniqueId)


#
def getFurObjectsPathDic(furObjects):
    dic = bscMtdCore.orderedDict()
    #
    if furObjects:
        for nodepathString in furObjects:
            objectPath = maUtils._getNodeFullpathNameString(nodepathString)
            uniqueId = maUuid._getNodeUniqueIdString(objectPath)
            dic[uniqueId] = objectPath
    return dic


#
def getFurObjectsInfoDic(furObjects):
    dic = bscMtdCore.orderedDict()
    #
    if furObjects:
        for nodepathString in furObjects:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            dic[uniqueId] = ()
    return dic


#
def getNhrObjectsInfoDic(nurbsHairObjects):
    dic = bscMtdCore.orderedDict()
    #
    if nurbsHairObjects:
        # View Progress
        progressExplain = u'''Read Nurbs Hair Information'''
        maxValue = len(nurbsHairObjects)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for nurbsHairObject in nurbsHairObjects:
            progressBar.update()
            uniqueId = maUuid._getNodeUniqueIdString(nurbsHairObject)
            #
            dic[uniqueId] = (
                datHash.getStrHashKey(getNhrObjectGraphNodeSub(nurbsHairObject)),
                datHash.getStrHashKey(getNhrObjectGraphGeometrySub(nurbsHairObject)),
                datHash.getStrHashKey(getNhrObjectGraphRelationSub(nurbsHairObject))
            )
    return dic


#
def setRefreshYetiGrow(growMesh):
    meshShape = maUtils._getNodeShapeNodeString(growMesh)
    connectYetiObjects = maUtils._getNodeTargetNodeStringList(meshShape, 'pgYetiMaya')
    if connectYetiObjects:
        for yetiObject in connectYetiObjects:
            yetiNode = maUtils._getNodeShapeNodeString(yetiObject)
            importNodes = cmds.pgYetiGraph(yetiNode, listNodes=1, type='import')
            if importNodes:
                for node in importNodes:
                    inputGeometry = cmds.pgYetiGraph(yetiNode, node=node, param='geometry', getParamValue=1)
                    if cmds.pgYetiGraph(yetiNode, node=node, param='type', getParamValue=1) == 0:
                        if inputGeometry == '*':
                            maUtils.setYetiNodeAttr(yetiNode, node, 'geometry', meshShape)
                        if inputGeometry != meshShape:
                            maUtils.setYetiNodeAttr(yetiNode, node, 'geometry', meshShape)


#
def getNurbsHairConnectObjectData(nurbsHairObject):
    def getBranch(nodepathString):
        if maUtils._getNodeIsTransform(nodepathString):
            objectPath = maUtils._getNodeFullpathNameString(nodepathString)
            graphObjectLis.append(objectPath)
            #
            nodepathString = maUtils._getNodeShapeNodeString(objectPath)
        else:
            graphNodeLis.append(nodepathString)
        #
        mainNodes = maUtils.getInputObjectsByAttrName(nodepathString, '.inHairGrp')
        #
        growMeshes = maUtils.getInputObjectsByAttrName(nodepathString, growMeshAttrNames)
        guideMeshes = maUtils.getInputObjectsByAttrName(nodepathString, guideMeshAttrNames)
        if mainNodes:
            [getBranch(i) for i in mainNodes]
        if growMeshes:
            [graphGrowGeometryLis.append(maUtils._getNodeFullpathNameString(i)) for i in growMeshes if i not in graphGrowGeometryLis]
        if guideMeshes:
            [graphGuideGeometryLis.append(maUtils._getNodeFullpathNameString(i)) for i in guideMeshes if i not in graphGuideGeometryLis]
    #
    growMeshAttrNames = ['.inSkinMesh']
    guideMeshAttrNames = ['.inGuideSurfs', '.inSelectedGuideSurfs']
    #
    graphObjectLis = []
    graphNodeLis = []
    graphGrowGeometryLis = []
    graphGuideGeometryLis = []
    #
    getBranch(nurbsHairObject)
    return graphObjectLis[1:], graphNodeLis, graphGrowGeometryLis, graphGuideGeometryLis


#
def getNurbsHairObjects(used=False):
    data = [maUtils._getNodeTransformNodeString(i, 1) for i in maUtils.getNodeLisByType('nurbsHair', fullPath=True)]
    if used is True:
        subLis = []
        for i in data:
            graphObjects = getNurbsHairConnectObjectData(i)[0]
            if len(graphObjects) >= 1:
                subLis.append(i)
        #
        lis = subLis
    else:
        lis = data
    return lis


#
def getNurbsHairGraphNodes(nurbsHairObject):
    def getBranch(mNode):
        if maUtils._getNodeIsTransform(mNode):
            objectPath = maUtils._getNodeFullpathNameString(mNode)
            mNode = maUtils._getNodeShapeNodeString(objectPath)
            #
            graphObjects.append(objectPath)
        else:
            graphNodes.append(mNode)
        #
        nodeLis = maUtils.getInputObjectsByAttrName(mNode, '.inHairGrp')
        if nodeLis:
            [getBranch(i) for i in nodeLis]
    #
    graphObjects = []
    graphNodes = []
    #
    getBranch(nurbsHairObject)
    return graphObjects, graphNodes


#
def getNhrObjectGraphGeometryObjects(nurbsHairObject):
    def getBranch(mNode):
        if maUtils._getNodeIsTransform(mNode):
            objectPath = maUtils._getNodeFullpathNameString(mNode)
            mNode = maUtils._getNodeShapeNodeString(objectPath)
        #
        nodeLis = maUtils.getInputObjectsByAttrName(mNode, '.inHairGrp')
        if nodeLis:
            [getBranch(i) for i in nodeLis]
        #
        geometryObjects = maUtils.getInputObjectsByAttrName(mNode, ['.inSkinMesh', '.inGuideSurfs', '.inSelectedGuideSurfs'])
        if geometryObjects:
            [lis.append(maUtils._getNodeFullpathNameString(i)) for i in geometryObjects if i not in lis]
    #
    lis = []
    getBranch(nurbsHairObject)
    return lis


# Sub Method
def getNhrObjectGraphNodeSub(nurbsHairObject):
    # Graph Nde_Node
    objectDatas = []
    nodeDataLis = []
    graphObjects, graphNodes = getNurbsHairGraphNodes(nurbsHairObject)
    if graphObjects:
        for seq, i in enumerate(graphObjects):
            data = maObj.getObjectCreateData(i)
            objectDatas.append(data)
    if graphNodes:
        for i in graphNodes:
            data = maObj.getObjectShapeCreateData(i)
            nodeDataLis.append(data)
    return objectDatas, nodeDataLis


#
def getNhrObjectsGraphNodeDic(nurbsHairObjects):
    dic = bscMtdCore.orderedDict()
    if nurbsHairObjects:
        for seq, i in enumerate(nurbsHairObjects):
            objectPath = i
            graphNodeData = getNhrObjectGraphNodeSub(objectPath)
            rowIndex = seq
            #
            uniqueId = maUuid._getNodeUniqueIdString(objectPath)
            dic[uniqueId] = graphNodeData, rowIndex
    return dic


#
def setCreateNurbsHairObjects(dataDic):
    def setBranch(data, uniqueId):
        if data:
            objectDatas, graphNodeDatas = data
            if objectDatas:
                mainData = objectDatas[0]
                maObj.setCreateObjectByCreateData(mainData, uniqueId)
                for i in objectDatas[1:]:
                    maObj.setCreateObjectByCreateData(i)
            if graphNodeDatas:
                for i in graphNodeDatas:
                    maObj.setNodeCreateByAttrDatum(i)
    #
    def setMain():
        if dataDic:
            dic = {}
            rowIndexLis = []
            for uniqueId, compData in dataDic.items():
                graphNodeData, rowIndex = compData
                dic[rowIndex] = graphNodeData, uniqueId
                rowIndexLis.append(rowIndex)
            #
            if dic:
                rowIndexLis.sort()
                for i in rowIndexLis:
                    data, uniqueId = dic[i]
                    setBranch(data, uniqueId)
    #
    setMain()


# Sub Method
def getNhrObjectGraphGeometrySub(nurbsHairObject):
    def getBranch(objectPath):
        shapePath = maUtils._getNodeShapeNodeString(objectPath)
        #
        shapeName = maUtils._nodeString2nodename_(shapePath)
        shapeType = maUtils._getNodeCategoryString(shapePath)
        transformData = maObj.getObjectTransformCreateData(objectPath)
        if shapeType == appCfg.DEF_mya_type_mesh:
            geomData = maGeom.getMeshObjectGeomData(objectPath)
            mapData = maGeom.getMeshObjectMapData(objectPath)
            lis.append((shapeName, shapeType, transformData, geomData, mapData))
        elif shapeType == appCfg.DEF_mya_type_nurbs_surface:
            geomData = maGeom.getNurbsSurfaceObjectGeomData(objectPath)
            mapData = None
            lis.append((shapeName, shapeType, transformData, geomData, mapData))
        elif shapeType == appCfg.DEF_mya_type_nurbs_curve:
            geomData = maGeom.getNurbsCurveObjectGeomData(objectPath)
            mapData = None
            lis.append((shapeName, shapeType, transformData, geomData, mapData))
    #
    lis = []
    #
    geomObjects = getNhrObjectGraphGeometryObjects(nurbsHairObject)
    if geomObjects:
        for seq, i in enumerate(geomObjects):
            getBranch(i)
    #
    return lis


#
def getNhrObjectsGraphGeometryDic(nurbsHairObjects):
    dic = bscMtdCore.orderedDict()
    if nurbsHairObjects:
        for seq, i in enumerate(nurbsHairObjects):
            objectPath = i
            graphObjectsData = getNhrObjectGraphGeometrySub(objectPath)
            rowIndex = seq
            uniqueId = maUuid._getNodeUniqueIdString(objectPath)
            dic[uniqueId] = graphObjectsData, rowIndex
    return dic


#
def setCreateNhrObjectsGeometry(dataDic):
    def setBranch(data):
        if data:
            for i in data:
                maGeom.setCreateObjectGraphGeometrySub(i)
    #
    def setMain():
        if dataDic:
            dic = {}
            rowIndexLis = []
            for k, v in dataDic.items():
                geometryObjectData, rowIndex = v
                dic[rowIndex] = geometryObjectData
                rowIndexLis.append(rowIndex)
            #
            if dic:
                rowIndexLis.sort()
                for i in rowIndexLis:
                    data = dic[i]
                    setBranch(data)
    #
    setMain()


# Sub Method
def getNhrObjectGraphRelationSub(nurbsHairObject):
    def getBranch(branchNodes):
        for i in branchNodes:
            subConnections = maAttr.getObjectConnectionDataArray(i)
            if subConnections:
                lis.extend(subConnections)
    #
    def getMain():
        connectionData = getNurbsHairConnectObjectData(nurbsHairObject)
        for i in connectionData:
            getBranch(i)
    #
    lis = []
    # Main Object
    mainConnections = maAttr.getObjectConnectionDataArray(nurbsHairObject)
    lis.extend(mainConnections)
    #
    getMain()
    return lis


#
def getNhrObjectsGraphRelationDic(nurbsHairObjects):
    dic = bscMtdCore.orderedDict()
    if nurbsHairObjects:
        for seq, i in enumerate(nurbsHairObjects):
            objectPath = i
            relationData = getNhrObjectGraphRelationSub(i)
            #
            uniqueId = maUuid._getNodeUniqueIdString(objectPath)
            dic[uniqueId] = relationData
    return dic


#
def setCreateNhrObjectsRelation(dataDic):
    def setBranch(data):
        if data:
            maAttr.setCreateConnections(data)
    #
    def setMain():
        if dataDic:
            for k, v in dataDic.items():
                setBranch(v)
    #
    setMain()


#
def getNhrGuideObjects(nurbsHairObject):
    def getBranch(subObjStr):
        nodeStrings = maUtils.getInputObjectsByAttrName(subObjStr, '.inHairGrp')
        if nodeStrings:
            for nodepathString in nodeStrings:
                objectType = maUtils._getNodeShapeCategoryString(nodepathString)
                if objectType == appCfg.MaNurbsHairInGuideCurvesType:
                    lis.append(nodepathString)
                #
                getBranch(nodepathString)
    #
    lis = []
    #
    shapePath = maUtils._getNodeShapeNodeString(nurbsHairObject)
    getBranch(shapePath)
    return lis


#
def getNhrObjectsByGuide(nhrGuideObject):
    def getBranch(subObjStr):
        nodeStrings = maUtils.getOutputNodeLisFilter(subObjStr, '.outHairGrp')
        if nodeStrings:
            for nodepathString in nodeStrings:
                objectType = maUtils._getNodeShapeCategoryString(nodepathString)
                if objectType == appCfg.MaNodeType_Plug_NurbsHair:
                    lis.append(nodepathString)
                #
                getBranch(nodepathString)
    #
    lis = []
    #
    shapePath = maUtils._getNodeShapeNodeString(nhrGuideObject)
    getBranch(shapePath)
    return lis


#
def isNhrHasSolGuideObject(nurbsHairObject):
    def getBranch(subObjStr):
        nodeStrings = maUtils.getInputObjectsByAttrName(subObjStr, '.inHairGrp')
        if nodeStrings:
            for nodepathString in nodeStrings:
                objectType = maUtils._getNodeShapeCategoryString(nodepathString)
                if objectType == appCfg.MaNurbsHairInGuideCurvesType:
                    lis.append(nodepathString)
                #
                getBranch(nodepathString)
    #
    lis = []
    #
    shapePath = maUtils._getNodeShapeNodeString(nurbsHairObject)
    getBranch(shapePath)
    return lis != []


#
def setConnectNurbsHairSolver(nurbsHairSolverObject, guideGroup):
    outAttrName = '.worldSpace[0]'
    inAttrName = '.inGuideCurves[{}].inStrand'
    shapePath = maUtils._getNodeShapeNodeString(nurbsHairSolverObject)
    if maUtils._isAppExist(shapePath) and maUtils._isAppExist(guideGroup):
        guideCurves = maUtils.getChildShapesByRoot(guideGroup, 'nurbsCurve')
        if guideCurves:
            for seq, i in enumerate(guideCurves):
                sourceAttr = i + outAttrName
                targetAttr = shapePath + inAttrName.format(str(seq))
                if not maUtils.isAttrConnected(sourceAttr, targetAttr):
                    maUtils.setAttrConnect(sourceAttr, targetAttr)


#
def getFurCacheExists(furObject):
    objectType = maUtils._getNodeShapeCategoryString(furObject)
    if objectType == appCfg.MaNodeType_Plug_Yeti:
        return getYetiCacheInfo(furObject)
    elif objectType == appCfg.MaHairSystemType:
        return getGeomCacheExists(furObject)
    elif objectType == appCfg.MaNodeType_Plug_NurbsHair:
        return getNhrCacheInfo(furObject)


#
def getNhrScatterObjects(nurbsHairObject):
    def getBranch(subObjStr):
        nodeStrings = maUtils.getInputObjectsByAttrName(subObjStr, '.inHairGrp')
        if nodeStrings:
            for nodepathString in nodeStrings:
                objectType = maUtils._getNodeShapeCategoryString(nodepathString)
                if objectType == appCfg.MaNurbsHairScatterType:
                    lis.append(nodepathString)
                #
                getBranch(nodepathString)
    #
    lis = []
    #
    shapePath = maUtils._getNodeShapeNodeString(nurbsHairObject)
    getBranch(shapePath)
    #
    return lis


#
def setNurbsHairNodeWriteCache(nurbsHairNode, cacheFile, timeTag=None):
    tempCacheFile = bscMethods.OsFile.temporaryName(cacheFile, timeTag)
    #
    melCommand = '''nurbsHairExport -f "{1}" -hn "{0}"'''.format(nurbsHairNode, tempCacheFile)
    mel.eval(melCommand)
    #
    bscMethods.OsFile.copyTo(tempCacheFile, cacheFile)


#
def setNhrCacheObjectReadCache(nhrCacheObject, cacheFile):
    maUtils.setAttrStringDatum(nhrCacheObject, appCfg.MaNurbsHairCacheFileAttrName, cacheFile)
    maUtils.setAttrDatumForce_(nhrCacheObject, appCfg.MaNurbsHairCacheModeAttrName, appCfg.MaNurbsHairSolverModeIndexDic['Read'])


#
def getNhrSolverGuideCacheObjects(mhrSolverGuideObjects):
    def getBranch(nodepathString):
        maShape = maUtils._getNodeShapeNodeString(nodepathString)
        existsCacheObjects = maUtils._getNodeSourceNodeStringList(maShape, appCfg.MaNurbsHairCacheType)
        if existsCacheObjects:
            lis.extend(existsCacheObjects)
    #
    lis = []
    [getBranch(i) for i in mhrSolverGuideObjects]
    #
    return lis


#
def setCollectionNhrSolverGuideObjectsCaches(nhrCacheObjects, targetDirectoryString, collection=True, repath=True):
    def setBranch(mObject):
        sourceFileString = maUtils.getAttrDatum(mObject, appCfg.MaNurbsHairCacheFileAttrName)
        osFileBasename = bscMethods.OsFile.basename(sourceFileString)
        targetFileString = bscMethods.OsPath.composeBy(targetDirectoryString, osFileBasename)
        if collection is True:
            bscMethods.OsFile.copyTo(sourceFileString, targetFileString)
        if repath is True:
            setNhrCacheObjectReadCache(mObject, targetFileString)
    #
    [setBranch(i) for i in nhrCacheObjects]


#
def setNurbsHairCovertToCache(nurbsHairObject, cacheFolder, timeTag=None):
    def setBranch(nodepathString):
        objectShape = maUtils._getNodeShapeNodeString(nodepathString)
        #
        objectName = maUtils._nodeString2nodename_(nodepathString)
        cacheObjectName = objectName + '_solCache'
        # Cache
        cacheFile = '{}/{}.nhr'.format(cacheFolder, objectName)
        setNurbsHairNodeWriteCache(objectShape, cacheFile, timeTag)
        # Attribute
        inputObjectSourceAttr = objectShape + '.outHairGrp'
        cacheObjectSourceAttr = cacheObjectName + '.outHairGrp'
        cacheObjectTargetAttr = cacheObjectName + '.inHairGrp'
        #
        if not maUtils._isAppExist(cacheObjectName):
            maUtils.setCreateNode(appCfg.MaNurbsHairCacheType, cacheObjectName)
            # maUtils.setAttrConnect(inputObjectSourceAttr, cacheObjectTargetAttr)
        #
        outputObjects = maUtils._getNodeTargetNodeStringList(objectShape)
        if outputObjects:
            for outputObject in outputObjects:
                if not cacheObjectName in outputObject:
                    outputObjectTargetAttr = outputObject + '.inHairGrp'
                    #
                    maUtils.setAttrDisconnect(inputObjectSourceAttr, outputObjectTargetAttr)
                    maUtils.setAttrConnect(cacheObjectSourceAttr, outputObjectTargetAttr)
        #
        setNhrCacheObjectReadCache(cacheObjectName, cacheFile)
    #
    nurbsHairShape = maUtils._getNodeShapeNodeString(nurbsHairObject)
    inputObjects = maUtils.getInputObjectsByAttrName(nurbsHairShape, '.inHairGrp')
    if inputObjects:
        [setBranch(i) for i in inputObjects if not maUtils._getNodeShapeCategoryString(i) == appCfg.MaNurbsHairCacheType]


#
def setNurbsHairObjectCreateSolverGuide(nurbsHairObject, assetName):
    def initNurbsHairInGuideCurves(node):
        cmds.setAttr(node + '.blendCurve[0].blendCurve_Position', 0)
        cmds.setAttr(node + '.blendCurve[0].blendCurve_FloatValue', 0)
        cmds.setAttr(node + '.blendCurve[1].blendCurve_Position', 1)
        cmds.setAttr(node + '.blendCurve[1].blendCurve_FloatValue', 0)
        # cmds.setAttr(node + '.ignore', 1)
        maUtils.setNodeOutlinerRgb(node, .25, 1, .5)
    #
    nhrObjectName = maUtils._nodeString2nodename_(nurbsHairObject)
    nhrSolGuideObjectName = nhrObjectName.replace(appCfg.MaNodeType_Plug_NurbsHair, appCfg.MaNurbsHairInGuideCurvesType)
    nhrSolGuideShapeName = nhrSolGuideObjectName + 'Shape'
    #
    boolean = isNhrHasSolGuideObject(nurbsHairObject)
    if not boolean:
        parentGroup = assetPr.astUnitRigSolNhrSolGuideObjectGroupPath(assetName)
        if not maUtils._isAppExist(parentGroup):
            maUtils.setAppPathCreate(parentGroup)
        #
        if not maUtils._isAppExist(nhrSolGuideObjectName):
            maObj.setCreateTransformObject(nhrSolGuideObjectName, appCfg.MaNurbsHairInGuideCurvesType, parent=parentGroup)
            initNurbsHairInGuideCurves(nhrSolGuideObjectName)
        #
        nhrSolGuideObjectSourceAttr = nhrSolGuideShapeName + '.outHairGrp'
        nhrSolGuideObjectTargetAttr = nhrSolGuideShapeName + '.inHairGrp'
        #
        nhrScatterObjects = getNhrScatterObjects(nurbsHairObject)
        if nhrScatterObjects:
            nhrScatterObject = nhrScatterObjects[0]
            nhrScatterShape = maUtils._getNodeShapeNodeString(nhrScatterObject)
            outputConnections = maUtils.getNodeOutputConnectionLis(nhrScatterShape)
            if outputConnections:
                for seq, (sourceAttr, targetAttr) in enumerate(outputConnections):
                    maUtils.setAttrDisconnect(sourceAttr, targetAttr)
                    maUtils.setAttrConnect(sourceAttr, nhrSolGuideObjectTargetAttr)
                    maUtils.setAttrConnect(nhrSolGuideObjectSourceAttr, targetAttr)
            #
            maUtils.setAttrStringDatumForce_(nhrSolGuideObjectName, prsOutputs.Util.astRigSolGuideSourceAttrLabel, nhrScatterObject)


#
def setNurbsHairObjectsShowMode(objectUuids, showMode=0):
    if objectUuids:
        for objectUuid in objectUuids:
            nodepathString = maUuid.getObject(objectUuid)
            maUtils.setAttrDatumForce_(nodepathString, 'showMode', showMode)


#
def setNurbsHairObjectsShowMode_(nhrObjects, showMode=0):
    if nhrObjects:
        for nodepathString in nhrObjects:
            maUtils.setAttrDatumForce_(nodepathString, 'showMode', showMode)
