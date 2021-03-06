# coding=utf-8
import os
#
import sys
#
import collections
#
import glob
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel
# noinspection PyUnresolvedReferences
import maya.api.OpenMaya as OpenMaya
#
from random import choice
#
from itertools import product
#
from LxBasic import bscMethods
#
from LxCore.config import appCfg
#
DEF_mya_default_matrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
#
none = ''


#
def _string2list(string, includes=None):
    lis = []
    if isinstance(string, str) or isinstance(string, unicode):
        if includes:
            if string in includes:
                lis = [string]
        else:
            lis = [string]
    elif isinstance(string, tuple) or isinstance(string, list):
        for i in string:
            if includes:
                if i in includes:
                    lis.append(i)
            else:
                lis.append(i)
    return lis


# Get Application [ String ]
def isMayaApp():
    data = os.environ.get(u'MAYA_APP_DIR')
    if data:
        return True
    return False


# Get Maya SubVersion [ Bool ]
def is64():
    # Bool <True/False>
    return cmds.about(is64=1)


# Get Maya Version [ Str ]
def getMayaVersion():
    # Str <Maya Version>
    return str(cmds.about(apiVersion=1))[:4]


#
def setMayaAppClose(force=0):
    cmds.quit(force=force)


# Get List's Reduce
def getReduceList(lis):
    reduceLis = []
    [reduceLis.append(i) for i in lis if i not in reduceLis]
    return reduceLis


#
def getOsTextureUdimLis(textureFile):
    lis = []
    textureFile = textureFile.replace('<UDIM>', '<udim>')
    subTextureFileLis = glob.glob(textureFile.replace('<udim>', '[0-9][0-9][0-9][0-9]'))
    if subTextureFileLis:
        for i in subTextureFileLis:
            subTextureFile = i.replace('\\', '/')
            lis.append(subTextureFile)
    return lis


#
def getOsTextureSequenceLis(textureFile):
    lis = []
    subTextureFileLis = glob.glob(textureFile.replace('<f>', '[0-9][0-9][0-9][0-9]'))
    if subTextureFileLis:
        for i in subTextureFileLis:
            subTextureFile = i.replace('\\', '/')
            lis.append(subTextureFile)
    return lis


#
def isOsTextureExists(textureFile):
    boolean = False
    textureBasename = bscMethods.OsFile.basename(textureFile)
    if '<udim>' in textureBasename.lower():
        subTextureFileLis = getOsTextureUdimLis(textureFile)
        if subTextureFileLis:
            boolean = True
    elif '<f>' in textureBasename.lower():
        subTextureFileLis = getOsTextureSequenceLis(textureFile)
        if subTextureFileLis:
            boolean = True
    else:
        if bscMethods.OsFile.isExist(textureFile):
            boolean = True
    return boolean


#
def _isAppExist(nodepathString, attrName=none):
    if nodepathString:
        if attrName:
            nodepathString = nodepathString + '.' + attrName
        return cmds.objExists(nodepathString)


#
def isNodeLocked(nodepathString):
    return cmds.lockNode(nodepathString, query=1, lock=1)[0]


#
def setObjectAssassinShader(objectLis, shadingEngine):
    return cmds.sets(objectLis, forceElement=shadingEngine)


#
def isReferenceNode(node):
    return cmds.referenceQuery(node, isNodeReferenced=1)


#
def setNodeLock(nodepathString):
    cmds.lockNode(nodepathString, lock=1)


#
def setNodeUnlock(nodepathString):
    cmds.lockNode(nodepathString, lock=0)


#
def setObjectTransformationConnect(sourceTransform, targetTransform):
    attrNameLis = ['translate', 'rotate', 'scale']
    axisLis = ['X', 'Y', 'Z']
    visibleAttrName = 'visibility'
    #
    for attrName, axis in product(attrNameLis, axisLis):
        sourceAttr = '{}.{}{}'.format(sourceTransform, attrName, axis)
        targetAttr = '{}.{}{}'.format(targetTransform, attrName, axis)
        setAttrConnect(sourceAttr, targetAttr)
    #
    setAttrConnect('{}.{}'.format(sourceTransform, visibleAttrName), '{}.{}'.format(targetTransform, visibleAttrName))


#
def setNodeTemplate(nodepathString, boolean=True):
    attrName = 'template'
    attr = nodepathString + '.' + attrName
    cmds.setAttr(attr, boolean)


#
def setObjectTransformationAttr(nodepathString, lockTransformation=True, hideTransformation=True):
    attrNameLis = appCfg.MaTransformationAttrLis
    axisLis = ['X', 'Y', 'Z']
    [cmds.setAttr('{}.{}{}'.format(nodepathString, attrName, axis), keyable=0, lock=lockTransformation, channelBox=not hideTransformation) for attrName, axis in product(attrNameLis, axisLis)]


# Make Identity
def makeIdentity(nodepathString, mode, translate, rotate, scale):
    cmds.makeIdentity(nodepathString, apply=mode, translate=translate, rotate=rotate, scale=scale)


#
def setObjectTransformation(nodepathString):
    makeIdentity(nodepathString, 1, 1, 1, 1)
    makeIdentity(nodepathString, 0, 1, 1, 1)


# Set Transform
def setObjectsTransformationDefault(objectLis):
    [setObjectTransformation(nodepathString) for nodepathString in objectLis]


#
def setObjectDisplayMode(nodepathString, mode=0):
    if mode == 0:
        cmds.displaySmoothness(
            nodepathString,
            divisionsU=0,
            divisionsV=0,
            pointsWire=4,
            pointsShaded=1,
            polygonObject=1
        )
    elif mode == 1:
        cmds.displaySmoothness(
            nodepathString,
            divisionsU=3,
            divisionsV=3,
            pointsWire=16,
            pointsShaded=4,
            polygonObject=3
        )


#
def setObjectLockTransform(nodepathString, boolean=False):
    channels = ['.translate', '.rotate', '.scale']
    axisLis = ['X', 'Y', 'Z']
    [cmds.setAttr(nodepathString + channel + axis, lock=boolean) for channel, axis in product(channels, axisLis)]
    cmds.setAttr(nodepathString + '.visibility', lock=0)


# Unlock Transform
def setObjectsLockTransform(objectLis, boolean=False):
    [setObjectLockTransform(nodepathString, boolean) for nodepathString in objectLis]


#
def setObjectCleanTransformKey(nodepathString):
    channels = ['.translate', '.rotate', '.scale']
    axisLis = ['X', 'Y', 'Z']
    [cmds.cutKey(nodepathString + channel + axis) for channel, axis in product(channels, axisLis)]
    cmds.cutKey(nodepathString + '.visibility')


# Clean Transform Channel Key
def setObjectsCleanTransformKey(objectLis):
    [setObjectCleanTransformKey(nodepathString) for nodepathString in objectLis]


#
def setObjectZeroTransform(nodepathString, visible=1):
    channels = ['.translate', '.rotate', '.scale']
    cmds.setAttr(nodepathString + channels[0], 0, 0, 0)
    cmds.setAttr(nodepathString + channels[1], 0, 0, 0)
    cmds.setAttr(nodepathString + channels[2], 1, 1, 1)
    if visible:
        cmds.setAttr(nodepathString + '.visibility', 1)


# Set Transform Channel's to Zero
def setObjectsZeroTransform(objectLis, visible=1):
    [setObjectZeroTransform(nodepathString, visible) for nodepathString in objectLis]


# Bake Object Transform Channel's Keyframe
def setObjectBakeKey(maObjs, startFrame, endFrame, keyframeOffset=0):

    maObjs = bscMethods.String.toList(maObjs)
    if maObjs:
        cmds.bakeResults(
            *maObjs,
            time=(startFrame - keyframeOffset, endFrame + keyframeOffset),
            simulation=1
        )


# Bake Object Shape Channel's Keyframe
def setObjectShapeBakeKey(maObjs, startFrame, endFrame, keyframeOffset=0):
    maObjs = bscMethods.String.toList(maObjs)
    if maObjs:
        objectShapes = [_dcc_getNodShapeNodepathStr(i) for i in maObjs]
        cmds.bakeResults(
            *objectShapes,
            time=(startFrame - keyframeOffset, endFrame + keyframeOffset),
            simulation=1
        )


# set Rand Object Color
def setObjectRandColor(nodepathString):
    colorRange = range(0, 31)
    cmds.setAttr(nodepathString + '.overrideEnabled', 1)
    cmds.setAttr(nodepathString + '.overrideColor', choice(colorRange))


#
def setGpuShader(nodepathString, r, g, b, a):
    objectName = _nodeString2nodename_(nodepathString)
    shaderName = objectName + '_gpuShader'
    shadingEngineName = shaderName + 'SG'
    if not cmds.objExists(shaderName):
        cmds.shadingNode('blinn', n=shaderName, asShader=True)
        cmds.setAttr(shaderName + '.color', r, g, b)
        cmds.setAttr(shaderName + '.transparency', a, a, a)
        cmds.sets(renderable=1, noSurfaceShader=1, empty=1, n=shadingEngineName)
        cmds.connectAttr(shaderName + '.color', shadingEngineName + '.surfaceShader')
        cmds.sets(nodepathString, forceElement=shadingEngineName)


#
def setObjectsRandColor(objectLis):
    [setObjectRandColor(nodepathString) for nodepathString in objectLis]


#
def setObjectAnnotation(nodepathString, message):
    annotationName = nodepathString + '_annotationShape'
    cmds.createNode('annotationShape', name=annotationName, parent=nodepathString)
    annotationPath = nodepathString + appCfg.DEF_mya_node_pathsep + annotationName
    cmds.setAttr(annotationPath + '.text', message, type='string')
    cmds.setAttr(annotationPath + '.displayArrow', 0)
    shape = _dcc_getNodShapeNodepathStr(nodepathString)
    cmds.connectAttr(shape + '.worldMatrix[0]', annotationName + '.dagObjectMatrix[0]')


#
def isAttrLock(nodepathString, attrName=None):
    if attrName:
        attr = nodepathString + '.' + attrName
    else:
        attr = nodepathString
    #
    return cmds.connectionInfo(attr, isLocked=1)


#
def setAttrBooleanDatum(nodepathString, attrName, boolean):
    attr = nodepathString + '.' + attrName
    cmds.setAttr(attr, boolean)


#
def setAttrBooleanDatumForce(nodepathString, attrName, boolean):
    attr = nodepathString + '.' + attrName
    if not cmds.objExists(attr):
        cmds.addAttr(nodepathString, longName=attrName, niceName=bscMethods.StrCamelcase.toPrettify(attrName), attributeType='bool')
    #
    cmds.setAttr(attr, lock=0)
    cmds.setAttr(attr, boolean, lock=1)


#
def setAttrBooleanDatumForce_(nodepathString, attrName, boolean):
    isLock = False
    if isNodeLocked(nodepathString):
        isLock = True
        setNodeUnlock(nodepathString)
        setAttrBooleanDatumForce(nodepathString, attrName, boolean)
    if isLock:
        setNodeLock(nodepathString)


#
def setAttrLock(attr, boolean):
    if not isReferenceNode(attr):
        cmds.setAttr(attr, lock=boolean)


#
def setAttrDatumForce_(nodepathString, attrName, data):
    attr = nodepathString + '.' + attrName
    #
    isLock = isAttrLock(attr)
    if isLock:
        setAttrLock(attr, False)
    #
    cmds.setAttr(attr, data)
    #
    if isLock:
        setAttrLock(attr, True)


#
def setAttrAdd(nodepathString, attrName, attributeType, data):
    attr = nodepathString + '.' + attrName
    if not _isAppExist(attr):
        cmds.addAttr(nodepathString, longName=attrName, attributeType=attributeType)
    #
    setAttrDatumForce_(nodepathString, attrName, data)


#
def setKeyAttr(nodepathString, attrName, data):
    attr = nodepathString + '.' + attrName
    if not cmds.getAttr(attr, lock=1):
        cmds.setAttr(attr, data)


#
def setAttrStringDatum(nodepathString, attrName, data):
    attr = nodepathString + '.' + attrName
    if _isAppExist(attr):
        cmds.setAttr(attr, data, type='string')


#
def setAttrStringDatumForce(nodepathString, attrName, data):
    attr = nodepathString + '.' + attrName
    if not cmds.objExists(attr):
        cmds.addAttr(nodepathString, longName=attrName, niceName=bscMethods.StrCamelcase.toPrettify(attrName), dataType='string')
    cmds.setAttr(attr, lock=0)
    cmds.setAttr(attr, data, type='string', lock=1)


#
def setAttrStringDatumForce_(nodepathString, attrName, data):
    isLock = False
    if isNodeLocked(nodepathString):
        isLock = True
        setNodeUnlock(nodepathString)
    setAttrStringDatumForce(nodepathString, attrName, data)
    if isLock:
        setNodeLock(nodepathString)


#
def getAttrDatum(nodepathString, attrName=none):
    if attrName:
        attr = nodepathString + '.' + attrName
    else:
        attr = nodepathString
    #
    if cmds.objExists(attr):
        return cmds.getAttr(attr)


#
def getNodeAttrModifyDatumLis(node):
    lis = []
    #
    attrNames = cmds.listAttr(node, read=1, write=1, connectable=1, scalar=1)
    if attrNames:
        for attrName in attrNames:
            attr = node + '.' + attrName
            if _isAppExist(attr):
                value = cmds.getAttr(attr)
                dataType = str(type(value))[7:-2]
                lis.append((attrName, value, dataType))
    return lis


#
def setCameraCreate(name):
    mCamera = cmds.camera(
        centerOfInterest=5,
        focalLength=35,
        lensSqueezeRatio=1,
        cameraScale=1,
        horizontalFilmAperture=1.41732,
        horizontalFilmOffset=0,
        verticalFilmAperture=0.94488,
        verticalFilmOffset=0,
        filmFit='Fill',
        overscan=1,
        motionBlur=0,
        shutterAngle=144,
        nearClipPlane=0.1,
        farClipPlane=10000,
        orthographic=0,
        orthographicWidth=30,
        panZoomEnabled=0,
        horizontalPan=0,
        verticalPan=0,
        zoom=1
    )
    transform = mCamera[0]
    cmds.rename(transform, name)


#
def setObjectAddParentGroup(child, parent):
    cmds.group(empty=1, name=parent)
    setNodeOutlinerRgb(parent, 0, 1, 0)
    cmds.parent(child, parent)


#
def setObjectAddChildGroup(child, parent):
    if not cmds.objExists(child) and cmds.objExists(parent):
        cmds.group(empty=1, name=child, parent=parent)
        setNodeOutlinerRgb(child, 0, 1, 0)


# Get Cameras
def getCameras(fullPath=True):
    # List [ <Camera> ]
    cameras = []
    data = cmds.ls(type='camera', long=fullPath)
    for i in data:
        transform = _dcc_getNodTransformNodepathStr(i, fullPath)
        cameras.append(transform)
    return cameras


# Get Object's Parent
def getObjectParent(nodepathString, fullPath=True):
    parent = cmds.listRelatives(nodepathString, parent=1, fullPath=fullPath)
    if parent:
        return parent[0]


# Get Object's Children
def getNodeChildLis(nodepathString, fullPath=True):
    lis = []
    if _isAppExist(nodepathString):
        lis = cmds.listRelatives(nodepathString, children=1, fullPath=fullPath) or []
    return lis


#
def getObjectChildrenCount(nodepathString):
    children = getNodeChildLis(nodepathString, 1)
    return len(children)


