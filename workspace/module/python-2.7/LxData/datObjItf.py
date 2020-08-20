# coding:utf-8
from . import datCfg


# raw **************************************************************************************************************** #
class ItfDatRaw(datCfg.DatUtility):
    CLS_dat__raw = None

    VAR_dat__raw__rawtype_pattern = None
    VAR_dat__raw__rawtype_str_dict = {
        'unicode': 'string',
        'str': 'string',
        'int': 'integer',
        'float': 'float',
        'list': 'array',
        'tuple': 'group',
        'None': 'null',
    }

    VAR_dat__raw__default = None

    def _initItfDatRaw(self, *args):
        """
        for __init__
        """
        self._rawObj = None

        self._raw__set_create_by_raw_(*args)

    # raw ************************************************************************************************************ #
    def _raw__get_raw_cls_(self):
        return self.CLS_dat__raw

    def _raw__set_raw_val_(self, raw):
        if self.VAR_dat__raw__rawtype_pattern is not None:
            if isinstance(raw, self.VAR_dat__raw__rawtype_pattern) is False:
                if isinstance(self.VAR_dat__raw__rawtype_pattern, (tuple, list)):
                    _ = u' or '.join([u'"{}"'.format(i.__name__) for i in self.VAR_dat__raw__rawtype_pattern])
                else:
                    _ = u'"{}"'.format(self.VAR_dat__raw__rawtype_pattern)
                tipString = u'class "{}" input raw must be type of {} not "{}".'.format(
                    self.__class__.__name__, _, raw.__class__.__name__
                )
                raise TypeError(tipString)

    def _raw__get_obj_by_raw(self, *args):
        raw = args[0]
        if self.CLS_dat__raw is not None:
            return self.CLS_dat__raw(raw)

    def _raw__set_create_by_raw_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                self._raw__set_raw_val_(raw)
                self._rawObj = self._raw__get_obj_by_raw(raw)

    def setRaw(self, *args):
        """
        :param args: raw
        :return: None
        """
        self._raw__set_create_by_raw_(*args)

    def _raw__get_raw_(self):
        return self._rawObj

    def raw(self):
        """
        :return: raw
        """
        return self._raw__get_raw_()

    # str ************************************************************************************************************ #
    def _raw__set_str_val_(self, rawString):
        if isinstance(rawString, (str, unicode)) is False:
            tipString = u'class "{}" input raw must be "str" or "unicode"'.format(self.__class__.__name__)
            raise TypeError(tipString)

    def _raw__set_create_by_str_(self, *args):
        if args:
            rawstr = args[0]
            if rawstr is not None:
                self._raw__set_str_val_(rawstr)

                self._rawObj = self._raw__get_raw_by_str(rawstr)

    def _raw__get_raw_by_str(self, *args):
        rawstr = args[0]
        if self.CLS_dat__raw is not None:
            return self.CLS_dat__raw(rawstr)

    def setRawString(self, *args):
        """
        :param args: str(raw)
        :return: None
        """
        self._raw__set_create_by_str_(*args)

    def _raw__get_str_(self):
        if self._rawObj is not None:
            return unicode(self._rawObj)
        return u''

    def rawString(self):
        """
        :return: str(raw)
        """
        return self._raw__get_str_()

    # create ********************************************************************************************************* #
    def _raw__set_create_(self, *args):
        if isinstance(args[0], (str, unicode)):
            self._raw__set_create_by_str_(*args)
        else:
            self._raw__set_create_by_raw_(*args)

    def create(self, *args):
        """
        :param args:
            1.raw
            2.str(raw)
        :return: None
        """
        if args:
            self._raw__set_create_(*args)
        else:
            raise TypeError(u'argument must not be "empty".')

    # type *********************************************************************************************************** #
    def _raw__get_rawtype_str_(self):
        return self.VAR_dat__raw__rawtype_str_dict[self.CLS_dat__raw.__name__]

    def rawtype(self):
        """
        :return: class(raw)
        """
        return self._raw__get_raw_cls_()

    def rawtypeString(self):
        """
        :return: str(type)
        """
        return self._raw__get_rawtype_str_()

    def hasRaw(self):
        """
        :return: bool
        """
        return self._rawObj is not None

    # **************************************************************************************************************** #
    def toString(self):
        """
        :return: str(raw)
        """
        return self._raw__get_str_()

    # **************************************************************************************************************** #
    def __eq__(self, other):
        return self.toString() == other.toString()

    def __ne__(self, other):
        return self.toString() != other.toString()

    # **************************************************************************************************************** #
    def __str__(self):
        return u'{}("{}")'.format(
            self._raw__get_rawtype_str_(), self._raw__get_str_()
        )

    def __repr__(self):
        return self.__str__()


