# coding:utf-8
from . import grhConfigure


class Def_GrhObjSet(grhConfigure.Utility):
    VAR_grh_objectsep = None

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
        """
        replace method
        """

    def _get_obj_exist_(self, *args):
        """
        replace method
        """

    def _get_obj_(self, *args):
        """
        replace method
        """

    def _get_obj_index_(self, *args):
        """
        replace method
        """

    def _get_string_(self):
        """
        replace method
        """

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
        keyString = args[0]
        assert keyString in self._objectFilterDict, u'''{}(object={})'s key "{}" is Unregistered.'''.format(
            self.__class__.__name__, self._obj, keyString
        )
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


# query ************************************************************************************************************** #
class Def_GrhPortQuery(grhConfigure.Utility):
    VAR_grh_portsep = None

    VAR_grh_property_list = [
        grhConfigure.Utility.DEF_grh_key_porttype,
        grhConfigure.Utility.DEF_grh_key_portpath,
        grhConfigure.Utility.DEF_grh_key_parent,
        grhConfigure.Utility.DEF_grh_key_children,
        grhConfigure.Utility.DEF_grh_key_assign
    ]

    def _initDefGrhPortQuery(self, *args):
        self._portRaw = args[0]

        self._build_query_(self._portRaw)

    def _build_query_(self, raw):
        """
        replace method
        """
    @property
    def portsep(self):
        return self.VAR_grh_portsep
    # noinspection PyUnresolvedReferences
    def __str__(self):
        return '{}(porttype="{}", portpath="{}")'.format(
            self.__class__.__name__,
            self.porttype,
            self.portpath
        )

    def __repr__(self):
        return self.__str__()


class Def_GrhNodeQuery(grhConfigure.Utility):
    CLS_grh_port_query_set = None
    CLS_grh_port_query = None

    VAR_grh_property_list = [
        grhConfigure.Utility.DEF_grh_key_type,
        grhConfigure.Utility.DEF_grh_key_category
    ]

    def _initDefGrhNodeQuery(self, *args):
        self._nodeRaw = args[0]

        self._portpathDict = {}

        self._portQuerySetObj = self.CLS_grh_port_query_set(self)

        self._build_query_(self._nodeRaw)

    def _build_query_(self, *args):
        """
        replace method
        """

    def _build_port_query_(self, *args):
        """
        replace method
        """

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

    # noinspection PyUnresolvedReferences
    def __str__(self):
        return '{}(type="{}", category="{}")'.format(
            self.__class__.__name__,
            self.type,
            self.category
        )

    def __repr__(self):
        return self.__str__()


class Def_GrhQueryCache(grhConfigure.Utility):
    CLS_grh_node_query_set = None
    CLS_grh_node_query = None

    # noinspection PyUnusedLocal
    def _initDefGrhQueryCache(self, *args):
        self._nodeQuerySetObj = self.CLS_grh_node_query_set(self)

    def _get_node_portpaths_(self, *args):
        """
        replace method
        """

    def _get_node_port_raws_(self, *args):
        """
        replace method
        """

    def _get_node_raw_(self, *args):
        """
        replace method
        """

    # **************************************************************************************************************** #
    def _get_has_node_(self, *args):
        """
        replace method
        """

    def _get_nodes_(self):
        """
        replace method
        """

    def _get_node_(self, *args):
        """
        replace method
        """

    def hasNode(self, *args):
        return self._get_has_node_(*args)

    def nodes(self):
        return self._get_nodes_()

    def node(self, *args):
        return self._get_node_(*args)

    def nodePort(self, *args):
        categoryString, portpathString = args
        return self.node(categoryString).port(portpathString)


