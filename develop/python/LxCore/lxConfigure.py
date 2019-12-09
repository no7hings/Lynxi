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
    Root_Develop_Default = 'e:/myworkspace/td/lynxi'

    Path_Local_Default = 'c:/.lynxi'

    Key_Environ_Python_Version = 'LYNXI_PYTHON_VERSION'

    Key_Environ_Enable_Develop = 'LYNXI_DEVELOP'

    Key_Environ_Path_Plug_Maya_Local = 'LYNXI_MAYA_PUSH_PATH'
    Key_Environ_Path_Plug_Maya_Server = 'LYNXI_MAYA_PLUG_PATH'
    Key_Environ_Path_Plug_Windows_Local = 'LYNXI_WINDOWS_PUSH_PATH'
    Key_Environ_Path_Plug_Windows_Server = 'LYNXI_WINDOWS_PLUG_PATH'

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
    Folder_Source = 'source'
    Folder_Compile = 'compile'
    Folder_Plug = 'plug'

    Folder_Maya = 'maya'
    Folder_Windows = 'windows'
    Folder_Python = 'python'
    Folder_Package = 'package'
    Folder_Qt = 'qt'
    Folder_Exe = 'exe'

    Folder_User = 'user'

    Folder_Share = 'share'
    Folder_Definition = 'definition'

    Key_User = 'user'
    Key_Timestamp = 'timestamp'

    Key_Server = 'server'
    Key_Local = 'local'

    Ext_Json = '.json'
    
    Key_Enable = 'enable'
    Key_Version = 'version'
    Key_Active = 'active'
    Key_Dependent = 'dependent'

    Key_App_Name = 'appname'
    Key_App_Version = 'appversion'

    Key_Python_Version = 'pythonversion'
    Key_Python_Package = 'pythonpackage'
    Key_Python_Module = 'pythonmodule'

    Key_Python_Import_Name = 'importname'

    Key_Module_App = 'moduleapp'
    Key_Module_Name = 'modulename'
    Key_Module_Version = 'moduleversion'

    Key_Package_App = 'packageapp'
    Key_Package_Name = 'packagename'
    Key_Package_Version = 'packageversion'
    Key_Package_Path = 'packagepath'
    Key_Package_Source_Path = 'sourcepath'

    Key_Plug_Name = 'plugname'
    Key_Plug_Version = 'plugversion'
    Key_Plug_Source_Path = 'plugpath'

    Key_Plug_Load_Name = 'loadname'
    Key_Plug_Module_Name = 'modulename'

    Version_Default = '0.0.0'
    Version_Active = 'active'

    App_Share = 'share'
    App_Maya = 'maya'

    Value_Python_Version_Default = '2.7.x'

    Python_Package_PyQt = 'PtQt'

    @staticmethod
    def _toSubPathMethod(*args):
        if args:
            if len(args) > 1:
                if isinstance(args[0], list) or isinstance(args[0], tuple):
                    return '/'.join(list(args[0]))
                return '/'.join(list(args))
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

    def dict(self):
        return {}

    #
    def _toStr(self, dic):
        return 'object = {}\r\n'.format(self.__class__.__name__) + '\r\n'.join(['{} = {}'.format(k, v) for k, v in dic.items()])

    def __str__(self):
        if self.dict():
            return self._toStr(self.dict())
        return ''


class Message(Basic):
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

    @classmethod
    def serverDirectory(cls):
        pass

    @classmethod
    def localDirectory(cls):
        pass

    @classmethod
    def developDirectory(cls):
        pass

    @classmethod
    def productDirectory(cls):
        pass

    def dict(self):
        return {
            self.Key_Server: self.serverDirectory(),
            self.Key_Local: self.localDirectory()
        }


class LynxiRoot(_AbcRoot):
    def __init__(self):
        self._initAbcRoot()

    def directory(self):
        return self.serverDirectory()

    @classmethod
    def serverDirectory(cls):
        if cls.isDevelop():
            return cls.developDirectory()
        return cls.productDirectory()

    @classmethod
    def localDirectory(cls):
        return cls.Path_Local_Default

    @classmethod
    def developDirectory(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Develop)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default

    @classmethod
    def productDirectory(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Module)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default


class ToolkitRoot(_AbcRoot):
    def __init__(self):
        self._initAbcRoot()

    def directory(self):
        return self.serverDirectory()

    @classmethod
    def serverDirectory(cls):
        if cls.isDevelop():
            return cls.developDirectory()
        return cls.productDirectory()

    @classmethod
    def localDirectory(cls):
        return cls.Path_Local_Default

    @classmethod
    def developDirectory(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Develop)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default

    @classmethod
    def productDirectory(cls):
        data = lxBasic.getOsEnvironValue(cls.Key_Environ_Path_Toolkit)
        if data is not None:
            return data.replace('\\', '/')
        return cls.Root_Develop_Default


