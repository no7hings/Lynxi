# coding:utf-8
from LxMaterial import mtlObjCore, mtlConfigure

from LxMaterial.mtlObjects import _mtlObjRaw


class _Dat_Method(mtlObjCore.Abc_MtlRawDatum):
    def __add__(self, other):
        """
        :param other: object of "Datum"
        :return: number
        """
        assert isinstance(other.raw(), self.raw_type), u'Argument Error, "arg" Must "raw_type".'

        return self.__class__(self, self.raw() + other.raw())

    def __sub__(self, other):
        """
        :param other: object of "Datum"
        :return: number
        """
        assert isinstance(other.raw(), self.raw_type), u'Argument Error, "arg" Must "raw_type".'

        return self.__class__(self, self.raw() - other.raw())

    def __mul__(self, other):
        """
        :param other: object of "Datum"
        :return: number
        """
        assert isinstance(other.raw(), self.raw_type), u'Argument Error, "arg" Must "raw_type".'

        return self.__class__(self, self.raw() * other.raw())

    def __div__(self, other):
        """
        :param other: object of "Datum"
        :return: number
        """
        assert isinstance(other.raw(), self.raw_type), u'Argument Error, "arg" Must "raw_type".'

        return self.__class__(self, self.raw() / other.raw())


class Dat_Closure(mtlObjCore.Abc_MtlRawDatum):
    CLS_raw = _mtlObjRaw.Raw_Closure

    raw_type = _mtlObjRaw.Raw_Closure

    VAR_mtlx_key_attribute = 'value'

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
    CLS_raw = bool

    raw_type = bool, int

    VAR_mtlx_key_attribute = 'value'

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
    CLS_raw = int

    raw_type = int, float

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_IntegerN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_set_child = Dat_Integer

    datum_string_separator = mtlConfigure.Separator_Raw_String

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_IntegerNN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_set_child = Dat_IntegerN

    datum_string_separator = mtlConfigure.Separator_Raw_String_Array

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_Float(_Dat_Method):
    CLS_raw = float

    raw_type = float, int

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_FloatN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_set_child = Dat_Float

    datum_string_separator = mtlConfigure.Separator_Raw_String

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_FloatNN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_set_child = Dat_FloatN

    datum_string_separator = mtlConfigure.Separator_Raw_String_Array

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_String(mtlObjCore.Abc_MtlRawDatum):
    CLS_raw = unicode

    raw_type = unicode, str

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_StringN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_set_child = Dat_String

    datum_string_separator = mtlConfigure.Separator_Raw_String

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)


class Dat_FileName(mtlObjCore.Abc_MtlRawDatum):
    CLS_raw = unicode

    raw_type = unicode, str

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_NodeName(mtlObjCore.Abc_MtlRawDatum):
    CLS_raw = unicode

    raw_type = unicode, str

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatum(*args)


class Dat_NodeNameN(mtlObjCore.Abc_MtlRawDatumset):
    CLS_set_child = Dat_NodeName

    datum_string_separator = mtlConfigure.Separator_Raw_String

    VAR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcMtlRawDatumset(*args)
