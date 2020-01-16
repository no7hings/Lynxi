# coding:utf-8
from LxScheme import shmCore, shmAbstract


class Sys_Platform(shmAbstract.Abc_System):
    object_category = shmCore.Basic.Category_Platform
    raw_key = shmCore.Basic.Key_Platform

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.createByRaw(args[0])
        else:
            self._initAbcSystem(*args)

    def createByRaw(self, raw):
        platformName = raw[self.Key_Name]
        platformVersion = raw[self.Key_Version]

        self._initAbcSystem(
            platformName, platformVersion
        )

    @property
    def platform(self):
        return self


class Sys_PltLanguage(shmAbstract.Abc_System):
    CLS_system = Sys_Platform

    object_category = shmCore.Basic.Category_Plf_Language

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.createByRaw(args[0])
        else:
            self._initAbcSystem(*args)

    @property
    def platform(self):
        return self._systemObj

    @property
    def language(self):
        return self

    def createByRaw(self, raw):
        platformName = raw[self.Key_Platform][self.Key_Name]
        platformVersion = raw[self.Key_Platform][self.Key_Version]
        languageName = raw[self.Key_Name]
        languageVersion = raw[self.Key_Version]

        self._initAbcSystem(
            platformName, platformVersion,
            languageName, languageVersion
        )

    def raw(self):
        return self.cls_dic_order(
            [
                (self.Key_Category, self.category),
                (self.Key_Name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw)
            ]
        )


class Sys_PltApplication(shmAbstract.Abc_System):
    CLS_system = Sys_Platform

    object_category = shmCore.Basic.Category_Plf_Application
    raw_key = shmCore.Basic.Key_Application

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.createByRaw(args[0])
        else:
            self._initAbcSystem(*args)

    @property
    def platform(self):
        return self._systemObj

    @property
    def application(self):
        return self

    def createByRaw(self, raw):
        platformName = raw[self.Key_Platform][self.Key_Name]
        platformVersion = raw[self.Key_Platform][self.Key_Version]
        applicationName = raw[self.Key_Name]
        applicationVersion = raw[self.Key_Version]

        self._initAbcSystem(
            platformName, platformVersion,
            applicationName, applicationVersion
        )

    def raw(self):
        return self.cls_dic_order(
            [
                (self.Key_Category, self.category),
                (self.Key_Name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw)
            ]
        )


class Sys_PltAppLanguage(shmAbstract.Abc_System):
    CLS_system = Sys_PltApplication

    object_category = shmCore.Basic.Category_Plf_App_Language

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.createByRaw(args[0])
        else:
            self._initAbcSystem(*args)

    @property
    def platform(self):
        return self._systemObj.platform

    @property
    def application(self):
        return self._systemObj

    @property
    def language(self):
        return self

    def createByRaw(self, raw):
        platformName = raw[self.Key_Platform][self.Key_Name]
        platformVersion = raw[self.Key_Platform][self.Key_Version]
        applicationName = raw[self.Key_Application][self.Key_Name]
        applicationVersion = raw[self.Key_Application][self.Key_Version]
        languageName = raw[self.Key_Name]
        languageVersion = raw[self.Key_Version]

        self._initAbcSystem(
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )

    def raw(self):
        return self.cls_dic_order(
            [
                (self.Key_Category, self.category),
                (self.Key_Name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw),
                (self.Key_Application, self.application.systemraw)
            ]
        )
