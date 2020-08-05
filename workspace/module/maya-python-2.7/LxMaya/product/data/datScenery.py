# coding=utf-8
import collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscObjects
#
from LxCore.config import appCfg
#
from LxPreset import prsOutputs, prsMethods
#
from LxCore.preset.prod import assetPr, sceneryPr
#
from LxMaya.command import maUtils, maAsb
#
currentProjectName = prsMethods.Project.mayaActiveName()
# File Label
scnSceneryLocatorLabel = prsOutputs.Util.scnSceneryLocatorLabel
astDefaultVersion = prsOutputs.Util.astDefaultVersion
# Type Config
# Group Config
basicGroupLabel = prsOutputs.Util.basicGroupLabel
basicModelLinkGroupLabel = prsOutputs.Util.basicModelLinkGroupLabel
basicGeometryGroupLabel = prsOutputs.Util.basicGeometryGroupLabel
basicSolverGeometrySubGroupLabel = prsOutputs.Util.basicSolverGeometrySubGroupLabel
basicCfxLinkGroupLabel = prsOutputs.Util.basicCfxLinkGroupLabel
#
basicAssemblyLabel = prsOutputs.Util.basicAssemblyLabel
scnAssemblyPrefix = prsOutputs.Util.scnAssemblyPrefix
#
none = ''


# Get List's Reduce
def getReduceList(lis):
    reduceLis = []
    if lis:
        [reduceLis.append(i) for i in lis if i not in reduceLis]
    return reduceLis


#
def getAstAssemblyReferenceLis(sceneryName):
    scnAssemblyGroupName = sceneryPr.scnAssemblyGroupName(sceneryName)
    return maUtils.getChildNodesByRoot(scnAssemblyGroupName, filterTypes=appCfg.DEF_mya_type_assembly_reference)


#
def getAstAssemblyLodDic(assemblyReferenceLis):
    dic = {}
    if assemblyReferenceLis:
        for i in assemblyReferenceLis:
            lodLevel = maAsb.getAssemblyLodLevel(i)
            dic.setdefault(lodLevel, []).append(i)
    return dic


#
def getScnAssemblyComposeDatumDic(projectName, sceneryName):
    dic = {}
    datumLis = getScnAssemblyComposeDatumLis(projectName, sceneryName)
    lis = []
    for i in datumLis:
        (
            (assetName, assetVariant),
            (arRelativePath, arNamespace, lodLevel, worldMatrix, worldBoundingBox, isVisible),
            (adFile, proxyCacheFile, gpuCacheFile, assetFile)
        ) = i
        dic.setdefault('Assembly', []).append(arRelativePath)
        if not assetName in lis:
            lis.append(assetName)
            dic.setdefault('Asset', []).append(arRelativePath)
        dic.setdefault(lodLevel, []).append(arRelativePath)
        if isVisible is True:
            dic.setdefault('Visible', []).append(arRelativePath)
    return dic


