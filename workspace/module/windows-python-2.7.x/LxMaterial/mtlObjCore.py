# coding:utf-8
from LxBasic import bscMethods

from LxMaterial import mtlConfigure, mtlMethods


class Def_MtlXml(mtlConfigure.Utility):
    DEF_mtl_file_attribute_separator = u' '

    VAR_mtl_file_element_key = u''
    VAR_mtl_file_attribute_key = u''

    def _initDefMtlXml(self):
        self._xmlIndentStr = ''

    def _xmlElement_(self):
        return self.VAR_mtl_file_element_key

    def _xmlAttachKey_(self):
        return self.VAR_mtl_file_attribute_key

    def _xmlAttachValue_(self):
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

    def _xmlAttaches_(self):
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
                    attributeRaw = attributeObject_._xmlAttaches_()
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

            tagString = elementObject_._xmlElement_()
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


class Abc_MtlDefCache(mtlConfigure.Utility):
    VAR_mtl_node_defs_file = None
    VAR_mtl_geometry_def_file = None
    VAR_mtl_material_def_file = None
    VAR_mtl_output_defs_file = None
    VAR_mtl_port_child_defs_file = None

    # noinspection PyUnusedLocal
    def _initAbcMtlDefCache(self, *args):
        self._nodeRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_node_defs_file
        ) or {}
        self._geometryRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_geometry_def_file
        ) or {}
        self._materialRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_material_def_file
        ) or {}
        self._outputRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_output_defs_file
        ) or {}
        self._portChildRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_port_child_defs_file
        ) or {}

        self._initialize_()

    def getObjectCategoryStrings(self):
        return self._typeStringDict.keys()

    def getObjectTypeString(self, categoryString):
        return self._typeStringDict.get(categoryString)

    def getObjectPortDefs(self, categoryString):
        return self._portDefsDict.get(categoryString, {})

    def getObjectPortDef(self, categoryString, portString):
        return self.getObjectPortDefs(categoryString).get(portString)

    def _initialize_(self):
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

        def getPortFnc_(
                categoryString_,
                portDef_
        ):
            _portnameString = portDef_[self.DEF_mtl_key_portname]
            _porttypeString = portDef_[self.DEF_mtl_key_porttype]
            _portdataString = portDef_[self.DEF_mtl_key_portdata]
            _assignString = portDef_[self.DEF_mtl_key_assign]

            _childPortnameStrings = []
            for seq, i in enumerate(self._portChildRaw.get(_porttypeString, [])):
                _childPortnameString = getChildFnc_(seq, categoryString_, _portnameString, _portdataString, _assignString, i)
                _childPortnameStrings.append(_childPortnameString)
            addPortFnc_(
                categoryString_,
                _portnameString,
                _porttypeString,
                _portdataString,
                _assignString,
                None,
                _childPortnameStrings
            )

        def getChildFnc_(
                childIndex_,
                categoryString_,
                parentPortnameString_,
                parentPortdataString_,
                parentAssignString_,
                portDef_
        ):
            _formatString = portDef_[self.DEF_mtl_key_format]
            _portnameString = _formatString.format(*[parentPortnameString_])
            _porttypeString = portDef_[self.DEF_mtl_key_porttype]

            if parentPortdataString_:
                _portdataString = parentPortdataString_.split(u',')[childIndex_].rstrip().lstrip()
            else:
                _portdataString = portDef_[self.DEF_mtl_key_portdata]

            assignString = portDef_[self.DEF_mtl_key_assign]
            addPortFnc_(
                categoryString_,
                _portnameString,
                _porttypeString,
                _portdataString,
                (parentAssignString_, assignString),
                parentPortnameString_,
                []
            )
            return _portnameString

        def addPortFnc_(
                categoryString_,
                portnameString_,
                porttypeString_,
                valueString_,
                assignString_,
                parentPortnameString_,
                childrenPortnameStrings_
        ):
            _dic = self.CLS_ordered_dict()
            _dic[self.DEF_mtl_key_porttype] = porttypeString_
            _dic[self.DEF_mtl_key_portdata] = valueString_
            _dic[self.DEF_mtl_key_assign] = assignString_
            _dic[self.DEF_mtl_key_parent] = parentPortnameString_
            _dic[self.DEF_mtl_key_children] = childrenPortnameStrings_
            self._portDefsDict[categoryString_][portnameString_] = _dic

        self._typeStringDict = self.CLS_ordered_dict()
        self._portDefsDict = self.CLS_ordered_dict()

        getNodeFnc_()
        getNodeSubFnc_(self.DEF_mtl_category_material, self._materialRaw)
        getNodeSubFnc_(self.DEF_mtl_category_geometry, self._geometryRaw)


