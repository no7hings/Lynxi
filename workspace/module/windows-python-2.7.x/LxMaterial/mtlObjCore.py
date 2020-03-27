# coding:utf-8
from LxBasic import bscMethods

from LxMaterial import mtlConfigure, mtlObjDef, mtlMethods


class Def_XmlObject(mtlConfigure.Utility):
    DEF_mtl_file_attribute_separator = u' '

    VAR_mtl_file_element_key = u''
    VAR_mtl_file_attribute_attach_key = u''

    def _initDefMtlObject(self):
        self._xmlIndentStr = ''

        self._xmlNameSuffixString = None

    def _xmlElementString_(self):
        return self.VAR_mtl_file_element_key

    def _xmlNameSuffixString_(self):
        return self._xmlNameSuffixString

    def _setXmlNameSuffixString_(self, string):
        self._xmlNameSuffixString = string

    def _xmlAttributeAttachKeyString_(self):
        return self.VAR_mtl_file_attribute_attach_key

    def _xmlAttributeAttachValueString_(self):
        pass

    @property
    def _xmlIndent_(self):
        return self._xmlIndentStr

    @_xmlIndent_.setter
    def _xmlIndent_(self, string):
        self._xmlIndentStr = string

    def _xmlAttributes_(self):
        pass

    def _xmlChildren_(self):
        pass

    def _xmlElements_(self):
        pass

    def _xmlAttributeAttaches_(self):
        """
        :return: list(tuple(key, value)/object instance of Def_XmlObject, ...)
        """
        pass

    @classmethod
    def _toXmlString(cls, elementObject, indent=4):
        def addPrefixFnc_(prefix_, lString, rString):
            lis.append(u'{}<{}{}'.format(lString, prefix_, rString))

        def addAttributeFnc_(attributeObject_, lString, rString):
            if attributeObject_ is not None:
                if isinstance(attributeObject_, Def_XmlObject):
                    attributeRaw = attributeObject_._xmlAttributeAttaches_()
                else:
                    attributeRaw = attributeObject_

                if attributeRaw:
                    for i in attributeRaw:
                        if isinstance(i, Def_XmlObject):
                            addAttributeFnc_(i, lString, rString)
                        else:
                            k, v = i
                            if v:
                                lis.append(u'{}{}="{}"{}'.format(lString, k, v, rString))

        def addBranchFnc_(elementObject_, rString, parentElementObject=None):
            if parentElementObject is not None:
                lString = elementObject_._xmlIndent_
            else:
                lString = u''

            tagString = elementObject_._xmlElementString_()
            addPrefixFnc_(tagString, lString=lString, rString=u'')
            # Attribute
            attributes = elementObject_._xmlAttributes_()
            if attributes:
                [addAttributeFnc_(i, lString=cls.DEF_mtl_file_attribute_separator, rString=u'') for i in attributes]
            # Children
            children = elementObject_._xmlChildren_()
            if children:
                lis.append(u'>\r\n')

                for i in children:
                    if i is not None:
                        i._xmlIndent_ = lString + defIndentString
                        addBranchFnc_(i, rString=rString, parentElementObject=elementObject_)

                lis.append(u'{}</{}>\r\n'.format(lString, tagString))
            else:
                lis.append(u'{}/>\r\n'.format(cls.DEF_mtl_file_attribute_separator))

            elements = elementObject_._xmlElements_()
            if elements:
                for i in elements:
                    i._xmlIndent_ = lString
                    addBranchFnc_(i, rString=u'', parentElementObject=elementObject_)

        defIndentString = u' ' * indent
        lis = [
            u'<?xml version="1.0"?>\r\n',
        ]

        addBranchFnc_(elementObject, rString='')
        return u''.join(lis)

    def __str__(self):
        return self._toXmlString(self)

    def __repr__(self):
        return self._toXmlString(self)


# raw **************************************************************************************************************** #
class Abc_MtlRaw(Def_XmlObject):
    def _initAbcMtlRaw(self, *args):
        if args:
            self._raw = args[0]
            self._rawType = type(self._raw)
        else:
            self._raw = None
            self._rawType = None

        self._initDefMtlObject()

    def _set_raw_(self, *args):
        pass

    def _set_raw_string_(self, *args):
        """
        :param args: raw string
        :return: None
        """
        pass

    def _set_raw_type_(self, typeString):
        """
        :param typeString: str
        :return: None
        """
        self._rawType = typeString

    def rawtype(self):
        """
        :return: str
        """
        return self._rawType

    def raw(self):
        """
        :return: raw of typed
        """
        return self._raw

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
        pass

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
    def _xmlAttributes_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xmlAttributeAttachValueString_(self):
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abc_MtlString(Abc_MtlRaw):
    def Abc_initAbcMtlString(self, *args):
        self._initAbcMtlRaw(*args)

    def toString(self):
        """
        :return: str
        """
        return unicode(self._raw)

    def _set_raw_string_(self, *args):
        self._raw = unicode(args[0])

    def _xmlAttributeAttachValueString_(self):
        if self._xmlNameSuffixString_() is not None:
            return '{}{}'.format(self.toString(), self._xmlNameSuffixString_())
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abc_MtlPath(Abc_MtlRaw):
    CLS_bsc_raw = None

    VAR_bsc_pathsep = None

    def _initAbcMtlPath(self, *args):
        self._initAbcMtlRaw(*args)

        if self.hasRaw():
            self._rawObjList = [self.CLS_bsc_raw(i) for i in self._raw.split(self.VAR_bsc_pathsep)]
        else:
            self._rawObjList = None

    @staticmethod
    def _toStringsMethod(pathString, pathsep):
        if pathString.startswith(pathsep):
            return pathString.split(pathsep)[1:]
        else:
            return pathString.split(pathsep)

    def _set_raw_(self, *args):
        raw = args[0]
        self._rawObjList = [self.CLS_bsc_raw(i) for i in raw.split(self.VAR_bsc_pathsep)]

    def _set_raw_string_(self, *args):
        self._set_raw_(*args)

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._rawObjList[-1].setRaw(nameString)

    def name(self):
        if self.hasRaw():
            return self._rawObjList[-1]

    def nameString(self):
        """
        :return: str
        """
        if self.hasRaw():
            return self.name().raw()
    
    def nodepathString(self):
        return self.toString()

    def toString(self):
        """
        :return: str
        """
        return self.VAR_bsc_pathsep.join([i.toString() for i in self._rawObjList])

    def pathsep(self):
        """
        :return: str
        """
        return self.VAR_bsc_pathsep

    def _xmlAttributeAttachValueString_(self):
        if self._xmlNameSuffixString_() is not None:
            return '{}{}'.format(self.toString(), self._xmlNameSuffixString_())
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abc_MtlNodeName(Abc_MtlPath):
    def _initAbcMtlNodeName(self, *args):
        self._initAbcMtlPath(*args)

    def nodepathString(self):
        return self.toString()


class Abc_MtlMaterialName(Abc_MtlNodeName):
    def _initAbcMtlMaterialName(self, *args):
        self._initAbcMtlNodeName(*args)


class Abc_MtlPortName(Abc_MtlPath):
    def _initAbcMtlPortName(self, *args):
        self._initAbcMtlPath(*args)

    def portpathString(self):
        return self.toString()


class Abc_MtlFileName(Abc_MtlPath):
    def _initAbcMtlFileName(self, *args):
        self._initAbcMtlPath(*args)


class Abc_MtlObjectSet(Def_XmlObject):
    VAR_grh_objectsep = u','

    # noinspection PyUnusedLocal
    def _initAbcMtlObjectSet(self, *args):
        if args:
            self._nameString = args[0]
        else:
            self._nameString = 'unknown'

        self._objectList = []
        self._objectFilterDict = {}

        self._objectCount = 0

        self._initDefMtlObject()

    def _initializeData_(self):
        self._objectList = []
        self._objectFilterDict = {}

        self._objectCount = 0

    def _set_add_obj_(self, *args):
        if len(args) == 2:
            keyString, obj = args
        else:
            obj = args[0]
            keyString = obj._queryKeyString_()

        if not keyString in self._objectFilterDict:
            self._objectList.append(obj)
            self._objectFilterDict[keyString] = obj
            self._objectCount += 1

    def _get_has_obj_(self, *args):
        if isinstance(args[0], (str, unicode)):
            keyString = args[0]
            return keyString in self._objectFilterDict
        elif isinstance(args[0], int):
            index = args[0]
            return 0 <= index <= (self._objectCount - 1)
        else:
            obj = args[0]
            keyString = obj._queryKeyString_()
            return keyString in self._objectFilterDict

    def _get_object_(self, *args):
        if isinstance(args[0], (str, unicode)):
            keyString = args[0]
            return self._objectFilterDict[keyString]
        elif isinstance(args[0], int):
            index = args[0]
            return self._objectList[index]

    def addObject(self, obj):
        keyString = obj._queryKeyString_()
        assert keyString not in self._objectFilterDict, u'''{}({})'s object "{}" is Exist.'''.format(
            self.__class__.__name__, self._nameString, keyString
        )
        self._set_add_obj_(obj)

    def hasObjects(self):
        """
        :return: bool
        """
        return self._objectList != []

    def objects(self):
        """
        :return: list(object, ...)
        """
        return self._objectList

    def hasObject(self, keyString):
        """
        :param keyString: str
        :return: bool
        """
        return self._get_has_obj_(keyString)

    def object(self, keyString):
        """
        :param keyString: str
        :return: object
        """
        assert keyString in self._objectFilterDict, u'''{}({})'s object "{}" is Unregistered.'''.format(
            self.__class__.__name__, self._nameString, keyString
        )
        return self._get_object_(keyString)

    def objectCount(self):
        """
        :return: int
        """
        return self._objectCount

    def objectAt(self, index):
        """
        :param index: int
        :return: object
        """
        return self._get_object_(index)

    def hasObjectAt(self, index):
        """
        :param index: int
        :return: object
        """
        return self._get_has_obj_(index)

    def toString(self):
        """
        :return: str
        """
        return self.VAR_grh_objectsep.join([i.toString() for i in self.objects()])

    def _xmlAttributeAttachValueString_(self):
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]

    def __len__(self):
        """
        :return: int
        """
        return self.objectCount()


