# coding:utf-8
from LxBasic import bscMethods

from LxData import datObjAbs

from LxGraphic import grhObjAbs

from . import mtlCfg


class Def_DatXmlObj(mtlCfg.Utility):
    VAR_dat_xml_file_attribute_separator = u' '

    VAR_dat_xml_file_element_tag = u''
    VAR_dat_xml_file_attribute_attach_tag = u''

    def _initDefDatXmlObj(self):
        self._xmlPrefixStr = u''

        self._xmlNamePrefixString = None
        self._xmlNameSuffixString = None

    def _xmlElementString_(self):
        return self.VAR_dat_xml_file_element_tag

    def _setXmlNamePrefixString_(self, string):
        self._xmlNamePrefixString = string

    def _xmlNamePrefixString_(self):
        return self._xmlNamePrefixString

    def _setXmlNameSuffixString_(self, string):
        self._xmlNameSuffixString = string

    def _xmlNameSuffixString_(self):
        return self._xmlNameSuffixString

    def _xmlAttributeAttachKeyString_(self):
        return self.VAR_dat_xml_file_attribute_attach_tag

    def _xmlAttributeAttachValueString_(self):
        pass

    @property
    def _xmlPrefixString_(self):
        return self._xmlPrefixStr

    @_xmlPrefixString_.setter
    def _xmlPrefixString_(self, string):
        self._xmlPrefixStr = string

    def _xmlAttributes_(self):
        pass

    def _xmlChildren_(self):
        pass

    def _xmlElements_(self):
        pass

    def _xmlAttributeAttaches_(self):
        """
        :return: list(tuple(key, value)/object instance of Def_DatXmlObj, ...)
        """
        pass

    @classmethod
    def _toXmlString(cls, elementObject, indent=4):
        def addPrefixFnc_(prefixStr_, lStr_, rStr_):
            lis.append(u'{}<{}{}'.format(lStr_, prefixStr_, rStr_))

        def addAttributeFnc_(attributeObject_, lStr_, rStr_):
            if attributeObject_ is not None:
                if isinstance(attributeObject_, Def_DatXmlObj):
                    attributeRaw = attributeObject_._xmlAttributeAttaches_()
                else:
                    attributeRaw = attributeObject_

                if isinstance(attributeRaw, (tuple, list)):
                    if attributeRaw:
                        for i in attributeRaw:
                            if isinstance(i, Def_DatXmlObj):
                                addAttributeFnc_(i, lStr_, rStr_)
                            else:
                                k, v = i
                                if v:
                                    lis.append(u'{}{}="{}"{}'.format(lStr_, k, v, rStr_))

        def addElementFnc_(elementObj_, rStr_, parentElementObj_=None):
            if parentElementObj_ is not None:
                _lString = elementObj_._xmlPrefixString_
            else:
                _lString = u''

            tagString = elementObj_._xmlElementString_()
            addPrefixFnc_(tagString, lStr_=_lString, rStr_=u'')
            # Attribute
            attributes = elementObj_._xmlAttributes_()
            if attributes:
                [addAttributeFnc_(i, lStr_=cls.VAR_dat_xml_file_attribute_separator, rStr_=u'') for i in attributes]
            # Children
            children = elementObj_._xmlChildren_()
            if children:
                lis.append(u'>\r\n')

                for i in children:
                    if i is not None:
                        i._xmlPrefixString_ = _lString + defIndentString
                        addElementFnc_(i, rStr_=rStr_, parentElementObj_=elementObj_)

                lis.append(u'{}</{}>\r\n'.format(_lString, tagString))
            else:
                lis.append(u'{}/>\r\n'.format(cls.VAR_dat_xml_file_attribute_separator))

            elements = elementObj_._xmlElements_()
            if elements:
                for i in elements:
                    i._xmlPrefixString_ = _lString
                    addElementFnc_(i, rStr_=u'', parentElementObj_=elementObj_)

        defIndentString = u' ' * indent
        lis = [
            u'<?xml version="1.0"?>\r\n',
        ]

        addElementFnc_(elementObject, rStr_='')
        return u''.join(lis)

    def __str__(self):
        return self._toXmlString(self)

    def __repr__(self):
        return self._toXmlString(self)


