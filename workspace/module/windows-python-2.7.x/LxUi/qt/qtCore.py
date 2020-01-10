# coding:utf-8
import sys
#
import re
#
import cgitb
#
from ctypes import wintypes
#
from PyQt5 import QtGui, QtCore, QtSvg
#
from PyQt5.QtWidgets import *
#
from LxBasic import bscMethods, bscObjects
#
from LxCore import lxBasic, lxConfigure, lxScheme
#
from LxUi import uiCore
#
cgitb.enable(format='text')
#
_families = uiCore.Lynxi_Ui_Family_Lis
#
cls_color = QtGui.QColor
cls_brush = QtGui.QBrush
cls_point = QtCore.QPoint
cls_pointF = QtCore.QPointF
cls_line = QtCore.QLine
cls_rect = QtCore.QRect
cls_rectF = QtCore.QRectF
cls_polygon = QtGui.QPolygon
cls_polygonF = QtGui.QPolygonF
cls_painter_path = QtGui.QPainterPath
#
ExtendSelectMode = 0
AddSelectMode = 1
SubSelectMode = 2
#
NormalState = 0
HoverState = 1
ActiveState = 2
ChosenState = 3
#
OnState = 4
OffState = 5
#
CheckedState = 6
UncheckedState = 7
UncheckableState = 8
#
SelectedState = 9
UnselectedState = 10
UnselectableState = 11
#
CurrentState = 12
SubSelectedState = 13
#
ExpandedState = 14
UnexpandState = 15
UnexpandableState = 16
#
PressedState = 17
UnpressedState = 18
UnpressableState = 19
#
EnterState = 20
UnenterState = 21
#
NormalStatus = 0
WarningStatus = 1
ErrorStatus = 2
OnStatus = 3
OffStatus = 4
#
NormalFocusStatus = 5
WarningFocusStatus = 6
#
NormalOffStatus = 7
WarningOffStatus = 8
#
LostStatus = 9
#
ListMode = 0
IconMode = 1
FormMode = 2
TreeMode = 3
#
LeftDir = 0
RightDir = 1
#
Horizontal = 0
Vertical = 1
Grid = 2
#
East = 3
West = 7
South = 5
North = 6
#
AlignLeft, AlignHCenter, AlignRight, AlignTop, AlignVCenter, AlignBottom = range(0, 6)
#
SolidBorder = 'solid'
InsetBorder = 'inset'
OutsetBorder = 'outset'
GrooveBorder = 'groove'
RidgeBorder = 'ridge'
#
UiTipTimer = QtCore.QTimer()
#
none = ''


def iconRoot():
    return lxScheme.Directory().icon.server


def capitalize(s):
    return s[0].upper() + s[1:] if s else s


def prettify(s):
    return ' '.join([capitalize(x) for x in re.findall('[a-zA-Z][a-z]*[0-9]*', s)])


def matrix3x3():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def matrix3x3Add(m1, m2):
    m = matrix3x3()
    for row in range(0, 3):
        for col in range(0, 3):
            m[row][col] = m1[row][col] + m2[row][col]
    return m


def matrix3x3Multiply(m1, m2):
    m = matrix3x3()
    for row in range(0, 3):
        for col in range(0, 3):
            m[row][col] = m1[row][0]*m2[0][col] + m1[row][1]*m2[1][col] + m1[row][2]*m2[2][col]
    return m


def setMatrix3x3Identity(m):
    for row in range(3):
        for col in range(0, 3):
            m[row][col] = int(row == col)
    return m


def isRectContainPos(rect, pos):
    boolean = False
    if rect is not None:
        x, y = pos
        #
        x_, y_ = rect.x(), rect.y()
        w_, h_ = rect.width(), rect.height()
        #
        boolean = x_ < x < x_ + w_ and y_ < y < y_ + h_
    return boolean


def toPercent(value, maxValue):
    if maxValue > 0:
        return float(value) / float(maxValue)
    else:
        return 0


# Get Percent
def toShowPercent(maxValue, value, roundCount=3):
    valueRange = 100
    percent = 0
    if value > 0:
        percent = round(float(value) / float([1, maxValue][maxValue > 0]), roundCount) * valueRange
    return percent


def hsvToRgb(h, s, v, maximum=255):
    h = float(h % 360.0)
    s = float(max(min(s, 1.0), 0.0))
    v = float(max(min(v, 1.0), 0.0))
    #
    c = v*s
    x = c*(1 - abs((h / 60.0) % 2 - 1))
    m = v - c
    if 0 <= h < 60:
        r_, g_, b_ = c, x, 0
    elif 60 <= h < 120:
        r_, g_, b_ = x, c, 0
    elif 120 <= h < 180:
        r_, g_, b_ = 0, c, x
    elif 180 <= h < 240:
        r_, g_, b_ = 0, x, c
    elif 240 <= h < 300:
        r_, g_, b_ = x, 0, c
    else:
        r_, g_, b_ = c, 0, x
    #
    if maximum == 255:
        r, g, b = int(round((r_ + m)*maximum)), int(round((g_ + m)*maximum)), int(round((b_ + m)*maximum))
    else:
        r, g, b = float((r_ + m)), float((g_ + m)), float((b_ + m))
    return r, g, b


def getRgbByString_(string, maximum=255):
    return hsvToRgb(int(''.join([str(ord(i)).zfill(3) for i in string])), 1, 1, maximum)


def getRgbByString(string, maximum=255):
    a = int(''.join([str(ord(i)).zfill(3) for i in string]))
    b = a % 3
    i = int(a / 256) % 3
    n = int(a % 256)
    if a % 2:
        if i == 0:
            r, g, b = 64 + 64 * b, n, 0
        elif i == 1:
            r, g, b = 0, 64 + 64 * b, n
        else:
            r, g, b = 0, n, 64 + 64 * b
    else:
        if i == 0:
            r, g, b = 0, n, 64 + 64 * b
        elif i == 1:
            r, g, b = 64 + 64 * b, 0, n
        else:
            r, g, b = 64 + 64 * b, n, 0
    #
    return r / 255.0*maximum, g / 255.0*maximum, b / 255.0*maximum


def getDesktop(*args):
    return QApplication.desktop(*args)


def getDesktopPrimaryRect(*args):
    desktop = QApplication.desktop(*args)
    return desktop.availableGeometry(desktop.primaryScreen())


def getDesktopRect(*args):
    desktop = QApplication.desktop(*args)
    return desktop.rect()


def getCursorPos(*args):
    return QtGui.QCursor.pos(*args)


# noinspection PyArgumentList
def setupApp():
    return QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)


# Signal
def uiSignal(*args):
    return QtCore.pyqtSignal(*args)


# Font
def xFont(size=8, weight=50, italic=False, underline=False, strikeOut=False, family=_families[0]):
    font = QtGui.QFont()
    font.setPointSize(size)
    font.setFamily(family)
    font.setWeight(weight)
    font.setItalic(italic)
    font.setUnderline(underline)
    font.setWordSpacing(1)
    font.setStrikeOut(strikeOut)
    return font


def _toLxOsIconFile(iconKeyword, ext='.png'):
    isMayaIcon = iconKeyword.startswith('maya')
    #
    subLabel = 'table'
    #
    if iconKeyword:
        if '#' in iconKeyword:
            subLabel = iconKeyword.split('#')[0]
            iconKeyword = iconKeyword.split('#')[-1]
        if '@' in subLabel:
            ext = '.' + subLabel.split('@')[-1]
            subLabel = subLabel.split('@')[0]
    else:
        iconKeyword = none
    #
    osFile = '{}/{}/{}{}'.format(iconRoot(), subLabel, iconKeyword, ext)
    #
    if isMayaIcon:
        if lxBasic.isOsExistsFile(osFile):
            return osFile
        else:
            return '{}/{}/{}{}'.format(iconRoot(), subLabel, 'default', ext)
    else:
        return osFile


def _toLxMayaOsIconFile(mayaNodeType):
    iconFile = _toLxOsIconFile('maya#out_{}'.format(mayaNodeType))
    if lxBasic.isOsExistsFile(iconFile):
        osFile = iconFile
    else:
        osFile = _toLxOsIconFile('maya#out_default')
    return osFile


def _toLxMayaOsSvgIconFile(mayaNodeType):
    iconFile = _toLxOsIconFile('maya@svg#{}'.format(mayaNodeType))
    if lxBasic.isOsExistsFile(iconFile):
        osFile = iconFile
    else:
        osFile = _toLxOsIconFile('maya@svg#{}default')
    return osFile


def getGradientColor(startPos, endPos, drawDir, isSelected, isHove):
    if isHove:
        startColor = endColor = cls_color(63, 255, 255, 255)
    else:
        if isSelected is True:
            startColor = endColor = cls_color(255, 127, 0, 255)
        else:
            if drawDir == 1:
                startColor = cls_color(63, 255, 127, 255)
                endColor = cls_color(255, 0, 63, 255)
            else:
                startColor = cls_color(255, 0, 63, 255)
                endColor = cls_color(63, 255, 127, 255)
    #
    gradient = QtGui.QLinearGradient(startPos, endPos)
    gradient.setColorAt(0, startColor)
    gradient.setColorAt(1, endColor)
    brush = QtGui.QBrush(gradient)
    pen = QtGui.QPen(brush, 1)
    #
    return pen, brush


def toGlobalPos(widget):
    op = widget.pos()
    p = widget.mapToGlobal(op)
    return p.x(), p.y()


class QPainterPath_(QtGui.QPainterPath):
    def __init__(self, *args, **kwargs):
        super(QtGui.QPainterPath, self).__init__(*args, **kwargs)
        self.setFillRule(QtCore.Qt.WindingFill)
    #
    def _addPoints(self, points):
        points = [QtCore.QPointF(x, y) for x, y in points]
        self.addPolygon(QtGui.QPolygonF(points))


