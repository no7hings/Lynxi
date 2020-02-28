# coding:utf-8
from LxMaBasic import maBscObjCore

from LxMaBasic.maBscObjects import _maBscObjRaw, _maBscObjValue


class Channel(maBscObjCore.Abc_MaChannel):
    def __init__(self, *args):
        self._initAbcMaChannel(*args)


class Attribute(maBscObjCore.Abc_MaAttribute):
    CLS_mya_port_string = _maBscObjRaw.PortString
    CLS_mya_channel_set = _maBscObjRaw.ObjectSet
    CLS_mya_channel = Channel
    CLS_mya_value = _maBscObjValue.Value

    def __init__(self, *args):
        self._initAbcMaAttribute(*args)


class Connection(maBscObjCore.Abc_MaConnection):
    def __init__(self, *args):
        self._initAbcMaConnection(*args)
