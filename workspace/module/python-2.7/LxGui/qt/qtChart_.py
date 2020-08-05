# coding=utf-8
import math
#
from LxBasic import bscMtdCore, bscMethods
#
#
from LxGui.qt import qtCore

#
fnc_angle = math.radians
fnc_sin = math.sin
fnc_cos = math.cos
fnc_tan = math.tan
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore


#
def getPieDrawData(data, width, height, side):
    def getBranch(inData, seq=0, qa=90, ma=0):
        explain, value, color = inData[seq]
        br, bg, bb, ba = color
        backgroundRgba = br, bg, bb, ba
        #
        p = float(value) / float(maxValue)
        _a = 360 * p
        a = 360 - _a
        s = ma + _a/2
        _xo = fnc_sin(fnc_angle(s)) * (side/4)
        _yo = fnc_cos(fnc_angle(s)) * (side/4)
        #
        piePath = qtCore.CLS_painterPath()
        _s = 4
        cx = w1 / 2 + _s/2 + x1
        cy = w1 / 2 + _s/2 + y1
        piePath.moveTo(cx, cy)
        piePath.arcTo(x1 - _s/2, y1 - _s/2, w1 + _s, w1 + _s, qa, a)
        #
        path = rimPath - piePath
        shadowPath = rimPath - piePath
        #
        percent = '%s%%' % (qtCore.toShowPercent(maxValue, value, roundCount=4))
        #
        lis.append((backgroundRgba, explain, percent, path, shadowPath, (_xo, -_yo)))
        #
        seq += 1
        qa += a
        ma += _a
        if seq <= dataCount - 1:
            getBranch(inData, seq, qa, ma)
    #
    lis = []
    if data:
        dataCount = len(data)
        maxValue = sum([i[1] for i in data])
        if maxValue > 0:
            w = width - side * 2
            h = height - side * 2
            x = side
            y = side
            #
            x1 = x
            y1 = y
            w1 = w
            rimPath = qtCore.CLS_painterPath()
            rimPath.addEllipse(x1, y1, w1, w1)
            #
            w2 = w1 / 2
            x2 = (w1 - w2) / 2 + x1
            y2 = (w1 - w2) / 2 + y1
            rimPath.addEllipse(x2, y2, w2, w2)
            #
            getBranch(data)
    return lis


#
def getUvDrawData(uvData, width, xPosition, yPosition):
    lis = []
    if uvData:
        nSideArray, idArray, uArray, vArray = uvData
        for sSeq, nSide in enumerate(nSideArray):
            s = sum(nSideArray[:sSeq])
            points = []
            us = []
            vs = []
            for nSeq in range(nSide):
                pointId = idArray[s + nSeq]
                u = uArray[pointId]
                us.append(u)
                v = vArray[pointId]
                vs.append(v)
            if 0 <= min(us) <= 1 and 0 <= min(vs) <= 1:
                for seq in range(nSide):
                    x = us[seq] * width + xPosition
                    y = (1 - vs[seq]) * width + yPosition
                    point = qtCore.CLS_point(x, y)
                    points.append(point)
            lis.append(qtCore.CLS_polygon(points))
    return lis


#
def getRegularPolygonPoints(xPos, yPos, sideCount, radius, side=0):
    lis = []
    for seq in range(sideCount):
        a = 360 / sideCount * seq
        x = fnc_sin(fnc_angle(a)) * (radius - side) + xPos
        y = fnc_cos(fnc_angle(a)) * (radius - side) + yPos
        lis.append((x, y))
    if lis:
        lis.append(lis[0])
    return lis