#
def getScnAssemblyComposeDatumLis(projectName, sceneryName):
    lis = []
    groupString = sceneryPr.scnAssemblyGroupName(sceneryName)
    if maUtils._isAppExist(groupString):
        stringLis = maUtils.getChildNodesByRoot(
            groupString,
            filterTypes=appCfg.DEF_mya_type_assembly_reference,
            fullPath=1
        )
        if stringLis:
            progressExplain = u'''Read Assembly Compose Unit(s)'''
            maxValue = len(stringLis)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for arPath in stringLis:
                progressBar.update()
                #
                arRelativePath = groupString + '|' + arPath.split(groupString)[-1][1:]
                arNamespace = maAsb.getAssemblyNamespace(arPath)
                adFile = maAsb.getAssemblyDefinitionFile(arPath)
                if adFile:
                    splitTexLis = adFile.replace('\\', '/').split('/')
                    assetName, assetVariant = splitTexLis[-3:-1]
                    lodLevel = maAsb.getAssemblyLodLevel(arPath)
                    worldMatrix = maUtils.getNodeWorldMatrix(arPath)
                    #
                    maUtils.setNodeWorldMatrix(
                        arPath,
                        [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
                    )
                    worldBoundingBox = maUtils.getNodeWorldBoundingBox(arPath)
                    maUtils.setNodeWorldMatrix(arPath, worldMatrix)
                    #
                    isVisible = maUtils.isLxNodeVisible(arPath)
                    if 'assembly/unit/' in adFile:
                        gpuCacheFile = assetPr.astUnitAssemblyGpuCacheFile(projectName, assetName)[1]
                        proxyCacheFile = assetPr.astUnitAssemblyProxyCacheFile(projectName, assetName, assetVariant)[1]
                        assetFile = assetPr.astUnitAssemblyProductFile(projectName, assetName, assetVariant)[1]
                    else:
                        gpuCacheFile = None
                        proxyCacheFile = None
                        assetFile = None
                    #
                    lis.append(
                        (
                            (assetName, assetVariant),
                            (arRelativePath, arNamespace, lodLevel, worldMatrix, worldBoundingBox, isVisible),
                            (adFile, proxyCacheFile, gpuCacheFile, assetFile)
                        )
                    )
    return lis


# List [ <Assemble> ]
def getAssetAssemblyReferenceLis():
    lis = []
    data = maUtils.getNodeLisByType('assemblyReference', 1)
    for i in data:
        adFile = maAsb.getAssemblyDefinitionFile(i)
        # Filter
        if adFile:
            if 'assembly/unit' in adFile:
                lis.append(i)
    return lis


#
def getActAssemblyReferenceLis():
    lis = []
    data = maUtils.getNodeLisByType('assemblyReference', 1)
    for i in data:
        adPathAttr = i + '.definition'
        adFile = cmds.getAttr(adPathAttr)
        # Filter
        if adFile:
            if '/act' in adFile:
                lis.append(i)
    return lis


#
def getSequenceSceneryArs():
    lis = []
    data = maUtils.getNodeLisByType('assemblyReference', 1)
    for i in data:
        adPathAttr = i + '.definition'
        adFile = cmds.getAttr(adPathAttr)
        # Filter
        if adFile:
            if '/scenery/seqScn' in adFile:
                lis.append(i)
    return lis


# List [ <Assemble> ]
def getAssemblyReferenceActiveDatumDic():
    def getBranch(assemblyReferenceString):
        activeItem = cmds.assembly(assemblyReferenceString, query=1, active=1)
        #
        adPathAttr = assemblyReferenceString + '.definition'
        adFile = cmds.getAttr(adPathAttr)
        splitData = adFile.split('/')
        name = splitData[-3]
        #
        data = assemblyReferenceString, name
        dic.setdefault(activeItem, []).append(data)
    #
    dic = collections.OrderedDict()
    assemblyUnits = getAssetAssemblyReferenceLis()
    for i in assemblyUnits:
        getBranch(i)
    return dic


# List [ <Assemble> ]
def getAssemblyFilterDic():
    dic = collections.OrderedDict()
    guessData = getAssetAssemblyReferenceLis()
    subData = getActAssemblyReferenceLis()
    guessData.extend(subData)
    for assemblyReferenceString in guessData:
        activeItem = cmds.assembly(assemblyReferenceString, query=1, active=1)
        #
        dic.setdefault(activeItem, []).append(assemblyReferenceString)
    return dic


#
def getSceneryInfo(printEnable=False):
    lis = []
    keyword = prsOutputs.Util.basicUnitRootGroupLabel + basicGroupLabel
    rootGroups = cmds.ls('*%s' % keyword)
    if rootGroups:
        for rootGroup in rootGroups:
            if maUtils._isAppExist(rootGroup):
                if rootGroup.startswith(prsOutputs.Util.Lynxi_Prefix_Product_scenery):
                    sceneryCategory = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicClassAttrLabel)
                    sceneryName = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicNameAttrLabel)
                    sceneryVariant = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicVariantAttrLabel)
                    sceneryStage = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicStageAttrLabel)
                    sceneryIndex = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicIndexAttrLabel)
                    if sceneryIndex is not None:
                        data = sceneryIndex, sceneryCategory, sceneryName, sceneryVariant, sceneryStage
                        if printEnable is True:
                            print '''sceneryIndex = '{}'\nsceneryCategory = '{}'\nsceneryName = '{}'\nsceneryVariant = '{}'\nsceneryStage = '{}'\n'''.format(
                                sceneryIndex,
                                sceneryCategory, sceneryName, sceneryVariant, sceneryStage
                            )
                        lis.append(data)
    return lis


