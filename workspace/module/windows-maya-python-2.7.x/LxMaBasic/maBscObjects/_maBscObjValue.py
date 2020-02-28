# coding:utf-8
from LxMaBasic import maBscObjCore


class Value(maBscObjCore.Abc_MaValue):
    def __init__(self, raw):
        self._initAbcMaValue(raw)
