# encoding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.api.OpenMaya as OpenMaya

from LxBasic import bscMtdCore, bscMethods, bscObjects

from LxPreset import prsConfigure
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
def toM2NodePath(nodepathString):
    return OpenMaya.MGlobal.getSelectionListByName(nodepathString).getDagPath(0)


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
def toM2TransformNode(nodepathString, mode=0):
    if mode == 0:
        return OpenMaya.MFnTransform(toM2NodePath(nodepathString))
    elif mode == 1:
        return OpenMaya.MFnTransform(nodepathString)


#
def toM2DagNode(nodepathString, mode=0):
    if mode == 0:
        return OpenMaya.MFnDagNode(toM2NodePath(nodepathString))
    elif mode == 1:
        return OpenMaya.MFnDagNode(nodepathString)


#
def getHir(groupString):
    def getBranch(nodepathString):
        m2DagNode = toM2DagNode(nodepathString)
        childCount = m2DagNode.childCount()
        if childCount:
            for seq in xrange(childCount):
                childObject = m2DagNode.child(seq)
                nodeType = childObject.apiTypeStr
                child = toM2DagNode(childObject, 1).fullPathName()
                if not isM2Intermediate(child):
                    dic.setdefault(nodepathString, []).append((child, nodeType))
                getBranch(child)
    #
    dic = bscMtdCore.orderedDict()
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
def toM2ParentObject(nodepathString):
    m2DagNode = toM2DagNode(nodepathString)
    return m2DagNode.parent(0)


#
def getM2ParentPath(nodepathString):
    m2ParentObject = toM2ParentObject(nodepathString)
    return OpenMaya.MFnDagNode(m2ParentObject).fullPathName()


#
def getM2ParentName(nodepathString):
    m2ParentObject = toM2ParentObject(nodepathString)
    return OpenMaya.MFnDagNode(m2ParentObject).name()


#
def getNodeName(nodepathString):
    m2DagNode = toM2DagNode(nodepathString)
    return m2DagNode.name()


#
def toM2Object(nodepathString):
    return toM2DagNode(nodepathString).object()


#
def getM2Type(nodepathString):
    return toM2DagNode(nodepathString).object().apiTypeStr


#
def isM2Intermediate(nodepathString):
    m2DagNode = toM2DagNode(nodepathString)
    return m2DagNode.isIntermediateObject


#
def getMeshShapePath(nodepathString):
    m2Type = getM2Type(nodepathString)
    if m2Type == appCfg.M2TransformType:
        m2DagNode = toM2DagNode(nodepathString)
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
def isM2ObjectVisible(nodepathString):
    m2ObjectPath = toM2NodePath(nodepathString)
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
    filterM2Types = bscMethods.String.toList(filterM2Types)
    #
    if maUtils._isAppExist(groupString):
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
    nodepathString = getGeometryObjectsByGroup(groupString)


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
def setNurbsCurveBoxCreate(nodepathString, worldBoundingBox):
    if not maUtils._isAppExist(nodepathString):
        objectName = maUtils._nodeString2nodename_(nodepathString)
        nodepathString = cmds.createNode('transform', name=objectName)
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
    return setNurbsCurveShapeUpdate(nodepathString, geomData)


