# coding:utf-8
from LxMaterial import mtlConfigure, mtlCore


class Def_XmlObject(mtlCore.Basic):
    PROXY_XML_CLS = None

    xml_name_label_suffix = None

    xml_separator_attribute = ' '

    xml_key_element = None
    xml_key_attribute = None

    def _initAbcXml(self, attributes=None, children=None, elements=None):
        self._xmlObj = self.PROXY_XML_CLS(
            self.xml_key_element,
            attributes, children, elements
        )

    def _xmlAttributeDic(self):
        pass

    @classmethod
    def _toXmlString(cls, elementObject, indent=4):
        def addPrefixFnc_(prefix_, lString, rString):
            lis.append(u'{}<{}{}'.format(lString, prefix_, rString))

        def addAttributeFnc_(elementMethod, lString, rString):
            if elementMethod is not None:
                for k, v in elementMethod()._xmlAttributeDic().items():
                    lis.append(u'{}{}="{}"{}'.format(lString, k, v, rString))

        def addElementFnc_(elementObject_, lString, rString):
            xmlObject = elementObject_._xmlObj

            lString += defIndentString

            prefix = xmlObject.prefix()
            addPrefixFnc_(prefix, lString=lString, rString='')

            attributes = xmlObject.attributes()
            if attributes:
                [addAttributeFnc_(i, lString=cls.xml_separator_attribute, rString='') for i in attributes]

            children = xmlObject.children()
            if children:
                if isinstance(children, cls.module_types.MethodType):
                    children = children()

                lis.append(u'>\r\n')
                [addElementFnc_(i, lString, rString) for i in children]
                lis.append(u'{}</{}>\r\n'.format(lString, prefix))
            else:
                lis.append(u'{}/>\r\n'.format(cls.xml_separator_attribute))

            elements = xmlObject.elements()
            if elements:
                if isinstance(elements, cls.module_types.MethodType):
                    elements = elements()

                [addElementFnc_(i, lString='', rString='') for i in elements]

        defIndentString = ' ' * indent
        if hasattr(elementObject, '_xmlObj'):
            lis = [
                u'<?xml version="1.0"?>\r\n',
                u'<materialx version="1.36">\r\n',
                u'{}<xi:include href="materialx/arnold/nodedefs.mtlx" />\r\n'.format(defIndentString)
            ]

            addElementFnc_(elementObject, lString='', rString='')

            lis.append(
                u'</materialx>'
            )
            return ''.join(lis)
        return ''

    def __str__(self):
        return self._toXmlString(self)


class Abc_Raw(mtlCore.Basic):
    xml_key_attribute = None

    def _initAbcRaw(self, *args):
        if args:
            self._raw = args[0]
            self._rawType = type(self._raw)
        else:
            self._raw = None
            self._rawType = None

    def _initAbcRawDatum(self):
        self._raw = None
        self._rawType = None

    @staticmethod
    def _toListSplit(lis, splitCount):
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

    def _xmlAttributeDic(self):
        """
        :return: dict
        """
        return self.cls_order_dic(
            [
                (self.xml_key_attribute, self.toString())
            ]
        )

    def __eq__(self, other):
        """
        :param other: typed raw
        :return: bool
        """
        return self.raw() == other.raw()


class Abc_RawXml(object):
    def _initAbcRawXml(self, *args):
        prefixString, attributes, children, elements = args

        self._prefixString = prefixString

        self._attributeObjLis = attributes
        self._childObjLis = children
        self._elementObjLis = elements

    def prefix(self):
        return self._prefixString

    def attributes(self):
        return self._attributeObjLis

    def children(self):
        return self._childObjLis

    def elements(self):
        return self._elementObjLis


