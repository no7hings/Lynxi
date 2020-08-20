# coding:utf-8
from . import datCfg, datObjItf


class AbsDatRaw(datObjItf.ItfDatRaw):
    def _initAbsDatRaw(self, *args):
        self._initItfDatRaw(*args)


class AbsDatTypename(datObjItf.ItfDatTypename):
    def _initAbsDatTypename(self, *args):
        self._initItfDatTypename(*args)


class AbsDatDatatype(datObjItf.ItfDatType):
    def _initAbsDatDatatype(self, *args):
        self._initItfDatType(*args)


class AbsDatPorttype(datObjItf.ItfDatType):
    def _initAbsDatPorttype(self, *args):
        self._initItfDatType(*args)


class AbsDatName(datObjItf.ItfDatName):
    def _initAbsDatName(self, *args):
        self._initItfDatName(*args)


# object ************************************************************************************************************* #
class AbsDatObjName(datObjItf.ItfDatObjName):
    def _initAbsDatObjName(self, *args):
        self._initItfDatObjName(*args)


class AbsDatFilename(datObjItf.ItfDatFilename):
    def _initAbsDatFilename(self, *args):
        self._initItfDatFilename(*args)


class AbsDatObjPath(datObjItf.ItfDatObjPath):
    def _initAbsDatObjPath(self, *args):
        self._initItfDatObjPath(*args)


class AbsDatObjVariant(datObjItf.ItfDatObjVariant):
    def _initAbsDatObjVariant(self, *args):
        self._initItfDatObjVariant(*args)


class AbsDatObjNamespace(datObjItf.ItfDatObjNamespace):
    def _initAbsDatObjNamespace(self, *args):
        self._initItfDatObjNamespace(*args)

    def _obj_path__get_raw_str_(self):
        sep = self.sep()
        # root
        if self._parentObj is None:
            return self.nameString()
        # in root
        elif self.parentString() == sep:
            return self.nameString()
        return sep.join([self.parentString(), self.nameString()])


class AbsDatObjComppath(datObjItf.ItfDatObjComppath):
    def _initAbsDatObjComppath(self, *args):
        self._initItfDatObjComppath(*args)


