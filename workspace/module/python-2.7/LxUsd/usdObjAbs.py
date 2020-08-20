# coding:utf-8
from LxGraphic import grhCfg, grhObjAbs

from . import usdCfg


class AbsUsdBasic(usdCfg.UsdUtility):
    pass


# ******************************************************************************************************************** #
class AbsUsdObjSceneLoader(
    AbsUsdBasic,
    grhObjAbs.AbsGrhObjSceneLoader
):
    def _initAbsUsdObjScene(self, *args, **kwargs):
        self._initAbsGrhObjScene(*args, **kwargs)

    def _obj_scene_loader__set_build_(self, *args, **kwargs):
        if args:
            _ = args[0]
            if isinstance(_, self.MOD_pxr_Usd.Stage):
                stageObj = _
            elif isinstance(_, (str, unicode)):
                stageFileStr = _
                stageObj = self.MOD_pxr_Usd.Stage.Open(stageFileStr)
            else:
                if _.__class__.__name__ == 'Stage':
                    stageObj = _
                else:
                    raise TypeError()

            self._usdStageObj = stageObj

    def _obj_scene_loader__get_node_obj_(self, *args):
        nodepathStr = args[0]
        return self._usdStageObj.GetPrimAtPath(nodepathStr)

    def _obj_scene_loader__get_node_root_obj_(self):
        return self._obj_scene_loader__get_node_obj_(
            self.DEF_usd__node_pathsep
        )

    def _obj_scene_loader__get_all_node_obj_list_(self, **kwargs):
        return list(
            self.MOD_pxr_Usd.PrimRange.AllPrims(
                self._obj_scene_loader__get_node_root_obj_()
            )
        )