class Abc_Path(Abc_Raw):
    RAW_CLS = None

    separator_path = None

    def _initAbcPath(self, *args):
        self._initAbcRaw(*args)
        if self.hasRaw():
            self._rawLis = [self.RAW_CLS(i) for i in self._raw.split(self.separator_path)]
        else:
            self._rawLis = None

    def separator(self):
        return self.separator_path

    @staticmethod
    def _toStringsMethod(pathString, pathsep):
        if pathString.startswith(pathsep):
            return pathString.split(pathsep)[1:]
        else:
            return pathString.split(pathsep)

    def createByRaw(self, *args):
        pass

    def setLastRaw(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._rawLis[-1].setRaw(nameString)

    def lastRaw(self):
        """
        :return: str
        """
        if self.hasRaw():
            return self._rawLis[-1].raw()

    def fullpathName(self):
        """
        :return: str
        """
        return self.raw()


class Abc_Dagpath(Def_XmlObject):
    RAW_PATH_NODE_CLS = None
    RAW_PATH_ATTRIBUTE_CLS = None

    category_path = None

    def _initAbcDagpath(self, nodeFullpathName, attributeFullpathName=None):
        if isinstance(nodeFullpathName, str) or isinstance(nodeFullpathName, unicode):
            self._nodePath = self.RAW_PATH_NODE_CLS(nodeFullpathName)
        else:
            self._nodePath = nodeFullpathName

        self._attributePath = self.RAW_PATH_ATTRIBUTE_CLS(attributeFullpathName)

    def createByRaw(self, *args):
        pass

    def __nodePathObject(self):
        return self._nodePath

    def nodePath(self):
        """
        :return: object of Path
        """
        return self.__nodePathObject()

    def setNodeName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__nodePathObject().setLastRaw(nameString)

    def nodeName(self):
        """
        :return: str
        """
        return self.__nodePathObject().lastRaw()

    def nodeFullpathName(self):
        """
        :return: str
        """
        return self.__nodePathObject().toString()

    def __attributePathObject(self):
        return self._attributePath

    def attributePath(self):
        """
        :return: object of Path
        """
        return self.__attributePathObject()

    def setAttributeName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__attributePathObject().setLastRaw(nameString)

    def attributeName(self):
        """
        :return: str
        """
        return self.__attributePathObject().lastRaw()

    def attributeFullpathName(self):
        """
        :return: str
        """
        return self.__attributePathObject().toString()

    def name(self):
        """
        :return: str
        """
        if self.__attributePathObject().hasRaw():
            return self.attributeName()
        return self.nodeName()

    def fullpathName(self):
        """
        :return: str
        """
        if self.__attributePathObject().hasRaw():
            return '.'.join([self.nodeFullpathName(), self.attributeFullpathName()])
        return self.nodeFullpathName()

    def _xmlAttributeDic(self):
        """
        :return: dict
        """
        return self.cls_order_dic(
            [
                (self.xml_key_attribute, self.name())
            ]
        )


class Abc_ObjectSet(Def_XmlObject):
    separator_object = ','
    # noinspection PyUnusedLocal
    def _initAbcObjectSet(self, *args):
        self._objectLis = []
        self._objectDic = {}
        self._objectCount = 0

        self._objectFilterStr = None

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

    def addObject(self, key, obj):
        assert key not in self._objectDic, '''Key is Exist.'''
        self._objectLis.append(obj)
        self._objectDic[key] = obj
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

    def objectWithKey(self, key):
        """
        :param key: key
        :return: bool
        """
        assert key not in self._objectDic, '''Key is Non - Exist.'''
        return self._objectDic[key]

    def hasObjectWithKey(self, key):
        """
        :param key: key
        :return: bool
        """
        return key in self._objectDic

    def toString(self):
        return self.separator_object.join([i.toString() for i in self.objects()])

    def __len__(self):
        """
        :return: int
        """
        return self.objectsCount()

    def _xmlAttributeDic(self):
        return self.cls_order_dic(
            [
                (self.xml_key_attribute, self.toString())
            ]
        )


class Abc_RawString(Def_XmlObject, Abc_Raw):
    def _initAbcRawString(self, *args):
        self._initAbcRaw(*args)

    def toString(self):
        return unicode(self._raw)

    def _xmlAttributeDic(self):
        """
        :return: dict
        """
        return self.cls_order_dic(
            [
                (self.xml_key_attribute, self.toString())
            ]
        )


class Abc_RawDatum(Abc_Raw):
    RAW_CLS = None

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
        assert args is not (), u'Argument must not be Empty.'

        if isinstance(args[0], (str, unicode)):
            self.createByString(*args)
        else:
            self.createByRaw(*args)

    def createByRaw(self, *args):
        """
        :param args: raw_type
        :return: None
        """
        assert args is not (), u'Argument must not be Empty.'
        raw = args[0]
        assert isinstance(raw, self.raw_type), u'Argument Error, "arg" Must "raw_type".'

        self.setRaw(self.RAW_CLS(raw))

    def createByString(self, *args):
        assert args is not (), u'Argument must not be Empty.'
        assert isinstance(args[0], (str, unicode))
        if args[0]:
            self.createByRaw(self.RAW_CLS(args[0]))

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

    def _xmlAttributeDic(self):
        return self.cls_order_dic(
            [
                (self.xml_key_attribute, self.toString())
            ]
        )


class Abc_RawDatumset(Abc_Raw):
    SET_CHILD_CLS = None

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

        [self.addChild(self.SET_CHILD_CLS(self, i)) for i in raw]

        self.setRaw(raw)

    def createByString(self, *args):
        assert args is not (), u'Argument must not be Empty.'
        assert isinstance(args[0], (str, unicode))
        if args[0]:
            valueStringLis = [i.lstrip().rstrip() for i in args[0].split(mtlConfigure.Separator_Raw_Basic)]
            raw = self._toListSplit(valueStringLis, self.childValueSize())
            self.createByRaw(raw)

    def toString(self):  # to override
        """
        :return: str
        """
        return self.datum_string_separator.join([i.toString() for i in self.children()])

    def typeString(self):
        return self._valueTypeStringPattern[0]

    def valueSize(self):
        return self._valueSizePattern[0]

    def childValueSize(self):
        return self._valueSizePattern[1]

    def addChild(self, datumObject):
        self._childLis.append(datumObject)

    def children(self):
        return self._childLis

    def childrenCount(self):
        return len(self._childLis)

    def hasChildren(self):
        return self._childLis != []

    def childAt(self, index):
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

    def _xmlAttributeDic(self):
        return self.cls_order_dic(
            [
                (self.xml_key_attribute, self.toString())
            ]
        )

    def __len__(self):
        """
        :return: int
        """
        return self.childrenCount()


class Abc_Value(Def_XmlObject):
    RAW_TYPE_CLS = None
    RAW_DATUM_CLS = None

    value_type_string_pattern = None
    sub_value_type_string = None

    value_size_pattern = None

    def _initAbcValue(self, *args):
        self._typeObj = self.RAW_TYPE_CLS(self.value_type_string_pattern[0])
        self._rawDatumObj = self.RAW_DATUM_CLS(self, *args)

    def _typeObject(self):
        return self._typeObj

    def type(self):
        """
        :return: object of Type
        """
        return self._typeObject()

    def typeString(self):
        """
        :return: str
        """
        return self._typeObject().toString()

    def _rawDatumObject(self):
        return self._rawDatumObj

    def datum(self):
        """
        :return: object of Datum
        """
        return self._rawDatumObject()

    def raw(self):
        """
        :return: raw of typed
        """
        return self._rawDatumObject().raw()

    def hasRaw(self):
        """
        :return: bool
        """
        return self._rawDatumObject().hasRaw()

    def toString(self):
        """
        :return: str
        """
        return self._rawDatumObject().toString()

    def _xmlAttributeDic(self):
        return self.cls_order_dic(
            [
                (self._typeObject().xml_key_attribute, self._typeObject().toString()),
                (self._rawDatumObject().xml_key_attribute, self._rawDatumObject().toString())
            ]
        )

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
        return self._rawDatumObject()._toPrintString()


class Abc_Port(Def_XmlObject):
    RAW_DAGPATH_CLS = None
    SET_CHILD_CLS = None

    def _initAbcPort(self, nodeFullpathName, attributeFullpathName):
        self._dagpathObj = self.RAW_DAGPATH_CLS(nodeFullpathName, attributeFullpathName)
        self._childSetObj = self.SET_CHILD_CLS()

        self._valueObj = None
        self._defValue = None

        self._input = None
        self._parent = None

        self._initAbcXml(attributes=[self._dagpathObject, self._valueObject])

    def createByRaw(self, *args):
        pass

    def _dagpathObject(self):
        return self._dagpathObj

    def dagpath(self):
        return self._dagpathObject()

    def fullpathName(self):
        """
        :return: str
        """
        return self._dagpathObject().fullpathName()

    def nodeName(self):
        """
        :return: str
        """
        return self._dagpathObject().nodeName()

    def nodeFullpathName(self):
        """
        :return: str
        """
        return self._dagpathObject().nodeFullpathName()

    def setAttributeName(self, nameString):
        self._dagpathObject().setAttributeName(nameString)

    def attributeName(self):
        """
        :return: str
        """
        return self._dagpathObject().attributeName()

    def attributeFullpathName(self):
        """
        :return: str
        """
        return self._dagpathObject().attributeFullpathName()

    def _valueObject(self):
        return self._valueObj

    def setValue(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._valueObj = valueObject

    def value(self):
        return self._valueObject()

    def hasValue(self):
        """
        :return: bool
        """
        return self._valueObject() is not None

    def valueType(self):
        return self._valueObject()

    def valueTypeString(self):
        return self._valueObject().typeString()

    def valueString(self):
        return self._valueObject().toString()

    def _defValueObject(self):
        return self._defValue

    def setDefValue(self, valueObject):
        self._defValue = valueObject

    def defValue(self):
        return self._defValueObject()

    def hasDefValue(self):
        """
        :return: bool
        """
        return self._defValueObject() is not None

    def _childSetObject(self):
        return self._childSetObj

    def children(self):
        """
        :return: list(object of Attribute, ...)
        """
        return self._childSetObject().objects()

    def hasChildren(self):
        """
        :return: bool
        """
        return self._childSetObject().hasObjects()

    def childrenCount(self):
        """
        :return: int
        """
        return self._childSetObject().objectsCount()

    def childAt(self, index):
        """
        :param index: int
        :return: object of Attribute
        """
        return self._childSetObject().objectAt(index)

    def childNameAt(self, index):
        """
        :param index: int
        :return: object of Attribute
        """
        return self.childAt(index).name()

    def childValueAt(self, index):
        """
        :param index: int
        :return: object of typed Value
        """
        return self.childAt(index).value()

    def childValueStringAt(self, index):
        """
        :param index: int
        :return: str
        """
        return self.childAt(index).valueString()

    def addChild(self, portObject):
        """
        :param portObject: object of Attribute
        :return: None
        """
        portObject._setParent(self)
        self._childSetObject().addObject(portObject.fullpathName(), portObject)

    def _inputObject(self):
        return self._input

    def setInputPort(self, portObject):
        """
        :param portObject: object of Attribute
        :return: None
        """
        self._input = portObject

    def importPort(self):
        """
        :return: object of Attribute
        """
        return self._inputObject()

    def hasInputPort(self):
        """
        :return: bool
        """
        return self._inputObject() is not None

    def _parentObject(self):
        return self._parent

    def _setParent(self, parentObject):
        self._parent = parentObject

    def parent(self):
        """
        :return: object of Attribute
        """
        return self._parentObject()

    def hasParent(self):
        """
        :return: bool
        """
        return self._parentObject() is not None

    def parentFullpathName(self):
        """
        :return: str
        """
        return self._parentObject().fullpathName()

    def parentAttributeName(self):
        """
        :return: str
        """
        return self._parentObject().attributeName()

    def parentFullAttributeName(self):
        """
        :return: str
        """
        return self._parentObject().attributeFullpathName()

    def _xmlAttributeDic(self):
        return self.cls_order_dic(
            [
                (self.xml_key_attribute, self._dagpathObject().fullpathName())
            ]
        )


class Abc_Dag(Def_XmlObject):
    RAW_TYPE_CLS = None
    RAW_CATEGORY_CLS = None
    RAW_DAGPATH_CLS = None

    SET_PORT_INPUT_CLS = None
    SET_CHILD_CLS = None

    PORT_INPUT_CLS = None
    DEF_CLS = None

    value_cls_dic = {}

    def _initAbcDag(self, categoryString, fullpathName):
        self._categoryObj = self.RAW_CATEGORY_CLS(categoryString)
        self._dagpathObj = self.RAW_DAGPATH_CLS(fullpathName)

        self._defObj = self.DEF_CLS(categoryString)
        self._typeObj = self.RAW_TYPE_CLS(categoryString)

        self._inputPortSetObj = self.SET_PORT_INPUT_CLS()

        self._childSetObj = self.SET_CHILD_CLS()

        portRaw = self._defObj.portRaw()
        for i in portRaw:
            attributeName = i[self.Key_Name]
            valueTypeString = i[self.Key_Type_String]
            valueString = i[self.Key_Value_String]

            portObject = self.PORT_INPUT_CLS(self.fullpathName(), attributeName)
            valueCls = self.value_cls_dic[valueTypeString]

            portObject.setValue(
                valueCls(valueString)
            )

            self.addInputPort(portObject)

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
        return self._typeObject()

    def typeString(self):
        return self._typeObject().raw()

    def _categoryObject(self):
        return self._categoryObj
    
    def setCategory(self, categoryString):
        """
        :param categoryString: str
        :return: None
        """
        self._categoryObject().setRaw(categoryString)

    def categoryString(self):
        """
        :return: str
        """
        return self._categoryObject().raw()

    def _dagpathObject(self):
        return self._dagpathObj

    def dagpath(self):
        """
        :return: object of Raw_Dagpath
        """
        return self._dagpathObject()
    
    def setFullpathName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObject().setRaw(nameString)

    def fullpathName(self):
        """
        :return: str
        """
        return self._dagpathObject().fullpathName()

    def setNodeName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObject().setNodeName(nameString)

    def nodeName(self):
        """
        :return: str
        """
        return self._dagpathObject().nodeName()

    def nodeFullpathName(self):
        """
        :return: str
        """
        return self._dagpathObject().nodeFullpathName()

    def _childSetObject(self):
        return self._childSetObj

    def children(self):
        """
        :return: list(object of Dag_Node, ...)
        """
        return self._childSetObject().objects()

    def hasChildren(self):
        """
        :return: bool
        """
        return self._childSetObject().hasObjects()

    def childrenCount(self):
        """
        :return: int
        """
        return self._childSetObject().objectsCount()

    def childAt(self, index):
        """
        :param index: int
        :return: object of Dag_Node
        """
        return self._childSetObject().objectAt(index)

    def addChild(self, nodeObject):
        """
        :param nodeObject: object of Dag_Node
        :return: None
        """
        self._childSetObject().addObject(nodeObject.fullpathName(), nodeObject)

    def __inputPortSetObject(self):
        return self._inputPortSetObj

    def inputPorts(self):
        """
        :return: list(object or attribute, ...)
        """
        return self.__inputPortSetObject().objects()

    def hasInputPorts(self):
        """
        :return: bool
        """
        return self.__inputPortSetObject().hasObjects()

    def addInputPort(self, portObject):
        """
        :param portObject: object of Attribute
        :return: None
        """
        self.__inputPortSetObject().addObject(
            portObject.attributeFullpathName(),
            portObject
        )

    def toString(self):
        return self.fullpathName()


class Abc_DagShader(Abc_Dag):
    PORT_OUTPUT_ClS = None

    port_output_name_string = None

    def _initAbcShader(self, *args):
        self._initAbcDag(*args)

        self._outputPortObj = self.PORT_OUTPUT_ClS(
            self.fullpathName(),
            self.port_output_name_string
        )

        self._initAbcXml(
            attributes=[self._dagpathObject, self._categoryObject, self._outputPortObject],
            children=self.inputPorts
        )

    def _outputPortObject(self):
        return self._outputPortObj

    def outputPort(self):
        return self._outputPortObject()


class Abc_DagGeometry(Abc_Dag):
    def _initAbcGeometry(self, *args):
        self._initAbcDag(*args)


class Abc_Shaderset(Def_XmlObject):
    RAW_DAGPATH_CLS = None
    SET_SHADER_CLS = None

    def _initAbcShaderset(self, fullpathName):
        self._dagpathObj = self.RAW_DAGPATH_CLS(fullpathName)

        self._shaderSetObj = self.SET_SHADER_CLS()

        self._initAbcXml(
            attributes=[self._dagpathObject],
            children=self.shaders
        )

    def _dagpathObject(self):
        return self._dagpathObj

    def _shaderSetObject(self):
        return self._shaderSetObj

    def dagpath(self):
        """
        :return: object of Raw_Dagpath
        """
        return self._dagpathObject()

    def setFullpathName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObject().setRaw(nameString)

    def fullpathName(self):
        """
        :return: str
        """
        return self._dagpathObject().fullpathName()

    def setNodeName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObject().setNodeName(nameString)

    def nodeName(self):
        """
        :return: str
        """
        return self._dagpathObject().nodeName()

    def nodeFullpathName(self):
        """
        :return: str
        """
        return self._dagpathObject().nodeFullpathName()

    def addShader(self, shaderObject):
        self._shaderSetObject().addObject(
            shaderObject.fullpathName(),
            shaderObject
        )

    def shaders(self):
        return self._shaderSetObject().objects()

    def _xmlAttributeDic(self):
        return self.cls_order_dic(
            [
                (self.xml_key_attribute, self.fullpathName())
            ]
        )


class Abc_Portset(Def_XmlObject):
    RAW_DAGPATH_CLS = None
    SET_PORT_INPUT_CLS = None

    def _initAbcPortset(self, *args):
        self._dagpathObj = self.RAW_DAGPATH_CLS(*args)

        self._inputPortSetObj = self.SET_PORT_INPUT_CLS()

    def _dagpathObject(self):
        return self._dagpathObj

    def __inputPortSetObject(self):
        return self._inputPortSetObj

    def dagpath(self):
        """
        :return: object of Raw_Dagpath
        """
        return self._dagpathObject()

    def setFullpathName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObject().setRaw(nameString)

    def fullpathName(self):
        """
        :return: str
        """
        return self._dagpathObject().fullpathName()

    def setNodeName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._dagpathObject().setNodeName(nameString)

    def nodeName(self):
        """
        :return: str
        """
        return self._dagpathObject().nodeName()

    def addInputPort(self, portObject):
        """
        :param portObject: object of Attribute
        :return: None
        """
        self.__inputPortSetObject().addObject(portObject.fullpathName(), portObject)

    def inputPorts(self):
        """
        :return: list(object or port, ...)
        """
        return self.__inputPortSetObject().objects()

    def hasInputPorts(self):
        """
        :return: bool
        """
        return self.__inputPortSetObject().hasObjects()


class Abc_Graph(mtlCore.Basic):
    RAW_NAME_CLS = None
    SET_NODE_CLS = None
    SET_OUTPUT_CLS = None

    def _initAbcGraph(self):
        self._nameObj = self.RAW_NAME_CLS()

        self._nodeSet = self.SET_NODE_CLS()
        self._outputSet = self.SET_OUTPUT_CLS()

    def _nameObject(self):
        return self._nameObj

    def __nodeSetObject(self):
        return self._nodeSet

    def __outputSetObject(self):
        return self._outputSet

    def name(self):
        """
        :return: str
        """
        return self._nameObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObject().setRaw(nameString)

    def addNode(self, nodeObject):
        """
        :param nodeObject: object of Dag_Node
        :return: None
        """
        self.__nodeSetObject().addObject(nodeObject.fullpathName(), nodeObject)

    def nodes(self):
        """
        :return: list(object or node, ...)
        """
        return self.__nodeSetObject().objects()

    def nodesCount(self):
        """
        :return: int
        """
        return self.__nodeSetObject().objectsCount()

    def hasNodes(self):
        """
        :return: bool
        """
        return self.__nodeSetObject().hasObjects()

    def addOutput(self, outputObject):
        """
        :param outputObject: object of Output
        :return: None
        """
        self.__outputSetObject().addObject(outputObject.fullpathName(), outputObject)

    def outputs(self):
        """
        :return: list(object or output, ...)
        """
        return self.__outputSetObject().objects()

    def outputsCount(self):
        """
        :return: int
        """
        return self.__outputSetObject().objectsCount()

    def hasOutputs(self):
        """
        :return: bool
        """
        return self.__outputSetObject().hasObjects()


class Abc_Collection(mtlCore.Basic):
    RAW_NAME_CLS = None
    SET_GEOMETRY_CLS = None
    COLLECTION_SET_CLS = None

    def _initAbcCollection(self):
        self._nameObj = self.RAW_NAME_CLS()
        self._geometrySet = self.SET_GEOMETRY_CLS()
        self._collectionSet = self.COLLECTION_SET_CLS()

    def _nameObject(self):
        return self._nameObj

    def name(self):
        """
        :return: str
        """
        return self._nameObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObject().setRaw(nameString)

    def _geometrySetObject(self):
        return self._geometrySet

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Dag_Geometry
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

    def geometryFullpathNames(self):
        """
        :return: list(str, ...)
        """
        return [i.fullpathName() for i in self.geometries()]

    def geometryNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nodeName() for i in self.geometries()]

    def geometryFullNodeNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nodeFullpathName() for i in self.geometries()]

    def __collectionSetObject(self):
        return self._collectionSet

    def addCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self.__collectionSetObject().addObject(collectionObject.fullpathName(), collectionObject)

    def collections(self):
        """
        :return: list(object of Collection, ...)
        """
        return self.__collectionSetObject().objects()

    def hasCollections(self):
        """
        :return: bool
        """
        return self.__collectionSetObject().hasObjects()

    def collectionNames(self):
        """
        :return: list(str, ...)
        """
        return [i.name() for i in self.collections()]