# data & value ******************************************************************************************************* #
class Abc_MtlData(Abc_MtlRaw):
    CLS_bsc_raw = None

    VAR_mtl_raw_type = None

    def _initAbcMtlData(self, *args):
        self._initAbcMtlRaw()

        if isinstance(args[0], Abc_MtlValue):
            self._valueObj = args[0]
            self._valueTypeStringPattern = self._valueObj.VAR_mtl_value_type_pattern
            self._valueSizePattern = self._valueObj.VAR_mtl_value_size_pattern
        elif isinstance(args[0], Abc_MtlMultidata):
            self._datumNObj = args[0]
            self._valueTypeStringPattern = self._datumNObj._valueTypeStringPattern[1:]
            self._valueSizePattern = self._datumNObj._valueSizePattern[1:]

        self.create(*args[1:])

    def create(self, *args):
        """
        :param args: 
            1.raw of typed
            2.str
        :return: None
        """
        assert args is not (), u'argument must not be "empty".'

        if isinstance(args[0], (str, unicode)):
            self._set_raw_string_(*args)
        else:
            self._set_raw_(*args)

    def _set_raw_(self, *args):
        """
        :param args: raw of typed
        :return: None
        """
        assert args is not (), u'argument must not be "empty".'
        raw = args[0]
        if self.VAR_mtl_raw_type is not None:
            assert isinstance(raw, self.VAR_mtl_raw_type), u'[ Argument Error ], "arg" Must "{}".'.format(self.VAR_mtl_raw_type)
            self.setRaw(
                self.CLS_bsc_raw(raw)
            )

    def _set_raw_string_(self, *args):
        """
        :param args: str
        :return: None
        """
        assert args is not (), u'argument must not be "empty".'
        assert isinstance(args[0], (str, unicode))
        if args[0] is not None:
            self._set_raw_(self._stringToRaw_(args[0]))

    def _stringToRaw_(self, string):
        return self.CLS_bsc_raw(string)

    def toString(self):
        if self.CLS_bsc_raw is float:
            if self._raw == 0:
                return '0.0'
            return unicode(self._raw)
        return unicode(self._raw)

    def typeString(self):
        return self._valueTypeStringPattern[0]

    def valueSize(self):
        return self._valueSizePattern[0]

    def _toPrintString(self):
        if self.typeString() is not None:
            return '{}({})'.format(self.typeString(), self.toString())
        return self.toString()

    def _xmlAttributeAttachValueString_(self):
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abc_MtlMultidata(Abc_MtlRaw):
    CLS_mtl_data = None

    VAR_mtl_data_separator = None

    def _initAbcMtlMultidata(self, *args):
        self._initAbcMtlRaw()

        if isinstance(args[0], Abc_MtlValue):
            self._valueObj = args[0]
            self._valueTypeStringPattern = self._valueObj.VAR_mtl_value_type_pattern
            self._valueSizePattern = self._valueObj.VAR_mtl_value_size_pattern
        elif isinstance(args[0], Abc_MtlMultidata):
            self._datumNObj = args[0]
            self._valueTypeStringPattern = self._datumNObj._valueTypeStringPattern[1:]
            self._valueSizePattern = self._datumNObj._valueSizePattern[1:]

        self._childLis = []
        self.create(*args[1:])

    @staticmethod
    def _fnc_get_list_split_(lis, splitCount):
        lis_ = []

        count = len(lis)
        cutCount = int(count / splitCount)
        for i in range(cutCount + 1):
            subLis = lis[i * splitCount:min((i + 1) * splitCount, count)]
            if subLis:
                if len(subLis) == 1:
                    lis_.append(subLis[0])
                else:
                    lis_.append(subLis)
        return lis_

    def create(self, *args):
        assert args is not (), u'argument must not be "empty".'

        if isinstance(args[0], (str, unicode)):
            self._set_raw_string_(*args)
        else:
            self._set_raw_(*args)

    def _set_raw_(self, *args):
        """
        :param args:
            1.list(raw of typed, ...);
            2.raw of typed, ...
        :return: None
        """
        assert args is not (), u'argument must not be "empty".'
        if isinstance(args[0], (tuple, list)):
            raw = list(args[0])
        else:
            raw = args

        if isinstance(self.valueSize(), int):
            raw = raw[:self.valueSize()]

        self.clear()
        [self.addChild(self.CLS_mtl_data(self, i)) for i in raw]

        self.setRaw(raw)

    def _set_raw_string_(self, *args):
        assert args is not (), u'argument must not be "empty".'
        assert isinstance(args[0], (str, unicode))
        if args[0]:
            valueStringLis = [i.lstrip().rstrip() for i in args[0].split(mtlConfigure.Utility.DEF_mtl_data_separator)]
            raw = self._fnc_get_list_split_(valueStringLis, self.childValueSize())
            self._set_raw_(raw)

    def toString(self):  # to override
        """
        :return: str
        """
        return self.VAR_mtl_data_separator.join([i.toString() for i in self.children()])

    def typeString(self):
        """
        :return: str
        """
        return self._valueTypeStringPattern[0]

    def valueSize(self):
        """
        :return: int
        """
        return self._valueSizePattern[0]

    def childValueSize(self):
        """
        :return: int
        """
        return self._valueSizePattern[1]

    def clear(self):
        self._childLis = []

    def addChild(self, datumObject):
        """
        :param datumObject: object of Data
        :return: None
        """
        self._childLis.append(datumObject)

    def children(self):
        """
        :return: list(object of Data)
        """
        return self._childLis

    def childrenCount(self):
        """
        :return: int
        """
        return len(self._childLis)

    def hasChildren(self):
        """
        :return: bool
        """
        return self._childLis != []

    def childAt(self, index):
        """
        :param index: object of Data
        :return:
        """
        return self.children()[index]

    def raw(self):
        """
        :return: list(raw of typed, ...)
        """
        return [i.raw() for i in self.children()]

    def _toPrintString(self):
        if self.typeString() is not None:
            return '{}({})'.format(self.typeString(), self.VAR_mtl_data_separator.join([i._toPrintString() for i in self.children()]))
        return self.VAR_mtl_data_separator.join([i._toPrintString() for i in self.children()])

    def _xmlAttributeAttachValueString_(self):
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]

    def __len__(self):
        """
        :return: int
        """
        return self.childrenCount()


class Abc_MtlValue(Def_XmlObject):
    CLS_mtl_datatype = None
    CLS_mtl_raw_data = None

    VAR_mtl_value_type_pattern = None
    VAR_mtl_value_size_pattern = None

    def _initAbcMtlValue(self, *args):
        self._datatypeObj = self.CLS_mtl_datatype(self.VAR_mtl_value_type_pattern[0])
        self._dataObj = self.CLS_mtl_raw_data(self, *args)

        self._initDefMtlObject()

    def datatype(self):
        """
        :return: object of Type
        """
        return self._datatypeObj

    def porttypeString(self):
        """
        :return: str
        """
        return self._datatypeObj.toString()

    def data(self):
        """
        :return: object of Data
        """
        return self._dataObj

    def setRaw(self, *args):
        self._dataObj._set_raw_(*args)

    def setRawString(self, *args):
        self._dataObj._set_raw_string_(*args)

    def raw(self):
        """
        :return: raw of typed
        """
        return self._dataObj.raw()

    def hasRaw(self):
        """
        :return: bool
        """
        return self._dataObj.hasRaw()

    def toString(self):
        """
        :return: str
        """
        return self._dataObj.toString()

    def _xmlAttributes_(self):
        return [
            self.datatype(), self.data()
        ]

    def _xmlAttributeAttachValueString_(self):
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]

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


