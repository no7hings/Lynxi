# encoding=utf-8
import os
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.mel as mel


def toLodFile(fileString_, lod):
    if fileString_ is not None:
        if lod > 0:
            base, ext = os.path.splitext(fileString_)
            return '{}_lod{}{}'.format(base, str(lod).zfill(2), ext)
        else:
            return fileString_


#
def toImportAssetGroupName(nodeName):
    return nodeName + '_importAsset' + '_grp'


#
def toDecomposeMatrixNodeName(nodeName):
    return nodeName + '_decomposeMatrix'


# Get Maya File Type
def _getMaFileType(fileString_):
    mayaFileType = 'mayaAscii'
    fieType = os.path.splitext(fileString_)[-1]
    if fieType == '.ma':
        mayaFileType = 'mayaAscii'
    elif fieType == '.mb':
        mayaFileType = 'mayaBinary'
    elif fieType == '.abc':
        mayaFileType = 'Alembic'
    return mayaFileType


#
def setAsbLodSwitchSubCmd(nodePath, lod):
    def setSubBranch(args):
        nodeType, inputAttrName, outputAttrName = args
        #
        data = cmds.listRelatives(nodePath, children=1, shapes=1, noIntermediate=0, fullPath=1, type=nodeType)
        if data:
            subNodePath = data[0]
            #
            outputFile = cmds.getAttr(nodePath + '.' + inputAttrName)
            if outputFile:
                lodFile = toLodFile(outputFile, lod)
                if os.path.isfile(lodFile):
                    cmds.setAttr(
                        subNodePath + '.' + outputAttrName,
                        lodFile,
                        type='string'
                    )
                else:
                    cmds.warning('file "{}" is not found.'.format(lodFile))
    #
    datumLis = [
        ('aiStandIn', 'proxyCacheFile', 'dso'),
        ('gpuCache', 'gpuCacheFile', 'cacheFileName')
    ]
    #
    for i in datumLis:
        setSubBranch(i)


#
def setCurAsbLodSwitchCmd(nodePath):
    lod = cmds.getAttr(nodePath + '.lod')
    setAsbLodSwitchSubCmd(nodePath, lod)


#
def setSelAsbSwitchCmd(lod):
    selNodeLis = cmds.ls(type='asbTransform', selection=1, dagObjects=1, long=1)
    if selNodeLis:
        for nodePath in selNodeLis:
            setAsbLodSwitchSubCmd(nodePath, lod)
            cmds.setAttr(nodePath + '.lod', lod)


#
def setMatrixConnect(nodePath, nodeName, importGroupName):
    worldMatrix = cmds.xform(nodePath, query=1, matrix=1, worldSpace=1)
    cmds.xform(importGroupName, matrix=worldMatrix, worldSpace=1)
    decomposeMatrixNode = cmds.createNode('decomposeMatrix', name=toDecomposeMatrixNodeName(nodeName))
    cmds.connectAttr(nodePath + '.' + 'worldMatrix[0]', decomposeMatrixNode + '.' + 'inputMatrix')
    #
    connectDatumLis = [
        ('outputTranslate', 'translate'),
        ('outputRotate', 'rotate'),
        ('outputScale', 'scale')
    ]
    for sourceAttr, targetAttr in connectDatumLis:
        cmds.connectAttr(decomposeMatrixNode + '.' + sourceAttr, importGroupName + '.' + targetAttr)


#
def setChildVisible(nodePath, boolean):
    def setSubBranch(args):
        nodeType, inputAttrName = args
        data = cmds.listRelatives(nodePath, children=1, shapes=1, noIntermediate=0, fullPath=1, type=nodeType)
        if data:
            subNodePath = data[0]
            cmds.setAttr(subNodePath + '.' + inputAttrName, boolean)
    #
    datumLis = [
        ('aiStandIn', 'visibility'),
        ('gpuCache', 'visibility')
    ]
    #
    for i in datumLis:
        setSubBranch(i)


