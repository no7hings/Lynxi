# coding:utf-8
from ..import mtlCfg


class Attribute(mtlCfg.Utility):
    @classmethod
    def composeBy(cls, nodepathString, portpathString):
        return cls.DEF_mtl_port_pathsep.join([nodepathString, portpathString])


