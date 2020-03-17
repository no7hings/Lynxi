# coding:utf-8
from LxBasic import bscMethods

from LxMaterial import mtlConfigure


# material port def
class Abc_MtlPortDef(mtlConfigure.Utility):
    def _initAbcMtlPortDef(self, portnameString, portRaw):
        self._portname = portnameString
        self._portraw = portRaw
    @property
    def portraw(self):
        return self._portraw
    @property
    def portname(self):
        return self._portname
    @property
    def porttype(self):
        return self._portraw[self.DEF_mtl_key_porttype]
    @property
    def portdata(self):
        return self._portraw[self.DEF_mtl_key_portdata]
    @property
    def assign(self):
        return self._portraw[self.DEF_mtl_key_assign]
    @property
    def parent(self):
        return self._portraw[self.DEF_mtl_key_parent]
    @property
    def children(self):
        return self._portraw[self.DEF_mtl_key_children]


# material object def
class Abc_MtlObjectDef(mtlConfigure.Utility):
    CLS_mtl_port_def = None

    def _initAbcMtlObjectDef(self, categoryString, objectRaw, outputRaw, portChildRaw):
        self._category = categoryString

        self._objectRaw = objectRaw
        self._outputRaw = outputRaw
        self._portChildRaw = portChildRaw

        self._objectDefDict = self.CLS_ordered_dict()

        self._portDefObjDict = self.CLS_ordered_dict()
        self._portDefObjList = []
        self._inputDefObjDict = self.CLS_ordered_dict()
        self._inputDefObjList = []
        self._outputDefObjDict = self.CLS_ordered_dict()
        self._outputDefObjList = []

        self._translateRaw_()
        self._getPortDefs_()

    def _translateRaw_(self):
        def getObjectRawFnc_(objectRaw_):
            _typeString = objectRaw_[self.DEF_mtl_key_type]
            self._objectDefDict[self.DEF_mtl_key_type] = _typeString
            self._objectDefDict[self.DEF_mtl_key_port] = self.CLS_ordered_dict()

            _portsRaw = objectRaw_[self.DEF_mtl_key_port]
            [getPortRawFnc_(i) for i in _portsRaw]
            _outputsRaw = self._outputRaw.get(_typeString, [])
            [getPortRawFnc_(i) for i in _outputsRaw]

        def getPortRawFnc_(portRaw_):
            _portnameString = portRaw_[self.DEF_mtl_key_portname]
            _porttypeString = portRaw_[self.DEF_mtl_key_porttype]
            _portdataString = portRaw_[self.DEF_mtl_key_portdata]
            _assignString = portRaw_[self.DEF_mtl_key_assign]

            _childPortnameStringList = []
            _childPortsRaw = self._portChildRaw.get(_porttypeString, [])
            for seq, _portraw in enumerate(_childPortsRaw):
                _childPortnameString = getChildPortRawFnc_(seq, _portnameString, _portdataString, _assignString, _portraw)
                if _childPortnameString is not None:
                    _childPortnameStringList.append(_childPortnameString)

            addPortFnc_(_portnameString, _porttypeString, _portdataString, _assignString, None, _childPortnameStringList)

        def getChildPortRawFnc_(childIndex_, parentPortnameString_, parentPortdataString_, parentAssignString_, portRaw_):
            _formatString = portRaw_[self.DEF_mtl_key_format]
            _portnameString = _formatString.format(*[parentPortnameString_])
            _porttypeString = portRaw_[self.DEF_mtl_key_porttype]

            if parentPortdataString_:
                _portdataString = parentPortdataString_.split(u',')[childIndex_].rstrip().lstrip()
            else:
                _portdataString = portRaw_[self.DEF_mtl_key_portdata]

            if parentAssignString_ == self.DEF_mtl_keyword_input:
                _portAssignString = self.DEF_mtl_keyword_input_channel
            elif parentAssignString_ == self.DEF_mtl_keyword_output:
                _portAssignString = self.DEF_mtl_keyword_output_channel
            else:
                _portAssignString = None

            if _portAssignString is not None:
                addPortFnc_(_portnameString, _porttypeString, _portdataString, _portAssignString, parentPortnameString_, [])
                return _portnameString

        def addPortFnc_(portnameString_, porttypeString_, valueString_, assignString_, parentPortnameString_, childrenPortnameStrings_):
            _dic = self.CLS_ordered_dict()
            _dic[self.DEF_mtl_key_porttype] = porttypeString_
            _dic[self.DEF_mtl_key_portdata] = valueString_
            _dic[self.DEF_mtl_key_assign] = assignString_
            _dic[self.DEF_mtl_key_parent] = parentPortnameString_
            _dic[self.DEF_mtl_key_children] = childrenPortnameStrings_
            self._objectDefDict[self.DEF_mtl_key_port][portnameString_] = _dic

        getObjectRawFnc_(self._objectRaw)

    def _getPortDefs_(self):
        for k, v in self._objectDefDict[self.DEF_mtl_key_port].items():
            assignString = v[self.DEF_mtl_key_assign]
            portDefObject = self.CLS_mtl_port_def(k, v)
            if assignString in [self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_input_channel]:
                pass
            elif assignString in [self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_output_channel]:
                pass
            self._portDefObjDict[k] = portDefObject
            self._portDefObjList.append(portDefObject)
    @property
    def category(self):
        return self._category
    @property
    def type(self):
        return self._objectDefDict[self.DEF_mtl_key_type]
    @property
    def ports(self):
        return self._portDefObjList

    def port(self, portnameString):
        return self._portDefObjDict[portnameString]
    @property
    def inputs(self):
        return self._inputDefObjList

    def input(self, portnameString):
        return self._inputDefObjDict[portnameString]
    @property
    def outputs(self):
        return self._outputDefObjList

    def output(self, portnameString):
        return self._outputDefObjList[portnameString]


