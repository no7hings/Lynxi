# coding:utf-8
from LxData.datObjects import _datObjData

from .. import datCfg, datObjAbs

from . import _datObjRaw


# Method for Digit Calculate
class _Val_Digit(datObjAbs.AbsDatValue):
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


# Value Float
class Val_Float(_Val_Digit):
    CLS_dat__value__datatype = _datObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_Float

    VAR_dat__value__rawtype_str_pattern = datCfg.DatUtility.DEF_dat__datatype__float
    VAR_dat__value__rawtype_pattern = float
    VAR_dat__value__rawsize_pattern = 1

    def __init__(self, *args):
        self._initAbsDatValue(*args)


class Val_FloatArray(datObjAbs.AbsDatValue):
    CLS_dat__value__datatype = _datObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatN

    VAR_dat__value__rawtype_str_pattern = (
        datCfg.DatUtility.DEF_dat__datatype__floatarray,
        datCfg.DatUtility.DEF_dat__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 1

    def __init__(self, *args):
        self._initAbsDatValue(*args)


class Val_Float2Array(datObjAbs.AbsDatValue):
    CLS_dat__value__datatype = _datObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_str_pattern = (
        datCfg.DatUtility.DEF_dat__datatype__float2array,
        datCfg.DatUtility.DEF_dat__datatype__float2,
        datCfg.DatUtility.DEF_dat__datatype__float
    )
    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawsize_pattern = float(u'inf'), 2, 1

    def __init__(self, *args):
        self._initAbsDatValue(*args)


class Val_Float3Array(datObjAbs.AbsDatValue):
    CLS_dat__value__datatype = _datObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawtype_str_pattern = (
        datCfg.DatUtility.DEF_dat__datatype__float3array,
        datCfg.DatUtility.DEF_dat__datatype__float3,
        datCfg.DatUtility.DEF_dat__datatype__float
    )
    VAR_dat__value__rawsize_pattern = float(u'inf'), 3, 1

    def __init__(self, *args):
        self._initAbsDatValue(*args)


class Val_Float4Array(datObjAbs.AbsDatValue):
    CLS_dat__value__datatype = _datObjRaw.Datatype
    CLS_dat__value__data = _datObjData.Dat_FloatNN

    VAR_dat__value__rawtype_pattern = list, tuple, float
    VAR_dat__value__rawtype_str_pattern = (
        datCfg.DatUtility.DEF_dat__datatype__float4array,
        datCfg.DatUtility.DEF_dat__datatype__float4,
        datCfg.DatUtility.DEF_dat__datatype__float
    )
    VAR_dat__value__rawsize_pattern = float(u'inf'), 4, 1

    def __init__(self, *args):
        self._initAbsDatValue(*args)
