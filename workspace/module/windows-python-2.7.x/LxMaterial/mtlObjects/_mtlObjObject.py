# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjCache, _mtlObjPort, _mtlObjValue


OBJ_mtl_config = mtlConfigure.Utility
DEF_mtl_value_cls_dict = {
    OBJ_mtl_config.DEF_mtl_porttype_closure: _mtlObjValue.Val_Closure,

    OBJ_mtl_config.DEF_mtl_porttype_shader: _mtlObjValue.Val_Closure,
    OBJ_mtl_config.DEF_mtl_porttype_visibility: _mtlObjValue.Val_Visibility,

    OBJ_mtl_config.DEF_mtl_porttype_boolean: _mtlObjValue.Val_Boolean,
    OBJ_mtl_config.DEF_mtl_porttype_Integer: _mtlObjValue.Val_Integer,
    OBJ_mtl_config.DEF_mtl_porttype_integer_array: _mtlObjValue.Val_IntegerArray,
    OBJ_mtl_config.DEF_mtl_porttype_float: _mtlObjValue.Val_Float,
    OBJ_mtl_config.DEF_mtl_porttype_float_array: _mtlObjValue.Val_FloatArray,

    OBJ_mtl_config.DEF_mtl_porttype_color2: _mtlObjValue.Val_Color2,
    OBJ_mtl_config.DEF_mtl_porttype_color2_array: _mtlObjValue.Val_Color2Array,
    OBJ_mtl_config.DEF_mtl_porttype_color3: _mtlObjValue.Val_Color3,
    OBJ_mtl_config.DEF_mtl_porttype_color3_array: _mtlObjValue.Val_Color3Array,
    OBJ_mtl_config.DEF_mtl_porttype_color4: _mtlObjValue.Val_Color4,
    OBJ_mtl_config.DEF_mtl_porttype_color4_array: _mtlObjValue.Val_Color4Array,

    OBJ_mtl_config.DEF_mtl_porttype_vector2: _mtlObjValue.Val_vector2,
    OBJ_mtl_config.DEF_mtl_porttype_vector2_array: _mtlObjValue.Val_vector2Array,
    OBJ_mtl_config.DEF_mtl_porttype_vector3: _mtlObjValue.Val_vector3,
    OBJ_mtl_config.DEF_mtl_porttype_vector3_array: _mtlObjValue.Val_vector3Array,
    OBJ_mtl_config.DEF_mtl_porttype_vector4: _mtlObjValue.Val_vector4,
    OBJ_mtl_config.DEF_mtl_porttype_vector4_array: _mtlObjValue.Val_vector4Array,

    OBJ_mtl_config.DEF_mtl_porttype_matrix33: _mtlObjValue.Val_matrix33,
    OBJ_mtl_config.DEF_mtl_porttype_matrix44: _mtlObjValue.Val_matrix44,

    OBJ_mtl_config.DEF_mtl_porttype_string: _mtlObjValue.Val_string,
    OBJ_mtl_config.DEF_mtl_porttype_string_array: _mtlObjValue.Val_stringArray,
    OBJ_mtl_config.DEF_mtl_porttype_file_name: _mtlObjValue.Val_file_name,
    OBJ_mtl_config.DEF_mtl_porttype_geometry_name: _mtlObjValue.Val_geometry_name,
    OBJ_mtl_config.DEF_mtl_porttype_geometry_name_array: _mtlObjValue.Val_geometry_nameArray
}