# material query
class Abc_MtlQueryCache(mtlConfigure.Utility):
    VAR_mtl_node_defs_file = None
    VAR_mtl_geometry_def_file = None
    VAR_mtl_material_def_file = None
    VAR_mtl_output_defs_file = None
    VAR_mtl_port_child_defs_file = None

    CLS_mtl_object_def = None

    # noinspection PyUnusedLocal
    def _initAbcMtlQueryCache(self, *args):
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

        self._objectDefObjList = []
        self._nodeDefObjDict = self.CLS_ordered_dict()

        self._initializeCache_()

    def nodeDefs(self):
        return self._objectDefObjList

    def nodeDef(self, categoryString):
        return self._nodeDefObjDict[categoryString]

    def categories(self):
        return self._nodeDefObjDict.keys()

    def _initializeCache_(self):
        def getObjectDefFnc_(objectsRaw_):
            for categoryString, objectRaw in objectsRaw_.items():
                _objectDefObj = self.CLS_mtl_object_def(
                    categoryString,
                    objectRaw,
                    self._outputRaw,
                    self._portChildRaw
                )
                self._objectDefObjList.append(_objectDefObj)
                self._nodeDefObjDict[categoryString] = _objectDefObj

        getObjectDefFnc_(self._nodeRaw)
        getObjectDefFnc_(self._materialRaw)
        getObjectDefFnc_(self._geometryRaw)


# ******************************************************************************************************************** #
class Abc_MtlDccPortDef(mtlConfigure.Utility):
    def _initAbcMtlDccPortDef(self, dccPortnameString, portRaw):
        self._dccPortname = dccPortnameString
        self._dccPortraw = portRaw
    @property
    def dccPortname(self):
        return self._dccPortname
    @property
    def portname(self):
        return self._dccPortraw[self.DEF_mtl_key_portname]
    @property
    def porttype(self):
        return self._dccPortraw[self.DEF_mtl_key_porttype]
    @property
    def portdata(self):
        return self._dccPortraw[self.DEF_mtl_key_portdata]
    @property
    def assign(self):
        return self._dccPortraw[self.DEF_mtl_key_assign]
    @property
    def parent(self):
        return self._dccPortraw[self.DEF_mtl_key_parent]
    @property
    def children(self):
        return self._dccPortraw[self.DEF_mtl_key_children]


