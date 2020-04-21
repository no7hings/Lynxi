# coding:utf-8
from ..import datCfg, datObjAbs

from . import _datObjString


class Portpath(datObjAbs.Abs_DatPath):
    CLS_dat_name = _datObjString.Portname

    VAR_dat_pathsep = datCfg.Utility.DEF_dat_port_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)


class Nodepath(datObjAbs.Abs_DatPath):
    CLS_dat_name = _datObjString.Nodename

    VAR_dat_pathsep = datCfg.Utility.DEF_dat_node_pathsep

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


class Filepath(datObjAbs.Abs_DatPath):
    CLS_dat_name = _datObjString.Filename

    VAR_dat_pathsep = datCfg.Utility.DEF_dat_file_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)
