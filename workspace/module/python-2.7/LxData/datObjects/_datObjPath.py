# coding:utf-8
from .. import datCfg, datObjAbs

from . import _datObjRaw


class Typepath(datObjAbs.AbsDatObjPath):
    CLS_dat__obj_path__name = _datObjRaw.ObjTypename

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__node_type_pathsep

    def __init__(self, *args):
        self._initAbsDatObjPath(*args)


class Portpath(datObjAbs.AbsDatObjPath):
    CLS_dat__obj_path__name = _datObjRaw.ObjName

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__node_port_pathsep

    def __init__(self, *args):
        self._initAbsDatObjPath(*args)


class Nodepath(datObjAbs.AbsDatObjPath):
    CLS_dat__obj_path__name = _datObjRaw.ObjName

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__node_pathsep

    def __init__(self, *args):
        self._initAbsDatObjPath(*args)


class Attrpath(datObjAbs.AbsDatObjComppath):
    CLS_dat__comppath__nodepath = Nodepath
    CLS_dat__comppath__portpath = Portpath

    def __init__(self, *args):
        self._initAbsDatObjComppath(*args)


class Filepath(datObjAbs.AbsDatObjPath):
    CLS_dat__obj_path__name = _datObjRaw.Filename

    CLS_dat__obj_path__objsep = datCfg.DatUtility.DEF_dat__file_pathsep

    def __init__(self, *args):
        self._initAbsDatObjPath(*args)
