# coding:utf-8
import re

import copy
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxBasic import bscMethods

from LxGraphic import grhCfg

from . import maBscCfg


class Mtd_MaBasic(maBscCfg.MaUtility):
    MOD_maya_cmds = cmds
    MOD_re = re
    MOD_copy = copy


class Mtd_MyaObj(Mtd_MaBasic):
    DEF_mya_porttype_integer_list = [
        'long', 'short', 'byte'
    ]

    DEF_mya_porttype_float_list = [
        'float', 'double', 'char'
    ]

    # **************************************************************************************************************** #
    @classmethod
    def _dcc_getNodAttrpathString(cls, *args):
        if len(args) > 1:
            return cls.DEF_mya_node_port_pathsep.join(list(args))
        return args[0]

    # **************************************************************************************************************** #
    @classmethod
    def _dcc_getNodExist(cls, nodepathString):
        if nodepathString is not None:
            return cls.MOD_maya_cmds.objExists(nodepathString)
        return False

    # **************************************************************************************************************** #
    # noinspection PyUnusedLocal
    @classmethod
    def _dcc_getNodNodetypeStr(cls, typepathString):
        return grhCfg.GrhUtility.DEF_grh__keyword__default

    @classmethod
    def _dcc_getNodCategoryStr(cls, nodepathString):
        return cls.MOD_maya_cmds.nodeType(nodepathString)

    # **************************************************************************************************************** #
    @classmethod
    def _obj_loader_cls__get_port_format_(cls, portpathString):
        _ = portpathString.split(cls.DEF_mya_node_port_pathsep)[-1]
        if _.endswith(u']'):
            return _.split(u'[')[0]
        return _

    @classmethod
    def _dcc_getNodPortnames(cls, typepathString):
        return cls.MOD_maya_cmds.attributeInfo(
            allAttributes=True,
            type=typepathString
        ) or []

    @classmethod
    def _dcc_getNodPortIsExist(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            exists=1
        )

    @classmethod
    def _dcc_getNodPortIsReadable(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            readable=1
        )

    @classmethod
    def _dcc_getNodPortIsWritable(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            writable=1
        )

    @classmethod
    def _dcc_getNodPortIsConnectable(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            connectable=1
        )

    @classmethod
    def _dcc_getNodPortIsMessage(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            message=1
        )

    @classmethod
    def _dcc_getNodPortIsColor(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            usedAsColor=1
        )

    @classmethod
    def _dcc_getNodPortIsFilename(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            usedAsFilename=1
        )

    @classmethod
    def _obj_loader_cls__get_port_is_multiple_(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            multi=1
        )

    @classmethod
    def _dcc_getNodPortIsEnumerate(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            enum=1
        )

    @classmethod
    def _dcc_getNodPorttype(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            attributeType=1
        )

    @classmethod
    def _dcc_getNodPortHasChildren(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            numberOfChildren=1
        ) is not None

    @classmethod
    def _dcc_getNodPortChildren(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            listChildren=1
        ) or []

    @classmethod
    def _dcc_getNodPortHasParent(cls, typepathString, portpathString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            listParent=1
        ) is not None

    @classmethod
    def _dcc_getNodPortParent(cls, typepathString, portpathString):
        _ = cls.MOD_maya_cmds.attributeQuery(
            cls._obj_loader_cls__get_port_format_(portpathString),
            type=typepathString,
            listParent=1
        )
        if _:
            return _[0]

    # **************************************************************************************************************** #
    @classmethod
    def _dcc_getAttrpathNodepath(cls, attrpathString):
        return bscMethods.MaAttrpath.nodepathString(attrpathString)

    @classmethod
    def _dcc_getAttrpathPortpath(cls, attrpathString):
        return bscMethods.MaAttrpath.portpathString(attrpathString)

    @classmethod
    def _dcc_getNodPortIsAppExist(cls, *args):
        return cls.MOD_maya_cmds.objExists(
            cls._dcc_getNodAttrpathString(*args)
        )

    @classmethod
    def _dcc_getNodPortIndexes(cls, *args):
        return cls.MOD_maya_cmds.getAttr(
            cls._dcc_getNodAttrpathString(*args),
            multiIndices=1,
            silent=1
        ) or []

    @classmethod
    def _dcc_toAttributeString(cls, nodepathString, portpathString):
        return cls.DEF_mya_node_port_pathsep.join(
            [nodepathString, portpathString]
        )

    @classmethod
    def _dcc_getNodPortSourceExist(cls, *args):
        if cls._dcc_getNodPortIsAppExist(*args):
            return cls.MOD_maya_cmds.connectionInfo(
                cls._dcc_getNodAttrpathString(*args),
                isExactDestination=1
            )
        return False

    @classmethod
    def _dcc_getNodPortIsSource(cls, *args):
        if cls._dcc_getNodPortIsAppExist(*args):
            return cls.MOD_maya_cmds.connectionInfo(
                cls._dcc_getNodAttrpathString(*args),
                isExactSource=1
            )
        return False

    @classmethod
    def _dcc_getNodPortSourceStr(cls, *args):
        if cls._dcc_getNodPortIsAppExist(*args):
            return cls.MOD_maya_cmds.connectionInfo(
                cls._dcc_getNodAttrpathString(*args),
                sourceFromDestination=1
            )

    @classmethod
    def _dcc_getNodPortHasTargets(cls, *args):
        if cls._dcc_getNodPortIsAppExist(*args):
            return cls.MOD_maya_cmds.connectionInfo(
                cls._dcc_getNodAttrpathString(*args),
                isExactSource=1
            )
        return False

    @classmethod
    def _dcc_getNodPortIsTarget(cls, *args):
        if cls._dcc_getNodPortIsAppExist(*args):
            return cls.MOD_maya_cmds.connectionInfo(
                cls._dcc_getNodAttrpathString(*args),
                isExactDestination=1
            )
        return False

    @classmethod
    def _dcc_getNodPortTargets(cls, *args):
        if cls._dcc_getNodPortIsAppExist(*args):
            return cls.MOD_maya_cmds.connectionInfo(
                cls._dcc_getNodAttrpathString(*args),
                destinationFromSource=1
            ) or []
        return []

    @classmethod
    def _dcc_getNodPortDatatype(cls, nodepathString, portpathString):
        return cls.MOD_maya_cmds.getAttr(
            cls._dcc_toAttributeString(nodepathString, portpathString),
            type=1,
            silent=1
        )

    @classmethod
    def _dcc_getNodPortraw(cls, nodepathString, portpathString, asString):
        return cls.MOD_maya_cmds.getAttr(
            cls._dcc_toAttributeString(nodepathString, portpathString),
            asString=asString,
            silent=1
        )

    # **************************************************************************************************************** #
    @classmethod
    def _dcc_getNodFullpathNodepathStr(cls, nodepathString):
        if not nodepathString.startswith(cls.DEF_mya_node_pathsep):
            return cls.MOD_maya_cmds.ls(nodepathString, long=1)[0]
        else:
            return nodepathString

    @classmethod
    def _dcc_getNodTransformNodepathStr(cls, nodepathString, fullpath=True):
        if cls._dcc_getNodExist(nodepathString):
            if cls._dcc_getNodCategoryStr(nodepathString) == cls.DEF_mya_type_transform:
                if fullpath:
                    return cls._dcc_getNodFullpathNodepathStr(nodepathString)
                else:
                    return bscMethods.MaNodeString.nodenameWithNamespace(nodepathString)
            else:
                stringLis = cls.MOD_maya_cmds.listRelatives(nodepathString, parent=1, fullPath=fullpath)
                if stringLis:
                    return stringLis[0]

    @classmethod
    def _dcc_getNodShapeNodepathStr(cls, nodepathString, fullpath=True):
        string = None
        if cls._dcc_getNodCategoryStr(nodepathString) == cls.DEF_mya_type_transform:
            stringLis = cls.MOD_maya_cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=1, fullPath=fullpath)
            if stringLis:
                string = stringLis[0]
        else:
            if fullpath:
                string = cls._dcc_getNodFullpathNodepathStr(nodepathString)
            else:
                string = bscMethods.MaNodeString.nodenameWithNamespace(nodepathString)
        return string

    @classmethod
    def _dcc_getNodParentExist(cls, nodepathString, fullpath=True):
        return cls.MOD_maya_cmds.listRelatives(nodepathString, parent=1, fullPath=fullpath) is not None

    @classmethod
    def _dcc_getNodParentNodepathStr(cls, nodepathString, fullpath=True):
        _ = cls.MOD_maya_cmds.listRelatives(nodepathString, parent=1, fullPath=fullpath)
        if _:
            return _[0]

    @classmethod
    def _dcc_getNodChildrenExist(cls, nodepathString, fullpath=True):
        return cls.MOD_maya_cmds.listRelatives(nodepathString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullpath) is not None

    @classmethod
    def _dcc_getNodChildNodepathStrList(cls, nodepathString, fullpath=True):
        return cls.MOD_maya_cmds.listRelatives(nodepathString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullpath) or []

    # **************************************************************************************************************** #
    @classmethod
    def _grh_getNodePortkey_(cls, portpathString):
        _ = portpathString.split(cls.DEF_mya_node_port_pathsep)
        string = ''
        for seq, i in enumerate(_):
            if i.endswith(u']'):
                i = i.split(u'[')[0]
            if seq > 0:
                string += (cls.DEF_mya_node_port_pathsep + i)
            else:
                string += i
        return string

    @classmethod
    def _grh_getNodePortPathdata_(cls, pathString):
        def addFnc_(item):
            if item:
                if not item in lis:
                    lis.append(item)

        def getBranchFnc_(pathString_):
            if not pathString_ in lis:
                stringLis = pathString_.split(pathsep)
                #
                dataCount = len(stringLis)
                for seq, data in enumerate(stringLis):
                    if data:
                        if seq < dataCount:
                            subPath = pathsep.join(stringLis[:seq])
                            addFnc_(subPath)
                #
                addFnc_(pathString_)

        lis = []
        pathsep = cls.DEF_mya_node_port_pathsep
        getBranchFnc_(pathString)
        return lis

    @classmethod
    def _grh_getNodePortChildren(cls, typepathString, portpathString):
        lis = []

        _children = cls._dcc_getNodPortChildren(typepathString, portpathString)
        if _children:
            for _i in _children:
                _fullpathPortnameString = cls.DEF_mya_node_port_pathsep.join([portpathString, _i])
                lis.append(_fullpathPortnameString)
        if cls._dcc_getNodPortIsColor(typepathString, portpathString):
            if portpathString == u'outColor':
                _alphaPortnameString = u'outAlpha'
            else:
                _alphaPortnameString = portpathString + u'A'
            if cls._dcc_getNodPortIsExist(typepathString, _alphaPortnameString):
                lis.append(_alphaPortnameString)

        return lis

    @classmethod
    def _grh_getNodePortSearchPortkeyStrings(cls, nodepathString, portpathString):
        def recursionFnc_(categoryString_, nodeString_, portString_):
            if cls._dcc_getNodPortHasChildren(categoryString_, portString_):
                _children = cls._grh_getNodePortChildren(categoryString_, portString_)
                if _children:
                    for _i in _children:
                        recursionFnc_(categoryString_, nodeString_, _i)
            else:
                lis.append(portString_)

        lis = []
        typepathString = cls.MOD_maya_cmds.nodeType(nodepathString)

        recursionFnc_(typepathString, nodepathString, portpathString)
        return lis

    @classmethod
    def _grh_getNodePortParent(cls, typepathString, portpathString):
        _ = cls._dcc_getNodPortParent(typepathString, portpathString)
        if _:
            return _

        if portpathString == u'outAlpha':
            return u'outColor'
        elif portpathString.endswith(u'A'):
            s = portpathString[:-1]
            if cls._dcc_getNodPortIsExist(typepathString, s):
                return s
            return _

    # **************************************************************************************************************** #
    @classmethod
    def _grh_getNodePortpathStringList(cls, nodepathString):
        def recursionFnc_(categoryString_, portnameString_):
            _children = cls._dcc_getNodPortChildren(categoryString_, portnameString_)
            if _children:
                for _i in _children:
                    _portnameString = u'{}.{}'.format(portnameString_, _i)
                    lis.append(_portnameString)
                    recursionFnc_(categoryString_, _portnameString)

        lis = []
        typepathString = cls.MOD_maya_cmds.nodeType(nodepathString)

        portStringList = bscMethods.List.cleanupTo(
            cls.MOD_maya_cmds.listAttr(nodepathString)
        )
        if portStringList:
            for k in portStringList:
                if cls._dcc_getNodPortHasParent(typepathString, k) is False:
                    lis.append(k)
                    recursionFnc_(typepathString, k)
        return lis

    @classmethod
    def _grh_getNodePortpathStringList_(cls, typepathString):
        def recursionFnc_(categoryString_, portnameString_):
            _children = cls._dcc_getNodPortChildren(categoryString_, portnameString_)
            if _children:
                for _i in _children:
                    _portnameString = u'{}.{}'.format(portnameString_, _i)
                    lis.append(_portnameString)
                    recursionFnc_(categoryString_, _portnameString)

        lis = []

        portStringList = bscMethods.List.cleanupTo(
            cls.MOD_maya_cmds.attributeInfo(
                allAttributes=True,
                type=typepathString
            ) or []
        )
        if portStringList:
            for k in portStringList:
                if cls._dcc_getNodPortHasParent(typepathString, k) is False:
                    lis.append(k)
                    recursionFnc_(typepathString, k)
        return lis

    @classmethod
    def _grh_getNodePortAssign(cls, typepathString, portpathString):
        _assignStr = None

        readable = cls._dcc_getNodPortIsReadable(typepathString, portpathString)
        writeable = cls._dcc_getNodPortIsWritable(typepathString, portpathString)

        if (readable, writeable) == (True, True):
            return grhCfg.GrhPortAssignQuery.gnport
        if (readable, writeable) == (True, False):
            return grhCfg.GrhPortAssignQuery.otport
        elif (readable, writeable) == (False, True):
            return grhCfg.GrhPortAssignQuery.inport

    @classmethod
    def _grh_getNodePorttypeString(cls, typepathString, portkeyString, isArray):
        _portTypeString = cls._dcc_getNodPorttype(typepathString, portkeyString)
        if cls._dcc_getNodPortIsColor(typepathString, portkeyString):
            if portkeyString == u'outColor':
                _alphaPortnameString = u'outAlpha'
            else:
                _alphaPortnameString = portkeyString + u'A'
            if cls._dcc_getNodPortIsExist(typepathString, _alphaPortnameString):
                _ = u'color4'
            else:
                _ = u'color3'

            if isArray is True:
                return _ + u'array'
            return _
        elif cls._dcc_getNodPortIsFilename(typepathString, portkeyString):
            return u'filename'
        elif cls._dcc_getNodPortIsEnumerate(typepathString, portkeyString):
            _ = u'string'
            if isArray is True:
                return _ + u'array'
            return _
        elif _portTypeString in cls.DEF_mya_porttype_integer_list:
            _ = u'integer'
            if isArray is True:
                return _ + u'array'
            return _
        elif _portTypeString in cls.DEF_mya_porttype_float_list:
            _ = u'float'
            if isArray:
                return _ + u'array'
            return _
        elif _portTypeString == u'bool':
            return u'boolean'
        return _portTypeString

    @classmethod
    def _grh_getNodePortDefDict(cls, typepathString, portpathStringList):
        dic = cls.CLS_ordered_dict()

        for portpathString in portpathStringList:
            portDict = cls.CLS_ordered_dict()

            assignString = cls._grh_getNodePortAssign(typepathString, portpathString)
            if assignString is not None:
                isArray = cls._grh_getNodePortIsArray(typepathString, portpathString)

                porttypeString = cls._grh_getNodePorttypeString(typepathString, portpathString, isArray)
                parentPortnameString = cls._grh_getNodePortParent(typepathString, portpathString)
                childPortnameStrings = cls._grh_getNodePortChildren(typepathString, portpathString)

                portDict[grhCfg.GrhUtility.DEF_grh__key_porttype] = porttypeString
                portDict[grhCfg.GrhUtility.DEF_grh__key_port_datatype] = porttypeString
                portDict[grhCfg.GrhUtility.DEF_grh__key_portpath] = portpathString
                portDict[grhCfg.GrhUtility.DEF_grh__key_assign] = assignString
                portDict[grhCfg.GrhUtility.DEF_grh__key_parent] = parentPortnameString
                portDict[grhCfg.GrhUtility.DEF_grh__key_children] = childPortnameStrings

                dic[portpathString] = portDict

        return dic

    @classmethod
    def _grh_getNodePortRawList(cls, typepathString, portpathStringList):
        lis = []

        for portpathString in portpathStringList:
            portDict = {}

            assignString = cls._grh_getNodePortAssign(typepathString, portpathString)
            isArray = cls._grh_getNodePortIsArray(typepathString, portpathString)

            porttypeString = cls._grh_getNodePorttypeString(typepathString, portpathString, isArray)
            parentPortnameString = cls._grh_getNodePortParent(typepathString, portpathString)
            childPortnameStrings = cls._grh_getNodePortChildren(typepathString, portpathString)

            portDict[grhCfg.GrhUtility.DEF_grh__key_porttype] = porttypeString
            portDict[grhCfg.GrhUtility.DEF_grh__key_port_datatype] = porttypeString
            portDict[grhCfg.GrhUtility.DEF_grh__key_portpath] = portpathString
            portDict[grhCfg.GrhUtility.DEF_grh__key_portraw] = None
            portDict[grhCfg.GrhUtility.DEF_grh__key_assign] = assignString
            portDict[grhCfg.GrhUtility.DEF_grh__key_parent] = parentPortnameString
            portDict[grhCfg.GrhUtility.DEF_grh__key_children] = childPortnameStrings

            lis.append(portDict)

        return lis

    @classmethod
    def _grh_getNodNodeRaw(cls, typepathString):
        dic = {
            grhCfg.GrhUtility.DEF_grh__key_node_typepath: typepathString,
            grhCfg.GrhUtility.DEF_grh__key_node_datatype: None,
            grhCfg.GrhUtility.DEF_grh__key_port: cls._grh_getNodePortRawList(
                typepathString, cls._grh_getNodePortpathStringList_(typepathString)
            )
        }

        return dic

    @classmethod
    def _grh_getNodePortRaw(cls, typepathString, portpathString):
        assignString = cls._grh_getNodePortAssign(typepathString, portpathString)
        isArray = cls._grh_getNodePortIsArray(typepathString, portpathString)

        porttypeString = cls._grh_getNodePorttypeString(typepathString, portpathString, isArray)
        parentPortnameString = cls._grh_getNodePortParent(typepathString, portpathString)
        childPortnameStrings = cls._grh_getNodePortChildren(typepathString, portpathString)

        return {
            grhCfg.GrhUtility.DEF_grh__key_porttype: porttypeString,
            grhCfg.GrhUtility.DEF_grh__key_port_datatype: porttypeString,
            grhCfg.GrhUtility.DEF_grh__key_portpath: portpathString, grhCfg.GrhUtility.DEF_grh__key_portraw: None,
            grhCfg.GrhUtility.DEF_grh__key_assign: assignString,
            grhCfg.GrhUtility.DEF_grh__key_parent: parentPortnameString,
            grhCfg.GrhUtility.DEF_grh__key_children: childPortnameStrings
        }

    @classmethod
    def _grh_getNodePortIsArray(cls, typepathString, portpathString):
        portPathdata = cls._grh_getNodePortPathdata_(portpathString)
        for seq, portpathString in enumerate(portPathdata):
            _isArray = cls._obj_loader_cls__get_port_is_multiple_(typepathString, portpathString)
            if _isArray:
                return True
        return False

    @classmethod
    def _grh_getNodePortkeyStringDict(cls, typepathString, portStringList):
        def recursionFnc_(categoryString_, portString_):
            _children = cls._dcc_getNodPortChildren(categoryString_, portString_)
            if _children:
                for _i in _children:
                    _fullpathPortnameString = u'{}.{}'.format(portString_, _i)
                    dic[_i] = _fullpathPortnameString
                    recursionFnc_(categoryString_, _fullpathPortnameString)

        dic = cls.CLS_ordered_dict()

        if portStringList:
            for i in portStringList:
                if cls._dcc_getNodPortHasParent(typepathString, i) is False:
                    dic[i] = i
                    recursionFnc_(typepathString, i)
        return dic
    # **************************************************************************************************************** #
    @classmethod
    def _grh_getNodePortdata_(cls, nodepathString, portkeyString, asString):
        exclude_datatype_list = [
            'mesh',
            'attributeAlias',
        ]
        typepathString = cls.MOD_maya_cmds.nodeType(nodepathString)

        if cls._dcc_getNodPortIsAppExist(nodepathString, portkeyString) is True:
            if cls._dcc_getNodPortIsMessage(typepathString, portkeyString):
                if cls._dcc_getNodPortSourceExist(nodepathString, portkeyString):
                    return bscMethods.MaAttrpath.nodepathString(
                        cls._dcc_getNodPortSourceStr(nodepathString, portkeyString)
                    )
                return ''
            elif cls._dcc_getNodPortIsEnumerate(typepathString, portkeyString):
                return cls.MOD_maya_cmds.getAttr(
                            cls._dcc_toAttributeString(nodepathString, portkeyString),
                            asString=asString,
                            silent=1
                        )
            else:
                datatype = cls._dcc_getNodPorttype(typepathString, portkeyString)
                if not datatype in exclude_datatype_list:
                    return cls.MOD_maya_cmds.getAttr(
                                cls._dcc_toAttributeString(nodepathString, portkeyString), silent=1
                            )

    @classmethod
    def _grh_getNodPortraw(cls, nodepathString, portkeyString, asString=True):
        def getArrayPortdataFnc_(nodepathString_, portStrings_):
            return [
                cls._grh_getNodePortdata_(
                    nodepathString_,
                    _l,
                    asString=False
                )
                for _l in portStrings_
            ]

        def getArrayFnc_(nodepathString_, formatStrings_):
            _lis = []
            for _format in formatStrings_:
                _formatString, _indexArray = _format
                _portStringList = []
                for _index in _indexArray:
                    s = _formatString.format(*_index)
                    _portStringList.append(s)
                _lis.append(_portStringList)

            _lis_ = []
            for _j in zip(*_lis):
                for _k in _j:
                    _lis_.append(
                        _k
                    )
            return getArrayPortdataFnc_(nodepathString_, _lis_)

        def getMultiBranchFnc_(nodepathString_, portkeyString_):
            _lis = []
            _isArrayEnable = False
            _portkeyStringList = cls._grh_getNodePortSearchPortkeyStrings(nodepathString_, portkeyString_)
            for _i in _portkeyStringList:
                _format = cls._grh_getNodePortFormat(nodepathString_, _i)
                if _format is not None:
                    _isArrayEnable = True
                    _lis.append(_format)
                else:
                    _lis.append(_i)

            if _isArrayEnable is True:
                return getArrayFnc_(nodepathString_, _lis)
            else:
                return getArrayPortdataFnc_(nodepathString_, _lis)

        typepathString = cls.MOD_maya_cmds.nodeType(nodepathString)

        if cls._dcc_getNodPortHasChildren(typepathString, portkeyString) is True:
            return getMultiBranchFnc_(nodepathString, portkeyString)
        else:
            format_ = cls._grh_getNodePortFormat(nodepathString, portkeyString)
            if format_ is not None:
                formatString, indexArray = format_
                return getArrayFnc_(nodepathString, [(formatString, indexArray)])
            else:
                return cls._grh_getNodePortdata_(
                    nodepathString,
                    portkeyString,
                    asString=asString
                )

    @classmethod
    def _grh_getNodePortIndexArray(cls, nodepathString, portkeyString):
        def recursionFnc_(categoryString_, nodepathString_, portString_):
            if cls._dcc_getNodPortIsAppExist(nodepathString_, portString_):
                key = cls._grh_getNodePortkey_(portString_)
                _indexes = cls._dcc_getNodPortIndexes(nodepathString_, portString_)
                _children = cls._dcc_getNodPortChildren(categoryString_, portString_)

                _hasIndex = _indexes != []
                _hasChild = _children != []

                _check = (_hasIndex, _hasChild)
                if _indexes:
                    if key in dic:
                        __indexes = dic[key]
                        if __indexes != _indexes:
                            for _i in _indexes:
                                if not _i in __indexes:
                                    __indexes.append(_i)
                        dic[key] = __indexes
                    else:
                        dic[key] = _indexes

                if _check == (True, True):
                    for index_ in _indexes:
                        for childPortname in _children:
                            _fullpathPortnameString = u'{}[{}].{}'.format(portString_, index_, childPortname)
                            recursionFnc_(categoryString_, nodepathString_, _fullpathPortnameString)
                elif _check == (True, False):
                    for index_ in _indexes:
                        _fullpathPortnameString = u'{}[{}]'.format(portString_, index_)
                        recursionFnc_(categoryString_, nodepathString_, _fullpathPortnameString)
                elif _check == (False, True):
                    for childPortname in _children:
                        _fullpathPortnameString = u'{}.{}'.format(portString_, childPortname)
                        recursionFnc_(categoryString_, nodepathString_, _fullpathPortnameString)

        dic = {}
        typepathString = cls.MOD_maya_cmds.nodeType(nodepathString)

        portPathdata = cls._grh_getNodePortPathdata_(portkeyString)

        for i in portPathdata:
            recursionFnc_(typepathString, nodepathString, i)
        return dic

    @classmethod
    def _grh_getNodePortFormat(cls, nodepathString, portkeyString):
        indexArrayDict = cls._grh_getNodePortIndexArray(nodepathString, portkeyString)
        portPathdata = cls._grh_getNodePortPathdata_(portkeyString)
        _portString = ''
        _lis = []
        for seq, i in enumerate(portPathdata):
            _portname = i.split(cls.DEF_mya_node_port_pathsep)[-1]
            if i in indexArrayDict:
                indexes = indexArrayDict[i]
                _indexString = u'[{{{}}}]'.format(len(_lis))
                if seq > 0:
                    _portString += (cls.DEF_mya_node_port_pathsep + _portname + _indexString)
                else:
                    _portString += (_portname + _indexString)
                _lis.append(indexes)
            else:
                if seq > 0:
                    _portString += (cls.DEF_mya_node_port_pathsep + _portname)
                else:
                    _portString += _portname
        if _lis:
            return _portString, bscMethods.NestedArray.mapTo(_lis)