class _AbcPath(Basic):
    ROOT_CLS = None

    def _initAbcPath(self, *args):
        self._root = self.ROOT_CLS()
        self._subPath = self._toSubPathMethod(*args)

    def root(self):
        return self._root

    def directory(self):
        return u'{}/{}'.format(self._root.directory(), self._subPath)

    def serverDirectory(self):
        return u'{}/{}'.format(self._root.serverDirectory(), self._subPath)

    def localDirectory(self):
        return u'{}/{}'.format(self._root.localDirectory(), self._subPath)

    def developDirectory(self):
        return u'{}/{}'.format(self._root.developDirectory(), self._subPath)

    def productDirectory(self):
        return u'{}/{}'.format(self._root.productDirectory(), self._subPath)

    def dict(self):
        return {
            self.Key_Server: self.serverDirectory(),
            self.Key_Local: self.localDirectory()
        }


class _AbcFile(Basic):
    PATH_CLS = None
    DefaultRaw = {}

    def _initAbcFile(self, pathArgs, fileBasename, ext):
        self._path = self.PATH_CLS(*pathArgs)

        self._fileName = '{}{}'.format(fileBasename, ext)

    def path(self):
        return self._path

    def createDevelopFile(self):
        pass

    def directory(self):
        return self._path.directory()

    def serverDirectory(self):
        return self._path.serverDirectory()

    def localDirectory(self):
        return self._path.localDirectory()

    def developDirectory(self):
        return self._path.developDirectory()

    def productDirectory(self):
        return self._path.productDirectory()

    def fileName(self):
        return self._fileName

    def file(self):
        return u'{}/{}'.format(self.directory(), self.fileName())

    def hasFile(self):
        return lxBasic.isOsExist(self.file())

    def developFile(self):
        return u'{}/{}'.format(self.developDirectory(), self.fileName())

    def hasDevelopFile(self):
        return lxBasic.isOsExist(self.developFile())

    def productFile(self):
        return u'{}/{}'.format(self.productDirectory(), self.fileName())

    def hasProductFile(self):
        return lxBasic.isOsExist(self.productFile())

    def raw(self):
        pass

    def __str__(self):
        return self._toStr(self.raw())


class _AbcJsonFile(_AbcFile):
    def _initAbcJsonFile(self, pathArgs, fileBasename):
        self._initAbcFile(pathArgs, fileBasename, '.json')

    def createDevelopFile(self):
        lxBasic.writeOsJson(self.DefaultRaw, self.file())

    def raw(self):
        if self.hasFile():
            return lxBasic.readOsJson(self.file())
        return self.DefaultRaw


class _AbcConfig(_AbcJsonFile):
    def _initAbcConfig(self, *args):
        self._initAbcJsonFile(args, 'config')

    def addVersion(self, version):
        pass


class _AbcModule(_AbcJsonFile):
    def _initAbcModule(self, *args):
        self._initAbcJsonFile(args, 'module')


class ExeSubRoot(_AbcPath):
    ROOT_CLS = LynxiRoot

    def __init__(self):
        self._initAbcPath(self.Folder_Exe)


class CodeModuleSubRoot(_AbcPath):
    ROOT_CLS = LynxiRoot

    def __init__(self):
        self._initAbcPath(self.Folder_Module)


class PythonModuleBranch(_AbcPath):
    ROOT_CLS = CodeModuleSubRoot

    def __init__(self, *args):
        self._initAbcPath(self.Folder_Python, *args)


class CodeProductSubRoot(_AbcPath):
    ROOT_CLS = LynxiRoot

    def __init__(self):
        self._initAbcPath(self.Folder_Product)


class PythonProductBranch(_AbcPath):
    ROOT_CLS = CodeProductSubRoot

    def __init__(self, *args):
        self._initAbcPath(self.Folder_Python, *args)


class PythonProductCompileBranch(_AbcPath):
    ROOT_CLS = CodeProductSubRoot

    def __init__(self, *args):
        self._initAbcPath(self.Folder_Python, self.Folder_Compile, *args)


class IconSubRoot(_AbcPath):
    ROOT_CLS = LynxiRoot

    def __init__(self):
        self._initAbcPath(self.Folder_Icon)


class PlugSubRoot(_AbcPath):
    ROOT_CLS = LynxiRoot

    def __init__(self):
        self._initAbcPath(self.Folder_Plug)


class _AbcAppPlugBranch(_AbcPath):
    ROOT_CLS = PlugSubRoot
    AppName = None

    def __init__(self, *args):
        self._initAbcAppPlugBranch(*args)

    def _initAbcAppPlugBranch(self, *args):
        self._initAbcPath(self.AppName, *args)


class PlugMayaBranch(_AbcAppPlugBranch):
    AppName = Lynxi_App_Maya
    def __init__(self, *args):
        self._initMayaPlugRoot(*args)

    def _initMayaPlugRoot(self, *args):
        self._initAbcAppPlugBranch(*args)


