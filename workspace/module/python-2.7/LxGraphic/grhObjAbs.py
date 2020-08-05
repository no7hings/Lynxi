# coding:utf-8
from LxBasic import bscObjItf, bscMethods

from . import grhObjItf


class Abs_GrhObjStack(bscObjItf.Itf_BscObjStack):
    def _initAbsGrhObjStack(self, *args):
        self._initItfBscObjStack(*args)


class Abs_GrhObjStackSite(grhObjItf.Itf_GrhObjStackSite):
    def _initAbsGrhObjStackSite(self, *args):
        self._initItfGrhVariantObjStack(*args)


# object scene ******************************************************************************************************* #
class Abs_GrhObjSceneLoader(grhObjItf.Itf_GrhObjSceneLoader):
    def _initAbsGrhObjScene(self, *args, **kwargs):
        self._initItfGrhObjScene(*args, **kwargs)


# object loader ****************************************************************************************************** #
class Abs_GrhObjLoader(grhObjItf.Itf_GrhObjLoader):
    def _initAbsGrhObjLoader(self, *args):
        self._initItfGrhObjLoader(*args)


# object queryraw **************************************************************************************************** #
class Abs_GrhPortQueryraw(grhObjItf.Itf_GrhPortQueryraw):
    def _initAbsGrhPortQueryraw(self, *args):
        self._initItfGrhPortQueryraw(*args)


class Abs_GrhNodeQueryraw(grhObjItf.Itf_GrhNodeQueryraw):
    def _initAbsGrhNodeQueryraw(self, *args):
        self._initItfGrhNodeQueryraw(*args)


class Abs_GrhObjQueryrawCreator(grhObjItf.Itf_GrhObjQueryrawCreator):
    def _initAbsGrhObjQueryBuilder(self, *args):
        self._initItfGrhObjQueryrawCreator(*args)


# object query ******************************************************************************************************* #
class Abs_GrhPortQuery(grhObjItf.Itf_GrhPortQuery):
    def _initAbsGrhPortQuery(self, *args):
        self._initItfGrhPortQuery(*args)


class Abs_GrhNodeQuery(grhObjItf.Itf_GrhNodeQuery):
    def _initAbsGrhNodeQuery(self, *args):
        self._initItfGrhNodeQuery(*args)


class Abs_GrhObjQueryBuilder(grhObjItf.Itf_GrhObjQueryBuilder):
    def _initAbsGrhObjQueryBuilder(self, *args):
        self._initItfGrhObjQueryBuilder(*args)


# translator object query cache ************************************************************************************** #
class Abs_GrhTrsObjLoader(grhObjItf.Itf_GrhTrsObjLoader):
    def _initAbsGrhTrsObjLoader(self, *args):
        self._initItfGrhTrsObjLoader(*args)


# translator object query cache ************************************************************************************** #
class Abs_GrhTrsPortQueryraw(grhObjItf.Itf_GrhTrsPortQueryraw):
    def _initAbsGrhTrsPortQueryraw(self, *args):
        self._initItfGrhPortQueryraw(*args)


class Abs_GrhTrsNodeQueryraw(grhObjItf.Itf_GrhTrsNodeQueryraw):
    def _initAbsGrhTrsNodeQueryraw(self, *args):
        self._initItfGrhTrsNodeQueryraw(*args)


class Abs_GrhTrsObjQueryrawCreator(grhObjItf.Itf_GrhTrsObjQueryrawCreator):
    def _initAbsGrhTrsObjQueryrawCreator(self, *args):
        self._initItfGrhTrsObjQueryBuilder(*args)


# translator object query ******************************************************************************************** #
class Abs_GrhTrsPortQuery(grhObjItf.Itf_GrhTrsPortQuery):
    def _initAbsGrhTrsPortQuery(self, *args):
        self._initItfGrhTrsPortQuery(*args)


class Abs_GrhTrsNodeQuery(grhObjItf.Itf_GrhTrsNodeQuery):
    def _initAbsGrhTrsNodeQuery(self, *args):
        self._initItfGrhTrsNodeQuery(*args)


