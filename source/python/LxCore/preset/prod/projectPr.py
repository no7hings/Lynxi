# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
from LxCore.preset import basicPr, pipePr
#
guidePresetKey = lxConfigure.LynxiProjectPresetKey
#
serverBasicPath = lxConfigure._getLxBasicPath()
#
localBasicPath = lxConfigure.getLxUserOsPath()
#
none = ''


#
def localProjectPresetFile():
    return basicPr.localPresetFile()


#
def localMayaProjectPresetFile(mayaVersion):
    return basicPr.localAppProjectPresetFile(lxConfigure.Lynxi_App_Maya, mayaVersion)


#
def getProjectPresetVariantDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    return basicPr.getGuidePresetVariantDic(guidePresetKey, projectName)


#
def getProjectMayaShelfPresetDic(projectName):
    mainPresetKey = lxConfigure.LynxiMayaPresetKey
    subPresetKey = lxConfigure.LynxiShelfPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


#
def getProjectMayaShelfDataDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    dic = lxBasic.orderedDict()
    data = getProjectMayaShelfPresetDic(projectName)
    if data:
        isTd = lxConfigure.isLxPipelineTd()
        if isTd:
            isAdmin = True
        else:
            isAdmin = False
        #
        for k, v in data.items():
            if k.endswith('PresetTool'):
                if isAdmin:
                    dic[k] = v
            elif not k.endswith('PresetTool'):
                dic[k] = v
    #
    return dic


#
def getProjectMayaToolPresetDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.LynxiMayaPresetKey
    subPresetKey = lxConfigure.LynxiKitPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


#
def getProjectMayaToolDataDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    dic = lxBasic.orderedDict()
    data = getProjectMayaToolPresetDic(projectName)
    if data:
        for k, v in data.items():
            if v:
                subDic = lxBasic.orderedDict()
                for ik, iv in v.items():
                    var = str
                    pathCmd = lxBasic._toVariantConvert('var', iv)
                    exec pathCmd
                    subDic[ik] = var
                dic[k] = subDic
    return dic


#
def getProjectMayaToolSubDataDic(toolPath):
    dic = lxBasic.orderedDict()
    #
    osFiles = lxBasic.getOsFilesByPath(toolPath)
    if osFiles:
        for osFile in osFiles:
            command = lxBasic.readOsFile(osFile)
            if command:
                commandName = lxBasic.getOsFileName(osFile)
                #
                toolTip = none
                #
                toolTipFile = lxBasic.getOsFileReplaceExt(osFile, '.tip')
                tipData = lxBasic.readOsFileLines(toolTipFile)
                if tipData:
                    toolTip = [unicode(i, "gbk").replace('\r\n', none) for i in tipData]
                #
                if osFile.endswith('.py'):
                    commandReduce = 'python({0});'.format(lxBasic.getJsonDumps(command))
                    dic[commandName] = osFile, commandReduce, toolTip
                #
                if osFile.endswith('.mel'):
                    dic[commandName] = osFile, command, toolTip
    return dic


#
def getProjectMayaScriptPresetDic(projectName):
    mainPresetKey = lxConfigure.LynxiMayaPresetKey
    subPresetKey = lxConfigure.LynxiScriptPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


#
def getProjectMayaTdPresetDic(projectName):
    mainPresetKey = lxConfigure.LynxiMayaPresetKey
    subPresetKey = lxConfigure.LynxiTdPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


# noinspection PyShadowingNames
def getProjectMayaScriptDataDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    dic = lxBasic.orderedDict()
    #
    data = getProjectMayaScriptPresetDic(projectName)
    if data:
        for k, v in data.items():
            if v:
                for ik, iv in v.items():
                    var = ''
                    pathCmd = lxBasic._toVariantConvert('var', iv)
                    exec pathCmd
                    if var:
                        dic.setdefault(k, []).append(var)
    return dic


#
def getProjectMayaTdPackagePathLis(projectName):
    lis = []
    #
    dataDic = getProjectMayaTdPresetDic(projectName)
    if dataDic:
        for k, v in dataDic.items():
            if v:
                mayaPackageStr = v[lxConfigure.LynxiMayaPackageKey]
                #
                var = ''
                pathCmd = lxBasic._toVariantConvert('var', mayaPackageStr)
                exec pathCmd
                #
                if var:
                    lis.append(var)
    return lis


