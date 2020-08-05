# coding=utf-8
import collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel

from LxBasic import bscMethods, bscObjects

from LxPreset import prsConfigure, prsMethods

from LxCore.preset.prod import assetPr

from LxMaya.command import maUtils, maGeom, maAttr

from LxMaya.product.data import datAsset

none = ''


# Clean Nde_Node By Name
def cleanNode(inData, nodeType):
    explain = u'Clean %s' % nodeType
    bscMethods.PyMessage.trace(explain)
    nodes = [i for i in inData if maUtils._isAppExist(i) and not maUtils.isReferenceNode(i)]
    if nodes:
        for node in nodes:
            if maUtils._isAppExist(node):
                cmds.lockNode(node, lock=0)
                cmds.delete(node)
                bscMethods.PyMessage.traceResult(node)


# Assign Default Shader
def setRootDefaultShaderCmd(rootString):
    logWin_ = bscObjects.LogWindow()
    logWin_.addStartProgress(u'Assign Default - Shader')
    cmds.sets(rootString, forceElement='initialShadingGroup')
    logWin_.addCompleteProgress()


# Assign Default Shaders
def setObjectDefaultShaderCmd(nodepathStrings):
    logWin_ = bscObjects.LogWindow()

    logWin_.addStartProgress(u'''Assign Initial - Shader''')
    for nodepathString in nodepathStrings:
        cmds.sets(nodepathString, forceElement='initialShadingGroup')
        cmds.sets(maUtils._dcc_getNodShapeNodepathStr(nodepathString), forceElement='initialShadingGroup')
        logWin_.addResult(maUtils._nodeString2nodename_(nodepathString), 'initialShadingGroup')
    logWin_.addCompleteProgress()


#
def setObjectTransparentRefresh(nodepathStrings):
    for objectPath in nodepathStrings:
        #
        attrDatum = maUtils.getAttrDatum(objectPath, 'primaryVisibility')
        maUtils.setAttrBooleanDatumForce(
            objectPath, prsConfigure.Product.VAR_product_attribute_object_renderable, attrDatum
        )
        #
        attrDatum = maUtils.getAttrDatum(objectPath, 'aiOpaque')
        maUtils.setAttrBooleanDatumForce(
            objectPath, prsConfigure.Product.VAR_product_attribute_object_transparent, not attrDatum
        )


# Clean Object's Unused Shape
def setObjectUnusedShapeClear(nodepathStrings):
    explain = u'''Clean Unused - Shape'''
    bscMethods.PyMessage.trace(explain)
    errorObjects = []
    # Get Error Objects
    for nodepathString in nodepathStrings:
        shapes = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=0, fullPath=1)
        if len(shapes) > 1:
            errorObjects.append(nodepathString)
    # Clean Error Objects's Shape
    if errorObjects:
        for nodepathString in errorObjects:
            shapes = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            usedShapes = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=1, fullPath=1)
            unusedShapes = [i for i in shapes if i and i not in usedShapes]
            if unusedShapes:
                for shape in unusedShapes:
                    cmds.delete(shape)
                    bscMethods.PyMessage.traceResult(maUtils._nodeString2nodename_(shape))


# Clean Unused Shader
def setUnusedShaderClear():
    mel.eval('MLdeleteUnused;')


# Unlock and Soft Normal
def setMeshVertexNormalUnlockCmd(nodepathStrings):
    explain = '''Unlock Mesh's Vertex Normal'''
    if nodepathStrings:
        maxValue = len(nodepathStrings)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for nodepathString in nodepathStrings:
            progressBar.update()
            maGeom.setMeshVertexNormalUnlock(nodepathString)


# Unlock and Soft Normal
def setMeshesSmoothNormal(nodepathStrings):
    explain = '''Soft ( Smooth ) Mesh's Edge'''
    if nodepathStrings:
        maxValue = len(nodepathStrings)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for nodepathString in nodepathStrings:
            progressBar.update()
            maGeom.setMeshEdgeSmooth(nodepathString, True)


# Clean Unknown Nde_Node
def setUnknownNodeClear():
    cleanNode(cmds.ls(type='unknown'), u'Unknown - Nde_Node')


