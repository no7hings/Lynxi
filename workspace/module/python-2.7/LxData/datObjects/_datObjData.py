# coding:utf-8
from .. import datCfg, datObjAbs


class _Dat_Digit(datObjAbs.AbsDatData):
    def __add__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_dat__raw__rawtype_pattern), u'Argument Error, "arg" Must "VAR_dat__raw__rawtype_pattern".'
        return self.__class__(self, self.raw() + other.raw())

    def __sub__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_dat__raw__rawtype_pattern), u'Argument Error, "arg" Must "VAR_dat__raw__rawtype_pattern".'
        return self.__class__(self, self.raw() - other.raw())

    def __mul__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_dat__raw__rawtype_pattern), u'Argument Error, "arg" Must "VAR_dat__raw__rawtype_pattern".'

        return self.__class__(self, self.raw() * other.raw())

    def __div__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_dat__raw__rawtype_pattern), u'Argument Error, "arg" Must "VAR_dat__raw__rawtype_pattern".'

        return self.__class__(self, self.raw() / other.raw())


class Dat_Closure(datObjAbs.AbsDatData):
    CLS_dat__raw = None
    VAR_dat__raw__rawtype_pattern = None

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)

    def _raw__get_str_(self):
        return u''


class Dat_Boolean(datObjAbs.AbsDatData):
    CLS_dat__raw = bool

    VAR_dat__raw__rawtype_pattern = bool, int
    VAR_dat__raw__default = False

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)

    def _raw__get_raw_by_str(self, string):
        _dict = {'false': False, 'true': True}
        if string in _dict:
            return _dict[string]
        else:
            return False

    def _raw__get_str_(self):
        if self.hasRaw():
            return [u'false', u'true'][self.raw()]
        return u'false'


class Dat_Integer(_Dat_Digit):
    CLS_dat__raw = int

    VAR_dat__raw__rawtype_pattern = int, float
    VAR_dat__raw__default = 0

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_IntegerN(datObjAbs.AbsDatData):
    CLS_dat__raw = list

    VAR_dat__raw__rawtype_pattern = list, tuple
    VAR_dat__raw__default = []

    CLS_dat__data__element = Dat_Integer

    VAR_dat__data__datasep = datCfg.DatUtility.DEF_dat__raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_IntegerNN(datObjAbs.AbsDatData):
    CLS_dat__raw = list

    VAR_dat__raw__rawtype_pattern = list, tuple
    VAR_dat__raw__default = []

    CLS_dat__data__element = Dat_IntegerN

    VAR_dat__data__datasep = datCfg.DatUtility.DEF_dat__compraw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_Float(_Dat_Digit):
    CLS_dat__raw = float

    VAR_dat__raw__rawtype_pattern = float, int
    VAR_dat__raw__default = 0.0

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_FloatN(datObjAbs.AbsDatData):
    CLS_dat__raw = list

    VAR_dat__raw__rawtype_pattern = list, tuple
    VAR_dat__raw__default = []

    CLS_dat__data__element = Dat_Float

    VAR_dat__data__datasep = datCfg.DatUtility.DEF_dat__raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_FloatNN(datObjAbs.AbsDatData):
    CLS_dat__raw = list

    VAR_dat__raw__rawtype_pattern = list, tuple
    VAR_dat__raw__default = []

    CLS_dat__data__element = Dat_FloatN

    VAR_dat__data__datasep = datCfg.DatUtility.DEF_dat__compraw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_String(datObjAbs.AbsDatData):
    CLS_dat__raw = unicode

    VAR_dat__raw__rawtype_pattern = unicode, str
    VAR_dat__raw__default = u''

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_StringN(datObjAbs.AbsDatData):
    CLS_dat__raw = list

    VAR_dat__raw__rawtype_pattern = list, tuple
    VAR_dat__raw__default = []

    CLS_dat__data__element = Dat_String

    VAR_dat__data__datasep = datCfg.DatUtility.DEF_dat__raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_Filepath(datObjAbs.AbsDatData):
    CLS_dat__raw = unicode

    VAR_dat__raw__rawtype_pattern = unicode, str
    VAR_dat__raw__default = u''

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_FilepathN(datObjAbs.AbsDatData):
    CLS_dat__raw = list

    VAR_dat__raw__rawtype_pattern = list, tuple
    VAR_dat__raw__default = []

    CLS_dat__data__element = Dat_Filepath

    VAR_dat__data__datasep = datCfg.DatUtility.DEF_dat__raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_Nodename(datObjAbs.AbsDatData):
    CLS_dat__raw = unicode

    VAR_dat__raw__rawtype_pattern = unicode, str
    VAR_dat__raw__default = u''

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)


class Dat_NodenameN(datObjAbs.AbsDatData):
    CLS_dat__raw = list

    VAR_dat__raw__rawtype_pattern = list, tuple
    VAR_dat__raw__default = []

    CLS_dat__data__element = Dat_Nodename

    VAR_dat__data__datasep = datCfg.DatUtility.DEF_dat__raw_strsep

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbsDatData(*args)
