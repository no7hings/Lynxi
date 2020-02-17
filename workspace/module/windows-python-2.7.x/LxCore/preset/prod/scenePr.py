# coding=utf-8
from LxBasic import bscConfigure, bscCore, bscMethods

from LxScheme import shmOutput
#
from LxPreset import prsConfigure, prsVariants, prsMethods
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr, sceneryPr
# do not delete and rename
serverBasicPath = shmOutput.Root().basic.server
localBasicPath = shmOutput.Root().basic.local
#
none = ''


# Group Name Config
def scSceneNameSet(sceneName, subLabelString):
    nameSet = '%s_%s%s' % (prsVariants.Util.Lynxi_Prefix_Product_scene, sceneName, subLabelString)
    return nameSet


# Group Name Config
def scSceneSubNameSet(sceneName, sceneVariant, subLabelString):
    nameSet = '%s_%s_%s%s' % (prsVariants.Util.Lynxi_Prefix_Product_scene, sceneName, sceneVariant, subLabelString)
    return nameSet


# Group Name Config
def scGroupNameSet(sceneName, groupNameLabel):
    nameSet = '%s_%s%s%s' % (
        prsVariants.Util.Lynxi_Prefix_Product_scene, sceneName, groupNameLabel, prsVariants.Util.basicGroupLabel)
    return nameSet


# Group Name Config
def scSubGroupNameSet(sceneName, sceneVariant, groupNameLabel):
    nameSet = '%s_%s_%s%s%s' % (
        prsVariants.Util.Lynxi_Prefix_Product_scene, sceneName, sceneVariant, groupNameLabel, prsVariants.Util.basicGroupLabel)
    return nameSet


#
def sceneFullName(sceneName, sceneVariant):
    nameSet = '%s_%s_%s' % (prsVariants.Util.Lynxi_Prefix_Product_scene, sceneName, sceneVariant)
    return nameSet


#
def scAstName(assetName, number, assetVariant):
    nameSet = '%s_%s_%s_%s' % (prsVariants.Util.Lynxi_Prefix_Product_Asset, assetName, number, assetVariant)
    return nameSet


#
def scComposeRootGroupName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, prsVariants.Util.basicComposeRootGroupLabel)
    return string


#
def scUnitRootGroupName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, prsVariants.Util.basicUnitRootGroupLabel)
    return string


#
def scCameraBranchName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, prsVariants.Util.basicScCameraGroupLabel)
    return string


#
def scAstBranchName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, prsVariants.Util.basicScAstGroupLabel)
    return string


#
def scSceneryBranchName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, prsVariants.Util.basicScSceneryGroupLabel)
    return string


#
def scRootGroupHierarchyConfig(sceneName):
    dic = bscCore.orderedDict()
    dic[scUnitRootGroupName(sceneName)] = []
    return dic


#
def getScLinkGroupLabel(sceneStage):
    string = prsVariants.Util.basicLayoutLinkGroupLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.basicLayoutLinkGroupLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.basicAnimationLinkGroupLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.basicSolverLinkGroupLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.basicSimulationLinkGroupLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.basicLightLinkGroupLabel
    return string


