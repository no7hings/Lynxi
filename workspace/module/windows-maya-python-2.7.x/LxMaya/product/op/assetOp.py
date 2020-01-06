# coding=utf-8
import collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel

from LxBasic import bscMethods

from LxCore import lxCore_

from LxUi.qt import qtLog, qtCommands

from LxCore.preset.prod import assetPr

from LxMaya.command import maUtils, maGeom, maAttr

from LxMaya.product.data import datAsset

none = ''


# Clean Nde_Node By Name
def cleanNode(inData, nodeType):
    explain = u'Clean %s' % nodeType
    bscMethods.PythonMessage().trace(explain)
    nodes = [i for i in inData if maUtils.isAppExist(i) and not maUtils.isReferenceNode(i)]
    if nodes:
        for node in nodes:
            if maUtils.isAppExist(node):
                cmds.lockNode(node, lock=0)
                cmds.delete(node)
                bscMethods.PythonMessage().traceResult(node)


# Assign Default Nde_ShaderRef
def setDefaultShader(logWin, objectLis):
    qtLog.viewStartSubProcess(logWin, u'Assign Default - Nde_ShaderRef')
    cmds.sets(objectLis, forceElement='initialShadingGroup')
    qtLog.viewStartSubProcess(logWin, u'Assign Default - Nde_ShaderRef')


# Assign Default Shaders
def setObjectDefaultShaderCmd(logWin, objectLis):
    explain = u'''Assign Initial - Nde_ShaderRef'''
    qtLog.viewStartSubProcess(logWin, explain)
    for objectString in objectLis:
        cmds.sets(objectString, forceElement='initialShadingGroup')
        cmds.sets(maUtils.getNodeShape(objectString), forceElement='initialShadingGroup')
        qtLog.viewResult(logWin, maUtils._toNodeName(objectString), 'initialShadingGroup')
    qtLog.viewCompleteSubProcess(logWin)


#
def setObjectTransparentRefresh(objectLis):
    for objectPath in objectLis:
        #
        attrDatum = maUtils.getAttrDatum(objectPath, 'primaryVisibility')
        maUtils.setAttrBooleanDatumForce(
            objectPath, lxCore_.LynxiAttrName_Object_RenderVisible, attrDatum
        )
        #
        attrDatum = maUtils.getAttrDatum(objectPath, 'aiOpaque')
        maUtils.setAttrBooleanDatumForce(
            objectPath, lxCore_.LynxiAttrName_Object_Transparent, not attrDatum
        )


