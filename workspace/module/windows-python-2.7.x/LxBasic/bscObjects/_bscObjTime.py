# coding:utf-8
from LxBasic import bscMtdCore, bscObjCore


class Timestamp(bscObjCore.Abc_BscTime):
    def __init__(self, timestamp):
        self._initAbcBscTime(timestamp)


class ActiveTimestamp(bscObjCore.Abc_BscTime):
    def __init__(self):
        self._initAbcBscTime(self._getSystemActiveTimestamp())
