# coding=utf-8
import os, collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore import lxConfigure
#
from LxCore.preset import prsVariant
#
from LxCore.preset.prod import projectPr, assetPr, scenePr
#
from LxMaya.command import maUtils
#
from LxMaya.product.data import datAsset
#
none = ''


#
def getRigAssetData(referenceNode, projectName):
    keyword = prsVariant.Util.astAnimationRigFileLabel
    subKeyword = prsVariant.Util.astLayoutRigFileLabel
    #
    referenceFile = cmds.referenceQuery(referenceNode, filename=1)
    data = ()
    # Filter is Rig
    if keyword in referenceFile or subKeyword in referenceFile:
        splitKey = keyword
        if subKeyword in referenceFile:
            splitKey = subKeyword
        #
        fileName = os.path.basename(referenceFile)
        #
        assetName = fileName.split(splitKey)[0]
        #
        assetClass = None
        #
        rigAssetName = prsVariant.Util.astBasicOsFileNameConfig(assetName, keyword, none)
        if subKeyword in referenceFile:
            rigAssetName = prsVariant.Util.astBasicOsFileNameConfig(assetName, subKeyword, none)
        # Check is Rig File
        if rigAssetName in fileName:
            # Number
            number = '0000'
            attrData = maUtils.getAttrDatum(referenceNode, prsVariant.Util.basicNumberAttrLabel)
            if attrData:
                number = attrData
            # Variant
            variant = prsVariant.Util.astDefaultVariant
            attrData = maUtils.getAttrDatum(referenceNode, prsVariant.Util.basicVariantAttrLabel)
            if attrData:
                variant = attrData
            #
            data = assetClass, assetName, number, variant
    return data


#
def getReferenceDic(projectName):
    def getBranch():
        assetData = getRigAssetData(referenceNode, projectName)
        if assetData:
            assetClass, assetName, number, variant = assetData
            isLoaded = cmds.referenceQuery(referenceNode, isLoaded=1)
            isGpu = maUtils.getAttrDatum(referenceNode, prsVariant.Util.showGpuAttrLabel)
            #
            state = 'Unloaded'
            if isLoaded:
                state = 'Loaded'
            if isGpu:
                state = 'GPU'
            #
            dic[referenceNode] = assetClass, assetName, number, variant, state
    #
    dic = collections.OrderedDict()
    #
    referenceNodes = maUtils.getNodeLisByType('reference', 1)
    for referenceNode in referenceNodes:
        if not cmds.referenceQuery(referenceNode, isNodeReferenced=1):
            # Debug ( Share Reference )
            try:
                getBranch()
            except:
                pass
    return dic


#
def getAssetNumberReduceData(projectName):
    dic = collections.OrderedDict()
    #
    inData = getReferenceDic(projectName)
    if inData:
        for k, v in inData.items():
            referenceNode = k
            assetClass, assetName, number, assetVariant, state = v
            filterKey = '%s - %s' % (assetClass, assetName)
            dic.setdefault(filterKey, []).append(referenceNode)
    return dic


#
def getAssetDirectoryReduceData(projectName):
    dic = collections.OrderedDict()
    #
    inData = getReferenceDic(projectName)
    if inData:
        for k, v in inData.items():
            referenceNode = k
            assetClass, assetName, number, assetVariant, state = v
            if state == 'Loaded':
                currentFile = maUtils.getReferenceFile(referenceNode, 1)
                correctFile = assetPr.astUnitProductFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
                )[1]
                dic[referenceNode] = currentFile, correctFile
    return dic


#
def getAssetNamespaceDic(projectName):
    dic = collections.OrderedDict()
    #
    inData = getReferenceDic(projectName)
    if inData:
        for k, v in inData.items():
            referenceNode = k
            assetClass, assetName, number, assetVariant, state = v
            if state == 'Loaded':
                namespacePath = maUtils.getReferenceNamespace(referenceNode)
                dic[namespacePath] = referenceNode
    return dic


#
def getAssetNamespaceReduceData(projectName, sceneName, sceneVariant):
    def getBranch():
        if state == 'Loaded':
            currentNamespace = maUtils.getReferenceNamespace(referenceNode)

            correctNamespace = scenePr.scAstRigNamespace(sceneName, sceneVariant, assetName, number)
            #
            dic[referenceNode] = currentNamespace, correctNamespace
    dic = collections.OrderedDict()
    #
    inData = getReferenceDic(projectName)
    if inData:
        for referenceNode, (assetClass, assetName, number, assetVariant, state) in inData.items():
            getBranch()
    return dic


#
def getOverlappingNaming(checkData):
    errors = []
    for k, v in checkData.items():
        if len(v) > 1:
            for i in v:
                errors.append(i)
    return errors


