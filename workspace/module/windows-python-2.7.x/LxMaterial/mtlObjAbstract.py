# coding:utf-8
from LxMaterial import mtlConfigure, mtlCore


class Def_Xml(mtlCore.Mtd_MtlBasic):
    xml_separator_attribute = u' '

    DEF_mtlx_key_element = u''
    DEF_mtlx_key_attribute = u''

    def _initDefXml(self):
        self._xmlIndentStr = ''

    def _xmlElementKeyString(self):
        return self.DEF_mtlx_key_element

    def _xmlAttributeKeyString(self):
        return self.DEF_mtlx_key_attribute

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

    def _xmlAttributeObjectLis(self):
        pass

    def _xmlChildList(self):
        pass

    def _xmlElementList(self):
        pass

    def _xmlAttributeRaw(self):
        """
        :return: list(tuple(key, value)/object instance of Def_Xml, ...)
        """
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
                    for i in attributeRaw:
                        if isinstance(i, Def_Xml):
                            addAttributeFnc_(i, lString, rString)
                        else:
                            k, v = i
                            if v:
                                lis.append(u'{}{}="{}"{}'.format(lString, k, v, rString))

        def addBranchFnc_(elementObject_, rString, parentElementObject=None):
            if parentElementObject is not None:
                lString = elementObject_._xmlIndentString
            else:
                lString = u''

            tagString = elementObject_._xmlElementKeyString()
            addPrefixFnc_(tagString, lString=lString, rString=u'')
            # Attribute
            attributes = elementObject_._xmlAttributeObjectLis()
            if attributes:
                [addAttributeFnc_(i, lString=cls.xml_separator_attribute, rString=u'') for i in attributes]
            # Children
            children = elementObject_._xmlChildList()
            if children:
                lis.append(u'>\r\n')

                for i in children:
                    if i is not None:
                        i._xmlIndentString = lString + defIndentString
                        addBranchFnc_(i, rString=rString, parentElementObject=elementObject_)

                lis.append(u'{}</{}>\r\n'.format(lString, tagString))
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

    def __repr__(self):
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

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]

    def __eq__(self, other):
        """
        :param other: typed raw
        :return: bool
        """
        return self.toString() == other.toString()


class Abc_Path(Abc_Raw):
    CLS_raw = None

    DEF_separator = None

    def _initAbcPath(self, *args):
        self._initAbcRaw(*args)

        if self.hasRaw():
            self._rawLis = [self.CLS_raw(i) for i in self._raw.split(self.DEF_separator)]
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
        self._rawLis = [self.CLS_raw(i) for i in raw.split(self.DEF_separator)]

    def createByString(self, *args):
        raw = args[0]
        self._rawLis = [self.CLS_raw(i) for i in raw.split(self.DEF_separator)]

    def setNameString(self, nameString):
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
        return self.DEF_separator.join([i.toString() for i in self._rawLis])

    def pathsep(self):
        """
        :return: str
        """
        return self.DEF_separator


class Abc_ShadersetPath(Abc_Path):
    def _initAbcShadersetPath(self, *args):
        self._initAbcPath(*args)

    def _xmlAttributeValueString(self):
        return self.fullpathName()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString()),
        ]


class Abc_Set(Def_Xml):
    DEF_separator_object = ','
    # noinspection PyUnusedLocal
    def _initAbcSet(self, *args):
        self._objectLis = []
        self._objectDic = {}

        self._objectCount = 0

        self._objectFilterStr = None

        self._initDefXml()

    def createByRaw(self, *args):
        pass

    def addObject(self, obj):
        """
        :param obj: object of typed
        :return:
        """
        queryString = obj._queryString()
        assert queryString not in self._objectDic, '''Key is Exist.'''
        self._objectLis.append(obj)
        self._objectDic[queryString] = obj
        self._objectCount += 1

    def hasObjects(self):
        """
        :return: bool
        """
        return self._objectLis != []

    def objects(self):
        """
        :return: list(object, ...)
        """
        return self._objectLis

    def hasObject(self, *args):
        """
        :return: bool
        """
        if isinstance(args[0], (str, unicode)):
            return args[0] in self._objectDic
        else:
            return args[0] in self._objectLis

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
        return self._objectLis[index]

    def hasObjectAt(self, index):
        """
        :param index: int
        :return: object
        """
        pass

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
        return self.DEF_separator_object.join([i.toString() for i in self.objects()])

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]

    def __len__(self):
        """
        :return: int
        """
        return self.objectCount()


