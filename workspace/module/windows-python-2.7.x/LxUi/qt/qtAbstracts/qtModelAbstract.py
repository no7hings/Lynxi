# coding:utf-8
import types
#
import math
#
from LxCore import lxBasic
#
from LxUi.qt import qtAbstract, qtAction, qtCore

#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
none = ''


# Basic Item
class Abc_QtItemModel(
    qtAbstract.QtItemModelAbs,
    qtAbstract.QtEnterItemModelAbs
):
    def _initItemModelBasic(self, widget):
        self._initItemModelAbs()
        self._initDatumEnterItemModelAbs()
        #
        self.setWidget(widget)
    #
    def _updateWidgetGeometry(self):
        pass
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        # noinspection PyUnusedLocal
        xOffset, yOffset = [0, 1][self._pressFlag], [0, 1][self._pressFlag]
        #
        width -= 1
        height -= 1
        #
        frameWidth, frameHeight = self._uiFrameWidth, self._uiFrameHeight
        iconWidth, iconHeight = self._uiIconWidth, self._uiIconHeight
        #
        indexWidth = self._uiIndexTextWidth
        #
        self._uiBasicRect.setRect(
            xPos, yPos,
            width, height
        )
        #
        xPos += self._uiOffset + self._uiSide
        # Check
        if self.isCheckEnable():
            iconWidth, iconHeight = self._uiCheckIconWidth, self._uiCheckIconHeight
            self.checkRect().setRect(
                xPos + (frameWidth - iconWidth)/2, yPos + (frameHeight - iconHeight)/2,
                iconWidth, iconHeight
            )
            xPos += frameWidth + self._uiSpacing
        # Color
        if self.isColorEnable():
            self._updateColorRect(xPos, yPos)
            xPos += frameWidth + self._uiSpacing
        # Expand
        if self.isExpandEnable():
            # Tree Item Offset
            xPos += self._uiExpandFrameWidth*self.itemLevel()
            self._updateExpandRect(xPos, yPos, width, height)
            #
            xPos += frameWidth + self._uiSpacing
        # Menu
        if self.isPressMenuEnable():
            self._updateMenuIconRect(xPos, yPos)
        # Icon and Sub Icon
        if self.icon() is not None:
            subIconWidth, subIconHeight = iconWidth*.75, iconHeight*.75
            if self.subIcon() is not None:
                self.iconRect().setRect(
                    xPos, yPos,
                    iconWidth, iconHeight
                )
                self.subIconRect().setRect(
                    xPos + (frameWidth - subIconWidth), yPos + (frameHeight - subIconHeight),
                    subIconWidth, subIconHeight
                )
            else:
                self.iconRect().setRect(
                    xPos + (frameWidth - iconWidth)/2, yPos + (frameHeight - iconHeight)/2,
                    iconWidth, iconHeight
                )
            if self.extendIcon() is not None:
                self.extendIconRect().setRect(
                    xPos + (self._uiExtendFrameWidth - self._uiExtendIconWidth)/2, yPos + (self._uiExtendFrameHeight - self._uiExtendIconHeight)/2,
                    self._uiExtendIconWidth, self._uiExtendIconHeight
                )
            #
            xPos += frameWidth + self._uiSpacing
        # Namespace
        if self.namespaceText() is not None:
            textWidth = self._textWidth(self.namespaceText())
            self._uiNamespaceRect.setRect(
                xPos, yPos,
                textWidth, frameHeight
            )
            xPos += textWidth
        # Name
        if self.nameText() is not None:
            self.nameTextRect().setRect(
                xPos, yPos,
                width - xPos - indexWidth, frameHeight
            )
        # SubName
        if self.uiSubName() is not None:
            self._uiSubNameRect.setRect(
                xPos, yPos,
                width - xPos, frameHeight
            )
        # Index
        if self.indexText() is not None:
            self._uiIndexTextRect.setRect(
                width - indexWidth - self._uiShadowRadius - self._uiSide, yPos,
                indexWidth, frameHeight
            )
    #
    def _updateGeometry(self):
        self._updateRectGeometry()
        #
        self._updateWidgetState()
    # Hover
    def _hoverStartAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            self.setPressHovered(True)
            #
            if self.isCheckButton():
                self.setCheckHovered(True)
            #
            event.ignore()
    #
    def _hoverExecuteAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            event.ignore()
    #
    def _hoverStopAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            self.setPressHovered(False)
            #
            if self.isCheckButton():
                self.setCheckHovered(False)
            #
            event.ignore()
    #
    def _pressStartAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            x, y = self._getEventPos(event)
            # Flag
            self._pressFlag, self._dragFlag = True, False
            # Check ( Check Emit Send First )
            self._checkClickSwitchAction()
            # Click
            self._clickedAction()
            #
            self._updateGeometry()
            self._updateQtPressStyle()
            #
            if self.isIconRectContain((x, y)):
                event.accept()
            else:
                event.ignore()
    #
    def _pressExecuteAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            x, y = self._getEventPos(event)
            # Flag
            self._pressFlag, self._dragFlag = False, True
            #
            self._updateGeometry()
            self._updateQtPressStyle()
            #
            if self.isIconRectContain((x, y)):
                event.accept()
            else:
                event.ignore()
    #
    def _pressStopAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            x, y = self._getEventPos(event)
            # Action
            self._releasedAction()
            # Flag
            self._pressFlag, self._dragFlag = False, False
            #
            self._updateGeometry()
            self._updateQtPressStyle()
            #
            if self.isIconRectContain((x, y)):
                event.accept()
            else:
                event.ignore()
    #
    def _clickedAction(self):
        self._clickedFlag, self._pressedFlag = True, False
        #
        if self.isPressable():
            self._pressedTimer.start(250)
            self.widget().clicked.emit()
            # Action
            self.acceptPressAction()
            # Command
            self.acceptPressCommand()
    #
    def _pressedAction(self):
        self._clickedFlag, self._pressedFlag = False, True
        #
        self.widget().pressed.emit()
    #
    def _releasedAction(self):
        self._pressedTimer.stop()
        #
        if self._pressFlag is True:
            self.widget().released.emit()
        #
        self._clickedFlag, self._pressedFlag = False, False
    # Override
    def _extendPressCurrentAction(self):
        parentItemModels = self.parentItemModels()
        if parentItemModels:
            [i.setSubSelected(self.isPressCurrent()) for i in parentItemModels]
    # Override
    def _extendPressSelectAction(self):
        parentItemModels = self.parentItemModels()
        if parentItemModels:
            if self.isSelected():
                [i.setSubSelected(True) for i in parentItemModels]
            else:
                [i.setSubSelected(False) for i in parentItemModels if not i.hasSelectedChildren()]
    #
    def _updateUiStyle(self):
        self._updateQtPressStyle()
        self._updateQtExpandStyle()
        self._updateQtCheckStyle()
    #
    def update(self):
        self._updateGeometry()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._pressedTimer = QtCore.QTimer(self._widget)
        self._pressedTimer.timeout.connect(self._pressedAction)
    #
    def filterColor(self):
        if self.isColorEnable():
            return self.widget()._uiColorBackgroundRgba
        else:
            return 96, 96, 96, 255
    #
    def setExclusiveChecked(self):
        viewModel = self.viewModel()
        if viewModel is not None:
            itemModels = viewModel.itemModels()
            if itemModels:
                [i.setChecked(False) for i in itemModels if not i == self and i.isChecked()]
            #
            self.setChecked(True)


