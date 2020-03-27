# coding:utf-8


class Def_BscRaw(object):
    VAR_bsc_rawtype = None

    def _initDefBscRaw(self, *args):
        self._raw = None
        self._set_raw_(*args)

    def _set_raw_(self, *args):
        if args:
            self._raw = args[0]

    def _set_raw_string_(self, *args):
        pass

    def _set_raw_type_(self, *args):
        pass

    def _get_raw_string_(self):
        pass

    def rawtype(self):
        """
        :return: str
        """
        return self.VAR_bsc_rawtype

    def rawtypeString(self):
        pass

    def raw(self):
        """
        :return: raw of typed
        """
        return self._raw

    def rawString(self):
        return self._get_raw_string_()

    def hasRaw(self):
        """
        :return: bool
        """
        return self._raw is not None

    def setRaw(self, raw):
        """
        :param raw: raw
        :return: None
        """
        self._raw = raw

    def toString(self):
        """
        :return: str
        """
        return self._get_raw_string_()

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

    def __str__(self):
        return '{}(raw="{}")'.format(type(self._raw).__name__, self._get_raw_string_())

    def __repr__(self):
        return self.__str__()


class Def_BscObjname(Def_BscRaw):
    CLS_bsc_raw = None

    VAR_bsc_namesep = None

    def _initDefBscObjname(self, *args):
        self._initDefBscRaw(*args)

        self._rawObjList = []

        self._set_raw_(*args)

    def _get_namespace_string_(self):
        pass

    def namesep(self):
        return self.VAR_bsc_namesep

    def name(self):
        if self.hasRaw():
            return self._rawObjList[-1]

    def nameString(self):
        """
        :return: str
        """
        if self.hasRaw():
            return self.name().toString()

    def objnameString(self):
        return self._get_raw_string_()

    def namespaces(self):
        if self.hasRaw():
            return self._rawObjList[:-1]

    def namespaceString(self):
        return self.VAR_bsc_namesep.join([i._get_raw_string_() for i in self._rawObjList[:-1]])


class Def_BscObjpath(Def_BscRaw):
    CLS_bsc_raw = None

    VAR_bsc_pathsep = None

    def _initDefBscObjpath(self, *args):
        self._initDefBscRaw(*args)

        self._rawObjList = []

        self._set_raw_(*args)

    def paths(self):
        if self.hasRaw():
            return self._rawObjList[:-1]

    def pathString(self):
        return self.VAR_bsc_pathsep.join([i._get_raw_string_() for i in self._rawObjList[:-1]])

    def name(self):
        """
        :return: object
        """
        if self.hasRaw():
            return self._rawObjList[-1]

    def nameString(self):
        """
        :return: str
        """
        if self.hasRaw():
            return self.name().toString()

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        if self.name():
            self.name()._set_raw_string_(nameString)

    def objpathString(self):
        """
        :return: str
        """
        return self._get_raw_string_()

    def pathsep(self):
        """
        :return: str
        """
        return self.VAR_bsc_pathsep