class Abc_RawString(Abc_Raw):
    def _initAbcRawString(self, *args):
        self._initAbcRaw(*args)

    def toString(self):
        """
        :return: str
        """
        return unicode(self._raw)

    def createByString(self, *args):
        self._raw = unicode(args[0])

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
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
        assert args is not (), u'argument must not be Empty.'

        if isinstance(args[0], (str, unicode)):
            self.createByString(*args)
        else:
            self.createByRaw(*args)

    def createByRaw(self, *args):
        """
        :param args: raw of typed
        :return: None
        """
        assert args is not (), u'argument must not be Empty.'
        raw = args[0]
        assert isinstance(raw, self.raw_type), u'[ Argument Error ], "arg" Must "{}".'.format(self.raw_type)

        self.setRaw(self.CLS_raw(raw))

    def createByString(self, *args):
        """
        :param args: str
        :return: None
        """
        assert args is not (), u'argument must not be Empty.'
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

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
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
        assert args is not (), u'argument must not be Empty.'

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
        assert args is not (), u'argument must not be Empty.'
        if isinstance(args[0], (tuple, list)):
            raw = list(args[0])
        else:
            raw = args

        [self.addChild(self.CLS_set_child(self, i)) for i in raw]

        self.setRaw(raw)

    def createByString(self, *args):
        assert args is not (), u'argument must not be Empty.'
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

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
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

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            self.datum()
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


