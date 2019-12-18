# coding:utf-8
from LxCore import lxBasic
env = lxBasic.Environ()

LynxiPipelineTds = [
    'dongchangbao',
    'changbao.dong'
]

LynxiPipelineTdPost = 'Pipeline - TD'
LynxiPipelineTdLevel = 3
pipelineTdBasicPaths = [
    'E:/myworkspace/td/lynxi'
]
# Environ Key
Lynxi_Key_Environ_Project = 'LYNXI_PROJECT'

LynxiUi_Value_TooltipDelayTime = 1000

Folder_Basic = '.lynxi'
Lynxi_App_Maya = 'maya'
LynxiPresetKey = 'preset'
LynxiPipelinePresetKey = 'pipeline'
LynxiVariantPresetKey = 'variant'
LynxiPersonnelPresetKey = 'personnel'
LynxiSoftwarePresetKey = 'software'
LynxiMayaPresetKey = 'maya'
Lynxi_Key_Preset_Project = 'project'
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
Lynxi_Key_Plug_PresetKey = 'plug'
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

Key_Plug_Name = 'plugName'
Key_Plug_Version = 'plugVersion'
Lynxi_Key_Plug_Versions = 'plugVersions'
Lynxi_Key_Plug_Load_Names = 'plugLoadNames'
Lynxi_Key_Plug_Load_Enable_Auto = 'autoLoad'
Lynxi_Key_Plug_Setup_Command = 'plugSetupCommand'
Lynxi_Key_Plug_Path = 'plugPath'
Lynxi_Key_Plug_Path_Deploy = 'plugDeployPath'
Lynxi_Key_Plug_Path_Module = 'plugModulePath'
Lynxi_Key_Plug_Path_Rlm = 'plugRlmPath'

LynxiVariantKey = 'key'
LynxiVariantValue = 'value'
LynxiUiNameKey = 'nameText'
LynxiUiTipKey = 'uiTip'
LynxiServerPathKey = 'serverDirectory'
LynxiUtilitiesPathKey = 'utilitiesPath'
LynxiLocalPathKey = 'localDirectory'
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
Lynxi_Mode_Develop_Enable_Product = False

Lynxi_Mode_Plug_Enable_Local = True
Lynxi_Mode_Plug_Enable_Module = True
Lynxi_Mode_Plug_Enable_Environ = True

Lynxi_Mode_Package_Enable_Local = True
varDic = globals()


def isLxPipelineTd():
    boolean = False
    user = lxBasic.getOsUser()
    if user in LynxiPipelineTds:
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


