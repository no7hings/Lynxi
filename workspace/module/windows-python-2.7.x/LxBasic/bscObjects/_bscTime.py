# coding:utf-8
from LxBasic import bscAbstract


class Time(bscAbstract.Abc_Time):
    def __init__(self, timestamp):
        self._initAbcTime(timestamp)


class ActiveTime(bscAbstract.Abc_Time):
    def __init__(self):
        self._initAbcTime(self._activeTimeStamp())