# Basic View
class Abc_QtViewModel(
    qtAbstract.QtViewModelAbs,
    qtAbstract.QtScrollAreaModelAbs
):
    def _initViewModelBasic(self, widget):
        self._initViewModelAbs()
        self._initScrollViewModelAbs()
        #
        self._initViewModelBasicAction()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setScrollBar(widget)
    #
    def _initViewModelBasicAction(self):
        self._trackActionModel = qtAction.QtTrackactionModel(self)
        self._trackActionModel.setMinimumPos(0, 0)
    #
    def _itemSize(self):
        if self._itemMode == qtCore.ListMode:
            w, h = self._viewportWidth - self._vScrollWidth(), self._uiItemHeight
        elif self._itemMode == qtCore.IconMode:
            w, h = self._uiItemWidth, self._uiItemHeight
        else:
            w, h = (self._viewportWidth - self._uiSpacing*(self._visibleColumnCount - 1))/self._visibleColumnCount - self._vScrollWidth(), self._uiItemHeight
        return w, h
    # Override
    def _gridSize(self):
        if self._itemMode == qtCore.ListMode:
            w, h = self._viewportWidth - [0, self._uiVScrollWidth][self._isVScrollable], self._uiItemHeight + self._uiSpacing
        elif self._itemMode == qtCore.IconMode:
            w, h = self._uiItemWidth + self._uiSpacing, self._uiItemHeight + self._uiSpacing
        else:
            w, h = (self._viewportWidth + self._uiSpacing)/self._visibleColumnCount, self._uiItemHeight + self._uiSpacing
        return w, h
    # View
    def _updateViewSize(self):
        self._viewWidth = [self._absWidth, self._viewportWidth - self._vScrollWidth()][self.isHScrollable()]
        self._viewHeight = [self._absHeight, self._viewportHeight - self._hScrollHeight()][self.isVScrollable()]
    #
    def _updateTrackSize(self):
        self._trackWidth = self._absWidth - self._viewportWidth
        self._trackHeight = self._absHeight - self._viewportHeight
    #
    def _updateScrollSize(self):
        self._isHScrollable, self._isVScrollable = self._absWidth > self.width(), self._absHeight > self.height()
        if self.isHScrollEnable():
            self.hScrollBar().viewModel()._updateUnion(self.isVScrollable())
            self.hScrollBar().viewModel().setScrollable(self.isHScrollable())
        #
        if self.isVScrollEnable():
            self.vScrollBar()._viewModel._updateUnion(self.isHScrollable())
            self.vScrollBar().viewModel().setScrollable(self.isVScrollable())
    #
    def _updateWidgetGeometry(self):
        pass
    #
    def _updateViewportGeometry(self):
        xPos, yPos = self._uiMargins[0], self._uiMargins[1]
        width, height = self._viewportWidth, self._viewportHeight
        # Viewport
        self._viewport.setGeometry(
            xPos, yPos,
            width - self._vScrollWidth(), height
        )
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        # Placeholder
        if self.isPlaceholderEnable():
            x, y, w, h = self._uiMethod._toGeometryRemap(self.placeholderSize(), self.size())
            self.placeholderRect().setRect(
                x, y, w, h
            )
        #
        self._uiFrameRect.setRect(
            xPos, yPos,
            width - self._vScrollWidth() - 1, height - 1
        )
        if self.isSelectEnable():
            pass
        if self.isCheckEnable():
            pass
    #
    def _updateScrollBarGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        if self.isHScrollEnable():
            if self.isHScrollable():
                self.hScrollBar().show()
                self.hScrollBar().setGeometry(
                    xPos, yPos + height - self._uiHScrollWidth,
                    width, self._uiHScrollWidth
                )
                self.hScrollBar().viewModel().setAbsHeight(self._absWidth)
                self.hScrollBar().viewModel().update()
            else:
                if self.hScrollBar() is not None:
                    self.hScrollBar().hide()
        #
        if self.isVScrollEnable():
            if self.isVScrollable():
                self.vScrollBar().show()
                self.vScrollBar().setGeometry(
                    xPos + width - self._uiVScrollWidth, yPos,
                    self._uiVScrollWidth, height
                )
                self.vScrollBar().viewModel().setAbsHeight(self._absHeight)
                self.vScrollBar().viewModel().update()
            else:
                if self.vScrollBar() is not None:
                    self.vScrollBar().hide()
    #
    def _updateVisibleItemsGeometry(self):
        if self.visibleIndexCount() > 0:
            for itemIndex in self.visibleItemIndexes():
                itemModel = self.itemModelAt(itemIndex)
                #
                widget = itemModel.widget()
                if itemIndex in self._itemModelVisiblePosDic:
                    x, y = self.itemVisiblePosAt(itemIndex)
                    #
                    w, h = self._itemSize()
                    #
                    widget.setGeometry(
                        x, y,
                        w, h
                    )
                    #
                    widget.show()
                else:
                    widget.hide()
            #
            if self.itemMode() is qtCore.TreeMode:
                self._updateWidget()
    #
    def _updateItemHoverByVisibleHover(self):
        self.setItemHoveredVisibleAt(self._curHoverVisibleIndex)
    #
    def _updateItemHoveredByVisiblePress(self):
        self.setItemHoveredVisibleAt(self._pressVisibleIndex)
    #
    def _updateItemPressByVisiblePress(self):
        visibleIndex = self._pressVisibleIndex
        #
        if self._expandFlag is True:
            pass
        elif self._checkFlag is True:
            self.setItemCheckVisibleAt(visibleIndex)
        elif self._expandFlag is False and self._checkFlag is False:
            # Update Change Flag
            self._updateItemPressChangeFlagVisibleAt(visibleIndex)
            #
            self.setItemPressVisibleAt(visibleIndex)
    #
    def _updateItemDragPressByVisiblePress(self):
        pass
    #
    def _updateItemExpandByVisiblePress(self):
        self.setItemExpandVisibleAt(self._pressVisibleIndex)
    #
    def _updateItemCheckByVisiblePress(self):
        self.setItemCheckVisibleAt(self._pressVisibleIndex)
    #
    def _updateVisibleCurIndexByPress(self):
        column, row = self._pressVisibleColumn, self._pressVisibleRow
        self._curVisibleColumn, self._curVisibleRow = self._getClampVisibleColumn(column), self._getClampVisibleRow(row)
        self._updateCurVisibleIndex()
    #
    def _clearHover(self):
        if self._hoverItemModel is not None:
            self._hoverItemModel.setPressHovered(False)
            self._hoverItemModel.setExtendPressHovered(False)
            #
            self._hoverItemModel.setExpandHovered(False)
            self._hoverItemModel.setCheckHovered(False)
        #
        self._hoverItemModel = None
    # Hover
    def _updateHoverChangeFlagVisibleAt(self, visibleIndex):
        # noinspection PyUnusedLocal
        itemIndex = self.itemIndexVisibleAt(visibleIndex)
    #
    def _updateItemHoverVisibleAt(self, visibleIndex):
        def pressHovered(itemModel):
            preHoverItemModel = self._hoverItemModel
            if not itemModel == preHoverItemModel:
                isChanged = True
            else:
                isChanged = False
            #
            if isChanged is True:
                if itemModel.isPressable():
                    itemModel.setPressHovered(True)
                #
                if preHoverItemModel is not None:
                    preHoverItemModel.setPressHovered(False)
                    #
                    preHoverItemModel.setExtendPressHovered(False)
                    preHoverItemModel.setExpandHovered(False)
                    preHoverItemModel.setCheckHovered(False)
                #
                self._hoverItemModel = itemModel
            #
            self._curHoverChangeFlag = isChanged
        #
        def extendPressHovered(itemModel):
            if itemModel.extendIcon() is not None:
                isExtendPressHovered = itemModel.isExtendIconRectContain(self._itemHoverPos)
                #
                itemModel.setExtendPressHovered(isExtendPressHovered)
                #
                self._extendPressFlag = isExtendPressHovered
        #
        def expandHovered(itemModel):
            if itemModel.isExpandable():
                isExpandHovered = itemModel.isExpandPressRectContain(self._itemHoverPos)
            else:
                isExpandHovered = False
            #
            if self._dragFlag is False:
                itemModel.setExpandHovered(isExpandHovered)
            #
            self._expandFlag = isExpandHovered
        #
        def checkHovered(itemModel):
            if itemModel.isCheckable():
                isCheckHovered = itemModel.isCheckRectContain(self._itemHoverPos)
            else:
                isCheckHovered = False
            #
            itemModel.setCheckHovered(isCheckHovered)
            #
            self._checkFlag = isCheckHovered
        #
        curItemModel = self.itemModelVisibleAt(visibleIndex)
        #
        pressHovered(curItemModel)
        extendPressHovered(curItemModel)
        #
        expandHovered(curItemModel)
        checkHovered(curItemModel)
    # Press
    def _updateItemPressChangeFlagVisibleAt(self, visibleIndex):
        itemModel = self.itemModelVisibleAt(visibleIndex)
        isChanged = False
        if itemModel.isPressable():
            if not itemModel == self._curPressItemModel:
                isChanged = True
        #
        self._curPressChangeFlag = isChanged
    #
    def _updateItemPressVisibleAt(self, visibleIndex):
        def _pressCurrentBranch(itemModel):
            isChanged = False
            preItemModel = self._curPressItemModel
            #
            if itemModel.isPressable():
                if not itemModel == preItemModel:
                    isChanged = True
            #
            if isChanged is True:
                # Clear First
                if preItemModel is not None:
                    preItemModel.setPressCurrent(False)
                #
                itemModel.setPressCurrent(True)
                #
                self._curPressItemModel = itemModel
                self._curPressItemIndex = self.itemModelIndex(itemModel)
                self._curPressVisibleIndex = visibleIndex
            #
            if self._dragStartVisibleIndex != self._curPressVisibleIndex:
                isChanged = True
            #
            self._curPressChangeFlag = isChanged
        #
        def _pressCommandBranch(itemModel):
            if self._expandFlag is True:
                pass
            elif self._checkFlag is True:
                pass
            else:
                if self._pressFlag is True:
                    if self._extendPressFlag is True:
                        itemModel.acceptExtendPressCommand()
                    else:
                        itemModel.acceptPressCommand()
        #
        curItemModel = self.itemModelVisibleAt(visibleIndex)
        #
        _pressCurrentBranch(curItemModel)
        _pressCommandBranch(curItemModel)
    # Range Press
    def _updateItemRangePressStartVisibleAt(self, visibleIndex):
        itemModel = self.itemModelVisibleAt(visibleIndex)
        #
        isChanged = False
        startItemModel = self._rangePressStartItemModel
        #
        if itemModel.isPressable():
            if not itemModel == startItemModel:
                isChanged = True
        #
        if isChanged is True:
            itemModel.setPressStarted(True)
            if startItemModel is not None:
                startItemModel.setPressStarted(False)
            #
            self._updateSelPressStartVisibleIndex(visibleIndex)
            self._rangePressStartItemModel = itemModel
    #
    def _updateItemRangePressStopVisibleAt(self, visibleIndex):
        if self._expandFlag is False and self._checkFlag is False:
            self.setItemSelectVisibleRange(self._selRangePressStartVisibleIndex, visibleIndex)
    #
    def _updatePressItemDragStartVisibleAt(self, visibleIndex):
        itemModel = self.itemModelVisibleAt(visibleIndex)
        #
        isChanged = False
        startItemModel = self._dragStartItemModel
        #
        if itemModel.isPressable():
            if not itemModel == startItemModel:
                isChanged = True
        #
        if isChanged is True:
            itemModel.setDragStarted(True)
            if startItemModel is not None:
                startItemModel.setDragStarted(False)
            #
            self._dragStartItemModel = itemModel
            self._dragStartVisibleIndex = visibleIndex
    # Expand
    def _updateItemExpandVisibleAt(self, visibleIndex):
        itemModel = self.itemModelVisibleAt(visibleIndex)
        #
        if itemModel.isExpandable():
            if self._pressFlag is True and self._expandFlag is True:
                itemModel._expandClickSwitchAction(isExtend=self._shiftFlag)
                #
                self._acceptItemExpandedEmit()
    #
    def _updateItemCheckChangeFlagVisibleAt(self, visibleIndex):
        pass
    # Range Check
    def _updateItemRangeCheckStartVisibleAt(self, visibleIndex):
        itemModel = self.itemModelVisibleAt(visibleIndex)
        #
        isChanged = False
        startItemModel = self._rangeCheckStartItemModel
        #
        if itemModel.isPressable():
            if not itemModel == startItemModel:
                isChanged = True
        #
        if isChanged is True:
            itemModel.setCheckStarted(True)
            if startItemModel is not None:
                startItemModel.setCheckStarted(False)
            #
            self._rangeCheckStartVisibleIndex = visibleIndex
            self._rangeCheckStartItemModel = itemModel
    #
    def _updateItemRangeCheckStopVisibleAt(self, visibleIndex):
        if self._checkFlag is True:
            self.setItemCheckVisibleRange(self._rangeCheckStartVisibleIndex, visibleIndex)
    #
    def _updateHoverLoc(self, x, y):
        enable = False
        #
        self._pressHoverPos = x, y
        #
        w, h = self._gridSize()
        xValue, yValue = self.value()
        #
        if self.isContainPos(x, y):
            column, row = self.visibleColumnLoc(x + xValue), self.visibleRowLoc(y + yValue)
            if self.isContainVisibleColumn(column) and self.isContainVisibleRow(row):
                self._hoveredVisibleColumn, self._hoveredVisibleRow = column, row
                visibleIndex = self.indexVisibleAt(column, row)
                if self.isContainVisibleIndex(visibleIndex):
                    self._curHoverVisibleIndex = visibleIndex
                    self._itemHoverPos = self._mapToItemPos(x, y, w, h, xValue, yValue, column, row)
                    #
                    enable = True
        #
        if enable is True:
            self._updateItemHoverByVisibleHover()
        else:
            self._hoveredVisibleColumn, self._hoveredVisibleRow = -1, -1
            self._curHoverVisibleIndex = -1
            #
            self._clearHover()
    #
    def _updatePressLoc(self, x, y, force=False):
        enable = False
        #
        self._pressClickPos = x, y
        #
        w, h = self._gridSize()
        xValue, yValue = self.value()
        #
        if self.isContainPos(x, y) or force is True:
            column, row = self.visibleColumnLoc(x + xValue), self.visibleRowLoc(y + yValue)
            if self.isContainVisibleColumn(column) and self.isContainVisibleRow(row) or force is True:
                self._pressVisibleColumn, self._pressVisibleRow = column, row
                visibleIndex = self.indexVisibleAt(column, row)
                if self.isContainVisibleIndex(visibleIndex) or force is True:
                    self._pressVisibleIndex = visibleIndex
                    self._itemPressPos = self._mapToItemPos(x, y, w, h, xValue, yValue, column, row)
                    #
                    enable = True
        #
        if enable is True:
            self._updateVisibleCurIndexByPress()
        else:
            self._pressVisibleColumn, self._pressVisibleRow = -1, -1
            self._pressVisibleIndex = -1
    #
    def _updateDragPressLoc(self, x, y):
        width, height = self.width(), self.height()
        #
        x += self._uiMargins[0]
        if self.isHScrollable():
            # Scroll
            if x < 0:
                if self.isHScrollable() is True and not self.isHMinimum():
                    self._hAutoScrollFlag = True
                    self._hAutoScrollRegion = 0
                    #
                    self.hScrollBar().viewModel().setTimerInterval(max(5, 500/(abs(y) + 1)))
                    self.hScrollBar().viewModel()._startAutoSubAction()
                else:
                    self._clearHover()
                    self._updateItemPressByVisiblePress()
            elif width < x:
                if self.isHScrollable() is True and not self.isHMaximum():
                    self._hAutoScrollFlag = True
                    self._hAutoScrollRegion = 1
                    #
                    self.hScrollBar().viewModel().setTimerInterval(max(5, 500/(abs(y - height) + 1)))
                    self.hScrollBar().viewModel()._startAutoAddAction()
                else:
                    self._clearHover()
                    self._updateItemPressByVisiblePress()
            else:
                self.hScrollBar().viewModel()._autoScrollStopAction()
                self.hScrollBar().viewModel().setTimerInterval(50)
                #
                self._hAutoScrollFlag = False
        #
        y += self._uiMargins[1]
        if self.isVScrollable():
            # Scroll
            if y <= 0:
                if self.isVScrollable() is True and not self.isVMinimum():
                    self._vAutoScrollFlag = True
                    self._vAutoScrollRegion = 0
                    #
                    self.vScrollBar().viewModel().setTimerInterval(max(5, 500/(abs(y) + 1)))
                    self.vScrollBar().viewModel()._startAutoSubAction()
                else:
                    self._clearHover()
                    self._updateItemPressByVisiblePress()
            elif height <= y:
                if self.isVScrollable() is True and not self.isVMaximum():
                    self._vAutoScrollFlag = True
                    self._vAutoScrollRegion = 1
                    #
                    self.vScrollBar().viewModel().setTimerInterval(max(5, 500/(abs(y - height) + 1)))
                    self.vScrollBar().viewModel()._startAutoAddAction()
                else:
                    self._clearHover()
                    self._updateItemPressByVisiblePress()
            else:
                self.vScrollBar().viewModel()._autoScrollStopAction()
                self.vScrollBar().viewModel().setTimerInterval(50)
                #
                self._vAutoScrollFlag = False
        else:
            if y < 0:
                if self.visibleIndexes():
                    visibleIndex = self.visibleIndexes()[0]
                    self.setItemHoveredVisibleAt(visibleIndex)
                    self.setItemPressVisibleAt(visibleIndex)
            elif self._absHeight < y:
                if self.visibleIndexes():
                    visibleIndex = self.visibleIndexes()[-1]
                    self.setItemHoveredVisibleAt(visibleIndex)
                    self.setItemPressVisibleAt(visibleIndex)
    # noinspection PyMethodMayBeStatic
    def _hoverStartAction(self, event):
        event.ignore()
    #
    def _hoverExecuteAction(self, event):
        x, y = self._getEventPos(event)
        #
        self._updateHoverLoc(x, y)
        # Tree Connection
        if self._itemMode is qtCore.TreeMode:
            if self._shiftFlag is True:
                self.widget().update()
        #
        event.ignore()
    #
    def _hoverStopAction(self, event):
        self._clearHover()
        #
        event.ignore()
    #
    def _hoverScrollAction(self):
        self._updateHoverLoc(*self._pressHoverPos)
    #
    def _pressStartAction(self, event):
        x, y = self._getEventPos(event)
        # Flag
        self._pressFlag, self._dragFlag, self._trackFlag = True, False, False
        self._curPressChangeFlag = False
        #
        self._updatePressLoc(x, y)
        # Action
        if self.isValidPress():
            self._updateSelPressStartVisibleIndex(self._pressVisibleIndex)
            #
            self._updateItemHoveredByVisiblePress()
            #
            self._updateItemPressByVisiblePress()
        else:
            if self.isSelectEnable():
                if self._shiftFlag is False and self._ctrlFlag is False:
                    self._restDragSelect()
                    #
                    self._clearSelect()
        #
        if self._selectChangeFlag is True:
            self.widget().selectedChanged.emit()
        #
        if self.isEventOverrideEnable():
            event.ignore()
        else:
            event.accept()
    #
    def _pressExecuteAction(self, event):
        x, y = self._getEventPos(event)
        #
        # Flag
        self._pressFlag, self._dragFlag, self._trackFlag = False, True, False
        #
        self._updateDragPressLoc(x, y)
        #
        if self._hAutoScrollFlag is False and self._vAutoScrollFlag is False:
            # Action
            self._updatePressLoc(x, y, force=True)
            #
            if self.isValidPress():
                # Hover
                self._updateItemHoveredByVisiblePress()
                # Press
                self._updateItemPressByVisiblePress()
        #
        if self._selectChangeFlag is True:
            self.widget().selectedChanged.emit()
        # Tree Connection
        if self._itemMode is qtCore.TreeMode:
            if self._shiftFlag is True:
                self._updateWidget()
        #
        if self.isEventOverrideEnable():
            event.ignore()
        else:
            event.accept()
    #
    def _pressStopAction(self, event):
        x, y = self._getEventPos(event)
        # Expand
        self._updateItemExpandByVisiblePress()
        # Stop Auto Scroll
        self._autoScrollStopAction()
        # Emit
        if self.isValidPress():
            if self._pressFlag is True and self._expandFlag is False and self._checkFlag is False:
                self.widget().currentChanged.emit()
        else:
            if self._curPressChangeFlag is True or self._itemIndexCount == 1:
                self.widget().currentChanged.emit()
        #
        self.widget().itemClicked.emit()
        # Flag
        self._pressFlag, self._dragFlag, self._trackFlag = False, False, False
        self._expandFlag, self._checkFlag = False, False
        #
        self._updateHoverLoc(x, y)
        #
        if self.isEventOverrideEnable():
            event.ignore()
        else:
            event.accept()
    #
    def _autoScrollExecuteAction(self):
        if self._vAutoScrollFlag is True:
            if self._vAutoScrollRegion == 0:
                row = self.minViewVisibleRow()
            else:
                row = self.maxViewVisibleRow()
            #
            self.setPressVisibleRow(row)
            #
            if self.isValidPress():
                self._updateItemHoveredByVisiblePress()
                #
                self._updateItemPressByVisiblePress()
    #
    def _autoScrollStopAction(self):
        if self.isHScrollable():
            self.hScrollBar().viewModel()._autoScrollStopAction()
            self.hScrollBar().viewModel().setTimerInterval(50)
        if self.isVScrollable():
            self.vScrollBar().viewModel()._autoScrollStopAction()
            self.vScrollBar().viewModel().setTimerInterval(50)
        #
        self._hAutoScrollFlag, self._vAutoScrollFlag = False, False
    #
    def _wheelAction(self, event):
        delta = event.angleDelta().y()
        if self.isVScrollable():
            self._vScrollBar.viewModel()._setShiftFlag(self._shiftFlag)
            self._vScrollBar.viewModel()._wheelAction(delta)
        #
        self._hoverScrollAction()
        #
        if self.isEventOverrideEnable():
            event.ignore()
        else:
            if self.isVScrollable():
                event.accept()
            else:
                event.ignore()
    #
    def _updateFlag(self):
        pass
    # Action
    def _columnTraceAction(self, delta):
        visibleIndex = self._curPressVisibleIndex
        #
        visibleIndex += delta
        visibleIndex = self._getClampVisibleIndex(visibleIndex)
        self.setCurrentVisibleIndex(visibleIndex)
        #
        self._updateByTraceAction()
    #
    def _rowTraceAction(self, delta):
        curVisibleRow = self._curVisibleRow
        #
        curVisibleRow += delta
        curVisibleRow = self._getClampVisibleRow(curVisibleRow)
        #
        visibleIndex = self.indexVisibleAt(self._curVisibleColumn, curVisibleRow)
        visibleIndex = self._getClampVisibleIndex(visibleIndex)
        self.setCurrentVisibleIndex(visibleIndex)
        #
        self._updateByTraceAction()
    # Action
    def _updateByTraceAction(self):
        self.setVisibleCurrent()
        #
        self.setCurrentVisibleCeiling()
    #
    def _updateByFilterAction(self):
        self._updateItemModelsExtendFilterVisible()
        self._updateSubVisibleItemModelIndexDicByFilter()
        #
        if self.isVisible():
            self._updateVisibleItemModelIndexLisByVisible_()
        else:
            self._updateVisibleItemModelIndexLisByFilter()
        #
        self.update()
        #
        self.vScrollBar().viewModel().scrollToMinimum()
        #
        self._updateCurVisibleIndexByCurItemModel()
    #
    def _expandClickAction(self):
        pass
    #
    def _setCtrlFlag(self, boolean):
        self._ctrlFlag = boolean
        #
        self.widget().update()
    #
    def _setShiftFlag(self, boolean):
        self._shiftFlag = boolean
        #
        self.widget().update()
    #
    def _setAltFlag(self, boolean):
        self._altFlag = boolean
        #
        self.widget().update()
    #
    def _clearPressed(self):
        if self._curPressItemModel is not None:
            self._curPressItemModel.setPressCurrent(False)
        #
        self._curPressItemModel = None
        #
        self._pressClickPos = 0, 0
        #
        self.widget().update()
    #
    def _clearSelected(self):
        pass
    #
    def _updateGeometry(self):
        self._updateWidgetGeometry()
        self._updateViewportGeometry()
        #
        self._updateRectGeometry()
        #
        self._updateVisibleItemsGeometry()
    #
    def _updateWidget(self):
        self.widget().update()
    #
    def _acceptItemExpandedEmit(self):
        self.widget().itemExpanded.emit()
    #
    def _updateAction(self):
        self._trackActionModel._updateTrackable(self.isHScrollable(), self.isVScrollable())
        #
        self._trackActionModel.setMaximumPos(self._trackWidth, self._trackHeight)
        self._trackActionModel.setPos(*self.value())
    #
    def _scrollValueChangeAction(self):
        self._updateVisibleItemsPos()
        self._updateVisibleItemsGeometry()
        #
        self._autoScrollExecuteAction()
    #
    def update(self, force=False):
        self._initTopItemModelSortKeyLis()
        #
        self._updateVisibleColumnCount()
        self._updateVisibleRowCount()
        #
        self._updateViewportSize()
        self._updateAbsSize()
        self._updateScrollSize()
        #
        self._updateViewSize()
        self._updateTrackSize()
        #
        self._updateScrollBarGeometry()
        #
        self._updateVisibleItemsPos()
        #
        self._updateGeometry()
        #
        self._updateAction()
        #
        self._updateWidget()
    #
    def setItemMode(self, mode):
        self._itemMode = mode
    #
    def setItemSize(self, w, h):
        self._uiItemWidth, self._uiItemHeight = max(int(w), 1), max(int(h), 1)
        #
        w, h = self._gridSize()
        if self.isHScrollEnable():
            self.hScrollBar().setBasicScrollValue(w)
            self.hScrollBar().setRowScrollValue(w)
        if self.isVScrollEnable():
            self.vScrollBar().setBasicScrollValue(h)
            self.vScrollBar().setRowScrollValue(h)
    #
    def value(self):
        return self.hValue(), self.vValue()
    #
    def isValidPress(self):
        return (
            self.isContainVisibleIndex(self._pressVisibleIndex) and
            self.isContainVisibleColumn(self._pressVisibleColumn) and
            self.isContainVisibleRow(self._pressVisibleRow)
        )
    # Hover
    def setItemHoveredVisibleAt(self, visibleIndex):
        if self.isContainVisibleIndex(visibleIndex):
            # Change Flag
            self._updateHoverChangeFlagVisibleAt(visibleIndex)
            #
            self._updateItemHoverVisibleAt(visibleIndex)
    # Press
    def setItemPressVisibleAt(self, visibleIndex):
        if self.isPressEnable():
            if self.isContainVisibleIndex(visibleIndex):
                if self.isSelectEnable():
                    itemIndex = self.itemIndexVisibleAt(visibleIndex)
                    # Press
                    if self._pressFlag is True:
                        # Separate
                        if self._shiftFlag is False and self._ctrlFlag is False:
                            self._sepSelectItemAt(itemIndex)
                            # Range Press Start
                            self._updateItemRangePressStartVisibleAt(visibleIndex)
                            # Drag Press Start
                            self._updatePressItemDragStartVisibleAt(visibleIndex)
                        # Addition
                        elif self._shiftFlag is True and self._ctrlFlag is False:
                            # Range Press Stop
                            self._updateItemRangePressStopVisibleAt(visibleIndex)
                        # Reverse
                        elif self._shiftFlag is False and self._ctrlFlag is True:
                            self._revSelectItemAt(itemIndex)
                        # Add
                        elif self._shiftFlag is True and self._ctrlFlag is True:
                            self._addSelectItemAt(itemIndex)
                    # Drag
                    elif self._dragFlag is True:
                        if self._shiftFlag is False and self._ctrlFlag is False:
                            self._addSelectItemRange(self._selRangePressStartVisibleIndex, visibleIndex)
                        # Addition
                        elif self._shiftFlag is True and self._ctrlFlag is False:
                            self._addSelectItemAt(itemIndex)
                        # Reverse
                        elif self._shiftFlag is False and self._ctrlFlag is True:
                            if self._curPressChangeFlag is True:
                                self._revSelectItemAt(itemIndex)
                        # Add
                        elif self._shiftFlag is True and self._ctrlFlag is True:
                            self._addSelectItemAt(itemIndex)
                else:
                    if self._pressFlag is True:
                        self._updatePressItemDragStartVisibleAt(visibleIndex)
                    #
                    self._updateItemPressVisibleAt(visibleIndex)
    # Range Press
    def setItemSelectVisibleRange(self, *visibleIndexRange):
        def setBranch(visibleIndex):
            if self.isContainVisibleIndex(visibleIndex):
                itemModel = self.itemModelVisibleAt(visibleIndex)
                itemIndex = self.itemModelIndex(itemModel)
                if itemModel.isSelectable():
                    if self._shiftFlag is True and self._checkFlag is False:
                        self._addSelectItemAt(itemIndex)
        #
        startIndex, stopIndex = min(visibleIndexRange), max(visibleIndexRange) + 1
        visibleIndexes = range(startIndex, stopIndex)
        if visibleIndexes:
            if self._pressFlag is True:
                if visibleIndexes:
                    [setBranch(i) for i in visibleIndexes]
    # Expand
    def setItemExpandVisibleAt(self, visibleIndex):
        if self.isContainVisibleIndex(visibleIndex):
            self._updateItemExpandVisibleAt(visibleIndex)
    # Check
    def setItemCheckVisibleAt(self, visibleIndex):
        if self.isContainVisibleIndex(visibleIndex):
            if self.isCheckEnable():
                itemIndex = self.itemIndexVisibleAt(visibleIndex)
                itemModel = self.itemModelVisibleAt(visibleIndex)
                # Press
                if self._pressFlag is True:
                    if self._altFlag is True:
                        self._sepCheckItemAt(itemIndex)
                    else:
                        if self._shiftFlag is False and self._ctrlFlag is False:
                            self._revCheckItemAt(itemIndex)
                            #
                            self._updateItemRangeCheckStartVisibleAt(visibleIndex)
                            #
                            self._dragStartChecked = itemModel.isChecked()
                        if self._shiftFlag is True and self._ctrlFlag is False:
                            self._updateItemRangeCheckStopVisibleAt(visibleIndex)
                            #
                            self._dragStartChecked = True
                        elif self._shiftFlag is False and self._ctrlFlag is True:
                            self._updateItemRangeCheckStopVisibleAt(visibleIndex)
                            #
                            self._dragStartChecked = False
                        elif self._shiftFlag is True and self._ctrlFlag is True:
                            self._updateItemRangeCheckStopVisibleAt(visibleIndex)
                # Drag
                elif self._dragFlag is True:
                    if self._altFlag is True:
                        self._sepCheckItemAt(itemIndex)
                    else:
                        if self._shiftFlag is False and self._ctrlFlag is False:
                            if self._dragStartChecked is True:
                                self._addCheckItemAt(itemIndex)
                            else:
                                self._subCheckItemAt(itemIndex)
                        elif self._shiftFlag is True and self._ctrlFlag is False:
                            self._addCheckItemAt(itemIndex)
                        elif self._shiftFlag is False and self._ctrlFlag is True:
                            self._subCheckItemAt(itemIndex)
                        elif self._shiftFlag is True and self._ctrlFlag is True:
                            pass
    # Range Check
    def setItemCheckVisibleRange(self, *visibleIndexRange):
        def setBranch(visibleIndex):
            if self.isContainVisibleIndex(visibleIndex):
                itemModel = self.itemModelVisibleAt(visibleIndex)
                itemIndex = self.itemModelIndex(itemModel)
                if itemModel.isCheckable():
                    if self._shiftFlag is True and self._ctrlFlag is True:
                        self._revCheckItemAt(itemIndex)
                    elif self._shiftFlag is True and self._ctrlFlag is False:
                        self._addCheckItemAt(itemIndex)
                    elif self._shiftFlag is False and self._ctrlFlag is True:
                        self._subCheckItemAt(itemIndex)
        #
        startIndex, stopIndex = min(visibleIndexRange), max(visibleIndexRange) + 1
        visibleIndexes = range(startIndex, stopIndex)
        # Press
        if self._checkFlag is True:
            if visibleIndexes:
                [setBranch(i) for i in visibleIndexes]
    #
    def setItemMultiFilterIn(self, itemIndexes, itemFilterColumn, itemFilterRow, boolean):
        if itemIndexes:
            for itemIndex in itemIndexes:
                itemModel = self.itemModelAt(itemIndex)
                if itemModel is not None:
                    itemModel.setMultiFilterDic(itemFilterColumn, itemFilterRow, boolean)
            #
            self._updateByFilterAction()
    #
    def setVisibleCurrent(self):
        self.setItemPressVisibleAt(self._curPressVisibleIndex)
    #
    def setCurrentVisibleCeiling(self):
        w, h = self._gridSize()
        value = self._curVisibleRow*h
        self.vScrollBar().viewModel().setValue(value)
        #
        self.vScrollBar().viewModel()._updateTempValue()
    #
    def cleanItems(self):
        if self._itemModelLis:
            [i.widget().deleteLater() for i in self._itemModelLis]
            #
            self._clearHover()
            self._clearPressed()
            self._clearSelected()
            #
            self._initViewModelAbsVar()
            #
            self.update()
    #
    def setFilterExplainRefresh(self):
        if self._filterEntryWidget is not None:
            self._filterEntryWidget.setNameText(str(len(self._itemModelLis)).zfill(4))
    #
    def setCheckAll(self):
        [i.setChecked(True) for i in self._itemModelLis if i.isFilterVisible() and i.isCheckable()]
    #
    def setUncheckAll(self):
        [i.setChecked(False) for i in self._itemModelLis if i.isFilterVisible() and i.isCheckable()]
    #
    def setExpandAll(self):
        self.setExtendExpanded(True)
    #
    def setUnexpandAll(self):
        self.setExtendExpanded(False)


