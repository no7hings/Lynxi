# coding:utf-8
from LxBasic.bscMethods import _bscMtdRaw

from .import grhObjDef


class Abs_GrhObjSet(grhObjDef.Def_GrhObjSet):
    DEF_grh_key_index = u'index'

    def _initAbsGrhObjSet(self, *args):
        self._initDefGrhObjSet(*args)

    def _initializeData_(self):
        self._objectList = []
        self._objectFilterDict = {}

        self._objectCount = 0

    def __str__(self):
        return self._get_string_()


# object query cache ************************************************************************************************* #
class Abs_GrhNodeRaw(grhObjDef.Def_GrhNodeRaw):
    def _initAbsGrhNodeRaw(self, *args):
        self._initDefGrhNodeRaw(*args)


class Abs_GrhPortQuery(grhObjDef.Def_GrhPortQuery):
    def _initAbsGrhPortQuery(self, *args):
        self._initDefGrhPortQuery(*args)


class Abs_GrhNodeQuery(grhObjDef.Def_GrhNodeQuery):
    def _initAbsGrhNodeQuery(self, *args):
        self._initDefGrhNodeQuery(*args)


class Abs_GrhObjQueryCache(grhObjDef.Def_GrhObjQueryCache):
    def _initAbsGrhObjQueryCache(self, *args):
        self._initDefGrhObjQueryCache(*args)


# translator object query cache ************************************************************************************** #
class Abs_GrhTrsNodeRaw(grhObjDef.Def_GrhTrsNodeRaw):
    def _initAbsGrhTrsNodeRaw(self, *args):
        self._initDefGrhTrsNodeRaw(*args)


class Abs_GrhTrsPortQuery(grhObjDef.Def_GrhTrsPortQuery):
    def _initAbsGrhTrsPortQuery(self, *args):
        self._initDefGrhTrsPortQuery(*args)


class Abs_GrhTrsNodeQuery(grhObjDef.Def_GrhTrsNodeQuery):
    def _initAbsGrhTrsNodeQuery(self, *args):
        self._initDefGrhTrsNodeQuery(*args)


class Abs_GrhTrsObjQueryCache(grhObjDef.Def_GrhTrsObjQueryCache):
    def _initAbsGrhTrsObjQueryCache(self, *args):
        self._initDefGrhTrsObjQueryCache(*args)


# object cache ******************************************************************************************************* #
class Abs_GrhObjCache(grhObjDef.Def_GrhObjCache):
    def _initAbsGrhObjCache(self, *args):
        self._initDefGrhObjCache(*args)