# > Port ( Attribute )
class Abc_Port(Def_Xml):
    CLS_portpath = None
    CLS_set_channel = None

    def _initAbcPort(self, *args):
        dagObject, fullpathPortname = args

        self._dagObj = dagObject
        self._dagpathObj = dagObject.path()

        self._portpathObj = self.CLS_portpath(fullpathPortname)

        self._channelSetObj = self.CLS_set_channel()

        self._valueObj = None
        self._defValueObj = None

        self._parentDagObj = None

        self._initDefXml()

    def createByRaw(self, *args):
        pass

    def dag(self):
        return self._dagObj

    def path(self):
        """
        :return: object of Portpath
        """
        return self._portpathObj

    def fullpathName(self):
        """
        :return: str
        """
        return self._portpathObj.pathsep().join(
            [self._dagpathObj.fullpathName(), self._portpathObj.fullpathName()]
        )

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

    def _setValueObject(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._valueObj = valueObject

    def porttype(self):
        return self._valueObj.type()

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

    def _addChannelObject(self, inputObject):
        """
        :param inputObject: object of Port
        :return: None
        """
        inputObject._setParent(self)
        self._channelSetObj.addObject(inputObject)

    def channels(self):
        """
        :return: list(object of Port, ...)
        """
        return self._channelSetObj.objects()

    def channel(self, channelName):
        return self._channelSetObj.objectWithKey(channelName)

    def hasChannels(self):
        """
        :return: bool
        """
        return self._channelSetObj.hasObjects()

    def channelString(self):
        return self._channelSetObj.toString()

    def _setParent(self, parentObject):
        self._parentDagObj = parentObject

    def parent(self):
        """
        :return: object of Port
        """
        return self._parentDagObj

    def hasParent(self):
        """
        :return: bool
        """
        return self._parentDagObj is not None

    def parentFullpathName(self):
        """
        :return: str
        """
        return self._parentDagObj.fullpathName()

    def parentAttributeName(self):
        """
        :return: str
        """
        return self._parentDagObj.portname()

    def parentFullAttributeName(self):
        """
        :return: str
        """
        return self._parentDagObj.fullpathPortname()

    def _queryString(self):
        return self.fullpathPortname()

    def _xmlAttributeValueString(self):
        return self.portname()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


class Abc_Input(Abc_Port):
    def _initAbcInput(self, *args):
        self._initAbcPort(*args)

        self._sourceDagObj = None
        self._sourcePortObj = None

    def connectFrom(self, outputObject):
        assert isinstance(outputObject, Abc_Output), u'''[ Argument Error ] "outputObject" must object of Output'''

        if self.isConnectedFrom(outputObject) is False:
            self._sourcePortObj = outputObject
            self._sourceDagObj = self._sourcePortObj.dag()

            outputObject.connectTo(self)

    def hasSource(self):
        return self._sourcePortObj is not None

    def source(self):
        """
        :return: object of Output
        """
        return self._sourcePortObj

    def isConnectedFrom(self, outputObject):
        return outputObject is self._sourcePortObj

    def _given(self):
        """
        :return:
            1.object of Dag
            2.object of Value
        """
        if self.hasSource() is True:
            return self.source()
        return self.value()

    def _xmlAttributeObjectLis(self):
        return [self.path(), self.porttype(), self._given()]


class Abc_ShaderInput(Abc_Input):
    def _initAbcShaderInput(self, *args):
        self._initAbcInput(*args)

    def sourceNodeGraphOutput(self):
        if self.hasSource():
            nodeGraph = self.source().dag().nodeGraph()
            if nodeGraph:
                return nodeGraph.getNodeGraphOutput(self)

    def _given(self):
        """
        :return:
            1.object of Dag
            2.object of Value
        """
        if self.hasSource() is True:
            return self.sourceNodeGraphOutput()
        return self.value()


class Abc_NodeInput(Abc_Input):
    def _initAbcNodeInput(self, *args):
        self._initAbcInput(*args)


class Abc_GeometryProperty(Abc_Port):
    def _initAbcGeometryProperty(self, *args):
        self._initAbcPort(*args)


class Abc_GeometryVisibility(Abc_Port):
    def _initAbcVisibility(self, *args):
        self._initAbcPort(*args)


class Abc_Output(Abc_Port):
    def _initAbcOutput(self, *args):
        self._initAbcPort(*args)
        
        self._targetPortObj = None

    def connectTo(self, inputObject):
        """
        :param inputObject: object of Input
        :return:
        """
        assert isinstance(inputObject, Abc_Input), u'''[ Argument Error ] "outputObject" must object of Input'''

        if self.isConnectedTo(inputObject) is False:
            self._targetPortObj = inputObject

            inputObject.connectFrom(self)

    def hasTarget(self):
        return self._targetPortObj is not None

    def isConnectedTo(self, inputObject):
        return self._targetPortObj is inputObject

    def target(self):
        return self._targetPortObj

    def _xmlAttributeValueString(self):
        return self.fullpathPortname()

    def _xmlAttributeRaw(self):
        return [
            self.dag(),
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


class Abc_ShaderOutput(Abc_Output):
    def _initAbcShaderOutput(self, *args):
        self._initAbcOutput(*args)


class Abc_NodeOutput(Abc_Output):
    def _initAbcNodeOutput(self, *args):
        self._initAbcOutput(*args)


# Geometry
class Abc_Geometry(Def_Xml):
    CLS_raw_dagpath = None

    CLS_set_property = None
    CLS_set_assign_visibility = None

    CLS_property = None
    CLS_visibility = None
    CLS_def_geometry = None

    DEF_cls_value = {}

    def _initAbcGeometry(self, *args):
        self._dagpathObj = self.CLS_raw_dagpath(*args)

        self._propertySetObj = self.CLS_set_property()
        self._visibilityAssignSetObj = self.CLS_set_assign_visibility()

        self._geometryDefObj = self.CLS_def_geometry()

        for i in self._geometryDefObj.properties():
            portnameString = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]

            portObj = self.CLS_property(self, portnameString)
            valueCls = self.DEF_cls_value[valueTypeString]

            portObj._setValueObject(valueCls(valueString))
            portObj._setDefValueObject(valueCls(valueString))

            self._addPropertyObject(portObj)

        for i in self._geometryDefObj.visibilities():
            portnameString = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]

            portObj = self.CLS_visibility(self, portnameString)
            valueCls = self.DEF_cls_value[valueTypeString]

            portObj._setValueObject(valueCls(valueString))
            portObj._setDefValueObject(valueCls(valueString))

            self._addVisibilityObject(portObj)

        self._initDefXml()

    def path(self):
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

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObj.setNameString(nameString)

    def nameString(self):
        """
        :return: str
        """
        return self._dagpathObj.nameString()

    def _addPropertyObject(self, propertyObject):
        self._propertySetObj.addObject(propertyObject)

    def property(self, propertyNameString):
        return self._propertySetObj.objectWithKey(propertyNameString)

    def hasProperty(self, *args):
        return self._propertySetObj.hasObject(*args)

    def properties(self):
        return self._propertySetObj.objects()

    def _addVisibilityObject(self, visibilityObject):
        self._visibilityAssignSetObj.addObject(visibilityObject)

    def visibility(self, visibilityNameString):
        return self._visibilityAssignSetObj.objectWithKey(visibilityNameString)

    def hasVisibility(self, *args):
        return self._visibilityAssignSetObj.hasObject(*args)

    def visibilities(self):
        return self._visibilityAssignSetObj.objects()

    def toString(self):
        return self.fullpathName()

    def _queryString(self):
        return self.fullpathName()

    def _xmlChildList(self):
        return self.properties()