# port *************************************************************************************************************** #
class Abc_MtlPort(
    Def_XmlObject,
    mtlObjDef.Def_XmlCacheObj
):
    CLS_grh_porttype = None
    CLS_grh_portpath = None

    def _initAbcMtlPort(self, *args):
        nodeObject, portpathString = args[:2]

        self._nodeObj = nodeObject
        self._nodepathObj = nodeObject.nodepath()

        self._portpathObj = self.CLS_grh_portpath(portpathString)

        # value
        self._valueObj = None
        self._defValueObj = None
        # source
        self._sourcePortIndex = None
        # target
        self._targetPortIndexList = []

        self._porttypeString = None

        self._parentPortpathStr = None
        self._childPortpathStrList = []

        self._initDefMtlObject()
        self._initDefMtlCacheObj(self.attrpathString())

        self._proxyObj = None

        self._assignString = None

    def _qry_index_(self, *args):
        return self._nodeObj.OBJ_mtl_obj_cache._get_index_(*args)

    def _qry_object_(self, index):
        return self._nodeObj.OBJ_mtl_obj_cache._get_object_(index)

    def _setProxy_(self, obj):
        self._proxyObj = obj

    def _set_porttype_(self, porttypeString):
        self._porttypeObj = self.CLS_grh_porttype(porttypeString)
        self._porttypeString = porttypeString

    def _setAssign_(self, assignString):
        self._assignString = assignString

    def _set_parent_(self, portnameString):
        self._parentPortpathStr = portnameString

    def _set_children_(self, portnameStrings):
        self._childPortpathStrList = portnameStrings

    def _set_raw_(self, *args):
        pass

    def node(self):
        return self._nodeObj

    def portpath(self):
        return self._portpathObj

    def attrpathString(self):
        return self._portpathObj.pathsep().join(
            [self._nodepathObj.nodepathString(), self._portpathObj.portpathString()]
        )

    def portpathString(self):
        return self._portpathObj.portpathString()

    def portname(self):
        return self._portpathObj.name()

    def portnameString(self):
        return self._portpathObj.nameString()

    def _setValue_(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._valueObj = valueObject

    def _setDefaultValue_(self, valueObject):
        self._defValueObj = valueObject

    def porttype(self):
        return self._porttypeObj

    def porttypeString(self):
        return self._porttypeObj.toString()

    def setValue(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._setValue_(valueObject)

    def value(self):
        """
        :return: object of Value
        """
        return self._valueObj

    def hasValue(self):
        """
        :return: bool
        """
        return self._valueObj is not None

    def valueTypeString(self):
        return self._valueObj.porttypeString()

    def portdataString(self):
        return self._valueObj.toString()

    def setPortdata(self, raw):
        self._valueObj.setRaw(raw)

    def setPortdataString(self, rawString):
        self._valueObj.setRawString(rawString)

    def defaultValue(self):
        """
        :return: object of Value
        """
        return self._defValueObj

    def hasDefaultValue(self):
        """
        :return: bool
        """
        return self._defValueObj is not None

    def isValueChanged(self):
        """
        :return: bool
        """
        return not self.value() == self.defaultValue()

    def isChanged(self):
        if self.isChannel() is True:
            return self.hasSource()
        return self.isValueChanged() or self.hasSource()

    def _isSourcePort_(self, portObject):
        return self._qry_index_(portObject) == self._sourcePortIndex
    # source
    def _setSourcePort_(self, portObject):
        if self._isSourcePort_(portObject) is False:
            self._sourcePortIndex = self._qry_index_(portObject)
            portObject._addTargetPort_(self)

    def connectFrom(self, portObject):
        assert isinstance(portObject, Abc_MtlOutput), u'''Argument "portObject" must type of "Output"'''
        self._setSourcePort_(portObject)

    def hasSource(self):
        return self._sourcePortIndex is not None

    def source(self):
        """
        :return: object of Output
        """
        if self.hasSource():
            return self._nodeObj.OBJ_mtl_obj_cache._get_object_(
                self._sourcePortIndex
            )

    def isConnectedFrom(self, portObject):
        return self._isSourcePort_(portObject)

    def _createTargetPort_(self, *args):
        pass

    def _hasTargetPort_(self, portObject):
        return self._qry_index_(portObject) in self._targetPortIndexList

    # target
    def _addTargetPort_(self, *args):
        portObject = args[0]
        index = self._qry_index_(portObject)
        if portObject.hasSource():
            sourceObject = portObject.source()

            if index in sourceObject._targetPortIndexList:
                sourceObject._targetPortIndexList.remove(index)

        if index not in self._targetPortIndexList:
            self._targetPortIndexList.append(index)
            portObject._setSourcePort_(self)

    def connectTo(self, portObject):
        assert isinstance(portObject, Abc_MtlInput), u'''Argument "portObject" must type of "Input"'''
        self._addTargetPort_(portObject)

    def hasTargets(self):
        return self._targetPortIndexList != []

    def target(self, attrpathString):
        pass

    def hasTarget(self, attrpathString):
        pass

    def targets(self):
        if self.hasTargets():
            return [
                self._qry_object_(i)
                for i in self._targetPortIndexList
            ]
        return []

    def isConnectedTo(self, portObject):
        return self._hasTargetPort_(portObject)

    def hasParent(self):
        return self._parentPortpathStr is not None

    def parent(self):
        if self.hasParent():
            return self._nodeObj.port(
                self._parentPortpathStr
            )

    def hasChildren(self):
        """
        :return: bool
        """
        return self._childPortpathStrList != []

    def childrenCount(self):
        return len(self._childPortpathStrList)

    def children(self):
        """
        :return: list(object of Port, ...)
        """
        if self.hasChildren():
            return [
                self._nodeObj.port(i)
                for i in self._childPortpathStrList
            ]

    def child(self, portnameString):
        if self.hasChild(portnameString):
            return self._nodeObj.port(portnameString)

    def childAt(self, index):
        if self.hasChildren():
            return self._nodeObj.port(self._childPortpathStrList[index])

    def hasChild(self, portnameString):
        return portnameString in self._childPortpathStrList

    def isChannel(self):
        return self._assignString in [
            self.DEF_mtl_keyword_input_channel,
            self.DEF_mtl_keyword_output_channel
        ]

    def insertTarget(self, inputPort, outputPort):
        for i in self.targets():
            outputPort.connectTo(i)
        self.connectTo(inputPort)

    def _queryKeyString_(self):
        return self.portpathString()

    def _xmlAttributeAttachValueString_(self):
        return self.portpathString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# port > input
class Abc_MtlInput(Abc_MtlPort):
    def _initAbcMtlInput(self, *args):
        self._initAbcMtlPort(*args)

    def portgiven(self):
        """
        :return:
            1.object of Node
            2.object of Value
        """
        if self.hasSource() is True:
            return self.source()
        return self.value()

    def _xmlAttributes_(self):
        return [
            self.portpath(),
            self.porttype(),
            self.portgiven()
        ]


# port > output
class Abc_MtlOutput(Abc_MtlPort):
    def _initAbcMtlOutput(self, *args):
        self._initAbcMtlPort(*args)

    def _xmlAttributeAttachValueString_(self):
        return self.portpathString()

    def _xmlAttributeAttaches_(self):
        if self.isChannel() is True:
            return [
                self.parent(),
                (self._xmlAttributeAttachKeyString_(), self.portnameString())
            ]
        else:
            return [
                self.node()
            ]

    def _xmlAttributes_(self):
        return [
            self.portpath(),
            self.porttype(),
            self.value()
        ]


class Abc_MtlGeometryProperty(Abc_MtlPort):
    def _initAbcMtlGeometryProperty(self, *args):
        self._initAbcMtlPort(*args)

    def _xmlAttributes_(self):
        return [
            self.portpath(),
            self.porttype(),
            self.value()
        ]


class Abc_MtlGeometryVisibility(Abc_MtlPort):
    def _initAbcMtlVisibilityAssign(self, *args):
        self._initAbcMtlPort(*args)

    def _xmlAttributes_(self):
        return [
            self.portpath(),
            self.value()
        ]


# object ************************************************************************************************************* #
class Abc_MtlObject(
    Def_XmlObject,
    mtlObjDef.Def_XmlCacheObj
):
    CLS_grh_type = None
    CLS_grh_category = None

    CLS_grh_nodepath = None

    CLS_grh_port_set = None

    OBJ_mtl_query_cache = None
    OBJ_mtl_obj_cache = None

    VAR_mtl_port_class_dict = {}
    VAR_mtl_value_class_dict = {}

    def _initAbcMtlObject(self, *args):
        categoryString, nodepathString = args[:2]

        self._categoryObj = self.CLS_grh_category(categoryString)
        self._nodepathObj = self.CLS_grh_nodepath(nodepathString)

        typeString = self.OBJ_mtl_query_cache.nodeDef(categoryString).type
        self._typeObj = self.CLS_grh_type(typeString)

        self._portSetObj = self.CLS_grh_port_set(categoryString)
        self._inputSetObj = self.CLS_grh_port_set(categoryString)
        self._outputSetObj = self.CLS_grh_port_set(categoryString)

        self._initDefMtlCacheObj(nodepathString)

        self.OBJ_mtl_obj_cache._set_add_obj_(self)

        self._initializePorts_()

        self._proxyObj = None

        self._initDefMtlObject()

    def _setProxy_(self, obj):
        self._proxyObj = obj

    def _setTypeString_(self, typeString):
        pass

    def _getPortObject_(self, portnameString, assignString):
        if assignString in self.VAR_mtl_port_class_dict:
            cls = self.VAR_mtl_port_class_dict[assignString]
            nodeObject = self
            return cls(nodeObject, portnameString)

    def _getPortCls_(self, assignString):
        if assignString in self.VAR_mtl_port_class_dict:
            return self.VAR_mtl_port_class_dict[assignString]

    def _addPortObject_(self, portObject, portnameString, assignString):
        if assignString in [self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_input_channel, self.DEF_mtl_keyword_property, self.DEF_mtl_keyword_visibility]:
            self._inputSetObj._set_add_obj_(portnameString, portObject)
        elif assignString in [self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_output_channel]:
            self._outputSetObj._set_add_obj_(portnameString, portObject)
        self._portSetObj._set_add_obj_(portnameString, portObject)

    def _initializePorts_(self):
        def addPortFnc_(nodepathString_, portDefObject_):
            _portnameString = portDefObject_.portname
            _porttypeString = portDefObject_.porttype
            _portdataString = portDefObject_.portdata
            _assignString = portDefObject_.assign
            _parentPortpathStr = portDefObject_.parent
            _childObjKeyStrings = portDefObject_.children

            _attributeString = mtlMethods.Attribute.composeBy(
                nodepathString_, _portnameString
            )
            _portCls = self.VAR_mtl_port_class_dict[_assignString]
            _objKeyString = _attributeString
            _portCls = self._getPortCls_(_assignString)

            _portObject = None
            if _portCls is not None:
                _portObject = self._mtd_cache_(
                    self.OBJ_mtl_obj_cache, _attributeString,
                    _portCls, (self, _portnameString)
                )

                _portObject._set_porttype_(_porttypeString)
                _portObject._set_parent_(_parentPortpathStr)
                _portObject._set_children_(_childObjKeyStrings)
                _portObject._setAssign_(_assignString)

                _valueCls = self.VAR_mtl_value_class_dict[_porttypeString]

                _portObject._setValue_(_valueCls(_portdataString))
                _portObject._setDefaultValue_(_valueCls(_portdataString))

                self._addPortObject_(_portObject, _portnameString, _assignString)

        for i in self.OBJ_mtl_query_cache.nodeDef(self.categoryString()).ports:
            addPortFnc_(self.nodepathString(), i)

    def _getChangedInputs_(self):
        def _addFnc(portObject):
            if not portObject in lis:
                lis.append(portObject)

        lis = []
        for i in self.inputs():
            if i.isChanged() is True:
                _addFnc(i)
        return lis

    def type(self):
        """
        :return: str
        """
        return self._typeObj

    def typeString(self):
        return self._typeObj.toString()

    def category(self):
        return self._categoryObj

    def categoryString(self):
        """
        :return: str
        """
        return self._categoryObj.toString()

    def nodepath(self):
        return self._nodepathObj

    def nodepathString(self):
        return self._nodepathObj.nodepathString()

    def name(self):
        return self._nodepathObj.name()

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.name().setRaw(nameString)

    def nameString(self):
        """
        :return: str
        """
        return self.name().toString()

    def hasPorts(self):
        return self._portSetObj.hasObjects()

    def hasPort(self, *args):
        return self._portSetObj._get_has_obj_(*args)

    def ports(self):
        return self._portSetObj.objects()

    def port(self, portpathString):
        assert self._portSetObj._get_has_obj_(portpathString) is True, u'''node "{}" do not has port "{}".'''.format(
            self.categoryString(), portpathString
        )
        return self._portSetObj._get_object_(portpathString)

    def hasInputs(self):
        return self._inputSetObj.hasObjects()

    def hasInput(self, *args):
        return self._inputSetObj._get_has_obj_(*args)

    def inputs(self):
        """
        :return: list(object or attribute, ...)
        """
        return self._inputSetObj.objects()

    def input(self, portpathString):
        """
        :param portpathString: str
        :return: object of Port
        """
        return self._inputSetObj.object(portpathString)

    def sourceNodes(self):
        return [i.source().node() for i in self.inputs() if i.hasSource()]

    def outputs(self):
        return self._outputSetObj.objects()

    def output(self, portpathString=None):
        if portpathString is not None:
            return self._outputSetObj.object(portpathString)
        return self._outputSetObj.objects()[-1]

    def targets(self):
        lis = []
        for outputObject in self.outputs():
            if outputObject.hasTargets():
                for inputObject in outputObject.targets():
                    if not inputObject in lis:
                        lis.append(inputObject)

        return lis

    def connections(self):
        lis = []
        for sourceObject in self.outputs():
            if sourceObject.hasTargets():
                for targetObject in sourceObject.targets():
                    if not targetObject in lis:
                        lis.append([sourceObject, targetObject])
        return lis

    def targetNodes(self, categoryString=None):
        return self._get_target_nodes_(self, categoryString)

    def allTargetNodes(self, categoryString=None):
        return self._get_all_target_nodes_(self, categoryString)

    @classmethod
    def _get_target_nodes_(cls, nodeObject, categoryString):
        lis = []
        for portObject in nodeObject.outputs():
            if portObject.hasTargets():
                for _targetObject in portObject.targets():
                    _nodeObject = _targetObject.node()
                    if not _nodeObject in lis:
                        lis.append(_nodeObject)

        return cls._get_nodes_filter_(lis, categoryString)

    @classmethod
    def _get_all_target_nodes_(cls, nodeObject, categoryString):
        def rcsFnc_(nodeObject_):
            for portObject in nodeObject_.outputs():
                if portObject.hasTargets():
                    for _targetObject in portObject.targets():
                        _nodeObject = _targetObject.node()
                        if not _nodeObject in lis:
                            lis.append(_nodeObject)
                            rcsFnc_(_nodeObject)
        lis = []
        rcsFnc_(nodeObject)
        return cls._get_nodes_filter_(lis, categoryString)

    @classmethod
    def _get_nodes_filter_(cls, nodeObjects, categoryString):
        lis = []
        if categoryString is not None:
            categoryString = bscMethods.String.toList(categoryString)

        for i in nodeObjects:
            _categoryString = i.categoryString()
            if categoryString is not None:
                if _categoryString in categoryString:
                    lis.append(i)
            else:
                lis.append(i)
        return lis

    def toString(self):
        return self.nodepathString()

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlElementString_(self):
        return self.categoryString()

    def _xmlAttributes_(self):
        return [
            self.nodepath(),
            self.type()
        ]

    def _xmlChildren_(self):
        return self._getChangedInputs_()

    def _xmlAttributeAttachValueString_(self):
        return self.nodepathString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# object > node
class Abc_MtlNode(Abc_MtlObject):
    def _initAbcMtlNode(self, *args):
        self._initAbcMtlObject(*args)


# object > dag
class Abc_MtlDag(Abc_MtlObject):
    CLS_mtl_child_set = None

    def _initAbcMtlDag(self, *args):
        categoryString, nodepathString = args[:2]

        self._nodepathObj = self.CLS_grh_nodepath(nodepathString)
        self._childSetObj = self.CLS_mtl_child_set(nodepathString)

        self._initAbcMtlObject(*args)

    def children(self):
        """
        :return: list(object of Node, ...)
        """
        return self._childSetObj.objects()

    def hasChildren(self):
        """
        :return: bool
        """
        return self._childSetObj.hasObjects()

    def childrenCount(self):
        """
        :return: int
        """
        return self._childSetObj.objectCount()

    def childAt(self, index):
        """
        :param index: int
        :return: object of Node
        """
        return self._childSetObj.objectAt(index)

    def addChild(self, nodeObject):
        """
        :param nodeObject: object of Node
        :return: None
        """
        self._childSetObj.addObject(nodeObject)


# geometry
class Abc_MtlGeometry(Abc_MtlDag):
    def _initAbcMtlGeometry(self, *args):
        categoryString, nodepathString = self.DEF_mtl_category_mesh, args[0]

        self._initAbcMtlDag(
            categoryString,
            nodepathString
        )


# port proxy ********************************************************************************************************* #
class Abc_MtlPortProxy(Def_XmlObject):
    def _initAbcMtlPortProxy(self, *args):
        self._portObj = args[0]
        self._portObj._setProxy_(self)

    def port(self):
        return self._portObj

    def _queryKeyString_(self):
        return self._portObj.portpathString()

    def _xmlAttributes_(self):
        return [
            self._portObj.portpath(),
            self._portObj.porttype(),
            self._portObj.value()
        ]


class Abc_MtlBindInput(Abc_MtlPortProxy):
    def _initAbcMtlBindInput(self, *args):
        self._initAbcMtlPortProxy(*args)

        self._nodeGraphOutputObj = None

    def _setNodeGraphOutput_(self, nodeGraphOutputObject):
        self._nodeGraphOutputObj = nodeGraphOutputObject

    def portgiven(self):
        if self._portObj.hasSource() is True:
            return self._nodeGraphOutputObj
        return self._portObj.value()

    def _xmlAttributes_(self):
        return [
            self._portObj.portpath(),
            self._portObj.porttype(),
            self.portgiven()
        ]


class Abc_MtlProperty(Abc_MtlPortProxy):
    def _initAbcMtlProperty(self, *args):
        self._initAbcMtlPortProxy(*args)


class Abc_MtlVisibility_(Abc_MtlPortProxy):
    def _initAbcMtlVisibilityAssign(self, *args):
        self._initAbcMtlPortProxy(*args)


# node graph output
class Abc_MtlNodeGraphOutput(Abc_MtlPortProxy):
    CLS_mtl_name = None

    def _initAbcMtlNodeGraphOutput(self, *args):
        self._initAbcMtlPortProxy(*args)

        self._nameObj = self.CLS_mtl_name(self._portObj.attrpathString())

        self._nodeGraphObj = None

    def _setNodeGraph_(self, nodeGraphObject):
        self._nodeGraphObj = nodeGraphObject

    def _setPort_(self, portObject):
        self._portObj = portObject

    def name(self):
        return self._nameObj

    def nameString(self):
        """
        :return: str
        """
        return self._nameObj.raw()

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObj.setRaw(nameString)

    def porttype(self):
        return self._portObj.porttype()

    def nodeGraph(self):
        return self._nodeGraphObj

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj,
            self._portObj.porttype(),
            self._portObj
        ]

    def _xmlAttributeAttachValueString_(self):
        return self._nameObj._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            self.nodeGraph(),
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# ******************************************************************************************************************** #
class Abc_MtlObjectProxy(Def_XmlObject):
    CLS_mtl_name = None
    CLS_mtl_node = None

    def _initAbcMtlObjectProxy(self, *args):
        self._getProxyNode_(*args)

    def _getProxyNode_(self, *args):
        if isinstance(args[0], Abc_MtlObject):
            self._nodeObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            self._nodeObj = self.CLS_mtl_node(*args)

        self._nodeObj._setProxy_(self)

        self._nameObj = self.CLS_mtl_name(self._nodeObj.nodepathString())

    def _queryKeyString_(self):
        return self._nodeObj.nodepathString()

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def node(self):
        return self._nodeObj

    def toString(self):
        return self._nodeObj.nodepathString()


class Abc_MtlShaderProxy(Abc_MtlObjectProxy):
    CLS_mtl_node_graph_set = None
    CLS_mtl_node_graph = None

    CLS_mtl_port_proxy_set = None
    CLS_mtl_port_proxy = None

    def _initAbcMtlShaderProxy(self, *args):
        self._initAbcMtlObjectProxy(*args)
        self._getProxyPorts_()

        self._nodeGraphSetObj = self.CLS_mtl_node_graph_set(self.name().toString())
        self._addNodeGraph_()

    def _getProxyPorts_(self):
        self._bindInputSetObj = self.CLS_mtl_port_proxy_set(self.node().nodepathString())

        for i in self._nodeObj.inputs():
            portProxyObject = self.CLS_mtl_port_proxy(i)
            self._bindInputSetObj._set_add_obj_(portProxyObject)

    def _updateNodeGraphs_(self):
        if self.hasNodeGraphs():
            nodeGraphObject = self.nodeGraph(0)

            materialProxyObject = self._getMaterialProxy_()
            if materialProxyObject is not None:
                nodeGraphObject.name()._setXmlNameSuffixString_(
                    '{}__{}'.format(
                        materialProxyObject.name()._xmlNameSuffixString_(), self._getMaterialContext_()
                    )
                )

            nodeGraphObject._update_(self.node())

    def _addNodeGraph_(self):
        nodeGraphObject = self.CLS_mtl_node_graph()

        nodeGraphObject.setNameString(
            self._nodeObj.nameString()
        )
        self._nodeGraphSetObj.addObject(nodeGraphObject)

    def _getMaterialContext_(self):
        for i in self._nodeObj.outputs():
            if i.hasTargets():
                targets = i.targets()
                for target in targets:
                    proxyNodeObject = target.node()._proxyObj
                    if isinstance(proxyNodeObject, Abc_MtlMaterialProxy):
                        return target.portnameString()

    def _getMaterialProxy_(self):
        for i in self._nodeObj.outputs():
            if i.hasTargets():
                targets = i.targets()
                for target in targets:
                    proxyNodeObject = target.node()._proxyObj
                    if isinstance(proxyNodeObject, Abc_MtlMaterialProxy):
                        return proxyNodeObject

    def bindInput(self, portnameString):
        return self._bindInputSetObj.object(portnameString)

    def bindInputs(self):
        return self._bindInputSetObj.objects()

    def hasNodeGraphs(self):
        return self._nodeGraphSetObj.hasObjects()

    def hasNodeGraph(self, nameString):
        return self._nodeGraphSetObj._get_has_obj_(nameString)

    def nodeGraph(self, nameString):
        return self._nodeGraphSetObj._get_object_(nameString)

    def nodeGraphs(self):
        return self._nodeGraphSetObj.objects()

    def _getChangedBindInputs_(self):
        lis = []
        portProxyObjects = self.bindInputs()
        if portProxyObjects:
            for portProxyObject in portProxyObjects:
                portObject = portProxyObject.port()
                if portObject.isChanged():
                    lis.append(portProxyObject)
        return lis

    def _xmlAttributes_(self):
        return [
            self._nodeObj.name(),
            self._nodeObj.category(),
            [(u'context', self._getMaterialContext_())]
        ]

    def _xmlChildren_(self):
        return self._getChangedBindInputs_()


class Abc_MtlMaterialProxy(Abc_MtlObjectProxy):
    def _initAbcMtlMaterialProxy(self, *args):
        self._initAbcMtlObjectProxy(*args)

    def _getProxyNode_(self, *args):
        if isinstance(args[0], Abc_MtlObject):
            self._nodeObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            nodepathString = args[0]
            self._nodeObj = self.CLS_mtl_node(self.DEF_mtl_category_material, nodepathString)

        self._nodeObj._setProxy_(self)

        self._nameObj = self.CLS_mtl_name(self._nodeObj.nodepathString())

    def surfaceInput(self):
        return self._nodeObj.port(u'surfaceshader')

    def connectSurfaceFrom(self, portObject):
        portObject.connectTo(self.surfaceInput())

    def surfaceShader(self):
        if self.surfaceInput().hasSource():
            return self.surfaceInput().source().node()._proxyObj

    def displacementInput(self):
        return self._nodeObj.port(u'displacementshader')

    def connectDisplacementFrom(self, portObject):
        portObject.connectTo(self.displacementInput())

    def displacementShader(self):
        if self.displacementInput().hasSource():
            return self.displacementInput().source().node()._proxyObj

    def volumeInput(self):
        return self._nodeObj.port(u'volumeshader')

    def connectVolumeFrom(self, portObject):
        portObject.connectTo(self.volumeInput())

    def volumeShader(self):
        if self.volumeInput().hasSource():
            return self.volumeInput().source().node()._proxyObj

    def shaders(self):
        return bscMethods.List.cleanupTo(
            [self.surfaceShader(), self.displacementShader(), self.volumeShader()]
        )

    def _xmlAttributes_(self):
        return [
            self.name()
        ]

    def _xmlChildren_(self):
        # update shader's node graph first
        for proxyObject in self.shaders():
            proxyObject._updateNodeGraphs_()
        return self.shaders()

    def _xmlElements_(self):
        lis = []
        for proxyObject in self.shaders():
            nodeGraphs = proxyObject.nodeGraphs()
            if nodeGraphs:
                for nodeGraph in nodeGraphs:
                    if nodeGraph.hasNodes():
                        if not nodeGraph in lis:
                            lis.append(nodeGraph)
        return lis

    def _xmlAttributeAttachValueString_(self):
        return self.name()._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abc_MtlGeometryProxy(Abc_MtlObjectProxy):
    CLS_mtl_port_proxy_set = None
    CLS_mtl_property = None
    CLS_mtl_visibility = None

    CLS_mtl_propertyset = None

    def _initAbcMtlGeometryProxy(self, *args):
        self._initAbcMtlObjectProxy(*args)
        self._getProxyPorts_()

        self._propertysetObj = self.CLS_mtl_propertyset(self.nameString())

    def _getProxyNode_(self, *args):
        if isinstance(args[0], Abc_MtlObject):
            self._nodeObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            nodepathString = args[0]
            self._nodeObj = self.CLS_mtl_node(self.DEF_mtl_category_mesh, nodepathString)

        self._nodeObj._setProxy_(self)

        self._nameObj = self.CLS_mtl_name(self._nodeObj.nodepathString())

    def _getProxyPorts_(self):
        self._propertySetObj = self.CLS_mtl_port_proxy_set(self.nameString())
        self._visibilitySetObj = self.CLS_mtl_port_proxy_set(self.nameString())

        for portObject in self._nodeObj.inputs():
            assignString = portObject._assignString
            if assignString == self.DEF_mtl_keyword_property:
                propertyObject = self.CLS_mtl_property(portObject)
                self._propertySetObj._set_add_obj_(propertyObject)
            elif assignString == self.DEF_mtl_keyword_visibility:
                visibilityObject = self.CLS_mtl_visibility(portObject)
                self._visibilitySetObj._set_add_obj_(visibilityObject)

    def _updatePropertyset_(self):
        self._propertysetObj._initializeSets_()

        for i in self.changedProperties():
            self._propertysetObj.addPort(i)

    def property(self, portnameString):
        return self._propertySetObj.object(portnameString)

    def properties(self):
        return self._propertySetObj.objects()

    def changedProperties(self):
        lis = []
        for i in self.properties():
            portObject = i.port()
            if portObject.isChanged():
                lis.append(i)
        return lis

    def visibility(self, portnameString):
        return self._visibilitySetObj.object(portnameString)

    def hasVisibility(self, *args):
        return self._visibilitySetObj._get_has_obj_(*args)

    def visibilities(self):
        return self._visibilitySetObj.objects()

    def changedVisibilities(self):
        lis = []
        for i in self.visibilities():
            portObject = i.port()
            if portObject.isChanged():
                lis.append(i)
        return lis

    def connectMaterial(self, materialProxyObject):
        materialProxyObject.node().output(u'material').connectTo(self.node().input(u'material'))

    def material(self):
        if self.node().input(u'material').hasSource():
            nodeObject = self.node().input(u'material').source().node()
            return nodeObject._proxyObj

    def setPropertyset(self, propertysetObject):
        self._propertysetObj = propertysetObject

    def propertyset(self):
        return self._propertysetObj

    def _xmlAttributes_(self):
        return [
            self._nodeObj.nodepath(),
            self._nodeObj.category()
        ]

    def _xmlChildren_(self):
        return self.changedProperties() + self.changedVisibilities()


# node graph
class Abc_MtlNodeGraph(Def_XmlObject):
    CLS_mtl_name = None

    CLS_mtl_node_set = None
    CLS_mtl_output_set = None

    CLS_mtl_node = None
    CLS_mtl_node_graph_output = None

    def _initAbcMtlNodeGraph(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._nodeSetObj = self.CLS_mtl_node_set()
        self._nodeGraphOutputSetObj = self.CLS_mtl_output_set()

        self._nodeGraphOutputDict = {}

        self._initDefMtlObject()

    @staticmethod
    def _getNodes_(nodeObject):
        def recursionFnc_(nodeObject_):
            for i in nodeObject_.inputs():
                if i.hasSource():
                    _nodeObject = i.source().node()
                    if not _nodeObject in lis:
                        lis.append(_nodeObject)
                        recursionFnc_(_nodeObject)

        lis = []
        recursionFnc_(nodeObject)
        return lis

    @staticmethod
    def _getPorts_(nodeObject):
        lis = []
        for i in nodeObject.inputs():
            if i.hasSource():
                lis.append(i)
        return lis

    def _update_(self, nodeObject):
        [self._addNode_(i) for i in self._getNodes_(nodeObject)]
        [self._addPort_(i) for i in self._getPorts_(nodeObject)]

    def _addNode_(self, *args):
        if isinstance(args[0], (str, unicode)):
            nodeObject = self.CLS_mtl_node(*args)
        else:
            nodeObject = args[0]

        if self._nodeSetObj._get_has_obj_(nodeObject) is False:
            self._nodeSetObj.addObject(nodeObject)

    def _addPort_(self, *args):
        portObject = args[0]

        sourceObject = portObject.source()
        count = self._nodeGraphOutputSetObj.objectCount()

        keyString = sourceObject.attrpathString()
        if self._nodeGraphOutputSetObj._get_has_obj_(keyString) is False:
            nameString = u'output_{}'.format(count)
            nodeGraphOutputObject = self.CLS_mtl_node_graph_output(sourceObject)
            nodeGraphOutputObject.setNameString(nameString)
            nodeGraphOutputObject._setNodeGraph_(self)
            self._nodeGraphOutputSetObj._set_add_obj_(keyString, nodeGraphOutputObject)
        else:
            nodeGraphOutputObject = self._nodeGraphOutputSetObj._get_object_(keyString)

        portObject._proxyObj._setNodeGraphOutput_(nodeGraphOutputObject)

    def name(self):
        return self._nameObj

    def nameString(self):
        """
        :return: str
        """
        return self._nameObj.raw()

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObj.setRaw(nameString)

    def nodes(self):
        """
        :return: list([<Node>, ...])
        """
        return self._nodeSetObj.objects()

    def node(self, nodepathString):
        """
        :param nodepathString: str("nodepathString")
        :return: <Node>
        """
        return self._nodeSetObj._get_object_(nodepathString)

    def nodeCount(self):
        """
        :return: int
        """
        return self._nodeSetObj.objectCount()

    def hasNodes(self):
        """
        :return: bool
        """
        return self._nodeSetObj.hasObjects()

    def outputs(self):
        """
        :return: list(object or output, ...)
        """
        return self._nodeGraphOutputSetObj.objects()

    def output(self, portpathString=None):
        """
        :param portpathString: str
        :return: object of Output
        """
        return self._nodeGraphOutputSetObj.object(portpathString)

    def hasOutputs(self):
        """
        :return: bool
        """
        return self._nodeGraphOutputSetObj.hasObjects()

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj
        ]

    def _xmlChildren_(self):
        return self.nodes() + self.outputs()

    def _xmlAttributeAttachValueString_(self):
        return self.name()._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# portset ************************************************************************************************************ #
class Abc_MtlPortset(Def_XmlObject):
    CLS_mtl_name = None

    CLS_grh_port_set = None
    
    def _initAbcMtlPortset(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._portSetObj = self.CLS_grh_port_set()

        self._initDefMtlObject()

    def _initializeSets_(self):
        self._portSetObj._initializeData_()

    def name(self):
        return self._nameObj

    def nameString(self):
        """
        :return: str
        """
        return self._nameObj.raw()

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObj.setRaw(nameString)

    def addPort(self, portObject):
        self._portSetObj.addObject(portObject)

    def addPorts(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addPort(i) for i in _]

    def ports(self):
        return self._portSetObj.objects()

    def hasPorts(self):
        return self._portSetObj.hasObjects()

    def _xmlAttributeAttachValueString_(self):
        return self.name()._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]

    def _xmlAttributes_(self):
        return [
            self.name()
        ]

    def _xmlChildren_(self):
        return self.ports()


# portset > propertyset
class Abc_MtlPropertyset(Abc_MtlPortset):
    def _initAbcMtlPropertyset(self, *args):
        self._initAbcMtlPortset(*args)


# geometry collection
class Abc_MtlCollection(Def_XmlObject):
    CLS_mtl_name = None

    CLS_mtl_geometry_set = None
    CLS_set_collection = None

    DEF_geometry_separator = None

    def _initAbcMtlCollection(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_mtl_geometry_set()
        self._collectionSetObj = self.CLS_set_collection()
        self._excludeGeometrySetObj = self.CLS_mtl_geometry_set()

        self._initDefMtlObject()

    def nameString(self):
        """
        :return: str
        """
        return self._nameObj.raw()

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObj.setRaw(nameString)

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Geometry
        :return:
        """
        self._geometrySetObj.addObject(geometryObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addGeometry(i) for i in list(_)]

    def geometries(self):
        """
        :return: list(object or geometry, ...)
        """
        return self._geometrySetObj.objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self._geometrySetObj.hasObjects()

    def geometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nodepathString() for i in self.geometries()]

    def fullpathGeometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nodepathString() for i in self.geometries()]

    def excludeGeometrySet(self):
        return self._excludeGeometrySetObj

    def addExcludeGeometry(self, geometryObject):
        self._excludeGeometrySetObj.addObject(geometryObject)

    def addExcludeGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addExcludeGeometry(i) for i in list(_)]

    def excludeGeometries(self):
        return self._excludeGeometrySetObj.objects()

    def collectionSet(self):
        return self._collectionSetObj

    def addCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self._collectionSetObj.addObject(collectionObject)

    def hasCollections(self):
        """
        :return: bool
        """
        return self._collectionSetObj.hasObjects()

    def collections(self):
        """
        :return: list(object of Collection, ...)
        """
        return self._collectionSetObj.objects()

    def collectionNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nameString() for i in self.collections()]

    def toString(self):
        return self.nameString()

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj,
            self._geometrySetObj,
            self.collectionSet(),
            self.excludeGeometrySet()
        ]

    def _xmlAttributeAttachValueString_(self):
        return self.nameString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# assign ************************************************************************************************************* #
class Abc_MtlAssign(Def_XmlObject):
    CLS_mtl_name = None
    CLS_mtl_geometry_set = None

    DEF_geometry_separator = None

    def _initAbcMtlAssign(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_mtl_geometry_set(
            self.nameString()
        )
        self._collectionObj = None

        self._lookObj = None

        self._initDefMtlObject()

    def name(self):
        return self._nameObj

    def hasName(self):
        return self._nameObj.hasRaw()

    def nameString(self):
        """
        :return: str
        """
        return self._nameObj.raw()

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObj._set_raw_string_(nameString)

    def _addGeometry_(self, *args):
        geometryObject = args[0]
        self._geometrySetObj.addObject(geometryObject)

    def hasGeometry(self, *args):
        return self._geometrySetObj._get_has_obj_(*args)

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Geometry
        :return: None
        """
        self._addGeometry_(geometryObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addGeometry(i) for i in list(_)]

    def geometries(self):
        """
        :return: list(object or geometry, ...)
        """
        return self._geometrySetObj.objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self._geometrySetObj.hasObjects()

    def geometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nameString() for i in self.geometries()]

    def fullpathGeometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nodepathString() for i in self.geometries()]

    def setCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self._collectionObj = collectionObject

    def collection(self):
        """
        :return: object of Collection
        """
        return self._collectionObj

    def collectionName(self):
        """
        :return: str
        """
        return self._collectionObj.nameString()

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlElementAttaches_(self):
        pass


