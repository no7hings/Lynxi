# coding:utf-8
import re

import copy

import collections
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxBasic import bscMethods

from LxMaBasic import maBscConfigure


class Mtd_MaBasic(maBscConfigure.Utility):
    MOD_re = re
    MOD_copy = copy
    MOD_maya_cmds = cmds
    CLS_ordered_dict = collections.OrderedDict


class Mtd_MaUtility(Mtd_MaBasic):

    @classmethod
    def _getNodeFullpathNameString(cls, nodeString):
        if not nodeString.startswith(cls.DEF_mya_node_separator):
            return cls.MOD_maya_cmds.ls(nodeString, long=1)[0]
        else:
            return nodeString

    @classmethod
    def _toAppExistStringList(cls, nodeString, fullPath=True):
        lis = []
        if isinstance(nodeString, (str, unicode)):
            if cls._isAppExist(nodeString):
                if fullPath is True:
                    lis = [cls._getNodeFullpathNameString(nodeString)]
                else:
                    lis = [bscMethods.MaNodeString.nodenameWithNamespace(nodeString)]
        elif isinstance(nodeString, (tuple, list)):
            for i in nodeString:
                if cls._isAppExist(i):
                    if fullPath is True:
                        lis.append(cls._getNodeFullpathNameString(i))
                    else:
                        lis.append(bscMethods.MaNodeString.nodenameWithNamespace(i))
        return lis

    @staticmethod
    def _setListCleanup(lis):
        lis_ = list(set(lis))
        lis_.sort(key=lis.index)
        return lis_

    @classmethod
    def _isAppExist(cls, nodeString):
        if nodeString is not None:
            return cls.MOD_maya_cmds.objExists(nodeString)
        return False