class _AbcAppPlugConfig(_AbcConfig):
    PATH_CLS = None
    DefaultRaw = {
        Basic.Key_Enable: True,
        Basic.Key_Version: [],
        Basic.Key_Plug_Load_Name: [],
        Basic.Key_Plug_Module_Name: None
    }
    AppName = None

    def _initAbcAppPlugConfig(self, appVersion, plugName):
        self._appName = self.AppName
        self._appVersion = appVersion
        self._plugName = plugName

        self._initAbcConfig(self.appVersion(), self.plugName())

    def appName(self):
        return self._appName

    def appVersion(self):
        return self._appVersion

    def plugName(self):
        return self._plugName

    def moduleName(self):
        if self.hasFile():
            return self.raw().get(self.Key_Plug_Module_Name, False)
        return self.plugName()

    def enable(self):
        if self.hasFile():
            return self.raw().get(self.Key_Enable, False)
        return False

    def versions(self):
        if self.hasFile():
            return self.raw().get(self.Key_Version, [])
        return []

    def loadNames(self):
        if self.raw():
            return self.raw().get(self.Key_Plug_Load_Name, [])
        return []


class MayaPlugConfig(_AbcAppPlugConfig):
    PATH_CLS = PlugMayaBranch
    AppName = Lynxi_App_Maya
    def __init__(self, appVersion, plugName):
        self._initMayaPlugConfig(appVersion, plugName)

    def _initMayaPlugConfig(self, appVersion, plugName):
        self._initAbcAppPlugConfig(appVersion, plugName)


class MayaSharePlugConfig(_AbcAppPlugConfig):
    PATH_CLS = PlugMayaBranch
    AppName = Lynxi_App_Maya
    def __init__(self, appVersion, plugName):
        self._initMayaSharePlugConfig(appVersion, plugName)

    def _initMayaSharePlugConfig(self, appVersion, plugName):
        self._appName = self.AppName
        self._appVersion = appVersion
        self._plugName = plugName

        self._initAbcConfig(self.Folder_Share, self.plugName())


class _AbcAppPlug(Basic):
    APP_PLUG_CONFIG_CLS = None

    def _initAbcAppPlug(self, appVersion, plugName, plugVersion):
        self._plugConfig = self.APP_PLUG_CONFIG_CLS(appVersion, plugName)

        self._plugVersion = plugVersion

    def plugConfig(self):
        return self._plugConfig

    def appName(self):
        return self.plugConfig().appName()

    def appVersion(self):
        return self.plugConfig().appVersion()

    def plugName(self):
        return self.plugConfig().plugName()
    
    def plugVersion(self):
        return self._plugVersion

    def serverDirectory(self):
        return u'{}/{}'.format(self._plugConfig.serverDirectory(), self._plugVersion)

    def localDirectory(self):
        return u'{}/{}'.format(self._plugConfig.localDirectory(), self._plugVersion)

    def createServerTimestamp(self):
        self._createTimestampMethod(
            self.serverSourcePath(), self.serverTimestampFile()
        )

    def createLocalTimestamp(self):
        self._createTimestampMethod(
            self.localSourcePath(), self.localTimestampFile()
        )

    def serverTimestampFile(self):
        return u'{}/timestamp.json'.format(
            self.serverDirectory()
        )

    def localTimestampFile(self):
        return u'{}/timestamp.json'.format(
            self.localDirectory()
        )

    def serverTimestampDatum(self):
        if lxBasic.isOsExist(self.serverTimestampFile()) is False:
            self.createServerTimestamp()
        return lxBasic.readOsJson(self.serverTimestampFile()) or {}

    def localTimestampDatum(self):
        if lxBasic.isOsExist(self.localTimestampFile()) is False:
            self.createLocalTimestamp()
        return lxBasic.readOsJson(self.localTimestampFile()) or {}

    def environFile(self):
        return u'{}/environ.json'.format(
            self.serverDirectory()
        )

    def environDatum(self):
        return lxBasic.readOsJson(self.environFile()) or []

    def toAppEnvironString(self):
        if self.environDatum():
            return '\r\n'.join([i.format(**self.dict())for i in self.environDatum()])

    def sourceDirectory(self):
        return '{}/source'.format(self.serverDirectory())

    def serverSourceDirectory(self):
        return '{}/source'.format(self.serverDirectory())

    def localSourceDirectory(self):
        return '{}/source'.format(self.localDirectory())

    def dict(self):
        return {
            self.Key_Plug_Name: self.plugConfig().plugName(),
            self.Key_Plug_Version: self.plugVersion(),
            self.Key_Plug_Source_Path: self.sourceDirectory()
        }

    def _getChangedSourceFiles(self):
        return self._getChangedFileMethod(
            self.serverTimestampDatum(), self.localTimestampDatum()
        )

    def localizationSource(self):
        changedFileLis = self._getChangedSourceFiles()
        if changedFileLis:
            for relativeOsFile in changedFileLis:
                sourceFile = self.serverSourceDirectory() + relativeOsFile
                targetFile = self.localSourceDirectory() + relativeOsFile

                lxBasic.setOsFileCopy(sourceFile, targetFile, force=False)

                traceMessage = u'localization Plug "{}" : "{}" > "{}"'.format(self.plugName(), sourceFile, targetFile)
                Message().traceResult(traceMessage)

                lxBasic.setOsFileCopy(self.serverTimestampFile(), self.localTimestampFile())
        else:
            traceMessage = u'Plug "{}" is "Non - Changed"'.format(self.plugName())
            Message().traceResult(traceMessage)

    def addPath(self):
        env.PATH += self.sourceDirectory()


