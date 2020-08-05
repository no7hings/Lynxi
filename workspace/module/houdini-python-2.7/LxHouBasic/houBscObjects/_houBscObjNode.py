# coding:utf-8
from LxData.datObjects import _datObjRaw, _datObjPath

from LxGraphic import grhCfg

from LxGraphic.grhObjects import _grhObjStack

from .. import houBscObjAbs

from ..houBscObjects import _houBscObjData, _houBscObjQuery, _houBscObjPort


class Node(houBscObjAbs.Abs_HouNode):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack

    CLS_grh__obj__path = _houBscObjData.Nodepath

    CLS_grh__obj__loader = _houBscObjQuery.ObjLoader

    CLS_grh__node__typepath = _houBscObjData.Typepath
    CLS_grh__node__datatype = _datObjRaw.Datatype

    CLS_grh__node__port_stack = _grhObjStack.PortStack

    CLS_grh__node__connector = _houBscObjPort.Connector

    VAR_grh__node__port_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _houBscObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.gnport_channel: _houBscObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.inport: _houBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.inport_channel: _houBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.otport: _houBscObjPort.Otport,
        grhCfg.GrhPortAssignQuery.otport_channel: _houBscObjPort.Otport,

        grhCfg.GrhPortAssignQuery.asport: _houBscObjPort.Asport,

        grhCfg.GrhPortAssignQuery.property: _houBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.visibility: _houBscObjPort.Inport
    }

    IST_grh__obj__query_builder = _houBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _houBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsHouNode(*args, **kwargs)
