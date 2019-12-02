# coding:utf-8
from LxUi import uiCore
#
from LxUi.qt.uiBasic import uiModelBasic

#
QtGui = uiCore.QtGui
QtCore = uiCore.QtCore
#
_point = QtCore.QPoint
_line = QtCore.QLine
_rect = QtCore.QRect


#
class UiFilterCheckItemModel(uiModelBasic._UiItemModelBasic):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideItemAttr()
        self.__overrideItemUi()
    #
    def __overrideItemAttr(self):
        self._isPressEnable = False
        self._isExpandEnable = False
        self._isCheckEnable = True
        self._isCheckButton = True
        #
        self._isViewFilterEnable = True
        #
        self._uiSubNameWidth = 96
        #
        self._filterChildren = []
        #
        self._maxFilterCount = 0
        self._viewFilterItemModelIndexCount = 0
        #
        self._viewFilterItemModelIndexLis = []
    #
    def __overrideItemUi(self):
        self._uiCheckIconKeyword = 'svg_basic@svg#boxUnchecked'
        self._uiCheckIcon = uiCore._toLxOsIconFile(self._uiCheckIconKeyword)
    @staticmethod
    def _updateFilterParent(parentItemModel, childItemModel):
        def action():
            if childItemModel._viewFilterItemModelIndexCount > 0:
                if parentItemModel.isChecked():
                    childItemModel.setCheckable(True)
                else:
                    childItemModel.setCheckable(False)
                #
                childItemModel.setRefresh()
        #
        childItemModel .setOffset(0)
        parentItemModel.widget().clicked.connect(action)
    #
    def _updateSubName(self):
        count, maxCount = self._viewFilterItemModelIndexCount, self._maxFilterCount
        if count > 0:
            percent = float(count) / float(maxCount)
            r, g, b = uiCore.hsvToRgb(120 * (1 - percent), 1, 1)
            self._uiSubNameText = '{} / {}'.format(count, maxCount)
            self.widget()._uiSubNameColor = r, g, b, 255
        else:
            self._uiSubNameText = None
        #
        self._updateWidgetState()
    #
    def _updateFilterChildrenVisible(self):
        if self._filterChildren:
            [i.setVisible(self.isChecked()) for i in self._filterChildren]
    #
    def _updateFilterColor(self):
        if self._filterViewWidget is not None:
            if self.isColorEnable():
                self._filterViewWidget._viewModel._updateFilterColorBy(
                    self._viewFilterItemModelIndexLis,
                    self.widget()._uiColorBackgroundRgba
                )
    #
    def _updateViewFilterItemModelIndexCount(self):
        self._viewFilterItemModelIndexCount = len(self._viewFilterItemModelIndexLis)
        self._isViewFilterable = self._viewFilterItemModelIndexCount > 0
        #
        self.setColorable(self.isViewFilterable())
        self.setCheckable(self.isViewFilterable())
    #
    def setNameText(self, string):
        self._uiNameText = unicode(string)
        #
        self.widget().setMaximumSize(166667, self._uiFrameHeight)
        self.widget().setMinimumSize(0, self._uiFrameHeight)
        #
        self._updateWidgetState()
    # Override
    def setCheckable(self, boolean):
        self._isCheckable = boolean
        self._isPressable = boolean
        #
        self._updateUiCheckStyle()
        self._updateUiPressStyle()
    # Override
    def setChecked(self, boolean, ignoreAction=False):
        if not boolean == self._isChecked:
            self._isChecked = boolean
            if ignoreAction is False:
                self.widget().clicked.emit()
            #
            self.setRefresh()
            #
            self.widget().toggled.emit(boolean)
            #
            self._updateUiCheckStyle()
    #
    def setCheckedAlone(self):
        if not self._filterChildren:
            filterButtons = [i for i in self.widget().parent().children() if isinstance(i, type(self.widget())) if i._filterChildren == []]
            for i in filterButtons:
                if i == self:
                    i.setChecked(True)
                else:
                    i.setChecked(False)
                #
                i.setRefresh()
    #
    def setOffset(self, value):
        self._uiOffset = value
        #
        self.update()
    #
    def addFilterChild(self, widget):
        self._filterChildren.append(widget)
        itemModel = widget.itemModel()
        self._updateFilterParent(self, itemModel)
    #
    def setMaxFilterCount(self, number):
        self._maxFilterCount = number
        self._updateSubName()
    #
    def _setUiCheckStyle(self, state):
        if state is uiCore.UncheckableState:
            self._uiCheckIcon = uiCore._toLxOsIconFile('svg_basic@svg#filterUncheckable')
            #
            self.widget()._uiNameRgba = 95, 95, 95, 255
            self.widget()._uiFontItalic = True
        else:
            r, g, b, a = 255, 255, 255, 255
            if state is uiCore.CheckedState:
                self._uiCheckIconKeyword = 'svg_basic@svg#filterChecked'
                #
                self.widget()._uiNameRgba = [(r*.75, g*.75, b*.75, a), (r, g, b, a)][self.isCheckHovered()]
            elif state is uiCore.UncheckedState:
                self._uiCheckIconKeyword = 'svg_basic@svg#filterUnchecked'
                #
                self.widget()._uiNameRgba = [(r*.5, g*.5, b*.5, a), (r*.75, g*.75, b*.75, a)][self.isCheckHovered()]
            #
            self._uiCheckIcon = uiCore._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])
            #
            self.widget()._uiFontItalic = False
    #
    def setRefresh(self):
        self._updateViewMultiFilterVisible()
        self._updateFilterColor()
        #
        self._updateSubName()


