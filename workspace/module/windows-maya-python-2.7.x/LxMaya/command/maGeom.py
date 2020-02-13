# encoding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.api.OpenMaya as OpenMaya

from LxBasic import bscCore, bscObjects
#
from LxCore import lxConfigure
#
from LxCore.config import appCfg
#
from LxDatabase.data import datHash
#
from LxMaya.command import maUtils, maUuid, maObj, maAttr
#
shapeLabel = 'Shape'
#
defaultUvSetName = 'map1'
#
none = ''


#
def toM2NodePath(objectString):
    return OpenMaya.MGlobal.getSelectionListByName(objectString).getDagPath(0)


#
def toM2MeshNode(meshObjectString, mode=0):
    if mode == 0:
        return OpenMaya.MFnMesh(toM2NodePath(meshObjectString))
    elif mode == 1:
        return OpenMaya.MFnMesh(meshObjectString)


#
def toM2SurfaceNode(nurbsSurfaceObjStr, mode=0):
    if mode == 0:
        return OpenMaya.MFnNurbsSurface(toM2NodePath(nurbsSurfaceObjStr))
    elif mode == 1:
        return OpenMaya.MFnNurbsSurface(nurbsSurfaceObjStr)


#
def toM2CurveNode(nurbsCurveObjStr, mode=0):
    if mode == 0:
        return OpenMaya.MFnNurbsCurve(toM2NodePath(nurbsCurveObjStr))
    elif mode == 1:
        return OpenMaya.MFnNurbsCurve(nurbsCurveObjStr)


#
def toM2TransformNode(objectString, mode=0):
    if mode == 0:
        return OpenMaya.MFnTransform(toM2NodePath(objectString))
    elif mode == 1:
        return OpenMaya.MFnTransform(objectString)


#
def toM2DagNode(objectString, mode=0):
    if mode == 0:
        return OpenMaya.MFnDagNode(toM2NodePath(objectString))
    elif mode == 1:
        return OpenMaya.MFnDagNode(objectString)


#
def getHir(groupString):
    def getBranch(objectString):
        m2DagNode = toM2DagNode(objectString)
        childCount = m2DagNode.childCount()
        if childCount:
            for seq in xrange(childCount):
                childObject = m2DagNode.child(seq)
                nodeType = childObject.apiTypeStr
                child = toM2DagNode(childObject, 1).fullPathName()
                if not isM2Intermediate(child):
                    dic.setdefault(objectString, []).append((child, nodeType))
                getBranch(child)
    #
    dic = bscCore.orderedDict()
    #
    getBranch(groupString)
    return dic


#
def getIntArray(m2IntArray):
    return [int(i) for i in m2IntArray]


#
def getFloatArray(m2FloatArray):
    return [float(i) for i in m2FloatArray]


#
def toM2Matrix(matrix):
    m2Matrix = OpenMaya.MMatrix()
    for seq in xrange(4):
        for subSeq in xrange(4):
            m2Matrix.setElement(seq, subSeq, matrix[seq * 4 + subSeq])
    return m2Matrix


#
def getPointArray(m2PointArray):
    return [(i[0], i[1], i[2]) for i in m2PointArray]


#
def toM2Point(point):
    m2Point = OpenMaya.MPoint()
    m2Point.x, m2Point.y, m2Point.z = point
    return m2Point


#
def toM2PointArray(pointArray):
    m2PointArray = OpenMaya.MPointArray()
    for point in pointArray:
        m2Point = toM2Point(point)
        m2PointArray.append(m2Point)
    return m2PointArray


#
def getVectorArray(m2VectorArray):
    return [(i[0], i[1], i[2]) for i in m2VectorArray]


#
def toM2Vector(vector):
    m2Vector = OpenMaya.MVector()
    m2Vector.x, m2Vector.y, m2Vector.z = vector
    return m2Vector


#
def toM2VectorArray(vectorArray):
    m2VectorArray = OpenMaya.MVectorArray()
    for vector in vectorArray:
        m2Vector = toM2Vector(vector)
        m2VectorArray.append(m2Vector)
    return m2VectorArray


#
def getFloatVector(m2FloatVector):
    x, y, z = m2FloatVector
    return x, y, z


#
def getTuple(m2Tuple):
    return '%s,%s' % (m2Tuple[0], m2Tuple[1])


#
def getFloatVectorArray(m2FloatVectorArray):
    return [(i[0], i[1], i[2]) for i in m2FloatVectorArray]


#
def toM2FloatVector(floatVector):
    m2FloatVector = OpenMaya.MFloatVector()
    m2FloatVector.x, m2FloatVector.y, m2FloatVector.z = floatVector
    return m2FloatVector


#
def toM2FloatVectorArray(floatVectorArray):
    m2FloatVectorArray = OpenMaya.MFloatVectorArray()
    for floatVector in floatVectorArray:
        m2FloatVector = toM2FloatVector(floatVector)
        m2FloatVectorArray.append(m2FloatVector)
    return m2FloatVectorArray


#
def getM2ObjectPath(m2Object):
    return m2Object.fullPathName()


#
def toM2ParentObject(objectString):
    m2DagNode = toM2DagNode(objectString)
    return m2DagNode.parent(0)


#
def getM2ParentPath(objectString):
    m2ParentObject = toM2ParentObject(objectString)
    return OpenMaya.MFnDagNode(m2ParentObject).fullPathName()


#
def getM2ParentName(objectString):
    m2ParentObject = toM2ParentObject(objectString)
    return OpenMaya.MFnDagNode(m2ParentObject).name()


#
def getNodeName(objectString):
    m2DagNode = toM2DagNode(objectString)
    return m2DagNode.name()


#
def toM2Object(objectString):
    return toM2DagNode(objectString).object()


#
def getM2Type(objectString):
    return toM2DagNode(objectString).object().apiTypeStr


#
def isM2Intermediate(objectString):
    m2DagNode = toM2DagNode(objectString)
    return m2DagNode.isIntermediateObject


#
def getMeshShapePath(objectString):
    m2Type = getM2Type(objectString)
    if m2Type == appCfg.M2TransformType:
        m2DagNode = toM2DagNode(objectString)
        count = m2DagNode.childCount()
        if count:
            for seq in xrange(count):
                childObject = m2DagNode.child(seq)
                m2Type = childObject.apiTypeStr
                childPath = toM2DagNode(childObject, 1).fullPathName()
                if m2Type == appCfg.M2MeshType:
                    if not isM2Intermediate(childPath):
                        meshShapePath = childPath
                        return meshShapePath


#
def isM2ObjectVisible(objectString):
    m2ObjectPath = toM2NodePath(objectString)
    return m2ObjectPath.isVisible


#
def getObjectsByGroup(groupString, filterM2Types):
    def getBranch(parentObject):
        m2DagNode = toM2DagNode(parentObject)
        count = m2DagNode.childCount()
        if count:
            for seq in xrange(count):
                childObject = m2DagNode.child(seq)
                childType = childObject.apiTypeStr
                childPath = toM2DagNode(childObject, 1).fullPathName()
                if childType in filterM2Types:
                    if not isM2Intermediate(childPath):
                        lis.append(parentObject)
                # Loop
                getBranch(childPath)
    #
    lis = []
    #
    filterM2Types = maUtils.string2list(filterM2Types)
    #
    if maUtils.isAppExist(groupString):
        getBranch(groupString)
    #
    return lis