class Abs_GrhTrsObjQueryBuilder(grhObjItf.Itf_GrhTrsObjQueryBuilder):
    def _initAbsGrhTrsObjQueryBuilder(self, *args):
        self._initItfGrhTrsObjQueryBuilder(*args)


# cache ************************************************************************************************************** #
class Abs_GrhObjQueue(grhObjItf.Itf_GrhObjQueue):
    def _initAbsGrhObjQueue(self, *args):
        self._initItfGrhObjQueue(*args)


# object ************************************************************************************************************* #
class Abs_GrhPort(grhObjItf.Itf_GrhPort):
    def _initAbsGrhPort(self, *args, **kwargs):
        self._initItfGrhPort(*args, **kwargs)

    # **************************************************************************************************************** #
    def _obj__set_parent_build_(self, *args):
        objpathStr = args[0]
        self._parentPathStr = objpathStr

    def _obj__set_children_build_(self, *args):
        portpathStrList = args[0]
        self._childPathStrList = portpathStrList

    # **************************************************************************************************************** #
    def _obj__get_parent_exist_(self, *args):
        if args:
            if isinstance(args[0], self.__class__):
                portObject = args[0]
                return portObject.portpathString() == self._parentPathStr
            elif isinstance(args[0], (str, unicode)):
                portpathString = args[0]
                return portpathString == self._parentPathStr
        return self._parentPathStr is not None

    def _obj__get_parent_obj_(self):
        if self._obj__get_parent_exist_() is True:
            return self.node().port(
                self._parentPathStr,
                self.assignString()
            )

    def _obj__get_child_obj_list_(self, *args, **kwargs):
        return [
            self._obj__get_child_obj_(i)
            for i in self._childPathStrList
        ]

    def _obj__get_child_exist_(self, *args):
        if args:
            portpathString = args[0]
            return portpathString in self._childPathStrList
        return self._obj__get_parent_exist_()

    def _obj__get_child_obj_(self, *args):
        if self.hasChildren():
            if isinstance(args[0], (str, unicode)):
                portpathString = args[0]
                return self.node().port(portpathString, self.assignString())
            elif isinstance(args[0], (int, float)):
                return self.node().port(self._childPathStrList[int(args[0])], self.assignString())

    def _obj__get_children_exist_(self):
        return self._childPathStrList != []

    # **************************************************************************************************************** #
    @classmethod
    def _get_attrpath_str_(cls, *args):
        return cls.CLS_grh__obj__path(*args).toString()


class Abs_GrhNode(grhObjItf.Itf_GrhNode):
    def _initAbsGrhNode(self, *args, **kwargs):
        self._initItfGrhNode(*args, **kwargs)


# connector ********************************************************************************************************** #
class Abs_GrhConnector(grhObjItf.Itf_GrhConnector):
    def _initAbsGrhConnector(self, *args):
        self._initItfGrhConnector(*args)


# geometry assign **************************************************************************************************** #
class Abs_GrhGeometryAssign(grhObjItf.Itf_GrhGeometryAssign):
    def _initAbsGrhGeometryAssign(self, *args, **kwargs):
        self._initItfGrhGeometryAssign(*args, **kwargs)


# object proxy ******************************************************************************************************* #
class Abs_GrhPortProxy(grhObjItf.Itf_GrhPortProxy):
    def _initAbsGrhPortProxy(self, *args, **kwargs):
        self._initItfGrhPortProxy(*args, **kwargs)


class Abs_GrhNodeProxy(grhObjItf.Itf_GrhNodeProxy):
    def _initAbsGrhNodeProxy(self, *args, **kwargs):
        self._initItfGrhNodeProxy(*args, **kwargs)


