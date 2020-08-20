# coding:utf-8
from LxBasic import bscMethods

from . import grhCfg, grhMtdCore


class ItfGrhObjStackSite(grhCfg.GrhUtility):
    CLS_grh__variant_set__obj_stack = None

    def _initItfGrhVariantObjStack(self, *args):
        self._obj = args[0]

        self._stackObjKeyStrList = []
        self._stackObjList = []

    # **************************************************************************************************************** #
    def _obj_stack_site__set_stack_obj_key_str_filter_(self, *args):
        stackObjKeyStrList = args[0]
        for i in self._stackObjKeyStrList:
            if not i in self._stackObjKeyStrList:
                stackObjKeyStrList.remove(i)
        return stackObjKeyStrList

    def _obj_stack_site__get_include_str_list_(self, kwargs):
        if kwargs:
            if u'include' in kwargs:
                _ = kwargs[u'include']
                if isinstance(_, (str, unicode)):
                    return self._obj_stack_site__set_stack_obj_key_str_filter_(
                        [_]
                    )
                elif isinstance(_, (tuple, list)):
                    return self._obj_stack_site__set_stack_obj_key_str_filter_(
                        list(_)
                    )

    def _obj_stack_site__get_exclude_str_list_(self, kwargs):
        if kwargs:
            if u'exclude' in kwargs:
                _ = kwargs[u'exclude']
                if isinstance(_, (str, unicode)):
                    return self._obj_stack_site__set_stack_obj_key_str_filter_(
                        [_]
                    )
                elif isinstance(_, (tuple, list)):
                    return self._obj_stack_site__set_stack_obj_key_str_filter_(
                        list(_)
                    )

    # **************************************************************************************************************** #
    def stacks(self):
        return self._stackObjList

    def hasStacks(self):
        return self._stackObjList != []

    def _obj_stack_site__set_stack_add_(self, *args):
        _ = args[0]
        if isinstance(_, (str, unicode)):
            objKeyStr = _
            if objKeyStr not in self._stackObjKeyStrList:
                objStackObj = self.CLS_grh__variant_set__obj_stack(self._obj)
                self._stackObjKeyStrList.append(objKeyStr)
                self._stackObjList.append(objStackObj)
        elif isinstance(_, self.CLS_grh__variant_set__obj_stack):
            _objStackObj = _
            _objKeyStr = None

    def addStack(self, *args):
        self._obj_stack_site__set_stack_add_(*args)

    def _obj_stack_site__get_stack_exist_(self, *args):
        objKeyStr = args[0]
        return objKeyStr in self._stackObjKeyStrList

    def hasStack(self, *args):
        return self._obj_stack_site__get_stack_exist_(*args)

    def _obj_stack_site__get_stack_obj_(self, *args):
        objKeyStr = args[0]
        if objKeyStr in self._stackObjKeyStrList:
            index = self._stackObjKeyStrList.index(objKeyStr)
            return self._stackObjList[index]

    def stack(self, *args):
        return self._obj_stack_site__get_stack_obj_(*args)

    # **************************************************************************************************************** #
    def _obj_stack_site__set_obj_add_(self, *args, **kwargs):
        if self.hasStacks():
            includeStrList = self._obj_stack_site__get_include_str_list_(kwargs)
            #
            objStackObjList = [self.stack(i) for i in includeStrList]
            for objStackObj in objStackObjList:
                if objStackObj is not None:
                    objStackObj._obj_stack__set_obj_add_(*args)

    def addObject(self, *args, **kwargs):
        self._obj_stack_site__set_obj_add_(*args, **kwargs)

    def _obj_stack_site__get_obj_exist_(self, *args, **kwargs):
        def getArgsFnc_(kwargs_):
            _variantStr = None
            if kwargs_:
                if u'include' in kwargs_:
                    _variantStr = kwargs_[u'include']
            return _variantStr

        includeStr = getArgsFnc_(kwargs)
        objStackObj = self._obj_stack_site__get_stack_obj_(includeStr)
        if objStackObj is not None:
            return objStackObj._obj_stack__get_obj_exist_(*args)
        return False

    def hasObject(self, *args, **kwargs):
        return self._obj_stack_site__get_obj_exist_(*args, **kwargs)

    def _obj_stack_site__get_obj_(self, *args, **kwargs):
        def getArgsFnc_(kwargs_):
            _variantStr = None
            if kwargs_:
                if u'include' in kwargs_:
                    _variantStr = kwargs_[u'include']
            return _variantStr

        includeStr = getArgsFnc_(kwargs)
        objStackObj = self._obj_stack_site__get_stack_obj_(includeStr)
        if objStackObj is not None:
            return objStackObj._obj_stack__get_obj_(*args)

    def object(self, *args, **kwargs):
        return self._obj_stack_site__get_obj_(*args, **kwargs)


# object query loader ************************************************************************************************ #
class ItfGrhObjSceneLoader(grhCfg.GrhUtility):
    def _initItfGrhObjScene(self, *args, **kwargs):
        self._obj_scene_loader__set_build_(*args, **kwargs)

    def _obj_scene_loader__set_build_(self, *args, **kwargs):
        pass

    # **************************************************************************************************************** #
    def _obj_scene_loader__get_node_obj_(self, *args):
        pass

    def getNode(self, *args):
        return self._obj_scene_loader__get_node_obj_(*args)

    # **************************************************************************************************************** #
    def _obj_scene_loader__get_node_root_obj_(self):
        pass

    def getNodeRoot(self):
        return self._obj_scene_loader__get_node_root_obj_()

    def _obj_scene_loader__get_all_node_obj_list_(self, **kwargs):
        pass

    # **************************************************************************************************************** #
    def getAllNodes(self, **kwargs):
        return self._obj_scene_loader__get_all_node_obj_list_(**kwargs)

    def _obj_scene_loader__get_all_node_str_list_(self, **kwargs):
        pass

    def getAllNodepaths(self, **kwargs):
        return self._obj_scene_loader__get_all_node_str_list_(**kwargs)