#
def scUnitLinkGroupName(sceneName, sceneVariant, sceneStage, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scSubGroupNameSet(sceneName, sceneVariant, getScLinkGroupLabel(sceneStage))
    return string


#
def scCameraSubGroupPath(sceneName, sceneVariant, sceneStage, namespace=none):
    string = scUnitLinkGroupName(sceneName, sceneVariant, sceneStage, namespace) + '|' + scCameraBranchName(sceneName, namespace)
    return string


#
def scAssetSubGroupPath(sceneName, sceneVariant, sceneStage, namespace=none):
    string = scUnitLinkGroupName(sceneName, sceneVariant, sceneStage, namespace) + '|' + scAstBranchName(sceneName, namespace)
    return string


#
def scScenerySubGroupPath(sceneName, sceneVariant, sceneStage, namespace=none):
    string = scUnitLinkGroupName(sceneName, sceneVariant, sceneStage, namespace) + '|' + scSceneryBranchName(sceneName, namespace)
    return string


#
def scAstRootGroupName(sceneName, sceneVariant, assetName, number, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + sceneFullName(sceneName, sceneVariant) + '_%s_%s%s' % (assetName, number, prsVariants.Util.basicGroupLabel)
    return string


#
def scAstRootGroupPath(sceneName, sceneVariant, assetName, number, namespace=none):
    return scAstBranchName(sceneName, namespace) + '|' + scAstRootGroupName(sceneName, sceneVariant, assetName, number, namespace)


#
def scAstModelGroupName(sceneName, sceneVariant, assetName, number, namespace=none):
    scAstRootGroup = scAstRootGroupName(sceneName, sceneVariant, assetName, number, namespace)
    astUnitRootGroup = prsMethods.Asset.rootName(assetName)
    assetModelGroupName = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
    string = '|'.join([scAstRootGroup, astUnitRootGroup, assetModelGroupName])
    return string


#
def scAstGeometryGroupName(sceneName, sceneVariant, assetName, number, namespace=none):
    scAstRootGroup = scAstRootGroupName(sceneName, sceneVariant, assetName, number, namespace)
    astUnitRootGroup = prsMethods.Asset.rootName(assetName)
    astModelGroup = prsMethods.Asset.modelLinkGroupName(assetName, namespace)
    astGeometryGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    string = '|'.join([scAstRootGroup, astUnitRootGroup, astModelGroup, astGeometryGroup])
    return string


#
def scLinkHierarchyConfig(sceneName, sceneVariant, sceneStage):
    dic = bscCore.orderedDict()
    # Main
    dic[scUnitLinkGroupName(sceneName, sceneVariant, sceneStage)] = [
        scCameraBranchName(sceneName),
        scAstBranchName(sceneName),
        scSceneryBranchName(sceneName)
    ]
    return dic


#
def sceneSchemeFileConfig():
    string = '{0}/{1}/{2}/{3}'.format(prsVariants.Util.dbSceneRoot, prsVariants.Util.dbBasicFolderName, prsConfigure.Utility.LynxiSchemeExt, prsVariants.Util.dbSceneBasicKey)
    return bscMethods.OsFile.uniqueName(string)


#
def sceneSetFileConfig(sceneIndex):
    string = '{0}/{1}/{2}/{3}'.format(prsVariants.Util.dbSceneRoot, prsVariants.Util.dbBasicFolderName, prsConfigure.Utility.LynxiSetExt, sceneIndex)
    return string


#
def defaultSceneSchemeConfig():
    lis = [
        True,
        u'000 - 000'
    ]
    return lis


# Scheme Data
def getUiSceneSchemeDataDic():
    def getCustomData():
        fileString_ = sceneSchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getDic(data):
        dic = bscCore.orderedDict()
        if data:
            for i in data:
                scheme, enabled, description = i
                dic[scheme] = enabled, description
        return dic
    #
    return getDic(getCustomData())


#
def getSceneViewName(sceneIndex):
    def getCustomData():
        fileString_ = sceneSchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getSubDic(data):
        dic = bscCore.orderedDict()
        if data:
            for i in data:
                scheme, enabled, description = i
                dic[scheme] = description
        return dic
    #
    def getMain(customDic):
        string = prsConfigure.Utility.DEF_value_preset_unspecified
        if sceneIndex in customDic:
            string = customDic[sceneIndex]
        return string
    #
    return getMain(getSubDic(getCustomData()))


#
def getSceneClass(sceneIndex):
    def getCustomData():
        fileString_ = sceneSetFileConfig(sceneIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic[prsConfigure.Product.DEF_key_info_category]
    #
    return getMain(getCustomData())


#
def getSceneName(sceneIndex):
    def getCustomData():
        fileString_ = sceneSetFileConfig(sceneIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['name']
    #
    return getMain(getCustomData())


#
def getScenePriority(sceneIndex):
    def getCustomData():
        fileString_ = sceneSetFileConfig(sceneIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['priority']
    #
    return getMain(getCustomData())


#
def getSceneVariants(sceneIndex):
    def getCustomData():
        fileString_ = sceneSetFileConfig(sceneIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic[prsConfigure.Product.DEF_key_info_variant]
    #
    return getMain(getCustomData())


#
def getSceneLinkEnabled(sceneIndex, link):
    def getCustomData():
        fileString_ = sceneSetFileConfig(sceneIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic[link]
    #
    return getMain(getCustomData())


#
def sceneViewInfoSet(sceneViewName, sceneCategory, sceneVariant):
    string = u'{} {} ( {} )'.format(
        prsMethods.Scene.categoryShowname(sceneCategory),
        sceneViewName,
        sceneVariant
    )
    return string


#
def sceneViewEnInfoSet(sceneViewName, sceneCategory, sceneVariant):
    string = '{} {} ( {} )'.format(
        bscMethods.StrCamelcase.toPrettify(sceneCategory),
        sceneViewName,
        sceneVariant
    )
    return string


#
def getSceneViewInfo(sceneIndex, sceneCategory, sceneVariant):
    return sceneViewInfoSet(getSceneViewName(sceneIndex), sceneCategory, sceneVariant)


#
def getSceneEnViewInfo(sceneIndex, sceneCategory, sceneVariant):
    return sceneViewEnInfoSet(getSceneViewName(sceneIndex), sceneCategory, sceneVariant)


#
def getSceneIndexesFilter(projectFilter, sceneClassFilters=None):
    def getCustomData():
        fileString_ = sceneSchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getBranch(lis, sceneIndex):
        fileString_ = sceneSetFileConfig(sceneIndex)
        data = bscMethods.OsJson.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                dbSceneClass = data[prsConfigure.Product.DEF_key_info_category]
                if sceneClassFilters is not None:
                    if dbSceneClass in sceneClassFilters:
                        lis.append(sceneIndex)
                elif sceneClassFilters is None:
                    lis.append(sceneIndex)
    #
    def getMain(data):
        lis = []
        if data:
            for i in data:
                sceneIndex, enabled, description = i
                if enabled is True:
                    getBranch(lis, sceneIndex)
        return lis
    #
    return getMain(getCustomData())


#
def getUiSceneMultMsgs(projectFilter, sceneClassFilters=None, sceneLinkFilter=None):
    def getCustomData():
        fileString_ = sceneSchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getLinks(data):
        lis = []
        for i in prsMethods.Scene.linkNames():
            enabled = data[i]
            if enabled is True:
                lis.append(i)
        return lis
    #
    def getBranch(dic, sceneIndex, description):
        fileString_ = sceneSetFileConfig(sceneIndex)
        data = bscMethods.OsJson.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                isFilter = False
                #
                dbSceneClass = data[prsConfigure.Product.DEF_key_info_category]
                dbSceneName = data['name']
                dbSceneLinks = getLinks(data)
                if sceneClassFilters is not None:
                    if dbSceneClass in sceneClassFilters:
                        if sceneLinkFilter is not None:
                            if sceneLinkFilter in dbSceneLinks:
                                isFilter = True
                        elif sceneLinkFilter is None:
                            isFilter = True
                elif sceneClassFilters is None:
                    if sceneLinkFilter is not None:
                        if sceneLinkFilter in dbSceneLinks:
                            isFilter = True
                    elif sceneLinkFilter is None:
                        isFilter = True
                #
                if isFilter is True:
                    dic[sceneIndex] = dbSceneName, description
    #
    def getMain(data):
        dic = bscCore.orderedDict()
        if data:
            for i in data:
                sceneIndex, enabled, description = i
                if enabled is True:
                    getBranch(dic, sceneIndex, description)
        return dic
    #
    return getMain(getCustomData())


#
def getUiSceneSetDataDic(projectFilter):
    def getCustomData():
        fileString_ = sceneSchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getBranch(dic, sceneIndex, description):
        fileString_ = sceneSetFileConfig(sceneIndex)
        data = bscMethods.OsJson.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                sceneCategory = data[prsConfigure.Product.DEF_key_info_category]
                sceneName = data['name']
                sceneVariants = data['variant']
                scenePriority = data['priority']
                scLayoutEnable = data['layout']
                scAnimationEnable = data['animation']
                scSolverEnable = data[prsMethods.Scene.solverLinkName()]
                scSimulationEnable = data['simulation']
                scLightEnable = data['light']
                for sceneVariant in sceneVariants:
                    dic[(sceneIndex, sceneVariant)] = description, sceneCategory, sceneName, scenePriority, scLayoutEnable, scAnimationEnable, scSolverEnable, scSimulationEnable, scLightEnable
    #
    def getMain(data):
        dic = bscCore.orderedDict()
        if data:
            for i in data:
                sceneIndex, enabled, description = i
                if enabled is True:
                    getBranch(dic, sceneIndex, description)
        return dic
    #
    return getMain(getCustomData())


# Start Frame Set
def scStartFrame(startFrame, keyFrameOffset=None):
    if keyFrameOffset:
        return startFrame - keyFrameOffset
    else:
        return startFrame - prsVariants.Util.animKeyFrameOffset


# End Frame Set
def scEndFrame(endFrame, keyFrameOffset=None):
    if keyFrameOffset:
        return endFrame + keyFrameOffset
    else:
        return endFrame + prsVariants.Util.animKeyFrameOffset


#
def alembicCacheInfoDic(sceneStage, startFrame, endFrame, step, description=None, notes=None):
    return {
        bscConfigure.Utility.DEF_key_info_timestamp: bscMethods.OsTimestamp.active(),
        bscConfigure.Utility.DEF_key_info_username: bscMethods.OsSystem.username(),
        #
        bscConfigure.Utility.DEF_key_info_description: description,
        bscConfigure.Utility.DEF_key_info_note: notes,
        #
        bscConfigure.Utility.DEF_key_info_stage: sceneStage,
        #
        'startFrame': startFrame,
        'endFrame': endFrame,
        'step': step
    }


# Get Dict For Animation Camera Cache's Link
def geomCacheIndexData(sceneStage, startFrame, endFrame, step, cacheIndex, timeTag):
    dic = bscCore.orderedDict()
    dic[bscConfigure.Utility.DEF_key_info_timestamp] = bscMethods.OsTimestamp.active()
    dic[bscConfigure.Utility.DEF_key_info_username] = bscMethods.OsSystem.username()
    #
    dic[bscConfigure.Utility.DEF_key_info_stage] = sceneStage
    dic[bscConfigure.Utility.DEF_key_info_version] = timeTag
    #
    dic['startFrame'] = startFrame
    dic['endFrame'] = endFrame
    dic['step'] = step
    #
    for k, v in cacheIndex.items():
        dic[k] = v
    return dic


# Get Dict For Fur Animation Cache's Link
def furCacheIndexData(nodePath, solverNodeType, cacheFile, startFrame, endFrame, sample, solverMode, timeTag):
    dic = bscCore.orderedDict()
    #
    dic[bscConfigure.Utility.DEF_key_info_timestamp] = bscMethods.OsTimestamp.active()
    dic[bscConfigure.Utility.DEF_key_info_username] = bscMethods.OsSystem.username()
    dic['version'] = timeTag
    #
    dic['startFrame'] = startFrame
    dic['endFrame'] = endFrame
    #
    dic['sample'] = sample
    dic['node'] = nodePath
    dic['nodeType'] = solverNodeType
    dic['solverMode'] = solverMode
    dic['cache'] = cacheFile
    return dic


#
def scSceneCameraName(sceneName, sceneVariant):
    string = scSceneSubNameSet(sceneName, sceneVariant, prsVariants.Util.scCameraNodeLabel)
    return string


#
def scOutputCameraName(sceneName, sceneVariant, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scSceneSubNameSet(sceneName, sceneVariant, prsVariants.Util.scOutputCameraNodeLabel)
    return string


# Camera Locator Name
def scOutputCameraLocatorName(sceneName, sceneVariant, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scSceneSubNameSet(sceneName, sceneVariant, prsVariants.Util.scCameraLocatorNodeLabel)
    return string


# Adjust Locator Name
def scOutputCameraSubLocatorName(sceneName, sceneVariant, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scSceneSubNameSet(sceneName, sceneVariant, prsVariants.Util.scCameraSubLocatorNodeLabel)
    return string


#
def scRenderSize():
    return prsVariants.Util.rndrImageWidth, prsVariants.Util.rndrImageHeight


#
def isLayoutLinkName(sceneStage):
    boolean = False
    if sceneStage in prsMethods.Scenery.VAR_product_scenery_layout_stage_list or sceneStage == prsMethods.Scene.layoutLinkName():
        boolean = True
    return boolean


#
def isAnimationLinkName(sceneStage):
    boolean = False
    if sceneStage in prsMethods.Scene.VAR_product_scene_animation_stage_list or sceneStage == prsMethods.Scene.animationLinkName():
        boolean = True
    return boolean


#
def isSolverLinkName(sceneStage):
    boolean = False
    if sceneStage in prsMethods.Scene.VAR_product_scene_solver_stage_list or sceneStage == prsMethods.Scene.solverLinkName():
        boolean = True
    return boolean


#
def isSimulationLinkName(sceneStage):
    boolean = False
    if sceneStage in prsMethods.Scene.VAR_product_scene_simulation_stage_list or sceneStage == prsMethods.Scene.simulationLinkName():
        boolean = True
    return boolean


#
def isLightLinkName(sceneStage):
    boolean = False
    if sceneStage in prsMethods.Scene.VAR_product_scene_light_stage_list or sceneStage == prsMethods.Scene.lightLinkName():
        boolean = True
    return boolean


#
def sceneLinkFolder(sceneStage):
    string = prsVariants.Util.scLayoutFolder
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutFolder
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationFolder
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverFolder
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationFolder
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightFolder
    return string


#
def sceneSourceFileLabel(sceneStage):
    string = prsVariants.Util.scLayoutSourceLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutSourceLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationSourceLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverSourceLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationSourceLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightSourceLabel
    return string


#
def sceneProductFileLabel(sceneStage):
    string = prsVariants.Util.scLayoutProductLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutProductLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationProductLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverProductLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationProductLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightProductLabel
    return string


#
def sceneExtraFileLabel(sceneStage):
    string = prsVariants.Util.scLayoutExtraLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutExtraLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationExtraLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverExtraLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationExtraLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightExtraLabel
    return string


#
def sceneRenderFileLabel(sceneStage):
    string = prsVariants.Util.scLayoutRenderLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutRenderLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationRenderLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverRenderLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationRenderLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightRenderLabel
    return string


#
def sceneCameraFileLabel(sceneStage):
    string = prsVariants.Util.scLayoutCameraLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutCameraLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationCameraLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverCameraLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationCameraLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightCameraLabel
    return string


#
def sceneSoundFileLabel(sceneStage):
    return prsMethods.Scene.toLinkMainLabelname(sceneStage) + prsVariants.Util.scSoundLabel.upper()


#
def sceneAssetFileLabel(sceneStage):
    string = prsVariants.Util.scLayoutAssetLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutAssetLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationAssetLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverAssetLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationAssetLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightAssetLabel
    return string


#
def scAstSolverFileLabel(sceneStage):
    subLabelString = prsVariants.Util.basicSolverSubLabel
    return bscMethods.StrUnderline.toLabel(prsMethods.Scene.toLinkMainLabelname(sceneStage), subLabelString)


#
def sceneSceneryFileLabel(sceneStage):
    string = prsVariants.Util.scLayoutSceneryLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutSceneryLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationSceneryLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverSceneryLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationSceneryLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightSceneryLabel
    return string


#
def scenePreviewFileLabel(sceneStage):
    string = prsVariants.Util.scLayoutPreviewLabel
    if prsMethods.Scene.isLayoutLinkName(sceneStage):
        string = prsVariants.Util.scLayoutPreviewLabel
    elif prsMethods.Scene.isAnimationLinkName(sceneStage):
        string = prsVariants.Util.scAnimationPreviewLabel
    elif prsMethods.Scene.isSolverLinkName(sceneStage):
        string = prsVariants.Util.scSolverPreviewLabel
    elif prsMethods.Scene.isSimulationLinkName(sceneStage):
        string = prsVariants.Util.scSimulationPreviewLabel
    elif prsMethods.Scene.isLightLinkName(sceneStage):
        string = prsVariants.Util.scLightPreviewLabel
    return string


#
def scSceneFileNameConfig(sceneName, nameLabel, extLabel):
    string = '%s%s%s' % (sceneName, nameLabel, extLabel)
    return string


#
def scAstFileNameConfig(assetName, number, nameLabel, extLabel):
    string = '%s_%s%s%s' % (assetName, number, nameLabel, extLabel)
    return string


#
def scAstNodeFileNameConfig(assetName, number, assetVariant, nodeLabel, nameLabel, extLabel):
    string = '%s_%s_%s_%s%s%s' % (assetName, number, assetVariant, nodeLabel, nameLabel, extLabel)
    return string


#
def scAstFolderNameConfig(assetName, number, nameLabel):
    string = '%s_%s%s' % (assetName, number, nameLabel)
    return string


#
def scAstNodeFolderNameConfig(assetName, number, assetVariant, nameLabel):
    string = '%s_%s_%s_%s' % (assetName, number, assetVariant, nameLabel)
    return string


# Camera
def scCameraNamespace(sceneName, sceneVariant):
    return scSceneSubNameSet(sceneName, sceneVariant, prsVariants.Util.scCameraNodeLabel)


#
def sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number):
    if sceneName and sceneVariant:
        string = sceneFullName(sceneName, sceneVariant) + '_%s_%s' % (assetName, number)
    else:
        string = '%s_%s_%s' % (prsVariants.Util.Lynxi_Prefix_Product_Asset, assetName, number)
    return string


# Model Product
def scAstModelNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scModelNodeLabel


# Model Cache
def scAstModelCacheNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scCacheNodeLabel


# Model
def scAstModelReferenceNode(sceneName, sceneVariant, assetName, number):
    return scAstModelNamespace(sceneName, sceneVariant, assetName, number) + appCfg.MaRN


# Rig
def scAstRigNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scRigNodeLabel


# Rig Reference Nde_Node
def scAstRigReferenceNode(sceneName, sceneVariant, assetName, number):
    return scAstRigNamespace(sceneName, sceneVariant, assetName, number) + appCfg.MaRN


# CFX
def scAstCfxNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.basicCharacterFxLinkLabel


#
def scAstSimulationNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.basicSimulationLinkLabel


# Model
def scAstModelDisplayLayer(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scModelNodeLabel + prsVariants.Util.displayLayerLabel


# CFX
def scAstCfxDisplayLayer(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scCfxNodeLabel + prsVariants.Util.displayLayerLabel


#
def scAstCfxReferenceNode(sceneName, sceneVariant, assetName, number):
    return scAstCfxNamespace(sceneName, sceneVariant, assetName, number) + appCfg.MaRN


# Solver
def scAstSolverNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scSolverNodeLabel


# Solver Cache
def scAstSolverCacheNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scSolverCacheNodeLabel


# Solver Cache
def scAstSolverCacheReferenceNode(sceneName, sceneVariant, assetName, number):
    return scAstSolverCacheNamespace(sceneName, sceneVariant, assetName, number) + appCfg.MaRN


# Extra
def scAstExtraNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scExtraNodeLabel


# Extra
def scAstExtraCacheNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scExtraCacheNodeLabel


#
def sceneAssetCfxUnitNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + prsVariants.Util.scCfxNodeLabel


#
def sceneUnitBasicDirectory(rootIndexKey, projectName):
    root = [prsVariants.Util.serverSceneRoot, prsVariants.Util.localSceneRoot, prsVariants.Util.backupSceneRoot]
    return '%s/%s/%s/%s' % (root[rootIndexKey], projectName, prsVariants.Util.basicSceneFolder, prsVariants.Util.scUnitFolder)


#
def sceneUnitCacheBasicDirectory(rootIndexKey, projectName):
    root = [prsVariants.Util.serverGeomCacheRoot, prsVariants.Util.localGeomCacheRoot, prsVariants.Util.backupGeomCacheRoot]
    return '%s/%s/%s' % (root[rootIndexKey], projectName, prsVariants.Util.basicCacheFolder)


#
def sceneUnitRenderBasicDirectory(rootIndexKey, projectName):
    root = [prsVariants.Util.serverRenderRoot, prsVariants.Util.localRenderRoot, prsVariants.Util.backupRenderRoot]
    return '%s/%s/%s' % (root[rootIndexKey], projectName, prsVariants.Util.basicRenderFolder)


#
def sceneUnitFolder(rootIndexKey, projectName, sceneCategory, sceneName):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    fileDirectory = '%s/%s' % (
        basicDirectory,
        sceneName
    )
    return fileDirectory


# Nde_Geometry Cache
def scUnitIndexFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = none
    extLabel = prsVariants.Util.scSceneIndexExt
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    fileString_ = '%s/%s/%s/%s' % (
        basicDirectory,
        sceneName, sceneVariant,
        osFileName
    )
    return osFileName, fileString_


#
def sceneUnitSourceFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneSourceFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.mayaAsciiExt)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def sceneUnitProductFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneProductFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.mayaAsciiExt)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def sceneExtraFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    folderLabel = sceneExtraFileLabel(sceneStage)
    #
    osFolder = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        folderLabel
    )
    return osFolder


#
def scUnitCameraProductFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneCameraFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.mayaAsciiExt)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scUnitCameraFbxFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneCameraFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.fbxExt)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scenePreviewFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, extLabel=prsVariants.Util.aviExt):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = scenePreviewFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def sceneSoundFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneSoundFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.mayaAsciiExt)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scenePreviewIndexFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = none
    extLabel = prsVariants.Util.scPreviewIndexExt
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def sceneCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant):
    basicDirectory = sceneUnitCacheBasicDirectory(rootIndexKey, projectName)
    #
    osFolder = '{0}/{1}/{2}'.format(
        basicDirectory,
        sceneName, sceneVariant
    )
    return osFolder


#
def scCameraCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant):
    basicDirectory = sceneUnitCacheBasicDirectory(rootIndexKey, projectName)
    #
    osFolder = '{0}/{1}/{2}/{3}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        prsVariants.Util.cacheCameraFolder
    )
    return osFolder


#
def scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant):
    basicDirectory = sceneUnitCacheBasicDirectory(rootIndexKey, projectName)
    #
    osFolder = '{0}/{1}/{2}/{3}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        prsVariants.Util.cacheAssetFolder
    )
    return osFolder