class Abc_DccMtlDefCache(mtlConfigure.Utility):
    VAR_mtl_dcc_node_defs_file = None
    VAR_mtl_dcc_geometry_def_file = None
    VAR_mtl_dcc_material_def_file = None
    VAR_mtl_dcc_output_defs_file = None
    VAR_mtl_dcc_port_child_defs_file = None

    OBJ_mtl_def_cache = None

    # noinspection PyUnusedLocal
    def _initAbcDccMtlDefCache(self, *args):
        self._dccNodeRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_node_defs_file
        ) or {}
        self._dccGeometryRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_geometry_def_file
        ) or {}
        self._dccMaterialRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_material_def_file
        ) or {}
        self._dccOutputRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_output_defs_file
        ) or {}
        self._dccPortChildRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_port_child_defs_file
        ) or {}

        self._initialize_()

    def getDccObjectCategoryStrings(self):
        return self._dccTypeStringDict.keys()

    def getDccObjectTypeString(self, dccCategoryString):
        return self._dccTypeStringDict.get(dccCategoryString)

    def getDccObjectCategoryString(self, dccCategoryString):
        return self._dccCategoryStringDict.get(dccCategoryString)

    def getDccObjectPortDefs(self, dccCategoryString):
        return self._dccPortDefsDict.get(dccCategoryString, {})

    def getDccObjectPortDef(self, dccCategoryString, dccPortnameString):
        return self.getDccObjectPortDefs(dccCategoryString).get(dccPortnameString)

    def getDccObjectPortnameString(self, dccCategoryString, dccPortnameString):
        return self._dccPortDefsDict[dccCategoryString][dccPortnameString][self.DEF_mtl_key_portname]

    def _initialize_(self):
        def getDccTypeFnc_(dccCategoryString_, typeString_):
            self._dccTypeStringDict[dccCategoryString_] = typeString_

        def getDccCategoryStringFnc_(dccCategoryString_, categoryString):
            self._dccCategoryStringDict[dccCategoryString_] = categoryString

        def getDccNodeFnc_():
            for _dccCategoryString, _dccObjectDef in self._dccNodeRaw.items():
                _categoryString = _dccObjectDef[self.DEF_mtl_key_target]
                _typeString = self.OBJ_mtl_def_cache.getObjectTypeString(_categoryString)

                getDccTypeFnc_(_dccCategoryString, _typeString)

                getDccCategoryStringFnc_(_dccCategoryString, _categoryString)

                getDccNodeSubFnc_(_typeString, _dccCategoryString, _categoryString, _dccObjectDef)

        def getDccNodeSubFnc_(typeString_, dccCategoryString_, categoryString_, dccObjectDef_):
            self._dccPortDefsDict[dccCategoryString_] = self.CLS_ordered_dict()

            portDefs = self.OBJ_mtl_def_cache.getObjectPortDefs(categoryString_)

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

            _childPortnameStrings = []
            childDefs = self._dccPortChildRaw.get(_porttypeString, [])
            for portDef in childDefs:
                _childPortnameString = getChildFnc_(dccCategoryString_, dccPortnameString_, portnameString_, portDef, portDefs_)
                _childPortnameStrings.append(_childPortnameString)

            addPortFnc_(
                dccCategoryString_,
                dccPortnameString_,  portnameString_,
                _porttypeString,
                _portdataString,
                _assignString,
                None,
                _childPortnameStrings
            )

        def getChildFnc_(
                dccCategoryString_,
                dccParentPortnameString_, parentPortnameString_,
                dccPortDef_, portDefs_
        ):
            _dccFormatString = dccPortDef_[self.DEF_mtl_key_format]
            _formatString = dccPortDef_[self.DEF_mtl_key_target][self.DEF_mtl_key_format]
            _dccPortnameString = _dccFormatString.format(*[dccParentPortnameString_])
            _portnameString = _formatString.format(*[parentPortnameString_])
            _portDef = portDefs_[_portnameString]
            _porttypeString = _portDef[self.DEF_mtl_key_porttype]
            _portdataString = _portDef[self.DEF_mtl_key_portdata]
            _assignString = _portDef[self.DEF_mtl_key_assign]
            addPortFnc_(
                dccCategoryString_,
                _dccPortnameString,  _portnameString,
                _porttypeString,
                _portdataString,
                _assignString,
                parentPortnameString_,
                []
            )
            return _portnameString

        def addPortFnc_(
                dccCategoryString_,
                dccPortnameString_,  portnameString_,
                porttypeString_,
                valueString_,
                assignString_,
                parentPortnameString_,
                childrenPortnameStrings_
        ):
            _dic = self.CLS_ordered_dict()
            _dic[self.DEF_mtl_key_portname] = portnameString_
            _dic[self.DEF_mtl_key_porttype] = porttypeString_
            _dic[self.DEF_mtl_key_portdata] = valueString_
            _dic[self.DEF_mtl_key_assign] = assignString_
            _dic[self.DEF_mtl_key_parent] = parentPortnameString_
            _dic[self.DEF_mtl_key_children] = childrenPortnameStrings_
            self._dccPortDefsDict[dccCategoryString_][dccPortnameString_] = _dic

        self._dccTypeStringDict = self.CLS_ordered_dict()
        self._dccCategoryStringDict = self.CLS_ordered_dict()
        self._dccPortDefsDict = self.CLS_ordered_dict()

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


