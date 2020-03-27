# coding:utf-8
import re
# noinspection PyUnresolvedReferences
from maya import cmds, mel
# noinspection PyUnresolvedReferences
from maya import OpenMaya, OpenMayaUI
# noinspection PyUnresolvedReferences
import maya.api.OpenMaya as Om2
#
from itertools import product

from LxBasic import bscMethods
#
from LxUi import uiCore
#
from LxUi.qt import qtCore
#
from LxMaya.method.config import _maConfig


#
class Mtd_AppMaya(_maConfig.MaConfig):
    _maConfig = _maConfig.MaConfig
    #
    MaProgressBar = None
    MaMaxProgressValue = 1
    MaProgressValue = 0

    @staticmethod
    def _toNamespaceByPathString(pathString, pathsep, namespacesep):
        return namespacesep.join(pathString.split(pathsep)[-1].split(namespacesep)[:-1]) + namespacesep

    @staticmethod
    def _toNamespaceByNameString(nameString, namespacesep):
        return namespacesep.join(nameString.split(namespacesep)[:-1]) + namespacesep

    @staticmethod
    def _toNameByPathString(pathString, pathsep, namespacesep):
        return pathString.split(pathsep)[-1].split(namespacesep)[-1]

    @staticmethod
    def _toNameByNameString(nameString, namespacesep):
        return nameString.split(namespacesep)[-1]

    @classmethod
    def _isStringMatch(cls, string, keyword):
        if keyword.startswith('*'):
            return string.endswith(keyword[1:])
        elif keyword.endswith('*'):
            return string.startswith(keyword[:-1])
        else:
            return keyword in string

    @classmethod
    def _toPathRebuildDatum(cls, pathString, pathsep, namespacesep):
        if pathString.startswith(pathsep):
            pathLis = []
            namespaceLis = []
            #
            lis1 = pathString.split(pathsep)
            if lis1:
                for i in lis1:
                    if i:
                        namespace = cls._toNamespaceByNameString(i, namespacesep)
                        name = cls._toNameByNameString(i, namespacesep)
                        if namespace:
                            if not namespace in namespaceLis:
                                namespaceLis.append(namespace)
                            #
                            index = namespaceLis.index(namespace)
                            pathLis.append('{{{}}}{}'.format(index, name))
                        else:
                            pathLis.append(i)

            return pathLis, namespaceLis
        else:
            return cls._toNameByNameString(pathString, namespacesep), cls._toNamespaceByNameString(pathString, namespacesep)

    # noinspection PyUnusedLocal
    @classmethod
    def _toPathByPathRebuildDatum(cls, pathDatum, namespaceDatum, pathsep, namespacesep):
        if isinstance(pathDatum, list) or isinstance(pathDatum, tuple):
            return pathsep + pathsep.join(pathDatum).format(*['' if i == namespacesep else i for i in namespaceDatum])
        else:
            return ('' if namespaceDatum == namespacesep else namespaceDatum) + pathDatum

    # noinspection PyUnusedLocal
    @classmethod
    def _toNameStringBySearchDatum(cls, pathDatum, namespaceDatum, pathsep, namespacesep):
        if isinstance(pathDatum, list) or isinstance(pathDatum, tuple):
            return pathDatum[-1].format(*namespaceDatum)
        else:
            return namespaceDatum + pathDatum

    @classmethod
    def _toNodeAttr(cls, stringLis):
        return cls.DEF_mya_port_separator.join(stringLis)

    @classmethod
    def _toAppCompPathLis(cls, nodePath):
        lis = []
        #
        stringLis = nodePath.split(cls.DEF_mya_node_separator)
        #
        count = len(stringLis)
        for seq, i in enumerate(stringLis):
            if i:
                if seq + 1 < count:
                    compPath = cls.DEF_mya_node_separator.join(stringLis[:seq + 1])
                    lis.append(compPath)
        #
        lis.append(nodePath)
        return lis

    @classmethod
    def _nodeString2nodename_(cls, nodePath, withNamespace=False):
        if withNamespace:
            string = nodePath.split(cls.DEF_mya_node_separator)[-1]
        else:
            if nodePath.endswith(']'):
                string = nodePath.split(cls.DEF_mya_node_separator)[-1]
            else:
                string = nodePath.split(cls.DEF_mya_node_separator)[-1].split(cls.DEF_mya_namespace_separator)[-1]
        return string

    @classmethod
    def _getNodeFullpathNameString(cls, nodepathString):
        if not nodepathString.startswith(cls.DEF_mya_node_separator):
            return cmds.ls(nodepathString, long=1)[0]
        else:
            return nodepathString

    @classmethod
    def _toShapeTransformString(cls, nodePath):
        if cls.DEF_mya_node_separator in nodePath:
            return cls.DEF_mya_node_separator.join(nodePath.split(cls.DEF_mya_node_separator)[:-1])
        else:
            return nodePath

    @classmethod
    def _toNodePathRemoveNamespace(cls, nodePath):
        namespace = cls._toNamespaceByNodePath(nodePath)
        if not namespace == cls.DEF_mya_namespace_separator:
            return nodePath.replace(namespace, '')
        else:
            return nodePath

    @classmethod
    def _toNodePathJoinNamespace(cls, nodePath, namespace):
        return cls.DEF_mya_node_separator.join([namespace + i for i in nodePath.split(cls.DEF_mya_node_separator) if i])

    @classmethod
    def _toNamespaceByNodePath(cls, nodePath):
        return cls._toNamespaceByPathString(nodePath, cls.DEF_mya_node_separator, cls.DEF_mya_namespace_separator)

    @classmethod
    def _toNamespaceByNodeName(cls, nodeName):
        return cls._toNamespaceByNameString(nodeName, cls.DEF_mya_namespace_separator)

    @classmethod
    def _toNameByNodePath(cls, nodePath):
        return cls._toNameByPathString(nodePath, cls.DEF_mya_node_separator, cls.DEF_mya_namespace_separator)

    @classmethod
    def _toNameByNodeName(cls, nodeName):
        return cls._toNameByNameString(nodeName, cls.DEF_mya_namespace_separator)

    @classmethod
    def _toNodeNameByAttr(cls, attr):
        return attr.split(cls.DEF_mya_port_separator)[0]

    @classmethod
    def _toAttrName(cls, attr):
        return cls.DEF_mya_port_separator.join(cls._nodeString2nodename_(attr).split(cls.DEF_mya_port_separator)[1:])

    @classmethod
    def _toAppExistStringList(cls, nodepathString, fullPath=True):
        lis = []
        if isinstance(nodepathString, str) or isinstance(nodepathString, unicode):
            if cls._isAppExist(nodepathString):
                if fullPath is True:
                    lis = [cls._getNodeFullpathNameString(nodepathString)]
                else:
                    lis = [cls._nodeString2nodename_(nodepathString)]
        elif isinstance(nodepathString, tuple) or isinstance(nodepathString, list):
            for i in nodepathString:
                if cls._isAppExist(i):
                    if fullPath is True:
                        lis.append(cls._getNodeFullpathNameString(i))
                    else:
                        lis.append(cls._nodeString2nodename_(i))
        return lis

    @classmethod
    def _toNodePathRebuildDatum(cls, nodePath):
        return cls._toPathRebuildDatum(nodePath, cls.DEF_mya_node_separator, cls.DEF_mya_namespace_separator)

    @classmethod
    def _toNodePathBySearchDatum(cls, pathDatum, namespaceDatum):
        return cls._toPathByPathRebuildDatum(
            pathDatum, namespaceDatum, cls.DEF_mya_node_separator, cls.DEF_mya_namespace_separator
        )

    @classmethod
    def _toNodeNameBySearchDatum(cls, pathDatum, namespaceDatum):
        return cls._toNameStringBySearchDatum(
            pathDatum, namespaceDatum,
            cls.DEF_mya_node_separator, cls.DEF_mya_namespace_separator
        )

    @classmethod
    def _toNodeSearchKey(cls, pathDatum, namespaceDatum, ignorePath=False, ignoreNamespace=False):
        if ignorePath is True:
            pathDatum = pathDatum[-1:]
            fn = cls._toNameStringBySearchDatum
        else:
            fn = cls._toPathByPathRebuildDatum
        #
        if ignoreNamespace is True:
            namespaceDatum = ['*:'*(len(i.split(cls.DEF_mya_namespace_separator)) - 1) if i != cls.DEF_mya_namespace_separator else i for i in namespaceDatum]
            subNamespaceDatum = ['']*len(namespaceDatum)
            return fn(
                pathDatum, namespaceDatum,
                cls.DEF_mya_node_separator, cls.DEF_mya_namespace_separator
            ), fn(
                pathDatum, subNamespaceDatum,
                cls.DEF_mya_node_separator, cls.DEF_mya_namespace_separator
            )
        else:
            return fn(
                pathDatum, namespaceDatum,
                cls.DEF_mya_node_separator, cls.DEF_mya_namespace_separator
            )

    @classmethod
    def getNodeLisBySearchKey(cls, searchKey, nodeType, fullPath=True):
        lis = []
        searchKeyLis = bscMethods.String.toList(searchKey)
        for searchKey in searchKeyLis:
            stringLis = cmds.ls(searchKey, type=nodeType, long=fullPath)
            if stringLis:
                [lis.append(i) for i in stringLis if i not in lis]
        return lis

    @classmethod
    def getNodeLisBySearchDatum(cls, nodeType, pathDatum, namespaceDatum, ignorePath=False, ignoreNamespace=False):
        searchKey = cls._toNodeSearchKey(
            pathDatum, namespaceDatum,
            ignorePath, ignoreNamespace
        )
        lis = cls.getNodeLisBySearchKey(searchKey, nodeType)
        return lis

    @classmethod
    def setNodeRename(cls, nodepathString, nameString):
        objectName = cls._nodeString2nodename_(nodepathString)
        if not nameString == objectName:
            if not cls.isNodeLocked(nodepathString):
                cmds.rename(nodepathString, nameString)

    @classmethod
    def setNodeRenameByUniqueId(cls, uniqueId, nameString):
        node = cls.getNodeByUniqueId(uniqueId)
        if node:
            cls.setNodeRename(node, nameString)

    @classmethod
    def _getNodeTransformNodeString(cls, nodepathString, fullPath=True):
        if cls._isAppExist(nodepathString):
            if cls._getNodeCategoryString(nodepathString) == cls.DEF_mya_type_transform:
                if fullPath:
                    return cls._getNodeFullpathNameString(nodepathString)
                else:
                    return cls._nodeString2nodename_(nodepathString)
            else:
                stringLis = cmds.listRelatives(nodepathString, parent=1, fullPath=fullPath)
                if stringLis:
                    return stringLis[0]

    @classmethod
    def getNodeByUniqueId(cls, uniqueId, fullPath=True):
        if bscMethods.UniqueId.isUsable(uniqueId):
            stringLis = cmds.ls(uniqueId, long=fullPath) or []
            if stringLis:
                if len(stringLis) == 1:
                    return stringLis[0]
                else:
                    return stringLis

    @classmethod
    def _getNodeUniqueIdString(cls, nodepathString):
        if cls._isAppExist(nodepathString):
            stringLis = cmds.ls(nodepathString, uuid=1)
            if stringLis:
                return stringLis[0]

    @classmethod
    def getUniqueIdLisByNode(cls, nodepathString):
        lis = []
        nodeLis = cls._toAppExistStringList(nodepathString)
        if nodeLis:
            for node in nodeLis:
                uniqueId = cls._getNodeUniqueIdString(node)
                lis.append(uniqueId)
        return lis

    @classmethod
    def getObjectUniqueId(cls, nodepathString):
        transformPath = cls._getNodeTransformNodeString(nodepathString)
        if transformPath:
            return cls._getNodeUniqueIdString(transformPath)

    @classmethod
    def getObjectUniqueIdLisByNode(cls, nodepathString):
        lis = []
        nodeLis = cls._toAppExistStringList(nodepathString)
        if nodeLis:
            for node in nodeLis:
                uniqueId = cls.getObjectUniqueId(node)
                lis.append(uniqueId)
        return lis

    @classmethod
    def setNodeAttr(cls, nodepathString, attrName, data, lockAttr=False):
        attr = cls._toNodeAttr([nodepathString, attrName])
        if cls._isAppExist(attr):
            if cls.isAttrLock(attr) is True:
                cmds.setAttr(attr, lock=0)
            #
            cmds.setAttr(attr, data)
            if lockAttr is True:
                cmds.setAttr(attr, lock=1)

    @classmethod
    def setAttrStringDatumForce_(cls, nodepathString, attrName, data, lockAttr=True):
        attr = cls._toNodeAttr([nodepathString, attrName])
        if not cls._isAppExist(attr):
            cmds.addAttr(nodepathString, longName=attrName, niceName=bscMethods.StrCamelcase.toPrettify(attrName), dataType='string')
        #
        cmds.setAttr(attr, lock=0)
        cmds.setAttr(attr, data, type='string', lock=lockAttr)

    @classmethod
    def setNodeColorAttr(cls, nodepathString, attrName, r, g, b, dataType='float3'):
        attr = cls._toNodeAttr([nodepathString, attrName])
        if cls._isAppExist(attr):
            cmds.setAttr(attr, r, g, b, type=dataType)

    @staticmethod
    def isAttrLock(attr):
        return cmds.connectionInfo(attr, isLocked=1)

    @classmethod
    def setNodeRgbAttrForce(cls, nodepathString, attrName, r, g, b):
        colorLabelLis = ['R', 'G', 'B']
        attr = cls._toNodeAttr([nodepathString, attrName])
        if not cls._isAppExist(attr):
            cmds.addAttr(nodepathString, longName=attrName, niceName=bscMethods.StrCamelcase.toPrettify(attrName), attributeType='float3', usedAsColor=1)
            for i in colorLabelLis:
                cmds.addAttr(nodepathString, longName=attrName + i, attributeType='float', parent=attrName)
        #
        cmds.setAttr(attr, lock=0)
        cmds.setAttr(attr, r, g, b, type='float3')

    @classmethod
    def setAttrBooleanDatumForce_(cls, nodepathString, attrName, boolean):
        attr = cls._toNodeAttr([nodepathString, attrName])
        if not cls._isAppExist(attr):
            cmds.addAttr(nodepathString, longName=attrName, niceName=bscMethods.StrCamelcase.toPrettify(attrName), attributeType='bool')
        #
        if cls.isAttrLock(attr) is True:
            cmds.setAttr(attr, lock=0)
        #
        cmds.setAttr(attr, boolean)

    @classmethod
    def setObjectTransformationAttr(cls, transformPath, lockTransformation=False, hideTransformation=False):
        attrNameLis = ['translate', 'rotate', 'scale']
        axisLis = ['X', 'Y', 'Z']
        [cmds.setAttr(cls._toNodeAttr([transformPath, attrName + axis]), keyable=0, lock=lockTransformation, channelBox=not hideTransformation) for attrName, axis in product(attrNameLis, axisLis)]

    @classmethod
    def _toNodeParentPath(cls, nodepathString):
        string = None
        objectPath = cls._getNodeFullpathNameString(nodepathString)
        if objectPath:
            data = cls.DEF_mya_node_separator.join(objectPath.split(cls.DEF_mya_node_separator)[:-1])
            if data:
                string = data
        return string

    @staticmethod
    def _getNodeCategoryString(nodepathString):
        return cmds.nodeType(nodepathString)

    @staticmethod
    def getNodeShowType(nodepathString):
        return cmds.ls(nodepathString, showType=1)

    @staticmethod
    def _isAppExist(nodepathString, attrName=None):
        boolean = False
        if nodepathString:
            if attrName:
                nodepathString = nodepathString + '.' + attrName
            boolean = cmds.objExists(nodepathString)
        return boolean

    @staticmethod
    def isAppVisible(nodepathString):
        return True if cmds.ls(nodepathString, visible=1) else False

    @staticmethod
    def _getNodeTargetNodeStringList(nodepathString, nodeTypeString=None):
        if nodeTypeString is not None:
            return cmds.listConnections(nodepathString, destination=1, source=0, type=nodeTypeString) or []
        else:
            return cmds.listConnections(nodepathString, destination=1, source=0) or []

    @classmethod
    def toSetName(cls, setPath, withNamespace=False):
        if withNamespace:
            string = setPath.split(cls.DEF_mya_set_separator)[-1]
        else:
            string = setPath.split(cls.DEF_mya_set_separator)[-1].split(cls.DEF_mya_namespace_separator)[-1]
        return string

    @classmethod
    def getNodeLisByType(cls, nodeTypeString, fullPath=True, exceptStrings=None):
        lis = []
        filterTypeLis = bscMethods.String.toList(nodeTypeString, cmds.allNodeTypes())
        if filterTypeLis:
            lis = cmds.ls(type=filterTypeLis, long=fullPath) or []
            if exceptStrings is not None:
                if lis:
                    [lis.remove(i) for i in exceptStrings if i in lis]
        return lis
    @classmethod
    def getShapeLisByType(cls, nodeTypeString, fullPath=True, exceptStrings=None):
        pass
    @staticmethod
    def setSelectClear():
        cmds.select(clear=1)
    @classmethod
    def setNodeSelect(cls, nodepathString, noExpand=False):
        objectLis = cls._toAppExistStringList(nodepathString)
        #
        cls.setSelectClear()
        cmds.select(objectLis, noExpand=noExpand)
    @classmethod
    def getNodeLisByFilter(cls, nodeTypeString, namespace=None, fullPath=True):
        lis = []
        #
        namespaceLis = bscMethods.String.toList(namespace)
        nodeLis = cls.getNodeLisByType(nodeTypeString, fullPath)
        if namespaceLis:
            for namespace in namespaceLis:
                namespace += ':'
                [lis.append(n) for n in nodeLis if n.startswith(namespace) and not n in lis]
        else:
            lis = nodeLis
        return lis
    @staticmethod
    def isNodeLocked(nodepathString):
        return cmds.lockNode(nodepathString, query=1, lock=1)[0]
    @staticmethod
    def setNodeShowByGroup(groupString):
        cmds.showHidden(groupString, below=True)
    @classmethod
    def setElementSet(cls, nodepathString, parentString):
        if not cls._isAppExist(parentString):
            cmds.sets(name=parentString, empty=1)
        #
        cmds.sets(nodepathString, forceElement=parentString, edit=1)
    @staticmethod
    def getSelectedNodeLis(fullPath=True):
        return cmds.ls(selection=1, long=fullPath) or []
    @classmethod
    def updateProgressBar(cls):
        if cls.MaProgressBar is None:
            cls.MaProgressBar = mel.eval('$lynxiProgressVar = $gMainProgressBar')
    @classmethod
    def viewProgress(cls, explain, maxValue):
        if maxValue > 0:
            cls.updateProgressBar()
            cls.MaMaxProgressValue = maxValue
            cls.MaProgressValue = 0
            #
            cmds.progressBar(
                cls.MaProgressBar,
                edit=True,
                beginProgress=True,
                isInterruptable=True,
                status=explain,
                maxValue=maxValue
            )
    @classmethod
    def updateProgress(cls):
        if cls.MaProgressBar is not None:
            cls.MaProgressValue += 1
            if cls.MaProgressValue == cls.MaMaxProgressValue:
                cls.closeProgress()
            else:
                cmds.progressBar(cls.MaProgressBar, edit=True, step=1)
    @classmethod
    def closeProgress(cls):
        cmds.progressBar(cls.MaProgressBar, edit=True, endProgress=True)
    @staticmethod
    def getNodeTypeLisByFilter(nodeTypeString):
        return cmds.listNodeTypes(nodeTypeString)
    @classmethod
    def traceWaning(cls, string):
        cmds.warning(string)
    @staticmethod
    def setMessageWindowShow(message, keyword, position='topCenter', fade=1, dragKill=0, alpha=.5):
        # topLeft topCenter topRight
        # midLeft midCenter midCenterTop midCenterBot midRight
        # botLeft botCenter botRight
        assistMessage = '%s <hl>%s</hl>' % (message, keyword)
        cmds.inViewMessage(
            assistMessage=assistMessage,
            fontSize=12,
            position=position,
            fade=fade,
            dragKill=dragKill,
            alpha=alpha
        )
    @staticmethod
    def getNodeWorldMatrix(nodepathString):
        return cmds.xform(nodepathString, query=1, matrix=1, worldSpace=1) or [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    @classmethod
    def isDefaultMatrix(cls, nodepathString):
        return cls.getNodeWorldMatrix(nodepathString) == cls.DEF_mya_default_matrix
    @staticmethod
    def setNodeWorldMatrix(nodepathString, worldMatrix):
        cmds.xform(nodepathString, matrix=worldMatrix, worldSpace=1)
    @staticmethod
    def setUndoChunkOpen():
        cmds.undoInfo(openChunk=1)
    @staticmethod
    def setUndoChunkClose():
        cmds.undoInfo(closeChunk=1)
    @staticmethod
    def isMeshFaceComp(nodepathString):
        expression = r'(\.f\[.*?\])'
        search = re.search(expression, nodepathString)
        if search is not None:
            return search.groups()[0]
    @staticmethod
    def isMeshEdgeComp(nodepathString):
        expression = r'(\.e\[.*?\])'
        search = re.search(expression, nodepathString)
        if search is not None:
            return search.groups()[0]
    @staticmethod
    def isMeshVertexComp(nodepathString):
        expression = r'(\.vtx\[.*?\])'
        search = re.search(expression, nodepathString)
        if search is not None:
            return search.groups()[0]
    @classmethod
    def _toMeshFaceComp(cls, nodepathString, ids):
        lis = []
        if ids:
            reduceArray = bscMethods.List.toFrameRange(ids)
            for i in reduceArray:
                if isinstance(i, int):
                    lis.append('{}.f[{}]'.format(nodepathString, i))
                elif isinstance(i, tuple):
                    lis.append('{}.f[{}:{}]'.format(nodepathString, *i))
        #
        return lis
    @classmethod
    def _toMeshEdgeComp(cls, nodepathString, ids):
        lis = []
        if ids:
            reduceArray = bscMethods.List.toFrameRange(ids)
            for i in reduceArray:
                if isinstance(i, int):
                    lis.append('{}.e[{}]'.format(nodepathString, i))
                elif isinstance(i, tuple):
                    lis.append('{}.e[{}:{}]'.format(nodepathString, *i))
        #
        return lis
    @classmethod
    def _toMeshVertexComp(cls, nodepathString, ids):
        lis = []
        if ids:
            reduceArray = bscMethods.List.toFrameRange(ids)
            for i in reduceArray:
                if isinstance(i, int):
                    lis.append('{}.vtx[{}]'.format(nodepathString, i))
                elif isinstance(i, tuple):
                    lis.append('{}.vtx[{}:{}]'.format(nodepathString, *i))
        #
        return lis


#
class Mtd_M2Basic(Mtd_AppMaya, _maConfig.Cfg_M2):
    @staticmethod
    def toM2NodePath(nodepathString):
        return Om2.MGlobal.getSelectionListByName(nodepathString).getDagPath(0)
    @classmethod
    def toM2TransformNode(cls, nodepathString, mode=0):
        if mode == 0:
            return Om2.MFnTransform(cls.toM2NodePath(nodepathString))
        elif mode == 1:
            return Om2.MFnTransform(nodepathString)
    @classmethod
    def toM2DagNode(cls, nodepathString, mode=0):
        if mode == 0:
            return Om2.MFnDagNode(cls.toM2NodePath(nodepathString))
        elif mode == 1:
            return Om2.MFnDagNode(nodepathString)
    @staticmethod
    def toM2Point(point):
        m2Point = Om2.MPoint()
        m2Point.x, m2Point.y, m2Point.z = point
        return m2Point
    @staticmethod
    def toM2Matrix(matrix):
        m2Matrix = Om2.MMatrix()
        for seq in range(4):
            for subSeq in range(4):
                m2Matrix.setElement(seq, subSeq, matrix[seq * 4 + subSeq])
        return m2Matrix


#
class Mtd_MaUiBasic(
    uiCore.UiMtdBasic,
    _maConfig.MaUiConfig
):
    @staticmethod
    def _toQtObject(ptr, base=qtCore.QWidget):
        # noinspection PyUnresolvedReferences
        return qtCore.qtWrapinstance(long(ptr), base)
    @classmethod
    def _toQtWidget(cls, controlName, base=qtCore.QWidget):
        ptr = OpenMayaUI.MQtUtil.findControl(controlName)
        if ptr is not None:
            return cls._toQtObject(ptr, base)
    @classmethod
    def getUiMainWindow(cls):
        return cls._toQtWidget(cls.MaUiName_MainWindow, qtCore.QMainWindow)
    @classmethod
    def getUiMainControl(cls):
        return cls._toQtWidget(cls.MaUiName_MainControl)
    @classmethod
    def getUiMenuBar(cls):
        for eachChild in cls.getUiMainWindow().children():
            if type(eachChild) == qtCore.QMenuBar:
                return eachChild
    @classmethod
    def getResultByDialog(cls, **kwargs):
        return cmds.confirmDialog(**kwargs)


#
class MaPresetMethodBasic(Mtd_AppMaya, _maConfig.MaUnitConfig):
    @staticmethod
    def _getUnitCommand(kwargs):
        return cmds.currentUnit(query=1, **kwargs)
    @staticmethod
    def _setUnitCommand(kwargs):
        cmds.currentUnit(**kwargs)
    @classmethod
    def getTimeUnit(cls):
        return cls._getUnitCommand({cls.MaUnit_Key_Time: True})
    @classmethod
    def setTimeUnit(cls, unit):
        if unit in cls.MaUnit_UiDic_Time:
            cls._setUnitCommand({cls.MaUnit_Key_Time: True})
        else:
            raise ValueError('Time - Unit is Invalid !!!')
    @classmethod
    def getAngleUnit(cls):
        return cls._getUnitCommand({cls.MaUnit_Key_Angle: True})
    @classmethod
    def setAngleUnit(cls, unit):
        if unit in cls.MaUnit_UiDic_Angle:
            cls._setUnitCommand({cls.MaUnit_Key_Angle: True})
        else:
            raise ValueError('Angle - Unit is Invalid !!!')
    @classmethod
    def getLinearUnit(cls):
        return cls._getUnitCommand({cls.MaUnit_Key_Linear: True})
    @classmethod
    def setLinearUnit(cls, unit):
        if unit in cls.MaUnit_UiDic_Linear:
            cls._setUnitCommand({cls.MaUnit_Key_Linear: True})
        else:
            raise ValueError('Linear - Unit is Invalid !!!')
    @classmethod
    def getUnitOptionDic(cls):
        dic = {}
        for k in [cls.MaUnit_Key_Time, cls.MaUnit_Key_Angle, cls.MaUnit_Key_Linear]:
            dic[k] = cls._getUnitCommand({k: True})
        return dic
    @classmethod
    def setUnitOption(cls, unitDic):
        if unitDic:
            for k, v in unitDic:
                cls._setUnitCommand({k: True})


#
class MaScriptJobMethodBasic(Mtd_AppMaya):
    @classmethod
    def setCreateEventScriptJob(cls, windowName, scriptJobEvn, method):
        if method:
            if not cmds.window(windowName, exists=1):
                cmds.window(windowName, title=bscMethods.StrCamelcase.toPrettify(windowName), sizeable=1, resizeToFitChildren=1)
            #
            if isinstance(method, list):
                [cmds.scriptJob(parent=windowName, event=[scriptJobEvn, i]) for i in method]

            else:
                cmds.scriptJob(parent=windowName, event=[scriptJobEvn, method])
    @classmethod
    def setCreateNodeDeleteScriptJob(cls, windowName, node, method):
        if method:
            if not cmds.window(windowName, exists=1):
                cmds.window(windowName, title=bscMethods.StrCamelcase.toPrettify(windowName), sizeable=1, resizeToFitChildren=1)
            #
            if isinstance(method, list):
                [cmds.scriptJob(parent=windowName, nodeDeleted=[node, i]) for i in method]
            else:
                cmds.scriptJob(parent=windowName, nodeDeleted=[node, method])
    @classmethod
    def setCreateAttrChangedScriptJob(cls, windowName, attr, method):
        if method:
            if not cmds.window(windowName, exists=1):
                cmds.window(windowName, title=bscMethods.StrCamelcase.toPrettify(windowName), sizeable=1, resizeToFitChildren=1)
            #
            if isinstance(method, list):
                [cmds.scriptJob(parent=windowName, attributeChange=[attr, i]) for i in method]
            else:
                cmds.scriptJob(parent=windowName, attributeChange=[attr, method])


#
class MaSetMethodBasic(Mtd_AppMaya, _maConfig.MaConfig):
    @classmethod
    def toCompSetPathLis(cls, setPath):
        lis = []
        #
        stringLis = setPath.split(cls.DEF_mya_set_separator)
        #
        for seq, data in enumerate(stringLis):
            if data:
                if seq > 0:
                    compPath = cls.DEF_mya_set_separator.join(stringLis[seq - 1:seq + 1])
                else:
                    compPath = cls.DEF_mya_set_separator.join(stringLis[:seq + 1])
                #
                lis.append(compPath)
        return lis
    @classmethod
    def getSetParentLis(cls, setString):
        return cmds.listSets(object=setString) or []
    @classmethod
    def setElementSetCreate(cls, setString):
        if not cls._isAppExist(setString):
            cmds.sets(name=setString, empty=1)
    @classmethod
    def setCompSetPathCreate(cls, compSetPath):
        splitLis = compSetPath.split(cls.DEF_mya_set_separator)
        if len(splitLis) > 1:
            setParent, setChild = splitLis
            cls.setElementSetCreate(setParent)
            #
            cls.setElementSetCreate(setChild)
            #
            setParentLis = cls.getSetParentLis(setChild)
            if not setChild in setParentLis:
                cmds.sets(setChild, forceElement=setParent, edit=1)
        else:
            setString = splitLis[0]
            cls.setElementSetCreate(setString)
    @classmethod
    def setSetPathCreate(cls, setPath):
        compSetPathLis = cls.toCompSetPathLis(setPath)
        [cls.setCompSetPathCreate(i) for i in compSetPathLis]
    @classmethod
    def getNodeLisBySet(cls, setString, fullPath=True):
        def getBranch(setNode):
            if cls._isAppExist(setNode):
                stringLis = cmds.sets(setNode, query=1) or []
                if stringLis:
                    for node in stringLis:
                        if fullPath is True:
                            nodePath = cls._getNodeFullpathNameString(node)
                            if not nodePath in lis:
                                lis.append(nodePath)
                        else:
                            if not node in lis:
                                lis.append(node)
        #
        lis = []
        setLis = cls._toAppExistStringList(setString)
        if setLis:
            [getBranch(i) for i in setLis]
        return lis


#
class MaNodeAttributeMethodBasic(Mtd_AppMaya, _maConfig.MaNodeAttributeConfig):
    @staticmethod
    def _getAttributeQueryNameString(attrName):
        guessName = attrName.split('.')[-1]
        if guessName.endswith(']'):
            attrName = guessName.split('[')[0]
        else:
            attrName = guessName
        return attrName
    @classmethod
    def getAttrRgb(cls, attr):
        r, g, b = 0, 0, 0
        if cls._isAppExist(attr):
            stringLis = cmds.getAttr(attr)
            if stringLis:
                r, g, b = stringLis[0]
        return r, g, b
    @staticmethod
    def getAttrType(attr):
        attrType = cmds.getAttr(attr, type=1)
        return attrType
    @staticmethod
    def isAttrSource(attr):
        return cmds.connectionInfo(attr, isSource=1)
    @staticmethod
    def isAttrExactSource(attr):
        return cmds.connectionInfo(attr, isExactSource=1)
    @staticmethod
    def isAttrDestination(attr):
        return cmds.connectionInfo(attr, isDestination=1)
    @staticmethod
    def isAttrExactDestination(attr):
        return cmds.connectionInfo(attr, isExactDestination=1)
    @staticmethod
    def isAttrLocked(attr):
        return cmds.connectionInfo(attr, isLocked=1)
    @staticmethod
    def setAttrLocked(attr, boolean):
        cmds.setAttr(attr, lock=boolean)
    @staticmethod
    def isAttrSettable(attr):
        return cmds.getAttr(attr, settable=1)
    @staticmethod
    def isAttrKeyable(attr):
        return cmds.getAttr(attr, keyable=1)


#
class MaConnectionMethodBasic(Mtd_AppMaya):
    @staticmethod
    def getOutputNodeLisByAttr(attr):
        return cmds.listConnections(attr, destination=1, source=0) or []
    @staticmethod
    def getInputNodeLisByAttr(attr):
        return cmds.listConnections(attr, destination=0, source=1) or []
    @classmethod
    def getOutputAttrLisFilter(cls, attr, target=None):
        lis = []
        if cls._isAppExist(attr):
            stringLis = cmds.listConnections(attr, destination=1, source=0, plugs=1)
            if stringLis:
                if target is not None:
                    lis = [i for i in stringLis if cls._isStringMatch(i, target)]
                else:
                    lis = stringLis
        return lis
    @classmethod
    def getInputAttrLisFilter(cls, attr, source=None):
        lis = []
        if cls._isAppExist(attr):
            stringLis = cmds.listConnections(attr, destination=0, source=1, plugs=1)
            if stringLis:
                if source is not None:
                    lis = [i for i in stringLis if cls._isStringMatch(i, source)]
                else:
                    lis = stringLis
        return lis
    @classmethod
    def getNodeOutputConnectionLis(cls, nodepathString):
        lis = []
        if cls._isAppExist(nodepathString):
            data = cmds.listConnections(nodepathString, destination=1, source=0, connections=1, plugs=1)
            if data:
                for seq, i in enumerate(data):
                    if seq % 2:
                        sourceAttr = data[seq - 1]
                        targetAttr = i
                        #
                        lis.append((sourceAttr, targetAttr))
        return lis
    @classmethod
    def getOutputConnectionLisFilter(cls, nodepathString, source=None, target=None):
        lis = []
        if cls._isAppExist(nodepathString):
            data = cmds.listConnections(nodepathString, destination=1, source=0, connections=1, plugs=1)
            if data:
                for seq, i in enumerate(data):
                    if seq % 2:
                        sourceAttr = data[seq - 1]
                        targetAttr = i
                        #
                        if source is not None:
                            sourceEnable = cls._isStringMatch(sourceAttr, source)
                        else:
                            sourceEnable = True
                        #
                        if target is not None:
                            targetEnable = cls._isStringMatch(targetAttr, target)
                        else:
                            targetEnable = True
                        #
                        if sourceEnable and targetEnable:
                            lis.append((sourceAttr, targetAttr))
        return lis
    @staticmethod
    def getNodeInputConnectionLis(nodepathString):
        lis = []
        data = cmds.listConnections(nodepathString, destination=0, source=1, connections=1, plugs=1)
        if data:
            for seq, i in enumerate(data):
                if seq % 2:
                    sourceAttr = i
                    targetAttr = data[seq - 1]
                    #
                    lis.append((sourceAttr, targetAttr))
        return lis
    # noinspection PyUnusedLocal
    @classmethod
    def getOutputNodeLisFilter(cls, nodepathString, source=None, target=None):
        lis = []
        if cls._isAppExist(nodepathString):
            stringLis = cmds.listConnections(nodepathString, destination=1, source=0, connections=1, plugs=1)
            if stringLis:
                if target is not None:
                    targetAttrLis = [i for seq, i in enumerate(stringLis) if seq % 2 and cls._isStringMatch(i, target)]
                else:
                    targetAttrLis = [i for seq, i in enumerate(stringLis) if seq % 2]
                #
                if targetAttrLis:
                    for targetAttr in targetAttrLis:
                        node = targetAttr.split(cls.DEF_mya_port_separator)[0]
                        lis.append(node)
        return lis
    # noinspection PyUnusedLocal
    @classmethod
    def getInputNodeLisFilter(cls, nodepathString, source=None, target=None):
        lis = []
        #
        if cls._isAppExist(nodepathString):
            stringLis = cmds.listConnections(nodepathString, destination=0, source=1, connections=1, plugs=1)
            if stringLis:
                if source is not None:
                    sourceAttrLis = [i for seq, i in enumerate(stringLis) if seq % 2 and cls._isStringMatch(i, source)]
                else:
                    sourceAttrLis = [i for seq, i in enumerate(stringLis) if seq % 2]
                #
                if sourceAttrLis:
                    for sourceAttr in sourceAttrLis:
                        node = sourceAttr.split(cls.DEF_mya_port_separator)[0]
                        lis.append(node)
        return lis
    @classmethod
    def setAttrConnect(cls, sourceAttr, targetAttr):
        if cls._isAppExist(sourceAttr) and cls._isAppExist(targetAttr):
            if not cmds.isConnected(sourceAttr, targetAttr):
                cmds.connectAttr(sourceAttr, targetAttr, force=1)
                #
                bscMethods.PyMessage.traceResult('Connect {} > {}'.format(sourceAttr, targetAttr))
    @classmethod
    def setAttrDisconnect(cls, sourceAttr, targetAttr):
        if cls._isAppExist(sourceAttr) and cls._isAppExist(targetAttr):
            if cmds.isConnected(sourceAttr, targetAttr):
                cmds.disconnectAttr(sourceAttr, targetAttr)
                #
                bscMethods.PyMessage.traceResult('Disconnect {} > {}'.format(sourceAttr, targetAttr))


#
class MaNodeMethodBasic(MaNodeAttributeMethodBasic, MaConnectionMethodBasic, _maConfig.MaNodeConfig):
    @classmethod
    def getNodeAttrRgb(cls, nodepathString, attrName):
        if bscMethods.UniqueId.isUsable(nodepathString):
            nodepathString = cls.getNodeByUniqueId(nodepathString)
        return cls.getAttrRgb(cls._toNodeAttr([nodepathString, attrName]))
    @classmethod
    def getNodeAttrValue(cls, nodepathString, attrName):
        attr = cls._toNodeAttr([nodepathString, attrName])
        if cls._isAppExist(attr):
            return cmds.getAttr(attr)
    @classmethod
    def getNodeAttrBoolean(cls, nodepathString, attrName):
        return cls.getNodeAttrValue(nodepathString, attrName) or False
    @staticmethod
    def getObjectParentLis(nodepathString, fullPath=True):
        return cmds.listRelatives(nodepathString, parent=1, fullPath=fullPath) or []
    @classmethod
    def getObjectLisByUniqueId(cls, uniqueId, fullPath=True):
        uniqueIdLis = bscMethods.UniqueId.toList(uniqueId)
        lis = []
        if uniqueIdLis:
            for uniqueId in uniqueIdLis:
                objectPath = cls.getNodeByUniqueId(uniqueId, fullPath)
                if isinstance(objectPath, str) or isinstance(objectPath, unicode):
                    lis.append(objectPath)
                elif isinstance(objectPath, list):
                    [lis.append(i) for i in objectPath]
        return lis
    @staticmethod
    def _getNodeShapeNodeStringList(transform, fullPath=True):
        return cmds.listRelatives(transform, children=1, shapes=1, noIntermediate=0, fullPath=fullPath) or []
    @classmethod
    def _getNodeShapeNodeString(cls, nodepathString, fullPath=True):
        string = None
        if cls._getNodeCategoryString(nodepathString) == cls.DEF_mya_type_transform:
            stringLis = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=1, fullPath=fullPath)
            if stringLis:
                string = stringLis[0]
        else:
            if fullPath:
                string = cls._getNodeFullpathNameString(nodepathString)
            else:
                string = cls._nodeString2nodename_(nodepathString)
        return string
    @classmethod
    def getObjectShapeByUniqueId(cls, uniqueId, fullPath=True):
        objectPath = cls.getNodeByUniqueId(uniqueId)
        if objectPath:
            return cls._getNodeShapeNodeString(objectPath, fullPath)
    @classmethod
    def _getNodeShapeCategoryString(cls, nodepathString):
        string = cls._getNodeCategoryString(nodepathString)
        if string == cls.DEF_mya_type_transform:
            shapePath = cls._getNodeShapeNodeString(nodepathString)
            if shapePath:
                string = cls._getNodeCategoryString(shapePath)
        return string
    @classmethod
    def getObjectTypeByUniqueId(cls, uniqueId):
        objectPath = cls.getNodeByUniqueId(uniqueId)
        if objectPath:
            return cls._getNodeShapeCategoryString(objectPath)
    @staticmethod
    def getObjectParent(nodepathString, fullPath=True):
        stringLis = cmds.listRelatives(nodepathString, parent=1, fullPath=fullPath)
        if stringLis:
            return stringLis[0]
    @classmethod
    def setObjectParent(cls, nodepathString, parentString):
        if cls._isAppExist(parentString) and cls._isAppExist(nodepathString):
            origParentPath = cls.getObjectParent(nodepathString)
            if origParentPath:
                if not parentString in origParentPath:
                    cmds.parent(nodepathString, parentString)
            else:
                cmds.parent(nodepathString, parentString)
    @classmethod
    def setObjectParentByUniqueId(cls, uniqueId, parentString):
        def setBranch(objectPath):
            if objectPath:
                cls.setObjectParent(objectPath, parentString)
        #
        uniqueIdLis = bscMethods.UniqueId.toList(uniqueId)
        if uniqueIdLis:
            [setBranch(cls.getNodeByUniqueId(i)) for i in uniqueIdLis]
    @classmethod
    def getObjectTextureReference(cls, nodepathString):
        if cls._isAppExist(nodepathString):
            shapePath = cls._getNodeShapeNodeString(nodepathString)
            if shapePath is not None:
                attr = shapePath + '.referenceObject'
                if cls._isAppExist(attr):
                    stringLis = cls.getInputNodeLisByAttr(attr)
                    if stringLis:
                        return stringLis[0]
    @classmethod
    def getObjectTextureReferenceByUniqueId(cls, uniqueId):
        objectPath = cls.getNodeByUniqueId(uniqueId)
        if objectPath:
            return cls.getObjectTextureReference(objectPath)
    @classmethod
    def setObjectRename(cls, nodepathString, nameString, withShape=False):
        shapeUniqueId = None
        if withShape is True:
            shapePath = cls._getNodeShapeNodeString(nodepathString)
            shapeUniqueId = cls._getNodeUniqueIdString(shapePath)
        cls.setNodeRename(nodepathString, nameString)
        #
        if shapeUniqueId is not None:
            shapeName = nameString + 'Shape'
            cls.setNodeRenameByUniqueId(shapeUniqueId, shapeName)
    @classmethod
    def setObjectRenameByUniqueId(cls, uniqueId, nameString, withShape=False):
        if bscMethods.UniqueId.isUsable(uniqueId):
            nodepathString = cls.getNodeByUniqueId(uniqueId)
            cls.setObjectRename(nodepathString, nameString, withShape)
    @classmethod
    def setObjectShapeRename(cls, nodepathString, nameString=None):
        shapePath = cls._getNodeShapeNodeString(nodepathString)
        shapeName = cls._nodeString2nodename_(shapePath)
        if shapePath:
            if nameString is None:
                objectName = cls._nodeString2nodename_(nodepathString)
                nameString = objectName + 'Shape'
            if nameString != shapeName:
                if not cls.isNodeLocked(shapePath):
                    cmds.rename(shapePath, nameString)
    @classmethod
    def setObjectShapeRenameByUniqueId(cls, uniqueId, nameString=None):
        if bscMethods.UniqueId.isUsable(uniqueId):
            nodepathString = cls.getNodeByUniqueId(uniqueId)
            cls.setObjectShapeRename(nodepathString, nameString)
    @classmethod
    def setObjectTextureReferenceRenameByUniqueId(cls, uniqueId):
        objectPath = cls.getNodeByUniqueId(uniqueId)
        refObjectPath = cls.getObjectTextureReference(objectPath)
        if refObjectPath is not None:
            objectName = cls._nodeString2nodename_(objectPath)
            newRefObjectName = objectName + '_reference'
            newRefShapeName = newRefObjectName + 'Shape'
            refObjectUniqueId = cls._getNodeUniqueIdString(refObjectPath)
            cls.setObjectRenameByUniqueId(refObjectUniqueId, newRefObjectName)
            cls.setObjectShapeRenameByUniqueId(refObjectUniqueId, newRefShapeName)
    @classmethod
    def getObjectLisByType(cls, nodeTypeString, fullPath=True, exceptStrings=None):
        lis = []
        #
        filterTypeLis = bscMethods.String.toList(nodeTypeString, cmds.allNodeTypes())
        shapeLis = cmds.ls(type=filterTypeLis, long=fullPath) or []
        if shapeLis:
            lis = [cls._getNodeTransformNodeString(i) for i in shapeLis]
        #
        if exceptStrings is not None:
            if lis:
                [lis.remove(i) for i in exceptStrings if i in lis]
        return lis
    @classmethod
    def getObjectLisByGroup(cls, groupString, nodeTypeString=None):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        def branchFn(nodepathString):
            stringLis = cmds.listRelatives(nodepathString, children=1, fullPath=1)
            if stringLis:
                for node in stringLis:
                    if filterTypeLis:
                        nodeType = cls._getNodeCategoryString(node)
                        if nodeType in filterTypeLis:
                            addFn(cls._getNodeTransformNodeString(node))
                    else:
                        addFn(cls._getNodeTransformNodeString(node))
                    #
                    branchFn(node)
        #
        lis = []
        #
        groupLis = cls._toAppExistStringList(groupString)
        filterTypeLis = bscMethods.String.toList(nodeTypeString)
        if groupLis:
            [branchFn(i) for i in groupLis]
        return lis
    @classmethod
    def getNodeChildLis(cls, nodepathString, fullPath=True):
        lis = []
        if cls._isAppExist(nodepathString):
            lis = cmds.listRelatives(nodepathString, children=1, fullPath=fullPath) or []
        return lis
    @classmethod
    def getNodeTransformLisByGroup(cls, groupString, nodeTypeString, fullPath=True):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        def branchFn(nodepathString):
            stringLis = cmds.listRelatives(nodepathString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullPath)
            if stringLis:
                for node in stringLis:
                    shapePath = cmds.listRelatives(node, children=1, shapes=1, noIntermediate=1, fullPath=1)
                    if shapePath:
                        if filterTypeLis:
                            shapeType = cls._getNodeCategoryString(shapePath)
                            if shapeType in filterTypeLis:
                                addFn(node)
                        else:
                            addFn(node)
                    #
                    branchFn(node)
        #
        lis = []
        #
        groupLis = cls._toAppExistStringList(groupString)
        filterTypeLis = bscMethods.String.toList(nodeTypeString)
        if groupLis:
            [branchFn(i) for i in groupLis]
        return lis
    @classmethod
    def getChildTransformLisByGroup(cls, groupString, fullPath=True):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        def branchFn(nodepathString):
            stringLis = cmds.listRelatives(nodepathString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullPath)
            if stringLis:
                for node in stringLis:
                    shapePathLis = cmds.listRelatives(node, children=1, shapes=1, noIntermediate=0, fullPath=1)
                    if shapePathLis:
                        addFn(node)
                    #
                    branchFn(node)
        #
        lis = []
        groupLis = cls._toAppExistStringList(groupString)
        if groupLis:
            [branchFn(i) for i in groupLis]
        return lis
    @classmethod
    def getNodeLisByGroup(cls, groupString, nodeTypeString, fullPath=True):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        def branchFn(nodepathString):
            stringLis = cmds.listRelatives(nodepathString, children=1, fullPath=fullPath)
            if stringLis:
                for node in stringLis:
                    if filterTypeLis:
                        nodeType = cls._getNodeCategoryString(node)
                        if nodeType in filterTypeLis:
                            addFn(node)
                    else:
                        addFn(node)
                    #
                    branchFn(node)
        #
        lis = []
        #
        groupLis = cls._toAppExistStringList(groupString)
        filterTypeLis = bscMethods.String.toList(nodeTypeString)
        if groupLis:
            [branchFn(i) for i in groupLis]
        return lis
    @classmethod
    def getChildShapeLisByGroup(cls, groupString, fullPath=True):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        def branchFn(nodepathString):
            stringLis = cmds.listRelatives(nodepathString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullPath)
            if stringLis:
                for node in stringLis:
                    shapePath = cls._getNodeShapeNodeString(node)
                    if shapePath:
                        addFn(shapePath)
                    #
                    branchFn(node)
        #
        lis = []
        groupLis = cls._toAppExistStringList(groupString)
        if groupLis:
            [branchFn(i) for i in groupLis]
        return lis
    @classmethod
    def getChildGroupLisByGroup(cls, groupString, fullPath=True):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        def branchFn(nodepathString):
            stringLis = cmds.listRelatives(nodepathString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullPath)
            if stringLis:
                for node in stringLis:
                    if cls._getNodeIsGroup(node):
                        addFn(node)
                    branchFn(node)

        lis = []
        groupLis = cls._toAppExistStringList(groupString)
        if groupLis:
            [branchFn(i) for i in groupLis]
        return lis
    # Selection Filter
    @classmethod
    def filterSelectedGroupLis(cls):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        lis = []
        #
        stringLis = cmds.ls(type=cls.DEF_mya_type_transform, selection=1, dagObjects=1, long=1) or []
        for i in stringLis:
            shapePathLis = cmds.listRelatives(i, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if shapePathLis is None:
                addFn(i)
        #
        return lis
    @classmethod
    def filterSelectedTransformLis(cls):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        lis = []
        #
        stringLis = cmds.ls(type=cls.DEF_mya_type_transform, selection=1, dagObjects=1, long=1) or []
        for i in stringLis:
            shapePathLis = cmds.listRelatives(i, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if shapePathLis is not None:
                addFn(i)
        #
        return lis
    @classmethod
    def filterSelectedNodeTransformLis(cls, nodeTypeString=None):
        def addFn(node):
            if not node in lis:
                lis.append(node)
        #
        lis = []
        #
        filterTypeLis = bscMethods.String.toList(nodeTypeString)
        stringLis = cmds.ls(type=cls.DEF_mya_type_transform, selection=1, dagObjects=1, long=1) or []
        for i in stringLis:
            shapePath = cls._getNodeShapeNodeString(i)
            if shapePath:
                if filterTypeLis:
                    shapeType = cls._getNodeCategoryString(shapePath)
                    if shapeType in filterTypeLis:
                        addFn(i)
                else:
                    addFn(i)
        #
        return lis
    @classmethod
    def _getNodeIsGroup(cls, nodepathString):
        boolean = False
        # Nde_Node Type is "Transform" and has Non "Shape(s)"
        if cmds.nodeType(nodepathString) == cls.DEF_mya_type_transform:
            shapePathLis = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if shapePathLis is None:
                boolean = True
        return boolean
    @classmethod
    def _getNodeIsTransform(cls, nodepathString):
        boolean = False
        # Nde_Node Type is "Transform" and has "Shape(s)"
        if cmds.nodeType(nodepathString) == cls.DEF_mya_type_transform:
            shapePathLis = cmds.listRelatives(nodepathString, children=1, shapes=1, noIntermediate=0, fullPath=1)
            if shapePathLis is not None:
                boolean = True
        return boolean
    @classmethod
    def _getNodeIsShape(cls, nodepathString):
        boolean = False
        if cmds.nodeType(nodepathString) != cls.DEF_mya_type_transform:
            transformPath = cls._getNodeTransformNodeString(nodepathString)
            shapePathLis = cls._getNodeShapeNodeStringList(nodepathString)
            if transformPath and not shapePathLis:
                boolean = True
        return boolean
    @classmethod
    def isGroupEmpty(cls, groupString):
        boolean = False
        if cmds.nodeType(groupString) == cls.DEF_mya_type_transform:
            childNodeLis = cmds.listRelatives(groupString, children=1, fullPath=1)
            if not childNodeLis:
                boolean = True
        return boolean
    @classmethod
    def getObjectChildObjectLis(cls, nodepathString, fullPath=True):
        return cmds.listRelatives(nodepathString, children=1, type=cls.DEF_mya_type_transform, fullPath=fullPath) or []
    @classmethod
    def getGroupLisByRoot(cls, groupString, fullPath=True):
        def getChild(parent):
            childNodeLis = cls.getNodeChildLis(parent, fullPath)
            if childNodeLis:
                for childNode in childNodeLis:
                    if cls._getNodeIsGroup(childNode):
                        lis.append(childNode)
                    getChild(childNode)

        useRoot = groupString
        if fullPath:
            useRoot = cls._getNodeFullpathNameString(groupString)
        lis = [useRoot]
        if cls._isAppExist(groupString):
            getChild(groupString)
        return lis
    @classmethod
    def setEmptyGroupClear(cls, groupString):
        if cls._isAppExist(groupString):
            childGroupLis = cls.getGroupLisByRoot(groupString)
            childGroupLis.reverse()
            for childGroup in childGroupLis:
                childNodeLis = cls.getNodeChildLis(childGroup)
                if not childNodeLis:
                    cls.setNodeDelete(childGroup)
    @classmethod
    def setNodeDelete(cls, nodepathString):
        if cls._isAppExist(nodepathString):
            cmds.delete(nodepathString)
    @classmethod
    def setNodesDelete(cls, nodepathString):
        nodeLis = cls._toAppExistStringList(nodepathString)
        [cls.setNodeDelete(i) for i in nodeLis]
    @classmethod
    def getAttrDefaultValueLis(cls, nodepathString, attrName, attrType):
        lis = []
        if not attrType in cls.MaAttrTypeLis_NonDefaultValue:
            attrQueryName = cls._getAttributeQueryNameString(attrName)
            lis = cmds.attributeQuery(attrQueryName, node=nodepathString, listDefault=1) or []
        return lis
    @classmethod
    def getNodeAttrDatum(cls, nodepathString, attrName):
        tup = ()
        if not attrName in cls.MaAttrNameLis_ShaderExcept:
            attr = cls._toNodeAttr([nodepathString, attrName])
            # Filter Exists
            if cmds.objExists(attr):
                attrType = cls.getAttrType(attr)
                if attrType in cls.MaAttrTypeLis_Readable:
                    # Debug ( Filter Connected is Unused with Mult Attribute )
                    if not cls.isAttrExactDestination(attr):
                        value = cmds.getAttr(attr)
                        if value is not None:
                            # Value
                            if value is True:
                                value = 1
                            elif value is False:
                                value = 0
                            # Lock
                            lockAttribute = cls.isAttrLocked(attr)
                            if lockAttribute is True:
                                lockAttribute = 1
                            elif lockAttribute is False:
                                lockAttribute = 0
                            # Compound Attribute
                            if attrName.endswith('_Position') or attrName.endswith('_FloatValue') or attrName.endswith('_Interp'):
                                tup = attrName, value, attrType, lockAttribute
                            else:
                                defaultValueLis = cls.getAttrDefaultValueLis(nodepathString, attrName, attrType)
                                if not value in defaultValueLis:
                                    tup = attrName, value, attrType, lockAttribute
        return tup
    @classmethod
    def getNodeAttrDatumLis(cls, nodepathString, attrNames):
        lis = []
        #
        if attrNames:
            for attrName in attrNames:
                attrData = cls.getNodeAttrDatum(nodepathString, attrName)
                if attrData:
                    lis.append(attrData)
        return lis
    @staticmethod
    def getNodeDefAttrNameLis(nodepathString):
        return cmds.listAttr(nodepathString, read=1, write=1, inUse=1, multi=1) or []
    @classmethod
    def getNodeDefAttrDatumLis(cls, nodepathString):
        attrNameLis = cls.getNodeDefAttrNameLis(nodepathString)
        return cls.getNodeAttrDatumLis(nodepathString, attrNameLis)
    @classmethod
    def setAttrStringDatum(cls, nodepathString, attrName, attrType, data, lockAttribute):
        if attrName in cls.MaAttrNameDic_Convert:
            attrName = cls.MaAttrNameDic_Convert[attrName]
        #
        attr = nodepathString + '.' + attrName
        if cls._isAppExist(attr):
            if not cls.isAttrDestination(attr):
                # Filter String
                isString = attrType == 'string'
                isMatrix = attrType == 'matrix'
                #
                if cls.isAttrLocked(attr):
                    cmds.setAttr(attr, lock=0)
                #
                if isString:
                    if data is not None:
                        cmds.setAttr(attr, data, type='string')
                elif isMatrix:
                    cmds.setAttr(attr, data, type='matrix')
                else:
                    # Debug ( Clamp Maximum or Minimum Value )
                    cmds.setAttr(attr, data, clamp=1)
                # Lock Attr
                cmds.setAttr(attr, lock=lockAttribute)
    @classmethod
    def setNodeCompoundAttrClear(cls, nodepathString):
        attrNameLis = cls.getNodeDefAttrNameLis(nodepathString)
        if attrNameLis:
            for attrName in attrNameLis:
                if attrName.endswith('_Position'):
                    mainAttrName = attrName.split('.')[0]
                    attr = nodepathString + '.' + mainAttrName
                    if cls._isAppExist(attr):
                        cmds.removeMultiInstance(attr)
    @classmethod
    def setNodeDefAttrByData(cls, nodepathString, attrData):
        colorAttrDic = {}
        # Debug Must Clear Compound Attribute First !!!
        cls.setNodeCompoundAttrClear(nodepathString)
        #
        for attrDatum in attrData:
            if attrDatum:
                attrName, value, attrType, isLocked = attrDatum
                if not attrName in cls.MaAttrNameLis_ShaderExcept:
                    cls.setAttrStringDatum(nodepathString, attrName, attrType, value, isLocked)
                # Debug Color Attribute
                if attrName.endswith('R') or attrName.endswith('G') or attrName.endswith('B'):
                    mainAttr = attrName[:-1]
                    colorAttrDic.setdefault(mainAttr, []).append(value)
        #
        if colorAttrDic:
            for k, v in colorAttrDic.items():
                if len(v) == 3:
                    cls.setNodeColorAttr(nodepathString, k, *v)
    @classmethod
    def setNodeOverrideRgb(cls, nodepathString, r, g, b, boolean=True):
        cmds.setAttr(cls._toNodeAttr([nodepathString, 'overrideRGBColors']), 1)
        cmds.setAttr(cls._toNodeAttr([nodepathString, 'overrideColorRGB']), r, g, b)
        cmds.setAttr(cls._toNodeAttr([nodepathString, 'overrideEnabled']), boolean)
    @classmethod
    def setNodeOverrideRgbByUniqueId(cls, uniqueId, r, g, b, boolean=True):
        objectPath = cls.getNodeByUniqueId(uniqueId)
        if objectPath:
            cls.setNodeOverrideRgb(objectPath, r, g, b, boolean)
    @classmethod
    def isNodeOutlinerColorEnable(cls, nodepathString):
        if bscMethods.UniqueId.isUsable(nodepathString):
            nodepathString = cls.getNodeByUniqueId(nodepathString)
        return cmds.getAttr(cls._toNodeAttr([nodepathString, 'useOutlinerColor'])) or False
    @classmethod
    def getNodeOutlinerRgb(cls, nodepathString):
        return cls.getNodeAttrRgb(nodepathString, 'outlinerColor')
    @classmethod
    def setNodeOutlinerRgb(cls, nodepathString, r, g, b, boolean=True):
        cmds.setAttr(cls._toNodeAttr([nodepathString, 'outlinerColor']), r, g, b)
        cmds.setAttr(cls._toNodeAttr([nodepathString, 'useOutlinerColor']), boolean)
    @classmethod
    def setNodeOutlinerColorEnable(cls, nodepathString, boolean):
        cls.setNodeAttr(nodepathString, 'useOutlinerColor', boolean)
    @classmethod
    def setNodeOutlinerRgbByUniqueId(cls, uniqueId, r, g, b, boolean=True):
        objectPath = cls.getNodeByUniqueId(uniqueId)
        if objectPath:
            cls.setNodeOutlinerRgb(objectPath, r, g, b, boolean)
    @classmethod
    def lynxi_setNodeAttr(cls, nodepathString):
        cls.setAttrStringDatumForce_(nodepathString, cls.LynxiAttrName_Artist, bscMethods.OsSystem.username())
        cls.setAttrStringDatumForce_(nodepathString, cls.LynxiAttrName_Update, bscMethods.OsSystem.activeTimestamp())
        cls.setAttrStringDatumForce_(nodepathString, cls.LynxiAttrName_NodeId, cls._getNodeUniqueIdString(nodepathString))
    @classmethod
    def lynxi_isNodeColorEnable(cls, nodepathString):
        boolean = True
        #
        attrName = cls.LynxiAttrName_NodeColorEnable
        attr = cls._toNodeAttr([nodepathString, attrName])
        if cls._isAppExist(attr):
            boolean = cls.getNodeAttrValue(nodepathString, attrName)
        else:
            cls.setAttrBooleanDatumForce_(nodepathString, attrName, boolean)
        return boolean
    @classmethod
    def lynxi_getNodeColor(cls, nodepathString):
        r, g, b = bscMethods.String.toRgb(cls._nodeString2nodename_(nodepathString), maximum=1.0)
        #
        attrName = cls.LynxiAttrName_NodeColor
        attr = cls._toNodeAttr([nodepathString, attrName])
        if cls._isAppExist(attr):
            r, g, b = cls.getAttrRgb(attr)
        else:
            cls.setNodeRgbAttrForce(nodepathString, attrName, r, g, b)
        return r, g, b
    @classmethod
    def getAssemblyReferenceNode(cls, nodepathString):
        node = None
        if cls._getNodeCategoryString(nodepathString) == cls.DEF_mya_type_assembly_reference:
            node = nodepathString
        else:
            parentNode = cls.getObjectParent(nodepathString)
            if cls._getNodeCategoryString(parentNode) == cls.DEF_mya_type_assembly_reference:
                node = parentNode
        return node
    # noinspection PyUnusedLocal
    @classmethod
    def lxHideShow(cls, operation, extend=False):
        if operation == 'hide':
            boolean = False
        else:
            boolean = True
        #
        stringLis = cmds.ls(selection=1, long=1)
        if stringLis:
            for node in stringLis:
                assemblyReferenceNode = cls.getAssemblyReferenceNode(node)
                if assemblyReferenceNode is not None:
                    cmds.addAttr(assemblyReferenceNode, longName=cls.LynxiKeyword_Node_Visible, attributeType='bool', keyable=1)
                    cls.setNodeAttr(assemblyReferenceNode, cls.MaAttrName_Visible, boolean)
                else:
                    cmds.addAttr(node, longName=cls.LynxiKeyword_Node_Visible, attributeType='bool', keyable=1)
                    cls.setNodeAttr(node, cls.MaAttrName_Visible, boolean)
            #
            if operation is 'hide':
                cls.setMessageWindowShow('Selected Nde_Node(s) is', 'Hide !!!')
            else:
                cls.setMessageWindowShow('Selected Nde_Node(s) is', 'Show !!!')
    @classmethod
    def isObjectShapeInstanced(cls, nodepathString):
        boolean = False
        shapePath = cls._getNodeShapeNodeString(nodepathString)
        if shapePath:
            stringLis = cmds.listRelatives(shapePath, allParents=1, fullPath=1) or []
            if len(stringLis) > 1:
                boolean = True
        return boolean
    @classmethod
    def setObjectInstanceCovert(cls, nodepathString):
        if cls.isObjectShapeInstanced(nodepathString):
            stringLis = cmds.duplicate(nodepathString)
            cmds.delete(nodepathString)
            cmds.rename(stringLis[0], cls._nodeString2nodename_(nodepathString))


#
class M2NodeMethodBasic(Mtd_M2Basic):
    pass


#
class M2GeometryNodeMethodBasic(MaNodeMethodBasic, Mtd_M2Basic):
    @classmethod
    def getMeshNormalLockVertexLis(cls, nodepathString):
        lis = []
        if cls._isAppExist(nodepathString):
            lis = []
            m2MeshObject = cls.toM2MeshNode(nodepathString)
            for vertexId in [i for i in xrange(m2MeshObject.numVertices)]:
                if m2MeshObject.isNormalLocked(vertexId):
                    lis.append(vertexId)
        #
        return lis
    @classmethod
    def toM2MeshNode(cls, string, mode=0):
        if mode == 0:
            return Om2.MFnMesh(cls.toM2NodePath(string))
        elif mode == 1:
            return Om2.MFnMesh(string)
    @classmethod
    def toM2SurfaceNode(cls, string, mode=0):
        if mode == 0:
            return Om2.MFnNurbsSurface(cls.toM2NodePath(string))
        elif mode == 1:
            return Om2.MFnNurbsSurface(string)
    @classmethod
    def toM2CurveNode(cls, string, mode=0):
        if mode == 0:
            return Om2.MFnNurbsCurve(cls.toM2NodePath(string))
        elif mode == 1:
            return Om2.MFnNurbsCurve(string)
    @classmethod
    def getMeshOpenEdgeIdLis(cls, string, roundCount=8):
        lis = []
        #
        borderEdgeIdLis = []
        edgeCoincideDic = {}
        m2MeshEdge = Om2.MItMeshEdge(cls.toM2NodePath(string))
        edgeIdLis = range(m2MeshEdge.count())
        for edgeId in edgeIdLis:
            m2MeshEdge.setIndex(edgeId)
            if m2MeshEdge.onBoundary() is True:
                borderEdgeIdLis.append(edgeId)
                #
                pointKeyLis = []
                for i in range(2):
                    point = m2MeshEdge.point(i)
                    x, y, z = round(point.x, roundCount), round(point.y, roundCount), round(point.z, roundCount)
                    pointKeyLis.append((x, y, z))
                #
                pointKeyLis.sort()
                #
                edgeCoincideDic.setdefault(tuple(pointKeyLis), []).append(edgeId)
        #
        for k, v in edgeCoincideDic.items():
            if len(v) > 1:
                for i in v:
                    lis.append(i)
        #
        for i in borderEdgeIdLis:
            if i not in lis:
                pass
        #
        return lis


#
class M2CameraMethodBasic(Mtd_M2Basic):
    @classmethod
    def toM2Camera(cls, nodepathString):
        return Om2.MFnCamera(cls.toM2NodePath(nodepathString))


#
class MaNodeGraphMethodBasic(MaNodeMethodBasic, _maConfig.MaNodeGraphConfig):
    @classmethod
    def setCompAppPathCreate(cls, compNodePath, lockTransformation=False, hideTransformation=False):
        objectName = cls._nodeString2nodename_(compNodePath)
        parentPath = cls._toNodeParentPath(compNodePath)
        if not cls._isAppExist(compNodePath):
            if parentPath:
                groupString = cmds.group(empty=1, name=objectName, parent=parentPath)
            else:
                groupString = cmds.group(empty=1, name=objectName)
            #
            cls.lynxi_setNodeAttr(groupString)
        #
        cls.setObjectTransformationAttr(compNodePath, lockTransformation, hideTransformation)
    @classmethod
    def setAppPathCreate(cls, nodePath, lockTransformation=False, hideTransformation=False):
        compPathLis = cls._toAppCompPathLis(nodePath)
        for compPath in compPathLis:
            cls.setCompAppPathCreate(compPath, lockTransformation, hideTransformation)
    @classmethod
    def getInputShapeLis(cls, nodepathString, filterType=None):
        lis = []
        if filterType is not None:
            inputConnectionLis = cmds.listConnections(nodepathString, destination=0, source=1, shapes=1, type=filterType)
        else:
            inputConnectionLis = cmds.listConnections(nodepathString, destination=0, source=1, shapes=1)
        if inputConnectionLis:
            for i in inputConnectionLis:
                if cls._getNodeIsTransform(i) or cls._getNodeIsShape(i):
                    lis.append(cls._getNodeFullpathNameString(i))
                else:
                    lis.append(i)
        return lis
    @classmethod
    def getObjectGraphData(cls, nodepathString):
        def branchFn(string):
            if not string in nodeLis:
                if cls._getNodeIsTransform(string):
                    shapeLis = cls._getNodeShapeNodeStringList(string)
                    usedLis = [string] + shapeLis
                    #
                    if not string in objectLis:
                        objectLis.append(string)
                else:
                    if cls._getNodeIsShape(string):
                        usedLis = [string]
                    else:
                        usedLis = [string]
                #
                if usedLis:
                    for i in usedLis:
                        if i not in nodeLis:
                            nodeLis.append(i)
                        #
                        inputStringLis = cmds.listConnections(i, destination=0, source=1, shapes=1) or []
                        for j in inputStringLis:
                            pathString = cls._getNodeFullpathNameString(j)
                            if not pathString in nodeLis:
                                branchFn(pathString)
                            if not pathString in nodeLis:
                                nodeLis.append(pathString)
        #
        objectLis = []
        nodeLis = []
        #
        branchFn(cls._getNodeFullpathNameString(nodepathString))
        return objectLis, nodeLis
    @classmethod
    def getObjectGraphLisForRename(cls, nodepathString):
        pass
    @classmethod
    def getObjectGraphLisForCollection(cls, nodepathString):
        pass


#
class Mtd_MaPlug(Mtd_AppMaya, _maConfig.MaPlugConfig):
    @staticmethod
    def getPlugLis():
        return cmds.pluginInfo(query=1, listPlugins=1)
    @staticmethod
    def isPlugLoaded(plugName):
        return cmds.pluginInfo(plugName, query=1, loaded=1)
    @staticmethod
    def loadAppPlug(plugName):
        cmds.loadPlugin(plugName, quiet=1)


#
class MaHotkeyMethodBasic(Mtd_AppMaya):
    @classmethod
    def setHotkeySet(cls, hotkeySetName):
        if not cmds.hotkeySet(hotkeySetName, query=True, exists=True):
            cmds.hotkeySet(hotkeySetName, current=True, source="Maya_Default")
    @classmethod
    def addCommand(cls, key, name, annotation, pythonCommand, ctrlModifier=False, shiftModifier=False, altModifier=False):
        cmds.nameCommand(
            name,
            annotation=annotation,
            command='python("{}")'.format(pythonCommand)
        )
        cmds.hotkey(
            name=name,
            k=key,
            ctrlModifier=ctrlModifier, shiftModifier=shiftModifier, altModifier=altModifier
        )
        bscMethods.PyMessage.traceResult('Add Hotkey "{}"'.format(annotation))