# Get Object's Children
def getObjectChildObjectLis(nodepathString, mType=appCfg.DEF_mya_type_transform, fullPath=True):
    objectLis = cmds.listRelatives(nodepathString, children=1, type=mType, fullPath=fullPath)
    return objectLis


#
def getObjectChildObjects(nodepathString, filterTypes, fullPath=True):
    lis = []
    filterTypes = bscMethods.String.toList(filterTypes)
    children = cmds.listRelatives(nodepathString, children=1, type=appCfg.DEF_mya_type_transform, fullPath=fullPath)
    if children:
        for child in children:
            if getTransformType(child) in filterTypes:
                lis.append(child)
    return lis


# Get Object's Transform
def _dcc_getNodTransformNodepathStr(nodepathString, fullPath=True):
    if _isAppExist(nodepathString):
        if _getNodeCategoryString(nodepathString) == appCfg.DEF_mya_type_transform:
            if fullPath:
                return _dcc_getNodFullpathNodepathStr(nodepathString)
            if not fullPath:
                return _nodeString2nodename_(nodepathString)
        else:
            transforms = cmds.listRelatives(nodepathString, parent=1, fullPath=fullPath)
            if transforms:
                return transforms[0]


#
def _toTransformByNodePath(nodePath):
    return appCfg.DEF_mya_node_pathsep.join(nodePath.split(appCfg.DEF_mya_node_pathsep)[:-1])


#
def _toNamespaceByNodePath(objectPath):
    return appCfg.DEF_mya_node_namespace_pathsep.join(objectPath.split(appCfg.DEF_mya_node_pathsep)[-1].split(appCfg.DEF_mya_node_namespace_pathsep)[:-1])


# Get Object's Shape
def _dcc_getNodShapeNodepathStr(nodepathString, fullPath=True):
    if _isAppExist(nodepathString):
        if _getNodeCategoryString(nodepathString) == appCfg.DEF_mya_type_transform:
            shapes = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=1, fullPath=fullPath)
            if shapes:
                return shapes[0]
        if not _getNodeCategoryString(nodepathString) == appCfg.DEF_mya_type_transform:
            if fullPath:
                return _dcc_getNodFullpathNodepathStr(nodepathString)
            if not fullPath:
                return _nodeString2nodename_(nodepathString)


