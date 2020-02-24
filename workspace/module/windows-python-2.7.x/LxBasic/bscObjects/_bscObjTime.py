# coding:utf-8
from LxBasic import bscMtdCore, bscObjCore


class Timestamp(bscObjCore.Abc_BscTime):
    def __init__(self, timestamp):
        self._initAbcTime(timestamp)


class ActiveTimestamp(bscObjCore.Abc_BscTime):
    def __init__(self):
        self._initAbcTime(self._getSystemActiveTimestamp())