#
def cleanUnusedAov():
    UnusedAov = []
    aovs = cmds.ls(type='aiAOV')
    if aovs and cmds.objExists('defaultArnoldRenderOptions'):
        aovUsed = maUtils._getNodeSourceNodeStringList('defaultArnoldRenderOptions', 'aiAOV')
        if aovUsed:
            UnusedAov = [aovs.remove(i) for i in aovUsed]
    cleanNode(UnusedAov, u'Unused Aovs')


#
def setDisplayLayerClear():
    explain = u'''Clean Display - Layer'''
    bscMethods.PyMessage.trace(explain)
    displayLayers = [i for i in cmds.ls(type='displayLayer') if i != 'defaultLayer' and cmds.getAttr(i + '.displayOrder') != 0 and not cmds.referenceQuery(i, isNodeReferenced=1)]
    if displayLayers:
        cmds.lockNode(displayLayers, lock=0)
        cmds.delete(displayLayers)
        [bscMethods.PyMessage.traceResult(i) for i in displayLayers]


#
def setCleanRenderLayer():
    explain = u'''Clean Render - Layer'''
    bscMethods.PyMessage.trace(explain)
    renderLayers = [i for i in cmds.ls(type='renderLayer') if i != 'defaultRenderLayer' and not cmds.referenceQuery(i, isNodeReferenced=1)]
    if renderLayers:
        cmds.lockNode(renderLayers, lock=0)
        cmds.delete(renderLayers)
        [bscMethods.PyMessage.traceResult(i) for i in renderLayers]


#
def setCleanReferenceFile():
    explain = u'''Clean Reference - File(s)'''
    bscMethods.PyMessage.trace(explain)
    referenceNodeLis = cmds.ls(type='reference')
    if referenceNodeLis:
        for referenceNode in referenceNodeLis:
            try:
                cmds.file(cmds.referenceQuery(referenceNode, filename=1), removeReference=1)
                bscMethods.PyMessage.traceResult(referenceNode)
            except:
                pass


#
def setCleanReferenceNode():
    explain = u'''Clean Reference - Nde_Node(s)'''
    bscMethods.PyMessage.trace(explain)
    referenceNodeLis = [i for i in cmds.ls(type="reference") if cmds.lockNode(i, q=1)]
    if referenceNodeLis:
        cmds.lockNode(referenceNodeLis, lock=0)
        cmds.delete(referenceNodeLis)
        [bscMethods.PyMessage.traceResult(i) for i in referenceNodeLis]


# Link Component Main Object Group Step01
def linkComponentMainObjectGroupStep01(nodepathString, inData):
    logWin_ = bscObjects.LogWindow()
    
    dic = collections.OrderedDict()
    for data in inData:
        for componentObjectData, shadingEngine in data.items():
            # Link Component Object Group
            componentObject = '%s.%s' % (nodepathString, (componentObjectData.split('.')[-1]))
            if cmds.objExists(shadingEngine):
                dic.setdefault(shadingEngine, []).append(componentObject)
                logWin_.addResult(componentObject, shadingEngine)
            else:
                logWin_.addError(shadingEngine, u'Non - Exist')
    linkComponentSubObjectGroup(nodepathString, dic)


# Link Component Main Object Group Step 02
def linkComponentMainObjectGroupStep02(nodepathString, inData):
    logWin_ = bscObjects.LogWindow()
    
    dic = collections.OrderedDict()
    for data in inData:
        # Link Object Group
        for componentObjectData, shadingEngine in inData[0].items():
            if cmds.objExists(shadingEngine):
                cmds.sets(nodepathString, forceElement=shadingEngine)
                logWin_.addResult(nodepathString, shadingEngine)
            else:
                logWin_.addError(shadingEngine, u'Non - Exists')
        # Link Component Object Group
        for componentObjectData, shadingEngine in data.items():
            componentObject = '%s.%s' % (nodepathString, (componentObjectData.split('.')[-1]))
            if cmds.objExists(shadingEngine):
                dic.setdefault(shadingEngine, []).append(componentObject)
                logWin_.addResult(componentObject, shadingEngine)
            else:
                logWin_.addError(shadingEngine, u'Non - Exists')
    linkComponentSubObjectGroup(nodepathString, dic)


