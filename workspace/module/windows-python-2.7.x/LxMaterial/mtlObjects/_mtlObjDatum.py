# coding:utf-8
from LxMaterial import mtlAbstract, mtlConfigure

from LxMaterial.mtlObjects import _mtlObjRaw


class _Dat_Method(mtlAbstract.Abc_RawDatum):
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


class Dat_Closure(mtlAbstract.Abc_RawDatum):
    CLS_raw = _mtlObjRaw.Raw_Closure

    raw_type = _mtlObjRaw.Raw_Closure

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatum(*args)

    def toString(self):
        return ''


class Dat_Boolean(mtlAbstract.Abc_RawDatum):
    CLS_raw = bool

    raw_type = bool, int

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatum(*args)

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

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatum(*args)


class Dat_IntegerN(mtlAbstract.Abc_RawDatumset):
    CLS_set_child = Dat_Integer

    datum_string_separator = mtlConfigure.Separator_Raw_String

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of datum, raw.
        """
        self._initAbcRawDatumset(*args)


class Dat_IntegerNN(mtlAbstract.Abc_RawDatumset):
    CLS_set_child = Dat_IntegerN

    datum_string_separator = mtlConfigure.Separator_Raw_String_Array

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatumset(*args)


class Dat_Float(_Dat_Method):
    CLS_raw = float

    raw_type = float, int

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatum(*args)


class Dat_FloatN(mtlAbstract.Abc_RawDatumset):
    CLS_set_child = Dat_Float

    datum_string_separator = mtlConfigure.Separator_Raw_String

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatumset(*args)


class Dat_FloatNN(mtlAbstract.Abc_RawDatumset):
    CLS_set_child = Dat_FloatN

    datum_string_separator = mtlConfigure.Separator_Raw_String_Array

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatumset(*args)


class Dat_String(mtlAbstract.Abc_RawDatum):
    CLS_raw = unicode

    raw_type = unicode, str

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatum(*args)


class Dat_StringN(mtlAbstract.Abc_RawDatumset):
    CLS_set_child = Dat_String

    datum_string_separator = mtlConfigure.Separator_Raw_String

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatumset(*args)


class Dat_FileName(mtlAbstract.Abc_RawDatum):
    CLS_raw = unicode

    raw_type = unicode, str

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatum(*args)


class Dat_NodeName(mtlAbstract.Abc_RawDatum):
    CLS_raw = unicode

    raw_type = unicode, str

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatum(*args)


class Dat_NodeNameN(mtlAbstract.Abc_RawDatumset):
    CLS_set_child = Dat_NodeName

    datum_string_separator = mtlConfigure.Separator_Raw_String

    STR_mtlx_key_attribute = 'value'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcRawDatumset(*args)
