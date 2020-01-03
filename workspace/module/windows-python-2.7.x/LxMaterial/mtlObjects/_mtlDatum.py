# coding:utf-8
from LxMaterial import mtlAbstract, mtlCore

from LxMaterial.mtlObjects import _mtlRaw


class _Dat_Method(mtlAbstract.Abc_Datum):
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


class Dat_Closure(mtlAbstract.Abc_Datum):
    RAW_CLS = _mtlRaw.Raw_Closure

    raw_type = _mtlRaw.Raw_Closure

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatum(*args)

    def toString(self):
        return ''


class Dat_Boolean(mtlAbstract.Abc_Datum):
    RAW_CLS = bool

    raw_type = bool, int

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatum(*args)

    def toString(self):
        """
        "true" / false"
        :return: str
        """
        if self.hasRaw():
            return ['false', 'true'][self.raw()]


class Dat_Integer(_Dat_Method):
    RAW_CLS = int

    raw_type = int, float

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatum(*args)


class Dat_IntegerN(mtlAbstract.Abc_Datumset):
    SET_CHILD_CLS = Dat_Integer

    datum_string_separator = mtlCore.Separator_Raw_String

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of datum, raw.
        """
        self._initAbcDatumSet(*args)


class Dat_IntegerNN(mtlAbstract.Abc_Datumset):
    SET_CHILD_CLS = Dat_IntegerN

    datum_string_separator = mtlCore.Separator_Raw_String_Array

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatumSet(*args)


class Dat_Float(_Dat_Method):
    RAW_CLS = float

    raw_type = float, int

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatum(*args)


class Dat_FloatN(mtlAbstract.Abc_Datumset):
    SET_CHILD_CLS = Dat_Float

    datum_string_separator = mtlCore.Separator_Raw_String

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatumSet(*args)


class Dat_FloatNN(mtlAbstract.Abc_Datumset):
    SET_CHILD_CLS = Dat_FloatN

    datum_string_separator = mtlCore.Separator_Raw_String_Array

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatumSet(*args)


class Dat_String(mtlAbstract.Abc_Datum):
    RAW_CLS = unicode

    raw_type = unicode, str

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatum(*args)


class Dat_StringN(mtlAbstract.Abc_Datumset):
    SET_CHILD_CLS = Dat_String

    datum_string_separator = mtlCore.Separator_Raw_String

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatumSet(*args)


class Dat_FileName(mtlAbstract.Abc_Datum):
    RAW_CLS = unicode

    raw_type = unicode, str

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatum(*args)


class Dat_NodeName(mtlAbstract.Abc_Datum):
    RAW_CLS = unicode

    raw_type = unicode, str

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatum(*args)


class Dat_NodeNameN(mtlAbstract.Abc_Datumset):
    SET_CHILD_CLS = Dat_NodeName

    datum_string_separator = mtlCore.Separator_Raw_String

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of datum, raw.
        """
        self._initAbcDatumSet(*args)
