# coding:utf-8
from ..import datCfg, datObjAbs


class _Dat_Digit(datObjAbs.Abs_DatData):
    def __add__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_dat_rawtype_pattern), u'Argument Error, "arg" Must "VAR_dat_rawtype_pattern".'
        return self.__class__(self, self.raw() + other.raw())

    def __sub__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_dat_rawtype_pattern), u'Argument Error, "arg" Must "VAR_dat_rawtype_pattern".'
        return self.__class__(self, self.raw() - other.raw())

    def __mul__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_dat_rawtype_pattern), u'Argument Error, "arg" Must "VAR_dat_rawtype_pattern".'

        return self.__class__(self, self.raw() * other.raw())

    def __div__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_dat_rawtype_pattern), u'Argument Error, "arg" Must "VAR_dat_rawtype_pattern".'

        return self.__class__(self, self.raw() / other.raw())


class Dat_Closure(datObjAbs.Abs_DatData):
    CLS_dat_raw = None
    VAR_dat_rawtype_pattern = None

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)

    def _get_rawstr_(self):
        return u''


class Dat_Boolean(datObjAbs.Abs_DatData):
    CLS_dat_raw = bool

    VAR_dat_rawtype_pattern = bool, int
    VAR_dat_raw_default = False

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)

    def _set_rawstr_to_rawobj_(self, string):
        _dict = {'false': False, 'true': True}
        if string in _dict:
            return _dict[string]
        else:
            return False

    def _get_rawstr_(self):
        if self.hasRaw():
            return [u'false', u'true'][self.raw()]
        return u'false'


class Dat_Integer(_Dat_Digit):
    CLS_dat_raw = int

    VAR_dat_rawtype_pattern = int, float
    VAR_dat_raw_default = 0

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_IntegerN(datObjAbs.Abs_DatData):
    CLS_dat_raw = list

    VAR_dat_rawtype_pattern = list, tuple
    VAR_dat_raw_default = []

    CLS_dat_data = Dat_Integer

    VAR_dat_compraw_strsep = datCfg.Utility.DEF_dat_raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_IntegerNN(datObjAbs.Abs_DatData):
    CLS_dat_raw = list

    VAR_dat_rawtype_pattern = list, tuple
    VAR_dat_raw_default = []

    CLS_dat_data = Dat_IntegerN

    VAR_dat_compraw_strsep = datCfg.Utility.DEF_dat_compraw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_Float(_Dat_Digit):
    CLS_dat_raw = float

    VAR_dat_rawtype_pattern = float, int
    VAR_dat_raw_default = 0.0

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_FloatN(datObjAbs.Abs_DatData):
    CLS_dat_raw = list

    VAR_dat_rawtype_pattern = list, tuple
    VAR_dat_raw_default = []

    CLS_dat_data = Dat_Float

    VAR_dat_compraw_strsep = datCfg.Utility.DEF_dat_raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_FloatNN(datObjAbs.Abs_DatData):
    CLS_dat_raw = list

    VAR_dat_rawtype_pattern = list, tuple
    VAR_dat_raw_default = []

    CLS_dat_data = Dat_FloatN

    VAR_dat_compraw_strsep = datCfg.Utility.DEF_dat_compraw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_String(datObjAbs.Abs_DatData):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_StringN(datObjAbs.Abs_DatData):
    CLS_dat_raw = list

    VAR_dat_rawtype_pattern = list, tuple
    VAR_dat_raw_default = []

    CLS_dat_data = Dat_String

    VAR_dat_compraw_strsep = datCfg.Utility.DEF_dat_raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_Filename(datObjAbs.Abs_DatData):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_FilenameN(datObjAbs.Abs_DatData):
    CLS_dat_raw = list

    VAR_dat_rawtype_pattern = list, tuple
    VAR_dat_raw_default = []

    CLS_dat_data = Dat_Filename

    VAR_dat_compraw_strsep = datCfg.Utility.DEF_dat_raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_Nodename(datObjAbs.Abs_DatData):
    CLS_dat_raw = unicode

    VAR_dat_rawtype_pattern = unicode, str
    VAR_dat_raw_default = u''

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_NodenameN(datObjAbs.Abs_DatData):
    CLS_dat_raw = list

    VAR_dat_rawtype_pattern = list, tuple
    VAR_dat_raw_default = []

    CLS_dat_data = Dat_Nodename

    VAR_dat_compraw_strsep = datCfg.Utility.DEF_dat_raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)
