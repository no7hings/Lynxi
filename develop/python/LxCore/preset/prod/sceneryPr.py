# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
from LxCore.config import sceneryCfg
#
from LxCore.preset import appVariant
# do not delete and rename
serverBasicPath = lxConfigure.Root()._serverPath()
localBasicPath = lxConfigure.Root()._localPath()
#
none = ''


#
def scnBasicNameSet(*args):
    formatString = ''
    for i in args:
        if isinstance(i, str) or isinstance(i, unicode):
            if not i.startswith('_'):
                j = '_{}'
            else:
                j = '{}'
            formatString += j
    return appVariant.Lynxi_Prefix_Product_Scenery + formatString.format(*args)


# Group Name Config
def scnBasicGroupNameSet(*args):
    return scnBasicNameSet(*args) + appVariant.basicGroupLabel


#
def scnBasicNodeNameSet(*args):
    return scnBasicNameSet(*args)


# Group Name Config
def scnGroupNameSet(sceneryName, groupNameLabel):
    nameSet = '%s_%s%s%s' % (appVariant.Lynxi_Prefix_Product_Scenery, sceneryName, groupNameLabel, appVariant.basicGroupLabel)
    return nameSet


#
def scnComposeRootGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, appVariant.basicComposeRootGroupLabel)
    return string


#
def scnUnitRootGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, appVariant.basicUnitRootGroupLabel)
    return string


#
def scnAssemblyGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, appVariant.basicAssemblyLabel)


#
def scnAssemblyFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, lxBasic.getComposeLabel(appVariant.basicAssemblyLabel, appVariant.basicFieldLabel))


#
def scnGpuFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, lxBasic.getComposeLabel(appVariant.basicGpuLabel, appVariant.basicFieldLabel))


#
def scnProxyFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, lxBasic.getComposeLabel(appVariant.basicProxyLabel, appVariant.basicFieldLabel))


#
def scnControlFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, lxBasic.getComposeLabel(appVariant.basicControlLabel, appVariant.basicFieldLabel))


#
def scnAssetFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, lxBasic.getComposeLabel(appVariant.basicAssetLabel, appVariant.basicFieldLabel))


#
def scnUnitLocatorName(sceneryName, sceneryVariant, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicNodeNameSet(sceneryName, sceneryVariant, appVariant.basicAssemblyLabel)


#
def scnAssemblyGroupPath(sceneryName, namespace=none):
    return '|' + '|'.join([scnUnitRootGroupName(sceneryName, namespace), scnAssemblyGroupName(sceneryName, namespace)])


#
def scnLightGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, appVariant.basicLightLinkGroupLabel)
    return string


#
def assemblyRepresentationsConfig():
    config = ['Box', 'GPU']
    [config.append('GPU-LOD%s' % str(level + 1).zfill(2)) for level in range(2)]
    config.append('Proxy')
    [config.append('Proxy-LOD%s' % str(level + 1).zfill(2)) for level in range(2)]
    config.append('Asset')
    config.append('None')
    return config


#
def assembleLodConfig():
    config = []
    [config.append('LOD - %s' % str(level).zfill(2)) for level in range(3)]
    return config


#
def assemblyGpuRepresentationsConfig():
    config = ['GPU']
    [config.append('GPU-LOD%s' % str(level + 1).zfill(2)) for level in range(2)]
    return config


#
def assemblyColorConfig():
    return {
        'GPU': 17, 'GPU-LOD01': 14, 'GPU-LOD02': 6,
        'Proxy': 17, 'Proxy-LOD01': 14, 'Proxy-LOD02': 6
    }


#
def assemblyLodColorConfig():
    dic = lxBasic.orderedDict()
    dic[17] = 'LOD00'
    dic[14] = 'LOD01'
    dic[6] = 'LOD02'
    return dic


