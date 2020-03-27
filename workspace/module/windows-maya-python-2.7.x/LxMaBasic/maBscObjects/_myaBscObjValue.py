# coding:utf-8
from LxMaBasic import myaBscObjCore


class Value(myaBscObjCore.Abc_MyaValue):
    def __init__(self, raw):
        self._initAbcMyaValue(raw)