class Mtd_MaObjectPort(Mtd_MaBasic):
    DEF_mya_porttype_integer_list = [
        'long', 'short', 'byte'
    ]
    DEF_mya_porttype_float_list = [
        'float', 'double', 'char'
    ]
    # **************************************************************************************************************** #
    @classmethod
    def _dcc_getObjectPortIsAppExist(cls, objectString, portString):
        return cls.MOD_maya_cmds.objExists(
            cls.DEF_mya_port_separator.join([objectString, portString])
        )

    @classmethod
    def _dcc_getObjectPortIndexes(cls, objectString, portString):
        return cls.MOD_maya_cmds.getAttr(
            cls.DEF_mya_port_separator.join([objectString, portString]),
            multiIndices=1,
            silent=1
        ) or []

    @classmethod
    def _dcc_getObjectPortIsReadable(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            readable=1
        )

    @classmethod
    def _dcc_getObjectPortIsWritable(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            writable=1
        )

    @classmethod
    def _dcc_getObjectPortIsMessage(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            message=1
        )

    @classmethod
    def _dcc_getObjectPortIsColor(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            usedAsColor=1
        )

    @classmethod
    def _dcc_getObjectPortIsFilename(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            usedAsFilename=1
        )

    @classmethod
    def _dcc_getObjectPortIsArray(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            multi=1
        )

    @classmethod
    def _dcc_getObjectPortIsEnumerate(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            enum=1
        )

    @classmethod
    def _dcc_getObjectPorttype(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            attributeType=1
        )

    @classmethod
    def _dcc_getObjectPortHasChildren(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            numberOfChildren=1
        ) is not None

    @classmethod
    def _dcc_getObjectPortChildren(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            listChildren=1
        ) or []

    @classmethod
    def _dcc_getObjectPortHasParent(cls, objectString, portString):
        return cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            listParent=1
        ) is not None

    @classmethod
    def _dcc_getObjectPortParent(cls, objectString, portString):
        _ = cls.MOD_maya_cmds.attributeQuery(
            cls._mtl_getObjectPortname_(portString),
            node=objectString,
            listParent=1
        )
        if _:
            return _[0]

    @classmethod
    def _dcc_getObjectPortnames(cls, objectString):
        return cls.MOD_maya_cmds.listAttr(objectString) or []

    @classmethod
    def _dcc_toAttributeString(cls, objectString, portString):
        return cls.DEF_mya_port_separator.join([objectString, portString])

    @classmethod
    def _dcc_getObjectPortHasSource(cls, objectString, portString):
        return cls.MOD_maya_cmds.connectionInfo(
            cls._dcc_toAttributeString(objectString, portString),
            isExactDestination=1
        )

    @classmethod
    def _dcc_getObjectPortIsSource(cls, objectString, portString):
        return cls.MOD_maya_cmds.connectionInfo(
            cls._dcc_toAttributeString(objectString, portString),
            isExactSource=1
        )

    @classmethod
    def _dcc_getObjectPortSource(cls, objectString, portString):
        return cls.MOD_maya_cmds.connectionInfo(
            cls._dcc_toAttributeString(objectString, portString),
            sourceFromDestination=1
        )

    @classmethod
    def _dcc_getObjectPortHasTargets(cls, objectString, portString):
        return cls.MOD_maya_cmds.connectionInfo(
            cls._dcc_toAttributeString(objectString, portString),
            isExactSource=1
        )

    @classmethod
    def _dcc_getObjectPortIsTarget(cls, objectString, portString):
        return cls.MOD_maya_cmds.connectionInfo(
            cls._dcc_toAttributeString(objectString, portString),
            isExactDestination=1
        )

    @classmethod
    def _dcc_getObjectPortTargets(cls, objectString, portString):
        return cls.MOD_maya_cmds.connectionInfo(
            cls._dcc_toAttributeString(objectString, portString),
            destinationFromSource=1
        ) or []

    @classmethod
    def _dcc_getObjectPortDatatype(cls, objectString, portString):
        return cls.MOD_maya_cmds.getAttr(
            cls._dcc_toAttributeString(objectString, portString),
            type=1,
            silent=1
        )

    @classmethod
    def _dcc_getObjectPortdata(cls, objectString, portString, asString):
        return cls.MOD_maya_cmds.getAttr(
            cls._dcc_toAttributeString(objectString, portString),
            asString=asString,
            silent=1
        )
    # **************************************************************************************************************** #
    @classmethod
    def _mtl_getObjectPortname_(cls, portString):
        _ = portString.split(cls.DEF_mya_port_separator)[-1]
        if _.endswith(u']'):
            return _.split(u'[')[0]
        return _

    @classmethod
    def _mtl_getObjectPortkey_(cls, portString):
        _ = portString.split(cls.DEF_mya_port_separator)
        string = ''
        for seq, i in enumerate(_):
            if i.endswith(u']'):
                i = i.split(u'[')[0]
            if seq > 0:
                string += (cls.DEF_mya_port_separator + i)
            else:
                string += i
        return string

    @classmethod
    def _mtl_getObjectPortpath_(cls, pathString):
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
        pathsep = cls.DEF_mya_port_separator
        getBranchFnc_(pathString)
        return lis

    @classmethod
    def _mtl_getObjectPortChildren(cls, objectString, portString):
        lis = []
        _children = cls._dcc_getObjectPortChildren(objectString, portString)
        if _children:
            for _i in _children:
                _fullpathPortnameString = cls.DEF_mya_port_separator.join([portString, _i])
                lis.append(_fullpathPortnameString)

        if cls._dcc_getObjectPortIsColor(objectString, portString):
            if portString == u'outColor':
                _alphaPortnameString = u'outAlpha'
            else:
                _alphaPortnameString = portString + u'A'
            if cls._dcc_getObjectPortIsAppExist(objectString, _alphaPortnameString):
                lis.append(_alphaPortnameString)

        return lis

    @classmethod
    def _mtl_getObjectPortSearchPortkeyStrings(cls, objectString, portString):
        def recursionFnc_(nodeString_, portString_):
            if cls._dcc_getObjectPortHasChildren(nodeString_, portString_):
                _children = cls._mtl_getObjectPortChildren(nodeString_, portString_)
                if _children:
                    for _i in _children:
                        recursionFnc_(nodeString_, _i)
            else:
                lis.append(portString_)

        lis = []
        recursionFnc_(objectString, portString)
        return lis

    @classmethod
    def _mtl_getObjectPortParent(cls, objectString, portString):
        _ = cls._dcc_getObjectPortParent(objectString, portString)
        if _:
            if portString == u'outAlpha':
                return u'outColor'
            elif portString.endswith(u'A'):
                s = portString[:-1]
                if cls._dcc_getObjectPortIsAppExist(objectString, s):
                    return s
                return _
            return _
    # **************************************************************************************************************** #
    @classmethod
    def _mtl_getObjectPortkeyStringList(cls, objectString):
        def recursionFnc_(portnameString_):
            _children = cls._dcc_getObjectPortChildren(objectString, portnameString_)
            if _children:
                for _i in _children:
                    _portnameString = u'{}.{}'.format(portnameString_, _i)
                    lis.append(_portnameString)
                    recursionFnc_(_portnameString)

        lis = []
        portStringList = bscMethods.List.cleanupTo(
            cls.MOD_maya_cmds.listAttr(objectString)
        )
        if portStringList:
            for k in portStringList:
                if cls._dcc_getObjectPortHasParent(objectString, k) is False:
                    lis.append(k)
                    recursionFnc_(k)
        return lis

    @classmethod
    def _mtl_getObjectPortAssignString(cls, objectString, portkeyString):
        _assignString = None
        readable = cls._dcc_getObjectPortIsReadable(objectString, portkeyString)
        writeable = cls._dcc_getObjectPortIsWritable(objectString, portkeyString)
        if (readable, writeable) == (True, True):
            return cls.DEF_mya_keyword_input
        elif (readable, writeable) == (True, False):
            return cls.DEF_mya_keyword_output

    @classmethod
    def _mtl_getObjectPorttypeString(cls, objectString, portkeyString, isArray):
        _portTypeString = cls._dcc_getObjectPorttype(objectString, portkeyString)
        if cls._dcc_getObjectPortIsColor(objectString, portkeyString):
            if portkeyString == u'outColor':
                _alphaPortnameString = u'outAlpha'
            else:
                _alphaPortnameString = portkeyString + u'A'
            if cls._dcc_getObjectPortIsAppExist(objectString, _alphaPortnameString):
                _ = u'color4'
            else:
                _ = u'color3'

            if isArray is True:
                return _ + u'array'
            return _
        elif cls._dcc_getObjectPortIsFilename(objectString, portkeyString):
            return u'filename'
        elif cls._dcc_getObjectPortIsEnumerate(objectString, portkeyString):
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
    def _mtl_getObjectPortDefDict(cls, objectString, portkeyStringList):
        dic = cls.CLS_ordered_dict()
        for portkeyString in portkeyStringList:
            portDict = cls.CLS_ordered_dict()
            assignString = cls._mtl_getObjectPortAssignString(objectString, portkeyString)
            if assignString is not None:
                isArray = cls._mtl_getObjectPortIsArray(objectString, portkeyString)

                porttypeString = cls._mtl_getObjectPorttypeString(objectString, portkeyString, isArray)
                parentPortnameString = cls._mtl_getObjectPortParent(objectString, portkeyString)
                childPortnameStrings = cls._mtl_getObjectPortChildren(objectString, portkeyString)

                portDict[cls.DEF_mya_key_porttype] = porttypeString
                portDict[cls.DEF_mya_key_assign] = assignString
                portDict[cls.DEF_mya_key_parent] = parentPortnameString
                portDict[cls.DEF_mya_key_children] = childPortnameStrings
                portDict[cls.DEF_mya_key_array] = isArray

                dic[portkeyString] = portDict

        return dic

    @classmethod
    def _mtl_getObjectPortIsArray(cls, objectString, portkeyString):
        def recursionFnc_(objectString_, portString_):
            if cls._dcc_getObjectPortIsAppExist(objectString_, portString_):
                _indexes = cls._dcc_getObjectPortIndexes(objectString_, portString_)
                _children = cls._dcc_getObjectPortChildren(objectString_, portString_)

                _hasIndex = _indexes != []
                _hasChild = _children != []

                _check = (_hasIndex, _hasChild)
                if _indexes:
                    return True

                if _check == (True, True):
                    for index_ in _indexes:
                        for childPortname in _children:
                            _fullpathPortnameString = u'{}[{}].{}'.format(portString_, index_, childPortname)
                            recursionFnc_(objectString_, _fullpathPortnameString)
                elif _check == (True, False):
                    for index_ in _indexes:
                        _fullpathPortnameString = u'{}[{}]'.format(portString_, index_)
                        recursionFnc_(objectString_, _fullpathPortnameString)
                elif _check == (False, True):
                    for childPortname in _children:
                        _fullpathPortnameString = u'{}.{}'.format(portString_, childPortname)
                        recursionFnc_(objectString_, _fullpathPortnameString)
                return False
        portpath = cls._mtl_getObjectPortpath_(portkeyString)
        for seq, i in enumerate(portpath):
            return recursionFnc_(objectString, i)
        return False

    @classmethod
    def _mtl_getObjectPortkeyStringDict(cls, objectString, portStringList):
        def recursionFnc_(portString_):
            _children = cls._dcc_getObjectPortChildren(objectString, portString_)
            if _children:
                for _i in _children:
                    _fullpathPortnameString = u'{}.{}'.format(portString_, _i)
                    dic[_i] = _fullpathPortnameString
                    recursionFnc_(_fullpathPortnameString)

        dic = cls.CLS_ordered_dict()
        if portStringList:
            for i in portStringList:
                if cls._dcc_getObjectPortHasParent(objectString, i) is False:
                    dic[i] = i
                    recursionFnc_(i)
        return dic
    # **************************************************************************************************************** #
    @classmethod
    def _mtl_getObjectPortFormatString(cls, objectString, portkeyString):
        portpath = cls._mtl_getObjectPortpath_(portkeyString)
        s = ''
        _ = []
        for seq, i in enumerate(portpath):
            _portname = i.split(cls.DEF_mya_port_separator)[-1]
            if cls._dcc_getObjectPortIsArray(objectString, i) is True:
                _indexString = u'[{{{}}}]'.format(len(_))
                if seq > 0:
                    s += (cls.DEF_mya_port_separator + _portname + _indexString)
                else:
                    s += (_portname + _indexString)
                _.append(True)
            else:
                if seq > 0:
                    s += '.' + _portname
                else:
                    s += _portname
        if _:
            return s

    @classmethod
    def _mtl_getObjectPortdata_(cls, objectString, portkeyString, asString):
        exclude_datatype_list = [
            'mesh',
            'attributeAlias',
        ]
        if cls._dcc_getObjectPortIsAppExist(objectString, portkeyString) is True:
            if cls._dcc_getObjectPortIsMessage(objectString, portkeyString):
                if cls._dcc_getObjectPortHasSource(objectString, portkeyString):
                    return bscMethods.MaAttributeString.nodeString(
                        cls._dcc_getObjectPortSource(objectString, portkeyString)
                    )
                return ''
            elif cls._dcc_getObjectPortIsEnumerate(objectString, portkeyString):
                return cls.MOD_maya_cmds.getAttr(
                            cls._dcc_toAttributeString(objectString, portkeyString),
                            asString=asString,
                            silent=1
                        )
            else:
                porttype = cls._dcc_getObjectPorttype(objectString, portkeyString)
                datatype = cls._dcc_getObjectPorttype(objectString, portkeyString)
                if not datatype in exclude_datatype_list:
                    return cls.MOD_maya_cmds.getAttr(
                                cls._dcc_toAttributeString(objectString, portkeyString), silent=1
                            )

    @classmethod
    def _mtl_getObjectPortdata(cls, objectString, portkeyString):
        def getArrayPortdataFnc_(objectString_, portStrings_):
            return [
                cls._mtl_getObjectPortdata_(
                    objectString_,
                    _l,
                    asString=False
                )
                for _l in portStrings_
            ]

        def getArrayFnc_(objectString_, formatStrings_):
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
            return getArrayPortdataFnc_(objectString_, _lis_)

        def getMultiBranchFnc_(objectString_, portkeyString_):
            _lis = []
            _isArrayEnable = False
            _portkeyStringList = cls._mtl_getObjectPortSearchPortkeyStrings(objectString_, portkeyString_)
            for _i in _portkeyStringList:
                _format = cls._mtl_getObjectPortFormat(objectString_, _i)
                if _format is not None:
                    _isArrayEnable = True
                    _lis.append(_format)
                else:
                    _lis.append(_i)

            if _isArrayEnable is True:
                return getArrayFnc_(objectString_, _lis)
            else:
                return getArrayPortdataFnc_(objectString_, _lis)

        if cls._dcc_getObjectPortHasChildren(objectString, portkeyString) is True:
            return getMultiBranchFnc_(objectString, portkeyString)
        else:
            format_ = cls._mtl_getObjectPortFormat(objectString, portkeyString)
            if format_ is not None:
                formatString, indexArray = format_
                return getArrayFnc_(objectString, [(formatString, indexArray)])
            else:
                return cls._mtl_getObjectPortdata_(
                    objectString,
                    portkeyString,
                    asString=True
                )

    @classmethod
    def _mtl_getObjectPortIndexArray(cls, objectString, portkeyString):
        def recursionFnc_(objectString_, portString_):
            if cls._dcc_getObjectPortIsAppExist(objectString_, portString_):
                key = cls._mtl_getObjectPortkey_(portString_)
                _indexes = cls._dcc_getObjectPortIndexes(objectString_, portString_)
                _children = cls._dcc_getObjectPortChildren(objectString_, portString_)

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
                            recursionFnc_(objectString_, _fullpathPortnameString)
                elif _check == (True, False):
                    for index_ in _indexes:
                        _fullpathPortnameString = u'{}[{}]'.format(portString_, index_)
                        recursionFnc_(objectString_, _fullpathPortnameString)
                elif _check == (False, True):
                    for childPortname in _children:
                        _fullpathPortnameString = u'{}.{}'.format(portString_, childPortname)
                        recursionFnc_(objectString_, _fullpathPortnameString)
        dic = {}
        portpath = cls._mtl_getObjectPortpath_(portkeyString)
        for i in portpath:
            recursionFnc_(objectString, i)
        return dic

    @classmethod
    def _mtl_getObjectPortFormat(cls, objectString, portkeyString):
        indexArrayDict = cls._mtl_getObjectPortIndexArray(objectString, portkeyString)
        portpath = cls._mtl_getObjectPortpath_(portkeyString)
        _portString = ''
        _lis = []
        for seq, i in enumerate(portpath):
            _portname = i.split(cls.DEF_mya_port_separator)[-1]
            if i in indexArrayDict:
                indexes = indexArrayDict[i]
                _indexString = u'[{{{}}}]'.format(len(_lis))
                if seq > 0:
                    _portString += (cls.DEF_mya_port_separator + _portname + _indexString)
                else:
                    _portString += (_portname + _indexString)
                _lis.append(indexes)
            else:
                if seq > 0:
                    _portString += (cls.DEF_mya_port_separator + _portname)
                else:
                    _portString += _portname
        if _lis:
            return _portString, bscMethods.NestedArray.restructureTo(_lis)


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
    def _getAttributeQueryNameString(cls, attributeString):
        _ = attributeString.split(cls.DEF_mya_port_separator)[-1]
        if _.endswith(u']'):
            return _.split(u'[')[0]
        return _

    @classmethod
    def _toAttributePortsepSplit(cls, attributeString):
        _ = attributeString.split(cls.DEF_mya_port_separator)
        return _[0], cls.DEF_mya_port_separator.join(_[1:])

    @classmethod
    def _getAttributeType(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            attributeType=1
        )

    @classmethod
    def _getAttributeData(cls, attributeString):
        if cls._getAttributeIsAppExist(attributeString) is True:
            if cls._getAttributeIsMessage(attributeString):
                if cls._getAttributeHasSource(attributeString):
                    return bscMethods.MaAttributeString.nodeString(cls._getAttributeSource(attributeString))
            else:
                return cls.MOD_maya_cmds.getAttr(attributeString, silent=1)

    @classmethod
    def _getAttributePorttype(cls, attributeString):
        if cls._getAttributeIsEnum(attributeString):
            return 'string'
        elif cls._getAttributeIsColor(attributeString):
            return 'color'
        elif cls._getAttributeIsFilename(attributeString):
            return 'filename'
        _ = cls._getAttributeType(attributeString)
        if _ in cls.DEF_mya_porttype_dict:
            return cls.DEF_mya_porttype_dict[_]
        return _

    @classmethod
    def _getAttributePortdata(cls, attributeString, asString):
        exclude_datatype_list = [
            'mesh',
            'attributeAlias',
            'TdataCompound',
        ]
        exclude_porttype_list = [
            'polyFaces'
        ]
        if cls._getAttributeIsAppExist(attributeString) is True:
            if cls._getAttributeIsMessage(attributeString):
                if cls._getAttributeHasSource(attributeString):
                    return bscMethods.MaAttributeString.nodeString(cls._getAttributeSource(attributeString))
                return ''
            else:
                porttype = cls._getAttributePorttype(attributeString)
                if porttype not in exclude_porttype_list:
                    datatype = cls._getAttributeDatatype(attributeString)
                    attributeString = cls._getAttributeString_(attributeString)
                    if datatype == 'enum':
                        return cls.MOD_maya_cmds.getAttr(attributeString, asString=asString, silent=1)
                    elif datatype not in exclude_datatype_list:
                        _ = cls.MOD_maya_cmds.getAttr(attributeString, silent=1)
                        if datatype in cls.DEF_mya_datatype_compchannel_list:
                            return list(_[0])
                        return _

    @classmethod
    def _getAttributeIsAppExist(cls, attributeString):
        attributeString = cls._getAttributeString_(attributeString)
        return cls.MOD_maya_cmds.objExists(attributeString)

    @classmethod
    def _getAttributeIsNodeExist(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            exists=1
        )

    @classmethod
    def _getAttributeIsCompound(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            usesMultiBuilder=1
        )

    @classmethod
    def _getAttributeIsMultichannel(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            multi=1
        )

    @classmethod
    def _getAttributeIndexes(cls, attributeString):
        """
        :param attributeString: etc. aiRampFloat1.ramp
        :return:
        """
        attributeString = cls._getAttributeString_(attributeString)
        return cls.MOD_maya_cmds.getAttr(attributeString, multiIndices=1, silent=1) or []

    @classmethod
    def _getAttributeIsMessage(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            message=1
        )

    @classmethod
    def _getAttributeIsColor(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            usedAsColor=1
        )

    @classmethod
    def _getAttributeIsFilename(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            usedAsFilename=1
        )

    @classmethod
    def _getAttributeIsEnum(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            enum=1
        )

    @classmethod
    def _getAttributeNicename(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            niceName=1
        )

    @classmethod
    def _getAttributeHasParent(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            listParent=1
        ) is not None

    @classmethod
    def _getAttributeParentPortname(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        _ = cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            listParent=1
        )
        if _:
            return _[0]

    @classmethod
    def _getAttributeHasChild(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            numberOfChildren=1
        ) > 0

    @classmethod
    def _getAttributeChildPortnameList(cls, attributeString):
        nodeString, portString = cls._getAttributeQueryString_(attributeString)
        return cls.MOD_maya_cmds.attributeQuery(
            cls._getAttributeQueryNameString(portString),
            node=nodeString,
            listChildren=1
        ) or []

    @classmethod
    def _getAttributeQueryString_(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            nodeString, portString = attributeString
        else:
            nodeString, portString = cls._toAttributePortsepSplit(attributeString)
        return nodeString, portString

    @classmethod
    def _getAttributeString_(cls, attributeString):
        if isinstance(attributeString, (tuple, list)):
            attributeString = cls.DEF_mya_port_separator.join(list(attributeString))
        return attributeString

    @classmethod
    def _getAttributeHasChannels(cls, attributeString):
        return cls._getAttributePorttype(attributeString) in cls.DEF_mya_datatype_compchannel_list

    @classmethod
    def _getAttributeChannelnameList(cls, attributeString):
        if cls._getAttributeHasChannels(attributeString):
            return cls._getAttributeChildPortnameList(attributeString)
        return []

    @classmethod
    def _getAttributeDefaultData(cls, attributeString):
        pass

    @classmethod
    def _getAttributeDatatype(cls, attributeString):
        attributeString = cls._getAttributeString_(attributeString)
        return cls.MOD_maya_cmds.getAttr(attributeString, type=1, silent=1)

    @classmethod
    def _getAttributeHasSource(cls, attributeString):
        attributeString = cls._getAttributeString_(attributeString)
        return cls.MOD_maya_cmds.connectionInfo(attributeString, isExactDestination=1)

    @classmethod
    def _getAttributeIsSource(cls, attributeString):
        attributeString = cls._getAttributeString_(attributeString)
        return cls.MOD_maya_cmds.connectionInfo(attributeString, isExactSource=1)

    @classmethod
    def _getAttributeSource(cls, attributeString):
        attributeString = cls._getAttributeString_(attributeString)
        return cls.MOD_maya_cmds.connectionInfo(attributeString, sourceFromDestination=1)

    @classmethod
    def _getAttributeHasTargets(cls, attributeString):
        return cls.MOD_maya_cmds.connectionInfo(attributeString, isExactSource=1)

    @classmethod
    def _getAttributeIsTarget(cls, attributeString):
        return cls.MOD_maya_cmds.connectionInfo(attributeString, isExactDestination=1)

    @classmethod
    def _getAttributeTargetList(cls, attributeString):
        attributeString = cls._getAttributeString_(attributeString)
        return cls.MOD_maya_cmds.connectionInfo(attributeString, destinationFromSource=1) or []

    @classmethod
    def _getAttributeNodeString(cls, attributeString):
        return bscMethods.MaAttributeString.nodeString(attributeString)

    @classmethod
    def _getAttributeFullpathPortname(cls, attributeString):
        return bscMethods.MaAttributeString.fullpathPortname(attributeString)

    @classmethod
    def _getAttributePortname(cls, attributeString):
        return bscMethods.MaAttributeString.name(attributeString)


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
    def _setMaFileExportSelected(cls, fileString, objectString, withHistory=False):
        temporaryFile = bscMethods.OsFile.temporaryName(fileString)
        cls.MOD_maya_cmds.select(objectString)
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
    def _setMaFileExportSelectedWithSet(cls, fileString, objectString, setString, withHistory=False):
        cls.MOD_maya_cmds.select(clear=1)
        cls.MOD_maya_cmds.select(objectString)

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
    def _getNodeIsGroup(cls, nodeString):
        boolean = False
        # category is "transform" and has no "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodeString) == cls.DEF_mya_type_transform:
            _ = cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if _ is None:
                boolean = True
        return boolean

    @classmethod
    def _getNodeIsTransform(cls, nodeString):
        boolean = False
        # category is "transform" and has "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodeString) == cls.DEF_mya_type_transform:
            _ = cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if _ is not None:
                boolean = True
        return boolean

    @classmethod
    def _getNodeIsShape(cls, nodeString):
        boolean = False
        # parent is "transform" and has no "shape(s)"
        if cls.MOD_maya_cmds.nodeType(nodeString) != cls.DEF_mya_type_transform:
            transformPath = cls._getNodeTransformNodeString(nodeString)
            _ = cls._getNodeShapeNodeStringList(nodeString)
            if transformPath and not _:
                boolean = True
        return boolean

    @classmethod
    def _isNodeDag(cls, nodeString):
        return cls.DEF_mya_node_separator in cls._getNodeFullpathNameString(nodeString)

    @classmethod
    def _getNodeUniqueIdString(cls, nodeString):
        if cls._isAppExist(nodeString):
            stringLis = cls.MOD_maya_cmds.ls(nodeString, uuid=1)
            if stringLis:
                return stringLis[0]

    @classmethod
    def _getNodeCategoryString(cls, nodeString):
        return cls.MOD_maya_cmds.nodeType(nodeString)

    @classmethod
    def _getNodeShapeCategoryString(cls, nodeString):
        string = cls._getNodeCategoryString(nodeString)
        if string == cls.DEF_mya_type_transform:
            shapePathString = cls._getNodeShapeNodeString(nodeString)
            if shapePathString:
                string = cls._getNodeCategoryString(shapePathString)
        return string

    @classmethod
    def _getNodeTransformNodeString(cls, nodeString, fullpath=True):
        if cls._isAppExist(nodeString):
            if cls._getNodeCategoryString(nodeString) == cls.DEF_mya_type_transform:
                if fullpath:
                    return cls._getNodeFullpathNameString(nodeString)
                else:
                    return bscMethods.MaNodeString.nodenameWithNamespace(nodeString)
            else:
                stringLis = cls.MOD_maya_cmds.listRelatives(nodeString, parent=1, fullPath=fullpath)
                if stringLis:
                    return stringLis[0]

    @classmethod
    def _getNodeShapeNodeString(cls, nodeString, fullpath=True):
        string = None
        if cls._getNodeCategoryString(nodeString) == cls.DEF_mya_type_transform:
            stringLis = cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=1, fullPath=fullpath)
            if stringLis:
                string = stringLis[0]
        else:
            if fullpath:
                string = cls._getNodeFullpathNameString(nodeString)
            else:
                string = bscMethods.MaNodeString.nodenameWithNamespace(nodeString)
        return string

    @classmethod
    def _getNodeShapeNodeStringList(cls, nodeString, fullpath=True):
        return cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=0, fullPath=fullpath) or []

    @classmethod
    def _getNodeTargetNodeStringList(cls, nodeString, includeCategoryString=None):
        if includeCategoryString is not None:
            return cls.MOD_maya_cmds.listConnections(nodeString, destination=1, source=0, type=includeCategoryString) or []
        return cls.MOD_maya_cmds.listConnections(nodeString, destination=1, source=0) or []

    @classmethod
    def _getNodeSourceNodeStringList(cls, nodeString, includeCategoryString=None):
        if includeCategoryString is not None:
            return cls.MOD_maya_cmds.listConnections(nodeString, destination=0, source=1, type=includeCategoryString) or []
        return cls.MOD_maya_cmds.listConnections(nodeString, destination=0, source=1) or []

    @classmethod
    def _getNodeShadingEngineNodeStringList(cls, nodeString, excludeNodeString=None):
        def branchFnc_(subObjectString):
            shapePathString = cls._getNodeShapeNodeString(subObjectString)
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
        stringLis = cls._toAppExistStringList(nodeString)

        if excludeNodeString is not None:
            excludeNodeString = bscMethods.String.toList(excludeNodeString)

        [branchFnc_(i) for i in stringLis]
        return lis

    @classmethod
    def _getShadingEngineObjectSetDatumList(cls, nodeString):
        """
        :param nodeString: str
        :return: list
        """
        lis = []
        #
        objSetLis = cls.MOD_maya_cmds.sets(nodeString, query=1)
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
    def _getNodeAllTargetNodeStringList(cls, nodeString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        def recursionFnc_(nodeString_):
            if extend is True:
                searchNodes = [cls._getNodeTransformNodeString(nodeString_), cls._getNodeShapeNodeString(nodeString_)]
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
        recursionFnc_(nodeString)
        #
        return lis

    @classmethod
    def _getNodeAllSourceNodeStringList(cls, nodeString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        def addFnc_(nodeString_):
            if not nodeString_ in lis:
                lis.append(nodeString_)

        def recursionFnc_(nodeString_):
            if extend is True:
                searchNodes = [cls._getNodeTransformNodeString(nodeString_), cls._getNodeShapeNodeString(nodeString_)]
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
        recursionFnc_(nodeString)
        #
        return lis


class Mtd_MaNodeGraph(Mtd_MaUtility):
    @classmethod
    def _getNodeGraphNodeStringList(cls, nodeString, includeCategoryString=None, excludeCategoryString=None, useShapeCategory=False, extend=False):
        return Mtd_MaObject._getNodeAllSourceNodeStringList(
            nodeString,
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
