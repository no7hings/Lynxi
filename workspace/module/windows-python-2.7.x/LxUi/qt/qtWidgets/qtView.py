# coding:utf-8
from LxUi import uiCore
#
from LxUi.qt import qtCore
#
from LxUi.qt.qtObjects import qtAbcWidget
#
from LxUi.qt._qtModels import _qtViewModel
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
_families = uiCore.Lynxi_Ui_Family_Lis
#
none = ''


# Scroll Bar
class QtScrollBar(qtAbcWidget.QtAbcObj_Scrollbar):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcScrollbarWidget()


#
class QtScrollArea(qtCore.QWidget):
    scrollWidth = 20
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initScrollArea()
        #
        self.setupUi()
        #
        self.setUiSize()
    #
    def _initScrollArea(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding
        )
        #
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        #
        self._initScrollAreaUi()
    #
    def _initScrollAreaUi(self):
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 0, 0, 0, 0
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MidButton:
            self.setCursor(QtCore.Qt.OpenHandCursor)
            #
            self._viewModel._trackStartAction(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MidButton:
            self.setCursor(QtCore.Qt.ArrowCursor)
            #
            self._viewModel._trackStopAction(event)
        else:
            self.setCursor(QtCore.Qt.ArrowCursor)
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MidButton:
            self.setCursor(QtCore.Qt.ClosedHandCursor)
            #
            self._viewModel._trackExecuteAction(event)
        else:
            self.setCursor(QtCore.Qt.ArrowCursor)
            event.ignore()
    #
    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        #
        self._vScrollBar._viewModel._wheelAction(delta)
        self._vScrollBar._viewModel._hoverScrollAction()
        # After Scroll Action
        self._viewModel._updateAction()
    #
    def resizeEvent(self, event):
        self._viewModel.update()
        event.ignore()
    #
    def addWidget(self, widget):
        self._layout.addWidget(widget)
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
    def getHeight_(self):
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
    def setContentsMargins(self, *args):
        self._layout.setContentsMargins(*args)
    #
    def setSpacing(self, *args):
        self._layout.setSpacing(*args)
    #
    def setUiSize(self):
        self.setMinimumSize(60, 60)
    #
    def setupUi(self):
        self._viewport = qtCore.QWidget(self)
        #
        self._vScrollBar, self._hScrollBar = QtScrollBar(self), QtScrollBar(self)
        #
        self._layout = qtCore.QVBoxLayout_(self._viewport)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(QtCore.Qt.AlignTop)
        #
        self._viewModel = _qtViewModel.QtScrollareaModel(self)


#
class QtCheckview(qtAbcWidget.QtAbcObj_ViewWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcViewWidget()
        #
        self.setupUi()
    #
    def addWidget(self, widget):
        self.viewModel().addItem(widget)
    #
    def setupUi(self):
        self._viewModel = _qtViewModel.QtCheckviewModel(self)


#
class QtTreeview(qtAbcWidget.QtAbcObj_ViewWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcViewWidget()
        self._overrideUi()
        #
        self.setupUi()
    #
    def _overrideUi(self):
        self._uiBranchBorderRgba = 127, 127, 127, 255
        self._uiBranchBorderHoverRgba = 223, 223, 223, 255
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        elif event.button() == QtCore.Qt.MidButton:
            self.setCursor(QtCore.Qt.OpenHandCursor)
            #
            self.viewModel()._trackStartAction(event)
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Placeholder
        if self.viewModel().isPlaceholderEnable():
            painter.setDrawImage(
                self.viewModel().placeholderRect(),
                self.viewModel().placeholderImage()
            )
        #
        if self.viewModel().isFocusFrameEnable():
            if self.hasFocus():
                painter.setDrawDottedFrame(
                    self.viewModel()._uiFrameRect,
                    self._uiBackgroundRgba, self._uiBorderRgba
                )
        #
        maxRow, minRow = self.viewModel().maxViewVisibleRow(), self.viewModel().minViewVisibleRow()
        #
        margins = self.viewModel().margins()
        #
        x, y = margins[0], margins[2]
        xValue, yValue = self.viewModel().value()
        #
        ew, eh = self.viewModel().expandSize()
        #
        _w, _h = 8, 8
        __w, __h = 4, 4
        w, h = self.viewModel()._gridSize()
        if w > 0 and h > 0:
            xOffset, yOffset = xValue % w, yValue % h
            x -= xOffset
            y -= yOffset
            #
            isExtendExpand = self.viewModel()._shiftFlag
            #
            indexLis = self.viewModel().visibleIndexes()
            if indexLis:
                for index in indexLis:
                    row = self.viewModel().visibleRowAt(index)
                    if minRow <= row <= maxRow:
                        itemModel = self.viewModel().itemModelVisibleAt(index)
                        if itemModel is not None:
                            isExpandable = itemModel.isExpandable()
                            if isExtendExpand is True:
                                isExpandHovered = itemModel.isExtendExpandHovered()
                                isParentExtendExpandHovered = itemModel.isParentExtendExpandHovered()
                            else:
                                isExpandHovered = itemModel.isExpandHovered()
                                isParentExtendExpandHovered = False
                            #
                            isExpanded = itemModel.isExpanded()
                            level = itemModel.itemLevel()
                            #
                            expandRect = itemModel.expandRect()
                            x_, y_ = expandRect.x(), expandRect.y()
                            w_, h_ = expandRect.width(), expandRect.height()
                            #
                            _x, _y = x + x_ + (w_ - _w) / 2, y + y_ + (h_ - _h) / 2
                            __x, __y = x + x_ + (w_ - __w) / 2, y + y_ + (h_ - __h) / 2
                            #
                            expandRect_ = QtCore.QRect(
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
                            if isExpandHovered is True:
                                painter.setBorderRgba(self._uiBranchBorderHoverRgba)
                            else:
                                painter.setBorderRgba(self._uiBranchBorderRgba)
                            #
                            if isExpandable is True:
                                #
                                painter.drawRect(expandRect_)
                                #
                                hLine = QtCore.QLine(
                                    _x + 2, yc, _x + _w - 2, yc
                                )
                                painter.drawLine(hLine)
                                if isExpanded is False:
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
                                    painter.setBorderRgba(self._uiBranchBorderHoverRgba)
                                else:
                                    painter.setBorderRgba(self._uiBranchBorderRgba)
                                # Horizontal Line
                                if isExpandable is True:
                                    _hLine = QtCore.QLine(
                                        xc - ew, yc, _x - 1, yc
                                    )
                                else:
                                    _hLine = QtCore.QLine(
                                        xc - ew, yc, __x - 1, yc
                                    )
                                painter.drawLine(_hLine)
                                # Vertical line
                                isLast = itemModel.isLastVisibleChildIndex()
                                for subLevel in range(level):
                                    isPreParentLast = itemModel.isParentLastVisibleChildIndexFor(subLevel - 1)
                                    if isExtendExpand is True:
                                        isParentExpandHovered = itemModel.isParentExpandHoveredAt(subLevel)
                                    else:
                                        isParentExpandHovered = False
                                    # Self Line
                                    if isLast and subLevel == 0:
                                        _vLine = QtCore.QLine(
                                            xc - ew * (subLevel + 1), y - (h - _h) / 2, xc - ew * (subLevel + 1), yc
                                        )
                                    else:
                                        _vLine = QtCore.QLine(
                                            xc - ew * (subLevel + 1), y - (h - _h) / 2, xc - ew * (subLevel + 1), _y + _h
                                        )
                                    #
                                    if not isPreParentLast:
                                        if isParentExpandHovered is False:
                                            painter.setBorderRgba(self._uiBranchBorderRgba)
                                        #
                                        painter.drawLine(_vLine)
                            #
                            y += h

        # painter.end()
    @qtAbcWidget.actionviewEventFilterModifier
    def eventFilter(self, *args):
        return False
    @qtAbcWidget.actionviewDropModifier
    def _menuDropAction(self):
        pass
    #
    def setActionData(self, actions):
        lis = []
        lis.extend(self._uiPreActions)
        lis.extend(list(actions))
        #
        self.actionData = lis
        #
        self._vScrollBar.setActionData(self.actionData)
    #
    def setupUi(self):
        self._hScrollBar = QtScrollBar(self)
        self._vScrollBar = QtScrollBar(self)
        #
        self._viewModel = _qtViewModel.QtTreeviewModel(self)
        #
        self._uiPreActions = [
            ('Check',),
            ('Check All#Ctrl + A', 'svg_basic@svg#checkedAll', self._viewModel.isCheckEnable, self._viewModel.setCheckAll),
            ('Uncheck All', 'svg_basic@svg#uncheckedAll', self._viewModel.isCheckEnable, self._viewModel.setUncheckAll),
            ('Expand', ),
            ('Expand All', 'svg_basic@svg#expand', self._viewModel.isExpandEnable, self._viewModel.setExpandAll),
            ('Unexpand All', 'svg_basic@svg#contract', self._viewModel.isExpandEnable, self._viewModel.setUnexpandAll)
        ]
        self.actionData = self._uiPreActions
        self.actionTitle = 'Extra Action'
        #
        self._vScrollBar.setActionData(self.actionData)


#
class QtGridview(qtAbcWidget.QtAbcObj_ViewWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcViewWidget()
        #
        self.setupUi()
    #
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(True)
        elif event.key() == QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(True)
            self._vScrollBar._shiftFlag = True
        elif event.key() == QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(True)
        # Focus
        elif event.key() == QtCore.Qt.Key_F:
            self.viewModel().setCurrentVisibleCeiling()
        # Column Move
        elif event.key() == QtCore.Qt.Key_Left:
            self.viewModel()._columnTraceAction(-1)
        elif event.key() == QtCore.Qt.Key_Right:
            self.viewModel()._columnTraceAction(+1)
        # Row Move
        elif event.key() == QtCore.Qt.Key_Up:
            self.viewModel()._rowTraceAction(-1)
        elif event.key() == QtCore.Qt.Key_Down:
            self.viewModel()._rowTraceAction(+1)
        # Select All
        elif event.key() == QtCore.Qt.Key_A and event.modifiers() == QtCore.Qt.ControlModifier:
            self.viewModel().setCheckAll()
        # Show
        elif event.key() == QtCore.Qt.Key_1 and event.modifiers() == QtCore.Qt.ControlModifier:
            self.viewModel().setSortByIndex()
        elif event.key() == QtCore.Qt.Key_2 and event.modifiers() == QtCore.Qt.ControlModifier:
            self.viewModel().setSortByName()
        # View
        if event.modifiers() == QtCore.Qt.AltModifier and event.key() == QtCore.Qt.Key_1:
            self.viewModel().setListMode()
        elif event.modifiers() == QtCore.Qt.AltModifier and event.key() == QtCore.Qt.Key_2:
            self.viewModel().setIconMode()
        elif event.modifiers() == QtCore.Qt.AltModifier and event.key() == QtCore.Qt.Key_3:
            self.viewModel().setDetailMode()
        else:
            event.ignore()
        # After Key Press Action
        self.viewModel()._hoverScrollAction()
        #
        if self.viewModel()._curPressChangeFlag is True:
            self.currentChanged.emit()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        elif event.button() == QtCore.Qt.MidButton:
            self.setCursor(QtCore.Qt.OpenHandCursor)
            #
            self.viewModel()._trackStartAction(event)
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
        else:
            event.ignore()
    #
    def focusInEvent(self, event):
        self.update()
        event.ignore()
    #
    def focusOutEvent(self, event):
        self.update()
        event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Placeholder
        if self.viewModel().isPlaceholderEnable():
            painter.setDrawImage(
                self.viewModel().placeholderRect(),
                self.viewModel().placeholderImage()
            )
        # Frame
        if self.viewModel().isFocusFrameEnable():
            if self.hasFocus():
                painter.setDrawDottedFrame(
                    self.viewModel()._uiFrameRect,
                    self._uiBackgroundRgba, self._uiBorderRgba
                )

        # painter.end()
    @qtAbcWidget.actionviewEventFilterModifier
    def eventFilter(self, *args):
        return False
    @qtAbcWidget.actionviewDropModifier
    def _menuDropAction(self):
        pass
    #
    def setItemSize(self, width, height):
        self.viewModel().setItemSize(width, height)
        self.viewModel().setAbcObjItemWidgetSize(width, height)
    #
    def setItemListModeSize(self, width, height):
        self.viewModel().setItemListModeSize(width, height)
    #
    def setItemIconModeSize(self, width, height):
        self.viewModel().setItemIconModeSize(width, height)
    #
    def addItem(self, widget):
        self.viewModel().addItem(widget)
    #
    def setActionData(self, actions):
        lis = []
        lis.extend(self._uiPreActions)
        lis.extend(list(actions))
        #
        self.actionData = lis
        #
        self._vScrollBar.setActionData(self.actionData)
    #
    def setSortByIndex(self):
        self.viewModel().setSortByIndex(force=True)
    #
    def setSortByName(self):
        self.viewModel().setSortByName(force=True)
    #
    def setSelectAll(self):
        self.viewModel().setSelectAll()
    #
    def setSelectClear(self):
        self.viewModel().setSelectClear()
    #
    def setFilterConnect(self, widget):
        self.viewModel().setFilterConnect(widget)
    #
    def setFilterExplainRefresh(self):
        self.viewModel().setFilterExplainRefresh()
    #
    def setMainIndexFilter(self, viewFilterItemIndexes):
        indexLis = self.viewModel().itemIndexes()
        for i in indexLis:
            if i in viewFilterItemIndexes:
                self.setItemVisible(i, True)
            else:
                self.setItemVisible(i, False)
        #
        self.setFilterIndexLimit(viewFilterItemIndexes)
    #
    def setSubIndexFilter(self, viewFilterItemIndexes, boolean):
        if self._filterIndexesLimit:
            [self.setItemVisible(i, boolean) for i in viewFilterItemIndexes if i in self._filterIndexesLimit]
        else:
            self.setItemsVisible(viewFilterItemIndexes, not boolean)
    #
    def setItemVisible(self, index, boolean):
        self.itemAt(index).setVisible(boolean)
    #
    def setItemsVisible(self, indices, boolean):
        for i in indices:
            self.setItemVisible(i, not boolean)
    #
    def setFilterIndexLimit(self, indices):
        self._filterIndexesLimit = indices
    #
    def setSingleSelectionEnable(self, boolean):
        self.viewModel().setSingleSelectionEnable(boolean)
    #
    def setListModeEnable(self, boolean):
        self.viewModel().setListModeEnable(boolean)
        #
        self.setItemSize(0, 20)
    #
    def setListMode(self):
        self.viewModel().setListMode()
    #
    def setContentsMargins(self, *args):
        self.viewModel().setMargins(*args)
    #
    def _setQtPressStyle(self, state):
        if state == qtCore.NormalState:
            self._uiBackgroundRgba = 0, 0, 0, 0
            self._uiBorderRgba = 0, 0, 0, 0
        elif state == qtCore.OnState:
            self._uiBackgroundRgba = 0, 0, 0, 0
            self._uiBorderRgba = 0, 127, 127, 255
        #
        self.update()
    #
    def setupUi(self):
        self._hScrollBar = QtScrollBar(self)
        self._vScrollBar = QtScrollBar(self)
        #
        self._viewModel = _qtViewModel.QtGridviewModel(self)
        #
        self._uiPreActions = [
            ('Basic', ),
            (
                'Sort', 'svg_basic@svg#name',
                [
                    ('Default#Ctrl + 1', 'checkBox', self._viewModel.isSortByIndex, self._viewModel.setSortByIndex),
                    ('Name#Ctrl + 2', 'checkBox', self._viewModel.isSortByName, self._viewModel.setSortByName)
                ]
            ),
            (
                'View', 'svg_basic@svg#menu',
                [
                    ('List#Alt + 1', 'checkBox', self._viewModel.isListMode, self._viewModel.setListMode),
                    ('Icon#Alt + 2', 'checkBox', self._viewModel.isIconMode, self._viewModel.setIconMode),
                    ('Detail#Alt + 3', 'checkBox', self._viewModel.isDetailMode, self._viewModel.setDetailMode)
                ]
             ),
            ('Check', ),
            ('Check All#Ctrl + A', 'svg_basic@svg#checkedAll', self._viewModel.isCheckEnable, self._viewModel.setCheckAll),
            ('Uncheck All', 'svg_basic@svg#uncheckedAll', self._viewModel.isCheckEnable, self._viewModel.setUncheckAll)
        ]
        self.actionData = self._uiPreActions
        self.actionTitle = 'Extra Action'
        #
        self._vScrollBar.setActionData(self.actionData)


# Preset
class QtPresetview(qtAbcWidget.QtAbcObj_ViewWidget):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcViewWidget()
        #
        self.setupUi()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        elif event.button() == QtCore.Qt.MidButton:
            self.setCursor(QtCore.Qt.OpenHandCursor)
            #
            self.viewModel()._trackStartAction(event)
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
        else:
            event.ignore()
    @qtAbcWidget.actionviewEventFilterModifier
    def eventFilter(self, *args):
        return False
    @qtAbcWidget.actionviewDropModifier
    def _menuDropAction(self):
        pass
    #
    def setActionData(self, actions):
        lis = []
        lis.extend(self._uiPreActions)
        lis.extend(list(actions))
        #
        self.actionData = lis
        #
        self._vScrollBar.setActionData(self.actionData)
    #
    def setupUi(self):
        self._hScrollBar = QtScrollBar(self)
        self._vScrollBar = QtScrollBar(self)
        #
        self._viewModel = _qtViewModel.QtPresetviewModel(self)
        #
        self._uiPreActions = [
            ('Check',),
            ('Check All#Ctrl + A', 'svg_basic@svg#checkedAll', self._viewModel.isCheckEnable, self._viewModel.setCheckAll),
            ('Uncheck All', 'svg_basic@svg#uncheckedAll', self._viewModel.isCheckEnable, self._viewModel.setUncheckAll),
            ('Expand', ),
            ('Expand All', 'svg_basic@svg#expand', self._viewModel.isExpandEnable, self._viewModel.setExpandAll),
            ('Unexpand All', 'svg_basic@svg#contract', self._viewModel.isExpandEnable, self._viewModel.setUnexpandAll)
        ]
        self.actionData = self._uiPreActions
        self.actionTitle = 'Extra Action'
        #
        self._vScrollBar.setActionData(self.actionData)