#
class QtPiechart_(qtCore.QWidget_):
    def __init__(self, *args, **kwargs):
        self._clsSuper = super(QtPiechart_, self)
        self._clsSuper.__init__(*args, **kwargs)
        #
        self._pressData = None
        #
        self.initUi()
        #
        self.setUiSize(self._wgt__frame_w_, self._wgt__frame_h_)
    #
    def setNameString(self, string):
        self._gui_qt__mdl__name_str_ = string
    # noinspection PyArgumentList
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.pressAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.pressAction(event)
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        #
        side = self._uiSide
        rimSide = self._rimSide
        xOffset = self._xOffset
        yOffset = self._yOffset
        #
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHint(painter.Antialiasing)
        if self._pieDrawData:
            for i in self._pieDrawData:
                backgroundRgba, explain, percent, path, shadowPath, pos = i
                painter.setBackgroundRgba(backgroundRgba)
                painter.setBorderRgba(223, 223, 223, 255)
                painter.setPenWidth(2)
                painter.drawPath(path)
                #
                newPath = shadowPath - path
                painter.setBackgroundRgba(0, 0, 0, 64)
                painter.setBorderRgba(0, 0, 0, 64)
                painter.setPenWidth(1)
                painter.drawPath(newPath)
            # Explain
            if self._subExplain is not None:
                rect = QtCore.QRect(
                    side, side,
                    width, self._explainHeight
                )
                painter.setPen(self._pen)
                painter.setFont(qtCore.qtFont(size=10, weight=50, family=qtCore._families[1]))
                painter.drawText(rect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, self._subExplain)
            else:
                if self._gui_qt__mdl__name_str_ is not None:
                    rect = QtCore.QRect(
                        side, side,
                        width, self._explainHeight
                    )
                    painter.setPen(self._pen)
                    painter.setFont(qtCore.qtFont(size=10, weight=50, family=qtCore._families[1]))
                    painter.drawText(rect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, self._gui_qt__mdl__name_str_)
            # Percent
            if self._percent is not None:
                rect = QtCore.QRect(
                    (width - self._explainWidth) / 2, (width - self._explainHeight) / 2,
                    self._explainWidth, self._explainHeight
                )
                painter.setPen(self._pen)
                painter.setFont(qtCore.qtFont(size=10, weight=50, family=qtCore._families[1]))
                painter.drawText(rect, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter, self._percent)

        # painter.end()  # for pyside2
    #
    def pressAction(self, event):
        isPressEnabled = False
        if self._selPathData:
            for seq, i in enumerate(self._selPathData):
                explain, percent, path, shadowPath, pos, isPress = i
                x, y = pos
                if path.contains(event.pos()) is True:
                    if isPress is False:
                        isPress = True
                        self._subExplain = '{0} : {1}'.format(self._gui_qt__mdl__name_str_, explain)
                        self._percent = percent
                        path.translate(x, y)
                        shadowPath.translate(x + 4, y + 4)
                    #
                    isPressEnabled = True
                    #
                    self._selPathData[seq] = path, pos, True
                elif path.contains(event.pos()) is False:
                    if isPress is True:
                        isPress = False
                        path.translate(-x, -y)
                        shadowPath.translate(-x - 4, -y - 4)
                #
                self._selPathData[seq] = explain, percent, path, shadowPath, pos, isPress
        #
        if not isPressEnabled:
            self._subExplain = None
            self._percent = None
        #
        self.update()
    #
    def setDrawData(self, data):
        self._selPathData = []
        #
        width = self._wgt__frame_w_
        height = self._wgt__frame_h_
        rimSide = self._rimSide
        #
        self._pieDrawData = getPieDrawData(
            data, width, height, rimSide
        )
        self._pieDrawData.reverse()
        self._selPathData = [(i[-5], i[-4], i[-3], i[-2], i[-1], False) for i in self._pieDrawData]
        #
        self.update()
    #
    def setDrawDatas(self, datas):
        for data in datas:
            pass
    #
    def setUiSize(self, width, height):
        self._wgt__frame_w_ = width
        self._wgt__frame_h_ = height
        self.setMaximumSize(width, height)
        self.setMinimumSize(width, height)
    #
    def setUiWidth(self, width):
        self._wgt__frame_w_ = width
        self.setMaximumSize(width, 166667)
        self.setMinimumSize(width, 0)
    #
    def initUi(self):
        self._wgt__frame_w_ = 400
        self._wgt__frame_h_ = 400
        self._uiSide = 8
        self._rimSide = 48
        self._xOffset = 0
        self._yOffset = 0
        #
        self._explainWidth = 240
        self._explainHeight = 20
        #
        self._pressPoint = qtCore.CLS_point(0, 0)
        #
        self._pieDrawData = []
        self._selPathData = []
        self._selPathDatas = []
        self._gui_qt__mdl__name_str_ = None
        self._subExplain = None
        self._percent = None
        self._pen = qtCore.CLS_pen(qtCore.CLS_color(223, 223, 223, 255))