#
def scUnitSceneryExtraFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneSceneryFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.dbExtraUnitKey)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scAssemblyLabel(sceneStage):
    subLabelString = prsVariants.Util.basicAssemblySubLabel
    return bscMethods.StrUnderline.toLabel(prsMethods.Scene.toLinkMainLabelname(sceneStage), subLabelString)


#
def scUnitAssemblyComposeFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = scAssemblyLabel(sceneStage)
    extLabel = prsVariants.Util.assemblyComposeExt
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant):
    basicDirectory = sceneUnitCacheBasicDirectory(rootIndexKey, projectName)
    #
    osFolder = '{0}/{1}/{2}/{3}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        prsVariants.Util.cacheSimulationFolder
    )
    return osFolder


#
def scCameraCacheIndexFile(rootIndexKey, projectName, sceneName, sceneVariant):
    fileLabel = none
    extLabel = prsVariants.Util.scGeomCacheIndexExt
    #
    osFolder = scCameraCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    #
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scUnitCameraAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, sceneStage):
    fileLabel = sceneCameraFileLabel(sceneStage)
    extLabel = prsVariants.Util.alembicCacheExt
    #
    osFolder = scCameraCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    #
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scAstCacheIndexFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number):
    fileLabel = none
    extLabel = prsVariants.Util.scGeomCacheIndexExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scAstModelAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, sceneStage, assetName, number):
    fileLabel = sceneAssetFileLabel(sceneStage)
    extLabel = prsVariants.Util.alembicCacheExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scAstRigExtraAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number):
    fileLabel = prsVariants.Util.scAstRigExtraLabel
    extLabel = prsVariants.Util.alembicCacheExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scAstModelPoseAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number):
    fileLabel = prsVariants.Util.scAstModelPoseLabel
    extLabel = prsVariants.Util.alembicCacheExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scAstSolverAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, sceneStage, assetName, number):
    fileLabel = scAstSolverFileLabel(sceneStage)
    extLabel = prsVariants.Util.alembicCacheExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scAstCfxFurCacheIndexFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    fileLabel = none
    extLabel = prsVariants.Util.scFurCacheIndexExt
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstNodeFileNameConfig(assetName, number, assetVariant, furObjectLabel, fileLabel, extLabel)
    #
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