class Abc_Assign(Def_XmlObject):
    RAW_NAME_CLS = None
    SET_GEOMETRY_CLS = None

    separator_geometry = None

    def _initAbcAssign(self, *args):
        self._nameObj = self.RAW_NAME_CLS(*args)

        self._geometrySet = self.SET_GEOMETRY_CLS()
        self._collectionObj = None

    def _nameObject(self):
        return self._nameObj

    def name(self):
        """
        :return: str
        """
        return self._nameObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObject().setRaw(nameString)

    def _geometrySetObject(self):
        return self._geometrySet

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Dag_Geometry
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

    def geometryFullpathNames(self):
        """
        :return: list(str, ...)
        """
        return [i.fullpathName() for i in self.geometries()]

    def geometryNodeNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nodeName() for i in self.geometries()]

    def geometryFullNodeNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nodeFullpathName() for i in self.geometries()]

    def geometryString(self):
        return self.separator_geometry.join(self.geometryFullpathNames())

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
        return self._collectionObj.name()


class Abc_AsnShaderset(Abc_Assign):
    SHADERSET_CLS = None

    def _initAbcMaterialAssign(self, *args):
        self._initAbcAssign(*args)

        self._shadersetObj = None

        self._initAbcXml(
            attributes=[self._nameObject, self._shadersetObject, self._geometrySetObject]
        )

    def _shadersetObject(self):
        return self._shadersetObj

    def addShaderset(self, shadersetObject):
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

    def _xmlAttributeDic(self):
        return self.cls_order_dic(
            [
                (self._shadersetObject().xml_key_attribute, self._shadersetObject().name())
            ]
        )