# obj key ************************************************************************************************************ #
class ItfDatObjKey(datCfg.DatUtility):
    def _obj_key_str_(self):
        pass


# name *************************************************************************************************************** #
class ItfDatName(ItfDatObjKey):
    def _initItfDatName(self, *args):
        self._set_name_build_(*args)

    # **************************************************************************************************************** #
    def _set_name_build_(self, *args):
        if args:
            self._raw = args[0]
        else:
            self._raw = None

    def setRaw(self, *args):
        self._set_name_build_(*args)

    def raw(self):
        return self._raw

    # **************************************************************************************************************** #
    def _get_name_raw_str_(self):
        if self._raw:
            return unicode(self._raw)
        return u''

    def toString(self):
        return self._get_name_raw_str_()

    # **************************************************************************************************************** #
    def __str__(self):
        return u'{}(raw="{}")'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()

    # **************************************************************************************************************** #
    def __eq__(self, other):
        if isinstance(other, ItfDatName):
            return self.toString() == other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() == unicode(other)

    def __ne__(self, other):
        if isinstance(other, ItfDatName):
            return self.toString() != other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() != unicode(other)


# type name ********************************************************************************************************** #
class ItfDatTypename(ItfDatObjKey):
    def _initItfDatTypename(self, *args):
        self._typeObj, self._raw = args

    def type(self):
        return self._typeObj

    def raw(self):
        return self._raw

    # **************************************************************************************************************** #
    def _get_typename_raw_str_(self):
        return unicode(self._raw)

    def toString(self):
        return self._get_typename_raw_str_()

    # **************************************************************************************************************** #
    def __str__(self):
        return u'{}.{}'.format(
            self._typeObj.__class__.__name__,
            self._raw
        )

    def __repr__(self):
        return self.__str__()

    # **************************************************************************************************************** #
    def __eq__(self, other):
        if isinstance(other, ItfDatTypename):
            return self.toString() == other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() == unicode(other)

    def __ne__(self, other):
        if isinstance(other, ItfDatTypename):
            return self.toString() != other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() != unicode(other)