class QPainter_(
    QtGui.QPainter,
    uiCore.Basic
):
    def __init__(self, *args, **kwargs):
        # noinspection PyArgumentList
        super(QtGui.QPainter, self).__init__(*args, **kwargs)
        #
        self._borderColor = QtGui.QColor(127, 127, 127, 255)
        self._backgroundColor = QtGui.QColor(63, 63, 63, 255)
        #
        self.cls_pen = QtGui.QPen(self._borderColor)
        self.cls_brush = QtGui.QBrush(self._backgroundColor)
    #
    def setBackgroundRgba(self, *args):
        if isinstance(args[0], int) or isinstance(args[0], float):
            assert len(args) == 4
            rgba = args
        elif isinstance(args[0], tuple) or isinstance(args[0], list):
            assert len(args[0]) == 4
            rgba = args[0][0], args[0][1], args[0][2], args[0][3]
        else:
            rgba = 0, 0, 0, 0
        #
        r, g, b, a = min(255, rgba[0]), min(255, rgba[1]), min(255, rgba[2]), min(255, rgba[3])
        self._backgroundColor = QtGui.QColor(r, g, b, a)
        #
        self.cls_brush = QtGui.QBrush(self._backgroundColor)
        self.setBrush(self.cls_brush)
    #
    def setBrushStyle(self, brushStyle):
        self.cls_brush = QtGui.QBrush(self._backgroundColor)
        self.cls_brush.setStyle(brushStyle)
        self.setBrush(self.cls_brush)
    #
    def setBorderRgba(self, *args):
        if isinstance(args[0], int) or isinstance(args[0], float):
            assert len(args) == 4
            rgba = args[0], args[1], args[2], args[3]
        elif isinstance(args[0], tuple) or isinstance(args[0], list):
            assert len(args[0]) == 4
            rgba = args[0][0], args[0][1], args[0][2], args[0][3]
        else:
            rgba = 0, 0, 0, 0
        #
        r, g, b, a = min(255, rgba[0]), min(255, rgba[1]), min(255, rgba[2]), min(255, rgba[3])
        self._borderColor = QtGui.QColor(r, g, b, a)
        #
        self.cls_pen = QtGui.QPen(self._borderColor)
        self.cls_pen.setCapStyle(QtCore.Qt.RoundCap)
        self.cls_pen.setWidth(1)
        self.setPen(self.cls_pen)
    #
    def setPenStyle(self, penStyle):
        self.cls_pen = QtGui.QPen(self._borderColor)
        self.cls_pen.setStyle(penStyle)
        self.setPen(self.cls_pen)
    #
    def setPenWidth(self, value):
        self.cls_pen = QtGui.QPen(self._borderColor)
        self.cls_pen.setWidth(value)
        self.setPen(self.cls_pen)
    #
    def setDrawFrame(self, points):
        points = [QtCore.QPoint(x, y) for x, y in points]
        self.drawPolygon(QtGui.QPolygon(points))
    #
    def setDrawDottedFrame(self, rect, backgroundRgba, borderRgba):
        self.setBackgroundRgba(backgroundRgba)
        #
        pen = QtGui.QPen(QtGui.QColor(*borderRgba))
        pen.setStyle(QtCore.Qt.DashLine)
        self.setPen(pen)
        #
        self.drawRect(rect)
    #
    def setDrawRimFrame(self, titleRect, centralRect, startPos, endPos, isPressCurrent, isChecked, isPressHovered):
        self.setBackgroundRgba(0, 0, 0, 0)
        if (isPressCurrent, isChecked, isPressHovered) == (True, True, True):
            backgroundColor0 = 255, 127, 64, 255
            backgroundColor1 = 63, 127, 255, 255
            borderColor0 = 255, 191, 0, 255
            borderColor1 = 0, 191, 255, 255
        elif (isPressCurrent, isChecked, isPressHovered) == (True, True, False):
            backgroundColor0 = 255, 127, 64, 255
            backgroundColor1 = 63, 127, 255, 255
            borderColor0 = 255, 127, 0, 255
            borderColor1 = 0, 127, 255, 255
        elif (isPressCurrent, isChecked, isPressHovered) == (True, False, True):
            backgroundColor0 = 0, 0, 0, 0
            backgroundColor1 = 63, 127, 255, 255
            borderColor0 = 127, 127, 127, 255
            borderColor1 = 0, 191, 255, 255
        elif (isPressCurrent, isChecked, isPressHovered) == (True, False, False):
            backgroundColor0 = 0, 0, 0, 0
            backgroundColor1 = 63, 127, 255, 255
            borderColor0 = 95, 95, 95, 255
            borderColor1 = 0, 127, 255, 255
        elif (isPressCurrent, isChecked, isPressHovered) == (False, True, True):
            backgroundColor0 = 255, 127, 64, 255
            backgroundColor1 = 0, 0, 0, 0
            borderColor0 = 255, 191, 0, 255
            borderColor1 = 127, 127, 127, 255
        elif (isPressCurrent, isChecked, isPressHovered) == (False, True, False):
            backgroundColor0 = 255, 127, 64, 255
            backgroundColor1 = 0, 0, 0, 0
            borderColor0 = 255, 127, 0, 255
            borderColor1 = 95, 95, 95, 255
        elif (isPressCurrent, isChecked, isPressHovered) == (False, False, True):
            backgroundColor0 = 0, 0, 0, 0
            backgroundColor1 = 0, 0, 0, 0
            borderColor0 = 127, 127, 127, 255
            borderColor1 = 127, 127, 127, 255
        else:
            backgroundColor0 = 0, 0, 0, 0
            backgroundColor1 = 0, 0, 0, 0
            borderColor0 = 0, 0, 0, 0
            borderColor1 = 0, 0, 0, 0
        #
        borderGradient = QtGui.QLinearGradient(startPos, endPos)
        borderGradient.setColorAt(0, cls_color(*borderColor0)), borderGradient.setColorAt(1, cls_color(*borderColor1))
        brush = QtGui.QBrush(borderGradient)
        #
        pen = QtGui.QPen(brush, 1)
        self.setPen(pen)
        backGroundGradient = QtGui.QLinearGradient(startPos, endPos)
        backGroundGradient.setColorAt(0, cls_color(*backgroundColor0))
        backGroundGradient.setColorAt(1, cls_color(*backgroundColor1))
        brush = QtGui.QBrush(backGroundGradient)
        self.setBrush(brush)
        self.drawRect(titleRect)
        self.setBackgroundRgba(0, 0, 0, 0)
        self.drawRect(centralRect)
    #
    def setDrawTreeConnect(self):
        pass
    #
    def setDrawExpandFrame(self, rect, isExpandable, isExpanded, isExpandHovered, hasChild, level):
        self.setBackgroundRgba(0, 0, 0, 0)
        self.setBorderRgba([(127, 127, 127, 255), (0, 191, 191, 255)][isExpandHovered])
        #
        w, h = 8, 8
        if isExpandable:
            x, y = rect.x(), rect.y()
            width, height = rect.width(), rect.height()
            frameRect = cls_rect(
                x + (width - w)/2 - 1, y + (height - h)/2 - 1,
                w, h
            )
            self.drawRect(frameRect)
    #
    def setDrawGradientFrame(self, rect, startPos, endPos, backgroundRgba, borderColors, isSelected, isChecked, isPressHovered, isBackGroundChanged=False):
        self.setBackgroundRgba(backgroundRgba)
        # borderRgba, selectedBorderRgba, hoveBorderRgba = borderColors
        #
        if isSelected:
            if isPressHovered:
                backgroundColor1 = cls_color(0, 127, 127, 255)
                borderColor1 = cls_color(63, 255, 255, 255)
            else:
                backgroundColor1 = cls_color(0, 127, 127, 255)
                borderColor1 = cls_color(0, 191, 191, 255)
        else:
            if isPressHovered:
                backgroundColor1 = cls_color(71, 71, 71, 255)
                borderColor1 = cls_color(127, 127, 127, 255)
            else:
                backgroundColor1 = cls_color(63, 63, 63, 255)
                borderColor1 = cls_color(95, 95, 95, 255)
        #
        if isChecked:
            if isPressHovered:
                backgroundColor0 = cls_color(255, 127, 64, 255)
                borderColor0 = cls_color(255, 191, 0, 255)
            else:
                backgroundColor0 = cls_color(255, 127, 64, 255)
                borderColor0 = cls_color(255, 127, 0, 255)
        else:
            if isPressHovered:
                backgroundColor0 = cls_color(71, 71, 71, 255)
                borderColor0 = cls_color(127, 127, 127, 255)
            else:
                backgroundColor0 = cls_color(63, 63, 63, 255)
                borderColor0 = cls_color(95, 95, 95, 255)
        #
        if isBackGroundChanged is True:
            backGroundGradient = QtGui.QLinearGradient(startPos, endPos)
            backGroundGradient.setColorAt(0, backgroundColor0)
            backGroundGradient.setColorAt(1, backgroundColor1)
            brush = QtGui.QBrush(backGroundGradient)
            self.setBrush(brush)
        #
        borderGradient = QtGui.QLinearGradient(startPos, endPos)
        borderGradient.setColorAt(0, borderColor0)
        borderGradient.setColorAt(1, borderColor1)
        brush = QtGui.QBrush(borderGradient)
        #
        pen = QtGui.QPen(brush, 1)
        self.setPen(pen)
        #
        self.drawRect(rect)
    #
    def setDrawZebraFrame(self, rect):
        pass
    #
    def setDrawPath(self, points):
        path = QPainterPath_()
        path._addPoints(points)
        self.drawPath(path)
        return path
    #
    def setDrawFocusFrame(self, shape, backgroundRgba=None, borderRgba=None):
        if backgroundRgba is None:
            backgroundRgba = 0, 0, 0, 0
        if borderRgba is None:
            borderRgba = 63, 255, 127, 255
        #
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba(borderRgba)
        #
        l_ = 8
        lines = None
        if isinstance(shape, tuple) or isinstance(shape, list):
            (x1, y1), (x2, y2), (x3, y3), (x4, y4) = shape
            lines = (
                ((x1, y1 + l_), (x1, y1), (x1 + l_, y1)),
                ((x2 - l_, y2), (x2, y2), (x2, y2 + l_)),
                ((x3, y3 - l_), (x3, y3), (x3 - l_, y3)),
                ((x4 + l_, y4), (x4, y4), (x4, y4 - l_))
            )
        elif isinstance(shape, QtCore.QRect):
            rect = shape
            #
            p1, p2, p3, p4 = rect.topLeft(), rect.topRight(), rect.bottomRight(), rect.bottomLeft()
            (x1, y1), (x2, y2), (x3, y3), (x4, y4) = (p1.x(), p1.y()), (p2.x(), p2.y()), (p3.x(), p3.y()), (p4.x(), p4.y())
            lines = (
                ((x1, y1 + l_), (x1, y1), (x1 + l_, y1)),
                ((x2 - l_, y2), (x2, y2), (x2, y2 + l_)),
                ((x3, y3 - l_), (x3, y3), (x3 - l_, y3)),
                ((x4 + l_, y4), (x4, y4), (x4, y4 - l_))
            )
        if lines:
            [self.setDrawPath(i) for i in lines]
    #
    def setDrawCrossPattern(self, rect):
        xPos = rect.x()
        yPos = rect.y()
        width = rect.width()
        height = rect.height()
        #
        w = rect.height()
        t = yPos
        l_ = (width - height) + xPos
        r = height + xPos
        b = height + yPos
        #
        cx = (l_ + b) / 2
        cy = (t + r) / 2
        #
        iw = height / 12
        ir = w / 2*.5
        #
        line = (
            (cx - iw, cy - ir),
            (cx + iw, cy - ir),
            (cx + iw, cy - iw),
            (cx + ir, cy - iw),
            (cx + ir, cy + iw),
            (cx + iw, cy + iw),
            (cx + iw, cy + ir),
            (cx - iw, cy + ir),
            (cx - iw, cy + iw),
            (cx - ir, cy + iw),
            (cx - ir, cy - iw),
            (cx - iw, cy - iw),
            (cx - iw, cy - ir)
        )
        self.setDrawPath(line)
    #
    def setDrawPlayPattern(self, rect, scale, backgroundRgba, borderRgba):
        xPos, yPos = rect.x(), rect.y()
        width = rect.width()
        height = rect.height()
        #
        r = height*scale
        x = (width - r) / 2 + xPos
        y = (height - r) / 2 + yPos
        #
        ellipseRect = QtCore.QRect(x - 1, y - 1, r + 2, r + 2)
        points = [
            self.getPointOnEllipse(x, y, r, 90),
            self.getPointOnEllipse(x, y, r, 210),
            self.getPointOnEllipse(x, y, r, 330),
            self.getPointOnEllipse(x, y, r, 90)
        ]
        #
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba(borderRgba)
        #
        self.cls_pen.setWidth(2)
        self.setPen(self.cls_pen)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.drawEllipse(ellipseRect)
        self.setDrawPath(points)
        #
        return ellipseRect
    #
    def setDrawExpandPattern(self, rect, scale, isExpanded, backgroundRgba, borderRgba):
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        #
        xPos, yPos = rect.x(), rect.y()
        width = rect.width()
        height = rect.height()
        #
        r = height*scale
        x = (width - r) / 2 + xPos
        y = (height - r) / 2 + yPos
        #
        if isExpanded is True:
            points = [
                self.getPointOnEllipse(x, y, r, 120),
                self.getPointOnEllipse(x, y, r, 240),
                self.getPointOnEllipse(x, y, r, 360),
                self.getPointOnEllipse(x, y, r, 120)
            ]
        else:
            points = [
                self.getPointOnEllipse(x, y, r, 90),
                self.getPointOnEllipse(x, y, r, 210),
                self.getPointOnEllipse(x, y, r, 330),
                self.getPointOnEllipse(x, y, r, 90)
            ]
        #
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba(borderRgba)
        self.setPenWidth(2)
        #
        path = self.setDrawPath(points)
        return path
    #
    def setDrawAxis(self, width, height, trackOffset, axisOffset, borderRgba):
        xTrackOffset, yTrackOffset = trackOffset
        xAxisOffset, yAxisOffset = axisOffset
        #
        xPoints = QtCore.QPointF(xAxisOffset, height - yAxisOffset - yTrackOffset), QtCore.QPointF(width - xTrackOffset, height - yAxisOffset - yTrackOffset)
        yPoints = QtCore.QPointF(xAxisOffset, 0), QtCore.QPointF(xAxisOffset, height - yAxisOffset - yTrackOffset)
        #
        self.setBackgroundRgba(0, 0, 0, 0)
        self.setBorderRgba(borderRgba)
        #
        self.drawLine(xPoints[0], xPoints[1])
        self.drawLine(yPoints[0], yPoints[1])
    #
    def setDrawGrid(self, width, height, axisDir, gridSize, trackOffset, gridOffset, borderRgba):
        def drawBranch(lines, axisSeq):
            for seq, points in enumerate(lines):
                value = seq - axisSeq + 1
                if value % 100 == 1:
                    pen = self.cls_pen
                    pen.setWidth(2)
                    self.setPen(pen)
                else:
                    pen = self.cls_pen
                    pen.setWidth(1)
                    self.setPen(pen)
                self.drawLine(*points)
        #
        def getHLines():
            lis = []
            for x in range(height / gridSize):
                xPos1 = xGridOffset
                xPos2 = width
                #
                if yAxisDir == -1:
                    yPos1 = yPos2 = height - (gridSize*(x - ySeq) + yGridOffset + yTrackOffset)
                else:
                    yPos1 = yPos2 = gridSize*(x - ySeq) + yGridOffset + yTrackOffset
                #
                lis.append((QtCore.QPointF(xPos1, yPos1), QtCore.QPointF(xPos2, yPos2)))
            return lis
        #
        def getVLines():
            lis = []
            for y in range(width / gridSize):
                xPos1 = xPos2 = gridSize*(y - xSeq) + xGridOffset + xTrackOffset
                #
                if yAxisDir == -1:
                    yPos1 = 0
                    yPos2 = height - yGridOffset
                else:
                    yPos1 = height
                    yPos2 = yGridOffset
                #
                lis.append((QtCore.QPointF(xPos1, yPos1), QtCore.QPointF(xPos2, yPos2)))
            return lis
        #
        if gridSize > 4:
            xAxisDir, yAxisDir = axisDir
            xTrackOffset, yTrackOffset = trackOffset
            xGridOffset, yGridOffset = gridOffset
            xSeq = xTrackOffset / gridSize
            ySeq = yTrackOffset / gridSize
            #
            hLines, vLines = getHLines(), getVLines()
            #
            self.setBackgroundRgba(0, 0, 0, 0)
            self.setBorderRgba(borderRgba)
            #
            drawBranch(hLines, ySeq); drawBranch(vLines, xSeq)
    #
    def setDrawGridMark(self, width, height, axisDir, gridSize, trackOffset, gridOffset, valueMultiple, valueOffset, borderRgba, numberMode):
        def drawBranch(points, axisSeq, mult, offset):
            for seq, point in enumerate(points):
                if (seq - axisSeq) % 5 == 0:
                    text = lxBasic.getShowNumber((seq - axisSeq) * mult + offset, numberMode)
                    self.drawText(point, text)
        #
        def getHPoints():
            lis = []
            for i in range(width / gridSize):
                if yAxisDir == -1:
                    xPos, yPos = gridSize*(i - xSeq) + xGridOffset + xTrackOffset, height
                else:
                    xPos, yPos = gridSize*(i - xSeq) + xGridOffset + xTrackOffset, textHeight
                #
                lis.append(cls_pointF(xPos, yPos))
            #
            return lis
        #
        def getVPoints():
            lis = []
            for i in range(height / gridSize):
                if yAxisDir == -1:
                    xPos, yPos = 0, height - (gridSize*(i - ySeq) + yGridOffset + yTrackOffset)
                else:
                    xPos, yPos = 0, gridSize*(i - ySeq) + yGridOffset + yTrackOffset
                #
                lis.append(cls_pointF(xPos, yPos))
            #
            return lis
        #
        if gridSize > 4:
            textHeight = self.fontMetrics().height()
            #
            xAxisDir, yAxisDir = axisDir
            xTrackOffset, yTrackOffset = trackOffset
            xGridOffset, yGridOffset = gridOffset
            xValueMult, yValueMult = valueMultiple
            xValueOffset, yValueOffset = valueOffset
            xSeq = xTrackOffset / gridSize
            ySeq = yTrackOffset / gridSize
            #
            hPoints, vPoints = getHPoints(), getVPoints()
            #
            self.setBorderRgba(borderRgba)
            self.setFont(xFont(size=8, weight=50, family=_families[0]))
            #
            drawBranch(hPoints, xSeq, xValueMult, xValueOffset); drawBranch(vPoints, ySeq, yValueMult, yValueOffset)
    #
    def setDrawFilterString(self, rect, isRightDir, string, keywordFilterString, explainColor):
        xPos, yPos = rect.x(), rect.y()
        #
        width, height = rect.width(), rect.height()
        #
        textOption = QtCore.Qt.AlignVCenter | QtCore.Qt.AlignVCenter
        #
        normalColor = explainColor
        highlightColor = 255, 127, 64, 255
        if string:
            keywordFilterString = keywordFilterString.lower()
            #
            stringLis = string.lower().split(keywordFilterString)
            [stringLis.insert(seq + seq - 1, keywordFilterString) for seq in range(len(stringLis)) if seq > 0]
            lis = [i for i in stringLis if i]
            if lis:
                index = 0
                w = self.fontMetrics().width(string)
                for i in lis:
                    l_ = len(i)
                    #
                    s = string[index:index + l_]
                    w_ = self.fontMetrics().width(s)
                    #
                    if isRightDir:
                        subRect = QtCore.QRect(xPos + (width - w), yPos, w_, height)
                    else:
                        subRect = QtCore.QRect(xPos, yPos, w_, height)
                    #
                    if i == keywordFilterString:
                        self.setBorderRgba(highlightColor)
                    else:
                        self.setBorderRgba(normalColor)
                    #
                    self.drawText(subRect, textOption, s)
                    #
                    index += l_
                    xPos += w_
    #
    def setDrawToolTip(self, rect, string, margin, shadowRadius, side, region):
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        #
        xPos = rect.x()
        yPos = rect.y()
        #
        width = rect.width()
        height = rect.height()
        #
        _s = shadowRadius
        #
        _w = self.fontMetrics().height() + margin*2 - _s - side*2
        #
        _xP = xPos + margin + side
        _yP = yPos + margin + side
        _wP = width - margin*2 - _s - side*2
        _hP = height - margin*2 - _s - side*2
        #
        path1 = cls_painter_path()
        path1.addRoundedRect(cls_rectF(_xP, _yP, _wP, _hP), 5.0, 5.0, QtCore.Qt.AbsoluteSize)
        path1_ = cls_painter_path()
        path1_.addRoundedRect(cls_rectF(_xP + _s, _yP + _s, _wP, _hP), 5.0, 5.0, QtCore.Qt.AbsoluteSize)
        #
        path2 = cls_painter_path()
        path2_ = cls_painter_path()
        #
        x1, x2, x3 = _xP + _wP - _w / 4, _xP + _wP + _w / 4, _xP + _wP - _w / 4
        _x1, _x2, _x3 = xPos + side*2 + _w / 2, xPos + side*2, xPos + side*2 + _w / 2
        #
        y1, y2, y3 = _yP, _yP + _w / 2, _yP + _w
        _y1, _y2, _y3 = _yP + _hP - _w, _yP + _hP - _w / 2, _yP + _hP
        if region == 0:
            path2.addPolygon(cls_polygonF([cls_pointF(_x1, y1), cls_pointF(_x2, y2 + 1), cls_pointF(_x3, y3)]))
            path2_.addPolygon(cls_polygonF([cls_pointF(_x1 + _s, y1 + _s), cls_pointF(_x2 + _s, y2 + _s + 1), cls_pointF(_x3 + _s, y3 + _s)]))
        elif region == 1:
            path2.addPolygon(cls_polygonF([cls_pointF(x1, y1), cls_pointF(x2, y2), cls_pointF(x3, y3)]))
            path2_.addPolygon(cls_polygonF([cls_pointF(x1 + _s, y1 + _s), cls_pointF(x2 + _s, y2 + _s), cls_pointF(x3 + _s, y3 + _s)]))
        elif region == 2:
            path2.addPolygon(cls_polygonF([cls_pointF(_x1, _y1), cls_pointF(_x2, _y2), cls_pointF(_x3, _y3)]))
            path2_.addPolygon(cls_polygonF([cls_pointF(_x1 + _s, _y1 + _s), cls_pointF(_x2 + _s, _y2 + _s), cls_pointF(_x3 + _s, _y3 + _s)]))
        else:
            path2.addPolygon(cls_polygonF([cls_pointF(x1, _y1), cls_pointF(x2, _y2 - 1), cls_pointF(x3, _y3)]))
            path2_.addPolygon(cls_polygonF([cls_pointF(x1 + _s, _y1 + _s), cls_pointF(x2 + _s, _y2 + _s - 1), cls_pointF(x3 + _s, _y3 + _s)]))
        #
        self.setBorderRgba(0, 0, 0, 64)
        self.setBackgroundRgba(0, 0, 0, 64)
        shadowPath = path1_ + path2_
        #
        self.drawPath(shadowPath)
        #
        self.setBackgroundRgba(255, 255, 255, 255)
        self.setBorderRgba(32, 32, 32, 255)
        #
        framePath = path1 + path2
        self.drawPath(framePath)
        #
        _xS = xPos + margin*2 + side
        _yS = yPos + margin*2 + side
        _wS = width - margin*4 - _s - side*2
        _hS = height - margin*4 - _s - side*2
        #
        textRect = QtCore.QRect(_xS, _yS, _wS, _hS)
        #
        self.drawText(textRect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, string)
    #
    def setDrawMenuFrame(self, rect, margin, side, shadowRadius, region, backgroundRgba, borderRgba):
        xPos, yPos = rect.x(), rect.y()
        #
        width, height = rect.width(), rect.height()
        #
        _s = shadowRadius
        #
        _xP = xPos + margin + side
        _yP = yPos + margin + side
        _wP = width - margin*2 - _s - side*2
        _hP = height - margin*2 - _s - side*2
        # Frame
        path1 = cls_painter_path()
        path2 = cls_painter_path()
        path1.addRect(cls_rectF(_xP, _yP, _wP, _hP))
        # Shadow
        path1_ = cls_painter_path()
        path2_ = cls_painter_path()
        path1_.addRect(cls_rectF(_xP + _s - 1, _yP + _s - 1, _wP, _hP))
        #
        x1, x2, x3 = _xP + margin, _xP + margin*2, _xP + margin*3
        _x1, _x2, _x3 = _xP + _wP - margin*3, _xP + _wP - margin*2, _xP + _wP - margin
        #
        y1, y2, y3 = _yP + 1, _yP - margin + 1, _yP + 1
        _y1, _y2, _y3 = _yP + _hP - 1, _yP + _hP + margin - 1, _yP + _hP - 1
        if region == 0:
            path2.addPolygon(cls_polygonF([cls_pointF(x1, y1), cls_pointF(x2, y2), cls_pointF(x3, y3)]))
            path2_.addPolygon(cls_polygonF([cls_pointF(x1 + _s, y1 + _s), cls_pointF(x2 + _s, y2 + _s), cls_pointF(x3 + _s, y3 + _s)]))
        elif region == 1:
            path2.addPolygon(cls_polygonF([cls_pointF(_x1, y1), cls_pointF(_x2, y2), cls_pointF(_x3, y3)]))
            path2_.addPolygon(cls_polygonF([cls_pointF(_x1 + _s, y1 + _s), cls_pointF(_x2 + _s, y2 + _s), cls_pointF(_x3 + _s, y3 + _s)]))
        elif region == 2:
            path2.addPolygon(cls_polygonF([cls_pointF(x1, _y1), cls_pointF(x2, _y2), cls_pointF(x3, _y3)]))
            path2_.addPolygon(cls_polygonF([cls_pointF(x1 + _s, _y1 + _s), cls_pointF(x2 + _s, _y2 + _s), cls_pointF(x3 + _s, _y3 + _s)]))
        else:
            path2.addPolygon(cls_polygonF([cls_pointF(_x1, _y1), cls_pointF(_x2, _y2), cls_pointF(_x3, _y3)]))
            path2_.addPolygon(cls_polygonF([cls_pointF(_x1 + _s, _y1 + _s), cls_pointF(_x2 + _s, _y2 + _s), cls_pointF(_x3 + _s, _y3 + _s)]))
        #
        self.setBorderRgba(0, 0, 0, 64)
        self.setBackgroundRgba(0, 0, 0, 64)
        shadowPath = path1_ + path2_
        self.drawPath(shadowPath)
        #
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba(borderRgba)
        framePath = path1 + path2
        self.drawPath(framePath)
    #
    def setDrawShadow(self, shape, xOffset, yOffset):
        self.setBorderRgba(0, 0, 0, 64)
        self.setBackgroundRgba(0, 0, 0, 64)
        #
        if isinstance(shape, tuple) or isinstance(shape, list):
            points = [QtCore.QPoint(x + xOffset, y + yOffset) for x, y in shape]
            self.drawPolygon(QtGui.QPolygon(points))
        elif isinstance(shape, QtCore.QRect):
            rect = cls_rect(shape.left() + xOffset, shape.top() + yOffset, shape.width() - 1, shape.height() - 1)
            self.drawRect(rect)
    #
    def setDrawKeyPressMark(self, width, height, key, borderRgba):
        rect = cls_rect(width - 120 - 4, 0, 120, height - 4)
        #
        self.setBorderRgba(borderRgba)
        self.setFont(xFont(size=10, weight=75, family=_families[1]))
        self.drawText(rect, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom, key)
    #
    def setDrawImage(self, rect, osImageFile):
        if osImageFile:
            if osImageFile.endswith('.svg'):
                self._setDrawSvgIcon(rect, osImageFile)
            else:
                pixmap = QtGui.QPixmap(osImageFile)
                self.drawPixmap(
                    rect,
                    pixmap
                )
    #
    def _setDrawSvgIcon(self, rect, osSvgFile):
        rectF = QtCore.QRectF(
            rect.x(), rect.y(),
            rect.width(), rect.height()
        )
        svgRender = QtSvg.QSvgRenderer(osSvgFile)
        svgRender.render(self, rectF)
        #
        pixmap = QtGui.QPixmap()
        pixmap.fill(QtCore.Qt.transparent)
        #
        self.drawPixmap(
            rect, pixmap
        )
    #
    def setDrawIconText(self, rect, iconText, backgroundRgba, borderRgba):
        w, h = rect.width(), rect.height()
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba(borderRgba)
        self.setRenderHint(QtGui.QPainter.Antialiasing, True)
        self.setPenWidth(2)
        self.drawEllipse(rect)
        self.setRenderHint(QtGui.QPainter.Antialiasing, False)
        self.drawText(rect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, iconText)
    #
    def setDrawButtonBasic(self, rect, borderWidth, borderRadius, backgroundRgba, borderRgba, borderStyle='outset'):
        p0, p1, p2, p3 = rect.topLeft(), rect.bottomLeft(), rect.bottomRight(), rect.topRight()
        w, h = rect.width(), rect.height()
        cx, cy = p0.x() + w/2, p0.y() + h/2
        #
        angleLis = []
        for p in [p0, p1, p2, p3]:
            a = self.getAngle(p.x(), p.y(), cx, cy)
            angleLis.append(a)
        #
        br, bb, bg, ba = borderRgba
        br0, bb0, bg0, ba0 = min(br*1.25, 255), min(bb*1.25, 255), min(bg*1.25, 255), ba
        br1, bb1, bg1, ba1 = min(br*1.5, 255), min(bb*1.5, 255), min(bg*1.5, 255), ba
        br3, bb3, bg3, ba3 = min(br*.875, 255), min(bb*.875, 255), min(bg*.875, 255), ba
        br4, bb4, bg4, ba4 = min(br*.725, 255), min(bb*.725, 255), min(bg*.725, 255), ba
        self.setBorderRgba((0, 0, 0, 0))
        if borderStyle == 'solid':
            self.setBackgroundRgba(borderRgba)
            self.drawRoundedRect(
                rect,
                borderRadius, borderRadius,
                QtCore.Qt.AbsoluteSize
            )
        else:
            if borderStyle == 'outset':
                a = 90
            elif borderStyle == 'inset':
                a = -90
            else:
                a = 90
            color = QtGui.QConicalGradient(cx, cy, a)
            color.setColorAt(0, QtGui.QColor(br0, bb0, bg0, ba0))
            for seq, a in enumerate(angleLis):
                p = float(a) / float(360)
                if seq == 0:
                    color.setColorAt(p, QtGui.QColor(br1, bb1, bg1, ba1))
                elif seq == 1:
                    color.setColorAt(p - .0125, QtGui.QColor(br1, bb1, bg1, ba1))
                    color.setColorAt(p, QtGui.QColor(br4, bb4, bg4, ba4))
                elif seq == 2:
                    color.setColorAt(p, QtGui.QColor(br4, bb4, bg4, ba4))
                elif seq == 3:
                    color.setColorAt(p - .0125, QtGui.QColor(br3, bb3, bg3, ba3))
                    color.setColorAt(p, QtGui.QColor(br0, bb0, bg0, ba0))
            color.setColorAt(1, QtGui.QColor(br0, bb0, bg0, ba0))
            #
            brush = QtGui.QBrush(color)
            self.setBrush(brush)
            self.drawRoundedRect(rect, borderRadius, borderRadius, QtCore.Qt.AbsoluteSize)
        #
        rect_ = QtCore.QRect(p0.x() + borderWidth, p0.y() + borderWidth, w - borderWidth*2, h - borderWidth*2)
        self.setBackgroundRgba(backgroundRgba)
        self.drawRoundedRect(
            rect_,
            borderRadius - borderWidth, borderRadius - borderWidth,
            QtCore.Qt.AbsoluteSize
        )
    #
    def setDrawTab(self, rect, borderWidth, borderRadius, backgroundRgba, borderRgba, tabRegion=0, tabPosition=South):
        p0, p1, p2, p3 = rect.topLeft(), rect.bottomLeft(), rect.bottomRight(), rect.topRight()
        x, y = p0.x(), p0.y()
        w, h = rect.width(), rect.height()
        x_, y_ = p0.x() + borderWidth, p0.y() + borderWidth
        w_, h_ = w - borderWidth*2, h - borderWidth*2
        #
        rectF0 = QtCore.QRectF(
            x, y,
            w, h
        )
        rectF0_ = QtCore.QRectF(
            x_, y_,
            w_, h_
        )
        path0 = QtGui.QPainterPath()
        path0.addRoundedRect(rectF0, borderRadius, borderRadius, QtCore.Qt.AbsoluteSize)
        path0_ = QtGui.QPainterPath()
        path0_.addRoundedRect(rectF0_, borderRadius - borderWidth, borderRadius - borderWidth, QtCore.Qt.AbsoluteSize)
        #
        if tabRegion == 1:
            if tabPosition == South or tabPosition == North:
                rectF1 = QtCore.QRectF(
                    x+w/2, y,
                    w/2+1, h
                )
                rectF1_ = QtCore.QRectF(
                    x_+w_/2, y_,
                    w_/2+1, h_
                )
            else:
                rectF1 = QtCore.QRectF(
                    x, y+h/2,
                    w, h/2+1
                )
                rectF1_ = QtCore.QRectF(
                    x_, y_+h_/2,
                    w_, h_/2+1
                )
        elif tabRegion == 2:
            if tabPosition == South or tabPosition == North:
                rectF1 = QtCore.QRectF(
                    x, y,
                    w/2+1, h
                )
                rectF1_ = QtCore.QRectF(
                    x_, y_,
                    w_/2+1, h_
                )
            else:
                rectF1 = QtCore.QRectF(
                    x, y,
                    w, h/2+1
                )
                rectF1_ = QtCore.QRectF(
                    x_, y_,
                    w_, h_/2+1
                )
        else:
            rectF1 = rectF0
            rectF1_ = rectF0_
        #
        path1 = QtGui.QPainterPath()
        path1.addRect(rectF1)
        #
        path1_ = QtGui.QPainterPath()
        path1_.addRect(rectF1_)
        #
        self.setBackgroundRgba(borderRgba)
        self.setBorderRgba((0, 0, 0, 0))
        self.drawPath(path0 + path1)
        #
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba((0, 0, 0, 0))
        self.drawPath(path0_ + path1_)


