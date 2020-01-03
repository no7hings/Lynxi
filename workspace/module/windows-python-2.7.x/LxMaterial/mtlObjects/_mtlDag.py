# coding:utf-8
from LxMaterial import mtlCore

from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlObjectSet, _mtlDefinition, _mtlPort, _mtlValue


VALUE_CLS_DIC = {
    mtlCore.Value_Type_Closure: _mtlValue.Val_Closure,

    mtlCore.Value_Type_Boolean: _mtlValue.Val_Boolean,
    mtlCore.Value_Type_Integer: _mtlValue.Val_Integer,
    mtlCore.Value_Type_Integer_Array: _mtlValue.Val_IntegerArray,
    mtlCore.Value_Type_Float: _mtlValue.Val_Float,
    mtlCore.Value_Type_Float_Array: _mtlValue.Val_FloatArray,

    mtlCore.Value_Type_Color2: _mtlValue.Val_Color2,
    mtlCore.Value_Type_Color2_Array: _mtlValue.Val_Color2Array,
    mtlCore.Value_Type_Color3: _mtlValue.Val_Color3,
    mtlCore.Value_Type_Color3_Array: _mtlValue.Val_Color3Array,
    mtlCore.Value_Type_Color4: _mtlValue.Val_Color4,
    mtlCore.Value_Type_Color4_Array: _mtlValue.Val_Color4Array,

    mtlCore.Value_Type_Vector2: _mtlValue.Val_Vector2,
    mtlCore.Value_Type_Vector2_Array: _mtlValue.Val_Vector2Array,
    mtlCore.Value_Type_Vector3: _mtlValue.Val_Vector3,
    mtlCore.Value_Type_Vector3_Array: _mtlValue.Val_Vector3Array,
    mtlCore.Value_Type_Vector4: _mtlValue.Val_Vector4,
    mtlCore.Value_Type_Vector4_Array: _mtlValue.Val_Vector4Array,

    mtlCore.Value_Type_Matrix33: _mtlValue.Val_Matrix33,
    mtlCore.Value_Type_Matrix44: _mtlValue.Val_Matrix44,

    mtlCore.Value_Type_String: _mtlValue.Val_String,
    mtlCore.Value_Type_String_Array: _mtlValue.Val_StringArray,
    mtlCore.Value_Type_FileName: _mtlValue.Val_FileName,
    mtlCore.Value_Type_GeometryName: _mtlValue.Val_GeometryName,
    mtlCore.Value_Type_GeometryName_Array: _mtlValue.Val_GeometryNameArray
}


class Dag_SurfaceShader(mtlAbstract.Abc_Shader):
    RAW_TYPE_CLS = _mtlRaw.Raw_Type

    RAW_CATEGORY_CLS = _mtlRaw.Raw_Category
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlObjectSet.Set_Dag
    SET_ATTRIBUTE_CLS = _mtlObjectSet.Set_Attribute

    PORT_CLS = _mtlPort.Prt_Shaderinput

    DEF_CLS = _mtlDefinition.Def_Node

    value_cls_dic = VALUE_CLS_DIC

    xml_prefix_label = 'shaderref'
    shader_output_type_string = 'surfaceshader'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcShader(*args)


class Dag_DisplacementShader(mtlAbstract.Abc_Shader):
    RAW_TYPE_CLS = _mtlRaw.Raw_Type

    RAW_CATEGORY_CLS = _mtlRaw.Raw_Category
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlObjectSet.Set_Dag
    SET_ATTRIBUTE_CLS = _mtlObjectSet.Set_Attribute

    PORT_CLS = _mtlPort.Prt_Shaderinput

    DEF_CLS = _mtlDefinition.Def_Node

    value_cls_dic = VALUE_CLS_DIC

    xml_prefix_label = 'shaderref'
    shader_output_type_string = 'displacementshader'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcShader(*args)


class Dag_VolumeShader(mtlAbstract.Abc_Shader):
    RAW_TYPE_CLS = _mtlRaw.Raw_Type

    RAW_CATEGORY_CLS = _mtlRaw.Raw_Category
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlObjectSet.Set_Dag
    SET_ATTRIBUTE_CLS = _mtlObjectSet.Set_Attribute

    PORT_CLS = _mtlPort.Prt_Shaderinput

    DEF_CLS = _mtlDefinition.Def_Node

    value_cls_dic = VALUE_CLS_DIC

    xml_prefix_label = 'shaderref'
    shader_output_type_string = 'volumeshader'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcShader(*args)


class Dag_Node(mtlAbstract.Abc_Dag):
    RAW_TYPE_CLS = _mtlRaw.Raw_Type

    RAW_CATEGORY_CLS = _mtlRaw.Raw_Category
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlObjectSet.Set_Dag
    SET_ATTRIBUTE_CLS = _mtlObjectSet.Set_Attribute

    DEF_CLS = _mtlDefinition.Def_Node

    def __init__(self, *args):
        self._initAbcDag(*args)


class Dag_Geometry(mtlAbstract.Abc_Geometry):
    RAW_TYPE_CLS = _mtlRaw.Raw_Type

    RAW_CATEGORY_CLS = _mtlRaw.Raw_Category
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlObjectSet.Set_Dag
    SET_ATTRIBUTE_CLS = _mtlObjectSet.Set_Attribute

    DEF_CLS = _mtlDefinition.Def_Node

    xml_prefix_label = 'geom'

    def __init__(self, *args):
        self._initAbcDag(*args)
