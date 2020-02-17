# coding:utf-8
from LxMaBasic import maBscObjAbstract


class Node(maBscObjAbstract.Abc_Node):
    def __init__(self, fullpathNameString):
        self._initAbcNode(fullpathNameString)


class Geometry(maBscObjAbstract.Abc_Node):
    def __init__(self, fullpathNameString):
        self._initAbcNode(fullpathNameString)
