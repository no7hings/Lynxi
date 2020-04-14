# coding:utf-8
from LxGraphic import grhCfg

from LxGraphic.grhObjects import _grhObjSet

from ..import mtlObjAbs

from ..mtlObjects import _mtlObjRaw, _mtlObjPort, _mtlObjQuery


class Node(mtlObjAbs.Abs_MtlNode):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_category = _mtlObjRaw.Category
    CLS_grh_nodepath = _mtlObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet

    VAR_grh_port_cls_dict = {
        grhCfg.Utility.DEF_grh_keyword_param: _mtlObjPort.Param,
        grhCfg.Utility.DEF_grh_keyword_param_channel: _mtlObjPort.ParamChannel,
        grhCfg.Utility.DEF_grh_keyword_input: _mtlObjPort.Input,
        grhCfg.Utility.DEF_grh_keyword_input_channel: _mtlObjPort.InputChannel,
        grhCfg.Utility.DEF_grh_keyword_output: _mtlObjPort.Output,
        grhCfg.Utility.DEF_grh_keyword_output_channel: _mtlObjPort.OutputChannel,

        grhCfg.Utility.DEF_grh_keyword_property: _mtlObjPort.Param,
        grhCfg.Utility.DEF_grh_keyword_visibility: _mtlObjPort.Param
    }
    VAR_grh_input_assign_list = [
        grhCfg.Utility.DEF_grh_keyword_input,
        grhCfg.Utility.DEF_grh_keyword_input_channel
    ]
    VAR_grh_output_assign_list = [
        grhCfg.Utility.DEF_grh_keyword_output,
        grhCfg.Utility.DEF_grh_keyword_output_channel
    ]
    VAR_grh_param_assign_list = [
        grhCfg.Utility.DEF_grh_keyword_param,
        grhCfg.Utility.DEF_grh_keyword_param_channel,
        # geometry
        grhCfg.Utility.DEF_grh_keyword_property,
        grhCfg.Utility.DEF_grh_keyword_visibility
    ]

    OBJ_grh_query_cache = _mtlObjQuery.OBJ_grh_query_cache_
    OBJ_grh_obj_cache = _mtlObjQuery.OBJ_grh_obj_cache_

    # xml ************************************************************************************************************ #
    VAR_mtl_file_attribute_attach_key = u'nodename'

    def __init__(self, *args):
        self._initAbsMtlNode(*args)


class NodeGraph(mtlObjAbs.Abc_MtlNodeGraph):
    CLS_mtl_name = _mtlObjRaw.Name

    CLS_mtl_node = Node
    CLS_mtl_node_set = _grhObjSet.NodeSet

    CLS_mtl_node_graph_output_set = _grhObjSet.ObjSet
    CLS_mtl_node_graph_output = _mtlObjPort.NodeGraphOutput

    VAR_mtl_file_element_key = u'nodegraph'
    VAR_mtl_file_attribute_attach_key = u'nodegraph'

    def __init__(self, *args):
        self._initAbcMtlNodeGraph(*args)


class ShaderProxy(mtlObjAbs.Abc_MtlShaderProxy):
    CLS_mtl_name = _mtlObjRaw.Name
    CLS_mtl_node = Node

    CLS_mtl_node_graph_set = _grhObjSet.ObjSet
    CLS_mtl_node_graph = NodeGraph

    CLS_mtl_port_proxy_set = _grhObjSet.ObjSet
    CLS_mtl_port_proxy = _mtlObjPort.BindInput

    VAR_mtl_file_element_key = u'shaderref'

    def __init__(self, *args):
        self._initAbcMtlShaderProxy(*args)


class MaterialProxy(mtlObjAbs.Abc_MtlMaterialProxy):
    CLS_mtl_name = _mtlObjRaw.Name
    CLS_mtl_node = Node

    VAR_mtl_file_element_key = u'material'
    VAR_mtl_file_attribute_attach_key = u'material'

    def __init__(self, *args):
        self._initAbcMtlMaterialProxy(*args)


class GeometryProxy(mtlObjAbs.Abc_MtlGeometryProxy):
    CLS_mtl_name = _mtlObjRaw.Name
    CLS_mtl_node = Node

    CLS_mtl_port_proxy_set = _grhObjSet.ObjSet
    CLS_mtl_property = _mtlObjPort.Property
    CLS_mtl_visibility = _mtlObjPort.Visibility

    CLS_mtl_propertyset = _mtlObjPort.Propertyset

    VAR_mtl_file_element_key = u'geometry'

    def __init__(self, *args):
        self._initAbcMtlGeometryProxy(*args)