class Abc_MtlDccObjectDef(mtlConfigure.Utility):
    CLS_mtl_dcc_port_def = None

    OBJ_mtl_query_cache = None

    def _initAbcMtlDccObjectDef(self, dccCategoryString, dccObjectRaw, dccOutputRaw, dccPortChildRaw):
        self._dccCategoryString = dccCategoryString
        self._dccObjectRaw = dccObjectRaw
        self._dccOutputRaw = dccOutputRaw
        self._dccPortChildRaw = dccPortChildRaw

        self._dccNodeDefDict = self.CLS_ordered_dict()

        self._dccPortDefObjDict = self.CLS_ordered_dict()
        self._dccPortDefObjList = []
        self._dccInputDefObjDict = self.CLS_ordered_dict()
        self._dccInputDefObjList = []
        self._dccOutputDefObjDict = self.CLS_ordered_dict()
        self._dccOutputDefObjList = []

        self._translateDccRaw_()
        self._getDccPorts_()

    def _translateDccRaw_(self):
        def getDccObjectRawFnc_(dccObjectRaw_):
            _categoryString = dccObjectRaw_[self.DEF_mtl_key_target_category]

            _nodeDefObject = self.OBJ_mtl_query_cache.nodeDef(_categoryString)
            _typeString = _nodeDefObject.type
            self._dccNodeDefDict[self.DEF_mtl_key_category] = _categoryString
            self._dccNodeDefDict[self.DEF_mtl_key_type] = _typeString
            self._dccNodeDefDict[self.DEF_mtl_key_target_port] = self.CLS_ordered_dict()
            if self.DEF_mtl_key_after_expression in dccObjectRaw_:
                self._dccNodeDefDict[self.DEF_mtl_key_after_expression] = dccObjectRaw_[self.DEF_mtl_key_after_expression]

            _dccPortsRaw = dccObjectRaw_[self.DEF_mtl_key_target_port]
            getDccPortsRawFnc_(_dccPortsRaw, _nodeDefObject)
            _dccOutputsRaw = self._dccOutputRaw.get(_typeString, {})
            getDccPortsRawFnc_(_dccOutputsRaw, _nodeDefObject)

        def getDccPortsRawFnc_(dccPortsRaw_, objectDefObject_):
            for dccPortnameString, _dccPortRaw in dccPortsRaw_.items():
                _portnameString = _dccPortRaw[self.DEF_mtl_key_target_portname]
                if isinstance(_portnameString, (tuple, list)):
                    for _portnameString in _portnameString:
                        getDccPortRawFnc_(dccPortnameString, _portnameString, objectDefObject_)
                else:
                    getDccPortRawFnc_(dccPortnameString, _portnameString, objectDefObject_)

        def getDccPortRawFnc_(dccPortnameString_, portnameString_, objectDefObject_):
            _portDefObject = objectDefObject_.port(portnameString_)
            _porttypeString = _portDefObject.porttype
            _portdataString = _portDefObject.portdata
            _assignString = _portDefObject.assign

            _dccChildPortsRaw = self._dccPortChildRaw.get(_porttypeString, [])
            for _dccPortDef in _dccChildPortsRaw:
                getDccChildPortRawFnc_(dccPortnameString_, portnameString_, _dccPortDef, objectDefObject_)

            addDccPortFnc_(dccPortnameString_, portnameString_, _portDefObject)

        def getDccChildPortRawFnc_(dccParentPortnameString_, parentPortnameString_, dccPortRaw_, objectDefObject_):
            _dccFormatString = dccPortRaw_[self.DEF_mtl_key_format]
            _formatString = dccPortRaw_[self.DEF_mtl_key_target_portname][self.DEF_mtl_key_format]
            _dccPortnameString = _dccFormatString.format(*[dccParentPortnameString_])
            _portnameString = _formatString.format(*[parentPortnameString_])

            _portDefObject = objectDefObject_.port(_portnameString)
            _porttypeString = _portDefObject.porttype
            _portdataString = _portDefObject.portdata
            _assignString = _portDefObject.assign

            addDccPortFnc_(_dccPortnameString, _portnameString, _portDefObject)

        def addDccPortFnc_(dccPortnameString_, portnameString_, portDefObject_):
            _dic = self.CLS_ordered_dict()
            _dic[self.DEF_mtl_key_portname] = portnameString_
            for _k, _v in portDefObject_.portraw.items():
                _dic[_k] = _v
            _assignString = portDefObject_.assign
            self._dccNodeDefDict[self.DEF_mtl_key_target_port][(dccPortnameString_, _assignString)] = _dic

        getDccObjectRawFnc_(self._dccObjectRaw)

    def _getDccPorts_(self):
        for k, v in self._dccNodeDefDict[self.DEF_mtl_key_target_port].items():
            dccPortnameString, assignString = k
            portDefObject = self.CLS_mtl_dcc_port_def(dccPortnameString, v)
            if assignString in [self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_input_channel]:
                self._dccInputDefObjDict[dccPortnameString] = portDefObject
                self._dccInputDefObjList.append(portDefObject)
            elif assignString in [self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_output_channel]:
                self._dccOutputDefObjDict[dccPortnameString] = portDefObject
                self._dccOutputDefObjList.append(portDefObject)
            self._dccPortDefObjDict[dccPortnameString] = portDefObject
            self._dccPortDefObjList.append(portDefObject)
    @property
    def dccCategory(self):
        return self._dccCategoryString
    @property
    def category(self):
        return self._dccNodeDefDict[self.DEF_mtl_key_category]
    @property
    def type(self):
        return self._dccNodeDefDict[self.DEF_mtl_key_type]
    @property
    def dccPorts(self):
        return self._dccPortDefObjList

    def dccPort(self, dccPortnameString):
        assert dccPortnameString in self._dccPortDefObjDict, u'''"{}"'s DCC Port "{}" is Unregistered'''.format(
            self.dccCategory,
            dccPortnameString
        )
        return self._dccPortDefObjDict[dccPortnameString]
    @property
    def dccInputs(self):
        return self._dccInputDefObjList

    def dccInput(self, dccPortnameString):
        return self._dccInputDefObjDict[dccPortnameString]
    @property
    def dccOutputs(self):
        return self._dccOutputDefObjList

    def dccOutput(self, dccPortnameString):
        return self._dccOutputDefObjDict[dccPortnameString]
    @property
    def afterExpression(self):
        return self._dccNodeDefDict.get(
            self.DEF_mtl_key_after_expression
        )