#
def getAssetStatisticsData(projectName):
    dic = collections.OrderedDict()
    #
    inData = getReferenceDic(projectName)
    if inData:
        for k, v in inData.items():
            referenceNode = k
            assetClass, assetName, number, assetVariant, state = v
            dic.setdefault(assetClass, []).append((assetName, number, assetVariant, state, referenceNode))
    return dic


#
def getGeometryCheck(localData, serverData):
    hierCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck = getAnimationSceneMeshConstant(localData, serverData)
    checkResult = False
    if hierCheck and geomCheck:
        checkResult = True
    #
    return checkResult


#
def getAnimationSceneMeshConstant(localData, serverData):
    hierCheck = False
    geomCheck = False
    geomShapeCheck = False
    mapCheck = False
    mapShapeCheck = False
    checkItems = ['hierarchy', 'geometry', 'geometryShape', 'map', 'mapShape']
    if localData and serverData:
        for seq, checkItem in enumerate(checkItems):
            if checkItem in localData.keys() and checkItem in serverData:
                if seq == 0:
                    hierCheck = localData[checkItem] == serverData[checkItem]
                if seq == 1:
                    geomCheck = localData[checkItem] == serverData[checkItem]
                if seq == 2:
                    geomShapeCheck = localData[checkItem] == serverData[checkItem]
                if seq == 3:
                    mapCheck = localData[checkItem] == serverData[checkItem]
                if seq == 4:
                    mapShapeCheck = localData[checkItem] == serverData[checkItem]
    #
    return hierCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck


#
def getAssetConstantData(projectName, sceneName, sceneVariant, inData, progressBar=None):
    numberKeyArray = []
    #
    assetArray = []
    assetNumCortArray = []
    assetDirCortArray = []
    assetNsHirCortArray = []
    assetNsNmCortArray = []
    assetHirClrArray = []
    #
    assetHierCortArray = []
    assetGeomCortArray = []
    assetGeomShapeCortArray = []
    assetMapCortArray = []
    assetMapShapeCortArray = []
    if inData:
        for seq, (k, v) in enumerate(inData.items()):
            if progressBar:
                progressBar.update()
            referenceNode = k
            assetClass, assetName, number, assetVariant, state = v
            if state == 'Loaded':
                existNumber = maUtils.getAttrDatum(referenceNode, prsVariant.Util.basicNumberAttrLabel)
                #
                numberKey = '%s - %s - %s' % (assetClass, assetName, number)
                if existNumber and not numberKey in numberKeyArray:
                    assetNumCortArray.append(referenceNode)
                numberKeyArray.append(numberKey)
                # Directory and namespace
                currentFile = maUtils.getReferenceFile(referenceNode, 1)
                correctFile = assetPr.astUnitProductFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
                )[1]
                #
                if currentFile.lower() == correctFile.lower():
                    assetDirCortArray.append(referenceNode)
                #
                currentNamespace = maUtils.getReferenceNamespace(referenceNode)
                correctNamespace = scenePr.scAstRigNamespace(sceneName, sceneVariant, assetName, number)
                if not ':' in currentNamespace:
                    assetNsHirCortArray.append(referenceNode)
                #
                if currentNamespace == correctNamespace:
                    assetNsNmCortArray.append(referenceNode)
                #
                assetArray.append(referenceNode)
                namespace = maUtils.getReferenceNamespace(referenceNode)
                astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
                if maUtils.isAppExist(astUnitModelProductGroup):
                    #
                    nonRefObjects = maUtils.getNonRefChildObjectsByRoot(astUnitModelProductGroup, 'mesh', 1)
                    if not nonRefObjects:
                        assetHirClrArray.append(referenceNode)
                    # Nde_Geometry Check
                    localData = datAsset.getMeshObjectsConstantDic(assetName, namespace)
                    serverData = {}
                    hierCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck = getAnimationSceneMeshConstant(localData, serverData)
                    if hierCheck:
                        assetHierCortArray.append(referenceNode)
                    if geomCheck:
                        assetGeomCortArray.append(referenceNode)
                    if geomShapeCheck:
                        assetGeomShapeCortArray.append(referenceNode)
                    if mapCheck:
                        assetMapCortArray.append(referenceNode)
                    if mapShapeCheck:
                        assetMapShapeCortArray.append(referenceNode)
    return \
        assetArray, assetNumCortArray, assetDirCortArray, assetNsHirCortArray, assetNsNmCortArray, assetHirClrArray, \
        assetHierCortArray, assetGeomCortArray, assetGeomShapeCortArray, assetMapCortArray, assetMapShapeCortArray


#
def getCacheUpdateTag(timeTag):
    string = '0000_0000_0000'
    isCacheUseMultLine = projectPr.getIsCacheUseMultLine()
    if isCacheUseMultLine:
        string = timeTag
    return string