# Dag
class Abc_Dag(Def_Xml):
    CLS_raw_type = None
    CLS_raw_category = None

    CLS_raw_dagpath = None

    CLS_set_input = None
    CLS_set_output = None
    CLS_set_child = None

    CLS_input = None
    CLS_output = None
    CLS_def_dag = None

    DEF_cls_value = {}

    def _initAbcDag(self, categoryString, fullpathName):
        self._categoryObj = self.CLS_raw_category(categoryString)
        self._dagpathObj = self.CLS_raw_dagpath(fullpathName)

        self._dagDefObj = self.CLS_def_dag(categoryString)
        self._typeObj = self.CLS_raw_type(self._dagDefObj.typeString())

        self._inputSetObj = self.CLS_set_input()
        self._outputSetObj = self.CLS_set_output()

        self._childSetObj = self.CLS_set_child()

        for i in self._dagDefObj.inputRaw():
            portnameString = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]

            portObj = self.CLS_input(self, portnameString)
            valueCls = self.DEF_cls_value[valueTypeString]

            portObj._setValueObject(valueCls(valueString))
            portObj._setDefValueObject(valueCls(valueString))

            self._addInputObject(portObj)

        for i in self._dagDefObj.outputRaw():
            portnameString = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]

            portObj = self.CLS_output(self, portnameString)

            valueCls = self.DEF_cls_value[valueTypeString]

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

    def path(self):
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

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObj.setNameString(nameString)

    def nameString(self):
        """
        :return: str
        """
        return self._dagpathObj.nameString()

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

    def addChild(self, dagObject):
        """
        :param dagObject: object of Node
        :return: None
        """
        self._childSetObj.addObject(dagObject)

    def _addInputObject(self, portObject):
        """
        :param portObject: object of Port
        :return: None
        """
        self._inputSetObj.addObject(portObject)

    def hasInputs(self):
        return self._inputSetObj.hasObjects()

    def hasInput(self, *args):
        return self._inputSetObj.hasObject(*args)

    def inputs(self):
        """
        :return: list(object or attribute, ...)
        """
        return self._inputSetObj.objects()

    def input(self, inputNameString):
        """
        :param inputNameString: str
        :return: object of Port
        """
        return self._inputSetObj.objectWithKey(inputNameString)

    def _addOutputObject(self, portObject):
        self._outputSetObj.addObject(portObject)

    def outputs(self):
        return self._outputSetObj.objects()

    def output(self, outputNameString):
        return self._outputSetObj.objectWithKey(outputNameString)

    def toString(self):
        return self.fullpathName()

    def sourceDags(self):
        return [i.source().dag() for i in self.inputs() if i.hasSource()]

    def targetDags(self):
        return [i.target().dag() for i in self.outputs() if i.hasTarget()]

    def targetShaders(self):
        return [i for i in self.targetDags() if isinstance(i, Abc_Shader)]

    def _queryString(self):
        return self.fullpathName()

    def connectedOutputs(self, toShader=False):
        lis = []

        for outputObject in self.outputs():
            if outputObject.hasTarget():
                if toShader is True:
                    if isinstance(outputObject.target().dag(), Abc_Shader):
                        lis.append(outputObject)
                else:
                    lis.append(outputObject)
        return lis


# Dag > Shader
class Abc_Shader(Abc_Dag):
    def _initAbcShader(self, *args):
        self._initAbcDag(*args)

        self._targetShadersetPortObj = None

    def setTargetShadersetPort(self, inputObject):
        self._targetShadersetPortObj = inputObject

    def targetShadersetPort(self):
        return self._targetShadersetPortObj

    def sourceNodeGraphs(self):
        lis = []
        for inputObject in self.inputs():
            if inputObject.hasSource():
                dag = inputObject.source().dag()
                nodeGraph = dag.nodeGraph()
                if nodeGraph is not None:
                    if not nodeGraph in lis:
                        lis.append(nodeGraph)
        return lis

    def outColor(self):
        return self.output('out_color')

    def outTransparency(self):
        return self.output('out_transparency')

    def outAlpha(self):
        return self.output('out_alpha')

    def _xmlAttributeObjectLis(self):
        return [self.path(), self.type()]

    def _xmlChildList(self):
        return self.inputs()


# Dag > Node
class Abc_Node(Abc_Dag):
    def _initAbcNode(self, *args):
        self._initAbcDag(*args)
        
        self._nodeGraphObj = None
        
    def setNodeGraph(self, nodeGraphObject):
        self._nodeGraphObj = nodeGraphObject

    def nodeGraph(self):
        return self._nodeGraphObj

    def _xmlElementKeyString(self):
        return self.categoryString()

    def _xmlAttributeObjectLis(self):
        return [self.path(), self.type()]

    def _xmlChildList(self):
        return self.inputs()

    def _xmlAttributeValueString(self):
        return self.fullpathName()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# Shaderset