class Abc_MtlMaterialAssign(Abc_MtlAssign):
    def _initAbcMtlMaterialAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._materialProxyObj = None

    def setMaterial(self, materialProxyObject):
        """
        :param materialProxyObject: object of MaterialProxy
        :return:
        """
        self._materialProxyObj = materialProxyObject

    def material(self):
        """
        :return: object of ShaderSet
        """
        return self._materialProxyObj

    def _xmlElementAttaches_(self):
        return [
            self._materialProxyObj,
            self._collectionObj
        ]

    def _xmlAttributeAttachValueString_(self):
        self.nameString()

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.material(),
            self._geometrySetObj,
            self.collection()
        ]


class Abc_MtlPropertyAssign(Abc_MtlAssign):
    def _initAbcMtlPropertyAssign(self, *args):
        pass


class Abc_MtlPropertysetAssign(Abc_MtlAssign):
    CLS_mtl_propertyset = None

    def _initAbcMtlPropertysetAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._propertysetObj = None

    def _setPropertyset_(self, *args):
        if isinstance(args[0], (str, unicode)):
            propertysetObject = self.CLS_mtl_propertyset(args[0])
        else:
            propertysetObject = args[0]
        self._propertysetObj = propertysetObject
        return self._propertysetObj

    def setPropertyset(self, *args):
        """
        :param args:
            1.str
            2.instance of "Propertyset"
        :return: instance of "Propertyset"
        """
        return self._setPropertyset_(*args)

    def hasPropertyset(self):
        return self._propertysetObj is not None

    def propertyset(self):
        """
        :return: object of Propertyset
        """
        return self._propertysetObj

    def _xmlElementAttaches_(self):
        return [
            self._propertysetObj,
            self._collectionObj
        ]

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.propertyset(),
            self._geometrySetObj,
            self.collection()
        ]