#
class QtMapchart_(qtCore.QWidget_):
    width = 380
    xPosition = 20
    yPosition = 0
    def __init__(self, *args, **kwargs):
        self.QtMapchart_Super = super(QtMapchart_, self)
        self.QtMapchart_Super.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.uvData = []
        self.draw = False
        #
        self.pen = qtCore.CLS_pen(qtCore.CLS_color(191, 191, 191, 255))
        self.brush = qtCore.CLS_brush(qtCore.CLS_color(0, 127, 127, 64))
        self.setUiStyle()
        self.setUiSize(400, 400)
    #
    def drawGrid(self, painter, width, xPosition, yPosition):
        # Grid
        grid = qtCore.CLS_rect(xPosition, yPosition, width, width)
        pen = qtCore.CLS_pen(qtCore.CLS_color(127, 127, 127, 255))
        painter.setPen(pen)
        painter.drawRect(grid)
    #
    def drawAxis(self, painter, width, xPosition, yPosition):
        # X Axis
        xLine = qtCore.CLS_line(xPosition, width + yPosition, width / 2 + xPosition, width + yPosition)
        pen = qtCore.CLS_pen(qtCore.CLS_color(255, 0, 63, 255))
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawLine(xLine)
        # Y Axis
        yLine = qtCore.CLS_line(xPosition, width / 2 + yPosition, xPosition, width + yPosition)
        pen = qtCore.CLS_pen(qtCore.CLS_color(63, 255, 127, 255))
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawLine(yLine)
    #
    def setDrawEnable(self, boolean):
        self.draw = boolean
    #
    def paintEvent(self, event):
        if self.draw:
            width = self.width
            xPosition = self.xPosition
            yPosition = self.yPosition
            #
            painter = qtCore.QPainter_(self)
            # painter.begin(self)  # for pyside2

            painter.setRenderHint(painter.Antialiasing)
            #
            self.drawGrid(painter, width, xPosition, yPosition)
            #
            self.drawAxis(painter, width, xPosition, yPosition)
            #
            quadrantText = '1001'
            quadrantPoint = qtCore.CLS_point(xPosition, width + 20 + yPosition)
            pen = qtCore.CLS_pen(qtCore.CLS_color(223, 223, 223, 255))
            painter.setPen(pen)
            painter.setFont(qtCore.qtFont(size=8, weight=75))
            painter.drawText(quadrantPoint, quadrantText)
            if self.uvData:
                drawData = self.uvData
                if drawData:
                    pen = qtCore.CLS_pen(qtCore.CLS_color(191, 191, 191, 255))
                    pen.setWidth(1)
                    painter.setPen(pen)
                    painter.setBrush(qtCore.CLS_brush(qtCore.CLS_color(0, 127, 127, 64)))
                    for i in drawData:
                        painter.drawPolygon(i, QtCore.Qt.WindingFill)

            # painter.end()  # for pyside2
        # self.draw = False
    # #
    # def wheelEvent(self, event):
    #     if event.delta() > 0:
    #         self.width  = self.width + 16
    #     if event.delta() < 0:
    #         self.width = self.width - 16
    #     self.update()
    # #
    # def mousePressEvent(self, event):
    #     pos = event.pos()
    #     if QApplication.mouseButtons() == QtCore.Qt.LeftButton:
    #         self.QtMapchart_Super.mousePressEvent(event)
    #     if QApplication.mouseButtons() == QtCore.Qt.MiddleButton:
    #         self.origPos = pos
    #         self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
    #
    # def mouseMoveEvent(self, event):
    #     pos = event.pos()
    #     x = pos.x()
    #     y = pos.y()
    #     # print pos - self.origPos
    #     if QApplication.mouseButtons() == QtCore.Qt.MiddleButton:
    #         self.move(event.globalPos() - self.dragPosition)
    #         # self.xPosition = x
    #         # self.yPosition = y
    #     # self.update()
    #
    def setDrawData(self, data):
        width = self.width
        xPosition = self.xPosition
        yPosition = self.yPosition
        #
        self.uvData = getUvDrawData(data, width, xPosition, yPosition)
    #
    def setUiStyle(self):
        self.setStyleSheet(
            'QFrame{border: none}'
            'QFrame{background: rgba(63, 63, 63, 255)}')
    #
    def setUiSize(self, width, height):
        self.setMinimumSize(width, height)


