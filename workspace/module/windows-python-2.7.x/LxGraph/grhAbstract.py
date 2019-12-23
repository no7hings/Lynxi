# coding:utf-8


class AbcRaw(object):
    def _initAbcRaw(self):
        self._rawType = None

        self._raw = None
        self._rawString = None

    def create(self, *args):
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
    def _toStringMethod(*args):
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


class AbcPath(AbcRaw):
    PathSeparator = None
    def _initAbcPath(self):
        self._initAbcRaw()

        self._rawLis = []

    @staticmethod
    def _toStringsMethod(pathString, pathsep):
        if pathString.startswith(pathsep):
            return pathString.split(pathsep)[1:]
        else:
            return pathString.split(pathsep)

    @staticmethod
    def _toStringMethod(rawObjects, pathsep):
        return pathsep + pathsep.join([i.raw() for i in rawObjects])

    def create(self, *args):
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
        return self._rawLis[-1].raw()

    def fullPathName(self):
        """
        :return: str
        """
        return self.raw()


class AbcDagPath(AbcRaw):
    NODE_PATH_CLS = None
    ATTRIBUTE_PATH_CLS = None
    def _initAbcDagPath(self):
        self._initAbcRaw()

        self._nodePathsep = None
        self._attributePathsep = None

        self._nodePath = self.NODE_PATH_CLS()
        self._attributePath = self.ATTRIBUTE_PATH_CLS()

    def create(self, *args):
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

    def fullNodeName(self):
        """
        :return: str
        """
        return self.__nodePathObject().raw()

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

    def fullAttributeName(self):
        """
        :return: str
        """
        return self.__attributePathObject().raw()

    def name(self):
        """
        :return: str
        """
        if self.__attributePathObject().hasRaw():
            return self.attributeName()
        else:
            return self.nodeName()

    def fullPathName(self):
        """
        :return: str
        """
        return self.raw()


class AbcObjectSet(object):
    def _initAbcObjectSet(self):
        self._objectLis = []
        self._objectDic = {}
        self._objectCount = 0

        self._objectFilterStr = None

    def create(self, *args):
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
        assert key in self._objectDic, '''Key is Exist.'''
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

    def objectWithKey(self, raw):
        """
        :param raw: raw
        :return: bool
        """
        assert raw in self._objectDic, '''Key is Non - Exist.'''
        return self._objectDic[raw]

    def hasObjectWithKey(self, raw):
        """
        :param raw: raw
        :return: bool
        """
        return raw in self._objectDic

    def __len__(self):
        """
        :return: int
        """
        return self.objectsCount()


class AbcType(AbcRaw):
    def _initAbcType(self):
        self._initAbcRaw()


class AbcName(AbcRaw):
    def _initAbcName(self):
        self._initAbcRaw()

    def setRaw(self, string):
        self._raw = string


class AbcData(AbcRaw):
    def _initAbcData(self):
        self._initAbcRaw()

    def createByString(self, *args):
        pass

    def str(self):
        return '{}({})'.format(self.rawType(), self.toString())

    def __str__(self):
        """
        :return: str
        """
        return self.str()


class AbcDataN(AbcRaw):
    RawSeparatorString = None

    CHILD_CLS = None

    def _initAbcDataN(self):
        self._initAbcRaw()

        self._pattern = float('inf')

        self._childLis = []

    def create(self, *args):
        """
        :param args: list(raw of typed, ...) / raw of typed, ...
        :return: None
        """
        assert args is not (), 'Argument Not be Empty.'
        if isinstance(args[0], list) or isinstance(args[0], tuple):
            raw = list(args[0])
        else:
            raw = args

        for i in raw:
            dataObject = self.CHILD_CLS()
            dataObject.create(i)
            self.addChild(dataObject)

        self.setRaw(raw)

    def createByString(self, *args):
        pass

    def toString(self):  # to override
        """
        :return: str
        """
        return self.RawSeparatorString.join([i.toString() for i in self.children()])

    def _setPattern(self, *args):
        if len(args) == 1:
            self._pattern = args[0]
        else:
            self._pattern = args

    def _pattern(self):
        return self._pattern

    def addChild(self, dataObject):
        self._childLis.append(dataObject)

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

    def str(self):
        return '{}({})'.format(self.rawType(), self.toString())

    def __str__(self):
        """
        :return: str
        """
        return self.str

    def __len__(self):
        """
        :return: int
        """
        return self.childrenCount()