# Scenery AD Name
def scnAssemblyAdName(sceneryClass, sceneryName, sceneryVariant=none):
    string = '%s_%s_%s%s' % (appVariant.Lynxi_Prefix_Product_Scenery, sceneryName, sceneryVariant, appVariant.scnSceneryDefinitionLabel)
    return string


# Scenery AR Name
def scnAssemblyArName(sceneryClass, sceneryName, sceneryVariant=none):
    string = '%s_%s_%s%s' % (appVariant.Lynxi_Prefix_Product_Scenery, sceneryName, sceneryVariant, appVariant.scnSceneryReferenceLabel)
    return string


#
def assemblyGroupArName(sceneryName):
    string = '%s_%s%s' % (appVariant.scnAssemblyPrefix, sceneryName, appVariant.scnSceneryReferenceLabel)
    return string


# Scenery Main Locator
def sceneryMainLocatorName(sceneryClass, sceneryName, sceneryVariant):
    string = '%s_%s_%s%s' % (appVariant.scnAssemblyPrefix, sceneryName, sceneryVariant, appVariant.scnSceneryLocatorLabel)
    return string


# Scenery Main Locator
def sceneryAssemblyMainLocatorName(sceneryName, sceneryVariant):
    string = '%s_%s_%s%s' % (appVariant.scnAssemblyPrefix, sceneryName, sceneryVariant, appVariant.scnSceneryLocatorLabel)
    return string


# Scene Object Locator Name
def sceneryAssemblySubLocatorName(assetName, number, assetVariant):
    string = '%s_%s_%s_%s%s' % (appVariant.scnAssemblyPrefix, assetName, number, assetVariant, appVariant.scnSceneryLocatorLabel)
    return string


#
def scnRootGroupHierarchyConfig(sceneryName):
    dic = lxBasic.orderedDict()
    dic[scnUnitRootGroupName(sceneryName)] = []
    return dic


#
def scnAssemblyHierarchyConfig(sceneryName):
    dic = lxBasic.orderedDict()
    # Main
    dic[scnAssemblyGroupName(sceneryName)] = [
        scnAssemblyFieldGroupName(sceneryName)
    ]
    return dic


#
def scnLightHierarchyConfig(sceneryName):
    dic = lxBasic.orderedDict()
    # Main
    dic[scnLightGroupName(sceneryName)] = [
        scnGroupNameSet(sceneryName, appVariant.lgtFieldLabel)
    ]
    return dic


#
def isSceneryStage(sceneryStage):
    boolean = False
    if sceneryStage in appVariant.scnSceneryStages:
        boolean = True
    return boolean


#
def isAssemblyStage(sceneryStage):
    boolean = False
    if sceneryStage in appVariant.scnAssemblyStages:
        boolean = True
    return boolean


#
def scenerySchemeFileConfig():
    string = '{0}/{1}/{2}/{3}'.format(appVariant.dbSceneryRoot, appVariant.dbBasicFolderName, lxConfigure.LynxiSchemeExt, appVariant.dbSceneryBasicKey)
    return lxBasic.getOsUniqueFile(string)


#
def scenerySetFileConfig(sceneryIndex):
    string = '{0}/{1}/{2}/{3}'.format(appVariant.dbSceneryRoot, appVariant.dbBasicFolderName, lxConfigure.LynxiSetExt, sceneryIndex)
    return string


#
def defaultScenerySchemeConfig():
    lis = [
        True,
        u'请输入备注'
    ]
    return lis