class Def_MtlObjCache(object):
    def _initDefMtlCache(self, keyString):
        self._objQueryKeyString = keyString

    def _mtlObjCacheKeyString_(self):
        return self._objQueryKeyString


class Abc_MtlObjCache(mtlConfigure.Utility):
    DEF_mtl_key_index = u'index'

    def _initAbcMtlObjCache(self):
        self._objectDict = {}
        self._objectList = []

        self._objectCount = 0

    def _initialize_(self):
        self._objectDict = {}
        self._objectList = []

        self._objectCount = 0

    def _addObject_(self, *args):
        if len(args) == 2:
            objectString, obj = args
        else:
            obj = args[0]
            objectString = obj._mtlObjCacheKeyString_()

        index = self._objectCount
        if obj not in self._objectList:
            self._objectList.append(obj)
            if objectString not in self._objectDict:
                self._objectDict[objectString] = {}
            self._objectDict[objectString][self.DEF_mtl_key_index] = index
            self._objectCount += 1

    def _hasObject_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objectString = args[0]
            return objectString in self._objectDict
        elif isinstance(args[0], int):
            index = args[0]
            return 0 <= index <= (self._objectCount - 1)
        elif isinstance(args[0], Def_MtlObjCache):
            objectString = args[0]._mtlObjCacheKeyString_()
            return objectString in self._objectDict

    def _object_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objectString = args[0]
            index = self._objectDict[objectString][self.DEF_mtl_key_index]
            return self._objectList[index]
        elif isinstance(args[0], int):
            index = args[0]
            return self._objectList[index]

    def _index_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objectString = args[0]
            return self._objectDict[objectString][self.DEF_mtl_key_index]
        elif isinstance(args[0], Def_MtlObjCache):
            cacheObject = args[0]
            return self._objectList.index(cacheObject)

    def _updateObject_(self, obj):
        if self._hasObject_(obj) is False:
            self._addObject_(obj)

    def addObject(self, obj):
        objectString = obj._mtlObjCacheKeyString_()
        assert objectString not in self._objectDict, u'''"{}" is Registered.'''.format(objectString)
        self._addObject_(obj)

    def objectCount(self):
        """
        :return: int
        """
        return self._objectCount

    def hasObjects(self):
        return self._objectList != []

    def hasObject(self, objectString):
        return self._hasObject_(objectString)

    def objects(self):
        return self._objectList

    def object(self, objectString):
        assert objectString in self._objectDict, u'''"{}" is Unregistered.'''.format(objectString)
        return self._object_(objectString)

    def objectNames(self):
        return [i._mtlObjCacheKeyString_() for i in self._objectList]


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

    def _xmlAttachValue_(self):
        return self.toString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
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


class ABc_MtlPath(Abc_MtlRaw):
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


class Abc_MtlDagpath(ABc_MtlPath):
    def _initAbcMtlDagpath(self, *args):
        self._initAbcMtlPath(*args)


class Abc_MtlFilePath(ABc_MtlPath):
    def _initAbcMtlFilePath(self, *args):
        self._initAbcMtlPath(*args)


class Abc_MtlMaterialDagpath(Abc_MtlDagpath):
    def _initAbcMtlMaterialDagpath(self, *args):
        self._initAbcMtlDagpath(*args)

    def _xmlAttachValue_(self):
        return self.fullpathName()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_()),
        ]


class Abc_MtlObjectSet(Def_MtlXml):
    VAR_mtl_object_separator = u','
    # noinspection PyUnusedLocal
    def _initAbcMtlObjectSet(self, *args):
        self._objectList = []
        self._objectDict = {}

        self._objectCount = 0

        self._initDefMtlXml()

    def _initialize_(self):
        self._objectList = []
        self._objectDict = {}

        self._objectCount = 0

    def _addObject_(self, *args):
        if len(args) == 2:
            queryString, obj = args
        else:
            obj = args[0]
            queryString = obj._queryKeyString_()

        self._objectList.append(obj)
        self._objectDict[queryString] = obj
        self._objectCount += 1

    def _hasObject_(self, *args):
        if isinstance(args[0], (str, unicode)):
            keyString = args[0]
            return keyString in self._objectDict
        elif isinstance(args[0], int):
            index = args[0]
            return 0 <= index <= (self._objectCount - 1)
        else:
            keyString = args[0]._queryKeyString_()
            return keyString in self._objectDict

    def _object_(self, *args):
        if isinstance(args[0], (str, unicode)):
            keyString = args[0]
            return self._objectDict[keyString]
        elif isinstance(args[0], int):
            index = args[0]
            return self._objectList[index]

    def _updateObject_(self, obj):
        if self._hasObject_(obj) is False:
            self._addObject_(obj)

    def addObject(self, obj):
        queryString = obj._queryKeyString_()
        assert queryString not in self._objectDict, u'''Key {} is Exist.'''.format(queryString)
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
        assert keyString in self._objectDict, u'''Key "{}" is Non - Exist.'''.format(keyString)
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

    def _xmlAttachValue_(self):
        return self.toString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
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

    def _xmlAttachValue_(self):
        return self.toString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
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

    def _xmlAttachValue_(self):
        return self.toString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
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

    def _xmlAttachValue_(self):
        return self.toString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
        ]

    def __len__(self):
        """
        :return: int
        """
        return self.childrenCount()


