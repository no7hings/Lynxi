# coding:utf-8
from LxBasic import bscMethods

from LxData import datObjAbs

from LxGraphic import grhObjAbs

from . import mtlCfg, mtlObjDef


class Def_XmlObject(mtlCfg.Utility):
    DEF_mtl_file_attribute_separator = u' '

    VAR_mtl_file_element_key = u''
    VAR_mtl_file_attribute_attach_key = u''

    def _initDefMtlObject(self):
        self._xmlIndentStr = ''

        self._xmlNamePrefixString = None
        self._xmlNameSuffixString = None

    def _xmlElementString_(self):
        return self.VAR_mtl_file_element_key

    def _setXmlNamePrefixString_(self, string):
        self._xmlNamePrefixString = string

    def _xmlNamePrefixString_(self):
        return self._xmlNamePrefixString

    def _setXmlNameSuffixString_(self, string):
        self._xmlNameSuffixString = string

    def _xmlNameSuffixString_(self):
        return self._xmlNameSuffixString

    def _xmlAttributeAttachKeyString_(self):
        return self.VAR_mtl_file_attribute_attach_key

    def _xmlAttributeAttachValueString_(self):
        pass

    @property
    def _xmlIndent_(self):
        return self._xmlIndentStr

    @_xmlIndent_.setter
    def _xmlIndent_(self, string):
        self._xmlIndentStr = string

    def _xmlAttributes_(self):
        pass

    def _xmlChildren_(self):
        pass

    def _xmlElements_(self):
        pass

    def _xmlAttributeAttaches_(self):
        """
        :return: list(tuple(key, value)/object instance of Def_XmlObject, ...)
        """
        pass

    @classmethod
    def _toXmlString(cls, elementObject, indent=4):
        def addPrefixFnc_(prefix_, lString, rString):
            lis.append(u'{}<{}{}'.format(lString, prefix_, rString))

        def addAttributeFnc_(attributeObject_, lString, rString):
            if attributeObject_ is not None:
                if isinstance(attributeObject_, Def_XmlObject):
                    attributeRaw = attributeObject_._xmlAttributeAttaches_()
                else:
                    attributeRaw = attributeObject_
                if isinstance(attributeRaw, (tuple, list)):
                    if attributeRaw:
                        for i in attributeRaw:
                            if isinstance(i, Def_XmlObject):
                                addAttributeFnc_(i, lString, rString)
                            else:
                                k, v = i
                                if v:
                                    lis.append(u'{}{}="{}"{}'.format(lString, k, v, rString))

        def addBranchFnc_(elementObject_, rString, parentElementObject=None):
            if parentElementObject is not None:
                lString = elementObject_._xmlIndent_
            else:
                lString = u''

            tagString = elementObject_._xmlElementString_()
            addPrefixFnc_(tagString, lString=lString, rString=u'')
            # Attribute
            attributes = elementObject_._xmlAttributes_()
            if attributes:
                [addAttributeFnc_(i, lString=cls.DEF_mtl_file_attribute_separator, rString=u'') for i in attributes]
            # Children
            children = elementObject_._xmlChildren_()
            if children:
                lis.append(u'>\r\n')

                for i in children:
                    if i is not None:
                        i._xmlIndent_ = lString + defIndentString
                        addBranchFnc_(i, rString=rString, parentElementObject=elementObject_)

                lis.append(u'{}</{}>\r\n'.format(lString, tagString))
            else:
                lis.append(u'{}/>\r\n'.format(cls.DEF_mtl_file_attribute_separator))

            elements = elementObject_._xmlElements_()
            if elements:
                for i in elements:
                    i._xmlIndent_ = lString
                    addBranchFnc_(i, rString=u'', parentElementObject=elementObject_)

        defIndentString = u' ' * indent
        lis = [
            u'<?xml version="1.0"?>\r\n',
        ]

        addBranchFnc_(elementObject, rString='')
        return u''.join(lis)

    def __str__(self):
        return self._toXmlString(self)

    def __repr__(self):
        return self._toXmlString(self)


# ******************************************************************************************************************** #
class Abs_MtlObjQueryCache(grhObjAbs.Abs_GrhObjQueryCache):
    VAR_mtl_node_file = None
    VAR_mtl_geometry_file = None
    VAR_mtl_material_file = None
    VAR_mtl_output_file = None
    VAR_mtl_port_child_file = None

    def _initAbsMtlObjQueryCache(self, *args):
        self._initAbsGrhObjQueryCache(*args)

        self._nodeRaws = bscMethods.OsJsonFile.read(
            self.VAR_mtl_node_file
        ) or {}
        self._materialRaws = bscMethods.OsJsonFile.read(
            self.VAR_mtl_material_file
        ) or {}
        self._geometryRaws = bscMethods.OsJsonFile.read(
            self.VAR_mtl_geometry_file
        ) or {}
        self._outputRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_output_file
        ) or {}
        self._portChildRaw = bscMethods.OsJsonFile.read(
            self.VAR_mtl_port_child_file
        ) or {}

        self._outNodeRaws = {}
        self._set_mtl_node_raws_build_()

    def _get_node_type_(self, *args):
        pass

    def _get_node_port_raws_(self, *args):
        pass

    def _get_node_raw_(self, *args):
        categoryString = args[0]
        return self._outNodeRaws[categoryString]

    # xml ************************************************************************************************************ #
    def _set_mtl_node_raws_build_(self):
        def getNodeRawFnc_(nodeRaws_):
            for categoryString, nodeRaw in nodeRaws_.items():
                raw = self.CLS_mtl_node_raw(
                    categoryString, nodeRaw, self._outputRaw, self._portChildRaw
                ).outRaw()
                self._outNodeRaws[categoryString] = raw

        getNodeRawFnc_(self._nodeRaws)
        getNodeRawFnc_(self._materialRaws)
        getNodeRawFnc_(self._geometryRaws)


class Abs_MtlObjCache(grhObjAbs.Abs_GrhObjCache):
    def _initAbsMtlObjCache(self, *args):
        self._initAbsGrhObjCache(*args)


# raw **************************************************************************************************************** #
class Abs_MtlRaw(
    datObjAbs.Abs_DatRaw,
    Def_XmlObject
):
    def _initAbsMtlRaw(self, *args):
        self._initAbsDatRaw(*args)

        self._initDefMtlObject()

    # xml ************************************************************************************************************ #
    def _xmlAttributes_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xmlAttributeAttachValueString_(self):
        if self._xmlNamePrefixString_() is not None:
            return u'{}{}'.format(self._xmlNamePrefixString_(), self.toString())
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abs_MtlNodename(
    datObjAbs.Abs_DatNodename,
    Def_XmlObject
):
    def _initAbsMtlNodename(self, *args):
        self._initAbsDatNodename(*args)

        self._initDefMtlObject()

    # **************************************************************************************************************** #
    def _xmlAttributes_(self):
        return [
            [('nodename', self.raw())]
        ]

    def _xmlAttributeAttachValueString_(self):
        if self._xmlNamePrefixString_() is not None:
            return u'{}{}'.format(self._xmlNamePrefixString_(), self.toString())
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abs_MtlPath(
    datObjAbs.Abs_DatPath,
    Def_XmlObject
):
    def _initAbsMtlPath(self, *args):
        self._initAbsDatPath(*args)

        self._initDefMtlObject()

    # **************************************************************************************************************** #
    def _xmlAttributes_(self):
        return [
            [('nodename', self.raw())]
        ]

    def _xmlAttributeAttachValueString_(self):
        if self._xmlNamePrefixString_() is not None:
            return u'{}{}'.format(self._xmlNamePrefixString_(), self.toString())
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# object set ********************************************************************************************************* #
class Abs_MtlObjSet(
    grhObjAbs.Abs_GrhObjSet,
    Def_XmlObject
):
    def _initAbsMtlObjSet(self, *args):
        self._initAbsGrhObjSet(*args)

        self._initDefMtlObject()

    # **************************************************************************************************************** #
    def _xmlAttributeAttachValueString_(self):
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# value ************************************************************************************************************** #
class Abs_MtlValue(
    datObjAbs.Abs_DatValue,
    Def_XmlObject
):

    def _initAbsMtlValue(self, *args):
        self._initAbsDatValue(*args)

        self._initDefMtlObject()

    # **************************************************************************************************************** #
    def _xmlAttributes_(self):
        return [
            self.datatype(), self.data()
        ]

    def _xmlAttributeAttachValueString_(self):
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# ******************************************************************************************************************** #
class Abs_MtlPort(
    Def_XmlObject,
    grhObjAbs.Abs_GrhPort
):
    def _initAbsMtlPort(self, *args):
        self._initAbsGrhPort(*args)

        self._initDefMtlObject()

        self._proxyObj = None

    # xml ************************************************************************************************************ #
    def _set_proxy_(self, obj):
        self._proxyObj = obj

    def _xmlAttributeAttachValueString_(self):
        return self.portpathString()

    def _xmlAttributeAttaches_(self):
        if self.hasParent() is True:
            return [
                self.parent(),
                (self._xmlAttributeAttachKeyString_(), self.portnameString())
            ]
        else:
            return [
                self.node(),
                (self._xmlAttributeAttachKeyString_(), self.portpathString())
            ]

    def _xmlAttributes_(self):
        return [
            self.portpath(),
            self.porttype(),
            self.portgiven()
        ]


