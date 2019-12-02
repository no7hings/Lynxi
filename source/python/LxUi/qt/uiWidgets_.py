# coding:utf-8
import cgitb
#
import types
#
from PyQt5 import QtGui, QtCore
#
from PyQt5.QtWidgets import *

from LxCore import lxBasic, lxConfigure
#
from LxUi import uiCore
#
from LxUi.qt.uiBasic import uiWidgetBasic
#
from LxUi.qt import uiWidgets

#
cgitb.enable(format='text')
#
_pen = QtGui.QPen
_color = QtGui.QColor
_brush = QtGui.QBrush
_point = QtCore.QPoint
_pointF = QtCore.QPointF
_line = QtCore.QLine
_rect = QtCore.QRect
_rectF = QtCore.QRectF
_polygon = QtGui.QPolygon
_polygonF = QtGui.QPolygonF
_path = QtGui.QPainterPath
#
_families = lxConfigure.Lynxi_Ui_Family_Lis
#
SolidBorder = 'solid'
InsetBorder = 'inset'
OutsetBorder = 'outset'
GrooveBorder = 'groove'
RidgeBorder = 'ridge'
#
none = ''


# noinspection PyProtectedMember
def uiChooseViewDropMethod(fn):
    def subFn(*args):
        # Class
        self = args[0]
        chooseNames = self._messages
        if chooseNames:
            dropBox = uiWidgetBasic._UiChooseDropView(self)
            dropBox.setCurrentIndex(self.currentIndex)
            dropBox.installEventFilter(self)
            dropBox._viewModel.addItems(chooseNames, self._uiIconKeyword)
            dropBox.setDrop()
        #
        return fn(*args)
    return subFn


#
def uiChooseBoxEventFilterMethod(fn):
    def subFn(*args):
        self = args[0]
        widget_ = args[1]
        event = args[2]
        # Filter by Widget is Press
        if type(widget_) == uiWidgetBasic._UiChooseDropView:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                widget_.close()
                #
                self.chooseChanged.emit()
            # Filter by Widget is Activate
            elif event.type() == QtCore.QEvent.WindowDeactivate:
                widget_.close()
        #
        return fn(*args)
    return subFn


#
def getRgbaStyle(rgba):
    return ', '.join([str(i) for i in rgba])


