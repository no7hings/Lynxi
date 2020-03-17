# coding:utf-8
from LxBasic import bscMethods

from LxMaterial import mtlConfigure, mtlObjDefCore, mtlMethods


class Def_MtlXml(mtlConfigure.Utility):
    DEF_mtl_file_attribute_separator = u' '

    VAR_mtl_file_element_key = u''
    VAR_mtl_file_attribute_key = u''

    def _initDefMtlXml(self):
        self._xmlIndentStr = ''

        self._xmlNameSuffixString = None

    def _xmlElementString_(self):
        return self.VAR_mtl_file_element_key

    def _xmlNameSuffixString_(self):
        return self._xmlNameSuffixString

    def _setXmlNameSuffixString_(self, string):
        self._xmlNameSuffixString = string

    def _xmlAttributeAttachKeyString_(self):
        return self.VAR_mtl_file_attribute_key

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
        :return: list(tuple(key, value)/object instance of Def_MtlXml, ...)
        """
        pass

    @classmethod
    def _toXmlString(cls, elementObject, indent=4):
        def addPrefixFnc_(prefix_, lString, rString):
            lis.append(u'{}<{}{}'.format(lString, prefix_, rString))

        def addAttributeFnc_(attributeObject_, lString, rString):
            if attributeObject_ is not None:
                if isinstance(attributeObject_, Def_MtlXml):
                    attributeRaw = attributeObject_._xmlAttributeAttaches_()
                else:
                    attributeRaw = attributeObject_

                if attributeRaw:
                    for i in attributeRaw:
                        if isinstance(i, Def_MtlXml):
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
class Abc_MtlRaw(Def_MtlXml):
    def _initAbcMtlRaw(self, *args):
        if args:
            self._raw = args[0]
            self._rawType = type(self._raw)
        else:
            self._raw = None
            self._rawType = None

        self._initDefMtlXml()

    def _initAbcMtlData(self):
        self._raw = None
        self._rawType = None

    @staticmethod
    def toListSplit(lis, splitCount):
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

    def createByRaw(self, *args):
        pass

    def createByString(self, *args):
        """
        :param args: raw string
        :return: None
        """
        pass

    def setRawType(self, typeString):
        """
        :param typeString: str
        :return: None
        """
        self._rawType = typeString

    def rawType(self):
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


class Abc_MtlString(Abc_MtlRaw):
    def Abc_initAbcMtlString(self, *args):
        self._initAbcMtlRaw(*args)

    def toString(self):
        """
        :return: str
        """
        return unicode(self._raw)

    def toCamelcaseString(self):
        return bscMethods.StrUnderline.toCamelcase(self.toString())

    def createByString(self, *args):
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
    CLS_mtl_raw = None

    VAR_mtl_raw_separator = None

    def _initAbcMtlPath(self, *args):
        self._initAbcMtlRaw(*args)

        if self.hasRaw():
            self._nameObjLis = [self.CLS_mtl_raw(i) for i in self._raw.split(self.VAR_mtl_raw_separator)]
        else:
            self._nameObjLis = None

    @staticmethod
    def _toStringsMethod(pathString, pathsep):
        if pathString.startswith(pathsep):
            return pathString.split(pathsep)[1:]
        else:
            return pathString.split(pathsep)

    def createByRaw(self, *args):
        raw = args[0]
        self._nameObjLis = [self.CLS_mtl_raw(i) for i in raw.split(self.VAR_mtl_raw_separator)]

    def createByString(self, *args):
        self.createByRaw(*args)

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObjLis[-1].setRaw(nameString)

    def name(self):
        if self.hasRaw():
            return self._nameObjLis[-1]

    def nameString(self):
        """
        :return: str
        """
        if self.hasRaw():
            return self.name().raw()
    
    def nodeString(self):
        return self.toString()
    
    def pathString(self):
        return self.toString()

    def fullpathName(self):
        """
        :return: str
        """
        return self.toString()

    def toString(self):
        """
        :return: str
        """
        return self.VAR_mtl_raw_separator.join([i.toString() for i in self._nameObjLis])

    def pathsep(self):
        """
        :return: str
        """
        return self.VAR_mtl_raw_separator

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

    def nodeString(self):
        return self.toString()


class Abc_MtlMaterialName(Abc_MtlNodeName):
    def _initAbcMtlMaterialName(self, *args):
        self._initAbcMtlNodeName(*args)


class Abc_MtlPortName(Abc_MtlPath):
    def _initAbcMtlPortName(self, *args):
        self._initAbcMtlPath(*args)

    def portString(self):
        return self.toString()


class Abc_MtlFileName(Abc_MtlPath):
    def _initAbcMtlFileName(self, *args):
        self._initAbcMtlPath(*args)


class Abc_MtlObjectSet(Def_MtlXml):
    VAR_mtl_object_separator = u','
    # noinspection PyUnusedLocal
    def _initAbcMtlObjectSet(self, *args):
        if args:
            self._nameString = args[0]
        else:
            self._nameString = 'unknown'

        self._objectList = []
        self._objectFilterDict = {}

        self._objectCount = 0

        self._initDefMtlXml()

    def _initializeData_(self):
        self._objectList = []
        self._objectFilterDict = {}

        self._objectCount = 0

    def _addObject_(self, *args):
        if len(args) == 2:
            keyString, obj = args
        else:
            obj = args[0]
            keyString = obj._queryKeyString_()

        if not keyString in self._objectFilterDict:
            self._objectList.append(obj)
            self._objectFilterDict[keyString] = obj
            self._objectCount += 1

    def _hasObject_(self, *args):
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

    def _object_(self, *args):
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
        self._addObject_(obj)

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
        return self._hasObject_(keyString)

    def object(self, keyString):
        """
        :param keyString: str
        :return: object
        """
        assert keyString in self._objectFilterDict, u'''{}({})'s object "{}" is Unregistered.'''.format(
            self.__class__.__name__, self._nameString, keyString
        )
        return self._object_(keyString)

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
        return self._object_(index)

    def hasObjectAt(self, index):
        """
        :param index: int
        :return: object
        """
        return self._hasObject_(index)

    def toString(self):
        """
        :return: str
        """
        return self.VAR_mtl_object_separator.join([i.toString() for i in self.objects()])

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
    CLS_mtl_raw = None

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
            self.createByString(*args)
        else:
            self.createByRaw(*args)

    def createByRaw(self, *args):
        """
        :param args: raw of typed
        :return: None
        """
        assert args is not (), u'argument must not be "empty".'
        raw = args[0]
        if self.VAR_mtl_raw_type is not None:
            assert isinstance(raw, self.VAR_mtl_raw_type), u'[ Argument Error ], "arg" Must "{}".'.format(self.VAR_mtl_raw_type)
            self.setRaw(
                self.CLS_mtl_raw(raw)
            )

    def createByString(self, *args):
        """
        :param args: str
        :return: None
        """
        assert args is not (), u'argument must not be "empty".'
        assert isinstance(args[0], (str, unicode))
        if args[0] is not None:
            self.createByRaw(self._stringToRaw_(args[0]))

    def _stringToRaw_(self, string):
        return self.CLS_mtl_raw(string)

    def toString(self):
        if self.CLS_mtl_raw is float:
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
        self._initAbcMtlData()

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

    def create(self, *args):
        assert args is not (), u'argument must not be "empty".'

        if isinstance(args[0], (str, unicode)):
            self.createByString(*args)
        else:
            self.createByRaw(*args)

    def createByRaw(self, *args):
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

    def createByString(self, *args):
        assert args is not (), u'argument must not be "empty".'
        assert isinstance(args[0], (str, unicode))
        if args[0]:
            valueStringLis = [i.lstrip().rstrip() for i in args[0].split(mtlConfigure.Utility.DEF_mtl_data_separator)]
            raw = self.toListSplit(valueStringLis, self.childValueSize())
            self.createByRaw(raw)

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


class Abc_MtlValue(Def_MtlXml):
    CLS_mtl_datatype = None
    CLS_mtl_raw_data = None

    VAR_mtl_value_type_pattern = None
    VAR_mtl_value_size_pattern = None

    def _initAbcMtlValue(self, *args):
        self._datatypeObj = self.CLS_mtl_datatype(self.VAR_mtl_value_type_pattern[0])
        self._dataObj = self.CLS_mtl_raw_data(self, *args)

        self._initDefMtlXml()

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
        self._dataObj.createByRaw(*args)

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
    Def_MtlXml,
    mtlObjDefCore.Def_MtlObjCache
):
    CLS_mtl_port_string = None

    def _initAbcMtlPort(self, *args):
        nodeObject, portString = args

        self._nodeObj = nodeObject
        self._nodeNameObj = nodeObject._nodeStringObject_()

        self._portNameObj = self.CLS_mtl_port_string(portString)

        # value
        self._valueObj = None
        self._defValueObj = None
        # source
        self._sourcePortIndex = None
        # target
        self._targetPortnameIndexList = []

        self._porttypeString = None

        self._parentPortnameString = None
        self._childPortnameStringList = []

        self._initDefMtlXml()
        self._initDefMtlObjCache(self.attributeString())

    def _setPorttypeString_(self, porttypeString):
        self._porttypeString = porttypeString

    def _setParentPortnameString_(self, portnameString):
        self._parentPortnameString = portnameString

    def _setChildPortnameStrings_(self, portnameStrings):
        self._childPortnameStringList = portnameStrings

    def createByRaw(self, *args):
        pass

    def node(self):
        return self._nodeObj

    def fullpathName(self):
        """
        :return: str
        """
        return self._portNameObj.pathsep().join(
            [self._nodeNameObj.nodeString(), self._portNameObj.portString()]
        )

    def portpath(self):
        return self._portNameObj

    def attributeString(self):
        return self._portNameObj.pathsep().join(
            [self._nodeNameObj.nodeString(), self._portNameObj.portString()]
        )

    def portString(self):
        return self._portNameObj.portString()

    def fullpathPortname(self):
        """
        :return: str
        """
        return self._portNameObj.portString()

    def portname(self):
        return self._portNameObj.name()

    def portnameString(self):
        return self._portNameObj.nameString()

    def _setValue_(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._valueObj = valueObject

    def porttype(self):
        return self.value().datatype()

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

    def valueString(self):
        return self._valueObj.toString()

    def setPortdata(self, raw):
        self._valueObj.setRaw(raw)

    def _setDefaultValue_(self, valueObject):
        self._defValueObj = valueObject

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

    def _qry_getObjectIndex_(self, portObject):
        return self._nodeObj.OBJ_mtl_obj_cache._index_(portObject)

    def _qry_getObject_(self, index):
        return self._nodeObj.OBJ_mtl_obj_cache._object_(index)

    def _isSourcePort_(self, portObject):
        return self._qry_getObjectIndex_(portObject) == self._sourcePortIndex

    # source
    def _setSourcePort_(self, portObject):
        if self._isSourcePort_(portObject) is False:
            self._sourcePortIndex = self._qry_getObjectIndex_(portObject)
            portObject._addTargetPort_(self)

    def connectFrom(self, portObject):
        assert isinstance(portObject, Abc_MtlOutput), u'''[ Argument Error ] "portObject" must object of Output'''
        self._setSourcePort_(portObject)

    def hasSource(self):
        return self._sourcePortIndex is not None

    def source(self):
        """
        :return: object of Output
        """
        if self.hasSource():
            return self._nodeObj.OBJ_mtl_obj_cache._object_(
                self._sourcePortIndex
            )

    def isConnectedFrom(self, portObject):
        return self._isSourcePort_(portObject)

    def _hasTargetPort_(self, portObject):
        return self._qry_getObjectIndex_(portObject) in self._targetPortnameIndexList

    # target
    def _addTargetPort_(self, portObject):
        if self._hasTargetPort_(portObject) is False:
            self._targetPortnameIndexList.append(
                self._qry_getObjectIndex_(portObject)
            )
            portObject._setSourcePort_(self)

    def connectTo(self, portObject):
        assert isinstance(portObject, Abc_MtlInput), u'''[ Argument Error ] "portObject" must object of "Input"'''
        self._addTargetPort_(portObject)

    def hasTargets(self):
        return self._targetPortnameIndexList != []

    def targets(self):
        if self.hasTargets():
            return [
                self._qry_getObject_(i)
                for i in self._targetPortnameIndexList
            ]

    def isConnectedTo(self, portObject):
        return self._hasTargetPort_(portObject)

    def hasParent(self):
        return self._parentPortnameString is not None

    def parent(self):
        if self.hasParent():
            return self._nodeObj.port(
                self._parentPortnameString
            )

    def hasChildren(self):
        """
        :return: bool
        """
        return self._childPortnameStringList != []

    def children(self):
        """
        :return: list(object of Port, ...)
        """
        if self.hasChildren():
            return [
                self._nodeObj.port(i)
                for i in self._childPortnameStringList
            ]

    def child(self, portnameString):
        if self.hasChildren():
            return self._nodeObj.port(portnameString)

    def hasChild(self, portnameString):
        return portnameString in self._childPortnameStringList

    def _queryKeyString_(self):
        return self.portString()

    def _xmlAttributeAttachValueString_(self):
        return self.portname().toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# port > input
class Abc_MtlInput(Abc_MtlPort):
    def _initAbcMtlInput(self, *args):
        self._initAbcMtlPort(*args)

    def _portGiven_(self):
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
            self._portGiven_()
        ]


# port > input > node input
class Abc_MtlNodeInput(Abc_MtlInput):
    def _initAbcMtlNodeInput(self, *args):
        self._initAbcMtlInput(*args)


# port > input > shader input
class Abc_MtlShaderInput(Abc_MtlInput):
    def _initAbcMtlShaderInput(self, *args):
        self._initAbcMtlInput(*args)

        self._nodeGraphOutputObj = None

    def _setNodeGraphOutput_(self, nodeGraphOutputObject):
        self._nodeGraphOutputObj = nodeGraphOutputObject

    def _getNodeGraphOutput_(self):
        return self._nodeGraphOutputObj

    def _portGiven_(self):
        if self.hasSource() is True:
            return self._getNodeGraphOutput_()
        return self.value()


# port > output
class Abc_MtlOutput(Abc_MtlPort):
    def _initAbcMtlOutput(self, *args):
        self._initAbcMtlPort(*args)

    def _xmlAttributeAttachValueString_(self):
        return self.portString()

    def _xmlAttributeAttaches_(self):
        if self.hasParent():
            return [
                self.parent(),
                (self._xmlAttributeAttachKeyString_(), self.portnameString())
            ]
        else:
            return [
                self.node(),
                (self._xmlAttributeAttachKeyString_(), self.portnameString())
            ]

    def _xmlAttributes_(self):
        return [
            self.portpath(),
            self.node(),
            self.porttype(),
            self.value()
        ]


# port > output > shader output
class Abc_MtlShaderOutput(Abc_MtlOutput):
    def _initAbcMtlShaderOutput(self, *args):
        self._initAbcMtlOutput(*args)


class Abc_MtlNodeOutput(Abc_MtlOutput):
    def _initAbcMtlNodeOutput(self, *args):
        self._initAbcMtlOutput(*args)


class Abc_MtlOutputChannel(Abc_MtlOutput):
    def _initAbcMtlOutputChannel(self, *args):
        self._initAbcMtlOutput(*args)


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
    def _initAbcMtlVisibility(self, *args):
        self._initAbcMtlPort(*args)

    def _xmlAttributes_(self):
        return [
            self.portpath(),
            self.value()
        ]


# object ************************************************************************************************************* #
class Abc_MtlObject(
    Def_MtlXml,
    mtlObjDefCore.Def_MtlObjCache
):
    CLS_mtl_type = None
    CLS_mtl_category = None

    CLS_mtl_node_string = None

    CLS_mtl_port_set = None

    CLS_mtl_source_node = None

    OBJ_mtl_query_cache = None
    OBJ_mtl_obj_cache = None

    VAR_mtl_port_class_dict = {}
    VAR_mtl_value_class_dict = {}

    def _initAbcMtlObject(self, categoryString, objectString):
        self._categoryObj = self.CLS_mtl_category(categoryString)
        self._nodeNameObj = self.CLS_mtl_node_string(objectString)

        typeString = self.OBJ_mtl_query_cache.nodeDef(categoryString).type
        self._typeObj = self.CLS_mtl_type(typeString)

        self._portSetObj = self.CLS_mtl_port_set(categoryString)
        self._inputSetObj = self.CLS_mtl_port_set(categoryString)
        self._outputSetObj = self.CLS_mtl_port_set(categoryString)

        self._initDefMtlObjCache(objectString)

        self.OBJ_mtl_obj_cache._addObject_(self)
        self._addPorts_(self.nodeString())

        self._initDefMtlXml()

    def _nodeStringObject_(self):
        return self._nodeNameObj

    def _typeObject(self):
        return self._typeObj

    def _setTypeString_(self, typeString):
        pass

    def _getPortObject_(self, portnameString, assignString):
        if assignString in self.VAR_mtl_port_class_dict:
            cls = self.VAR_mtl_port_class_dict[assignString]
            nodeObject = self
            return cls(nodeObject, portnameString)

    def _addPortObject_(self, portObject, portnameString, assignString):
        if assignString in [self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_input_channel]:
            self._inputSetObj._addObject_(portnameString, portObject)
        elif assignString in [self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_output_channel]:
            self._outputSetObj._addObject_(portnameString, portObject)
        self._portSetObj._addObject_(portnameString, portObject)

    def _addPorts_(self, objectString):
        def addPortFnc_(objectString_, portDefObject_):
            _portnameString = portDefObject_.portname
            _porttypeString = portDefObject_.porttype
            _portdataString = portDefObject_.portdata
            _assignString = portDefObject_.assign
            _parentPortnameString = portDefObject_.parent
            _childPortnameStrings = portDefObject_.children

            _attributeString = mtlMethods.Attribute.composeBy(
                objectString_, _portnameString
            )
            _portCls = self.VAR_mtl_port_class_dict[_assignString]
            _objKeyString = _portCls._toMtlObjKeyString_(_attributeString)
            if self.OBJ_mtl_obj_cache._hasObject_(_objKeyString) is False:
                _portObject = self._getPortObject_(_portnameString, _assignString)
                if _portObject is not None:
                    _portObject._setParentPortnameString_(_parentPortnameString)
                    _portObject._setChildPortnameStrings_(_childPortnameStrings)

                    self.OBJ_mtl_obj_cache._addObject_(_portObject)
            else:
                _portObject = self.OBJ_mtl_obj_cache._object_(_objKeyString)

            if _portObject is not None:
                _valueCls = self.VAR_mtl_value_class_dict[_porttypeString]

                _portObject._setValue_(_valueCls(_portdataString))
                _portObject._setDefaultValue_(_valueCls(_portdataString))

                self._addPortObject_(_portObject, _portnameString, _assignString)

        for i in self.OBJ_mtl_query_cache.nodeDef(self.categoryString()).ports:
            addPortFnc_(objectString, i)

    def type(self):
        """
        :return: str
        """
        return self._typeObj

    def typeString(self):
        return self._typeObj.toString()

    def _categoryObject(self):
        return self._categoryObj

    def category(self):
        return self._categoryObject()

    def categoryString(self):
        """
        :return: str
        """
        return self._categoryObject().toString()

    def nodeString(self):
        return self.nameString()

    def name(self):
        return self._nodeNameObj.name()

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
        return self._portSetObj._hasObject_(*args)

    def ports(self):
        return self._portSetObj.objects()

    def port(self, portString):
        return self._portSetObj.object(portString)

    def hasInputs(self):
        return self._inputSetObj.hasObjects()

    def hasInput(self, *args):
        return self._inputSetObj._hasObject_(*args)

    def inputs(self):
        """
        :return: list(object or attribute, ...)
        """
        return self._inputSetObj.objects()

    def input(self, portString):
        """
        :param portString: str
        :return: object of Port
        """
        return self._inputSetObj.object(portString)

    def valueChangedInputs(self):
        def _addFnc(portObject):
            if not portObject in lis:
                lis.append(portObject)

        lis = []
        for i in self.inputs():
            if i.hasParent():
                if i.hasSource():
                    _addFnc(i)
            else:
                if i.isValueChanged() or i.hasSource():
                    _addFnc(i)
        return lis

    def sourceNodes(self):
        return [i.source().node() for i in self.inputs() if i.hasSource()]

    def outputs(self):
        return self._outputSetObj.objects()

    def output(self, portString):
        return self._outputSetObj.object(portString)

    def toString(self):
        return self.nameString()

    def _queryKeyString_(self):
        return self.nameString()


# object > node
class Abc_MtlNode(Abc_MtlObject):
    def _initAbcMtlNode(self, *args):
        self._initAbcMtlObject(*args)

    def _xmlElementString_(self):
        return self.categoryString()

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.type()
        ]

    def _xmlChildren_(self):
        return self.valueChangedInputs()

    def _xmlAttributeAttachValueString_(self):
        return self.nameString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# object > shader
class Abc_MtlShader(Abc_MtlObject):
    CLS_mtl_node_graph = None
    CLS_mtl_node_graph_set = None

    def _initAbcMtlShader(self, *args):
        categoryString, nodeString = args[:2]

        self._initAbcMtlObject(*args)

        self._nodeGraphSetObj = self.CLS_mtl_node_graph_set(nodeString)
        self._addNodeGraph_()

    def _updateNodeGraphs_(self):
        if self.hasNodeGraphs():
            nodeGraphObject = self.nodeGraph(0)

            material = self._getMaterial_()
            if material is not None:
                nodeGraphObject.name()._setXmlNameSuffixString_(
                    '{}__{}__nodegraph'.format(
                        material.name()._xmlNameSuffixString_(), self._getMaterialTarget_().portnameString()
                    )
                )

            nodeGraphObject._update_(self)

    def _addNodeGraph_(self):
        nodeGraphObject = self.CLS_mtl_node_graph()

        nodeGraphObject.setNameString(
            self.nameString()
        )
        self._nodeGraphSetObj.addObject(nodeGraphObject)

    def hasNodeGraphs(self):
        return self._nodeGraphSetObj.hasObjects()

    def hasNodeGraph(self, nameString):
        return self._nodeGraphSetObj._hasObject_(nameString)

    def nodeGraph(self, nameString):
        return self._nodeGraphSetObj._object_(nameString)

    def _getMaterialTarget_(self):
        for i in self.outputs():
            if i.hasTargets():
                targets = i.targets()
                for target in targets:
                    targetNode = target.node()
                    if isinstance(targetNode, Abc_MtlMaterial):
                        return target

    def _getMaterial_(self):
        for i in self.outputs():
            if i.hasTargets():
                targets = i.targets()
                for target in targets:
                    targetNode = target.node()
                    if isinstance(targetNode, Abc_MtlMaterial):
                        return targetNode

    def nodeGraphs(self):
        return self._nodeGraphSetObj.objects()

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.category(),
            self._getMaterialTarget_()
        ]

    def _xmlChildren_(self):
        return self.valueChangedInputs()


# material
class Abc_MtlMaterial(Abc_MtlObject):
    def _initAbcMtlMaterial(self, *args):
        nodeString = args[0]
        self._initAbcMtlObject(
            self.DEF_mtl_category_material,
            nodeString
        )

    def surfaceInput(self):
        return self.port(u'surfaceshader')

    def displacementInput(self):
        return self.port(u'displacementshader')

    def volumeInput(self):
        return self.port(u'volumeshader')

    def connectSurfaceFrom(self, portObject):
        self.surfaceInput().connectFrom(portObject)

    def surfaceShader(self):
        if self.surfaceInput().hasSource():
            return self.surfaceInput().source().node()

    def connectDisplacementFrom(self, portObject):
        self.displacementInput().connectFrom(portObject)

    def displacementShader(self):
        if self.displacementInput().hasSource():
            return self.displacementInput().source().node()

    def connectVolumeFrom(self, portObject):
        self.volumeInput().connectFrom(portObject)

    def volumeShader(self):
        if self.volumeInput().hasSource():
            return self.volumeInput().source().node()

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
        for s in self.shaders():
            s._updateNodeGraphs_()

        return self.shaders()

    def _xmlElements_(self):
        lis = []
        for s in self.shaders():
            nodeGraphs = s.nodeGraphs()
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


# object > dag
class Abc_MtlDag(Abc_MtlObject):
    CLS_mtl_child_set = None

    def _initAbcMtlDag(self, *args):
        categoryString, nodeString = args[:2]

        self._nodeNameObj = self.CLS_mtl_node_string(nodeString)
        self._childSetObj = self.CLS_mtl_child_set(nodeString)

        self._initAbcMtlObject(*args)

    def nodeString(self):
        return self._nodeNameObj.nodeString()

    def dagpath(self):
        """
        :return: object of Dagpath
        """
        return self._nodeNameObj

    def fullpathName(self):
        """
        :return: str
        """
        return self._nodeNameObj.nodeString()

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
    CLS_mtl_property_set = None
    CLS_mtl_visibility_set = None
    CLS_mtl_propertyset = None

    CLS_mtl_material_set = None

    def _initAbcMtlGeometry(self, *args):
        categoryString, nodeString = self.DEF_mtl_category_geometry, args[0]

        self._propertySetObj = self.CLS_mtl_property_set(nodeString)
        self._visibilitySetObj = self.CLS_mtl_visibility_set(nodeString)

        self._initAbcMtlDag(
            categoryString,
            nodeString
        )

        self._materialSetObj = self.CLS_mtl_material_set(nodeString)
        self._propertysetObj = self.CLS_mtl_propertyset(nodeString)

    def _addPortObject_(self, portObject, portnameString, assignString):
        if assignString in [self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_input_channel]:
            self._inputSetObj._addObject_(portnameString, portObject)
        elif assignString in [self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_output_channel]:
            self._outputSetObj._addObject_(portnameString, portObject)
        elif assignString == self.DEF_mtl_keyword_property:
            self._propertySetObj._addObject_(portnameString, portObject)
            self._inputSetObj._addObject_(portnameString, portObject)
        elif assignString == self.DEF_mtl_keyword_visibility:
            self._visibilitySetObj._addObject_(portnameString, portObject)
            self._inputSetObj._addObject_(portnameString, portObject)

        self._portSetObj._addObject_(portnameString, portObject)

    def _updatePropertyset_(self):
        self._propertysetObj._initializeSets_()

        for i in self.valueChangedProperties():
            self._propertysetObj.addPort(i)

    def property(self, portnameString):
        return self._propertySetObj.object(portnameString)

    def hasProperty(self, *args):
        return self._propertySetObj._hasObject_(*args)

    def properties(self):
        return self._propertySetObj.objects()

    def valueChangedProperties(self):
        lis = []
        for i in self.properties():
            if i.isValueChanged():
                lis.append(i)
        return lis

    def visibility(self, portnameString):
        return self._visibilitySetObj.object(portnameString)

    def hasVisibility(self, *args):
        return self._visibilitySetObj._hasObject_(*args)

    def visibilities(self):
        return self._visibilitySetObj.objects()

    def valueChangedVisibilities(self):
        lis = []
        for i in self.visibilities():
            if i.isValueChanged():
                lis.append(i)
        return lis

    def addMaterial(self, materialObject):
        self._materialSetObj._addObject_(materialObject)

    def materials(self):
        return self._materialSetObj.objects()

    def setPropertyset(self, propertysetObject):
        self._propertysetObj = propertysetObject

    def propertyset(self):
        return self._propertysetObj

    def toString(self):
        return self.nodeString()

    def _queryKeyString_(self):
        return self.nodeString()

    def _xmlAttributes_(self):
        return [
            self.dagpath()
        ]

    def _xmlChildren_(self):
        return self.valueChangedInputs()

    def _xmlAttributeAttachValueString_(self):
        return self.nodeString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# portset
class Abc_MtlPortset(Def_MtlXml):
    CLS_mtl_name = None

    CLS_mtl_port_set = None
    
    def _initAbcMtlPortset(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._portSetObj = self.CLS_mtl_port_set()

        self._initDefMtlXml()

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


# node graph output
class Abc_MtlNodeGraphOutput(Def_MtlXml):
    CLS_mtl_name = None

    def _initAbcMtlNodeGraphOutput(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._portObj = None

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

    def port(self):
        return self._portObj

    def porttype(self):
        return self._portObj.porttype()

    def nodeGraph(self):
        return self._nodeGraphObj

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.porttype(),
            self.port()
        ]

    def _xmlAttributeAttachValueString_(self):
        return self.name()._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            self.nodeGraph(),
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# node graph
class Abc_MtlNodeGraph(Def_MtlXml):
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

        self._initDefMtlXml()

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

    def _addNode_(self, *args):
        if isinstance(args[0], (str, unicode)):
            nodeObject = self.CLS_mtl_node(*args)
        else:
            nodeObject = args[0]

        if self._nodeSetObj._hasObject_(nodeObject) is False:
            self._nodeSetObj.addObject(nodeObject)

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

    def _addPort_(self, *args):
        portObject = args[0]

        sourceObject = portObject.source()
        count = self._nodeGraphOutputSetObj.objectCount()

        keyString = sourceObject.attributeString()
        if self._nodeGraphOutputSetObj._hasObject_(keyString) is False:
            nameString = u'output_{}'.format(count)
            nodeGraphOutputObject = self.CLS_mtl_node_graph_output(nameString)
            nodeGraphOutputObject._setPort_(sourceObject)
            nodeGraphOutputObject._setNodeGraph_(self)
            self._nodeGraphOutputSetObj._addObject_(keyString, nodeGraphOutputObject)
        else:
            nodeGraphOutputObject = self._nodeGraphOutputSetObj._object_(keyString)

        portObject._setNodeGraphOutput_(nodeGraphOutputObject)

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

    def node(self, nodeString):
        """
        :param nodeString: str("nodeString")
        :return: <Node>
        """
        return self._nodeSetObj._object_(nodeString)

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

    def output(self, portString):
        """
        :param portString: str
        :return: object of Output
        """
        return self._nodeGraphOutputSetObj.object(portString)

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


# geometry collection
class Abc_MtlCollection(Def_MtlXml):
    CLS_mtl_name = None

    CLS_mtl_geometry_set = None
    CLS_set_collection = None

    DEF_geometry_separator = None

    def _initAbcMtlCollection(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_mtl_geometry_set()
        self._collectionSetObj = self.CLS_set_collection()
        self._excludeGeometrySetObj = self.CLS_mtl_geometry_set()

        self._initDefMtlXml()

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
        return [i.nodeString() for i in self.geometries()]

    def fullpathGeometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nodeString() for i in self.geometries()]

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


class Abc_MtlAssign(Def_MtlXml):
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

        self._initDefMtlXml()

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
        self._nameObj.createByString(nameString)

    def _addGeometry_(self, *args):
        geometryObject = args[0]
        self._geometrySetObj.addObject(geometryObject)

    def hasGeometry(self, *args):
        return self._geometrySetObj._hasObject_(*args)

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
        return [i.nodeString() for i in self.geometries()]

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

        self._materialObj = None

    def setMaterial(self, materialObject):
        """
        :param materialObject: object of Material
        :return:
        """
        self._materialObj = materialObject

    def material(self):
        """
        :return: object of ShaderSet
        """
        return self._materialObj

    def _xmlElementAttaches_(self):
        return [
            self._materialObj,
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


class Abc_MtlVisibility(Abc_MtlAssign):
    CLS_mtl_type = None
    CLS_value_visibility = None

    CLS_set_geometry_viewer = None

    OBJ_mtl_query_cache = None

    def _initAbcMtlVisibility(self, *args):
        self._initAbcMtlAssign(*args)

        self._vistypeObj = None

        self._visibilityValueObj = None

        self._viewerGeometrySetObj = self.CLS_set_geometry_viewer()

    def type(self):
        return self._vistypeObj

    def setTypeString(self, portnameString):
        self._vistypeObj = self.CLS_mtl_type(portnameString)

        portdataString = self.OBJ_mtl_query_cache.nodeDef(self.DEF_mtl_category_geometry).port(portnameString).portdata

        self._visibilityValueObj = self.CLS_value_visibility(portdataString)

    def typeString(self):
        return self._vistypeObj.toString()

    def visible(self):
        return self._visibilityValueObj

    def setGeometryVisibility(self, geometryVisibilityObject):
        visibilityString = geometryVisibilityObject.portString()
        self._vistypeObj = self.CLS_mtl_type(visibilityString)

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


class Abc_MtlLook(Def_MtlXml):
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

        self._initDefMtlXml()

    def _addGeometry_(self, *args):
        geometryObject = args[0]
        self._geometrySetObj.addObject(geometryObject)

    def _updateAssigns_(self):
        for i in self._geometrySetObj.objects():
            self._addGeometryMaterialAssigns_(i)
            self._addGeometryPropertyAssigns_(i)
            self._addGeometryVisibilities_(i)

    def _addGeometryMaterialAssigns_(self, geometryObject):
        def addFnc_(geometryObject_, materialObject_):
            materialObject_.name()._setXmlNameSuffixString_(
                '__{}__material'.format(self.nameString())
            )
            _count = self._materialAssignSetObj.objectCount()
            _keyString = materialObject_.nodeString()
            if self._materialAssignSetObj._hasObject_(_keyString):
                _materialAssignObject = self._materialAssignSetObj._object_(_keyString)
            else:
                _materialAssignObject = self.CLS_mtl_material_assign(
                    'material_assign_{}'.format(_count)
                )
                _materialAssignObject.setMaterial(materialObject_)
                self._materialAssignSetObj._addObject_(_keyString, _materialAssignObject)

            if _materialAssignObject.hasGeometry(geometryObject_) is False:
                _materialAssignObject.addGeometry(geometryObject_)

        [addFnc_(geometryObject, i) for i in geometryObject.materials()]

    def _addGeometryPropertyAssigns_(self, geometryObject):
        def addFnc_(geometryObject_, propertysetObject_):
            propertysetObject_.name()._setXmlNameSuffixString_(
                '__{}__propertyset'.format(self.nameString())
            )

            _count = self._propertysetAssignSetObj.objectCount()
            _keyString = geometryObject_.nodeString()
            if self._propertysetAssignSetObj._hasObject_(_keyString):
                _propertysetAssignObject = self._propertysetAssignSetObj._object_(_keyString)
            else:
                _propertysetAssignObject = self.CLS_mtl_propertyset_assign(
                    'propertyset_assign_{}'.format(_count)
                )
                self._propertysetAssignSetObj._addObject_(_keyString, _propertysetAssignObject)

            _propertysetAssignObject.setPropertyset(propertysetObject_)
            if _propertysetAssignObject.hasGeometry(geometryObject_) is False:
                _propertysetAssignObject.addGeometry(geometryObject_)

        geometryObject._updatePropertyset_()
        propertysetObject = geometryObject.propertyset()
        if propertysetObject.hasPorts():
            addFnc_(geometryObject, propertysetObject)

    def _addGeometryVisibilities_(self, geometryObject):
        def addFnc_(geometryObject_, portObject_):
            _count = self._visibilitySetObj.objectCount()
            _keyString = portObject_.portString()
            if self._visibilitySetObj._hasObject_(_keyString):
                _visibilityObject = self._visibilitySetObj._object_(_keyString)
            else:
                _visibilityObject = self.CLS_mtl_visibility(
                    'visibility_{}'.format(_count)
                )
                _visibilityObject.setGeometryVisibility(portObject_)
                self._visibilitySetObj._addObject_(_keyString, _visibilityObject)

            if _visibilityObject.hasGeometry(geometryObject_) is False:
                _visibilityObject.addGeometry(geometryObject_)

        geometryVisibilities = geometryObject.valueChangedVisibilities()
        if geometryVisibilities:
            [addFnc_(geometryObject, i) for i in geometryVisibilities]

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def geometries(self):
        return self._geometrySetObj.objects()

    def hasGeometries(self):
        return self._geometrySetObj.hasObjects()

    def addGeometry(self, geometryObject):
        self._addGeometry_(geometryObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (tuple, list)):
            [self.addGeometry(i) for i in list(args[0])]
        else:
            [self.addGeometry(i) for i in list(args)]

    def geometry(self, geometryString):
        return self._geometrySetObj.object(geometryString)

    def hasGeometry(self, *args):
        return self._geometrySetObj._hasObject_(*args)

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


class Abc_MtlFile(Def_MtlXml):
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

        self._initDefMtlXml()

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
        self._lookSetObj._addObject_(keyString, fileObject)

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
        return self._lookSetObj._hasObject_(lookString)

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


class Abc_MtlTrsBasic(mtlConfigure.Utility):
    def _initAbcMtlTrsBasic(self):
        pass


# translate node def
class Abc_MtlTrsObject(Abc_MtlTrsBasic):
    CLS_mtl_object = None
    CLS_mtl_dcc_object = None

    OBJ_mtl_query_cache = None
    OBJ_mtl_dcc_query_cache = None

    OBJ_mtl_obj_cache = None

    def _initAbcMtlTrsObject(self, *args):
        dccNodeString = args[0]

        self._dccNodeString = dccNodeString
        self._dccNodeObj = self.CLS_mtl_dcc_object(self._dccNodeString)
        self._dccCategoryString = self._dccNodeObj.category()

        self._mtlCategoryString = self.OBJ_mtl_dcc_query_cache.dccNodeDef(self._dccCategoryString).category
        self._mtlNodeString = self._translateNodeString_(self._dccNodeObj.nodeString())

        self._getMtlNode_()

        self._translatePorts_()
        self._runAfterExpression_()

    def _translateNodeString_(self, nodeString):
        return nodeString.replace(self.DEF_mya_node_separator, self.DEF_mtl_node_separator)

    def _translatePorts_(self):
        def getPortFnc_(dccObjectDefObject_):
            _dccPortnameString = dccObjectDefObject_.dccPortname
            _portnameString = dccObjectDefObject_.portname

            if self._dccNodeObj.hasPort(_dccPortnameString):
                _dccPortObject = self._dccNodeObj.port(_dccPortnameString)
                _portObject = self._mtlNodeObj.port(_portnameString)

                updatePortGivenFnc_(_dccPortObject, _portObject)

        def updatePortGivenFnc_(dccPortObject_, portObject_):
            if dccPortObject_.hasSource():
                updatePortSourceFnc_(dccPortObject_, portObject_)
            else:
                updatePortdataFnc_(dccPortObject_, portObject_)

        def updatePortSourceFnc_(dccPortObject_, portObject_):
            _dccSource = dccPortObject_.source()
            _dccSourceNode = _dccSource.node()

            _dccSourceNodeString = _dccSourceNode.nodeString()
            _dccSourceCategoryString = _dccSourceNode.category()
            _dccObjectDefObject = self.OBJ_mtl_dcc_query_cache.dccNodeDef(_dccSourceCategoryString)
            _sourceCategoryString = _dccObjectDefObject.category
            _dccSourcePortnameString = _dccSource.portString()
            _sourcePortnameString = _dccObjectDefObject.dccOutput(_dccSourcePortnameString).portname

            _sourceNodeString = self._translateNodeString_(_dccSourceNodeString)
            _sourceNode = getSourceNodeFnc_(_sourceCategoryString, _sourceNodeString)

            _source = _sourceNode.output(_sourcePortnameString)

            portObject_.connectFrom(_source)

        def getSourceNodeFnc_(categoryString_, nodeString_):
            _nodeCls = self._mtlNodeObj.CLS_mtl_source_node
            if _nodeCls is None:
                _nodeCls = self._mtlNodeObj.__class__

            _objKeyString = _nodeCls._toMtlObjKeyString_(nodeString_)
            if self.OBJ_mtl_obj_cache._hasObject_(_objKeyString) is True:
                _nodeObject = self.OBJ_mtl_obj_cache._object_(_objKeyString)
            else:
                _nodeObject = _nodeCls(categoryString_, nodeString_)
            return _nodeObject

        def updatePortdataFnc_(dccPortObject_, portObject_):
            portObject_.setPortdata(dccPortObject_.portdata())

        for i in self.OBJ_mtl_dcc_query_cache.dccNodeDef(self._dccCategoryString).dccPorts:
            getPortFnc_(i)

    def _runAfterExpression_(self):
        afterExpression = self.OBJ_mtl_dcc_query_cache.dccNodeDef(self._dccCategoryString).afterExpression
        if afterExpression:
            commands = afterExpression['command']
            if commands:
                cmdsStr = ';'.join(commands)
                exec cmdsStr

    def getMtlPortdata(self, portnameString):
        pass

    def setMtlPortdata(self, portnameString, portdata):
        pass

    def setMtlPortSource(self, source):
        pass

    def _getMtlNode_(self):
        nodeCls = self.CLS_mtl_object
        nodeString = self._mtlNodeString
        objKeyString = nodeCls._toMtlObjKeyString_(nodeString)
        if self.OBJ_mtl_obj_cache._hasObject_(objKeyString) is True:
            self._mtlNodeObj = self.OBJ_mtl_obj_cache._object_(objKeyString)
        else:
            self._mtlNodeObj = self.CLS_mtl_object(
                self._mtlCategoryString,
                self._mtlNodeString
            )

    def dccNode(self):
        return self._dccNodeObj

    # materialx
    def mtlNode(self):
        return self._mtlNodeObj

    def mtlCategoryString(self):
        return self._mtlCategoryString

    def __str__(self):
        return self._mtlNodeObj.__str__()


# translate node
class Abc_MtlTrsNode(Abc_MtlTrsObject):
    def _initAbcMtlTrsNode(self, *args):
        self._initAbcMtlTrsObject(*args)


# translate node graph
class Abc_MtlTrsNodeGraph(Abc_MtlTrsBasic):
    CLS_mtl_node_graph = None
    CLS_mtl_dcc_node_graph = None

    CLS_mtl_trs_node = None

    OBJ_mtl_query_cache = None
    OBJ_mtl_dcc_query_cache = None

    def _initAbcMtlTrsNodeGraph(self, *args):
        self._dccNodeObj = args[0]

        self._getMtlNodes_()

    def _getMtlNodes_(self):
        dccNodeGraph = self._dccNodeObj.nodeGraph()
        dccNodes = dccNodeGraph.nodes()
        for i in dccNodes:
            dccCategoryString = i.category()
            if self.OBJ_mtl_dcc_query_cache.hasDccCategory(dccCategoryString):
                dccObjectString = i.nodeString()
                trsNode = self.CLS_mtl_trs_node(dccObjectString)
            else:
                bscMethods.PyMessage.traceWarning(
                    u'''DCC Category "{}" is Unregistered!!!'''.format(dccCategoryString)
                )


# translate shader
class Abc_MtlTrsShader(Abc_MtlTrsObject):
    CLS_mtl_trs_node_graph = None

    def _initAbcMtlTrsShader(self, *args):
        self._initAbcMtlTrsObject(*args)

        self._getMtlNodeGraphs_()

    def _getMtlNodeGraphs_(self):

        trsNodeGraph = self.CLS_mtl_trs_node_graph(self._dccNodeObj)

        self._mtlNodeObj._updateNodeGraphs_()


# translate material
class Abc_MtlTrsMaterial(Abc_MtlTrsObject):
    CLS_mtl_trs_shader = None

    def _initAbcMtlTrsMaterial(self, *args):
        self._initAbcMtlTrsObject(*args)

        self._getMtlShaders_()

    def _getMtlNode_(self):
        self._mtlNodeObj = self.CLS_mtl_object(
            self._dccNodeObj.nodeString()
        )

    def _getMtlShaders_(self):
        dccShaders = self._dccNodeObj.shaders()
        for i in dccShaders:
            dccObjectString = i.nodeString()
            trsShader = self.CLS_mtl_trs_shader(dccObjectString)


# translate geometry
class Abc_MtlTrsGeometry(Abc_MtlTrsObject):
    CLS_mtl_trs_material = None

    def _initAbcMtlTrsGeometry(self, *args):
        self._initAbcMtlTrsObject(*args)

        self._getMtlMaterials_()

    def _getMtlNode_(self):
        self._mtlNodeObj = self.CLS_mtl_object(
            self._mtlNodeString
        )

    def _getMtlMaterials_(self):
        dccMaterials = self._dccNodeObj.materials()

        for i in dccMaterials:
            dccObjectString = i.nodeString()
            trsMaterialObject = self.CLS_mtl_trs_material(dccObjectString)
            materialObject = trsMaterialObject.mtlNode()
            self._mtlNodeObj.addMaterial(materialObject)


class Abc_MtlTrsLook(mtlConfigure.Utility):
    CLS_mtl_look = None
    CLS_trs_geometry = None
    def _initAbcMtlTrsLook(self, *args):
        self._mtlLookObj = self.CLS_mtl_look(*args)

    def mtlNode(self):
        return self._mtlLookObj

    def addDccGeometry(self, geometryString):
        trsGeometry = self.CLS_trs_geometry(geometryString)
        mtlGeometryObject = trsGeometry.mtlNode()
        if self._mtlLookObj.hasGeometry(mtlGeometryObject) is False:
            self._mtlLookObj.addGeometry(mtlGeometryObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Geometry "{}" is Exist.'''.format(mtlGeometryObject.nodeString())
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


class Abc_MtlTrsFile(mtlConfigure.Utility):
    CLS_mtl_file = None
    CLS_trs_geometry = None
    CLS_trs_look = None

    def _initAbcMtlTrsFile(self, *args):
        fileString = args[0]
        self._mtlFileObj = self.CLS_mtl_file(fileString)
        self._mtlFileObj.addReference(u'materialx/arnold/nodedefs.mtlx')

    def addLook(self, lookString):
        trsLookObject = self.CLS_trs_look(lookString)
        if self._mtlFileObj.hasLook(lookString) is False:
            lookObject = trsLookObject.mtlNode()
            self._mtlFileObj.addLook(lookObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Look "{}" is Exist.'''.format(lookString)
            )
        return trsLookObject

    def look(self, lookString):
        return self._mtlFileObj.look(lookString)

    def __str__(self):
        return self._mtlFileObj.__str__()

    def save(self):
        self._mtlFileObj.save()
        bscMethods.PyMessage.traceResult(
            u'save file "{}"'.format(self._mtlFileObj.fullpathFilename())
        )
