# coding:utf-8
from LxBasic import bscMethods

from LxMaBasic import maBscConfigure, maBscMtdCore, maBscMethods


class Abc_MaBasic(maBscConfigure.Utility):
    pass


class Abc_MaObjectSet(Abc_MaBasic):
    # noinspection PyUnusedLocal
    def _initAbcMaObjectSet(self, *args):
        self._objectLis = []
        self._objectDic = {}

        self._objectCount = 0

        self._objectFilterStr = None

    def createByRaw(self, *args):
        pass

    def addObject(self, key, obj):
        assert key not in self._objectDic, '''Key is Exist.'''
        self._objectLis.append(obj)
        self._objectDic[key] = obj
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

    def hasObject(self, *args):
        """
        :return: bool
        """
        if isinstance(args[0], (str, unicode)):
            return args[0] in self._objectDic
        else:
            return args[0] in self._objectLis

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

    def objectWithKey(self, keyString):
        """
        :param keyString: str
        :return: bool
        """
        assert keyString in self._objectDic, u'''Key is Non - Exist.'''
        return self._objectDic[keyString]

    def hasObjectWithKey(self, keyString):
        """
        :param keyString: str
        :return: bool
        """
        return keyString in self._objectDic

    def __len__(self):
        """
        :return: int
        """
        return self.objectCount()


class Abc_MaValue(Abc_MaBasic):
    def _initAbcMaValue(self, typeString, data):
        self.datatypeString = typeString
        self._data = data

    def data(self):
        return self._data

    def datatype(self):
        return self.datatypeString

    def __str__(self):
        return u'{}(data={}({}), datatype="{}")'.format(
            self.__class__.__name__,
            type(self.data()).__name__,
            str(self.data()),
            self.datatype()
        )