# ******************************************************************************************************************** #
class Abs_MtlObjQueryCache(grhObjAbs.Abs_GrhObjQueryrawCache):
    def _initAbsMtlObjQueryCache(self, *args):
        self._initAbsGrhObjQueryCache(*args)

    # **************************************************************************************************************** #
    def _set_node_queries_build_(self):
        self._nodeRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_node_file
        ) or {}
        self._materialRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_material_file
        ) or {}
        self._geometryRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_geometry_file
        ) or {}
        self._outputRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_output_file
        ) or {}
        self._portChildRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh_port_child_file
        ) or {}

        self._nodeRawDict = {}
        for i in [
            self._nodeRaws, self._materialRaws, self._geometryRaws
        ]:
            self._nodeRawDict.update(i)

    # **************************************************************************************************************** #
    def _get_node_raw_(self, *args):
        categoryString = args[0]

        if categoryString in self._nodeRawDict:
            return self._nodeRawDict[categoryString]

    def _get_node_queryraw_obj_(self, *args):
        categoryString = args[0]

        nodeRaw = self._get_node_raw_(categoryString)
        if nodeRaw:
            return self.CLS_grh_node_queryraw(
                categoryString, nodeRaw,
                self._outputRaws, self._portChildRaws
            )
        else:
            print categoryString

    # **************************************************************************************************************** #
    def _get_category_exist_(self, *args):
        categoryString = args[0]
        return categoryString in self._nodeRawDict

    def _get_categories_(self):
        return self._nodeRawDict.keys()


class Abs_MtlObjCache(grhObjAbs.Abs_GrhObjCache):
    def _initAbsMtlObjCache(self, *args):
        self._initAbsGrhObjCache(*args)


# raw **************************************************************************************************************** #
class Abs_MtlRaw(
    Def_DatXmlObj,
    datObjAbs.Abs_DatRaw
):
    def _initAbsMtlRaw(self, *args):
        self._initAbsDatRaw(*args)

        self._initDefDatXmlObj()

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


class Abs_MtlPortname(
    Def_DatXmlObj,
    datObjAbs.Abs_DatPortname,
):
    def _initAbsMtlPortname(self, *args):
        self._initAbsDatPortname(*args)

        self._initDefDatXmlObj()


class Abs_MtlNodename(
    Def_DatXmlObj,
    datObjAbs.Abs_DatNodename,
):
    def _initAbsMtlNodename(self, *args):
        self._initAbsDatNodename(*args)

        self._initDefDatXmlObj()

    # **************************************************************************************************************** #
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


class Abs_MtlPath(
    Def_DatXmlObj,
    datObjAbs.Abs_DatPath
):
    def _initAbsMtlPath(self, *args):
        self._initAbsDatPath(*args)

        self._initDefDatXmlObj()

    # **************************************************************************************************************** #
    def _xmlAttributes_(self):
        return [
            [('raw', self.pathString())]
        ]

    def _xmlAttributeAttachValueString_(self):
        if self._xmlNamePrefixString_() is not None:
            return u'{}{}'.format(self._xmlNamePrefixString_(), self.pathString())
        return self.pathString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abs_MtlAttrpath(
    Def_DatXmlObj,
    datObjAbs.Abs_DatAttrpath
):
    def _initAbsMtlAttrpath(self, *args):
        self._initAbsDatAttrpath(*args)

        self._initDefDatXmlObj()


# object set ********************************************************************************************************* #
class Abs_MtlObjSet(
    Def_DatXmlObj,
    grhObjAbs.Abs_GrhObjSet
):
    def _initAbsMtlObjSet(self, *args):
        self._initAbsGrhObjSet(*args)

        self._initDefDatXmlObj()

    # **************************************************************************************************************** #
    def _xmlAttributeAttachValueString_(self):
        return self.toString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


# value ************************************************************************************************************** #
class Abs_MtlValue(
    Def_DatXmlObj,
    datObjAbs.Abs_DatValue
):

    def _initAbsMtlValue(self, *args):
        self._initAbsDatValue(*args)

        self._initDefDatXmlObj()

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
    Def_DatXmlObj,
    grhObjAbs.Abs_GrhPort
):
    def _initAbsMtlPort(self, *args):
        self._initAbsGrhPort(*args)

        self._initDefDatXmlObj()

        self._proxyObj = None

    # xml ************************************************************************************************************ #
    def _xmlAttributeAttachValueString_(self):
        return self.portpathString()

    def _xmlAttributeAttaches_(self):
        if self.isChannel() is True:
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
    Def_DatXmlObj,
    grhObjAbs.Abs_GrhNode
):
    def _initAbsMtlNode(self, *args):
        self._initAbsGrhNode(*args)

        self._initDefDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xmlElementString_(self):
        return self.categoryString()

    def _xmlAttributes_(self):
        return [
            self.nodepath(),
            self.type()
        ]

    def _xmlChildren_(self):
        return self.changedInparm()

    def _xmlAttributeAttachValueString_(self):
        return self.nodepathString()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abs_MtlConnector(
    grhObjAbs.Abs_GrhConnector
):
    def _initAbsMtlConnector(self, *args):
        self._initAbsGrhConnector(*args)


