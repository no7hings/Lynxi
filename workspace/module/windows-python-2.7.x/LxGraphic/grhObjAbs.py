# coding:utf-8
from LxBasic import bscMethods

from .import grhCfg, grhObjDef


class Abs_GrhObjSet(grhObjDef.Def_GrhObjSet):

    def _initAbsGrhObjSet(self, *args):
        self._initDefGrhObjSet(*args)

    def __str__(self):
        return self._get_string_()


# object query cache ************************************************************************************************* #
class Abs_GrhPortQueryraw(grhObjDef.Def_GrhPortQueryraw):
    def _initAbsGrhPortQueryraw(self, *args):
        self._initDefGrhPortQueryraw(*args)


class Abs_GrhNodeQueryraw(grhObjDef.Def_GrhNodeQueryraw):
    def _initAbsGrhNodeQueryraw(self, *args):
        self._initDefGrhNodeQueryraw(*args)


class Abs_GrhObjQueryrawCache(grhObjDef.Def_GrhObjQueryrawCache):
    def _initAbsGrhObjQueryCache(self, *args):
        self._initDefGrhObjQueryrawCache(*args)


# object query ******************************************************************************************************* #
class Abs_GrhPortQuery(grhObjDef.Def_GrhPortQuery):
    def _initAbsGrhPortQuery(self, *args):
        self._initDefGrhPortQuery(*args)


class Abs_GrhNodeQuery(grhObjDef.Def_GrhNodeQuery):
    def _initAbsGrhNodeQuery(self, *args):
        self._initDefGrhNodeQuery(*args)


# translator object query cache ************************************************************************************** #
class Abs_GrhTrsPortQueryraw(grhObjDef.Def_GrhTrsPortQueryraw):
    def _initAbsGrhTrsPortQueryraw(self, *args):
        self._initDefGrhPortQueryraw(*args)


class Abs_GrhTrsNodeQueryraw(grhObjDef.Def_GrhTrsNodeQueryraw):
    def _initAbsGrhTrsNodeQueryraw(self, *args):
        self._initDefGrhTrsNodeQueryraw(*args)


class Abs_GrhTrsObjQueryCache(grhObjDef.Def_GrhTrsObjQueryrawCache):
    def _initAbsGrhTrsObjQueryCache(self, *args):
        self._initDefGrhTrsObjQueryCache(*args)


# translator object query ******************************************************************************************** #
class Abs_GrhTrsPortQuery(grhObjDef.Def_GrhTrsPortQuery):
    def _initAbsGrhTrsPortQuery(self, *args):
        self._initDefGrhTrsPortQuery(*args)


class Abs_GrhTrsNodeQuery(grhObjDef.Def_GrhTrsNodeQuery):
    def _initAbsGrhTrsNodeQuery(self, *args):
        self._initDefGrhTrsNodeQuery(*args)


# cache ************************************************************************************************************** #
class Abs_GrhObjCache(grhObjDef.Def_GrhObjCache):
    def _initAbsGrhObjCache(self, *args):
        self._initDefGrhObjCache(*args)


# object ************************************************************************************************************* #
class Abs_GrhConnector(grhObjDef.Def_GrhConnector):
    def _initAbsGrhConnector(self, *args):
        self._initDefGrhConnector(*args)


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
        objpathString = args[0]
        self._parentPathStr = objpathString
        # mark

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

        for portObject in self.inparms():
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
            for portObject in nodeObject_.inparms():
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

        for portObject in self.ports():
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
            for portObject in nodeObject_.ports():
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
            categoryString = bscMethods.String.toList(args[0])
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


# object proxy ******************************************************************************************************* #
class Abs_GrhPortProxy(grhObjDef.Def_GrhPortProxy):
    def _initAbsGrhPortProxy(self, *args):
        self._initDefGrhPortProxy(*args)


class Abs_GrhNodeProxy(grhObjDef.Def_GrhNodeProxy):
    def _initAbsGrhNodeProxy(self, *args):
        self._initDefGrhNodeProxy(*args)


# node graph ********************************************************************************************************* #
class Abs_GrhNodeGraph(grhObjDef.Def_GrhNodeGraph):
    def _initAbsGrhNodeGraph(self, *args):
        self._initDefGrhNodeGraph(*args)


class Abs_GrhNodeGraphOutput(grhObjDef.Def_GrhNodeGraphOutput):
    def _initAbsGrhNodeGraphOutput(self, *args):
        self._initDefGrhNodeGraphOutput(*args)


