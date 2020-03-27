# coding:utf-8
from LxMaterial import mtlObjCore, mtlConfigure

from LxMaterial.mtlObjects import _mtlObjRaw


class _Dat_Method(mtlObjCore.Abc_MtlData):
    def __add__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_mtl_raw_type), u'Argument Error, "arg" Must "VAR_mtl_raw_type".'

        return self.__class__(self, self.raw() + other.raw())

    def __sub__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_mtl_raw_type), u'Argument Error, "arg" Must "VAR_mtl_raw_type".'

        return self.__class__(self, self.raw() - other.raw())

    def __mul__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_mtl_raw_type), u'Argument Error, "arg" Must "VAR_mtl_raw_type".'

        return self.__class__(self, self.raw() * other.raw())

    def __div__(self, other):
        """
        :param other: object of "Data"
        :return: number
        """
        assert isinstance(other.raw(), self.VAR_mtl_raw_type), u'Argument Error, "arg" Must "VAR_mtl_raw_type".'

        return self.__class__(self, self.raw() / other.raw())


class Dat_Closure(mtlObjCore.Abc_MtlData):
    CLS_bsc_raw = _mtlObjRaw.Raw_Closure

    VAR_mtl_raw_type = None

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlData(*args)

    def toString(self):
        return ''


class Dat_Boolean(mtlObjCore.Abc_MtlData):
    CLS_bsc_raw = bool

    VAR_mtl_raw_type = bool, int

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlData(*args)

    def _stringToRaw_(self, string):
        return {'false': False, 'true': True}[string]

    def toString(self):
        """
        "true" / false"
        :return: str
        """
        if self.hasRaw():
            return ['false', 'true'][self.raw()]


class Dat_Integer(_Dat_Method):
    CLS_bsc_raw = int

    VAR_mtl_raw_type = int, float

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlData(*args)


class Dat_IntegerN(mtlObjCore.Abc_MtlMultidata):
    CLS_mtl_data = Dat_Integer

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2.object of data, raw.
        """
        self._initAbcMtlMultidata(*args)


class Dat_IntegerNN(mtlObjCore.Abc_MtlMultidata):
    CLS_mtl_data = Dat_IntegerN

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_array_separator

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlMultidata(*args)


class Dat_Float(_Dat_Method):
    CLS_bsc_raw = float

    VAR_mtl_raw_type = float, int

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlData(*args)


class Dat_FloatN(mtlObjCore.Abc_MtlMultidata):
    CLS_mtl_data = Dat_Float

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlMultidata(*args)


class Dat_FloatNN(mtlObjCore.Abc_MtlMultidata):
    CLS_mtl_data = Dat_FloatN

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_array_separator

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlMultidata(*args)


class Dat_string(mtlObjCore.Abc_MtlData):
    CLS_bsc_raw = unicode

    VAR_mtl_raw_type = unicode, str

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlData(*args)


class Dat_stringN(mtlObjCore.Abc_MtlMultidata):
    CLS_mtl_data = Dat_string

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlMultidata(*args)


class Dat_file_name(mtlObjCore.Abc_MtlData):
    CLS_bsc_raw = unicode

    VAR_mtl_raw_type = unicode, str

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlData(*args)


class Dat_NodeName(mtlObjCore.Abc_MtlData):
    CLS_bsc_raw = unicode

    VAR_mtl_raw_type = unicode, str

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlData(*args)


class Dat_NodeNameN(mtlObjCore.Abc_MtlMultidata):
    CLS_mtl_data = Dat_NodeName

    VAR_mtl_data_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_file_attribute_attach_key = 'datastring'

    def __init__(self, *args):
        """
        :param args:
            1-1.object of value, raw;
            1-2..object of data, raw.
        """
        self._initAbcMtlMultidata(*args)
