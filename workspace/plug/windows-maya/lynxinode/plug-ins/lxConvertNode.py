# encoding=utf-8
import sys
#
import math
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
# noinspection PyUnresolvedReferences
import maya.api.OpenMaya as OpenMaya
# noinspection PyUnresolvedReferences
import maya.api.OpenMayaUI as OpenMayaUI


# Use 2.0 API
def maya_useNewAPI():
    pass


# Command
class curveToMeshCmd(object):
    def __init__(self, *args):
        (
            curveObject, meshCreate,
            uniformEnable,
            vDivision, uDivision,
            width, widthExtra,
            spin, spinExtra,
            twist, taper, arch, archAttachCurveEnable,
            minPercent, maxPercent,
            sample,
            smoothDepth,
            angleOffset
        ) = args
        # noinspection PyArgumentList
        self._mCurve = OpenMaya.MFnNurbsCurve(curveObject)
        self._mMeshCreate = meshCreate
        #
        self._vDivision = vDivision - 1
        self._uDivision = uDivision - 1
        #
        self._uiWidth = width
        self._widthExtra = widthExtra
        self._spin = spin
        self._spinExtra = spinExtra
        #
        self._twist = twist
        self._taper = taper
        self._arch = arch
        self._archAttachCurveEnable = archAttachCurveEnable
        #
        self._sample = sample
        self._smoothDepth = smoothDepth
        #
        self._angleOffset = angleOffset
        # Clamp in 0.1
        self._minPercent = max(min(minPercent, minPercent - .1, 1.0 - .1), 0.0)
        self._maxPercent = max(maxPercent, min(minPercent + .1, 1.0), .1)
        #
        self._uniformEnable = uniformEnable
        #
        paramRange = self._mCurve.knotDomain
        #
        self._minParam = paramRange[0]
        self._maxParam = paramRange[1]
        #
        self._length = self._mCurve.length()
        #
        self._searchCount = int(self._vDivision*self._sample)
        #
        step = int(math.log(self._vDivision, 2) / 2)
        # Minimum Use 1
        self._vStep = max(step, 1)
        #
        self._updateBasicData()
        self._updateReduceData()
        self._updateCreateData()
    @staticmethod
    def _mapRangeValue(range1, range2, value1):
        assert isinstance(range1, tuple) or isinstance(range1, list), 'Argument Error, "range1" Must "tuple" or "list".'
        assert isinstance(range2, tuple) or isinstance(range2, list), 'Argument Error, "range2" Must "tuple" or "list".'
        #
        min1, max1 = range1
        min2, max2 = range2
        #
        percent = float(value1 - min1)/(max1 - min1)
        #
        value2 = (max2 - min2) * percent + min2
        return value2
    #
    def _updateByPercentAt(self, index, percent):
        if self._uniformEnable is True:
            length = self._mapRangeValue((0, 1), (0, self._length), percent)
            param = self._mCurve.findParamFromLength(length)
        else:
            param = self._mapRangeValue((0, 1), (self._minParam, self._maxParam), percent)
        #
        v = OpenMaya.MVector()
        #
        xAxis = v.kXaxisVector
        xAxis_ = v.kXnegAxisVector
        #
        yAxis = v.kYaxisVector
        yAxis_ = v.kYnegAxisVector
        #
        zAxis = v.kZaxisVector
        zAxis_ = v.kZnegAxisVector
        #
        point, tangent = self._mCurve.getDerivativesAtParam(param, 4)
        tangent = tangent.normalize()
        #
        if index == 0:
            if tangent.isEquivalent(yAxis) or tangent.isEquivalent(yAxis_):
                axis = xAxis
            else:
                axis = yAxis
            # Vector Multiplication Cross
            xNormal = tangent.__rxor__(axis)
            yNormal = xNormal.__rxor__(tangent)
        else:
            quaternion = self._tangents[index - 1].rotateTo(tangent)
            #
            xNormal = self._xNormals[index - 1]
            xNormal = xNormal.rotateBy(quaternion)
            #
            yNormal = self._yNormals[index - 1]
            yNormal = yNormal.rotateBy(quaternion)
        #
        self._vPercents[index] = percent
        #
        self._points[index] = point
        self._tangents[index] = tangent
        #
        self._xNormals[index] = xNormal.normalize()
        self._yNormals[index] = yNormal.normalize()
    #
    def _updateBasicData(self):
        maxCount = self._searchCount + 1
        #
        self._vPercents = [None]*maxCount
        #
        self._points = [None]*maxCount
        self._tangents = [None]*maxCount
        #
        self._xNormals = [None]*maxCount
        self._yNormals = [None]*maxCount
        #
        for seq in range(maxCount):
            if seq == 0:
                percent = self._minPercent
            elif seq == self._searchCount:
                percent = self._maxPercent
            else:
                percent = self._mapRangeValue((0, maxCount), (self._minPercent, self._maxPercent), seq)
            #
            self._updateByPercentAt(seq, percent)
    #
    def _updateAngle(self):
        # Angels
        self._angles = []
        self._angleDic = {}
        if self._tangents:
            for seq, t in enumerate(self._tangents):
                curPercent = self._vPercents[seq]
                #
                angleOffset = self._angleOffset.getValueAtPosition(curPercent)
                angleMult = 1 + (angleOffset - .5) * 10.0
                #
                preSeq = seq - 1
                if preSeq <= 0:
                    preSeq = 0
                #
                nexSeq = seq + 1
                if nexSeq >= self._searchCount:
                    nexSeq = self._searchCount
                #
                preTangent = self._tangents[preSeq]
                nexTangent = self._tangents[nexSeq]
                #
                preAngle = t.angle(preTangent)
                nexAngle = t.angle(nexTangent)
                #
                angle = sum([preAngle, nexAngle]) / 2.0 * angleMult
                # Must Round to .000x
                angle = round(angle, 3)
                #
                self._angles.append(angle)
                self._angleDic.setdefault(angle, []).append(seq)
    #
    def _updateAngleSortLis(self):
        self._seqSortLis = []
        if self._angleDic:
            angles = self._angleDic.keys()
            angles.sort()
            for a in angles:
                seqs = self._angleDic[a]
                self._seqSortLis.extend(seqs)
    #
    def _updateReduceData(self):
        def updateBranch():
            self._filterSeqs = []
            #
            self._updateAngle()
            self._updateAngleSortLis()
            #
            if self._angles:
                for n in range(rangeCount):
                    seq = n + 1
                    #
                    curPercent = self._vPercents[seq]
                    #
                    preSeq = seq - span
                    if preSeq <= 0:
                        preSeq = 0
                    prePercent = self._vPercents[preSeq]
                    #
                    nexSeq = seq + span
                    if nexSeq >= self._searchCount:
                        nexSeq = self._searchCount
                    nexPercent = self._vPercents[nexSeq]
                    # Current Angle
                    curAngle = self._angles[seq]
                    #
                    preAngles = []
                    nexAngles = []
                    for sn in range(span):
                        subSeq = sn + 1
                        # Previous
                        preAngleSeq = seq - subSeq
                        if preAngleSeq <= minSeq:
                            da = (self._angles[minSeq + 1] - self._angles[minSeq])*subSeq
                            preAngles.append(self._angles[minSeq] + da)
                        else:
                            preAngles.append(self._angles[preAngleSeq])
                        # Next
                        nexAngleSeq = seq + subSeq
                        if nexAngleSeq >= maxSeq:
                            da = (self._angles[maxSeq] - self._angles[maxSeq - 1])*subSeq
                            preAngles.append(self._angles[maxSeq] + da)
                        else:
                            nexAngles.append(self._angles[nexAngleSeq])
                    #
                    preAngle = sum(preAngles) / span
                    nexAngle = sum(nexAngles) / span
                    #
                    angleSum = sum([preAngle, curAngle, nexAngle])
                    #
                    if angleSum > 0:
                        preAnglePercent = (preAngle + curAngle) / angleSum
                        nexAnglePercent = (curAngle + nexAngle) / angleSum
                        #
                        dAnglePercent = nexAnglePercent - preAnglePercent
                    else:
                        dAnglePercent = 0.0
                    #
                    percentRange = nexPercent - prePercent
                    dPercent = percentRange / 2.0
                    #
                    minPercent = 1.0/(self._vDivision*10.0)
                    #
                    newPercent = (curPercent + dPercent*dAnglePercent)
                    # Clamp Percent
                    newPercent = max(min(newPercent, nexPercent - minPercent), prePercent + minPercent)
                    #
                    self._updateByPercentAt(seq, newPercent)
        #
        def updateFilterSeq():
            for n in range(rangeCount):
                seq = n + 1
                #
                if seq % self._sample == 0:
                    self._filterSeqs.append(seq)
            #
            self._filterSeqs.insert(0, 0)
            self._filterSeqs.append(self._searchCount)
            self._filterSeqs.sort()
        #
        self._filterSeqs = []
        #
        span = self._sample
        #
        minSeq = 0
        maxSeq = self._searchCount
        rangeCount = self._searchCount - 2
        #
        for i in range(self._smoothDepth):
            updateBranch()
        #
        updateFilterSeq()
    #
    def _updateCreateData(self):
        def step01():
            l = [0, 1, 2 + uCount, 1 + uCount]
            for v in range(vCount):
                for u in range(uCount):
                    self._nSideArray.append(4)
                    if u == 0:
                        l_ = [(i + v*(uCount + 1)) for i in l]
                    else:
                        l_ = [(i + v*(uCount + 1) + u) for i in l]
                    #
                    self._vertexIdArray.extend(l_)
        #
        def step02():
            if (uCount + 1) % 2:
                m = int((uCount + 1) / 2)
            else:
                m = None
            #
            c = float(uCount) / 2.0
            #
            for v in range(vCount + 1):
                seq = v
                for u in range(uCount + 1):
                    if seq == 0:
                        rSeq = 0
                    elif seq == self._vDivision:
                        rSeq = self._searchCount
                    else:
                        rSeq = self._filterSeqs[seq]
                    #
                    point = self._points[rSeq]
                    tangent = self._tangents[rSeq]
                    sideVector = self._xNormals[rSeq]
                    midVector = self._yNormals[rSeq]
                    #
                    vPercent = self._vPercents[rSeq]
                    uPercent = float(abs(u - c)) / float(c)
                    #
                    widthExtra = self._widthExtra.getValueAtPosition(vPercent)
                    spinExtra = self._spinExtra.getValueAtPosition(vPercent)
                    #
                    vector = sideVector*(width*widthExtra*2)/2 + sideVector*((taper - 1)*vPercent)*width/2
                    #
                    p_ = OpenMaya.MPoint()
                    if u == 0 or u == uCount:
                        v_ = vector
                    else:
                        if u == m:
                            # noinspection PyArgumentList
                            v_ = OpenMaya.MVector(0, 0, 0)
                        else:
                            v_ = uPercent*vector
                    #
                    archRadians = math.radians(uPercent*90*arch)/2
                    if u < c:
                        archRadians = -math.radians(uPercent*90*arch)/2
                        v_ /= -1
                    # Arch
                    rotArch = OpenMaya.MQuaternion()
                    # noinspection PyArgumentList
                    rotArch.setValue(
                        OpenMaya.MVector(tangent.x, tangent.y, tangent.z),
                        archRadians
                    )
                    v_ = v_.rotateBy(rotArch)
                    #
                    if not archAttachCurveEnable:
                        v_ -= midVector*arch*(math.sin(math.radians(45)))*width/2
                    # Spin + Spin Extra +  Twist
                    rotSpin = OpenMaya.MQuaternion()
                    # noinspection PyArgumentList
                    rotSpin.setValue(
                        OpenMaya.MVector(tangent.x, tangent.y, tangent.z),
                        math.radians(spin) + math.radians(spinExtra * 360) + math.radians(twist * vPercent)
                    )
                    v_ = v_.rotateBy(rotSpin)
                    #
                    p_.x, p_.y, p_.z = point.x + v_.x, point.y + v_.y, point.z + v_.z
                    #
                    self._pointArray.append(p_)
                    #
                    if u == 0:
                        self._uArray.append(1.0)
                    elif u == uCount:
                        self._uArray.append(0.0)
                    else:
                        if u == c:
                            self._uArray.append(0.5)
                        elif c < u:
                            self._uArray.append(.5 - uPercent/2)
                        elif u < c:
                            self._uArray.append(.5 + uPercent/2)
                    #
                    self._vArray.append(1 - vPercent)
        #
        self._nSideArray, self._vertexIdArray = [], []
        self._pointArray = []
        self._uArray, self._vArray = [], []
        #
        vCount = self._vDivision
        uCount = self._uDivision
        #
        width = self._uiWidth
        spin = self._spin
        #
        twist = self._twist
        taper = self._taper
        arch = self._arch
        archAttachCurveEnable = self._archAttachCurveEnable
        #
        step01()
        step02()
    #
    def createMesh(self):
        mMesh = OpenMaya.MFnMesh()
        #
        mMesh.create(
            self._pointArray,
            self._nSideArray,
            self._vertexIdArray,
            parent=self._mMeshCreate
        )
        #
        mapSet = 'map1'
        mMesh.setUVs(self._uArray, self._vArray, mapSet)
        mMesh.assignUVs(self._nSideArray, self._vertexIdArray, mapSet)


