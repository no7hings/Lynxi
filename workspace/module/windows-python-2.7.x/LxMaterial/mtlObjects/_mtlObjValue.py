# coding:utf-8
"""
[
# model of Value
]
"""
from LxMaterial import mtlObjAbstract, mtlConfigure

from LxMaterial.mtlObjects import _mtlObjRaw
from LxMaterial.mtlObjects import _mtlObjDatum


# Method for Digit Calculate
class _Val_DigitMethod(mtlObjAbstract.Abc_Value):
    def __add__(self, other):
        """
        :param other: object of Value
        :return: object of Value
        """
        return self.__class__((self.datum() + other.datum()).raw())

    def __sub__(self, other):
        """
        :param other: object of Value
        :return: object of Value
        """
        return self.__class__((self.datum() - other.datum()).raw())

    def __mul__(self, other):
        """
        :param other: object of Value
        :return: object of Value
        """
        return self.__class__((self.datum() * other.datum()).raw())

    def __div__(self, other):
        """
        :param other: object of Value
        :return: object of Value
        """
        return self.__class__((self.datum() / other.datum()).raw())


# Value Def
class Val_Closure(mtlObjAbstract.Abc_Value):
    """
    boolean Value
    """
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_Closure

    value_type_string_pattern = mtlConfigure.Value_Type_Closure,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(valueString).
        """
        self._initAbcValue(*args)


# Value Boolean
class Val_Boolean(mtlObjAbstract.Abc_Value):
    """
    boolean Value
    """
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_Boolean

    value_type_string_pattern = mtlConfigure.Value_Type_Boolean,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Visibility(mtlObjAbstract.Abc_Value):
    """
    boolean Value
    """
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_Boolean

    value_type_string_pattern = mtlConfigure.Value_Type_Boolean,

    value_size_pattern = 1

    STR_mtlx_key_attribute = 'visible'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(valueString).
        """
        self._initAbcValue(*args)

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# Value Integer
class Val_Integer(_Val_DigitMethod):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_Integer

    value_type_string_pattern = mtlConfigure.Value_Type_Integer,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args:
            1.int;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_IntegerArray(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_IntegerN

    value_type_string_pattern = mtlConfigure.Value_Type_Integer_Array, None

    value_size_pattern = float('inf'), 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(int, ...);
            1-2.int, ...
            2.str(valueString).
        """
        self._initAbcValue(*args)


# Value Float
class Val_Float(_Val_DigitMethod):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_Float

    value_type_string_pattern = mtlConfigure.Value_Type_Float,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args:
            1.float;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_FloatArray(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatN

    value_type_string_pattern = mtlConfigure.Value_Type_Float_Array, None

    value_size_pattern = float('inf'), 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(float, ...);
            1-2.float, ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


# Value Color
class Val_Color2(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatN

    value_type_string_pattern = mtlConfigure.Value_Type_Color2, None

    value_size_pattern = 2, 1

    def __init__(self, *args):
        """
        * color2(red, alpha)
        :param args:
            1-1.list(float, float);
            1-2.float, float;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Color2Array(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatNN

    value_type_string_pattern = mtlConfigure.Value_Type_Color2_Array, None, None

    value_size_pattern = float('inf'), 2, 1

    def __init__(self, *args):
        """
        * list of color2
        :param args:
            1-1.list(list(float, float), ...);
            1-2.list(float, float), ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Color3(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatN

    value_type_string_pattern = mtlConfigure.Value_Type_Color3, None

    value_size_pattern = 3, 1

    def __init__(self, *args):
        """
        * color3(red, green, blue)
        :param args:
            1-1.list(float, float, float);
            1-2.float, float, float;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Color3Array(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatNN

    value_type_string_pattern = mtlConfigure.Value_Type_Color3_Array, None, None

    value_size_pattern = float('inf'), 3, 1

    def __init__(self, *args):
        """
        * list of color3
        :param args:
            1-1.list(list(float, float, float), ...);
            1-2.list(float, float, float), ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Color4(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatN

    value_type_string_pattern = mtlConfigure.Value_Type_Color4, None

    value_size_pattern = 4, 1

    def __init__(self, *args):
        """
        * color4(red, green, blue, alpha)
        :param args:
            1-1.list(float, float, float, float);
            1-2.float, float, float, float;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Color4Array(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatNN

    value_type_string_pattern = mtlConfigure.Value_Type_Color4_Array, None, None

    value_size_pattern = float('inf'), 4, 1

    def __init__(self, *args):
        """
        * list of color4
        :param args:
            1-1.list(list(float, float, float, float), ...);
            1-2.list(float, float, float, float), ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


# Value Vector
class Val_Vector2(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatN

    value_type_string_pattern = mtlConfigure.Value_Type_Vector2, None

    value_size_pattern = 2, 1

    def __init__(self, *args):
        """
        * vector2(x, y)
        :param args:
            1-1.list(float, float);
            1-2.float, float;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Vector2Array(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatNN

    value_type_string_pattern = mtlConfigure.Value_Type_Vector2_Array, None, None

    value_size_pattern = float('inf'), 2, 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float), ...);
            1-2.list(float, float), ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Vector3(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatN

    value_type_string_pattern = mtlConfigure.Value_Type_Vector3, None

    value_size_pattern = 3, 1

    def __init__(self, *args):
        """
        * vector3(x, y, z)
        :param args:
            1-1.list(float, float, float);
            1-2.float, float, float;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Vector3Array(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatNN

    value_type_string_pattern = mtlConfigure.Value_Type_Vector3_Array, None, None

    value_size_pattern = float('inf'), 3, 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float), ...);
            1-2.list(float, float, float), ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Vector4(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatN

    value_type_string_pattern = mtlConfigure.Value_Type_Vector4, None

    value_size_pattern = 4, 1

    def __init__(self, *args):
        """
        * vector4(x, y, z, w)
        :param args:
            1-1.list(float, float, float, float);
            1-2.float, float, float, float;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Vector4Array(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatNN

    value_type_string_pattern = mtlConfigure.Value_Type_Vector4_Array, None, None

    value_size_pattern = float('inf'), 4, 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float, float), ...);
            1-2.list(float, float, float, float), ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_String(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_String

    value_type_string_pattern = mtlConfigure.Value_Type_String,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcValue(*args)


class Val_StringArray(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_StringN

    value_type_string_pattern = mtlConfigure.Value_Type_String_Array, mtlConfigure.Value_Type_String

    value_size_pattern = float('inf'), 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_FileName(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FileName

    value_type_string_pattern = mtlConfigure.Value_Type_FileName,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcValue(*args)


class Val_GeometryName(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_NodeName

    value_type_string_pattern = mtlConfigure.Value_Type_GeometryName,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcValue(*args)


class Val_GeometryNameArray(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_StringN

    value_type_string_pattern = mtlConfigure.Value_Type_GeometryName_Array, mtlConfigure.Value_Type_GeometryName

    value_size_pattern = float('inf'), 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Matrix33(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatNN

    value_type_string_pattern = mtlConfigure.Value_Type_Matrix33, None, None

    value_size_pattern = 3, 3, 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float), list(float, float, float), list(float, float, float));
            1-2.list(float, float, float), list(float, float, float), list(float, float, float);
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_Matrix44(mtlObjAbstract.Abc_Value):
    CLS_raw_type = _mtlObjRaw.Raw_ValueType
    CLS_raw_datum = _mtlObjDatum.Dat_FloatNN

    value_type_string_pattern = mtlConfigure.Value_Type_Matrix33, None, None

    value_size_pattern = 4, 4, 1

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float, float), list(float, float, float, float), list(float, float, float, float), list(float, float, float, float));
            1-2.list(float, float, float, float), list(float, float, float, float), list(float, float, float, float), list(float, float, float, float);
            2.str(valueString).
        """
        self._initAbcValue(*args)
