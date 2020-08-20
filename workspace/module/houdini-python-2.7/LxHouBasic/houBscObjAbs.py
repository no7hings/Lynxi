# coding:utf-8
from LxBasic import bscMethods

from LxGraphic import grhCfg, grhObjItf, grhObjAbs

from . import houBscCfg, houBscMtdCore, houBscMethods

from .houBscMethods import _houBscMtdMtx


class AbsHouBasic(houBscCfg.HouBscUtility):
    pass


# ******************************************************************************************************************** #
class AbsHouObjLoader(
    AbsHouBasic,
    grhObjAbs.AbsGrhObjLoader
):
    def _initAbsHoObjLoader(self, *args):
        self._initAbsGrhObjLoader(*args)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__set_node_raw_build_(cls, *args):
        out_nodeRawDict, typepathStr = args
        # property
        out_nodeRawDict[cls.DEF_grh__key_node_typepath] = typepathStr
        out_nodeRawDict[cls.DEF_grh__key_node_datatype] = None
        # port
        _out_portRawList = []
        out_nodeRawDict[cls.DEF_grh__key_port] = _out_portRawList
        cls._obj_loader_cls__set_ports_add_(
            _out_portRawList, typepathStr
        )

    @classmethod
    def _obj_loader_cls__set_ports_add_(cls, *args):
        out_portRawList, typepathStr = args

        nt = cls.MOD_hou.nodeType(typepathStr)

        ps = nt.parmTemplates()
        for p in ps:
            cls._obj_loader_cls__set_port_add_(out_portRawList, p)

    @classmethod
    def _obj_loader_cls__set_port_add_(cls, *args):
        out_portRawList, parmTemplateObj = args

        _portpathStr = parmTemplateObj.name()
        if parmTemplateObj.type().name() == cls.MOD_hou.parmTemplateType.FolderSet.name():
            pass
        if parmTemplateObj.type().name() == cls.MOD_hou.parmTemplateType.Menu.name():
            pass
        if cls._obj_loader_cls__get_port_is_compound_(parmTemplateObj) is True:
            cls._obj_loader_cls__set_port_compound_add_(out_portRawList, parmTemplateObj)
        else:
            _datatypeStr = cls._obj_loader_cls__get_port_datatype_(parmTemplateObj)
            if _datatypeStr is not None:
                _assignStr = grhCfg.GrhPortAssignQuery.inport
                _childObjPathList = []
                # add parent first
                cls._obj_loader_cls__set_port_raw_add_(
                    out_portRawList,
                    portpath=_portpathStr,
                    porttype=_datatypeStr,
                    datatype=_datatypeStr,
                    assign=_assignStr,
                    children=_childObjPathList
                )

                cls._obj_loader_cls__set_port_children_add_(
                    out_portRawList,
                    _childObjPathList,
                    _assignStr,
                    parmTemplateObj
                )

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_port_format_(cls, string):
        if '#' in string:
            return string.replace('#', ''), string.replace('#', '{}')
        return string, None

    @classmethod
    def _obj_loader_cls__set_port_children_add_(cls, *args):
        out_portRawList, portChildStrList, parentAssignStr, parmTemplateObj = args
        if cls._obj_loader_cls__get_port_is_ramp_(parmTemplateObj):
            cls._obj_loader_cls__set_port_ramp_children_add_(
                out_portRawList,
                portChildStrList,
                parentAssignStr,
                parmTemplateObj
            )
        else:
            cls._obj_loader_cls__set_port_common_children_add_(
                out_portRawList,
                portChildStrList,
                parentAssignStr,
                parmTemplateObj
            )

    @classmethod
    def _obj_loader_cls__set_port_ramp_children_add_(cls, *args):
        out_portRawList, portChildStrList, parentAssignStr, parentParmTemplateObj = args

        if parentAssignStr == cls.DEF_grh__keyword__gnport:
            _assignStr = cls.DEF_grh__keyword__gnport_channel
        if parentAssignStr == cls.DEF_grh__keyword__inport:
            _assignStr = cls.DEF_grh__keyword__inport_channel
        elif parentAssignStr == cls.DEF_grh__keyword__otport:
            _assignStr = cls.DEF_grh__keyword__otport_channel
        else:
            raise TypeError()

        parentPortpathString = parentParmTemplateObj.name()
        rampTypeString = parentParmTemplateObj.parmType().name()
        _child_list = cls.DEF_hou__port_ramp_child_dict[rampTypeString]
        for i in _child_list:
            formatString = i[cls.DEF_grh__key_format]
            _portpathStr = formatString.format(
                **{
                    cls.DEF_grh__key_portpath: parentPortpathString
                }
            )
            _datatypeStr = i[cls.DEF_grh__key_porttype]
            cls._obj_loader_cls__set_port_raw_add_(
                out_portRawList,
                portpath=_portpathStr,
                porttype=_datatypeStr,
                datatype=_datatypeStr,
                assign=_assignStr,
                parent=parentPortpathString,
                children=[]
            )

            portChildStrList.append(_portpathStr)

    @classmethod
    def _obj_loader_cls__set_port_common_children_add_(cls, *args):
        out_portRawList, portChildStrList, parentAssignStr, parentParmTemplateObj = args

        parentPortpathString = parentParmTemplateObj.name()
        datatypeString = parentParmTemplateObj.dataType().name()
        schemeString = parentParmTemplateObj.namingScheme().name()
        childCount = parentParmTemplateObj.numComponents()

        if parentAssignStr == cls.DEF_grh__keyword__gnport:
            _assignStr = cls.DEF_grh__keyword__gnport_channel
        if parentAssignStr == cls.DEF_grh__keyword__inport:
            _assignStr = cls.DEF_grh__keyword__inport_channel
        elif parentAssignStr == cls.DEF_grh__keyword__otport:
            _assignStr = cls.DEF_grh__keyword__otport_channel
        else:
            raise TypeError()

        _dict = cls.DEF_hou__port_child_dict
        if childCount > 1:
            if schemeString in _dict:
                origChildPortRaw = _dict[schemeString]
                if isinstance(origChildPortRaw, (tuple, list)):
                    for index, i in enumerate(origChildPortRaw):
                        _formatString = i
                        _portpathStr = _formatString.format(
                            **{
                                cls.DEF_grh__key_portpath: parentPortpathString
                            }
                        )
                        _datatypeStr = cls.DEF_hou__port_datatype_dict_1[datatypeString]
                        cls._obj_loader_cls__set_port_raw_add_(
                            out_portRawList,
                            portpath=_portpathStr,
                            porttype=_datatypeStr,
                            datatype=_datatypeStr,
                            assign=_assignStr,
                            parent=parentPortpathString,
                            children=[]
                        )
                        portChildStrList.append(_portpathStr)
                elif isinstance(origChildPortRaw, (str, unicode)):
                    for index in xrange(childCount):
                        _formatString = origChildPortRaw

                        _portpathStr = _formatString.format(
                            **{
                                cls.DEF_grh__key_portpath: parentPortpathString,
                                cls.DEF_grh__key_index: index + 1
                            }
                        )
                        _datatypeStr = cls.DEF_hou__port_datatype_dict_1[datatypeString]
                        cls._obj_loader_cls__set_port_raw_add_(
                            out_portRawList,
                            portpath=_portpathStr,
                            porttype=_datatypeStr,
                            datatype=_datatypeStr,
                            assign=_assignStr,
                            parent=parentPortpathString,
                            children=[]
                        )

                        portChildStrList.append(_portpathStr)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_port_datatype_(cls, parmTemplateObj):
        dict_0 = cls.DEF_hou__port_datatype_dict_0

        portpathString = parmTemplateObj.name()
        typeString = parmTemplateObj.type().name()
        datatypeString = parmTemplateObj.dataType().name()
        schemeString = parmTemplateObj.namingScheme().name()
        childCount = parmTemplateObj.numComponents()
        if typeString in dict_0:
            if childCount == 1:
                return dict_0[typeString]
            else:
                dict_1 = cls.DEF_hou__port_datatype_dict_1
                dict_2 = cls.DEF_hou__port_datatype_dict_2
                if schemeString in dict_2:
                    _porttypeString = dict_1[datatypeString]
                    porttypeString = dict_2[schemeString].format(
                        **{
                            cls.DEF_grh__key_portpath: portpathString,
                            cls.DEF_grh__key_porttype: _porttypeString,
                            cls.DEF_grh__key_portsize: childCount
                        }
                    )
                    return porttypeString

    @classmethod
    def _obj_loader_cls__get_port_is_compound_(cls, parmTemplateObj):
        # noinspection PyUnresolvedReferences
        if parmTemplateObj.type().name() == cls.MOD_hou.parmTemplateType.Folder.name():
            return True
        return False

    @classmethod
    def _obj_loader_cls__get_port_is_multiple_(cls, parmTemplateObj):
        # noinspection PyUnresolvedReferences
        if parmTemplateObj.type().name() == cls.MOD_hou.parmTemplateType.Folder.name():
            # noinspection PyUnresolvedReferences
            if parmTemplateObj.folderType().name() in [
                cls.MOD_hou.folderType.MultiparmBlock.name()
            ]:
                return True
            return False
        return False

    @classmethod
    def _obj_loader_cls__get_port_is_ramp_(cls, parmTemplateObj):
        # noinspection PyUnresolvedReferences
        if parmTemplateObj.type().name() == cls.MOD_hou.parmTemplateType.Ramp.name():
            return True
        return False

    @classmethod
    def _obj_loader_cls__get_is_vop_(cls, nodeObj):
        if nodeObj.type().category().name() == cls.MOD_hou.vopNodeTypeCategory().name():
            return True
        return False

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_compound_port_porttype_(cls, parmTemplateObj):
        dict_0 = cls.DEF_hou__compound_port_datatype_dict_0
        typeString = parmTemplateObj.type().name()
        if typeString in dict_0:
            return dict_0[typeString]

    @classmethod
    def _obj_loader_cls__set_port_compound_add_(cls, *args):
        def rcsFnc_(parmTemplateObj_, parentPortRaw_):
            if cls._obj_loader_cls__get_port_is_compound_(parmTemplateObj_) is True:
                if parentPortRaw_ is not None:
                    _parentPortpathStr = parentPortRaw_[cls.DEF_grh__key_portpath]
                else:
                    _parentPortpathStr = None
                if cls._obj_loader_cls__get_port_is_multiple_(parmTemplateObj_) is True:
                    _porttypeStr = u'multiple'
                else:
                    _porttypeStr = u'compound'

                _portpathStr, _formatStr = cls._obj_loader_cls__get_port_format_(
                    parmTemplateObj_.name()
                )
                _assignStr = grhCfg.GrhPortAssignQuery.inport
                _childObjPathList = []
                _ps = parmTemplateObj_.parmTemplates()

                _portRaw = cls._obj_loader_cls__set_port_raw_add_(
                    out_portRawList,
                    portpath=_portpathStr,
                    porttype=_porttypeStr,
                    datatype=_porttypeStr,
                    assign=_assignStr,
                    format=_formatStr,
                    parent=_parentPortpathStr,
                    children=_childObjPathList
                )
                for _p in _ps:
                    _childObjPathList.append(_p.name())
                    rcsFnc_(_p, _portRaw)
            else:
                if parentPortRaw_ is not None:
                    _parentPortpathStr = parentPortRaw_[cls.DEF_grh__key_portpath]
                else:
                    _parentPortpathStr = None

                _porttypeString = cls._obj_loader_cls__get_compound_port_porttype_(parmTemplateObj_)
                if _porttypeString is not None:
                    _portpathStr, _formatStr = cls._obj_loader_cls__get_port_format_(
                        parmTemplateObj_.name()
                    )
                    _assignStr = grhCfg.GrhPortAssignQuery.inport
                    _parentPortnameString = None
                    _childObjPathList = []
                    # add parent first
                    cls._obj_loader_cls__set_port_raw_add_(
                        out_portRawList,
                        portpath=_portpathStr,
                        porttype=_porttypeString,
                        datatype=_porttypeString,
                        assign=_assignStr,
                        format=_formatStr,
                        parent=_parentPortpathStr,
                        children=_childObjPathList
                    )

                    cls._obj_loader_cls__set_port_children_add_(
                        out_portRawList,
                        _childObjPathList,
                        _assignStr,
                        parmTemplateObj_
                    )

        out_portRawList, parmTemplateObj = args
        rcsFnc_(parmTemplateObj, None)

    @classmethod
    def _obj_loader_cls__get_inport_compound_raws_(cls, nodepathStr):
        portRawLis = []

        n = cls.MOD_hou.node(nodepathStr)
        nt = n.type()
        ps = nt.parmTemplates()
        for p in ps:
            if cls._obj_loader_cls__get_port_is_compound_(p) is True:
                cls._obj_loader_cls__set_port_compound_add_(portRawLis, p)

        return portRawLis

    @classmethod
    def _grh__obj_loader_cls__get_customize_vlport_port_raws_(cls, *args, **kwargs):
        def addFnc_(porttype_, portpath_, assign_, parent_, children_):
            _portDict = cls._obj_loader_cls__set_port_raw_add_(
                lis,
                portpath=portpath_,
                porttype=porttype_,
                datatype=porttype_,
                assign=assign_,
                parent=parent_,
                children=children_
            )
            lis.append(_portDict)
            return _portDict

        lis = []

        nodepathStr = args[0]
        if kwargs:
            if u'virtual' in kwargs:
                if kwargs[u'virtual'] is True:
                    nodepathStr = kwargs[u'virtualPath']
        n = cls.MOD_hou.node(nodepathStr)
        if 'pattern' in kwargs:
            ps = n.globParms(kwargs['pattern'])
        else:
            ps = n.parms()
        if ps:
            dict0 = cls.DEF_hou__port_otport_dict_0
            dict1 = cls.DEF_hou__port_otport_dict_1
            for p in ps:
                portpathStr = p.name()
                _datatypeString = ''

                if portpathStr in dict0:
                    portRaw0 = dict0[portpathStr]
                    _portpathStr = portRaw0[cls.DEF_grh__key_portpath]
                    porttypeString = portRaw0[cls.DEF_grh__key_porttype]
                    assignString = portRaw0[cls.DEF_grh__key_assign]
                    parentPortnameString = portRaw0[cls.DEF_grh__key_parent]
                    childPortpathStrList = portRaw0[cls.DEF_grh__key_children]
                    addFnc_(
                        porttypeString,
                        _portpathStr,
                        assignString,
                        parentPortnameString,
                        childPortpathStrList
                    )
                elif portpathStr in dict1:
                    portRaw1 = dict1[portpathStr]
                    _portpathStr = portRaw1[cls.DEF_grh__key_portpath]
                    porttypeString = portRaw1[cls.DEF_grh__key_porttype]
                    assignString = portRaw1[cls.DEF_grh__key_assign]
                    parentPortnameString = ps[0]
                    childPortpathStrList = portRaw1[cls.DEF_grh__key_children]
                    addFnc_(
                        porttypeString,
                        _portpathStr,
                        assignString,
                        parentPortnameString,
                        childPortpathStrList
                    )
                else:
                    _portpathStr = portpathStr
                    assignString = grhCfg.GrhPortAssignQuery.otport
                    parentPortnameString = None
                    childPortpathStrList = []
                    addFnc_(
                        _datatypeString,
                        _portpathStr,
                        assignString,
                        parentPortnameString,
                        childPortpathStrList
                    )

        return lis

    @classmethod
    def _grh__obj_loader_cls__get_customize_inport_port_raws_(cls, *args, **kwargs):
        def addFnc_(porttype_, portpath_, assign_, parent_, children_):
            _portDict = cls._obj_loader_cls__set_port_raw_add_(
                lis,
                portpath=portpath_,
                porttype=porttype_,
                datatype=porttype_,
                assign=assign_,
                parent=parent_,
                children=children_
            )
            lis.append(_portDict)
            return _portDict

        lis = []

        nodepathStr = args[0]
        if kwargs:
            if u'virtual' in kwargs:
                if kwargs[u'virtual'] is True:
                    nodepathStr = kwargs[u'virtualPath']
        n = cls.MOD_hou.node(nodepathStr)
        ps = n.inputNames()
        if cls._obj_loader_cls__get_is_vop_(n) is True:
            dts = n.outputDataTypes()
        else:
            dts = None
        if ps:
            for portpathStr in ps:
                index = n.outputIndex(portpathStr)
                if dts:
                    _datatypeString = dts[index]
                else:
                    _datatypeString = ''

                _portpathStr = portpathStr
                porttypeString = ''

                assignString = grhCfg.GrhPortAssignQuery.inport
                parentPortnameString = None
                childPortpathStrList = []
                addFnc_(
                    porttypeString,
                    _portpathStr,
                    assignString,
                    parentPortnameString,
                    childPortpathStrList
                )

        return lis

    @classmethod
    def _grh__obj_loader_cls__get_customize_otport_port_raws_(cls, *args, **kwargs):
        def addFnc_(porttype_, portpath_, assign_, parent_, children_):
            _portDict = cls._obj_loader_cls__set_port_raw_add_(
                lis,
                portpath=portpath_,
                porttype=porttype_,
                datatype=porttype_,
                assign=assign_,
                parent=parent_,
                children=children_
            )
            lis.append(_portDict)
            return _portDict

        lis = []

        nodepathStr = args[0]
        if kwargs:
            if u'virtual' in kwargs:
                if kwargs[u'virtual'] is True:
                    nodepathStr = kwargs[u'virtualPath']
        n = cls.MOD_hou.node(nodepathStr)
        ps = n.outputNames()
        if cls._obj_loader_cls__get_is_vop_(n) is True:
            dts = n.outputDataTypes()
        else:
            dts = None
        if ps:
            dict0 = cls.DEF_hou__port_otport_dict_0
            dict1 = cls.DEF_hou__port_otport_dict_1
            for portpathStr in ps:
                index = n.outputIndex(portpathStr)
                if dts:
                    _datatypeString = dts[index]
                else:
                    _datatypeString = ''

                if portpathStr in dict0:
                    portRaw0 = dict0[portpathStr]
                    _portpathStr = portRaw0[cls.DEF_grh__key_portpath]
                    porttypeString = portRaw0[cls.DEF_grh__key_porttype]
                    assignString = portRaw0[cls.DEF_grh__key_assign]
                    parentPortnameString = portRaw0[cls.DEF_grh__key_parent]
                    childPortpathStrList = portRaw0[cls.DEF_grh__key_children]
                    addFnc_(
                        porttypeString,
                        _portpathStr,
                        assignString,
                        parentPortnameString,
                        childPortpathStrList
                    )
                elif portpathStr in dict1:
                    portRaw1 = dict1[portpathStr]
                    _portpathStr = portRaw1[cls.DEF_grh__key_portpath]
                    porttypeString = portRaw1[cls.DEF_grh__key_porttype]
                    assignString = portRaw1[cls.DEF_grh__key_assign]
                    parentPortnameString = ps[0]
                    childPortpathStrList = portRaw1[cls.DEF_grh__key_children]
                    addFnc_(
                        porttypeString,
                        _portpathStr,
                        assignString,
                        parentPortnameString,
                        childPortpathStrList
                    )
                else:
                    _portpathStr = portpathStr
                    assignString = grhCfg.GrhPortAssignQuery.otport
                    parentPortnameString = None
                    childPortpathStrList = []
                    addFnc_(
                        _datatypeString,
                        _portpathStr,
                        assignString,
                        parentPortnameString,
                        childPortpathStrList
                    )

        return lis

    # **************************************************************************************************************** #
    @classmethod
    def _grh__obj_loader_cls__get_port_exist_(cls, *args):
        nodepathStr, portpathStr = args
        n = cls.MOD_hou.node(nodepathStr)
        if n is not None:
            # is parameter
            p = n.parm(portpathStr)
            if p is not None:
                return True
            # is connector
            elif portpathStr in n.inputNames() or portpathStr in n.outputNames():
                return True
            return False
        return False

    @classmethod
    def _grh__obj_loader_cls__get_port_source_exist_(cls, nodepathStr, portpathStr):
        n = cls.MOD_hou.node(nodepathStr)
        i = n.inputIndex(portpathStr)
        if i >= 0:
            cs = n.inputConnectors()[i]
            return cs != ()
        return False

    @classmethod
    def _obj_loader_cls__get_port_source_str_(cls, nodepathStr, portpathStr):
        n = cls.MOD_hou.node(nodepathStr)
        i = n.inputIndex(portpathStr)
        if i >= 0:
            cs = n.inputConnectors()[i]
            if cs:
                c = cs[0]
                return c.inputNode().path(), c.inputName()

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_port_target_exist_(cls, nodepathStr, portpathStr):
        n = cls.MOD_hou.node(nodepathStr)
        i = n.outputIndex(portpathStr)
        if i >= 0:
            cs = n.outputConnectors()[i]
            return cs != ()
        return False

    @classmethod
    def _obj_loader_cls__get_port_target_str_list_(cls, nodepathStr, portpathStr):
        lis = []
        n = cls.MOD_hou.node(nodepathStr)
        i = n.outputIndex(portpathStr)
        if i >= 0:
            cs = n.outputConnectors()[i]
            if cs:
                for c in cs:
                    lis.append(
                        (c.outputNode().path(), c.outputName())
                    )
        return lis

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_port_portraw_(cls, nodepathStr, portpathStr, **kwargs):
        if kwargs:
            pass

        n = cls.MOD_hou.node(nodepathStr)
        p = n.parm(portpathStr)
        if p is not None:
            return p.eval()

    @classmethod
    def _obj_loader_cls__get_port_exist_(cls, nodepathStr, portpathStr):
        n = cls.MOD_hou.node(nodepathStr)
        if n:
            p = n.parm(portpathStr)
            if p:
                return True
            return False
        return False

    # **************************************************************************************************************** #
    @classmethod
    def _grh__obj_loader_cls__get_definition_node_raw_(cls, *args):
        out_node_raw_dict = cls.CLS_ordered_dict()
        cls._obj_loader_cls__set_node_raw_build_(
            out_node_raw_dict,
            *args
        )
        return out_node_raw_dict

    @classmethod
    def _grh__obj_loader_cls__get_customize_port_raw_list_(cls, *args, **kwargs):
        return cls._grh__obj_loader_cls__get_customize_vlport_port_raws_(*args, **kwargs) +\
               cls._grh__obj_loader_cls__get_customize_inport_port_raws_(*args, **kwargs) +\
               cls._grh__obj_loader_cls__get_customize_otport_port_raws_(*args, **kwargs)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_node_typepath_(cls, nodepathStr):
        return cls.MOD_hou.node(nodepathStr).type().nameWithCategory()

    @classmethod
    def _obj_loader_cls__get_property_assign_relation_dict_(cls, *args):
        pass


