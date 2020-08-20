# coding:utf-8
from LxBasic import bscMethods

from LxData import datObjAbs

from LxGraphic import grhObjAbs

from . import mtxCfg


class AbsMtxBasic(mtxCfg.MtxUtility):
    pass


# ******************************************************************************************************************** #
class AbsMtxObjLoader(grhObjAbs.AbsGrhObjLoader):
    def _initAbsMtxObjLoader(self, *args):
        self._initAbsGrhObjLoader(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__set_node_raw_create_(cls, *args):
        (
            nodeRawDict,
            typepathStr,
            orig_node_raw_dict,
            orig_otport_raw_list_dict,
            orig_child_port_raw_list_dict
        ) = args

        _datatypeStr = orig_node_raw_dict[cls.DEF_grh__key_node_datatype]
        # property
        nodeRawDict[cls.DEF_grh__key_node_typepath] = typepathStr
        nodeRawDict[cls.DEF_grh__key_node_datatype] = _datatypeStr
        # port
        _portRawList = []

        _orig_port_raw_list = orig_node_raw_dict[cls.DEF_grh__key_port]
        cls._obj_loader_cls__set_ports_create_(_portRawList, _orig_port_raw_list, orig_child_port_raw_list_dict)

        _orig_otport_raw_list = orig_otport_raw_list_dict.get(_datatypeStr, [])
        cls._obj_loader_cls__set_ports_create_(_portRawList, _orig_otport_raw_list, orig_child_port_raw_list_dict)

        nodeRawDict[cls.DEF_grh__key_port] = _portRawList

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__set_ports_create_(cls, *args):
        portRawList, orig_port_raw_list, orig_child_port_raw_list_dict = args
        for orig_port_raw in orig_port_raw_list:
            cls._obj_loader_cls__set_port_create_(portRawList, orig_port_raw, orig_child_port_raw_list_dict)

    @classmethod
    def _obj_loader_cls__set_port_create_(cls, *args):
        portRawList, orig_port_raw, orig_child_port_raw_list_dict = args
        _portpathStr = orig_port_raw[cls.DEF_grh__key_portpath]
        if cls.DEF_grh__key_porttype in orig_port_raw:
            _porttypeStr = orig_port_raw[cls.DEF_grh__key_porttype]
        else:
            _porttypeStr = None
        _datatypeStr = orig_port_raw[cls.DEF_grh__key_port_datatype]
        _portrawStr = orig_port_raw[cls.DEF_grh__key_portraw]
        _assignStr = orig_port_raw[cls.DEF_grh__key_assign]

        _childStrList = []
        # add parent first
        cls._obj_loader_cls__set_port_raw_add_(
            portRawList,
            portpath=_portpathStr,
            porttype=_porttypeStr,
            datatype=_datatypeStr,
            portraw=_portrawStr,
            assign=_assignStr,
            children=_childStrList
        )

        orig_child_port_raw_list = orig_child_port_raw_list_dict.get(_datatypeStr, [])

        cls._obj_loader_cls__set_port_children_create_(
            portRawList, _childStrList, orig_port_raw, orig_child_port_raw_list
        )

    @classmethod
    def _obj_loader_cls__set_port_children_create_(cls, *args):
        portRawList, childStrList, orig_parent_port_raw, orig_child_port_raw_list = args

        for _index, _orig_child_port_raw in enumerate(orig_child_port_raw_list):
            cls._obj_loader_cls__set_port_child_create_(
                portRawList, childStrList, orig_parent_port_raw, _orig_child_port_raw,
                _index
            )

    @classmethod
    def _obj_loader_cls__set_port_child_create_(cls, *args):
        portRawList, childStrList, origParentPortRaw, origPortRaw, childIndex = args

        _parentPortpathStr = origParentPortRaw[cls.DEF_grh__key_portpath]
        _parentPorttypeStr = origParentPortRaw[cls.DEF_grh__key_port_datatype]
        parentPortrawString = origParentPortRaw[cls.DEF_grh__key_portraw]
        parentAssignString = origParentPortRaw[cls.DEF_grh__key_assign]

        _formatString = origPortRaw[cls.DEF_grh__key_format]

        _portpathStr = _formatString.format(
            **{
                cls.DEF_grh__key_portpath: _parentPortpathStr
            }
        )
        _datatypeStr = origPortRaw[cls.DEF_grh__key_port_datatype]

        if parentPortrawString:
            _portrawStr = parentPortrawString.split(u',')[childIndex].rstrip().lstrip()
        else:
            _portrawStr = origPortRaw[cls.DEF_grh__key_portraw]

        if parentAssignString == cls.DEF_grh__keyword__gnport:
            _portAssignString = cls.DEF_grh__keyword__gnport_channel
        if parentAssignString == cls.DEF_grh__keyword__inport:
            _portAssignString = cls.DEF_grh__keyword__inport_channel
        elif parentAssignString == cls.DEF_grh__keyword__otport:
            _portAssignString = cls.DEF_grh__keyword__otport_channel
        else:
            raise TypeError()

        cls._obj_loader_cls__set_port_raw_add_(
            portRawList,
            portpath=_portpathStr,
            porttype=_parentPorttypeStr,
            datatype=_parentPorttypeStr,
            portraw=_portrawStr,
            assign=_portAssignString,
            parent=_parentPortpathStr,
            children=[]
        )
        childStrList.append(_portpathStr)

    # **************************************************************************************************************** #
    @classmethod
    def _grh__obj_loader_cls__get_definition_node_raw_(cls, *args):
        out_node_raw_dict = cls.CLS_ordered_dict()
        cls._obj_loader_cls__set_node_raw_create_(
            out_node_raw_dict,
            *args
        )
        return out_node_raw_dict


# ******************************************************************************************************************** #
class AbsMtxObjQueryBuilder(grhObjAbs.AbsGrhObjQueryrawCreator):
    def _initAbsMtxObjQueryBuilder(self, *args):
        self._initAbsGrhObjQueryBuilder(*args)

    # **************************************************************************************************************** #
    def _queryraw_loader__set_build_(self):
        self._nodeRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__node_file
        ) or {}
        self._materialRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__material_file
        ) or {}
        self._geometryRaws = bscMethods.OsJsonFile.read(
            self.VAR_grh__geometry_file
        ) or {}
        self._origOtportRaw = bscMethods.OsJsonFile.read(
            self.VAR_grh__output_file
        ) or {}
        self._origPortChildRaw = bscMethods.OsJsonFile.read(
            self.VAR_grh__port_child_file
        ) or {}

        self._origNodeRaws = self.CLS_ordered_dict()
        for i in [
            self._nodeRaws, self._materialRaws, self._geometryRaws
        ]:
            self._origNodeRaws.update(i)

    # **************************************************************************************************************** #
    def _queryraw_loader__get_node_raw_(self, *args):
        typepathStr = args[0]

        if typepathStr in self._origNodeRaws:
            origNodeRaw = self._origNodeRaws[typepathStr]
            return self.CLS_grh__obj_query_creator__obj_loader.getDefinitionNodeRaw(
                typepathStr, origNodeRaw, self._origOtportRaw, self._origPortChildRaw
            )

    # **************************************************************************************************************** #
    def _queryraw_loader__get_category_exist_(self, *args):
        typepathStr = args[0]
        return typepathStr in self._origNodeRaws

    def _queryraw_loader__get_categories_(self):
        return self._origNodeRaws.keys()


