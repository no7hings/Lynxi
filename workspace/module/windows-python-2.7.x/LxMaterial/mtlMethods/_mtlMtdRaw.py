# coding:utf-8
from .. import mtlConfigure


class Attribute(mtlConfigure.Utility):
    @classmethod
    def composeBy(cls, nodepathString, portpathString):
        return cls.DEF_mtl_port_pathsep.join([nodepathString, portpathString])