class AbcDataNN(AbcRaw):
    RawSeparatorString = None

    CHILD_CLS = None

    def _initAbcDataNN(self):
        self._initAbcRaw()

        self._pattern = float('inf'), float('inf')

        self._subRawType = None
        self._childLis = []

    def create(self, *args):
        """
        :param args: list(list(raw of typed, ...), ...) / list(raw of typed, ...), ...
        :return: self
        """
        assert args is not (), 'Argument Not be Empty.'
        if isinstance(args[0], list) or isinstance(args[0], tuple):
            raw = list(args[0])
        else:
            raw = args

        for i in raw:
            dataObject = self.CHILD_CLS()
            if self.subRawType() is not None:
                dataObject.setRawType(self.subRawType())

            dataObject.create(*i)
            self.addChild(dataObject)

        self.setRaw(raw)

    def createByString(self, *args):
        pass

    def toString(self):
        """
        :return: str
        """
        return self.RawSeparatorString.join([i.toString() for i in self.children()])

    def _setPattern(self, *args):
        self._pattern = args

    def _pattern(self):
        return self._pattern

    def setSubRawType(self, typeString):
        """
        :param typeString: str
        :return: None
        """
        self._subRawType = typeString

    def subRawType(self):
        """
        :return: str
        """
        return self._subRawType

    def addChild(self, dataObject):
        """
        :param dataObject: object of Data
        :return: None
        """
        self._childLis.append(dataObject)

    def children(self):
        """
        :return: list(object of Data, ...)
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

    def raw(self):
        """
        :return: list(list(raw of typed, ...), ...)
        """
        return [i.raw() for i in self.children()]

    def str(self):
        if self.subRawType() is not None:
            return '{}({})'.format(self.rawType(), ', '.join([i.str() for i in self.children()]))
        else:
            return '{}({})'.format(self.rawType(), self.toString())

    def __str__(self):
        """
        :return: str
        """
        return self.str()

    def __len__(self):
        """
        :return: int
        """
        return self.childrenCount()


class AbcValue(object):
    RawTypeString = None
    SubRawTypeString = None

    TYPE_CLS = None
    DATA_CLS = None

    def _initAbcValue(self):
        self._type = self.TYPE_CLS(self.RawTypeString)

        self._data = self.DATA_CLS()

    def create(self, *args):
        """
        :param args: typed of raw
        :return: None
        """
        if self.RawTypeString is not None:
            self.__dataObject().setRawType(self.RawTypeString)
        if self.SubRawTypeString is not None:
            self.__dataObject().setSubRawType(self.SubRawTypeString)

        self.__dataObject().create(*args)

    def createByString(self, *args):
        """
        :param args: raw string
        :return: None
        """
        pass

    def __typeObject(self):
        return self._type

    def type(self):
        """
        :return: str
        """
        return self.__typeObject().raw()

    def __dataObject(self):
        return self._data

    def data(self):
        """
        :return: object of Data
        """
        return self.__dataObject()

    def raw(self):
        """
        :return: raw of typed
        """
        return self.__dataObject().raw()

    def hasRaw(self):
        """
        :return: bool
        """
        return self.__dataObject().hasRaw()

    def _setDataNSize(self, *args):
        assert hasattr(self.__dataObject(), '_setPattern')
        self.__dataObject()._setPattern(*args)

    def _dataNSize(self):
        assert hasattr(self.__dataObject(), '_pattern')
        return self.__dataObject()._pattern()

    def toString(self):
        """
        :return: str
        """
        return self.__dataObject().toString()

    def __eq__(self, other):
        """
        :param other: object of Value
        :return: bool
        """
        return self.data() == other.data()

    def __str__(self):
        """
        :return: str
        """
        return self.__dataObject().str()


class AbcAttribute(object):
    DAG_PATH_CLS = None
    CHILD_SET_CLS = None

    def _initAbcAttribute(self):
        self._dagPath = self.DAG_PATH_CLS()
        self._childSet = self.CHILD_SET_CLS()

        self._value = None
        self._defValue = None

        self._input = None
        self._parent = None

    def create(self, *args):
        pass

    def __dagPathObject(self):
        return self._dagPath

    def dagPath(self):
        return self.__dagPathObject()

    def fullPathName(self):
        """
        :return: str
        """
        return self.__dagPathObject().fullPathName()

    def nodeName(self):
        """
        :return: str
        """
        return self.__dagPathObject().nodeName()

    def fullNodeName(self):
        """
        :return: str
        """
        return self.__dagPathObject().fullNodeName()

    def setAttributeName(self, nameString):
        self.__dagPathObject().setAttributeName(nameString)

    def attributeName(self):
        """
        :return: str
        """
        return self.__dagPathObject().attributeName()

    def fullAttributeName(self):
        """
        :return: str
        """
        return self.__dagPathObject().fullAttributeName()

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
        return self.__valueObject().type()

    def valueString(self):
        self.__valueObject().toString()

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
        return self._childSet

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
        self.__childSetObject().addObject(attributeObject.fullPathName(), attributeObject)

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

    def inputFullPathName(self):
        """
        :return: str
        """
        return self.input().fullPathName()

    def inputNodeName(self):
        """
        :return: str
        """
        return self.input().nodeName()

    def inputFullNodeName(self):
        """
        :return: str
        """
        return self.input().fullNodeName()

    def inputAttributeName(self):
        """
        :return: str
        """
        return self.input().attributeName()

    def inputFullAttributeName(self):
        """
        :return: str
        """
        return self.input().fullAttributeName()

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

    def parentFullPathName(self):
        """
        :return: str
        """
        return self.__parentObject().fullPathName()

    def parentAttributeName(self):
        """
        :return: str
        """
        return self.__parentObject().attributeName()

    def parentFullAttributeName(self):
        """
        :return: str
        """
        return self.__parentObject().fullAttributeName()


class AbcOutput(object):
    NAME_CLS = None

    def _initAbcOutput(self):
        self._name = self.NAME_CLS()
        self._input = None

    def __nameObject(self):
        return self._name

    def setName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__nameObject().setRaw(nameString)

    def name(self):
        """
        :return: str
        """
        return self.__nameObject().raw()

    def _inputObject(self):
        return self._input

    def input(self):
        """
        :return: object of Attribute
        """
        return self._input

    def inputFullPathName(self):
        """
        :return: str
        """
        return self._inputObject().fullPathName()

    def inputNodeName(self):
        """
        :return: str
        """
        return self.input().nodeName()

    def inputFullNodeName(self):
        """
        :return: str
        """
        return self.input().fullNodeName()

    def inputAttributeName(self):
        """
        :return: str
        """
        return self._inputObject().attributeName()

    def inputFullAttributeName(self):
        """
        :return: str
        """
        return self._inputObject().fullAttributeName()


class AbcNode(object):
    TYPE_CLS = None
    CATEGORY_CLS = None
    DAG_PATH_CLS = None
    CHILD_SET_CLS = None
    ATTRIBUTE_SET_CLS = None

    def _initAbcNode(self):
        self._type = self.TYPE_CLS()
        self._category = self.CATEGORY_CLS()
        self._dagPath = self.DAG_PATH_CLS()
        self._childSet = self.CHILD_SET_CLS()
        self._attributeSet = self.ATTRIBUTE_SET_CLS()

        self._defRaw = None

    def loadDef(self, *args):
        pass

    def defRaw(self):
        return self._defRaw

    def create(self, *args):
        pass

    def __typeObject(self):
        return self._type

    def type(self):
        """
        :return: str
        """
        return self.__typeObject().raw()

    def __categoryObject(self):
        return self._category
    
    def setCategory(self, categoryString):
        """
        :param categoryString: str
        :return: None
        """
        self.__categoryObject().setRaw(categoryString)

    def category(self):
        """
        :return: str
        """
        return self.__categoryObject().raw()

    def __dagPathObject(self):
        return self._dagPath

    def dagPath(self):
        """
        :return: object of DagNodePath
        """
        return self.__dagPathObject()
    
    def setFullPathName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__dagPathObject().setRaw(nameString)

    def fullPathName(self):
        """
        :return: str
        """
        return self.__dagPathObject().fullPathName()

    def setNodeName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__dagPathObject().setNodeName(nameString)

    def nodeName(self):
        """
        :return: str
        """
        return self.__dagPathObject().nodeName()

    def fullNodeName(self):
        """
        :return: str
        """
        return self.__dagPathObject().fullNodeName()

    def __childSetObject(self):
        return self._childSet

    def children(self):
        """
        :return: list(object of Node, ...)
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
        :return: object of Node
        """
        return self.__childSetObject().objectAt(index)

    def addChild(self, nodeObject):
        """
        :param nodeObject: object of Node
        :return: None
        """
        self.__childSetObject().addObject(nodeObject.fullPathName(), nodeObject)

    def __attributeSetObject(self):
        return self._attributeSet

    def attributes(self):
        """
        :return: list(object or attribute, ...)
        """
        return self.__attributeSetObject().objects()

    def hasAttributes(self):
        """
        :return: bool
        """
        return self.__attributeSetObject().hasObjects()

    def attributesCount(self):
        """
        :return: int
        """
        return self.__attributeSetObject().objectsCount()

    def attributeAt(self, index):
        """
        :param index: int
        :return: object of Attribute
        """
        return self.__attributeSetObject().objectAt(index)

    def addAttribute(self, attributeObject):
        """
        :param attributeObject: object of Attribute
        :return: None
        """
        self.__attributeSetObject().addObject(attributeObject.fullPathName(), attributeObject)

    def __str__(self):
        return self.fullPathName()


class AbcShader(AbcNode):
    OUTPUT_CLS = None

    def _initAbcShader(self):
        self._initAbcNode()

        self._output = self.OUTPUT_CLS()

    def __outputObject(self):
        return self._output

    def output(self):
        """
        :return: object of Output
        """
        return self.__outputObject()

    def outputFullPathName(self):
        """
        :return: str
        """
        return self.__outputObject().fullPathName()

    def outputNodeName(self):
        """
        :return: str
        """
        return self.__outputObject().nodeName()

    def outputFullNodeName(self):
        """
        :return: str
        """
        return self.__outputObject().fullNodeName()

    def outputAttributeName(self):
        """
        :return: str
        """
        return self.__outputObject().attributeName()

    def outputFullAttributeName(self):
        """
        :return: str
        """
        return self.__outputObject().fullAttributeName()


class AbcGeometry(AbcNode):
    def _initAbcGeometry(self):
        self._initAbcNode()


class AbcGraph(object):
    NAME_CLS = None
    NODE_SET_CLS = None
    OUTPUT_SET_CLS = None

    def _initGraph(self):
        self._name = self.NAME_CLS()
        self._nodeSet = self.NODE_SET_CLS()
        self._outputSet = self.OUTPUT_SET_CLS()

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
        :param nodeObject: object of Node
        :return: None
        """
        self.__nodeSetObject().addObject(nodeObject.fullPathName(), nodeObject)

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
        self.__outputSetObject().addObject(outputObject.fullPathName(), outputObject)

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