#
class meshToSurfaceCmd(object):
    def __init__(self, *args):
        (
            meshObject, surfaceCreate,
            direction
        ) = args
        # noinspection PyArgumentList
        self._mMesh = OpenMaya.MFnMesh(meshObject)
        self._mSurfaceCreate = surfaceCreate
        #
        self._direction = max(min(direction, 3), 0)
        #
        self._updateBasicData()
        self._updateCreateData()
    @staticmethod
    def _getKnotsArray(count, degree):
        lis = []
        minKnots, maxKnots = 0.0, 1.0
        #
        iPCount = count - 2
        [lis.append(minKnots) for i in range(degree)]
        #
        for seq in range(iPCount):
            lis.append(float(seq + 1) * maxKnots / (iPCount + 1))
        #
        [lis.append(maxKnots) for i in range(degree)]
        return lis
    @staticmethod
    def _getMidPoint(point1, point2):
        x, y, z = (point1.x + point2.x)/2, (point1.y + point2.y)/2, (point1.z + point2.z)/2
        # noinspection PyArgumentList
        return OpenMaya.MPoint(x, y, z)
    #
    def _pointAt(self, column, row):
        vertexId = self._rowVertexIdDic[row][column]
        return self._pointArray[vertexId]
    #
    def _midPointAt(self, column0, column1, row0, row1):
        point1 = self._pointAt(column0, row0)
        point2 = self._pointAt(column1, row1)
        return self._getMidPoint(point1, point2)
    #
    def _updateBasicData(self):
        def step1():
            for faceId in self._faceIds:
                vertexIds = self._mMesh.getPolygonVertices(faceId)
                for vertexId in vertexIds:
                    self._vertexFaceIdDic.setdefault(vertexId, []).append(faceId)
                    self._faceVertexIdDic.setdefault(faceId, []).append(vertexId)
        #
        def step2():
            dic = {}
            if self._vertexFaceIdDic:
                for k, v in self._vertexFaceIdDic.items():
                    dic.setdefault(len(v), []).append(k)
            #
            if dic:
                self._cornerVertexIdLis = dic[1]
                assert len(self._cornerVertexIdLis) == 4, 'Error: Mesh is Unused'
                self._borderVertexIdLis = dic[2]
        #
        def step3():
            def updateVertexIdSortLis(vertexId):
                if not vertexId in self._vertexIdSortLis:
                    self._vertexIdSortLis.append(vertexId)
            #
            def updateFaceIdSortLis(faceId):
                if not faceId in self._faceIdSortLis:
                    self._faceIdSortLis.append(faceId)
            #
            def updateRowVertexIdDic(row, vertexId):
                self._rowVertexIdDic.setdefault(row, []).append(vertexId)
            #
            def updateRowFaceIdDic(row, faceId):
                self._rowFaceIdDic.setdefault(row, []).append(faceId)
            #
            def getNexColumn(vertexId, faceId):
                curFaceVertexIds = self._faceVertexIdDic[faceId]
                curVertexIndex = curFaceVertexIds.index(vertexId)
                preVertexIndex = curVertexIndex - 1
                #
                preVertexId = curFaceVertexIds[preVertexIndex]
                preFaceIds = [i for i in self._vertexFaceIdDic[preVertexId] if i not in self._faceIdSortLis]
                return preVertexId, preFaceIds
            #
            def getNexRow(vertexId, faceId):
                curFaceVertexIds = self._faceVertexIdDic[faceId]
                curVertexIndex = curFaceVertexIds.index(vertexId)
                if curVertexIndex == 3:
                    nexVertexIndex = 0
                else:
                    nexVertexIndex = curVertexIndex + 1
                #
                nexVertexId = curFaceVertexIds[nexVertexIndex]
                nexFaceIds = [i for i in self._vertexFaceIdDic[nexVertexId] if i not in self._faceIdSortLis]
                return nexVertexId, nexFaceIds
            #
            def getLastRowColumn(faceIds):
                self._maxVertexRow += 1
                #
                for seq, faceId in enumerate(faceIds):
                    vertexIds = self._faceVertexIdDic[faceId]
                    if seq == 0:
                        cornerVertexId = [i for i in vertexIds if i in self._cornerVertexIdLis][0]
                        updateVertexIdSortLis(cornerVertexId)
                        updateRowVertexIdDic(self._maxVertexRow, cornerVertexId)
                    #
                    vertexId = [i for i in vertexIds if i not in self._vertexIdSortLis][0]
                    updateVertexIdSortLis(vertexId)
                    updateRowVertexIdDic(self._maxVertexRow, vertexId)
            #
            def toNexColumn(vertexId, faceId):
                updateVertexIdSortLis(vertexId)
                updateFaceIdSortLis(faceId)
                #
                updateRowVertexIdDic(self._maxVertexRow, vertexId)
                updateRowFaceIdDic(self._maxVertexRow, faceId)
                #
                nexVertexId, nexFaceIds = getNexColumn(vertexId, faceId)
                #  Add Column
                if self._maxVertexRow == 0:
                    self._maxVertexColumn += 1
                # Nex Column
                if nexFaceIds:
                    nexFaceId = nexFaceIds[0]
                    toNexColumn(nexVertexId, nexFaceId)
                # Last Column Nex Row
                else:
                    _curLastVertexId = self._vertexIdSortLis[-1]
                    _curLastFaceId = self._faceIdSortLis[-1]
                    #
                    startRowEndVertexId, _ = getNexColumn(_curLastVertexId, _curLastFaceId)
                    #
                    updateVertexIdSortLis(startRowEndVertexId)
                    updateRowVertexIdDic(self._maxVertexRow, startRowEndVertexId)
                    #
                    curRowStartVertexId = self._rowVertexIdDic[self._maxVertexRow][0]
                    curRowStartFaceId = self._rowFaceIdDic[self._maxVertexRow][0]
                    nexRowStartVertexId, nexRowStartFaceIds = getNexRow(curRowStartVertexId, curRowStartFaceId)
                    # Nex Column
                    if nexRowStartFaceIds:
                        self._maxVertexRow += 1
                        #
                        nexRowStartFaceId = nexRowStartFaceIds[0]
                        toNexColumn(nexRowStartVertexId, nexRowStartFaceId)
                    # Last Row
                    else:
                        lastRowFaceIds = self._rowFaceIdDic[self._maxVertexRow]
                        getLastRowColumn(lastRowFaceIds)
            #
            startVertexId = self._cornerVertexIdLis[self._direction]
            startFaceId = self._vertexFaceIdDic[startVertexId][0]
            toNexColumn(startVertexId, startFaceId)
        #
        self._numPolygons = self._mMesh.numPolygons
        self._faceIds = range(self._numPolygons)
        #
        self._pointArray = self._mMesh.getPoints(space=4)
        #
        self._vertexFaceIdDic, self._faceVertexIdDic = {}, {}
        #
        self._cornerVertexIdLis = []
        self._borderVertexIdLis = []
        #
        self._vertexIdSortLis, self._faceIdSortLis = [], []
        #
        self._maxVertexColumn, self._maxVertexRow = 0, 0
        #
        self._rowVertexIdDic = {}
        self._rowFaceIdDic = {}
        #
        step1()
        step2()
        step3()
    #
    def _updateCreateData(self):
        def step1():
            def getBranchAtColumn(vertexIds, column):
                vertexId = vertexIds[column]
                point = self._pointArray[vertexId]
                if column == 0:
                    nexColumn = column + 1
                    nexVertexId = vertexIds[nexColumn]
                    nexPoint = self._pointArray[nexVertexId]
                    nexMidPoint = self._getMidPoint(point, nexPoint)
                    self._cvPointArray.append(point)
                    self._cvPointArray.append(nexMidPoint)
                elif column == self._maxVertexColumn:
                    preColumn = column - 1
                    preVertexId = vertexIds[preColumn]
                    prePoint = self._pointArray[preVertexId]
                    preMidPoint = self._getMidPoint(prePoint, point)
                    self._cvPointArray.append(preMidPoint)
                    self._cvPointArray.append(point)
                else:
                    self._cvPointArray.append(point)
            #
            def getPointAtRow(row, columns):
                vertexIds = self._rowVertexIdDic[row]
                [getBranchAtColumn(vertexIds, column) for column in columns]
            #
            def getMidPointsInRow(row1, row2, columns):
                vertexIds1 = self._rowVertexIdDic[row1]
                vertexIds2 = self._rowVertexIdDic[row2]
                for column in columns:
                    vertexId1 = vertexIds1[column]
                    vertexId2 = vertexIds2[column]
                    point1 = self._pointArray[vertexId1]
                    point2 = self._pointArray[vertexId2]
                    #
                    midPoint = self._getMidPoint(point1, point2)
                    if column == 0:
                        nexColumn = column + 1
                        nexMidPoint = self._midPointAt(column, nexColumn, row1, row2)
                        self._cvPointArray.append(midPoint)
                        self._cvPointArray.append(nexMidPoint)
                    elif column == self._maxVertexColumn:
                        preColumn = column - 1
                        preMidPoint = self._midPointAt(preColumn, column, row1, row2)
                        self._cvPointArray.append(preMidPoint)
                        self._cvPointArray.append(midPoint)
                    else:
                        self._cvPointArray.append(midPoint)
            #
            def getMain():
                rows = range(self._maxVertexRow + 1)
                columns = range(self._maxVertexColumn + 1)
                for row in rows:
                    if row == 0:
                        nexRow = row + 1
                        getPointAtRow(row, columns)
                        getMidPointsInRow(row, nexRow, columns)
                    elif row == self._maxVertexRow:
                        preRow = row - 1
                        getMidPointsInRow(preRow, row, columns)
                        getPointAtRow(row, columns)
                    else:
                        getPointAtRow(row, columns)
            #
            getMain()
        #
        def step2():
            self._uKnotsArray = self._getKnotsArray(self._maxVertexRow + 1, self._uDegree)
            self._vKnotsArray = self._getKnotsArray(self._maxVertexColumn + 1, self._vDegree)
        #
        self._cvPointArray = []
        self._uKnotsArray, self._vKnotsArray = [], []
        self._uDegree, self._vDegree = 3, 3
        self._uFrom, self._vFrom = 1, 1
        #
        step1()
        step2()
    #
    def createSurface(self):
        mSurface = OpenMaya.MFnNurbsSurface()
        mSurface.create(
            self._cvPointArray,
            self._uKnotsArray, self._vKnotsArray,
            self._uDegree, self._vDegree, self._uFrom, self._vFrom,
            True,
            parent=self._mSurfaceCreate
        )


# Nde_Node
class curveToMesh(OpenMayaUI.MPxLocatorNode):
    nodeName = 'curveToMesh'
    # noinspection PyArgumentList
    typeId = OpenMaya.MTypeId(0x8700A)
    nodeClass = 'lynxi/geometry'
    #
    inputCurveAttr = OpenMaya.MObject()
    outputMeshAttr = OpenMaya.MObject()
    #
    uniformEnableAttr = OpenMaya.MObject()
    #
    vDivisionAttr = OpenMaya.MObject()
    uDivisionAttr = OpenMaya.MObject()
    #
    widthAttr = OpenMaya.MObject()
    widthExtraAttr = OpenMaya.MObject()
    #
    spinAttr = OpenMaya.MObject()
    spinExtraAttr = OpenMaya.MObject()
    #
    twistAttr = OpenMaya.MObject()
    taperAttr = OpenMaya.MObject()
    archAttr = OpenMaya.MObject()
    archAttachCurveEnableAttr = OpenMaya.MObject()
    #
    minPercentAttr = OpenMaya.MObject()
    maxPercentAttr = OpenMaya.MObject()
    #
    sampleAttr = OpenMaya.MObject()
    smoothDepthAttr = OpenMaya.MObject()
    angleOffsetAttr = OpenMaya.MObject()
    def __init__(self):
        super(curveToMesh, self).__init__()
    @classmethod
    def _addCompAttr(cls, longName, shortName):
        compAttr = OpenMaya.MFnCompoundAttribute()
        numAttr = OpenMaya.MFnNumericAttribute()
        enumAttr = OpenMaya.MFnEnumAttribute()
        #
        attr = compAttr.create(longName, shortName)
        #
        positionAttr = numAttr.create(
            longName + '_Position', shortName + 'p',
            OpenMaya.MFnNumericData.kFloat
        )
        #
        valueAttr = numAttr.create(
            longName + '_FloatValue', shortName + 'v',
            OpenMaya.MFnNumericData.kFloat
        )
        #
        interpAttr = enumAttr.create(
            longName + '_Interp', shortName + 'i'
        )
        enumAttr.addField('None', 0)
        enumAttr.addField('Linear', 1)
        enumAttr.addField('Smooth', 2)
        enumAttr.addField('Spline', 3)
        enumAttr.default = 3
        compAttr.addChild(positionAttr)
        compAttr.addChild(valueAttr)
        compAttr.addChild(interpAttr)
        #
        compAttr.storable = True
        compAttr.array = True
        compAttr.usesArrayDataBuilder = True
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addIntNumAttr(cls, longName, shortName, value, maximum=None, minimum=None, softMax=None, softMin=None, keyable=True):
        numAttr = OpenMaya.MFnNumericAttribute()
        #
        attr = numAttr.create(longName, shortName, OpenMaya.MFnNumericData.kInt, int(value))
        numAttr.writable = True
        numAttr.keyable = keyable
        numAttr.storable = True
        numAttr.channelBox = True
        if maximum is not None:
            numAttr.setMax(int(maximum))
        if minimum is not None:
            numAttr.setMin(int(minimum))
        if softMax is not None:
            numAttr.setSoftMax(softMax)
        if softMin is not None:
            numAttr.setSoftMin(softMin)
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addFloatNumAttr(cls, longName, shortName, value, maximum=None, minimum=None, softMax=None, softMin=None, keyable=True):
        numAttr = OpenMaya.MFnNumericAttribute()
        #
        attr = numAttr.create(longName, shortName, OpenMaya.MFnNumericData.kFloat, float(value))
        numAttr.writable = True
        numAttr.keyable = keyable
        numAttr.storable = True
        numAttr.channelBox = True
        if maximum is not None:
            numAttr.setMax(float(maximum))
        if minimum is not None:
            numAttr.setMin(float(minimum))
        if softMax is not None:
            numAttr.setSoftMax(float(softMax))
        if softMin is not None:
            numAttr.setSoftMin(float(softMin))
        cls.addAttribute(attr)
        return attr
    @classmethod
    def _addBooleanNumAttr(cls, longName, shortName, value, keyable=True):
        numAttr = OpenMaya.MFnNumericAttribute()
        #
        attr = numAttr.create(longName, shortName, OpenMaya.MFnNumericData.kBoolean, value)
        numAttr.writable = True
        numAttr.keyable = keyable
        numAttr.storable = True
        numAttr.channelBox = True
        cls.addAttribute(attr)
        return attr
    @classmethod
    def initializer(cls):
        typedAttr = OpenMaya.MFnTypedAttribute()
        # Connect
        cls.inputCurveAttr = typedAttr.create(
            'inputCurve', 'incrv',
            OpenMaya.MFnData.kNurbsCurve
        )
        typedAttr.hidden = True
        typedAttr.writable = True
        typedAttr.storable = True
        cls.addAttribute(cls.inputCurveAttr)
        #
        cls.outputMeshAttr = typedAttr.create(
            'outputMesh', 'otmsh',
            OpenMaya.MFnData.kMesh
        )
        typedAttr.hidden = True
        typedAttr.writable = True
        typedAttr.storable = True
        cls.addAttribute(cls.outputMeshAttr)
        #
        cls.uniformEnableAttr = cls._addBooleanNumAttr(
            'uniformEnable', 'ufmEn',
            value=1
        )
        # Custom
        cls.vDivisionAttr = cls._addIntNumAttr(
            'vDivision', 'vdvn',
            value=32,
            minimum=2
        )
        cls.uDivisionAttr = cls._addIntNumAttr(
            'uDivision', 'udvn',
            value=2,
            minimum=2
        )
        # Modify
        cls.widthAttr = cls._addFloatNumAttr(
            'width', 'wdh',
            value=1,
            minimum=0
        )
        cls.widthExtraAttr = cls._addCompAttr(
            'widthExtra', 'wdhex'
        )
        cls.spinAttr = cls._addFloatNumAttr(
            'spin', 'spn',
            value=0
        )
        cls.spinExtraAttr = cls._addCompAttr(
            'spinExtra', 'spnex'
        )
        #
        cls.twistAttr = cls._addFloatNumAttr(
            'twist', 'twt',
            value=0
        )
        cls.taperAttr = cls._addFloatNumAttr(
            'taper', 'tpr',
            value=1,
            minimum=0
        )
        cls.archAttr = cls._addFloatNumAttr(
            'arch', 'arh',
            value=0,
            minimum=-1, maximum=1
        )
        cls.archAttachCurveEnableAttr = cls._addBooleanNumAttr(
            'archAttachCurveEnable', 'arhatcven',
            value=1
        )
        #
        cls.minPercentAttr = cls._addFloatNumAttr(
            'minPercent', 'mnprn',
            value=0,
            minimum=0, maximum=1
        )
        cls.maxPercentAttr = cls._addFloatNumAttr(
            'maxPercent', 'mxprn',
            value=1,
            minimum=0, maximum=1
        )
        #
        cls.sampleAttr = cls._addIntNumAttr(
            'sample', 'spl',
            value=4,
            minimum=1, maximum=25
        )
        #
        cls.smoothDepthAttr = cls._addIntNumAttr(
            'smoothDepth', 'smtdp',
            value=2,
            minimum=0, maximum=25
        )
        cls.angleOffsetAttr = cls._addCompAttr(
            'angleOffset', 'anlof'
        )
        #
        cls.attributeAffects(
            cls.inputCurveAttr, cls.outputMeshAttr,
        )
        #
        cls.attributeAffects(
            cls.uniformEnableAttr, cls.outputMeshAttr,
        )
        #
        cls.attributeAffects(
            cls.vDivisionAttr, cls.outputMeshAttr,
        )
        cls.attributeAffects(
            cls.uDivisionAttr, cls.outputMeshAttr,
        )
        #
        cls.attributeAffects(
            cls.widthAttr, cls.outputMeshAttr,
        )
        cls.attributeAffects(
            cls.widthExtraAttr, cls.outputMeshAttr,
        )
        #
        cls.attributeAffects(
            cls.spinAttr, cls.outputMeshAttr,
        )
        cls.attributeAffects(
            cls.spinExtraAttr, cls.outputMeshAttr,
        )
        #
        cls.attributeAffects(
            cls.twistAttr, cls.outputMeshAttr,
        )
        cls.attributeAffects(
            cls.taperAttr, cls.outputMeshAttr,
        )
        cls.attributeAffects(
            cls.archAttr, cls.outputMeshAttr,
        )
        cls.attributeAffects(
            cls.archAttachCurveEnableAttr, cls.outputMeshAttr,
        )
        #
        cls.attributeAffects(
            cls.minPercentAttr, cls.outputMeshAttr,
        )
        cls.attributeAffects(
            cls.maxPercentAttr, cls.outputMeshAttr,
        )
        #
        cls.attributeAffects(
            cls.sampleAttr, cls.outputMeshAttr,
        )
        cls.attributeAffects(
            cls.smoothDepthAttr, cls.outputMeshAttr,
        )
        #
        cls.attributeAffects(
            cls.angleOffsetAttr, cls.outputMeshAttr,
        )
    @classmethod
    def create(cls):
        node = curveToMesh()
        return node
    @staticmethod
    def covertCommand(*args):
        if not args[0].isNull():
            cmd = curveToMeshCmd(*args)
            cmd.createMesh()
    # noinspection PyMethodOverriding
    def compute(self, plug, dataBlock):
        if (
                plug == curveToMesh.outputMeshAttr
                ):
            #
            inputCurve = dataBlock.inputValue(curveToMesh.inputCurveAttr)
            inputCurveObject = inputCurve.asNurbsCurve()
            #
            uniformEnable = dataBlock.inputValue(curveToMesh.uniformEnableAttr)
            uniformEnableBool = uniformEnable.asBool()
            #
            vDivision = dataBlock.inputValue(curveToMesh.vDivisionAttr)
            vDivisionValue = vDivision.asInt()
            uDivision = dataBlock.inputValue(curveToMesh.uDivisionAttr)
            uDivisionValue = uDivision.asInt()
            #
            width = dataBlock.inputValue(curveToMesh.widthAttr)
            widthValue = width.asFloat()
            # noinspection PyArgumentList
            widthExtraValue = OpenMaya.MRampAttribute(self.thisMObject(), curveToMesh.widthExtraAttr)
            #
            spin = dataBlock.inputValue(curveToMesh.spinAttr)
            spinValue = spin.asFloat()
            # noinspection PyArgumentList
            spinExtraValue = OpenMaya.MRampAttribute(self.thisMObject(), curveToMesh.spinExtraAttr)
            #
            twist = dataBlock.inputValue(curveToMesh.twistAttr)
            twistValue = twist.asFloat()
            taper = dataBlock.inputValue(curveToMesh.taperAttr)
            taperValue = taper.asFloat()
            arch = dataBlock.inputValue(curveToMesh.archAttr)
            archValue = arch.asFloat()
            archAttachCurveEnable = dataBlock.inputValue(curveToMesh.archAttachCurveEnableAttr)
            archAttachCurveEnableBool = archAttachCurveEnable.asBool()
            #
            minPercent = dataBlock.inputValue(curveToMesh.minPercentAttr)
            minPercentValue = minPercent.asFloat()
            maxPercent = dataBlock.inputValue(curveToMesh.maxPercentAttr)
            maxPercentValue = maxPercent.asFloat()
            #
            sample = dataBlock.inputValue(curveToMesh.sampleAttr)
            sampleValue = sample.asInt()
            #
            smoothDepth = dataBlock.inputValue(curveToMesh.smoothDepthAttr)
            smoothDepthValue = smoothDepth.asInt()
            # noinspection PyArgumentList
            angleOffsetValue = OpenMaya.MRampAttribute(self.thisMObject(), curveToMesh.angleOffsetAttr)
            #
            outputMesh = dataBlock.outputValue(curveToMesh.outputMeshAttr)
            outputMeshData = OpenMaya.MFnMeshData()
            outputMeshCreate = outputMeshData.create()
            #
            self.covertCommand(
                inputCurveObject, outputMeshCreate,
                uniformEnableBool,
                vDivisionValue, uDivisionValue,
                widthValue, widthExtraValue,
                spinValue, spinExtraValue,
                twistValue, taperValue, archValue, archAttachCurveEnableBool,
                minPercentValue, maxPercentValue,
                sampleValue, smoothDepthValue,
                angleOffsetValue
            )
            #
            outputMesh.setMObject(outputMeshCreate)
            dataBlock.setClean(plug)
        else:
            return None


