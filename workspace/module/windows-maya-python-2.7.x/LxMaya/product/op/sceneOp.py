# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscObjects
#
from LxCore import lxBasic, lxConfigure
#
from LxCore.config import sceneCfg
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import assetPr, scenePr
#
from LxMaya.command import maUtils, maObj, maAttr, maHier, maAsb
#
from LxMaya.product.data import datScene
#
none = ''


#
def setSceneCustomizeLabel(sceneName, data):
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if maUtils.isAppExist(scUnitRoot):
        maUtils.setAttrStringDatumForce(scUnitRoot, appVariant.basicCustomizeAttrLabel, data)


#
def setSceneRootIndex(sceneName, data):
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if maUtils.isAppExist(scUnitRoot):
        maUtils.setAttrStringDatumForce(scUnitRoot, appVariant.basicRootIndexAttrLabel, str(data))


# Camera
def setCreateSceneCamera(sceneName, sceneVariant):
    camera = scenePr.scSceneCameraName(sceneName, sceneVariant)
    maUtils.setCameraCreate(camera)
    maUtils.setNodeOverrideColor(camera, color=13)


#
def setAddSceneCameras(sceneName, cameras):
    sceneRoot = scenePr.scUnitRootGroupName(sceneName)
    #
    activeCameras = datScene.getScActiveCameraLis(sceneName)
    [activeCameras.append(i) for i in cameras if i not in activeCameras if maUtils.isAppExist(i)]
    #
    attrData = sceneCfg.CameraSep.join(activeCameras)
    maUtils.setAttrStringDatumForce_(sceneRoot, sceneCfg.SceneCameraAttr, attrData)


#
def setRemoveSceneCameras(sceneName, cameras):
    sceneLocator = scenePr.scUnitRootGroupName(sceneName)
    #
    activeCameras = datScene.getScActiveCameraLis(sceneName)
    [activeCameras.remove(i) for i in cameras if i in activeCameras]
    #
    attrData = sceneCfg.CameraSep.join(activeCameras)
    maUtils.setAttrStringDatumForce_(sceneLocator, sceneCfg.SceneCameraAttr, attrData)


#
def setClearConstraint(objectString, startFrame, endFrame, frameOffset):
    origObject = 'orig_%s_%s' % (cmds.nodeType(objectString), id(objectString))
    tempObject = 'temp_%s_%s' % (cmds.nodeType(objectString), id(objectString))
    #
    maUtils.setCurrentFrame(startFrame)
    # Copy to Temp with Connection
    cmds.duplicate(
        objectString,
        name=tempObject, returnRootsOnly=0, upstreamNodes=0, inputConnections=1
    )
    maUtils.setCleanChild(tempObject)
    maUtils.setParentToWorld(tempObject)
    # Unlock Transform
    maUtils.setObjectLockTransform(tempObject, 0)
    # Get Translate
    cmds.parentConstraint(objectString, tempObject)
    #
    cmds.bakeResults(
        tempObject,
        time=(startFrame - frameOffset, endFrame + frameOffset),
        simulation=1, shape=1
    )
    #
    cmds.delete(tempObject + '_parentConstraint1')
    #
    cmds.rename(tempObject, origObject)
    return origObject


# Create Camera Locator
def setCreateSceneCameraLocator(cameraLocator, camera, startFrame, endFrame, frameOffset):
    if cmds.objExists(cameraLocator):
        cmds.delete(cameraLocator)
    if not cmds.objExists(cameraLocator):
        cmds.spaceLocator(name=cameraLocator, position=(0, 0, 0))
        maUtils.setNodeOverrideColor(cameraLocator, color=13)
        #
        cmds.parentConstraint(camera, cameraLocator)
        maUtils.setObjectBakeKey(
            cameraLocator,
            startFrame, endFrame, frameOffset
        )
        cmds.delete(cameraLocator + '_parentConstraint1')


# Create Output Camera
def setCreateSceneOutputCamera(outputCamera, camera, startFrame, endFrame, frameOffset, isDeleteOrig=False):
    if cmds.objExists(outputCamera):
        cmds.delete(outputCamera)
    if not cmds.objExists(outputCamera):
        maUtils.setCurrentFrame(startFrame)
        # Copy
        cmds.duplicate(
            camera,
            name=outputCamera, returnRootsOnly=1, upstreamNodes=1
        )
        maUtils.setObjectLockTransform(outputCamera, 0)
        # Clean Transform Key
        maUtils.setObjectCleanTransformKey(outputCamera)
        # Back Shape Key
        maUtils.setObjectShapeBakeKey(outputCamera, startFrame, endFrame, frameOffset)
        #
        if isDeleteOrig:
            maUtils.setNodeDelete(camera)