# ******************************************************************************************************************** #
class AbsHouObjQueryrawCreator(grhObjAbs.AbsGrhObjQueryrawCreator):
    def _initAbsHoObjQueryrawCreator(self, *args):
        self._initAbsGrhObjQueryBuilder(*args)

    # **************************************************************************************************************** #
    def _queryraw_loader__get_node_raw_(self, *args):
        typepathString = args[0]
        return self.CLS_grh__obj_query_creator__obj_loader.getDefinitionNodeRaw(typepathString)


# ******************************************************************************************************************** #
class AbsHouObjQueue(grhObjAbs.AbsGrhObjQueue):
    def _initAbsHoObjQueue(self, *args):
        self._initAbsGrhObjQueue(*args)


# ******************************************************************************************************************** #
class AbsHouConnector(grhObjAbs.AbsGrhConnector):
    def _initAbsHoConnector(self, *args):
        self._initAbsGrhConnector(*args)


# ******************************************************************************************************************** #
class AbsHouPort(
    grhObjAbs.AbsGrhPort,
    AbsHouBasic
):
    def _initAbsHoPort(self, *args, **kwargs):
        self._initAbsGrhPort(*args, **kwargs)
        self._hou_bsc__port__set_build_(**kwargs)

    def _hou_bsc__port__set_build_(self, **kwargs):
        # enable
        if u'virtual' in kwargs:
            self._isHouVirtualEnable = kwargs[u'virtual']
        else:
            self._isHouVirtualEnable = False
        # path
        if self._isHouVirtualEnable is True:
            self._houVirtualNodePathStr = kwargs[u'virtualPath']
        else:
            self._houVirtualNodePathStr = None

        self._houVirtualRaw = None

    # **************************************************************************************************************** #
    def _grh__port__get_multi_indexes_(self):
        def getCountFnc_(portpathStr_):
            return AbsHouObjLoader._obj_loader_cls__get_port_portraw_(
                self.path().nodepathString(), portpathStr_
            )

        def count2indexesFnc_(count_):
            return [_i + 1 for _i in range(count_)]

        def getIndexesFnc_(portpathStr_):
            _count = getCountFnc_(portpathStr_)
            return count2indexesFnc_(_count)

        def getMultiChannelIndexesFnc_(compIndexes_, portObj_):
            _formatStr = portObj_.portQuery().format
            _countLis = []
            _multiIndexes = bscMethods.NestedArray.mapTo(compIndexes_)
            for _i in _multiIndexes:
                _portpathStr = _formatStr.format(*_i)
                _count = getCountFnc_(_portpathStr)
                if _count is not None:
                    _countLis.append(_count)
            return count2indexesFnc_(max(_countLis))

        def getCompIndexesFnc_(portObj_):
            _allMultiParentObjs = self._grh__port__get_all_multi_parent_(portObj_)
            _compIndexes = []
            for _seq, _portObj in enumerate(_allMultiParentObjs):
                if _seq == 0:
                    _topIndexes = getIndexesFnc_(_portObj.portpathString())
                    _compIndexes.append(
                        _topIndexes
                    )
                else:
                    _indexes = getMultiChannelIndexesFnc_(_compIndexes, _portObj)
                    _compIndexes.append(
                        _indexes
                    )

            _compIndexes.append(
                getMultiChannelIndexesFnc_(_compIndexes, portObj_)
            )
            return _compIndexes

        if self.isMultiRoot():
            return bscMethods.NestedArray.mapTo(
                [getIndexesFnc_(self.portpathString())]
            )

        elif self.isMultiBranch():
            return bscMethods.NestedArray.mapTo(getCompIndexesFnc_(self))
        return []

    def _grh__port__get_multi_portpath_str_list_(self):
        lis = []
        multiParentObj = self.multiParent()
        multiIndexes = multiParentObj.multiIndexes()

        formatStr = self.portQuery().format
        for _i in multiIndexes:
            portpathStr = formatStr.format(*_i)
            lis.append(portpathStr)

        return lis

    # **************************************************************************************************************** #
    def _inport__get_source_exist_(self, *args, **kwargs):
        if self._isHouVirtualEnable is True:
            return self._inportSourceOtportObj is not None
        elif AbsHouObjLoader._grh__obj_loader_cls__get_port_exist_(
                self.path().nodepathString(), self.path().portpathString()
        ) is True:
            if grhCfg.GrhPortAssignQuery.isInport(self.assignString()):
                return AbsHouObjLoader._grh__obj_loader_cls__get_port_source_exist_(
                    self.path().nodepathString(), self.path().portpathString()
                )
            return False
        return False

    def _inport__get_source_port_obj_(self, **kwargs):
        if self._inport__get_source_exist_() is True:
            if self._isHouVirtualEnable is True:
                return self._inportSourceOtportObj

            _nodepathString, portpathStr = AbsHouObjLoader._obj_loader_cls__get_port_source_str_(
                self.path().nodepathString(), self.path().portpathString()
            )

            portObj = self._grh__port__get_port_cache_obj_(
                (_nodepathString,),
                # source: otport, target: inport
                (portpathStr, grhCfg.GrhPortAssignQuery.otport)
            )
            return portObj

    # **************************************************************************************************************** #
    def _otport__get_target_port_exist_(self, *args):
        if AbsHouObjLoader._grh__obj_loader_cls__get_port_exist_(
                self.path().nodepathString(), self.path().portpathString()
        ) is True:
            if grhCfg.GrhPortAssignQuery.isOtport(self.assignString()):
                return AbsHouObjLoader._obj_loader_cls__get_port_target_exist_(
                    self.path().nodepathString(), self.path().portpathString()
                )
            return False
        return False

    def _otport__get_target_port_obj_list_(self):
        lis = []
        if self._otport__get_target_port_exist_() is True:
            connectionLis = AbsHouObjLoader._obj_loader_cls__get_port_target_str_list_(
                self.path().nodepathString(), self.path().portpathString()
            )
            for _nodepathString, portpathStr in connectionLis:
                portObj = self._grh__port__get_port_cache_obj_(
                    (_nodepathString,),
                    # source: otport, target: inport
                    (portpathStr, grhCfg.GrhPortAssignQuery.inport)
                )
                lis.append(portObj)
        return lis

    # **************************************************************************************************************** #
    def _grh__port__get_portraw_(self, *args, **kwargs):
        def getPortrawFnc_(portpathStr_):
            return AbsHouObjLoader._obj_loader_cls__get_port_portraw_(
                self.path().nodepathString(), portpathStr_
            )

        if self._isHouVirtualEnable is True:
            if AbsHouObjLoader._grh__obj_loader_cls__get_port_exist_(
                self._houVirtualNodePathStr, self.path().portpathString()
            ):
                return AbsHouObjLoader._obj_loader_cls__get_port_portraw_(
                    self._houVirtualNodePathStr, self.path().portpathString(), **kwargs
                )

        elif AbsHouObjLoader._grh__obj_loader_cls__get_port_exist_(
                self.path().nodepathString(), self.path().portpathString()
        ) is True:
            if self.isCompound():
                return
            elif self.isMultiChannel():
                _lis = []
                multiParentObj = self.multiParent()
                parentMultiIndexes = multiParentObj.multiIndexes()

                _formatStr = self.portQuery().format
                for _i in parentMultiIndexes:
                    _portpathStr = _formatStr.format(*_i)
                    _lis.append(
                        getPortrawFnc_(_portpathStr)
                    )
                return _lis
            elif self.isMultiBranch():
                return
            elif self.isMultiRoot():
                return
            elif self.isRampBranch():
                return houBscMtdCore.Mtd_HouGrh._grh_getNodRampChannelRaw(
                    self.path().nodepathString(), self.path().portpathString(),
                    self.parent().path().portpathString()
                )
            elif self.isRampRoot():
                return houBscMtdCore.Mtd_HouGrh._grh_getNodRampPortraw(
                    self.path().nodepathString(), self.path().portpathString()
                )
            elif self.hasChildren():
                return [i.portraw() for i in self.children()]
            return AbsHouObjLoader._obj_loader_cls__get_port_portraw_(
                self.path().nodepathString(), self.path().portpathString(), **kwargs
            )

    def _grh__port__set_portraw_(self, *args, **kwargs):
        if self._isHouVirtualEnable is True:
            self._houVirtualRaw = args[0]