#
class Abc_QtScrollAreaModel(qtAbstract.QtScrollAreaModelAbs):
    def _initScrollAreaBasic(self, widget):
        self._initScrollViewModelAbs()
        #
        self._initScrollAreaBasicAttr()
        self._initScrollAreaBasicAction()
        self._initScrollAreaBasicVar()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setScrollBar(widget)
    #
    def _initScrollAreaBasicVar(self):
        self._pressFlag, self._dragFlag, self._trackFlag = False, False, False
        #
        self._miniWidth, self._miniHeight = 60, 60
    #
    def _initScrollAreaBasicAttr(self):
        pass
    #
    def _initScrollAreaBasicAction(self):
        pass
    #
    def _updateViewportGeometry(self):
        hValue, vValue = self.value()
        #
        xPos, yPos = self._uiMargins[0] - hValue, self._uiMargins[1] - vValue
        #
        width = [self.viewportWidth(), self._absWidth][self.isHScrollable()] - [0, self._uiVScrollWidth][self.isHScrollable() is False and self._isVScrollable is True]
        height = [self.viewportHeight(), self._absHeight][self._isVScrollable] - [0, self._uiVScrollWidth][self.isHScrollable() is True and self._isVScrollable is False]
        # Viewport
        self._viewport.setGeometry(
            xPos, yPos,
            width, height
        )
    #
    def _updateScrollBarGeometry(self):
        xPos, yPos = self._uiMargins[0], self._uiMargins[1]
        #
        width, height = self.viewportWidth(), self.viewportHeight()
        #
        if self.isHScrollable():
            self._hScrollBar.show()
            self._hScrollBar.setGeometry(
                xPos, yPos + height - self._uiHScrollWidth,
                width, self._uiHScrollWidth
            )
        else:
            self._hScrollBar.hide()
        #
        if self._isVScrollable:
            self._vScrollBar.show()
            self._vScrollBar.setGeometry(
                xPos + width - self._uiVScrollWidth, yPos,
                self._uiVScrollWidth, height
            )
        else:
            self._vScrollBar.hide()
    #
    def _updateGeometry(self):
        self._updateViewportGeometry()
        self._updateScrollBarGeometry()
    #
    def update(self, force=False):
        height = self.viewportHeight()
        width = self.viewportWidth()
        #
        size = self._layout.minimumSize()
        #
        self._absWidth, self._absHeight = size.width(), size.height()
        self._isHScrollable, self._isVScrollable = width < self._absWidth, height < self._absHeight
        #
        self._hScrollBar._viewModel._updateUnion(self._isVScrollable)
        self._vScrollBar._viewModel._updateUnion(self._isHScrollable)
        #
        self._hScrollBar._viewModel.setAbsHeight(self._absWidth)
        self._vScrollBar._viewModel.setAbsHeight(self._absHeight)
        #
        self._trackWidth = self._absWidth - width + [0, self._uiVScrollWidth][self._isVScrollable]
        self._trackHeight = self._absHeight - height + [0, self._uiVScrollWidth][self._isVScrollable]
        #
        self._updateGeometry()
        #
        self._updateAction()
    #
    def isMaximum(self):
        return self._vScrollBar._viewModel.isMaximum()
    #
    def isMinimum(self):
        return self._vScrollBar._viewModel.isMinimum()


#
class _QtItemModel(Abc_QtItemModel):
    def __init__(self, widget):
        self._initItemModelBasic(widget)


#
class _QtViewModel(Abc_QtViewModel):
    def __init__(self, widget):
        self._initViewModelBasic(widget)


#
class QtTreeviewItemModel(Abc_QtItemModel):
    def __init__(self, widget):
        self._initItemModelBasic(widget)


