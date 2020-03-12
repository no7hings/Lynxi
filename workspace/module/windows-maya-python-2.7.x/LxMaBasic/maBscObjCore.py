# coding:utf-8
from LxBasic import bscMethods

from LxMaBasic import maBscConfigure, maBscMtdCore, maBscMethods


class Abc_MyaQueryCache(maBscConfigure.Utility):
    def _initAbcMyaQueryCache(self):
        self._objectPortStringsDict = {}
        self._objectPortQueryDict = {}
        self._objectPortkeyStringQueryDict = {}

    def _getPortkeyStrings_(self, categoryString, objectString):
        dic = self._objectPortStringsDict
        if categoryString in dic:
            return dic[categoryString]
        _ = maBscMtdCore.Mtd_MaObjectPort._mtl_getObjectPortkeyStringList(objectString)
        dic[categoryString] = _
        return _

    def _getQueryFnc_(self, categoryString, objectString, dic, fnc):
        if categoryString in dic:
            return dic[categoryString]

        portkeyStringList = self._getPortkeyStrings_(categoryString, objectString)

        _ = fnc(
            objectString,
            portkeyStringList
        )
        dic[categoryString] = _
        return _

    def _getObjectPortDefQuery_(self, categoryString, objectString):
        return self._getQueryFnc_(
            categoryString,
            objectString,
            self._objectPortQueryDict,
            maBscMtdCore.Mtd_MaObjectPort._mtl_getObjectPortDefDict
        )

    def _getObjectPortPortkeyQuery_(self, categoryString, objectString):
        return self._getQueryFnc_(
            categoryString,
            objectString,
            self._objectPortkeyStringQueryDict,
            maBscMtdCore.Mtd_MaObjectPort._mtl_getObjectPortkeyStringDict
        )


class Abc_MyaObjCache(maBscConfigure.Utility):
    pass


class Def_MyaObjCache(object):
    def _initDefMyaObjCache(self, keyString):
        self._defQueryKeyString = keyString

    def _myaDefCacheKeyString_(self):
        return self._defQueryKeyString


class Abc_MyaBasic(maBscConfigure.Utility):
    pass


class Abc_MyaObjectSet(Abc_MyaBasic):
    # noinspection PyUnusedLocal
    def _initAbcMyaObjectSet(self, *args):
        self._objectLis = []
        self._objectDict = {}

        self._objectCount = 0

        self._objectFilterStr = None

    def createByRaw(self, *args):
        pass

    def addObject(self, key, obj):
        assert key not in self._objectDict, u'''key "{}" is Exist.'''.format(key)
        self._objectLis.append(obj)
        self._objectDict[key] = obj
        self._objectCount += 1

    def hasObjects(self):
        """
        :return: bool
        """
        return self._objectLis != []

    def objects(self):
        """
        :return: list(object, ...)
        """
        return self._objectLis

    def _hasObject_(self, *args):
        """
        :return: bool
        """
        if isinstance(args[0], (str, unicode)):
            return args[0] in self._objectDict
        else:
            return args[0] in self._objectLis

    def _object_(self, *args):
        """
        :param args:
            1.str
            2.int
        :return: bool
        """
        if isinstance(args[0], (str, unicode)):
            keyString = args[0]
            assert keyString in self._objectDict, u'''Key: "{}" is Non - Exist.'''.format(keyString)
            return self._objectDict[keyString]
        elif isinstance(args[0], int):
            index = args[0]
            return self._objectLis[index]

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
        return self._objectLis[index]

    def hasObjectAt(self, index):
        """
        :param index: int
        :return: object
        """
        pass

    def __len__(self):
        """
        :return: int
        """
        return self.objectCount()


class Abc_MyaValue(Abc_MyaBasic):
    def _initAbcMyaValue(self, raw):
        self._raw = raw

    def raw(self):
        return self._raw

    def rawtype(self):
        return type(self.raw()).__name__

    def __str__(self):
        return u'{}(raw="{}", rawtype="{}")'.format(
            self.__class__.__name__,
            str(self.raw()),
            self.rawtype(),
        )


