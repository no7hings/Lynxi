# coding:utf-8
from LxData.datObjects import _datObjRaw, _datObjPath

from LxGraphic import grhCfg

from LxGraphic.grhObjects import _grhObjStack

from .. import usdObjAbs

from ..usdObjects import _usdObjRaw, _usdObjQuery, _usdObjPort


class Node(usdObjAbs.Abs_UsdNode):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack

    CLS_grh__obj__path = _usdObjRaw.Nodepath

    CLS_grh__obj__loader = _usdObjQuery.ObjLoader

    CLS_grh__node__typepath = _datObjPath.Typepath
    CLS_grh__node__datatype = _datObjRaw.Datatype

    CLS_grh__node__port_stack = _grhObjStack.PortStack

    CLS_grh__node__connector = _usdObjPort.Connector

    IST_grh__obj__query_builder = _usdObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _usdObjQuery.GRH_OBJ_QUEUE

    VAR_grh__node__port_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _usdObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.gnport_channel: _usdObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.inport: _usdObjPort.Inport,
        grhCfg.GrhPortAssignQuery.inport_channel: _usdObjPort.Inport,
        grhCfg.GrhPortAssignQuery.otport: _usdObjPort.Otport,
        grhCfg.GrhPortAssignQuery.otport_channel: _usdObjPort.Otport,

        grhCfg.GrhPortAssignQuery.asport: _usdObjPort.Asport,

        grhCfg.GrhPortAssignQuery.property: _usdObjPort.Inport,
        grhCfg.GrhPortAssignQuery.visibility: _usdObjPort.Inport
    }

    def __init__(self, *args, **kwargs):
        self._initAbsUsdNode(*args, **kwargs)
