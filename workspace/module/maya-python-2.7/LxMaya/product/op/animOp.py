# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscMethods
#
from LxPreset import prsOutputs
#
from LxCore.preset.prod import assetPr
#
from LxMaya.command import maUtils

#
inGpuAttrLabel = prsOutputs.Util.inGpuAttrLabel
showGpuAttrLabel = prsOutputs.Util.showGpuAttrLabel
#
none = ''


#
def setSwitchAssetRig(projectName, referenceNode, classify, name, subNumber):
    #
    startFrame, endFrame = maUtils.getFrameRange()
    #
    cacheFile = maUtils.getAttrDatum(referenceNode, inGpuAttrLabel)
    if bscMethods.OsFile.isExist(cacheFile):
        bscMethods.OsFile.remove(cacheFile)
    #
    gpuName = assetPr.astGpuName(name, subNumber)
    maUtils.setCleanNodeForce(gpuName)
    #
    maUtils.setAttrBooleanDatumForce_(referenceNode, showGpuAttrLabel, 0)
    maUtils.setAttrStringDatumForce_(referenceNode, inGpuAttrLabel, none)
    #
    maUtils.setReloadReferenceFile(referenceNode)


#
def setRepairReferenceNamespace(inData, progressBar=None):
    errorReferenceNamespaceDic = {}
    if inData:
        for seq, (namespacePath, referenceNode) in enumerate(inData.items()):
            if progressBar:
                progressBar.update()
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