#
class UiCheckItemModel(uiModelBasic._UiItemModelBasic):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideItemAttr()
    #
    def __overrideItemAttr(self):
        self._isCheckEnable = True
        self._isCheckButton = True
        #
        self._uiCheckIconKeyword = 'svg_basic@svg#filterUnchecked'
        self._uiCheckIcon = uiCore._toLxOsIconFile(self._uiCheckIconKeyword)
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        width -= 1
        height -= 1
        #
        self._uiBasicRect.setRect(
            xPos, yPos,
            width, height
        )
        #
        xOffset, yOffset = [0, 1][self._pressFlag], [0, 1][self._pressFlag]
        # Check
        if self.isCheckEnable() is True:
            self.checkRect().setRect(
                xPos + (self._uiFrameWidth - self._uiIconWidth) / 2 + xOffset, yPos + (self._uiFrameHeight - self._uiIconHeight) / 2 + yOffset,
                self._uiIconWidth - xOffset, self._uiIconHeight - yOffset
            )
            xPos += self._uiFrameWidth + self._uiSpacing
        # Icon
        if self.icon() is not None:
            self.iconRect().setRect(
                xPos + (self._uiFrameWidth - self._uiIconWidth) / 2 + xOffset, yPos + (self._uiFrameHeight - self._uiIconHeight) / 2 + yOffset,
                self._uiIconWidth - xOffset, self._uiIconHeight - yOffset
            )
            xPos += self._uiFrameWidth + self._uiSpacing
        # Name
        if self.nameText() is not None:
            self._uiNameTextRect.setRect(
                xPos + xOffset, yPos + yOffset,
                width - xPos - xOffset, self._uiFrameHeight - yOffset
            )
    #
    def setCheckedAlone(self):
        if self.isCheckable():
            if self.isAutoExclusive():
                childItems = [i for i in self.widget().parent().children() if isinstance(i, type(self.widget())) if i.itemModel() != self]
                #
                self.setChecked(True)
                #
                for i in childItems:
                    if i.isCheckable():
                        i.setChecked(False, ignoreAction=True)
    # Override
    def setCheckable(self, boolean):
        self._isCheckable = boolean
        self._isPressable = boolean
        #
        self._updateUiCheckStyle()
        self._updateUiPressStyle()
    # Override
    def setChecked(self, boolean, ignoreAction=False):
        if not boolean == self._isChecked:
            self._isChecked = boolean
            if ignoreAction is False:
                self.widget().checked.emit()
                #
                self.setCheckedAlone()
            #
            self.widget().toggled.emit(boolean)
            #
            self._updateUiCheckStyle()
    #
    def _setUiCheckStyle(self, state):
        if state is uiCore.UncheckableState:
            self._uiCheckIconKeyword = ['svg_basic@svg#filterUncheckable', 'svg_basic@svg#radioButtonUncheckable'][self._isAutoExclusive]
            self._uiCheckIcon = uiCore._toLxOsIconFile(self._uiCheckIconKeyword)
            #
            self.widget()._uiNameRgba = 95, 95, 95, 255
            self.widget()._uiFontItalic = True
        else:
            r, g, b, a = 255, 255, 255, 255
            if state is uiCore.CheckedState:
                self._uiCheckIconKeyword = ['svg_basic@svg#filterChecked', 'svg_basic@svg#radioButtonChecked'][self._isAutoExclusive]
                #
                self.widget()._uiNameRgba = [(r*.75, g*.75, b*.75, a), (r, g, b, a)][self.isCheckHovered()]
            elif state is uiCore.UncheckedState:
                self._uiCheckIconKeyword = ['svg_basic@svg#filterUnchecked', 'svg_basic@svg#radioButtonUnchecked'][self._isAutoExclusive]
                #
                self.widget()._uiNameRgba = [(r*.5, g*.5, b*.5, a), (r*.75, g*.75, b*.75, a)][self.isCheckHovered()]
            #
            self._uiCheckIcon = uiCore._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])
            #
            self.widget()._uiFontItalic = False