# ******************************************************************************************************************** #
class AbsUsdObjLoader(
    AbsUsdBasic,
    grhObjAbs.AbsGrhObjLoader,
):
    # noinspection PyUnusedLocal
    def _initAbsUsdObjLoader(self, *args):
        self._initAbsGrhObjLoader(*args)

    # class method *************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_obj_scene_obj_(cls):
        return cls.CALL_grh__obj_loader__get_obj_scene.__dict__[u'GRH_OBJ_SCENE_LOADER']

    @classmethod
    def _obj_loader_cls__get_obj_exist_(cls, *args):
        _ = args[0]
        if isinstance(args[0], cls.MOD_pxr_Usd.Prim):
            n = args[0]
        elif isinstance(args[0], (str, unicode)):
            n = cls.getScene().getNode(_)
        else:
            raise TypeError()
        return n.IsValid()

    @classmethod
    def _obj_loader_cls__get_port_datatype_(cls, *args):
        p = args[0]
        if isinstance(p, cls.MOD_pxr_Usd.Attribute):
            _datatypeStr = p.GetTypeName().aliasesAsStrings[0]
            if _datatypeStr in cls.DEF_usd__datatype_dict:
                return cls.DEF_usd__datatype_dict[_datatypeStr]
            return _datatypeStr
        elif isinstance(p, cls.MOD_pxr_Usd.Relationship):
            return u'assign'

    @classmethod
    def _grh__obj_loader_cls__get_port_source_exist_(cls, *args):
        p = cls.getNodePort(*args)
        # port
        if isinstance(p, cls.MOD_pxr_Usd.Attribute):
            return p.GetConnections() != []
        # binding
        # elif isinstance(p, cls.MOD_pxr_Usd.Relationship):
        #     return p.GetTargets() != []
        return False

    @classmethod
    def _obj_loader_cls__get_port_source_str_(cls, *args):
        p = cls.getNodePort(*args)
        # inport
        if isinstance(p, cls.MOD_pxr_Usd.Attribute):
            ps = p.GetConnections()
            if ps:
                return ps[0].pathString
        # asport
        # elif isinstance(p, cls.MOD_pxr_Usd.Relationship):
        #     ns = p.GetTargets()
        #     p.GetNamespace()
        #     if ns:
        #         return cls.DEF_usd__node_port_pathsep.join(
        #             [ns[0].pathString, p.GetNamespace()]
        #         )

    @classmethod
    def _obj_loader_cls__get_inport_portraw_(cls, *args, **kwargs):
        if kwargs:
            pass
        p = cls.getNodePort(*args)
        if isinstance(p, cls.MOD_pxr_Usd.Attribute):
            _ = p.Get()
            if _ is not None:
                if isinstance(_, cls.MOD_pxr_Sdf.AssetPath):
                    return _.path
                if isinstance(_, (int, float, bool, str, unicode, tuple, list)):
                    return _
                return list(_)
        elif isinstance(p, cls.MOD_pxr_Usd.Relationship):
            return [i.pathString for i in p.GetTargets()]

    @classmethod
    def _obj_loader_cls__get_asport_assignment_str_list_(cls, *args, **kwargs):
        if kwargs:
            pass
        p = cls.getNodePort(*args)
        if isinstance(p, cls.MOD_pxr_Usd.Relationship):
            return [i.pathString for i in p.GetTargets()]
        return []

    # **************************************************************************************************************** #
    @classmethod
    def _grh__obj_loader_cls__get_definition_node_raw_(cls, *args):
        typepathStr = args[0]
        return {
            cls.DEF_grh__key_node_typepath: typepathStr,
            cls.DEF_grh__key_node_datatype: None,
            cls.DEF_grh__key_port: []
        }

    @classmethod
    def _obj_loader_cls__get_port_assign_str_(cls, *args):
        pass

    @classmethod
    def _obj_loader_cls__get_customize_port_raw_(cls, *args):
        if len(args) == 2:
            nodepathStr, portpathStr = args
            objSceneObj = cls.getScene()
            n = objSceneObj.getNode(nodepathStr)
            p = n.GetProperty(portpathStr)
        elif len(args) == 1:
            p = args[0]
        else:
            raise TypeError()

        portpathStr = p.GetName()
        portNamespaceStr = p.GetNamespace()
        # material
        assignStrDict_0 = {
            u'outputs:arnold:surface': cls.DEF_grh__keyword__gnport,
            u'outputs:arnold:displacement': cls.DEF_grh__keyword__gnport,
            u'outputs:arnold:volume': cls.DEF_grh__keyword__gnport,
            u'outputs:surface': cls.DEF_grh__keyword__gnport,
            u'outputs:displacement': cls.DEF_grh__keyword__gnport,
            u'outputs:volume': cls.DEF_grh__keyword__gnport,
            # material assign
            u'material:binding': cls.DEF_grh__keyword__asport
        }
        # node
        assignStrDict_1 = {
            u'inputs': cls.DEF_grh__keyword__inport,
            u'outputs': cls.DEF_grh__keyword__otport
        }
        # geometry render attribute
        assignStrDict_2 = {
            u'primvars:arnold': cls.DEF_grh__keyword__property,
            u'primvars:arnold:visibility': cls.DEF_grh__keyword__visibility
        }
        if portpathStr in assignStrDict_0:
            assignStr = assignStrDict_0[portpathStr]
        elif portNamespaceStr in assignStrDict_1:
            assignStr = assignStrDict_1[portNamespaceStr]
        elif portNamespaceStr in assignStrDict_2:
            assignStr = assignStrDict_2[portNamespaceStr]
        else:
            assignStr = cls.DEF_grh__keyword__inport

        datatypeStr = cls._obj_loader_cls__get_port_datatype_(p)

        return cls._obj_loader_cls__get_port_raw_(
            portpath=portpathStr,
            porttype=datatypeStr,
            datatype=datatypeStr,
            assign=assignStr
        )

    @classmethod
    def _grh__obj_loader_cls__get_customize_port_raw_list_(cls, *args):
        nodepathStr = args[0]

        lis = []
        objSceneObj = cls.getScene()
        n = objSceneObj.getNode(nodepathStr)
        ps = n.GetProperties()
        for p in ps:
            portRawDict = cls._obj_loader_cls__get_customize_port_raw_(p)
            if portRawDict:
                lis.append(portRawDict)
        return lis

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_type_str_(cls, *args):
        _ = args[0]
        if isinstance(args[0], cls.MOD_pxr_Usd.Prim):
            n = args[0]
        elif isinstance(args[0], (str, unicode)):
            n = cls.getScene().getNode(_)
        else:
            raise TypeError()
        return n.GetTypeName()

    @classmethod
    def _obj_loader_cls__get_typepath_str_(cls, *args):
        nodepathStr = args[0]

        sep = cls.DEF_usd__node_pathsep
        objSceneObj = cls.getScene()
        n = objSceneObj.getNode(nodepathStr)
        lis = [n.GetTypeName()]
        metadata = n.GetAllMetadata()
        if u'kind' in metadata:
            lis.append(metadata[u'kind'])
        if n.HasProperty(u'info:id'):
            p = n.GetProperty(u'info:id')
            lis.append(p.Get())
        return sep.join(lis)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_port_obj_(cls, *args):
        nodepathStr, portpathStr = args
        objSceneObj = cls.getScene()
        n = objSceneObj.getNode(nodepathStr)
        return n.GetProperty(portpathStr)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_node_parent_exist_(cls, *args):
        objSceneObj = cls.getScene()
        n = objSceneObj.getNode(*args)
        return n.GetParent().IsValid()

    @classmethod
    def _obj_loader_cls__get_node_parent_str_(cls, *args):
        objSceneObj = cls.getScene()
        n = objSceneObj.getNode(*args)
        p = n.GetParent()
        if p.IsValid():
            return p.GetPath().pathString

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_node_children_exist_(cls, *args, **kwargs):
        objSceneObj = cls.getScene()
        n = objSceneObj.getNode(*args)
        # debug
        return n.GetChildren() != []

    @classmethod
    def _obj_loader_cls__get_node_child_str_list_(cls, *args, **kwargs):
        nodepathStr = args[0]
        objSceneObj = cls.getScene()
        n = objSceneObj.getNode(nodepathStr)
        ns = n.GetChildren()
        return [i.GetPath().pathString for i in cls._obj_loader_cls__set_node_filter_(ns, **kwargs)]

    @classmethod
    def _obj_loader_cls__get_node_all_child_str_list_(cls, *args, **kwargs):
        nodepathStr = args[0]
        objSceneObj = cls.getScene()
        ns = list(
            cls.MOD_pxr_Usd.PrimRange.AllPrims(
                objSceneObj.getNode(nodepathStr)
            )
        )[1:]
        return [i.GetPath().pathString for i in cls._obj_loader_cls__set_node_filter_(ns, **kwargs)]

    # compnode ******************************************************************************************************* #
    @classmethod
    def _obj_loader_cls__get_node_is_compnode_(cls, *args):
        nodepathStr = args[0]
        if cls.getNodeType(nodepathStr) == cls.VAR_grh__obj_loader__node_type__transform:
            if cls.getNodeHasChildren(nodepathStr) is True:
                childStrList = cls.getNodeChildPaths(nodepathStr)
                if len(childStrList) == 1:
                    if cls.getNodeType(childStrList[0]) != cls.VAR_grh__obj_loader__node_type__transform:
                        return True
                    return False
                return False
            return False
        return False

    @classmethod
    def _obj_loader_cls__get_node_is_transform_(cls, *args):
        nodepathStr = args[0]
        return cls.getNodeType(nodepathStr) == cls.VAR_grh__obj_loader__node_type__transform

    @classmethod
    def _obj_loader_cls__get_node_is_shape_(cls, *args):
        nodepathStr = args[0]
        if cls.getNodeType(nodepathStr) != cls.VAR_grh__obj_loader__node_type__transform:
            parentPathStr = cls.getNodeParentPath(nodepathStr)
            if cls.getNodeType(parentPathStr) == cls.VAR_grh__obj_loader__node_type__transform:
                if cls.getNodeHasChildren(nodepathStr) is False:
                    return True
                return False
        return False


