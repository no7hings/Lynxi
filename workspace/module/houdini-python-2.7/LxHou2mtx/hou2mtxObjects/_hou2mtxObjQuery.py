# coding:utf-8
from LxData.datObjects import _datObjRaw
# graphic
from LxGraphic import grhCfg, grhObjAbs

from LxGraphic.grhObjects import _grhObjStack, _grhObjQuery
# materialx
from LxMtx import mtxCfg

from LxMtx.mtxObjects import _mtxObjQuery
# usd
from LxHouBasic import houBscCfg

from LxHouBasic.houBscObjects import _houBscObjQuery
# usd2material
from .. import hou2mtxCfg, hou2mtxObjAbs


class TrsObjLoader(hou2mtxObjAbs.Abs_Hou2mtxTrsObjLoader):
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
        self._initAbsHou2mtxTrsObjLoader(*args)


class TrsObjQueryrawCreator(hou2mtxObjAbs.Abs_Hou2mtxObjQueryrawCreator):
    CLS_grh__trs_obj_queryraw_creator__node_stack = _grhObjStack.TrsNodeQueryrawStack
    CLS_grh__trs_obj_queryraw_creator__node = _grhObjQuery.TrsNodeQueryraw

    CLS_grh__trs_obj_queryraw_creator__obj_loader = TrsObjLoader

    VAR_grh__trs_obj_queryraw_creator__node_file = hou2mtxCfg.Hou2mtxUtility.DEF_usd2mtx__node_file
    VAR_grh__trs_obj_queryraw_creator__geometry_file = hou2mtxCfg.Hou2mtxUtility.DEF_usd2mtx__geometry_file
    VAR_grh__trs_obj_queryraw_creator__material_file = hou2mtxCfg.Hou2mtxUtility.DEF_usd2mtx__material_file

    IST_grh__trs_obj_queryraw_creator__source = _houBscObjQuery.GRH_OBJ_QUERYRAW_CREATOR
    IST_grh__trs_obj_queryraw_creator__target = _mtxObjQuery.GRH_OBJ_QUERYRAW_CREATOR

    def __init__(self, *args):
        self._initAbsHou2mtxObjQueryrawCreator(*args)


GRH_TRS_OBJ_QUERYRAW_CREATOR = TrsObjQueryrawCreator()


class TrsPortQuery(grhObjAbs.Abs_GrhTrsPortQuery):
    IST_grh__trs_obj__queryraw_creator = GRH_TRS_OBJ_QUERYRAW_CREATOR

    def __init__(self, *args):
        self._initAbsGrhTrsPortQuery(*args)


class TrsNodeQuery(grhObjAbs.Abs_GrhTrsNodeQuery):
    CLS_grh__trs_port_query_set = _grhObjStack.TrsPortQueryStack
    CLS_grh__trs_port_query = TrsPortQuery

    IST_grh__trs_obj__queryraw_creator = GRH_TRS_OBJ_QUERYRAW_CREATOR

    def __init__(self, *args):
        self._initAbsGrhTrsNodeQuery(*args)


class TrsObjQueryBuilder(grhObjAbs.Abs_GrhTrsObjQueryBuilder):
    CLS_grh__trs_node_query_set = _grhObjStack.TrsNodeQueryStack
    CLS_grh__trs_node_query = TrsNodeQuery

    def __init__(self, *args):
        self._initAbsGrhTrsObjQueryBuilder(*args)


GRH_TRS_OBJ_QUERY_BUILDER = TrsObjQueryBuilder(
    houBscCfg.HouBscUtility.DEF_hou__graphic_name, mtxCfg.MtxUtility.DEF_mtx___graphic_name
)


class TrsObjQueue(grhObjAbs.Abs_GrhObjQueue):
    CLS_grh__obj_queue__node_stack = _grhObjStack.TrsNodeStack

    def __init__(self, *args):
        self._initAbsGrhObjQueue(*args)


GRH_TRS_OBJ_QUEUE = TrsObjQueue()
