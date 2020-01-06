# coding:utf-8
from LxBasic import bscAbstract


class PC(bscAbstract.Abc_System):
    @property
    def userName(self):
        return self._getUserName()

    @property
    def hostName(self):
        return self._getHostName()

    @property
    def host(self):
        return self._getHost()


class Sys_Environ(bscAbstract.Abc_System):
    def __init__(self, keyString):
        self._keyString = keyString

    @property
    def value(self):
        return self._getEnvironValue(self._keyString)