# Animation Fur Cache Path
def scAstCfxYetiCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, timeTag=None):
    extLabel = '.%04d.fur'
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    if timeTag:
        subLabelString = '_' + timeTag
    else:
        subLabelString = none
    #
    subFolder = scAstNodeFolderNameConfig(assetName, number, assetVariant, furObjectLabel) + subLabelString
    #
    fileName = furObjectLabel + extLabel
    #
    fileString_ = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder, fileName
    )
    return fileName, fileString_


#
def scAstCfxGeomCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, timeTag=None):
    extLabel = '.xml'
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    if timeTag:
        subLabelString = '_' + timeTag
    else:
        subLabelString = none
    #
    subFolder = scAstNodeFolderNameConfig(assetName, number, assetVariant, furObjectLabel) + subLabelString
    #
    fileName = furObjectLabel + extLabel
    #
    fileString_ = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder, fileName
    )
    return fileName, fileString_


#
def scAstCfxAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, timeTag=None):
    extLabel = prsVariants.Util.alembicCacheExt
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    if timeTag:
        subLabelString = '_' + timeTag
    else:
        subLabelString = none
    #
    subFolder = scAstNodeFolderNameConfig(assetName, number, assetVariant, furObjectLabel) + subLabelString
    #
    fileName = furObjectLabel + extLabel
    #
    fileString_ = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder, fileName
    )
    return fileName, fileString_


#
def scAstCfxNurbsHairCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, timeTag=None):
    extLabel = '.####.nhr'
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    if timeTag:
        subLabelString = '_' + timeTag
    else:
        subLabelString = none
    #
    subFolder = scAstNodeFolderNameConfig(assetName, number, assetVariant, furObjectLabel) + subLabelString
    #
    fileName = furObjectLabel + extLabel
    #
    fileString_ = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder, fileName
    )
    return fileName, fileString_


