# coding:utf-8
from LxCore import lxBasic, lxConfigure

from LxCore.definition import abstract, path, bin, raw

env = lxBasic.Environ()


class Resource(lxConfigure.Basic):
    def __init__(self, config, version):
        self.Cls_Config_Dic = {
            self.Category_Windows_Python_Module: Cfg_WinPythonModule,
            self.Category_Windows_App_Python_Module: Cfg_WinAppPythonModule,
            self.Category_Windows_Python_Package: Cfg_WindowsPythonPackage,
            self.Category_Windows_App_Python_Package: Cfg_WinAppPythonPackage,
            self.Category_Windows_App_Plug: Cfg_WinAppPlug
        }

        self._initResource(config, version)

    def _initResource(self, config, version):
        self._config = config
        self._version = version

        self._overrideEnvironRaw()

    def _overrideEnvironRaw(self):
        raw_ = self._config.environ().raw()
        if raw_:
            for k, v in raw_.items():
                value = v[self.Key_Value]
                if isinstance(value, tuple) or isinstance(value, list):
                    value = [u'{}'.format(i.format(**self._formatDict())) for i in value]
                else:
                    value = u'{}'.format(value.format(**self._formatDict()))

                v[self.Key_Value] = value

    def _getChangedSourceFiles(self):
        return self._getChangedFileMethod(
            self.serverTimestampDatum(), self.localTimestampDatum()
        )

    def _toRaw(self):
        raw_ = self._config.raw()
        raw_[self.Key_Version] = self.version()
        return raw_

    def config(self):
        return self._config

    def category(self):
        return self._config.category()

    def name(self):
        return self._config.name()

    def version(self):
        return self._version

    def _activeDirectory(self):
        return u'{}/{}'.format(self._config._activeDirectory(), self.version())

    def activeSourceDirectory(self):
        return u'{}/{}'.format(self._activeDirectory(), self.Folder_Source)

    def _serverDirectory(self):
        return u'{}/{}'.format(self._config._serverDirectory(), self.version())

    def serverSourceDirectory(self):
        return u'{}/{}'.format(self._serverDirectory(), self.Folder_Source)

    def _localDirectory(self):
        return u'{}/{}'.format(self._config._localDirectory(), self.version())

    def localSourceDirectory(self):
        return u'{}/{}'.format(self._localDirectory(), self.Folder_Source)

    def _developDirectory(self):
        return u'{}/{}'.format(self._config._developDirectory(), self.version())

    def _developSourceDirectory(self):
        return u'{}/{}'.format(self._developDirectory(), self.Folder_Source)

    def _productDirectory(self):
        return u'{}/{}'.format(self._config._productDirectory(), self.version())

    def _productSourceDirectory(self):
        return u'{}/{}'.format(self._productDirectory(), self.Folder_Source)

    def createDevelopDirectory(self):
        lxBasic.createOsPath(self._developDirectory())

    def serverTimestampFile(self):
        return u'{}/timestamp.json'.format(
            self._serverDirectory()
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
            self._localDirectory()
        )

    def createLocalTimestamp(self):
        self._createTimestampMethod(
            self.localSourceDirectory(), self.localTimestampFile()
        )

    def localTimestampDatum(self):
        if lxBasic.isOsExist(self.localTimestampFile()) is False:
            self.createLocalTimestamp()
        return lxBasic.readOsJson(self.localTimestampFile()) or {}

    def localizationSource(self):
        changedFileLis = self._getChangedSourceFiles()
        if changedFileLis:
            for relativeOsFile in changedFileLis:
                sourceFile = self.serverSourceDirectory() + relativeOsFile
                targetFile = self.localSourceDirectory() + relativeOsFile

                lxBasic.setOsFileCopy(sourceFile, targetFile, force=False)

                traceMessage = u'Localization Resource "{}" : "{}" > "{}"'.format(
                    self._config.name(), sourceFile, targetFile
                )
                lxConfigure.Message().traceResult(traceMessage)

                lxBasic.setOsFileCopy(self.serverTimestampFile(), self.localTimestampFile())
        else:
            traceMessage = u'Resource "{}"  is "Non - Changed"'.format(self._config.name())
            lxConfigure.Message().traceResult(traceMessage)

    def addEnvirons(self):
        raw_ = self._config.environ().raw()
        if raw_:
            for k, v in raw_.items():
                operate = v[self.Key_Operate]
                if operate == '+':
                    operate = '+='
                value = v[self.Key_Value]
                if isinstance(value, tuple) or isinstance(value, list):
                    value = [u'"{}"'.format(i) for i in value]
                    command = u'env.{} {} [{}]'.format(k, operate, ', '.join(value))
                else:
                    value = u'"{}"'.format(value)
                    command = u'env.{} {} {}'.format(k, operate, value)

                exec command

    def environCommands(self):
        lis = []
        raw_ = self._config.environ().raw()
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
        return self._config.dependent().hasRaw()

    def dependentResources(self):
        def recursionFn(resource_):
            raw_ = resource_.config().dependent().raw()
            if raw_:
                for k, v in raw_.items():
                    category = k
                    for ik, iv in v.items():
                        name = ik

                        argument = iv[self.Key_Argument]

                        configMethod = self.Cls_Config_Dic[category]
                        if isinstance(argument, tuple) or isinstance(argument, list):
                            config = configMethod(name, *argument)
                        else:
                            config = configMethod(name, argument)
                        version = iv[self.Key_Version]
                        if version == self.Version_Active:
                            version = config.version().active()

                        resource = config.resourceAt(version)
                        addFn(resource)
                        recursionFn(resource)

        def addFn(resource_):
            name = resource_.name()
            if not name in nameLis:
                nameLis.append(name)
                lis.append(resource_)

        nameLis = [self.name()]

        lis = [self]

        recursionFn(self)

        return lis

    def dependentEnviron(self):
        environ = raw.Raw_Environ()

        dependentLis = self.dependentResources()
        if dependentLis:
            for i in dependentLis:
                environ += i.config().environ()

        return environ

    def _formatDict(self):
        return {
            self.Attr_Path:  self._activeDirectory(),
            self.Attr_Path_Source: self.activeSourceDirectory()
        }

    def setup(self):
        pass

    def raw(self):
        return {
            self.Key_Category: self._config.category(),
            self.Key_Name: self._config.name(),
            self.Key_Version: self.version(),
            self.Key_Argument: self._config.argument()
        }

    def __str__(self):
        return self._toStringMethod(self.raw())