# ******************************************************************************************************************** #
class AbsUsdObjQueryrawCreator(grhObjAbs.AbsGrhObjQueryrawCreator):
    def _initAbsUsdObjQueryrawCreator(self, *args):
        self._initAbsGrhObjQueryBuilder(*args)

    # **************************************************************************************************************** #
    def _queryraw_loader__get_node_raw_(self, *args):
        return self.CLS_grh__obj_query_creator__obj_loader.getDefinitionNodeRaw(*args)


# ******************************************************************************************************************** #
class AbsUsdObjQueue(grhObjAbs.AbsGrhObjQueue):
    def _initAbsUsdObjQueue(self, *args):
        self._initAbsGrhObjQueue(*args)


# ******************************************************************************************************************** #
class AbsUsdConnector(grhObjAbs.AbsGrhConnector):
    def _initAbsUsdConnector(self, *args):
        self._initAbsGrhConnector(*args)


# ******************************************************************************************************************** #
class AbsUsdPort(grhObjAbs.AbsGrhPort):
    def _initAbsUsdPort(self, *args):
        self._initAbsGrhPort(*args)

    # **************************************************************************************************************** #
    def _inport__get_source_exist_(self, *args):
        if grhCfg.GrhPortAssignQuery.isInport(self.assignString()):
            return self.CLS_grh__obj__loader._grh__obj_loader_cls__get_port_source_exist_(
                self.path().nodepathString(), self.path().portpathString()
            )
        return False

    def _inport__get_source_port_obj_(self, *args):
        if self._inport__get_source_exist_() is True:
            attrpathStr = self.CLS_grh__obj__loader._obj_loader_cls__get_port_source_str_(
                self.path().nodepathString(), self.path().portpathString()
            )
            # covert to attribute object
            _attrPathObj = self.CLS_grh__obj__path(attrpathStr)
            _nodepathStr, _portpathStr = _attrPathObj.nodepathString(), _attrPathObj.portpathString()
            # print _attrPathObj
            # print _nodepathStr, _portpathStr, "A"
            portObj = self._grh__port__get_port_cache_obj_(
                (_nodepathStr,),
                # source: otport > target: inport
                (_portpathStr, grhCfg.GrhPortAssignQuery.otport)
            )
            return portObj

    # **************************************************************************************************************** #
    def _grh__port__get_portraw_(self, *args, **kwargs):
        return self.CLS_grh__obj__loader._obj_loader_cls__get_inport_portraw_(
            self.path().nodepathString(), self.path().portpathString(),
            *args, **kwargs
        )

    # **************************************************************************************************************** #
    def _asport__get_assignment_node_obj_list_(self, *args, **kwargs):
        if self.isAsport():
            return self.CLS_grh__obj__loader._obj_loader_cls__get_asport_assignment_str_list_(
                self.path().nodepathString(), self.path().portpathString(),
                *args, **kwargs
            )
        return []