# Link Loop
def linkComponentSubObjectGroup(nodepathString, data):
    if data:
        for shadingEngine, nodepathStrings in data.items():
            cmds.sets(nodepathStrings, forceElement=shadingEngine)
        for shadingEngine, nodepathStrings in data.items():
            linkData = cmds.sets(shadingEngine, query=1)
            linkObjects = []
            if linkData:
                linkObjects = [
                    i for i in linkData
                    if '.f[' in i
                    if i.startswith(nodepathString + '.')]
            elif not linkData:
                return True
            elif linkObjects == nodepathStrings:
                return True
            elif linkObjects != nodepathStrings:
                linkComponentSubObjectGroup(nodepathString, data)


# Get Arnold
def getMtoa():
    # noinspection PyUnresolvedReferences
    from mtoa.ui.globals.common import updateArnoldRendererCommonGlobalsTab
    updateArnoldRendererCommonGlobalsTab()


#
def setSolverGroupGeometryHide(assetName, namespace=none):
    # Solver Group
    solverGroup = assetPr.astUnitModelSolverGroupName(assetName, namespace)
    forHide = maUtils.getNodeLisByType('mesh', 1, solverGroup)
    [maUtils.setHide(maUtils._dcc_getNodTransformNodepathStr(i)) for i in forHide]


#
def setSolverFurGroup(assetName, namespace=none, hide=0):
    # Solver Group
    solverGroup = assetPr.astUnitModelSolverGroupName(assetName, namespace)
    # Solver Fur Group
    cfxGroup = prsMethods.Asset.groomLinkGroupName(assetName)
    #
    maUtils.setObjectParent(cfxGroup, solverGroup)
    # Set Grow Hide
    if hide:
        forHide = maUtils.getNodeLisByType('mesh', 1, cfxGroup)
        [maUtils.setHide(maUtils._dcc_getNodTransformNodepathStr(i)) for i in forHide]


#
def setCreateAstExtraData(extraData):
    if extraData:
        
        if prsConfigure.Product.DEF_key_info_attribute in extraData:
            attributeData = extraData[prsConfigure.Product.DEF_key_info_attribute]
            setCreateAstAttributeData(attributeData)
        if prsConfigure.Product.DEF_key_info_connection in extraData:
            connectionDic = extraData[prsConfigure.Product.DEF_key_info_connection]
            setCreateAstExtraConnectionSub(connectionDic)
        if prsConfigure.Product.DEF_key_info_nhrconnection in extraData:
            nhrConnectionDic = extraData[prsConfigure.Product.DEF_key_info_nhrconnection]
            setCreateAstExtraConnectionSub(nhrConnectionDic)


#
def setCreateAstAttributeData(attributeData):
    if attributeData:
        for objectPath, (shapeNodeData, shapeCustomAttrData) in attributeData.items():
            if maUtils._isAppExist(objectPath):
                maAttr.setNodeDefAttrByData(objectPath, shapeNodeData, lockAttribute=False)
                maAttr.setObjectUserDefinedAttrs(objectPath, shapeCustomAttrData, lockAttribute=True)


#
def setCreateAstExtraConnectionSub(connectionDic):
    if connectionDic:
        # View Progress
        progressExplain = u'''Create Connection'''
        maxValue = len(connectionDic)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for objectPath, connectionArray in connectionDic.items():
            if objectPath.startswith('|'):
                objectPath = objectPath[1:]
            #
            progressBar.update()
            if maUtils._isAppExist(objectPath):
                for sourceAttr, targetAttr in connectionArray:
                    if maUtils._isAppExist(sourceAttr) and maUtils._isAppExist(targetAttr):
                        if not cmds.isConnected(sourceAttr, targetAttr):
                            cmds.connectAttr(sourceAttr, targetAttr, force=1)


#
def setDisconnectNhrGuideObjectsConnection(assetName):
    nhrGuideObjects = datAsset.getAstUnitSolverNhrGuideObjects(assetName)
    if nhrGuideObjects:
        for nhrGuideObject in nhrGuideObjects:
            shapePath = maUtils._dcc_getNodShapeNodepathStr(nhrGuideObject)
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
