# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet

from .. import mtlConfigure, mtlObjAbs

from ..mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjCache, _mtlObjPort, _mtlObjValue


OBJ_mtl_config = mtlConfigure.Utility
_DEF_mtl_value_cls_dict = {
    OBJ_mtl_config.DEF_mtl_porttype_closure: _mtlObjValue.Val_Closure,

    OBJ_mtl_config.DEF_mtl_porttype_shader: _mtlObjValue.Val_Closure,
    OBJ_mtl_config.DEF_mtl_porttype_visibility: _mtlObjValue.Val_Visibility,

    OBJ_mtl_config.DEF_mtl_porttype_boolean: _mtlObjValue.Val_Boolean,
    OBJ_mtl_config.DEF_mtl_porttype_Integer: _mtlObjValue.Val_Integer,
    OBJ_mtl_config.DEF_mtl_porttype_integerarray: _mtlObjValue.Val_IntegerArray,
    OBJ_mtl_config.DEF_mtl_porttype_float: _mtlObjValue.Val_Float,
    OBJ_mtl_config.DEF_mtl_porttype_floatarray: _mtlObjValue.Val_FloatArray,

    OBJ_mtl_config.DEF_mtl_porttype_color2: _mtlObjValue.Val_Color2,
    OBJ_mtl_config.DEF_mtl_porttype_color2array: _mtlObjValue.Val_Color2Array,
    OBJ_mtl_config.DEF_mtl_porttype_color3: _mtlObjValue.Val_Color3,
    OBJ_mtl_config.DEF_mtl_porttype_color3array: _mtlObjValue.Val_Color3Array,
    OBJ_mtl_config.DEF_mtl_porttype_color4: _mtlObjValue.Val_Color4,
    OBJ_mtl_config.DEF_mtl_porttype_color4array: _mtlObjValue.Val_Color4Array,

    OBJ_mtl_config.DEF_mtl_porttype_vector2: _mtlObjValue.Val_Vector2,
    OBJ_mtl_config.DEF_mtl_porttype_vector2array: _mtlObjValue.Val_Vector2Array,
    OBJ_mtl_config.DEF_mtl_porttype_vector3: _mtlObjValue.Val_Vector3,
    OBJ_mtl_config.DEF_mtl_porttype_vector3array: _mtlObjValue.Val_Vector3Array,
    OBJ_mtl_config.DEF_mtl_porttype_vector4: _mtlObjValue.Val_Vector4,
    OBJ_mtl_config.DEF_mtl_porttype_vector4array: _mtlObjValue.Val_Vector4Array,

    OBJ_mtl_config.DEF_mtl_porttype_matrix33: _mtlObjValue.Val_Matrix33,
    OBJ_mtl_config.DEF_mtl_porttype_matrix44: _mtlObjValue.Val_Matrix44,

    OBJ_mtl_config.DEF_mtl_porttype_string: _mtlObjValue.Val_String,
    OBJ_mtl_config.DEF_mtl_porttype_stringarray: _mtlObjValue.Val_StringArray,
    OBJ_mtl_config.DEF_mtl_porttype_filename: _mtlObjValue.Val_Filename,
    OBJ_mtl_config.DEF_mtl_porttype_nodename: _mtlObjValue.Val_Nodename,
    OBJ_mtl_config.DEF_mtl_porttype_nodenamearray: _mtlObjValue.Val_NodenameArray
}


class Node(mtlObjAbs.Abc_MtlNode):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_category = _mtlObjRaw.Category
    CLS_grh_nodepath = _mtlObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet

    OBJ_grh_query_cache = _mtlObjCache.OBJ_grh_query_cache
    OBJ_grh_obj_cache = _mtlObjCache.OBJ_grh_obj_cache

    VAR_grh_value_cls_dict = _DEF_mtl_value_cls_dict

    VAR_grh_port_cls_dict = {
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


class Geometry(mtlObjAbs.Abc_MtlGeometry):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_category = _mtlObjRaw.Category
    CLS_grh_nodepath = _mtlObjRaw.Nodepath

    CLS_grh_port_set = _grhObjSet.PortSet

    CLS_mtl_child_set = _mtlObjSet.GeometrySet
    CLS_mtl_material_set = _mtlObjSet.MaterialSet

    VAR_grh_value_cls_dict = _DEF_mtl_value_cls_dict

    VAR_grh_port_cls_dict = {
        OBJ_mtl_config.DEF_mtl_keyword_input: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_property: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_visibility: _mtlObjPort.Input,
        OBJ_mtl_config.DEF_mtl_keyword_output: _mtlObjPort.Output,
        OBJ_mtl_config.DEF_mtl_keyword_input_channel: _mtlObjPort.InputChannel,
        OBJ_mtl_config.DEF_mtl_keyword_output_channel: _mtlObjPort.OutputChannel
    }

    OBJ_grh_query_cache = _mtlObjCache.OBJ_grh_query_cache
    OBJ_grh_obj_cache = _mtlObjCache.OBJ_grh_obj_cache

    VAR_mtl_file_element_key = u'geometry'
    VAR_mtl_file_attribute_attach_key = u'geom'

    def __init__(self, *args):
        self._initAbcMtlGeometry(*args)


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
    CLS_mtl_node = Geometry

    CLS_mtl_port_proxy_set = _grhObjSet.ObjSet
    CLS_mtl_property = _mtlObjPort.Property
    CLS_mtl_visibility = _mtlObjPort.Visibility

    CLS_mtl_propertyset = _mtlObjPort.Propertyset

    VAR_mtl_file_element_key = u'geometry'

    def __init__(self, *args):
        self._initAbcMtlGeometryProxy(*args)
