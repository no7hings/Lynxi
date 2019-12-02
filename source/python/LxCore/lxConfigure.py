# coding:utf-8
from LxCore import lxBasic
# 0 ( 255, 0, 64 ), 1 (255, 255, 64), 2 (255, 127, 0), 3 (64, 255, 127), 4 (0, 223, 223),
# 5 (191, 191, 191), 6 (223, 223, 223), 7 (127, 127, 127), 8 (0, 0, 0)
LynxiUi_HtmlColor_Lis = [
    '#ff0040',
    '#ffff40',
    '#ff7f00',
    '#40ff7f',
    '#00bfbf',
    '#bfbfbf',
    '#dfdfdf',
    '#7f7f7f',
    '#000000'
]
LynxiPipelineTds = [
    'dongchangbao',
    'changbao.dong'
]
LynxiWindow_Size_Default = 1920 * .85, 1080 * .85
LynxiWindow_SubSize_Default = 1920 * .75, 1080 * .75
LynxiWindow_Size_Dialog = 1920 * .5, 1080 * .5
LynxiPipelineTdPost = 'Pipeline - TD'
LynxiPipelineTdLevel = 3
pipelineTdBasicPaths = [
    'E:/myworkspace/td/lynxi'
]
LynxiPythonModule_Basic_Lis = [
    'LxCore.config.appConfig',
    'LxCore.method.basic._methodBasic',
    'LxCore.method._osMethod',
    'LxCore.method._dbMethod',
    'LxCore.method._uiMethod',
    'LxCore.method._productMethod',
    'LxCore.lxBasic',
    'LxCore.lxConfigure',
    'LxUi.uiCore',
    'LxUi.command.uiHtml',
    'LxUi.qt.uiDefinition',
    'LxUi.qt.uiAbstract',
    'LxUi.qt.uiAction',
    'LxUi.qt.uiBasic.uiModelBasic',
    'LxUi.qt.uiBasic.uiWidgetBasic',
    'LxUi.qt.uiWidgets.uiWindow',
    'LxUi.qt.uiWidgets.uiView',
    'LxUi.qt.uiWidgets.uiGroup',
    'LxUi.qt.uiWidgets.uiItem',
    'LxUi.qt.uiWidgets',
    'LxUi.qt.uiWidgets_',
    'LxUi.qt.uiChart_',
    # Behind Ui
    'LxCore.lxLog',
    'LxCore.lxProgress',
    'LxCore.lxTip',
    'LxCore.config.appCfg',
    'LxCore.config.basicCfg',
    'LxCore.config.assetCfg',
    'LxCore.config.sceneryCfg',
    'LxCore.config.sceneCfg',
    'LxCore.preset.appPr',
    'LxCore.preset.basicPr',
    'LxCore.preset.pipePr',
    'LxCore.preset.prod.projectPr',
    'LxCore.preset.prod.assetPr',
    'LxCore.preset.prod.sceneryPr',
    'LxCore.preset.prod.scenePr',
    'LxCore.preset.plugPr',
    'LxCore.preset.personnelPr',
    'LxCore.preset.appVariant',
    'LxInterface.qt.ifAbstract',
    'LxInterface.qt.ifBasic.ifWidgetBasic',
]
LynxiPythonModule_Maya_Lis = [
    'LxMaya.method.config._maConfig',
    'LxMaya.method.basic._maMethodBasic',
    'LxMaya.method._maUiMethod',
    'LxMaya.method._maMethod',
    'LxMaya.method._maPlugMethod',
    'LxMaya.method._maProductMethod',
    'LxMaya.method',

]
Lynxi_Ui_Family_Lis = [
    'Arial',
    'Arial Unicode MS',
    'Arial Black'
]
# Environ Key
Lynxi_Key_Environ_Path_Basic = 'LYNXI_PATH'
Lynxi_Key_Environ_Path_Develop = 'LYNXI_DEVELOP_PATH'
Lynxi_Key_Environ_Path_Product = 'LYNXI_PRODUCT_PATH'
Lynxi_Key_Environ_Path_ToolKit = 'LYNXI_TOOLKIT_PATH'
Lynxi_Key_Environ_Develop = 'LYNXI_DEVELOP'
# Environ Key
Lynxi_Key_Environ_Version = 'LYNXI_VERSION'
Lynxi_Key_Environ_Update = 'LYNXI_Update'
Lynxi_Key_Environ_Project = 'LYNXI_PROJECT'
Lynxi_Key_Environ_MessageCount = 'LYNXI_MESSAGE_COUNT'
Lynxi_Key_Environ_TooltipAutoShow = 'LYNXI_TOOLTIP_AUTO_SHOW'
Lynxi_Key_Environ_Path_MayaPush = 'LYNXI_MAYA_PUSH_PATH'
Lynxi_Key_Environ_Path_MayaPlug = 'LYNXI_MAYA_PLUG_PATH'
Lynxi_Key_Environ_Path_WindowsPush = 'LYNXI_WINDOWS_PUSH_PATH'
Lynxi_Key_Environ_Path_WindowsPlug = 'LYNXI_WINDOWS_PLUG_PATH'

