# coding:utf-8
from LxBasic import bscMethods

from LxScheme import shmCfg


class Abs_ShmObject(shmCfg.ShmUtility):
    def _initAbsShmObject(self, category, name):
        self._category = category
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, string):
        self._category = string

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, string):
        self._name = string

    def raw(self):
        return {
            self.DEF_shm__key__category: self._category,
            self.DEF_shm__key__name: self._name,
        }

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


# path
class Abs_ShmPath(shmCfg.ShmUtility):
    def _initAbsShmPath(self):
        pass

    def _shm__path__get_active_path_str_(self):
        pass

    @property
    def active(self):
        return self._shm__path__get_active_path_str_()

    def _shm__path__get_server_path_str_(self):
        pass

    @property
    def server(self):
        return self._shm__path__get_server_path_str_()

    def _shm__path__get_local_path_str_(self):
        pass

    @property
    def local(self):
        return self._shm__path__get_local_path_str_()

    def _shm__path__get_develop_path_str_(self):
        pass

    @property
    def develop(self):
        return self._shm__path__get_develop_path_str_()

    def _shm__path__get_product_path_str_(self):
        pass

    @property
    def product(self):
        return self._shm__path__get_product_path_str_()

    def _shm__path__get_workspace_path_str_(self):
        pass

    @property
    def workspace(self):
        return self._shm__path__get_workspace_path_str_()

    def _formatDict_(self):
        return {
            self.DEF_shm__keyword__self: self,
        }

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.Path_Key_Active, self.server),
                (self.Path_Key_Server, self.server),
                (self.Path_Key_Local, self.local),
                (self.Path_Key_Develop, self.develop),
                (self.Path_Key_Product, self.product)
            ]
        )

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


class Abs_ShmRoot(Abs_ShmPath):
    DEF_shm__root__key_develop = None
    DEF_shm__root__key_product = None
    DEF_shm__root__key_local = None

    DEF_util__root__default_develop = None
    DEF_util__root__default_product = None
    DEF_util__root__default_local = None

    def _initAbsShmRoot(self):
        pass

    def _shm__path__get_develop_path_str_(self):
        return bscMethods.OsEnviron.getAsPath(
            self.DEF_shm__root__key_develop,
            self.DEF_util__root__default_develop
        )

    def _shm__path__get_product_path_str_(self):
        return bscMethods.OsEnviron.getAsPath(
            self.DEF_shm__root__key_product,
            self.DEF_util__root__default_product
        )

    def _shm__path__get_local_path_str_(self):
        return bscMethods.OsEnviron.getAsPath(
            self.DEF_shm__root__key_local,
            self.DEF_util__root__default_local
        )


class Abs_ShmDirectory(Abs_ShmPath):
    CLS_shm__root = None

    def _initAbsShmDirectory(self, *args):
        self.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/{self.subpath}',
            self.Path_Key_Server: u'{self.root.server}/{self.subpath}',
            self.Path_Key_Local: u'{self.root.local}/{self.subpath}',
            self.Path_Key_Develop: u'{self.root.develop}/{self.subpath}',
            self.Path_Key_Product: u'{self.root.product}/{self.subpath}',
            self.Path_Key_Workspace: u'{self.root.workspace}/{self.subpath}'
        }

        self._root = self.CLS_shm__root()

        self._subPathString = self._toSubPathMethod(*args)
        self._subNameString = self._toSubNameMethod(*args)

        if args:
            self._baseName = args[-1]

    @property
    def root(self):
        return self._root

    @property
    def pathname(self):
        return self._subNameString

    @property
    def subpath(self):
        return self._subPathString

    @property
    def basename(self):
        return self._baseName

    def _shm__path__get_active_path_str_(self):
        return self.pathFormatString[self.Path_Key_Active].format(**self._formatDict_())

    def _shm__path__get_server_path_str_(self):
        return self.pathFormatString[self.Path_Key_Server].format(**self._formatDict_())

    def _shm__path__get_local_path_str_(self):
        return self.pathFormatString[self.Path_Key_Local].format(**self._formatDict_())

    def _shm__path__get_develop_path_str_(self):
        return self.pathFormatString[self.Path_Key_Develop].format(**self._formatDict_())

    def _shm__path__get_product_path_str_(self):
        return self.pathFormatString[self.Path_Key_Product].format(**self._formatDict_())

    def _shm__path__get_workspace_path_str_(self):
        return self.pathFormatString[self.Path_Key_Workspace].format(**self._formatDict_())


