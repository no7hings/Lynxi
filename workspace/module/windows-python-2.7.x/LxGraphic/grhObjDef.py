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
        pass

    def _set_add_obj_(self, *args):
        if len(args) == 2:
            objectKeyString, obj = args
        else:
            obj = args[0]
            objectKeyString = obj._get_object_key_string_()

        if not objectKeyString in self._objectFilterDict:
            self._objectList.append(obj)
            self._objectFilterDict[objectKeyString] = obj
            self._objectCount += 1

    def _get_has_obj_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objectKeyString = args[0]
            return objectKeyString in self._objectFilterDict
        elif isinstance(args[0], int):
            index = args[0]
            return 0 <= index <= (self._objectCount - 1)
        else:
            obj = args[0]
            objectKeyString = obj._queryKeyString_()
            return objectKeyString in self._objectFilterDict

    def _get_object_(self, *args):
        if isinstance(args[0], (str, unicode)):
            objectKeyString = args[0]
            return self._objectFilterDict[objectKeyString]
        elif isinstance(args[0], int):
            index = args[0]
            return self._objectList[index]

    def _get_string_(self):
        pass

    def addObject(self, *args):
        obj = args[0]
        objectKeyString = self._get_object_key_string_(obj)
        assert objectKeyString not in self._objectFilterDict, u'''{}({})'s object "{}" is Exist.'''.format(
            self.__class__.__name__, self._obj, objectKeyString
        )
        self._set_add_obj_(*args)

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

    def hasObject(self, objectKeyString):
        """
        :param objectKeyString: str
        :return: bool
        """
        return self._get_has_obj_(objectKeyString)

    def object(self, objectKeyString):
        """
        :param objectKeyString: str
        :return: object
        """
        assert objectKeyString in self._objectFilterDict, u'''{}({})'s object "{}" is Unregistered.'''.format(
            self.__class__.__name__, self._obj, objectKeyString
        )
        return self._get_object_(objectKeyString)

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
        return self._get_object_(index)

    def hasObjectAt(self, index):
        """
        :param index: int
        :return: object
        """
        return self._get_has_obj_(index)

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


class Def_GrhObj(grhConfigure.Utility):
    def _initDefGrhObject(self, *args):
        pass

    def _var_object_key_string_(self):
        pass


