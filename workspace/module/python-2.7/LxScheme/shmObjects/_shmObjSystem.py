# coding:utf-8
from .. import shmCfg, shmObjAbs


class Sys_Python27(shmCfg.ShmUtility):
    def __init__(self):
        pass

    @property
    def name(self):
        return 'python'

    @property
    def version(self):
        return '2.7'


class Sys_Platform(shmObjAbs.AbsShmSystem):
    VAR_shm__system__category = shmCfg.ShmUtility.DEF_shm__rsc__category__platform
    VAR_shm__system__raw_key = shmCfg.ShmUtility.Key_Platform

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self._shm_system__set_build_(args[0])
        else:
            self._initAbsShmSystem(*args)

    def _shm_system__set_build_(self, raw):
        platformNameStr = raw[self.DEF_shm__key__name]
        platformVersionStr = raw[self.DEF_shm__key__version]

        self._initAbsShmSystem(
            platformNameStr, platformVersionStr
        )

    @property
    def platform(self):
        return self

    @property
    def language(self):
        return Sys_Python27()


class Sys_PltLanguage(shmObjAbs.AbsShmSystem):
    CLS_shm__system = Sys_Platform

    VAR_shm__system__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_language

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self._shm_system__set_build_(args[0])
        else:
            self._initAbsShmSystem(*args)

    @property
    def platform(self):
        return self._systemObj

    @property
    def language(self):
        return self

    def _shm_system__set_build_(self, raw):
        platformNameStr = raw[self.Key_Platform][self.DEF_shm__key__name]
        platformVersionStr = raw[self.Key_Platform][self.DEF_shm__key__version]
        languageNameStr = raw[self.DEF_shm__key__name]
        languageVersionStr = raw[self.DEF_shm__key__version]

        self._initAbsShmSystem(
            platformNameStr, platformVersionStr,
            languageNameStr, languageVersionStr
        )

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.DEF_shm__key__category, self.category),
                (self.DEF_shm__key__name, self.name),
                (self.DEF_shm__key__version, self.version),
                (self.Key_Platform, self.platform.systemraw)
            ]
        )


class Sys_PltApplication(shmObjAbs.AbsShmSystem):
    CLS_shm__system = Sys_Platform

    VAR_shm__system__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_application
    VAR_shm__system__raw_key = shmCfg.ShmUtility.Key_Application

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self._shm_system__set_build_(args[0])
        else:
            self._initAbsShmSystem(*args)

    @property
    def platform(self):
        return self._systemObj

    @property
    def application(self):
        return self

    @property
    def language(self):
        return Sys_Python27()

    def _shm_system__set_build_(self, raw):
        platformNameStr = raw[self.Key_Platform][self.DEF_shm__key__name]
        platformVersionStr = raw[self.Key_Platform][self.DEF_shm__key__version]
        applicationNameStr = raw[self.DEF_shm__key__name]
        applicationVersionStr = raw[self.DEF_shm__key__version]

        self._initAbsShmSystem(
            platformNameStr, platformVersionStr,
            applicationNameStr, applicationVersionStr
        )

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.DEF_shm__key__category, self.category),
                (self.DEF_shm__key__name, self.name),
                (self.DEF_shm__key__version, self.version),
                (self.Key_Platform, self.platform.systemraw)
            ]
        )


class Sys_PltAppLanguage(shmObjAbs.AbsShmSystem):
    CLS_shm__system = Sys_PltApplication

    VAR_shm__system__category = shmCfg.ShmUtility.DEF_shm__rsc__category__plf_lng_language

    def __init__(self, *args):
        if isinstance(args[0], dict):
            self._shm_system__set_build_(args[0])
        else:
            self._initAbsShmSystem(*args)

    @property
    def platform(self):
        return self._systemObj.platform

    @property
    def application(self):
        return self._systemObj

    @property
    def language(self):
        return self

    def _shm_system__set_build_(self, raw):
        platformNameStr = raw[self.Key_Platform][self.DEF_shm__key__name]
        platformVersionStr = raw[self.Key_Platform][self.DEF_shm__key__version]
        applicationNameStr = raw[self.Key_Application][self.DEF_shm__key__name]
        applicationVersionStr = raw[self.Key_Application][self.DEF_shm__key__version]
        languageNameStr = raw[self.DEF_shm__key__name]
        languageVersionStr = raw[self.DEF_shm__key__version]

        self._initAbsShmSystem(
            platformNameStr, platformVersionStr,
            applicationNameStr, applicationVersionStr,
            languageNameStr, languageVersionStr
        )

    def raw(self):
        return self.CLS_dic_order(
            [
                (self.DEF_shm__key__category, self.category),
                (self.DEF_shm__key__name, self.name),
                (self.DEF_shm__key__version, self.version),
                (self.Key_Platform, self.platform.systemraw),
                (self.Key_Application, self.application.systemraw)
            ]
        )
