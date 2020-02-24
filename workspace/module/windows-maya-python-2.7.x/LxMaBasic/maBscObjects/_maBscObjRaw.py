# coding:utf-8
from LxBasic import bscObjCore

from LxMaBasic import maBscObjCore


class NodeName(bscObjCore.Abc_BscDccNodeString):
    VAR_separator_namespace = ':'
    VAR_separator_node = '|'

    def __init__(self, nodeString):
        self._initAbcDccNodeString(nodeString)


class PortString(bscObjCore.Abc_BscDccPortString):
    VAR_separator_port = '.'

    def __init__(self, portString):
        self._initAbcDccPortString(portString)


class ObjectSet(maBscObjCore.Abc_MaObjectSet):
    def __init__(self, *args):
        self._initAbcMaObjectSet(*args)
