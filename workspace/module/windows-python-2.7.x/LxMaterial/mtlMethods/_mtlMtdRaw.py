# coding:utf-8
from LxMaterial import mtlConfigure


class Attribute(mtlConfigure.Utility):
    @classmethod
    def composeBy(cls, nodeString, portString):
        return cls.DEF_mtl_port_separator.join([nodeString, portString])


