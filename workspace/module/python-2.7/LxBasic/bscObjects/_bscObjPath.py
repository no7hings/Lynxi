# coding:utf-8
from LxBasic import bscObjAbs


class OsDirectory(bscObjAbs.Abc_BscPath):
    def __init__(self, directoryString):
        assert isinstance(directoryString, str) or isinstance(directoryString, unicode), u'Argument: "fileString" must be "str" or "unicode".'
        self._directoryString = self._osPathToPythonStyle(directoryString)

    def __str__(self):
        return self._directoryString
