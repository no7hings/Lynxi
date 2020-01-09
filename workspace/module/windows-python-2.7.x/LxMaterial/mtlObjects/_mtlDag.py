# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlSet, _mtlDefinition, _mtlPort, _mtlValue


VALUE_CLS_DIC = {
    mtlConfigure.Value_Type_Closure: _mtlValue.Val_Closure,

    mtlConfigure.Value_Type_Boolean: _mtlValue.Val_Boolean,
    mtlConfigure.Value_Type_Integer: _mtlValue.Val_Integer,
    mtlConfigure.Value_Type_Integer_Array: _mtlValue.Val_IntegerArray,
    mtlConfigure.Value_Type_Float: _mtlValue.Val_Float,
    mtlConfigure.Value_Type_Float_Array: _mtlValue.Val_FloatArray,

    mtlConfigure.Value_Type_Color2: _mtlValue.Val_Color2,
    mtlConfigure.Value_Type_Color2_Array: _mtlValue.Val_Color2Array,
    mtlConfigure.Value_Type_Color3: _mtlValue.Val_Color3,
    mtlConfigure.Value_Type_Color3_Array: _mtlValue.Val_Color3Array,
    mtlConfigure.Value_Type_Color4: _mtlValue.Val_Color4,
    mtlConfigure.Value_Type_Color4_Array: _mtlValue.Val_Color4Array,

    mtlConfigure.Value_Type_Vector2: _mtlValue.Val_Vector2,
    mtlConfigure.Value_Type_Vector2_Array: _mtlValue.Val_Vector2Array,
    mtlConfigure.Value_Type_Vector3: _mtlValue.Val_Vector3,
    mtlConfigure.Value_Type_Vector3_Array: _mtlValue.Val_Vector3Array,
    mtlConfigure.Value_Type_Vector4: _mtlValue.Val_Vector4,
    mtlConfigure.Value_Type_Vector4_Array: _mtlValue.Val_Vector4Array,

    mtlConfigure.Value_Type_Matrix33: _mtlValue.Val_Matrix33,
    mtlConfigure.Value_Type_Matrix44: _mtlValue.Val_Matrix44,

    mtlConfigure.Value_Type_String: _mtlValue.Val_String,
    mtlConfigure.Value_Type_String_Array: _mtlValue.Val_StringArray,
    mtlConfigure.Value_Type_FileName: _mtlValue.Val_FileName,
    mtlConfigure.Value_Type_GeometryName: _mtlValue.Val_GeometryName,
    mtlConfigure.Value_Type_GeometryName_Array: _mtlValue.Val_GeometryNameArray
}


class Dag_SurfaceShader(mtlAbstract.Abc_DagShader):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_TYPE_CLS = _mtlRaw.Raw_Type
    RAW_CATEGORY_CLS = _mtlRaw.Raw_ShaderCategory
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath

    SET_PORT_INPUT_CLS = _mtlSet.Set_Port
    SET_CHILD_CLS = _mtlSet.Set_Dag

    PORT_INPUT_CLS = _mtlPort.Prt_Shaderinput
    PORT_OUTPUT_ClS = _mtlPort.Prt_Shaderoutput

    DEF_CLS = _mtlDefinition.Def_Node

    value_cls_dic = VALUE_CLS_DIC

    xml_key_element = 'shaderref'

    port_output_name_string = 'surfaceshader'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcShader(*args)


class Dag_DisplacementShader(mtlAbstract.Abc_DagShader):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_TYPE_CLS = _mtlRaw.Raw_Type
    RAW_CATEGORY_CLS = _mtlRaw.Raw_ShaderCategory
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath

    SET_PORT_INPUT_CLS = _mtlSet.Set_Port
    SET_CHILD_CLS = _mtlSet.Set_Dag

    PORT_INPUT_CLS = _mtlPort.Prt_Shaderinput
    PORT_OUTPUT_ClS = _mtlPort.Prt_Shaderoutput

    DEF_CLS = _mtlDefinition.Def_Node

    value_cls_dic = VALUE_CLS_DIC

    xml_key_element = 'shaderref'

    port_output_name_string = 'displacementshader'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcShader(*args)


class Dag_VolumeShader(mtlAbstract.Abc_DagShader):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_TYPE_CLS = _mtlRaw.Raw_Type
    RAW_CATEGORY_CLS = _mtlRaw.Raw_ShaderCategory
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath

    SET_PORT_INPUT_CLS = _mtlSet.Set_Port
    SET_CHILD_CLS = _mtlSet.Set_Dag

    PORT_INPUT_CLS = _mtlPort.Prt_Shaderinput
    PORT_OUTPUT_ClS = _mtlPort.Prt_Shaderoutput

    DEF_CLS = _mtlDefinition.Def_Node

    value_cls_dic = VALUE_CLS_DIC

    xml_key_element = 'shaderref'

    port_output_name_string = 'volumeshader'

    def __init__(self, *args):
        """
        :param args: str(shader_category), str(shader_name)
        """
        self._initAbcShader(*args)


class Dag_Node(mtlAbstract.Abc_Dag):
    RAW_TYPE_CLS = _mtlRaw.Raw_Type

    RAW_CATEGORY_CLS = _mtlRaw.Raw_NodeCategory
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlSet.Set_Dag
    SET_PORT_INPUT_CLS = _mtlSet.Set_Port

    DEF_CLS = _mtlDefinition.Def_Node

    def __init__(self, *args):
        self._initAbcDag(*args)


class Dag_Geometry(mtlAbstract.Abc_DagGeometry):
    RAW_TYPE_CLS = _mtlRaw.Raw_Type

    RAW_CATEGORY_CLS = _mtlRaw.Raw_NodeCategory
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlSet.Set_Dag
    SET_PORT_INPUT_CLS = _mtlSet.Set_Port

    DEF_CLS = _mtlDefinition.Def_Node

    xml_key_element = 'geom'

    def __init__(self, *args):
        self._initAbcDag('geometry', *args)