#
def scUnitIndexDic(sceneIndex, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, startFrame, endFrame):
    dic = bscCore.orderedDict()
    #
    dic[bscConfigure.Utility.DEF_key_info_timestamp] = bscMethods.OsTimestamp.active()
    dic[bscConfigure.Utility.DEF_key_info_username] = bscMethods.OsSystem.username()
    #
    dic[prsVariants.Util.basicIndexAttrLabel] = sceneIndex
    dic[prsVariants.Util.basicProjectAttrLabel] = projectName
    dic[prsVariants.Util.basicClassAttrLabel] = sceneCategory
    dic[prsVariants.Util.basicNameAttrLabel] = sceneName
    dic[prsVariants.Util.basicVariantAttrLabel] = sceneVariant
    dic[prsVariants.Util.basicStageAttrLabel] = sceneStage
    dic[prsVariants.Util.basicStartFrameAttrLabel] = startFrame
    dic[prsVariants.Util.basicEndFrameAttrLabel] = endFrame
    return dic


#
def scUnitCameraIndexDic(cameraData):
    return {prsVariants.Util.basicCameraAttrLabel: cameraData}


#
def scUnitAssetIndexDic(assetData):
    return {prsVariants.Util.basicAssetAttrLabel: assetData}


#
def scUnitSceneryIndexDic(sceneryData):
    return {prsVariants.Util.basicSceneryAttrLabel: sceneryData}


#
def scUnitRenderBasicFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitRenderBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    #
    osFolder = '{0}/{1}_{2}_{3}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
    )
    return osFolder


#
def scUnitRenderFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize=None):
    basicFolder = scUnitRenderBasicFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage)
    #
    if not customize:
        customize = prsVariants.Util.scDefaultCustomizeLabel
    #
    osFolder = '{0}/{1}'.format(
        basicFolder,
        customize,
    )
    return osFolder


#
def scUnitRenderImageFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize=None):
    basicFolder = scUnitRenderBasicFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage)
    #
    if not customize:
        customize = prsVariants.Util.scDefaultCustomizeLabel
        #
    #
    osFolder = '{0}/{1}/{2}'.format(
        basicFolder,
        customize,
        'images'
    )
    return osFolder


#
def scUnitRenderFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize):
    osFolder = scUnitRenderFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize)
    #
    fileLabel = sceneRenderFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.mayaAsciiExt)
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def sceUnitRenderIndexFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize):
    osFolder = scUnitRenderFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize)
    #
    fileLabel = sceneRenderFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.scRenderIndexExt)
    fileString_ = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scDeadlineBatchName(projectName, sceneName, sceneVariant, customize, jobType):
    string = u'{3}( {4} ) @ {0} : {1}( {2} )'.format(
        projectName,
        sceneName, sceneVariant, customize, jobType
    )
    return string


#
def scDeadlineJobName(renderLayer, startFrame, endFrame, width, height, timeTag):
    string = u'Layer : {0} ; Frame : {1} - {2} ; Size : {3} * {4} ; Tag : {5}'.format(
        renderLayer,
        startFrame, endFrame,
        width, height,
        timeTag,
    )
    return string


# Deadline Info
def scDeadlineInfoFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize):
    osFolder = scUnitRenderFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize)
    subFolder = '.'.join([prsVariants.Util.basicDeadlineFolder, prsVariants.Util.basicMayaFolder])
    #
    fileLabel = sceneRenderFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.scDeadlineInfoExt)
    fileString_ = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder,
        osFileName
    )
    return osFileName, fileString_


# Deadline Job
def scDeadlineJobFile(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize):
    osFolder = scUnitRenderFolder(rootIndexKey, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize)
    subFolder = '.'.join([prsVariants.Util.basicDeadlineFolder, prsVariants.Util.basicMayaFolder])
    #
    fileLabel = sceneRenderFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, prsVariants.Util.scDeadlineJobExt)
    fileString_ = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder,
        osFileName
    )
    return osFileName, fileString_


#
def getSceneStage(projectName, sceneCategory, sceneName, sceneVariant):
    string = prsMethods.Scenery.VAR_product_scenery_layout_stage_list[0]
    indexFile = scUnitIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant
    )[1]
    if bscMethods.OsFile.isExist(indexFile):
        data = bscMethods.OsJson.read(indexFile)
        string = data[prsVariants.Util.basicStageAttrLabel]
    #
    return string


#
def getScUnitFrameRange(projectName, sceneCategory, sceneName, sceneVariant):
    startFrame, endFrame = prsVariants.Util.animStartFrame, prsVariants.Util.animStartFrame + 20
    indexFile = scUnitIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant
    )[1]
    if bscMethods.OsFile.isExist(indexFile):
        data = bscMethods.OsJson.read(indexFile)
        startFrame = data[prsVariants.Util.basicStartFrameAttrLabel]
        endFrame = data[prsVariants.Util.basicEndFrameAttrLabel]
    return startFrame, endFrame


#
def getSceneProductFile(projectName, sceneCategory, sceneName, sceneVariant):
    string = none
    sceneStage = getSceneStage(projectName, sceneCategory, sceneName, sceneVariant)
    #
    productFile = sceneUnitProductFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant, sceneStage
    )[1]
    if bscMethods.OsFile.isExist(productFile):
        string = productFile
    return string


#
def getScUnitPreviewServerFile(projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    string = none
    previewTimeStamp = 0
    for osExt in [prsVariants.Util.aviExt, prsVariants.Util.movExt]:
        previewFile = scenePreviewFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName, sceneCategory, sceneName, sceneVariant, sceneStage, osExt
        )[1]
        if bscMethods.OsFile.isExist(previewFile):
            timeStamp = bscMethods.OsFile.mtimestamp(previewFile)
            currentTimeStamp = float(timeStamp)
            if currentTimeStamp > previewTimeStamp:
                string = previewFile
            previewTimeStamp = currentTimeStamp
    return string


#
def getSceneUnitProductUpdate(projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    string = prsVariants.Util.infoNonExistsLabel
    #
    serverProductFile = sceneUnitProductFile(
        prsConfigure.Utility.DEF_value_root_server, projectName, sceneCategory, sceneName, sceneVariant, sceneStage
    )[1]
    #
    if bscMethods.OsFile.isExist(serverProductFile):
        data = bscMethods.OsFile.mtimeChnPrettify(serverProductFile)
        if data:
            string = data
    return string


#
def getSceneCameraIndexDataDic(projectName, sceneCategory, sceneName, sceneVariant):
    dic = bscCore.orderedDict()
    # Key File
    indexFile = scUnitIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant
    )[1]
    if bscMethods.OsFile.isExist(indexFile):
        data = bscMethods.OsJson.read(indexFile)
        cameraData = data['camera']
        if cameraData:
            fileDirectory = scCameraCacheFolder(
                prsConfigure.Utility.DEF_value_root_server,
                projectName,
                sceneName, sceneVariant
            )
            for i in cameraData:
                osFileBasename = i + prsVariants.Util.scGeomCacheIndexExt
                fileString_ = bscMethods.OsPath.composeBy(fileDirectory, osFileBasename)
                if bscMethods.OsFile.isExist(fileString_):
                    cacheIndexData = bscMethods.OsJson.read(fileString_)
                    dataType = 'camera'
                    timestamp = bscMethods.OsFile.mtimestamp(fileString_)
                    sceneStage = cacheIndexData['stage']
                    cache = cacheIndexData[prsConfigure.Product.DEF_key_cache]
                    #
                    startFrame, endFrame = getScUnitFrameRange(projectName, sceneCategory, sceneName, sceneVariant)
                    #
                    dic.setdefault(dataType, []).append((
                        timestamp, sceneStage, startFrame, endFrame, cache
                    ))
    return dic