class Basic(object):
    Category_Windows_Bin = 'windows_bin'
    Category_Windows_Python_Scheme = 'windows_python_scheme'
    Category_Windows_App_Python_Scheme = 'windows_app_python_scheme'
    Category_Windows_Python_Module = 'windows_python_module'
    Category_Windows_App_Python_Module = 'windows_app_python_module'
    Category_Windows_Python_Package = 'windows_python_package'
    Category_Windows_App_Python_Package = 'windows_app_python_package'
    Category_Windows_App_Plug = 'windows_app_plug'

    Root_Develop_Default = 'e:/myworkspace/td/lynxi'

    Path_Local_Default = 'c:/.lynxi'

    Key_Environ_Python_Version = 'LYNXI_PYTHON_VERSION'

    Key_Environ_Enable_Develop = 'LYNXI_DEVELOP'

    Key_Environ_Path_Develop = 'LYNXI_DEVELOP_PATH'
    Key_Environ_Path_Preset = 'LYNXI_PRESET_PATH'

    Key_Environ_Path_User = 'LYNXI_USER_PATH'

    Key_Environ_Path_Module = 'LYNXI_MODULE_PATH'
    Key_Environ_Path_Toolkit = 'LYNXI_TOOLKIT_PATH'

    Folder_Log = '.log'
    Folder_Tool = 'tool'
    Folder_Icon = 'icon'
    Folder_Product = 'product'
    Folder_Module = 'module'
    Folder_Resource = 'resource'
    Folder_Develop = 'develop'
    Folder_Version = 'version'
    Folder_Source = 'source'
    Folder_Compile = 'compile'
    Folder_Workspace = 'workspace'
    Folder_Plug = 'plug'

    Folder_Maya = 'maya'
    Folder_Windows = 'windows'
    Folder_Python = 'python'
    Folder_Package = 'package'
    Folder_Qt = 'qt'
    Folder_Bin = 'exe'

    Folder_User = 'user'

    Folder_Share = 'share'
    Folder_Definition = 'definition'

    Key_User = 'user'
    Key_Timestamp = 'timestamp'

    Ext_Json = '.json'

    Key_Enable = 'enable'
    Key_Category = 'category'
    Key_Name = 'name'

    Key_Version = 'version'
    Key_Record = 'record'
    Key_Active = 'active'

    Key_Application = 'application'
    Key_Bin = 'bin'
    Key_Platform = 'platform'

    Key_App = 'app'

    Key_Python_Version = 'python_version'

    Key_Resource = 'resource'
    Key_Argument = 'argument'

    Key_Config = 'config'

    Key_Dependent = 'dependent'
    Key_Dependent_Module = 'dependent_module'
    Key_Dependent_Package = 'dependent_package'

    Key_Language = 'language'
    Key_Language_Name = 'language_name'
    Key_Language_Version = 'language_version'

    Key_Package = 'package'
    Key_Module = 'module'

    Key_Python_Package = 'python_package'
    Key_Python_Module = 'python_module'

    Key_Resource_Source_Path = 'sourcepath'
    Key_Resource_Compile_Path = 'compilepath'

    Key_Plug_Name = 'plugname'
    Key_Plug_Version = 'plugversion'
    Key_Plug_App = 'plugapp'
    Key_Plug_Source_Path = 'plugpath'

    Key_Plug_Load_Name = 'loadname'
    Key_Plug_Module_Name = 'modulename'

    Language_Python = 'python'
    Language_Share = 'share'

    Version_Default = '0.0.0'
    Version_Active = 'active'

    Bin_Share = 'share'
    App_Maya = 'maya'
    Version_Share = 'share'

    Platform_Windows = 'windows'

    Python_Version_27 = '2.7.x'

    Python_Package_Pyqt5 = 'PyQt5'
    Python_Package_Yaml = 'yaml'
    Python_Package_Chardet = 'chardet'
    Python_Package_Materialx = 'MaterialX'
    Python_Package_Pil = 'PIL'
    Python_Package_Dingtalkchatbot = 'dingtalkchatbot'

    Python_Module_Core = 'LxCore'
    Python_Module_Command = 'LxCommand'
    Python_Module_Database = 'LxDatabase'
    Python_Module_Ui = 'LxUi'
    Python_Module_Interface = 'LxInterface'

    Python_Module_Maya = 'LxMaya'
    Python_Module_Deadline = 'LxDeadline'

    Python_Module_Graph = 'LxGraph'
    Python_Module_Material = 'LxMaterial'

    App_Plug_Lynxinode = 'lynxinode'

    Environ_Key_Path = 'PATH'
    Environ_Key_Maya_Python_Path = 'PYTHONPATH'
    Environ_Key_Maya_Icon_Path = 'XBMLANGPATH'
    Environ_Key_Maya_Plug_Path = 'MAYA_PLUG_IN_PATH'
    Environ_Key_Maya_Script_Path = 'MAYA_SCRIPT_PATH'

    Key_Value = 'value'
    Key_Operate = 'operate'
    Key_Environ = 'environ'
    Key_Environ_Key = 'environ_key'
    Key_Environ_Value = 'environ_value'
    Key_Environ_Operate = 'environ_operation'

    Key_Path_Source = 'path_source'
    Key_Path_Compile = 'path_compile'
    Key_Path_Workspace = 'path_workspace'

    Operation_Add = '+='
    Operation_Replace = '='

    Attr_Key_Self = 'self'
    Attr_Key_Root = 'root'
    Attr_Key_Path = 'path'

    Attr_Key_Active = 'active'
    Attr_Key_Server = 'server'
    Attr_Key_Local = 'local'
    Attr_Key_Develop = 'develop'
    Attr_Key_Product = 'product'

    Attr_Path_Root = 'root'
    Attr_Path_Server_Root = 'serverroot'
    Attr_Path_Local_Root = 'localroot'
    Attr_Path_Develop_Root = 'developroot'
    Attr_Path_Product_Root = 'productroot'

    Attr_Path = 'path'
    Attr_Path_Source = 'sourcepath'

    Key_Path_SubPath = 'subpath'
    Key_Path_SubName = 'subname'
    Key_Path_Base_Name = 'basename'

    _String_Indent = '    '

    @staticmethod
    def _toSubPathMethod(*args):
        if args:
            sep = '/'
            if len(args) > 1:
                if isinstance(args[0], list) or isinstance(args[0], tuple):
                    return sep.join(list(args[0]))
                return sep.join(list(args))
            return args[0]

    @staticmethod
    def _toSubNameMethod(*args):
        if args:
            sep = '-'
            if len(args) > 1:
                if isinstance(args[0], list) or isinstance(args[0], tuple):
                    return sep.join(list(args[0]))
                return sep.join(list(args))
            return args[0]

    @staticmethod
    def _createTimestampMethod(osPath, osJsonFile):
        dic = {}

        isAscii = False
        if lxBasic.isOsExist(osJsonFile) is False:
            osFiles = lxBasic.getOsFiles(osPath)
            if osFiles:
                for osFile in osFiles:
                    osFileTimestamp = str(lxBasic.getOsFileMtimestamp(osFile))
                    relativeOsFile = osFile[len(osPath):]

                    if isinstance(relativeOsFile, unicode):
                        isAscii = True

                    dic[relativeOsFile] = osFileTimestamp

        lxBasic.writeOsJson(dic, osJsonFile, ensure_ascii=isAscii)

    @staticmethod
    def _getChangedFileMethod(sourceTimestamp, targetTimestamp):
        lis = []

        for localOsFile, sourceTime in sourceTimestamp.items():
            if targetTimestamp.__contains__(localOsFile):
                targetTime = targetTimestamp[localOsFile]
                if sourceTime != targetTime:
                    lis.append(localOsFile)
            #
            else:
                lis.append(localOsFile)

        return lis

    @classmethod
    def isDevelop(cls):
        boolean = False
        envData = lxBasic.getOsEnvironValue(cls.Key_Environ_Enable_Develop)
        if envData:
            if envData.lower() == 'true':
                boolean = True
        return boolean

    def _strDatum(self):
        return {}

    @classmethod
    def _toStringMethod(cls, datum, indent=4):
        def addNone(lString, rString):
            lis.append(u'{}null{}'.format(lString, rString))

        def addString(raw, lString, rString):
            lis.append(u'{}"{}"{}'.format(lString, raw, rString))

        def addUnicode(raw, lString, rString):
            lis.append(u'{}"{}"{}'.format(lString, raw, rString))

        def addNumber(raw, lString, rString):
            lis.append(u'{}{}{}'.format(lString, raw, rString))

        def addBoolean(raw, lString, rString):
            lis.append(u'{}{}{}'.format(lString, str(raw).lower(), rString))

        def addMember(raw, lString, rString):
            if isinstance(raw, bool):
                addBoolean(raw, lString, rString)

            elif isinstance(raw, int) or isinstance(raw, float):
                addNumber(raw, lString, rString)

            elif isinstance(raw, str):
                addString(raw, lString, rString)

            elif isinstance(raw, unicode):
                addUnicode(raw, lString, rString)

        def addValue(raw, lString, rString, rawType=dict):
            if raw is None:
                addNone(lString=lString, rString='\r\n')

            elif isinstance(raw, list) or isinstance(raw, tuple):
                lString += defIndentString
                addList(raw, lString=lString, rString=rString)

            elif isinstance(raw, dict):
                lString += defIndentString
                addDictionary(raw, lString=lString, rString=rString)

            else:
                if rawType == dict:
                    addMember(raw, lString='', rString=rString)
                else:
                    addMember(raw, lString=lString+defIndentString, rString=rString)

        def addList(raw, lString, rString):
            if raw:
                lis.append(u'{lString}[{rString}'.format(lString='', rString='\r\n'))

                c = len(raw)
                for seq, i in enumerate(raw):
                    if seq < c - 1:
                        addValue(i, lString=lString, rString=',\r\n', rawType=list)
                    else:
                        addValue(i, lString=lString, rString='\r\n', rawType=list)

                lis.append(u'{lString}]{rString}'.format(lString=lString, rString=rString))

            else:
                lis.append(u'{lString}[]{rString}\r\n'.format(lString=lString, rString=rString))

        def addDictionary(raw, lString, rString):
            if raw:
                lis.append(u'{lString}{{{rString}'.format(lString='', rString='\r\n'))

                c = len(raw)
                for seq, (k, v) in enumerate(raw.items()):
                    addMember(k, lString=lString + defIndentString, rString=': ')

                    if seq < c - 1:
                        addValue(v, lString=lString, rString=',\r\n', rawType=dict)
                    else:
                        addValue(v, lString=lString, rString='\r\n', rawType=dict)

                lis.append(u'{lString}}}{rString}'.format(lString=lString, rString=rString))

            else:
                lis.append(u'{lString}{{}}{rString}'.format(lString='', rString=rString))

        def addRaw(raw):
            if raw is None:
                addNone(lString='', rString='\r\n')

            elif isinstance(raw, list) or isinstance(raw, tuple):
                addList(raw, lString='', rString='\r\n')

            elif isinstance(raw, dict):
                addDictionary(raw, lString='', rString='\r\n')

        defIndentString = ' ' * indent
        lis = [
            u'{} = '.format(cls.__name__)
        ]

        addRaw(datum)

        return ''.join(lis)

    def __str__(self):
        if self._strDatum():
            return self._toStringMethod(self._strDatum())
        return ''


