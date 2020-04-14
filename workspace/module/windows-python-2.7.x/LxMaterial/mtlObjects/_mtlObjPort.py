# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet

from ..import mtlCfg, mtlObjAbs

from ..mtlObjects import _mtlObjRaw, _mtlObjValue


_OBJ_mtl_config = mtlCfg.Utility
_VAR_mtl_value_cls_dict = {
    _OBJ_mtl_config.DEF_mtl_porttype_closure: _mtlObjValue.Val_Closure,

    _OBJ_mtl_config.DEF_mtl_porttype_shader: _mtlObjValue.Val_Closure,
    _OBJ_mtl_config.DEF_mtl_porttype_visibility: _mtlObjValue.Val_Visibility,

    _OBJ_mtl_config.DEF_mtl_porttype_boolean: _mtlObjValue.Val_Boolean,
    _OBJ_mtl_config.DEF_mtl_porttype_Integer: _mtlObjValue.Val_Integer,
    _OBJ_mtl_config.DEF_mtl_porttype_integerarray: _mtlObjValue.Val_IntegerArray,
    _OBJ_mtl_config.DEF_mtl_porttype_float: _mtlObjValue.Val_Float,
    _OBJ_mtl_config.DEF_mtl_porttype_floatarray: _mtlObjValue.Val_FloatArray,

    _OBJ_mtl_config.DEF_mtl_porttype_color2: _mtlObjValue.Val_Color2,
    _OBJ_mtl_config.DEF_mtl_porttype_color2array: _mtlObjValue.Val_Color2Array,
    _OBJ_mtl_config.DEF_mtl_porttype_color3: _mtlObjValue.Val_Color3,
    _OBJ_mtl_config.DEF_mtl_porttype_color3array: _mtlObjValue.Val_Color3Array,
    _OBJ_mtl_config.DEF_mtl_porttype_color4: _mtlObjValue.Val_Color4,
    _OBJ_mtl_config.DEF_mtl_porttype_color4array: _mtlObjValue.Val_Color4Array,

    _OBJ_mtl_config.DEF_mtl_porttype_vector2: _mtlObjValue.Val_Vector2,
    _OBJ_mtl_config.DEF_mtl_porttype_vector2array: _mtlObjValue.Val_Vector2Array,
    _OBJ_mtl_config.DEF_mtl_porttype_vector3: _mtlObjValue.Val_Vector3,
    _OBJ_mtl_config.DEF_mtl_porttype_vector3array: _mtlObjValue.Val_Vector3Array,
    _OBJ_mtl_config.DEF_mtl_porttype_vector4: _mtlObjValue.Val_Vector4,
    _OBJ_mtl_config.DEF_mtl_porttype_vector4array: _mtlObjValue.Val_Vector4Array,

    _OBJ_mtl_config.DEF_mtl_porttype_matrix33: _mtlObjValue.Val_Matrix33,
    _OBJ_mtl_config.DEF_mtl_porttype_matrix44: _mtlObjValue.Val_Matrix44,

    _OBJ_mtl_config.DEF_mtl_porttype_string: _mtlObjValue.Val_String,
    _OBJ_mtl_config.DEF_mtl_porttype_stringarray: _mtlObjValue.Val_StringArray,
    _OBJ_mtl_config.DEF_mtl_porttype_filename: _mtlObjValue.Val_Filename,
    _OBJ_mtl_config.DEF_mtl_porttype_nodename: _mtlObjValue.Val_Nodename,
    _OBJ_mtl_config.DEF_mtl_porttype_nodenamearray: _mtlObjValue.Val_NodenameArray
}


class Param(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_mtl_file_element_key = u'parameter'
    VAR_mtl_file_attribute_attach_key = u'member'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class ParamChannel(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_mtl_file_element_key = u'parameter'
    VAR_mtl_file_attribute_attach_key = u'channels'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class Input(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_attach_key = u'member'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class InputChannel(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_mtl_file_element_key = u'input'
    VAR_mtl_file_attribute_attach_key = u'channels'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class Output(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'member'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class OutputChannel(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'channels'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class NodeGraphOutput(mtlObjAbs.Abc_MtlNodeGraphOutput):
    CLS_mtl_name = _mtlObjRaw.Name

    VAR_mtl_file_element_key = u'output'
    VAR_mtl_file_attribute_attach_key = u'output'

    def __init__(self, *args):
        self._initAbcMtlNodeGraphOutput(*args)


class BindInput(mtlObjAbs.Abc_MtlBindInput):
    CLS_mtl_name = _mtlObjRaw.Name

    VAR_mtl_file_element_key = u'bindinput'

    def __init__(self, *args):
        self._initAbcMtlBindInput(*args)


class Property(mtlObjAbs.Abc_MtlProperty):
    CLS_mtl_name = _mtlObjRaw.Name

    VAR_mtl_file_element_key = u'property'

    def __init__(self, *args):
        self._initAbcMtlProperty(*args)


class Visibility(mtlObjAbs.Abs_MtlVisibility):
    CLS_mtl_name = _mtlObjRaw.Name

    VAR_mtl_file_element_key = u'visibility'

    def __init__(self, *args):
        self._initAbsMtlVisibility(*args)


class Propertyset(mtlObjAbs.Abc_MtlPropertyset):
    CLS_mtl_name = _mtlObjRaw.Name

    CLS_grh_port_set = _grhObjSet.ObjSet

    VAR_mtl_file_element_key = u'propertyset'
    VAR_mtl_file_attribute_attach_key = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry dagpath)
        """
        self._initAbcMtlPropertyset(*args)
