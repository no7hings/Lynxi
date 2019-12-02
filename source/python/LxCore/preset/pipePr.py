# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
from LxCore.preset import basicPr
#
_serverBasicPath = lxConfigure._getLxBasicPath()
_productPath = lxConfigure._getLxProductPath()
#
_userPath = lxConfigure.getLxUserOsPath()
#
_mayaVersion = lxBasic.getMayaAppVersion()
#
configExt = '.config'
#
none = ''


#
def getPipelinePresetVariantDic(pipelineScheme):
    return basicPr.getGuidePresetVariantDic(lxConfigure.LynxiPipelinePresetKey, pipelineScheme)


#
def userPresetFileDic(userPath=_userPath):
    dic = lxBasic.orderedDict()
    dic[lxConfigure.LynxiProjectPresetKey] = '{0}/{1}/{2}{3}'.format(
        userPath, lxConfigure.LynxiPresetKey, lxConfigure.LynxiProjectPresetKey, configExt
    )
    return dic


#
def env_basic_pipeline_dic(basicPath=_serverBasicPath, mayaVersion=_mayaVersion):
    dic = lxBasic.orderedDict()
    dic['config'] = basicPath + '/{0}'.format(lxConfigure.LynxiPresetKey)
    dic['environ'] = basicPath + '/preset/environ'
    dic['project'] = basicPath + '/preset/project'
    dic['team'] = basicPath + '/preset/team'
    dic['artist'] = basicPath + '/preset/artist'
    dic['path'] = basicPath + '/preset/path'
    dic['naming'] = basicPath + '/preset/naming'
    dic['software'] = basicPath + '/preset/software'
    
    dic[lxConfigure.LynxiPresetKey] = basicPath + '/{0}/{1}'.format(lxConfigure.LynxiPresetKey, lxConfigure.LynxiKitPresetKey)
    #
    dic['tool'] = basicPath + '/tool/maya'
    #
    dic['icon'] = basicPath + '/icon'
    #
    dic['windowsPlug'] = _productPath + '/plug/windows'
    dic['windowsPush'] = 'C:/_pipe' + '/plug/windows'
    #
    dic['mayaPlug'] = _productPath + '/plug/maya/' + mayaVersion
    dic['mayaPush'] = 'C:/_pipe' + '/plug/maya/' + mayaVersion
    #
    dic['pythonScript'] = basicPath + '/script/python/'
    dic['windowsScript'] = basicPath + '/script/windows/'
    dic['mayaScript'] = basicPath + '/script/maya/' + mayaVersion
    #
    dic['mayaPython'] = basicPath + '/maya/python'
    dic['mayaLog'] = basicPath + '/log/maya'
    #
    dic['pythonSharePackage'] = basicPath + '/package/python/share/2.7.x'
    dic['mayaPythonPackage'] = basicPath + '/package/python/maya/' + mayaVersion
    dic['mayaDoc'] = basicPath + '/doc/maya'
    #
    dic['mayaLightEnv'] = basicPath + '/maya/asset/' + mayaVersion + '/lightEnv/arnold'
    return dic


#
def env_app_maya_pipeline_dic(mayaVersion):
    dic = lxBasic.orderedDict()
    #
    productPath = lxConfigure._getLxProductPath()
    #
    dic[lxConfigure.Lynxi_Key_Environ_Path_WindowsPlug] = productPath + '/plug/windows'
    dic[lxConfigure.Lynxi_Key_Environ_Path_WindowsPush] = 'C:/_pipe' + '/plug/windows'
    #
    dic[lxConfigure.Lynxi_Key_Environ_Path_MayaPlug] = productPath + '/plug/maya/'
    dic[lxConfigure.Lynxi_Key_Environ_Path_MayaPush] = 'C:/_pipe' + '/plug/maya/'
    return dic


#
def env_app_maya_dic(basicPath=_serverBasicPath, mayaVersion=_mayaVersion):
    dic = lxBasic.orderedDict()
    #
    data = env_basic_pipeline_dic(basicPath, mayaVersion)
    # Script Path
    dic['MAYA_SCRIPT_PATH'] = data['mayaScript']
    # Plug Path
    dic['MAYA_PLUG_IN_PATH'] = data['mayaPlug']
    return dic


#
def env_basic_python_package_lis(basicPath=_serverBasicPath):
    lis = []
    #
    sharePackagePath = basicPath + '/package/python/share/2.7.x'
    lis.append(sharePackagePath)
    return lis


