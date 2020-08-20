# coding:utf-8
from LxData.datObjects import _datObjData

from .. import mtxObjAbs, mtxCfg

from . import _mtxObjRaw


# Method for Digit Calculate
class _Val_Digit(mtxObjAbs.AbsMtxValue):
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
class Val_Closure(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_Closure

    VAR_dat__value__rawtype_str_pattern = mtxCfg.MtxUtility.DEF_mtx__datatype__closure
    VAR_dat__value__rawtype_pattern = None
    VAR_dat__value__rawsize_pattern = 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


# Value Boolean ****************************************************************************************************** #
class Val_Boolean(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_Boolean

    VAR_dat__value__rawtype_str_pattern = mtxCfg.MtxUtility.DEF_mtx__datatype__boolean
    VAR_dat__value__rawtype_pattern = bool
    VAR_dat__value__rawsize_pattern = 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Visibility(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_Boolean

    VAR_dat__value__rawtype_str_pattern = mtxCfg.MtxUtility.DEF_mtx__datatype__boolean
    VAR_dat__value__rawtype_pattern = bool
    VAR_dat__value__rawsize_pattern = 1

    VAR_dat__xml_obj__attribute_attach_str = u'visible'
    VAR_dat__xml_obj__element_prefix_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.bool;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


# Value Integer
class Val_Integer(_Val_Digit):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_Integer

    VAR_dat__value__rawtype_str_pattern = mtxCfg.MtxUtility.DEF_mtx__datatype__Integer
    VAR_dat__value__rawtype_pattern = int
    VAR_dat__value__rawsize_pattern = 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.int;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_IntegerArray(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_IntegerN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__integerarray,
        mtxCfg.MtxUtility.DEF_mtx__datatype__Integer
    )
    VAR_dat__value__rawtype_pattern = list, int
    VAR_dat__value__rawsize_pattern = float(u'inf'), 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(int, ...);
            1-2.int, ...
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


# Value Float
class Val_Float(_Val_Digit):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_Float

    VAR_dat__value__rawtype_str_pattern = mtxCfg.MtxUtility.DEF_mtx__datatype__float
    VAR_dat__value__rawtype_pattern = float
    VAR_dat__value__rawsize_pattern = 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1.float;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_FloatArray(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__floatarray,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(float("0.0"), ...);
            1-2.float(0.0), ...;
            2.str("0.0, ...").
        """
        self._initAbsMtxValue(*args)


# Value Color
class Val_Color2(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__color2,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = tuple, float
    VAR_dat__value__rawsize_pattern = 2, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * color2(red, alpha)
        :param args:
            1-1.list(float, float);
            1-2.float, float;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Color2Array(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__color2array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__color2,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 2, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * list of color2
        :param args:
            1-1.list(list(float, float), ...);
            1-2.list(float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Color3(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__color3,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = tuple, float
    VAR_dat__value__rawsize_pattern = 3, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * color3(red, green, blue)
        :param args:
            1-1.list(float, float, float);
            1-2.float, float, float;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Color3Array(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__color3array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__color3,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 3, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * list of color3
        :param args:
            1-1.list(list(float, float, float), ...);
            1-2.list(float, float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Color4(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__color4,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = tuple, float
    VAR_dat__value__rawsize_pattern = 4, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * color4(red, green, blue, alpha)
        :param args:
            1-1.list(float, float, float, float);
            1-2.float, float, float, float;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Color4Array(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__color4array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__color4,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 4, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * list of color4
        :param args:
            1-1.list(list(float, float, float, float), ...);
            1-2.list(float, float, float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


# Value Vector
class Val_Vector2(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector2,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = tuple, float
    VAR_dat__value__rawsize_pattern = 2, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * vector2(x, y)
        :param args:
            1-1.list(float, float);
            1-2.float, float;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Vector2Array(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector2array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector2,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 2, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float), ...);
            1-2.list(float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Vector3(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector3,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = tuple, float
    VAR_dat__value__rawsize_pattern = 3, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * vector3(x, y, z)
        :param args:
            1-1.list(float, float, float);
            1-2.float, float, float;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Vector3Array(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector3array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector3,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 3, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float), ...);
            1-2.list(float, float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Vector4(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector4,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = tuple, float
    VAR_dat__value__rawsize_pattern = 4, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        * vector4(x, y, z, w)
        :param args:
            1-1.list(float, float, float, float);
            1-2.float, float, float, float;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Vector4Array(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector4array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector4,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 4, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float, float), ...);
            1-2.list(float, float, float, float), ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_String(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_String

    VAR_dat__value__rawtype_str_pattern = mtxCfg.MtxUtility.DEF_mtx__datatype__string
    VAR_dat__value__rawtype_pattern = unicode
    VAR_dat__value__rawsize_pattern = 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbsMtxValue(*args)


class Val_StringArray(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_StringN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__stringarray,
        mtxCfg.MtxUtility.DEF_mtx__datatype__string
    )
    VAR_dat__value__rawtype_pattern = list, unicode
    VAR_dat__value__rawsize_pattern = float(u'inf'), 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Filepath(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_Filepath

    VAR_dat__value__rawtype_str_pattern = mtxCfg.MtxUtility.DEF_mtx__datatype__filename
    VAR_dat__value__rawtype_pattern = unicode
    VAR_dat__value__rawsize_pattern = 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbsMtxValue(*args)


class Val_FilepathArray(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_StringN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__stringarray,
        mtxCfg.MtxUtility.DEF_mtx__datatype__string
    )
    VAR_dat__value__rawtype_pattern = list, unicode
    VAR_dat__value__rawsize_pattern = float(u'inf'), 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Nodename(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_Nodename

    VAR_dat__value__rawtype_str_pattern = mtxCfg.MtxUtility.DEF_mtx__datatype__geomname
    VAR_dat__value__rawtype_pattern = unicode
    VAR_dat__value__rawsize_pattern = 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args: str
        """
        self._initAbsMtxValue(*args)


class Val_NodenameArray(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_StringN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__geomnamearray,
        mtxCfg.MtxUtility.DEF_mtx__datatype__geomname
    )
    VAR_dat__value__rawtype_pattern = list, unicode
    VAR_dat__value__rawsize_pattern = float(u'inf'), 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(unicode, ...);
            1-2.unicode, ...;
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Matrix33(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__matrix33,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector3,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = tuple, tuple, float
    VAR_dat__value__rawsize_pattern = 3, 3, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float), list(float, float, float), list(float, float, float));
            1-2.list(float, float, float), list(float, float, float), list(float, float, float);
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)


class Val_Matrix44(mtxObjAbs.AbsMtxValue):
    CLS_dat__value__datatype = _mtxObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        mtxCfg.MtxUtility.DEF_mtx__datatype__matrix44,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector4,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float
    )
    VAR_dat__value__rawtype_pattern = tuple, tuple, float
    VAR_dat__value__rawsize_pattern = 4, 4, 1

    VAR_dat__xml_obj__element_prefix_str = u'value'
    VAR_dat__xml_obj__attribute_attach_str = u'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.list(list(float, float, float, float), list(float, float, float, float), list(float, float, float, float), list(float, float, float, float));
            1-2.list(float, float, float, float), list(float, float, float, float), list(float, float, float, float), list(float, float, float, float);
            2.str(portrawString).
        """
        self._initAbsMtxValue(*args)
