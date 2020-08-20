# coding:utf-8
from LxBasic import bscCfg

from .. import shmCfg, shmObjAbs


class Pth_Root(shmObjAbs.AbsShmRoot):
    DEF_shm__root__key_local = bscCfg.BscUtility.DEF_util__environ_key__path_local
    DEF_shm__root__key_develop = bscCfg.BscUtility.DEF_util__environ_key__path_develop
    DEF_shm__root__key_product = bscCfg.BscUtility.DEF_util__environ_key__path_product

    DEF_util__root__default_develop = shmCfg.ShmRootDefaultValue.develop
    DEF_util__root__default_product = shmCfg.ShmRootDefaultValue.product
    DEF_util__root__default_local = shmCfg.ShmRootDefaultValue.local

    def __init__(self):
        self._initAbsShmRoot()

    def _shm__path__get_active_path_str_(self):
        return self._shm__path__get_server_path_str_()

    def _shm__path__get_server_path_str_(self):
        if self.isDevelop():
            return self._shm__path__get_develop_path_str_()
        return self._shm__path__get_product_path_str_()

    def _shm__path__get_workspace_path_str_(self):
        return self._shm__path__get_develop_path_str_()


class Pth_IconRoot(shmObjAbs.AbsShmRoot):
    DEF_shm__root__key_local = bscCfg.BscUtility.DEF_util__environ_key__path_local
    DEF_shm__root__key_develop = bscCfg.BscUtility.DEF_util__environ_key__path_develop
    DEF_shm__root__key_product = bscCfg.BscUtility.DEF_util__environ_key__path_product

    DEF_util__root__default_develop = shmCfg.ShmRootDefaultValue.develop
    DEF_util__root__default_product = shmCfg.ShmRootDefaultValue.product
    DEF_util__root__default_local = shmCfg.ShmRootDefaultValue.local

    def __init__(self):
        self._initAbsShmRoot()

    def _shm__path__get_active_path_str_(self):
        return self._shm__path__get_server_path_str_()

    def _shm__path__get_server_path_str_(self):
        if self.isDevelop():
            return self._shm__path__get_develop_path_str_()
        return self._shm__path__get_product_path_str_()

    def _shm__path__get_workspace_path_str_(self):
        return self._shm__path__get_develop_path_str_()


class Pth_PresetRoot(shmObjAbs.AbsShmRoot):
    DEF_shm__root__key_local = bscCfg.BscUtility.DEF_util__environ_key__path_local
    DEF_shm__root__key_develop = bscCfg.BscUtility.DEF_util__environ_key__path_develop
    DEF_shm__root__key_product = shmCfg.ShmUtility.DEF_util__environ_key__path_preset

    DEF_util__root__default_develop = shmCfg.ShmRootDefaultValue.develop
    DEF_util__root__default_product = shmCfg.ShmRootDefaultValue.product
    DEF_util__root__default_local = shmCfg.ShmRootDefaultValue.local

    def __init__(self):
        self._initAbsShmRoot()

    def _shm__path__get_active_path_str_(self):
        return self._shm__path__get_server_path_str_()

    def _shm__path__get_server_path_str_(self):
        return self._shm__path__get_product_path_str_()

    def _shm__path__get_workspace_path_str_(self):
        return self._shm__path__get_develop_path_str_()


class Pth_KitRoot(shmObjAbs.AbsShmRoot):
    DEF_shm__root__key_local = bscCfg.BscUtility.DEF_util__environ_key__path_local
    DEF_shm__root__key_develop = bscCfg.BscUtility.DEF_util__environ_key__path_develop
    DEF_shm__root__key_product = shmCfg.ShmUtility.DEF_util__environ_key__path_kit

    DEF_util__root__default_develop = shmCfg.ShmRootDefaultValue.develop
    DEF_util__root__default_product = shmCfg.ShmRootDefaultValue.product
    DEF_util__root__default_local = shmCfg.ShmRootDefaultValue.local

    def __init__(self):
        self._initAbsShmRoot()

    def _shm__path__get_active_path_str_(self):
        return self._shm__path__get_server_path_str_()

    def _shm__path__get_server_path_str_(self):
        if self.isDevelop():
            return self._shm__path__get_develop_path_str_()
        return self._shm__path__get_product_path_str_()

    def _shm__path__get_workspace_path_str_(self):
        return self._shm__path__get_develop_path_str_()


class OsDirectory(shmObjAbs.AbsShmDirectory):
    CLS_shm__root = Pth_Root

    def __init__(self, *args):
        self._initAbsShmDirectory(*args)


class Pth_IconDirectory(shmObjAbs.AbsShmDirectory):
    CLS_shm__root = Pth_IconRoot

    def __init__(self):
        self._initAbsShmDirectory('icon')