class TestWidget(QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._pos = West
        if self._pos == West:
            self.setMaximumSize(24, 96)
        elif self._pos == West:
            self.setMaximumSize(24, 96)
    #
    def paintEvent(self, event):
        painter = QPainter_()
        # painter.begin(self)  # fix
        #
        w, h = 96, 24
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        painter.setBackgroundRgba((63, 255, 127, 255))
        # painter.drawRect(QtCore.QRect(xPos, yPos, width, height))
        #
        if self._pos == West:
            rect0 = QtCore.QRect(w-h, 0, h, h)
            rect1 = QtCore.QRect(h, 0, w-h, h)
            painter.rotate(-90)
            painter.translate(-w, 0)
        else:
            rect0 = QtCore.QRect(0, 0, h, h)
            rect1 = QtCore.QRect(h, 0, w - h, h)
            painter.rotate(90)
            painter.translate(0, -h)
        #
        painter.setBackgroundRgba((255, 0, 63, 255))
        painter.setBorderRgba((255, 0, 63, 255))
        painter.drawRect(rect0)
        #
        textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        string = 'Test'
        painter.setBorderRgba((255, 255, 255, 255))
        painter.drawText(
            rect1,
            textOption,
            string
        )

        # painter.end()


class QThread_(QtCore.QThread):
    started = uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QThread_, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._threadIndex = 0
        self._isStarted = False
        self._threadEnable = True
    #
    def setThreadIndex(self, number):
        self._threadIndex = number
    #
    def threadIndex(self):
        return self._threadIndex
    #
    def setStarted(self, boolean):
        if not boolean == self._isStarted:
            self._isStarted = boolean
    #
    def isStarted(self):
        return self._isStarted
    #
    def setThreadEnable(self, boolean):
        self._threadEnable = boolean
    #
    def run(self):
        if self._threadEnable is True:
            self.started.emit()


class xPythonHighlighter(QtGui.QSyntaxHighlighter):
    ruleLis = []
    formatDic = {}
    def __init__(self, *args):
        self.clsSuper = super(xPythonHighlighter, self)
        self.clsSuper.__init__(*args)
        #
        self.initializeFormat()
        self.initializeRule()
    #
    def initializeFormat(self):
        baseFormat = QtGui.QTextCharFormat()
        baseFormat.setFontFamily('Arial Unicode MS')
        baseFormat.setFontPointSize(8)
        for name, color in [
                ('normal', QtGui.QColor(223, 223, 223, 255)),
                ('keyword', QtGui.QColor(255, 127, 64, 255)),
                ('builtin', QtGui.QColor(127, 127, 255, 255)),
                ('constant', QtGui.QColor(127, 127, 255, 255)),
                ('decorator', QtGui.QColor(255, 255, 64, 255)),
                ('comment', QtGui.QColor(95, 95, 95, 255)),
                ('string', QtGui.QColor(255, 255, 127, 255)),
                ('unicode', QtGui.QColor(64, 159, 127, 255)),
                ('number', QtGui.QColor(96, 159, 191, 255)),
                ('error', QtGui.QColor(255, 0, 63, 255))
        ]:
            charFormat = QtGui.QTextCharFormat(baseFormat)
            charFormat.setForeground(color)
            if name in ('keyword', 'decorator'):
                charFormat.setFontWeight(QtGui.QFont.Bold)
            self.formatDic[name] = charFormat
    #
    def initializeRule(self):
        KEYWORDS = [
            'and', 'as', 'assert', 'break', 'class',
            'continue', 'def', 'del', 'elif', 'else', 'except',
            'exec', 'finally', 'for', 'from', 'global', 'if',
            'import', 'in', 'is', 'lambda', 'not', 'or', 'pass',
            'print', 'raise', 'return', 'try', 'while', 'with',
            'yield'
        ]
        #
        BUILTINS = [
            'abs', 'all', 'any', 'basestring', 'bool',
            'callable', 'chr', 'classmethod', 'cmp', 'compile',
            'complex', 'delattr', 'dict', 'dir', 'divmod',
            'enumerate', 'eval', 'execfile', 'exit', 'file',
            'filter', 'float', 'frozenset', 'getattr', 'globals',
            'hasattr', 'hex', 'id', 'int', 'isinstance',
            'issubclass', 'iter', 'len', 'list', 'locals', 'map',
            'max', 'min', 'object', 'oct', 'open', 'ord', 'pow',
            'property', 'range', 'reduce', 'repr', 'reversed',
            'round', 'set', 'setattr', 'slice', 'sorted',
            'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
            'vars', 'zip'
        ]
        #
        CONSTANTS = [
            'False', 'True', 'None', 'NotImplemented',
            'Ellipsis'
        ]
        #
        self.ruleLis.append(
            (QtCore.QRegExp('|'.join([r'\b%s\b' % keyword for keyword in KEYWORDS])), 'keyword')
        )
        self.ruleLis.append(
            (QtCore.QRegExp('|'.join([r'\b%s\b' % builtin for builtin in BUILTINS])), 'builtin')
        )
        self.ruleLis.append(
            (QtCore.QRegExp('|'.join([r'\b%s\b' % constant for constant in CONSTANTS])), 'constant')
        )
        self.ruleLis.append(
            (QtCore.QRegExp(
                r'\b[+-]?[0-9]+[lL]?\b' r'|\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b' r'|\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b'),
             'number')
        )
        self.ruleLis.append(
            (QtCore.QRegExp(r'\b@\w+\b'), 'decorator')
        )
        #
        stringRe = QtCore.QRegExp(r"""(?:'[^']*'|"[^"]*")""")
        stringRe.setMinimal(True)
        self.ruleLis.append(
            (stringRe, 'string')
        )
        self.stringRe = QtCore.QRegExp(r"""(?:"["]".*"["]"|'''.*''')""")
        self.stringRe.setMinimal(True)
        self.ruleLis.append(
            (self.stringRe, 'string')
        )
        #
        unicodeRe = QtCore.QRegExp(r"""(?:u'[^u']*'|u"[^u"]*")""")
        unicodeRe.setMinimal(True)
        self.ruleLis.append(
            (unicodeRe, 'unicode')
        )
        #
        self.tripleSingleRe = QtCore.QRegExp(r"""'''(?!')""")
        self.tripleDoubleRe = QtCore.QRegExp(r'''"""(?!')''')
    #
    def highlightBlock(self, text):
        NORMAL, TRIPLESINGLE, TRIPLEDOUBLE, ERROR = range(4)
        #
        textLength = len(text)
        prevState = self.previousBlockState()
        #
        self.setFormat(0, textLength, self.formatDic['normal'])
        #
        if text.startswith('Traceback') or text.startswith('Error: '):
            self.setCurrentBlockState(ERROR)
            self.setFormat(0, textLength, self.formatDic['error'])
            return
        #
        if prevState == ERROR and not (text.startswith(sys.ps1) or text.startswith('#')):
            self.setCurrentBlockState(ERROR)
            self.setFormat(0, textLength, self.formatDic['error'])
            return
        #
        for r, f in self.ruleLis:
            i = r.indexIn(text)
            while i >= 0:
                length = r.matchedLength()
                self.setFormat(i, length, self.formatDic[f])
                i = r.indexIn(text, i + length)
        #
        if not text:
            pass
        elif text.startswith('#'):
            self.setFormat(0, len(text), self.formatDic['comment'])
        else:
            stack = []
            for i, c in enumerate(text):
                if c in ("'", '"'):
                    if stack and stack[-1] == c:
                        stack.pop()
                    else:
                        stack.append(c)
                elif c == '#' and len(stack) == 0:
                    self.setFormat(i, len(text), self.formatDic['comment'])
                    break
        #
        self.setCurrentBlockState(NORMAL)
        #
        if self.stringRe.indexIn(text) != -1:
            return
        #
        for i, s in [
                (self.tripleSingleRe.indexIn(text), TRIPLESINGLE),
                (self.tripleDoubleRe.indexIn(text), TRIPLEDOUBLE)
        ]:
            if self.previousBlockState() == s:
                if i == -1:
                    i = len(text)
                    self.setCurrentBlockState(s)
                self.setFormat(0, i + 3, self.formatDic['string'])
            elif i > -1:
                self.setCurrentBlockState(s)
                self.setFormat(i, len(text), self.formatDic['string'])


class QWidget_(QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        #
        self.setStyleSheet(
            'QWidget{border: none}'
            'QWidget{background: rgba(63, 63, 63, 0)}'
        )


class UiMainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self._drawFrame = False
    #
    def getHeight(self):
        lis = []
        layout = self.layout()
        if layout is not None:
            count = layout.count()
            if count:
                for i in range(0, count):
                    item = layout.itemAt(i)
                    if item:
                        widget = item.widget()
                        height = widget.height()
                        lis.append(height)
            #
            if lis:
                return sum(lis) + 4
            else:
                return self.minimumSize().height()
    #
    def setDrawFrameEnable(self, boolean):
        self._drawFrame = boolean
        self.update()
    #
    def paintEvent(self, event):
        if self._drawFrame is True:
            painter = QPainter_()
            # painter.begin(self)  # fix

            xPos = 0
            yPos = 0
            offset = 1
            uiShadowRadius = 4
            #
            self._uiBackgroundRgba = 63, 63, 63, 255
            self._uiBorderRgba = 95, 95, 95, 255
            #
            width = self.width() - offset
            height = self.height() - offset
            #
            framePointLis = (
                (xPos, yPos),
                (width + xPos - uiShadowRadius, yPos),
                (width + xPos - uiShadowRadius, height + yPos - uiShadowRadius),
                (xPos, height + yPos - uiShadowRadius),
                (xPos, yPos)
            )
            #
            focusFramePointLis = (
                (xPos, yPos),
                (width + xPos - uiShadowRadius, yPos),
                (width + xPos - uiShadowRadius, height + yPos - uiShadowRadius),
                (xPos, height + yPos - uiShadowRadius),
            )
            painter.setDrawShadow(framePointLis, 3, 3)
            #
            painter.setBorderRgba(self._uiBorderRgba)
            painter.setBackgroundRgba(self._uiBackgroundRgba)
            #
            painter.setDrawPath(framePointLis)
            painter.setDrawFocusFrame(
                focusFramePointLis
            )

            # painter.end()


def getWidgetMinimumHeight(widget):
    lis = []
    layout = widget.layout()
    if layout is not None:
        count = layout.count()
        spacing = layout.spacing()
        if count:
            for i in range(0, count):
                item = layout.itemAt(i)
                if item:
                    wd = item.widget()
                    h = wd.height()
                    lis.append(h)
        #
        if lis:
            return sum(lis) + (count - 1)*spacing
        else:
            return widget.minimumSize().height()
    else:
        return 0


class QGridLayout_(QGridLayout):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QGridLayout, self)
        self.clsSuper.__init__(*args, **kwargs)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(2)
    #
    def setAlignmentX(self, horizontal, vertical):
        if horizontal == 'left':
            self.setAlignment(QtCore.Qt.AlignLeft)
        if horizontal == 'center':
            self.setAlignment(QtCore.Qt.AlignHCenter)
        if horizontal == 'right':
            self.setAlignment(QtCore.Qt.AlignRight)
        if vertical == 'top':
            self.setAlignment(QtCore.Qt.AlignTop)
        if vertical == 'center':
            self.setAlignment(QtCore.Qt.AlignVCenter)
        if vertical == 'bottom':
            self.setAlignment(QtCore.Qt.AlignBottom)


class QVBoxLayout_(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QVBoxLayout, self)
        self.clsSuper.__init__(*args, **kwargs)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(2)
    #
    def setAlignmentX(self, horizontal, vertical):
        if horizontal == 'left':
            self.setAlignment(QtCore.Qt.AlignLeft)
        if horizontal == 'center':
            self.setAlignment(QtCore.Qt.AlignHCenter)
        if horizontal == 'right':
            self.setAlignment(QtCore.Qt.AlignRight)
        if vertical == 'top':
            self.setAlignment(QtCore.Qt.AlignTop)
        if vertical == 'center':
            self.setAlignment(QtCore.Qt.AlignVCenter)
        if vertical == 'bottom':
            self.setAlignment(QtCore.Qt.AlignBottom)


class QHBoxLayout_(QHBoxLayout):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QHBoxLayout, self)
        self.clsSuper.__init__(*args, **kwargs)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(2)
    #
    def setAlignmentX(self, horizontal=none, vertical=none):
        if horizontal == 'left':
            self.setAlignment(QtCore.Qt.AlignLeft)
        elif horizontal == 'center':
            self.setAlignment(QtCore.Qt.AlignHCenter)
        elif horizontal == 'right':
            self.setAlignment(QtCore.Qt.AlignRight)
        if vertical == 'top':
            self.setAlignment(QtCore.Qt.AlignTop)
        elif vertical == 'center':
            self.setAlignment(QtCore.Qt.AlignVCenter)
        elif vertical == 'bottom':
            self.setAlignment(QtCore.Qt.AlignBottom)


