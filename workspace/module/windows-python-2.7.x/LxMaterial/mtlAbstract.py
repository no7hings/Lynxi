# coding:utf-8
from LxMaterial import mtlConfigure, mtlCore


class Def_Xml(mtlCore.Basic):
    xml_separator_attribute = u' '

    STR_mtlx_key_element = u''
    STR_mtlx_key_attribute = u''

    def _initDefXml(self):
        self._xmlIndentStr = ''

    def _xmlElementKeyString(self):
        return self.STR_mtlx_key_element

    def _xmlAttributeKeyString(self):
        return self.STR_mtlx_key_attribute

    def _xmlAttributeValueString(self):
        pass

    @property
    def _xmlIndentString(self):
        return self._xmlIndentStr

    @_xmlIndentString.setter
    def _xmlIndentString(self, string):
        self._xmlIndentStr = string

    def _xmlNameString(self):
        pass

    def _xmlAttributeLis(self):
        pass

    def _xmlChildList(self):
        pass

    def _xmlElementList(self):
        pass

    def _xmlAttributeRaw(self):
        pass

    @classmethod
    def _toXmlString(cls, elementObject, indent=4):
        def addPrefixFnc_(prefix_, lString, rString):
            lis.append(u'{}<{}{}'.format(lString, prefix_, rString))

        def addAttributeFnc_(attributeObject_, lString, rString):
            if attributeObject_ is not None:
                if isinstance(attributeObject_, Def_Xml):
                    attributeRaw = attributeObject_._xmlAttributeRaw()
                else:
                    attributeRaw = attributeObject_

                if attributeRaw:
                    for k, v in attributeRaw:
                        lis.append(u'{}{}="{}"{}'.format(lString, k, v, rString))

        def addBranchFnc_(elementObject_, rString, parentElementObject=None):
            if parentElementObject is not None:
                lString = elementObject_._xmlIndentString
            else:
                lString = ''

            elementTagString = elementObject_._xmlElementKeyString()
            addPrefixFnc_(elementTagString, lString=lString, rString='')
            # Attribute
            attributes = elementObject_._xmlAttributeLis()
            if attributes:
                [addAttributeFnc_(i, lString=cls.xml_separator_attribute, rString='') for i in attributes]
            # Children
            children = elementObject_._xmlChildList()
            if children:
                lis.append(u'>\r\n')

                for i in children:
                    i._xmlIndentString = lString + defIndentString
                    addBranchFnc_(i, rString=rString, parentElementObject=elementObject_)

                lis.append(u'{}</{}>\r\n'.format(lString, elementTagString))
            else:
                lis.append(u'{}/>\r\n'.format(cls.xml_separator_attribute))

            elements = elementObject_._xmlElementList()
            if elements:
                for i in elements:
                    i._xmlIndentString = lString
                    addBranchFnc_(i, rString=u'', parentElementObject=elementObject_)

        defIndentString = u' ' * indent
        lis = [
            u'<?xml version="1.0"?>\r\n',
        ]

        addBranchFnc_(elementObject, rString='')
        return u''.join(lis)

    def __str__(self):
        return self._toXmlString(self)


class Abc_Raw(Def_Xml):
    def _initAbcRaw(self, *args):
        if args:
            self._raw = args[0]
            self._rawType = type(self._raw)
        else:
            self._raw = None
            self._rawType = None

        self._initDefXml()

    def _initAbcRawDatum(self):
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

    def _xmlAttributeRaw(self):
        """
        :return: dict
        """
        return [
            (self._xmlAttributeKeyString(), self.toString())
        ]

    def __eq__(self, other):
        """
        :param other: typed raw
        :return: bool
        """
        return self.toString() == other.toString()