class Mtd_MaUtility(Mtd_MaBasic):
    @classmethod
    def _dcc_getNodFullpathNodepathStr(cls, nodepathString):
        if not nodepathString.startswith(cls.DEF_mya_node_pathsep):
            return cls.MOD_maya_cmds.ls(nodepathString, long=1)[0]
        else:
            return nodepathString

    @classmethod
    def _toAppExistStringList(cls, nodepathString, fullPath=True):
        lis = []
        if isinstance(nodepathString, (str, unicode)):
            if cls._isAppExist(nodepathString):
                if fullPath is True:
                    lis = [cls._dcc_getNodFullpathNodepathStr(nodepathString)]
                else:
                    lis = [bscMethods.MaNodeString.nodenameWithNamespace(nodepathString)]
        elif isinstance(nodepathString, (tuple, list)):
            for i in nodepathString:
                if cls._isAppExist(i):
                    if fullPath is True:
                        lis.append(cls._dcc_getNodFullpathNodepathStr(i))
                    else:
                        lis.append(bscMethods.MaNodeString.nodenameWithNamespace(i))
        return lis

    @staticmethod
    def _setListCleanup(lis):
        lis_ = list(set(lis))
        lis_.sort(key=lis.index)
        return lis_

    @classmethod
    def _isAppExist(cls, nodepathString):
        if nodepathString is not None:
            return cls.MOD_maya_cmds.objExists(nodepathString)
        return False


