# coding:utf-8
from LxMaBasic import maBscObjCore

from LxMaBasic.maBscObjects import _maBscObjRaw, _maBscObjValue


class Attribute(maBscObjCore.Abc_MyaPort):
    CLS_mya_port_string = _maBscObjRaw.PortString
    CLS_mya_value = _maBscObjValue.Value

    def __init__(self, *args):
        self._initAbcMyaPort(*args)


class Connection(maBscObjCore.Abc_MyaConnection):
    def __init__(self, *args):
        self._initAbcMyaConnection(*args)
