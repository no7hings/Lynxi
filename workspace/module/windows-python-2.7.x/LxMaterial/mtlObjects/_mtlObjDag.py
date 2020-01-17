# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjDefinition, _mtlObjPort, _mtlObjValue


DIC_CLS_VALUE = {
    mtlConfigure.Value_Type_Closure: _mtlObjValue.Val_Closure,

    mtlConfigure.Value_Type_Boolean: _mtlObjValue.Val_Boolean,
    mtlConfigure.Value_Type_Integer: _mtlObjValue.Val_Integer,
    mtlConfigure.Value_Type_Integer_Array: _mtlObjValue.Val_IntegerArray,
    mtlConfigure.Value_Type_Float: _mtlObjValue.Val_Float,
    mtlConfigure.Value_Type_Float_Array: _mtlObjValue.Val_FloatArray,

    mtlConfigure.Value_Type_Color2: _mtlObjValue.Val_Color2,
    mtlConfigure.Value_Type_Color2_Array: _mtlObjValue.Val_Color2Array,
    mtlConfigure.Value_Type_Color3: _mtlObjValue.Val_Color3,
    mtlConfigure.Value_Type_Color3_Array: _mtlObjValue.Val_Color3Array,
    mtlConfigure.Value_Type_Color4: _mtlObjValue.Val_Color4,
    mtlConfigure.Value_Type_Color4_Array: _mtlObjValue.Val_Color4Array,

    mtlConfigure.Value_Type_Vector2: _mtlObjValue.Val_Vector2,
    mtlConfigure.Value_Type_Vector2_Array: _mtlObjValue.Val_Vector2Array,
    mtlConfigure.Value_Type_Vector3: _mtlObjValue.Val_Vector3,
    mtlConfigure.Value_Type_Vector3_Array: _mtlObjValue.Val_Vector3Array,
    mtlConfigure.Value_Type_Vector4: _mtlObjValue.Val_Vector4,
    mtlConfigure.Value_Type_Vector4_Array: _mtlObjValue.Val_Vector4Array,

    mtlConfigure.Value_Type_Matrix33: _mtlObjValue.Val_Matrix33,
    mtlConfigure.Value_Type_Matrix44: _mtlObjValue.Val_Matrix44,

    mtlConfigure.Value_Type_String: _mtlObjValue.Val_String,
    mtlConfigure.Value_Type_String_Array: _mtlObjValue.Val_StringArray,
    mtlConfigure.Value_Type_FileName: _mtlObjValue.Val_FileName,
    mtlConfigure.Value_Type_GeometryName: _mtlObjValue.Val_GeometryName,
    mtlConfigure.Value_Type_GeometryName_Array: _mtlObjValue.Val_GeometryNameArray
}


class Geometry(mtlAbstract.Abc_Geometry):
    CLS_raw_type = _mtlObjRaw.Raw_Type
    CLS_raw_category = _mtlObjRaw.Raw_NodeCategory
    CLS_raw_dagpath = _mtlObjRaw.Raw_NodePath

    CLS_set_input = _mtlObjSet.Set_Input
    CLS_set_output = _mtlObjSet.Set_Output
    CLS_set_child = _mtlObjSet.Set_Dag

    CLS_input = _mtlObjPort.Property
    CLS_output = _mtlObjPort.GeometryOutput
    CLS_definition = _mtlObjDefinition.Def_Node

    DIC_cls_value = DIC_CLS_VALUE

    STR_mtlx_key_element = 'geom'

    def __init__(self, *args):
        self._initAbcGeometry('geometry', *args)


class Shader(mtlAbstract.Abc_Shader):
    CLS_raw_type = _mtlObjRaw.Raw_Type
    CLS_raw_category = _mtlObjRaw.Raw_ShaderCategory
    CLS_raw_dagpath = _mtlObjRaw.Raw_NodePath

    CLS_set_input = _mtlObjSet.Set_Input
    CLS_set_output = _mtlObjSet.Set_Output
    CLS_set_child = _mtlObjSet.Set_Dag

    CLS_input = _mtlObjPort.ShaderInput
    CLS_output = _mtlObjPort.ShaderOutput
    CLS_definition = _mtlObjDefinition.Def_Node

    DIC_cls_value = DIC_CLS_VALUE

    STR_mtlx_key_element = 'shaderref'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcShader(*args)


class Node(mtlAbstract.Abc_Node):
    CLS_raw_type = _mtlObjRaw.Raw_Type
    CLS_raw_category = _mtlObjRaw.Raw_NodeCategory
    CLS_raw_dagpath = _mtlObjRaw.Raw_NodePath

    CLS_set_input = _mtlObjSet.Set_Input
    CLS_set_output = _mtlObjSet.Set_Output
    CLS_set_child = _mtlObjSet.Set_Dag

    CLS_input = _mtlObjPort.NodeInput
    CLS_output = _mtlObjPort.NodeOutput
    CLS_definition = _mtlObjDefinition.Def_Node

    DIC_cls_value = DIC_CLS_VALUE

    STR_mtlx_key_attribute = 'nodename'

    def __init__(self, *args):
        self._initAbcNode(*args)

