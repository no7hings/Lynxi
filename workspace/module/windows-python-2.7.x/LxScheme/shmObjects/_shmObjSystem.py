# coding:utf-8
from LxScheme import shmConfigure, shmObjCore


class Sys_Platform(shmObjCore.Abc_ShmSystem):
    VAR_shm_object_category = shmConfigure.Utility.Category_Platform
    VAR_shm_raw_key = shmConfigure.Utility.Key_Platform

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.createByRaw(args[0])
        else:
            self._initAbcShmSystem(*args)

    def createByRaw(self, raw):
        platformName = raw[self.DEF_key_name]
        platformVersion = raw[self.Key_Version]

        self._initAbcShmSystem(
            platformName, platformVersion
        )

    @property
    def platform(self):
        return self


class Sys_PltLanguage(shmObjCore.Abc_ShmSystem):
    CLS_shm_system = Sys_Platform

    VAR_shm_object_category = shmConfigure.Utility.Category_Plf_Language

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.createByRaw(args[0])
        else:
            self._initAbcShmSystem(*args)

    @property
    def platform(self):
        return self._systemObj

    @property
    def language(self):
        return self

    def createByRaw(self, raw):
        platformName = raw[self.Key_Platform][self.DEF_key_name]
        platformVersion = raw[self.Key_Platform][self.Key_Version]
        languageName = raw[self.DEF_key_name]
        languageVersion = raw[self.Key_Version]

        self._initAbcShmSystem(
            platformName, platformVersion,
            languageName, languageVersion
        )

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.Key_Category, self.category),
                (self.DEF_key_name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw)
            ]
        )


class Sys_PltApplication(shmObjCore.Abc_ShmSystem):
    CLS_shm_system = Sys_Platform

    VAR_shm_object_category = shmConfigure.Utility.Category_Plf_Application
    VAR_shm_raw_key = shmConfigure.Utility.Key_Application

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.createByRaw(args[0])
        else:
            self._initAbcShmSystem(*args)

    @property
    def platform(self):
        return self._systemObj

    @property
    def application(self):
        return self

    def createByRaw(self, raw):
        platformName = raw[self.Key_Platform][self.DEF_key_name]
        platformVersion = raw[self.Key_Platform][self.Key_Version]
        applicationName = raw[self.DEF_key_name]
        applicationVersion = raw[self.Key_Version]

        self._initAbcShmSystem(
            platformName, platformVersion,
            applicationName, applicationVersion
        )

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.Key_Category, self.category),
                (self.DEF_key_name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw)
            ]
        )


class Sys_PltAppLanguage(shmObjCore.Abc_ShmSystem):
    CLS_shm_system = Sys_PltApplication

    VAR_shm_object_category = shmConfigure.Utility.Category_Plf_App_Language

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self.createByRaw(args[0])
        else:
            self._initAbcShmSystem(*args)

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
        platformName = raw[self.Key_Platform][self.DEF_key_name]
        platformVersion = raw[self.Key_Platform][self.Key_Version]
        applicationName = raw[self.Key_Application][self.DEF_key_name]
        applicationVersion = raw[self.Key_Application][self.Key_Version]
        languageName = raw[self.DEF_key_name]
        languageVersion = raw[self.Key_Version]

        self._initAbcShmSystem(
            platformName, platformVersion,
            applicationName, applicationVersion,
            languageName, languageVersion
        )

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.Key_Category, self.category),
                (self.DEF_key_name, self.name),
                (self.Key_Version, self.version),
                (self.Key_Platform, self.platform.systemraw),
                (self.Key_Application, self.application.systemraw)
            ]
        )
