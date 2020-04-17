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

    def _set_obj_set_data_int_(self):
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
        elif isinstance(args[0], object):
            return args[0]

    def _get_obj_index_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objKeyString = args[0]
            obj = self._objectFilterDict[objKeyString]
            return self._objectList.index(obj)
        elif isinstance(args[0], (int, float)):
            index = args[0]
            return int(index)
        elif isinstance(args[0], object):
            obj = args[0]
            return self._objectList.index(obj)

    def _get_string_(self):
        return self.VAR_grh_objectsep.join([i.toString() for i in self.objects()])

    def addObject(self, *args):
        obj = args[0]
        keyString = self._get_object_key_string_(obj)
        assert keyString not in self._objectFilterDict, u'''{}({})'s object "{}" is Exist.'''.format(
            self.__class__.__name__, self._obj.__class__.__name__, keyString
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

    def _set_obj_exist_val_(self, *args):
        if args:
            keyString = args[0]
            if not keyString in self._objectFilterDict:
                raise KeyError(
                    u'''Class: "{}"; Connect: "{}" key "{}" is Unregistered.'''.format(
                        self.__class__.__name__,
                        self._obj.__class__.__name__,
                        keyString
                    )
                )
        else:
            raise KeyError(
                u'''Class: "{}"; Connect: "{}" key Must not be Empty.'''.format(
                        self.__class__.__name__,
                        self._obj.__class__.__name__
                    )
            )

    def object(self, *args):
        """
        :param args:
            1.args[0]
        :return: object
        """
        self._set_obj_exist_val_(*args)
        if args:
            keyString = args[0]

            return self._get_obj_(keyString)

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
class Def_GrhNodeQueryraw(grhCfg.Utility):
    def _initDefGrhNodeQueryraw(self, *args):
        self._categoryString, self._nodeRaw, self._outputRaw, self._portChildRaw = args

        self._outRawDict = self.CLS_ordered_dict()

        self._set_node_raw_build_(self._nodeRaw)

    def _set_node_raw_build_(self, nodeRaw):
        _typeString = nodeRaw[self.DEF_grh_key_type]
        # property
        self._outRawDict[self.DEF_grh_key_type] = _typeString
        self._outRawDict[self.DEF_grh_key_category] = self._categoryString
        # port
        self._outRawDict[self.DEF_grh_key_port] = []
        _portRaws = nodeRaw[self.DEF_grh_key_port]
        self._set_port_raws_build_(_portRaws)
        _outputRaws = self._outputRaw.get(_typeString, [])
        self._set_port_raws_build_(_outputRaws)

    def _set_port_raws_build_(self, portRaws):
        for i in portRaws:
            self._set_port_raw_build_(i)

    def _set_port_raw_build_(self, portQueryraw):
        _portpathString = portQueryraw[self.DEF_grh_key_portpath]
        _porttypeString = portQueryraw[self.DEF_grh_key_porttype]
        _portrawString = portQueryraw[self.DEF_grh_key_portraw]
        _assignString = portQueryraw[self.DEF_grh_key_assign]

        _childPathStrList = []
        childPortQueryraws = self._portChildRaw.get(_porttypeString, [])
        for seq, childPortQueryraw in enumerate(childPortQueryraws):
            childPortpathString = self._set_port_child_raw_build_(
                portQueryraw, childPortQueryraw,
                seq
            )
            if childPortpathString is not None:
                _childPathStrList.append(childPortpathString)

        self._set_port_raw_add_(_portpathString, _porttypeString, _portrawString, _assignString, None, _childPathStrList)

    def _set_port_child_raw_build_(self, parentPortQueryraw, portQueryraw, childIndex):
        parentPortpathString = parentPortQueryraw[self.DEF_grh_key_portpath]
        parentPorttypeString = parentPortQueryraw[self.DEF_grh_key_porttype]
        parentPortrawString = parentPortQueryraw[self.DEF_grh_key_portraw]
        parentAssignString = parentPortQueryraw[self.DEF_grh_key_assign]

        _formatString = portQueryraw[self.DEF_grh_keyword_format]

        _portpathString = _formatString.format(*[parentPortpathString])
        _porttypeString = portQueryraw[self.DEF_grh_key_porttype]

        if parentPortrawString:
            _portrawString = parentPortrawString.split(u',')[childIndex].rstrip().lstrip()
        else:
            _portrawString = portQueryraw[self.DEF_grh_key_portraw]

        if parentAssignString == self.DEF_grh_keyword_inparm:
            _portAssignString = self.DEF_grh_keyword_inparm_channel
        elif parentAssignString == self.DEF_grh_keyword_otparm:
            _portAssignString = self.DEF_grh_keyword_otparm_channel
        else:
            _portAssignString = None

        if _portAssignString is not None:
            self._set_port_raw_add_(_portpathString, parentPorttypeString, _portrawString, _portAssignString, parentPortpathString, [])
            return _portpathString

    def _set_port_raw_add_(self, portpath, porttype, portraw, assign, parent, children):
        _dic = self.CLS_ordered_dict()

        _dic[self.DEF_grh_key_portpath] = portpath
        _dic[self.DEF_grh_key_porttype] = porttype
        _dic[self.DEF_grh_key_portraw] = portraw
        _dic[self.DEF_grh_key_assign] = assign
        _dic[self.DEF_grh_key_parent] = parent
        _dic[self.DEF_grh_key_children] = children

        self._outRawDict[self.DEF_grh_key_port].append(_dic)

    def outRaw(self):
        return self._outRawDict


class Def_GrhPortQuery(grhCfg.Utility):
    VAR_grh_portsep = None

    VAR_grh_property_list = [
        grhCfg.Utility.DEF_grh_key_porttype,
        grhCfg.Utility.DEF_grh_key_portpath,
        grhCfg.Utility.DEF_grh_key_portraw,
        grhCfg.Utility.DEF_grh_key_assign,
        grhCfg.Utility.DEF_grh_key_parent,
        grhCfg.Utility.DEF_grh_key_children
    ]

    def _initDefGrhPortQuery(self, *args):
        self._portQueryrawList = args[0]

        self._set_port_query_build_(self._portQueryrawList)

    def _set_port_query_build_(self, *args):
        raw = args[0]
        for i in self.VAR_grh_property_list:
            self.__dict__[i] = raw[i]

    @property
    def portsep(self):
        return self.VAR_grh_portsep

    @property
    def portQueryraw(self):
        return self._portQueryrawList

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

    VAR_grh_param_assign_keyword_list = []
    VAR_grh_inparm_assign_keyword_list = []
    VAR_grh_otparm_assign_keyword_list = []

    VAR_grh_channel_assign_keyword_list = []

    def _initDefGrhNodeQuery(self, *args):
        self._nodeQueryRawDict = args[0]
        self._portpathDict = {}

        self._set_node_query_build_(self._nodeQueryRawDict)
        self._set_port_queries_build_(self._nodeQueryRawDict)

    def _set_node_query_build_(self, *args):
        raw = args[0]

        for i in self.VAR_grh_property_list:
            self.__dict__[i] = raw[i]

    def _set_port_queries_build_(self, *args):
        raw = args[0]

        self._portQuerySetObj = self.CLS_grh_port_query_set(self)
        self._paramQuerySetObj = self.CLS_grh_port_query_set(self)
        self._inparmQuerySetObj = self.CLS_grh_port_query_set(self)
        self._otparmQuerySetObj = self.CLS_grh_port_query_set(self)

        portRaws = raw[self.DEF_grh_key_port]
        for i in portRaws:
            self._set_port_query_build_(i)

    def _set_port_query_build_(self, *args):
        raw = args[0]

        obj = self.CLS_grh_port_query(raw)

        portpathString = raw[self.DEF_grh_key_portpath]
        portnameString = portpathString.split(obj.portsep)[-1]
        self._portpathDict[portnameString] = portpathString

        assignString = raw[self.DEF_grh_key_assign]
        if assignString in self.VAR_grh_param_assign_keyword_list:
            self._paramQuerySetObj._set_obj_add_(obj)
        if assignString in self.VAR_grh_inparm_assign_keyword_list:
            self._inparmQuerySetObj._set_obj_add_(obj)
        if assignString in self.VAR_grh_otparm_assign_keyword_list:
            self._otparmQuerySetObj._set_obj_add_(obj)

        self._portQuerySetObj._set_obj_add_(obj)

    # **************************************************************************************************************** #
    def _get_portpath_(self, *args):
        portpathString = args[0]
        if portpathString in self._portpathDict:
            return self._portpathDict[portpathString]
        return portpathString

    # **************************************************************************************************************** #
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

    # **************************************************************************************************************** #
    def params(self):
        return self._paramQuerySetObj.objects()

    def hasParam(self, *args):
        return self._paramQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def param(self, *args):
        return self._paramQuerySetObj.object(
            self._get_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def inparms(self):
        return self._inparmQuerySetObj.objects()

    def hasInparm(self, *args):
        return self._inparmQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def inparm(self, *args):
        return self._inparmQuerySetObj.object(
            self._get_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def otparms(self):
        return self._otparmQuerySetObj.objects()

    def hasOtparm(self, *args):
        return self._otparmQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def otparm(self, *args):
        return self._otparmQuerySetObj.object(
            self._get_portpath_(*args)
        )

    @property
    def nodeQueryraw(self):
        return self._nodeQueryRawDict

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
    CLS_grh_node_raw = None

    CLS_grh_node_query_set = None
    CLS_grh_node_query = None

    VAR_grh_node_file = None
    VAR_grh_geometry_file = None
    VAR_grh_material_file = None
    VAR_grh_output_file = None
    VAR_grh_port_child_file = None

    # noinspection PyUnusedLocal
    def _initDefGrhObjQueryCache(self, *args):
        self._nodeQuerySetObj = self.CLS_grh_node_query_set(self)
        
        self._set_node_queries_build_()
    
    def _set_node_queries_build_(self):
        pass

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
    def _get_node_exist_(self, *args):
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
        return self._get_node_exist_(*args)

    def nodes(self):
        return self._get_nodes_()

    def node(self, *args):
        return self._get_node_(*args)

    def nodePort(self, *args):
        categoryString, portpathString = args
        return self.node(categoryString).port(portpathString)


# translator object query cache ************************************************************************************** #
class Def_GrhTrsNodeQueryraw(grhCfg.Utility):
    VAR_mtl_def_key_list = []

    VAR_grh_trs_port_key_dic = {
        grhCfg.Utility.DEF_grh_key_porttype: grhCfg.Utility.DEF_grh_key_target_porttype,
        grhCfg.Utility.DEF_grh_key_portraw: grhCfg.Utility.DEF_grh_key_target_portraw,
        grhCfg.Utility.DEF_grh_key_assign: grhCfg.Utility.DEF_grh_key_target_assign,
        grhCfg.Utility.DEF_grh_key_parent: grhCfg.Utility.DEF_grh_key_target_parent,
        grhCfg.Utility.DEF_grh_key_children: grhCfg.Utility.DEF_grh_key_target_children
    }

    VAR_grh_trs_channel_keyword_list = []

    def _initDefGrhTrsNodeQueryraw(self, *args):
        (
            self._tgtNodeQueryObj,
            self._srcCategoryString,
            self._trsNodeRaws, self._trsOutputRaws, self._trsPortChildRaws
        ) = args

        self._outTrsRawDict = self.CLS_ordered_dict()

        self._set_trs_node_raw_build_()

    def _set_trs_node_raw_build_(self):
        self._tgtCategoryString = self._trsNodeRaws[self.DEF_grh_key_target_category]

        self._tgtTypeString = self._tgtNodeQueryObj.type
        self._outTrsRawDict[self.DEF_grh_key_source_category] = self._srcCategoryString
        self._outTrsRawDict[self.DEF_grh_key_target_category] = self._tgtCategoryString

        self._outTrsRawDict[self.DEF_grh_key_type] = self._tgtTypeString

        self._outTrsRawDict[self.DEF_grh_key_source_port] = []

        for _key in self.VAR_mtl_def_key_list:
            if _key in self._trsNodeRaws:
                self._outTrsRawDict[_key] = self._trsNodeRaws[_key]

        trsPortQueryraws = self._trsNodeRaws[self.DEF_grh_key_source_port]
        self._set_trs_port_raws_build_(trsPortQueryraws)

        trsOutputQueryraws = self._trsOutputRaws.get(self._tgtTypeString, {})
        self._set_trs_port_raws_build_(trsOutputQueryraws)

    def _set_trs_port_raws_build_(self, trsPortQueryraws):
        for srcPortpathString, trsPortQueryraw in trsPortQueryraws.items():
            if self.DEF_grh_key_target_portpath in trsPortQueryraw:
                tgtPortpathString = trsPortQueryraw[self.DEF_grh_key_target_portpath]

                if isinstance(tgtPortpathString, (str, unicode)):
                    self._set_trs_port_raw_build_(
                        trsPortQueryraw,
                        srcPortpathString, tgtPortpathString
                    )

                elif isinstance(tgtPortpathString, (tuple, list)):
                    for tgtPortpathString_ in tgtPortpathString:
                        self._set_trs_port_raw_build_(
                            trsPortQueryraw,
                            srcPortpathString, tgtPortpathString_
                        )

    def _set_trs_port_raw_build_(self, trsPortQueryraw, srcPortpathString, tgtPortpathString):
        tgtPortQueryObject = self._tgtNodeQueryObj.port(tgtPortpathString)

        if self.DEF_grh_key_source_porttype in trsPortQueryraw:
            srcPorttypeString = trsPortQueryraw[self.DEF_grh_key_source_porttype]
        else:
            srcPorttypeString = tgtPortQueryObject.porttype

        tgtAssignString = tgtPortQueryObject.assign

        if tgtAssignString not in self.VAR_grh_trs_channel_keyword_list:
            trsChildPortQueryraws = self._trsPortChildRaws.get(srcPorttypeString, [])
            for trsChildPortQueryraw in trsChildPortQueryraws:
                self._set_trs_port_child_raw_build_(
                    trsChildPortQueryraw,
                    srcPortpathString, tgtPortpathString,
                    srcPorttypeString
                )

            self._set_trs_port_raw_add_(srcPortpathString, tgtPortpathString, tgtPortQueryObject)

    def _set_trs_port_child_raw_build_(self, trsPortQueryraw, srcParentPortpathString, tgtParentPortpathString, srcPorttypeString):
        srcFormatString = trsPortQueryraw[self.DEF_grh_keyword_format]
        tgtFormatString = trsPortQueryraw[self.DEF_grh_key_target_portpath][self.DEF_grh_keyword_format]

        if srcPorttypeString == self.DEF_grh_keyword_porttype_uv_1:
            srcPortpathString = srcFormatString.format(*[srcParentPortpathString, srcParentPortpathString[:-2]])
        else:
            srcPortpathString = srcFormatString.format(*[srcParentPortpathString])

        tgtPortpathString = tgtFormatString.format(*[tgtParentPortpathString])

        tgtPortQueryObject = self._tgtNodeQueryObj.port(tgtPortpathString)

        self._set_trs_port_raw_add_(srcPortpathString, tgtPortpathString, tgtPortQueryObject)

    def _set_trs_port_raw_add_(self, srcPortpath, tgtPortpath, tgtPortQueryObject):
        _dic = self.CLS_ordered_dict()

        _dic[self.DEF_grh_key_source_portpath] = srcPortpath
        _dic[self.DEF_grh_key_target_portpath] = tgtPortpath

        for _k, _v in tgtPortQueryObject.portQueryraw.items():
            _dic[_k] = _v

        self._outTrsRawDict[self.DEF_grh_key_source_port].append(_dic)

    def outTrsRaw(self):
        return self._outTrsRawDict


class Def_GrhTrsPortQuery(grhCfg.Utility):
    VAR_grh_portsep = None

    VAR_grh_trs_property_list = [
        grhCfg.Utility.DEF_grh_key_source_portpath,
        grhCfg.Utility.DEF_grh_key_target_portpath,
        grhCfg.Utility.DEF_grh_key_porttype,
        grhCfg.Utility.DEF_grh_key_portraw,
        grhCfg.Utility.DEF_grh_key_assign,
        grhCfg.Utility.DEF_grh_key_parent,
        grhCfg.Utility.DEF_grh_key_children
    ]

    def _initDefGrhTrsPortQuery(self, *args):
        self._trsPortQueryraw = args[0]

        self._set_trs_port_query_build_(self._trsPortQueryraw)

    def _set_trs_port_query_build_(self, *args):
        raw = args[0]
        for i in self.VAR_grh_trs_property_list:
            self.__dict__[i] = raw[i]

    @property
    def portsep(self):
        return self.VAR_grh_portsep

    @property
    def trsPortQueryraw(self):
        return self._trsPortQueryraw

    def __str__(self):
        _ = u''
        count = len(self.VAR_grh_trs_property_list)
        for seq, i in enumerate(self.VAR_grh_trs_property_list):
            _ += u'{}="{}"'.format(i, self.__dict__[i])
            if seq < (count - 1):
                _ += u', '

        return u'{}({})'.format(
            self.__class__.__name__,
            _
        )

    def __repr__(self):
        return self.__str__()


class Def_GrhTrsNodeQuery(grhCfg.Utility):
    CLS_grh_trs_port_query_set = None
    CLS_grh_trs_port_query = None

    VAR_grh_trs_property_list = [
        grhCfg.Utility.DEF_grh_key_source_category,
        grhCfg.Utility.DEF_grh_key_target_category,
        grhCfg.Utility.DEF_grh_key_type
    ]

    VAR_grh_param_assign_keyword_list = []
    VAR_grh_inparm_assign_keyword_list = []
    VAR_grh_otparm_assign_keyword_list = []

    VAR_grh_channel_assign_keyword_list = []

    def _initDefGrhTrsNodeQuery(self, *args):
        self._trsNodeQueryrawDict = args[0]
        self._srcPortpathDict = {}

        self._set_trs_node_query_build_(self._trsNodeQueryrawDict)
        self._set_trs_port_queries_build_(self._trsNodeQueryrawDict)

    def _set_trs_node_query_build_(self, *args):
        raw = args[0]

        for i in self.VAR_grh_trs_property_list:
            self.__dict__[i] = raw[i]

    def _set_trs_port_queries_build_(self, *args):
        raw = args[0]

        self._trsPortQuerySetObj = self.CLS_grh_trs_port_query_set(self)
        self._trsParamQuerySetObj = self.CLS_grh_trs_port_query_set(self)
        self._trsInparmQuerySetObj = self.CLS_grh_trs_port_query_set(self)
        self._trsOtparmQuerySetObj = self.CLS_grh_trs_port_query_set(self)

        portRaws = raw[self.DEF_grh_key_source_port]
        for i in portRaws:
            self._set_trs_port_query_build_(i)

    def _set_trs_port_query_build_(self, *args):
        raw = args[0]

        obj = self.CLS_grh_trs_port_query(raw)

        portpathString = raw[self.DEF_grh_key_portpath]

        portnameString = portpathString.split(obj.portsep)[-1]
        self._srcPortpathDict[portnameString] = portpathString

        assignString = raw[self.DEF_grh_key_assign]
        if assignString in self.VAR_grh_param_assign_keyword_list:
            self._trsParamQuerySetObj._set_obj_add_(obj)
        if assignString in self.VAR_grh_inparm_assign_keyword_list:
            self._trsInparmQuerySetObj._set_obj_add_(obj)
        if assignString in self.VAR_grh_otparm_assign_keyword_list:
            self._trsOtparmQuerySetObj._set_obj_add_(obj)

        self._trsPortQuerySetObj._set_obj_add_(obj)

    # **************************************************************************************************************** #
    def _get_src_portpath_(self, *args):
        portpathString = args[0]
        if portpathString in self._srcPortpathDict:
            return self._srcPortpathDict[portpathString]
        return portpathString

    # **************************************************************************************************************** #
    def trsPorts(self):
        return self._trsPortQuerySetObj.objects()

    def hasTrsPort(self, *args):
        return self._trsPortQuerySetObj.hasObject(
            self._get_src_portpath_(*args)
        )

    def trsPort(self, *args):
        return self._trsPortQuerySetObj.object(
            self._get_src_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def trsParams(self):
        return self._trsParamQuerySetObj.objects()

    def hasTrsParam(self, *args):
        return self._trsParamQuerySetObj.hasObject(
            self._get_src_portpath_(*args)
        )

    def trsParam(self, *args):
        return self._trsParamQuerySetObj.object(
            self._get_src_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def trsInparms(self):
        return self._trsInparmQuerySetObj.objects()

    def hasTrsInparms(self, *args):
        return self._trsInparmQuerySetObj.hasObject(
            self._get_src_portpath_(*args)
        )

    def trsInparm(self, *args):
        return self._trsInparmQuerySetObj.object(
            self._get_src_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def trsOtparms(self):
        return self._trsOtparmQuerySetObj.objects()

    def hasTrsOtparm(self, *args):
        return self._trsOtparmQuerySetObj.hasObject(
            self._get_src_portpath_(*args)
        )

    def trsOtparm(self, *args):
        return self._trsOtparmQuerySetObj.object(
            self._get_src_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def TrsNodeQueryraw(self):
        return self._trsNodeQueryrawDict

    # **************************************************************************************************************** #
    @property
    def targetPortRaw(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh_key_target_port,
            {}
        )

    @property
    def mtlPortdataRaw(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh_key_target_portraw,
            {}
        )

    @property
    def customNode(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh_keyword_custom_node,
            {}
        )

    @property
    def createExpressionRaw(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh_keyword_create_expression,
            {}
        )

    @property
    def afterExpressionRaw(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh_keyword_after_expression,
            {}
        )


# cache
class Def_GrhTrsObjQueryCache(grhCfg.Utility):
    CLS_grh_trs_node_raw = None

    CLS_grh_trs_node_query_set = None
    CLS_grh_trs_node_query = None

    VAR_grh_trs_node_file = None
    VAR_grh_trs_geometry_file = None
    VAR_grh_trs_material_file = None
    VAR_grh_trs_output_file = None
    VAR_grh_trs_port_child_file = None

    VAR_grh_trs_custom_category_file = None
    VAR_grh_trs_custom_node_file = None

    OBJ_grh_query_cache = None

    # noinspection PyUnusedLocal
    def _initDefGrhTrsObjQueryCache(self, *args):
        self._trsNodeQuerySetObj = self.CLS_grh_trs_node_query_set(self)

        self._set_trs_node_queries_build_()

    # **************************************************************************************************************** #
    def _get_node_raw_(self, *args):
        categoryString = args[0]
        return self._outTrsNodeRawsDict[categoryString]

    def _get_node_exist_(self, *args):
        return self._trsNodeQuerySetObj.hasObject(*args)

    def _get_nodes_(self):
        return self._trsNodeQuerySetObj.objects()

    def _get_node_(self, *args):
        if self._trsNodeQuerySetObj._get_obj_exist_(*args):
            obj = self._trsNodeQuerySetObj._get_obj_(*args)
        else:
            raw = self._get_node_raw_(*args)
            obj = self.CLS_grh_trs_node_query(raw)
            self._trsNodeQuerySetObj._set_obj_add_(obj)
        return obj

    def trsNodes(self):
        return self._get_nodes_()

    def hasTrsNode(self, *args):
        return self._get_node_exist_(*args)

    def trsNode(self, *args):
        srcCategoryString = args[0]
        assert srcCategoryString in self._outTrsNodeRawsDict, u'''Source Category "{}" is Unregistered!!!'''.format(srcCategoryString)
        return self._get_node_(*args)

    # **************************************************************************************************************** #
    def srcCategories(self):
        return self._outTrsNodeRawsDict.keys()

    def hasSrcCategory(self, srcCategoryString):
        return srcCategoryString in self._outTrsNodeRawsDict

    def _set_trs_node_queries_build_(self):
        def getTrsNodeQueryFnc_(nodeRaws_):
            for _srcCategoryString, _trsNodeRaw in nodeRaws_.items():
                _tgtCategoryString = _trsNodeRaw[self.DEF_grh_key_target_category]
                _tgtNodeQueryObj = self.OBJ_grh_query_cache.node(_tgtCategoryString)

                trsRaw = self.CLS_grh_trs_node_raw(
                    _tgtNodeQueryObj,
                    _srcCategoryString,
                    _trsNodeRaw, self._trsOutputRaws, self._trsPortChildRaws
                ).outTrsRaw()

                _dccObjectDefObj = self.CLS_grh_trs_node_query(trsRaw)

                self._outTrsNodeRawsDict[_srcCategoryString] = trsRaw

        self._trsNodeRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_node_file
        ) or {}
        self._trsGeometryRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_geometry_file
        ) or {}
        self._trsMaterialRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_material_file
        ) or {}
        self._trsOutputRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_output_file
        ) or {}
        self._trsPortChildRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_port_child_file
        ) or {}

        self._trsCustomCategoryRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_custom_category_file
        ) or {}
        self._trsCustomNodeRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_custom_node_file
        ) or {}

        self._srcNodeRawDict = self.CLS_ordered_dict()

        self._outTrsNodeRawsDict = {}

        getTrsNodeQueryFnc_(self._trsNodeRaws)
        getTrsNodeQueryFnc_(self._trsMaterialRaws)
        getTrsNodeQueryFnc_(self._trsGeometryRaws)
        getTrsNodeQueryFnc_(self._trsCustomNodeRaws)


