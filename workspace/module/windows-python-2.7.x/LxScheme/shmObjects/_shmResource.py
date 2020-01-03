# coding:utf-8
from LxCore import lxCore_

from LxScheme import shmAbstract

from LxScheme.shmObjects import _shmSystem, _shmRaw, _shmFile, _shmMethod

env = _shmMethod.Mtd_Environ()
syspath = _shmMethod.Mtd_SystemPath()


class Rsc_Operate(shmAbstract.Abc_Operate):
    def __init__(self, config, version):
        self._cls_dic = {
            self.Category_Plf_Language: Rsc_PltLanguage,
            self.Category_Plf_Application: Rsc_PltApplication,

            self.Category_Plf_Lan_Package: Rsc_PltLanPackage,
            self.Category_Plf_App_Lan_Package: Rsc_PltAppLanPackage,
            self.Category_Plf_App_Package: Rsc_PltAppPackage,

            self.Category_Plf_Lan_Plug: Rsc_PltLanPlug,
            self.Category_Plf_App_Lan_Plug: Rsc_PltAppLanPlug,
            self.Category_Plf_App_Plug: Rsc_PltAppPlug,

            self.Category_Plf_Lan_Module: Rsc_PltLanModule,
            self.Category_Plf_App_Lan_Module: Rsc_PltAppLanModule,
            self.Category_Plf_App_Module: Rsc_PltAppModule,

            self.Category_Plf_Lan_Scheme: Rsc_PltLanScheme,
            self.Category_Plf_App_Lan_Scheme: Rsc_PltAppLanScheme
        }
        self._argument_dic = {
            self.Category_Plf_Language: [
                '{system.platform.name}', '{system.platform.version}'
            ],
            self.Category_Plf_Application: [
                '{system.platform.name}', '{system.platform.version}'
            ],
            # Package
            self.Category_Plf_Lan_Package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Lan_Package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            # Plug
            self.Category_Plf_Lan_Plug: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Lan_Plug: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Plug: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            # Module
            self.Category_Plf_Lan_Module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Lan_Module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            self.Category_Plf_Lan_Scheme: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.Category_Plf_App_Lan_Scheme: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ]
        }

        self._initAbcOperate(config, version)

    def addPythonPath(self):
        global syspath
        syspath += self.sourcepath

    def addDependentSystemPaths(self):
        dependentLis = self.dependents()
        [i.addPythonPath() for i in dependentLis]

    def addDependentEnvirons(self):
        pass

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


class Rsc_PltLanguage(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_Platform
    FILE_CLS = _shmFile.Fle_RscBin
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_Language

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
        )


class Rsc_PltApplication(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_Platform
    FILE_CLS = _shmFile.Fle_RscBin
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_Application

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
        )


class Rsc_PltLanPackage(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltLanguage
    FILE_CLS = _shmFile.Fle_RscPackage
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_Lan_Package

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppLanPackage(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltAppLanguage
    FILE_CLS = _shmFile.Fle_RscPackage
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_App_Lan_Package

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )


class Rsc_PltAppPackage(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltApplication
    FILE_CLS = _shmFile.Fle_RscPackage
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_App_Package

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion
        )


class Rsc_PltLanPlug(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltLanguage
    FILE_CLS = _shmFile.Fle_RscPlug
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_Lan_Plug

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppLanPlug(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltAppLanguage
    FILE_CLS = _shmFile.Fle_RscPlug
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_App_Lan_Plug

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )


class Rsc_PltAppPlug(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltApplication
    FILE_CLS = _shmFile.Fle_RscPlug
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_App_Plug

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion
        )


class Rsc_PltLanModule(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltLanguage
    FILE_CLS = _shmFile.Fle_RscModule
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_Lan_Module

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppModule(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltApplication
    FILE_CLS = _shmFile.Fle_RscModule
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_App_Module

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion
        """
        self._initAbcResource(*args)


class Rsc_PltLanScheme(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltLanguage
    FILE_CLS = _shmFile.Fle_RscScheme
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_Lan_Scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, languageName, languageVersion
        """
        self._initAbcResource(*args)


class Rsc_PltAppLanModule(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltAppLanguage
    FILE_CLS = _shmFile.Fle_RscModule
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_App_Lan_Module

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion
        """

        self._initAbcResource(*args)


class Rsc_PltAppLanScheme(shmAbstract.Abc_Resource):
    SYSTEM_CLS = _shmSystem.Sys_PltAppLanguage
    FILE_CLS = _shmFile.Fle_RscScheme
    RAW_CLS = _shmRaw.Raw_Resource
    OPERATE_CLS = Rsc_Operate

    object_category = lxCore_.Basic.Category_Plf_App_Lan_Scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion
        """

        self._initAbcResource(*args)
