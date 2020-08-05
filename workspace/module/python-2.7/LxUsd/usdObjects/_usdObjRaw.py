# coding:utf-8
from LxData import datObjAbs

from LxData.datObjects import _datObjRaw

from .. import usdCfg


class Objnamespace(datObjAbs.Abs_DatObjNamespace):
    CLS_dat__obj_path__name = _datObjRaw.Name

    CLS_dat__obj_path__objsep = usdCfg.UsdUtility.DEF_usd__node_namespace_pathsep

    def __init__(self, *args):
        self._initAbsDatObjNamespace(*args)


class Objname(datObjAbs.Abs_DatObjName):
    CLS_dat__obj_name__namespace = Objnamespace
    CLS_dat__obj_name__name = _datObjRaw.Name

    def __init__(self, *args):
        self._initAbsDatObjName(*args)


class Portpath(datObjAbs.Abs_DatObjPath):
    CLS_dat__obj_path__name = _datObjRaw.ObjName

    CLS_dat__obj_path__objsep = usdCfg.UsdUtility.DEF_usd__node_port_pathsep

    def __init__(self, *args):
        self._initAbsDatObjPath(*args)


class Nodepath(datObjAbs.Abs_DatObjPath):
    CLS_dat__obj_path__name = _datObjRaw.ObjName

    CLS_dat__obj_path__objsep = usdCfg.UsdUtility.DEF_usd__node_pathsep

    def __init__(self, *args):
        self._initAbsDatObjPath(*args)


class Attrpath(datObjAbs.Abs_DatObjComppath):
    CLS_dat__comppath__nodepath = Nodepath
    CLS_dat__comppath__portpath = Portpath

    def __init__(self, *args):
        self._initAbsDatObjComppath(*args)