# Assembly Unit Information
def getAssemblyUnitInfo(assemblyReferenceString):
    # List [ <Type>,
    #        <Name>,
    #        <Variant> ]
    tup = ()
    attr = assemblyReferenceString + '.definition'
    adFile = cmds.getAttr(attr)
    if adFile:
        if 'assembly/unit' in adFile:
            splitData = adFile.split('/')
            name = splitData[-3]
            variant = splitData[-2]
            tup = name, variant
    return tup


# Get Hierarchy ( Sub Method )
def getHierarchyData(keyword):
    data = cmds.ls(
        '*%s' % keyword,
        dag=1,
        leaf=1,
        noIntermediate=1,
        long=1)
    return data


# Get Hierarchy ( Main Method )
def getHierarchyDic(root):
    # Dict { <Parent> :
    #       List [ <Child> ] }
    dic = collections.OrderedDict()
    lis = []
    if cmds.objExists(root):
        if root:
            hierarchyData = getHierarchyData(root)
            for data in hierarchyData:
                dataR = data.split('|')
                # Check Naming Error( Overlapping Name )
                if len(dataR) == len(set(dataR)):
                    for seq, i in enumerate(dataR):
                        if seq > 1:
                            subDic = collections.OrderedDict()
                            k = dataR[seq - 1]
                            v = dataR[seq]
                            subDic[k] = v
                            lis.append(subDic)
                else:
                    [dataR.remove(i) for i in getReduceList(dataR)]
                    cmds.error('Naming Error:  %s (Overlapping Name: %s)' % (data, dataR))

    if lis:
        [dic.setdefault(ik, []).append(iv) for i in getReduceList(lis) for ik, iv in i.items()]
        return dic


#
def getAssemblyActiveVariant(assemblyReferenceString):
    attr = assemblyReferenceString + '.definition'
    adFile = cmds.getAttr(attr)
    variant = 'Non - Exists'
    # Filter
    if adFile:
        if 'assembly/unit' in adFile:
            variant = adFile.split('/')[-2]
    return variant


#
def getProxyIsOverrideAov(assemblyReferenceString):
    boolean = False
    dsoObject = getAssemblyReferenceProxyObject(assemblyReferenceString)
    attrData = maUtils.getAttrDatum(dsoObject, 'override')
    if attrData == 1:
        boolean = True
    return boolean


#
def getProxyIsPrimaryVisibility(assemblyReferenceString):
    proxyNode = getAssemblyReferenceProxyNode(assemblyReferenceString)
    return maUtils.getAttrDatum(proxyNode, 'primaryVisibility')


#
def getProxyIsCastsShadows(assemblyReferenceString):
    proxyNode = getAssemblyReferenceProxyNode(assemblyReferenceString)
    return maUtils.getAttrDatum(proxyNode, 'castsShadows')


#
def getProxyIsReceiveShadows(assemblyReferenceString):
    proxyNode = getAssemblyReferenceProxyNode(assemblyReferenceString)
    return maUtils.getAttrDatum(proxyNode, 'receiveShadows')


#
def getProxyIsLowQualityDisplay(assemblyReferenceString):
    boolean = False
    proxyObject = getAssemblyReferenceProxyObject(assemblyReferenceString)
    isUseBox = maUtils.getAttrDatum(proxyObject, 'box')
    if isUseBox:
        boolean = True
    return boolean


#
def getProxyIsHighQualityDisplay(assemblyReferenceString):
    boolean = False
    proxyObject = getAssemblyReferenceProxyObject(assemblyReferenceString)
    isUseGpu = maUtils.getAttrDatum(proxyObject, 'gpu')
    if isUseGpu:
        boolean = True
    return boolean


#
def getAssemblyReferenceProxyObject(assemblyReferenceString):
    proxyObject = none
    guessData = cmds.listRelatives(assemblyReferenceString, children=1, noIntermediate=1, fullPath=1)
    if guessData:
        for object in guessData:
            if cmds.nodeType(object) == 'transform':
                proxyObject = object
    return proxyObject


#
def getAssemblyReferenceProxyNode(assemblyReferenceString):
    proxyNode = none
    guessData = cmds.listRelatives(assemblyReferenceString, children=1, noIntermediate=1, fullPath=1)
    if guessData:
        for object in guessData:
            if cmds.nodeType(object) == 'transform':
                shapes = maUtils.getMainShapes(object)
                for shape in shapes:
                    if cmds.nodeType(shape) == 'aiStandIn' or maUtils._getNodeCategoryString(shape) == 'RedshiftProxyMesh':
                        proxyNode = shape
    return proxyNode
