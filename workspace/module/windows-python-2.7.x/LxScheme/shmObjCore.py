# coding:utf-8
from LxBasic import bscMethods

from LxScheme import shmConfigure


class Abc_ShmObject(shmConfigure.Utility):
    def _initAbcShmObject(self, category, name):
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
            self.Key_Category: self._category,
            self.DEF_key_name: self._name,
        }

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


class Abc_ShmPath(shmConfigure.Utility):
    def _initAbcShmPath(self):
        pass

    @property
    def active(self):
        return self._activePath()

    @property
    def server(self):
        return self._serverPath()

    @property
    def local(self):
        return self._localPath()

    @property
    def develop(self):
        return self._developPath()

    @property
    def product(self):
        return self._productPath()

    @property
    def workspace(self):
        return self._workspacePath()

    def _activePath(self):
        pass

    def _serverPath(self):
        pass

    def _localPath(self):
        pass

    def _developPath(self):
        pass

    def _productPath(self):
        pass

    def _workspacePath(self):
        pass

    def _formatDict_(self):
        return {
            self.Attr_Key_Self: self,
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


class Abc_ShmRoot(Abc_ShmPath):
    DEF_environ_key_develop = None
    DEF_environ_key_product = None
    DEF_environ_key_local = None

    VAR_path_default_develop = None
    VAR_path_default_product = None
    VAR_path_default_local = None

    def _initAbcShmRoot(self):
        pass

    def _developPath(self):
        return bscMethods.OsEnviron.getAsPath(
            self.DEF_environ_key_develop,
            self.VAR_path_default_develop
        )

    def _productPath(self):
        return bscMethods.OsEnviron.getAsPath(
            self.DEF_environ_key_product,
            self.VAR_path_default_product
        )

    def _localPath(self):
        return bscMethods.OsEnviron.getAsPath(
            self.DEF_environ_key_local,
            self.VAR_path_default_local
        )


class Abc_ShmDirectory(Abc_ShmPath):
    CLS_shm_root = None

    def _initAbcShmDirectory(self, *args):
        self.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/{self.subpath}',
            self.Path_Key_Server: u'{self.root.server}/{self.subpath}',
            self.Path_Key_Local: u'{self.root.local}/{self.subpath}',
            self.Path_Key_Develop: u'{self.root.develop}/{self.subpath}',
            self.Path_Key_Product: u'{self.root.product}/{self.subpath}',
            self.Path_Key_Workspace: u'{self.root.workspace}/{self.subpath}'
        }

        self._root = self.CLS_shm_root()

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

    def _activePath(self):
        return self.pathFormatString[self.Path_Key_Active].format(**self._formatDict_())

    def _serverPath(self):
        return self.pathFormatString[self.Path_Key_Server].format(**self._formatDict_())

    def _localPath(self):
        return self.pathFormatString[self.Path_Key_Local].format(**self._formatDict_())

    def _developPath(self):
        return self.pathFormatString[self.Path_Key_Develop].format(**self._formatDict_())

    def _productPath(self):
        return self.pathFormatString[self.Path_Key_Product].format(**self._formatDict_())

    def _workspacePath(self):
        return self.pathFormatString[self.Path_Key_Workspace].format(**self._formatDict_())