#
def getMaCustomPlugPresetDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.LynxiMayaPresetKey
    subPresetKey = lxConfigure.LynxiPlugPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


#
def getIsCloseMaya(sourceProjectName, targetProjectName):
    boolean = False
    sourcePlugData = getMaCustomPlugPresetDic(sourceProjectName)
    targetPlugData = getMaCustomPlugPresetDic(targetProjectName)
    if not targetPlugData == sourcePlugData:
        boolean = True
    return boolean


#
def getMaCustomPlugPathDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    dic = lxBasic.orderedDict()
    data = getMaCustomPlugPresetDic(projectName)
    # Customize
    if data:
        mayaVersion = getProjectMayaVersion(projectName)
        for k, v in data.items():
            plugName = k
            plugVersion = v[lxConfigure.LynxiPlugVersionKey]
            plugPath = basicPr.localAppPlugPath(lxConfigure.Lynxi_App_Maya, mayaVersion, plugName, plugVersion)
            dic[plugName] = plugPath
    # Definition
    plugName, plugVersion = 'lynxinode', '1.0'
    dic[plugName] = basicPr.localAppPlugPath(lxConfigure.Lynxi_App_Maya, 'definition', plugName, plugVersion)
    #
    return dic


#
def getProjectMayaRenderer(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.LynxiBasicPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaRendererKey)


#
def isMayaUsedArnoldRenderer():
    boolean = False
    renderer = getProjectMayaRenderer()
    if renderer == lxConfigure.LynxiArnoldRendererValue:
        boolean = True
    return boolean


#
def getProjectMayaTimeUnit(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.LynxiBasicPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaTimeUnitKey)


#
def getProjectEpisodes(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.LynxiBasicPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.LynxiEpisodePresetKey)


#
def getProjectMayaVersion(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    if projectName.startswith(lxConfigure.Lynxi_Keyword_Project_Default):
        return projectName.split('_')[-1]
    else:
        mainPresetKey = lxConfigure.LynxiMayaPresetKey
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
        return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaVersionKey)


#
def getProjectMayaCommonPlugLoadNames(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.LynxiMayaPresetKey
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaCommonPlugsKey)