# value
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

    def _xmlAttachValue_(self):
        return self.toString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
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
class Abc_MtlPort(
    Def_MtlXml,
    Def_MtlObjCache
):
    CLS_mtl_port_dagpath = None

    def _initAbcMtlPort(self, *args):
        nodeObject, fullpathPortname = args

        self._objectObj = nodeObject
        self._dagpathObj = nodeObject.dagpath()

        self._portDagpathObj = self.CLS_mtl_port_dagpath(fullpathPortname)

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
        self._initDefMtlCache(self.fullpathName())

    def _setPorttypeString_(self, porttypeString):
        self._porttypeString = porttypeString

    def _setParentPortnameString_(self, portnameString):
        self._parentPortnameString = portnameString

    def _setChildPortnameStrings_(self, portnameStrings):
        self._childPortnameStringList = portnameStrings

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

    def setRaw(self, raw):
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
        return self._objectObj.OBJ_mtl_obj_cache._index_(portObject)

    def _qry_getObject_(self, index):
        return self._objectObj.OBJ_mtl_obj_cache._object_(index)

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
            return self._objectObj.OBJ_mtl_obj_cache._object_(
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
            return self._objectObj.attribute(
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
                self._objectObj.attribute(i)
                for i in self._childPortnameStringList
            ]

    def child(self, portnameString):
        if self.hasChildren():
            return self._objectObj.attribute(portnameString)

    def hasChild(self, portnameString):
        return portnameString in self._childPortnameStringList

    def _queryKeyString_(self):
        return self.fullpathPortname()

    def _xmlAttachValue_(self):
        return self.portname().toString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
        ]


# port > input
class Abc_MtlInput(Abc_MtlPort):
    def _initAbcMtlInput(self, *args):
        self._initAbcMtlPort(*args)

    def _attributeGiven_(self):
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
            self.dagpath(),
            self.porttype(),
            self._attributeGiven_()
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

    def _attributeGiven_(self):
        if self.hasSource() is True:
            return self._getNodeGraphOutput_()
        return self.value()


# port > output
class Abc_MtlOutput(Abc_MtlPort):
    def _initAbcMtlOutput(self, *args):
        self._initAbcMtlPort(*args)

    def _xmlAttachValue_(self):
        return self.fullpathPortname()

    def _xmlAttaches_(self):
        if self.hasParent():
            return [
                self.parent(),
                (self._xmlAttachKey_(), self.portnameString())
            ]
        else:
            return [
                self.node(),
                (self._xmlAttachKey_(), self.portnameString())
            ]

    def _xmlAttributes_(self):
        return [
            self.dagpath(),
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
            self.dagpath(),
            self.porttype(),
            self.value()
        ]


class Abc_MtlGeometryVisibility(Abc_MtlPort):
    def _initAbcMtlVisibility(self, *args):
        self._initAbcMtlPort(*args)

    def _xmlAttributes_(self):
        return [
            self.dagpath(),
            self.porttype(),
            self.value()
        ]