class Mtd_MaAttribute(Mtd_MaBasic):
    DEF_mya_porttype_dict = {
        'bool': 'boolean',
        'long': 'integer',
        'short': 'integer',
        'byte': 'integer',
        'float': 'float',
        'double': 'float',
        'char': 'string',
    }

    @classmethod
    def _getAttributeQueryNameString(cls, attrpathString):
        _ = attrpathString.split(cls.DEF_mya_node_port_pathsep)[-1]
        if _.endswith(u']'):
            return _.split(u'[')[0]
        return _

    @classmethod
    def _toAttributePortsepSplit(cls, attrpathString):
        _ = attrpathString.split(cls.DEF_mya_node_port_pathsep)
        return _[0], cls.DEF_mya_node_port_pathsep.join(_[1:])

    @classmethod
    def _getAttributeType(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            attributeType=1
        )

    @classmethod
    def _getAttributeData(cls, attrpathString):
        if cls._getAttributeIsAppExist(attrpathString) is True:
            if cls._getAttributeIsMessage(attrpathString):
                if cls._getAttributeHasSource(attrpathString):
                    return bscMethods.MaAttrpath.nodepathString(cls._getAttributeSource(attrpathString))
            else:
                return cls.MOD_maya_cmds.getAttr(attrpathString, silent=1)

    @classmethod
    def _getAttributePorttype(cls, attrpathString):
        if cls._getAttributeIsEnum(attrpathString):
            return 'string'
        elif cls._getAttributeIsColor(attrpathString):
            return 'color'
        elif cls._getAttributeIsFilename(attrpathString):
            return 'filename'
        _ = cls._getAttributeType(attrpathString)
        if _ in cls.DEF_mya_porttype_dict:
            return cls.DEF_mya_porttype_dict[_]
        return _

    @classmethod
    def _getAttributePortdata(cls, attrpathString, asString):
        exclude_datatype_list = [
            'mesh',
            'attributeAlias',
            'TdataCompound',
        ]
        exclude_porttype_list = [
            'polyFaces'
        ]
        if cls._getAttributeIsAppExist(attrpathString) is True:
            if cls._getAttributeIsMessage(attrpathString):
                if cls._getAttributeHasSource(attrpathString):
                    return bscMethods.MaAttrpath.nodepathString(cls._getAttributeSource(attrpathString))
                return ''
            else:
                porttype = cls._getAttributePorttype(attrpathString)
                if porttype not in exclude_porttype_list:
                    datatype = cls._getAttributeDatatype(attrpathString)
                    attrpathString = cls._getAttributeString_(attrpathString)
                    if datatype == 'enum':
                        return cls.MOD_maya_cmds.getAttr(attrpathString, asString=asString, silent=1)
                    elif datatype not in exclude_datatype_list:
                        _ = cls.MOD_maya_cmds.getAttr(attrpathString, silent=1)
                        if datatype in cls.DEF_mya_datatype_compchannel_list:
                            return list(_[0])
                        return _

    @classmethod
    def _getAttributeIsAppExist(cls, attrpathString):
        attrpathString = cls._getAttributeString_(attrpathString)
        return cls.MOD_maya_cmds.objExists(attrpathString)

    @classmethod
    def _getAttributeIsNodeExist(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            exists=1
        )

    @classmethod
    def _getAttributeIsCompound(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            usesMultiBuilder=1
        )

    @classmethod
    def _getAttributeIsMultichannel(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            multi=1
        )

    @classmethod
    def _getAttributeIndexes(cls, attrpathString):
        """
        :param attrpathString: etc. aiRampFloat1.ramp
        :return:
        """
        attrpathString = cls._getAttributeString_(attrpathString)
        return cls.MOD_maya_cmds.getAttr(attrpathString, multiIndices=1, silent=1) or []

    @classmethod
    def _getAttributeIsMessage(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            message=1
        )

    @classmethod
    def _getAttributeIsColor(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            usedAsColor=1
        )

    @classmethod
    def _getAttributeIsFilename(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            usedAsFilename=1
        )

    @classmethod
    def _getAttributeIsEnum(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            enum=1
        )

    @classmethod
    def _getAttributeNicename(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            niceName=1
        )

    @classmethod
    def _getAttributeHasParent(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            listParent=1
        ) is not None

    @classmethod
    def _getAttributeParentPortname(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        _ = cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            listParent=1
        )
        if _:
            return _[0]

    @classmethod
    def _getAttributeHasChild(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            numberOfChildren=1
        ) > 0

    @classmethod
    def _getAttributeChildPortnameList(cls, attrpathString):
        nodepathString, portpathString = cls._getAttributeQueryString_(attrpathString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portpathString),
            node=nodepathString,
            listChildren=1
        ) or []

    @classmethod
    def _getAttributeQueryString_(cls, attrpathString):
        if isinstance(attrpathString, (tuple, list)):
            nodepathString, portpathString = attrpathString
        else:
            nodepathString, portpathString = cls._toAttributePortsepSplit(attrpathString)
        return nodepathString, portpathString

    @classmethod
    def _getAttributeString_(cls, attrpathString):
        if isinstance(attrpathString, (tuple, list)):
            attrpathString = cls.DEF_mya_node_port_pathsep.join(list(attrpathString))
        return attrpathString

    @classmethod
    def _getAttributeHasChannels(cls, attrpathString):
        return cls._getAttributePorttype(attrpathString) in cls.DEF_mya_datatype_compchannel_list

    @classmethod
    def _getAttributeChannelnameList(cls, attrpathString):
        if cls._getAttributeHasChannels(attrpathString):
            return cls._getAttributeChildPortnameList(attrpathString)
        return []

    @classmethod
    def _getAttributeDefaultData(cls, attrpathString):
        pass

    @classmethod
    def _getAttributeDatatype(cls, attrpathString):
        attrpathString = cls._getAttributeString_(attrpathString)
        return cls.MOD_maya_cmds.getAttr(attrpathString, type=1, silent=1)

    @classmethod
    def _getAttributeHasSource(cls, attrpathString):
        attrpathString = cls._getAttributeString_(attrpathString)
        return cls.MOD_maya_cmds.connectionInfo(attrpathString, isExactDestination=1)

    @classmethod
    def _getAttributeIsSource(cls, attrpathString):
        attrpathString = cls._getAttributeString_(attrpathString)
        return cls.MOD_maya_cmds.connectionInfo(attrpathString, isExactSource=1)

    @classmethod
    def _getAttributeSource(cls, attrpathString):
        attrpathString = cls._getAttributeString_(attrpathString)
        return cls.MOD_maya_cmds.connectionInfo(attrpathString, sourceFromDestination=1)

    @classmethod
    def _getAttributeHasTargets(cls, attrpathString):
        return cls.MOD_maya_cmds.connectionInfo(attrpathString, isExactSource=1)

    @classmethod
    def _getAttributeIsTarget(cls, attrpathString):
        return cls.MOD_maya_cmds.connectionInfo(attrpathString, isExactDestination=1)

    @classmethod
    def _getAttributeTargetList(cls, attrpathString):
        attrpathString = cls._getAttributeString_(attrpathString)
        return cls.MOD_maya_cmds.connectionInfo(attrpathString, destinationFromSource=1) or []

    @classmethod
    def _getAttributeNodeString(cls, attrpathString):
        return bscMethods.MaAttrpath.nodepathString(attrpathString)

    @classmethod
    def _getAttributeFullpathPortname(cls, attrpathString):
        return bscMethods.MaAttrpath.portpathString(attrpathString)

    @classmethod
    def _getAttributePortname(cls, attrpathString):
        return bscMethods.MaAttrpath.name(attrpathString)


