# coding:utf-8
from LxBasic import bscObjects


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

    Category_Plf_Lan_Tool = 'plf-lan-tool'
    Category_Plf_App_Lan_Tool = 'plf-app-lan-tool'
    Category_Plf_App_Tool = 'plf-app-tool'

    Category_Project = 'project'

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

    Environ_Key_Scheme_Name = 'LYNXI_SCHEME_NAME'
    Environ_Key_Scheme_Version = 'LYNXI_SCHEME_VERSION'
    Environ_Key_Scheme_System = 'LYNXI_SCHEME_SYSTEM'

    Environ_Key_Enable_Develop = 'LYNXI_ENABLE_DEVELOP'
    Environ_Key_Path_Product = 'LYNXI_PATH_PRODUCT'

    Environ_Key_Path_Develop = 'LYNXI_PATH_DEVELOP'
    Environ_Key_Path_Local = 'LYNXI_PATH_LOCAL'

    Environ_Key_Path_Preset = 'LYNXI_PATH_PRESET'
    Environ_Key_Path_Toolkit = 'LYNXI_PATH_TOOLKIT'

    Environ_Key_Python_Bin_Path = 'LYNXI_BIN_PYTHON_PATH'

    Folder_Source = 'source'

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
    Key_Custom = 'custom'

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
        bscObjects.JsonFile(osJsonFile).write(timestampDic, ensure_ascii=isAscii)

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

        envData = bscObjects.Sys_Environ(cls.Environ_Key_Enable_Develop).value
        if envData:
            if envData.lower() == 'true':
                boolean = True
        return boolean

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
        if self._jsonStrRaw():
            return self._toJsonStringMethod(self._jsonStrRaw())
        return ''