# ******************************************************************************************************************** #
class AbsMtxObjQueue(grhObjAbs.AbsGrhObjQueue):
    def _initAbsMtxObjQueue(self, *args):
        self._initAbsGrhObjQueue(*args)


# raw **************************************************************************************************************** #
class AbsMtxRaw(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatRaw
):
    def _initAbsMtxRaw(self, *args):
        self._initAbsDatRaw(*args)

        self._initAbsDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_list_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxDatatype(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatDatatype
):
    def _initAbsMtxDatatype(self, *args):
        self._initAbsDatDatatype(*args)

        self._initAbsDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_list_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxObjProxyNamespace(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatObjNamespace
):
    def _initAbsMtxObjProxyNamespace(self, *args):
        self._initAbsDatObjNamespace(*args)

        self._initAbsDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_list_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxName(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatName
):
    def _initAbsMtxName(self, *args):
        self._initAbsDatName(*args)

        self._initAbsDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_list_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxObjTypename(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatObjName,
):
    def _initAbsMtxObjTypename(self, *args):
        self._initAbsDatObjName(*args)

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_list_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxObjName(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatObjName,
):
    def _initAbsMtxObjName(self, *args):
        self._initAbsDatObjName(*args)

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_list_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxPath(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatObjPath
):
    def _initAbsMtxPath(self, *args):
        self._initAbsDatObjPath(*args)

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_list_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxAttrpath(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatObjComppath
):
    def _initAbsMtxAttrpath(self, *args):
        self._initAbsDatObjComppath(*args)

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_list_(self):
        return [
            [('raw', self.raw())]
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


# object set ********************************************************************************************************* #
class AbsMtxObjSet(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhObjStack
):
    def _initAbsMtxObjSet(self, *args):
        self._initAbsGrhObjStack(*args)

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


# value ************************************************************************************************************** #
class AbsMtxValue(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    datObjAbs.AbsDatValue
):

    def _initAbsMtxValue(self, *args):
        self._initAbsDatValue(*args)

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_list_(self):
        return [
            self.datatype(), self.data()
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.toString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


# ******************************************************************************************************************** #
class AbsMtxPort(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhPort
):
    def _initAbsMtxPort(self, *args, **kwargs):
        self._initAbsGrhPort(*args, **kwargs)

        self._initAbsDatXmlObj()

        self._proxyObj = None

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.portpathString()

    def _xml_obj__get_attribute_attach_list_(self):
        if self.isChannel() is True:
            # <... nodename="nodepath" member="parent portpath" channel="portname" />
            return [
                self.parent(),
                (self._xml_obj__get_attribute_attach_key_str_(), self.portnameString())
            ]
        else:
            # <... nodename = "nodepath" member = "portpath" />
            return [
                self.node(),
                (self._xml_obj__get_attribute_attach_key_str_(), self.portpathString())
            ]

    def _xml_obj__get_attribute_list_(self):
        return [
            self.portpath(),
            self.datatype(),
            self.portgiven()
        ]


class AbsMtxNode(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhNode
):
    def _initAbsMtxNode(self, *args, **kwargs):
        self._initAbsGrhNode(*args, **kwargs)

        self._initAbsDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xml_obj__get_element_prefix_str(self):
        return self.typepathString()

    def _xml_obj__get_attribute_list_(self):
        return [
            self.path(),
            self.datatype()
        ]

    def _xml_obj__get_child_element_list_(self):
        return self.changedInport()

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.pathString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxConnector(
    grhObjAbs.AbsGrhConnector
):
    def _initAbsMtxConnector(self, *args):
        self._initAbsGrhConnector(*args)


# port proxy ********************************************************************************************************* #
class AbsMtxPortProxy(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhPortProxy,
):
    def _initAbsMtxPortProxy(self, *args, **kwargs):
        self._initAbsGrhPortProxy(*args, **kwargs)

        self._initAbsDatXmlObj()

    def _xml_obj__get_attribute_list_(self):
        return [
            self.bindObject().portpath(),
            self.bindObject().datatype(),
            self.bindPortgiven()
        ]


class AbsMtxShaderProxy(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhShaderProxy
):
    def _initAbsMtxShaderProxy(self, *args, **kwargs):
        self._initAbsGrhShaderProxy(*args, **kwargs)

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_list_(self):
        return [
            self.path(),
            self.bindObject().typepath(),
            [(u'context', self._shader_proxy__get_material_context_())]
        ]

    def _xml_obj__get_child_element_list_(self):
        return self.changedBindInportProxies()


class AbsMtxMaterialProxy(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhMaterialProxy
):
    def _initAbsMtxMaterialProxy(self, *args, **kwargs):
        self._initAbsGrhMaterialProxy(*args, **kwargs)

        self._initAbsDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_list_(self):
        return [
            self.path()
        ]

    def _xml_obj__get_child_element_list_(self):
        # update shader's node graph first
        for shaderProxyObj in self.shaders():
            nodeGraphObj = shaderProxyObj.inputNodeGraph()
            nodeGraphObj._node_graph__set_bind_obj_update_()
        return self.shaders()

    def _xml_obj__get_sibling_element_list_(self):
        lis = []
        # node graph
        for shaderProxyObj in self.shaders():
            nodeGraphObjs = shaderProxyObj.inputNodeGraphs()
            if nodeGraphObjs:
                for nodeGraphObj in nodeGraphObjs:
                    if nodeGraphObj.hasBindNodes():
                        if not nodeGraphObj in lis:
                            lis.append(nodeGraphObj)
        return lis

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.pathString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxGeometryProxy(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhGeometryProxy
):
    def _initAbsMtxGeometryProxy(self, *args, **kwargs):
        self._initAbsGrhGeometryProxy(*args, **kwargs)

        self._initAbsDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_list_(self):
        return [
            self.path(),
            self.bindObject().typepath()
        ]

    def _xml_obj__get_child_element_list_(self):
        return self.changedProperties() + self.changedVisibilities()


# node graph ********************************************************************************************************* #
class AbsMtxNodeGraph(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhNodeGraph
):
    def _initAbsMtxNodeGraph(self, *args, **kwargs):
        self._initAbsGrhNodeGraph(*args, **kwargs)

    # **************************************************************************************************************** #
    def _xml_obj__get_attribute_list_(self):
        return [
            self.path()
        ]

    def _xml_obj__get_child_element_list_(self):
        return self.bindNodes() + self.bindOtportProxies()

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.pathString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


class AbsMtxNodeGraphOtportProxy(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj,
    grhObjAbs.AbsGrhNodeGraphPortProxy,
):
    def _initAbsMtxNodeGraphOtportProxy(self, *args, **kwargs):
        self._initAbsGrhNodeGraphPortProxy(*args, **kwargs)

        self._initAbsDatXmlObj()

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_list_(self):
        return [
            self.path(),
            self.bindObject().datatype(),
            self.bindObject()
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.pathString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            self.bindNodeGraph(),
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


# portset ************************************************************************************************************ #
class AbsMtxPortset(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj
):
    CLS_mtx__name = None

    CLS_grh__node__port_stack = None
    
    def _initAbsMtxPortset(self, *args):
        self._nameObj = self.CLS_mtx__name(*args)

        self._portStackObj = self.CLS_grh__node__port_stack()

        self._initAbsDatXmlObj()

    def restore(self):
        self._portStackObj.restore()

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
        self._portStackObj.addObject(portObject)

    def addPorts(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addPort(i) for i in _]

    def ports(self):
        return self._portStackObj.objects()

    def hasPorts(self):
        return self._portStackObj.hasObjects()

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.name()._xml_obj__get_attribute_attach_value_str_()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]

    def _xml_obj__get_attribute_list_(self):
        return [
            self.name()
        ]

    def _xml_obj__get_child_element_list_(self):
        return self.ports()


# geometry collection
class AbsMtxCollection(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj
):
    CLS_mtx__name = None

    CLS_mtx__look__geometry_proxy_stack = None
    CLS_mtx__collection_set = None

    DEF_geometry_separator = None

    def _initAbsMtxCollection(self, *args):
        self._nameObj = self.CLS_mtx__name(*args)

        self._geometryProxyStackObj = self.CLS_mtx__look__geometry_proxy_stack()
        self._collectionStackObj = self.CLS_mtx__collection_set()
        self._excludeGeometryStackObj = self.CLS_mtx__look__geometry_proxy_stack()

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def nameString(self):
        """
        :return: str
        """
        return self._nameObj.toString()

    def setNameString(self, nameString):
        """
        :param nameString: str
        :return: None
        """
        self._nameObj.setRaw(nameString)

    def addGeometry(self, geometryProxyObj):
        """
        :param geometryProxyObj: object of Geometry
        :return:
        """
        self._geometryProxyStackObj.addObject(geometryProxyObj)

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
        return self._geometryProxyStackObj.objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self._geometryProxyStackObj.hasObjects()

    def geometryNameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.bindPathString() for i in self.geometries()]

    def geometryPathStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.bindPathString() for i in self.geometries()]

    def excludeGeometrySet(self):
        return self._excludeGeometryStackObj

    def addExcludeGeometry(self, geometryProxyObj):
        self._excludeGeometryStackObj.addObject(geometryProxyObj)

    def addExcludeGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addExcludeGeometry(i) for i in list(_)]

    def excludeGeometries(self):
        return self._excludeGeometryStackObj.objects()

    def collectionSet(self):
        return self._collectionStackObj

    def addCollection(self, collectionObject):
        """
        :param collectionObject: object of Collection
        :return: None
        """
        self._collectionStackObj.addObject(collectionObject)

    def hasCollections(self):
        """
        :return: bool
        """
        return self._collectionStackObj.hasObjects()

    def collections(self):
        """
        :return: list(object of Collection, ...)
        """
        return self._collectionStackObj.objects()

    def collectionNames(self):
        """
        :return: list(str, ...)
        """
        return [i.nameString() for i in self.collections()]

    def toString(self):
        return self.nameString()

    def _xml_obj__get_attribute_list_(self):
        return [
            self._nameObj,
            self._geometryProxyStackObj,
            self.collectionSet(),
            self.excludeGeometrySet()
        ]

    def _xml_obj__get_attribute_attach_value_str_(self):
        return self.nameString()

    def _xml_obj__get_attribute_attach_list_(self):
        return [
            (self._xml_obj__get_attribute_attach_key_str_(), self._xml_obj__get_attribute_attach_value_str_())
        ]