class AbsHouNode(
    grhObjAbs.AbsGrhNode,
    AbsHouBasic
):
    def _initAbsHouNode(self, *args, **kwargs):
        if args:
            # nodepath
            addCustomEnable = False
            if len(args) == 1:
                _nodepathStr = args[0]

                typepathStr = AbsHouObjLoader._obj_loader_cls__get_node_typepath_(_nodepathStr)
                nodepathStr = houBscMtdCore.Mtd_HouGrh._dcc_getNodFullpathNodepathStr(_nodepathStr)
                addCustomEnable = True
            # ( category, nodepath )
            elif len(args) == 2:
                typepathStr, nodepathStr = args
            else:
                raise TypeError()

            # initialization
            self._initAbsGrhNode(typepathStr, nodepathStr, **kwargs)

            # add custom port
            vlportPortRawList = self.CLS_grh__obj__loader.getCustomizeVlportRaws(nodepathStr, pattern=u'ar_*', **kwargs)
            [self._grh_node__set_customize_port_obj_create_(i, **kwargs) for i in vlportPortRawList]
            inportPortRawList = self.CLS_grh__obj__loader.getCustomizeInportRaws(nodepathStr, **kwargs)
            [self._grh_node__set_customize_port_obj_create_(i, **kwargs) for i in inportPortRawList]
            otportPortRawList = self.CLS_grh__obj__loader.getCustomizeOtportRaws(nodepathStr, **kwargs)
            [self._grh_node__set_customize_port_obj_create_(i, **kwargs) for i in otportPortRawList]
        else:
            raise TypeError()

        self._hou_bsc__node__set_build_(**kwargs)

    def _hou_bsc__node__set_build_(self, **kwargs):
        if u'virtual' in kwargs:
            self._isHouVirtualEnable = kwargs[u'virtual']
        else:
            self._isHouVirtualEnable = False

        if self._isHouVirtualEnable is True:
            self._houVirtualPathStr = kwargs[u'virtualPath']
        else:
            self._houVirtualPathStr = None