class Message(object):
    Lynxi_Message_Enable = True
    def __init__(self):
        pass

    @classmethod
    def setEnable(cls, boolean):
        cls.Lynxi_Message_Enable = boolean

    @classmethod
    def isEnable(cls):
        return cls.Lynxi_Message_Enable

    def trace(self, text):
        if self.isEnable() is True:
            print u'# Lynxi {}'.format(lxBasic.getOsActiveViewTime())
            print u'    {}'.format(text)

    def traceResult(self, text):
        self.trace(
            u'''# Result {}'''.format(text)
        )

    def traceWarning(self, text):
        self.trace(
            u'''# Warning {}'''.format(text)
        )

    def traceError(self, text):
        self.trace(
            u'''# Error {}'''.format(text)
        )


class _AbcRoot(Basic):
    def _initAbcRoot(self):
        pass

    @property
    def active(self):
        return self._activeDirectory()

    def _activeDirectory(self):
        pass

    @property
    def server(self):
        return self._serverDirectory()

    @classmethod
    def _serverDirectory(cls):
        pass

    @property
    def local(self):
        return self._localDirectory()

    @classmethod
    def _localDirectory(cls):
        pass

    @property
    def develop(self):
        return self._developDirectory()

    @classmethod
    def _developDirectory(cls):
        pass

    @property
    def product(self):
        return self._productDirectory()

    @classmethod
    def _productDirectory(cls):
        pass

    def _strDatum(self):
        return lxBasic.orderedDict(
            [
                (self.Attr_Key_Active, self.server),
                (self.Attr_Key_Server, self.server),
                (self.Attr_Key_Local, self.local),
                (self.Attr_Key_Develop, self.develop),
                (self.Attr_Key_Product, self.product)
            ]
        )