# assign ************************************************************************************************************* #
class AbsMtxAssign(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj
):
    CLS_mtx__name = None
    CLS_mtx__look__geometry_proxy_stack = None

    DEF_geometry_separator = None

    def _initAbsMtxAssign(self, *args):
        lookArg, nameArg = args

        self._lookObj = lookArg

        self._nameObj = self.CLS_mtx__name(nameArg)

        self._geometryProxyStackObj = self.CLS_mtx__look__geometry_proxy_stack(
            self.nameString()
        )
        self._collectionObj = None

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
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
        self._nameObj._raw__set_create_by_str_(nameString)

    # **************************************************************************************************************** #
    def look(self):
        return self._lookObj

    # **************************************************************************************************************** #
    def _assign__set_geometry_proxy_add_(self, *args):
        geometryProxyObj = args[0]
        self._geometryProxyStackObj.addObject(geometryProxyObj)

    def hasGeometry(self, *args):
        return self._geometryProxyStackObj._obj_stack__get_obj_exist_(*args)

    def addGeometry(self, geometryProxyObj):
        """
        :param geometryProxyObj: object of Geometry
        :return: None
        """
        self._assign__set_geometry_proxy_add_(geometryProxyObj)

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
        return self._geometryProxyStackObj.objects()

    def hasGeometries(self):
        """
        :return: bool
        """
        return self._geometryProxyStackObj.hasObjects()

    def geometryNameStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.nameString() for i in self.geometries()]

    def geometryPathStrings(self):
        """
        :return: list(str, ...)
        """
        return [i.bindPathString() for i in self.geometries()]

    # **************************************************************************************************************** #
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

    def _xmlElementAttaches_(self):
        pass