# Clean Object's Unused Shape
def setObjectUnusedShapeClear(objectLis):
    explain = u'''Clean Unused - Shape'''
    bscMethods.PythonMessage().trace(explain)
    errorObjects = []
    # Get Error Objects
    for objectString in objectLis:
        shapes = cmds.listRelatives(objectString, children=1, shapes=1, noIntermediate=0, fullPath=1)
        if len(shapes) > 1:
            errorObjects.append(objectString)
    # Clean Error Objects's Shape
    if errorObjects:
        for objectString in errorObjects:
            shapes = cmds.listRelatives(objectString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            usedShapes = cmds.listRelatives(objectString, children=1, shapes=1, noIntermediate=1, fullPath=1)
            unusedShapes = [i for i in shapes if i and i not in usedShapes]
            if unusedShapes:
                for shape in unusedShapes:
                    cmds.delete(shape)
                    bscMethods.PythonMessage().traceResult(maUtils._toNodeName(shape))


# Clean Unused Nde_ShaderRef
def setUnusedShaderClear():
    mel.eval('MLdeleteUnused;')


# Unlock and Soft Normal
def setMeshVertexNormalUnlockCmd(objectLis):
    explain = '''Unlock Mesh's Vertex Normal'''
    if objectLis:
        maxValue = len(objectLis)
        progressBar = qtCommands.setProgressWindowShow(explain, maxValue)
        for objectString in objectLis:
            progressBar.updateProgress()
            maGeom.setMeshVertexNormalUnlock(objectString)


# Unlock and Soft Normal
def setMeshesSmoothNormal(objectLis):
    explain = '''Soft ( Smooth ) Mesh's Edge'''
    if objectLis:
        maxValue = len(objectLis)
        progressBar = qtCommands.setProgressWindowShow(explain, maxValue)
        for objectString in objectLis:
            progressBar.updateProgress()
            maGeom.setMeshEdgeSmooth(objectString, True)


# Clean Unknown Nde_Node
def setUnknownNodeClear():
    cleanNode(cmds.ls(type='unknown'), u'Unknown - Nde_Node')


#
def cleanUnusedAov(logWin):
    UnusedAov = []
    aovs = cmds.ls(type='aiAOV')
    if aovs and cmds.objExists('defaultArnoldRenderOptions'):
        aovUsed = maUtils.getInputNodes('defaultArnoldRenderOptions', 'aiAOV')
        if aovUsed:
            UnusedAov = [aovs.remove(i) for i in aovUsed]
    cleanNode(UnusedAov, u'Unused Aovs')


#
def setDisplayLayerClear():
    explain = u'''Clean Display - Layer'''
    bscMethods.PythonMessage().trace(explain)
    displayLayers = [i for i in cmds.ls(type='displayLayer') if i != 'defaultLayer' and cmds.getAttr(i + '.displayOrder') != 0 and not cmds.referenceQuery(i, isNodeReferenced=1)]
    if displayLayers:
        cmds.lockNode(displayLayers, lock=0)
        cmds.delete(displayLayers)
        [bscMethods.PythonMessage().traceResult(i) for i in displayLayers]


#
def setCleanRenderLayer():
    explain = u'''Clean Render - Layer'''
    bscMethods.PythonMessage().trace(explain)
    renderLayers = [i for i in cmds.ls(type='renderLayer') if i != 'defaultRenderLayer' and not cmds.referenceQuery(i, isNodeReferenced=1)]
    if renderLayers:
        cmds.lockNode(renderLayers, lock=0)
        cmds.delete(renderLayers)
        [bscMethods.PythonMessage().traceResult(i) for i in renderLayers]


#
def setCleanReferenceFile():
    explain = u'''Clean Reference - File(s)'''
    bscMethods.PythonMessage().trace(explain)
    referenceNodeLis = cmds.ls(type='reference')
    if referenceNodeLis:
        for referenceNode in referenceNodeLis:
            try:
                cmds.file(cmds.referenceQuery(referenceNode, filename=1), removeReference=1)
                bscMethods.PythonMessage().traceResult(referenceNode)
            except:
                pass


#
def setCleanReferenceNode():
    explain = u'''Clean Reference - Nde_Node(s)'''
    bscMethods.PythonMessage().trace(explain)
    referenceNodeLis = [i for i in cmds.ls(type="reference") if cmds.lockNode(i, q=1)]
    if referenceNodeLis:
        cmds.lockNode(referenceNodeLis, lock=0)
        cmds.delete(referenceNodeLis)
        [bscMethods.PythonMessage().traceResult(i) for i in referenceNodeLis]


# Link Component Main Object Group Step01
def linkComponentMainObjectGroupStep01(logWin, objectString, inData):
    dic = collections.OrderedDict()
    for data in inData:
        for componentObjectData, shadingEngine in data.items():
            # Link Component Object Group
            componentObject = '%s.%s' % (objectString, (componentObjectData.split('.')[-1]))
            if cmds.objExists(shadingEngine):
                dic.setdefault(shadingEngine, []).append(componentObject)
                qtLog.viewResult(logWin, componentObject, shadingEngine)
            else:
                qtLog.viewError(logWin, shadingEngine, u'Non - Exist')
    linkComponentSubObjectGroup(objectString, dic)


# Link Component Main Object Group Step 02
def linkComponentMainObjectGroupStep02(logWin, objectString, inData):
    dic = collections.OrderedDict()
    for data in inData:
        # Link Object Group
        for componentObjectData, shadingEngine in inData[0].items():
            if cmds.objExists(shadingEngine):
                cmds.sets(objectString, forceElement=shadingEngine)
                qtLog.viewResult(logWin, objectString, shadingEngine)
            else:
                qtLog.viewError(logWin, shadingEngine, u'Non - Exists')
        # Link Component Object Group
        for componentObjectData, shadingEngine in data.items():
            componentObject = '%s.%s' % (objectString, (componentObjectData.split('.')[-1]))
            if cmds.objExists(shadingEngine):
                dic.setdefault(shadingEngine, []).append(componentObject)
                qtLog.viewResult(logWin, componentObject, shadingEngine)
            else:
                qtLog.viewError(logWin, shadingEngine, u'Non - Exists')
    linkComponentSubObjectGroup(objectString, dic)


# Link Loop
def linkComponentSubObjectGroup(objectString, data):
    if data:
        for shadingEngine, objectLis in data.items():
            cmds.sets(objectLis, forceElement=shadingEngine)
        for shadingEngine, objectLis in data.items():
            linkData = cmds.sets(shadingEngine, query=1)
            linkObjects = []
            if linkData:
                linkObjects = [
                    i for i in linkData
                    if '.f[' in i
                    if i.startswith(objectString + '.')]
            elif not linkData:
                return True
            elif linkObjects == objectLis:
                return True
            elif linkObjects != objectLis:
                linkComponentSubObjectGroup(objectString, data)


# Get Arnold
def getMtoa():
    # noinspection PyUnresolvedReferences
    from mtoa.ui.globals.common import updateArnoldRendererCommonGlobalsTab
    updateArnoldRendererCommonGlobalsTab()


# Relink AOVs
def setRelinkArnoldAovs(maxDepth=50):
    if maUtils.isArnoldEnable():
        getMtoa()
        aovLists = ['%s.aovList[%s]' % ('defaultArnoldRenderOptions', i) for i in range(0, maxDepth)]
        for aovList in aovLists:
            if cmds.objExists(aovList):
                if not cmds.listConnections(aovList, source=1, connections=1):
                    aovs = maUtils.getNodeLisByType('aiAOV')
                    if aovs:
                        for i in aovs:
                            if not cmds.listConnections(i + '.message', destination=1, source=0):
                                try:
                                    cmds.connectAttr(i + '.message', aovList)
                                except:
                                    cmds.listConnections(i + '.message', destination=1, source=0)


# repair AOVs
def setRepairArnoldAovs(logWin, maxDepth=50):
    explain = u'''Repair AOVs'''
    qtLog.viewStartSubProcess(logWin, explain)
    #
    getMtoa()
    if maUtils.isArnoldEnable():
        aovLists = ['%s.aovList[%s]' % ('defaultArnoldRenderOptions', i) for i in range(0, maxDepth)]
        for aovList in aovLists:
            if cmds.objExists(aovList):
                if not cmds.listConnections(aovList, source=1, connections=1):
                    aovs = maUtils.getNodeLisByType('aiAOV')
                    if aovs:
                        for i in aovs:
                            if not cmds.listConnections(i + '.message', destination=1, source=0):
                                try:
                                    cmds.connectAttr(i + '.message', aovList)
                                    qtLog.viewResult(logWin, i, aovList)
                                except:
                                    cmds.listConnections(i + '.message', destination=1, source=0)
    #
    qtLog.viewCompleteSubProcess(logWin)


#
def setRebuildAov(aovData):
    getMtoa()
    importAttrConfig = [('defaultArnoldFilter.message', '.outputs[0].filter'), ('defaultArnoldDriver.message', '.outputs[0].driver')]
    for aovNode, aovName in aovData.items():
        if not maUtils.isAppExist(aovNode):
            maUtils.setCreateNode('aiAOV', aovNode)
            for sourceAttr, targetAttrName in importAttrConfig:
                targetAttr = aovNode + targetAttrName
                maUtils.setAttrConnect(sourceAttr, targetAttr)
                maUtils.setAttrStringDatumForce(aovNode, 'name', aovName)
    #
    setRelinkArnoldAovs()


#
def setSolverGroupGeometryHide(assetName, namespace=none):
    # Solver Group
    solverGroup = assetPr.astUnitModelSolverGroupName(assetName, namespace)
    forHide = maUtils.getNodeLisByType('mesh', 1, solverGroup)
    [maUtils.setHide(maUtils.getNodeTransform(i)) for i in forHide]


#
def setSolverFurGroup(assetName, namespace=none, hide=0):
    # Solver Group
    solverGroup = assetPr.astUnitModelSolverGroupName(assetName, namespace)
    # Solver Fur Group
    cfxGroup = assetPr.astUnitCfxLinkGroupName(assetName)
    #
    maUtils.setObjectParent(cfxGroup, solverGroup)
    # Set Grow Hide
    if hide:
        forHide = maUtils.getNodeLisByType('mesh', 1, cfxGroup)
        [maUtils.setHide(maUtils.getNodeTransform(i)) for i in forHide]


#
def setCreateAstExtraData(extraData):
    if extraData:
        if lxCore_.LynxiAttributeDataKey in extraData:
            attributeData = extraData[lxCore_.LynxiAttributeDataKey]
            setCreateAstAttributeData(attributeData)
        if lxCore_.LynxiConnectionDataKey in extraData:
            connectionDic = extraData[lxCore_.LynxiConnectionDataKey]
            setCreateAstExtraConnectionSub(connectionDic)
        if lxCore_.LynxiNhrConnectionDataKey in extraData:
            nhrConnectionDic = extraData[lxCore_.LynxiNhrConnectionDataKey]
            setCreateAstExtraConnectionSub(nhrConnectionDic)


#
def setCreateAstAttributeData(attributeData):
    if attributeData:
        for objectPath, (shapeNodeData, shapeCustomAttrData) in attributeData.items():
            if maUtils.isAppExist(objectPath):
                maAttr.setNodeDefAttrByData(objectPath, shapeNodeData, lockAttribute=False)
                maAttr.setObjectUserDefinedAttrs(objectPath, shapeCustomAttrData, lockAttribute=True)


#
def setCreateAstExtraConnectionSub(connectionDic):
    if connectionDic:
        # View Progress
        progressExplain = u'''Create Connection'''
        maxValue = len(connectionDic)
        progressBar = qtCommands.setProgressWindowShow(progressExplain, maxValue)
        for objectPath, connectionArray in connectionDic.items():
            if objectPath.startswith('|'):
                objectPath = objectPath[1:]
            #
            progressBar.updateProgress()
            if maUtils.isAppExist(objectPath):
                for sourceAttr, targetAttr in connectionArray:
                    if maUtils.isAppExist(sourceAttr) and maUtils.isAppExist(targetAttr):
                        if not cmds.isConnected(sourceAttr, targetAttr):
                            cmds.connectAttr(sourceAttr, targetAttr, force=1)


#
def setDisconnectNhrGuideObjectsConnection(assetName):
    nhrGuideObjects = datAsset.getAstUnitSolverNhrGuideObjects(assetName)
    if nhrGuideObjects:
        for nhrGuideObject in nhrGuideObjects:
            shapePath = maUtils.getNodeShape(nhrGuideObject)
            inputConnections = maUtils.getNodeInputConnectionLis(shapePath)
            if inputConnections:
                for sourceAttr, targetAttr in inputConnections:
                    if targetAttr.endswith('.inHairGrp'):
                        maUtils.setAttrDisconnect(sourceAttr, targetAttr)
            #
            outputConnections = maUtils.getNodeOutputConnectionLis(shapePath)
            if outputConnections:
                for sourceAttr, targetAttr in outputConnections:
                    if targetAttr.endswith('.inHairGrp'):
                        maUtils.setAttrDisconnect(sourceAttr, targetAttr)