#
def setScUnitCreateCameraOutputPositionSub(
        cameraObject, subLabel,
        sceneClass, sceneName, sceneVariant,
        startFrame, endFrame, frameOffset):
    outputObject = scenePr.scOutputCameraLocatorName(sceneName, sceneVariant) + subLabel
    subOutputObject = scenePr.scOutputCameraSubLocatorName(sceneName, sceneVariant) + subLabel
    #
    if maUtils.isAppExist(outputObject):
        maUtils.setNodeDelete(outputObject)
    #
    if maUtils.isAppExist(subOutputObject):
        maUtils.setNodeDelete(subOutputObject)
    #
    cmds.spaceLocator(name=outputObject, position=(0, 0, 0))
    maUtils.setNodeOverrideColor(outputObject, color=13)
    cmds.spaceLocator(name=subOutputObject, position=(0, 0, 0))
    maUtils.setNodeOverrideColor(subOutputObject, color=17)
    #
    cmds.parent(subOutputObject, outputObject)
    # Bake Key Frame
    maUtils.translateAnimationPosition(cameraObject, outputObject, startFrame, endFrame, frameOffset)
    return outputObject, subOutputObject


#
def setScUnitCreateCameraOutputAttributeSub(
        cameraObject, subLabel,
        sceneClass, sceneName, sceneVariant,
        startFrame, endFrame, frameOffset):
    outputObject = scenePr.scOutputCameraName(sceneName, sceneVariant) + subLabel
    #
    if maUtils.isAppExist(outputObject):
        maUtils.setNodeDelete(outputObject)
    #
    maObj.setCreateObject('camera', outputObject)
    #
    maObj.setCloneAttributes(cameraObject, outputObject, useShape=True)
    maObj.setCloneConnections(cameraObject, outputObject, useShape=True)
    #
    outputObjectShape = maUtils.getNodeShape(outputObject)
    maUtils.setObjectBakeKey(
        outputObjectShape,
        startFrame, endFrame, frameOffset
    )
    return outputObject


#
def setScCreateOutputCameraMain(
        cameraObject, subLabel,
        sceneClass, sceneName, sceneVariant,
        startFrame, endFrame, frameOffset,
        zAdjust=0.000000):
    outputLocatorObject, subOutputLocatorObject = setScUnitCreateCameraOutputPositionSub(
        cameraObject, subLabel,
        sceneClass, sceneName, sceneVariant,
        startFrame, endFrame, frameOffset
    )
    outputCameraObject = setScUnitCreateCameraOutputAttributeSub(
        cameraObject, subLabel,
        sceneClass, sceneName, sceneVariant,
        startFrame, endFrame, frameOffset
    )
    cmds.parent(outputCameraObject, subOutputLocatorObject)
    cmds.setAttr(outputCameraObject + '.translateZ', zAdjust)
    #
    maUtils.setObjectZeroTransform(outputCameraObject)
    maUtils.setObjectLockTransform(outputCameraObject, 1)


# Set Output Camera
def setSceneOutputCamera(camera, subLabel, sceneClass, sceneName, sceneVariant, startFrame, endFrame, frameOffset, isDeleteOrig=False, zAdjust=0.000000):
    # Step 01
    cameraLocatorObject = scenePr.scOutputCameraLocatorName(sceneName, sceneVariant) + subLabel
    setCreateSceneCameraLocator(
        cameraLocatorObject,
        camera,
        startFrame, endFrame, frameOffset
    )
    # Step 02
    outputCamera = scenePr.scOutputCameraName(sceneName, sceneVariant) + subLabel
    setCreateSceneOutputCamera(
        outputCamera,
        camera,
        startFrame, endFrame, frameOffset,
        isDeleteOrig
    )
    # Step 03
    cameraSubLocator = scenePr.scOutputCameraSubLocatorName(sceneName, sceneVariant) + subLabel
    if cmds.objExists(cameraSubLocator):
        cmds.delete(cameraSubLocator)
    elif not cmds.objExists(cameraSubLocator):
        maUtils.setCurrentFrame(startFrame)
        #
        cmds.duplicate(cameraLocatorObject, name=cameraSubLocator, returnRootsOnly=1)
        maUtils.setNodeOverrideColor(cameraSubLocator, color=17)
        cmds.parent(outputCamera, cameraSubLocator)
        cmds.parent(cameraSubLocator, cameraLocatorObject)
        cmds.setAttr(cameraSubLocator + '.translateZ', zAdjust)
        maUtils.setObjectZeroTransform(outputCamera)
        maUtils.setObjectLockTransform(outputCamera, 1)


