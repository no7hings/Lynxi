# coding:utf-8
from .. import grhConfigure, grhObjAbs

from . import _grhObjSet


class PortQuery(grhObjAbs.Abs_GrhPortQuery):
    VAR_grh_portsep = grhConfigure.Utility.DEF_grh_portsep

    def __init__(self, *args):
        self._initAbsGrhPortQuery(*args)


class NodeQuery(grhObjAbs.Abs_GrhNodeQuery):
    CLS_grh_port_query = PortQuery
    CLS_grh_port_query_set = _grhObjSet.PortQuerySet

    def __init__(self, *args):
        self._initAbsGrhNodeQuery(*args)
