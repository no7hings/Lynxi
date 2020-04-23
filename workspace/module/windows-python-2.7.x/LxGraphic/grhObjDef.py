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
class Def_GrhPortQueryraw(grhCfg.Utility):
    def _initDefGrhPortQueryraw(self, *args):
        self._outPortRawDict = args[0]

        self._set_port_queryraw_property_build_(self._outPortRawDict)

    def _set_port_queryraw_property_build_(self, *args):
        raw = args[0]
        for k, v in raw.items():
            self.__dict__[k] = raw[k]

    def outPortRaw(self):
        return self._outPortRawDict


class Def_GrhNodeQueryraw(grhCfg.Utility):
    CLS_grh_port_queryraw_set = None
    CLS_grh_port_queryraw = None

    def _initDefGrhNodeQueryraw(self, *args):
        if len(args) == 2:
            self._categoryString, self._outNodeRawDict = args
        else:
            (
                self._categoryString,
                self._nodeRaw, self._otparmRawDict, self._portChildRawDict
            ) = args

            self._outNodeRawDict = self.CLS_ordered_dict()

            self._set_node_raw_build_(self._nodeRaw)

        self._set_node_property_build_(self._outNodeRawDict)

        self._set_node_port_queryraw_build_(
            self._outNodeRawDict[self.DEF_grh_key_port]
        )

    # **************************************************************************************************************** #
    def _set_node_property_build_(self, *args):
        raw = args[0]
        for k, v in raw.items():
            self.__dict__[k] = raw[k]

    def _set_node_port_queryraw_build_(self, *args):
        raw = args[0]

        self._portQueryrawObjSet = self.CLS_grh_port_queryraw_set(self)
        for i in raw:
            portQueryrawObject = self.CLS_grh_port_queryraw(i)
            self._portQueryrawObjSet._set_obj_add_(portQueryrawObject)

    # **************************************************************************************************************** #
    def _set_node_raw_build_(self, nodeRaw):
        _typeString = nodeRaw[self.DEF_grh_key_type]
        # property
        self._outNodeRawDict[self.DEF_grh_key_type] = _typeString
        self._outNodeRawDict[self.DEF_grh_key_category] = self._categoryString
        # port
        self._outNodeRawDict[self.DEF_grh_key_port] = []

        _portRawList = nodeRaw[self.DEF_grh_key_port]
        self._set_port_raws_build_(_portRawList)

        _otparmRawList = self._otparmRawDict.get(_typeString, [])
        self._set_port_raws_build_(_otparmRawList)

    def _set_port_raws_build_(self, portRaws):
        for i in portRaws:
            self._set_port_raw_build_(i)

    def _set_port_raw_build_(self, portRaw):
        _portpathString = portRaw[self.DEF_grh_key_portpath]
        _porttypeString = portRaw[self.DEF_grh_key_porttype]
        _portrawString = portRaw[self.DEF_grh_key_portraw]
        _assignString = portRaw[self.DEF_grh_key_assign]

        _childPathStrList = []
        childPortQueryraws = self._portChildRawDict.get(_porttypeString, [])
        for seq, childPortRaw in enumerate(childPortQueryraws):
            childPortpathString = self._set_port_child_raw_build_(
                portRaw, childPortRaw,
                seq
            )
            if childPortpathString is not None:
                _childPathStrList.append(childPortpathString)

        self._set_port_raw_add_(_portpathString, _porttypeString, _portrawString, _assignString, None, _childPathStrList)

    def _set_port_child_raw_build_(self, parentPortRaw, portRaw, childIndex):
        parentPortpathString = parentPortRaw[self.DEF_grh_key_portpath]
        parentPorttypeString = parentPortRaw[self.DEF_grh_key_porttype]
        parentPortrawString = parentPortRaw[self.DEF_grh_key_portraw]
        parentAssignString = parentPortRaw[self.DEF_grh_key_assign]

        _formatString = portRaw[self.DEF_grh_keyword_format]

        _portpathString = _formatString.format(*[parentPortpathString])
        _porttypeString = portRaw[self.DEF_grh_key_porttype]

        if parentPortrawString:
            _portrawString = parentPortrawString.split(u',')[childIndex].rstrip().lstrip()
        else:
            _portrawString = portRaw[self.DEF_grh_key_portraw]

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
        outPortRaw = self.CLS_ordered_dict()

        outPortRaw[self.DEF_grh_key_portpath] = portpath
        outPortRaw[self.DEF_grh_key_porttype] = porttype
        outPortRaw[self.DEF_grh_key_portraw] = portraw
        outPortRaw[self.DEF_grh_key_assign] = assign
        outPortRaw[self.DEF_grh_key_parent] = parent
        outPortRaw[self.DEF_grh_key_children] = children

        self._outNodeRawDict[self.DEF_grh_key_port].append(outPortRaw)

    # **************************************************************************************************************** #
    def outNodeRaw(self):
        return self._outNodeRawDict

    # **************************************************************************************************************** #
    def portQueryraws(self):
        return self._portQueryrawObjSet.objects()

    def hasPortQueryraw(self, *args):
        return self._portQueryrawObjSet.hasObject(*args)

    def portQueryraw(self, *args):
        if self.hasPortQueryraw(*args):
            return self._portQueryrawObjSet.object(*args)

    def outPortRaw(self, *args):
        if self.hasPortQueryraw(*args):
            return self._portQueryrawObjSet.object(*args).outPortRaw()