class Abc_Shaderset(Def_Xml):
    CLS_raw_dagpath = None
    CLS_set_input = None

    CLS_input = None
    CLS_def_dag = None

    DEF_cls_value = None

    def _initAbcShaderset(self, fullpathName):
        self._dagpathObj = self.CLS_raw_dagpath(fullpathName)

        self._inputSetObj = self.CLS_set_input()

        self._surfaceDagObj = None
        self._displacementDagObj = None
        self._sourceVolumeDagObj = None

        self._surfacePortObj = None
        self._displacementPortObj = None
        self._sourceVolumePortObj = None
        
        for i in self.CLS_def_dag.shadersetInputRaw():
            portnameString = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]

            portObj = self.CLS_input(self, portnameString)
            valueCls = self.DEF_cls_value[valueTypeString]

            portObj._setValueObject(valueCls(valueString))
            portObj._setDefValueObject(valueCls(valueString))

            self._addInputObject(portObj)

        self._initDefXml()

        self._suffixString = '__shaderset'

    def path(self):
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

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObj.setNameString(nameString)

    def nameString(self):
        """
        :return: str
        """
        return self._dagpathObj.nameString()

    def _addInputObject(self, inputObject):
        self._inputSetObj.addObject(inputObject)

    def inputs(self):
        """
        :return: list(object or attribute, ...)
        """
        return self._inputSetObj.objects()

    def input(self, inputNameString):
        """
        :param inputNameString: str
        :return: object of Port
        """
        return self._inputSetObj.objectWithKey(inputNameString)

    def inputSurface(self):
        return self.input('surfaceshader')

    def inputDisplacement(self):
        return self.input('displacementshader')

    def inputVolume(self):
        return self.input('volumeshader')

    def connectSurfaceFrom(self, outputObject):
        self._surfacePortObj = outputObject
        self._surfacePortObj.connectTo(self.inputSurface())
        self._surfaceDagObj = self._surfacePortObj.dag()
        self._surfaceDagObj.setTargetShadersetPort(self.inputSurface())

    def surfaceShader(self):
        return self._surfaceDagObj

    def connectDisplacementFrom(self, outputObject):
        self._displacementPortObj = outputObject
        self._displacementPortObj.connectTo(self.inputDisplacement())
        self._displacementDagObj = self._displacementPortObj.dag()
        self._displacementDagObj.setTargetShadersetPort(self.inputDisplacement())

    def displacementShader(self):
        return self._displacementDagObj

    def connectVolumeFrom(self, outputObject):
        self._sourceVolumePortObj = outputObject
        self._sourceVolumePortObj.connectTo(self.inputVolume())
        self._sourceVolumeDagObj = self._sourceVolumePortObj.dag()
        self._sourceVolumeDagObj.setTargetShadersetPort(self.inputVolume())

    def volumeShader(self):
        return self._sourceVolumeDagObj

    def shaders(self):
        return [self.surfaceShader(), self.displacementShader(), self.volumeShader()]

    def sourcePorts(self):
        pass

    def _xmlAttributeObjectLis(self):
        return [self.path()]

    def _xmlChildList(self):
        return self.shaders()

    def _xmlElementList(self):
        lis = []
        for s in self.shaders():
            if s is not None:
                objects = s.sourceNodeGraphs()
                if objects:
                    for o in objects:
                        if not o in lis:
                            lis.append(o)
        return lis

    def _xmlAttributeValueString(self):
        return self.fullpathName()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# Portset
