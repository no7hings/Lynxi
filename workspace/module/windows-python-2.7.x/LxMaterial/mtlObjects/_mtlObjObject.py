# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjCache, _mtlObjAttribute, _mtlObjValue


OBJ_mtl_config = mtlConfigure.Utility
DEF_mtl_value_cls_dict = {
    OBJ_mtl_config.DEF_mtl_datatype_closure: _mtlObjValue.Val_Closure,

    OBJ_mtl_config.DEF_mtl_datatype_boolean: _mtlObjValue.Val_Boolean,
    OBJ_mtl_config.DEF_mtl_datatype_Integer: _mtlObjValue.Val_Integer,
    OBJ_mtl_config.DEF_mtl_datatype_integer_array: _mtlObjValue.Val_IntegerArray,
    OBJ_mtl_config.DEF_mtl_datatype_float: _mtlObjValue.Val_Float,
    OBJ_mtl_config.DEF_mtl_datatype_float_array: _mtlObjValue.Val_FloatArray,

    OBJ_mtl_config.DEF_mtl_datatype_color2: _mtlObjValue.Val_Color2,
    OBJ_mtl_config.DEF_mtl_datatype_color2_array: _mtlObjValue.Val_Color2Array,
    OBJ_mtl_config.DEF_mtl_datatype_color3: _mtlObjValue.Val_Color3,
    OBJ_mtl_config.DEF_mtl_datatype_color3_array: _mtlObjValue.Val_Color3Array,
    OBJ_mtl_config.DEF_mtl_datatype_color4: _mtlObjValue.Val_Color4,
    OBJ_mtl_config.DEF_mtl_datatype_color4_array: _mtlObjValue.Val_Color4Array,

    OBJ_mtl_config.DEF_mtl_datatype_vector2: _mtlObjValue.Val_vector2,
    OBJ_mtl_config.DEF_mtl_datatype_vector2_array: _mtlObjValue.Val_vector2Array,
    OBJ_mtl_config.DEF_mtl_datatype_vector3: _mtlObjValue.Val_vector3,
    OBJ_mtl_config.DEF_mtl_datatype_vector3_array: _mtlObjValue.Val_vector3Array,
    OBJ_mtl_config.DEF_mtl_datatype_vector4: _mtlObjValue.Val_vector4,
    OBJ_mtl_config.DEF_mtl_datatype_vector4_array: _mtlObjValue.Val_vector4Array,

    OBJ_mtl_config.DEF_mtl_datatype_matrix33: _mtlObjValue.Val_matrix33,
    OBJ_mtl_config.DEF_mtl_datatype_matrix44: _mtlObjValue.Val_matrix44,

    OBJ_mtl_config.DEF_mtl_datatype_string: _mtlObjValue.Val_string,
    OBJ_mtl_config.DEF_mtl_datatype_string_array: _mtlObjValue.Val_stringArray,
    OBJ_mtl_config.DEF_mtl_datatype_file_name: _mtlObjValue.Val_file_name,
    OBJ_mtl_config.DEF_mtl_datatype_geometry_name: _mtlObjValue.Val_geometry_name,
    OBJ_mtl_config.DEF_mtl_datatype_geometry_name_array: _mtlObjValue.Val_geometry_nameArray
}


class Node(mtlObjCore.Abc_MtlNode):
    CLS_mtl_type = _mtlObjRaw.TypeString
    CLS_mtl_category = _mtlObjRaw.NodeCategoryString
    CLS_mtl_node_dagpath = _mtlObjRaw.Raw_NodeDagpath

    CLS_mtl_port_set = _mtlObjSet.PortSet

    CLS_mtl_source_object = None

    OBJ_mtl_def_cache = _mtlObjCache.OBJ_mtl_def_cache
    OBJ_mtl_obj_cache = _mtlObjCache.OBJ_mtl_obj_cache

    VAR_mtl_value_class_dict = DEF_mtl_value_cls_dict

    VAR_mtl_port_class_dict = {
        OBJ_mtl_config.DEF_mtl_keyword_input: _mtlObjAttribute.NodeInput,
        OBJ_mtl_config.DEF_mtl_keyword_output: _mtlObjAttribute.NodeOutput,
        (OBJ_mtl_config.DEF_mtl_keyword_input, OBJ_mtl_config.DEF_mtl_keyword_channel): _mtlObjAttribute.NodeInputChannel,
        (OBJ_mtl_config.DEF_mtl_keyword_output, OBJ_mtl_config.DEF_mtl_keyword_channel): _mtlObjAttribute.NodeOutputChannel
    }

    VAR_mtl_file_attribute_key = 'nodename'

    def __init__(self, *args):
        self._initAbcMtlNode(*args)


class NodeGraph(mtlObjCore.Abc_MtlNodeGraph):
    CLS_mtl_name = _mtlObjRaw.NameString

    CLS_mtl_node_set = _mtlObjSet.ObjectSet
    CLS_mtl_output_set = _mtlObjSet.PortSet

    CLS_mtl_node = Node
    CLS_mtl_node_graph_output = _mtlObjAttribute.NodeGraphOutput

    VAR_mtl_file_element_key = u'nodegraph'
    VAR_mtl_file_attribute_key = u'nodegraph'

    def __init__(self, *args):
        self._initAbcMtlNodeGraph(*args)


