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


# ******************************************************************************************************************** #
class Def_DatName(datCfg.Utility):
    def _initDefDatName(self, *args):
        self._set_name_build_(*args)

    # **************************************************************************************************************** #
    def _set_name_build_(self, *args):
        if args:
            raw = args[0]
            self._raw = unicode(raw)

    def _get_name_raw_(self):
        return self._raw

    def setRaw(self, *args):
        self._set_name_build_(*args)

    def raw(self):
        return self._raw

    # **************************************************************************************************************** #
    def toString(self):
        return self._get_name_raw_()

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}(raw="{}")'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()


class Def_DatNodename(datCfg.Utility):
    CLS_dat_namespace = None
    CLS_dat_name = None

    VAR_dat_namesep = None

    def _initDefDatFilename(self, *args):
        self._set_nodename_build_(*args)

    # **************************************************************************************************************** #
    def _set_nodename_build_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                sep = self.VAR_dat_namesep
                _ = raw.split(sep)
                if len(_) == 1:
                    namespaceString = sep
                    nameString = _[0]
                else:
                    namespaceString = sep.join([i for i in _[:-1] if i])
                    if namespaceString == u'':
                        namespaceString = sep
                    nameString = _[-1]

                self._namespaceObj = self.CLS_dat_namespace(namespaceString)
                self._nameObj = self.CLS_dat_name(nameString)

    def _get_nodename_raw_(self):
        sep = self.VAR_dat_namesep
        if self.namespaceString() == sep:
            return self.nameString()
        return sep.join(
            [self.namespaceString(), self.nameString()]
        )

    def setRaw(self, *args):
        self._set_nodename_build_(*args)

    def raw(self):
        return self._get_nodename_raw_()

    # **************************************************************************************************************** #
    def hasNamespace(self):
        return self._namespaceObj is not None

    def namespace(self):
        return self._namespaceObj

    def namespaceString(self):
        if self.hasNamespace():
            return self._namespaceObj.toString()

    # **************************************************************************************************************** #
    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    # **************************************************************************************************************** #
    def nodenameString(self):
        return self._get_nodename_raw_()

    # **************************************************************************************************************** #
    def toString(self):
        return self._get_nodename_raw_()

    # **************************************************************************************************************** #
    @classmethod
    def namesep(cls):
        return cls.VAR_dat_namesep

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}(raw="{}")'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()


class Def_DatFilename(datCfg.Utility):
    CLS_dat_base = None
    CLS_dat_ext = None

    VAR_dat_extsep = None

    def _initDefDatFilename(self, *args):
        self._set_filename_build_(*args)

    # **************************************************************************************************************** #
    def _set_filename_build_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                sep = self.VAR_dat_extsep

                _ = raw.split(sep)
                if len(_) == 1:
                    baseString = _[0]
                    self._baseObj = self.CLS_dat_base(baseString)
                    self._extObj = None
                else:
                    baseString = sep.join(_[:-1])
                    extString = sep + _[-1]
                    self._baseObj = self.CLS_dat_base(baseString)
                    self._extObj = self.CLS_dat_ext(extString)

    def _get_filename_raw_(self):
        if self.hasExt():
            return self.baseString() + self.extString()
        return self.baseString()

    def setRaw(self, *args):
        self._set_filename_build_(*args)

    def raw(self):
        return self._get_filename_raw_()

    # **************************************************************************************************************** #
    def base(self):
        return self._baseObj

    def baseString(self):
        return self._baseObj.toString()

    def hasExt(self):
        return self._extObj is not None

    def ext(self):
        return self._extObj

    def extString(self):
        if self.hasExt():
            return self._extObj.toString()

    # **************************************************************************************************************** #
    def toString(self):
        return self._get_filename_raw_()

    # **************************************************************************************************************** #
    @classmethod
    def extsep(cls):
        return cls.VAR_dat_extsep

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}(raw="{}")'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()