class Abs_MtlNode(
    Def_XmlObject,
    grhObjAbs.Abs_GrhNode
):
    def _initAbsMtlNode(self, *args):
        self._initAbsGrhNode(*args)

        self._initDefMtlObject()

        self._proxyObj = None

    # xml ************************************************************************************************************ #
    def _set_proxy_(self, obj):
        self._proxyObj = obj

    def _xmlElementString_(self):
        return self.categoryString()

    def _xmlAttributes_(self):
        return [
            self.nodepath(),
            self.type()
        ]

    def _xmlChildren_(self):
        return self._get_changed_inputs_()

    def _xmlAttributeAttachValueString_(self):
        return self.nodepathString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# port proxy ********************************************************************************************************* #
class Abc_MtlPortProxy(Def_XmlObject):
    CLS_mtl_name = None

    def _initAbcMtlPortProxy(self, *args):
        self._portObj = args[0]
        self._portObj._set_proxy_(self)

        self._nameObj = self.CLS_mtl_name(self._portObj.portpathString())

    def port(self):
        return self._portObj

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def setNameString(self, nameString):
        self._nameObj.setRawString(nameString)

    def _queryKeyString_(self):
        return self._portObj.portpathString()

    def _xmlAttributes_(self):
        return [
            self._portObj.portpath(),
            self._portObj.porttype(),
            self._portObj.value()
        ]


class Abc_MtlBindInput(Abc_MtlPortProxy):
    def _initAbcMtlBindInput(self, *args):
        self._initAbcMtlPortProxy(*args)

        self._nodeGraphOutputObj = None

    def _setNodeGraphOutput_(self, nodeGraphOutputObject):
        self._nodeGraphOutputObj = nodeGraphOutputObject

    def portgiven(self):
        if self._portObj.hasSource() is True:
            return self._nodeGraphOutputObj
        return self._portObj.value()

    def _xmlAttributes_(self):
        return [
            self._portObj.portpath(),
            self._portObj.porttype(),
            self.portgiven()
        ]


class Abc_MtlProperty(Abc_MtlPortProxy):
    def _initAbcMtlProperty(self, *args):
        self._initAbcMtlPortProxy(*args)


class Abs_MtlVisibility(Abc_MtlPortProxy):
    def _initAbsMtlVisibility(self, *args):
        self._initAbcMtlPortProxy(*args)


# node graph output
class Abc_MtlNodeGraphOutput(Abc_MtlPortProxy):

    def _initAbcMtlNodeGraphOutput(self, *args):
        self._initAbcMtlPortProxy(*args)

        self._nameObj = self.CLS_mtl_name(self._portObj.attrpathString())

        self._nodeGraphObj = None

    def _setNodeGraph_(self, nodeGraphObject):
        self._nodeGraphObj = nodeGraphObject

    def _setPort_(self, portObject):
        self._portObj = portObject

    def porttype(self):
        return self._portObj.porttype()

    def nodeGraph(self):
        return self._nodeGraphObj

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj,
            self._portObj.porttype(),
            self._portObj
        ]

    def _xmlAttributeAttachValueString_(self):
        return self._nameObj._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            self.nodeGraph(),
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# ******************************************************************************************************************** #
class Abc_MtlObjectProxy(Def_XmlObject):
    CLS_mtl_name = None
    CLS_mtl_node = None

    def _initAbcMtlObjectProxy(self, *args):
        self._getProxyNode_(*args)

    def _getProxyNode_(self, *args):
        if isinstance(args[0], Abs_MtlNode):
            self._nodeObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            self._nodeObj = self.CLS_mtl_node(*args)

        self._nodeObj._set_proxy_(self)

        self._nameObj = self.CLS_mtl_name(
            self._nodeObj.nodepathString()
        )

    def _queryKeyString_(self):
        return self._nodeObj.nodepathString()

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def node(self):
        return self._nodeObj

    def toString(self):
        return self._nodeObj.nodepathString()


class Abc_MtlShaderProxy(Abc_MtlObjectProxy):
    CLS_mtl_node_graph_set = None
    CLS_mtl_node_graph = None

    CLS_mtl_port_proxy_set = None
    CLS_mtl_port_proxy = None

    def _initAbcMtlShaderProxy(self, *args):
        self._initAbcMtlObjectProxy(*args)
        self._getProxyPorts_()

        self._nodeGraphSetObj = self.CLS_mtl_node_graph_set(
            self
        )
        self._addNodeGraph_()

    def _getProxyPorts_(self):
        self._bindInputSetObj = self.CLS_mtl_port_proxy_set(self.node().nodepathString())

        for i in self._nodeObj.inputs():
            portProxyObject = self.CLS_mtl_port_proxy(i)
            self._bindInputSetObj._set_obj_add_(portProxyObject)

    def _updateNodeGraphs_(self):
        if self.hasNodeGraphs():
            nodeGraphObject = self.nodeGraph(0)

            materialProxyObject = self._getMaterialProxy_()
            if materialProxyObject is not None:
                nodeGraphObject.name()._setXmlNamePrefixString_(
                    u'{}/'.format(
                        materialProxyObject.name()._xmlAttributeAttachValueString_()
                    )
                )

            nodeGraphObject._update_(self.node())

    def _addNodeGraph_(self):
        nodeGraphObject = self.CLS_mtl_node_graph()

        nodeGraphObject.setNameString(
            self._nodeObj.nameString()
        )
        self._nodeGraphSetObj.addObject(nodeGraphObject)

    def _getMaterialContext_(self):
        for i in self._nodeObj.outputs():
            if i.hasTargets():
                targets = i.targets()
                for target in targets:
                    proxyNodeObject = target.node()._proxyObj
                    if isinstance(proxyNodeObject, Abc_MtlMaterialProxy):
                        return target.portnameString()

    def _getMaterialProxy_(self):
        for i in self._nodeObj.outputs():
            if i.hasTargets():
                targets = i.targets()
                for target in targets:
                    proxyNodeObject = target.node()._proxyObj
                    if isinstance(proxyNodeObject, Abc_MtlMaterialProxy):
                        return proxyNodeObject

    def bindInput(self, portnameString):
        return self._bindInputSetObj.object(portnameString)

    def bindInputs(self):
        return self._bindInputSetObj.objects()

    def hasNodeGraphs(self):
        return self._nodeGraphSetObj.hasObjects()

    def hasNodeGraph(self, nameString):
        return self._nodeGraphSetObj._get_obj_exist_(nameString)

    def nodeGraph(self, nameString):
        return self._nodeGraphSetObj._get_obj_(nameString)

    def nodeGraphs(self):
        return self._nodeGraphSetObj.objects()

    def _getChangedBindInputs_(self):
        lis = []
        portProxyObjects = self.bindInputs()
        if portProxyObjects:
            for portProxyObject in portProxyObjects:
                portObject = portProxyObject.port()
                if portObject.isChanged():
                    lis.append(portProxyObject)
        return lis

    def _xmlAttributes_(self):
        return [
            self._nodeObj.nodepath(),
            self._nodeObj.category(),
            [(u'context', self._getMaterialContext_())]
        ]

    def _xmlChildren_(self):
        return self._getChangedBindInputs_()


