# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore import lxBasic, lxConfigure
from LxUi.qt import qtProgress
#
from LxCore.config import appCfg, sceneCfg
#
from LxCore.preset import appVariant
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
    keyword = appVariant.basicUnitRootGroupLabel + appVariant.basicGroupLabel
    rootGroups = cmds.ls('*%s' % keyword)
    if rootGroups:
        for rootGroup in rootGroups:
            if maUtils.isAppExist(rootGroup):
                if rootGroup.startswith(appVariant.Lynxi_Prefix_Product_Scene):
                    sceneIndex = maUtils.getAttrDatum(rootGroup, appVariant.basicIndexAttrLabel)
                    sceneClass = maUtils.getAttrDatum(rootGroup, appVariant.basicClassAttrLabel)
                    sceneName = maUtils.getAttrDatum(rootGroup, appVariant.basicNameAttrLabel)
                    sceneVariant = maUtils.getAttrDatum(rootGroup, appVariant.basicVariantAttrLabel)
                    sceneStage = maUtils.getAttrDatum(rootGroup, appVariant.basicStageAttrLabel)
                    if sceneIndex is not None:
                        if sceneClass in sceneCfg.scBasicClass()[1:]:
                            data = sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage
                            #
                            if printEnable is True:
                                print '''sceneIndex = '{}'\nsceneClass = '{}'\nsceneName = '{}'\nsceneVariant = '{}'\nsceneStage = '{}'\n'''.format(
                                    sceneIndex,
                                    sceneClass, sceneName, sceneVariant, sceneStage
                                )
                            lis.append(data)
    return lis


#
def getSceneCustomizeLabel(sceneName):
    string = appVariant.scDefaultCustomizeLabel
    #
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if maUtils.isAppExist(scUnitRoot):
        data = maUtils.getAttrDatum(scUnitRoot, appVariant.basicCustomizeAttrLabel)
        if data:
            string = data
    #
    return string


#
def getSceneRootIndex(sceneName):
    intValue = lxConfigure.LynxiRootIndex_Local
    #
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if maUtils.isAppExist(scUnitRoot):
        data = maUtils.getAttrDatum(scUnitRoot, appVariant.basicRootIndexAttrLabel)
        if data:
            intValue = int(data)
        else:
            maUtils.setAttrStringDatumForce(scUnitRoot, appVariant.basicRootIndexAttrLabel, str(intValue))
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
    attrData = maUtils.getAttrDatum(sceneRoot, sceneCfg.SceneCameraAttr)
    if attrData:
        splitData = attrData.split(sceneCfg.CameraSep)
        for i in splitData:
            cameras.append(i)
    #
    lis = []
    [lis.append(i) for i in cameras if i not in lis if maUtils.isAppExist(i)]
    return lis


#
def getScCameraLis(sceneName, sceneVariant, sceneStage):
    if scenePr.isScLayoutLink(sceneStage) or scenePr.isScAnimationLink(sceneStage):
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
        subLabel = lxBasic.getSubLabel(seq)
        data = sceneName + subLabel
        lis.append(data)
    return lis