class AbsMtxMaterialAssign(AbsMtxAssign):
    def _initAbsMtxMaterialAssign(self, *args):
        self._initAbsMtxAssign(*args)

        self._materialProxyObj = None

    def setMaterial(self, tgtMaterialObj):
        """
        :param tgtMaterialObj: object of MaterialProxy
        :return:
        """
        self._materialProxyObj = tgtMaterialObj

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

    def _xml_obj__get_attribute_attach_value_str_(self):
        self.nameString()

    def _xml_obj__get_attribute_list_(self):
        return [
            self.name(),
            self.material(),
            self._geometryProxyStackObj,
            self.collection()
        ]


class AbsMtxPropertyAssign(AbsMtxAssign):
    def _initAbsMtxPropertyAssign(self, *args):
        pass


class AbsMtxPropertysetAssign(AbsMtxAssign):
    CLS_mtx__propertyset = None

    def _initAbsMtxPropertysetAssign(self, *args):
        self._initAbsMtxAssign(*args)

        self._propertysetObj = None

    def _setPropertyset_(self, *args):
        if isinstance(args[0], (str, unicode)):
            propertysetObject = self.CLS_mtx__propertyset(args[0])
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

    def _xml_obj__get_attribute_list_(self):
        return [
            self.name(),
            self.propertyset(),
            self._geometryProxyStackObj,
            self.collection()
        ]