#
class QPalette_(QtGui.QPalette):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QtGui.QPalette, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        brush = QtGui.QBrush(QtGui.QColor(63, 127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        #
        brush = QtGui.QBrush(QtGui.QColor(63, 127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        #
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        #
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        #
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        self.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        self.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)


#
class xSplitter(QSplitter):
    def __init__(self, *args):
        self.clsSuper = super(xSplitter, self)
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
            'QSplitter::handle{border: 1px rgba(47, 47, 47, 255) ; border-radius: 1px ; border-style: outset ;\
             margin: 160px 2px 160px 2px}'
        )
        #
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


#
class xExplainLabel(QWidget):
    clicked = uiCore.uiSignal()
    doubleClicked = uiCore.uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.initUi()
        #
        self.setUiSize()
    #
    def setNameText(self, string):
        if string:
            self._uiNameText = string
        #
        self.update()
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    @uiCore.uiTooltipStartMethod
    def enterEvent(self, event):
        pass
    @uiCore.uiTooltipStopMethod
    def leaveEvent(self, event):
        pass
    # noinspection PyArgumentList
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
    # noinspection PyArgumentList
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.doubleClicked.emit()
    #
    def setSuperExplain(self, superString):
        self._superExplain = superString
        #
        self.update()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        #
        xPos = 0
        yPos = 0
        #
        width = self.width()
        height = self.height()
        if self._uiNameText is not None:
            painter.setBorderRgba(self._uiNameRgba)
            #
            explainRect = QtCore.QRect(
                xPos + self._uiFrameWidth, yPos, width - self._uiFrameWidth, self._uiFrameHeight
            )
            painter.setFont(uiCore.xFont(size=8, weight=50, family=_families[0]))
            reduceStr = uiCore.getUiStrWidthReduce(painter, self._uiNameText, width - 40)
            painter.drawText(explainRect, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter, reduceStr + self._separator)
        #
        if self._superExplain is not None:
            painter.setBorderRgba(self._superExplainColor)
            #
            explainRect = QtCore.QRect(
                xPos, yPos, width, self._uiFrameHeight
            )
            painter.setFont(uiCore.xFont(size=8, weight=50, family=_families[0]))
            painter.drawText(explainRect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, self._superExplain)
    #
    def _setUiPressStatus(self, status):
        if status is uiCore.NormalStatus:
            self._uiNameRgba = 191, 191, 191, 255
        elif status is uiCore.WarningStatus:
            self._uiNameRgba = 255, 255, 64, 255
        elif status is uiCore.ErrorStatus:
            self._uiNameRgba = 255, 0, 63, 255
        elif status is uiCore.OnStatus:
            self._uiNameRgba = 63, 255, 127, 255
        elif status is uiCore.OffStatus:
            self._uiNameRgba = 95, 95, 95, 255
        #
        self.update()
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(80, 20))
        self.setMinimumSize(QtCore.QSize(80, 20))
    #
    def initUi(self):
        self._uiFrameWidth = 20
        self._uiFrameHeight = 20
        #
        self._uiBackgroundRgba = 63, 63, 63, 0
        self._uiBorderRgba = 63, 63, 63, 0
        self._uiNameRgba = 191, 191, 191, 255
        self._superExplainColor = 0, 191, 191, 255
        #
        self._uiNameText = None
        self._separator = ' : '
        self._superExplain = None


#
class xIconLabel(QWidget):
    clicked = uiCore.uiSignal()
    doubleClicked = uiCore.uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
        #
        self.setUiStyle()
        self.setUiSize()
    @uiCore.uiTooltipStartMethod
    def enterEvent(self, event):
        self._setUiPressStyle(uiCore.HoverState)
    @uiCore.uiTooltipStopMethod
    def leaveEvent(self, event):
        self._updateUiStyle()
    @uiCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
            #
            if self.parent():
                self.parent().mousePressEvent(event)
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self.setMenu()
    @uiCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.doubleClicked.emit()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        #
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side, spacing = self._uiSide, self._uiSpacing
        #
        frameWidth, frameHeight = self._uiFrameWidth, self._uiFrameHeight
        iconWidth, iconHeight = self._uiIconWidth, self._uiIconHeight
        #
        xPos += side
        if self._iconLabel is not None:
            iconOsFile = uiCore._toLxOsIconFile(self._iconLabel)
            #
            if self._subIconLabel is not None:
                rect = QtCore.QRect(
                    xPos, yPos,
                    iconWidth, iconHeight
                )
            else:
                rect = QtCore.QRect(
                    xPos + (frameWidth - iconWidth) / 2, yPos + (frameHeight - iconHeight) / 2,
                    iconWidth, iconHeight
                )
            #
            painter.setDrawImage(rect, iconOsFile)
            if self._subIconLabel is not None:
                iconOsFile = uiCore._toLxOsIconFile(self._subIconLabel)
                #
                rect = QtCore.QRect(
                    xPos + frameWidth - iconWidth*.75, yPos + frameHeight - iconHeight*.75,
                    iconWidth*.75, iconHeight*.75
                )
                painter.setDrawImage(rect, iconOsFile)
        #
        if self._uiMenuIconKeyword is not None:
            w, h = iconWidth * .5, iconHeight * .5
            rect = QtCore.QRect(
                0, 0,
                w, h
            )
            painter.setDrawImage(
                rect,
                uiCore._toLxOsIconFile(self._uiMenuIconKeyword)
            )
        #
        xPos += frameWidth + spacing
    @uiWidgetBasic.uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiWidgetBasic.uiActionViewDropMethod
    def setMenu(self):
        pass
    #
    def _updateUiStyle(self):
        self._setUiPressStyle([uiCore.NormalState, uiCore.OnState][self._isSelected])
    #
    def setNameText(self, string, explainColor=None, explainFont=None):
        if string:
            self._uiNameText = string
        if explainColor:
            self._uiExplainNormalStateColor = explainColor
        if explainFont:
            self._uiExplainFont = explainFont
        #
        self.textLabel.setText(string)
        self.textLabel.setFont(self._uiExplainFont)
        #
        self._updateUiStyle()
    #
    def setIcon(self, iconKeywords, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        if isinstance(iconKeywords, str) or isinstance(iconKeywords, unicode):
            self._iconLabel = iconKeywords
        elif isinstance(iconKeywords, tuple) or isinstance(iconKeywords, list):
            iconKeyword, subIconKeyword = iconKeywords
            self._iconLabel = iconKeyword
            self._subIconLabel = subIconKeyword
        #
        self._uiIconWidth = iconWidth
        self._uiIconHeight = iconHeight
        #
        self._uiFrameWidth = frameWidth
        self._uiFrameHeight = frameHeight
        #
        self.setUiSize()
        #
        self._updateUiStyle()
    #
    def setIconSubLabel(self, string):
        self._iconSubLabel = string
    #
    def setSelected(self, boolean):
        self._isSelected = boolean
        #
        self._updateUiStyle()
    #
    def setTooltip(self, string):
        if string is not None:
            self.uiTip = string
        else:
            self.uiTip = None
    #
    def setActionData(self, actions):
        if actions:
            self.actionData = actions
            self._uiMenuIconKeyword = 'svg_basic@svg#menu_mark'
        else:
            self._uiMenuIconKeyword = None
        #
        self._updateUiStyle()
    #
    def _setUiPressStyle(self, state):
        if state is uiCore.NormalState:
            self._uiNameRgba = self._uiExplainNormalStateColor
        elif state is uiCore.HoverState:
            self._uiNameRgba = 63, 255, 255, 255
        elif state is uiCore.OnState:
            self._uiNameRgba = 255, 127, 64, 255
        #
        uiStyle = '''
            QLabel{{background: rgba(0, 0, 0, 0)}}
            QLabel{{color: rgba({0})}}
            QLabel{{border: none}}
        '''.format(getRgbaStyle(self._uiNameRgba))
        self.textLabel.setStyleSheet(uiStyle)
        #
        self.update()
    #
    def setUiWidth(self, width):
        self.setMaximumWidth(width)
        self.setMinimumWidth(width)
    #
    def setUiStyle(self):
        self.textLabel.setStyleSheet(
            'QLabel{background: rgba(0, 0, 0, 0)}'
            'QLabel{color: rgba(191, 191, 191, 255)}'
            'QLabel{border: none}'
        )
        #
        self._updateUiStyle()
    #
    def setUiSize(self):
        self.setMaximumSize(166667, self._uiFrameHeight)
        self.setMinimumSize(0, self._uiFrameHeight)
    #
    def initUi(self):
        self._uiSide, self._uiSpacing = 2, 2
        self._uiFrameWidth = 20
        self._uiFrameHeight = 20
        #
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 71, 71, 71, 255
        #
        self._isSelected = False
        #
        self._iconLabel = None
        self._iconSubLabel = None
        self._uiMenuIconKeyword = None
        self._subIconLabel = None
        #
        self._uiIconWidth = 16
        self._uiIconHeight = 16
        #
        self._uiNameText = None
        self._uiNameRgba = 191, 191, 191, 255
        self._uiExplainFont = uiCore.xFont(size=8, weight=50, family=_families[0])
        #
        self._uiExplainNormalStateColor = 191, 191, 191, 255
        #
        self.actionData = []
    #
    def setupUi(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(self._uiFrameWidth + self._uiSide + self._uiSpacing, 1, 1, 1)
        layout.setSpacing(0)
        #
        self.textLabel = QLabel()
        layout.addWidget(self.textLabel)
        self.textLabel.setFont(self._uiExplainFont)


#
class QRadioButton_(QRadioButton):
    # noinspection PyArgumentList
    def __init__(self, iconKeyword=None, *args, **kwargs):
        self.clsSuper = super(QRadioButton_, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._uiIconKeyword = 'basic#radioCheck'
        if iconKeyword:
            self._uiIconKeyword = iconKeyword
        #
        self.toggled.connect(self._updateUiStyle)
        self.setFont(uiCore.xFont(size=8, weight=50, family=_families[1]))
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
    @uiCore.uiTooltipStartMethod
    def enterEvent(self, event):
        if self.isCheckable():
            self._setUiPressStyle(uiCore.HoverState)
    @uiCore.uiTooltipStopMethod
    def leaveEvent(self, event):
        self._updateUiStyle()
    #
    def _updateUiStyle(self):
        if self.isCheckable():
            self._setUiPressStyle([uiCore.UncheckedState, uiCore.CheckedState][self.isChecked()])
        else:
            self._setUiPressStyle(uiCore.UncheckableState)
    #
    def _setUiPressStyle(self, state):
        if state is uiCore.CheckedState:
            self.setStyleSheet(
                '''
                QRadioButton{{background: rgba(63, 63, 63, 0) ; color:rgba(223, 223, 223, 255)}}
                QRadioButton{{border: none}}
                QRadioButton::indicator:checked{{image: url({0})}}
                QRadioButton::indicator:unchecked{{image: url({1})}}
                '''.format(uiCore._toLxOsIconFile(self._uiIconKeyword + 'on'), uiCore._toLxOsIconFile(self._uiIconKeyword + 'off'))
            )
        elif state is uiCore.UncheckedState:
            self.setStyleSheet(
                '''
                QRadioButton{{background: rgba(63, 63, 63, 0) ; color:rgba(95, 95, 95, 255)}}
                QRadioButton{{border: none}}
                QRadioButton::indicator:checked{{image: url({0})}}
                QRadioButton::indicator:unchecked{{image: url({1})}}
                '''.format(uiCore._toLxOsIconFile(self._uiIconKeyword + 'on'), uiCore._toLxOsIconFile(self._uiIconKeyword + 'off'))
            )
        elif state is uiCore.UncheckableState:
            self.setStyleSheet(
                '''
                QRadioButton{{background: rgba(63, 63, 63, 0) ; color:rgba(95, 95, 95, 255)}}
                QRadioButton{{border: none}}
                QRadioButton::indicator:checked{{image: url({0})}}
                QRadioButton::indicator:unchecked{{image: url({1})}}
                '''.format(uiCore._toLxOsIconFile('svg_basic@svg#unused'), uiCore._toLxOsIconFile('svg_basic@svg#unused'))
            )
        elif state is uiCore.HoverState:
            self.setStyleSheet(
                '''
                QRadioButton{{background: rgba(63, 63, 63, 0) ; color:rgba(63, 255, 255, 255)}}
                QRadioButton{{border: none}}
                QRadioButton::indicator:checked{{image: url({0})}}
                QRadioButton::indicator:unchecked{{image: url({1})}}
                '''.format(uiCore._toLxOsIconFile(self._uiIconKeyword), uiCore._toLxOsIconFile(self._uiIconKeyword))
            )
    #
    def setUiSize(self, width=20, height=20):
        self.setMaximumSize(width, height)
        self.setMinimumSize(width, height)


#
class xCheckBox(QCheckBox):
    # noinspection PyArgumentList
    def __init__(self, iconKeyword=None, *args, **kwargs):
        self.clsSuper = super(QCheckBox, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        if iconKeyword:
            self._uiIconKeyword = iconKeyword
        #
        self.toggled.connect(self._updateUiStyle)
        self.setFont(uiCore.xFont(size=8, weight=50, family=_families[1]))
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
    #
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
    @uiCore.uiTooltipStartMethod
    def enterEvent(self, event):
        if self.isCheckable():
            self._setUiPressStyle(uiCore.HoverState)
    @uiCore.uiTooltipStopMethod
    def leaveEvent(self, event):
        self._updateUiStyle()
    #
    def datum(self):
        return self.isChecked()
    #
    def _updateUiStyle(self):
        if self.isCheckable():
            self._setUiPressStyle([uiCore.UncheckedState, uiCore.CheckedState][self.isChecked()])
        else:
            self._setUiPressStyle(uiCore.UncheckableState)
    #
    def _setUiPressStyle(self, state):
        if state is uiCore.CheckedState:
            self.setStyleSheet(
                '''
                QCheckBox{{background: rgba(0,0, 0, 0) ; color:rgba(223, 223, 223, 255)}}
                QCheckBox{{border: none}}
                QCheckBox::indicator:checked{{image: url({0})}}
                QCheckBox::indicator:unchecked{{image: url({1})}}
            '''.format(uiCore._toLxOsIconFile(self._uiIconKeyword + 'on'), uiCore._toLxOsIconFile(self._uiIconKeyword + 'off'))
            )
        elif state is uiCore.UncheckedState:
            self.setStyleSheet(
                '''
                QCheckBox{{background: rgba(0, 0, 0, 0) ; color:rgba(95, 95, 95, 255)}}
                QCheckBox{{border: none}}
                QCheckBox::indicator:checked{{image: url({0})}}
                QCheckBox::indicator:unchecked{{image: url({1})}}
            '''.format(uiCore._toLxOsIconFile(self._uiIconKeyword + 'on'), uiCore._toLxOsIconFile(self._uiIconKeyword + 'off'))
            )
        elif state is uiCore.UncheckableState:
            self.setStyleSheet(
                '''
                QCheckBox{{background: rgba(0,0, 0, 0) ; color:rgba(95, 95, 95, 255)}}
                QCheckBox{{border: none}}
                QCheckBox::indicator:checked{{image: url({0})}}
                QCheckBox::indicator:unchecked{{image: url({1})}}
            '''.format(uiCore._toLxOsIconFile(self._uiIconKeyword + 'Disable'), uiCore._toLxOsIconFile(self._uiIconKeyword + 'Disable'))
            )
        elif state is uiCore.HoverState:
            self.setStyleSheet(
                '''
                QCheckBox{{background: rgba(63, 63, 63, 0) ; color:rgba(63, 255, 255, 255)}}
                QCheckBox{{border: none}}
                QCheckBox::indicator:checked{{image: url({0})}}
                QCheckBox::indicator:unchecked{{image: url({1})}}
            '''.format(uiCore._toLxOsIconFile(self._uiIconKeyword), uiCore._toLxOsIconFile(self._uiIconKeyword))
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


#
class xSpacer(QLineEdit):
    # noinspection PyArgumentList
    def __init__(self, *args, **kwargs):
        super(xSpacer, self).__init__(*args, **kwargs)
        self.setReadOnly(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        #
        self.setStyleSheet(
            'QLineEdit{background: rgba(63, 63, 63,0)}'
            'QLineEdit{border: none}')
        #
        self.setMaximumSize(QtCore.QSize(166667, 0))
        self.setMinimumSize(QtCore.QSize(0, 0))


#
class QTextEdit_(QTextEdit):
    entryChanged = uiCore.uiSignal()
    #
    menuWidth = 160
    # noinspection PyArgumentList
    def __init__(self, parent=None, *args, **kwargs):
        self.clsSuper = super(QTextEdit_, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self._parent = parent
        #
        self.isPressMenuEnable = True
        #
        self.contextMenu = None
        #
        self.setUiStyle()
    #
    def enterEvent(self, event):
        if not self.hasFocus() and not self.isReadOnly():
            parent = self._parent
            if parent:
                if hasattr(parent, '_setUiPressStyle'):
                    parent._setUiPressStyle(uiCore.HoverState)
    #
    def leaveEvent(self, event):
        if not self.hasFocus() and not self.isReadOnly():
            parent = self._parent
            if parent:
                if hasattr(parent, '_updateUiStyle'):
                    parent._updateUiStyle()
    #
    def keyPressEvent(self, event):
        self.clsSuper.keyPressEvent(event)
        self.entryChanged.emit()
    #
    def focusInEvent(self, event):
        self.clsSuper.focusInEvent(event)
        if self._parent:
            if not self.isReadOnly():
                self._parent._setUiPressStyle(uiCore.OnState)
    #
    def focusOutEvent(self, event):
        self.clsSuper.focusOutEvent(event)
        if self._parent:
            if self.isReadOnly():
                self._parent._setUiPressStyle(uiCore.OffState)
            if not self.isReadOnly():
                self._parent._setUiPressStyle(uiCore.NormalState)
    @uiWidgetBasic.uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    # noinspection PyArgumentList
    def contextMenuEvent(self, event):
        if self.isPressMenuEnable:
            actions = [
                ('Copy#Ctrl + C', '', True, self.copy),
                ('Paste#Ctrl + V', '', True, self.paste),
                (),
                ('Cut#Ctrl + X', '', True, self.cut),
                (),
                ('Undo#Ctrl + Z', '', True, self.undo),
                ('Redo#Ctrl + Y', '', True, self.redo),
                (),
                ('Select All#Ctrl + A', '', True, self.selectAll)
            ]
            #
            if self.isReadOnly():
                actions = [
                    ('Copy#Ctrl + C', '', True, self.copy),
                    (),
                    ('Select All#Ctrl + A', '', True, self.selectAll)
                ]
            #
            if actions:
                self.contextMenu = uiWidgetBasic._UiActionDropView(self)
                self.contextMenu.setFocusProxy(self)
                self.contextMenu.installEventFilter(self)
                self.contextMenu.setActionData(actions)
                self.contextMenu.setDrop()
    # noinspection PyArgumentList
    def paste(self):
        self.clsSuper.paste()
        #
        self.entryChanged.emit()
    #
    def insertFromMimeData(self, source):
        if source.hasText():
            cursor = self.textCursor()
            cursor.insertText(source.text())
        else:
            self.clsSuper.insertFromMimeData(source)
    #
    def setText(self, *args):
        self.clsSuper.setText(*args)
        self.entryChanged.emit()
    #
    def setEnterEnable(self, boolean):
        self.setReadOnly(not boolean)
    #
    def setEditEnable(self, boolean):
        self.setReadOnly(not boolean)
        self.isPressMenuEnable = boolean
    #
    def setSelectionEnable(self, boolean):
        if boolean is False:
            self.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
    #
    def setUiStyle(self):
        self.setStyleSheet(
            'QTextEdit{background: rgba(0, 0, 0, 0) ; color: rgba(223, 223, 223, 255)}'
            'QTextEdit{border: none}'
            'QTextEdit{selection-color: rgba(255, 255, 255, 255) ; selection-background-color: rgba(0, 127, 127, 255)}'
        )
        uiCore.setScrollBarStyle(self)


#
class xBoxFrame(QWidget):
    frameXPos = 0
    frameYPos = 0
    #
    frameWidth = 0
    frameHeight = 480
    #
    backgroundRgba = 56
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        #
        offset = 2
        #
        xPos = 0
        yPos = self.frameYPos
        #
        width = self.width() - offset
        height = self.frameHeight - offset
        #
        backgroundRect = QtCore.QRect(xPos, yPos, width, height)
        #
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRect(backgroundRect)
    #
    def initUi(self):
        self._uiBackgroundRgba = 56, 56, 56, 255
        self._uiBorderRgba = 95, 95, 95, 255


#
class xTipFrame(QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        self._dragFlag = True
        self._dragStartPoint = QtCore.QPoint(0, 0)
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._dragFlag = True
            self._dragStartPoint = event.globalPos() - self.pos()
    #
    def mouseMoveEvent(self, event):
        if self._dragFlag:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(event.globalPos() - self._dragStartPoint)
    #
    def mouseReleaseEvent(self, event):
        self._dragFlag = False
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        #
        borderRgba = 127
        backgroundRgba = 64
        #
        xPos = 0
        yPos = 0
        gap = 16
        offset = 1
        uiShadowRadius = 4
        #
        width = self.width() - offset
        height = self.height() - offset
        #
        framePointLis = (
            (xPos, yPos),
            (width + xPos - uiShadowRadius, yPos),
            (width + xPos - uiShadowRadius, height + yPos - gap - uiShadowRadius),
            (width - gap * 2 + xPos - uiShadowRadius, height + yPos - gap - uiShadowRadius),
            (width - gap * 2 + xPos - uiShadowRadius, height + yPos - uiShadowRadius),
            (width - gap * 3 + xPos - uiShadowRadius, height + yPos - gap - uiShadowRadius),
            (xPos, height + yPos - gap - uiShadowRadius),
            (xPos, yPos)
        )
        #
        painter.setDrawShadow(framePointLis, 3, 3)
        #
        painter.setBorderRgba(borderRgba, borderRgba, borderRgba, 255)
        painter.setBackgroundRgba(backgroundRgba, backgroundRgba, backgroundRgba, 127)
        painter.setDrawPath(framePointLis)
        #
        focusFramePointLis = (
            (xPos, yPos),
            (width + xPos - uiShadowRadius, yPos),
            (width + xPos - uiShadowRadius, height + yPos - gap - uiShadowRadius),
            (xPos, height + yPos - gap - uiShadowRadius),
        )
        painter.setDrawFocusFrame(focusFramePointLis)


#
class xLineEdit(QLineEdit):
    entryChanged = uiCore.uiSignal()
    #
    clicked = uiCore.uiSignal()
    doubleClicked = uiCore.uiSignal()
    #
    borderWidth = 1
    borderRadius = 10
    borderStyle = InsetBorder
    #
    menuWidth = 160
    # noinspection PyArgumentList
    def __init__(self, parent=None, *args, **kwargs):
        self.clsSuper = super(xLineEdit, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.textChanged.connect(self.entryEvent)
        self.returnPressed.connect(self.entryEvent)
        #
        self._parent = parent
        #
        self.contextMenu = None
        #
        self.initUi()
        #
        self.setUiStyle()
        self.setUiSize()
    # noinspection PyArgumentList
    def mousePressEvent(self, event):
        self.clsSuper.mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
    # noinspection PyArgumentList
    def mouseDoubleClickEvent(self, event):
        self.clsSuper.mouseDoubleClickEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            return self.doubleClicked.emit()
    #
    def focusInEvent(self, event):
        self.clsSuper.focusInEvent(event)
        self._updateUiStyle()
    #
    def focusOutEvent(self, event):
        self.clsSuper.focusOutEvent(event)
        self._updateUiStyle()
    @uiWidgetBasic.uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    # noinspection PyArgumentList
    def contextMenuEvent(self, event):
        actions = [
            ('Copy#Ctrl + C', '', self.isSelected(), self.copy),
            ('Paste#Ctrl + V', '', True, self.paste),
            (),
            ('Cut#Ctrl + X', '', self.isSelected(), self.cut),
            ('Delete', '', self.isSelected(), self.del_),
            (),
            ('Undo#Ctrl + Z', '', True, self.undo),
            ('Redo#Ctrl + Y', '', True, self.redo),
            (),
            ('Select All#Ctrl + A', '', True, self.selectAll)
        ]
        #
        if self.isReadOnly():
            actions = [
                ('Copy#Ctrl + C', '', True, self.copy),
                (),
                ('Select All#Ctrl + A', '', True, self.selectAll)
            ]
        #
        if actions:
            self.contextMenu = uiWidgetBasic._UiActionDropView(self)
            self.contextMenu.setFocusProxy(self)
            self.contextMenu.installEventFilter(self)
            self.contextMenu.setActionData(actions)
            self.contextMenu.setDrop()
    #
    def paste(self):
        self.clsSuper.paste()
        self.entryChanged.emit()
    #
    def del_(self):
        self.clsSuper.del_()
        self.entryChanged.emit()
    #
    def isSelected(self):
        boolean = False
        if self.selectedText():
            boolean = True
        return boolean
    #
    def entryEvent(self):
        self.entryChanged.emit()
    #
    def setEnterEnable(self, boolean):
        self.setReadOnly(boolean)
        #
        if boolean is False:
            self.setFocus(QtCore.Qt.MouseFocusReason)
        elif boolean is True:
            self.clearFocus()
        #
        self._updateUiStyle()
    #
    def _updateUiStyle(self):
        if self._parent:
            if self.hasFocus():
                if not self.isReadOnly():
                    self._parent._setUiPressStyle(uiCore.OnState)
            elif not self.hasFocus():
                if self.isReadOnly():
                    self._parent._setUiPressStyle(uiCore.OffState)
                if not self.isReadOnly():
                    self._parent._setUiPressStyle(uiCore.NormalState)
    #
    def setUiStyle(self):
        self.setStyleSheet(
            'QLineEdit{background: rgba(0, 0, 0, 0) ; color: rgba(223, 223, 223, 255)}'
            'QLineEdit{border: none}'
            'QLineEdit{selection-color: rgba(255, 255, 255, 255) ; selection-background-color: rgba(0, 127, 127, 255)}'
        )
    #
    def setUiSize(self):
        self.setMaximumSize(166667, 20)
        self.setMinimumSize(0, 20)
    #
    def initUi(self):
        pass


#
class xEntryBox(QFrame):
    entryChanged = uiCore.uiSignal()
    #
    borderRadius = 0
    normalBorderStyle = InsetBorder
    offBorderStyle = SolidBorder
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QFrame, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.initUi()
        #
        self.setupUi()
        #
        self.setUiStyle()
        self.setUiSize()
    #
    def setNameText(self, explain):
        self.entryLabel.setPlaceholderText('Enter ' + explain + '...')
    #
    def setDatum(self, string):
        if string:
            if isinstance(string, str) or isinstance(string, unicode):
                self.entryLabel.setText(string)
            if isinstance(string, list):
                self.entryLabel.setText(';'.join(string))
        if not string:
            self.entryLabel.setText(none)
        #
        self.setClearButtonVisibleSwitch()
    #
    def setIntValidator(self):
        self.entryLabel.setValidator(QtGui.QIntValidator())
    #
    def setTextValidator(self, limit):
        reg = QtCore.QRegExp('[a-zA-Z]%s' % ('[a-zA-Z0-9_]' * limit))
        validator = QtGui.QRegExpValidator(reg, self.entryLabel)
        self.entryLabel.setValidator(validator)
    #
    def setClearButtonVisibleSwitch(self):
        if not self._isEntryLock:
            self._clearButton.setVisible([False, True][len(self.entryLabel.text()) > 0])
        if self._isEntryLock:
            self._clearButton.setVisible(False)
    #
    def setEnterEnable(self, boolean):
        self.entryLabel.setReadOnly(not boolean)
        self._isEntryLock = not boolean
        self._updateUiStyle()
    #
    def entryEvent(self):
        self.entryChanged.emit()
        self.setClearButtonVisibleSwitch()
    #
    def setClear(self):
        self.entryLabel.clear()
        self.setClearButtonVisibleSwitch()
    #
    def setEntryEnableSwitch(self):
        self._isEntryLock = not self._isEntryLock
        self.entryLabel.setEnterEnable(self._isEntryLock)
        self.setClearButtonVisibleSwitch()
    #
    def datum(self):
        string = none
        data = self.entryLabel.text()
        if data:
            if isinstance(data, str) or isinstance(data, unicode):
                string = data
            else:
                string = str(data.toUtf8()).decode('utf-8')
        return string
    #
    def _updateUiStyle(self):
        self._setUiPressStyle([uiCore.NormalState, uiCore.OffState][self._isEntryLock])
        self.setClearButtonVisibleSwitch()
    #
    def _setUiPressStyle(self, state):
        if state is uiCore.NormalState:
            uiStyle = '''
            QFrame{{background: rgba(0, 0, 0, 0)}}
            QFrame{{border: {0}px rgba(47, 47, 47, 255) ; border-radius: {1}px ; border-style: {2}}}
            '''.format(1, self.borderRadius, self.normalBorderStyle)
            self.setStyleSheet(uiStyle)
        elif state is uiCore.OnState:
            uiStyle = '''
            QFrame{{background: rgba(47, 47, 47, 255)}}
            QFrame{{border: {0}px rgba(47, 47, 47, 255) ; border-radius: {1}px ; border-style: {2}}}
            '''.format(1, self.borderRadius, self.normalBorderStyle)
            self.setStyleSheet(uiStyle)
        elif state is uiCore.OffState:
            uiStyle = '''
                QFrame{{background: rgba(0, 0, 0, 0)}}
                QFrame{{border: {0}px rgba(63, 63, 63, 255) ; border-radius: {1}px ; border-style: {2}}}
            '''.format(1, self.borderRadius, self.offBorderStyle)
            self.setStyleSheet(uiStyle)
    #
    def setUiStyle(self):
        self._setUiPressStyle(uiCore.OffState)
    #
    def setUiSize(self):
        pass
    #
    def initUi(self):
        self._isEntryLock = True
    #
    def setupUi(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        self._entryEnableButton = uiWidgets.UiIconbutton('svg_basic@svg#help')
        layout.addWidget(self._entryEnableButton)
        self._entryEnableButton.clicked.connect(self.setEntryEnableSwitch)
        self._entryEnableButton.setTooltip(u'点击启用/关闭输入锁定')
        #
        self.entryLabel = xLineEdit(self)
        layout.addWidget(self.entryLabel)
        self.entryLabel.setReadOnly(True)
        self.entryLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.entryLabel.setFont(uiCore.xFont(size=8, weight=50))
        self.entryLabel.entryChanged.connect(self.entryEvent)
        # self.entryLabel.doubleClicked.connect(self.setEntryEnableSwitch)
        #
        self._clearButton = uiWidgets.UiIconbutton('entryClear')
        self._clearButton.hide()
        layout.addWidget(self._clearButton)
        self._clearButton.clicked.connect(self.setClear)
        self._clearButton.clicked.connect(self.entryEvent)


#
class xEntryLabel(QFrame):
    datumChanged = uiCore.uiSignal()
    entryChanged = uiCore.uiSignal()
    chooseChanged = uiCore.uiSignal()
    #
    explainWidth = 120
    chooseBoxWidth = 256
    chooseItemHeight = 20
    #
    maxVisibleItems = 10
    #
    borderRadius = 10
    borderStyle = InsetBorder
    def __init__(self, explainVisible=True, *args, **kwargs):
        self.clsSuper = super(xEntryLabel, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.explainVisible = explainVisible
        #
        self.initUi()
        #
        self.setupUi()
        #
        self.setUiStyle()
        self.setUiSize()
        #
        self._updateUiStyle()
    #
    def setNameText(self, string):
        if string:
            self.explainLabel.setNameText(string)
            #
            self._uiNameText = string
    #
    def setTooltip(self, string):
        self.explainLabel.setTooltip(string)
    #
    def setExplainToolTip(self, string):
        self.explainLabel.setToolTip(string)
    #
    def setExplainVisible(self, boolean):
        self.explainLabel.setVisible(boolean)
    #
    def setExplainCountSwitch(self):
        if self._messages:
            message = self.entryLabel.text()
            if message in self._messages:
                index = self._messages.index(message)
                #
                maxCount = len(self._messages)
                superString = '%s/%s' % (index + 1, maxCount)
                self.explainLabel.setSuperExplain(superString)
                #
                self.currentIndex = index
        else:
            self.explainLabel.setSuperExplain(none)
    #
    def setWidth(self, width):
        self.explainLabel.setMinimumWidth(width)
        self.explainLabel.setMaximumWidth(width)
    @staticmethod
    def getCovertMessage(message):
        data = None
        if message is not None:
            if isinstance(message, bool):
                data = str(message)
            elif isinstance(message, int) or isinstance(message, float):
                data = str(message)
            elif isinstance(message, str) or isinstance(message, unicode):
                data = message
            elif isinstance(message, list) or isinstance(message, tuple):
                message = [str(i) for i in message]
                data = ','.join(message)
            elif isinstance(message, dict):
                data = ','.join([':'.join(i) for i in message.items()])
        #
        return data
    #
    def setDatum(self, message):
        if message is not None:
            data = self.getCovertMessage(message)
            #
            if data is not None:
                self.entryLabel.setText(data)
        #
        self._msgTypeRecord = message
        #
        self._updateUiStyle()
    #
    def setDefaultDatum(self, message):
        self._defaultMsg = message
        #
        self.setDatum(message)
    #
    def setDatumLis(self, strings, iconKeyword=none):
        if strings:
            if isinstance(strings, str) or isinstance(strings, unicode):
                strings = [strings]
            #
            self._messages = strings
            self.setChoose(strings[0])
            #
            self._uiIconKeyword = iconKeyword
            #
            self.setChooseEnable(True)
        else:
            self.setChooseClear()
            self.setChooseEnable(False)
    #
    def datum(self):
        message = None
        data = self.entryLabel.text()
        if data is not None:
            if isinstance(self._msgTypeRecord, bool):
                message = eval(data)
            elif isinstance(self._msgTypeRecord, int):
                message = int(data)
            elif isinstance(self._msgTypeRecord, float):
                message = float(data)
            elif isinstance(self._msgTypeRecord, str) or isinstance(self._msgTypeRecord, unicode):
                if not self._datumDic:
                    message = data
                else:
                    message = self._datumDic[data][1]
            elif isinstance(self._msgTypeRecord, list) or isinstance(self._msgTypeRecord, tuple):
                message = data.split(',')
            elif isinstance(self._msgTypeRecord, tuple):
                message = data.split(',')
            elif isinstance(self._msgTypeRecord, dict):
                dic = {}
                lis = [i.split(':') for i in data.split(',')]
                for k, v in lis:
                    dic[k] = v
                message = dic
        return message
    #
    def setMultMsg(self, multMsg):
        if multMsg is not None:
            self._multMsg = multMsg
    #
    def setExtendDatumDic(self, multMsgs):
        if isinstance(multMsgs, dict):
            messages = []
            self._datumDic = lxBasic.orderedDict()
            for index, (name, description) in multMsgs.items():
                viewName = unicode(description)
                if viewName in messages:
                    if not '#' in viewName:
                        viewName += '#1'
                    else:
                        number = int(viewName.split('#')[-1])
                        viewName = viewName.split('#')[0] + '[%s]' % number + 1
                #
                self._datumDic[viewName] = index, name
                messages.append(viewName)
            #
            self.setDatumLis(messages)
    #
    def getMultMsg(self):
        if self._datumDic:
            message = self.entryLabel.text()
            return self._datumDic[message]
    #
    def setChoose(self, string):
        if string in self._messages:
            self.setDatum(string)
            #
            self.chooseChanged.emit()
            self.datumChanged.emit()
            #
            self.setExplainCountSwitch()
    #
    def scrollUp(self):
        index = self.currentIndex
        if index > 0:
            message = self._messages[index - 1]
            self.setChoose(message)
    #
    def scrollDown(self):
        index = self.currentIndex
        count = len(self._messages)
        if index < count - 1:
            message = self._messages[index + 1]
            self.setChoose(message)
    #
    def setChecked(self, boolean):
        self._checkButton.setChecked(boolean)
        self._checkClickSwitchAction()
    #
    def _checkClickSwitchAction(self):
        self.setDatum([False, True][self._checkButton.isChecked()])
    #
    def setIntValidator(self):
        self.entryLabel.setValidator(QtGui.QIntValidator())
    #
    def setStrValidator(self, limit):
        reg = QtCore.QRegExp('[a-zA-Z]%s' % ('[a-zA-Z0-9_]'*limit))
        validator = QtGui.QRegExpValidator(reg, self.entryLabel)
        self.entryLabel.setValidator(validator)
    #
    def setSceneNumValidator(self):
        reg = QtCore.QRegExp('[0-9][0-9][0-9][A-Z]')
        validator = QtGui.QRegExpValidator(reg, self.entryLabel)
        self.entryLabel.setValidator(validator)
    @uiChooseBoxEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiChooseViewDropMethod
    def setDropBox(self):
        pass
    #
    def getExplain(self):
        return self._uiNameText
    #
    def setClearButtonVisibleSwitch(self):
        if not self._isEntryLock:
            boolean = [False, True][len(self.entryLabel.text()) > 0]
        else:
            boolean = False
        #
        self._clearButton.setVisible(boolean)
        self._copyButton.setVisible(boolean)
    #
    def entryEvent(self):
        self.entryChanged.emit()
        self.datumChanged.emit()
        self.setClearButtonVisibleSwitch()
    #
    def setLockVisible(self, boolean):
        self._entryEnableButton.setVisible(boolean)
    #
    def setEnterEnable(self, boolean):
        self.entryLabel.setReadOnly(not boolean)
        self._isEntryLock = not boolean
        self._updateUiStyle()
    #
    def isEnterEnable(self):
        return not self._isEntryLock
    #
    def setChooseEnable(self, boolean):
        self._chooseButton.setVisible(boolean)
        self._isChooseEnable = boolean
        self._updateUiStyle()
    #
    def ieChooseEnable(self):
        return self._isChooseEnable
    #
    def setCheckEnable(self, boolean):
        self._checkButton.setVisible(boolean)
        self._isCheckEnable = boolean
        #
        self._updateUiStyle()
    #
    def setEnterClear(self):
        self.entryLabel.clear()
        self.setClearButtonVisibleSwitch()
    # noinspection PyArgumentList
    def setEntryCopy(self):
        message = self.datum()
        clipboard = QApplication.clipboard()
        clipboard.setText(message)
    #
    def setChooseClear(self):
        self.entryLabel.clear()
        self._messages = []
        self.chooseChanged.emit()
        self.datumChanged.emit()
        self.setExplainCountSwitch()
    #
    def setEntryEnableSwitch(self):
        self._isEntryLock = not self._isEntryLock
        self.entryLabel.setEnterEnable(self._isEntryLock)
        self.setClearButtonVisibleSwitch()
    #
    def setAddButton(self, button):
        self._mainLayout.addWidget(button)
    #
    def _setUiPressStyle(self, state):
        if state is uiCore.NormalState:
            uiStyle = '''
                QWidget{{background: rgba(0, 0, 0, 0)}}
                QWidget{{border: {0}px rgba(47, 47, 47, 255) ; border-radius: {1}px ; border-style: {2}}}
            '''.format(1, self.borderRadius, self.borderStyle)
            self.entryWidget.setStyleSheet(uiStyle)
        elif state is uiCore.OnState:
            uiStyle = '''
                QWidget{{background: rgba(56, 56, 56, 255)}}
                QWidget{{border: {0}px rgba(47, 47, 47, 255) ; border-radius: {1}px ; border-style: {2}}}
            '''.format(1, self.borderRadius, self.borderStyle)
            self.entryWidget.setStyleSheet(uiStyle)
        elif state is uiCore.OffState:
            self.entryWidget.setStyleSheet(
                'QWidget{background: rgba(0, 0, 0, 0)}'
                'QWidget{border: none}'
            )
        self._updateUiStatus()
    #
    def _updateUiStyle(self):
        self._setUiPressStyle([uiCore.NormalState, uiCore.OffState][self._isEntryLock])
        #
        self.entryLabel.setPlaceholderText(['Enter ' + self._uiNameText + '...', none][self._isEntryLock])
        #
        self.setClearButtonVisibleSwitch()
    #
    def _setUiPressStatus(self, status):
        self.explainLabel._setUiPressStatus(status)
    #
    def _updateUiStatus(self):
        if self._defaultMsg is not None:
            message = self.datum()
            if message == self._defaultMsg:
                self._uiStatus = uiCore.NormalStatus
            else:
                self._uiStatus = uiCore.WarningStatus
        #
        self._setUiPressStatus(self._uiStatus)
    #
    def setUiStyle(self):
        self.setStyleSheet(
            'QFrame{background: rgba(63, 63, 63, 0)}'
            'QFrame{border: none}'
        )
        self._setUiPressStyle(uiCore.NormalState)
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(166667, 20))
        self.setMinimumSize(QtCore.QSize(0, 20))
        #
        self.explainLabel.setMaximumWidth(self.explainWidth)
        self.explainLabel.setMinimumWidth(self.explainWidth)
    #
    def initUi(self):
        self._datum = None
        self._multMsg = None
        self._multDic = None
        self._datumDic = lxBasic.orderedDict()
        #
        self._msgTypeRecord = none
        self._defaultMsg = None
        self._msgType = str
        #
        self._isEntryLock = True
        self._isChooseLock = True
        #
        self._isChooseEnable = False
        self._uiIconKeyword = None
        #
        self._isCheckEnable = False
        #
        self._uiNameText = none
        #
        self._uiStatus = uiCore.NormalStatus
        #
        self.dropBox = None
        #
        self.currentIndex = 0
        #
        self._messages = []
    #
    def setupUi(self):
        self._mainLayout = QHBoxLayout(self)
        self._mainLayout.setContentsMargins(0, 0, 0, 0)
        self._mainLayout.setSpacing(2)
        #
        self.explainLabel = xExplainLabel()
        self._mainLayout.addWidget(self.explainLabel)
        # Debug ( Must Set after addWidget )
        self.explainLabel.setVisible(self.explainVisible)
        #
        self.entryWidget = QWidget()
        self._mainLayout.addWidget(self.entryWidget)
        layout = QHBoxLayout(self.entryWidget)
        layout.setContentsMargins(2, 0, 2, 0)
        layout.setSpacing(2)
        #
        self._chooseButton = uiWidgets.UiIconbutton('basic#choose')
        self._chooseButton.hide()
        layout.addWidget(self._chooseButton)
        self._chooseButton.clicked.connect(self.setDropBox)
        self._chooseButton.upScrolled.connect(self.scrollUp)
        self._chooseButton.downScrolled.connect(self.scrollDown)
        self._chooseButton.setTooltip(u'1.左键点击：查看/选择更多选项\r\n2.中键滚动：向上/向下选择')
        #
        self._entryEnableButton = uiWidgets.UiIconbutton('basic#entry')
        self._entryEnableButton.hide()
        layout.addWidget(self._entryEnableButton)
        self._entryEnableButton.clicked.connect(self.setEntryEnableSwitch)
        self._entryEnableButton.setTooltip(u'点击启用/关闭输入锁定')
        #
        self._checkButton = xCheckBox('basic#boxCheck')
        self._checkButton.hide()
        layout.addWidget(self._checkButton)
        self._checkButton.clicked.connect(self._checkClickSwitchAction)
        self._checkButton.setTooltip(u'点击启用/禁用')
        #
        self.entryLabel = xLineEdit(self)
        layout.addWidget(self.entryLabel)
        self.entryLabel.setReadOnly(self._isEntryLock)
        self.entryLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.entryLabel.setFont(uiCore.xFont(size=8, weight=50, family=_families[0]))
        self.entryLabel.entryChanged.connect(self.entryEvent)
        #
        self._copyButton = uiWidgets.UiIconbutton('basic#copy')
        self._copyButton.hide()
        layout.addWidget(self._copyButton)
        self._copyButton.setTooltip(u'点击复制输入')
        self._copyButton.clicked.connect(self.setEntryCopy)
        #
        self._clearButton = uiWidgets.UiIconbutton('entryClear')
        self._clearButton.hide()
        layout.addWidget(self._clearButton)
        self._clearButton.setTooltip(u'点击清除输入')
        self._clearButton.clicked.connect(self.setEnterClear)
        self._clearButton.clicked.connect(self.entryEvent)


#
class xToolBar(QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )
        #
        self._initUi()
        #
        self.setupUi()
        #
        self.setUiSize()
    #
    def addItem(self, widget):
        return self._layout.addWidget(widget)
    #
    def addWidget(self, widget):
        return self._layout.addWidget(widget)
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(166667, self._uiHeight))
        self.setMinimumSize(QtCore.QSize(0, self._uiHeight))
    #
    def _initUi(self):
        self._uiHeight = 32
    #
    def setupUi(self):
        self._layout = uiCore.QHBoxLayout_(self)
        self._layout.setAlignment(QtCore.Qt.AlignVCenter)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(2)


#
class QTreeWidgetItem_(QTreeWidgetItem):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QTreeWidgetItem, self)
        self.clsSuper.__init__(*args, **kwargs)
        self.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
        )
        #
        self.name = None
        self.path = None
        self.filter = None
    #
    def setItemWidget(self, index, itemWidget):
        treeBox = self.treeWidget()
        if treeBox:
            treeBox.setItemWidget(self, index, itemWidget)
    #
    def removeItemWidget(self, index):
        treeBox = self.treeWidget()
        if treeBox:
            treeBox.removeItemWidget(self, index)
    #
    def itemWidget(self, index):
        treeBox = self.treeWidget()
        return treeBox.itemWidget(self, index)
    #
    def parentItems(self):
        def getBranch(treeItem):
            parentItem = treeItem.parent()
            if parentItem:
                lis.append(parentItem)
                getBranch(parentItem)
        lis = []
        getBranch(self)
        return lis
    #
    def setTooltip(self, index, string):
        self.setToolTip(index, string)
    #
    def childItems(self):
        def getBranch(treeItem):
            childCount = treeItem.childCount()
            for seq in range(childCount):
                childItem = treeItem.child(seq)
                lis.append(childItem)
                getBranch(childItem)
        lis = []
        getBranch(self)
        return lis
    #
    def setItemFont(self, index, state):
        isItalic = False
        isUnderline = False
        #
        if isinstance(state, str) or isinstance(state, unicode):
            if state == none:
                fontWeight = 50
                rgba = 191, 191, 191, 255
            elif state.lower() == 'warning':
                fontWeight = 50
                rgba = 255, 255, 64, 255
            elif state.lower() == 'error' or state.lower() == 'unload':
                fontWeight = 50
                rgba = 255, 0, 63, 255
                isUnderline = True
            elif state.lower() == 'disable':
                fontWeight = 50
                rgba = 127, 64, 255, 255
                isUnderline = True
            elif state.lower() == 'wait':
                fontWeight = 50
                rgba = 32, 191, 255, 255
            elif state.lower() == 'on':
                fontWeight = 50
                rgba = 63, 255, 127, 255
            elif state.lower() == 'off':
                fontWeight = 50
                rgba = 127, 127, 127, 255
                isItalic = True
            elif state.lower() == 'lock':
                fontWeight = 50
                rgba = 127, 127, 127, 255
                isUnderline = True
            elif state.lower() == 'focus':
                fontWeight = 50
                rgba = 63, 255, 127, 255
                isUnderline = True
            elif state.lower() == 'info':
                fontWeight = 75
                rgba = 63, 255, 127, 255
            else:
                fontWeight = 50
                rgba = 191, 191, 191, 255
        else:
            fontWeight = 50
            rgba = 191, 191, 191, 255
        #
        r, g, b, a = rgba
        brush = QtGui.QBrush(QtGui.QColor(r, g, b, a))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setForeground(index, brush)
        #
        font = uiCore.xFont(
            size=8,
            weight=fontWeight,
            italic=isItalic,
            underline=isUnderline,
            family=_families[0]
        )
        #
        self.setFont(index, font)
    #
    def setItemIcon(self, index, iconKeyword, state=none):
        if iconKeyword:
            if isinstance(state, str) or isinstance(state, unicode):
                iconKeyword += state
            #
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(uiCore._toLxOsIconFile(iconKeyword)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.On
            )
            self.setIcon(index, icon)
        else:
            icon = QtGui.QIcon()
            self.setIcon(index, icon)
        #
        self.setItemFont(index, state)
    #
    def setItemCheckIcon(self, index, iconKeyword, state=None):
        dic = {'on': 'adopt', 'off': 'disable'}
        if iconKeyword:
            if isinstance(state, str) or isinstance(state, unicode):
                iconKeyword += dic.get(state.lower(), state.lower())
            #
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(uiCore._toLxOsIconFile(iconKeyword)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.On
            )
            self.setIcon(index, icon)
        else:
            icon = QtGui.QIcon()
            self.setIcon(index, icon)
        #
        self.setItemFont(index, state)
    #
    def setItemIcon_(self, index, iconKeyword, state=None):
        if iconKeyword:
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(uiCore._toLxOsIconFile(iconKeyword)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.On
            )
            self.setIcon(index, icon)
        if not iconKeyword:
            icon = QtGui.QIcon()
            self.setIcon(index, icon)
        #
        self.setItemFont(index, state)
    #
    def setItemMayaIcon(self, index, mayaNodeType, state=None):
        if mayaNodeType:
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(uiCore._toLxMayaOsIconFile(mayaNodeType)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.On
            )
            self.setIcon(index, icon)
        #
        self.setItemFont(index, state)
    #
    def setItemIconWidget(self, index, iconKeyword, explain=none, state=None):
        isItalic = False
        isUnderline = False
        #
        if isinstance(state, str) or isinstance(state, unicode):
            if state.lower() == 'warning':
                fontWeight = 50
                rgba = 255, 255, 64, 255
            elif state.lower() == 'error' or state.lower() == 'unload':
                fontWeight = 50
                rgba = 255, 0, 63, 255
                isUnderline = True
            elif state.lower() == 'disable':
                fontWeight = 50
                rgba = 127, 64, 255, 255
                isUnderline = True
            elif state.lower() == 'wait':
                fontWeight = 50
                rgba = 32, 191, 255, 255
            elif state.lower() == 'on':
                fontWeight = 50
                rgba = 63, 255, 127, 255
            elif state.lower() == 'off':
                fontWeight = 50
                rgba = 127, 127, 127, 255
                isItalic = True
            elif state.lower() == 'lock':
                fontWeight = 50
                rgba = 127, 127, 127, 255
                isUnderline = True
            elif state.lower() == 'focus':
                fontWeight = 50
                rgba = 63, 255, 127, 255
                isUnderline = True
            elif state.lower() == 'info':
                fontWeight = 75
                rgba = 63, 255, 127, 255
            else:
                fontWeight = 50
                rgba = 191, 191, 191, 255
        else:
            fontWeight = 50
            rgba = 191, 191, 191, 255
        #
        font = uiCore.xFont(size=8, weight=fontWeight, italic=isItalic, underline=isUnderline, family=_families[0])
        #
        treeBox = self.treeWidget()
        #
        existsItemWidget = self.itemWidget(index)
        if not existsItemWidget:
            itemWidget = xIconLabel(treeBox)
            treeBox.setItemWidget(self, index, itemWidget)
        else:
            itemWidget = existsItemWidget
        #
        if state is not None:
            itemWidget.setIcon((iconKeyword, 'state@svg#%s' % state))
        else:
            itemWidget.setIcon((iconKeyword, None))
        #
        itemWidget.setNameText(explain, explainColor=rgba, explainFont=font)
        self.setText(index, none)
        self.name = explain
        #
        return itemWidget


#
class QTreeWidget_(QTreeWidget):
    focusIn = uiCore.uiSignal()
    focusOut = uiCore.uiSignal()
    #
    headerBorderStyle = SolidBorder
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QTreeWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setIndentation(12)
        self.setSortingEnabled(True)
        self.sortByColumn(1, QtCore.Qt.SortOrder())
        #
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragOnly)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        #
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        #
        self.setAllColumnsShowFocus(True)
        self.setUniformRowHeights(True)
        self.setWordWrap(True)
        #
        self.headerView = self.header()
        self.headerView.setHighlightSections(True)
        self.headerView.setSortIndicatorShown(True)
        self.headerView.setCascadingSectionResizes(True)
        self.headerView.setFont(uiCore.xFont(size=8, weight=75))
        #
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #
        self.setStyle(uiCore.QCommonStyle_())
        #
        self.initUi()
        #
        self.setUiStyle()
        self.setUiSize()
    #
    def addItem(self, item):
        self.addTopLevelItem(item)
    @staticmethod
    def addChild(parent, child):
        parent.addChild(child)
    #
    def setActionData(self, actions):
        self.actionData = actions
    #
    def insertItem(self, index, item):
        self.insertTopLevelItem(index, item)
    #
    def removeItem(self):
        pass
    #
    def topItems(self):
        lis = []
        for i in range(self.topLevelItemCount()):
            topItem = self.topLevelItem(i)
            lis.append(topItem)
        return lis
    #
    def treeItems(self):
        def getBranch(treeItem):
            childCount = treeItem.childCount()
            if childCount:
                for index in range(childCount):
                    childItem = treeItem.child(index)
                    lis.append(childItem)
                    getBranch(childItem)
        #
        lis = []
        for i in range(self.topLevelItemCount()):
            topItem = self.topLevelItem(i)
            lis.append(topItem)
            getBranch(topItem)
        return lis
    #
    def treeItemNames(self, column=0):
        def getBranch(treeItem):
            childCount = treeItem.childCount()
            if childCount:
                for index in range(childCount):
                    childItem = treeItem.child(index)
                    childItemName = childItem.text(column)
                    lis.append(childItemName)
                    getBranch(childItem)
        #
        lis = []
        for i in range(self.topLevelItemCount()):
            topItem = self.topLevelItem(i)
            topItemName = topItem.text(column)
            lis.append(topItemName)
            getBranch(topItem)
        return lis
    #
    def selectedItemNames(self):
        lis = []
        treeItems = self.selectedItems()
        if treeItems:
            for i in treeItems:
                if hasattr(i, 'name'):
                    name = i.name
                else:
                    name = i.text(0)
                #
                if name is not None:
                    lis.append(name)
        return lis
    #
    def selectedItemTexts(self, column=0):
        lis = []
        if self.selectedItems():
            for treeItem in self.selectedItems():
                if isinstance(column, int):
                    name = str(treeItem.text(column))
                    lis.append(name)
                elif isinstance(column, list):
                    subLis = []
                    for i in column:
                        name = str(treeItem.text(i))
                        subLis.append(name)
                    #
                    lis.append(subLis)
        return lis
    #
    def itemWidgetDatumDic(self, column=(0, 1)):
        dic = lxBasic.orderedDict()
        for treeItem in self.treeItems():
            for seq in range(*column):
                itemWidget = self.itemWidget(treeItem, seq)
                if itemWidget is not None:
                    datum = itemWidget.datum()
                else:
                    datum = str(treeItem.text(seq))
                #
                dic.setdefault(treeItem, []).append(datum)
        #
        return dic
    #
    def selectedItemPaths(self):
        lis = []
        treeItems = self.selectedItems()
        if treeItems:
            for i in treeItems:
                if hasattr(i, 'path'):
                    path = i.path
                    if path is not None:
                        data = path
                    else:
                        data = i.text(0)
                else:
                    data = i.text(0)
                #
                lis.append(data)
        return lis
    #
    def setColumns(self, explains, widths, widthSet, mode=0):
        count = len(explains)
        maxDivision = sum(widths)
        unitWidth = widthSet / maxDivision
        if mode == 1:
            unitWidth = widthSet
        self.setColumnCount(count)
        self.setHeaderLabels(explains)
        for index in range(0, count):
            self.setColumnWidth(index, unitWidth * (widths[index]))
            self.headerItem().setBackground(index, QtGui.QColor(63, 63, 63))
            brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
            brush.setStyle(QtCore.Qt.SolidPattern)
            self.headerItem().setForeground(index, brush)
            icon = QtGui.QIcon()
            #
            if index == 0:
                iconKeyword = 'svg_basic@svg#treeWidgetHeader'
            else:
                iconKeyword = 'svg_basic@svg#vLine'
            icon.addPixmap(
                QtGui.QPixmap(uiCore._toLxOsIconFile(iconKeyword)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.On
            )
            if explains[index]:
                self.headerItem().setIcon(index, icon)
            font = QtGui.QFont()
            font.setWeight(75)
            self.headerItem().setFont(index, font)
    #
    def setColumns_(self, explainLis, maxWidth):
        explain = []
        [explain.append('%s' % i) for i in explainLis]
        count = len(explain)
        self.setColumnCount(count)
        self.setHeaderLabels(explain)
        #
        for i in range(0, count):
            if i == 0:
                self.setColumnWidth(i, maxWidth / 2)
            else:
                self.setColumnWidth(i, maxWidth / 2 / (count - 1))
        #
        for index in range(0, count):
            self.headerItem().setBackground(index, QtGui.QColor(32, 32, 32))
            brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
            brush.setStyle(QtCore.Qt.SolidPattern)
            self.headerItem().setForeground(index, brush)
            icon = QtGui.QIcon()
            if index == 0:
                iconKeyword = 'svg_basic@svg#treeWidgetHeader'
            else:
                iconKeyword = 'svg_basic@svg#vLine'
            icon.addPixmap(
                QtGui.QPixmap(uiCore._toLxOsIconFile(iconKeyword)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.On
            )
            self.headerItem().setIcon(index, icon)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            self.headerItem().setFont(index, font)
    #
    def setHeaderView(self, data, widthSet, mode=1):
        count = len(data)
        explains = [lxBasic._toStringPrettify(i[0]) for i in data]
        widths = [i[1] for i in data]
        maxDivision = sum(widths)
        unitWidth = widthSet / maxDivision
        if mode == 1:
            unitWidth = widthSet
        self.setColumnCount(count)
        self.setHeaderLabels(explains)
        for index in range(0, count):
            self.setColumnWidth(index, unitWidth * (widths[index]))
            self.headerItem().setBackground(index, QtGui.QColor(63, 63, 63))
            brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
            brush.setStyle(QtCore.Qt.SolidPattern)
            self.headerItem().setForeground(index, brush)
            icon = QtGui.QIcon()
            iconLabel = 'horizontalAdjust.png'
            if index == 0:
                iconLabel = 'horizontalAdjustOn.png'
            icon.addPixmap(
                QtGui.QPixmap(uiCore.iconRoot() + '/panel/' + iconLabel),
                QtGui.QIcon.Normal,
                QtGui.QIcon.On
            )
            if explains[index]:
                self.headerItem().setIcon(index, icon)
            font = QtGui.QFont()
            font.setWeight(75)
            self.headerItem().setFont(index, font)
    #
    def updateExpandDic(self, dic):
        treeItems = self.treeItems()
        if treeItems:
            for treeItem in treeItems:
                if hasattr(treeItem, 'path'):
                    path = treeItem.path
                    if path is not None:
                        isExpanded = treeItem.isExpanded()
                        dic[path] = isExpanded
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clsSuper.mousePressEvent(event)
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self.setMenu()
    #
    def focusInEvent(self, event):
        self.clsSuper.focusInEvent(event)
        #
        # self.verticalScrollBar().show()
        # self.horizontalScrollBar().show()
        #
        self.focusIn.emit()
    #
    def focusOutEvent(self, event):
        self.clsSuper.focusOutEvent(event)
        #
        # self.verticalScrollBar().hide()
        # self.horizontalScrollBar().hide()
        #
        self.focusOut.emit()
    @uiWidgetBasic.uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiWidgetBasic.uiActionViewDropMethod
    def setMenu(self):
        pass
    #
    def setSelectAll(self):
        treeItems = self.treeItems()
        [i.setSelected(True) for i in treeItems if not i.isHidden()]
    #
    def setSingleSelection(self):
        self.setSelectionMode(QAbstractItemView.SingleSelection)
    #
    def setNoSelection(self):
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
    # Filter
    def setFilterConnect(self, filterWidget):
        self._filterViewWidget = filterWidget
        self._filterViewWidget.entryChanged.connect(self.setStringFilter)
    #
    def setFilterExplainRefresh(self):
        filterItems = self.treeItems()
        filterWidget = self._filterViewWidget
        #
        filterWidget.setNameText(str(len(filterItems)).zfill(4))
    #
    def setStringFilter(self):
        treeWidget = self
        filterWidget = self._filterViewWidget
        #
        uiCore.setTreeWidgetKeywordFilter(treeWidget, filterWidget, self._filterLimitLis)
    #
    def setFilterLimitLis(self, lis):
        self._filterLimitLis = lis
    #
    def setUiStyle(self, inuse='A'):
        uiStyle = '''
            QHeaderView{{
                color: rgba(191, 191, 191, 255); background: rgba(63, 63, 63, 255)
            }}
            QHeaderView{{
                border: 1px rgba(80, 80, 80, 255) ;
                border-top-left-radius: 2px ; border-top-right-radius: 2px ;
                border-bottom-left-radius: 2px ; border-bottom-right-radius: 2px ;
                border-style: solid
            }}
            QHeaderView::section{{
                background: rgba(63, 63, 63, 255) ; margin: 4px, 4px, 4px, 4px
            }}
            QHeaderView::section{{border: none}}
            QHeaderView::up-arrow{{image: url({0}/svg_basic/up.svg)}}
            QHeaderView::down-arrow{{image: url({0}/svg_basic/down.svg)}}
        '''.format(uiCore.iconRoot())
        self.headerView.setStyleSheet(uiStyle)
        #
        self.setPalette(QPalette_())
        uiCore.setTreeWidgetStyle(self)
        uiCore.setScrollBarStyle(self)
    #
    def initUi(self):
        self._filterLimitLis = None
        #
        self._filterViewWidget = None
        self.actionData = []
        #
        self._itemGraphDic = {}
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(166667, 166667))
        self.setMinimumSize(QtCore.QSize(0, 0))
        #
        self.headerView.setMaximumHeight(24)
        self.headerView.setMinimumHeight(24)
    @classmethod
    def getGraphDatumDic(cls, objectPaths, pathsep, progressBar=None):
        dic = lxBasic.orderedDict()
        # Get Root
        def getRoot(objectPath, objectNames):
            node = objectNames[-1]
            dic.setdefault((none, none), []).append((node, objectPath))
        # Get Branch
        def getBranch(objectPath, objectNames, dataArray):
            parent = objectNames[-2]
            parentPath = pathsep.join(objectNames[:-1])
            node = objectNames[-1]
            dataArray.append(((parent, parentPath), (node, objectPath)))
        #
        def getMain():
            dataArray = []
            # Get Dict
            if objectPaths:
                for objectPath in objectPaths:
                    if progressBar:
                        progressBar.updateProgress()
                    #
                    if not objectPath.startswith(pathsep):
                        objectPath = pathsep + objectPath
                    #
                    objectNames = objectPath.split(pathsep)
                    isRoot = len(objectNames) == 2
                    # Filter is Root
                    if isRoot:
                        getRoot(objectPath, objectNames)
                    else:
                        getBranch(objectPath, objectNames, dataArray)
            # Reduce Dict
            if dataArray:
                cls.setTreeViewPathDic(dic, dataArray)
        #
        getMain()
        return dic
    @classmethod
    def setTreeViewPathDic(cls, dic, dataArray):
        [dic.setdefault(parent, []).append(child) for parent, child in cls.getReduceList(dataArray)]
    @staticmethod
    def getReduceList(listData):
        reduceLis = []
        [reduceLis.append(i) for i in listData if i not in reduceLis]
        return reduceLis
    @classmethod
    def toGraphCompPaths(cls, path, pathsep):
        # List [ <Path> ]
        lis = []
        #
        dataArray = path.split(pathsep)
        #
        dataCount = len(dataArray)
        for seq, data in enumerate(dataArray):
            if data:
                if seq + 1 < dataCount:
                    compPath = pathsep.join(dataArray[:seq + 1])
                    lis.append(compPath)
        #
        lis.append(path)
        return lis
    @classmethod
    def getGraphPaths(cls, paths, pathsep):
        # List [ <Path> ]
        lis = []
        for path in paths:
            compPathLis = cls.toGraphCompPaths(path, pathsep)
            for compPath in compPathLis:
                if not compPath in lis:
                    lis.append(compPath)
        return lis
    #
    def getGraphExpandDic(self):
        dic = lxBasic.orderedDict()
        #
        treeItems = self.treeItems()
        if treeItems:
            for treeItem in treeItems:
                path = treeItem.path
                isExpanded = treeItem.isExpanded()
                dic[path] = isExpanded
        return dic
    #
    def setupGraph(self, datumDic, branchViewMethod=None, expandedDic=None, clearItemGraphDic=True):
        # Set Hierarchy Branch
        def setRoot(data):
            root, rootPath = data
            if root and rootPath:
                rootItem = QTreeWidgetItem_([root])
                rootItem.path = rootPath
                rootItem.name = root
                self.addTopLevelItem(rootItem)
                self._itemGraphDic[rootPath] = rootItem
                branchViewMethod(rootItem)
        #
        def setBranch(parentDatum):
            parent, parentPath = parentDatum
            if clearItemGraphDic is True:
                if not parentPath in self._itemGraphDic:
                    setRoot(parentDatum)
            #
            if parentDatum in datumDic:
                branchArray = datumDic[parentDatum]
                for branchData in branchArray:
                    objectName, objectPath = branchData
                    treeItem = QTreeWidgetItem_([objectName])
                    #
                    treeItem.path = objectPath
                    treeItem.name = objectName
                    #
                    isExistsParent = parent != none
                    if isExistsParent:
                        if parentPath in self._itemGraphDic:
                            parentItem = self._itemGraphDic[parentPath]
                            parentItem.addChild(treeItem)
                            if parentPath in expandedDic:
                                isExpand = expandedDic[parentPath]
                                parentItem.setExpanded(isExpand)
                        else:
                            self.addTopLevelItem(treeItem)
                    else:
                        self.addTopLevelItem(treeItem)
                    #
                    self._itemGraphDic[objectPath] = treeItem
                    if isinstance(branchViewMethod, types.FunctionType) or isinstance(branchViewMethod, types.ClassType):
                        # noinspection PyCallingNonCallable
                        branchViewMethod(treeItem)
                    #
                    setBranch(branchData)
        #
        if clearItemGraphDic is True:
            self._itemGraphDic = {}
        #
        if not isinstance(expandedDic, dict):
            expandedDic = {}
        #
        rootDatum = datumDic.keys()[0]
        if rootDatum:
            setBranch(rootDatum)
    #
    def itemGraphDic(self):
        return self._itemGraphDic
    #
    def clearGraphDic(self):
        self._itemGraphDic.clear()


#
class xCheckItemWidget(QWidget):
    clicked = uiCore.uiSignal()
    doubleClicked = uiCore.uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
        #
        self.setUiStyle()
        self.setUiSize()
    #
    def enterEvent(self, event):
        self._setUiPressStyle(uiCore.HoverState)
    #
    def leaveEvent(self, event):
        self._updateUiStyle()
    # noinspection PyArgumentList
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.checkBoxRect.contains(event.pos()):
                if self._isCheckable is True:
                    self._checkClickSwitchAction()
            else:
                self.setExpandSwitch()
                self.clicked.emit()
            #
            event.accept()
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
        else:
            event.ignore()
    # noinspection PyArgumentList
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.doubleClicked.emit()
            #
            event.accept()
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        event.accept()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        #
        painter.setFont(uiCore.xFont(size=8, weight=75, family=_families[2]))
        painter.setBorderRgba(self._uiBackgroundRgba)
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        #
        xPos = 0
        yPos = 0
        #
        width = self.width()
        height = self.height()
        #
        xPos += self._uiOffset
        # Background
        rect = QtCore.QRect(xPos, yPos, width, height)
        painter.drawRect(rect)
        # FilterColor
        if self._isColorEnable is True:
            rect = QtCore.QRect(
                xPos + (self._uiFrameWidth - self._uiColorWidth) / 2, (self._uiFrameHeight - self._filterBoxHeight) / 2,
                self._uiColorWidth, self._filterBoxHeight
            )
            painter.setBorderRgba(self._uiColorBorderRgba)
            painter.setBackgroundRgba(self._uiColorBackgroundRgba)
            painter.drawRect(rect)
            #
            xPos += self._uiFrameWidth
        #
        painter.setBorderRgba(self._uiNameRgba)
        # Expand
        if self._isExpandable is True:
            self.expandBoxRect = QtCore.QRect(
                xPos + (self._uiFrameWidth - self._expandBoxWidth) / 2, (self._uiFrameHeight - self._expandBoxHeight) / 2,
                self._expandBoxWidth, self._expandBoxHeight
            )
            icon = QtGui.QPixmap(self._expandBoxIcon)
            painter.drawPixmap(self.expandBoxRect, icon)
            #
            xPos += self._uiFrameWidth
        # Index
        if self._isIndexEnabled is True:
            indexTextRect = QtCore.QRect(
                xPos, yPos, self._uiIndexTextWidth, height
            )
            painter.drawText(indexTextRect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, str(self._index))
            #
            xPos += self._uiIndexTextWidth
        # Check Box
        if self._checkBoxIcon is not None:
            self.checkBoxRect = QtCore.QRect(
                xPos + (self._uiFrameWidth - self._uiIconWidth) / 2, (self._uiFrameHeight - self._uiIconHeight) / 2,
                self._uiIconWidth, self._uiIconHeight
            )
            icon = QtGui.QPixmap(self._checkBoxIcon)
            painter.drawPixmap(self.checkBoxRect, icon)
            #
            xPos += self._uiFrameWidth
        # Explain
        if self._datum is not None:
            showMessage = [self._datum, self._uiNameText][self._uiNameText is not None]
            explainRect = QtCore.QRect(
                xPos, yPos, width - xPos, height
            )
            isItalic = not self._isChecked
            painter.setFont(uiCore.xFont(size=8, weight=75, italic=isItalic, family=_families[2]))
            painter.drawText(explainRect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, showMessage)
    @uiWidgetBasic.uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiWidgetBasic.uiActionViewDropMethod
    def _menuDropAction(self):
        pass
    #
    def setActionData(self, actions):
        self.actionData = actions
    #
    def setExpanded(self, boolean):
        self._isExpanded = boolean
        #
        self.getExpandState()
    #
    def setExpandable(self, boolean):
        self._isExpandable = boolean
    #
    def setIndex(self, index):
        self._index = str(index)
    #
    def setChecked(self, boolean):
        self._isChecked = boolean
        #
        self._updateUiStyle()
    #
    def setCheckable(self, boolean):
        self._isCheckable = boolean
        #
        self._updateUiStyle()
    #
    def setNameText(self, string):
        self._uiNameText = string
    #
    def setDatum(self, string):
        self._datum = string
    #
    def isExpanded(self):
        return self._isExpanded
    #
    def isChecked(self):
        return self._isChecked
    #
    def getExplain(self):
        return self._uiNameText
    #
    def datum(self):
        return self._datum
    #
    def setFilterColor(self, color):
        self._isColorEnable = True
        #
        self._uiColorBackgroundRgba = color
    #
    def filterColor(self):
        if self._isColorEnable is True:
            return self._uiColorBackgroundRgba
    #
    def addWidget(self, widget):
        self._mainLayout.addWidget(widget)
    #
    def _checkClickSwitchAction(self):
        self._isChecked = not self._isChecked
        self._updateUiStyle()
    #
    def setExpandSwitch(self):
        self._isExpanded = not self._isExpanded
        #
        self.getExpandState()
    #
    def getCheckState(self):
        if self._isCheckable is True:
            self._checkBoxIcon = uiCore.iconRoot() + '/basic/' + ['checkOff.png', 'checkOn.png'][self._isChecked]
        elif self._isCheckable is False:
            self._checkBoxIcon = uiCore.iconRoot() + '/basic/uncheckable.png'
    #
    def getExpandState(self):
        self._expandBoxIcon = uiCore.iconRoot() + '/basic/' + ['branchClose.png', 'branchOpen.png'][self._isExpanded]
    #
    def _updateUiStyle(self):
        if self._isCheckable is True:
            self._setUiPressStyle([uiCore.UncheckedState, uiCore.CheckedState][self._isChecked])
        elif self._isCheckable is False:
            self._setUiPressStyle(uiCore.UncheckableState)
        #
        self.getCheckState()
    #
    def _setUiPressStyle(self, state):
        if state is uiCore.CheckedState:
            self._uiNameRgba = 191, 191, 191, 255
            self._uiBackgroundRgba = 63, 63, 63, 255
        elif state is uiCore.UncheckedState:
            self._uiNameRgba = 95, 95, 95, 255
            self._uiBackgroundRgba = 63, 63, 63, 255
        elif state is uiCore.UncheckableState:
            self._uiNameRgba = 191, 191, 191, 255
            self._uiBackgroundRgba = 63, 63, 63, 255
        elif state is uiCore.HoverState:
            self._uiNameRgba = 223, 223, 223, 255
            self._uiBackgroundRgba = 71, 71, 71, 255
        #
        self.update()
    #
    def setUiStyle(self):
        self._updateUiStyle()
    #
    def setUiSize(self):
        self.setMaximumHeight(self._uiFrameHeight)
        self.setMinimumHeight(self._uiFrameHeight)
    #
    def initUi(self):
        self._isColorEnable = False
        self._isExpandable = False
        self._isIndexEnabled = True
        #
        self._isCheckable = True
        self._isChecked = False
        self._isExpanded = False
        #
        self._checkBoxIcon = uiCore.iconRoot() + '/basic/check.png'
        self._expandBoxIcon = uiCore.iconRoot() + '/basic/branchClose.png'
        self._uiNameText = None
        self._datum = None
        self._index = 0
        #
        self._uiOffset = 0
        #
        self._uiIndexTextWidth = 32
        self._uiColorWidth = 12
        self._filterBoxHeight = 12
        self._expandBoxWidth = 8
        self._expandBoxHeight = 8
        self._explainWidth = 480
        #
        self._uiFrameWidth = 20
        self._uiFrameHeight = 20
        self._uiIconWidth = 16
        self._uiIconHeight = 16
        self._uiSide = 8
        #
        self._indexPosX = self._uiSide
        #
        self._uiBackgroundRgba = 71, 71, 71, 255
        self._uiBorderRgba = 95, 95, 95, 255
        self._uiNameRgba = 223, 223, 223, 255
        #
        self._uiColorBackgroundRgba = 63, 255, 127, 255
        self._uiColorBorderRgba = 127, 127, 127, 255
        #
        self.checkBoxRect = QtCore.QRect(0, 0, 0, 0)
        self.expandBoxRect = QtCore.QRect(0, 0, 0, 0)
        #
        self.actionData = []
    #
    def setupUi(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(self._explainWidth, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(QtCore.Qt.AlignLeft)
        #
        widget = uiCore.QWidget_()
        layout.addWidget(widget)
        self._mainLayout = QHBoxLayout(widget)
        self._mainLayout.setContentsMargins(0, 0, 0, 0)
        self._mainLayout.setSpacing(2)


# Sub Method
class xPresetItemWidget(QWidget):
    clicked = uiCore.uiSignal()
    doubleClicked = uiCore.uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def enterEvent(self, event):
        pass
        # self.subItemWidget.show()
    #
    def leaveEvent(self, event):
        pass
        # self.subItemWidget.hide()
    #
    def setActionData(self, actions):
        self.mainWidget.setActionData(actions)
    #
    def setIndex(self, index):
        self.mainWidget.setIndex(index)
    #
    def setExpanded(self, boolean):
        self.mainWidget.setExpanded(boolean)
        self.subItemWidget.setVisible(boolean)
    #
    def setChecked(self, boolean):
        if isinstance(boolean, bool):
            self.mainWidget.setChecked(boolean)
        if boolean is None:
            self.mainWidget.setCheckable(False)
            self.mainWidget.setChecked(True)
    #
    def setDescription(self, string):
        self.descriptionLabel.setDatum(string)
    #
    def setNameText(self, string):
        self.mainWidget.setNameText(string)
    #
    def setDatum(self, string):
        self.mainWidget.setDatum(string)
    #
    def addWidget(self, widget):
        self.subItemLayout.addWidget(widget)
    #
    def isExpanded(self):
        return self.mainWidget.isExpanded()
    #
    def isChecked(self):
        return self.mainWidget.isChecked()
    #
    def getExplain(self):
        return self.mainWidget.getExplain()
    #
    def datum(self):
        return self.mainWidget.datum()
    #
    def setMainData(self, key, value, isUseNiceName=False):
        if key:
            self.setDatum(key)
            if isUseNiceName:
                self.setNameText(lxBasic._toStringPrettify(key))
        if value:
            enabled, description = value
            self.setChecked(enabled)
            self.setDescription(description)
    #
    def getMainData(self):
        key = self.mainWidget.datum()
        enabled = self.mainWidget.isChecked()
        description = self.descriptionLabel.datum()
        return key, enabled, description
    #
    def setSubData(self, messages, isExpanded=False):
        if messages:
            for i in messages:
                if i:
                    setKey, setUiKey, setData, defData, uiData = i
                    widget = xEntryLabel()
                    widget.setExplainToolTip(setKey)
                    widget.setNameText(setUiKey)
                    widget.setWidth(240)
                    widget.key = setKey
                    #
                    if isinstance(uiData, bool):
                        widget.setDefaultDatum(defData)
                        widget.setChecked(setData)
                        widget.setCheckEnable(True)
                    elif isinstance(uiData, int):
                        widget.setDefaultDatum(defData)
                        widget.setDatum(setData)
                        widget.setLockVisible(True)
                    elif isinstance(uiData, float):
                        widget.setDefaultDatum(defData)
                        widget.setDatum(setData)
                        widget.setLockVisible(True)
                    elif isinstance(uiData, str) or isinstance(uiData, unicode):
                        widget.setDefaultDatum(defData)
                        widget.setDatum(setData)
                        widget.setLockVisible(True)
                    elif isinstance(uiData, tuple):
                        widget.setDefaultDatum(defData)
                        widget.setDatum(setData)
                        widget.setLockVisible(True)
                    elif isinstance(uiData, list):
                        widget.setDefaultDatum(defData)
                        widget.setDatumLis(uiData)
                        widget.setChooseEnable(True)
                        widget.setChoose(setData)
                    elif isinstance(uiData, dict):
                        widget.setExtendDatumDic(uiData)
                        dic = lxBasic.orderedDict()
                        for k, (ik, iv) in uiData.items():
                            dic[ik] = iv
                        if setData in dic.keys():
                            widget.setChoose(dic[setData])
                    #
                    self.subItemLayout.addWidget(widget)
                    #
                    self._itemModelLis.append(widget)
            #
            self.mainWidget.setExpandable(True)
            self.setExpanded(isExpanded)
    #
    def getSubData(self):
        dic = {}
        if self._itemModelLis:
            for i in self._itemModelLis:
                value = i.datum()
                key = i.key
                dic[key] = value
        return dic
    #
    def getItemData(self):
        pass
    #
    def setFilterColor(self, color):
        if color is not None:
            self.mainWidget.setFilterColor(color)
    #
    def filterColor(self):
        return self.mainWidget.filterColor()
    #
    def setExpandWidgetVisibleSwitch(self):
        self.subItemWidget.setVisible(self.subItemWidget.isHidden())
    #
    def initUi(self):
        self._itemModelLis = []
    #
    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(QtCore.Qt.AlignTop)
        #
        self.mainWidget = xCheckItemWidget()
        layout.addWidget(self.mainWidget)
        self.mainWidget.clicked.connect(self.setExpandWidgetVisibleSwitch)
        #
        self.subItemWidget = QWidget()
        self.subItemWidget.hide()
        layout.addWidget(self.subItemWidget)
        #
        self.subItemLayout = QVBoxLayout(self.subItemWidget)
        self.subItemLayout.setContentsMargins(0, 0, 0, 0)
        self.subItemLayout.setSpacing(0)
        #
        self.descriptionLabel = xEntryBox()
        self.mainWidget.addWidget(self.descriptionLabel)


#
class xRegisterListViewBox(QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def addItem(self, item):
        self._itemCount += 1
        item.setIndex(self._itemCount)
        self._itemModelLis.append(item)
        self._scrollBox.addWidget(item)
    #
    def addWidget(self, widget):
        self._scrollBox.addWidget(widget)
    #
    def items(self):
        return self._itemModelLis
    #
    def itemNames(self):
        lis = []
        if self._itemModelLis:
            lis = [i.datum() for i in self._itemModelLis if i.datum() is not None]
        return lis
    #
    def itemCount(self):
        return self._itemCount
    #
    def clearItems(self):
        if self._itemModelLis:
            [i.deleteLater() for i in self._itemModelLis]
            self._itemCount = 0
            self._itemModelLis = []
    #
    def setupUiStyle(self):
        pass
    #
    def initUi(self):
        self._itemCount = 0
        self._itemModelLis = []
        self._itemNames = []
    #
    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        #
        self._scrollBox = uiCore.QScrollArea_()
        layout.addWidget(self._scrollBox)


#
class UiExpandWidget(QWidget):
    expanded = uiCore.uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(UiExpandWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def addWidget(self, widget):
        self._layout.addWidget(widget)
    #
    def setExpanded(self, boolean):
        self._isExpanded = boolean
        self._expandAction()
    #
    def setExpandDir(self, expandDir):
        self._expandDir = expandDir
        #
        self._updateExpandDir()
        #
        self._updateUiPressStyle()
    #
    def _updateExpandDir(self):
        if self._expandDir == uiCore.LeftDir:
            self._mainLayout.setContentsMargins(self._sideWidth, 0, 0, 0)
        else:
            self._mainLayout.setContentsMargins(0, 0, self._sideWidth, 0)
    #
    def isExpanded(self):
        return self._isExpanded
    #
    def leaveEvent(self, event):
        self._isPressHovered = False
        self._updateUiPressStyle()
    #
    def mousePressEvent(self, event):
        isEnable = False
        if event.button() == QtCore.Qt.LeftButton:
            if self._pressPath is not None:
                if self._pressPath.contains(event.pos()):
                    isEnable = True
            #
            self._pressFlag, self._dragFlag = True, False
        #
        self._isAvailablePress = isEnable
        #
        event.ignore()
    #
    def mouseMoveEvent(self, event):
        isEnable = False
        if event.buttons() == QtCore.Qt.NoButton:
            if self._pressPath is not None:
                if self._pressPath.contains(event.pos()):
                    isEnable = True
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                #
                self._pressFlag, self._dragFlag = False, True
        #
        self._isPressHovered = isEnable
        #
        self._updateUiPressStyle()
        #
        event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self._pressFlag is True:
                if self._isAvailablePress:
                    self.setExpandSwitch()
                    #
                    self._isPressHovered = False
                    self._updateUiPressStyle()
        #
        self._pressFlag, self._dragFlag = False, False
        #
        event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        #
        h = self._buttonHeight
        #
        width = self.width()
        height = self.height()
        #
        w = self._sideWidth
        #
        yPos = 0
        gap = 2
        #
        if self._expandDir == uiCore.LeftDir:
            xPos = 0
            framePointLis = (
                (xPos, yPos + (height - h) / 2 + w - gap),
                (w - gap, yPos + (height - h) / 2 - 1),
                (w - gap, yPos + (height + h) / 2 - 1),
                (xPos, yPos + (height + h) / 2 - w + gap - 1),
                (xPos, yPos + (height - h) / 2 + w - gap)
            )
        else:
            xPos = width - w
            framePointLis = (
                (xPos + gap, yPos + (height - h) / 2),
                (width - 1, yPos + (height - h) / 2 + w - gap - 1),
                (width - 1, yPos + (height + h) / 2 - w + gap - 1),
                (xPos + gap, yPos + (height + h) / 2 - 2),
                (xPos + gap, yPos + (height - h) / 2)

            )
        painter.setBorderRgba(self._uiBorderRgba)
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        #
        self._pressPath = uiCore.QPainterPath_()
        self._pressPath._addPoints(framePointLis)
        #
        painter.drawPath(self._pressPath)
        #
        if self._expandDir == uiCore.LeftDir:
            rect = QtCore.QRect(
                xPos - gap + (w - self._uiIconWidth + gap) / 2, (height - self._uiIconHeight) / 2,
                self._uiIconWidth, self._uiIconHeight
            )
        else:
            rect = QtCore.QRect(
                xPos + gap + (w - self._uiIconWidth - gap) / 2, (height - self._uiIconHeight) / 2,
                self._uiIconWidth, self._uiIconHeight
            )
        #
        painter.setDrawImage(rect, self._expandBoxIcon)
    #
    def eventFilter(self, widget, event):
        # Filter by Widget is Press
        if widget == self._widget:
            if event.type() == QtCore.QEvent.DragMove:
                return True
        return False
    #
    def setExpandSwitch(self):
        self._isExpanded = not self._isExpanded
        #
        self.expanded.emit()
        #
        self._expandAction()
    #
    def _expandAction(self):
        self._widget.setVisible(self._isExpanded)
        #
        self._updateMinimumWidth()
        self._updateUiPressStyle()
    #
    def _updateUiPressStyle(self):
        self._setUiPressStyle([uiCore.UnexpandState, uiCore.ExpandedState][self._isExpanded])
    #
    def isPressHovered(self):
        return self._isPressHovered
    #
    def _setUiPressStyle(self, state):
        r1, g1, b1, a1 = 143, 143, 143, 255
        if state is uiCore.ExpandedState:
            self._uiBackgroundRgba = 71, 71, 71, 255
            self._uiBorderRgba = [(r1*.75, g1*.75, b1*.75, a1), (r1, g1, b1, a1)][self.isPressHovered()]
            if self._expandDir == uiCore.LeftDir:
                self._expandIconKeyword = 'svg_basic@svg#retract_v_right'
            else:
                self._expandIconKeyword = 'svg_basic@svg#retract_v_left'
        else:
            self._uiBackgroundRgba = 63, 63, 63, 255
            self._uiBorderRgba = [(r1*.5, g1*.5, b1*.5, a1), (r1*.75, g1*.75, b1*.75, a1)][self.isPressHovered()]
            if self._expandDir == uiCore.LeftDir:
                self._expandIconKeyword = 'svg_basic@svg#retract_v_left'
            else:
                self._expandIconKeyword = 'svg_basic@svg#retract_v_right'
        #
        self._expandBoxIcon = uiCore._toLxOsIconFile(self._expandIconKeyword + ['', 'on'][self.isPressHovered()])
        #
        self.update()
    #
    def setUiWidth(self, value):
        self.setMaximumWidth(value)
        self._defaultWidth = value
        #
        self._widget.setMaximumWidth(value - self._sideWidth - 1)
        self._widget.setMinimumWidth(value - self._sideWidth - 1)
        #
        self._updateMinimumWidth()
    #
    def _updateMinimumWidth(self):
        self.setMinimumWidth([self._sideWidth, self._defaultWidth][self._isExpanded])
    #
    def initUi(self):
        self._pressFlag, self._dragFlag = False, False
        self._isAvailablePress = False
        #
        self._isPressHovered = False
        #
        self._uiBackgroundRgba = 71, 71, 71, 255
        self._uiBorderRgba = 95, 95, 95, 255
        #
        self._buttonHeight = 120
        #
        self._sideWidth = 20
        self._defaultWidth = 20
        #
        self._uiIconWidth = 16
        self._uiIconHeight = 32
        #
        self._pressPath = None
        self._isExpanded = True
        #
        self._expandDir = uiCore.RightDir
        #
        self._expandIconKeyword = 'svg_basic@svg#retract_v_left'
        self._expandBoxIcon = uiCore._toLxOsIconFile(self._expandIconKeyword)
    #
    def setupUi(self):
        self._mainLayout = QHBoxLayout(self)
        self._mainLayout.setSpacing(0)
        #
        self._updateExpandDir()
        #
        self._widget = uiCore.QWidget_(self)
        self._mainLayout.addWidget(self._widget)
        self._layout = QVBoxLayout(self._widget)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        #
        self._widget.installEventFilter(self)


#
class xTreeLabelBar(QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )
        #
        self._layout = uiCore.QHBoxLayout_(self)
        self._layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(2)
        #
        self.actionTitle = None
        self.actionData = []
        #
        self.setUiSize()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._clickFlag = True
            #
            event.ignore()
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
        else:
            event.ignore()
    @uiWidgetBasic.uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiWidgetBasic.uiActionViewDropMethod
    def _menuDropAction(self):
        pass
    #
    def addItem(self, iconKeyword, state=None):
        itemWidget = xIconLabel()
        if iconKeyword:
            if state is not None:
                itemWidget.setIcon((iconKeyword, 'state@svg#%s' % state))
            else:
                itemWidget.setIcon((iconKeyword, None))
        self._layout.addWidget(itemWidget)
    #
    def setAlignment(self, horizontal):
        if horizontal == 'left':
            self._layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        if horizontal == 'center':
            self._layout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        if horizontal == 'right':
            self._layout.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(166667, 20))
        self.setMinimumSize(QtCore.QSize(0, 20))
