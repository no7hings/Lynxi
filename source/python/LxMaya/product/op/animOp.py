# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore import lxBasic
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import assetPr
#
from LxMaya.command import maUtils, maFile
#
inGpuAttrLabel = appVariant.inGpuAttrLabel
showGpuAttrLabel = appVariant.showGpuAttrLabel
#
none = ''


#
def setSwitchAssetGpu(projectName, referenceNode, classify, name, subNumber):
    update = lxBasic.getOsActiveTimeTag()
    artist = lxBasic.getOsUser()
    #
    startFrame, endFrame = maUtils.getFrameRange()
    #
    namespace = maUtils.getReferenceNamespace(referenceNode)
    astUnitModelProductGroup = '%s:%s' % (namespace, assetPr.astUnitModelProductGroupName(name))
    #
    tempPath = appVariant.temporaryDirectory(appVariant.serverAnimationRoot, projectName, artist, update)
    cacheFileName = appVariant.cacheFileNameConfig(name, subNumber, appVariant.asbGpuFileLabel, '_' + update)
    cacheFile = '%s/%s' % (tempPath, cacheFileName)
    gpuName = assetPr.astGpuName(name, subNumber)
    #
    maFile.abcExport(
        astUnitModelProductGroup,
        cacheFile,
        startFrame, endFrame, 1
    )
    maUtils.setGpu(gpuName, cacheFile)
    #
    maUtils.setAttrBooleanDatumForce_(referenceNode, showGpuAttrLabel, 1)
    maUtils.setAttrStringDatumForce_(referenceNode, inGpuAttrLabel, cacheFile)
    #
    maUtils.setUnloadReference(referenceNode)


#
def setSwitchAssetRig(projectName, referenceNode, classify, name, subNumber):
    #
    startFrame, endFrame = maUtils.getFrameRange()
    #
    cacheFile = maUtils.getAttrDatum(referenceNode, inGpuAttrLabel)
    if lxBasic.isOsExistsFile(cacheFile):
        lxBasic.setOsFileRemove(cacheFile)
    #
    gpuName = assetPr.astGpuName(name, subNumber)
    maUtils.setCleanNodeForce(gpuName)
    #
    maUtils.setAttrBooleanDatumForce_(referenceNode, showGpuAttrLabel, 0)
    maUtils.setAttrStringDatumForce_(referenceNode, inGpuAttrLabel, none)
    #
    maUtils.setReloadReferenceFile(referenceNode)


#
def setRepairReferenceNamespace(inData, progressBar=none):
    errorReferenceNamespaceDic = {}
    if inData:
        for seq, (namespacePath, referenceNode) in enumerate(inData.items()):
            if progressBar:
                progressBar.updateProgress()
            #
            tempNamespace = '_'.join(namespacePath.split(':')) + '_reduce_' + str(seq)
            #
            if ':' in namespacePath:
                #
                if not ':' in referenceNode:
                    maUtils.setReferenceNamespace(referenceNode, tempNamespace)
                #
                if ':' in referenceNode:
                    parentNamespacePath = referenceNode[:-len(referenceNode.split(':')[-1]) - 1]
                    # Delete & Rename
                    errorReferenceNamespaceDic.setdefault(parentNamespacePath, []).append(referenceNode)
    # Reference in Namespace
    if errorReferenceNamespaceDic:
        errorReferenceNodeLis = []
        #
        for seq, (parentNamespacePath, referenceNodes) in enumerate(errorReferenceNamespaceDic.items()):
            for subSeq, referenceNode in enumerate(referenceNodes):
                tempNamespace = '_'.join(parentNamespacePath.split(':')) + '_reduce_' + str(seq) + str(subSeq)
                maUtils.setReferenceNamespace(referenceNode, tempNamespace)
                errorReferenceNodeLis.append(referenceNode)
        #
        if errorReferenceNodeLis:
            for referenceNode in errorReferenceNodeLis:
                correctReferenceNode = referenceNode.split(':')[-1]
                maUtils.setRenameForce(referenceNode, correctReferenceNode)