class Abc_MtlMaterialProxy(Abc_MtlObjectProxy):
    def _initAbcMtlMaterialProxy(self, *args):
        self._initAbcMtlObjectProxy(*args)

    def _getProxyNode_(self, *args):
        if isinstance(args[0], Abs_MtlNode):
            self._nodeObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            nodepathString = args[0]
            self._nodeObj = self.CLS_mtl_node(self.DEF_mtl_category_material, nodepathString)

        self._nodeObj._set_proxy_(self)

        self._nameObj = self.CLS_mtl_name(self._nodeObj.nodepathString())

    def surfaceInput(self):
        return self._nodeObj.port(u'surfaceshader')

    def connectSurfaceFrom(self, portObject):
        portObject.connectTo(self.surfaceInput())

    def surfaceShader(self):
        if self.surfaceInput().hasSource():
            return self.surfaceInput().source().node()._proxyObj

    def displacementInput(self):
        return self._nodeObj.port(u'displacementshader')

    def connectDisplacementFrom(self, portObject):
        portObject.connectTo(self.displacementInput())

    def displacementShader(self):
        if self.displacementInput().hasSource():
            return self.displacementInput().source().node()._proxyObj

    def volumeInput(self):
        return self._nodeObj.port(u'volumeshader')

    def connectVolumeFrom(self, portObject):
        portObject.connectTo(self.volumeInput())

    def volumeShader(self):
        if self.volumeInput().hasSource():
            return self.volumeInput().source().node()._proxyObj

    def shaders(self):
        return bscMethods.List.cleanupTo(
            [self.surfaceShader(), self.displacementShader(), self.volumeShader()]
        )

    def _xmlAttributes_(self):
        return [
            self.name()
        ]

    def _xmlChildren_(self):
        # update shader's node graph first
        for proxyObject in self.shaders():
            proxyObject._updateNodeGraphs_()
        return self.shaders()

    def _xmlElements_(self):
        lis = []
        for proxyObject in self.shaders():
            nodeGraphs = proxyObject.nodeGraphs()
            if nodeGraphs:
                for nodeGraph in nodeGraphs:
                    if nodeGraph.hasNodes():
                        if not nodeGraph in lis:
                            lis.append(nodeGraph)
        return lis

    def _xmlAttributeAttachValueString_(self):
        return self.name()._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abc_MtlGeometryProxy(Abc_MtlObjectProxy):
    CLS_mtl_port_proxy_set = None
    CLS_mtl_property = None
    CLS_mtl_visibility = None

    CLS_mtl_propertyset = None

    def _initAbcMtlGeometryProxy(self, *args):
        self._initAbcMtlObjectProxy(*args)
        self._getProxyPorts_()

        self._propertysetObj = self.CLS_mtl_propertyset(self.nameString())

    def _getProxyNode_(self, *args):
        if isinstance(args[0], Abs_MtlNode):
            self._nodeObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            nodepathString = args[0]
            self._nodeObj = self.CLS_mtl_node(self.DEF_mtl_category_mesh, nodepathString)

        self._nodeObj._set_proxy_(self)

        self._nameObj = self.CLS_mtl_name(self._nodeObj.nodepathString())

    def _getProxyPorts_(self):
        self._propertySetObj = self.CLS_mtl_port_proxy_set(self._nodeObj)
        self._visibilitySetObj = self.CLS_mtl_port_proxy_set(self._nodeObj)

        for portObject in self._nodeObj.params():
            assignString = portObject.typeString()
            if assignString == self.DEF_mtl_keyword_property:
                propertyObject = self.CLS_mtl_property(portObject)
                self._propertySetObj._set_obj_add_(propertyObject)
            elif assignString == self.DEF_mtl_keyword_visibility:
                visibilityObject = self.CLS_mtl_visibility(portObject)
                self._visibilitySetObj._set_obj_add_(visibilityObject)

    def _updatePropertyset_(self):
        self._propertysetObj._initializeSets_()

        for i in self.changedProperties():
            self._propertysetObj.addPort(i)

    def property(self, portnameString):
        return self._propertySetObj.object(portnameString)

    def properties(self):
        return self._propertySetObj.objects()

    def changedProperties(self):
        lis = []
        for i in self.properties():
            portObject = i.port()
            if portObject.isChanged():
                lis.append(i)
        return lis

    def visibility(self, portnameString):
        return self._visibilitySetObj.object(portnameString)

    def hasVisibility(self, *args):
        return self._visibilitySetObj._get_obj_exist_(*args)

    def visibilities(self):
        return self._visibilitySetObj.objects()

    def changedVisibilities(self):
        lis = []
        for i in self.visibilities():
            portObject = i.port()
            if portObject.isChanged():
                lis.append(i)
        return lis

    def connectMaterial(self, materialProxyObject):
        materialProxyObject.node().output(u'material').connectTo(self.node().input(u'material'))

    def material(self):
        if self.node().input(u'material').hasSource():
            nodeObject = self.node().input(u'material').source().node()
            return nodeObject._proxyObj

    def setPropertyset(self, propertysetObject):
        self._propertysetObj = propertysetObject

    def propertyset(self):
        return self._propertysetObj

    def _xmlAttributes_(self):
        return [
            self._nodeObj.nodepath(),
            self._nodeObj.category()
        ]

    def _xmlChildren_(self):
        return self.changedProperties() + self.changedVisibilities()


# node graph
class Abc_MtlNodeGraph(Def_XmlObject):
    CLS_mtl_name = None

    CLS_mtl_node_set = None
    CLS_mtl_node_graph_output_set = None

    CLS_mtl_node = None
    CLS_mtl_node_graph_output = None

    def _initAbcMtlNodeGraph(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._nodeSetObj = self.CLS_mtl_node_set()
        self._nodeGraphOutputSetObj = self.CLS_mtl_node_graph_output_set()

        self._nodeGraphOutputDict = {}

        self._initDefMtlObject()

    @staticmethod
    def _getNodes_(nodeObject):
        def recursionFnc_(nodeObject_):
            for i in nodeObject_.inputs():
                if i.hasSource():
                    _nodeObject = i.source().node()
                    if not _nodeObject in lis:
                        lis.append(_nodeObject)
                        recursionFnc_(_nodeObject)

        lis = []
        recursionFnc_(nodeObject)
        return lis

    @staticmethod
    def _getPorts_(nodeObject):
        lis = []
        for i in nodeObject.inputs():
            if i.hasSource():
                lis.append(i)
        return lis

    def _update_(self, nodeObject):
        [self._addNode_(i) for i in self._getNodes_(nodeObject)]
        [self._addPort_(i) for i in self._getPorts_(nodeObject)]

    def _addNode_(self, *args):
        if isinstance(args[0], (str, unicode)):
            nodeObject = self.CLS_mtl_node(*args)
        else:
            nodeObject = args[0]

        if self._nodeSetObj._get_obj_exist_(nodeObject) is False:
            self._nodeSetObj.addObject(nodeObject)

    def _addPort_(self, *args):
        portObject = args[0]

        sourceObject = portObject.source()
        count = self._nodeGraphOutputSetObj.objectCount()

        keyString = sourceObject.attrpathString()
        if self._nodeGraphOutputSetObj._get_obj_exist_(keyString) is False:
            nameString = u'output_{}'.format(count)
            nodeGraphOutputObject = self.CLS_mtl_node_graph_output(sourceObject)
            nodeGraphOutputObject.setNameString(nameString)
            nodeGraphOutputObject._setNodeGraph_(self)
            self._nodeGraphOutputSetObj._set_obj_add_(keyString, nodeGraphOutputObject)
        else:
            nodeGraphOutputObject = self._nodeGraphOutputSetObj._get_obj_(keyString)

        portObject._proxyObj._setNodeGraphOutput_(nodeGraphOutputObject)

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

    def outputs(self):
        """
        :return: list(object or output, ...)
        """
        return self._nodeGraphOutputSetObj.objects()

    def output(self, portpathString=None):
        """
        :param portpathString: str
        :return: object of Output
        """
        return self._nodeGraphOutputSetObj.object(portpathString)

    def hasOutputs(self):
        """
        :return: bool
        """
        return self._nodeGraphOutputSetObj.hasObjects()

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj
        ]

    def _xmlChildren_(self):
        return self.nodes() + self.outputs()

    def _xmlAttributeAttachValueString_(self):
        return self.name()._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# portset ************************************************************************************************************ #