# ******************************************************************************************************************** #
class Abs_GrhPort(grhObjDef.Def_GrhPort):
    def _initAbsGrhPort(self, *args):
        self._initDefGrhPort(*args)

    # **************************************************************************************************************** #
    def _get_node_cache_obj_(self, *args):
        nodepathString = args[0]
        objArgs = nodepathString, self._nodeObj.__class__, (nodepathString, )
        return self._nodeObj.OBJ_grh_obj_cache.object(*objArgs)

    def _get_port_cache_obj_(self, *args):
        nodepathString, portpathString = args

        if isinstance(nodepathString, (str, unicode)):
            nodeCls = self._nodeObj.__class__
        else:
            _nodeObject = nodepathString
            nodeCls = _nodeObject.__class__

        objArgs = nodepathString, nodeCls, (nodepathString, )

        nodeObject_ = self._nodeObj.OBJ_grh_obj_cache.object(*objArgs)

        portpathString = self._nodeObj._nodeQueryObj._get_portpath_(portpathString)
        if nodeObject_.hasPort(portpathString):
            return nodeObject_.port(portpathString)

        portCls = self.__class__
        return portCls(nodeObject_, portpathString)

    # **************************************************************************************************************** #
    def _set_parent_(self, *args):
        portnameString = args[0]
        self._parentPathStr = portnameString

    def _get_parent_exist_(self):
        return self._parentPathStr is not None

    def _get_parent_(self):
        if self._get_parent_exist_() is True:
            return self._nodeObj.port(self._parentPathStr)

    def _get_children_exist_(self):
        return self._childPathStrList != []

    def _get_children_(self):
        return [
            self._get_child_(i)
            for i in self._childPathStrList
        ]

    def _get_child_exist_(self, *args):
        portpathString = args[0]
        return portpathString in self._childPathStrList

    def _get_child_(self, *args):
        portpathString = args[0]
        if self.hasChildren():
            return self._nodeObj.port(portpathString)

    def _set_children_(self, *args):
        portpathStrings = args[0]
        self._childPathStrList = portpathStrings

    # **************************************************************************************************************** #
    def _get_portdata_(self, *args):
        self._valueObj.raw()

    def _get_portdata_string_(self, *args):
        self._valueObj.toString()

    def _set_portdata_(self, *args):
        self._valueObj.setRaw(*args)

    def _set_portdata_string_(self, *args):
        self._valueObj.setRawString(*args)

    # **************************************************************************************************************** #
    def _get_is_target_(self):
        return self._get_source_exist_()

    def _get_targets_exist_(self):
        return self._targetPortIndexList != []

    def _get_targets_(self):
        return [
            self._get_cache_obj_(i)
            for i in self._targetPortIndexList
        ]

    def _get_target_exist_(self, *args):
        pass

    def _get_target_(self, *args):
        if isinstance(args[0], (int, float)):
            index = args[0]
            if index in self._targetPortIndexList:
                objIndex = self._targetPortIndexList[index]
                return self._get_cache_obj_(objIndex)

    # **************************************************************************************************************** #
    @classmethod
    def _get_attrpath_(cls, *args):
        return cls.CLS_grh_portpath.pathsep().join(
            list(args)
        )


class Abs_GrhNode(grhObjDef.Def_GrhNode):
    def _initAbsGrhNode(self, *args):
        self._initDefGrhNode(*args)

    # **************************************************************************************************************** #
    def _get_source_nodes_(self, *args):
        def addFnc_(obj):
            keyString = obj.nodepathString()
            if keyString not in keyStrList:
                keyStrList.append(keyString)
                lis.append(obj)
                return True
            return False

        keyStrList = []
        lis = []

        for portObject in self.inputs():
            if portObject.hasSource():
                _nodeObject = portObject.source().node()
                addFnc_(_nodeObject)

        return self._get_nodes_filter_(lis, *args)

    def _get_all_source_nodes_(self, *args):
        def addFnc_(obj):
            keyString = obj.nodepathString()
            if keyString not in keyStrList:
                keyStrList.append(keyString)
                lis.append(obj)
                return True
            return False

        def rcsFnc_(nodeObject_):
            for portObject in nodeObject_.inputs():
                if portObject.hasSource():
                    _nodeObject = portObject.source().node()
                    if addFnc_(_nodeObject) is True:
                        rcsFnc_(_nodeObject)

        keyStrList = []
        lis = []
        rcsFnc_(self)
        return self._get_nodes_filter_(lis, *args)

    def _get_target_nodes_(self, *args):
        def addFnc_(obj):
            keyString = obj.nodepathString()
            if keyString not in keyStrList:
                keyStrList.append(keyString)
                lis.append(obj)
                return True
            return False

        keyStrList = []
        lis = []

        for portObject in self.outputs():
            if portObject.hasTargets():
                for _targetObject in portObject.targets():
                    _nodeObject = _targetObject.node()
                    addFnc_(_nodeObject)

        return self._get_nodes_filter_(lis, *args)

    def _get_all_target_nodes_(self, *args):
        def addFnc_(obj):
            keyString = obj.nodepathString()
            if keyString not in keyStrList:
                keyStrList.append(keyString)
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

        keyStrList = []
        lis = []
        rcsFnc_(self)
        return self._get_nodes_filter_(lis, *args)

    @classmethod
    def _get_nodes_filter_(cls, nodeObjects, *args):
        lis = []
        if args:
            categoryString = _bscMtdRaw.String.toList(args[0])
        else:
            categoryString = None

        for i in nodeObjects:
            _categoryString = i.categoryString()
            if categoryString is not None:
                if _categoryString in categoryString:
                    lis.append(i)
            else:
                lis.append(i)
        return lis
