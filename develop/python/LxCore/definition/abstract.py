# coding:utf-8
from LxCore import lxBasic, lxConfigure


class Abc_Object(lxConfigure.Basic):
    def _initAbcObject(self, category, name):
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
            self.Key_Name: self._name,
        }

    def __str__(self):
        return self._toStringMethod(self.raw())


class Abc_Path(lxConfigure.Basic):
    def _initAbcPath(self):
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

    def _formatDict(self):
        return {
            self.Attr_Key_Self: self,
        }

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Path_Key_Active, self.server),
                (self.Path_Key_Server, self.server),
                (self.Path_Key_Local, self.local),
                (self.Path_Key_Develop, self.develop),
                (self.Path_Key_Product, self.product)
            ]
        )

    def __str__(self):
        return self._toStringMethod(self.raw())


class Abc_PthRoot(Abc_Path):
    def _initAbcPthRoot(self):
        pass

    def _localPath(self):
        data = lxBasic.getOsEnvironValue(self.Key_Environ_Path_Local)
        if data is not None:
            return data.replace('\\', '/')
        return self.Path_Local_Default

    def _developPath(self):
        data = lxBasic.getOsEnvironValue(self.Key_Environ_Path_Develop)
        if data is not None:
            return data.replace('\\', '/')
        return self.Root_Develop_Default

    def _productPath(self):
        data = lxBasic.getOsEnvironValue(self.Key_Environ_Path_Product)
        if data is not None:
            return data.replace('\\', '/')
        return self.Root_Product_Default


class Abc_PthDirectory(Abc_Path):
    ROOT_CLS = None

    def _initAbcPthDirectory(self, *args):
        self.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/{self.subpath}',
            self.Path_Key_Server: u'{self.root.server}/{self.subpath}',
            self.Path_Key_Local: u'{self.root.local}/{self.subpath}',
            self.Path_Key_Develop: u'{self.root.develop}/{self.subpath}',
            self.Path_Key_Product: u'{self.root.product}/{self.subpath}',
            self.Path_Key_Workspace: u'{self.root.workspace}/{self.subpath}'
        }

        self._root = self.ROOT_CLS()

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
        return self.pathFormatString[self.Path_Key_Active].format(**self._formatDict())

    def _serverPath(self):
        return self.pathFormatString[self.Path_Key_Server].format(**self._formatDict())

    def _localPath(self):
        return self.pathFormatString[self.Path_Key_Local].format(**self._formatDict())

    def _developPath(self):
        return self.pathFormatString[self.Path_Key_Develop].format(**self._formatDict())

    def _productPath(self):
        return self.pathFormatString[self.Path_Key_Product].format(**self._formatDict())

    def _workspacePath(self):
        pass


class Abc_File(lxConfigure.Basic):
    DIRECTORY_CLS = None
    METHOD_CLS = None

    def _initAbcFile(self, directoryArgs, baseName, ext):
        self.pathFormatString = {
            self.Path_Key_Active: u'{self.directory.active}/{self.basename}',
            self.Path_Key_Server: u'{self.directory.server}/{self.basename}',
            self.Path_Key_Local: u'{self.directory.local}/{self.basename}',
            self.Path_Key_Develop: u'{self.directory.develop}/{self.basename}',
            self.Path_Key_Product: u'{self.directory.product}/{self.basename}'
        }

        self._directory = self.DIRECTORY_CLS(*directoryArgs)

        self._baseName = u'{}{}'.format(baseName, ext)

    @classmethod
    def _readMethod(cls, fileString):
        return cls.METHOD_CLS(fileString).read()

    @classmethod
    def _writeMethod(cls, fileString, raw):
        cls.METHOD_CLS(fileString).write(raw)

    @property
    def directory(self):
        return self._directory

    @property
    def basename(self):
        return self._baseName

    def activeFile(self):
        return self.pathFormatString[self.Path_Key_Active].format(**self._formatDict())

    def createActiveFile(self, raw):
        self._writeMethod(self.activeFile(), raw)

    def hasActiveFile(self):
        return lxBasic.isOsExist(self.activeFile())

    def activeFileRaw(self):
        if self.hasActiveFile():
            return self._readMethod(self.activeFile())
        return {}

    def serverFile(self):
        return self.pathFormatString[self.Path_Key_Server].format(**self._formatDict())

    def createServerFile(self, raw):
        self._writeMethod(self.serverFile(), raw)

    def hasServerFile(self):
        return lxBasic.isOsExist(self.serverFile())

    def serverFileRaw(self):
        if self.hasServerFile():
            return self._readMethod(self.serverFile())
        return {}

    def localFile(self):
        return self.pathFormatString[self.Path_Key_Local].format(**self._formatDict())

    def hasLocalFile(self):
        return lxBasic.isOsExist(self.localFile())

    def developFile(self):
        return self.pathFormatString[self.Path_Key_Develop].format(**self._formatDict())

    def hasDevelopFile(self):
        return lxBasic.isOsExist(self.developFile())

    def productFile(self):
        return self.pathFormatString[self.Path_Key_Product].format(**self._formatDict())

    def hasProductFile(self):
        return lxBasic.isOsExist(self.productFile())

    def _formatDict(self):
        return {
            self.Attr_Key_Self: self,
        }

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Path_Key_Active, self.activeFile()),
                (self.Path_Key_Server, self.serverFile()),
                (self.Path_Key_Local, self.localFile()),
                (self.Path_Key_Develop, self.developFile()),
                (self.Path_Key_Product, self.productFile())
            ]
        )

    def __str__(self):
        return self._toStringMethod(self.raw())