class Node(mtlObjCore.Abc_MtlNode):
    CLS_grh_type = _mtlObjRaw.TypeString
    CLS_grh_category = _mtlObjRaw.NodeCategory
    CLS_grh_nodepath = _mtlObjRaw.NodeName

    CLS_grh_port_set = _mtlObjSet.PortSet

    OBJ_mtl_query_cache = _mtlObjCache.OBJ_mtl_query_cache
    OBJ_mtl_obj_cache = _mtlObjCache.OBJ_mtl_obj_cache

    VAR_mtl_value_class_dict = DEF_mtl_value_cls_dict

    VAR_mtl_port_class_dict = {
        OBJ_mtl_config.DEF_mtl_keyword_input: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_property: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_visibility: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_output: _mtlObjPort.Output,
        OBJ_mtl_config.DEF_mtl_keyword_input_channel: _mtlObjPort.InputChannel,
        OBJ_mtl_config.DEF_mtl_keyword_output_channel: _mtlObjPort.OutputChannel
    }

    VAR_mtl_file_attribute_attach_key = u'nodename'

    def __init__(self, *args):
        self._initAbcMtlNode(*args)


class Geometry(mtlObjCore.Abc_MtlGeometry):
    CLS_grh_type = _mtlObjRaw.TypeString
    CLS_grh_category = _mtlObjRaw.NodeCategory
    CLS_grh_nodepath = _mtlObjRaw.NodeName

    CLS_grh_port_set = _mtlObjSet.PortSet

    CLS_mtl_child_set = _mtlObjSet.GeometrySet
    CLS_mtl_material_set = _mtlObjSet.MaterialSet

    VAR_mtl_value_class_dict = DEF_mtl_value_cls_dict

    VAR_mtl_port_class_dict = {
        OBJ_mtl_config.DEF_mtl_keyword_input: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_property: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_visibility: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_output: _mtlObjPort.Output,
        OBJ_mtl_config.DEF_mtl_keyword_input_channel: _mtlObjPort.InputChannel,
        OBJ_mtl_config.DEF_mtl_keyword_output_channel: _mtlObjPort.OutputChannel
    }

    OBJ_mtl_query_cache = _mtlObjCache.OBJ_mtl_query_cache
    OBJ_mtl_obj_cache = _mtlObjCache.OBJ_mtl_obj_cache

    VAR_mtl_file_element_key = u'geometry'
    VAR_mtl_file_attribute_attach_key = u'geom'

    def __init__(self, *args):
        self._initAbcMtlGeometry(*args)


class NodeGraph(mtlObjCore.Abc_MtlNodeGraph):
    CLS_mtl_name = _mtlObjRaw.NameString

    CLS_mtl_node = Node
    CLS_mtl_node_set = _mtlObjSet.ObjectSet
    CLS_mtl_output_set = _mtlObjSet.PortSet

    CLS_mtl_node_graph_output = _mtlObjPort.NodeGraphOutput

    VAR_mtl_file_element_key = u'nodegraph'
    VAR_mtl_file_attribute_attach_key = u'nodegraph'

    def __init__(self, *args):
        self._initAbcMtlNodeGraph(*args)


class ShaderProxy(mtlObjCore.Abc_MtlShaderProxy):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_node = Node

    CLS_mtl_node_graph_set = _mtlObjSet.NodeGraphSet
    CLS_mtl_node_graph = NodeGraph

    CLS_mtl_port_proxy_set = _mtlObjSet.PortSet
    CLS_mtl_port_proxy = _mtlObjPort.BindInput

    VAR_mtl_file_element_key = u'shaderref'

    def __init__(self, *args):
        self._initAbcMtlShaderProxy(*args)


class MaterialProxy(mtlObjCore.Abc_MtlMaterialProxy):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_node = Node

    VAR_mtl_file_element_key = u'material'
    VAR_mtl_file_attribute_attach_key = u'material'

    def __init__(self, *args):
        self._initAbcMtlMaterialProxy(*args)


class GeometryProxy(mtlObjCore.Abc_MtlGeometryProxy):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_node = Geometry

    CLS_mtl_port_proxy_set = _mtlObjSet.PortSet
    CLS_mtl_property = _mtlObjPort.Property
    CLS_mtl_visibility = _mtlObjPort.Visibility

    CLS_mtl_propertyset = _mtlObjPort.Propertyset

    VAR_mtl_file_element_key = u'geometry'

    def __init__(self, *args):
        self._initAbcMtlGeometryProxy(*args)
