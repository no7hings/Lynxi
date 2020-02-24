# coding:utf-8
from LxMaBasic import maBscObjCore

from LxMaBasic.maBscObjects import _maBscObjRaw, _maBscObjValue


class Attribute(maBscObjCore.Abc_MaAttribute):
    CLS_mya_port_string = _maBscObjRaw.PortString
    CLS_mya_value = _maBscObjValue.Value

    def __init__(self, nodeObject, name):
        self._initAbcMaAttribute(nodeObject, name)


class Connection(maBscObjCore.Abc_MaConnection):
    def __init__(self, sourceAttributeObject, targetAttributeObject):
        self._initAbcMaConnection(sourceAttributeObject, targetAttributeObject)