# Get Camera Data
def getSceneAssetIndexData():
    lis = []
    #
    inData = getScAnimAssetRefDic()
    if inData:
        for k, v in inData.items():
            assetIndex, assetClass, assetName, number, assetVariant = v
            lis.append(
                (assetIndex, assetClass, assetName, number, assetVariant)
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
            assetIndex, assetClass, assetName, number, assetVariant = v
            lis.append(
                (assetClass, assetName, number, assetVariant, keyNode)
            )
    return lis


#
def getSceneSounds():
    return maUtils.getNodeLisByType('audio')


#
def getScSceneryIndexLis(sceneName, sceneVariant, sceneStage):
    lis = []
    scSceneryBranchPath = scenePr.scScenerySubGroupPath(sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_layout)
    if maUtils.isAppExist(scSceneryBranchPath):
        childGroups = maUtils.getGroupLisByRoot(scSceneryBranchPath)
        for i in childGroups:
            indexAttr = i + '.' + appVariant.basicIndexAttrLabel
            if maUtils.isAppExist(indexAttr):
                branchGroup = i
                #
                sceneryIndex = maUtils.getAttrDatum(branchGroup, appVariant.basicIndexAttrLabel)
                sceneryClass = maUtils.getAttrDatum(branchGroup, appVariant.basicClassAttrLabel)
                sceneryName = maUtils.getAttrDatum(branchGroup, appVariant.basicNameAttrLabel)
                sceneryVariant = maUtils.getAttrDatum(branchGroup, appVariant.basicVariantAttrLabel)
                sceneryStage = maUtils.getAttrDatum(branchGroup, appVariant.basicStageAttrLabel)
                lis.append(
                    (sceneryIndex, sceneryClass, sceneryName, sceneryVariant, sceneryStage)
                )
    return lis


#
def getScAnimAssetRefData(referenceNode):
    keywords = [appVariant.astAnimationRigFileLabel, appVariant.astLayoutRigFileLabel]
    #
    osFile = cmds.referenceQuery(referenceNode, filename=1)
    data = ()
    # Filter is Rig
    if keywords:
        for keyword in keywords:
            if keyword in osFile:
                splitKey = keyword
                #
                fileName = lxBasic.getOsFileBasename(osFile)
                #
                assetName = fileName.split(splitKey)[0]
                namespace = maUtils.getReferenceNamespace(referenceNode)
                #
                root = assetPr.astUnitRigLinkGroupName(assetName, namespace)
                #
                if maUtils.isAppExist(root):
                    assetIndex = maUtils.getAttrDatum(root, appVariant.basicIndexAttrLabel)
                    if assetIndex:
                        assetClass = assetPr.getAssetClass(assetIndex)
                        # Number
                        number = '0000'
                        attrData = maUtils.getAttrDatum(referenceNode, appVariant.basicNumberAttrLabel)
                        if attrData:
                            number = attrData
                        # Variant
                        assetVariant = appVariant.astDefaultVariant
                        attrData = maUtils.getAttrDatum(referenceNode, appVariant.basicVariantAttrLabel)
                        if attrData:
                            assetVariant = attrData
                        #
                        data = assetIndex, assetClass, assetName, number, assetVariant
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
    dic = lxBasic.orderedDict()
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
    if referenceNode.startswith(appVariant.Lynxi_Prefix_Product_Scene) and referenceNode.endswith(
            appVariant.basicCfxLinkGroupLabel + 'RN'):
        namespace = maUtils.getReferenceNamespace(referenceNode)
        #
        splitData = referenceNode.split('_')
        sceneClass = None
        sceneName = getSceneName(splitData)
        sceneVariant = getSceneVariant(splitData)
        assetName = getAssetName(splitData)
        number = getNumber(splitData)
        #
        cfxGroup = assetPr.astUnitCfxLinkGroupName(assetName, namespace)
        if maUtils.isAppExist(cfxGroup):
            assetClass = maUtils.getAttrDatum(cfxGroup, appVariant.basicClassAttrLabel)
            assetVariant = maUtils.getAttrDatum(cfxGroup, appVariant.basicVariantAttrLabel)
            data = sceneClass, sceneName, sceneVariant, assetClass, assetName, number, assetVariant
    return data


#
def getScAstCfxFurObjects(assetName, namespace):
    lis = []
    # Yeti
    cfxYetiGroup = assetPr.yetiNodeGroupName(assetName, namespace)
    if maUtils.isAppExist(cfxYetiGroup):
        yetiObjects = maUtils.getChildObjectsByRoot(cfxYetiGroup, appCfg.MaNodeType_Plug_Yeti, fullPath=1)
        lis.extend(yetiObjects)
    # Yeti Guide System
    cfxYetiGuideSystemGroup = assetPr.guideSystemGroupName(assetName, namespace)
    if maUtils.isAppExist(cfxYetiGuideSystemGroup):
        yetiGuideSystems = maUtils.getChildObjectsByRoot(cfxYetiGuideSystemGroup, appCfg.MaHairSystemType, fullPath=1)
        lis.extend(yetiGuideSystems)
    # Pfx Hair System
    cfxPfxHairSystemGroup = assetPr.pfxSystemGroupName(assetName, namespace)
    if maUtils.isAppExist(cfxPfxHairSystemGroup):
        pfxHairSystems = maUtils.getChildObjectsByRoot(cfxPfxHairSystemGroup, appCfg.MaHairSystemType, fullPath=1)
        lis.extend(pfxHairSystems)
    # Nurbs Hair
    cfxNurbsHairGroup = assetPr.astCfxNurbsHairNodeGroupName(assetName, namespace)
    if maUtils.isAppExist(cfxNurbsHairGroup):
        nurbsHairObjects = maUtils.getChildObjectsByRoot(cfxNurbsHairGroup, appCfg.MaNodeType_Plug_NurbsHair, fullPath=1)
        lis.extend(nurbsHairObjects)
    #
    return lis


#
def getScAstCfxFurDic():
    def getBranch(referenceNode):
        assetData = getScAnimAssetCfxFurData(referenceNode)
        if assetData:
            sceneClass, sceneName, sceneVariant, assetClass, assetName, number, assetVariant = assetData
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
            dic.setdefault((sceneClass, sceneName, sceneVariant), []).append((referenceNode, assetClass, assetName, number, assetVariant, state, cfxObjects))
    dic = lxBasic.orderedDict()
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
            assetIndex, assetClass, assetName, number, assetVariant
         ) = value
        # CFX
        isCfxEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Cfx)
        if isCfxEnable:
            scAstCfxNamespace = scenePr.scAstCfxNamespace(
                sceneName, sceneVariant,
                assetName, number
            )
            cfxFurObjects = getScAstCfxFurObjects(assetName, scAstCfxNamespace)
            #
            assets.append((
                assetIndex, assetClass, assetName, number, assetVariant, cfxFurObjects
            ))
    #
    dic = lxBasic.orderedDict()
    #
    sceneInfoLis = getSceneInfo()
    if sceneInfoLis:
        for sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage in sceneInfoLis:
            assets = []
            # Asset
            assetIndexData = scenePr.getSceneAssetIndexDataDic(
                projectName,
                sceneClass, sceneName, sceneVariant
            )
            if assetIndexData:
                for k, v in assetIndexData.items():
                    for i in v:
                        getBranch(i)
            #
            dic[(sceneIndex, sceneClass, sceneName, sceneVariant)] = assets
    return dic


