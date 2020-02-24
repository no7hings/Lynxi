# coding:utf-8
from LxMaBasic import maBscObjCore

from LxMaBasic.maBscObjects import _maBscObjRaw


class Attribute(maBscObjCore.Abc_MaAttribute):
    CLS_maya_string_port = _maBscObjRaw.PortString

    def __init__(self, nodeObject, name):
        self._initAbcMaAttribute(nodeObject, name)


class Connection(maBscObjCore.Abc_MaConnection):
    def __init__(self, sourceAttributeObject, targetAttributeObject):
        self._initAbcMaConnection(sourceAttributeObject, targetAttributeObject)
