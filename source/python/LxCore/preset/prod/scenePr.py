# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
from LxCore.config import appCfg, sceneCfg
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import projectPr, assetPr, sceneryPr
# do not delete and rename
serverBasicPath = lxConfigure.Root().root()
localBasicPath = lxConfigure.Root().userRoot()
#
none = ''


# Group Name Config
def scSceneNameSet(sceneName, subLabel):
    nameSet = '%s_%s%s' % (appVariant.Lynxi_Prefix_Product_Scene, sceneName, subLabel)
    return nameSet


# Group Name Config
def scSceneSubNameSet(sceneName, sceneVariant, subLabel):
    nameSet = '%s_%s_%s%s' % (appVariant.Lynxi_Prefix_Product_Scene, sceneName, sceneVariant, subLabel)
    return nameSet


# Group Name Config
def scGroupNameSet(sceneName, groupNameLabel):
    nameSet = '%s_%s%s%s' % (appVariant.Lynxi_Prefix_Product_Scene, sceneName, groupNameLabel, appVariant.basicGroupLabel)
    return nameSet


# Group Name Config
def scSubGroupNameSet(sceneName, sceneVariant, groupNameLabel):
    nameSet = '%s_%s_%s%s%s' % (appVariant.Lynxi_Prefix_Product_Scene, sceneName, sceneVariant, groupNameLabel, appVariant.basicGroupLabel)
    return nameSet


#
def sceneFullName(sceneName, sceneVariant):
    nameSet = '%s_%s_%s' % (appVariant.Lynxi_Prefix_Product_Scene, sceneName, sceneVariant)
    return nameSet


#
def scAstName(assetName, number, assetVariant):
    nameSet = '%s_%s_%s_%s' % (appVariant.Lynxi_Prefix_Product_Asset, assetName, number, assetVariant)
    return nameSet


#
def scComposeRootGroupName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, appVariant.basicComposeRootGroupLabel)
    return string


#
def scUnitRootGroupName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, appVariant.basicUnitRootGroupLabel)
    return string


#
def scCameraBranchName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, appVariant.basicScCameraGroupLabel)
    return string


#
def scAstBranchName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, appVariant.basicScAstGroupLabel)
    return string


