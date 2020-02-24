# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscMtdCore, bscMethods, bscObjects
#
from LxPreset import prsConfigure, prsOutputs, prsMethods
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr, scenePr
#
from LxDatabase import dbGet
#
from LxMaya.command import maUtils, maGeom, maAsb, maAbc, maFur
#
from LxMaya.product.data import datAsset
#
none = ''


#
def getSceneInfo(printEnable=False):
    lis = []
    keyword = prsOutputs.Util.basicUnitRootGroupLabel + prsOutputs.Util.basicGroupLabel
    rootGroups = cmds.ls('*%s' % keyword)
    if rootGroups:
        for rootGroup in rootGroups:
            if maUtils._isAppExist(rootGroup):
                if rootGroup.startswith(prsOutputs.Util.Lynxi_Prefix_Product_scene):
                    sceneIndex = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicIndexAttrLabel)
                    sceneCategory = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicClassAttrLabel)
                    sceneName = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicNameAttrLabel)
                    sceneVariant = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicVariantAttrLabel)
                    sceneStage = maUtils.getAttrDatum(rootGroup, prsOutputs.Util.basicStageAttrLabel)
                    if sceneIndex is not None:
                        if prsMethods.Scene.isValidCategory(sceneCategory) is True:
                            data = sceneIndex, sceneCategory, sceneName, sceneVariant, sceneStage
                            #
                            if printEnable is True:
                                print '''sceneIndex = '{}'\nsceneCategory = '{}'\nsceneName = '{}'\nsceneVariant = '{}'\nsceneStage = '{}'\n'''.format(
                                    sceneIndex,
                                    sceneCategory, sceneName, sceneVariant, sceneStage
                                )
                            lis.append(data)
    return lis


#
def getSceneCustomizeLabel(sceneName):
    string = prsOutputs.Util.scDefaultCustomizeLabel
    #
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if maUtils._isAppExist(scUnitRoot):
        data = maUtils.getAttrDatum(scUnitRoot, prsOutputs.Util.basicCustomizeAttrLabel)
        if data:
            string = data
    #
    return string


#
def getSceneRootIndex(sceneName):
    intValue = prsConfigure.Utility.DEF_value_root_local
    #
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if maUtils._isAppExist(scUnitRoot):
        data = maUtils.getAttrDatum(scUnitRoot, prsOutputs.Util.basicRootIndexAttrLabel)
        if data:
            intValue = int(data)
        else:
            maUtils.setAttrStringDatumForce(scUnitRoot, prsOutputs.Util.basicRootIndexAttrLabel, str(intValue))
    #
    return intValue


#
def getScOutputCameraLis(sceneName, sceneVariant):
    lis = []
    outputCameraName = scenePr.scOutputCameraName(sceneName, sceneVariant)
    cameras = maUtils.getCameras()
    if cameras:
        for i in cameras:
            if outputCameraName in i:
                lis.append(i)
    return lis


#
def getScActiveCameraLis(sceneName):
    sceneRoot = scenePr.scUnitRootGroupName(sceneName)
    #
    cameras = []
    attrData = maUtils.getAttrDatum(sceneRoot, prsConfigure.Product.VAR_product_attribute_camera)
    if attrData:
        splitData = attrData.split(prsConfigure.Product.VAR_product_separator_camera)
        for i in splitData:
            cameras.append(i)
    #
    lis = []
    [lis.append(i) for i in cameras if i not in lis if maUtils._isAppExist(i)]
    return lis


#
def getScCameraLis(sceneName, sceneVariant, sceneStage):
    if scenePr.isLayoutLinkName(sceneStage) or scenePr.isAnimationLinkName(sceneStage):
        lis = getScActiveCameraLis(sceneName)
    else:
        lis = getScOutputCameraLis(sceneName, sceneVariant)
    return lis


# Get Camera Data
def getSceneCameraIndexData(sceneName):
    lis = []
    #
    inData = getScActiveCameraLis(sceneName)
    for seq, i in enumerate(inData):
        subLabelString = bscMethods.OsFile.seqLabel(seq)
        data = sceneName + subLabelString
        lis.append(data)
    return lis


# Get Camera Data
def getSceneAssetIndexData():
    lis = []
    #
    inData = getScAnimAssetRefDic()
    if inData:
        for k, v in inData.items():
            assetIndex, assetCategory, assetName, number, assetVariant = v
            lis.append(
                (assetIndex, assetCategory, assetName, number, assetVariant)
            )
    return lis


