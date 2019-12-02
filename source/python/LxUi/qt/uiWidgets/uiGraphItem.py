# coding:utf-8
from LxCore import lxConfigure
#
from LxUi import uiCore
#
from LxUi.qt.uiBasic import uiWidgetBasic
#
from LxUi.qt.uiModels import uiGraphItemModel
#
QtGui = uiCore.QtGui
QtCore = uiCore.QtCore
#
_point = QtCore.QPoint
_pointF = QtCore.QPointF
_line = QtCore.QLine
_rect = QtCore.QRect
_rectF = QtCore.QRectF
#
_color = QtGui.QColor
_path = QtGui.QPainterPath
#
_families = lxConfigure.Lynxi_Ui_Family_Lis
#
none = ''


#
class xGraphNodeItem(uiCore.QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(xGraphNodeItem, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def enterEvent(self, event):
        self._itemModel._hoverStartAction(event)
    #
    def leaveEvent(self, event):
        self._itemModel._hoverStopAction(event)
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            # Press
            self._itemModel._pressSelectAction(event)
            # Drag
            self._itemModel._dragMoveStartAction(event)
            event.accept()
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            # Press
            self._itemModel._releaseSelectAction()
            # Drag
            self._itemModel._dragMoveStopAction()
            #
            self._itemModel._attributeDropAction(event)
            event.accept()
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # Press
            self._itemModel._dragSelectAction()
            # Drag
            self._itemModel._dragMoveExecuteAction(event)
            event.accept()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        # Shadow
        painter.setBorderRgba((0, 0, 0, 64))
        painter.setBackgroundRgba((0, 0, 0, 64))
        painter.drawRoundedRect(
            self._itemModel._shadowRect,
            self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
            QtCore.Qt.AbsoluteSize
        )
        # Background
        painter.setBorderRgba(self._uiBorderRgba)
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.drawRoundedRect(
            self._itemModel._uiBasicRect,
            self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
            QtCore.Qt.AbsoluteSize
        )
        # Connection
        painter.setBorderRgba((0, 0, 0, 64))
        painter.setBackgroundRgba((0, 0, 0, 64))
        painter.drawEllipse(self._itemModel._inputConnectionShadowRect)
        painter.drawEllipse(self._itemModel._outputConnectionShadowRect)
        #
        painter.setBackgroundRgba(self._uiInputConnectionBackgroundRgba)
        painter.setBorderRgba(self._uiConnectBorderRgba)
        painter.drawEllipse(self._itemModel._inputConnectionRect)
        #
        painter.setBackgroundRgba(self._uiOutputConnectionBackgroundRgba)
        painter.setBorderRgba(self._uiConnectBorderRgba)
        painter.drawEllipse(self._itemModel._outputConnectionRect)
        #
        if self._itemModel._uiIcon is not None:
            icon = QtGui.QPixmap(self._itemModel._uiIcon)
            painter.drawPixmap(self._itemModel._uiIconRect, icon)
        if self._itemModel._type is not None:
            painter.setFont(
                uiCore.xFont(size=self._itemModel._uiFontSize, weight=75, family=uiCore._families[1])
            )
            painter.setBorderRgba(self._uiBorderRgba)
            painter.drawText(
                self._itemModel._uiTypeTextRect,
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
                uiCore.prettify(self._itemModel._type)
            )
    @uiWidgetBasic.uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    #
    def setIndex(self, value):
        self._itemModel.setIcon(value)
    #
    def setIcon(self, iconKeyword):
        self._itemModel.setIcon(iconKeyword)
    #
    def setNameText(self, string):
        self._itemModel.setNameText(string)
    #
    def setType(self, string):
        self._itemModel.setType(string)
    #
    def setViewModel(self, model):
        self._itemModel.setViewModel(model)
    #
    def setInputAttributes(self, lis):
        self._itemModel.setInputAttributes(lis)
    #
    def setOutputAttributes(self, lis):
        self._itemModel.setOutputAttributes(lis)
    #
    def setSelected(self, boolean):
        self._itemModel.setSelected(boolean)
    #
    def isSelected(self):
        return self._itemModel.isSelected()
    #
    def index(self):
        return self._itemModel.index()
    #
    def initUi(self):
        self._uiBorderRgba = 127, 127, 127, 255
        self._uiBackgroundRgba = 127, 127, 127, 127
        #
        self._uiConnectBorderRgba = 127, 127, 127, 255
        self._uiInputConnectionBackgroundRgba = 95, 95, 95, 255
        self._uiOutputConnectionBackgroundRgba = 95, 95, 95, 255
        #
        self._uiAttributeBorderRgba = 127, 127, 127, 255
    #
    def setupUi(self):
        self._itemModel = uiGraphItemModel.xGraphNodeItemModel(self)


#
class xGraphGroupItem(uiCore.QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(xGraphGroupItem, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._itemModel._pressSelectAction(event)
            # Drag
            self._itemModel._dragMoveStartAction(event)
            #
            event.accept()
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            # Drag
            self._itemModel._dragMoveStopAction()
            #
            event.accept()
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # Drag
            self._itemModel._dragMoveExecuteAction(event)
            #
            event.accept()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        #
        if self._itemModel._isPressCurrent is False:
            painter.setBrushStyle(QtCore.Qt.FDiagPattern)
        else:
            painter.setBackgroundRgba(0, 0, 0, 0)
            painter.setBorderRgba(255, 255, 255, 255)
            painter.drawRoundedRect(
                self._itemModel._rimRect,
                self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
                QtCore.Qt.AbsoluteSize
            )
        #
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRoundedRect(
            self._itemModel._uiBasicRect,
            self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
            QtCore.Qt.AbsoluteSize
        )
        #
        if self._itemModel._isExpanded is False:
            painter.setBackgroundRgba(self._uiBorderRgba)
            #
            if self._itemModel._isInputConnectionEnable:
                painter.drawEllipse(self._itemModel._inputConnectionRect)
            if self._itemModel._isOutputConnectionEnable:
                painter.drawEllipse(self._itemModel._outputConnectionRect)
            #
            painter.setFont(
                uiCore.xFont(size=self._itemModel._uiFontSize, weight=75, family=uiCore._families[1])
            )
            painter.setBorderRgba(self._uiBorderRgba)
            painter.drawText(
                self._itemModel._uiTypeTextRect,
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
                uiCore.prettify(self._itemModel._type)
            )
    #
    def setColor(self, r, g, b):
        self._uiBorderRgba = r, g, b, 255
        self._uiBackgroundRgba = r, g, b, 32
    #
    def initUi(self):
        self._uiBorderRgba = 127, 127, 127, 255
        self._uiBackgroundRgba = 127, 127, 127, 32
        #
        self._uiConnectBorderRgba = 127, 127, 127, 255
        self._uiInputConnectionBackgroundRgba = 95, 95, 95, 255
        self._uiOutputConnectionBackgroundRgba = 95, 95, 95, 255
    #
    def setupUi(self):
        self._itemModel = uiGraphItemModel.xGraphGroupItemModel(self)


#
class xGraphExplainItem(uiCore.QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(xGraphExplainItem, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def enterEvent(self, event):
        self._itemModel._hoverStartAction(event)
    #
    def leaveEvent(self, event):
        self._itemModel._hoverStopAction(event)
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._itemModel._pressStartAction(event)
            event.accept()
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._itemModel._pressStopAction(event)
            event.accept()
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self._itemModel._pressExecuteAction(event)
            event.accept()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setFont(self.font())
        #
        if self._itemModel._isExpandEnable is True:
            painter.setDrawExpandPattern(
                self._itemModel._uiExpandRect, .75,
                self._itemModel._isExpanded,
                self._uiBackgroundRgba, self._uiNameRgba
            )
        #
        if self._itemModel._uiNameText is not None:
            painter.setBorderRgba(self._uiNameRgba)
            painter.drawText(
                self._itemModel._uiNameTextRect,
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignHCenter,
                self._itemModel._uiNameText
            )
        #
        if self._itemModel._uiIndexText is not None:
            painter.setFont(uiCore.xFont(size=8, weight=50, family=uiCore._families[0]))
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(
                self._itemModel._uiIndexTextRect,
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTop,
                self._itemModel._uiIndexText
            )
    #
    def setNameText(self, string, color=None):
        self._itemModel.setNameText(string)
    #
    def setIndex(self, value):
        self._itemModel.setIndex(value)
    #
    def setProxyItem(self, item):
        self._itemModel.setProxyItem(item)
    #
    def initUi(self):
        self._uiBorderRgba = 127, 127, 127, 255
        self._uiBackgroundRgba = 71, 71, 71, 255
        #
        self._uiIndexRgba = 127, 127, 127, 255
        self._uiNameRgba = 191, 191, 191, 255
        #
        self.setFont(uiCore.xFont(size=10, weight=50, family=uiCore._families[0]))
    #
    def setupUi(self):
        self._itemModel = uiGraphItemModel.xGraphExplainItemModel(self, (_point, _rect))


#
class xGraphConnectionItem(uiCore.QWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(xGraphConnectionItem, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setMouseTracking(True)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._itemModel._pressSelectAction(event)
            #
            event.ignore()
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self._itemModel._hoverExecuteAction(event)
            #
            event.ignore()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        #
        pen, brush = uiCore.getGradientColor(
            self._itemModel._startPoint, self._itemModel._endPoint,
            self._itemModel._drawDir,
            self._itemModel._isSelected, self._itemModel._isPressHovered
        )
        #
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(self._itemModel._curvePath)
    #
    def setIndex(self, value):
        self._itemModel.setIndex(value)
    #
    def initUi(self):
        self._uiBorderRgba = 0, 0, 0, 0
        self._uiBackgroundRgba = 0, 0, 0, 0
    #
    def setupUi(self):
        self._itemModel = uiGraphItemModel.xGraphConnectionItemModel(self)


#
class xGraphAttributePortItem(uiWidgetBasic._UiViewBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(xGraphAttributePortItem, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initViewBasic()
        #
        self.setupUi()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        # Shadow
        painter.setBorderRgba((0, 0, 0, 64))
        painter.setBackgroundRgba((0, 0, 0, 64))
        painter.drawRoundedRect(
            self._itemModel._shadowRect,
            self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
            QtCore.Qt.AbsoluteSize
        )
        # Basic
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRoundedRect(
            self._itemModel._uiBasicRect,
            self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
            QtCore.Qt.AbsoluteSize
        )
        #
        maxRow, minRow = self.itemModel().maxViewVisibleRow(), self.itemModel().minViewVisibleRow()
        margins = self.itemModel().margins()
        x, y = margins[0], margins[2]
        xValue, yValue = self.itemModel().value()
        _w, _h = 8, 8
        __w, __h = 4, 4
        w, h = self.itemModel()._gridSize()
        xOffset, yOffset = xValue % w, yValue % h
        x -= xOffset
        y -= yOffset
        #
        isExtendExpand = self.itemModel()._shiftFlag
        #
        indices = self.itemModel().visibleIndexes()
        if indices:
            for index in indices:
                row = self.itemModel().visibleRowAt(index)
                if minRow <= row <= maxRow:
                    itemModel = self.itemModel().itemModelVisibleAt(index)
                    if itemModel is not None:
                        isExpandable = itemModel.isExpandable()
                        if isExtendExpand is True:
                            isExpandHovered = itemModel.isExtendExpandHovered()
                            isParentExtendExpandHovered = itemModel.isParentExtendExpandHovered()
                        else:
                            isExpandHovered = itemModel.isExpandHovered()
                            isParentExtendExpandHovered = False
                        isExpanded = itemModel.isExpanded()
                        level = itemModel.itemLevel()
                        #
                        expandRect = itemModel.expandRect()
                        x_, y_ = expandRect.x(), expandRect.y()
                        w_, h_ = expandRect.width(), expandRect.height()
                        _x, _y = x + x_ + (w_ - _w) / 2, y + y_ + (h_ - _h) / 2
                        __x, __y = x + x_ + (w_ - __w) / 2, y + y_ + (h_ - __h) / 2
                        expandRect = QtCore.QRect(
                            _x, _y,
                            _w, _h
                        )
                        ellipseRect = QtCore.QRect(
                            __x, __y,
                            __w, __h
                        )
                        xc, yc = _x + _w / 2, _y + _h / 2
                        #
                        painter.setBackgroundRgba(0, 0, 0, 0)
                        if isExpandHovered:
                            painter.setBorderRgba(64, 255, 255, 255)
                        else:
                            painter.setBorderRgba(127, 127, 127, 255)
                        #
                        if isExpandable:
                            #
                            painter.drawRect(expandRect)
                            #
                            hLine = QtCore.QLine(
                                _x + 2, yc, _x + _w - 2, yc
                            )
                            painter.drawLine(hLine)
                            if not isExpanded:
                                vLine = QtCore.QLine(
                                    xc, _y + 2, xc, _y + _h - 2
                                )
                                painter.drawLine(vLine)
                        else:
                            if level > 0:
                                painter.drawRect(ellipseRect)
                        # Hierarchy Line
                        if level > 0:
                            painter.setBackgroundRgba(0, 0, 0, 0)
                            if isParentExtendExpandHovered:
                                painter.setBorderRgba(64, 255, 255, 255)
                            else:
                                painter.setBorderRgba(127, 127, 127, 255)
                            # Horizontal Line
                            if isExpandable:
                                _hLine = QtCore.QLine(
                                    xc - 20, yc, _x - 1, yc
                                )
                            else:
                                _hLine = QtCore.QLine(
                                    xc - 20, yc, __x - 1, yc
                                )
                            painter.drawLine(_hLine)
                            # Vertical line
                            isLast = itemModel.isLastVisibleChildIndex()
                            for l in range(level):
                                isPreParentLast = itemModel.isParentLastVisibleChildIndexFor(l - 1)
                                if isExtendExpand is True:
                                    isParentExpandHovered = itemModel.isParentExpandHoveredAt(l)
                                else:
                                    isParentExpandHovered = False
                                # Self Line
                                if isLast and l == 0:
                                    _vLine = QtCore.QLine(
                                        xc - 20 * (l + 1), y - (h - _h) / 2, xc - 20 * (l + 1), yc
                                    )
                                else:
                                    _vLine = QtCore.QLine(
                                        xc - 20 * (l + 1), y - (h - _h) / 2, xc - 20 * (l + 1), _y + _h
                                    )
                                #
                                if not isPreParentLast:
                                    if isParentExpandHovered is False:
                                        painter.setBorderRgba(127, 127, 127, 255)
                                    painter.drawLine(_vLine)
                        #
                        y += h
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._itemModel = uiGraphItemModel.xGraphAttributePortItemModel(self)
        self._viewModel = self._itemModel
