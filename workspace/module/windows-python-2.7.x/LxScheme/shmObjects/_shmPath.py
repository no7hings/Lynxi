# coding:utf-8
from LxScheme import shmConfigure, shmAbstract


class Pth_Root(shmAbstract.Abc_PthRoot):
    environ_key_local = shmConfigure.Basic.Environ_Key_Path_Local
    environ_key_develop = shmConfigure.Basic.Environ_Key_Path_Develop
    environ_key_product = shmConfigure.Basic.Environ_Key_Path_Product

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


class Pth_ToolkitRoot(shmAbstract.Abc_PthRoot):
    environ_key_local = shmConfigure.Basic.Environ_Key_Path_Local
    environ_key_develop = shmConfigure.Basic.Environ_Key_Path_Develop
    environ_key_product = shmConfigure.Basic.Environ_Key_Path_Product

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


class Pth_IconRoot(shmAbstract.Abc_PthRoot):
    environ_key_local = shmConfigure.Basic.Environ_Key_Path_Local
    environ_key_develop = shmConfigure.Basic.Environ_Key_Path_Develop
    environ_key_product = shmConfigure.Basic.Environ_Key_Path_Product

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


class Pth_PresetRoot(shmAbstract.Abc_PthRoot):
    environ_key_local = shmConfigure.Basic.Environ_Key_Path_Local
    environ_key_develop = shmConfigure.Basic.Environ_Key_Path_Develop
    environ_key_product = shmConfigure.Basic.Environ_Key_Path_Product

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


class Pth_Directory(shmAbstract.Abc_PthDirectory):
    ROOT_CLS = Pth_Root

    def __init__(self, *args):
        self._initAbcPthDirectory(*args)


class Pth_IconDirectory(shmAbstract.Abc_PthDirectory):
    ROOT_CLS = Pth_IconRoot

    def __init__(self):
        self._initAbcPthDirectory('icon')