class AbsMtxVisibilityAssign(AbsMtxAssign):
    CLS_grh__type = None

    CLS_mtx__value_visibility = None

    CLS_mtx__geometry_viewer_set = None

    def _initAbsMtxVisibilityAssign(self, *args):
        self._initAbsMtxAssign(*args)

        self._vistypeObj = None

        self._visibilityValueObj = None

        self._viewerGeometryStackObj = self.CLS_mtx__geometry_viewer_set()

    def type(self):
        return self._vistypeObj

    def typeString(self):
        return self._vistypeObj.toString()

    def visible(self):
        return self._visibilityValueObj

    def assignVisibility(self, portObj):
        visibilityString = portObj.portpathString()

        self._vistypeObj = self.CLS_grh__type(visibilityString)

        self._visibilityValueObj = portObj.value()

    def addViewerGeometry(self, geometryProxyObj):
        self._viewerGeometryStackObj.addObject(geometryProxyObj)

    def viewerGeometries(self):
        return self._viewerGeometryStackObj.objsets()

    # xml ************************************************************************************************************ #
    def _xmlElementAttaches_(self):
        return [
            self._collectionObj
        ]

    def _xml_obj__get_attribute_list_(self):
        return [
            self.name(),
            self.type(),
            self.visible(),
            self._geometryProxyStackObj,
            self._viewerGeometryStackObj,
            self.collection()
        ]