#
def getGeometryObjectsByGroup(groupString):
    return getObjectsByGroup(
        groupString,
        [appCfg.M2MeshType, appCfg.M2NurbsSurfaceType, appCfg.M2NurbsCurveType]
    )


#
def getGeometryObjectIndexLisByGroup(groupString):
    objectString = getGeometryObjectsByGroup(groupString)


#
def getMeshObjectsByGroup(groupString):
    return getObjectsByGroup(
        groupString,
        appCfg.M2MeshType
    )


# Mesh Data ( Rebuild )
def getMeshObjectGeomData(meshObjectString):
    m2MeshObject = toM2MeshNode(meshObjectString)
    pointArray = m2MeshObject.getPoints()
    nSideArray, vertexIdArray = m2MeshObject.getVertices()
    return (
        (
            getIntArray(nSideArray),
            getIntArray(vertexIdArray)
        ),
        getPointArray(pointArray)
    )


#
def getNurbsSurfaceObjectGeomData(nurbsSurfaceObjStr):
    m2SurfaceObject = toM2SurfaceNode(nurbsSurfaceObjStr)
    cvPointArray = m2SurfaceObject.cvPositions()
    uKnotsArray = m2SurfaceObject.knotsInU()
    vKnotsArray = m2SurfaceObject.knotsInV()
    uDegree = m2SurfaceObject.degreeInU
    vDegree = m2SurfaceObject.degreeInV
    uForm = m2SurfaceObject.formInU
    vForm = m2SurfaceObject.formInV
    return (
        (
            (getFloatArray(uKnotsArray), getFloatArray(vKnotsArray)),
            (uDegree, vDegree),
            (uForm, vForm)
        ),
        getPointArray(cvPointArray)
    )


#
def getNurbsCurveObjectGeomData(nurbsCurveObjStr):
    m2CurveNode = toM2CurveNode(nurbsCurveObjStr)
    cvPointArray = m2CurveNode.cvPositions()
    knotsArray = m2CurveNode.knots()
    degree = m2CurveNode.degree
    form = m2CurveNode.form
    return (
        (
            getFloatArray(knotsArray),
            degree,
            form
        ),
        getPointArray(cvPointArray)
    )


#
def setNurbsCurveBoxCreate(objectString, worldBoundingBox):
    if not maUtils.isAppExist(objectString):
        objectName = maUtils._toNodeName(objectString)
        objectString = cmds.createNode('transform', name=objectName)
    #
    xmin, ymin, zmin, xmax, ymax, zmax = worldBoundingBox
    geomData = (
        (
            [float(i) for i in xrange(16)],
            1,
            1
        ),
        [
            (xmax, ymax, zmax), (xmax, ymax, zmin), (xmax, ymin, zmin), (xmax, ymin, zmax), (xmax, ymax, zmax),
            (xmin, ymax, zmax), (xmin, ymax, zmin), (xmax, ymax, zmin), (xmin, ymax, zmin), (xmin, ymin, zmin),
            (xmax, ymin, zmin), (xmin, ymin, zmin), (xmin, ymin, zmax), (xmax, ymin, zmax), (xmin, ymin, zmax),
            (xmin, ymax, zmax)
        ]
    )
    return setNurbsCurveShapeUpdate(objectString, geomData)


#
def setNurbsCurveShapeUpdate(objectString, geomData):
    shapeName = maUtils._toNodeName(objectString) + shapeLabel
    shapePath = objectString + '|' + shapeName
    #
    (knotsArray, degree, form), cvPointArray = geomData
    if not maUtils.isAppExist(shapePath):
        m2CurveNode = OpenMaya.MFnNurbsCurve()
        m2CurveNode.create(
            toM2PointArray(cvPointArray),
            knotsArray,
            degree,
            form,
            False,
            True,
            parent=toM2Object(objectString)
        )
        #
        m2CurveNode.setName(shapeName)
    else:
        m2CurveNode = toM2CurveNode(shapePath)
        m2CurveNode.setCVPositions(toM2PointArray(cvPointArray), space=4)
    #
    return shapePath


#
def getMeshObjectPointArray(meshObjectString):
    m2MeshObject = toM2MeshNode(meshObjectString)
    pointArray = m2MeshObject.getPoints(space=4)
    return getPointArray(pointArray)


#
def getMeshObjectVertexNormal(meshObjectString):
    m2MeshObject = toM2MeshNode(meshObjectString)
    normalArray = []
    vertexIds = range(m2MeshObject.numVertices)
    for vertexId in vertexIds:
        normal = m2MeshObject.getVertexNormal(vertexId, True)
        normalArray.append(normal)
    return getFloatVectorArray(normalArray), vertexIds


#
def getMeshFaceVertexNormal(meshObjectString):
    m2MeshObject = toM2MeshNode(meshObjectString)
    faceVertexNormalDataArray = []
    for faceId in xrange(m2MeshObject.numPolygons):
        vertexIdArray = m2MeshObject.getPolygonVertices(faceId)
        for vertexId in vertexIdArray:
            vertexNormal = m2MeshObject.getFaceVertexNormal(faceId, vertexId)
            faceVertexNormalData = getFloatVector(vertexNormal), faceId, vertexId
            faceVertexNormalDataArray.append(faceVertexNormalData)
    return faceVertexNormalDataArray


#
def getMeshObjectEdgeSmooth(meshObjectString):
    edgeIds = []
    edgeSmooths = []
    #
    m2MeshObject = toM2MeshNode(meshObjectString)
    for edgeId in xrange(m2MeshObject.numEdges):
        edgeIds.append(edgeId)
        edgeSmooths.append(m2MeshObject.isEdgeSmooth(edgeId))
    return edgeIds, edgeSmooths


#
def getSurfacePointLoops(nurbsSurfaceObjStr, useMode=0):
    m2SurfaceObject = toM2SurfaceNode(nurbsSurfaceObjStr)
    uIndexCount = m2SurfaceObject.numCVsInU
    vIndexCount = m2SurfaceObject.numCVsInV
    cvPointArray = []
    # Use U
    if useMode == 0:
        for uIndex in xrange(uIndexCount):
            subCvPointArray = []
            for vIndex in xrange(vIndexCount):
                cvPoint = m2SurfaceObject.cvPosition(uIndex, vIndex)
                if not cvPoint in subCvPointArray:
                    subCvPointArray.append(cvPoint)
            cvPointArray.append(getPointArray(subCvPointArray))
    # Use V
    if useMode == 1:
        for vIndex in xrange(vIndexCount - 1):
            subCvPointArray = []
            for uIndex in xrange(uIndexCount - 1):
                cvPoint = m2SurfaceObject.cvPosition(uIndex, vIndex)
                subCvPointArray.append(cvPoint)
            cvPointArray.append(getPointArray(subCvPointArray))
    return cvPointArray


#
def getCurveKnotsData(cvPointCount, degree):
    iPCount = cvPointCount - 2
    knotsArray = [0.0]*degree
    maxKnots = 1.0
    for seq in xrange(iPCount):
        knotsArray.append(float(seq + 1.0))
        maxKnots = seq + 2.0
    knotsArray += [maxKnots]*degree
    return knotsArray


#
def getCurvePointsPosition(nurbsCurveObjStr):
    m2CurveNode = toM2CurveNode(nurbsCurveObjStr)
    cvPointArray = m2CurveNode.cvPositions(space=4)
    return getPointArray(cvPointArray)


#
def getMeshTopoReduce(nSideData, vertexIdData):
    lis = []
    if nSideData:
        index = 0
        for seq, nSide in enumerate(nSideData):
            lis.append(seq)
            vertexIdArray = vertexIdData[index:index + nSide]
            vertexIdArray.sort()
            lis.extend(vertexIdArray)
            index += nSide
    return lis