class MayaPlug(_AbcAppPlug):
    RESOURCE_CONFIG_CLS = MayaPlugConfig

    def __init__(self, appVersion, plugName, plugVersion):
        self._initMayaPlug(
            appVersion, plugName, plugVersion
        )
    
    def _initMayaPlug(self, appVersion, plugName, plugVersion):
        self._initAbcAppPlug(
            appVersion, plugName, plugVersion
        )

    def moduleName(self):
        return self.plugConfig().moduleName()

    def moduleFile(self):
        return u'{}/module.json'.format(
            self.serverDirectory()
        )

    def moduleDatum(self):
        return lxBasic.readOsJson(self.moduleFile()) or []

    def dict(self):
        return {
            self.Key_Plug_Name: self.plugConfig().plugName(),
            self.Key_Plug_Module_Name: self.plugConfig().moduleName(),
            self.Key_Plug_Version: self.plugVersion(),
            self.Key_Plug_Source_Path: self.sourceDirectory()
        }

    def appModuleDatum(self):
        if self.moduleDatum():
            return '\r\n'.join([i.format(**self.dict())for i in self.moduleDatum()])

    def appModuleFile(self):
        return '{}/{}.mod'.format(lxBasic.getMayaAppOsModPath(self.appVersion()), self.moduleName())

    def pushModule(self):
        origDatum = lxBasic.readOsData(self.appModuleFile())
        raw = self.appModuleDatum()
        if origDatum != raw:
            lxBasic.writeOsData(
                raw, self.appModuleFile()
            )
            traceMessage = u'Plug "{}" Update Module : "{}" '.format(self.plugName(), self.appModuleFile())
            Message().traceResult(traceMessage)
        else:
            traceMessage = u'Plug "{}" Module is "Non - Changed"'.format(self.plugName())
            Message().traceResult(traceMessage)


class MayaSharePlug(MayaPlug):
    RESOURCE_CONFIG_CLS = MayaSharePlugConfig

    def __init__(self, appVersion, plugName, plugVersion):
        self._initMayaPlug(
            appVersion, plugName, plugVersion
        )


class PackageSubRoot(_AbcPath):
    ROOT_CLS = LynxiRoot

    def __init__(self):
        self._initAbcPath(self.Folder_Package)


class PythonPackageBranch(_AbcPath):
    ROOT_CLS = PackageSubRoot

    def __init__(self, *args):
        self._initAbcPath(self.Folder_Python, *args)


class _AbcPythonResourceConfig(_AbcConfig):
    PATH_CLS = None
    DefaultRaw = {
        Basic.Key_Enable: True,
        Basic.Key_Version: [],
   }
    def _initAbcPythonResourceConfig(self, pythonVersion, *args):
        self._pythonVersion = pythonVersion
        self._initAbcConfig(pythonVersion, *args)

    def pythonVersion(self):
        return self._pythonVersion

    def enable(self):
        if self.hasFile():
            return self.raw().get(self.Key_Enable, False)
        return False

    def versions(self):
        if self.hasFile():
            return self.raw().get(self.Key_Version, [])
        return []


class _AbcPythonModuleConfig(_AbcPythonResourceConfig):
    PATH_CLS = None
    DefaultRaw = {
        Basic.Key_Enable: True,
        Basic.Key_Version: [],
        Basic.Key_Python_Import_Name: None,
        Basic.Key_Python_Package: [],
        Basic.Key_Python_Module: []
    }
    def _initAbcPythonModuleConfig(self, pythonVersion, *args):
        self._moduleName = args[-1]
        args_ = list(args[:-1])
        args_.append(self._moduleName.lower())
        self._initAbcPythonResourceConfig(pythonVersion, *args_)

    def moduleName(self):
        return self._moduleName


class PythonShareModuleConfig(_AbcPythonModuleConfig):
    PATH_CLS = PythonModuleBranch
    def __init__(self, pythonVersion, moduleName):
        self._initPythonShareModuleConfig(pythonVersion, moduleName)

    def _initPythonShareModuleConfig(self, pythonVersion, moduleName):
        self._initAbcPythonModuleConfig(
            pythonVersion,
            self.App_Share,
            moduleName
        )