#
def scSceneryBranchName(sceneName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scGroupNameSet(sceneName, appVariant.basicScSceneryGroupLabel)
    return string


#
def scRootGroupHierarchyConfig(sceneName):
    dic = lxBasic.orderedDict()
    dic[scUnitRootGroupName(sceneName)] = []
    return dic


#
def getScLinkGroupLabel(sceneStage):
    string = appVariant.basicLayoutLinkGroupLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.basicLayoutLinkGroupLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.basicAnimationLinkGroupLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.basicSolverLinkGroupLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.basicSimulationLinkGroupLabel
    elif isScLightLink(sceneStage):
        string = appVariant.basicLightLinkGroupLabel
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
    string = [none, namespace + ':'][namespace is not none] + sceneFullName(sceneName, sceneVariant) + '_%s_%s%s' % (assetName, number, appVariant.basicGroupLabel)
    return string


#
def scAstRootGroupPath(sceneName, sceneVariant, assetName, number, namespace=none):
    return scAstBranchName(sceneName, namespace) + '|' + scAstRootGroupName(sceneName, sceneVariant, assetName, number, namespace)


#
def scAstModelGroupName(sceneName, sceneVariant, assetName, number, namespace=none):
    scAstRootGroup = scAstRootGroupName(sceneName, sceneVariant, assetName, number, namespace)
    astUnitRootGroup = assetPr.astUnitRootGroupName(assetName)
    assetModelGroupName = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    string = '|'.join([scAstRootGroup, astUnitRootGroup, assetModelGroupName])
    return string


#
def scAstGeometryGroupName(sceneName, sceneVariant, assetName, number, namespace=none):
    scAstRootGroup = scAstRootGroupName(sceneName, sceneVariant, assetName, number, namespace)
    astUnitRootGroup = assetPr.astUnitRootGroupName(assetName)
    astModelGroup = assetPr.astUnitModelLinkGroupName(assetName, namespace)
    astGeometryGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
    string = '|'.join([scAstRootGroup, astUnitRootGroup, astModelGroup, astGeometryGroup])
    return string


#
def scLinkHierarchyConfig(sceneName, sceneVariant, sceneStage):
    dic = lxBasic.orderedDict()
    # Main
    dic[scUnitLinkGroupName(sceneName, sceneVariant, sceneStage)] = [
        scCameraBranchName(sceneName),
        scAstBranchName(sceneName),
        scSceneryBranchName(sceneName)
    ]
    return dic


#
def sceneSchemeFileConfig():
    string = '{0}/{1}/{2}/{3}'.format(appVariant.dbSceneRoot, appVariant.dbBasicFolderName, lxConfigure.LynxiSchemeExt, appVariant.dbSceneBasicKey)
    return lxBasic.getOsUniqueFile(string)


#
def sceneSetFileConfig(sceneIndex):
    string = '{0}/{1}/{2}/{3}'.format(appVariant.dbSceneRoot, appVariant.dbBasicFolderName, lxConfigure.LynxiSetExt, sceneIndex)
    return string


#
def defaultSceneSchemeConfig():
    lis = [
        True,
        u'000 - 000'
    ]
    return lis


#
def defaultSceneSetConfig(projectName, number=0):
    lis = [
        [('project', u'项目 ( Project(s) )'), (projectName, )],
        #
        [(lxConfigure.LynxiInfoKey_Class, u'类型 ( Classification )'), sceneCfg.scBasicClass()],
        [('name', u'名字 ( Name )'), 'ID{}'.format(str(number).zfill(6))],
        [('variant', u'变体 ( Variant(s) )'), (appVariant.scnDefaultVariant, )],
        [('priority', u'优先级 ( Priority )'), sceneCfg.basicScenePriorityLis()],
        #
        [('scenery', u'场景 ( Scenery )'), sceneryPr.getUiSceneryMultMsgs(projectName, 'scenery')],
        #
        [('layout', u'镜头预览 ( Layout )'), False],
        [('animation', u'镜头动画 ( Animation )'), False],
        [(lxConfigure.LynxiProduct_Scene_Link_Solver, u'镜头模拟 ( Solver )'), False],
        [(lxConfigure.LynxiProduct_Scene_Link_Simulation, u'镜头解算 ( Simulation )'), False],
        [('light', u'镜头灯光 ( Light )'), False]
    ]
    return lis


# Scheme Data
def getUiSceneSchemeDataDic():
    def getCustomData():
        osFile = sceneSchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for i in data:
                scheme, enabled, description = i
                dic[scheme] = enabled, description
        return dic
    #
    return getDic(getCustomData())


#
def getUiSceneSetDataLis(projectName, sceneIndex, number=0, overrideNumber=False):
    def getDefaultData():
        return defaultSceneSetConfig(projectName, number)
    #
    def getCustomData():
        osFile = sceneSetFileConfig(sceneIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getDic(defaultLis, customDic):
        lis = []
        if defaultLis:
            for i in defaultLis:
                setKey, uiData = i
                # Key
                setUiKey = none
                if isinstance(setKey, str) or isinstance(setKey, unicode):
                    setUiKey = lxBasic._toStringPrettify(setKey)
                elif isinstance(setKey, tuple):
                    setKey, setUiKey = setKey
                # Value
                defValue = uiData
                setValue = uiData
                if isinstance(uiData, list):
                    defValue = uiData[0]
                    setValue = uiData[0]
                elif isinstance(uiData, dict):
                    defValue = uiData.values()[0][0]
                    setValue = uiData.values()[0][0]
                #
                if customDic:
                    if setKey in customDic:
                        setValue = customDic[setKey]
                    else:
                        if setKey == 'name':
                            setValue = 'ID{}'.format(str(number).zfill(6))
                #
                lis.append(
                    (setKey, setUiKey, setValue, defValue, uiData)
                )
        return lis
    #
    return getDic(getDefaultData(), getCustomData())


#
def getSceneViewName(sceneIndex):
    def getCustomData():
        osFile = sceneSchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getSubDic(data):
        dic = lxBasic.orderedDict()
        if data:
            for i in data:
                scheme, enabled, description = i
                dic[scheme] = description
        return dic
    #
    def getMain(customDic):
        string = lxConfigure.LynxiValue_Unspecified
        if sceneIndex in customDic:
            string = customDic[sceneIndex]
        return string
    #
    return getMain(getSubDic(getCustomData()))


#
def getSceneClass(sceneIndex):
    def getCustomData():
        osFile = sceneSetFileConfig(sceneIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic[lxConfigure.LynxiInfoKey_Class]
    #
    return getMain(getCustomData())


#
def getSceneName(sceneIndex):
    def getCustomData():
        osFile = sceneSetFileConfig(sceneIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['name']
    #
    return getMain(getCustomData())


#
def getScenePriority(sceneIndex):
    def getCustomData():
        osFile = sceneSetFileConfig(sceneIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['priority']
    #
    return getMain(getCustomData())


#
def getSceneVariants(sceneIndex):
    def getCustomData():
        osFile = sceneSetFileConfig(sceneIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic[lxConfigure.LynxiInfoKey_Variant]
    #
    return getMain(getCustomData())


#
def getSceneLinkEnabled(sceneIndex, link):
    def getCustomData():
        osFile = sceneSetFileConfig(sceneIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic[link]
    #
    return getMain(getCustomData())


#
def sceneViewInfoSet(sceneViewName, sceneClass, sceneVariant):
    string = u'{} {} ( {} )'.format(
        sceneCfg.scBasicViewClassDic(sceneClass)[1],
        sceneViewName,
        sceneVariant
    )
    return string


#
def sceneViewEnInfoSet(sceneViewName, sceneClass, sceneVariant):
    string = '{} {} ( {} )'.format(
        lxBasic._toStringPrettify(sceneClass),
        sceneViewName,
        sceneVariant
    )
    return string


#
def getSceneViewInfo(sceneIndex, sceneClass, sceneVariant):
    return sceneViewInfoSet(getSceneViewName(sceneIndex), sceneClass, sceneVariant)


#
def getSceneEnViewInfo(sceneIndex, sceneClass, sceneVariant):
    return sceneViewEnInfoSet(getSceneViewName(sceneIndex), sceneClass, sceneVariant)


#
def getSceneIndexesFilter(projectFilter, sceneClassFilters=None):
    def getCustomData():
        osFile = sceneSchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getBranch(lis, sceneIndex):
        osFile = sceneSetFileConfig(sceneIndex)
        data = lxBasic.readOsJson(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                dbSceneClass = data[lxConfigure.LynxiInfoKey_Class]
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
        osFile = sceneSchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getLinks(data):
        lis = []
        for i in sceneCfg.basicSceneLinkLis():
            enabled = data[i]
            if enabled is True:
                lis.append(i)
        return lis
    #
    def getBranch(dic, sceneIndex, description):
        osFile = sceneSetFileConfig(sceneIndex)
        data = lxBasic.readOsJson(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                isFilter = False
                #
                dbSceneClass = data[lxConfigure.LynxiInfoKey_Class]
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
        dic = lxBasic.orderedDict()
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
        osFile = sceneSchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getBranch(dic, sceneIndex, description):
        osFile = sceneSetFileConfig(sceneIndex)
        data = lxBasic.readOsJson(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                sceneClass = data[lxConfigure.LynxiInfoKey_Class]
                sceneName = data['name']
                sceneVariants = data['variant']
                scenePriority = data['priority']
                scLayoutEnable = data['layout']
                scAnimationEnable = data['animation']
                scSolverEnable = data[lxConfigure.LynxiProduct_Scene_Link_Solver]
                scSimulationEnable = data['simulation']
                scLightEnable = data['light']
                for sceneVariant in sceneVariants:
                    dic[(sceneIndex, sceneVariant)] = description, sceneClass, sceneName, scenePriority, scLayoutEnable, scAnimationEnable, scSolverEnable, scSimulationEnable, scLightEnable
    #
    def getMain(data):
        dic = lxBasic.orderedDict()
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
        return startFrame - appVariant.animKeyFrameOffset


# End Frame Set
def scEndFrame(endFrame, keyFrameOffset=None):
    if keyFrameOffset:
        return endFrame + keyFrameOffset
    else:
        return endFrame + appVariant.animKeyFrameOffset


#
def previewIndexData(linkFile):
    dic = lxBasic.orderedDict()
    dic[lxConfigure.Lynxi_Key_Info_Update] = lxBasic.getOsActiveTimestamp()
    dic[lxConfigure.Lynxi_Key_Info_Artist] = lxBasic.getOsUser()
    dic[lxConfigure.Lynxi_Key_Info_SourceFile] = linkFile
    return dic


#
def alembicCacheInfoDic(sceneStage, startFrame, endFrame, step, description=None, notes=None):
    return {
        lxConfigure.Lynxi_Key_Info_Update: lxBasic.getOsActiveTimestamp(),
        lxConfigure.Lynxi_Key_Info_Artist: lxBasic.getOsUser(),
        #
        lxConfigure.Lynxi_Key_Info_Description: description,
        lxConfigure.Lynxi_Key_Info_Note: notes,
        #
        lxConfigure.Lynxi_Key_Info_Stage: sceneStage,
        #
        'startFrame': startFrame,
        'endFrame': endFrame,
        'step': step
    }


# Get Dict For Animation Camera Cache's Link
def geomCacheIndexData(sceneStage, startFrame, endFrame, step, cacheIndex, timeTag):
    dic = lxBasic.orderedDict()
    dic[lxConfigure.Lynxi_Key_Info_Update] = lxBasic.getOsActiveTimestamp()
    dic[lxConfigure.Lynxi_Key_Info_Artist] = lxBasic.getOsUser()
    #
    dic[lxConfigure.Lynxi_Key_Info_Stage] = sceneStage
    dic[lxConfigure.Lynxi_Key_Info_Version] = timeTag
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
    dic = lxBasic.orderedDict()
    #
    dic[lxConfigure.Lynxi_Key_Info_Update] = lxBasic.getOsActiveTimestamp()
    dic[lxConfigure.Lynxi_Key_Info_Artist] = lxBasic.getOsUser()
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
    string = scSceneSubNameSet(sceneName, sceneVariant, appVariant.scCameraNodeLabel)
    return string


#
def scOutputCameraName(sceneName, sceneVariant, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scSceneSubNameSet(sceneName, sceneVariant, appVariant.scOutputCameraNodeLabel)
    return string


# Camera Locator Name
def scOutputCameraLocatorName(sceneName, sceneVariant, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scSceneSubNameSet(sceneName, sceneVariant, appVariant.scCameraLocatorNodeLabel)
    return string


# Adjust Locator Name
def scOutputCameraSubLocatorName(sceneName, sceneVariant, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scSceneSubNameSet(sceneName, sceneVariant, appVariant.scCameraSubLocatorNodeLabel)
    return string


#
def scRenderSize():
    return appVariant.rndrImageWidth, appVariant.rndrImageHeight


#
def isScLayoutLink(sceneStage):
    boolean = False
    if sceneStage in lxConfigure.LynxiScLayoutStages or sceneStage == lxConfigure.LynxiProduct_Scene_Link_layout:
        boolean = True
    return boolean


#
def isScAnimationLink(sceneStage):
    boolean = False
    if sceneStage in lxConfigure.LynxiScAnimationStages or sceneStage == lxConfigure.LynxiProduct_Scene_Link_Animation:
        boolean = True
    return boolean


#
def isScSolverLink(sceneStage):
    boolean = False
    if sceneStage in lxConfigure.LynxiScSolverStages or sceneStage == lxConfigure.LynxiProduct_Scene_Link_Solver:
        boolean = True
    return boolean


#
def isScSimulationLink(sceneStage):
    boolean = False
    if sceneStage in lxConfigure.LynxiScSimulationStages or sceneStage == lxConfigure.LynxiProduct_Scene_Link_Simulation:
        boolean = True
    return boolean


#
def isScLightLink(sceneStage):
    boolean = False
    if sceneStage in lxConfigure.LynxiScLightStages or sceneStage == lxConfigure.LynxiProduct_Scene_Link_Light:
        boolean = True
    return boolean


#
def getSceneLink(sceneStage):
    link = lxConfigure.LynxiProduct_Scene_Link_layout
    if isScLayoutLink(sceneStage):
        link = lxConfigure.LynxiProduct_Scene_Link_layout
    elif isScAnimationLink(sceneStage):
        link = lxConfigure.LynxiProduct_Scene_Link_Animation
    elif isScSolverLink(sceneStage):
        link = lxConfigure.LynxiProduct_Scene_Link_Solver
    elif isScSimulationLink(sceneStage):
        link = lxConfigure.LynxiProduct_Scene_Link_Simulation
    elif isScLightLink(sceneStage):
        link = lxConfigure.LynxiProduct_Scene_Link_Light
    return link


#
def scBasicLinkLabel(sceneStage):
    string = appVariant.scLayoutLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightLabel
    return string


#
def sceneLinkFolder(sceneStage):
    string = appVariant.scLayoutFolder
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutFolder
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationFolder
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverFolder
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationFolder
    elif isScLightLink(sceneStage):
        string = appVariant.scLightFolder
    return string


#
def sceneSourceFileLabel(sceneStage):
    string = appVariant.scLayoutSourceLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutSourceLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationSourceLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverSourceLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationSourceLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightSourceLabel
    return string


#
def sceneProductFileLabel(sceneStage):
    string = appVariant.scLayoutProductLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutProductLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationProductLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverProductLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationProductLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightProductLabel
    return string


#
def sceneExtraFileLabel(sceneStage):
    string = appVariant.scLayoutExtraLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutExtraLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationExtraLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverExtraLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationExtraLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightExtraLabel
    return string


#
def sceneRenderFileLabel(sceneStage):
    string = appVariant.scLayoutRenderLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutRenderLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationRenderLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverRenderLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationRenderLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightRenderLabel
    return string


#
def sceneCameraFileLabel(sceneStage):
    string = appVariant.scLayoutCameraLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutCameraLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationCameraLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverCameraLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationCameraLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightCameraLabel
    return string


#
def sceneSoundFileLabel(sceneStage):
    return scBasicLinkLabel(sceneStage) + appVariant.scSoundLabel.upper()


#
def sceneAssetFileLabel(sceneStage):
    string = appVariant.scLayoutAssetLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutAssetLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationAssetLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverAssetLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationAssetLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightAssetLabel
    return string


#
def scAstSolverFileLabel(sceneStage):
    subLabel = appVariant.basicSolverSubLabel
    return lxBasic.getComposeLabel(scBasicLinkLabel(sceneStage), subLabel)


#
def sceneSceneryFileLabel(sceneStage):
    string = appVariant.scLayoutSceneryLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutSceneryLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationSceneryLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverSceneryLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationSceneryLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightSceneryLabel
    return string


#
def scenePreviewFileLabel(sceneStage):
    string = appVariant.scLayoutPreviewLabel
    if isScLayoutLink(sceneStage):
        string = appVariant.scLayoutPreviewLabel
    elif isScAnimationLink(sceneStage):
        string = appVariant.scAnimationPreviewLabel
    elif isScSolverLink(sceneStage):
        string = appVariant.scSolverPreviewLabel
    elif isScSimulationLink(sceneStage):
        string = appVariant.scSimulationPreviewLabel
    elif isScLightLink(sceneStage):
        string = appVariant.scLightPreviewLabel
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
    return scSceneSubNameSet(sceneName, sceneVariant, appVariant.scCameraNodeLabel)


#
def sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number):
    if sceneName and sceneVariant:
        string = sceneFullName(sceneName, sceneVariant) + '_%s_%s' % (assetName, number)
    else:
        string = '%s_%s_%s' % (appVariant.Lynxi_Prefix_Product_Asset, assetName, number)
    return string


# Model Product
def scAstModelNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scModelNodeLabel


# Model Cache
def scAstModelCacheNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scCacheNodeLabel


# Model
def scAstModelReferenceNode(sceneName, sceneVariant, assetName, number):
    return scAstModelNamespace(sceneName, sceneVariant, assetName, number) + appCfg.MaRN


# Rig
def scAstRigNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scRigNodeLabel


# Rig Reference Node
def scAstRigReferenceNode(sceneName, sceneVariant, assetName, number):
    return scAstRigNamespace(sceneName, sceneVariant, assetName, number) + appCfg.MaRN


# CFX
def scAstCfxNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.basicCharacterFxLinkLabel


#
def scAstSimulationNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.basicSimulationLinkLabel


# Model
def scAstModelDisplayLayer(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scModelNodeLabel + appVariant.displayLayerLabel


# CFX
def scAstCfxDisplayLayer(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scCfxNodeLabel + appVariant.displayLayerLabel


#
def scAstCfxReferenceNode(sceneName, sceneVariant, assetName, number):
    return scAstCfxNamespace(sceneName, sceneVariant, assetName, number) + appCfg.MaRN


# Solver
def scAstSolverNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scSolverNodeLabel


# Solver Cache
def scAstSolverCacheNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scSolverCacheNodeLabel


# Solver Cache
def scAstSolverCacheReferenceNode(sceneName, sceneVariant, assetName, number):
    return scAstSolverCacheNamespace(sceneName, sceneVariant, assetName, number) + appCfg.MaRN


# Extra
def scAstExtraNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scExtraNodeLabel


# Extra
def scAstExtraCacheNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scExtraCacheNodeLabel


#
def sceneAssetCfxUnitNamespace(sceneName, sceneVariant, assetName, number):
    return sceneAssetUnitNamespace(sceneName, sceneVariant, assetName, number) + appVariant.scCfxNodeLabel


#
def sceneUnitBasicDirectory(rootIndexKey, projectName):
    root = [appVariant.serverSceneRoot, appVariant.localSceneRoot, appVariant.backupSceneRoot]
    return '%s/%s/%s/%s' % (root[rootIndexKey], projectName, appVariant.basicSceneFolder, appVariant.scUnitFolder)


#
def sceneUnitCacheBasicDirectory(rootIndexKey, projectName):
    root = [appVariant.serverGeomCacheRoot, appVariant.localGeomCacheRoot, appVariant.backupGeomCacheRoot]
    return '%s/%s/%s' % (root[rootIndexKey], projectName, appVariant.basicCacheFolder)


#
def sceneUnitRenderBasicDirectory(rootIndexKey, projectName):
    root = [appVariant.serverRenderRoot, appVariant.localRenderRoot, appVariant.backupRenderRoot]
    return '%s/%s/%s' % (root[rootIndexKey], projectName, appVariant.basicRenderFolder)


#
def sceneUnitFolder(rootIndexKey, projectName, sceneClass, sceneName):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    osPath = '%s/%s' % (
        basicDirectory,
        sceneName
    )
    return osPath


# Geometry Cache
def scUnitIndexFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    fileLabel = none
    extLabel = appVariant.scSceneIndexExt
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    osFile = '%s/%s/%s/%s' % (
        basicDirectory,
        sceneName, sceneVariant,
        osFileName
    )
    return osFileName, osFile


#
def sceneUnitSourceFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneSourceFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.mayaAsciiExt)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def sceneUnitProductFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneProductFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.mayaAsciiExt)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def sceneExtraFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
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
def scUnitCameraProductFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneCameraFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.mayaAsciiExt)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scUnitCameraFbxFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneCameraFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.fbxExt)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scenePreviewFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, extLabel=appVariant.aviExt):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = scenePreviewFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def sceneSoundFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneSoundFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.mayaAsciiExt)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scenePreviewIndexFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = none
    extLabel = appVariant.scPreviewIndexExt
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


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
        appVariant.cacheCameraFolder
    )
    return osFolder


#
def scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant):
    basicDirectory = sceneUnitCacheBasicDirectory(rootIndexKey, projectName)
    #
    osFolder = '{0}/{1}/{2}/{3}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        appVariant.cacheAssetFolder
    )
    return osFolder


#
def scUnitSceneryExtraFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = sceneSceneryFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.dbExtraUnitKey)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scAssemblyLabel(sceneStage):
    subLabel = appVariant.basicAssemblySubLabel
    return lxBasic.getComposeLabel(scBasicLinkLabel(sceneStage), subLabel)


#
def scUnitAssemblyComposeFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    basicDirectory = sceneUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneLinkFolder(sceneStage)
    fileLabel = scAssemblyLabel(sceneStage)
    extLabel = appVariant.assemblyComposeExt
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant):
    basicDirectory = sceneUnitCacheBasicDirectory(rootIndexKey, projectName)
    #
    osFolder = '{0}/{1}/{2}/{3}'.format(
        basicDirectory,
        sceneName, sceneVariant,
        appVariant.cacheSimulationFolder
    )
    return osFolder


#
def scCameraCacheIndexFile(rootIndexKey, projectName, sceneName, sceneVariant):
    fileLabel = none
    extLabel = appVariant.scGeomCacheIndexExt
    #
    osFolder = scCameraCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    #
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


#
def scUnitCameraAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, sceneStage):
    fileLabel = sceneCameraFileLabel(sceneStage)
    extLabel = appVariant.alembicCacheExt
    #
    osFolder = scCameraCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, extLabel)
    #
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


#
def scAstCacheIndexFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number):
    fileLabel = none
    extLabel = appVariant.scGeomCacheIndexExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