class Abc_ShmFile(shmConfigure.Utility):
    CLS_shm_directory = None
    CLS_shm_file = None

    def _initAbcShmFile(self, directoryArgs, baseName, ext):
        self.pathFormatString = {
            self.Path_Key_Active: u'{self.directory.active}/{self.basename}',
            self.Path_Key_Server: u'{self.directory.server}/{self.basename}',
            self.Path_Key_Local: u'{self.directory.local}/{self.basename}',
            self.Path_Key_Develop: u'{self.directory.develop}/{self.basename}',
            self.Path_Key_Product: u'{self.directory.product}/{self.basename}'
        }

        self._directory = self.CLS_shm_directory(*directoryArgs)

        self._baseName = u'{}{}'.format(baseName, ext)

    @classmethod
    def _readMethod(cls, fileString):
        return cls.CLS_shm_file(fileString).read()

    @classmethod
    def _writeMethod(cls, fileString, raw):
        cls.CLS_shm_file(fileString).write(raw)

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

    def serverFile(self):
        return self.pathFormatString[self.Path_Key_Server].format(**self._formatDict_())

    def createServerFile(self, raw):
        self._writeMethod(self.serverFile(), raw)

    def isServerExist(self):
        return bscMethods.OsPath.isExist(self.serverFile())

    def serverFileRaw(self):
        if self.isServerExist():
            return self._readMethod(self.serverFile())
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
            self.Attr_Key_Self: self,
        }

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.Path_Key_Active, self.activeFile()),
                (self.Path_Key_Server, self.serverFile()),
                (self.Path_Key_Local, self.localFile()),
                (self.Path_Key_Develop, self.developFile()),
                (self.Path_Key_Product, self.productFile())
            ]
        )

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


class Abc_ShmSystem(Abc_ShmObject):
    CLS_shm_system = None

    VAR_shm_object_category = None
    VAR_shm_raw_key = None

    def _initAbcShmSystem(self, *args):
        self._argument = args

        systemName, systemVersion = args[-2:]

        self._initAbcShmObject(
            self.VAR_shm_object_category, systemName
        )
        self._version = systemVersion

        if self.CLS_shm_system is not None:
            self._systemObj = self.CLS_shm_system(*args[:-2])

    def create(self, *args):
        """
        = self._initAbcShmSystem(*args)
        :param args:
            Platform: *(platformName, platformVersion);
            Platform-Language: *(platformName, platformVersion, languageName, languageVersion);
            Platform-Application: *(platformName, platformVersion, applicationName, applicationVersion);
            Platform-Application-Language: *(platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion).
        :return: None
        """
        self._initAbcShmSystem(*args)

    def createByRaw(self, raw):
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
                (self.DEF_key_name, self.name),
                (self.Key_Version, self.version)
            ]
        )

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.Key_Category, self.category),
                (self.DEF_key_name, self.name),
                (self.Key_Version, self.version)
            ]
        )

    def argument(self):
        return self._argument

    def __str__(self):
        return self._toJsonStringMethod(self.raw())


class Abc_ShmRaw(shmConfigure.Utility):
    def _initAbcShmRaw(self, raw, defRaw):
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


class Abc_ShmConfigure(Abc_ShmRaw):
    def _initAbcShmConfigure(self, enable, category, name):
        self.create(
            self.CLS_dic_order(
                [
                    (self.Key_Enable, enable),
                    (self.Key_Category, category),
                    (self.DEF_key_name, name)
                ]
            )
        )

        self._rawObjDic = self.CLS_dic_order()

    def addRaw(self, key, value):
        self._rawObjDic[key] = value

    def raw(self):
        dic = self._raw
        for k, v in self._rawObjDic.items():
            dic[k] = v.raw()
        return dic


