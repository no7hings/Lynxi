# coding:utf-8
from LxBasic import bscMethods

from . import grhCfg


class Def_GrhObjSet(grhCfg.Utility):
    VAR_grh_objectsep = None

    DEF_grh_key_index = u'index'

    # noinspection PyUnusedLocal
    def _initDefGrhObjSet(self, *args):
        if args:
            self._obj = args[0]
        else:
            self._obj = 'unknown'

        self._objectList = []
        self._objectFilterDict = {}

        self._objectCount = 0

    def _initializeData_(self):
        self._objectList = []
        self._objectFilterDict = {}

        self._objectCount = 0

    def _get_object_key_string_(self, obj):
        """
        replace method
        """

    def _get_objs_(self):
        return self._objectList

    def _set_obj_add_(self, *args):
        if len(args) == 2:
            objKeyString, obj = args
        else:
            obj = args[0]
            objKeyString = self._get_object_key_string_(obj)

        if objKeyString not in self._objectFilterDict:
            index = self._objectCount
            self._objectList.append(obj)
            self._objectFilterDict[objKeyString] = {}
            self._objectFilterDict[objKeyString][self.DEF_grh_key_index] = index
            self._objectCount += 1

    def _get_obj_exist_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objKeyString = args[0]
            return objKeyString in self._objectFilterDict
        elif isinstance(args[0], int):
            index = args[0]
            return 0 <= index <= (self._objectCount - 1)
        elif isinstance(args[0], object):
            obj = args[0]
            objKeyString = self._get_object_key_string_(obj)
            return objKeyString in self._objectFilterDict

    def _get_obj_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objKeyString = args[0]
            index = self._objectFilterDict[objKeyString][self.DEF_grh_key_index]
            return self._objectList[index]
        elif isinstance(args[0], (int, float)):
            index = args[0]
            return self._objectList[int(index)]

    def _get_obj_index_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objKeyString = args[0]
            obj = self._objectFilterDict[objKeyString]
            return self._objectList.index(obj)
        elif isinstance(args[0], object):
            obj = args[0]
            return self._objectList.index(obj)

    def _get_string_(self):
        return self.VAR_grh_objectsep.join([i.toString() for i in self.objects()])

    def addObject(self, *args):
        obj = args[0]
        keyString = self._get_object_key_string_(obj)
        assert keyString not in self._objectFilterDict, u'''{}({})'s object "{}" is Exist.'''.format(
            self.__class__.__name__, self._obj, keyString
        )
        self._set_obj_add_(*args)

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
        return self._get_obj_exist_(keyString)

    def object(self, *args):
        """
        :param args:
            1.args[0]
        :return: object
        """
        if args:
            keyString = args[0]
            assert keyString in self._objectFilterDict, u'''{}(object={})'s key "{}" is Unregistered.'''.format(
                self.__class__.__name__, self._obj, keyString
            )
            return self._get_obj_(keyString)

        raise ValueError(
            u'class "{}" {}.object(*args)" argument must not empty'.format(
                self._obj.__class__.__name__,
                self.__class__.__name__
            )
        )

    def index(self, *args):
        return self._get_obj_index_(*args)

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
        return self._get_obj_(index)

    def hasObjectAt(self, index):
        """
        :param index: int
        :return: object
        """
        return self._get_obj_exist_(index)

    def toString(self):
        """
        :return: str
        """
        return self._get_string_()

    def __len__(self):
        """
        :return: int
        """
        return self.objectCount()