# material dcc Query
class Abc_MtlDccQueryCache(mtlConfigure.Utility):
    VAR_mtl_dcc_node_defs_file = None
    VAR_mtl_dcc_geometry_def_file = None
    VAR_mtl_dcc_material_def_file = None
    VAR_mtl_dcc_custom_def_file = None
    VAR_mtl_dcc_output_defs_file = None
    VAR_mtl_dcc_port_child_defs_file = None

    CLS_mtl_dcc_object_def = None

    OBJ_mtl_query_cache = None

    # noinspection PyUnusedLocal
    def _initAbcMtlDccQueryCache(self, *args):
        self._dccObjectRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_node_defs_file
        ) or {}
        self._dccGeometryRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_geometry_def_file
        ) or {}
        self._dccMaterialRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_material_def_file
        ) or {}
        self._dccCustomRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_custom_def_file
        ) or {}
        self._dccOutputRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_output_defs_file
        ) or {}
        self._dccPortChildRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_port_child_defs_file
        ) or {}

        self._initializeDccCache_()

    def dccNodeDefs(self):
        return self._dccObjectDefObjList

    def dccNodeDef(self, dccCategoryString):
        assert dccCategoryString in self._dccObjectDefObjDict, u'''DCC Category "{}" is Unregistered!!!'''.format(dccCategoryString)
        return self._dccObjectDefObjDict[dccCategoryString]

    def dccCategories(self):
        return self._dccObjectDefObjDict.keys()

    def hasDccCategory(self, dccCategoryString):
        return dccCategoryString in self._dccObjectDefObjDict

    def _initializeDccCache_(self):
        def getDccObjectDefFnc_(objectsRaw_):
            for _dccCategoryString, _dccObjectRaw in objectsRaw_.items():
                _dccObjectDefObj = self.CLS_mtl_dcc_object_def(
                    _dccCategoryString,
                    _dccObjectRaw,
                    self._dccOutputRaw,
                    self._dccPortChildRaw
                )
                self._dccObjectDefObjList.append(_dccObjectDefObj)
                self._dccObjectDefObjDict[_dccCategoryString] = _dccObjectDefObj

        self._dccObjectRawDict = self.CLS_ordered_dict()

        self._dccObjectDefObjList = []
        self._dccObjectDefObjDict = self.CLS_ordered_dict()

        getDccObjectDefFnc_(self._dccObjectRaw)
        getDccObjectDefFnc_(self._dccMaterialRaw)
        getDccObjectDefFnc_(self._dccGeometryRaw)
        getDccObjectDefFnc_(self._dccCustomRaw)