class Abc_Portset(Def_Xml):
    CLS_raw_name = None

    CLS_set_port = None
    
    def _initAbcPortset(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._portSetObj = self.CLS_set_port()

        self._initDefXml()

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

    def ports(self):
        return self._portSetObj.objects()

    def _xmlAttributeValueString(self):
        return self.nameString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


class Abc_Propertyset(Abc_Portset):
    def _initAbcPropertyset(self, *args):
        self._initAbcPortset(*args)

    def _xmlAttributeObjectLis(self):
        return [self.name()]

    def _xmlChildList(self):
        return self.ports()


# Output of Node-Graph
class Abc_NodeGraphOutput(Def_Xml):
    CLS_raw_name = None

    def _initAbcNodeGraphOutput(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._portObj = None

        self._nodeGraphObj = None

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

    def setPort(self, outputObject):
        self._portObj = outputObject

    def port(self):
        return self._portObj

    def porttype(self):
        return self._portObj.porttype()

    def setNodeGraph(self, nodeGraphObject):
        self._nodeGraphObj = nodeGraphObject

    def nodeGraph(self):
        return self._nodeGraphObj

    def _queryString(self):
        return self.nameString()

    def _xmlAttributeObjectLis(self):
        return [self.name(), self.porttype(), self.port()]

    def _xmlAttributeValueString(self):
        return self.nameString()

    def _xmlAttributeRaw(self):
        return [
            self.nodeGraph(),
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


class Abc_NodeGraph(Def_Xml):
    CLS_raw_name = None

    CLS_set_dag = None
    CLS_set_input = None

    CLS_node = None
    CLS_output = None

    def _initAbcNodeGraph(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._dagSetObj = self.CLS_set_dag()
        self._outputSetObj = self.CLS_set_input()

        self._outputDic = {}

        self._initDefXml()

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

    def addNode(self, *args):
        """
        :param args:
            1.object of Dag
            2.str(node category), str(node name)
        :return:
        """
        if isinstance(args[0], Abc_Dag):
            nodeObject = args[0]
        else:
            nodeObject = self.CLS_node(*args)

        nodeObject.setNodeGraph(self)

        self._dagSetObj.addObject(nodeObject)

        outputObjects = nodeObject.connectedOutputs(toShader=True)
        if outputObjects:
            for outputObject in outputObjects:
                name = u'output{}'.format(self._outputSetObj.objectCount())
                nodeGraphOutputObject = self.CLS_output(name)
                nodeGraphOutputObject.setPort(outputObject)
                self._addOutputObject(nodeGraphOutputObject)

                key = outputObject.target().fullpathName()
                self._outputDic[key] = nodeGraphOutputObject

    def addNodes(self, *args):
        if isinstance(args[0], (list, tuple)):
            objectLis = args[0]
        else:
            objectLis = args

        [self.addNode(i) for i in objectLis]

    def nodes(self):
        """
        :return: list(object or node, ...)
        """
        return self._dagSetObj.objects()

    def nodeCount(self):
        """
        :return: int
        """
        return self._dagSetObj.objectCount()

    def hasNodes(self):
        """
        :return: bool
        """
        return self._dagSetObj.hasObjects()

    def _addOutputObject(self, outputObject):
        """
        :param outputObject: object of Output
        :return: None
        """
        outputObject.setNodeGraph(self)

        self._outputSetObj.addObject(outputObject)

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

    def getNodeGraphOutput(self, inputObject):
        key = inputObject.fullpathName()
        return self._outputDic[key]

    def hasOutputs(self):
        """
        :return: bool
        """
        return self._outputSetObj.hasObjects()

    def _xmlAttributeObjectLis(self):
        return [self._nameObj]

    def _xmlChildList(self):
        return self.nodes() + self.outputs()

    def _xmlAttributeValueString(self):
        return self.nameString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# Collection of Geometry(s)
class Abc_GeometryCollection(Def_Xml):
    CLS_raw_name = None

    CLS_set_geometry = None
    CLS_set_collection = None

    DEF_geometry_separator = None

    def _initAbcGeometryCollection(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._geometrySetObj = self.CLS_set_geometry()
        self._collectionSetObj = self.CLS_set_collection()
        self._excludeGeometrySetObj = self.CLS_set_geometry()

        self._initDefXml()

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
    
    def geometrySet(self):
        return self._geometrySetObj

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Geometry
        :return:
        """
        self._geometrySetObj.addObject(geometryObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            objectLis = args[0]
        else:
            objectLis = args

        [self.addGeometry(i) for i in objectLis]

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
        return [i.fullpathName() for i in self.geometries()]

    def fullpathGeometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.fullpathName() for i in self.geometries()]

    def excludeGeometrySet(self):
        return self._excludeGeometrySetObj

    def addExcludeGeometry(self, geometryObject):
        self._excludeGeometrySetObj.addObject(geometryObject)

    def addExcludeGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            objectLis = args[0]
        else:
            objectLis = args

        [self.addExcludeGeometry(i) for i in objectLis]

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

    def _queryString(self):
        return self.nameString()

    def _xmlAttributeObjectLis(self):
        return [self._nameObj, self.geometrySet(), self.collectionSet(), self.excludeGeometrySet()]

    def _xmlAttributeValueString(self):
        return self.nameString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


class Abc_Assign(Def_Xml):
    CLS_raw_name = None
    CLS_set_geometry = None

    DEF_geometry_separator = None

    def _initAbcAssign(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._geometrySetObj = self.CLS_set_geometry()
        self._collectionObj = None
        
        self._lookObj = None

        self._initDefXml()

    def name(self):
        return self._nameObj

    def hasNameString(self):
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

    def geometrySet(self):
        """
        :return: object of Set
        """
        return self._geometrySetObj

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Geometry
        :return: None
        """
        self._geometrySetObj.addObject(geometryObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            objectLis = args[0]
        else:
            objectLis = args

        [self.addGeometry(i) for i in objectLis]

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
        return [i.fullpathName() for i in self.geometries()]

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
    
    def setLook(self, lookObject):
        self._lookObj = lookObject
        self._lookObj.addAssign(self)

    def _queryString(self):
        return self.nameString()

    def _givens(self):
        pass


class Abc_ShadersetAssign(Abc_Assign):
    def _initAbcShadersetAssign(self, *args):
        self._initAbcAssign(*args)

        self._shadersetObj = None

    def _shadersetObject(self):
        return self._shadersetObj

    def setShaderset(self, shadersetObject):
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

    def _givens(self):
        return [self._shadersetObj, self._collectionObj]

    def _xmlAttributeValueString(self):
        self.nameString()

    def _xmlAttributeObjectLis(self):
        return [self.name(), self.shaderset(), self.geometrySet(), self.collection()]


class Abc_PropertysetAssign(Abc_Assign):
    def _initPropertysetAssign(self, *args):
        self._initAbcAssign(*args)

        self._propertysetObj = None

    def setPropertyset(self, propertysetObject):
        """
        :param propertysetObject: object of Propertyset
        :return: None
        """
        self._propertysetObj = propertysetObject

    def propertyset(self):
        """
        :return: object of Propertyset
        """
        return self._propertysetObj

    def _givens(self):
        return [self._propertysetObj, self._collectionObj]

    def _xmlAttributeObjectLis(self):
        return [self.name(), self.propertyset(), self.geometrySet(), self.collection()]


class Abc_VisibilityAssign(Abc_Assign):
    CLS_raw_type = None
    CLS_value_visibility = None

    CLS_set_geometry_viewer = None

    CLS_def_geometry = None

    def _initAbcVisibilityAssign(self, *args):
        self._initAbcAssign(*args)

        self._geometryDef = self.CLS_def_geometry()

        self._typeObj = None

        self._visibilityValueObj = None
        self._defVisibilityValueObj = None

        self._viewerGeometrySetObj = self.CLS_set_geometry_viewer()

    def setTypeString(self, visibilityTypeString):
        self._typeObj = self.CLS_raw_type(visibilityTypeString)

        i = self._geometryDef.visibility(visibilityTypeString)
        valueString = i[self.Key_Value_String]

        self._visibilityValueObj = self.CLS_value_visibility(valueString)

    def type(self):
        return self._typeObj

    def visible(self):
        return self._visibilityValueObj

    def viewerGeometrySet(self):
        return self._viewerGeometrySetObj
    
    def addViewerGeometry(self, geometryObject):
        self._viewerGeometrySetObj.addObject(geometryObject)
        
    def viewerGeometries(self):
        return self._viewerGeometrySetObj.objsets()

    def _givens(self):
        return [self._collectionObj]

    def _xmlAttributeObjectLis(self):
        return [self.name(), self.type(), self.visible(), self.geometrySet(), self.viewerGeometrySet(), self.collection()]


class Abc_Look(Def_Xml):
    CLS_raw_name = None

    CLS_set_assign = None

    CLS_set_assign_shaderset = None
    ClS_set_assign_propertyset = None
    CLS_set_assign_visibility = None

    def _initAbcLook(self, *args):
        self._nameObj = self.CLS_raw_name(*args)

        self._shadersetAssignSetObj = self.CLS_set_assign_shaderset()
        self._propertysetAssignSetObj = self.ClS_set_assign_propertyset()
        self._visibilityAssignSetObj = self.CLS_set_assign_visibility()

        self._assignSetObj = self.CLS_set_assign()

        self._initDefXml()

    def nameString(self):
        return self._nameObj.toString()

    def _assignSetObject(self):
        return self._assignSetObj

    def addVisibilityAssign(self, visibilityAssignObject):
        """
        :param visibilityAssignObject: object of VisibilityAssign
        :return:
        """
        assert isinstance(visibilityAssignObject, Abc_VisibilityAssign)

        count = self._visibilityAssignSetObj.objectCount()
        if visibilityAssignObject.hasNameString() is False:
            visibilityAssignObject.setNameString('visibility_assign_{}'.format(count))
        self._visibilityAssignSetObj.addObject(visibilityAssignObject)

    def visibilityAssigns(self):
        return self._visibilityAssignSetObj.objects()

    def addShadersetAssign(self, shadersetAssignObject):
        """
        :param shadersetAssignObject: object of ShadersetAssign
        :return:
        """
        assert isinstance(shadersetAssignObject, Abc_ShadersetAssign)

        count = self._shadersetAssignSetObj.objectCount()
        if shadersetAssignObject.hasNameString() is False:
            shadersetAssignObject.setNameString('shaderset_assign_{}'.format(count))
        self._shadersetAssignSetObj.addObject(shadersetAssignObject)

    def shadersetAssigns(self):
        return self._shadersetAssignSetObj.objects()

    def addPropertysetAssign(self, propertysetAssignObject):
        """
        :param propertysetAssignObject: object of PropertysetAssign
        :return:
        """
        assert isinstance(propertysetAssignObject, Abc_PropertysetAssign)

        count = self._propertysetAssignSetObj.objectCount()
        if propertysetAssignObject.hasNameString() is False:
            propertysetAssignObject.setNameString('propertyset_assign_{}'.format(count))
        self._propertysetAssignSetObj.addObject(propertysetAssignObject)

    def propertysetAssigns(self):
        return self._propertysetAssignSetObj.objects()

    def addAssign(self, assignObject):
        if isinstance(assignObject, Abc_VisibilityAssign):
            self.addVisibilityAssign(assignObject)
        elif isinstance(assignObject, Abc_ShadersetAssign):
            self.addShadersetAssign(assignObject)
        elif isinstance(assignObject, Abc_PropertysetAssign):
            self.addPropertysetAssign(assignObject)

    def hasAssigns(self):
        return self.assigns() != []

    def assigns(self):
        return self.visibilityAssigns() + self.shadersetAssigns() + self.propertysetAssigns()

    def _givens(self):
        lis = []
        for i in self.assigns():
            for j in i._givens():
                if j is not None:
                    if j not in lis:
                        lis.append(j)
        return lis

    def _queryString(self):
        return self.nameString()

    def _xmlAttributeObjectLis(self):
        return [self._nameObj]

    def _xmlChildList(self):
        return self.assigns()

    def _xmlElementList(self):
        return self._givens()


class Abc_Reference(Def_Xml):
    CLS_raw_file = None

    def _initAbcInclude(self, *args):
        self._fileObj = self.CLS_raw_file(*args)

        self._initDefXml()

    def _fileObject(self):
        return self._fileObj

    def file(self):
        return self._fileObject()

    def filenameString(self):
        return self._fileObject().toString()

    def _queryString(self):
        return self.filenameString()

    def _xmlAttributeObjectLis(self):
        return [self.file()]


class Abc_XmlDocument(Def_Xml):
    CLS_raw_file = None

    CLS_raw_version = None

    CLS_set_reference = None
    CLS_set_look = None

    DEF_mtlx_version = None

    def _initAbcXmlDocument(self, *args):
        self._fileObj = self.CLS_raw_file(*args)
        self._versionObj = self.CLS_raw_version(self.DEF_mtlx_version)

        self._referenceSetObj = self.CLS_set_reference()
        self._lookSetObj = self.CLS_set_look()

        self._initDefXml()

    def _fileObject(self):
        return self._fileObj

    def filenameString(self):
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
        self._lookSetObject().addObject(referenceObject)

    def references(self):
        return self._lookSetObject().objects()

    def _lookSetObject(self):
        return self._lookSetObj

    def addLook(self, lookObject):
        self._lookSetObject().addObject(lookObject)

    def looks(self):
        return self._lookSetObject().objects()

    def _xmlAttributeObjectLis(self):
        return [self.version()]

    def _xmlChildList(self):
        return self.looks()


class Abc_Def(mtlCore.Mtd_MtlBasic):
    def _initAbcDef(self):
        self._nodeDefsDic = mtlConfigure.Def_Dag_Dic
        self._outputDefDic = mtlConfigure.Def_Output_Dic

    def load(self, *args):
        pass

    def getNodeDef(self, keyString):
        assert keyString in self._nodeDefsDic, u'Category "{}" is Non-Definition'.format(keyString)
        return self._nodeDefsDic.get(keyString, {})

    def getOutputDef(self, keyString):
        assert keyString in self._outputDefDic, u'Type "{}" is Non-Definition'.format(keyString)
        return self._outputDefDic.get(keyString, {})

    def nodeCategories(self):
        return self._nodeDefsDic.keys()


class Abc_TypeDef(Abc_Def):
    pass


class Abc_GeometryDef(mtlCore.Mtd_MtlBasic):
    def _initAbcGeometryDef(self):
        self._geometryDefDic = mtlConfigure.Def_Geometry_Dic
        self._geometryPropertyDefLis = self._geometryDefDic['property']
        self._geometryVisibilityDefLis = self._geometryDefDic['visibility']

        self._geometryPropertyDefDic = {}
        for i in self._geometryPropertyDefLis:
            nameString = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]
            self._geometryPropertyDefDic[nameString] = {
                self.Key_Type_String: valueTypeString,
                self.Key_Value_String: valueString
            }

        self._geometryVisibilityDefDic = {}
        for i in self._geometryVisibilityDefLis:
            nameString = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]
            self._geometryVisibilityDefDic[nameString] = {
                self.Key_Type_String: valueTypeString,
                self.Key_Value_String: valueString
            }

    def properties(self):
        return self._geometryPropertyDefLis

    def property(self, propertyNameString):
        return self._geometryPropertyDefDic[propertyNameString]

    def visibilities(self):
        return self._geometryVisibilityDefLis

    def visibility(self, visibilityNameString):
        return self._geometryVisibilityDefDic[visibilityNameString]


class Abc_DagDef(Abc_Def):
    def _initAbcDagDef(self, category):
        self._initAbcDef()

        self._categoryString = category

        self._nodeDefDic = self.getNodeDef(self._categoryString)

        self._typeString = self._nodeDefDic.get(self.Key_Type_String)

    def categoryString(self):
        return self._categoryString

    def typeString(self):
        return self._typeString

    @staticmethod
    def shadersetInputRaw():
        return [
            {
                u'name': u'surfaceshader',
                u'typeString': u'closure',
                u'valueString': u''
            },
            {
                u'name': u'displacementshader',
                u'typeString': u'closure',
                u'valueString': u''
            },
            {
                u'name': u'volumeshader',
                u'typeString': u'closure',
                u'valueString': u''
            }
        ]

    def inputRaw(self):
        return self._nodeDefDic.get(self.Key_Port, [])

    def outputRaw(self):
        return self._outputDefDic.get(self._typeString, [])