class Abc_ShmResource(Abc_ShmObject):
    CLS_shm_system = None
    CLS_shm_file = None
    CLS_shm_raw = None
    CLS_shm_operate = None

    VAR_shm_object_category = None

    def _initAbcShmResource(self, *args):
        """
        :param args:
        :return:
        """
        # Object
        resourceName = args[0]
        self._initAbcShmObject(
            self.VAR_shm_object_category, resourceName
        )
        # Bin
        self._argument = args[1:]
        self._systemObj = self.CLS_shm_system(*self._argument)

        self._enable = True
        # Config
        self._rawObj = self.CLS_shm_raw(
            True, self.VAR_shm_object_category, resourceName,
            self._systemObj
        )
        # File
        args_ = list(self._systemObj.argument())
        args_.append(resourceName.lower())
        fileArgs = [i for i in args_ if not i == self.Keyword_Share]
        self._fileObj = self.CLS_shm_file(*fileArgs)
        # Raw
        self._version = self._rawObj.version
        self._environ = self._rawObj.environ
        self._dependent = self._rawObj.dependent
        # init
        self._loadCache()

    def _loadCache(self):
        serverRaw = self.file.serverFileRaw()
        if serverRaw:
            if self.isUsedef() is False:
                self.version.create(serverRaw[self.Key_Version])
                self.environ.create(serverRaw[self.Key_Environ])
                self.dependent.create(serverRaw[self.Key_Dependent])

        self._raw = self._rawObj.raw()

    def _getModuleVersion(self):
        module = bscMethods.PyLoader.reload(self.name)
        if module:
            if hasattr(module, '__version__'):
                return module.__version__
        return self.Version_Default

    def create(self, *args):
        pass

    @property
    def isPackage(self):
        return self.category in self.Category_Package_Lis

    @property
    def isModule(self):
        return self.category in self.Category_Module_Lis

    @property
    def isPlug(self):
        return self.category in self.Category_Plug_Lis

    @property
    def isScheme(self):
        return self.category in self.Category_Scheme_Lis

    @property
    def path(self):
        return self._fileObj.directory

    @property
    def file(self):
        return self._fileObj

    @property
    def argument(self):
        return self._argument

    @property
    def enable(self):
        return self._enable

    @property
    def system(self):
        return self._systemObj

    @property
    def version(self):
        return self._version

    @property
    def config(self):
        return self._rawObj

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def environ(self):
        return self._environ

    @environ.setter
    def environ(self, environ):
        self._environ = environ

    @property
    def dependent(self):
        return self._dependent

    @dependent.setter
    def dependent(self, dependent):
        self._dependent = dependent

    def raw(self):
        return self._rawObj

    def operateAt(self, version=None):
        if self.isModule:
            if version is None:
                version = self._getModuleVersion()

        return self.CLS_shm_operate(self, version)

    def createServerCache(self):
        self.file.createServerFile(self.config.raw())

    def createDevelopDirectories(self):
        for i in self.version.record:
            resource = self.operateAt(i)
            resource.createDevelopDirectory()

    def createDevelopSourceDirectories(self):
        for i in self.version.record:
            resource = self.operateAt(i)
            resource.createDevelopSourceDirectory()

    def createResource(self, version):
        pass

    def workspaceSourceDirectory(self):
        return u'{}/{}'.format(self.path.workspace, self.name)

    def __str__(self):
        return self._toJsonStringMethod(self.config.raw())

    def __repr__(self):
        return self.__str__()


class Abc_ShmPreset(shmConfigure.Utility):
    CLS_shm_system = None
    CLS_shm_file = None
    CLS_shm_raw = None
    CLS_shm_operate = None

    VAR_shm_object_category = None

    def _initAbcShmPreset(self, *args):
        """
        :param args:
        :return:
        """
        # Object
        presetName = args[0]
        # Bin
        self._argument = args[1:]

        self._enable = True
        # Raw
        self._rawObj = self.CLS_shm_raw(
            True, self.VAR_shm_object_category, presetName,
        )
        # File
        self._fileObj = self.CLS_shm_file(presetName)
        # init
        self._loadCache()

    @property
    def file(self):
        return self._fileObj

    @property
    def raw(self):
        return self._rawObj

    def _loadCache(self):
        pass

    def __str__(self):
        return self._toJsonStringMethod(self.raw.raw())


