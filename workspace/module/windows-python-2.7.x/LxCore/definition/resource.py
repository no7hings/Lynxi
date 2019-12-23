# coding:utf-8
from LxCore import lxBasic, lxConfigure

from LxCore.definition import method, abstract, system, file, raw

env = method.Environ()


class Rsc_Operate(lxConfigure.Basic):
    def __init__(self, config, version):
        self.Cls_Resource_Dic = {
            self.Category_Plt_Language: Rsc_PltLanguage,
            self.Category_Plt_Application: Rsc_PltApplication,

            self.Category_Plt_Lan_Package: Rsc_PltLanPackage,
            self.Category_Plt_App_Lan_Package: Rsc_PltAppLanPackage,

            self.Category_Plt_App_Package: Rsc_PltAppPackage,

            self.Category_Plt_Lan_Module: Rsc_PltLanModule,
            self.Category_Plt_App_Lan_Module: Rsc_PltAppLanModule,

            self.Category_Plt_App_Module: Rsc_PltAppModule,

            self.Category_Plt_Lan_Scheme: Rsc_PltLanScheme,
            self.Category_Plt_App_Lan_Scheme: Rsc_PltAppLanScheme
        }

        self._initResource(config, version)

    def _initResource(self, config, version):
        self._configObj = config
        self._version = version

        self._overrideEnvironRaw()

    def _overrideEnvironRaw(self):
        raw_ = self.environ.raw()
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

    @property
    def path(self):
        return self._configObj.file.directory

    @property
    def config(self):
        return self._configObj

    @property
    def category(self):
        return self._configObj.category

    @property
    def name(self):
        return self._configObj.name

    @property
    def system(self):
        return self._configObj.system

    @property
    def file(self):
        return self._configObj.file

    @property
    def version(self):
        return self._version

    @property
    def environ(self):
        return self._configObj.environ

    @property
    def dependent(self):
        return self._configObj.dependent

    @property
    def sourcepath(self):
        if self.isDevelop():
            if self._configObj.isModule:
                return self._workspacePath()
            return self.activeSourceDirectory()
        return self.activeSourceDirectory()

    def _activePath(self):
        return u'{}/{}'.format(self.path._activePath(), self.version)

    def activeSourceDirectory(self):
        return u'{}/{}'.format(self._activePath(), self.Folder_Source)

    def _serverPath(self):
        return u'{}/{}'.format(self.path._serverPath(), self.version)

    def serverSourceDirectory(self):
        return u'{}/{}'.format(self._serverPath(), self.Folder_Source)

    def _localPath(self):
        return u'{}/{}'.format(self.path._localPath(), self.version)

    def localSourceDirectory(self):
        return u'{}/{}'.format(self._localPath(), self.Folder_Source)

    def _developPath(self):
        return u'{}/{}'.format(self.path._developPath(), self.version())

    def _developSourceDirectory(self):
        return u'{}/{}'.format(self._developPath(), self.Folder_Source)

    def _productPath(self):
        return u'{}/{}'.format(self.path._productPath(), self.version)

    def _productSourceDirectory(self):
        return u'{}/{}'.format(self._productPath(), self.Folder_Source)

    def _workspacePath(self):
        return self.path._workspacePath()

    def createDevelopDirectory(self):
        lxBasic.createOsPath(self._developPath())

    def serverTimestampFile(self):
        return u'{}/timestamp.json'.format(
            self._serverPath()
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
            self._localPath()
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
                    self.name, sourceFile, targetFile
                )
                lxConfigure.Message().traceResult(traceMessage)

                lxBasic.setOsFileCopy(self.serverTimestampFile(), self.localTimestampFile())
        else:
            traceMessage = u'Resource "{}"  is "Non - Changed"'.format(self.name)
            lxConfigure.Message().traceResult(traceMessage)

    def addEnvirons(self):
        raw_ = self.environ.raw()
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
        return self._configObj.dependent.hasRaw()

    def dependents(self):
        def recursionFn(operate_):
            raw_ = operate_.dependent.raw()
            if raw_:
                for k, v in raw_.items():
                    name = k

                    category = v[self.Key_Category]
                    argument = []
                    argument_ = v[self.Key_Argument]
                    for i in argument_:
                        i = i.format(**self._formatDict())
                        argument.append(i)

                    cls = self.Cls_Resource_Dic[category]

                    resource_ = cls(name, *argument)

                    if resource_.file.isServerExist():
                        version = v[self.Key_Version]
                        if version == self.Version_Active:
                            version = resource_.version.active

                        operate__ = resource_.operateAt(version)
                        addFn(operate__)
                        recursionFn(operate__)

        def addFn(operate_):
            name = operate_.name
            if not name in nameLis:
                nameLis.append(name)
                lis.append(operate_)

        nameLis = [self.name]

        lis = [self]

        recursionFn(self)

        return lis

    def dependentEnvirons(self):
        environ = raw.Raw_Environ()

        dependentLis = self.dependents()
        if dependentLis:
            for i in dependentLis:
                environ += i.environ

        return environ

    def _formatDict(self):
        return {
            self.Attr_Key_Self: self,
            self.Attr_Key_Path:  self._activePath(),
            self.Attr_Key_System: self.system,
            self.Attr_Key_Path_Source: self.activeSourceDirectory()
        }

    def setup(self):
        pass

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Category, self._configObj.category),
                (self.Key_Name, self._configObj.name),
                (self.Key_Version, self.version),
                (self.Key_Argument, self._configObj.argument)
            ]
        )

    def __str__(self):
        return self._toStringMethod(self.raw())


class Rsc_PltLanguage(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_Platform
    FILE_CLS = file.Fle_BinConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_Language

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
        )


class Rsc_PltApplication(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_Platform
    FILE_CLS = file.Fle_BinConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_Application

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
        )


class Rsc_PltLanPackage(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_PltLanguage
    FILE_CLS = file.Fle_PackageConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_Lan_Package

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppLanPackage(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_PltAppLanguage
    FILE_CLS = file.Fle_PackageConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_App_Lan_Package

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )


class Rsc_PltAppPackage(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_PltApplication
    FILE_CLS = file.Fle_PackageConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_App_Package

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion
        )


class Rsc_PltLanModule(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_PltLanguage
    FILE_CLS = file.Fle_CfgModuleConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_Lan_Module

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppModule(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_PltApplication
    FILE_CLS = file.Fle_CfgModuleConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_App_Module

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion
        )


class Rsc_PltLanScheme(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_PltLanguage
    FILE_CLS = file.Fle_SchemeConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_Lan_Scheme

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppLanModule(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_PltAppLanguage
    FILE_CLS = file.Fle_CfgModuleConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_App_Lan_Module

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )


class Rsc_PltAppLanScheme(abstract.Abc_Resource):
    SYSTEM_CLS = system.Sys_PltAppLanguage
    FILE_CLS = file.Fle_SchemeConfigure
    RAW_CLS = raw.Raw_Configure
    OPERATE_CLS = Rsc_Operate

    object_category = lxConfigure.Basic.Category_Plt_App_Lan_Scheme

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )
