# encoding=utf-8
import collections
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxMaya.command import maGeom, maInfo
#
none = ''


#
def getBBoxMPointArray(m2BoundingBox):
    maxiM2Point = m2BoundingBox.max
    miniMPoint = m2BoundingBox.min
    return miniMPoint, maxiM2Point


#
def getBBox(nodepathString):
    MObject = maGeom.toM2DagNode(nodepathString)
    m2BoundingBox = MObject.boundingBox
    bBoxMPointArray = getBBoxMPointArray(m2BoundingBox)
    return maGeom.getPointArray(bBoxMPointArray)


#
def getMeshBBox(mesh):
    m2MeshObject = maGeom.toM2MeshNode(mesh)
    m2BoundingBox = m2MeshObject.boundingBox
    bBoxMPointArray = getBBoxMPointArray(m2BoundingBox)
    return maGeom.getPointArray(bBoxMPointArray)


#
def getMeshPointArray(mesh):
    m2MeshObject = maGeom.toM2MeshNode(mesh)
    m2PointArray = m2MeshObject.getPoints()
    return maGeom.getPointArray(m2PointArray)


#
def getMeshesPointArray(meshObjects, existsOnly=True):
    lis = []
    for mesh in meshObjects:
        pointArray = []
        if not existsOnly:
            pointArray = getMeshPointArray(mesh)
        if existsOnly:
            exists = 0
            if cmds.getAttr(mesh + '.visibility') == 1:
                exists += 1
            transforms = cmds.listRelatives(mesh, parent=1, fullPath=1)
            if transforms:
                transform = transforms[0]
                if cmds.getAttr(transform + '.visibility') == 1:
                    exists += 1
            if exists == 2:
                pointArray = getMeshPointArray(mesh)
        lis.extend(pointArray)
    return lis


#
def getPointArrayRoundReduce(pointArray, roundCount=3):
    lis = []
    for point in pointArray:
        x, y, z = point
        point = round(x, roundCount), round(y, roundCount), round(z, roundCount)
        if not point in lis:
            lis.append(point)
    return lis


#
def getBBoxMap(boundingBox):
    mini, maxi = boundingBox
    _x, _y, _z = mini
    x, y, z = maxi
    return _x, _y, _z, x, y, z


# Reduce Bounding Box Map to Cube
def getBBoxMapReduce(boundingBoxMap):
    _x, _y, _z, x, y, z = boundingBoxMap
    mini = min(_x, _y, _z)
    maxi = max(x, y, z)
    return mini, mini, mini, maxi, maxi, maxi


#
def isPointInBoundingBox(point, boundingBoxMap):
    px, py, pz = point
    _bx, _by, _bz, bx, by, bz = boundingBoxMap
    if _bx < px < bx and _by < py < by and _bz < pz < bz:
        return True


#
def getPointArrayInBBox(pointArray, boundingBoxMap):
    lis = []
    for point in pointArray:
        if isPointInBoundingBox(point, boundingBoxMap):
            lis.append(point)
    return lis


#
def getOcBranchLis(boundingBoxMap):
    _x, _y, _z, x, y, z = boundingBoxMap
    mx = (x + _x) / 2
    my = (y + _y) / 2
    mz = (z + _z) / 2
    b0 = mx, my, _z, x, y, mz
    b1 = _x, my, _z, mx, y, mz
    b2 = mx, _y, _z, x, my, mz
    b3 = _x, _y, _z, mx, my, mz
    b4 = mx, my, mz, x, y, z
    b5 = _x, my, mz, mx, y, z
    b6 = mx, _y, mz, x, my, z
    b7 = _x, _y, mz, mx, my, z
    return b0, b1, b2, b3, b4, b5, b6, b7


#
def getMeshesBoxData(root, existsOnly=True):
    # Sub Method
    def getBranch(pointArray_, boundingBoxMap, depth):
        if depth > 0:
            depth = depth - 1
            pointArrayInBBox = getPointArrayInBBox(pointArray_, boundingBoxMap)
            if pointArrayInBBox:
                lis.remove(boundingBoxMap)
                branches = getOcBranchLis(boundingBoxMap)
                for branch in branches:
                    if getPointArrayInBBox(pointArrayInBBox, branch):
                        lis.append(branch)
                    getBranch(pointArrayInBBox, branch, depth)
    #
    meshObjects = maGeom.getMeshObjectsByGroup(root)
    pointArray = getMeshesPointArray(meshObjects, existsOnly)
    maxiBoundingBox = getBBox(root)
    maxBoundingBoxMap = getBBoxMap(maxiBoundingBox)
    maxiBoundingBoxReduce = getBBoxMapReduce(maxBoundingBoxMap)
    lis = [maxiBoundingBoxReduce]
    #
    maxDepth = len(pointArray) / 4096 + 1
    maxDepth = [6, maxDepth][maxDepth < 6]
    getBranch(pointArray, maxiBoundingBoxReduce, maxDepth)
    return lis