#
def getOutputCameras(projectName, sceneCategory, sceneName, sceneVariant):
    lis = []
    # Key File
    indexFile = scUnitIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant
    )[1]
    if bscMethods.OsFile.isExist(indexFile):
        data = bscMethods.OsJson.read(indexFile)
        cameraData = data['camera']
        if cameraData:
            for seq in range(len(cameraData)):
                subLabelString = bscMethods.OsFile.seqLabel(seq)
                #
                namespace = scCameraNamespace(sceneName, sceneVariant) + subLabelString
                #
                outputCamera = scOutputCameraName(sceneName, sceneVariant, namespace) + subLabelString
                lis.append(outputCamera)
    return lis


#
def getSceneAssetIndexDataDic(projectName, sceneCategory, sceneName, sceneVariant):
    dic = bscCore.orderedDict()
    # Key File
    indexFile = scUnitIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant
    )[1]
    if bscMethods.OsFile.isExist(indexFile):
        data = bscMethods.OsJson.read(indexFile)
        scAstUploadData = data['asset']
        if scAstUploadData:
            fileDirectory = scAstAlembicCacheFolder(
                prsConfigure.Utility.DEF_value_root_server,
                projectName, sceneName, sceneVariant
            )
            for i in scAstUploadData:
                assetIndex, assetCategory, assetName, number, assetVariant = i
                osFileBasename = scAstFileNameConfig(assetName, number, none, prsVariants.Util.scGeomCacheIndexExt)
                fileString_ = bscMethods.OsPath.composeBy(fileDirectory, osFileBasename)
                dataType = 'asset'
                if bscMethods.OsFile.isExist(fileString_):
                    cacheIndexData = bscMethods.OsJson.read(fileString_)
                    timestamp = bscMethods.OsFile.mtimestamp(fileString_)
                    sceneStage = cacheIndexData[bscConfigure.Utility.DEF_key_info_stage]
                    #

                    modelCache = bscMethods.Dict.getValue(cacheIndexData, prsConfigure.Product.DEF_key_cache)
                    extraCache = bscMethods.Dict.getValue(cacheIndexData, prsConfigure.Product.DEF_key_rigcache)
                else:
                    timestamp = None
                    sceneStage = None
                    modelCache = None
                    extraCache = None
                #
                startFrame, endFrame = getScUnitFrameRange(projectName, sceneCategory, sceneName, sceneVariant)
                #
                dic.setdefault(dataType, []).append((
                    timestamp, sceneStage, startFrame, endFrame,
                    modelCache,
                    assetIndex, assetCategory, assetName, number, assetVariant
                ))
    return dic


#
def getScSceneryIndexDataDic(projectName, sceneCategory, sceneName, sceneVariant, sceneStage=None):
    dic = bscCore.orderedDict()
    # Key File
    indexFile = scUnitIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant
    )[1]
    if bscMethods.OsFile.isExist(indexFile):
        data = bscMethods.OsJson.read(indexFile)
        key = 'scenery'
        if key in data:
            if sceneStage is None:
                sceneStage = data[bscConfigure.Utility.DEF_key_info_stage]
            #
            indexDatas = data['scenery']
            if indexDatas:
                for i in indexDatas:
                    sceneryIndex, sceneryCategory, sceneryName, sceneryVariant, sceneryStage = i
                    sceneryExtraFile = scUnitSceneryExtraFile(
                        prsConfigure.Utility.DEF_value_root_server,
                        projectName, sceneCategory, sceneName, sceneVariant, sceneStage
                    )[1]
                    sceneryFile = sceneryPr.scnUnitDefinitionFile(
                        prsConfigure.Utility.DEF_value_root_server,
                        projectName, sceneryCategory, sceneryName, sceneryVariant, prsMethods.Scenery.VAR_product_scenery_layout_stage_list[0]
                    )[1]
                    timestamp = bscMethods.OsFile.mtimestamp(sceneryExtraFile)
                    dic.setdefault(key, []).append((
                        timestamp,
                        sceneStage,
                        sceneryIndex, sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
                        sceneryFile, sceneryExtraFile
                    ))
    return dic


#
def getScSceneryExtraData(projectName, sceneCategory, sceneName, sceneVariant):
    dic = bscCore.orderedDict()
    sceneStage = getSceneStage(
        projectName,
        sceneCategory, sceneName, sceneVariant
    )
    extraFile = scUnitSceneryExtraFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant, sceneStage
    )[1]
    if bscMethods.OsFile.isExist(extraFile):
        data = bscMethods.OsJson.read(extraFile)
        if data:
            dic = data
    return dic


#
def getScSceneryAssemblyDic(projectName, sceneCategory, sceneName, sceneVariant):
    extraData = getScSceneryExtraData(projectName, sceneCategory, sceneName, sceneVariant)
    if prsConfigure.Product.DEF_key_info_asbreference in extraData:
        data = extraData[prsConfigure.Product.DEF_key_info_asbreference]
        if data:
            for i in data:
                objectPath, definition, namespace = i
                if bscMethods.OsFile.isExist(definition):
                    print definition


#
def getScCameraCacheActive(projectName, sceneName, sceneVariant, subLabelString=none):
    key = prsConfigure.Product.DEF_key_cache
    #
    fileString_ = scCameraCacheIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneName, sceneVariant
    )[1]
    subOsFile = bscMethods.OsFile.subFilename(fileString_, subLabelString)
    cache = prsVariants.Util.infoNonExistsLabel
    if bscMethods.OsFile.isExist(subOsFile):
        cacheIndexData = bscMethods.OsJson.read(subOsFile)
        if key in cacheIndexData:
            cache = cacheIndexData[key]
    return cache


#
def getScAstModelCacheActive(projectName, sceneName, sceneVariant, assetName, number):
    key = prsConfigure.Product.DEF_key_cache
    #
    fileString_ = scAstCacheIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneName, sceneVariant, assetName, number
    )[1]
    cache = prsVariants.Util.infoNonExistsLabel
    if bscMethods.OsFile.isExist(fileString_):
        cacheIndexData = bscMethods.OsJson.read(fileString_)
        if key in cacheIndexData:
            cache = cacheIndexData[key]
    return cache


#
def getScAstSolverCacheActive(projectName, sceneName, sceneVariant, assetName, number):
    key = prsConfigure.Product.DEF_key_solvercache
    #
    fileString_ = scAstCacheIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneName, sceneVariant, assetName, number
    )[1]
    #
    cache = prsVariants.Util.infoNonExistsLabel
    if bscMethods.OsFile.isExist(fileString_):
        cacheIndexData = bscMethods.OsJson.read(fileString_)
        if key in cacheIndexData:
            cache = cacheIndexData[key]
    return cache


#
def getScAstModelPoseCacheActive(projectName, sceneName, sceneVariant, assetName, number):
    timeTag = bscConfigure.Utility.DEF_time_tag_default
    cache = scAstModelPoseAlembicCacheFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        sceneName, sceneVariant, assetName, number
    )[1]
    return bscMethods.OsFile.toJoinTimetag(cache, timeTag)


#
def getScAstRigExtraCacheActive(projectName, sceneName, sceneVariant, assetName, number):
    key = prsConfigure.Product.DEF_key_rigcache
    #
    fileString_ = scAstCacheIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneName, sceneVariant, assetName, number
    )[1]
    cache = prsVariants.Util.infoNonExistsLabel
    if bscMethods.OsFile.isExist(fileString_):
        cacheIndexData = bscMethods.OsJson.read(fileString_)
        if key in cacheIndexData:
            cache = cacheIndexData[key]
    return cache


