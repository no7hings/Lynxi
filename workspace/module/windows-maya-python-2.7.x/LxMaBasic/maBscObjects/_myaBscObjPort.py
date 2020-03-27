# coding:utf-8
from LxGraphic.grhObjects import _grhObjRaw

from LxMaBasic import myaBscObjCore

from LxMaBasic.maBscObjects import _myaBscObjRaw, _myaBscObjValue


class Port(myaBscObjCore.Abc_MyaPort):
    CLS_grh_portpath = _myaBscObjRaw.PortnameString
    CLS_mya_value = _myaBscObjValue.Value

    def __init__(self, *args):
        self._initAbcMyaPort(*args)


class Connection(myaBscObjCore.Abc_MyaConnection):
    def __init__(self, *args):
        self._initAbcMyaConnection(*args)


class Port_(myaBscObjCore.Abs_MyaPort):
    CLS_grh_porttype = _grhObjRaw.Porttype

    CLS_grh_portpath = _myaBscObjRaw.Portpath

    def __init__(self, *args):
        self._initAbsMyaPort(*args)