class Def_GrhObjCache(grhConfigure.Utility):
    CLS_cache_obj_set = None
    # noinspection PyUnusedLocal
    def _initDefGrhObjCache(self, *args):
        self._objSetObj = self.CLS_cache_obj_set(self)

    # **************************************************************************************************************** #
    def _get_objs_(self):
        """
        replace method
        """

    def _set_obj_add_(self, *args):
        """
        replace method
        """

    def _get_obj_exist_(self, *args):
        """
        replace method
        """

    def _get_obj_(self, *args):
        """
        replace method
        """

    def _get_obj_index_(self, *args):
        """
        replace method
        """

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
class Def_GrhObj(grhConfigure.Utility):
    OBJ_grh_query_cache = None

    OBJ_grh_obj_cache = None

    # noinspection PyUnusedLocal
    def _initDefGrhObj(self, *args):
        # parent
        self._parentPathStr = None
        # children
        self._childPathStrList = []

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


class Def_GrhPort(Def_GrhObj):
    CLS_grh_porttype = None

    CLS_grh_portpath = None

    def _initDefGrhPort(self, *args):
        self._initDefGrhObj()

        nodeObject, portpathString = args[:2]
        # node
        self._nodeObj = nodeObject
        # portpath
        self._set_portpath_(portpathString)
        # value
        self._valueObj = None
        self._defValueObj = None
        # source
        self._sourcePortIndex = None
        # target
        self._targetPortIndexList = []

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
    def _set_porttype_(self, *args):
        porttypeString = args[0]
        self._porttypeObj = self.CLS_grh_porttype(porttypeString)

    def porttype(self):
        return self._porttypeObj

    def porttypeString(self):
        return self._porttypeObj.toString()

    # **************************************************************************************************************** #
    def _set_portpath_(self, *args):
        portpathString = args[0]
        self._portpathObj = self.CLS_grh_portpath(portpathString)

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

    def isChanged(self):
        return self.isValueChanged() or self.hasSource()

    # **************************************************************************************************************** #
    def _get_is_source_(self):
        """
        replace method
        """

    def _get_source_exist_(self, *args):
        """
        replace method
        """

    def _get_source_(self):
        """
        replace method
        """

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

    # **************************************************************************************************************** #
    def _set_add_target_(self, *args):
        """
        replace method
        """

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
        """
        replace method
        """

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
    def portgiven(self):
        if self.hasSource() is True:
            return self.source()
        return self.portdata()

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


class Def_GrhNode(Def_GrhObj):
    CLS_grh_type = None
    CLS_grh_category = None

    CLS_grh_nodepath = None

    CLS_grh_port_set = None
    VAR_grh_port_cls_dict = {}
    VAR_grh_value_cls_dict = {}

    VAR_grh_input_assign_list = []
    VAR_grh_output_assign_list = []
    VAR_grh_parameter_assign_list = []

    def _initDefGrhNode(self, *args):
        self._initDefGrhObj()

        categoryString, nodepathString = args[:2]

        self._typeObj = None
        self._categoryObj = self.CLS_grh_category(categoryString)
        self._nodepathObj = self.CLS_grh_nodepath(nodepathString)

        self._portSetObj = self.CLS_grh_port_set(self)

        self._inputSetObj = self.CLS_grh_port_set(self)
        self._outputSetObj = self.CLS_grh_port_set(self)
        self._parameterSetObj = self.CLS_grh_port_set(self)

        self._nodeQueryObj = self.OBJ_grh_query_cache.node(
            self.categoryString()
        )

        self.OBJ_grh_obj_cache._set_obj_add_(self)

        self._set_ports_initialize_()

    # **************************************************************************************************************** #
    def _get_port_cls_(self, *args):
        """
        replace method
        """

    def _get_value_cls_(self, *args):
        pass

    def _set_ports_initialize_(self):
        """
        replace method
        """

    def _set_node_query_(self, obj):
        """
        replace method
        """

    # **************************************************************************************************************** #
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
        pass

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
        return self._outputSetObj.object(*args)

    # **************************************************************************************************************** #
    def parameters(self):
        return self._parameterSetObj.objects()

    def hasParameter(self, *args):
        return self._parameterSetObj.hasObject(*args)

    def parameter(self, *args):
        return self._parameterSetObj.object(*args)

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


class Def_GrhConnection(grhConfigure.Utility):
    def _initDefGrhConnection(self):
        pass