#
class UiEnableItemModel(uiModelBasic._UiItemModelBasic):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideItemAttr()
    #
    def __overrideItemAttr(self):
        self._isCheckEnable = True
        self._isCheckButton = True
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
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
                xPos, yPos,
                self._uiIconWidth, self._uiIconHeight
            )
        # Check
        if self.isCheckEnable() is True:
            self.checkRect().setRect(
                (self._uiFrameWidth - self._uiIconWidth), (self._uiFrameHeight - self._uiIconHeight),
                self._uiIconWidth, self._uiIconHeight
            )
    #
    def setCheckedAlone(self):
        if self.isCheckable():
            if self.isAutoExclusive():
                childItems = [i for i in self.widget().parent().children() if isinstance(i, type(self.widget())) if i.itemModel() != self]
                #
                self.setChecked(True)
                #
                for i in childItems:
                    if i.isCheckable():
                        i.setChecked(False, ignoreAction=True)
    #
    def setChecked(self, boolean, ignoreAction=False):
        if not boolean == self._isChecked:
            self._isChecked = boolean
            if ignoreAction is False:
                self.widget().clicked.emit()
            #
            if ignoreAction is False:
                self.setCheckedAlone()
            #
            self.widget().toggled.emit(boolean)
            #
            self._updateUiCheckStyle()


#
class UiTreeItemModel(uiModelBasic._UiItemModelBasic):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideItemAttr()
    #
    def __overrideItemAttr(self):
        pass