#
def getSceneAssetUnitData(branchGroup):
    data = ()
    assetIndex = maUtils.getAttrDatum(branchGroup, appVariant.basicIndexAttrLabel)
    if assetIndex:
        assetClass = maUtils.getAttrDatum(branchGroup, appVariant.basicClassAttrLabel)
        assetName = maUtils.getAttrDatum(branchGroup, appVariant.basicNameAttrLabel)
        number = maUtils.getAttrDatum(branchGroup, appVariant.basicNumberAttrLabel)
        assetVariant = maUtils.getAttrDatum(branchGroup, appVariant.basicVariantAttrLabel)
        timeTag = maUtils.getAttrDatum(branchGroup, appVariant.basicTagAttrLabel)
        #
        data = assetIndex, assetClass, assetName, number, assetVariant, timeTag
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
                subLabel
            )
            #
            isServerExists = lxBasic.isOsExistsFile(activeCacheFile)
            if isServerExists is True:
                branchInfo = False
                #
                namespace = scenePr.scCameraNamespace(
                    sceneName, sceneVariant
                ) + subLabel
                #
                localTimeTag = None
                alembicNode = None
                if maUtils.isNamespaceExists(namespace):
                    nodeLis = maUtils.getDependNodesByNamespace(namespace)
                    if nodeLis:
                        alembicNodes = maUtils.getNodesFilterByTypes(nodeLis, [appCfg.MaNodeType_Alembic])
                        if alembicNodes:
                            alembicNode = alembicNodes[0]
                            alembicCache = maAbc.getAlembicCacheFile(alembicNode)
                            if alembicCache:
                                if lxBasic.isOsExistsFile(alembicCache):
                                    localTimeTag = lxBasic.getOsFileTimeTag(alembicCache)
                        else:
                            localTimeTag = False
                    #
                    branchInfo = alembicNode, namespace, localTimeTag
            return branchInfo
        #
        subLabel = lxBasic.getSubLabel(seq)
        scCameraCacheBranchInfo = getScCameraCacheBranch()
        cameraCompose.append((
            subLabel,
            scCameraCacheBranchInfo
        ))
    # Asset
    def getScAssetBranch(value):
        # Model Product
        def getScAstModelProductBranch():
            branchInfo = None
            #
            isModelEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Model)
            if isModelEnable is True:
                branchInfo = False
                #
                scAstModelNamespace = scenePr.scAstModelNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                scAstModelGroup = assetPr.astUnitModelLinkGroupName(assetName, scAstModelNamespace)
                if maUtils.isAppExist(scAstModelGroup):
                    if not maUtils.isReferenceNode(scAstModelGroup):
                        scAstModelLocalTimeTag = maUtils.getAttrDatum(scAstModelGroup, appVariant.basicTagAttrLabel)
                    else:
                        scAstModelLocalTimeTag = assetPr.getAstUnitProductActiveTimeTag(
                            projectName,
                            assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Model
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
            isServerExists = lxBasic.isOsExistsFile(scAstModelCacheFile)
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
                        alembicNodeLis = maUtils.getNodesFilterByTypes(nodeLis, [appCfg.MaNodeType_Alembic])
                        if alembicNodeLis:
                            alembicNode = alembicNodeLis[0]
                            alembicCache = maAbc.getAlembicCacheFile(alembicNode)
                            if alembicCache:
                                if lxBasic.isOsExistsFile(alembicCache):
                                    localTimeTag = lxBasic.getOsFileTimeTag(alembicCache)
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
            isServerExists = lxBasic.isOsExistsFile(activeCacheFile)
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
                        alembicNodeLis = maUtils.getNodesFilterByTypes(nodeLis, [appCfg.MaNodeType_Alembic])
                        if alembicNodeLis:
                            alembicNode = alembicNodeLis[0]
                            alembicCache = maAbc.getAlembicCacheFile(alembicNode)
                            if alembicCache:
                                if lxBasic.isOsExistsFile(alembicCache):
                                    localTimeTag = lxBasic.getOsFileTimeTag(alembicCache)
                        else:
                            localTimeTag = False
                    #
                    branchInfo = alembicNode, namespace, localTimeTag
            return branchInfo
        # CFX Product
        def getScAstCfxProductBranch():
            branchInfo = None
            isCfxEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Cfx)
            if isCfxEnable is True:
                branchInfo = False
                #
                scAstCfxNamespace = scenePr.scAstCfxNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                scAstCfxGroup = assetPr.astUnitCfxLinkGroupName(assetName, scAstCfxNamespace)
                if maUtils.isAppExist(scAstCfxGroup):
                    if not maUtils.isReferenceNode(scAstCfxGroup):
                        scAstCfxLocalTimeTag = maUtils.getAttrDatum(scAstCfxGroup, appVariant.basicTagAttrLabel)
                    else:
                        scAstCfxLocalTimeTag = assetPr.getAstUnitProductActiveTimeTag(
                            projectName,
                            assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Cfx
                        )
                    #
                    branchInfo = scAstCfxGroup, scAstCfxNamespace, scAstCfxLocalTimeTag
            #
            return branchInfo
        # CFX Fur Cache(s)
        def getScAstCfxCacheBranch():
            branchInfoLis = []
            isCfxEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Cfx)
            if isCfxEnable is True:
                namespace = scenePr.scAstCfxNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                linkGroup = assetPr.astUnitCfxLinkGroupName(assetName, namespace)
                if maUtils.isAppExist(linkGroup):
                    furObjectLis = getScAstCfxFurObjects(assetName, namespace)
                    if furObjectLis:
                        for furObject in furObjectLis:
                            localFurCacheFile, localSolverMode, localCacheStartFrame, localCacheEndFrame = maFur.getFurCacheExists(furObject)
                            #
                            localTimeTag = lxBasic.getOsFileTimeTag(localFurCacheFile)
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
            isSolverEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Solver)
            if isSolverEnable is True:
                branchInfo = False
                #
                scAstSolverNamespace = scenePr.scAstSolverNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                scAstSolverGroup = assetPr.astUnitSolverLinkGroupName(assetName, scAstSolverNamespace)
                if maUtils.isAppExist(scAstSolverGroup):
                    if not maUtils.isReferenceNode(scAstSolverGroup):
                        scAstSolverLocalTimeTag = maUtils.getAttrDatum(scAstSolverGroup, appVariant.basicTagAttrLabel)
                    else:
                        scAstSolverLocalTimeTag = assetPr.getAstUnitProductActiveTimeTag(
                            projectName,
                            assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Solver
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
            isScAstSolverCacheEnable = lxBasic.isOsExist(scAstSolverCacheFile)
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
                        alembicNodeLis = maUtils.getNodesFilterByTypes(nodeLis, [appCfg.MaNodeType_Alembic])
                        if alembicNodeLis:
                            alembicNode = alembicNodeLis[0]
                            alembicCache = maAbc.getAlembicCacheFile(alembicNode)
                            if alembicCache:
                                if lxBasic.isOsExistsFile(alembicCache):
                                    localTimeTag = lxBasic.getOsFileTimeTag(alembicCache)
                    #
                    branchInfo = alembicNode, namespace, localTimeTag
            return branchInfo
        (
            timestamp,
            cacheSceneStage,
            startFrame, endFrame,
            scAstModelCache,
            assetIndex,
            assetClass, assetName, number, assetVariant
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
            assetClass, assetName, number, assetVariant,
            scAstModelProductBranchInfo, scAstModelCacheBranchInfo,
            scAstCfxProductBranchInfo, scAstCfxCacheBranchInfoLis,
            scAstSolverProductBranchInfo, scAstSolverCacheBranchInfo,
            scAstExtraCacheBranchInfo
        ))
    #
    dic = lxBasic.orderedDict()
    #
    sceneInfoLis = getSceneInfo()
    if sceneInfoLis:
        for sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage in sceneInfoLis:
            cameraCompose = []
            assetCompose = []
            # Camera
            cameraIndexData = scenePr.getSceneCameraIndexDataDic(
                projectName, sceneClass, sceneName, sceneVariant
            )
            if cameraIndexData:
                for k, v in cameraIndexData.items():
                    for camSeq, i in enumerate(v):
                        getScCameraBranch(camSeq)
            # Asset
            assetIndexData = scenePr.getSceneAssetIndexDataDic(
                projectName, sceneClass, sceneName, sceneVariant
            )
            if assetIndexData:
                for k, v in assetIndexData.items():
                    for i in v:
                        getScAssetBranch(i)
            #
            dic[(sceneIndex, sceneClass, sceneName, sceneVariant)] = cameraCompose, assetCompose
    #
    return dic


