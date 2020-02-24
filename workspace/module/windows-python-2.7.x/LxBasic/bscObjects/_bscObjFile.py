# coding:utf-8
from LxBasic import bscObjCore

from LxBasic.bscMethods import _bscMtdFile


class OsFile(bscObjCore.Abc_BscFile):
    def __init__(self, fileString):
        self._initAbcBscFile(fileString)

    def read(self, readLines=False):
        return _bscMtdFile.OsFile.read(self._fileString)

    def write(self, raw):
        _bscMtdFile.OsFile.write(self._fileString, raw)


class OsJsonFile(bscObjCore.Abc_BscFile):
    def __init__(self, fileString):
        self._initAbcBscFile(fileString)

    def read(self, encoding=None):
        return _bscMtdFile.OsJsonFile.read(self._fileString)

    def write(self, raw, indent=4, ensure_ascii=True):
        _bscMtdFile.OsJsonFile.write(self._fileString, raw, indent, ensure_ascii)