#
def getSceneAssetUploadData():
    lis = []
    #
    inData = getScAnimAssetRefDic()
    if inData:
        for k, v in inData.items():
            keyNode = k
            assetIndex, assetCategory, assetName, number, assetVariant = v
            lis.append(
                (assetCategory, assetName, number, assetVariant, keyNode)
            )
    return lis


#
def getSceneSounds():
    return maUtils.getNodeLisByType('audio')


#
def getScSceneryIndexLis(sceneName, sceneVariant, sceneStage):
    lis = []
    scSceneryBranchPath = scenePr.scScenerySubGroupPath(sceneName, sceneVariant, prsMethods.Scene.layoutLinkName())
    if maUtils._isAppExist(scSceneryBranchPath):
        childGroups = maUtils.getGroupLisByRoot(scSceneryBranchPath)
        for i in childGroups:
            indexAttr = i + '.' + prsOutputs.Util.basicIndexAttrLabel
            if maUtils._isAppExist(indexAttr):
                branchGroup = i
                #
                sceneryIndex = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicIndexAttrLabel)
                sceneryCategory = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicClassAttrLabel)
                sceneryName = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicNameAttrLabel)
                sceneryVariant = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicVariantAttrLabel)
                sceneryStage = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicStageAttrLabel)
                lis.append(
                    (sceneryIndex, sceneryCategory, sceneryName, sceneryVariant, sceneryStage)
                )
    return lis


#
def getScAnimAssetRefData(referenceNode):
    keywords = [prsOutputs.Util.astAnimationRigFileLabel, prsOutputs.Util.astLayoutRigFileLabel]
    #
    fileString_ = cmds.referenceQuery(referenceNode, filename=1)
    data = ()
    # Filter is Rig
    if keywords:
        for keyword in keywords:
            if keyword in fileString_:
                splitKey = keyword
                #
                fileName = bscMethods.OsFile.basename(fileString_)
                #
                assetName = fileName.split(splitKey)[0]
                namespace = maUtils.getReferenceNamespace(referenceNode)
                #
                root = prsMethods.Asset.rigLinkGroupName(assetName, namespace)
                #
                if maUtils._isAppExist(root):
                    assetIndex = maUtils.getAttrDatum(root, prsOutputs.Util.basicIndexAttrLabel)
                    if assetIndex:
                        assetCategory = assetPr.getAssetClass(assetIndex)
                        # Number
                        number = '0000'
                        attrData = maUtils.getAttrDatum(referenceNode, prsOutputs.Util.basicNumberAttrLabel)
                        if attrData:
                            number = attrData
                        # Variant
                        assetVariant = prsOutputs.Util.astDefaultVariant
                        attrData = maUtils.getAttrDatum(referenceNode, prsOutputs.Util.basicVariantAttrLabel)
                        if attrData:
                            assetVariant = attrData
                        #
                        data = assetIndex, assetCategory, assetName, number, assetVariant
    return data


# Get Dict For Rig Asset's Data
def getScAnimAssetRefDic():
    def getBranch(referenceNode):
        isLoaded = cmds.referenceQuery(referenceNode, isLoaded=1)
        if isLoaded:
            assetData = getScAnimAssetRefData(referenceNode)
            if assetData:
                dic[referenceNode] = assetData
    #
    dic = bscMtdCore.orderedDict()
    #
    referenceNodes = maUtils.getReferenceNodeLis()
    for i in referenceNodes:
        if not maUtils.isReferenceNode(i):
            try:
                getBranch(i)
            except:
                print 'Error: {} is Unused'.format(none)
    return dic


#
def getScAnimAssetCfxFurData(referenceNode):
    def getSceneName(dataArray):
        return dataArray[1]
    #
    def getSceneVariant(dataArray):
        return dataArray[2]
    #
    def getAssetName(dataArray):
        return '_'.join(dataArray[3:-2])
    #
    def getNumber(dataArray):
        return '_'.join(dataArray[-2:-1])
    data = ()
    # Filter is CFX
    if referenceNode.startswith(prsOutputs.Util.Lynxi_Prefix_Product_scene) and referenceNode.endswith(
            prsOutputs.Util.basicCfxLinkGroupLabel + 'RN'):
        namespace = maUtils.getReferenceNamespace(referenceNode)
        #
        splitData = referenceNode.split('_')
        sceneCategory = None
        sceneName = getSceneName(splitData)
        sceneVariant = getSceneVariant(splitData)
        assetName = getAssetName(splitData)
        number = getNumber(splitData)
        #
        cfxGroup = prsMethods.Asset.groomLinkGroupName(assetName, namespace)
        if maUtils._isAppExist(cfxGroup):
            assetCategory = maUtils.getAttrDatum(cfxGroup, prsOutputs.Util.basicClassAttrLabel)
            assetVariant = maUtils.getAttrDatum(cfxGroup, prsOutputs.Util.basicVariantAttrLabel)
            data = sceneCategory, sceneName, sceneVariant, assetCategory, assetName, number, assetVariant
    return data


