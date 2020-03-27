# coding:utf-8
from LxBasic import bscMethods

from LxMaterial import mtlConfigure


class Abc_MtlRawTranslator(mtlConfigure.Utility):
    def _initAbcMtlRawTranslator(self, objectRaw, outputRaw, portChildRaw):
        self._objectRaw = objectRaw
        self._outputRaw = outputRaw
        self._portChildRaw = portChildRaw

        self._outRawDict = self.CLS_ordered_dict()

        self._translateObjectRaw_(self._objectRaw)

    def _translateObjectRaw_(self, objectRaw_):
        _typeString = objectRaw_[self.DEF_mtl_key_type]
        self._outRawDict[self.DEF_mtl_key_type] = _typeString
        self._outRawDict[self.DEF_mtl_key_port] = self.CLS_ordered_dict()

        _portsRaw = objectRaw_[self.DEF_mtl_key_port]
        self._translateDccPortsRaw_(_portsRaw)
        _outputsRaw = self._outputRaw.get(_typeString, [])
        self._translateDccPortsRaw_(_outputsRaw)

    def _translateDccPortsRaw_(self, portRaws):
        for i in portRaws:
            self._translatePortRaw_(i)

    def _translatePortRaw_(self, portRaw):
        _portnameString = portRaw[self.DEF_mtl_key_portname]
        _porttypeString = portRaw[self.DEF_mtl_key_porttype]
        _portdataString = portRaw[self.DEF_mtl_key_portdata]
        _assignString = portRaw[self.DEF_mtl_key_assign]

        _childPortpathStrList = []
        _childPortsRaw = self._portChildRaw.get(_porttypeString, [])
        for seq, _portraw in enumerate(_childPortsRaw):
            _childPortnameString = self._translateChildPortRaw_(seq, _portnameString, _porttypeString, _portdataString, _assignString, _portraw)
            if _childPortnameString is not None:
                _childPortpathStrList.append(_childPortnameString)

        self._addPortRaw_(_portnameString, _porttypeString, _portdataString, _assignString, None, _childPortpathStrList)

    def _translateChildPortRaw_(self, childIndex_, parentPortnameString_, parentPorttypeString_, parentPortdataString_, parentAssignString_, portRaw):
        _formatString = portRaw[self.DEF_mtl_key_format]

        _portnameString = _formatString.format(*[parentPortnameString_])
        _porttypeString = portRaw[self.DEF_mtl_key_porttype]

        if parentPortdataString_:
            _portdataString = parentPortdataString_.split(u',')[childIndex_].rstrip().lstrip()
        else:
            _portdataString = portRaw[self.DEF_mtl_key_portdata]

        if parentAssignString_ == self.DEF_mtl_keyword_input:
            _portAssignString = self.DEF_mtl_keyword_input_channel
        elif parentAssignString_ == self.DEF_mtl_keyword_output:
            _portAssignString = self.DEF_mtl_keyword_output_channel
        else:
            _portAssignString = None

        if _portAssignString is not None:
            self._addPortRaw_(_portnameString, parentPorttypeString_, _portdataString, _portAssignString, parentPortnameString_, [])
            return _portnameString

    def _addPortRaw_(self, portnameString_, porttypeString_, valueString_, assignString_, parentPortnameString_, childrenPortnameStrings_):
        _dic = self.CLS_ordered_dict()
        _dic[self.DEF_mtl_key_porttype] = porttypeString_
        _dic[self.DEF_mtl_key_portdata] = valueString_
        _dic[self.DEF_mtl_key_assign] = assignString_
        _dic[self.DEF_mtl_key_parent] = parentPortnameString_
        _dic[self.DEF_mtl_key_children] = childrenPortnameStrings_
        self._outRawDict[self.DEF_mtl_key_port][portnameString_] = _dic

    def outRaw(self):
        return self._outRawDict


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

    CLS_mtl_raw_translator = None

    def _initAbcMtlObjectDef(self, categoryString, objectRaw, outputRaw, portChildRaw):
        self._category = categoryString

        self._objectRaw = objectRaw
        self._outputRaw = outputRaw
        self._portChildRaw = portChildRaw

        self._objectDefDict = self.CLS_mtl_raw_translator(
            objectRaw,
            outputRaw,
            portChildRaw
        ).outRaw()

        self._portDefObjDict = self.CLS_ordered_dict()
        self._portDefObjList = []
        self._inputDefObjDict = self.CLS_ordered_dict()
        self._inputDefObjList = []
        self._outputDefObjDict = self.CLS_ordered_dict()
        self._outputDefObjList = []

        self._getPortDefs_()

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
class Abc_MtlDccRawTranslator(mtlConfigure.Utility):
    OBJ_mtl_query_cache = None
    VAR_mtl_def_key_list = []

    def _initMtlDccRawTranslator(self, dccObjectRaw, dccOutputRaw, dccPortChildRaw):
        self._dccOutRawDict = self.CLS_ordered_dict()

        self._dccObjectRaw = dccObjectRaw
        self._dccOutputRaw = dccOutputRaw
        self._dccPortChildRaw = dccPortChildRaw

        self._translateDccObjectRaw_()

    def _translateDccObjectRaw_(self):
        self._mtlCategoryString = self._dccObjectRaw[self.DEF_mtl_key_mtl_category]

        self._mtlNodeDefObj = self.OBJ_mtl_query_cache.nodeDef(self._mtlCategoryString)

        self._typeString = self._mtlNodeDefObj.type
        self._dccOutRawDict[self.DEF_mtl_key_category] = self._mtlCategoryString
        self._dccOutRawDict[self.DEF_mtl_key_type] = self._typeString
        self._dccOutRawDict[self.DEF_mtl_key_dcc_port] = self.CLS_ordered_dict()

        for _key in self.VAR_mtl_def_key_list:
            if _key in self._dccObjectRaw:
                self._dccOutRawDict[_key] = self._dccObjectRaw[_key]

        dccPortsRaw = self._dccObjectRaw[self.DEF_mtl_key_dcc_port]
        self._translateDccPortsRaw_(dccPortsRaw)

        dccOutputsRaw = self._dccOutputRaw.get(self._typeString, {})
        self._translateDccPortsRaw_(dccOutputsRaw)

    def _translateDccPortsRaw_(self, dccPortsRaw):
        for dccPortnameString, dccPortRaw in dccPortsRaw.items():
            if self.DEF_mtl_key_mtl_portname in dccPortRaw:
                mtlPortnameString = dccPortRaw[self.DEF_mtl_key_mtl_portname]

                if isinstance(mtlPortnameString, (str, unicode)):
                    self._translateDccPortRaw_(dccPortnameString, mtlPortnameString, dccPortRaw)

                elif isinstance(mtlPortnameString, (tuple, list)):
                    for mtlPortnameString_ in mtlPortnameString:
                        self._translateDccPortRaw_(dccPortnameString, mtlPortnameString_, dccPortRaw)

    def _translateDccPortRaw_(self, dccPortnameString, mtlPortnameString, dccPortRaw_):
        mtlPortDefObject = self._mtlNodeDefObj.port(mtlPortnameString)

        if self.DEF_mtl_key_dcc_porttype in dccPortRaw_:
            mtlPorttypeString = dccPortRaw_[self.DEF_mtl_key_dcc_porttype]
        else:
            mtlPorttypeString = mtlPortDefObject.porttype

        mtlAssignString = mtlPortDefObject.assign

        if mtlAssignString not in [self.DEF_mtl_keyword_input_channel, self.DEF_mtl_keyword_output_channel]:
            dccChildPortsRaw = self._dccPortChildRaw.get(mtlPorttypeString, [])
            for _dccPortDef in dccChildPortsRaw:
                self._translateDccChildPortRaw_(dccPortnameString, mtlPortnameString, mtlPorttypeString, _dccPortDef)

            self._addDccPortRaw_(dccPortnameString, mtlPortnameString, mtlPortDefObject)

    def _translateDccChildPortRaw_(self, dccParentPortnameString, parentPortnameString, mtlPorttypeString, dccPortRaw_):
        _dccFormatString = dccPortRaw_[self.DEF_mtl_key_format]
        _formatString = dccPortRaw_[self.DEF_mtl_key_mtl_portname][self.DEF_mtl_key_format]
        if mtlPorttypeString == self.DEF_mtl_keyword_porttype_uv_1:
            _dccPortnameString = _dccFormatString.format(*[dccParentPortnameString, dccParentPortnameString[:-2]])
        else:
            _dccPortnameString = _dccFormatString.format(*[dccParentPortnameString])

        _portnameString = _formatString.format(*[parentPortnameString])

        mtlPortDefObject = self._mtlNodeDefObj.port(_portnameString)

        self._addDccPortRaw_(_dccPortnameString, _portnameString, mtlPortDefObject)

    def _addDccPortRaw_(self, dccPortnameString, mtlPortnameString, portDefObject_):
        _dic = self.CLS_ordered_dict()
        _dic[self.DEF_mtl_key_portname] = mtlPortnameString
        for _k, _v in portDefObject_.portraw.items():
            _dic[_k] = _v
        _assignString = portDefObject_.assign
        self._dccOutRawDict[self.DEF_mtl_key_dcc_port][(dccPortnameString, _assignString)] = _dic

    def dccOutRaw(self):
        return self._dccOutRawDict


