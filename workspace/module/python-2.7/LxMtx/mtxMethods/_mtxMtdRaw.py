# coding:utf-8
from .. import mtxCfg


class Attribute(mtxCfg.MtxUtility):
    @classmethod
    def composeBy(cls, nodepathString, portpathString):
        return cls.DEF_mtx__node_port_pathsep.join([nodepathString, portpathString])


