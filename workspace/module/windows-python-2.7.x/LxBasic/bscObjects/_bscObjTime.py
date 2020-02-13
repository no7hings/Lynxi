# coding:utf-8
from LxBasic import bscCore, bscObjAbstract


class Time(bscObjAbstract.Abc_Time):
    def __init__(self, timestamp):
        self._initAbcTime(timestamp)


class ActiveTime(bscObjAbstract.Abc_Time):
    def __init__(self):
        self._initAbcTime(self._getSystemActiveTimestamp())
