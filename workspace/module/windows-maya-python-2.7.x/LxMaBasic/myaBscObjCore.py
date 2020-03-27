# coding:utf-8
from LxBasic import bscObjCore, bscMethods

from LxGraphic import grhObjCore

from LxMaBasic import myaBscConfigure, myaBscMtdCore, maBscMethods


class Abc_MyaQueryCache(myaBscConfigure.Utility):
    def _initAbcMyaQueryCache(self):
        self._objectPortStringsDict = {}
        self._objectPortQueryDict = {}
        self._objectPortkeyStringQueryDict = {}

    def _getPortkeyStrings_(self, categoryString, nodepathString):
        dic = self._objectPortStringsDict
        if categoryString in dic:
            return dic[categoryString]
        _ = myaBscMtdCore.Mtd_MaObjectPort._mtl_getObjectPortkeyStringList(nodepathString)
        dic[categoryString] = _
        return _

    def _getQueryFnc_(self, categoryString, nodepathString, dic, fnc):
        if categoryString in dic:
            return dic[categoryString]

        portkeyStringList = self._getPortkeyStrings_(categoryString, nodepathString)

        _ = fnc(
            nodepathString,
            portkeyStringList
        )
        dic[categoryString] = _
        return _

    def _getObjectPortDefQuery_(self, categoryString, nodepathString):
        return self._getQueryFnc_(
            categoryString,
            nodepathString,
            self._objectPortQueryDict,
            myaBscMtdCore.Mtd_MaObjectPort._mtl_getObjectPortDefDict
        )

    def _getObjectPortPortkeyQuery_(self, categoryString, nodepathString):
        return self._getQueryFnc_(
            categoryString,
            nodepathString,
            self._objectPortkeyStringQueryDict,
            myaBscMtdCore.Mtd_MaObjectPort._mtl_getObjectPortkeyStringDict
        )


class Abc_MyaObjCache(myaBscConfigure.Utility):
    pass


class Def_MyaQueryObj(object):
    def _initDefMyaQueryObj(self, keyString):
        self._defQueryKeyString = keyString

    def _myaQueryObjKeyString_(self):
        return self._defQueryKeyString


class Abc_MyaNodeString(bscObjCore.Abc_BscDccNodeString):
    def _initAbcMyaNodeString(self, nodepathString):
        self._initAbcBscDccNodeString(nodepathString)


class Abc_MyaPortString(bscObjCore.Abc_BscDccPortString):
    def _initAbcMyaPortString(self, nodepathString):
        self._initAbcBscDccPortString(nodepathString)


class Abc_MyaBasic(myaBscConfigure.Utility):
    pass