#
def setNurbsCurveShapeUpdate(nodepathString, geomData):
    shapeName = maUtils._nodeString2nodename_(nodepathString) + shapeLabel
    shapePath = nodepathString + '|' + shapeName
    #
    (knotsArray, degree, form), cvPointArray = geomData
    if not maUtils._isAppExist(shapePath):
        m2CurveNode = OpenMaya.MFnNurbsCurve()
        m2CurveNode.create(
            toM2PointArray(cvPointArray),
            knotsArray,
            degree,
            form,
            False,
            True,
            parent=toM2Object(nodepathString)
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
    dic = bscMtdCore.orderedDict()
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
def getNurbsSurfaceObjectMapData(nodepathString):
    m2SurfaceObject = toM2SurfaceNode(nodepathString)
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
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            nodepathString = maUtils.getObjectRelativePath(groupString, nodepathString)
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            dic[uniqueId] = nodepathString
    return dic


#
def getMeshObjectsPathData(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getMeshObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            dic[uniqueId] = nodepathString
    return dic


#
def getGeometryObjectsTransformDic(groupString, assetName):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    if nodepathStrings:
        for seq, nodepathString in enumerate(nodepathStrings):
            parentObjectPath = maUtils._toNodeParentPath(nodepathString)
            parentObjectPath = maUtils.getObjectRelativePath(groupString, parentObjectPath)
            parentObjectPath = parentObjectPath.replace(assetName, '<assetName>')
            #
            objectName = maUtils._nodeString2nodename_(nodepathString)
            objectName = objectName.replace(assetName, '<assetName>')
            #
            transformationMatrix = maObj.getObjectTransformation_(nodepathString)
            customAttrData = maAttr.getNodeUserDefAttrData(nodepathString)
            rowIndex = seq
            #
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            dic[uniqueId] = parentObjectPath, objectName, transformationMatrix, customAttrData, rowIndex
    return dic


#
def getGeometryObjectsTransformDic_(nodepathStrings, groupString, assetName=None):
    dic = bscMtdCore.orderedDict()
    #
    if nodepathStrings:
        for seq, nodepathString in enumerate(nodepathStrings):
            parentObjectPath = maUtils._toNodeParentPath(nodepathString)
            parentObjectPath = maUtils.getObjectRelativePath(groupString, parentObjectPath)
            objectName = maUtils._nodeString2nodename_(nodepathString)
            #
            if assetName is not None:
                parentObjectPath = parentObjectPath.replace(assetName, '<assetName>')
                objectName = objectName.replace(assetName, '<assetName>')
            #
            transformationMatrix = maObj.getObjectTransformation_(nodepathString)
            displayAttrData, customAttrData = maAttr.getObjectDisplayAttrData(nodepathString), maAttr.getNodeUserDefAttrData(nodepathString)
            #
            rowIndex = seq
            #
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            dic[uniqueId] = parentObjectPath, objectName, transformationMatrix, customAttrData + displayAttrData, rowIndex
    return dic


#
def getCompMeshesTransformData(groupString, assetName):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getMeshObjectsByGroup(groupString)
    if nodepathStrings:
        for seq, nodepathString in enumerate(nodepathStrings):
            parentObjectPath = maUtils._toNodeParentPath(nodepathString)
            parentObjectPath = parentObjectPath.replace(assetName, '<assetName>')
            #
            objectName = maUtils._nodeString2nodename_(nodepathString)
            objectName = objectName.replace(assetName, '<assetName>')
            #
            transformationMatrix = maObj.getObjectTransformation_(nodepathString)
            customAttrData = maAttr.getNodeUserDefAttrData(nodepathString)
            rowIndex = seq
            #
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            dic[uniqueId] = parentObjectPath, objectName, transformationMatrix, customAttrData, rowIndex
    return dic


#
def getNurbsCurveObjectsTransformData(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getObjectsByGroup(groupString, appCfg.M2NurbsCurveType)
    if nodepathStrings:
        for seq, nodepathString in enumerate(nodepathStrings):
            parentObjectPath = maUtils._toNodeParentPath(nodepathString)
            parentObjectPath = maUtils.getObjectRelativePath(groupString, parentObjectPath)
            #
            objectName = maUtils._nodeString2nodename_(nodepathString)
            #
            transformationMatrix = maObj.getObjectTransformation_(nodepathString)
            customAttrData = maAttr.getNodeUserDefAttrData(nodepathString)
            rowIndex = seq
            #
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            dic[uniqueId] = parentObjectPath, objectName, transformationMatrix, customAttrData, rowIndex
    return dic


#
def getGeometryObjectsGeometryDic(groupString):
    geomTopoDic, geomShapeDic = bscMtdCore.orderedDict(), bscMtdCore.orderedDict()
    #
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                topologyData, shapeData = getMeshObjectGeomData(nodepathString)
            elif objectType == appCfg.DEF_mya_type_nurbs_surface:
                topologyData, shapeData = getNurbsSurfaceObjectGeomData(nodepathString)
            else:
                topologyData, shapeData = getNurbsCurveObjectGeomData(nodepathString)
            #
            geomTopoDic[uniqueId], geomShapeDic[uniqueId] = topologyData, shapeData
    return geomTopoDic, geomShapeDic


#
def getGeometryObjectsGeometryDic_(nodepathStrings):
    geomTopoDic, geomShapeDic = bscMtdCore.orderedDict(), bscMtdCore.orderedDict()
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                topologyData, shapeData = getMeshObjectGeomData(nodepathString)
            elif objectType == appCfg.DEF_mya_type_nurbs_surface:
                topologyData, shapeData = getNurbsSurfaceObjectGeomData(nodepathString)
            else:
                topologyData, shapeData = getNurbsCurveObjectGeomData(nodepathString)
            #
            geomTopoDic[uniqueId], geomShapeDic[uniqueId] = topologyData, shapeData
    return geomTopoDic, geomShapeDic


#
def getMeshObjectsGeomData(groupString):
    geomTopoDic, geomShapeDic = bscMtdCore.orderedDict(), bscMtdCore.orderedDict()
    #
    nodepathStrings = getMeshObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            topologyData, shapeData = getMeshObjectGeomData(nodepathString)
            geomTopoDic[uniqueId], geomShapeDic[uniqueId] = topologyData, shapeData
    return geomTopoDic, geomShapeDic


#
def getNurbsCurveObjectsGeomData(groupString):
    geomTopoDic, geomShapeDic = bscMtdCore.orderedDict(), bscMtdCore.orderedDict()
    #
    nodepathStrings = getObjectsByGroup(groupString, appCfg.M2NurbsCurveType)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            topologyData, shapeData = getNurbsCurveObjectGeomData(nodepathString)
            geomTopoDic[uniqueId], geomShapeDic[uniqueId] = topologyData, shapeData
    return geomTopoDic, geomShapeDic


#
def getGeometryObjectsVertexNormalDic(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                vertexNormalData = getMeshObjectVertexNormal(nodepathString)
            else:
                vertexNormalData = None
            #
            dic[uniqueId] = vertexNormalData
    return dic


#
def getGeometryObjectsVertexNormalDic_(nodepathStrings):
    dic = bscMtdCore.orderedDict()
    #
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                vertexNormal = getMeshObjectVertexNormal(nodepathString)
            else:
                vertexNormal = None
            #
            dic[uniqueId] = vertexNormal
    return dic


#
def getMeshObjectsVertexNormalData(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getMeshObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            vertexNormalData = getMeshObjectVertexNormal(nodepathString)
            dic[uniqueId] = vertexNormalData
    return dic


#
def getGeometryObjectsEdgeSmoothDic(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                edgeSmoothData = getMeshObjectEdgeSmooth(nodepathString)
            else:
                edgeSmoothData = None
            #
            dic[uniqueId] = edgeSmoothData
    return dic


#
def getGeometryObjectsEdgeSmoothDic_(nodepathStrings):
    dic = bscMtdCore.orderedDict()
    #
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                edgeSmoothData = getMeshObjectEdgeSmooth(nodepathString)
            else:
                edgeSmoothData = None
            #
            dic[uniqueId] = edgeSmoothData
    return dic


#
def getCompMeshesEdgeSmoothData(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getMeshObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            edgeSmooth = getMeshObjectEdgeSmooth(nodepathString)
            dic[uniqueId] = edgeSmooth
    return dic


#
def getGeometryObjectsMapDic(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                mapData = getMeshObjectMapData(nodepathString)
            else:
                mapData = None
            #
            dic[uniqueId] = mapData
    return dic


#
def getGeometryObjectsMapDic_(nodepathStrings):
    dic = bscMtdCore.orderedDict()
    #
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                mapData = getMeshObjectMapData(nodepathString)
            else:
                mapData = None
            #
            dic[uniqueId] = mapData
    return dic


#
def getCompMeshesMapData(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getMeshObjectsByGroup(groupString)
    if nodepathStrings:
        for nodepathString in nodepathStrings:
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            mapData = getMeshObjectMapData(nodepathString)
            dic[uniqueId] = mapData
    return dic


#
def getCompMeshesAttributeData(meshObjStrs):
    dic = bscMtdCore.orderedDict()
    #
    if meshObjStrs:
        for nodepathString in meshObjStrs:
            meshShape = getMeshShapePath(nodepathString)
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
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
    groupName = maUtils._nodeString2nodename_(groupString)
    #
    relativePath = '|' + groupName + '|'.join(('|'.join(objectPath.split(groupString)[1:])).split('|'))
    if ':' in relativePath:
        namespace = ':'.join(objectPath.split('|')[-1].split(':')[:-1]) + ':'
        #
        relativePath = ('|' + groupName + '|'.join(('|'.join(objectPath.split(groupString)[1:])).split('|'))).replace(namespace, none)
    return datHash.getStrHashKey(relativePath)


#
def getGeometryObjectsPathInfo(nodepathStrings, groupString):
    lis = []
    for nodepathString in nodepathStrings:
        pathInfo = getObjectPathInfo(nodepathString, groupString)
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
def getGeometryObjectGeomInfo(nodepathString, roundLimit=8):
    objectType = maUtils._getNodeShapeCategoryString(nodepathString)
    if objectType == appCfg.DEF_mya_type_mesh:
        return getMeshObjectGeomInfo(nodepathString, roundLimit)
    elif objectType == appCfg.DEF_mya_type_nurbs_surface:
        return getNurbsSurfaceObjectGeomInfo(nodepathString, roundLimit)
    elif objectType == appCfg.DEF_mya_type_nurbs_curve:
        return getNurbsCurveObjectGeomInfo(nodepathString, roundLimit)


#
def getMeshObjectGeomInfo(nodepathString, roundLimit=8):
    return getMeshObjectGeomTopoInfo(nodepathString), getMeshObjectGeomShapeInfo(nodepathString, roundLimit)


#
def getNurbsSurfaceObjectGeomInfo(nodepathString, roundLimit=8):
    topoData, shapeData = getNurbsSurfaceObjectGeomData(nodepathString)
    return datHash.getNumHashKey(topoData), datHash.getFloatHashKey(shapeData, roundLimit)


#
def getNurbsCurveObjectGeomInfo(nodepathString, roundLimit=8):
    topoData, shapeData = getNurbsCurveObjectGeomData(nodepathString)
    return datHash.getNumHashKey(topoData), datHash.getFloatHashKey(shapeData, roundLimit)


#
def getGeometryObjectMapInfo(nodepathString, roundLimit=8):
    objectType = maUtils._getNodeShapeCategoryString(nodepathString)
    if objectType == appCfg.DEF_mya_type_mesh:
        return getMeshObjectMapInfo(nodepathString, roundLimit)
    elif objectType == appCfg.DEF_mya_type_nurbs_surface:
        return None, None
    elif objectType == appCfg.DEF_mya_type_nurbs_curve:
        return None, None


#
def getMeshObjectMapInfo(nodepathString, roundLimit=8):
    return getMeshObjectMapTopoInfo(nodepathString), getMeshObjectMapShapeInfo(nodepathString, roundLimit)


#
def getMeshObjectGeomTopoInfo(meshObjectString):
    infoData = getMeshObjectGeomTopoInfoData(meshObjectString)
    return datHash.getIntHashKey(infoData)


#
def getGeometryObjectsGeomInfo(nodepathStrings):
    geomTopoLis, geomShapeLis = [], []
    for nodepathString in nodepathStrings:
        geomTopoInfo, geomShapeInfo = getGeometryObjectGeomInfo(nodepathString)
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
def getGeometryObjectsMapInfo(nodepathStrings):
    mapTopoLis, mapShapeLis = [], []
    for nodepathString in nodepathStrings:
        mapTopoInfo, mapShapeInfo = getGeometryObjectMapInfo(nodepathString)
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
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    #
    pathInfo = getGeometryObjectsPathInfo(nodepathStrings, groupString)
    geomTopoInfo, geomShapeInfo = getGeometryObjectsGeomInfo(nodepathStrings)
    mapTopoInfo, mapShapeInfo = getGeometryObjectsMapInfo(nodepathStrings)
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
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    if nodepathStrings:
        # View Progress
        progressExplain = u'''Read Nde_Geometry Information'''
        maxValue = len(nodepathStrings)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for nodepathString in nodepathStrings:
            progressBar.update()
            #
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            #
            dic[uniqueId] = \
                (getObjectPathInfo(nodepathString, groupString), ) + \
                getGeometryObjectGeomInfo(nodepathString) + \
                getGeometryObjectMapInfo(nodepathString)
    #
    return dic


#
def getGeometryObjectsInfoDic_(nodepathStrings, groupString):
    dic = bscMtdCore.orderedDict()
    #
    for nodepathString in nodepathStrings:
        uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
        #
        pathInfo = getObjectPathInfo(nodepathString, groupString)
        geomTopoInfo, geomShapeInfo = getGeometryObjectGeomInfo(nodepathString)
        mapTopoInfo, mapShapeInfo = getGeometryObjectMapInfo(nodepathString)
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
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getMeshObjectsByGroup(groupString)
    if nodepathStrings:
        # View Progress
        progressExplain = u'''Read Mesh Information'''
        maxValue = len(nodepathStrings)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for nodepathString in nodepathStrings:
            progressBar.update()
            #
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            #
            dic[uniqueId] = (
                # Path
                getObjectPathInfo(nodepathString, groupString),
                # Nde_Geometry
                getMeshObjectGeomTopoInfo(nodepathString),
                getMeshObjectGeomShapeInfo(nodepathString),
                # Map
                getMeshObjectMapTopoInfo(nodepathString),
                getMeshObjectMapShapeInfo(nodepathString)
            )
    return dic


#
def getNurbsCurveObjectsInfoData(groupString):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getObjectsByGroup(groupString, appCfg.M2NurbsCurveType)
    if nodepathStrings:
        # View Progress
        progressExplain = u'''Read Nurbs Curve Information'''
        maxValue = len(nodepathStrings)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        #
        for nodepathString in nodepathStrings:
            progressBar.update()
            uniqueId = maUuid._getNodeUniqueIdString(nodepathString)
            #
            dic[uniqueId] = (
                # Path
                getObjectPathInfo(nodepathString, groupString),
                # Nde_Geometry
            ) + tuple(getNurbsCurveObjectGeomInfo(nodepathString))
    return dic


#
def getScGeometryObjectsInfoDic_(groupString, pathKey, searchRoot):
    dic = bscMtdCore.orderedDict()
    #
    nodepathStrings = getGeometryObjectsByGroup(groupString)
    if nodepathStrings:
        # View Progress
        progressExplain = u'''Read Nde_Geometry Information'''
        maxValue = len(nodepathStrings)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for nodepathString in nodepathStrings:
            progressBar.update()
            if searchRoot in nodepathString:
                key = maUtils._nodeString2nodename_(nodepathString)
                #
                pathInfo = getObjectPathInfo(nodepathString, pathKey)
                geomTopoInfo, geomShapeInfo = getGeometryObjectGeomInfo(nodepathString)
                mapTopoInfo, mapShapeInfo = getGeometryObjectMapInfo(nodepathString)
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
def setCreateGeometryObjectShape(nodepathString, geomData, shapeName=none):
    if geomData:
        if maUtils._isAppExist(nodepathString):
            if not shapeName:
                shapeName = maUtils._nodeString2nodename_(nodepathString) + shapeLabel
            objectShape = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
            if not maUtils._isAppExist(objectShape):
                geomTopData, geomShapeData = geomData
                if len(geomTopData) == 2:
                    m2MeshObject = OpenMaya.MFnMesh()
                    nSideArray, vertexIdArray = geomTopData
                    pointArray = geomShapeData
                    m2MeshObject.create(
                        toM2PointArray(pointArray),
                        nSideArray,
                        vertexIdArray,
                        parent=toM2Object(nodepathString)
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
                            parent=toM2Object(nodepathString)
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
                            parent=toM2Object(nodepathString)
                        )
                        #
                        m2SurfaceObject.setName(shapeName)


#
def setCreateMeshObjectShape(nodepathString, geomData, shapeName=none):
    if geomData:
        if maUtils._isAppExist(nodepathString):
            if not shapeName:
                shapeName = maUtils._nodeString2nodename_(nodepathString) + shapeLabel
            #
            shapePath = nodepathString + '|' + shapeName
            #
            if not maUtils._isAppExist(shapePath):
                m2MeshObject = OpenMaya.MFnMesh()
                (nSideArray, vertexIdArray), pointArray = geomData
                m2MeshObject.create(
                    toM2PointArray(pointArray),
                    nSideArray,
                    vertexIdArray,
                    parent=toM2Object(nodepathString)
                )
                #
                m2MeshObject.setName(shapeName)


#
def setCreateNurbsSurfaceObjectShape(nodepathString, geomData, shapeName=None):
    if geomData:
        if maUtils._isAppExist(nodepathString):
            if not shapeName:
                shapeName = maUtils._nodeString2nodename_(nodepathString) + shapeLabel
            #
            shapePath = nodepathString + '|' + shapeName
            #
            if not maUtils._isAppExist(shapePath):
                m2SurfaceObject = OpenMaya.MFnNurbsSurface()
                ((uKnotsArray, vKnotsArray), (uDegree, vDegree), (uForm, vForm)), cvPointArray = geomData
                m2SurfaceObject.create(
                    toM2PointArray(cvPointArray),
                    uKnotsArray, vKnotsArray,
                    uDegree, vDegree,
                    uForm, vForm,
                    True,
                    parent=toM2Object(nodepathString)
                )
                #
                m2SurfaceObject.setName(shapeName)


#
def setNurbsCurveShapeCreate(nodepathString, geomData, shapeName=None):
    if geomData:
        if not shapeName:
            shapeName = maUtils._nodeString2nodename_(nodepathString) + shapeLabel
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
            parent=toM2Object(nodepathString)
        )
        #
        m2CurveNode.setName(shapeName)


#
def setCreateObjectGraphGeometrySub(objectData, lockTransform=False):
    shapeName, shapeType, transformData, geomData, mapData = objectData
    nodepathString = maObj.setCreateObjectTransformPath(transformData, lockTransform)
    if shapeType == appCfg.DEF_mya_type_mesh:
        setCreateMeshObjectShape(nodepathString, geomData, shapeName)
        setCreateMeshObjectMap(nodepathString, mapData)
        maUtils.setObjectDefaultShadingEngine(nodepathString)
    elif shapeType == appCfg.DEF_mya_type_nurbs_surface:
        setCreateNurbsSurfaceObjectShape(nodepathString, geomData, shapeName)
        maUtils.setObjectDefaultShadingEngine(nodepathString)
    elif shapeType == appCfg.DEF_mya_type_nurbs_curve:
        setNurbsCurveShapeCreate(nodepathString, geomData, shapeName)


#
def setCreateObjectsTransform(transformDataDic, assetName, lockTransform):
    if transformDataDic:
        rowIndexLis = []
        #
        dic = bscMtdCore.orderedDict()
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
                if not maUtils._isAppExist(objectLocalPath):
                    if not maUtils._isAppExist(parentLocalPath):
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
                shapeName = maUtils.getAttrDatum(objectPath, prsConfigure.Product.DEF_key_attribute_shapename)
                setCreateGeometryObjectShape(objectPath, (topologyData, shapeData), shapeName)


#
def setCreateMeshObjectsGeometry(dataDics):
    geomTopoDic, geomShapeDic = dataDics
    if geomTopoDic and geomShapeDic:
        for uniqueId, topologyData in geomTopoDic.items():
            shapeData = geomShapeDic[uniqueId]
            nodepathStrings = maUuid.getObjects(uniqueId)
            if nodepathStrings:
                nodepathString = nodepathStrings[0]
                setCreateMeshObjectShape(nodepathString, (topologyData, shapeData))


#
def setCreateNurbsCurveObjectsGeometry(dataDics):
    geomTopoDic, geomShapeDic = dataDics
    if geomTopoDic and geomShapeDic:
        for uniqueId, topologyData in geomTopoDic.items():
            shapeData = geomShapeDic[uniqueId]
            nodepathStrings = maUuid.getObjects(uniqueId)
            if nodepathStrings:
                nodepathString = nodepathStrings[0]
                setNurbsCurveShapeCreate(nodepathString, (topologyData, shapeData))


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
                nodepathStrings = maUuid.getObjects(uniqueId)
                if nodepathStrings:
                    nodepathString = nodepathStrings[0]
                    objectType = maUtils._getNodeShapeCategoryString(nodepathString)
                    if objectType == appCfg.DEF_mya_type_mesh:
                        setCreateMeshObjectEdgeSmooth(nodepathString, data)


#
def setCreateCompMeshesEdgeSmooth(dataDic):
    if dataDic:
        for uniqueId, data in dataDic.items():
            if data:
                nodepathStrings = maUuid.getObjects(uniqueId)
                if nodepathStrings:
                    nodepathString = nodepathStrings[0]
                    setCreateMeshObjectEdgeSmooth(nodepathString, data)


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
            nodepathStrings = maUuid.getObjects(uniqueId)
            if nodepathStrings:
                nodepathString = nodepathStrings[0]
                objectType = maUtils._getNodeShapeCategoryString(nodepathString)
                if objectType == appCfg.DEF_mya_type_mesh:
                    setCreateMeshObjectMap(nodepathString, mapData)


#
def setCreateCompMeshesMap(dataDic):
    if dataDic:
        for uniqueId, mapData in dataDic.items():
            nodepathStrings = maUuid.getObjects(uniqueId)
            if nodepathStrings:
                nodepathString = nodepathStrings[0]
                setCreateMeshObjectMap(nodepathString, mapData)


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
    if maUtils._isAppExist(meshObjectString):
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
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
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
        nodepathString = maUuid.getObject(uniqueId)
        if nodepathString:
            objectType = maUtils._getNodeShapeCategoryString(nodepathString)
            if objectType == appCfg.DEF_mya_type_mesh:
                maUtils.setObjectDefaultShadingEngine(nodepathString)
            elif objectType == appCfg.DEF_mya_type_nurbs_surface:
                maUtils.setObjectDefaultShadingEngine(nodepathString)


# Get Poly Mesh Evaluate ( Method )
def getMeshObjectEvaluate(nodepathStrings, vertex, edge, face, triangle, uvcoord, area, worldArea, shell, boundingBox, showMode):
    # Dict { <Evaluate Name>: <Evaluate Data> }
    dic = bscMtdCore.orderedDict()
    used = [vertex, edge, face, triangle, uvcoord, area, worldArea, shell, boundingBox]
    # View Progress
    explain = '''Read Mesh Evaluate Data'''
    maxValue = sum(used)
    progressBar = bscObjects.ProgressWindow(explain, maxValue)
    # >>>> 01
    if vertex:
        progressBar.update('Vertex')
        dic['vertex'] = cmds.polyEvaluate(nodepathStrings, vertex=1)
    # >>>> 02
    if edge:
        progressBar.update('Edge')
        dic['edge'] = cmds.polyEvaluate(nodepathStrings, edge=1)
    # >>>> 03
    if face:
        progressBar.update('Face')
        dic['face'] = cmds.polyEvaluate(nodepathStrings, face=1)
    # >>>> 04
    if triangle:
        progressBar.update('Triangle')
        dic['triangle'] = cmds.polyEvaluate(nodepathStrings, triangle=1)
    # >>>> 05
    if uvcoord:
        progressBar.update('UV')
        dic['uvcoord'] = cmds.polyEvaluate(nodepathStrings, uvcoord=1)
    # >>>> 06
    if area:
        progressBar.update('Area')
        dic['area'] = cmds.polyEvaluate(nodepathStrings, area=1)
    # >>>> 07
    if worldArea:
        progressBar.update('World Area')
        dic['worldArea'] = cmds.polyEvaluate(nodepathStrings, worldArea=1)
    # >>>> 08
    if shell:
        progressBar.update('Shell')
        dic['shell'] = cmds.polyEvaluate(nodepathStrings, shell=1)
    # >>>> 09
    if boundingBox:
        progressBar.update('Bounding Box')
        dic['boundingBox'] = cmds.polyEvaluate(nodepathStrings, boundingBox=1)
    return dic


# Get Poly Meshes's Evaluate ( Data )
def getMeshObjectsEvaluateDic(nodepathStrings, showMode=0):
    # Dict { <Poly Mesh> :
    #        List [ <Evaluate Info> ] }
    dic = bscMtdCore.orderedDict()
    if nodepathStrings:
        count = len(nodepathStrings)
        data = getMeshObjectEvaluate(
            nodepathStrings,
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
    dic = bscMtdCore.orderedDict()
    #
    info = getGeometryObjectsInfo(groupString)
    for seq, i in enumerate(infoKeyLis):
        dic[i] = info[seq]
    return dic


#
def getGeometryObjectsConstantDic_(groupString):
    dic = bscMtdCore.orderedDict()
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
def getMeshReferenceObject(nodepathString):
    shapePath = maUtils._dcc_getNodShapeNodepathStr(nodepathString)
    attr = shapePath + '.referenceObject'
    guessData = maUtils.getInputNodeLisByAttr(attr)
    if guessData:
        return guessData[0]