class Def_DatPath(datCfg.Utility):
    CLS_dat_name = None

    VAR_dat_pathsep = None

    def _initDefDatPath(self, *args):
        self._parentObj = None
        self._childObjList = []

        self._set_path_build_(*args)

    # **************************************************************************************************************** #
    def _set_path_build_(self, *args):
        if args:
            if len(args) == 1:
                raw = args[0]
                if raw is not None:
                    sep = self.VAR_dat_pathsep

                    if raw == sep:
                        self._parentObj = None
                        self._nameObj = self.CLS_dat_name(sep)
                    else:
                        _ = raw.split(sep)

                        if len(_) == 1:
                            self._parentObj = None
                            nameRaw = _[-1]
                        else:
                            parentRawString = sep.join([i for i in _[:-1]])
                            # root
                            if parentRawString == u'':
                                self._parentObj = self.__class__(sep)
                            else:
                                self._parentObj = self.__class__(parentRawString)

                            nameRaw = _[-1]

                        self._nameObj = self.CLS_dat_name(nameRaw)
            elif len(args) == 2:
                parentRaw, nameRaw = args
                if isinstance(parentRaw, Def_DatPath):
                    self._parentObj = parentRaw
                elif isinstance(parentRaw, (str, unicode)):
                    self._parentObj = self.__class__(parentRaw)

                if isinstance(nameRaw, Def_DatRaw):
                    self._nameObj = nameRaw
                elif isinstance(nameRaw, (str, unicode)):
                    self._nameObj = self.CLS_dat_name(nameRaw)
            #
            if self._parentObj is not None:
                self._parentObj._set_child_add_(self)

    def _get_path_raw_(self):
        sep = self.VAR_dat_pathsep
        if self._parentObj is None:
            return self.nameString()
        elif self.parentString() == sep:
            return sep + sep.join(
                [
                    i
                    for i in [self.nameString()]
                ]
            )
        return sep.join(
            [
                i
                for i in [self.parentString(), self.nameString()]
            ]
        )

    def setRaw(self, *args):
        self._set_path_build_(*args)

    def raw(self):
        return self._get_path_raw_()

    # **************************************************************************************************************** #
    def _get_parent_exist_(self):
        return self._parentObj is not None

    def hasParent(self):
        return self._get_parent_exist_()

    def setParent(self, *args):
        pass

    def parent(self):
        return self._parentObj

    def setParentString(self, *args):
        pass

    def parentString(self):
        if self._get_parent_exist_():
            return self._parentObj.toString()

    # **************************************************************************************************************** #
    def _set_child_add_(self, *args):
        obj = args[0]
        self._childObjList.append(obj)

    def children(self):
        return self._childObjList

    def addChild(self, *args):
        self._set_child_add_(*args)

    def child(self, *args):
        index = args[0]
        return self._childObjList[index]

    def _get_all_children_(self):
        def rscFnc_(pathObj_):
            childPathObjs = pathObj_.children()
            if childPathObjs:
                for _pathObj in childPathObjs:
                    rscFnc_(_pathObj)
                    lis.append(_pathObj)

        lis = []

        rscFnc_(self)
        return lis

    def allChildren(self):
        return self._get_all_children_()

    # **************************************************************************************************************** #
    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def setNameString(self, *args):
        self._nameObj.setRaw(*args)

    # **************************************************************************************************************** #
    def toString(self):
        return self._get_path_raw_()

    # **************************************************************************************************************** #
    @classmethod
    def pathsep(cls):
        return cls.VAR_dat_pathsep

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}(raw="{}")'.format(
            self.__class__.__name__, self.raw()
        )

    def __repr__(self):
        return self.__str__()


class Def_DatNamespace(Def_DatPath):
    def _initDefDatNamespace(self, *args):
        self._initDefDatPath(*args)


class Def_DatAttrpath(datCfg.Utility):
    CLS_dat_nodepath = None
    CLS_dat_portpath = None

    def _initDefDatAttrpath(self, *args):
        self._set_obj_path_build_(*args)

    # **************************************************************************************************************** #
    def _set_obj_path_build_(self, *args):
        if args:
            # str("nodepath.portpath")
            if len(args) == 1:
                raw = args[0]
                if raw is not None:
                    sep = self.portsep()

                    _ = raw.split(sep)

                    if len(_) == 1:
                        nodepathString = None
                        portpathString = _[-1]
                    else:
                        nodepathString = _[0]
                        portpathString = sep.join([i for i in _[1:]])

                    self._pathObj = self.CLS_dat_nodepath(nodepathString)
                    self._portpathObj = self.CLS_dat_portpath(portpathString)
            elif len(args) == 2:
                nodepathRaw, portpathRaw = args
                # *.objects.Nodepath / str("nodepath")
                if isinstance(nodepathRaw, Def_DatPath):
                    self._pathObj = nodepathRaw
                elif isinstance(nodepathRaw, (str, unicode)):
                    self._pathObj = self.CLS_dat_nodepath(nodepathRaw)
                # objects.Portpath / str("portpath")
                if isinstance(portpathRaw, Def_DatPath):
                    self._portpathObj = portpathRaw
                elif isinstance(portpathRaw, (str, unicode)):
                    self._portpathObj = self.CLS_dat_portpath(portpathRaw)

    def _get_attrpath_raw(self):
        sep = self.portsep()
        return sep.join(
           [
               i
               for i in [self.nodepathString(), self.portpathString()]
               if i
           ]
        )

    def setRaw(self, *args):
        self._set_obj_path_build_(*args)

    def raw(self):
        return self._get_attrpath_raw()

    # **************************************************************************************************************** #
    def nodepath(self):
        return self._pathObj

    def nodepathString(self):
        return self._pathObj.toString()

    def portpath(self):
        return self._portpathObj

    def portpathString(self):
        return self._portpathObj.toString()

    # **************************************************************************************************************** #
    def toString(self):
        return self._get_attrpath_raw()

    # **************************************************************************************************************** #
    @classmethod
    def nodesep(cls):
        return cls.CLS_dat_nodepath.pathsep()

    @classmethod
    def portsep(cls):
        return cls.CLS_dat_portpath.pathsep()

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}(raw="{}")'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()