class Abc_Path(Abc_Raw):
    CLS_raw = None

    STR_separator = None

    def _initAbcPath(self, *args):
        self._initAbcRaw(*args)

        if self.hasRaw():
            self._rawLis = [self.CLS_raw(i) for i in self._raw.split(self.STR_separator)]
        else:
            self._rawLis = None

    @staticmethod
    def _toStringsMethod(pathString, pathsep):
        if pathString.startswith(pathsep):
            return pathString.split(pathsep)[1:]
        else:
            return pathString.split(pathsep)

    def createByRaw(self, *args):
        raw = args[0]
        self._rawLis = [self.CLS_raw(i) for i in raw.split(self.STR_separator)]

    def createByString(self, *args):
        raw = args[0]
        self._rawLis = [self.CLS_raw(i) for i in raw.split(self.STR_separator)]

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._rawLis[-1].setRaw(nameString)

    def nameString(self):
        """
        :return: str
        """
        if self.hasRaw():
            return self._rawLis[-1].raw()

    def fullpathName(self):
        """
        :return: str
        """
        return self.toString()

    def toString(self):
        """
        :return: str
        """
        return self.STR_separator.join([i.toString() for i in self._rawLis])

    def pathsep(self):
        """
        :return: str
        """
        return self.STR_separator


class Abc_ShadersetPath(Abc_Path):
    def _initAbcShadersetPath(self, *args):
        self._initAbcPath(*args)

    def _xmlNameString(self):
        return self.fullpathName()

    def _xmlAttributeRaw(self):
        """
        :return: dict
        """
        return [
            (self._xmlAttributeKeyString(), self._xmlNameString())
        ]


class Abc_Set(Def_Xml):
    STR_separator_object = ','
    # noinspection PyUnusedLocal
    def _initAbcSet(self, *args):
        self._objectLis = []
        self._objectDic = {}
        self._objectCount = 0

        self._objectFilterStr = None

        self._initDefXml()

    def createByRaw(self, *args):
        pass

    def objects(self):
        """
        :return: list(object, ...)
        """
        return self._objectLis

    def hasObjects(self):
        """
        :return: bool
        """
        return self._objectLis != []

    def objectsCount(self):
        """
        :return: int
        """
        return self._objectCount

    def addObject(self, keyString, obj):
        """
        :param keyString: str(query key)
        :param obj: object of typed
        :return: 
        """
        assert keyString not in self._objectDic, '''Key is Exist.'''
        self._objectLis.append(obj)
        self._objectDic[keyString] = obj
        self._objectCount += 1

    def objectAt(self, index):
        """
        :param index: int
        :return: object
        """
        return self._objectLis[index]

    def hasObjectAt(self, index):
        """
        :param index: int
        :return: object
        """
        pass

    def hasObject(self, obj):
        """
        :return: bool
        """
        return obj in self._objectLis

    def objectWithKey(self, keyString):
        """
        :param keyString: str
        :return: bool
        """
        assert keyString in self._objectDic, u'''Key is Non - Exist.'''
        return self._objectDic[keyString]

    def hasObjectWithKey(self, keyString):
        """
        :param keyString: str
        :return: bool
        """
        return keyString in self._objectDic

    def toString(self):
        """
        :return: str
        """
        return self.STR_separator_object.join([i.toString() for i in self.objects()])

    def __len__(self):
        """
        :return: int
        """
        return self.objectsCount()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.toString())
        ]


class Abc_RawString(Abc_Raw):
    def _initAbcRawString(self, *args):
        self._initAbcRaw(*args)

    def toString(self):
        """
        :return: str
        """
        return unicode(self._raw)

    def _xmlAttributeRaw(self):
        """
        :return: dict
        """
        return [
            (self._xmlAttributeKeyString(), self.toString())
        ]


class Abc_RawDatum(Abc_Raw):
    CLS_raw = None

    raw_type = None

    raw_def = None

    def _initAbcRawDatum(self, *args):
        self._initAbcRaw()

        if isinstance(args[0], Abc_Value):
            self._valueObj = args[0]
            self._valueTypeStringPattern = self._valueObj.value_type_string_pattern
            self._valueSizePattern = self._valueObj.value_size_pattern
        elif isinstance(args[0], Abc_RawDatumset):
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
        assert args is not (), u'Argument must not be Empty.'

        if isinstance(args[0], (str, unicode)):
            self.createByString(*args)
        else:
            self.createByRaw(*args)

    def createByRaw(self, *args):
        """
        :param args: raw of typed
        :return: None
        """
        assert args is not (), u'Argument must not be Empty.'
        raw = args[0]
        assert isinstance(raw, self.raw_type), u'Argument Error, "arg" Must "{}".'.format(self.raw_type)

        self.setRaw(self.CLS_raw(raw))

    def createByString(self, *args):
        """
        :param args: str
        :return: None
        """
        assert args is not (), u'Argument must not be Empty.'
        assert isinstance(args[0], (str, unicode))
        if args[0]:
            self.createByRaw(self.CLS_raw(args[0]))

    def toString(self):
        return unicode(self._raw)

    def typeString(self):
        return self._valueTypeStringPattern[0]

    def valueSize(self):
        return self._valueSizePattern[0]

    def _toPrintString(self):
        if self.typeString() is not None:
            return '{}({})'.format(self.typeString(), self.toString())
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.toString())
        ]


