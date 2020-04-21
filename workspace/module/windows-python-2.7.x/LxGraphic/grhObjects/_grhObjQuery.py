# coding:utf-8
from ..import grhCfg, grhObjAbs

from ..grhObjects import _grhObjSet


class PortQueryraw(grhObjAbs.Abs_GrhPortQueryraw):
    def __init__(self, *args):
        self._initAbsGrhPortQueryraw(*args)


class NodeQueryraw(grhObjAbs.Abs_GrhNodeQueryraw):
    CLS_grh_port_queryraw_set = _grhObjSet.PortQueryrawSet
    CLS_grh_port_queryraw = PortQueryraw

    def __init__(self, *args):
        self._initAbsGrhNodeQueryraw(*args)


class TrsPortQueryraw(grhObjAbs.Abs_GrhTrsPortQueryraw):
    VAR_grh_trs_query_key = grhCfg.Utility.DEF_grh_key_source_portpath

    def __init__(self, *args):
        self._initAbsGrhTrsPortQueryraw(*args)


class TrsNodeQueryraw(grhObjAbs.Abs_GrhTrsNodeQueryraw):
    CLS_grh_trs_port_queryraw_set = _grhObjSet.TrsPortQueryrawSet
    CLS_grh_trs_port_queryraw = TrsPortQueryraw

    VAR_mtl_def_key_list = [
        grhCfg.Utility.DEF_grh_key_target_port,
        grhCfg.Utility.DEF_grh_key_target_portraw,
        grhCfg.Utility.DEF_grh_keyword_custom_node,
        grhCfg.Utility.DEF_grh_keyword_create_expression,
        grhCfg.Utility.DEF_grh_keyword_after_expression
    ]

    def __init__(self, *args):
        self._initAbsGrhTrsNodeQueryraw(*args)
