# coding:utf-8
from ..import grhCfg, grhObjAbs

from . import _grhObjSet


class NodeQueryraw(grhObjAbs.Abs_GrhNodeQueryraw):
    def __init__(self, *args):
        self._initAbsGrhNodeQueryraw(*args)


class PortQuery(grhObjAbs.Abs_GrhPortQuery):
    VAR_grh_portsep = grhCfg.Utility.DEF_grh_port_pathsep

    def __init__(self, *args):
        self._initAbsGrhPortQuery(*args)


class NodeQuery(grhObjAbs.Abs_GrhNodeQuery):
    CLS_grh_port_query_set = _grhObjSet.PortQuerySet
    CLS_grh_port_query = PortQuery

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    VAR_grh_channel_assign_keyword_list = [
        grhCfg.Utility.DEF_grh_keyword_inparm_channel,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel
    ]

    def __init__(self, *args):
        self._initAbsGrhNodeQuery(*args)


class TrsNodeQueryraw(grhObjAbs.Abs_GrhTrsNodeQueryraw):
    VAR_mtl_def_key_list = [
        grhCfg.Utility.DEF_grh_key_target_port,
        grhCfg.Utility.DEF_grh_key_target_portraw,
        grhCfg.Utility.DEF_grh_keyword_custom_node,
        grhCfg.Utility.DEF_grh_keyword_create_expression,
        grhCfg.Utility.DEF_grh_keyword_after_expression
    ]

    VAR_grh_trs_channel_keyword_list = [
        grhCfg.Utility.DEF_grh_keyword_inparm_channel,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel
    ]

    def __init__(self, *args):
        self._initAbsGrhTrsNodeQueryraw(*args)


class TrsPortQuery(grhObjAbs.Abs_GrhTrsPortQuery):
    def __init__(self, *args):
        self._initAbsGrhTrsPortQuery(*args)


class TrsNodeQuery(grhObjAbs.Abs_GrhTrsNodeQuery):
    CLS_grh_trs_port_query_set = _grhObjSet.TrsPortQuerySet
    CLS_grh_trs_port_query = TrsPortQuery

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    VAR_grh_channel_assign_keyword_list = [
        grhCfg.Utility.DEF_grh_keyword_inparm_channel,
        grhCfg.Utility.DEF_grh_keyword_otparm_channel
    ]

    def __init__(self, *args):
        self._initAbsGrhTrsNodeQuery(*args)
