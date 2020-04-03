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

    def _set_obj_add_(self, *args):
        if len(args) == 2:
            objKeyString, obj = args
        else:
            obj = args[0]
            objKeyString = self._get_object_key_string_(obj)

        if not objKeyString in self._objectFilterDict:
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
        elif isinstance(args[0], int):
            index = args[0]
            return self._objectList[index]

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

    def __str__(self):
        return self._get_string_()


class Abs_GrhPortQuery(grhObjDef.Def_GrhPortQuery):
    def _initAbsGrhPortQuery(self, *args):
        self._initDefGrhPortQuery(*args)

    def _build_query_(self, *args):
        raw = args[0]
        for i in self.VAR_grh_property_list:
            self.__dict__[i] = raw[i]


class Abs_GrhNodeQuery(grhObjDef.Def_GrhNodeQuery):
    def _initAbsGrhNodeQuery(self, *args):
        self._initDefGrhNodeQuery(*args)

    def _build_query_(self, *args):
        raw = args[0]

        for i in self.VAR_grh_property_list:
            self.__dict__[i] = raw[i]

        portRaws = raw[self.DEF_grh_key_port]
        for i in portRaws:
            self._build_port_query_(i)

    def _build_port_query_(self, *args):
        raw = args[0]
        portpathString = raw[self.DEF_grh_key_portpath]
        obj = self.CLS_grh_port_query(raw)
        portnameString = portpathString.split(obj.portsep)[-1]
        self._portpathDict[portnameString] = portpathString
        self._portQuerySetObj._set_obj_add_(obj)


class Abs_GrhQueryCache(grhObjDef.Def_GrhQueryCache):
    def _initAbsGrhQueryCache(self, *args):
        self._initDefGrhQueryCache(*args)

    def _get_has_node_(self, *args):
        return self._nodeQuerySetObj.hasObject(*args)

    def _get_nodes_(self):
        return self._nodeQuerySetObj.objects()

    def _get_node_(self, *args):
        if self._nodeQuerySetObj._get_obj_exist_(*args):
            return self._nodeQuerySetObj._get_obj_(*args)
        else:
            raw = self._get_node_raw_(*args)
            obj = self.CLS_grh_node_query(raw)
            self._nodeQuerySetObj._set_obj_add_(obj)
            return obj


class Abs_GrhObjCache(grhObjDef.Def_GrhObjCache):
    def _initAbsGrhObjCache(self, *args):
        self._initDefGrhObjCache(*args)

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


# ******************************************************************************************************************** #
class Abs_GrhPort(grhObjDef.Def_GrhPort):
    def _initAbsGrhPort(self, *args):
        self._initDefGrhPort(*args)

    # **************************************************************************************************************** #
    def _get_node_cache_obj_(self, *args):
        nodepathString = args[0]
        objArgs = nodepathString, self._nodeObj.__class__, (nodepathString, )
        return self.OBJ_grh_obj_cache.object(*objArgs)

    def _get_port_cache_obj_(self, *args):
        nodepathString, portpathString = args

        if isinstance(nodepathString, (str, unicode)):
            nodeCls = self._nodeObj.__class__
        else:
            _nodeObject = nodepathString
            nodeCls = _nodeObject.__class__

        objArgs = nodepathString, nodeCls, (nodepathString, )

        nodeObject_ = self.OBJ_grh_obj_cache.object(*objArgs)

        portpathString = self._nodeObj._nodeQueryObj._get_portpath_(portpathString)
        if nodeObject_.hasPort(portpathString):
            return nodeObject_.port(portpathString)

        portCls = self.__class__
        return portCls(nodeObject_, portpathString)

    def _get_cache_obj_(self, *args):
        self.OBJ_grh_obj_cache._get_obj_(*args)

    def _get_cache_obj_index(self, *args):
        return self.OBJ_grh_obj_cache._get_obj_index_(*args)

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
    def _get_is_source_(self):
        return self._get_targets_exist_()

    def _get_source_exist_(self, *args):
        return self._sourcePortIndex is not None

    def _get_source_(self):
        if self._get_source_exist_() is True:
            return self._get_cache_obj_(
                self._sourcePortIndex
            )

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

    def _set_source_(self, *args):
        obj = args[0]
        if self._get_source_exist_(obj) is False:
            self._sourcePortIndex = self._get_cache_obj_index(obj)
            obj._set_add_target_(self)

    @classmethod
    def _get_attrpath_(cls, *args):
        return cls.CLS_grh_portpath.pathsep().join(
            list(args)
        )


class Abs_GrhNode(grhObjDef.Def_GrhNode):
    def _initAbsGrhNode(self, *args):
        self._initDefGrhNode(*args)

    def _get_port_cls_(self, *args):
        assignString = args[0]
        if assignString in self.VAR_grh_port_cls_dict:
            return self.VAR_grh_port_cls_dict[assignString]

    def _get_value_cls_(self, *args):
        porttypeString = args[0]
        if porttypeString in self.VAR_grh_value_cls_dict:
            return self.VAR_grh_value_cls_dict[porttypeString]

    def _set_ports_initialize_(self):
        def addPortFnc_(nodepathString_, portQuery_):
            _porttypeString = portQuery_.porttype
            _portpathString = portQuery_.portpath
            _assignString = portQuery_.assign
            _parentPathStr = portQuery_.parent
            _childPortnameStrings = portQuery_.children

            _portCls = self._get_port_cls_(_assignString)

            if _portCls is not None:
                _attrpathString = _portCls._get_attrpath_(
                    nodepathString_, _portpathString
                )
                objArgs = _attrpathString, _portCls, (self, _portpathString)
                _portObject = self.OBJ_grh_obj_cache.object(*objArgs)
                if _portObject is not None:
                    _portObject._set_porttype_(_porttypeString)
                    if _assignString in self.VAR_grh_input_assign_list:
                        self._inputSetObj._set_obj_add_(_portObject)
                    elif _assignString in self.VAR_grh_output_assign_list:
                        self._outputSetObj._set_obj_add_(_portObject)
                    elif _assignString in self.VAR_grh_parameter_assign_list:
                        self._parameterSetObj._set_obj_add_(_portObject)
                    _portObject._set_parent_(_parentPathStr)
                    _portObject._set_children_(_childPortnameStrings)

                    self._portSetObj._set_obj_add_(_portObject)

        for i in self._nodeQueryObj.ports():
            addPortFnc_(self.nodepathString(), i)

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