#
def scAstModelAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, sceneStage, assetName, number):
    fileLabel = sceneAssetFileLabel(sceneStage)
    extLabel = appVariant.alembicCacheExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


#
def scAstRigExtraAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number):
    fileLabel = appVariant.scAstRigExtraLabel
    extLabel = appVariant.alembicCacheExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


#
def scAstModelPoseAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number):
    fileLabel = appVariant.scAstModelPoseLabel
    extLabel = appVariant.alembicCacheExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


#
def scAstSolverAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, sceneStage, assetName, number):
    fileLabel = scAstSolverFileLabel(sceneStage)
    extLabel = appVariant.alembicCacheExt
    #
    osFolder = scAstAlembicCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstFileNameConfig(assetName, number, fileLabel, extLabel)
    #
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


#
def scAstCfxFurCacheIndexFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    fileLabel = none
    extLabel = appVariant.scFurCacheIndexExt
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    osFileName = scAstNodeFileNameConfig(assetName, number, assetVariant, furObjectLabel, fileLabel, extLabel)
    #
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


# Animation Fur Cache Path
def scAstCfxYetiCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, timeTag=None):
    extLabel = '.%04d.fur'
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    if timeTag:
        subLabel = '_' + timeTag
    else:
        subLabel = none
    #
    subFolder = scAstNodeFolderNameConfig(assetName, number, assetVariant, furObjectLabel) + subLabel
    #
    fileName = furObjectLabel + extLabel
    #
    osFile = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder, fileName
    )
    return fileName, osFile


