# coding:utf-8
from LxBasic import bscMethods

from LxMaterial import mtlConfigure, mtlMethods


class Abc_MtlBasic(mtlConfigure.Utility):
    DEF_mtl_file_attribute_separator = u' '

    VAR_mtl_file_element_key = u''
    VAR_mtl_file_attribute_key = u''

    def _initAbcMtlXml(self):
        self._xmlIndentStr = ''

    def _xmlElementKeyString(self):
        return self.VAR_mtl_file_element_key

    def _xmlAttributeKeyString(self):
        return self.VAR_mtl_file_attribute_key

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
        :return: list(tuple(key, value)/object instance of Abc_MtlBasic, ...)
        """
        pass

    @classmethod
    def _toXmlString(cls, elementObject, indent=4):
        def addPrefixFnc_(prefix_, lString, rString):
            lis.append(u'{}<{}{}'.format(lString, prefix_, rString))

        def addAttributeFnc_(attributeObject_, lString, rString):
            if attributeObject_ is not None:
                if isinstance(attributeObject_, Abc_MtlBasic):
                    attributeRaw = attributeObject_._xmlAttributeRaw()
                else:
                    attributeRaw = attributeObject_

                if attributeRaw:
                    for i in attributeRaw:
                        if isinstance(i, Abc_MtlBasic):
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
                [addAttributeFnc_(i, lString=cls.DEF_mtl_file_attribute_separator, rString=u'') for i in attributes]
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
                lis.append(u'{}/>\r\n'.format(cls.DEF_mtl_file_attribute_separator))

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


class Abc_MtlTypeDef(mtlConfigure.Utility):
    def _initAbcMtlTypeDef(self):
        pass


class Abc_MtlBasicDef(mtlConfigure.Utility):
    VAR_geometry_category_string = None
    VAR_material_category_string = None
    # noinspection PyUnusedLocal
    def _initAbcMtlBasicDef(self, *args):
        self._nodeRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_node_defs_file
        ) or {}
        self._geometryRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_geometry_def_file
        ) or {}
        self._materialRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_material_def_file
        ) or {}
        self._outputRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_output_defs_file
        ) or {}
        self._portChildRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_port_child_defs_file
        ) or {}

        self._typeStringDict = self.CLS_ordered_dict()
        self._portDefsDict = self.CLS_ordered_dict()

        self._getData_()

    def getObjectDef(self, categoryString):
        if categoryString in self._nodeRaw:
            return self._nodeRaw.get(
                categoryString, {}
            )
        elif categoryString == self.VAR_geometry_category_string:
            return self._geometryRaw
        elif categoryString == self.VAR_material_category_string:
            return self._materialRaw
        return {}

    def getObjectTypeString(self, categoryString):
        return self._typeStringDict.get(categoryString)

    def getObjectPortDefs(self, categoryString):
        return self._portDefsDict.get(categoryString, {})

    def portChildDefs(self):
        return self._portChildRaw

    def _getData_(self):
        def getTypeFnc_(categoryString_, typeString_):
            self._typeStringDict[categoryString_] = typeString_

        def getNodeFnc_():
            for categoryString, dccNodeDef in self._nodeRaw.items():
                getNodeSubFnc_(categoryString, dccNodeDef)

        def getNodeSubFnc_(categoryString_, nodeRaw_):
            typeString = nodeRaw_[self.DEF_mtl_key_type]
            getTypeFnc_(categoryString_, typeString)
            self._portDefsDict[categoryString_] = self.CLS_ordered_dict()

            portDefs = nodeRaw_[self.DEF_mtl_key_port]
            for portDef in portDefs:
                getPortFnc_(categoryString_, portDef)

            portDefs = self._outputRaw.get(typeString, [])
            for i in portDefs:
                getPortFnc_(categoryString_, i)

        def getPortFnc_(categoryString_, portDef_):
            portnameString = portDef_[self.DEF_mtl_key_portname]
            porttypeString = portDef_[self.DEF_mtl_key_porttype]
            portdataString = portDef_[self.DEF_mtl_key_portdata]
            assignString = portDef_[self.DEF_mtl_key_assign]

            addPortFnc_(categoryString_, portnameString, porttypeString, portdataString, assignString, None)
            for seq, i in enumerate(self._portChildRaw.get(porttypeString, [])):
                getChildFnc_(seq, categoryString_, portnameString, portdataString, assignString, i)

        def getChildFnc_(index, categoryString_, parentPortnameString_, parentPortdataString_, parentAssignString_, portDef_):
            formatString = portDef_[self.DEF_mtl_key_format]
            portnameString = formatString.format(*[parentPortnameString_])
            porttypeString = portDef_[self.DEF_mtl_key_porttype]

            if parentPortdataString_:
                portdataString = parentPortdataString_.split(u',')[index].rstrip().lstrip()
            else:
                portdataString = portDef_[self.DEF_mtl_key_portdata]

            assignString = portDef_[self.DEF_mtl_key_assign]
            addPortFnc_(categoryString_, portnameString, porttypeString, portdataString, (parentAssignString_, assignString), parentPortnameString_)

        def addPortFnc_(categoryString_, portnameString_, porttypeString_, valueString_, assignString_, parentPortnameString_):
            _dic = self.CLS_ordered_dict()
            _dic[self.DEF_mtl_key_porttype] = porttypeString_
            _dic[self.DEF_mtl_key_portdata] = valueString_
            _dic[self.DEF_mtl_key_assign] = assignString_
            _dic[self.DEF_mtl_key_parent] = parentPortnameString_
            self._portDefsDict[categoryString_][portnameString_] = _dic

        getNodeFnc_()
        getNodeSubFnc_(self.DEF_mtl_category_material, self._materialRaw)
        getNodeSubFnc_(self.DEF_mtl_category_geometry, self._geometryRaw)


class Abc_MtlObjectDef(mtlConfigure.Utility):
    CLS_mtl_basic_def = None

    # noinspection PyUnusedLocal
    def _initAbcMtlObjectDef(self, *args):
        categoryString = args[0]

        self._basicDefObject = self.CLS_mtl_basic_def()

        self._categoryString = categoryString
        self._typeString = self._basicDefObject.getObjectTypeString(categoryString)

        self._portDefsDict = self._basicDefObject.getObjectPortDefs(self._categoryString)

    def categoryString(self):
        return self._categoryString

    def typeString(self):
        return self._typeString

    def portDefs(self):
        return self._portDefsDict

    def getPortDef(self, portnameString):
        return self._portDefsDict.get(portnameString)

    def getPorttypeString(self, portnameString):
        return self._portDefsDict[portnameString][self.DEF_mtl_key_porttype]


class Abc_MtlNodeDef(Abc_MtlObjectDef):
    def _initAbcMtlNodeDef(self, *args):
        self._initAbcMtlObjectDef(*args)


class Abc_MtlMaterialDef(Abc_MtlObjectDef):
    # noinspection PyUnusedLocal
    def _initAbcMtlMaterialDef(self, *args):
        self._initAbcMtlObjectDef(*args)


class Abc_MtlGeometryDef(Abc_MtlObjectDef):
    def _initAbcMtlGeometryDef(self, *args):
        self._initAbcMtlObjectDef(*args)


class Abc_MtlRaw(Abc_MtlBasic):
    def _initAbcMtlRaw(self, *args):
        if args:
            self._raw = args[0]
            self._rawType = type(self._raw)
        else:
            self._raw = None
            self._rawType = None

        self._initAbcMtlXml()

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

    def _xmlAttributeObjectLis(self):
        return [
            [('raw', self.raw())]
        ]

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

    def __ne__(self, other):
        """
        :param other: typed raw
        :return: bool
        """
        return self.toString() != other.toString()


class Abc_MtlDagpath(Abc_MtlRaw):
    CLS_mtl_raw = None

    VAR_mtl_raw_separator = None

    def _initAbcMtlDagpath(self, *args):
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


class Abc_MtlMaterialDagpath(Abc_MtlDagpath):
    def _initAbcMtlMaterialDagpath(self, *args):
        self._initAbcMtlDagpath(*args)

    def _xmlAttributeValueString(self):
        return self.fullpathName()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString()),
        ]


class Abc_MtlObjectSet(Abc_MtlBasic):
    VAR_mtl_object_separator = ','
    # noinspection PyUnusedLocal
    def _initAbcMtlObjectSet(self, *args):
        self._objectLis = []
        self._objectDic = {}

        self._objectCount = 0

        self._objectFilterStr = None

        self._initAbcMtlXml()

    def createByRaw(self, *args):
        pass

    def addObject(self, obj):
        """
        :param obj: object of typed
        :return:
        """
        queryString = obj._queryString()
        assert queryString not in self._objectDic, u'''Key {} is Exist.'''.format(queryString)
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
        assert keyString in self._objectDic, u'''Key: "{}" is Non - Exist.'''.format(keyString)
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
        return self.VAR_mtl_object_separator.join([i.toString() for i in self.objects()])

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


class Abc_MtlRawString(Abc_MtlRaw):
    def _initAbcMtlRawString(self, *args):
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

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# data
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

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
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


# value
class Abc_MtlValue(Abc_MtlBasic):
    CLS_mtl_datatype = None
    CLS_mtl_raw_data = None

    VAR_mtl_value_type_pattern = None
    VAR_mtl_value_size_pattern = None

    def _initAbcMtlValue(self, *args):
        self._datatypeObj = self.CLS_mtl_datatype(self.VAR_mtl_value_type_pattern[0])
        self._dataObj = self.CLS_mtl_raw_data(self, *args)

        self._initAbcMtlXml()

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

    def _xmlAttributeObjectLis(self):
        return [
            self.datatype(), self.data()
        ]

    def _xmlAttributeValueString(self):
        return self.toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
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


# port
class Abc_MtlPort(Abc_MtlBasic):
    CLS_mtl_port_dagpath = None
    CLS_mtl_port_set = None

    def _initAbcMtlPort(self, *args):
        nodeObject, fullpathPortname = args

        self._objectObj = nodeObject
        self._dagpathObj = nodeObject.dagpath()

        self._portDagpathObj = self.CLS_mtl_port_dagpath(fullpathPortname)

        # value
        self._valueObj = None
        self._defValueObj = None

        # connect
        self._sourcePortObj = None
        self._targetPortObj = None

        # children
        self._childSetObj = self.CLS_mtl_port_set()
        self._parentObj = None

        self._initAbcMtlXml()

    def createByRaw(self, *args):
        pass

    def node(self):
        return self._objectObj

    def dagpath(self):
        """
        :return: object of Portpath
        """
        return self._portDagpathObj

    def fullpathName(self):
        """
        :return: str
        """
        return self._portDagpathObj.pathsep().join(
            [self._dagpathObj.fullpathName(), self._portDagpathObj.fullpathName()]
        )

    def portstring(self):
        return self._portDagpathObj

    def fullpathNodename(self):
        """
        :return: str
        """
        return self._dagpathObj.fullpathName()

    def fullpathPortname(self):
        """
        :return: str
        """
        return self._portDagpathObj.fullpathName()

    def portname(self):
        return self._portDagpathObj.name()

    def portnameString(self):
        return self._portDagpathObj.nameString()

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

    # source
    def _setSource_(self, portObject):
        if self.isConnectedFrom(portObject) is False:
            self._sourcePortObj = portObject

            portObject.connectTo(self)

    def connectFrom(self, outputObject):
        assert isinstance(outputObject, Abc_MtlOutput), u'''[ Argument Error ] "outputObject" must object of Output'''
        self._setSource_(outputObject)

    def hasSource(self):
        return self._sourcePortObj is not None

    def source(self):
        """
        :return: object of Output
        """
        return self._sourcePortObj

    def isConnectedFrom(self, outputObject):
        return outputObject is self._sourcePortObj

    # target
    def _setTarget_(self, portObject):
        if self.isConnectedTo(portObject) is False:
            self._targetPortObj = portObject

            portObject.connectFrom(self)

    def connectTo(self, inputObject):
        assert isinstance(inputObject, Abc_MtlInput), u'''[ Argument Error ] "outputObject" must object of Input'''
        self._setTarget_(inputObject)

    def hasTarget(self):
        return self._targetPortObj is not None

    def isConnectedTo(self, inputObject):
        return self._targetPortObj is inputObject

    def target(self):
        return self._targetPortObj

    # channel
    def _setParent_(self, portObject):
        self._parentObj = portObject

    def parent(self):
        return self._parentObj

    def hasParent(self):
        return self._parentObj is not None

    def _addChild_(self, portObject):
        """
        :param portObject: object of Port
        :return: None
        """
        self._childSetObj.addObject(portObject)
        portObject._setParent_(self)

    def children(self):
        """
        :return: list(object of Port, ...)
        """
        return self._childSetObj.objects()

    def hasChildren(self):
        """
        :return: bool
        """
        return self._childSetObj.hasObjects()

    def child(self, channelString):
        return self._childSetObj.objectWithKey(channelString)

    def hasChild(self, channelString):
        return self._childSetObj.hasObjectWithKey(channelString)

    def _queryString(self):
        return self.fullpathPortname()

    def _xmlAttributeValueString(self):
        return self.portname().toString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# port > input
class Abc_MtlInput(Abc_MtlPort):
    def _initAbcMtlInput(self, *args):
        self._initAbcMtlPort(*args)

    def _given(self):
        """
        :return:
            1.object of Node
            2.object of Value
        """
        if self.hasSource() is True:
            return self.source()
        return self.value()

    def _xmlAttributeObjectLis(self):
        return [
            self.dagpath(),
            self.porttype(),
            self._given()
        ]


# port > input > node input
class Abc_MtlNodeInput(Abc_MtlInput):
    def _initAbcMtlNodeInput(self, *args):
        self._initAbcMtlInput(*args)


# port > input > shader input
class Abc_MtlShaderInput(Abc_MtlInput):
    def _initAbcMtlShaderInput(self, *args):
        self._initAbcMtlInput(*args)

    def sourceNodeGraphOutput(self):
        if self.hasSource() is True:
            nodeGraph = self.source().node().nodeGraph()
            if nodeGraph is not None:
                return nodeGraph.getNodeGraphOutput(self)

    def _given(self):
        """
        :return:
            1.object of Node
            2.object of Value
        """
        if self.hasSource() is True:
            return self.sourceNodeGraphOutput()
        return self.value()


# port > output
class Abc_MtlOutput(Abc_MtlPort):
    def _initAbcMtlOutput(self, *args):
        self._initAbcMtlPort(*args)

        self._nodeGraphOutput = None

    def _setNodeGraphOutput_(self, nodeGraphOutputObject):
        self._nodeGraphOutput = nodeGraphOutputObject

    def _xmlAttributeValueString(self):
        return self.fullpathPortname()

    def _xmlAttributeRaw(self):
        if self.hasParent():
            return [
                self.parent(),
                (self._xmlAttributeKeyString(), self.portnameString())
            ]
        else:
            return [
                self.node(),
                (self._xmlAttributeKeyString(), self.portnameString())
            ]

    def _xmlAttributeObjectLis(self):
        return [
            self.dagpath(),
            self.node(),
            self.porttype(),
            self.value()
        ]


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

    def _xmlAttributeObjectLis(self):
        return [
            self.dagpath(),
            self.porttype(),
            self.value()
        ]


class Abc_MtlGeometryVisibility(Abc_MtlPort):
    def _initAbcMtlVisibility(self, *args):
        self._initAbcMtlPort(*args)

    def _xmlAttributeObjectLis(self):
        return [
            self.dagpath(),
            self.porttype(),
            self.value()
        ]


# object
class Abc_MtlObject(Abc_MtlBasic):
    CLS_mtl_type = None
    CLS_mtl_category = None

    CLS_mtl_node_dagpath = None

    CLS_mtl_object_def = None

    CLS_mtl_port_set = None

    CLS_mtl_input = None
    CLS_mtl_input_channel = None
    CLS_mtl_output = None
    CLS_mtl_output_channel = None

    CLS_mtl_source_object = None

    VAR_mtl_value_class_dict = {}

    def _initAbcMtlObject(self, categoryString, fullpathName):
        self._objectDefObj = self.CLS_mtl_object_def(categoryString)

        self._categoryObj = self.CLS_mtl_category(categoryString)
        self._dagpathObj = self.CLS_mtl_node_dagpath(fullpathName)

        self._typeObj = self.CLS_mtl_type(self._objectDefObj.typeString())

        self._attributeSetObj = self.CLS_mtl_port_set()
        self._inputSetObj = self.CLS_mtl_port_set()
        self._outputSetObj = self.CLS_mtl_port_set()

        self._addPorts_()

        self._initAbcMtlXml()

    def _typeObject(self):
        return self._typeObj

    def _setType(self, typeString):
        self._typeObj = self.CLS_mtl_type(typeString)

    def objectDef(self):
        return self._objectDefObj

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

    def _addPorts_(self):
        def addFnc_(portObject_, assignString_):
            if assignString_ == self.DEF_mtl_keyword_input or assignString_ == (self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_channel):
                self._addInput_(portObject_)
            elif assignString_ == self.DEF_mtl_keyword_output or assignString_ == (self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_channel):
                self._addOutput_(portObject_)

            self._addAttribute_(portObject_)

        def addPortFnc_(portnameString_, portDef_):
            _porttypeString = portDef_[self.DEF_mtl_key_porttype]
            _valueString = portDef_[self.DEF_mtl_key_portdata]
            _assignString = portDef_[self.DEF_mtl_key_assign]

            portObject = None
            if _assignString == self.DEF_mtl_keyword_input:
                portObject = self.CLS_mtl_input(self, portnameString_)
            elif _assignString == self.DEF_mtl_keyword_output:
                portObject = self.CLS_mtl_output(self, portnameString_)
            elif _assignString == (self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_channel):
                portObject = self.CLS_mtl_input_channel(self, portnameString_)
            elif _assignString == (self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_channel):
                portObject = self.CLS_mtl_output_channel(self, portnameString_)

            if portObject is not None:
                valueCls = self.VAR_mtl_value_class_dict[_porttypeString]

                portObject._setValue_(valueCls(_valueString))
                portObject._setDefaultValue_(valueCls(_valueString))

                addFnc_(portObject, _assignString)

        def addChildFnc_(portnameString_, portDef_):
            _parentString = portDef_[self.DEF_mtl_key_parent]
            if _parentString:
                parentPortObject = self.attribute(_parentString)
                portObject = self.attribute(portnameString_)
                parentPortObject._addChild_(portObject)

        for k, v in self._objectDefObj.portDefs().items():
            addPortFnc_(k, v)

        for k, v in self._objectDefObj.portDefs().items():
            addChildFnc_(k, v)

    def _addAttribute_(self, portObject):
        if isinstance(portObject, (tuple, list)):
            [self._attributeSetObj.addObject(i) for i in portObject]
        else:
            self._attributeSetObj.addObject(portObject)

    def hasAttributes(self):
        return self._attributeSetObj.hasObjects()

    def hasAttribute(self, *args):
        return self._attributeSetObj.hasObject(*args)

    def attributes(self):
        return self._attributeSetObj.objects()

    def attribute(self, fullpathPortname):
        return self._attributeSetObj.objectWithKey(fullpathPortname)

    def _addInput_(self, portObject):
        if isinstance(portObject, (tuple, list)):
            [self._inputSetObj.addObject(i) for i in portObject]
        else:
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

    def input(self, fullpathPortname):
        """
        :param fullpathPortname: str
        :return: object of Port
        """
        return self._inputSetObj.objectWithKey(fullpathPortname)

    def valueChangedInputs(self):
        def _addFnc(portObject):
            if not portObject in lis:
                lis.append(portObject)

        lis = []
        for i in self.inputs():
            if i.isValueChanged() or i.hasSource():
                if i.hasParent():
                    _addFnc(i.parent())
                _addFnc(i)
        return lis

    def _addOutput_(self, portObject):
        if isinstance(portObject, (tuple, list)):
            [self._outputSetObj.addObject(i) for i in portObject]
        else:
            self._outputSetObj.addObject(portObject)

    def outputs(self):
        return self._outputSetObj.objects()

    def output(self, fullpathPortname):
        return self._outputSetObj.objectWithKey(fullpathPortname)

    def toString(self):
        return self.fullpathName()

    def sourceDags(self):
        return [i.source().node() for i in self.inputs() if i.hasSource()]

    def targetDags(self):
        return [i.target().node() for i in self.outputs() if i.hasTarget()]

    def targetShaders(self):
        return [i for i in self.targetDags() if isinstance(i, Abc_MtlShader)]

    def _queryString(self):
        return self.fullpathName()

    def connectedOutputs(self, toShader=False):
        lis = []

        for outputObject in self.outputs():
            if outputObject.hasTarget():
                if toShader is True:
                    if isinstance(outputObject.target().node(), Abc_MtlShader):
                        lis.append(outputObject)
                else:
                    lis.append(outputObject)
        return lis


# material
class Abc_MtlMaterial(Abc_MtlObject):
    def _initAbcMtlMaterial(self, *args):
        nodeString = args[0]
        self._initAbcMtlObject(
            self.DEF_mtl_category_material,
            nodeString
        )

        self._surfaceDagObj = None
        self._displacementDagObj = None
        self._sourceVolumeDagObj = None

        self._surfacePortObj = None
        self._displacementPortObj = None
        self._sourceVolumePortObj = None

    def surfaceInput(self):
        return self.input('surface_shader')

    def displacementInput(self):
        return self.input('displacement_shader')

    def volumeInput(self):
        return self.input('volume_shader')

    def connectSurfaceFrom(self, outputObject):
        self._surfacePortObj = outputObject
        self._surfacePortObj.connectTo(self.surfaceInput())
        self._surfaceDagObj = self._surfacePortObj.node()
        self._surfaceDagObj.setTargetMaterialPort(self.surfaceInput())

    def surfaceShader(self):
        return self._surfaceDagObj

    def connectDisplacementFrom(self, outputObject):
        self._displacementPortObj = outputObject
        self._displacementPortObj.connectTo(self.displacementInput())
        self._displacementDagObj = self._displacementPortObj.node()
        self._displacementDagObj.setTargetMaterialPort(self.displacementInput())

    def displacementShader(self):
        return self._displacementDagObj

    def connectVolumeFrom(self, outputObject):
        self._sourceVolumePortObj = outputObject
        self._sourceVolumePortObj.connectTo(self.volumeInput())
        self._sourceVolumeDagObj = self._sourceVolumePortObj.node()
        self._sourceVolumeDagObj.setTargetMaterialPort(self.volumeInput())

    def volumeShader(self):
        return self._sourceVolumeDagObj

    def shaders(self):
        return [self.surfaceShader(), self.displacementShader(), self.volumeShader()]

    def sourcePorts(self):
        pass

    def _xmlAttributeObjectLis(self):
        return [
            self.dagpath()
        ]

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


# object > node
class Abc_MtlNode(Abc_MtlObject):
    def _initAbcMtlNode(self, *args):
        self._initAbcMtlObject(*args)

        self._nodeGraphObj = None

    def _setNodeGraph_(self, nodeGraphObject):
        self._nodeGraphObj = nodeGraphObject

    def nodeGraph(self):
        return self._nodeGraphObj

    def _xmlElementKeyString(self):
        return self.categoryString()

    def _xmlAttributeObjectLis(self):
        return [
            self.dagpath()
        ]

    def _xmlChildList(self):
        return self.valueChangedInputs()

    def _xmlAttributeValueString(self):
        return self.fullpathName()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# object > shader
class Abc_MtlShader(Abc_MtlObject):
    def _initAbcMtlShader(self, *args):
        self._initAbcMtlObject(*args)

        self._targetMaterialPortObj = None

    def setTargetMaterialPort(self, portObject):
        self._targetMaterialPortObj = portObject

    def targetMaterialPort(self):
        return self._targetMaterialPortObj

    def sourceNodeGraphs(self):
        lis = []
        for portObject in self.inputs():
            if portObject.hasSource():
                node = portObject.source().node()
                nodeGraph = node.nodeGraph()
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
        return [
            self.dagpath(),
            self.category(),
            self.targetMaterialPort()
        ]

    def _xmlChildList(self):
        return self.valueChangedInputs()


# object > dag
class Abc_MtlDag(Abc_MtlObject):
    CLS_mtl_child_set = None
    def _initAbcMtlDag(self, *args):
        self._initAbcMtlObject(*args)

        self._childSetObj = self.CLS_mtl_child_set()

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
class Abc_MtlGeometry(Abc_MtlObject):
    CLS_mtl_node_dagpath = None
    CLS_mtl_object_def = None

    CLS_mtl_port_set = None
    CLS_mtl_visibility_set = None

    CLS_mtl_property = None
    CLS_mtl_visibility = None

    VAR_mtl_value_class_dict = {}

    def _initAbcMtlGeometry(self, *args):
        nodeString = args[0]
        self._initAbcMtlObject(
            self.DEF_mtl_category_geometry,
            nodeString
        )
        self._propertySetObj = self.CLS_mtl_port_set()
        self._visibilitySetObj = self.CLS_mtl_visibility_set()

        self._addGeometryPorts_()

        self._initAbcMtlXml()

    def _addGeometryPorts_(self):
        def addPortFnc_(portnameString_, portDef_):
            valueTypeString = portDef_[self.DEF_mtl_key_porttype]
            portdataString = portDef_[self.DEF_mtl_key_portdata]
            assignString = portDef_[self.DEF_mtl_key_assign]
            if assignString == self.DEF_mtl_keyword_property:
                portObj = self.CLS_mtl_property(self, portnameString_)
                self._addProperty_(portObj)
            else:
                portObj = self.CLS_mtl_visibility(self, portnameString_)
                self._addVisibility_(portObj)

            self._addAttribute_(portObj)

            valueCls = self.VAR_mtl_value_class_dict[valueTypeString]

            portObj._setValue_(valueCls(portdataString))
            portObj._setDefaultValue_(valueCls(portdataString))

        for k, v in self._objectDefObj.portDefs().items():
            addPortFnc_(k, v)

    def _addProperty_(self, portObject):
        self._propertySetObj.addObject(portObject)

    def _addVisibility_(self, portObject):
        self._visibilitySetObj.addObject(portObject)

    def property(self, portnameString):
        return self._propertySetObj.objectWithKey(portnameString)

    def hasProperty(self, *args):
        return self._propertySetObj.hasObject(*args)

    def properties(self):
        return self._propertySetObj.objects()

    def visibility(self, portnameString):
        return self._visibilitySetObj.objectWithKey(portnameString)

    def hasVisibility(self, *args):
        return self._visibilitySetObj.hasObject(*args)

    def visibilities(self):
        return self._visibilitySetObj.objects()

    def valueChangedInputs(self):
        def _addFnc(portObject):
            if not portObject in lis:
                lis.append(portObject)

        lis = []
        for i in self.properties() + self.visibilities():
            if i.isValueChanged() or i.hasSource():
                if i.hasParent():
                    _addFnc(i.parent())
                _addFnc(i)
        return lis

    def toString(self):
        return self.fullpathName()

    def _queryString(self):
        return self.fullpathName()

    def _xmlAttributeObjectLis(self):
        return [
            self.dagpath()
        ]

    def _xmlChildList(self):
        return self.valueChangedInputs()


# portset
class Abc_MtlPortset(Abc_MtlBasic):
    CLS_mtl_name = None

    CLS_mtl_port_set = None
    
    def _initAbcMtlPortset(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._inputSetObj = self.CLS_mtl_port_set()

        self._initAbcMtlXml()

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

    def addAttribute(self, portObject):
        self._inputSetObj.addObject(portObject)

    def attributes(self):
        return self._inputSetObj.objects()

    def _xmlAttributeValueString(self):
        return self.nameString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# portset > propertyset
class Abc_MtlPropertyset(Abc_MtlPortset):
    def _initAbcMtlPropertyset(self, *args):
        self._initAbcMtlPortset(*args)

    def _xmlAttributeObjectLis(self):
        return [
            self.name()
        ]

    def _xmlChildList(self):
        return self.attributes()


# node graph output
class Abc_MtlNodeGraphOutput(Abc_MtlBasic):
    CLS_mtl_name = None

    def _initAbcMtlNodeGraphOutput(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

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

    def _setPort_(self, outputObject):
        self._portObj = outputObject
        self._portObj._setNodeGraphOutput_(self)

    def port(self):
        return self._portObj

    def porttype(self):
        return self._portObj.porttype()

    def _setNodeGraph_(self, nodeGraphObject):
        self._nodeGraphObj = nodeGraphObject

    def nodeGraph(self):
        return self._nodeGraphObj

    def _queryString(self):
        return self.nameString()

    def _xmlAttributeObjectLis(self):
        return [
            self.name(),
            self.porttype(),
            self.port()
        ]

    def _xmlAttributeValueString(self):
        return self.nameString()

    def _xmlAttributeRaw(self):
        return [
            self.nodeGraph(),
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


class Abc_MtlNodeGraph(Abc_MtlBasic):
    CLS_mtl_name = None

    CLS_mtl_node_set = None
    CLS_mtl_output_set = None

    CLS_mtl_node = None
    CLS_mtl_output = None

    def _initAbcMtlNodeGraph(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._nodeSetObj = self.CLS_mtl_node_set()
        self._outputSetObj = self.CLS_mtl_output_set()

        self._outputDic = {}

        self._initAbcMtlXml()

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
            1.object of Node
            2.str(node category), str(node name)
        :return:
        """
        if isinstance(args[0], Abc_MtlObject):
            nodeObject = args[0]
        else:
            nodeObject = self.CLS_mtl_node(*args)

        nodeObject._setNodeGraph_(self)

        self._nodeSetObj.addObject(nodeObject)

        outputObjects = nodeObject.connectedOutputs(toShader=True)
        if outputObjects:
            for outputObject in outputObjects:
                name = u'output{}'.format(self._outputSetObj.objectCount())
                nodeGraphOutputObject = self.CLS_mtl_output(name)
                nodeGraphOutputObject._setPort_(outputObject)
                self._addOutput_(nodeGraphOutputObject)

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
        return self._nodeSetObj.objects()

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

    def _addOutput_(self, outputObject):
        """
        :param outputObject: object of Output
        :return: None
        """
        outputObject._setNodeGraph_(self)

        self._outputSetObj.addObject(outputObject)

    def outputs(self):
        """
        :return: list(object or output, ...)
        """
        return self._outputSetObj.objects()

    def output(self, fullpathPortname):
        """
        :param fullpathPortname: str
        :return: object of Output
        """
        return self._outputSetObj.objectWithKey(fullpathPortname)

    def getNodeGraphOutput(self, portObject):
        key = portObject.fullpathName()
        return self._outputDic[key]

    def hasOutputs(self):
        """
        :return: bool
        """
        return self._outputSetObj.hasObjects()

    def _xmlAttributeObjectLis(self):
        return [
            self._nameObj
        ]

    def _xmlChildList(self):
        return self.nodes() + self.outputs()

    def _xmlAttributeValueString(self):
        return self.nameString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


