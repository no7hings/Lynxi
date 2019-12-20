# coding:utf-8
from LxCore.definition import abstract


class Pth_Root(abstract.Abc_PthRoot):
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


class Pth_Directory(abstract.Abc_PthDirectory):
    ROOT_CLS = Pth_Root

    def __init__(self, *args):
        self._initAbcPthDirectory(*args)