class AbsUsdNode(grhObjAbs.AbsGrhNode):
    def _initAbsUsdNode(self, *args, **kwargs):
        if args:
            # nodepath
            if len(args) == 1:
                _ = args[0]
                if self.CLS_grh__obj__loader.getNodeIsExist(_) is True:
                    typepathStr = self.CLS_grh__obj__loader.getNodeTypepath(_)
                    nodepathStr = _
                else:
                    raise TypeError()
            # ( category, nodepath )
            elif len(args) == 2:
                typepathStr, nodepathStr = args
                self._initAbsGrhNode(*args)
            else:
                raise TypeError()

            # initialization
            self._initAbsGrhNode(typepathStr, nodepathStr, **kwargs)
            # add custom port
            portRawList = self.CLS_grh__obj__loader.getCustomizePortRaws(nodepathStr)
            [self._grh_node__set_customize_port_obj_create_(i) for i in portRawList]
        else:
            raise TypeError()

    # hierarchy ****************************************************************************************************** #
    def _obj__get_parent_exist_(self, *args):
        return self.CLS_grh__obj__loader.getNodeHasParent(
                self.pathString()
            )

    def _obj__get_parent_obj_(self, *args):
        if self._obj__get_parent_exist_() is True:
            _nodepathStr = self.CLS_grh__obj__loader.getNodeParentPath(
                self.pathString()
            )
            return self._node_cls__get_node_cache_obj_(_nodepathStr)

    def _obj__get_children_exist_(self, *args):
        return self.CLS_grh__obj__loader.getNodeHasChildren(
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
            _nodepathStrList = self.CLS_grh__obj__loader.getNodeChildPaths(
                self.pathString(), *args, **kwargs
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

        asString = getArgsFnc_(kwargs)

        if self._obj__get_children_exist_() is True:
            _nodepathStrList = self.CLS_grh__obj__loader.getNodeAllChildPaths(
                self.pathString(), *args, **kwargs
            )
            if asString is True:
                return _nodepathStrList
            return [self._node_cls__get_node_cache_obj_(_i) for _i in _nodepathStrList]
        return []

    # **************************************************************************************************************** #
    def _grh_node__get_is_compnode_(self):
        return self.CLS_grh__obj__loader.getNodeIsCompnode(
            self.pathString()
        )

    def _grh_node__get_is_transform_(self):
        return self.CLS_grh__obj__loader.getNodeIsTransform(
            self.pathString()
        )

    def _grh_node__get_is_shape_(self):
        return self.CLS_grh__obj__loader.getNodeIsShape(
            self.pathString()
        )