class Abs_ShmFile(shmCfg.ShmUtility):
    CLS_shm__directory = None
    CLS_shm__file = None

    def _initAbsShmFile(self, directoryArgs, baseName, ext):
        self.pathFormatString = {
            self.Path_Key_Active: u'{self.directory.active}/{self.basename}',
            self.Path_Key_Server: u'{self.directory.server}/{self.basename}',
            self.Path_Key_Local: u'{self.directory.local}/{self.basename}',
            self.Path_Key_Develop: u'{self.directory.develop}/{self.basename}',
            self.Path_Key_Product: u'{self.directory.product}/{self.basename}'
        }

        self._directory = self.CLS_shm__directory(*directoryArgs)

        self._baseName = u'{}{}'.format(baseName, ext)

    @classmethod
    def _readMethod(cls, filepathStr):
        return cls.CLS_shm__file(filepathStr).read()

    @classmethod
    def _writeMethod(cls, filepathStr, raw):
        cls.CLS_shm__file(filepathStr).write(raw)

    @property
    def root(self):
        return self._directory.root

    @property
    def directory(self):
        return self._directory

    @property
    def basename(self):
        return self._baseName

    def activeFile(self):
        return self.pathFormatString[self.Path_Key_Active].format(**self._formatDict_())

    def createActiveFile(self, raw):
        self._writeMethod(self.activeFile(), raw)

    def isActiveExist(self):
        return bscMethods.OsPath.isExist(self.activeFile())

    def activeFileRaw(self):
        if self.isActiveExist():
            return self._readMethod(self.activeFile())
        return {}

    @property
    def server_file(self):
        return self.pathFormatString[self.Path_Key_Server].format(
            **self._formatDict_()
        )

    def createServerFile(self, raw):
        self._writeMethod(self.server_file, raw)

    def isServerExist(self):
        return bscMethods.OsPath.isExist(self.server_file)

    def serverFileRaw(self):
        if self.isServerExist():
            return self._readMethod(self.server_file)
        return {}

    def localFile(self):
        return self.pathFormatString[self.Path_Key_Local].format(**self._formatDict_())

    def isLocalExist(self):
        return bscMethods.OsPath.isExist(self.localFile())

    def developFile(self):
        return self.pathFormatString[self.Path_Key_Develop].format(**self._formatDict_())

    def isDevelopExist(self):
        return bscMethods.OsPath.isExist(self.developFile())

    def productFile(self):
        return self.pathFormatString[self.Path_Key_Product].format(**self._formatDict_())

    def isProductExist(self):
        return bscMethods.OsPath.isExist(self.productFile())

    def _formatDict_(self):
        return {
            self.DEF_shm__keyword__self: self,
        }

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.Path_Key_Active, self.activeFile()),
                (self.Path_Key_Server, self.server_file),
                (self.Path_Key_Local, self.localFile()),
                (self.Path_Key_Develop, self.developFile()),
                (self.Path_Key_Product, self.productFile())
            ]
        )

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


# system
class Abs_ShmSystem(Abs_ShmObject):
    CLS_shm__system = None

    VAR_shm__system__category = None
    VAR_shm__system__raw_key = None

    def _initAbsShmSystem(self, *args):
        self._argument = args

        systemName, systemVersion = args[-2:]

        self._initAbsShmObject(
            self.VAR_shm__system__category, systemName
        )
        self._version = systemVersion

        if self.CLS_shm__system is not None:
            self._systemObj = self.CLS_shm__system(*args[:-2])

    def create(self, *args):
        """
        = self._initAbsShmSystem(*args)
        :param args:
            Platform: *(platformName, platformVersion);
            Platform-Language: *(platformName, platformVersion, languageName, languageVersion);
            Platform-Application: *(platformName, platformVersion, applicationName, applicationVersion);
            Platform-Application-Language: *(platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion).
        :return: None
        """
        self._initAbsShmSystem(*args)

    def _shm_system__set_build_(self, raw):
        pass

    def setVersion(self, string):
        self._version = string

    @property
    def version(self):
        return self._version

    @property
    def system(self):
        return self._systemObj

    @property
    def systemraw(self):
        return self.CLS_dic_order(
            [
                (self.DEF_shm__key__name, self.name),
                (self.DEF_shm__key__version, self.version)
            ]
        )

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.DEF_shm__key__category, self.category),
                (self.DEF_shm__key__name, self.name),
                (self.DEF_shm__key__version, self.version)
            ]
        )

    def argument(self):
        return self._argument

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