class Abs_MyaObjSet(grhObjCore.Abs_GrhObjSet):
    def _initAbsMyaObjSet(self, *args):
        self._initAbsGrhObjSet(*args)


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
    CLS_grh_portpath = None

    def __init__(self, *args):
        pass

    def _initAbcMyaPort(self, nodeObject, portpathString):
        self._nodeObj = nodeObject

        self._portpathObj = self.CLS_grh_portpath(portpathString)

        self._porttypeString = None

        self._parentPortpathStr = None
        self._childPortpathStrList = []

        self._isArray = False

    def _set_porttype_(self, porttypeString):
        self._porttypeString = porttypeString

    def _set_parent_(self, portnameString):
        self._parentPortpathStr = portnameString

    def _set_children_(self, portpathStrings):
        self._childPortpathStrList = portpathStrings

    def _set_array_(self, boolean):
        self._isArray = boolean

    def _get_node_obj_(self, nodepathString):
        return self._nodeObj.__class__(nodepathString)

    def _get_port_obj_(self, nodepathString, portpathString):
        if isinstance(nodepathString, (str, unicode)):
            nodeObject = self._nodeObj.__class__(nodepathString)
        else:
            nodeObject = nodepathString
        return nodeObject.port(portpathString)

    def node(self):
        return self._nodeObj

    def attrpathString(self):
        return bscMethods.MaAttributeString.composeBy(
            self._nodeObj.nodepathString(),
            self.portpathString()
        )

    def portpathString(self):
        return self._portpathObj.portpathString()

    def portname(self):
        return self._portpathObj.portname()

    def portdata(self, asString=True):
        nodepathString = self.node().nodepathString()
        portpathString = self.portpathString()
        return myaBscMtdCore.Mtd_MaObjectPort._mtl_getObjectPortdata(
            nodepathString, portpathString, asString
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

    def indexes(self):
        return maBscMethods.Attribute.indexes(self.attrpathString())

    def nicename(self):
        return maBscMethods.Attribute.nicename(self.attrpathString())

    def hasParent(self):
        return self._parentPortpathStr is not None

    def parent(self):
        if self.hasParent():
            return self._nodeObj.port(self._parentPortpathStr)

    def hasChildren(self):
        return self._childPortpathStrList != []

    def children(self):
        if self.hasChildren():
            return [
                self._nodeObj.port(i) for i in self._childPortpathStrList
            ]
        return []

    def child(self, portnameString):
        if self.hasChildren():
            return self._nodeObj.port(portnameString)

    def hasChild(self, portnameString):
        return portnameString in self._childPortpathStrList

    def hasSource(self):
        return maBscMethods.Attribute.hasSource(self.attrpathString())

    def isSource(self):
        return maBscMethods.Attribute.isSource(self.attrpathString())

    def source(self):
        portpathString = self.attrpathString()
        if maBscMethods.Attribute.isAppExist(portpathString):
            maBscMethods.Attribute.source(portpathString)
            _attrpathString = maBscMethods.Attribute.source(portpathString)
            if _attrpathString:
                sourceNodeString = maBscMethods.Attribute.nodepathString(_attrpathString)
                sourcePortString = maBscMethods.Attribute.portpathString(_attrpathString)
                sourceNodeObject = self._get_node_obj_(sourceNodeString)
                return sourceNodeObject.port(sourcePortString)

    def hasTargets(self):
        return maBscMethods.Attribute.hasTargets(self.attrpathString())

    def isTarget(self):
        return maBscMethods.Attribute.isTarget(self.attrpathString())

    def targets(self):
        lis = []
        for attrpathString in maBscMethods.Attribute.targets(self.attrpathString()):
            lis.append(
                self._get_port_obj_(
                    maBscMethods.Attribute.nodepathString(attrpathString),
                    maBscMethods.Attribute.portpathString(attrpathString)
                )
            )
        return lis

    def portgiven(self):
        if self.hasSource() is True:
            return self.source()
        return self.portdata()

    def __str__(self):
        return u'{}(portpathString="{}", porttype="{}", node="{}")'.format(
            self.__class__.__name__,
            self.portpathString(),
            self.porttype(),
            self.node().nodepathString()
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
        return 'connection(source="{}", target="{}")'.format(self.source().attrpathString(), self.target().attrpathString())

    def __repr__(self):
        return self.__str__()


# object ************************************************************************************************************* #
class Abc_MyaObject(
    Abc_MyaBasic,
    Def_MyaQueryObj
):
    CLS_mya_node_string = None
    CLS_mya_port = None

    CLS_mya_port_set = None

    OBJ_mya_query_cache = None

    def __init__(self, *args):
        pass

    def _initAbcMyaObject(self, nodepathString):
        assert maBscMethods.Node.isExist(nodepathString), u'{} is Non-Exist'.format(nodepathString)
        self._nodepathObj = self.CLS_mya_node_string(
            nodepathString
        )

        self._categoryString = maBscMethods.Node.category(self.nodepathString())

        self._initDefMyaQueryObj(self._categoryString)

        self._portDefDict = self.OBJ_mya_query_cache._getObjectPortDefQuery_(
            self._categoryString,
            self.nodepathString()
        )
        self._portkeyStrDict = self.OBJ_mya_query_cache._getObjectPortPortkeyQuery_(
            self._categoryString,
            self.nodepathString()
        )

        self._portSetObj = self.CLS_mya_port_set()
        self._inputSetObj = self.CLS_mya_port_set()
        self._outputSetObj = self.CLS_mya_port_set()

        self._set_build_ports_()

    def _get_portkey_(self, portnameString):
        if portnameString in self._portkeyStrDict:
            return self._portkeyStrDict[portnameString]
        return portnameString

    def _set_build_ports_(self):
        def addPortFnc_(portString_, portDef_, portCls_):
            _assignString = portDef_[self.DEF_mya_key_assign]
            _porttypeString = portDef_[self.DEF_mya_key_porttype]
            _parentPortpathStr = portDef_[self.DEF_mya_key_parent]
            _childPortnameStrings = portDef_[self.DEF_mya_key_children]
            _isArray = portDef_[self.DEF_mya_key_array]

            _portObject = portCls_(self, portString_)
            _portObject._set_porttype_(_porttypeString)
            if _assignString == self.DEF_mya_keyword_input:
                self._inputSetObj._set_add_obj_(portString_, _portObject)
            elif _assignString == self.DEF_mya_keyword_output:
                self._outputSetObj._set_add_obj_(portString_, _portObject)

            _portObject._set_parent_(_parentPortpathStr)
            _portObject._set_children_(_childPortnameStrings)
            _portObject._set_array_(_isArray)

            self._portSetObj._set_add_obj_(portString_, _portObject)

        for k, v in self._portDefDict.items():
            addPortFnc_(k, v, self.CLS_mya_port)

    def nodepathString(self):
        return self._nodepathObj.nodepathString()

    def name(self):
        return self._nodepathObj.name()

    def category(self):
        return self._categoryString

    def isExist(self):
        return maBscMethods.Node.isExist(self.nodepathString())

    def ports(self):
        return self._portSetObj.objects()

    def hasPort(self, portpathString):
        return self._portSetObj._get_has_obj_(portpathString)

    def port(self, portpathString):
        portkeyString = self._get_portkey_(portpathString)
        assert self._portSetObj._get_has_obj_(portkeyString) is True, u'''node "{}" do not has port "{}".'''.format(
            self._categoryString, portkeyString
        )
        return self._portSetObj._get_object_(
            portkeyString
        )

    def inputs(self):
        return self._inputSetObj.objects()

    def hasInput(self, portpathString):
        return self._inputSetObj._get_has_obj_(portpathString)

    def input(self, portpathString):
        portkeyString = self._get_portkey_(portpathString)
        assert self._inputSetObj._get_has_obj_(portkeyString) is True, u'''node "{}" do not has input "{}".'''.format(
            self._categoryString, portkeyString
        )
        return self._inputSetObj._get_object_(
            portkeyString
        )

    def outputs(self):
        return self._outputSetObj.objects()

    def hasOutput(self, portpathString):
        return self._outputSetObj._get_has_obj_(portpathString)

    def output(self, portpathString):
        portkeyString = self._get_portkey_(portpathString)
        assert self._outputSetObj._get_has_obj_(portkeyString) is True, u'''node "{}" do not has output "{}".'''.format(
            self._categoryString, portkeyString
        )
        return self._outputSetObj._get_object_(
            portkeyString
        )

    def allSourceNodes(self, categoryString=None):
        return [
            self.__class__(i)
            for i in myaBscMtdCore.Mtd_MaObject._getNodeAllSourceNodeStringList(
                self.nodepathString(), includeCategoryString=categoryString
            )
        ]

    def targetNodes(self, categoryString=None):
        return [
            self.__class__(i)
            for i in myaBscMtdCore.Mtd_MaObject._getNodeTargetNodeStringList(
                self.nodepathString(), includeCategoryString=categoryString
            )
        ]

    def allTargetNodes(self, categoryString=None):
        return [
            self.__class__(i)
            for i in myaBscMtdCore.Mtd_MaObject._getNodeAllTargetNodeStringList(
                self.nodepathString(), includeCategoryString=categoryString
            )
        ]

    def __str__(self):
        return u'{}(name="{}", category="{}")'.format(
            self.__class__.__name__,
            self.name(),
            self.category()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaNode(Abc_MyaObject):
    def __init__(self, *args):
        pass

    def _initAbcMyaNode(self, nodepathString):
        self._initAbcMyaObject(nodepathString)


class Abc_MyaDag(Abc_MyaObject):
    CLS_mya_dag = None
    CLS_mya_node = None

    def _initAbcMyaDag(self, nodepathString):
        assert maBscMethods.Node.isExist(nodepathString), u'{} is Non-Exist'.format(nodepathString)
        # Convert to fullpath
        self._initAbcMyaObject(
            maBscMethods.Node.toFullpathName(nodepathString)
        )

    def parent(self):
        return self.CLS_mya_dag(
            myaBscMtdCore.Mtd_MaDag._getDagParentString(self.nodepathString())
        )

    def children(self):
        return [
            self.CLS_mya_dag(i)
            for i in myaBscMtdCore.Mtd_MaDag._getDagChildStringList(self.nodepathString())
        ]

    def __str__(self):
        return u'{}(nodepathString="{}", category="{}")'.format(
            self.__class__.__name__,
            self.nodepathString(),
            self.category()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaTransform(Abc_MyaDag):
    def _initAbcMyaTransform(self, nodepathString):
        self._initAbcMyaDag(nodepathString)

    def shape(self):
        return self.CLS_mya_dag(
            maBscMethods.Node.shapeName(self.nodepathString())
        )

    def shapes(self):
        return [
            self.CLS_mya_dag(i)
            for i in myaBscMtdCore.Mtd_MaObject._getNodeShapeNodeStringList(self.nodepathString())
        ]


class Abc_MyaCompDag(Abc_MyaDag):
    CLS_mya_transform = None

    def _initAbcMyaCompDag(self, nodepathString):
        # Convert to transform fullpath
        shapeNodepathString = maBscMethods.Node.shapeName(nodepathString)

        self._initAbcMyaDag(shapeNodepathString)

    def transform(self):
        return self.CLS_mya_transform(
            maBscMethods.Node.transformName(self.nodepathString())
        )

    def __str__(self):
        return u'{}(nodepathString="{}", category="{}")'.format(
            self.__class__.__name__,
            self.nodepathString(),
            self.category()
        )

    def __repr__(self):
        return self.__str__()


class Abc_MyaGeometry(Abc_MyaCompDag):
    CLS_mya_node = None

    def _initAbcMyaGeometry(self, nodepathString):
        self._initAbcMyaCompDag(nodepathString)

    def materials(self):
        return [
            self.CLS_mya_node(i)
            for i in myaBscMtdCore.Mtd_MaObject._getNodeShadingEngineNodeStringList(self.nodepathString())
        ]


class Abc_MyaGroup(Abc_MyaDag):
    def _initAbcMyaGroup(self, nodepathString):
        self._initAbcMyaDag(nodepathString)

    def __str__(self):
        return u'{}(nodepathString="{}")'.format(
            self.__class__.__name__,
            self.nodepathString(),
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
            for i in myaBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.root().nodepathString(),
                includeCategoryString=self.DEF_mya_type_mesh,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def nurbsSurface(self):
        return [
            self.CLS_geometry(i)
            for i in myaBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.root().nodepathString(),
                includeCategoryString=self.DEF_mya_type_nurbs_surface,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def nurbsCurves(self):
        return [
            self.CLS_geometry(i)
            for i in myaBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.root().nodepathString(),
                includeCategoryString=self.DEF_mya_type_nurbs_curve,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def geometries(self):
        return [
            self.CLS_geometry(i)
            for i in myaBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.root().nodepathString(),
                includeCategoryString=self.DEF_mya_type_geometry_list,
                useShapeCategory=True,
                withShape=False
            )
        ]


# ******************************************************************************************************************** #
class Abs_MyaPort(grhObjCore.Abs_GrhPort):
    def _initAbsMyaPort(self, *args):
        self._initAbsGrhPort(*args)

    def _get_is_source_(self):
        return maBscMethods.Attribute.isSource(self.attrpathString())

    def _get_has_source(self):
        return maBscMethods.Attribute.hasSource(self.attrpathString())

    def _get_source_(self):
        portpathString = self.attrpathString()
        if maBscMethods.Attribute.isAppExist(portpathString):
            maBscMethods.Attribute.source(portpathString)
            _attrpathString = maBscMethods.Attribute.source(portpathString)
            if _attrpathString:
                _nodepathString = maBscMethods.Attribute.nodepathString(_attrpathString)
                _portpathString = maBscMethods.Attribute.portpathString(_attrpathString)
                _portkeyString = self._nodeObj._get_portkey_(_portpathString)
                _nodeObject = self._get_node_obj_(_nodepathString)
                return _nodeObject.port(_portkeyString)

    def _get_is_target_(self):
        return maBscMethods.Attribute.isTarget(self.attrpathString())

    def _get_has_targets_(self):
        return maBscMethods.Attribute.hasTargets(self.attrpathString())

    def _get_targets_(self):
        lis = []
        for _attrpathString in maBscMethods.Attribute.targets(self.attrpathString()):
            _nodepathString = maBscMethods.Attribute.nodepathString(_attrpathString)
            _portpathString = maBscMethods.Attribute.portpathString(_attrpathString)
            _portkeyString = self._nodeObj._get_portkey_(_portpathString)
            _portObject = self._get_port_obj_(
                    _nodepathString,
                    _portkeyString
                )
            if _portObject is not None:
                lis.append(
                    _portObject
                )
        return lis

    def _get_target_(self, *args):
        pass


class Abs_MyaNode(grhObjCore.Abs_GrhNode):
    def _initAbsMyaNode(self, *args):
        nodepathString = args[0]
        categoryString = maBscMethods.Node.category(nodepathString)

        self._initAbsGrhNode(categoryString, nodepathString)

        self._portDefDict = self.OBJ_grh_query_cache._getObjectPortDefQuery_(
            categoryString,
            nodepathString
        )

        self._portkeyStrDict = self.OBJ_grh_query_cache._getObjectPortPortkeyQuery_(
            categoryString,
            nodepathString
        )

        self._set_build_ports_()

    def _set_build_ports_(self):
        def addPortFnc_(portString_, portDef_, portCls_):
            _assignString = portDef_[self.DEF_grh_key_assign]
            _porttypeString = portDef_[self.DEF_grh_key_porttype]
            _parentPortpathStr = portDef_[self.DEF_grh_key_parent]
            _childPortnameStrings = portDef_[self.DEF_grh_key_children]

            _portObject = portCls_(self, portString_)
            _portObject._set_porttype_(_porttypeString)
            if _assignString == self.DEF_grh_keyword_input:
                self._inputSetObj._set_add_obj_(portString_, _portObject)
            elif _assignString == self.DEF_grh_keyword_output:
                self._outputSetObj._set_add_obj_(portString_, _portObject)

            _portObject._set_parent_(_parentPortpathStr)
            _portObject._set_children_(_childPortnameStrings)

            self._portSetObj._set_add_obj_(portString_, _portObject)

        for k, v in self._portDefDict.items():
            addPortFnc_(k, v, self.CLS_grh_port)

    def _get_portkey_(self, portnameString):
        if portnameString in self._portkeyStrDict:
            return self._portkeyStrDict[portnameString]
        return portnameString
