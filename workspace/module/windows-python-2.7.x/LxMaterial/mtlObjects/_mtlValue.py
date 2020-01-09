# coding:utf-8
"""
[
# model of Value
]
"""
from LxMaterial import mtlAbstract, mtlConfigure

from LxMaterial.mtlObjects import _mtlRaw
from LxMaterial.mtlObjects import _mtlDatum


# Method for Digit Calculate
class _Val_DigitMethod(mtlAbstract.Abc_Value):
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
class Val_Closure(mtlAbstract.Abc_Value):
    """
    boolean Value
    """
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_Closure

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
class Val_Boolean(mtlAbstract.Abc_Value):
    """
    boolean Value
    """
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_Boolean

    value_type_string_pattern = mtlConfigure.Value_Type_Boolean,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(valueString).
        """
        self._initAbcValue(*args)


# Value Integer
class Val_Integer(_Val_DigitMethod):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_Integer

    value_type_string_pattern = mtlConfigure.Value_Type_Integer,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args:
            1.int;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_IntegerArray(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_IntegerN

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
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_Float

    value_type_string_pattern = mtlConfigure.Value_Type_Float,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args:
            1.float;
            2.str(valueString).
        """
        self._initAbcValue(*args)


class Val_FloatArray(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatN

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
class Val_Color2(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatN

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


class Val_Color2Array(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatNN

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


class Val_Color3(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatN

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


class Val_Color3Array(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatNN

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


class Val_Color4(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatN

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


class Val_Color4Array(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatNN

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
class Val_Vector2(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatN

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


class Val_Vector2Array(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatNN

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


class Val_Vector3(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatN

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


class Val_Vector3Array(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatNN

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


class Val_Vector4(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatN

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


class Val_Vector4Array(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatNN

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


class Val_String(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_String

    value_type_string_pattern = mtlConfigure.Value_Type_String,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcValue(*args)


class Val_StringArray(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_StringN

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


class Val_FileName(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FileName

    value_type_string_pattern = mtlConfigure.Value_Type_FileName,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcValue(*args)


class Val_GeometryName(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_NodeName

    value_type_string_pattern = mtlConfigure.Value_Type_GeometryName,

    value_size_pattern = 1

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcValue(*args)


class Val_GeometryNameArray(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_StringN

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


class Val_Matrix33(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatNN

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


class Val_Matrix44(mtlAbstract.Abc_Value):
    RAW_TYPE_CLS = _mtlRaw.Raw_ValueType
    RAW_DATUM_CLS = _mtlDatum.Dat_FloatNN

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