class Abc_System(Abc_Object):
    key_environ_bin_path = None
    key_bin_default = None

    object_category = None
    raw_key = None
    def _initAbcBin(self, name, version):
        self._initAbcObject(self.object_category, name)

        self._version = version

    def setVersion(self, string):
        self._version = string

    @property
    def version(self):
        return self._version

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Category, self.category),
                (self.Key_Name, self.name),
                (self.Key_Version, self.version)
            ]
        )

    @property
    def systemraw(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Name, self.name),
                (self.Key_Version, self.version)
            ]
        )

    def __str__(self):
        return self._toStringMethod(self.raw())


class Abc_SysPlatform(Abc_System):
    def _initAbcSysPlatform(self, platformName, platformVersion):
        self._initAbcBin(platformName, platformVersion)


class Abc_SysBin(Abc_System):
    SYSTEM_CLS = None

    def _initAbcSysPltLanguage(self, platformName, platformVersion, languageName, languageVersion):
        self._initAbcBin(languageName, languageVersion)

        self._systemObj = self.SYSTEM_CLS(
            platformName, platformVersion,
        )

    def _initAbcSysPltApplication(self, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbcBin(applicationName, applicationVersion)

        self._systemObj = self.SYSTEM_CLS(platformName, platformVersion)

    def _initAbcSysPltAppLanguage(self, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcBin(languageName, languageVersion)

        self._systemObj = self.SYSTEM_CLS(
            platformName, platformVersion,
            applicationName, applicationVersion
        )

    @property
    def system(self):
        return self._systemObj

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Category, self.category),
                (self.Key_Name, self.name),
                (self.Key_Version, self.version)
            ]
        )


class Abc_Raw(lxConfigure.Basic):
    def _initAbcRaw(self):
        self._raw = lxBasic.orderedDict()

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
        return self._toStringMethod(self.raw())


class Abc_RawConfigure(Abc_Raw):
    def _initAbcRawConfigure(self, enable, category, name):
        self.create(
            lxBasic.orderedDict(
                [
                    (self.Key_Enable, enable),
                    (self.Key_Category, category),
                    (self.Key_Name, name)
                ]
            )
        )

        self._rawObjDic = lxBasic.orderedDict()

    def addRaw(self, key, value):
        self._rawObjDic[key] = value

    def raw(self):
        dic = self._raw
        for k, v in self._rawObjDic.items():
            dic[k] = v.raw()
        return dic


class Abc_Resource(Abc_Object):
    SYSTEM_CLS = None
    FILE_CLS = None
    CONFIGURE_CLS = None
    OPERATE_CLS = None

    object_category = None

    def _initRaw(self):
        serverRaw = self.file.serverFileRaw()
        if serverRaw:
            self.version.create(serverRaw[self.Key_Version])
            self.environ.create(serverRaw[self.Key_Environ])
            self.dependent.create(serverRaw[self.Key_Dependent])

        self._raw = self._configObj.raw()

    def _initAbcResource(self, *args):
        resourceName = args[0]
        self._initAbcObject(self.object_category, resourceName)
        # Bin
        self._argument = args[1:]
        self._systemObj = self.SYSTEM_CLS(*self._argument)

        self._enable = True
        # Config
        self._configObj = self.CONFIGURE_CLS(
            True, self.object_category, resourceName,
            self._systemObj
        )
        # File
        args_ = list(args[1:])
        args_.append(resourceName.lower())
        fileArgs = [i for i in args_ if not i == self.Keyword_Share]
        self._fileObj = self.FILE_CLS(*fileArgs)

        self._version = self._configObj.version
        self._environ = self._configObj.environ
        self._dependent = self._configObj.dependent
        # Raw
        self._initRaw()

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
        return self._configObj

    def operateAt(self, version):
        if version in self.version.record:
            return self.OPERATE_CLS(self, version)

    def createServerCache(self):
        self.file.createServerFile(self.raw().raw())

    def createDevelopDirectories(self):
        for i in self.version.record:
            resource = self.operateAt(i)
            resource.createDevelopDirectory()

    def createResource(self, version):
        pass

    def __str__(self):
        return self._toStringMethod(self.raw().raw())