#
class QtValueEnterItemModel(qtAbstract.QtValueEnterItemModelAbs):
    def __init__(self, widget):
        self._initValueEnterItemModelAbs()
        self.setWidget(widget)
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.size()
        #
        side, spacing = self._uiSide, self._uiSpacing
        frameWidth, frameHeight = self.frameSize()
        #
        xPos += side
        #
        explainWidth = self._uiNameTextWidth
        if self.nameText() is not None:
            self.nameTextRect().setRect(
                xPos, yPos,
                explainWidth, frameHeight
            )
            xPos += explainWidth
        #
        rectCount = self.valueCount()
        w, h = (width - xPos - side - spacing*(rectCount - 1)) / rectCount, height
        #
        for rect in self.enterRects():
            rect.setRect(
                xPos, yPos,
                w, h
            )
            #
            xPos += w + spacing
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        width -= 1
        height -= 1
        #
        side, spacing = self._uiSide, self._uiSpacing
        frameWidth, frameHeight = self._uiFrameWidth, self._uiFrameHeight
        #
        xPos += side
        #
        if self.nameText() is not None:
            xPos += self._uiNameTextWidth
        #
        rectCount = self.valueCount()
        w, h = (width - xPos - side - spacing * (rectCount - 1)) / rectCount, height
        #
        for widget in self.enterWidgets():
            widget.setGeometry(
                xPos + side, yPos,
                w - side*2, h
            )
            #
            xPos += w + spacing + side
    #
    def update(self):
        self._updateRectGeometry()
        self._updateChildrenGeometry()


# Filter Item
class QtFilterEnterItemModel(qtAbstract.QtEnterItemModelAbs):
    def __init__(self, widget):
        self._initDatumEnterItemModelAbs()
        #
        self.__overrideAttr()
        #
        self.setWidget(widget)
    #
    def __overrideAttr(self):
        self._filterWidth = 200
        self._isEnterEnable = True
        self._isEnterable = True
        #
        self._xLeftPos = 0
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side = 2
        frameWidth, frameHeight = self.frameSize()
        #
        xPos = max(0, width - self._filterWidth)
        #
        xPos += side
        #
        self._xLeftPos = xPos
        self._uiBasicRect.setRect(
            xPos, yPos,
            width - xPos, frameHeight
        )
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        width -= 1
        height -= 1
        #
        side = 2
        #
        frameWidth, frameHeight = 20, 20
        #
        xPos = max(0, width - self._filterWidth)
        #
        xPos += side*2
        #
        self._historyButton.setGeometry(
            xPos, yPos,
            frameWidth, frameHeight
        )
        #
        self._enterWidget.setGeometry(
            xPos + frameWidth, yPos,
            width - xPos - side, frameHeight
        )
        #
        self._copyButton.setGeometry(
            width - frameWidth*2 - side, yPos,
            frameWidth, frameHeight
        )
        self._clearButton.setGeometry(
            width - frameWidth - side, yPos,
            frameWidth, frameHeight
        )
    #
    def _updateButtonVisible(self):
        boolean = [False, True][len(self._enterWidget.text()) > 0]
        #
        self._clearButton.setVisible(boolean)
        self._copyButton.setVisible(boolean)
    #
    def update(self):
        self._updateRectGeometry()
        #
        self._updateChildrenGeometry()
        self._updateButtonVisible()
        #
        self._updateWidgetState()
    #
    def setDatum(self, data):
        self._enterWidget.setText(self._uiDatumText)
        #
        self._updateButtonVisible()
    #
    def datum(self):
        return unicode(self._enterWidget.text())
    #
    def setEnterClear(self):
        self._enterWidget.clear()
        self._updateButtonVisible()
        #
        self._updateWidgetState()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._historyButton = self._widget._historyButton
        #
        self._copyButton = self._widget._copyButton
        self._clearButton = self._widget._clearButton
        #
        self._enterWidget = self._widget._enterWidget


#
class QtEnterItemModel(Abc_QtItemModel):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideAttr()
        self.__overrideUi()
    #
    def __overrideAttr(self):
        self._isCheckEnable = False
        #
        self._xLeftPos = 0
    #
    def __overrideUi(self):
        self._uiCheckIconKeyword = 'svg_basic@svg#boxUnchecked'
        self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.size()
        #
        side = self._uiSide
        frameWidth, frameHeight = self.frameSize()
        #
        xOffset, yOffset = 0, 0
        #
        xPos += side
        #
        explainWidth = self._uiNameTextWidth
        if self.nameText() is not None:
            self._uiNameTextRect.setRect(
                xPos, yPos,
                explainWidth, frameHeight
            )
            xPos += explainWidth
        #
        self._xLeftPos = xPos
        self._uiBasicRect.setRect(
            xPos, yPos,
            width - xPos, frameHeight
        )
        #
        if self.isEnterEnable():
            xPos += frameWidth
        #
        if self.isChooseEnable():
            xPos += frameWidth
            self.indexTextRect().setRect(
                side, yPos,
                explainWidth, frameHeight
            )
        #
        if self.isCheckEnable():
            self._uiCheckRect.setRect(
                xPos + (self._uiFrameWidth - self._uiIconWidth) / 2 + xOffset, yPos + (self._uiFrameHeight - self._uiIconHeight) / 2 + yOffset,
                self._uiIconWidth - xOffset, self._uiIconHeight - yOffset
            )
            xPos += frameWidth
        #
        textHeight = self._textHeight()
        #
        self._uiDatumRect.setRect(
            xPos + 2, yPos + (frameHeight - textHeight)/2,
            width - xPos - side, height
        )
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        width -= 1
        height -= 1
        #
        side = self._uiSide
        #
        frameWidth, frameHeight = self._uiFrameWidth, self._uiFrameHeight
        #
        xPos += side
        #
        if self.nameText() is not None:
            xPos += self._uiNameTextWidth
        #
        if self.isChooseEnable():
            self._chooseButton.setGeometry(
                xPos, yPos,
                frameWidth, frameHeight
            )
            self._chooseButton.show()
            xPos += frameWidth
        else:
            self._chooseButton.hide()
        #
        if self.isEnterEnable():
            self._entryButton.setGeometry(
                xPos, yPos,
                frameWidth, frameHeight
            )
            #
            self._entryButton.show()
            #
            if self.isEnterable():
                self._enterWidget.setGeometry(
                    xPos + frameWidth, yPos,
                    width - xPos - side, frameHeight
                )
                #
                self._enterWidget.show()
            else:
                self._enterWidget.hide()
            #
            xPos += frameWidth
        else:
            self._entryButton.hide()
            self._enterWidget.hide()
        #
        if self.isCheckEnable():
            xPos += frameWidth
        #
        self._copyButton.setGeometry(
            width - frameWidth*2, yPos,
            frameWidth, frameHeight
        )
        self._clearButton.setGeometry(
            width - frameWidth, yPos,
            frameWidth, frameHeight
        )
    #
    def _updateButtonVisible(self):
        if self.isEnterable():
            boolean = [False, True][len(self._enterWidget.text()) > 0]
        else:
            boolean = False
        #
        self._clearButton.setVisible(boolean)
        self._copyButton.setVisible(boolean)
    #
    def _entryableSwitchAction(self):
        self._isEnterable = not self._isEnterable
        #
        self._enterWidget.setEnterable(self._isEnterable)
        self._updateEnterWidget()
        #
        self._updateChildrenGeometry()
        self._updateButtonVisible()
        #
        self._updateWidgetState()
    #
    def _updateEnterWidget(self):
        if self.isEnterable() is True:
            self._enterWidget.setText(self._uiDatumText)
    #
    def _updateUiEnterState(self):
        self.setEntered(self._enterWidget.hasFocus())
        #
        if self.isEnterable():
            if self.isEntered():
                self.setUiEnterState(qtCore.EnterState)
            else:
                self.setUiEnterState(qtCore.UnenterState)
        else:
            self.setUiEnterState(qtCore.NormalState)
        #
        self._updateWidgetState()
    #
    def _updateWidgetStyle(self):
        pass
    #
    def _entryAction(self):
        if self.isEnterable() is True:
            text = unicode(self._enterWidget.text())
            if not text == self._uiDatumText:
                self.setDatum(self._covertDatum(text))
                #
                self.widget().entryChanged.emit(), self.widget().datumChanged.emit()
        #
        self._updateQtPressStatusByDatum()
    #
    def _chooseAction(self):
        index = self._datumLis.index(self._datum)
        if len(self._datumLis) == 1:
            self._curDatumIndex = 0
            self.widget().chooseChanged.emit(), self.widget().datumChanged.emit()
        elif len(self._datumLis) > 1:
            if not index == self._curDatumIndex:
                self._curDatumIndex = index
                #
                self._updateEnterWidget()
                #
                self.widget().chooseChanged.emit(), self.widget().datumChanged.emit()
            #
            elif self._enterWidget.text() != self._uiDatumText:
                self._updateEnterWidget()
        #
        self._updateQtPressStatusByDatum()
    # For Override
    def _checkClickAction(self):
        if not self._datum == self._isChecked:
            self.setDatum(self._isChecked)
            #
            self.widget().checkChanged.emit(), self.widget().datumChanged.emit()
        #
        self._updateQtPressStatusByDatum()
    #
    def _updateQtPressStatusByDatum(self):
        if self._defaultDatum is not None:
            if self._datum != self._defaultDatum:
                self._setQtPressStatus(qtCore.WarningStatus)
                self.setUiEnterStatus(qtCore.WarningStatus)
            else:
                self._setQtPressStatus(qtCore.NormalStatus)
                self.setUiEnterStatus(qtCore.NormalStatus)
        else:
            self._setQtPressStatus(qtCore.NormalStatus)
            self.setUiEnterStatus(qtCore.NormalStatus)
        #
        self._updateQtPressStatus()
    #
    def update(self):
        self._updateRectGeometry()
        #
        self._updateChildrenGeometry()
        self._updateButtonVisible()
        #
        self._updateWidgetState()
    #
    def setNameText(self, string):
        if string is not None:
            self._uiNameText = unicode(string)
        #
        if self.nameText() is not None:
            self._enterWidget.setPlaceholderText(u'Enter {} ...'.format(self.nameText()))
    #
    def setDatum(self, datum):
        self._datum = datum
        self._datumType = type(datum)
        self.setDatumText(datum)
        #
        self._updateEnterWidget()
        self._updateButtonVisible()
        #
        self._updateQtPressStatusByDatum()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._pressedTimer = QtCore.QTimer(self._widget)
        self._pressedTimer.timeout.connect(self._pressedAction)
        #
        self._entryButton = self._widget._entryButton
        self._chooseButton = self._widget._chooseButton
        #
        self._copyButton = self._widget._copyButton
        self._clearButton = self.widget()._clearButton
        #
        self._enterWidget = self._widget._enterWidget
    #
    def setEnterEnable(self, boolean):
        self._isEnterEnable = boolean
        #
        self._datumType = unicode
    #
    def isEnterEnable(self):
        return self._isEnterEnable
    #
    def setEnterable(self, boolean):
        self._isEnterable = boolean
        self._enterWidget.setReadOnly(not self.isEnterable())
    #
    def setCheckEnable(self, boolean):
        self._isCheckEnable = boolean
        self.setDatum(self._isChecked)
    #
    def setEnterClear(self):
        self._enterWidget.clear()
        #
        self._datum = None
        self._uiDatumText = None
        #
        self.update()
    #
    def setChooseClear(self):
        self.setDatumLis(None)
        self.widget().chooseChanged.emit(), self.widget().datumChanged.emit()
        self._updateWidgetState()
    #
    def setUiEnterState(self, state):
        if state is qtCore.NormalState:
            self.widget()._uiEnterBackgroundRgba = 0, 0, 0, 0
            self.widget()._uiEnterBorderRgba = 0, 0, 0, 0
        else:
            if state is qtCore.EnterState:
                self.widget()._uiEnterBorderRgba = 63, 127, 255, 255
            elif state is qtCore.UnenterState:
                self.widget()._uiEnterBorderRgba = 95, 95, 95, 255
            #
            self._updateUiEnterStatus()
    #
    def _setQtCheckStyle(self, state):
        if state is qtCore.UncheckableState:
            self._uiCheckIconKeyword = ['svg_basic@svg#boxUncheckable', 'svg_basic@svg#radioUncheckable'][self.isAutoExclusive()]
            self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
        else:
            if state is qtCore.CheckedState:
                self._uiCheckIconKeyword = ['svg_basic@svg#boxChecked', 'svg_basic@svg#radioChecked'][self.isAutoExclusive()]
            elif state is qtCore.UncheckedState:
                self._uiCheckIconKeyword = ['svg_basic@svg#boxUnchecked', 'svg_basic@svg#radioUnchecked'][self.isAutoExclusive()]
            #
            self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])


# Text Brower
class QtTextBrowerItemModel(qtAbstract.QtEnterItemModelAbs):
    def __init__(self, widget):
        self._initDatumEnterItemModelAbs()
        #
        self.__overrideAttr()
        self.__overrideRect()
        #
        self.setWidget(widget)
    #
    def __overrideAttr(self):
        self._isEnterEnable = True
        self._isEnterable = True
        #
        self._isCounterEnable = True
        #
        self._counterWidth = 32
        self._countOffset = 0
        #
        self._isCodingEnable = False
        #
        self._coding = None
    #
    def __overrideRect(self):
        self._uiLineCounterRect = QtCore.QRect()
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side = 0
        #
        xPos += side
        #
        self.basicRect().setRect(
            xPos, yPos,
            width, height
        )
        self._uiLineCounterRect.setRect(
            xPos + 1, yPos + 1,
            self._counterWidth, height - 2
        )
        #
        xPos += self._counterWidth
        #
        self._uiEnterRect.setRect(
            xPos + 1, yPos + 1,
            width - xPos - side - 2, height - 2
        )
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side = 0
        #
        xPos += side
        #
        xPos += self._counterWidth
        #
        self._enterWidget.setGeometry(
            xPos + 1, yPos + 1,
            width - xPos - side - 2, height - 2
        )
    #
    def _updateCounter(self):
        value = self._enterWidget.verticalScrollBar().value()
        #
        self._countOffset = value
        #
        self._updateWidgetState()
    #
    def _updateUiEnterState(self):
        self.setEntered(self._enterWidget.hasFocus())
        #
        if self.isEnterable():
            if self.isEntered():
                self.setUiEnterState(qtCore.EnterState)
            else:
                self.setUiEnterState(qtCore.UnenterState)
        else:
            self.setUiEnterState(qtCore.NormalState)
        #
        self._updateWidgetState()
    #
    def update(self):
        self._updateRectGeometry()
        #
        self._updateChildrenGeometry()
    #
    def setNameText(self, string):
        if string is not None:
            self._uiNameText = unicode(string)
        if self.nameText() is not None:
            self._enterWidget.setPlaceholderText(u'Enter {} ...'.format(self.nameText()))
    #
    def setDatum(self, data):
        self._enterWidget.setText(self._uiDatumText)
    #
    def datum(self):
        return unicode(self._enterWidget.text())
    #
    def isCodingEnable(self):
        return self._isCodingEnable
    #
    def setEnterClear(self):
        self._enterWidget.setPlainText(none)
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._enterWidget = self.widget()._textEdit
    #
    def setUiEnterState(self, state):
        if state is qtCore.NormalState:
            self.widget()._uiEnterBackgroundRgba = 0, 0, 0, 0
            self.widget()._uiEnterBorderRgba = 0, 0, 0, 0
        else:
            if state is qtCore.EnterState:
                self.widget()._uiEnterBorderRgba = 63, 127, 255, 255
            elif state is qtCore.UnenterState:
                self.widget()._uiEnterBorderRgba = 95, 95, 95, 255
            #
            self._updateUiEnterStatus()


