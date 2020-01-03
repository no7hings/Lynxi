# coding:utf-8
from LxBasic import bscAbstract


class Time(bscAbstract.Abc_Time):
    def __init__(self, timestamp):
        self._initAbcTime(timestamp)


class Tme_Active(bscAbstract.Abc_Time):
    def __init__(self):
        self._initAbcTime(self._activeTimeStamp())