# value ************************************************************************************************************** #
class AbsDatData(datObjItf.ItfDatRaw):
    CLS_dat__data__element = None

    VAR_dat__data__datasep = None

    def _initAbsDatData(self, *args):
        self._parentObj = args[0]
        rawArgs = args[1:]

        if isinstance(args[0], AbsDatValue):
            self._valueObj = self._parentObj

            self._rawtypePattern = self._valueObj.VAR_dat__value__rawtype_pattern
            self._rawtypeStrPattern = self._valueObj.VAR_dat__value__rawtype_str_pattern
            self._rawsizePattern = self._valueObj.VAR_dat__value__rawsize_pattern
        elif isinstance(args[0], AbsDatData):
            self._dataObj = self._parentObj

            if len(self._dataObj._rawtypePattern) == 2:
                self._rawtypePattern = self._dataObj._rawtypePattern[-1]
            else:
                self._rawtypePattern = self._dataObj._rawtypePattern[1:]

            if len(self._dataObj._rawtypeStrPattern) == 2:
                self._rawtypeStrPattern = self._dataObj._rawtypeStrPattern[-1]
            else:
                self._rawtypeStrPattern = self._dataObj._rawtypeStrPattern[1:]

            if len(self._dataObj._rawsizePattern) == 2:
                self._rawsizePattern = self._dataObj._rawsizePattern[-1]
            else:
                self._rawsizePattern = self._dataObj._rawsizePattern[1:]
        else:
            self._rawtypePattern = None
            self._rawtypeStrPattern = None
            self._rawsizePattern = None

        self._rawObj = None
        self._childDataObjList = []

        self._raw__set_create_(*rawArgs)

    @staticmethod
    def _fnc_get_list_split_(lis, splitCount):
        lis_ = []

        count = len(lis)
        cutCount = int(count / splitCount)
        for i in range(cutCount + 1):
            subLis = lis[i*splitCount:min((i + 1)*splitCount, count)]
            if subLis:
                if len(subLis) == 1:
                    lis_.append(subLis[0])
                else:
                    lis_.append(subLis)
        return lis_

    def _raw__get_rawtype_str_(self):
        if self._rawtypeStrPattern is not None:
            if isinstance(self._rawtypeStrPattern, (tuple, list)):
                return self._rawtypeStrPattern[0]
            return self._rawtypeStrPattern

    def clear(self):
        self._childDataObjList = []

    def rawsize(self):
        """
        :return: int
        """
        if self._data__get_is_comp_():
            return self._rawsizePattern[0]
        return self._rawsizePattern

    # element ********************************************************************************************************** #
    def addElement(self, dataObj):
        """
        :param dataObj: object of Data
        :return: None
        """
        self._childDataObjList.append(dataObj)

    def hasElements(self):
        """
        :return: bool
        """
        return self._childDataObjList != []

    def elements(self):
        """
        :return: list(object of Data)
        """
        return self._childDataObjList

    def elementCount(self):
        """
        :return: int
        """
        return len(self._childDataObjList)

    def element(self, *args):
        if isinstance(args[0], (int, float)):
            return self._childDataObjList[int(args[0])]

    def elementAt(self, index):
        """
        :param index: object of Data
        :return:
        """
        return self.elements()[index]

    def elementRawtype(self):
        """
        :return: class of raw
        """
        return self._rawtypePattern[1]

    def elementRawsize(self):
        """
        :return: int
        """
        return self._rawsizePattern[1]

    def _data__get_is_comp_(self):
        return isinstance(self._rawtypePattern, (tuple, list))

    # raw ************************************************************************************************************ #
    def _raw__get_raw_cls_(self):
        if self._rawtypePattern is not None:
            if isinstance(self._rawtypePattern, (tuple, list)):
                return self._rawtypePattern[0]
            return self._rawtypePattern
        return self.CLS_dat__raw

    def _raw__get_obj_by_raw(self, raw):
        cls = self._raw__get_raw_cls_()
        if cls is not None:
            return cls(raw)

    def _set_compraw_to_rawobj_(self, *args):
        raw = args[0]
        self.clear()

        [self.addElement(self.CLS_dat__data__element(self, i)) for i in raw]
        cls = self._raw__get_raw_cls_()
        if cls is not None:
            return cls([i.raw() for i in self.elements()])

    def _raw__set_create_by_raw_(self, *args):
        if args:
            _ = args[0]
            if self._data__get_is_comp_() is True:
                if isinstance(_, (tuple, list)):
                    if len(args) == 1:
                        compraw = _
                    else:
                        if self.elementRawtype() in (tuple, list):
                            if len(_) == self.elementRawsize():
                                compraw = args
                            else:
                                raise ValueError("value format is error")
                        else:
                            compraw = args
                else:
                    compraw = args

                if isinstance(self.rawsize(), int):
                    compraw = compraw[:self.rawsize()]

                self._rawObj = self._set_compraw_to_rawobj_(compraw)
            else:
                raw = _
                if raw is not None:
                    self._raw__set_raw_val_(raw)

                    self._rawObj = self._raw__get_obj_by_raw(raw)

    def _data__get_compraw_(self):
        cls = self._raw__get_raw_cls_()
        if cls is not None:
            return cls([i._raw__get_raw_() for i in self.elements()])

    def _raw__get_raw_(self):
        if self._data__get_is_comp_():
            return self._data__get_compraw_()
        return self._rawObj

    # rawstr ********************************************************************************************************* #
    def _raw__get_raw_by_str(self, rawString):
        if self.CLS_dat__raw is not None:
            return self.CLS_dat__raw(rawString)

    def _set_comprawstr_to_rawobj_(self, *args):
        rawstr = args[0]
        self.clear()
        [self.addElement(self.CLS_dat__data__element(self, i)) for i in rawstr]
        cls = self._raw__get_raw_cls_()
        if cls is not None:
            return cls([i.raw() for i in self.elements()])

    def _raw__set_create_by_str_(self, *args):
        if args:
            rawstr = args[0]
            if rawstr is not None:
                self._raw__set_str_val_(rawstr)
                if self._data__get_is_comp_():
                    valueStringLis = [i.lstrip().rstrip() for i in args[0].split(self.VAR_dat__data__datasep)]
                    rawstr = self._fnc_get_list_split_(valueStringLis, self.elementRawsize())
                    self._rawObj = self._set_comprawstr_to_rawobj_(rawstr)
                else:
                    self._rawObj = self._raw__get_raw_by_str(rawstr)

    def _get_comprawstr_(self):
        return self.VAR_dat__data__datasep.join(
            [i._raw__get_str_() for i in self.elements()]
        )

    def _raw__get_str_(self):
        if self._data__get_is_comp_():
            return self._get_comprawstr_()

        if self._rawObj is not None:
            return unicode(self._rawObj)
        return u''

    # create ********************************************************************************************************* #
    def _raw__set_create_(self, *args):
        if self._data__get_is_comp_():
            if len(args) > 1:
                self._raw__set_create_by_raw_(*args)
            else:
                if isinstance(args[0], (str, unicode)):
                    self._raw__set_create_by_str_(*args)
                else:
                    self._raw__set_create_by_raw_(*args)
        else:
            if isinstance(args[0], (str, unicode)):
                self._raw__set_create_by_str_(*args)
            else:
                self._raw__set_create_by_raw_(*args)

    @classmethod
    def datasep(cls):
        return cls.VAR_dat__data__datasep

    def __len__(self):
        return self.elementCount()