class Mtd_MaFile(Mtd_MaBasic):
    DEF_mya_type_maya_ascii = 'mayaAscii'
    DEF_mya_type_maya_binary = 'mayaBinary'
    AlembicType = 'Alembic'
    #
    FileTypeDic = {
        '.ma': DEF_mya_type_maya_ascii,
        '.mb': DEF_mya_type_maya_binary,
        '.abc': AlembicType
    }
    #
    MaFileExportAllOption = 'exportAll'
    MaFileExportSelectedOption = 'exportSelected'
    #
    MaFileConstructionHistoryOption = 'constructionHistory'
    MaFileShaderOption = 'shader'
    #
    MaFileExportSelectedOptions = [
        MaFileConstructionHistoryOption,
        MaFileShaderOption
    ]
    VAR_file_export_kwarg_dic = dict(
        type='mayaAscii',
        options='v=0',
        force=True,
        defaultExtensions=True,
        exportAll=True,
        preserveReferences=False,
    )
    VAR_file_import_kwarg_dic = dict(
        options='v=0;',
        type='mayaAscii',
        i=True,
        renameAll=True,
        mergeNamespacesOnClash=True,
        namespace=':',
        preserveReferences=True
    )

    @classmethod
    def _getMaFileType(cls, fileString):
        ext = bscMethods.OsFile.ext(fileString)
        return cls.FileTypeDic.get(ext, cls.DEF_mya_type_maya_ascii)

    @classmethod
    def _maFileExportCommand(cls, fileString, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.VAR_file_export_kwarg_dic.copy()
        #
        optionKwargs['type'] = cls._getMaFileType(fileString)
        #
        cls.MOD_maya_cmds.file(fileString, **optionKwargs)

    @classmethod
    def _maFileImportCommand(cls, fileString, optionKwargs=None):
        if optionKwargs is None:
            optionKwargs = cls.VAR_file_import_kwarg_dic.copy()
        #
        optionKwargs['type'] = cls._getMaFileType(fileString)
        #
        cls.MOD_maya_cmds.file(
            fileString,
            **optionKwargs
        )

    @classmethod
    def _setMaFileImport(cls, fileString, namespace=':'):
        optionKwargs = cls.VAR_file_import_kwarg_dic.copy()
        #
        optionKwargs['type'] = cls._getMaFileType(fileString)
        optionKwargs['namespace'] = namespace
        #
        cls.MOD_maya_cmds.file(
            fileString,
            **optionKwargs
        )
    
    @classmethod
    def _setMaFileImportWithGroup(cls, fileString, groupString, namespace=':'):
        cls.MOD_maya_cmds.file(
            fileString,
            i=1,
            options='v=0;',
            type=cls._getMaFileType(fileString),
            ra=1,
            mergeNamespacesOnClash=1,
            namespace=namespace,
            preserveReferences=1,
            groupReference=True,
            groupString=groupString
        )
        
    @classmethod
    def _setMaAlembicImport(cls, fileString, namespace=':'):
        cls.MOD_maya_cmds.loadPlugin('AbcImport', quiet=1)

        cls.MOD_maya_cmds.file(
            fileString,
            i=1,
            options='v=0;',
            type='Alembic',
            ra=1,
            mergeNamespacesOnClash=1,
            namespace=namespace,
            preserveReferences=1
        )
        #
        if namespace:
            alembicNodeString = namespace + ':' + bscMethods.OsFile.name(fileString) + '_AlembicNode'
        else:
            alembicNodeString = bscMethods.OsFile.name(fileString) + '_AlembicNode'

        if cls.MOD_maya_cmds.objExists(alembicNodeString):
            pass
        else:
            cls.MOD_maya_cmds.createNode(cls.DEF_mya_type_alembic, name=alembicNodeString)
            cls.MOD_maya_cmds.setAttr(alembicNodeString + '.abc_File', fileString, type='string')

    @classmethod
    def _setMaMaterialExport(cls, fileString, shadingEngines, aiAovs):
        cls.MOD_maya_cmds.select(clear=1)
        if shadingEngines:
            cls.MOD_maya_cmds.select(shadingEngines, noExpand=1)
            if aiAovs:
                cls.MOD_maya_cmds.select(aiAovs, add=1)
            cls.MOD_maya_cmds.file(rename=fileString)
            cls.MOD_maya_cmds.file(
                force=1,
                options='v=0',
                type=cls._getMaFileType(fileString),
                preserveReferences=0,
                exportSelected=1
            )
            cls.MOD_maya_cmds.select(clear=1)
        
    @classmethod
    def _setMaFileExportSelected(cls, fileString, nodepathString, withHistory=False):
        temporaryFile = bscMethods.OsFile.temporaryName(fileString)
        cls.MOD_maya_cmds.select(nodepathString)
        cls.MOD_maya_cmds.file(
            temporaryFile,
            force=1,
            options='v=0',
            type=cls._getMaFileType(fileString),
            preserveReferences=0,
            exportSelected=1,
            constructionHistory=withHistory
        )
        cls.MOD_maya_cmds.select(clear=1)
        bscMethods.OsFile.copyTo(temporaryFile, fileString)
        
    @classmethod
    def _setMaFileExportSelectedWithSet(cls, fileString, nodepathString, setString, withHistory=False):
        cls.MOD_maya_cmds.select(clear=1)
        cls.MOD_maya_cmds.select(nodepathString)

        if isinstance(setString, str):
            if cls.MOD_maya_cmds.objExists(setString):
                cls.MOD_maya_cmds.select(setString, add=1, noExpand=1)
        elif isinstance(setString, list):
            for i in setString:
                if cls.MOD_maya_cmds.objExists(i):
                    cls.MOD_maya_cmds.select(i, add=1, noExpand=1)
        #
        temporaryFile = bscMethods.OsFile.temporaryName(fileString)
        cls.MOD_maya_cmds.file(
            temporaryFile,
            force=1,
            options='v=0',
            type=cls._getMaFileType(fileString),
            preserveReferences=0,
            exportSelected=1,
            constructionHistory=withHistory
        )
        cls.MOD_maya_cmds.select(clear=1)
        bscMethods.OsFile.copyTo(temporaryFile, fileString)

    @classmethod
    def _setMaFileReference(cls, fileString, namespace=':'):
        cls.MOD_maya_cmds.file(
            fileString,
            ignoreVersion=1,
            reference=1,
            mergeNamespacesOnClash=0,
            namespace=namespace,
            options='v=0;p=17;f=0',
            type=cls._getMaFileType(fileString)
        )
    
    @classmethod
    def _setMaCacheReference(cls, fileString, namespace=':'):
        cls.MOD_maya_cmds.file(
            fileString,
            reference=1,
            mergeNamespacesOnClash=1,
            namespace=namespace
        )

    @classmethod
    def _setMaFileOpen(cls, fileString):
        cls.MOD_maya_cmds.file(
            fileString,
            open=1,
            options='v=0',
            force=1,
            type=cls._getMaFileType(fileString)
        )
        
    @classmethod
    def _setMaFileSaveToServer(cls, fileString):
        temporaryFile = bscMethods.OsFile.temporaryName(fileString)
        cls.MOD_maya_cmds.file(rename=temporaryFile)
        cls.MOD_maya_cmds.file(save=1, type=cls._getMaFileType(fileString))
        bscMethods.OsFile.copyTo(temporaryFile, fileString)
        
    @classmethod
    def _setMaFileSaveToLocal(cls, fileString, timetag=None):
        if timetag is None:
            timetag = bscMethods.OsTimetag.active()
        #
        bscMethods.OsFile.createDirectory(fileString)
        fileString = bscMethods.OsFile.toJoinTimetag(fileString, timetag)
        # Main
        cls.MOD_maya_cmds.file(rename=fileString)
        cls.MOD_maya_cmds.file(
            save=1,
            options='v=0;',
            force=1,
            type=cls._getMaFileType(fileString)
        )
    
    @classmethod
    def _setMaFileUpdate(cls, fileString):
        origString = cls.MOD_maya_cmds.file(query=1, sceneName=1)
        cls._setMaFileSaveToServer(fileString)
        cls.MOD_maya_cmds.file(rename=origString)
    
    @classmethod
    def _setMaFileOpenAsTemporary(cls, fileString):
        if bscMethods.OsFile.isExist(fileString):
            temporaryFile = bscMethods.OsFile.temporaryName(fileString)
            bscMethods.OsFile.createDirectory(temporaryFile)

            bscMethods.OsFile.copyTo(fileString, temporaryFile)
            cls._setMaFileOpen(temporaryFile)
        
    @classmethod
    def _setMaFileOpenAsBackup(cls, fileString, backupString, timetag=None):
        if bscMethods.OsFile.isExist(fileString):
            if timetag is None:
                timetag = bscMethods.OsTimetag.active()
            bscMethods.OsFile.createDirectory(backupString)
            localFileJoinUpdateTag = bscMethods.OsFile.toJoinTimetag(backupString, timetag)
            
            bscMethods.OsFile.copyTo(fileString, localFileJoinUpdateTag)
            cls._setMaFileOpen(localFileJoinUpdateTag)
    
    @classmethod
    def _setMaFileNew(cls):
        cls.MOD_maya_cmds.file(new=1, force=1)


class Mtd_MaObject(Mtd_MaUtility):

    @classmethod
    def _getNodeIsGroup(cls, nodepathString):
        boolean = False
        # category is "transform" and has no "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodepathString) == cls.DEF_mya_type_transform:
            _ = cls.MOD_maya_cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if _ is None:
                boolean = True
        return boolean

    @classmethod
    def _getNodeIsTransform(cls, nodepathString):
        boolean = False
        # category is "transform" and has "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodepathString) == cls.DEF_mya_type_transform:
            _ = cls.MOD_maya_cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if _ is not None:
                boolean = True
        return boolean

    @classmethod
    def _getNodeIsShape(cls, nodepathString):
        boolean = False
        # parent is "transform" and has no "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodepathString) != cls.DEF_mya_type_transform:
            transformPath = cls._dcc_getNodTransformNodepathStr(nodepathString)
            _ = cls._getNodeShapeNodeStringList(nodepathString)
            if transformPath and not _:
                boolean = True
        return boolean

    @classmethod
    def _isNodeDag(cls, nodepathString):
        return cls.DEF_mya_node_pathsep in cls._dcc_getNodFullpathNodepathStr(nodepathString)

    @classmethod
    def _getNodeUniqueIdString(cls, nodepathString):
        if cls._isAppExist(nodepathString):
            stringLis = cls.MOD_maya_cmds.ls(nodepathString, uuid=1)
            if stringLis:
                return stringLis[0]

    @classmethod
    def _getNodeCategoryString(cls, nodepathString):
        return cls.MOD_maya_cmds.nodeType(nodepathString)

    @classmethod
    def _getNodeShapeCategoryString(cls, nodepathString):
        string = cls._getNodeCategoryString(nodepathString)
        if string == cls.DEF_mya_type_transform:
            shapePathString = cls._dcc_getNodShapeNodepathStr(nodepathString)
            if shapePathString:
                string = cls._getNodeCategoryString(shapePathString)
        return string

    @classmethod
    def _dcc_getNodTransformNodepathStr(cls, nodepathString, fullpath=True):
        if cls._isAppExist(nodepathString):
            if cls._getNodeCategoryString(nodepathString) == cls.DEF_mya_type_transform:
                if fullpath:
                    return cls._dcc_getNodFullpathNodepathStr(nodepathString)
                else:
                    return bscMethods.MaNodeString.nodenameWithNamespace(nodepathString)
            else:
                stringLis = cls.MOD_maya_cmds.listRelatives(nodepathString, parent=1, fullPath=fullpath)
                if stringLis:
                    return stringLis[0]

    @classmethod
    def _dcc_getNodShapeNodepathStr(cls, nodepathString, fullpath=True):
        string = None
        if cls._getNodeCategoryString(nodepathString) == cls.DEF_mya_type_transform:
            stringLis = cls.MOD_maya_cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=1, fullPath=fullpath)
            if stringLis:
                string = stringLis[0]
        else:
            if fullpath:
                string = cls._dcc_getNodFullpathNodepathStr(nodepathString)
            else:
                string = bscMethods.MaNodeString.nodenameWithNamespace(nodepathString)
        return string

    @classmethod
    def _getNodeShapeNodeStringList(cls, nodepathString, fullpath=True):
        return cls.MOD_maya_cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=0, fullPath=fullpath) or []

    @classmethod
    def _getNodeTargetNodeStringList(cls, nodepathString, includeCategoryString=None):
        if includeCategoryString is not None:
            return cls.MOD_maya_cmds.listConnections(nodepathString, destination=1, source=0, type=includeCategoryString) or []
        return cls.MOD_maya_cmds.listConnections(nodepathString, destination=1, source=0) or []

    @classmethod
    def _getNodeSourceNodeStringList(cls, nodepathString, includeCategoryString=None):
        if includeCategoryString is not None:
            return cls.MOD_maya_cmds.listConnections(nodepathString, destination=0, source=1, type=includeCategoryString) or []
        return cls.MOD_maya_cmds.listConnections(nodepathString, destination=0, source=1) or []

    @classmethod
    def _getNodeShadingEngineNodeStringList(cls, nodepathString, excludeNodeString=None):
        def branchFnc_(subObjectString):
            shapePathString = cls._dcc_getNodShapeNodepathStr(subObjectString)
            if not shapePathString:
                shapePathString = subObjectString
            #
            _ = cls._getNodeTargetNodeStringList(shapePathString, cls.DEF_mya_type_shading_engine)
            if _:
                if excludeNodeString is not None:
                    [lis.append(j) for j in _ if not j in lis and not j in excludeNodeString]
                else:
                    [lis.append(j) for j in _ if not j in lis]
        #
        lis = []
        #
        stringLis = cls._toAppExistStringList(nodepathString)

        if excludeNodeString is not None:
            excludeNodeString = bscMethods.String.toList(excludeNodeString)

        [branchFnc_(i) for i in stringLis]
        return lis

    @classmethod
    def _getShadingEngineObjectSetDatumList(cls, nodepathString):
        """
        :param nodepathString: str
        :return: list
        """
        lis = []
        #
        objSetLis = cls.MOD_maya_cmds.sets(nodepathString, query=1)
        if objSetLis:
            shaderObjectPathLis = [i for i in cls.MOD_maya_cmds.ls(objSetLis, leaf=1, noIntermediate=1, long=1)]
            for shaderObjectPath in shaderObjectPathLis:
                # Object Group
                showType = cls.MOD_maya_cmds.ls(shaderObjectPath, showType=1)[1]
                if showType == 'float3':
                    shaderObjectPath_ = shaderObjectPath.split('.')[0]
                    shaderObjectUuid = cls._getNodeUniqueIdString(shaderObjectPath_)
                    objSetData = shaderObjectPath, shaderObjectUuid
                    if not objSetData in lis:
                        lis.append(objSetData)
                else:
                    shaderObjectUuid = cls._getNodeUniqueIdString(shaderObjectPath)
                    objSetData = shaderObjectPath, shaderObjectUuid
                    if not objSetData in lis:
                        lis.append(objSetData)
        return lis

    @classmethod
    def _getNodeAllTargetNodeStringList(cls, nodepathString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        def recursionFnc_(nodeString_):
            if extend is True:
                searchNodes = [cls._dcc_getNodTransformNodepathStr(nodeString_), cls._dcc_getNodShapeNodepathStr(nodeString_)]
                set(searchNodes)
            else:
                searchNodes = [nodeString_]

            for subNode in searchNodes:
                nodeStrings = cls.MOD_maya_cmds.listConnections(subNode, destination=1, source=0, shapes=1)
                if nodeStrings:
                    for i in nodeStrings:
                        if useShapeCategory is True:
                            nodeTypeString = cls._getNodeShapeCategoryString(i)
                        else:
                            nodeTypeString = cls._getNodeCategoryString(i)

                        if includeCategoryString is not None:
                            if nodeTypeString in includeCategoryString:
                                if not i in lis:
                                    lis.append(i)
                        elif excludeCategoryString is not None:
                            if nodeTypeString not in excludeCategoryString:
                                if not i in lis:
                                    lis.append(i)
                        else:
                            if not i in lis:
                                lis.append(i)
                        #
                        if not i in lis:
                            searchLis.append(i)
                            recursionFnc_(i)

        #
        searchLis = []
        #
        lis = []
        #
        if includeCategoryString is not None:
            includeCategoryString = bscMethods.String.toList(includeCategoryString)
        elif excludeCategoryString is not None:
            excludeCategoryString = bscMethods.String.toList(excludeCategoryString)
        #
        recursionFnc_(nodepathString)
        #
        return lis

    @classmethod
    def _getNodeAllSourceNodeStringList(cls, nodepathString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        def addFnc_(nodeString_):
            if not nodeString_ in lis:
                lis.append(nodeString_)

        def recursionFnc_(nodeString_):
            if extend is True:
                searchNodes = [cls._dcc_getNodTransformNodepathStr(nodeString_), cls._dcc_getNodShapeNodepathStr(nodeString_)]
                set(searchNodes)
            else:
                searchNodes = [nodeString_]

            for subNode in searchNodes:
                nodeStrings = cls.MOD_maya_cmds.listConnections(subNode, destination=0, source=1, shapes=1)
                if nodeStrings:
                    for i in nodeStrings:
                        if useShapeCategory is True:
                            nodeTypeString = cls._getNodeShapeCategoryString(i)
                        else:
                            nodeTypeString = cls._getNodeCategoryString(i)

                        if includeCategoryString is not None:
                            if nodeTypeString in includeCategoryString:
                                addFnc_(i)
                        elif excludeCategoryString is not None:
                            if nodeTypeString not in excludeCategoryString:
                                addFnc_(i)
                        else:
                            addFnc_(i)
                        #
                        if not i in searchLis:
                            searchLis.append(i)
                            recursionFnc_(i)
        #
        searchLis = []
        #
        lis = []
        #
        if includeCategoryString is not None:
            includeCategoryString = bscMethods.String.toList(includeCategoryString)
        elif excludeCategoryString is not None:
            excludeCategoryString = bscMethods.String.toList(excludeCategoryString)
        #
        recursionFnc_(nodepathString)
        #
        return lis


class Mtd_MaNodeGraph(Mtd_MaUtility):
    @classmethod
    def _getNodeGraphNodeStringList(cls, nodepathString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        return Mtd_MaObject._getNodeAllSourceNodeStringList(
            nodepathString,
            includeCategoryString,
            excludeCategoryString,
            useShapeCategory,
            extend
        )

    @classmethod
    def _getNodeGraphConnectionDatumList(cls):
        pass


class Mtd_MaDag(Mtd_MaUtility):
    @classmethod
    def _getDagParentString(cls, dagString, fullpath=True):
        _ = cls.MOD_maya_cmds.listRelatives(dagString, parent=1, fullPath=fullpath)
        if _:
            return _[0]

    @classmethod
    def _getDagChildStringList(cls, dagString, fullpath=True):
        return cls.MOD_maya_cmds.listRelatives(dagString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullpath) or []


class Mtd_MaShadingEngine(Mtd_MaUtility):
    pass


class Mtd_MaNodeGroup(Mtd_MaUtility):
    @classmethod
    def _getGroupChildNodeStringList(cls, groupString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, withShape=True):
        def addFnc_(nodeString_):
            if not nodeString_ in lis:
                if withShape is True:
                    lis.append(nodeString_)
                else:
                    if Mtd_MaObject._getNodeIsShape(nodeString_) is False:
                        lis.append(nodeString_)

        def recursionFnc_(nodeString_):
            nodeStrings = cls.MOD_maya_cmds.listRelatives(nodeString_, children=1, fullPath=1)
            if nodeStrings:
                for i in nodeStrings:
                    if useShapeCategory is True:
                        nodeTypeString = Mtd_MaObject._getNodeShapeCategoryString(i)
                    else:
                        nodeTypeString = Mtd_MaObject._getNodeCategoryString(i)

                    if includeCategoryString is not None:
                        if nodeTypeString in includeCategoryString:
                            addFnc_(i)
                    elif excludeCategoryString is not None:
                        if nodeTypeString not in excludeCategoryString:
                            addFnc_(i)
                    else:
                        addFnc_(i)
                    #
                    if not i in searchLis:
                        searchLis.append(i)
                        recursionFnc_(i)
        #
        searchLis = []
        #
        lis = []
        #
        if includeCategoryString is not None:
            includeCategoryString = bscMethods.String.toList(includeCategoryString)
        elif excludeCategoryString is not None:
            excludeCategoryString = bscMethods.String.toList(excludeCategoryString)
        #
        recursionFnc_(groupString)
        #
        return lis


class Mtd_MaPlug(Mtd_MaBasic):
    pass
