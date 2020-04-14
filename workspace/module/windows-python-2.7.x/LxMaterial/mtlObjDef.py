# coding:utf-8
from LxBasic import bscMethods

from . import mtlCfg


# ******************************************************************************************************************** #
class Def_GrhTrsNodeRaw(mtlCfg.Utility):
    OBJ_grh_query_cache = None
    VAR_mtl_def_key_list = []

    def _initDefGrhTrsNodeRaw(self, dccObjectRaw, dccOutputRaw, dccPortChildRaw):
        self._dccOutRawDict = self.CLS_ordered_dict()

        self._dccObjectRaw = dccObjectRaw
        self._dccOutputRaw = dccOutputRaw
        self._dccPortChildRaw = dccPortChildRaw

        self._translateDccObjectRaw_()

    def _translateDccObjectRaw_(self):
        self._mtlCategoryString = self._dccObjectRaw[self.DEF_mtl_key_mtl_category]

        self._mtlNodeDefObj = self.OBJ_grh_query_cache.nodeDef(self._mtlCategoryString)

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
        _dic[self.DEF_mtl_key_portpath] = mtlPortnameString
        for _k, _v in portDefObject_.portraw.items():
            _dic[_k] = _v
        _assignString = portDefObject_.assign
        self._dccOutRawDict[self.DEF_mtl_key_dcc_port][(dccPortnameString, _assignString)] = _dic

    def dccOutRaw(self):
        return self._dccOutRawDict


class Def_GrhTrsPortQuery(mtlCfg.Utility):
    def _initDefGrhTrsPortQuery(self, dccPortnameString, portRaw):
        self._dccPortname = dccPortnameString
        self._dccPortraw = portRaw
    @property
    def dccPortname(self):
        return self._dccPortname
    @property
    def mtlPortname(self):
        return self._dccPortraw[self.DEF_mtl_key_portpath]
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


class Def_GrhTrsNodeQuery(mtlCfg.Utility):
    CLS_mtl_dcc_port_def = None

    CLS_mtl_dcc_raw_translator = None

    VAR_mtl_def_key_list = []

    def _initDefGrhTrsNodeQuery(self, dccCategoryString, dccObjectRaw, dccOutputRaw, dccPortChildRaw):
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
class Def_GrhTrsObjQueryCache(mtlCfg.Utility):
    VAR_mtl_dcc_node_file = None
    VAR_mtl_dcc_geometry_file = None
    VAR_mtl_dcc_material_file = None
    VAR_mtl_dcc_output_file = None
    VAR_mtl_dcc_port_child_file = None

    VAR_mtl_dcc_custom_category_file = None
    VAR_mtl_dcc_custom_node_file = None

    CLS_mtl_dcc_object_def = None

    OBJ_grh_query_cache = None

    # noinspection PyUnusedLocal
    def _initDefGrhTrsObjQueryCache(self, *args):
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
        if cacheQueryObject._get_obj_exist_(objectKeyString) is True:
            return cacheQueryObject._get_obj_(objectKeyString)
        else:
            cacheObject = objectCls(*clsArgs)
            cacheQueryObject._set_obj_add_(cacheObject)
            return cacheObject