class QScrollArea_(QScrollArea):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QScrollArea, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(
            QtCore.Qt.WA_TranslucentBackground | QtCore.Qt.WA_TransparentForMouseEvents
        )
        #
        self.setWidgetResizable(True)
        #
        self.setupUi()
        #
        self.setUiStyle()
    #
    def addWidget(self, widget, width=0):
        self._verticalLayout.addWidget(widget)
        if width:
            widget.setMinimumWidth(width)
            widget.setMaximumWidth(width)
    #
    def setSpacing(self, value):
        self._verticalLayout.setSpacing(value)
    #
    def setScrollBarVisible(self, horizontalVisible, verticalVisible):
        if horizontalVisible == NormalState:
            self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        elif horizontalVisible == OnState:
            self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        elif horizontalVisible == OffState:
            self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        if verticalVisible == NormalState:
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        elif verticalVisible == OnState:
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        elif verticalVisible == OffState:
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    #
    def setUiStyle(self):
        self.setStyleSheet(
            'QScrollArea{background: rgba(0, 0, 0, 0) ; color: rgba(191, 191, 191, 255)}'
            'QScrollArea{border: none}'
        )
        setScrollBarStyle(self)
    #
    def setScrollToBottom(self):
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
    #
    def getHeight(self):
        lis = []
        count = self._verticalLayout.count()
        if count:
            for i in range(0, count):
                item = self._verticalLayout.itemAt(i)
                if item:
                    widget = item.widget()
                    height = widget.height()
                    lis.append(height)
        #
        if lis:
            return sum(lis) + 4
        else:
            return self._verticalLayout.minimumSize().height()
    #
    def setHeight(self, value):
        self.setMinimumHeight(value)
    #
    def setUiSize(self, width, height):
        self.setMaximumSize(width, height)
        self.setMinimumSize(width, height)
    #
    def childItems(self):
        lis = []
        #
        layout = self._verticalLayout
        count = layout.count()
        if count:
            for index in range(count):
                widget = layout.itemAt(index).widget()
                lis.append(widget)
        return lis
    #
    def setupUi(self):
        widget = QWidget_()
        self.setWidget(widget)
        #
        self._verticalLayout = QVBoxLayout_(widget)
        self._verticalLayout.setContentsMargins(0, 0, 0, 0)
        self._verticalLayout.setSpacing(2)
        self._verticalLayout.setAlignment(QtCore.Qt.AlignTop)