#
def getScAstCfxFurObjects(assetName, namespace):
    lis = []
    # Yeti
    cfxYetiGroup = assetPr.yetiNodeGroupName(assetName, namespace)
    if maUtils._isAppExist(cfxYetiGroup):
        yetiObjects = maUtils.getChildObjectsByRoot(cfxYetiGroup, appCfg.MaNodeType_Plug_Yeti, fullPath=1)
        lis.extend(yetiObjects)
    # Yeti Guide System
    cfxYetiGuideSystemGroup = assetPr.guideSystemGroupName(assetName, namespace)
    if maUtils._isAppExist(cfxYetiGuideSystemGroup):
        yetiGuideSystems = maUtils.getChildObjectsByRoot(cfxYetiGuideSystemGroup, appCfg.MaHairSystemType, fullPath=1)
        lis.extend(yetiGuideSystems)
    # Pfx Hair System
    cfxPfxHairSystemGroup = assetPr.pfxSystemGroupName(assetName, namespace)
    if maUtils._isAppExist(cfxPfxHairSystemGroup):
        pfxHairSystems = maUtils.getChildObjectsByRoot(cfxPfxHairSystemGroup, appCfg.MaHairSystemType, fullPath=1)
        lis.extend(pfxHairSystems)
    # Nurbs Hair
    cfxNurbsHairGroup = assetPr.astCfxNurbsHairNodeGroupName(assetName, namespace)
    if maUtils._isAppExist(cfxNurbsHairGroup):
        nurbsHairObjects = maUtils.getChildObjectsByRoot(cfxNurbsHairGroup, appCfg.MaNodeType_Plug_NurbsHair, fullPath=1)
        lis.extend(nurbsHairObjects)
    #
    return lis


#
def getScAstCfxFurDic():
    def getBranch(referenceNode):
        assetData = getScAnimAssetCfxFurData(referenceNode)
        if assetData:
            sceneCategory, sceneName, sceneVariant, assetCategory, assetName, number, assetVariant = assetData
            cfxObjects = []
            #
            isLoaded = cmds.referenceQuery(referenceNode, isLoaded=1)
            state = 'Unloaded'
            if isLoaded:
                state = 'Loaded'
                #
                namespace = maUtils.getReferenceNamespace(referenceNode)
                cfxObjects = getScAstCfxFurObjects(assetName, namespace)
            #
            dic.setdefault((sceneCategory, sceneName, sceneVariant), []).append((referenceNode, assetCategory, assetName, number, assetVariant, state, cfxObjects))
    dic = bscMtdCore.orderedDict()
    #
    referenceNodes = maUtils.getReferenceNodeLis()
    for node in referenceNodes:
        # Ignore multilayer Reference
        if not maUtils.isReferenceNode(node):
            getBranch(node)
    return dic


#
def getScAstCfxFurDic_(projectName):
    def getBranch(value):
        (
            _, cacheSceneStage, startFrame, endFrame, scAstModelCache,
            assetIndex, assetCategory, assetName, number, assetVariant
         ) = value
        # CFX
        isCfxEnable = assetPr.getAssetIsLinkEnable(assetIndex, prsMethods.Asset.groomLinkName())
        if isCfxEnable:
            scAstCfxNamespace = scenePr.scAstCfxNamespace(
                sceneName, sceneVariant,
                assetName, number
            )
            cfxFurObjects = getScAstCfxFurObjects(assetName, scAstCfxNamespace)
            #
            assets.append((
                assetIndex, assetCategory, assetName, number, assetVariant, cfxFurObjects
            ))
    #
    dic = bscMtdCore.orderedDict()
    #
    sceneInfoLis = getSceneInfo()
    if sceneInfoLis:
        for sceneIndex, sceneCategory, sceneName, sceneVariant, sceneStage in sceneInfoLis:
            assets = []
            # Asset
            assetIndexData = scenePr.getSceneAssetIndexDataDic(
                projectName,
                sceneCategory, sceneName, sceneVariant
            )
            if assetIndexData:
                for k, v in assetIndexData.items():
                    for i in v:
                        getBranch(i)
            #
            dic[(sceneIndex, sceneCategory, sceneName, sceneVariant)] = assets
    return dic


