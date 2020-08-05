# coding:utf-8
from LxGraphic import grhCfg, grhObjAbs

from . import maBscCfg, maBscMtdCore


class Abs_MaBasic(maBscCfg.MaUtility):
    pass


class Abs_MaObjLoader(
    Abs_MaBasic,
    grhObjAbs.Abs_GrhObjLoader,
):
    def _initAbsMaObjLoader(self, *args):
        self._initAbsGrhObjLoader(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_port_format_(cls, portpathString):
        _ = portpathString.split(cls.DEF_mya_node_port_pathsep)[-1]
        if _.endswith(u']'):
            return _.split(u'[')[0]
        return _

    @classmethod
    def _obj_loader_cls__get_port_is_multiple_(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            multi=1
        )

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_node_typepath_(cls, nodepathStr):
        return cls.MOD_maya_cmds.nodeType(nodepathStr)

    @classmethod
    def _obj_loader_cls__get_typepath_str_(cls, *args):
        nodepathStr = args[0]
        return cls.MOD_maya_cmds.nodeType(nodepathStr)

    @classmethod
    def _obj_loader_cls__get_fullpath_str_(cls, *args):
        nodepathStr = args[0]
        return maBscMtdCore.Mtd_MyaObj._dcc_getNodFullpathNodepathStr(nodepathStr)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_material_assign_relation_dict_(cls, *args):
        def addFnc_(dic_, geoPathStr_, mtlPathStr_):
            if geoPathStr_ not in dic_:
                dic_[geoPathStr_] = mtlPathStr_

        def branchFnc_(dic_, asnPathStr_):
            _objStrList = cls.MOD_maya_cmds.sets(asnPathStr_, query=1)
            _mtlPathStr = asnPathStr_
            if _objStrList:
                # to full path
                _objPathStrList = [j_ for _i in _objStrList for j_ in cls.MOD_maya_cmds.ls(_i, long=1)]
                for _ in _objPathStrList:
                    showType = cls.MOD_maya_cmds.ls(_, showType=1)[1]
                    if showType == u'float3':
                        _geomPathStr = _.split(u'.')[0]
                        addFnc_(dic_, _geomPathStr, _mtlPathStr)
                    else:
                        _geomPathStr = _
                        addFnc_(dic_, _geomPathStr, _mtlPathStr)

        if isinstance(args[0], (str, unicode)):
            assignPathStrList = args
        elif isinstance(args[0], (tuple, list)):
            assignPathStrList = args[0]
        else:
            raise TypeError()

        dic = {}
        [branchFnc_(dic, i) for i in assignPathStrList]
        return dic

    # **************************************************************************************************************** #
    @classmethod
    def _grh__obj_loader_cls__get_definition_node_raw_(cls, *args):
        typepathStr = args[0]
        return maBscMtdCore.Mtd_MyaObj._grh_getNodNodeRaw(
            typepathStr
        )

    @classmethod
    def _obj_loader_cls__get_definition_port_raw_(cls, *args):
        typepathString, portpathString = args
        return maBscMtdCore.Mtd_MyaObj._grh_getNodePortRaw(
            typepathString, portpathString
        )

    @classmethod
    def _obj_loader_cls__get_customize_port_raw_(cls, *args):
        pass


# ******************************************************************************************************************** #
class Abs_MaObjQueryrawCreator(grhObjAbs.Abs_GrhObjQueryrawCreator):
    def _initAbsMaObjQueryrawCreator(self, *args):
        self._initAbsGrhObjQueryBuilder(*args)

    # **************************************************************************************************************** #
    def _queryraw_loader__get_node_raw_(self, *args):
        typepathString = args[0]
        return self.CLS_grh__obj_query_creator__obj_loader.getDefinitionNodeRaw(typepathString)

    # **************************************************************************************************************** #
    def _queryraw_loader__get_port_raw_(self, *args):
        typepathString, portpathString = args
        return maBscMtdCore.Mtd_MyaObj._grh_getNodePortRaw(
            typepathString, portpathString
        )


# ******************************************************************************************************************** #
class Abs_MaObjQueue(grhObjAbs.Abs_GrhObjQueue):
    def _initAbsMayObjQueue(self, *args):
        self._initAbsGrhObjQueue(*args)


class Abs_MaConnector(grhObjAbs.Abs_GrhConnector):
    def _initAbsMaConnector(self, *args):
        self._initAbsGrhConnector(*args)


# ******************************************************************************************************************** #
class Abs_MaPort(
    Abs_MaBasic,
    grhObjAbs.Abs_GrhPort,
):
    def _initAbsMaPort(self, *args, **kwargs):
        self._initAbsGrhPort(*args, **kwargs)

    # **************************************************************************************************************** #
    def _grh__port__get_multi_indexes_(self):
        return maBscMtdCore.Mtd_MyaObj._dcc_getNodPortIndexes(
            self.path().nodepathString(), self.path().portpathString()
        )

    # **************************************************************************************************************** #
    def _inport__get_source_exist_(self, *args):
        if args:
            pass
        return maBscMtdCore.Mtd_MyaObj._dcc_getNodPortSourceExist(
            self.pathString()
        )

    def _inport__get_source_port_obj_(self):
        sourceAttrpathString = maBscMtdCore.Mtd_MyaObj._dcc_getNodPortSourceStr(self.pathString())
        if sourceAttrpathString:
            _nodepathString = maBscMtdCore.Mtd_MyaObj._dcc_getAttrpathNodepath(sourceAttrpathString)
            _portpathStr = maBscMtdCore.Mtd_MyaObj._dcc_getAttrpathPortpath(sourceAttrpathString)

            portpathStr = self.node()._nodeQueryObj._node_query__get_portpath_(_portpathStr)
            portObj = self._grh__port__get_port_cache_obj_(
                (_nodepathString,),
                (portpathStr, grhCfg.GrhPortAssignQuery.otport)
            )
            return portObj

    # **************************************************************************************************************** #
    def _otport__get_target_port_exist_(self, *args):
        if args:
            pass
        return self._otport__get_target_ports_exist_()

    # **************************************************************************************************************** #
    def _otport__get_target_ports_exist_(self):
        return maBscMtdCore.Mtd_MyaObj._dcc_getNodPortHasTargets(self.pathString())

    def _otport__get_target_port_obj_list_(self):
        lis = []

        for _attrpathString in maBscMtdCore.Mtd_MyaObj._dcc_getNodPortTargets(
                self.pathString()
        ):
            _nodepathString = maBscMtdCore.Mtd_MyaObj._dcc_getAttrpathNodepath(_attrpathString)
            _portpathStr = maBscMtdCore.Mtd_MyaObj._dcc_getAttrpathPortpath(_attrpathString)

            portpathStr = self.node()._nodeQueryObj._node_query__get_portpath_(_portpathStr)

            portObj = self._grh__port__get_port_cache_obj_(
                (_nodepathString, ),
                (portpathStr, grhCfg.GrhPortAssignQuery.inport)
            )
            if portObj is not None:
                lis.append(
                    portObj
                )
        return lis

    # **************************************************************************************************************** #
    def _grh__port__get_portraw_(self, *args, **kwargs):
        if args:
            asString = args[0]
        elif kwargs:
            asString = kwargs['asString']
        else:
            asString = True

        return maBscMtdCore.Mtd_MyaObj._grh_getNodPortraw(
            self.path().nodepathString(), self.path().portpathString(), asString=asString
        )


class Abs_MaNode(
    Abs_MaBasic,
    grhObjAbs.Abs_GrhNode,
):
    def _initAbsMaNode(self, *args, **kwargs):
        if args:
            if len(args) == 1:
                nodepathStr = args[0]
                typepathStr = self.CLS_grh__obj__loader.getNodeTypepath(nodepathStr)
                fullpathStr = self.CLS_grh__obj__loader.getFullpath(nodepathStr)
                self._initAbsGrhNode(
                    typepathStr, fullpathStr
                )
            elif len(args) == 2:
                self._initAbsGrhNode(*args, **kwargs)
            else:
                raise TypeError()
        else:
            raise TypeError()

    # **************************************************************************************************************** #
    @classmethod
    def _node_cls__get_port_raw_(cls, *args):
        pass

    # hierarchy ****************************************************************************************************** #
    def _obj__get_parent_exist_(self, *args):
        return maBscMtdCore.Mtd_MyaObj._dcc_getNodParentExist(
            self.pathString()
        )

    def _obj__get_parent_obj_(self, *args, **kwargs):
        if self._obj__get_parent_exist_() is True:
            _nodepathStr = maBscMtdCore.Mtd_MyaObj._dcc_getNodParentNodepathStr(
                self.pathString()
            )
            return self._node_cls__get_node_cache_obj_(_nodepathStr)

    def _obj__get_children_exist_(self, *args):
        return maBscMtdCore.Mtd_MyaObj._dcc_getNodChildrenExist(
            self.pathString()
        )

    def _obj__get_child_obj_list_(self, *args, **kwargs):
        def getArgsFnc_(kwargs_):
            _asString = False
            if kwargs_:
                if u'asString' in kwargs_:
                    _asString = kwargs_[u'asString']

            return _asString

        asString = getArgsFnc_(kwargs)

        if self._obj__get_children_exist_() is True:
            _nodepathStrList = maBscMtdCore.Mtd_MyaObj._dcc_getNodChildNodepathStrList(
                self.pathString()
            )
            if asString is True:
                return _nodepathStrList
            return [self._node_cls__get_node_cache_obj_(_i) for _i in _nodepathStrList]
        return []

    def _obj__get_all_child_obj_list_(self, *args, **kwargs):
        def getArgsFnc_(kwargs_):
            _asString = False
            if kwargs_:
                if u'asString' in kwargs_:
                    _asString = kwargs_[u'asString']

            return _asString

        def rcsFnc_(nodePathStr_):
            _nodepathStrList = maBscMtdCore.Mtd_MyaObj._dcc_getNodChildNodepathStrList(
                nodePathStr_
            )
            if _nodepathStrList:
                for _nodePathStr in _nodepathStrList:
                    pass

        lis = []

        asString = getArgsFnc_(kwargs)


class Abs_MaGroup(Abs_MaNode):
    def _initAbsMaGroup(self, *args, **kwargs):
        self._initAbsMaNode(*args, **kwargs)

    def groups(self):
        pass

    def nodes(self):
        pass


class Abs_MaCompnode(Abs_MaNode):
    CLS_mya_node = None

    def _initAbsMaCompnode(self, *args, **kwargs):
        nodepathStr = args[0]
        self._shapePathStr = maBscMtdCore.Mtd_MyaObj._dcc_getNodShapeNodepathStr(nodepathStr)

        self._initAbsMaNode(
            self._shapePathStr, **kwargs
        )

    def transform(self):
        return self.CLS_mya_node(
            maBscMtdCore.Mtd_MaObject._dcc_getNodTransformNodepathStr(self._shapePathStr)
        )


class Abs_MaGeometry(Abs_MaCompnode):
    def _initAbsMaGeometry(self, *args, **kwargs):
        self._initAbsMaCompnode(*args, **kwargs)

    def materials(self):
        return [
            self.CLS_mya_node(i)
            for i in maBscMtdCore.Mtd_MaObject._getNodeShadingEngineNodeStringList(
                self.pathString()
            )
        ]


class Abs_MaGeometryGroup(Abs_MaNode):
    CLS_grh__geometry = None

    def _initAbsMaGeometryGroup(self, *args, **kwargs):
        self._initAbsMaNode(*args, **kwargs)

    def meshes(self):
        return [
            self.CLS_grh__geometry(i)
            for i in maBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.pathString(),
                includeCategoryString=self.DEF_mya_type_mesh,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def nurbsSurface(self):
        return [
            self.CLS_grh__geometry(i)
            for i in maBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.pathString(),
                includeCategoryString=self.DEF_mya_type_nurbs_surface,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def nurbsCurves(self):
        return [
            self.CLS_grh__geometry(i)
            for i in maBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.pathString(),
                includeCategoryString=self.DEF_mya_type_nurbs_curve,
                useShapeCategory=True,
                withShape=False
            )
        ]

    def geometries(self):
        return [
            self.CLS_grh__geometry(i)
            for i in maBscMtdCore.Mtd_MaNodeGroup._getGroupChildNodeStringList(
                self.pathString(),
                includeCategoryString=self.DEF_mya_type_geometry_list,
                useShapeCategory=True,
                withShape=False
            )
        ]


# geometry assign **************************************************************************************************** #
class Abs_MaGeomAssign(
    Abs_MaBasic,
    grhObjAbs.Abs_GrhGeometryAssign,
):
    def _initAbsMaGeomAssign(self, *args, **kwargs):
        self._initAbsGrhGeometryAssign(*args, **kwargs)

    def _grh__geometry_assign__set_build_(self, *args):
        self._grh__geometry_assign__set_material_relation_build_(
            Abs_MaObjLoader._obj_loader_cls__get_material_assign_relation_dict_(*args)
        )
        # geometry
        self._grh__geometry_assign__set_geometry_build_(
            self._materialRelationDict.keys()
        )
        # material
        self._grh__geometry_assign__set_material_build_(
            self._materialRelationDict.values()
        )
