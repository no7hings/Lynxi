# coding:utf-8
from LxScheme import shmCore, shmObjAbstract

from LxScheme.shmObjects import _shmObjSystem, _shmObjRaw, _shmObjFile


class Rsc_Operate(shmObjAbstract.Abc_Operate):
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
        pass

    def addDependentSystemPaths(self):
        dependentLis = self.dependents()
        [i.addPythonPath() for i in dependentLis]

    def addDependentEnvirons(self):
        pass

    def addEnvirons(self):
        pass


# Bin
class Rsc_PltLanguage(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_Platform
    CLS_path_file = _shmObjFile.Fle_RscBin
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_Language

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
        )


class Rsc_PltApplication(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_Platform
    CLS_path_file = _shmObjFile.Fle_RscBin
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_Application

    def __init__(self, resourceName, platformName, platformVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
        )


# Package
class Rsc_PltLanPackage(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltLanguage
    CLS_path_file = _shmObjFile.Fle_RscPackage
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_Lan_Package

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppLanPackage(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_path_file = _shmObjFile.Fle_RscPackage
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Lan_Package

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )


class Rsc_PltAppPackage(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltApplication
    CLS_path_file = _shmObjFile.Fle_RscPackage
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Package

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion
        )


# Plug
class Rsc_PltLanPlug(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltLanguage
    CLS_path_file = _shmObjFile.Fle_RscPlug
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_Lan_Plug

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppLanPlug(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_path_file = _shmObjFile.Fle_RscPlug
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Lan_Plug

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )


class Rsc_PltAppPlug(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltApplication
    CLS_path_file = _shmObjFile.Fle_RscPlug
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Plug

    def __init__(self, resourceName, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            applicationName, applicationVersion
        )


# Module
class Rsc_PltLanModule(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltLanguage
    CLS_path_file = _shmObjFile.Fle_RscModule
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_Lan_Module

    def __init__(self, resourceName, platformName, platformVersion, languageName, languageVersion):
        self._initAbcResource(
            resourceName,
            platformName, platformVersion,
            languageName, languageVersion
        )


class Rsc_PltAppModule(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltApplication
    CLS_path_file = _shmObjFile.Fle_RscModule
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Module

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion
        """
        self._initAbcResource(*args)


class Rsc_PltAppLanModule(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_path_file = _shmObjFile.Fle_RscModule
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Lan_Module

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion
        """

        self._initAbcResource(*args)


# Scheme
class Rsc_PltLanScheme(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltLanguage
    CLS_path_file = _shmObjFile.Fle_RscScheme
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_Lan_Scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, languageName, languageVersion
        """
        self._initAbcResource(*args)


class Rsc_PltAppLanScheme(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_path_file = _shmObjFile.Fle_RscScheme
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Lan_Scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion
        """

        self._initAbcResource(*args)


class Rsc_PltAppScheme(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltApplication
    CLS_path_file = _shmObjFile.Fle_RscScheme
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Scheme

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion
        """

        self._initAbcResource(*args)


# Tool
class Rsc_PltLanTool(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltLanguage
    CLS_path_file = _shmObjFile.Fle_RscTool
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_Lan_Tool

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, languageName, languageVersion
        """
        self._initAbcResource(*args)


class Rsc_PltAppLanTool(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltAppLanguage
    CLS_path_file = _shmObjFile.Fle_RscTool
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Lan_Tool

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion
        """

        self._initAbcResource(*args)


class Rsc_PltAppTool(shmObjAbstract.Abc_Resource):
    CLS_system = _shmObjSystem.Sys_PltApplication
    CLS_path_file = _shmObjFile.Fle_RscTool
    CLS_raw = _shmObjRaw.Raw_Resource
    CLS_operate = Rsc_Operate

    object_category = shmCore.Basic.Category_Plf_App_Tool

    def __init__(self, *args):
        """
        :param args: resourceName, platformName, platformVersion, applicationName, applicationVersion
        """

        self._initAbcResource(*args)