class Abc_MtlDccPortDef(mtlConfigure.Utility):
    def _initAbcMtlDccPortDef(self, dccPortnameString, portRaw):
        self._dccPortname = dccPortnameString
        self._dccPortraw = portRaw
    @property
    def dccPortname(self):
        return self._dccPortname
    @property
    def mtlPortname(self):
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

    CLS_mtl_dcc_raw_translator = None

    VAR_mtl_def_key_list = []

    def _initAbcMtlDccObjectDef(self, dccCategoryString, dccObjectRaw, dccOutputRaw, dccPortChildRaw):
        self._dccCategoryString = dccCategoryString

        self._dccNodeDefDict = self.CLS_mtl_dcc_raw_translator(
            dccObjectRaw,
            dccOutputRaw,
            dccPortChildRaw
        ).dccOutRaw()

        self._dccPortDefObjDict = self.CLS_ordered_dict()
        self._dccPortDefObjList = []
        self._dccInputDefObjDict = self.CLS_ordered_dict()
        self._dccInputDefObjList = []
        self._dccOutputDefObjDict = self.CLS_ordered_dict()
        self._dccOutputDefObjList = []

        self._getDccPortDefs_()

    def _getDccPortDefs_(self):
        for k, v in self._dccNodeDefDict[self.DEF_mtl_key_dcc_port].items():
            dccPortnameString, mtlAssignString = k
            portDefObject = self.CLS_mtl_dcc_port_def(dccPortnameString, v)
            if mtlAssignString in [self.DEF_mtl_keyword_input, self.DEF_mtl_keyword_input_channel, self.DEF_mtl_keyword_property, self.DEF_mtl_keyword_visibility]:
                self._dccInputDefObjDict[dccPortnameString] = portDefObject
                self._dccInputDefObjList.append(portDefObject)
            elif mtlAssignString in [self.DEF_mtl_keyword_output, self.DEF_mtl_keyword_output_channel]:
                self._dccOutputDefObjDict[dccPortnameString] = portDefObject
                self._dccOutputDefObjList.append(portDefObject)
            self._dccPortDefObjDict[dccPortnameString] = portDefObject
            self._dccPortDefObjList.append(portDefObject)
    @property
    def dccCategory(self):
        return self._dccCategoryString
    @property
    def mtlCategory(self):
        return self._dccNodeDefDict[self.DEF_mtl_key_category]
    @property
    def type(self):
        return self._dccNodeDefDict[self.DEF_mtl_key_type]
    @property
    def dccPorts(self):
        return self._dccPortDefObjList

    def dccPort(self, dccPortnameString):
        assert dccPortnameString in self._dccPortDefObjDict, u'''DCC Port "{}.{}" is Unregistered'''.format(
            self._dccCategoryString,
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

    def hasDccOutput(self, dccPortnameString):
        return dccPortnameString in self._dccOutputDefObjDict

    def dccOutput(self, dccPortnameString):
        return self._dccOutputDefObjDict[dccPortnameString]
    @property
    def mtlPortRaw(self):
        return self._dccNodeDefDict.get(
            self.DEF_mtl_key_mtl_port,
            {}
        )
    @property
    def mtlPortdataRaw(self):
        return self._dccNodeDefDict.get(
            self.DEF_mtl_key_mtl_portdata,
            {}
        )
    @property
    def customNode(self):
        return self._dccNodeDefDict.get(
            self.DEF_mtl_key_custom_node,
            {}
        )
    @property
    def createExpressionRaw(self):
        return self._dccNodeDefDict.get(
            self.DEF_mtl_key_create_expression,
            {}
        )
    @property
    def afterExpressionRaw(self):
        return self._dccNodeDefDict.get(
            self.DEF_mtl_key_after_expression,
            {}
        )


# material dcc Query
class Abc_MtlDccQueryCache(mtlConfigure.Utility):
    VAR_mtl_dcc_node_file = None
    VAR_mtl_dcc_geometry_file = None
    VAR_mtl_dcc_material_file = None
    VAR_mtl_dcc_output_file = None
    VAR_mtl_dcc_port_child_file = None

    VAR_mtl_dcc_custom_category_file = None
    VAR_mtl_dcc_custom_node_file = None

    CLS_mtl_dcc_object_def = None

    OBJ_mtl_query_cache = None

    # noinspection PyUnusedLocal
    def _initAbcMtlDccQueryCache(self, *args):
        self._dccObjectRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_node_file
        ) or {}
        self._dccGeometryRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_geometry_file
        ) or {}
        self._dccMaterialRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_material_file
        ) or {}
        self._dccOutputRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_output_file
        ) or {}
        self._dccPortChildRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_port_child_file
        ) or {}

        self._dccCustomCategoryRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_custom_category_file
        ) or {}
        self._dccCustomNodeRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_dcc_custom_node_file
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
        getDccObjectDefFnc_(self._dccCustomNodeRaw)


