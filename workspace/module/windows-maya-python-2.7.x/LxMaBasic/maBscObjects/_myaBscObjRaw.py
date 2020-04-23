# coding:utf-8
from LxData import datObjAbs

from LxData.datObjects import _datObjRaw

from ..import myaBscCfg


class Namespace(datObjAbs.Abs_DatNamespace):
    CLS_dat_name = _datObjRaw.Name

    VAR_dat_pathsep = myaBscCfg.Utility.DEF_mya_namespace_pathsep

    def __init__(self, *args):
        self._initAbsDatNamespace(*args)


class Nodename(datObjAbs.Abs_DatNodename):
    CLS_dat_namespace = Namespace
    CLS_dat_name = _datObjRaw.Name

    VAR_dat_namesep = myaBscCfg.Utility.DEF_mya_namespace_pathsep

    def __init__(self, *args):
        self._initAbsDatNodename(*args)


class Portpath(datObjAbs.Abs_DatPath):
    CLS_dat_name = _datObjRaw.Name

    VAR_dat_pathsep = myaBscCfg.Utility.DEF_mya_port_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)


class Nodepath(datObjAbs.Abs_DatPath):
    CLS_dat_name = _datObjRaw.Nodename

    VAR_dat_pathsep = myaBscCfg.Utility.DEF_mya_node_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)


class Attrpath(datObjAbs.Abs_DatAttrpath):
    CLS_dat_raw = unicode

    CLS_dat_nodepath = Nodepath
    CLS_dat_portpath = Portpath

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        self._initAbsDatAttrpath(*args)