class Cfg_WinApplication(abstract._AbcResourceConfig):
    PATH_CLS = path.ApplicationDirectory

    BIN_CLS = bin.Plf_Windows
    RAW_CLS = raw.Raw_ResourceConfig
    RESOURCE_CLS = Resource

    Category = lxConfigure.Basic.Category_Windows_Bin

    def __init__(self, binName, platformVersion):
        self._initAbcWindowsBinConfig(
            binName, platformVersion
        )


class Cfg_WinPythonModule(abstract._AbcResourceConfig):
    PATH_CLS = path.ModuleDirectory

    BIN_CLS = bin.Win_Python
    RAW_CLS = raw.Raw_ResourceConfig
    RESOURCE_CLS = Resource

    Category = lxConfigure.Basic.Category_Windows_Python_Module

    def __init__(self, resourceName, languageVersion):
        self._initAbcWindowsPythonResourceConfig(
            resourceName,
            languageVersion,
        )


class Cfg_WindowsPythonPackage(abstract._AbcResourceConfig):
    PATH_CLS = path.PackagePath

    BIN_CLS = bin.Win_Python
    RAW_CLS = raw.Raw_ResourceConfig
    RESOURCE_CLS = Resource

    Category = lxConfigure.Basic.Category_Windows_Python_Package

    def __init__(self, resourceName, languageVersion):
        self._initAbcWindowsPythonResourceConfig(
            resourceName,
            languageVersion
        )


class Cfg_WinAppPythonModule(abstract._AbcResourceConfig):
    PATH_CLS = path.ModuleDirectory

    BIN_CLS = bin.Win_Application
    RAW_CLS = raw.Raw_ResourceConfig
    RESOURCE_CLS = Resource

    Category = lxConfigure.Basic.Category_Windows_App_Python_Module

    def __init__(self, resourceName, appName, appVersion):
        self._initAbcWindowsAppPythonResourceConfig(
            resourceName,
            appName, appVersion,

        )


class Cfg_WinAppPythonPackage(abstract._AbcResourceConfig):
    PATH_CLS = path.PackagePath

    BIN_CLS = bin.Win_Application
    RAW_CLS = raw.Raw_ResourceConfig
    RESOURCE_CLS = Resource

    Category = lxConfigure.Basic.Category_Windows_App_Python_Package

    def __init__(self, resourceName, appName, appVersion):
        self._initAbcWindowsAppPythonResourceConfig(
            resourceName,
            appName, appVersion,
        )


class Cfg_WinAppPlug(abstract._AbcResourceConfig):
    PATH_CLS = path.AppPlugPath

    BIN_CLS = bin.Win_Application
    RAW_CLS = raw.Raw_ResourceConfig
    RESOURCE_CLS = Resource

    Category = lxConfigure.Basic.Category_Windows_App_Plug

    def __init__(self, resourceName, appName, appVersion):
        self._initAbcWindowsAppResourceConfig(
            resourceName,
            appName, appVersion,
        )


class Cfg_WinPythonScheme(abstract._AbcResourceConfig):
    PATH_CLS = path.SchemePath

    BIN_CLS = bin.Win_Python
    RAW_CLS = raw.Raw_ResourceConfig
    RESOURCE_CLS = Resource

    Category = lxConfigure.Basic.Category_Windows_Python_Scheme

    def __init__(self, schemeName, languageVersion):
        self._initAbcWindowsPythonResourceConfig(
            schemeName,
            languageVersion
        )


class Cfg_WinAppPythonScheme(abstract._AbcResourceConfig):
    PATH_CLS = path.SchemePath

    BIN_CLS = bin.Win_Application
    RAW_CLS = raw.Raw_ResourceConfig
    RESOURCE_CLS = Resource

    Category = lxConfigure.Basic.Category_Windows_App_Python_Scheme

    def __init__(self, schemeName, appName, appVersion):
        self._initAbcWindowsAppPythonResourceConfig(
            schemeName,
            appName, appVersion
        )
