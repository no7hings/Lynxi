# coding:utf-8
from LxData.datObjects import _datObjString

from ..import myaBscObjAbs

from ..maBscObjects import _myaBscObjRaw, _myaBscObjQuery


class Connection(myaBscObjAbs.Abc_MyaConnection):
    def __init__(self, *args):
        self._initAbcMyaConnection(*args)


class Port(myaBscObjAbs.Abs_MyaPort):
    CLS_grh_type = _datObjString.Type
    CLS_grh_porttype = _datObjString.Porttype

    CLS_grh_portpath = _myaBscObjRaw.Portpath

    def __init__(self, *args):
        self._initAbsMyaPort(*args)
