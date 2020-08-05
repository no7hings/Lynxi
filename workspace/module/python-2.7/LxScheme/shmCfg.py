# coding:utf-8
import sys

import copy

import collections

from LxBasic import bscObjects


from LxBasic import bscCfg, bscMethods


class ShmUtility(object):
    MOD_sys = sys
    MOD_copy = copy
    CLS_dic_order = collections.OrderedDict

    DEF_shm__rsc__category__platform = 'platform'
    DEF_shm__rsc__category__plf_language = 'plf-language'
    DEF_shm__rsc__category__plf_application = 'plf-application'
    DEF_shm__rsc__category__plf_lng_language = 'plf-app-language'

    DEF_shm__rsc__category__plf_package = 'plf-package'
    DEF_shm__rsc__category__plf_lng_package = 'plf-lan-package'
    DEF_shm__rsc__category__plf_App_Package = 'plf-app-package'
    DEF_shm__rsc__category__plf_app_lng_Package = 'plf-app-lan-package'

    DEF_shm__rsc__category__plf_plug = 'plf-plug'
    DEF_shm__rsc__category__plf_lng_plug = 'plf-lan-plug'
    DEF_shm__rsc__category__plf_app_lng_plug = 'plf-app-lan-plug'
    DEF_shm__rsc__category__plf_app_plug = 'plf-app-plug'

    DEF_shm__rsc__category__plf_module = 'plf-module'
    DEF_shm__rsc__category__plf_lng_module = 'plf-lan-module'
    DEF_shm__rsc__category__plf_app_lng_module = 'plf-app-lan-module'
    DEF_shm__rsc__category__plf_app_module = 'plf-app-module'

    DEF_shm__rsc__category__plf_scheme = 'plf-scheme'
    DEF_shm__rsc__category__plf_app_scheme = 'plf-app-scheme'
    DEF_shm__rsc__category__plf_lng_scheme = 'plf-lan-scheme'
    DEF_shm__rsc__category__plf_app_lng_scheme = 'plf-app-lan-scheme'
    DEF_shm__rsc__category__plf_App_Scheme = 'plf-app-scheme'

    DEF_shm__rsc__category__plf_Lng_tool = 'plf-lan-tool'
    DEF_shm__rsc__category__plf_app_lng_tool = 'plf-app-lan-tool'
    DEF_shm__rsc__category__plf_app_tool = 'plf-app-tool'

    # **************************************************************************************************************** #
    Category_Project = 'project'

    Category_Scheme_Lis = [
        DEF_shm__rsc__category__plf_scheme,
        DEF_shm__rsc__category__plf_lng_scheme,
        DEF_shm__rsc__category__plf_app_scheme,
        DEF_shm__rsc__category__plf_app_lng_scheme
    ]
    Category_Package_Lis = [
        DEF_shm__rsc__category__plf_package,
        DEF_shm__rsc__category__plf_lng_package,
        DEF_shm__rsc__category__plf_app_lng_Package,
        DEF_shm__rsc__category__plf_App_Package
    ]
    Category_Bin_Lis = [
        DEF_shm__rsc__category__platform,
        DEF_shm__rsc__category__plf_language,
        DEF_shm__rsc__category__plf_application,
        DEF_shm__rsc__category__plf_lng_language
    ]
    Category_Module_Lis = [
        DEF_shm__rsc__category__plf_module,
        DEF_shm__rsc__category__plf_lng_module,
        DEF_shm__rsc__category__plf_app_lng_module,
        DEF_shm__rsc__category__plf_app_module
    ]
    Category_Plug_Lis = [
        DEF_shm__rsc__category__plf_plug,
        DEF_shm__rsc__category__plf_lng_plug,
        DEF_shm__rsc__category__plf_app_lng_plug,
        DEF_shm__rsc__category__plf_app_plug
    ]

    DEF_shm__keyword__share = 'share'

    DEF_util__environ_key__name_scheme = 'LYNXI_NAME_SCHEME'
    Environ_KeyVAR_kit__window__version_Scheme = 'LYNXI_VERSION_SCHEME'
    Environ_Key_File_Scheme = 'LYNXI_SETUP_FILE_SCHEME'
    Environ_Key_Config_File_Scheme = 'LYNXI_CONFIG_FILE_SCHEME'

    Environ_Key_Enable_Develop = 'LYNXI_ENABLE_DEVELOP'

    DEF_util__environ_key__path_preset = u'LYNXI_PATH_PRESET'

    DEF_util__environ_key__path_kit = u'LYNXI_PATH_KIT'
    DEF_util__environ_key__path_appkit = u'LYNXI_PATH_APPKIT'
    DEF_util__environ_key__path_toolkit = u'LYNXI_PATH_TOOLKIT'

    DEF_util__environ_key__paths_source = u'LYNXI_PATHS_SOURCE'

    Environ_Key_Python_Bin_Path = u'LYNXI_BIN_PYTHON_PATH'

    Environ_Key_Loadname_Plug = u'LYNXI_LOADNAME_PLUG'
    Environ_Key_Loadname_Module = u'LYNXI_LOADNAME_MODULE'

    DEF_shm__folder__source = 'source'

    Key_User = 'user'
    Key_Timestamp = 'timestamp'

    Ext_Json = '.json'

    DEF_shm__key__enable = 'enable'
    DEF_shm__key__category = 'category'
    DEF_shm__key__name = 'name'

    DEF_shm__key__system = 'system'
    DEF_shm__key__version = 'version'
    Key_Record = 'record'
    Key_Active = 'active'
    Key_Develop = 'develop'
    Key_Custom = 'custom'

    Key_Application = 'application'
    Key_Bin = 'bin'
    Key_Platform = 'platform'

    Key_App = 'app'

    Key_PythonVAR_kit__window__version = 'python_version'

    Key_Resource = 'resource'

    Key_Config = 'config'

    Key_Program = 'program'

    Key_Dependent = 'dependent'
    Key_Dependent_Module = 'dependent_module'
    Key_Dependent_Package = 'dependent_package'

    Key_Language = 'language'
    Key_Language_Name = 'language_name'
    Key_LanguageVAR_kit__window__version = 'language_version'

    Key_Module = 'module'
    Key_Plug = 'plug'

    Key_Python_Package = 'python_package'
    Key_Python_Module = 'python_module'

    Key_Resource_Source_Path = 'sourcepath'
    Key_Resource_Compile_Path = 'compilepath'

    DEF_key_plug_name = 'plugname'
    DEF_key_plug_version = 'plugversion'
    Key_Plug_App = 'plugapp'
    Key_Plug_Source_Path = 'plugpath'

    Key_Plug_Load_Name = 'loadname'
    Key_Plug_Module_Name = 'moduleName'

    Language_Python = 'python'

    Version_Default = '0.0.0'
    DEF_shm_keyword__version_active = 'active'
    DEF_shm_keyword__system_active = 'active'

    App_Maya = 'maya'

    Platform_Windows = 'windows'

    PythonVAR_kit__window__version_27 = '2.7'

    Key_Path = 'path'

    Key_Environ = 'environ'
    Key_Value = 'value'
    Key_Operate = 'operate'
    DEF_shm__keyword_index = 'index'

    Operation_Add = '+='
    Operation_Replace = '='

    DEF_shm__keyword__self = 'self'
    Attr_Key_Root = 'root'
    Attr_Key_Path = 'path'

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
        return ''

    @staticmethod
    def _createTimestampMethod(osPath, osJsonFile):
        isAscii = False
        timestampDic = bscMethods.OsDirectory.allFileTimestampDict(osPath)
        bscMethods.OsJsonFile.write(osJsonFile, timestampDic, ensure_ascii=isAscii)

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
        return [False, True][bscMethods.OsEnviron.get(bscCfg.BscUtility.DEF_util__environ_key__enable_develop, u'FALSE').lower() == u'true']

    @classmethod
    def isUsedef(cls):
        return [False, True][bscMethods.OsEnviron.get(bscCfg.BscUtility.DEF_util__environ_key__enable_usedef, u'FALSE').lower() == u'true']

    @classmethod
    def setUsedef(cls, boolean):
        bscMethods.OsEnviron.set(bscCfg.BscUtility.DEF_util__environ_key__enable_usedef, [u'FALSE', u'TRUE'][boolean])

    # noinspection PyMethodMayBeStatic
    def _jsonStrRaw(self):
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

        def addValueFnc_(raw_, lString, rString, rawtype=None):
            if raw_ is None:
                addNoneFnc_(lString=lString, rString='\r\n')

            elif isinstance(raw_, list) or isinstance(raw_, tuple):
                lString += defIndentString
                addListFnc_(raw_, lString=lString, rString=rString)

            elif isinstance(raw_, dict):
                lString += defIndentString
                addDictionaryFnc_(raw_, lString=lString, rString=rString)

            else:
                if rawtype == dict:
                    addMemberFnc_(raw_, lString='', rString=rString)
                else:
                    addMemberFnc_(raw_, lString=lString+defIndentString, rString=rString)

        def addListFnc_(raw_, lString, rString):
            if raw_:
                lis.append(u'{lString}[{rString}'.format(lString='', rString='\r\n'))

                c = len(raw_)
                for seq, i in enumerate(raw_):
                    if seq < c - 1:
                        addValueFnc_(i, lString=lString, rString=',\r\n', rawtype=list)
                    else:
                        addValueFnc_(i, lString=lString, rString='\r\n', rawtype=list)

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
                        addValueFnc_(v, lString=lString, rString=',\r\n', rawtype=dict)
                    else:
                        addValueFnc_(v, lString=lString, rString='\r\n', rawtype=dict)

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
        if self._jsonStrRaw():
            return self._toJsonStringMethod(self._jsonStrRaw())
        return ''