#
class meshToSurface(OpenMayaUI.MPxLocatorNode):
    nodeName = 'meshToSurface'
    # noinspection PyArgumentList
    typeId = OpenMaya.MTypeId(0x8700C)
    nodeClass = 'lynxi/geometry'
    #
    inputMeshAttr = OpenMaya.MObject()
    outputSurfaceAttr = OpenMaya.MObject()
    #
    directionAttr = OpenMaya.MObject()
    def __init__(self):
        super(meshToSurface, self).__init__()
    @classmethod
    def _addIntNumAttr(cls, longName, shortName, value, maximum=None, minimum=None, softMax=None, softMin=None, keyable=True):
        numAttr = OpenMaya.MFnNumericAttribute()
        #
        attr = numAttr.create(longName, shortName, OpenMaya.MFnNumericData.kInt, int(value))
        numAttr.writable = True
        numAttr.keyable = keyable
        numAttr.storable = True
        numAttr.channelBox = True
        if maximum is not None:
            numAttr.setMax(int(maximum))
        if minimum is not None:
            numAttr.setMin(int(minimum))
        if softMax is not None:
            numAttr.setSoftMax(softMax)
        if softMin is not None:
            numAttr.setSoftMin(softMin)
        cls.addAttribute(attr)
        return attr
    @classmethod
    def initializer(cls):
        typedAttr = OpenMaya.MFnTypedAttribute()
        # Connect
        cls.inputMeshAttr = typedAttr.create(
            'inputMesh', 'inmsh',
            OpenMaya.MFnData.kMesh
        )
        typedAttr.hidden = True
        typedAttr.writable = True
        typedAttr.storable = True
        cls.addAttribute(cls.inputMeshAttr)
        #
        cls.outputSurfaceAttr = typedAttr.create(
            'outputSurface', 'otsfc',
            OpenMaya.MFnData.kNurbsSurface
        )
        typedAttr.hidden = True
        typedAttr.writable = True
        typedAttr.storable = True
        cls.addAttribute(cls.outputSurfaceAttr)
        #
        cls.directionAttr = cls._addIntNumAttr(
            'direction', 'dir',
            value=0,
            minimum=0, maximum=3,
            softMin=0, softMax=3
        )
        #
        cls.attributeAffects(
            cls.inputMeshAttr, cls.outputSurfaceAttr,
        )
        cls.attributeAffects(
            cls.directionAttr, cls.outputSurfaceAttr,
        )
    @classmethod
    def create(cls):
        node = meshToSurface()
        return node
    @staticmethod
    def covertCommand(*args):
        if not args[0].isNull():
            cmd = meshToSurfaceCmd(*args)
            cmd.createSurface()
    # noinspection PyMethodOverriding
    def compute(self, plug, dataBlock):
        if (
                plug == meshToSurface.outputSurfaceAttr
                ):
            inputMesh = dataBlock.inputValue(meshToSurface.inputMeshAttr)
            inputMeshObject = inputMesh.asMesh()
            #
            direction = dataBlock.inputValue(meshToSurface.directionAttr)
            directionValue = direction.asInt()
            #
            outSurface = dataBlock.outputValue(meshToSurface.outputSurfaceAttr)
            outputSurfaceData = OpenMaya.MFnNurbsSurfaceData()
            outSurfaceCreate = outputSurfaceData.create()
            #
            self.covertCommand(
                inputMeshObject, outSurfaceCreate,
                directionValue
            )
            #
            outSurface.setMObject(outSurfaceCreate)
            dataBlock.setClean(plug)
        else:
            return None