class Shader(mtlObjCore.Abc_MtlShader):
    CLS_mtl_type = _mtlObjRaw.TypeString
    CLS_mtl_category = _mtlObjRaw.ShaderCategoryString
    CLS_mtl_node_dagpath = _mtlObjRaw.Raw_NodeDagpath

    CLS_mtl_port_set = _mtlObjSet.PortSet

    CLS_mtl_source_object = Node

    CLS_mtl_node_graph_set = _mtlObjSet.NodeGraphSet
    CLS_mtl_node_graph = NodeGraph

    OBJ_mtl_def_cache = _mtlObjCache.OBJ_mtl_def_cache
    OBJ_mtl_obj_cache = _mtlObjCache.OBJ_mtl_obj_cache

    VAR_mtl_value_class_dict = DEF_mtl_value_cls_dict
    VAR_mtl_port_class_dict = {
        OBJ_mtl_config.DEF_mtl_keyword_input: _mtlObjAttribute.ShaderInput,
        OBJ_mtl_config.DEF_mtl_keyword_output: _mtlObjAttribute.ShaderOutput,
        (OBJ_mtl_config.DEF_mtl_keyword_input, OBJ_mtl_config.DEF_mtl_keyword_channel): _mtlObjAttribute.ShaderInputChannel,
        (OBJ_mtl_config.DEF_mtl_keyword_output, OBJ_mtl_config.DEF_mtl_keyword_channel): _mtlObjAttribute.ShaderOutputChannel
    }

    VAR_mtl_file_element_key = u'shaderref'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcMtlShader(*args)


class Material(mtlObjCore.Abc_MtlMaterial):
    CLS_mtl_type = _mtlObjRaw.TypeString
    CLS_mtl_category = _mtlObjRaw.NodeCategoryString
    CLS_mtl_node_dagpath = _mtlObjRaw.Raw_MaterialDagpath

    CLS_mtl_port_set = _mtlObjSet.PortSet

    CLS_mtl_source_object = Shader

    OBJ_mtl_def_cache = _mtlObjCache.OBJ_mtl_def_cache
    OBJ_mtl_obj_cache = _mtlObjCache.OBJ_mtl_obj_cache

    VAR_mtl_value_class_dict = DEF_mtl_value_cls_dict
    VAR_mtl_port_class_dict = {
        OBJ_mtl_config.DEF_mtl_keyword_input: _mtlObjAttribute.MaterialInput,
        OBJ_mtl_config.DEF_mtl_keyword_output: _mtlObjAttribute.MaterialOutput,
        (OBJ_mtl_config.DEF_mtl_keyword_input, OBJ_mtl_config.DEF_mtl_keyword_channel): _mtlObjAttribute.NodeInputChannel,
        (OBJ_mtl_config.DEF_mtl_keyword_output, OBJ_mtl_config.DEF_mtl_keyword_channel): _mtlObjAttribute.NodeOutputChannel
    }

    VAR_mtl_file_element_key = u'material'
    VAR_mtl_file_attribute_key = u'material'

    def __init__(self, *args):
        """
        * 1.maya: shading engine name
        :param args: str(shader set name)
        """
        self._initAbcMtlMaterial(*args)


class Geometry(mtlObjCore.Abc_MtlGeometry):
    CLS_mtl_type = _mtlObjRaw.TypeString
    CLS_mtl_category = _mtlObjRaw.NodeCategoryString
    CLS_mtl_node_dagpath = _mtlObjRaw.Raw_NodeDagpath

    CLS_mtl_port_set = _mtlObjSet.PortSet

    CLS_mtl_property_set = _mtlObjSet.PropertySet
    CLS_mtl_visibility_set = _mtlObjSet.VisibilitySet

    VAR_mtl_value_class_dict = DEF_mtl_value_cls_dict

    VAR_mtl_port_class_dict = {
        OBJ_mtl_config.DEF_mtl_keyword_input: _mtlObjAttribute.NodeInput,
        OBJ_mtl_config.DEF_mtl_keyword_output: _mtlObjAttribute.NodeOutput,
        (OBJ_mtl_config.DEF_mtl_keyword_input, OBJ_mtl_config.DEF_mtl_keyword_channel): _mtlObjAttribute.NodeInputChannel,
        (OBJ_mtl_config.DEF_mtl_keyword_output, OBJ_mtl_config.DEF_mtl_keyword_channel): _mtlObjAttribute.NodeOutputChannel,
        OBJ_mtl_config.DEF_mtl_keyword_property: _mtlObjAttribute.GeometryProperty,
        OBJ_mtl_config.DEF_mtl_keyword_visibility: _mtlObjAttribute.GeometryVisibility,
    }

    OBJ_mtl_def_cache = _mtlObjCache.OBJ_mtl_def_cache
    OBJ_mtl_obj_cache = _mtlObjCache.OBJ_mtl_obj_cache

    VAR_mtl_file_element_key = u'geom'

    def __init__(self, *args):
        self._initAbcMtlGeometry(*args)