class Abc_AsnPortset(Abc_Assign):
    PORTSET_CLS = None

    def _initAbcPortsetAssign(self, *args):
        self._initAbcAssign(*args)

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
        return self.__portsetObject().name()


class Abc_Look(Def_XmlObject):
    RAW_NAME_CLS = None
    SET_ASSIGN_CLS = None

    def _initAbcLook(self, *args):
        self._nameObj = self.RAW_NAME_CLS(*args)

        self._assignSetObj = self.SET_ASSIGN_CLS()

        self._initAbcXml(
            attributes=[self._nameObject],
            children=self.assigns,
            elements=self.shadersets
        )

    def _nameObject(self):
        return self._nameObj

    def name(self):
        return self._nameObj.toString()

    def __assignSetObject(self):
        return self._assignSetObj

    def addAssign(self, assignObject):
        self.__assignSetObject().addObject(
            assignObject.name(),
            assignObject
        )

    def assigns(self):
        return self.__assignSetObject().objects()

    def shadersets(self):
        return [i.shaderset() for i in self.assigns()]


class Abc_Include(mtlCore.Basic):
    pass


class Abc_Asset(mtlCore.Basic):
    SET_LOOK_CLS = None
    RAW_FILE_CLS = None

    def _initAbcAsset(self, *args):
        pass


class Abc_Def(mtlCore.Basic):
    def _initAbcDef(self):
        self._nodeDefsDic = mtlConfigure.Def_Node_Dic

    def load(self, *args):
        pass

    def get(self, key):
        assert key in self._nodeDefsDic, u'Category "{}" is Non-Definition'.format(key)
        return self._nodeDefsDic.get(key, {})


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
