# coding:utf-8
from .. import shmCfg, shmObjAbs

from . import _shmObjSystem, _shmObjRaw, _shmObjFile


class Rsc_Operate(shmObjAbs.AbsShmRscOperate):
    def __init__(self, config, version):
        self.VAR_shm__rsc_op__rsc_cls_dict = {
            # bin
            self.DEF_shm__rsc__category__plf_language: Rsc_PltLanguage,
            self.DEF_shm__rsc__category__plf_application: Rsc_PltApplication,
            # package
            self.DEF_shm__rsc__category__plf_lng_package: Rsc_PltLanPackage,
            self.DEF_shm__rsc__category__plf_app_lng_Package: Rsc_PltAppLanPackage,
            self.DEF_shm__rsc__category__plf_App_Package: Rsc_PltAppPackage,
            # plug
            self.DEF_shm__rsc__category__plf_plug: Rsc_PltPlug,
            self.DEF_shm__rsc__category__plf_lng_plug: Rsc_PltLanPlug,
            self.DEF_shm__rsc__category__plf_app_lng_plug: Rsc_PltAppLanPlug,
            self.DEF_shm__rsc__category__plf_app_plug: Rsc_PltAppPlug,
            # module
            self.DEF_shm__rsc__category__plf_lng_module: Rsc_PltLanModule,
            self.DEF_shm__rsc__category__plf_app_lng_module: Rsc_PltAppLanModule,
            self.DEF_shm__rsc__category__plf_app_module: Rsc_PltAppModule,
            # scheme
            self.DEF_shm__rsc__category__plf_lng_scheme: Rsc_PltLanScheme,
            self.DEF_shm__rsc__category__plf_app_scheme: Rsc_PltAppScheme,
            self.DEF_shm__rsc__category__plf_app_lng_scheme: Rsc_PltAppLanScheme
        }
        self.VAR_shm__rsc_op__rsc_sys_args_format_dict = {
            # bin
            self.DEF_shm__rsc__category__plf_language: [
                '{system.platform.name}', '{system.platform.version}'
            ],
            self.DEF_shm__rsc__category__plf_application: [
                '{system.platform.name}', '{system.platform.version}'
            ],
            # package
            self.DEF_shm__rsc__category__plf_lng_package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.DEF_shm__rsc__category__plf_app_lng_Package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.DEF_shm__rsc__category__plf_App_Package: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            # plug
            self.DEF_shm__rsc__category__plf_plug: [
                '{system.platform.name}', '{system.platform.version}'
            ],
            self.DEF_shm__rsc__category__plf_lng_plug: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.DEF_shm__rsc__category__plf_app_lng_plug: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.DEF_shm__rsc__category__plf_app_plug: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            # module
            self.DEF_shm__rsc__category__plf_lng_module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.DEF_shm__rsc__category__plf_app_lng_module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.DEF_shm__rsc__category__plf_app_module: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            # scheme
            self.DEF_shm__rsc__category__plf_lng_scheme: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.language.name}', '{system.language.version}'
            ],
            self.DEF_shm__rsc__category__plf_app_scheme: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}'
            ],
            self.DEF_shm__rsc__category__plf_app_lng_scheme: [
                '{system.platform.name}', '{system.platform.version}',
                '{system.application.name}', '{system.application.version}',
                '{system.language.name}', '{system.language.version}'
            ]
        }

        self._initAbsShmRscOperate(config, version)

    def setPythonModuleAdd(self):
        pass

    def addDependentSystemPaths(self):
        dependentLis = self.dependents()
        [i.setPythonModuleAdd() for i in dependentLis]

    def addDependentEnvirons(self):
        pass

    def addEnvirons(self):
        pass


# Bin
class Rsc_PltLanguage(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_Platform
    CLS_shm__resource_file = _shmObjFile.Fle_RscBin
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_language

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
        )


class Rsc_PltApplication(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_Platform
    CLS_shm__resource_file = _shmObjFile.Fle_RscBin
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_application

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
        )


# package > platform language **************************************************************************************** #
class Rsc_PltLanPackage(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltLanguage
    CLS_shm__resource_file = _shmObjFile.Fle_RscPackage
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_lng_package

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


# package > platform application ( plug ? )
class Rsc_PltAppPackage(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltApplication
    CLS_shm__resource_file = _shmObjFile.Fle_RscPackage
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_App_Package

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion
        )


# package > platform application language
class Rsc_PltAppLanPackage(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_shm__resource_file = _shmObjFile.Fle_RscPackage
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_app_lng_Package

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )


# plug > platform **************************************************************************************************** #
class Rsc_PltPlug(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_Platform
    CLS_shm__resource_file = _shmObjFile.Fle_RscPlug
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_plug

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion
        )


# plug > platform language
class Rsc_PltLanPlug(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltLanguage
    CLS_shm__resource_file = _shmObjFile.Fle_RscPlug
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_lng_plug

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppLanPlug(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_shm__resource_file = _shmObjFile.Fle_RscPlug
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_app_lng_plug

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )


class Rsc_PltAppPlug(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltApplication
    CLS_shm__resource_file = _shmObjFile.Fle_RscPlug
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_app_plug

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion
        )


# Module
class Rsc_PltLanModule(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltLanguage
    CLS_shm__resource_file = _shmObjFile.Fle_RscModule
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_lng_module

    def __init__(
            self,
            resourceName,
            platformName,
            platformVersion,
            languageName,
            languageVersion
    ):
        self._initAbsShmResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppModule(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltApplication
    CLS_shm__resource_file = _shmObjFile.Fle_RscModule
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_app_module

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion
        """
        self._initAbsShmResource(*args)


class Rsc_PltAppLanModule(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_shm__resource_file = _shmObjFile.Fle_RscModule
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_app_lng_module

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion
        """

        self._initAbsShmResource(*args)


# Scheme
class Rsc_PltScheme(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_Platform
    CLS_shm__resource_file = _shmObjFile.Fle_RscScheme
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, languageName, languageVersion
        """
        self._initAbsShmResource(*args)


class Rsc_PltLanScheme(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltLanguage
    CLS_shm__resource_file = _shmObjFile.Fle_RscScheme
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_lng_scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, languageName, languageVersion
        """
        self._initAbsShmResource(*args)


class Rsc_PltAppScheme(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltApplication
    CLS_shm__resource_file = _shmObjFile.Fle_RscScheme
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_App_Scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion
        """

        self._initAbsShmResource(*args)


class Rsc_PltAppLanScheme(shmObjAbs.AbsShmResource):
    CLS_shm__resource_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_shm__resource_file = _shmObjFile.Fle_RscScheme
    CLS_shm__resource_raw = _shmObjRaw.RscResourceConfigure
    CLS_shm__resource_operate = Rsc_Operate

    VAR_shm__resource__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_app_lng_scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion
        """

        self._initAbsShmResource(*args)