# object
class Abc_MtlObject(
    Def_MtlXml,
    Def_MtlObjCache
):
    CLS_mtl_type = None
    CLS_mtl_category = None

    CLS_mtl_node_dagpath = None

    CLS_mtl_port_set = None

    CLS_mtl_source_object = None

    OBJ_mtl_def_cache = None
    OBJ_mtl_obj_cache = None

    VAR_mtl_port_class_dict = {}
    VAR_mtl_value_class_dict = {}

    def _initAbcMtlObject(self, categoryString, objectString):
        self._categoryObj = self.CLS_mtl_category(categoryString)
        self._dagpathObj = self.CLS_mtl_node_dagpath(objectString)

        typeString = self.OBJ_mtl_def_cache.getObjectTypeString(categoryString)
        self._typeObj = self.CLS_mtl_type(typeString)

        self._portSetObj = self.CLS_mtl_port_set()
        self._inputSetObj = self.CLS_mtl_port_set()
        self._outputSetObj = self.CLS_mtl_port_set()

        self._initDefMtlCache(self.fullpathName())

        self.OBJ_mtl_obj_cache._addObject_(self)
        self._addPorts_()

        self._initDefMtlXml()

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
        if assignString == self.DEF_mtl_keyword_input or assignString == (self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_channel):
            self._inputSetObj._addObject_(portnameString, portObject)
        elif assignString == self.DEF_mtl_keyword_output or assignString == (self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_channel):
            self._outputSetObj._addObject_(portnameString, portObject)
        self._portSetObj._addObject_(portnameString, portObject)

    def _addPorts_(self):
        def addPortFnc_(portnameString_, portDef_):
            _porttypeString = portDef_[self.DEF_mtl_key_porttype]
            _valueString = portDef_[self.DEF_mtl_key_portdata]
            _assignString = portDef_[self.DEF_mtl_key_assign]
            _parentPortnameString = portDef_[self.DEF_mtl_key_parent]
            _childPortnameStrings = portDef_[self.DEF_mtl_key_children]

            _attributeString = mtlMethods.Attribute.composeBy(
                self.fullpathName(), portnameString_
            )

            if self.OBJ_mtl_obj_cache._hasObject_(_attributeString) is False:
                _portObject = self._getPortObject_(portnameString_, _assignString)
                if _portObject is not None:

                    _portObject._setParentPortnameString_(_parentPortnameString)
                    _portObject._setChildPortnameStrings_(_childPortnameStrings)

                    self.OBJ_mtl_obj_cache._addObject_(_portObject)
            else:
                _portObject = self.OBJ_mtl_obj_cache.object(_attributeString)

            if _portObject is not None:
                _valueCls = self.VAR_mtl_value_class_dict[_porttypeString]

                _portObject._setValue_(_valueCls(_valueString))
                _portObject._setDefaultValue_(_valueCls(_valueString))

                self._addPortObject_(_portObject, portnameString_, _assignString)

        portDefDict = self.OBJ_mtl_def_cache.getObjectPortDefs(
            self.categoryString()
        )
        for k, v in portDefDict.items():
            addPortFnc_(k, v)

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

    def dagpath(self):
        """
        :return: object of Dagpath
        """
        return self._dagpathObj

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

    def hasAttributes(self):
        return self._portSetObj.hasObjects()

    def hasAttribute(self, *args):
        return self._portSetObj._hasObject_(*args)

    def attributes(self):
        return self._portSetObj.objects()

    def attribute(self, fullpathPortname):
        return self._portSetObj.object(fullpathPortname)

    def hasInputs(self):
        return self._inputSetObj.hasObjects()

    def hasInput(self, *args):
        return self._inputSetObj._hasObject_(*args)

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
        return self._inputSetObj.object(fullpathPortname)

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

    def output(self, fullpathPortname):
        return self._outputSetObj.object(fullpathPortname)

    def toString(self):
        return self.fullpathName()

    def _queryKeyString_(self):
        return self.fullpathName()


# material
class Abc_MtlMaterial(Abc_MtlObject):
    def _initAbcMtlMaterial(self, *args):
        nodeString = args[0]
        self._initAbcMtlObject(
            self.DEF_mtl_category_material,
            nodeString
        )
        self._surfacePortObj = self.attribute(u'surface_shader')
        self._displacementPortObj = self.attribute(u'displacement_shader')
        self._volumePortObj = self.attribute(u'volume_shader')

        self._surfaceSourceObj = None
        self._surfaceShaderObj = None
        self._displacementSourceObj = None
        self._displacementShaderObj = None
        self._volumeSourceObj = None
        self._volumeShaderObj = None

    def surfaceInput(self):
        return self._surfacePortObj

    def displacementInput(self):
        return self._displacementPortObj

    def volumeInput(self):
        return self._volumePortObj

    def connectSurfaceFrom(self, portObject):
        self._surfacePortObj.connectFrom(portObject)

    def surfaceShader(self):
        if self._surfacePortObj.hasSource():
            return self._surfacePortObj.source().node()

    def connectDisplacementFrom(self, portObject):
        self._displacementPortObj.connectFrom(portObject)

    def displacementShader(self):
        if self._displacementPortObj.hasSource():
            return self._displacementPortObj.source().node()

    def connectVolumeFrom(self, portObject):
        self._volumePortObj.connectFrom(portObject)

    def volumeShader(self):
        if self._volumePortObj.hasSource():
            return self._volumePortObj.source().node()

    def shaders(self):
        return bscMethods.List.cleanupTo(
            [self.surfaceShader(), self.displacementShader(), self.volumeShader()]
        )

    def sourcePorts(self):
        pass

    def _xmlAttributes_(self):
        return [
            self.dagpath()
        ]

    def _xmlChildren_(self):
        # update shader's node graph first
        for s in self.shaders():
            s._updateNodeGraphs_()
        return self.shaders()

    def _xmlElements_(self):
        lis = []
        for s in self.shaders():
            objects = s.nodeGraphs()
            if objects:
                for o in objects:
                    if not o in lis:
                        lis.append(o)
        return lis

    def _xmlAttachValue_(self):
        return self.fullpathName()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
        ]


# object > node
class Abc_MtlNode(Abc_MtlObject):
    def _initAbcMtlNode(self, *args):
        self._initAbcMtlObject(*args)

        self._nodeGraphObj = None

    def _setNodeGraph_(self, nodeGraphObject):
        self._nodeGraphObj = nodeGraphObject

    def _xmlElement_(self):
        return self.categoryString()

    def _xmlAttributes_(self):
        return [
            self.dagpath(),
            self.type()
        ]

    def _xmlChildren_(self):
        return self.valueChangedInputs()

    def _xmlAttachValue_(self):
        return self.fullpathName()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
        ]