class Abc_MtlVisibilityAssign(Abc_MtlAssign):
    CLS_grh_type = None
    CLS_value_visibility = None

    CLS_set_geometry_viewer = None

    OBJ_mtl_query_cache = None

    def _initAbcMtlVisibilityAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._vistypeObj = None

        self._visibilityValueObj = None

        self._viewerGeometrySetObj = self.CLS_set_geometry_viewer()

    def type(self):
        return self._vistypeObj

    def setTypeString(self, portnameString):
        self._vistypeObj = self.CLS_grh_type(portnameString)

        portdataString = self.OBJ_mtl_query_cache.nodeDef(self.DEF_mtl_category_mesh).port(portnameString).portdata

        self._visibilityValueObj = self.CLS_value_visibility(portdataString)

    def typeString(self):
        return self._vistypeObj.toString()

    def visible(self):
        return self._visibilityValueObj

    def setGeometryVisibility(self, geometryVisibilityObject):
        visibilityString = geometryVisibilityObject.portpathString()
        self._vistypeObj = self.CLS_grh_type(visibilityString)

        self._visibilityValueObj = geometryVisibilityObject.value()

    def addViewerGeometry(self, geometryObject):
        self._viewerGeometrySetObj.addObject(geometryObject)

    def viewerGeometries(self):
        return self._viewerGeometrySetObj.objsets()

    def _xmlElementAttaches_(self):
        return [
            self._collectionObj
        ]

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.type(),
            self.visible(),
            self._geometrySetObj,
            self._viewerGeometrySetObj,
            self.collection()
        ]