class AbsDatValue(datCfg.DatUtility):
    CLS_dat__value__datatype = None
    CLS_dat__value__data = None

    VAR_dat__value__rawtype_str_pattern = None
    VAR_dat__value__rawtype_pattern = None
    VAR_dat__value__rawsize_pattern = None

    def _initAbsDatValue(self, *args):
        self._value__set_build_(*args)

    def _value__set_build_(self, *args):
        # datatype
        self._value__set_datatype_build_(self.VAR_dat__value__rawtype_str_pattern)
        # data
        self._dataKeyStrList = []
        self._dataObjList = []
        #
        self._value__set_data_build_(*args)
        self._value__set_default_data_build_(self._dataObj)

    def _value__set_datatype_build_(self, *args):
        _ = args[0]
        if isinstance(_, (tuple, list)):
            self._nodeDatatypeObj = self.CLS_dat__value__datatype(_[0])
        else:
            self._nodeDatatypeObj = self.CLS_dat__value__datatype(_)

    def _value__set_data_build_(self, *args):
        if isinstance(args[0], AbsDatData):
            self._dataObj = args[0]
        else:
            self._dataObj = self.CLS_dat__value__data(
                self, *args
            )

    def _value__set_default_data_build_(self, *args):
        if isinstance(args[0], AbsDatData):
            self._defaultDataObj = self.MOD_copy.deepcopy(
                args[0]
            )
        else:
            self._defaultDataObj = self.CLS_dat__value__data(
                self, *args
            )

    def datatype(self):
        """
        :return: *objects.Datatype
        """
        return self._nodeDatatypeObj

    def datatypeString(self):
        """
        :return: str
        """
        return self._nodeDatatypeObj.toString()

    # **************************************************************************************************************** #
    def data(self):
        """
        :return: *objects.Data
        """
        return self._dataObj

    def dataString(self):
        return self._dataObj.toString()

    # **************************************************************************************************************** #
    def defaultData(self):
        return self._defaultDataObj

    def defaultDataString(self):
        return self._defaultDataObj.toString()

    # **************************************************************************************************************** #
    def isDataChanged(self):
        return self._dataObj != self._defaultDataObj

    # **************************************************************************************************************** #
    def setRaw(self, *args, **kwargs):
        if kwargs:
            pass
        self._dataObj.setRaw(*args)

    def hasRaw(self):
        """
        :return: bool
        """
        return self._dataObj.hasRaw()

    def raw(self):
        """
        :return: raw of typed
        """
        return self._dataObj.raw()

    # **************************************************************************************************************** #
    def setRawString(self, *args):
        self._dataObj.setRawString(*args)

    def rawString(self):
        return self._dataObj.toString()

    # **************************************************************************************************************** #
    def toString(self):
        """
        :return: str
        """
        return self._dataObj.toString()

    # **************************************************************************************************************** #
    @classmethod
    def typePattern(cls):
        return cls.VAR_dat__value__rawtype_pattern

    @classmethod
    def sizePattern(cls):
        return cls.VAR_dat__value__rawsize_pattern

    def covertTo(self, dataType):
        pass

    # **************************************************************************************************************** #
    def __eq__(self, other):
        """
        :param other: object of Value
        :return: bool
        """
        return self.data() == other.data()

    def __ne__(self, other):
        """
        :param other: object of Value
        :return: bool
        """
        return self.data() != other.data()