LynxiUi_Value_TooltipDelayTime = 1000

Lynxi_Folder_Basic = '.lynxi'
Lynxi_App_Maya = 'maya'
LynxiPresetKey = 'preset'
LynxiPipelinePresetKey = 'pipeline'
LynxiVariantPresetKey = 'variant'
LynxiPersonnelPresetKey = 'personnel'
LynxiSoftwarePresetKey = 'software'
LynxiMayaPresetKey = 'maya'
LynxiProjectPresetKey = 'project'
LynxiBasicPresetKey = 'basic'
LynxiDeploymentPresetKey = 'deployment'
LynxiEnvironPresetKey = 'environ'
LynxiSetPresetKey = 'set'
LynxiEpisodePresetKey = 'episode'
LynxiProductionPresetKey = 'production'
LynxiInspectionPresetKey = 'Inspection'
LynxiPreferencePresetKey = 'preference'
LynxiOptionPresetKey = 'option'
LynxiAssetPresetKey = 'asset'
LynxiSceneryPresetKey = 'scenery'
LynxiScenePresetKey = 'scene'
LynxiAnimationPresetKey = 'animation'
LynxiDefinitionPresetKey = 'definition'
LynxiDevelopmentPresetKey = 'development'
LynxiTeamPresetKey = 'team'
LynxiPostPresetKey = 'post'
LynxiUserPresetKey = 'user'
LynxiStoragePresetKey = 'storage'
LynxiRootPresetKey = 'root'
LynxiFilePresetKey = 'file'
LynxiNamePresetKey = 'name'
LynxiDataPresetKey = 'data'
LynxiDatabasePresetKey = 'database'
LynxiDirectoryPresetKey = 'directory'
LynxiNodePresetKey = 'node'
LynxiAttributePresetKey = 'attribute'
LynxiCustomizationPresetKey = 'customization'
LynxiShelfPresetKey = 'shelf'
LynxiShelfToolPresetKey = 'shelfTool'
LynxiKitPresetKey = 'kit'
LynxiAppPresetKey = 'app'
LynxiPlugPresetKey = 'plug'
LynxiRendererPresetKey = 'renderer'
LynxiVersionPresetKey = 'version'
LynxiScriptPresetKey = 'script'
LynxiTdPresetKey = 'td'
LynxiGeneralValue = 'General'
LynxiValue_Unspecified = 'Unspecified'
LynxiDefaultPresetValue = 'Preset_2018'
LynxiDefaultPipelineValue = 'Pipeline_2018'
LynxiDefaultVariantValue = 'Variant_2018'
LynxiDefaultPersonnelValue = 'Personnel_2018'
LynxiDefaultSoftwareValue = 'Software_2018'
LynxiDefaultMayaValue = 'Maya_2018'
Lynxi_Keyword_Project_Default = 'Default_Project'
LynxiDefaultProjectValue = 'Default_Project_2017'
LynxiDefaultSchemeValue = 'Default_Scheme'
LynxiPostLevelKey = 'postLevel'
LynxiUserEnNameKey = 'enName'
LynxiUserCnNameKey = 'cnName'
LynxiUserMailKey = 'mail'
LynxiUserSendMailEnabledKey = 'sendMail'
LynxiDefaultEpisodeKey = '001A'
LynxiMayaTimeUnitKey = 'mayaTimeUnit'
LynxiDefaultTimeUnitValue = '24 fps'
LynxiProjectClassificationKey = 'projectClassification'
LynxiFilmProjectValue = 'Film'
LynxiCgProjectValue = 'CG'
LynxiGameProjectValue = 'Game'
LynxiAppNameKey = 'appName'
LynxiAppNamesKey = 'appNames'
LynxiAppVersionKey = 'appVersion'
LynxiAppVersionsKey = 'appVersions'
LynxiShelfNameKey = 'shelfName'
LynxiToolNameKey = 'toolName'
LynxiScriptNameKey = 'scriptName'
LynxiPlugNameKey = 'plugName'
LynxiPlugVersionKey = 'plugVersion'
LynxiPlugVersionsKey = 'plugVersions'
LynxiPlugLoadNamesKey = 'plugLoadNames'
LynxiPlugAutoLoadKey = 'autoLoad'
LynxiPlugSetupCommandKey = 'plugSetupCommand'
LynxiPlugPathKey = 'plugPath'
LynxiPlugDeployPathKey = 'plugDeployPath'
LynxiPlugModulePathKey = 'plugModulePath'
LynxiPlugRlmPathKey = 'plugRlmPath'
LynxiVariantKey = 'key'
LynxiVariantValue = 'value'
LynxiUiNameKey = 'nameText'
LynxiUiTipKey = 'uiTip'
LynxiServerPathKey = 'serverPath'
LynxiUtilitiesPathKey = 'utilitiesPath'
LynxiLocalPathKey = 'localPath'
LynxiServerRootKey = 'serverRoot'
LynxiLocalRootKey = 'localRoot'
LynxiBackupRootKey = 'backupRoot'
LynxiMayaPackageKey = 'mayaPackage'
LynxiMayaScriptKey = 'mayaScript'
LynxiAssetUploadCommandKey = 'assetUploadCmd'
LynxiAssetLoadCommandKey = 'assetLoadCmd'
LynxiSceneUploadCommandKey = 'sceneUploadCmd'
LynxiSceneLoadCommandKey = 'sceneLoadCmd'
LynxiMayaVersionKey = 'mayaVersion'
LynxiDefaultMayaVersion = '2017'
LynxiMayaCommonPlugsKey = 'mayaCommonPlugs'
LynxiMayaRendererKey = 'mayaRenderer'
LynxiMayaSoftwareRendererValue = 'Maya - Software'
LynxiMayaHardwareRendererValue = 'Maya - Hardware'
LynxiArnoldRendererValue = 'Arnold'
LynxiRedshiftRendererValue = 'Redshift'
LynxiMayaPlugPresetKey = 'mayaPlug'
LynxiSchemeExt = '.index'
LynxiSetExt = '.set'
LynxiUiPathsep = ' > '
LynxiRootIndex_Server = 0
LynxiRootIndex_Local = 1
LynxiRootIndex_Backup = 2
LynxiRootLabelDic = {
    0: 'serverRoot',
    1: 'localRoot',
    2: 'backupRoot'
}
# Module
LynxiProduct_Module_Asset = 'asset'
LynxiProduct_Module_Scenery = 'scenery'
LynxiProduct_Module_Scene = 'scene'
LynxiProduct_Asset_Link_Model = 'model'
LynxiAstModelStages = [
    'model',
    'texture',
    'mdlShader'
]
LynxiProduct_Asset_Link_Rig = 'rig'
LynxiAstRigStages = [
    'rigLayout',
    'rigAnimation'
]
LynxiProduct_Asset_Link_Cfx = 'cfx'
LynxiAstCfxStages = [
    'groom',
    'cfxShader'
]
LynxiProduct_Asset_Link_Solver = 'solver'
LynxiAstRigSolStages = [
    'solverBind'
]
LynxiProduct_Asset_Link_Light = 'light'
LynxiAstLightStages = [
    'light',
    'lgtShader'
]
LynxiProduct_Asset_Link_Assembly = 'assembly'
LynxiAstAssemblyStages = [
    'assembly'
]
LynxiProduct_Scenery_Link_Scenery = 'scenery'
LynxiScnSceneryStages = [
    'scenery'
]
LynxiProduct_Scene_Link_layout = 'layout'
LynxiScLayoutStages = [
    'layout'
]
LynxiProduct_Scene_Link_Animation = 'animation'
LynxiScAnimationStages = [
    'blocking',
    'final',
    'polish'
]
LynxiProduct_Scene_Link_Solver = 'solver'
LynxiScSolverStages = [
    'solverSimulation'
]
LynxiProduct_Scene_Link_Simulation = 'simulation'
LynxiScSimulationStages = [
    'simulation'
]
LynxiProduct_Scene_Link_Light = 'light'
LynxiScLightStages = [
    'shader',
    'light',
    'render'
]
Lynxi_Key_Info_SourceFile = 'link'
LynxiCacheInfoKey = 'cache'
LynxiPoseCacheInfoKey = 'poseCache'
LynxiModelCacheInfoKey = 'modelCache'
LynxiSolverCacheInfoKey = 'solverCache'
LynxiExtraCacheInfoKey = 'extraCache'