#
def defaultScenerySetConfig(projectName, number=0):
    lis = [
        [('project', u'项目 ( Project(s) )'), (projectName, )],
        [('classify', u'类型 ( Classify )'), sceneryCfg.scnBasicClass()],
        [('name', u'名字 ( Name )'), 'ID{}'.format(str(number).zfill(6))],
        [('variant', u'变体 ( Variant(s) )'), (appVariant.scnDefaultVariant, )],
        [('priority', u'优先级 ( Priority )'), sceneryCfg.basicSceneryPriorities()],
        [(lxConfigure.LynxiProduct_Scenery_Link_Scenery, u'场景布景 ( Scenery )'), False],
        [(lxConfigure.LynxiProduct_Scene_Link_layout, u'场景预览 ( Layout )'), False],
        [(lxConfigure.LynxiProduct_Scene_Link_Animation, u'场景动画 ( Animation )'), False],
        [(lxConfigure.LynxiProduct_Scene_Link_Simulation, u'场景解算 ( Simulation )'), False],
        [(lxConfigure.LynxiProduct_Scene_Link_Light, u'场景灯光 ( Light )'), False]
    ]
    return lis


# Scheme Data
def getUiScenerySchemeDataDic():
    def getCustomData():
        osFile = scenerySchemeFileConfig()
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
def getUiScenerySetDataLis(projectName, sceneryIndex, number=0):
    def getDefaultData():
        return defaultScenerySetConfig(projectName, number)
    #
    def getCustomData():
        osFile = scenerySetFileConfig(sceneryIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getDic(defaultLis, customDic):
        lis = []
        if defaultLis:
            for i in defaultLis:
                setKey, uiData = i
                setUiKey = none
                if isinstance(setKey, str) or isinstance(setKey, unicode):
                    setUiKey = lxBasic._toStringPrettify(setKey)
                if isinstance(setKey, tuple):
                    setKey, setUiKey = setKey
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
                lis.append(
                    (setKey, setUiKey, setValue, defValue, uiData)
                )
        return lis
    #
    return getDic(getDefaultData(), getCustomData())


#
def getSceneryViewName(sceneryIndex):
    def getCustomData():
        osFile = scenerySchemeFileConfig()
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
        if sceneryIndex in customDic:
            string = customDic[sceneryIndex]
        return string
    #
    return getMain(getSubDic(getCustomData()))


#
def getSceneryClass(sceneryIndex):
    def getCustomData():
        osFile = scenerySetFileConfig(sceneryIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['classify']
    #
    return getMain(getCustomData())


#
def getSceneryName(sceneryIndex):
    def getCustomData():
        osFile = scenerySetFileConfig(sceneryIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['name']
    #
    return getMain(getCustomData())


#
def getSceneryPriority(sceneryIndex):
    def getCustomData():
        osFile = scenerySetFileConfig(sceneryIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['priority']
    #
    return getMain(getCustomData())


#
def getSceneryVariants(sceneryIndex):
    def getCustomData():
        osFile = scenerySetFileConfig(sceneryIndex)
        return lxBasic.readOsJson(osFile)
    #
    def getMain(customDic):
        if customDic:
            return customDic['variant']
    #
    return getMain(getCustomData())


#
def sceneryViewInfoSet(sceneryViewName, sceneryClass, sceneryVariant):
    string = u'{} {} ( {} )'.format(
        sceneryCfg.scnBasicViewClassDic(sceneryClass)[1],
        sceneryViewName,
        sceneryVariant
    )
    return string


#
def getSceneryViewInfo(sceneryIndex, sceneryClass=None, sceneryVariant=None):
    if sceneryClass is None:
        sceneryClass = getSceneryClass(sceneryIndex)
    if sceneryVariant is None:
        sceneryVariant = appVariant.scnDefaultVariant
    return sceneryViewInfoSet(getSceneryViewName(sceneryIndex), sceneryClass, sceneryVariant)


#
def getSceneryIndexesFilter(projectFilter, sceneryClassFilters=None):
    def getCustomData():
        osFile = scenerySchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getBranch(lis, sceneryIndex):
        osFile = scenerySetFileConfig(sceneryIndex)
        data = lxBasic.readOsJson(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                dbSceneryClass = data['classify']
                if sceneryClassFilters is not None:
                    if dbSceneryClass in sceneryClassFilters:
                        lis.append(sceneryIndex)
                elif sceneryClassFilters is None:
                    lis.append(sceneryIndex)
    #
    def getMain(data):
        lis = []
        if data:
            for i in data:
                sceneryIndex, enabled, description = i
                if enabled is True:
                    getBranch(lis, sceneryIndex)
        return lis
    return getMain(getCustomData())


#
def getUiSceneryMultMsgs(projectFilter, sceneryClassFilters=None, sceneryLinkFilter=None):
    def getCustomData():
        osFile = scenerySchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getLinks(data):
        lis = []
        for i in appVariant.scnBasicLinks:
            enabled = data[i]
            if enabled is True:
                lis.append(i)
        return lis
    #
    def getBranch(dic, sceneryIndex, description):
        osFile = scenerySetFileConfig(sceneryIndex)
        data = lxBasic.readOsJson(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                isMatch = False
                #
                dbSceneryClass = data['classify']
                dbSceneryName = data['name']
                dbSceneryLinks = getLinks(data)
                if sceneryClassFilters is not None:
                    if dbSceneryClass in sceneryClassFilters:
                        if sceneryLinkFilter is not None:
                            if sceneryLinkFilter in dbSceneryLinks:
                                isMatch = True
                        elif sceneryLinkFilter is None:
                            isMatch = True
                elif sceneryClassFilters is None:
                    if sceneryLinkFilter is not None:
                        if sceneryLinkFilter in dbSceneryLinks:
                            isMatch = True
                    elif sceneryLinkFilter is None:
                        isMatch = True
                #
                if isMatch is True:
                    dic[sceneryIndex] = dbSceneryName, description
    #
    def getMain(data):
        dic = lxBasic.orderedDict()
        if data:
            for i in data:
                sceneryIndex, enabled, description = i
                if enabled is True:
                    getBranch(dic, sceneryIndex, description)
        return dic
    #
    return getMain(getCustomData())


#
def getSceneryDescriptionDic():
    def getCustomData():
        osFile = scenerySchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getBranch(dic, sceneryIndex):
        osFile = scenerySetFileConfig(sceneryIndex)
        data = lxBasic.readOsJson(osFile)
        if data:
            sceneryName = data['name']
            dic[sceneryName] = sceneryIndex
    #
    def getMain(data):
        dic = lxBasic.orderedDict()
        if data:
            for i in data:
                sceneryIndex, enabled, description = i
                if enabled is True:
                    getBranch(dic, sceneryIndex)
        return dic
    #
    return getMain(getCustomData())


#
def getUiScenerySetDataDic(projectFilter):
    def getCustomData():
        osFile = scenerySchemeFileConfig()
        return lxBasic.readOsJson(osFile)
    #
    def getBranch(dic, sceneryIndex, description):
        osFile = scenerySetFileConfig(sceneryIndex)
        data = lxBasic.readOsJson(osFile)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                sceneryClass = data['classify']
                sceneryName = data['name']
                sceneryVariants = data['variant']
                sceneryPriority = data['priority']
                #
                sceneryEnabled = lxBasic.getKeyEnabled(data, lxConfigure.LynxiProduct_Scenery_Link_Scenery)
                scLayoutEnable = data[lxConfigure.LynxiProduct_Scene_Link_layout]
                scAnimationEnable = data[lxConfigure.LynxiProduct_Scene_Link_Animation]
                scSimulationEnable = data[lxConfigure.LynxiProduct_Scene_Link_Simulation]
                scLightEnable = data[lxConfigure.LynxiProduct_Scene_Link_Light]
                for sceneryVariant in sceneryVariants:
                    dic[(sceneryIndex, sceneryVariant)] = description, sceneryClass, sceneryName, sceneryPriority, sceneryEnabled, scLayoutEnable, scAnimationEnable, scSimulationEnable, scLightEnable
    #
    def getMain(data):
        dic = lxBasic.orderedDict()
        if data:
            for i in data:
                sceneryIndex, enabled, description = i
                if enabled is True:
                    getBranch(dic, sceneryIndex, description)
        return dic
    return getMain(getCustomData())


#
def isScnSceneryLink(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScnSceneryStages or sceneryStage == lxConfigure.LynxiProduct_Scenery_Link_Scenery:
        boolean = True
    return boolean


#
def isScnLayoutLink(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScLayoutStages or sceneryStage == lxConfigure.LynxiProduct_Scene_Link_layout:
        boolean = True
    return boolean


#
def isScnAnimationLink(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScAnimationStages or sceneryStage == lxConfigure.LynxiProduct_Scene_Link_Animation:
        boolean = True
    return boolean


#
def isScnSimulationLink(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScSimulationStages or sceneryStage == lxConfigure.LynxiProduct_Scene_Link_Simulation:
        boolean = True
    return boolean


#
def isScnLightLink(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScLightStages or sceneryStage == lxConfigure.LynxiProduct_Scene_Link_Light:
        boolean = True
    return boolean


#
def getSceneryLink(sceneryStage):
    link = lxConfigure.LynxiProduct_Scenery_Link_Scenery
    if isScnSceneryLink(sceneryStage):
        link = lxConfigure.LynxiProduct_Scenery_Link_Scenery
    elif isScnLayoutLink(sceneryStage):
        link = lxConfigure.LynxiProduct_Scene_Link_layout
    elif isScnAnimationLink(sceneryStage):
        link = lxConfigure.LynxiProduct_Scene_Link_Animation
    elif isScnSimulationLink(sceneryStage):
        link = lxConfigure.LynxiProduct_Scene_Link_Simulation
    elif isScnLightLink(sceneryStage):
        link = lxConfigure.LynxiProduct_Scene_Link_Light
    return link


#
def sceneryLinkFolder(sceneryStage):
    string = appVariant.scnSceneryFolder
    if isScnSceneryLink(sceneryStage):
        string = appVariant.scnSceneryFolder
    elif isScnLayoutLink(sceneryStage):
        string = appVariant.scnLayoutFolder
    elif isScnAnimationLink(sceneryStage):
        string = appVariant.scnAnimationFolder
    elif isScnSimulationLink(sceneryStage):
        string = appVariant.scnSimulationFolder
    elif isScnLightLink(sceneryStage):
        string = appVariant.scnLightFolder
    return string


#
def scnBasicLinkLabel(sceneryStage):
    string = appVariant.basicSceneryLinkLabel
    if isScnSceneryLink(sceneryStage):
        string = appVariant.basicSceneryLinkLabel
    elif isScnLayoutLink(sceneryStage):
        string = appVariant.basicLayoutLinkLabel
    elif isScnAnimationLink(sceneryStage):
        string = appVariant.basicAnimationLinkLabel
    elif isScnSimulationLink(sceneryStage):
        string = appVariant.basicSimulationLinkLabel
    elif isScnLightLink(sceneryStage):
        string = appVariant.basicLightLinkLabel
    return string


#
def scenerySourceFileLabel(sceneryStage):
    string = appVariant.scnScenerySourceLabel
    if isScnSceneryLink(sceneryStage):
        string = appVariant.scnScenerySourceLabel
    elif isScnLayoutLink(sceneryStage):
        string = appVariant.scnLayoutSourceLabel
    elif isScnAnimationLink(sceneryStage):
        string = appVariant.scnAnimationSourceLabel
    elif isScnSimulationLink(sceneryStage):
        string = appVariant.scnSimulationSourceLabel
    elif isScnLightLink(sceneryStage):
        string = appVariant.scnLightSourceLabel
    return string


#
def scnProductFileLabel(sceneryStage):
    subLabel = appVariant.basicProductSubLabel
    return lxBasic.getComposeLabel(scnBasicLinkLabel(sceneryStage), subLabel)


#
def scnAssemblyLabel(sceneryStage):
    subLabel = appVariant.basicAssemblySubLabel
    return lxBasic.getComposeLabel(scnBasicLinkLabel(sceneryStage), subLabel)


#
def sceneryPreviewFileLabel(sceneryStage):
    string = appVariant.scnSceneryPreviewLabel
    if isScnSceneryLink(sceneryStage):
        string = appVariant.scnSceneryPreviewLabel
    elif isScnLayoutLink(sceneryStage):
        string = appVariant.scnLayoutPreviewLabel
    elif isScnAnimationLink(sceneryStage):
        string = appVariant.scnAnimationPreviewLabel
    elif isScnSimulationLink(sceneryStage):
        string = appVariant.scnSimulationPreviewLabel
    elif isScnLightLink(sceneryStage):
        string = appVariant.scnLightPreviewLabel
    return string


#
def sceneryDefinitionFileLabel(sceneryStage):
    string = appVariant.scnSceneryDefinitionLabel
    if isScnSceneryLink(sceneryStage):
        string = appVariant.scnSceneryDefinitionLabel
    if isScnLayoutLink(sceneryStage):
        string = appVariant.scnLayoutDefinitionLabel
    elif isScnAnimationLink(sceneryStage):
        string = appVariant.scnAnimationDefinitionLabel
    elif isScnSimulationLink(sceneryStage):
        string = appVariant.scnSimulationDefinitionLabel
    elif isScnLightLink(sceneryStage):
        string = appVariant.scnLightDefinitionLabel
    return string


#
def scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel):
    string = '%s%s%s' % (sceneryName, fileLabel, extLabel)
    return string


# Scenery Path
def sceneryUnitBasicDirectory(rootIndexKey, projectName):
    root = [appVariant.serverSceneryRoot, appVariant.localSceneryRoot, appVariant.backupSceneryRoot]
    return '%s/%s/%s/%s' % (root[rootIndexKey], projectName, appVariant.basicSceneryFolder, appVariant.scnUnitFolder)


#
def sceneryUnitFolder(rootIndexKey, projectName, sceneryClass, sceneryName):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    osPath = '%s/%s' % (
        basicDirectory,
        sceneryName
    )
    return osPath


#
def scnUnitSourceFile(rootIndexKey, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = scenerySourceFileLabel(sceneryStage)
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scnUnitProductFile(rootIndexKey, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = scnProductFileLabel(sceneryStage)
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scnUnitPreviewFile(rootIndexKey, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage, extLabel=appVariant.jpgExt):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = sceneryPreviewFileLabel(sceneryStage)
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scnUnitDefinitionFile(rootIndexKey, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = sceneryDefinitionFileLabel(sceneryStage)
    extLabel = appVariant.mayaAsciiExt
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def scnUnitAssemblyComposeFile(rootIndexKey, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = scnAssemblyLabel(sceneryStage)
    extLabel = appVariant.assemblyComposeExt
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    osFile = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, osFile


#
def getScnAssemblyComposeDatumDic(projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage):
    dic = {}
    serverFile = scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = lxBasic.readOsJson(serverFile)
    lis = []
    if datumLis:
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
def getSceneryUnitProductUpdate(projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage):
    string = appVariant.infoNonExistsLabel
    #
    serverProductFile = scnUnitProductFile(
        lxConfigure.LynxiRootIndex_Server, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    if lxBasic.isOsExistsFile(serverProductFile):
        data = lxBasic.getCnViewTime(lxBasic.getOsFileMtimestamp(serverProductFile))
        if data:
            string = data
    return string


#
def getScnUnitPreviewFile(projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage):
    renderPreviewFile = scnUnitPreviewFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        extLabel=appVariant.pngExt
    )[1]
    if lxBasic.isOsExistsFile(renderPreviewFile):
        return renderPreviewFile
    else:
        viewportPreviewFile = scnUnitPreviewFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage,
            extLabel=appVariant.jpgExt
        )[1]
        if lxBasic.isOsExistsFile(viewportPreviewFile):
            return viewportPreviewFile