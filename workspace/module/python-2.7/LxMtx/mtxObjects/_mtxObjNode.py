# coding:utf-8
from LxData.datObjects import _datObjRaw

from LxGraphic import grhCfg

from LxGraphic.grhObjects import _grhObjStack

from .. import mtxObjAbs

from . import _mtxObjRaw, _mtxObjPort, _mtxObjQuery


class Node(mtxObjAbs.AbsMtxNode):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack

    CLS_grh__obj__path = _mtxObjRaw.Nodepath
    CLS_grh__obj__loader = _mtxObjQuery.ObjLoader

    CLS_grh__node__typepath = _mtxObjRaw.Typepath
    CLS_grh__node__datatype = _mtxObjRaw.Datatype

    CLS_grh__node__port_stack = _grhObjStack.PortStack
    CLS_grh__node__connector = _mtxObjPort.Connector

    VAR_grh__node__port_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _mtxObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.gnport_channel: _mtxObjPort.Gnport,
        grhCfg.GrhPortAssignQuery.inport: _mtxObjPort.Inport,
        grhCfg.GrhPortAssignQuery.inport_channel: _mtxObjPort.Inchannel,
        grhCfg.GrhPortAssignQuery.otport: _mtxObjPort.Otport,
        grhCfg.GrhPortAssignQuery.otport_channel: _mtxObjPort.Otchannel,

        grhCfg.GrhPortAssignQuery.asport: _mtxObjPort.Asport,

        grhCfg.GrhPortAssignQuery.property: _mtxObjPort.Inport,
        grhCfg.GrhPortAssignQuery.visibility: _mtxObjPort.Inport
    }

    # **************************************************************************************************************** #
    IST_grh__obj__query_builder = _mtxObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__attribute_attach_str = u'nodename'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxNode(*args, **kwargs)


class NodeGraph(mtxObjAbs.AbsMtxNodeGraph):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Nodepath

    CLS_grh__node_graph__node_stack = _grhObjStack.NodeStack

    CLS_grh__node_graph__port_proxy_stack = _grhObjStack.NodeGraphOtportProxyStack
    CLS_grh__node_graph__port_proxy = _mtxObjPort.NodeGraphOtportProxy

    # **************************************************************************************************************** #
    VAR_dat__xml_obj__element_prefix_str = u'nodegraph'
    VAR_dat__xml_obj__attribute_attach_str = u'nodegraph'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxNodeGraph(*args, **kwargs)


class ShaderProxy(mtxObjAbs.AbsMtxShaderProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Nodepath

    CLS_grh__obj_proxy__bind_obj = Node

    CLS_grh__node_proxy__input_graph_stack = _grhObjStack.ObjStack
    CLS_grh__node_proxy__input_graph = NodeGraph

    CLS_grh__node_proxy__bind_port_proxy_stack = _grhObjStack.PortProxyStack

    VAR_grh__node_proxy__bind_port_proxy_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _mtxObjPort.GnportProxy,
        grhCfg.GrhPortAssignQuery.inport: _mtxObjPort.InportProxy,
        grhCfg.GrhPortAssignQuery.inport_channel: _mtxObjPort.InportProxy,
        grhCfg.GrhPortAssignQuery.otport: _mtxObjPort.OtportProxy,
        grhCfg.GrhPortAssignQuery.otport_channel: _mtxObjPort.OtportProxy,

        grhCfg.GrhPortAssignQuery.asport: _mtxObjPort.AsportProxy,

        grhCfg.GrhUtility.DEF_grh__keyword__property: _mtxObjPort.Property,
        grhCfg.GrhUtility.DEF_grh__keyword__visibility: _mtxObjPort.Visibility
    }

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'shaderref'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxShaderProxy(*args, **kwargs)


class MaterialProxy(mtxObjAbs.AbsMtxMaterialProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Nodepath

    CLS_grh__obj_proxy__bind_obj = Node
    # graph
    CLS_grh__node_proxy__input_graph_stack = _grhObjStack.ObjStack
    CLS_grh__node_proxy__input_graph = NodeGraph
    # port
    CLS_grh__node_proxy__bind_port_proxy_stack = _grhObjStack.PortProxyStack
    VAR_grh__node_proxy__bind_port_proxy_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _mtxObjPort.GnportProxy,
        grhCfg.GrhPortAssignQuery.inport: _mtxObjPort.InportProxy,
        grhCfg.GrhPortAssignQuery.inport_channel: _mtxObjPort.InportProxy,
        grhCfg.GrhPortAssignQuery.otport: _mtxObjPort.OtportProxy,
        grhCfg.GrhPortAssignQuery.otport_channel: _mtxObjPort.OtportProxy,

        grhCfg.GrhPortAssignQuery.asport: _mtxObjPort.AsportProxy,

        grhCfg.GrhUtility.DEF_grh__keyword__property: _mtxObjPort.Property,
        grhCfg.GrhUtility.DEF_grh__keyword__visibility: _mtxObjPort.Visibility
    }

    # xml ************************************************************************************************************ #
    VAR_grh_material_proxy__surface_shader_port_str = u'surfaceshader'
    VAR_grh_material_proxy__displacement_shader_port_str = u'displacementshader'
    VAR_grh_material_proxy__volume_port_str = u'volumeshader'

    VAR_dat__xml_obj__element_prefix_str = u'material'
    VAR_dat__xml_obj__attribute_attach_str = u'material'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxMaterialProxy(*args, **kwargs)


class GeometryProxy(mtxObjAbs.AbsMtxGeometryProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Nodepath

    CLS_grh__obj_proxy__bind_obj = Node
    # graph
    CLS_grh__node_proxy__input_graph_stack = _grhObjStack.ObjStack
    CLS_grh__node_proxy__input_graph = NodeGraph
    # port
    CLS_grh__node_proxy__bind_port_proxy_stack = _grhObjStack.PortProxyStack
    VAR_grh__node_proxy__bind_port_proxy_cls_dict = {
        grhCfg.GrhPortAssignQuery.gnport: _mtxObjPort.GnportProxy,
        grhCfg.GrhPortAssignQuery.inport: _mtxObjPort.InportProxy,
        grhCfg.GrhPortAssignQuery.inport_channel: _mtxObjPort.InportProxy,
        grhCfg.GrhPortAssignQuery.otport: _mtxObjPort.OtportProxy,
        grhCfg.GrhPortAssignQuery.otport_channel: _mtxObjPort.OtportProxy,

        grhCfg.GrhPortAssignQuery.asport: _mtxObjPort.AsportProxy,

        grhCfg.GrhUtility.DEF_grh__keyword__property: _mtxObjPort.Property,
        grhCfg.GrhUtility.DEF_grh__keyword__visibility: _mtxObjPort.Visibility
    }
    # portset
    CLS_grh__node_proxy__portset_stack = _grhObjStack.ObjStack
    CLS_grh__node_proxy__portset = _mtxObjPort.Propertyset

    CLS_grh__node_proxy__input_node_proxy_stack = _grhObjStack.ObjProxyStack

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'geometry'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxGeometryProxy(*args, **kwargs)