# ******************************************************************************************************************** #
class Abc_MtlLook(Def_XmlObject):
    CLS_mtl_name = None

    CLS_mtl_assign_set = None

    CLS_mtl_visibility = None
    CLS_mtl_visibility_set = None

    CLS_mtl_material_assign = None
    CLS_mtl_material_assign_set = None

    CLS_mtl_propertyset_assign = None
    CLS_mtl_propertyset_assign_set = None

    CLS_mtl_geometry = None
    CLS_mtl_geometry_set = None

    def _initAbcMtlLook(self, *args):
        nameString = args[0]
        self._nameObj = self.CLS_mtl_name(nameString)

        self._visibilitySetObj = self.CLS_mtl_visibility_set(nameString)
        self._materialAssignSetObj = self.CLS_mtl_material_assign_set(nameString)
        self._propertysetAssignSetObj = self.CLS_mtl_propertyset_assign_set(nameString)

        self._assignSetObj = self.CLS_mtl_assign_set(nameString)
        self._geometrySetObj = self.CLS_mtl_geometry_set(nameString)

        self._initDefMtlObject()

    def _addGeometryProxy_(self, *args):
        geometryObject = args[0]
        self._geometrySetObj.addObject(geometryObject)

    def _updateAssigns_(self):
        for i in self._geometrySetObj.objects():
            self._addGeometryMaterialAssigns_(i)
            self._addGeometryPropertyAssigns_(i)
            self._addGeometryVisibilities_(i)

    def _addGeometryMaterialAssigns_(self, geometryProxyObject):
        def addFnc_(geometryObject_, materialProxyObject_):
            materialObject_ = materialProxyObject_.node()
            materialProxyObject_.name()._setXmlNameSuffixString_(
                '__{}'.format(self.nameString())
            )
            _count = self._materialAssignSetObj.objectCount()
            _keyString = materialObject_.nodepathString()
            if self._materialAssignSetObj._get_has_obj_(_keyString):
                _materialAssignObject = self._materialAssignSetObj._get_object_(_keyString)
            else:
                _materialAssignObject = self.CLS_mtl_material_assign(
                    'materialassign_{}'.format(_count)
                )
                _materialAssignObject.setMaterial(materialProxyObject_)
                self._materialAssignSetObj._set_add_obj_(_keyString, _materialAssignObject)

            if _materialAssignObject.hasGeometry(geometryObject_) is False:
                _materialAssignObject.addGeometry(geometryObject_)

        materialProxyObject = geometryProxyObject.material()
        if materialProxyObject is not None:
            addFnc_(geometryProxyObject, materialProxyObject)

    def _addGeometryPropertyAssigns_(self, geometryProxyObject):
        def addFnc_(geometryObject_, propertysetObject_):
            propertysetObject_.name()._setXmlNameSuffixString_(
                '__{}'.format(self.nameString())
            )
            _count = self._propertysetAssignSetObj.objectCount()
            _keyString = geometryObject_.node().nodepathString()
            if self._propertysetAssignSetObj._get_has_obj_(_keyString):
                _propertysetAssignObject = self._propertysetAssignSetObj._get_object_(_keyString)
            else:
                _propertysetAssignObject = self.CLS_mtl_propertyset_assign(
                    propertysetObject_.name()._xmlAttributeAttachValueString_()
                )
                self._propertysetAssignSetObj._set_add_obj_(_keyString, _propertysetAssignObject)

            _propertysetAssignObject.setPropertyset(propertysetObject_)
            if _propertysetAssignObject.hasGeometry(geometryObject_) is False:
                _propertysetAssignObject.addGeometry(geometryObject_)

        geometryProxyObject._updatePropertyset_()
        propertysetObject = geometryProxyObject.propertyset()
        if propertysetObject.hasPorts():
            addFnc_(geometryProxyObject, propertysetObject)

    def _addGeometryVisibilities_(self, geometryProxyObject):
        def addFnc_(geometryObject_, portProxyObject_):
            _portObject = portProxyObject_.port()
            _count = self._visibilitySetObj.objectCount()
            _keyString = _portObject.portpathString()
            if self._visibilitySetObj._get_has_obj_(_keyString):
                _visibilityObject = self._visibilitySetObj._get_object_(_keyString)
            else:
                _visibilityObject = self.CLS_mtl_visibility(
                    'visibility_{}'.format(_count)
                )
                _visibilityObject.setGeometryVisibility(_portObject)
                self._visibilitySetObj._set_add_obj_(_keyString, _visibilityObject)

            if _visibilityObject.hasGeometry(geometryObject_) is False:
                _visibilityObject.addGeometry(geometryObject_)

        geometryVisibilities = geometryProxyObject.changedVisibilities()
        if geometryVisibilities:
            [addFnc_(geometryProxyObject, i) for i in geometryVisibilities]

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def geometries(self):
        return self._geometrySetObj.objects()

    def hasGeometries(self):
        return self._geometrySetObj.hasObjects()

    def addGeometry(self, geometryProxyObject):
        self._addGeometryProxy_(geometryProxyObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (tuple, list)):
            [self.addGeometry(i) for i in list(args[0])]
        else:
            [self.addGeometry(i) for i in list(args)]

    def geometry(self, geometryString):
        return self._geometrySetObj.object(geometryString)

    def hasGeometry(self, *args):
        return self._geometrySetObj._get_has_obj_(*args)

    def materialAssigns(self):
        return self._materialAssignSetObj.objects()

    def propertysetAssigns(self):
        return self._propertysetAssignSetObj.objects()

    def visibilities(self):
        return self._visibilitySetObj.objects()

    def hasAssigns(self):
        return self.assigns() != []

    def assigns(self):
        return self.materialAssigns() + self.propertysetAssigns() + self.visibilities()

    def _xmlElementAttaches_(self):
        lis = []
        for assignObject in self.assigns():
            for xmlObject in assignObject._xmlElementAttaches_():
                if xmlObject is not None:
                    if xmlObject not in lis:
                        lis.append(xmlObject)
        return lis

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj
        ]

    def _xmlChildren_(self):
        self._updateAssigns_()
        return self.assigns()

    def _xmlElements_(self):
        return self._xmlElementAttaches_()


class Abc_MtlFile(Def_XmlObject):
    CLS_mtl_filepath = None

    CLS_mtl_version = None

    CLS_mtl_reference = None
    CLS_mtl_reference_set = None

    CLS_mtl_look = None
    CLS_mtl_look_set = None

    VAR_mtlx_version = None

    def _initAbcMtlFile(self, *args):
        self._filepathObj = self.CLS_mtl_filepath(*args)
        self._versionObj = self.CLS_mtl_version(self.VAR_mtlx_version)

        self._referenceSetObj = self.CLS_mtl_reference_set()
        self._lookSetObj = self.CLS_mtl_look_set()

        self._initDefMtlObject()

    def _addLook_(self, *args):
        if isinstance(args[0], (str, unicode)):
            lookObject = self.CLS_mtl_look(args[0])
        elif isinstance(args[0], self.CLS_mtl_look):
            lookObject = args[0]
        else:
            lookObject = self.CLS_mtl_look(u'default_look')
        self._lookSetObj.addObject(lookObject)
        return lookObject

    def _addReference_(self, *args):
        if self.CLS_mtl_reference is not None:
            referenceCls = self.CLS_mtl_reference
        else:
            referenceCls = self.__class__

        if isinstance(args[0], (str, unicode)):
            fileObject = referenceCls(args[0])
        elif isinstance(args[0], referenceCls):
            fileObject = args[0]
        else:
            fileObject = referenceCls(u'default')

        keyString = fileObject.fullpathFilename()
        self._lookSetObj._set_add_obj_(keyString, fileObject)

    def filepath(self):
        return self._filepathObj

    def fullpathFilename(self):
        return self._filepathObj.toString()

    def version(self):
        return self._versionObj

    def versionString(self):
        return self._versionObj.toString()

    def addReference(self, fileObject):
        self._addReference_(fileObject)

    def references(self):
        return self._lookSetObj.objects()

    def reference(self, fileString):
        return self._lookSetObj.object(fileString)

    def hasLook(self, lookString):
        return self._lookSetObj._get_has_obj_(lookString)

    def addLook(self, *args):
        """
        :param args:
            1.str
            2.instance of "Look"
        :return:
        """
        return self._addLook_(*args)

    def looks(self):
        return self._lookSetObj.objects()

    def look(self, lookString):
        return self._lookSetObj.object(lookString)

    def save(self):
        xmlDoc = self.__str__()
        bscMethods.OsFile.write(
            self.fullpathFilename(), xmlDoc
        )

    def _xmlAttributes_(self):
        return [
            self.version()
        ]

    def _xmlChildren_(self):
        return self.looks()


