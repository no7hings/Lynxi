# coding:utf-8
from LxBasic import bscConfigure, bscAbstract


class Path(bscAbstract.Abc_DccPath):
    separator_namespace = ':'
    separator_node = '|'
    separator_attribute = '.'

    def __init__(self, pathString):
        self._initAbcDccPath(pathString)