Lynxi_Key_Info_Stage = 'stage'
Lynxi_Key_Info_Update = 'update'
Lynxi_Key_Info_Timestamp = 'timestamp'
Lynxi_Key_Info_Version = 'version'
Lynxi_Key_Info_User = 'user'
Lynxi_Key_Info_Artist = 'artist'
Lynxi_Key_Info_HostName = 'hostName'
Lynxi_Key_Info_Host = 'host'
Lynxi_Key_Info_Description = 'description'
Lynxi_Key_Info_Note = 'note'
Lynxi_Key_Info_Notes = 'notes'
Lynxi_Key_Info_Data = 'data'
Lynxi_Key_Info_StartFrame = 'startFrame'
Lynxi_Key_Info_EndFrame = 'endFrame'

Lynxi_Key_Info_Active = 'active'

LynxiSolverInfoKey = 'solver'
LynxiProjectInfoKey = 'project'
LynxiInfoKey_Index = 'index'
LynxiInfoKey_Class = 'classify'
LynxiInfoKey_Name = 'name'
LynxiInfoKey_Variant = 'variant'
LynxiAttributeDataKey = 'attribute'
LynxiAlembicAttrDataKey = 'alembicAttr'
LynxiConnectionDataKey = 'connection'
LynxiNhrConnectionDataKey = 'nhrConnection'
LynxiAssemblyReferenceDataKey = 'assemblyReference'
LynxiTransformationDataKey = 'transformation'
LynxiDatumKey_Extra_WorldMatrix = 'worldMatrix'
LynxiObjectShapeNameAttrName = 'lynxiShapeName'
LynxiTaskTimestampAttrName = 'lynxiTaskTimeStamp'
LynxiUpdateExt = '.update'
LynxiResultExt = '.result'
LynxiScCameraCacheType = 'cameraCache'
LynxiScAstModelCacheType = 'modelCache'
LynxiScAstCfxFurCacheType = 'cfxFurCache'
LynxiScAstExtraCacheType = 'extraCache'
# Ignore Send Message
if lxBasic.getOsUser() in LynxiPipelineTds:
    LynxiIsSendMail = False
    LynxiIsSendDingTalk = False
