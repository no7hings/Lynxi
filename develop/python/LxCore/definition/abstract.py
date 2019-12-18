# coding:utf-8
from LxCore import lxBasic, lxConfigure


class _AbcRaw(lxConfigure.Basic):
    def _initAbcRaw(self):
        self._raw = {}
        self._defRaw = {}

        self._cacheRaw = {}

    def create(self, raw):
        self._raw = raw
        self._defRaw = raw

    def _getValue(self, key):
        if key in self._raw:
            return self._raw[key]
        return self._defRaw.get(key)

    def setRaw(self, raw):
        self._raw = raw

    def raw(self):
        return self._raw

    def hasRaw(self):
        return self._raw != {}

    def setDefRaw(self, raw):
        self._defRaw = raw

    def hasDefRaw(self):
        return self._defRaw is not None

    def defRaw(self):
        return self._defRaw

    def setCacheRaw(self, raw):
        pass

    def hasCacheRaw(self):
        return self._cacheRaw is not None

    def cacheRaw(self):
        return self._cacheRaw

    def __str__(self):
        return self._toStringMethod(self.raw())


class _AbcBin(lxConfigure.Basic):
    def _initAbcBin(self, name, version):
        self._name = name
        self._version = version

    def setName(self, string):
        self._name = string

    def name(self):
        return self._name

    def setVersion(self, string):
        self._version = string

    def version(self):
        return self._version

    def raw(self):
        return {
            self.Key_Name: self.name(),
            self.Key_Version: self.version()
        }

    def __str__(self):
        return self._toStringMethod(self.raw())


class _AbcPlatform(_AbcBin):
    def _initAbcPlatform(self, platformName, platformVersion):
        self._initAbcBin(platformName, platformVersion)


class _AbcLanguage(_AbcBin):
    Key_Environ_Bin_Path = None
    Bin_Path_Default = None

    def _initAbcLanguage(self, name, version):
        self._initAbcBin(name, version)


class _AbcApplication(_AbcBin):
    PLATFORM_CLS = None
    LANGUAGE_CLS = None

    def _initAbcApplication(self, platformName, platformVersion, appName, appVersion, languageName, languageVersion):
        self._initAbcBin(appName, appVersion)

        if platformName == self.Bin_Share:
            self._platform = self.PLATFORM_CLS(platformName, platformVersion)
        else:
            self._platform = self.PLATFORM_CLS(platformVersion)

        if languageName == self.Language_Python:
            self._language = self.LANGUAGE_CLS(languageVersion)
        else:
            self._language = self.LANGUAGE_CLS(languageName, languageVersion)

    def _initAbcWindowsMaya(self, version):
        self._initAbcApplication(
            self.Platform_Windows, self.Version_Share,
            self.App_Maya, version,
            self.Language_Python, self.Python_Version_27
        )

    def platform(self):
        return self._platform

    def language(self):
        return self._language

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Name, self.name()),
                (self.Key_Version, self.version()),
                (self.Key_Platform, self.platform().raw()),
                (self.Key_Language, self.language().raw())
            ]
        )


class _AbcResourceConfig(lxConfigure._AbcConfigFile):
    PATH_WORKSPACE_CLS = lxConfigure.WorkspaceModulePath

    RAW_CLS = None
    BIN_CLS = None
    RESOURCE_CLS = None

    Category = None

    def _initAbcResourceConfig(self, *args):
        name = args[0]

        args_ = list(args[1:])
        args_.append(name.lower())

        self._initAbcConfigFile(*args_)

        self._initRaw()

    def _initRaw(self):
        cacheRaw = self.cacheRaw()
        if cacheRaw:
            self.version().create(cacheRaw[self.Key_Version])
            self.environ().create(cacheRaw[self.Key_Environ])
            self.dependent().create(cacheRaw[self.Key_Dependent])

        self._raw = self._rawObj.raw()

    def _initAbcWindowsBinConfig(self, binName, platformVersion):
        self._bin = self.BIN_CLS(platformVersion)

        platformName = self._bin.name()

        self._rawObj = self.RAW_CLS(
            self.Category, binName,
            self._bin
        )

        self._argument = platformVersion

        if platformVersion == self.Version_Share:
            self._initAbcResourceConfig(
                binName,
                platformName
            )
        else:
            self._initAbcResourceConfig(
                binName,
                platformName, platformVersion
            )

    def _initAbcWindowsPythonResourceConfig(self, resourceName, languageVersion):
        self._bin = self.BIN_CLS(self.Version_Share, languageVersion)
        self._platform = self._bin.platform()
        self._language = self._bin.language()

        platformName = self._platform.name()

        languageName = self._language.name()

        self._rawObj = self.RAW_CLS(
            self.Category, resourceName,
            self._bin
        )

        self._argument = languageVersion

        self._initAbcResourceConfig(
            resourceName,
            platformName,
            languageName, languageVersion
        )

    def _initAbcWindowsAppPythonResourceConfig(self, resourceName, appName, appVersion):
        self._bin = self.BIN_CLS(appName, appVersion)
        self._platform = self._bin.platform()
        self._language = self._bin.language()

        appName = self._bin.name()
        appVersion = self._bin.version()

        platformName = self._platform.name()

        languageName = self._language.name()
        languageVersion = self._language.version()

        self._rawObj = self.RAW_CLS(
            self.Category, resourceName,
            self._bin
        )

        self._argument = [appName, appVersion]

        if appVersion == self.Bin_Share:
            self._initAbcResourceConfig(
                resourceName,
                platformName,
                appName,
                languageName, languageVersion,
            )
        else:
            self._initAbcResourceConfig(
                resourceName,
                platformName,
                appName, appVersion,
                languageName, languageVersion,
            )

    def _initAbcWindowsAppResourceConfig(self, resourceName, appName, appVersion):
        self._bin = self.BIN_CLS(appName, appVersion)
        self._platform = self._bin.platform()
        self._language = self._bin.language()

        platformName = self._platform.name()

        self._rawObj = self.RAW_CLS(
            self.Category, resourceName,
            self._bin
        )

        self._argument = [appName, appVersion]

        if appVersion == self.Version_Share:
            self._initAbcResourceConfig(
                resourceName,
                platformName,
                appName
            )
        else:
            self._initAbcResourceConfig(
                resourceName,
                platformName,
                appName, appVersion
            )

    def _initAbcWindowsPythonSchemeConfig(self, schemeName, languageVersion):
        pass

    def _initAbcWindowsAppPythonSchemeConfig(self, schemeName, appName, appVersion):
        pass

    def argument(self):
        return self._argument

    def bin(self):
        return self._bin

    def enable(self):
        return self._rawObj.enable()

    def category(self):
        return self._rawObj.category()

    def name(self):
        return self._rawObj.name()

    def version(self):
        return self._rawObj.version()

    def environ(self):
        return self._rawObj.environ()

    def dependent(self):
        return self._rawObj.dependent()

    def resourceAt(self, version):
        if version in self.version().record():
            return self.RESOURCE_CLS(self, version)

    def createCache(self):
        self.FILE_CLS(self.file()).write(self._rawObj.raw())

    def createDevelopDirectories(self):
        for i in self.version().record():
            resource = self.resourceAt(i)
            resource.createDevelopDirectory()

    def createResource(self, version):
        pass

    def __str__(self):
        return self._toStringMethod(self.raw())