# Tool Tip Box
class QtTooltipWidget_(
    QWidget,
    uiCore.Basic
):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QtTooltipWidget_, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        self.setupUi()
    #
    def setTooltip(self, string):
        message = none
        if isinstance(string, list)or isinstance(string, tuple):
            message = '\n'.join(string)
        if isinstance(string, str) or isinstance(string, unicode):
            message = string
        #
        self._datum = message + '\n...'
        #
        self.update()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.hide()
            if hasattr(self.parent(), '_tooltipTimer'):
                self.parent()._tooltipTimer.stop()
    #
    def paintEvent(self, event):
        painter = QPainter_(self)
        # painter.begin(self)  # fix

        painter.setFont(self.font())
        #
        painter.setBorderRgba(self._uiBorderRgba)
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        #
        if self._datum is not None:
            painter.setDrawToolTip(
                self.rect(),
                self._datum,
                self._uiMargin, self._uiShadowRadius, self._uiSide, self._region
            )

        # painter.end()
    #
    def tooltipShow(self):
        parent = self.parent()
        if parent:
            deskPos = getCursorPos()
            deskRect = getDesktopRect()
            #
            xd, yd = deskPos.x(), deskPos.y()
            wd, hd = deskRect.width(), deskRect.height()
            #
            region = self.getUiRegion(xd, yd, wd, hd)
            #
            op = parent.pos()
            p = parent.mapToGlobal(op)
            w, h = parent.width(), parent.height()
            #
            x_, y_ = p.x() - op.x(), p.y() - op.y()
            if region == 0 or region == 2:
                x_ += w
            #
            self.uiShow(x_, y_)
    #
    def uiShow(self, xPos=None, yPos=None):
        deskPos = getCursorPos()
        deskRect = getDesktopRect()
        #
        parent = self.parent()
        if parent:
            if xPos is None:
                xPos = deskPos.x()
            if yPos is None:
                yPos = deskPos.y()
            #
            maxWidth, maxHeight = deskRect.width(), deskRect.height()
            #
            xOffset = 4
            yOffset = 0
            #
            side = self._uiSide
            margin = self._uiMargin
            shadowRadius = self._uiShadowRadius
            #
            if self._datum is not None:
                width = self.getUiStrWidth(self, self._datum) + margin*4 + shadowRadius + side*2
                #
                _h = self.fontMetrics().height()
                __h = (_h + margin*2 - shadowRadius - side*2) / 2
                #
                height = len(self._datum.split('\n'))*_h + margin*4 + shadowRadius
                #
                xP, yP, region = self.getRegionPos(
                    xPos, yPos,
                    maxWidth, maxHeight,
                    width, height,
                    xOffset, yOffset
                )
                self._region = region
                #
                if region == 0 or region == 1:
                    _yP = yP - margin - side - __h
                else:
                    _yP = yP + margin + shadowRadius + side + __h
                #
                point = QtCore.QPoint(xP, _yP)
                #
                self.setGeometry(point.x(), point.y(), width, height)
                self.show()
    #
    def setUiSize(self, width, height):
        self.setMaximumSize(width, height)
    #
    def initUi(self):
        self._datum = None
        self._uiNameText = None
        #
        self._uiSide = 2
        self._gap = 16
        self._uiMargin = 8
        self._uiShadowRadius = 2
        #
        self._uiBackgroundRgba = 255, 255, 255, 255
        self._uiBorderRgba = 32, 32, 32, 255
        self._uiNameRgba = 32, 32, 32, 255
        #
        self._uiIconWidth = 16
        self._uiIconHeight = 16
        #
        self._uiFrameWidth = 20
        self._uiFrameHeight = 20
        #
        self._region = 0
    #
    def setupUi(self):
        self.setFont(xFont(size=10, weight=75, family=_families[0]))


