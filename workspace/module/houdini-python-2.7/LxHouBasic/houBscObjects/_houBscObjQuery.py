# coding:utf-8
from LxData.datObjects import _datObjRaw

from LxGraphic import grhCfg, grhObjAbs

from LxGraphic.grhObjects import _grhObjStack, _grhObjQuery

from .. import houBscCfg, houBscObjAbs


class ObjLoader(houBscObjAbs.AbsHouObjLoader):
    def __init__(self, *args):
        self._initAbsHoObjLoader(*args)


class ObjQueryrawCreator(houBscObjAbs.AbsHouObjQueryrawCreator):
    CLS_grh__obj_query_creator__node_queryraw_stack = _grhObjStack.NodeQueryrawStack
    CLS_grh__obj_query_creator__node_queryraw = _grhObjQuery.NodeQueryraw

    CLS_grh__obj_query_creator__obj_loader = ObjLoader

    def __init__(self, *args):
        self._initAbsHoObjQueryrawCreator(*args)


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
    houBscCfg.HouBscUtility.DEF_hou__graphic_name
)


# object queue ******************************************************************************************************* #
class ObjQueue(houBscObjAbs.AbsHouObjQueue):
    CLS_grh__obj_queue__node_stack = _grhObjStack.NodeStack

    def __init__(self, *args):
        self._initAbsHoObjQueue(*args)


GRH_OBJ_QUEUE = ObjQueue()