# ******************************************************************************************************************** #
class AbsMtxLook(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj
):
    CLS_mtx__look__name = None
    CLS_mtx__look__namespace = None

    CLS_mtx__look__assign_stack = None

    CLS_mtx__look__material_assign = None
    CLS_mtx__look__material_assign_stack = None

    CLS_mtx__look__propertyset_assign = None
    CLS_mtx__look__propertyset_assign_stack = None

    CLS_mtx__look__visibility_assign = None
    CLS_mtx__look__visibility_assign_stack = None

    CLS_mtx__look__geometry_proxy_stack = None

    def _initAbsMtxLook(self, *args):
        fileArg, nameArg = args

        self._fileObj = fileArg
        self._nameObj = self.CLS_mtx__look__name(nameArg)

        self._visibilityAssignStackObj = self.CLS_mtx__look__visibility_assign_stack(nameArg)
        self._materialAssignStackObj = self.CLS_mtx__look__material_assign_stack(nameArg)
        self._propertysetAssignStackObj = self.CLS_mtx__look__propertyset_assign_stack(nameArg)

        self._geometryProxyStackObj = self.CLS_mtx__look__geometry_proxy_stack(nameArg)

        self._initAbsDatXmlObj()

    # **************************************************************************************************************** #
    def _look__set_assigns_create_(self):
        for i in self._geometryProxyStackObj.objects():
            self._look__set_material_assigns_create_(i)
            self._look__set_propertyset_assigns_create_(i)
            self._look__set_visibility_assigns_create_(i)

    def _look__set_material_assigns_create_(self, geometryProxyObj):
        def addFnc_(geometryProxyObj_, materialProxyObj_):
            _materialNodeObj = materialProxyObj_.bindObject()
            _count = self._materialAssignStackObj.objectsCount()
            _keyString = _materialNodeObj.pathString()
            if self._materialAssignStackObj._obj_stack__get_obj_exist_(_keyString):
                _materialAssignObj = self._materialAssignStackObj._obj_stack__get_obj_(_keyString)
            else:
                _materialAssignObj = self.CLS_mtx__look__material_assign(
                    self, u'material_assign_{}'.format(_count)
                )
                _materialAssignObj.setMaterial(materialProxyObj_)
                self._materialAssignStackObj._obj_stack__set_obj_add_(_keyString, _materialAssignObj)

            if _materialAssignObj.hasGeometry(geometryProxyObj_) is False:
                _materialAssignObj.addGeometry(geometryProxyObj_)
        #
        # namespaceStr = self.nameString()
        # materialProxyObj = geometryProxyObj.inputNodeProxy(namespaceStr)
        # if materialProxyObj is not None:
        #     addFnc_(geometryProxyObj, materialProxyObj)
        materialProxyObjList = geometryProxyObj.assignmentMaterialProxies()
        for materialProxyObj in materialProxyObjList:
            addFnc_(geometryProxyObj, materialProxyObj)

    def _look__set_propertyset_assigns_create_(self, geometryProxyObj):
        def addFnc_(geometryProxyObj_, propertysetObj_):
            _count = self._propertysetAssignStackObj.objectsCount()
            _keyString = geometryProxyObj_.bindPathString()
            if self._propertysetAssignStackObj._obj_stack__get_obj_exist_(_keyString):
                _propertysetAssignObj = self._propertysetAssignStackObj._obj_stack__get_obj_(_keyString)
            else:
                _propertysetAssignObj = self.CLS_mtx__look__propertyset_assign(
                    self, propertysetObj_.nameString()
                )
                # _materialAssignObj = self.CLS_mtx__look__material_assign(
                #     self, u'material_assign_{}'.format(_count)
                # )
                self._propertysetAssignStackObj._obj_stack__set_obj_add_(_keyString, _propertysetAssignObj)

            _propertysetAssignObj.setPropertyset(propertysetObj_)
            if _propertysetAssignObj.hasGeometry(geometryProxyObj_) is False:
                _propertysetAssignObj.addGeometry(geometryProxyObj_)

        bindPortsetNamespaceStr = geometryProxyObj.bindPortsetNamespaceString()
        propertysetObj = geometryProxyObj._geometry_proxy__set_propertyset_update_(bindPortsetNamespaceStr)
        if propertysetObj.hasPorts():
            addFnc_(geometryProxyObj, propertysetObj)

    def _look__set_visibility_assigns_create_(self, geometryProxyObj):
        def addFnc_(geometryProxyObj_, portProxyObj_):
            _portObject = portProxyObj_.bindObject()
            _count = self._visibilityAssignStackObj.objectsCount()
            _keyString = _portObject.portpathString()
            if self._visibilityAssignStackObj._obj_stack__get_obj_exist_(_keyString):
                _visibilityObject = self._visibilityAssignStackObj._obj_stack__get_obj_(_keyString)
            else:
                _visibilityObject = self.CLS_mtx__look__visibility_assign(
                    self, u'visibility_assign_{}'.format(_count)
                )
                _visibilityObject.assignVisibility(_portObject)
                self._visibilityAssignStackObj._obj_stack__set_obj_add_(_keyString, _visibilityObject)

            if _visibilityObject.hasGeometry(geometryProxyObj_) is False:
                _visibilityObject.addGeometry(geometryProxyObj_)

        geometryVisibilities = geometryProxyObj.changedVisibilities()
        if geometryVisibilities:
            [addFnc_(geometryProxyObj, i) for i in geometryVisibilities]

    # **************************************************************************************************************** #
    def _look__get_geometry_namespace_str_(self):
        return self.nameString()

    def geometryNamespaceString(self):
        return self._look__get_geometry_namespace_str_()

    # **************************************************************************************************************** #
    def file(self):
        return self._fileObj

    # **************************************************************************************************************** #
    def name(self):
        return self._nameObj

    def nameString(self):
        return self._nameObj.toString()

    # **************************************************************************************************************** #
    def geometries(self):
        return self._geometryProxyStackObj.objects()

    def hasGeometries(self):
        return self._geometryProxyStackObj.hasObjects()

    def _look__set_geometry_proxy_add_(self, *args):
        geometryProxyObj = args[0]
        if geometryProxyObj.namespace().isRoot() is True:
            geometryNamespaceStr = self.geometryNamespaceString()
            geometryProxyObj.setNamespaceString(geometryNamespaceStr)
        # add Variant
        # geometryObj = geometryProxyObj.bindObject()
        # geometryObj.addVariantObject(self.nameString())
        # add geometry
        self._geometryProxyStackObj.addObject(geometryProxyObj)

    def addGeometry(self, geometryProxyObj):
        self._look__set_geometry_proxy_add_(geometryProxyObj)

    def addGeometries(self, *args):
        if isinstance(args[0], (tuple, list)):
            [self.addGeometry(i) for i in list(args[0])]
        else:
            [self.addGeometry(i) for i in list(args)]

    def geometry(self, geometryString):
        return self._geometryProxyStackObj.object(geometryString)

    def hasGeometry(self, *args):
        return self._geometryProxyStackObj._obj_stack__get_obj_exist_(*args)

    # **************************************************************************************************************** #
    def materialAssigns(self):
        return self._materialAssignStackObj.objects()

    def propertysetAssigns(self):
        return self._propertysetAssignStackObj.objects()

    def visibilityAssigns(self):
        return self._visibilityAssignStackObj.objects()

    # **************************************************************************************************************** #
    def hasAssigns(self):
        return self.assigns() != []

    def assigns(self):
        return self.materialAssigns() + self.propertysetAssigns() + self.visibilityAssigns()

    def _xmlElementAttaches_(self):
        lis = []
        for assignObject in self.assigns():
            for xmlObject in assignObject._xmlElementAttaches_():
                if xmlObject is not None:
                    if xmlObject not in lis:
                        lis.append(xmlObject)
        return lis

    def _xml_obj__get_attribute_list_(self):
        return [
            self._nameObj
        ]

    def _xml_obj__get_child_element_list_(self):
        self._look__set_assigns_create_()
        return self.assigns()

    def _xml_obj__get_sibling_element_list_(self):
        return self._xmlElementAttaches_()