else:
    LynxiIsSendMail = True
    LynxiIsSendDingTalk = True
LynxiCharacterClassKey = 'character'
LynxiPropClassKey = 'prop'
LynxiAssetClassLis = [
    LynxiCharacterClassKey,
    LynxiPropClassKey
]
LynxiSceneryClassKey = 'scenery'
LynxiMainTimeTag = '0000_0000_0000'
LynxiProduct_Stage_Pending = 'pending'
LynxiProduct_Stage_Wip = 'wip'
LynxiProduct_Stage_Delivery = 'delivery'
LynxiProduct_Stage_Refine = 'refine'
LynxiProduct_Stage_Validated = 'validated'
LynxiAttrName_Object_Transparent = 'lxObjectTransparent'
LynxiAttrName_Object_RenderVisible = 'lxObjectRenderVisible'
none = ''
LynxiDevelopMode = True
varDic = globals()


def _getLxBasicPath():
    data = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_Basic)
    if data:
        string = data.replace('\\', '/')
    else:
        string = 'e:/myworkspace/td/lynxi'
    return string


def _getLxDevelopPath():
    data = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_Develop)
    if data:
        string = data.replace('\\', '/')
    else:
        string = 'e:/myworkspace/td/lynxi'
    return string


def _getLxProductPath():
    envData = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_Product)
    if envData:
        string = envData.replace('\\', '/')
    else:
        string = 'e:/myworkspace/td/lynxi'
    return string


def getLxPythonModulePath():
    string = none
    basicPath = _getLxBasicPath()
    if basicPath:
        string = basicPath + '/module.pyc'
        if isLxDevelop():
            string = basicPath + '/module'
    return string


def getLxPresetPath():
    data = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_Product)
    if data:
        string = data.replace('\\', '/')
    else:
        string = 'e:/myworkspace/td/lynxi'
    return string


def getLxPlugPath():
    if LynxiDevelopMode is True:
        if isLxDevelop():
            data = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_Develop)
        else:
            data = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_Product)
    else:
        data = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_Product)
    if data:
        string = data.replace('\\', '/')
    else:
        string = 'e:/myworkspace/td/lynxi'
    return string