class _AbcPythonPackageConfig(_AbcPythonResourceConfig):
    PATH_CLS = None
    DefaultRaw = {
        Basic.Key_Enable: True,
        Basic.Key_Version: [],
        Basic.Key_Python_Import_Name: None,
        Basic.Key_Python_Package: []
    }

    def _initAbcPythonPackageConfig(self, pythonVersion, *args):
        self._packageName = args[-1]
        args_ = list(args[:-1])
        args_.append(self._packageName.lower())
        self._initAbcPythonResourceConfig(pythonVersion, *args_)

    def packageName(self):
        return self._packageName


class PythonSharePackageConfig(_AbcPythonPackageConfig):
    PATH_CLS = PythonPackageBranch

    def __init__(self, pythonVersion, packageName):
        self._initPythonSharePackageConfig(pythonVersion, packageName)

    def _initPythonSharePackageConfig(self, pythonVersion, packageName):
        self._initAbcPythonPackageConfig(
            pythonVersion,
            self.App_Share,
            packageName
        )


class _AbcPythonAppPackageConfig(_AbcPythonPackageConfig):
    def _initAbcPythonAppPackageConfig(self, pythonVersion, appName, appVersion, packageName):
        self._initAbcPythonPackageConfig(pythonVersion, packageName)

        self._appName = appName
        self._appVersion = appVersion

        self._initAbcConfig(
            self.pythonVersion(),
            appName, appVersion,
            self.packageName().lower()
        )

    def appName(self):
        return self._appName

    def appVersion(self):
        return self._appVersion


class PythonMayaPackageConfig(_AbcPythonAppPackageConfig):
    PATH_CLS = PythonPackageBranch

    def __init__(self, pythonVersion, appVersion, packageName):
        self._initPythonMayaPackageConfig(pythonVersion, appVersion, packageName)

    def _initPythonMayaPackageConfig(self, pythonVersion, appVersion, packageName):
        self._initAbcPythonAppPackageConfig(
            pythonVersion,
            Lynxi_App_Maya,
            appVersion, packageName
        )


class _AbcPythonPackage(Basic):
    RESOURCE_CONFIG_CLS = None
    def _initAbcPythonPackage(self, pythonVersion, packageName, packageVersion):
        self._packageConfig = self.RESOURCE_CONFIG_CLS(pythonVersion, packageName)

        self._packageVersion = packageVersion

    def packageConfig(self):
        return self._packageConfig

    def pythonVersion(self):
        return self.packageConfig().pythonVersion()

    def packageName(self):
        return self.packageConfig().packageName()

    def packageVersion(self):
        return self._packageVersion

    def directory(self):
        return u'{}/{}'.format(self.packageConfig().directory(), self.packageVersion())

    def serverDirectory(self):
        return u'{}/{}'.format(self.packageConfig().serverDirectory(), self.packageVersion())

    def localDirectory(self):
        return u'{}/{}'.format(self.packageConfig().localDirectory(), self.packageVersion())

    def developDirectory(self):
        return u'{}/{}'.format(self.packageConfig().developDirectory(), self.packageVersion())

    def productDirectory(self):
        return u'{}/{}'.format(self.packageConfig().productDirectory(), self.packageVersion())

    def sourceDirectory(self):
        return u'{}/{}'.format(self.directory(), self.Folder_Source)

    def hasSource(self):
        return lxBasic.isOsExist(self.sourceDirectory())

    def serverSourceDirectory(self):
        return u'{}/{}'.format(self.serverDirectory(), self.Folder_Source)

    def hasServerSource(self):
        return lxBasic.isOsExist(self.serverDirectory())

    def localSourceDirectory(self):
        return u'{}/{}'.format(self.localDirectory(), self.Folder_Source)

    def developSourceDirectory(self):
        return u'{}/{}'.format(self.developDirectory(), self.Folder_Source)

    def hasDevelopSource(self):
        return lxBasic.isOsExist(self.developSourceDirectory())

    def productSourceDirectory(self):
        return u'{}/{}'.format(self.productDirectory(), self.Folder_Source)

    def hasProductSource(self):
        return lxBasic.isOsExist(self.productSourceDirectory())

    def serverTimestampFile(self):
        return u'{}/timestamp.json'.format(
            self.serverDirectory()
        )

    def createServerTimestamp(self):
        self._createTimestampMethod(
            self.serverSourceDirectory(), self.serverTimestampFile()
        )

    def serverTimestampDatum(self):
        if lxBasic.isOsExist(self.serverTimestampFile()) is False:
            self.createServerTimestamp()
        return lxBasic.readOsJson(self.serverTimestampFile()) or {}

    def localTimestampFile(self):
        return u'{}/timestamp.json'.format(
            self.localDirectory()
        )

    def createLocalTimestamp(self):
        self._createTimestampMethod(
            self.localSourceDirectory(), self.localTimestampFile()
        )

    def localTimestampDatum(self):
        if lxBasic.isOsExist(self.localTimestampFile()) is False:
            self.createLocalTimestamp()
        return lxBasic.readOsJson(self.localTimestampFile()) or {}

    def _getChangedSourceFiles(self):
        return self._getChangedFileMethod(
            self.serverTimestampDatum(), self.localTimestampDatum()
        )

    def dict(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Python_Version, self.pythonVersion()),
                (self.Key_Package_Name, self.packageName()),
                (self.Key_Package_Version, self.packageVersion()),
                (self.Key_Package_Source_Path, self.sourceDirectory())
            ]
        )

    def addPath(self):
        env.PATH += self.sourceDirectory()

    def localizationSource(self):
        changedFileLis = self._getChangedSourceFiles()
        if changedFileLis:
            for relativeOsFile in changedFileLis:
                sourceFile = self.serverSourceDirectory() + relativeOsFile
                targetFile = self.localSourceDirectory() + relativeOsFile

                lxBasic.setOsFileCopy(sourceFile, targetFile, force=False)

                traceMessage = u'Localization Package "{}" : "{}" > "{}"'.format(self.packageName(), sourceFile, targetFile)
                Message().traceResult(traceMessage)

                lxBasic.setOsFileCopy(self.serverTimestampFile(), self.localTimestampFile())
        else:
            traceMessage = u'Package "{}"  is "Non - Changed"'.format(self.packageName())
            Message().traceResult(traceMessage)


