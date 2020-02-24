# coding=utf-8
from LxBasic import bscMtdCore, bscMethods

from LxScheme import shmOutput
#
from LxPreset import prsConfigure, prsOutputs, prsMethods

# do not delete and rename
serverBasicPath = shmOutput.Root().basic.server
localBasicPath = shmOutput.Root().basic.local
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
    return prsOutputs.Util.Lynxi_Prefix_Product_scenery + formatString.format(*args)


# Group Name Config
def scnBasicGroupNameSet(*args):
    return scnBasicNameSet(*args) + prsOutputs.Util.basicGroupLabel


#
def scnBasicNodeNameSet(*args):
    return scnBasicNameSet(*args)


# Group Name Config
def scnGroupNameSet(sceneryName, groupNameLabel):
    nameSet = '%s_%s%s%s' % (
        prsOutputs.Util.Lynxi_Prefix_Product_scenery, sceneryName, groupNameLabel, prsOutputs.Util.basicGroupLabel)
    return nameSet


#
def scnComposeRootGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, prsOutputs.Util.basicComposeRootGroupLabel)
    return string


#
def scnUnitRootGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, prsOutputs.Util.basicUnitRootGroupLabel)
    return string


#
def scnAssemblyGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, prsOutputs.Util.basicAssemblyLabel)


#
def scnAssemblyFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsOutputs.Util.basicAssemblyLabel, prsOutputs.Util.basicFieldLabel))


#
def scnGpuFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsOutputs.Util.basicGpuLabel, prsOutputs.Util.basicFieldLabel))


#
def scnProxyFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsOutputs.Util.basicProxyLabel, prsOutputs.Util.basicFieldLabel))


#
def scnControlFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsOutputs.Util.basicControlLabel, prsOutputs.Util.basicFieldLabel))


