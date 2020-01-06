# coding:utf-8
from LxMaterial import mtlConfigure


class Abc_Xml(object):
    def _initAbcXml(self):
        pass

    def categoryString(self):
        pass

    def attribute(self):
        pass

    def children(self):
        pass


class Abc_Raw(object):
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

    @staticmethod
    def _createByStringMethod(*args):
        pass

    @staticmethod
    def _toJsonStringMethod(*args):
        pass

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
        return self.raw() == other.raw()


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

    @staticmethod
    def _toJsonStringMethod(rawObjects, pathsep):
        return pathsep + pathsep.join([i.raw() for i in rawObjects])

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


class Abc_Dagpath(mtlConfigure.Basic):
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

    def _strJsonRaw(self):
        return {
            self.Key_Name: self.name(),
            self.Key_FullpathName: self.fullpathName()
        }

    def __str__(self):
        return self._toJsonStringMethod(self._strJsonRaw())


class Abc_Nodepath(object):
    pass


class Abc_ObjectSet(object):
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

    def __len__(self):
        """
        :return: int
        """
        return self.objectsCount()


class Abc_Type(Abc_Raw):
    def _initAbcType(self, *args):
        self._initAbcRaw(*args)

    def toString(self):
        return unicode(self._raw)


class Abc_Name(Abc_Raw):
    def _initAbcName(self, *args):
        self._initAbcRaw(*args)

    def toString(self):
        return unicode(self._raw)


class Abc_Datum(Abc_Raw):
    RAW_CLS = None

    raw_type = None
    raw_def = None

    def _initAbcDatum(self, *args):
        self._initAbcRawDatum()

        if isinstance(args[0], Abc_Value):
            self._valueObj = args[0]
            self._valueTypeStringPattern = self._valueObj.value_type_string_pattern
            self._valueSizePattern = self._valueObj.value_size_pattern
        elif isinstance(args[0], Abc_Datumset):
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

    def __str__(self):
        """
        :return: str
        """
        return self._toPrintString()


class Abc_Datumset(Abc_Raw):
    SET_CHILD_CLS = None

    datum_string_separator = None
    raw_def = None

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

    def _initAbcDatumSet(self, *args):
        self._initAbcRawDatum()

        if isinstance(args[0], Abc_Value):
            self._valueObj = args[0]
            self._valueTypeStringPattern = self._valueObj.value_type_string_pattern
            self._valueSizePattern = self._valueObj.value_size_pattern
        elif isinstance(args[0], Abc_Datumset):
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

    def __str__(self):
        """
        :return: str
        """
        return self._toPrintString()

    def __len__(self):
        """
        :return: int
        """
        return self.childrenCount()


class Abc_Value(object):
    RAW_TYPE_CLS = None
    DATUM_CLS = None

    value_type_string_pattern = None
    sub_value_type_string = None

    value_size_pattern = None

    def _initAbcValue(self, *args):
        self._typeObj = self.RAW_TYPE_CLS(self.value_type_string_pattern[0])
        self._datumObj = self.DATUM_CLS(self, *args)

    def __typeObject(self):
        return self._typeObj

    def type(self):
        """
        :return: str
        """
        return self.__typeObject()

    def typeString(self):
        return self.__typeObject().toString()

    def __datumObject(self):
        return self._datumObj

    def datum(self):
        """
        :return: object of Data
        """
        return self.__datumObject()

    def raw(self):
        """
        :return: raw of typed
        """
        return self.__datumObject().raw()

    def hasRaw(self):
        """
        :return: bool
        """
        return self.__datumObject().hasRaw()

    def toString(self):
        """
        :return: str
        """
        return self.__datumObject().toString()

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
        return self.__datumObject()._toPrintString()