class QCommonStyle_(QCommonStyle):
    def __init__(self):
        self.clsSuper = super(QCommonStyle, self)
        self.clsSuper.__init__()
    #
    def drawPrimitive(self, *args):
        element, option, painter, widget = args
        if element == QStyle.PE_FrameFocusRect:
            return
        elif element == QStyle.PE_IndicatorBranch:
            return
        else:
            QCommonStyle().drawPrimitive(element, option, painter, widget)


def getTooltipDelayTime():
    if lxScheme.Shm_Interface().isTooltipAutoShow() is False:
        return lxConfigure.LynxiUi_Value_TooltipDelayTime
    else:
        return 250


def closeTooltipAutoShow():
    if UiTipTimer.isActive():
        lxScheme.Shm_Interface().setTooltipAutoShow(False)
        UiTipTimer.stop()


def uiTooltipStartMethod(method):
    def subFn(*args):
        def show():
            if uiTip:
                if not hasattr(self, '_tooltipWidget'):
                    self._tooltipWidget = QtTooltipWidget_(self)
                #
                self._tooltipWidget.setTooltip(uiTip)
                self._tooltipWidget.tooltipShow()
                #
                lxScheme.Shm_Interface().setTooltipAutoShow(True)
            #
            self._tooltipTimer.stop()
        # Class
        self = args[0]
        #
        if self.isVisible():
            if hasattr(self, 'uiTip'):
                # Tip
                uiTip = self.uiTip
                # Timer
                if not hasattr(self, '_tooltipTimer'):
                    self._tooltipTimer = QtCore.QTimer(self)
                #
                self._tooltipTimer.start(getTooltipDelayTime())
                self._tooltipTimer.timeout.connect(show)
        return method(*args)
    return subFn