#
def getScCameraCacheDic(projectName, sceneName, sceneVariant, subLabelString):
    dic = bscCore.orderedDict()
    #
    sceneStages = [prsMethods.Scene.layoutLinkName(), prsMethods.Scene.animationLinkName(), prsMethods.Scene.simulationLinkName()]
    for sceneStage in sceneStages:
        cacheFile = scUnitCameraAlembicCacheFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName,
            sceneName, sceneVariant, sceneStage
        )[1]
        subCacheFile = bscMethods.OsFile.subFilename(cacheFile, subLabelString)
        #
        base, ext = bscMethods.OsFile.toExtSplit(subCacheFile)
        #
        osFiles = bscCore.glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
        if osFiles:
            for fileString_ in osFiles:
                fileString_ = fileString_.replace('\\', '/')
                dic.setdefault(sceneStage, []).append(fileString_)
    #
    return dic


#
def getScCameraCacheActiveTimeTag(projectName, sceneName, sceneVariant, subLabelString=none):
    fileString_ = getScCameraCacheActive(projectName, sceneName, sceneVariant, subLabelString)
    return bscMethods.OsFile.findTimetag(fileString_)


#
def getScAstModelCacheActiveTimeTag(projectName, sceneName, sceneVariant, assetName, number):
    fileString_ = getScAstModelCacheActive(projectName, sceneName, sceneVariant, assetName, number)
    return bscMethods.OsFile.findTimetag(fileString_)


#
def getScAstSolverCacheActiveTimeTag(projectName, sceneName, sceneVariant, assetName, number):
    fileString_ = getScAstSolverCacheActive(projectName, sceneName, sceneVariant, assetName, number)
    return bscMethods.OsFile.findTimetag(fileString_)


#
def getScAstRigExtraCacheActiveTimeTag(projectName, sceneName, sceneVariant, assetName, number):
    fileString_ = getScAstRigExtraCacheActive(projectName, sceneName, sceneVariant, assetName, number)
    return bscMethods.OsFile.findTimetag(fileString_)


#
def getScAstCfxFurCache(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    fileString_ = scAstCfxFurCacheIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        sceneName, sceneVariant, assetName, number, assetVariant,
        furObjectLabel
    )[1]
    furCache = prsVariants.Util.infoNonExistsLabel
    if bscMethods.OsFile.isExist(fileString_):
        cacheIndexData = bscMethods.OsJson.read(fileString_)
        furCache = cacheIndexData[prsConfigure.Product.DEF_key_cache]
    return furCache


#
def getScAstModelCacheDic(projectName, sceneName, sceneVariant, assetName, number):
    dic = bscCore.orderedDict()
    sceneStages = [prsMethods.Scene.layoutLinkName(), prsMethods.Scene.animationLinkName(), prsMethods.Scene.simulationLinkName(), prsMethods.Scene.solverLinkName()]
    for sceneStage in sceneStages:
        cacheFile = scAstModelAlembicCacheFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName,
            sceneName, sceneVariant, sceneStage,
            assetName, number
        )[1]
        #
        base, ext = bscMethods.OsFile.toExtSplit(cacheFile)
        #
        osFiles = bscCore.glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
        if osFiles:
            for fileString_ in osFiles:
                fileString_ = fileString_.replace('\\', '/')
                dic.setdefault(sceneStage, []).append(fileString_)
    #
    return dic


#
def getScAstSolverCacheDic(projectName, sceneName, sceneVariant, assetName, number):
    dic = bscCore.orderedDict()
    sceneStages = [prsMethods.Scene.layoutLinkName(), prsMethods.Scene.animationLinkName(), prsMethods.Scene.simulationLinkName(), prsMethods.Scene.solverLinkName()]
    for sceneStage in sceneStages:
        cacheFile = scAstSolverAlembicCacheFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName,
            sceneName, sceneVariant, sceneStage,
            assetName, number
        )[1]
        #
        base, ext = bscMethods.OsFile.toExtSplit(cacheFile)
        #
        osFiles = bscCore.glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
        if osFiles:
            for fileString_ in osFiles:
                fileString_ = fileString_.replace('\\', '/')
                dic.setdefault(sceneStage, []).append(fileString_)
    #
    return dic


#
def getScAstExtraCacheDic(projectName, sceneName, sceneVariant, assetName, number):
    dic = bscCore.orderedDict()
    #
    cacheFile = scAstRigExtraAlembicCacheFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        sceneName, sceneVariant,
        assetName, number
    )[1]
    #
    base, ext = bscMethods.OsFile.toExtSplit(cacheFile)
    #
    osFiles = bscCore.glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
    if osFiles:
        for fileString_ in osFiles:
            fileString_ = fileString_.replace('\\', '/')
            dic.setdefault(prsMethods.Asset.rigLinkName(), []).append(fileString_)
    #
    return dic


#
def getScAstCfxFurCacheDic(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, furObjectType):
    dic = bscCore.orderedDict()
    #
    cacheFile = None
    if furObjectType == appCfg.MaNodeType_Plug_Yeti:
        cacheFile = scAstCfxYetiCacheFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName,
            sceneName, sceneVariant,
            assetName, number, assetVariant, furObjectLabel
        )[1]
    elif furObjectType == appCfg.MaHairSystemType:
        cacheFile = scAstCfxGeomCacheFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName,
            sceneName, sceneVariant,
            assetName, number, assetVariant, furObjectLabel
        )[1]
    elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
        cacheFile = scAstCfxNurbsHairCacheFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName,
            sceneName, sceneVariant,
            assetName, number, assetVariant, furObjectLabel
        )[1]
    if cacheFile:
        fileDirectory, osFileBasename = bscMethods.OsFile.dirname(cacheFile), bscMethods.OsFile.basename(cacheFile)
        #
        fileDirectorys = bscCore.glob.glob(fileDirectory + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]')
        if fileDirectorys:
            for fileDirectory in fileDirectorys:
                fileDirectory = fileDirectory.replace('\\', '/')
                fileString_ = bscMethods.OsPath.composeBy(fileDirectory, osFileBasename)
                dic.setdefault(prsMethods.Asset.groomLinkName(), []).append(fileString_)
    return dic


