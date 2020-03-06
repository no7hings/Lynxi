# coding:utf-8
"""
[
# model of Value
]
"""
from LxMaterial import mtlObjCore, mtlConfigure

from LxMaterial.mtlObjects import _mtlObjRaw
from LxMaterial.mtlObjects import _mtlObjData


# Method for Digit Calculate
class _Val_DigitMethod(mtlObjCore.Abc_MtlValue):
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
class Val_Closure(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_Closure

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_closure,

    VAR_mtl_value_size_pattern = 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


# Value Boolean
class Val_Boolean(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_Boolean

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_boolean,

    VAR_mtl_value_size_pattern = 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_Visibility(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_Boolean

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_boolean,

    VAR_mtl_value_size_pattern = 1

    VAR_mtl_file_attribute_key = u'visible'
    VAR_mtl_file_element_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# Value Integer
class Val_Integer(_Val_DigitMethod):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_Integer

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_Integer,

    VAR_mtl_value_size_pattern = 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.int;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_IntegerArray(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_IntegerN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_integer_array, None

    VAR_mtl_value_size_pattern = float('inf'), 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(int, ...);
            1-2.int, ...
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


# Value Float
class Val_Float(_Val_DigitMethod):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_Float

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_float,

    VAR_mtl_value_size_pattern = 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.float;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_FloatArray(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_float_array, None

    VAR_mtl_value_size_pattern = float('inf'), 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(float, ...);
            1-2.float, ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


# Value Color
class Val_Color2(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_color2, None

    VAR_mtl_value_size_pattern = 2, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * color2(red, alpha)
        :param args:
            1-1.list(float, float);
            1-2.float, float;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_Color2Array(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatNN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_color2_array, None, None

    VAR_mtl_value_size_pattern = float('inf'), 2, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * list of color2
        :param args:
            1-1.list(list(float, float), ...);
            1-2.list(float, float), ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_Color3(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_color3, None

    VAR_mtl_value_size_pattern = 3, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * color3(red, green, blue)
        :param args:
            1-1.list(float, float, float);
            1-2.float, float, float;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_Color3Array(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatNN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_color3_array, None, None

    VAR_mtl_value_size_pattern = float('inf'), 3, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * list of color3
        :param args:
            1-1.list(list(float, float, float), ...);
            1-2.list(float, float, float), ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_Color4(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_color4, None

    VAR_mtl_value_size_pattern = 4, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * color4(red, green, blue, alpha)
        :param args:
            1-1.list(float, float, float, float);
            1-2.float, float, float, float;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_Color4Array(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatNN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_color4_array, None, None

    VAR_mtl_value_size_pattern = float('inf'), 4, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * list of color4
        :param args:
            1-1.list(list(float, float, float, float), ...);
            1-2.list(float, float, float, float), ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


# Value Vector
class Val_vector2(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_vector2, None

    VAR_mtl_value_size_pattern = 2, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * vector2(x, y)
        :param args:
            1-1.list(float, float);
            1-2.float, float;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_vector2Array(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatNN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_vector2_array, None, None

    VAR_mtl_value_size_pattern = float('inf'), 2, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float), ...);
            1-2.list(float, float), ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_vector3(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_vector3, None

    VAR_mtl_value_size_pattern = 3, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * vector3(x, y, z)
        :param args:
            1-1.list(float, float, float);
            1-2.float, float, float;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_vector3Array(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatNN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_vector3_array, None, None

    VAR_mtl_value_size_pattern = float('inf'), 3, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float), ...);
            1-2.list(float, float, float), ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_vector4(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_vector4, None

    VAR_mtl_value_size_pattern = 4, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        * vector4(x, y, z, w)
        :param args:
            1-1.list(float, float, float, float);
            1-2.float, float, float, float;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_vector4Array(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatNN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_vector4_array, None, None

    VAR_mtl_value_size_pattern = float('inf'), 4, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float, float), ...);
            1-2.list(float, float, float, float), ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_string(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_string

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_string,

    VAR_mtl_value_size_pattern = 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcMtlValue(*args)


class Val_stringArray(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_stringN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_string_array, mtlConfigure.Utility.DEF_mtl_datatype_string

    VAR_mtl_value_size_pattern = float('inf'), 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_file_name(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_file_name

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_file_name,

    VAR_mtl_value_size_pattern = 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcMtlValue(*args)


class Val_geometry_name(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_NodeName

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_geometry_name,

    VAR_mtl_value_size_pattern = 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcMtlValue(*args)


class Val_geometry_nameArray(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_stringN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_geometry_name_array, mtlConfigure.Utility.DEF_mtl_datatype_geometry_name

    VAR_mtl_value_size_pattern = float('inf'), 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_matrix33(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatNN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_matrix33, None, None

    VAR_mtl_value_size_pattern = 3, 3, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float), list(float, float, float), list(float, float, float));
            1-2.list(float, float, float), list(float, float, float), list(float, float, float);
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)


class Val_matrix44(mtlObjCore.Abc_MtlValue):
    CLS_mtl_datatype = _mtlObjRaw.DatatypeString
    CLS_mtl_raw_data = _mtlObjData.Dat_FloatNN

    VAR_mtl_value_type_pattern = mtlConfigure.Utility.DEF_mtl_datatype_matrix33, None, None

    VAR_mtl_value_size_pattern = 4, 4, 1

    VAR_mtl_file_element_key = u'value'
    VAR_mtl_file_attribute_key = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float, float), list(float, float, float, float), list(float, float, float, float), list(float, float, float, float));
            1-2.list(float, float, float, float), list(float, float, float, float), list(float, float, float, float), list(float, float, float, float);
            2.str(valueString).
        """
        self._initAbcMtlValue(*args)