class Abc_MtlReference(Abc_MtlFile):
    def _initAbcMtlReference(self, *args):
        self._initAbcMtlFile(*args)

    def _queryKeyString_(self):
        return self.fullpathFilename()

    def _xmlAttributes_(self):
        return [
            self._filepathObj
        ]


# ******************************************************************************************************************** #
class Abc_MtlTrsBasic(mtlConfigure.Utility):
    def _initAbcMtlTrsBasic(self):
        pass


# translate ********************************************************************************************************** #
class Abc_MtlDccTranslator(mtlConfigure.Utility):
    OBJ_mtl_trs_query_cache = None

    VAR_mtl_channel_convert_dict = {
        mtlConfigure.Utility.DEF_mtl_porttype_color3: {
            u'category': u'float_to_rgb',
            u'output_portname': u'rgb',
            u'connect': {
                u'rgb.r': u'r',
                u'rgb.g': u'g',
                u'rgb.b': u'b'
            }
        },
        mtlConfigure.Utility.DEF_mtl_porttype_vector3: {
            u'category': u'float_to_rgb',
            u'output_portname': u'vector',
            u'connect': {
                u'vector.x': u'r',
                u'vector.y': u'b',
                u'vector.z': u'b',
            }
        },
        mtlConfigure.Utility.DEF_mtl_porttype_color4: {
            u'category': u'float_to_rgba',
            u'output_portname': u'rgba',
            u'connect': {
                u'rgba.r': u'r',
                u'rgba.g': u'g',
                u'rgba.b': u'b',
                u'rgba.a': u'a'
            }
        },
        mtlConfigure.Utility.DEF_mtl_porttype_vector4: {
            u'category': u'float_to_rgba',
            u'output_portname': u'vector',
            u'connect': {
                u'vector.x': u'r',
                u'vector.y': u'b',
                u'vector.z': u'b',
                u'vector.w': u'a'
            }
        },
    }

    def _initAbcMtlDccTranslator(self, *args):
        mtlNodeCls, dccNodeCls, dccNodeString = args[:3]

        self._mtlNodeCls = mtlNodeCls
        self._dccNodeCls = dccNodeCls

        self._dccNodeObj = self._dccNodeCls(dccNodeString)
        self._dccCategoryString = self._dccNodeObj.category()
        self._dccNodeString = self._dccNodeObj.nodepathString()
        self._dccNodeDefObj = self.OBJ_mtl_trs_query_cache.dccNodeDef(self._dccCategoryString)

        self._mtlCategoryString = self._dccNodeDefObj.mtlCategory
        self._mtlNodeDefObj = self._mtlNodeCls.OBJ_mtl_query_cache.nodeDef(self._mtlCategoryString)
        self._mtlNodeString = self._getMtlNodeString_(self._dccNodeString)

        self._mtlNodeObj = self._getMtlNode_(self._mtlCategoryString, self._mtlNodeString)

        self._translateDccPorts_()

        self._setMtlPorts_()

    def _getMtlNode_(self, mtlCategoryString, mtlNodeString):
        _nodeCls = self._mtlNodeCls
        if mtlCategoryString == self.DEF_mtl_category_mesh:
            return _nodeCls._mtd_cache_(
                _nodeCls.OBJ_mtl_obj_cache, mtlNodeString,
                _nodeCls, (mtlNodeString, )
            )
        return _nodeCls._mtd_cache_(
            _nodeCls.OBJ_mtl_obj_cache, mtlNodeString,
            _nodeCls, (mtlCategoryString, mtlNodeString)
        )

    def _getMtlCategoryString(self, dccCategoryString):
        pass

    def _getMtlNodeString_(self, nodepathString):
        return nodepathString.replace(self.DEF_mya_node_separator, self.DEF_mtl_node_separator)
    # translate port
    def _translateDccPorts_(self):
        # debug use input
        for i in self._dccNodeDefObj.dccInputs:
            self._translateDccInput_(i)

    def _translateDccInput_(self, dccPortDefObject):
        _dccPortnameString = dccPortDefObject.dccPortname
        _mtlPortnameString = dccPortDefObject.mtlPortname

        if self._dccNodeObj.hasPort(_dccPortnameString):
            _dccPortObject = self._dccNodeObj.port(_dccPortnameString)
            _mtlPortObject = self._mtlNodeObj.port(_mtlPortnameString)

            self._translateDccInputGiven_(_dccPortObject, _mtlPortObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'Dcc Port "{}" is Unregistered'.format(_dccPortnameString)
            )

    def _translateDccInputGiven_(self, dccPortObject, mtlPortObject):
        self._translateDccPortPortdata_(dccPortObject, mtlPortObject)
        if dccPortObject.hasSource():
            self._translateDccConnect_(dccPortObject, mtlPortObject)

    def _translateDccConnect_(self, dccPortObject, mtlPortObject):
        sourceMtlPortObject = self._getSourceMtlPort(dccPortObject)
        if sourceMtlPortObject is not None:
            targetMtlPortObject = mtlPortObject
            if targetMtlPortObject.isChannel():
                self._convertMtlConnect_(targetMtlPortObject, sourceMtlPortObject)
            else:
                sourceMtlPortObject.connectTo(targetMtlPortObject)

    def _getSourceMtlPort(self, dccPortObject):
        _dccPortObject = dccPortObject.source()
        _dccNodeObject = _dccPortObject.node()

        _dccNodeString = _dccNodeObject.nodepathString()
        _dccCategoryString = _dccNodeObject.category()
        if self.OBJ_mtl_trs_query_cache.hasDccCategory(_dccCategoryString):
            _dccObjectDefObject = self.OBJ_mtl_trs_query_cache.dccNodeDef(_dccCategoryString)
            _mtlCategoryString = _dccObjectDefObject.mtlCategory

            _dccPortnameString = _dccPortObject.portpathString()
            if _dccObjectDefObject.hasDccOutput(_dccPortnameString):
                _mtlPortnameString = _dccObjectDefObject.dccOutput(_dccPortnameString).mtlPortname

                _mtlNodeString = self._getMtlNodeString_(_dccNodeString)
                _mtlNodeObject = self._getMtlNode_(_mtlCategoryString, _mtlNodeString)

                return _mtlNodeObject.output(_mtlPortnameString)
            else:
                print _dccPortObject.node().nodepathString(), _dccPortnameString
        else:
            print _dccPortObject.node().nodepathString()

    def _convertMtlConnect_(self, mtlTargetChannelObject, sourceMtlChannelObject):
        mtlTargetParentPortObject = mtlTargetChannelObject.parent()
        mtlParentPorttypeString = mtlTargetParentPortObject.porttypeString()
        if mtlParentPorttypeString in self.VAR_mtl_channel_convert_dict:
            mtlAttributestring = mtlTargetParentPortObject.attrpathString()
            _mtlCategoryString = self.VAR_mtl_channel_convert_dict[mtlParentPorttypeString][u'category']
            _mtlOutputPortnameString = self.VAR_mtl_channel_convert_dict[mtlParentPorttypeString][u'output_portname']
            _connectDict = self.VAR_mtl_channel_convert_dict[mtlParentPorttypeString][u'connect']
            _mtlNodestring = '{}@{}'.format(mtlAttributestring.replace(self.DEF_mtl_port_separator, u'__'), _mtlCategoryString)
            _mtlNodeObject = self._getMtlNode_(_mtlCategoryString, _mtlNodestring)

            _mtlNodeObject.output(_mtlOutputPortnameString).connectTo(mtlTargetParentPortObject)

            mtlTargetChannelPortname = mtlTargetChannelObject.portnameString()

            sourceMtlChannelObject.connectTo(_mtlNodeObject.input(mtlTargetChannelPortname))

    def _translateDccPortPortdata_(self, dccPortObject, mtlPortObject):
        dccPortdata = dccPortObject.portdata()
        if self._dccNodeDefObj.mtlPortdataRaw:
            _keyString = mtlPortObject.portnameString()
            if _keyString in self._dccNodeDefObj.mtlPortdataRaw:
                _dict = self._dccNodeDefObj.mtlPortdataRaw[_keyString]
                if dccPortdata in _dict:
                    dccPortdata = _dict[dccPortdata]
        mtlPortObject.setPortdata(dccPortdata)

    def _convertMtlPortdata_(self):
        pass

    def _setMtlPorts_(self):
        mtlPortRaw = self._dccNodeDefObj.mtlPortRaw
        if mtlPortRaw:
            for k, v in mtlPortRaw.items():
                portdataString = v[self.DEF_mtl_key_portdata]
                self._mtlNodeObj.port(k).setPortdataString(portdataString)