def getLxUserOsPath():
    osUserDocument = lxBasic.getOsDocumentPath()
    string = '{0}/{1}'.format(osUserDocument, Lynxi_Folder_Basic)
    return string


def lxUserFilerHistoryFile():
    return getLxUserOsPath() + '/filter.hist'


def getLxLogPath():
    string = none
    basicPath = _getLxBasicPath()
    if basicPath:
        string = basicPath + '/.log'
    return string


def getLxMayaPlugPath():
    if isLxDevelop():
        data = getLxPlugPath() + '/plug/maya/'
    else:
        data = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_MayaPlug)
    if data:
        string = data
    else:
        string = 'e:/myworkspace/td/lynxi/plug/maya/'
    return string


def getLxMayaPushPath():
    data = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Path_MayaPush)
    if data:
        string = data
    else:
        string = 'C:/_pipe/plug/maya/'
    return string


def _getLxDevelopVersionFile():
    string = none
    basicPath = _getLxBasicPath()
    if basicPath:
        string = basicPath + '/.info/version.info'
    return string


def _getLxDevelopPythonVersionFile():
    string = none
    basicPath = _getLxBasicPath()
    if basicPath:
        string = '{}/.info/python.version'.format(basicPath)
    return string


def getLxRelatedPythonModuleLis():
    lis = ['LxCore', 'LxDatabase', 'LxUi', 'LxInterface']
    if lxBasic.isMayaApp():
        lis.extend(['LxMaya', 'LxDeadline'])
    return lis


def isLxPipelineTd():
    boolean = False
    user = lxBasic.getOsUser()
    if user in LynxiPipelineTds:
        boolean = True
    return boolean


def isLxDevelop():
    boolean = False
    envData = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_Develop)
    if envData:
        if envData.lower() == 'true':
            boolean = True
    return boolean


def setTooltipAutoShow(boolean):
    envValue = str(boolean).upper()
    lxBasic.setOsEnvironValue(Lynxi_Key_Environ_TooltipAutoShow, envValue)


def isTooltipAutoShow():
    boolean = False
    envData = lxBasic.getOsEnvironValue(Lynxi_Key_Environ_TooltipAutoShow)
    if envData:
        if envData == str(True).upper():
            boolean = True
    return boolean


def getLxVariantValue(varName):
    if varName in varDic:
        return varDic[varName]


def setLxVariantValue(varName, value):
    varDic[varName] = value


def lxProductRecordDatumDic(osFile, stage=None, description=None, notes=None):
    dic = lxBasic.orderedDict()
    dic[Lynxi_Key_Info_SourceFile] = osFile
    dic[Lynxi_Key_Info_Update] = lxBasic.getOsActiveTimestamp()
    dic[Lynxi_Key_Info_Artist] = lxBasic.getOsUser()
    dic[Lynxi_Key_Info_HostName] = lxBasic.getOsHostName()
    dic[Lynxi_Key_Info_Host] = lxBasic.getOsHost()
    dic[Lynxi_Key_Info_Stage] = stage
    dic[Lynxi_Key_Info_Description] = description
    dic[Lynxi_Key_Info_Note] = notes
    return dic


# Get Update File
def _toLxProductRecordFile(osFile):
    base = lxBasic.getOsFileBase(osFile)
    string = base + LynxiUpdateExt
    return string


# Get Update File
def _toLxProductResultFile(osFile):
    base = lxBasic.getOsFileBase(osFile)
    string = base + LynxiResultExt
    return string


def traceMessage(text):
    print u'# Lynxi {}'.format(lxBasic.getOsActiveViewTime())
    print u'    {}'.format(text)


def traceResult(text):
    traceMessage(
        u'''# Result {}'''.format(text)
    )


def traceWarning(text):
    traceMessage(
        u'''# Warning {}'''.format(text)
    )


def traceError(text):
    traceMessage(
        u'''# Error {}'''.format(text)
    )


def _setLogAdd(text, osLogFile):
    lxBasic.setOsFilePathCreate(osLogFile)
    with open(osLogFile, 'a') as log:
        log.writelines(u'{} @ {}\n'.format(lxBasic.getOsActiveViewTime(), lxBasic.getOsUser()))
        log.writelines(u'{}\n'.format(text))
        log.close()


