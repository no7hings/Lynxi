# coding:utf-8
import os

import sys

import platform

from LxBasic import bscObjects

from LxCore import lxBasic

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
LynxiAppNameKey = 'applicationName'
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


class System(object):
    platform_dic = {
        'Windows': 'windows',
        'Linux': 'linux'
    }
    application_dic = {
        'maya.exe': 'maya',
        'maya': 'maya'
    }

    def __init__(self, argv=None):
        if argv is None:
            argv = sys.argv
        self._argv = argv

    @property
    def platform(self):
        return self.platform_dic.get(platform.system())

    @property
    def application(self):
        return self.application_dic.get(os.path.basename(self._argv[0]))

    def isWindows(self):
        return self.platform == 'windows'

    def isMaya(self):
        return self.application == 'maya'


class Basic(object):
    Category_Platform = 'platform'

    Category_Plf_Language = 'plf-language'
    Category_Plf_Application = 'plf-application'
    Category_Plf_App_Language = 'plf-app-language'

    Category_Plf_Lan_Package = 'plf-lan-package'
    Category_Plf_App_Lan_Package = 'plf-app-lan-package'
    Category_Plf_App_Package = 'plf-app-package'

    Category_Plf_Lan_Plug = 'plf-lan-plug'
    Category_Plf_App_Lan_Plug = 'plf-app-lan-plug'
    Category_Plf_App_Plug = 'plf-app-plug'

    Category_Plf_Lan_Module = 'plf-lan-module'
    Category_Plf_App_Lan_Module = 'plf-app-lan-module'
    Category_Plf_App_Module = 'plf-app-module'

    Category_Plf_Lan_Scheme = 'plf-lan-scheme'
    Category_Plf_App_Lan_Scheme = 'plf-app-lan-scheme'
    Category_Plf_App_Scheme = 'plf-app-scheme'

    Category_Scheme_Lis = [
        Category_Plf_Lan_Scheme, Category_Plf_App_Lan_Scheme
    ]
    Category_Package_Lis = [
        Category_Plf_Lan_Package, Category_Plf_App_Lan_Package, Category_Plf_App_Package
    ]
    Category_Bin_Lis = [
        Category_Plf_Language, Category_Plf_Application, Category_Plf_App_Language
    ]
    Category_Module_Lis = [
        Category_Plf_Lan_Module, Category_Plf_App_Lan_Module, Category_Plf_App_Module
    ]

    Root_Develop_Default = 'e:/myworkspace/td/lynxi'
    Root_Product_Default = 'e:/myworkspace/td/lynxi'
    Path_Local_Default = 'c:/.lynxi'

    Keyword_Share = 'share'

    Key_Environ_Scheme_Name = 'LYNXI_SCHEME_NAME'
    Key_Environ_Scheme_Version = 'LYNXI_SCHEME_VERSION'
    Key_Environ_Scheme_System = 'LYNXI_SCHEME_SYSTEM'

    Key_Environ_Enable_Develop = 'LYNXI_DEVELOP'
    Key_Environ_Path_Product = 'LYNXI_PATH'

    Key_Environ_Path_Develop = 'LYNXI_DEVELOP_PATH'
    Key_Environ_Path_Local = 'LYNXI_LOCAL_PATH'

    Key_Environ_Path_Preset = 'LYNXI_PRESET_PATH'
    Key_Environ_Path_Toolkit = 'LYNXI_TOOLKIT_PATH'

    Key_Environ_Python_Bin_Path = 'LYNXI_BIN_PYTHON_PATH'

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

    Key_System = 'system'
    Key_Version = 'version'
    Key_Record = 'record'
    Key_Active = 'active'
    Key_Develop = 'develop'

    Key_Application = 'application'
    Key_Bin = 'bin'
    Key_Platform = 'platform'

    Key_App = 'app'

    Key_Python_Version = 'python_version'

    Key_Resource = 'resource'

    Key_Config = 'config'

    Key_Program = 'program'

    Key_Dependent = 'dependent'
    Key_Dependent_Module = 'dependent_module'
    Key_Dependent_Package = 'dependent_package'

    Key_Language = 'language'
    Key_Language_Name = 'language_name'
    Key_Language_Version = 'language_version'

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
    Keyword_Version_Active = 'active'
    Keyword_System_Active = 'active'

    Bin_Share = 'share'
    App_Maya = 'maya'
    Version_Share = 'share'

    Platform_Windows = 'windows'

    Python_Version_27 = '2.7.x'

    Environ_Key_Path = 'PATH'
    Environ_Key_Maya_Python_Path = 'PYTHONPATH'
    Environ_Key_Maya_Icon_Path = 'XBMLANGPATH'
    Environ_Key_Maya_Plug_Path = 'MAYA_PLUG_IN_PATH'
    Environ_Key_Maya_Script_Path = 'MAYA_SCRIPT_PATH'

    Key_Path = 'path'

    Key_Environ = 'environ'
    Key_Value = 'value'
    Key_Operate = 'operate'

    Operation_Add = '+='
    Operation_Replace = '='

    Attr_Key_Self = 'self'
    Attr_Key_Root = 'root'
    Attr_Key_Path = 'path'
    Attr_Key_System = 'system'

    Path_Key_Active = 'active'
    Path_Key_Server = 'server'
    Path_Key_Local = 'local'
    Path_Key_Develop = 'develop'
    Path_Key_Product = 'product'
    Path_Key_Workspace = 'workspace'

    Attr_Key_Path_Source = 'sourcepath'

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
        isAscii = False
        timestampDic = bscObjects.Pth_Directory(osPath).allChildFileTimestampDic()

        lxBasic.writeOsJson(timestampDic, osJsonFile, ensure_ascii=isAscii)

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

    def _strRaw(self):
        return {}

    @classmethod
    def _toJsonStringMethod(cls, raw, indent=4):
        def addNoneFnc_(lString, rString):
            lis.append(u'{}null{}'.format(lString, rString))

        def addStringFnc_(raw_, lString, rString):
            lis.append(u'{}"{}"{}'.format(lString, raw_, rString))

        def addUnicodeFnc_(raw_, lString, rString):
            lis.append(u'{}"{}"{}'.format(lString, raw_, rString))

        def addNumberFnc_(raw_, lString, rString):
            lis.append(u'{}{}{}'.format(lString, raw_, rString))

        def addBooleanFnc_(raw_, lString, rString):
            lis.append(u'{}{}{}'.format(lString, str(raw_).lower(), rString))

        def addMemberFnc_(raw_, lString, rString):
            if isinstance(raw_, bool):
                addBooleanFnc_(raw_, lString, rString)

            elif isinstance(raw_, int) or isinstance(raw_, float):
                addNumberFnc_(raw_, lString, rString)

            elif isinstance(raw_, str):
                addStringFnc_(raw_, lString, rString)

            elif isinstance(raw_, unicode):
                addUnicodeFnc_(raw_, lString, rString)

        def addValueFnc_(raw_, lString, rString, rawType=None):
            if raw_ is None:
                addNoneFnc_(lString=lString, rString='\r\n')

            elif isinstance(raw_, list) or isinstance(raw_, tuple):
                lString += defIndentString
                addListFnc_(raw_, lString=lString, rString=rString)

            elif isinstance(raw_, dict):
                lString += defIndentString
                addDictionaryFnc_(raw_, lString=lString, rString=rString)

            else:
                if rawType == dict:
                    addMemberFnc_(raw_, lString='', rString=rString)
                else:
                    addMemberFnc_(raw_, lString=lString+defIndentString, rString=rString)

        def addListFnc_(raw_, lString, rString):
            if raw_:
                lis.append(u'{lString}[{rString}'.format(lString='', rString='\r\n'))

                c = len(raw_)
                for seq, i in enumerate(raw_):
                    if seq < c - 1:
                        addValueFnc_(i, lString=lString, rString=',\r\n', rawType=list)
                    else:
                        addValueFnc_(i, lString=lString, rString='\r\n', rawType=list)

                lis.append(u'{lString}]{rString}'.format(lString=lString, rString=rString))

            else:
                lis.append(u'{lString}[]{rString}\r\n'.format(lString=lString, rString=rString))

        def addDictionaryFnc_(raw_, lString, rString):
            if raw_:
                lis.append(u'{lString}{{{rString}'.format(lString='', rString='\r\n'))

                c = len(raw_)
                for seq, (k, v) in enumerate(raw_.items()):
                    addMemberFnc_(k, lString=lString + defIndentString, rString=': ')

                    if seq < c - 1:
                        addValueFnc_(v, lString=lString, rString=',\r\n', rawType=dict)
                    else:
                        addValueFnc_(v, lString=lString, rString='\r\n', rawType=dict)

                lis.append(u'{lString}}}{rString}'.format(lString=lString, rString=rString))

            else:
                lis.append(u'{lString}{{}}{rString}'.format(lString='', rString=rString))

        def addRawFnc_(raw_):
            if raw_ is None:
                addNoneFnc_(lString='', rString='\r\n')

            elif isinstance(raw_, list) or isinstance(raw_, tuple):
                addListFnc_(raw_, lString='', rString='\r\n')

            elif isinstance(raw_, dict):
                addDictionaryFnc_(raw_, lString='', rString='\r\n')

        defIndentString = ' ' * indent

        lis = [
            u'{} = '.format(cls.__name__)
        ]

        addRawFnc_(raw)

        return ''.join(lis)

    def __str__(self):
        if self._strRaw():
            return self._toJsonStringMethod(self._strRaw())
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
            print u'# Lynxi <{}>'.format(lxBasic.getOsActiveViewTime())
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


