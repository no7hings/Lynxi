# coding:utf-8
from LxBasic import bscConfigure
from LxScheme import shmConfigure, shmObjCore


class Pth_Root(shmObjCore.Abc_ShmRoot):
    environ_key_local = bscConfigure.Utility.DEF_key_environ_path_local
    environ_key_develop = bscConfigure.Utility.DEF_key_environ_path_develop
    environ_key_product = bscConfigure.Utility.DEF_key_environ_path_product

    VAR_path_default_develop = 'e:/myworkspace/td/lynxi'
    VAR_path_default_product = 'e:/myworkspace/td/lynxi'
    VAR_path_default_local = 'c:/.lynxi'

    def __init__(self):
        self._initAbcPthRoot()

    def _activePath(self):
        return self._serverPath()

    def _serverPath(self):
        if self.isDevelop():
            return self._developPath()
        return self._productPath()

    def _workspacePath(self):
        return self._developPath()


class Pth_IconRoot(shmObjCore.Abc_ShmRoot):
    environ_key_local = bscConfigure.Utility.DEF_key_environ_path_local
    environ_key_develop = bscConfigure.Utility.DEF_key_environ_path_develop
    environ_key_product = bscConfigure.Utility.DEF_key_environ_path_product

    VAR_path_default_develop = 'e:/myworkspace/td/lynxi'
    VAR_path_default_product = 'e:/myworkspace/td/lynxi'
    VAR_path_default_local = 'c:/.lynxi'

    def __init__(self):
        self._initAbcPthRoot()

    def _activePath(self):
        return self._serverPath()

    def _serverPath(self):
        if self.isDevelop():
            return self._developPath()
        return self._productPath()

    def _workspacePath(self):
        return self._developPath()


class Pth_PresetRoot(shmObjCore.Abc_ShmRoot):
    environ_key_local = bscConfigure.Utility.DEF_key_environ_path_local
    environ_key_develop = bscConfigure.Utility.DEF_key_environ_path_develop
    environ_key_product = shmConfigure.Utility.Environ_Key_Path_Preset

    VAR_path_default_develop = 'e:/myworkspace/td/lynxi'
    VAR_path_default_product = 'e:/myworkspace/td/lynxi'
    VAR_path_default_local = 'c:/.lynxi'

    def __init__(self):
        self._initAbcPthRoot()

    def _activePath(self):
        return self._serverPath()

    def _serverPath(self):
        return self._productPath()

    def _workspacePath(self):
        return self._developPath()


class Pth_ToolkitRoot(shmObjCore.Abc_ShmRoot):
    environ_key_local = bscConfigure.Utility.DEF_key_environ_path_local
    environ_key_develop = bscConfigure.Utility.DEF_key_environ_path_develop
    environ_key_product = shmConfigure.Utility.Environ_Key_Path_Toolkit

    VAR_path_default_develop = 'e:/myworkspace/td/lynxi'
    VAR_path_default_product = 'e:/myworkspace/td/lynxi'
    VAR_path_default_local = 'c:/.lynxi'

    def __init__(self):
        self._initAbcPthRoot()

    def _activePath(self):
        return self._serverPath()

    def _serverPath(self):
        return self._productPath()

    def _workspacePath(self):
        return self._developPath()


class OsDirectory(shmObjCore.Abc_ShmDirectory):
    CLS_path_root = Pth_Root

    def __init__(self, *args):
        self._initAbcPthDirectory(*args)


class Pth_IconDirectory(shmObjCore.Abc_ShmDirectory):
    CLS_path_root = Pth_IconRoot

    def __init__(self):
        self._initAbcPthDirectory('icon')
