# coding:utf-8
from LxBasic import bscConfigure
from LxScheme import shmCore, shmObjAbstract


class Pth_Root(shmObjAbstract.Abc_PthRoot):
    environ_key_local = bscConfigure.MtdBasic.STR_key_environ_path_local
    environ_key_develop = bscConfigure.MtdBasic.STR_key_environ_path_develop
    environ_key_product = bscConfigure.MtdBasic.STR_key_environ_path_product

    path_default_develop = 'e:/myworkspace/td/lynxi'
    path_default_product = 'e:/myworkspace/td/lynxi'
    path_default_local = 'c:/.lynxi'

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


class Pth_IconRoot(shmObjAbstract.Abc_PthRoot):
    environ_key_local = bscConfigure.MtdBasic.STR_key_environ_path_local
    environ_key_develop = bscConfigure.MtdBasic.STR_key_environ_path_develop
    environ_key_product = bscConfigure.MtdBasic.STR_key_environ_path_product

    path_default_develop = 'e:/myworkspace/td/lynxi'
    path_default_product = 'e:/myworkspace/td/lynxi'
    path_default_local = 'c:/.lynxi'

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


class Pth_PresetRoot(shmObjAbstract.Abc_PthRoot):
    environ_key_local = bscConfigure.MtdBasic.STR_key_environ_path_local
    environ_key_develop = bscConfigure.MtdBasic.STR_key_environ_path_develop
    environ_key_product = shmCore.Basic.Environ_Key_Path_Preset

    path_default_develop = 'e:/myworkspace/td/lynxi'
    path_default_product = 'e:/myworkspace/td/lynxi'
    path_default_local = 'c:/.lynxi'

    def __init__(self):
        self._initAbcPthRoot()

    def _activePath(self):
        return self._serverPath()

    def _serverPath(self):
        return self._productPath()

    def _workspacePath(self):
        return self._developPath()


class Pth_ToolkitRoot(shmObjAbstract.Abc_PthRoot):
    environ_key_local = bscConfigure.MtdBasic.STR_key_environ_path_local
    environ_key_develop = bscConfigure.MtdBasic.STR_key_environ_path_develop
    environ_key_product = shmCore.Basic.Environ_Key_Path_Toolkit

    path_default_develop = 'e:/myworkspace/td/lynxi'
    path_default_product = 'e:/myworkspace/td/lynxi'
    path_default_local = 'c:/.lynxi'

    def __init__(self):
        self._initAbcPthRoot()

    def _activePath(self):
        return self._serverPath()

    def _serverPath(self):
        return self._productPath()

    def _workspacePath(self):
        return self._developPath()


class Pth_Directory(shmObjAbstract.Abc_PthDirectory):
    CLS_path_root = Pth_Root

    def __init__(self, *args):
        self._initAbcPthDirectory(*args)


class Pth_IconDirectory(shmObjAbstract.Abc_PthDirectory):
    CLS_path_root = Pth_IconRoot

    def __init__(self):
        self._initAbcPthDirectory('icon')