# Scroll Bar
class QtScrollBarModel(qtAbstract.QtScrollBarModelAbs):
    def __init__(self, widget):
        self._initScrollBarModelAbs()
        #
        self.setWidget(widget)


#
class Abc_QtTabModel(qtAbstract.QtTabItemModelAbs):
    def _initTabModelBasic(self, widget):
        self._initTabItemModelAbs()
        #
        self.setWidget(widget)
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        width -= 1
        height -= 1
        #
        self.basicRect().setRect(
            xPos+1, yPos+1,
            width, height
        )
        #
        side, spacing = self._uiSide, self._uiSpacing
        frameWidth, frameHeight = self.frameSize()
        #
        if self.tabPosition() == qtCore.South or self.tabPosition() == qtCore.North:
            w, h = self.itemSize()
        else:
            h, w = self.itemSize()
        #
        iconWidth, iconHeight = self.iconSize()
        _w, _h = (h - iconWidth) / 2, (h - iconHeight) / 2
        if self.tabPosition() == qtCore.West:
            # Icon
            if self.icon() is not None:
                self.iconRect().setRect(
                    w - h - side + _w, yPos + _h,
                    iconWidth, iconHeight
                )
            # Name
            if self.nameText() is not None:
                self.nameTextRect().setRect(
                    xPos + frameWidth + spacing + side, yPos,
                    w - frameWidth*2 - spacing*2 - side*2, h
                )
        else:
            xPos += side
            if self.icon() is not None:
                self.iconRect().setRect(
                    xPos + _w, yPos + _h,
                    iconWidth, iconHeight
                )
                xPos += frameWidth + spacing
            #
            if self.nameText() is not None:
                self.nameTextRect().setRect(
                    xPos, yPos,
                    w - frameWidth*2 - spacing*2 - side*2, h
                )
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        width -= 1
        height -= 1
        #
        side, spacing = self._uiSide, self._uiSpacing
        #
        frameWidth, frameHeight = self.frameSize()
        #
        if self.tabPosition() == qtCore.South or self.tabPosition() == qtCore.North:
            w, h = self.itemSize()
        else:
            h, w = self.itemSize()
        #
        _w, _h = (h - frameWidth) / 2,  (h - frameHeight) / 2
        if self.tabPosition() == qtCore.South or self.tabPosition() == qtCore.North:
            self._menuButton.setGeometry(
                w - frameWidth - side + _w - 2, yPos + _h,
                frameWidth, frameHeight
            )
            self._menuButton.setIcon('svg_basic@svg#menu_tab_h')
        else:
            self._menuButton.setGeometry(
                xPos + _h, w - frameWidth - side + _w - 2,
                frameWidth, frameHeight
            )
            self._menuButton.setIcon('svg_basic@svg#menu_tab_v')
        #
        if self.isPressCurrent():
            self._menuButton.show()
        else:
            self._menuButton.hide()
    #
    def _updateGeometry(self):
        self._updateRectGeometry()
        self._updateChildrenGeometry()
    #
    def _hoverAction(self):
        #
        self.update()
    #
    def _pressClickAction(self):
        self.widget().currentToggled.emit(self.isPressCurrent())
        #
        self.update()
    #
    def tabRegion(self):
        itemIndex = self.viewModel().itemModelIndex(self)
        if itemIndex == self.viewModel().minItemIndex():
            return 1
        elif itemIndex == self.viewModel().maxItemIndex():
            return 2
        else:
            return 0
    #
    def update(self):
        self._updateGeometry()
        #
        self._updateWidgetState()
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            if state is qtCore.CurrentState:
                self.widget()._uiNameRgba = [(63, 127, 255, 255), (63, 255, 255, 255)][self.isPressHovered()]
                self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword + ['cur', 'on'][self.isPressHovered()])
            elif state is qtCore.NormalState:
                self.widget()._uiNameRgba = [(191, 191, 191, 255), (223, 223, 223, 255)][self.isPressHovered()]
                self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword + ['', 'on'][self.isPressHovered()])
            #
            self.widget()._uiFontItalic = False


#
class QtTabModel(Abc_QtTabModel):
    def __init__(self, widget):
        self._initTabModelBasic(widget)


#
class QtButtonTabModel(Abc_QtTabModel):
    def __init__(self, widget):
        self._initTabModelBasic(widget)
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self._uiIconKeyword = iconKeyword
        if self._uiIconKeyword is not None:
            self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword)
        else:
            self._uiIcon = None
        #
        self.setFrameSize(frameWidth, frameHeight)
        self.setIconSize(iconWidth, iconHeight)
        #
        self._updateWidgetState()
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            r1, g1, b1, a1 = 143, 143, 143, 255
            r2, g2, b2, a2 = 255, 255, 255, 255
            if state is qtCore.CurrentState:
                self.widget()._uiBackgroundRgba = 71, 71, 71, 255
                self.widget()._uiBorderRgba = [(r1 * .75, g1 * .75, b1 * .75, a1), (r1, g1, b1, a1)][self.isPressHovered()]
                self.widget()._uiNameRgba = [(63, 127, 255, 255), (r2, g2, b2, a2)][self.isPressHovered()]
                if self._uiIconKeyword is not None:
                    self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword + ['cur', 'on'][self.isPressHovered()])
            elif state is qtCore.NormalState:
                self.widget()._uiBackgroundRgba = 63, 63, 63, 255
                self.widget()._uiBorderRgba = [(r1 * .5, g1 * .5, b1 * .5, a1), (r1 * .75, g1 * .75, b1 * .75, a1)][self.isPressHovered()]
                self.widget()._uiNameRgba = [(r2*.75, g2*.75, b2*.75, a2), (r2, g2, b2, a2)][self.isPressHovered()]
                #
                if self._uiIconKeyword is not None:
                    self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword + ['', 'on'][self.isPressHovered()])
            #
            self.widget()._uiFontItalic = False


# Tab Item
class QtShelfTabModel(Abc_QtTabModel):
    def __init__(self, widget):
        self._initTabModelBasic(widget)
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        width -= 1
        height -= 1
        #
        self.basicRect().setRect(
            xPos, yPos,
            width, height
        )
        #
        w, h = self.itemSize()
        #
        iconWidth, iconHeight = self.iconSize()
        #
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            if not self.isPressCurrent() and not self.isPressHovered():
                yPos += 4
                h -= 4
                # noinspection PyArgumentEqualDefault
                self.widget().setFont(qtCore.xFont(size=8, weight=50, family=qtCore._families[2]))
            else:
                # noinspection PyArgumentEqualDefault
                self.widget().setFont(qtCore.xFont(size=10, weight=50, family=qtCore._families[2]))
            #
            self.nameTextRect().setRect(
                xPos, yPos,
                w, h
            )
        else:
            if not self.isPressCurrent() and not self.isPressHovered():
                xPos += 8
                w -= 8
                iconWidth -= 8
                iconHeight -= 8
            #
            self.iconRect().setRect(
                xPos + (w - iconWidth)/2, yPos + (w - iconHeight)/2,
                iconWidth, iconHeight
            )
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        width -= 1
        height -= 1
        #
        w, h = self.itemSize()
        frameWidth, frameHeight = 20, 20
        if self.tabPosition() == qtCore.South or self.tabPosition() == qtCore.North:
            self._closeButton.setGeometry(
                xPos + 2, yPos + 2,
                10, 10
            )
            self._menuButton.setGeometry(
                width - frameWidth + (h - frameWidth)/2, yPos + (h - frameHeight)/2,
                frameWidth, frameHeight
            )
            self._menuButton.setIcon('svg_basic@svg#tabMenu_h')
        else:
            self._closeButton.setGeometry(
                xPos + 2, yPos + 2,
                10, 10
            )
            self._menuButton.setGeometry(
                xPos + (w - frameWidth)/2, yPos + w,
                frameWidth, frameHeight
            )
            self._menuButton.setIcon('svg_basic@svg#menu_d')
        #
        if self.isPressCurrent():
            self._menuButton.show()
        else:
            self._menuButton.hide()
    #
    def _updateGeometry(self):
        self._updateRectGeometry()
        self._updateChildrenGeometry()
    #
    def _hoverAction(self):
        #
        self.update()
    #
    def _pressClickAction(self):
        self.widget().currentToggled.emit(self.isPressCurrent())
        #
        self.update()
    #
    def update(self):
        self._updateGeometry()
        #
        self._updateWidgetState()
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            r2, g2, b2, a2 = 223, 223, 223, 255
            if state is qtCore.CurrentState:
                self.widget()._uiNameRgba = [(63, 127, 255, 255), (r2, g2, b2, a2)][self.isPressHovered()]
                self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword + ['cur', 'on'][self.isPressHovered()])
                if self._uiIconKeyword is not None:
                    self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword + ['cur', 'on'][self.isPressHovered()])
            elif state is qtCore.NormalState:
                self.widget()._uiNameRgba = [(r2*.5, g2*.5, b2*.5, a2), (r2 * .75, g2 * .75, b2 * .75, a2)][self.isPressHovered()]
                if self._uiIconKeyword is not None:
                    self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword + ['', 'on'][self.isPressHovered()])
            #
            self.widget()._uiFontItalic = False


# Choose Tab Item
class QtChooseTabModel(qtAbstract.QtEnterItemModelAbs):
    def __init__(self, widget):
        self._initDatumEnterItemModelAbs()
        #
        self.setWidget(widget)
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        frameWidth, frameHeight = 20, 20
        #
        self.datumRect().setRect(
            xPos, yPos,
            width - frameWidth, height
        )
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        frameWidth, frameHeight = 20, 20
        #
        self.widget()._chooseButton.setGeometry(
            width - frameWidth + (height - frameHeight)/2, yPos + (height - frameWidth)/2,
            frameWidth, frameHeight
        )
    #
    def _chooseAction(self):
        index = self._datumLis.index(self._datum)
        if not index == self._curDatumIndex:
            self._curDatumIndex = index
            #
            self.widget().chooseChanged.emit()
    #
    def update(self):
        self._updateRectGeometry()
        self._updateChildrenGeometry()
    #
    def setWidget(self, widget):
        self._widget = widget


#
class Abc_QtTabBarModel(qtAbstract.QtTabBarModelAbs):
    def _initTabBarModelBasic(self, widget):
        self._initTabBarModelAbs()
        #
        self.setWidget(widget)
        self.setViewport(widget)
    #
    def _updateViewportGeometry(self):
        xPos, yPos = self._uiMargins[0], self._uiMargins[1]
        #
        w, h = self.viewSize()
        #
        self._viewport.setGeometry(
            xPos, yPos,
            w, h
        )
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        w, h = self.itemSize()
        #
        xValue, yValue = self.scrollValue()
        currentItemIndex = self.currentItemIndex()
        #
        self._uiBasicRect.setRect(
            xPos, yPos,
            width, height
        )
    #
    def _updateGeometry(self):
        self._updateViewportGeometry()
        #
        self._updateRectGeometry()
        #
        self._updateItemsGeometry()
    #
    def _clearHover(self):
        if self._hoverItemModel is not None:
            self._hoverItemModel.setPressHovered(False)
        #
        self._hoverItemModel = None
        self._hoverItemIndex = -1
        #
        self._updateWidgetState()
    #
    def update(self):
        self._updateLayoutAttr()
        #
        self._updateViewportSize()
        self._updateAbsSize()
        #
        self._updateScrollState()
        #
        self._updateViewSize()
        #
        self._updateItemModelsPos()
        #
        self._updateGeometry()
        #
        self._updateWidgetState()
    #
    def hScrollSize(self):
        return self._uiHScrollWidth, self._uiHScrollHeight
    #
    def vScrollSize(self):
        return self._uiVScrollWidth, self._uiVScrollHeight
    #
    def isHMaximum(self):
        if self.isHScrollable():
            return self._hScrollValue == self._hScrollMaximum
        else:
            return True
    #
    def isHMinimum(self):
        if self.isHScrollable():
            return self._hScrollValue == self._hScrollMinimum
        else:
            return True
    #
    def isMaximum(self):
        return self.isHMaximum(), self.isVMaximum()
    #
    def isVMaximum(self):
        if self.isVScrollable():
            return self._vScrollValue == self._vScrollMaximum
        else:
            return True
    #
    def isVMinimum(self):
        if self.isVScrollable():
            return self._vScrollValue == self._vScrollMinimum
        else:
            return True
    #
    def isMinimum(self):
        return self.isHMinimum(), self.isVMinimum()


# Tab Bar
class QtTabBarModel(Abc_QtTabBarModel):
    def __init__(self, widget):
        self._initTabBarModelBasic(widget)


#
class Abc_QtTabGroupModel(qtAbstract.QtTabViewModelAbs):
    def _initTabViewModelBasic(self, widget):
        self._initTabViewModelAbs()
        #
        self.setWidget(widget)
        self.setViewport(widget)
    #
    def _updateViewportGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side, spacing = self._uiSide, self._uiSpacing
        #
        w, h = self.tabSize()
        buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
        #
        if self.tabPosition() is qtCore.West:
            _h = (w - buttonHeight) / 2
            # Tab Bar
            self.tabBar().setGeometry(
                xPos, yPos,
                w, height
            )
            #
            self.viewport().setGeometry(
                xPos + w + side, yPos,
                width - w - side, height
            )
        elif self.tabPosition() is qtCore.East:
            _h = (w - buttonHeight) / 2
            # Tab Bar
            self.tabBar().setGeometry(
                width - w, yPos,
                w, height
            )
            #
            self.viewport().setGeometry(
                xPos, yPos,
                width - w - side, height
            )
        elif self.tabPosition() is qtCore.South:
            _w = (h - buttonWidth) / 2
            scrollWidth, scrollHeight = buttonWidth * 3 + _w * 2, h
            # Tab Bar
            self.tabBar().setGeometry(
                xPos, height - h,
                width, h
            )
            #
            self.viewport().setGeometry(
                xPos, yPos,
                width, height - h - side
            )
        else:
            _w = (h - buttonWidth) / 2
            scrollWidth, scrollHeight = buttonWidth * 3 + _w * 2, h
            # Tab Bar
            self.tabBar().setGeometry(
                xPos, yPos,
                width, h
            )
            #
            self.viewport().setGeometry(
                xPos, yPos + h + side,
                width, height - h - side
            )
        if self.tabWidgets():
            for i in self.tabWidgets():
                w, h = self.viewport().width(), self.viewport().height()
                i.setGeometry(
                    0, 0,
                    w, h
                )
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        w, h = self._uiTabBarWidth, self._uiTabBarHeight
        buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
        #
        self.basicRect().setRect(
            xPos, yPos,
            width, height
        )
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            _w = (h - buttonWidth)/2
            scrollWidth, scrollHeight = buttonWidth*3 + _w*2, h
            #
            self.scrollRect().setRect(
                xPos + width - scrollWidth, yPos - 1,
                scrollWidth, scrollHeight
            )
        else:
            _h = (w - buttonHeight) / 2
            scrollWidth, scrollHeight = w, buttonHeight * 3 + _h * 2
            #
            self.scrollRect().setRect(
                xPos - 1, yPos + height - scrollHeight,
                scrollWidth, scrollHeight
            )
    #
    def _updateChildrenGeometry(self):
        pass
    #
    def _updateScrollButtonState(self):
        pass
    #
    def _updateGeometry(self):
        self._updateViewportGeometry()
        #
        self._updateRectGeometry()
        #
        self._updateChildrenGeometry()
    #
    def update(self):
        self._updateGeometry()
        #
        self._updateWidgetState()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._tabBar = self.widget()._tabBar


