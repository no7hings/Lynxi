# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore import lxBasic, lxProgress
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import sceneryPr
#
from LxMaya.command import maUtils, maGeom
# Type Config
typeSet = appVariant.astBasicClassifications
typeLabel = appVariant.assetClassifyAbbDic
typeDic = appVariant.assetClassifyFullDic
# File Label
scnSceneryLocatorLabel = appVariant.scnSceneryLocatorLabel
sceneryLabel = appVariant.localSceneryRoot
scnSceneryDefinitionLabel = appVariant.scnSceneryDefinitionLabel
# Utilities Label
adFileAttrLabel = appVariant.adFileAttrLabel
asbLodLevelAttrLabel = appVariant.asbLodLevelAttrLabel
#
none = ''


#
def setAssemblySceneDefinitionCreate(nodeName, osFile):
    cmds.assembly(name=nodeName, type='assemblyDefinition')
    cmds.assembly(nodeName, edit=1, createRepresentation='Scene', input=osFile)
    cmds.assembly(nodeName, edit=1, active=lxBasic.getOsFileBasename(osFile))


#
def setAssemblyAnnotation(assemblyReferenceString, text):
    maUtils.setObjectAnnotation(assemblyReferenceString, text)


#
def getAssemblyActive(assemblyReferenceString):
    return cmds.assembly(assemblyReferenceString, query=1, active=1) or 'None'


#
def getAssemblyLodLevel(assemblyReferenceString):
    lodLevel = 'LOD00'
    config = sceneryPr.assemblyLodColorConfig()
    color = cmds.getAttr(assemblyReferenceString + '.overrideColor')
    if color in config:
        lodLevel = config[color]
    return lodLevel


#
def setAssemblyLodLevel(assemblyReferenceString, lodLevel):
    activeItem = getAssemblyActive(assemblyReferenceString)
    #
    activeKey = ['GPU', 'Proxy'][activeItem.startswith('Proxy')]
    levelLabel = [none, lodLevel][lodLevel != 'LOD00']
    targetItem = [activeKey, activeKey + '-' + lodLevel][levelLabel != none]
    setAssemblyActive(assemblyReferenceString, targetItem)
    #
    colorConfig = sceneryPr.assemblyColorConfig()
    color = colorConfig[targetItem]
    maUtils.setNodeOverrideColor(assemblyReferenceString, color)


# Set Assembly
def setAssemblyActive(assemblyReferenceString, name):
    cmds.assembly(assemblyReferenceString + '.representations', edit=1, active=name)


#
def getAssemblyNamespace(assemblyReference):
    return cmds.assembly(assemblyReference, query=1, repNamespace=1)


#
def getAssemblyDefinitionFile(assemblyReference):
    return cmds.getAttr(assemblyReference + '.definition')


#
def setAssemblyReferenceCreate(nodeName, adFile):
    nodeName = cmds.assembly(name=nodeName, type='assemblyReference')
    cmds.setAttr(nodeName + '.definition', adFile, type='string')


#
def setScnGpuCacheCreate(objectString, cacheFile, lod=0):
    cmds.loadPlugin('gpuCache', quiet=1)
    #
    nodeName = maUtils._toNodeName(objectString)
    shapeName = nodeName + 'Shape'
    shapePath = objectString + '|' + shapeName
    #
    cacheFileAttr = shapePath + '.' + 'cacheFileName'
    #
    choiceNodeName = nodeName + 'Choice'
    lodAttrName = 'lod'
    lodAttr = objectString + '.' + lodAttrName
    #
    cmds.createNode('transform', name=nodeName)
    cmds.createNode('gpuCache', name=shapeName, parent=objectString)
    if isinstance(cacheFile, str) or isinstance(cacheFile, unicode):
        cmds.setAttr(cacheFileAttr, cacheFile, type='string')
    elif isinstance(cacheFile, tuple) or isinstance(cacheFile, list):
        cmds.setAttr(cacheFileAttr, cacheFile[lod], type='string')
        #
        cmds.addAttr(objectString, longName=lodAttrName, attributeType='enum', enumName='lod0:lod1:lod2:', keyable=1)
        #
        choiceNode = cmds.createNode('choice', name=choiceNodeName)
        for seq, i in enumerate(cacheFile):
            lodFileAttrName = 'lodCacheFile{}'.format(seq)
            lodFileAttr = objectString + '.' + lodFileAttrName
            targetAttr = choiceNode + '.' + 'input[{}]'.format(seq)
            #
            cmds.addAttr(objectString, longName=lodFileAttrName, dataType='string', usedAsFilename=1)
            cmds.setAttr(lodFileAttr, i, type='string')
            #
            cmds.connectAttr(lodFileAttr, targetAttr, force=1)
        #
        cmds.connectAttr(lodAttr, choiceNode + '.' + 'selector')
        cmds.connectAttr(choiceNode + '.' + 'output', cacheFileAttr)
        #
        cmds.setAttr(lodAttr, lod)


