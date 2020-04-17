# coding:utf-8
from . import datCfg


# ******************************************************************************************************************** #
class Def_DatRaw(datCfg.Utility):
    CLS_dat_raw = None

    VAR_dat_rawtype_pattern = None
    VAR_dat_raw_default = None

    VAR_dat_rawtype_str_dict = {
        'unicode': 'string',
        'str': 'string',
        'int': 'integer',
        'float': 'float',
        'list': 'array',
        'tuple': 'group',
        'None': 'null',
    }

    def _initDefDatRaw(self, *args):
        self._rawObj = None

        self._set_raw_create_(*args)

    # raw ************************************************************************************************************ #
    def _get_raw_cls_(self):
        return self.CLS_dat_raw

    def _set_raw_val_(self, raw):
        if self.VAR_dat_rawtype_pattern is not None:
            if isinstance(raw, self.VAR_dat_rawtype_pattern) is False:
                if isinstance(self.VAR_dat_rawtype_pattern, (tuple, list)):
                    _ = ' or '.join(['"{}"'.format(i.__name__) for i in self.VAR_dat_rawtype_pattern])
                else:
                    _ = '"{}"'.format(self.VAR_dat_rawtype_pattern)
                tipString = u'class "{}" input raw must be type of {}.'.format(self.__class__.__name__, _)
                raise TypeError(tipString)

    def _set_raw_to_rawobj_(self, *args):
        raw = args[0]

        if self.CLS_dat_raw is not None:
            return self.CLS_dat_raw(raw)

    def _set_raw_create_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                self._set_raw_val_(raw)
                self._rawObj = self._set_raw_to_rawobj_(raw)

    def _get_raw_(self):
        return self._rawObj

    def setRaw(self, *args):
        self._set_raw_create_(*args)

    def raw(self):
        """
        :return: raw of typed
        """
        return self._get_raw_()

    # rawstr ********************************************************************************************************* #
    def _set_rawstr_val_(self, rawString):
        if isinstance(rawString, (str, unicode)) is False:
            tipString = u'class "{}" input raw must be "str" or "unicode"'.format(self.__class__.__name__)
            raise TypeError(tipString)

    def _set_rawstr_to_rawobj_(self, *args):
        rawstr = args[0]
        if self.CLS_dat_raw is not None:
            return self.CLS_dat_raw(rawstr)

    def _set_rawstr_create_(self, *args):
        if args:
            rawstr = args[0]
            if rawstr is not None:
                self._set_rawstr_val_(rawstr)

                self._rawObj = self._set_rawstr_to_rawobj_(rawstr)

    def _get_rawstr_(self):
        if self._rawObj is not None:
            return unicode(self._rawObj)
        return u''

    def setRawString(self, *args):
        self._set_rawstr_create_(*args)

    def rawString(self):
        return self._get_rawstr_()

    # create ********************************************************************************************************* #
    def _set_create_(self, *args):
        if isinstance(args[0], (str, unicode)):
            self._set_rawstr_create_(*args)
        else:
            self._set_raw_create_(*args)

    def create(self, *args):
        """
        :param args:
            1.raw of typed
            2.str
        :return: None
        """
        assert args is not (), u'argument must not be "empty".'
        self._set_create_(*args)

    # **************************************************************************************************************** #
    def _set_raw_type_(self, *args):
        pass

    def _get_rawtypestr_(self):
        return self.VAR_dat_rawtype_str_dict[self.CLS_dat_raw.__name__]

    def rawtype(self):
        return self._get_raw_cls_()

    def rawtypeString(self):
        return self._get_rawtypestr_()

    def hasRaw(self):
        """
        :return: bool
        """
        return self._rawObj is not None

    def toString(self):
        """
        :return: str
        """
        return self._get_rawstr_()

    # **************************************************************************************************************** #
    def __eq__(self, other):
        """
        :param other: typed raw
        :return: bool
        """
        return self.toString() == other.toString()

    def __ne__(self, other):
        """
        :param other: typed raw
        :return: bool
        """
        return self.toString() != other.toString()

    # **************************************************************************************************************** #
    def __str__(self):
        return u'{}("{}")'.format(self._get_rawtypestr_(), self._get_rawstr_())

    def __repr__(self):
        return self.__str__()


class Def_DatNodename(Def_DatRaw):
    CLS_dat_namespace = None
    CLS_dat_name = None

    VAR_dat_namesep = None

    def _initDefDatFilename(self, *args):
        self._namespaceObj = self.CLS_dat_namespace()
        self._nameObj = self.CLS_dat_name()

        self._initDefDatRaw(*args)

    def namespace(self):
        return self._namespaceObj

    def namespaceString(self):
        return self._namespaceObj.toString()

    # **************************************************************************************************************** #
    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    @classmethod
    def namesep(cls):
        return cls.VAR_dat_namesep


class Def_DatFilename(Def_DatRaw):
    CLS_dat_base = None
    CLS_dat_ext = None

    VAR_dat_extsep = None

    def _initDefDatFilename(self, *args):
        self._baseObj = self.CLS_dat_base()
        self._extObj = self.CLS_dat_ext()
        self._initDefDatRaw(*args)

    def base(self):
        return self._baseObj

    def baseString(self):
        return self._baseObj.toString()

    def ext(self):
        return self._extObj

    def extString(self):
        return self._extObj.toString()


class Def_DatPath(Def_DatRaw):
    CLS_dat_dirname = None
    CLS_dat_bscname = None

    VAR_dat_pathsep = None

    def _initDefDatPath(self, *args):
        self._dirnameObj = self.CLS_dat_dirname()
        self._bscnameObj = self.CLS_dat_bscname()

        self._initDefDatRaw(*args)

    # **************************************************************************************************************** #
    def dirname(self):
        """
        :return: obj
        """
        return self._dirnameObj

    def dirnameString(self):
        return self._dirnameObj.toString()

    def setDirnameString(self, *args):
        self._dirnameObj.setRawString(*args)

    # **************************************************************************************************************** #
    def bscname(self):
        return self._bscnameObj

    def bscnameString(self):
        """
        :return: str
        """
        return self._bscnameObj.toString()

    def setBscnameString(self, *args):
        self._bscnameObj.setRawString(*args)

    # **************************************************************************************************************** #
    def name(self):
        return self.bscname()

    def nameString(self):
        return self.bscnameString()

    def setNameString(self, nameString):
        self.setBscnameString(nameString)

    @classmethod
    def pathsep(cls):
        """
        :return: str
        """
        return cls.VAR_dat_pathsep


class Def_DatAttrpath(Def_DatRaw):
    CLS_dat_nodepath = None
    CLS_dat_portpath = None

    def _initDefDatAttrpath(self, *args):
        self._nodepathObj = self.CLS_dat_nodepath()
        self._portpathObj = self.CLS_dat_portpath()

        self._initDefDatRaw(*args)

    def nodepath(self):
        return self._nodepathObj

    def nodepathString(self):
        return self._nodepathObj.toString()

    def portpath(self):
        return self._portpathObj

    def portpathString(self):
        return self._portpathObj.toString()
