# coding:utf-8
from LxBasic import bscObjCore

from LxMaBasic import maBscConfigure, maBscObjCore


class NodeName(bscObjCore.Abc_BscDccNodeString):
    VAR_bsc_namespace_separator = maBscConfigure.Utility.DEF_mya_namespace_separator
    VAR_bsc_node_separator = maBscConfigure.Utility.DEF_mya_node_separator

    def __init__(self, nodeString):
        self._initAbcBscDccNodeString(nodeString)


class PortString(bscObjCore.Abc_BscDccPortString):
    VAR_bsc_port_separator = maBscConfigure.Utility.DEF_mya_port_separator

    def __init__(self, portString):
        self._initAbcBscDccPortString(portString)


class ObjectSet(maBscObjCore.Abc_MyaObjectSet):
    def __init__(self, *args):
        self._initAbcMyaObjectSet(*args)