class Abs_GrhShaderProxy(grhObjItf.Itf_GrhNodeProxy):
    def _initAbsGrhShaderProxy(self, *args, **kwargs):
        self._initItfGrhNodeProxy(*args, **kwargs)

    # **************************************************************************************************************** #
    def inputMaterialNamespaceString(self):
        return self._obj_proxy_cls__get_connect_obj_proxy_namespace_str_(self)

    # **************************************************************************************************************** #
    def _shader_proxy__get_material_context_(self):
        for portObj in self._bindObj.otports():
            if portObj.hasTargets():
                targetPortObjs = portObj.targets()
                for targetPortObj in targetPortObjs:
                    targetNodeObj = targetPortObj.node()
                    materialNamespaceStr = self.inputMaterialNamespaceString()
                    if targetNodeObj.hasProxy(materialNamespaceStr) is True:
                        return targetPortObj.portnameString()

    def _shader_proxy__get_material_node_proxy_(self):
        for portObj in self._bindObj.otports():
            if portObj.hasTargets():
                targetPortObjs = portObj.targets()
                for targetPortObj in targetPortObjs:
                    targetNodeObj = targetPortObj.node()
                    materialNamespaceStr = self.inputMaterialNamespaceString()
                    if targetNodeObj.hasProxy(materialNamespaceStr) is True:
                        return targetNodeObj.proxy(materialNamespaceStr)


class Abs_GrhMaterialProxy(grhObjItf.Itf_GrhNodeProxy):
    VAR_grh_material_proxy__surface_shader_port_str = None
    VAR_grh_material_proxy__displacement_shader_port_str = None
    VAR_grh_material_proxy__volume_port_str = None

    def _initAbsGrhMaterialProxy(self, *args, **kwargs):
        self._initItfGrhNodeProxy(*args, **kwargs)

    # **************************************************************************************************************** #
    def _material_proxy_cls__set_shader_connect(self, *args):
        shaderInportObj, _ = args
        connectNamespaceStr = self.connectNamespaceString()
        if isinstance(_, Abs_GrhPort):
            shaderNodeObj = _.node()
            shaderOtportObj = _
            shaderNodeProxyObj = shaderNodeObj.proxy(connectNamespaceStr)
        elif isinstance(_, Abs_GrhNode):
            shaderNodeObj = _
            shaderOtportObj = shaderNodeObj.otport()
            shaderNodeProxyObj = shaderNodeObj.proxy(connectNamespaceStr)
        elif isinstance(_, Abs_GrhShaderProxy):
            shaderNodeProxyObj = _
            shaderOtportObj = shaderNodeProxyObj.bindObject().otport()
        else:
            raise TypeError()
        # set namespace
        if shaderNodeProxyObj.namespace().isRoot() is True:
            shaderNodeProxyObj.setNamespaceString(connectNamespaceStr)
        # connect
        shaderOtportObj.connectTo(shaderInportObj)

    # **************************************************************************************************************** #
    def bindSurfaceInport(self):
        return self._bindObj.inport(
            self.VAR_grh_material_proxy__surface_shader_port_str
        )

    def connectSurfaceShaderFrom(self, *args):
        self._material_proxy_cls__set_shader_connect(
            self.bindSurfaceInport(),
            *args
        )

    def surfaceShader(self):
        if self.bindSurfaceInport().hasSource():
            connectNamespaceStr = self.connectNamespaceString()
            return self.bindSurfaceInport().source().node().proxy(connectNamespaceStr)

    # **************************************************************************************************************** #
    def bindDisplacementInport(self):
        return self._bindObj.inport(
            self.VAR_grh_material_proxy__displacement_shader_port_str
        )

    def connectDisplacementShaderFrom(self, *args):
        self._material_proxy_cls__set_shader_connect(
            self.bindDisplacementInport(),
            *args
        )

    def displacementShader(self):
        if self.bindDisplacementInport().hasSource():
            connectNamespaceStr = self.connectNamespaceString()
            return self.bindDisplacementInport().source().node().proxy(connectNamespaceStr)

    # **************************************************************************************************************** #
    def bindVolumeInport(self):
        return self._bindObj.inport(
            self.VAR_grh_material_proxy__volume_port_str
        )

    def connectVolumeShaderFrom(self, *args):
        self._material_proxy_cls__set_shader_connect(
            self.bindDisplacementInport(),
            *args
        )

    def volumeShader(self):
        if self.bindVolumeInport().hasSource():
            connectNamespaceStr = self.connectNamespaceString()
            return self.bindVolumeInport().source().node().proxy(connectNamespaceStr)

    # **************************************************************************************************************** #
    def shaders(self):
        return bscMethods.List.cleanupTo(
            [self.surfaceShader(), self.displacementShader(), self.volumeShader()]
        )

    # **************************************************************************************************************** #
    def materialOtport(self):
        return self.bindOtport(u'material')