def uiTooltipStopMethod(method):
    def subFn(*args):
        # Class
        self = args[0]
        #
        if hasattr(self, '_tooltipTimer'):
            self._tooltipTimer.stop()
        if hasattr(self, '_tooltipWidget'):
            self._tooltipWidget.hide()
        #
        UiTipTimer.start(2000)
        UiTipTimer.timeout.connect(closeTooltipAutoShow)
        return method(*args)
    return subFn


def uiTooltipClearMethod(method):
    def subFn(*args):
        # Class
        self = args[0]
        #
        if hasattr(self, '_tooltipTimer'):
            self._tooltipTimer.stop()
        if hasattr(self, '_tooltipWidget'):
            self._tooltipWidget.hide()
        #
        closeTooltipAutoShow()
        return method(*args)
    return subFn


def getAppWindow():
    # Maya Window

    system = bscObjects.System()
    if system.isMaya:
        # noinspection PyUnresolvedReferences
        import sip
        # noinspection PyUnresolvedReferences
        import maya.OpenMayaUI as OpenMayaUI
        # noinspection PyUnresolvedReferences
        window = OpenMayaUI.MQtUtil.mainWindow()
        if window:
            return sip.wrapinstance(long(window), QtCore.QObject)
    else:
        # noinspection PyArgumentList
        windows = QApplication.allWidgets()
        for i in windows:
            if i.__class__.__name__ == 'QtIf_ToolFloatWindow':
                return i


def getApp():
    # noinspection PyArgumentList
    return QtCore.QCoreApplication.instance()


def getParamX(param):
    return param & 0xffff


def getParamY(param):
    return param >> 16