#
def scAstCfxGeomCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, timeTag=None):
    extLabel = '.xml'
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    if timeTag:
        subLabel = '_' + timeTag
    else:
        subLabel = none
    #
    subFolder = scAstNodeFolderNameConfig(assetName, number, assetVariant, furObjectLabel) + subLabel
    #
    fileName = furObjectLabel + extLabel
    #
    osFile = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder, fileName
    )
    return fileName, osFile


#
def scAstCfxAlembicCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, timeTag=None):
    extLabel = appVariant.alembicCacheExt
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    if timeTag:
        subLabel = '_' + timeTag
    else:
        subLabel = none
    #
    subFolder = scAstNodeFolderNameConfig(assetName, number, assetVariant, furObjectLabel) + subLabel
    #
    fileName = furObjectLabel + extLabel
    #
    osFile = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder, fileName
    )
    return fileName, osFile


#
def scAstCfxNurbsHairCacheFile(rootIndexKey, projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, timeTag=None):
    extLabel = '.####.nhr'
    #
    osFolder = scAstSimulationCacheFolder(rootIndexKey, projectName, sceneName, sceneVariant)
    #
    if timeTag:
        subLabel = '_' + timeTag
    else:
        subLabel = none
    #
    subFolder = scAstNodeFolderNameConfig(assetName, number, assetVariant, furObjectLabel) + subLabel
    #
    fileName = furObjectLabel + extLabel
    #
    osFile = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder, fileName
    )
    return fileName, osFile