# object query cache ************************************************************************************************* #
class Def_GrhNodeRaw(grhCfg.Utility):
    def _initDefGrhNodeRaw(self, *args):
        self._categoryString, self._nodeRaw, self._outputRaw, self._portChildRaw = args

        self._outRaw = self.CLS_ordered_dict()

        self._set_node_raw_build_(self._nodeRaw)

    def _set_node_raw_build_(self, nodeRaw):
        _typeString = nodeRaw[self.DEF_grh_key_type]
        # property
        self._outRaw[self.DEF_grh_key_type] = _typeString
        self._outRaw[self.DEF_grh_key_category] = self._categoryString
        # port
        self._outRaw[self.DEF_grh_key_port] = []
        _portRaws = nodeRaw[self.DEF_grh_key_port]
        self._set_port_raws_build_(_portRaws)
        _outputRaws = self._outputRaw.get(_typeString, [])
        self._set_port_raws_build_(_outputRaws)

    def _set_port_raws_build_(self, portRaws):
        for i in portRaws:
            self._set_port_raw_build_(i)

    def _set_port_raw_build_(self, portRaw):
        _portpathString = portRaw[self.DEF_grh_key_portpath]
        _porttypeString = portRaw[self.DEF_grh_key_porttype]
        _portdataString = portRaw[self.DEF_grh_key_portdata]
        _assignString = portRaw[self.DEF_grh_key_assign]

        _childPathStrList = []
        _childPortsRaw = self._portChildRaw.get(_porttypeString, [])
        for seq, _portraw in enumerate(_childPortsRaw):
            _childPortnameString = self._set_port_child_raw_build_(seq, _portpathString, _porttypeString, _portdataString, _assignString, _portraw)
            if _childPortnameString is not None:
                _childPathStrList.append(_childPortnameString)

        self._set_port_raw_add_(_portpathString, _porttypeString, _portdataString, _assignString, None, _childPathStrList)

    def _set_port_child_raw_build_(self, childIndex, parentPortpath, parentPorttype, parentPortdata, parentAssign, portRaw):
        _formatString = portRaw[self.DEF_grh_keyword_format]

        _portpathString = _formatString.format(*[parentPortpath])
        _porttypeString = portRaw[self.DEF_grh_key_porttype]

        if parentPortdata:
            _portdataString = parentPortdata.split(u',')[childIndex].rstrip().lstrip()
        else:
            _portdataString = portRaw[self.DEF_grh_key_portdata]

        if parentAssign == self.DEF_grh_keyword_input:
            _portAssignString = self.DEF_grh_keyword_input_channel
        elif parentAssign == self.DEF_grh_keyword_output:
            _portAssignString = self.DEF_grh_keyword_output_channel
        else:
            _portAssignString = None

        if _portAssignString is not None:
            self._set_port_raw_add_(_portpathString, parentPorttype, _portdataString, _portAssignString, parentPortpath,
                                    [])
            return _portpathString

    def _set_port_raw_add_(self, portpath, porttype, portdata, assign, parent, children):
        _dic = self.CLS_ordered_dict()

        _dic[self.DEF_grh_key_portpath] = portpath
        _dic[self.DEF_grh_key_porttype] = porttype
        _dic[self.DEF_grh_key_portdata] = portdata
        _dic[self.DEF_grh_key_assign] = assign
        _dic[self.DEF_grh_key_parent] = parent
        _dic[self.DEF_grh_key_children] = children

        self._outRaw[self.DEF_grh_key_port].append(_dic)

    def outRaw(self):
        return self._outRaw


class Def_GrhPortQuery(grhCfg.Utility):
    VAR_grh_portsep = None

    VAR_grh_property_list = [
        grhCfg.Utility.DEF_grh_key_porttype,
        grhCfg.Utility.DEF_grh_key_portpath,
        grhCfg.Utility.DEF_grh_key_portdata,
        grhCfg.Utility.DEF_grh_key_assign,
        grhCfg.Utility.DEF_grh_key_parent,
        grhCfg.Utility.DEF_grh_key_children
    ]

    def _initDefGrhPortQuery(self, *args):
        self._portRaw = args[0]

        self._build_query_(self._portRaw)

    def _build_query_(self, *args):
        raw = args[0]
        for i in self.VAR_grh_property_list:
            self.__dict__[i] = raw[i]
    @property
    def portsep(self):
        return self.VAR_grh_portsep

    @property
    def portraw(self):
        return self._portRaw

    def __str__(self):
        _ = u''
        count = len(self.VAR_grh_property_list)
        for seq, i in enumerate(self.VAR_grh_property_list):
            _ += u'{}="{}"'.format(i, self.__dict__[i])
            if seq < (count - 1):
                _ += u', '

        return u'{}({})'.format(
            self.__class__.__name__,
            _
        )

    def __repr__(self):
        return self.__str__()