# object > shader
class Abc_MtlShader(Abc_MtlObject):
    CLS_mtl_node_graph = None
    CLS_mtl_node_graph_set = None

    def _initAbcMtlShader(self, *args):
        self._initAbcMtlObject(*args)

        self._nodeGraphSetObj = self.CLS_mtl_node_graph_set()
        self._addNodeGraph_()

    def _updateNodeGraphs_(self):
        if self.hasNodeGraphs():
            nodeGraphObject = self.nodeGraph(0)
            nodeGraphObject._update_(self)

    def _addNodeGraph_(self):
        nodeGraphObject = self.CLS_mtl_node_graph()

        count = self._nodeGraphSetObj.objectCount()
        nodeGraphObject.setNameString(
            self.fullpathName() + '__nodegraph_{}'.format(count)
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

    def nodeGraphs(self):
        return self._nodeGraphSetObj.objects()

    def _xmlAttributes_(self):
        return [
            self.dagpath(),
            self.category(),
            self._getMaterialTarget_()
        ]

    def _xmlChildren_(self):
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

    CLS_mtl_port_set = None
    CLS_mtl_property_set = None
    CLS_mtl_visibility_set = None

    CLS_mtl_material_set = None

    def _initAbcMtlGeometry(self, *args):
        nodeString = args[0]

        self._propertySetObj = self.CLS_mtl_property_set()
        self._visibilitySetObj = self.CLS_mtl_visibility_set()

        self._initAbcMtlObject(
            self.DEF_mtl_category_geometry,
            nodeString
        )

    def _addPortObject_(self, portObject, portnameString, assignString):
        if assignString == self.DEF_mtl_keyword_input or assignString == (self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_channel):
            self._inputSetObj._addObject_(portnameString, portObject)
        elif assignString == self.DEF_mtl_keyword_output or assignString == (self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_channel):
            self._outputSetObj._addObject_(portnameString, portObject)
        elif assignString == self.DEF_mtl_keyword_property:
            self._propertySetObj._addObject_(portnameString, portObject)
            self._inputSetObj._addObject_(portnameString, portObject)
        elif assignString == self.DEF_mtl_keyword_visibility:
            self._visibilitySetObj._addObject_(portnameString, portObject)
            self._inputSetObj._addObject_(portnameString, portObject)

        self._portSetObj._addObject_(portnameString, portObject)

    def property(self, portnameString):
        return self._propertySetObj.object(portnameString)

    def hasProperty(self, *args):
        return self._propertySetObj._hasObject_(*args)

    def properties(self):
        return self._propertySetObj.objects()

    def visibility(self, portnameString):
        return self._visibilitySetObj.object(portnameString)

    def hasVisibility(self, *args):
        return self._visibilitySetObj._hasObject_(*args)

    def visibilities(self):
        return self._visibilitySetObj.objects()

    def toString(self):
        return self.fullpathName()

    def _queryKeyString_(self):
        return self.fullpathName()

    def _xmlAttributes_(self):
        return [
            self.dagpath()
        ]

    def _xmlChildren_(self):
        return self.valueChangedInputs()


# portset
class Abc_MtlPortset(Def_MtlXml):
    CLS_mtl_name = None

    CLS_mtl_port_set = None
    
    def _initAbcMtlPortset(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._inputSetObj = self.CLS_mtl_port_set()

        self._initDefMtlXml()

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

    def _xmlAttachValue_(self):
        return self.nameString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
        ]


# portset > propertyset
class Abc_MtlPropertyset(Abc_MtlPortset):
    def _initAbcMtlPropertyset(self, *args):
        self._initAbcMtlPortset(*args)

    def _xmlAttributes_(self):
        return [
            self.name()
        ]

    def _xmlChildren_(self):
        return self.attributes()


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

    def _xmlAttachValue_(self):
        return self.nameString()

    def _xmlAttaches_(self):
        return [
            self.nodeGraph(),
            (self._xmlAttachKey_(), self._xmlAttachValue_())
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

        nodeObject._setNodeGraph_(self)
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
        nameString = u'output_{}'.format(count)
        nodeGraphOutputObject = self.CLS_mtl_node_graph_output(nameString)
        nodeGraphOutputObject._setPort_(sourceObject)
        nodeGraphOutputObject._setNodeGraph_(self)
        self._nodeGraphOutputSetObj.addObject(nodeGraphOutputObject)

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

    def _xmlAttachValue_(self):
        return self.nameString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
        ]


# geometry collection
class Abc_MtlGeometryCollection(Def_MtlXml):
    CLS_mtl_name = None

    CLS_set_geometry = None
    CLS_set_collection = None

    DEF_geometry_separator = None

    def _initAbcMtlGeometryCollection(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_set_geometry()
        self._collectionSetObj = self.CLS_set_collection()
        self._excludeGeometrySetObj = self.CLS_set_geometry()

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

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj,
            self.geometrySet(),
            self.collectionSet(),
            self.excludeGeometrySet()
        ]

    def _xmlAttachValue_(self):
        return self.nameString()

    def _xmlAttaches_(self):
        return [
            (self._xmlAttachKey_(), self._xmlAttachValue_())
        ]


class Abc_MtlAssign(Def_MtlXml):
    CLS_mtl_name = None
    CLS_set_geometry = None

    DEF_geometry_separator = None

    def _initAbcMtlAssign(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_set_geometry()
        self._collectionObj = None

        self._lookObj = None

        self._initDefMtlXml()

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

    def _queryKeyString_(self):
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

    def _xmlAttachValue_(self):
        self.nameString()

    def _xmlAttributes_(self):
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

    def _xmlAttributes_(self):
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

    OBJ_mtl_def_cache = None

    def _initAbcMtlVisibilityAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._typeObj = None

        self._visibilityValueObj = None
        self._defVisibilityValueObj = None

        self._viewerGeometrySetObj = self.CLS_set_geometry_viewer()

    def setTypeString(self, portnameString):
        self._typeObj = self.CLS_mtl_type(portnameString)

        portDef = self.OBJ_mtl_def_cache.getObjectPortDef(self.DEF_mtl_category_geometry, portnameString)
        portdataString = portDef[self.DEF_mtl_key_portdata]

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

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.type(),
            self.visible(),
            self.geometrySet(),
            self.viewerGeometrySet(),
            self.collection()
        ]


class Abc_MtlLook(Def_MtlXml):
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

        self._initDefMtlXml()

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

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj
        ]

    def _xmlChildren_(self):
        return self.assigns()

    def _xmlElements_(self):
        return self._givens()