#
def setScnProxyCacheCreate(objectString, cacheFile, lod=0):
    cmds.loadPlugin('lxCommand', quiet=1)
    if not cmds.objExists('ArnoldStandInDefaultLightSet'):
        cmds.createNode('objectSet', name='ArnoldStandInDefaultLightSet', shared=1)
        cmds.lightlink(object='ArnoldStandInDefaultLightSet', light='defaultLightSet')
    #
    nodeName = maUtils._toNodeName(objectString)
    shapeName = nodeName + 'Shape'
    shapePath = objectString + '|' + shapeName
    #
    cacheFileAttr = shapePath + '.' + 'dso'
    #
    choiceNodeName = nodeName + 'Choice'
    lodAttrName = 'lod'
    lodAttr = objectString + '.' + lodAttrName
    #
    cmds.createNode('transform', name=nodeName)
    cmds.createNode('aiStandIn', name=shapeName, parent=objectString)
    #
    cmds.setAttr(shapePath + '.mode', 3)
    if isinstance(cacheFile, str) or isinstance(cacheFile, unicode):
        cmds.setAttr(cacheFileAttr, cacheFile, type='string')
    elif isinstance(cacheFile, tuple) or isinstance(cacheFile, list):
        cmds.setAttr(cacheFileAttr, cacheFile[lod], type='string')
        #
        cmds.addAttr(objectString, longName=lodAttrName, attributeType='enum', enumName='lod0:lod1:lod2:', keyable=1)
        #
        choiceNode = cmds.createNode('choice', name=choiceNodeName)
        for seq, i in enumerate(cacheFile):
            lodFileAttrName = 'lodCacheFile{}'.format(seq)
            lodFileAttr = objectString + '.' + lodFileAttrName
            targetAttr = choiceNode + '.' + 'input[{}]'.format(seq)
            #
            cmds.addAttr(objectString, longName=lodFileAttrName, dataType='string', usedAsFilename=1)
            cmds.setAttr(lodFileAttr, i, type='string')
            #
            cmds.connectAttr(lodFileAttr, targetAttr, force=1)
        #
        cmds.connectAttr(lodAttr, choiceNode + '.' + 'selector')
        cmds.connectAttr(choiceNode + '.' + 'output', cacheFileAttr)
        #
        cmds.setAttr(lodAttr, lod)


#
def getAssemblyReferencesTransformationByRoot(rootPath):
    lis = []
    nodeTypeLis = ['assemblyReference', 'transform']
    if maUtils.isAppExist(rootPath):
        rootName = maUtils._toNodeName(rootPath)
        objectPathLis = maUtils.getChildrenByRoot(rootPath)
        objectPathLis.insert(0, rootName)
        if objectPathLis:
            for objectPath in objectPathLis:
                if maUtils.getNodeType(objectPath) in nodeTypeLis:
                    if objectPath == rootName:
                        objectRelativePath = rootName
                    else:
                        objectRelativePath = rootName + objectPath.split(rootPath)[-1]
                    #
                    print objectRelativePath
                    transformationData = maUtils.getObjectTransformation(objectPath)
                    lis.append((objectRelativePath, transformationData))
    return lis