class AbcAssign(object):
    NAME_CLS = None
    GEOMETRY_SET_CLS = None

    def _initAbcAssign(self):
        self._name = self.NAME_CLS()
        self._geometrySet = self.GEOMETRY_SET_CLS()
        self._collection = None

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
        :param geometryObject: object of Geometry
        :return: None
        """
        self.__geometrySetObject().addObject(geometryObject.fullPathName(), geometryObject)

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

    def geometryFullPathNames(self):
        """
        :return: list(str, ...)
        """
        return [i.fullPathName() for i in self.geometries()]

    def geometryNodeNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nodeName() for i in self.geometries()]

    def geometryFullNodeNames(self):
        """
        :return: list(str, ...)
        """
        return [i.fullNodeName() for i in self.geometries()]

    def __collectionObject(self):
        return self._collection

    def setCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self._collection = collectionObject

    def collection(self):
        """
        :return: object of Collection
        """
        return self.__collectionObject()

    def collectionName(self):
        """
        :return: str
        """
        return self._collection.name()


class AbcShaderSetAssign(AbcAssign):
    def _initAbcShaderSetAssign(self):
        self._initAbcAssign()
        self._shaderSet = None

    def __shaderSetObject(self):
        return self._shaderSet

    def shaderSet(self):
        """
        :return: object of ShaderSet
        """
        return self.__shaderSetObject()

    def setShaderSetName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__shaderSetObject().setName(nameString)

    def shaderSetName(self):
        """
        :return: str
        """
        return self.shaderSet().name()


class AbcAttributeSetAssign(AbcAssign):
    def _initAbcAttributeSetAssign(self):
        self._initAbcAssign()
        self._attributeSet = None

    def __attributeSetObject(self):
        return self._attributeSet

    def attributeSet(self):
        """
        :return: object of AttributeSet
        """
        return self.__attributeSetObject()

    def setAttributeSetName(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self.__attributeSetObject().setName(nameString)

    def attributeSetName(self):
        """
        :return: str
        """
        return self.__attributeSetObject().name()


class AbcShaderSet(object):
    NAME_CLS = None
    SHADER_SET_CLS = None

    def _initAbcShaderSet(self):
        self._name = self.NAME_CLS()
        self._shaderSet = self.SHADER_SET_CLS()

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

    def __shaderSetObject(self):
        return self._shaderSet

    def addShader(self, shaderObject):
        """
        :param shaderObject: object of Shader
        :return: None
        """
        self.__shaderSetObject().addObject(shaderObject.fullPathName(), shaderObject)

    def shaders(self):
        """
        :return: list(object or shader, ...)
        """
        return self.__shaderSetObject().objects()

    def hasShaders(self):
        """
        :return: bool
        """
        return self.__shaderSetObject().hasObjects()


class AbcAttributeSet(object):
    NAME_CLS = None
    ATTRIBUTE_SET_CLS = None

    def _initAbcAttributeSet(self):
        self._name = self.NAME_CLS()
        self._attributeSet = self.ATTRIBUTE_SET_CLS()

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

    def __attributeSetObject(self):
        return self._attributeSet

    def addAttribute(self, attributeObject):
        """
        :param attributeObject: object of Attribute
        :return: None
        """
        self.__attributeSetObject().addObject(attributeObject.fullPathName(), attributeObject)

    def attributes(self):
        """
        :return: list(object or attribute, ...)
        """
        return self.__attributeSetObject().objects()

    def hasAttributes(self):
        """
        :return: bool
        """
        return self.__attributeSetObject().hasObjects()


class AbcCollection(object):
    NAME_CLS = None
    GEOMETRY_SET_CLS = None
    COLLECTION_SET_CLS = None

    def _initAbcCollection(self):
        self._name = self.NAME_CLS()
        self._geometrySet = self.GEOMETRY_SET_CLS()
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
        :param geometryObject: object of Geometry
        :return:
        """
        self.__geometrySetObject().addObject(geometryObject.fullPathName(), geometryObject)

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

    def geometryFullPathNames(self):
        """
        :return: list(str, ...)
        """
        return [i.fullPathName() for i in self.geometries()]

    def geometryNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nodeName() for i in self.geometries()]

    def geometryFullNodeNames(self):
        """
        :return: list(str, ...)
        """
        return [i.fullNodeName() for i in self.geometries()]

    def __collectionSetObject(self):
        return self._collectionSet

    def addCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self.__collectionSetObject().addObject(collectionObject.fullPathName(), collectionObject)

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


class AbcAsset(object):
    pass


class AbcLook(object):
    pass


class AbcDef(object):
    def _initAbcDef(self):
        self._nodeClassDic = {}

    def load(self, *args):
        pass

    def getDefNode(self, categoryString):
        pass

    def get(self, key):
        pass


class AbcTypeDef(AbcDef):
    pass


class AbcNodeDef(AbcDef):
    def _initAbcNodeDef(self):
        self._initAbcDef()
