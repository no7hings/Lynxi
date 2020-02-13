# coding=utf-8
from LxBasic import bscCore, bscMethods

from LxCore import lxConfigure, lxScheme
#
from LxCore.config import sceneryCfg
#
from LxPreset import prsVariants, prsMethods

# do not delete and rename
serverBasicPath = lxScheme.Root().basic.server
localBasicPath = lxScheme.Root().basic.local
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
    return prsVariants.Util.Lynxi_Prefix_Product_Scenery + formatString.format(*args)


# Group Name Config
def scnBasicGroupNameSet(*args):
    return scnBasicNameSet(*args) + prsVariants.Util.basicGroupLabel


#
def scnBasicNodeNameSet(*args):
    return scnBasicNameSet(*args)


# Group Name Config
def scnGroupNameSet(sceneryName, groupNameLabel):
    nameSet = '%s_%s%s%s' % (
    prsVariants.Util.Lynxi_Prefix_Product_Scenery, sceneryName, groupNameLabel, prsVariants.Util.basicGroupLabel)
    return nameSet


#
def scnComposeRootGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, prsVariants.Util.basicComposeRootGroupLabel)
    return string


#
def scnUnitRootGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, prsVariants.Util.basicUnitRootGroupLabel)
    return string


#
def scnAssemblyGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, prsVariants.Util.basicAssemblyLabel)


#
def scnAssemblyFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsVariants.Util.basicAssemblyLabel, prsVariants.Util.basicFieldLabel))


#
def scnGpuFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsVariants.Util.basicGpuLabel, prsVariants.Util.basicFieldLabel))


#
def scnProxyFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsVariants.Util.basicProxyLabel, prsVariants.Util.basicFieldLabel))


#
def scnControlFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsVariants.Util.basicControlLabel, prsVariants.Util.basicFieldLabel))


#
def scnAssetFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsVariants.Util.basicAssetLabel, prsVariants.Util.basicFieldLabel))


#
def scnUnitLocatorName(sceneryName, sceneryVariant, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicNodeNameSet(sceneryName, sceneryVariant, prsVariants.Util.basicAssemblyLabel)


#
def scnAssemblyGroupPath(sceneryName, namespace=none):
    return '|' + '|'.join([scnUnitRootGroupName(sceneryName, namespace), scnAssemblyGroupName(sceneryName, namespace)])


#
def scnLightGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, prsVariants.Util.basicLightLinkGroupLabel)
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
    dic = bscCore.orderedDict()
    dic[17] = 'LOD00'
    dic[14] = 'LOD01'
    dic[6] = 'LOD02'
    return dic


# Scenery AD Name
def scnAssemblyAdName(sceneryCategory, sceneryName, sceneryVariant=none):
    string = '%s_%s_%s%s' % (prsVariants.Util.Lynxi_Prefix_Product_Scenery, sceneryName, sceneryVariant, prsVariants.Util.scnSceneryDefinitionLabel)
    return string


# Scenery AR Name
def scnAssemblyArName(sceneryCategory, sceneryName, sceneryVariant=none):
    string = '%s_%s_%s%s' % (prsVariants.Util.Lynxi_Prefix_Product_Scenery, sceneryName, sceneryVariant, prsVariants.Util.scnSceneryReferenceLabel)
    return string


#
def assemblyGroupArName(sceneryName):
    string = '%s_%s%s' % (
    prsVariants.Util.scnAssemblyPrefix, sceneryName, prsVariants.Util.scnSceneryReferenceLabel)
    return string


# Scenery Main Locator
def sceneryMainLocatorName(sceneryCategory, sceneryName, sceneryVariant):
    string = '%s_%s_%s%s' % (
    prsVariants.Util.scnAssemblyPrefix, sceneryName, sceneryVariant, prsVariants.Util.scnSceneryLocatorLabel)
    return string


# Scenery Main Locator
def sceneryAssemblyMainLocatorName(sceneryName, sceneryVariant):
    string = '%s_%s_%s%s' % (
    prsVariants.Util.scnAssemblyPrefix, sceneryName, sceneryVariant, prsVariants.Util.scnSceneryLocatorLabel)
    return string


# Scene Object Locator Name
def sceneryAssemblySubLocatorName(assetName, number, assetVariant):
    string = '%s_%s_%s_%s%s' % (
    prsVariants.Util.scnAssemblyPrefix, assetName, number, assetVariant, prsVariants.Util.scnSceneryLocatorLabel)
    return string


#
def scnRootGroupHierarchyConfig(sceneryName):
    dic = bscCore.orderedDict()
    dic[scnUnitRootGroupName(sceneryName)] = []
    return dic