class Root(_AbcRoot):
    def __init__(self):
        self._initAbcRoot()

    def _activeDirectory(self):
        return self._serverDirectory()

    @classmethod
    def _serverDirectory(cls):
        if cls.isDevelop():
            return cls._developDirectory()
        return cls._productDirectory()

    @classmethod
    def _localDirectory(cls):
        return cls.Path_Local_Default

    @classmethod
    def _developDirectory(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Develop)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default

    @classmethod
    def _productDirectory(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Module)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default


class ToolkitRoot(_AbcRoot):
    def __init__(self):
        self._initAbcRoot()

    def _activeDirectory(self):
        return self._serverDirectory()

    @classmethod
    def _serverDirectory(cls):
        if cls.isDevelop():
            return cls._developDirectory()
        return cls._productDirectory()

    @classmethod
    def _localDirectory(cls):
        return cls.Path_Local_Default

    @classmethod
    def _developDirectory(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Develop)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default

    @classmethod
    def _productDirectory(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Toolkit)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default


class _AbcPath(Basic):
    ROOT_CLS = None

    def _initAbcPath(self, *args):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.root.active}/{self.subpath}',
            self.Attr_Key_Server: u'{self.root.server}/{self.subpath}',
            self.Attr_Key_Local: u'{self.root.local}/{self.subpath}',
            self.Attr_Key_Develop: u'{self.root.develop}/{self.subpath}',
            self.Attr_Key_Product: u'{self.root.product}/{self.subpath}'
        }

        self._root = self.ROOT_CLS()

        self._subPathString = self._toSubPathMethod(*args)
        self._subNameString = self._toSubNameMethod(*args)

        if args:
            self._baseName = args[-1]

    @property
    def root(self):
        return self._root

    def subPath(self):
        return self._subPathString

    @property
    def subpath(self):
        return self.subPath()

    def subName(self):
        return self._subNameString

    @property
    def subname(self):
        return self.subName()

    def baseName(self):
        return self._baseName

    @property
    def basename(self):
        return self.baseName()

    def _activeDirectory(self):
        return self._formatStringDic[self.Attr_Key_Active].format(**self._formatDict())

    @property
    def active(self):
        return self._activeDirectory()

    def _serverDirectory(self):
        return self._formatStringDic[self.Attr_Key_Server].format(**self._formatDict())

    @property
    def server(self):
        return self._serverDirectory()

    def _localDirectory(self):
        return self._formatStringDic[self.Attr_Key_Local].format(**self._formatDict())

    @property
    def local(self):
        return self._localDirectory()

    def _developDirectory(self):
        return self._formatStringDic[self.Attr_Key_Develop].format(**self._formatDict())

    @property
    def develop(self):
        return self._developDirectory()

    def _productDirectory(self):
        return self._formatStringDic[self.Attr_Key_Product].format(**self._formatDict())

    @property
    def product(self):
        return self._productDirectory()

    def _formatDict(self):
        return {
            self.Attr_Key_Self: self,
        }

    def _strDatum(self):
        return lxBasic.orderedDict(
            [
                (self.Attr_Key_Active, self.server),
                (self.Attr_Key_Server, self.server),
                (self.Attr_Key_Local, self.local),
                (self.Attr_Key_Develop, self.develop),
                (self.Attr_Key_Product, self.product)
            ]
        )


