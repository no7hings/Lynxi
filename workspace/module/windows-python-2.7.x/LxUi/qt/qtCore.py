# coding:utf-8
import sys
#
import re
#
import cgitb
#
from ctypes import wintypes
#
from LxBasic import bscConfigure, bscMethods, bscObjects

from LxScheme import shmOutput
#
from LxUi import uiCore

mod_pyqt5 = bscMethods.PyLoader.reload('PyQt5')
if mod_pyqt5:
    LOAD_INDEX = 0
    from PyQt5 import QtGui, QtCore, QtSvg
    # noinspection PyUnresolvedReferences
    from PyQt5.QtWidgets import *
else:
    LOAD_INDEX = 1
    mod_pyside2 = bscMethods.PyLoader.reload('PySide2')
    if mod_pyside2:
        # noinspection PyUnresolvedReferences
        from PySide2 import QtGui, QtCore, QtSvg
        # noinspection PyUnresolvedReferences
        from PySide2.QtWidgets import *


#
cgitb.enable(format='text')
#
_families = uiCore.Lynxi_Ui_Family_Lis
#
CLS_color = QtGui.QColor
CLS_brush = QtGui.QBrush
CLS_point = QtCore.QPoint
CLS_pointF = QtCore.QPointF
CLS_line = QtCore.QLine
CLS_rect = QtCore.QRect
CLS_rectF = QtCore.QRectF
CLS_polygon = QtGui.QPolygon
CLS_polygonF = QtGui.QPolygonF
CLS_painterPath = QtGui.QPainterPath
CLS_painter = QtGui.QPainter

CLS_pen = QtGui.QPen
CLS_timer = QtCore.QTimer
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
TOOLTIP_TIMER = CLS_timer()
#
none = ''

load_dic = {
    'qtProperty': [
        ("PyQt5.QtCore", "pyqtProperty"),
        ("PySide2.QtCore", "Property")
    ],
    'qtSignal': [
        ("PyQt5.QtCore", "pyqtSignal"),
        ("PySide2.QtCore", "Signal")
    ],
    'qtWrapinstance': [
        ("sip", "wrapinstance"),
        ("shiboken2", "wrapInstance")
    ],
    'qtIsDeleted': [
        ("sip", "isdeleted"),
        ("shiboken2", "isValid")
    ]
}

misplaced_dic = {
        "QtCore.pyqtProperty": "QtCore.Property",
        "QtCore.pyqtSignal": "QtCore.Signal",
        "QtCore.pyqtSlot": "QtCore.Slot",
        "QtCore.QAbstractProxyModel": "QtCore.QAbstractProxyModel",
        "QtCore.QSortFilterProxyModel": "QtCore.QSortFilterProxyModel",
        "QtCore.QStringListModel": "QtCore.QStringListModel",
        "QtCore.QItemSelection": "QtCore.QItemSelection",
        "QtCore.QItemSelectionModel": "QtCore.QItemSelectionModel",
        "QtCore.QItemSelectionRange": "QtCore.QItemSelectionRange",
        "uic.loadUi": "QtCompat.loadUi",
        "sip.wrapinstance": "QtCompat.wrapInstance",
        "sip.unwrapinstance": "QtCompat.getCppPointer",
        "sip.isdeleted": "QtCompat.isValid",
        "QtWidgets.qApp": "QtWidgets.QApplication.instance()",
        "QtCore.QCoreApplication.translate": "QtCompat.translate",
        "QtWidgets.QApplication.translate": "QtCompat.translate",
        "QtCore.qInstallMessageHandler": "QtCompat.qInstallMessageHandler",
        "QtWidgets.QStyleOptionViewItem": "QtCompat.QStyleOptionViewItemV4",
    }


def iconRoot():
    return shmOutput.Directory().icon.server


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


def hsv2rgb(h, s, v, maximum=255):
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
    return hsv2rgb(int(''.join([str(ord(i)).zfill(3) for i in string])), 1, 1, maximum)


def str2rgb(string, maximum=255):
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


# noinspection PyUnusedLocal
def qtSignal(*args):
    module = bscMethods.PyLoader.reload(load_dic[sys._getframe().f_code.co_name][LOAD_INDEX][0])
    categoryString = u'module.{}(*args)'.format(load_dic[sys._getframe().f_code.co_name][LOAD_INDEX][1])
    return eval(categoryString)


# noinspection PyUnusedLocal
def qtWrapinstance(*args):
    module = bscMethods.PyLoader.reload(load_dic[sys._getframe().f_code.co_name][LOAD_INDEX][0])
    categoryString = u'module.{}(*args)'.format(load_dic[sys._getframe().f_code.co_name][LOAD_INDEX][1])
    return eval(categoryString)


# noinspection PyUnusedLocal
def qtIsDeleted(*args):
    module = bscMethods.PyLoader.reload(load_dic[sys._getframe().f_code.co_name][LOAD_INDEX][0])
    categoryString = u'module.{}(*args)'.format(load_dic[sys._getframe().f_code.co_name][LOAD_INDEX][1])
    return eval(categoryString)