class Def_GrhNodeQuery(grhCfg.Utility):
    CLS_grh_port_query_set = None
    CLS_grh_port_query = None

    VAR_grh_property_list = [
        grhCfg.Utility.DEF_grh_key_type,
        grhCfg.Utility.DEF_grh_key_category
    ]

    def _initDefGrhNodeQuery(self, *args):
        raw = args[0]

        self._portpathDict = {}

        self._portQuerySetObj = self.CLS_grh_port_query_set(self)
        self._inputQuerySetObj = self.CLS_grh_port_query_set(self)
        self._outputQuerySetObj = self.CLS_grh_port_query_set(self)

        self._build_query_(raw)

    def _build_query_(self, *args):
        raw = args[0]

        for i in self.VAR_grh_property_list:
            self.__dict__[i] = raw[i]

        portRaws = raw[self.DEF_grh_key_port]
        for i in portRaws:
            self._build_port_query_(i)

    def _build_port_query_(self, *args):
        raw = args[0]

        obj = self.CLS_grh_port_query(raw)

        portpathString = raw[self.DEF_grh_key_portpath]
        portnameString = portpathString.split(obj.portsep)[-1]
        self._portpathDict[portnameString] = portpathString

        assignString = raw[self.DEF_grh_key_assign]
        if assignString in [self.DEF_grh_keyword_input, self.DEF_grh_keyword_input_channel]:
            self._inputQuerySetObj._set_obj_add_(obj)
        elif assignString in [self.DEF_grh_keyword_output, self.DEF_grh_keyword_output_channel]:
            self._outputQuerySetObj._set_obj_add_(obj)
        self._portQuerySetObj._set_obj_add_(obj)

    # **************************************************************************************************************** #
    def _get_portpath_(self, *args):
        portpathString = args[0]
        if portpathString in self._portpathDict:
            return self._portpathDict[portpathString]
        return portpathString

    def ports(self):
        return self._portQuerySetObj.objects()

    def hasPort(self, *args):
        return self._portQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def port(self, *args):
        return self._portQuerySetObj.object(
            self._get_portpath_(*args)
        )

    def inputs(self):
        return self._inputQuerySetObj.objects()

    def hasInput(self, *args):
        return self._inputQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def input(self, *args):
        return self._inputQuerySetObj.object(
            self._get_portpath_(*args)
        )

    def outputs(self):
        return self._outputQuerySetObj.objects()

    def hasOutput(self, *args):
        return self._outputQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def output(self, *args):
        return self._outputQuerySetObj.object(
            self._get_portpath_(*args)
        )

    def __str__(self):
        _ = u''
        count = len(self.VAR_grh_property_list)
        for seq, i in enumerate(self.VAR_grh_property_list):
            _ += u'{}="{}"'.format(i, self.__dict__[i])
            if seq < (count - 1):
                _ += u', '

        return u'{}({})'.format(
            self.__class__.__name__,
            _
        )

    def __repr__(self):
        return self.__str__()


class Def_GrhObjQueryCache(grhCfg.Utility):
    CLS_mtl_node_raw = None

    CLS_grh_node_query_set = None
    CLS_grh_node_query = None

    # noinspection PyUnusedLocal
    def _initDefGrhObjQueryCache(self, *args):
        self._nodeQuerySetObj = self.CLS_grh_node_query_set(self)

    def _get_node_type_(self, *args):
        """
        replace method
        """

    def _get_node_port_raws_(self, *args):
        """
        replace method
        """

    def _get_node_raw_(self, *args):
        categoryString = args[0]
        return {
            self.DEF_grh_key_category: categoryString,
            self.DEF_grh_key_type: self._get_node_type_(categoryString),
            self.DEF_grh_key_port: self._get_node_port_raws_(categoryString)
        }

    # **************************************************************************************************************** #
    def _get_has_node_(self, *args):
        return self._nodeQuerySetObj.hasObject(*args)

    def _get_nodes_(self):
        return self._nodeQuerySetObj.objects()

    def _get_node_(self, *args):
        if self._nodeQuerySetObj._get_obj_exist_(*args):
            obj = self._nodeQuerySetObj._get_obj_(*args)
        else:
            raw = self._get_node_raw_(*args)
            obj = self.CLS_grh_node_query(raw)
            self._nodeQuerySetObj._set_obj_add_(obj)
        return obj

    def hasNode(self, *args):
        return self._get_has_node_(*args)

    def nodes(self):
        return self._get_nodes_()

    def node(self, *args):
        return self._get_node_(*args)

    def nodeDef(self, *args):
        return self._get_node_(*args)

    def nodePort(self, *args):
        categoryString, portpathString = args
        return self.node(categoryString).port(portpathString)