#
class UiGridItemModel(uiModelBasic._UiItemModelBasic):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideItemAttr()
        self.__initUi()
        self.__initVar()
        #
        self.__connectUi(widget)
    #
    def __connectUi(self, widget):
        self._widget = widget
    #
    def __overrideItemAttr(self):
        self._id = None
        self._uiImage = None
        #
        self._uiItemWidth, self._uiItemHeight = 20, 20
        self._uiImageWidth, self._uiImageHeight = 20, 20
        #
        self._uiNameTextWidth, self._uiIndexTextWidth = 32, 32
        #
        self._uiFrameWidth, self._uiFrameHeight = 20, 20
        self._uiIconWidth, self._uiIconHeight = 16, 16
        #
        self._uiCentralWidth, self._uiCentralHeight = 0, 0
        #
        self._uiOffset, self._uiSide, self._uiSpacing, self._uiShadowRadius = 0, 2, 2, 4
        #
        self._uiColorWidth, self._uiColorHeight = 12, 12
    #
    def __initUi(self):
        self._uiBasicRect, self._shadowRect = _rect(), _rect()
        self._titleRect, self._uiCentralRect, self._imageRect = _rect(), _rect(), _rect()
        self._uiExpandRect, self._uiCheckRect, self._uiColorRect = _rect(), _rect(), _rect()
        self._uiIndexTextRect, self._uiNameTextRect, self._uiIconRect = _rect(), _rect(), _rect()
    #
    def __initVar(self):
        pass
    #
    def __initAction(self):
        pass
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        xOffset, yOffset = [0, 1][self._pressFlag], [0, 1][self._pressFlag]
        #
        titleHeight = self._uiFrameHeight
        #
        shadowRadius = [0, self._uiShadowRadius][self._itemMode]
        #
        indexWidth = self._uiIndexTextWidth
        #
        self._uiBasicRect.setRect(
            xPos, yPos,
            width - shadowRadius, height - shadowRadius
        )
        self._shadowRect.setRect(
            xPos + shadowRadius, yPos + titleHeight + shadowRadius,
            width - shadowRadius, height - titleHeight - shadowRadius
        )
        #
        self._titleRect.setRect(
            xPos, yPos,
            width - shadowRadius - 1, titleHeight
        )
        self._uiCentralRect.setRect(
            xPos, yPos + titleHeight,
            width - shadowRadius - 1, height - titleHeight - shadowRadius - 1
        )
        self._imageRect.setRect(
            xPos + 1, yPos + titleHeight + 1,
            width - shadowRadius - 2, height - titleHeight - shadowRadius - 2
        )
        #
        xPos += self._uiSide
        # Check Box
        if self._isCheckEnable is True:
            self._uiCheckRect.setRect(
                xPos + (self._uiFrameWidth - self._uiIconWidth)/2 + xOffset, yPos + (self._uiFrameHeight - self._uiIconHeight)/2 + yOffset,
                self._uiIconWidth - xOffset, self._uiIconHeight - yOffset
            )
            xPos += self._uiFrameWidth + self._uiSpacing
        # Color
        if self._isColorEnable is True:
            self._uiColorRect.setRect(
                xPos + (self._uiFrameWidth - self._uiColorWidth)/2, yPos + (self._uiFrameHeight - self._uiColorHeight)/2,
                self._uiColorWidth, self._uiColorHeight
            )
            xPos += self._uiFrameWidth + self._uiSpacing
        # Icon
        if self._uiIcon is not None:
            self._uiIconRect.setRect(
                xPos + (self._uiFrameWidth - self._uiIconWidth)/2, yPos + (self._uiFrameHeight - self._uiIconHeight)/2,
                self._uiIconWidth, self._uiIconHeight
            )
            xPos += self._uiFrameWidth + self._uiSpacing
        # Name
        if self.nameText() is not None:
            self._uiNameTextRect.setRect(
                xPos, yPos,
                width - xPos - indexWidth, self._uiFrameHeight
            )
        # Index
        if self._uiIndexText is not None:
            self._uiIndexTextRect.setRect(
                width - indexWidth - shadowRadius - self._uiSide, yPos,
                indexWidth, self._uiFrameHeight
            )
    #
    def _updateGeometry(self):
        self._updateRectGeometry()
    #
    def update(self):
        self._updateGeometry()
        self._updateWidgetState()
    #
    def setId(self, string):
        self._id = string
    #
    def setImage(self, image):
        self._uiImage = image
    #
    def setItemMode(self, itemMode):
        self._itemMode = itemMode
        #
        self.update()
    #
    def id(self):
        return self._id
    #
    def setFilterStatus(self, state):
        if state.lower() == 'warning':
            self._setUiPressStatus(uiCore.WarningStatus)
        elif state.lower() == 'error':
            self._setUiPressStatus(uiCore.ErrorStatus)
        elif state.lower() == 'on':
            self._setUiPressStatus(uiCore.OnStatus)
        else:
            self._setUiPressStatus(uiCore.NormalStatus)