# object cache ******************************************************************************************************* #
class Def_GrhCacheObj(object):
    @classmethod
    def _mtd_get_cache_obj_(cls, cacheObject, objKeyString, objCls, clsArgs):
        if cacheObject._get_obj_exist_(objKeyString) is True:
            return cacheObject._get_obj_(objKeyString)
        #
        obj = objCls(*clsArgs)
        cacheObject._set_obj_add_(obj)
        return obj


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
            if isinstance(args[0], Def_GrhCacheObj):
                obj = args[0]
                return obj
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
    CLS_grh_obj_proxy_set = None

    # noinspection PyUnusedLocal
    def _initDefGrhObj(self, *args):
        # parent
        self._parentPathStr = None
        # children
        self._childPathStrList = []
        # proxy
        self._proxyObj = None

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

    def setParent(self, *args):
        self._set_parent_(*args)

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

    # **************************************************************************************************************** #
    def _set_proxy_obj_(self, obj):
        self._proxyObj = obj

    def proxy(self, *args):
        return self._proxyObj


class Def_GrhConnector(grhCfg.Utility):
    OBJ_grh_obj_cache = None

    def _initDefGrhConnector(self, *args):
        self._sourcePortIndex = None
        self._targetPortIndex = None

        self._set_connection_build_(*args)

    def _get_cache_obj_(self, *args):
        return self.OBJ_grh_obj_cache._get_obj_(*args)

    def _get_cache_obj_index_(self, *args):
        return self.OBJ_grh_obj_cache._get_obj_index_(*args)

    def _set_connection_build_(self, *args):
        sourceRaw, targetRaw = args
        self._sourcePortIndex = self._get_cache_obj_index_(sourceRaw)
        self._targetPortIndex = self._get_cache_obj_index_(targetRaw)

    def source(self):
        return self._get_cache_obj_(
            self._sourcePortIndex
        )

    def inparm(self):
        return self.source()

    def input(self):
        return self.source().node()

    def target(self):
        return self._get_cache_obj_(
            self._targetPortIndex
        )

    def otparm(self):
        return self.target()

    def output(self):
        return self.target().node()

    def insert(self, portObj):
        self.source()._set_port_target_add_(portObj)
        portObj._set_port_target_add_(self.target())

    def destroy(self):
        pass

    def __str__(self):
        return '{}(source="{}", target="{}")'.format(
            self.__class__.__name__,
            self.source().pathString(),
            self.target().pathString()
        )

    def __repr__(self):
        return self.__str__()