class BinSubRoot(_AbcPath):
    ROOT_CLS = Root

    def __init__(self):
        self._initAbcPath(self.Folder_Bin)


class PythonModuleBranch(_AbcPath):
    ROOT_CLS = Root

    def __init__(self, *args):
        self._initAbcPath(self.Folder_Python, *args)

    def _overrideFormatString(self):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.root.active}/resource/module',
            self.Attr_Key_Server: u'{self.root.server}/resource/module',
            self.Attr_Key_Local: u'{self.root.local}/resource/module',
            self.Attr_Key_Develop: u'{self.root.develop}/resource/module',
            self.Attr_Key_Product: u'{self.root.product}/resource/module'
        }


class WorkspaceModuleRoot(_AbcPath):
    ROOT_CLS = Root

    def __init__(self):
        self._initAbcPath(self.Folder_Workspace)

        self._overrideFormatString()

    def _overrideFormatString(self):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.root.active}/workspace/module',
            self.Attr_Key_Server: u'{self.root.server}/workspace/module',
            self.Attr_Key_Local: u'{self.root.local}/workspace/module',
            self.Attr_Key_Develop: u'{self.root.develop}/workspace/module',
            self.Attr_Key_Product: u'{self.root.product}/workspace/module'
        }


class WorkspaceModulePath(_AbcPath):
    ROOT_CLS = WorkspaceModuleRoot

    def __init__(self, *args):
        self._initAbcPath(*args)


class IconSubRoot(_AbcPath):
    ROOT_CLS = Root

    def __init__(self):
        self._initAbcPath(self.Folder_Icon)


class UserSubRoot(_AbcPath):
    ROOT_CLS = Root

    def __init__(self):
        self._initAbcPath(self.Folder_User)


class UserBranch(_AbcPath):
    ROOT_CLS = UserSubRoot

    def __init__(self, *args):
        self._initAbcPath(*args)


class UserPreset(Basic):
    Folder_Preset = 'preset'

    Folder_Render = 'render'
    Folder_Project = 'project'
    Folder_Ui = 'ui'
    Folder_Filter = 'filter'
    def __init__(self):
        self._root = UserBranch(lxBasic.getOsUser())

    def _activeDirectory(self):
        return self._root._localDirectory()

    def uiDirectory(self):
        return u'{}/{}'.format(self._activeDirectory(), self.Folder_Ui)

    def renderDirectory(self):
        return u'{}/{}'.format(self._activeDirectory(), self.Folder_Render)

    def projectConfigFile(self):
        return u'{}/{}{}'.format(self._activeDirectory(), self.Folder_Project, self.Ext_Json)

    def appProjectFile(self, appName, appVersion):
        return u'{}/{}/{}.{}{}'.format(self._activeDirectory(), self.Folder_Project, appName, appVersion, self.Ext_Json)

    def uiFilterHistoryFile(self):
        return u'{}/{}.history{}'.format(self.uiDirectory(), self.Folder_Filter, self.Ext_Json)


class LogSubRoot(_AbcPath):
    ROOT_CLS = Root

    def __init__(self):
        self._initAbcPath(self.Folder_Log)