class Abc_MtlFileReference(Def_MtlXml):
    CLS_mtl_file = None

    def _initAbcMtlFileReference(self, *args):
        self._fileObj = self.CLS_mtl_file(*args)

        self._initDefMtlXml()

    def _fileObject(self):
        return self._fileObj

    def file(self):
        return self._fileObject()

    def filenameString(self):
        return self._fileObject().toString()

    def _queryKeyString_(self):
        return self.filenameString()

    def _xmlAttributes_(self):
        return [
            self.file()
        ]


class Abc_MtlFile(Def_MtlXml):
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

        self._initDefMtlXml()

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

    def _xmlAttributes_(self):
        return [
            self.version()
        ]

    def _xmlChildren_(self):
        return self.looks()


class Abc_MtlTrsBasic(mtlConfigure.Utility):
    def _initAbcMtlTrsBasic(self):
        pass


# translate node def
class Abc_MtlTrsObject(Abc_MtlTrsBasic):
    CLS_mtl_object = None
    CLS_mtl_dcc_object = None

    OBJ_mtl_def_cache = None
    OBJ_mtl_dcc_def_cache = None

    def _initAbcMtlTrsObject(self, *args):
        dccNodeString = args[0]

        self._dccNodeString = dccNodeString
        self._dccObjectObj = self.CLS_mtl_dcc_object(self._dccNodeString)
        self._dccCategoryString = self._dccObjectObj.category()

        self._categoryString = self.OBJ_mtl_dcc_def_cache.getDccObjectCategoryString(self._dccCategoryString)
        self._nodeString = self._dccObjectObj.fullpathName().replace(self.DEF_mya_node_separator, self.DEF_mtl_node_separator)

        self._getObject_()

    def _getObject_(self):
        self._objectObj = self.CLS_mtl_object(
            self._categoryString,
            self._nodeString
        )

    def _getPorts_(self):
        def getPortFnc_(_dccPortnameString, dccPortDatum_):
            _dccPort = self._dccObjectObj.attribute(_dccPortnameString)

            _portnameString = dccPortDatum_[self.DEF_mtl_key_portname]
            _port = self._objectObj.attribute(_portnameString)

            if _dccPort.hasSource():
                _dccSource = _dccPort.source()
                _dccSourceNode = _dccSource.node()

                _dccSourceNodeString = _dccSourceNode.fullpathName()
                _dccSourceCategoryString = _dccSourceNode.category()
                _dccSourcePortnameString = _dccSource.fullpathPortname()

                _sourceCategoryString = self.OBJ_mtl_dcc_def_cache.getDccObjectCategoryString(_dccSourceCategoryString)
                _sourcePortnameString = self.OBJ_mtl_dcc_def_cache.getDccObjectPortnameString(_dccSourceCategoryString, _dccSourcePortnameString)

                _sourceNodeCls = self._objectObj.CLS_mtl_source_object
                if _sourceNodeCls is None:
                    _sourceNodeCls = self._objectObj.__class__

                _sourceNode = _sourceNodeCls(_sourceCategoryString, _dccSourceNodeString)
                _source = _sourceNode.output(_sourcePortnameString)

                _port.connectFrom(_source)
            else:
                _port.setRaw(_dccPort.portdata())

        portDefsDict = self.OBJ_mtl_dcc_def_cache.getDccObjectPortDefs(self._dccCategoryString)
        for dccPortnameString, dccPortDatum in portDefsDict.items():
            getPortFnc_(dccPortnameString, dccPortDatum)

    def _getPort_(self, dccPortnameString, dccPortDef):
        pass

    def dccObject(self):
        return self._dccObjectObj

    # materialx
    def mtlObject(self):
        return self._objectObj

    def categoryString(self):
        return self._objectObj.categoryString()

    def __str__(self):
        return self._objectObj.__str__()