class ShmResourceCategory(object):
    pass


class ShmSystemArgument(object):
    # platform
    platform = [
        'share', 'share'
    ]
    platform__python_27 = [
        'share', 'share',
        'python', '2.7'
    ]
    platform__maya = [
        'share', 'share',
        'maya', 'share'
    ]
    platform__maya__python_27 = [
        'share', 'share',
        'maya', 'share',
        'python', '2.7'
    ]
    platform__maya_2019 = [
        'share', 'share',
        'maya', '2019'
    ]
    platform__houdini = [
        'share', 'share',
        'houdini', 'share'
    ]
    platform__houdini__python_27 = [
        'share', 'share',
        'houdini', 'share',
        'python', '2.7'
    ]
    platform__houdini_18 = [
        'share', 'share',
        'houdini', '18'
    ]
    # windows
    windows = [
        'windows', 'share'
    ]
    windows__python_27 = [
        'windows', 'share',
        'python', '2.7'
    ]
    windows__maya = [
        'windows', 'share',
        'maya', 'share'
    ]
    windows__maya_2019 = [
        'windows', 'share',
        'maya', '2019'
    ]
    windows__houdini = [
        'windows', 'share',
        'houdini', 'share'
    ]
    windows__houdini_18 = [
        'windows', 'share',
        'houdini', '18'
    ]
    # windows-x64
    windows_x64 = [
        'windows', 'x64'
    ]
    # linux
    linux = [
        'linux', 'share'
    ]
    linux__python_27 = [
        'linux', 'share',
        'python', '2.7'
    ]
    linux__houdini_18 = [
        'linux', 'share',
        'houdini', '18'
    ]
    # linux x64
    linux_x64 = [
        'linux', 'x64'
    ]
    linux_x64__python_27 = [
        'linux', 'x64',
        'python', '2.7'
    ]

    linux_x64__houdini = [
        'linux', 'x64',
        'houdini', 'share'
    ]
    linux_x64__houdini_18 = [
        'linux', 'x64',
        'houdini', '18'
    ]

    linux_x64__maya = [
        'linux', 'x64',
        'maya', 'share'
    ]
    linux_x64__maya_18 = [
        'linux', 'x64',
        'maya', '18'
    ]


class ShmRootDefaultKey(object):
    pass


class ShmRootDefaultValue(object):
    develop = bscCfg.BscUtility.DEF_util__root__default_develop
    product = bscCfg.BscUtility.DEF_util__root__default_product
    local = bscCfg.BscUtility.DEF_util__root__default_local