class _AbcFile(Basic):
    PATH_CLS = None
    PATH_WORKSPACE_CLS = None

    FILE_CLS = None

    def _initAbcFile(self, pathArgs, fileBasename, ext):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.path.active}/{self.basename}',
            self.Attr_Key_Server: u'{self.path.server}/{self.basename}',
            self.Attr_Key_Local: u'{self.path.local}/{self.basename}',
            self.Attr_Key_Develop: u'{self.path.develop}/{self.basename}',
            self.Attr_Key_Product: u'{self.path.product}/{self.basename}'
        }

        self._raw = {}

        self._path = self.PATH_CLS(*pathArgs)
        self._workspacePath = self.PATH_WORKSPACE_CLS(*pathArgs)

        self._baseName = u'{}{}'.format(fileBasename, ext)

    @property
    def root(self):
        return self._path.root

    @property
    def path(self):
        return self._path

    @property
    def workspacepath(self):
        return self._workspacePath

    def _activeDirectory(self):
        return self._path._activeDirectory()

    def _serverDirectory(self):
        return self._path._serverDirectory()

    def _localDirectory(self):
        return self._path._localDirectory()

    def _developDirectory(self):
        return self._path._developDirectory()

    def _productDirectory(self):
        return self._path._productDirectory()

    def _workspaceDirectory(self):
        return self._workspacePath._developDirectory()

    def subPath(self):
        return self._path.subPath()

    def subName(self):
        return self._path.subName()

    def baseName(self):
        return self._baseName

    @property
    def basename(self):
        return self.baseName()

    def file(self):
        return self._formatStringDic[self.Attr_Key_Active].format(**self._formatDict())

    def hasFile(self):
        return lxBasic.isOsExist(self.file())

    def raw(self):
        return self._raw

    def cacheRaw(self):
        if self.hasFile():
            return self.FILE_CLS(self.file()).read()
        return {}

    def severFile(self):
        return self._formatStringDic[self.Attr_Key_Server].format(**self._formatDict())

    def hasServerFile(self):
        return lxBasic.isOsExist(self.severFile())

    def localFile(self):
        return self._formatStringDic[self.Attr_Key_Local].format(**self._formatDict())

    def hasLocalFile(self):
        return lxBasic.isOsExist(self.localFile())

    def developFile(self):
        return self._formatStringDic[self.Attr_Key_Develop].format(**self._formatDict())

    def hasDevelopFile(self):
        return lxBasic.isOsExist(self.developFile())

    def productFile(self):
        return self._formatStringDic[self.Attr_Key_Product].format(**self._formatDict())

    def hasProductFile(self):
        return lxBasic.isOsExist(self.productFile())

    def _formatDict(self):
        return {
            self.Attr_Key_Self: self,
        }


class _AbcConfigFile(_AbcFile):
    FILE_CLS = lxBasic.JsonFile

    def _initAbcConfigFile(self, *args):
        self._initAbcFile(args, 'config', '.json')

        self._overrideFormatString()

    def _overrideFormatString(self):
        formatDict = {
            self.Attr_Key_Active: u'{self.root.active}/{self.subname}',
            self.Attr_Key_Server: u'{self.root.server}/{self.subname}',
            self.Attr_Key_Local: u'{self.root.local}/{self.subname}',
            self.Attr_Key_Develop: u'{self.root.develop}/{self.subname}',
            self.Attr_Key_Product: u'{self.root.product}/{self.subname}'
        }
        self.path._formatStringDic = formatDict
        self.workspacepath._formatStringDic = formatDict


class _AbcSchemeFile(_AbcFile):
    FILE_CLS = lxBasic.JsonFile
    PATH_WORKSPACE_CLS = WorkspaceModulePath

    def _initAbcSchemeFile(self, schemeName):
        self._initAbcFile((), '{}.scheme'.format(schemeName), '.json')


class Log(Basic):
    def __init__(self):
        self._subRoot = LogSubRoot()

    def exceptionFile(self):
        return u'{}/{}.exception.log'.format(
            self._subRoot._serverDirectory(), lxBasic.getOsActiveDateTag()
        )

    def errorFile(self):
        return u'{}/{}.error.log'.format(
            self._subRoot._serverDirectory(), lxBasic.getOsActiveDateTag()
        )

    def developFile(self):
        return u'{}/{}.develop.log'.format(
            self._subRoot._serverDirectory(), lxBasic.getOsActiveDateTag()
        )

    def addException(self, text):
        self.add(
            text,
            self.exceptionFile()
        )

    def addError(self, text):
        self.add(
            text,
            self.errorFile()
        )

    def addDevelop(self, text):
        self.add(
            text,
            self.developFile()
        )

    @staticmethod
    def add(text, osLogFile):
        lxBasic.setOsFilePathCreate(osLogFile)
        with open(osLogFile, 'a') as log:
            log.writelines(u'{} @ {}\n'.format(lxBasic.getOsActiveViewTime(), lxBasic.getOsUser()))
            log.writelines(u'{}\n'.format(text))
            log.close()