# node translate ***************************************************************************************************** #
class Abs_GrhNodeTranslator(grhCfg.Utility):
    VAR_mtl_channel_convert_dict = {}

    VAR_grh_trs_src_node_pathsep = None
    VAR_grh_trs_tgt_node_pathsep = None

    def _initAbsGrhNodeTranslator(self, *args):
        self._trsNodeObj, self._srcNodeObj, self._tgtNodeCls = args[:3]

        self._srcCategoryStr = self._srcNodeObj.categoryString()
        self._srcNodeStr = self._srcNodeObj.nodepathString()
        self._trsNodeQueryObj = self._trsNodeObj.CLS_grh_trs_node_query(self._srcCategoryStr)

        self._tgtCategoryStr = self._trsNodeQueryObj.target_category
        self._tgtNodeQueryObj = self._tgtNodeCls.CLS_grh_node_query(self._tgtCategoryStr)
        self._tgtNodeStr = self._get_tgt_nodestr_(self._srcNodeStr)
        self._tgtNodeObj = self._get_tgt_node_(self._tgtCategoryStr, self._tgtNodeStr)

        self._set_ports_trs_()

        self._set_tgt_custom_ports_()

    def _get_tgt_node_(self, tgtCategoryString, tgtNodeString):
        _nodeCls = self._tgtNodeCls
        return _nodeCls._mtd_get_cache_obj_(
            _nodeCls.OBJ_grh_obj_cache, tgtNodeString,
            _nodeCls, (tgtCategoryString, tgtNodeString)
        )

    def _get_tgt_nodestr_(self, srcNodeString):
        return srcNodeString.replace(
            self.VAR_grh_trs_src_node_pathsep, self.VAR_grh_trs_tgt_node_pathsep
        )

    def _get_source_tgt_port_(self, srcPortObject):
        _srcSourcePortObject = srcPortObject.source()
        _srcSourceNodeObject = _srcSourcePortObject.node()

        _srcNodeStr = _srcSourceNodeObject.nodepathString()
        _srcCategoryStr = _srcSourceNodeObject.categoryString()

        if self._trsNodeObj.CLS_grh_trs_node_query.OBJ_grh_trs_queryraw_cache.hasSrcCategory(_srcCategoryStr):
            _trsNodeQueryObject = self._trsNodeObj.CLS_grh_trs_node_query(_srcCategoryStr)
            tgtCategoryString = _trsNodeQueryObject.target_category

            srcPortpathString = _srcSourcePortObject.portpathString()
            if _trsNodeQueryObject.hasTrsOtparm(srcPortpathString):
                tgtPortpathString = _trsNodeQueryObject.trsOtparm(srcPortpathString).target_portpath

                tgtNodeString = self._get_tgt_nodestr_(_srcNodeStr)
                _mtlNodeObject = self._get_tgt_node_(tgtCategoryString, tgtNodeString)

                return _mtlNodeObject.otparm(tgtPortpathString)
            else:
                print _srcSourcePortObject.node().nodepathString(), srcPortpathString
        else:
            print _srcSourcePortObject.node().nodepathString()

    def _set_ports_trs_(self):
        # portraw
        for i in self._trsNodeQueryObj.trsParams():
            self._set_params_trs_(i)

        # connect
        for i in self._trsNodeQueryObj.trsInparms():
            self._set_input_trs_(i)

    def _set_params_trs_(self, trsPortQueryObject):
        srcPortpathString = trsPortQueryObject.source_portpath
        tgtPortpathString = trsPortQueryObject.target_portpath
        if self._srcNodeObj.hasPort(srcPortpathString):
            scrPortObject = self._srcNodeObj.port(srcPortpathString)
            tgtPortObject = self._tgtNodeObj.port(tgtPortpathString)

            self._set_port_portraw_trs_(scrPortObject, tgtPortObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'Source Category "{}"; Port "{}" is Unregistered.'.format(
                    self._srcCategoryStr,
                    srcPortpathString
                )
            )

    def _set_input_trs_(self, trsPortQueryObject):
        srcPortpathString = trsPortQueryObject.source_portpath
        tgtPortpathString = trsPortQueryObject.target_portpath

        if self._srcNodeObj.hasPort(srcPortpathString):
            scrPortObject = self._srcNodeObj.port(srcPortpathString)
            tgtPortObject = self._tgtNodeObj.port(tgtPortpathString)

            self._set_input_given_trs_(scrPortObject, tgtPortObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'Source Category "{}"; Port "{}" is Unregistered.'.format(
                    self._srcCategoryStr,
                    srcPortpathString
                )
            )

    def _set_input_given_trs_(self, srcPortObject, tgtPortObject):
        # raw
        # self._set_port_portraw_trs_(srcPortObject, tgtPortObject)
        # connect
        if srcPortObject.hasSource():
            self._set_input_connect_trs_(srcPortObject, tgtPortObject)

    def _set_input_connect_trs_(self, srcPortObject, tgtPortObject):
        tgtSourcePortObject = self._get_source_tgt_port_(srcPortObject)
        if tgtSourcePortObject is not None:
            tgtTargetPortObject = tgtPortObject
            if tgtTargetPortObject.isChannel():
                self._set_input_connect_convert_(
                    tgtSourcePortObject, tgtTargetPortObject
                )
            else:
                tgtSourcePortObject.connectTo(tgtTargetPortObject)

    def _set_port_portraw_trs_(self, srcPortObject, tgtPortObject):
        srcPortraw = self._get_input_portraw_covert_(
            srcPortObject, tgtPortObject
        )
        tgtPortObject.setPortraw(srcPortraw)

    # **************************************************************************************************************** #
    def _set_input_connect_convert_(self, tgtSourcePortObject, tgtTargetPortObject):
        convertDict = self.VAR_mtl_channel_convert_dict

        tgtTargetParentPortObject = tgtTargetPortObject.parent()
        tgtParentPorttypeString = tgtTargetParentPortObject.porttypeString()
        if tgtParentPorttypeString in convertDict:
            tgtAttrpathString = tgtTargetParentPortObject.attrpathString()
            tgtCategoryString = convertDict[tgtParentPorttypeString][u'category']

            _tgtNodeString = u'{}__{}'.format(tgtAttrpathString.replace(self.DEF_grh_port_pathsep, u'__'), tgtCategoryString)
            _tgtNodeObject = self._get_tgt_node_(tgtCategoryString, _tgtNodeString)

            _tgtNodeObject.otparm().connectTo(tgtTargetParentPortObject)

            _tgtTargetChannelPortnameString = tgtTargetPortObject.portnameString()
            _tgtTargetChannelObject = _tgtNodeObject.inparm(_tgtTargetChannelPortnameString)

            tgtSourcePortObject.connectTo(_tgtTargetChannelObject)

    def _get_input_portraw_covert_(self, srcPortObject, tgtPortObject):
        srcPortraw = srcPortObject.portraw()
        if self._trsNodeQueryObj.mtlPortdataRaw:
            _keyString = tgtPortObject.portnameString()
            if _keyString in self._trsNodeQueryObj.mtlPortdataRaw:
                _dict = self._trsNodeQueryObj.mtlPortdataRaw[_keyString]
                if srcPortraw in _dict:
                    return _dict[srcPortraw]
        return srcPortraw

    # **************************************************************************************************************** #
    def _set_tgt_custom_ports_(self):
        targetPortRaw = self._trsNodeQueryObj.targetPortRaw
        if targetPortRaw:
            for k, v in targetPortRaw.items():
                portrawString = v[self.DEF_grh_key_portraw]
                self._tgtNodeObj.port(k).setPortrawString(portrawString)

    def tgtNode(self):
        return self._tgtNodeObj