def setExceptionLogAdd(text):
    logDirectory = getLxLogPath()
    osLogFile = logDirectory + '/' + '%s.exception.log' % lxBasic.getOsActiveDateTag()
    _setLogAdd(text, osLogFile)


def setErrorLogAdd(text):
    logDirectory = getLxLogPath()
    osLogFile = logDirectory + '/' + '%s.error.log' % lxBasic.getOsActiveDateTag()
    _setLogAdd(text, osLogFile)


def setDevelopLogAdd(text):
    logDirectory = getLxLogPath()
    osLogFile = logDirectory + '/' + '%s.develop.log' % lxBasic.getOsActiveDateTag()
    _setLogAdd(text, osLogFile)


def _getLxBasicIconRoot():
    string = none
    basicPath = _getLxBasicPath()
    if basicPath:
        string = basicPath + '/source/icon'
    return string


Lynxi_Folder_Icon = 'icon'
Lynxi_Folder_Source = 'source'
Lynxi_Folder_Compile = 'compile'
Lynxi_Folder_Python = 'python'
Lynxi_Folder_Qt = 'qt'

Lynxi_Folder_Product = 'product'


class DevelopPath(object):
    def __init__(self, version=None):
        self._version = version

        self._root = _getLxDevelopPath()

    @property
    def root(self):
        return self._root

    @property
    def pythonSourceRoot(self):
        return '{}/{}/{}'.format(self._root, Lynxi_Folder_Source, Lynxi_Folder_Python)

    @property
    def pythonCompileRoot(self):
        return '{}/{}/{}'.format(self._root, Lynxi_Folder_Compile, Lynxi_Folder_Python)

    @property
    def pythonVersionInfoFile(self):
        return '{}/{}/{}.info.json'.format(self._root, Lynxi_Folder_Source, self._version)

    @property
    def iconRoot(self):
        return '{}/{}/{}'.format(self._root, Lynxi_Folder_Source, Lynxi_Folder_Icon)

    def __repr__(self):
        return self._root


class ProductPath(object):
    def __init__(self, version=None):
        if version is not None:
            self._version = version
        else:
            self._version = Version().active()

        self._root = _getLxProductPath()

    @property
    def root(self):
        return self._root

    @property
    def pythonSourceRoot(self):
        return '{}/{}/{}.{}'.format(self._root, Lynxi_Folder_Source, Lynxi_Folder_Python, self._version)

    @property
    def pythonCompileRoot(self):
        return '{}/{}/{}.{}'.format(self._root, Lynxi_Folder_Compile, Lynxi_Folder_Python, self._version)

    @property
    def pythonVersionInfoFile(self):
        return '{}/{}/{}.info.json'.format(self._root, Lynxi_Folder_Source, self._version)

    @property
    def iconRoot(self):
        return '{}/{}/{}.{}'.format(self._root, Lynxi_Folder_Source, Lynxi_Folder_Icon, self._version)

    def __str__(self):
        return self._root


class BasicPath(object):
    def __init__(self, version=None):
        if version is not None:
            self._version = version
        else:
            self._version = Version().active()

        self._root = _getLxBasicPath()

    @property
    def root(self):
        return self._root

    @property
    def pythonRoot(self):
        if isLxDevelop():
            return DevelopPath().pythonSourceRoot
        else:
            return ProductPath(self._version).pythonCompileRoot

    @property
    def iconRoot(self):
        if isLxDevelop():
            return DevelopPath().iconRoot
        else:
            return ProductPath(self._version).iconRoot

    def __repr__(self):
        return self._root


class Version(object):
    def __init__(self):
        self._active = 1.0

        self._developFile = '{}/.info/python.version'.format(_getLxDevelopPath())
        self._productFile = '{}/.info/python.version'.format(_getLxProductPath())

        self._basicFile = '{}/.info/python.version'.format(_getLxBasicPath())

        self._load()

    def _load(self):
        if lxBasic.isOsExistsFile(self._basicFile):
            self._active = lxBasic.readOsJsonDic(self._basicFile, Lynxi_Key_Info_Active) or 1.0
        else:
            self._active = 1.0

    def _upload(self, version):
        lxBasic.writeOsJson(
            {
                Lynxi_Key_Info_Active: version,

                Lynxi_Key_Info_User: lxBasic.getOsUser(),
                Lynxi_Key_Info_Timestamp: lxBasic.getOsActiveTimestamp()
            },
            self._developFile
        )

        lxBasic.setOsFileCopy(self._developFile, self._productFile)

    def active(self):
        return self._active