#
def scnAssetFieldGroupName(sceneryName, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicGroupNameSet(sceneryName, bscMethods.StrUnderline.toLabel(
        prsOutputs.Util.basicAssetLabel, prsOutputs.Util.basicFieldLabel))


#
def scnUnitLocatorName(sceneryName, sceneryVariant, namespace=None):
    return ('' if namespace is None else namespace + ':') + scnBasicNodeNameSet(sceneryName, sceneryVariant, prsOutputs.Util.basicAssemblyLabel)


#
def scnAssemblyGroupPath(sceneryName, namespace=none):
    return '|' + '|'.join([scnUnitRootGroupName(sceneryName, namespace), scnAssemblyGroupName(sceneryName, namespace)])


#
def scnLightGroupName(sceneryName, namespace=none):
    string = [none, namespace + ':'][namespace is not none] + scnGroupNameSet(sceneryName, prsOutputs.Util.basicLightLinkGroupLabel)
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
    dic = bscMtdCore.orderedDict()
    dic[17] = 'LOD00'
    dic[14] = 'LOD01'
    dic[6] = 'LOD02'
    return dic


# Scenery AD Name
def scnAssemblyAdName(sceneryCategory, sceneryName, sceneryVariant=none):
    string = '%s_%s_%s%s' % (prsOutputs.Util.Lynxi_Prefix_Product_scenery, sceneryName, sceneryVariant, prsOutputs.Util.scnSceneryDefinitionLabel)
    return string


# Scenery AR Name
def scnAssemblyArName(sceneryCategory, sceneryName, sceneryVariant=none):
    string = '%s_%s_%s%s' % (prsOutputs.Util.Lynxi_Prefix_Product_scenery, sceneryName, sceneryVariant, prsOutputs.Util.scnSceneryReferenceLabel)
    return string


#
def assemblyGroupArName(sceneryName):
    string = '%s_%s%s' % (
        prsOutputs.Util.scnAssemblyPrefix, sceneryName, prsOutputs.Util.scnSceneryReferenceLabel)
    return string


# Scenery Main Locator
def sceneryMainLocatorName(sceneryCategory, sceneryName, sceneryVariant):
    string = '%s_%s_%s%s' % (
        prsOutputs.Util.scnAssemblyPrefix, sceneryName, sceneryVariant, prsOutputs.Util.scnSceneryLocatorLabel)
    return string


# Scenery Main Locator
def sceneryAssemblyMainLocatorName(sceneryName, sceneryVariant):
    string = '%s_%s_%s%s' % (
        prsOutputs.Util.scnAssemblyPrefix, sceneryName, sceneryVariant, prsOutputs.Util.scnSceneryLocatorLabel)
    return string


# Scene Object Locator Name
def sceneryAssemblySubLocatorName(assetName, number, assetVariant):
    string = '%s_%s_%s_%s%s' % (
        prsOutputs.Util.scnAssemblyPrefix, assetName, number, assetVariant, prsOutputs.Util.scnSceneryLocatorLabel)
    return string


#
def scnRootGroupHierarchyConfig(sceneryName):
    dic = bscMtdCore.orderedDict()
    dic[scnUnitRootGroupName(sceneryName)] = []
    return dic


#
def scnAssemblyHierarchyConfig(sceneryName):
    dic = bscMtdCore.orderedDict()
    # Main
    dic[scnAssemblyGroupName(sceneryName)] = [
        scnAssemblyFieldGroupName(sceneryName)
    ]
    return dic


#
def scnLightHierarchyConfig(sceneryName):
    dic = bscMtdCore.orderedDict()
    # Main
    dic[scnLightGroupName(sceneryName)] = [
        scnGroupNameSet(sceneryName, prsOutputs.Util.lgtFieldLabel)
    ]
    return dic


#
def isSceneryStage(sceneryStage):
    boolean = False
    if sceneryStage in prsOutputs.Util.scnSceneryStages:
        boolean = True
    return boolean


#
def isAssemblyStage(sceneryStage):
    boolean = False
    if sceneryStage in prsOutputs.Util.scnAssemblyStages:
        boolean = True
    return boolean


#
def scenerySchemeFileConfig():
    string = '{0}/{1}/{2}/{3}'.format(
        prsOutputs.Util.dbSceneryRoot,
        prsOutputs.Util.dbBasicFolderName,
        prsConfigure.Utility.LynxiSchemeExt,
        prsOutputs.Util.dbSceneryBasicKey
    )
    return bscMethods.OsFile.uniqueName(string)


#
def scenerySetFileConfig(sceneryIndex):
    string = '{0}/{1}/{2}/{3}'.format(
        prsOutputs.Util.dbSceneryRoot,
        prsOutputs.Util.dbBasicFolderName,
        prsConfigure.Utility.LynxiSetExt,
        sceneryIndex
    )
    return string


#
def defaultScenerySchemeConfig():
    lis = [
        True,
        u'请输入备注'
    ]
    return lis


# Scheme Data
def getUiScenerySchemeDataDic():
    def getCustomData():
        fileString_ = scenerySchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getDic(data):
        dic = bscMtdCore.orderedDict()
        if data:
            for i in data:
                scheme, enabled, description = i
                dic[scheme] = enabled, description
        return dic
    #
    return getDic(getCustomData())


#
def getSceneryViewName(sceneryIndex):
    def getCustomData():
        fileString_ = scenerySchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getSubDic(data):
        dic = bscMtdCore.orderedDict()
        if data:
            for i in data:
                scheme, enabled, description = i
                dic[scheme] = description
        return dic
    #
    def getMain(customDic):
        string = prsConfigure.Utility.DEF_value_preset_unspecified
        if sceneryIndex in customDic:
            string = customDic[sceneryIndex]
        return string
    #
    return getMain(getSubDic(getCustomData()))


#
def getSceneryClass(sceneryIndex):
    def getCustomData():
        fileString_ = scenerySetFileConfig(sceneryIndex)
        return bscMethods.OsJsonFile.read(fileString_)
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
        return bscMethods.OsJsonFile.read(fileString_)
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
        return bscMethods.OsJsonFile.read(fileString_)
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
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getMain(customDic):
        if customDic:
            return customDic['variant']
    #
    return getMain(getCustomData())


#
def sceneryViewInfoSet(sceneryViewName, sceneryCategory, sceneryVariant):
    string = u'{} {} ( {} )'.format(
        prsMethods.Scenery.categoryShowname(sceneryCategory),
        sceneryViewName,
        sceneryVariant
    )
    return string


#
def getSceneryViewInfo(sceneryIndex, sceneryCategory=None, sceneryVariant=None):
    if sceneryCategory is None:
        sceneryCategory = getSceneryClass(sceneryIndex)
    if sceneryVariant is None:
        sceneryVariant = prsOutputs.Util.scnDefaultVariant
    return sceneryViewInfoSet(getSceneryViewName(sceneryIndex), sceneryCategory, sceneryVariant)


#
def getSceneryIndexesFilter(projectFilter, sceneryClassFilters=None):
    def getCustomData():
        fileString_ = scenerySchemeFileConfig()
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getBranch(lis, sceneryIndex):
        fileString_ = scenerySetFileConfig(sceneryIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
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
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getLinks(data):
        lis = []
        for i in prsOutputs.Util.scnBasicLinks:
            enabled = data[i]
            if enabled is True:
                lis.append(i)
        return lis
    #
    def getBranch(dic, sceneryIndex, description):
        fileString_ = scenerySetFileConfig(sceneryIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
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
        dic = bscMtdCore.orderedDict()
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
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getBranch(dic, sceneryIndex):
        fileString_ = scenerySetFileConfig(sceneryIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
        if data:
            sceneryName = data['name']
            dic[sceneryName] = sceneryIndex
    #
    def getMain(data):
        dic = bscMtdCore.orderedDict()
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
        return bscMethods.OsJsonFile.read(fileString_)
    #
    def getBranch(dic, sceneryIndex, description):
        fileString_ = scenerySetFileConfig(sceneryIndex)
        data = bscMethods.OsJsonFile.read(fileString_)
        if data:
            projectNames = data['project']
            if projectFilter in projectNames:
                sceneryCategory = data['classify']
                sceneryName = data['name']
                sceneryVariants = data['variant']
                sceneryPriority = data['priority']
                #
                sceneryEnabled = bscMethods.Dict.getAsBoolean(data, prsMethods.Scenery.assemblyLinkName())
                scLayoutEnable = data[prsMethods.Scene.layoutLinkName()]
                scAnimationEnable = data[prsMethods.Scene.animationLinkName()]
                scSimulationEnable = data[prsMethods.Scene.simulationLinkName()]
                scLightEnable = data[prsMethods.Scene.lightLinkName()]
                for sceneryVariant in sceneryVariants:
                    dic[(sceneryIndex, sceneryVariant)] = description, sceneryCategory, sceneryName, sceneryPriority, sceneryEnabled, scLayoutEnable, scAnimationEnable, scSimulationEnable, scLightEnable
    #
    def getMain(data):
        dic = bscMtdCore.orderedDict()
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
    if sceneryStage in prsMethods.Scenery.VAR_product_scenery_assembly_stage_list or sceneryStage == prsMethods.Scenery.assemblyLinkName():
        boolean = True
    return boolean


#
def isLayoutLinkName(sceneryStage):
    boolean = False
    if sceneryStage in prsMethods.Scenery.VAR_product_scenery_layout_stage_list or sceneryStage == prsMethods.Scene.layoutLinkName():
        boolean = True
    return boolean


#
def isAnimationLinkName(sceneryStage):
    boolean = False
    if sceneryStage in prsMethods.Scene.VAR_product_scene_animation_stage_list or sceneryStage == prsMethods.Scene.animationLinkName():
        boolean = True
    return boolean


#
def isSimulationLinkName(sceneryStage):
    boolean = False
    if sceneryStage in prsMethods.Scene.VAR_product_scene_simulation_stage_list or sceneryStage == prsMethods.Scene.simulationLinkName():
        boolean = True
    return boolean


#
def isLightLinkName(sceneryStage):
    boolean = False
    if sceneryStage in prsMethods.Scene.VAR_product_scene_light_stage_list or sceneryStage == prsMethods.Scene.lightLinkName():
        boolean = True
    return boolean


#
def sceneryLinkFolder(sceneryStage):
    string = prsOutputs.Util.scnSceneryFolder
    if isSceneryLinkName(sceneryStage):
        string = prsOutputs.Util.scnSceneryFolder
    elif isLayoutLinkName(sceneryStage):
        string = prsOutputs.Util.scnLayoutFolder
    elif isAnimationLinkName(sceneryStage):
        string = prsOutputs.Util.scnAnimationFolder
    elif isSimulationLinkName(sceneryStage):
        string = prsOutputs.Util.scnSimulationFolder
    elif isLightLinkName(sceneryStage):
        string = prsOutputs.Util.scnLightFolder
    return string


#
def scenerySourceFileLabel(sceneryStage):
    string = prsOutputs.Util.scnScenerySourceLabel
    if isSceneryLinkName(sceneryStage):
        string = prsOutputs.Util.scnScenerySourceLabel
    elif isLayoutLinkName(sceneryStage):
        string = prsOutputs.Util.scnLayoutSourceLabel
    elif isAnimationLinkName(sceneryStage):
        string = prsOutputs.Util.scnAnimationSourceLabel
    elif isSimulationLinkName(sceneryStage):
        string = prsOutputs.Util.scnSimulationSourceLabel
    elif isLightLinkName(sceneryStage):
        string = prsOutputs.Util.scnLightSourceLabel
    return string


#
def scnProductFileLabel(sceneryStage):
    subLabelString = prsOutputs.Util.basicProductSubLabel
    return bscMethods.StrUnderline.toLabel(prsMethods.Scenery.toLinkMainLabelname(sceneryStage), subLabelString)


#
def scnAssemblyLabel(sceneryStage):
    subLabelString = prsOutputs.Util.basicAssemblySubLabel
    return bscMethods.StrUnderline.toLabel(prsMethods.Scenery.toLinkMainLabelname(sceneryStage), subLabelString)


#
def sceneryPreviewFileLabel(sceneryStage):
    string = prsOutputs.Util.scnSceneryPreviewLabel
    if isSceneryLinkName(sceneryStage):
        string = prsOutputs.Util.scnSceneryPreviewLabel
    elif isLayoutLinkName(sceneryStage):
        string = prsOutputs.Util.scnLayoutPreviewLabel
    elif isAnimationLinkName(sceneryStage):
        string = prsOutputs.Util.scnAnimationPreviewLabel
    elif isSimulationLinkName(sceneryStage):
        string = prsOutputs.Util.scnSimulationPreviewLabel
    elif isLightLinkName(sceneryStage):
        string = prsOutputs.Util.scnLightPreviewLabel
    return string


#
def sceneryDefinitionFileLabel(sceneryStage):
    string = prsOutputs.Util.scnSceneryDefinitionLabel
    if isSceneryLinkName(sceneryStage):
        string = prsOutputs.Util.scnSceneryDefinitionLabel
    if isLayoutLinkName(sceneryStage):
        string = prsOutputs.Util.scnDefLayoutinitionLabel
    elif isAnimationLinkName(sceneryStage):
        string = prsOutputs.Util.scnAnimationDefinitionLabel
    elif isSimulationLinkName(sceneryStage):
        string = prsOutputs.Util.scnSimulationDefinitionLabel
    elif isLightLinkName(sceneryStage):
        string = prsOutputs.Util.scnLightDefinitionLabel
    return string


#
def scnSceneryFileNameConfig(sceneryName, fileLabel, extLabel):
    string = '%s%s%s' % (sceneryName, fileLabel, extLabel)
    return string


# Scenery Path
def sceneryUnitBasicDirectory(rootIndexKey, projectName):
    root = [prsOutputs.Util.serverSceneryRoot, prsOutputs.Util.localSceneryRoot, prsOutputs.Util.backupSceneryRoot]
    return '%s/%s/%s/%s' % (root[rootIndexKey], projectName, prsOutputs.Util.basicSceneryFolder, prsOutputs.Util.scnUnitFolder)


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
    extLabel = prsOutputs.Util.mayaAsciiExt
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
    extLabel = prsOutputs.Util.mayaAsciiExt
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
def scnUnitPreviewFile(rootIndexKey, projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage, extLabel=prsOutputs.Util.jpgExt):
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
    extLabel = prsOutputs.Util.mayaAsciiExt
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
    extLabel = prsOutputs.Util.assemblyComposeExt
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
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        sceneryCategory, sceneryName, sceneryVariant, sceneryStage
    )[1]
    datumLis = bscMethods.OsJsonFile.read(serverFile)
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
    string = prsOutputs.Util.infoNonExistsLabel
    #
    serverProductFile = scnUnitProductFile(
        prsConfigure.Utility.DEF_value_root_server, projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage
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
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
        extLabel=prsOutputs.Util.pngExt
    )[1]
    if bscMethods.OsFile.isExist(renderPreviewFile):
        return renderPreviewFile
    else:
        viewportPreviewFile = scnUnitPreviewFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
            extLabel=prsOutputs.Util.jpgExt
        )[1]
        if bscMethods.OsFile.isExist(viewportPreviewFile):
            return viewportPreviewFile