#
class UiPresetItemModel(uiModelBasic._UiItemModelBasic):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideItem()
    #
    def __overrideItem(self):
        self.__overrideItemAttr()
        self.__overrideItemUi()
    #
    def __overrideItemAttr(self):
        self.setExpandButton(True)
    #
    def __overrideItemUi(self):
        self._uiCheckIconKeyword = 'svg_basic@svg#boxUnchecked'
        self._uiCheckIcon = uiCore._toLxOsIconFile(self._uiCheckIconKeyword)
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        width -= 1
        height -= 1
        #
        messageWidth = self.widget()._messageWidth
        describeWidth = self.widget()._describeWidth
        #
        describeLabel = self.widget()._descriptionLabel
        #
        if self.itemLevel() == 0:
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
                    xPos + (self._uiFrameWidth - iconWidth) / 2, yPos + (self._uiFrameHeight - iconHeight) / 2,
                    iconWidth, iconHeight
                )
                xPos += self._uiFrameWidth + self._uiSpacing
            # Color
            if self.isColorEnable():
                self._uiColorRect.setRect(
                    xPos + (self._uiFrameWidth - self._uiColorWidth) / 2, yPos + (self._uiFrameHeight - self._uiColorHeight) / 2,
                    self._uiColorWidth, self._uiColorHeight
                )
                xPos += self._uiFrameWidth + self._uiSpacing
            # Expand
            if self.isExpandEnable():
                # Tree Item Offset
                xPos += self._uiExpandFrameWidth * self.itemLevel()
                #
                self.expandRect().setRect(
                    xPos + (self._uiFrameWidth - self._uiIconWidth) / 2, yPos + (self._uiFrameHeight - self._uiIconHeight) / 2,
                    self._uiIconWidth, self._uiIconHeight
                )
                self.expandPressRect().setRect(
                    xPos, yPos,
                    width - xPos, height
                )
                xPos += self._uiFrameWidth + self._uiSpacing
            # Index
            if self.indexText() is not None:
                self._uiIndexTextRect.setRect(
                    xPos, yPos,
                    self._uiIndexTextWidth, self._uiFrameHeight
                )
                xPos += self._uiIndexTextWidth + self._uiSpacing
            # Icon and Sub Icon
            if self.icon() is not None:
                self.iconRect().setRect(
                    xPos + (self._uiFrameWidth - self._uiIconWidth) / 2,
                    yPos + (self._uiFrameHeight - self._uiIconHeight) / 2,
                    self._uiIconWidth, self._uiIconHeight
                )
                if self.extendIcon() is not None:
                    self.extendIconRect().setRect(
                        xPos + (self._uiExtendFrameWidth - self._uiExtendIconWidth) / 2,
                        yPos + (self._uiExtendFrameHeight - self._uiExtendIconHeight) / 2,
                        self._uiExtendIconWidth, self._uiExtendIconHeight
                    )
                #
                xPos += self._uiFrameWidth + self._uiSpacing
            # Name
            if self.nameText() is not None:
                self._uiNameTextRect.setRect(
                    xPos, yPos,
                    width - xPos, self._uiFrameHeight
                )
            # SubName
            if self.uiSubName() is not None:
                self._uiSubNameRect.setRect(
                    xPos, yPos,
                    width - xPos, self._uiFrameHeight
                )
            #
            xPos = max(messageWidth, width - describeWidth)
            describeLabel.setGeometry(
                xPos, yPos,
                width - xPos, height + 1
            )
        else:
            self.widget()._descriptionLabel.hide()
    #
    def _setUiPressStyle(self, state):
        if state is uiCore.UnpressableState:
            self.widget()._uiBackgroundRgba = 0, 0, 0, 0
            self.widget()._uiBorderRgba = 0, 0, 0, 0
            #
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            self.widget()._uiBackgroundRgba = [(0, 0, 0, 0), (80, 80, 80, 255)][self.isPressHovered()]
            self.widget()._uiBorderRgba = [(0, 0, 0, 0), (80, 80, 80, 255)][self.isPressHovered()]
            #
            self.widget()._uiNameRgba = [(191, 191, 191, 255), (223, 223, 223, 255)][self.isPressHovered()]
            #
            self.widget()._uiFontItalic = False
    #
    def _setUiCheckStyle(self, state):
        if state is uiCore.UncheckableState:
            self._uiCheckIcon = uiCore._toLxOsIconFile('svg_basic@svg#lock')
        else:
            if state is uiCore.CheckedState:
                self._uiCheckIconKeyword = ['svg_basic@svg#boxChecked', 'svg_basic@svg#radioChecked'][self.isAutoExclusive()]
                #
                self.widget()._uiNameRgba = 191, 191, 191, 255
                self.widget()._uiFontItalic = False
            elif state is uiCore.UncheckedState:
                self._uiCheckIconKeyword = ['svg_basic@svg#boxUnchecked', 'svg_basic@svg#radioUnchecked'][self.isAutoExclusive()]
                #
                self.widget()._uiNameRgba = 127, 127, 127, 255
                self.widget()._uiFontItalic = True
            #
            self._uiCheckIcon = uiCore._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])
    #
    def addChild(self, widget):
        self.setExpandEnable(True)
        self.viewModel().setExpandEnable(True)
        #
        widget.setParent(self.viewModelViewport())
        #
        itemModel = self
        itemIndex = self.viewModel().itemModelIndex(itemModel)
        #
        childItemIndex = self.viewModel().itemIndexCount()
        #
        childItemModel = widget.itemModel()
        #
        childItemModel.setViewModel(self.viewModel())
        childItemModel.setParentItemModel(itemModel)
        #
        childItemModel.setIndex(childItemIndex)
        childItemModel.setItemSize(*self.viewModel().itemSize())
        #
        childItemModel.setEventOverrideEnable(True)
        # Item Model
        self.viewModel()._addItemModel(childItemModel)
        # Level
        childItemExtendLevel = self.itemLevel() + 1
        self.viewModel()._updateItemModelLevelFor(childItemExtendLevel, childItemIndex)
        self.viewModel()._updateItemModelLevelIndexFor(childItemExtendLevel, childItemIndex)
        # Sub Index
        self.viewModel()._addSubItemModelIndexAt(itemIndex, childItemIndex)
        self.viewModel()._addSubVisibleItemModelIndexAt(itemIndex, childItemIndex)
        # Sub Sort
        self.viewModel()._addSubItemModelIndexSortAt(itemIndex, childItemIndex)