class Abc_MtlTrsObject(
    Abc_MtlTrsBasic,
    mtlObjDef.Def_XmlCacheObj
):
    CLS_mtl_object = None
    CLS_mtl_dcc_object = None

    CLS_mtl_translator = None

    OBJ_mtl_query_cache = None
    OBJ_mtl_trs_query_cache = None

    OBJ_mtl_obj_cache = None
    OBJ_mtl_trs_obj_cache = None

    def _initAbcMtlTrsObject(self, *args):
        dccNodeString = args[0]

        self._translatorObj = self.CLS_mtl_translator(
            self.CLS_mtl_object, self.CLS_mtl_dcc_object, dccNodeString
        )

        self._initDefMtlCacheObj(self._translatorObj._dccNodeString)

        self._runCreateExpressions_()

    def _runCreateExpressions_(self):
        expressionDict = self._translatorObj._dccNodeDefObj.createExpressionRaw
        self._runExpressions_(expressionDict)

    def _runAfterExpressions_(self):
        expressionDict = self._translatorObj._dccNodeDefObj.afterExpressionRaw
        self._runExpressions_(expressionDict)

    def _runExpressions_(self, expressionDict):
        if expressionDict:
            if self.DEF_mtl_key_command in expressionDict:
                commands = expressionDict[self.DEF_mtl_key_command]
                if commands:
                    cmdsStr = ';'.join(commands)
                    exec cmdsStr

    def _runInsertToTargetExpression_(self, targetDccNodeObjects, targetMtlOutputPortString, mtlInputPortString, mtlOutputPortString):
        for targetDccNode in targetDccNodeObjects:
            targetTrsNodeObject = self.getTrsNode(targetDccNode.nodepathString())
            targetMtlNodeObject = targetTrsNodeObject.mtlNode()
            copyMtlNodeString = u'{}@{}'.format(targetMtlNodeObject.nodepathString(), self.mtlNode().categoryString())
            copyMtlNodeObject = self.getMtlNode(self.mtlNode().categoryString(), copyMtlNodeString)
            [i.setPortdataString(self.mtlNode().input(i.portpathString()).portdataString()) for i in copyMtlNodeObject.inputs()]

            targetMtlNodeObject.output(targetMtlOutputPortString).insertTarget(
                copyMtlNodeObject.input(mtlInputPortString),
                copyMtlNodeObject.output(mtlOutputPortString)
            )

    def _runInsertColorCorrectExpression_(self, portdataDict=None):
        connections = self.mtlNode().connections()
        mtl_category_0 = 'color_correct'
        node_string_0 = '{}@{}'.format(self.mtlNode().nodepathString(), mtl_category_0)
        mtlColorCorrectObject = self.getMtlNode(mtl_category_0, node_string_0)
        for sourceObject, targetObject in connections:
            if sourceObject.isChannel() is False:
                mtlColorCorrectObject.output().connectTo(targetObject)
            else:
                _dict = {
                    'r': 'rgba.r',
                    'g': 'rgba.g',
                    'b': 'rgba.b',
                    'a': 'rgba.a'
                }
                mtlColorCorrectObject.output(_dict[sourceObject.portnameString()]).connectTo(targetObject)

        self.mtlNode().output().connectTo(mtlColorCorrectObject.input('input'))
        if portdataDict:
            for k, v in portdataDict.items():
                mtlColorCorrectObject.port(k).setPortdata(self.dccNode().port(v).portdata())
        return mtlColorCorrectObject

    def _convertDccMultiTexture_(self, filepathString):
        if self.dccNode().category() == u'file':
            isUdim = True
            if filepathString:
                isSequence = self.dccNode().port('useFrameExtension').portdata()
                uvTilingMode = self.dccNode().port('uvTilingMode').portdata()
                dirnameString = bscMethods.OsFile.dirname(filepathString)
                basenameString = bscMethods.OsFile.basename(filepathString)
                #
                findKeys = self.MOD_re.findall(u'[0-9][0-9][0-9][0-9]', basenameString)
                if findKeys:
                    if u'<udim>' in basenameString.lower():
                        isUdim = False
                    elif not uvTilingMode == 'UDIM (Mari)':
                        isUdim = False
                    #
                    if isUdim:
                        basenameString = basenameString.replace(findKeys[-1], '<udim>')
                    elif isSequence:
                        basenameString = basenameString.replace(findKeys[-1], '<f>')
                    #
                    filepathString = bscMethods.OsPath.composeBy(dirnameString, basenameString)
        return filepathString

    def getMtlNode(self, mtlCategoryString, mtlNodeString):
        return self._mtd_cache_(
            self.OBJ_mtl_obj_cache, mtlNodeString,
            self.CLS_mtl_object, (mtlCategoryString, mtlNodeString)
        )

    def getTrsNode(self, dccNodeString):
        return self._mtd_cache_(
            self.OBJ_mtl_trs_obj_cache, dccNodeString,
            self.__class__, (dccNodeString, )
        )

    def dccNodeDef(self):
        return self._translatorObj._dccNodeDefObj

    def dccNode(self):
        return self._translatorObj._dccNodeObj

    def mtlNodeDef(self):
        return self._translatorObj._mtlNodeDefObj

    def mtlNode(self):
        return self._translatorObj._mtlNodeObj

    def __str__(self):
        return self._translatorObj._mtlNodeObj.__str__()


# translate node
class Abc_MtlTrsNode(Abc_MtlTrsObject):
    def _initAbcMtlTrsNode(self, *args):
        self._initAbcMtlTrsObject(*args)


# proxy ************************************************************************************************************** #
class Abc_MtlTrsObjectProxy(Abc_MtlTrsBasic):
    CLS_mtl_node_proxy = None

    CLS_mtl_trs_node = None

    def _initAbcMtlTrsObjectProxy(self, *args):
        dccNodeString = args[0]

        self._trsNodeObject = self.CLS_mtl_trs_node._mtd_cache_(
            self.CLS_mtl_trs_node.OBJ_mtl_trs_obj_cache, dccNodeString,
            self.CLS_mtl_trs_node, (dccNodeString,)
        )

        self._dccNodeObj = self._trsNodeObject.dccNode()
        self._mtlNodeObj = self._trsNodeObject.mtlNode()

        self._mtlNodeProxyObj = self.CLS_mtl_node_proxy(self._mtlNodeObj)

    def dccNode(self):
        return self._dccNodeObj

    def mtlNode(self):
        return self._mtlNodeObj

    def mtlNodeProxy(self):
        return self._mtlNodeProxyObj

    def __str__(self):
        return self._mtlNodeProxyObj.__str__()


class Abc_MtlTrsShaderProxy(Abc_MtlTrsObjectProxy):
    def _initAbcMtlTrsShaderProxy(self, *args):
        self._initAbcMtlTrsObjectProxy(*args)

        self._translateMtlNodes_()

    def _translateMtlNodes_(self):
        dccNodes = self._dccNodeObj.allSourceNodes()
        for i in dccNodes:
            dccCategoryString = i.category()
            dccNodeString = i.nodepathString()
            if self.CLS_mtl_trs_node.OBJ_mtl_trs_query_cache.hasDccCategory(dccCategoryString):
                _trsNodeObject = self.CLS_mtl_trs_node._mtd_cache_(
                    self.CLS_mtl_trs_node.OBJ_mtl_trs_obj_cache, dccNodeString,
                    self.CLS_mtl_trs_node, (dccNodeString,)
                )
            else:
                bscMethods.PyMessage.traceWarning(
                    u'''DCC Category "{}({})"is Unregistered!!!'''.format(dccCategoryString, dccNodeString)
                )


class Abc_MtlTrsMaterialProxy(Abc_MtlTrsObjectProxy):
    CLS_mtl_trs_shader_proxy = None

    VAR_mtl_dcc_shader_portname_list = []

    def _initAbcMtlTrsMaterialProxy(self, *args):
        self._initAbcMtlTrsObjectProxy(*args)

        self._translateMtlShaderProxies_()

    def _translateMtlShaderProxies_(self):
        for dccPortnameString in self.VAR_mtl_dcc_shader_portname_list:
            if isinstance(dccPortnameString, (str, unicode)):
                dccPortObject = self._dccNodeObj.port(dccPortnameString)
                if dccPortObject.hasSource():
                    dccShaderObject = dccPortObject.source().node()
                    dccNodeString = dccShaderObject.nodepathString()
                    _trsNodeProxyObject = self.CLS_mtl_trs_shader_proxy(dccNodeString)
            elif isinstance(dccPortnameString, (tuple, list)):
                dccPortObjects = [self._dccNodeObj.port(i) for i in dccPortnameString]
                if dccPortObjects[0].hasSource():
                    dccPortObject = dccPortObjects[0]

                    dccShaderObject = dccPortObject.source().node()
                    dccNodeString = dccShaderObject.nodepathString()

                    _sourceTrsNodeProxyObject = self.CLS_mtl_trs_shader_proxy(dccNodeString)
                    sourceNodeDefObject = _sourceTrsNodeProxyObject._trsNodeObject.dccNodeDef()
                    sourcePortnameString = sourceNodeDefObject.dccPort(dccPortObject.source().portpathString()).mtlPortname

                    _targetTrsNodeProxyObject = self
                    targetDccNodeDefObject = _targetTrsNodeProxyObject._trsNodeObject.dccNodeDef()
                    targetPortnameString = targetDccNodeDefObject.dccPort(dccPortObject.portpathString()).mtlPortname

                    _sourceTrsNodeProxyObject.mtlNode().port(sourcePortnameString).connectTo(
                        _targetTrsNodeProxyObject.mtlNode().port(targetPortnameString)
                    )
                else:
                    dccPortObject = dccPortObjects[1]
                    if dccPortObject.hasSource():
                        dccShaderObject = dccPortObject.source().node()
                        dccNodeString = dccShaderObject.nodepathString()
                        _trsNodeProxyObject = self.CLS_mtl_trs_shader_proxy(dccNodeString)


class Abc_MtlTrsGeometryProxy(Abc_MtlTrsObjectProxy):
    CLS_mtl_trs_material_proxy = None

    def _initAbcMtlTrsGeometryProxy(self, *args):
        self._initAbcMtlTrsObjectProxy(*args)

        self._getMtlMaterials_()

    def _getMtlMaterials_(self):
        dccMaterials = self._dccNodeObj.materials()

        for i in dccMaterials:
            dccNodeString = i.nodepathString()
            _trsNodeProxyObject = self.CLS_mtl_trs_material_proxy(dccNodeString)
            materialProxyObject = _trsNodeProxyObject.mtlNodeProxy()
            self._mtlNodeProxyObj.connectMaterial(materialProxyObject)


# ******************************************************************************************************************** #
class Abc_MtlTrsLook(Abc_MtlTrsBasic):
    CLS_mtl_look = None
    CLS_mtl_trs_geometry_proxy = None

    def _initAbcMtlTrsLook(self, *args):
        self._mtlLookObj = self.CLS_mtl_look(*args)

    def mtlNode(self):
        return self._mtlLookObj

    def addDccGeometry(self, dccNodeString):

        _trsNodeProxyObject = self.CLS_mtl_trs_geometry_proxy(dccNodeString)

        mtlNodeProxyObject = _trsNodeProxyObject.mtlNodeProxy()
        if self._mtlLookObj.hasGeometry(mtlNodeProxyObject) is False:
            self._mtlLookObj.addGeometry(mtlNodeProxyObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Geometry "{}" is Exist.'''.format(mtlNodeProxyObject.nodepathString())
            )

    def addDccGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addDccGeometry(i) for i in _]

    def _getMtlGeometries_(self):
        pass

    def __str__(self):
        return self._mtlLookObj.__str__()


# ******************************************************************************************************************** #
class Abc_MtlTrsFile(Abc_MtlTrsBasic):
    CLS_mtl_file = None
    CLS_trs_look = None

    OBJ_mtl_trs_obj_cache = None

    def _initAbcMtlTrsFile(self, *args):
        fileString = args[0]
        self._mtlFileObj = self.CLS_mtl_file(fileString)
        self._mtlFileObj.addReference(u'materialx/arnold/nodedefs.mtlx')

    def addLook(self, lookString):
        trsLookObject = self.CLS_trs_look(lookString)
        if self._mtlFileObj.hasLook(lookString) is False:
            mtlLookObject = trsLookObject.mtlNode()
            self._mtlFileObj.addLook(mtlLookObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Look "{}" is Exist.'''.format(lookString)
            )
        return trsLookObject

    def look(self, lookString):
        return self._mtlFileObj.look(lookString)

    def __str__(self):
        for i in self.OBJ_mtl_trs_obj_cache.objects():
            i._runAfterExpressions_()

        return self._mtlFileObj.__str__()

    def save(self):
        self._mtlFileObj.save()

        for i in self.OBJ_mtl_trs_obj_cache.objects():
            i._runAfterExpressions_()

        bscMethods.PyMessage.traceResult(
            u'save file "{}"'.format(self._mtlFileObj.fullpathFilename())
        )
