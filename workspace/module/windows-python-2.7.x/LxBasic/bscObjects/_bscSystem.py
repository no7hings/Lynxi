# coding:utf-8
from LxBasic import bscAbstract


class Mtd_Pc(bscAbstract.Abc_System):
    @classmethod
    def userName(cls):
        return cls._getUserName()

    @classmethod
    def hostName(cls):
        return cls._getHostName()

    @classmethod
    def host(cls):
        return cls._getHost()