#
def getAssemblyReferencesWorldMatrixByRoot(rootPath):
    lis = []
    nodeTypeLis = ['assemblyReference', 'transform']
    if maUtils.isAppExist(rootPath):
        rootName = maUtils._toNodeName(rootPath)
        objectPathLis = maUtils.getChildrenByRoot(rootPath)
        #
        objectPathLis.insert(0, rootName)
        if objectPathLis:
            for objectPath in objectPathLis:
                if maUtils.getNodeType(objectPath) in nodeTypeLis:
                    objectRelativePath = rootName + objectPath.split(rootPath)[-1]
                    #
                    transformationData = maUtils.getNodeWorldMatrix(objectPath)
                    lis.append((objectRelativePath, transformationData))
    return lis


#
def getAssemblyCurrentItem(assemblyReferenceString):
    activeItem = getAssemblyActive(assemblyReferenceString)
    if activeItem.startswith('GPU'):
        activeItem = 'GPU'
    elif activeItem.startswith('Proxy'):
        activeItem = 'Proxy'
    return activeItem


# Get Select Scenery Object
def getSelSceneryObject(objects=none):
    def getBranch(maObj):
        if cmds.nodeType(maObj) == 'assemblyReference':
            adPathAttr = maObj + '.definition'
            adData = cmds.getAttr(adPathAttr)
            # Filter ( Assembly Unit )
            if adData:
                if 'assembly/unit' in adData:
                    lis.append(maObj)
        else:
            if cmds.listRelatives(maObj, parent=1, fullPath=1):
                getBranch(cmds.listRelatives(maObj, parent=1, fullPath=1)[0])
    #
    lis = []
    if not objects:
        objects = cmds.ls(selection=True)
    for i in objects:
        getBranch(i)
    return lis


