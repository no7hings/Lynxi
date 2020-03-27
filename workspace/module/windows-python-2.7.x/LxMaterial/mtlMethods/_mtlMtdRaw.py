# coding:utf-8
from LxMaterial import mtlConfigure


class Attribute(mtlConfigure.Utility):
    @classmethod
    def composeBy(cls, nodepathString, portpathString):
        return cls.DEF_mtl_port_separator.join([nodepathString, portpathString])