#
class QtSequencechart_(qtCore.QWidget_):
    def __init__(self, *args, **kwargs):
        self._clsSuper = super(QtSequencechart_, self)
        self._clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setUiSize()
    #
    def setDrawData(self, rangeArray, startNum, endNum):
        if rangeArray != self._rangeArray:
            self._rangeArray = rangeArray
            self._startNum = startNum
            self._endNum = endNum
            #
            self.update()
    #
    def paintEvent(self, event):
        xPos = 0
        yPos = 0
        width = self.width()
        height = self.height()
        #
        side = 2
        #
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        #
        painter.setFont(qtCore.qtFont(size=8, weight=75))
        #
        startNum = self._startNum
        endNum = self._endNum
        #
        maxValue = endNum - startNum + 1
        #
        if maxValue > 0:
            width = maxValue * 4
            #
            painter.setBorderRgba(71, 71, 71, 255)
            painter.setBackgroundRgba(39, 39, 39, 255)
            #
            rect = qtCore.CLS_rect(xPos + side, yPos + side, width - side * 2, height - side * 2)
            painter.drawRect(rect)
            #
            if self._rangeArray is not None:
                rangeArray = self._rangeArray
                #
                dvWidth = float(width - side * 2) / float(maxValue)
                subSide = side + 2
                for numRange in rangeArray:
                    if isinstance(numRange, int):
                        xSubPos = side + int((numRange - startNum) * dvWidth)
                        ySubPos = subSide - 1
                        subWidth = int(dvWidth)
                        subHeight = height - subSide * 2 + 2
                        #
                        percent = float(1) / float(maxValue)
                        r, g, b = qtCore.hsv2rgb(140, 1 * percent, 1)
                        painter.setBorderRgba(r, g, b, 255)
                        painter.setBackgroundRgba(r, g, b, 255)
                        #
                        subRect = qtCore.CLS_rect(xSubPos, ySubPos, subWidth, subHeight)
                        painter.drawRect(subRect)
                        #
                        painter.setBorderRgba(0, 0, 0, 255)
                        painter.setBackgroundRgba(0, 0, 0, 0)
                        subPoint = qtCore.CLS_point(xSubPos, ySubPos + 12)
                        painter.drawText(subPoint, str(numRange))
                    elif isinstance(numRange, tuple) or isinstance(numRange, list):
                        subStartNum, subEndNum = numRange
                        xSubPos = side + int((subStartNum - startNum) * dvWidth)
                        ySubPos = subSide - 1
                        subWidth = int((subEndNum - subStartNum + 1) * dvWidth)
                        subHeight = height - subSide * 2 + 2
                        #
                        percent = float(subEndNum - subStartNum + 1) / float(maxValue)
                        r, g, b = qtCore.hsv2rgb(140, 1 * percent, 1)
                        painter.setBorderRgba(r, g, b, 255)
                        painter.setBackgroundRgba(r, g, b, 255)
                        #
                        subRect = qtCore.CLS_rect(xSubPos, ySubPos, subWidth, subHeight)
                        painter.drawRect(subRect)
                        #
                        painter.setBorderRgba(0, 0, 0, 255)
                        painter.setBackgroundRgba(0, 0, 0, 0)
                        subPoint = qtCore.CLS_point(xSubPos, ySubPos + 12)
                        painter.drawText(subPoint, '{}-{}'.format(subStartNum, subEndNum))

        # painter.end()  # for pyside2
    #
    def setUiSize(self):
        self.setMaximumSize(166667, 20)
        self.setMinimumSize(0, 20)
    #
    def initUi(self):
        self._rangeArray = None
        #
        self._startNum = 0
        self._endNum = 0
        #
        self._rangeRects = []