class Abc_PthRoot(Basic):
    def _initAbcPthRoot(self):
        pass

    @property
    def active(self):
        return self._activePath()

    def _activePath(self):
        pass

    @property
    def server(self):
        return self._serverPath()

    @classmethod
    def _serverPath(cls):
        pass

    @property
    def local(self):
        return self._localPath()

    @classmethod
    def _localPath(cls):
        pass

    @property
    def develop(self):
        return self._developPath()

    @classmethod
    def _developPath(cls):
        pass

    @property
    def product(self):
        return self._productPath()

    @classmethod
    def _productPath(cls):
        pass

    def _strRaw(self):
        return lxBasic.orderedDict(
            [
                (self.Path_Key_Active, self.server),
                (self.Path_Key_Server, self.server),
                (self.Path_Key_Local, self.local),
                (self.Path_Key_Develop, self.develop),
                (self.Path_Key_Product, self.product)
            ]
        )


class Root(Abc_PthRoot):
    def __init__(self):
        self._initAbcPthRoot()

    def _activePath(self):
        return self._serverPath()

    @classmethod
    def _serverPath(cls):
        if cls.isDevelop():
            return cls._developPath()
        return cls._productPath()

    @classmethod
    def _localPath(cls):
        return cls.Path_Local_Default

    @classmethod
    def _developPath(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Develop)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default

    @classmethod
    def _productPath(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Product)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default