class Abc_MtlPortset(Def_XmlObject):
    CLS_mtl_name = None

    CLS_grh_port_set = None
    
    def _initAbcMtlPortset(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._portSetObj = self.CLS_grh_port_set()

        self._initDefMtlObject()

    def _initializeSets_(self):
        self._portSetObj._initializeData_()

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

    def addPort(self, portObject):
        self._portSetObj.addObject(portObject)

    def addPorts(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addPort(i) for i in _]

    def ports(self):
        return self._portSetObj.objects()

    def hasPorts(self):
        return self._portSetObj.hasObjects()

    def _xmlAttributeAttachValueString_(self):
        return self.name()._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]

    def _xmlAttributes_(self):
        return [
            self.name()
        ]

    def _xmlChildren_(self):
        return self.ports()


# portset > propertyset
class Abc_MtlPropertyset(Abc_MtlPortset):
    def _initAbcMtlPropertyset(self, *args):
        self._initAbcMtlPortset(*args)


# geometry collection
class Abc_MtlCollection(Def_XmlObject):
    CLS_mtl_name = None

    CLS_mtl_geometry_set = None
    CLS_mtl_collection_set = None

    DEF_geometry_separator = None

    def _initAbcMtlCollection(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_mtl_geometry_set()
        self._collectionSetObj = self.CLS_mtl_collection_set()
        self._excludeGeometrySetObj = self.CLS_mtl_geometry_set()

        self._initDefMtlObject()

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

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Geometry
        :return:
        """
        self._geometrySetObj.addObject(geometryObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addGeometry(i) for i in list(_)]

    def geometries(self):
        """
        :return: list(object or geometry, ...)
        """
        return self._geometrySetObj.objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self._geometrySetObj.hasObjects()

    def geometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nodepathString() for i in self.geometries()]

    def fullpathGeometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nodepathString() for i in self.geometries()]

    def excludeGeometrySet(self):
        return self._excludeGeometrySetObj

    def addExcludeGeometry(self, geometryObject):
        self._excludeGeometrySetObj.addObject(geometryObject)

    def addExcludeGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addExcludeGeometry(i) for i in list(_)]

    def excludeGeometries(self):
        return self._excludeGeometrySetObj.objects()

    def collectionSet(self):
        return self._collectionSetObj

    def addCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self._collectionSetObj.addObject(collectionObject)

    def hasCollections(self):
        """
        :return: bool
        """
        return self._collectionSetObj.hasObjects()

    def collections(self):
        """
        :return: list(object of Collection, ...)
        """
        return self._collectionSetObj.objects()

    def collectionNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nameString() for i in self.collections()]

    def toString(self):
        return self.nameString()

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj,
            self._geometrySetObj,
            self.collectionSet(),
            self.excludeGeometrySet()
        ]

    def _xmlAttributeAttachValueString_(self):
        return self.nameString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# assign ************************************************************************************************************* #
class Abc_MtlAssign(Def_XmlObject):
    CLS_mtl_name = None
    CLS_mtl_geometry_set = None

    DEF_geometry_separator = None

    def _initAbcMtlAssign(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_mtl_geometry_set(
            self.nameString()
        )
        self._collectionObj = None

        self._lookObj = None

        self._initDefMtlObject()

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
        self._nameObj._set_rawstr_create_(nameString)

    def _addGeometry_(self, *args):
        geometryObject = args[0]
        self._geometrySetObj.addObject(geometryObject)

    def hasGeometry(self, *args):
        return self._geometrySetObj._get_obj_exist_(*args)

    def addGeometry(self, geometryObject):
        """
        :param geometryObject: object of Geometry
        :return: None
        """
        self._addGeometry_(geometryObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addGeometry(i) for i in list(_)]

    def geometries(self):
        """
        :return: list(object or geometry, ...)
        """
        return self._geometrySetObj.objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self._geometrySetObj.hasObjects()

    def geometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nameString() for i in self.geometries()]

    def fullpathGeometrynameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nodepathString() for i in self.geometries()]

    def setCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self._collectionObj = collectionObject

    def collection(self):
        """
        :return: object of Collection
        """
        return self._collectionObj

    def collectionName(self):
        """
        :return: str
        """
        return self._collectionObj.nameString()

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlElementAttaches_(self):
        pass


class Abc_MtlMaterialAssign(Abc_MtlAssign):
    def _initAbcMtlMaterialAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._materialProxyObj = None

    def setMaterial(self, materialProxyObject):
        """
        :param materialProxyObject: object of MaterialProxy
        :return:
        """
        self._materialProxyObj = materialProxyObject

    def material(self):
        """
        :return: object of ShaderSet
        """
        return self._materialProxyObj

    def _xmlElementAttaches_(self):
        return [
            self._materialProxyObj,
            self._collectionObj
        ]

    def _xmlAttributeAttachValueString_(self):
        self.nameString()

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.material(),
            self._geometrySetObj,
            self.collection()
        ]


class Abc_MtlPropertyAssign(Abc_MtlAssign):
    def _initAbcMtlPropertyAssign(self, *args):
        pass


class Abc_MtlPropertysetAssign(Abc_MtlAssign):
    CLS_mtl_propertyset = None

    def _initAbcMtlPropertysetAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._propertysetObj = None

    def _setPropertyset_(self, *args):
        if isinstance(args[0], (str, unicode)):
            propertysetObject = self.CLS_mtl_propertyset(args[0])
        else:
            propertysetObject = args[0]
        self._propertysetObj = propertysetObject
        return self._propertysetObj

    def setPropertyset(self, *args):
        """
        :param args:
            1.str
            2.instance of "Propertyset"
        :return: instance of "Propertyset"
        """
        return self._setPropertyset_(*args)

    def hasPropertyset(self):
        return self._propertysetObj is not None

    def propertyset(self):
        """
        :return: object of Propertyset
        """
        return self._propertysetObj

    def _xmlElementAttaches_(self):
        return [
            self._propertysetObj,
            self._collectionObj
        ]

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.propertyset(),
            self._geometrySetObj,
            self.collection()
        ]


class Abc_MtlVisibilityAssign(Abc_MtlAssign):
    CLS_grh_type = None
    CLS_value_visibility = None

    CLS_set_geometry_viewer = None

    OBJ_grh_query_cache = None

    def _initAbcMtlVisibilityAssign(self, *args):
        self._initAbcMtlAssign(*args)

        self._vistypeObj = None

        self._visibilityValueObj = None

        self._viewerGeometrySetObj = self.CLS_set_geometry_viewer()

    def type(self):
        return self._vistypeObj

    def setTypeString(self, portnameString):
        self._vistypeObj = self.CLS_grh_type(portnameString)

        portdataString = self.OBJ_grh_query_cache.nodeDef(self.DEF_mtl_category_mesh).port(portnameString).portdata

        self._visibilityValueObj = self.CLS_value_visibility(portdataString)

    def typeString(self):
        return self._vistypeObj.toString()

    def visible(self):
        return self._visibilityValueObj

    def setGeometryVisibility(self, geometryVisibilityObject):
        visibilityString = geometryVisibilityObject.portpathString()
        self._vistypeObj = self.CLS_grh_type(visibilityString)

        self._visibilityValueObj = geometryVisibilityObject.value()

    def addViewerGeometry(self, geometryObject):
        self._viewerGeometrySetObj.addObject(geometryObject)

    def viewerGeometries(self):
        return self._viewerGeometrySetObj.objsets()

    def _xmlElementAttaches_(self):
        return [
            self._collectionObj
        ]

    def _xmlAttributes_(self):
        return [
            self.name(),
            self.type(),
            self.visible(),
            self._geometrySetObj,
            self._viewerGeometrySetObj,
            self.collection()
        ]


# ******************************************************************************************************************** #
class Abc_MtlLook(Def_XmlObject):
    CLS_mtl_name = None

    CLS_mtl_assign_set = None

    CLS_mtl_visibility = None
    CLS_mtl_visibility_set = None

    CLS_mtl_material_assign = None
    CLS_mtl_material_assign_set = None

    CLS_mtl_propertyset_assign = None
    CLS_mtl_propertyset_assign_set = None

    CLS_mtl_geometry_set = None

    def _initAbcMtlLook(self, *args):
        nameString = args[0]
        self._nameObj = self.CLS_mtl_name(nameString)

        self._visibilitySetObj = self.CLS_mtl_visibility_set(nameString)
        self._materialAssignSetObj = self.CLS_mtl_material_assign_set(nameString)
        self._propertysetAssignSetObj = self.CLS_mtl_propertyset_assign_set(nameString)

        self._assignSetObj = self.CLS_mtl_assign_set(nameString)
        self._geometrySetObj = self.CLS_mtl_geometry_set(nameString)

        self._initDefMtlObject()

    def _addGeometryProxy_(self, *args):
        geometryProxyObject = args[0]
        self._geometrySetObj.addObject(geometryProxyObject)

    def _updateAssigns_(self):
        for i in self._geometrySetObj.objects():
            self._addGeometryMaterialAssigns_(i)
            self._addGeometryPropertyAssigns_(i)
            self._addGeometryVisibilities_(i)

    def _addGeometryMaterialAssigns_(self, geometryProxyObject):
        def addFnc_(geometryObject_, materialProxyObject_):
            materialObject_ = materialProxyObject_.node()
            materialProxyObject_.name()._setXmlNamePrefixString_(
                u'{}/'.format(self.nameString())
            )
            _count = self._materialAssignSetObj.objectCount()
            _keyString = materialObject_.nodepathString()
            if self._materialAssignSetObj._get_obj_exist_(_keyString):
                _materialAssignObject = self._materialAssignSetObj._get_obj_(_keyString)
            else:
                _materialAssignObject = self.CLS_mtl_material_assign(
                    'materialassign_{}'.format(_count)
                )
                _materialAssignObject.setMaterial(materialProxyObject_)
                self._materialAssignSetObj._set_obj_add_(_keyString, _materialAssignObject)

            if _materialAssignObject.hasGeometry(geometryObject_) is False:
                _materialAssignObject.addGeometry(geometryObject_)

        materialProxyObject = geometryProxyObject.material()
        if materialProxyObject is not None:
            addFnc_(geometryProxyObject, materialProxyObject)

    def _addGeometryPropertyAssigns_(self, geometryProxyObject):
        def addFnc_(geometryObject_, propertysetObject_):
            propertysetObject_.name()._setXmlNamePrefixString_(
                u'{}'.format(self.nameString())
            )
            _count = self._propertysetAssignSetObj.objectCount()
            _keyString = geometryObject_.node().nodepathString()
            if self._propertysetAssignSetObj._get_obj_exist_(_keyString):
                _propertysetAssignObject = self._propertysetAssignSetObj._get_obj_(_keyString)
            else:
                _propertysetAssignObject = self.CLS_mtl_propertyset_assign(
                    propertysetObject_.name()._xmlAttributeAttachValueString_()
                )
                self._propertysetAssignSetObj._set_obj_add_(_keyString, _propertysetAssignObject)

            _propertysetAssignObject.setPropertyset(propertysetObject_)
            if _propertysetAssignObject.hasGeometry(geometryObject_) is False:
                _propertysetAssignObject.addGeometry(geometryObject_)

        geometryProxyObject._updatePropertyset_()
        propertysetObject = geometryProxyObject.propertyset()
        if propertysetObject.hasPorts():
            addFnc_(geometryProxyObject, propertysetObject)

    def _addGeometryVisibilities_(self, geometryProxyObject):
        def addFnc_(geometryObject_, portProxyObject_):
            _portObject = portProxyObject_.port()
            _count = self._visibilitySetObj.objectCount()
            _keyString = _portObject.portpathString()
            if self._visibilitySetObj._get_obj_exist_(_keyString):
                _visibilityObject = self._visibilitySetObj._get_obj_(_keyString)
            else:
                _visibilityObject = self.CLS_mtl_visibility(
                    'visibility_{}'.format(_count)
                )
                _visibilityObject.setGeometryVisibility(_portObject)
                self._visibilitySetObj._set_obj_add_(_keyString, _visibilityObject)

            if _visibilityObject.hasGeometry(geometryObject_) is False:
                _visibilityObject.addGeometry(geometryObject_)

        geometryVisibilities = geometryProxyObject.changedVisibilities()
        if geometryVisibilities:
            [addFnc_(geometryProxyObject, i) for i in geometryVisibilities]

    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    def geometries(self):
        return self._geometrySetObj.objects()

    def hasGeometries(self):
        return self._geometrySetObj.hasObjects()

    def addGeometry(self, geometryProxyObject):
        self._addGeometryProxy_(geometryProxyObject)

    def addGeometries(self, *args):
        if isinstance(args[0], (tuple, list)):
            [self.addGeometry(i) for i in list(args[0])]
        else:
            [self.addGeometry(i) for i in list(args)]

    def geometry(self, geometryString):
        return self._geometrySetObj.object(geometryString)

    def hasGeometry(self, *args):
        return self._geometrySetObj._get_obj_exist_(*args)

    def materialAssigns(self):
        return self._materialAssignSetObj.objects()

    def propertysetAssigns(self):
        return self._propertysetAssignSetObj.objects()

    def visibilities(self):
        return self._visibilitySetObj.objects()

    def hasAssigns(self):
        return self.assigns() != []

    def assigns(self):
        return self.materialAssigns() + self.propertysetAssigns() + self.visibilities()

    def _xmlElementAttaches_(self):
        lis = []
        for assignObject in self.assigns():
            for xmlObject in assignObject._xmlElementAttaches_():
                if xmlObject is not None:
                    if xmlObject not in lis:
                        lis.append(xmlObject)
        return lis

    def _queryKeyString_(self):
        return self.nameString()

    def _xmlAttributes_(self):
        return [
            self._nameObj
        ]

    def _xmlChildren_(self):
        self._updateAssigns_()
        return self.assigns()

    def _xmlElements_(self):
        return self._xmlElementAttaches_()


class Abc_MtlFile(Def_XmlObject):
    CLS_mtl_filepath = None

    CLS_mtl_version = None

    CLS_mtl_reference_set = None
    CLS_mtl_reference = None

    CLS_mtl_look_set = None
    CLS_mtl_look = None

    VAR_mtlx_version = None

    def _initAbcMtlFile(self, *args):
        self._filepathObj = self.CLS_mtl_filepath(*args)
        self._versionObj = self.CLS_mtl_version(self.VAR_mtlx_version)

        self._referenceSetObj = self.CLS_mtl_reference_set()
        self._lookSetObj = self.CLS_mtl_look_set()

        self._initDefMtlObject()

    def _addLook_(self, *args):
        if isinstance(args[0], (str, unicode)):
            lookObject = self.CLS_mtl_look(args[0])
        elif isinstance(args[0], self.CLS_mtl_look):
            lookObject = args[0]
        else:
            lookObject = self.CLS_mtl_look(u'default_look')
        self._lookSetObj.addObject(lookObject)
        return lookObject

    def _addReference_(self, *args):
        if self.CLS_mtl_reference is not None:
            referenceCls = self.CLS_mtl_reference
        else:
            referenceCls = self.__class__

        if isinstance(args[0], (str, unicode)):
            fileObject = referenceCls(args[0])
        elif isinstance(args[0], referenceCls):
            fileObject = args[0]
        else:
            fileObject = referenceCls(u'default')

        keyString = fileObject.fullpathFilename()
        self._lookSetObj._set_obj_add_(keyString, fileObject)

    def filepath(self):
        return self._filepathObj

    def fullpathFilename(self):
        return self._filepathObj.toString()

    def version(self):
        return self._versionObj

    def versionString(self):
        return self._versionObj.toString()

    def addReference(self, fileObject):
        self._addReference_(fileObject)

    def references(self):
        return self._lookSetObj.objects()

    def reference(self, fileString):
        return self._lookSetObj.object(fileString)

    def hasLook(self, lookString):
        return self._lookSetObj._get_obj_exist_(lookString)

    def addLook(self, *args):
        """
        :param args:
            1.str
            2.instance of "Look"
        :return:
        """
        return self._addLook_(*args)

    def looks(self):
        return self._lookSetObj.objects()

    def look(self, lookString):
        return self._lookSetObj.object(lookString)

    def save(self):
        xmlDoc = self.__str__()
        bscMethods.OsFile.write(
            self.fullpathFilename(), xmlDoc
        )

    def _xmlAttributes_(self):
        return [
            self.version()
        ]

    def _xmlChildren_(self):
        return self.looks()


class Abc_MtlReference(Abc_MtlFile):
    def _initAbcMtlReference(self, *args):
        self._initAbcMtlFile(*args)

    def _queryKeyString_(self):
        return self.fullpathFilename()

    def _xmlAttributes_(self):
        return [
            self._filepathObj
        ]


# ******************************************************************************************************************** #
class Abc_MtlTrsBasic(mtlCfg.Utility):
    def _initAbcMtlTrsBasic(self):
        pass


# translate ********************************************************************************************************** #
class Abc_MtlDccTranslator(mtlCfg.Utility):
    OBJ_mtl_trs_query_cache = None

    VAR_mtl_channel_convert_dict = {
        mtlCfg.Utility.DEF_mtl_porttype_color3: {
            u'category': u'float_to_rgb',
            u'output_portname': u'rgb',
            u'connect': {
                u'rgb.r': u'r',
                u'rgb.g': u'g',
                u'rgb.b': u'b'
            }
        },
        mtlCfg.Utility.DEF_mtl_porttype_vector3: {
            u'category': u'float_to_rgb',
            u'output_portname': u'vector',
            u'connect': {
                u'vector.x': u'r',
                u'vector.y': u'b',
                u'vector.z': u'b',
            }
        },
        mtlCfg.Utility.DEF_mtl_porttype_color4: {
            u'category': u'float_to_rgba',
            u'output_portname': u'rgba',
            u'connect': {
                u'rgba.r': u'r',
                u'rgba.g': u'g',
                u'rgba.b': u'b',
                u'rgba.a': u'a'
            }
        },
        mtlCfg.Utility.DEF_mtl_porttype_vector4: {
            u'category': u'float_to_rgba',
            u'output_portname': u'vector',
            u'connect': {
                u'vector.x': u'r',
                u'vector.y': u'b',
                u'vector.z': u'b',
                u'vector.w': u'a'
            }
        },
    }

    def _initAbcMtlDccTranslator(self, *args):
        mtlNodeCls, dccNodeCls, dccNodeString = args[:3]

        self._mtlNodeCls = mtlNodeCls
        self._dccNodeCls = dccNodeCls

        self._dccNodeObj = self._dccNodeCls(dccNodeString)
        self._dccCategoryString = self._dccNodeObj.categoryString()
        self._dccNodeString = self._dccNodeObj.nodepathString()
        self._dccNodeDefObj = self.OBJ_mtl_trs_query_cache.dccNodeDef(self._dccCategoryString)

        self._mtlCategoryString = self._dccNodeDefObj.mtlCategory
        self._mtlNodeDefObj = self._mtlNodeCls.OBJ_grh_query_cache.nodeDef(self._mtlCategoryString)
        self._mtlNodeString = self._getMtlNodeString_(self._dccNodeString)

        self._mtlNodeObj = self._getMtlNode_(self._mtlCategoryString, self._mtlNodeString)

        self._translateDccPorts_()

        self._setMtlPorts_()

    def _getMtlNode_(self, mtlCategoryString, mtlNodeString):
        _nodeCls = self._mtlNodeCls
        return _nodeCls._mtd_cache_(
            _nodeCls.OBJ_grh_obj_cache, mtlNodeString,
            _nodeCls, (mtlCategoryString, mtlNodeString)
        )

    def _getMtlCategoryString(self, dccCategoryString):
        pass

    def _getMtlNodeString_(self, nodepathString):
        return nodepathString.replace(self.DEF_mya_node_separator, self.DEF_mtl_node_pathsep)
    # translate port
    def _translateDccPorts_(self):
        # debug use input
        for i in self._dccNodeDefObj.dccInputs:
            self._translateDccInput_(i)

    def _translateDccInput_(self, dccPortDefObject):
        _dccPortnameString = dccPortDefObject.dccPortname
        _mtlPortnameString = dccPortDefObject.mtlPortname

        if self._dccNodeObj.hasPort(_dccPortnameString):
            _dccPortObject = self._dccNodeObj.port(_dccPortnameString)
            _mtlPortObject = self._mtlNodeObj.port(_mtlPortnameString)

            self._translateDccInputGiven_(_dccPortObject, _mtlPortObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'Dcc Port "{}" is Unregistered'.format(_dccPortnameString)
            )

    def _translateDccInputGiven_(self, dccPortObject, mtlPortObject):
        self._translateDccPortPortdata_(dccPortObject, mtlPortObject)
        if dccPortObject.hasSource():
            self._translateDccConnect_(dccPortObject, mtlPortObject)

    def _translateDccConnect_(self, dccPortObject, mtlPortObject):
        sourceMtlPortObject = self._getSourceMtlPort(dccPortObject)
        if sourceMtlPortObject is not None:
            targetMtlPortObject = mtlPortObject
            if targetMtlPortObject.hasParent():
                self._convertMtlConnect_(targetMtlPortObject, sourceMtlPortObject)
            else:
                sourceMtlPortObject.connectTo(targetMtlPortObject)

    def _getSourceMtlPort(self, dccPortObject):
        _dccPortObject = dccPortObject.source()
        _dccNodeObject = _dccPortObject.node()

        _dccNodeString = _dccNodeObject.nodepathString()
        _dccCategoryString = _dccNodeObject.categoryString()
        if self.OBJ_mtl_trs_query_cache.hasDccCategory(_dccCategoryString):
            _dccObjectDefObject = self.OBJ_mtl_trs_query_cache.dccNodeDef(_dccCategoryString)
            _mtlCategoryString = _dccObjectDefObject.mtlCategory

            _dccPortnameString = _dccPortObject.portpathString()
            if _dccObjectDefObject.hasDccOutput(_dccPortnameString):
                _mtlPortnameString = _dccObjectDefObject.dccOutput(_dccPortnameString).mtlPortname

                _mtlNodeString = self._getMtlNodeString_(_dccNodeString)
                _mtlNodeObject = self._getMtlNode_(_mtlCategoryString, _mtlNodeString)

                return _mtlNodeObject.output(_mtlPortnameString)
            else:
                print _dccPortObject.node().nodepathString(), _dccPortnameString
        else:
            print _dccPortObject.node().nodepathString()

    def _convertMtlConnect_(self, mtlTargetChannelObject, sourceMtlChannelObject):
        mtlTargetParentPortObject = mtlTargetChannelObject.parent()
        mtlParentPorttypeString = mtlTargetParentPortObject.porttypeString()
        if mtlParentPorttypeString in self.VAR_mtl_channel_convert_dict:
            mtlAttributestring = mtlTargetParentPortObject.attrpathString()
            _mtlCategoryString = self.VAR_mtl_channel_convert_dict[mtlParentPorttypeString][u'category']
            _mtlOutputPortnameString = self.VAR_mtl_channel_convert_dict[mtlParentPorttypeString][u'output_portname']
            _connectDict = self.VAR_mtl_channel_convert_dict[mtlParentPorttypeString][u'connect']
            _mtlNodestring = u'{}/{}'.format(mtlAttributestring.replace(self.DEF_mtl_port_pathsep, u'__'), _mtlCategoryString)
            _mtlNodeObject = self._getMtlNode_(_mtlCategoryString, _mtlNodestring)

            _mtlNodeObject.output(_mtlOutputPortnameString).connectTo(mtlTargetParentPortObject)

            mtlTargetChannelPortname = mtlTargetChannelObject.portnameString()

            sourceMtlChannelObject.connectTo(_mtlNodeObject.input(mtlTargetChannelPortname))

    def _translateDccPortPortdata_(self, dccPortObject, mtlPortObject):
        dccPortdata = dccPortObject.portdata()
        if self._dccNodeDefObj.mtlPortdataRaw:
            _keyString = mtlPortObject.portnameString()
            if _keyString in self._dccNodeDefObj.mtlPortdataRaw:
                _dict = self._dccNodeDefObj.mtlPortdataRaw[_keyString]
                if dccPortdata in _dict:
                    dccPortdata = _dict[dccPortdata]
        mtlPortObject.setPortdata(dccPortdata)

    def _convertMtlPortdata_(self):
        pass

    def _setMtlPorts_(self):
        mtlPortRaw = self._dccNodeDefObj.mtlPortRaw
        if mtlPortRaw:
            for k, v in mtlPortRaw.items():
                portdataString = v[self.DEF_mtl_key_portdata]
                self._mtlNodeObj.port(k).setPortdataString(portdataString)


class Abc_MtlTrsNode(
    Abc_MtlTrsBasic,
    mtlObjDef.Def_XmlCacheObj
):
    CLS_mtl_object = None
    CLS_mtl_dcc_object = None

    CLS_mtl_translator = None

    OBJ_mtl_trs_query_cache = None

    OBJ_grh_obj_cache = None
    OBJ_mtl_trs_obj_cache = None

    def _initAbcMtlTrsNode(self, *args):
        dccNodeString = args[0]

        self._translatorObj = self.CLS_mtl_translator(
            self.CLS_mtl_object,
            self.CLS_mtl_dcc_object,
            dccNodeString
        )

        self._initDefMtlCacheObj(self._translatorObj._dccNodeString)

        self._runCreateExpressions_()

    def _runCreateExpressions_(self):
        expressionDict = self._translatorObj._dccNodeDefObj.createExpressionRaw
        self._runExpressions_(expressionDict)

    def _runAfterExpressions_(self):
        expressionDict = self._translatorObj._dccNodeDefObj.afterExpressionRaw
        self._runExpressions_(expressionDict)

    def _runExpressions_(self, expressionDict):
        if expressionDict:
            if self.DEF_mtl_key_command in expressionDict:
                commands = expressionDict[self.DEF_mtl_key_command]
                if commands:
                    cmdsStr = ';'.join(commands)
                    exec cmdsStr

    def _runInsertToTargetExpression_(self, targetDccNodeObjects, targetMtlOutputPortString, mtlInputPortString, mtlOutputPortString):
        for targetDccNode in targetDccNodeObjects:
            targetTrsNodeObject = self.getTrsNode(targetDccNode.nodepathString())
            targetMtlNodeObject = targetTrsNodeObject.mtlNode()
            copyMtlNodeString = u'{}/{}'.format(targetMtlNodeObject.nodepathString(), self.mtlNode().categoryString())
            copyMtlNodeObject = self.getMtlNode(self.mtlNode().categoryString(), copyMtlNodeString)
            [i.setPortdataString(self.mtlNode().input(i.portpathString()).portdataString()) for i in copyMtlNodeObject.inputs()]

            targetMtlNodeObject.output(targetMtlOutputPortString).insertTarget(
                copyMtlNodeObject.input(mtlInputPortString),
                copyMtlNodeObject.output(mtlOutputPortString)
            )

    def _runInsertColorCorrectExpression_(self, portdataDict=None):
        mtlConnections = self.mtlNode().connections()
        mtl_category_0 = 'color_correct'
        node_string_0 = u'{}/{}'.format(self.mtlNode().nodepathString(), mtl_category_0)
        mtlColorCorrectObject = self.getMtlNode(mtl_category_0, node_string_0)
        for mtlSourceObject, mtlTargetObject in mtlConnections:
            if mtlSourceObject.hasParent() is False:
                mtlColorCorrectObject.output().connectTo(mtlTargetObject)
            else:
                _dict = {
                    'r': 'rgba.r',
                    'g': 'rgba.g',
                    'b': 'rgba.b',
                    'a': 'rgba.a'
                }
                _portnameString = _dict[mtlSourceObject.portnameString()]
                mtlColorCorrectObject.output(_portnameString).connectTo(mtlTargetObject)

        self.mtlNode().output().connectTo(mtlColorCorrectObject.input('input'))
        if portdataDict:
            for k, v in portdataDict.items():
                mtlColorCorrectObject.port(k).setPortdata(self.dccNode().port(v).portdata())
        return mtlColorCorrectObject

    def _convertDccMultiTexture_(self, filepathString):
        if self.dccNode().categoryString() == u'file':
            isUdim = True
            if filepathString:
                isSequence = self.dccNode().port('useFrameExtension').portdata()
                uvTilingMode = self.dccNode().port('uvTilingMode').portdata()
                dirnameString = bscMethods.OsFile.dirname(filepathString)
                basenameString = bscMethods.OsFile.basename(filepathString)
                #
                findKeys = self.MOD_re.findall(u'[0-9][0-9][0-9][0-9]', basenameString)
                if findKeys:
                    if u'<udim>' in basenameString.lower():
                        isUdim = False
                    elif not uvTilingMode == 'UDIM (Mari)':
                        isUdim = False
                    #
                    if isUdim:
                        basenameString = basenameString.replace(findKeys[-1], '<udim>')
                    elif isSequence:
                        basenameString = basenameString.replace(findKeys[-1], '<f>')
                    #
                    filepathString = bscMethods.OsPath.composeBy(dirnameString, basenameString)
        return filepathString

    def getMtlNode(self, mtlCategoryString, mtlNodeString):
        return self._mtd_cache_(
            self.OBJ_grh_obj_cache, mtlNodeString,
            self.CLS_mtl_object, (mtlCategoryString, mtlNodeString)
        )

    def getTrsNode(self, dccNodeString):
        return self._mtd_cache_(
            self.OBJ_mtl_trs_obj_cache, dccNodeString,
            self.__class__, (dccNodeString, )
        )

    def dccNodeDef(self):
        return self._translatorObj._dccNodeDefObj

    def dccNode(self):
        return self._translatorObj._dccNodeObj

    def mtlNodeDef(self):
        return self._translatorObj._mtlNodeDefObj

    def mtlNode(self):
        return self._translatorObj._mtlNodeObj

    def __str__(self):
        return self._translatorObj._mtlNodeObj.__str__()


# proxy ************************************************************************************************************** #
class Abc_MtlTrsNodeProxy(Abc_MtlTrsBasic):
    CLS_mtl_node_proxy = None

    CLS_mtl_trs_node = None

    def _initAbcMtlTrsNodeProxy(self, *args):
        dccNodeString = args[0]

        self._trsNodeObject = self.CLS_mtl_trs_node._mtd_cache_(
            self.CLS_mtl_trs_node.OBJ_mtl_trs_obj_cache, dccNodeString,
            self.CLS_mtl_trs_node, (dccNodeString,)
        )

        self._dccNodeObj = self._trsNodeObject.dccNode()
        self._mtlNodeObj = self._trsNodeObject.mtlNode()

        self._mtlNodeProxyObj = self.CLS_mtl_node_proxy(self._mtlNodeObj)

    def dccNode(self):
        return self._dccNodeObj

    def mtlNode(self):
        return self._mtlNodeObj

    def mtlNodeProxy(self):
        return self._mtlNodeProxyObj

    def __str__(self):
        return self._mtlNodeProxyObj.__str__()


class Abc_MtlTrsShaderProxy(Abc_MtlTrsNodeProxy):
    def _initAbcMtlTrsShaderProxy(self, *args):
        self._initAbcMtlTrsNodeProxy(*args)

        self._translateMtlNodes_()

    def _translateMtlNodes_(self):
        dccNodes = self._dccNodeObj.allSourceNodes()
        for i in dccNodes:
            dccCategoryString = i.categoryString()
            dccNodeString = i.nodepathString()
            if self.CLS_mtl_trs_node.OBJ_mtl_trs_query_cache.hasDccCategory(dccCategoryString):
                _trsNodeObject = self.CLS_mtl_trs_node._mtd_cache_(
                    self.CLS_mtl_trs_node.OBJ_mtl_trs_obj_cache, dccNodeString,
                    self.CLS_mtl_trs_node, (dccNodeString,)
                )
            else:
                bscMethods.PyMessage.traceWarning(
                    u'''DCC Category "{}({})"is Unregistered!!!'''.format(dccCategoryString, dccNodeString)
                )


class Abc_MtlTrsMaterialProxy(Abc_MtlTrsNodeProxy):
    CLS_mtl_trs_shader_proxy = None

    VAR_mtl_dcc_shader_portname_list = []

    def _initAbcMtlTrsMaterialProxy(self, *args):
        self._initAbcMtlTrsNodeProxy(*args)

        self._translateMtlShaderProxies_()

    def _translateMtlShaderProxies_(self):
        for dccPortnameString in self.VAR_mtl_dcc_shader_portname_list:
            if isinstance(dccPortnameString, (str, unicode)):
                dccPortObject = self._dccNodeObj.port(dccPortnameString)
                if dccPortObject.hasSource():
                    dccShaderObject = dccPortObject.source().node()
                    dccNodeString = dccShaderObject.nodepathString()
                    _trsNodeProxyObject = self.CLS_mtl_trs_shader_proxy(dccNodeString)
            elif isinstance(dccPortnameString, (tuple, list)):
                dccPortObjects = [self._dccNodeObj.port(i) for i in dccPortnameString]
                if dccPortObjects[0].hasSource():
                    dccPortObject = dccPortObjects[0]

                    dccShaderObject = dccPortObject.source().node()
                    dccNodeString = dccShaderObject.nodepathString()

                    _sourceTrsNodeProxyObject = self.CLS_mtl_trs_shader_proxy(dccNodeString)
                    sourceNodeDefObject = _sourceTrsNodeProxyObject._trsNodeObject.dccNodeDef()
                    sourcePortnameString = sourceNodeDefObject.dccPort(dccPortObject.source().portpathString()).mtlPortname

                    _targetTrsNodeProxyObject = self
                    targetDccNodeDefObject = _targetTrsNodeProxyObject._trsNodeObject.dccNodeDef()
                    targetPortnameString = targetDccNodeDefObject.dccPort(dccPortObject.portpathString()).mtlPortname

                    _sourceTrsNodeProxyObject.mtlNode().port(sourcePortnameString).connectTo(
                        _targetTrsNodeProxyObject.mtlNode().port(targetPortnameString)
                    )
                else:
                    dccPortObject = dccPortObjects[1]
                    if dccPortObject.hasSource():
                        dccShaderObject = dccPortObject.source().node()
                        dccNodeString = dccShaderObject.nodepathString()
                        _trsNodeProxyObject = self.CLS_mtl_trs_shader_proxy(dccNodeString)


class Abc_MtlTrsGeometryProxy(Abc_MtlTrsNodeProxy):
    CLS_mtl_trs_material_proxy = None

    def _initAbcMtlTrsGeometryProxy(self, *args):
        self._initAbcMtlTrsNodeProxy(*args)

        self._getMtlMaterials_()

    def _getMtlMaterials_(self):
        dccMaterials = self._dccNodeObj.materials()

        for i in dccMaterials:
            dccNodeString = i.nodepathString()
            _trsNodeProxyObject = self.CLS_mtl_trs_material_proxy(dccNodeString)
            materialProxyObject = _trsNodeProxyObject.mtlNodeProxy()
            self._mtlNodeProxyObj.connectMaterial(materialProxyObject)


# ******************************************************************************************************************** #
class Abc_MtlTrsLook(Abc_MtlTrsBasic):
    CLS_mtl_look = None
    CLS_mtl_trs_geometry_proxy = None

    def _initAbcMtlTrsLook(self, *args):
        self._mtlLookObj = self.CLS_mtl_look(*args)

    def mtlNode(self):
        return self._mtlLookObj

    def addDccGeometry(self, dccNodeString):

        _trsNodeProxyObject = self.CLS_mtl_trs_geometry_proxy(dccNodeString)

        mtlNodeProxyObject = _trsNodeProxyObject.mtlNodeProxy()
        if self._mtlLookObj.hasGeometry(mtlNodeProxyObject) is False:
            self._mtlLookObj.addGeometry(mtlNodeProxyObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Geometry "{}" is Exist.'''.format(mtlNodeProxyObject.nodepathString())
            )

    def addDccGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addDccGeometry(i) for i in _]

    def _getMtlGeometries_(self):
        pass

    def __str__(self):
        return self._mtlLookObj.__str__()


# ******************************************************************************************************************** #
class Abc_MtlTrsFile(Abc_MtlTrsBasic):
    CLS_mtl_file = None
    CLS_trs_look = None

    OBJ_mtl_trs_obj_cache = None

    def _initAbcMtlTrsFile(self, *args):
        fileString = args[0]
        self._mtlFileObj = self.CLS_mtl_file(fileString)
        self._mtlFileObj.addReference(u'materialx/arnold/nodedefs.mtlx')

    def addLook(self, lookString):
        trsLookObject = self.CLS_trs_look(lookString)
        if self._mtlFileObj.hasLook(lookString) is False:
            mtlLookObject = trsLookObject.mtlNode()
            self._mtlFileObj.addLook(mtlLookObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Look "{}" is Exist.'''.format(lookString)
            )
        return trsLookObject

    def look(self, lookString):
        return self._mtlFileObj.look(lookString)

    def __str__(self):
        for i in self.OBJ_mtl_trs_obj_cache.objects():
            i._runAfterExpressions_()

        return self._mtlFileObj.__str__()

    def save(self):
        self._mtlFileObj.save()

        for i in self.OBJ_mtl_trs_obj_cache.objects():
            i._runAfterExpressions_()

        bscMethods.PyMessage.traceResult(
            u'save file "{}"'.format(self._mtlFileObj.fullpathFilename())
        )