class Abs_GrhGeometryProxy(grhObjItf.Itf_GrhNodeProxy):
    def _initAbsGrhGeometryProxy(self, *args, **kwargs):
        self._initItfGrhNodeProxy(*args, **kwargs)

        self._portsetStackObj = self.CLS_grh__node_proxy__portset_stack(self)

    # **************************************************************************************************************** #
    def inputMaterialNamespaceString(self):
        return self._obj_proxy_cls__get_connect_obj_proxy_namespace_str_(self)

    # **************************************************************************************************************** #
    def property(self, *args):
        return self.bindPortProxy(*args)

    def hasProperty(self, *args):
        return self.hasBindPortProxy(*args)

    def properties(self):
        return [
            i
            for i in self.bindPortProxies()
            if i.bindObject().assignString() == self.DEF_grh__keyword__property
        ]

    def changedProperties(self):
        lis = []
        for portProxyObj in self.properties():
            portObj = portProxyObj.bindObject()
            if portObj.isChanged():
                lis.append(portProxyObj)
        return lis

    # **************************************************************************************************************** #
    def visibility(self, *args):
        return self.bindPortProxy(*args)

    def hasVisibility(self, *args):
        return self.hasBindPortProxy(*args)

    def visibilities(self):
        return [
            i
            for i in self.bindPortProxies()
            if i.bindObject().assignString() == self.DEF_grh__keyword__visibility
        ]

    def changedVisibilities(self):
        lis = []
        for i in self.visibilities():
            portObj = i.bindObject()
            if portObj.isChanged():
                lis.append(i)
        return lis

    # **************************************************************************************************************** #
    def materialInport(self):
        return self.bindInport(u'material')

    # **************************************************************************************************************** #
    def materialAsport(self):
        return self.bindAsport(u'materialassign')

    def hasAssignmentMaterials(self):
        return self.materialAsport().hasAssignmentNodes()

    def assignmentMaterials(self):
        return self.materialAsport().assignmentNodes()

    def assignmentMaterialProxies(self):
        namespaceStr = self.connectNamespaceString()
        return [i.proxy(namespaceStr) for i in self.assignmentMaterials() if i.hasProxy(namespaceStr)]

    # **************************************************************************************************************** #
    def _node_proxy__set_input_node_connect_(self, *args):
        geometryProxyObj, materialProxyObj = self, args[0]
        sourceObj, targetObj = materialProxyObj.materialOtport(), geometryProxyObj.materialInport()
        sourceObj.connectTo(targetObj)

    def _node_proxy__set_assignment_node_add_(self, *args):
        geometryProxyObj, materialProxyObj = self, args[0]
        # geometryProxyObj.materialAsport().restoreAssignment()
        geometryProxyObj.materialAsport().addAssignmentNode(materialProxyObj.bindObject())

    # **************************************************************************************************************** #
    def _geometry_proxy__set_propertyset_update_(self, *args):
        if self._portsetStackObj._obj_stack__get_obj_exist_(*args) is True:
            portsetObj = self._portsetStackObj._obj_stack__get_obj_(*args)
            portsetObj.restore()
        else:
            portsetObj = self.CLS_grh__node_proxy__portset(*args)
            self._portsetStackObj._obj_stack__set_obj_add_(portsetObj)

        portProxyObjList = self.changedProperties()
        if portProxyObjList:
            for portProxyObj in self.changedProperties():
                portsetObj.addPort(portProxyObj)

        return portsetObj

    def setPropertyset(self, portsetObj):
        self._portsetStackObj._obj_stack__set_obj_add_(portsetObj)

    def propertyset(self, *args):
        return self._portsetStackObj._obj_stack__get_obj_(*args)