# translator object query cache ************************************************************************************** #
class Def_GrhTrsNodeRaw(grhCfg.Utility):
    OBJ_grh_query_cache = None
    VAR_mtl_def_key_list = []

    def _initDefGrhTrsNodeRaw(self, *args):
        dccObjectRaw, dccOutputRaw, dccPortChildRaw = args

        self._dccOutRawDict = self.CLS_ordered_dict()

        self._dccObjectRaw = dccObjectRaw
        self._dccOutputRaw = dccOutputRaw
        self._dccPortChildRaw = dccPortChildRaw

        self._translateDccObjectRaw_()

    def _translateDccObjectRaw_(self):
        self._mtlCategoryString = self._dccObjectRaw[self.DEF_grh_key_target_category]

        self._mtlNodeDefObj = self.OBJ_grh_query_cache.nodeDef(self._mtlCategoryString)

        self._typeString = self._mtlNodeDefObj.type
        self._dccOutRawDict[self.DEF_grh_key_category] = self._mtlCategoryString
        self._dccOutRawDict[self.DEF_grh_key_type] = self._typeString
        self._dccOutRawDict[self.DEF_grh_key_source_port] = self.CLS_ordered_dict()

        for _key in self.VAR_mtl_def_key_list:
            if _key in self._dccObjectRaw:
                self._dccOutRawDict[_key] = self._dccObjectRaw[_key]

        dccPortsRaw = self._dccObjectRaw[self.DEF_grh_key_source_port]
        self._translateDccPortsRaw_(dccPortsRaw)

        dccOutputsRaw = self._dccOutputRaw.get(self._typeString, {})
        self._translateDccPortsRaw_(dccOutputsRaw)

    def _translateDccPortsRaw_(self, dccPortsRaw):
        for dccPortnameString, dccPortRaw in dccPortsRaw.items():
            if self.DEF_grh_key_target_portpath in dccPortRaw:
                mtlPortnameString = dccPortRaw[self.DEF_grh_key_target_portpath]

                if isinstance(mtlPortnameString, (str, unicode)):
                    self._translateDccPortRaw_(dccPortnameString, mtlPortnameString, dccPortRaw)

                elif isinstance(mtlPortnameString, (tuple, list)):
                    for mtlPortnameString_ in mtlPortnameString:
                        self._translateDccPortRaw_(dccPortnameString, mtlPortnameString_, dccPortRaw)

    def _translateDccPortRaw_(self, dccPortnameString, mtlPortnameString, dccPortRaw_):
        mtlPortDefObject = self._mtlNodeDefObj.port(mtlPortnameString)

        if self.DEF_grh_key_source_porttype in dccPortRaw_:
            mtlPorttypeString = dccPortRaw_[self.DEF_grh_key_source_porttype]
        else:
            mtlPorttypeString = mtlPortDefObject.porttype

        mtlAssignString = mtlPortDefObject.assign

        if mtlAssignString not in [self.DEF_grh_keyword_input_channel, self.DEF_grh_keyword_output_channel]:
            dccChildPortsRaw = self._dccPortChildRaw.get(mtlPorttypeString, [])
            for _dccPortDef in dccChildPortsRaw:
                self._translateDccChildPortRaw_(dccPortnameString, mtlPortnameString, mtlPorttypeString, _dccPortDef)

            self._addDccPortRaw_(dccPortnameString, mtlPortnameString, mtlPortDefObject)

    def _translateDccChildPortRaw_(self, dccParentPortnameString, parentPortnameString, mtlPorttypeString, dccPortRaw_):
        _dccFormatString = dccPortRaw_[self.DEF_grh_keyword_format]
        _formatString = dccPortRaw_[self.DEF_grh_key_target_portpath][self.DEF_grh_keyword_format]
        if mtlPorttypeString == self.DEF_grh_keyword_porttype_uv_1:
            _dccPortnameString = _dccFormatString.format(*[dccParentPortnameString, dccParentPortnameString[:-2]])
        else:
            _dccPortnameString = _dccFormatString.format(*[dccParentPortnameString])

        _portnameString = _formatString.format(*[parentPortnameString])

        mtlPortDefObject = self._mtlNodeDefObj.port(_portnameString)

        self._addDccPortRaw_(_dccPortnameString, _portnameString, mtlPortDefObject)

    def _addDccPortRaw_(self, dccPortnameString, mtlPortnameString, portDefObject_):
        _dic = self.CLS_ordered_dict()
        _dic[self.DEF_grh_key_portpath] = mtlPortnameString
        for _k, _v in portDefObject_.portraw.items():
            _dic[_k] = _v
        _assignString = portDefObject_.assign
        self._dccOutRawDict[self.DEF_grh_key_source_port][(dccPortnameString, _assignString)] = _dic

    def dccOutRaw(self):
        return self._dccOutRawDict


class Def_GrhTrsPortQuery(grhCfg.Utility):
    def _initDefGrhTrsPortQuery(self, *args):
        dccPortnameString, portRaw = args

        self._dccPortname = dccPortnameString
        self._dccPortraw = portRaw
    @property
    def dccPortname(self):
        return self._dccPortname
    @property
    def mtlPortname(self):
        return self._dccPortraw[self.DEF_grh_key_portpath]
    @property
    def porttype(self):
        return self._dccPortraw[self.DEF_grh_key_porttype]
    @property
    def portdata(self):
        return self._dccPortraw[self.DEF_grh_key_portdata]
    @property
    def assign(self):
        return self._dccPortraw[self.DEF_grh_key_assign]
    @property
    def parent(self):
        return self._dccPortraw[self.DEF_grh_key_parent]
    @property
    def children(self):
        return self._dccPortraw[self.DEF_grh_key_children]


