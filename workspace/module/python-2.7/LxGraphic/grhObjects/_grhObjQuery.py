# coding:utf-8
from .. import grhCfg, grhObjAbs

from . import _grhObjStack


class PortQueryraw(grhObjAbs.AbsGrhPortQueryraw):
    def __init__(self, *args):
        self._initAbsGrhPortQueryraw(*args)


class NodeQueryraw(grhObjAbs.AbsGrhNodeQueryraw):
    CLS_grh__node_queryraw__port_queryraw_stack = _grhObjStack.PortQueryrawStack
    CLS_grh__node_queryraw__port_queryraw = PortQueryraw

    def __init__(self, *args):
        self._initAbsGrhNodeQueryraw(*args)


class TrsPortQueryraw(grhObjAbs.AbsGrhTrsPortQueryraw):
    def __init__(self, *args):
        self._initAbsGrhTrsPortQueryraw(*args)


class TrsNodeQueryraw(grhObjAbs.AbsGrhTrsNodeQueryraw):
    CLS_grh__trs_node_queryraw__port_stack = _grhObjStack.TrsPortQueryrawStack
    CLS_grh__trs_node_queryraw__port = TrsPortQueryraw

    def __init__(self, *args):
        self._initAbsGrhTrsNodeQueryraw(*args)