# xml document ******************************************************************************************************* #
class AbsDatXmlObj(object):
    VAR_dat__xml_obj__attribute_separator = u' '

    VAR_dat__xml_obj__element_prefix_str = u''
    VAR_dat__xml_obj__attribute_attach_str = u''

    def _initAbsDatXmlObj(self):
        self._xmlPrefixStr = u''

        self._xmlNamePrefixString = None
        self._xmlNameSuffixString = None

    # **************************************************************************************************************** #
    def _xml_obj__get_left_indent_str_(self):
        return self._xmlPrefixStr

    def _xml_obj__set_left_indent_str_(self, string):
        self._xmlPrefixStr = string

    # **************************************************************************************************************** #
    def _xml_obj__get_element_prefix_str(self):
        return self.VAR_dat__xml_obj__element_prefix_str

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_attach_key_str_(self):
        return self.VAR_dat__xml_obj__attribute_attach_str

    def _xml_obj__get_attribute_attach_value_str_(self):
        pass

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_attach_list_(self):
        pass

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_list_(self):
        pass

    # **************************************************************************************************************** #
    def _xml_obj__get_sibling_element_list_(self):
        pass

    # **************************************************************************************************************** #
    def _xml_obj__get_child_element_list_(self):
        pass

    @classmethod
    def _xml_obj_cls__get_str_(cls, elementObj, indent=4):
        def addPrefixFnc_(lis_, prefixStr_, lStr_, rStr_):
            lis_.append(u'{}<{}{}'.format(lStr_, prefixStr_, rStr_))

        def addAttributeFnc_(lis_, attributeArg_, lStr_, rStr_):
            if attributeArg_ is not None:
                if isinstance(attributeArg_, AbsDatXmlObj):
                    # noinspection PyNoneFunctionAssignment
                    _attributeRaw = attributeArg_._xml_obj__get_attribute_attach_list_()
                else:
                    _attributeRaw = attributeArg_

                if isinstance(_attributeRaw, (tuple, list)):
                    if _attributeRaw:
                        for _i in _attributeRaw:
                            if isinstance(_i, AbsDatXmlObj):
                                addAttributeFnc_(lis_, _i, lStr_, rStr_)
                            else:
                                k, v = _i
                                if v:
                                    lis_.append(
                                        u'{}{}="{}"{}'.format(lStr_, k, v, rStr_)
                                    )

        def addElementFnc_(lis_, elementObj_, rStr_, parentElementObj_=None):
            if parentElementObj_ is not None:
                _lStr = elementObj_._xml_obj__get_left_indent_str_()
            else:
                _lStr = u''

            _prefixStr = elementObj_._xml_obj__get_element_prefix_str()
            addPrefixFnc_(lis_, _prefixStr, lStr_=_lStr, rStr_=u'')
            # Attribute
            _attributeList = elementObj_._xml_obj__get_attribute_list_()
            if _attributeList:
                [addAttributeFnc_(lis_, _i, lStr_=cls.VAR_dat__xml_obj__attribute_separator, rStr_=u'') for _i in _attributeList]
            # Child Element
            _childElementList = elementObj_._xml_obj__get_child_element_list_()
            if _childElementList:
                lis.append(u'>{}'.format(linefeedStr))

                for _i in _childElementList:
                    if _i is not None:
                        _i._xml_obj__set_left_indent_str_(_lStr + defIndentStr)
                        addElementFnc_(lis_, _i, rStr_=rStr_, parentElementObj_=elementObj_)

                lis.append(u'{}</{}>{}'.format(_lStr, _prefixStr, linefeedStr))
            else:
                lis.append(u'{}/>{}'.format(cls.VAR_dat__xml_obj__attribute_separator, linefeedStr))
            # Sibling Element
            _siblingElementList = elementObj_._xml_obj__get_sibling_element_list_()
            if _siblingElementList:
                for _i in _siblingElementList:
                    _i._xml_obj__set_left_indent_str_(_lStr)
                    addElementFnc_(lis_, _i, rStr_=u'', parentElementObj_=elementObj_)

        linefeedStr = '\r\n'
        defIndentStr = u' ' * indent

        lis = [
            u'<?xml version="1.0"?>{}'.format(linefeedStr),
        ]

        addElementFnc_(lis, elementObj, rStr_=u'')
        return u''.join(lis)

    def __str__(self):
        return self._xml_obj_cls__get_str_(self)

    def __repr__(self):
        return self._xml_obj_cls__get_str_(self)