class Abs_GrhTrsNode(grhObjDef.Def_GrhTrsNode):
    def _initAbsGrhTrsNode(self, *args):
        self._initDefGrhTrsNode(*args)


# node proxy translate *********************************************************************************************** #
class Abs_GrhTrsNodeProxy(grhCfg.Utility):
    CLS_grh_trs_node = None

    CLS_grh_tgt_node_proxy = None

    def _initAbsGrhTrsNodeProxy(self, *args):
        srcNodeString = args[0]

        self._trsNodeObject = self.CLS_grh_trs_node._mtd_get_cache_obj_(
            self.CLS_grh_trs_node.OBJ_grh_trs_obj_cache, srcNodeString,
            self.CLS_grh_trs_node, (srcNodeString,)
        )

        self._srcNodeObj = self._trsNodeObject.srcNode()
        self._tgtNodeObj = self._trsNodeObject.tgtNode()

        self._tgtNodeProxyObj = self.CLS_grh_tgt_node_proxy(
            self._tgtNodeObj
        )

    def srcNode(self):
        return self._srcNodeObj

    def tgtNodeProxy(self):
        return self._tgtNodeProxyObj

    def tgtNode(self):
        return self._tgtNodeObj

    def __str__(self):
        return self.tgtNodeProxy().__str__()