class Abc_ShmOperate(shmConfigure.Utility):
    _cls_dic = {}
    _argument_dic = {}

    def _initAbcShmOperate(self, resource, version):
        self._resourceObj = resource
        self._version = version

        self.__covertEnvironRaw()

    def __covertEnvironValue(self, value):
        value = value.format(**self._formatDict_())
        value = value.replace(self.root.active, '{root.active}')
        if self.resource.isModule:
            value = '{}|'.format(self._workspacePath().replace(self.root.active, '{root.active}')) + value
        return '{}:{}'.format(self.name, value)

    def __covertEnvironRaw(self):
        raw_ = self.environ.raw()
        if raw_:
            for k, v in raw_.items():
                value = v[self.Key_Value]
                if isinstance(value, tuple) or isinstance(value, list):
                    value = [self.__covertEnvironValue(i) for i in value]
                else:
                    value = self.__covertEnvironValue(value)

                v[self.Key_Value] = value

    def _getChangedSourceFiles(self):
        return self._getChangedFileMethod(
            self.serverTimestampDatum(), self.localTimestampDatum()
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
        return self._version

    @property
    def environ(self):
        return self.resource.environ

    @property
    def dependent(self):
        return self.resource.dependent

    @property
    def sourcepath(self):
        return self.activeSourceDirectory()

    def _activePath(self):
        return u'{}/{}'.format(self.path._activePath(), self.version)

    def activeSourceDirectory(self):
        return u'{}/{}'.format(self._activePath(), self.Folder_Source)

    def _serverPath(self):
        return u'{}/{}'.format(self.path.server, self.version)

    def serverSourceDirectory(self):
        return u'{}/{}'.format(self._serverPath(), self.Folder_Source)

    def _localPath(self):
        return u'{}/{}'.format(self.path.local, self.version)

    def localSourceDirectory(self):
        return u'{}/{}'.format(self._localPath(), self.Folder_Source)

    def _developPath(self):
        return u'{}/{}'.format(self.path.develop, self.version)

    def developSourceDirectory(self):
        return u'{}/{}'.format(self._developPath(), self.Folder_Source)

    def _productPath(self):
        return u'{}/{}'.format(self.path.product, self.version)

    def productSourceDirectory(self):
        return u'{}/{}'.format(self._productPath(), self.Folder_Source)

    def workspaceSourceDirectory(self):
        return self.resource.workspaceSourceDirectory()

    def _workspacePath(self):
        return self.path._workspacePath()

    def developSetupFile(self):
        return u'{}/{}'.format(self.developSourceDirectory(), u'setup.json')

    def createDevelopSetupFile(self):
        self.file._writeMethod(
            self.developSetupFile(),
            self.CLS_dic_order(
                [
                    (self.Key_User, bscMethods.OsSystem.username()),
                    (self.Key_Timestamp, bscMethods.OsSystem.activeTimestamp()),
                    (self.Key_Environ, self.dependentEnvirons()),
                    (self.Key_Module, self.dependentModules()),
                    (self.Key_Plug, self.dependentPlugs())
                ]
            )
        )

    def createDevelopDirectory(self):
        bscMethods.OsDirectory.create(self._developPath())

    def createDevelopSourceDirectory(self):
        bscMethods.OsDirectory.create(self.developSourceDirectory())

    def serverTimestampFile(self):
        return u'{}/source.timestamp.json'.format(
            self._serverPath()
        )

    def createServerTimestamp(self):
        self._createTimestampMethod(
            self.serverSourceDirectory(), self.serverTimestampFile()
        )

    def serverTimestampDatum(self):
        if bscMethods.OsPath.isExist(self.serverTimestampFile()) is False:
            self.createServerTimestamp()
        return bscMethods.OsJsonFile.read(self.serverTimestampFile()) or {}

    def localTimestampFile(self):
        return u'{}/source.timestamp.json'.format(
            self._localPath()
        )

    def createLocalTimestamp(self):
        self._createTimestampMethod(
            self.localSourceDirectory(), self.localTimestampFile()
        )

    def localTimestampDatum(self):
        if bscMethods.OsPath.isExist(self.localTimestampFile()) is False:
            self.createLocalTimestamp()
        return bscMethods.OsJsonFile.read(self.localTimestampFile()) or {}

    def localizationSource(self):
        changedFileLis = self._getChangedSourceFiles()
        if changedFileLis:
            for relativeOsFile in changedFileLis:
                sourceFile = self.serverSourceDirectory() + relativeOsFile
                targetFile = self.localSourceDirectory() + relativeOsFile

                bscMethods.OsFile.copyTo(sourceFile, targetFile, force=False)

                traceMessage = u'Localization Resource "{}" : "{}" > "{}"'.format(
                    self.name, sourceFile, targetFile
                )
                bscMethods.PyMessage.traceResult(traceMessage)

                bscMethods.OsFile.copyTo(self.serverTimestampFile(), self.localTimestampFile())
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

    def dependents(self):
        def recursionFnc(operate_):
            raw_ = operate_.dependent.raw()
            if raw_:
                for k, v in raw_.items():
                    resourceName = k
                    category = v[self.Key_Category]
                    system = v[self.Key_System]
                    version = v[self.Key_Version]

                    cls = self._cls_dic[category]
                    argument = []

                    argument_format_lis = self.MOD_copy.deepcopy(self._argument_dic[category])

                    if isinstance(system, dict):
                        for ik, iv in system.items():
                            if ik in argument_format_lis:
                                index = argument_format_lis.index(ik)
                                argument_format_lis[index] = iv

                    for i in argument_format_lis:
                        i = i.format(**operate_._formatDict_())
                        argument.append(i)

                    resource_ = cls(resourceName, *argument)

                    if resource_.file.isServerExist():
                        if version == self.Keyword_Version_Active:
                            version = resource_.version.active

                        operate__ = resource_.operateAt(version)
                        addFnc(operate__)
                        recursionFnc(operate__)

        def addFnc(operate_):
            name = operate_.name
            if not name in nameLis:
                nameLis.append(name)
                lis.append(operate_)

        nameLis = [self.name]

        lis = [self]

        recursionFnc(self)

        return lis

    def dependentEnvirons(self):
        dependentLis = self.dependents()

        environ = dependentLis[0].environ
        if len(dependentLis) > 1:
            if dependentLis[1:]:
                for i in dependentLis:
                    environ += i.environ

        return environ.raw()

    def dependentPaths(self):
        lis = []

        dependentLis = self.dependents()
        for i in dependentLis:
            lis.append(i.sourcepath)

        return lis

    def dependentModules(self):
        lis = []

        dependentLis = self.dependents()
        for i in dependentLis:
            if i.resource.isModule:
                lis.append(i.name)
        if lis:
            lis.sort()
        return lis

    def dependentPlugs(self):
        lis = []

        dependentLis = self.dependents()
        for i in dependentLis:
            if i.resource.isPlug:
                lis.append(i.name)
        if lis:
            lis.sort()
        return lis

    def _formatDict_(self):
        return {
            self.Attr_Key_Self: self,
            self.Attr_Key_System: self.system
        }

    def pushSourceToDevelop(self):
        workspaceSourcePath = self.resource.workspaceSourceDirectory()
        developSourceDirectory = self.developSourceDirectory()

        relativeOsFileLis = bscMethods.OsDirectory.allFileRelativenames(workspaceSourcePath, extString='.py')
        if relativeOsFileLis:
            bscMethods.OsDirectory.remove(developSourceDirectory)
            for i in relativeOsFileLis:
                workspacePyFile = u'{}/{}'.format(workspaceSourcePath, i)
                developPyFile = u'{}/{}/{}'.format(developSourceDirectory, self.name, i)
                bscMethods.OsFile.copyTo(workspacePyFile, developPyFile)

    def setup(self):
        pass

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.Key_Category, self.category),
                (self.DEF_key_name, self.name),
                (self.Key_Version, self.version),
                (self.Key_System, self.system.raw())
            ]
        )

    def __str__(self):
        return self._toJsonStringMethod(self.raw())