# Tab View
class QtTabGroupModel(Abc_QtTabGroupModel):
    def __init__(self, widget):
        self._initTabViewModelBasic(widget)


# Window
class QtWindowModel(qtAbstract.QtWindowModelAbs):
    def __init__(self, widget):
        self._initWindowModelAbs()
        #
        self._initAbcQtWindow()
        #
        self._overrideAttr()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setViewportLayout(widget)
    #
    def _overrideAttr(self):
        self._isExpandEnable = True
        self._isExpandable = True
        self._isExpanded = True
    #
    def _initAbcQtWindow(self):
        self._initAbcQtWindowAttr()
        self._initAbcQtWindowUi()
        self._initAbcQtWindowRect()
        self._initAbcQtWindowAction()
        self._initAbcQtWindowVar()
    #
    def _initAbcQtWindowAttr(self):
        self._xMenuPos, self._yMenuPos = 0, 0
        self._xTranslate, self._yTranslate = 0, 0
    #
    def _initAbcQtWindowUi(self):
        pass
    #
    def _initAbcQtWindowRect(self):
        pass
    #
    def _initAbcQtWindowAction(self):
        self._progressTimer.timeout.connect(self.setProgressZero)
    #
    def _initAbcQtWindowVar(self):
        pass
    #
    def _updateWidgetSize(self):
        width, height = self.width(), self.height()
        if self.isExpanded():
            minimumSize = self.viewport().layout().minimumSize()
            w, h = minimumSize.width(), minimumSize.height()
            #
            if self.isMenuEnable():
                h += self._uiMenuHeight
            if self.isStatusEnable():
                h += self._uiStatusHeight
            #
            shadowRadius = self._uiShadowRadius
            l, t, r, b = self.margins()
            #
            width_, height_ = w + l + r + shadowRadius, h + t + b + shadowRadius
        else:
            width_, height_ = 0, self._uiMenuHeight
        #
        self.widget().resize(max(width, width_), max(height, height_))
    #
    def _getEventPos(self, event):
        point = event.pos()
        x, y = point.x(), point.y()
        return x - self._uiMargins[0], y - self._uiMargins[1]
    #
    def _updateHoverLoc(self, x, y):
        pass
    #
    def _updatePressLoc(self, x, y):
        pass
    # Hover
    def _hoverStartAction(self, event):
        pass
    #
    def _hoverExecuteAction(self, event):
        # noinspection PyUnusedLocal
        x, y = self._getEventPos(event)
    #
    def _hoverStopAction(self, event):
        pass
    #
    def _hoverScrollAction(self):
        pass
    #
    def _pressStartAction(self, event, isDoubleClick=False):
        x, y = self._getEventPos(event)
        # Flag
        self._pressFlag, self._dragFlag = True, False
        # Action
        self._dragStartAction(event)
        #
        self._updatePressLoc(x, y)
        #
        if isDoubleClick:
            if self.isMenuRectContainPos((x, y)):
                if self.isExpanded():
                    self._maximizeButtonPressAction()
    #
    def _pressExecuteAction(self, event):
        x, y = self._getEventPos(event)
        # Flag
        self._pressFlag, self._dragFlag = False, True
        # Action
        self._dragExecuteAction(event)
        #
        self._updatePressLoc(x, y)
    #
    def _pressStopAction(self, event):
        self._pressFlag, self._dragFlag = False, False
    #
    def _dragStartAction(self, event):
        self._dragStartPoint = event.globalPos() - self.pos()
    #
    def _dragExecuteAction(self, event):
        if self.isDragable():
            self.widget().move(event.globalPos() - self._dragStartPoint)
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        width -= 1
        height -= 1
        #
        frameWidth, frameHeight = self._uiFrameWidth, self._uiFrameHeight
        shadowRadius = [self._uiShadowRadius, 0][self.isMaximized()]
        #
        self.basicRect().setRect(
            xPos, yPos,
            width - shadowRadius, height - shadowRadius
        )
        # Resize
        if self.isResizeable():
            self.resizeRect().setRect(
                width - frameWidth - shadowRadius - 1, height - frameHeight - shadowRadius - 1,
                frameWidth, frameHeight
            )
        # Placeholder
        if self.isPlaceholderEnable():
            x, y, w, h = self._uiMethod._toGeometryRemap(self.placeholderSize(), self.size())
            self.placeholderRect().setRect(
                x, y, w, h
            )
        #
        if self.direction() is qtCore.Horizontal:
            w, h = (width - shadowRadius) / 4, 4
            pointLis = [
                (xPos + w, yPos),
                (width - w - shadowRadius, yPos),
                (width - w - h - shadowRadius, yPos + h),
                (xPos + w + h, yPos + h),
                (xPos + w, yPos)
            ]
            path = qtCore.QPainterPath_()
            path._addPoints(pointLis)
            self._uiFocusPath = path
        else:
            w, h = 4, (height - shadowRadius) / 4
            pointLis = [
                (width - shadowRadius, yPos + h),
                (width - shadowRadius, height - h - shadowRadius),
                (width - w - shadowRadius, height - w - h - shadowRadius),
                (width - w - shadowRadius, yPos + w + h),
                (width - shadowRadius, yPos + h)
            ]
            path = qtCore.QPainterPath_()
            path._addPoints(pointLis)
            self._uiFocusPath = path
    #
    def _updateMenuButtonGeometry(self):
        width, height = self.width() - 1, self.height() - 1
        #
        menuWidth, menuHeight = self._uiMenuWidth, self._uiMenuHeight
        buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
        #
        isHorizontal = self.direction() is qtCore.Horizontal
        #
        side, spacing, shadowRadius = self._uiSide, self._uiSpacing, [self._uiShadowRadius, 0][self.isMaximized()]
        if isHorizontal:
            xPos, yPos = width - buttonWidth - side - shadowRadius, (menuHeight - buttonHeight)/2
        else:
            xPos, yPos = width - menuHeight + (menuHeight - buttonWidth)/2 - shadowRadius, (menuHeight - buttonWidth)/2
        #
        self._closeButton.setGeometry(
            xPos, yPos,
            buttonWidth, buttonHeight
        )
        # Maximize
        if self.isMaximizeable():
            if isHorizontal:
                xPos -= (buttonWidth + spacing)
            else:
                yPos += (buttonWidth + spacing)
            #
            self._maximizeButton.setGeometry(
                xPos, yPos,
                buttonWidth, buttonHeight
            )
            #
            if self.isExpanded():
                self._maximizeButton.setIconKeyword(['svg_basic@svg#maximize', 'svg_basic@svg#normmize'][self.isMaximized()])
            #
            self._maximizeButton.show()
        else:
            self._maximizeButton.hide()
        # Minimize
        if self.isMinimizeable():
            if isHorizontal:
                xPos -= (buttonWidth + spacing)
            else:
                yPos += (buttonWidth + spacing)
            #
            self._minimizeButton.setGeometry(
                xPos, yPos,
                buttonWidth, buttonHeight
            )
            #
            self._minimizeButton.show()
        else:
            self._minimizeButton.hide()
        # Expand
        if self.isExpandable():
            if isHorizontal:
                xPos -= (buttonWidth + spacing)
            else:
                yPos += (buttonWidth + spacing)
            #
            self._expandButton.setGeometry(
                xPos, yPos,
                buttonWidth, buttonHeight
            )
            #
            if not self.isMaximized():
                iconKeyword = ['svg_basic@svg#unfold', 'svg_basic@svg#fold'][self.isExpanded()]
                self._expandButton.setIconKeyword(iconKeyword)
            #
            self._expandButton.show()
        else:
            self._expandButton.hide()
        # Menu
        if isHorizontal:
            xPos -= (buttonWidth + spacing)
        else:
            yPos += (buttonWidth + spacing)
        #
        self._menuButton.setGeometry(
            xPos, yPos,
            buttonWidth, buttonHeight
        )
        #
        self._xMenuPos, self._yMenuPos = xPos, yPos
        #
        self._progressBar.setGeometry(
            0, -2,
            width - shadowRadius, 1
        )
    #
    def _updateMenuRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        width -= 1
        height -= 1
        #
        menuWidth, menuHeight = self._uiMenuWidth, self._uiMenuHeight
        statusWidth, statusHeight = self._uiStatusWidth, self._uiStatusHeight
        #
        side, spacing, shadowRadius = self._uiSide, self._uiSpacing, [self._uiShadowRadius, 0][self.isMaximized()]
        #
        iconWidth, iconHeight = self._uiIconWidth, self._uiIconHeight
        frameWidth, frameHeight = self._uiMenuHeight, self._uiMenuHeight
        # Menu
        if self.isMenuEnable():
            _w, _h = (frameWidth - iconWidth) / 2, (frameHeight - iconHeight) / 2
            if self.direction() == qtCore.Horizontal:
                x, y = xPos, yPos
                w, h = width - shadowRadius, menuHeight
                #
                xPos += side
                # Icon
                if self.icon() is not None:
                    self.iconRect().setRect(
                        xPos + _w, yPos + _h,
                        iconWidth, iconHeight
                    )
                    #
                    xPos += (frameWidth + spacing)
                # Name
                if self.nameText() is not None:
                    textMaxWidth = self._xMenuPos - xPos
                    self.widget().setFont(self.widget()._uiNameTextFont)
                    textWidth = self._textWidth(self.nameText())
                    rectWidth = min(textMaxWidth, textWidth)
                    self.nameTextRect().setRect(
                        xPos, yPos,
                        rectWidth, frameWidth
                    )
                    xPos += (rectWidth + spacing)
                # Index
                if self.indexText() is not None:
                    textMaxWidth = self._xMenuPos - xPos
                    self.widget().setFont(self.widget()._uiIndexFont)
                    textWidth = self._textWidth(self.indexText())
                    rectWidth = min(textMaxWidth, textWidth)
                    self.indexTextRect().setRect(
                        xPos, yPos,
                        rectWidth, frameWidth
                    )
            else:
                x, y = width - menuHeight - shadowRadius, yPos
                w, h = menuHeight, height - shadowRadius
                #
                xPos += side
                # Icon
                if self.icon() is not None:
                    self.iconRect().setRect(
                        xPos + _w, yPos + _h,
                        iconWidth, iconHeight
                    )
                    xPos += (frameWidth + spacing)
                # Name
                if self.nameText() is not None:
                    self.widget().setFont(self.widget()._uiNameTextFont)
                    textWidth = self._textWidth(self.nameText())
                    rectWidth = textWidth
                    self.nameTextRect().setRect(
                        xPos, yPos,
                        rectWidth, frameWidth
                    )
                    xPos += (rectWidth + spacing)
                # Index
                if self.indexText() is not None:
                    self.widget().setFont(self.widget()._uiIndexFont)
                    textWidth = self._textWidth(self.indexText())
                    rectWidth = textWidth
                    self.indexTextRect().setRect(
                        xPos, yPos,
                        rectWidth, frameWidth
                    )
                    xPos += (textWidth + spacing)
                #
                self._xTranslate, self._yTranslate = width - menuHeight - shadowRadius, height - shadowRadius
            #
            self._uiMenuRect.setRect(
                x, y,
                w, h
            )
    #
    def _updateStatusButtonGeometry(self):
        if self.isStatusEnable() and self.isExpanded():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()
            width -= 1
            height -= 1
            #
            buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
            #
            spacing = self._uiSpacing
            shadowRadius = [self._uiShadowRadius, 0][self.isMaximized()]
            #
            xPos += self._uiSide
            yPos = height - self._uiMenuHeight - shadowRadius + (self._uiMenuHeight - buttonHeight)/2
            self._helpButton.show()
            #
            self._helpButton.setGeometry(
                xPos, yPos,
                buttonWidth, buttonHeight
            )
            #
            if self.isDialogEnable():
                dialogButtonWidth = 96
                xPos = width - dialogButtonWidth - self._uiSide - shadowRadius
                #
                self._cancelButton.show()
                self._cancelButton.setGeometry(
                    xPos, yPos,
                    dialogButtonWidth, buttonHeight
                )
                #
                xPos -= (dialogButtonWidth + spacing)
                #
                self._confirmButton.show()
                self._confirmButton.setGeometry(
                    xPos, yPos,
                    dialogButtonWidth, buttonHeight
                )
            else:
                self._cancelButton.hide()
                self._confirmButton.hide()
        else:
            self._helpButton.hide()
            self._cancelButton.hide()
            self._confirmButton.hide()
    #
    def _updateStatusRectGeometry(self):
        if self.isStatusEnable() and self.isExpanded():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()
            width -= 1
            height -= 1
            #
            buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
            shadowRadius = [self._uiShadowRadius, 0][self.isMaximized()]
            #
            yPos = height - self._uiStatusHeight - shadowRadius
            #
            buttonWidth, buttonHeight = buttonWidth, buttonHeight
            #
            statusWidth, statusHeight = width - shadowRadius, self._uiStatusHeight
            #
            self.statusRect().setRect(
                xPos, yPos,
                statusWidth, self._uiStatusHeight
            )
            #
            self.statusTextRect().setRect(
                xPos + buttonWidth, yPos + (statusHeight - buttonHeight)/2,
                self._uiStatusTextWidth, buttonHeight
            )
    #
    def _updatePercentRectGeometry(self):
        if self.isPercentEnable():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()
            width -= 1
            height -= 1
            #
            menuWidth, menuHeight = self._uiMenuWidth, self._uiMenuHeight
            #
            shadowRadius = [self._uiShadowRadius, 0][self.isMaximized()]
            #
            if self.direction() == qtCore.Horizontal:
                maxWidth = width - shadowRadius
                percent = min(float(self._uiProgressValue) / float(self._uiMaxProgressValue), 1)
                #
                self._uiPercentValueRect.setRect(
                    xPos + 1, yPos + self._uiMenuHeight - 2,
                    maxWidth * percent, 1
                )
            else:
                maxHeight = height - shadowRadius
                percent = min(float(self._uiProgressValue) / float(self._uiMaxProgressValue), 1)
                #
                self._uiPercentValueRect.setRect(
                    width - menuHeight - shadowRadius, yPos,
                    1, maxHeight * percent
                )
    #
    def _updateViewportGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        menuWidth, menuHeight = self._uiMenuWidth, self._uiMenuHeight
        statusWidth, statusHeight = self._uiStatusWidth, self._uiStatusHeight
        #
        shadowRadius = [self._uiShadowRadius, 0][self.isMaximized()]
        #
        if self.isExpanded():
            self.viewport().show()
            #
            if self.direction() is qtCore.Horizontal:
                x, y = xPos, yPos + self._uiMenuHeight
                w = width - shadowRadius
                #
                if self.isStatusEnable():
                    h = height - (menuHeight + statusHeight) - shadowRadius
                else:
                    h = height - menuHeight - shadowRadius
            else:
                x, y = xPos, yPos
                w = width - menuHeight - shadowRadius
                #
                if self.isStatusEnable():
                    h = height - statusHeight - shadowRadius
                else:
                    h = height - shadowRadius
            #
            self.viewport().setGeometry(
                *self._toViewportGeometryArgs(x, y, w, h)
            )
        else:
            self.viewport().hide()
    #
    def _updateGeometry(self):
        self._updateRectGeometry()
        #
        self._updateMenuButtonGeometry()
        self._updateMenuRectGeometry()
        #
        self._updateStatusButtonGeometry()
        self._updateStatusRectGeometry()
        #
        self._updateViewportGeometry()
        #
        self._updatePercentRectGeometry()
    # noinspection PyUnusedLocal
    def _resizeAction(self, event, message):
        if self.isResizeable():
            return qtCore.nativeEve(self._widget, message)
        else:
            return False, 0
    # Button
    def _maximizeButtonPressAction(self):
        if self.isMaximizeable():
            boolean = self.widget().isMaximized()
            if boolean:
                self._isMaximized = False
                self.widget().showNormal()
            else:
                self._isMaximized = True
                self.widget().showMaximized()
        #
        boolean = self.isMaximized()
        #
        self.setDragable(not boolean)
        self.setResizeable(not boolean)
        #
        self._expandButton.setPressable(not boolean)
        #
        self.update()
    #
    def _minimizeButtonPressAction(self):
        if self.isMinimizeable():
            if self.widget().isMinimized():
                self._isMinimized = False
            else:
                self._isMinimized = True
                #
                self.widget().showMinimized()
        #
        self.update()
    #
    def _expandButtonPressAction(self):
        if self.isExpandable():
            xPos, yPos = self.x(), self.y()
            currentWidth, currentHeight = self.width(), self.height()
            if self._isExpanded is True:
                shadowRadius = [self._uiShadowRadius, 0][self.isMaximized()]
                #
                if self.direction() is qtCore.Horizontal:
                    width, height = self._uiMenuWidth, self._uiMenuHeight + shadowRadius + 1
                else:
                    width, height = self._uiMenuHeight + shadowRadius + 1, self._uiMenuWidth
                #
                self._uiWidth, self._uiHeight = currentWidth, currentHeight
                #
                x, y = xPos + currentWidth - width, yPos
                #
                self.widget().setGeometry(
                    x, y,
                    width, height
                )
                #
                self._isExpanded = False
            else:
                width, height = self._uiWidth, self._uiHeight
                #
                x, y = xPos + currentWidth - width, yPos
                #
                self.widget().setGeometry(
                    x, y,
                    width, height
                )
                #
                self._isExpanded = True
            #
            boolean = self.isExpanded()
            #
            self.setResizeable(boolean)
            #
            self._maximizeButton.setPressable(boolean)
        #
        self._updateWidgetSize()
        self.update()
    #
    def _setCtrlFlag(self, boolean):
        self._ctrlFlag = boolean
        #
        self._updateWidgetState()
    #
    def _setShiftFlag(self, boolean):
        self._shiftFlag = boolean
        #
        self._updateWidgetState()
    #
    def _setAltFlag(self, boolean):
        self._altFlag = boolean
        #
        self._updateWidgetState()
    #
    def setProgressZero(self):
        if self.isMessageWindow() is False:
            self._uiMaxProgressValue = 1
            self._uiProgressValue = 0
            self._updatePercentRectGeometry()
            self._updateWidgetState()
            #
            self.setPercentEnable(False)
            #
            self._progressTimer.stop()
    #
    def _progressValueChangeAction(self):
        if self._uiProgressValue >= self._uiMaxProgressValue:
            self._progressTimer.start(500)
        #
        self._updatePercentRectGeometry()
        self._updateWidgetState()
    #
    def update(self):
        self._updateGeometry()
        #
        self._updateWidgetState()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self.widget().setMouseTracking(True)
        #
        self._menuButton = self.widget()._menuButton
        self._closeButton = self.widget()._closeButton
        self._maximizeButton = self.widget()._maximizeButton
        self._minimizeButton = self.widget()._minimizeButton
        self._expandButton = self.widget()._expandButton
        #
        self._helpButton = self.widget()._helpButton
        self._cancelButton = self.widget()._cancelButton
        self._confirmButton = self.widget()._confirmButton
        #
        self._progressBar = self.widget()._progressBar
    #
    def setSpacing(self, value):
        self._uiSpacing = value
    #
    def spacing(self):
        return self._uiSpacing