# geometry collection
class Abc_MtlGeometryCollection(Abc_MtlBasic):
    CLS_mtl_name = None

    CLS_set_geometry = None
    CLS_set_collection = None

    DEF_geometry_separator = None

    def _initAbcMtlGeometryCollection(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_set_geometry()
        self._collectionSetObj = self.CLS_set_collection()
        self._excludeGeometrySetObj = self.CLS_set_geometry()

        self._initAbcMtlXml()

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
        return [
            self._nameObj,
            self.geometrySet(),
            self.collectionSet(),
            self.excludeGeometrySet()
        ]

    def _xmlAttributeValueString(self):
        return self.nameString()

    def _xmlAttributeRaw(self):
        return [
            (self._xmlAttributeKeyString(), self._xmlAttributeValueString())
        ]


class Abc_MtlAssign(Abc_MtlBasic):
    CLS_mtl_name = None
    CLS_set_geometry = None

    DEF_geometry_separator = None

    def _initAbcMtlAssign(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_set_geometry()
        self._collectionObj = None

        self._lookObj = None

        self._initAbcMtlXml()

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


class Abc_MtlShadersetAssign(Abc_MtlAssign):
    def _initAbcMtlShadersetAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._shadersetObj = None

    def _shadersetObject(self):
        return self._shadersetObj

    def setMaterial(self, shadersetObject):
        """
        :param shadersetObject: object of Material
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
        return [
            self.name(),
            self.shaderset(),
            self.geometrySet(),
            self.collection()
        ]


class Abc_MtlPropertysetAssign(Abc_MtlAssign):
    def _initAbcMtlPropertysetAssign(self, *args):
        self._initAbcMtlAssign(*args)

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
        return [
            self.name(),
            self.propertyset(),
            self.geometrySet(),
            self.collection()
        ]


class Abc_MtlVisibilityAssign(Abc_MtlAssign):
    CLS_mtl_type = None
    CLS_value_visibility = None

    CLS_set_geometry_viewer = None

    CLS_mtl_object_def = None

    def _initAbcMtlVisibilityAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._objectDefObj = self.CLS_mtl_object_def(
            self.DEF_mtl_category_geometry
        )

        self._typeObj = None

        self._visibilityValueObj = None
        self._defVisibilityValueObj = None

        self._viewerGeometrySetObj = self.CLS_set_geometry_viewer()

    def setTypeString(self, portnameString):
        self._typeObj = self.CLS_mtl_type(portnameString)

        i = self._objectDefObj.getPortDef(portnameString)
        portdataString = i[self.DEF_mtl_key_portdata]

        self._visibilityValueObj = self.CLS_value_visibility(portdataString)

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
        return [
            self.name(),
            self.type(),
            self.visible(),
            self.geometrySet(),
            self.viewerGeometrySet(),
            self.collection()
        ]


class Abc_MtlLook(Abc_MtlBasic):
    CLS_mtl_name = None

    CLS_set_assign = None

    CLS_set_assign_shaderset = None
    ClS_set_assign_propertyset = None
    CLS_mtl_visibility_set = None

    def _initAbcMtlLook(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._shadersetAssignSetObj = self.CLS_set_assign_shaderset()
        self._propertysetAssignSetObj = self.ClS_set_assign_propertyset()
        self._visibilitySetObj = self.CLS_mtl_visibility_set()

        self._assignSetObj = self.CLS_set_assign()

        self._initAbcMtlXml()

    def nameString(self):
        return self._nameObj.toString()

    def _assignSetObject(self):
        return self._assignSetObj

    def addVisibilityAssign(self, visibilityAssignObject):
        """
        :param visibilityAssignObject: object of VisibilityAssign
        :return:
        """
        assert isinstance(visibilityAssignObject, Abc_MtlVisibilityAssign)

        count = self._visibilitySetObj.objectCount()
        if visibilityAssignObject.hasNameString() is False:
            visibilityAssignObject.setNameString('visibility_assign_{}'.format(count))
        self._visibilitySetObj.addObject(visibilityAssignObject)

    def visibilityAssigns(self):
        return self._visibilitySetObj.objects()

    def addShadersetAssign(self, shadersetAssignObject):
        """
        :param shadersetAssignObject: object of ShadersetAssign
        :return:
        """
        assert isinstance(shadersetAssignObject, Abc_MtlShadersetAssign)

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
        assert isinstance(propertysetAssignObject, Abc_MtlPropertysetAssign)

        count = self._propertysetAssignSetObj.objectCount()
        if propertysetAssignObject.hasNameString() is False:
            propertysetAssignObject.setNameString('propertyset_assign_{}'.format(count))
        self._propertysetAssignSetObj.addObject(propertysetAssignObject)

    def propertysetAssigns(self):
        return self._propertysetAssignSetObj.objects()

    def addAssign(self, assignObject):
        if isinstance(assignObject, Abc_MtlVisibilityAssign):
            self.addVisibilityAssign(assignObject)
        elif isinstance(assignObject, Abc_MtlShadersetAssign):
            self.addShadersetAssign(assignObject)
        elif isinstance(assignObject, Abc_MtlPropertysetAssign):
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
        return [
            self._nameObj
        ]

    def _xmlChildList(self):
        return self.assigns()

    def _xmlElementList(self):
        return self._givens()


class Abc_MtlFileReference(Abc_MtlBasic):
    CLS_mtl_file = None

    def _initAbcMtlFileReference(self, *args):
        self._fileObj = self.CLS_mtl_file(*args)

        self._initAbcMtlXml()

    def _fileObject(self):
        return self._fileObj

    def file(self):
        return self._fileObject()

    def filenameString(self):
        return self._fileObject().toString()

    def _queryString(self):
        return self.filenameString()

    def _xmlAttributeObjectLis(self):
        return [
            self.file()
        ]


class Abc_MtlFile(Abc_MtlBasic):
    CLS_mtl_file = None

    CLS_mtl_version = None

    CLS_mtl_reference_file_set = None
    CLS_mtl_look_set = None

    VAR_mtlx_version = None

    def _initAbcMtlFile(self, *args):
        self._fileObj = self.CLS_mtl_file(*args)
        self._versionObj = self.CLS_mtl_version(self.VAR_mtlx_version)

        self._referenceSetObj = self.CLS_mtl_reference_file_set()
        self._lookSetObj = self.CLS_mtl_look_set()

        self._initAbcMtlXml()

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
        return [
            self.version()
        ]

    def _xmlChildList(self):
        return self.looks()


class Abc_DccMtlBasicDef(mtlConfigure.Utility):
    CLS_mtl_basic_def = None
    # noinspection PyUnusedLocal
    def _initAbcDccMtlBasicDef(self, *args):
        self._nodeRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_node_defs_file
        ) or {}
        self._geometryRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_geometry_def_file
        ) or {}
        self._materialRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_material_def_file
        ) or {}
        self._outputRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_output_defs_file
        ) or {}

        self._portChildRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_arnold_port_child_defs_file
        ) or {}
        self._dccNodeRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_maya_arnold_node_defs_file
        ) or {}
        self._dccGeometryRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_maya_arnold_geometry_def_file
        ) or {}
        self._dccMaterialRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_maya_arnold_material_def_file
        ) or {}
        self._dccOutputRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_maya_arnold_output_defs_file
        ) or {}

        self._dccPortChildRaw = bscMethods.OsJsonFile.read(
            self.DEF_mtl_maya_arnold_port_child_defs_file
        ) or {}

        self._basicDefObj = self.CLS_mtl_basic_def()

        self._dccTypeStringDict = self.CLS_ordered_dict()
        self._dccCategoryStringDict = self.CLS_ordered_dict()
        self._dccPortDefsDict = self.CLS_ordered_dict()

        self._getData_()

    def getMtlObjectTypeString(self, dccCategoryString):
        return self._dccTypeStringDict.get(dccCategoryString)

    def getMtlCategoryString(self, dccCategoryString):
        return self._dccCategoryStringDict.get(dccCategoryString)

    def getMtlObjectPortDefs(self, dccCategoryString):
        return self._dccPortDefsDict.get(dccCategoryString, {})

    def getMtlPortnameString(self, dccCategoryString, dccPortnameString):
        return self._dccPortDefsDict[dccCategoryString][dccPortnameString][self.DEF_mtl_key_portname]

    def _getData_(self):
        def getDccTypeFnc_(dccCategoryString_, typeString_):
            self._dccTypeStringDict[dccCategoryString_] = typeString_

        def getDccCategoryStringFnc_(dccCategoryString_, categoryString):
            self._dccCategoryStringDict[dccCategoryString_] = categoryString

        def getDccNodeFnc_():
            for _dccCategoryString, _dccObjectDef in self._dccNodeRaw.items():
                _categoryString = _dccObjectDef[self.DEF_mtl_key_target]
                _objectDef = self._nodeRaw[_categoryString]

                _typeString = _objectDef[self.DEF_mtl_key_type]
                getDccTypeFnc_(_dccCategoryString, _typeString)

                getDccCategoryStringFnc_(_dccCategoryString, _categoryString)

                getDccNodeSubFnc_(_typeString, _dccCategoryString, _categoryString, _dccObjectDef)

        def getDccNodeSubFnc_(typeString_, dccCategoryString_, categoryString_, dccObjectDef_):
            self._dccPortDefsDict[dccCategoryString_] = self.CLS_ordered_dict()

            portDefs = self._basicDefObj.getObjectPortDefs(categoryString_)

            _dccPortDefs = dccObjectDef_[self.DEF_mtl_key_port]
            for dccPortnameString, dccPortDef in _dccPortDefs.items():
                portnameString = dccPortDef[self.DEF_mtl_key_target]

                getDccPortFnc_(dccCategoryString_, dccPortnameString, portnameString, portDefs)
            #
            _dccPortDefs = self._dccOutputRaw.get(typeString_, {})
            for dccPortnameString, dccPortDef in _dccPortDefs.items():
                portnameString = dccPortDef[self.DEF_mtl_key_target]
                getDccPortFnc_(dccCategoryString_, dccPortnameString, portnameString, portDefs)

        def getDccPortFnc_(dccCategoryString_, dccPortnameString_, portnameString_, portDefs_):
            _portDef = portDefs_[portnameString_]
            _porttypeString = _portDef[self.DEF_mtl_key_porttype]
            _portdataString = _portDef[self.DEF_mtl_key_portdata]
            _assignString = _portDef[self.DEF_mtl_key_assign]

            addPortFnc_(dccCategoryString_, dccPortnameString_, portnameString_, _porttypeString, _portdataString, _assignString, None)
            childDefs = self._dccPortChildRaw.get(_porttypeString, [])
            for portDef in childDefs:
                getChildFnc_(dccCategoryString_, dccPortnameString_, portnameString_, portDef, portDefs_)

        def getChildFnc_(dccCategoryString_, dccParentPortnameString_, parentPortnameString_, dccPortDef_, portDefs_):
            _dccFormatString = dccPortDef_[self.DEF_mtl_key_format]
            _formatString = dccPortDef_[self.DEF_mtl_key_target][self.DEF_mtl_key_format]
            _dccPortnameString = _dccFormatString.format(*[dccParentPortnameString_])
            _portnameString = _formatString.format(*[parentPortnameString_])
            _portDef = portDefs_[_portnameString]
            _porttypeString = _portDef[self.DEF_mtl_key_porttype]
            _portdataString = _portDef[self.DEF_mtl_key_portdata]
            _assignString = _portDef[self.DEF_mtl_key_assign]
            addPortFnc_(dccCategoryString_, _dccPortnameString, _portnameString, _porttypeString, _portdataString, _assignString, parentPortnameString_)

        def addPortFnc_(dccCategoryString_, dccPortnameString_, portnameString_, porttypeString_, valueString_, assignString_, parentPortnameString_):
            _dic = self.CLS_ordered_dict()
            _dic[self.DEF_mtl_key_portname] = portnameString_
            _dic[self.DEF_mtl_key_porttype] = porttypeString_
            _dic[self.DEF_mtl_key_portdata] = valueString_
            _dic[self.DEF_mtl_key_assign] = assignString_
            _dic[self.DEF_mtl_key_parent] = parentPortnameString_
            self._dccPortDefsDict[dccCategoryString_][dccPortnameString_] = _dic

        getDccNodeFnc_()
        getDccNodeSubFnc_(
            self.DEF_mtl_category_material,
            self.DEF_mtl_maya_category_material,
            self.DEF_mtl_category_material,
            self._dccMaterialRaw
        )
        getDccNodeSubFnc_(
            self.DEF_mtl_category_geometry,
            self.DEF_mtl_maya_category_geometry,
            self.DEF_mtl_category_geometry,
            self._dccGeometryRaw
        )


# dcc node def
class Abc_DccMtlObjectDef(mtlConfigure.Utility):
    CLS_mtl_dcc_basic_def = None
    CLS_mtl_object_def = None

    def _initAbcDccMtlObjectDef(self, *args):
        dccCategoryString = args[0]

        self._dccBasicDefObj = self.CLS_mtl_dcc_basic_def()

        self._dccCategoryString = dccCategoryString
        self._dccTypeString = None

        self._typeString = self._dccBasicDefObj.getMtlObjectTypeString(dccCategoryString)
        self._categoryString = self._dccBasicDefObj.getMtlCategoryString(dccCategoryString)
        self._dccPortDefsDef = self._dccBasicDefObj.getMtlObjectPortDefs(dccCategoryString)

        self._defObjectObj = self.CLS_mtl_object_def(self._categoryString)

    def dccTypeString(self):
        return self._dccTypeString

    def dccCategoryString(self):
        return self._dccCategoryString

    def dccPortDefs(self):
        return self._dccPortDefsDef

    def defObject(self):
        return self._defObjectObj


class Abc_DccMtlNodeDef(Abc_DccMtlObjectDef):
    def _initAbcDccMtlNodeDef(self, *args):
        self._initAbcDccMtlObjectDef(*args)


class Abc_DccMtlMaterialDef(Abc_DccMtlObjectDef):
    def _initAbcDccMtlMaterialDef(self, *args):
        self._initAbcDccMtlObjectDef(*args)


class Abc_DccMtlGeometryDef(Abc_DccMtlObjectDef):
    def _initAbcDccMtlGeometryDef(self, *args):
        self._initAbcDccMtlObjectDef(*args)


# dcc node def
class Abc_DccMtlObject(mtlConfigure.Utility):
    CLS_mtl_object = None
    CLS_mtl_dcc_object = None

    CLS_mtl_dcc_object_def = None

    def _initAbcDccMtlObject(self, *args):
        dccNodeString = args[0]

        self._dccNodeString = dccNodeString
        self._dccObjectObj = self.CLS_mtl_dcc_object(dccNodeString)
        self._nodeString = self._dccObjectObj.fullpathName().replace(self.DEF_mya_node_separator, self.DEF_mtl_node_separator)

        self._dccObjectDefObj = self.CLS_mtl_dcc_object_def(self.dccCategoryString())

        self._getObject_()

        self._getPorts_()

    def _getObject_(self):
        self._objectObj = self.CLS_mtl_object(
            self._dccObjectDefObj.defObject().categoryString(),
            self._dccObjectObj.fullpathName()
        )

    def _getPorts_(self):
        def getPortFnc_(_dccPortnameString, dccPortDatum_):
            _portnameString = dccPortDatum_[self.DEF_mtl_key_portname]

            _dccPort = self._dccObjectObj.attribute(_dccPortnameString)
            _port = self._objectObj.attribute(_portnameString)
            _port.value().setRaw(_dccPort.portdata())
            if _dccPort.hasSource():
                _dccSource = _dccPort.source()
                _dccSourceNode = _dccSource.node()
                _dccSourceCategoryString = _dccSourceNode.category()
                _dccSourcePortnameString = _dccSource.fullpathPortname()

                print self._dccObjectDefObj._dccBasicDefObj.getMtlPortnameString(_dccSourceCategoryString, _dccSourcePortnameString)

                _sourceNodeCls = self._objectObj.CLS_mtl_source_object
                if _sourceNodeCls is None:
                    _sourceNodeCls = self._objectObj.__class__

        def getChildFnc_(dccPortDatum_):
            _dccPortnameString = dccPortDatum_[self.DEF_mtl_key_dcc_portname]
            _portnameString = dccPortDatum_[self.DEF_mtl_key_portname]

            _dccPort = self._dccObjectObj.attribute(_dccPortnameString)
            if _dccPort.hasSource():
                _dccSource = _dccPort.source()
                _dccSourceNode = _dccSource.node()

        for dccPortnameString, dccPortDatum in self._dccObjectDefObj.dccPortDefs().items():
            getPortFnc_(dccPortnameString, dccPortDatum)

    # dcc
    def dccObjectDef(self):
        return self._dccObjectDefObj

    def dccObject(self):
        return self._dccObjectObj

    def dccCategoryString(self):
        return self.dccObject().category()

    # materialx
    def objectDef(self):
        return self.object().objectDef()

    def object(self):
        return self._objectObj

    def categoryString(self):
        return self.object().categoryString()


# dcc material
class Abc_DccMtlMaterial(Abc_DccMtlObject):
    def _initAbcDccMtlMaterial(self, *args):
        self._initAbcDccMtlObject(*args)

    def _getObject_(self):
        self._objectObj = self.CLS_mtl_object(
            self.dccObject().fullpathName()
        )


# dcc geometry
class Abc_DccMtlGeometry(Abc_DccMtlObject):
    def _initAbcDccMtlGeometry(self, *args):
        self._initAbcDccMtlObject(*args)

    def _getObject_(self):
        self._objectObj = self.CLS_mtl_object(
            self._nodeString
        )


class Abc_DccMtlShader(Abc_DccMtlObject):
    pass


# dcc node
class Abc_DccMtlNode(Abc_DccMtlObject):
    def _initAbcDccMtlNode(self, *args):
        self._initAbcDccMtlObject(*args)