#
class LxAssemblyMethod(object):
    NamespaceAttrName = 'namespace'
    LodAttrName = 'lod'
    #
    ProxyCacheOutputAttrName = 'proxyCacheFile'
    ProxyCacheNodeType = 'aiStandIn'
    ProxyCacheShapeLabel = 'ProxyCache'
    ProxyCacheFileAttrName = 'dso'
    ProxyCacheShowMode = 0
    #
    GpuCacheNodeType = 'gpuCache'
    GpuCacheOutputAttrName = 'gpuCacheFile'
    GpuCacheShapeLabel = 'GpuCache'
    GpuCacheFileAttrName = 'cacheFileName'
    #
    CurveShapeLabel = 'Curve'
    #
    AssetOutputAttrName = 'assetFile'
    #
    ControlShapeLabel = 'Control'
    ContainerLabel = 'Container'
    #
    Keyword = 'assemblyObjectEnable'
    def __init__(self, objectString):
        cmds.loadPlugin('lxProductNode', quiet=1)
        #
        self._objectPath = objectString
        self._objectName = maUtils._toNodeName(self._objectPath)
        #
        self._namespace = self._objectName + '_ns'
        #
        self._proxyCacheShapeName = self._objectName + self.ProxyCacheShapeLabel
        self._proxyCacheShapePath = maUtils._toNodePathString([self._objectPath, self._proxyCacheShapeName])
        #
        self._gpuCacheShapeName = self._objectName + self.GpuCacheShapeLabel
        self._gpuCacheShapePath = maUtils._toNodePathString([self._objectPath, self._gpuCacheShapeName])
        #
        self._curveShapeName = self._objectName + self.CurveShapeLabel
        #
        self._containerNodeName = self._objectName + self.ContainerLabel
        self._containerNodePath = maUtils._toNodePathString([self._objectPath, self._containerNodeName])
        #
        self._objectParentPath = maUtils._toNodeParentPath(self._objectPath)
        self._objectName = maUtils._toNodeName(self._objectPath)
    #
    def _setParentPathCreate(self):
        maUtils.setNodeParentPathCreate(self._objectPath)
    #
    def _setObjectCreate(self):
        if not maUtils.isAppExist(self._objectPath):
            cmds.createNode('asbTransform', name=self._objectName, parent=self._objectParentPath)
        #
        cmds.setAttr(maUtils._toNodeAttr([self._objectPath, self.NamespaceAttrName]), self._namespace, type='string')
        #
        cmds.setAttr(maUtils._toNodeAttr([self._objectPath, self.ProxyCacheOutputAttrName]), self._proxyCacheFile, type='string')
        cmds.setAttr(maUtils._toNodeAttr([self._objectPath, self.GpuCacheOutputAttrName]), self._gpuCacheFile, type='string')
        cmds.setAttr(maUtils._toNodeAttr([self._objectPath, self.AssetOutputAttrName]), self._assetFile, type='string')
        #
        cmds.setAttr(maUtils._toNodeAttr([self._objectPath, self.LodAttrName]), self._lod)
        #
        maUtils.setObjectDisplayHandleEnable(self._objectPath, True)
    #
    def _setProxyCacheCreate(self):
        if self._proxyCacheFile is not None:
            if not maUtils.isAppExist(self._proxyCacheShapePath):
                self._proxyCacheShapeName = self._objectName + self.ProxyCacheShapeLabel
                cmds.createNode(
                    self.ProxyCacheNodeType,
                    name=self._proxyCacheShapeName, parent=self._objectPath
                )
            #
            cmds.setAttr(self._proxyCacheShapePath + '.standInDrawOverride', 4)
            cmds.setAttr(self._proxyCacheShapePath + '.mode', self.ProxyCacheShowMode)
            cmds.setAttr(maUtils._toNodeAttr([self._proxyCacheShapePath, self.ProxyCacheFileAttrName]), self._proxyCacheFile, type='string')
    #
    def _setGpuCacheCreate(self):
        if self._gpuCacheFile is not None:
            if not maUtils.isAppExist(self._gpuCacheShapePath):
                cmds.createNode(
                    self.GpuCacheNodeType,
                    name=self._gpuCacheShapeName, parent=self._objectPath
                )
            cmds.setAttr(maUtils._toNodeAttr([self._gpuCacheShapePath, self.GpuCacheFileAttrName]), self._gpuCacheFile, type='string')
            maUtils.setNodeTemplate(self._gpuCacheShapePath)
    #
    def _setContainerCreate(self):
        if not maUtils.isAppExist(self._containerNodePath):
            cmds.container(type='dagContainer', name=self._containerNodeName)
            cmds.parent(self._containerNodeName, self._objectPath)
            cmds.setAttr(self._containerNodePath + '.blackBox', 1, lock=1)
            cmds.setAttr(self._containerNodePath + '.iconName', 'out_gpuCache.png', type='string')
            cmds.setAttr(self._containerNodePath + '.hiddenInOutliner', 1)
    #
    def _setContainerAddNodes(self):
        cmds.container(
            self._containerNodePath,
            edit=1,
            force=1,
            addNode=[
                self._gpuCacheShapePath,
                self._worldControlShape
            ]
        )
    #
    def updateBoundingBox(self, boundingBox):
        self._worldControlShape = maGeom.setNurbsCurveBoxCreate(self._objectPath, boundingBox)
        maUtils.setNodeCenterPivots(self._objectPath)
    #
    def updateMatrix(self, matrix):
        maUtils.setNodeWorldMatrix(self._objectPath, matrix)
    #
    def create(self, proxyCacheFile=None, gpuCacheFile=None, assetFile=None, lod=0):
        self._proxyCacheFile = proxyCacheFile
        self._gpuCacheFile = gpuCacheFile
        self._assetFile = assetFile
        #
        self._lod = lod
        #
        self._setParentPathCreate()
        self._setObjectCreate()
        #
        self._setProxyCacheCreate()
        self._setGpuCacheCreate()
        self._setContainerCreate()
    #
    def updateGeometry(self, matrix, boundingBox):
        self.updateBoundingBox(boundingBox)
        self.updateMatrix(matrix)
        #
        self._setContainerAddNodes()
