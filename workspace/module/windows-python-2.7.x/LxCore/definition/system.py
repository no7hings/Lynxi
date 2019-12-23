# coding:utf-8
from LxCore import lxBasic, lxConfigure

from LxCore.definition import abstract


class Sys_Platform(abstract.Abc_System):
    object_category = lxConfigure.Basic.Category_Platform
    raw_key = lxConfigure.Basic.Key_Platform

    def __init__(self, platformName, platformVersion):
        self._initAbcSystem(platformName, platformVersion)


class Sys_PltApplication(abstract.Abc_System):
    SYSTEM_CLS = Sys_Platform

    object_category = lxConfigure.Basic.Category_Plt_Application
    raw_key = lxConfigure.Basic.Key_Application

    def __init__(self, platformName, platformVersion, applicationName, applicationVersion):
        self._initAbcSystem(
            platformName, platformVersion,
            applicationName, applicationVersion
        )

    @property
    def platform(self):
        return self._systemObj

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Category, self.category),
                (self.Key_Name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw)
            ]
        )


class Sys_PltLanguage(abstract.Abc_System):
    SYSTEM_CLS = Sys_Platform

    object_category = lxConfigure.Basic.Category_Plt_Language

    def __init__(self, platformName, platformVersion, languageName, languageVersion):
        self._initAbcSystem(
            platformName, platformVersion,
            languageName, languageVersion
        )

    @property
    def platform(self):
        return self._systemObj

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Category, self.category),
                (self.Key_Name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw)
            ]
        )


class Sys_PltAppLanguage(abstract.Abc_System):
    SYSTEM_CLS = Sys_PltApplication

    object_category = lxConfigure.Basic.Category_Plt_App_Language

    def __init__(self, platformName, platformVersion, applicationName, applicationVersion, languageName, languageVersion):
        self._initAbcSystem(
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )

    @property
    def platform(self):
        return self._systemObj.platform

    @property
    def application(self):
        return self._systemObj

    def raw(self):
        return lxBasic.orderedDict(
            [
                (self.Key_Category, self.category),
                (self.Key_Name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw),
                (self.Key_Application, self.application.systemraw)
            ]
        )