#
class QtHistogramchart_(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        self._clsSuper = super(qtCore.QWidget, self)
        self._clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding,
            qtCore.QSizePolicy.Expanding
        )
        #
        self.initUi()
        #
        self.setUiSize()
    #
    def setDrawData(self, valueArray, valueOffset, valueExplain):
        self._valueArray = valueArray
        self._xValueOffset, self._yValueOffset = valueOffset
        self._xValueExplain, self._yValueExplain = valueExplain
        #
        self.update()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            xPos = event.pos().x() - self._xTrackOffset - self._xGridOffset
            self._selectedIndex = int(xPos/int(self._uiGridSize/2))
            #
            self.update()
            # Drag Select
            self._moveFlag = True
        #
        elif event.button() == QtCore.Qt.RightButton:
            pass
        elif event.button() == QtCore.Qt.MidButton:
            # Track
            self._trackStartPoint = event.globalPos()
            self._trackFlag = True
            # Zoom
            self._zoomFlag = False
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._moveFlag = False
        elif event.button() == QtCore.Qt.RightButton:
            pass
        elif event.button() == QtCore.Qt.MidButton:
            # Track
            self._xTempTrackOffset = self._xTrackOffset
            self._trackFlag = False
            # Zoom
            self._zoomFlag = True
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            if self._moveFlag is True:
                self.setSelectedIndexRefresh(event)
                #
                self.update()
        elif event.buttons() == QtCore.Qt.RightButton:
            pass
        elif event.buttons() == QtCore.Qt.MidButton:
            # Track
            if self._trackFlag is True:
                point = event.globalPos() - self._trackStartPoint
                self._trackMoveAction(point)
        else:
            event.ignore()
    #
    def wheelEvent(self, event):
        if self._zoomFlag is True:
            delta = event.angleDelta().y()
            self.zoomAction(delta)
    #
    def paintEvent(self, event):
        xPos = 0
        yPos = 0
        #
        width = self.width()
        height = self.height()
        #
        gridSize = self._uiGridSize
        #
        xGridOffset = self._xGridOffset
        yGridOffset = gridSize
        #
        xTrackOffset = self._xTrackOffset
        yTrackOffset = 0
        #
        xValueMult = 1
        yValueMult = 1
        #
        xGridMult = self._xGridMult
        yGridMult = self._yGridMult
        #
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setDrawGrid(
            width, height, (1, -1),
            gridSize, (xTrackOffset, yTrackOffset), (xGridOffset, yGridOffset),
            self._gridColor
        )
        #
        self._colSelRects = []
        #
        if self._valueArray:
            maxValue = max(self._valueArray)
            if maxValue:
                xValueMult = xGridMult
                yValueMult = int(float('1' + len(str(maxValue)) * '0') / float(yGridMult))
                #
                columnWidth = gridSize / xGridMult
                #
                limitHeight = gridSize / yGridMult
                #
                currentValueX = None
                currentValueY = None
                for seq, v in enumerate(self._valueArray):
                    rgbPercent = float(v) / float(maxValue)
                    r, g, b = qtCore.hsv2rgb(140 * rgbPercent, 1, 1)
                    #
                    painter.setBackgroundRgba(r, g, b, 255)
                    painter.setBorderRgba(r, g, b, 255)
                    #
                    valuePercent = float(v) / float(yValueMult)
                    columnPosX = xPos + columnWidth * seq + xGridOffset + xTrackOffset + 1
                    columnPoxY = (height - limitHeight * valuePercent * yGridMult - yGridOffset + yTrackOffset)
                    #
                    if xGridOffset <= columnPosX <= width:
                        drawRect = qtCore.CLS_rect(
                            columnPosX, columnPoxY,
                            columnWidth - 2, (limitHeight * valuePercent) * yGridMult
                        )
                        painter.drawRect(drawRect)
                        #
                        if seq == self._selectedIndex:
                            currentValueX = seq + self._xValueOffset
                            currentValueY = v + self._yValueOffset
                            #
                            painter.setBackgroundRgba(0, 0, 0, 0)
                            painter.setBorderRgba(223, 223, 223, 255)
                            #
                            selRect = qtCore.CLS_rect(
                                columnPosX, 0,
                                columnWidth - 2, height - yGridOffset
                            )
                            #
                            painter.drawRect(selRect)
                #
                if currentValueX is not None and currentValueY is not None:
                    textRect = qtCore.CLS_rect(
                        xGridOffset + 8, 0 + 8,
                        width, height
                    )
                    #
                    painter.setBorderRgba(223, 223, 223, 255)
                    painter.setFont(qtCore.qtFont(size=12, weight=75))

                    painter.drawText(
                        textRect,
                        QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop,
                        '{2} ( {0} )\r\n{3} ( {1} )'.format(
                            self._xValueExplain,
                            self._yValueExplain, currentValueX,
                            bscMethods.Value.toPrettify(currentValueY, useMode=self._useMode)
                        )
                    )
        #
        painter.setDrawAxis(
            width, height, (xTrackOffset, yTrackOffset), (xGridOffset - 1, yGridOffset - 1),
            self._axisColor
        )
        painter.setDrawGridMark(
            width, height, (1, -1),
            gridSize, (xTrackOffset, yTrackOffset), (xGridOffset, yGridOffset),
            (xValueMult, yValueMult), (self._xValueOffset, self._yValueOffset),
            self._markColor,
            self._useMode
        )

        # painter.end()  # for pyside2
    #
    def setSelectedIndexRefresh(self, event):
        xPos = event.pos().x() - self._xTrackOffset - self._xGridOffset
        self._selectedIndex = int(xPos / int(self._uiGridSize / self._xGridMult))
    #
    def _trackMoveAction(self, point):
        radix = self._uiGridSize / 2
        xTrackOffset = self._xTempTrackOffset
        xTrackOffset += point.x()
        #
        if self._limitEnabled is True:
            xTrackOffset = [0, xTrackOffset][xTrackOffset < 0]
        # Track
        if self._trackFlag is True:
            self._xTrackOffset = int(xTrackOffset/radix)*radix
        #
        self.update()
    #
    def zoomAction(self, delta):
        radix = 2.5
        if radix >= self._yGridMult:
            self._yGridMult += [0, radix][delta > 0]
        elif radix < self._yGridMult < self._uiGridSize:
            self._yGridMult += [-radix, radix][delta > 0]
        elif self._yGridMult >= self._uiGridSize:
            self._yGridMult += [-radix, 0][delta > 0]
        #
        self.update()
    #
    def setSelected(self, index):
        self._selectedIndex = index
    #
    def setUiSize(self):
        self.setMaximumSize(166667, 166667)
        self.setMinimumSize(0, 0)
    #
    def initUi(self):
        self._gridColor = 71, 71, 71, 255
        self._markColor = 191, 191, 191, 255
        self._axisColor = 191, 191, 191, 255
        #
        self._useMode = 1
        #
        self._zoomFlag = True
        #
        self._limitEnabled = True
        self._trackFlag = False
        self._trackStartPoint = qtCore.CLS_point(0, 0)
        self._xTempTrackOffset = 0
        self._xTrackOffset = 0
        #
        self._moveFlag = False
        #
        self._uiGridSize = 20
        #
        self._xGridMult = 2
        self._yGridMult = 10
        #
        self._xGridOffset = self._uiGridSize*2
        #
        self._valueArray = []
        #
        self._xValueOffset = 0
        self._yValueOffset = 0
        #
        self._xValueExplain = 'X'
        self._yValueExplain = 'Y'
        #
        self._selectedIndex = -1
        #
        self._colSelRects = []


