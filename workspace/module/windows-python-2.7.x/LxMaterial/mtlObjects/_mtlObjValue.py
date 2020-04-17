# coding:utf-8
from LxData.datObjects import _datObjData

from ..import mtlObjAbs, mtlCfg

from ..mtlObjects import _mtlObjRaw


# Method for Digit Calculate
class _Val_Digit(mtlObjAbs.Abs_MtlValue):
    def __add__(self, other):
        """
        :param other: object of Value
        :return: object of Value
        """
        return self.__class__((self.data() + other.data()).raw())

    def __sub__(self, other):
        """
        :param other: object of Value
        :return: object of Value
        """
        return self.__class__((self.data() - other.data()).raw())

    def __mul__(self, other):
        """
        :param other: object of Value
        :return: object of Value
        """
        return self.__class__((self.data() * other.data()).raw())

    def __div__(self, other):
        """
        :param other: object of Value
        :return: object of Value
        """
        return self.__class__((self.data() / other.data()).raw())


# Value Def
class Val_Closure(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_Closure

    VAR_dat_rawtype_pattern = None
    VAR_dat_rawtype_str_pattern = mtlCfg.Utility.DEF_mtl_porttype_closure
    VAR_dat_rawsize_pattern = 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


# Value Boolean ****************************************************************************************************** #
class Val_Boolean(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_Boolean

    VAR_dat_rawtype_pattern = bool
    VAR_dat_rawtype_str_pattern = mtlCfg.Utility.DEF_mtl_porttype_boolean
    VAR_dat_rawsize_pattern = 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Visibility(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_Boolean

    VAR_dat_rawtype_pattern = bool
    VAR_dat_rawtype_str_pattern = mtlCfg.Utility.DEF_mtl_porttype_boolean
    VAR_dat_rawsize_pattern = 1

    VAR_dat_xml_file_attribute_attach_tag = u'visible'
    VAR_dat_xml_file_element_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# Value Integer
class Val_Integer(_Val_Digit):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_Integer

    VAR_dat_rawtype_pattern = int
    VAR_dat_rawtype_str_pattern = mtlCfg.Utility.DEF_mtl_porttype_Integer
    VAR_dat_rawsize_pattern = 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.int;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_IntegerArray(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_IntegerN

    VAR_dat_rawtype_pattern = list, int
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_integerarray,
        mtlCfg.Utility.DEF_mtl_porttype_Integer
    )
    VAR_dat_rawsize_pattern = float('inf'), 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(int, ...);
            1-2.int, ...
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


# Value Float
class Val_Float(_Val_Digit):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_Float

    VAR_dat_rawtype_pattern = float
    VAR_dat_rawtype_str_pattern = mtlCfg.Utility.DEF_mtl_porttype_float
    VAR_dat_rawsize_pattern = 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.float;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_FloatArray(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatN

    VAR_dat_rawtype_pattern = list, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_floatarray,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = float('inf'), 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(float, ...);
            1-2.float, ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


# Value Color
class Val_Color2(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatN

    VAR_dat_rawtype_pattern = tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_color2,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = 2, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * color2(red, alpha)
        :param args:
            1-1.list(float, float);
            1-2.float, float;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Color2Array(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatNN

    VAR_dat_rawtype_pattern = list, tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_color2array,
        mtlCfg.Utility.DEF_mtl_porttype_color2,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = float('inf'), 2, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * list of color2
        :param args:
            1-1.list(list(float, float), ...);
            1-2.list(float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Color3(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatN

    VAR_dat_rawtype_pattern = tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_color3,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = 3, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * color3(red, green, blue)
        :param args:
            1-1.list(float, float, float);
            1-2.float, float, float;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Color3Array(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatNN

    VAR_dat_rawtype_pattern = list, tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_color3array,
        mtlCfg.Utility.DEF_mtl_porttype_color3,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = float('inf'), 3, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * list of color3
        :param args:
            1-1.list(list(float, float, float), ...);
            1-2.list(float, float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Color4(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatN

    VAR_dat_rawtype_pattern = tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_color4,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = 4, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * color4(red, green, blue, alpha)
        :param args:
            1-1.list(float, float, float, float);
            1-2.float, float, float, float;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Color4Array(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatNN

    VAR_dat_rawtype_pattern = list, tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_color4array,
        mtlCfg.Utility.DEF_mtl_porttype_color4,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = float('inf'), 4, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * list of color4
        :param args:
            1-1.list(list(float, float, float, float), ...);
            1-2.list(float, float, float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


# Value Vector
class Val_Vector2(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatN

    VAR_dat_rawtype_pattern = tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_vector2,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = 2, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * vector2(x, y)
        :param args:
            1-1.list(float, float);
            1-2.float, float;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Vector2Array(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatNN

    VAR_dat_rawtype_pattern = list, tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_vector2array,
        mtlCfg.Utility.DEF_mtl_porttype_vector2,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = float('inf'), 2, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float), ...);
            1-2.list(float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Vector3(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatN

    VAR_dat_rawtype_pattern = tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_vector3,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = 3, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * vector3(x, y, z)
        :param args:
            1-1.list(float, float, float);
            1-2.float, float, float;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Vector3Array(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatNN

    VAR_dat_rawtype_pattern = list, tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_vector3array,
        mtlCfg.Utility.DEF_mtl_porttype_vector3,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = float('inf'), 3, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float), ...);
            1-2.list(float, float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Vector4(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatN

    VAR_dat_rawtype_pattern = tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_vector4,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = 4, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        * vector4(x, y, z, w)
        :param args:
            1-1.list(float, float, float, float);
            1-2.float, float, float, float;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Vector4Array(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatNN

    VAR_dat_rawtype_pattern = list, tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_vector4array,
        mtlCfg.Utility.DEF_mtl_porttype_vector4,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = float('inf'), 4, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float, float), ...);
            1-2.list(float, float, float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_String(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_String

    VAR_dat_rawtype_pattern = unicode
    VAR_dat_rawtype_str_pattern = mtlCfg.Utility.DEF_mtl_porttype_string
    VAR_dat_rawsize_pattern = 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbsMtlValue(*args)


class Val_StringArray(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_StringN

    VAR_dat_rawtype_pattern = list, unicode
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_stringarray,
        mtlCfg.Utility.DEF_mtl_porttype_string
    )
    VAR_dat_rawsize_pattern = float('inf'), 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Filename(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_Filename

    VAR_dat_rawtype_pattern = unicode
    VAR_dat_rawtype_str_pattern = mtlCfg.Utility.DEF_mtl_porttype_filename
    VAR_dat_rawsize_pattern = 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbsMtlValue(*args)


class Val_FilenameArray(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_StringN

    VAR_dat_rawtype_pattern = list, unicode
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_stringarray,
        mtlCfg.Utility.DEF_mtl_porttype_string
    )
    VAR_dat_rawsize_pattern = float('inf'), 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Nodename(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_Nodename

    VAR_dat_rawtype_pattern = unicode
    VAR_dat_rawtype_str_pattern = mtlCfg.Utility.DEF_mtl_porttype_nodename
    VAR_dat_rawsize_pattern = 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbsMtlValue(*args)


class Val_NodenameArray(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_StringN

    VAR_dat_rawtype_pattern = list, unicode
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_nodenamearray,
        mtlCfg.Utility.DEF_mtl_porttype_nodename
    )
    VAR_dat_rawsize_pattern = float('inf'), 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Matrix33(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatNN

    VAR_dat_rawtype_pattern = tuple, tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_matrix33,
        mtlCfg.Utility.DEF_mtl_porttype_vector3,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = 3, 3, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float), list(float, float, float), list(float, float, float));
            1-2.list(float, float, float), list(float, float, float), list(float, float, float);
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)


class Val_Matrix44(mtlObjAbs.Abs_MtlValue):
    CLS_dat_datatype = _mtlObjRaw.Datatype
    CLS_dat_data = _datObjData.Dat_FloatNN

    VAR_dat_rawtype_pattern = tuple, tuple, float
    VAR_dat_rawtype_str_pattern = (
        mtlCfg.Utility.DEF_mtl_porttype_matrix44,
        mtlCfg.Utility.DEF_mtl_porttype_vector4,
        mtlCfg.Utility.DEF_mtl_porttype_float
    )
    VAR_dat_rawsize_pattern = 4, 4, 1

    VAR_dat_xml_file_element_tag = u'value'
    VAR_dat_xml_file_attribute_attach_tag = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float, float), list(float, float, float, float), list(float, float, float, float), list(float, float, float, float));
            1-2.list(float, float, float, float), list(float, float, float, float), list(float, float, float, float), list(float, float, float, float);
            2.str(portrawString).
        """
        self._initAbsMtlValue(*args)