#
def scUnitIndexDic(sceneIndex, projectName, sceneClass, sceneName, sceneVariant, sceneStage, startFrame, endFrame):
    dic = lxBasic.orderedDict()
    #
    dic[lxConfigure.Lynxi_Key_Info_Update] = lxBasic.getOsActiveTimestamp()
    dic[lxConfigure.Lynxi_Key_Info_Artist] = lxBasic.getOsUser()
    #
    dic[appVariant.basicIndexAttrLabel] = sceneIndex
    dic[appVariant.basicProjectAttrLabel] = projectName
    dic[appVariant.basicClassAttrLabel] = sceneClass
    dic[appVariant.basicNameAttrLabel] = sceneName
    dic[appVariant.basicVariantAttrLabel] = sceneVariant
    dic[appVariant.basicStageAttrLabel] = sceneStage
    dic[appVariant.basicStartFrameAttrLabel] = startFrame
    dic[appVariant.basicEndFrameAttrLabel] = endFrame
    return dic


#
def scUnitCameraIndexDic(cameraData):
    return {appVariant.basicCameraAttrLabel: cameraData}


#
def scUnitAssetIndexDic(assetData):
    return {appVariant.basicAssetAttrLabel: assetData}


#
def scUnitSceneryIndexDic(sceneryData):
    return {appVariant.basicSceneryAttrLabel: sceneryData}


#
def scUnitRenderBasicFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage):
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
def scUnitRenderFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize=None):
    basicFolder = scUnitRenderBasicFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage)
    #
    if not customize:
        customize = appVariant.scDefaultCustomizeLabel
    #
    osFolder = '{0}/{1}'.format(
        basicFolder,
        customize,
    )
    return osFolder


#
def scUnitRenderImageFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize=None):
    basicFolder = scUnitRenderBasicFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage)
    #
    if not customize:
        customize = appVariant.scDefaultCustomizeLabel
        #
    #
    osFolder = '{0}/{1}/{2}'.format(
        basicFolder,
        customize,
        'images'
    )
    return osFolder


#
def scUnitRenderFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize):
    osFolder = scUnitRenderFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize)
    #
    fileLabel = sceneRenderFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.mayaAsciiExt)
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


#
def sceUnitRenderIndexFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize):
    osFolder = scUnitRenderFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize)
    #
    fileLabel = sceneRenderFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.scRenderIndexExt)
    osFile = '{0}/{1}'.format(
        osFolder,
        osFileName
    )
    return osFileName, osFile


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
def scDeadlineInfoFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize):
    osFolder = scUnitRenderFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize)
    subFolder = '.'.join([appVariant.basicDeadlineFolder, appVariant.basicMayaFolder])
    #
    fileLabel = sceneRenderFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.scDeadlineInfoExt)
    osFile = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder,
        osFileName
    )
    return osFileName, osFile


# Deadline Job
def scDeadlineJobFile(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize):
    osFolder = scUnitRenderFolder(rootIndexKey, projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize)
    subFolder = '.'.join([appVariant.basicDeadlineFolder, appVariant.basicMayaFolder])
    #
    fileLabel = sceneRenderFileLabel(sceneStage)
    #
    osFileName = scSceneFileNameConfig(sceneName, fileLabel, appVariant.scDeadlineJobExt)
    osFile = '{0}/{1}/{2}'.format(
        osFolder,
        subFolder,
        osFileName
    )
    return osFileName, osFile


#
def getSceneStage(projectName, sceneClass, sceneName, sceneVariant):
    string = lxConfigure.LynxiScLayoutStages[0]
    indexFile = scUnitIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant
    )[1]
    if lxBasic.isOsExistsFile(indexFile):
        data = lxBasic.readOsJson(indexFile)
        string = data[appVariant.basicStageAttrLabel]
    #
    return string


#
def getScUnitFrameRange(projectName, sceneClass, sceneName, sceneVariant):
    startFrame, endFrame = appVariant.animStartFrame, appVariant.animStartFrame + 20
    indexFile = scUnitIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant
    )[1]
    if lxBasic.isOsExistsFile(indexFile):
        data = lxBasic.readOsJson(indexFile)
        startFrame = data[appVariant.basicStartFrameAttrLabel]
        endFrame = data[appVariant.basicEndFrameAttrLabel]
    return startFrame, endFrame


#
def getSceneProductFile(projectName, sceneClass, sceneName, sceneVariant):
    string = none
    sceneStage = getSceneStage(projectName, sceneClass, sceneName, sceneVariant)
    #
    productFile = sceneUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    if lxBasic.isOsExistsFile(productFile):
        string = productFile
    return string


#
def getScUnitPreviewServerFile(projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    string = none
    previewTimeStamp = 0
    for osExt in [appVariant.aviExt, appVariant.movExt]:
        previewFile = scenePreviewFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, sceneClass, sceneName, sceneVariant, sceneStage, osExt
        )[1]
        if lxBasic.isOsExistsFile(previewFile):
            timeStamp = lxBasic.getOsFileMtimestamp(previewFile)
            currentTimeStamp = float(timeStamp)
            if currentTimeStamp > previewTimeStamp:
                string = previewFile
            previewTimeStamp = currentTimeStamp
    return string