class Abc_RawDatumset(Abc_Raw):
    CLS_set_child = None

    datum_string_separator = None

    raw_def = None

    def _initAbcRawDatumset(self, *args):
        self._initAbcRawDatum()

        if isinstance(args[0], Abc_Value):
            self._valueObj = args[0]
            self._valueTypeStringPattern = self._valueObj.value_type_string_pattern
            self._valueSizePattern = self._valueObj.value_size_pattern
        elif isinstance(args[0], Abc_RawDatumset):
            self._datumNObj = args[0]
            self._valueTypeStringPattern = self._datumNObj._valueTypeStringPattern[1:]
            self._valueSizePattern = self._datumNObj._valueSizePattern[1:]

        self._childLis = []
        self.create(*args[1:])

    def create(self, *args):
        assert args is not (), u'Argument must not be Empty.'

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
        assert args is not (), u'Argument must not be Empty.'
        if isinstance(args[0], (tuple, list)):
            raw = list(args[0])
        else:
            raw = args

        [self.addChild(self.CLS_set_child(self, i)) for i in raw]

        self.setRaw(raw)

    def createByString(self, *args):
        assert args is not (), u'Argument must not be Empty.'
        assert isinstance(args[0], (str, unicode))
        if args[0]:
            valueStringLis = [i.lstrip().rstrip() for i in args[0].split(mtlConfigure.Separator_Raw_Basic)]
            raw = self.toListSplit(valueStringLis, self.childValueSize())
            self.createByRaw(raw)

    def toString(self):  # to override
        """
        :return: str
        """
        return self.datum_string_separator.join([i.toString() for i in self.children()])

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

    def addChild(self, datumObject):
        """
        :param datumObject: object of Datum
        :return: None
        """
        self._childLis.append(datumObject)

    def children(self):
        """
        :return: list(object of Datum)
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
        :param index: object of Datum
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
            return '{}({})'.format(self.typeString(), self.datum_string_separator.join([i._toPrintString() for i in self.children()]))
        return self.datum_string_separator.join([i._toPrintString() for i in self.children()])

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.toString())
        ]

    def __len__(self):
        """
        :return: int
        """
        return self.childrenCount()


class Abc_Value(Def_Xml):
    CLS_raw_type = None
    CLS_raw_datum = None

    value_type_string_pattern = None
    sub_value_type_string = None

    value_size_pattern = None

    def _initAbcValue(self, *args):
        self._typeObj = self.CLS_raw_type(self.value_type_string_pattern[0])
        self._datumObj = self.CLS_raw_datum(self, *args)

        self._initDefXml()

    def type(self):
        """
        :return: object of Type
        """
        return self._typeObj

    def typeString(self):
        """
        :return: str
        """
        return self._typeObj.toString()

    def datum(self):
        """
        :return: object of Datum
        """
        return self._datumObj

    def raw(self):
        """
        :return: raw of typed
        """
        return self._datumObj.raw()

    def hasRaw(self):
        """
        :return: bool
        """
        return self._datumObj.hasRaw()

    def toString(self):
        """
        :return: str
        """
        return self._datumObj.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._datumObj._xmlAttributeKeyString(), self._datumObj.toString())
        ]

    def __eq__(self, other):
        """
        :param other: object of Value
        :return: bool
        """
        return self.datum() == other.datum()

    def __str__(self):
        """
        :return: str
        """
        return self._datumObj._toPrintString()


# Port ( Attribute )
class Abc_Port(Def_Xml):
    CLS_portpath = None
    CLS_set_channel = None

    def _initAbcPort(self, dagObject, fullpathPortname):
        self._dagObj = dagObject
        self._dagpathObj = dagObject.dagpath()

        self._portpathObj = self.CLS_portpath(fullpathPortname)

        self._channelSetObj = self.CLS_set_channel()

        self._valueObj = None
        self._defValueObj = None

        self._connectDagObj = None
        self._connectOutputObj = None

        self._parentDagObj = None

        self._initDefXml()

    def createByRaw(self, *args):
        pass

    def dag(self):
        return self._dagObj
    
    def dagpath(self):
        return self._dagpathObj

    def portpath(self):
        """
        :return: object of Portpath
        """
        return self._portpathObj

    def fullpathName(self):
        """
        :return: str
        """
        self._portpathObj.pathsep().join(
            [self._dagpathObj.fullpathName(), self._portpathObj.fullpathName()]
        )
        return self._dagpathObj.fullpathName()

    def dagname(self):
        """
        :return: str
        """
        return self._dagpathObj.nameString()

    def fullpathDagname(self):
        """
        :return: str
        """
        return self._dagpathObj.fullpathName()

    def portname(self):
        """
        :return: str
        """
        return self._portpathObj.nameString()

    def fullpathPortname(self):
        """
        :return: str
        """
        return self._portpathObj.fullpathName()

    def connect(self):
        """
        :return: 
            1.object of Dag
            2.object of Value
        """
        if self._connectDagObj is not None:
            return self._connectDagObj
        return self._valueObj

    def _setValueObject(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._valueObj = valueObject

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

    def valueType(self):
        return self._valueObj.type()

    def valueTypeString(self):
        return self._valueObj.typeString()

    def valueString(self):
        return self._valueObj.toString()

    def _setDefValueObject(self, valueObject):
        self._defValueObj = valueObject

    def defValue(self):
        """
        :return: object of Value
        """
        return self._defValueObj

    def hasDefValue(self):
        """
        :return: bool
        """
        return self._defValueObj is not None

    def isValueChanged(self):
        pass

    def channels(self):
        """
        :return: list(object of Port, ...)
        """
        return self._channelSetObj.objects()

    def hasChannel(self):
        """
        :return: bool
        """
        return self._channelSetObj.hasObjects()

    def channelString(self):
        return self._channelSetObj.toString()

    def _addChannelObject(self, portObject):
        """
        :param portObject: object of Port
        :return: None
        """
        portObject._setParent(self)
        self._channelSetObj.addObject(portObject.fullpathName(), portObject)

    def connectTo(self, dagObject, outputNameString=None):
        self._connectDagObj = dagObject
        if outputNameString is not None:
            self._connectOutputObj = self._connectDagObj.output(outputNameString)

    def connectDag(self):
        """
        :return: object of Dag
        """
        return self._connectDagObj

    def hasConnectDag(self):
        return self._connectDagObj is not None

    def connectOutput(self):
        return self._connectOutputObj

    def _setParent(self, parentObject):
        self._parentDagObj = parentObject

    def parent(self):
        """
        :return: object of Port
        """
        return self._parentDagObj()

    def hasParent(self):
        """
        :return: bool
        """
        return self._parentDagObj() is not None

    def parentFullpathName(self):
        """
        :return: str
        """
        return self._parentDagObj().fullpathName()

    def parentAttributeName(self):
        """
        :return: str
        """
        return self._parentDagObj().portname()

    def parentFullAttributeName(self):
        """
        :return: str
        """
        return self._parentDagObj().fullpathPortname()

    def _xmlAttributeLis(self):
        return [self.portpath(), self.valueType(), self.connect(), self.connectOutput()]

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.portname())
        ]


class Abc_ShaderPort(Abc_Port):
    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.portname())
        ]


class Abc_NodePort(Abc_Port):
    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.portname())
        ]


class Abc_Output(Def_Xml):
    CLS_raw_name = None

    def _initAbcOutput(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()


class Abc_ShaderOutput(Abc_Output):
    def _initAbcShaderOutput(self, *args):
        self._initAbcOutput(*args)

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.nameString())
        ]


class Abc_NodeOutput(Abc_Output):
    def _initAbcNodeOutput(self, *args):
        self._initAbcOutput(*args)

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.nameString())
        ]


# Dag
class Abc_Dag(Def_Xml):
    CLS_raw_type = None
    CLS_raw_category = None

    CLS_raw_dagpath = None

    CLS_set_port = None
    CLS_set_output = None
    CLS_set_child = None

    CLS_port = None
    CLS_output = None
    CLS_definition = None

    DIC_cls_value = {}

    def _initAbcDag(self, categoryString, fullpathName):
        self._categoryObj = self.CLS_raw_category(categoryString)
        self._dagpathObj = self.CLS_raw_dagpath(fullpathName)

        self._defObj = self.CLS_definition(categoryString)
        self._typeObj = self.CLS_raw_type(self._defObj.typeString())

        self._portSetObj = self.CLS_set_port()
        self._outputSetObj = self.CLS_set_output()

        self._childSetObj = self.CLS_set_child()

        for i in self._defObj.portRaw():
            portname = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]

            portObj = self.CLS_port(self, portname)
            valueCls = self.DIC_cls_value[valueTypeString]

            portObj._setValueObject(valueCls(valueString))
            portObj._setDefValueObject(valueCls(valueString))

            self._addPortObject(portObj)

        for i in self._defObj.outputRaw():
            portname = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]

            portObj = self.CLS_port(self, portname)

            valueCls = self.DIC_cls_value[valueTypeString]

            portObj._setValueObject(valueCls(valueString))
            portObj._setDefValueObject(valueCls(valueString))

            self._addOutputObject(portObj)

        self._initDefXml()

    def loadDef(self, *args):
        pass

    def createByRaw(self, *args):
        pass

    def _typeObject(self):
        return self._typeObj

    def type(self):
        """
        :return: str
        """
        return self._typeObj

    def typeString(self):
        return self._typeObj.raw()

    def _categoryObject(self):
        return self._categoryObj

    def category(self):
        return self._categoryObject()

    def categoryString(self):
        """
        :return: str
        """
        return self._categoryObject().toString()

    def _dagpathObject(self):
        return self._dagpathObj

    def dagpath(self):
        """
        :return: object of Dagpath
        """
        return self._dagpathObj
    
    def setFullpathName(self, fullpathName):
        """
        :param fullpathName: str
        :return: None
        """
        self._dagpathObj.setRaw(fullpathName)

    def fullpathName(self):
        """
        :return: str
        """
        return self._dagpathObj.fullpathName()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObj.setName(nameString)

    def nameString(self):
        """
        :return: str
        """
        return self._dagpathObj.nameString()

    def _childSetObject(self):
        return self._childSetObj

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
        return self._childSetObj.objectsCount()

    def childAt(self, index):
        """
        :param index: int
        :return: object of Node
        """
        return self._childSetObj.objectAt(index)

    def addChild(self, dagObject):
        """
        :param dagObject: object of Node
        :return: None
        """
        self._childSetObj.addObject(dagObject.fullpathName(), dagObject)

    def _addPortObject(self, portObject):
        """
        :param portObject: object of Port
        :return: None
        """
        self._portSetObj.addObject(
            portObject.fullpathPortname(),
            portObject
        )

    def ports(self):
        """
        :return: list(object or attribute, ...)
        """
        return self._portSetObj.objects()

    def port(self, portNameString):
        """
        :param portNameString: str
        :return: object of Port
        """
        return self._portSetObj.objectWithKey(portNameString)

    def _addOutputObject(self, portObject):
        self._outputSetObj.addObject(
            portObject.fullpathPortname(),
            portObject
        )

    def outputs(self):
        return self._outputSetObj.objects()

    def output(self, outputNameString):
        return self._outputSetObj.objectWithKey(outputNameString)

    def toString(self):
        return self.fullpathName()

    def connectDags(self):
        return [i.connectDag() for i in self.ports() if i.hasConnectDag()]

    def connectNodeGraphs(self):
        lis = []
        for p in self.ports():
            connectDag = p.connectDag()
            if isinstance(connectDag, Abc_NodeGraph):
                if not connectDag in lis:
                    lis.append(connectDag)
        return lis


# Geometry
class Abc_Geometry(Abc_Dag):
    def _initAbcGeometry(self, *args):
        self._initAbcDag(*args)


# Shader
class Abc_Shader(Abc_Dag):
    def _initAbcShader(self, *args):
        self._initAbcDag(*args)

        self._outputportObj = None

    def _outputportObject(self):
        return self._outputportObj

    def setOutputport(self, portObject):
        self._outputportObj = portObject

    def outputport(self):
        return self._outputportObject()

    def _xmlAttributeLis(self):
        return [self.dagpath(), self.category(), self.outputport()]

    def _xmlChildList(self):
        return self.ports()


# Node
class Abc_Node(Abc_Dag):
    def _initAbcNode(self, *args):
        self._initAbcDag(*args)

    def _xmlElementKeyString(self):
        return self.categoryString()

    def _xmlAttributeLis(self):
        return [self.dagpath(), self.type()]

    def _xmlChildList(self):
        return self.ports()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.fullpathName())
        ]


# Material
class Abc_Shaderset(Def_Xml):
    CLS_raw_dagpath = None
    CLS_set_shader = None

    CLS_output = None

    def _initAbcShaderset(self, fullpathName):
        self._dagpathObj = self.CLS_raw_dagpath(fullpathName)

        self._shaderSetObj = self.CLS_set_shader()

        self._initDefXml()

        self._prefixString = ''
        self._suffixString = '__shaderset'

    def dagpath(self):
        """
        :return: object of Dagpath
        """
        return self._dagpathObj

    def setFullpathName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObj.setRaw(nameString)

    def fullpathName(self):
        """
        :return: str
        """
        return self._dagpathObj.fullpathName()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObj.setName(nameString)

    def nameString(self):
        """
        :return: str
        """
        return self._dagpathObj.nameString()

    def _addShaderObject(self, shaderObject):
        self._shaderSetObj.addObject(
            shaderObject.fullpathName(),
            shaderObject
        )

    def addSurfaceShader(self, shaderObject):
        shaderObject.setOutputport(
            self.CLS_output('surfaceshader')
        )
        self._addShaderObject(shaderObject)

    def addDisplacementShader(self, shaderObject):
        shaderObject.setOutputport(
            self.CLS_output('displacementshader')
        )
        self._addShaderObject(shaderObject)

    def addVolumeShader(self, shaderObject):
        shaderObject.setOutputport(
            self.CLS_output('volumeshader')
        )
        self._addShaderObject(shaderObject)

    def shaders(self):
        return self._shaderSetObj.objects()

    def _xmlNameString(self):
        return self.fullpathName() + self._suffixString

    def _xmlAttributeLis(self):
        return [self.dagpath()]

    def _xmlChildList(self):
        return self.shaders()

    def _xmlElementList(self):
        lis = []
        for s in self.shaders():
            objects = s.connectNodeGraphs()
            if objects:
                for o in objects:
                    if not o in lis:
                        lis.append(o)
        return lis

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.fullpathName())
        ]


class Abc_Portset(Def_Xml):
    CLS_raw_name = None
    
    def _initAbcPortset(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._initDefXml()


class Abc_GeometryPortset(Abc_Portset):
    def _initAbcGeometryPortset(self, *args):
        self._initAbcPortset(*args)


class Abc_NodeGraph(Def_Xml):
    CLS_raw_name = None

    CLS_set_dag = None
    CLS_set_port = None

    CLS_node = None

    def _initAbcNodeGraph(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._dagSetObj = self.CLS_set_dag()
        self._outputSetObj = self.CLS_set_port()

        self._initDefXml()

    def _nameRawObject(self):
        return self._nameObj

    def _dagSetObject(self):
        return self._dagSetObj

    def nameString(self):
        """
        :return: str
        """
        return self._nameRawObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameRawObject().setRaw(nameString)

    def addNode(self, *args):
        if isinstance(args[0], Abc_Dag):
            dagObject = args[0]
        else:
            dagObject = self.CLS_node(*args)

        self._dagSetObject().addObject(dagObject.fullpathName(), dagObject)

    def nodes(self):
        """
        :return: list(object or node, ...)
        """
        return self._dagSetObject().objects()

    def nodeCount(self):
        """
        :return: int
        """
        return self._dagSetObject().objectsCount()

    def hasNode(self):
        """
        :return: bool
        """
        return self._dagSetObject().hasObjects()

    def _addOutputObject(self, outputObject):
        """
        :param outputObject: object of Output
        :return: None
        """
        self._outputSetObj.addObject(outputObject.fullpathName(), outputObject)

    def outputs(self):
        """
        :return: list(object or output, ...)
        """
        return self._outputSetObj.objects()
    
    def output(self, outputNameString):
        """
        :param outputNameString: str
        :return: object of Output
        """
        return self._outputSetObj.objectWithKey(outputNameString)

    def hasOutput(self):
        """
        :return: bool
        """
        return self._outputSetObj.hasObjects()

    def _xmlAttributeLis(self):
        return [self._nameRawObject()]

    def _xmlChildList(self):
        return self.nodes() + self.outputs()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self.nameString())
        ]


class Abc_GemCollection(Def_Xml):
    CLS_raw_name = None

    CLS_set_geometry = None
    CLS_set_collection = None

    separator_geometry = None

    def _initAbcCollection(self):
        self._nameObj = self.CLS_raw_name()
        self._gemSetObj = self.CLS_set_geometry()
        self._collectionSet = self.CLS_set_collection()

        self._initDefXml()

    def _nameRawObject(self):
        return self._nameObj

    def nameString(self):
        """
        :return: str
        """
        return self._nameRawObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameRawObject().setRaw(nameString)

    def _geometrySetObject(self):
        return self._gemSetObj

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Geometry
        :return:
        """
        self._geometrySetObject().addObject(geometryObject.fullpathName(), geometryObject)

    def geometries(self):
        """
        :return: list(object or geometry, ...)
        """
        return self._geometrySetObject().objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self._geometrySetObject().hasObjects()

    def geomnames(self):
        """
        :return: list(str, ...)
        """
        return [i.dagname() for i in self.geometries()]

    def fullpathGeomnames(self):
        """
        :return: list(str, ...)
        """
        return [i.fullpathName() for i in self.geometries()]

    def geometryString(self):
        return self.separator_geometry.join(self.fullpathGeomnames())

    def _collectionSetObject(self):
        return self._collectionSet

    def addCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self._collectionSetObject().addObject(collectionObject.fullpathName(), collectionObject)

    def collections(self):
        """
        :return: list(object of Collection, ...)
        """
        return self._collectionSetObject().objects()

    def hasCollections(self):
        """
        :return: bool
        """
        return self._collectionSetObject().hasObjects()

    def collectionNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nameString() for i in self.collections()]


