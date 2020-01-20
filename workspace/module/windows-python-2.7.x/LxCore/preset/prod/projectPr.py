# coding=utf-8
from LxBasic import bscMethods, bscCommands

from LxCore import lxConfigure, lxScheme
#
from LxCore.preset import basicPr
#
guidePresetKey = lxConfigure.Lynxi_Key_Preset_Project
# do not delete and rename
serverBasicPath = lxScheme.Root().basic.server
localBasicPath = lxScheme.Root().basic.local
#
none = ''


#
def getProjectPresetVariantDic(projectName=None):
    if projectName is None:
        projectName = getMayaProjectName()
    return basicPr.getGuidePresetVariantDic(guidePresetKey, projectName)


#
def getProjectMayaShelfPresetDic(projectName):
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Maya
    subPresetKey = lxConfigure.Lynxi_Key_Preset_Shelf
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


#
def getProjectMayaShelfDataDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    dic = bscCommands.orderedDict()
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
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Maya
    subPresetKey = lxConfigure.Lynxi_Key_Preset_Kit
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


#
def getProjectMayaToolDataDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    dic = bscCommands.orderedDict()
    data = getProjectMayaToolPresetDic(projectName)
    if data:
        for k, v in data.items():
            if v:
                subDic = bscCommands.orderedDict()
                for ik, iv in v.items():
                    var = str
                    pathCmd = bscCommands.toVariantConvert('var', iv)
                    exec pathCmd
                    subDic[ik] = var
                dic[k] = subDic
    return dic


#
def getProjectMayaToolSubDataDic(toolPath):
    dic = bscCommands.orderedDict()
    #
    osFiles = bscMethods.OsDirectory.filenames(toolPath)
    if osFiles:
        for osFile in osFiles:
            command = bscMethods.OsFile.read(osFile)
            if command:
                commandName = bscCommands.getOsFileName(osFile)
                #
                toolTip = none
                #
                toolTipFile = bscCommands.getOsFileReplaceExt(osFile, '.tip')
                tipData = bscMethods.OsFile.readlines(toolTipFile)
                if tipData:
                    toolTip = [unicode(i, "gbk").replace('\r\n', none) for i in tipData]
                #
                if osFile.endswith('.py'):
                    if bscCommands.isMayaApp():
                        commandReduce = 'python({0});'.format(bscMethods.OsJson.dump(command))
                    else:
                        commandReduce = bscMethods.OsJson.dump(command)

                    dic[commandName] = osFile, commandReduce, toolTip
                #
                if osFile.endswith('.mel'):
                    dic[commandName] = osFile, command, toolTip
    return dic


#
def getProjectMayaScriptPresetDic(projectName):
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Maya
    subPresetKey = lxConfigure.Lynxi_Key_Preset_Script
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


#
def getProjectMayaTdPresetDic(projectName):
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Maya
    subPresetKey = lxConfigure.Lynxi_Key_Preset_Td
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getSubPresetEnabledSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey)


# noinspection PyShadowingNames
def getProjectMayaScriptDatumDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    dic = bscCommands.orderedDict()
    #
    data = getProjectMayaScriptPresetDic(projectName)
    if data:
        for k, v in data.items():
            if v:
                for ik, iv in v.items():
                    var = ''
                    scriptText = bscCommands.toVariantConvert('var', iv)
                    exec scriptText
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
                scriptText = bscCommands.toVariantConvert('var', mayaPackageStr)
                exec scriptText
                #
                if var:
                    lis.append(var)
    return lis