# geometry assign **************************************************************************************************** #
class AbsHouGeomAssign(
    grhObjAbs.AbsGrhGeometryAssign,
    AbsHouBasic
):
    def _initAbsHoGeomAssign(self, *args, **kwargs):
        self._initAbsGrhGeometryAssign(*args, **kwargs)
        self._hou_bsc__geometry_assign__set_build_()

    def _grh__geometry_assign__set_build_(self, *args):
        assetArg, assignArg = args
        assetFnc = _houBscMtdMtx._AssetFnc(assetArg)

        self._grh__geometry_assign__get_virtual_relation_build_(
            assetFnc.getVirtualRelationDict(assetFnc.getVisibleGeometryObjs())
        )
        #
        self._grh__geometry_assign__set_material_relation_build_(
            assetFnc.getMaterialAssignRelationDict(assignArg)
        )
        self._grh__geometry_assign__set_property_relation_build_(
            assetFnc.getPropertyAssignRelationDict(assetFnc.getVisibleGeometryObjs())
        )
        # geometry
        self._grh__geometry_assign__set_geometry_build_(
            self._materialRelationDict.keys()
        )
        # material
        self._grh__geometry_assign__set_material_build_(
            self._materialRelationDict.values()
        )

    def _grh__geometry_assign__get_geometry_obj_list_(self):
        return [
            self.CLS_grh__assign__obj._node_cls__get_node_cache_obj_(
                self.VAR_grh__assign__mesh_typepath_str,
                geometryPathStr, virtual=True, virtualPath=self._virtualRelationDict[geometryPathStr]
            )
            for geometryPathStr in self._geometryPathStrList
        ]

    # connect material
    def _hou_bsc__geometry_assign__set_build_(self):
        for nodeObj in self.geometries():
            geometryPathStr = nodeObj.pathString()
            materialPathStr = self._materialRelationDict[geometryPathStr]
            if materialPathStr:
                materialObj = self.CLS_grh__assign__obj._node_cls__get_node_cache_obj_(
                    materialPathStr
                )
                geometryMaterialInport = nodeObj.port('shop_materialpath')
                geometryMaterialInport._isHouVirtualEnable = True
                geometryMaterialInport.connectFrom(
                    materialObj.port('surface')
                )