#
def getChildObjectsByRoot(root, filterTypes, fullPath=True):
    def getBranch(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                objectType = getTransformType(child)
                if objectType in filterTypes:
                    lis.append(child)
                getBranch(child)
    #
    lis = []
    filterTypes = bscMethods.String.toList(filterTypes)
    if _isAppExist(root):
        getBranch(root)
    return lis


#
def getChildNodesByRoot(root, filterTypes, fullPath=True):
    # Sub Method
    def getChild(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                nodeType = _getNodeCategoryString(child)
                if nodeType in typeLis:
                    lis.append(child)
                #
                getChild(child)
    lis = []
    #
    typeLis = bscMethods.String.toList(filterTypes)
    if _isAppExist(root):
        getChild(root)
    return lis


#
def getChildTransformLisByGroup(root, fullPath=True):
    # Sub Method
    def getChild(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                if _getNodeIsTransform(child):
                    lis.append(child)
                getChild(child)
    lis = []
    getChild(root)
    return lis


#
def getChildShapesByRoot(root, filterTypes, fullPath=True):
    lis = []
    def getChild(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                objectType = getTransformType(child)
                if objectType in filterTypes:
                    shapes = getMainShapes(child, fullPath)
                    lis.extend(shapes)
                getChild(child)
    #
    filterTypes = bscMethods.String.toList(filterTypes)
    if _isAppExist(root):
        getChild(root)
    return lis


#
def getGroupLisByRoot(root, fullPath=True):
    def getChild(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                if _getNodeIsGroup(child):
                    lis.append(child)
                getChild(child)
    useRoot = root
    if fullPath:
        useRoot = _dcc_getNodFullpathNodepathStr(root)
    lis = [useRoot]
    if _isAppExist(root):
        getChild(root)
    return lis


#
def getChildGroupLisByGroup(root, fullPath=True):
    def getChild(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                if _getNodeIsGroup(child):
                    lis.append(child)
    useRoot = root
    if fullPath:
        useRoot = _dcc_getNodFullpathNodepathStr(root)
    lis = []
    if _isAppExist(useRoot):
        getChild(useRoot)
    return lis


#
def setEmptyGroupClear(root):
    if _isAppExist(root):
        childGroups = getGroupLisByRoot(root)
        childGroups.reverse()
        for i in childGroups:
            childObjects = getObjectChildObjectLis(i)
            if not childObjects:
                setNodeDelete(i)


#
def getChildrenByRoot(root, fullPath=True):
    # Sub Method
    def getChild(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                lis.append(child)
                getChild(child)
    #
    lis = []
    if _isAppExist(root):
        getChild(root)
    return lis


#
def getRootCompose(root, fullPath=True):
    # Sub Method
    def getChild(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                lis.append(child)
                getChild(child)

    #
    lis = []
    if _isAppExist(root):
        rootPath = _dcc_getNodFullpathNodepathStr(root)
        lis = [rootPath]
        getChild(rootPath)
    return lis


#
def getNonRefChildObjectsByRoot(root, nodeType, fullPath=True):
    lis = []
    def getChild(parent):
        children = getNodeChildLis(parent, fullPath)
        if children:
            for child in children:
                if getTransformType(child) == nodeType:
                    if not isReferenceNode(child):
                        lis.append(child)
                getChild(child)
    #
    if _isAppExist(root):
        getChild(root)
    return lis


#
def setCleanupHierarchy(root, exceptObjectTypes):
    needCleanNode = []
    children = getChildrenByRoot(root, 1)
    #
    if children:
        for child in children:
            if not _getNodeIsGroup(child):
                if not _getNodeShapeCategoryString(child) in exceptObjectTypes:
                    needCleanNode.append(child)
    #
    if needCleanNode:
        needCleanNode.reverse()
        for node in needCleanNode:
            if _isAppExist(node):
                setNodeDelete(node)


#
def setCleanSceneDirty():
    return cmds.dgdirty(allPlugs=1)


#
def getObjectPathJoinNamespace(objectPath, namespace):
    isFullPath = objectPath.startswith(appCfg.DEF_mya_node_pathsep)
    if isFullPath:
        return (appCfg.DEF_mya_node_pathsep + namespace + ':').join(objectPath.split(appCfg.DEF_mya_node_pathsep))
    elif not isFullPath:
        return namespace + ':' + (appCfg.DEF_mya_node_pathsep + namespace + ':').join(objectPath.split(appCfg.DEF_mya_node_pathsep))


#
def getObjectPathRemoveNamespace(objectPath):
    paths = [i.split(appCfg.DEF_mya_node_namespace_pathsep)[-1] for i in objectPath.split(appCfg.DEF_mya_node_pathsep)]
    return appCfg.DEF_mya_node_pathsep.join(paths)


#
def getNodeJoinNamespace(nodepathString, namespace):
    return namespace + ':' + nodepathString


#
def getObjectStringJoinNamespace(nodepathString, namespace):
    if appCfg.DEF_mya_node_pathsep in nodepathString:
        return getObjectPathJoinNamespace(nodepathString, namespace)
    else:
        return getNodeJoinNamespace(nodepathString, namespace)


#
def getTranslateVector(nodepathString):
    data = cmds.getAttr(nodepathString + '.translate')
    if data:
        return data[0]


#
def getRotateVector(nodepathString):
    data = cmds.getAttr(nodepathString + '.rotate')
    if data:
        return data[0]


#
def getScaleVector(nodepathString):
    data = cmds.getAttr(nodepathString + '.scale')
    if data:
        return data[0]


#
def getLocalPivotVector(nodepathString):
    data = cmds.getAttr(nodepathString + '.rotatePivot')
    if data:
        return data[0]


#
def getLocalScalePivotVector(nodepathString):
    data = cmds.getAttr(nodepathString + '.scalePivot')
    if data:
        return data[0]


#
def getWorldPivotVector(nodepathString):
    _bx, _by, _bz, bx, by, bz = cmds.exactWorldBoundingBox(nodepathString)
    px, py, pz = getLocalPivotVector(nodepathString)
    lpx, lpy, lpz = (_bx + bx - px), (_by + by - py), (_bz + bz - pz)
    tx, ty, tz = getTranslateVector(nodepathString)
    px, py, pz = getLocalPivotVector(nodepathString)
    wpx, wpy, wpz = lpx - tx, lpy - ty, lpz - tz
    return wpx, wpy, wpz


#
def setRotatePivot(nodepathString, data):
    if data:
        cmds.setAttr(nodepathString + '.rotatePivot', data[0], data[1], data[2])


#
def setScalePivot(nodepathString, data):
    if data:
        cmds.setAttr(nodepathString + '.scalePivot', data[0], data[1], data[2])


#
def getPivot(nodepathString, targetObject):
    targetRotatePivotData = getLocalPivotVector(targetObject)
    if targetRotatePivotData:
        setRotatePivot(nodepathString, targetRotatePivotData)
    #
    targetScalePivotData = getLocalScalePivotVector(targetObject)
    if targetScalePivotData:
        setScalePivot(nodepathString, targetScalePivotData)


# Get Position
def getPosition(nodepathString, targetObject, keepConstraint=False):
    cmds.parentConstraint(targetObject, nodepathString)
    if not keepConstraint:
        constraint = nodepathString + '_parentConstraint1'
        if ':' in nodepathString:
            constraint = nodepathString.split(':')[-1] + '_parentConstraint1'
        cmds.delete(constraint)


# Get Scale
def getScale(nodepathString, targetObject, keepConstraint=False):
    cmds.scaleConstraint(targetObject, nodepathString)
    if not keepConstraint:
        constraint = nodepathString + '_scaleConstraint1'
        if ':' in nodepathString:
            constraint = nodepathString.split(':')[-1] + '_scaleConstraint1'
        cmds.delete(constraint)


#
def getAnimationKey(nodepathString, targetObject, startFrame, endFrame, frameOffset=0):
    tempLocator = 'temp_locator'
    if cmds.objExists(tempLocator):
        cmds.delete(tempLocator)
    cmds.spaceLocator(name='temp_locator')
    cmds.parent(tempLocator, targetObject)
    setObjectZeroTransform(tempLocator, visible=0)
    #
    cmds.parentConstraint(tempLocator, nodepathString)
    cmds.scaleConstraint(tempLocator, nodepathString)
    #
    setObjectBakeKey(nodepathString, startFrame, endFrame, frameOffset)
    #
    parentConstraint = nodepathString + '_parentConstraint1'
    scaleConstraint = nodepathString + '_scaleConstraint1'
    if ':' in nodepathString:
        parentConstraint = nodepathString.split(':')[-1] + '_parentConstraint1'
        scaleConstraint = nodepathString.split(':')[-1] + '_scaleConstraint1'
    cmds.delete(parentConstraint)
    cmds.delete(scaleConstraint)
    cmds.delete(tempLocator)


#
def _dcc_getNodFullpathNodepathStr(nodepathString):
    string = nodepathString
    isPath = nodepathString.startswith(appCfg.DEF_mya_node_pathsep)
    if not isPath:
        data = cmds.ls(nodepathString, long=1)
        if data:
            string = data[0]
    return string


#
def isObjectPath(string):
    return string.startswith(appCfg.DEF_mya_node_pathsep)


#
def _nodeString2nodename_(objectPath, useMode=0):
    string = none
    if useMode == 0:
        string = objectPath.split(appCfg.DEF_mya_node_pathsep)[-1]
    elif useMode == 1:
        string = objectPath.split(appCfg.DEF_mya_node_pathsep)[-1].split(appCfg.DEF_mya_node_namespace_pathsep)[-1]
    return string


#
def getObjectRelativePath(rootPath, objectPath):
    splitKey = _nodeString2nodename_(rootPath)
    string = rootPath + objectPath.split(splitKey)[-1]
    return string


#
def _toNodeParentPath(nodepathString):
    string = None
    objectPath = _dcc_getNodFullpathNodepathStr(nodepathString)
    if objectPath:
        data = appCfg.DEF_mya_node_pathsep.join(objectPath.split(appCfg.DEF_mya_node_pathsep)[:-1])
        if data:
            string = data
    return string


#
def getObjectRowIndex(nodepathString):
    integer = 0
    parent = _toNodeParentPath(nodepathString)
    children = getNodeChildLis(parent, fullPath=True)
    if children:
        objectPath = _dcc_getNodFullpathNodepathStr(nodepathString)
        if objectPath in children:
            integer = int(children.index(objectPath))
    return integer


# Get Transform's Shape
def _getNodeShapeNodeStringList(transform, fullPath=True):
    shapes = cmds.listRelatives(transform, children=1, shapes=1, noIntermediate=0, fullPath=fullPath)
    return shapes


# Get Transform's Shape
def getMainShapes(transform, fullPath=True):
    shapes = cmds.listRelatives(transform, children=1, shapes=1, noIntermediate=1, fullPath=fullPath)
    return shapes


#
def getAttrName(attr):
    attrName = '.'.join(attr.split('.')[1:])
    return attrName


#
def setObjectTransferInputConnections(sourceObject, targetObject):
    inputConnectionLis = getNodeInputConnectionLis(sourceObject)
    if inputConnectionLis:
        for outputAttr, inputAttr in inputConnectionLis:
            targetAttrName = getAttrName(inputAttr)
            targetAttr = targetObject + '.' + targetAttrName
            if _isAppExist(targetAttr):
                if not isAttrLock(targetAttr):
                    setAttrConnect(outputAttr, targetAttr)


#
def setObjectClearInputTransformationConnection(nodepathString):
    attrNameLis = appCfg.MaTransformationAttrLis
    axisLis = ['X', 'Y', 'Z']
    for attrName, axis in product(attrNameLis, axisLis):
        attr = nodepathString + '.' + attrName + axis
        if _isAppExist(attr):
            inputConnectionLis = getNodeInputConnectionLis(attr)
            for sourceAttr, targetAttr in inputConnectionLis:
                if isAttrConnected(sourceAttr, targetAttr):
                    setAttrDisconnect(sourceAttr, targetAttr)
        if attrName == 'scale':
            cmds.setAttr(attr, 1)
        else:
            cmds.setAttr(attr, 0)


#
def setMeshTransfer(sourceObject, targetObject):
    sourceShape = _dcc_getNodShapeNodepathStr(sourceObject, True)
    targetShape = _dcc_getNodShapeNodepathStr(targetObject, True)
    sourceAttr = sourceShape + '.worldMesh'
    targetAttr = targetShape + '.inMesh'
    setAttrConnect(sourceAttr, targetAttr)


#
def setObjectTransferTransformation(sourceObject, targetObject):
    attrDataArray = getObjectTransformation_(sourceObject)
    if attrDataArray:
        for attData in attrDataArray:
            attr, data = attData
            attrName = getAttrName(attr)
            targetAttr = targetObject + '.' + attrName
            if _isAppExist(targetAttr):
                if not isAttrLock(targetAttr) and not isAttrDestination(targetAttr):
                    cmds.setAttr(targetAttr, data)


#
def setObjectTransferVisibility(sourceObject, targetObject):
    sourceAttr = sourceObject + '.visibility'
    targetAttr = targetObject + '.visibility'
    if _isAppExist(targetAttr):
        if not isAttrLock(targetAttr) and not isAttrDestination(targetAttr):
            data = cmds.getAttr(sourceAttr)
            cmds.setAttr(targetAttr, data)


#
def setObjectClearInputVisibleConnection(nodepathString):
    attr = nodepathString + '.visibility'
    #
    inputConnectionLis = getNodeInputConnectionLis(attr)
    if inputConnectionLis:
        for sourceAttr, targetAttr in inputConnectionLis:
            if isAttrConnected(sourceAttr, targetAttr):
                setAttrDisconnect(sourceAttr, targetAttr)
    #
    cmds.setAttr(attr, 1)


# Get Input Nde_Node ( Method )
def _getNodeSourceNodeStringList(nodepathString, nodeTypeString=None):
    if nodeTypeString is not None:
        return cmds.listConnections(nodepathString, destination=0, source=1, type=nodeTypeString) or []
    return cmds.listConnections(nodepathString, destination=0, source=1) or []


#
def getInputNodesFilterByType(nodepathString, filterTypes):
    def getBranch(subObjStr):
        searchNodes = [subObjStr, _dcc_getNodShapeNodepathStr(subObjStr)]
        set(searchNodes)
        for subNode in searchNodes:
            inputNodes = cmds.listConnections(subNode, destination=0, source=1, shapes=1)
            if inputNodes:
                for inputNode in inputNodes:
                    #
                    nodeType = _getNodeCategoryString(inputNode)
                    if nodeType in filterTypes:
                        if not inputNode in lis:
                            lis.append(inputNode)
                    #
                    if not inputNode in searchLis:
                        searchLis.append(inputNode)
                        getBranch(inputNode)
    #
    searchLis = []
    #
    lis = []
    #
    filterTypes = bscMethods.String.toList(filterTypes)
    #
    getBranch(nodepathString)
    #
    return lis


#
def setObjectAddPositionChoice(namespace, nodepathString):
    origLocatorName = namespace + ':' + 'origPosition_locator'
    userLocatorName = namespace + ':' + 'userPosition_locator'
    choiceNodeName = namespace + ':' + 'position_choice'
    decomposeMatrixName = namespace + ':' + 'position_decomposeMatrix'
    if not cmds.objExists(origLocatorName):
        cmds.spaceLocator(name=origLocatorName, position=(0, 0, 0))
        #
        setObjectClearInputTransformationConnection(origLocatorName)
        setObjectClearInputVisibleConnection(origLocatorName)
        #
        setObjectTransferTransformation(nodepathString, origLocatorName)
        setObjectTransferVisibility(nodepathString, origLocatorName)
        #
        setObjectTransferInputConnections(nodepathString, origLocatorName)
        #
        setObjectLockTransform(origLocatorName, True)
    #
    if not cmds.objExists(userLocatorName):
        cmds.spaceLocator(name=userLocatorName, position=(0, 0, 0))
    #
    if not cmds.objExists(choiceNodeName):
        cmds.createNode('choice', name=choiceNodeName)
        cmds.createNode('decomposeMatrix', name=decomposeMatrixName)
        #
        cmds.connectAttr(origLocatorName + '.worldMatrix[0]', choiceNodeName + '.input[0]')
        cmds.connectAttr(userLocatorName + '.worldMatrix[0]', choiceNodeName + '.input[1]')
        #
        cmds.connectAttr(choiceNodeName + '.output', decomposeMatrixName + '.inputMatrix')
        #
        connectDatumLis = [
            ('outputTranslate', 'translate'),
            ('outputRotate', 'rotate'),
            ('outputScale', 'scale')
        ]
        setObjectClearInputTransformationConnection(nodepathString)
        for sourceAttr, targetAttr in connectDatumLis:
            cmds.connectAttr(decomposeMatrixName + '.' + sourceAttr, nodepathString + '.' + targetAttr)


#
def getInputShapeLis(nodepathString, filterType=none):
    lis = []
    #
    guessData = cmds.listConnections(nodepathString, destination=0, source=1, shapes=1, type=filterType)
    if guessData:
        for i in guessData:
            if _getNodeIsTransform(i) or _getNodeIsShape(i):
                lis.append(_dcc_getNodFullpathNodepathStr(i))
            else:
                lis.append(i)
    return lis


# List [ <Output Connection Nde_Node> ]
def _getNodeTargetNodeStringList(nodepathString, filterType=none):
    return cmds.listConnections(nodepathString, destination=1, source=0, type=filterType) or []


#
def getOutputShapes(nodepathString, filterType=none):
    lis = []
    guessData = cmds.listConnections(nodepathString, destination=1, source=0, type=filterType, shapes=1)
    if guessData:
        for i in guessData:
            if _getNodeIsTransform(i) or _getNodeIsShape(i):
                lis.append(_dcc_getNodFullpathNodepathStr(i))
            else:
                lis.append(i)
    return lis


#
def getInputAttrByAttr(attr):
    lis = []
    data = cmds.listConnections(attr, destination=0, source=1, connections=1, plugs=1)
    if data:
        for seq, i in enumerate(data):
            if seq % 2:
                sourceAttr = i
                lis.append(sourceAttr)
    return lis


#
def getInputNodeLisByAttr(attr):
    return cmds.listConnections(attr, destination=0, source=1) or []


#
def getOutputNodeLisByAttr(attr):
    return cmds.listConnections(attr, destination=1, source=0) or []


#
def getInputObjectsByAttrName(nodepathString, filterAttrNames=None):
    lis = []
    filterAttrNames = bscMethods.String.toList(filterAttrNames)
    #
    if _isAppExist(nodepathString):
        guessData = cmds.listConnections(nodepathString, destination=0, source=1, connections=1)
        if guessData:
            inputAttrs = []
            if filterAttrNames:
                for attrName in filterAttrNames:
                    subInputConnections = [i for i in guessData if attrName in i]
                    inputAttrs.extend(subInputConnections)
            else:
                inputAttrs = guessData
            #
            if inputAttrs:
                for inputConnection in inputAttrs:
                    inputObjects = getInputNodeLisByAttr(inputConnection)
                    lis.extend(inputObjects)
    return lis


#
def getOutputNodeLisFilter(nodepathString, attrNames=none):
    # List [ <Output Nde_Node> ]
    nodes = []
    if _isAppExist(nodepathString):
        guessData = cmds.listConnections(nodepathString, destination=1, source=0, connections=1)
        if guessData:
            outputConnections = [i for i in guessData if attrNames in i]
            if outputConnections:
                for outputConnection in outputConnections:
                    outputNodes = _getNodeTargetNodeStringList(outputConnection)
                    nodes.extend(outputNodes)
    return nodes


#
def getInputAttrFilterByAttrName(nodepathString, filterAttrNames=None):
    lis = []
    filterAttrNames = bscMethods.String.toList(filterAttrNames)
    #
    guessData = cmds.listConnections(nodepathString, destination=0, source=1, connections=1)
    if guessData:
        if filterAttrNames:
            for attrName in filterAttrNames:
                lis = [i for i in guessData if attrName in i]
        else:
            lis = guessData
    #
    return lis


#
def getNodeInputConnectionLis(nodepathString):
    lis = []
    data = cmds.listConnections(nodepathString, destination=0, source=1, connections=1, plugs=1)
    if data:
        for seq, i in enumerate(data):
            if seq % 2:
                sourceAttr = i
                targetAttr = data[seq - 1]
                #
                lis.append((sourceAttr, targetAttr))
    return lis


#
def getNodeOutputConnectionLis(nodepathString):
    lis = []
    data = cmds.listConnections(nodepathString, destination=1, source=0, connections=1, plugs=1)
    if data:
        for seq, i in enumerate(data):
            if seq % 2:
                sourceAttr = data[seq - 1]
                targetAttr = i
                #
                lis.append((sourceAttr, targetAttr))
    return lis


#
def getInputConnectionsFilterByNamespace(node, filterNamespace):
    lis = []
    data = cmds.listConnections(node, destination=0, source=1, connections=1, plugs=1)
    if data:
        for seq, i in enumerate(data):
            if seq % 2:
                sourceAttr = i
                targetAttr = data[seq - 1]
                if not sourceAttr.startswith(filterNamespace):
                    lis.append((sourceAttr, targetAttr))
    return lis


#
def getOutputConnectionsFilterByNamespace(node, filterNamespace):
    lis = []
    data = cmds.listConnections(node, destination=1, source=0, connections=1, plugs=1)
    if data:
        for seq, i in enumerate(data):
            if seq % 2:
                sourceAttr = data[seq - 1]
                targetAttr = i
                if not targetAttr.startswith(filterNamespace):
                    lis.append((sourceAttr, targetAttr))
    return lis


#
def getObjectTransformation_(nodepathString):
    lis = []
    attrNameLis = appCfg.MaTransformationAttrLis
    axisLis = ['X', 'Y', 'Z']
    for channel, axis in product(attrNameLis, axisLis):
        attr = nodepathString + '.' + channel + axis
        if _isAppExist(attr):
            data = cmds.getAttr(attr)
            lis.append((attr, data))
    #
    visibilityAttr = nodepathString + '.' + 'visibility'
    visibilityData = cmds.getAttr(visibilityAttr)
    lis.append((visibilityAttr, visibilityData))
    return lis


#
def getObjectLocalPath(root, objectPath):
    if not root.startswith('|'):
        root = '|' + root
    #
    rootName = _nodeString2nodename_(root, useMode=1)
    #
    path = '|' + rootName + '|'.join(('|'.join(objectPath.split(root)[1:])).split('|'))
    if ':' in path:
        namespace = _toNamespaceByNodePath(objectPath)
        path = path.replace(namespace + ':', none)
    #
    return path


#
def getObjectTransformation(nodepathString):
    lis = []
    channelLis = [
        '.translate', '.rotate', '.scale',
        '.rotatePivot', '.scalePivot'
    ]
    axisLis = ['X', 'Y', 'Z']
    for channel, axis in product(channelLis, axisLis):
        attrName = channel + axis
        attr = nodepathString + channel + axis
        if _isAppExist(attr):
            data = cmds.getAttr(attr)
            lis.append((attrName, data))
    #
    vsbAttrName = '.visibility'
    visibilityAttr = nodepathString + vsbAttrName
    visibilityData = cmds.getAttr(visibilityAttr)
    lis.append((vsbAttrName, visibilityData))
    return lis


#
def getChildrenTransAttrDicByRoot(root):
    def getBranch(objectPath):
        transAttrs = getObjectTransformation(objectPath)
        if transAttrs:
            localDirectory = getObjectLocalPath(root, objectPath)
            dic[localDirectory] = transAttrs
    #
    dic = collections.OrderedDict()
    rootPath = _dcc_getNodFullpathNodepathStr(root)
    objectPaths = getChildrenByRoot(rootPath)
    objectPaths.insert(0, rootPath)
    #
    if objectPaths:
        [getBranch(i) for i in objectPaths]
    #
    return dic


#
def setTransAttrByDic(dic):
    def setBranch(objectPath, attrData):
        attrName, data = attrData
        relativePath = objectPath[1:]
        #
        attr = relativePath + attrName
        #
        if _isAppExist(attr):

            cmds.setAttr(attr, data)
    if dic:
        [setBranch(k, i) for k, v in dic.items() for i in v]


#
def setObjectTransAttr(objectPath, transAttrData):
    if _isAppExist(objectPath):
        if transAttrData:
            for i in transAttrData:
                attrName, data = i
                attr = objectPath + attrName
                setAsbAttr(attr, data)


#
def setAsbAttr(attr, data):
    if _isAppExist(attr):
        if not cmds.getAttr(attr, lock=1):
            cmds.setAttr(attr, data)


#
def getNodeAttrData(node):
    attrData = collections.OrderedDict()
    nodeType = cmds.nodeType(node)
    #
    attrNames = cmds.listAttr(node, read=1, write=1, connectable=1, scalar=1)
    if attrNames:
        for attrName in attrNames:
            attrData[attrName] = cmds.getAttr(node + '.' + attrName)
    return node, nodeType, attrData


#
def isAttrSource(nodepathString, attrName=none):
    if attrName:
        attr = nodepathString + '.' + attrName
    else:
        attr = nodepathString
    return cmds.connectionInfo(attr, isSource=1)


#
def isAttrDestination(nodepathString, attrName=none):
    if attrName:
        attr = nodepathString + '.' + attrName
    else:
        attr = nodepathString
    return cmds.connectionInfo(attr, isDestination=1)


#
def isAttrExactDestination(nodepathString, attrName=none):
    if attrName:
        attr = nodepathString + '.' + attrName
    else:
        attr = nodepathString
    return cmds.connectionInfo(attr, isExactDestination=1)


#
def setNodeOutlinerRgb(nodepathString, r, g, b):
    cmds.setAttr(nodepathString + '.useOutlinerColor', 1)
    cmds.setAttr(nodepathString + '.outlinerColor', r, g, b)


#
def setCreateShaderWithAttrData(attrData):
    if attrData:
        nodeName, nodeType, attrData = attrData
        if not cmds.objExists(nodeName):
            cmds.shadingNode(nodeType, name=nodeName, asShader=1)
            for attrName, attrValue in attrData:
                cmds.setAttr(nodeName + '.' + attrName, attrValue)


# set Maya View
def setMayaView(modelPanel, mCamera):
    cmds.modelEditor(
        modelPanel,
        edit=1,
        activeView=1,
        useDefaultMaterial=0,
        wireframeOnShaded=0,
        dl='default',
        twoSidedLighting=0,
        allObjects=0,
        manipulators=1,
        grid=0,
        hud=1,
        sel=1
    )
    cmds.modelEditor(
        modelPanel,
        edit=1,
        activeView=1,
        polymeshes=1,
        subdivSurfaces=1,
        fluids=1,
        strokes=1,
        nCloths=1,
        nParticles=1,
        pluginObjects=['gpuCacheDisplayFilter', 1],
        displayAppearance='smoothShaded'
    )
    cameraShape = _dcc_getNodShapeNodepathStr(mCamera)
    cmds.camera(
        cameraShape,
        edit=1,
        displayFilmGate=0,
        displaySafeAction=0,
        displaySafeTitle=0,
        displayFieldChart=0,
        displayResolution=1,
        displayGateMask=1,
        filmFit=1,
        overscan=1
    )
    cmds.setAttr(cameraShape + '.displayGateMaskOpacity', 1)
    cmds.setAttr(cameraShape + '.displayGateMaskColor', 0, 0, 0, type='double3')
    #
    cmds.displayRGBColor('background', .25, .25, .25)
    cmds.displayRGBColor('backgroundTop', .25, .25, .25)
    cmds.displayRGBColor('backgroundBottom', .25, .25, .25)


# Set Camera View
def setCameraView(nodepathString):
    defaultPanel = 'modelPanel4'
    if cmds.panel(defaultPanel, exists=1):
        cmds.lookThru(nodepathString, defaultPanel)
        setMayaView(defaultPanel, nodepathString)


#
def setViewportShaderDisplayMode(panel):
    cmds.modelEditor(
        panel,
        edit=1,
        useDefaultMaterial=0,
        displayAppearance='smoothShaded',
        displayTextures=0,
        displayLights='default',
        shadows=0
    )


# Display Nde_ShaderRef
def setViewportTextureDisplayMode(panel):
    cmds.modelEditor(
        panel,
        edit=1,
        useDefaultMaterial=0,
        displayAppearance='smoothShaded',
        displayTextures=1,
        displayLights='default',
        shadows=0
    )


# Display Nde_ShaderRef
def setViewportLightDisplayMode(panel):
    cmds.modelEditor(
        panel,
        edit=1,
        useDefaultMaterial=0,
        displayAppearance='smoothShaded',
        displayTextures=1,
        displayLights='all',
        shadows=1
    )


# Set Display Mode [ Mode 5: Nde_ShaderRef(Non-Texture), Mode 6: Nde_ShaderRef ]
def setDisplayMode(displayMode):
    modelPanels = cmds.getPanel(typ='modelPanel')
    for currentPanel in modelPanels:
        if displayMode == 5:
            setViewportShaderDisplayMode(currentPanel)
        elif displayMode == 6:
            setViewportTextureDisplayMode(currentPanel)
        elif displayMode == 7:
            setViewportLightDisplayMode(currentPanel)


# set Object Color
def setNodeOverrideColor(nodepathString, color=17):
    cmds.setAttr(nodepathString + '.overrideEnabled', 1)
    cmds.setAttr(nodepathString + '.overrideColor', color)


#
def _toNodeAttr(stringLis):
    return appCfg.DEF_mya_node_port_pathsep.join(stringLis)


#
def _toNodePathString(stringLis):
    return appCfg.DEF_mya_node_pathsep.join(stringLis)


#
def _toNamespace(stringLis):
    return appCfg.DEF_mya_node_namespace_pathsep.join(stringLis)


#
def setNodeOverrideRgb(nodepathString, r, g, b):
    cmds.setAttr(_toNodeAttr([nodepathString, 'overrideRGBColors']), 1)
    cmds.setAttr(_toNodeAttr([nodepathString, 'overrideColorRGB']), r, g, b)
    cmds.setAttr(_toNodeAttr([nodepathString, 'overrideEnabled']), True)


#
def getModuleInfo():
    dic = collections.OrderedDict()
    moduleInfo = cmds.moduleInfo(listModules=1)
    for i in moduleInfo:
        dic[i] = dict(
            modulePath=cmds.moduleInfo(definition=1, moduleName=i),
            plugPath=cmds.moduleInfo(path=1, moduleName=i),
            version=cmds.moduleInfo(version=1, moduleName=i))
    return dic


# Set Render Size
def setRenderSize(width, height, dpi=72):
    cmds.setAttr('defaultResolution.width', width)
    cmds.setAttr('defaultResolution.height', height)
    cmds.setAttr('defaultResolution.dpi', dpi)
    # Debug ( deviceAspectRatio Attribute Error )
    # cmds.setAttr('defaultResolution.deviceAspectRatio', float(width / height))
    cmds.setAttr('defaultResolution.pixelAspect', 1)


#
def setVisiblePanelsDelete():
    panels = cmds.getPanel(visiblePanels=1)
    for panel in panels:
        if panel != 'modelPanel4':
            if cmds.panel(panel, query=1, exists=1):
                window = panel + 'Window'
                if cmds.window(window, query=1, exists=1):
                    cmds.deleteUI(window, window=1)


#
def setWindowDelete(windowName):
    if cmds.window(windowName, exists=1):
        cmds.deleteUI(windowName)


#
def setCreateEventScriptJob(windowName, scriptJobEvn, method):
    if method:
        if not cmds.window(windowName, exists=1):
            cmds.window(windowName, title='Script Job Window', sizeable=1, resizeToFitChildren=1)
        #
        if isinstance(method, list):
            for subMethod in method:
                cmds.scriptJob(parent=windowName, event=[scriptJobEvn, subMethod])
        else:
            cmds.scriptJob(parent=windowName, event=[scriptJobEvn, method])


#
def setCreateNodeDeleteScriptJob(windowName, node, method):
    if method:
        if not cmds.window(windowName, exists=1):
            cmds.window(windowName, title=bscMethods.StrCamelcase.toPrettify(windowName), sizeable=1, resizeToFitChildren=1)
        #
        if isinstance(method, list):
            for subMethod in method:
                cmds.scriptJob(parent=windowName, nodeDeleted=[node, subMethod])
        else:
            cmds.scriptJob(parent=windowName, nodeDeleted=[node, method])


#
def setCreateAttrChangedScriptJob(windowName, attr, method):
    if method:
        if not cmds.window(windowName, exists=1):
            cmds.window(windowName, title=bscMethods.StrCamelcase.toPrettify(windowName), sizeable=1, resizeToFitChildren=1)
        #
        if isinstance(method, list):
            for subMethod in method:
                cmds.scriptJob(parent=windowName, attributeChange=[attr, subMethod])
        else:
            cmds.scriptJob(parent=windowName, attributeChange=[attr, method])


#
def hideHandel(nodepathString):
    if cmds.toggle(nodepathString, query=1, selectHandle=1):
        cmds.toggle(nodepathString, selectHandle=1)
    if cmds.toggle(nodepathString, query=1, rotatePivot=1):
        cmds.toggle(nodepathString, rotatePivot=1)
    if cmds.toggle(nodepathString, query=1, scalePivot=1):
        cmds.toggle(nodepathString, scalePivot=1)


#
def displayHandle(nodepathString, boolean):
    if boolean:
        if not cmds.toggle(nodepathString, query=1, selectHandle=1):
            cmds.toggle(nodepathString, selectHandle=1)
        if not cmds.toggle(nodepathString, query=1, rotatePivot=1):
            cmds.toggle(nodepathString, rotatePivot=1)
        if not cmds.toggle(nodepathString, query=1, scalePivot=1):
            cmds.toggle(nodepathString, scalePivot=1)
    if not boolean:
        if cmds.toggle(nodepathString, query=1, selectHandle=1):
            cmds.toggle(nodepathString, selectHandle=1)
        if cmds.toggle(nodepathString, query=1, rotatePivot=1):
            cmds.toggle(nodepathString, rotatePivot=1)
        if cmds.toggle(nodepathString, query=1, scalePivot=1):
            cmds.toggle(nodepathString, scalePivot=1)


#
def setObjectDisplayHandleEnable(nodepathString, boolean):
    attr = nodepathString + '.' + 'displayHandle'
    cmds.setAttr(attr, boolean)


#
def setObjectParent(childPath, parentPath):
    if _isAppExist(parentPath) and _isAppExist(childPath):
        origParentPath = getObjectParent(childPath)
        if origParentPath:
            if parentPath.startswith(appCfg.DEF_mya_node_pathsep):
                if not parentPath == origParentPath:
                    cmds.parent(childPath, parentPath)
            else:
                if not parentPath in origParentPath:
                    cmds.parent(childPath, parentPath)
        else:
            cmds.parent(childPath, parentPath)


#
def setShapeParent(sourceObject, targetObject):
    if _isAppExist(sourceObject) and _isAppExist(targetObject):
        sourceShape = _dcc_getNodShapeNodepathStr(sourceObject)
        origParentPath = getObjectParent(sourceObject)
        if origParentPath:
            if not targetObject in origParentPath:
                cmds.parent(sourceShape, targetObject, shape=1, add=1)
        else:
            cmds.parent(sourceShape, targetObject, shape=1, add=1)


#
def setElementSet(element, mSet):
    if not _isAppExist(mSet):
        cmds.sets(name=mSet)
    cmds.sets(element, forceElement=mSet, edit=1)


#
def setParentGroup(child, parent, groupName='null'):
    if cmds.objExists(parent) and cmds.objExists(child):
        cmds.group(child, name=groupName, parent=parent)


# Reorder Object ( dir = 1 / -1 )
def setObjectReorder(nodepathString, rowIndex):
    cmds.reorder(nodepathString, relative=rowIndex)


#
def setObjectReferenceDisplay(nodepathString):
    if _isAppExist(nodepathString):
        cmds.setAttr(nodepathString + '.overrideEnabled', 1)
        cmds.setAttr(nodepathString + '.overrideDisplayType', 2)


#
def setCleanChild(nodepathString):
    allChild = cmds.listRelatives(nodepathString, children=1, fullPath=True)
    shape = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=1, fullPath=True)
    if allChild:
        for i in allChild:
            if i not in shape:
                cmds.delete(i)


# Parent To World
def setParentToWorld(nodepathString):
    if cmds.listRelatives(nodepathString, parent=1):
        cmds.parent(nodepathString, world=1)


#
def setNodeRename(nodepathString, newName):
    if newName != nodepathString:
        if not isNodeLocked(nodepathString):
            cmds.rename(nodepathString, newName)


#
def setObjectShapeRename(nodepathString, name):
    shape = _dcc_getNodShapeNodepathStr(nodepathString, fullPath=True)
    shapeName = _nodeString2nodename_(shape)
    if shape:
        if name != shapeName:
            if not isNodeLocked(shape):
                cmds.rename(shape, name)


#
def setObjectRename(objectPath, name):
    objectName = _nodeString2nodename_(objectPath)
    if not name == objectName:
        if not isNodeLocked(objectPath):
            cmds.rename(objectPath, name)


#
def setRenameForce(nodepathString, name):
    if name != nodepathString:
        if _isAppExist(nodepathString):
            if _isAppExist(name):
                name += '_reduce'
            setNodeUnlock(nodepathString)
            cmds.rename(nodepathString, name)
            setNodeLock(name)


#
def isPolyMesh(nodepathString):
    if cmds.nodeType(nodepathString) == appCfg.DEF_mya_type_transform:
        shape = _dcc_getNodShapeNodepathStr(nodepathString)
        if cmds.nodeType(shape) == 'mesh':
            return True
        else:
            return False
    else:
        return False


#
def _getNodeIsShape(nodepathString):
    boolean = False
    if cmds.nodeType(nodepathString) != appCfg.DEF_mya_type_transform:
        shapes = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=1, fullPath=True)
        if not shapes:
            boolean = True
    return boolean


#
def _getNodeIsTransform(nodepathString):
    boolean = False
    if cmds.nodeType(nodepathString) == appCfg.DEF_mya_type_transform:
        shapes = _getNodeShapeNodeStringList(nodepathString)
        if shapes:
            boolean = True
    return boolean


#
def _getNodeIsGroup(nodepathString):
    boolean = False
    if cmds.nodeType(nodepathString) == appCfg.DEF_mya_type_transform:
        shapes = _getNodeShapeNodeStringList(nodepathString)
        if not shapes:
            boolean = True
    return boolean


# Check Object is Empty Group
def isGroupEmpty(nodepathString):
    if cmds.nodeType(nodepathString) == appCfg.DEF_mya_type_transform:
        child = cmds.listRelatives(nodepathString, children=1)
        if not child:
            return True


#
def isChild(parent, child):
    boolean = False
    if _isAppExist(child):
        checkData = _dcc_getNodFullpathNodepathStr(child)
        if checkData:
            if parent in checkData:
                boolean = True
    return boolean


#
def getSelectedObjects(fullPath=True, useShape=0):
    lis = []
    data = cmds.ls(selection=1, long=fullPath)
    if data:
        if useShape:
            lis = [_dcc_getNodShapeNodepathStr(i, fullPath) for i in data]
        else:
            lis = data
    return lis


#
def setSelObject(nodepathString, add=False):
    if _isAppExist(nodepathString):
        cmds.select(nodepathString, add=add)


#
def setNodeSelect(nodepathStringLis, noExpand=0):
    existsObjects = [i for i in nodepathStringLis if _isAppExist(i)]
    cmds.select(existsObjects, noExpand=noExpand)


#
def setSelClear():
    cmds.select(clear=1)


#
def getObjectExistsFilter(objectPaths):
    return [i for i in objectPaths if _isAppExist(i)]


#
def setUpdateSel(objectLis):
    selObjects = getSelectedNodeLis()
    #
    existsObjects = getObjectExistsFilter(objectLis)
    #
    for i in existsObjects:
        if i not in selObjects:
            cmds.select(i, add=1)
    #
    for i in selObjects:
        if i not in existsObjects:
            cmds.select(i, deselect=1)


#
def _getNodeCategoryString(nodepathString):
    return cmds.nodeType(nodepathString)


#
def getNodeTypes():
    return cmds.allNodeTypes()


#
def getAttrTypes():
    attrTypes = []
    nodeTypes = getNodeTypes()
    for nodeType in nodeTypes:
        attrNames = cmds.attributeInfo(type=nodeType, all=1)
        for attrName in attrNames:
            attType = cmds.attributeQuery(attrName, typ=nodeType, attributeType=1)
            if not attType in attrTypes:
                attrTypes.append(str(attType))
    return attrTypes


#
def getTransformType(nodepathString):
    if _getNodeCategoryString(nodepathString) == appCfg.DEF_mya_type_transform:
        shape = _dcc_getNodShapeNodepathStr(nodepathString, 1)
        if shape:
            return _getNodeCategoryString(shape)


#
def _getNodeShapeCategoryString(nodepathString):
    nodeType = _getNodeCategoryString(nodepathString)
    #
    if nodeType == appCfg.DEF_mya_type_transform:
        shapePath = _dcc_getNodShapeNodepathStr(nodepathString)
        if shapePath:
            string = _getNodeCategoryString(shapePath)
        else:
            string = nodeType
    else:
        string = nodeType
    #
    return string


#
def getNodeTransforms(mType, fullPath=True, keyword=none):
    def getBranch(nodeType):
        if nodeType in getNodeTypes():
            data = cmds.ls(type=mType, long=fullPath)
            if data:
                for n in data:
                    transform = _dcc_getNodTransformNodepathStr(n)
                    if transform:
                        if keyword in transform and not transform in lis:
                            lis.append(transform)
                    if not transform:
                        lis.append(n)
    #
    lis = []
    if isinstance(mType, str) or isinstance(mType, unicode):
        getBranch(mType)
    #
    if isinstance(mType, list):
        [getBranch(t) for t in mType]
    #
    return lis


#
def getNodeLisByType(mTypes, fullPath=True, keyword=none):
    def getUsed(nodeTypes):
        usableAttrs = getNodeTypes()
        if nodeTypes:
            return [i for i in nodeTypes if i in usableAttrs]
    #
    def getBranch(nodeTypes):
        data = cmds.ls(type=nodeTypes, long=fullPath)
        if data:
            [lis.append(n) for n in data if keyword in n and not n in lis]
    #
    lis = []
    # to List
    mTypes = bscMethods.String.toList(mTypes)
    # to Used List
    mTypes = getUsed(mTypes)
    # type Arg != []
    if mTypes:
        getBranch(mTypes)
    #
    return lis


#
def getNodesByNamespace(filterType, filterNamespace, fullPath=True):
    lis = []
    #
    filterNamespace = bscMethods.String.toList(filterNamespace)
    nodes = getNodeLisByType(filterType, fullPath)
    if filterNamespace and nodes:
        for namespace in filterNamespace:
            namespace += ':'
            [lis.append(n) for n in nodes if n.startswith(namespace) and not n in lis]
    #
    return lis


def getNodeLisByFilter(filterType, filterNamespace=None, fullPath=True):
    if filterNamespace:
        return getNodesByNamespace(filterType, filterNamespace, fullPath)
    else:
        return getNodeLisByType(filterType, fullPath)


#
def getSets():
    exceptSets = ['defaultLightSet', 'defaultObjectSet', 'initialParticleSE', 'initialShadingGroup']
    lis = [i for i in cmds.ls(sets=1) if i not in exceptSets and not isReferenceNode(i) and not _getNodeCategoryString(i) == 'animLayer']
    return lis


#
def getNodeLisBySet(mSet):
    lis = []
    data = cmds.sets(mSet, query=1)
    if data:
        lis = data
    return lis


#
def getUnusedSets():
    lis = [i for i in getSets() if not getNodeLisBySet(i)]
    return lis


#
def getDeforms():
    lis = [i for i in cmds.ls(type='geometryFilter') if not isReferenceNode(i)]
    return lis


#
def getNodesInDeform(deform):
    lis = []
    sets = cmds.listConnections(deform + '.message', type='objectSet')
    if sets:
        mSet = sets[0]
        lis = getNodeLisBySet(mSet)
    return lis


#
def getUnusedDeforms():
    lis = [i for i in getDeforms() if not getNodesInDeform(i)]
    return lis


#
def getShapeDeforms():
    lis = [i for i in cmds.ls(type='controlPoint', intermediateObjects=1) if not isReferenceNode(i)]
    return lis


#
def getUnusedShapeDeforms():
    lis = [i for i in getShapeDeforms() if not _getNodeTargetNodeStringList(i)]
    return lis


#
def getDisplayLayers():
    exceptLayers = ['defaultLayer']
    lis = [i for i in cmds.ls(type='displayLayer') if i not in exceptLayers and not isReferenceNode(i)]
    return lis


#
def setCreateDisplayLayer(layerName):
    cmds.createDisplayLayer(name=layerName, number=1, empty=1)


#
def setDisplayLayerVisible(displayLayer, boolean):
    cmds.setAttr(displayLayer + '.visibility', boolean)


# set Object Color
def setDisplayLayerColor(nodepathString, color=(1, 1, 1)):
    cmds.setAttr(nodepathString + '.enabled', 1)
    cmds.setAttr(nodepathString + '.color', 1)
    cmds.setAttr(nodepathString + '.overrideColorRGB', *color)
    cmds.setAttr(nodepathString + '.overrideRGBColors', 1)


#
def setAddObjectToDisplayLayer(displayLayer, objects):
    cmds.editDisplayLayerMembers(displayLayer, *objects, noRecurse=1)


#
def getNodesByDisplayLayer(layer):
    return cmds.editDisplayLayerMembers(layer, query=1)


#
def getUnusedDisplayLayers():
    lis = [i for i in getDisplayLayers() if not getNodesByDisplayLayer(i)]
    return lis


#
def getRenderLayers():
    exceptLayers = ['defaultRenderLayer']
    lis = [i for i in cmds.ls(type='renderLayer') if i not in exceptLayers and not isReferenceNode(i)]
    return lis


#
def getNodesByRenderLayer(layer):
    return cmds.editRenderLayerMembers(layer, query=1)


#
def getUnusedRenderLayers():
    lis = [i for i in getRenderLayers() if not getNodesByRenderLayer(i)]
    return lis


#
def getYetiShapeLis():
    yetiNodes = getNodeLisByType('pgYetiMaya', fullPath=True)
    return yetiNodes


#
def getYetiObjects():
    yetiObjects = [_dcc_getNodTransformNodepathStr(i, 1) for i in getNodeLisByType('pgYetiMaya', fullPath=True)]
    return yetiObjects


#
def isNamingOverlapping(node):
    data = cmds.ls(node, long=1)
    if len(data) > 1:
        return True


#
def getKeyableAttr(nodepathString):
    return cmds.listAttr(nodepathString, keyable=1)


#
def getAnimCurve(nodepathString, attrName):
    # List [ <Input Connection Nde_Node> ]
    attr = nodepathString + '.' + attrName
    inputNodes = cmds.listConnections(attr, destination=0, source=1)
    if inputNodes:
        inputNode = inputNodes[0]
        if _getNodeCategoryString(inputNode).startswith('animCurve'):
            return inputNode


#
def getObjectFilter(mType, fullPath=True, keyword=none):
    shapes = []
    if mType in getNodeTypes():
        data = cmds.ls(type=mType, dag=1, leaf=1, noIntermediate=1, long=fullPath)
        shapes = [i for i in data if keyword in i]
    return shapes


#
def getObjectTransformsByType(mType, fullPath=True, keyword=none):
    transforms = []
    if mType in getNodeTypes():
        data = cmds.ls(type=mType, dag=1, leaf=1, noIntermediate=1, long=fullPath)
        transforms = [_dcc_getNodTransformNodepathStr(i, 1) for i in data if keyword in i]
    return transforms


# Debug ( Use All Nodes Data for Rebuild )
def getYetiImportConnectionDic():
    dic = collections.OrderedDict()
    yetiObjects = getYetiObjects()
    for yetiObject in yetiObjects:
        yetiNode = _dcc_getNodShapeNodepathStr(yetiObject)
        importNodes = cmds.pgYetiGraph(yetiNode, listNodes=1, type='import')
        for node in importNodes:
            geometryData = cmds.pgYetiGraph(yetiNode, node=node, param='geometry', getParamValue=1)
            if cmds.pgYetiGraph(yetiNode, node=node, param='type', getParamValue=1) == 2:
                dic.setdefault(geometryData, []).append((yetiNode, node))
            else:
                dic.setdefault(_dcc_getNodTransformNodepathStr(geometryData, 1), []).append((yetiNode, node))
    return dic


# Repair Yeti Object Lost Connect Grow
def setRepairYetiGrows():
    yetiObjects = getYetiObjects()
    if yetiObjects:
        for yetiObject in yetiObjects:
            yetiNode = _dcc_getNodShapeNodepathStr(yetiObject)
            growMeshes = _getNodeSourceNodeStringList(yetiNode, 'mesh')
            if growMeshes:
                growMesh = growMeshes[0]
                meshShape = _dcc_getNodShapeNodepathStr(growMesh)
                #
                importNodes = cmds.pgYetiGraph(yetiNode, listNodes=1, type='import')
                for node in importNodes:
                    inputGeometry = cmds.pgYetiGraph(yetiNode, node=node, param='geometry', getParamValue=1)
                    if cmds.pgYetiGraph(yetiNode, node=node, param='type', getParamValue=1) == 0:
                        if inputGeometry == '*':
                            setYetiNodeAttr(yetiNode, node, 'geometry', meshShape)
                        if inputGeometry != meshShape:
                            setYetiNodeAttr(yetiNode, node, 'geometry', meshShape)


#
def getYetiGroomDic(yetiObject):
    dic = collections.OrderedDict()
    yetiNode = _dcc_getNodShapeNodepathStr(yetiObject)
    importNodes = cmds.pgYetiGraph(yetiNode, listNodes=1, type='import')
    if importNodes:
        for node in importNodes:
            geometryData = cmds.pgYetiGraph(yetiNode, node=node, param='geometry', getParamValue=1)
            if cmds.pgYetiGraph(yetiNode, node=node, param='type', getParamValue=1) == 1:
                if _isAppExist(geometryData):
                    dic[_dcc_getNodTransformNodepathStr(geometryData, 1)] = node
                if not _isAppExist(geometryData):
                    dic['%s ( Groom - Error )' % node] = node
    return dic


#
def getYetiGrowDic(yetiObject):
    dic = collections.OrderedDict()
    yetiNode = _dcc_getNodShapeNodepathStr(yetiObject)
    importNodes = cmds.pgYetiGraph(yetiNode, listNodes=1, type='import')
    if importNodes:
        for node in importNodes:
            geometryData = cmds.pgYetiGraph(yetiNode, node=node, param='geometry', getParamValue=1)
            if cmds.pgYetiGraph(yetiNode, node=node, param='type', getParamValue=1) == 0:
                if _isAppExist(geometryData):
                    if geometryData == '*':
                        dic['%s ( Grow - Error )' % node] = node
                    if geometryData != '*':
                        dic[_dcc_getNodTransformNodepathStr(geometryData, 1)] = node
                if not _isAppExist(geometryData):
                    dic['%s ( Grow - Error )' % node] = node
    return dic


#
def getErrorYetiObject(yetiObject):
    pass


#
def getYetiMapDic(yetiObject):
    dic = collections.OrderedDict()
    yetiNode = _dcc_getNodShapeNodepathStr(yetiObject)
    mapNodes = cmds.pgYetiGraph(yetiNode, listNodes=1, type='texture')
    if mapNodes:
        for mapNode in mapNodes:
            string = cmds.pgYetiGraph(yetiNode, node=mapNode, param='file_name', getParamValue=1)
            if isOsTextureExists(string):
                dic[string] = mapNode
            else:
                dic['%s ( Map - Error )' % mapNode] = mapNode
    return dic


#
def getYetiGuideSetDic(yetiObject):
    dic = collections.OrderedDict()
    yetiNode = _dcc_getNodShapeNodepathStr(yetiObject)
    importNodes = cmds.pgYetiGraph(yetiNode, listNodes=1, type='import')
    if importNodes:
        for node in importNodes:
            geometryData = cmds.pgYetiGraph(yetiNode, node=node, param='geometry', getParamValue=1)
            if cmds.pgYetiGraph(yetiNode, node=node, param='type', getParamValue=1) == 2:
                if _isAppExist(geometryData):
                    dic[geometryData] = node
                if not _isAppExist(geometryData):
                    dic['%s ( Guide - Error )' % node] = node
    return dic


#
def getYetiGuideData(yetiObject):
    dic = collections.OrderedDict()
    yetiNode = _dcc_getNodShapeNodepathStr(yetiObject)
    guideSets = getInputObjectsByAttrName(yetiNode, '.guideSets')
    if guideSets:
        for guideSet in guideSets:
            subDic = collections.OrderedDict()
            if _isAppExist(guideSet):
                curves = getInputObjectsByAttrName(guideSet, '.dagSetMembers')
                for curve in curves:
                    if _isAppExist(curve):
                        curveLongName = _dcc_getNodFullpathNodepathStr(curve)
                        curveShape = _dcc_getNodShapeNodepathStr(curveLongName, 1)
                        follicles = getInputObjectsByAttrName(curveShape, '.create')
                        if follicles:
                            follicle = follicles[0]
                            subDic.setdefault(curveLongName, []).append(_dcc_getNodTransformNodepathStr(follicle, 1))
                            #
                            follicleShape = _dcc_getNodShapeNodepathStr(follicle, 1)
                            localCurves = getInputObjectsByAttrName(follicleShape, '.startPosition')
                            localCurvesReduce = getReduceList(localCurves)
                            localCurve = none
                            if localCurvesReduce:
                                localCurve = localCurvesReduce[0]
                            subDic.setdefault(curveLongName, []).append(_dcc_getNodTransformNodepathStr(localCurve, 1))
                            #
                            hairSystems = getInputObjectsByAttrName(follicleShape, '.currentPosition')
                            hairSystemsReduce = getReduceList(hairSystems)
                            hairSystem = none
                            if hairSystemsReduce:
                                hairSystem = hairSystems[0]
                            subDic.setdefault(curveLongName, []).append(_dcc_getNodTransformNodepathStr(hairSystem, 1))
                            #
                            hairSystemShape = _dcc_getNodShapeNodepathStr(hairSystem, 1)
                            nuclei = getInputObjectsByAttrName(hairSystemShape, '.startFrame')
                            nucleiReduce = getReduceList(nuclei)
                            nucleus = none
                            if nucleiReduce:
                                nucleus = nuclei[0]
                            subDic.setdefault(curveLongName, []).append(_dcc_getNodFullpathNodepathStr(nucleus))
                dic[guideSet] = subDic
    return dic


#
def getYetiGuideHairSystems(yetiObject):
    lis = []
    yetiNode = _dcc_getNodShapeNodepathStr(yetiObject)
    guideSets = getInputObjectsByAttrName(yetiNode, '.guideSets')
    if guideSets:
        for guideSet in guideSets:
            if _isAppExist(guideSet):
                curves = getInputObjectsByAttrName(guideSet, '.dagSetMembers')
                for curve in curves:
                    if _isAppExist(curve):
                        curvePath = _dcc_getNodFullpathNodepathStr(curve)
                        curveShape = _dcc_getNodShapeNodepathStr(curvePath, 1)
                        follicles = getInputObjectsByAttrName(curveShape, '.create')
                        if follicles:
                            follicle = follicles[0]
                            follicleShape = _dcc_getNodShapeNodepathStr(follicle, 1)
                            #
                            hairSystems = getInputObjectsByAttrName(follicleShape, '.currentPosition')
                            for hairSystem in hairSystems:
                                if not hairSystem in lis:
                                    lis.append(hairSystem)
    return lis


#
def getYetiGuideSets(yetiObject):
    lis = []
    yetiShapeString = _dcc_getNodShapeNodepathStr(yetiObject)
    guideSets = getInputObjectsByAttrName(yetiShapeString, '.guideSets')
    if guideSets:
        for guideSet in guideSets:
            if _isAppExist(guideSet):
                lis.append(guideSet)
    return lis


#
def setYetiNodeAttr(yetiShapeString, node, attr, inputNode):
    cmds.pgYetiGraph(yetiShapeString, node=node, param=attr, setParamValueString=inputNode)


#
def setYetiTextureParam(yetiShapeString, node, mapFile):
    cmds.pgYetiGraph(yetiShapeString, node=node, param='file_name', setParamValueString=mapFile)


#
def getYetiRefObject(nodepathString):
    lis = []
    shape = _dcc_getNodShapeNodepathStr(nodepathString)
    referenceObjects = getInputObjectsByAttrName(shape, '.referenceObject')
    if referenceObjects:
        [lis.append(_dcc_getNodFullpathNodepathStr(i)) for i in referenceObjects]
    return lis


#
def getPfxHairObjects():
    lis = [_dcc_getNodTransformNodepathStr(i, 1) for i in getNodeLisByType('pfxHair', fullPath=True) if _getNodeSourceNodeStringList(i, 'hairSystem')]
    return lis


#
def getPfxHairBrushes(pfxHairObject):
    pfxHairNode = _dcc_getNodShapeNodepathStr(pfxHairObject, 1)
    brushes = getInputObjectsByAttrName(pfxHairNode, '.brush')
    return brushes


#
def getPfxHairSystemObjects(pfxHairObject):
    pfxHairNode = _dcc_getNodShapeNodepathStr(pfxHairObject, 1)
    systemObjects = getInputObjectsByAttrName(pfxHairNode, '.renderHairs')
    return getReduceList(systemObjects)


#
def getPfxHairOutputCurves(follicleObject):
    outputCurveObjects = []
    follicleShape = _dcc_getNodShapeNodepathStr(follicleObject, 1)
    guessObjects = getOutputNodeLisFilter(follicleShape, '.outCurve')
    if guessObjects:
        for nodepathString in guessObjects:
            if _getNodeCategoryString(nodepathString) == 'rebuildCurve':
                outputObjects = getOutputNodeLisFilter(nodepathString, '.outputCurve')
                outputCurveObjects.extend(outputObjects)
            if getTransformType(nodepathString) == 'nurbsCurve':
                outputCurveObjects.append(nodepathString)
    return outputCurveObjects


#
def getPfxHairShaders(pfxHairObject):
    shaders = []
    systemObjects = getPfxHairSystemObjects(pfxHairObject)
    if systemObjects:
        for systemObject in systemObjects:
            systemShape = _dcc_getNodShapeNodepathStr(systemObject, 1)
            inputNodes = getInputObjectsByAttrName(systemShape, '.aiHairShader')
            shaders.extend(inputNodes)
    return getReduceList(shaders)


#
def getPfxHairTextures(pfxHairObject):
    textureNodes = []
    shaders = getPfxHairShaders(pfxHairObject)
    if shaders:
        for shader in shaders:
            inputNodes = _getNodeSourceNodeStringList(shader, 'file')
            subInputNodes = _getNodeSourceNodeStringList(shader, 'aiImage')
            textureNodes.extend(inputNodes)
            textureNodes.extend(subInputNodes)
    return textureNodes


#
def getPfxHairMapNodes(pfxHairObject):
    maps = []
    systemObjects = getPfxHairSystemObjects(pfxHairObject)
    if systemObjects:
        for systemObject in systemObjects:
            systemShape = _dcc_getNodShapeNodepathStr(systemObject, 1)
            inputNodes = getInputObjectsByAttrName(systemShape, '.baldnessMap')
            maps.extend(inputNodes)
    return getReduceList(maps)


#
def getPfxHairConnectionData(pfxHairObject):
    growObjects = []
    systemObjects = getPfxHairSystemObjects(pfxHairObject)
    nucleusObjects = []
    follicleData = collections.OrderedDict()
    if systemObjects:
        for systemObject in systemObjects:
            systemShape = _dcc_getNodShapeNodepathStr(systemObject, 1)
            nucleusObjects = getInputObjectsByAttrName(systemShape, '.startFrame')
            follicleObjects = getInputObjectsByAttrName(systemShape, '.inputHair')
            for follicleObject in follicleObjects:
                follicleShape = _dcc_getNodShapeNodepathStr(follicleObject, 1)
                localCurveObjects = getInputObjectsByAttrName(follicleShape, '.startPosition')
                outputCurveObjects = getPfxHairOutputCurves(follicleObject)
                follicleData[follicleObject] = getReduceList(localCurveObjects), getReduceList(outputCurveObjects)
                # Grow Object
                existsGrowObjects = getInputObjectsByAttrName(follicleShape, '.inputMesh')
                growObjects.extend(existsGrowObjects)
    shaders = getPfxHairShaders(pfxHairObject)
    textures = getPfxHairTextures(pfxHairObject)
    maps = getPfxHairMapNodes(pfxHairObject)
    return getReduceList(growObjects), shaders, textures, maps, getReduceList(systemObjects), getReduceList(nucleusObjects), follicleData


#
def setRepairShape(nodepathString, useMode=0):
    shapes = _getNodeShapeNodeStringList(nodepathString, 1)
    mainShapes = getMainShapes(nodepathString, 1)
    if not mainShapes:
        if useMode == 0:
            if shapes:
                mainShape = shapes[0]
                cmds.setAttr(mainShape + '.intermediateObject', 0)
        if useMode == 1:
            cmds.delete(nodepathString)


#
def isIntermediateShape(shape):
    boolean = cmds.getAttr(shape + '.intermediateObject')
    return boolean


#
def setShapeIntermediate(shape, boolean):
    cmds.setAttr(shape + '.intermediateObject', boolean)


#
def setCleanHistory(nodes):
    cmds.delete(nodes, constructionHistory=1)


# Assign Default Nde_ShaderRef
def setObjectDefaultShaderCmd(objectLis):
    # [cmds.sets(nodepathString, forceElement='initialShadingGroup') for nodepathString in objectLis]
    [setNodeDefaultShader(nodepathString) for nodepathString in objectLis]


#
def getObjectLinkShader():
    pass


# Assign Default Nde_ShaderRef
def setNodeDefaultShader(nodepathString):
    # cmds.sets(nodepathString, forceElement='initialShadingGroup')
    cmds.sets(_dcc_getNodShapeNodepathStr(nodepathString, 1), forceElement='initialShadingGroup')


#
def setObjectCleanShaders(nodepathString):
    shadingEngines = _getNodeTargetNodeStringList(nodepathString, 'shadingEngine')
    if shadingEngines:
        [cmds.sets(nodepathString, remove=i) for i in shadingEngines]


# Set Attr
def setHide(nodepathString):
    attr = nodepathString + '.' + 'visibility'
    if cmds.objExists(attr):
        cmds.setAttr(attr, 0)


# Set Attr
def setShow(nodepathString):
    attr = nodepathString + '.' + 'visibility'
    if cmds.objExists(attr):
        cmds.setAttr(attr, 1)


# Set Attr
def isHide(nodepathString):
    attr = nodepathString + '.' + 'visibility'
    return cmds.getAttr(attr)


def isLxNodeVisible(nodepathString):
    attr = nodepathString + 'lxVisible'
    if _isAppExist(attr):
        return cmds.getAttr(attr)
    else:
        return True


#
def setLocatorCreate(nodepathString):
    return cmds.spaceLocator(name=nodepathString, position=(0, 0, 0))


#
def setNodeVisible(nodepathString, boolean):
    attr = nodepathString + '.' + 'visibility'
    cmds.setAttr(attr, boolean)


#
def isNodeVisible(nodepathString):
    attr = nodepathString + '.' + 'visibility'
    return cmds.getAttr(attr)


#
def getObjectHierarchyDic(mType, root):
    # Dict { <Parent> :
    #       List [ <Child> ] }
    dic = collections.OrderedDict()
    lis = []
    if root:
        hierarchyData = getObjectTransformsByType(mType, 1, root)
        for data in hierarchyData:
            splitData = data.split(appCfg.DEF_mya_node_pathsep)
            # Check Naming Error( Overlapping Name )
            if len(splitData) == len(set(splitData)):
                for seq, i in enumerate(splitData):
                    if seq > 1:
                        subDic = collections.OrderedDict()
                        k = splitData[seq - 1]
                        v = splitData[seq]
                        subDic[k] = v
                        lis.append(subDic)
            else:
                [splitData.remove(i) for i in getReduceList(splitData)]
                cmds.error('Naming Error:  %s (Overlapping Name: %s)' % (data, splitData))
    if lis:
        [dic.setdefault(ik, []).append(iv) for i in getReduceList(lis) for ik, iv in i.items()]
    return dic


#
def setCopyNode(nodepathString, newObject):
    cmds.duplicate(nodepathString, name=newObject, returnRootsOnly=1)


#
def setReferenceNamespace(referenceNode, namespace):
    if namespace:
        if not cmds.namespace(exists=namespace):
            fileName = cmds.referenceQuery(referenceNode, filename=1)
            cmds.file(fileName, namespace=namespace, edit=1)


#
def setNamespaceRename(namespace, newNamespace, parent=':'):
    if cmds.namespace(exists=namespace) and not cmds.namespace(exists=newNamespace) and cmds.namespace(exists=parent):
        cmds.namespace(rename=[namespace, newNamespace], parent=parent)


#
def setCreateContainer(nodeName):
    if not _isAppExist(nodeName):
        cmds.container(type='dagContainer', name=nodeName)
        cmds.setAttr(nodeName + '.blackBox', 1)
        cmds.setAttr(nodeName + '.iconName', 'toolSettings.png', type='string')


#
def getContainerNodes(container):
    return cmds.container(container, query=1, nodeList=1)


# Set Nde_Node in Container
def setInContainer(container, nodes):
    if not _isAppExist(container):
        cmds.container(type='dagContainer', name=container)
        cmds.setAttr(container + '.blackBox', 1)
        cmds.setAttr(container + '.iconName', 'toolSettings.png', type='string')
        #
        cmds.container(container, edit=1, force=1, addNode=nodes)


#
def setOutContainer(container, nodes):
    cmds.container(container, edit=1, force=1, removeNode=nodes)


#
def setRemoveContainer(container):
    cmds.container(container, edit=1, force=1)


#
def setContainerAddNodes(container, nodes):
    if _isAppExist(container):
        cmds.container(container, edit=1, force=1, addNode=nodes)


#
def setContainerNamespace(container, namespace):
    if _isAppExist(container):
        nodes = getContainerNodes(container)
        if nodes:
            for node in nodes:
                setNodeRename(node, namespace + ':' + node)
        setNodeRename(container, namespace + ':' + container)


#
def getReferenceNodeLis():
    errorNodes = ['_UNKNOWN_REF_NODE_']
    lis = [i for i in getNodeLisByType('reference') if not i.startswith('sharedReferenceNode') if i not in errorNodes]
    return lis


#
def getReferenceNodeFilterByNamespace(filterNamespace):
    lis = []
    #
    nodes = getReferenceNodeLis()
    filterNamespace = bscMethods.String.toList(filterNamespace)
    if nodes and filterNamespace:
        for node in nodes:
            namespace = getReferenceNamespace(node)
            if namespace in filterNamespace:
                lis.append(node)
    return lis


#
def getNodesByReferenceNode(referenceNode):
    nodes = cmds.referenceQuery(referenceNode, nodes=1)
    return nodes


#
def getReferenceFile(referenceNode, useMode=0):
    string = none
    fileData = cmds.referenceQuery(referenceNode, filename=1)
    if fileData:
        if useMode == 0:
            string = fileData
        elif useMode == 1:
            if fileData.endswith('}'):
                string = fileData.split('{')[0]
            else:
                string = fileData
    return string


#
def setCleanReferences():
    referenceNodes = getReferenceNodeLis()
    if referenceNodes:
        for referenceNode in referenceNodes:
            setReferenceRemove(referenceNode)


#
def getReferenceNumber(referenceNode):
    number = 0
    fileData = cmds.referenceQuery(referenceNode, filename=1)
    if fileData.endswith('}'):
        number = int(fileData.split('{')[-1][:-1])
    return number


#
def getReferenceNamespace(referenceNode):
    namespace = none
    try:
        guessData = cmds.referenceQuery(referenceNode, namespace=1)[1:]
        if guessData:
            namespace = guessData
    except Exception, e:
        print str(e)
    return namespace


#
def setNamespaceRemove(namespace):
    if cmds.namespace(exists=namespace):
        cmds.namespace(removeNamespace=namespace, mergeNamespaceWithRoot=1)


#
def getNamespaces():
    cmds.namespace(setNamespace=':')
    namespaceData = cmds.namespaceInfo(listOnlyNamespaces=1, recurse=1)
    return namespaceData


#
def getReferenceNamespaceDic():
    dic = collections.OrderedDict()
    referenceNodes = cmds.ls(type='reference')
    for referenceNode in referenceNodes:
        namespace = getReferenceNamespace(referenceNode)
        if namespace:
            dic[namespace] = referenceNode
    return dic


#
def setCurrentNamespace(namespace):
    cmds.namespace(setNamespace=namespace)


#
def getDependNodesByNamespace(namespace):
    nodes = []
    if isNamespaceExists(namespace):
        nodes = cmds.namespaceInfo(namespace, listOnlyDependencyNodes=1, dagPath=1)
    return nodes


#
def getNodesFilterByTypes(nodes, filterTypes):
    lis = []
    if nodes:
        for i in nodes:
            if _isAppExist(i):
                nodeType = _getNodeCategoryString(i)
                if nodeType in filterTypes:
                    lis.append(i)
    return lis


#
def isNamespaceExists(namespace):
    return cmds.namespace(exists=namespace)


#
def setAddNamespace(namespace):
    if namespace:
        if not cmds.namespace(exists=namespace):
            cmds.namespace(add=namespace)


#
def getNamespaceLis():
    lis = []
    exceptNamespace = ['UI', 'shared']
    namespaceData = cmds.namespaceInfo(recurse=1, listOnlyNamespaces=1)
    if namespaceData:
        namespaceData.reverse()
        for subNamespaceData in namespaceData:
            if not subNamespaceData in exceptNamespace:
                isAssemble = False
                nodes = cmds.namespaceInfo(subNamespaceData, listOnlyDependencyNodes=1, dagPath=1)
                if nodes:
                    for node in nodes:
                        parent = getObjectParent(node, 1)
                        if _getNodeCategoryString(parent) == 'assemblyReference':
                            isAssemble = True
                            break
                #
                if not isAssemble:
                    lis.append(subNamespaceData)
    return lis


#
def getSelectedNodeLis(fullPath=True):
    return cmds.ls(selection=1, long=fullPath)


#
def getSelObjParentFilter(keyword, fullPath=True):
    lis = []
    objectLis = cmds.ls(selection=1, long=fullPath)
    if objectLis:
        for nodepathString in objectLis:
            parent = getObjectParentFilter(nodepathString, keyword, fullPath)
            if parent:
                lis.append(parent)
    return lis


#
def getRoot(nodepathString, fullPath=True):
    objectFullPath = _dcc_getNodFullpathNodepathStr(nodepathString)
    if objectFullPath:
        root = nodepathString
        if objectFullPath.startswith(appCfg.DEF_mya_node_pathsep):
            splitData = objectFullPath.split(appCfg.DEF_mya_node_pathsep)
            root = splitData[1]
            #
            if fullPath:
                root = appCfg.DEF_mya_node_pathsep.join(splitData[:2])
        return root


#
def getObjectParentFilter(nodepathString, keyword, fullPath=True):
    string = none
    objectFullPath = _dcc_getNodFullpathNodepathStr(nodepathString)
    if objectFullPath:
        splitData = objectFullPath.split(appCfg.DEF_mya_node_pathsep)
        hasParent = False
        loc = 0
        #
        for seq, i in enumerate(splitData):
            if keyword in i:
                hasParent = True
                loc = seq
        #
        if hasParent:
            parent = splitData[loc]
            if fullPath:
                parent = appCfg.DEF_mya_node_pathsep.join(splitData[:loc + 1])
            string = parent
    return string


#
def getSelectedObjectsFilter(mType, fullPath=True):
    lis = []
    objectLis = cmds.ls(selection=1, long=fullPath)
    for nodepathString in objectLis:
        if _getNodeShapeCategoryString(nodepathString) == mType:
            lis.append(nodepathString)
    return lis


#
def getSelectedObjectsFilterByTypes(mTypes, fullPath=True):
    lis = []
    objectLis = cmds.ls(selection=1, long=fullPath)
    for nodepathString in objectLis:
        if _getNodeShapeCategoryString(nodepathString) in mTypes:
            lis.append(nodepathString)
    return lis


#
def setLoadReferenceFile(referenceNode, mFile):
    cmds.file(mFile, loadReference=referenceNode)


#
def setReloadReferenceFile(referenceNode):
    cmds.file(loadReference=referenceNode)


#
def setLoadReference(referenceNode):
    cmds.file(loadReference=referenceNode)


#
def setUnloadReference(referenceNode):
    cmds.file(unloadReference=referenceNode)


#
def setReferenceRemove(referenceNode):
    if _isAppExist(referenceNode):
        fileString_ = getReferenceFile(referenceNode)
        cmds.file(fileString_, removeReference=1)


#
def setCleanNodeForce(node):
    if _isAppExist(node) and not isReferenceNode(node):
        cmds.lockNode(node, lock=0)
        cmds.delete(node)


#
def setCleanNode(node):
    if _isAppExist(node) and not isReferenceNode(node) and not isNodeLocked(node):
        cmds.delete(node)


# Clean Nde_Node By Name
def setCleanNodesForce(nodes):
    [setCleanNodeForce(node) for node in nodes]


#
def setNodesClear(nodes):
    [setCleanNode(node) for node in nodes]


#
def setNodesClearByNamespace(namespace):
    nodes = getDependNodesByNamespace(namespace)
    if nodes:
        setNodesClear(nodes)


#
def setCleanUnusedSets():
    unusedSets = getUnusedSets()
    setNodesClear(unusedSets)


#
def setCleanUnusedDisplayLayers():
    unusedLayers = getUnusedDisplayLayers()
    setNodesClear(unusedLayers)


#
def setCleanUnusedRenderLayers():
    unusedLayers = getUnusedRenderLayers()
    setNodesClear(unusedLayers)


#
def setUnusedNamespacesClean():
    namespaces = getNamespaceLis()
    if namespaces:
        for namespace in namespaces:
            cmds.namespace(setNamespace=namespace)
            childNamespaceList = cmds.namespaceInfo(recurse=1, listOnlyNamespaces=1)
            nodes = cmds.namespaceInfo(listOnlyDependencyNodes=1, dagPath=1)
            #
            parentNamespace = cmds.namespaceInfo(parent=1)
            cmds.namespace(setNamespace=':')
            if not childNamespaceList:
                if not nodes:
                    cmds.namespace(removeNamespace=namespace)
                else:
                    isClean = False
                    #
                    for node in nodes:
                        if cmds.referenceQuery(node, isNodeReferenced=1):
                            isClean = True
                            break
                    #
                    if not isClean:
                        cmds.namespace(force=1, moveNamespace=(namespace, parentNamespace))
                        cmds.namespace(removeNamespace=namespace)


#
def setCleanUnknownPlugs():
    unknownPlugs = cmds.unknownPlugin(query=1, list=1)
    if unknownPlugs:
        for plugLoadName in unknownPlugs:
            cmds.unknownPlugin(plugLoadName, remove=1)


#
def setCleanUnknownNodes():
    unknownNodes = cmds.ls(type='unknown')
    if unknownNodes:
        setCleanNodesForce(unknownNodes)


# Get Frame Range
def getFrameRange(startFrame=none):
    # Lis [ <Start Frame>,
    #       <End Frame> ]
    if not startFrame:
        startFrame = int(cmds.playbackOptions(query=1, minTime=1))
    endFrame = int(cmds.playbackOptions(query=1, maxTime=1))
    if startFrame >= endFrame:
        startFrame = int(cmds.playbackOptions(query=1, minTime=1))
    return startFrame, endFrame


# Get Render Size
def getRenderSize():
    width = cmds.getAttr('defaultResolution.width')
    height = cmds.getAttr('defaultResolution.height')
    return width, height


#
def setCurrentFrame(frame):
    cmds.currentTime(frame)


#
def getCurrentFrame():
    return cmds.currentTime(query=1)


#
def setAnimationFrameRange(startFrame, endFrame):
    cmds.playbackOptions(minTime=startFrame)
    cmds.playbackOptions(animationStartTime=int(startFrame) - 5)
    cmds.playbackOptions(maxTime=endFrame)
    cmds.playbackOptions(animationEndTime=int(endFrame) + 5)


#
def setCreateNode(nodeType, name):
    cmds.createNode(nodeType, name=name)


#
def _toAppCompPathLis(objectPath):
    lis = []
    #
    dataArray = objectPath.split(appCfg.DEF_mya_node_pathsep)
    #
    dataCount = len(dataArray)
    for seq, data in enumerate(dataArray):
        if data:
            if seq + 1 < dataCount:
                subPath = appCfg.DEF_mya_node_pathsep.join(dataArray[:seq + 1])
                lis.append(subPath)
    #
    lis.append(objectPath)
    return lis


#
def setCompAppPathCreate(objectPath, isLock=False):
    objectName = _nodeString2nodename_(objectPath)
    parentPath = _toNodeParentPath(objectPath)
    if not _isAppExist(objectPath):
        cmds.group(empty=1, name=objectName)
    #
    if parentPath:
        setObjectParent('|' + objectName, parentPath)
    #
    if isLock:
        setObjectTransformationAttr(objectPath)


#
def setAppPathCreate(objectPath, isLock=False):
    appCompPathLis = _toAppCompPathLis(objectPath)
    for subPath in appCompPathLis:
        setCompAppPathCreate(subPath, isLock)


#
def setNodeParentPathCreate(objectPath):
    appCompPathLis = _toAppCompPathLis(objectPath)
    for seq, subPath in enumerate(appCompPathLis):
        if not subPath == objectPath:
            setCompAppPathCreate(subPath)


#
def setCloneHierarchy(root, cloneRoot='|clone_grp'):
    if not _isAppExist(cloneRoot):
        cmds.group(empty=1, name=cloneRoot)
    paths = getGroupLisByRoot(root)
    for path in paths:
        clonePath = cloneRoot + path
        setCompAppPathCreate(clonePath)


#
def setGpu(name, mFile):
    if not _isAppExist(name):
        cmds.createNode(appCfg.DEF_mya_type_transform, name=name)
        cmds.createNode('gpuCache', name=name + '_inCache', parent=name)
    if os.path.isfile(mFile):
        cmds.setAttr(name + '_inCache' + '.cacheFileName', mFile, type='string')


#
def getConnectAttrData(nodepathString, attrName):
    lis = []
    attr = nodepathString + '.' + attrName
    if _isAppExist(attr):
        data = cmds.listConnections(attr)
        if data:
            lis = data
    return lis


#
def setAttrConnect(sourceAttr, targetAttr):
    if _isAppExist(sourceAttr) and _isAppExist(targetAttr):
        if not cmds.isConnected(sourceAttr, targetAttr):
            cmds.connectAttr(sourceAttr, targetAttr, force=1)


#
def isAttrConnected(sourceAttr, targetAttr):
    if _isAppExist(sourceAttr) and _isAppExist(targetAttr):
        return cmds.isConnected(sourceAttr, targetAttr)
    else:
        return False


#
def setAttrDisconnect(sourceAttr, targetAttr):
    if _isAppExist(sourceAttr) and _isAppExist(targetAttr):
        if cmds.isConnected(sourceAttr, targetAttr):
            cmds.disconnectAttr(sourceAttr, targetAttr)


#
def setObjectClearInputConnection(nodepathString):
    inputConnectionLis = getNodeInputConnectionLis(nodepathString)
    if inputConnectionLis:
        for sourceAttr, targetAttr in inputConnectionLis:
            setAttrDisconnect(sourceAttr, targetAttr)


#
def setObjectClearOutputConnection(nodepathString):
    outputConnectionLis = getNodeOutputConnectionLis(nodepathString)
    if outputConnectionLis:
        for sourceAttr, targetAttr in outputConnectionLis:
            setAttrDisconnect(sourceAttr, targetAttr)


#
def setObjectSingleShow(boolean):
    cmds.isolateSelect('modelPanel4', state=boolean)


#
def setDefaultShaderColor(red, green, blue):
    cmds.setAttr('lambert1.color', red, green, blue)


#
def setDefaultShaderRandomColor():
    colorRange = [i / 100.0 for i in range(0, 100)]
    cmds.setAttr('lambert1.color', choice(colorRange), choice(colorRange), choice(colorRange))


#
def setObjectDefaultShadingEngine(maObj):
    shape = _dcc_getNodShapeNodepathStr(maObj)
    shadingEngines = _getNodeTargetNodeStringList(shape, appCfg.DEF_mya_type_shading_engine)
    if not shadingEngines:
        cmds.sets(shape, forceElement='initialShadingGroup')


#
def getRandomColor():
    values = [i / 100.0 for i in range(0, 100)]
    return choice(values), choice(values), choice(values)


#
def getRandomValue(valueRange):
    values = [i for i in range(valueRange[0], valueRange[1])]
    return choice(valueRange)


# Set Plugs
def getPlugLis():
    return cmds.pluginInfo(query=1, listPlugins=1)


#
def setPlugLoad(plugLoadName):
    cmds.loadPlugin(plugLoadName, quiet=1)


#
def isPlugLoaded(plugLoadName):
    return cmds.pluginInfo(plugLoadName, query=1, loaded=1)


#
def isPlugRegistered(plugLoadName):
    return cmds.pluginInfo(plugLoadName, query=1, registered=1)


#
def setPlugUnload(plugLoadName):
    cmds.unloadPlugin(plugLoadName, force=1)


#
def getPlugPath(plugLoadName):
    return cmds.pluginInfo(plugLoadName, query=1, path=1)


# Set Clean Turtle
def setCleanTurtle():
    setPlugUnload('Turtle')
    unusedNodes = [
        'TurtleRenderOptions',
        'TurtleDefaultBakeLayer',
        'TurtleBakeLayerManager',
        'TurtleUIOptions'
    ]
    setCleanNodesForce(unusedNodes)


# Set Blend
def setNodeBlendCreate(sourceObject, targetObject, nodeName):
    if _isAppExist(sourceObject) and _isAppExist(targetObject):
        sourceShape = _dcc_getNodShapeNodepathStr(sourceObject, 1)
        targetShape = _dcc_getNodShapeNodepathStr(targetObject, 1)
        #
        isVisibility = cmds.getAttr(targetShape + '.visibility')
        cmds.setAttr(targetShape + '.visibility', 1)
        # worldMatrix = getNodeWorldMatrix(sourceObject)
        # if not worldMatrix == DEF_mya_default_matrix:
        #     pass
        # cmds.blendShape(sourceShape, targetShape, name=nodeName, weight=(0, 1), before=1)
        cmds.blendShape(sourceShape, targetShape, name=nodeName, weight=(0, 1), origin='world', before=1)
        if isVisibility == 0:
            cmds.setAttr(targetShape + '.visibility', 0)


# Get File
def getFile(caption='Open', okCaption='*', startingDirectory=none):
    fileLis = cmds.fileDialog2(
        caption=caption, okCaption='%s' % okCaption, fileMode=4,
        startingDirectory=startingDirectory)
    return fileLis


# Get Folder
def getFolder(caption='Open ', okCaption='*', startingDirectory=none):
    fileLis = cmds.fileDialog2(
        caption=caption, okCaption='%sFolder' % okCaption, fileMode=2,
        startingDirectory=startingDirectory)
    return fileLis


#
def setNodeDelete(nodepathString):
    if _isAppExist(nodepathString):
        cmds.delete(nodepathString)


#
def setNodesDelete(nodeLis):
    stringLis = bscMethods.String.toList(nodeLis)
    [setNodeDelete(i) for i in stringLis]


#
def getCurrentFile():
    return cmds.file(query=1, expandName=1)


# Get Current RenderLayer
def getCurrentRenderLayer():
    # Str <Render Layer>
    currentRenderLayer = cmds.editRenderLayerGlobals(query=1, currentRenderLayer=1)
    if currentRenderLayer == 'defaultRenderLayer':
        currentRenderLayer = 'masterLayer'
    return currentRenderLayer


#
def getTimeUnit():
    return cmds.currentUnit(query=1, time=1)


#
def getShowTimeUnit():
    timeUnit = getTimeUnit()
    dic = ''


#
def setTimeUnit(unit):
    cmds.currentUnit(time=unit)


#
def isArnoldEnable():
    return cmds.objExists('defaultArnoldRenderOptions')


#
def isRedshiftEnable():
    return cmds.objExists('redshiftOptions')


#
def setObjectHiddenInOutline(nodepathString, boolean=1):
    cmds.setAttr(nodepathString + '.hiddenInOutliner', boolean)


#
def runMelCommand(command):
    mel.eval(command)


#
def setRebuildMayaUi():
    setWindowDelete('unifiedRenderGlobalsWindow')
    runMelCommand('buildNewSceneUI;')


# Get Name Overlapping
def getNameOverlappingObjectLis(mObjectPaths):
    lis = []
    for mObjectPath in mObjectPaths:
        objectName = _nodeString2nodename_(mObjectPath)
        data = cmds.ls(objectName, long=1)
        if len(data) > 1:
            lis.append(mObjectPath)
    return lis


#
def setCreateMeshObjectEdgeSmooth(nodepathString):
    cmds.polySoftEdge(nodepathString, a=180, constructionHistory=0)


#
def getMeshBoundingBox(objectLis):
    return cmds.polyEvaluate(objectLis, boundingBox=1)


#
def setObjectMove(nodepathString, x, y, z):
    cmds.move(x, y, z, nodepathString, relative=1)


#
def toM2Object(mNode):
    return toM2DagNode(mNode).object()


#
def toM2NodePath(nodepathString):
    return OpenMaya.MGlobal.getSelectionListByName(nodepathString).getDagPath(0)


# noinspection PyArgumentList
def toM2TransformNode(nodepathString, mode=0):
    if mode == 0:
        return OpenMaya.MFnTransform(toM2NodePath(nodepathString))
    if mode == 1:
        return OpenMaya.MFnTransform(nodepathString)


#
def getM2ObjectPath(m2Node):
    return m2Node.fullPathName()


# noinspection PyArgumentList
def toM2DagNode(nodepathString, mode=0):
    if mode == 0:
        return OpenMaya.MFnDagNode(toM2NodePath(nodepathString))
    if mode == 1:
        return OpenMaya.MFnDagNode(nodepathString)


#
def getBBoxMPointArray(m2BoundingBox):
    maxiM2Point = m2BoundingBox.max
    miniMPoint = m2BoundingBox.min
    return miniMPoint, maxiM2Point


#
def getIntArray(m2IntArray):
    return [int(i) for i in m2IntArray]


#
def getFloatArray(m2FloatArray):
    return [float(i) for i in m2FloatArray]


#
def toM2Matrix(matrix):
    m2Matrix = OpenMaya.MMatrix()
    for seq in range(4):
        for subSeq in range(4):
            m2Matrix.setElement(seq, subSeq, matrix[seq * 4 + subSeq])
    return m2Matrix


# noinspection PyArgumentList
def getMTransformationMatrix(matrix):
    return OpenMaya.MTransformationMatrix(toM2Matrix(matrix))


#
def getPointArray(m2PointArray):
    return [(i[0], i[1], i[2]) for i in m2PointArray]


#
def toM2Point(point):
    m2Point = OpenMaya.MPoint()
    m2Point.x, m2Point.y, m2Point.z = point
    return m2Point


#
def toM2PointArray(pointArray):
    m2PointArray = OpenMaya.MPointArray()
    for seq in range(len(pointArray)):
        point = pointArray[seq]
        m2Point = toM2Point(point)
        m2PointArray.append(m2Point)
    return m2PointArray


#
def getVectorArray(m2VectorArray):
    return [(i[0], i[1], i[2]) for i in m2VectorArray]


#
def toM2Vector(vector):
    m2Vector = OpenMaya.MVector()
    m2Vector.x, m2Vector.y, m2Vector.z = vector
    return m2Vector


#
def toM2VectorArray(vectorArray):
    m2VectorArray = OpenMaya.MVectorArray()
    for seq in range(len(vectorArray)):
        vector = vectorArray[seq]
        m2Vector = toM2Vector(vector)
        m2VectorArray.append(m2Vector)
    return m2VectorArray


#
def getFloatVector(m2FloatVector):
    x, y, z = m2FloatVector
    return x, y, z


#
def getTuple(m2Tuple):
    return '%s,%s' % (m2Tuple[0], m2Tuple[1])


#
def getFloatVectorArray(m2FloatVectorArray):
    return [(i[0], i[1], i[2]) for i in m2FloatVectorArray]


#
def toM2FloatVector(floatVector):
    m2FloatVector = OpenMaya.MFloatVector()
    m2FloatVector.x, m2FloatVector.y, m2FloatVector.z = floatVector
    return m2FloatVector


#
def toM2FloatVectorArray(floatVectorArray):
    m2FloatVectorArray = OpenMaya.MFloatVectorArray()
    for seq in range(len(floatVectorArray)):
        floatVector = floatVectorArray[seq]
        m2FloatVector = toM2FloatVector(floatVector)
        m2FloatVectorArray.append(m2FloatVector)
    return m2FloatVectorArray


#
def getObjectBBox(nodepathString):
    MObject = toM2DagNode(nodepathString)
    m2BoundingBox = MObject.boundingBox
    bBoxMPointArray = getBBoxMPointArray(m2BoundingBox)
    mini, maxi = getPointArray(bBoxMPointArray)
    _x, _y, _z = mini
    x, y, z = maxi
    return (x, _x), (y, _y), (z, _z)


#
def setSelMeshesToOrigin(mode=0):
    objectLis = getSelectedObjects(1, 1)
    if objectLis:
        bbox = getMeshBoundingBox(objectLis)
        (x, _x), (y, _y), (z, _z) = bbox
        centerX = (x + _x) / 2
        centerY = (y + _y) / 2
        centerZ = (z + _z) / 2
        for i in objectLis:
            if mode == 0:
                setObjectMove(i, -centerX, -centerY, -centerZ)
            elif mode == 1:
                setObjectMove(i, -centerX, -y, -centerZ)


#
def getPivotByBBox(nodepathString):
    bBox = getObjectBBox(nodepathString)
    pivot = []
    for seq, i in enumerate(['X', 'Y', 'Z']):
        p = bBox[seq][1]
        pivot.append(p)
    #
    cmds.xform(nodepathString, scalePivot=pivot, worldSpace=1)
    cmds.xform(nodepathString, rotatePivot=pivot, worldSpace=1)


#
def getTranslateByBBox(nodepathString, targetObject):
    origTranslate = getTranslateVector(nodepathString)
    bBox1 = getObjectBBox(nodepathString)
    bBox2 = getObjectBBox(targetObject)
    translation = []
    for seq, i in enumerate(['X', 'Y', 'Z']):
        t_o = origTranslate[seq]
        t_c = bBox2[seq][1] - bBox1[seq][1]
        t_t = t_o + t_c
        translation.append(t_t)
    #
    cmds.xform(nodepathString, translation=translation)


#
def getScaleByBBox(nodepathString, targetObject):
    # Debug ( Reset Scale Value)
    cmds.xform(nodepathString, scale=[1, 1, 1])
    #
    origScale = getScaleVector(nodepathString)
    bBox1 = getObjectBBox(nodepathString)
    bBox2 = getObjectBBox(targetObject)
    #
    scale = []
    for seq, i in enumerate(['X', 'Y', 'Z']):
        s_o = origScale[seq]
        s_c = float(bBox2[seq][1] - bBox2[seq][0]) / float(bBox1[seq][1] - bBox1[seq][0])
        #
        s_t = s_c + s_o - 1
        #
        scale.append(s_t)
    #
    cmds.xform(nodepathString, scale=scale)


#
def getOrigPivot(nodepathString):
    origTranslate = getTranslateVector(nodepathString)
    cmds.xform(nodepathString, pivots=origTranslate, worldSpace=1)


#
def getNodeTypeLisByFilter(mType):
    return cmds.listNodeTypes(mType)


#
def setClearConstraintByRoot(root):
    constraints = getChildNodesByRoot(
        root,
        [
            'parentConstraint',
            'pointConstraint',
            'orientConstraint',
            'scaleConstraint'
        ]
    )
    if constraints:
        setNodesDelete(constraints)


#
def getTranslateVector_(nodepathString):
    return cmds.xform(nodepathString, query=1, translation=1)


#
def setTranslate_(nodepathString, data):
    cmds.xform(nodepathString, translation=data)


#
def getRotateVector_(nodepathString):
    return cmds.xform(nodepathString, query=1, rotation=1)


#
def setRotate_(nodepathString, data):
    cmds.xform(nodepathString, rotation=data)


#
def getScaleVector_(nodepathString):
    return cmds.xform(nodepathString, query=1, scale=1)


#
def setScale_(nodepathString, data):
    return cmds.xform(nodepathString, scale=data)


#
def getRotatePivotVector_(nodepathString, isWorld):
    return cmds.xform(nodepathString, query=1, rotatePivot=1, worldSpace=isWorld)


#
def getScalePivotVector_(nodepathString, isWorld):
    return cmds.xform(nodepathString, query=1, scalePivot=1, worldSpace=isWorld)


#
def setRotatePivot_(nodepathString, data, isWorld):
    cmds.xform(nodepathString, rotatePivot=data, worldSpace=isWorld)


#
def setScalePivot_(nodepathString, data, isWorld):
    cmds.xform(nodepathString, scalePivot=data, worldSpace=isWorld)


#
def getWorldRotatePivotVector_(nodepathString):
    worldPivot = getRotatePivotVector_(nodepathString, isWorld=True)
    localPivot = getRotatePivotVector_(nodepathString, isWorld=False)
    return [i - localPivot[index] for index, i in enumerate(worldPivot)]


#
def getWorldScalePivotVector_(nodepathString):
    worldPivot = getScalePivotVector_(nodepathString, isWorld=True)
    localPivot = getScalePivotVector_(nodepathString, isWorld=False)
    return [i - localPivot[index] for index, i in enumerate(worldPivot)]


#
def getRotate_(nodepathString, targetObject):
    tarRotate = getRotateVector(targetObject)
    cmds.xform(nodepathString, rotation=tarRotate)


#
def setZeroPos_(nodepathString):
    setTranslate_(nodepathString, [0, 0, 0])
    setRotate_(nodepathString, [0, 0, 0])
    setScale_(nodepathString, [1, 1, 1])


#
def getPos_(nodepathString, targetObject):
    # Record Pos
    tarTranslate = getTranslateVector_(targetObject)
    tarRotate = getRotateVector_(targetObject)
    tarScale = getScaleVector_(targetObject)
    # Zero Pos
    setZeroPos_(targetObject)
    # Translate with Scale Pivot
    bugOffset = getWorldScalePivotVector_(targetObject)
    setTranslate_(nodepathString, bugOffset)
    # Get World Pivot
    tarWorldRotatePivot = getRotatePivotVector_(targetObject, isWorld=True)
    setRotatePivot_(nodepathString, tarWorldRotatePivot, isWorld=True)
    #
    tarWorldScalePivot = getScalePivotVector_(targetObject, isWorld=True)
    setScalePivot_(nodepathString, tarWorldScalePivot, isWorld=True)
    # Set Target Orig Pos
    setTranslate_(targetObject, tarTranslate)
    setRotate_(targetObject, tarRotate)
    setScale_(targetObject, tarScale)
    # Set Object Orig Pos
    translateOffset = [i + bugOffset[index] for index, i in enumerate(tarTranslate)]
    setTranslate_(nodepathString, translateOffset)
    setRotate_(nodepathString, tarRotate)
    setScale_(nodepathString, tarScale)
    #
    getPosition(nodepathString, targetObject)
    getScale(nodepathString, targetObject)


#
def viewWarning(string):
    cmds.warning(string)


#
def viewError(string):
    cmds.error(string)


#
def getOptionVar(var):
    return cmds.optionVar(query=var)


#
def delOptionVar(var):
    cmds.optionVar(remove=var)


#
def setNodeShowByGroup(groupName):
    cmds.showHidden(groupName, below=True)


#
def translateAnimationPosition(sourceObject, targetObject, startFrame, endFrame, frameOffset=0):
    def setRotationCovert(frame, r0, r1):
        x0, y0, z0 = r0
        x1, y1, z1 = r1
        #
        x_ = x0 + x1
        y_ = y0 + y1
        z_ = z0 + z1
        #
        x, y, z = x1, y1, z1
        # Error 0
        if y_ != 0 and z_ != 0:
            if round((y_ + z_), 4) == 0:
                x = 180 + x1
                y = y0
                z = z0
                print 'Fix {} RotateX {} > {} '.format(frame, x1, x)
        if x_ != 0 and z_ != 0:
            if round((x_ + z_), 4) == 0:
                x = x0
                y = 180 + y1
                z = z0
                print 'Fix {} RotateY {} > {} '.format(frame, y1, y)
        if x_ != 0 and y_ != 0:
            if round((x_ + y_), 4) == 0:
                x = x0
                y = y0
                z = 180 + z1
                print 'Fix {} RotateZ {} > {} '.format(frame, z1, z)
        # Error 1
        _x = int(abs(x0 - x1)) + 1
        _y = int(abs(y0 - y1)) + 1
        _z = int(abs(z0 - z1)) + 1
        if _x == 360:
            x = x0 - (x0 - x1) % 360
            print 'Fix {} RotateX {} > {} '.format(frame, x1, x)
        if _y == 360:
            y = y0 - (y0 - y1) % 360
            print 'Fix {} RotateY {} > {} '.format(frame, y1, y)
        if _z == 360:
            z = z0 - (z0 - z1) % 360
            print 'Fix {} RotateZ {} > {} '.format(frame, z1, z)
        return [x, y, z]
    #
    def getWorldTranslation(nodepathString):
        return cmds.xform(nodepathString, query=1, worldSpace=1, translation=1)
    #
    def getWorldRotation(nodepathString):
        return cmds.xform(nodepathString, query=1, worldSpace=1, rotation=1)
    #
    def getWordScale(nodepathString):
        return cmds.xform(nodepathString, query=1, worldSpace=1, scale=1)
    #
    def setTranslation(frame):
        worldTranslation = getWorldTranslation(sourceObject)
        for seq, v in enumerate(worldTranslation):
            cmds.setKeyframe(targetObject, attribute=translationAttrNameLis[seq], time=(frame, frame), value=v, noResolve=1)
        return worldTranslation
    #
    def setRotation(frame, preWorldRotation):
        worldRotation = setRotationCovert(frame, preWorldRotation, getWorldRotation(sourceObject))
        for seq, v in enumerate(worldRotation):
            cmds.setKeyframe(targetObject, attribute=rotationAttrNameLis[seq], time=(frame, frame), value=v, noResolve=1)
        return worldRotation
    #
    def setScale(frame):
        for seq, scale in enumerate(getWordScale(sourceObject)):
            cmds.setKeyframe(targetObject, attribute=scaleAttrNameLis[seq], time=(frame, frame), value=scale, noResolve=1)
    #
    def setMain():
        preWorldRotation = [0, 0, 0]
        for frame in range(startFrame - frameOffset, endFrame + frameOffset + 1):
            cmds.currentTime(frame)
            #
            setTranslation(frame)
            #
            worldRotation = setRotation(frame, preWorldRotation)
            # Update Pre
            preWorldRotation = worldRotation
            #
            setScale(frame)
    #
    translationAttrNameLis = ['translateX', 'translateY', 'translateZ']
    rotationAttrNameLis = ['rotateX', 'rotateY', 'rotateZ']
    scaleAttrNameLis = ['scaleX', 'scaleY', 'scaleZ']
    #
    setMain()


#
def getNodeWorldMatrix(nodepathString):
    return cmds.xform(nodepathString, query=1, matrix=1, worldSpace=1) or DEF_mya_default_matrix


#
def isDefaultMatrix(nodepathString):
    return getNodeWorldMatrix(nodepathString) == DEF_mya_default_matrix


#
def getNodeWorldBoundingBox(nodepathString):
    return cmds.xform(nodepathString, query=1, boundingBox=1, worldSpace=1) or [0, 0, 0, 0, 0, 0]


#
def getNodeBoundingBox(nodepathString):
    lis = []
    mainAttrName = 'boundingBox'
    subAttrNameLis = ['boundingBoxMin', 'boundingBoxMax']
    axisLis = ['X', 'Y', 'Z']
    for subAttrName, axis in product(subAttrNameLis, axisLis):
        attr = '{}.{}.{}.{}{}'.format(nodepathString, mainAttrName, subAttrName, subAttrName, axis)
        lis.append(cmds.getAttr(attr))
    return lis


#
def setNodeCenterPivots(nodepathString):
    cmds.xform(nodepathString, centerPivots=True)


#
def setNodeWorldMatrix(nodepathString, worldMatrix):
    cmds.xform(nodepathString, matrix=worldMatrix, worldSpace=1)


#
def updateProgressBar(cls):
    if cls.MaProgressBar is None:
        cls.MaProgressBar = mel.eval('$lynxiProgressVar = $gMainProgressBar')


#
class MaProgressBar(object):
    MaProgressExplain = None
    MaProgressBar = None
    MaMaxProgressValue = 1
    MaProgressValue = 0
    #
    def updateProgressBar(self):
        if self.MaProgressBar is None:
            self.MaProgressBar = mel.eval('$lynxiProgressVar = $gMainProgressBar')
    #
    def viewProgress(self, explain, maxValue):
        if maxValue > 0:
            self.MaProgressExplain = explain
            self.updateProgressBar()
            self.MaMaxProgressValue = maxValue
            self.MaProgressValue = 0
            #
            cmds.progressBar(
                self.MaProgressBar,
                edit=True,
                beginProgress=True,
                isInterruptable=True,
                status=explain,
                maxValue=maxValue
            )
        return self
    #
    def updateProgress(self, subExplain=None):
        if self.MaProgressBar is not None:
            self.MaProgressValue += 1
            if self.MaProgressValue == self.MaMaxProgressValue:
                self.closeProgress()
            else:
                cmds.progressBar(self.MaProgressBar, edit=True, step=1)
                if subExplain is not None:
                    cmds.progressBar(self.MaProgressBar, edit=True, status='{} ( {} )'.format(self.MaProgressExplain, subExplain))
    #
    def closeProgress(self):
        cmds.progressBar(self.MaProgressBar, edit=True, endProgress=True)


#
def getMeshShapeDeformDatumLis(groupString):
    lis = []
    shapeLis = getChildShapesByRoot(groupString, filterTypes='mesh')
    if shapeLis:
        progressBar = MaProgressBar()
        maxValue = len(shapeLis)
        progressBar.viewProgress('Read Datum(s)', maxValue)
        for targetShapePath in shapeLis:
            progressBar.update()
            if targetShapePath.endswith(appCfg.MaKeyword_ShapeDeformed):
                transformPath = _toTransformByNodePath(targetShapePath)
                namespace = _toNamespaceByNodePath(transformPath)
                shapeName = _nodeString2nodename_(targetShapePath)
                sourceShapeName = shapeName[:-len(appCfg.MaKeyword_ShapeDeformed)]
                sourceShapePath = transformPath + '|' + namespace + ':' + sourceShapeName
                if _isAppExist(sourceShapePath):
                    lis.append((sourceShapePath, targetShapePath))
    return lis


# View Maya Message
def setMessageWindowShow(message, keyword, position='topCenter', fade=1, dragKill=0, alpha=.5):
    # topLeft topCenter topRight
    # midLeft midCenter midCenterTop midCenterBot midRight
    # botLeft botCenter botRight
    assistMessage = '%s <hl>%s</hl>' % (message, keyword)
    cmds.inViewMessage(
        assistMessage=assistMessage,
        fontSize=12,
        position=position,
        fade=fade,
        dragKill=dragKill,
        alpha=alpha
    )


# View Maya Message
def viewResult(message, keyword, position='botLeft', fade=1, dragKill=0, alpha=1):
    # topLeft topCenter topRight
    # midLeft midCenter midCenterTop midCenterBot midRight
    # botLeft botCenter botRight
    assistMessage = '%s <hl>%s</hl>' % (message, keyword)
    cmds.inViewMessage(
        assistMessage=assistMessage,
        fontSize=8,
        position=position,
        fade=fade,
        dragKill=dragKill,
        alpha=alpha
    )


#
def setViewportVp2Renderer(modelPanel, mode=0):
    # Render Name [<vp2Renderer>, ]
    currentPanel = modelPanel
    rendererName = 'base_OpenGL_Renderer'
    if mode == 1:
        rendererName = 'vp2Renderer'
    panelType = cmds.getPanel(typeOf=currentPanel)
    if panelType == 'modelPanel':
        cmds.modelEditor(currentPanel, edit=1, rendererName=rendererName, rom='myOverride')
        if rendererName == 'vp2Renderer':
            cmds.setAttr('hardwareRenderingGlobals.lineAAEnable', 1)
            cmds.setAttr('hardwareRenderingGlobals.multiSampleEnable', 1)
            cmds.setAttr('hardwareRenderingGlobals.ssaoEnable', 1)