#
def setSelAsbImportAddSubCmd(nodePath):
    nodeName = nodePath.split('|')[-1]
    attrName = 'assetFile'
    fileString_ = cmds.getAttr(nodePath + '.' + attrName)
    #
    namespace = cmds.getAttr(nodePath + '.' + 'namespace')
    importGroupName = toImportAssetGroupName(nodeName)
    #
    if importGroupName is not None and fileString_ is not None:
        if not cmds.objExists(importGroupName):
            if os.path.isfile(fileString_):
                cmds.file(
                    fileString_,
                    i=1,
                    options='v=0;',
                    type=_getMaFileType(fileString_),
                    ra=1,
                    mergeNamespacesOnClash=1,
                    namespace=namespace,
                    preserveReferences=1,
                    groupReference=True,
                    groupName=importGroupName
                )
                #
                setMatrixConnect(nodePath, nodeName, importGroupName)


#
def setSelAsbImportAddCmd():
    selNodeLis = cmds.ls(type='asbTransform', selection=1, dagObjects=1, long=1)
    if selNodeLis:
        for nodePath in selNodeLis:
            setSelAsbImportAddSubCmd(nodePath)
            setChildVisible(nodePath, 0)
        #
        cmds.select(selNodeLis[-1])


#
def setSelAsbRefAddCmd(nodePath):
    nodeName = nodePath.split('|')[-1]
    attrName = 'assetFile'
    fileString_ = cmds.getAttr(nodePath + '.' + attrName)
    #
    namespace = cmds.getAttr(nodePath + '.' + 'namespace')
    importGroupName = toImportAssetGroupName(nodeName)
    #
    if importGroupName is not None and fileString_ is not None:
        if not cmds.objExists(importGroupName):
            if os.path.isfile(fileString_):
                cmds.file(
                    fileString_,
                    ignoreVersion=1,
                    reference=1,
                    mergeNamespacesOnClash=0,
                    namespace=namespace,
                    options='v=0;',
                    type=_getMaFileType(fileString_),
                    groupReference=True,
                    groupName=importGroupName
                )
                #
                cmds.setAttr(importGroupName + '.' + 'useOutlinerColor', 1)
                cmds.setAttr(importGroupName + '.' + 'outlinerColor', 0, 1, 0)
                #
                setMatrixConnect(nodePath, nodeName, importGroupName)


#
def setSelAsbRefsAddCmd():
    selNodeLis = cmds.ls(type='asbTransform', selection=1, dagObjects=1, long=1)
    if selNodeLis:
        for nodePath in selNodeLis:
            setSelAsbRefAddCmd(nodePath)
            setChildVisible(nodePath, 0)
        #
        cmds.select(selNodeLis[-1])


#
def setSelAsbRemoveSubCmd(nodePath):
    nodeName = nodePath.split('|')[-1]
    #
    namespace = cmds.getAttr(nodePath + '.' + 'namespace')
    importGroupName = toImportAssetGroupName(nodeName)
    #
    referenceNode = namespace + 'RN'
    #
    if importGroupName is not None:
        if cmds.objExists(referenceNode):
            cmds.file(cmds.referenceQuery(referenceNode, filename=1), removeReference=1)
        #
        else:
            nodeLis = cmds.namespaceInfo(namespace, listOnlyDependencyNodes=1, dagPath=1)
            if nodeLis:
                [cmds.delete(i) for i in nodeLis if cmds.objExists(i)]
        #
        if cmds.objExists(importGroupName):
            cmds.delete(importGroupName)


#
def setSelAsbRemoveCmd():
    selNodeLis = cmds.ls(type='asbTransform', selection=1, dagObjects=1, long=1)
    if selNodeLis:
        for nodePath in selNodeLis:
            setSelAsbRemoveSubCmd(nodePath)
            setChildVisible(nodePath, 1)
        #
        cmds.select(selNodeLis[-1])