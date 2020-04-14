# coding:utf-8
from ..import datCfg, datObjAbs

from . import _datObjString


class Portpath(datObjAbs.Abs_DatPath):
    CLS_dat_raw = unicode

    CLS_dat_dirname = _datObjString.Name
    CLS_dat_bscname = _datObjString.Name

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = datCfg.Utility.DEF_dat_port_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)


class Nodepath(datObjAbs.Abs_DatPath):
    CLS_dat_raw = unicode

    CLS_dat_dirname = _datObjString.Nodename
    CLS_dat_bscname = _datObjString.Nodename

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = datCfg.Utility.DEF_dat_node_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)


class Filepath(datObjAbs.Abs_DatPath):
    CLS_dat_raw = unicode

    CLS_dat_dirname = _datObjString.Name
    CLS_dat_bscname = _datObjString.Filename

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    VAR_dat_pathsep = datCfg.Utility.DEF_dat_file_pathsep

    def __init__(self, *args):
        self._initAbsDatPath(*args)