class Def_GrhObjQueryrawCache(grhCfg.Utility):
    CLS_grh_node_queryraw = None

    CLS_grh_node_queryraw_set = None

    VAR_grh_node_file = None
    VAR_grh_geometry_file = None
    VAR_grh_material_file = None
    VAR_grh_output_file = None
    VAR_grh_port_child_file = None

    # noinspection PyUnusedLocal
    def _initDefGrhObjQueryrawCache(self, *args):
        self._nodeQueryrawSetObj = self.CLS_grh_node_queryraw_set(self)

        self._set_node_queries_build_()

    def _set_node_queries_build_(self):
        pass

    # **************************************************************************************************************** #
    def _get_node_type_(self, *args):
        """
        replace method
        """

    # **************************************************************************************************************** #
    @classmethod
    def _mtd_get_queryraw_(cls, *args):
        setObj, getObjMtd, keyArgs = args
        if setObj._get_obj_exist_(*keyArgs):
            obj = setObj._get_obj_(*keyArgs)
        else:
            obj = getObjMtd(*keyArgs)
            setObj._set_obj_add_(obj)
        return obj

    # **************************************************************************************************************** #
    def _get_node_queryraw_obj_(self, *args):
        pass

    def _get_node_queryraw_(self, *args):
        return self._mtd_get_queryraw_(
            self._nodeQueryrawSetObj,
            self._get_node_queryraw_obj_,
            args
        )

    def nodeQueryraw(self, *args):
        """
        :param args:
            1 args: ( str( "category" ), )
        :return: objects.NodeQueryraw
        """
        return self._get_node_queryraw_(*args)

    # **************************************************************************************************************** #
    def _get_port_raw_(self, *args):
        categoryString, portpathString = args
        nodeQueryrawObject = self._get_node_queryraw_(categoryString)
        return nodeQueryrawObject.outPortRaw(portpathString)

    def _get_port_queryraw_obj_(self, *args):
        categoryString, portpathString = args
        portRaw = self._get_port_raw_(categoryString, portpathString)
        return self.CLS_grh_node_queryraw.CLS_grh_port_queryraw(portRaw)

    def _get_port_queryraw(self, *args):
        categoryString, portpathString = args
        if self.hasCategory(categoryString):
            nodeQueryrawObject = self._get_node_queryraw_(categoryString)
            return nodeQueryrawObject.portQueryraw(portpathString)
        return self._get_port_queryraw_obj_(
            categoryString, portpathString
        )

    def portQueryraw(self, *args):
        """
        :param args:
            1 args: ( str( "category" ), str( "portpath" ) )
        :return: objects.NodeQueryraw
        """
        return self._get_port_queryraw(*args)

    # **************************************************************************************************************** #
    def _get_category_exist_(self, *args):
        pass

    def _get_categories_(self):
        pass

    def categories(self):
        return self._get_categories_()

    def hasCategory(self, *args):
        return self._get_category_exist_(*args)


# object query ******************************************************************************************************* #
class Def_GrhPortQuery(grhCfg.Utility):
    VAR_grh_portsep = None

    OBJ_grh_queryraw_cache = None

    def _initDefGrhPortQuery(self, *args):
        # build
        if args:
            if isinstance(args[0], Def_GrhNodeQueryraw):
                self._nodeQueryrawObj, self._portQueryrawObj = args
            # query
            elif isinstance(args[0], (str, unicode)):
                categoryString, portpathString = args
                self._nodeQueryrawObj, self._portQueryrawObj = (
                    self.OBJ_grh_queryraw_cache.nodeQueryraw(categoryString),
                    self.OBJ_grh_queryraw_cache.portQueryraw(categoryString, portpathString)
                )
            else:
                raise TypeError(
                    u'''argument must be: (objects.NodeQueryraw, objects.PortQueryraw); (str("category"), str("portpath"))'''
                )
        else:
            raise TypeError(
                u'''argument must not be empty'''
            )

        self._set_port_query_property_build_()

    def _set_port_query_property_build_(self):
        for k, v in self._portQueryrawObj.outPortRaw().items():
            self.__dict__[k] = v

    def nodeQueryraw(self):
        return self._nodeQueryrawObj

    def portQueryraw(self):
        return self._portQueryrawObj

    @property
    def portsep(self):
        return self.VAR_grh_portsep

    def __str__(self):
        return u'{}(category="{}", portpath="{}")'.format(
            self.__class__.__name__,
            self._nodeQueryrawObj.category,
            self._portQueryrawObj.portpath
        )

    def __repr__(self):
        return self.__str__()


