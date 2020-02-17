# coding:utf-8
from LxMaBasic import maBscCore


class Node(maBscCore.NodeBasic):
    pass


class Shader(maBscCore.NodeBasic):
    pass


class Geometry(maBscCore.NodeBasic):
    @classmethod
    def shadingEngines(cls, objectString):
        return cls._getNodeShadingEngineStringList(objectString)
