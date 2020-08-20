# coding:utf-8
from LxData.datObjects import _datObjRaw, _datObjPath

from LxGraphic import grhCfg

from LxGraphic.grhObjects import _grhObjStack

from .. import maBscObjAbs

from ..maBscObjects import _maBscObjRaw, _maBscObjQuery, _maBscObjPort


class Node(maBscObjAbs.AbsMaNode):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack

    CLS_grh__obj__path = _maBscObjRaw.Nodepath

    CLS_grh__obj__loader = _maBscObjQuery.ObjLoader

    CLS_grh__node__typepath = _datObjPath.Typepath
    CLS_grh__node__datatype = _datObjRaw.Datatype

    CLS_grh__node__port_stack = _grhObjStack.PortStack
    CLS_grh__node__connector = _maBscObjPort.Connector

    VAR_grh__node__port_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _maBscObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.gnport_channel: _maBscObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.inport: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.inport_channel: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.otport: _maBscObjPort.Otport,
        grhCfg.GrhPortAssignQuery.otport_channel: _maBscObjPort.Otport,

        grhCfg.GrhPortAssignQuery.asport: _maBscObjPort.Asport,

        grhCfg.GrhPortAssignQuery.property: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.visibility: _maBscObjPort.Inport
    }

    IST_grh__obj__query_builder = _maBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _maBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsMaNode(*args, **kwargs)


class Geometry(maBscObjAbs.AbsMaGeometry):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack

    CLS_grh__obj__path = _maBscObjRaw.Nodepath
    CLS_grh__obj__loader = _maBscObjQuery.ObjLoader

    CLS_grh__node__typepath = _datObjPath.Typepath
    CLS_grh__node__datatype = _datObjRaw.Datatype

    CLS_grh__node__port_stack = _grhObjStack.PortStack

    CLS_grh__node__connector = _maBscObjPort.Connector

    VAR_grh__node__port_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _maBscObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.gnport_channel: _maBscObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.inport: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.inport_channel: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.otport: _maBscObjPort.Otport,
        grhCfg.GrhPortAssignQuery.otport_channel: _maBscObjPort.Otport,

        grhCfg.GrhPortAssignQuery.asport: _maBscObjPort.Asport,

        grhCfg.GrhPortAssignQuery.property: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.visibility: _maBscObjPort.Inport
    }

    CLS_mya_node = Node

    IST_grh__obj__query_builder = _maBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _maBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsMaGeometry(*args, **kwargs)


class GeometryRoot(maBscObjAbs.AbsMaGeometryGroup):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack

    CLS_grh__obj__path = _maBscObjRaw.Nodepath
    CLS_grh__obj__loader = _maBscObjQuery.ObjLoader

    CLS_grh__node__typepath = _datObjPath.Typepath
    CLS_grh__node__datatype = _datObjRaw.Datatype

    CLS_grh__node__port_stack = _grhObjStack.PortStack
    CLS_grh__node__connector = _maBscObjPort.Connector

    CLS_grh__geometry = Geometry

    VAR_grh__node__port_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _maBscObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.gnport_channel: _maBscObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.inport: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.inport_channel: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.otport: _maBscObjPort.Otport,
        grhCfg.GrhPortAssignQuery.otport_channel: _maBscObjPort.Otport,

        grhCfg.GrhPortAssignQuery.asport: _maBscObjPort.Asport,

        grhCfg.GrhPortAssignQuery.property: _maBscObjPort.Inport,
        grhCfg.GrhPortAssignQuery.visibility: _maBscObjPort.Inport
    }

    IST_grh__obj__query_builder = _maBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _maBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsMaGeometryGroup(*args, **kwargs)