class Abc_MyaPort(Abc_MyaBasic):
    CLS_mya_port_string = None
    CLS_mya_value = None

    def __init__(self, *args):
        pass

    def _initAbcMyaPort(self, nodeObject, portString):
        self._objectObj = nodeObject

        self._portStringObj = self.CLS_mya_port_string(portString)

        self._porttypeString = None

        self._parentPortnameString = None

        self._childPortnameStringList = []

        self._isArray = False

    def _setPorttypeString_(self, porttypeString):
        self._porttypeString = porttypeString

    def _setParentPortnameString_(self, portnameString):
        self._parentPortnameString = portnameString

    def _setChildPortnameStrings_(self, portnameStrings):
        self._childPortnameStringList = portnameStrings

    def _setArray_(self, boolean):
        self._isArray = boolean

    def _getNodeObject_(self, nodeString):
        return self._objectObj.__class__(nodeString)

    def _create_(self, nodeString, portString):
        if isinstance(nodeString, (str, unicode)):
            nodeObject = self._objectObj.__class__(nodeString)
        else:
            nodeObject = nodeString
        return nodeObject.attribute(portString)

    def node(self, *args):
        if args:
            cls = args[0]
            shaderObject = cls(self._objectObj.fullpathName())
            if isinstance(shaderObject, Abc_MyaShader):
                shaderObject._setContext_(args[1])
            return shaderObject
        return self._objectObj

    def fullpathName(self):
        return bscMethods.MaAttributeString.composeBy(
            self._objectObj.fullpathName(),
            self.fullpathPortname()
        )

    def fullpathPortname(self):
        return self._portStringObj.fullpathPortname()

    def portname(self):
        return self._portStringObj.portname()

    def value(self):
        return self.CLS_mya_value(
            self.portdata()
        )

    def portdata(self):
        nodeString = self.node().fullpathName()
        portString = self.fullpathPortname()
        return maBscMtdCore.Mtd_MaObjectPort._mtl_getObjectPortdata(
            nodeString, portString
        )

    def porttype(self):
        return self._porttypeString

    def isMessage(self):
        return self._porttypeString == u'message'

    def isColor(self):
        return self._porttypeString in [u'color3', u'color4']

    def isFilename(self):
        return self._porttypeString == u'filename'

    def isArray(self):
        return self._isArray

    def nicename(self):
        return maBscMethods.Attribute.nicename(self.fullpathName())

    def hasParent(self):
        return self._parentPortnameString is not None

    def parent(self):
        if self.hasParent():
            return self._objectObj.attribute(self._parentPortnameString)

    def hasChildren(self):
        return self._childPortnameStringList != []

    def children(self):
        if self.hasChildren():
            return [
                self._objectObj.attribute(i) for i in self._childPortnameStringList
            ]
        return []

    def child(self, portnameString):
        if self.hasChildren():
            return self._objectObj.attribute(portnameString)

    def hasChild(self, portnameString):
        return portnameString in self._childPortnameStringList

    def defaultRaw(self):
        pass

    def hasSource(self):
        return maBscMethods.Attribute.hasSource(self.fullpathName())

    def isSource(self):
        return maBscMethods.Attribute.isSource(self.fullpathName())

    def source(self):
        portString = self.fullpathName()
        if maBscMethods.Attribute.isAppExist(self.fullpathName()):
            maBscMethods.Attribute.source(portString)
            sourceAttributeString = maBscMethods.Attribute.source(portString)
            if sourceAttributeString:
                sourceNodeString = maBscMethods.Attribute.nodeString(sourceAttributeString)
                sourcePortString = maBscMethods.Attribute.fullpathPortname(sourceAttributeString)
                sourceNodeObject = self._getNodeObject_(sourceNodeString)
                return sourceNodeObject.attribute(sourcePortString)

    def hasTargets(self):
        return maBscMethods.Attribute.hasTargets(self.fullpathName())

    def isTarget(self):
        return maBscMethods.Attribute.isTarget(self.fullpathName())

    def targets(self):
        lis = []
        for attributeString in maBscMethods.Attribute.targets(self.fullpathName()):
            lis.append(
                self._create_(
                    maBscMethods.Attribute.nodeString(attributeString),
                    maBscMethods.Attribute.fullpathPortname(attributeString)
                )
            )
        return lis

    def __str__(self):
        return u'{}(fullpathPortname="{}", porttype="{}", node="{}")'.format(
            self.__class__.__name__,
            self.fullpathPortname(),
            self.porttype(),
            self.node().fullpathName()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaConnection(Abc_MyaBasic):
    def _initAbcMyaConnection(self, sourceAttributeObject, targetAttributeObject):
        self._sourceAttributeObj = sourceAttributeObject
        self._targetAttributeObj = targetAttributeObject

    def source(self):
        return self._sourceAttributeObj

    def target(self):
        return self._targetAttributeObj

    def __str__(self):
        return 'connection(source="{}", target="{}")'.format(self.source().fullpathName(), self.target().fullpathName())

    def __repr__(self):
        return self.__str__()


class Abc_MyaObject(
    Abc_MyaBasic,
    Def_MyaObjCache
):
    CLS_mya_node_string = None
    CLS_mya_port = None

    CLS_mya_port_set = None

    OBJ_mya_query_cache = None

    def __init__(self, *args):
        pass

    def _initAbcMyaObject(self, nodeString):
        assert maBscMethods.Node.isExist(nodeString), u'{} is Non-Exist'.format(nodeString)
        self._nodeStringObj = self.CLS_mya_node_string(
            nodeString
        )

        self._categoryString = maBscMethods.Node.category(self.fullpathName())

        self._initDefMyaObjCache(self._categoryString)

        self._portDefQuery = self.OBJ_mya_query_cache._getObjectPortDefQuery_(
            self._categoryString,
            self.fullpathName()
        )
        self._portkeyQuery = self.OBJ_mya_query_cache._getObjectPortPortkeyQuery_(
            self._categoryString,
            self.fullpathName()
        )

        self._portSetObj = self.CLS_mya_port_set()
        self._inputSetObj = self.CLS_mya_port_set()
        self._outputSetObj = self.CLS_mya_port_set()

        self._addPorts_()

    def _toPortkey_(self, portnameString):
        if portnameString in self._portkeyQuery:
            return self._portkeyQuery[portnameString]
        return portnameString

    def _addPorts_(self):
        def addPortFnc_(portString_, portDef_, portCls_):
            _assignString = portDef_[self.DEF_mya_key_assign]
            _porttypeString = portDef_[self.DEF_mya_key_porttype]
            _parentPortnameString = portDef_[self.DEF_mya_key_parent]
            _childPortnameStrings = portDef_[self.DEF_mya_key_children]
            _isArray = portDef_[self.DEF_mya_key_array]

            _portObject = portCls_(self, portString_)
            _portObject._setPorttypeString_(_porttypeString)
            if _assignString == self.DEF_mya_keyword_input:
                self._inputSetObj.addObject(portString_, _portObject)
            elif _assignString == self.DEF_mya_keyword_output:
                self._outputSetObj.addObject(portString_, _portObject)

            _portObject._setParentPortnameString_(_parentPortnameString)
            _portObject._setChildPortnameStrings_(_childPortnameStrings)
            _portObject._setArray_(_isArray)

            self._portSetObj.addObject(portString_, _portObject)

        for k, v in self._portDefQuery.items():
            addPortFnc_(k, v, self.CLS_mya_port)

    def fullpathName(self):
        return self._nodeStringObj.fullpathName()

    def name(self):
        return self._nodeStringObj.name()

    def category(self):
        return self._categoryString

    def isExist(self):
        return maBscMethods.Node.isExist(self.fullpathName())

    def attributes(self):
        return self._portSetObj.objects()

    def hasAttribute(self, portString):
        return self._portSetObj._hasObject_(portString)

    def attribute(self, portString):
        return self._portSetObj._object_(
            self._toPortkey_(portString)
        )

    def inputs(self):
        return self._inputSetObj.objects()

    def hasInput(self, portString):
        return self._inputSetObj._hasObject_(portString)

    def input(self, portString):
        return self._inputSetObj._object_(
            self._toPortkey_(portString)
        )

    def outputs(self):
        return self._outputSetObj.objects()

    def hasOutput(self, portString):
        return self._outputSetObj._hasObject_(portString)

    def output(self, portString):
        return self._outputSetObj._object_(
            self._toPortkey_(portString)
        )

    def isDag(self):
        return maBscMethods.Node.isDag(self.fullpathName())

    def __str__(self):
        return u'{}(name="{}", category="{}")'.format(
            self.__class__.__name__,
            self.name(),
            self.category()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaNodeGraph(Abc_MyaBasic):
    CLS_mya_node = None
    CLS_mya_connection = None

    def _initAbcMyaNodeGraph(self, *args):
        self._targetNodeObj = args[0]

        self._nameString = self._targetNodeObj.fullpathName() + '__nodegraph'

    def name(self):
        return self._nameString

    def targetNode(self):
        return self._targetNodeObj

    def nodes(self):
        return [
            self.CLS_mya_node(i)
            for i in maBscMtdCore.Mtd_MaNodeGraph._getNodeGraphNodeStringList(self._targetNodeObj.fullpathName())
        ]

    def outputs(self):
        lis = []
        for i in self._targetNodeObj.attributes():
            if i.hasSource():
                lis.append(i.source())
        return lis

    def connections(self):
        lis = []
        for i in self.nodes():
            for j in i.attributes():
                if j.hasSource():
                    lis.append(self.CLS_mya_connection(j.source(), j))
        return lis

    def __str__(self):
        return u'{}(name="{}")'.format(
            self.__class__.__name__,
            self.name()
        )


class Abc_MyaShader(Abc_MyaObject):
    CLS_mya_node_graph = None

    def __init__(self, *args):
        pass

    def _initAbcMyaShader(self, nodeString):
        self._initAbcMyaObject(nodeString)
        self._contextString = None

    def _setContext_(self, typeString):
        self._contextString = typeString

    def context(self):
        return self._contextString

    def nodeGraph(self):
        return self.CLS_mya_node_graph(self)

    def __str__(self):
        return u'{}(name="{}", category="{}", context="{}")'.format(
            self.__class__.__name__,
            self.name(),
            self.category(),
            self.context()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaMaterial(Abc_MyaObject):
    CLS_mya_shader = None

    DEF_mya_portname_surface_shader = 'surfaceShader'
    DEF_mya_portname_displacement_shader = 'displacementShader'
    DEF_mya_portname_volume_shader = 'volumeShader'

    def _initAbcMyaMaterial(self, nodeString):
        self._initAbcMyaObject(nodeString)

    def shaders(self):
        return bscMethods.List.cleanupTo(
            [
                self.surfaceShader(),
                self.displacementShader(),
                self.volumeShader()
            ]
        )

    def surfaceInput(self):
        return self._portSetObj._object_(self.DEF_mya_portname_surface_shader)

    def surfaceSource(self):
        return self.surfaceInput().source()

    def surfaceShader(self):
        _ = self.surfaceSource()
        if _:
            return _.node(
                self.CLS_mya_shader,
                self.DEF_mya_portname_surface_shader
            )

    def displacementInput(self):
        return self._portSetObj._object_(self.DEF_mya_portname_displacement_shader)

    def displacementSource(self):
        return self.displacementInput().source()

    def displacementShader(self):
        _ = self.displacementSource()
        if _:
            return _.node(
                self.CLS_mya_shader,
                self.DEF_mya_portname_displacement_shader
            )

    def volumeInput(self):
        return self._portSetObj._object_(self.DEF_mya_portname_volume_shader)

    def volumeSource(self):
        return self.volumeInput().source()

    def volumeShader(self):
        _ = self.volumeSource()
        if _:
            return _.node(
                self.CLS_mya_shader,
                self.DEF_mya_portname_volume_shader
            )


class Abc_MyaNode(Abc_MyaObject):
    def __init__(self, *args):
        pass

    def _initAbcMyaNode(self, nodeString):
        self._initAbcMyaObject(nodeString)


class Abc_MyaDag(Abc_MyaObject):
    CLS_mya_dag = None
    CLS_mya_node = None

    def _initAbcMyaDag(self, nodeString):
        assert maBscMethods.Node.isExist(nodeString), u'{} is Non-Exist'.format(nodeString)
        # Convert to fullpath
        self._initAbcMyaObject(
            maBscMethods.Node.toFullpathName(nodeString)
        )

    def parent(self):
        return self.CLS_mya_dag(
            maBscMtdCore.Mtd_MaDag._getDagParentString(self.fullpathName())
        )

    def children(self):
        return [
            self.CLS_mya_dag(i)
            for i in maBscMtdCore.Mtd_MaDag._getDagChildStringList(self.fullpathName())
        ]

    def __str__(self):
        return u'{}(fullpathName="{}", category="{}")'.format(
            self.__class__.__name__,
            self.fullpathName(),
            self.category()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaCompoundDag(Abc_MyaDag):
    CLS_mya_transform = None

    def _initAbcMyaCompoundDag(self, nodeString):
        # Convert to transform fullpath
        shapeString = maBscMethods.Node.shapeName(nodeString)

        self._initAbcMyaDag(shapeString)

    def transform(self):
        return self.CLS_mya_transform(
            maBscMethods.Node.transformName(self.fullpathName())
        )

    def __str__(self):
        return u'{}(fullpathName="{}", category="{}")'.format(
            self.__class__.__name__,
            self.fullpathName(),
            self.category()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaTransform(Abc_MyaDag):
    def _initAbcMyaTransform(self, nodeString):
        self._initAbcMyaDag(nodeString)

    def shape(self):
        return self.CLS_mya_dag(
            maBscMethods.Node.shapeName(self.fullpathName())
        )

    def shapes(self):
        return [
            self.CLS_mya_dag(i)
            for i in maBscMtdCore.Mtd_MaObject._getNodeShapeNodeStringList(self.fullpathName())
        ]


class Abc_MyaGeometry(Abc_MyaCompoundDag):
    CLS_mya_material = None

    def _initAbcMyaGeometry(self, nodeString):
        self._initAbcMyaCompoundDag(nodeString)

    def materials(self):
        return [
            self.CLS_mya_material(i)
            for i in maBscMtdCore.Mtd_MaObject._getNodeShadingEngineNodeStringList(self.fullpathName())
        ]


class Abc_MyaGroup(Abc_MyaDag):
    def _initAbcMyaGroup(self, nodeString):
        self._initAbcMyaDag(nodeString)

    def __str__(self):
        return u'{}(fullpathName="{}")'.format(
            self.__class__.__name__,
            self.fullpathName(),
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaNodeRoot(Abc_MyaBasic):
    CLS_group = None
    CLS_node = None

    def _initAbcMyaNodeRoot(self, groupString):
        self._rootObj = self.CLS_group(groupString)

    def root(self):
        return self._rootObj

    def groups(self):
        return


class Abc_MyaGeometryRoot(Abc_MyaNodeRoot):
    CLS_geometry = None

    def _initAbcMyaGeometryRoot(self, groupString):
        self._initAbcMyaNodeRoot(groupString)

    def meshes(self):
        return [
            self.CLS_geometry(i)
            for i in maBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.root().fullpathName(),
                includeCategoryString=self.DEF_mya_type_mesh,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def nurbsSurface(self):
        return [
            self.CLS_geometry(i)
            for i in maBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.root().fullpathName(),
                includeCategoryString=self.DEF_mya_type_nurbs_surface,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def nurbsCurves(self):
        return [
            self.CLS_geometry(i)
            for i in maBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.root().fullpathName(),
                includeCategoryString=self.DEF_mya_type_nurbs_curve,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def geometries(self):
        return [
            self.CLS_geometry(i)
            for i in maBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.root().fullpathName(),
                includeCategoryString=self.DEF_mya_type_geometry_list,
                useShapeCategory=True,
                withShape=False
            )
        ]