# port proxy ********************************************************************************************************* #
class Abs_MtlPortProxy(
    Def_DatXmlObj,
    grhObjAbs.Abs_GrhPortProxy,
):
    CLS_grh_name = None

    def _initAbsMtlPortProxy(self, *args):
        self._initAbsGrhPortProxy(*args)

        self._initDefDatXmlObj()

    def _xmlAttributes_(self):
        return [
            self._portObj.portpath(),
            self._portObj.porttype(),
            self._portObj.value()
        ]


class Abc_MtlInputProxy(Abs_MtlPortProxy):
    def _initAbcMtlInputProxy(self, *args):
        self._initAbsMtlPortProxy(*args)

        self._nodeGraphOutputObj = None

    def portgiven(self):
        if self._portObj.hasSource() is True:
            return self.nodeGraphOutput()
        return self._portObj.value()

    def _xmlAttributes_(self):
        return [
            self._portObj.portpath(),
            self._portObj.porttype(),
            self.portgiven()
        ]


class Abs_MtlNodeProxy(
    Def_DatXmlObj,
    grhObjAbs.Abs_GrhNodeProxy
):
    def _initAbsMtlNodeProxy(self, *args):
        self._initAbsGrhNodeProxy(*args)

        self._initDefDatXmlObj()


class Abc_MtlShaderProxy(Abs_MtlNodeProxy):
    def _initAbcMtlShaderProxy(self, *args):
        self._initAbsMtlNodeProxy(*args)

    def _get_material_context_(self):
        for otparmObject in self._nodeObj.otparms():
            if otparmObject.hasTargets():
                targetPortObjects = otparmObject.targets()
                for targetPortObject in targetPortObjects:
                    proxyNodeObject = targetPortObject.node().proxy()
                    if isinstance(proxyNodeObject, Abc_MtlMaterialProxy):
                        return targetPortObject.portnameString()

    def _get_material_node_proxy_(self):
        for otparmObject in self._nodeObj.otparms():
            if otparmObject.hasTargets():
                targetPortObjects = otparmObject.targets()
                for targetPortObject in targetPortObjects:
                    proxyNodeObject = targetPortObject.node().proxy()
                    if isinstance(proxyNodeObject, Abc_MtlMaterialProxy):
                        return proxyNodeObject

    # **************************************************************************************************************** #
    def _xmlAttributes_(self):
        return [
            self._nodeObj.nodepath(),
            self._nodeObj.category(),
            [(u'context', self._get_material_context_())]
        ]

    def _xmlChildren_(self):
        return self._get_changed_bind_inputs_()