class Def_GrhNodeQuery(grhCfg.Utility):
    CLS_grh_port_query_set = None
    CLS_grh_port_query = None

    VAR_grh_param_assign_keyword_list = []
    VAR_grh_inparm_assign_keyword_list = []
    VAR_grh_otparm_assign_keyword_list = []

    OBJ_grh_queryraw_cache = None

    def _initDefGrhNodeQuery(self, *args):
        if args:
            if isinstance(args[0], Def_GrhNodeQueryraw):
                self._nodeQueryrawObj = args[0]
            elif isinstance(args[0], (str, unicode)):
                categoryString = args[0]
                self._nodeQueryrawObj = self.OBJ_grh_queryraw_cache.nodeQueryraw(categoryString)
            else:
                raise TypeError(
                    u''''''
                )
        else:
            raise TypeError(
                u'''argument must not be empty'''
            )

        self._portpathDict = {}

        self._set_node_query_property_build_()
        self._set_port_queries_build_()

    def _set_node_query_property_build_(self):
        for k, v in self._nodeQueryrawObj.outNodeRaw().items():
            self.__dict__[k] = v

    def _set_port_queries_build_(self):
        self._portQuerySetObj = self.CLS_grh_port_query_set(self)
        self._paramQuerySetObj = self.CLS_grh_port_query_set(self)
        self._inparmQuerySetObj = self.CLS_grh_port_query_set(self)
        self._otparmQuerySetObj = self.CLS_grh_port_query_set(self)

        for portQueryrawObject in self._nodeQueryrawObj.portQueryraws():
            self._set_port_query_build_(portQueryrawObject)

    def _set_port_query_build_(self, *args):
        portQueryrawObject = args[0]

        portQueryObject = self.CLS_grh_port_query(
            self.nodeQueryraw(),
            portQueryrawObject
        )

        portpathString = portQueryrawObject.portpath
        portnameString = portpathString.split(portQueryObject.portsep)[-1]
        self._portpathDict[portnameString] = portpathString

        assignString = portQueryrawObject.assign
        if assignString in self.VAR_grh_param_assign_keyword_list:
            self._paramQuerySetObj._set_obj_add_(portQueryObject)
        if assignString in self.VAR_grh_inparm_assign_keyword_list:
            self._inparmQuerySetObj._set_obj_add_(portQueryObject)
        if assignString in self.VAR_grh_otparm_assign_keyword_list:
            self._otparmQuerySetObj._set_obj_add_(portQueryObject)

        self._portQuerySetObj._set_obj_add_(portQueryObject)

    # **************************************************************************************************************** #
    def _get_portpath_(self, *args):
        portpathString = args[0]
        if portpathString in self._portpathDict:
            return self._portpathDict[portpathString]
        return portpathString

    # **************************************************************************************************************** #
    def portQueries(self):
        return self._portQuerySetObj.objects()

    def hasPortQuery(self, *args):
        return self._portQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def portQuery(self, *args):
        return self._portQuerySetObj.object(
            self._get_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def paramQueries(self):
        return self._paramQuerySetObj.objects()

    def hasParamQuery(self, *args):
        return self._paramQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def paramQuery(self, *args):
        return self._paramQuerySetObj.object(
            self._get_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def inparmQueries(self):
        return self._inparmQuerySetObj.objects()

    def hasInparmQuery(self, *args):
        return self._inparmQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def inparmQuery(self, *args):
        return self._inparmQuerySetObj.object(
            self._get_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def otparmQueries(self):
        return self._otparmQuerySetObj.objects()

    def hasOtparmQuery(self, *args):
        return self._otparmQuerySetObj.hasObject(
            self._get_portpath_(*args)
        )

    def otparmQuery(self, *args):
        return self._otparmQuerySetObj.object(
            self._get_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def nodeQueryraw(self):
        return self._nodeQueryrawObj

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return u'{}(category="{}")'.format(
            self.__class__.__name__,
            self._nodeQueryrawObj.category
        )

    def __repr__(self):
        return self.__str__()


# translator object query cache ************************************************************************************** #
class Def_GrhTrsPortQueryraw(grhCfg.Utility):
    VAR_grh_trs_query_key = None

    def _initDefGrhPortQueryraw(self, *args):
        self._srcPortQueryrawObj, self._tgtPortQueryrawObj, self._outTrsPortRaw = args

        self._set_trs_port_queryraw_property_build_(self._outTrsPortRaw)

    def _set_trs_port_queryraw_property_build_(self, *args):
        raw = args[0]
        for k, v in raw.items():
            self.__dict__[k] = raw[k]

    # **************************************************************************************************************** #
    def outTrsPortRaw(self):
        return self._outTrsPortRaw

    # **************************************************************************************************************** #
    def srcPortQueryraw(self):
        return self._srcPortQueryrawObj

    def tgtPortQueryraw(self):
        return self._tgtPortQueryrawObj


class Def_GrhTrsNodeQueryraw(grhCfg.Utility):
    CLS_grh_trs_port_queryraw_set = None
    CLS_grh_trs_port_queryraw = None

    VAR_mtl_def_key_list = []

    VAR_grh_trs_port_key_dic = {
        grhCfg.Utility.DEF_grh_key_porttype: grhCfg.Utility.DEF_grh_key_target_porttype,
        grhCfg.Utility.DEF_grh_key_portraw: grhCfg.Utility.DEF_grh_key_target_portraw,
        grhCfg.Utility.DEF_grh_key_assign: grhCfg.Utility.DEF_grh_key_target_assign,
        grhCfg.Utility.DEF_grh_key_parent: grhCfg.Utility.DEF_grh_key_target_parent,
        grhCfg.Utility.DEF_grh_key_children: grhCfg.Utility.DEF_grh_key_target_children
    }

    def _initDefGrhTrsNodeQueryraw(self, *args):
        (
            self._srcNodeQueryrawObj, self._tgtNodeQueryrawObj,
            self._trsNodeRaws, self._trsOutputRaws, self._trsPortChildRawDict
        ) = args

        self._outTrsNodeRawDict = self.CLS_ordered_dict()

        self._set_trs_node_queryraw_build_()

        self._set_trs_node_queryraw_property_build_(self._outTrsNodeRawDict)

        self._set_trs_node_port_queryraw_build_(
            self._outTrsNodeRawDict[self.DEF_grh_key_source_port]
        )

    # **************************************************************************************************************** #
    def _set_trs_node_queryraw_property_build_(self, *args):
        raw = args[0]
        for k, v in raw.items():
            self.__dict__[k] = raw[k]

    def _set_trs_node_port_queryraw_build_(self, *args):
        raw = args[0]

        self._trsPortQueryrawObjSet = self.CLS_grh_trs_port_queryraw_set(self)
        for i in raw:
            srcPortpathString = i[self.DEF_grh_key_source_portpath]
            srcPortQueryrawObject = self._srcNodeQueryrawObj.portQueryraw(srcPortpathString)
            tgtPortpathString = i[self.DEF_grh_key_target_portpath]
            tgtPortQueryrawObject = self._tgtNodeQueryrawObj.portQueryraw(tgtPortpathString)

            trsPortQueryrawObject = self.CLS_grh_trs_port_queryraw(
                srcPortQueryrawObject, tgtPortQueryrawObject,
                i
            )
            self._trsPortQueryrawObjSet._set_obj_add_(trsPortQueryrawObject)

    # **************************************************************************************************************** #
    def _set_trs_node_queryraw_build_(self):
        self._srcCategoryString = self._srcNodeQueryrawObj.category
        self._tgtCategoryString = self._tgtNodeQueryrawObj.category

        self._tgtTypeString = self._tgtNodeQueryrawObj.type
        self._outTrsNodeRawDict[self.DEF_grh_key_source_category] = self._srcCategoryString
        self._outTrsNodeRawDict[self.DEF_grh_key_target_category] = self._tgtCategoryString

        self._outTrsNodeRawDict[self.DEF_grh_key_source_port] = []

        for _key in self.VAR_mtl_def_key_list:
            if _key in self._trsNodeRaws:
                self._outTrsNodeRawDict[_key] = self._trsNodeRaws[_key]

        trsPortQueryraws = self._trsNodeRaws[self.DEF_grh_key_source_port]
        self._set_trs_port_raws_build_(trsPortQueryraws)

        trsOutputQueryraws = self._trsOutputRaws.get(self._tgtTypeString, {})
        self._set_trs_port_raws_build_(trsOutputQueryraws)

    def _set_trs_port_raws_build_(self, trsPortRaws):
        for srcPortpathString, trsPortRaw in trsPortRaws.items():
            if self.DEF_grh_key_target_portpath in trsPortRaw:
                tgtPortpathString = trsPortRaw[self.DEF_grh_key_target_portpath]

                if isinstance(tgtPortpathString, (str, unicode)):
                    self._set_trs_port_raw_build_(
                        trsPortRaw,
                        srcPortpathString, tgtPortpathString
                    )

                elif isinstance(tgtPortpathString, (tuple, list)):
                    for tgtPortpathString_ in tgtPortpathString:
                        self._set_trs_port_raw_build_(
                            trsPortRaw,
                            srcPortpathString, tgtPortpathString_
                        )

    def _set_trs_port_raw_build_(self, trsPortRaw, srcPortpathString, tgtPortpathString):
        tgtPortQueryrawObject = self._tgtNodeQueryrawObj.portQueryraw(tgtPortpathString)

        if self.DEF_grh_key_source_porttype in trsPortRaw:
            srcPorttypeString = trsPortRaw[self.DEF_grh_key_source_porttype]
        else:
            srcPorttypeString = tgtPortQueryrawObject.porttype

        if tgtPortQueryrawObject.parent is None:
            trsChildPortRawList = self._trsPortChildRawDict.get(srcPorttypeString, [])
            for trsChildPortRaw in trsChildPortRawList:
                self._set_trs_port_child_raw_build_(
                    trsChildPortRaw,
                    srcPortpathString, tgtPortpathString,
                    srcPorttypeString
                )

            self._set_trs_port_raw_add_(srcPortpathString, tgtPortpathString, tgtPortQueryrawObject)

    def _set_trs_port_child_raw_build_(self, trsPortRaw, srcParentPortpathString, tgtParentPortpathString, srcPorttypeString):
        srcFormatString = trsPortRaw[self.DEF_grh_keyword_format]
        tgtFormatString = trsPortRaw[self.DEF_grh_key_target_portpath][self.DEF_grh_keyword_format]

        if srcPorttypeString == self.DEF_grh_keyword_porttype_uv_1:
            srcPortpathString = srcFormatString.format(*[srcParentPortpathString, srcParentPortpathString[:-2]])
        else:
            srcPortpathString = srcFormatString.format(*[srcParentPortpathString])

        tgtPortpathString = tgtFormatString.format(*[tgtParentPortpathString])

        tgtPortQueryrawObject = self._tgtNodeQueryrawObj.portQueryraw(tgtPortpathString)

        self._set_trs_port_raw_add_(srcPortpathString, tgtPortpathString, tgtPortQueryrawObject)

    def _set_trs_port_raw_add_(self, srcPortpath, tgtPortpath, tgtPortQueryrawObject):
        _dic = self.CLS_ordered_dict()

        _dic[self.DEF_grh_key_source_portpath] = srcPortpath
        _dic[self.DEF_grh_key_target_portpath] = tgtPortpath

        self._outTrsNodeRawDict[self.DEF_grh_key_source_port].append(_dic)

    # **************************************************************************************************************** #
    def trsPortQueryraws(self):
        return self._trsPortQueryrawObjSet.objects()

    def hasTrsPortQueryraw(self, *args):
        return self._trsPortQueryrawObjSet.hasObject(*args)

    def trsPortQueryraw(self, *args):
        if self.hasTrsPortQueryraw(*args):
            return self._trsPortQueryrawObjSet.object(*args)

    def outTrsPortRaw(self, *args):
        if self.hasTrsPortQueryraw(*args):
            return self._trsPortQueryrawObjSet.object(*args).outTrsPortRaw()

    # **************************************************************************************************************** #
    def outTrsNodeRaw(self):
        return self._outTrsNodeRawDict

    # **************************************************************************************************************** #
    def srcNodeQueryraw(self):
        raise self._srcNodeQueryrawObj

    def tgtNodeQueryraw(self):
        raise self._tgtNodeQueryrawObj


class Def_GrhTrsObjQueryrawCache(grhCfg.Utility):
    CLS_grh_trs_node_queryraw_set = None
    CLS_grh_trs_node_queryraw = None

    VAR_grh_trs_node_file = None
    VAR_grh_trs_geometry_file = None
    VAR_grh_trs_material_file = None
    VAR_grh_trs_output_file = None
    VAR_grh_trs_port_child_file = None

    VAR_grh_trs_custom_category_file = None
    VAR_grh_trs_custom_node_file = None

    OBJ_grh_src_queryraw_cache = None
    OBJ_grh_tgt_queryraw_cache = None

    # noinspection PyUnusedLocal
    def _initDefGrhTrsObjQueryCache(self, *args):
        self._trsNodeQueryrawSetObj = self.CLS_grh_trs_node_queryraw_set(self)

        self._set_trs_node_queries_build_()

    # **************************************************************************************************************** #
    def _set_trs_node_queries_build_(self):
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
        self._trsPortChildRawDict = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_port_child_file
        ) or {}

        self._trsCustomCategoryRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_custom_category_file
        ) or {}
        self._trsCustomNodeRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_trs_custom_node_file
        ) or {}

        self._trsNodeRawDict = {}

        for i in [
            self._trsNodeRaws, self._trsMaterialRaws, self._trsGeometryRaws, self._trsCustomNodeRaws
        ]:
            self._trsNodeRawDict.update(i)

    # **************************************************************************************************************** #
    @classmethod
    def _mtd_get_trs_queryraw_(cls, *args):
        setObj, getObjMtd, keyArgs = args
        if setObj._get_obj_exist_(*keyArgs):
            obj = setObj._get_obj_(*keyArgs)
        else:
            obj = getObjMtd(*keyArgs)
            setObj._set_obj_add_(obj)
        return obj

    def _get_trs_node_raw_(self, *args):
        srcCategoryString = args[0]
        if srcCategoryString in self._trsNodeRawDict:
            return self._trsNodeRawDict[srcCategoryString]

    def _get_trs_node_queryraw_obj_(self, *args):
        srcCategoryString = args[0]

        trsNodeRaw = self._get_trs_node_raw_(srcCategoryString)
        if trsNodeRaw:
            _tgtCategoryString = trsNodeRaw[self.DEF_grh_key_target_category]
            _srcNodeQueryrawObj = self.OBJ_grh_src_queryraw_cache.nodeQueryraw(srcCategoryString)
            _tgtNodeQueryrawObj = self.OBJ_grh_tgt_queryraw_cache.nodeQueryraw(_tgtCategoryString)
            return self.CLS_grh_trs_node_queryraw(
                _srcNodeQueryrawObj,
                _tgtNodeQueryrawObj,
                trsNodeRaw,
                self._trsOutputRaws, self._trsPortChildRawDict
            )
        else:
            print srcCategoryString

    def _get_trs_node_queryraw_(self, *args):
        return self._mtd_get_trs_queryraw_(
            self._trsNodeQueryrawSetObj,
            self._get_trs_node_queryraw_obj_,
            args
        )

    def trsNodeQueryraw(self, *args):
        return self._get_trs_node_queryraw_(*args)

    # **************************************************************************************************************** #
    def _get_trs_port_queryraw_(self, *args):
        srcCategoryString, srcPortpathString = args
        trsNodeQueryrawObject = self._get_trs_node_queryraw_(srcCategoryString)
        return trsNodeQueryrawObject.trsPortQueryraw(srcPortpathString)

    def trsPortQueryraw(self, *args):
        return self._get_trs_port_queryraw_(*args)

    # **************************************************************************************************************** #
    def _get_trs_source_category_exist_(self, *args):
        srcCategoryString = args[0]
        return srcCategoryString in self._trsNodeRawDict

    def _get_trs_source_categories_(self):
        return self._trsNodeRawDict.keys()

    def srcCategories(self):
        return self._get_trs_source_categories_()

    def hasSrcCategory(self, srcCategoryString):
        return self._get_trs_source_category_exist_(srcCategoryString)


# translator object query ******************************************************************************************** #
class Def_GrhTrsPortQuery(grhCfg.Utility):
    VAR_grh_portsep = None

    VAR_grh_trs_property_list = [
        grhCfg.Utility.DEF_grh_key_source_portpath,
        grhCfg.Utility.DEF_grh_key_target_portpath
    ]

    OBJ_grh_trs_queryraw_cache = None

    def _initDefGrhTrsPortQuery(self, *args):
        if isinstance(args[0], Def_GrhTrsPortQueryraw):
            self._trsPortQueryrawObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            srcCategoryString, srcPortpathString = args
            self._trsPortQueryrawObj = self.OBJ_grh_trs_queryraw_cache.trsPortQueryraw(
                srcCategoryString, srcPortpathString
            )
        else:
            raise TypeError()

        self._set_trs_port_query_build_()

    def _set_trs_port_query_build_(self):
        for i in self.VAR_grh_trs_property_list:
            self.__dict__[i] = self._trsPortQueryrawObj.__dict__[i]

    # **************************************************************************************************************** #
    def trsPortQueryraw(self):
        return self._trsPortQueryrawObj

    # **************************************************************************************************************** #
    @property
    def portsep(self):
        return self.VAR_grh_portsep

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

    VAR_grh_param_assign_keyword_list = []
    VAR_grh_inparm_assign_keyword_list = []
    VAR_grh_otparm_assign_keyword_list = []

    OBJ_grh_trs_queryraw_cache = None

    def _initDefGrhTrsNodeQuery(self, *args):
        if isinstance(args[0], Def_GrhTrsNodeQueryraw):
            self._trsNodeQueryrawObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            srcCategoryString = args[0]
            self._trsNodeQueryrawObj = self.OBJ_grh_trs_queryraw_cache.trsNodeQueryraw(
                srcCategoryString
            )
        else:
            raise TypeError()

        self._trsNodeQueryrawDict = self._trsNodeQueryrawObj.outTrsNodeRaw()

        self._srcPortpathDict = {}

        self._set_trs_node_query_property_build_()

        self._set_trs_port_queries_build_()

    def _set_trs_node_query_property_build_(self):
        for k, v in self._trsNodeQueryrawObj.outTrsNodeRaw().items():
            self.__dict__[k] = v

    def _set_trs_port_queries_build_(self):
        self._trsPortQuerySetObj = self.CLS_grh_trs_port_query_set(self)
        self._trsParamQuerySetObj = self.CLS_grh_trs_port_query_set(self)
        self._trsInparmQuerySetObj = self.CLS_grh_trs_port_query_set(self)
        self._trsOtparmQuerySetObj = self.CLS_grh_trs_port_query_set(self)

        for trsPortQueryrawObject in self._trsNodeQueryrawObj.trsPortQueryraws():
            self._set_trs_port_query_build_(trsPortQueryrawObject)

    def _set_trs_port_query_build_(self, *args):
        trsPortQueryrawObject = args[0]

        trsPortQueryObject = self.CLS_grh_trs_port_query(trsPortQueryrawObject)

        tgtPortQueryrawObject = trsPortQueryrawObject.tgtPortQueryraw()

        portpathString = tgtPortQueryrawObject.portpath

        portnameString = portpathString.split(trsPortQueryObject.portsep)[-1]
        self._srcPortpathDict[portnameString] = portpathString

        assignString = tgtPortQueryrawObject.assign
        if assignString in self.VAR_grh_param_assign_keyword_list:
            self._trsParamQuerySetObj._set_obj_add_(trsPortQueryObject)
        if assignString in self.VAR_grh_inparm_assign_keyword_list:
            self._trsInparmQuerySetObj._set_obj_add_(trsPortQueryObject)
        if assignString in self.VAR_grh_otparm_assign_keyword_list:
            self._trsOtparmQuerySetObj._set_obj_add_(trsPortQueryObject)

        self._trsPortQuerySetObj._set_obj_add_(trsPortQueryObject)

    # **************************************************************************************************************** #
    def _get_src_portpath_(self, *args):
        portpathString = args[0]
        if portpathString in self._srcPortpathDict:
            return self._srcPortpathDict[portpathString]
        return portpathString

    # **************************************************************************************************************** #
    def trsPortQueries(self):
        return self._trsPortQuerySetObj.objects()

    def hasTrsPortQuery(self, *args):
        return self._trsPortQuerySetObj.hasObject(
            self._get_src_portpath_(*args)
        )

    def trsPortQuery(self, *args):
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
            keyString, objCls, objClsArgs = args
            if self._objSetObj._get_obj_exist_(keyString) is True:
                return self._objSetObj._get_obj_(keyString)
            else:
                obj = objCls(*objClsArgs)
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
    CLS_grh_path = None

    # noinspection PyUnusedLocal
    def _initDefGrhObj(self, *args):
        # parent
        self._parentPathStr = None
        # children
        self._childPathStrList = []
        # proxy
        self._proxyObj = None

    # **************************************************************************************************************** #
    def _set_obj_path_build_(self, *args):
        self._pathObj = self.CLS_grh_path(*args)

    def path(self):
        return self._pathObj

    def pathString(self):
        return self._pathObj.toString()

    def name(self):
        """
        :return: objects.Nodename / objects.Portname
        """
        return self._pathObj.name()

    def nameString(self):
        """
        :return: str("name")
        """
        return self._pathObj.nameString()

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


class Def_GrhPort(
    Def_GrhObj,
    Def_GrhCacheObj
):
    CLS_grh_port_query = None

    CLS_grh_type = None

    CLS_grh_porttype = None

    CLS_grh_portpath = None

    VAR_grh_value_cls_dict = {}

    def _initDefGrhPort(self, *args):
        self._initDefGrhObj()

        nodeObject, _ = args[:2]
        # node
        self._nodeObj = nodeObject
        categoryString = self._nodeObj.categoryString()
        # port
        if isinstance(_, (str, unicode)):
            portpathString = _
            self._portQueryObj = self.CLS_grh_port_query(
                categoryString, portpathString
            )
        elif isinstance(_, Def_GrhPortQuery):
            self._portQueryObj = _
        else:
            raise TypeError()

        self._set_port_build_(self._portQueryObj)
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
        self._set_obj_path_build_(self._nodeObj.path(), self.portpath())

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
        return self._portpathObj.name()

    def portnameString(self):
        return self._portpathObj.nameString()

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
        return self.pathString()

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
    CLS_grh_node_query = None

    CLS_grh_type = None
    CLS_grh_category = None

    CLS_grh_port_set = None
    VAR_grh_port_cls_dict = {}

    CLS_grh_connector = None

    VAR_grh_param_assign_keyword_list = []
    VAR_grh_inparm_assign_keyword_list = []
    VAR_grh_otparm_assign_keyword_list = []

    OBJ_grh_obj_cache = None

    def _initDefGrhNode(self, *args):
        self._initDefGrhObj()

        _, nodepathString = args[:2]

        if isinstance(_, (str, unicode)):
            categoryString = _
            self._nodeQueryObj = self.CLS_grh_node_query(categoryString)
        elif isinstance(_, Def_GrhPortQuery):
            self._nodeQueryObj = _
        else:
            raise TypeError()

        self._set_obj_path_build_(nodepathString)

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

        for i in nodeQueryObject.portQueries():
            addPortFnc_(self.pathString(), i)

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
        return self.pathString()

    def __str__(self):
        return u'{}(category="{}", nodepath="{}")'.format(
            self.__class__.__name__,
            self.categoryString(),
            self.pathString()
         )

    def __repr__(self):
        return self.__str__()


# connector ********************************************************************************************************** #
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


# object proxy ******************************************************************************************************* #
class Def_GrhObjProxy(grhCfg.Utility):
    CLS_grh_name = None

    def _initDefGrhObjProxy(self, *args):
        if isinstance(args[0], Def_GrhObj):
            self._nameObj = self.CLS_grh_name(args[0].toString())
        elif isinstance(args[0], (str, unicode)):
            self._nameObj = self.CLS_grh_name(args[0])
        else:
            raise TypeError(
                u'''argument must be: str("path") / objects.Port / objects.Node'''
            )

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def setNameString(self, *args):
        self._nameObj.setRaw(*args)


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
            proxyObj = args[0]
            obj = proxyObj.node()
            keyString = obj.toString()
            if self._nodeGraphSetObj._get_obj_exist_(keyString) is False:
                self._set_node_graph_obj_add_(obj)
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
        return self._nodeObj.pathString()


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
        for inparmObject in self._obj.inparms():
            if inparmObject.hasSource():
                lis.append(inparmObject)
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

        keyString = sourceObject.pathString()
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


class Def_GrhTrsNode(
    grhCfg.Utility,
    Def_GrhCacheObj
):
    CLS_grh_trs_node_query = None

    CLS_grh_src_node = None
    CLS_grh_tgt_node = None

    CLS_grh_node_translator = None

    OBJ_grh_trs_query_cache = None

    OBJ_grh_trs_obj_cache = None
    OBJ_grh_src_obj_cache = None
    OBJ_grh_tgt_obj_cache = None

    def _initDefGrhTrsNode(self, *args):
        srcNodeString = args[0]

        self._srcNodeObj = self.CLS_grh_src_node(srcNodeString)

        self._translatorObj = self.CLS_grh_node_translator(
            self,
            self._srcNodeObj,
            self.CLS_grh_tgt_node
        )

        self._set_create_expressions_run_()

    def _set_create_expressions_run_(self):
        expressionDict = self._translatorObj._trsNodeQueryObj.createExpressionRaw
        self._set_expressions_run_(expressionDict)

    def _set_after_expressions_run_(self):
        expressionDict = self._translatorObj._trsNodeQueryObj.afterExpressionRaw
        self._set_expressions_run_(expressionDict)

    # noinspection PyMethodMayBeStatic
    def _set_expressions_run_(self, expressionDict):
        if expressionDict:
            if self.DEF_grh_keyword_command in expressionDict:
                commands = expressionDict[self.DEF_grh_keyword_command]
                if commands:
                    cmdsStr = ';'.join(commands)
                    exec cmdsStr

    # **************************************************************************************************************** #
    def _cmd_set_node_insert_(self, outputSrcNodeObjects, targetMtlOtparmString, tgtInparmString, tgtOtparmString):
        for srcNodeObject in outputSrcNodeObjects:
            trsNodeObject = self.getTrsNode(srcNodeObject.pathString())
            tgtNodeObject = trsNodeObject.tgtNode()

            copyTgtNodeString = u'{}__{}'.format(tgtNodeObject.pathString(), self.tgtNode().categoryString())
            copyTgtNodeObject = self.getTgtNode(self.tgtNode().categoryString(), copyTgtNodeString)

            [i.setPortrawString(self.tgtNode().inparm(i.portpathString()).portrawString()) for i in copyTgtNodeObject.inparms()]

            tgtNodeObject.otparm(targetMtlOtparmString).insertTarget(
                copyTgtNodeObject.inparm(tgtInparmString),
                copyTgtNodeObject.otparm(tgtOtparmString)
            )

    def _cmd_set_color_correct_insert_(self, portdataDict=None):
        tgtConnectors = self.tgtNode().outputConnectors()

        mtl_category_0 = u'color_correct'
        node_string_0 = u'{}__{}'.format(self.tgtNode().pathString(), mtl_category_0)

        _tgtColorCorrectObject = self.getTgtNode(mtl_category_0, node_string_0)

        for _tgtConnector in tgtConnectors:
            if _tgtConnector.source().isChannel() is False:
                _portObject = _tgtColorCorrectObject.otparm()
            else:
                _dict = {
                    u'r': u'rgba.r',
                    u'g': u'rgba.g',
                    u'b': u'rgba.b',
                    u'a': u'rgba.a'
                }
                _portpathString = _dict[_tgtConnector.source().portnameString()]
                _portObject = _tgtColorCorrectObject.otparm(_portpathString)

            _tgtConnector.insert(_portObject)

        self.tgtNode().otparm().connectTo(_tgtColorCorrectObject.inparm(u'input'))
        if portdataDict:
            for k, v in portdataDict.items():
                _tgtColorCorrectObject.port(k).setPortraw(self.srcNode().port(v).portraw())
        return _tgtColorCorrectObject

    def _cmd_set_multi_texture_covert_(self, filepathString):
        srcNodeObject = self.srcNode()
        if srcNodeObject.categoryString() == u'file':
            isUdim = True
            if filepathString:
                isSequence = srcNodeObject.port(u'useFrameExtension').portraw()
                uvTilingMode = srcNodeObject.port(u'uvTilingMode').portraw()
                dirnameString = bscMethods.OsFile.dirname(filepathString)
                basenameString = bscMethods.OsFile.basename(filepathString)
                #
                findKeys = self.MOD_re.findall(u'[0-9][0-9][0-9][0-9]', basenameString)
                if findKeys:
                    if u'<udim>' in basenameString.lower():
                        isUdim = False
                    elif not uvTilingMode == u'UDIM (Mari)':
                        isUdim = False
                    #
                    if isUdim:
                        basenameString = basenameString.replace(findKeys[-1], u'<udim>')
                    elif isSequence:
                        basenameString = basenameString.replace(findKeys[-1], u'<f>')
                    #
                    filepathString = bscMethods.OsPath.composeBy(dirnameString, basenameString)
        return filepathString

    # **************************************************************************************************************** #
    def getTrsNode(self, srcNodeString):
        return self._mtd_get_cache_obj_(
            self.OBJ_grh_trs_obj_cache, srcNodeString,
            self.__class__, (srcNodeString, )
        )

    def getTgtNode(self, tgtCategoryString, tgtNodeString):
        return self._mtd_get_cache_obj_(
            self.OBJ_grh_tgt_obj_cache, tgtNodeString,
            self.CLS_grh_tgt_node, (tgtCategoryString, tgtNodeString)
        )

    def trsNodeQuery(self):
        return self._translatorObj._trsNodeQueryObj

    def srcNode(self):
        return self._srcNodeObj

    def tgtNode(self):
        return self._translatorObj.tgtNode()

    def __str__(self):
        return self.tgtNode().__str__()