class Abs_ShmRaw(shmCfg.ShmUtility):
    def _initAbsShmRaw(self, raw, defRaw):
        if raw is not None:
            self._raw = raw
        else:
            self._raw = defRaw

    def create(self, raw):
        self._raw = raw

    def get(self, key):
        if key in self._raw:
            return self._raw[key]

    def set(self, key, value):
        self._raw[key] = value

    def add(self, key, value):
        self._raw[key] = value

    def raw(self):
        return self._raw

    def hasRaw(self):
        return self._raw != {}

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


class Abs_ShmConfigure(Abs_ShmRaw):
    def _initAbsShmConfigure(self, enable, category, name):
        self.create(
            self.CLS_dic_order(
                [
                    (self.DEF_shm__key__enable, enable),
                    (self.DEF_shm__key__category, category),
                    (self.DEF_shm__key__name, name)
                ]
            )
        )

        self._rawObjDic = self.CLS_dic_order()

    def addRaw(self, key, value):
        self._rawObjDic[key] = value

    def raw(self):
        dic = self._raw
        for keyStr, rawObj in self._rawObjDic.items():
            dic[keyStr] = rawObj.raw()
        return dic

    @property
    def enable(self):
        return self._raw[self.DEF_shm__key__enable]

    @property
    def category(self):
        return self._raw[self.DEF_shm__key__category]

    @property
    def name(self):
        return self._raw[self.DEF_shm__key__name]