# Action Item
class QtActionItemModel(Abc_QtItemModel):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideAttr()
        self.__overrideUi()
        self.__connectUi(widget)
    #
    def __overrideAttr(self):
        self._isSeparator = False
        self._isExtendEnable = False
        #
        self._checkFn = None
        #
        self._uiExtendIconKeyword = None
        self._uiExtendIcon = None
        #
        self._uiFrameWidth, self._uiFrameHeight = 20, 20
        self._uiIconWidth, self._uiIconHeight = 16, 16
        #
        self._uiOffset, self._uiSide, self._uiSpacing, self._uiShadowRadius = 0, 2, 2, 4
        #
        self._uiItemWidth, self._uiItemHeight = 200, 20
        self._uiItemSize = 200, 20
        #
        self._pressAction = None
        self._itemActionData = []
    #
    def __overrideUi(self):
        self._uiBasicRect = QtCore.QRect()
        self._basicLine = QtCore.QLine()
        self._uiIconRect, self._uiNameTextRect, self._uiSubNameRect, self._uiExtendRect = QtCore.QRect(), QtCore.QRect(), QtCore.QRect(), QtCore.QRect()
        self._uiSubIconRect = QtCore.QRect()
    #
    def __connectUi(self, widget):
        self._widget = widget
        self._extendButton = widget._extendButton
    #
    def setViewModel(self, model):
        self._viewModel = model
        self.widget().setParent(model._widget)
        #
        self._graphModelWidget = self._viewModel._widget
    #
    def _updateRectGeometry(self):
        self._updateUiStyle()
        #
        xPos, yPos = 0, 0
        #
        side, spacing, shadowRadius = self._uiSide, self._uiSpacing, self._uiShadowRadius
        #
        width, height = self._uiItemWidth, self._uiItemHeight
        #
        frameWidth, frameHeight = self.frameSize()
        iconWidth, iconHeight = self.iconSize()
        #
        if self._isSeparator is True:
            xP1, yP1 = xPos, yPos + self._uiItemHeight/2
            xP2, yP2 = width - 1, yPos + self._uiItemHeight/2
            if self._uiNameText is not None:
                textWidth = self.widget().fontMetrics().width(self._uiNameText)
                #
                self._uiNameTextRect.setRect(
                    xPos + self._uiSide, yPos,
                    width, self._uiItemHeight
                )
                xP1 += side + textWidth + spacing
            #
            self._basicLine.setLine(
                xP1, yP1,
                xP2, yP2
             )
        else:
            self._uiBasicRect.setRect(
                xPos, yPos,
                width - 1, height - 1
            )
            xPos += side
            #
            _w, _h = (frameWidth - iconWidth)/2, (frameHeight - iconHeight)/2
            if self._uiIcon is not None or self._uiCheckIcon is not None:
                if self._uiSubIcon is not None:
                    self._uiIconRect.setRect(
                        xPos, yPos,
                        iconWidth, iconHeight
                    )
                    self._uiSubIconRect.setRect(
                        xPos + (frameWidth - iconWidth*.75), yPos + (frameHeight - iconHeight*.75),
                        iconWidth*.75, iconHeight*.75
                    )
                else:
                    self._uiIconRect.setRect(
                        xPos + _w, yPos + _h,
                        iconWidth, iconHeight
                    )
                xPos += self._uiFrameWidth + self._uiSpacing
            if self._uiNameText is not None:
                self._uiNameTextRect.setRect(
                    xPos, yPos,
                    width, self._uiItemHeight
                )
            if self._uiSubNameText is not None:
                self._uiSubNameRect.setRect(
                    0, yPos,
                    width - [0, self._uiFrameWidth][self._isExtendEnable] - side - shadowRadius, self._uiItemHeight
                )
            if self._uiExtendIcon is not None:
                self._uiExtendRect.setRect(
                    width - self._uiFrameWidth + (self._uiFrameWidth - self._uiIconWidth)/2 - side, yPos + (self._uiFrameWidth - self._uiIconHeight)/2,
                    self._uiIconWidth, self._uiIconHeight
                )
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = self._uiItemWidth - self._uiFrameWidth, 0
        self._extendButton.setGeometry(
            xPos, yPos,
            self._uiFrameWidth, self._uiFrameHeight
        )
    #
    def _updateGeometry(self):
        self._updateRectGeometry()
        self._updateChildrenGeometry()
    #
    def _clickAction(self, event):
        if self.isPressable() or self.isExtendEnable():
            self.widget().clicked.emit()
        #
        event.ignore()
    #
    def _updateUiStyle(self):
        if (self.isPressable() or self.isExtendEnable()) and not self.isSeparator():
            self._setQtPressStyle([qtCore.UnpressedState, qtCore.PressedState][self.isPressCurrent()])
        else:
            self._setQtPressStyle(qtCore.UnpressableState)
        #
        if self._isCheckEnable is True:
            if self._isCheckable is True:
                self._setQtCheckStyle([qtCore.UncheckedState, qtCore.CheckedState][self.isChecked()])
            else:
                self._setQtCheckStyle(qtCore.UncheckableState)
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            if self._uiIconKeyword is not None:
                self._uiIcon = qtCore._toLxOsIconFile('svg_basic@svg#unused')
            if self._uiSubIconKeyword is not None:
                self._uiSubIcon = None
            if self._uiExtendIconKeyword is not None:
                self._uiExtendIcon = None
            #
            self.widget()._uiBackgroundRgba = 0, 0, 0, 0
            self.widget()._uiBorderRgba = 0, 0, 0, 0
            #
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            if state is qtCore.UnpressedState:
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword)
                if self._uiExtendIconKeyword is not None:
                    self._uiExtendIcon = qtCore._toLxOsIconFile(self._uiExtendIconKeyword)
                #
                self.widget()._uiBackgroundRgba = 0, 0, 0, 0
                self.widget()._uiBorderRgba = 0, 0, 0, 0
                #
                self.widget()._uiNameRgba = 191, 191, 191, 255
                #
                self.widget()._uiFontItalic = False
            elif state is qtCore.PressedState:
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + 'on')
                if self._uiExtendIconKeyword is not None:
                    self._uiExtendIcon = qtCore._toLxOsIconFile(self._uiExtendIconKeyword + 'on')
                #
                self.widget()._uiBackgroundRgba = 71, 71, 71, 255
                self.widget()._uiBorderRgba = 71, 71, 71, 255
                #
                self.widget()._uiNameRgba = 63, 255, 255, 255
                #
                self.widget()._uiFontItalic = False
            #
            if self._uiSubIconKeyword is not None:
                self._uiSubIcon = qtCore._toLxOsIconFile(self._uiSubIconKeyword)
        #
        self._updateWidgetState()
    #
    def update(self):
        self._updateGeometry()
        #
        self._updateWidgetState()
    #
    def setSeparators(self, boolean=True):
        self._isSeparator = boolean
    #
    def isSeparator(self):
        return self._isSeparator
    #
    def setExtendEnable(self, boolean):
        self._isExtendEnable = boolean
    #
    def isExtendEnable(self):
        return self._isExtendEnable
    #
    def setActionData(self, data):
        if len(data) >= 3:
            self.setPressable(True)
            #
            name, iconKeyword, enable = data[:3]
            #
            if isinstance(name, str) or isinstance(name, unicode):
                pass
            elif isinstance(name, tuple) or isinstance(name, list):
                pass
            if '#' in name:
                name, subName = name.split('#')
                self._uiSubNameText = subName
            #
            self._uiNameText = name
            self._isCheckEnable = iconKeyword == 'checkBox'
            #
            if self.isCheckEnable():
                if isinstance(enable, types.FunctionType) or isinstance(enable, types.MethodType):
                    self._checkFn = enable
                    self._isChecked = enable()
                elif isinstance(enable, bool):
                    self._isChecked = enable
                #
                if self._isChecked is None:
                    self.setPressable(False)
                    self.setCheckable(False)
                else:
                    self.setPressable(True)
                    self.setCheckable(True)
            else:
                if isinstance(iconKeyword, tuple) or isinstance(iconKeyword, list):
                    iconKeyword, subIconKeyword = iconKeyword
                else:
                    subIconKeyword = None
                #
                if iconKeyword:
                    self._uiIconKeyword = iconKeyword
                #
                if subIconKeyword:
                    self._uiSubIconKeyword = subIconKeyword
                #
                if isinstance(enable, types.FunctionType) or isinstance(enable, types.MethodType):
                    self._isPressable = enable()
                elif isinstance(enable, bool):
                    self._isPressable = enable
                elif isinstance(enable, tuple) or isinstance(enable, list):
                    self._isExtendEnable = True
                    self._uiExtendIconKeyword = 'svg_basic@svg#tabMenu_h'
                    self._itemActionData = enable
            #
            if len(data) >= 4:
                action = data[3]
                if isinstance(action, types.FunctionType) or isinstance(action, types.MethodType):
                    self.setPressAction(action)
                elif isinstance(action, str) or isinstance(action, unicode):
                    self.setPressCommand(action)
            if len(data) >= 5:
                subAction = data[4]
                if subAction:
                    if isinstance(subAction, types.FunctionType) or isinstance(subAction, types.MethodType):
                        self._extendButton.show()
                        self._extendButton.clicked.connect(subAction)
        #
        else:
            self.setPressable(False)
            self.setSeparators()
            #
            if len(data) >= 1:
                self._uiNameText = data[0]
        #
        self._updateUiStyle()
    #
    def setItemSize(self, width, height):
        self._uiItemWidth, self._uiItemHeight = width, height
        #
        self.update()
    #
    def itemActionData(self):
        return self._itemActionData
    #
    def setChecked(self, boolean, ignoreAction=False):
        if not boolean == self._isChecked:
            if self._checkFn is not None:
                isChecked = self._checkFn()
                if isChecked is not None:
                    if isChecked != boolean:
                        self.acceptPressAction()
            #
            self._isChecked = boolean
            #
            self._updateQtCheckStyle()
    #
    def isChecked(self):
        if self._checkFn is not None:
            isChecked = self._checkFn()
            self._isChecked = isChecked
        #
        return self._isChecked
    #
    def setPressCurrent(self, boolean, ignoreAction=False):
        if not boolean == self._isPressCurrent:
            self._isPressCurrent = boolean
            #
            self._updateUiStyle()


# Action Drop View
class QtActionDropViewModel(qtAbstract.QtActionDropViewModelAbs):
    def __init__(self, widget, itemClass):
        self._initActionDropViewModelAbs()
        #
        self.setWidget(widget)
        self.setScrollBar(widget)
        self.setButton(widget)
        #
        self._itemClass = itemClass


# Choose View
class QtChooseViewModel(Abc_QtViewModel):
    def __init__(self, widget):
        self._initViewModelBasic(widget)
        #
        self.__overrideViewAttr()
    #
    def __overrideViewAttr(self):
        self._isHScrollEnable, self._isVScrollEnable = False, True