class PythonSharePackage(_AbcPythonPackage):
    RESOURCE_CONFIG_CLS = PythonSharePackageConfig
    def __init__(self, pythonVersion, packageName, packageVersion):
        self._initAbcPythonPackage(pythonVersion, packageName, packageVersion)


class _AbcPythonAppPackage(_AbcPythonPackage):
    RESOURCE_CONFIG_CLS = None

    def _initAbcPythonAppPackage(self, pythonVersion, appName, appVersion, packageName, packageVersion):
        self._packageConfig = self.RESOURCE_CONFIG_CLS(pythonVersion, appVersion, packageName)

        self._packageVersion = packageVersion

        self._appName = appName
        self._appVersion = appVersion

    def appName(self):
        return self._appName

    def appVersion(self):
        return self._appVersion


class PythonMayaPackage(_AbcPythonAppPackage):
    RESOURCE_CONFIG_CLS = PythonMayaPackageConfig
    def __init__(self, pythonVersion, appVersion, packageName, packageVersion):
        self._initAbcPythonAppPackage(
            pythonVersion,
            Lynxi_App_Maya, appVersion,
            packageName, packageVersion
        )


class UserSubRoot(_AbcPath):
    ROOT_CLS = LynxiRoot

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

    def directory(self):
        return self._root.localDirectory()

    def uiDirectory(self):
        return u'{}/{}'.format(self.directory(), self.Folder_Ui)

    def renderDirectory(self):
        return u'{}/{}'.format(self.directory(), self.Folder_Render)

    def projectConfigFile(self):
        return u'{}/{}{}'.format(self.directory(), self.Folder_Project, self.Ext_Json)

    def appProjectFile(self, appName, appVersion):
        return u'{}/{}/{}.{}{}'.format(self.directory(), self.Folder_Project, appName, appVersion, self.Ext_Json)

    def uiFilterHistoryFile(self):
        return u'{}/{}.history{}'.format(self.uiDirectory(), self.Folder_Filter, self.Ext_Json)


class LogSubRoot(_AbcPath):
    ROOT_CLS = LynxiRoot

    def __init__(self):
        self._initAbcPath(self.Folder_Log)