# translate node
class Abc_MtlTrsNode(Abc_MtlTrsObject):
    def _initAbcMtlTrsNode(self, *args):
        self._initAbcMtlTrsObject(*args)

        self._getPorts_()


# translate shader
class Abc_MtlTrsShader(Abc_MtlTrsObject):
    CLS_mtl_trs_node_graph = None

    def _initAbcMtlTrsShader(self, *args):
        self._initAbcMtlTrsObject(*args)

        self._getMtlShaderPorts_()

    def _getMtlNode_(self, dccCategoryString, dccNodeString):
        categoryString = self.OBJ_mtl_dcc_def_cache.getDccObjectCategoryString(dccCategoryString)
        nodeString = dccNodeString

        nodeCls = self._objectObj.CLS_mtl_source_object
        if nodeCls is None:
            nodeCls = self._objectObj.__class__

        return nodeCls(categoryString, nodeString)

    def _getMtlShaderPorts_(self):
        def getPortFnc_(_dccPortnameString, dccPortDatum_):
            _dccPort = self._dccObjectObj.attribute(_dccPortnameString)

            _portnameString = dccPortDatum_[self.DEF_mtl_key_portname]
            _port = self._objectObj.attribute(_portnameString)

            if _dccPort.hasSource():
                _dccSource = _dccPort.source()
                _dccSourceNode = _dccSource.node()

                _dccSourceNodeString = _dccSourceNode.fullpathName()
                _dccSourceCategoryString = _dccSourceNode.category()
                _dccSourcePortnameString = _dccSource.fullpathPortname()

                _sourceCategoryString = self.OBJ_mtl_dcc_def_cache.getDccObjectCategoryString(_dccSourceCategoryString)
                _sourcePortnameString = self.OBJ_mtl_dcc_def_cache.getDccObjectPortnameString(_dccSourceCategoryString, _dccSourcePortnameString)

                _sourceNodeCls = self._objectObj.CLS_mtl_source_object
                if _sourceNodeCls is None:
                    _sourceNodeCls = self._objectObj.__class__

                _sourceNode = _sourceNodeCls(_sourceCategoryString, _dccSourceNodeString)
                _source = _sourceNode.output(_sourcePortnameString)

                _port.connectFrom(_source)
            else:
                _port.setRaw(_dccPort.portdata())

        trsNodeGraph = self.CLS_mtl_trs_node_graph(self._dccObjectObj)

        portDefsDict = self.OBJ_mtl_dcc_def_cache.getDccObjectPortDefs(self._dccCategoryString)
        for dccPortnameString, dccPortDatum in portDefsDict.items():
            getPortFnc_(dccPortnameString, dccPortDatum)

        self._objectObj._updateNodeGraphs_()
        print self._objectObj.nodeGraph(0)


# translate material
class Abc_MtlTrsMaterial(Abc_MtlTrsObject):
    def _initAbcMtlTrsMaterial(self, *args):
        self._initAbcMtlTrsObject(*args)

    def _getObject_(self):
        self._objectObj = self.CLS_mtl_object(
            self.dccObject().fullpathName()
        )

    def _getMaterialPorts_(self):
        pass


# translate geometry
class Abc_MtlTrsGeometry(Abc_MtlTrsObject):
    def _initAbcMtlTrsGeometry(self, *args):
        self._initAbcMtlTrsObject(*args)

        self._getPorts_()

    def _getObject_(self):
        self._objectObj = self.CLS_mtl_object(
            self._nodeString
        )


# translate node graph
class Abc_MtlTrsNodeGraph(Abc_MtlTrsBasic):
    CLS_mtl_node_graph = None
    CLS_mtl_dcc_node_graph = None

    CLS_mtl_trs_node = None

    def _initAbcMtlTrsNodeGraph(self, *args):
        self._dccNodeObj = args[0]

        self._getNodes_()

    def _getNodes_(self):
        dccNodeGraph = self._dccNodeObj.nodeGraph()
        dccNodes = dccNodeGraph.nodes()
        # print dccNodeGraph.outputs()
        for i in dccNodes:
            _dccCategoryString = i.category()
            _dccNodeString = i.fullpathName()

            _trsNode = self.CLS_mtl_trs_node(_dccNodeString)


class Abc_MtlTrsFile(object):
    pass
