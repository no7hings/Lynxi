# coding:utf-8
from LxGraphic import grhCfg, grhObjAbs

from LxGraphic.grhObjects import _grhObjStack, _grhObjQuery

from .. import usdCfg, usdObjAbs

from ..usdObjects import _usdObjCallback


class ObjLoader(usdObjAbs.AbsUsdObjLoader):
    CALL_grh__obj_loader__get_obj_scene = _usdObjCallback

    VAR_grh__obj_loader__node_type__transform = usdCfg.UsdUtility.DEF_usd__node_type_transform

    def __init__(self, *args):
        self._initAbsUsdObjLoader(*args)


class ObjQueryrawCreator(usdObjAbs.AbsUsdObjQueryrawCreator):
    CLS_grh__obj_query_creator__node_queryraw_stack = _grhObjStack.NodeQueryrawStack
    CLS_grh__obj_query_creator__node_queryraw = _grhObjQuery.NodeQueryraw

    CLS_grh__obj_query_creator__obj_loader = ObjLoader

    def __init__(self, *args):
        self._initAbsUsdObjQueryrawCreator(*args)


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
    usdCfg.UsdUtility.DEF_usd__graphic_name
)


# object cache ******************************************************************************************************* #
class ObjQueue(usdObjAbs.AbsUsdObjQueue):
    CLS_grh__obj_queue__node_stack = _grhObjStack.NodeStack

    def __init__(self, *args):
        self._initAbsUsdObjQueue(*args)


GRH_OBJ_QUEUE = ObjQueue()
