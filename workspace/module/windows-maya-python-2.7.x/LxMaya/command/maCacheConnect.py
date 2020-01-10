# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxBasic import bscMethods, bscObjects
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr
#
from LxMaya.command import maUtils, maGeom
#
MaAlembicCacheShapeLabel = '_inCache'
#
MaBlendNodeLabel = '_inShape'
MaKeyword_ShapeOrig = 'Orig'
MaKeyword_ShapeDeformed = 'Deformed'


#
class LxAstModelCacheConnectMethod(object):
    def __init__(self, assetName, cacheNamespace, assetNamespace):
        self._connectionLis = []
        self._errorObjectLis = []
        #
        self._nodeLis = []
        #
        self._assetName = assetName
        #
        self._cacheNamespace = cacheNamespace
        self._assetNamespace = assetNamespace
        #
        self._rootGroupName = assetPr.astUnitModelLinkGroupName(self._assetName)
        #
        self._containerName = assetPr.astModelContainerName(self._assetName)
        self._scContainerName = assetPr.astModelContainerName(self._assetName, self._assetNamespace)
        #
        self._cacheGroupName = maUtils._toNamespace([self._cacheNamespace, self._rootGroupName])
        self._assetGroupName = maUtils._toNamespace([self._assetNamespace, self._rootGroupName])
    @staticmethod
    def _toCacheShapeName(nodeName, targetNamespace):
        return targetNamespace + ':' + nodeName + MaAlembicCacheShapeLabel
    @staticmethod
    def _toBlendShapeNodeName(nodeName):
        return nodeName + MaBlendNodeLabel
    @staticmethod
    def _toTargetLocalPath(objectPath, sourceNamespace, targetNamespace):
        return objectPath.replace(sourceNamespace + ':', targetNamespace + ':')[1:]
    #
    def _setShapeBlendCmd(self, sourceObjectPath, targetObjectPath, visibility):
        sourceShapePath = maUtils.getNodeShape(sourceObjectPath)
        sourceShapeName = maUtils._toNodeName(sourceShapePath)
        #
        targetObjectName = maUtils._toNodeName(targetObjectPath)
        #
        targetShapePath = maUtils.getNodeShape(targetObjectPath)
        targetShapeName = maUtils._toNodeName(targetShapePath, useMode=1)
        # Parent Source Shape
        maUtils.setShapeParent(sourceShapePath, targetObjectPath)
        #
        newSourceShapePath = targetObjectPath + '|' + sourceShapeName
        self._nodeLis.append(newSourceShapePath)
        # Debug Source Shape Hide
        cmds.setAttr(targetShapePath + '.visibility', 1)
        #
        blendShapeNode = self._toBlendShapeNodeName(targetObjectName)
        # Create
        if not maUtils.isAppExist(blendShapeNode):
            origShapePath = targetObjectPath + '|' + targetShapeName + appCfg.MaKeyword_ShapeOrig
            if maUtils.isAppExist(origShapePath):
                maUtils.setNodeDelete(origShapePath)
            # Must Use "before" Arg
            # cmds.blendShape(newSourceShapePath, targetShapePath, name=blendShapeNode, weight=(0, 1), before=1)
            cmds.blendShape(newSourceShapePath, targetShapePath, name=blendShapeNode, weight=(0, 1), origin='world', before=1)
            #
            self._nodeLis.append(blendShapeNode)
            self._nodeLis.append(origShapePath)
        # Reconnect
        else:
            sourceAttrName = 'worldMesh[0]'
            targetAttrName = 'inputTarget[0].inputTargetGroup[0].inputTargetItem[6000].inputGeomTarget'
            sourceAttr = newSourceShapePath + '.' + sourceAttrName
            targetAttr = blendShapeNode + '.' + targetAttrName
            maUtils.setAttrConnect(sourceAttr, targetAttr)
            #
            self._connectionLis.append((sourceAttr, targetAttr))
        # Hied Shape
        cmds.setAttr(newSourceShapePath + '.intermediateObject', 1)
        if visibility == 1:
            cmds.setAttr(targetShapePath + '.visibility', cmds.getAttr(newSourceShapePath + '.visibility'))
    @classmethod
    def _setBlendResultClear(cls, targetObjectPath):
        shapePath = maUtils.getNodeShape(targetObjectPath)
        nodeLis = maUtils.getInputNodes(shapePath, 'tweak')
        maUtils.setNodesClear(nodeLis)
    @classmethod
    def _setContainerAddNodes(cls, container, nodes):
        existsNodeLis = [i for i in nodes if maUtils.isAppExist(i)]
        cmds.container(container, edit=1, force=1, addNode=existsNodeLis)
    #
    def _setShapeConnectCmd(self, sourceObjectPath, targetObjectPath, visibility):
        self._setShapeBlendCmd(sourceObjectPath, targetObjectPath, visibility)
        self._setBlendResultClear(targetObjectPath)
    @classmethod
    def _setTransformConnectCmd(cls, sourceObjectPath, targetObjectPath):
        maUtils.setObjectClearInputTransformationConnection(targetObjectPath)
        maUtils.setObjectClearInputVisibleConnection(targetObjectPath)
        #
        maUtils.setObjectTransferTransformation(sourceObjectPath, targetObjectPath)
        maUtils.setObjectTransferVisibility(sourceObjectPath, targetObjectPath)
        #
        maUtils.setObjectTransferInputConnections(sourceObjectPath, targetObjectPath)
    #
    def _setContainerRefresh(self):
        if not maUtils.isAppExist(self._scContainerName):
            if not maUtils.isAppExist(self._scContainerName):
                maUtils.setCreateContainer(self._scContainerName)
            #
            maUtils.setContainerNamespace(self._containerName, self._assetNamespace)
    #
    def _setSourceShapesRename(self):
        stringLis = self._cacheObjectLis
        if stringLis:
            maxValue = len(stringLis)
            progressBar = bscObjects.If_Progress('Rename Cache Shape(s)', maxValue)
            for objectPath in stringLis:
                progressBar.update()
                #
                objectName = maUtils._toNodeName(objectPath, useMode=1)
                #
                newSourceShapeName = self._toCacheShapeName(objectName, self._assetNamespace)
                if maUtils.isAppExist(newSourceShapeName):
                    maUtils.setNodeDelete(newSourceShapeName)
                #
                shapePath = maUtils.getNodeShape(objectPath)
                shapeName = maUtils._toNodeName(shapePath, useMode=1)
                # Clean Nde_ShaderRef
                if shapeName != newSourceShapeName:
                    maUtils.setNodeRename(shapePath, newSourceShapeName)
    #
    def _setAlembicTransformConnect(self):
        nodeLis = self._cacheGroupLis + self._cacheObjectLis
        if nodeLis:
            maxValue = len(nodeLis)
            progressBar = bscObjects.If_Progress('Connect Transform(s)', maxValue)
            for sourcePath in nodeLis:
                progressBar.update()
                #
                targetPath = self._toTargetLocalPath(sourcePath, self._cacheNamespace, self._assetNamespace)
                if maUtils.isAppExist(targetPath):
                    self._setTransformConnectCmd(sourcePath, targetPath)
    #
    def _setAlembicShapeConnect(self):
        objectLis = self._cacheObjectLis
        if objectLis:
            maxValue = len(objectLis)
            progressBar = bscObjects.If_Progress('Connect Shape(s)', maxValue)
            #
            for sourcePath in objectLis:
                progressBar.update()
                #
                targetPath = self._toTargetLocalPath(sourcePath, self._cacheNamespace, self._assetNamespace)
                if maUtils.isAppExist(targetPath):
                    if maGeom.isMeshGeomTopoMatch(sourcePath, targetPath) is True:
                        self._setShapeConnectCmd(
                            sourcePath, targetPath,
                            self._withVisible
                        )
                        maUtils.setNodeOutlinerRgb(targetPath, 0, 1, 0)
                    else:
                        self._errorObjectLis.append(targetPath)
                        maUtils.setNodeOutlinerRgb(targetPath, 1, 0, 0)
    #
    def create(self, cacheFile, assetFile, cacheNamespace, assetNamespace):
        pass
    #
    def connect(self):
        self._withVisible = True
        #
        self._cacheGroupLis = maUtils.getGroupLisByRoot(self._cacheGroupName)
        self._cacheObjectLis = maUtils.getChildObjectsByRoot(self._cacheGroupName, filterTypes=appCfg.MaNodeType_Mesh)
        #
        self._setContainerRefresh()
        #
        if maUtils.isAppExist(self._cacheGroupName) and maUtils.isAppExist(self._assetGroupName):
            self._setSourceShapesRename()
            #
            self._setAlembicTransformConnect()
            self._setAlembicShapeConnect()
            #
            maUtils.setNodeDelete(self._cacheGroupName)
        #
        self._setContainerAddNodes(self._scContainerName, self._nodeLis)
    #
    def setSourceClear(self):
        alembicNodeLis = maUtils.getDependNodesByNamespace(self._cacheNamespace)
        if alembicNodeLis:
            for alembicNode in alembicNodeLis:
                shapeLis = maUtils.getOutputShapes(alembicNode, appCfg.MaNodeType_Mesh)
                if shapeLis:
                    maUtils.setNodesClear(shapeLis)
            #
            maUtils.setNodesClear(alembicNodeLis)
    @property
    def connectionLis(self):
        return self._connectionLis
    @property
    def errorObjectLis(self):
        return self._errorObjectLis