# Font
def qtFont(size=8, weight=50, italic=False, underline=False, strikeOut=False, family=_families[0]):
    font = QtGui.QFont()
    font.setPointSize(size)
    font.setFamily(family)
    font.setWeight(weight)
    font.setItalic(italic)
    font.setUnderline(underline)
    font.setWordSpacing(1)
    font.setStrikeOut(strikeOut)
    return font


def _toLxOsIconFile(iconKeyword, ext=u'.png'):
    isMayaIcon = iconKeyword.startswith('maya')
    #
    subLabelString = 'table'
    #
    if iconKeyword:
        if '#' in iconKeyword:
            subLabelString = iconKeyword.split('#')[0]
            iconKeyword = iconKeyword.split('#')[-1]
        if '@' in subLabelString:
            ext = '.' + subLabelString.split('@')[-1]
            subLabelString = subLabelString.split('@')[0]
    else:
        iconKeyword = none
    #
    fileString_ = '{}/{}/{}{}'.format(iconRoot(), subLabelString, iconKeyword, ext)
    #
    if isMayaIcon:
        if bscMethods.OsFile.isExist(fileString_):
            return fileString_
        else:
            return '{}/{}/{}{}'.format(iconRoot(), subLabelString, 'default', ext)
    else:
        return fileString_


def _toLxMayaOsIconFile(mayaNodeType):
    iconFile = _toLxOsIconFile('maya#out_{}'.format(mayaNodeType))
    if bscMethods.OsFile.isExist(iconFile):
        fileString_ = iconFile
    else:
        fileString_ = _toLxOsIconFile('maya#out_default')
    return fileString_


def _toLxMayaOsSvgIconFile(mayaNodeType):
    iconFile = _toLxOsIconFile('maya@svg#{}'.format(mayaNodeType))
    if bscMethods.OsFile.isExist(iconFile):
        fileString_ = iconFile
    else:
        fileString_ = _toLxOsIconFile('maya@svg#{}default')
    return fileString_


def getGradientColor(startPos, endPos, drawDir, isSelected, isHove):
    if isHove:
        startColor = endColor = CLS_color(63, 255, 255, 255)
    else:
        if isSelected is True:
            startColor = endColor = CLS_color(255, 127, 0, 255)
        else:
            if drawDir == 1:
                startColor = CLS_color(63, 255, 127, 255)
                endColor = CLS_color(255, 0, 63, 255)
            else:
                startColor = CLS_color(255, 0, 63, 255)
                endColor = CLS_color(63, 255, 127, 255)
    #
    gradient = QtGui.QLinearGradient(startPos, endPos)
    gradient.setColorAt(0, startColor)
    gradient.setColorAt(1, endColor)
    brush = CLS_brush(gradient)
    pen = CLS_pen(brush, 1)
    #
    return pen, brush


def toGlobalPos(widget):
    op = widget.pos()
    p = widget.mapToGlobal(op)
    return p.x(), p.y()


def mtdTooltipStartModifier(method):
    def subFn(*args):
        def show():
            if uiTip:
                if not hasattr(self, '_tooltipWidget'):
                    self._tooltipWidget = QtTooltipWidget_(self)
                #
                self._tooltipWidget.setTooltip(uiTip)
                self._tooltipWidget.tooltipShow()
                #
                shmOutput.Interface().setTooltipAutoShow(True)
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


def mtdTooltipStopModifier(method):
    def subFn(*args):
        # Class
        self = args[0]
        #
        if hasattr(self, '_tooltipTimer'):
            self._tooltipTimer.stop()
        if hasattr(self, '_tooltipWidget'):
            self._tooltipWidget.hide()
        #
        TOOLTIP_TIMER.start(2000)
        TOOLTIP_TIMER.timeout.connect(closeTooltipAutoShow)
        return method(*args)
    return subFn


def toRgbaStylesheetString(rgba):
    return ', '.join([str(i) for i in rgba])


class QPainterPath_(QtGui.QPainterPath):
    def __init__(self, *args):
        super(QPainterPath_, self).__init__(*args)
        self.setFillRule(QtCore.Qt.WindingFill)
    #
    def _addPoints(self, points):
        points = [CLS_pointF(x, y) for x, y in points]
        self.addPolygon(CLS_polygonF(points))