class AbsMtxFile(
    AbsMtxBasic,
    datObjAbs.AbsDatXmlObj
):
    CLS_mtx__file__path = None

    CLS_mtx__file__version = None

    CLS_mtx__file__reference_stack = None
    CLS_mtx__file__reference = None

    CLS_mtx__file__look_stack = None
    CLS_mtx__file__look = None

    VAR_mtx__file__version = None

    def __init__(self, *args, **kwargs):
        pass

    def _initAbsMtxFile(self, *args):
        self._filepathObj = self.CLS_mtx__file__path(*args)
        self._versionObj = self.CLS_mtx__file__version(self.VAR_mtx__file__version)

        self._referenceStackObj = self.CLS_mtx__file__reference_stack()
        self._lookStackObj = self.CLS_mtx__file__look_stack(self)

        self._initAbsDatXmlObj()

    def _file__set_look_add_(self, *args):
        if args:
            _ = args[0]
            if isinstance(_, (str, unicode)):
                lookStr = _
                lookObject = self.CLS_mtx__file__look(self, lookStr)
            elif isinstance(_, self.CLS_mtx__file__look):
                lookObject = _
            else:
                raise TypeError
        else:
            lookObject = self.CLS_mtx__file__look(self, u'default_look')

        self._lookStackObj.addObject(lookObject)
        return lookObject

    def _file__set_reference_add_(self, *args):
        if self.CLS_mtx__file__reference is not None:
            referenceCls = self.CLS_mtx__file__reference
        else:
            referenceCls = self.__class__

        if isinstance(args[0], (str, unicode)):
            fileObj = referenceCls(args[0])
        elif isinstance(args[0], referenceCls):
            fileObj = args[0]
        else:
            fileObj = referenceCls(u'default')

        keyString = fileObj.fullpathFilename()
        self._referenceStackObj._obj_stack__set_obj_add_(keyString, fileObj)

    def filepath(self):
        return self._filepathObj

    def fullpathFilename(self):
        return self._filepathObj.toString()

    def version(self):
        return self._versionObj

    def versionString(self):
        return self._versionObj.toString()

    def addReference(self, fileObject):
        self._file__set_reference_add_(fileObject)

    def references(self):
        return self._referenceStackObj.objects()

    def reference(self, fileString):
        return self._referenceStackObj.object(fileString)

    def hasLook(self, lookStr):
        return self._lookStackObj._obj_stack__get_obj_exist_(lookStr)

    def addLook(self, *args):
        """
        :param args:
            1.str
            2.instance of "Look"
        :return:
        """
        return self._file__set_look_add_(*args)

    def looks(self):
        return self._lookStackObj.objects()

    def look(self, lookStr):
        return self._lookStackObj.object(lookStr)

    def lookIndex(self, *args):
        return self._lookStackObj._obj_stack__get_obj_index_(*args)

    def save(self):
        xmlDoc = self.__str__()
        bscMethods.OsFile.write(
            self.fullpathFilename(), xmlDoc
        )

    def _xml_obj__get_attribute_list_(self):
        return [
            self.version()
        ]

    def _xml_obj__get_child_element_list_(self):
        return self.references() + self.looks()