class Abs_ShmResource(Abs_ShmObject):
    CLS_shm__resource_system = None
    CLS_shm__resource_file = None
    CLS_shm__resource_raw = None
    CLS_shm__resource_operate = None

    VAR_shm__resource__category = None

    def _initAbsShmResource(self, *args):
        _ = args[0]
        if isinstance(_, (str, unicode)):
            # Object
            categoryStr = self.VAR_shm__resource__category
            nameStr = args[0]
            self._initAbsShmObject(
                categoryStr, nameStr
            )
            # Bin
            sysRaw = args[1:]
            self._systemObj = self.CLS_shm__resource_system(*sysRaw)

            self._enable = True
            # Config
            self._rawObj = self.CLS_shm__resource_raw(
                True, categoryStr, nameStr,
                self._systemObj
            )
            # File
            pathArgs = list(self._systemObj.argument())
            pathArgs.append(nameStr.lower())
            fileArgs = [i for i in pathArgs if not i == self.DEF_shm__keyword__share] or [self.DEF_shm__keyword__share]
            self._fileObj = self.CLS_shm__resource_file(*fileArgs)
            # Raw
            self._versionObj = self._rawObj.version
            self._environObj = self._rawObj.environ
            self._dependentObj = self._rawObj.dependent
            # init
            self._loadCache()

    def _loadCache(self):
        serverRaw = self.file.serverFileRaw()
        if serverRaw:
            if self.isUsedef() is False:
                self.version.create(serverRaw[self.DEF_shm__key__version])
                self.environ.create(serverRaw[self.Key_Environ])
                self.dependent.create(serverRaw[self.Key_Dependent])

        self._raw = self._rawObj.raw()

    def _getModuleVersion(self):
        module = bscMethods.PyLoader.load(self.name)
        if module:
            if hasattr(module, '__version__'):
                return module.__version__
        return self.Version_Default

    def create(self, *args):
        pass

    @property
    def is_bin(self):
        return self.category in self.Category_Bin_Lis

    @property
    def is_package(self):
        return self.category in self.Category_Package_Lis

    @property
    def is_module(self):
        return self.category in self.Category_Module_Lis

    @property
    def is_plug(self):
        return self.category in self.Category_Plug_Lis

    @property
    def is_scheme(self):
        return self.category in self.Category_Scheme_Lis

    @property
    def path(self):
        return self._fileObj.directory

    @property
    def file(self):
        return self._fileObj

    @property
    def enable(self):
        return self._rawObj.enable

    @property
    def system(self):
        return self._systemObj

    @property
    def version(self):
        return self._versionObj

    @property
    def config(self):
        return self._rawObj

    @version.setter
    def version(self, version):
        self._versionObj = version

    @property
    def environ(self):
        return self._environObj

    @environ.setter
    def environ(self, environ):
        self._environObj = environ

    @property
    def dependent(self):
        return self._dependentObj

    @dependent.setter
    def dependent(self, dependent):
        self._dependentObj = dependent

    def raw(self):
        return self._rawObj

    def operateAt(self, version=None):
        if self.is_module:
            if version is None:
                version = self._getModuleVersion()

        return self.CLS_shm__resource_operate(self, version)

    def createServerConfigFile(self):
        self.file.createServerFile(
            self.config.raw()
        )
        #
        bscMethods.PyMessage.traceResult(
            u'save file "{}"'.format(self.file.server_file)
        )

    def createDevelopDirectories(self):
        for i in self.version.record:
            rscOpObj = self.operateAt(i)
            rscOpObj.createDevelopDirectory()

    def createDevelopSourceDirectories(self):
        for i in self.version.record:
            rscOpObj = self.operateAt(i)
            rscOpObj.createDevelopSourceDirectory()

    def createResource(self, version):
        pass

    @property
    def workspace_source_directory(self):
        return u'{}/{}'.format(self.path.workspace, self.name)

    def createWorkspaceSourceDirectory(self):
        bscMethods.OsDirectory.create(self.workspace_source_directory, trace=True)

    def __str__(self):
        return self._toJsonStringMethod(self.config.raw())

    def __repr__(self):
        return self.__str__()


