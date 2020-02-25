# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjDefinition, _mtlObjAttribute, _mtlObjValue


DEF_CLS_VALUE = {
    mtlConfigure.Utility.DEF_mtl_datatype_closure: _mtlObjValue.Val_Closure,

    mtlConfigure.Utility.DEF_mtl_datatype_boolean: _mtlObjValue.Val_Boolean,
    mtlConfigure.Utility.DEF_mtl_datatype_Integer: _mtlObjValue.Val_Integer,
    mtlConfigure.Utility.DEF_mtl_datatype_integer_array: _mtlObjValue.Val_IntegerArray,
    mtlConfigure.Utility.DEF_mtl_datatype_float: _mtlObjValue.Val_Float,
    mtlConfigure.Utility.DEF_mtl_datatype_float_array: _mtlObjValue.Val_FloatArray,

    mtlConfigure.Utility.DEF_mtl_datatype_color2: _mtlObjValue.Val_Color2,
    mtlConfigure.Utility.DEF_mtl_datatype_color2_array: _mtlObjValue.Val_Color2Array,
    mtlConfigure.Utility.DEF_mtl_datatype_color3: _mtlObjValue.Val_Color3,
    mtlConfigure.Utility.DEF_mtl_datatype_color3_array: _mtlObjValue.Val_Color3Array,
    mtlConfigure.Utility.DEF_mtl_datatype_color4: _mtlObjValue.Val_Color4,
    mtlConfigure.Utility.DEF_mtl_datatype_color4_array: _mtlObjValue.Val_Color4Array,

    mtlConfigure.Utility.DEF_mtl_datatype_vector2: _mtlObjValue.Val_vector2,
    mtlConfigure.Utility.DEF_mtl_datatype_vector2_array: _mtlObjValue.Val_vector2Array,
    mtlConfigure.Utility.DEF_mtl_datatype_vector3: _mtlObjValue.Val_vector3,
    mtlConfigure.Utility.DEF_mtl_datatype_vector3_array: _mtlObjValue.Val_vector3Array,
    mtlConfigure.Utility.DEF_mtl_datatype_vector4: _mtlObjValue.Val_vector4,
    mtlConfigure.Utility.DEF_mtl_datatype_vector4_array: _mtlObjValue.Val_vector4Array,

    mtlConfigure.Utility.DEF_mtl_datatype_matrix33: _mtlObjValue.Val_matrix33,
    mtlConfigure.Utility.DEF_mtl_datatype_matrix44: _mtlObjValue.Val_matrix44,

    mtlConfigure.Utility.DEF_mtl_datatype_string: _mtlObjValue.Val_string,
    mtlConfigure.Utility.DEF_mtl_datatype_string_array: _mtlObjValue.Val_stringArray,
    mtlConfigure.Utility.DEF_mtl_datatype_file_name: _mtlObjValue.Val_file_name,
    mtlConfigure.Utility.DEF_mtl_datatype_geometry_name: _mtlObjValue.Val_geometry_name,
    mtlConfigure.Utility.DEF_mtl_datatype_geometry_name_array: _mtlObjValue.Val_geometry_nameArray
}


class Geometry(mtlObjCore.Abc_MtlGeometry):
    CLS_mtl_node_dagpath = _mtlObjRaw.Raw_NodeDagpath

    CLS_mtl_property_set = _mtlObjSet.Set_Property
    CLS_mtl_visibility_assign = _mtlObjSet.Set_Visibility

    CLS_mtl_property = _mtlObjAttribute.GeometryProperty
    CLS_mtl_visibility = _mtlObjAttribute.GeometryVisibility
    CLS_mtl_geometry_def = _mtlObjDefinition.GeometryDef

    VAR_mtl_value_class_dict = DEF_CLS_VALUE

    VAR_mtl_file_element_key = 'geom'

    def __init__(self, *args):
        self._initAbcMtlGeometry(*args)


class Shader(mtlObjCore.Abc_MtlShader):
    CLS_mtl_type = _mtlObjRaw.Raw_Type
    CLS_mtl_category = _mtlObjRaw.Raw_ShaderCategory
    CLS_mtl_node_dagpath = _mtlObjRaw.Raw_NodeDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute
    CLS_mtl_child_set = _mtlObjSet.Set_Dag

    CLS_mtl_input = _mtlObjAttribute.ShaderInput
    CLS_mtl_output = _mtlObjAttribute.ShaderOutput
    CLS_mtl_node_def = _mtlObjDefinition.NodeDef

    VAR_mtl_value_class_dict = DEF_CLS_VALUE

    VAR_mtl_file_element_key = 'shaderref'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcMtlShader(*args)


class Node(mtlObjCore.Abc_MtlNode):
    CLS_mtl_type = _mtlObjRaw.Raw_Type
    CLS_mtl_category = _mtlObjRaw.Raw_Category
    CLS_mtl_node_dagpath = _mtlObjRaw.Raw_NodeDagpath

    CLS_mtl_attribute_set = _mtlObjSet.Set_Attribute
    CLS_mtl_child_set = _mtlObjSet.Set_Dag

    CLS_mtl_input = _mtlObjAttribute.NodeInput
    CLS_mtl_output = _mtlObjAttribute.NodeOutput
    CLS_mtl_node_def = _mtlObjDefinition.NodeDef

    VAR_mtl_value_class_dict = DEF_CLS_VALUE

    VAR_mtl_file_attribute_key = 'nodename'

    def __init__(self, *args):
        self._initAbcMtlNode(*args)