class Log(Basic):
    def __init__(self):
        self._subRoot = LogSubRoot()

    def exceptionFile(self):
        return u'{}/{}.exception.log'.format(
            self._subRoot.serverDirectory(), lxBasic.getOsActiveDateTag()
        )

    def errorFile(self):
        return u'{}/{}.error.log'.format(
            self._subRoot.serverDirectory(), lxBasic.getOsActiveDateTag()
        )

    def developFile(self):
        return u'{}/{}.develop.log'.format(
            self._subRoot.serverDirectory(), lxBasic.getOsActiveDateTag()
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


class PythonModule(_AbcConfig):
    PATH_CLS = PythonModuleBranch
    DefaultRaw = {
        Basic.Key_Python_Package: {},
        Basic.Key_Version: [],
        Basic.Key_Active: Basic.Version_Default,
        Basic.Key_Python_Version: '2.7.x'
    }
    def __init__(self, moduleName):
        self._initPythonModule(moduleName)

    def _initPythonModule(self, moduleName):
        self._initAbcConfig()

        self._moduleName = moduleName

    def _getPythonPackageLis(self):
        if self.hasFile():
            return self.raw().get(self.Key_Python_Package, {})
        return {}

    def developDirectory(self):
        return self.path().developDirectory()

    def productDirectory(self):
        return self.productCompileDirectory()

    def productCompileDirectory(self):
        return u'{}/{}/{}/{}'.format(
            PythonProductBranch().developDirectory(),
            self.moduleName().lower(), self.active(), self.Folder_Compile
        )

    def productSourceDirectory(self):
        return u'{}/{}/{}/{}'.format(
            PythonProductBranch().developDirectory(),
            self.moduleName().lower(), self.active(), self.Folder_Source
        )

    def moduleName(self):
        return self._moduleName

    def active(self):
        if self.hasFile():
            return self.raw().get(self.Key_Active, self.Version_Default)
        return self.Version_Default

    def versions(self):
        if self.hasFile():
            return self.raw().get(self.Key_Version, [])
        return []

    def pythonVersion(self):
        if self.hasFile():
            return self.raw().get(self.Key_Python_Version, '2.7.x')
        return '2.7.x'

    def _getRelativePyFileLis(self):
        lis = []

        osPath = '{}/{}'.format(self.developDirectory(), self.moduleName())

        osFiles = lxBasic.getOsFiles(osPath)
        if osFiles:
            for osFile in osFiles:
                if osFile.endswith('.py'):
                    lis.append('/{}{}'.format(self.moduleName(), osFile[len(osPath):]))
        return lis

    def publishProduct(self):
        relativeFileLis = self._getRelativePyFileLis()
        if relativeFileLis:
            import py_compile

            developDirectory = self.developDirectory()

            productPyDirectory = self.productSourceDirectory()
            productPycDirectory = self.productCompileDirectory()
            for relativeFile in relativeFileLis:
                pyFile = developDirectory + relativeFile
                py_compile.compile(pyFile)

                pycFile = pyFile[:-3] + '.pyc'

                productPyFile = productPyDirectory + pyFile[len(developDirectory):]
                lxBasic.setOsFileCopy(pyFile, productPyFile)
                Message().traceResult(
                    u'{} > {}'.format(pyFile, productPyFile)
                )

                productPycFile = productPycDirectory + pycFile[len(developDirectory):]
                lxBasic.setOsFileCopy(pycFile, productPycFile)
                Message().traceResult(
                    u'{} > {}'.format(pycFile, productPycFile)
                )

    def addDevelopPath(self):
        env.PATH += self.developDirectory()

    def addProductPath(self):
        env.PATH += self.productDirectory()

    def hashKey(self):
        return u'{}/{}'.format(self.developDirectory(), 'hash.json')


class Lynxi_Module_Python(_AbcModule):
    PATH_CLS = PythonModuleBranch

    Lynxi_Python_Module_Core = 'LxCore'
    Lynxi_Python_Module_Database = 'LxDatabase'
    Lynxi_Python_Module_Ui = 'LxUi'
    Lynxi_Python_Module_Interface = 'LxInterface'

    Lynxi_Python_Module_Maya = 'LxMaya'
    Lynxi_Python_Module_Deadline = 'LxDeadline'

    Lynxi_Python_Module_Graph = 'LxGraph'
    Lynxi_Python_Module_Material = 'LxMaterial'

    Lynxi_Python_Module_Basic_Lis = [
        'LxCore.config.appConfig',
        'LxCore.method.basic._methodBasic',
        'LxCore.method._osMethod',
        'LxCore.method._dbMethod',
        'LxCore.method._uiMethod',
        'LxCore.method._productMethod',

        'LxCore.lxBasic',
        'LxCore.lxConfigure',
        # Ui
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

    Lynxi_Python_Module_Maya_Lis = [
        'LxMaya.method.config._maConfig',

        'LxMaya.method.basic._maMethodBasic',

        'LxMaya.method._maUiMethod',
        'LxMaya.method._maMethod',
        'LxMaya.method._maPlugMethod',
        'LxMaya.method._maProductMethod',
        'LxMaya.method',

    ]

    DefaultRaw = {
        Basic.Key_Active: Basic.Version_Default,
        Basic.Key_Python_Version: Basic.Value_Python_Version_Default,
        Basic.Key_Python_Module: {
            Lynxi_Python_Module_Core: {
                Basic.Key_Module_App: Basic.App_Share,
                Basic.Key_Active: Basic.Version_Default,
            },
            Lynxi_Python_Module_Ui: {
                Basic.Key_Enable: True,
                Basic.Key_Module_App: Basic.App_Share,
                Basic.Key_Active: Basic.Version_Default,
                Basic.Key_Python_Package: {
                    Basic.Python_Package_PyQt: {
                        Basic.Key_Package_App: Basic.App_Share,
                        Basic.Key_Active: "5.3.2"
                    }
                },
                Basic.Key_Python_Module: {
                    Lynxi_Python_Module_Core: {
                        Basic.Key_Active: Basic.Version_Active
                    }
                }
            },
            Lynxi_Python_Module_Interface: {
                Basic.Key_Enable: True,
                Basic.Key_Module_App: Basic.App_Share,
                Basic.Key_Active: Basic.Version_Default,
                Basic.Key_Python_Module: {
                    Lynxi_Python_Module_Ui: {
                        Basic.Key_Active: Basic.Version_Active
                    }
                }
            },
            Lynxi_Python_Module_Database: {
                Basic.Key_Enable: True,
                Basic.Key_Module_App: Basic.App_Share,
                Basic.Key_Active: Basic.Version_Default
            },
            Lynxi_Python_Module_Deadline: {
                Basic.Key_Enable: True,
                Basic.Key_Module_App: Basic.App_Share,
                Basic.Key_Active: Basic.Version_Default
            },
            Lynxi_Python_Module_Graph: {
                Basic.Key_Enable: False,
                Basic.Key_Module_App: Basic.App_Share,
                Basic.Key_Active: Basic.Version_Default
            },

            Lynxi_Python_Module_Material: {
                Basic.Key_Enable: False,
                Basic.Key_Module_App: Basic.App_Share,
                Basic.Key_Active: Basic.Version_Default
            },

            Lynxi_Python_Module_Maya: {
                Basic.Key_Enable: True,
                Basic.Key_Module_App: Basic.App_Maya,
                Basic.Key_Active: Basic.Version_Default
            }
        }
    }

    def __init__(self):
        self._initAbcModule()

    def publishProduct(self):
        moduleLis = [
            self.Lynxi_Python_Module_Core,
            self.Lynxi_Python_Module_Database,
            self.Lynxi_Python_Module_Ui,
            self.Lynxi_Python_Module_Interface,
            self.Lynxi_Python_Module_Maya,
            self.Lynxi_Python_Module_Deadline
        ]
        for i in moduleLis:
            pythonModule = PythonModule(i)
            pythonModule.publishProduct()

    def getPythonModules(self, osPath, moduleName):

        if self.isDevelop():
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
    def setPythonModuleUpdate_(modulePaths):
        if modulePaths:
            from LxCore import lxProgress
            # View Progress
            progressExplain = '''Update Python Module(s)'''
            maxValue = len(modulePaths)
            progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
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

        cls.setPythonModuleUpdate_(moduleLis)

    def reloadAll(self):
        import pkgutil

        moduleLis = [
            self.Lynxi_Python_Module_Core,
            self.Lynxi_Python_Module_Database,
            self.Lynxi_Python_Module_Ui,
            self.Lynxi_Python_Module_Interface,
            self.Lynxi_Python_Module_Maya,
            self.Lynxi_Python_Module_Deadline
        ]
        for i in moduleLis:
            loader = pkgutil.find_loader(i)
            if loader:
                osPath = loader.filename.replace('\\', '/')
                self.setPythonModuleUpdate_(self.getPythonModules(osPath, i))

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


class Lynxi_Icon(_AbcConfig):
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
        from LxUi.qt import qtCore
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


class _AppBasic(Basic):
    AppName = None
    PLUG_APP_BRANCH_CLS = None
    APP_PLUG_CONFIG_CLS = None

    def _initAppBasic(self, appVersion):
        self._appName = self.AppName
        self._appVersion = appVersion

    def appName(self):
        return self._appName

    def appVersion(self):
        return self._appVersion

    def plugConfigs(self):
        lis = []
        osPath = self.PLUG_APP_BRANCH_CLS(self.appName(), self.appVersion()).serverDirectory()
        if lxBasic.isOsExist(osPath):
            osFileNameLis = lxBasic.getOsFileBasenameLisByPath(osPath)
            if osFileNameLis:
                for osFileName in osFileNameLis:
                    plugConfig = self.APP_PLUG_CONFIG_CLS(self._appVersion, osFileName)
                    if plugConfig.hasFile():
                        lis.append(plugConfig)
        return lis

    def plugDatumDic(self):
        dic = lxBasic.orderedDict()
        if self._appName != LynxiValue_Unspecified:
            osPath = self.PLUG_APP_BRANCH_CLS(self._appVersion).serverDirectory()
            if lxBasic.isOsExist(osPath):
                osFileNameLis = lxBasic.getOsFileBasenameLisByPath(osPath)
                if osFileNameLis:
                    for osFileName in osFileNameLis:
                        plugConfig = self.APP_PLUG_CONFIG_CLS(self._appVersion, osFileName)
                        configFile = plugConfig.file()
                        if lxBasic.isOsExist(configFile):
                            if plugConfig.enable() is True:
                                plugName = osFileName
                                dic[plugName] = [
                                    False,
                                    u'插件预设',
                                    [
                                        [Key_Plug_Version, plugConfig.versions()],
                                        [Lynxi_Key_Plug_Load_Names, tuple(plugConfig.loadNames())],
                                        [Lynxi_Key_Plug_Load_Enable_Auto, False],
                                        ['loadCondition', ()]
                                    ]
                                ]
        return dic

    def dict(self):
        return {
            self.Key_App_Name: self.appName(),
            self.Key_App_Version: self.appVersion()
        }


class Maya(_AppBasic):
    AppName = Lynxi_App_Maya

    PLUG_APP_BRANCH_CLS = PlugMayaBranch
    APP_PLUG_CONFIG_CLS = MayaPlugConfig
    def __init__(self, appVersion):
        self._initAppBasic(appVersion)

    def environFile(self):
        return lxBasic.getMayaAppsEnvFile(self._appVersion)