class Abc_GeometryAssign(Def_Xml):
    CLS_raw_name = None
    CLS_set_geometry = None

    separator_geometry = None

    def _initAbcGeometryAssign(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._gemSetObj = self.CLS_set_geometry()
        self._collectionObj = None

        self._initDefXml()

    def _nameRawObject(self):
        return self._nameObj

    def nameString(self):
        """
        :return: str
        """
        return self._nameRawObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameRawObject().setRaw(nameString)

    def _geometrySetObject(self):
        return self._gemSetObj

    def geometrySet(self):
        """
        :return: object of Set
        """
        return self._geometrySetObject()

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Geometry
        :return: None
        """
        self._geometrySetObject().addObject(geometryObject.fullpathName(), geometryObject)

    def geometries(self):
        """
        :return: list(object or geometry, ...)
        """
        return self._geometrySetObject().objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self._geometrySetObject().hasObjects()

    def geomnames(self):
        """
        :return: list(str, ...)
        """
        return [i.dagname() for i in self.geometries()]

    def fullpathGeomnames(self):
        """
        :return: list(str, ...)
        """
        return [i.fullpathName() for i in self.geometries()]

    def geometryString(self):
        """
        :return: str
        """
        return self.separator_geometry.join(self.fullpathGeomnames())

    def __collectionObject(self):
        return self._collectionObj

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
        return self.__collectionObject()

    def collectionName(self):
        """
        :return: str
        """
        return self._collectionObj.nameString()


class Abc_ShadersetAssign(Abc_GeometryAssign):
    CLS_shaderset = None

    def _initAbcShadersetAssign(self, *args):
        self._initAbcGeometryAssign(*args)

        self._shadersetObj = None

    def _shadersetObject(self):
        return self._shadersetObj

    def addShaderset(self, shadersetObject):
        """
        :param shadersetObject: object of Shaderset
        :return:
        """
        self._shadersetObj = shadersetObject

    def shaderset(self):
        """
        :return: object of ShaderSet
        """
        return self._shadersetObject()

    def shadersetName(self):
        """
        :return: str
        """
        return self.shaderset().fullpathName()

    def _xmlAttributeLis(self):
        return [self._nameRawObject(), self.shaderset(), self.geometrySet()]

    def _xmlAttributeRaw(self):
        return [
            (self._shadersetObject()._xmlAttributeKeyString(), self._shadersetObject().nameString())
        ]


class Abc_GeomPortsetAssign(Abc_GeometryAssign):
    CLS_portset = None

    def _initAbcGeomPortsetAssign(self, *args):
        self._initAbcGeometryAssign(*args)

        self._portsetObj = None

    def __portsetObject(self):
        return self._portsetObj

    def attributeSet(self):
        """
        :return: object of Set_Port
        """
        return self.__portsetObject()

    def setAttributeSetName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__portsetObject().setName(nameString)

    def attributeSetName(self):
        """
        :return: str
        """
        return self.__portsetObject().nameString()


class Abc_Look(Def_Xml):
    CLS_raw_name = None

    CLS_set_assign = None

    def _initAbcLook(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._assignSetObj = self.CLS_set_assign()

        self._initDefXml()

    def _nameRawObject(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def _assignSetObject(self):
        return self._assignSetObj

    def addAssign(self, assignObject):
        self._assignSetObject().addObject(
            assignObject.nameString(),
            assignObject
        )

    def assigns(self):
        return self._assignSetObject().objects()

    def shadersets(self):
        return [i.shaderset() for i in self.assigns()]

    def _xmlAttributeLis(self):
        return [self._nameRawObject()]

    def _xmlChildList(self):
        return self.assigns()

    def _xmlElementList(self):
        return self.shadersets()


class Abc_Reference(Def_Xml):
    CLS_raw_file = None

    def _initAbcInclude(self, *args):
        self._fileObj = self.CLS_raw_file(*args)

        self._initDefXml()

    def _fileObject(self):
        return self._fileObj

    def file(self):
        return self._fileObject()

    def filename(self):
        return self._fileObject().toString()

    def _xmlAttributeLis(self):
        return [self.file()]


class Abc_XmlDocument(Def_Xml):
    CLS_raw_file = None

    CLS_raw_version = None

    CLS_set_reference = None
    CLS_set_look = None

    STR_mtlx_version = None

    def _initAbcXmlDocument(self, *args):
        self._fileObj = self.CLS_raw_file(*args)
        self._versionObj = self.CLS_raw_version(self.STR_mtlx_version)

        self._referenceSetObj = self.CLS_set_reference()
        self._lookSetObj = self.CLS_set_look()

        self._initDefXml()

    def _fileObject(self):
        return self._fileObj

    def filename(self):
        return self._fileObject().toString()

    def _versionObject(self):
        return self._versionObj

    def version(self):
        return self._versionObject()

    def versionname(self):
        return self._versionObject().toString()

    def _referenceSetObject(self):
        return self._referenceSetObj

    def addReference(self, referenceObject):
        self._lookSetObject().addObject(
            referenceObject.filename(),
            referenceObject
        )

    def references(self):
        return self._lookSetObject().objects()

    def _lookSetObject(self):
        return self._lookSetObj

    def addLook(self, lookObject):
        self._lookSetObject().addObject(
            lookObject.nameString(),
            lookObject
        )

    def looks(self):
        return self._lookSetObject().objects()

    def _xmlAttributeLis(self):
        return [self.version()]

    def _xmlChildList(self):
        return self.looks()


class Abc_Def(mtlCore.Basic):
    def _initAbcDef(self):
        self._nodeDefsDic = mtlConfigure.Def_Node_Dic

    def load(self, *args):
        pass

    def get(self, keyString):
        assert keyString in self._nodeDefsDic, u'Category "{}" is Non-Definition'.format(keyString)
        return self._nodeDefsDic.get(keyString, {})


class Abc_TypeDef(Abc_Def):
    pass


class Abc_DagDef(Abc_Def):
    def _initAbcDagDef(self, category):
        self._initAbcDef()
        self._categoryString = category

        self._nodeDefDic = self.get(self._categoryString)

    def categoryString(self):
        return self._categoryString

    def typeString(self):
        return self._nodeDefDic.get(self.Key_Type_String)

    def portRaw(self):
        return self._nodeDefDic.get(self.Key_Port, [])

    @staticmethod
    def outputRaw():
        return [
            {
                "name": "out_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "out_transparency",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
