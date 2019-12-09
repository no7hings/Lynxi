# coding:utf-8
"""
[
# model of Value
]
"""
from LxGraph import grhAbstract, grhConfigure

from LxGraph.grhModel import grhRaw, grhData


class _ValDigitBasic(grhAbstract.AbcValue):
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


class ValBoolean(grhAbstract.AbcValue):
    """
    boolean Value
    """
    RawTypeString = grhConfigure.Value_Type_String_Boolean

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatBoolean

    def __init__(self, *args):
        """
        :param args: bool
        """
        self._initAbcValue()

        self.create(*args)


class ValInteger(_ValDigitBasic):
    RawTypeString = grhConfigure.Value_Type_String_Integer

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatInteger

    def __init__(self, *args):
        """
        :param args: int
        """
        self._initAbcValue()

        self.create(*args)


class ValFloat(_ValDigitBasic):
    RawTypeString = grhConfigure.Value_Type_String_Float

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloat

    def __init__(self, *args):
        """
        :param args: float
        """
        self._initAbcValue()

        self.create(*args)


class ValColor2(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Color2

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatN

    def __init__(self, *args):
        """
        * color2(red, alpha)
        :param args: list(float, float) / float, float
        """
        self._initAbcValue()

        self._setDataNSize(2)

        self.create(*args)


class ValColor3(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Color3

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatN

    def __init__(self, *args):
        """
        * color3(red, green, blue)
        :param args: list(float, float, float) / float, float, float
        """
        self._initAbcValue()

        self._setDataNSize(3)

        self.create(*args)


class ValColor4(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Color4

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatN

    def __init__(self, *args):
        """
        * color4(red, green, blue, alpha)
        :param args: list(float, float, float, float) / float, float, float, float
        """
        self._initAbcValue()

        self._setDataNSize(4)

        self.create(*args)


class ValVector2(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Vector2

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatN

    def __init__(self, *args):
        """
        * vector2(x, y)
        :param args: list(float, float) / float, float
        """
        self._initAbcValue()

        self._setDataNSize(2)

        self.create(*args)


class ValVector3(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Vector3

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatN

    def __init__(self, *args):
        """
        * vector3(x, y, z)
        :param args: list(float, float, float) / float, float, float
        """
        self._initAbcValue()

        self._setDataNSize(3)

        self.create(*args)


class ValVector4(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Vector4

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatN

    def __init__(self, *args):
        """
        * vector4(x, y, z, w)
        :param args: list(float, float, float, float) / float, float, float, float
        """
        self._initAbcValue()

        self._setDataNSize(4)

        self.create(*args)


class ValString(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_String

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatString

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcValue()

        self.create(*args)


class ValFileName(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_FileName

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFileName

    def __init__(self, *args):
        self._initAbcValue()

        self.create(*args)


class ValGeometryName(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_GeometryName

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatNodeName

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbcValue()

        self.create(*args)


class ValIntegerArray(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Integer_Array
    SubRawTypeString = grhConfigure.Value_Type_String_Integer

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatIntegerN

    def __init__(self, *args):
        """
        :param args: list(int, ...) / int, ...
        """
        self._initAbcValue()

        self.create(*args)


class ValFloatArray(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Float_Array
    SubRawTypeString = grhConfigure.Value_Type_String_Float

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatN

    def __init__(self, *args):
        """
        :param args: list(float, ...) / float, ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'))

        self.create(*args)


class ValColor2Array(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Color2_Array
    SubRawTypeString = grhConfigure.Value_Type_String_Color2

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatNN

    def __init__(self, *args):
        """
        :param args: list(list(float, float) ...) / list(float, float) ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'), 2)

        self.create(*args)


class ValColor3Array(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Color3_Array
    SubRawTypeString = grhConfigure.Value_Type_String_Color3

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatNN

    def __init__(self, *args):
        """
        :param args: list(list(float, float, float) ...) / list(float, float, float) ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'), 3)

        self.create(*args)


class ValColor4Array(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Color4_Array
    SubRawTypeString = grhConfigure.Value_Type_String_Color4

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatNN

    def __init__(self, *args):
        """
        :param args: list(list(float, float, float, float) ...) / list(float, float, float, float) ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'), 4)

        self.create(*args)


class ValVector2Array(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Vector2_Array
    SubRawTypeString = grhConfigure.Value_Type_String_Vector2

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatNN

    def __init__(self, *args):
        """
        :param args: list(list(float, float) ...) / list(float, float) ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'), 2)

        self.create(*args)


class ValVector3Array(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Vector3_Array
    SubRawTypeString = grhConfigure.Value_Type_String_Vector3

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatNN

    def __init__(self, *args):
        """
        :param args: list(list(float, float, float) ...) / list(float, float, float) ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'), 3)

        self.create(*args)


class ValVector4Array(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Vector4_Array
    SubRawTypeString = grhConfigure.Value_Type_String_Vector4

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatNN

    def __init__(self, *args):
        """
        :param args: list(list(float, float, float, float) ...) / list(float, float, float, float) ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'), 4)

        self.create(*args)


class ValStringArray(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_String_Array
    SubRawTypeString = grhConfigure.Value_Type_String_String

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatStringN

    def __init__(self, *args):
        """
        :param args: list(unicode, ...) / unicode, ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'))

        self.create(*args)


class ValGeometryNameArray(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_GeometryName_Array
    SubRawTypeString = grhConfigure.Value_Type_String_GeometryName

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatStringN

    def __init__(self, *args):
        """
        :param args:  list(unicode, ...) / unicode, ...
        """
        self._initAbcValue()

        self._setDataNSize(float('inf'))

        self.create(*args)


class ValMatrix33(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Matrix33

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatNN

    def __init__(self, *args):
        """
        :param args: list(list(float, float, float), list(float, float, float), list(float, float, float)) or list(float, float, float), list(float, float, float), list(float, float, float)
        """
        self._initAbcValue()

        self._setDataNSize(3, 3)

        self.create(*args)


class ValMatrix44(grhAbstract.AbcValue):
    RawTypeString = grhConfigure.Value_Type_String_Matrix33

    TYPE_CLS = grhRaw.ValueType
    DATA_CLS = grhData.DatFloatNN

    def __init__(self, *args):
        self._initAbcValue()

        self._setDataNSize(4, 4)

        self.create(*args)