# ******************************************************************************************************************** #
class Def_MtlObjCache(object):
    def _initDefMtlObjCache(self, objectName):
        self._mtlObjectNameString = objectName

    @classmethod
    def _toMtlObjKeyString_(cls, objectName):
        return '{}({})'.format(
            cls.__name__, objectName
        )

    def _mtlObjKeyString_(self):
        return self._toMtlObjKeyString_(
            self._mtlObjectNameString
        )

    def _mtlObjectNameString_(self):
        return self._mtlObjectNameString


class Abc_MtlObjCache(mtlConfigure.Utility):
    DEF_mtl_key_index = u'index'

    def _initAbcMtlObjCache(self):
        self._objectFilterDict = {}
        self._objectList = []

        self._objectCount = 0

    def _initializeCache_(self):
        self._objectFilterDict = {}
        self._objectList = []

        self._objectCount = 0

    def _addObject_(self, *args):
        if len(args) == 2:
            key, obj = args
        else:
            obj = args[0]
            key = obj._mtlObjKeyString_()

        index = self._objectCount
        if key not in self._objectFilterDict:
            self._objectFilterDict[key] = {}
            if obj not in self._objectList:
                self._objectList.append(obj)
            self._objectFilterDict[key][self.DEF_mtl_key_index] = index
            self._objectCount += 1

    def _hasObject_(self, *args):
        if isinstance(args[0], (str, unicode)):
            key = args[0]
            return key in self._objectFilterDict
        elif isinstance(args[0], int):
            index = args[0]
            return 0 <= index <= (self._objectCount - 1)
        elif isinstance(args[0], Def_MtlObjCache):
            obj = args[0]
            key = obj._mtlObjKeyString_()
            return key in self._objectFilterDict

    def _object_(self, *args):
        if isinstance(args[0], (str, unicode)):
            key = args[0]
            index = self._objectFilterDict[key][self.DEF_mtl_key_index]
            return self._objectList[index]
        elif isinstance(args[0], int):
            index = args[0]
            return self._objectList[index]

    def _index_(self, *args):
        if isinstance(args[0], (str, unicode)):
            key = args[0]
            return self._objectFilterDict[key][self.DEF_mtl_key_index]
        elif isinstance(args[0], Def_MtlObjCache):
            cacheObject = args[0]
            return self._objectList.index(cacheObject)

    def _updateObject_(self, obj):
        if self._hasObject_(obj) is False:
            self._addObject_(obj)

    def addObject(self, obj):
        key = obj._mtlObjKeyString_()
        assert key not in self._objectFilterDict, u'''"{}" is Registered.'''.format(key)
        self._addObject_(obj)

    def objectCount(self):
        """
        :return: int
        """
        return self._objectCount

    def hasObjects(self):
        return self._objectList != []

    def hasObject(self, key):
        return self._hasObject_(key)

    def objects(self):
        return self._objectList

    def object(self, key):
        assert key in self._objectFilterDict, u'''"{}" is Unregistered.'''.format(key)
        return self._object_(key)

    def objectNames(self):
        return [i._mtlObjKeyString_() for i in self._objectList]