class Abc_MtlMaterialProxy(Abs_MtlNodeProxy):
    def _initAbcMtlMaterialProxy(self, *args):
        self._initAbsMtlNodeProxy(*args)

    # **************************************************************************************************************** #
    def surfaceInput(self):
        return self._nodeObj.port(u'surfaceshader')

    def connectSurfaceFrom(self, portObject):
        portObject.connectTo(self.surfaceInput())

    def surfaceShader(self):
        if self.surfaceInput().hasSource():
            return self.surfaceInput().source().node().proxy()

    # **************************************************************************************************************** #
    def displacementInput(self):
        return self._nodeObj.port(u'displacementshader')

    def connectDisplacementFrom(self, portObject):
        portObject.connectTo(self.displacementInput())

    def displacementShader(self):
        if self.displacementInput().hasSource():
            return self.displacementInput().source().node().proxy()

    # **************************************************************************************************************** #
    def volumeInput(self):
        return self._nodeObj.port(u'volumeshader')

    def connectVolumeFrom(self, portObject):
        portObject.connectTo(self.volumeInput())

    def volumeShader(self):
        if self.volumeInput().hasSource():
            return self.volumeInput().source().node().proxy()

    # **************************************************************************************************************** #
    def shaders(self):
        return bscMethods.List.cleanupTo(
            [self.surfaceShader(), self.displacementShader(), self.volumeShader()]
        )

    # xml ************************************************************************************************************ #
    def _xmlAttributes_(self):
        return [
            self.name()
        ]

    def _xmlChildren_(self):
        # update shader's node graph first
        for nodeProxyObject in self.shaders():
            nodeGraphObject = nodeProxyObject.nodeGraph(nodeProxyObject)
            materialNodeProxyObject = nodeProxyObject._get_material_node_proxy_()
            if materialNodeProxyObject is not None:
                nodeGraphObject.name()._setXmlNamePrefixString_(
                    u'{}/'.format(
                        materialNodeProxyObject.name()._xmlAttributeAttachValueString_()
                    )
                )
            nodeGraphObject._set_node_graph_update_()
        return self.shaders()

    def _xmlElements_(self):
        lis = []
        for nodeProxyObject in self.shaders():
            nodeGraphObjects = nodeProxyObject.nodeGraphs()
            if nodeGraphObjects:
                for nodeGraphObject in nodeGraphObjects:
                    if nodeGraphObject.hasNodes():
                        if not nodeGraphObject in lis:
                            lis.append(nodeGraphObject)
        return lis

    def _xmlAttributeAttachValueString_(self):
        return self.name()._xmlAttributeAttachValueString_()

    def _xmlAttributeAttaches_(self):
        return [
            (self._xmlAttributeAttachKeyString_(), self._xmlAttributeAttachValueString_())
        ]


class Abc_MtlGeometryProxy(Abs_MtlNodeProxy):
    CLS_mtl_property = None
    CLS_mtl_visibility_assign = None

    CLS_mtl_propertyset = None

    def _initAbcMtlGeometryProxy(self, *args):
        self._initAbsMtlNodeProxy(*args)

        self._propertysetObj = self.CLS_mtl_propertyset(self.nameString())

    def _updatePropertyset_(self):
        self._propertysetObj._initializeSets_()

        for i in self.changedProperties():
            self._propertysetObj.addPort(i)

    # **************************************************************************************************************** #
    def property(self, *args):
        return self.bindParam(*args)

    def hasProperty(self, *args):
        return self.hasBindParam(*args)

    def properties(self):
        return [
            i
            for i in self.bindParams()
            if i.port().typeString() == self.DEF_grh_keyword_property
        ]

    def changedProperties(self):
        lis = []
        for i in self.properties():
            portObject = i.port()
            if portObject.isChanged():
                lis.append(i)
        return lis

    # **************************************************************************************************************** #
    def visibility(self, *args):
        return self.bindParam(*args)

    def hasVisibility(self, *args):
        return self.hasBindParam(*args)

    def visibilities(self):
        return [
            i
            for i in self.bindParams()
            if i.port().typeString() == self.DEF_grh_keyword_visibility
        ]

    def changedVisibilities(self):
        lis = []
        for i in self.visibilities():
            portObject = i.port()
            if portObject.isChanged():
                lis.append(i)
        return lis

    # **************************************************************************************************************** #
    def connectMaterial(self, materialProxyObject):
        materialProxyObject.node().otparm(u'material').connectTo(self.node().inparm(u'material'))

    def material(self):
        if self.node().inparm(u'material').hasSource():
            nodeObject = self.node().inparm(u'material').source().node()
            return nodeObject.proxy()

    def setPropertyset(self, propertysetObject):
        self._propertysetObj = propertysetObject

    def propertyset(self):
        return self._propertysetObj

    # **************************************************************************************************************** #
    def _xmlAttributes_(self):
        return [
            self._nodeObj.nodepath(),
            self._nodeObj.category()
        ]

    def _xmlChildren_(self):
        return self.changedProperties() + self.changedVisibilities()


# node graph ********************************************************************************************************* #
class Abc_MtlNodeGraph(
    Def_DatXmlObj,
    grhObjAbs.Abs_GrhNodeGraph
):

    def _initAbcMtlNodeGraph(self, *args):
        self._initAbsGrhNodeGraph(*args)

    # **************************************************************************************************************** #
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


