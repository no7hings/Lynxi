# coding:utf-8
from LxBasic import bscMethods
#
from LxGui.qt import qtCore, guiQtWgtAbs
#
from LxGui.qt.guiQtModels import _guiQtMdlGraphitem

from . import _guiQtWgtBasic
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
none = ''


#
class xGraphNodeItem(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(xGraphNodeItem, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def enterEvent(self, event):
        self._itemModel._gui_qt__set_enter_event_update_(event)
    #
    def leaveEvent(self, event):
        self._itemModel._gui_qt__set_leave_event_update_(event)
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
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHints(painter.Antialiasing | painter.SmoothPixmapTransform)
        # Shadow
        painter.setBorderRgba((0, 0, 0, 64))
        painter.setBackgroundRgba((0, 0, 0, 64))
        painter.drawRoundedRect(
            self._itemModel._shadowRect,
            self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
            QtCore.Qt.AbsoluteSize
        )
        # Background
        painter.setBorderRgba(self._wgt__border_rgba)
        painter.setBackgroundRgba(self._wgt__background_rgba)
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
            painter._gui_qt__set_image_draw_(self._itemModel._uiIconRect, icon)
            painter.device()
        if self._itemModel._type is not None:
            painter.setFont(
                qtCore.qtFont(size=self._itemModel._uiFontSize, weight=75, family=qtCore._families[1])
            )
            painter.setBorderRgba(self._wgt__border_rgba)
            painter.drawText(
                self._itemModel._gui_qt__mdl__type_str_Rect,
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
                bscMethods.StrUnderline.toCamelcase(self._itemModel._type)
            )

        # painter.end()  # for pyside2

    @_guiQtWgtBasic.gui_qt__mdf__set_actionview_event_filter
    def eventFilter(self, *args):
        return False
    #
    def setIndex(self, value):
        self._itemModel.setIcon(value)
    #
    def setIcon(self, iconKeywordStr):
        self._itemModel.setIcon(iconKeywordStr)
    #
    def setNameString(self, string):
        self._itemModel.setNameString(string)
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
        self._wgt__border_rgba = 127, 127, 127, 255
        self._wgt__background_rgba = 127, 127, 127, 127
        #
        self._uiConnectBorderRgba = 127, 127, 127, 255
        self._uiInputConnectionBackgroundRgba = 95, 95, 95, 255
        self._uiOutputConnectionBackgroundRgba = 95, 95, 95, 255
        #
        self._uiAttributeBorderRgba = 127, 127, 127, 255
    #
    def setupUi(self):
        self._itemModel = _guiQtMdlGraphitem.xGraphNodeItemModel(self)


#
class xGraphGroupItem(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(xGraphGroupItem, self)
            self._clsSuper.__init__(*args, **kwargs)
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
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

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
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        painter.drawRoundedRect(
            self._itemModel._uiBasicRect,
            self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
            QtCore.Qt.AbsoluteSize
        )
        #
        if self._itemModel._isExpanded is False:
            painter.setBackgroundRgba(self._wgt__border_rgba)
            #
            if self._itemModel._isInputConnectionEnable:
                painter.drawEllipse(self._itemModel._inputConnectionRect)
            if self._itemModel._isOutputConnectionEnable:
                painter.drawEllipse(self._itemModel._outputConnectionRect)
            #
            painter.setFont(
                qtCore.qtFont(size=self._itemModel._uiFontSize, weight=75, family=qtCore._families[1])
            )
            painter.setBorderRgba(self._wgt__border_rgba)
            painter.drawText(
                self._itemModel._gui_qt__mdl__type_str_Rect,
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
                bscMethods.StrUnderline.toCamelcase(self._itemModel._type)
            )

        # painter.end()  # for pyside2
    #
    def setColor(self, r, g, b):
        self._wgt__border_rgba = r, g, b, 255
        self._wgt__background_rgba = r, g, b, 32
    #
    def initUi(self):
        self._wgt__border_rgba = 127, 127, 127, 255
        self._wgt__background_rgba = 127, 127, 127, 32
        #
        self._uiConnectBorderRgba = 127, 127, 127, 255
        self._uiInputConnectionBackgroundRgba = 95, 95, 95, 255
        self._uiOutputConnectionBackgroundRgba = 95, 95, 95, 255
    #
    def setupUi(self):
        self._itemModel = _guiQtMdlGraphitem.xGraphGroupItemModel(self)


#
class xGraphExplainItem(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(xGraphExplainItem, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def enterEvent(self, event):
        self._itemModel._gui_qt__set_enter_event_update_(event)
    #
    def leaveEvent(self, event):
        self._itemModel._gui_qt__set_leave_event_update_(event)
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._itemModel._gui_qt__mdl__set_mouse_press_event_update_(event)
            event.accept()
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._itemModel._gui_qt__mdl__set_mouse_release_event_update_(event)
            event.accept()
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self._itemModel._gui_qt__mdl__set_mouse_press_move_event_update_(event)
            event.accept()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setFont(self.font())
        #
        if self._itemModel._isExpandEnable is True:
            painter.setDrawExpandPattern(
                self._itemModel._uiExpandRect, .75,
                self._itemModel._isExpanded,
                self._wgt__background_rgba, self._wgt__name_rgba
            )
        #
        if self._itemModel._gui_qt__mdl__name_str_ is not None:
            painter.setBorderRgba(self._wgt__name_rgba)
            painter.drawText(
                self._itemModel._gui_qt__mdl__name_str_Rect,
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignHCenter,
                self._itemModel._gui_qt__mdl__name_str_
            )
        #
        if self._itemModel._gui_qt__mdl__index_str_ is not None:
            painter.setFont(qtCore.qtFont(size=8, weight=50, family=qtCore._families[0]))
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(
                self._itemModel._gui_qt__mdl__index_str_Rect,
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTop,
                self._itemModel._gui_qt__mdl__index_str_
            )

        # painter.end()  # for pyside2
    #
    def setNameString(self, string, color=None):
        self._itemModel.setNameString(string)
    #
    def setIndex(self, value):
        self._itemModel.setIndex(value)
    #
    def setProxyItem(self, item):
        self._itemModel.setProxyItem(item)
    #
    def initUi(self):
        self._wgt__border_rgba = 127, 127, 127, 255
        self._wgt__background_rgba = 71, 71, 71, 255
        #
        self._uiIndexRgba = 127, 127, 127, 255
        self._wgt__name_rgba = 191, 191, 191, 255
        #
        self.setFont(qtCore.qtFont(size=10, weight=50, family=qtCore._families[0]))
    #
    def setupUi(self):
        self._itemModel = _guiQtMdlGraphitem.xGraphExplainItemModel(self, (qtCore.CLS_point, qtCore.CLS_rect))


#
class xGraphConnectionItem(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(xGraphConnectionItem, self)
            self._clsSuper.__init__(*args, **kwargs)
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
            self._itemModel._gui_qt__mdl__set_mouse_move_event_update_(event)
            #
            event.ignore()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHints(painter.Antialiasing | painter.SmoothPixmapTransform)
        #
        pen, brush = qtCore.getGradientColor(
            self._itemModel._startPoint, self._itemModel._endPoint,
            self._itemModel._drawDir,
            self._itemModel._isSelected, self._itemModel._isPressHovered
        )
        #
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(self._itemModel._curvePath)

        # painter.end()  # for pyside2
    #
    def setIndex(self, value):
        self._itemModel.setIndex(value)
    #
    def initUi(self):
        self._wgt__border_rgba = 0, 0, 0, 0
        self._wgt__background_rgba = 0, 0, 0, 0
    #
    def setupUi(self):
        self._itemModel = _guiQtMdlGraphitem.xGraphConnectionItemModel(self)


#
class xGraphAttributePortItem(guiQtWgtAbs.AbsGuiQtViewWgt):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(xGraphAttributePortItem, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtViewWgt()
        #
        self.setupUi()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
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
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        painter.drawRoundedRect(
            self._itemModel._uiBasicRect,
            self._itemModel._uiWidthRound, self._itemModel._uiHeightRound,
            QtCore.Qt.AbsoluteSize
        )
        #
        maxRow, minRow = self.itemModel().maxViewVisibleRow(), self.itemModel().minViewVisibleRow()
        widgetMargins = self.itemModel().widgetMargins()
        x, y = widgetMargins[0], widgetMargins[2]
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

        # painter.end()  # for pyside2
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._itemModel = _guiQtMdlGraphitem.xGraphAttributePortItemModel(self)
        self._viewModel = self._itemModel