# ******************************************************************************************************************** #
class Def_XmlCacheObj(object):
    def _initDefMtlCacheObj(self, objectName):
        self._mtlObjectNameString = objectName

    def _mtlCacheObjKeyString_(self):
        return self._mtlObjectNameString

    @classmethod
    def _mtd_cache_(cls, cacheQueryObject, objectKeyString, objectCls, clsArgs):
        if cacheQueryObject._get_has_obj_(objectKeyString) is True:
            return cacheQueryObject._get_object_(objectKeyString)
        else:
            cacheObject = objectCls(*clsArgs)
            cacheQueryObject._set_add_obj_(cacheObject)
            return cacheObject


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

    def _set_add_obj_(self, *args):
        if len(args) == 2:
            objKeyString, obj = args
        else:
            obj = args[0]
            objKeyString = obj._mtlCacheObjKeyString_()

        index = self._objectCount
        if objKeyString not in self._objectFilterDict:
            self._objectFilterDict[objKeyString] = {}
            if obj not in self._objectList:
                self._objectList.append(obj)
            self._objectFilterDict[objKeyString][self.DEF_mtl_key_index] = index
            self._objectCount += 1

    def _get_has_obj_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objKeyString = args[0]
            return objKeyString in self._objectFilterDict
        elif isinstance(args[0], int):
            index = args[0]
            return 0 <= index <= (self._objectCount - 1)
        elif isinstance(args[0], Def_XmlCacheObj):
            obj = args[0]
            objKeyString = obj._mtlCacheObjKeyString_()
            return objKeyString in self._objectFilterDict

    def _get_object_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objKeyString = args[0]
            index = self._objectFilterDict[objKeyString][self.DEF_mtl_key_index]
            return self._objectList[index]
        elif isinstance(args[0], (int, float)):
            index = args[0]
            return self._objectList[int(index)]

    def _get_index_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objKeyString = args[0]
            return self._objectFilterDict[objKeyString][self.DEF_mtl_key_index]
        elif isinstance(args[0], Def_XmlCacheObj):
            obj = args[0]
            objKeyString = obj._mtlCacheObjKeyString_()
            return self._objectFilterDict[objKeyString][self.DEF_mtl_key_index]

    def addObject(self, obj):
        objKeyString = obj._mtlCacheObjKeyString_()
        assert objKeyString not in self._objectFilterDict, u'''"{}" is Registered.'''.format(objKeyString)
        self._set_add_obj_(obj)

    def objectCount(self):
        """
        :return: int
        """
        return self._objectCount

    def hasObjects(self):
        return self._objectList != []

    def hasObject(self, objKeyString):
        return self._get_has_obj_(objKeyString)

    def objects(self):
        return self._objectList

    def object(self, objKeyString):
        assert objKeyString in self._objectFilterDict, u'''"{}" is Unregistered.'''.format(objKeyString)
        return self._get_object_(objKeyString)

    def objectNames(self):
        return [i._mtlCacheObjKeyString_() for i in self._objectList]