class Def_GrhTrsNodeQuery(grhCfg.Utility):
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
        for k, v in self._dccNodeDefDict[self.DEF_grh_key_source_port].items():
            dccPortnameString, mtlAssignString = k
            portDefObject = self.CLS_mtl_dcc_port_def(dccPortnameString, v)
            if mtlAssignString in [self.DEF_grh_keyword_input, self.DEF_grh_keyword_input_channel, self.DEF_grh_keyword_property, self.DEF_grh_keyword_visibility]:
                self._dccInputDefObjDict[dccPortnameString] = portDefObject
                self._dccInputDefObjList.append(portDefObject)
            elif mtlAssignString in [self.DEF_grh_keyword_output, self.DEF_grh_keyword_output_channel]:
                self._dccOutputDefObjDict[dccPortnameString] = portDefObject
                self._dccOutputDefObjList.append(portDefObject)
            self._dccPortDefObjDict[dccPortnameString] = portDefObject
            self._dccPortDefObjList.append(portDefObject)
    @property
    def dccCategory(self):
        return self._dccCategoryString
    @property
    def mtlCategory(self):
        return self._dccNodeDefDict[self.DEF_grh_key_category]
    @property
    def type(self):
        return self._dccNodeDefDict[self.DEF_grh_key_type]
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
            self.DEF_grh_key_target_port,
            {}
        )
    @property
    def mtlPortdataRaw(self):
        return self._dccNodeDefDict.get(
            self.DEF_grh_key_target_portdata,
            {}
        )
    @property
    def customNode(self):
        return self._dccNodeDefDict.get(
            self.DEF_grh_keyword_custom_node,
            {}
        )
    @property
    def createExpressionRaw(self):
        return self._dccNodeDefDict.get(
            self.DEF_grh_keyword_create_expression,
            {}
        )
    @property
    def afterExpressionRaw(self):
        return self._dccNodeDefDict.get(
            self.DEF_grh_keyword_after_expression,
            {}
        )


class Def_GrhTrsObjQueryCache(grhCfg.Utility):
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


# object cache ******************************************************************************************************* #
class Def_GrhObjCache(grhCfg.Utility):
    CLS_cache_obj_set = None

    # noinspection PyUnusedLocal
    def _initDefGrhObjCache(self, *args):
        self._objSetObj = self.CLS_cache_obj_set(self)

    # **************************************************************************************************************** #
    def _get_objs_(self):
        return self._objSetObj._get_objs_()

    def _set_obj_add_(self, *args):
        self._objSetObj._set_obj_add_(*args)

    def _get_obj_exist_(self, *args):
        return self._objSetObj._get_obj_exist_(*args)

    def _get_obj_(self, *args):
        if len(args) == 1:
            if isinstance(args[0], (float, int)):
                index = args[0]
                return self._objSetObj._get_obj_(index)
            elif isinstance(args[0], (str, unicode)):
                keyString = args[0]
                return self._objSetObj._get_obj_(keyString)
        else:
            keyString, cls, clsArgs = args
            if self._objSetObj._get_obj_exist_(keyString) is True:
                return self._objSetObj._get_obj_(keyString)
            else:
                obj = cls(*clsArgs)
                self._objSetObj._set_obj_add_(obj)
                return obj

    def _get_obj_index_(self, *args):
        return self._objSetObj._get_obj_index_(*args)

    def objects(self):
        return self._get_objs_()

    def addObject(self, *args):
        self._set_obj_add_(*args)

    def hasObject(self, *args):
        return self._get_obj_exist_(*args)

    def object(self, *args):
        return self._get_obj_(*args)

    def index(self, *args):
        return self._get_obj_index_(*args)


# object ************************************************************************************************************* #
class Def_GrhObj(grhCfg.Utility):
    # noinspection PyUnusedLocal
    def _initDefGrhObj(self, *args):
        # parent
        self._parentPathStr = None
        # children
        self._childPathStrList = []

    @classmethod
    def _mtd_cache_(cls, cacheQueryObject, objectKeyString, objectCls, clsArgs):
        if cacheQueryObject._get_obj_exist_(objectKeyString) is True:
            return cacheQueryObject._get_obj_(objectKeyString)
        else:
            cacheObject = objectCls(*clsArgs)
            cacheQueryObject._set_obj_add_(cacheObject)
            return cacheObject

    # **************************************************************************************************************** #
    def _set_parent_(self, *args):
        """
        replace method
        """

    def _get_parent_exist_(self):
        """
        replace method
        """

    def _get_parent_(self):
        """
        replace method
        """

    def hasParent(self):
        return self._get_parent_exist_()

    def parent(self):
        return self._get_parent_()

    # **************************************************************************************************************** #
    def _get_children_exist_(self):
        """
        replace method
        """

    def _set_child_add_(self, *args):
        """
        replace method
        """

    def _get_child_exist_(self, *args):
        """
        replace method
        """

    def _get_children_(self, *args):
        """
        replace method
        """

    def _get_child_(self, *args):
        """
        replace method
        """

    def _set_children_(self, *args):
        """
        replace method
        """

    def hasChildren(self):
        """
        :return: bool
        """
        return self._get_children_exist_()

    def children(self):
        """
        :return: list
        """
        return self._get_children_()

    def hasChild(self, *args):
        """
        :return: bool
        """
        return self._get_child_exist_(*args)

    def child(self, *args):
        """
        :param args: str
        :return: object
        """
        return self._get_child_(*args)