class Def_GrhPort(Def_GrhObj):
    CLS_grh_porttype = None

    CLS_grh_portpath = None

    def _initDefGrhPort(self, *args):
        nodeObject, portpathString = args[:2]

        self._nodeObj = nodeObject

        self._nodepathObj = nodeObject.nodepath()

        self._portpathObj = self.CLS_grh_portpath(portpathString)

        self._parentPortpathStr = None
        self._childPortpathStrList = []

    # **************************************************************************************************************** #
    def _var_object_key_string_(self):
        return self.attrpathString()

    def _get_node_obj_(self, nodepathString):
        return self._nodeObj.__class__(nodepathString)

    def _get_port_obj_(self, *args):
        nodepathString, portpathString = args
        if isinstance(nodepathString, (str, unicode)):
            nodeObject = self._nodeObj.__class__(nodepathString)
        else:
            nodeObject = nodepathString
        if nodeObject.hasPort(portpathString):
            return nodeObject.port(portpathString)
        return self.__class__(nodeObject, portpathString)

    # **************************************************************************************************************** #
    def _set_porttype_(self, porttypeString):
        self._porttypeObj = self.CLS_grh_porttype(porttypeString)

    def porttype(self):
        return self._porttypeObj

    def porttypeString(self):
        return self._porttypeObj.toString()

    def portpath(self):
        return self._portpathObj

    def attrpathString(self):
        return self._portpathObj.pathsep().join(
            [self._nodepathObj.objpathString(), self._portpathObj.objpathString()]
        )

    def portpathString(self):
        return self._portpathObj.portpathString()

    def portname(self):
        return self._portpathObj.name()

    def portnameString(self):
        return self._portpathObj.nameString()

    # **************************************************************************************************************** #
    def node(self):
        return self._nodeObj

    # **************************************************************************************************************** #
    def _set_parent_(self, portnameString):
        self._parentPortpathStr = portnameString

    def _set_children_(self, portpathStrings):
        self._childPortpathStrList = portpathStrings

    def _get_has_child_(self, *args):
        portpathString = args[0]
        return portpathString in self._childPortpathStrList

    def _get_child_(self, *args):
        portpathString = args[0]
        if self.hasChildren():
            return self._nodeObj.port(portpathString)

    def hasParent(self):
        return self._parentPortpathStr is not None

    def parent(self):
        if self.hasParent():
            return self._nodeObj.port(self._parentPortpathStr)

    def hasChildren(self):
        return self._childPortpathStrList != []

    def children(self):
        if self.hasChildren():
            return [self._nodeObj.port(i) for i in self._childPortpathStrList]
        return []

    def hasChild(self, *args):
        return self._get_has_child_(*args)

    def child(self, *args):
        return self._get_child_(*args)

    # **************************************************************************************************************** #

    def _get_is_source_(self):
        pass

    def _get_has_source(self):
        pass

    def _get_source_(self):
        pass

    def _get_is_target_(self):
        pass

    def _get_has_targets_(self):
        pass

    def _get_targets_(self):
        pass

    def _get_target_(self, *args):
        pass

    def isSource(self):
        return self._get_is_source_()

    def hasSource(self):
        return self._get_has_source()

    def source(self):
        return self._get_source_()

    def isTarget(self):
        return self._get_is_target_()

    def hasTargets(self):
        return self._get_has_targets_()

    def targets(self):
        return self._get_targets_()

    def hasTarget(self, *args):
        return self._get_target_(*args)

    # **************************************************************************************************************** #
    def _get_portdata_(self, *args):
        pass

    def portdata(self, *args):
        return self._get_portdata_(*args)

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
    CLS_grh_port = None

    OBJ_grh_query_cache = None

    def _initDefGrhNode(self, *args):
        categoryString, nodepathString = args[:2]

        self._typeObj = None
        self._categoryObj = self.CLS_grh_category(categoryString)
        self._nodepathObj = self.CLS_grh_nodepath(nodepathString)

        self._portSetObj = self.CLS_grh_port_set(self)
        self._inputSetObj = self.CLS_grh_port_set(self)
        self._outputSetObj = self.CLS_grh_port_set(self)

        self._portDefDict = {}
        self._portkeyStrDict = {}

    # **************************************************************************************************************** #
    def _var_object_key_string_(self):
        return self.nodepathString()

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
        return self._nodepathObj.objpathString()

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
    def ports(self):
        return self._portSetObj.objects()

    def hasPort(self, *args):
        return self._portSetObj._get_has_obj_(*args)

    def port(self, *args):
        return self._portSetObj.object(*args)

    def inputs(self):
        return self._inputSetObj.objects()

    def hasInput(self, *args):
        return self._inputSetObj._get_has_obj_(*args)

    def input(self, *args):
        return self._inputSetObj.object(*args)

    def outputs(self):
        return self._outputSetObj.objects()

    def hasOutput(self, *args):
        return self._outputSetObj._get_has_obj_(*args)

    def output(self, *args):
        return self._outputSetObj.object(*args)

    # **************************************************************************************************************** #
    def _get_source_nodes_(self, *args):
        def addFnc_(obj):
            key = obj.nodepathString()
            if key not in keyLis:
                keyLis.append(key)
                lis.append(obj)
                return True
            return False

        keyLis = []
        lis = []

        for portObject in self.inputs():
            if portObject.hasSource():
                _nodeObject = portObject.source().node()
                addFnc_(_nodeObject)

        return self._get_nodes_filter_(lis, *args)

    def _get_all_source_nodes_(self, *args):
        def addFnc_(obj):
            key = obj.nodepathString()
            if key not in keyLis:
                keyLis.append(key)
                lis.append(obj)
                return True
            return False

        def rcsFnc_(nodeObject_):
            for portObject in nodeObject_.inputs():
                if portObject.hasSource():
                    _nodeObject = portObject.source().node()
                    if addFnc_(_nodeObject) is True:
                        rcsFnc_(_nodeObject)

        keyLis = []
        lis = []
        rcsFnc_(self)
        return self._get_nodes_filter_(lis, *args)

    def _get_target_nodes_(self, *args):
        def addFnc_(obj):
            key = obj.nodepathString()
            if key not in keyLis:
                keyLis.append(key)
                lis.append(obj)
                return True
            return False

        keyLis = []
        lis = []

        for portObject in self.outputs():
            if portObject.hasTargets():
                for _targetObject in portObject.targets():
                    _nodeObject = _targetObject
                    addFnc_(_nodeObject)

        return self._get_nodes_filter_(lis, *args)

    def _get_all_target_nodes_(self, *args):
        def addFnc_(obj):
            key = obj.nodepathString()
            if key not in keyLis:
                keyLis.append(key)
                lis.append(obj)
                return True
            return False

        def rcsFnc_(nodeObject_):
            for portObject in nodeObject_.outputs():
                if portObject.hasTargets():
                    for _targetObject in portObject.targets():
                        _nodeObject = _targetObject.node()
                        if addFnc_(_nodeObject) is True:
                            rcsFnc_(_nodeObject)

        keyLis = []
        lis = []
        rcsFnc_(self)
        return self._get_nodes_filter_(lis, *args)

    @classmethod
    def _get_nodes_filter_(cls, nodeObjects, *args):
        pass

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