class QPainter_(QtGui.QPainter, uiCore.UiMtdBasic):
    def __init__(self, *args, **kwargs):
        super(QPainter_, self).__init__(*args, **kwargs)
        #
        self._borderColor = CLS_color(127, 127, 127, 255)
        self._backgroundColor = CLS_color(63, 63, 63, 255)
        #
        self._pen = CLS_pen(self._borderColor)
        self._brush = CLS_brush(self._backgroundColor)
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
        self._backgroundColor = CLS_color(r, g, b, a)
        #
        self._brush = CLS_brush(self._backgroundColor)
        self.setBrush(self._brush)
    #
    def setBrushStyle(self, brushStyle):
        self._brush = CLS_brush(self._backgroundColor)
        self._brush.setStyle(brushStyle)
        self.setBrush(self._brush)
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
        self._borderColor = CLS_color(r, g, b, a)
        #
        self._pen = CLS_pen(self._borderColor)
        self._pen.setCapStyle(QtCore.Qt.RoundCap)
        self._pen.setWidth(1)
        self.setPen(self._pen)
    #
    def setPenStyle(self, penStyle):
        self._pen = CLS_pen(self._borderColor)
        self._pen.setStyle(penStyle)
        self.setPen(self._pen)
    #
    def setPenWidth(self, value):
        self._pen = CLS_pen(self._borderColor)
        self._pen.setWidth(value)
        self.setPen(self._pen)
    #
    def setDrawFrame(self, points):
        points = [CLS_point(x, y) for x, y in points]
        self.drawPolygon(CLS_polygon(points))
    #
    def setDrawDottedFrame(self, rect, backgroundRgba, borderRgba):
        self.setBackgroundRgba(backgroundRgba)
        #
        pen = CLS_pen(CLS_color(*borderRgba))
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
        borderGradient.setColorAt(0, CLS_color(*borderColor0)), borderGradient.setColorAt(1, CLS_color(*borderColor1))
        brush = CLS_brush(borderGradient)
        #
        pen = CLS_pen(brush, 1)
        self.setPen(pen)
        backGroundGradient = QtGui.QLinearGradient(startPos, endPos)
        backGroundGradient.setColorAt(0, CLS_color(*backgroundColor0))
        backGroundGradient.setColorAt(1, CLS_color(*backgroundColor1))
        brush = CLS_brush(backGroundGradient)
        self.setBrush(brush)
        self.drawRect(titleRect)
        self.setBackgroundRgba(0, 0, 0, 0)
        self.drawRect(centralRect)
    #
    def setDrawGradientFrame(self, rect, startPos, endPos, backgroundRgba, borderColors, isSelected, isChecked, isPressHovered, isBackGroundChanged=False):
        self.setBackgroundRgba(backgroundRgba)
        # borderRgba, selectedBorderRgba, hoveBorderRgba = borderColors
        #
        if isSelected:
            if isPressHovered:
                backgroundColor1 = CLS_color(0, 127, 127, 255)
                borderColor1 = CLS_color(63, 255, 255, 255)
            else:
                backgroundColor1 = CLS_color(0, 127, 127, 255)
                borderColor1 = CLS_color(0, 191, 191, 255)
        else:
            if isPressHovered:
                backgroundColor1 = CLS_color(71, 71, 71, 255)
                borderColor1 = CLS_color(127, 127, 127, 255)
            else:
                backgroundColor1 = CLS_color(63, 63, 63, 255)
                borderColor1 = CLS_color(95, 95, 95, 255)
        #
        if isChecked:
            if isPressHovered:
                backgroundColor0 = CLS_color(255, 127, 64, 255)
                borderColor0 = CLS_color(255, 191, 0, 255)
            else:
                backgroundColor0 = CLS_color(255, 127, 64, 255)
                borderColor0 = CLS_color(255, 127, 0, 255)
        else:
            if isPressHovered:
                backgroundColor0 = CLS_color(71, 71, 71, 255)
                borderColor0 = CLS_color(127, 127, 127, 255)
            else:
                backgroundColor0 = CLS_color(63, 63, 63, 255)
                borderColor0 = CLS_color(95, 95, 95, 255)
        #
        if isBackGroundChanged is True:
            backGroundGradient = QtGui.QLinearGradient(startPos, endPos)
            backGroundGradient.setColorAt(0, backgroundColor0)
            backGroundGradient.setColorAt(1, backgroundColor1)
            brush = CLS_brush(backGroundGradient)
            self.setBrush(brush)
        #
        borderGradient = QtGui.QLinearGradient(startPos, endPos)
        borderGradient.setColorAt(0, borderColor0)
        borderGradient.setColorAt(1, borderColor1)
        brush = CLS_brush(borderGradient)
        #
        pen = CLS_pen(brush, 1)
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
        elif isinstance(shape, CLS_rect):
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
        ellipseRect = CLS_rect(x - 1, y - 1, r + 2, r + 2)
        points = [
            self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=90),
            self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=210),
            self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=330),
            self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=90)
        ]
        #
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba(borderRgba)
        #
        self._pen.setWidth(2)
        self.setPen(self._pen)
        self.setRenderHint(self.Antialiasing)
        self.drawEllipse(ellipseRect)
        self.setDrawPath(points)
        #
        return ellipseRect
    #
    def setDrawExpandPattern(self, rect, scale, isExpanded, backgroundRgba, borderRgba):
        self.setRenderHint(self.Antialiasing)
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
                self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=120),
                self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=240),
                self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=360),
                self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=120)
            ]
        else:
            points = [
                self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=90),
                self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=210),
                self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=330),
                self.mtd_raw_ellipse2d.positionAtAngle(center=(x, y), radius=r, angle=90)
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
        xPoints = CLS_pointF(xAxisOffset, height - yAxisOffset - yTrackOffset), CLS_pointF(width - xTrackOffset, height - yAxisOffset - yTrackOffset)
        yPoints = CLS_pointF(xAxisOffset, 0), CLS_pointF(xAxisOffset, height - yAxisOffset - yTrackOffset)
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
                    pen = self._pen
                    pen.setWidth(2)
                    self.setPen(pen)
                else:
                    pen = self._pen
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
                lis.append((CLS_pointF(xPos1, yPos1), CLS_pointF(xPos2, yPos2)))
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
                lis.append((CLS_pointF(xPos1, yPos1), CLS_pointF(xPos2, yPos2)))
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
                    text = bscMethods.Value.toPrettify(
                        (seq - axisSeq) * mult + offset,
                        numberMode
                    )
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
                lis.append(CLS_pointF(xPos, yPos))
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
                lis.append(CLS_pointF(xPos, yPos))
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
            self.setFont(qtFont(size=8, weight=50, family=_families[0]))
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
                        subRect = CLS_rect(xPos + (width - w), yPos, w_, height)
                    else:
                        subRect = CLS_rect(xPos, yPos, w_, height)
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
        self.setRenderHint(self.Antialiasing)
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
        path1 = CLS_painterPath()
        path1.addRoundedRect(CLS_rectF(_xP, _yP, _wP, _hP), 5.0, 5.0, QtCore.Qt.AbsoluteSize)
        path1_ = CLS_painterPath()
        path1_.addRoundedRect(CLS_rectF(_xP + _s, _yP + _s, _wP, _hP), 5.0, 5.0, QtCore.Qt.AbsoluteSize)
        #
        path2 = CLS_painterPath()
        path2_ = CLS_painterPath()
        #
        x1, x2, x3 = _xP + _wP - _w / 4, _xP + _wP + _w / 4, _xP + _wP - _w / 4
        _x1, _x2, _x3 = xPos + side*2 + _w / 2, xPos + side*2, xPos + side*2 + _w / 2
        #
        y1, y2, y3 = _yP, _yP + _w / 2, _yP + _w
        _y1, _y2, _y3 = _yP + _hP - _w, _yP + _hP - _w / 2, _yP + _hP
        if region == 0:
            path2.addPolygon(CLS_polygonF([CLS_pointF(_x1, y1), CLS_pointF(_x2, y2 + 1), CLS_pointF(_x3, y3)]))
            path2_.addPolygon(CLS_polygonF([CLS_pointF(_x1 + _s, y1 + _s), CLS_pointF(_x2 + _s, y2 + _s + 1), CLS_pointF(_x3 + _s, y3 + _s)]))
        elif region == 1:
            path2.addPolygon(CLS_polygonF([CLS_pointF(x1, y1), CLS_pointF(x2, y2), CLS_pointF(x3, y3)]))
            path2_.addPolygon(CLS_polygonF([CLS_pointF(x1 + _s, y1 + _s), CLS_pointF(x2 + _s, y2 + _s), CLS_pointF(x3 + _s, y3 + _s)]))
        elif region == 2:
            path2.addPolygon(CLS_polygonF([CLS_pointF(_x1, _y1), CLS_pointF(_x2, _y2), CLS_pointF(_x3, _y3)]))
            path2_.addPolygon(CLS_polygonF([CLS_pointF(_x1 + _s, _y1 + _s), CLS_pointF(_x2 + _s, _y2 + _s), CLS_pointF(_x3 + _s, _y3 + _s)]))
        else:
            path2.addPolygon(CLS_polygonF([CLS_pointF(x1, _y1), CLS_pointF(x2, _y2 - 1), CLS_pointF(x3, _y3)]))
            path2_.addPolygon(CLS_polygonF([CLS_pointF(x1 + _s, _y1 + _s), CLS_pointF(x2 + _s, _y2 + _s - 1), CLS_pointF(x3 + _s, _y3 + _s)]))
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
        textRect = CLS_rect(_xS, _yS, _wS, _hS)
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
        path1 = CLS_painterPath()
        path2 = CLS_painterPath()
        path1.addRect(CLS_rectF(_xP, _yP, _wP, _hP))
        # Shadow
        path1_ = CLS_painterPath()
        path2_ = CLS_painterPath()
        path1_.addRect(CLS_rectF(_xP + _s - 1, _yP + _s - 1, _wP, _hP))
        #
        x1, x2, x3 = _xP + margin, _xP + margin*2, _xP + margin*3
        _x1, _x2, _x3 = _xP + _wP - margin*3, _xP + _wP - margin*2, _xP + _wP - margin
        #
        y1, y2, y3 = _yP + 1, _yP - margin + 1, _yP + 1
        _y1, _y2, _y3 = _yP + _hP - 1, _yP + _hP + margin - 1, _yP + _hP - 1
        if region == 0:
            path2.addPolygon(CLS_polygonF([CLS_pointF(x1, y1), CLS_pointF(x2, y2), CLS_pointF(x3, y3)]))
            path2_.addPolygon(CLS_polygonF([CLS_pointF(x1 + _s, y1 + _s), CLS_pointF(x2 + _s, y2 + _s), CLS_pointF(x3 + _s, y3 + _s)]))
        elif region == 1:
            path2.addPolygon(CLS_polygonF([CLS_pointF(_x1, y1), CLS_pointF(_x2, y2), CLS_pointF(_x3, y3)]))
            path2_.addPolygon(CLS_polygonF([CLS_pointF(_x1 + _s, y1 + _s), CLS_pointF(_x2 + _s, y2 + _s), CLS_pointF(_x3 + _s, y3 + _s)]))
        elif region == 2:
            path2.addPolygon(CLS_polygonF([CLS_pointF(x1, _y1), CLS_pointF(x2, _y2), CLS_pointF(x3, _y3)]))
            path2_.addPolygon(CLS_polygonF([CLS_pointF(x1 + _s, _y1 + _s), CLS_pointF(x2 + _s, _y2 + _s), CLS_pointF(x3 + _s, _y3 + _s)]))
        else:
            path2.addPolygon(CLS_polygonF([CLS_pointF(_x1, _y1), CLS_pointF(_x2, _y2), CLS_pointF(_x3, _y3)]))
            path2_.addPolygon(CLS_polygonF([CLS_pointF(_x1 + _s, _y1 + _s), CLS_pointF(_x2 + _s, _y2 + _s), CLS_pointF(_x3 + _s, _y3 + _s)]))
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
            points = [CLS_point(x + xOffset, y + yOffset) for x, y in shape]
            self.drawPolygon(CLS_polygon(points))
        elif isinstance(shape, CLS_rect):
            rect = CLS_rect(shape.left() + xOffset, shape.top() + yOffset, shape.width() - 1, shape.height() - 1)
            self.drawRect(rect)
    #
    def setDrawKeyPressMark(self, width, height, key, borderRgba):
        rect = CLS_rect(width - 120 - 4, 0, 120, height - 4)
        #
        self.setBorderRgba(borderRgba)
        self.setFont(qtFont(size=10, weight=75, family=_families[1]))
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
        rectF = CLS_rectF(
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
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba(borderRgba)
        # noinspection PyArgumentEqualDefault
        self.setRenderHint(self.Antialiasing, True)
        self.setPenWidth(2)
        self.drawEllipse(rect)
        self.setRenderHint(self.Antialiasing, False)
        self.drawText(rect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, iconText)
    #
    def setDrawButtonBasic(self, rect, borderWidth, borderRadius, backgroundRgba, borderRgba, borderStyle='outset'):
        p0, p1, p2, p3 = rect.topLeft(), rect.bottomLeft(), rect.bottomRight(), rect.topRight()
        w, h = rect.width(), rect.height()
        cx, cy = p0.x() + w/2, p0.y() + h/2
        #
        angleLis = []
        for p in [p0, p1, p2, p3]:
            a = self.mtd_raw_position_2d.toAngle(
                position0=(p.x(), p.y()),
                position1=(cx, cy)
            )
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
            color.setColorAt(0, CLS_color(br0, bb0, bg0, ba0))
            for seq, a in enumerate(angleLis):
                p = float(a) / float(360)
                if seq == 0:
                    color.setColorAt(p, CLS_color(br1, bb1, bg1, ba1))
                elif seq == 1:
                    color.setColorAt(p - .0125, CLS_color(br1, bb1, bg1, ba1))
                    color.setColorAt(p, CLS_color(br4, bb4, bg4, ba4))
                elif seq == 2:
                    color.setColorAt(p, CLS_color(br4, bb4, bg4, ba4))
                elif seq == 3:
                    color.setColorAt(p - .0125, CLS_color(br3, bb3, bg3, ba3))
                    color.setColorAt(p, CLS_color(br0, bb0, bg0, ba0))
            color.setColorAt(1, CLS_color(br0, bb0, bg0, ba0))
            #
            brush = CLS_brush(color)
            self.setBrush(brush)
            self.drawRoundedRect(rect, borderRadius, borderRadius, QtCore.Qt.AbsoluteSize)
        #
        rect_ = CLS_rect(p0.x() + borderWidth, p0.y() + borderWidth, w - borderWidth*2, h - borderWidth*2)
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
        rectF0 = CLS_rectF(
            x, y,
            w, h
        )
        rectF0_ = CLS_rectF(
            x_, y_,
            w_, h_
        )
        path0 = CLS_painterPath()
        path0.addRoundedRect(rectF0, borderRadius, borderRadius, QtCore.Qt.AbsoluteSize)
        path0_ = CLS_painterPath()
        path0_.addRoundedRect(rectF0_, borderRadius - borderWidth, borderRadius - borderWidth, QtCore.Qt.AbsoluteSize)
        #
        if tabRegion == 1:
            if tabPosition == South or tabPosition == North:
                rectF1 = CLS_rectF(
                    x+w/2, y,
                    w/2+1, h
                )
                rectF1_ = CLS_rectF(
                    x_+w_/2, y_,
                    w_/2+1, h_
                )
            else:
                rectF1 = CLS_rectF(
                    x, y+h/2,
                    w, h/2+1
                )
                rectF1_ = CLS_rectF(
                    x_, y_+h_/2,
                    w_, h_/2+1
                )
        elif tabRegion == 2:
            if tabPosition == South or tabPosition == North:
                rectF1 = CLS_rectF(
                    x, y,
                    w/2+1, h
                )
                rectF1_ = CLS_rectF(
                    x_, y_,
                    w_/2+1, h_
                )
            else:
                rectF1 = CLS_rectF(
                    x, y,
                    w, h/2+1
                )
                rectF1_ = CLS_rectF(
                    x_, y_,
                    w_, h_/2+1
                )
        else:
            rectF1 = rectF0
            rectF1_ = rectF0_
        #
        path1 = CLS_painterPath()
        path1.addRect(rectF1)
        #
        path1_ = CLS_painterPath()
        path1_.addRect(rectF1_)
        #
        self.setBackgroundRgba(borderRgba)
        self.setBorderRgba((0, 0, 0, 0))
        self.drawPath(path0 + path1)
        #
        self.setBackgroundRgba(backgroundRgba)
        self.setBorderRgba((0, 0, 0, 0))
        self.drawPath(path0_ + path1_)


class QThread_(QtCore.QThread):
    started = qtSignal()
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
                ('normal', CLS_color(223, 223, 223, 255)),
                ('keyword', CLS_color(255, 127, 64, 255)),
                ('builtin', CLS_color(127, 127, 255, 255)),
                ('constant', CLS_color(127, 127, 255, 255)),
                ('decorator', CLS_color(255, 255, 64, 255)),
                ('comment', CLS_color(95, 95, 95, 255)),
                ('string', CLS_color(255, 255, 127, 255)),
                ('unicode', CLS_color(64, 159, 127, 255)),
                ('number', CLS_color(96, 159, 191, 255)),
                ('error', CLS_color(255, 0, 63, 255))
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
        self.clsSuper = super(QWidget_, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        #
        self.setStyleSheet(
            'QWidget{border: none}'
            'QWidget{background: rgba(63, 63, 63, 0)}'
        )


class QWidget__(QWidget):
    def __init__(self, *args, **kwargs):
        if LOAD_INDEX is 0:
            self.clsSuper = super(QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QWidget__, self)
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


class QGridLayout_(QGridLayout):
    def __init__(self, *args, **kwargs):
        if LOAD_INDEX is 0:
            self.clsSuper = super(QGridLayout, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QGridLayout_, self)
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
        if LOAD_INDEX is 0:
            self.clsSuper = super(QVBoxLayout, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QVBoxLayout_, self)
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
        if LOAD_INDEX is 0:
            self.clsSuper = super(QHBoxLayout, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QHBoxLayout_, self)
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
        if LOAD_INDEX is 0:
            self.clsSuper = super(QScrollArea, self)
            self.clsSuper.__init__(*args, **kwargs)

            self.setAttribute(QtCore.Qt.WA_TranslucentBackground | QtCore.Qt.WA_TransparentForMouseEvents)
        else:
            self.clsSuper = super(QScrollArea_, self)
            self.clsSuper.__init__(*args, **kwargs)

            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
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
    uiCore.UiMtdBasic
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
            region = self.mtd_raw_position_2d.toRegion(
                position=(xd, yd),
                size=(wd, hd)
            )
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
                xP, yP, region = self.mtd_raw_position_2d.regionTo(
                    position=(xPos, yPos),
                    size=(width, height),
                    maximumSize=(maxWidth, maxHeight),
                    offset=(xOffset, yOffset)
                )
                self._region = region
                #
                if region == 0 or region == 1:
                    _yP = yP - margin - side - __h
                else:
                    _yP = yP + margin + shadowRadius + side + __h
                #
                point = CLS_point(xP, _yP)
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
        self.setFont(qtFont(size=10, weight=75, family=_families[0]))


class QSplitter_(QSplitter):
    def __init__(self, *args):
        if LOAD_INDEX is 0:
            self.clsSuper = super(QSplitter, self)
            self.clsSuper.__init__(*args)
        else:
            self.clsSuper = super(QSplitter_, self)
            self.clsSuper.__init__(*args)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setHandleWidth(2)
        self.setContentsMargins(0, 0, 0, 0)
        #
        self.setStyleSheet(
            'QSplitter{background: rgba(0, 0, 0, 0)}'
            'QSplitter{border: none}'
            'QSplitter::handle{background: rgba(63, 63, 63, 255)}'
            'QSplitter::handle{border: 1px rgba(47, 47, 47, 255) ; border-radius: 1px ; border-style: outset ; margin: 160px 2px 160px 2px}'
        )
        #
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class QCommonStyle_(QCommonStyle):
    def __init__(self):
        if LOAD_INDEX is 0:
            self.clsSuper = super(QCommonStyle, self)
            self.clsSuper.__init__()
        else:
            self.clsSuper = super(QCommonStyle_, self)
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


class QPalette_(QtGui.QPalette):
    def __init__(self, *args):
        if LOAD_INDEX is 0:
            self.clsSuper = super(QtGui.QPalette, self)
            self.clsSuper.__init__(*args)
        else:
            self.clsSuper = super(QPalette_, self)
            self.clsSuper.__init__(*args)
        #
        brush = CLS_brush(CLS_color(63, 127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        #
        brush = CLS_brush(CLS_color(63, 127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        #
        brush = CLS_brush(CLS_color(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        #
        brush = CLS_brush(CLS_color(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        #
        brush = CLS_brush(CLS_color(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)


class QRadioButton_(QRadioButton):
    # noinspection PyArgumentList
    def __init__(self, iconKeyword=None, *args, **kwargs):
        if LOAD_INDEX is 0:
            self.clsSuper = super(QRadioButton, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QRadioButton_, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._uiIconKeyword = 'basic#radioCheck'
        if iconKeyword:
            self._uiIconKeyword = iconKeyword
        #
        self.toggled.connect(self._updateUiStyle)
        self.setFont(qtFont(size=8, weight=50, family=_families[1]))
        #
        self.setUiSize()
        #
        self._updateUiStyle()
    #
    def setNameText(self, explain):
        self.setText(explain)
        self.setMaximumSize(QtCore.QSize(166667, 20))
        self.setMinimumSize(QtCore.QSize(0, 20))
    #
    def setCheckable(self, *args):
        self.clsSuper.setCheckable(*args)
        self._updateUiStyle()
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    #
    def setIconExplain(self, iconKeyword, width=24, height=24):
        self._uiIconKeyword = iconKeyword
        self.setMaximumSize(QtCore.QSize(166667, height))
        self.setMinimumSize(QtCore.QSize(width, height))
        self._updateUiStyle()
    @mtdTooltipStartModifier
    def enterEvent(self, event):
        if self.isCheckable():
            self._setQtPressStyle(HoverState)
    @mtdTooltipStopModifier
    def leaveEvent(self, event):
        self._updateUiStyle()
    #
    def _updateUiStyle(self):
        if self.isCheckable():
            self._setQtPressStyle([UncheckedState, CheckedState][self.isChecked()])
        else:
            self._setQtPressStyle(UncheckableState)
    #
    def _setQtPressStyle(self, state):
        if state is CheckedState:
            self.setStyleSheet(
                '''
                QRadioButton{{background: rgba(63, 63, 63, 0) ; color:rgba(223, 223, 223, 255)}}
                QRadioButton{{border: none}}
                QRadioButton::indicator:checked{{image: url({0})}}
                QRadioButton::indicator:unchecked{{image: url({1})}}
                '''.format(_toLxOsIconFile(self._uiIconKeyword + 'on'), _toLxOsIconFile(self._uiIconKeyword + 'off'))
            )
        elif state is UncheckedState:
            self.setStyleSheet(
                '''
                QRadioButton{{background: rgba(63, 63, 63, 0) ; color:rgba(95, 95, 95, 255)}}
                QRadioButton{{border: none}}
                QRadioButton::indicator:checked{{image: url({0})}}
                QRadioButton::indicator:unchecked{{image: url({1})}}
                '''.format(_toLxOsIconFile(self._uiIconKeyword + 'on'), _toLxOsIconFile(self._uiIconKeyword + 'off'))
            )
        elif state is UncheckableState:
            self.setStyleSheet(
                '''
                QRadioButton{{background: rgba(63, 63, 63, 0) ; color:rgba(95, 95, 95, 255)}}
                QRadioButton{{border: none}}
                QRadioButton::indicator:checked{{image: url({0})}}
                QRadioButton::indicator:unchecked{{image: url({1})}}
                '''.format(_toLxOsIconFile('svg_basic@svg#unused'), _toLxOsIconFile('svg_basic@svg#unused'))
            )
        elif state is HoverState:
            self.setStyleSheet(
                '''
                QRadioButton{{background: rgba(63, 63, 63, 0) ; color:rgba(63, 255, 255, 255)}}
                QRadioButton{{border: none}}
                QRadioButton::indicator:checked{{image: url({0})}}
                QRadioButton::indicator:unchecked{{image: url({1})}}
                '''.format(_toLxOsIconFile(self._uiIconKeyword), _toLxOsIconFile(self._uiIconKeyword))
            )
    #
    def setUiSize(self, width=20, height=20):
        self.setMaximumSize(width, height)
        self.setMinimumSize(width, height)


class QCheckBox_(QCheckBox):
    def __init__(self, iconKeyword=None, *args):
        if LOAD_INDEX is 0:
            self.clsSuper = super(QCheckBox, self)
            self.clsSuper.__init__(*args)
        else:
            self.clsSuper = super(QCheckBox_, self)
            self.clsSuper.__init__(*args)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        if iconKeyword:
            self._uiIconKeyword = iconKeyword
        # noinspection PyUnresolvedReferences
        self.toggled.connect(self._updateUiStyle)
        # noinspection PyArgumentEqualDefault
        self.setFont(qtFont(size=8, weight=50, family=_families[1]))
        #
        self.setUiSize()
        #
        self._updateUiStyle()
    #
    def setNameText(self, explain):
        self.setText(explain)
        self.setMaximumSize(QtCore.QSize(166667, 20))
        self.setMinimumSize(QtCore.QSize(0, 20))
    #
    def setDatum(self, message):
        self.setChecked(message)
    # noinspection PyUnusedLocal
    def setIconExplain(self, iconKeyword, width=24, height=24):
        self._uiIconKeyword = iconKeyword
        self.setMaximumSize(QtCore.QSize(166667, height))
        self.setMinimumSize(QtCore.QSize(0, height))
        self._updateUiStyle()
    #
    def setDirt(self, dirt='left'):
        if dirt == 'left':
            self.setLayoutDirection(QtCore.Qt.LeftToRight)
        elif dirt == 'right':
            self.setLayoutDirection(QtCore.Qt.RightToLeft)
    #
    def setChecked(self, boolean):
        self.clsSuper.setChecked(boolean)
        #
        self._isChecked = boolean
        self._updateUiStyle()
    #
    def setCheckable(self, boolean):
        self.clsSuper.setCheckable(boolean)
        #
        self._isCheckable = boolean
        self._updateUiStyle()
    #
    def isChecked(self):
        if self.isCheckable():
            return self.clsSuper.isChecked()
        else:
            return False
    #
    def setToggledConnect(self, checkBox):
        checkBox.toggled.connect(self.setVisible)
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    @mtdTooltipStartModifier
    def enterEvent(self, event):
        if self.isCheckable():
            self._setQtPressStyle(HoverState)
    @mtdTooltipStopModifier
    def leaveEvent(self, event):
        self._updateUiStyle()
    #
    def datum(self):
        return self.isChecked()
    #
    def _updateUiStyle(self):
        if self.isCheckable():
            self._setQtPressStyle([UncheckedState, CheckedState][self.isChecked()])
        else:
            self._setQtPressStyle(UncheckableState)
    #
    def _setQtPressStyle(self, state):
        if state is CheckedState:
            self.setStyleSheet(
                '''
                QCheckBox{{background: rgba(0,0, 0, 0) ; color:rgba(223, 223, 223, 255)}}
                QCheckBox{{border: none}}
                QCheckBox::indicator:checked{{image: url({0})}}
                QCheckBox::indicator:unchecked{{image: url({1})}}
            '''.format(_toLxOsIconFile(self._uiIconKeyword + 'on'), _toLxOsIconFile(self._uiIconKeyword + 'off'))
            )
        elif state is UncheckedState:
            self.setStyleSheet(
                '''
                QCheckBox{{background: rgba(0, 0, 0, 0) ; color:rgba(95, 95, 95, 255)}}
                QCheckBox{{border: none}}
                QCheckBox::indicator:checked{{image: url({0})}}
                QCheckBox::indicator:unchecked{{image: url({1})}}
            '''.format(_toLxOsIconFile(self._uiIconKeyword + 'on'), _toLxOsIconFile(self._uiIconKeyword + 'off'))
            )
        elif state is UncheckableState:
            self.setStyleSheet(
                '''
                QCheckBox{{background: rgba(0,0, 0, 0) ; color:rgba(95, 95, 95, 255)}}
                QCheckBox{{border: none}}
                QCheckBox::indicator:checked{{image: url({0})}}
                QCheckBox::indicator:unchecked{{image: url({1})}}
            '''.format(_toLxOsIconFile(self._uiIconKeyword + 'Disable'), _toLxOsIconFile(self._uiIconKeyword + 'Disable'))
            )
        elif state is HoverState:
            self.setStyleSheet(
                '''
                QCheckBox{{background: rgba(63, 63, 63, 0) ; color:rgba(63, 255, 255, 255)}}
                QCheckBox{{border: none}}
                QCheckBox::indicator:checked{{image: url({0})}}
                QCheckBox::indicator:unchecked{{image: url({1})}}
            '''.format(_toLxOsIconFile(self._uiIconKeyword), _toLxOsIconFile(self._uiIconKeyword))
            )
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(20, 20))
        self.setMinimumSize(QtCore.QSize(20, 20))
    #
    def initUi(self):
        self._uiIconKeyword = 'basic#boxCheck'
        #
        self._isCheckable = True
        self._isChecked = False


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


def getTooltipDelayTime():
    if shmOutput.Interface().isTooltipAutoShow() is False:
        return bscConfigure.Utility.VAR_ui_time_tooltip_delay
    else:
        return 250


def closeTooltipAutoShow():
    if TOOLTIP_TIMER.isActive():
        shmOutput.Interface().setTooltipAutoShow(False)
        TOOLTIP_TIMER.stop()


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

    if bscMethods.MayaApp.isActive():
        # noinspection PyUnresolvedReferences
        import maya.OpenMayaUI as OpenMayaUI
        # noinspection PyUnresolvedReferences
        window = OpenMayaUI.MQtUtil.mainWindow()
        if window:
            return qtWrapinstance(long(window), QWidget)
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


def nativeEnvFnc(ui, message):
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


def getAppWidgetFilterByCategoryName(categoryName):
    lis = []
    # noinspection PyArgumentList
    widgets = QApplication.allWidgets()
    if widgets:
        for w in widgets:
            if categoryName == w.__class__.__name__:
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
    shadow.setColor(CLS_color(32, 32, 32))
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
    categoryName = args[0].__class__.__name__
    parent = self.parent()
    if parent:
        cs = parent.children()
        if cs:
            for c in cs:
                if categoryName == c.__class__.__name__:
                    lis.append(c)
    #
    if len(lis) > 1:
        lis[0].uiQuit()


#
def uiSetupShowMethod(method):
    def subMethod(*args, **kwargs):
        from LxScheme import shmOutput
        shmOutput.Resource().loadActive()
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
        from LxScheme import shmOutput
        shmOutput.Resource().loadActive()
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
