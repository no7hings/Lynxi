# coding:utf-8
from LxData.datObjects import _datObjRaw
# graphic
from LxGraphic import grhCfg, grhObjAbs

from LxGraphic.grhObjects import _grhObjStack, _grhObjQuery
# materialx
from LxMtx import mtxCfg

from LxMtx.mtxObjects import _mtxObjQuery
# usd
from LxUsd import usdCfg

from LxUsd.usdObjects import _usdObjQuery
# usd2material
from .. import usd2mtxCfg, usd2mtxObjAbs


class TrsObjLoader(usd2mtxObjAbs.AbsUsd2mtxTrsObjLoader):
    VAR_grh__trs_obj_loader__node_property_key_list = [
        grhCfg.GrhUtility.DEF_grh__key_target_port,
        grhCfg.GrhUtility.DEF_grh__keyword__custom_node,
        grhCfg.GrhUtility.DEF_grh__keyword__create_expression,
        grhCfg.GrhUtility.DEF_grh__keyword__after_expression
    ]

    VAR_grh__trs_obj_loader__port_property_key_list = [
        grhCfg.GrhUtility.DEF_grh__keyword_portraw_convert,
        grhCfg.GrhUtility.DEF_grh__keyword_datatype_convert
    ]

    def __init__(self, *args):
        self._initAbsUsd2mtxTrsObjLoader(*args)


class TrsObjQueryrawCreator(usd2mtxObjAbs.AbsUsd2mtxObjQueryrawCreator):
    CLS_grh__trs_obj_queryraw_creator__node_stack = _grhObjStack.TrsNodeQueryrawStack
    CLS_grh__trs_obj_queryraw_creator__node = _grhObjQuery.TrsNodeQueryraw

    CLS_grh__trs_obj_queryraw_creator__obj_loader = TrsObjLoader

    VAR_grh__trs_obj_queryraw_creator__node_file = usd2mtxCfg.Usd2mtxUtility.DEF_usd2mtx__node_file
    VAR_grh__trs_obj_queryraw_creator__geometry_file = usd2mtxCfg.Usd2mtxUtility.DEF_usd2mtx__geometry_file
    VAR_grh__trs_obj_queryraw_creator__material_file = usd2mtxCfg.Usd2mtxUtility.DEF_usd2mtx__material_file
    VAR_grh__trs_output_file = usd2mtxCfg.Usd2mtxUtility.DEF_usd2mtx_output_defs_file
    VAR_grh__trs_port_child_file = usd2mtxCfg.Usd2mtxUtility.DEF_usd2mtx_port_child_defs_file

    VAR_grh__trs_custom_category_file = usd2mtxCfg.Usd2mtxUtility.DEF_usd2mtx_custom_category_file
    VAR_grh__trs_custom_node_file = usd2mtxCfg.Usd2mtxUtility.DEF_usd2mtx_custom_node_file

    IST_grh__trs_obj_queryraw_creator__source = _usdObjQuery.GRH_OBJ_QUERYRAW_CREATOR
    IST_grh__trs_obj_queryraw_creator__target = _mtxObjQuery.GRH_OBJ_QUERYRAW_CREATOR

    def __init__(self, *args):
        self._initAbsUsd2mtxObjQueryrawCreator(*args)


GRH_TRS_OBJ_QUERYRAW_CREATOR = TrsObjQueryrawCreator()


class TrsPortQuery(grhObjAbs.AbsGrhTrsPortQuery):
    IST_grh__trs_obj__queryraw_creator = GRH_TRS_OBJ_QUERYRAW_CREATOR

    def __init__(self, *args):
        self._initAbsGrhTrsPortQuery(*args)


class TrsNodeQuery(grhObjAbs.AbsGrhTrsNodeQuery):
    CLS_grh__trs_port_query_set = _grhObjStack.TrsPortQueryStack
    CLS_grh__trs_port_query = TrsPortQuery

    IST_grh__trs_obj__queryraw_creator = GRH_TRS_OBJ_QUERYRAW_CREATOR

    def __init__(self, *args):
        self._initAbsGrhTrsNodeQuery(*args)


class TrsObjQueryBuilder(grhObjAbs.AbsGrhTrsObjQueryBuilder):
    CLS_grh__trs_node_query_set = _grhObjStack.TrsNodeQueryStack
    CLS_grh__trs_node_query = TrsNodeQuery

    def __init__(self, *args):
        self._initAbsGrhTrsObjQueryBuilder(*args)


GRH_TRS_OBJ_QUERY_BUILDER = TrsObjQueryBuilder(
    usdCfg.UsdUtility.DEF_usd__graphic_name, mtxCfg.MtxUtility.DEF_mtx___graphic_name
)


class TrsObjQueue(grhObjAbs.AbsGrhObjQueue):
    CLS_grh__obj_queue__node_stack = _grhObjStack.TrsNodeStack

    def __init__(self, *args):
        self._initAbsGrhObjQueue(*args)


GRH_TRS_OBJ_QUEUE = TrsObjQueue()
