# coding:utf-8
from LxMaBasic import maBscMethods

from LxMaBasic.maBscObjects import _maBscObjPath


class Abc_Node(object):
    def _initAbcNode(self, nodeFullpathName):
        self._pathObj = _maBscObjPath.Path(nodeFullpathName)

    def isExist(self):
        return maBscMethods.Node.isExist(self.fullpathName())

    def path(self):
        return self._pathObj

    def fullpathName(self):
        return self.path().fullpathName()

    def name(self):
        return self.path().name()


class Abc_Geometry(Abc_Node):
    pass
