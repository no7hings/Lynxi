# coding:utf-8
from LxData import datObjAbs

from LxData.datObjects import _datObjString

from ..import myaBscCfg


class Nodename(datObjAbs.Abs_DatNodename):
    CLS_dat_raw = unicode

    CLS_dat_namespace = _datObjString.Name
    CLS_dat_name = _datObjString.Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_namesep = myaBscCfg.Utility.DEF_mya_namespace_separator

    def __init__(self, *args):
        self._initAbsDatNodename(*args)


class Portpath(datObjAbs.Abs_DatPath):
    CLS_dat_name = _datObjString.Portname

    VAR_dat_pathsep = myaBscCfg.Utility.DEF_mya_port_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)


class Nodepath(datObjAbs.Abs_DatPath):
    CLS_dat_name = _datObjString.Nodename

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