class Abs_ShmRscOperate(shmCfg.ShmUtility):
    VAR_shm__rsc_op__rsc_cls_dict = {}
    VAR_shm__rsc_op__rsc_sys_args_format_dict = {}

    def _initAbsShmRscOperate(self, *args):
        resourceObj, versionStr = args
        # copy
        self._resourceObj = self.MOD_copy.deepcopy(resourceObj)
        self._versionStr = versionStr

        self._shm__rsc_op__set_environ_raw_convert_()

    def _shm__rsc_op__set_environ_value_convert_(self, value):
        value = value.format(
            **self._formatDict_()
        )
        value = value.replace(
            self.root.active, u'{root.active}'
        )
        if self.resource.is_module:
            value = u'{}|'.format(
                self._shm__rsc_op__get_workspace_path_str_().replace(self.root.active, u'{root.active}')
            ) + value
        return u'<{}>{}'.format(self.name, value)

    def _shm__rsc_op__set_environ_raw_convert_(self):
        raw_ = self.environ.raw()
        if raw_:
            for k, v in raw_.items():
                _ = v[self.Key_Value]
                if isinstance(_, (tuple, list)):
                    value = [self._shm__rsc_op__set_environ_value_convert_(i) for i in _]
                else:
                    value = self._shm__rsc_op__set_environ_value_convert_(_)

                v[self.Key_Value] = value

    def _getChangedSourceFiles(self):
        return self._getChangedFileMethod(
            self._shm__rsc_op__get_server_timestamp_dict_(), self._shm__rsc_op__get_local_timestamp_dict_()
        )

    @property
    def resource(self):
        return self._resourceObj

    @property
    def root(self):
        return self.resource.file.root

    @property
    def path(self):
        return self.resource.file.directory

    @property
    def category(self):
        return self.resource.category

    @property
    def name(self):
        return self.resource.name

    @property
    def system(self):
        return self.resource.system

    @property
    def file(self):
        return self.resource.file

    @property
    def version(self):
        return self._versionStr

    @property
    def environ(self):
        return self.resource.environ

    @property
    def dependent(self):
        return self.resource.dependent

    @property
    def sourcepath(self):
        return self.active_source_directory

    @property
    def develop_setup_json_filepath(self):
        return u'{}/{}/{}'.format(
            self.develop_source_directory, self.name,
            u'setup.json'
        )

    @property
    def workspace_setup_json_filepath(self):
        return u'{}/{}'.format(
            self.workspace_source_directory,
            u'setup.json'
        )

    @property
    def workspace_setup_shell_filepath(self):
        if bscMethods.LinuxPlatform.isActive():
            return u'{}/{}'.format(
                self.workspace_source_directory,
                u'setup.sh'
            )
        elif bscMethods.WindowsPlatform.isActive():
            return u'{}/{}'.format(
                self.workspace_source_directory,
                u'setup.bat'
            )
        raise ()

    def _shm__rsc_op__get_active_path_str_(self):
        return u'{}/{}'.format(
            self.path._shm__path__get_active_path_str_(),
            self.version
        )

    @property
    def active_source_directory(self):
        return u'{}/{}'.format(
            self._shm__rsc_op__get_active_path_str_(),
            self.DEF_shm__folder__source
        )

    def _shm__rsc_op__get_server_path_str_(self):
        return u'{}/{}'.format(
            self.path.server,
            self.version
        )

    @property
    def server_source_directory(self):
        return u'{}/{}'.format(
            self._shm__rsc_op__get_server_path_str_(),
            self.DEF_shm__folder__source
        )

    def _shm__rsc_op__get_local_path_str_(self):
        return u'{}/{}'.format(
            self.path.local,
            self.version
        )

    @property
    def local_source_directory(self):
        return u'{}/{}'.format(
            self._shm__rsc_op__get_local_path_str_(),
            self.DEF_shm__folder__source
        )

    def _shm__rsc_op__get_develop_path_str_(self):
        return u'{}/{}'.format(self.path.develop, self.version)

    @property
    def develop_source_directory(self):
        return u'{}/{}'.format(
            self._shm__rsc_op__get_develop_path_str_(),
            self.DEF_shm__folder__source
        )

    def _shm__rsc_op__get_product_path_str_(self):
        return u'{}/{}'.format(self.path.product, self.version)

    @property
    def product_source_directory(self):
        return u'{}/{}'.format(
            self._shm__rsc_op__get_product_path_str_(),
            self.DEF_shm__folder__source
        )

    @property
    def workspace_source_directory(self):
        return self.resource.workspace_source_directory

    def _shm__rsc_op__get_workspace_path_str_(self):
        return self.path._shm__path__get_workspace_path_str_()

    def createDevelopSetupJsonFile(self):
        fileStr = self.develop_setup_json_filepath
        self.file._writeMethod(
            fileStr,
            self._shm__rsc_op__get_setup_raw_()
        )
        bscMethods.PyMessage.traceResult(
            u'save file "{}"'.format(fileStr)
        )

    def _shm__rsc_op__get_setup_raw_(self):
        return self.CLS_dic_order(
                [
                    (self.DEF_shm__key__name, self.name),
                    (self.DEF_shm__key__version, self.version),
                    (self.Key_User, bscMethods.OsPlatform.username()),
                    (self.Key_Timestamp, bscMethods.OsPlatform.activeTimestamp()),
                    (self.Key_Environ, self._shm__rsc_op__get_setup_environ_raw_()),
                    (self.Key_Module, self._shm__rsc_op__get_setup_module_name_str_list_()),
                    (self.Key_Plug, self._shm__rsc_op__get_setup_plug_name_str_list_())
                ]
            )

    def createWorkspaceSetupJsonFile(self):
        fileStr = self.workspace_setup_json_filepath
        self.file._writeMethod(
            fileStr,
            self._shm__rsc_op__get_setup_raw_()
        )
        bscMethods.PyMessage.traceResult(
            u'save file "{}"'.format(fileStr)
        )

    def createWorkspaceSetupShellFile(self):
        pass

    def createDevelopDirectory(self):
        bscMethods.OsDirectory.create(self._shm__rsc_op__get_develop_path_str_())

    def createDevelopSourceDirectory(self):
        directoryStr = self.develop_source_directory
        if bscMethods.OsDirectory.isExist(directoryStr) is False:
            bscMethods.OsDirectory.create(
                directoryStr
            )
            bscMethods.PyMessage.traceResult(
                u'create directory "{}"'.format(directoryStr)
            )

    @property
    def server_timestamp_filepath(self):
        return u'{}/source.timestamp.json'.format(
            self._shm__rsc_op__get_server_path_str_()
        )

    def createServerTimestamp(self):
        self._createTimestampMethod(
            self.server_source_directory, self.server_timestamp_filepath
        )

    def _shm__rsc_op__get_server_timestamp_dict_(self):
        if bscMethods.OsPath.isExist(self.server_timestamp_filepath) is False:
            self.createServerTimestamp()
        return bscMethods.OsJsonFile.read(self.server_timestamp_filepath) or {}

    @property
    def local_timestamp_file(self):
        return u'{}/source.timestamp.json'.format(
            self._shm__rsc_op__get_local_path_str_()
        )

    def createLocalTimestamp(self):
        self._createTimestampMethod(
            self.local_source_directory, self.local_timestamp_file
        )

    def _shm__rsc_op__get_local_timestamp_dict_(self):
        if bscMethods.OsPath.isExist(self.local_timestamp_file) is False:
            self.createLocalTimestamp()
        return bscMethods.OsJsonFile.read(self.local_timestamp_file) or {}

    def localizationSource(self):
        changedFileLis = self._getChangedSourceFiles()
        if changedFileLis:
            for relativeOsFile in changedFileLis:
                sourceFile = self.server_source_directory + relativeOsFile
                targetFile = self.local_source_directory + relativeOsFile

                bscMethods.OsFile.copyTo(sourceFile, targetFile, force=False)

                traceMessage = u'Localization Resource "{}" : "{}" > "{}"'.format(
                    self.name, sourceFile, targetFile
                )
                bscMethods.PyMessage.traceResult(traceMessage)

                bscMethods.OsFile.copyTo(self.server_timestamp_filepath, self.local_timestamp_file)
        else:
            traceMessage = u'Resource "{}"  is "Non - Changed"'.format(self.name)
            bscMethods.PyMessage.traceResult(traceMessage)

    def environCommands(self):
        lis = []

        raw_ = self.environ.raw()
        if raw_:
            for k, v in raw_.items():
                value = v[self.Key_Value]
                operate = v[self.Key_Operate]
                if operate == '+':
                    operate = '+='
                if isinstance(value, tuple) or isinstance(value, list):
                    for i in value:
                        command = u'os.environ["{}"] {} "{};"'.format(k, operate, i)

                        lis.append(command)
                else:
                    command = u'os.environ["{}"] {} "{};"'.format(k, operate, value)

                    lis.append(command)

        return lis

    def hasDependents(self):
        return self.resource.dependent.hasRaw()

    def _shm__rsc_op__get_rsc_cls_(self, categoryStr):
        if categoryStr in self.VAR_shm__rsc_op__rsc_cls_dict:
            return self.VAR_shm__rsc_op__rsc_cls_dict[categoryStr]
        raise

    def _shm__rsc_op__get_rsc_sys_arg_format_list_(self, categoryStr):
        if categoryStr in self.VAR_shm__rsc_op__rsc_sys_args_format_dict:
            return self.VAR_shm__rsc_op__rsc_sys_args_format_dict[categoryStr]
        raise

    @classmethod
    def _shm__rsc_op_cls__get_arg_extend_(cls, args):
        _lis = []
        for i in args:
            if i == cls.DEF_shm__keyword__share:
                _lis.append([cls.DEF_shm__keyword__share])
            else:
                _lis.append([cls.DEF_shm__keyword__share, i])
        return bscMethods.NestedArray.mapTo(_lis)

    def _shm__rsc_op__get_dependent_obj_list_(self):
        def findRscObjFnc_(baseRscOpObj_, rscNameStr_, rscRaw_):
            _categoryStr = rscRaw_[self.DEF_shm__key__category]
            _systemRaw = rscRaw_[self.DEF_shm__key__system]
            _versionStr = rscRaw_[self.DEF_shm__key__version]
            _rscCls = self._shm__rsc_op__get_rsc_cls_(_categoryStr)
            _rscSysArgs = []

            _rscSysArgFormatList = self.MOD_copy.deepcopy(
                self._shm__rsc_op__get_rsc_sys_arg_format_list_(_categoryStr)
            )

            # override
            if isinstance(_systemRaw, dict):
                for _ik, _iv in _systemRaw.items():
                    if _ik in _rscSysArgFormatList:
                        index = _rscSysArgFormatList.index(_ik)
                        _rscSysArgFormatList[index] = _iv
            # format argument
            for i in _rscSysArgFormatList:
                i = i.format(**baseRscOpObj_._formatDict_())
                _rscSysArgs.append(i)

            _subRscSysArgsList = self._shm__rsc_op_cls__get_arg_extend_(_rscSysArgs)
            for _subRscSysArgs in _subRscSysArgsList:
                _rscObj = _rscCls(rscNameStr_, *_subRscSysArgs)
                if _rscObj.file.isServerExist():
                    return _rscObj

        def rcsFnc_(baseRscOpObj_, rscOpObj_):
            _dependentRaw = rscOpObj_.dependent.raw()
            if _dependentRaw:
                for k, v in _dependentRaw.items():
                    _versionStr = v[self.DEF_shm__key__version]

                    # resource object
                    _rscObj = findRscObjFnc_(baseRscOpObj_, k, v)
                    if _rscObj is not None:
                        if _versionStr == self.DEF_shm_keyword__version_active:
                            _versionStr = _rscObj.version.active
                        # operate object
                        _rscOpObj = _rscObj.operateAt(_versionStr)
                        addFnc_(_rscOpObj)
                        rcsFnc_(baseRscOpObj_, _rscOpObj)
                    else:
                        bscMethods.PyMessage.traceWarning(
                            u'dependent resource name: "{}" is not found.'.format(k)
                        )

        def addFnc_(rscOpObj_):
            _nameStr = rscOpObj_.name
            if not _nameStr in nameLis:
                nameLis.append(_nameStr)
                lis.append(rscOpObj_)

        nameLis = [self.name]

        lis = [self]

        rcsFnc_(self, self)

        return lis

    def dependents(self):
        return self._shm__rsc_op__get_dependent_obj_list_()

    def dependentSourcePathStrings(self):
        lis = []

        resourceOpObjList = self.dependents()
        for i in resourceOpObjList:
            lis.append(i.sourcepath)

        return lis

    def _shm__rsc_op__get_setup_environ_raw_(self):
        resourceOpObjList = self.dependents()

        environ = resourceOpObjList[0].environ
        if len(resourceOpObjList) > 1:
            if resourceOpObjList[1:]:
                for i in resourceOpObjList:
                    environ += i.environ

        return environ.raw()

    def _shm__rsc_op__get_setup_module_name_str_list_(self):
        lis = []

        resourceOpObjList = self.dependents()
        for i in resourceOpObjList:
            if i.resource.is_module:
                lis.append(i.name)
        if lis:
            lis.sort()
        return lis

    def _shm__rsc_op__get_setup_plug_name_str_list_(self):
        lis = []

        resourceOpObjList = self.dependents()
        for i in resourceOpObjList:
            if i.resource.is_plug:
                lis.append(i.name)
        if lis:
            lis.sort()
        return lis

    def _formatDict_(self):
        return {
            self.DEF_shm__keyword__self: self,
            self.DEF_shm__key__system: self.system
        }

    def pushWorkspaceSourceToDevelop(self):
        if self.resource.is_module or self.resource.is_scheme:
            sourcePathStr = self.workspace_source_directory
            targetPathStr = self.develop_source_directory

            relativeOsFileLis = bscMethods.OsDirectory.allFileRelativenames(
                sourcePathStr,
                extString=['.py', '.xml', '.shelf', '.hda', 'json', '.sh']
            )
            if relativeOsFileLis:
                bscMethods.OsDirectory.remove(targetPathStr)
                for i in relativeOsFileLis:
                    workspacePyFile = u'{}/{}'.format(sourcePathStr, i)
                    developPyFile = u'{}/{}/{}'.format(targetPathStr, self.name, i)
                    bscMethods.OsFile.copyTo(workspacePyFile, developPyFile)

                bscMethods.PyMessage.traceResult(
                    u'push {}: "{}" to develop;'.format(self.category, self.name)
                )
                bscMethods.PyMessage.traceResult(
                    u'"{}" > "{}".'.format(self.workspace_source_directory, self.develop_source_directory)
                )

    def pushWorkspaceSourceToServer(self, *args):
        if self.resource.is_module or self.resource.is_scheme:
            sourcePathStr = self.workspace_source_directory
            targetPathStr = self.server_source_directory
            if args:
                targetPathStr = args[0] + targetPathStr[len(self.root.server):]

            relativeOsFileLis = bscMethods.OsDirectory.allFileRelativenames(
                sourcePathStr,
                extString=['.py', '.xml', '.shelf', '.hda', '.json', '.sh']
            )
            if relativeOsFileLis:
                bscMethods.OsDirectory.remove(targetPathStr)
                for i in relativeOsFileLis:
                    sourceFile = u'{}/{}'.format(sourcePathStr, i)
                    targetFile = u'{}/{}/{}'.format(targetPathStr, self.name, i)
                    # print sourceFile, targetFile
                    bscMethods.OsFile.copyTo(sourceFile, targetFile)

    def setup(self):
        pass

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.DEF_shm__key__category, self.category),
                (self.DEF_shm__key__name, self.name),
                (self.DEF_shm__key__version, self.version),
                (self.DEF_shm__key__system, self.system.raw())
            ]
        )

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


