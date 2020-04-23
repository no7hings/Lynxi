# coding:utf-8
from LxGraphic import grhObjAbs

from . import myaBscCfg, myaBscMtdCore, maBscMethods


# ******************************************************************************************************************** #
class Abs_MyaObjQueryCache(grhObjAbs.Abs_GrhObjQueryrawCache):
    def _initAbsMyaObjQueryCache(self, *args):
        self._initAbsGrhObjQueryCache(*args)

    def _get_node_type_(self, *args):
        return self.DEF_grh_keyword_default

    # **************************************************************************************************************** #
    def _get_node_raw_(self, *args):
        categoryString = args[0]
        return {
            self.DEF_grh_key_category: categoryString,
            self.DEF_grh_key_type: self._get_node_type_(categoryString),
            self.DEF_grh_key_port: self._get_node_port_raws_(categoryString)
        }

    @classmethod
    def _get_node_port_raws_(cls, *args):
        categoryString = args[0]
        portpathStringList = myaBscMtdCore.Mtd_MyaNode._grh_getNodePortpathStringList_(
            categoryString
        )
        return myaBscMtdCore.Mtd_MyaNode._grh_getNodePortRawList(
            categoryString,
            portpathStringList
        )

    def _get_node_queryraw_obj_(self, *args):
        categoryString = args[0]

        nodeRaw = self._get_node_raw_(categoryString)
        if nodeRaw:
            return self.CLS_grh_node_queryraw(
                categoryString, nodeRaw
            )
        else:
            print categoryString

    # **************************************************************************************************************** #
    def _get_port_raw_(self, *args):
        categoryString, portpathString = args
        return myaBscMtdCore.Mtd_MyaNode._grh_getNodePortRaw(categoryString, portpathString)


# ******************************************************************************************************************** #
class Abs_MyaObjCache(grhObjAbs.Abs_GrhObjCache):
    def _initAbsMayObjCache(self, *args):
        self._initAbsGrhObjCache(*args)


class Abc_MyaBasic(myaBscCfg.Utility):
    pass


class Abs_MyaConnector(grhObjAbs.Abs_GrhConnector):
    def _initAbsMyaConnector(self, *args):
        self._initAbsGrhConnector(*args)


# ******************************************************************************************************************** #
class Abs_MyaPort(
    grhObjAbs.Abs_GrhPort,
    Abc_MyaBasic
):
    def _initAbsMyaPort(self, *args):
        self._initAbsGrhPort(*args)

    # **************************************************************************************************************** #
    def _get_indexes_(self):
        return myaBscMtdCore.Mtd_MyaNode._dcc_getNodePortIndexes(
            self.pathString()
        )

    # **************************************************************************************************************** #
    def _get_portraw_(self, *args):
        if args:
            asString = args[0]
        else:
            asString = True

        return myaBscMtdCore.Mtd_MyaNode._grh_getNodePortdata(
            self.path().nodepathString(), self.path().portpathString(), asString
        )

    # **************************************************************************************************************** #
    def _get_is_source_(self):
        return myaBscMtdCore.Mtd_MyaNode._dcc_getNodePortIsSource(
            self.pathString()
        )

    def _get_port_source_exist_(self):
        return myaBscMtdCore.Mtd_MyaNode._dcc_getNodePortHasSource(
            self.pathString()
        )

    def _get_source_(self):
        sourceAttrpathString = myaBscMtdCore.Mtd_MyaNode._dcc_getNodePortSource(
            self.pathString()
        )
        if sourceAttrpathString:
            _nodepathString = myaBscMtdCore.Mtd_MyaNode._dcc_getAttrpathNodepath(sourceAttrpathString)
            _portpathString = myaBscMtdCore.Mtd_MyaNode._dcc_getAttrpathPortpath(sourceAttrpathString)
            _nodeObject = self._get_node_cache_obj_(_nodepathString)
            return _nodeObject.port(_portpathString)

    # **************************************************************************************************************** #
    def _get_is_target_(self):
        return myaBscMtdCore.Mtd_MyaNode._dcc_getNodePortIsTarget(
            self.pathString()
        )

    def _get_targets_exist_(self):
        return myaBscMtdCore.Mtd_MyaNode._dcc_getNodePortHasTargets(
            self.pathString()
        )

    def _get_targets_(self):
        lis = []

        for _attrpathString in myaBscMtdCore.Mtd_MyaNode._dcc_getNodePortTargets(
                self.pathString()
        ):
            _nodepathString = myaBscMtdCore.Mtd_MyaNode._dcc_getAttrpathNodepath(_attrpathString)
            _portpathString = myaBscMtdCore.Mtd_MyaNode._dcc_getAttrpathPortpath(_attrpathString)

            _portObject = self._get_port_cache_obj_(
                    _nodepathString,
                    _portpathString
                )
            if _portObject is not None:
                lis.append(
                    _portObject
                )
        return lis


class Abs_MyaNode(
    grhObjAbs.Abs_GrhNode,
    Abc_MyaBasic
):
    def _initAbsMyaNode(self, *args):
        nodepathString = args[0]
        categoryString = maBscMethods.Node.category(nodepathString)

        self._initAbsGrhNode(
            categoryString,
            maBscMethods.Node.toFullpathName(nodepathString),
        )

    def _get_parent_(self):
        return self.__class__(
            myaBscMtdCore.Mtd_MaDag._getDagParentString(
                self.pathString()
            )
        )

    def _get_children_(self):
        return [
            self.__class__(i)
            for i in myaBscMtdCore.Mtd_MaDag._getDagChildStringList(
                self.pathString()
            )
        ]


class Abc_MyaGroup(Abs_MyaNode):
    def _initAbcMyaGroup(self, nodepathString):
        self._initAbsMyaNode(nodepathString)

    def groups(self):
        pass

    def nodes(self):
        pass


class Abc_MyaCompnode(Abs_MyaNode):
    CLS_mya_node = None

    def _initAbcMyaCompnode(self, nodepathString):
        self._initAbsMyaNode(
            maBscMethods.Node.shapeName(nodepathString)
        )
        self._pathString = maBscMethods.Node.shapeName(nodepathString)

    def transform(self):
        return self.CLS_mya_node(
            maBscMethods.Node.transformName(self._pathString)
        )


class Abc_MyaGeometry(Abc_MyaCompnode):
    def _initAbcMyaGeometry(self, nodepathString):
        self._initAbcMyaCompnode(nodepathString)

    def materials(self):
        return [
            self.CLS_mya_node(i)
            for i in myaBscMtdCore.Mtd_MaObject._getNodeShadingEngineNodeStringList(
                self.pathString()
            )
        ]


class Abc_MyaGeometryGroup(Abs_MyaNode):
    CLS_grh_geometry = None

    def _initAbcMyaGeometryGroup(self, groupString):
        self._initAbsMyaNode(groupString)

    def meshes(self):
        return [
            self.CLS_grh_geometry(i)
            for i in myaBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.pathString(),
                includeCategoryString=self.DEF_mya_type_mesh,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def nurbsSurface(self):
        return [
            self.CLS_grh_geometry(i)
            for i in myaBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.pathString(),
                includeCategoryString=self.DEF_mya_type_nurbs_surface,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def nurbsCurves(self):
        return [
            self.CLS_grh_geometry(i)
            for i in myaBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.pathString(),
                includeCategoryString=self.DEF_mya_type_nurbs_curve,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def geometries(self):
        return [
            self.CLS_grh_geometry(i)
            for i in myaBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.pathString(),
                includeCategoryString=self.DEF_mya_type_geometry_list,
                useShapeCategory=True,
                withShape=False
            )
        ]