#
def getSceneUnitProductUpdate(projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    string = appVariant.infoNonExistsLabel
    #
    serverProductFile = sceneUnitProductFile(
        lxConfigure.LynxiRootIndex_Server, projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    #
    if lxBasic.isOsExistsFile(serverProductFile):
        data = lxBasic.getCnViewTime(lxBasic.getOsFileMtimestamp(serverProductFile))
        if data:
            string = data
    return string


#
def getSceneCameraIndexDataDic(projectName, sceneClass, sceneName, sceneVariant):
    dic = lxBasic.orderedDict()
    # Key File
    indexFile = scUnitIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant
    )[1]
    if lxBasic.isOsExistsFile(indexFile):
        data = lxBasic.readOsJson(indexFile)
        cameraData = data['camera']
        if cameraData:
            osPath = scCameraCacheFolder(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                sceneName, sceneVariant
            )
            for i in cameraData:
                osFileBasename = i + appVariant.scGeomCacheIndexExt
                osFile = lxBasic._toOsFile(osPath, osFileBasename)
                if lxBasic.isOsExistsFile(osFile):
                    cacheIndexData = lxBasic.readOsJson(osFile)
                    dataType = 'camera'
                    timestamp = lxBasic.getOsFileMtimestamp(osFile)
                    sceneStage = cacheIndexData['stage']
                    cache = cacheIndexData[lxConfigure.LynxiCacheInfoKey]
                    #
                    startFrame, endFrame = getScUnitFrameRange(projectName, sceneClass, sceneName, sceneVariant)
                    #
                    dic.setdefault(dataType, []).append((
                        timestamp, sceneStage, startFrame, endFrame, cache
                    ))
    return dic


#
def getOutputCameras(projectName, sceneClass, sceneName, sceneVariant):
    lis = []
    # Key File
    indexFile = scUnitIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant
    )[1]
    if lxBasic.isOsExistsFile(indexFile):
        data = lxBasic.readOsJson(indexFile)
        cameraData = data['camera']
        if cameraData:
            for seq in range(len(cameraData)):
                subLabel = lxBasic.getSubLabel(seq)
                #
                namespace = scCameraNamespace(sceneName, sceneVariant) + subLabel
                #
                outputCamera = scOutputCameraName(sceneName, sceneVariant, namespace) + subLabel
                lis.append(outputCamera)
    return lis


#
def getSceneAssetIndexDataDic(projectName, sceneClass, sceneName, sceneVariant):
    dic = lxBasic.orderedDict()
    # Key File
    indexFile = scUnitIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant
    )[1]
    if lxBasic.isOsExistsFile(indexFile):
        data = lxBasic.readOsJson(indexFile)
        scAstUploadData = data['asset']
        if scAstUploadData:
            osPath = scAstAlembicCacheFolder(
                lxConfigure.LynxiRootIndex_Server,
                projectName, sceneName, sceneVariant
            )
            for i in scAstUploadData:
                assetIndex, assetClass, assetName, number, assetVariant = i
                osFileBasename = scAstFileNameConfig(assetName, number, none, appVariant.scGeomCacheIndexExt)
                osFile = lxBasic._toOsFile(osPath, osFileBasename)
                dataType = 'asset'
                if lxBasic.isOsExistsFile(osFile):
                    cacheIndexData = lxBasic.readOsJson(osFile)
                    timestamp = lxBasic.getOsFileMtimestamp(osFile)
                    sceneStage = cacheIndexData[lxConfigure.Lynxi_Key_Info_Stage]
                    #
                    modelCache = lxBasic.getKeyData(cacheIndexData, lxConfigure.LynxiCacheInfoKey)
                    extraCache = lxBasic.getKeyData(cacheIndexData, lxConfigure.LynxiExtraCacheInfoKey)
                else:
                    timestamp = None
                    sceneStage = None
                    modelCache = None
                    extraCache = None
                #
                startFrame, endFrame = getScUnitFrameRange(projectName, sceneClass, sceneName, sceneVariant)
                #
                dic.setdefault(dataType, []).append((
                    timestamp, sceneStage, startFrame, endFrame,
                    modelCache,
                    assetIndex, assetClass, assetName, number, assetVariant
                ))
    return dic


#
def getScSceneryIndexDataDic(projectName, sceneClass, sceneName, sceneVariant, sceneStage=None):
    dic = lxBasic.orderedDict()
    # Key File
    indexFile = scUnitIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant
    )[1]
    if lxBasic.isOsExistsFile(indexFile):
        data = lxBasic.readOsJson(indexFile)
        key = 'scenery'
        if key in data:
            if sceneStage is None:
                sceneStage = data[lxConfigure.Lynxi_Key_Info_Stage]
            #
            indexDatas = data['scenery']
            if indexDatas:
                for i in indexDatas:
                    sceneryIndex, sceneryClass, sceneryName, sceneryVariant, sceneryStage = i
                    sceneryExtraFile = scUnitSceneryExtraFile(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName, sceneClass, sceneName, sceneVariant, sceneStage
                    )[1]
                    sceneryFile = sceneryPr.scnUnitDefinitionFile(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName, sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiScLayoutStages[0]
                    )[1]
                    timestamp = lxBasic.getOsFileMtimestamp(sceneryExtraFile)
                    dic.setdefault(key, []).append((
                        timestamp,
                        sceneStage,
                        sceneryIndex, sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                        sceneryFile, sceneryExtraFile
                    ))
    return dic


#
def getScSceneryExtraData(projectName, sceneClass, sceneName, sceneVariant):
    dic = lxBasic.orderedDict()
    sceneStage = getSceneStage(
        projectName,
        sceneClass, sceneName, sceneVariant
    )
    extraFile = scUnitSceneryExtraFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    if lxBasic.isOsExistsFile(extraFile):
        data = lxBasic.readOsJson(extraFile)
        if data:
            dic = data
    return dic


#
def getScSceneryAssemblyDic(projectName, sceneClass, sceneName, sceneVariant):
    extraData = getScSceneryExtraData(projectName, sceneClass, sceneName, sceneVariant)
    if lxConfigure.LynxiAssemblyReferenceDataKey in extraData:
        data = extraData[lxConfigure.LynxiAssemblyReferenceDataKey]
        if data:
            for i in data:
                objectPath, definition, namespace = i
                if lxBasic.isOsExistsFile(definition):
                    print definition


#
def getScCameraCacheActive(projectName, sceneName, sceneVariant, subLabel=none):
    key = lxConfigure.LynxiCacheInfoKey
    #
    osFile = scCameraCacheIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneName, sceneVariant
    )[1]
    subOsFile = lxBasic.getOsSubFile(osFile, subLabel)
    cache = appVariant.infoNonExistsLabel
    if lxBasic.isOsExistsFile(subOsFile):
        cacheIndexData = lxBasic.readOsJson(subOsFile)
        if key in cacheIndexData:
            cache = cacheIndexData[key]
    return cache


#
def getScAstModelCacheActive(projectName, sceneName, sceneVariant, assetName, number):
    key = lxConfigure.LynxiCacheInfoKey
    #
    osFile = scAstCacheIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneName, sceneVariant, assetName, number
    )[1]
    cache = appVariant.infoNonExistsLabel
    if lxBasic.isOsExistsFile(osFile):
        cacheIndexData = lxBasic.readOsJson(osFile)
        if key in cacheIndexData:
            cache = cacheIndexData[key]
    return cache