#
def getMeshObjectGeomTopoInfoData(meshObjectString):
    m2MeshObject = toM2MeshNode(meshObjectString)
    try:
        nSideArray, vertexIdArray = m2MeshObject.getVertices()
        return getMeshTopoReduce(nSideArray, getIntArray(vertexIdArray))
    except RuntimeError:
        maUtils.viewError('{} is Error'.format(meshObjectString))


# Mesh Map
def getMeshObjectMapData(meshObjectString):
    dic = bscCore.orderedDict()
    #
    m2MeshObject = toM2MeshNode(meshObjectString)
    uvSetNames = m2MeshObject.getUVSetNames()
    # Debug ( Non - Exists Default Uv Sets )
    if not defaultUvSetName in uvSetNames:
        m2MeshObject.renameUVSet(uvSetNames[0], defaultUvSetName)
        uvSetNames = m2MeshObject.getUVSetNames()
    if uvSetNames:
        for uvSet in uvSetNames:
            uArray, vArray = m2MeshObject.getUVs(uvSet)
            nSideArray, uvIdArray = m2MeshObject.getAssignedUVs(uvSet)
            uvData = getIntArray(nSideArray), getIntArray(uvIdArray), getFloatArray(uArray), getFloatArray(vArray)
            dic[uvSet] = uvData
    return dic


#
def getNurbsSurfaceObjectMapData(objectString):
    m2SurfaceObject = toM2SurfaceNode(objectString)
    uArray, vArray = m2SurfaceObject.getUVs()


#
def setRepairMeshMap(meshObjectString):
    m2MeshObject = toM2MeshNode(meshObjectString)
    uvSetNames = m2MeshObject.getUVSetNames()
    # Debug ( Non - Exists Default Uv Sets )
    if not defaultUvSetName in uvSetNames:
        m2MeshObject.renameUVSet(uvSetNames[0], defaultUvSetName)


#
def getMeshObjectMapTopo(meshObjectString):
    lis = []
    #
    m2MeshObject = toM2MeshNode(meshObjectString)
    uvSetNames = m2MeshObject.getUVSetNames()
    if uvSetNames:
        # infoData.extend(uvSetNames)
        for seq, uvSet in enumerate(uvSetNames):
            lis.append(seq)
            nSideArray, uvIdArray = m2MeshObject.getAssignedUVs(uvSet)
            subTopoData = getMeshTopoReduce(nSideArray, getIntArray(uvIdArray))
            lis.extend(subTopoData)
    return lis


#
def getMeshObjectMapShape(meshObjectString):
    lis = []
    #
    m2MeshObject = toM2MeshNode(meshObjectString)
    uvSetNames = m2MeshObject.getUVSetNames()
    if uvSetNames:
        for uvSet in uvSetNames:
            if uvSet:
                uArray, vArray = m2MeshObject.getUVs(uvSet)
                lis.extend(getFloatArray(uArray))
                lis.extend(getFloatArray(vArray))
    return lis