#
def getMaCustomPlugPresetDic(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Maya
    subPresetKey = lxConfigure.Lynxi_Key_Preset_Plug
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
def getProjectMayaRenderer(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Basic
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
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Basic
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaTimeUnitKey)


#
def getProjectEpisodes(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Basic
    guideSchemeKey = projectName
    #
    mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
    return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.Lynxi_Key_Preset_Episode)


#
def getProjectMayaVersion(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    if projectName.startswith(lxConfigure.Lynxi_Keyword_Project_Default):
        return projectName.split('_')[-1]
    else:
        mainPresetKey = lxConfigure.Lynxi_Key_Preset_Maya
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(guidePresetKey, mainPresetKey, guideSchemeKey)
        return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaVersionKey)


#
def getProjectMayaCommonPlugLoadNames(projectName=none):
    if not projectName:
        projectName = getMayaProjectName()
    #
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Maya
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
            autoLoad = v[lxConfigure.Lynxi_Key_Plug_Load_Enable_Auto]
            if autoLoad is True:
                loadNames = v[lxConfigure.Lynxi_Key_Plug_Load_Names]
                if loadNames:
                    lis.extend(loadNames)
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
    if bscCommands.isMayaApp():
        lis = getMayaProjectNames()
    else:
        lis = getProjectNames()
    return lis


#
def getMayaProjectNames(mayaVersion=None):
    lis = []
    if bscCommands.isMayaApp():
        projectNameLis = getProjectNames()
        if projectNameLis:
            for projectName in projectNameLis:
                projectMayaVersion = getProjectMayaVersion(projectName)
                if mayaVersion is None:
                    currentMayaVersion = bscCommands.getMayaAppVersion()
                else:
                    currentMayaVersion = mayaVersion
                #
                if str(projectMayaVersion) == currentMayaVersion:
                    lis.append(projectName)
    return lis


#
def getMayaProjectNameDic():
    dic = bscCommands.orderedDict()
    if bscCommands.isMayaApp():
        data = getProjectNameDic()
        if data:
            for projectName, (enabled, description) in data.items():
                mayaVersion = getProjectMayaVersion(projectName)
                currentMayaVersion = bscCommands.getMayaAppVersion()
                if str(mayaVersion) == currentMayaVersion:
                    dic[projectName] = enabled, description
    else:
        pass
    return dic


# Get Project's Name
def getProjectName():
    # String <Project Name>
    string = lxConfigure.LynxiDefaultProjectValue

    osFile = lxScheme.UserPreset().projectConfigFile
    if not bscCommands.isOsExistsFile(osFile):
        setLocalProjectPreset(string)
    else:
        data = bscMethods.OsJson.read(osFile)
        if data:
            string = data[guidePresetKey]
    #
    return string


#
def getAppProjectName():
    if bscCommands.isMayaApp():
        string = getMayaProjectName()
    else:
        string = getProjectName()
    return string


# Get Project's Name
def getMayaProjectName():
    if bscCommands.isMayaApp():
        mayaVersion = bscCommands.getMayaAppVersion()
        string = '{}_{}'.format(lxConfigure.Lynxi_Keyword_Project_Default, mayaVersion)
        #
        environValue = getMayaProjectEnviron()
        if environValue is not None:
            string = environValue
        else:
            currentMayaVersion = bscCommands.getMayaAppVersion()
            osFile = lxScheme.UserPreset().applicationProjectConfigFile(lxConfigure.Lynxi_App_Maya, mayaVersion)
            if not bscCommands.isOsExistsFile(osFile):
                setLocalMayaProjectPreset(string, currentMayaVersion)
            #
            data = bscMethods.OsJson.read(osFile)
            if data:
                string = data[guidePresetKey]
    else:
        string = lxConfigure.LynxiDefaultProjectValue
    #
    setMayaProjectEnviron(string)
    return string


#
def getMayaProjectEnviron():
    environKey = lxConfigure.Lynxi_Environ_Key_Project
    return bscCommands.getOsEnvironValue(environKey)


#
def setMayaProjectEnviron(projectName):
    if bscCommands.isMayaApp():
        environKey = lxConfigure.Lynxi_Environ_Key_Project
        bscCommands.setOsEnvironValue(environKey, projectName)


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
    if bscCommands.isMayaApp():
        pass
    else:
        setLocalProjectPreset(projectName)


# Set Project Config
def setLocalProjectPreset(projectName):
    osFile = lxScheme.UserPreset().projectConfigFile
    bscMethods.OsFile.createDirectory(osFile)
    data = dict(project=projectName)
    bscMethods.OsJson.write(osFile, data)


# Set Project Config
def setLocalMayaProjectPreset(projectName, mayaVersion):
    if bscCommands.isMayaApp():
        osFile = lxScheme.UserPreset().applicationProjectConfigFile(lxConfigure.Lynxi_App_Maya, mayaVersion)
        bscMethods.OsFile.createDirectory(osFile)
        data = dict(project=projectName)
        bscMethods.OsJson.write(osFile, data)


#
def getAssetClassifyDic(astBasicClassifications):
    dic = bscCommands.orderedDict()
    for i in astBasicClassifications:
        dic[i[0].lower()] = i
    return dic


#
def getAssetClassifyAbbLabelDic(astBasicClassifications):
    dic = bscCommands.orderedDict()
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
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Storage
    subPresetKey = lxConfigure.Lynxi_Key_Preset_Root
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
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Storage
    subPresetKey = lxConfigure.Lynxi_Key_Preset_Root
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
    outDic = bscCommands.orderedDict()
    #
    if not projectName:
        projectName = getMayaProjectName()
    #
    guideSchemeKey = projectName
    mainPresetKey = lxConfigure.Lynxi_Key_Preset_Storage
    subPresetKey = lxConfigure.Lynxi_Key_Preset_Root
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
    dic = bscCommands.orderedDict()
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
                projectIndex = bscMethods.Uuid.str2uuid(projectName)
                dic[projectIndex] = projectName, description
    return dic