class Def_GrhPort(
    Def_GrhObj,
    Def_GrhCacheObj
):
    CLS_grh_type = None

    CLS_grh_porttype = None

    CLS_grh_attrpath = None
    CLS_grh_portpath = None

    VAR_grh_value_cls_dict = {}

    def _initDefGrhPort(self, *args):
        self._initDefGrhObj()

        nodeObject, _ = args[:2]
        # node
        self._nodeObj = nodeObject
        # port
        if isinstance(_, (str, unicode)):
            self._set_portpath_build_(_)
        if isinstance(_, Def_GrhPortQuery):
            self._set_port_build_(_)
        # source
        self._sourcePortIndex = None
        # target
        self._targetPortIndexList = []

    def _get_cache_obj_(self, *args):
        return self._nodeObj.OBJ_grh_obj_cache._get_obj_(*args)

    def _get_cache_obj_index_(self, *args):
        return self._nodeObj.OBJ_grh_obj_cache._get_obj_index_(*args)

    # **************************************************************************************************************** #
    def _set_port_build_(self, *args):
        portQueryObject = args[0]

        porttypeString = portQueryObject.porttype

        self._set_portpath_build_(portQueryObject.portpath)
        self._set_attrpath_build_(self._nodeObj.nodepath(), self.portpath())

        self._set_type_build_(portQueryObject.assign)
        self._set_porttype_build_(porttypeString)

        self._set_parent_(portQueryObject.parent)
        self._set_children_(portQueryObject.children)

        valueCls = self._get_value_cls_(porttypeString)
        if valueCls is not None:
            portrawString = portQueryObject.portraw
            self._set_value_(
                valueCls(portrawString)
            )
            self._set_default_value_(
                valueCls(portrawString)
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
    def _set_type_build_(self, *args):
        self._typeObj = self.CLS_grh_type(*args)

    def type(self):
        return self._typeObj

    def typeString(self):
        return self._typeObj.toString()

    # **************************************************************************************************************** #
    def _set_porttype_build_(self, *args):
        self._porttypeObj = self.CLS_grh_porttype(*args)

    def porttype(self):
        return self._porttypeObj

    def porttypeString(self):
        return self._porttypeObj.toString()

    # **************************************************************************************************************** #
    def _set_portpath_build_(self, *args):
        self._portpathObj = self.CLS_grh_portpath(*args)

    def portpath(self):
        return self._portpathObj

    def portpathString(self):
        return self._portpathObj.toString()

    def portname(self):
        return self._portpathObj.bscname()

    def portnameString(self):
        return self._portpathObj.bscnameString()

    # **************************************************************************************************************** #
    def _set_attrpath_build_(self, *args):
        self._attrpathObj = self.CLS_grh_attrpath(*args)

    def attrpath(self):
        return self._attrpathObj

    def attrpathString(self):
        return self._attrpathObj.toString()

    # **************************************************************************************************************** #
    def path(self):
        return self._attrpathObj

    def pathString(self):
        return self._attrpathObj.toString()

    def name(self):
        return self._portpathObj.bscname()

    def nameString(self):
        return self._portpathObj.bscnameString()

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
    def _get_portraw_(self, *args):
        return self._valueObj.raw()

    def _get_portrawstr_(self, *args):
        return self._valueObj.rawString()

    def _set_portraw_(self, *args):
        self._valueObj.setRaw(*args)

    def _set_portrawstr_(self, *args):
        self._valueObj.setRawString(*args)

    def setPortraw(self, *args):
        self._set_portraw_(*args)

    def setPortrawString(self, *args):
        self._set_portrawstr_(*args)

    def portraw(self, *args):
        return self._get_portraw_(*args)

    def portrawString(self):
        return self._get_portrawstr_()

    def isChanged(self):
        return self.isValueChanged() or self.hasSource()

    # **************************************************************************************************************** #
    def _get_is_source_(self, *args):
        return self._get_port_target_exist_(*args)

    def _get_port_source_exist_(self, *args):
        if args:
            return self._get_cache_obj_index_(args[0]) == self._sourcePortIndex
        return self._sourcePortIndex is not None

    def _get_source_(self):
        if self._get_port_source_exist_() is True:
            return self._get_cache_obj_(
                self._sourcePortIndex
            )

    def isSource(self):
        return self._get_is_source_()

    def hasSource(self):
        return self._get_port_source_exist_()

    def source(self):
        return self._get_source_()

    # **************************************************************************************************************** #
    def _get_is_target_(self):
        return self._get_port_source_exist_()

    def _get_targets_exist_(self):
        return self._targetPortIndexList != []

    def _get_targets_(self):
        return [
            self._get_cache_obj_(i)
            for i in self._targetPortIndexList
        ]

    def _get_port_target_exist_(self, *args):
        if args:
            index = self._get_cache_obj_index_(*args)
            if index is not None:
                return index in self._targetPortIndexList
            return False
        return self._targetPortIndexList != []

    def _get_target_(self, *args):
        if isinstance(args[0], (int, float)):
            index = args[0]
            if index in self._targetPortIndexList:
                objIndex = self._targetPortIndexList[index]
                return self._get_cache_obj_(objIndex)

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

    def insertTarget(self, *args):
        inparmObj, otparmObj = args

        for i in self.targets():
            otparmObj.connectTo(i)
        self.connectTo(inparmObj)

    # **************************************************************************************************************** #
    def _set_port_target_add_(self, *args):
        obj = args[0]

        # destroy old
        index = self._get_cache_obj_index_(obj)
        if obj.hasSource():
            sourceObject = obj.source()
            if index in sourceObject._targetPortIndexList:
                sourceObject._targetPortIndexList.remove(index)
        # connect new
        if index not in self._targetPortIndexList:
            self._targetPortIndexList.append(index)
            obj._set_port_source_(self)

    def connectTo(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: None
        """
        self._set_port_target_add_(*args)

    def isConnectTo(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: bool
        """
        return self._get_port_target_exist_(*args)

    # **************************************************************************************************************** #
    def _set_port_source_(self, *args):
        obj = args[0]
        if self._get_port_source_exist_(obj) is False:
            self._sourcePortIndex = self._get_cache_obj_index_(obj)
            obj._set_port_target_add_(self)

    def connectFrom(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: None
        """
        self._set_port_source_(*args)

    def isConnectFrom(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: bool
        """
        return self._get_port_source_exist_(*args)

    # **************************************************************************************************************** #
    def _get_port_given_(self):
        if self.hasSource() is True:
            return self.source()
        return self.value()

    def portgiven(self):
        return self._get_port_given_()

    # **************************************************************************************************************** #
    def isChannel(self):
        return self.hasParent()

    # **************************************************************************************************************** #
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


class Def_GrhNode(
    Def_GrhObj,
    Def_GrhCacheObj
):
    CLS_grh_type = None
    CLS_grh_category = None

    CLS_grh_nodepath = None

    CLS_grh_port_set = None
    VAR_grh_port_cls_dict = {}

    CLS_grh_connector = None

    VAR_grh_param_assign_keyword_list = []
    VAR_grh_inparm_assign_keyword_list = []
    VAR_grh_otparm_assign_keyword_list = []

    VAR_grh_channel_assign_keyword_list = []

    OBJ_grh_query_cache = None
    OBJ_grh_obj_cache = None

    def _initDefGrhNode(self, *args):
        self._initDefGrhObj()

        categoryString, nodepathString = args[:2]
        self._nodeQueryObj = self.OBJ_grh_query_cache.node(
            categoryString
        )

        self._set_nodepath_build_(nodepathString)

        self._set_node_build_(self._nodeQueryObj)

        self.OBJ_grh_obj_cache._set_obj_add_(self)

        self._set_ports_build_(self._nodeQueryObj)

    # **************************************************************************************************************** #
    def _set_node_build_(self, *args):
        nodeQueryObject = args[0]

        self._set_type_build_(nodeQueryObject.type)
        self._set_category_build_(nodeQueryObject.category)

    # **************************************************************************************************************** #
    def _set_type_build_(self, *args):
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
    def _set_category_build_(self, *args):
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

    # **************************************************************************************************************** #
    def _set_nodepath_build_(self, *args):
        self._nodepathObj = self.CLS_grh_nodepath(*args)

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

    # **************************************************************************************************************** #
    def path(self):
        return self._nodepathObj

    def pathString(self):
        return self._nodepathObj.toString()

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

    # **************************************************************************************************************** #
    def _get_port_cls_(self, *args):
        assignString = args[0]
        if assignString in self.VAR_grh_port_cls_dict:
            return self.VAR_grh_port_cls_dict[assignString]

    def _set_ports_build_(self, *args):
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
                    if _assignString in self.VAR_grh_param_assign_keyword_list:
                        self._paramSetObj._set_obj_add_(_portObject)
                    if _assignString in self.VAR_grh_inparm_assign_keyword_list:
                        self._inparmSetObj._set_obj_add_(_portObject)
                    if _assignString in self.VAR_grh_otparm_assign_keyword_list:
                        self._otparmSetObj._set_obj_add_(_portObject)
                    self._portSetObj._set_obj_add_(_portObject)

        nodeQueryObject = args[0]

        self._portSetObj = self.CLS_grh_port_set(self)
        self._paramSetObj = self.CLS_grh_port_set(self)
        self._inparmSetObj = self.CLS_grh_port_set(self)
        self._otparmSetObj = self.CLS_grh_port_set(self)

        for i in nodeQueryObject.ports():
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

    @classmethod
    def _mtd_get_changed_ports_(cls, *args):
        def addFnc_(portObject_):
            if portObject_ not in lis:
                lis.append(portObject_)

        portObjects = args[0]
        lis = []
        for i in portObjects:
            if i.isChanged() is True:
                addFnc_(i)
        return lis

    def changedPorts(self):
        return self._mtd_get_changed_ports_(
            self._portSetObj.objects()
        )

    # **************************************************************************************************************** #
    def params(self):
        return self._paramSetObj.objects()

    def hasParam(self, *args):
        return self._paramSetObj.hasObject(*args)

    def param(self, *args):
        return self._paramSetObj.object(*args)

    def changedParams(self):
        return self._mtd_get_changed_ports_(
            self._paramSetObj.objects()
        )

    # **************************************************************************************************************** #
    def inparms(self):
        return self._inparmSetObj.objects()

    def hasInparm(self, *args):
        return self._inparmSetObj.hasObject(*args)

    def inparm(self, *args):
        return self._inparmSetObj.object(*args)

    def changedInparm(self):
        """
        :return: list
        """
        return self._mtd_get_changed_ports_(
            self._inparmSetObj.objects()
        )

    # **************************************************************************************************************** #
    def otparms(self):
        return self._otparmSetObj.objects()

    def hasOtparm(self, *args):
        return self._otparmSetObj.hasObject(*args)

    def otparm(self, *args):
        if args:
            portpathString = args[0]
            return self._otparmSetObj.object(portpathString)
        return self._otparmSetObj.objects()[-1]

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
    def inputConnections(self):
        lis = []
        for inparmObject in self.inparms():
            if inparmObject.hasSource():
                sourceObject = inparmObject.source()
                connection = (sourceObject, inparmObject)
                if connection not in lis:
                    lis.append(connection)
        return lis

    def inputConnectors(self):
        return [
            self.CLS_grh_connector(*i)
            for i in self.inputConnections()
        ]

    def outputConnections(self):
        lis = []
        for otparmObject in self.otparms():
            if otparmObject.hasTargets():
                for targetObject in otparmObject.targets():
                    connection = (otparmObject, targetObject)
                    if connection not in lis:
                        lis.append(connection)
        return lis

    def outputConnectors(self):
        return [
            self.CLS_grh_connector(*i)
            for i in self.outputConnections()
        ]

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


# object proxy ******************************************************************************************************* #
class Def_GrhObjProxy(grhCfg.Utility):
    CLS_grh_name = None

    def _initDefGrhObjProxy(self, *args):
        if isinstance(args[0], Def_GrhObj):
            self._nameObj = self.CLS_grh_name(args[0].toString())
        elif isinstance(args[0], (str, unicode)):
            self._nameObj = self.CLS_grh_name(args[0])
        else:
            raise ValueError(u'argument must be raw of "str / unicode"; object of "Port"; object or "Node"')

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def setNameString(self, *args):
        self._nameObj.setRawString(*args)


class Def_GrhPortProxy(Def_GrhObjProxy):
    def _initDefGrhPortProxy(self, *args):
        self._initDefGrhObjProxy(*args)

        self._set_port_proxy_build_(*args)

        self._nodeGraphOutputObj = None

    def _set_port_proxy_build_(self, *args):
        self._portObj = args[0]
        self._portObj._set_proxy_obj_(self)

    # **************************************************************************************************************** #
    def port(self):
        return self._portObj

    def _set_node_graph_output_(self, *args):
        self._nodeGraphOutputObj = args[0]

    def connectNodeGraphOutput(self, *args):
        self._set_node_graph_output_(*args)

    def nodeGraphOutput(self):
        return self._nodeGraphOutputObj


class Def_GrhNodeProxy(Def_GrhObjProxy):
    CLS_grh_node = None

    CLS_grh_node_graph_set = None
    CLS_grh_node_graph = None

    CLS_grh_port_proxy_set = None
    VAR_grh_port_proxy_cls_dict = {}

    def _initDefGrhNodeProxy(self, *args):
        self._initDefGrhObjProxy(*args)

        self._set_node_proxy_build_(*args)
        self._set_port_proxies_build_()

        self._set_node_graph_build_()

    def _set_node_proxy_build_(self, *args):
        if isinstance(args[0], Def_GrhNode):
            self._nodeObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            self._nodeObj = self.CLS_grh_node(*args)

        self._nodeObj._set_proxy_obj_(self)

    # **************************************************************************************************************** #
    def _get_port_proxy_cls_(self, *args):
        assignString = args[0]
        if assignString in self.VAR_grh_port_proxy_cls_dict:
            return self.VAR_grh_port_proxy_cls_dict[assignString]

    def _set_port_proxies_build_(self):
        def fnc_(portObjs_, setObj_):
            for _i in portObjs_:
                assignString = _i.typeString()
                _portProxyCls = self._get_port_proxy_cls_(assignString)
                if _portProxyCls is not None:
                    _portProxyObject = _portProxyCls(_i)
                    setObj_._set_obj_add_(_portProxyObject)

        self._portProxySetObj = self.CLS_grh_port_proxy_set(self)
        self._paramProxySetObj = self.CLS_grh_port_proxy_set(self)
        self._inputProxySetObj = self.CLS_grh_port_proxy_set(self)
        self._outputProxySetObj = self.CLS_grh_port_proxy_set(self)

        for portObjs, setObj in [
            (self._nodeObj.ports(), self._portProxySetObj),
            (self._nodeObj.params(), self._paramProxySetObj),
            (self._nodeObj.inparms(), self._inputProxySetObj),
            (self._nodeObj.otparms(), self._outputProxySetObj)
        ]:
            fnc_(portObjs, setObj)

    # **************************************************************************************************************** #
    def _set_node_graph_build_(self):
        self._nodeGraphSetObj = self.CLS_grh_node_graph_set(self)

    # **************************************************************************************************************** #
    def node(self):
        return self._nodeObj

    # **************************************************************************************************************** #
    def _set_node_graph_obj_add_(self, *args):
        nodeObject = args[0]
        nodeGraphObject = self.CLS_grh_node_graph(nodeObject)
        self._nodeGraphSetObj.addObject(nodeGraphObject)

    def _get_node_graph_obj_(self, *args):
        if isinstance(args[0], (str, unicode)):
            keyString = args[0]
            if self._nodeGraphSetObj._get_obj_exist_(keyString):
                return self._nodeGraphSetObj._get_obj_(keyString)
        elif isinstance(args[0], (int, float)):
            index = args[0]
            if self._nodeGraphSetObj._get_obj_exist_(index):
                return self._nodeGraphSetObj._get_obj_(index)
        #
        elif isinstance(args[0], Def_GrhNode):
            obj = args[0]
            keyString = obj.toString()
            if self._nodeGraphSetObj._get_obj_exist_(keyString) is False:
                self._set_node_graph_obj_add_(obj)
            return self._nodeGraphSetObj._get_obj_(keyString)
        elif isinstance(args[0], Def_GrhNodeProxy):
            obj = args[0]
            keyString = obj.nameString()
            if self._nodeGraphSetObj._get_obj_exist_(keyString) is False:
                self._set_node_graph_obj_add_(obj.node())
            return self._nodeGraphSetObj._get_obj_(keyString)

    def addNodeGraph(self, *args):
        self._set_node_graph_obj_add_(*args)

    def hasNodeGraphs(self):
        return self._nodeGraphSetObj.hasObjects()

    def hasNodeGraph(self, *args):
        return self._nodeGraphSetObj.hasObject(*args)

    def nodeGraph(self, *args):
        return self._get_node_graph_obj_(*args)

    def nodeGraphs(self):
        return self._nodeGraphSetObj.objects()

    # **************************************************************************************************************** #
    def bindPorts(self):
        return self._portProxySetObj.objects()

    def hasBindPort(self, *args):
        return self._portProxySetObj.hasObject(*args)

    def bindPort(self, *args):
        return self._portProxySetObj.object(*args)

    # **************************************************************************************************************** #
    def bindParams(self):
        return self._paramProxySetObj.objects()

    def hasBindParam(self, *args):
        return self._paramProxySetObj.hasObject(*args)

    def bindParam(self, *args):
        return self._paramProxySetObj.object(*args)

    # **************************************************************************************************************** #
    def _get_changed_bind_inputs_(self):
        lis = []
        portProxyObjects = self.bindInputs()
        if portProxyObjects:
            for i in portProxyObjects:
                portObject = i.port()
                if portObject.isChanged():
                    lis.append(i)
        return lis

    def bindInput(self, *args):
        return self._inputProxySetObj.object(*args)

    def hasBindInput(self, *args):
        return self._inputProxySetObj.hasObject(*args)

    def bindInputs(self):
        return self._inputProxySetObj.objects()

    def changedBindInputs(self):
        return self._get_changed_bind_inputs_()

    # **************************************************************************************************************** #
    def bindOutputs(self):
        return self._outputProxySetObj.objects()

    def hasBindOutput(self, *args):
        return self._outputProxySetObj.hasObject(*args)

    def bindOutput(self, *args):
        return self._outputProxySetObj.object(*args)

    # **************************************************************************************************************** #
    def toString(self):
        return self._nodeObj.nodepathString()


# node graph ********************************************************************************************************* #
class Def_GrhNodeGraph(grhCfg.Utility):
    CLS_grh_name = None

    CLS_grh_node_set = None

    CLS_grh_node_graph_output_set = None
    CLS_grh_node_graph_output = None

    def _initDefGrhNodeGraph(self, *args):
        self._set_node_graph_build_(*args)

    def _set_node_graph_build_(self, *args):
        self._obj = args[0]

        self._nameObj = self.CLS_grh_name(
            self._obj.toString()
        )

        self._nodeSetObj = self.CLS_grh_node_set(self)
        self._nodeGraphOutputSetObj = self.CLS_grh_node_graph_output_set(self)

    def _get_source_nodes_(self):
        return self._obj.allSourceNodes()

    def _get_source_ports_(self):
        lis = []
        for i in self._obj.inparms():
            if i.hasSource():
                lis.append(i)
        return lis

    def _set_node_graph_update_(self):
        self._nodeSetObj._set_obj_set_data_int_()
        self._nodeGraphOutputSetObj._set_obj_set_data_int_()

        [self._set_node_add_(i) for i in self._get_source_nodes_()]
        [self._set_output_add_(i) for i in self._get_source_ports_()]

    def _set_node_add_(self, *args):
        nodeObject = args[0]

        if self._nodeSetObj._get_obj_exist_(nodeObject) is False:
            self._nodeSetObj.addObject(nodeObject)

    def _set_output_add_(self, *args):
        portObject = args[0]

        sourceObject = portObject.source()
        count = self._nodeGraphOutputSetObj.objectCount()

        keyString = sourceObject.attrpathString()
        if self._nodeGraphOutputSetObj._get_obj_exist_(keyString) is False:
            nameString = u'output_{}'.format(count)
            nodeGraphOutputObject = self.CLS_grh_node_graph_output(sourceObject)
            nodeGraphOutputObject.setNameString(nameString)
            nodeGraphOutputObject.setNodeGraph(self)
            self._nodeGraphOutputSetObj._set_obj_add_(keyString, nodeGraphOutputObject)
        else:
            nodeGraphOutputObject = self._nodeGraphOutputSetObj._get_obj_(keyString)

        portObject.proxy().connectNodeGraphOutput(
            nodeGraphOutputObject
        )

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

    # **************************************************************************************************************** #
    def nodes(self):
        """
        :return: list([<Node>, ...])
        """
        return self._nodeSetObj.objects()

    def node(self, nodepathString):
        """
        :param nodepathString: str("nodepathString")
        :return: <Node>
        """
        return self._nodeSetObj._get_obj_(nodepathString)

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

    # **************************************************************************************************************** #
    def outputs(self):
        """
        :return: list(object or output, ...)
        """
        return self._nodeGraphOutputSetObj.objects()

    def hasOutput(self, *args):
        return self._nodeGraphOutputSetObj.hasObject(*args)

    def output(self, *args):
        """
        :param args:
            1: str
        :return: object of Output
        """
        return self._nodeGraphOutputSetObj.object(*args)

    def hasOutputs(self):
        """
        :return: bool
        """
        return self._nodeGraphOutputSetObj.hasObjects()

    def outputCount(self):
        return self._nodeGraphOutputSetObj.objectCount()


class Def_GrhNodeGraphOutput(Def_GrhObjProxy):
    def _initDefGrhNodeGraphOutput(self, *args):
        self._set_node_graph_output_build_(*args)

    def _set_node_graph_output_build_(self, *args):
        self._portObj = args[0]

        self._initDefGrhObjProxy(self._portObj.toString())

        self._nodeGraphObj = None

    # **************************************************************************************************************** #
    def port(self):
        return self._portObj

    # **************************************************************************************************************** #
    def _set_node_graph_(self, *args):
        self._nodeGraphObj = args[0]

    def setNodeGraph(self, *args):
        self._set_node_graph_(*args)

    def nodeGraph(self):
        return self._nodeGraphObj
