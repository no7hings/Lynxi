# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.api.OpenMaya as OpenMaya
#
from LxMaya.command import maUtils, maUuid, maAttr
#
modelObjectType = [
    'mesh',
    'nurbsSurface',
    'nurbsCurve'
]
#
MayaTransformType = 'transform'
#
none = ''


#
def setCreateObject(shapeType, objectName):
    shapeName = objectName + 'Shape'
    cmds.createNode(MayaTransformType, name=objectName)
    cmds.createNode(shapeType, name=shapeName, parent=objectName)


#
def setCloneAttributes(sourceObject, targetObject, useShape=False):
    if useShape is True:
        sourceObject = maUtils.getNodeShape(sourceObject)
        targetObject = maUtils.getNodeShape(targetObject)
    #
    sourceAttrData = maAttr.getNodeDefAttrDatumLis(sourceObject)
    if sourceAttrData:
        maAttr.setNodeDefAttrByData(targetObject, sourceAttrData)


#
def setCloneConnections(sourceObject, targetObject, useShape=False):
    if useShape is True:
        sourceObject = maUtils.getNodeShape(sourceObject)
        targetObject = maUtils.getNodeShape(targetObject)
    #
    sourceInputConnections = maUtils.getNodeInputConnectionLis(sourceObject)
    if sourceInputConnections:
        for sourceAttr, targetAttr in sourceInputConnections:
            attrName = maUtils.getAttrName(targetAttr)
            newTargetAttr = targetObject + '.' + attrName
            maUtils.setAttrConnect(sourceAttr, newTargetAttr)


# Transform Data ( Rebuild )
def getObjectTransformation_(objectPath):
    mTransform = maUtils.toM2TransformNode(objectPath)
    matrix = mTransform.transformation().asMatrix()
    return maUtils.getFloatArray(matrix)


#
def getObjectTransformCreateData(objectPath):
    parentPath = maUtils._toNodeParentPath(objectPath)
    transformName = maUtils._toNodeName(objectPath)
    transformNodeData = getObjectTransformation_(objectPath)
    customAttrData = maAttr.getNodeUserDefAttrData(objectPath)
    return parentPath, transformName, transformNodeData, customAttrData


#
def getObjectShapeCreateData(objectPath):
    shapePath = maUtils.getNodeShape(objectPath)
    #
    shapeName = maUtils._toNodeName(shapePath)
    shapeType = maUtils.getNodeType(shapePath)
    definedAttrData = maAttr.getNodeDefAttrDatumLis(shapePath)
    customAttrData = maAttr.getNodeUserDefAttrData(shapePath)
    return shapeName, shapeType, definedAttrData, customAttrData


#
def setCreateObjectTransformPath(transformData, lockTransform):
    parentPath, transformName, transformNodeData, transformCustomAttrData = transformData
    parentLocalPath = parentPath[1:]
    objectLocalPath = parentLocalPath + '|' + transformName
    if not maUtils.isAppExist(objectLocalPath):
        if not maUtils.isAppExist(parentLocalPath):
            maUtils.setAppPathCreate(parentLocalPath, lockTransform)
        #
        setCreateObjectTransform(transformName, transformNodeData, parentLocalPath)
        if transformCustomAttrData:
            maAttr.setObjectUserDefinedAttrs(objectLocalPath, transformCustomAttrData)
    return objectLocalPath


#
def setCreateObjectTransform(objectString, transformData, parent=none):
    if transformData:
        m2Transform = OpenMaya.MFnTransform()
        if parent:
            m2Transform.create(maUtils.toM2Object(parent))
        else:
            m2Transform.create()
        #
        m2Transform.setName(objectString)
        m2Transform.setTransformation(maUtils.getMTransformationMatrix(transformData))
        #
        objectPath = maUtils.getM2ObjectPath(m2Transform)
        #
        maUtils.setNodeOutlinerRgb(objectPath, 1, 1, 0)


#
def setCreateObjectShape(shapeName, shapeType, definedAttrData=None, customAttrData=None, transform=None):
    # Filter Exists
    if transform:
        shapePath = transform + '|' + shapeName
    else:
        shapePath = shapeName
    #
    if not maUtils.isAppExist(shapePath):
        if transform:
            cmds.createNode(shapeType, name=shapeName, parent=transform)
        else:
            cmds.createNode(shapeType, name=shapeName)
    #
    if definedAttrData:
        maAttr.setNodeDefAttrByData(shapePath, definedAttrData, lockAttribute=False)
    if customAttrData:
        maAttr.setObjectUserDefinedAttrs(shapePath, customAttrData, lockAttribute=False)


#
def setCreateTransformObject(objectName, shapeType, shapeDefinedAttrData=None, shapeCustomAttrData=None, parent=None):
    if parent:
        objectPath = parent + '|' + objectName
    else:
        objectPath = '|' + objectName
    #
    if not maUtils.isAppExist(objectPath):
        cmds.createNode(MayaTransformType, name=objectName, parent=parent)
        #
        shapeName = objectName + 'Shape'
        #
        setCreateObjectShape(
            shapeName, shapeType,
            definedAttrData=shapeDefinedAttrData, customAttrData=shapeCustomAttrData,
            transform=objectPath
        )


#
def getObjectCreateData(objectPath):
    return getObjectTransformCreateData(objectPath), getObjectShapeCreateData(objectPath)


#
def setCreateObjectByCreateData(objectData, uniqueId=None, lockTransform=True):
    if objectData:
        transformCreateData, shapeCreateData = objectData
        transformPath = setCreateObjectTransformPath(transformCreateData, lockTransform)
        #
        if uniqueId:
            maUuid.setUniqueIdForce(transformPath, uniqueId)
        #
        if shapeCreateData:
            shapeName, shapeType, shapeDefinedAttrData, shapeCustomAttrData = shapeCreateData
            setCreateObjectShape(
                shapeName, shapeType,
                definedAttrData=shapeDefinedAttrData, customAttrData=shapeCustomAttrData,
                transform=transformPath
            )


#
def setNodeCreateByAttrDatum(nodeCreateData):
    if nodeCreateData:
        nodeName, nodeType, nodeDefinedAttrData, nodeCustomAttrData = nodeCreateData
        setCreateObjectShape(
            nodeName, nodeType,
            definedAttrData=nodeDefinedAttrData, customAttrData=nodeCustomAttrData
        )


#
def getGraphDataByRoot(root):
    transfroms = []
    shapes = []
    children = maUtils.getChildrenByRoot(root, fullPath=True)
    if children:
        pass


#
def getObjectGraphData(objectString):
    def getBranch(objectString_):
        if not objectString_ in transformLis and not objectString_ in nodeLis:
            if maUtils.isTransform(objectString_):
                objectPath = maUtils._getNodePathString(objectString_)
                shapePath = maUtils._getNodePathString(objectString_)
                objectString_ = maUtils.getNodeShape(objectPath)
                #
                transformLis.append(objectPath)
            elif maUtils.isShape(objectString_):
                shapeLis.append(objectString_)
            else:
                nodeLis.append(objectString_)
            #
            branchNodes = maUtils.getInputShapeLis(objectString_)
            if branchNodes:
                [getBranch(i) for i in branchNodes]
    #
    transformLis = []
    shapeLis = []
    nodeLis = []
    #
    getBranch(objectString)
    return transformLis, shapeLis, nodeLis