class ItfGrhObjLoader(grhCfg.GrhUtility):
    CALL_grh__obj_loader__get_obj_scene = None

    VAR_grh__obj_loader__node_type__transform = None

    def _initItfGrhObjLoader(self, *args):
        pass

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_obj_scene_obj_(cls):
        pass

    @classmethod
    def getScene(cls):
        return cls._obj_loader_cls__get_obj_scene_obj_()

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__set_port_raw_add_(cls, portRawList, **kwargs):
        _portRaw = cls.CLS_ordered_dict()
        for i in [
            cls.DEF_grh__key_portpath,
            cls.DEF_grh__key_porttype,
            cls.DEF_grh__key_port_datatype,
            cls.DEF_grh__key_portraw,
            cls.DEF_grh__key_assign,
            cls.DEF_grh__key_format,
            cls.DEF_grh__key_parent,
            cls.DEF_grh__key_children
        ]:
            if i in kwargs:
                _portRaw[i] = kwargs[i]
            else:
                _portRaw[i] = None
        portRawList.append(_portRaw)
        return _portRaw

    @classmethod
    def _obj_loader_cls__get_port_raw_(cls, **kwargs):
        _portRaw = cls.CLS_ordered_dict()
        for i in [
            cls.DEF_grh__key_portpath,
            cls.DEF_grh__key_porttype,
            cls.DEF_grh__key_port_datatype,
            cls.DEF_grh__key_portraw,
            cls.DEF_grh__key_assign,
            cls.DEF_grh__key_format,
            cls.DEF_grh__key_parent,
            cls.DEF_grh__key_children
        ]:
            if i in kwargs:
                _portRaw[i] = kwargs[i]
            else:
                _portRaw[i] = None
        return _portRaw

    # **************************************************************************************************************** #
    @classmethod
    def _grh__obj_loader_cls__get_definition_node_raw_(cls, *args):
        pass

    @classmethod
    def getDefinitionNodeRaw(cls, *args):
        return cls._grh__obj_loader_cls__get_definition_node_raw_(*args)

    @classmethod
    def _obj_loader_cls__get_definition_port_raw_(cls, *args):
        pass

    @classmethod
    def getDefinitionPortRaw(cls, *args):
        return cls._obj_loader_cls__get_definition_port_raw_(*args)

    @classmethod
    def _grh__obj_loader_cls__get_customize_vlport_port_raws_(cls, *args, **kwargs):
        pass

    @classmethod
    def getCustomizeVlportRaws(cls, *args, **kwargs):
        return cls._grh__obj_loader_cls__get_customize_vlport_port_raws_(*args, **kwargs)

    @classmethod
    def _grh__obj_loader_cls__get_customize_inport_port_raws_(cls, *args, **kwargs):
        pass

    @classmethod
    def getCustomizeInportRaws(cls, *args, **kwargs):
        return cls._grh__obj_loader_cls__get_customize_inport_port_raws_(*args, **kwargs)

    @classmethod
    def _grh__obj_loader_cls__get_customize_otport_port_raws_(cls, *args, **kwargs):
        pass

    @classmethod
    def getCustomizeOtportRaws(cls, *args, **kwargs):
        return cls._grh__obj_loader_cls__get_customize_otport_port_raws_(*args, **kwargs)

    @classmethod
    def _obj_loader_cls__get_customize_port_raw_(cls, *args, **kwargs):
        pass

    @classmethod
    def getCustomizePortRaw(cls, *args, **kwargs):
        return cls._obj_loader_cls__get_customize_port_raw_(*args, **kwargs)

    @classmethod
    def _grh__obj_loader_cls__get_customize_port_raw_list_(cls, *args, **kwargs):
        pass

    @classmethod
    def getCustomizePortRaws(cls, *args, **kwargs):
        return cls._grh__obj_loader_cls__get_customize_port_raw_list_(*args, **kwargs)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_obj_exist_(cls, *args):
        pass

    @classmethod
    def getNodeIsExist(cls, *args):
        return cls._obj_loader_cls__get_obj_exist_(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_type_str_(cls, *args):
        pass

    @classmethod
    def getNodeType(cls, *args):
        return cls._obj_loader_cls__get_type_str_(*args)

    @classmethod
    def _obj_loader_cls__get_typepath_str_(cls, *args):
        pass

    @classmethod
    def getNodeTypepath(cls, *args):
        return cls._obj_loader_cls__get_typepath_str_(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_fullpath_str_(cls, *args):
        pass

    @classmethod
    def getFullpath(cls, *args):
        return cls._obj_loader_cls__get_fullpath_str_(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_port_obj_(cls, *args):
        pass

    @classmethod
    def getNodePort(cls, *args):
        return cls._obj_loader_cls__get_port_obj_(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_node_parent_exist_(cls, *args):
        pass

    @classmethod
    def getNodeHasParent(cls, *args):
        return cls._obj_loader_cls__get_node_parent_exist_(*args)

    @classmethod
    def _obj_loader_cls__get_node_parent_str_(cls, *args):
        pass

    @classmethod
    def getNodeParentPath(cls, *args):
        return cls._obj_loader_cls__get_node_parent_str_(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__set_node_filter_(cls, *args, **kwargs):
        def getIncludeVarFnc_(kwargs_):
            if kwargs_:
                if u'include' in kwargs_:
                    _ = kwargs_[u'include']
                    if isinstance(_, (str, unicode)):
                        return [_]
                    elif isinstance(_, (tuple, list)):
                        return list(_)

        def getExcludeVarFnc_(kwargs_):
            if kwargs_:
                if u'exclude' in kwargs_:
                    _ = kwargs_[u'exclude']
                    if isinstance(_, (str, unicode)):
                        return [_]
                    elif isinstance(_, (tuple, list)):
                        return list(_)

        ns = args[0]

        includeTypeList = getIncludeVarFnc_(kwargs)
        excludeTypeList = getExcludeVarFnc_(kwargs)

        if includeTypeList is not None:

            return [i for i in ns if cls.getNodeType(i) in includeTypeList]
        elif excludeTypeList is not None:
            return [i for i in ns if cls.getNodeType(i) not in excludeTypeList]
        return ns

    @classmethod
    def _obj_loader_cls__get_node_children_exist_(cls, *args, **kwargs):
        pass

    @classmethod
    def getNodeHasChildren(cls, *args):
        return cls._obj_loader_cls__get_node_children_exist_(*args)

    @classmethod
    def _obj_loader_cls__get_node_child_str_list_(cls, *args, **kwargs):
        pass

    @classmethod
    def getNodeChildPaths(cls, *args, **kwargs):
        return cls._obj_loader_cls__get_node_child_str_list_(*args, **kwargs)

    @classmethod
    def _obj_loader_cls__get_node_all_child_str_list_(cls, *args, **kwargs):
        pass

    @classmethod
    def getNodeAllChildPaths(cls, *args, **kwargs):
        return cls._obj_loader_cls__get_node_all_child_str_list_(*args, **kwargs)

    # compnode ******************************************************************************************************* #
    @classmethod
    def _obj_loader_cls__get_node_is_compnode_(cls, *args):
        pass

    @classmethod
    def getNodeIsCompnode(cls, *args):
        return cls._obj_loader_cls__get_node_is_compnode_(*args)

    @classmethod
    def _obj_loader_cls__get_node_is_transform_(cls, *args):
        pass

    @classmethod
    def getNodeIsTransform(cls, *args):
        return cls._obj_loader_cls__get_node_is_transform_(*args)

    @classmethod
    def _obj_loader_cls__get_node_is_shape_(cls, *args):
        pass

    @classmethod
    def getNodeIsShape(cls, *args):
        """
        is not "transform"; parent is "transform"
        :param args:
        :return:
        """
        return cls._obj_loader_cls__get_node_is_shape_(*args)


# object query raw creator ******************************************************************************************* #
class ItfGrhPortQueryraw(grhCfg.GrhUtility):
    def _initItfGrhPortQueryraw(self, *args):
        self._portRaw = args[0]

        self._port_queryraw__set_property_build_(
            self._portRaw
        )

    def _port_queryraw__set_property_build_(self, *args):
        raw = args[0]
        for k, v in raw.items():
            self.__dict__[k] = raw[k]

    def portRaw(self):
        return self._portRaw

    def __str__(self):
        if hasattr(self, u'portpath'):
            return u'{}(portpath="{}")'.format(
                self.__class__.__name__,
                self.portpath
            )
        return ''

    def __repr__(self):
        return self.__str__()


class ItfGrhNodeQueryraw(grhCfg.GrhUtility):
    CLS_grh__node_queryraw__port_queryraw_stack = None
    CLS_grh__node_queryraw__port_queryraw = None

    def _initItfGrhNodeQueryraw(self, *args):
        if len(args) == 1:
            self._nodeRaw = args[0]
            self._typepathStr = self._nodeRaw[grhCfg.GrhNodeQuery.typepath]
        else:
            raise TypeError(
                u'''???'''
            )

        self._grh__node_queryraw__set_property_build_(self._nodeRaw)

        self._grh__node_queryraw__set_ports_build_(
            self._nodeRaw[self.DEF_grh__key_port]
        )

    # **************************************************************************************************************** #
    def _grh__node_queryraw__set_property_build_(self, *args):
        raw = args[0]
        for k, v in raw.items():
            self.__dict__[k] = raw[k]

    def _grh__node_queryraw__set_ports_build_(self, *args):
        portRaws = args[0]
        self._nodeQueryrawInportStackObj = self.CLS_grh__node_queryraw__port_queryraw_stack(self)
        self._nodeQueryrawOtportStackObj = self.CLS_grh__node_queryraw__port_queryraw_stack(self)
        self._nodeQueryrawAsportStackObj = self.CLS_grh__node_queryraw__port_queryraw_stack(self)

        for portRaw in portRaws:
            self._grh__node_queryraw__set_port_create_(portRaw)

    def _grh__node_queryraw__set_port_create_(self, *args):
        portRaw = args[0]
        _assignStr = portRaw[self.DEF_grh__key_assign]

        portQueryrawObj = self.CLS_grh__node_queryraw__port_queryraw(portRaw)
        # portQueryraw can be "inport" and / or "otport"

        if grhCfg.GrhPortAssignQuery.isInport(_assignStr):
            self._nodeQueryrawInportStackObj._obj_stack__set_obj_add_(portQueryrawObj)
        if grhCfg.GrhPortAssignQuery.isOtport(_assignStr):
            self._nodeQueryrawOtportStackObj._obj_stack__set_obj_add_(portQueryrawObj)
        if grhCfg.GrhPortAssignQuery.isAsport(_assignStr):
            self._nodeQueryrawAsportStackObj._obj_stack__set_obj_add_(portQueryrawObj)
        return portQueryrawObj

    # **************************************************************************************************************** #
    def nodeRaw(self):
        return self._nodeRaw

    # **************************************************************************************************************** #
    def portQueryraws(self, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_list_(
            (self._nodeQueryrawInportStackObj, self._nodeQueryrawOtportStackObj, self._nodeQueryrawAsportStackObj),
            **kwargs
        )

    def hasPortQueryraw(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_exist_(
            (self._nodeQueryrawInportStackObj, self._nodeQueryrawOtportStackObj, self._nodeQueryrawAsportStackObj),
            *args, **kwargs
        )

    def portQueryraw(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_(
            (self._nodeQueryrawInportStackObj, self._nodeQueryrawOtportStackObj, self._nodeQueryrawAsportStackObj),
            *args, **kwargs
        )

    def createPortQueryraw(self, *args):
        portRaw = args[0]
        return self.CLS_grh__node_queryraw__port_queryraw(portRaw)

    def outPortRaw(self, *args, **kwargs):
        if self.hasPortQueryraw(*args, **kwargs):
            return self.portQueryraw(*args, **kwargs).portRaw()

    # inport ********************************************************************************************************* #
    def inportQueryraws(self):
        return self._nodeQueryrawInportStackObj.objects()

    def hasInportQueryraw(self, *args):
        return self._nodeQueryrawInportStackObj.hasObject(*args)

    def inportQueryraw(self, *args):
        if self.hasInportQueryraw(*args):
            return self._nodeQueryrawInportStackObj.object(*args)

    def outInportRaw(self, *args):
        if self.hasInportQueryraw(*args):
            return self.inportQueryraw(*args).portRaw()
    
    # otport ********************************************************************************************************* #
    def otportQueryraws(self):
        return self._nodeQueryrawOtportStackObj.objects()

    def hasOtportQueryraw(self, *args):
        return self._nodeQueryrawOtportStackObj.hasObject(*args)

    def otportQueryraw(self, *args):
        if self.hasOtportQueryraw(*args):
            return self._nodeQueryrawOtportStackObj.object(*args)

    def outOtportRaw(self, *args):
        if self.hasOtportQueryraw(*args):
            return self.otportQueryraw(*args).portRaw()

    # asport ********************************************************************************************************* #
    def asportQueryraws(self):
        return self._nodeQueryrawAsportStackObj.objects()

    def hasAsportQueryraw(self, *args):
        return self._nodeQueryrawAsportStackObj.hasObject(*args)

    def asportQueryraw(self, *args):
        if self.hasAsportQueryraw(*args):
            return self._nodeQueryrawAsportStackObj.object(*args)

    def outAsportRaw(self, *args):
        if self.hasAsportQueryraw(*args):
            return self.asportQueryraw(*args).portRaw()

    # **************************************************************************************************************** #
    def __str__(self):
        if hasattr(self, u'typepath'):
            return u'{}(typepath="{}")'.format(
                self.__class__.__name__,
                self.typepath
            )
        return ''

    def __repr__(self):
        return self.__str__()


class ItfGrhObjQueryrawCreator(grhCfg.GrhUtility):
    CLS_grh__obj_query_creator__node_queryraw_stack = None
    CLS_grh__obj_query_creator__node_queryraw = None

    CLS_grh__obj_query_creator__obj_loader = None

    VAR_grh__node_file = None
    VAR_grh__geometry_file = None
    VAR_grh__material_file = None
    VAR_grh__output_file = None
    VAR_grh__port_child_file = None

    # noinspection PyUnusedLocal
    def _initItfGrhObjQueryrawCreator(self, *args):
        self._nodeQueryrawStackObj = self.CLS_grh__obj_query_creator__node_queryraw_stack(self)

        self._queryraw_loader__set_build_()

    def _queryraw_loader__set_build_(self):
        pass

    # **************************************************************************************************************** #
    def _queryraw_loader__get_node_raw_(self, *args):
        pass

    def _queryraw_loader__get_node_obj_(self, *args):
        if isinstance(args[0], (str, unicode)):
            typepathStr = args[0]
            nodeRaw = self._queryraw_loader__get_node_raw_(typepathStr)
            if nodeRaw:
                return self.CLS_grh__obj_query_creator__node_queryraw(
                    nodeRaw
                )
            raise TypeError(
                u'''???'''
            )
        elif isinstance(args[0], dict):
            return self.CLS_grh__obj_query_creator__node_queryraw(*args)
        raise TypeError(
            u'''???'''
        )

    def _queryraw_loader__get_node_(self, *args):
        if self._nodeQueryrawStackObj._obj_stack__get_obj_exist_(*args):
            return self._nodeQueryrawStackObj._obj_stack__get_obj_(*args)
        #
        obj = self._queryraw_loader__get_node_obj_(*args)
        self._nodeQueryrawStackObj._obj_stack__set_obj_add_(obj)
        return obj

    def nodeQueryraw(self, *args):
        """
        :param args:
            1 args: ( str( "typepath" ), )
        :return: objects.NodeQueryraw
        """
        return self._queryraw_loader__get_node_(*args)

    # **************************************************************************************************************** #
    def _queryraw_loader__get_port_raw_(self, *args):
        typepathStr, portpathStr = args
        nodeQueryrawObj = self._queryraw_loader__get_node_(typepathStr)
        return nodeQueryrawObj.portQueryraw(portpathStr)

    def _queryraw_loader__get_port_obj_(self, *args):
        portQueryrawCls = self.CLS_grh__obj_query_creator__node_queryraw.CLS_grh__node_queryraw__port_queryraw
        if isinstance(args[0], (str, unicode)):
            portRaw = self._queryraw_loader__get_port_raw_(*args)
            if portRaw:
                return portQueryrawCls(portRaw)
            raise TypeError(
                u'''???'''
            )
        elif isinstance(args[0], dict):
            return portQueryrawCls(*args)
        raise TypeError(
            u'''???'''
        )

    def _queryraw_loader__get_port_(self, *args):
        typepathStr, portpathStr = args
        # exist node
        if self._nodeQueryrawStackObj._obj_stack__get_obj_exist_(typepathStr):
            nodeQueryrawObject = self._nodeQueryrawStackObj._obj_stack__get_obj_(typepathStr)
            # registered port
            if nodeQueryrawObject.hasPortQueryraw(portpathStr):
                return nodeQueryrawObject.portQueryraw(portpathStr)
            # unregistered port
            return self._queryraw_loader__get_port_obj_(
                typepathStr, portpathStr
            )
        #
        raise TypeError(
            u'''typepath "{}" is unregistered'''
        )

    def portQueryraw(self, *args):
        """
        :param args:
            1 args: ( str( "typepath" ), str( "portpath" ) )
        :return: objects.NodeQueryraw
        """
        return self._queryraw_loader__get_port_(*args)

    # **************************************************************************************************************** #
    def _queryraw_loader__get_categories_(self):
        pass

    def _queryraw_loader__get_category_exist_(self, *args):
        pass

    def typepaths(self):
        return self._queryraw_loader__get_categories_()

    def hasTypepath(self, *args):
        return self._queryraw_loader__get_category_exist_(*args)


# object query builder *********************************************************************************************** #
class ItfGrhObjQueryDef(object):
    IST_grh__obj_query__queryraw_builder = None

    def _initItfGrhObjQueryDef(self, *args):
        pass


class ItfGrhPortQuery(
    grhCfg.GrhUtility,
    ItfGrhObjQueryDef
):
    VAR_grh__port_query__portsep = None

    def _initItfGrhPortQuery(self, *args):
        # build
        if args:
            nodeArg, portArg = args
            if isinstance(nodeArg, ItfGrhNodeQuery):
                self._nodeQueryrawObj = nodeArg.nodeQueryraw()
            elif isinstance(nodeArg, ItfGrhNodeQueryraw):
                self._nodeQueryrawObj = nodeArg
            elif isinstance(nodeArg, (str, unicode)):
                typepathStr = nodeArg
                self._nodeQueryrawObj = self.IST_grh__obj_query__queryraw_builder.nodeQueryraw(typepathStr)
            else:
                raise TypeError()

            if isinstance(portArg, ItfGrhPortQueryraw):
                self._portQueryrawObj = portArg
            elif isinstance(portArg, (str, unicode)):
                typepathStr = self._nodeQueryrawObj.typepath
                portpathStr = portArg
                self._portQueryrawObj = self.IST_grh__obj_query__queryraw_builder.portQueryraw(typepathStr, portpathStr)
            elif isinstance(portArg, dict):
                portRaw = portArg
                self._portQueryrawObj = self.IST_grh__obj_query__queryraw_builder._queryraw_loader__get_port_obj_(portRaw)
            else:
                raise TypeError()

        self._port_query__set_property_build_()

    def _port_query__set_property_build_(self):
        for k, v in self._portQueryrawObj.portRaw().items():
            self.__dict__[k] = v

    def nodeQueryraw(self):
        return self._nodeQueryrawObj

    def portQueryraw(self):
        return self._portQueryrawObj

    @property
    def portsep(self):
        return self.VAR_grh__port_query__portsep

    # **************************************************************************************************************** #
    def toString(self):
        return self._portQueryrawObj.portpath

    # **************************************************************************************************************** #
    def __str__(self):
        return u'{}(typepath="{}", portpath="{}", assign="{}")'.format(
            self.__class__.__name__,
            self._nodeQueryrawObj.typepath,
            self._portQueryrawObj.portpath,
            self._portQueryrawObj.assign
        )

    def __repr__(self):
        return self.__str__()


class ItfGrhNodeQuery(
    grhCfg.GrhUtility,
    ItfGrhObjQueryDef
):
    CLS_grh__node_query__port_query_stack = None
    CLS_grh__node_query__port_query = None

    def _initItfGrhNodeQuery(self, *args):
        if args:
            self._graphicNameString = u'unknown'
            if isinstance(args[0], ItfGrhNodeQueryraw):
                self._nodeQueryrawObj = args[0]
            elif isinstance(args[0], dict):
                pass
            elif isinstance(args[0], (str, unicode)):
                typepathStr = args[0]
                self._nodeQueryrawObj = self.IST_grh__obj_query__queryraw_builder.nodeQueryraw(typepathStr)
                if len(args) == 2:
                    self._graphicNameString = args[1]
            else:
                raise TypeError(
                    u''''''
                )
        else:
            raise TypeError(
                u'''argument must not be empty'''
            )

        self._portpathDict = {}

        self._node_query__set_property_build_()
        self._node_query__set_ports_build_()

        # bscMethods.PyMessage.traceResult(
        #     u'''create node query : "{} @ {}"'''.format(
        #         self.__dict__[u'category'], self._graphicNameString
        #     )
        # )

    def _node_query__set_property_build_(self):
        for k, v in self._nodeQueryrawObj.nodeRaw().items():
            self.__dict__[k] = v

    def _node_query__set_ports_build_(self):
        self._nodeQueryInportStackObj = self.CLS_grh__node_query__port_query_stack(self)
        self._nodeQueryOtportStackObj = self.CLS_grh__node_query__port_query_stack(self)
        self._nodeQueryAsportStackObj = self.CLS_grh__node_query__port_query_stack(self)
        
        [self._node_query__set_port_build_(self._nodeQueryInportStackObj, i) for i in self._nodeQueryrawObj.inportQueryraws()]
        [self._node_query__set_port_build_(self._nodeQueryOtportStackObj, i) for i in self._nodeQueryrawObj.otportQueryraws()]
        [self._node_query__set_port_build_(self._nodeQueryAsportStackObj, i) for i in self._nodeQueryrawObj.asportQueryraws()]
    
    def _node_query__set_port_build_(self, *args):
        portStackObj, portQueryrawObj = args

        portQueryObj = self.CLS_grh__node_query__port_query(
            self.nodeQueryraw(),
            portQueryrawObj
        )

        portpathStr = portQueryrawObj.portpath
        portnameStr = portpathStr.split(portQueryObj.portsep)[-1]
        self._portpathDict[portnameStr] = portpathStr

        portStackObj._obj_stack__set_obj_add_(portQueryObj)

    # **************************************************************************************************************** #
    def _node_query__get_portpath_(self, *args):
        portpathStr = args[0]
        if portpathStr in self._portpathDict:
            return self._portpathDict[portpathStr]
        return portpathStr

    # **************************************************************************************************************** #
    def portQueries(self, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_list_(
            (self._nodeQueryInportStackObj, self._nodeQueryOtportStackObj, self._nodeQueryAsportStackObj),
            **kwargs
        )

    def hasPortQuery(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_exist_(
            (self._nodeQueryInportStackObj, self._nodeQueryOtportStackObj, self._nodeQueryAsportStackObj),
            *args, **kwargs
        )

    def portQuery(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_(
            (self._nodeQueryInportStackObj, self._nodeQueryOtportStackObj, self._nodeQueryAsportStackObj),
            *args, **kwargs
        )

    # **************************************************************************************************************** #
    def inportQueries(self):
        return self._nodeQueryInportStackObj.objects()

    def hasInportQuery(self, *args):
        return self._nodeQueryInportStackObj.hasObject(*args)

    def inportQuery(self, *args):
        return self._nodeQueryInportStackObj.object(*args)

    # **************************************************************************************************************** #
    def otportQueries(self):
        return self._nodeQueryOtportStackObj.objects()

    def hasOtportQuery(self, *args):
        return self._nodeQueryOtportStackObj.hasObject(*args)

    def otportQuery(self, *args):
        return self._nodeQueryOtportStackObj.object(*args)

    # **************************************************************************************************************** #
    def asportQueries(self):
        return self._nodeQueryAsportStackObj.objects()

    def hasAsportQuery(self, *args):
        return self._nodeQueryAsportStackObj.hasObject(*args)

    def asportQuery(self, *args):
        return self._nodeQueryAsportStackObj.object(*args)

    # **************************************************************************************************************** #
    def nodeQueryraw(self):
        return self._nodeQueryrawObj

    # **************************************************************************************************************** #
    def toString(self):
        return self._nodeQueryrawObj.typepath

    # **************************************************************************************************************** #
    def __str__(self):
        if hasattr(self, u'typepath'):
            return u'{}(typepath="{}")'.format(
                self.__class__.__name__,
                self._nodeQueryrawObj.typepath
            )
        return u''

    def __repr__(self):
        return self.__str__()


class ItfGrhObjQueryBuilder(grhCfg.GrhUtility):
    CLS_grh__obj_query_builder__node_query_stack = None
    CLS_grh__obj_query_builder__node_query = None

    # noinspection PyUnusedLocal
    def _initItfGrhObjQueryBuilder(self, *args):
        self._graphicNameString = args[0]

        self._nodeQueryStackObj = self.CLS_grh__obj_query_builder__node_query_stack(self)

    # **************************************************************************************************************** #
    def _get_node_query_(self, *args):
        typepathStr = args[0]
        if self._nodeQueryStackObj._obj_stack__get_obj_exist_(typepathStr):
            return self._nodeQueryStackObj._obj_stack__get_obj_(typepathStr)

        obj = self.CLS_grh__obj_query_builder__node_query(
            typepathStr,
            self._graphicNameString
        )
        self._nodeQueryStackObj._obj_stack__set_obj_add_(obj)
        return obj

    def nodeQuery(self, *args):
        return self._get_node_query_(*args)

    # **************************************************************************************************************** #
    def _get_port_query_(self, *args):
        typepathStr, portpathStr = args
        nodeQueryObject = self._get_node_query_(typepathStr)
        return nodeQueryObject.portQuery(portpathStr)

    def portQuery(self, *args):
        """
        :param args: ( str( "category" ), str( "portpath" ) )
        :return:
        """
        return self._get_port_query_(*args)

    # **************************************************************************************************************** #
    def _get_inport_query_(self, *args):
        typepathStr, portpathStr = args
        nodeQueryObject = self._get_node_query_(typepathStr)
        return nodeQueryObject.inportQuery(portpathStr)

    def inportQuery(self, *args):
        return self._get_inport_query_(*args)

    # **************************************************************************************************************** #
    def _get_otport_query_(self, *args):
        typepathStr, portpathStr = args
        nodeQueryObject = self._get_node_query_(typepathStr)
        return nodeQueryObject.otportQuery(portpathStr)

    def otportQuery(self, *args):
        return self._get_otport_query_(*args)

    # **************************************************************************************************************** #
    @property
    def nodeQueryCls(self):
        return self.CLS_grh__obj_query_builder__node_query

    @property
    def portQueryCls(self):
        return self.CLS_grh__obj_query_builder__node_query.CLS_grh__node_query__port_query


# object queue ******************************************************************************************************* #
class ItfGrhCacheObjDef(object):
    CLS_grh__cache_obj__variant = None
    CLS_grh__cache_obj__variant_obj_stack = None

    def _initItfGrhCacheObjDef(self):
        self._defaultVariantObj = self.CLS_grh__cache_obj__variant(
            self.CLS_grh__cache_obj__variant.sep()
        )
        self._variantObj = self.CLS_grh__cache_obj__variant(
            self.CLS_grh__cache_obj__variant.sep()
        )

        self._variantStackObj = self.CLS_grh__cache_obj__variant_obj_stack(self)
        self._variantStackObj._obj_stack__set_obj_add_(self)

    # **************************************************************************************************************** #
    def addVariantObject(self, *args):
        variantStr = args[0]
        variantObj = grhCfg.GrhUtility.MOD_copy.copy(self)
        variantObj._cache_obj__set_variant_str_(variantStr)
        self._variantStackObj._obj_stack__set_obj_add_(variantObj)
        return variantObj

    def variantObjects(self):
        return self._variantStackObj._obj_stack__get_obj_list_()

    def variantObject(self, *args):
        return self._variantStackObj._obj_stack__get_obj_(*args)

    def isVariantObject(self):
        return self._variantObj == self._defaultVariantObj

    # **************************************************************************************************************** #
    def variant(self):
        return self._variantObj

    def _cache_obj__set_variant_str_(self, *args):
        self._variantObj.setRaw(*args)

    def variantString(self):
        return self._variantObj.toString()


class ItfGrhObjQueue(grhCfg.GrhUtility):
    CLS_grh__obj_queue__node_stack = None

    # noinspection PyUnusedLocal
    def _initItfGrhObjQueue(self, *args):
        # node
        self._objQueueNodeStackObj = self.CLS_grh__obj_queue__node_stack(self)
        self._objQueueNodeTypepathStrList = []

    # **************************************************************************************************************** #
    def _obj_queue__set_node_add_(self, *args):
        obj = args[0]
        if self._objQueueNodeStackObj.hasObject(obj) is False:
            self._objQueueNodeStackObj.addObject(obj)
            typepathStr = obj.typepathString()
            self._objQueueNodeTypepathStrList.append(typepathStr)

    def addNode(self, *args):
        self._obj_queue__set_node_add_(*args)

    # **************************************************************************************************************** #
    def _obj_queue__get_node_exist_(self, *args):
        return self._objQueueNodeStackObj.hasObject(*args)

    def hasNode(self, *args):
        return self._obj_queue__get_node_exist_(*args)

    def _obj_queue__get_node_(self, *args, **kwargs):
        if kwargs:
            pass

        # gain exist
        if len(args) == 1:
            if isinstance(args[0], ItfGrhCacheObjDef):
                obj = args[0]
                return self._objQueueNodeStackObj._obj_stack__get_obj_(obj)
            elif isinstance(args[0], (float, int)):
                index = args[0]
                return self._objQueueNodeStackObj._obj_stack__get_obj_(index)
            elif isinstance(args[0], (str, unicode)):
                objKeyStr = args[0]
                return self._objQueueNodeStackObj._obj_stack__get_obj_(objKeyStr)
        #
        objKeyStr, objCls, objClsArgs = args
        if self._objQueueNodeStackObj.hasObject(objKeyStr) is True:
            return self._objQueueNodeStackObj.object(objKeyStr)
        # register
        obj = objCls(*objClsArgs, **kwargs)
        self._obj_queue__set_node_add_(obj)
        return obj

    def node(self, *args, **kwargs):
        return self._obj_queue__get_node_(*args, **kwargs)

    # **************************************************************************************************************** #
    def _obj_queue__get_nodes_exist_(self, **kwargs):
        return self._objQueueNodeStackObj._obj_stack__get_objs_exist_(**kwargs)

    def hasNodes(self, **kwargs):
        return self._obj_queue__get_nodes_exist_(**kwargs)

    def _obj_queue__get_node_obj_list_(self, **kwargs):
        if kwargs:
            if u'include' in kwargs:
                _ = kwargs[u'include']
                if isinstance(_, (str, unicode)):
                    includeArg = [_]
                elif isinstance(_, (tuple, list)):
                    includeArg = _
                else:
                    raise
                return [self._objQueueNodeStackObj.object(s) for s, i in enumerate(self._objQueueNodeTypepathStrList) if i in includeArg]
        return self._objQueueNodeStackObj._obj_stack__get_obj_list_(**kwargs)

    def nodes(self, **kwargs):
        return self._obj_queue__get_node_obj_list_(**kwargs)

    # **************************************************************************************************************** #
    def _obj_queue__set_data_init_(self):
        self._objQueueNodeStackObj.restore()

    def restore(self):
        self._obj_queue__set_data_init_()


# object ************************************************************************************************************* #
class ItfGrhObjDef(object):
    """
    basic primitive
    """
    CLS_grh__obj__obj_stack = None
    CLS_grh__obj__obj_proxy_stack = None

    CLS_grh__obj__path = None

    CLS_grh__obj__loader = None

    IST_grh__obj__query_builder = None
    IST_grh__obj__queue = None

    VAR_grh__dcc = None

    # noinspection PyUnusedLocal
    def _initItfGrhObjDef(self, *args):
        # parent
        self._parentObjPath = None
        # children
        self._childObjPathList = []
        # proxy stack
        self._objProxyStackObj = self.CLS_grh__obj__obj_proxy_stack(self)

    # build ********************************************************************************************************** #
    def _obj__set_path_build_(self, *args):
        self._objPathObj = self.CLS_grh__obj__path(*args)

    def _obj__set_children_build_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    # create ********************************************************************************************************* #
    def _obj__set_create_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    def create(self, *args):
        """
        :param args:
        :return:
        """
        self._obj__set_create_(*args)

    # path *********************************************************************************************************** #
    def path(self):
        """
        :return: instance(ObjPath)
        """
        return self._objPathObj

    def pathString(self):
        """
        :return: str(ObjPath)
        """
        return self._objPathObj.toString()

    def name(self):
        """
        :return: instance(ObjName)
        """
        return self._objPathObj.name()

    def nameString(self):
        """
        :return: str(ObjName)
        """
        return self._objPathObj.nameString()

    # parent ********************************************************************************************************* #
    def _obj__get_parent_exist_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    def isParent(self):
        """
        :return: bool
        """
        return self._obj__get_children_exist_()

    def hasParent(self, *args):
        """
        :param args:
            1.instance(Obj)
            2.instance(ObjPath)
            3.str(ObjPath)
        :return: bool
        """
        return self._obj__get_parent_exist_(*args)

    def _obj__set_parent_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    def setParent(self, *args):
        """
        :param args:
            1.instance(Obj)
            2.instance(ObjPath)
            3.str(ObjPath)
        :return:
        """
        self._obj__set_parent_(*args)

    def _obj__get_parent_obj_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    def parent(self):
        """
        :return: instance(Obj)
        """
        return self._obj__get_parent_obj_()

    # **************************************************************************************************************** #
    def _obj__get_parent_obj_list_(self, **kwargs):
        def rcsFnc_(obj_):
            if obj_.hasParent():
                _parentObj = obj_.parent()
                lis.append(_parentObj)
                rcsFnc_(_parentObj)

        if kwargs:
            pass

        lis = []
        rcsFnc_(self)
        return lis

    def allParents(self, **kwargs):
        """
        :param kwargs:
        :return: list(obj)
        """
        return self._obj__get_parent_obj_list_(**kwargs)

    # child ********************************************************************************************************** #
    def _obj__get_child_exist_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    def isChild(self):
        """
        :return: bool
        """
        return self._obj__get_parent_exist_()

    def hasChild(self, *args):
        """
        :return: bool
        """
        return self._obj__get_child_exist_(*args)

    def _obj__set_child_add_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    def addChild(self, *args):
        """
        :param args: instance(Obj)
        :return: None
        """
        self._obj__set_child_add_(*args)

    def _obj__get_child_obj_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    def child(self, *args):
        """
        :param args: = ObjStack.object(*args)
        :return: instance(Obj)
        """
        return self._obj__get_child_obj_(*args)

    def _obj_child__get_index_(self, *args):
        """
        replace method
        """
        raise NotImplementedError

    def childIndex(self, *args):
        """
        :param args: = ObjStack.objectIndex(*args)
        :return: int
        """
        return self._obj_child__get_index_(*args)

    # **************************************************************************************************************** #
    def _obj__get_children_exist_(self, *args, **kwargs):
        """
        replace method
        """
        raise NotImplementedError

    def hasChildren(self):
        """
        :return: bool
        """
        return self._obj__get_children_exist_()

    def _obj__get_child_obj_list_(self, *args, **kwargs):
        """
        replace method
        """
        raise NotImplementedError

    def children(self, *args, **kwargs):
        """
        :return: list(Obj)
        """
        return self._obj__get_child_obj_list_(*args, **kwargs)

    # **************************************************************************************************************** #
    def _obj__get_all_child_obj_list_(self, *args, **kwargs):
        def rcsFnc_(obj_):
            if obj_.hasParent():
                _childObjList = obj_._obj__get_child_obj_list_()
                for _childObj in _childObjList:
                    lis.append(_childObj)
                    rcsFnc_(_childObj)

        if kwargs:
            pass

        lis = []
        rcsFnc_(self)
        return lis

    def allChildren(self, *args, **kwargs):
        """
        :param args: = ObjStack.objects(*args, **kwargs)
        :param kwargs:
        :return: list
        """
        return self._obj__get_all_child_obj_list_(
            *args, **kwargs
        )

    # to string ****************************************************************************************************** #
    def toString(self):
        """
        :return: str(ObjPath)
        """
        return self.pathString()

    # proxy ********************************************************************************************************** #
    def _obj__get_proxy_obj_exist_(self, *args):
        return self._objProxyStackObj._obj_stack__get_obj_exist_(*args)

    def hasProxy(self, *args):
        """
        :param args: = ObjStack.hasObject(*args)
        :return: bool
        """
        return self._obj__get_proxy_obj_exist_(*args)

    def _obj__set_proxy_obj_add_(self, *args, **kwargs):
        if kwargs:
            pass
        if self._objProxyStackObj.hasObject(*args) is False:
            self._objProxyStackObj._obj_stack__set_obj_add_(*args)

    def addProxy(self, *args, **kwargs):
        """
        :param args: = ObjStack.add(*args, **kwargs)
        :param kwargs:
        :return: None
        """
        self._obj__set_proxy_obj_add_(*args, **kwargs)

    def proxies(self):
        """
        :return: list(object(proxy))
        """
        return self._objProxyStackObj._obj_stack__get_obj_list_()

    def proxy(self, *args):
        """
        :param args:
            1.instance(NamespacePath)
            2.str(NamespacePath)
        :return: instance(ObjProxy)
        """
        if args:
            if self._objProxyStackObj._obj_stack__get_obj_exist_(*args) is True:
                return self._objProxyStackObj._obj_stack__get_obj_(*args)
        return self._objProxyStackObj._obj_stack__get_obj_list_()[-1]

    def proxyNamespaceStrings(self):
        """
        :return: list(str(NamespacePath))
        """
        return self._objProxyStackObj.keys()


# port *************************************************************************************************************** #
# input port definition
class ItfGrhInportDef(object):
    def _initItfGrhInportDef(self):
        self._inportSourceOtportObj = None

    # method ********************************************************************************************************* #
    def _inport__get_source_exist_(self, *args, **kwargs):
        if args:
            otportObj = args[0]
            return otportObj == self._inportSourceOtportObj
        return self._inportSourceOtportObj is not None

    def hasSource(self, *args, **kwargs):
        """
        :param args:
            1.args[0]: object(Port)
        :return: bool
        """
        return self._inport__get_source_exist_(*args, **kwargs)

    def _inport__get_source_port_obj_(self, **kwargs):
        if self._inport__get_source_exist_() is True:
            return self._inportSourceOtportObj

    def source(self, **kwargs):
        """
        :param kwargs:
        :return: instance(Port)
        """
        return self._inport__get_source_port_obj_(**kwargs)

    # **************************************************************************************************************** #
    def _inport__set_source_port_obj_add_(self, *args):
        otportObj = args[0]

        if self._inport__get_source_exist_(otportObj) is False:
            inportObj = self
            inportObj._inport__set_source_port_obj_cache_add_(otportObj)
            otportObj._otport__set_target_port_obj_cache_add_(inportObj)

    def _inport__set_source_port_obj_cache_add_(self, *args):
        otportObj = args[0]
        if self._inport__get_source_exist_(otportObj) is False:
            self._inportSourceOtportObj = otportObj
        else:
            raise TypeError()

    def addSource(self, *args):
        """
        :param args:
            1.args[0]: object or "Port"
        :return: None
        """
        self._inport__set_source_port_obj_add_(*args)

    def isConnectFrom(self, *args):
        """
        = self.hasSource(*args)
        """
        return self._inport__get_source_exist_(*args)

    def connectFrom(self, *args):
        """
        = self.addSource(*args)
        """
        self._inport__set_source_port_obj_add_(*args)

    def _inport__set_source_port_obj_del_(self):
        if self._inportSourceOtportObj is not None:
            inportObj, otportObj = self, self._inportSourceOtportObj
            #
            otportObj._otport__set_target_port_obj_cache_del_(inportObj)
            inportObj._inport__set_source_port_obj_cache_del_()

    def _inport__set_source_port_obj_cache_del_(self):
        if self._inportSourceOtportObj is not None:
            self._inportSourceOtportObj = None

    def removeSource(self):
        """
        :return: None
        """
        self._inport__set_source_port_obj_del_()

    def disconnect(self):
        """
        = self.removeSource()
        """
        self._inport__set_source_port_obj_del_()


# output port definition
class ItfGrhOtportDef(object):
    def _initItfGrhOtportDef(self):
        self._otportTargetInportObjList = []

    # method ********************************************************************************************************* #
    def _otport__get_target_port_exist_(self, *args):
        if args:
            inportObj = args[0]
            return inportObj in self._otportTargetInportObjList
        return self._otport__get_target_ports_exist_()

    def _otport__get_target_port_obj_(self, *args):
        if isinstance(args[0], (int, float)):
            index = args[0]
            return self._otportTargetInportObjList[index]

    def hasTarget(self, *args):
        """
        :param args:
            1.instance(Port)
        :return: bool
        """
        return self._otport__get_target_port_exist_(*args)

    def isConnectTo(self, *args):
        """
        = self.hasTarget(*args)
        """
        return self._otport__get_target_port_exist_(*args)

    def target(self, *args):
        """
        :param args:
            1.int
        :return: *objects.Port()
        """
        return self._otport__get_target_port_obj_(*args)

    def _otport__set_target_port_obj_add_(self, *args, **kwargs):
        if kwargs:
            pass

        inportObj = args[0]
        # inport object is connect one otport only
        if inportObj._inport__get_source_exist_() is True:
            preSourceOtportObj = inportObj._inport__get_source_port_obj_()
            if self is preSourceOtportObj is False:
                inportObj._inport__set_source_port_obj_del_()

        if self._otport__get_target_port_exist_(inportObj) is False:
            otportObj = self
            otportObj._otport__set_target_port_obj_cache_add_(inportObj)
            inportObj._inport__set_source_port_obj_cache_add_(otportObj)

    def _otport__set_target_port_obj_cache_add_(self, *args):
        inportObj = args[0]
        if self._otport__get_target_port_exist_(inportObj) is False:
            self._otportTargetInportObjList.append(inportObj)
        else:
            raise

    def addTarget(self, *args, **kwargs):
        """
        :param args:
            1.args[0]: instance(Port)
        :return: None
        """
        self._otport__set_target_port_obj_add_(*args, **kwargs)

    def connectTo(self, *args, **kwargs):
        """
        = addTarget(*args, **kwargs)
        """
        self._otport__set_target_port_obj_add_(*args, **kwargs)

    def _otport__set_target_port_obj_del_(self, *args, **kwargs):
        if kwargs:
            pass

        inportObj = args[0]
        if inportObj in self._otportTargetInportObjList:
            otportObj = self
            #
            otportObj._otport__set_target_port_obj_cache_del_(inportObj)
            inportObj._inport__set_source_port_obj_cache_del_()

    def _otport__set_target_port_obj_cache_del_(self, *args):
        inportObj = args[0]
        if inportObj in self._otportTargetInportObjList:
            self._otportTargetInportObjList.remove(inportObj)

    def removeTarget(self, *args, **kwargs):
        """
        :param args:
            1.args[0]: instance(Port)
        :param kwargs:
        :return: None
        """
        self._otport__set_target_port_obj_del_(*args, **kwargs)

    def disconnectTo(self, *args, **kwargs):
        """
        = self.removeTarget(*args, **kwargs)
        """
        self._otport__set_target_port_obj_del_(*args, **kwargs)

    # **************************************************************************************************************** #
    def _otport__get_target_ports_exist_(self):
        return self._otportTargetInportObjList != []

    def _otport__get_target_port_obj_list_(self):
        return self._otportTargetInportObjList

    def hasTargets(self):
        """
        :return: bool
        """
        return self._otport__get_target_ports_exist_()

    def targets(self):
        """
        :return: list(instance(Port))
        """
        return self._otport__get_target_port_obj_list_()

    # **************************************************************************************************************** #
    def _otport__set_target_insert_(self, *args):
        inportObj, otportObj = args
        for portObj in self._otport__get_target_port_obj_list_():
            self._otport__set_target_port_obj_del_(portObj)
            otportObj._otport__set_target_port_obj_add_(portObj)

        self._otport__set_target_port_obj_add_(inportObj)

    def insertTarget(self, *args):
        """
        :param args:
            args[0]: instance(Port)
        :return:
        """
        self._otport__set_target_insert_(*args)


# assign port definition
class ItfGrhAsportDef(object):
    def _initItfGrhAsportDef(self, *args):
        objStackCls = args[0]
        self._asportAssignNodeStackObj = objStackCls(self)

    # method ********************************************************************************************************* #
    def _asport__get_assignment_node_exist_(self, *args):
        if args:
            self._asportAssignNodeStackObj.hasObject(*args)
        return self._asport__get_assignment_nodes_exist_()

    def hasAssignmentNode(self, *args):
        """
        :param args:
        :return: bool
        """
        return self._asport__get_assignment_node_exist_(*args)

    def _asport__set_assignment_node_obj_add_(self, *args):
        self._asportAssignNodeStackObj._obj_stack__set_obj_add_(*args)

    def addAssignmentNode(self, *args):
        """
        :param args:
            args[0]: instance(Node)
        :return:
        """
        self._asport__set_assignment_node_obj_add_(*args)

    def _asport__get_assignment_node_obj_(self, *args):
        return self._asportAssignNodeStackObj.object(*args)

    def assignmentNode(self, *args):
        """
        :param args: = ObjStack
        :return: instance(Node)
        """
        return self._asport__get_assignment_node_obj_(*args)

    def restoreAssignment(self):
        """
        :return: None
        """
        self._asportAssignNodeStackObj.restore()

    # **************************************************************************************************************** #
    def _asport__get_assignment_nodes_exist_(self, **kwargs):
        return self._asportAssignNodeStackObj.hasObjects(**kwargs)

    def hasAssignmentNodes(self, **kwargs):
        """
        :param kwargs:
        :return: bool
        """
        return self._asport__get_assignment_nodes_exist_(**kwargs)

    def _asport__get_assignment_node_obj_list_(self, **kwargs):
        return self._asportAssignNodeStackObj.objects(**kwargs)

    def assignmentNodes(self, **kwargs):
        """
        :param kwargs:
        :return: list(instance(Node))
        """
        return self._asport__get_assignment_node_obj_list_(**kwargs)


class ItfGrhPort(
    grhCfg.GrhUtility,
    ItfGrhObjDef,
    ItfGrhCacheObjDef,
    # port definition
    ItfGrhInportDef,
    ItfGrhOtportDef,
    ItfGrhAsportDef
):
    CLS_grh__port__porttype = None
    CLS_grh__port__datatype = None
    CLS_grh__port__assign = None

    VAR_grh__value_cls_dict = {}

    def _initItfGrhPort(self, *args, **kwargs):
        self._initItfGrhObjDef()
        self._initItfGrhCacheObjDef()
        #
        self._initItfGrhInportDef()
        self._initItfGrhOtportDef()
        self._initItfGrhAsportDef(
            self.CLS_grh__obj__obj_stack
        )
        #
        nodeArg, portArg = args
        # node
        nodeObj = nodeArg
        # port
        # port query
        if isinstance(portArg, ItfGrhPortQuery):
            self._portQueryObj = portArg
        # portpath
        elif isinstance(portArg, (str, unicode)):
            portpathStr = portArg
            nodeQueryObj = nodeObj.nodeQuery()
            portQueryCls = self.IST_grh__obj__query_builder.portQueryCls
            # registered port
            if nodeQueryObj.hasPortQuery(portpathStr):
                self._portQueryObj = nodeQueryObj.portQuery(portpathStr)
            # unregistered port
            else:
                self._portQueryObj = portQueryCls(nodeQueryObj, portpathStr)
        # port raw
        elif isinstance(portArg, dict):
            portRaw = portArg
            portpathStr = portArg[self.DEF_grh__key_portpath]
            nodeQueryObj = nodeObj.nodeQuery()
            portQueryCls = self.IST_grh__obj__query_builder.portQueryCls
            # registered port
            if nodeQueryObj.hasPortQuery(portpathStr):
                self._portQueryObj = nodeQueryObj.portQuery(portpathStr)
            # unregistered port
            else:
                self._portQueryObj = portQueryCls(nodeQueryObj, portRaw)
        else:
            raise TypeError()

        self._grh__port__set_build_(nodeObj, self._portQueryObj, **kwargs)

    # **************************************************************************************************************** #
    def _grh__port__set_build_(self, *args, **kwargs):
        if kwargs:
            pass

        nodeObj, portQueryObj = args

        self._nodeObj = nodeObj

        datatypeStr = portQueryObj.datatype

        self._obj__set_path_build_(
            nodeObj.path(),
            portQueryObj.portpath
        )

        self._grh__port__set_porttype_build_(portQueryObj.porttype)
        self._grh__port__set_datatype_build_(datatypeStr)
        self._grh__port__set_assign_build_(portQueryObj.assign)

        parentString = portQueryObj.parent
        self._obj__set_parent_(parentString)
        self._obj__set_children_build_(portQueryObj.children)

        valueCls = self._get_port_value_cls_(datatypeStr)
        if valueCls is not None:
            portrawString = portQueryObj.portraw

            self._set_port_value_build_(
                valueCls(portrawString)
            )

    # **************************************************************************************************************** #
    def _grh__port__get_node_cache_obj_(self, *args):
        return self.node()._node_cls__get_node_cache_obj_(*args)

    def _grh__port__get_port_cache_obj_(self, *args):
        return self.node()._node_cls__get_port_cache_obj_(*args)

    # **************************************************************************************************************** #
    def _grh__port__set_assign_build_(self, *args):
        self._assignObj = self.CLS_grh__port__assign(*args)

    def assign(self):
        return self._assignObj

    def assignString(self):
        return self._assignObj.toString()

    # **************************************************************************************************************** #
    def _grh__port__set_porttype_build_(self, *args):
        self._porttypeObj = self.CLS_grh__port__porttype(*args)

    def porttype(self):
        return self._porttypeObj

    def porttypeString(self):
        return self._porttypeObj.toString()

    # **************************************************************************************************************** #
    def _grh__port__set_datatype_build_(self, *args):
        self._portDatatypeObj = self.CLS_grh__port__datatype(*args)

    def datatype(self):
        return self._portDatatypeObj

    def datatypeString(self):
        return self._portDatatypeObj.toString()

    # **************************************************************************************************************** #
    def portpath(self):
        return self._objPathObj.portpath()

    def portpathString(self):
        return self._objPathObj.portpathString()

    def portname(self):
        return self._objPathObj.portname()

    def portnameString(self):
        return self._objPathObj.portnameString()

    # **************************************************************************************************************** #
    def isCompound(self):
        return self.porttypeString() in [
            u'compound'
        ]

    def isMultiple(self):
        return self.porttypeString() in [
            u'multiple'
        ]

    # **************************************************************************************************************** #
    def _grh__port__get_is_multi_root_(self):
        if self.hasParent() is False:
            return self.isMultiple()
        return False

    def _grh__port__get_is_multi_branch_(self):
        def rcsFnc_(portObj_):
            if portObj_.hasParent():
                _parentPortObj = portObj_.parent()
                if _parentPortObj.isMultiple():
                    return True
                return rcsFnc_(_parentPortObj)
            return False
        if self.isMultiple():
            return rcsFnc_(self)
        return False

    def _grh__port__get_is_multi_channel_(self):
        if self.hasParent():
            return self.parent().isMultiple()
        return False

    def _grh__port__get_multi_indexes_(self):
        """
        replace method
        """

    def _grh__port__get_multi_portpath_str_list_(self):
        """
        replace method
        """

    def isMultiRoot(self):
        return self._grh__port__get_is_multi_root_()

    def isMultiBranch(self):
        return self._grh__port__get_is_multi_branch_()

    def isMultiChannel(self):
        return self._grh__port__get_is_multi_channel_()

    def multiIndexes(self):
        return self._grh__port__get_multi_indexes_()

    def multiPortpaths(self):
        return self._grh__port__get_multi_portpath_str_list_()

    # **************************************************************************************************************** #
    def _grh__port__get_multi_parent_exist_(self):
        def rcsFnc_(portObj_):
            if portObj_.hasParent():
                _parentPortObj = portObj_.parent()
                if _parentPortObj.isMultiple():
                    return True
                return rcsFnc_(_parentPortObj)
            return False
        return rcsFnc_(self)

    def _grh__port__get_multi_parent_(self):
        def rcsFnc_(portObj_):
            if portObj_.hasParent():
                _parentPortObj = portObj_.parent()
                if _parentPortObj.isMultiple():
                    return _parentPortObj
                return rcsFnc_(_parentPortObj)
        return rcsFnc_(self)

    def hasMultiParent(self):
        return self._grh__port__get_multi_parent_exist_()

    def multiParent(self):
        return self._grh__port__get_multi_parent_()

    # **************************************************************************************************************** #
    def _grh__port__get_all_multi_parent_(self, *args):
        def rcsFnc_(lis_, portObj_):
            if portObj_.hasParent():
                _parentPortObj = portObj_.parent()
                if _parentPortObj.isMultiple():
                    lis_.append(_parentPortObj)
                rcsFnc_(lis_, _parentPortObj)

        lis = []
        if args:
            portObj = args[0]
        else:
            portObj = self

        rcsFnc_(lis, portObj)
        lis.reverse()
        return lis

    def allMultiParent(self):
        return self._grh__port__get_all_multi_parent_()

    # **************************************************************************************************************** #
    def multiChildren(self):
        pass

    # **************************************************************************************************************** #
    def isRampRoot(self):
        return self.porttypeString() == u'ramp'

    def isRampBranch(self):
        if self.hasParent():
            return self.parent().isRampRoot()
        return False

    # **************************************************************************************************************** #
    def isColorport(self):
        return self.porttypeString() in [
            u'color2',
            u'color3',
            u'color4'
        ]

    # **************************************************************************************************************** #
    def isFilename(self):
        return self.porttypeString() == u'filename'

    def isArray(self):
        return self.porttypeString() in [
            u'booleanarray',
            u'integerarray',
            u'floatarray',
            u'color2array',
            u'color3array',
            u'color4array',
            u'vector2array',
            u'vector3array',
            u'vector4array',
            u'stringarray'
        ]

    # **************************************************************************************************************** #
    def node(self):
        return self._nodeObj

    # **************************************************************************************************************** #
    def _get_port_value_cls_(self, *args):
        porttypeString = args[0]
        if porttypeString in self.VAR_grh__value_cls_dict:
            return self.VAR_grh__value_cls_dict[porttypeString]

    def _set_port_value_build_(self, *args):
        obj = args[0]
        self._valueObj = obj

    def setValue(self, valueObject):
        """
        :param valueObject: object of Value
        :return: None
        """
        self._set_port_value_build_(valueObject)

    def hasValue(self):
        """
        :return: bool
        """
        return self._valueObj is not None

    def value(self):
        """
        :return: object of Value
        """
        return self._valueObj

    # **************************************************************************************************************** #
    def isValueChanged(self):
        """
        :return: bool
        """
        return self.value().isDataChanged()

    # **************************************************************************************************************** #
    def _grh__port__get_portraw_(self, *args, **kwargs):
        return self._valueObj.raw()

    def _grh__port__set_portraw_(self, *args, **kwargs):
        self._valueObj.setRaw(*args, **kwargs)

    def setPortraw(self, *args, **kwargs):
        self._grh__port__set_portraw_(*args, **kwargs)

    def portraw(self, *args, **kwargs):
        return self._grh__port__get_portraw_(*args, **kwargs)

    # **************************************************************************************************************** #
    def _grh__port__get_portrawstr_(self):
        return self._valueObj.rawString()

    def _grh__port__set_portrawstr_(self, *args):
        self._valueObj.setRawString(*args)

    def setPortrawString(self, *args):
        self._grh__port__set_portrawstr_(*args)

    def portrawString(self):
        return self._grh__port__get_portrawstr_()

    # **************************************************************************************************************** #
    def _get_port_is_changed_(self):
        return self.isValueChanged() or self.hasSource()

    def isChanged(self):
        return self._get_port_is_changed_()

    # **************************************************************************************************************** #
    def _grh__port__get_given_(self):
        if self.hasSource() is True:
            return self.source()
        return self.value()

    def portgiven(self):
        return self._grh__port__get_given_()

    # **************************************************************************************************************** #
    def isPort(self):
        return self.hasParent() is False

    def isChannel(self):
        return self.hasParent()

    def isInport(self):
        return grhCfg.GrhPortAssignQuery.isInport(self.assignString())

    def isOtport(self):
        return grhCfg.GrhPortAssignQuery.isOtport(self.assignString())

    def isAsport(self):
        return grhCfg.GrhPortAssignQuery.isAsport(self.assignString())

    # **************************************************************************************************************** #
    def portQuery(self):
        return self._portQueryObj

    # **************************************************************************************************************** #
    def __str__(self):
        return u'{}(path="{}", porttype="{}", datatype="{}")'.format(
            self.__class__.__name__,
            self.pathString(),
            self.porttypeString(),
            self.datatypeString()
        )

    def __repr__(self):
        return self.__str__()

    # **************************************************************************************************************** #
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.toString() == other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() == other
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.toString() != other.toString()
        elif isinstance(other, (str, unicode)):
            return self.toString() != other
        return False


# node *************************************************************************************************************** #
class ItfGrhNode(
    grhCfg.GrhUtility,
    ItfGrhObjDef,
    ItfGrhCacheObjDef
):
    CLS_grh__node__typepath = None
    CLS_grh__node__datatype = None

    CLS_grh__node__port_stack = None
    CLS_grh__node__connector = None

    VAR_grh__node__port_cls_dict = {}

    def _initItfGrhNode(self, *args, **kwargs):
        self._initItfGrhObjDef()
        self._initItfGrhCacheObjDef()

        typepathArg, nodeArg = args[:2]

        if isinstance(typepathArg, self.IST_grh__obj__query_builder.nodeQueryCls):
            self._nodeQueryObj = typepathArg
        elif isinstance(typepathArg, dict):
            pass
        elif isinstance(typepathArg, (str, unicode)):
            typepathStr = typepathArg
            self._nodeQueryObj = self.IST_grh__obj__query_builder.nodeQuery(
                typepathStr
            )
        else:
            raise TypeError(
                u'''???'''
            )

        self._grh_node__set_build_(
            self._nodeQueryObj, nodeArg,
            **kwargs
        )

    # **************************************************************************************************************** #
    @classmethod
    def _node_cls__get_node_cache_obj_(cls, *args, **kwargs):
        nodeArg = args
        # ( nodepath, )
        if len(nodeArg) == 1:
            nodepathStr = nodeArg[0]
        # ( typepath, nodepath )
        elif len(nodeArg) == 2:
            nodepathStr = nodeArg[1]
        else:
            raise TypeError(
                u'''???'''
            )
        objArgs = nodepathStr, cls, nodeArg
        return cls.IST_grh__obj__queue._obj_queue__get_node_(*objArgs, **kwargs)

    @classmethod
    def _node_cls__get_port_cache_obj_(cls, *args):
        nodeArg, portArg = args
        # node object
        if isinstance(nodeArg, cls):
            nodeObj = nodeArg
        # ( nodepath, ) / ( category, nodepath )
        elif isinstance(nodeArg, (tuple, list)):
            nodeArgs = nodeArg
            nodeObj = cls._node_cls__get_node_cache_obj_(*nodeArgs)
        else:
            raise TypeError(
                u'''???'''
            )
        # ( portpath, assign )
        if isinstance(portArg, (tuple, list)):
            portpathStr, assignStr = portArg
        else:
            raise TypeError(
                u'''???'''
            )

        if nodeObj.hasPort(portpathStr, assign=assignStr):
            return nodeObj.port(portpathStr, assignStr)

        portCls = cls._node_cls__get_port_cls_(assignStr)
        return portCls(nodeObj, portpathStr)

    # **************************************************************************************************************** #
    @classmethod
    def _node_cls__get_port_cls_(cls, *args):
        assignStr = args[0]
        if assignStr in cls.VAR_grh__node__port_cls_dict:
            return cls.VAR_grh__node__port_cls_dict[assignStr]

    # **************************************************************************************************************** #
    @classmethod
    def _node_cls__get_port_raw_(cls, *args):
        pass

    # **************************************************************************************************************** #
    def _grh_node__set_build_(self, *args, **kwargs):
        if kwargs:
            pass
        nodeQueryObject, nodepathStr = args
        # covert to available path
        _nodepathStr = self.CLS_grh__obj__path(nodepathStr).toString()
        # exist
        if self.IST_grh__obj__queue.hasNode(_nodepathStr) is True:
            nodeObj = self.IST_grh__obj__queue._obj_queue__get_node_(_nodepathStr)

            self._objProxyStackObj = nodeObj._objProxyStackObj
            self._objPathObj = nodeObj._objPathObj

            self._nodeTypepathObj = nodeObj._nodeTypepathObj
            self._nodeDatatypeObj = nodeObj._nodeDatatypeObj

            self._nodeInportStackObj = nodeObj._nodeInportStackObj
            self._nodeOtportStackObj = nodeObj._nodeOtportStackObj
            self._nodeAsportStackObj = nodeObj._nodeAsportStackObj
        # non - exist
        else:
            self._obj__set_path_build_(_nodepathStr)

            self._grh_node__set_typepath_build_(nodeQueryObject.typepath)
            self._grh_node__set_datatype_build_(nodeQueryObject.datatype)

            self._nodeInportStackObj = self.CLS_grh__node__port_stack(self)
            self._nodeOtportStackObj = self.CLS_grh__node__port_stack(self)
            self._nodeAsportStackObj = self.CLS_grh__node__port_stack(self)

            self._grh_node__set_definition_ports_create_(self._nodeQueryObj, **kwargs)
            #
            self.IST_grh__obj__queue.addNode(self)

    # **************************************************************************************************************** #
    def _grh_node__set_typepath_build_(self, *args):
        self._nodeTypepathObj = self.CLS_grh__node__typepath(*args)

    def typepath(self):
        return self._nodeTypepathObj

    def typepathString(self):
        return self._nodeTypepathObj.toString()

    def typename(self):
        return self._nodeTypepathObj.name()

    def typenameString(self):
        return self._nodeTypepathObj.nameString()

    # compnode ******************************************************************************************************** #
    def _grh_node__get_is_compnode_(self):
        pass

    def isCompnode(self):
        return self._grh_node__get_is_compnode_()

    def _grh_node__get_is_transform_(self):
        pass

    def isTransform(self):
        return self._grh_node__get_is_transform_()

    def _grh_node__get_is_shape_(self):
        pass

    def isShape(self):
        return self._grh_node__get_is_shape_()

    def _grh_node__get_transform_obj_(self):
        pass

    def transform(self):
        return self._grh_node__get_transform_obj_()

    def _grh_node__get_shape_obj_list_(self):
        pass

    def shapes(self):
        return self._grh_node__get_shape_obj_list_()

    # **************************************************************************************************************** #
    def _grh_node__set_datatype_build_(self, *args):
        self._nodeDatatypeObj = self.CLS_grh__node__datatype(*args)

    def datatype(self):
        return self._nodeDatatypeObj

    def datatypeString(self):
        return self._nodeDatatypeObj.toString()

    # port *********************************************************************************************************** #
    def _grh_node__set_definition_ports_create_(self, *args, **kwargs):
        nodeQueryObject = args[0]
        nodeObj = self
        [self._grh_node__set_port_obj_create_(nodeObj, self._nodeInportStackObj, i, **kwargs) for i in nodeQueryObject.inportQueries()]
        [self._grh_node__set_port_obj_create_(nodeObj, self._nodeOtportStackObj, i, **kwargs) for i in nodeQueryObject.otportQueries()]
        [self._grh_node__set_port_obj_create_(nodeObj, self._nodeAsportStackObj, i, **kwargs) for i in nodeQueryObject.asportQueries()]

    def _grh_node__set_port_obj_create_(self, *args, **kwargs):
        nodeObj, portStackObj, portQueryObj = args
        portCls = self._node_cls__get_port_cls_(portQueryObj.assign)
        if portCls is not None:
            portObj = portCls(nodeObj, portQueryObj, **kwargs)
            portStackObj._obj_stack__set_obj_add_(portObj)

    # **************************************************************************************************************** #
    def _grh_node__set_customize_port_obj_create_(self, *args, **kwargs):
        portStackObjDict = {
            grhCfg.GrhPortAssignQuery.gnport: [self._nodeInportStackObj, self._nodeOtportStackObj],
            #
            grhCfg.GrhPortAssignQuery.inport: [self._nodeInportStackObj],
            grhCfg.GrhPortAssignQuery.otport: [self._nodeOtportStackObj],
            #
            grhCfg.GrhPortAssignQuery.asport: [self._nodeAsportStackObj],
            #
            grhCfg.GrhPortAssignQuery.property: [self._nodeInportStackObj],
            grhCfg.GrhPortAssignQuery.visibility: [self._nodeInportStackObj]
        }

        _ = args[0]

        if isinstance(_, dict):
            portRaw = args[0]

            portpathStr = portRaw[self.DEF_grh__key_portpath]
            assignStr = portRaw[self.DEF_grh__key_assign]
            if self._grh_node__get_port_exist_(portpathStr, assignStr) is False:
                portQueryCls = self.IST_grh__obj__query_builder.portQueryCls
                portQueryObj = portQueryCls(
                    self._nodeQueryObj, portRaw
                )
                if assignStr in portStackObjDict:
                    nodeObj = self
                    for portStackObj in portStackObjDict[assignStr]:
                        self._grh_node__set_port_obj_create_(
                            nodeObj,
                            portStackObj,
                            portQueryObj,
                            **kwargs
                        )

    # **************************************************************************************************************** #
    def _grh_node__get_ports_exist_(self, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_ports_exist_(
            (self._nodeInportStackObj, self._nodeOtportStackObj, self._nodeAsportStackObj),
            **kwargs
        )

    def hasPorts(self, **kwargs):
        return self._grh_node__get_ports_exist_(**kwargs)

    def _grh_node__get_port_obj_list_(self, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_list_(
            (self._nodeInportStackObj, self._nodeOtportStackObj, self._nodeAsportStackObj),
            **kwargs
        )

    def ports(self, **kwargs):
        """
        :return: list( *objects.Port )
        """
        return self._grh_node__get_port_obj_list_(**kwargs)

    # **************************************************************************************************************** #
    def _grh_node__get_port_exist_(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_exist_(
            (self._nodeInportStackObj, self._nodeOtportStackObj, self._nodeAsportStackObj),
            *args, **kwargs
        )

    def hasPort(self, *args, **kwargs):
        """
        :param args: bool
        :return:
        """
        return self._grh_node__get_port_exist_(*args, **kwargs)

    def _grh_node__get_port_obj_(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_(
            (self._nodeInportStackObj, self._nodeOtportStackObj, self._nodeAsportStackObj),
            *args, **kwargs
        )

    def port(self, *args, **kwargs):
        """
        :param args:
            1.str( "portpath" )
        :return: object
        """
        return self._grh_node__get_port_obj_(*args, **kwargs)

    # **************************************************************************************************************** #
    @classmethod
    def _node_cls__get_changed_port_obj_list_(cls, *args):
        def addFnc_(portObject_):
            if portObject_ not in lis:
                lis.append(portObject_)

        portObjects = args[0]
        lis = []
        for i in portObjects:
            if i.isChanged() is True:
                addFnc_(i)
        return lis

    @classmethod
    def _node_cls__set_filter_(cls, *args, **kwargs):
        def getIncludeVarFnc_(kwargs_):
            if kwargs_:
                if u'include' in kwargs_:
                    _ = kwargs_[u'include']
                    if isinstance(_, (str, unicode)):
                        return [_]
                    elif isinstance(_, (tuple, list)):
                        return list(_)

        def getExcludeVarFnc_(kwargs_):
            if kwargs_:
                if u'exclude' in kwargs_:
                    _ = kwargs_[u'exclude']
                    if isinstance(_, (str, unicode)):
                        return [_]
                    elif isinstance(_, (tuple, list)):
                        return list(_)

        ns = args[0]

        includeTypeList = getIncludeVarFnc_(kwargs)
        excludeTypeList = getExcludeVarFnc_(kwargs)

        if includeTypeList is not None:
            return [i for i in ns if i.typepathString() in includeTypeList]
        elif excludeTypeList is not None:
            return [i for i in ns if i.typepathString() not in excludeTypeList]
        return ns

    # **************************************************************************************************************** #
    def inports(self, **kwargs):
        return self._nodeInportStackObj._obj_stack__get_obj_list_(**kwargs)

    def hasInport(self, *args):
        return self._nodeInportStackObj._obj_stack__get_obj_exist_(*args)

    def inport(self, *args):
        portpathStr = args[0]
        if self._nodeInportStackObj._obj_stack__get_obj_exist_(*args) is False:
            raise TypeError(
                u'''node "{}"; inport "{}" is unregistered'''.format(
                    self.pathString(),
                    portpathStr
                )
            )
        return self._nodeInportStackObj._obj_stack__get_obj_(*args)

    def changedInport(self):
        """
        :return: list
        """
        return self._node_cls__get_changed_port_obj_list_(
            self._nodeInportStackObj.objects()
        )

    # **************************************************************************************************************** #
    def otports(self, **kwargs):
        return self._nodeOtportStackObj._obj_stack__get_obj_list_(**kwargs)

    def hasOtport(self, *args):
        return self._nodeOtportStackObj._obj_stack__get_obj_exist_(*args)

    def otport(self, *args):
        if args:
            portpathStr = args[0]
            if self._nodeOtportStackObj._obj_stack__get_obj_exist_(*args) is False:
                raise TypeError(
                    u'''node "{}"; otport "{}" is unregistered'''.format(
                        self.pathString(),
                        portpathStr
                    )
                )
            return self._nodeOtportStackObj._obj_stack__get_obj_(portpathStr)
        return self._nodeOtportStackObj.objects()[0]

    # **************************************************************************************************************** #
    def asports(self, **kwargs):
        return self._nodeAsportStackObj._obj_stack__get_obj_list_(**kwargs)

    def hasAsport(self, *args):
        return self._nodeAsportStackObj._obj_stack__get_obj_exist_(*args)

    def asport(self, *args):
        return self._nodeAsportStackObj._obj_stack__get_obj_(*args)

    # input connect port ********************************************************************************************* #
    def _grh_node__get_connect_input_port_obj_list_(self):
        lis = []
        for inportObj in self.inports():
            if inportObj.hasSource():
                lis.append(
                    inportObj.source()
                )
        return lis

    def inputPorts(self):
        return self._grh_node__get_connect_input_port_obj_list_()

    # input connect node ********************************************************************************************* #
    def _grh_node__get_connect_input_node_obj_list_(self, **kwargs):
        def addFnc_(obj):
            objKeyStr = obj.pathString()
            if objKeyStr not in keyStrList:
                keyStrList.append(objKeyStr)
                lis.append(obj)
                return True
            return False

        keyStrList = []
        lis = []

        for portObj in self.inports():
            if portObj.hasSource():
                addFnc_(
                    portObj.source().node()
                )

        return self._node_cls__set_filter_(lis, **kwargs)

    def inputNodes(self, **kwargs):
        return self._grh_node__get_connect_input_node_obj_list_(**kwargs)

    def _grh_node__get_all_connect_input_node_obj_list_(self, **kwargs):
        def addFnc_(obj):
            objKeyStr = obj.pathString()
            if objKeyStr not in keyStrList:
                keyStrList.append(objKeyStr)
                lis.append(obj)
                return True
            return False

        def rcsFnc_(nodeObject_):
            for _portObj in nodeObject_.inports():
                if _portObj.hasSource():
                    _nodeObj = _portObj.source().node()
                    if addFnc_(_nodeObj) is True:
                        rcsFnc_(_nodeObj)

        keyStrList = []
        lis = []
        rcsFnc_(self)
        return self._node_cls__set_filter_(lis, **kwargs)

    def allInputNodes(self, **kwargs):
        return self._grh_node__get_all_connect_input_node_obj_list_(**kwargs)

    # **************************************************************************************************************** #
    def inputConnections(self):
        lis = []
        for inportObj in self.inports():
            if inportObj.hasSource():
                sourceObject = inportObj.source()
                connection = (sourceObject, inportObj)
                if connection not in lis:
                    lis.append(connection)
        return lis

    def inputConnectors(self):
        return [
            self.CLS_grh__node__connector(*i)
            for i in self.inputConnections()
        ]

    # output connect node ******************************************************************************************** #
    def _grh_node__get_connect_output_node_obj_list_(self, **kwargs):
        def addFnc_(obj):
            objKeyStr = obj.pathString()
            if objKeyStr not in keyStrList:
                keyStrList.append(objKeyStr)
                lis.append(obj)
                return True
            return False

        keyStrList = []
        lis = []

        for portObj in self.otports():
            if portObj.hasTargets():
                for targetObj in portObj.targets():
                    _nodeObj = targetObj.node()
                    addFnc_(_nodeObj)

        return self._node_cls__set_filter_(lis, **kwargs)

    def outputNodes(self, **kwargs):
        return self._grh_node__get_connect_output_node_obj_list_(**kwargs)

    def _grh_node__get_all_connect_output_node_obj_list_(self, **kwargs):
        def addFnc_(obj):
            objKeyStr = obj.pathString()
            if objKeyStr not in keyStrList:
                keyStrList.append(objKeyStr)
                lis.append(obj)
                return True
            return False

        def rcsFnc_(nodeObject_):
            for _portObj in nodeObject_.otports():
                if _portObj.hasTargets():
                    for _targetObj in _portObj.targets():
                        _nodeObj = _targetObj.node()
                        if addFnc_(_nodeObj) is True:
                            rcsFnc_(_nodeObj)

        keyStrList = []
        lis = []
        rcsFnc_(self)
        return self._node_cls__set_filter_(lis, **kwargs)

    def allOutputNodes(self, **kwargs):
        return self._grh_node__get_all_connect_output_node_obj_list_(**kwargs)

    # **************************************************************************************************************** #
    def outputConnections(self):
        lis = []
        for otportObject in self.otports():
            if otportObject.hasTargets():
                for targetObject in otportObject.targets():
                    connection = (otportObject, targetObject)
                    if connection not in lis:
                        lis.append(connection)
        return lis

    def outputConnectors(self):
        return [
            self.CLS_grh__node__connector(*i)
            for i in self.outputConnections()
        ]

    # **************************************************************************************************************** #
    def nodeQuery(self):
        return self._nodeQueryObj

    # **************************************************************************************************************** #
    def _grh_node__get_override_port_obj_(self, *args, **kwargs):
        def getParentFnc_(nodeObj_, portpathStr_, ):
            for _nodeObj in nodeObj_.allParents():
                if _nodeObj.hasPort(portpathStr_, **kwargs) is True:
                    return _nodeObj.port(portpathStr_, **kwargs)

        portpathStr = args[0]

        # find self port
        if self.hasPort(portpathStr, **kwargs) is True:
            return self.port(portpathStr, **kwargs)
        # find nearest parent port
        return getParentFnc_(self, portpathStr)

    def overridePort(self, *args, **kwargs):
        return self._grh_node__get_override_port_obj_(*args, **kwargs)

    def _grh_node__get_override_port_obj_list_(self, *args, **kwargs):
        lis = []

        if isinstance(args[0], (str, unicode)):
            portpathStrList = list(args)
        elif isinstance(args[0], (tuple, list)):
            portpathStrList = args[0]
        else:
            raise TypeError()

        for portpathStr in portpathStrList:
            portObj = self.overridePort(portpathStr, **kwargs)
            if portObj is not None:
                lis.append(portObj)
        return lis

    def overridePorts(self, *args, **kwargs):
        return self._grh_node__get_override_port_obj_list_(*args, **kwargs)

    # **************************************************************************************************************** #
    def overrideInport(self, *args):
        return self.overridePort(
            *args,
            assign=grhCfg.GrhPortAssignQuery.inport
        )

    def overrideInports(self, *args):
        return self.overridePorts(
            *args,
            assign=grhCfg.GrhPortAssignQuery.inport
        )

    # **************************************************************************************************************** #
    def overrideOtport(self, *args):
        return self.overridePort(
            *args,
            assign=grhCfg.GrhPortAssignQuery.otport
        )

    def overrideOtports(self, *args):
        return self.overridePorts(
            *args,
            assign=grhCfg.GrhPortAssignQuery.otport
        )

    # **************************************************************************************************************** #
    def overrideAsport(self, *args):
        return self.overridePort(
            *args,
            assign=grhCfg.GrhPortAssignQuery.asport
        )

    def overrideAsports(self, *args):
        return self.overridePorts(
            *args,
            assign=grhCfg.GrhPortAssignQuery.asport
        )

    # **************************************************************************************************************** #
    def __str__(self):
        return u'{}(path="{}", typepath="{}")'.format(
            self.__class__.__name__,
            self.pathString(),
            self.typepathString()
         )

    def __repr__(self):
        return self.__str__()


class ItfGrhStage(grhCfg.GrhUtility):
    def _initTrsGrhStage(self, *args):
        pass

    def _stage__get_root_obj_(self):
        pass

    def root(self):
        pass

    def _stage__get_node_obj_list_(self):
        pass

    def nodes(self):
        pass


# connector ********************************************************************************************************** #
class ItfGrhConnector(grhCfg.GrhUtility):
    IST_grh__obj__queue = None

    def _initItfGrhConnector(self, *args):
        # source
        self._sourceObj = None
        # target
        self._targetObj = None

        self._set_connector_build_(*args)

    # **************************************************************************************************************** #
    def _set_connector_build_(self, *args):
        self._sourceObj, self._targetObj = args

    # **************************************************************************************************************** #
    def sourcePort(self):
        return self._sourceObj

    def sourceNode(self):
        return self.sourcePort().node()

    def targetPort(self):
        return self._targetObj

    def targetNode(self):
        return self.targetPort().node()

    def insertPort(self, portObj):
        self.sourcePort().removeTarget(self.targetPort())
        self.sourcePort().addTarget(portObj)
        portObj.addTarget(self.targetPort())

    def __str__(self):
        return '{}(source="{}", target="{}")'.format(
            self.__class__.__name__,
            self.sourcePort().pathString(),
            self.targetPort().pathString()
        )

    def __repr__(self):
        return self.__str__()


class ItfGrhGeometryAssign(grhCfg.GrhUtility):
    CLS_grh__assign__obj = None
    VAR_grh__assign__mesh_typepath_str = None
    VAR_grh__assign__material_typepath_str = None

    # noinspection PyUnusedLocal
    def _initItfGrhGeometryAssign(self, *args, **kwargs):
        self._grh__geometry_assign__set_build_(*args)

    def _grh__geometry_assign__set_build_(self, *args):
        pass

    def _grh__geometry_assign__get_virtual_relation_build_(self, *args):
        self._virtualRelationDict = args[0]

    def _grh__geometry_assign__set_material_relation_build_(self, *args):
        self._materialRelationDict = args[0]

    def _grh__geometry_assign__set_property_relation_build_(self, *args):
        self._propertyRelationDict = args[0]

    # geometry ******************************************************************************************************* #
    def _grh__geometry_assign__set_geometry_build_(self, *args):
        self._geometryPathStrList = args[0]

    def _grh__geometry_assign__get_geometry_obj_list_(self):
        return [
            self.CLS_grh__assign__obj._node_cls__get_node_cache_obj_(i)
            for i in self._geometryPathStrList
        ]

    def geometries(self):
        return self._grh__geometry_assign__get_geometry_obj_list_()

    # material ******************************************************************************************************* #
    def _grh__geometry_assign__set_material_build_(self, *args):
        self._materialPathList = args[0]

    def _grh__geometry_assign__get_material_obj_list_(self):
        return [
            self.CLS_grh__assign__obj._node_cls__get_node_cache_obj_(i)
            for i in self._materialPathList
        ]

    def materials(self):
        return self._grh__geometry_assign__get_material_obj_list_()

    def _grh__geometry_assign__get_relation_(self):
        return self._materialRelationDict

    def relation(self):
        return self._grh__geometry_assign__get_relation_()


# object proxy ******************************************************************************************************* #
class ItfGrhObjProxy(grhCfg.GrhUtility):
    CLS_grh__obj_proxy__bind_obj = None

    CLS_grh__obj_proxy__obj_namespace = None
    CLS_grh__obj_proxy__obj_path = None

    def _initItfGrhObjProxy(self, *args, **kwargs):
        # use as "node"
        if len(args) == 1:
            pathArg = args[0]
        # use as "port"
        elif len(args) == 2:
            pathArg = args[1]
        else:
            raise TypeError()
        # path
        # use as "port proxy" or "node proxy"
        if isinstance(pathArg, ItfGrhObjDef):
            obj = pathArg
            self._objPoxyPathObj = self.CLS_grh__obj_proxy__obj_path(
                obj.pathString()
            )
        # use as "node graph"
        elif isinstance(pathArg, ItfGrhNodeProxy):
            nodeProxyObj = pathArg
            self._objPoxyPathObj = self.CLS_grh__obj_proxy__obj_path(
                nodeProxyObj.bindPathString()
            )
        # ???
        elif isinstance(pathArg, (str, unicode)):
            self._objPoxyPathObj = self.CLS_grh__obj_proxy__obj_path(
                pathArg
            )
        else:
            raise TypeError(
                u'''???'''
            )

        # namespace
        namespaceArg = None
        if kwargs:
            if u'namespace' in kwargs:
                namespaceArg = kwargs[u'namespace']
        #
        if isinstance(namespaceArg, self.CLS_grh__obj_proxy__obj_namespace):
            self._namespaceObj = namespaceArg
        elif isinstance(namespaceArg, (str, unicode)):
            self._namespaceObj = self.CLS_grh__obj_proxy__obj_namespace(namespaceArg)
        elif namespaceArg is None:
            self._namespaceObj = self.CLS_grh__obj_proxy__obj_namespace()
        else:
            raise TypeError(
                u'''???'''
            )

    # **************************************************************************************************************** #
    def setPath(self, *args):
        pathObj = args[0]
        self._objPoxyPathObj = pathObj

    def path(self):
        return self._objPoxyPathObj

    def setPathString(self, *args):
        self._objPoxyPathObj.setRaw(*args)

    def pathString(self):
        return self._objPoxyPathObj.toString()

    # **************************************************************************************************************** #
    def setName(self, *args):
        pathObj = args[0]
        self._objPoxyPathObj = pathObj

    def name(self):
        return self._objPoxyPathObj

    def setNameString(self, *args):
        self._objPoxyPathObj.setRaw(*args)

    def nameString(self):
        return self._objPoxyPathObj.toString()

    # **************************************************************************************************************** #
    def _obj_proxy__set_namespace_obj_(self, *args):
        self._namespaceObj = args[0]

    def setNamespace(self, *args):
        self._obj_proxy__set_namespace_obj_(*args)

    def namespace(self):
        return self._namespaceObj

    # **************************************************************************************************************** #
    def _obj_proxy__set_namespace_str_(self, *args):
        self._namespaceObj.setRaw(*args)

    def setNamespaceString(self, *args):
        self._obj_proxy__set_namespace_str_(*args)

    def namespaceString(self):
        return self._namespaceObj.toString()

    # **************************************************************************************************************** #
    def _obj_proxy__get_bind_obj_(self):
        # noinspection PyUnresolvedReferences
        return self._bindObj

    def bindObject(self):
        return self._obj_proxy__get_bind_obj_()

    def _obj_proxy__get_bind_path_obj_(self):
        # noinspection PyUnresolvedReferences
        return self._bindObj.path()

    def bindPath(self):
        return self._obj_proxy__get_bind_path_obj_()

    def _obj_proxy__get_bind_path_str_(self):
        # noinspection PyUnresolvedReferences
        return self._bindObj.pathString()

    def bindPathString(self):
        return self._obj_proxy__get_bind_path_str_()

    # namespace ****************************************************************************************************** #
    @classmethod
    def _obj_proxy_cls__get_bind_obj_proxy_namespace_str_(cls, *args):  # bind
        objProxy = args[0]
        return objProxy.pathString()

    def bindNamespaceString(self):
        return self._obj_proxy_cls__get_bind_obj_proxy_namespace_str_(self)

    @classmethod
    def _obj_proxy_cls__get_connect_obj_proxy_namespace_str_(cls, *args):  # connect
        objProxy = args[0]
        return objProxy.namespaceString()

    def connectNamespaceString(self):
        return self._obj_proxy_cls__get_connect_obj_proxy_namespace_str_(self)

    # **************************************************************************************************************** #
    def toString(self):
        return self.pathString()


class ItfGrhPortProxy(ItfGrhObjProxy):
    def _initItfGrhPortProxy(self, *args, **kwargs):
        self._initItfGrhObjProxy(*args, **kwargs)
        # build
        self._port_proxy__set_build_(*args)

    def _port_proxy__set_build_(self, *args):
        nodeProxyRaw, portRaw = args
        self._bindNodeProxy = nodeProxyRaw
        self._bindObj = portRaw

        nodeProxyNamespaceObj = self._bindNodeProxy.namespace()
        self.path().nodepath().name().setNamespace(nodeProxyNamespaceObj)

        self._bindObj.addProxy(self)

    # bind object **************************************************************************************************** #
    def _obj_proxy__get_bind_obj_(self):
        return self._bindObj

    # bind node proxy ************************************************************************************************ #
    def bindNodeProxy(self):
        return self._bindNodeProxy

    # **************************************************************************************************************** #
    def sourceNamespaceString(self):
        return self._obj_proxy_cls__get_connect_obj_proxy_namespace_str_(self)

    # connect ******************************************************************************************************** #
    def _port_proxy__get_source_proxy_exist_(self):
        portObj = self.bindObject()
        if portObj.hasSource() is True:
            sourcePortObject = portObj.source()
            sourceNamespaceStr = self.sourceNamespaceString()
            return sourcePortObject.hasProxy(sourceNamespaceStr)

    def hasSourceProxy(self):
        return self._port_proxy__get_source_proxy_exist_()

    def _port_proxy__get_source_proxy_obj_(self):
        portObj = self.bindObject()
        if portObj.hasSource() is True:
            sourcePortObj = portObj.source()
            sourceNamespaceStr = self.sourceNamespaceString()
            if sourcePortObj.hasProxy(sourceNamespaceStr) is True:
                return sourcePortObj.proxy(sourceNamespaceStr)

    def sourceProxy(self):
        return self._port_proxy__get_source_proxy_obj_()

    # **************************************************************************************************************** #
    def bindPortgiven(self):
        portObj = self.bindObject()
        if portObj.hasSource() is True:
            sourcePortObj = portObj.source()
            sourceNamespaceStr = self.sourceNamespaceString()
            if sourcePortObj.hasProxy(sourceNamespaceStr) is True:
                sourcePortProxyObj = sourcePortObj.proxy(sourceNamespaceStr)
                return sourcePortProxyObj
        return portObj.value()


# node
class ItfGrhNodeProxy(ItfGrhObjProxy):
    CLS_grh__node_proxy__bind_port_proxy_stack = None
    VAR_grh__node_proxy__bind_port_proxy_cls_dict = {}

    CLS_grh__node_proxy__portset_stack = None
    CLS_grh__node_proxy__portset = None

    CLS_grh__node_proxy__input_graph_stack = None
    CLS_grh__node_proxy__input_graph = None

    CLS_grh__node_proxy__input_node_proxy_stack = None

    def _initItfGrhNodeProxy(self, *args, **kwargs):
        self._initItfGrhObjProxy(*args, **kwargs)
        # set namespace
        self._objPoxyPathObj.name().setNamespace(self._namespaceObj)
        # build
        self._node_proxy__set_build_(*args)

    def _node_proxy__set_build_(self, *args):
        self._node_proxy__set_bind_node_build_(*args)
        # bind port proxies
        self._node_proxy__set_bind_port_proxies_build_(self._bindObj)
        # input node graph
        self._node_proxy__set_input_node_graph_stack_build_()
        # input node proxy
        self._node_proxy__set_input_node_proxy_stack_build_()

    def _node_proxy__set_bind_node_build_(self, *args):
        nodeRaw = args[0]
        if isinstance(nodeRaw, self.CLS_grh__obj_proxy__bind_obj):
            self._bindObj = nodeRaw
        elif isinstance(nodeRaw, (str, unicode)):
            self._bindObj = self.CLS_grh__obj_proxy__bind_obj(*args)
        else:
            raise TypeError()
        self._bindObj.addProxy(self)

    # **************************************************************************************************************** #
    def _obj_proxy__set_namespace_obj_(self, *args):
        namespaceObj = args[0]
        newNamespaceStr = namespaceObj.toString()

        self._namespaceObj = namespaceObj
        # rename node namespace
        self._node_proxy__set_namespace_str_(newNamespaceStr)
        # rename ports namespace
        self._node_proxy__set_ports_namespace_str_(newNamespaceStr)

    # **************************************************************************************************************** #
    def _obj_proxy__set_namespace_str_(self, *args):
        newNamespaceStr = args[0]

        self._namespaceObj.setRaw(newNamespaceStr)
        # rename node namespace
        self._node_proxy__set_namespace_str_(newNamespaceStr)
        # rename ports namespace
        self._node_proxy__set_ports_namespace_str_(newNamespaceStr)

    # **************************************************************************************************************** #
    def _node_proxy__set_namespace_str_(self, *args):
        self._bindObj._objProxyStackObj._obj_stack__set_obj_rename_(self, *args)

    def _node_proxy__set_ports_namespace_str_(self, *args):
        newNamespaceStr = args[0]
        for portProxyObj in self.bindPortProxies():
            portObj = portProxyObj.bindObject()
            namespaceObj = portProxyObj.namespace()
            namespaceObj.setParentString(newNamespaceStr)
            portObj._objProxyStackObj._obj_stack__set_obj_rename_(
                portProxyObj,
                namespaceObj.toString()
            )

    # bind object **************************************************************************************************** #
    def _obj_proxy__get_bind_obj_(self):
        return self._bindObj

    # bind port ****************************************************************************************************** #
    def _node_proxy__get_bind_port_proxy_cls_(self, *args):
        assignStr = args[0]
        if assignStr in self.VAR_grh__node_proxy__bind_port_proxy_cls_dict:
            return self.VAR_grh__node_proxy__bind_port_proxy_cls_dict[assignStr]

    def _node_proxy__set_bind_port_proxies_build_(self, *args):
        def addFnc_(nodeProxyObj_, portObjs_, setObj_, portProxyNamespaceStr_):
            for _portObj in portObjs_:
                _assignStr = _portObj.assignString()
                _portProxyCls = self._node_proxy__get_bind_port_proxy_cls_(_assignStr)
                if _portProxyCls is not None:
                    _portProxyObj = _portProxyCls(
                        nodeProxyObj_,
                        _portObj,
                        namespace=portProxyNamespaceStr_
                    )
                    setObj_._obj_stack__set_obj_add_(_portProxyObj)

        nodeObj = args[0]

        bindPortProxyNamespaceStr = self.bindNamespaceString()

        self._bindInportProxyStackObj = self.CLS_grh__node_proxy__bind_port_proxy_stack(self)
        self._bindOtportProxyStackObj = self.CLS_grh__node_proxy__bind_port_proxy_stack(self)
        self._bindAsportProxyStackObj = self.CLS_grh__node_proxy__bind_port_proxy_stack(self)

        for portObjs, setObj in [
            (nodeObj.inports(), self._bindInportProxyStackObj),
            (nodeObj.otports(), self._bindOtportProxyStackObj),
            (nodeObj.asports(), self._bindAsportProxyStackObj)
        ]:
            addFnc_(
                self, portObjs, setObj,
                bindPortProxyNamespaceStr
            )

    def bindPortProxies(self, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_list_(
            (self._bindInportProxyStackObj, self._bindOtportProxyStackObj, self._bindAsportProxyStackObj),
            **kwargs
        )

    def hasBindPortProxy(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_exist_(
            (self._bindInportProxyStackObj, self._bindOtportProxyStackObj, self._bindAsportProxyStackObj),
            *args, **kwargs
        )

    def bindPortProxy(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_(
            (self._bindInportProxyStackObj, self._bindOtportProxyStackObj, self._bindAsportProxyStackObj),
            *args, **kwargs
        )

    def bindPort(self, *args, **kwargs):
        portProxyObj = self.bindPortProxy(*args, **kwargs)
        if portProxyObj:
            return portProxyObj.bindObject()

    # bind inport **************************************************************************************************** #
    def bindInportProxies(self):
        return self._bindInportProxyStackObj.objects()

    def hasBindInportProxy(self, *args):
        return self._bindInportProxyStackObj.hasObject(*args)

    def bindInportProxy(self, *args):
        return self._bindInportProxyStackObj.object(*args)

    def bindInport(self, *args):
        portProxyObj = self.bindInportProxy(*args)
        if portProxyObj:
            return portProxyObj.bindObject()

    def _node_proxy__get_changed_bind_inport_proxies_(self):
        lis = []
        portProxyObjs = self.bindInportProxies()
        if portProxyObjs:
            for portProxyObj in portProxyObjs:
                portObj = portProxyObj.bindObject()
                if portObj.isChanged():
                    lis.append(portProxyObj)
        return lis

    def changedBindInportProxies(self):
        return self._node_proxy__get_changed_bind_inport_proxies_()

    # bind otport **************************************************************************************************** #
    def bindOtportProxies(self):
        return self._bindOtportProxyStackObj.objects()

    def hasBindOtportProxy(self, *args):
        return self._bindOtportProxyStackObj.hasObject(*args)

    def bindOtportProxy(self, *args):
        return self._bindOtportProxyStackObj.object(*args)

    def bindOtport(self, *args):
        portProxyObj = self.bindOtportProxy(*args)
        if portProxyObj:
            return portProxyObj.bindObject()

    # bind asport **************************************************************************************************** #
    def bindAsportProxies(self):
        return self._bindAsportProxyStackObj.objects()

    def hasBindAsportProxy(self, *args):
        return self._bindAsportProxyStackObj.hasObject(*args)

    def bindAsportProxy(self, *args):
        return self._bindAsportProxyStackObj.object(*args)

    def bindAsport(self, *args):
        portProxyObj = self.bindAsportProxy(*args)
        if portProxyObj:
            return portProxyObj.bindObject()

    # bind portset *************************************************************************************************** #
    def bindPortsetNamespaceString(self):
        return self._obj_proxy_cls__get_bind_obj_proxy_namespace_str_(self)

    # input node graph *********************************************************************************************** #
    def _node_proxy__set_input_node_graph_stack_build_(self):
        self._inputNodeGraphStackObj = self.CLS_grh__node_proxy__input_graph_stack(self)

    # **************************************************************************************************************** #
    def inputNodeGraphNameString(self):
        nameObj = self.CLS_grh__obj_proxy__obj_path(self.bindPathString())
        nameObj.name().setNamespace(self.namespace())
        return nameObj.toString()

    # **************************************************************************************************************** #
    def _node_proxy__set_input_node_graph_obj_add_(self, *args):
        objProxyObj = args[0]
        nodeGraphNameStr = objProxyObj.inputNodeGraphNameString()
        if self._inputNodeGraphStackObj.hasObject(nodeGraphNameStr) is False:
            inputNodeGraphNamespaceStr = self.connectNamespaceString()
            # node graph
            nodeGraphObj = self.CLS_grh__node_proxy__input_graph(
                objProxyObj,
                namespace=inputNodeGraphNamespaceStr
            )
            self._inputNodeGraphStackObj.addObject(nodeGraphObj)
            return nodeGraphObj
        return self._inputNodeGraphStackObj.object(nodeGraphNameStr)

    def addInputNodeGraph(self, *args):
        self._node_proxy__set_input_node_graph_obj_add_(*args)

    def hasInputNodeGraphs(self):
        return self._inputNodeGraphStackObj.hasObjects()

    def inputNodeGraphs(self):
        return self._inputNodeGraphStackObj.objects()

    def hasInputNodeGraph(self, *args):
        return self._inputNodeGraphStackObj.hasObject(*args)

    def _node_proxy__get_input_node_graph_obj_(self, *args):
        if args:
            _ = args[0]
            if isinstance(_, (str, unicode)):
                keyStr = _
                if self._inputNodeGraphStackObj._obj_stack__get_obj_exist_(keyStr):
                    return self._inputNodeGraphStackObj._obj_stack__get_obj_(keyStr)
            elif isinstance(_, (int, float)):
                index = _
                if self._inputNodeGraphStackObj._obj_stack__get_obj_exist_(index):
                    return self._inputNodeGraphStackObj._obj_stack__get_obj_(index)
            elif isinstance(_, ItfGrhNodeProxy):
                objProxyObj = _
                return self._node_proxy__set_input_node_graph_obj_add_(objProxyObj)
        #
        objProxyObj = self
        return self._node_proxy__set_input_node_graph_obj_add_(objProxyObj)

    def inputNodeGraph(self, *args):
        return self._node_proxy__get_input_node_graph_obj_(*args)

    # input node proxy *********************************************************************************************** #
    def _node_proxy__set_input_node_proxy_stack_build_(self):
        if self.CLS_grh__node_proxy__input_node_proxy_stack is not None:
            self._inputNodeProxyObjStack = self.CLS_grh__node_proxy__input_node_proxy_stack(self)

    def _node_proxy__get_input_node_proxy_exist_(self, *args):
        return self._inputNodeProxyObjStack._obj_stack__get_obj_exist_(*args)

    def _node_proxy__set_input_node_connect_(self, *args):
        pass

    def _node_proxy__set_assignment_node_add_(self, *args):
        pass

    def _node_proxy__set_input_node_proxy_connect_(self, *args):
        _ = args[0]
        if isinstance(_, ItfGrhNodeProxy):
            nodeProxyObj = _
            if self._inputNodeProxyObjStack._obj_stack__get_obj_exist_(nodeProxyObj) is False:
                if nodeProxyObj.namespace().isRoot() is True:
                    connectNamespaceStr = self.connectNamespaceString()
                    nodeProxyObj.setNamespaceString(connectNamespaceStr)
                #
                self._inputNodeProxyObjStack._obj_stack__set_obj_add_(nodeProxyObj)
                # connect node
                self._node_proxy__set_input_node_connect_(nodeProxyObj)
                self._node_proxy__set_assignment_node_add_(nodeProxyObj)

    def connectNodeProxyFrom(self, *args):
        self._node_proxy__set_input_node_proxy_connect_(*args)

    def connectNodeProxyTo(self, *args):
        pass

    def _node_proxy__get_input_node_proxy_(self, *args):
        if self._inputNodeProxyObjStack._obj_stack__get_obj_exist_(*args) is True:
            return self._inputNodeProxyObjStack._obj_stack__get_obj_(*args)

    def inputNodeProxy(self, *args):
        return self._node_proxy__get_input_node_proxy_(*args)


# node graph ********************************************************************************************************* #
class ItfGrhNodeGraph(ItfGrhObjProxy):
    CLS_grh__node_graph__node_stack = None

    CLS_grh__node_graph__port_proxy_stack = None
    CLS_grh__node_graph__port_proxy = None

    def _initItfGrhNodeGraph(self, *args, **kwargs):
        self._initItfGrhObjProxy(*args, **kwargs)
        # set namespace
        self._objPoxyPathObj.name().setNamespace(self._namespaceObj)

        self._node_graph__set_build_(*args)

    # **************************************************************************************************************** #
    def _node_graph__set_build_(self, *args):
        outputNodeProxyObj = args[0]

        self._outputNodeProxyObj = outputNodeProxyObj
        self._bindObj = outputNodeProxyObj.bindObject()

        self._nodeGraphNodeStackObj = self.CLS_grh__node_graph__node_stack(self)
        self._nodeGraphOtportProxyStackObj = self.CLS_grh__node_graph__port_proxy_stack(self)

    # **************************************************************************************************************** #
    def _obj_proxy__get_bind_obj_(self):
        return self._bindObj

    # **************************************************************************************************************** #
    def outputNodeProxy(self):
        return self._outputNodeProxyObj

    # **************************************************************************************************************** #
    def _node_graph__get_bind_node_obj_list_(self):
        return self._bindObj.allInputNodes()

    def _node_graph__set_bind_node_add_(self, *args):
        nodeObj = args[0]

        if self._nodeGraphNodeStackObj.hasObject(nodeObj) is False:
            self._nodeGraphNodeStackObj.addObject(nodeObj)
            #
            bindNamespaceStr = self.bindNamespaceString()
            nodeObj.addProxy(
                bindNamespaceStr,
                self
            )

    def _node_graph__get_bind_port_obj_list_(self):
        return self._bindObj.inputPorts()

    def _node_graph__set_bind_port_add_(self, *args):
        portObj = args[0]

        portpathStr = portObj.pathString()
        if self._nodeGraphOtportProxyStackObj._obj_stack__get_obj_exist_(portpathStr) is False:
            bindNamespaceStr = self.bindNamespaceString()

            portProxyObj = self.CLS_grh__node_graph__port_proxy(
                self,
                portObj,
                namespace=bindNamespaceStr
            )

            # count = self._nodeGraphOtportProxyStackObj.objectsCount()
            # pathStr = u'output_{}'.format(count)
            # portProxyObj.setPathString(pathStr)

            self._nodeGraphOtportProxyStackObj._obj_stack__set_obj_add_(portpathStr, portProxyObj)

    def _node_graph__set_bind_obj_update_(self):
        # restore nodes
        self._nodeGraphNodeStackObj.restore()
        [self._node_graph__set_bind_node_add_(i) for i in self._node_graph__get_bind_node_obj_list_()]
        # restore ports
        self._nodeGraphOtportProxyStackObj.restore()
        [self._node_graph__set_bind_port_add_(i) for i in self._node_graph__get_bind_port_obj_list_()]

    # bind node ****************************************************************************************************** #
    def hasBindNodes(self):
        """
        :return: bool
        """
        return self._nodeGraphNodeStackObj.hasObjects()

    def bindNodes(self):
        """
        :return: list([<Node>, ...])
        """
        return self._nodeGraphNodeStackObj.objects()

    def bindNode(self, nodepathStr):
        """
        :param nodepathStr: str("nodepathStr")
        :return: *objects.Node()
        """
        return self._nodeGraphNodeStackObj._obj_stack__get_obj_(nodepathStr)

    def bindNodeCount(self):
        """
        :return: int
        """
        return self._nodeGraphNodeStackObj.objectsCount()

    # bind port ****************************************************************************************************** #
    def hasBindOtportProxies(self):
        """
        :return: bool
        """
        return self._nodeGraphOtportProxyStackObj.hasObjects()

    def bindOtportProxies(self):
        """
        :return: list(object or output, ...)
        """
        return self._nodeGraphOtportProxyStackObj.objects()

    def hasBindOtportProxy(self, *args):
        return self._nodeGraphOtportProxyStackObj.hasObject(*args)

    def bindOtportProxy(self, *args):
        """
        :param args:
            1: str
        :return: object of Output
        """
        return self._nodeGraphOtportProxyStackObj.object(*args)

    def bindOtport(self, *args):
        return self.bindOtportProxy(*args).bindObject()

    def bindOtportCount(self):
        return self._nodeGraphOtportProxyStackObj.objectsCount()


class ItfGrhNodeGraphPortProxy(ItfGrhPortProxy):
    def _initAbsItfNodeGraphOtportProxy(self, *args, **kwargs):
        self._initItfGrhPortProxy(*args, **kwargs)

    def bindNodeGraph(self):
        return self._bindNodeProxy


# translator object query cache ************************************************************************************** #
class ItfGrhTrsObjLoader(grhCfg.GrhUtility):
    VAR_grh__trs_obj_loader__node_property_key_list = []

    VAR_grh__trs_obj_loader__port_property_key_list = []

    def _initItfGrhTrsObjLoader(self, *args):
        pass

    @classmethod
    def _trs_grh__obj_loader_cls__get_definition_node_raw_(cls, *args):
        pass

    @classmethod
    def getDefinitionTrsNodeRaw(cls, *args):
        return cls._trs_grh__obj_loader_cls__get_definition_node_raw_(*args)


# translator object query cache ************************************************************************************** #
class ItfGrhTrsPortQueryraw(grhCfg.GrhUtility):
    def _initItfGrhPortQueryraw(self, *args):
        self._srcPortQueryrawObj, self._tgtPortQueryrawObj, self._outTrsPortRaw = args

        self._trs_port_queryraw__set_build_(self._outTrsPortRaw)

    def _trs_port_queryraw__set_build_(self, *args):
        self._trs_port_queryraw__set_properties_build_(*args)

    def _trs_port_queryraw__set_properties_build_(self, *args):
        raw = args[0]
        for k, v in raw.items():
            self.__dict__[k] = raw[k]

    # **************************************************************************************************************** #
    def outTrsPortRaw(self):
        return self._outTrsPortRaw

    # **************************************************************************************************************** #
    def srcPortQueryraw(self):
        return self._srcPortQueryrawObj

    def tgtPortQueryraw(self):
        return self._tgtPortQueryrawObj

    # **************************************************************************************************************** #
    def __str__(self):
        if hasattr(self, u'source_portpath') and hasattr(self, u'target_portpath'):
            return u'{}(source_portpath="{}", target_portpath="{}")'.format(
                self.__class__.__name__,
                self.source_portpath,
                self.target_portpath
            )
        return u''

    def __repr__(self):
        return self.__str__()


class ItfGrhTrsNodeQueryraw(grhCfg.GrhUtility):
    CLS_grh__trs_node_queryraw__port_stack = None
    CLS_grh__trs_node_queryraw__port = None

    def _initItfGrhTrsNodeQueryraw(self, *args):
        if isinstance(args[0], dict):
            self._trsObjRawDict = args[0]
            self._trs_node_queryraw__set_build_(self._trsObjRawDict)

    # **************************************************************************************************************** #
    def _trs_node_queryraw__set_build_(self, *args):
        nodeRaw = args[0]
        self._trs_node_queryraw__set_properties_build_(nodeRaw)
        portRaws = nodeRaw[self.DEF_grh__key_source_port]
        self._trs_grh__node_queryraw__set_ports_build_(portRaws)

    def _trs_node_queryraw__set_properties_build_(self, *args):
        raw = args[0]
        for k, v in raw.items():
            self.__dict__[k] = raw[k]

    def _trs_grh__node_queryraw__set_ports_build_(self, *args):
        outTrsPortRaws = args[0]

        self._trsInportQueryrawStackObj = self.CLS_grh__trs_node_queryraw__port_stack(self)
        self._trsOtportQueryrawStackObj = self.CLS_grh__trs_node_queryraw__port_stack(self)
        self._trsAsportQueryrawStackObj = self.CLS_grh__trs_node_queryraw__port_stack(self)
        for outTrsPortRaw in outTrsPortRaws:
            self._trs_grh__node_queryraw__set_port_create_(outTrsPortRaw)

    def _trs_grh__node_queryraw__set_port_create_(self, *args):
        outTrsPortRaw = args[0]

        srcPortQueryrawObj = outTrsPortRaw[self.DEF_grh__key_source]
        tgtPortQueryrawObj = outTrsPortRaw[self.DEF_grh__key_target]
        tgtAssignStr = tgtPortQueryrawObj.assign

        trsPortQueryrawObject = self.CLS_grh__trs_node_queryraw__port(
            srcPortQueryrawObj, tgtPortQueryrawObj,
            outTrsPortRaw
        )

        if grhCfg.GrhPortAssignQuery.isInport(tgtAssignStr):
            self._trsInportQueryrawStackObj._obj_stack__set_obj_add_(trsPortQueryrawObject)
        if grhCfg.GrhPortAssignQuery.isOtport(tgtAssignStr):
            self._trsOtportQueryrawStackObj._obj_stack__set_obj_add_(trsPortQueryrawObject)
        if grhCfg.GrhPortAssignQuery.isAsport(tgtAssignStr):
            self._trsAsportQueryrawStackObj._obj_stack__set_obj_add_(trsPortQueryrawObject)

    # **************************************************************************************************************** #
    def trsPortQueryraws(self, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_list_(
            (self._trsInportQueryrawStackObj, self._trsOtportQueryrawStackObj, self._trsAsportQueryrawStackObj),
            **kwargs
        )

    def hasTrsPortQueryraw(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_exist_(
            (self._trsInportQueryrawStackObj, self._trsOtportQueryrawStackObj, self._trsAsportQueryrawStackObj),
            *args, **kwargs
        )

    def trsPortQueryraw(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_(
            (self._trsInportQueryrawStackObj, self._trsOtportQueryrawStackObj, self._trsAsportQueryrawStackObj),
            *args, **kwargs
        )

    def outTrsPortRaw(self, *args, **kwargs):
        if self.hasTrsPortQueryraw(*args, **kwargs):
            return self.trsPortQueryraw(*args, **kwargs).outTrsPortRaw()

    # **************************************************************************************************************** #
    def trsInportQueryraws(self):
        return self._trsInportQueryrawStackObj.objects()

    def hasTrsInportQueryraw(self, *args):
        return self._trsInportQueryrawStackObj.hasObject(*args)

    def trsInportQueryraw(self, *args):
        if self.hasTrsInportQueryraw(*args):
            return self._trsInportQueryrawStackObj.object(*args)

    def outTrsInportRaw(self, *args):
        if self.hasTrsInportQueryraw(*args):
            return self._trsInportQueryrawStackObj.object(*args).outTrsPortRaw()

    # **************************************************************************************************************** #
    def trsOtportQueryraws(self):
        return self._trsOtportQueryrawStackObj.objects()

    def hasTrsOtportQueryraw(self, *args):
        return self._trsOtportQueryrawStackObj.hasObject(*args)

    def trsOtportQueryraw(self, *args):
        if self.hasTrsOtportQueryraw(*args):
            return self._trsOtportQueryrawStackObj.object(*args)

    def outTrsOtportRaw(self, *args):
        if self.hasTrsOtportQueryraw(*args):
            return self._trsOtportQueryrawStackObj.object(*args).outTrsPortRaw()

    # **************************************************************************************************************** #
    def trsAsportQueryraws(self):
        return self._trsAsportQueryrawStackObj.objects()

    def hasTrsAsportQueryraw(self, *args):
        return self._trsAsportQueryrawStackObj.hasObject(*args)

    def trsAsportQueryraw(self, *args):
        if self.hasTrsAsportQueryraw(*args):
            return self._trsAsportQueryrawStackObj.object(*args)

    def outTrsAsportRaw(self, *args):
        if self.hasTrsAsportQueryraw(*args):
            return self._trsAsportQueryrawStackObj.object(*args).outTrsPortRaw()

    # **************************************************************************************************************** #
    def outTrsNodeRaw(self):
        return self._trsObjRawDict

    def __str__(self):
        if hasattr(self, u'source_typepath') and hasattr(self, u'target_typepath'):
            return u'{}(source_typepath="{}", target_typepath="{}")'.format(
                self.__class__.__name__,
                self.source_typepath,
                self.target_typepath
            )
        return u''

    def __repr__(self):
        return self.__str__()


class ItfGrhTrsObjQueryrawCreator(grhCfg.GrhUtility):
    CLS_grh__trs_obj_queryraw_creator__node_stack = None
    CLS_grh__trs_obj_queryraw_creator__node = None

    CLS_grh__trs_obj_queryraw_creator__obj_loader = None

    IST_grh__trs_obj_queryraw_creator__source = None
    IST_grh__trs_obj_queryraw_creator__target = None

    VAR_grh__trs_obj_queryraw_creator__node_file = None
    VAR_grh__trs_obj_queryraw_creator__geometry_file = None
    VAR_grh__trs_obj_queryraw_creator__material_file = None
    VAR_grh__trs_output_file = None
    VAR_grh__trs_port_child_file = None

    VAR_grh__trs_custom_category_file = None
    VAR_grh__trs_custom_node_file = None

    # noinspection PyUnusedLocal
    def _initItfGrhTrsObjQueryBuilder(self, *args):
        self._trsNodeQueryrawStackObj = self.CLS_grh__trs_obj_queryraw_creator__node_stack(self)

        self._trs_obj_queryraw_creator__set_nodes_build_()

    # **************************************************************************************************************** #
    def _trs_obj_queryraw_creator__set_nodes_build_(self):
        self._origTrsNodeRawDict = self.CLS_ordered_dict()

        self._trs_obj_queryraw_creator__set_orig_raw_build_(
            self._origTrsNodeRawDict
        )

    def _trs_obj_queryraw_creator__set_orig_raw_build_(self, *args):
        """
        for override
        """

    # **************************************************************************************************************** #
    @classmethod
    def _trs_obj_queryraw_creator_cls__get_node_(cls, *args):
        setObj, getObjMtd, keyArgs = args
        if setObj._obj_stack__get_obj_exist_(*keyArgs):
            obj = setObj._obj_stack__get_obj_(*keyArgs)
        else:
            obj = getObjMtd(*keyArgs)
            setObj._obj_stack__set_obj_add_(obj)
        return obj

    def _trs_obj_queryraw_creator__get_node_raw_(self, *args):
        pass

    def _trs_obj_queryraw_creator__get_node_obj_(self, *args):
        srcTypepathStr = args[0]

        _trsObjRaw = self._trs_obj_queryraw_creator__get_node_raw_(srcTypepathStr)
        if _trsObjRaw:
            return self.CLS_grh__trs_obj_queryraw_creator__node(_trsObjRaw)
        else:
            print srcTypepathStr

    def _trs_obj_queryraw_creator__get_node_(self, *args):
        return self._trs_obj_queryraw_creator_cls__get_node_(
            self._trsNodeQueryrawStackObj,
            self._trs_obj_queryraw_creator__get_node_obj_,
            args
        )

    def trsNodeQueryraw(self, *args):
        return self._trs_obj_queryraw_creator__get_node_(*args)

    # **************************************************************************************************************** #
    def _trs_obj_queryraw_creator__get_port_(self, *args):
        srcTypepathStr, srcPortpathStr = args
        trsNodeQueryrawObject = self._trs_obj_queryraw_creator__get_node_(srcTypepathStr)
        return trsNodeQueryrawObject.trsPortQueryraw(srcPortpathStr)

    def trsPortQueryraw(self, *args):
        return self._trs_obj_queryraw_creator__get_port_(*args)

    # **************************************************************************************************************** #
    def _trs_obj_queryraw_creator__get_source_typepaths_(self):
        return self._origTrsNodeRawDict.keys()

    def srcTypepaths(self):
        return self._trs_obj_queryraw_creator__get_source_typepaths_()

    def _trs_obj_queryraw_creator__get_source_typepath_exist_(self, *args):
        srcTypepathStr = args[0]
        return srcTypepathStr in self._origTrsNodeRawDict

    def hasSrcTypepath(self, *args):
        return self._trs_obj_queryraw_creator__get_source_typepath_exist_(*args)


# translator object query ******************************************************************************************** #
class ItfGrhTrsPortQuery(grhCfg.GrhUtility):
    VAR_grh__portsep = None

    VAR_grh__trs_property_list = [
        grhCfg.GrhUtility.DEF_grh__key_source_portpath,
        grhCfg.GrhUtility.DEF_grh__key_target_portpath
    ]

    IST_grh__trs_obj__queryraw_creator = None

    def _initItfGrhTrsPortQuery(self, *args):
        if isinstance(args[0], ItfGrhTrsPortQueryraw):
            self._trsPortQueryrawObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            srcTypepathStr, srcPortpathStr = args
            self._trsPortQueryrawObj = self.IST_grh__trs_obj__queryraw_creator.trsPortQueryraw(
                srcTypepathStr, srcPortpathStr
            )
        else:
            raise TypeError()

        self._trsPortOutRaw = ''

        self._set_trs_port_query_build_()

    def _set_trs_port_query_build_(self):
        for k, v in self._trsPortQueryrawObj.outTrsPortRaw().items():
            self.__dict__[k] = v

    # **************************************************************************************************************** #
    def trsPortQueryraw(self):
        return self._trsPortQueryrawObj

    # **************************************************************************************************************** #
    @property
    def portsep(self):
        return self.VAR_grh__portsep

    # **************************************************************************************************************** #
    def __str__(self):
        if hasattr(self, u'source_portpath') and hasattr(self, u'target_portpath'):
            return u'{}(source_portpath="{}", target_portpath="{}")'.format(
                self.__class__.__name__,
                self.source_portpath,
                self.target_portpath
            )
        return u''

    def __repr__(self):
        return self.__str__()


class ItfGrhTrsNodeQuery(grhCfg.GrhUtility):
    CLS_grh__trs_port_query_set = None
    CLS_grh__trs_port_query = None

    IST_grh__trs_obj__queryraw_creator = None

    def _initItfGrhTrsNodeQuery(self, *args):
        self._srcGraphicNameString, self._tgtGraphicNameString = u'unknown', u'unknown'
        if isinstance(args[0], ItfGrhTrsNodeQueryraw):
            self._trsNodeQueryrawObj = args[0]
        elif isinstance(args[0], (str, unicode)):
            srcTypepathStr = args[0]
            self._trsNodeQueryrawObj = self.IST_grh__trs_obj__queryraw_creator.trsNodeQueryraw(
                srcTypepathStr
            )
            if len(args) == 3:
                self._srcGraphicNameString, self._tgtGraphicNameString = args[1:]
        else:
            raise TypeError()

        self._trsNodeQueryrawDict = self._trsNodeQueryrawObj.outTrsNodeRaw()

        self._srcPortpathDict = {}

        self._trs_node_query__set_properties_build_()

        self._trs_node_query__set_ports_build_()

        # bscMethods.PyMessage.traceResult(
        #     u'''create node translator query: "{} @ {}" > "{} @ {}"'''.format(
        #         self.__dict__[u'source_typepath'],  self._srcGraphicNameString,
        #         self.__dict__[u'target_typepath'], self._tgtGraphicNameString
        #     )
        # )

    def _trs_node_query__set_properties_build_(self):
        for k, v in self._trsNodeQueryrawObj.outTrsNodeRaw().items():
            self.__dict__[k] = v

    def _trs_node_query__set_ports_build_(self):
        self._trsInportQueryStackObj = self.CLS_grh__trs_port_query_set(self)
        [
            self._trs_node_query__set_port_build_(self._trsInportQueryStackObj, i)
            for i in self._trsNodeQueryrawObj.trsInportQueryraws()
        ]
        self._trsOtportQueryStackObj = self.CLS_grh__trs_port_query_set(self)
        [
            self._trs_node_query__set_port_build_(self._trsOtportQueryStackObj, i)
            for i in self._trsNodeQueryrawObj.trsOtportQueryraws()
        ]
        self._trsAsportQueryStackObj = self.CLS_grh__trs_port_query_set(self)
        [
            self._trs_node_query__set_port_build_(self._trsAsportQueryStackObj, i)
            for i in self._trsNodeQueryrawObj.trsAsportQueryraws()
        ]

    def _trs_node_query__set_port_build_(self, *args):
        trsPortQueryStackObj, trsPortQueryrawObj = args

        trsPortQueryObject = self.CLS_grh__trs_port_query(trsPortQueryrawObj)

        srcPortpathStr = trsPortQueryObject.source_portpath
        portnameString = srcPortpathStr.split(trsPortQueryObject.portsep)[-1]
        self._srcPortpathDict[portnameString] = srcPortpathStr

        trsPortQueryStackObj._obj_stack__set_obj_add_(trsPortQueryObject)

    # **************************************************************************************************************** #
    def _get_src_portpath_(self, *args):
        portpathStr = args[0]
        if portpathStr in self._srcPortpathDict:
            return self._srcPortpathDict[portpathStr]
        return portpathStr

    # **************************************************************************************************************** #
    def trsPortQueries(self, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_list_(
            (self._trsInportQueryStackObj, self._trsOtportQueryStackObj, self._trsAsportQueryStackObj),
            **kwargs
        )

    def hasTrsPortQuery(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_exist_(
            (self._trsInportQueryStackObj, self._trsOtportQueryStackObj, self._trsAsportQueryStackObj),
            *args, **kwargs
        )

    def trsPortQuery(self, *args, **kwargs):
        return grhMtdCore._Mtd_Node._node_cls__get_port_obj_(
            (self._trsInportQueryStackObj, self._trsOtportQueryStackObj, self._trsAsportQueryStackObj),
            *args, **kwargs
        )

    # **************************************************************************************************************** #
    def trsInportQueries(self):
        return self._trsInportQueryStackObj.objects()

    def hasTrsInportQuery(self, *args):
        return self._trsInportQueryStackObj.hasObject(
            self._get_src_portpath_(*args)
        )

    def trsInportQuery(self, *args):
        return self._trsInportQueryStackObj.object(
            self._get_src_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def trsOtportQueries(self):
        return self._trsOtportQueryStackObj.objects()

    def hasTrsOtportQuery(self, *args):
        return self._trsOtportQueryStackObj.hasObject(
            self._get_src_portpath_(*args)
        )

    def trsOtportQuery(self, *args):
        return self._trsOtportQueryStackObj.object(
            self._get_src_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def trsAsportQueries(self):
        return self._trsAsportQueryStackObj.objects()

    def hasTrsAsportQuery(self, *args):
        return self._trsAsportQueryStackObj.hasObject(
            self._get_src_portpath_(*args)
        )

    def trsAsportQuery(self, *args):
        return self._trsAsportQueryStackObj.object(
            self._get_src_portpath_(*args)
        )

    # **************************************************************************************************************** #
    def TrsNodeQueryraw(self):
        return self._trsNodeQueryrawDict

    # **************************************************************************************************************** #
    @property
    def targetPortRaw(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh__key_target_port,
            {}
        )

    @property
    def tgtPortdataRaw(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh__keyword_portraw_convert,
            {}
        )

    @property
    def customNode(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh__keyword__custom_node,
            {}
        )

    @property
    def createExpressionRaw(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh__keyword__create_expression,
            {}
        )

    @property
    def afterExpressionRaw(self):
        return self._trsNodeQueryrawDict.get(
            self.DEF_grh__keyword__after_expression,
            {}
        )

    def __str__(self):
        if hasattr(self, u'source_typepath') and hasattr(self, u'target_typepath'):
            return u'{}(source_typepath="{}", target_typepath="{}")'.format(
                self.__class__.__name__,
                self.source_typepath,
                self.target_typepath
            )
        return u''

    def __repr__(self):
        return self.__str__()


class ItfGrhTrsObjQueryBuilder(grhCfg.GrhUtility):
    CLS_grh__trs_node_query_set = None
    CLS_grh__trs_node_query = None

    # noinspection PyUnusedLocal
    def _initItfGrhTrsObjQueryBuilder(self, *args):
        self._srcGraphicNameString, self._tgtGraphicNameString = args

        self._trsNodeQueryStackObj = self.CLS_grh__trs_node_query_set(self)

    def _get_trs_node_query_(self, *args):
        srcTypepathStr = args[0]
        if self._trsNodeQueryStackObj._obj_stack__get_obj_exist_(srcTypepathStr):
            return self._trsNodeQueryStackObj._obj_stack__get_obj_(srcTypepathStr)

        obj = self.CLS_grh__trs_node_query(
            srcTypepathStr,
            self._srcGraphicNameString, self._tgtGraphicNameString
        )
        self._trsNodeQueryStackObj._obj_stack__set_obj_add_(obj)
        return obj

    def trsNodeQuery(self, *args):
        return self._get_trs_node_query_(*args)

    def _get_trs_port_query_(self, *args):
        pass

    def trsPortQuery(self, *args):
        return self._get_trs_port_query_(*args)

    def hasSrcTypepath(self, *args):
        queryrawCacheObject = self.CLS_grh__trs_node_query.IST_grh__trs_obj__queryraw_creator
        return queryrawCacheObject.hasSrcTypepath(*args)


# translator ********************************************************************************************************* #
class ItfGrhObjTranslator(grhCfg.GrhUtility):
    VAR_grh__obj_translator__channel_convert_dict = {}

    VAR_grh__obj_translator__src_node_pathsep = None
    VAR_grh__obj_translator__tgt_node_pathsep = None

    def _initItfGrhObjTranslator(self, *args):
        self._trsNodeObj, self._srcNodeObj, self._tgtNodeCls = args[:3]

        self._srcTypepathStr = self._srcNodeObj.typepathString()
        self._srcNodeStr = self._srcNodeObj.pathString()
        self._trsNodeQueryObj = self._trsNodeObj.IST_grh__trs_node__obj_query_builder.trsNodeQuery(self._srcTypepathStr)

        self._tgtTypepathStr = self._trsNodeQueryObj.target_typepath
        self._tgtNodeQueryObj = self._tgtNodeCls.IST_grh__obj__query_builder.nodeQuery(self._tgtTypepathStr)
        self._tgtNodeStr = self._obj_translator__get_tgt_path_(self._srcNodeStr)
        self._tgtNodeObj = self._obj_translator__get_tgt_obj_(self._tgtTypepathStr, self._tgtNodeStr)

        self._obj_translator__set_ports_()

        self._trs__set_tgt_custom_ports_()

    def _obj_translator__get_tgt_path_(self, srcNodeString):
        return srcNodeString.replace(
            self.VAR_grh__obj_translator__src_node_pathsep, self.VAR_grh__obj_translator__tgt_node_pathsep
        )

    def _obj_translator__get_tgt_obj_(self, tgtTypepathStr, tgtNodepathString):
        _nodeCls = self._tgtNodeCls
        objArgs = tgtNodepathString, _nodeCls, (tgtTypepathStr, tgtNodepathString)
        return _nodeCls.IST_grh__obj__queue._obj_queue__get_node_(*objArgs)

    def _obj_translator__get_tgt_port_source_obj_(self, srcTargetPortObj):
        srcPortObj = srcTargetPortObj.source()
        srcNodeObj = srcPortObj.node()

        srcNodepathStr = srcNodeObj.pathString()
        srcTypepathStr = srcNodeObj.typepathString()

        if self._trsNodeObj.IST_grh__trs_node__obj_query_builder.hasSrcTypepath(srcTypepathStr):
            trsNodeQueryObject = self._trsNodeObj.IST_grh__trs_node__obj_query_builder.trsNodeQuery(srcTypepathStr)
            tgtTypepathStr = trsNodeQueryObject.target_typepath

            srcPortpathStr = srcPortObj.portpathString()
            srcAssignString = srcPortObj.assignString()
            if trsNodeQueryObject.hasTrsPortQuery(srcPortpathStr, srcAssignString):
                trsPortQueryObject = trsNodeQueryObject.trsPortQuery(srcPortpathStr, srcAssignString)
                _tgtPortpathStr = trsPortQueryObject.target_portpath

                tgtNodepathString = self._obj_translator__get_tgt_path_(srcNodepathStr)
                tgtNodeObject = self._obj_translator__get_tgt_obj_(tgtTypepathStr, tgtNodepathString)
                tgtAssignStr = trsPortQueryObject.target.assign
                return tgtNodeObject.port(_tgtPortpathStr, tgtAssignStr)
            else:
                print srcPortObj.node().pathString(), srcPortpathStr, "A"
        else:
            print srcPortObj.node().pathString()

    def _obj_translator__set_ports_(self):
        for i in self._trsNodeQueryObj.trsInportQueries():
            self._obj_translator__set_port_value_(i)
            self._obj_translator__set_port_connection_(i)
        # for i in self._trsNodeQueryObj.trsAsportQueries():
        #     self._obj_translator__set_asport_assignment_(i)

    # **************************************************************************************************************** #
    def _obj_translator__set_port_value_(self, trsPortQueryObj):
        _srcPortpathStr = trsPortQueryObj.source_portpath
        _tgtAssignStr = trsPortQueryObj.target.assign
        if self._srcNodeObj.hasPort(_srcPortpathStr, assign=_tgtAssignStr):
            scrPortObject = self._srcNodeObj.port(_srcPortpathStr, assign=_tgtAssignStr)

            _tgtPortpathStr = trsPortQueryObj.target_portpath
            tgtAssignStr = trsPortQueryObj.target.assign

            tgtPortObj = self._tgtNodeObj.port(_tgtPortpathStr, tgtAssignStr)

            if tgtPortObj.isChannel() is False:
                self._obj_translator__set_port_portraw_(
                    trsPortQueryObj,
                    scrPortObject,
                    tgtPortObj
                )
        # else:
        #     bscMethods.PyMessage.traceWarning(
        #         u'Source Typepath "{}"; Port "{}" is Unregistered.'.format(
        #             self._srcTypepathStr,
        #             _srcPortpathStr
        #         )
        #     )

    def _obj_translator__set_port_portraw_(self, trsPortQueryObj, srcPortObj, tgtPortObj):
        srcPortraw = self._obj_translator__set_portraw_convert_(
            trsPortQueryObj, srcPortObj
        )
        #
        tgtPortObj.setPortraw(srcPortraw)

    @classmethod
    def _obj_translator__set_portraw_convert_(cls, trsPortQueryObj, srcPortObj):
        _srcPortraw = srcPortObj.portraw()
        if hasattr(trsPortQueryObj, u'portraw_convert'):
            _convertDict = trsPortQueryObj.portraw_convert
            # enumerate
            if u'enumerate' in _convertDict:
                _enumerateConvertRaw = _convertDict[u'enumerate']
                if isinstance(_enumerateConvertRaw, (tuple, list)):
                    if _srcPortraw is not None:
                        return _enumerateConvertRaw[_srcPortraw]
                elif isinstance(_enumerateConvertRaw, dict):
                    if _srcPortraw in _enumerateConvertRaw:
                        return _enumerateConvertRaw[_srcPortraw]
            # datatype
            if u'datatype' in _convertDict:
                _datatypeConvertDict = _convertDict[u'datatype']
                _sourceDatatype, _targetDatatype = _datatypeConvertDict[u'source'], _datatypeConvertDict[u'target']
                if (_sourceDatatype, _targetDatatype) == (u'float3array', u'floatarray'):
                    return [j for i in _srcPortraw for j in i]
        return _srcPortraw

    # connection ***************************************************************************************************** #
    def _obj_translator__set_port_connection_(self, trsPortQueryObj):
        _srcPortpathStr = trsPortQueryObj.source_portpath
        _tgtAssignStr = trsPortQueryObj.target.assign
        if self._srcNodeObj.hasPort(_srcPortpathStr, assign=_tgtAssignStr):
            _srcPortObj = self._srcNodeObj.port(_srcPortpathStr, assign=_tgtAssignStr)

            _tgtPortpathStr = trsPortQueryObj.target_portpath
            _tgtAssignStr = trsPortQueryObj.target.assign
            _tgtNodeObj = self._tgtNodeObj
            tgtPortObj = self._tgtNodeObj.port(_tgtPortpathStr, _tgtAssignStr)

            self._obj_translator__set_port_connection_source_(_srcPortObj, tgtPortObj)
        # else:
        #     bscMethods.PyMessage.traceWarning(
        #         u'Source Typepath "{}"; Port "{}" is Unregistered.'.format(
        #             self._srcCategoryStr,
        #             _srcPortpathStr
        #         )
        #     )

    def _obj_translator__set_port_connection_source_(self, srcPortObj, tgtPortObj):
        if srcPortObj.hasSource():
            tgtSourcePortObj = self._obj_translator__get_tgt_port_source_obj_(srcPortObj)
            if tgtSourcePortObj is not None:
                tgtTargetPortObject = tgtPortObj
                if tgtTargetPortObject.isChannel():
                    self._obj_translator__set_channel_connection_convert_(
                        tgtSourcePortObj, tgtTargetPortObject
                    )
                else:
                    tgtSourcePortObj.connectTo(tgtTargetPortObject)

    def _obj_translator__set_channel_connection_convert_(self, tgtSourcePortObj, tgtTargetPortObject):
        convertDict = self.VAR_grh__obj_translator__channel_convert_dict

        tgtTargetParentPortObject = tgtTargetPortObject.parent()
        tgtParentPorttypeString = tgtTargetParentPortObject.porttypeString()
        if tgtParentPorttypeString in convertDict:
            tgtAttrpathString = tgtTargetParentPortObject.pathString()
            tgtTypepathStr = convertDict[tgtParentPorttypeString][grhCfg.GrhNodeQuery.typepath]

            _tgtNodeString = u'{}__{}_0'.format(tgtAttrpathString.replace(self.DEF_grh__node_port_pathsep, u'__'), tgtTypepathStr)
            _tgtNodeObject = self._obj_translator__get_tgt_obj_(tgtTypepathStr, _tgtNodeString)

            _tgtNodeObject.otport().connectTo(tgtTargetParentPortObject)

            _tgtTargetChannelPortnameString = tgtTargetPortObject.portnameString()
            _tgtTargetChannelObject = _tgtNodeObject.inport(_tgtTargetChannelPortnameString)

            tgtSourcePortObj.connectTo(_tgtTargetChannelObject)

    # assignment ***************************************************************************************************** #
    def _obj_translator__set_asport_assignment_(self, trsPortQueryObj):
        _srcPortpathStr = trsPortQueryObj.source_portpath
        if self._srcNodeObj.hasAsport(_srcPortpathStr):
            _srcPortObj = self._srcNodeObj.asport(_srcPortpathStr)

    # **************************************************************************************************************** #
    def _trs__set_tgt_custom_ports_(self):
        targetPortRaw = self._trsNodeQueryObj.targetPortRaw
        if targetPortRaw:
            for k, v in targetPortRaw.items():
                portrawString = v[self.DEF_grh__key_portraw]
                self._tgtNodeObj.inport(k).setPortrawString(portrawString)

    def srcNode(self):
        return self._srcNodeObj

    def tgtNode(self):
        return self._tgtNodeObj


class ItfGrhTrsNode(
    grhCfg.GrhUtility,
    ItfGrhCacheObjDef
):
    CLS_grh__trs_node__src_node = None
    CLS_grh__trs_node__tgt_node = None

    CLS_grh__trs_node__obj_translator = None

    IST_grh__trs_node__obj_query_builder = None

    IST_grh__trs_node__obj_cache = None

    def _initItfGrhTrsNode(self, *args, **kwargs):
        self._grh__trs_node__set_build_(*args, **kwargs)

    def _grh__trs_node__set_build_(self, *args, **kwargs):
        if kwargs:
            pass

        srcNodepathStr = args[0]
        self._srcNodeObj = self.getSrcNode(srcNodepathStr)

        self._translatorObj = self.CLS_grh__trs_node__obj_translator(
            self,
            self._srcNodeObj,
            self.CLS_grh__trs_node__tgt_node
        )

        self._grh__trs_node__set_create_expressions_run_()

        if self.IST_grh__trs_node__obj_cache.hasNode(srcNodepathStr) is True:
            pass
        else:
            self.IST_grh__trs_node__obj_cache.addNode(self)

    def _grh__trs_node__set_create_expressions_run_(self):
        expressionDict = self._translatorObj._trsNodeQueryObj.createExpressionRaw
        self._grh__trs_node__set_expressions_run_(expressionDict)

    def _grh__trs_node__set_after_expressions_run_(self):
        expressionDict = self._translatorObj._trsNodeQueryObj.afterExpressionRaw
        self._grh__trs_node__set_expressions_run_(expressionDict)

    def _grh__trs_node__set_expressions_run_(self, expressionDict):
        if expressionDict:
            if self.DEF_grh__keyword__command in expressionDict:
                commands = expressionDict[self.DEF_grh__keyword__command]
                if commands:
                    cmdsStr = ';'.join(commands)
                    exec cmdsStr

    # **************************************************************************************************************** #
    def _cmd_set_node_insert_(self, outputSrcNodeObjects, tgtTargetOtportStr, tgtInportString, tgtOtportString):
        for srcNodeObj in outputSrcNodeObjects:
            trsNodeObject = self.getTrsNode(srcNodeObj.pathString())
            tgtNodeObject = trsNodeObject.tgtNode()

            copyTgtNodeString = u'{}__{}_0'.format(tgtNodeObject.pathString(), self.tgtNode().typepathString())
            copyTgtNodeObject = self.getTgtNode(self.tgtNode().typepathString(), copyTgtNodeString)

            [i.setPortrawString(self.tgtNode().inport(i.portpathString()).portrawString()) for i in copyTgtNodeObject.inports()]

            tgtNodeObject.otport(tgtTargetOtportStr).insertTarget(
                copyTgtNodeObject.inport(tgtInportString),
                copyTgtNodeObject.otport(tgtOtportString)
            )

    def _cmd_set_color_correct_insert_(self, portdataDict=None):
        tgtConnectors = self.tgtNode().outputConnectors()

        mtl_category_0 = u'color_correct'
        node_string_0 = u'{}__{}_0'.format(self.tgtNode().pathString(), mtl_category_0)

        _tgtColorCorrectObject = self.getTgtNode(mtl_category_0, node_string_0)

        for _tgtConnector in tgtConnectors:
            if _tgtConnector.sourcePort().isChannel() is False:
                _portObj = _tgtColorCorrectObject.otport()
            else:
                _dict = {
                    u'r': u'rgba.r',
                    u'g': u'rgba.g',
                    u'b': u'rgba.b',
                    u'a': u'rgba.a'
                }
                _portpathStr = _dict[_tgtConnector.sourcePort().portnameString()]
                _portObj = _tgtColorCorrectObject.otport(_portpathStr)

            _tgtConnector.insertPort(_portObj)

        self.tgtNode().otport().connectTo(_tgtColorCorrectObject.inport(u'input'))
        if portdataDict:
            for k, v in portdataDict.items():
                _tgtColorCorrectObject.inport(k).setPortraw(self.srcNode().inport(v).portraw())
        return _tgtColorCorrectObject

    def _cmd_set_multi_texture_covert_(self, filepathString):
        srcNodeObj = self.srcNode()
        if srcNodeObj.typepathString() == u'file':
            isUdim = True
            if filepathString:
                isSequence = srcNodeObj.inport(u'useFrameExtension').portraw()
                uvTilingMode = srcNodeObj.inport(u'uvTilingMode').portraw()
                dirnameString = bscMethods.OsFile.dirname(filepathString)
                basenameString = bscMethods.OsFile.basename(filepathString)
                #
                findKeys = self.MOD_re.findall(u'[0-9][0-9][0-9][0-9]', basenameString)
                if findKeys:
                    if u'<udim>' in basenameString.lower():
                        isUdim = False
                    elif not uvTilingMode == u'UDIM (Mari)':
                        isUdim = False
                    #
                    if isUdim:
                        basenameString = basenameString.replace(findKeys[-1], u'<udim>')
                    elif isSequence:
                        basenameString = basenameString.replace(findKeys[-1], u'<f>')
                    #
                    filepathString = bscMethods.OsPath.composeBy(dirnameString, basenameString)
        return filepathString

    def getSrcNodes(self, **kwargs):
        return self.srcObjectQueue().nodes(**kwargs)

    def getTgtNodes(self, **kwargs):
        return self.tgtObjectQueue().nodes(**kwargs)

    # **************************************************************************************************************** #
    def srcObjectQueue(self):
        return self.CLS_grh__trs_node__src_node.IST_grh__obj__queue

    def tgtObjectQueue(self):
        return self.CLS_grh__trs_node__tgt_node.IST_grh__obj__queue

    # **************************************************************************************************************** #
    def typepathString(self):
        return self._srcNodeObj.typepathString()

    def pathString(self):
        return self._srcNodeObj.pathString()

    # **************************************************************************************************************** #
    @classmethod
    def _trs_node_cls__get_node_obj_(cls, nodeCls, cacheObj, *args):
        nodeArg = args
        # ( nodepath, )
        if len(nodeArg) == 1:
            nodepathStr = nodeArg[0]
        # ( typepath, nodepath )
        elif len(nodeArg) == 2:
            nodepathStr = nodeArg[1]
        else:
            raise TypeError(
                u'''???'''
            )
        #
        objArgs = nodepathStr, nodeCls, nodeArg
        return cacheObj._obj_queue__get_node_(*objArgs)

    def getTrsNode(self, *args):
        return self._trs_node_cls__get_node_obj_(
            self.__class__,
            self.IST_grh__trs_node__obj_cache,
            *args
        )

    def getSrcNode(self, *args):
        return self._trs_node_cls__get_node_obj_(
            self.CLS_grh__trs_node__src_node,
            self.CLS_grh__trs_node__src_node.IST_grh__obj__queue,
            *args
        )

    def getTgtNode(self, *args):
        return self._trs_node_cls__get_node_obj_(
            self.CLS_grh__trs_node__tgt_node,
            self.CLS_grh__trs_node__tgt_node.IST_grh__obj__queue,
            *args
        )

    # **************************************************************************************************************** #
    def trsNodeQuery(self):
        return self._translatorObj._trsNodeQueryObj

    def trsPortQuery(self, *args):
        return self.trsNodeQuery().trsPortQuery(*args)

    # **************************************************************************************************************** #
    def srcNode(self):
        return self._srcNodeObj

    def srcInport(self, *args):
        return self.srcNode().inport(*args)

    # **************************************************************************************************************** #
    def tgtNode(self):
        return self._translatorObj.tgtNode()

    def tgtInport(self, *args):
        return self.tgtNode().inport(
            self.trsPortQuery(*args).target_portpath
        )

    # **************************************************************************************************************** #
    def toString(self):
        return self._srcNodeObj.toString()

    # **************************************************************************************************************** #
    def __str__(self):
        return self.tgtNode().__str__()


# ******************************************************************************************************************** #
class ItfGrhNodeTrsRawLoader(grhCfg.GrhUtility):
    pass


# node proxy translate *********************************************************************************************** #
class ItfGrhTrsNodeProxy(grhCfg.GrhUtility):
    CLS_grh__trs_node_proxy__trs_node = None

    CLS_grh__trs_node_proxy__tgt_node_proxy = None

    def _initItfGrhTrsNodeProxy(self, *args, **kwargs):
        # node
        self._trsNodeObj = self._grh__trs_node_proxy__get_trs_node_cache_obj_(
            *args
        )

        self._srcNodeObj = self._trsNodeObj.srcNode()
        self._tgtNodeObj = self._trsNodeObj.tgtNode()
        # node proxy
        namespaceArg = None
        if kwargs:
            if u'namespace' in kwargs:
                namespaceArg = kwargs[u'namespace']
        self._tgtNodeProxyObj = self.CLS_grh__trs_node_proxy__tgt_node_proxy(
            self._tgtNodeObj,
            namespace=namespaceArg
        )

    def _grh__grh__trs_node_proxy__get_trs_node_cache_obj_exist_(self, nodepathArg):
        objCache = self.CLS_grh__trs_node_proxy__trs_node.IST_grh__trs_node__obj_cache
        return objCache.hasNode(
            nodepathArg
        )

    def _grh__trs_node_proxy__get_trs_node_cache_obj_(self, *args):
        srcNodepathStr = args[0]

        objCache = self.CLS_grh__trs_node_proxy__trs_node.IST_grh__trs_node__obj_cache
        objArgs = srcNodepathStr, self.CLS_grh__trs_node_proxy__trs_node, (srcNodepathStr,)
        return objCache._obj_queue__get_node_(*objArgs)

    def getTrsNode(self, *args):
        return self._grh__trs_node_proxy__get_trs_node_cache_obj_(*args)

    def trsNode(self):
        return self._trsNodeObj

    def trsNodeQuery(self):
        return self.CLS_grh__trs_node_proxy__trs_node.IST_grh__trs_node__obj_query_builder.trsNodeQuery(
            self._srcNodeObj.typepathString()
        )

    def srcNode(self):
        return self._srcNodeObj

    def tgtNodeProxy(self):
        return self._tgtNodeProxyObj

    def tgtNode(self):
        return self._tgtNodeObj

    def __str__(self):
        return self.tgtNodeProxy().__str__()
