# coding:utf-8
from..import bscObjAbs


class ObjStack(bscObjAbs.AbsBscObjStack):
    def __init__(self, *args):
        self._initAbsBscObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.path()


class Port(bscObjAbs.AbsBscPort):
    def __init__(self, *args, **kwargs):
        self._initAbsBscPort(*args, **kwargs)


class Node(bscObjAbs.AbsBscNode):
    CLS_bsc__node__port = Port
    CLS_bsc__node__port_stack = ObjStack

    def __init__(self, *args, **kwargs):
        self._initAbsBscNode(*args, **kwargs)


class DagTree(bscObjAbs.AbsBscDagTree):
    CLS_bsc__node_tree__node = Node
    CLS_bsc__node_tree__node_stack = ObjStack

    def __init__(self, *args):
        self._initAbsBscDagTree(*args)
