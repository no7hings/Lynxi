# coding:utf-8
from LxData import datObjAbs

from LxData.datObjects import _datObjString

from ..import myaBscCfg


class Portpath(datObjAbs.Abs_DatPath):
    CLS_dat_raw = unicode

    CLS_dat_dirname = _datObjString.Name
    CLS_dat_bscname = _datObjString.Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = myaBscCfg.Utility.DEF_mya_port_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)


class Nodename(datObjAbs.Abs_DatNodename):
    CLS_dat_raw = unicode

    CLS_dat_namespace = _datObjString.Name
    CLS_dat_name = _datObjString.Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_namesep = myaBscCfg.Utility.DEF_mya_namespace_separator

    def __init__(self, *args):
        self._initAbsDatNodename(*args)


class Nodepath(datObjAbs.Abs_DatPath):
    CLS_dat_raw = unicode

    CLS_dat_dirname = _datObjString.Nodename
    CLS_dat_bscname = _datObjString.Nodename

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = myaBscCfg.Utility.DEF_mya_node_separator

    def __init__(self, *args):
        self._initAbsDatPath(*args)