# port
class Def_GrhPort(Def_GrhObj):
    CLS_grh_type = None

    CLS_grh_porttype = None

    CLS_grh_portpath = None

    VAR_grh_value_cls_dict = {}

    def _initDefGrhPort(self, *args):
        self._initDefGrhObj()

        nodeObject, _ = args[:2]
        # node
        self._nodeObj = nodeObject
        # port
        if isinstance(_, (str, unicode)):
            self._set_portpath_(_)
        if isinstance(_, Def_GrhPortQuery):
            self._set_port_build_(_)
        # source
        self._sourcePortIndex = None
        # target
        self._targetPortIndexList = []

    def _get_cache_obj_(self, *args):
        return self._nodeObj.OBJ_grh_obj_cache._get_obj_(*args)

    def _get_cache_obj_index(self, *args):
        return self._nodeObj.OBJ_grh_obj_cache._get_obj_index_(*args)

    # **************************************************************************************************************** #
    def _set_port_build_(self, *args):
        portQueryObject = args[0]

        porttypeString = portQueryObject.porttype

        self._set_type_(portQueryObject.assign)
        self._set_porttype_(porttypeString)
        self._set_portpath_(portQueryObject.portpath)
        self._set_parent_(portQueryObject.parent)
        self._set_children_(portQueryObject.children)

        valueCls = self._get_value_cls_(porttypeString)
        if valueCls is not None:
            portdata = portQueryObject.portdata
            self._set_value_(
                valueCls(portdata)
            )
            self._set_default_value_(
                valueCls(portdata)
            )

    # **************************************************************************************************************** #
    def _get_node_cache_obj_(self, *args):
        """
        replace method
        """

    def _get_port_cache_obj_(self, *args):
        """
        replace method
        """

    # **************************************************************************************************************** #
    def _set_type_(self, *args):
        self._typeObj = self.CLS_grh_type(*args)

    def type(self):
        return self._typeObj

    def typeString(self):
        return self._typeObj.toString()

    # **************************************************************************************************************** #
    def _set_porttype_(self, *args):
        self._porttypeObj = self.CLS_grh_porttype(*args)

    def porttype(self):
        return self._porttypeObj

    def porttypeString(self):
        return self._porttypeObj.toString()

    # **************************************************************************************************************** #
    def _set_portpath_(self, *args):
        self._portpathObj = self.CLS_grh_portpath(*args)

    def portpath(self):
        return self._portpathObj

    def portpathString(self):
        return self._portpathObj.toString()

    def portname(self):
        return self._portpathObj.bscname()

    def portnameString(self):
        return self._portpathObj.bscnameString()

    def attrpathString(self):
        return self._portpathObj.pathsep().join(
            [self._nodeObj.toString(), self._portpathObj.toString()]
        )

    def pathString(self):
        return self.attrpathString()

    # **************************************************************************************************************** #
    def _get_indexes_(self):
        """
        replace method
        """

    def isColor(self):
        return self.porttypeString() in [
            u'color2',
            u'color3',
            u'color4'
        ]

    def isFilename(self):
        return self.porttypeString() == u'filename'

    def isArray(self):
        return self.porttypeString() in [
            u'integerarray',
            u'floatarray',
            u'color2array',
            u'color3array',
            u'color4array',
            u'vector2array',
            u'vector3array',
            u'vector4array',
            u'stringarray'
        ]

    def indexes(self):
        return self._get_indexes_()

    # **************************************************************************************************************** #
    def node(self):
        return self._nodeObj

    # **************************************************************************************************************** #
    def _get_value_cls_(self, *args):
        porttypeString = args[0]
        if porttypeString in self.VAR_grh_value_cls_dict:
            return self.VAR_grh_value_cls_dict[porttypeString]

    def _set_value_(self, *args):
        obj = args[0]
        self._valueObj = obj

    def setValue(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._set_value_(valueObject)

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

    # **************************************************************************************************************** #
    def _set_default_value_(self, *args):
        obj = args[0]
        self._defValueObj = obj

    def setDefaultValue(self, *args):
        self._set_default_value_(*args)

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

    # **************************************************************************************************************** #
    def isValueChanged(self):
        """
        :return: bool
        """
        return not self.value() == self.defaultValue()

    # **************************************************************************************************************** #
    def _get_portdata_(self, *args):
        """
        replace method
        """

    def _get_portdata_string_(self, *args):
        """
        replace method
        """

    def _set_portdata_(self, *args):
        pass

    def _set_portdata_string_(self, *args):
        pass

    def portdata(self, *args):
        return self._get_portdata_(*args)

    def portdataString(self):
        return self._get_portdata_string_()

    def setPortdata(self, raw):
        self._valueObj.setRaw(raw)

    def setPortdataString(self, rawString):
        self._valueObj.setRawString(rawString)

    def isChanged(self):
        return self.isValueChanged() or self.hasSource()

    # **************************************************************************************************************** #
    def _get_is_source_(self):
        return self._get_targets_exist_()

    def _get_source_exist_(self, *args):
        if args:
            return self._get_cache_obj_index(args[0]) == self._sourcePortIndex
        return self._sourcePortIndex is not None

    def _get_source_(self):
        if self._get_source_exist_() is True:
            return self._get_cache_obj_(
                self._sourcePortIndex
            )

    def isSource(self):
        return self._get_is_source_()

    def hasSource(self):
        return self._get_source_exist_()

    def source(self):
        return self._get_source_()

    # **************************************************************************************************************** #
    def _get_is_target_(self):
        """
        replace method
        """

    def _get_targets_exist_(self):
        """
        replace method
        """

    def _get_targets_(self):
        """
        replace method
        """

    def _get_target_exist_(self, *args):
        """
        replace method
        """

    def _get_target_(self, *args):
        """
        replace method
        """

    def isTarget(self):
        """
        :return: bool
        """
        return self._get_is_target_()

    def hasTargets(self):
        """
        :return: list
        """
        return self._get_targets_exist_()

    def targets(self):
        return self._get_targets_()

    def hasTarget(self, *args):
        return self._get_target_(*args)

    def target(self, *args):
        return self._get_target_(*args)

    def insertTarget(self, inputPort, outputPort):
        for i in self.targets():
            outputPort.connectTo(i)
        self.connectTo(inputPort)

    # **************************************************************************************************************** #
    def _set_add_target_(self, *args):
        obj = args[0]

        index = self._get_cache_obj_index(obj)
        if obj.hasSource():
            sourceObject = obj.source()
            if index in sourceObject._targetPortIndexList:
                sourceObject._targetPortIndexList.remove(index)

        if index not in self._targetPortIndexList:
            self._targetPortIndexList.append(index)
            obj._set_source_(self)

    def connectTo(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: None
        """
        self._set_add_target_(*args)

    def isConnectTo(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: bool
        """
        return self._get_target_exist_(*args)

    # **************************************************************************************************************** #
    def _set_source_(self, *args):
        obj = args[0]
        if self._get_source_exist_(obj) is False:
            self._sourcePortIndex = self._get_cache_obj_index(obj)
            obj._set_add_target_(self)

    def connectFrom(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: None
        """
        self._set_source_(*args)

    def isConnectFrom(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: bool
        """
        return self._get_source_exist_(*args)

    # **************************************************************************************************************** #
    def _get_port_given_(self):
        if self.hasSource() is True:
            return self.source()
        return self.value()

    def portgiven(self):
        return self._get_port_given_()

    def toString(self):
        return self.attrpathString()

    def __str__(self):
        return u'{}(portpath="{}", porttype="{}", node="{}")'.format(
            self.__class__.__name__,
            self.portpath().toString(),
            self.porttype().toString(),
            self.node().toString()
        )

    def __repr__(self):
        return self.__str__()


# node
class Def_GrhNode(Def_GrhObj):
    CLS_grh_type = None
    CLS_grh_category = None

    CLS_grh_nodepath = None

    CLS_grh_port_set = None
    VAR_grh_port_cls_dict = {}

    VAR_grh_input_assign_list = []
    VAR_grh_output_assign_list = []
    VAR_grh_param_assign_list = []

    OBJ_grh_query_cache = None
    OBJ_grh_obj_cache = None

    def _initDefGrhNode(self, *args):
        self._initDefGrhObj()

        categoryString, nodepathString = args[:2]

        self._nodepathObj = self.CLS_grh_nodepath(nodepathString)

        self._nodeQueryObj = self.OBJ_grh_query_cache.node(
            categoryString
        )

        self._set_node_build_(self._nodeQueryObj)

        self._portSetObj = self.CLS_grh_port_set(self)
        self._paramSetObj = self.CLS_grh_port_set(self)
        self._inputSetObj = self.CLS_grh_port_set(self)
        self._outputSetObj = self.CLS_grh_port_set(self)

        self.OBJ_grh_obj_cache._set_obj_add_(self)

        self._set_ports_build_()

    # **************************************************************************************************************** #
    def _set_node_build_(self, *args):
        nodeQueryObject = args[0]

        self._set_type_(nodeQueryObject.type)
        self._set_category_(nodeQueryObject.category)

    # **************************************************************************************************************** #
    def _set_type_(self, *args):
        self._typeObj = self.CLS_grh_type(*args)

    def type(self):
        """
        :return: object
        """
        return self._typeObj

    def typeString(self):
        """
        :return: str
        """
        return self._typeObj.toString()

    # **************************************************************************************************************** #
    def _set_category_(self, *args):
        self._categoryObj = self.CLS_grh_category(*args)

    def category(self):
        """
        :return: object
        """
        return self._categoryObj

    def categoryString(self):
        """
        :return: str
        """
        return self._categoryObj.toString()

    def nodepath(self):
        """
        :return: object
        """
        return self._nodepathObj

    def nodepathString(self):
        """
        :return: str
        """
        return self.nodepath().toString()

    def nodename(self):
        return self._nodepathObj.bscname()

    def nodenameString(self):
        return self._nodepathObj.bscnameString()

    def name(self):
        """
        :return: object
        """
        return self._nodepathObj.name()

    def nameString(self):
        """
        :return: str
        """
        return self.name().toString()

    def pathString(self):
        return self.nodepathString()

    # **************************************************************************************************************** #
    def _get_port_cls_(self, *args):
        assignString = args[0]
        if assignString in self.VAR_grh_port_cls_dict:
            return self.VAR_grh_port_cls_dict[assignString]

    def _set_ports_build_(self):
        def addPortFnc_(nodepathString_, portQuery_):
            _porttypeString = portQuery_.porttype
            _portpathString = portQuery_.portpath
            _assignString = portQuery_.assign

            _portCls = self._get_port_cls_(_assignString)

            if _portCls is not None:
                _attrpathString = _portCls._get_attrpath_(
                    nodepathString_, _portpathString
                )
                objArgs = _attrpathString, _portCls, (self, portQuery_)
                _portObject = self.OBJ_grh_obj_cache.object(*objArgs)
                if _portObject is not None:
                    if _assignString in self.VAR_grh_param_assign_list:
                        self._paramSetObj._set_obj_add_(_portObject)
                    elif _assignString in self.VAR_grh_input_assign_list:
                        self._inputSetObj._set_obj_add_(_portObject)
                    elif _assignString in self.VAR_grh_output_assign_list:
                        self._outputSetObj._set_obj_add_(_portObject)

                    self._portSetObj._set_obj_add_(_portObject)

        for i in self._nodeQueryObj.ports():
            addPortFnc_(self.nodepathString(), i)

    def ports(self):
        """
        :return: list
        """
        return self._portSetObj.objects()

    def hasPort(self, *args):
        """
        :param args: bool
        :return:
        """
        return self._portSetObj._get_obj_exist_(*args)

    def port(self, portpathString):
        """
        :param portpathString: str
        :return: object
        """
        return self._portSetObj.object(
            self._nodeQueryObj._get_portpath_(portpathString)
        )

    # **************************************************************************************************************** #
    def _get_changed_inputs_(self):
        def addFnc_(portObject_):
            if not portObject_ in lis:
                lis.append(portObject_)

        lis = []
        for i in self.inputs():
            if i.isChanged() is True:
                addFnc_(i)
        return lis

    def inputs(self):
        return self._inputSetObj.objects()

    def hasInput(self, *args):
        return self._inputSetObj.hasObject(*args)

    def input(self, *args):
        return self._inputSetObj.object(*args)

    def changedInputs(self):
        """
        :return: list
        """
        return self._get_changed_inputs_()

    # **************************************************************************************************************** #
    def outputs(self):
        return self._outputSetObj.objects()

    def hasOutput(self, *args):
        return self._outputSetObj.hasObject(*args)

    def output(self, *args):
        if args:
            portpathString = args[0]
            return self._outputSetObj.object(portpathString)
        return self._outputSetObj.objects()[-1]

    # **************************************************************************************************************** #
    def params(self):
        return self._paramSetObj.objects()

    def hasParam(self, *args):
        return self._paramSetObj.hasObject(*args)

    def param(self, *args):
        return self._paramSetObj.object(*args)

    # **************************************************************************************************************** #
    def _get_source_nodes_(self, *args):
        """
        replace method
        """

    def _get_all_source_nodes_(self, *args):
        """
        replace method
        """

    def _get_target_nodes_(self, *args):
        """
        replace method
        """

    def _get_all_target_nodes_(self, *args):
        """
        replace method
        """

    @classmethod
    def _get_nodes_filter_(cls, nodeObjects, *args):
        """
        replace method
        """

    def sourceNodes(self, *args):
        return self._get_source_nodes_(*args)

    def allSourceNodes(self, *args):
        return self._get_all_source_nodes_(*args)

    def targetNodes(self, *args):
        return self._get_target_nodes_(*args)

    def allTargetNodes(self, *args):
        return self._get_all_target_nodes_(*args)

    # **************************************************************************************************************** #
    def connections(self):
        lis = []
        for sourceObject in self.outputs():
            if sourceObject.hasTargets():
                for targetObject in sourceObject.targets():
                    connection = (sourceObject, targetObject)
                    if not connection in lis:
                        lis.append(connection)
        return lis

    # **************************************************************************************************************** #
    def toString(self):
        return self.nodepathString()

    def __str__(self):
        return u'{}(nodepath="{}", category="{}")'.format(
            self.__class__.__name__,
            self.nodepath().toString(),
            self.category().toString()
        )

    def __repr__(self):
        return self.__str__()


class Def_GrhConnection(grhCfg.Utility):
    def _initDefGrhConnection(self):
        pass