class Abc_MtlNodeGraphOutput(
    Def_DatXmlObj,
    grhObjAbs.Abs_GrhNodeGraphOutput
):
    def _initAbcMtlNodeGraphOutput(self, *args):
        self._initAbsGrhNodeGraphOutput(*args)

        self._initDefDatXmlObj()

    # xml ************************************************************************************************************ #
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


# portset ************************************************************************************************************ #
class Abc_MtlPortset(Def_DatXmlObj):
    CLS_mtl_name = None

    CLS_grh_port_set = None
    
    def _initAbcMtlPortset(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._portSetObj = self.CLS_grh_port_set()

        self._initDefDatXmlObj()

    def _initializeSets_(self):
        self._portSetObj._set_obj_set_data_int_()

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


# geometry collection
class Abc_MtlCollection(Def_DatXmlObj):
    CLS_mtl_name = None

    CLS_mtl_geometry_set = None
    CLS_mtl_collection_set = None

    DEF_geometry_separator = None

    def _initAbcMtlCollection(self, *args):
        self._nameObj = self.CLS_mtl_name(*args)

        self._geometrySetObj = self.CLS_mtl_geometry_set()
        self._collectionSetObj = self.CLS_mtl_collection_set()
        self._excludeGeometrySetObj = self.CLS_mtl_geometry_set()

        self._initDefDatXmlObj()

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
class Abc_MtlAssign(Def_DatXmlObj):
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

        self._initDefDatXmlObj()

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

    def typeString(self):
        return self._vistypeObj.toString()

    def visible(self):
        return self._visibilityValueObj

    def assignVisibility(self, portObj):
        visibilityString = portObj.portpathString()

        self._vistypeObj = self.CLS_grh_type(visibilityString)

        self._visibilityValueObj = portObj.value()

    def addViewerGeometry(self, geometryObject):
        self._viewerGeometrySetObj.addObject(geometryObject)

    def viewerGeometries(self):
        return self._viewerGeometrySetObj.objsets()

    # xml ************************************************************************************************************ #
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
class Abc_MtlLook(Def_DatXmlObj):
    CLS_mtl_name = None

    CLS_mtl_assign_set = None

    CLS_mtl_material_assign = None
    CLS_mtl_material_assign_set = None

    CLS_mtl_propertyset_assign = None
    CLS_mtl_propertyset_assign_set = None

    CLS_mtl_visibility_assign = None
    CLS_mtl_visibility_assign_set = None

    CLS_mtl_geometry_set = None

    def _initAbcMtlLook(self, *args):
        nameString = args[0]
        self._nameObj = self.CLS_mtl_name(nameString)

        self._visibilitySetObj = self.CLS_mtl_visibility_assign_set(nameString)
        self._materialAssignSetObj = self.CLS_mtl_material_assign_set(nameString)
        self._propertysetAssignSetObj = self.CLS_mtl_propertyset_assign_set(nameString)

        self._assignSetObj = self.CLS_mtl_assign_set(nameString)
        self._geometrySetObj = self.CLS_mtl_geometry_set(nameString)

        self._initDefDatXmlObj()

    def _addGeometryProxy_(self, *args):
        geometryProxyObject = args[0]
        self._geometrySetObj.addObject(geometryProxyObject)

    def _updateAssigns_(self):
        for i in self._geometrySetObj.objects():
            self._addGeometryMaterialAssigns_(i)
            self._addGeometryPropertyAssigns_(i)
            self._addGeometryVisibilities_(i)

    def _addGeometryMaterialAssigns_(self, geometryProxyObject):
        def addFnc_(geometryProxyObject_, materialProxyObject_):
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

            if _materialAssignObject.hasGeometry(geometryProxyObject_) is False:
                _materialAssignObject.addGeometry(geometryProxyObject_)

        materialProxyObject = geometryProxyObject.material()
        if materialProxyObject is not None:
            addFnc_(geometryProxyObject, materialProxyObject)

    def _addGeometryPropertyAssigns_(self, geometryProxyObject):
        def addFnc_(geometryProxyObject_, propertysetObject_):
            propertysetObject_.name()._setXmlNamePrefixString_(
                u'{}'.format(self.nameString())
            )
            _count = self._propertysetAssignSetObj.objectCount()
            _keyString = geometryProxyObject_.node().nodepathString()
            if self._propertysetAssignSetObj._get_obj_exist_(_keyString):
                _propertysetAssignObject = self._propertysetAssignSetObj._get_obj_(_keyString)
            else:
                _propertysetAssignObject = self.CLS_mtl_propertyset_assign(
                    propertysetObject_.name()._xmlAttributeAttachValueString_()
                )
                self._propertysetAssignSetObj._set_obj_add_(_keyString, _propertysetAssignObject)

            _propertysetAssignObject.setPropertyset(propertysetObject_)
            if _propertysetAssignObject.hasGeometry(geometryProxyObject_) is False:
                _propertysetAssignObject.addGeometry(geometryProxyObject_)

        geometryProxyObject._updatePropertyset_()
        propertysetObject = geometryProxyObject.propertyset()
        if propertysetObject.hasPorts():
            addFnc_(geometryProxyObject, propertysetObject)

    def _addGeometryVisibilities_(self, geometryProxyObject):
        def addFnc_(geometryProxyObject_, portProxyObject_):
            _portObject = portProxyObject_.port()
            _count = self._visibilitySetObj.objectCount()
            _keyString = _portObject.portpathString()
            if self._visibilitySetObj._get_obj_exist_(_keyString):
                _visibilityObject = self._visibilitySetObj._get_obj_(_keyString)
            else:
                _visibilityObject = self.CLS_mtl_visibility_assign(
                    'visibility_{}'.format(_count)
                )
                _visibilityObject.assignVisibility(_portObject)
                self._visibilitySetObj._set_obj_add_(_keyString, _visibilityObject)

            if _visibilityObject.hasGeometry(geometryProxyObject_) is False:
                _visibilityObject.addGeometry(geometryProxyObject_)

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

    def _xmlAttributes_(self):
        return [
            self._nameObj
        ]

    def _xmlChildren_(self):
        self._updateAssigns_()
        return self.assigns()

    def _xmlElements_(self):
        return self._xmlElementAttaches_()


class Abc_MtlFile(Def_DatXmlObj):
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

        self._initDefDatXmlObj()

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

    # xml ************************************************************************************************************ #
    def _xmlAttributes_(self):
        return [
            self._filepathObj
        ]


# proxy ************************************************************************************************************** #
class Abc_MtlTrsNodeProxy(grhObjAbs.Abs_GrhTrsNodeProxy):
    def _initAbcMtlTrsNodeProxy(self, *args):
        self._initAbsGrhTrsNodeProxy(*args)


class Abc_MtlTrsShaderProxy(Abc_MtlTrsNodeProxy):
    def _initAbcMtlTrsShaderProxy(self, *args):
        self._initAbcMtlTrsNodeProxy(*args)

        self._set_nodes_trs_()

    def _set_nodes_trs_(self):
        srcNodes = self._srcNodeObj.allSourceNodes()
        for srcNode in srcNodes:
            srcCategoryString = srcNode.categoryString()
            srcNodeString = srcNode.nodepathString()
            if self.CLS_grh_trs_node.CLS_grh_trs_node_query.OBJ_grh_trs_queryraw_cache.hasSrcCategory(srcCategoryString):
                _trsNodeObject = self.CLS_grh_trs_node._mtd_get_cache_obj_(
                    self.CLS_grh_trs_node.OBJ_grh_trs_obj_cache, srcNodeString,
                    self.CLS_grh_trs_node, (srcNodeString,)
                )
            else:
                bscMethods.PyMessage.traceWarning(
                    u'''Source Category: "{}"; Node: "{}" is Unregistered.'''.format(
                        srcCategoryString,
                        srcNodeString,
                    )
                )


class Abc_MtlTrsMaterialProxy(Abc_MtlTrsNodeProxy):
    CLS_grh_trs_shader_proxy = None

    VAR_grh_trs_src_shader_portpath_list = []

    def _initAbcMtlTrsMaterialProxy(self, *args):
        self._initAbcMtlTrsNodeProxy(*args)

        self._set_shaders_trs_()

    def _set_shaders_trs_(self):
        for srcPortpathString in self.VAR_grh_trs_src_shader_portpath_list:
            if isinstance(srcPortpathString, (str, unicode)):
                srcPortObject = self._srcNodeObj.port(srcPortpathString)
                if srcPortObject.hasSource():
                    srcShaderObject = srcPortObject.source().node()
                    srcShaderNodeString = srcShaderObject.nodepathString()

                    _trsNodeProxyObject = self.CLS_grh_trs_shader_proxy(
                        srcShaderNodeString
                    )
            elif isinstance(srcPortpathString, (tuple, list)):
                dccPortObjects = [self._srcNodeObj.port(i) for i in srcPortpathString]
                if dccPortObjects[0].hasSource():
                    srcPortObject = dccPortObjects[0]

                    srcShaderObject = srcPortObject.source().node()
                    srcShaderNodeString = srcShaderObject.nodepathString()

                    _scrTrsNodeProxyObject = self.CLS_grh_trs_shader_proxy(srcShaderNodeString)
                    _scrTrsNodeQueryObject = _scrTrsNodeProxyObject._trsNodeObject.trsNodeQuery()
                    sourcePortnameString = _scrTrsNodeQueryObject.trsPortQuery(srcPortObject.source().portpathString()).target_portpath

                    _targetTrsNodeProxyObject = self
                    targetDccNodeDefObject = _targetTrsNodeProxyObject._trsNodeObject.trsNodeQuery()
                    targetPortnameString = targetDccNodeDefObject.trsPortQuery(srcPortObject.portpathString()).target_portpath

                    _scrTrsNodeProxyObject.tgtNode().port(sourcePortnameString).connectTo(
                        _targetTrsNodeProxyObject.tgtNode().port(targetPortnameString)
                    )
                else:
                    srcPortObject = dccPortObjects[1]
                    if srcPortObject.hasSource():
                        srcShaderObject = srcPortObject.source().node()
                        srcShaderNodeString = srcShaderObject.nodepathString()

                        _trsNodeProxyObject = self.CLS_grh_trs_shader_proxy(
                            srcShaderNodeString
                        )


class Abc_MtlTrsGeometryProxy(Abc_MtlTrsNodeProxy):
    CLS_grh_trs_material_proxy = None

    def _initAbcMtlTrsGeometryProxy(self, *args):
        self._initAbcMtlTrsNodeProxy(*args)

        self._set_material_trs_()

    def _set_material_trs_(self):
        dccMaterials = self._srcNodeObj.materials()

        for i in dccMaterials:
            srcMaterialNodeString = i.nodepathString()
            _trsNodeProxyObject = self.CLS_grh_trs_material_proxy(srcMaterialNodeString)
            materialProxyObject = _trsNodeProxyObject.tgtNodeProxy()
            self._tgtNodeProxyObj.connectMaterial(materialProxyObject)


# ******************************************************************************************************************** #
class Abc_MtlTrsLook(mtlCfg.Utility):
    CLS_mtl_look = None
    CLS_mtl_trs_geometry_proxy = None

    def _initAbcMtlTrsLook(self, *args):
        self._mtlLookObj = self.CLS_mtl_look(*args)

    def tgtNode(self):
        return self._mtlLookObj

    def addDccGeometry(self, srcNodeString):

        _trsNodeProxyObject = self.CLS_mtl_trs_geometry_proxy(srcNodeString)

        mtlNodeProxyObject = _trsNodeProxyObject.tgtNodeProxy()
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
class Abc_MtlTrsFile(mtlCfg.Utility):
    CLS_mtl_file = None
    CLS_trs_look = None

    OBJ_grh_trs_obj_cache = None

    def _initAbcMtlTrsFile(self, *args):
        fileString = args[0]
        self._mtlFileObj = self.CLS_mtl_file(fileString)
        self._mtlFileObj.addReference(u'materialx/arnold/nodedefs.mtlx')

    def addLook(self, lookString):
        trsLookObject = self.CLS_trs_look(lookString)
        if self._mtlFileObj.hasLook(lookString) is False:
            mtlLookObject = trsLookObject.tgtNode()
            self._mtlFileObj.addLook(mtlLookObject)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Look "{}" is Exist.'''.format(lookString)
            )
        return trsLookObject

    def look(self, lookString):
        return self._mtlFileObj.look(lookString)

    def __str__(self):
        for i in self.OBJ_grh_trs_obj_cache.objects():
            i._set_after_expressions_run_()

        return self._mtlFileObj.__str__()

    def save(self):
        self._mtlFileObj.save()

        for i in self.OBJ_grh_trs_obj_cache.objects():
            i._set_after_expressions_run_()

        bscMethods.PyMessage.traceResult(
            u'save file "{}"'.format(self._mtlFileObj.fullpathFilename())
        )