#
def getBox(boundingBoxMap):
    _x, _y, _z, x, y, z = boundingBoxMap
    xValue = x - _x
    yValue = y - _y
    zValue = z - _z
    xPosition = x + _x
    yPosition = y + _y
    zPosition = z + _z
    return xValue / 2, yValue / 2, zValue / 2, xPosition / 2, yPosition / 2, zPosition / 2


#
def boxDic(boundingBoxMap):
    x, y, z, X, Y, Z = getBox(boundingBoxMap)
    dic = collections.OrderedDict()
    dic['x'] = dict(
        yz=[('.localPosition', X, Y+y, Z+z), ('.localScale', x, 0, 0)],
        _yz=[('.localPosition', X, Y-y, Z+z), ('.localScale', x, 0, 0)],
        _y_z=[('.localPosition', X, Y-y, Z-z), ('.localScale', x, 0, 0)],
        y_z=[('.localPosition', X, Y+y, Z-z), ('.localScale', x, 0, 0)]
    )
    dic['y'] = dict(
        xz=[('.localPosition', X+x, Y, Z+z), ('.localScale', 0, y, 0)],
        _xz=[('.localPosition', X+x, Y, Z-z), ('.localScale', 0, y, 0)],
        _x_z=[('.localPosition', X-x, Y, Z-z), ('.localScale', 0, y, 0)],
        x_z=[('.localPosition', X-x, Y, Z+z), ('.localScale', 0, y, 0)]
    )
    dic['z'] = dict(
        xy=[('.localPosition', X+x, Y+y, Z), ('.localScale', 0, 0, z)],
        _xy=[('.localPosition', X-x, Y+y, Z), ('.localScale', 0, 0, z)],
        _x_y=[('.localPosition', X-x, Y-y, Z), ('.localScale', 0, 0, z)],
        x_y=[('.localPosition', X+x, Y-y, Z), ('.localScale', 0, 0, z)]
    )
    return dic


# Create Boxes
def spaceBoxes(boundingBoxMapArray):
    for seq, boundingBoxMap in enumerate(boundingBoxMapArray):
        data = boxDic(boundingBoxMap)
        box = 'box' + '_' + str(seq).zfill(4)
        if cmds.objExists(box):
            cmds.delete(box)
        if not cmds.objExists(box):
            cmds.createNode('transform', name=box)
            for k, v in data.items():
                for ik, iv in v.items():
                    border = box + ik
                    cmds.createNode('locator', name=border, parent=box)
                    cmds.setAttr(border + iv[0][0], iv[0][1], iv[0][2], iv[0][3])
                    cmds.setAttr(border + iv[1][0], iv[1][1], iv[1][2], iv[1][3])


#
def getPolyCubeData(boundingBoxMap):
    _x, _y, _z, x, y, z = boundingBoxMap
    w = x - _x
    h = y - _y
    d = z - _z
    tx = (x + _x) / 2
    ty = (y + _y) / 2
    tz = (z + _z) / 2
    return w, h, d, tx, ty, tz


#
def setPolyCube(boundingBoxMapArray, group=none):
    cubeArray = []
    for seq, boundingBoxMap in enumerate(boundingBoxMapArray):
        w, h, d, tx, ty, tz = getPolyCubeData(boundingBoxMap)
        cube = 'box' + '_' + str(seq).zfill(4)
        cmds.polyCube(name=cube, w=w, h=h, d=d)
        cubeArray.append(cube)
        cmds.setAttr(cube + '.translate', tx, ty, tz)
    #
    if group:
        cmds.group(empty=1, name=group)
        cmds.parent(cubeArray, group)


#
def setMeshesBox(sourceGroup, targetGroup=none, existsOnly=True):
    boundingBoxMapArray = getMeshesBoxData(sourceGroup, existsOnly)
    boxArray = []
    for seq, boundingBoxMap in enumerate(boundingBoxMapArray):
        w, h, d, tx, ty, tz = getPolyCubeData(boundingBoxMap)
        box = 'box' + '_' + str(seq).zfill(4)
        cmds.polyCube(name=box, w=w, h=h, d=d)
        boxArray.append(box)
        cmds.setAttr(box + '.translate', tx, ty, tz)
    #
    if targetGroup:
        cmds.group(empty=1, name=targetGroup)
        cmds.parent(boxArray, targetGroup)


#
def getObjectBBoxInfo(nodepathString, roundLimit=6):
    bBox = getBBox(nodepathString)
    infoData = [j for i in bBox for j in i]
    return maInfo.getFloatHashKey(infoData, roundLimit)