class ItfDatType(ItfDatObjKey):
    CLS_dat__type__typename = None

    VAR_dat__type__category_dict = {}
    VAR_dat__type__role_dict = {}

    def _initItfDatType(self, *args):
        self._type__set_build_(*args)

    # **************************************************************************************************************** #
    def _type__set_build_(self, *args):
        if args:
            _ = args[0]
            if isinstance(_, (str, unicode)):
                self._typenameObj = self.CLS_dat__type__typename(
                    self, _
                )
                # category
                if _ in self.VAR_dat__type__category_dict:
                    self._categoryObj = self.CLS_dat__type__typename(
                        self, self.VAR_dat__type__category_dict[_]
                    )
                else:
                    self._categoryObj = self.CLS_dat__type__typename(
                        self, _
                    )
                # role
                if _ in self.VAR_dat__type__role_dict:
                    self._roleObj = self.CLS_dat__type__typename(
                        self, self.VAR_dat__type__role_dict[_]
                    )
                else:
                    self._roleObj = self.CLS_dat__type__typename(
                        self, _
                    )

    # **************************************************************************************************************** #
    def category(self):
        return self._categoryObj

    def categoryString(self):
        return self._categoryObj.toString()

    # **************************************************************************************************************** #
    def role(self):
        return self._roleObj

    def roleString(self):
        return self._roleObj.toString()

    # **************************************************************************************************************** #
    def name(self):
        return self._typenameObj

    def nameString(self):
        return self._typenameObj.toString()

    # **************************************************************************************************************** #
    def setRaw(self, *args):
        self._type__set_build_(*args)

    def raw(self):
        return self._typenameObj.raw()

    # **************************************************************************************************************** #
    def _type__get_raw_str_(self):
        return self._typenameObj.toString()

    def toString(self):
        return self._type__get_raw_str_()

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}.{}'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()

    # **************************************************************************************************************** #
    def __eq__(self, other):
        if isinstance(other, ItfDatType):
            return self.toString() == other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() == unicode(other)

    def __ne__(self, other):
        if isinstance(other, ItfDatType):
            return self.toString() != other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() != unicode(other)


# ******************************************************************************************************************** #
class ItfDatObjName(ItfDatObjKey):
    CLS_dat__obj_name__namespace = None
    CLS_dat__obj_name__name = None

    def _initItfDatObjName(self, *args):
        self._objname__set_build_(*args)

    # **************************************************************************************************************** #
    def _objname__set_build_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                sep = self.sep()
                _ = raw.split(sep)
                if len(_) == 1:
                    namespaceString = sep
                    nameString = _[0]
                else:
                    namespaceString = sep.join([i for i in _[:-1] if i])
                    if namespaceString == u'':
                        namespaceString = sep
                    nameString = _[-1]

                self._namespaceObj = self.CLS_dat__obj_name__namespace(namespaceString)
                self._nameObj = self.CLS_dat__obj_name__name(nameString)

    def _objname__get_raw_(self):
        sep = self.sep()
        if self.namespaceString() == sep:
            return self.nameString()
        return sep.join(
            [self.namespaceString(), self.nameString()]
        )

    def setRaw(self, *args):
        self._objname__set_build_(*args)

    def raw(self):
        return self._objname__get_raw_()

    # **************************************************************************************************************** #
    def hasNamespace(self):
        return self._namespaceObj is not None

    def namespace(self):
        return self._namespaceObj

    def setNamespace(self, *args):
        obj = args[0]
        self._namespaceObj = obj

    def setNamespaceString(self):
        pass

    def namespaceString(self):
        if self.hasNamespace():
            return self._namespaceObj.toString()

    # **************************************************************************************************************** #
    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    # **************************************************************************************************************** #
    def toString(self):
        return self._objname__get_raw_()

    # **************************************************************************************************************** #
    @classmethod
    def sep(cls):
        return cls.CLS_dat__obj_name__namespace.sep()

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}(raw="{}")'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()


# ******************************************************************************************************************** #
class ItfDatFilename(ItfDatObjKey):
    CLS_dat__filename__base = None
    CLS_dat__filename__ext = None

    VAR_dat__extsep = None

    def _initItfDatFilename(self, *args):
        self._file_name__set_create_by_raw_(*args)

    # **************************************************************************************************************** #
    def _file_name__set_create_by_raw_(self, *args):
        if args:
            raw = args[0]
            if raw is not None:
                sep = self.VAR_dat__extsep

                _ = raw.split(sep)
                if len(_) == 1:
                    baseString = _[0]
                    self._baseObj = self.CLS_dat__filename__base(baseString)
                    self._extObj = None
                else:
                    baseString = sep.join(_[:-1])
                    extString = sep + _[-1]
                    self._baseObj = self.CLS_dat__filename__base(baseString)
                    self._extObj = self.CLS_dat__filename__ext(extString)

    def _file_name__get_raw_(self):
        if self.hasExt():
            return self.baseString() + self.extString()
        return self.baseString()

    def setRaw(self, *args):
        self._file_name__set_create_by_raw_(*args)

    def raw(self):
        return self._file_name__get_raw_()

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
        return self._file_name__get_raw_()

    # **************************************************************************************************************** #
    @classmethod
    def extsep(cls):
        return cls.VAR_dat__extsep

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}(raw="{}")'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()