# node graph ********************************************************************************************************* #
class Abs_GrhNodeGraph(grhObjItf.Itf_GrhNodeGraph):
    def _initAbsGrhNodeGraph(self, *args, **kwargs):
        self._initItfGrhNodeGraph(*args, **kwargs)


class Abs_GrhNodeGraphPortProxy(grhObjItf.Itf_GrhNodeGraphPortProxy):
    def _initAbsGrhNodeGraphPortProxy(self, *args, **kwargs):
        self._initAbsItfNodeGraphOtportProxy(*args, **kwargs)


# node translate ***************************************************************************************************** #
class Abs_GrhObjTranslator(grhObjItf.Itf_GrhObjTranslator):
    def _initAbsGrhObjTranslator(self, *args):
        self._initItfGrhObjTranslator(*args)


class Abs_GrhTrsNode(grhObjItf.Itf_GrhTrsNode):
    def _initAbsGrhTrsNode(self, *args):
        self._initItfGrhTrsNode(*args)


# node proxy translate *********************************************************************************************** #
class Abs_GrhTrsNodeProxy(grhObjItf.Itf_GrhTrsNodeProxy):
    def _initAbsGrhTrsNodeProxy(self, *args, **kwargs):
        self._initItfGrhTrsNodeProxy(*args, **kwargs)


class Abs_GrhTrsShaderProxy(grhObjItf.Itf_GrhTrsNodeProxy):
    def _initAbsGrhTrsShaderProxy(self, *args, **kwargs):
        self._initItfGrhTrsNodeProxy(*args, **kwargs)

        self._trs_shader_proxy__set_nodes_()

    # **************************************************************************************************************** #
    def _trs_shader_proxy__set_nodes_(self):
        srcNodeObjects = self._srcNodeObj.allInputNodes()
        for srcNodeObject in srcNodeObjects:
            srcTypepathStr = srcNodeObject.typepathString()
            srcNodepathStr = srcNodeObject.pathString()
            if self.CLS_grh__trs_node_proxy__trs_node.IST_grh__trs_node__obj_query_builder.hasSrcTypepath(srcTypepathStr):
                _trsNodeObject = self._grh__trs_node_proxy__get_trs_node_cache_obj_(srcNodepathStr)
            else:
                bscMethods.PyMessage.traceWarning(
                    u'''Source Typepath: "{}"; Node: "{}" is Unregistered.'''.format(
                        srcTypepathStr,
                        srcNodepathStr,
                    )
                )