#
def getScAstUnitDic(projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    def getBranch(args):
        (
            timestamp,
            cacheStage,
            startFrame, endFrame,
            cache,
            assetIndex,
            assetClass, assetName, number, assetVariant
         ) = args
        #
        sceneAssetUnitGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        if maUtils.isAppExist(sceneAssetUnitGroup):
            maUtils.setObjectParent(sceneAssetUnitGroup, scLinkAssetGroup)
            if scenePr.isScSolverLink(sceneStage) or scenePr.isScLightLink(sceneStage):
                scAstModelNamespace = scenePr.scAstModelNamespace(
                    sceneName, sceneVariant,
                    assetName, number
                )
                assetPr.astUnitModelLinkGroupName(assetName, scAstModelNamespace)
                key = assetPr.astUnitModelLinkGroupName(assetName, scAstModelNamespace)
            else:
                key = sceneAssetUnitGroup
            #
            print '''assetIndex = '{}'\nassetClass = '{}'\nassetName = '{}'\nassetVariant = '{}'\nnumber = '{}'\n'''.format(
                assetIndex,
                assetClass, assetName, assetVariant, number
            )
            dic[key] = assetIndex, assetClass, assetName, number, assetVariant
    #
    dic = lxBasic.orderedDict()
    #
    sceneAssetData = scenePr.getSceneAssetIndexDataDic(
        projectName, sceneClass, sceneName, sceneVariant
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
        assetClass, assetName, number,
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
    if scenePr.isScLayoutLink(sceneStage) or scenePr.isScAnimationLink(sceneStage):
        meshRoot = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    elif scenePr.isScSimulationLink(sceneStage):
        meshRoot = scenePr.scAstModelGroupName(sceneName, sceneVariant, assetName, number, namespace)
    elif scenePr.isScSolverLink(sceneStage) or scenePr.isScLightLink(sceneStage):
        meshRoot = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    #
    if meshRoot:
        astModelGroup = assetPr.astUnitModelLinkGroupName(assetName, namespace)
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
            progressBar = qtProgress.viewSubProgress(explain, maxValue)
            for meshKey in unionInfoDic:
                progressBar.updateProgress()
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
def getScAstRigAlembicAttrData(projectName, assetClass, assetName, assetVariant):
    lis = []
    rigExtraData = assetPr.getAssetUnitExtraData(
        projectName,
        assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
    )
    if rigExtraData:
        if lxConfigure.LynxiAlembicAttrDataKey in rigExtraData:
            data = rigExtraData[lxConfigure.LynxiAlembicAttrDataKey]
            if data:
                lis = data
    return lis


#
def getScSceneryExtraData(sceneName, sceneVariant, sceneStage):
    dic = lxBasic.orderedDict()
    assemblyReferenceData, transformationData = getScScenery(sceneName, sceneVariant, sceneStage)
    dic[lxConfigure.LynxiAssemblyReferenceDataKey] = assemblyReferenceData
    dic[lxConfigure.LynxiTransformationDataKey] = transformationData
    return dic


#
def getScAssemblyComposeDatumLis(sceneName, sceneVariant, sceneStage):
    lis = []
    rootPath = scenePr.scScenerySubGroupPath(sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_layout)
    if maUtils.isAppExist(rootPath):
        stringLis = maUtils.getChildNodesByRoot(rootPath, filterTypes=appCfg.MaNodeType_AssemblyReference)
        if stringLis:
            progressExplain = u'''Read Assembly Compose Unit(s)'''
            maxValue = len(stringLis)
            progressBar = qtProgress.viewSubProgress(progressExplain, maxValue)
            for assemblyPath in stringLis:
                progressBar.updateProgress()
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
    scSceneryBranchPath = scenePr.scScenerySubGroupPath(sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_layout)
    if maUtils.isAppExist(scSceneryBranchPath):
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
    if maUtils.isAppExist(astUnitModelProductGroup):
        lis = maGeom.getMeshObjectsByGroup(astUnitModelProductGroup)
    return lis


#
def getMeshObjectsConstantDic(astUnitModelProductGroup):
    infoConfig = ['hierarchy', 'geometry', 'geometryShape', 'map', 'mapShape']
    dic = lxBasic.orderedDict()
    meshesInformation = maGeom.getGeometryObjectsInfo(astUnitModelProductGroup)
    for seq, i in enumerate(infoConfig):
        dic[i] = meshesInformation[seq]
    return dic


#
def getMeshConstantDataByRoot(sceneName, sceneVariant, assetName, number, namespace=none):
    # Dict { <Constant Item>: <Constant Value> }
    dic = lxBasic.orderedDict()
    geometries = []
    if namespace:
        scAstGeometryGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    else:
        scAstGeometryGroup = scenePr.scAstGeometryGroupName(sceneName, sceneVariant, assetName, number)
    if maUtils.isAppExist(scAstGeometryGroup):
        geometries = maGeom.getMeshObjectsByGroup(scAstGeometryGroup)
    #
    if geometries:
        dic = datAsset.getMeshObjectsEvaluateDic(geometries)
        subData = getMeshObjectsConstantDic(scAstGeometryGroup)
        for k, v in subData.items():
            dic[k] = v
    return dic