class ItfDatObjPath(ItfDatObjKey):
    CLS_dat__obj_path__name = None

    CLS_dat__obj_path__objsep = None

    def __init__(self, *args):
        pass

    def _initItfDatObjPath(self, *args):
        self._parentObj = None

        self._childObjDict = {}
        self._childObjList = []

        self._obj_path__set_create_by_raw_(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_path__set_strip_(cls, pathString, pathsep):
        def rcsFnc_(pathString_, pathsep_):
            if pathString_ == pathsep_:
                return pathsep_
            elif pathString_.endswith(pathsep_):
                return rcsFnc_(pathString_[:-len(pathsep_)], pathsep_)
            return pathString_
        return rcsFnc_(pathString, pathsep)

    def _obj_path__set_create_by_raw_(self, *args):
        sep = self.sep()
        if args:
            if len(args) == 1:
                raw = args[0]
                if raw is not None:
                    raw = self._obj_path__set_strip_(raw, sep)

                    if raw == sep:
                        self._parentObj = None
                        self._nameObj = self.CLS_dat__obj_path__name(sep)
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

                        self._nameObj = self.CLS_dat__obj_path__name(nameRaw)
                else:
                    self._nameObj = self.CLS_dat__obj_path__name(sep)
            #
            elif len(args) == 2:
                parentRaw, nameRaw = args
                if isinstance(parentRaw, ItfDatObjPath):
                    self._parentObj = parentRaw
                elif isinstance(parentRaw, (str, unicode)):
                    self._parentObj = self.__class__(parentRaw)

                if isinstance(nameRaw, ItfDatRaw):
                    self._nameObj = nameRaw
                elif isinstance(nameRaw, (str, unicode)):
                    self._nameObj = self.CLS_dat__obj_path__name(nameRaw)
            #
            if self._parentObj is not None:
                self._parentObj._obj_path__set_cache_child_update_(self)
        else:
            self._nameObj = self.CLS_dat__obj_path__name(sep)

    def _obj_path__get_raw_str_(self):
        sep = self.sep()
        # root
        if self._parentObj is None:
            return self.nameString()
        # in root
        elif self.parentString() == sep:
            return sep + self.nameString()
        return sep.join([self.parentString(), self.nameString()])

    def setRaw(self, *args):
        self._obj_path__set_create_by_raw_(*args)

    def raw(self):
        return self._obj_path__get_raw_str_()

    def setRawString(self, *args):
        self._obj_path__set_create_by_raw_(*args)

    # **************************************************************************************************************** #
    def _obj_path__set_cache_parent_update_(self, pathObject):
        if pathObject.parent() != self._parentObj:
            self._parentObj = pathObject

    def _obj_path__set_cache_child_update_(self, *args):
        pathObject = args[0]
        nameString = pathObject.nameString()
        if nameString not in self._childObjDict:
            self._childObjDict[nameString] = pathObject
            self._childObjList.append(pathObject)

    # **************************************************************************************************************** #
    def root(self):
        return self.CLS_dat__obj_path__name(
            self.CLS_dat__obj_path__objsep
        )

    # **************************************************************************************************************** #
    def _get_path_parent_obj_exist_(self, pathObject):
        return pathObject == self._parentObj

    def _get_path_parent_exist_(self, *args):
        if args:
            if isinstance(args[0], self.__class__):
                return self._get_path_parent_obj_exist_(
                    args[0]
                )
            elif isinstance(args[0], (str, unicode)):
                return self._get_path_parent_obj_exist_(
                    self.__class__(args[0])
                )
        return self._parentObj is not None

    def _obj_path__set_parent_(self, *args):
        if self._get_path_parent_exist_(*args) is False:
            if isinstance(args[0], ItfDatObjPath):
                self._obj_path__set_cache_parent_update_(args[0])
            elif isinstance(args[0], (str, unicode)):
                self._obj_path__set_cache_parent_update_(self.__class__(args[0]))

            parentRaw = args[0]
            if isinstance(parentRaw, self.__class__):
                self._parentObj = parentRaw
            elif isinstance(parentRaw, (str, unicode)):
                self._parentObj = self.__class__(parentRaw)
            elif parentRaw is None:
                self._parentObj = self.__class__(self.sep())

            self._parentObj._obj_path__set_cache_child_update_(self)

    def isParent(self):
        return self._obj_path__get_children_exist_()

    def hasParent(self, *args):
        return self._get_path_parent_exist_(*args)

    def setParent(self, *args):
        self._obj_path__set_parent_(*args)

    def parent(self):
        return self._parentObj

    def setParentString(self, *args):
        self._obj_path__set_parent_(*args)

    def parentString(self):
        if self._parentObj is not None:
            return self._parentObj.toString()

    # **************************************************************************************************************** #
    def _get_path_cache_child_name_obj_exist_(self, nameObject):
        return nameObject.toString() in self._childObjDict

    def _get_path_cache_child_obj_exist_(self, pathObject):
        return

    # **************************************************************************************************************** #
    def _obj_path__get_children_exist_(self):
        return self._childObjList != []

    def hasChildren(self):
        return self._obj_path__get_children_exist_()

    def children(self):
        return self._childObjList

    # **************************************************************************************************************** #
    def _obj_path__set_child_add_(self, *args):
        pathObject = args[0]
        pathObject._obj_path__set_cache_parent_update_(self)

    def addChild(self, *args):
        self._obj_path__set_child_add_(*args)

    def isChild(self):
        return self._get_path_parent_exist_()

    def _obj_path__get_child_exist_(self, *args):
        if args:
            if isinstance(args[0], ItfDatObjPath):
                pathObject = args[0]
                return self._get_path_cache_child_name_obj_exist_(
                    pathObject.name()
                )
            elif isinstance(args[0], (str, unicode)):
                pathObject = self.__class__(args[0])
                return self._get_path_cache_child_name_obj_exist_(
                    pathObject.name()
                )
        return self._get_path_parent_exist_()

    def hasChild(self, *args):
        return self._obj_path__get_child_exist_(*args)

    def child(self, *args):
        index = args[0]
        return self._childObjList[index]

    # **************************************************************************************************************** #
    def _obj_path__get_all_child_obj_list_(self):
        def rcsFnc_(pathObj_):
            childPathObjs = pathObj_.children()
            if childPathObjs:
                for pathObject in childPathObjs:
                    rcsFnc_(pathObject)
                    lis.append(pathObject)

        lis = []

        rcsFnc_(self)
        return lis

    def allChildren(self):
        return self._obj_path__get_all_child_obj_list_()

    # **************************************************************************************************************** #
    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def setNameString(self, *args):
        self._nameObj.setRaw(*args)

    # **************************************************************************************************************** #
    def isRoot(self):
        return self.nameString() == self.sep()

    # **************************************************************************************************************** #
    def toString(self):
        return self._obj_path__get_raw_str_()

    # **************************************************************************************************************** #
    @classmethod
    def sep(cls):
        return cls.CLS_dat__obj_path__objsep

    # **************************************************************************************************************** #
    def __str__(self):
        return u'{}(parent="{}", name="{}")'.format(
            self.__class__.__name__,
            self.parentString(),
            self.nameString()
        )

    def __repr__(self):
        return self.__str__()

    # **************************************************************************************************************** #
    def __eq__(self, other):
        if isinstance(other, ItfDatObjPath):
            return self.toString() == other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() == other
        return False

    def __ne__(self, other):
        if isinstance(other, ItfDatObjPath):
            return self.toString() != other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() != other
        return False


class ItfDatObjVariant(ItfDatObjPath):
    def _initItfDatObjVariant(self, *args):
        self._initItfDatObjPath(*args)


class ItfDatObjNamespace(ItfDatObjPath):
    def _initItfDatObjNamespace(self, *args):
        self._initItfDatObjPath(*args)


class ItfDatObjComppath(ItfDatObjKey):
    CLS_dat__comppath__nodepath = None
    CLS_dat__comppath__portpath = None

    def _initItfDatObjComppath(self, *args):
        self._set_obj_path_build_(*args)

    # **************************************************************************************************************** #
    def _set_obj_path_build_(self, *args):
        if args:
            # str( "nodepath.portpath" )
            if len(args) == 1:
                raw = args[0]
                if raw is not None:
                    nodesep = self.nodesep()
                    portsep = self.portsep()
                    _ = raw.split(portsep)

                    if len(_) == 1:
                        nodepathString = None
                        portpathString = _[-1]
                    else:
                        if nodesep != portsep:
                            nodepathString = _[0]
                            portpathString = portsep.join([i for i in _[1:]])
                        else:
                            nodepathString = portsep.join([i for i in _[:-1]])
                            portpathString = _[-1]

                    self._nodepathObj = self.CLS_dat__comppath__nodepath(nodepathString)
                    self._portpathObj = self.CLS_dat__comppath__portpath(portpathString)
            elif len(args) == 2:
                nodepathRaw, portpathRaw = args
                # *.objects.Nodepath() / str( "nodepath" )
                if isinstance(nodepathRaw, self.CLS_dat__comppath__nodepath):
                    self._nodepathObj = nodepathRaw
                elif isinstance(nodepathRaw, (str, unicode)):
                    self._nodepathObj = self.CLS_dat__comppath__nodepath(nodepathRaw)
                # objects.Portpath() / str( "portpath" )
                if isinstance(portpathRaw, self.CLS_dat__comppath__portpath):
                    self._portpathObj = portpathRaw
                elif isinstance(portpathRaw, (str, unicode)):
                    self._portpathObj = self.CLS_dat__comppath__portpath(portpathRaw)
            else:
                raise TypeError(
                    u'''???'''
                )

    def _get_attrpath_raw(self):
        portsep = self.portsep()
        return portsep.join(
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
    def setNodepath(self, obj):
        self._nodepathObj = obj

    def nodepath(self):
        return self._nodepathObj

    def nodepathString(self):
        return self._nodepathObj.toString()

    def nodename(self):
        return self._nodepathObj.name()

    def nodenameString(self):
        return self._nodepathObj.nameString()

    # **************************************************************************************************************** #
    def portpath(self):
        return self._portpathObj

    def portpathString(self):
        return self._portpathObj.toString()

    def portname(self):
        return self._portpathObj.name()

    def portnameString(self):
        return self._portpathObj.nameString()

    # **************************************************************************************************************** #
    def toString(self):
        return self._get_attrpath_raw()

    # **************************************************************************************************************** #
    @classmethod
    def nodesep(cls):
        return cls.CLS_dat__comppath__nodepath.sep()

    @classmethod
    def portsep(cls):
        return cls.CLS_dat__comppath__portpath.sep()

    @classmethod
    def sep(cls):
        return cls.CLS_dat__comppath__portpath.sep()

    # **************************************************************************************************************** #
    def __str__(self):
        return '{}(raw="{}")'.format(
            self.__class__.__name__,
            self.raw()
        )

    def __repr__(self):
        return self.__str__()
