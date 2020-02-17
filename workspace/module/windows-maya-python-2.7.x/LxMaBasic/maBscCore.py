# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxBasic import bscMethods

from LxMaBasic import maBscConfigure


class UtilityBasic(maBscConfigure.Utility):
    MOD_maya_cmds = cmds
    @staticmethod
    def _setListCleanup(lis):
        lis_ = list(set(lis))
        lis_.sort(key=lis.index)
        return lis_

    @classmethod
    def _isNodeExist(cls, nodeString):
        return cls.MOD_maya_cmds.objExists(nodeString)

    @classmethod
    def _getNodeUniqueIdString(cls, nodeString):
        if cls._isNodeExist(nodeString):
            stringLis = cls.MOD_maya_cmds.ls(nodeString, uuid=1)
            if stringLis:
                return stringLis[0]

    @classmethod
    def _getNodePathString(cls, nodeString):
        if not nodeString.startswith(cls.DEF_separator_node):
            return cls.MOD_maya_cmds.ls(nodeString, long=1)[0]
        else:
            return nodeString


class NodeBasic(UtilityBasic):

    @classmethod
    def _toExistNodeList(cls, nodeString, fullPath=True):
        lis = []
        if isinstance(nodeString, (str, unicode)):
            if cls._isNodeExist(nodeString):
                if fullPath is True:
                    lis = [cls._getNodePathString(nodeString)]
                else:
                    lis = [cls._getNodeNameString(nodeString)]
        elif isinstance(nodeString, (tuple, list)):
            for i in nodeString:
                if cls._isNodeExist(i):
                    if fullPath is True:
                        lis.append(cls._getNodePathString(i))
                    else:
                        lis.append(cls._getNodeNameString(i))
        return lis

    @classmethod
    def _getNodeTypeString(cls, nodeString):
        return cls.MOD_maya_cmds.nodeType(nodeString)

    @classmethod
    def _getNodeShapeTypeString(cls, objectString):
        string = cls._getNodeTypeString(objectString)
        if string == cls.DEF_type_transform:
            shapePathString = cls._getNodeShapeString(objectString)
            if shapePathString:
                string = cls._getNodeTypeString(shapePathString)
        return string

    @classmethod
    def _getNodeNameString(cls, nodePath, includeNamespace=False):
        if includeNamespace is True:
            string = nodePath.split(cls.DEF_separator_node)[-1]
        else:
            string = nodePath.split(cls.DEF_separator_node)[-1].split(cls.DEF_separator_namespace)[-1]
        return string

    @classmethod
    def _getNodeTransformString(cls, nodeString, fullPath=True):
        if cls._isNodeExist(nodeString):
            if cls._getNodeTypeString(nodeString) == cls.DEF_type_transform:
                if fullPath:
                    return cls._getNodePathString(nodeString)
                else:
                    return cls._getNodeNameString(nodeString)
            else:
                stringLis = cls.MOD_maya_cmds.listRelatives(nodeString, parent=1, fullPath=fullPath)
                if stringLis:
                    return stringLis[0]

    @classmethod
    def _getNodeShapeString(cls, nodeString, fullPath=True):
        string = None
        if cls._getNodeTypeString(nodeString) == cls.DEF_type_transform:
            stringLis = cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=1, fullPath=fullPath)
            if stringLis:
                string = stringLis[0]
        else:
            if fullPath:
                string = cls._getNodePathString(nodeString)
            else:
                string = cls._getNodeNameString(nodeString)
        return string

    @classmethod
    def _getNodeShapeStringList(cls, nodeString, fullPath=True):
        return cls.MOD_maya_cmds.listRelatives(nodeString, children=1, shapes=1, noIntermediate=0, fullPath=fullPath) or []

    @classmethod
    def _getNodeTargetStringList(cls, nodeString, includeTypeString=None):
        if includeTypeString is not None:
            return cls.MOD_maya_cmds.listConnections(nodeString, destination=1, source=0, type=includeTypeString) or []
        return cls.MOD_maya_cmds.listConnections(nodeString, destination=1, source=0) or []

    @classmethod
    def _getNodeSourceStringList(cls, nodeString, includeTypeString=None):
        if includeTypeString is not None:
            return cls.MOD_maya_cmds.listConnections(nodeString, destination=0, source=1, type=includeTypeString) or []
        return cls.MOD_maya_cmds.listConnections(nodeString, destination=0, source=1) or []

    @classmethod
    def _getNodeShadingEngineStringList(cls, nodeString):
        def getBranch(subObjectString):
            shapePathString = cls._getNodeShapeString(subObjectString)
            if not shapePathString:
                shapePathString = subObjectString
            #
            outputObjectLis = cls._getNodeTargetStringList(shapePathString, cls.DEF_type_shading_engine)
            if outputObjectLis:
                [lis.append(j) for j in outputObjectLis if not j in lis and not j in cls.DEF_shading_engine_default_list]

        #
        lis = []
        #
        stringLis = cls._toExistNodeList(nodeString)
        [getBranch(i) for i in stringLis]
        return lis

    @classmethod
    def _getShadingEngineObjectSetDatumList(cls, objectString):
        """
        :param objectString: str
        :return: list
        """
        lis = []
        #
        objSetLis = cls.MOD_maya_cmds.sets(objectString, query=1)
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
    def _getNodeAllTargetStringList(cls, nodeString, includeTypeString=None, excludeTypeString=None, useShapeType=False, extend=False):
        def recursionFnc_(nodeString_):
            if extend is True:
                searchNodes = [cls._getNodeTransformString(nodeString_), cls._getNodeShapeString(nodeString_)]
                set(searchNodes)
            else:
                searchNodes = [nodeString_]

            for subNode in searchNodes:
                nodeStrings = cls.MOD_maya_cmds.listConnections(subNode, destination=1, source=0, shapes=1)
                if nodeStrings:
                    for i in nodeStrings:
                        if useShapeType is True:
                            nodeTypeString = cls._getNodeShapeTypeString(i)
                        else:
                            nodeTypeString = cls._getNodeTypeString(i)

                        if includeTypeString is not None:
                            if nodeTypeString in includeTypeString:
                                if not i in lis:
                                    lis.append(i)
                        elif excludeTypeString is not None:
                            if nodeTypeString not in excludeTypeString:
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
        if includeTypeString is not None:
            includeTypeString = bscMethods.String.toList(includeTypeString)
        elif excludeTypeString is not None:
            excludeTypeString = bscMethods.String.toList(excludeTypeString)
        #
        recursionFnc_(nodeString)
        #
        return lis

    @classmethod
    def _getNodeAllSourceStringList(cls, nodeString, includeTypeString=None, excludeTypeString=None, useShapeType=False, extend=False):
        def recursionFnc_(nodeString_):
            if extend is True:
                searchNodes = [cls._getNodeTransformString(nodeString_), cls._getNodeShapeString(nodeString_)]
                set(searchNodes)
            else:
                searchNodes = [nodeString_]

            for subNode in searchNodes:
                nodeStrings = cls.MOD_maya_cmds.listConnections(subNode, destination=0, source=1, shapes=1)
                if nodeStrings:
                    for i in nodeStrings:
                        if useShapeType is True:
                            nodeTypeString = cls._getNodeShapeTypeString(i)
                        else:
                            nodeTypeString = cls._getNodeTypeString(i)

                        print i, nodeTypeString

                        if includeTypeString is not None:
                            if nodeTypeString in includeTypeString:
                                if not i in lis:
                                    lis.append(i)
                        elif excludeTypeString is not None:
                            if nodeTypeString not in excludeTypeString:
                                if not i in lis:
                                    lis.append(i)
                        else:
                            if not i in lis:
                                lis.append(i)
                        #
                        if not i in searchLis:
                            searchLis.append(i)
                            recursionFnc_(i)

        #
        searchLis = []
        #
        lis = []
        #
        if includeTypeString is not None:
            includeTypeString = bscMethods.String.toList(includeTypeString)
        elif excludeTypeString is not None:
            excludeTypeString = bscMethods.String.toList(excludeTypeString)
        #
        recursionFnc_(nodeString)
        #
        return lis

    @classmethod
    def isExist(cls, nodeString):
        return cls._isNodeExist(nodeString)

    @classmethod
    def nodeTypeString(cls, nodeString):
        return cls._getNodeTypeString(nodeString)

    @classmethod
    def transformFullpathName(cls, nodeString):
        return cls._getNodeTransformString(nodeString)

    @classmethod
    def shapeFullpathName(cls, nodeString):
        return cls._getNodeShapeString(nodeString)
