# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet

from ..import mtlCfg, mtlObjAbs

from ..mtlObjects import _mtlObjRaw, _mtlObjValue, _mtlObjQuery


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


class Connector(mtlObjAbs.Abs_MtlConnector):
    OBJ_grh_obj_cache = _mtlObjQuery.GRH_OBJ_CACHE

    def __init__(self, *args):
        self._initAbsMtlConnector(*args)


class Param(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype

    CLS_grh_attrpath = _mtlObjRaw.Attrpath
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_dat_xml_file_element_tag = u'parameter'
    VAR_dat_xml_file_attribute_attach_tag = u'member'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class ParamChannel(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype

    CLS_grh_attrpath = _mtlObjRaw.Attrpath
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_dat_xml_file_element_tag = u'parameter'
    VAR_dat_xml_file_attribute_attach_tag = u'channels'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class Inparm(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype

    CLS_grh_attrpath = _mtlObjRaw.Attrpath
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_dat_xml_file_element_tag = u'input'
    VAR_dat_xml_file_attribute_attach_tag = u'member'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class InparmChannel(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype

    CLS_grh_attrpath = _mtlObjRaw.Attrpath
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_dat_xml_file_element_tag = u'input'
    VAR_dat_xml_file_attribute_attach_tag = u'channels'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class Otparm(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype

    CLS_grh_attrpath = _mtlObjRaw.Attrpath
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_dat_xml_file_element_tag = u'output'
    VAR_dat_xml_file_attribute_attach_tag = u'member'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


class OtparmChannel(mtlObjAbs.Abs_MtlPort):
    CLS_grh_type = _mtlObjRaw.Type
    CLS_grh_porttype = _mtlObjRaw.Porttype

    CLS_grh_attrpath = _mtlObjRaw.Attrpath
    CLS_grh_portpath = _mtlObjRaw.Portpath

    VAR_grh_value_cls_dict = _VAR_mtl_value_cls_dict

    VAR_dat_xml_file_element_tag = u'output'
    VAR_dat_xml_file_attribute_attach_tag = u'channels'

    def __init__(self, *args):
        self._initAbsMtlPort(*args)


# ******************************************************************************************************************** #
class BindParm(mtlObjAbs.Abs_MtlPortProxy):
    CLS_grh_name = _mtlObjRaw.Name

    VAR_dat_xml_file_element_tag = u'bindparam'

    def __init__(self, *args):
        self._initAbsMtlPortProxy(*args)


class BindInparm(mtlObjAbs.Abc_MtlInputProxy):
    CLS_grh_name = _mtlObjRaw.Name

    VAR_dat_xml_file_element_tag = u'bindinput'

    def __init__(self, *args):
        self._initAbcMtlInputProxy(*args)


class BindOtparm(mtlObjAbs.Abs_MtlPortProxy):
    CLS_grh_name = _mtlObjRaw.Name

    VAR_dat_xml_file_element_tag = u'bindoutput'

    def __init__(self, *args):
        self._initAbsMtlPortProxy(*args)


class NodeGraphOutput(mtlObjAbs.Abc_MtlNodeGraphOutput):
    CLS_grh_name = _mtlObjRaw.Name

    VAR_dat_xml_file_element_tag = u'output'
    VAR_dat_xml_file_attribute_attach_tag = u'output'

    def __init__(self, *args):
        self._initAbcMtlNodeGraphOutput(*args)


# ******************************************************************************************************************** #
class Property(mtlObjAbs.Abs_MtlPortProxy):
    CLS_grh_name = _mtlObjRaw.Name

    VAR_dat_xml_file_element_tag = u'property'

    def __init__(self, *args):
        self._initAbsMtlPortProxy(*args)


class Visibility(mtlObjAbs.Abs_MtlPortProxy):
    CLS_grh_name = _mtlObjRaw.Name

    VAR_dat_xml_file_element_tag = u'visibility'

    def __init__(self, *args):
        self._initAbsMtlPortProxy(*args)


class Propertyset(mtlObjAbs.Abc_MtlPortset):
    CLS_mtl_name = _mtlObjRaw.Name

    CLS_grh_port_set = _grhObjSet.ObjSet

    VAR_dat_xml_file_element_tag = u'propertyset'
    VAR_dat_xml_file_attribute_attach_tag = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry dagpath)
        """
        self._initAbcMtlPortset(*args)
