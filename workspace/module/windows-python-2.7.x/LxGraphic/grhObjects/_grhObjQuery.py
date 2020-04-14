# coding:utf-8
from ..import grhCfg, grhObjAbs

from . import _grhObjSet


class NodeRaw(grhObjAbs.Abs_GrhNodeRaw):
    def __init__(self, *args):
        self._initAbsGrhNodeRaw(*args)


class PortQuery(grhObjAbs.Abs_GrhPortQuery):
    VAR_grh_portsep = grhCfg.Utility.DEF_grh_portsep

    def __init__(self, *args):
        self._initAbsGrhPortQuery(*args)


class NodeQuery(grhObjAbs.Abs_GrhNodeQuery):
    CLS_grh_port_query_set = _grhObjSet.PortQuerySet
    CLS_grh_port_query = PortQuery

    def __init__(self, *args):
        self._initAbsGrhNodeQuery(*args)