#
class QtColorchart_(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        self._clsSuper = super(qtCore.QWidget, self)
        self._clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding,
            qtCore.QSizePolicy.Expanding
        )
        #
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding,
            qtCore.QSizePolicy.Expanding
        )
        #
        self.initUi()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            # Press
            self._pressFlag = True
            # Move
            self._moveFlag = True
        elif event.button() == QtCore.Qt.RightButton:
            # Track
            self._trackStartPoint = event.globalPos()
            self._trackFlag = True
            # Zoom
            self._zoomFlag = False
        elif event.button() == QtCore.Qt.MidButton:
            # Circle
            point = event.pos()
            self._circleStartAngle = self.getCircleAngle(point)
            self._circleFlag = True
        # Zoom
        self._zoomFlag = False
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self._pressFlag is True:
                self.cls_colorPoint = event.pos()
                #
                self.update()
            #
            self._moveFlag = True
        elif event.button() == QtCore.Qt.RightButton:
            # Track
            self._xTempTrackOffset = self._xTrackOffset
            self._yTempTrackOffset = self._yTrackOffset
            self._trackFlag = True
        elif event.button() == QtCore.Qt.MidButton:
            # Circle
            self._tempCircleAngle = self._circleAngle
            self._circleFlag = True
        # Zoom
        self._zoomFlag = True
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # Press
            self._pressFlag = False
            # Move
            self._moveFlag = True
            #
            self.cls_colorPoint = event.pos()
            #
            self.update()
        elif event.buttons() == QtCore.Qt.RightButton:
            # Track
            self._trackFlag = True
            point = event.globalPos() - self._trackStartPoint
            self.trackAction(point)
        elif event.buttons() == QtCore.Qt.MidButton:
            # Circle
            self._circleFlag = True
            #
            point = event.pos()
            self.circleAction(point)
    #
    def wheelEvent(self, event):
        if self._zoomFlag is True:
            delta = event.angleDelta().y()
            self.zoomAction(delta)
        #
        self._pressFlag = False
        self._moveFlag = False
        self._circleFlag = False
        self._trackFlag = False
    #
    def resizeEvent(self, event):
        self._pressFlag = False
        self._moveFlag = False
        self._circleFlag = False
        self._trackFlag = False
    #
    def paintEvent(self, event):
        def setDrawColor():
            def setDrawBranch(x, y):
                p = x, y
                if not p in points:
                    points.append(p)
                    colorPoint = qtCore.CLS_point(x, y)
                    if mainColorPath.contains(colorPoint):
                        subPoints = getRegularPolygonPoints(x, y, sideCount, subRadius, side=0)
                        colorPath = qtCore.QPainterPath_()
                        colorPath._addPoints(subPoints)

                        angle = bscMethods.Math2D.getAngleByCoord(x, y, xPos, yPos)
                        length = bscMethods.Math2D.getLengthByCoord(x, y, xPos, yPos)
                        #
                        h = -angle - hOffset
                        #
                        r1 = mainRadius
                        a1 = angle
                        d1 = 360.0 / sideCount
                        d2 = 360.0 / sideCount / 2
                        of = -d2
                        a2 = a1 + of - math.floor(a1 / d1) * d1
                        l = [math.sin(fnc_angle(d1)) / math.cos(fnc_angle(a2)) * r1, r1][a1 % 180 == 0]
                        #
                        s = length / (l - subRadius)
                        s = float(max(min(s, 1.0), 0.0))
                        v = vMult / 100.0
                        v = float(max(min(v, 1.0), 0.0))
                        #
                        r, g, b = qtCore.hsv2rgb(h, s, v)
                        backgroundRgba = r, g, b, 255
                        borderRgba = 0, 0, 0, 255
                        #
                        if self._pressFlag is True or self._moveFlag is True or self._circleFlag is True or self._trackFlag is True:
                            if colorPath.contains(pressPoint):
                                self._rbgColor = r, g, b
                                self._hsvColor = h, s, v
                                self._htmlColor = hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)
                        #
                        painter.setBackgroundRgba(backgroundRgba)
                        painter.setBorderRgba(borderRgba)
                        #
                        painter.setPenWidth(2)
                        painter.drawPath(colorPath)
                        #
                        self.cls_colorPathDic[(r, g, b)] = colorPath, colorPoint
            #
            xPos = width / 2
            yPos = height / 2
            #
            pressPoint = self.cls_colorPoint
            #
            count = self._count
            #
            hOffset = self._circleAngle
            vMult = self._vMult
            #
            side = 16
            sideCount = 6
            #
            mainRadius = min(width, height) / 2 - side
            #
            subRadius = float(mainRadius) / count
            #
            mainPoints = getRegularPolygonPoints(xPos, yPos, sideCount, mainRadius, subRadius / 2)
            mainColorPath = qtCore.QPainterPath_()
            mainColorPath._addPoints(mainPoints)
            #
            xCount = int(count * .75)
            yCount = int(count * .75)
            #
            for xSeq in range(xCount):
                for ySeq in range(yCount):
                    xOffset = fnc_sin(fnc_angle(60)) * subRadius
                    #
                    xSubR = xOffset * xSeq * 2 - xOffset * (ySeq % 2)
                    ySubR = ySeq * subRadius * 1.5
                    #
                    xSubPos = xSubR + xPos
                    _ySubPos = ySubR + yPos
                    #
                    _xSubPos = width / 2 - xSubR
                    ySubPos = height / 2 - ySubR
                    #
                    setDrawBranch(xSubPos, ySubPos)
                    setDrawBranch(_xSubPos, ySubPos)
                    setDrawBranch(xSubPos, _ySubPos)
                    setDrawBranch(_xSubPos, _ySubPos)
        #
        self.cls_colorPathDic = {}
        points = []
        #
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        painter.setRenderHint(painter.Antialiasing)
        #
        width = self.width()
        height = self.height()
        #
        setDrawColor()
        #
        if self._rbgColor is not None:
            textRect = qtCore.CLS_rect(
                8, 8,
                width, height
            )
            #
            painter.setBorderRgba(223, 223, 223, 255)
            painter.setFont(qtCore.qtFont(size=12, weight=75))
            painter.setPenWidth(1)
            painter.drawText(
                textRect,
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop,
                'R : {0}\r\nG : {1}\r\nB : {2}'.format(*self._rbgColor)
            )
            #
            if self._rbgColor in self.cls_colorPathDic:
                selPath, selPoint = self.cls_colorPathDic[self._rbgColor]
                painter.setBackgroundRgba(0, 0, 0, 0)
                painter.setBorderRgba(223, 223, 223, 255)
                #
                painter.setPenWidth(4)
                painter.drawPath(selPath)
                #
                self.cls_colorPoint = selPoint
        if self._rbgColor is not None:
            sh, ss, sv = self._hsvColor
            textRect = qtCore.CLS_rect(
                8, 80,
                width, height
            )
            #
            painter.setBorderRgba(223, 223, 223, 255)
            painter.setFont(qtCore.qtFont(size=12, weight=75))
            painter.setPenWidth(1)
            painter.drawText(
                textRect,
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop,
                'H : {0}\r\nS : {1}\r\nV : {2}'.format(round(sh % 360, 2), round(ss, 2), round(sv, 2))
            )
        if self._htmlColor is not None:
            textRect = qtCore.CLS_rect(
                8, 152,
                width, height
            )
            #
            painter.setBorderRgba(223, 223, 223, 255)
            painter.setFont(qtCore.qtFont(size=12, weight=75))
            painter.setPenWidth(1)
            painter.drawText(
                textRect,
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop,
                '#{}'.format(self._htmlColor)
            )

        # painter.end()  # for pyside2
    #
    def zoomAction(self, delta):
        radix = 3
        #
        self._count = bscMethods.Value.stepTo(
            value=self._count, delta=-delta, step=radix,
            valueRange=(self._countMinimum, self._countMaximum)
        )
        #
        self.update()
    #
    def circleAction(self, point):
        angle_ = self.getCircleAngle(point)
        #
        angle = self._tempCircleAngle + self._circleStartAngle
        angle -= angle_
        #
        if self._circleFlag is True:
            self._circleAngle = angle
        #
        self.update()
    #
    def trackAction(self, point):
        xDelta = point.x()
        yDelta = point.y()
        xRadix = 5.0
        yRadix = 5.0
        self._vMult = bscMethods.Value.stepTo(
            value=self._vMult, delta=-yDelta, step=yRadix,
            valueRange=(self._vMultMinimum, self._vMultMaximum)
        )
        #
        self.update()
    #
    def resizeAction(self, size):
        pass
    #
    def getDragPos(self, xPos, yPos, width, height):
        point = self.cls_colorPoint
        pos0 = self._tempCenterCoord
        #
        width0, height0 = self._tempSize
        #
        scale = float(min(width, height)) / float(min(width0, height0))
        #
        x = point.x()
        y = point.y()
        #
        x -= (pos0[0] - xPos)
        y -= (pos0[1] - yPos)
        return qtCore.CLS_point(x, y)
    #
    def getCircleAngle(self, point):
        width = self.width()
        height = self.height()
        #
        xPos = width / 2
        yPos = height / 2
        #
        x = point.x()
        y = point.y()
        #
        return bscMethods.Math2D.getAngleByCoord(x, y, xPos, yPos)
    #
    def getCurrentRgb(self):
        print self._rbgColor
    #
    def initUi(self):
        self._rbgColor = None
        self._hsvColor = None
        self._htmlColor = None
        #
        self.cls_colorPath = None
        #
        self.cls_colorPathDic = {}
        #
        self._zoomFlag = True
        #
        self._pressFlag = True
        self._moveFlag = False
        #
        self._trackStartPoint = qtCore.CLS_point(0, 0)
        #
        self.cls_colorPoint = qtCore.CLS_point(0, 0)
        self._tempColorPoint = qtCore.CLS_point(0, 0)
        self._tempCenterCoord = 0, 0
        self._tempSize = 240, 240
        #
        self._circleStartAngle = 0.0
        #
        self._circleFlag = False
        #
        self._tempCircleAngle = 0.0
        self._circleAngle = 0.0
        #
        self._trackFlag = False
        self._xTempTrackOffset = 0
        self._yTempTrackOffset = 0
        self._xTrackOffset = 0
        self._yTrackOffset = 0
        #
        self._zoomFlag = True
        #
        self._count = 13
        self._countMaximum = 34
        self._countMinimum = 4
        #
        self._vMult = 100.0
        self._vMultMaximum = 100.0
        self._vMultMinimum = 0.0
    #
    def setUiSize(self):
        self.setMaximumSize(166667, 166667)
        self.setMinimumSize(240, 240)