# Choose Drop View
class QtChooseDropViewModel(qtAbstract.QtChooseDropViewModelAbs):
    def __init__(self, widget, itemClass):
        self._initChooseDropViewModelAbs()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setButton(widget)
        self._itemClass = itemClass


# Icon Button
class QtIconbuttonModel(Abc_QtItemModel):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        pass
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        width -= 1
        height -= 1
        #
        self._uiBasicRect.setRect(
            xPos, yPos,
            width, height
        )
        # Icon
        if self.icon() is not None:
            self.iconRect().setRect(
                xPos + (self._uiFrameWidth - self._uiIconWidth)/2 + [0, 1][self._pressFlag], yPos + (self._uiFrameHeight - self._uiIconHeight)/2 + [0, 1][self._pressFlag],
                self._uiIconWidth, self._uiIconHeight
            )
            if self.extendIcon() is not None:
                self.extendIconRect().setRect(
                    xPos + (self._uiExtendFrameWidth - self._uiExtendIconWidth)/2, yPos + (self._uiExtendFrameHeight - self._uiExtendIconHeight)/2,
                    self._uiExtendIconWidth, self._uiExtendIconHeight
                )
            xPos += self._uiFrameWidth + self._uiSpacing
        # Name
        if self.nameText() is not None:
            self._uiNameTextRect.setRect(
                xPos, yPos,
                width - xPos, self._uiFrameHeight
            )
    #
    def _updateQtPressStyle(self):
        if self.isPressEnable():
            if self.isPressable():
                self._setQtPressStyle(qtCore.NormalState)
                #
                self._updateQtPressStatus()
            else:
                self._setQtPressStyle(qtCore.UnpressableState)
        #
        self._updateWidgetState()
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            if self._uiIconKeyword is not None:
                self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + 'off')
            #
            self.widget().update()
            #
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            if state is qtCore.NormalState:
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + ['', 'on'][self.isPressHovered()])
                #
                if self._uiExtendIconKeyword is not None:
                    self._uiExtendIcon = qtCore._toLxOsIconFile(self._uiExtendIconKeyword + ['', 'on'][self.isExtendPressHovered()])
                #
                self.widget()._uiFontItalic = False


# Press Button
class QtPressbuttonModel(Abc_QtItemModel):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        self._uiSide = 4
        self._uiFrameWidth, self._uiFrameHeight = 24, 24
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side = self._uiSide
        #
        frameWidth, frameHeight = self.frameSize()
        iconWidth, iconHeight = self.iconSize()
        #
        xOffset, yOffset = [0, 1][self._pressFlag], [0, 1][self._pressFlag]
        #
        self.basicRect().setRect(
            xPos + xOffset, yPos + yOffset,
            width - xOffset, height - yOffset
        )
        #
        if self.isPercentEnable():
            self.percentFrameRect().setRect(
                xPos + 1 + xOffset, yPos + 1 + yOffset,
                width - 2 - xOffset, height - 2 - yOffset
            )
            #
            if self._valueMaximum > 0:
                rectWidth = max(int(width*self._valuePercent), 10)
            else:
                rectWidth = width
            #
            self._uiPercentValueRect.setRect(
                xPos + (width - rectWidth) + 3 + xOffset, yPos + 3 + yOffset,
                rectWidth - 6 - xOffset, height - 6 - yOffset
            )
        # Icon
        if self.icon() is not None:
            self.iconRect().setRect(
                xPos + (frameWidth - iconWidth)/2 + xOffset, yPos + (frameHeight - iconHeight)/2 + yOffset,
                iconWidth, iconHeight
            )
            if self.extendIcon() is not None:
                self.extendIconRect().setRect(
                    xPos + (self._uiExtendFrameWidth - self._uiExtendIconWidth)/2, yPos + (self._uiExtendFrameHeight - self._uiExtendIconHeight)/2,
                    self._uiExtendIconWidth, self._uiExtendIconHeight
                )
            xPos += frameWidth + self._uiSpacing
        else:
            xPos += side
        # Name
        if self.nameText() is not None:
            if self.isPercentEnable():
                percentTextWidth = self._textWidth(self.percentText())
                self.percentTextRect().setRect(
                    width - percentTextWidth - side - 3 + xOffset, yPos + yOffset,
                    percentTextWidth, height
                )
            else:
                percentTextWidth = 0
            #
            self.nameTextRect().setRect(
                xPos + xOffset, yPos + yOffset,
                width - xPos - percentTextWidth - side, height
            )
    #
    def _updateQtPressStatus(self):
        if self.isPercentEnable():
            self._setUiPercentStatus(self._valuePercent)
        else:
            status = self._uiPressStatus
            #
            if status is qtCore.OffStatus:
                self.widget()._uiBackgroundRgba = 55, 55, 55, 255
            else:
                if status is qtCore.NormalStatus:
                    self.widget()._uiBackgroundRgba = [(79, 79, 79, 255), (119, 119, 119, 255)][self.isPressHovered()]
                else:
                    if status is qtCore.ErrorStatus:
                        r, g, b = 255, 0, 64
                    elif status is qtCore.WarningStatus:
                        r, g, b = 255, 255, 64
                    elif status is qtCore.OnStatus:
                        r, g, b = 64, 255, 127
                    else:
                        r, g, b = 159, 159, 159
                    #
                    self.widget()._uiBackgroundRgba = [(r*.5, g*.5, b*.5, 255), (r*.75, g*.75, b*.75, 255)][self.isPressHovered()]
    #
    def _setUiPercentStatus(self, percent):
        if self.isPercentable():
            if self._valueMaximum > 0:
                if percent == 1:
                    r, g, b = 64, 255, 127
                else:
                    r, g, b = self.hsvToRgb(45 * percent, 1, 1)
                #
                self.widget()._uiPercentValueRgba = [(r * .5, g * .5, b * .5, 255), (r * .75, g * .75, b * .75, 255)][self.isPressHovered()]
        else:
            self.widget()._uiPercentValueRgba = 79, 79, 79, 255
    #
    def _updateQtPressStyle(self):
        if self.isPressEnable():
            if self.isPressable():
                if self._pressFlag is True:
                    self._setQtPressStyle(qtCore.PressedState)
                else:
                    self._setQtPressStyle(qtCore.NormalState)
                    self._updateQtPressStatus()
            else:
                self._setQtPressStyle(qtCore.UnpressableState)
        #
        self._updateWidgetState()
    #
    def _updateWidgetStyle(self):
        pass
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            self.widget()._uiBackgroundRgba = 55, 55, 55, 255
            self.widget()._uiBorderRgba = 63, 63, 63, 255
            #
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiBorderStyle = 'inset'
            #
            self.widget()._uiFontItalic = True
        else:
            if state is qtCore.NormalState:
                self.widget()._uiBackgroundRgba = [(79, 79, 79, 255), (119, 119, 119, 255)][self.isPressHovered()]
                self.widget()._uiBorderRgba = [(127, 127, 127, 255), (159, 159, 159, 255)][self.isPressHovered()]
                self.widget()._uiNameRgba = [(191, 191, 191, 255), (255, 255, 255, 255)][self.isPressHovered()]
                #
                self.widget()._uiBorderStyle = 'outset'
            elif state is qtCore.PressedState:
                self.widget()._uiBackgroundRgba = 47, 47, 47, 255
                #
                self.widget()._uiBorderRgba = 63, 127, 255, 255
                self.widget()._uiNameRgba = 255, 255, 255, 255
                #
                self.widget()._uiBorderStyle = 'inset'
            #
            self.widget()._uiFontItalic = False
    # noinspection PyUnresolvedReferences
    def acceptPressCommand(self):
        if self._pressCommand is not None:
            if lxBasic.isMayaApp():
                import maya.mel as mel
                mel.eval(self._pressCommand)
            else:
                exec eval(self._pressCommand)
        #
        self.setPressHovered(False)


# Attribute Item
class QtAttributeItemModel(Abc_QtItemModel):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        self._isPressEnable = False
        self._isExpandEnable = True
        self._isColorEnable = True


#
class Abc_QtChartModel(qtAbstract.QtChartModelAbs):
    _angle = math.radians
    _sin = math.sin
    _cos = math.cos
    _tan = math.tan
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
    def _initChartBasic(self):
        self._initChartModelAbs()
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.size()
        #
        width -= 1
        height -= 1
        #
        side = 8
        #
        self.basicRect().setRect(
            xPos, yPos,
            width, height
        )
        if self.image():
            x, y, w, h = self._toGeometryRemap(self.imageSize(), self.size())
            #
            self.imageRect().setRect(
                xPos + x + side/2, yPos + y + side/2,
                w - side, h - side
            )
    #
    def _updateDrawDatum(self):
        pass
    #
    def update(self):
        self._updateRectGeometry()
        self._updateDrawDatum()


#
class Abc_QtGroupModel(qtAbstract.QtGroupModelAbs):
    def _initGroupModelBasic(self, widget):
        self._initGroupModelAbs()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setViewportLayout(widget)
    #
    def _expandClickAction(self):
        if self.isExpandable():
            self.widget().expanded.emit()
        #
        self.update()
    #
    def _updateWidgetSize(self):
        frameWidth, frameHeight = self.frameSize()
        #
        width_, height_ = 0, frameHeight
        if self.isSeparated() is False:
            if self.isExpanded():
                layout = self.viewport().layout()
                count = layout.count()
                if count:
                    minimumSize = layout.minimumSize()
                    w, h = minimumSize.width(), minimumSize.height()
                    height_ = frameHeight + h
        #
        self.widget().setMinimumSize(width_, height_ + self.groupSpacing())
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.size()
        #
        width -= 1
        height -= 1
        #
        self.basicRect().setRect(
            xPos, yPos,
            width, height
        )
        #
        side, spacing = self._uiSide, self._uiSpacing
        frameWidth, frameHeight = self.frameSize()
        buttonWidth, buttonHeight = self.buttonSize()
        # Image
        if self.image() is not None:
            x, y, w, h = self._toGeometryRemap(self.imageSize(), self.size())
            #
            self.imageRect().setRect(
                xPos + x + side / 2, yPos + y + side / 2,
                w - side, h - side
            )
        #
        xPos += side
        # Color
        if self.isColorEnable():
            self._updateColorRect(xPos, yPos)
            xPos += frameWidth + self._uiSpacing
        # Expand
        if self.isExpandEnable():
            self._updateExpandRect(xPos, yPos, width, height)
            xPos += frameWidth + self._uiSpacing
        # Name
        if self.nameText() is not None:
            self._updateNameTextRect(xPos, yPos, width-(buttonWidth+spacing)-side, height)
    #
    def _updateViewportGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.size()
        width -= 1
        height -= 1
        #
        frameWidth, frameHeight = self.frameSize()
        #
        yPos += frameHeight
        if self.isSeparated() is False:
            if self.isExpanded():
                self._updateViewportRect(
                    xPos, yPos,
                    width, height
                )
                #
                # self.viewport().setGeometry(
                #     xPos, yPos,
                #     width, height-yPos
                # )
                #
                self.viewport().show()
            else:
                self.viewport().hide()
        else:
            self.viewport().show()
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.size()
        width -= 1
        height -= 1
        #
        side, spacing = self._uiSide, self._uiSpacing
        frameWidth, frameHeight = self.frameSize()
        buttonWidth, buttonHeight = self.buttonSize()
        #
        xPos += side
        _w, _h = (frameWidth - buttonWidth) / 2, (frameHeight - buttonHeight) / 2
        #
        xPos = width - side - buttonWidth
        #
        self.widget()._separateButton.setGeometry(
            width - side - buttonWidth, yPos + _h,
            buttonWidth, buttonHeight
        )
        #
        xPos -= buttonWidth + spacing
        self.widget()._menuButton.setGeometry(
            xPos, yPos + _h,
            buttonWidth, buttonHeight
        )
    #
    def setUnpin(self):
        self.setSeparated(True)
        self.update()
        #
        windowModel = self.widget()._separateWindow.viewModel()
        windowModel.setConnectViewport(self.viewport())
        windowModel.setExpanded(True)
        #
        frameWidth, frameHeight = self.frameSize()
        #
        self.widget()._separateWindow.setNameText(self.nameText())
        #
        if hasattr(self, '_viewportGeometryRecord'):
            x, y, w, h = self._viewportGeometryRecord
        else:
            w = self.width() + 8
            h = qtCore.getWidgetMinimumHeight(self.viewport()) + 32 + 8
            op = self.widget().pos()
            p = self.widget().mapToGlobal(op)
            x, y = p.x() - op.x(), p.y() - op.y()
        #
        self.widget()._separateWindow.setGeometry(
            x - frameWidth, y + frameHeight,
            w, h
        )
        self.widget()._separateWindow.show()
        #
        self._setSeparateButtonSwitch()
    #
    def setPin(self):
        op = self.widget()._separateWindow.pos()
        p = self.widget()._separateWindow.mapToGlobal(op)
        x, y = p.x() - op.x(), p.y() - op.y()
        w, h = self.widget()._separateWindow.width(), self.widget()._separateWindow.height()
        self._viewportGeometryRecord = x, y, w, h
        #
        self.widgetLayout().addWidget(self.viewport())
        #
        self.setSeparated(False)
        #
        self.update()
        #
        self.widget()._separateWindow.hide()
        #
        self._setSeparateButtonSwitch()
    #
    def _separateSwitchAction(self):
        if self.isSeparated():
            self.setPin()
        else:
            self.setUnpin()
        #
        self.widget().separated.emit()
    #
    def _setSeparateButtonSwitch(self):
        iconKeyword = ['svg_basic@svg#separateWindow', 'svg_basic@svg#unseparateWindow'][self.isSeparated()]
        self.widget()._separateButton.setIcon(iconKeyword)
    #
    def setActionData(self, actionData, title):
        self._menuButton.setActionData(actionData)
    #
    def setWidget(self, widget):
        self._widget = widget
        self._menuButton = widget._menuButton
    #
    def setViewport(self, widget):
        if hasattr(widget, '_viewport'):
            self._viewport = widget._viewport
        else:
            self._viewport = qtCore.QWidget_(self.widget())
        #
        self._widgetLayout = qtCore.QVBoxLayout(self.widget())
        self._widgetLayout.setContentsMargins(0, 0, 0, 0)
        self._widgetLayout.setSpacing(0)
        #
        self._widgetLayout.addWidget(self._viewport)
        #
        self._viewport.setGeometry(0, 0, 0, 0)
        self._viewport.setAttribute(
            QtCore.Qt.WA_TranslucentBackground | QtCore.Qt.WA_TransparentForMouseEvents
        )
        self._viewport.setMouseTracking(True)
        #
        self._viewport.setFocusProxy(self.widget())
    #
    def update(self):
        self._updateWidgetSizePolicy()
        self._updateWidgetSize()
        #
        self._updateViewportGeometry()
        #
        self._updateChildrenGeometry()
        self._updateRectGeometry()
        #
        self._updateWidgetState()
    #
    def setFilterColor(self, rgba):
        if rgba is not None:
            self.setColorEnable(True)
            #
            self.widget()._uiColorBackgroundRgba = rgba
        else:
            self.setColorEnable(False)
        #
        self._updateQtPressStyle()


#
class QtGroupModel(Abc_QtGroupModel):
    def __init__(self, widget):
        self._initGroupModelBasic(widget)