class Abs_ShmRscBuilder(shmCfg.ShmUtility):
    VAR_shm__rsc__system_dict = {}
    VAR_shm__rsc__class_dict = {}
    VAR_shm__rsc__version_dict = {}
    VAR_shm__rsc__environ_dict = {}
    VAR_shm__rsc__dependent_dict = {}

    def _initAbsShmRscBuilder(self, *args):
        self._shm_rsc_builder__set_builder_()

    def _shm_rsc_builder__set_builder_(self):
        self._resourceObjList = []

        for k, v in self.VAR_shm__rsc__system_dict.items():
            categoryStr = v[self.DEF_shm__key__category]
            name = v[self.DEF_shm__key__name]
            argument = v[self.DEF_shm__key__system]
            rscCls = self.VAR_shm__rsc__class_dict[categoryStr]

            rscObj = rscCls(name, *argument)
            if k in self.VAR_shm__rsc__version_dict:
                rscObj.version.create(self.VAR_shm__rsc__version_dict[k])

            if k in self.VAR_shm__rsc__environ_dict:
                rscObj.environ.create(self.VAR_shm__rsc__environ_dict[k])

            if k in self.VAR_shm__rsc__dependent_dict:
                rscObj.dependent.create(self.VAR_shm__rsc__dependent_dict[k])

            self._resourceObjList.append(rscObj)

    def resources(self):
        return self._resourceObjList

    def bins(self):
        lis = []
        for i in self.resources():
            if i.is_bin:
                lis.append(i)
        return lis

    def schemes(self):
        lis = []
        for i in self.resources():
            if i.is_scheme:
                lis.append(i)
        return lis

    def modules(self):
        lis = []
        for i in self.resources():
            if i.is_module:
                lis.append(i)
        return lis

    def packages(self):
        lis = []
        for i in self.resources():
            if i.is_package:
                lis.append(i)
        return lis

    def plugs(self):
        lis = []
        for i in self.resources():
            if i.is_plug:
                lis.append(i)
        return lis

    def createDefConfigCaches(self):
        if self.resources():
            for i in self.resources():
                i.createServerConfigFile()

    def createDefDevelopDirectories(self):
        if self.resources():
            for i in self.resources():
                i.createDevelopDirectories()

    def createDevelopSourceDirectories(self):
        if self.resources():
            for i in self.resources():
                i.createDevelopSourceDirectories()
