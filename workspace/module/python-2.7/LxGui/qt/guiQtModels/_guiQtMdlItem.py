# coding:utf-8
from LxGui.qt import qtCore, guiQtMdlAbs
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
CLS_point = QtCore.QPoint
CLS_line = QtCore.QLine
CLS_rect = QtCore.QRect


#
class QtFilterCheckviewItemModel(guiQtMdlAbs.Abs_GuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
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
        self._uiCheckIconKeyword = 'svg_basic/boxUnchecked'
        self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
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
            r, g, b = qtCore.hsv2rgb(120 * (1 - percent), 1, 1)
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
                    self.widget()._wgt__color__background_rgba
                )
    #
    def _updateViewFilterItemModelIndexCount(self):
        self._viewFilterItemModelIndexCount = len(self._viewFilterItemModelIndexLis)
        self._isViewFilterable = self._viewFilterItemModelIndexCount > 0
        #
        self.setColorable(self.isViewFilterable())
        self.setCheckable(self.isViewFilterable())
    #
    def setNameString(self, string):
        self._gui_qt__mdl__name_str_ = unicode(string)
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
        self._updateQtCheckStyle()
        self._gui_qt__set_press_style_update_()
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
            self._updateQtCheckStyle()
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
    def _setQtCheckStyle(self, state):
        if state is qtCore.UncheckableState:
            self._uiCheckIcon = qtCore._toLxOsIconFile('svg_basic/filteruncheckable')
            #
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
            self.widget()._uiFontItalic = True
        else:
            r, g, b, a = 255, 255, 255, 255
            if state is qtCore.CheckedState:
                self._uiCheckIconKeyword = 'svg_basic/filterchecked'
                #
                self.widget()._wgt__name_rgba = [(r*.75, g*.75, b*.75, a), (r, g, b, a)][self.isCheckHovered()]
            elif state is qtCore.UncheckedState:
                self._uiCheckIconKeyword = 'svg_basic/filterunchecked'
                #
                self.widget()._wgt__name_rgba = [(r*.5, g*.5, b*.5, a), (r*.75, g*.75, b*.75, a)][self.isCheckHovered()]
            #
            self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])
            #
            self.widget()._uiFontItalic = False
    #
    def setRefresh(self):
        self._updateViewMultiFilterVisible()
        self._updateFilterColor()
        #
        self._updateSubName()


#
class QtGridViewitemModel(guiQtMdlAbs.Abs_GuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
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
        self._gui_qt__mdl__name_str_Width, self._gui_qt__mdl__index_str_Width = 32, 32
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
        self._uiBasicRect, self._shadowRect = CLS_rect(), CLS_rect()
        self._titleRect, self._uiCentralRect, self._imageRect = CLS_rect(), CLS_rect(), CLS_rect()
        self._uiExpandRect, self._uiCheckRect, self._uiColorRect = CLS_rect(), CLS_rect(), CLS_rect()
        self._gui_qt__mdl__index_str_Rect, self._gui_qt__mdl__name_str_Rect, self._uiIconRect = CLS_rect(), CLS_rect(), CLS_rect()
    #
    def __initVar(self):
        pass
    #
    def __initAction(self):
        pass
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        xOffset, yOffset = [0, 1][self._pressFlag], [0, 1][self._pressFlag]
        #
        titleHeight = self._uiFrameHeight
        #
        shadowRadius = [0, self._uiShadowRadius][self._itemMode]
        #
        indexWidth = self._gui_qt__mdl__index_str_Width
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
            self._gui_qt__mdl__name_str_Rect.setRect(
                xPos, yPos,
                width - xPos - indexWidth, self._uiFrameHeight
            )
        # Index
        if self._gui_qt__mdl__index_str_ is not None:
            self._gui_qt__mdl__index_str_Rect.setRect(
                width - indexWidth - shadowRadius - self._uiSide, yPos,
                indexWidth, self._uiFrameHeight
            )
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._gui_qt__mdl__set_rect_geometry_update_()
    #
    def update(self):
        self._gui_qt__mdl__set_geometry_update_()
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
            self._setQtPressStatus(qtCore.WarningStatus)
        elif state.lower() == 'error':
            self._setQtPressStatus(qtCore.ErrorStatus)
        elif state.lower() == 'on':
            self._setQtPressStatus(qtCore.OnStatus)
        else:
            self._setQtPressStatus(qtCore.NormalStatus)


#
class QtPresetviewItemModel(guiQtMdlAbs.Abs_GuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
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
        self._uiCheckIconKeyword = 'svg_basic/boxunchecked'
        self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
                self._gui_qt__mdl__index_str_Rect.setRect(
                    xPos, yPos,
                    self._gui_qt__mdl__index_str_Width, self._uiFrameHeight
                )
                xPos += self._gui_qt__mdl__index_str_Width + self._uiSpacing
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
                self._gui_qt__mdl__name_str_Rect.setRect(
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
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            self.widget()._wgt__background_rgba = 0, 0, 0, 0
            self.widget()._wgt__border_rgba = 0, 0, 0, 0
            #
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            self.widget()._wgt__background_rgba = [(0, 0, 0, 0), (80, 80, 80, 255)][self.isPressHovered()]
            self.widget()._wgt__border_rgba = [(0, 0, 0, 0), (80, 80, 80, 255)][self.isPressHovered()]
            #
            self.widget()._wgt__name_rgba = [(191, 191, 191, 255), (223, 223, 223, 255)][self.isPressHovered()]
            #
            self.widget()._uiFontItalic = False
    #
    def _setQtCheckStyle(self, state):
        if state is qtCore.UncheckableState:
            self._uiCheckIcon = qtCore._toLxOsIconFile('svg_basic/lock')
        else:
            if state is qtCore.CheckedState:
                self._uiCheckIconKeyword = ['svg_basic/boxchecked', 'svg_basic/radiochecked'][self.isAutoExclusive()]
                #
                self.widget()._wgt__name_rgba = 191, 191, 191, 255
                self.widget()._uiFontItalic = False
            elif state is qtCore.UncheckedState:
                self._uiCheckIconKeyword = ['svg_basic/boxunchecked', 'svg_basic/radiounchecked'][self.isAutoExclusive()]
                #
                self.widget()._wgt__name_rgba = 127, 127, 127, 255
                self.widget()._uiFontItalic = True
            #
            self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])
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
class QtRecordviewItemItemModel(guiQtMdlAbs.Abs_GuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
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
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
            self._gui_qt__mdl__set_color_rect_update_(xPos, yPos)
            xPos += self._uiFrameWidth + self._uiSpacing
        # Expand
        if self.isExpandEnable():
            # Tree Item Offset
            self._updateExpandRect(xPos, yPos, width, height)
            xPos += self._uiFrameWidth + self._uiSpacing
        # Icon and Sub Icon
        if self.icon() is not None or self.iconText() is not None:
            self._gui_qt__mdl__set_icon_rect_update_(xPos, yPos)
            #
            xPos += self._uiFrameWidth + self._uiSpacing
        # Name
        if self.nameText() is not None:
            self._updateNameTextRect(xPos, yPos, width, height)


class QtTreeItemModel(guiQtMdlAbs.Abs_GuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)


class QtValueLineModel(guiQtMdlAbs.Abs_GuiQtValueLineMdl):
    def __init__(self, *args):
        self._initAbsGuiQtValueLineMdl(*args)


class QtPressbuttonModel(guiQtMdlAbs.Abs_GuiQtPressbuttonMdl):
    def __init__(self, *args):
        self._initAbsGuiQtPressbuttonMdl(*args)
