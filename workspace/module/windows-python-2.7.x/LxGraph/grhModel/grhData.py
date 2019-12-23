# coding:utf-8
from LxGraph import grhAbstract, grhConfigure


class _DatDigitBasic(grhAbstract.AbcData):
    def __add__(self, other):
        """
        :param other: object of Data
        :return: number
        """
        return self.__class__(self.raw() + other.raw())

    def __sub__(self, other):
        """
        :param other: object of Data
        :return: number
        """
        return self.__class__(self.raw() - other.raw())

    def __mul__(self, other):
        """
        :param other: object of Data
        :return: number
        """
        return self.__class__(self.raw() * other.raw())

    def __div__(self, other):
        """
        :param other: object of Data
        :return: number
        """
        return self.__class__(self.raw() / other.raw())


class DatInteger(_DatDigitBasic):
    def __init__(self, *args):
        self._initAbcData()
        if args is not ():
            self.create(*args)

    def create(self, *args):
        """
        :param args: int
        :return: None
        """
        assert args is not (), 'Argument Not be Empty.'
        raw = args[0]
        assert isinstance(raw, int) or isinstance(raw, float), 'Argument Error, "args[0]" Must "int" or "float".'
        self.setRaw(int(raw))

    def toString(self):
        """
        :return: str
        """
        return str(self.raw())


class DatFloat(_DatDigitBasic):
    def __init__(self, *args):
        self._initAbcData()
        if args is not ():
            self.create(*args)

    def create(self, *args):
        """
        :param args: float
        :return: None
        """
        assert args is not (), 'Argument Not be Empty.'
        raw = args[0]
        assert isinstance(raw, int) or isinstance(raw, float), 'Argument Error, "args[0]" Must "int" or "float".'
        if raw is not None:
            self.setRaw(float(raw))

    def toString(self):
        """
        :return: str
        """
        return str(self.raw())


class DatBoolean(grhAbstract.AbcData):
    def __init__(self, *args):
        self._initAbcData()
        if args is not ():
            self.create(*args)

    def create(self, *args):
        """
        :param args: bool
        :return: None
        """
        assert args is not (), 'Argument Not be Empty.'
        raw = args[0]
        assert isinstance(raw, int), 'Argument Error, "arg" Must "bool".'
        self.setRaw(raw)

    def toString(self):
        """
        "true" / false"
        :return: str
        """
        return ['false', 'true'][self.raw()]


class DatString(grhAbstract.AbcData):
    def __init__(self, *args):
        self._initAbcData()
        if args is not ():
            self.create(*args)

    def create(self, *args):
        """
        :param args: str
        :return: None
        """
        assert args is not (), 'Argument Not be Empty.'
        raw = args[0]
        assert isinstance(raw, str) or isinstance(args[0], unicode), 'Argument Error, "arg" Must "str" or "unicode".'
        self.setRaw(raw)

    def toString(self):
        """
        :return: str
        """
        return self.raw()


class DatFileName(grhAbstract.AbcData):
    def __init__(self, *args):
        self._initAbcData()
        if args is not ():
            self.create(*args)

    def create(self, *args):
        """
        :param args: str
        :return: None
        """
        assert args is not (), 'Argument Not be Empty.'
        raw = args[0]
        assert isinstance(raw, str) or isinstance(args[0], unicode), 'Argument Error, "args[0]" Must "str" or "unicode".'
        self.setRaw(raw)

    def toString(self):
        """
        :return: str
        """
        return self.raw()


class DatNodeName(grhAbstract.AbcData):
    def __init__(self, *args):
        self._initAbcData()
        if args is not ():
            self.create(*args)

    def create(self, *args):
        """
        :param args: str
        :return: None
        """
        assert args is not (), 'Argument Not be Empty.'
        raw = args[0]
        assert isinstance(raw, str) or isinstance(args[0], unicode), 'Argument Error, "args[0]" Must "str" or "unicode".'
        self.setRaw(raw)

    def toString(self):
        """
        :return: str
        """
        return self.raw()


class DatIntegerN(grhAbstract.AbcDataN):
    RawSeparatorString = grhConfigure.Separator_String_Raw
    CHILD_CLS = DatInteger

    def __init__(self, *args):
        self._initAbcDataN()
        if args is not ():
            self.create(*args)


class DatFloatN(grhAbstract.AbcDataN):
    RawSeparatorString = grhConfigure.Separator_String_Raw
    CHILD_CLS = DatFloat

    def __init__(self, *args):
        self._initAbcDataN()
        if args is not ():
            self.create(*args)


class DatStringN(grhAbstract.AbcDataN):
    RawSeparatorString = grhConfigure.Separator_String_Raw
    CHILD_CLS = DatString

    def __init__(self, *args):
        self._initAbcDataN()
        if args is not ():
            self.create(*args)


class DatNodeNameN(grhAbstract.AbcDataN):
    RawSeparatorString = grhConfigure.Separator_String_Raw
    CHILD_CLS = DatNodeName

    def __init__(self, *args):
        self._initAbcDataN()
        if args is not ():
            self.create(*args)


class DatIntegerNN(grhAbstract.AbcDataNN):
    RawSeparatorString = grhConfigure.Separator_String_Raw_Array
    CHILD_CLS = DatIntegerN

    def __init__(self, *args):
        self._initAbcDataNN()
        if args is not ():
            self.create(*args)


class DatFloatNN(grhAbstract.AbcDataNN):
    RawSeparatorString = grhConfigure.Separator_String_Raw_Array
    CHILD_CLS = DatFloatN

    def __init__(self, *args):
        self._initAbcDataNN()
        if args is not ():
            self.create(*args)