class AbsMtxReference(AbsMtxFile):
    def _initAbsMtxReference(self, *args):
        self._initAbsMtxFile(*args)

    # xml ************************************************************************************************************ #
    def _xml_obj__get_attribute_list_(self):
        return [
            self._filepathObj
        ]


# ******************************************************************************************************************** #
class AbsMtxTrsLook(AbsMtxBasic):
    CLS_mtx__trs_look__tgt_look = None
    CLS_mtx__trs_look__trs_geometry_proxy = None

    def _initAbsMtxTrsLook(self, *args):
        trsFileArg, tgtLookArg = args
        self._trsFileObj = trsFileArg
        tgtFileObj = trsFileArg.tgtFile()
        self._tgtLookObj = self.CLS_mtx__trs_look__tgt_look(tgtFileObj, tgtLookArg)

    def trsFile(self):
        return self._trsFileObj

    def tgtLook(self):
        return self._tgtLookObj

    def addSrcGeometry(self, srcNodepathStr):
        # geometry namespace = look name
        namespaceStr = self.tgtLook().nameString()
        trsGeometryProxyObj = self.CLS_mtx__trs_look__trs_geometry_proxy(
            srcNodepathStr,
            namespace=namespaceStr
        )
        # target
        tgtGeometryProxyObj = trsGeometryProxyObj.tgtNodeProxy()
        if self.tgtLook().hasGeometry(tgtGeometryProxyObj) is False:
            self.tgtLook().addGeometry(tgtGeometryProxyObj)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Geometry "{}" is Exist.'''.format(tgtGeometryProxyObj.pathString())
            )

    def addSrcGeometries(self, *args):
        if isinstance(args[0], (list, tuple)):
            _ = args[0]
        else:
            _ = args

        [self.addSrcGeometry(i) for i in _]

    def _mtx__trs_look__set_material_assign_add_(self, *args):
        pass

    def addAssign(self, *args):
        self._mtx__trs_look__set_material_assign_add_(*args)

    def __str__(self):
        return self._tgtLookObj.__str__()


# ******************************************************************************************************************** #
class AbsMtxTrsFile(AbsMtxBasic):
    CLS_mtx__trs_file__tgt_file = None
    CLS_mtx__trs_file__trs_look = None

    IST_mtx__trs_file__trs_obj_queue = None

    def _initAbsMtxTrsFile(self, *args):
        fileString = args[0]
        self._tgtFileObj = self.CLS_mtx__trs_file__tgt_file(fileString)
        self._tgtFileObj.addReference(
            u'materialx/arnold/nodedefs.mtlx'
        )

    def tgtFile(self):
        return self._tgtFileObj

    def addLook(self, lookStr):
        trsLookObj = self.CLS_mtx__trs_file__trs_look(self, lookStr)
        if self._tgtFileObj.hasLook(lookStr) is False:
            tgtLookObk = trsLookObj.tgtLook()
            self._tgtFileObj.addLook(tgtLookObk)
        else:
            bscMethods.PyMessage.traceWarning(
                u'''Look "{}" is Exist.'''.format(lookStr)
            )
        return trsLookObj

    def tgtLook(self, lookStr):
        return self._tgtFileObj.look(lookStr)

    def tgtLooks(self):
        return self._tgtFileObj.looks()

    def save(self):
        for i in self.IST_mtx__trs_file__trs_obj_queue.nodes():
            i._grh__trs_node__set_after_expressions_run_()

        self._tgtFileObj.save()

        bscMethods.PyMessage.traceResult(
            u'save file "{}"'.format(
                self._tgtFileObj.fullpathFilename()
            )
        )

    def __str__(self):
        for i in self.IST_mtx__trs_file__trs_obj_queue.nodes():
            i._grh__trs_node__set_after_expressions_run_()

        return self._tgtFileObj.__str__()