#
def getProjectMayaCustomPlugLoadNames(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    lis = []
    data = getMaCustomPlugPresetDic(projectName)
    if data:
        for k, v in data.items():
            autoLoad = v[lxConfigure.LynxiPlugAutoLoadKey]
            if autoLoad is True:
                loadNames = v[lxConfigure.LynxiPlugLoadNamesKey]
                if loadNames:
                    lis.extend(loadNames)
    return lis


#
def getProjectMayaCustomPlugCheckDic(projectName=None):
    if projectName is None:
        projectName = getMayaProjectName()
        #
    dic = lxBasic.orderedDict()
    data = getMaCustomPlugPresetDic(projectName)
    # Customize
    if data:
        mayaVersion = getProjectMayaVersion(projectName)
        for k, v in data.items():
            plugName = k
            autoLoad = v[lxConfigure.LynxiPlugAutoLoadKey]
            if autoLoad is True:
                plugVersion = v[lxConfigure.LynxiPlugVersionKey]
                loadNames = v[lxConfigure.LynxiPlugLoadNamesKey]
                plugPath = basicPr.localAppPlugPath(lxConfigure.Lynxi_App_Maya, mayaVersion, plugName, plugVersion)
                dic[plugName] = loadNames, plugPath
    #
    return dic


#
def getProjectMayaCustomPlugSetupCommands(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    lis = []
    data = getMaCustomPlugPresetDic(projectName)
    if data:
        mayaVersion = getProjectMayaVersion(projectName)
        for k, v in data.items():
            plugName = k
            plugVersion = v[lxConfigure.LynxiPlugVersionKey]
            setupPyFile = basicPr.serverPlugSetupPy(lxConfigure.Lynxi_App_Maya, mayaVersion, plugName, plugVersion)
            if lxBasic.isOsExistsFile(setupPyFile):
                setupCommand = open(setupPyFile, 'r').read()
                setupCommandReduce = 'python({0});'.format(lxBasic.getJsonDumps(setupCommand))
                lis.append(setupCommandReduce)
    #
    return lis


#
def getProjectPath(projectName):
    if '@' in projectName:
        subName, mainName = projectName.split('@')
        projectName = mainName + '/' + subName
    return projectName


#
def getProjectNames():
    return basicPr.getPresetSchemes((guidePresetKey,))


#
def getProjectNameDic():
    return basicPr.getUiPresetSchemeDataDic((guidePresetKey, ))


#
def getProjectDescription(projectName):
    string = none
    data = basicPr.getUiPresetSchemeDataDic((guidePresetKey, ))
    if data:
        if projectName in data:
            string = data[projectName][1]
    return string


#
def getProjectViewInfo(projectName):
    string = u'项目 : {0}' .format(
        getProjectDescription(projectName)
    )
    return string


#
def getAppProjectNames():
    if lxBasic.isMayaApp():
        lis = getMayaProjectNames()
    else:
        lis = getProjectNames()
    return lis


#
def getMayaProjectNames(mayaVersion=None):
    lis = []
    if lxBasic.isMayaApp():
        projectNameLis = getProjectNames()
        if projectNameLis:
            for projectName in projectNameLis:
                projectMayaVersion = getProjectMayaVersion(projectName)
                if mayaVersion is None:
                    currentMayaVersion = lxBasic.getMayaAppVersion()
                else:
                    currentMayaVersion = mayaVersion
                #
                if str(projectMayaVersion) == currentMayaVersion:
                    lis.append(projectName)
    return lis


#
def getMayaProjectNameDic():
    dic = lxBasic.orderedDict()
    if lxBasic.isMayaApp():
        data = getProjectNameDic()
        if data:
            for projectName, (enabled, description) in data.items():
                mayaVersion = getProjectMayaVersion(projectName)
                currentMayaVersion = lxBasic.getMayaAppVersion()
                if str(mayaVersion) == currentMayaVersion:
                    dic[projectName] = enabled, description
    else:
        pass
    return dic


# Get Project's Name
def getProjectName():
    # String <Project Name>
    string = lxConfigure.LynxiDefaultProjectValue
    osFile = localProjectPresetFile()
    if not lxBasic.isOsExistsFile(osFile):
        setLocalProjectPreset(string)
    else:
        data = lxBasic.readOsJson(osFile)
        if data:
            string = data[guidePresetKey]
    #
    return string


#
def getAppProjectName():
    if lxBasic.isMayaApp():
        string = getMayaProjectName()
    else:
        string = getProjectName()
    return string


# Get Project's Name
def getMayaProjectName():
    if lxBasic.isMayaApp():
        mayaVersion = lxBasic.getMayaAppVersion()
        string = '{}_{}'.format(lxConfigure.Lynxi_Keyword_Project_Default, mayaVersion)
        #
        environValue = getMayaProjectEnviron()
        if environValue is not None:
            string = environValue
        else:
            currentMayaVersion = lxBasic.getMayaAppVersion()
            osFile = localMayaProjectPresetFile(currentMayaVersion)
            if not lxBasic.isOsExistsFile(osFile):
                setLocalMayaProjectPreset(string, currentMayaVersion)
            #
            data = lxBasic.readOsJson(osFile)
            if data:
                string = data[guidePresetKey]
    else:
        string = lxConfigure.LynxiDefaultProjectValue
    #
    setMayaProjectEnviron(string)
    return string


#
def getMayaProjectEnviron():
    environKey = lxConfigure.Lynxi_Key_Environ_Project
    return lxBasic.getOsEnvironValue(environKey)


#
def setMayaProjectEnviron(projectName):
    if lxBasic.isMayaApp():
        environKey = lxConfigure.Lynxi_Key_Environ_Project
        lxBasic.setOsEnvironValue(environKey, projectName)


#
def getProjectProxyExt(projectName=none):
    usedRenderer = getProjectMayaRenderer(projectName)
    osExt = '.prx'
    if usedRenderer == lxConfigure.LynxiArnoldRendererValue:
        osExt = '.ass'
    if usedRenderer == lxConfigure.LynxiRedshiftRendererValue:
        osExt = '.rs'
    return osExt


#
def setLocalAppProjectPreset(projectName):
    if lxBasic.isMayaApp():
        pass
    else:
        setLocalProjectPreset(projectName)


# Set Project Config
def setLocalProjectPreset(projectName):
    osFile = localProjectPresetFile()
    lxBasic.setOsFilePathCreate(osFile)
    data = dict(project=projectName)
    lxBasic.writeOsJson(data, osFile)


# Set Project Config
def setLocalMayaProjectPreset(projectName, mayaVersion):
    if lxBasic.isMayaApp():
        osFile = localMayaProjectPresetFile(mayaVersion)
        lxBasic.setOsFilePathCreate(osFile)
        data = dict(project=projectName)
        lxBasic.writeOsJson(data, osFile)


# Set Project Config
def setLocalMayaPlugPreset(projectName, mayaVersion):
    osFile = localMayaProjectPresetFile(mayaVersion)
    lxBasic.setOsFilePathCreate(osFile)
    data = dict(project=projectName)
    lxBasic.writeOsJson(data, osFile)


#
def getAssetClassifyDic(astBasicClassifications):
    dic = lxBasic.orderedDict()
    for i in astBasicClassifications:
        dic[i[0].lower()] = i
    return dic


#
def getAssetClassifyAbbLabelDic(astBasicClassifications):
    dic = lxBasic.orderedDict()
    for i in astBasicClassifications:
        dic[i] = i[0].lower()
    return dic


#
def getProjectServerRootLis(projectName=none):
    lis = []
    if not projectName:
        projectName = getMayaProjectName()
    #
    guideSchemeKey = projectName
    mainPresetKey = lxConfigure.LynxiStoragePresetKey
    subPresetKey = lxConfigure.LynxiRootPresetKey
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    dic = basicPr.getSubPresetSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)
    #
    key = lxConfigure.LynxiServerRootKey
    if dic:
        if key in dic:
            data = dic[key]
            if data:
                for k, v in data.items():
                    projectRoot = '{0}/{1}'.format(v, projectName)
                    if not projectRoot in lis:
                        lis.append(projectRoot)
    #
    return lis


#
def getProjectLocalRootLis(projectName=none):
    lis = []
    if not projectName:
        projectName = getMayaProjectName()
    #
    guideSchemeKey = projectName
    mainPresetKey = lxConfigure.LynxiStoragePresetKey
    subPresetKey = lxConfigure.LynxiRootPresetKey
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    dic = basicPr.getSubPresetSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)
    #
    key = lxConfigure.LynxiLocalRootKey
    if dic:
        if key in dic:
            data = dic[key]
            if data:
                for subKey, root in data.items():
                    projectRoot = '{0}/{1}'.format(root, projectName)
                    if not projectRoot in lis:
                        lis.append(projectRoot)
    #
    return lis


#
def getProjectRootDic(projectName=none):
    outDic = lxBasic.orderedDict()
    #
    if not projectName:
        projectName = getMayaProjectName()
    #
    guideSchemeKey = projectName
    mainPresetKey = lxConfigure.LynxiStoragePresetKey
    subPresetKey = lxConfigure.LynxiRootPresetKey
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    dic = basicPr.getSubPresetSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)
    if dic:
        for k, v in dic.items():
            for ik, iv in v.items():
                outDic.setdefault(ik, []).append(iv)
    #
    return outDic


#
def getIsCacheUseMultLine():
    return False


#
def getProjectExtendDatumDic(projectNameFilter=None):
    dic = lxBasic.orderedDict()
    #
    data = getProjectNameDic()
    if data:
        for projectName, (enable, description) in data.items():
            filterEnable = False
            if projectNameFilter is not None:
                if projectName == projectNameFilter:
                    filterEnable = True
            else:
                filterEnable = True
            #
            if filterEnable is True and (enable is True or enable is None):
                projectIndex = lxBasic.getUniqueId(projectName)
                dic[projectIndex] = projectName, description
    return dic