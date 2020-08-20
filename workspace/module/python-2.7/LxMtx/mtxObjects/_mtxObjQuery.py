# coding:utf-8
from LxData.datObjects import _datObjRaw

from LxGraphic import grhCfg, grhObjAbs

from LxGraphic.grhObjects import _grhObjStack, _grhObjQuery

from .. import mtxCfg, mtxObjAbs


class ObjLoader(mtxObjAbs.AbsMtxObjLoader):
    def __init__(self, *args):
        self._initAbsMtxObjLoader(*args)


class ObjQueryrawCreator(mtxObjAbs.AbsMtxObjQueryBuilder):
    CLS_grh__obj_query_creator__node_queryraw_stack = _grhObjStack.NodeQueryrawStack
    CLS_grh__obj_query_creator__node_queryraw = _grhObjQuery.NodeQueryraw

    CLS_grh__obj_query_creator__obj_loader = ObjLoader

    VAR_grh__node_file = mtxCfg.MtxUtility.DEF_mtx__arnold_node_defs_file
    VAR_grh__geometry_file = mtxCfg.MtxUtility.DEF_mtx__arnold_geometry_def_file
    VAR_grh__material_file = mtxCfg.MtxUtility.DEF_mtx__arnold_material_def_file
    VAR_grh__output_file = mtxCfg.MtxUtility.DEF_mtx__arnold_output_defs_file
    VAR_grh__port_child_file = mtxCfg.MtxUtility.DEF_mtx__arnold_port_child_defs_file

    def __init__(self, *args):
        self._initAbsMtxObjQueryBuilder(*args)


GRH_OBJ_QUERYRAW_CREATOR = ObjQueryrawCreator()


class PortQuery(grhObjAbs.AbsGrhPortQuery):
    VAR_grh__port_query__portsep = grhCfg.GrhUtility.DEF_grh__node_port_pathsep

    IST_grh__obj_query__queryraw_builder = GRH_OBJ_QUERYRAW_CREATOR

    def __init__(self, *args):
        self._initAbsGrhPortQuery(*args)


class NodeQuery(grhObjAbs.AbsGrhNodeQuery):
    CLS_grh__node_query__port_query_stack = _grhObjStack.PortQueryStack
    CLS_grh__node_query__port_query = PortQuery

    IST_grh__obj_query__queryraw_builder = GRH_OBJ_QUERYRAW_CREATOR

    def __init__(self, *args):
        self._initAbsGrhNodeQuery(*args)


class ObjQueryBuilder(grhObjAbs.AbsGrhObjQueryBuilder):
    CLS_grh__obj_query_builder__node_query = NodeQuery
    CLS_grh__obj_query_builder__node_query_stack = _grhObjStack.NodeQueryStack

    def __init__(self, *args):
        self._initAbsGrhObjQueryBuilder(*args)


GRH_OBJ_QUERY_BUILDER = ObjQueryBuilder(
    mtxCfg.MtxUtility.DEF_mtx___graphic_name
)


class ObjQueue(mtxObjAbs.AbsMtxObjQueue):
    CLS_grh__obj_queue__node_stack = _grhObjStack.NodeStack

    def __init__(self, *args):
        self._initAbsMtxObjQueue(*args)


GRH_OBJ_QUEUE = ObjQueue()