def nativeEve(ui, message):
    pixel = 8
    msg2 = wintypes.MSG.from_address(message.__int__())
    width = ui.width()
    height = ui.height()
    if msg2.message == 0x0084:
        xPosition = getParamX(msg2.lParam) - ui.frameGeometry().x()
        yPosition = getParamY(msg2.lParam) - ui.frameGeometry().y()
        if xPosition < pixel < yPosition < (height - pixel):
            return True, 10
        elif (width - pixel) < xPosition < (width + pixel) and pixel < yPosition < (height - pixel):
            return True, 11
        elif (width - pixel) > xPosition > pixel > yPosition:
            return True, 12
        elif xPosition < pixel and yPosition < pixel:
            return True, 13
        elif (width - pixel) < xPosition < (width + pixel) and yPosition < pixel:
            return True, 14
        elif pixel < xPosition < (width - pixel) and (height - pixel) < yPosition < (height + pixel):
            return True, 15
        elif xPosition < pixel and (height - pixel) < yPosition:
            return True, 0x10
        elif (width - pixel) < xPosition and (height - pixel) < yPosition:
            return True, 17
    return False, 0


def quitUi():
    if not getAppWindow():
        pass
        # app = getApp()
        # # app.quit()


def setScrollBarStyle(ui):
    uiStyle = '''
        QScrollBar:vertical{{
            background: rgba(56, 56, 56, 255) ;
            width: {2}px ; margin: 0px, 0px, 0px, 0px ; padding: {3}px 0px {3}px 0px ;
            border: 1px  rgba(95, 95, 95, 255) ; border-radius: {1}px ; border-style: solid
        }}
        QScrollBar::handle:vertical{{
            background: rgba(71, 71, 71, 255) ; width: 5px ; min-height: 5px ;
            border: 1px rgba(95, 95, 95, 255) ; border-radius: 0px ; border-style: solid none solid none
        }}
        QScrollBar::handle:vertical:hover{{
            background:rgba(95, 95, 95, 255) ; min-height: 5px ;
            border: 1px  rgba(127, 127, 127, 255) ; border-radius: 0px ; border-style: solid none solid none
        }}
        QScrollBar::add-line:vertical{{
            image: url({0}/svg_basic/vScrollAdd_.svg)
        }}
        QScrollBar::add-line:vertical:hover{{
            image: url({0}/svg_basic/vScrollAdd_On.svg)
        }}
        QScrollBar::sub-line:vertical{{
            image: url({0}/svg_basic/vScrollSub_.svg)
        }}
        QScrollBar::sub-line:vertical:hover{{
            image: url({0}/svg_basic/vScrollSub_On.svg)
        }}
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
            background: none
        }}
        QScrollBar:horizontal{{
            background: rgba(56, 56, 56, 255) ;
            height: {2}px ; margin: 0px, 0px, 0px, 0px ; padding: 0px {3}px 0px {3}px ;
            border: 1px  rgba(95, 95, 95, 255) ; border-radius: {1}px ; border-style: solid
        }}
        QScrollBar::handle:horizontal{{
            background: rgba(71, 71, 71, 255) ; height: 5px ; min-height: 5px ;
            border: 1px  rgba(95, 95, 95, 255) ; border-radius: 0px ; border-style: none solid none solid
        }}
        QScrollBar::handle:horizontal:hover{{
            background: rgba(95, 95, 95, 255) ; min-width: 5px ;
            border: 1px  rgba(127, 127, 127, 255) ; border-radius: 0px ; border-style: none solid none solid
        }}
        QScrollBar::add-line:horizontal{{
            image: url({0}/svg_basic/hScrollAdd_.svg)
        }}
        QScrollBar::add-line:horizontal:hover{{
            image: url({0}/svg_basic/hScrollAdd_On.svg)
        }}
        QScrollBar::sub-line:horizontal{{
            image: url({0}/svg_basic/hScrollSub_.svg)
        }}
        QScrollBar::sub-line:horizontal:hover{{
            image: url({0}/svg_basic/hScrollSub_On.svg)
        }}
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
            background: none
        }}
    '''.format(iconRoot(), 0, 20, 20)
    ui.verticalScrollBar().setStyleSheet(uiStyle)
    ui.horizontalScrollBar().setStyleSheet(uiStyle)


def setTreeWidgetStyle(ui):
    uiStyle = '''
        QTreeWidget{{
            color: rgba(191, 191, 191, 255); background: rgba(63, 63, 63, 255)
        }}
        QTreeWidget{{
            border: none
        }}
        QTreeWidget::item{{
            height: 22px ; margin: 1px 1px 0px 1px
        }}
        QTreeWidget::item:hover{{
            color: rgba(255, 255, 255, 255)
        }}
        QTreeWidget::branch:closed:has-children:has-siblings{{
            border-image: none ; image: url({0}/svg_basic/{1}.svg)
        }}
        QTreeWidget::branch:closed:has-children:has-siblings:hover{{
            border-image: none ; image: url({0}/svg_basic/{1}On.svg)
        }}
        QTreeWidget::branch:closed:has-children:!has-siblings{{
            border-image: none ; image: url({0}/svg_basic/{1}.svg)
        }}
        QTreeWidget::branch:closed:has-children:!has-siblings:hover{{
            border-image: none ; image: url({0}/svg_basic/{1}On.svg)
        }}
        QTreeWidget::branch:open:has-children:has-siblings{{
        border-image: none ; image: url({0}/svg_basic/{2}.svg)
        }}
        QTreeWidget::branch:open:has-children:has-siblings:hover{{
        border-image: none ; image: url({0}/svg_basic/{2}On.svg)
        }}
        QTreeWidget::branch:open:has-children:!has-siblings{{
            border-image: none ; image: url({0}/svg_basic/{2}.svg)
        }}
        QTreeWidget::branch:open:has-children:!has-siblings:hover{{
            border-image: none ; image: url({0}/svg_basic/{2}On.svg)
        }}
    '''.format(
        iconRoot(),
        'expandClose', 'expandOpen'
    )
    ui.setStyleSheet(uiStyle)


def deleteMayaUi(keyword):
    w = getAppWindow()
    if w is not None:
        cs = w.children()
        if cs:
            for i in cs:
                if keyword in str(i):
                    i.uiQuit()


def getAppWidgetFilterByClassName(className):
    lis = []
    # noinspection PyArgumentList
    widgets = QApplication.allWidgets()
    if widgets:
        for w in widgets:
            if className == w.__class__.__name__:
                lis.append(w)
    return lis


#
def getLogWindow():
    w = getAppWindow()
    if w is not None:
        cs = w.children()
        if cs:
            for i in cs:
                if i.__class__.__name__ == 'QtLogWindow':
                    return i


# Shadow
def setShadow(ui, radius=4):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(radius)
    shadow.setColor(QtGui.QColor(32, 32, 32))
    shadow.setOffset(0, 2)
    ui.setGraphicsEffect(shadow)


#
def getUiStrWidth(ui, string):
    linesep = '\n'
    if linesep in string:
        splitData = string.split(linesep)
        values = [ui.fontMetrics().width(i) for i in splitData]
        value = max(values)
    else:
        value = ui.fontMetrics().width(string)
    return value


#
def getUiStrWidthReduce(ui, string, maxiWidth):
    def getIndex():
        width = 0
        for seq, i in enumerate(string):
            subWidth = getUiStrWidth(ui, i)
            width = width + subWidth
            if width >= maxiWidth:
                return seq
    #
    index = getIndex()
    splitIndex = [getIndex(), -1][index is None]
    boolean = getUiStrWidth(ui, string) > maxiWidth
    return [string, string[:splitIndex] + '...'][boolean]


#
def setExistsUiDelete(*args):
    lis = []
    #
    self = args[0]
    className = args[0].__class__.__name__
    parent = self.parent()
    if parent:
        cs = parent.children()
        if cs:
            for c in cs:
                if className == c.__class__.__name__:
                    lis.append(c)
    #
    if len(lis) > 1:
        lis[0].uiQuit()


#
def uiSetupShowMethod(method):
    def subMethod(*args, **kwargs):
        from LxCore import lxScheme
        lxScheme.Shm_Resource().loadActive()
        #
        from LxCore.setup import plugSetup
        plugSetup.setMayaPlugSetup()
        #
        deleteMayaUi(method.__module__)
        #
        return method(*args, **kwargs)
    return subMethod


#
def uiSetupShowMethod_(method):
    def subMethod(*args, **kwargs):
        from LxCore import lxScheme
        lxScheme.Shm_Resource().loadActive()
        #
        from LxCore.setup import plugSetup
        plugSetup.setMayaPlugSetup()
        #
        setExistsUiDelete(*args)
        #
        return method(*args, **kwargs)
    return subMethod


#
def setTreeWidgetKeywordFilter(treeWidget, filterWidget, filterLimitLis=None):
    if treeWidget and filterWidget:
        if filterLimitLis is not None:
            itemLis = filterLimitLis
        else:
            itemLis = treeWidget.treeItems()
        #
        treeWidget.clearSelection()
        #
        filterWidget.setNameText(str(len(itemLis)).zfill(3))
        var = filterWidget.datum()
        if var and itemLis:
            parentItems = []
            for item in itemLis:
                keywordFilterString = item.text(0)
                if hasattr(item, 'name'):
                    text = item.name
                    if text is not None:
                        keywordFilterString = text
                if var.lower() in keywordFilterString.lower():
                    subParentItems = item.parentItems()
                    parentItems.extend(subParentItems)
                    item.setHidden(False)
                else:
                    item.setHidden(True)
            if parentItems:
                [(item.setHidden(False), item.setExpanded(True)) for item in parentItems]
        else:
            [item.setHidden(False) for item in itemLis]
        #
        check = sum([not item.isHidden() for item in itemLis])
        if hasattr(filterWidget, '_setQtPressStyle'):
            if not check:
                filterWidget._setQtPressStyle(ErrorStatus)
            else:
                filterWidget._setQtPressStyle(OnState)
        elif hasattr(filterWidget, 'setUiEnterStatus'):
            if check:
                filterWidget.setUiEnterStatus(NormalStatus)
            else:
                filterWidget.setUiEnterStatus(ErrorStatus)
