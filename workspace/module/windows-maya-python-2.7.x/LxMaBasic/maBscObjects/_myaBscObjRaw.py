# coding:utf-8
from LxBasic import bscObjCore

from LxGraphic.grhObjects import _grhObjRaw

from LxMaBasic import myaBscConfigure, myaBscObjCore


class NodeName(myaBscObjCore.Abc_MyaNodeString):
    VAR_bsc_namespace_separator = myaBscConfigure.Utility.DEF_mya_namespace_separator
    VAR_bsc_node_separator = myaBscConfigure.Utility.DEF_mya_node_separator

    def __init__(self, nodepathString):
        self._initAbcMyaNodeString(nodepathString)


class PortnameString(myaBscObjCore.Abc_MyaPortString):
    VAR_bsc_port_separator = myaBscConfigure.Utility.DEF_mya_port_separator

    def __init__(self, portpathString):
        self._initAbcMyaPortString(portpathString)


class NodeSet(myaBscObjCore.Abs_MyaObjSet):
    def __init__(self, *args):
        self._initAbsMyaObjSet(*args)


class PortSet(myaBscObjCore.Abs_MyaObjSet):
    def __init__(self, *args):
        self._initAbsMyaObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.portpathString()


# ******************************************************************************************************************** #

class Name(bscObjCore.Abs_BscName):
    VAR_bsc_rawtype = str

    def __init__(self, *args):
        self._initAbsBscName(*args)


class Portpath(bscObjCore.Abs_BscObjpath):
    CLS_bsc_raw = _grhObjRaw.Name

    VAR_bsc_pathsep = myaBscConfigure.Utility.DEF_mya_port_separator

    def __init__(self, *args):
        self._initAbsBscObjpath(*args)


class Nodename(bscObjCore.Abs_BscNodename):
    CLS_bsc_raw = _grhObjRaw.Name

    VAR_bsc_namesep = u':'

    def __init__(self, *args):
        self._initAbsBscNodename(*args)


class Nodepath(bscObjCore.Abs_BscObjpath):
    CLS_bsc_raw = Nodename

    VAR_bsc_pathsep = myaBscConfigure.Utility.DEF_mya_node_separator

    def __init__(self, *args):
        self._initAbsBscObjpath(*args)