class Abs_GrhTrsMaterialProxy(grhObjItf.Itf_GrhTrsNodeProxy):
    CLS_grh__trs_input_node_proxy = None

    VAR_grh__trs_src_source_portpath_list = []

    def _initAbsGrhTrsMaterialProxy(self, *args, **kwargs):
        self._initItfGrhTrsNodeProxy(*args, **kwargs)

        self._grh__trs_material_proxy__set_shaders_()

    # **************************************************************************************************************** #
    def _grh__trs_material_proxy__get_shader_connection_(self):
        pass

    def _grh__trs_material_proxy__set_shaders_(self):
        def getConnectionFnc_(_srcMaterialPortObj):
            if _srcMaterialPortObj.hasSource():
                _srcMaterialPortpathStr = _srcMaterialPortObj.portpathString()
                _srcShaderObj = _srcMaterialPortObj.source().node()
                _srcShaderNodepathStr = _srcShaderObj.pathString()
                return _srcMaterialPortpathStr, _srcShaderNodepathStr

        def getShaderConnectionFnc_(portpathRaw_):
            _srcMaterialPortpathStr, _srcShaderNodepathStr = None, None
            if isinstance(portpathRaw_, (str, unicode)):
                _srcMaterialPortpathStr = portpathRaw_
                if self._srcNodeObj.hasInport(_srcMaterialPortpathStr):
                    _srcMaterialPortObj = self._srcNodeObj.inport(_srcMaterialPortpathStr)
                    return getConnectionFnc_(_srcMaterialPortObj)
            elif isinstance(portpathRaw_, (tuple, list)):
                _srcMaterialPortObjs = [self._srcNodeObj.inport(_i) for _i in portpathRaw_ if self._srcNodeObj.hasInport(_i)]
                for i in _srcMaterialPortObjs:
                    if i.hasSource():
                        return getConnectionFnc_(i)

        tgtMaterialProxyObj = self.tgtNodeProxy()
        for arg in self.VAR_grh__trs_src_source_portpath_list:
            _ = getShaderConnectionFnc_(arg)
            if _ is not None:
                srcMaterialPortpathStr, srcShaderNodepathStr = _
                if srcShaderNodepathStr is not None:
                    connectNamespaceStr = tgtMaterialProxyObj.connectNamespaceString()
                    # proxy object
                    trsShaderProxyObj = self.CLS_grh__trs_input_node_proxy(
                        srcShaderNodepathStr,
                        namespace=connectNamespaceStr
                    )

                    tgtShaderObject = trsShaderProxyObj.tgtNode()
                    tgtMaterialPortObj = self.trsNode().tgtInport(srcMaterialPortpathStr)
                    tgtShaderPortObj = tgtShaderObject.otport()

                    tgtShaderPortObj.connectTo(tgtMaterialPortObj)


class Abs_GrhTrsGeometryProxy(grhObjItf.Itf_GrhTrsNodeProxy):
    CLS_grh__trs_input_node_proxy = None

    VAR_grh__trs_src_material_portpath = None

    def _initAbsGrhTrsGeometryProxy(self, *args, **kwargs):
        self._initItfGrhTrsNodeProxy(*args, **kwargs)

        self._trs_geometry_proxy__set_materials_()
        self._trs_geometry_proxy__set_ports_()

    # **************************************************************************************************************** #
    def _trs_geometry_proxy__get_src_binding_material_obj_list_(self):
        pass

    def _trs_geometry_proxy__get_src_port_obj_list_(self):
        pass

    # **************************************************************************************************************** #
    def _trs_geometry_proxy__set_materials_(self):
        tgtGeometryProxyObj = self.tgtNodeProxy()
        srcMaterialObjs = self._trs_geometry_proxy__get_src_binding_material_obj_list_()
        for srcMaterialObj in srcMaterialObjs:
            srcMaterialNodepathStr = srcMaterialObj.pathString()
            # material proxy namespace = geometry proxy namespace = look name
            materialNamespaceStr = tgtGeometryProxyObj.inputMaterialNamespaceString()
            trsMaterialProxyObj = self.CLS_grh__trs_input_node_proxy(
                srcMaterialNodepathStr,
                namespace=materialNamespaceStr
            )
            tgtMaterialProxyObj = trsMaterialProxyObj.tgtNodeProxy()
            tgtGeometryProxyObj.connectNodeProxyFrom(tgtMaterialProxyObj)

    def _trs_geometry_proxy__set_ports_(self):
        srcPortObjList = self._trs_geometry_proxy__get_src_port_obj_list_()
        if srcPortObjList:
            trsNodeQueryObj = self.trsNodeQuery()
            tgtNodeObj = self.tgtNode()
            for srcPortObj in srcPortObjList:
                srcPortpathStr = srcPortObj.portpathString()
                trsPortQueryObj = trsNodeQueryObj.trsPortQuery(srcPortpathStr)
                tgtPortpathStr = trsPortQueryObj.target_portpath
                if tgtNodeObj.hasInport(tgtPortpathStr):
                    tgtPortObj = tgtNodeObj.inport(tgtPortpathStr)
                    translatorCls = self.trsNode().CLS_grh__trs_node__obj_translator
                    srcPortraw = translatorCls._obj_translator__set_portraw_convert_(trsPortQueryObj, srcPortObj)
                    tgtPortObj.setPortraw(srcPortraw)