#
def getSceneAssetUnitData(branchGroup):
    data = ()
    assetIndex = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicIndexAttrLabel)
    if assetIndex:
        assetCategory = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicClassAttrLabel)
        assetName = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicNameAttrLabel)
        number = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicNumberAttrLabel)
        assetVariant = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicVariantAttrLabel)
        timeTag = maUtils.getAttrDatum(branchGroup, prsOutputs.Util.basicTagAttrLabel)
        #
        data = assetIndex, assetCategory, assetName, number, assetVariant, timeTag
    return data


#
def getScComposeInfoDic(projectName):
    # Camera
    def getScCameraBranch(seq):
        def getScCameraCacheBranch():
            branchInfo = None
            #
            activeCacheFile = scenePr.getScCameraCacheActive(
                projectName,
                sceneName, sceneVariant,
                subLabelString
            )
            #
            isServerExists = bscMethods.OsFile.isExist(activeCacheFile)
            if isServerExists is True:
                branchInfo = False
                #
                namespace = scenePr.scCameraNamespace(
                    sceneName, sceneVariant
                ) + subLabelString
                #
                localTimeTag = None
                alembicNode = None
                if maUtils.isNamespaceExists(namespace):
                    nodeLis = maUtils.getDependNodesByNamespace(namespace)
                    if nodeLis:
                        alembicNodes = maUtils.getNodesFilterByTypes(nodeLis, [appCfg.DEF_mya_type_alembic])
                        if alembicNodes:
                            alembicNode = alembicNodes[0]
                            alembicCache = maAbc.getAlembicCacheFile(alembicNode)
                            if alembicCache:
                                if bscMethods.OsFile.isExist(alembicCache):
                                    localTimeTag = bscMethods.OsFile.findTimetag(alembicCache)
                        else:
                            localTimeTag = False
                    #
                    branchInfo = alembicNode, namespace, localTimeTag
            return branchInfo
        #
        subLabelString = bscMethods.OsFile.seqLabel(seq)
        scCameraCacheBranchInfo = getScCameraCacheBranch()
        cameraCompose.append((
            subLabelString,
            scCameraCacheBranchInfo
        ))
    # Asset
    def getScAssetBranch(value):
        # Model Product
        def getScAstModelProductBranch():
            branchInfo = None
            #
            isModelEnable = assetPr.getAssetIsLinkEnable(assetIndex, prsMethods.Asset.modelLinkName())
            if isModelEnable is True:
                branchInfo = False
                #
                scAstModelNamespace = scenePr.scAstModelNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                scAstModelGroup = prsMethods.Asset.modelLinkGroupName(assetName, scAstModelNamespace)
                if maUtils._isAppExist(scAstModelGroup):
                    if not maUtils.isReferenceNode(scAstModelGroup):
                        scAstModelLocalTimeTag = maUtils.getAttrDatum(scAstModelGroup, prsOutputs.Util.basicTagAttrLabel)
                    else:
                        scAstModelLocalTimeTag = assetPr.getAstUnitProductActiveTimeTag(
                            projectName,
                            assetCategory, assetName, assetVariant, prsMethods.Asset.modelLinkName()
                        )
                    #
                    branchInfo = scAstModelGroup, scAstModelNamespace, scAstModelLocalTimeTag
            return branchInfo
        # Model Cache
        def getScAstModelCacheBranch():
            branchInfo = None
            #
            scAstModelCacheFile = scenePr.getScAstModelCacheActive(
                projectName,
                sceneName, sceneVariant, assetName, number
            )
            isServerExists = bscMethods.OsFile.isExist(scAstModelCacheFile)
            if isServerExists:
                branchInfo = False
                #
                namespace = scenePr.scAstModelCacheNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                #
                localTimeTag = None
                alembicNode = None
                if maUtils.isNamespaceExists(namespace):
                    nodeLis = maUtils.getDependNodesByNamespace(namespace)
                    if nodeLis:
                        alembicNodeLis = maUtils.getNodesFilterByTypes(nodeLis, [appCfg.DEF_mya_type_alembic])
                        if alembicNodeLis:
                            alembicNode = alembicNodeLis[0]
                            alembicCache = maAbc.getAlembicCacheFile(alembicNode)
                            if alembicCache:
                                if bscMethods.OsFile.isExist(alembicCache):
                                    localTimeTag = bscMethods.OsFile.findTimetag(alembicCache)
                        else:
                            localTimeTag = False
                    else:
                        localTimeTag = False
                    #
                    branchInfo = alembicNode, namespace, localTimeTag
            return branchInfo
        # Extra Cache
        def getScAstExtraCacheBranch():
            branchInfo = None
            #
            activeCacheFile = scenePr.getScAstRigExtraCacheActive(
                projectName,
                sceneName, sceneVariant,
                assetName, number
            )
            #
            isServerExists = bscMethods.OsFile.isExist(activeCacheFile)
            if isServerExists:
                branchInfo = False
                #
                namespace = scenePr.scAstExtraNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                localTimeTag = None
                alembicNode = None
                if maUtils.isNamespaceExists(namespace):
                    nodeLis = maUtils.getDependNodesByNamespace(namespace)
                    if nodeLis:
                        alembicNodeLis = maUtils.getNodesFilterByTypes(nodeLis, [appCfg.DEF_mya_type_alembic])
                        if alembicNodeLis:
                            alembicNode = alembicNodeLis[0]
                            alembicCache = maAbc.getAlembicCacheFile(alembicNode)
                            if alembicCache:
                                if bscMethods.OsFile.isExist(alembicCache):
                                    localTimeTag = bscMethods.OsFile.findTimetag(alembicCache)
                        else:
                            localTimeTag = False
                    #
                    branchInfo = alembicNode, namespace, localTimeTag
            return branchInfo
        # CFX Product
        def getScAstCfxProductBranch():
            branchInfo = None
            isCfxEnable = assetPr.getAssetIsLinkEnable(assetIndex, prsMethods.Asset.groomLinkName())
            if isCfxEnable is True:
                branchInfo = False
                #
                scAstCfxNamespace = scenePr.scAstCfxNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                scAstCfxGroup = prsMethods.Asset.groomLinkGroupName(assetName, scAstCfxNamespace)
                if maUtils._isAppExist(scAstCfxGroup):
                    if not maUtils.isReferenceNode(scAstCfxGroup):
                        scAstCfxLocalTimeTag = maUtils.getAttrDatum(scAstCfxGroup, prsOutputs.Util.basicTagAttrLabel)
                    else:
                        scAstCfxLocalTimeTag = assetPr.getAstUnitProductActiveTimeTag(
                            projectName,
                            assetCategory, assetName, assetVariant, prsMethods.Asset.groomLinkName()
                        )
                    #
                    branchInfo = scAstCfxGroup, scAstCfxNamespace, scAstCfxLocalTimeTag
            #
            return branchInfo
        # CFX Fur Cache(s)
        def getScAstCfxCacheBranch():
            branchInfoLis = []
            isCfxEnable = assetPr.getAssetIsLinkEnable(assetIndex, prsMethods.Asset.groomLinkName())
            if isCfxEnable is True:
                namespace = scenePr.scAstCfxNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                linkGroup = prsMethods.Asset.groomLinkGroupName(assetName, namespace)
                if maUtils._isAppExist(linkGroup):
                    furObjectLis = getScAstCfxFurObjects(assetName, namespace)
                    if furObjectLis:
                        for furObject in furObjectLis:
                            localFurCacheFile, localSolverMode, localCacheStartFrame, localCacheEndFrame = maFur.getFurCacheExists(furObject)
                            #
                            localTimeTag = bscMethods.OsFile.findTimetag(localFurCacheFile)
                            #
                            furObjectLabel = maFur.getFurObjectLabel(furObject, assetName)
                            branchInfoLis.append(
                                (furObjectLabel, (furObject, namespace, localTimeTag))
                            )
            #
            return branchInfoLis
        # Solver Product
        def getScAstSolverProductBranch():
            branchInfo = None
            #
            isSolverEnable = assetPr.getAssetIsLinkEnable(assetIndex, prsMethods.Asset.solverLinkName())
            if isSolverEnable is True:
                branchInfo = False
                #
                scAstSolverNamespace = scenePr.scAstSolverNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                scAstSolverGroup = prsMethods.Asset.solverLinkGroupName(assetName, scAstSolverNamespace)
                if maUtils._isAppExist(scAstSolverGroup):
                    if not maUtils.isReferenceNode(scAstSolverGroup):
                        scAstSolverLocalTimeTag = maUtils.getAttrDatum(scAstSolverGroup, prsOutputs.Util.basicTagAttrLabel)
                    else:
                        scAstSolverLocalTimeTag = assetPr.getAstUnitProductActiveTimeTag(
                            projectName,
                            assetCategory, assetName, assetVariant, prsMethods.Asset.solverLinkName()
                        )
                    #
                    branchInfo = scAstSolverGroup, scAstSolverNamespace, scAstSolverLocalTimeTag
            #
            return branchInfo
        # Solver Cache
        def getScAstSolverCacheBranch():
            branchInfo = None
            #
            scAstSolverCacheFile = scenePr.getScAstSolverCacheActive(
                projectName,
                sceneName, sceneVariant, assetName, number
            )
            isScAstSolverCacheEnable = bscMethods.OsFile.isExist(scAstSolverCacheFile)
            #
            if isScAstSolverCacheEnable:
                branchInfo = False

                #
                namespace = scenePr.scAstSolverCacheNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                localTimeTag = None
                alembicNode = None
                if maUtils.isNamespaceExists(namespace):
                    nodeLis = maUtils.getDependNodesByNamespace(namespace)
                    if nodeLis:
                        alembicNodeLis = maUtils.getNodesFilterByTypes(nodeLis, [appCfg.DEF_mya_type_alembic])
                        if alembicNodeLis:
                            alembicNode = alembicNodeLis[0]
                            alembicCache = maAbc.getAlembicCacheFile(alembicNode)
                            if alembicCache:
                                if bscMethods.OsFile.isExist(alembicCache):
                                    localTimeTag = bscMethods.OsFile.findTimetag(alembicCache)
                    #
                    branchInfo = alembicNode, namespace, localTimeTag
            return branchInfo
        (
            timestamp,
            cacheSceneStage,
            startFrame, endFrame,
            scAstModelCache,
            assetIndex,
            assetCategory, assetName, number, assetVariant
        ) = value
        # Model Product
        scAstModelProductBranchInfo = getScAstModelProductBranch()
        # Model Cache
        scAstModelCacheBranchInfo = getScAstModelCacheBranch()
        # Extra Cache
        scAstExtraCacheBranchInfo = getScAstExtraCacheBranch()
        # CFX Product
        scAstCfxProductBranchInfo = getScAstCfxProductBranch()
        scAstCfxCacheBranchInfoLis = getScAstCfxCacheBranch()
        # Solver Product
        scAstSolverProductBranchInfo = getScAstSolverProductBranch()
        # Solver Cache
        scAstSolverCacheBranchInfo = getScAstSolverCacheBranch()
        #
        assetCompose.append((
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            scAstModelProductBranchInfo, scAstModelCacheBranchInfo,
            scAstCfxProductBranchInfo, scAstCfxCacheBranchInfoLis,
            scAstSolverProductBranchInfo, scAstSolverCacheBranchInfo,
            scAstExtraCacheBranchInfo
        ))
    #
    dic = bscMtdCore.orderedDict()
    #
    sceneInfoLis = getSceneInfo()
    if sceneInfoLis:
        for sceneIndex, sceneCategory, sceneName, sceneVariant, sceneStage in sceneInfoLis:
            cameraCompose = []
            assetCompose = []
            # Camera
            cameraIndexData = scenePr.getSceneCameraIndexDataDic(
                projectName, sceneCategory, sceneName, sceneVariant
            )
            if cameraIndexData:
                for k, v in cameraIndexData.items():
                    for camSeq, i in enumerate(v):
                        getScCameraBranch(camSeq)
            # Asset
            assetIndexData = scenePr.getSceneAssetIndexDataDic(
                projectName, sceneCategory, sceneName, sceneVariant
            )
            if assetIndexData:
                for k, v in assetIndexData.items():
                    for i in v:
                        getScAssetBranch(i)
            #
            dic[(sceneIndex, sceneCategory, sceneName, sceneVariant)] = cameraCompose, assetCompose
    #
    return dic


