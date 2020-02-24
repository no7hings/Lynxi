# coding:utf-8
from LxMaterial import mtlObjCore, mtlConfigure

from LxMaterial.mtlObjects import _mtlObjRaw


class _Dat_Method(mtlObjCore.Abc_MtlRawDatum):
    def __add__(self, other):
        """
        :param other: object of "Datum"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_mtl_raw_type), u'Argument Error, "arg" Must "VAR_mtl_raw_type".'

        return self.__class__(self, self.raw() + other.raw())

    def __sub__(self, other):
        """
        :param other: object of "Datum"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_mtl_raw_type), u'Argument Error, "arg" Must "VAR_mtl_raw_type".'

        return self.__class__(self, self.raw() - other.raw())

    def __mul__(self, other):
        """
        :param other: object of "Datum"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_mtl_raw_type), u'Argument Error, "arg" Must "VAR_mtl_raw_type".'

        return self.__class__(self, self.raw() * other.raw())

    def __div__(self, other):
        """
        :param other: object of "Datum"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_mtl_raw_type), u'Argument Error, "arg" Must "VAR_mtl_raw_type".'

        return self.__class__(self, self.raw() / other.raw())


class Dat_Closure(mtlObjCore.Abc_MtlRawDatum):
    CLS_mtl_raw = _mtlObjRaw.Raw_Closure

    VAR_mtl_raw_type = _mtlObjRaw.Raw_Closure

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)

    def toString(self):
        return ''


class Dat_Boolean(mtlObjCore.Abc_MtlRawDatum):
    CLS_mtl_raw = bool

    VAR_mtl_raw_type = bool, int

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)

    def toString(self):
        """
        "true" / false"
        :return: str
        """
        if self.hasRaw():
            return ['false', 'true'][self.raw()]


class Dat_Integer(_Dat_Method):
    CLS_mtl_raw = int

    VAR_mtl_raw_type = int, float

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_IntegerN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_mtl_child_set = Dat_Integer

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_IntegerNN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_mtl_child_set = Dat_IntegerN

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_array_separator

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_Float(_Dat_Method):
    CLS_mtl_raw = float

    VAR_mtl_raw_type = float, int

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_FloatN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_mtl_child_set = Dat_Float

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_FloatNN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_mtl_child_set = Dat_FloatN

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_array_separator

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_string(mtlObjCore.Abc_MtlRawDatum):
    CLS_mtl_raw = unicode

    VAR_mtl_raw_type = unicode, str

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_stringN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_mtl_child_set = Dat_string

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_file_name(mtlObjCore.Abc_MtlRawDatum):
    CLS_mtl_raw = unicode

    VAR_mtl_raw_type = unicode, str

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_NodeName(mtlObjCore.Abc_MtlRawDatum):
    CLS_mtl_raw = unicode

    VAR_mtl_raw_type = unicode, str

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_NodeNameN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_mtl_child_set = Dat_NodeName

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)