#
def getScAstSolverCacheActive(projectName, sceneName, sceneVariant, assetName, number):
    key = lxConfigure.LynxiSolverCacheInfoKey
    #
    osFile = scAstCacheIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneName, sceneVariant, assetName, number
    )[1]
    #
    cache = appVariant.infoNonExistsLabel
    if lxBasic.isOsExistsFile(osFile):
        cacheIndexData = lxBasic.readOsJson(osFile)
        if key in cacheIndexData:
            cache = cacheIndexData[key]
    return cache


#
def getScAstModelPoseCacheActive(projectName, sceneName, sceneVariant, assetName, number):
    timeTag = '0000_0000_0000'
    cache = scAstModelPoseAlembicCacheFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneName, sceneVariant, assetName, number
    )[1]
    return lxBasic.getOsFileJoinTimeTag(cache, timeTag)


#
def getScAstRigExtraCacheActive(projectName, sceneName, sceneVariant, assetName, number):
    key = lxConfigure.LynxiExtraCacheInfoKey
    #
    osFile = scAstCacheIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneName, sceneVariant, assetName, number
    )[1]
    cache = appVariant.infoNonExistsLabel
    if lxBasic.isOsExistsFile(osFile):
        cacheIndexData = lxBasic.readOsJson(osFile)
        if key in cacheIndexData:
            cache = cacheIndexData[key]
    return cache


#
def getScCameraCacheDic(projectName, sceneName, sceneVariant, subLabel):
    dic = lxBasic.orderedDict()
    #
    sceneStages = [lxConfigure.LynxiProduct_Scene_Link_layout, lxConfigure.LynxiProduct_Scene_Link_Animation, lxConfigure.LynxiProduct_Scene_Link_Simulation]
    for sceneStage in sceneStages:
        cacheFile = scUnitCameraAlembicCacheFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant, sceneStage
        )[1]
        subCacheFile = lxBasic.getOsSubFile(cacheFile, subLabel)
        #
        base, ext = lxBasic.toOsFileSplitByExt(subCacheFile)
        #
        osFiles = lxBasic.glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
        if osFiles:
            for osFile in osFiles:
                osFile = osFile.replace('\\', '/')
                dic.setdefault(sceneStage, []).append(osFile)
    #
    return dic


#
def getScCameraCacheActiveTimeTag(projectName, sceneName, sceneVariant, subLabel=none):
    osFile = getScCameraCacheActive(projectName, sceneName, sceneVariant, subLabel)
    return lxBasic.getOsFileTimeTag(osFile)


#
def getScAstModelCacheActiveTimeTag(projectName, sceneName, sceneVariant, assetName, number):
    osFile = getScAstModelCacheActive(projectName, sceneName, sceneVariant, assetName, number)
    return lxBasic.getOsFileTimeTag(osFile)


#
def getScAstSolverCacheActiveTimeTag(projectName, sceneName, sceneVariant, assetName, number):
    osFile = getScAstSolverCacheActive(projectName, sceneName, sceneVariant, assetName, number)
    return lxBasic.getOsFileTimeTag(osFile)


#
def getScAstRigExtraCacheActiveTimeTag(projectName, sceneName, sceneVariant, assetName, number):
    osFile = getScAstRigExtraCacheActive(projectName, sceneName, sceneVariant, assetName, number)
    return lxBasic.getOsFileTimeTag(osFile)


#
def getScAstCfxFurCache(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    osFile = scAstCfxFurCacheIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneName, sceneVariant, assetName, number, assetVariant,
        furObjectLabel
    )[1]
    furCache = appVariant.infoNonExistsLabel
    if lxBasic.isOsExistsFile(osFile):
        cacheIndexData = lxBasic.readOsJson(osFile)
        furCache = cacheIndexData[lxConfigure.LynxiCacheInfoKey]
    return furCache


#
def getScAstModelCacheDic(projectName, sceneName, sceneVariant, assetName, number):
    dic = lxBasic.orderedDict()
    sceneStages = [lxConfigure.LynxiProduct_Scene_Link_layout, lxConfigure.LynxiProduct_Scene_Link_Animation, lxConfigure.LynxiProduct_Scene_Link_Simulation, lxConfigure.LynxiProduct_Scene_Link_Solver]
    for sceneStage in sceneStages:
        cacheFile = scAstModelAlembicCacheFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant, sceneStage,
            assetName, number
        )[1]
        #
        base, ext = lxBasic.toOsFileSplitByExt(cacheFile)
        #
        osFiles = lxBasic.glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
        if osFiles:
            for osFile in osFiles:
                osFile = osFile.replace('\\', '/')
                dic.setdefault(sceneStage, []).append(osFile)
    #
    return dic


#
def getScAstSolverCacheDic(projectName, sceneName, sceneVariant, assetName, number):
    dic = lxBasic.orderedDict()
    sceneStages = [lxConfigure.LynxiProduct_Scene_Link_layout, lxConfigure.LynxiProduct_Scene_Link_Animation, lxConfigure.LynxiProduct_Scene_Link_Simulation, lxConfigure.LynxiProduct_Scene_Link_Solver]
    for sceneStage in sceneStages:
        cacheFile = scAstSolverAlembicCacheFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant, sceneStage,
            assetName, number
        )[1]
        #
        base, ext = lxBasic.toOsFileSplitByExt(cacheFile)
        #
        osFiles = lxBasic.glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
        if osFiles:
            for osFile in osFiles:
                osFile = osFile.replace('\\', '/')
                dic.setdefault(sceneStage, []).append(osFile)
    #
    return dic


#
def getScAstExtraCacheDic(projectName, sceneName, sceneVariant, assetName, number):
    dic = lxBasic.orderedDict()
    #
    cacheFile = scAstRigExtraAlembicCacheFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneName, sceneVariant,
        assetName, number
    )[1]
    #
    base, ext = lxBasic.toOsFileSplitByExt(cacheFile)
    #
    osFiles = lxBasic.glob.glob(base + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]' + ext)
    if osFiles:
        for osFile in osFiles:
            osFile = osFile.replace('\\', '/')
            dic.setdefault(lxConfigure.LynxiProduct_Asset_Link_Rig, []).append(osFile)
    #
    return dic


#
def getScAstCfxFurCacheDic(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel, furObjectType):
    dic = lxBasic.orderedDict()
    #
    cacheFile = None
    if furObjectType == appCfg.MaNodeType_Plug_Yeti:
        cacheFile = scAstCfxYetiCacheFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant,
            assetName, number, assetVariant, furObjectLabel
        )[1]
    elif furObjectType == appCfg.MaHairSystemType:
        cacheFile = scAstCfxGeomCacheFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant,
            assetName, number, assetVariant, furObjectLabel
        )[1]
    elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
        cacheFile = scAstCfxNurbsHairCacheFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant,
            assetName, number, assetVariant, furObjectLabel
        )[1]
    if cacheFile:
        osPath, osFileBasename = lxBasic.getOsFileSplitFileNameData(cacheFile)
        #
        osPaths = lxBasic.glob.glob(osPath + '_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]')
        if osPaths:
            for osPath in osPaths:
                osPath = osPath.replace('\\', '/')
                osFile = lxBasic._toOsFile(osPath, osFileBasename)
                dic.setdefault(lxConfigure.LynxiProduct_Asset_Link_Cfx, []).append(osFile)
    return dic