class ToolkitSubRoot(_AbcPath):
    ROOT_CLS = ToolkitRoot
    def __init__(self):
        self._initAbcPath(self.Folder_Tool)


class Lynxi_Scheme_Python(_AbcSchemeFile):
    PATH_CLS = PythonModuleBranch

    Python_Module_Core = 'LxCore'
    Python_Module_Command = 'LxCommand'
    Python_Module_Database = 'LxDatabase'
    Python_Module_Ui = 'LxUi'
    Python_Module_Interface = 'LxInterface'

    Python_Module_Maya = 'LxMaya'
    Python_Module_Deadline = 'LxDeadline'

    Python_Module_Graph = 'LxGraph'
    Python_Module_Material = 'LxMaterial'

    Lynxi_Python_Module_Basic_Lis = [
        'LxCore.config.appConfig',
        'LxCore.method.basic._methodBasic',
        'LxCore.method._osMethod',
        'LxCore.method._dbMethod',
        'LxCore.method._uiMethod',
        'LxCore.method._productMethod',
        #
        'LxCore.lxBasic',
        'LxCore.lxConfigure',
        'LxCore.definition.abstract',
        'LxCore.definition.path',
        'LxCore.definition.raw',
        'LxCore.definition.bin',
        'LxCore.definition.resource',
        'LxCore.definition.preset',
        # Ui
        'LxUi.uiConfigure',
        'LxUi.command.uiHtml',
        'LxUi.qt.qtCore',
        'LxUi.qt.qtDefinition',
        'LxUi.qt.qtAbstract',
        'LxUi.qt.qtAction',
        'LxUi.qt.qtBasic.qtModelBasic',
        'LxUi.qt.qtBasic.qtWidgetBasic',
        'LxUi.qt.qtWidgets.qtWindow',
        'LxUi.qt.qtWidgets.qtView',
        'LxUi.qt.qtWidgets.qtGroup',
        'LxUi.qt.qtWidgets.qtItem',
        'LxUi.qt.qtWidgets',
        'LxUi.qt.qtWidgets_',
        'LxUi.qt.qtChart_',
        'LxUi.qt.qtLog',
        'LxUi.qt.qtProgress',
        'LxUi.qt.qtTip',
        # Behind Ui
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

    Lynxi_Python_Module_Maya_Lis = [
        'LxMaya.method.config._maConfig',

        'LxMaya.method.basic._maMethodBasic',

        'LxMaya.method._maUiMethod',
        'LxMaya.method._maMethod',
        'LxMaya.method._maPlugMethod',
        'LxMaya.method._maProductMethod',
        'LxMaya.method',

    ]

    def __init__(self, schemeName='default'):
        self._initAbcSchemeFile(schemeName)

        self._defRaw = {
            self.Key_Python_Version: self.Python_Version_27,
            self.Key_Active: self.Version_Default,
            self.Key_Dependent: {
            },
            self.Key_Environ: {
            }
        }

    @classmethod
    def languageVersion(cls):
        return cls.Python_Version_27

    def _dependentDic(self):
        if self.hasFile():
            return self.raw().get(self.Key_Dependent, {})
        return {}

    def _pythonModuleDic(self):
        if self._dependentDic():
            return self._dependentDic().get(self.Key_Python_Module, {})
        return {}

    def _setModulesCreateWorkareaDirectory(self):
        pass

    def _setModulesAddDevelopWorkareaPath(self):
        pass

    def _addPythonPackagePath(self):
        pass

    def _addPythonModulePath(self):
        pass

    def createDefaultSchemeFile(self):
        pass

    def publishProduct(self):
        pass

    @classmethod
    def _getPythonModuleLisMethod(cls, osPath, moduleName):

        if cls.isDevelop():
            ext = '.py'
        else:
            ext = '.pyc'

        osFiles = lxBasic.getOsFiles(osPath)

        lis = []

        timestampLis = []
        moduleDic = {}

        if osFiles:
            for osFile in osFiles:
                if osFile.endswith(ext):
                    timestamp = lxBasic.getOsFileMtimestamp(osFile)
                    timestampLis.append(timestamp)

                    modulePath = moduleName + '.' + osFile[len(osPath) + 1:-len(ext)].replace('/', '.')
                    if modulePath.endswith('__init__'):
                        moduleDic[timestamp] = modulePath[:(-len('__init__') - 1)]
                    else:
                        moduleDic[timestamp] = modulePath

        if timestampLis:
            timestampLis.sort()
            timestampLis.reverse()
            for i in timestampLis:
                if i in moduleDic:
                    module = moduleDic[i]
                    lis.append(module)

        return lis

    @staticmethod
    def _pythonModuleReloadMethod(modulePaths):
        if modulePaths:
            from LxUi.qt import qtProgress  # import in Method
            # View Progress
            progressExplain = '''Update Python Module(s)'''
            maxValue = len(modulePaths)
            progressBar = qtProgress.viewSubProgress(progressExplain, maxValue)
            for i in modulePaths:
                modulePath = '.'.join(i.split('.')[:-1])
                moduleName = i.split('.')[-1]

                progressBar.updateProgress(moduleName)

                if modulePath:
                    command = '''from {0} import {1};reload({1})'''.format(modulePath, moduleName)
                else:
                    command = '''import {0};reload({0})'''.format(moduleName)

                exec command

    @classmethod
    def reloadBasic(cls):
        moduleLis = cls.Lynxi_Python_Module_Basic_Lis
        if lxBasic.isMayaApp():
            moduleLis += cls.Lynxi_Python_Module_Maya_Lis

        cls._pythonModuleReloadMethod(moduleLis)

    def reloadAll(self):
        import pkgutil

        moduleLis = [
            self.Python_Module_Core,
            self.Python_Module_Database,
            self.Python_Module_Ui,
            self.Python_Module_Interface,
            self.Python_Module_Maya,
            self.Python_Module_Deadline
        ]
        for i in moduleLis:
            loader = pkgutil.find_loader(i)
            if loader:
                osPath = loader.filename.replace('\\', '/')
                self._pythonModuleReloadMethod(self._getPythonModuleLisMethod(osPath, i))

    def serverVersion(self):
        if lxBasic.isOsExistsFile(self.file()):
            return lxBasic.readOsJsonDic(self.file(), Lynxi_Key_Info_Active) or self.Version_Default
        return self.Version_Default

    def localVersion(self):
        data = lxBasic.getOsEnvironValue(self.Key_Environ_Python_Version)
        if data is not None:
            return data
        return self.Version_Default

    def setLocalRefresh(self):
        serverVersion = self.serverVersion()
        lxBasic.setOsEnvironValue(self.Key_Environ_Python_Version, serverVersion)
        Message().traceResult(
            u'Set Version : {}'.format(serverVersion)
        )


class Lynxi_Icon(_AbcConfigFile):
    pass


class Ui(Basic):
    Lynxi_Key_Environ_Message_Count = 'LYNXI_MESSAGE_COUNT'
    Lynxi_Key_Environ_Enable_Tooltip_Auto = 'LYNXI_TOOLTIP_AUTO_SHOW'
    def __init__(self):
        pass

    @classmethod
    def restMessageCount(cls):
        lxBasic.setOsEnvironValue(cls.Lynxi_Key_Environ_Message_Count, '0')

    @classmethod
    def setMessageCount(cls, value):
        data = lxBasic.getOsEnvironValue(cls.Lynxi_Key_Environ_Message_Count)
        #
        if data:
            value_ = str(int(data) + value)
        else:
            value_ = str(0)
        #
        lxBasic.setOsEnvironValue(cls.Lynxi_Key_Environ_Message_Count, value_)
        return int(value_)

    @staticmethod
    def closeAll():
        from LxUi.qt import qtCore  # import in Method
        reload(qtCore)
        #
        w = qtCore.getAppWindow()
        if w is not None:
            cs = w.children()
            if cs:
                for i in cs:
                    moduleName = i.__class__.__module__
                    if moduleName.startswith('LxInterface.qt') or moduleName.startswith('LxUi.qt'):
                        i.deleteLater()

    @classmethod
    def setTooltipAutoShow(cls, boolean):
        envValue = str(boolean).upper()
        lxBasic.setOsEnvironValue(cls.Lynxi_Key_Environ_Enable_Tooltip_Auto, envValue)

    @classmethod
    def isTooltipAutoShow(cls):
        boolean = False
        envData = lxBasic.getOsEnvironValue(cls.Lynxi_Key_Environ_Enable_Tooltip_Auto)
        if envData:
            if envData == str(True).upper():
                boolean = True
        return boolean


class Product(Basic):
    def __init__(self):
        pass