#
def scnAssemblyHierarchyConfig(sceneryName):
    dic = bscCore.orderedDict()
    # Main
    dic[scnAssemblyGroupName(sceneryName)] = [
        scnAssemblyFieldGroupName(sceneryName)
    ]
    return dic


#
def scnLightHierarchyConfig(sceneryName):
    dic = bscCore.orderedDict()
    # Main
    dic[scnLightGroupName(sceneryName)] = [
        scnGroupNameSet(sceneryName, prsVariants.Util.lgtFieldLabel)
    ]
    return dic


#
def isSceneryStage(sceneryStage):
    boolean = False
    if sceneryStage in prsVariants.Util.scnSceneryStages:
        boolean = True
    return boolean


#
def isAssemblyStage(sceneryStage):
    boolean = False
    if sceneryStage in prsVariants.Util.scnAssemblyStages:
        boolean = True
    return boolean


#
def scenerySchemeFileConfig():
    string = '{0}/{1}/{2}/{3}'.format(prsVariants.Util.dbSceneryRoot, prsVariants.Util.dbBasicFolderName, lxConfigure.LynxiSchemeExt, prsVariants.Util.dbSceneryBasicKey)
    return bscMethods.OsFile.uniqueName(string)


#
def scenerySetFileConfig(sceneryIndex):
    string = '{0}/{1}/{2}/{3}'.format(prsVariants.Util.dbSceneryRoot, prsVariants.Util.dbBasicFolderName, lxConfigure.LynxiSetExt, sceneryIndex)
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
        [('variant', u'变体 ( Variant(s) )'), (prsVariants.Util.scnDefaultVariant,)],
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
        fileString_ = scenerySchemeFileConfig()
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
def getUiScenerySetDataLis(projectName, sceneryIndex, number=0):
    def getDefaultData():
        return defaultScenerySetConfig(projectName, number)
    #
    def getCustomData():
        fileString_ = scenerySetFileConfig(sceneryIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getDic(defaultLis, customDic):
        lis = []
        if defaultLis:
            for i in defaultLis:
                setKey, uiData = i
                setUiKey = none
                if isinstance(setKey, str) or isinstance(setKey, unicode):
                    setUiKey = bscMethods.StrCamelcase.toPrettify(setKey)
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
        fileString_ = scenerySchemeFileConfig()
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
        string = lxConfigure.LynxiValue_Unspecified
        if sceneryIndex in customDic:
            string = customDic[sceneryIndex]
        return string
    #
    return getMain(getSubDic(getCustomData()))


#
def getSceneryClass(sceneryIndex):
    def getCustomData():
        fileString_ = scenerySetFileConfig(sceneryIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['classify']
    #
    return getMain(getCustomData())


#
def getSceneryName(sceneryIndex):
    def getCustomData():
        fileString_ = scenerySetFileConfig(sceneryIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['name']
    #
    return getMain(getCustomData())


#
def getSceneryPriority(sceneryIndex):
    def getCustomData():
        fileString_ = scenerySetFileConfig(sceneryIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['priority']
    #
    return getMain(getCustomData())


#
def getSceneryVariants(sceneryIndex):
    def getCustomData():
        fileString_ = scenerySetFileConfig(sceneryIndex)
        return bscMethods.OsJson.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['variant']
    #
    return getMain(getCustomData())


#
def sceneryViewInfoSet(sceneryViewName, sceneryCategory, sceneryVariant):
    string = u'{} {} ( {} )'.format(
        sceneryCfg.scnBasicViewClassDic(sceneryCategory)[1],
        sceneryViewName,
        sceneryVariant
    )
    return string


#
def getSceneryViewInfo(sceneryIndex, sceneryCategory=None, sceneryVariant=None):
    if sceneryCategory is None:
        sceneryCategory = getSceneryClass(sceneryIndex)
    if sceneryVariant is None:
        sceneryVariant = prsVariants.Util.scnDefaultVariant
    return sceneryViewInfoSet(getSceneryViewName(sceneryIndex), sceneryCategory, sceneryVariant)


#
def getSceneryIndexesFilter(projectFilter, sceneryClassFilters=None):
    def getCustomData():
        fileString_ = scenerySchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getBranch(lis, sceneryIndex):
        fileString_ = scenerySetFileConfig(sceneryIndex)
        data = bscMethods.OsJson.read(fileString_)
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
        fileString_ = scenerySchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getLinks(data):
        lis = []
        for i in prsVariants.Util.scnBasicLinks:
            enabled = data[i]
            if enabled is True:
                lis.append(i)
        return lis
    #
    def getBranch(dic, sceneryIndex, description):
        fileString_ = scenerySetFileConfig(sceneryIndex)
        data = bscMethods.OsJson.read(fileString_)
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
        dic = bscCore.orderedDict()
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
        fileString_ = scenerySchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getBranch(dic, sceneryIndex):
        fileString_ = scenerySetFileConfig(sceneryIndex)
        data = bscMethods.OsJson.read(fileString_)
        if data:
            sceneryName = data['name']
            dic[sceneryName] = sceneryIndex
    #
    def getMain(data):
        dic = bscCore.orderedDict()
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
        fileString_ = scenerySchemeFileConfig()
        return bscMethods.OsJson.read(fileString_)
    #
    def getBranch(dic, sceneryIndex, description):
        fileString_ = scenerySetFileConfig(sceneryIndex)
        data = bscMethods.OsJson.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                sceneryCategory = data['classify']
                sceneryName = data['name']
                sceneryVariants = data['variant']
                sceneryPriority = data['priority']
                #
                sceneryEnabled = bscMethods.Dict.getAsBoolean(data, lxConfigure.LynxiProduct_Scenery_Link_Scenery)
                scLayoutEnable = data[lxConfigure.LynxiProduct_Scene_Link_layout]
                scAnimationEnable = data[lxConfigure.LynxiProduct_Scene_Link_Animation]
                scSimulationEnable = data[lxConfigure.LynxiProduct_Scene_Link_Simulation]
                scLightEnable = data[lxConfigure.LynxiProduct_Scene_Link_Light]
                for sceneryVariant in sceneryVariants:
                    dic[(sceneryIndex, sceneryVariant)] = description, sceneryCategory, sceneryName, sceneryPriority, sceneryEnabled, scLayoutEnable, scAnimationEnable, scSimulationEnable, scLightEnable
    #
    def getMain(data):
        dic = bscCore.orderedDict()
        if data:
            for i in data:
                sceneryIndex, enabled, description = i
                if enabled is True:
                    getBranch(dic, sceneryIndex, description)
        return dic
    return getMain(getCustomData())


#
def isSceneryLinkName(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScnSceneryStages or sceneryStage == lxConfigure.LynxiProduct_Scenery_Link_Scenery:
        boolean = True
    return boolean


#
def isLayoutLinkName(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScLayoutStages or sceneryStage == lxConfigure.LynxiProduct_Scene_Link_layout:
        boolean = True
    return boolean


#
def isAnimationLinkName(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScAnimationStages or sceneryStage == lxConfigure.LynxiProduct_Scene_Link_Animation:
        boolean = True
    return boolean


#
def isSimulationLinkName(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScSimulationStages or sceneryStage == lxConfigure.LynxiProduct_Scene_Link_Simulation:
        boolean = True
    return boolean


#
def isLightLinkName(sceneryStage):
    boolean = False
    if sceneryStage in lxConfigure.LynxiScLightStages or sceneryStage == lxConfigure.LynxiProduct_Scene_Link_Light:
        boolean = True
    return boolean


#
def sceneryLinkFolder(sceneryStage):
    string = prsVariants.Util.scnSceneryFolder
    if isSceneryLinkName(sceneryStage):
        string = prsVariants.Util.scnSceneryFolder
    elif isLayoutLinkName(sceneryStage):
        string = prsVariants.Util.scnLayoutFolder
    elif isAnimationLinkName(sceneryStage):
        string = prsVariants.Util.scnAnimationFolder
    elif isSimulationLinkName(sceneryStage):
        string = prsVariants.Util.scnSimulationFolder
    elif isLightLinkName(sceneryStage):
        string = prsVariants.Util.scnLightFolder
    return string


#
def scenerySourceFileLabel(sceneryStage):
    string = prsVariants.Util.scnScenerySourceLabel
    if isSceneryLinkName(sceneryStage):
        string = prsVariants.Util.scnScenerySourceLabel
    elif isLayoutLinkName(sceneryStage):
        string = prsVariants.Util.scnLayoutSourceLabel
    elif isAnimationLinkName(sceneryStage):
        string = prsVariants.Util.scnAnimationSourceLabel
    elif isSimulationLinkName(sceneryStage):
        string = prsVariants.Util.scnSimulationSourceLabel
    elif isLightLinkName(sceneryStage):
        string = prsVariants.Util.scnLightSourceLabel
    return string


#
def scnProductFileLabel(sceneryStage):
    subLabelString = prsVariants.Util.basicProductSubLabel
    return bscMethods.StrUnderline.toLabel(prsMethods.Scenery.toLinkMainLabelname(sceneryStage), subLabelString)


#
def scnAssemblyLabel(sceneryStage):
    subLabelString = prsVariants.Util.basicAssemblySubLabel
    return bscMethods.StrUnderline.toLabel(prsMethods.Scenery.toLinkMainLabelname(sceneryStage), subLabelString)


#
def sceneryPreviewFileLabel(sceneryStage):
    string = prsVariants.Util.scnSceneryPreviewLabel
    if isSceneryLinkName(sceneryStage):
        string = prsVariants.Util.scnSceneryPreviewLabel
    elif isLayoutLinkName(sceneryStage):
        string = prsVariants.Util.scnLayoutPreviewLabel
    elif isAnimationLinkName(sceneryStage):
        string = prsVariants.Util.scnAnimationPreviewLabel
    elif isSimulationLinkName(sceneryStage):
        string = prsVariants.Util.scnSimulationPreviewLabel
    elif isLightLinkName(sceneryStage):
        string = prsVariants.Util.scnLightPreviewLabel
    return string


#
def sceneryDefinitionFileLabel(sceneryStage):
    string = prsVariants.Util.scnSceneryDefinitionLabel
    if isSceneryLinkName(sceneryStage):
        string = prsVariants.Util.scnSceneryDefinitionLabel
    if isLayoutLinkName(sceneryStage):
        string = prsVariants.Util.scnDefLayoutinitionLabel
    elif isAnimationLinkName(sceneryStage):
        string = prsVariants.Util.scnAnimationDefinitionLabel
    elif isSimulationLinkName(sceneryStage):
        string = prsVariants.Util.scnSimulationDefinitionLabel
    elif isLightLinkName(sceneryStage):
        string = prsVariants.Util.scnLightDefinitionLabel
    return string


#
def scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel):
    string = '%s%s%s' % (sceneryName, fileLabel, extLabel)
    return string


# Scenery Path
def sceneryUnitBasicDirectory(rootIndexKey, projectName):
    root = [prsVariants.Util.serverSceneryRoot, prsVariants.Util.localSceneryRoot, prsVariants.Util.backupSceneryRoot]
    return '%s/%s/%s/%s' % (root[rootIndexKey], projectName, prsVariants.Util.basicSceneryFolder, prsVariants.Util.scnUnitFolder)


#
def sceneryUnitFolder(rootIndexKey, projectName, sceneryCategory, sceneryName):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    osPath = '%s/%s' % (
        basicDirectory,
        sceneryName
    )
    return osPath


#
def scnUnitSourceFile(rootIndexKey, projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = scenerySourceFileLabel(sceneryStage)
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scnUnitProductFile(rootIndexKey, projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = scnProductFileLabel(sceneryStage)
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scnUnitPreviewFile(rootIndexKey, projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage, extLabel=prsVariants.Util.jpgExt):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = sceneryPreviewFileLabel(sceneryStage)
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scnUnitDefinitionFile(rootIndexKey, projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = sceneryDefinitionFileLabel(sceneryStage)
    extLabel = prsVariants.Util.mayaAsciiExt
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def scnUnitAssemblyComposeFile(rootIndexKey, projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage):
    basicDirectory = sceneryUnitBasicDirectory(rootIndexKey, projectName)
    #
    linkFolder = sceneryLinkFolder(sceneryStage)
    fileLabel = scnAssemblyLabel(sceneryStage)
    extLabel = prsVariants.Util.assemblyComposeExt
    #
    osFileName = scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel)
    fileString_ = '{0}/{1}/{2}/{3}/{4}'.format(
        basicDirectory,
        sceneryName, sceneryVariant,
        linkFolder,
        osFileName
    )
    return osFileName, fileString_


#
def getScnAssemblyComposeDatumDic(projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage):
    dic = {}
    serverFile = scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = bscMethods.OsJson.read(serverFile)
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
def getSceneryUnitProductUpdate(projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage):
    string = prsVariants.Util.infoNonExistsLabel
    #
    serverProductFile = scnUnitProductFile(
        lxConfigure.LynxiRootIndex_Server, projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    if bscMethods.OsFile.isExist(serverProductFile):
        data = bscMethods.OsFile.mtimeChnPrettify(serverProductFile)
        if data:
            string = data
    return string


#
def getScnUnitPreviewFile(projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage):
    renderPreviewFile = scnUnitPreviewFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
        extLabel=prsVariants.Util.pngExt
    )[1]
    if bscMethods.OsFile.isExist(renderPreviewFile):
        return renderPreviewFile
    else:
        viewportPreviewFile = scnUnitPreviewFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
            extLabel=prsVariants.Util.jpgExt
        )[1]
        if bscMethods.OsFile.isExist(viewportPreviewFile):
            return viewportPreviewFile