class Abc_MaAttribute(Abc_MaBasic):
    CLS_mya_port_string = None
    CLS_mya_value = None

    def __init__(self, *args):
        pass

    def _initAbcMaAttribute(self, nodeObject, portString):
        self._nodeObj = nodeObject

        self._portStringObj = self.CLS_mya_port_string(portString)

        self._valueObj = self.CLS_mya_value(
            maBscMethods.Attribute.datatype(self.fullpathName()),
            maBscMethods.Attribute.data(self.fullpathName())
        )

    def _create_(self, nodeString, portString):
        if isinstance(nodeString, (str, unicode)):
            return self.__class__(
                self._nodeObj.__class__(nodeString),
                portString
            )
        return self.__class__(
            nodeString,
            portString
        )

    def node(self, *args):
        if args:
            cls = args[0]
            shaderObject = cls(self._nodeObj.fullpathName())
            if isinstance(shaderObject, Abc_MaShader):
                shaderObject._setContext(args[1])
            return shaderObject
        return self._nodeObj

    def fullpathName(self):
        return bscMethods.MaAttributeString.composeBy(
            self._nodeObj.fullpathName(),
            self.fullpathPortname()
        )

    def fullpathPortname(self):
        return self._portStringObj.fullpathPortname()

    def portname(self):
        return self._portStringObj.portname()

    def porttype(self):
        return self.value().datatype()

    def value(self):
        return self._valueObj

    def data(self):
        return self.value().data()

    def datatype(self):
        return self.value().datatype()

    def isCompound(self):
        return maBscMethods.Attribute.isCompound(self.fullpathName())

    def isMultichannel(self):
        return maBscMethods.Attribute.isMultichannel(self.fullpathName())

    def isMessage(self):
        return maBscMethods.Attribute.isMessage(self.fullpathName())

    def hasParent(self):
        return maBscMethods.Attribute.parent(self.fullpathName()) is not None

    def parent(self):
        _ = maBscMethods.Attribute.parent(self.fullpathName())
        if _:
            return self._create_(self.node(), _)

    def hasChildren(self):
        return maBscMethods.Attribute.hasChildren(self.fullpathName())

    def children(self):
        _ = maBscMethods.Attribute.children(self.fullpathName())
        if _:
            lis = []
            for i in _:
                lis.append(
                    self._create_(
                        self.node(),
                        maBscMethods.Attribute.composeBy(self.fullpathPortname(), i)
                    )
                )
            return lis
        return []

    def defaultRaw(self):
        pass

    def hasSource(self):
        return maBscMethods.Attribute.hasSource(self.fullpathName())

    def isSource(self):
        return maBscMethods.Attribute.isSource(self.fullpathName())

    def source(self):
        _ = maBscMethods.Attribute.source(self.fullpathName())
        if _:
            return self._create_(
                maBscMethods.Attribute.nodeString(_),
                maBscMethods.Attribute.fullpathPortname(_)
            )
        return

    def hasTarget(self):
        return maBscMethods.Attribute.hasTarget(self.fullpathName())

    def isTarget(self):
        return maBscMethods.Attribute.isTarget(self.fullpathName())

    def target(self):
        _ = maBscMethods.Attribute.target(self.fullpathName())
        if _:
            return self._create_(
                maBscMethods.Attribute.nodeString(_),
                maBscMethods.Attribute.fullpathPortname(_)
            )
        return

    def __str__(self):
        return u'{}(fullpathPortname="{}", porttype="{}", node="{}")'.format(
            self.__class__.__name__,
            self.fullpathPortname(),
            self.porttype(),
            self.node().fullpathName()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MaConnection(Abc_MaBasic):
    def _initAbcMaConnection(self, sourceAttributeObject, targetAttributeObject):
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


class Abc_MaObject(Abc_MaBasic):
    CLS_mya_node_string = None
    CLS_mya_attribute = None

    CLS_mya_set_attribute = None

    def __init__(self, *args):
        pass

    def _initAbcMaObject(self, nodeString):
        assert maBscMethods.Node.isExist(nodeString), u'{} is Non-Exist'.format(nodeString)

        self._nodeStringObj = self.CLS_mya_node_string(
            nodeString
        )

        self._attributeSetObj = self.CLS_mya_set_attribute()
        for i in maBscMethods.Node.fullpathPortnames(self.fullpathName()):
            self._attributeSetObj.addObject(i, self.CLS_mya_attribute(self, i))

        self._attributeSetObj = self.CLS_mya_set_attribute()
        for i in maBscMethods.Node.inputFullpathPortname(self.fullpathName()):
            self._attributeSetObj.addObject(i, self.CLS_mya_attribute(self, i))

        self._outputSetObj = self.CLS_mya_set_attribute()
        for i in maBscMethods.Node.outputFullpathPortname(self.fullpathName()):
            self._outputSetObj.addObject(i, self.CLS_mya_attribute(self, i))

    def fullpathName(self):
        return self._nodeStringObj.fullpathName()

    def name(self):
        return self._nodeStringObj.name()

    def category(self):
        return maBscMethods.Node.category(self.fullpathName())

    def isExist(self):
        return maBscMethods.Node.isExist(self.fullpathName())

    def attributes(self):
        return self._attributeSetObj.objects()

    def attribute(self, portString):
        return self._attributeSetObj.objectWithKey(portString)

    def inputs(self):
        return self._attributeSetObj.objects()

    def input(self, portString):
        return self._attributeSetObj.objectWithKey(portString)

    def outputs(self):
        return self._outputSetObj.objects()

    def output(self, portString):
        return self._outputSetObj.objectWithKey(portString)

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


class Abc_MaNodeGraph(Abc_MaBasic):
    CLS_mya_node = None
    CLS_mya_connection = None

    def _initAbcMaNodeGraph(self, shaderObject):
        self._shaderObj = shaderObject

    def nodes(self):
        return [
            self.CLS_mya_node(i)
            for i in maBscMtdCore.Mtd_MaNodeGraph._getNodeGraphNodeStringList(self._shaderObj.fullpathName())
        ]

    def outputs(self):
        lis = []
        for i in self._shaderObj.attributes():
            if i.hasSource():
                lis.append(i)
        return lis

    def connections(self):
        lis = []
        for i in self.nodes():
            for j in i.attributes():
                if j.hasSource():
                    lis.append(self.CLS_mya_connection(j.source(), j))
        return lis


class Abc_MaShader(Abc_MaObject):
    CLS_mya_node_graph = None

    def __init__(self, *args):
        pass

    def _initAbcMaShader(self, nodeString):
        self._initAbcMaObject(nodeString)
        self._contextString = None

    def _setContext(self, typeString):
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


class Abc_MaMaterial(Abc_MaObject):
    CLS_mya_shader = None

    DEF_mya_portname_surface_shader = 'surfaceShader'
    DEF_mya_portname_displacement_shader = 'displacementShader'
    DEF_mya_portname_volume_shader = 'volumeShader'

    def _initAbcMaMaterial(self, nodeString):
        self._initAbcMaObject(nodeString)

    def shaders(self):
        return bscMethods.List.cleanupTo(
            [
                self.surfaceShader(),
                self.displacementShader(),
                self.volumeShader()
            ]
        )

    def surfaceInput(self):
        return self._attributeSetObj.objectWithKey(self.DEF_mya_portname_surface_shader)

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
        return self._attributeSetObj.objectWithKey(self.DEF_mya_portname_displacement_shader)

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
        return self._attributeSetObj.objectWithKey(self.DEF_mya_portname_volume_shader)

    def volumeSource(self):
        return self.volumeInput().source()

    def volumeShader(self):
        _ = self.volumeSource()
        if _:
            return _.node(
                self.CLS_mya_shader,
                self.DEF_mya_portname_volume_shader
            )


class Abc_MaDag(Abc_MaObject):
    CLS_mya_dag = None
    CLS_mya_node = None

    def _initAbcMaDag(self, nodeString):
        assert maBscMethods.Node.isExist(nodeString), u'{} is Non-Exist'.format(nodeString)
        # Convert to fullpath
        self._initAbcMaObject(
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


class Abc_MaCompoundDag(Abc_MaDag):
    CLS_mya_transform = None

    def _initAbcMaCompoundDag(self, nodeString):
        # Convert to transform fullpath
        self._initAbcMaDag(
            maBscMethods.Node.transformName(nodeString)
        )

        self._transformObj = self.CLS_mya_transform(
            maBscMethods.Node.transformName(self.fullpathName())
        )

        self._shapeObj = self.CLS_mya_dag(
            maBscMethods.Node.shapeName(self.fullpathName())
        )

    def transform(self):
        return self._transformObj

    def shape(self):
        return self._shapeObj

    def shapeCategory(self):
        return self.shape().category()

    def shapes(self):
        return [
            self.CLS_mya_dag(i)
            for i in maBscMtdCore.Mtd_MaNode._getNodeShapeNodeStringList(self.fullpathName())
        ]

    def __str__(self):
        return u'{}(fullpathName="{}", shapeCategory="{}")'.format(
            self.__class__.__name__,
            self.fullpathName(),
            self.shapeCategory()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MaTransform(Abc_MaDag):
    def _initAbcMaTransform(self, nodeString):
        self._initAbcMaDag(nodeString)


class Abc_MaGeometry(Abc_MaCompoundDag):
    CLS_mya_material = None

    def _initAbcMaGeometry(self, nodeString):
        self._initAbcMaCompoundDag(nodeString)

    def materials(self):
        return [
            self.CLS_mya_material(i)
            for i in maBscMtdCore.Mtd_MaNode._getNodeShadingEngineNodeStringList(self.fullpathName())
        ]


class Abc_MaGroup(Abc_MaDag):
    def _initAbcMaGroup(self, nodeString):
        self._initAbcMaDag(nodeString)

    def __str__(self):
        return u'{}(fullpathName="{}")'.format(
            self.__class__.__name__,
            self.fullpathName(),
        )

    def __repr__(self):
        return self.__str__()


class Abc_MaNodeRoot(Abc_MaBasic):
    CLS_group = None
    CLS_node = None

    def _initAbcMaNodeRoot(self, groupString):
        self._rootObj = self.CLS_group(groupString)

    def root(self):
        return self._rootObj

    def groups(self):
        return


class Abc_MaGeometryRoot(Abc_MaNodeRoot):
    CLS_geometry = None

    def _initAbcMaGeometryRoot(self, groupString):
        self._initAbcMaNodeRoot(groupString)

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