class Abc_PthDirectory(Basic):
    DIRECTORY_CLS = None

    def _initAbcPthDirectory(self, *args):
        self.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/{self.subpath}',
            self.Path_Key_Server: u'{self.root.server}/{self.subpath}',
            self.Path_Key_Local: u'{self.root.local}/{self.subpath}',
            self.Path_Key_Develop: u'{self.root.develop}/{self.subpath}',
            self.Path_Key_Product: u'{self.root.product}/{self.subpath}'
        }

        self._root = self.DIRECTORY_CLS()

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

    def pathName(self):
        return self._subNameString

    @property
    def subname(self):
        return self.pathName()

    def baseName(self):
        return self._baseName

    @property
    def basename(self):
        return self.baseName()

    def _activePath(self):
        return self.pathFormatString[self.Path_Key_Active].format(**self._formatDict())

    @property
    def active(self):
        return self._activePath()

    def _serverPath(self):
        return self.pathFormatString[self.Path_Key_Server].format(**self._formatDict())

    @property
    def server(self):
        return self._serverPath()

    def _localPath(self):
        return self.pathFormatString[self.Path_Key_Local].format(**self._formatDict())

    @property
    def local(self):
        return self._localPath()

    def _developPath(self):
        return self.pathFormatString[self.Path_Key_Develop].format(**self._formatDict())

    @property
    def develop(self):
        return self._developPath()

    def _productPath(self):
        return self.pathFormatString[self.Path_Key_Product].format(**self._formatDict())

    @property
    def product(self):
        return self._productPath()

    def _formatDict(self):
        return {
            self.Attr_Key_Self: self,
        }

    def _strRaw(self):
        return lxBasic.orderedDict(
            [
                (self.Path_Key_Active, self.server),
                (self.Path_Key_Server, self.server),
                (self.Path_Key_Local, self.local),
                (self.Path_Key_Develop, self.develop),
                (self.Path_Key_Product, self.product)
            ]
        )


class UserSubRoot(Abc_PthDirectory):
    DIRECTORY_CLS = Root

    def __init__(self):
        self._initAbcPthDirectory(self.Folder_User)


class UserBranch(Abc_PthDirectory):
    DIRECTORY_CLS = UserSubRoot

    def __init__(self, *args):
        self._initAbcPthDirectory(*args)


class UserPreset(Basic):
    Folder_Preset = 'preset'

    Folder_Render = 'render'
    Folder_Project = 'project'
    Folder_Ui = 'ui'
    Folder_Filter = 'filter'
    def __init__(self):
        self._root = UserBranch(lxBasic.getOsUser())

    def _activePath(self):
        return self._root._localPath()

    def uiDirectory(self):
        return u'{}/{}'.format(self._activePath(), self.Folder_Ui)

    def renderDirectory(self):
        return u'{}/{}'.format(self._activePath(), self.Folder_Render)

    def projectConfigFile(self):
        return u'{}/{}{}'.format(self._activePath(), self.Folder_Project, self.Ext_Json)

    def appProjectFile(self, applicationName, appVersion):
        return u'{}/{}/{}.{}{}'.format(self._activePath(), self.Folder_Project, applicationName, appVersion, self.Ext_Json)

    def uiFilterHistoryFile(self):
        return u'{}/{}.history{}'.format(self.uiDirectory(), self.Folder_Filter, self.Ext_Json)