# Initialize
def initializePlugin(obj):
    # noinspection PyArgumentList
    plug = OpenMaya.MFnPlugin(obj, 'ChangBao.Dong', '1.0.0', 'Any')
    # Register Nde_Node
    try:
        plug.registerNode(
            curveToMesh.nodeName,
            curveToMesh.typeId,
            curveToMesh.create,
            curveToMesh.initializer
        )
    except:
        sys.stderr.write('Failed to Register Nde_Node: %s' % curveToMesh.nodeName)
        raise
    try:
        plug.registerNode(
            meshToSurface.nodeName,
            meshToSurface.typeId,
            meshToSurface.create,
            meshToSurface.initializer
        )
    except:
        sys.stderr.write('Failed to Register Nde_Node: %s' % meshToSurface.nodeName)
        raise


# Uninitialize
def uninitializePlugin(obj):
    # noinspection PyArgumentList
    plug = OpenMaya.MFnPlugin(obj)
    # Deregister Nde_Node
    try:
        plug.deregisterNode(
            curveToMesh.typeId
        )
    except:
        sys.stderr.write('Failed to Deregister Nde_Node: %s' % curveToMesh.nodeName)
        raise
    try:
        plug.deregisterNode(
            meshToSurface.typeId
        )
    except:
        sys.stderr.write('Failed to Deregister Nde_Node: %s' % meshToSurface.nodeName)
        raise