#
def getScAstCfxFurCacheTimeTag(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    fileString_ = getScAstCfxFurCache(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel)
    return bscMethods.OsFile.findTimetag(fileString_)


#
def getScAstCfxYetiCacheExists(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    def getFrame(cachePerFrame):
        string = cachePerFrame[-8:-4]
        if string.isdigit():
            frame = int(string)
            return frame
    #
    keyword = '.%04d.fur'
    ext = '.fur'
    #
    cache = none
    solverMode = 'On'
    startFrame = 0
    endFrame = 0
    #
    cacheFile = getScAstCfxFurCache(
        projectName,
        sceneName, sceneVariant,
        assetName, number, assetVariant,
        furObjectLabel
    )
    #
    if cacheFile:
        if cacheFile.endswith(ext):
            if cacheFile.endswith(keyword):
                base = cacheFile[:-len(keyword)]
                caches = bscCore.glob.glob(base + '.[0-9][0-9][0-9][0-9]' + ext)
                if caches:
                    cache = cacheFile
                    startCache = caches[0]
                    startFrame = getFrame(startCache)
                    #
                    endCache = caches[-1]
                    endFrame = getFrame(endCache)
    #
    return cache, solverMode, startFrame, endFrame


#
def getScAstCfxGeomCacheExists(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    solverModeDic = {'0': 'Off', '1': 'Static', '2': 'Dynamic Follicle Only', '3': 'All Follicle'}
    cacheExtDic = dict(mcc='.mc', mcx='.mcx')
    ext = '.xml'
    #
    cache = none
    solverMode = 'Static'
    startFrame = 0
    endFrame = 0
    #
    xmlFile = getScAstCfxFurCache(
        projectName,
        sceneName, sceneVariant,
        assetName, number, assetVariant,
        furObjectLabel
    )
    #
    if xmlFile:
        if xmlFile.endswith(ext):
            if bscMethods.OsFile.isExist(xmlFile):
                with open(xmlFile, 'r') as f:
                    lines = f.readlines()
                    f.close()
                    if lines:
                        cacheType = 'OneFile'
                        cacheFormat = 'mcx'
                        solverIndex = 1
                        startTime = 0
                        endTime = 0
                        timePerFrame = 1
                        # Get XML
                        for line in lines:
                            if '<cacheType' in line:
                                cacheType = line.split('=')[1][1:-8]
                                cacheFormat = line.split('=')[-1][1:-4]
                            if '.simulationMethod' in line:
                                solverIndex = line.split('=')[-1][:1]
                            if '<time Range' in line:
                                startTime, endTime = line.split('=')[-1][1:-4].split('-')
                            if '<cacheTimePerFrame' in line:
                                timePerFrame = line.split('=')[-1][1:-4]
                        # Check Exists
                        if cacheType == 'OneFile':
                            base, ext = bscMethods.OsFile.toExtSplit(xmlFile)
                            cacheFile = base + cacheExtDic[cacheFormat]
                            if bscMethods.OsFile.isExist(cacheFile):
                                cache = xmlFile
                                solverMode = solverModeDic[solverIndex]
                                startFrame = int(startTime) / int(timePerFrame)
                                endFrame = int(endTime) / int(timePerFrame)
    #
    return cache, solverMode, startFrame, endFrame


#
def getScAstCfxNurbsHairCacheExists(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    def getFrame(cachePerFrame):
        string = cachePerFrame[-8:-4]
        if string.isdigit():
            frame = int(string)
            return frame
    #
    keyword = '.####.nhr'
    ext = '.nhr'
    #
    cache = none
    solverMode = 'Read'
    startFrame = 0
    endFrame = 0
    #
    cacheFile = getScAstCfxFurCache(
        projectName,
        sceneName, sceneVariant,
        assetName, number, assetVariant,
        furObjectLabel
    )
    #
    if cacheFile:
        if cacheFile.endswith(ext):
            if cacheFile.endswith(keyword):
                base = cacheFile[:-len(keyword)]
                caches = bscCore.glob.glob(base + '.[0-9][0-9][0-9][0-9]' + ext)
                if caches:
                    cache = cacheFile
                    startCache = caches[0]
                    startFrame = getFrame(startCache)
                    #
                    endCache = caches[-1]
                    endFrame = getFrame(endCache)
    #
    return cache, solverMode, startFrame, endFrame


#
def getScAstCfxFurCacheExists(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, furObjectType):
    if furObjectType == appCfg.MaNodeType_Plug_Yeti:
        return getScAstCfxYetiCacheExists(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel)
    elif furObjectType == appCfg.MaHairSystemType:
        return getScAstCfxGeomCacheExists(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel)
    elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
        return getScAstCfxNurbsHairCacheExists(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel)


#
def getMeshDataFile(fileString_):
    ext = bscMethods.OsFile.ext(fileString_)
    return fileString_[:-len(ext)] + prsVariants.Util.dbMeshUnitKey


#
def getScRenderCustomizes(projectName, sceneCategory, sceneName, sceneVariant, sceneStage):
    lis = []
    #
    fileDirectory = scUnitRenderBasicFolder(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        sceneCategory, sceneName, sceneVariant, sceneStage
    )
    #
    if bscMethods.OsDirectory.isExist(fileDirectory):
        subFolders = bscMethods.OsDirectory.basenames(fileDirectory)
        if subFolders:
            for subOsFolder in subFolders:
                renderFile = scUnitRenderFile(
                    prsConfigure.Utility.DEF_value_root_server,
                    projectName, sceneCategory, sceneName, sceneVariant, sceneStage, subOsFolder
                )[1]
                if bscMethods.OsFile.isExist(renderFile):
                    if not subOsFolder in lis:
                        lis.append(subOsFolder)
    #
    return lis


#
def getScRenderIndexData(
        sceneIndex,
        projectName,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        width, height,
        prefix,
        composeFiles,
        imageFiles
):
    dic = bscCore.orderedDict()
    #
    dic[bscConfigure.Utility.DEF_key_info_timestamp] = bscMethods.OsTimestamp.active()
    dic[bscConfigure.Utility.DEF_key_info_username] = bscMethods.OsSystem.username()
    #
    dic[prsVariants.Util.basicIndexAttrLabel] = sceneIndex
    dic[prsVariants.Util.basicProjectAttrLabel] = projectName
    dic[prsVariants.Util.basicClassAttrLabel] = sceneCategory
    dic[prsVariants.Util.basicNameAttrLabel] = sceneName
    dic[prsVariants.Util.basicVariantAttrLabel] = sceneVariant
    dic[prsVariants.Util.basicStageAttrLabel] = sceneStage
    dic[prsVariants.Util.basicStartFrameAttrLabel] = startFrame
    dic[prsVariants.Util.basicEndFrameAttrLabel] = endFrame
    dic[prsVariants.Util.basicWidthAttrLabel] = width
    dic[prsVariants.Util.basicHeightAttrLabel] = height
    #
    dic['prefix'] = prefix
    dic['compose'] = composeFiles
    dic['image'] = imageFiles
    return dic


#
def getScRenderImageData(projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize):
    indexFile = sceUnitRenderIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    if bscMethods.OsFile.isExist(indexFile):
        data = bscMethods.OsJson.read(indexFile)
        image = data['image']
        prefix = data['prefix']
        #
        return prefix, image


#
def getScRenderCompose(projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize):
    indexFile = sceUnitRenderIndexFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    if bscMethods.OsFile.isExist(indexFile):
        data = bscMethods.OsJson.read(indexFile)
        compose = data['compose']
        #
        return compose


#
def getScTdUploadCommand(projectName, link):
    dataDic = prsMethods.Project.mayaTdPresetDict(projectName)
    if dataDic:
        if link in dataDic:
            data = dataDic[link]
            if data:
                mayaPackageStr = data[prsConfigure.Utility.LynxiMayaScriptKey]
                #
                var = ''
                pathCmd = bscMethods.Variant.covertTo('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if bscMethods.OsDirectory.isExist(var):
                        fileString_ = var + '/' + prsConfigure.Utility.LynxiSceneUploadCommandKey + '.py'
                        if bscMethods.OsFile.isExist(fileString_):
                            command = bscMethods.OsFile.read(fileString_)
                            pythonCommand = 'python(' + bscMethods.OsJson.dump(command) + ');'
                            #
                            return pythonCommand


#
def getScTdLoadCommand(projectName, link):
    dataDic = prsMethods.Project.mayaTdPresetDict(projectName)
    if dataDic:
        if link in dataDic:
            data = dataDic[link]
            if data:
                mayaPackageStr = data[prsConfigure.Utility.LynxiMayaScriptKey]
                #
                var = ''
                pathCmd = bscMethods.Variant.covertTo('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if bscMethods.OsDirectory.isExist(var):
                        fileString_ = var + '/' + prsConfigure.Utility.LynxiSceneLoadCommandKey + '.py'
                        if bscMethods.OsFile.isExist(fileString_):
                            command = bscMethods.OsFile.read(fileString_)
                            pythonCommand = 'python(' + bscMethods.OsJson.dump(command) + ');'
                            #
                            return pythonCommand
