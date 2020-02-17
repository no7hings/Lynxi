# coding:utf-8
from LxBasic import bscCore, bscAbstract


class Timestamp(bscAbstract.Abc_Time):
    def __init__(self, timestamp):
        self._initAbcTime(timestamp)


class ActiveTimestamp(bscAbstract.Abc_Time):
    def __init__(self):
        self._initAbcTime(self._getSystemActiveTimestamp())