#
def getGeometryObjectsPathDic(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getGeometryObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            objectString = maUtils.getObjectRelativePath(groupString, objectString)
            uniqueId = maUuid.getNodeUniqueId(objectString)
            dic[uniqueId] = objectString
    return dic


#
def getMeshObjectsPathData(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getMeshObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            dic[uniqueId] = objectString
    return dic


#
def getGeometryObjectsTransformDic(groupString, assetName):
    dic = bscCore.orderedDict()
    #
    objectStrings = getGeometryObjectsByGroup(groupString)
    if objectStrings:
        for seq, objectString in enumerate(objectStrings):
            parentObjectPath = maUtils._toNodeParentPath(objectString)
            parentObjectPath = maUtils.getObjectRelativePath(groupString, parentObjectPath)
            parentObjectPath = parentObjectPath.replace(assetName, '<assetName>')
            #
            objectName = maUtils._toNodeName(objectString)
            objectName = objectName.replace(assetName, '<assetName>')
            #
            transformationMatrix = maObj.getObjectTransformation_(objectString)
            customAttrData = maAttr.getNodeUserDefAttrData(objectString)
            rowIndex = seq
            #
            uniqueId = maUuid.getNodeUniqueId(objectString)
            dic[uniqueId] = parentObjectPath, objectName, transformationMatrix, customAttrData, rowIndex
    return dic


#
def getGeometryObjectsTransformDic_(objectStrings, groupString, assetName=None):
    dic = bscCore.orderedDict()
    #
    if objectStrings:
        for seq, objectString in enumerate(objectStrings):
            parentObjectPath = maUtils._toNodeParentPath(objectString)
            parentObjectPath = maUtils.getObjectRelativePath(groupString, parentObjectPath)
            objectName = maUtils._toNodeName(objectString)
            #
            if assetName is not None:
                parentObjectPath = parentObjectPath.replace(assetName, '<assetName>')
                objectName = objectName.replace(assetName, '<assetName>')
            #
            transformationMatrix = maObj.getObjectTransformation_(objectString)
            displayAttrData, customAttrData = maAttr.getObjectDisplayAttrData(objectString), maAttr.getNodeUserDefAttrData(objectString)
            #
            rowIndex = seq
            #
            uniqueId = maUuid.getNodeUniqueId(objectString)
            dic[uniqueId] = parentObjectPath, objectName, transformationMatrix, customAttrData + displayAttrData, rowIndex
    return dic


#
def getCompMeshesTransformData(groupString, assetName):
    dic = bscCore.orderedDict()
    #
    objectStrings = getMeshObjectsByGroup(groupString)
    if objectStrings:
        for seq, objectString in enumerate(objectStrings):
            parentObjectPath = maUtils._toNodeParentPath(objectString)
            parentObjectPath = parentObjectPath.replace(assetName, '<assetName>')
            #
            objectName = maUtils._toNodeName(objectString)
            objectName = objectName.replace(assetName, '<assetName>')
            #
            transformationMatrix = maObj.getObjectTransformation_(objectString)
            customAttrData = maAttr.getNodeUserDefAttrData(objectString)
            rowIndex = seq
            #
            uniqueId = maUuid.getNodeUniqueId(objectString)
            dic[uniqueId] = parentObjectPath, objectName, transformationMatrix, customAttrData, rowIndex
    return dic


#
def getNurbsCurveObjectsTransformData(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getObjectsByGroup(groupString, appCfg.M2NurbsCurveType)
    if objectStrings:
        for seq, objectString in enumerate(objectStrings):
            parentObjectPath = maUtils._toNodeParentPath(objectString)
            parentObjectPath = maUtils.getObjectRelativePath(groupString, parentObjectPath)
            #
            objectName = maUtils._toNodeName(objectString)
            #
            transformationMatrix = maObj.getObjectTransformation_(objectString)
            customAttrData = maAttr.getNodeUserDefAttrData(objectString)
            rowIndex = seq
            #
            uniqueId = maUuid.getNodeUniqueId(objectString)
            dic[uniqueId] = parentObjectPath, objectName, transformationMatrix, customAttrData, rowIndex
    return dic


#
def getGeometryObjectsGeometryDic(groupString):
    geomTopoDic, geomShapeDic = bscCore.orderedDict(), bscCore.orderedDict()
    #
    objectStrings = getGeometryObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                topologyData, shapeData = getMeshObjectGeomData(objectString)
            elif objectType == appCfg.MaNodeType_NurbsSurface:
                topologyData, shapeData = getNurbsSurfaceObjectGeomData(objectString)
            else:
                topologyData, shapeData = getNurbsCurveObjectGeomData(objectString)
            #
            geomTopoDic[uniqueId], geomShapeDic[uniqueId] = topologyData, shapeData
    return geomTopoDic, geomShapeDic


#
def getGeometryObjectsGeometryDic_(objectStrings):
    geomTopoDic, geomShapeDic = bscCore.orderedDict(), bscCore.orderedDict()
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                topologyData, shapeData = getMeshObjectGeomData(objectString)
            elif objectType == appCfg.MaNodeType_NurbsSurface:
                topologyData, shapeData = getNurbsSurfaceObjectGeomData(objectString)
            else:
                topologyData, shapeData = getNurbsCurveObjectGeomData(objectString)
            #
            geomTopoDic[uniqueId], geomShapeDic[uniqueId] = topologyData, shapeData
    return geomTopoDic, geomShapeDic


#
def getMeshObjectsGeomData(groupString):
    geomTopoDic, geomShapeDic = bscCore.orderedDict(), bscCore.orderedDict()
    #
    objectStrings = getMeshObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            topologyData, shapeData = getMeshObjectGeomData(objectString)
            geomTopoDic[uniqueId], geomShapeDic[uniqueId] = topologyData, shapeData
    return geomTopoDic, geomShapeDic


#
def getNurbsCurveObjectsGeomData(groupString):
    geomTopoDic, geomShapeDic = bscCore.orderedDict(), bscCore.orderedDict()
    #
    objectStrings = getObjectsByGroup(groupString, appCfg.M2NurbsCurveType)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            topologyData, shapeData = getNurbsCurveObjectGeomData(objectString)
            geomTopoDic[uniqueId], geomShapeDic[uniqueId] = topologyData, shapeData
    return geomTopoDic, geomShapeDic


#
def getGeometryObjectsVertexNormalDic(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getGeometryObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                vertexNormalData = getMeshObjectVertexNormal(objectString)
            else:
                vertexNormalData = None
            #
            dic[uniqueId] = vertexNormalData
    return dic


#
def getGeometryObjectsVertexNormalDic_(objectStrings):
    dic = bscCore.orderedDict()
    #
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                vertexNormal = getMeshObjectVertexNormal(objectString)
            else:
                vertexNormal = None
            #
            dic[uniqueId] = vertexNormal
    return dic


#
def getMeshObjectsVertexNormalData(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getMeshObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            vertexNormalData = getMeshObjectVertexNormal(objectString)
            dic[uniqueId] = vertexNormalData
    return dic


#
def getGeometryObjectsEdgeSmoothDic(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getGeometryObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                edgeSmoothData = getMeshObjectEdgeSmooth(objectString)
            else:
                edgeSmoothData = None
            #
            dic[uniqueId] = edgeSmoothData
    return dic


#
def getGeometryObjectsEdgeSmoothDic_(objectStrings):
    dic = bscCore.orderedDict()
    #
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                edgeSmoothData = getMeshObjectEdgeSmooth(objectString)
            else:
                edgeSmoothData = None
            #
            dic[uniqueId] = edgeSmoothData
    return dic


#
def getCompMeshesEdgeSmoothData(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getMeshObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            edgeSmooth = getMeshObjectEdgeSmooth(objectString)
            dic[uniqueId] = edgeSmooth
    return dic


#
def getGeometryObjectsMapDic(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getGeometryObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                mapData = getMeshObjectMapData(objectString)
            else:
                mapData = None
            #
            dic[uniqueId] = mapData
    return dic


#
def getGeometryObjectsMapDic_(objectStrings):
    dic = bscCore.orderedDict()
    #
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                mapData = getMeshObjectMapData(objectString)
            else:
                mapData = None
            #
            dic[uniqueId] = mapData
    return dic


#
def getCompMeshesMapData(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getMeshObjectsByGroup(groupString)
    if objectStrings:
        for objectString in objectStrings:
            uniqueId = maUuid.getNodeUniqueId(objectString)
            mapData = getMeshObjectMapData(objectString)
            dic[uniqueId] = mapData
    return dic


#
def getCompMeshesAttributeData(meshObjStrs):
    dic = bscCore.orderedDict()
    #
    if meshObjStrs:
        for objectString in meshObjStrs:
            meshShape = getMeshShapePath(objectString)
            uniqueId = maUuid.getNodeUniqueId(objectString)
            renderAttrData = maAttr.getNodeRenderAttrData(meshShape)
            plugAttrData = maAttr.getNodePlugAttrData(meshShape)
            customAttrData = maAttr.getNodeUserDefAttrData(meshShape)
            dic[uniqueId] = renderAttrData, plugAttrData, customAttrData
    return dic


#
def getObjectPathInfo(objectPath, groupString):
    if groupString.startswith('|'):
        groupString = groupString[1:]
    #
    groupName = maUtils._toNodeName(groupString)
    #
    relativePath = '|' + groupName + '|'.join(('|'.join(objectPath.split(groupString)[1:])).split('|'))
    if ':' in relativePath:
        namespace = ':'.join(objectPath.split('|')[-1].split(':')[:-1]) + ':'
        #
        relativePath = ('|' + groupName + '|'.join(('|'.join(objectPath.split(groupString)[1:])).split('|'))).replace(namespace, none)
    return datHash.getStrHashKey(relativePath)


#
def getGeometryObjectsPathInfo(objectStrings, groupString):
    lis = []
    for objectString in objectStrings:
        pathInfo = getObjectPathInfo(objectString, groupString)
        lis.append(pathInfo)
    #
    lis.sort()
    return datHash.getStrHashKey(lis)


#
def getMeshObjectsPathInfo(groupString, meshObjStrs=None):
    lis = []
    if meshObjStrs is None:
        meshObjStrs = getMeshObjectsByGroup(groupString)
    #
    for meshObjectString in meshObjStrs:
        pathInfo = getObjectPathInfo(meshObjectString, groupString)
        lis.append(pathInfo)
    #
    lis.sort()
    return datHash.getStrHashKey(lis)


#
def getGeometryObjectGeomInfo(objectString, roundLimit=8):
    objectType = maUtils.getShapeType(objectString)
    if objectType == appCfg.MaNodeType_Mesh:
        return getMeshObjectGeomInfo(objectString, roundLimit)
    elif objectType == appCfg.MaNodeType_NurbsSurface:
        return getNurbsSurfaceObjectGeomInfo(objectString, roundLimit)
    elif objectType == appCfg.MaNodeType_NurbsCurve:
        return getNurbsCurveObjectGeomInfo(objectString, roundLimit)


#
def getMeshObjectGeomInfo(objectString, roundLimit=8):
    return getMeshObjectGeomTopoInfo(objectString), getMeshObjectGeomShapeInfo(objectString, roundLimit)


#
def getNurbsSurfaceObjectGeomInfo(objectString, roundLimit=8):
    topoData, shapeData = getNurbsSurfaceObjectGeomData(objectString)
    return datHash.getNumHashKey(topoData), datHash.getFloatHashKey(shapeData, roundLimit)


#
def getNurbsCurveObjectGeomInfo(objectString, roundLimit=8):
    topoData, shapeData = getNurbsCurveObjectGeomData(objectString)
    return datHash.getNumHashKey(topoData), datHash.getFloatHashKey(shapeData, roundLimit)


#
def getGeometryObjectMapInfo(objectString, roundLimit=8):
    objectType = maUtils.getShapeType(objectString)
    if objectType == appCfg.MaNodeType_Mesh:
        return getMeshObjectMapInfo(objectString, roundLimit)
    elif objectType == appCfg.MaNodeType_NurbsSurface:
        return None, None
    elif objectType == appCfg.MaNodeType_NurbsCurve:
        return None, None


#
def getMeshObjectMapInfo(objectString, roundLimit=8):
    return getMeshObjectMapTopoInfo(objectString), getMeshObjectMapShapeInfo(objectString, roundLimit)


#
def getMeshObjectGeomTopoInfo(meshObjectString):
    infoData = getMeshObjectGeomTopoInfoData(meshObjectString)
    return datHash.getIntHashKey(infoData)


#
def getGeometryObjectsGeomInfo(objectStrings):
    geomTopoLis, geomShapeLis = [], []
    for objectString in objectStrings:
        geomTopoInfo, geomShapeInfo = getGeometryObjectGeomInfo(objectString)
        geomTopoLis.append(geomTopoInfo), geomShapeLis.append(geomShapeInfo)
    #
    geomTopoLis.sort(), geomShapeLis.sort()
    #
    return datHash.getStrHashKey(geomTopoLis), datHash.getStrHashKey(geomShapeLis)


#
def getMeshObjectsGeomTopoInfo(meshObjStrs):
    infoArray = [getMeshObjectGeomTopoInfo(meshObjectString) for meshObjectString in meshObjStrs]
    # Ignore Order
    infoArray.sort()
    return datHash.getStrHashKey(infoArray)


#
def getMeshObjectsGeomShapeInfo(meshObjStrs, roundLimit=8):
    infoArray = [getMeshObjectGeomShapeInfo(meshObjectString, roundLimit) for meshObjectString in meshObjStrs]
    # Ignore Order
    infoArray.sort()
    return datHash.getStrHashKey(infoArray)


#
def getMeshObjectGeomShapeInfo(meshObjectString, roundLimit=8):
    m2MeshObject = toM2MeshNode(meshObjectString)
    pointArray = m2MeshObject.getPoints()
    infoData = [j for i in getPointArray(pointArray) for j in i]
    return datHash.getFloatHashKey(infoData, roundLimit)


#
def getMeshObjectMapTopoInfo(meshObjectString):
    infoData = getMeshObjectMapTopo(meshObjectString)
    return datHash.getIntHashKey(infoData)


#
def getGeometryObjectsMapInfo(objectStrings):
    mapTopoLis, mapShapeLis = [], []
    for objectString in objectStrings:
        mapTopoInfo, mapShapeInfo = getGeometryObjectMapInfo(objectString)
        mapTopoLis.append(mapTopoInfo), mapShapeLis.append(mapShapeInfo)
    #
    mapTopoLis.sort(), mapShapeLis.sort()
    #
    return datHash.getStrHashKey(mapTopoLis), datHash.getStrHashKey(mapShapeLis)


#
def getMeshObjectsMapTopoInfo(meshObjStrs):
    infoArray = [getMeshObjectMapTopoInfo(meshObjectString) for meshObjectString in meshObjStrs]
    # Ignore Order
    infoArray.sort()
    return datHash.getStrHashKey(infoArray)


#
def getMeshObjectMapShapeInfo(meshObjectString, roundLimit=8):
    infoData = getMeshObjectMapShape(meshObjectString)
    return datHash.getFloatHashKey(infoData, roundLimit)


#
def getMeshObjectsMapShapeInfo(meshObjStrs):
    infoArray = [getMeshObjectMapShapeInfo(meshObjectString) for meshObjectString in meshObjStrs]
    infoArray.sort()
    return datHash.getStrHashKey(infoArray)


#
def getMeshAttrInfo(meshObjectString):
    infoData = []
    #
    meshShape = getMeshShapePath(meshObjectString)
    if meshShape:
        infoData.extend(maAttr.getNodeRenderAttrData(meshShape))
        infoData.extend(maAttr.getNodePlugAttrData(meshShape))
    return datHash.getStrHashKey(infoData)


#
def getMeshesAttrInfo(meshObjStrs):
    infoArray = [getMeshAttrInfo(meshObjectString) for meshObjectString in meshObjStrs]
    infoArray.sort()
    return datHash.getStrHashKey(infoArray)


#
def getGeometryObjectsInfo(groupString):
    objectStrings = getGeometryObjectsByGroup(groupString)
    #
    pathInfo = getGeometryObjectsPathInfo(objectStrings, groupString)
    geomTopoInfo, geomShapeInfo = getGeometryObjectsGeomInfo(objectStrings)
    mapTopoInfo, mapShapeInfo = getGeometryObjectsMapInfo(objectStrings)
    return (
        # Path
        pathInfo,
        # Nde_Geometry
        geomTopoInfo, geomShapeInfo,
        # Map
        mapTopoInfo, mapShapeInfo
    )


#
def getMeshObjectsInfo(groupString):
    meshObjStrs = getMeshObjectsByGroup(groupString)
    #
    pathInfo = getMeshObjectsPathInfo(groupString, meshObjStrs)
    geomTopoInfo = getMeshObjectsGeomTopoInfo(meshObjStrs)
    geomShapeInfo = getMeshObjectsGeomShapeInfo(meshObjStrs)
    mapTopoInfo = getMeshObjectsMapTopoInfo(meshObjStrs)
    mapShapeInfo = getMeshObjectsMapShapeInfo(meshObjStrs)
    return (
        # Path
        pathInfo,
        # Nde_Geometry
        geomTopoInfo, geomShapeInfo,
        # Map
        mapTopoInfo, mapShapeInfo
    )


#
def getGeometryObjectsInfoDic(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getGeometryObjectsByGroup(groupString)
    if objectStrings:
        # View Progress
        progressExplain = u'''Read Nde_Geometry Information'''
        maxValue = len(objectStrings)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for objectString in objectStrings:
            progressBar.update()
            #
            uniqueId = maUuid.getNodeUniqueId(objectString)
            #
            dic[uniqueId] = \
                (getObjectPathInfo(objectString, groupString), ) + \
                getGeometryObjectGeomInfo(objectString) + \
                getGeometryObjectMapInfo(objectString)
    #
    return dic


#
def getGeometryObjectsInfoDic_(objectStrings, groupString):
    dic = bscCore.orderedDict()
    #
    for objectString in objectStrings:
        uniqueId = maUuid.getNodeUniqueId(objectString)
        #
        pathInfo = getObjectPathInfo(objectString, groupString)
        geomTopoInfo, geomShapeInfo = getGeometryObjectGeomInfo(objectString)
        mapTopoInfo, mapShapeInfo = getGeometryObjectMapInfo(objectString)
        #
        dic[uniqueId] = (
            # Path
            pathInfo,
            # Nde_Geometry
            geomTopoInfo, geomShapeInfo,
            # Map
            mapTopoInfo, mapShapeInfo
        )
    #
    return dic


#
def getMeshObjectsInfoDic(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getMeshObjectsByGroup(groupString)
    if objectStrings:
        # View Progress
        progressExplain = u'''Read Mesh Information'''
        maxValue = len(objectStrings)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for objectString in objectStrings:
            progressBar.update()
            #
            uniqueId = maUuid.getNodeUniqueId(objectString)
            #
            dic[uniqueId] = (
                # Path
                getObjectPathInfo(objectString, groupString),
                # Nde_Geometry
                getMeshObjectGeomTopoInfo(objectString),
                getMeshObjectGeomShapeInfo(objectString),
                # Map
                getMeshObjectMapTopoInfo(objectString),
                getMeshObjectMapShapeInfo(objectString)
            )
    return dic


#
def getNurbsCurveObjectsInfoData(groupString):
    dic = bscCore.orderedDict()
    #
    objectStrings = getObjectsByGroup(groupString, appCfg.M2NurbsCurveType)
    if objectStrings:
        # View Progress
        progressExplain = u'''Read Nurbs Curve Information'''
        maxValue = len(objectStrings)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        #
        for objectString in objectStrings:
            progressBar.update()
            uniqueId = maUuid.getNodeUniqueId(objectString)
            #
            dic[uniqueId] = (
                # Path
                getObjectPathInfo(objectString, groupString),
                # Nde_Geometry
            ) + tuple(getNurbsCurveObjectGeomInfo(objectString))
    return dic


#
def getScGeometryObjectsInfoDic_(groupString, pathKey, searchRoot):
    dic = bscCore.orderedDict()
    #
    objectStrings = getGeometryObjectsByGroup(groupString)
    if objectStrings:
        # View Progress
        progressExplain = u'''Read Nde_Geometry Information'''
        maxValue = len(objectStrings)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for objectString in objectStrings:
            progressBar.update()
            if searchRoot in objectString:
                key = maUtils._toNodeName(objectString)
                #
                pathInfo = getObjectPathInfo(objectString, pathKey)
                geomTopoInfo, geomShapeInfo = getGeometryObjectGeomInfo(objectString)
                mapTopoInfo, mapShapeInfo = getGeometryObjectMapInfo(objectString)
                dic[key] = (
                    # Path
                    pathInfo,
                    # Nde_Geometry
                    geomTopoInfo, geomShapeInfo,
                    # Map
                    mapTopoInfo, mapShapeInfo
                )
    return dic


#
def setCreateGeometryObjectShape(objectString, geomData, shapeName=none):
    if geomData:
        if maUtils.isAppExist(objectString):
            if not shapeName:
                shapeName = maUtils._toNodeName(objectString) + shapeLabel
            objectShape = maUtils.getNodeShape(objectString)
            if not maUtils.isAppExist(objectShape):
                geomTopData, geomShapeData = geomData
                if len(geomTopData) == 2:
                    m2MeshObject = OpenMaya.MFnMesh()
                    nSideArray, vertexIdArray = geomTopData
                    pointArray = geomShapeData
                    m2MeshObject.create(
                        toM2PointArray(pointArray),
                        nSideArray,
                        vertexIdArray,
                        parent=toM2Object(objectString)
                    )
                    #
                    m2MeshObject.setName(shapeName)
                elif len(geomTopData) == 3:
                    m2CurveNode = OpenMaya.MFnNurbsCurve()
                    knotsArray, degree, form = geomTopData
                    cvPointArray = geomShapeData
                    if isinstance(form, int):
                        m2CurveNode.create(
                            toM2PointArray(cvPointArray),
                            knotsArray,
                            degree,
                            form,
                            False,
                            True,
                            parent=toM2Object(objectString)
                        )
                        #
                        m2CurveNode.setName(shapeName)
                    elif isinstance(form, list):
                        m2SurfaceObject = OpenMaya.MFnNurbsSurface()
                        (uKnotsArray, vKnotsArray), (uDegree, vDegree), (uForm, vForm) = knotsArray, degree, form
                        m2SurfaceObject.create(
                            toM2PointArray(cvPointArray),
                            uKnotsArray, vKnotsArray,
                            uDegree, vDegree,
                            uForm, vForm,
                            True,
                            parent=toM2Object(objectString)
                        )
                        #
                        m2SurfaceObject.setName(shapeName)


#
def setCreateMeshObjectShape(objectString, geomData, shapeName=none):
    if geomData:
        if maUtils.isAppExist(objectString):
            if not shapeName:
                shapeName = maUtils._toNodeName(objectString) + shapeLabel
            #
            shapePath = objectString + '|' + shapeName
            #
            if not maUtils.isAppExist(shapePath):
                m2MeshObject = OpenMaya.MFnMesh()
                (nSideArray, vertexIdArray), pointArray = geomData
                m2MeshObject.create(
                    toM2PointArray(pointArray),
                    nSideArray,
                    vertexIdArray,
                    parent=toM2Object(objectString)
                )
                #
                m2MeshObject.setName(shapeName)


#
def setCreateNurbsSurfaceObjectShape(objectString, geomData, shapeName=None):
    if geomData:
        if maUtils.isAppExist(objectString):
            if not shapeName:
                shapeName = maUtils._toNodeName(objectString) + shapeLabel
            #
            shapePath = objectString + '|' + shapeName
            #
            if not maUtils.isAppExist(shapePath):
                m2SurfaceObject = OpenMaya.MFnNurbsSurface()
                ((uKnotsArray, vKnotsArray), (uDegree, vDegree), (uForm, vForm)), cvPointArray = geomData
                m2SurfaceObject.create(
                    toM2PointArray(cvPointArray),
                    uKnotsArray, vKnotsArray,
                    uDegree, vDegree,
                    uForm, vForm,
                    True,
                    parent=toM2Object(objectString)
                )
                #
                m2SurfaceObject.setName(shapeName)


#
def setNurbsCurveShapeCreate(objectString, geomData, shapeName=None):
    if geomData:
        if not shapeName:
            shapeName = maUtils._toNodeName(objectString) + shapeLabel
        #
        m2CurveNode = OpenMaya.MFnNurbsCurve()
        (knotsArray, degree, form), cvPointArray = geomData
        m2CurveNode.create(
            toM2PointArray(cvPointArray),
            knotsArray,
            degree,
            form,
            False,
            True,
            parent=toM2Object(objectString)
        )
        #
        m2CurveNode.setName(shapeName)


#
def setCreateObjectGraphGeometrySub(objectData, lockTransform=False):
    shapeName, shapeType, transformData, geomData, mapData = objectData
    objectString = maObj.setCreateObjectTransformPath(transformData, lockTransform)
    if shapeType == appCfg.MaNodeType_Mesh:
        setCreateMeshObjectShape(objectString, geomData, shapeName)
        setCreateMeshObjectMap(objectString, mapData)
        maUtils.setObjectDefaultShadingEngine(objectString)
    elif shapeType == appCfg.MaNodeType_NurbsSurface:
        setCreateNurbsSurfaceObjectShape(objectString, geomData, shapeName)
        maUtils.setObjectDefaultShadingEngine(objectString)
    elif shapeType == appCfg.MaNodeType_NurbsCurve:
        setNurbsCurveShapeCreate(objectString, geomData, shapeName)


#
def setCreateObjectsTransform(transformDataDic, assetName, lockTransform):
    if transformDataDic:
        rowIndexLis = []
        #
        dic = bscCore.orderedDict()
        for uniqueId, data in transformDataDic.items():
            parentObjectPath, objectName, transformationMatrix, customAttrData, rowIndex = data
            #
            parentObjectPath = parentObjectPath.replace('<assetName>', assetName)
            objectName = objectName.replace('<assetName>', assetName)
            #
            rowIndexLis.append(rowIndex)
            #
            dic[rowIndex] = uniqueId, parentObjectPath, objectName, transformationMatrix, customAttrData
        #
        if rowIndexLis:
            rowIndexLis.sort()
            for rowIndex in rowIndexLis:
                uniqueId, parentObjectPath, objectName, transformationMatrix, customAttrData = dic[rowIndex]
                #
                if parentObjectPath.startswith('|'):
                    parentLocalPath = parentObjectPath[1:]
                else:
                    parentLocalPath = parentObjectPath
                #
                objectLocalPath = parentLocalPath + '|' + objectName
                if not maUtils.isAppExist(objectLocalPath):
                    if not maUtils.isAppExist(parentLocalPath):
                        maUtils.setAppPathCreate(parentLocalPath, lockTransform)
                    #
                    maObj.setCreateObjectTransform(objectName, transformationMatrix, parentLocalPath)
                    if customAttrData:
                        maAttr.setObjectUserDefinedAttrs(objectLocalPath, customAttrData)
                    #
                    maUuid.setUniqueIdForce(objectLocalPath, uniqueId)
                else:
                    print u'{} is Exists'.format(objectName)


#
def setCreateGeometryObjectsShape(dataDics):
    geomTopoDic, geomShapeDic = dataDics
    if geomTopoDic and geomShapeDic:
        for uniqueId, topologyData in geomTopoDic.items():
            shapeData = geomShapeDic[uniqueId]
            objectPath = maUuid.getObject(uniqueId)
            if objectPath:
                shapeName = maUtils.getAttrDatum(objectPath, lxConfigure.LynxiObjectShapeNameAttrName)
                setCreateGeometryObjectShape(objectPath, (topologyData, shapeData), shapeName)


#
def setCreateMeshObjectsGeometry(dataDics):
    geomTopoDic, geomShapeDic = dataDics
    if geomTopoDic and geomShapeDic:
        for uniqueId, topologyData in geomTopoDic.items():
            shapeData = geomShapeDic[uniqueId]
            objectStrings = maUuid.getObjects(uniqueId)
            if objectStrings:
                objectString = objectStrings[0]
                setCreateMeshObjectShape(objectString, (topologyData, shapeData))


#
def setCreateNurbsCurveObjectsGeometry(dataDics):
    geomTopoDic, geomShapeDic = dataDics
    if geomTopoDic and geomShapeDic:
        for uniqueId, topologyData in geomTopoDic.items():
            shapeData = geomShapeDic[uniqueId]
            objectStrings = maUuid.getObjects(uniqueId)
            if objectStrings:
                objectString = objectStrings[0]
                setNurbsCurveShapeCreate(objectString, (topologyData, shapeData))


# Sub Method
def setCreateMeshObjectEdgeSmooth(meshObjectString, smoothData):
    edgeIds, edgeSmooths = smoothData
    m2MeshObject = toM2MeshNode(meshObjectString)
    #
    m2MeshObject.setEdgeSmoothings(edgeIds, edgeSmooths)
    #
    m2MeshObject.updateSurface()


#
def setCreateGeometryObjectsEdgeSmooth(dataDic):
    if dataDic:
        for uniqueId, data in dataDic.items():
            if data:
                objectStrings = maUuid.getObjects(uniqueId)
                if objectStrings:
                    objectString = objectStrings[0]
                    objectType = maUtils.getShapeType(objectString)
                    if objectType == appCfg.MaNodeType_Mesh:
                        setCreateMeshObjectEdgeSmooth(objectString, data)


#
def setCreateCompMeshesEdgeSmooth(dataDic):
    if dataDic:
        for uniqueId, data in dataDic.items():
            if data:
                objectStrings = maUuid.getObjects(uniqueId)
                if objectStrings:
                    objectString = objectStrings[0]
                    setCreateMeshObjectEdgeSmooth(objectString, data)


# Sub Method
def setCreateMeshObjectMap(meshObjectString, mapData):
    if mapData:
        m2MeshObject = toM2MeshNode(meshObjectString)
        # Get Map Sets
        mapSets = m2MeshObject.getUVSetNames()
        for mapSet, uvData in mapData.items():
            if not mapSet in mapSets:
                m2MeshObject.createUVSet(mapSet)
            m2MeshObject.clearUVs(mapSet)
            nSideArray, uvIdArray, uArray, vArray = uvData
            m2MeshObject.setUVs(uArray, vArray, mapSet)
            m2MeshObject.assignUVs(nSideArray, uvIdArray, mapSet)


#
def setCreateGeometryObjectMap(dataDic):
    if dataDic:
        for uniqueId, mapData in dataDic.items():
            objectStrings = maUuid.getObjects(uniqueId)
            if objectStrings:
                objectString = objectStrings[0]
                objectType = maUtils.getShapeType(objectString)
                if objectType == appCfg.MaNodeType_Mesh:
                    setCreateMeshObjectMap(objectString, mapData)


#
def setCreateCompMeshesMap(dataDic):
    if dataDic:
        for uniqueId, mapData in dataDic.items():
            objectStrings = maUuid.getObjects(uniqueId)
            if objectStrings:
                objectString = objectStrings[0]
                setCreateMeshObjectMap(objectString, mapData)


# Sub Method
def setCreateMeshAttr(meshShape, attrData):
    if attrData:
        renderAttrData, plugAttrData, customAttrData = attrData
        if renderAttrData:
            maAttr.setNodeDefAttrByData(meshShape, renderAttrData)
        if plugAttrData:
            maAttr.setNodeDefAttrByData(meshShape, plugAttrData)
        if customAttrData:
            maAttr.setObjectUserDefinedAttrs(meshShape, customAttrData)


#
def setCreateCompMeshesAttribute(attrDic):
    if attrDic:
        for uniqueId, attrData in attrDic.items():
            meshObjectString = maUuid.getObject(uniqueId)
            if meshObjectString:
                meshShape = getMeshShapePath(meshObjectString)
                setCreateMeshAttr(meshShape, attrData)


#
def setMeshVertexNormal(meshObjectString, vertexNormalsData):
    m2MeshObject = toM2MeshNode(meshObjectString)
    normalArray, vertexIdArray = vertexNormalsData
    for seq, vertexId in enumerate(vertexIdArray):
        normal = toM2Vector(normalArray[seq])
        m2MeshObject.setVertexNormal(normal, vertexId)
    #
    m2MeshObject.updateSurface()


#
def setMeshFaceVertexNormals(meshObjectString, faceVertexNormalsData):
    m2MeshObject = toM2MeshNode(meshObjectString)
    for data in faceVertexNormalsData:
        vertexNormal, faceId, vertexId = data
        m2MeshObject.setFaceVertexNormal(toM2Vector(vertexNormal), faceId, vertexId)
    #
    m2MeshObject.updateSurface()


#
def getMeshObjectIsNormalLocked(meshObjectString):
    boolean = True
    if maUtils.isAppExist(meshObjectString):
        lis = []
        m2MeshObject = toM2MeshNode(meshObjectString)
        for vertexId in xrange(m2MeshObject.numVertices):
            if not m2MeshObject.isNormalLocked(vertexId):
                lis.append(vertexId)
        if lis:
            if len(lis) == m2MeshObject.numVertices:
                boolean = False
    else:
        boolean = False
    return boolean


#
def setMeshVertexNormalLock(meshObjectString):
    m2MeshObject = toM2MeshNode(meshObjectString)
    m2MeshObject.lockVertexNormals(xrange(m2MeshObject.numVertices))


#
def setMeshVertexNormalUnlock(meshObjectString):
    m2MeshObject = toM2MeshNode(meshObjectString)
    m2MeshObject.unlockVertexNormals(xrange(m2MeshObject.numVertices))


#
def setMeshEdgeSmooth(meshObjectString, boolean):
    m2MeshObject = toM2MeshNode(meshObjectString)
    edgeCount = m2MeshObject.numEdges
    m2MeshObject.setEdgeSmoothings(xrange(edgeCount), [boolean]*edgeCount)
    #
    m2MeshObject.updateSurface()


#
def setMeshVertexs(meshObjectString, pointArray):
    m2MeshObject = toM2MeshNode(meshObjectString)
    m2PointArray = toM2PointArray(pointArray)
    #
    m2MeshObject.setPoints(m2PointArray)
    #
    m2MeshObject.updateSurface()


#
def getMeshesTopoConstantData(groupString, withShape=0, maxRound=8):
    dic = {}
    meshObjStrs = getMeshObjectsByGroup(groupString)
    if meshObjStrs:
        # View Progress
        progressExplain = u'''Read Mesh Topology'''
        maxValue = len(meshObjStrs)
        progressBar = bscObjects.If_Progress(progressExplain, maxValue)
        for meshObjectString in meshObjStrs:
            progressBar.update()
            info = getMeshObjectGeomTopoInfo(meshObjectString)
            if withShape:
                geomShapeInfo = getMeshObjectGeomShapeInfo(meshObjectString, maxRound)
                info = info + geomShapeInfo
            # Debug ( Identical Topology )
            dic.setdefault(info, []).append(meshObjectString)
    return dic


#
def isMeshGeomTopoMatch(sourceMeshObject, targetMeshObject):
    boolean = False
    if cmds.objExists(sourceMeshObject) and cmds.objExists(targetMeshObject):
        if getMeshObjectGeomTopoInfo(sourceMeshObject) == getMeshObjectGeomTopoInfo(targetMeshObject):
            boolean = True
    return boolean


#
def clearZeroFace():
    pass


#
def setSelectCoincideFace(groupString, roundLimit=8):
    lis = []
    meshObjStrs = getMeshObjectsByGroup(groupString)
    if meshObjStrs:
        dic = {}
        for meshObjectString in meshObjStrs:
            m2MeshObject = toM2MeshNode(meshObjectString)
            mPointArray = m2MeshObject.getPoints()
            pointArray = getPointArray(mPointArray)
            pointArray.sort()
            infoData = [j for i in pointArray for j in i]
            hashKey = datHash.getFloatHashKey(infoData, roundLimit)
            dic.setdefault(hashKey, []).append(meshObjectString)
        if dic:
            for k, v in dic.items():
                if len(v) > 1:
                    for i in v[1:]:
                        lis.append(i)
    if lis:
        maUtils.setNodeSelect(lis)


#
def setGeometryObjectsDefaultShadingEngine(uniqueIds):
    for uniqueId in uniqueIds:
        objectString = maUuid.getObject(uniqueId)
        if objectString:
            objectType = maUtils.getShapeType(objectString)
            if objectType == appCfg.MaNodeType_Mesh:
                maUtils.setObjectDefaultShadingEngine(objectString)
            elif objectType == appCfg.MaNodeType_NurbsSurface:
                maUtils.setObjectDefaultShadingEngine(objectString)


# Get Poly Mesh Evaluate ( Method )
def getMeshObjectEvaluate(objectStrings, vertex, edge, face, triangle, uvcoord, area, worldArea, shell, boundingBox, showMode):
    # Dict { <Evaluate Name>: <Evaluate Data> }
    dic = bscCore.orderedDict()
    used = [vertex, edge, face, triangle, uvcoord, area, worldArea, shell, boundingBox]
    # View Progress
    explain = '''Read Mesh Evaluate Data'''
    maxValue = sum(used)
    progressBar = bscObjects.If_Progress(explain, maxValue)
    # >>>> 01
    if vertex:
        progressBar.update('Vertex')
        dic['vertex'] = cmds.polyEvaluate(objectStrings, vertex=1)
    # >>>> 02
    if edge:
        progressBar.update('Edge')
        dic['edge'] = cmds.polyEvaluate(objectStrings, edge=1)
    # >>>> 03
    if face:
        progressBar.update('Face')
        dic['face'] = cmds.polyEvaluate(objectStrings, face=1)
    # >>>> 04
    if triangle:
        progressBar.update('Triangle')
        dic['triangle'] = cmds.polyEvaluate(objectStrings, triangle=1)
    # >>>> 05
    if uvcoord:
        progressBar.update('UV')
        dic['uvcoord'] = cmds.polyEvaluate(objectStrings, uvcoord=1)
    # >>>> 06
    if area:
        progressBar.update('Area')
        dic['area'] = cmds.polyEvaluate(objectStrings, area=1)
    # >>>> 07
    if worldArea:
        progressBar.update('World Area')
        dic['worldArea'] = cmds.polyEvaluate(objectStrings, worldArea=1)
    # >>>> 08
    if shell:
        progressBar.update('Shell')
        dic['shell'] = cmds.polyEvaluate(objectStrings, shell=1)
    # >>>> 09
    if boundingBox:
        progressBar.update('Bounding Box')
        dic['boundingBox'] = cmds.polyEvaluate(objectStrings, boundingBox=1)
    return dic


# Get Poly Meshes's Evaluate ( Data )
def getMeshObjectsEvaluateDic(objectStrings, showMode=0):
    # Dict { <Poly Mesh> :
    #        List [ <Evaluate Info> ] }
    dic = bscCore.orderedDict()
    if objectStrings:
        count = len(objectStrings)
        data = getMeshObjectEvaluate(
            objectStrings,
            vertex=1, edge=1, face=1, triangle=1, uvcoord=1, area=1, worldArea=1, shell=1, boundingBox=1,
            showMode=showMode
        )
        box = data['boundingBox']
        #
        dic['geometries'] = count
        dic['vertex'] = data['vertex']
        dic['edge'] = data['edge']
        dic['face'] = data['face']
        dic['triangle'] = data['triangle']
        dic['uvcoord'] = data['uvcoord']
        dic['area'] = data['area']
        dic['worldArea'] = data['worldArea']
        dic['shell'] = data['shell']
        dic['axisX'] = box[0][1] + box[0][0]
        dic['horz'] = box[1][0]
        dic['widthX'] = box[0][1] - box[0][0]
        dic['heightY'] = box[1][1] - box[1][0]
        dic['widthZ'] = box[2][1] - box[2][0]
    return dic


#
def getGeometryObjectsConstantDic(groupString):
    infoKeyLis = ['hierarchy', 'geometry', 'geometryShape', 'map', 'mapShape']
    #
    dic = bscCore.orderedDict()
    #
    info = getGeometryObjectsInfo(groupString)
    for seq, i in enumerate(infoKeyLis):
        dic[i] = info[seq]
    return dic


#
def getGeometryObjectsConstantDic_(groupString):
    dic = bscCore.orderedDict()
    #
    meshObjStrs = getMeshObjectsByGroup(groupString)
    if meshObjStrs:
        dic = getMeshObjectsEvaluateDic(meshObjStrs)
    #
    geometryObjStrs = getGeometryObjectsByGroup(groupString)
    if geometryObjStrs:
        subDic = getGeometryObjectsConstantDic(groupString)
        for k, v in subDic.items():
            dic[k] = v
    return dic


#
def getMeshReferenceObject(objectString):
    shapePath = maUtils.getNodeShape(objectString)
    attr = shapePath + '.referenceObject'
    guessData = maUtils.getInputNodeLisByAttr(attr)
    if guessData:
        return guessData[0]