class Abc_Port(mtlConfigure.Basic):
    RAW_DAGPATH_CLS = None
    SET_CHILD_CLS = None

    xml_prefix_label = None

    def _initAbcPort(self, nodeFullpathName, attributeFullpathName):
        self._dagpathObj = self.RAW_DAGPATH_CLS(nodeFullpathName, attributeFullpathName)
        self._childSetObj = self.SET_CHILD_CLS()

        self._value = None
        self._defValue = None

        self._input = None
        self._parent = None

    def createByRaw(self, *args):
        pass

    def __dagpathObject(self):
        return self._dagpathObj

    def dagpath(self):
        return self.__dagpathObject()

    def fullpathName(self):
        """
        :return: str
        """
        return self.__dagpathObject().fullpathName()

    def nodeName(self):
        """
        :return: str
        """
        return self.__dagpathObject().nodeName()

    def nodeFullpathName(self):
        """
        :return: str
        """
        return self.__dagpathObject().nodeFullpathName()

    def setAttributeName(self, nameString):
        self.__dagpathObject().setAttributeName(nameString)

    def attributeName(self):
        """
        :return: str
        """
        return self.__dagpathObject().attributeName()

    def attributeFullpathName(self):
        """
        :return: str
        """
        return self.__dagpathObject().attributeFullpathName()

    def __valueObject(self):
        return self._value

    def setValue(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._value = valueObject

    def value(self):
        return self.__valueObject()

    def hasValue(self):
        """
        :return: bool
        """
        return self.__valueObject() is not None

    def valueType(self):
        return self.__valueObject()

    def valueTypeString(self):
        return self.__valueObject().typeString()

    def valueString(self):
        return self.__valueObject().toString()

    def __defValueObject(self):
        return self._defValue

    def setDefValue(self, valueObject):
        self._defValue = valueObject

    def defValue(self):
        return self.__defValueObject()

    def hasDefValue(self):
        """
        :return: bool
        """
        return self.__defValueObject() is not None

    def __childSetObject(self):
        return self._childSetObj

    def children(self):
        """
        :return: list(object of Attribute, ...)
        """
        return self.__childSetObject().objects()

    def hasChildren(self):
        """
        :return: bool
        """
        return self.__childSetObject().hasObjects()

    def childrenCount(self):
        """
        :return: int
        """
        return self.__childSetObject().objectsCount()

    def childAt(self, index):
        """
        :param index: int
        :return: object of Attribute
        """
        return self.__childSetObject().objectAt(index)

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

    def addChild(self, attributeObject):
        """
        :param attributeObject: object of Attribute
        :return: None
        """
        attributeObject._setParent(self)
        self.__childSetObject().addObject(attributeObject.fullpathName(), attributeObject)

    def _inputObject(self):
        return self._input

    def setInput(self, attributeObject):
        """
        :param attributeObject: object of Attribute
        :return: None
        """
        self._input = attributeObject

    def input(self):
        """
        :return: object of Attribute
        """
        return self._inputObject()

    def hasInput(self):
        """
        :return: bool
        """
        return self._inputObject() is not None

    def inputFullpathName(self):
        """
        :return: str
        """
        return self.input().fullpathName()

    def inputNodeName(self):
        """
        :return: str
        """
        return self.input().nodeName()

    def inputFullNodeName(self):
        """
        :return: str
        """
        return self.input().nodeFullpathName()

    def inputAttributeName(self):
        """
        :return: str
        """
        return self.input().attributeName()

    def inputAttributeFullpathName(self):
        """
        :return: str
        """
        return self.input().attributeFullpathName()

    def __parentObject(self):
        return self._parent

    def _setParent(self, parentObject):
        self._parent = parentObject

    def parent(self):
        """
        :return: object of Attribute
        """
        return self.__parentObject()

    def hasParent(self):
        """
        :return: bool
        """
        return self.__parentObject() is not None

    def parentFullpathName(self):
        """
        :return: str
        """
        return self.__parentObject().fullpathName()

    def parentAttributeName(self):
        """
        :return: str
        """
        return self.__parentObject().attributeName()

    def parentFullAttributeName(self):
        """
        :return: str
        """
        return self.__parentObject().attributeFullpathName()


class Abc_Dag(mtlConfigure.Basic):
    RAW_TYPE_CLS = None
    RAW_CATEGORY_CLS = None
    RAW_DAGPATH_CLS = None
    SET_CHILD_CLS = None
    SET_PORT_CLS = None
    PORT_CLS = None
    DEF_CLS = None

    xml_prefix_label = None

    value_cls_dic = {}

    def _initAbcDag(self, categoryString, fullpathName):
        self._categoryObj = self.RAW_CATEGORY_CLS(categoryString)
        self._dagpathObj = self.RAW_DAGPATH_CLS(fullpathName)

        self._defObj = self.DEF_CLS(categoryString)
        self._typeObj = self.RAW_TYPE_CLS(self._defObj.typeString())

        self._childSetObj = self.SET_CHILD_CLS()
        self._attributeSet = self.SET_PORT_CLS()

        attributeRaw = self._defObj.attribute()
        for k, v in attributeRaw.items():
            attribute = self.PORT_CLS(self.fullpathName(), k)
            valueTypeString = v[self.Key_Type_String]
            valueString = v[self.Key_Value_String]

            attribute.setValue(self.value_cls_dic[valueTypeString](valueString))
            self.addAttribute(attribute)

    def loadDef(self, *args):
        pass

    def createByRaw(self, *args):
        pass

    def __typeObject(self):
        return self._typeObj

    def type(self):
        """
        :return: str
        """
        return self.__typeObject()

    def typeString(self):
        return self.__typeObject().raw()

    def __categoryObject(self):
        return self._categoryObj
    
    def setCategory(self, categoryString):
        """
        :param categoryString: str
        :return: None
        """
        self.__categoryObject().setRaw(categoryString)

    def categoryString(self):
        """
        :return: str
        """
        return self.__categoryObject().raw()

    def __dagpathObject(self):
        return self._dagpathObj

    def dagpath(self):
        """
        :return: object of Raw_Dagpath
        """
        return self.__dagpathObject()
    
    def setFullpathName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__dagpathObject().setRaw(nameString)

    def fullpathName(self):
        """
        :return: str
        """
        return self.__dagpathObject().fullpathName()

    def setNodeName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__dagpathObject().setNodeName(nameString)

    def nodeName(self):
        """
        :return: str
        """
        return self.__dagpathObject().nodeName()

    def nodeFullpathName(self):
        """
        :return: str
        """
        return self.__dagpathObject().nodeFullpathName()

    def __childSetObject(self):
        return self._childSetObj

    def children(self):
        """
        :return: list(object of Dag_Node, ...)
        """
        return self.__childSetObject().objects()

    def hasChildren(self):
        """
        :return: bool
        """
        return self.__childSetObject().hasObjects()

    def childrenCount(self):
        """
        :return: int
        """
        return self.__childSetObject().objectsCount()

    def childAt(self, index):
        """
        :param index: int
        :return: object of Dag_Node
        """
        return self.__childSetObject().objectAt(index)

    def addChild(self, nodeObject):
        """
        :param nodeObject: object of Dag_Node
        :return: None
        """
        self.__childSetObject().addObject(nodeObject.fullpathName(), nodeObject)

    def __portSetObject(self):
        return self._attributeSet

    def attributes(self):
        """
        :return: list(object or attribute, ...)
        """
        return self.__portSetObject().objects()

    def hasAttributes(self):
        """
        :return: bool
        """
        return self.__portSetObject().hasObjects()

    def attributesCount(self):
        """
        :return: int
        """
        return self.__portSetObject().objectsCount()

    def attributeAt(self, index):
        """
        :param index: int
        :return: object of Attribute
        """
        return self.__portSetObject().objectAt(index)

    def addAttribute(self, attributeObject):
        """
        :param attributeObject: object of Attribute
        :return: None
        """
        self.__portSetObject().addObject(
            attributeObject.attributeFullpathName(),
            attributeObject
        )


class Abc_Shader(Abc_Dag):
    shader_output_type_string = None
    xml_prefix_label = None

    def _initAbcShader(self, *args):
        self._initAbcDag(*args)

    def _xmlStrRaw(self):
        return {
            self.Key_Label: self.xml_prefix_label,
            self.Key_Attribute: {
                self.Atr_Xml_Name: self.fullpathName(),
                self.Atr_Xml_Node: self.categoryString(),
                self.Atr_Xml_Shader_Output_Type: self.shader_output_type_string
            },
            self.Key_Children: self.attributes()
        }


class Abc_Geometry(Abc_Dag):
    def _initAbcGeometry(self, *args):
        self._initAbcDag(*args)


class Abc_Element(mtlConfigure.Basic):
    xml_name_prefix_label = None
    xml_name_suffix_label = None


class Abc_Material(Abc_Element):
    RAW_DAGPATH_CLS = None
    SET_SHADER_CLS = None

    def _initAbcMaterial(self, fullpathName):
        self._dagpathObj = self.RAW_DAGPATH_CLS(fullpathName)

        self._shaderSetObj = self.SET_SHADER_CLS()

    def __shaderSetObject(self):
        return self._shaderSetObj

    def __dagpathObject(self):
        return self._dagpathObj

    def dagpath(self):
        """
        :return: object of Raw_Dagpath
        """
        return self.__dagpathObject()

    def setFullpathName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__dagpathObject().setRaw(nameString)

    def fullpathName(self):
        """
        :return: str
        """
        return self.__dagpathObject().fullpathName()

    def setNodeName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__dagpathObject().setNodeName(nameString)

    def nodeName(self):
        """
        :return: str
        """
        return self.__dagpathObject().nodeName()

    def nodeFullpathName(self):
        """
        :return: str
        """
        return self.__dagpathObject().nodeFullpathName()

    def addShader(self, shaderObject):
        self.__shaderSetObject().addObject(
            shaderObject.fullpathName(),
            shaderObject
        )

    def shaders(self):
        return self.__shaderSetObject().objects()


class Abc_Graph(mtlConfigure.Basic):
    RAW_NAME_CLS = None
    SET_NODE_CLS = None
    SET_OUTPUT_CLS = None

    def _initAbcGraph(self):
        self._name = self.RAW_NAME_CLS()

        self._nodeSet = self.SET_NODE_CLS()
        self._outputSet = self.SET_OUTPUT_CLS()

    def __nameObject(self):
        return self._name

    def name(self):
        """
        :return: str
        """
        return self.__nameObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__nameObject().setRaw(nameString)

    def __nodeSetObject(self):
        return self._nodeSet

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

    def __outputSetObject(self):
        return self._outputSet

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


class Abc_Portset(mtlConfigure.Basic):
    RAW_NAME_CLS = None
    SET_PORT_CLS = None

    def _initAbcAttributeSet(self):
        self._name = self.RAW_NAME_CLS()
        self._portSetObj = self.SET_PORT_CLS()

    def __nameObject(self):
        return self._name

    def name(self):
        """
        :return: str
        """
        return self.__nameObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__nameObject().setRaw(nameString)

    def __portSetObject(self):
        return self._portSetObj

    def addAttribute(self, attributeObject):
        """
        :param attributeObject: object of Attribute
        :return: None
        """
        self.__portSetObject().addObject(attributeObject.fullpathName(), attributeObject)

    def attributes(self):
        """
        :return: list(object or attribute, ...)
        """
        return self.__portSetObject().objects()

    def hasAttributes(self):
        """
        :return: bool
        """
        return self.__portSetObject().hasObjects()


class Abc_Collection(mtlConfigure.Basic):
    RAW_NAME_CLS = None
    SET_GEOMETRY_CLS = None
    COLLECTION_SET_CLS = None

    def _initAbcCollection(self):
        self._name = self.RAW_NAME_CLS()
        self._geometrySet = self.SET_GEOMETRY_CLS()
        self._collectionSet = self.COLLECTION_SET_CLS()

    def __nameObject(self):
        return self._name

    def name(self):
        """
        :return: str
        """
        return self.__nameObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__nameObject().setRaw(nameString)

    def __geometrySetObject(self):
        return self._geometrySet

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Dag_Geometry
        :return:
        """
        self.__geometrySetObject().addObject(geometryObject.fullpathName(), geometryObject)

    def geometries(self):
        """
        :return: list(object or geometry, ...)
        """
        return self.__geometrySetObject().objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self.__geometrySetObject().hasObjects()

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


# Assign
class Abc_Assign(mtlConfigure.Basic):
    RAW_NAME_CLS = None
    SET_GEOMETRY_CLS = None

    separator_geometry = None

    xml_prefix_label = None

    def _initAbcAssign(self, *args):
        self._name = self.RAW_NAME_CLS(*args)

        self._geometrySet = self.SET_GEOMETRY_CLS()
        self._collectionObj = None

    def __nameObject(self):
        return self._name

    def name(self):
        """
        :return: str
        """
        return self.__nameObject().raw()

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__nameObject().setRaw(nameString)

    def __geometrySetObject(self):
        return self._geometrySet

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Dag_Geometry
        :return: None
        """
        self.__geometrySetObject().addObject(geometryObject.fullpathName(), geometryObject)

    def geometries(self):
        """
        :return: list(object or geometry, ...)
        """
        return self.__geometrySetObject().objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self.__geometrySetObject().hasObjects()

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


class Abc_MaterialAssign(Abc_Assign):
    MATERIAL_CLS = None

    def _initAbcMaterialAssign(self, *args):
        self._initAbcAssign(*args)

        self._shadersetObj = None

    def __shaderSetObject(self):
        return self._shadersetObj

    def addMaterial(self, shadersetObject):
        self._shadersetObj = shadersetObject

    def material(self):
        """
        :return: object of ShaderSet
        """
        return self.__shaderSetObject()

    def materialName(self):
        """
        :return: str
        """
        return self.material().fullpathName()

    def _xmlStrRaw(self):
        return self.cls_order_dic(
            [
                # Label
                (self.Key_Label, self.xml_prefix_label),
                # Attribute
                (
                    self.Key_Attribute, self.cls_order_dic(
                        [
                            (self.Atr_Xml_Name, self.name()),
                            (self.Atr_Xml_Material, self.materialName()),
                            (self.Atr_Xml_Geom, self.geometryString()),
                        ]
                    )
                )
            ]
        )


class Abc_PortsetAssign(Abc_Assign):
    PORTSET_CLS = None

    def _initAbcPortsetAssign(self, *args):
        self._initAbcAssign(*args)

        self._portsetObj = None

    def __portsetObject(self):
        return self._portsetObj

    def attributeSet(self):
        """
        :return: object of Set_Attribute
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


# Look
class Abc_Look(mtlConfigure.Basic):
    RAW_NAME_CLS = None
    SET_ASSIGN_CLS = None

    xml_prefix_label = None

    def _initAbcLook(self, *args):
        self._nameObj = self.RAW_NAME_CLS(*args)

        self._assignSetObj = self.SET_ASSIGN_CLS()

    def name(self):
        return self._nameObj.raw()

    def __assignSetObject(self):
        return self._assignSetObj

    def addAssign(self, assignObject):
        self.__assignSetObject().addObject(
            assignObject.name(),
            assignObject
        )

    def assigns(self):
        return self.__assignSetObject().objects()

    def _xmlStrRaw(self):
        return self.cls_order_dic(
            [
                (self.Key_Label, self.xml_prefix_label),
                (
                    self.Key_Attribute, self.cls_order_dic(
                        [
                            (self.Atr_Xml_Name, self.name())
                        ],
                    )
                ),
                (self.Key_Children, self.assigns()),

                (self.Key_Element, [i.material() for i in self.assigns()])
            ]
        )


class Abc_Asset(mtlConfigure.Basic):
    pass


class Abc_Def(mtlConfigure.Basic):
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

    def attribute(self):
        return self._nodeDefDic.get(self.Key_Attribute, {})
