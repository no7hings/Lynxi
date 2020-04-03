# coding:utf-8
from LxData.datObjects import _datObjString

from .. import myaBscObjCore

from ..maBscObjects import _myaBscObjRaw, _myaBscObjQuery


class Connection(myaBscObjCore.Abc_MyaConnection):
    def __init__(self, *args):
        self._initAbcMyaConnection(*args)


class Port(myaBscObjCore.Abs_MyaPort):
    CLS_grh_porttype = _datObjString.Porttype

    CLS_grh_portpath = _myaBscObjRaw.Portpath

    OBJ_grh_query_cache = _myaBscObjQuery.OBJ_grh_query_cache
    OBJ_grh_obj_cache = _myaBscObjQuery.OBJ_grh_obj_cache

    def __init__(self, *args):
        self._initAbsMyaPort(*args)