#
def setScAstRigRefresh(sceneName, sceneVariant, sceneStage):
    if sceneName and sceneVariant:
        data = datScene.getScAnimAssetRefDic()
        if data:
            for referenceNode, (assetIndex, assetClass, assetName, number, assetVariant) in data.items():
                scAstRigNamespace = scenePr.scAstRigNamespace(sceneName, sceneVariant, assetName, number)
                scRigReferenceNode = scAstRigNamespace + 'RN'
                #
                namespace = maUtils.getReferenceNamespace(referenceNode)
                if not namespace == scAstRigNamespace:
                    maUtils.setReferenceNamespace(referenceNode, scAstRigNamespace)
                #
                if not referenceNode == scRigReferenceNode:
                    maUtils.setRenameForce(referenceNode, scRigReferenceNode)
                #
                astUnitRootGroup = assetPr.astUnitRootGroupName(assetName, scAstRigNamespace)
                #
                linkAssetPath = scenePr.scAssetSubGroupPath(sceneName, sceneVariant, sceneStage)
                scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
                #
                if not maUtils.isAppExist(scAstRootGroup):
                    # Create Group
                    maUtils.setAppPathCreate(scAstRootGroup)
                    #
                    timeTag = lxBasic.getOsActiveTimeTag()
                    maHier.refreshScAstUnitBranch(
                        scAstRootGroup,
                        assetIndex,
                        assetClass, assetName, number, assetVariant,
                        timeTag
                    )
                    maUtils.setNodeOutlinerRgb(scAstRootGroup, 0, 1, 1)
                    #
                    maUtils.setObjectParent(astUnitRootGroup, scAstRootGroup)
                    maUtils.setObjectParent(scAstRootGroup, linkAssetPath)


#
def setCreateScSceneryAssembly(data, root):
    if data:
        for i in data:
            objectPath, definition, namespace = i
            objectPath = objectPath[1:]
            #
            parentPath = maUtils._toNodeParentPath(objectPath)
            if parentPath:
                maUtils.setAppPathCreate(objectPath)
            objectName = maUtils._toNodeName(objectPath)
            if not maUtils.isAppExist(objectPath):
                maAsb.setAssemblyReferenceCreate(objectName, definition)
            #
            maUtils.setObjectParent(objectPath, root)


#
def setScSceneryAsbTransformation(data):
    if data:
        for subData in data:
            explain = '''Load Assembly Transformation(s)'''
            maxValue = len(subData)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for i in subData:
                progressBar.update()
                objectPath, transAttrData = i
                #
                if objectPath.startswith('|'):
                    objectPath = objectPath[1:]
                #
                maUtils.setObjectTransAttr(objectPath, transAttrData)


#
def setCreateScAstSolverExtra(extraData, sourceNamespace, targetNamespace):
    if extraData:
        if lxConfigure.LynxiAttributeDataKey in extraData:
            attributeData = extraData[lxConfigure.LynxiAttributeDataKey]
            setCreateScAstSolverAttribute(attributeData, targetNamespace)
        if lxConfigure.LynxiConnectionDataKey in extraData:
            connectionData = extraData[lxConfigure.LynxiConnectionDataKey]
            setCreateScAstSolverConnection(connectionData, sourceNamespace, targetNamespace)


#
def setCreateScAstSolverAttribute(data, namespace):
    if data:
        explain = '''Load Scene Asset ( Solver ) Attribute'''
        maxValue = len(data)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        for objectPath, (shapeNodeData, shapeCustomAttrData) in data.items():
            progressBar.update()
            objectPath = maUtils.getObjectPathJoinNamespace(objectPath, namespace)
            if maUtils.isAppExist(objectPath):
                maAttr.setNodeDefAttrByData(objectPath, shapeNodeData, lockAttribute=False)
                maAttr.setObjectUserDefinedAttrs(objectPath, shapeCustomAttrData, lockAttribute=False)


#
def setCreateScAstSolverConnection(data, sourceNamespace, targetNamespace):
    if data:
        explain = '''Load Scene Asset ( Solver ) Connection'''
        maxValue = len(data)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        for objectPath, connectionArray in data.items():
            progressBar.update()
            objectPath = maUtils.getObjectPathJoinNamespace(objectPath, targetNamespace)
            if maUtils.isAppExist(objectPath):
                for sourceAttr, targetAttr in connectionArray:
                    sourceAttr = maUtils.getNodeJoinNamespace(sourceAttr, sourceNamespace)
                    targetAttr = maUtils.getNodeJoinNamespace(targetAttr, targetNamespace)
                    if not maUtils.isAttrConnected(sourceAttr, targetAttr):
                        maUtils.setAttrConnect(sourceAttr, targetAttr)


#
def setScAstModelDisplayLayer(assetName, namespace, displayLater):
    hideLis = []
    #
    linGroup = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    lis = maUtils.getChildrenByRoot(linGroup)
    #
    if lis:
        for i in lis:
            attr = i + '.lxVisible'
            if maUtils.isAppExist(attr):
                boolean = maUtils.getAttrDatum(attr)
                if boolean is False:
                    hideLis.append(i)
    #
    if displayLater:
        if not maUtils.isAppExist(displayLater):
            maUtils.setCreateDisplayLayer(displayLater)
        #
        maUtils.setDisplayLayerColor(displayLater, color=(1, 1, .25))
        maUtils.setDisplayLayerVisible(displayLater, False)
        maUtils.setAddObjectToDisplayLayer(displayLater, hideLis)
    else:
        [maUtils.setHide(i) for i in hideLis]