#
def getScAstCfxFurCacheTimeTag(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel):
    osFile = getScAstCfxFurCache(projectName, sceneName, sceneVariant, assetName, number, assetVariant, furObjectLabel)
    return lxBasic.getOsFileTimeTag(osFile)


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
                caches = lxBasic.glob.glob(base + '.[0-9][0-9][0-9][0-9]' + ext)
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
            if lxBasic.isOsExistsFile(xmlFile):
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
                            base, ext = lxBasic.toOsFileSplitByExt(xmlFile)
                            cacheFile = base + cacheExtDic[cacheFormat]
                            if lxBasic.isOsExistsFile(cacheFile):
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
                caches = lxBasic.glob.glob(base + '.[0-9][0-9][0-9][0-9]' + ext)
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
def getMeshDataFile(osFile):
    ext = lxBasic.getOsFileExt(osFile)
    return osFile[:-len(ext)] + appVariant.dbMeshUnitKey


#
def getRenderPoolFile(osFile, renderRoot):
    def getProjectIndex():
        indexData = osFile.lower().split(pathsep)
        projectName = renderRoot.split(pathsep)[-2].lower()
        return indexData.index(projectName)
    #
    def getOsActiveTimeTag():
        lis = []
        tagIndex = [chr(i) for i in range(65, 75)]
        #
        tag = lxBasic.datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d-%H%M%S-%f')
        for t in tag:
            if t.isdigit():
                s = tagIndex[int(t)]
            else:
                s = t
            lis.append(s)
        #
        return ''.join(lis)
    #
    string = none
    #
    pathsep = appCfg.OsFilePathSep
    timestamp = lxBasic.getOsFileMtimestamp(osFile)
    if timestamp:
        osFile = lxBasic.getPathReduce(osFile, pathsep)
        cutIndex = getProjectIndex()
        splitData = osFile.split(pathsep)
        osFile = renderRoot + pathsep + pathsep.join(splitData[cutIndex + 1:])
        base, ext = lxBasic.toOsFileSplitByExt(osFile)
        osFileName = lxBasic.getOsFileName(osFile)
        osFolder = base[:-len(osFileName) - 1]
        timeTag = getOsActiveTimeTag()
        #
        string = osFolder + pathsep + timeTag + pathsep + osFileName + ext
    return string


#
def getScWorkspaceRootDic():
    dic = lxBasic.orderedDict()
    #
    for rootIndexKey in [lxConfigure.LynxiRootIndex_Local, lxConfigure.LynxiRootIndex_Server]:
        dic[rootIndexKey] = scUnitRenderFolder, lxBasic._toStringPrettify(lxConfigure.LynxiRootLabelDic[rootIndexKey])
    return dic


#
def getScRenderCustomizes(projectName, sceneClass, sceneName, sceneVariant, sceneStage):
    lis = []
    #
    osPath = scUnitRenderBasicFolder(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage
    )
    #
    if lxBasic.isOsExist(osPath):
        subFolders = lxBasic.getOsFileBasenameLisByPath(osPath)
        if subFolders:
            for subOsFolder in subFolders:
                renderFile = scUnitRenderFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName, sceneClass, sceneName, sceneVariant, sceneStage, subOsFolder
                )[1]
                if lxBasic.isOsExistsFile(renderFile):
                    if not subOsFolder in lis:
                        lis.append(subOsFolder)
    #
    return lis


#
def getScRenderIndexData(
        sceneIndex,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        width, height,
        prefix,
        composeFiles,
        imageFiles
):
    dic = lxBasic.orderedDict()
    #
    dic[lxConfigure.Lynxi_Key_Info_Update] = lxBasic.getOsActiveTimestamp()
    dic[lxConfigure.Lynxi_Key_Info_Artist] = lxBasic.getOsUser()
    #
    dic[appVariant.basicIndexAttrLabel] = sceneIndex
    dic[appVariant.basicProjectAttrLabel] = projectName
    dic[appVariant.basicClassAttrLabel] = sceneClass
    dic[appVariant.basicNameAttrLabel] = sceneName
    dic[appVariant.basicVariantAttrLabel] = sceneVariant
    dic[appVariant.basicStageAttrLabel] = sceneStage
    dic[appVariant.basicStartFrameAttrLabel] = startFrame
    dic[appVariant.basicEndFrameAttrLabel] = endFrame
    dic[appVariant.basicWidthAttrLabel] = width
    dic[appVariant.basicHeightAttrLabel] = height
    #
    dic['prefix'] = prefix
    dic['compose'] = composeFiles
    dic['image'] = imageFiles
    return dic


#
def getScRenderImageData(projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize):
    indexFile = sceUnitRenderIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    if lxBasic.isOsExistsFile(indexFile):
        data = lxBasic.readOsJson(indexFile)
        image = data['image']
        prefix = data['prefix']
        #
        return prefix, image


#
def getScRenderCompose(projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize):
    indexFile = sceUnitRenderIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    if lxBasic.isOsExistsFile(indexFile):
        data = lxBasic.readOsJson(indexFile)
        compose = data['compose']
        #
        return compose


#
def getScTdUploadCommand(projectName, link):
    dataDic = projectPr.getProjectMayaTdPresetDic(projectName)
    if dataDic:
        if link in dataDic:
            data = dataDic[link]
            if data:
                mayaPackageStr = data[lxConfigure.LynxiMayaScriptKey]
                #
                var = ''
                pathCmd = lxBasic._toVariantConvert('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if lxBasic.isOsExist(var):
                        osFile = var + '/' + lxConfigure.LynxiSceneUploadCommandKey + '.py'
                        if lxBasic.isOsExist(osFile):
                            command = lxBasic.readOsFile(osFile)
                            pythonCommand = 'python(' + lxBasic.getJsonDumps(command) + ');'
                            #
                            return pythonCommand


#
def getScTdLoadCommand(projectName, link):
    dataDic = projectPr.getProjectMayaTdPresetDic(projectName)
    if dataDic:
        if link in dataDic:
            data = dataDic[link]
            if data:
                mayaPackageStr = data[lxConfigure.LynxiMayaScriptKey]
                #
                var = ''
                pathCmd = lxBasic._toVariantConvert('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    if lxBasic.isOsExist(var):
                        osFile = var + '/' + lxConfigure.LynxiSceneLoadCommandKey + '.py'
                        if lxBasic.isOsExist(osFile):
                            command = lxBasic.readOsFile(osFile)
                            pythonCommand = 'python(' + lxBasic.getJsonDumps(command) + ');'
                            #
                            return pythonCommand