#
class UiRecordItemModel(uiModelBasic._UiItemModelBasic):
    def __init__(self, widget):
        self._initItemModelBasic(widget)
        #
        self.__overrideItem()
    #
    def __overrideItem(self):
        self.__overrideItemAttr()
        self.__overrideItemUi()
    #
    def __overrideItemAttr(self):
        pass
    #
    def __overrideItemUi(self):
        self._uiFrameWidth, self._uiFrameHeight = 32, 32
        self._uiIconWidth, self._uiIconHeight = 24, 24
    #
    def _updateRectGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        width -= 1
        height -= 1
        #
        self._uiBasicRect.setRect(
            xPos, yPos,
            width, height
        )
        #
        xPos += self._uiSide
        # Color
        if self.isColorEnable():
            self._updateColorRect(xPos, yPos)
            xPos += self._uiFrameWidth + self._uiSpacing
        # Expand
        if self.isExpandEnable():
            # Tree Item Offset
            self._updateExpandRect(xPos, yPos, width, height)
            xPos += self._uiFrameWidth + self._uiSpacing
        # Icon and Sub Icon
        if self.icon() is not None or self.iconText() is not None:
            self._updateIconRect(xPos, yPos)
            #
            xPos += self._uiFrameWidth + self._uiSpacing
        # Name
        if self.nameText() is not None:
            self._updateNameTextRect(xPos, yPos, width, height)