# Pack Path
def env_app_maya_python_package_lis(basicPath=_serverBasicPath, mayaVersion=_mayaVersion):
    # List [ <Path> ]
    lis = []
    data = env_basic_pipeline_dic(basicPath, mayaVersion)
    # Python Packages
    lis.append(data['pythonSharePackage'])
    lis.append(data['mayaPythonPackage'])
    return lis


#
def nameComposePreset():
    dic = lxBasic.orderedDict()
    dic['projectName'] = '< Project Name >'
    #
    dic['astUnitBasicDirectory'] = '< Asset Directory >'
    dic['sceneryDirectory'] = '< Scenery Directory >'
    dic['animationDirectory'] = '< Animation Directory >'
    dic['actDirectory'] = '< Act Directory >'
    dic['lightDirectory'] = '< Light Directory >'
    dic['renderDirectory'] = '< Render Directory >'
    dic['cacheDirectory'] = '< Cache Directory >'
    #
    dic['assetClassify'] = '< Asset Classify >'
    dic['assetClassify'] = '< Asset Classify Label >'
    dic['assetName'] = '< Asset Name >'
    dic['assetVariant'] = '< Asset Variant >'
    dic['assetLabel'] = '< Asset Label >'
    #
    dic['episodeNumber'] = '< Episode Number >'
    dic['sequenceNumber'] = '< Sequence Number >'
    dic['shotNumber'] = '< Shot Number >'
    #
    dic['actName'] = '< Act Name >'
    return dic


#
def projectClassifies():
    lis = [
        'animation',
        'series',
        'game',
    ]
    return lis


#
def astBasicClassifications():
    lis = [
        'character',
        'prop',
    ]
    return lis


#
def assetClassifyPreset():
    classifies = [
        'character',
        'prop',
    ]
    assetClassifyAbbDic = [{i: i[0]} for i in classifies]
    assetClassifyFullDic = [{i[0]: i} for i in classifies]
    return classifies, assetClassifyAbbDic, assetClassifyFullDic


# Shape Config
def objectShapePreset():
    shape = [
        '_shape',
        '_alembic',
        '_shapeDeformed'
    ]
    state = [
        'modeling',
        'shading',
        'rigging'
    ]
    shapeDic = {
        state[0]: shape[0],
        state[1]: shape[1],
        state[2]: shape[2]
    }
    stateDic = {
        shape[0]: state[0],
        shape[1]: state[0],
        shape[2]: state[0]
    }
    lis = [
        shape,
        state,
        shapeDic,
        stateDic
    ]
    return lis


#
def mayaHelpDirectory(keyword):
    osPath = '{0}/{1}/{2}/{3}'.format(_serverBasicPath, 'doc', lxConfigure.Lynxi_App_Maya, keyword)
    return osPath


#
def information():
    osFile = lxConfigure._getLxDevelopVersionFile()
    info = none
    if lxBasic.isOsExistsFile(osFile):
        data = lxBasic.readOsJson(osFile)
        info = data['update']
    return info


#
def getToolPresetData(keyword):
    mainKey = 'tool'
    #
    dic = lxBasic.orderedDict()
    presetPath = env_basic_pipeline_dic()[mainKey]
    subConfigPath = presetPath + '/' + keyword
    #
    osFiles = lxBasic.getOsFilesByPath(subConfigPath)
    if osFiles:
        for osFile in osFiles:
            command = lxBasic.readOsFile(osFile)
            commandName = lxBasic.getOsFileName(osFile)
            #
            toolTip = none
            toolTipFile = lxBasic.getOsFileReplaceExt(osFile, '.tip')
            if lxBasic.isOsExistsFile(toolTipFile):
                data = lxBasic.readOsData(toolTipFile)
                if data:
                    toolTip = [unicode(i, "gbk").replace('\r\n', none) for i in data]
            #
            if osFile.endswith('.py'):
                commandReduce = 'python(' + lxBasic.getJsonDumps(command) + ');'
                dic[commandName] = commandReduce, toolTip
            #
            elif osFile.endswith('.mel'):
                dic[commandName] = command, toolTip
    return dic


#
def getPythonModuleData(modules=none):
    lis = []
    data = lxBasic.getSystemModuleData()
    if data:
        for k, v in data.items():
            root = k.split('.')[0]
            if root in modules:
                lis.append(k)
    lis.sort()
    return lis