#
def getScAstUnitDic(projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    def getBranch(args):
        (
            timestamp,
            cacheStage,
            startFrame, endFrame,
            cache,
            assetIndex,
            assetCategory, assetName, number, assetVariant
         ) = args
        #
        sceneAssetUnitGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        if maUtils._isAppExist(sceneAssetUnitGroup):
            maUtils.setObjectParent(sceneAssetUnitGroup, scLinkAssetGroup)
            if scenePr.isSolverLinkName(sceneStage) or scenePr.isLightLinkName(sceneStage):
                scAstModelNamespace = scenePr.scAstModelNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                key = prsMethods.Asset.modelLinkGroupName(assetName, scAstModelNamespace)
            else:
                key = sceneAssetUnitGroup
            #
            print '''assetIndex = '{}'\nassetCategory = '{}'\nassetName = '{}'\nassetVariant = '{}'\nnumber = '{}'\n'''.format(
                assetIndex,
                assetCategory, assetName, assetVariant, number
            )
            dic[key] = assetIndex, assetCategory, assetName, number, assetVariant
    #
    dic = bscMtdCore.orderedDict()
    #
    sceneAssetData = scenePr.getSceneAssetIndexDataDic(
        projectName, sceneCategory, sceneName, sceneVariant
    )
    scLinkAssetGroup = scenePr.scAssetSubGroupPath(sceneName, sceneVariant, sceneStage)
    if sceneAssetData:
        for k, v in sceneAssetData.items():
            for i in v:
                getBranch(i)
    #
    return dic


#
def getScAstModelMeshConstantData(
        sceneName, sceneVariant, sceneStage,
        assetIndex,
        assetCategory, assetName, number,
        namespace):
    totalArray = []
    pathChangedArray = []
    geomChangedArray = []
    geomShapeChangedArray = []
    mapChangedArray = []
    mapShapeChangedArray = []
    #
    meshRoot = None
    #
    if scenePr.isLayoutLinkName(sceneStage) or scenePr.isAnimationLinkName(sceneStage):
        meshRoot = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
    elif scenePr.isSimulationLinkName(sceneStage):
        meshRoot = scenePr.scAstModelGroupName(sceneName, sceneVariant, assetName, number, namespace)
    elif scenePr.isSolverLinkName(sceneStage) or scenePr.isLightLinkName(sceneStage):
        meshRoot = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
    #
    if meshRoot:
        astModelGroup = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
        searchRoot = assetPr.astUnitModelProductGroupName(assetName)
        #
        localInfoDic = maGeom.getScGeometryObjectsInfoDic_(meshRoot, astModelGroup, searchRoot)
        serverInfoDic = dbGet.getDbGeometryObjectsInfoDic(assetIndex, assetName, namespace, searchRoot)
        #
        if localInfoDic and serverInfoDic:
            unionInfoDic = localInfoDic.copy()
            unionInfoDic.update(serverInfoDic)
            # View Progress
            explain = '''Read Asset ( Mesh ) Data'''
            maxValue = len(unionInfoDic)
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for meshKey in unionInfoDic:
                progressBar.update()
                #
                totalArray.append(meshKey)
                pathCheck, geomCheck, geomShapeCheck, mapCheck, mapShapeCheck = datAsset.getMeshConstant(
                    meshKey,
                    localInfoDic,
                    serverInfoDic
                )
                if not pathCheck:
                    pathChangedArray.append(meshKey)
                if not geomCheck:
                    geomChangedArray.append(meshKey)
                if not geomShapeCheck:
                    geomShapeChangedArray.append(meshKey)
                if not mapCheck:
                    mapChangedArray.append(meshKey)
                if not mapShapeCheck:
                    mapShapeChangedArray.append(meshKey)
    #
    return totalArray, pathChangedArray, geomChangedArray, geomShapeChangedArray, mapChangedArray, mapShapeChangedArray


#
def getScAstRigAlembicAttrData(projectName, assetCategory, assetName, assetVariant):
    lis = []
    rigExtraData = assetPr.getAssetUnitExtraData(
        projectName,
        assetCategory, assetName, assetVariant, prsMethods.Asset.rigLinkName()
    )
    if rigExtraData:
        if prsConfigure.Product.DEF_key_info_abcattribute in rigExtraData:
            data = rigExtraData[prsConfigure.Product.DEF_key_info_abcattribute]
            if data:
                lis = data
    return lis


#
def getScSceneryExtraData(sceneName, sceneVariant, sceneStage):
    dic = bscMtdCore.orderedDict()
    assemblyReferenceData, transformationData = getScScenery(sceneName, sceneVariant, sceneStage)
    dic[prsConfigure.Product.DEF_key_info_asbreference] = assemblyReferenceData
    dic[prsConfigure.Product.DEF_key_info_transformation] = transformationData
    return dic


#
def getScAssemblyComposeDatumLis(sceneName, sceneVariant, sceneStage):
    lis = []
    rootPath = scenePr.scScenerySubGroupPath(sceneName, sceneVariant, prsMethods.Scene.layoutLinkName())
    if maUtils._isAppExist(rootPath):
        stringLis = maUtils.getChildNodesByRoot(rootPath, filterTypes=appCfg.DEF_mya_type_assembly_reference)
        if stringLis:
            progressExplain = u'''Read Assembly Compose Unit(s)'''
            maxValue = len(stringLis)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for assemblyPath in stringLis:
                progressBar.update()
                datum = getScnAssemblyComposeDatumSub(assemblyPath, rootPath)
                if datum:
                    lis.append(datum)
    #
    return lis


#
def getScnAssemblyComposeDatumSub(assemblyPath, groupString):
    relativePath = assemblyPath.split(groupString)[-1][1:]
    arNamespace = maAsb.getAssemblyNamespace(assemblyPath)
    adFile = maAsb.getAssemblyDefinitionFile(assemblyPath)
    if adFile:
        splitTexLis = adFile.replace('\\', '/').split('/')
        projectName = splitTexLis[-6]
        assetName, assetVariant = splitTexLis[-3:-1]
        #
        worldMatrix = maUtils.getNodeWorldMatrix(assemblyPath)
        #
        maUtils.setNodeWorldMatrix(
            assemblyPath,
            [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        )
        worldBoundingBox = maUtils.getNodeWorldBoundingBox(assemblyPath)
        maUtils.setNodeWorldMatrix(assemblyPath, worldMatrix)
        #
        isVisible = maUtils.isLxNodeVisible(assemblyPath)
        if 'assembly/unit/' in adFile.lower():
            lodLevel = maAsb.getAssemblyLodLevel(assemblyPath)
            #
            gpuCacheFile = assetPr.astUnitAssemblyGpuCacheFile(projectName, assetName)[1]
            proxyCacheFile = assetPr.astUnitAssemblyProxyCacheFile(projectName, assetName, assetVariant)[1]
            assetFile = assetPr.astUnitAssemblyProductFile(projectName, assetName, assetVariant)[1]
            return (
                (assetName, assetVariant),
                (relativePath, arNamespace, lodLevel, worldMatrix, worldBoundingBox, isVisible),
                (adFile, proxyCacheFile, gpuCacheFile, assetFile)
            )


#
def getScScenery(sceneName, sceneVariant, sceneStage):
    lis1 = []
    lis2 = []
    scSceneryBranchPath = scenePr.scScenerySubGroupPath(sceneName, sceneVariant, prsMethods.Scene.layoutLinkName())
    if maUtils._isAppExist(scSceneryBranchPath):
        objectPathLis = maUtils.getObjectChildObjectLis(scSceneryBranchPath, 'assemblyReference')
        if objectPathLis:
            for objectPath in objectPathLis:
                relativePath = objectPath.split(scSceneryBranchPath)[-1]
                assemblyDefinitionFile = maAsb.getAssemblyDefinitionFile(objectPath)
                namespace = maAsb.getAssemblyNamespace(objectPath)
                lis1.append((relativePath, assemblyDefinitionFile, namespace))
                #
                transformation = maAsb.getAssemblyReferencesTransformationByRoot(objectPath)
                lis2.append(transformation)
    return lis1, lis2


#
def getGeometryMeshes(sceneName, sceneVariant, assetName, number, namespace):
    lis = []
    if namespace:
        astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    else:
        astUnitModelProductGroup = scenePr.scAstGeometryGroupName(sceneName, sceneVariant, assetName, number)
    if maUtils._isAppExist(astUnitModelProductGroup):
        lis = maGeom.getMeshObjectsByGroup(astUnitModelProductGroup)
    return lis


#
def getMeshObjectsConstantDic(astUnitModelProductGroup):
    infoConfig = ['hierarchy', 'geometry', 'geometryShape', 'map', 'mapShape']
    dic = bscMtdCore.orderedDict()
    meshesInformation = maGeom.getGeometryObjectsInfo(astUnitModelProductGroup)
    for seq, i in enumerate(infoConfig):
        dic[i] = meshesInformation[seq]
    return dic


#
def getMeshConstantDataByRoot(sceneName, sceneVariant, assetName, number, namespace=none):
    # Dict { <Constant Item>: <Constant Value> }
    dic = bscMtdCore.orderedDict()
    geometries = []
    if namespace:
        scAstGeometryGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    else:
        scAstGeometryGroup = scenePr.scAstGeometryGroupName(sceneName, sceneVariant, assetName, number)
    if maUtils._isAppExist(scAstGeometryGroup):
        geometries = maGeom.getMeshObjectsByGroup(scAstGeometryGroup)
    #
    if geometries:
        dic = datAsset.getMeshObjectsEvaluateDic(geometries)
        subData = getMeshObjectsConstantDic(scAstGeometryGroup)
        for k, v in subData.items():
            dic[k] = v
    return dic
