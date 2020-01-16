# coding:utf-8
from LxUi.qt import qtCore, qtDefinition, qtAction

#
QtCore = qtCore.QtCore
#
none = ''


# Item
class QtAbc_ItemModel(qtDefinition.QtDef_ItemModel):
    def _initAbcItemModel(self):
        self._initItemModelDef()
        #
        self._initAbcItemModelAttr()
        self._initAbcItemModelAction()
        self._initAbcItemModelRect()
        self._initAbcItemModelUi()
        self._initAbcItemModelVar()
    #
    def _initAbcItemModelAttr(self):
        self._itemMode = qtCore.ListMode
        #
        self._proxyItem = None
        #
        self._isPressButton = False
        self._isPressEnable = True
        self._isPressHovered = False
        #
        self._isExtendPressHovered = False
        self._isPressable = True
        self._isPressed = False
        self._isPressCurrent = False
        self._isPressStarted = False
        self._isDragPressStarted = False
        #
        self._isSelectEnable = False
        self._isSelectable = True
        self._isSelected = False
        self._isSubSelected = False
        self._isSelectExclusive = False
        #
        self._pressAction = None
        self._pressCommand = None
        #
        self._extendPressAction = None
        self._extendPressCommand = None
        #
        self._isPercentEnable = False
        self._isPercentable = False
    #
    def _initAbcItemModelAction(self):
        pass
    #
    def _initAbcItemModelRect(self):
        self._uiPercentFrameRect = QtCore.QRect(-20, -20, 1, 1)
        self._uiPercentValueRect = QtCore.QRect(-20, -20, 1, 1)
        self._uiPercentTextRect = QtCore.QRect(-20, -20, 1, 1)
        #
        self._uiExtendIconRect = QtCore.QRect(-20, -20, 1, 1)
        self._uiSubNameRect = QtCore.QRect(-20, -20, 1, 1)
        #
        self._pressRect = QtCore.QRect(-20, -20, 1, 1)
    #
    def _initAbcItemModelUi(self):
        self._uiSubNameText = None
        #
        self._uiPercentText = 'N/a'
        #
        self._uiTextAlignment = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        #
        self._uiExtendIconKeyword = None
        self._uiExtendIcon = None
        #
        self._uiCheckIconWidth, self._uiCheckIconHeight = 16.0, 16.0
        #
        self._uiScale = 1.0
        self._uiItemXPos, self._uiItemYPos = 0, 0
        #
        self._uiOffset, self._uiSide, self._uiSpacing, self._uiShadowRadius = 0, 2.0, 2.0, 0
        #
        self._uiBasicWidth, self._uiBasicHeight = 20.0, 20.0
        self._uiWidth, self._uiHeight = 20.0, 20.0
        #
        self._uiWidthRecord, self._uiHeightRecord = 0, 0
        #
        self._uiBasicFrameWidth, self._uiBasicFrameHeight = 20.0, 20.0
        self._uiExtendFrameWidth, self._uiExtendFrameHeight = 10.0, 10.0
        #
        self._uiExtendIconWidth, self._uiExtendIconHeight = 8.0, 8.0
        #
        self._uiBasicConnectionWidth, self._uiBasicConnectionHeight = 12.0, 12.0
        self._uiConnectionWidth, self._uiConnectionHeight = 12.0, 12.0
        #
        self._uiBasicWidthRound, self._uiBasicHeightRound = 10.0, 10.0
        self._uiWidthRound, self._uiHeightRound = 2.0, 2.0
        #
        self._uiIndexTextWidth, self._uiNameTextWidth, self._uiSubNameWidth = 32.0, 32.0, 32.0
    #
    def _initAbcItemModelVar(self):
        # Keyword
        self._isKeywordFilterable = False
        self._isKeywordFilterVisible = True
        self._filterKeyword = None
        # Multi
        self._isMultiFilterVisible = True
        self._multiFilterDic = {}
        # Extend
        self._isExtendFilterVisible = False
        #
        self._parentItemModel = None
        #
        self._valueMaximum = 0
        self._value = 0
        self._valuePercent = 0.0
    #
    def _visibleIndexAt(self, childItemIndex):
        if childItemIndex in self.visibleChildItemIndexes():
            return self.visibleChildItemIndexes().index(childItemIndex)
        else:
            return -1
    #
    def _isLastVisibleIndexAt(self, childItemIndex):
        visibleIndex = self._visibleIndexAt(childItemIndex)
        if not visibleIndex == -1:
            return visibleIndex == self.visibleChildItemIndexCount() - 1
        else:
            return False
    #
    def _updateKeywordFilterVisible(self):
        var = self.filterKeyword()
        if self.nameText() is not None and var is not None:
            filterString = self.nameText()
            #
            self._isKeywordFilterable = True
            #
            if var.lower() in filterString.lower():
                boolean = True
            else:
                boolean = False
        else:
            self._isKeywordFilterable = False
            #
            boolean = True
        #
        self.setKeywordFilterVisible(boolean)
    #
    def _updateMultiFilterVisible(self):
        boolean = True
        if self._multiFilterDic:
            for i in self._multiFilterDic.values():
                b = sum(i.values()) > 0
                if b is False:
                    boolean = False
                    break
        #
        self.setMultiFilterVisible(boolean)
    #
    def _updateVisible(self):
        if self.isExtendFilterVisible():
            boolean = self.isExpandVisible()
        else:
            boolean = self.isExpandVisible() and self.isFilterVisible()
        #
        self.setVisible(boolean)
        #
        self.widget().visibleToggled.emit(boolean)
    #
    def _expandClickAction(self):
        def setVisibleBranch(itemModel, boolean):
            itemIndex = self.viewModel().itemModelIndex(itemModel)
            visibleChildItemIndexes = itemModel.visibleChildItemIndexes()
            if visibleChildItemIndexes:
                if boolean is True:
                    if itemModel.isExpanded() is True:
                        self.viewModel()._addExtendVisibleItemModelIndexesAt(itemIndex, visibleChildItemIndexes)
                        for childItemIndex in visibleChildItemIndexes:
                            childItemModel = self.viewModel().itemModelAt(childItemIndex)
                            setVisibleBranch(childItemModel, boolean)
                else:
                    self.viewModel()._subExtendVisibleItemModelIndexesAt(itemIndex, visibleChildItemIndexes)
                    for childItemIndex in visibleChildItemIndexes:
                        childItemModel = self.viewModel().itemModelAt(childItemIndex)
                        setVisibleBranch(childItemModel, boolean)
        #
        if self.visibleChildItemIndexCount() > 0:
            setVisibleBranch(self, self.isExpanded())
            #
            self.viewModel().update()
    #
    def _updateByExtendExpandAction(self):
        def setVisibleBranch(itemModel, boolean):
            itemIndex = self.viewModel().itemModelIndex(itemModel)
            visibleChildItemIndexes = itemModel.visibleChildItemIndexes()
            if visibleChildItemIndexes:
                if boolean is True:
                    self.viewModel()._addExtendVisibleItemModelIndexesAt(itemIndex, visibleChildItemIndexes)
                    for childItemIndex in visibleChildItemIndexes:
                        childItemModel = self.viewModel().itemModelAt(childItemIndex)
                        childItemModel.setExpanded(boolean, ignoreAction=True)
                        setVisibleBranch(childItemModel, boolean)
                else:
                    self.viewModel()._subExtendVisibleItemModelIndexesAt(itemIndex, visibleChildItemIndexes)
                    for childItemIndex in visibleChildItemIndexes:
                        childItemModel = self.viewModel().itemModelAt(childItemIndex)
                        childItemModel.setExpanded(boolean, ignoreAction=True)
                        setVisibleBranch(childItemModel, boolean)
        #
        if self.visibleChildItemIndexCount() > 0:
            setVisibleBranch(self, self.isExpanded())
            #
            self.viewModel().update()
    #
    def _expandClickSwitchAction(self, isExtend=False):
        if self.isExpandable():
            if isExtend is True:
                self.setExtendExpanded(not self._isExpanded)
            else:
                self.setExpanded(not self._isExpanded)
    # For Override
    def _extendPressCurrentAction(self):
        pass
    # For Override
    def _extendPressSelectAction(self):
        pass
    #
    def _updateQtPressStatus(self):
        if self.isPercentEnable():
            pass
        else:
            status = self._uiPressStatus
            if status is qtCore.OffStatus:
                self._widget._uiNameRgba = 95, 95, 95, 255
            else:
                if status is qtCore.ErrorStatus:
                    r, g, b = 255, 0, 64
                elif status is qtCore.WarningStatus:
                    r, g, b = 255, 255, 64
                elif status is qtCore.OnStatus:
                    r, g, b = 64, 255, 127
                else:
                    r, g, b = 255, 255, 255
                #
                self._widget._uiNameRgba = [(r * .75, g * .75, b * .75, 255), (r, g, b, 255)][self.isPressHovered()]
    #
    def _updateQtPressStyle(self):
        if self.isPressEnable():
            if self.isPressable():
                if self.isSelectEnable():
                    if self.isSelectable():
                        if self.isSelected():
                            self._setQtPressStyle(qtCore.SelectedState)
                        else:
                            self._setQtPressStyle([qtCore.UnselectedState, qtCore.SubSelectedState][self.isSubSelected()])
                    else:
                        self._setQtPressStyle(qtCore.UnpressableState)
                else:
                    if self.isPressCurrent():
                        self._setQtPressStyle(qtCore.CurrentState)
                    else:
                        self._setQtPressStyle(qtCore.NormalState)
            else:
                self._setQtPressStyle(qtCore.UnpressableState)
        #
        self._updateWidgetState()
    #
    def _updateRectGeometry(self):
        pass
    #
    def viewModelViewport(self):
        return self.viewModel().viewport()
    #
    def setWidget(self, widget):
        self._widget = widget
    #
    def setTextAlignment(self, args):
        self._uiTextAlignment = args
    #
    def setExtendIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self._uiExtendIconKeyword = iconKeyword
        #
        if self._uiExpandIconKeyword is not None:
            self._uiExtendIcon = self._toLxOsIconFile(self._uiExtendIconKeyword)
        else:
            self._uiExpandIcon = None
        #
        self.setExtendFrameSize(frameWidth, frameHeight)
        self.setExtendIconSize(iconWidth, iconHeight)
        #
        self._updateWidgetState()
    #
    def extendIcon(self):
        return self._uiExtendIcon
    #
    def setUiSubName(self, string):
        if string is not None:
            self._uiSubNameText = unicode(string)
        #
        self._updateWidgetState()
    #
    def uiSubName(self):
        return self._uiSubNameText
    #
    def setItemMode(self, itemMode):
        self._itemMode = itemMode
        self._updateWidgetState()
    #
    def itemModel(self):
        return self._itemMode
    #
    def setUiScale(self, value):
        self._uiScale = value
    #
    def uiScale(self):
        return self._uiScale
    #
    def setFilterKeyword(self, string):
        self._filterKeyword = string
        #
        self._updateKeywordFilterVisible()
        #
        self._updateWidgetState()
    #
    def isKeywordFilterable(self):
        return self._isKeywordFilterable
    #
    def setKeywordFilterVisible(self, boolean):
        if not boolean == self._isKeywordFilterVisible:
            self._isKeywordFilterVisible = boolean
        #
        self._updateVisible()
    #
    def isKeywordFilterVisible(self):
        if self.isKeywordFilterable():
            return self._isKeywordFilterVisible
        else:
            return True
    #
    def setMultiFilterDic(self, itemFilterColumn, itemFilterRow, boolean):
        if not itemFilterColumn in self._multiFilterDic:
            self._multiFilterDic[itemFilterColumn] = {}
        self._multiFilterDic[itemFilterColumn][itemFilterRow] = boolean
        #
        self._updateMultiFilterVisible()
    #
    def setMultiFilterVisible(self, boolean):
        if not boolean == self._isMultiFilterVisible:
            self._isMultiFilterVisible = boolean
        #
        self._updateVisible()
    #
    def isMultiFilterVisible(self):
        return self._isMultiFilterVisible
    #
    def isFilterVisible(self):
        return self.isKeywordFilterVisible() and self.isMultiFilterVisible()
    #
    def setExtendFilterVisible(self, boolean):
        if not boolean == self._isExtendFilterVisible:
            self._isExtendFilterVisible = boolean
        #
        self._updateVisible()
    #
    def isExtendFilterVisible(self):
        return self._isExtendFilterVisible
    #
    def isExpandVisible(self):
        parentItemModels = self.parentItemModels()
        boolean = True
        if parentItemModels:
            for itemModel in parentItemModels:
                if not itemModel.isExpanded():
                    boolean = False
                    break
        return boolean
    #
    def setExtendFrameSize(self, w, h):
        self._uiExtendFrameWidth, self._uiExtendFrameHeight = w, h
    #
    def extendFrameSize(self):
        return self._uiExtendFrameWidth, self._uiExtendFrameHeight
    #
    def setExtendIconSize(self, w, h):
        self._uiExtendIconWidth, self._uiExtendIconHeight = w, h
    #
    def extendIconSize(self):
        return self._uiExtendIconWidth, self._uiExtendIconHeight
    #
    def setProxyItem(self, item):
        self._proxyItem = item
    #
    def proxyItem(self):
        return self._proxyItem
    #
    def setParentItemModel(self, itemModel):
        self._parentItemModel = itemModel
    #
    def parentItemModel(self):
        return self._parentItemModel
    #
    def parentItem(self):
        if self.parentItemModel():
            return self.parentItemModel().widget()
    #
    def parentItemModels(self):
        def getBranch(itemModel):
            parentItemModel = itemModel.parentItemModel()
            if parentItemModel is not None:
                if not parentItemModel in lis:
                    lis.append(parentItemModel)
                #
                getBranch(parentItemModel)
        #
        lis = []
        #
        getBranch(self)
        return lis
    #
    def parentItems(self):
        return [i.widget() for i in self.parentItemModels()]
    #
    def hasParent(self):
        return self.parentItemModel() is not None
    #
    def childItemIndexes(self):
        if self.viewModel() is not None:
            itemIndex = self.viewModel().itemModelIndex(self)
            return self.viewModel().childItemIndexesAt(itemIndex)
        else:
            return []
    #
    def allChildItemIndexes(self):
        def getBranch(itemIndex):
            childItemIndexes = self.viewModel().childItemIndexesAt(itemIndex)
            if childItemIndexes:
                for childItemIndex in childItemIndexes:
                    lis.append(childItemIndex)
                    #
                    getBranch(childItemIndex)
        #
        lis = []
        if self.viewModel() is not None:
            getBranch(self.viewModel().itemModelIndex(self))
        return lis
    #
    def childItemIndexCount(self):
        if self.viewModel() is not None:
            itemIndex = self.viewModel().itemModelIndex(self)
            return self.viewModel().childItemIndexCountAt(itemIndex)
        else:
            return 0
    #
    def allChildItemIndexCount(self):
        return len(self.allChildItemIndexes())
    #
    def childItemModels(self):
        return self.viewModel().itemModelsIn(self.childItemIndexes())
    #
    def childItemNames(self):
        return [i.name() for i in self.childItemModels()]
    #
    def childItems(self):
        return self.viewModel().itemsIn(self.childItemIndexes())
    #
    def allChildItemModels(self):
        return self.viewModel().itemModelsIn(self.allChildItemIndexes())
    #
    def visibleChildItemIndexes(self):
        if self.viewModel() is not None:
            parentIndex = self.viewModel().itemModelIndex(self)
            return self.viewModel().visibleChildItemIndexesAt(parentIndex)
        else:
            return []
    #
    def visibleChildItemIndexCount(self):
        if self.viewModel() is not None:
            parentIndex = self.viewModel().itemModelIndex(self)
            return self.viewModel().visibleChildItemIndexCountAt(parentIndex)
        else:
            return 0
    #
    def allVisibleChildItemIndexCount(self):
        pass
    #
    def visibleChildItemModels(self):
        lis = []
        childItemIndexes = self.visibleChildItemIndexes()
        if childItemIndexes:
            for childItemIndex in childItemIndexes:
                itemModel = self.viewModel().itemModelAt(childItemIndex)
                lis.append(itemModel)
        return lis
    #
    def allVisibleChildItemModels(self):
        pass
    #
    def hasChildren(self):
        return self.childItemIndexCount() > 0
    #
    def hasVisibleChildren(self):
        return self.visibleChildItemIndexCount() > 0
    #
    def hasKeywordFilterVisibleChildren(self):
        boolean = False
        itemIndexLis = self.allChildItemIndexes()
        if itemIndexLis:
            for childItemIndex in itemIndexLis:
                itemModel = self.viewModel().itemModelAt(childItemIndex)
                if itemModel.isKeywordFilterVisible():
                    return True
        return boolean
    #
    def hasSelectedChildren(self):
        boolean = False
        itemIndexLis = self.allChildItemIndexes()
        if itemIndexLis:
            for childItemIndex in itemIndexLis:
                itemModel = self.viewModel().itemModelAt(childItemIndex)
                if itemModel.isSelected():
                    boolean = True
                    break
        return boolean
    #
    def childItemVisibleIndex(self, childItemModel):
        if childItemModel in self.visibleChildItemModels():
            return self.visibleChildItemModels().index(childItemModel)
        else:
            return -1
    #
    def isChildLastVisibleIndex(self, childItemModel):
        extendVisibleIndex = self.childItemVisibleIndex(childItemModel)
        return extendVisibleIndex == self.visibleChildItemIndexCount() - 1
    #
    def extendVisibleIndex(self):
        parentItemModel = self.parentItemModel()
        if parentItemModel is not None:
            childItemIndex = self.viewModel().itemModelIndex(self)
            return parentItemModel._visibleIndexAt(childItemIndex)
        else:
            return -1
    #
    def isLastVisibleChildIndex(self):
        parentItemModel = self.parentItemModel()
        if parentItemModel is not None:
            childItemIndex = self.viewModel().itemModelIndex(self)
            return parentItemModel._isLastVisibleIndexAt(childItemIndex)
        else:
            return False
    #
    def isParentLastVisibleChildIndexFor(self, level):
        parentItemModels = self.parentItemModels()
        itemModel = parentItemModels[level]
        return itemModel.isLastVisibleChildIndex()
    #
    def preExtendVisibleItemModelIndex(self):
        pass
    #
    def itemLevel(self):
        itemIndex = self.viewModel().itemModelIndex(self)
        return self.viewModel().itemLevelAt(itemIndex)
    #
    def isExtendExpandHovered(self):
        boolean = False
        #
        isExpandHovered = self.isExpandHovered()
        #
        if isExpandHovered is True:
            boolean = True
        else:
            parentItemModels = self.parentItemModels()
            if parentItemModels:
                for itemModel in parentItemModels:
                    if itemModel.isExpandHovered() is True:
                        boolean = True
                        break
        return boolean
    #
    def isParentExtendExpanded(self):
        boolean = True
        parentItemModels = self.parentItemModels()
        if parentItemModels:
            for itemModel in parentItemModels:
                if not itemModel.isExpanded():
                    boolean = False
                    break
        return boolean
    #
    def isParentExtendExpandHovered(self):
        boolean = False
        parentItemModels = self.parentItemModels()
        if parentItemModels:
            for itemModel in parentItemModels:
                if itemModel.isExpandHovered() is True:
                    boolean = True
                    break
        return boolean
    #
    def isParentExpandHoveredAt(self, level):
        def getHoveredLevel():
            value = None
            for l in range(levelCount):
                itemModel = parentItemModels[l]
                if itemModel.isExpandHovered() is True:
                    value = l
                    break
            return value
        #
        boolean = False
        parentItemModels = self.parentItemModels()
        if parentItemModels:
            levelCount = len(parentItemModels)
            #
            expandHoveredLevel = getHoveredLevel()
            if expandHoveredLevel is not None:
                if level <= expandHoveredLevel:
                    boolean = True
        return boolean
    #
    def setExpanded(self, boolean, ignoreAction=False):
        if not boolean == self._isExpanded:
            self._isExpanded = boolean
            #
            if ignoreAction is False:
                self._expandClickAction()
        #
        self._updateQtExpandStyle()
    #
    def setExtendExpanded(self, boolean, ignoreAction=False):
        self._isExpanded = boolean
        if ignoreAction is False:
            self._updateByExtendExpandAction()
        #
        self._updateQtExpandStyle()
    #
    def isExpandPressRectContain(self, pos):
        if self.isExpandButton():
            return self.isRectContainPos(self.expandPressRect(), pos)
        else:
            return self.isRectContainPos(self.expandRect(), pos)
    #
    def setExpandSize(self, w, h):
        self._uiExpandFrameWidth, self._uiExpandFrameHeight = w, h
    #
    def expandSize(self):
        return self._uiExpandFrameWidth, self._uiExpandFrameHeight
    #
    def isIconRectContain(self, pos):
        if self.iconRect() is not None:
            return self.isRectContainPos(self.iconRect(), pos)
        else:
            return False
    #
    def extendIconRect(self):
        return self._uiExtendIconRect
    #
    def isExtendIconRectContain(self, pos):
        if self.extendIconRect() is not None:
            return self.isRectContainPos(self.extendIconRect(), pos)
        else:
            return False
    #
    def setExtendPressHovered(self, boolean):
        if not boolean == self._isExtendPressHovered:
            self._isExtendPressHovered = boolean
        #
        self._updateQtPressStyle()
    #
    def isExtendPressHovered(self):
        return self._isExtendPressHovered
    #
    def setPressCurrent(self, boolean, ignoreAction=True):
        if not boolean == self._isPressCurrent:
            self._isPressCurrent = boolean
            #
            if ignoreAction is False:
                self._pressClickAction()
                #
                self._extendPressCurrentAction()
            #
            self._updateQtPressStyle()
    #
    def setSubSelected(self, boolean):
        if not boolean == self._isSubSelected:
            self._isSubSelected = boolean
            #
            self._updateQtPressStyle()
    #
    def isSubSelected(self):
        if self.isSelectable():
            return self._isSubSelected
        else:
            return False
    #
    def pressRect(self):
        return self._pressRect
    #
    def setPressAction(self, action):
        self._pressAction = action
    #
    def pressAction(self):
        return self._pressAction
    #
    def acceptPressAction(self):
        if self._pressAction is not None:
            self._pressAction()
    #
    def setPressCommand(self, command):
        self._pressCommand = command
    #
    def pressCommand(self):
        return self._pressCommand
    #
    def acceptPressCommand(self):
        if self._pressCommand is not None:
            exec self._pressCommand
            #
            self.setPressHovered(False)
    #
    def setExtendPressAction(self, action):
        self._extendPressAction = action
    #
    def acceptExtendPressAction(self):
        if self._extendPressAction is not None:
            self._extendPressAction()
    #
    def setExtendPressCommand(self, command):
        self._extendPressCommand = command
    #
    def extendPressCommand(self):
        return self._extendPressCommand
    #
    def acceptExtendPressCommand(self):
        if self._extendPressCommand is not None:
            exec self._extendPressCommand
            #
            self.setExtendPressHovered(False)
    #
    def setSelected(self, boolean):
        if not boolean == self._isSelected:
            self._isSelected = boolean
            #
            self._extendPressSelectAction()
            #
            self._updateQtPressStyle()
    #
    def setPercentEnable(self, boolean):
        self._isPercentEnable = boolean
        #
        self._updateQtPressStyle()
    #
    def isPercentEnable(self):
        return self._isPercentEnable
    #
    def setPercentable(self, boolean):
        self._isPercentable = boolean
    #
    def isPercentable(self):
        if self.isPercentEnable():
            return self._isPercentable
        else:
            return False
    #
    def percentText(self):
        return self._uiPercentText
    #
    def percentTextRect(self):
        return self._uiPercentTextRect
    #
    def percentFrameRect(self):
        return self._uiPercentFrameRect
    #
    def percentValueRect(self):
        return self._uiPercentValueRect
    #
    def setPercent(self, maxValue, value):
        self._valueMaximum = maxValue
        self._value = value
        if self._valueMaximum > 0:
            self.setPercentable(True)
            #
            self._valuePercent = float(value) / float(maxValue)
            #
            if value == 0:
                self._uiPercentText = '0%'
            elif value == maxValue:
                self._uiPercentText = '100%'
            else:
                self._uiPercentText = '{} / {}'.format(str(value).zfill(4), str(maxValue).zfill(4))
        else:
            self.setPercentable(False)
            #
            self._valuePercent = 0
            self._uiPercentText = 'N/a'
        #
        self._updateRectGeometry()
        self._updateQtPressStyle()
    #
    def setPercentRest(self):
        self._uiPercentText = 'N/a'
        #
        self._valueMaximum = 0
        self._value = 0
        #
        self.percentValueRect().setRect(-20, -20, 1, 1)
        self._updateQtPressStyle()
    #
    def setPressStarted(self, boolean):
        if not boolean == self._isPressStarted:
            self._isPressStarted = boolean
            #
            self._updateWidgetState()
    #
    def isPressStarted(self):
        if self.isPressable():
            return self._isPressStarted
        else:
            return False
    #
    def setDragStarted(self, boolean):
        if not boolean == self._isDragPressStarted:
            self._isDragPressStarted = boolean
            #
            self._updateWidgetState()
    #
    def isDragStarted(self):
        if self.isPressable():
            return self._isDragPressStarted
        else:
            return False
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
        childItemModel.setExpandSize(*self.viewModel().expandSize())
        childItemModel.setSelectEnable(self.viewModel().isSelectEnable())
        childItemModel.setExpandEnable(True)
        childItemModel.setCheckEnable(self.viewModel().isCheckEnable())
        childItemModel.setColorEnable(self.viewModel().isColorEnable())
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


# Enter Item
class QtAbc_EnteritemModel(qtDefinition.QtDef_ItemModel):
    def _initAbcEnteritemModel(self):
        self._initItemModelDef()
        #
        self._initAbcEnteritemModelAttr()
        self._initAbcEnteritemModelAction()
        self._initAbcEnteritemModelRect()
        self._initAbcEnteritemModelUi()
        self._initAbcEnteritemModelVar()
    #
    def _initAbcEnteritemModelAttr(self):
        self._datum = None
        self._datumType = None
        self._defaultDatum = None
        #
        self._datumLis = []
        self._datumDic = {}
        #
        self._datumCount = 0
        self._curDatumIndex = 0
        #
        self._enterWidget = None
        #
        self._isEnterEnable = False
        self._isEnterable = False
        self._isEntered = False
        #
        self._isChooseEnable = False
        self._isChooseable = False
        #
        self._uiEnterStatus = qtCore.NormalStatus
    #
    def _initAbcEnteritemModelAction(self):
        pass
    #
    def _initAbcEnteritemModelRect(self):
        self._uiEnterRect = QtCore.QRect(-20, -20, 1, 1)
    #
    def _initAbcEnteritemModelUi(self):
        self._uiDatumText = None
        self._uiDatumTextLis = []
        self._uiDatumTextDic = {}
    #
    def _initAbcEnteritemModelVar(self):
        pass
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
    def _updateUiEnterStatus(self):
        status = self._uiEnterStatus
        if status is qtCore.NormalStatus:
            self.widget()._uiEnterBackgroundRgba = [(47, 47, 47, 255), (39, 39, 39, 255)][self.isEntered()]
        elif status is qtCore.WarningStatus:
            self.widget()._uiEnterBackgroundRgba = [(127, 127, 64, 255), (96, 96, 48, 255)][self.isEntered()]
        elif status is qtCore.ErrorStatus:
            self.widget()._uiEnterBackgroundRgba = [(127, 64, 64, 255), (96, 48, 48, 255)][self.isEntered()]
        elif status is qtCore.OnStatus:
            self.widget()._uiEnterBackgroundRgba = [(64, 127, 64, 255), (48, 96, 48, 255)][self.isEntered()]
    #
    def _chooseAction(self):
        pass
    #
    def _chooseScrollUpAction(self):
        index = self._curDatumIndex
        if index > 0:
            datum = self._datumLis[index - 1]
            self.setChoose(datum)
    #
    def _chooseScrollDownAction(self):
        index = self._curDatumIndex
        count = len(self._datumLis)
        if index < count - 1:
            datum = self._datumLis[index + 1]
            self.setChoose(datum)
    #
    def setIntValidator(self):
        self._enterWidget.setIntValidator()
        self._datumType = int
    #
    def setTextValidator(self, limit):
        self._enterWidget.setTextValidator(limit)
        self._datumType = unicode
    #
    def setUiEnterState(self, state):
        if state is qtCore.NormalState:
            self._widget._uiEnterBackgroundRgba = 0, 0, 0, 0
            self._widget._uiEnterBorderRgba = 0, 0, 0, 0
        else:
            if state is qtCore.EnterState:
                self._widget._uiEnterBorderRgba = 63, 127, 255, 255
            elif state is qtCore.UnenterState:
                self._widget._uiEnterBorderRgba = 95, 95, 95, 255
            #
            self._updateUiEnterStatus()
    #
    def setUiEnterStatus(self, status):
        self._uiEnterStatus = status
        #
        self._updateUiEnterState()
    #
    def setDatum(self, datum):
        self._datum = datum
        self._datumType = type(datum)
        #
        self.setDatumText(datum)
    #
    def datum(self):
        return self._covertDatum(self._uiDatumText)
    #
    def _covertDatum(self, text):
        _datum = None
        if self._datumType is bool:
            _datum = eval(text)
        elif self._datumType is int:
            _datum = int(text)
        elif self._datumType is float:
            _datum = float(text)
        elif self._datumType is str or self._datumType is unicode:
            if not self._datumDic:
                _datum = text
            else:
                _datum = self._datumDic[text][1]
        elif self._datumType is tuple or self._datumType is list:
            _datum = text.split(',')
        elif self._datumType is dict:
            dic = {}
            lis = [i.split(':') for i in text.split(',')]
            for k, v in lis:
                dic[k] = v
            _datum = dic
        return _datum
    #
    def setDatumText(self, datum):
        self._uiDatumText = self._toUiDatum(datum)
        #
        self._updateWidgetState()
    #
    def datumText(self):
        return self._uiDatumText
    #
    def datumRect(self):
        return self._uiDatumRect
    #
    def drawDatumText(self):
        return self._toDrawText(self.datumRect(), self.datumText())
    #
    def setDefaultDatum(self, datum):
        self._defaultDatum = datum
    #
    def defaultDatum(self):
        return self._defaultDatum
    #
    def setDatumLis(self, lis):
        if lis:
            self._datumLis = lis
            self._datumCount = len(self._datumLis)
            self.setDatumTextLis(self._datumLis)
            #
            self.setChoose(self._datumLis[0])
            #
            self.setChooseable(True)
        else:
            self._datumLis = []
            #
            self._datumCount = 0
            self.setDatumTextLis(self._datumLis)
            #
            self._datum = None
            self._curDatumIndex = 0
            #
            self.setChooseable(False)
    #
    def datumLis(self):
        return self._datumLis
    #
    def setDatumTextLis(self, lis):
        if lis:
            self._uiDatumTextLis = lis
            self._uiDatumText = lis[0]
        else:
            self._uiDatumTextLis = []
            self._uiDatumText = None
    #
    def datumTextLis(self):
        return self._uiDatumTextLis
    #
    def setExtendDatumDic(self, dic):
        if isinstance(dic, dict):
            lis = []
            uiLis = []
            #
            self._datumDic = {}
            self._uiDatumTextDic = {}
            for key, (datum, description) in dic.items():
                datumText = unicode(description)
                if datumText in uiLis:
                    if not '#' in datumText:
                        datumText += '#1'
                    else:
                        number = int(datumText.split('#')[-1])
                        datumText = datumText.split('#')[0] + '[%s]' % number + 1
                #
                self._datumDic[datumText] = key, datum
                self._uiDatumTextDic[datum] = datumText
                #
                lis.append(datum)
                uiLis.append(datumText)
            #
            self.setDatumLis(lis)
            self.setDatumTextLis(uiLis)
    #
    def extendDatumDic(self):
        return self._datumDic
    #
    def extendDatum(self):
        if self._datumDic:
            return self._datumDic[self._uiDatumText]
    #
    def chooseCount(self):
        return len(self._datumLis)
    #
    def setChooseIndex(self, index):
        datum = self._datumLis[index]
        self.setChoose(datum)
    #
    def chooseIndex(self):
        return self._curDatumIndex
    #
    def setEnterEnable(self, boolean):
        self._isEnterEnable = boolean
        self._datumType = unicode
    #
    def isEnterEnable(self):
        return self._isEnterEnable
    #
    def setEnterable(self, boolean):
        self._isEnterable = boolean
    #
    def isEnterable(self):
        if self.isEnterEnable():
            return self._isEnterable
        else:
            return False
    #
    def setEntered(self, boolean):
        self._isEntered = boolean
    #
    def isEntered(self):
        if self.isEnterable():
            return self._isEntered
        else:
            return False
    #
    def setChooseEnable(self, boolean):
        self._isChooseEnable = boolean
        #
        self.update()
    #
    def isChooseEnable(self):
        return self._isChooseEnable
    #
    def setChooseable(self, boolean):
        self._isChooseable = boolean
    #
    def isChooseable(self):
        if self.isChooseEnable():
            return self._isChooseable
        else:
            return False
    #
    def setChoose(self, string):
        if self._datumDic:
            if string in self._datumLis:
                self.setDatum(string)
                self.setDatumText(self._uiDatumTextDic[string])
            elif string in self._uiDatumTextLis:
                self.setDatum(self._datumDic[string][1])
                self.setDatumText(string)
        else:
            if string in self._datumLis:
                self.setDatum(string)
                self.setDatumText(string)
        #
        self._chooseAction()


# Value Enter Item
class QtAbc_ValueEnteritemModel(qtDefinition.QtDef_ItemModel):
    def _initAbcValueEnteritemModel(self):
        self._initItemModelDef()
        #
        self._initAbcValueEnteritemModelAttr()
        self._initAbcValueEnteritemModelAction()
        self._initAbcValueEnteritemModelRect()
        self._initAbcValueEnteritemModelUi()
        self._initAbcValueEnteritemModelVar()
    #
    def _initAbcValueEnteritemModelAttr(self):
        self._valueLis = []
        self._defaultValueLis = []
        #
        self._valueCount = 1
        #
        self._enterIndex = -1
        #
        self._isEnterEnable = True
        self._isEnterable = True
        self._isEnteredLis = []
        #
        self._valueType = None
        #
        self._enterWidgetClass = None
        #
        self._uiEnterStatusLis = []
        #
        self._enterWidgetLis = []
        #
        self._maxValue, self._miniValue = None, None
    #
    def _initAbcValueEnteritemModelAction(self):
        pass
    #
    def _initAbcValueEnteritemModelRect(self):
        self._uiEnterRectLis = [QtCore.QRect()]
    #
    def _initAbcValueEnteritemModelUi(self):
        self._uiValueTextLis = []
    #
    def _initAbcValueEnteritemModelVar(self):
        pass
    #
    def _getEnterIndex(self, widget):
        return self._enterWidgetLis.index(widget)
    #
    def _updateEnterWidgetState(self):
        if self.isEnterable():
            for seq, i in enumerate(self.enterWidgets()):
                self.setEntered(seq, i.hasFocus())
            #
            if self._defaultValueLis:
                for index, defaultValue in enumerate(self._defaultValueLis):
                    widget = self._enterWidgetLis[index]
                    value = widget.value()
                    if value != defaultValue:
                        self._uiEnterStatusLis[index] = qtCore.WarningStatus
                    else:
                        self._uiEnterStatusLis[index] = qtCore.NormalStatus
        #
        self._updateUiEnterState()
    #
    def _updateEnterWidgets(self):
        if self._enterWidgetLis:
            [i.deleteLater() for i in self._enterWidgetLis]
        #
        self._uiEnterRectLis = []
        self._enterWidgetLis = []
        for index in xrange(self.valueCount()):
            self._uiEnterRectLis.append(QtCore.QRect())
            #
            widget = self._enterWidgetClass(self.widget())
            self._enterWidgetLis.append(widget)
            widget.setEnterable(self.isEnterable())
            #
            value = self._valueLis[index]
            if isinstance(value, int):
                self._valueType = int
                widget.setIntValidator()
            elif isinstance(value, float):
                self._valueType = float
                widget.setFloatValidator()
            widget.setText(str(value))
            widget.setFont(self.widget().font())
            #
            widget.focusChanged.connect(self._updateEnterWidgetState)
            widget.entryChanged.connect(self._updateEnterWidgetState)
        #
        self.widget()._uiEnterBackgroundRgbaLis = [(47, 47, 47, 255)]*self.valueCount()
        self.widget()._uiEnterBorderRgbaLis = [(95, 95, 95, 255)]*self.valueCount()
        #
        self._uiEnterStatusLis = [qtCore.NormalStatus] * self.valueCount()
    #
    def _updateUiEnterState(self):
        for index in range(self.valueCount()):
            if self.isEnterable():
                if self.isEntered(index):
                    self.setUiEnterState(index, qtCore.EnterState)
                else:
                    self.setUiEnterState(index, qtCore.UnenterState)
            else:
                self.setUiEnterState(index, qtCore.NormalState)
        #
        self._updateWidgetState()
    #
    def _updateUiEnterStatus(self):
        for index in range(self.valueCount()):
            status = self._uiEnterStatusLis[index]
            if status is qtCore.NormalStatus:
                self.widget()._uiEnterBackgroundRgbaLis[index] = [(47, 47, 47, 255), (39, 39, 39, 255)][self.isEntered(index)]
            elif status is qtCore.WarningStatus:
                self.widget()._uiEnterBackgroundRgbaLis[index] = [(127, 127, 64, 255), (96, 96, 48, 255)][self.isEntered(index)]
            elif status is qtCore.ErrorStatus:
                self.widget()._uiEnterBackgroundRgbaLis[index] = [(127, 64, 64, 255), (96, 48, 48, 255)][self.isEntered(index)]
            elif status is qtCore.OnStatus:
                self.widget()._uiEnterBackgroundRgbaLis[index] = [(64, 127, 64, 255), (48, 96, 48, 255)][self.isEntered(index)]
    #
    def setEnterWidgetClass(self, cls):
        self._enterWidgetClass = cls
    #
    def setValue(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self._valueLis = [value]
        elif isinstance(value, tuple) or isinstance(value, list):
            self._valueLis = list(value)
            #
            self._valueCount = len(self._valueLis)
            #
            self._updateEnterWidgets()
            #
            self._isEnteredLis = [False]*self._valueCount
    #
    def value(self):
        for index in xrange(self.valueCount()):
            text = self._enterWidgetLis[index].text()
            if self._valueType == int:
                if text:
                    self._valueLis[index] = int(text)
                else:
                    self._valueLis[index] = 0
            elif self._valueType == float:
                if text:
                    self._valueLis[index] = float(text)
                else:
                    self._valueLis[index] = 0.0
        #
        if self._valueLis:
            if len(self._valueLis) == 1:
                return self._valueLis[0]
            else:
                return tuple(self._valueLis)
    #
    def setValueRange(self, minimum, maximum):
        self._miniValue, self._maxValue = minimum, maximum
        #
        if self._enterWidgetLis:
            [i.setValueRange(self._miniValue, self._maxValue) for i in self._enterWidgetLis]
    #
    def setDefaultValue(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self._defaultValueLis = [value]
        elif isinstance(value, tuple) or isinstance(value, list):
            self._defaultValueLis = list(value)
        #
        if not self._valueLis:
            self.setValue(self._defaultValueLis)
    #
    def valueCount(self):
        return self._valueCount
    #
    def enterRects(self):
        return self._uiEnterRectLis
    #
    def enterWidgets(self):
        return self._enterWidgetLis
    #
    def setUiEnterStatus(self, index, status):
        self._uiEnterStatusLis[index] = status
        #
        self._updateUiEnterState()
    #
    def setEnterEnable(self, boolean):
        self._isEnterEnable = boolean
    #
    def isEnterEnable(self):
        return self._isEnterEnable
    #
    def setEnterable(self, boolean):
        self._isEnterable = boolean
    #
    def isEnterable(self):
        if self.isEnterEnable():
            return self._isEnterable
        else:
            return False
    #
    def setEntered(self, index, boolean):
        self._isEnteredLis[index] = boolean
    #
    def isEntered(self, index=0):
        if self.isEnterable():
            return self._isEnteredLis[index]
        else:
            return False
    #
    def setUiEnterState(self, index, state):
        if state is qtCore.NormalState:
            self.widget()._uiEnterBackgroundRgbaLis[index] = 0, 0, 0, 0
            self.widget()._uiEnterBorderRgbaLis[index] = 0, 0, 0, 0
        else:
            if state is qtCore.EnterState:
                self.widget()._uiEnterBorderRgbaLis[index] = 63, 127, 255, 255
            elif state is qtCore.UnenterState:
                self.widget()._uiEnterBorderRgbaLis[index] = 95, 95, 95, 255
            #
            self._updateUiEnterStatus()


# View
class QtAbc_ViewModel(qtDefinition.QtDef_ViewModel):
    def _initAbcViewModel(self):
        self._initDefViewModel()
        #
        self._initAbcViewModelAttr()
        self._initAbcViewModelAction()
        self._initAbcViewModelRect()
        self._initAbcViewModelUi()
        self._initAbcViewModelVar()
    #
    def _initAbcViewModelAttr(self):
        self._itemMode = qtCore.ListMode
        #
        self._isPressEnable = True
        self._isSelectEnable = False
        self._isExpandEnable = False
        self._isCheckEnable = False
        self._isColorEnable = False
        #
        self._isExtendExpanded = False
        self._isFilterEnable = False
        #
        self._isEventOverrideEnable = False
        #
        self._filterEntryWidget = None
        #
        self._isFocusFrameEnable = True
    #
    def _initAbcViewModelAction(self):
        self._ctrlFlag, self._shiftFlag, self._altFlag = False, False, False
        #
        self._extendPressFlag = False
        #
        self._expandFlag, self._checkFlag = False, False
        #
        self._dragPressFlag, self._dragCheckFlag = False, False
        #
        self._curPressChangeFlag, self._curCheckChangeFlag = False, False
        self._curHoverChangeFlag, self._selectChangeFlag = False, False
    #
    def _initAbcViewModelRect(self):
        self._dragPressRect = QtCore.QRect(-20, -20, 1, 1)
        self._dragCheckRect = QtCore.QRect(-20, -20, 1, 1)
    #
    def _initAbcViewModelUi(self):
        self._uiWidth, self._uiHeight = 20, 20
        #
        self._uiExpandFrameWidth, self._uiExpandFrameHeight = 20.0, 20.0
    #
    def _initAbcViewModelVar(self):
        self._itemModelLis = []
        #
        self._visibleItemModelIndexLis = []
        #
        self._topItemModelIndexSortLis = []
        self._topItemModelSortKeyLis = []
        #
        self._subItemModelIndexDic = {}
        self._subItemModelIndexCountDic = {}
        self._subVisibleItemModelIndexDic = {}
        self._subVisibleItemModelIndexCountDic = {}
        #
        self._subItemModelIndexSortDic = {}
        self._subItemModelSortKeyDic = {}
        #
        self._itemModelLevelDic = {}
        self._itemModelLevelIndexDic = {}
        # Index
        self._itemIndexCount = 0
        self._minItemIndex, self._maxItemIndex = 0, 0
        self._visibleIndexCount = 0
        self._minVisibleIndex, self._maxVisibleIndex = 0, 0
        self._hoverItemIndex = -1
        self._curHoverVisibleIndex = -1
        self._curPressItemIndex = -1
        self._curCheckItemIndex = - 1
        self._curPressVisibleIndex = -1
        self._curCheckVisibleIndex = -1
        self._pressVisibleIndex = -1
        # Sub Index
        self._subIndexCountDic = {}
        self._subVisibleIndexCountDic = {}
        #
        self._selectedItemModelIndexLis = []
        self._selectedItemModelIndexCount = 0
        self._checkedItemModelIndexCount = 0
        #
        self._selRangePressStartVisibleIndex = -1
        self._rangePressStartItemIndex = -1
        self._rangePressStartItemModel = None
        #
        self._rangeCheckStartVisibleIndex = - 1
        self._rangeCheckStartItemIndex = -1
        self._rangeCheckStartItemModel = None
        #
        self._dragStartVisibleIndex = -1
        self._dragStartItemIndex = -1
        self._dragStartItemModel = None
        self._dragStartChecked = False
        #
        self._curCheckItemModel = None
    #
    def _visibleIndexAt(self, itemIndex):
        if itemIndex in self._visibleItemModelIndexLis:
            return self._visibleItemModelIndexLis.index(itemIndex)
        else:
            return -1
    #
    def _visibleIndex(self, itemModel):
        itemIndex = self.itemModelIndex(itemModel)
        return self._visibleIndexAt(itemIndex)
    #
    def _getClampVisibleColumn(self, column):
        return max(min(int(column), self._maxVisibleColumn), self._minVisibleColumn)
    #
    def _getClampVisibleRow(self, row):
        return max(min(int(row), self._maxVisibleRow), self._minVisibleRow)
    # Visible Item Index
    def _addVisibleItemModelIndexAt(self, itemIndex):
        if not itemIndex in self._visibleItemModelIndexLis:
            self._visibleItemModelIndexLis.append(itemIndex)
            self._updateItemModelVisiblePosAt(itemIndex)
            #
            self._updateVisibleItemModelIndexCount()
    #
    def _updateVisibleItemModelIndexCount(self):
        self._visibleIndexCount = len(self._visibleItemModelIndexLis)
        self._updateMaxVisibleIndex()
    #
    def _updateMaxVisibleIndex(self):
        self._maxVisibleIndex = self._visibleIndexCount + self._minVisibleIndex - 1
    # Select
    def _sepSelectItemAt(self, itemIndex):
        # Clear First
        if self.selectedItemIndexes():
            for i in self.selectedItemIndexes():
                if not i == itemIndex:
                    itemModel = self.itemModelAt(i)
                    itemModel.setSelected(False)
        #
        if not itemIndex in self.selectedItemIndexes():
            itemModel = self.itemModelAt(itemIndex)
            itemModel.setSelected(True)
        #
        self._selectedItemModelIndexLis = [itemIndex]
        # Current Flag
        self._updateCurPressItemIndexAt(itemIndex)
        # Select Flag
        self._selectChangeFlag = True
    #
    def _addSelectItemAt(self, itemIndex):
        isChanged = False
        #
        if not itemIndex in self.selectedItemIndexes():
            self.selectedItemIndexes().append(itemIndex)
            #
            itemModel = self.itemModelAt(itemIndex)
            itemModel.setSelected(True)
            #
            isChanged = True
        # Current Flag
        self._updateCurPressItemIndexAt(itemIndex)
        # Select Flag
        self._selectChangeFlag = isChanged
    #
    def _subSelectItemAt(self, itemIndex):
        isChanged = False
        #
        if itemIndex in self.selectedItemIndexes():
            self.selectedItemIndexes().remove(itemIndex)
            #
            itemModel = self.itemModelAt(itemIndex)
            itemModel.setSelected(False)
            #
            isChanged = True
        # Current Flag
        self._updateCurPressItemIndexAt(itemIndex)
        # Select Flag
        self._selectChangeFlag = isChanged
    #
    def _revSelectItemAt(self, itemIndex):
        if itemIndex in self.selectedItemIndexes():
            self.selectedItemIndexes().remove(itemIndex)
            #
            itemModel = self.itemModelAt(itemIndex)
            itemModel.setSelected(False)
        else:
            self.selectedItemIndexes().append(itemIndex)
            #
            itemModel = self.itemModelAt(itemIndex)
            itemModel.setSelected(True)
        # Current Flag
        self._updateCurPressItemIndexAt(itemIndex)
        # Select Flag
        self._selectChangeFlag = True
    #
    def _restDragSelect(self):
        self._selRangePressStartVisibleIndex = -1
    #
    def _addSelectItemRange(self, *visibleIndexRange):
        isChanged = False
        #
        startIndex, stopIndex = min(visibleIndexRange), max(visibleIndexRange) + 1
        if startIndex >= 0:
            visibleIndexes = range(startIndex, stopIndex)
            for itemIndex in self.selectedItemIndexes():
                visibleIndex = self._visibleIndexAt(itemIndex)
                if not visibleIndex in visibleIndexes:
                    itemModel = self.itemModelAt(itemIndex)
                    itemModel.setSelected(False)
                    #
                    isChanged = True
            #
            lis = []
            #
            for visibleIndex in visibleIndexes:
                itemIndex = self.itemIndexVisibleAt(visibleIndex)
                if itemIndex is not None:
                    itemModel = self.itemModelAt(itemIndex)
                    itemModel.setSelected(True)
                    lis.append(itemIndex)
                    #
                    isChanged = True
            #
            self._selectedItemModelIndexLis = lis
            # Current Flag
            self._updateCurPressItemIndexAt(visibleIndexRange[-1])
            # Select Flag
            if self._curPressChangeFlag is True:
                self._selectChangeFlag = isChanged
            else:
                self._selectChangeFlag = False
    # noinspection PyUnusedLocal
    def _traceSelect(self, delta):
        if self.selectedItemIndexes():
            for itemIndex in self.selectedItemIndexes():
                pass
    #
    def _clearSelect(self, ignoreVisible=False):
        isChanged = False
        if self.selectedItemIndexes():
            for itemIndex in self.selectedItemIndexes():
                itemModel = self.itemModelAt(itemIndex)
                if ignoreVisible is False:
                    itemModel.setSelected(False)
            #
            isChanged = True
        #
        self._selectedItemModelIndexLis = []
        # Current Flag
        self._updateCurPressItemIndexAt(-1)
        # Select Flag
        self._selectChangeFlag = isChanged
    #
    def _updateCurPressItemIndexAt(self, itemIndex):
        isChanged = False
        if not self._curPressItemIndex == itemIndex:
            isChanged = True
        #
        self._curPressItemIndex = itemIndex
        self._curPressVisibleIndex = self._visibleIndexAt(self._curPressItemIndex)
        self._curPressItemModel = self.itemModelAt(self._curPressItemIndex)
        #
        if self._curPressItemModel is not None:
            self._curPressItemModel.setPressCurrent(True, ignoreAction=True)
        #
        self._curPressChangeFlag = isChanged
    # Check
    def _sepCheckItemAt(self, itemIndex):
        # Clear First
        if self.checkedItemIndexes():
            for i in self.checkedItemIndexes():
                if not i == itemIndex:
                    itemModel = self.itemModelAt(i)
                    itemModel.setChecked(False)
        #
        if not itemIndex in self.checkedItemIndexes():
            itemModel = self.itemModelAt(itemIndex)
            itemModel.setChecked(True)
        #
        self._updateCurCheckItemIndexAt(itemIndex)
    #
    def _addCheckItemAt(self, itemIndex):
        if not itemIndex in self.checkedItemIndexes():
            self.checkedItemIndexes().append(itemIndex)
            #
            itemModel = self.itemModelAt(itemIndex)
            if itemModel._isChecked is False:
                itemModel.setChecked(True)
        #
        self._updateCurCheckItemIndexAt(itemIndex)
    #
    def _subCheckItemAt(self, itemIndex):
        if itemIndex in self.checkedItemIndexes():
            self.checkedItemIndexes().remove(itemIndex)
            #
            itemModel = self.itemModelAt(itemIndex)
            if itemModel._isChecked is True:
                itemModel.setChecked(False)
        #
        self._updateCurCheckItemIndexAt(itemIndex)
    #
    def _revCheckItemAt(self, itemIndex):
        if itemIndex in self.checkedItemIndexes():
            self.checkedItemIndexes().remove(itemIndex)
            #
            itemModel = self.itemModelAt(itemIndex)
            if itemModel._isChecked is True:
                itemModel.setChecked(False)
        else:
            self.checkedItemIndexes().append(itemIndex)
            #
            itemModel = self.itemModelAt(itemIndex)
            if itemModel._isChecked is False:
                itemModel.setChecked(True)
        #
        self._updateCurCheckItemIndexAt(itemIndex)
    #
    def _clearCheck(self, ignoreVisible=False):
        if self.checkedItemIndexes():
            for itemIndex in self.checkedItemIndexes():
                itemModel = self.itemModelAt(itemIndex)
                if ignoreVisible is False and itemModel._isChecked is True:
                    itemModel.setChecked(False)
        #
        self._updateCurPressItemIndexAt(-1)
    #
    def _updateCurCheckItemIndexAt(self, itemIndex):
        self._curCheckItemIndex = itemIndex
        self._curCheckVisibleIndex = self._visibleIndexAt(self._curPressItemIndex)
        self._curCheckItemModel = self.itemModelAt(self._curPressItemIndex)
    # Sort
    def _initTopItemModelSortKeyLis(self):
        if not self._topItemModelSortKeyLis:
            for itemIndex in self.topItemIndexes():
                itemModel = self.itemModelAt(itemIndex)
                if itemModel is not None:
                    name = itemModel.nameText()
                    self._topItemModelSortKeyLis.append((itemIndex, name))
    #
    def _initSubItemModelSortKeyLis(self):
        pass
    #
    def _addTopItemModelIndexSortAt(self, itemIndex):
        if not itemIndex in self._topItemModelIndexSortLis:
            self._topItemModelIndexSortLis.append(itemIndex)
    #
    def _updateTopItemModelIndexSortLis(self):
        self._topItemModelIndexSortLis = []
        #
        for sortKeys in self._topItemModelSortKeyLis:
            itemIndex = sortKeys[0]
            self._topItemModelIndexSortLis.append(itemIndex)
    #
    def _addSubItemModelIndexSortAt(self, parentItemIndex, childItemIndex):
        if not parentItemIndex in self._subItemModelIndexSortDic:
            self._subItemModelIndexSortDic[parentItemIndex] = []
        if not childItemIndex in self._subItemModelIndexSortDic[parentItemIndex]:
            self._subItemModelIndexSortDic[parentItemIndex].append(childItemIndex)
    #
    def _updateSubItemModelIndexSortDic(self):
        pass
    # Item Level
    def _updateItemModelLevelFor(self, level, itemIndex):
        self._itemModelLevelDic[itemIndex] = level
    #
    def _updateItemModelLevelIndexFor(self, level, itemIndex):
        self._itemModelLevelIndexDic.setdefault(level, []).append(itemIndex)
    # Extend Item Index
    def _addSubItemModelIndexAt(self, parentItemIndex, childItemIndex):
        def updateMain():
            if not parentItemIndex in self._subItemModelIndexDic:
                self._subItemModelIndexDic[parentItemIndex] = []
        #
        def updateVisible():
            parentItemModel = self.itemModelAt(parentItemIndex)
            parentItemModel.setExpandable(True)
            #
            childItemModel = self.itemModelAt(childItemIndex)
            if parentItemModel.isExpanded() is True:
                parentItemVisibleIndex = self._visibleIndexAt(parentItemIndex)
                childItemIndexCount = self.childItemIndexCountAt(parentItemIndex)
                if not childItemIndex in self._visibleItemModelIndexLis:
                    self._visibleItemModelIndexLis.insert(parentItemVisibleIndex + childItemIndexCount, childItemIndex)
                    #
                    self._updateVisibleItemModelIndexCount()
            else:
                childItemModel._updateVisible()
        #
        def updateSub():
            if not childItemIndex in self._subItemModelIndexDic[parentItemIndex]:
                self._subItemModelIndexDic[parentItemIndex].append(childItemIndex)
                self._updateSubItemModelIndexCountAt(parentItemIndex)
                #
                updateVisible()
        #
        updateMain()
        updateSub()
    #
    def _updateSubItemModelIndexCountAt(self, parentItemIndex):
        childItemIndexes = self.childItemIndexesAt(parentItemIndex)
        count = len(childItemIndexes)
        self._subItemModelIndexCountDic[parentItemIndex] = count
        #
        parentItemModel = self.itemModelAt(parentItemIndex)
        parentItemModel.setExpandable(count > 0)
    # Extend Visible Item Index
    def _addSubVisibleItemModelIndexAt(self, parentItemIndex, childItemIndex):
        def updateMain():
            if not parentItemIndex in self._subVisibleItemModelIndexDic:
                self._subVisibleItemModelIndexDic[parentItemIndex] = []
        #
        def updateSub():
            if not childItemIndex in self._subVisibleItemModelIndexDic[parentItemIndex]:
                self._subVisibleItemModelIndexDic[parentItemIndex].append(childItemIndex)
                self._updateSubVisibleItemModelIndexCountAt(parentItemIndex)
        #
        updateMain()
        updateSub()
    #
    def _updateSubVisibleItemModelIndexCountAt(self, parentItemIndex):
        childItemIndexes = self.visibleChildItemIndexesAt(parentItemIndex)
        #
        count = len(childItemIndexes)
        self._subVisibleItemModelIndexCountDic[parentItemIndex] = count
        #
        parentItemModel = self.itemModelAt(parentItemIndex)
        parentItemModel.setExpandable(count > 0)
    # Extend Visible
    def _addExtendVisibleItemModelIndexesAt(self, parentItemIndex, childItemIndexes):
        if childItemIndexes:
            parentItemVisibleIndex = self._visibleIndexAt(parentItemIndex)
            if parentItemVisibleIndex is not None:
                if parentItemVisibleIndex >= 0:
                    for childExtendVisibleIndex, childItemIndex in enumerate(childItemIndexes):
                        if not childItemIndex in self.visibleItemIndexes():
                            self._visibleItemModelIndexLis.insert(parentItemVisibleIndex + childExtendVisibleIndex + 1, childItemIndex)
                            childItemModel = self.itemModelAt(childItemIndex)
                            childItemModel._updateVisible()
            #
            self._updateVisibleItemModelIndexCount()
    # noinspection PyUnusedLocal
    def _subExtendVisibleItemModelIndexesAt(self, parentItemIndex, childItemIndexes):
        if childItemIndexes:
            for childItemIndex in childItemIndexes:
                if childItemIndex in self.visibleItemIndexes():
                    self._visibleItemModelIndexLis.remove(childItemIndex)
                    childItemModel = self.itemModelAt(childItemIndex)
                    childItemModel._updateVisible()
            #
            self._updateVisibleItemModelIndexCount()
    #
    def _updateCurVisibleIndex(self):
        visibleIndex = self._indexAt(self._curVisibleColumn, self._curVisibleRow, self._visibleColumnCount)
        if self.isContainVisibleIndex(visibleIndex):
            self._curPressVisibleIndex = visibleIndex
    #
    def _updatePressVisibleIndex(self):
        visibleIndex = self._indexAt(self._pressVisibleColumn, self._pressVisibleRow, self._visibleColumnCount)
        if self.isContainVisibleIndex(visibleIndex):
            self._pressVisibleIndex = visibleIndex
    #
    def _updateCurItemIndexByCurItemModel(self):
        itemIndex = self.itemModelIndex(self._curPressItemModel)
        if itemIndex is not None:
            self.setCurrentIndex(itemIndex)
    #
    def _updateCurVisibleIndexByCurItemModel(self):
        visibleIndex = self._visibleIndex(self._curPressItemModel)
        if visibleIndex is not None:
            self.setCurrentVisibleIndex(visibleIndex)
    #
    def _updateVisibleColumnCount(self):
        if self._itemMode is qtCore.ListMode:
            value = 1
        elif self._itemMode is qtCore.IconMode:
            value = self._toColumnCount(self.viewportWidth(), self._uiItemWidth)
        else:
            value = 1
        #
        self.setVisibleColumnCount(value)
    #
    def _updateCurVisibleColumn(self):
        self._curVisibleColumn = self._getClampVisibleColumn(self.visibleColumnAt(self._curPressVisibleIndex))
    #
    def _updateMaxVisibleColumn(self):
        self._maxVisibleColumn = self._minVisibleColumn + self._visibleColumnCount - 1
    #
    def _updateVisibleRowCount(self):
        value = self._getRowCount(self._visibleIndexCount, self._visibleColumnCount)
        self.setVisibleRowCount(value)
    #
    def _updateCurVisibleRow(self):
        self._curVisibleRow = self._getClampVisibleRow(self.visibleRowAt(self._curPressVisibleIndex))
    #
    def _updateMaxVisibleRow(self):
        self._maxVisibleRow = self._minVisibleRow + self._visibleRowCount - 1
    #
    def _updateAbsSize(self):
        w, h = self._gridSize()
        self._absWidth, self._absHeight = self._visibleColumnCount*w, self._visibleRowCount*h
    #
    def _getClampVisibleIndex(self, visibleIndex):
        return max(min(int(visibleIndex), self._maxVisibleIndex), self._minVisibleIndex)
    # Position
    def _itemModelVisiblePosAt(self, visibleIndex):
        xPos, yPos = 0, 0
        xValue, yValue = self.value()
        w, h = self._gridSize()
        #
        column = self.visibleColumnAt(visibleIndex)
        row = self.visibleRowAt(visibleIndex)
        #
        x, y = xPos + column*w, yPos + row*h
        return x - xValue, y - yValue
    #
    def _updateItemModelVisiblePosAt(self, itemIndex):
        visibleIndex = self._visibleIndexAt(itemIndex)
        if visibleIndex is not None:
            x, y = self._itemModelVisiblePosAt(visibleIndex)
            w, h = self._gridSize()
            if -h < y <= self._viewHeight:
                self._itemModelVisiblePosDic[itemIndex] = x, y
    #
    def _getVisibleIndexRange(self):
        width, height = self._viewWidth, self._viewHeight
        xValue, yValue = self.value()
        #
        w, h = self._gridSize()
        #
        rowCount = max(int(height/h), 0)
        rowOffset = max(int(yValue/h), 0)
        maxRow = rowCount + rowOffset + 1
        #
        minVisibleIndex = self._indexAt(self._minVisibleColumn, rowOffset, self._visibleColumnCount)
        maxVisibleIndex = self._indexAt(self._maxVisibleColumn, maxRow, self._visibleColumnCount)
        #
        minimum = max(minVisibleIndex, 0)
        maximum = min(maxVisibleIndex, self.visibleIndexCount())
        return minimum, maximum
    #
    def _updateVisibleItemsPos(self):
        self._itemModelVisiblePosDic = {}
        if self.visibleIndexCount() > 0:
            minimum, maximum = self._getVisibleIndexRange()
            for itemIndex in self.visibleItemIndexes()[minimum:maximum + 1]:
                self._updateItemModelVisiblePosAt(itemIndex)
    # Size
    def _updateItemModelSizeAt(self, itemIndex):
        w, h = self._uiItemWidth, self._uiItemHeight
        self._itemModelSizeDic[itemIndex] = w, h
    #
    def _updateItemModelsSize(self):
        self._itemModelSizeDic = {}
        if self.itemIndexCount() > 0:
            for itemIndex in self.itemIndexes():
                self._updateItemModelSizeAt(itemIndex)
    #
    def _updateItemModelVisibleSizeAt(self, itemIndex):
        w, h = self._uiItemWidth, self._uiItemHeight
        self._itemModelVisibleSizeDic[itemIndex] = w, h
    #
    def _updateItemModelsVisibleSize(self):
        self._itemModelVisibleSizeDic = {}
        if self.visibleIndexCount() > 0:
            for itemIndex in self.visibleItemIndexes():
                self._updateItemModelVisibleSizeAt(itemIndex)
    # Visible Lis
    def _updateVisibleItemModelIndexLisByVisible(self, ignoreHidden=False):
        def getBranch(itemIndex):
            itemModel = self.itemModelAt(itemIndex)
            # Visible
            if itemModel.isFilterVisible() or ignoreHidden is True:
                self._visibleItemModelIndexLis.append(itemIndex)
                self._updateItemModelVisiblePosAt(itemIndex)
            # Children
            if itemModel.isExpanded():
                if itemIndex in self._subItemModelIndexSortDic:
                    childItemIndexes = self._subItemModelIndexSortDic[itemIndex]
                    for childItemIndex in childItemIndexes:
                        getBranch(childItemIndex)
        #
        self._visibleItemModelIndexLis = []
        #
        if self._topItemModelIndexSortLis:
            for i in self._topItemModelIndexSortLis:
                getBranch(i)
        #
        self._updateVisibleItemModelIndexCount()
    # Visible Lis
    def _updateVisibleItemModelIndexLisByVisible_(self):
        def getBranch(itemIndex):
            itemModel = self.itemModelAt(itemIndex)
            # Visible
            if itemModel.isVisible():
                self._visibleItemModelIndexLis.append(itemIndex)
                self._updateItemModelVisiblePosAt(itemIndex)
            # Children
            if itemModel.isExpanded():
                if itemIndex in self._subItemModelIndexSortDic:
                    childItemIndexes = self._subItemModelIndexSortDic[itemIndex]
                    for childItemIndex in childItemIndexes:
                        getBranch(childItemIndex)
        #
        self._visibleItemModelIndexLis = []
        #
        if self._topItemModelIndexSortLis:
            for i in self._topItemModelIndexSortLis:
                getBranch(i)
        #
        self._updateVisibleItemModelIndexCount()
    #
    def _updateVisibleItemModelIndexLisByFilter(self):
        def getBranch(itemIndex):
            itemModel = self.itemModelAt(itemIndex)
            # Visible
            if itemModel.isMultiFilterVisible():
                self._visibleItemModelIndexLis.append(itemIndex)
                self._updateItemModelVisiblePosAt(itemIndex)
            # Children
            if itemModel.isExpanded():
                if itemIndex in self._subItemModelIndexSortDic:
                    childItemIndexes = self._subItemModelIndexSortDic[itemIndex]
                    for childItemIndex in childItemIndexes:
                        getBranch(childItemIndex)
        #
        self._visibleItemModelIndexLis = []
        #
        if self._topItemModelIndexSortLis:
            for i in self._topItemModelIndexSortLis:
                getBranch(i)
        #
        self._updateVisibleItemModelIndexCount()
    #
    def _updateItemModelsExtendFilterVisible(self):
        def getBranch(itemModel):
            if itemModel.isFilterVisible():
                parentItemModels = itemModel.parentItemModels()
                [lis.append(j) for j in parentItemModels if not j in lis]
        #
        lis = []
        itemModels = self.itemModels()
        if self._isFilterEnable is True:
            if itemModels:
                for i in itemModels:
                    getBranch(i)
        #
        for i in itemModels:
            if i in lis:
                i.setExtendFilterVisible(True)
            else:
                i.setExtendFilterVisible(False)
    #
    def _updateSubVisibleItemModelIndexDicByFilter(self):
        def getBranch(itemIndex):
            itemModel = self.itemModelAt(itemIndex)
            parentItemModel = itemModel.parentItemModel()
            if parentItemModel is not None:
                parentItemIndex = self.itemModelIndex(parentItemModel)
                # Filter Visible
                if itemModel.isFilterVisible() or itemModel.isExtendFilterVisible():
                    self._subVisibleItemModelIndexDic.setdefault(parentItemIndex, []).append(itemIndex)
                    self._addSubVisibleItemModelIndexAt(parentItemIndex, itemIndex)
                    # Expand Visible
                    if parentItemModel.isExpanded():
                        itemModel._updateVisible()
                # Count
                self._updateSubVisibleItemModelIndexCountAt(parentItemIndex)
            # Children
            if itemIndex in self._subItemModelIndexSortDic:
                childItemIndexes = self._subItemModelIndexSortDic[itemIndex]
                for childItemIndex in childItemIndexes:
                    getBranch(childItemIndex)
        #
        self._subVisibleItemModelIndexDic = {}
        #
        if self._topItemModelIndexSortLis:
            for i in self._topItemModelIndexSortLis:
                getBranch(i)
    #
    def _updateByExtendExpandAction(self):
        itemModels = self.topItemModels()
        if itemModels:
            for itemModel in itemModels:
                itemModel.setExtendExpanded(self.isExtendExpanded())
    #
    def _keywordFilterAction(self):
        itemModels = self.itemModels()
        #
        filterEnterLabel = self._filterEntryWidget
        #
        if filterEnterLabel:
            keywordFilterString = filterEnterLabel.datum()
            if keywordFilterString:
                self._isFilterEnable = True
                for i in itemModels:
                    i.setFilterKeyword(keywordFilterString)
            else:
                self._isFilterEnable = False
                [i.setFilterKeyword(None) for i in itemModels]
        #
        self._updateByFilterAction()
        #
        visibleCount = self.visibleIndexCount()
        #
        if hasattr(filterEnterLabel, 'setUiEnterStatus'):
            if visibleCount > 0:
                filterEnterLabel.setUiEnterStatus(qtCore.NormalStatus)
            else:
                filterEnterLabel.setUiEnterStatus(qtCore.ErrorStatus)
        elif hasattr(filterEnterLabel, '_setQtPressStyle'):
            if visibleCount > 0:
                filterEnterLabel._setQtPressStyle(qtCore.OnState)
            else:
                filterEnterLabel._setQtPressStyle(qtCore.ErrorStatus)
    #
    def _updateSelPressStartVisibleIndex(self, visibleIndex):
        if self._shiftFlag is False and self._checkFlag is False:
            self._selRangePressStartVisibleIndex = visibleIndex
    # For Override
    def _updateByFilterAction(self):
        pass
    # For Override
    def update(self):
        pass
    #
    def isContainVisibleIndex(self, visibleIndex):
        if self._visibleIndexCount:
            return self._minVisibleIndex <= visibleIndex <= self._maxVisibleIndex
        else:
            return False
    #
    def isContainItemColumn(self, column):
        return self._minItemColumn <= column <= self._maxItemColumn
    #
    def isContainVisibleColumn(self, column):
        return self._minVisibleColumn <= column <= self._maxVisibleColumn
    #
    def isContainItemRow(self, row):
        return self._minItemRow <= row <= self._maxItemRow
    #
    def isContainVisibleRow(self, row):
        return self._minVisibleRow <= row <= self._maxVisibleRow
    #
    def itemModelsIn(self, itemIndexes):
        lis = []
        if itemIndexes:
            for itemIndex in itemIndexes:
                itemModel = self.itemModelAt(itemIndex)
                lis.append(itemModel)
        return lis
    #
    def itemAt(self, itemIndex):
        itemModel = self.itemModelAt(itemIndex)
        if itemModel:
            return itemModel.widget()
    #
    def itemsIn(self, itemIndexes):
        lis = []
        if itemIndexes:
            for itemIndex in itemIndexes:
                itemModel = self.itemModelAt(itemIndex)
                lis.append(itemModel.widget())
        return lis
    #
    def itemVisiblePosAt(self, itemIndex):
        return self._itemModelVisiblePosDic.get(itemIndex, (0, 0))
    #
    def itemVisibleSizeAt(self, itemIndex):
        return self._itemModelVisibleSizeDic.get(itemIndex, (0, 0))
    #
    def itemModelVisibleAt(self, visibleIndex):
        if self.isContainVisibleIndex(visibleIndex):
            itemIndex = self._visibleItemModelIndexLis[visibleIndex]
            return self.itemModelAt(itemIndex)
    #
    def itemVisibleAt(self, visibleIndex):
        itemModel = self.itemModelVisibleAt(visibleIndex)
        if itemModel:
            return itemModel.widget()
    #
    def itemIndexVisibleAt(self, visibleIndex):
        itemModel = self.itemModelVisibleAt(visibleIndex)
        return self.itemModelIndex(itemModel)
    #
    def isVisibleItemIndexAt(self, itemIndex):
        return itemIndex in self._visibleItemModelIndexLis
    #
    def indexVisibleAt(self, column, row):
        return self._getClampVisibleColumn(column) + self._getClampVisibleRow(row)*self._visibleColumnCount
    #
    def visibleColumnAt(self, visibleIndex):
        return self._columnAt(visibleIndex, self._visibleColumnCount)
    #
    def visibleRowAt(self, visibleIndex):
        return self._rowAt(visibleIndex, self._visibleColumnCount)
    #
    def visibleIndexLoc(self, x, y):
        column, row = self.visibleColumnLoc(x), self.visibleRowLoc(y)
        return self.indexVisibleAt(column, row)
    #
    def visibleColumnLoc(self, x):
        w, h = self._gridSize()
        return self._columnLoc(x, w)
    #
    def visibleRowLoc(self, y):
        w, h = self._gridSize()
        return self._rowLoc(y, h)
    #
    def itemIndex(self, widget):
        itemModel = widget.itemModel()
        return self.itemModelIndex(itemModel)
    #
    def setCurrentIndex(self, itemIndex):
        self._updateCurPressItemIndexAt(self._getClampItemIndex(itemIndex))
        self._updateCurItemColumn()
        self._updateCurItemRow()
    #
    def setCurrentVisibleIndex(self, visibleIndex):
        self._curPressVisibleIndex = self._getClampVisibleIndex(visibleIndex)
        self._updateCurVisibleColumn()
        self._updateCurVisibleRow()
    #
    def extendPressStartVisibleIndex(self):
        return self._selRangePressStartVisibleIndex
    #
    def setDragStartVisibleIndex(self, visibleIndex):
        self._dragStartVisibleIndex = self._getClampVisibleIndex(visibleIndex)
    #
    def dragStartVisibleIndex(self):
        return self._dragStartVisibleIndex
    #
    def setMinItemIndex(self, itemIndex):
        self._minItemIndex = int(itemIndex)
        self._updateMaxItemIndex()
    #
    def setMinVisibleIndex(self, visibleIndex):
        self._minVisibleIndex = int(visibleIndex)
        self._updateMaxVisibleIndex()
    #
    def setVisibleColumnCount(self, value):
        self._visibleColumnCount = int(value)
        self._updateMaxVisibleColumn()
    #
    def setMinVisibleColumn(self, value):
        self._minVisibleColumn = int(value)
        self._updateMaxVisibleColumn()
    #
    def setCurrentColumn(self, value):
        self._curItemColumn = self._getClampItemColumn(value)
        self._updateCurItemIndex()
    #
    def setCurrentVisibleColumn(self, value):
        self._curVisibleColumn = self._getClampVisibleColumn(value)
        self._updateCurVisibleIndex()
    #
    def setVisibleRowCount(self, value):
        self._visibleRowCount = int(value)
        self._updateMaxVisibleRow()
    #
    def setMinVisibleRow(self, row):
        self._minVisibleRow = int(row)
        self._updateMaxVisibleRow()
    #
    def setCurrentItemRow(self, row):
        self._curItemRow = self._getClampItemRow(row)
        self._updateCurItemIndex()
    #
    def setCurrentVisibleRow(self, row):
        self._curVisibleRow = self._getClampVisibleRow(row)
        self._updateCurVisibleIndex()
    #
    def setPressVisibleRow(self, row):
        self._pressVisibleRow = self._getClampVisibleRow(row)
        self._updatePressVisibleIndex()
    #
    def minViewVisibleRow(self):
        w, h = self._gridSize()
        _, yValue = self.value()
        return self._rowLoc(yValue, h)
    #
    def maxViewVisibleRow(self):
        w, h = self._gridSize()
        _, yValue = self.value()
        height = self.height()
        return self._rowLoc(yValue + height, h)
    #
    def currentItem(self):
        if self._curPressItemModel is not None:
            return self._curPressItemModel.widget()
    #
    def checkedItemIndexes(self):
        return [self.itemModelIndex(i) for i in self.itemModels() if i.isChecked()]
    #
    def checkedItemModels(self):
        return [i for i in self.itemModels() if i.isChecked()]
    #
    def checkedItems(self):
        return [i.widget() for i in self.checkedItemModels()]
    #
    def selectedItemIndexes(self):
        return self._selectedItemModelIndexLis
    #
    def selectedItemModels(self):
        return [self.itemModelAt(i) for i in self.selectedItemIndexes()]
    #
    def selectedItems(self):
        return [i.widget() for i in self.selectedItemModels()]
    #
    def visibleCheckItemModels(self):
        return [i for i in self.visibleItemModels() if i.isChecked()]
    #
    def visibleCheckItems(self):
        return [i.widget() for i in self.visibleCheckItemModels()]
    #
    def childItemIndexesAt(self, parentItemIndex):
        if parentItemIndex in self._subItemModelIndexDic:
            return self._subItemModelIndexDic[parentItemIndex]
        else:
            return []
    #
    def childItemIndexCountAt(self, parentItemIndex):
        if parentItemIndex in self._subItemModelIndexCountDic:
            return self._subItemModelIndexCountDic[parentItemIndex]
        else:
            return 0
    #
    def visibleChildItemIndexesAt(self, parentItemIndex):
        if parentItemIndex in self._subVisibleItemModelIndexDic:
            return self._subVisibleItemModelIndexDic[parentItemIndex]
        else:
            return []
    #
    def visibleChildItemIndexCountAt(self, parentItemIndex):
        if parentItemIndex in self._subVisibleItemModelIndexCountDic:
            return self._subVisibleItemModelIndexCountDic[parentItemIndex]
        else:
            return 0
    #
    def itemLevelAt(self, itemIndex):
        if itemIndex in self._itemModelLevelDic:
            return self._itemModelLevelDic[itemIndex]
        else:
            return 0
    #
    def itemIndexesFor(self, level):
        return self._itemModelLevelIndexDic.get(level, [])
    #
    def itemModelsFor(self, level):
        return [self.itemModelAt(i) for i in self.itemIndexesFor(level)]
    #
    def topItemIndexes(self):
        return self.itemIndexesFor(0)
    #
    def topItemModels(self):
        return self.itemModelsFor(0)
    #
    def visibleColumnCount(self):
        return self._visibleColumnCount
    #
    def rowCount(self):
        return self._itemRowCount
    #
    def visibleRowCount(self):
        return self._visibleRowCount
    #
    def setWidget(self, widget):
        self._widget = widget
        self._widget.setMouseTracking(True)
    #
    def setAbcObjItemWidgetSize(self, w, h):
        self._uiBasicItemWidth, self._uiBasicItemHeight = max(int(w), 1), max(int(h), 1)
    #
    def itemBasicSize(self):
        return self._uiBasicItemWidth, self._uiBasicItemHeight
    #
    def setBasicGridSize(self, w, h):
        self._uiBasicGridWidth, self._uiBasicGridHeight = max(int(w), 1), max(int(h), 1)
    #
    def basicGridSize(self):
        return self._uiBasicGridWidth, self._uiBasicGridHeight
    #
    def setGridSize(self, w, h):
        self._uiGridWidth, self._uiGridHeight = max(int(w), 1), max(int(h), 1)
    #
    def gridSize(self):
        return self._uiGridWidth, self._uiGridHeight
    # For Override
    def value(self):
        return 0, 0
    #
    def setItemMode(self, mode):
        self._itemMode = mode
    #
    def itemMode(self):
        return self._itemMode
    #
    def setPressEnable(self, boolean):
        if not boolean == self._isPressEnable:
            self._isPressEnable = boolean
    #
    def isPressEnable(self):
        return self._isPressEnable
    #
    def setSelectEnable(self, boolean):
        self._isSelectEnable = boolean
    #
    def isSelectEnable(self):
        return self._isSelectEnable
    #
    def setExpandEnable(self, boolean):
        if not boolean == self._isExpandEnable:
            self._isExpandEnable = boolean
    #
    def isExpandEnable(self):
        return self._isExpandEnable
    #
    def setExpandSize(self, w, h):
        self._uiExpandFrameWidth, self._uiExpandFrameHeight = w, h
    #
    def expandSize(self):
        return self._uiExpandFrameWidth, self._uiExpandFrameHeight
    #
    def setCheckEnable(self, boolean):
        if not boolean == self._isCheckEnable:
            self._isCheckEnable = boolean
    #
    def isCheckEnable(self):
        return self._isCheckEnable
    #
    def setColorEnable(self, boolean):
        if not boolean == self._isColorEnable:
            self._isColorEnable = boolean
    #
    def isColorEnable(self):
        return self._isColorEnable
    #
    def setExtendExpanded(self, boolean, ignoreAction=False):
        self._isExtendExpanded = boolean
        if ignoreAction is False:
            self._updateByExtendExpandAction()
    #
    def isExtendExpanded(self):
        if self.isExpandEnable():
            return self._isExtendExpanded
        else:
            return False
    #
    def setEventOverrideEnable(self, boolean):
        self._isEventOverrideEnable = boolean
    #
    def isEventOverrideEnable(self):
        return self._isEventOverrideEnable
    #
    def setFocusFrameEnable(self, boolean):
        if not boolean == self._isFocusFrameEnable:
            self._isFocusFrameEnable = boolean
        #
        self._widget.update()
    #
    def isFocusFrameEnable(self):
        return self._isFocusFrameEnable
    #
    def setFilterConnect(self, widget):
        self._filterEntryWidget = widget
        self._filterEntryWidget.entryChanged.connect(self._keywordFilterAction)
    #
    def addItem(self, widget):
        widget.setParent(self._viewport)
        itemIndex = self.itemIndexCount()
        #
        itemModel = widget.itemModel()
        #
        itemModel.setViewModel(self)
        #
        itemModel.setIndex(itemIndex)
        itemModel.setItemSize(*self.itemSize())
        itemModel.setExpandSize(*self.expandSize())
        itemModel.setSelectEnable(self.isSelectEnable())
        itemModel.setExpandEnable(self.isExpandEnable())
        itemModel.setCheckEnable(self.isCheckEnable())
        itemModel.setColorEnable(self.isColorEnable())
        #
        itemModel.setItemMode(self._itemMode)
        #
        itemModel.setEventOverrideEnable(True)
        # Item Model
        self._addItemModel(itemModel)
        # Level
        self._updateItemModelLevelFor(0, itemIndex)
        self._updateItemModelLevelIndexFor(0, itemIndex)
        # Index
        self._addVisibleItemModelIndexAt(itemIndex)
        # Sort
        self._addTopItemModelIndexSortAt(itemIndex)
        # Check
        if itemModel.isChecked():
            self._addCheckItemAt(itemIndex)
    #
    def removeItem(self, widget):
        itemModel = widget.itemModel()
        widget.deleteLater()
        self.removeItemModel(itemModel)
    #
    def removeItemModel(self, itemModel):
        if itemModel in self._itemModelLis:
            self._itemModelLis.remove(itemModel)
            #
            self._updateItemModelIndexCount()
            #
            self.update()


# Group
class QtAbc_GroupModel(qtDefinition.QtDef_GroupModel):
    def _initAbcGroupModel(self):
        self._initGroupModelDef()
    #
    def _initAbcGroupModelAttr(self):
        pass


# Scroll Bar
class QtAbc_ScrollbarModel(qtDefinition.QtDef_ScrollbarWidget):
    def _initAbcScrollbarModel(self):
        self._initDefScrollbarWidget()
    #
    def _initAbcScrollbarModelVar(self):
        self._initDefScrollbarWidgetVar()
    #
    def _initScrollBarConnect(self):
        self._subScrollButton.clicked.connect(self._subPageAction)
        self._subScrollButton.pressed.connect(self._startAutoSubAction)
        self._subScrollButton.released.connect(self._autoScrollStopAction)
        #
        self._addScrollButton.clicked.connect(self._addPageAction)
        self._addScrollButton.pressed.connect(self._startAutoAddAction)
        self._addScrollButton.released.connect(self._autoScrollStopAction)
    #
    def __menuSize(self):
        return [0, self._uiScrollBarWidth][self._isPressMenuEnable]
    #
    def __buttonSize(self):
        return self._uiScrollBarWidth
    #
    def __unionSize(self):
        return [0, self._uiScrollBarWidth][self._unionFlag]
    @staticmethod
    def _getPercent(height, maxHeight):
        if maxHeight > 0:
            return float(height)/float(maxHeight)
        else:
            return 0
    #
    def _updatePercent(self):
        self._percent = self.mtd_raw_value.mapTo(
            value=self._value,
            sourceValueRange=(self._minimum, self._maximum),
            targetValueRange=(self._minPercent, self._maxPercent)
        )
    #
    def _updateValueByRow(self):
        self._value = int(self._value/self._rowValue)*self._rowValue
    #
    def _updateValueByPercent(self):
        self._updateMaximumValue()
        #
        value = self.mtd_raw_value.mapTo(
            value=self._percent,
            sourceValueRange=(self._minPercent, self._maxPercent),
            targetValueRange=(self._minimum, self._maximum),
        )
        #
        self.setValue(value)
        # Update To Temp
        self._updateTempValue()
    #
    def _updateTempValue(self):
        self._tempValue = self._value
    #
    def _updateRow(self):
        self._curVisibleRow = int(round(self._value/self._rowValue))
        #
        self._minItemRow = int(self._minimum/self._rowValue)
        self._maxItemRow = int(self._maximum/self._rowValue)
    #
    def _updatePageSize(self):
        if self._dir == qtCore.Vertical:
            if self._rowValue > 0:
                self._pageValue = int(self.height()/self._rowValue)*self._rowValue
        else:
            if self._rowValue > 0:
                self._pageValue = int(self.width()/self._rowValue)*self._rowValue
    #
    def _updateMaximumValue(self):
        height = self.height()
        self._maximum = self._absHeight - height
    #
    def _updateSliderGeometry(self):
        if self.isScrollable():
            xPos, yPos = self._pos
            #
            width, height = self.width(), self.height()
            #
            w = self._uiScrollBarWidth
            #
            relativeHeight = int(self._maxSliderHeight - self._sliderHeight)
            #
            self._sliderPos = int(self._percent*relativeHeight + w + self.__menuSize())
            #
            if self.direction() == qtCore.Vertical:
                self.basicRect().setRect(
                    xPos, yPos,
                    w - 1, height - self.__unionSize() - 1
                )
                #
                self.sliderRect().setRect(
                    xPos, yPos + self._sliderPos,
                    w - 1, self._sliderHeight
                )
            else:
                self.basicRect().setRect(
                    xPos, yPos,
                    width - self.__unionSize() - 1, w - 1
                )
                #
                self.sliderRect().setRect(
                    xPos + self._sliderPos, yPos,
                    self._sliderHeight, w - 1
                )
    #
    def _updateChildrenGeometry(self):
        if self._isScrollable is True:
            xPos, yPos = self._pos
            #
            width, height = self.width(), self.height()
            #
            w = h = self._uiScrollBarWidth
            # Menu Enable
            if self._isPressMenuEnable is True:
                self._menuButton.show()
            else:
                self._menuButton.hide()
            #
            self._subScrollButton.show(), self._addScrollButton.show()
            self._subScrollButton.setPressable(not self._value == self._minimum), self._addScrollButton.setPressable(not self._value == self._maximum)
            if self._dir == qtCore.Vertical:
                self._menuButton.setGeometry(
                    xPos, yPos,
                    w, h
                )
                self._subScrollButton.setGeometry(
                    xPos, yPos + self.__menuSize(),
                    w, h
                )
                self._addScrollButton.setGeometry(
                    xPos, yPos + height - w - self.__unionSize(),
                    w, h
                )
            else:
                self._menuButton.setGeometry(
                    xPos, yPos,
                    w, h
                )
                self._subScrollButton.setGeometry(
                    xPos + self.__menuSize(), yPos,
                    w, h
                )
                self._addScrollButton.setGeometry(
                    xPos + width - w - self.__unionSize(), yPos,
                    w, h
                )
        else:
            self._menuButton.hide()
            self._subScrollButton.hide()
            self._addScrollButton.hide()
    #
    def _updateTooltipGeometry(self):
        if self.isTooltipEnable():
            if self.isScrollable():
                if self._dragFlag is True or self._autoScrollFlag is True:
                    currentRow = self._curVisibleRow + 1
                    text = str(currentRow)
                    view = self.widget().parent()
                    if hasattr(view, 'viewModel'):
                        viewModel = view.viewModel()
                        visibleIndex = currentRow * viewModel.visibleColumnCount()
                        text = viewModel.itemModelVisibleAt(visibleIndex).nameText()
                    #
                    self.tooltipWidget().setTooltip(text)
                    #
                    if self._dir == qtCore.Vertical:
                        p1, p2 = self.widget().rect().topLeft(), self.widget().rect().topRight()
                        p_ = self.widget().mapToGlobal(p1 + p2/2)
                        #
                        self.tooltipWidget().uiShow(
                            p_.x(), p_.y() + self._sliderPos
                        )
                else:
                    self.tooltipWidget().hide()
            else:
                self.tooltipWidget().hide()
    #
    def _updateGeometry(self):
        self._updateSliderGeometry()
        self._updateChildrenGeometry()
        self._updateTooltipGeometry()
    #
    def _hoverScrollAction(self):
        self._updateHoverLoc(*self._pressHoverPos)
    #
    def _clearHover(self):
        if self._isSliderHover is True:
            self._isSliderHover = False
        #
        self._pressHoverPos = 0, 0
        #
        self.widget().update()
    #
    def _clearPress(self):
        if self._isSliderPress is True:
            self._isSliderPress = False
            #
            self.widget().update()
    #
    def _clearClick(self):
        if self._isClick is True:
            self._isClick = False
            #
            self.widget().update()
    #
    def _addAction(self):
        if self.value() < self.maximum():
            value = self.mtd_raw_value.stepTo(
                value=self._value, delta=+1, step=40,
                valueRange=(self._minimum, self._maximum)
            )
            self.setValue(value)
        else:
            self._autoScrollStopAction()
    #
    def _subAction(self):
        if self.minimum() < self.value():
            value = self.mtd_raw_value.stepTo(
                value=self._value,
                delta=-1,
                step=40,
                valueRange=(self._minimum, self._maximum)
            )
            self.setValue(value)
        else:
            self._autoScrollStopAction()
    #
    def _addRowAction(self):
        if self._curVisibleRow < self._maxItemRow:
            value = self.mtd_raw_value.stepTo(
                value=self._value,
                delta=+1,
                step=self._rowValue,
                valueRange=(self._minimum, self._maximum)
            )
            self.setValue(value, isRow=True)
        else:
            self._autoScrollStopAction()
    #
    def _subRowAction(self):
        if self._minItemRow < self._curVisibleRow:
            value = self.mtd_raw_value.stepTo(
                value=self._value,
                delta=-1,
                step=self._rowValue,
                valueRange=(self._minimum, self._maximum)
            )
            self.setValue(value, isRow=True)
        else:
            self._autoScrollStopAction()
    #
    def _subPageAction(self):
        value = self.mtd_raw_value.stepTo(
            value=self._value,
            delta=-1,
            step=self._pageValue,
            valueRange=(self._minimum, self._maximum)
        )
        self.setValue(value)
    #
    def _addPageAction(self):
        value = self.mtd_raw_value.stepTo(
            value=self._value,
            delta=+1,
            step=self._pageValue,
            valueRange=(self._minimum, self._maximum)
        )
        self.setValue(value)
    #
    def _addScrollAction(self):
        if self._shiftFlag is True:
            self._addRowAction()
        else:
            self._addAction()
    #
    def _subScrollAction(self):
        if self._shiftFlag is True:
            self._subRowAction()
        else:
            self._subAction()
    #
    def _updatePressStartPos(self, x, y):
        if self._dir == qtCore.Vertical:
            self._yPressStartPos = int(y)
        else:
            self._yPressStartPos = int(x)
    #
    def _updateClickPos(self, x, y):
        if self._dir == qtCore.Vertical:
            self._clickPos = int(y)
        else:
            self._clickPos = int(x)
        #
        self._updateClickRect()
    #
    def _updateHoverLoc(self, x, y):
        if self._isScrollable:
            self._pressHoverPos = x, y
            #
            if self.basicRect() is not None:
                if self.basicRect().contains(x, y):
                    if self.sliderRect().contains(x, y):
                        self._isSliderHover = True
                    else:
                        self._isSliderHover = False
                    #
                    self.widget().update()
                else:
                    self._clearHover()
    #
    def _updateDragPressLoc(self, x, y):
        if self._isScrollable is True:
            if self._dir == qtCore.Vertical:
                v = int(y)
            else:
                v = int(x)
            #
            v_ = self._tempValue
            #
            yOffset = v - self._yPressStartPos
            v_ += yOffset/self._dragPercent
            #
            v_ = max(min(v_, self._maximum), self._minimum)
            #
            self.setValue(v_)
    #
    def _updateClickRect(self):
        xPos, yPos = self._pos
        #
        width, height = self.width(), self.height()
        #
        w, h = self._uiScrollBarWidth, self._uiScrollBarWidth
        #
        if self.direction() == qtCore.Vertical:
            c = max(min(self._clickPos, height - self.__unionSize() - 2), 2 + 1)
            h = c - self._sliderPos
            #
            self._clickRect.setRect(
                xPos + 2, yPos + self._sliderPos,
                w - 4, h
            )
        else:
            c = max(min(self._clickPos, width - self.__unionSize() - 2), 2 + 1)
            w = c - self._sliderPos
            #
            self._clickRect.setRect(
                xPos + self._sliderPos, yPos + 2,
                w, h - 4
            )
    #
    def _updateClickLoc(self, x, y):
        if self.isScrollable():
            width, height = self.width(), self.height()
            #
            if self.direction() == qtCore.Vertical:
                v = int(y)
                maxV = height
            else:
                v = int(x)
                maxV = width
            #
            percent = float(v - (self.__menuSize() + self.__buttonSize()))/float(maxV - (self.__menuSize() + self.__buttonSize()*2 + self.__unionSize()))
            #
            value = self._maximum*percent
            #
            self.setValue(value)
    #
    def _hoverExecuteAction(self, event):
        point = event.pos()
        x, y = point.x(), point.y()
        #
        self._updateHoverLoc(x, y)
    #
    def _pressStartAction(self, event):
        if self.basicRect() is not None:
            point = event.pos()
            x, y = point.x(), point.y()
            if self.basicRect().contains(event.pos()):
                if self.sliderRect().contains(event.pos()):
                    # Flag
                    self._pressFlag, self._dragFlag, self._clickFlag = True, True, False
                    # Action
                    self._updatePressStartPos(x, y)
                else:
                    # Flag
                    self._pressFlag, self._dragFlag, self._clickFlag = False, False, True
                    # Action
                    self._updateClickPos(x, y)
            else:
                self._pressFlag, self._dragFlag, self._clickFlag = False, False, False
            #
            self.widget().update()
    #
    def _pressExecuteAction(self, event):
        point = event.pos()
        x, y = point.x(), point.y()
        #
        if self._dragFlag is True:
            self._updateDragPressLoc(x, y)
        elif self._clickFlag is True:
            self._updateClickPos(x, y)
        #
        self.widget().update()
    #
    def _pressStopAction(self, event):
        point = event.pos()
        x, y = point.x(), point.y()
        # Action
        if self._clickFlag is True:
            self._updateClickLoc(x, y)
        # Flag
        self._pressFlag, self._dragFlag, self._clickFlag = False, False, False
        #
        self._clearPress()
        #
        self._updateTempValue()
        #
        self._autoScrollStopAction()
        #
        self.widget().update()
    #
    def _wheelAction(self, delta):
        if self._isScrollable:
            step = self._basicValue
            #
            value = self.mtd_raw_value.stepTo(
                value=self._value,
                delta=-delta,
                step=step,
                valueRange=(self._minimum, self._maximum)
            )
            self.setValue(value)
            #
            self._updateTempValue()
    #
    def _startAutoAddAction(self):
        self._autoScrollFlag = True
        #
        self._addScrollTimer.setInterval(self._timerInterval)
        #
        if self._addScrollFlag is False:
            self._addScrollFlag = True
            #
            self._addScrollTimer.timeout.connect(self._addScrollAction)
        #
        if not self.isMaximum():
            if not self._addScrollTimer.isActive():
                self._addScrollTimer.start()
    #
    def _startAutoSubAction(self):
        self._autoScrollFlag = True
        #
        self._subScrollTimer.setInterval(self._timerInterval)
        #
        if self._subScrollFlag is False:
            self._subScrollFlag = True
            #
            self._subScrollTimer.timeout.connect(self._subScrollAction)
        #
        if not self.isMinimum():
            if not self._subScrollTimer.isActive():
                self._subScrollTimer.start()
    #
    def _autoScrollStopAction(self):
        self._tooltipWidget.hide()
        #
        self._addScrollTimer.stop(), self._subScrollTimer.stop()
        #
        self._updateTempValue()
        #
        self.widget().stop.emit()
        #
        self._autoScrollFlag = False
    #
    def _updateUnion(self, boolean):
        if self._unionFlag is not boolean:
            self._unionFlag = boolean
            #
            self.update()
    #
    def update(self):
        width, height = self.width(), self.height()
        #
        w = self._uiScrollBarWidth
        #
        if self._dir == qtCore.Vertical:
            self._pos = width - w, 0
            scrollHeight = self.height()
        else:
            self._pos = 0, height - w
            scrollHeight = self.width()
        #
        if self._isScrollable is True:
            self._maxSliderHeight = scrollHeight - (w*2 + self.__menuSize() + self.__unionSize())
            #
            self._maximum = self._absHeight - scrollHeight + self.__unionSize()
            self._value = self.getClampValue(self._value)
            # Percent
            self._updatePercent()
            # Row
            self._updateRow()
            #
            self._sliderPercent = qtCore.toPercent(scrollHeight, self._absHeight)
            #
            absSliderHeight = int(self._sliderPercent*self._maxSliderHeight)
            if absSliderHeight < self._minSliderHeight:
                self._sliderHeight = self._minSliderHeight
            else:
                self._sliderHeight = absSliderHeight
            #
            self._dragPercent = qtCore.toPercent(self._maxSliderHeight, self._absHeight)
        else:
            self._initAbcScrollbarModelVar()
        #
        self._updatePageSize()
        #
        self._updateGeometry()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._addScrollButton = self.widget()._addScrollButton
        self._subScrollButton = self.widget()._subScrollButton
        self._menuButton = self.widget()._menuButton
        self._tooltipWidget = self.widget()._tooltipWidget
        #
        self._initScrollBarConnect()
    #
    def setValueByPercent(self, percent):
        value = self.mtd_raw_value.mapTo(
            value=percent,
            sourceValueRange=(self._minPercent, self._maxPercent),
            targetValueRange=(self._minimum, self._maximum),
        )
        #
        self.setValue(value)
        # Update To Temp
        self._updateTempValue()
    #
    def valuePercent(self):
        return self.mtd_raw_value.mapTo(
            value=self._value,
            sourceValueRange=(self._minimum, self._maximum),
            targetValueRange=(self._minPercent, self._maxPercent),
        )


# Scroll Area
class QtAbc_ScrollareaModel(qtDefinition.QtDef_ScrollareaWidget):
    def _initAbcScrollareaModel(self):
        self._initDefScrollarea()
        #
        self._initAbcScrollareaModelAttr()
        self._initAbcScrollareaModelAction()
        self._initAbcScrollareaModelUi()
        self._initAbcScrollareaModelVar()
    #
    def _initAbcScrollareaModelAttr(self):
        pass
    #
    def _initAbcScrollareaModelAction(self):
        self._trackActionModel = qtAction.QtTrackactionModel(self)
        self._trackActionModel.setMinimumPos(0, 0)
    #
    def _initAbcScrollareaModelUi(self):
        pass
    #
    def _initAbcScrollareaModelVar(self):
        pass
    #
    def _trackStartAction(self, event):
        # Flag
        self._pressFlag, self._dragFlag, self._trackFlag = False, False, True
        # Action
        self.trackActionModel()._startAction(event)
    #
    def _trackExecuteAction(self, event):
        # Flag
        self._pressFlag, self._dragFlag, self._trackFlag = False, False, True
        # Action
        self.trackActionModel()._executeAction(event)
        self._hoverExecuteAction(event)
        #
        x, y = self.trackActionModel().pos()
        self.vScrollBar()._viewModel.setValue(y)
    # noinspection PyUnusedLocal
    def _trackStopAction(self, event):
        # Action
        self.trackActionModel()._stopAction()
        self.vScrollBar()._viewModel._updateTempValue()
        # Flag
        self._pressFlag, self._dragFlag, self._trackFlag = False, False, False
    #
    def trackActionModel(self):
        return self._trackActionModel


# Action Drop View
class QtAbc_ActionDropviewModel(qtDefinition.QtDef_Widget):
    def _initAbcActionDropAbcViewModel(self):
        self._initDefWidget()
        #
        self._initAbcActionDropAbcViewModelAttr()
        self._initAbcActionDropAbcViewModelAction()
        self._initAbcActionDropAbcViewModelRect()
        self._initAbcActionDropAbcViewModelUi()
        self._initAbcActionDropAbcViewModelVar()
    #
    def _initAbcActionDropAbcViewModelAttr(self):
        self._widget = None
        #
        self._itemClass = None
        #
        self._vScrollBar = None
        #
        self._separateButton = None
        #
        self._isTearable = False
    #
    def _initAbcActionDropAbcViewModelAction(self):
        self._curPressChangeFlag = False
        #
        self._pressFlag, self._dragFlag = False, False
        self._actionFlag = False
    #
    def _initAbcActionDropAbcViewModelUi(self):
        self._uiMaxWidth, self._uiMinWidth = 480, 160
        #
        self._uiFrameWidth, self._uiFrameHeight = 20, 20
        self._uiItemHeight = 20
        #
        self._uiSide, self._gap, self._uiMargin, self._uiShadowRadius = 4, 16, 8, 4
    #
    def _initAbcActionDropAbcViewModelRect(self):
        self._uiBasicRect, self._titleRect, self._uiCentralRect = QtCore.QRect(), QtCore.QRect(), QtCore.QRect()
        self._titleLine = QtCore.QLine()
    #
    def _initAbcActionDropAbcViewModelVar(self):
        self._region = 0
        #
        self._subItemDic = {}
        self._subItemPosDic = {}
        self._subCurIndexDic = {}
        self._subCurItemDic = {}
        self._subActionsDic = {}
        self._subEnableDic = {}
        self._subRectDic = {}
        self._subAbsRectDic = {}
        self._subRectPosDic = {}
        self._subRectWidthDic = {}
        self._subRectHeightDic = {}
        self._subIndexCountDic = {}
        #
        self._uiNameText = None
        #
        self._acceptAction = None
        #
        self._curPressAction = None
        self._curPressCommand = None
        #
        self._curItemColumn = 0
    #
    def __titleHeight(self):
        return [0, self._uiItemHeight][self._isTearable]
    #
    def _getWidthAt(self, column):
        item = self._itemClass()
        #
        actionData = self._subActionsDic[column]
        #
        texts = [i[0] for i in actionData if i]
        if self._uiNameText is not None:
            texts.append(self._uiNameText)
        #
        widths = [item.fontMetrics().width(i) for i in texts]
        if widths:
            width = max(min(max(widths) + 48, self._uiMaxWidth), self._uiMinWidth)
        else:
            width = self._uiMinWidth
        #
        item.deleteLater()
        return width
    #
    def _getHeightAt(self, column):
        actionData = self._subActionsDic[column]
        #
        count = len(actionData)
        return max(min(count, 32), 0)*self._uiItemHeight
    # Index
    def _updateSubIndexCount(self, column, value):
        self._subIndexCountDic[column] = int(value)
    #
    def _updateSubActions(self, column, subActions):
        self._subActionsDic[column] = subActions
    #
    def _updateSubRectPos(self, column, xPos, yPos):
        self._subRectPosDic[column] = xPos, yPos - column
    #
    def _updateSubRectSize(self, column, width, height):
        self._subRectWidthDic[column] = width
        self._subRectHeightDic[column] = height
    #
    def _updateMain(self, column, actionData):
        if actionData:
            self._initAt(column)
            self._updateSubActions(column, actionData)
            #
            self._setupActions(column, actionData)
    #
    def _updateSub(self, column, actionData):
        if actionData:
            self._initAt(column)
            self._updateSubActions(column, actionData)
            #
            self._setupSubActions(column)
            #
            self._updateSubGeometry(column)
    #
    def _setupActions(self, column, actionData):
        for data in actionData:
            widget = self._itemClass(self._widget)
            widget.setActionData(data)
            #
            self.addItem(column, widget)
    #
    def _setupSubActions(self, column):
        actionData = self._subActionsDic[column]
        for data in actionData:
            widget = self._itemClass(self._widget)
            widget.setActionData(data)
            #
            self.addSubItem(column, widget)
    #
    def _updateSubCurrent(self, column, itemModel):
        isChanged = False
        curItem = self._subCurItemDic.get(column, None)
        #
        if not itemModel == curItem:
            isChanged = True
        #
        if isChanged is True:
            if curItem is not None:
                curItem.setPressCurrent(False)
                curItem.setPressHovered(False)
                curItem.setCheckHovered(False)
            #
            itemModel.setPressCurrent(True)
            itemModel.setPressHovered(True)
            itemModel.setCheckHovered(True)
        #
        self._curPressChangeFlag = isChanged
        #
        self._subCurItemDic[column] = itemModel
        self._subCurIndexDic[column] = itemModel.index()
    #
    def _updateCheckItemsAt(self, column):
        [i._updateUiStyle() for i in self.subItemModelsAt(column) if i.isCheckEnable()]
    #
    def _updateScrollBarGeometry(self):
        pass
    #
    def _updateChildrenGeometry(self, column):
        if self._isTearable is True:
            xPos, yPos = self._subRectPosDic[column]
            side = self._uiSide
            #
            self._separateButton.show()
            self._separateButton.setGeometry(
                xPos + side, yPos - self._uiItemHeight,
                self._uiItemHeight, self._uiItemHeight
            )
    #
    def _updateSubItemModelPosAt(self, column, index):
        xPos, yPos = self._subRectPosDic[column]
        #
        x, y = xPos + 1, yPos + index*self._uiItemHeight + 1
        self._subItemPosDic[column][index] = x, y
    #
    def _updateSubItemModelsPos(self, column):
        count = self._subIndexCountDic.get(column, 0)
        if count > 0:
            for index in range(count):
                self._updateSubItemModelPosAt(column, index)
    #
    def _updateItemsGeometry(self, column):
        count = self._subIndexCountDic.get(column, 0)
        if count > 0:
            v = 0
            for index in range(count):
                itemModel = self._subItemDic[column][index]
                widget = itemModel.widget()
                #
                widget.show()
                #
                x, y = self._subItemPosDic[column][index]
                w, h = self._subRectWidthDic[column], self._uiItemHeight
                #
                widget.setGeometry(
                    x, y - v,
                    w, h
                )
                #
                itemModel = widget._itemModel
                itemModel.setItemSize(w, h)
    #
    def _updateRectGeometry(self, column):
        xPos, yPos = self._subRectPosDic[column]
        width, height = self._subRectWidthDic[column], self._subRectHeightDic[column]
        #
        self._subRectDic[column] = QtCore.QRect(
            xPos, yPos,
            width + 1, height + 1
        )
        self._subAbsRectDic[column] = QtCore.QRect(
            xPos, yPos,
            width + self._uiShadowRadius + 1, height + self._uiShadowRadius + 1
        )
        #
        self._titleRect.setRect(
            xPos + self._uiSide, yPos - self._uiItemHeight,
            width - self._uiSide*2, self._uiItemHeight
        )
        self._titleLine.setLine(
            xPos, yPos,
            xPos + width, yPos
        )
    #
    def _updateSubRectGeometry(self, column):
        preColumn = column - 1
        #
        xPos, yPos = self._subRectPosDic[column]
        width, height = self._subRectWidthDic[column], self._subRectHeightDic[column]
        #
        preWidth = self._subRectWidthDic.get(preColumn, -self._uiShadowRadius) + self._uiShadowRadius
        #
        if self._region == 0 or self._region == 2:
            x, y = xPos + preWidth, yPos
        else:
            x, y = xPos - width - self._uiShadowRadius - column, yPos
        #
        w, h = width, height
        #
        self._subRectDic[column] = QtCore.QRect(
            x, y,
            w + 1, h + 1
        )
        self._subAbsRectDic[column] = QtCore.QRect(
            x, y,
            w + self._uiShadowRadius + 1, h + self._uiShadowRadius + 1
        )
    #
    def _updateSubItemPosAt(self, column, index):
        preColumn = column - 1
        #
        xPos, yPos = self._subRectPosDic[column]
        width, height = self._subRectWidthDic[column], self._subRectHeightDic[column]
        #
        preWidth = self._subRectWidthDic.get(preColumn, -self._uiShadowRadius) + self._uiShadowRadius
        if self._region == 0 or self._region == 2:
            xPos = xPos + preWidth + column
        else:
            xPos = xPos - width - self._uiShadowRadius + 0
        #
        x, y = xPos, yPos + index*self._uiItemHeight + 1
        self._subItemPosDic[column][index] = x, y
    #
    def _updateSubItemsPos(self, column):
        for index in range(self._subIndexCountDic[column]):
            self._updateSubItemPosAt(column, index)
    #
    def _updateSubItemsGeometry(self, column):
        self._updateSubItemsPos(column)
        #
        count = self._subIndexCountDic[column]
        if count > 0:
            v = 0
            for index in range(count):
                itemModel = self._subItemDic[column][index]
                widget = itemModel.widget()
                #
                widget.show()
                #
                x, y = self._subItemPosDic[column][index]
                w, h = self._subRectWidthDic[column], self._uiItemHeight
                #
                widget.setGeometry(
                    x, y - v,
                    w, h
                )
                #
                itemModel = widget._itemModel
                itemModel.setItemSize(w, h)
    #
    def _updateGeometry(self, column):
        self._updateRectGeometry(column)
        self._updateItemsGeometry(column)
        self._updateChildrenGeometry(column)
        #
        self._subEnableDic[column] = True
    #
    def _updateSubGeometry(self, column):
        preColumn = column - 1
        preIndex = self._subCurIndexDic.get(preColumn)
        if preIndex in self._subItemPosDic[preColumn]:
            xPos, yPos = self._subItemPosDic[preColumn][preIndex]
            self._updateSubRectPos(column, xPos, yPos)
            width, height = self._getWidthAt(column), self._getHeightAt(column)
            self._updateSubRectSize(column, width, height)
            #
            self._updateSubRectGeometry(column)
            self._updateSubItemsGeometry(column)
            #
            self._subEnableDic[column] = True
    #
    def _columnAt(self, x):
        pass
    #
    def _indexAt(self, y):
        return int(y/self._uiItemHeight)
    #
    def _mapToSubRectPos(self, column, event):
        rect = self._subRectDic.get(column, None)
        if rect is not None:
            point = event.globalPos() - self.widget().mapToGlobal(self._subRectDic[column].topLeft())
            x, y = point.x(), point.y()
        else:
            x, y = 0, 0
        return x, y
    #
    def _clearSubCurItem(self, column):
        curItem = self._subCurItemDic.get(column, None)
        if curItem is not None:
            curItem.setPressCurrent(False)
            curItem.setPressHovered(False)
            curItem.setCheckHovered(False)
        #
        self._subCurItemDic[column] = None
        self._subCurIndexDic[column] = -1
    #
    def _clearHover(self):
        column = 0
        self._clearSubCurItem(column)
        #
        nexColumn = column + 1
        self._initAt(nexColumn)
        #
        self.widget().update()
    #
    def _hoverExecuteAction(self, event):
        pos = event.globalPos()
        column = 0
        nexColumn = column + 1
        #
        mainRect = self._subAbsRectDic.get(column)
        if mainRect is not None:
            if mainRect.contains(pos):
                x, y = self._mapToSubRectPos(column, event)
                index = self._indexAt(y)
                #
                self.setItemPressVisibleAt(column, index)
                #
                self._clearSubCurItem(nexColumn)
            else:
                subRect = self._subAbsRectDic.get(nexColumn, None)
                if subRect is not None:
                    if subRect.contains(pos):
                        x, y = self._mapToSubRectPos(nexColumn, event)
                        index = self._indexAt(y)
                        #
                        self.setSubItemCurrentAt(nexColumn, index)
                    else:
                        self._clearSubCurItem(nexColumn)
                else:
                    self._clearSubCurItem(column)
        #
        self.widget().update()
    #
    def _pressStartAction(self, event):
        self._pressFlag, self._dragFlag = True, False
        self._actionFlag = True
        #
        pos = event.globalPos()
        column = 0
        nexColumn = column + 1
        mainRect = self._subAbsRectDic.get(column)
        if mainRect is not None:
            if mainRect.contains(pos):
                x, y = self._mapToSubRectPos(column, event)
                index = self._indexAt(y)
                self.setSubItemPressAt(column, index)
            else:
                subRect = self._subAbsRectDic.get(nexColumn, None)
                if subRect is not None:
                    x, y = self._mapToSubRectPos(nexColumn, event)
                    index = self._indexAt(y)
                    self.setSubItemPressAt(nexColumn, index)
    #
    def _pressExecuteAction(self, event):
        self._pressFlag, self._dragFlag = False, True
        #
        column = self._curItemColumn
        x, y = self._mapToSubRectPos(column, event)
        index = self._indexAt(y)
        #
        self.setSubItemCheckAt(column, index)
    # noinspection PyUnusedLocal
    def _pressStopAction(self, event):
        if self._dragFlag is True:
            self.widget().actionAccepted.emit()
        else:
            if self._curPressAction is not None:
                self._curPressAction()
            elif self._curPressCommand is not None:
                exec self._curPressCommand
        #
        if self.widget()._shiftFlag is True:
            self._updateCheckItemsAt(self._curItemColumn)
        else:
            self.widget().close()
            self.widget().deleteLater()
        #
        self._pressFlag, self._dragFlag = False, False
    #
    def _initAt(self, column):
        def clearItems():
            items = self._subItemDic.get(column, None)
            if items:
                [i.widget().deleteLater() for i in items]
        #
        def clearVar():
            self._subEnableDic[column] = False
            #
            self._subRectDic[column] = None
            self._subAbsRectDic[column] = None
            self._subRectPosDic[column] = 0, 0
            self._subRectWidthDic[column] = 240
            self._subRectHeightDic[column] = 20
            #
            self._subIndexCountDic[column] = 0
            self._subItemDic[column] = []
            self._subItemPosDic[column] = {}
            #
            self._subCurIndexDic[column] = -1
            self._subCurItemDic[column] = None
            self._subActionsDic[column] = []
        #
        clearItems()
        clearVar()
    #
    def _drop(self, worldPos, deskRect):
        column = 0
        #
        xPos, yPos = worldPos.x(), worldPos.y()
        #
        maxWidth = deskRect.width()
        maxHeight = deskRect.height()
        #
        width, height = self._getWidthAt(column), self._getHeightAt(column)
        self._updateSubRectSize(column, width, height)
        #
        side, margin, shadowRadius = self._uiSide, self._uiMargin, self._uiShadowRadius
        #
        xOffset, yOffset = 0, 0
        #
        width_, height_ = width + margin*2 + side*2 + shadowRadius + 1, height + margin*2 + side*2 + shadowRadius + 1 + self.__titleHeight()
        #

        xP, yP, region = self.mtd_raw_position_2d.regionTo(
            position=(xPos, yPos),
            size=(width_, height_),
            maximumSize=(maxWidth, maxHeight),
            offset=(xOffset, yOffset)
        )
        self._region = region
        #
        if region == 0 or region == 1:
            _yP = yP - side
        else:
            _yP = yP + side + shadowRadius
        if region == 0 or region == 2:
            _xP = xP - margin*3
        else:
            _xP = xP + margin*3 + side + shadowRadius
        #
        self._uiBasicRect.setRect(
            _xP, _yP,
            width_, height_
        )
        self.widget().setGeometry(deskRect)
        #
        self.widget().show()
        #
        self.update()
    #
    def _updateShiftMode(self):
        self.widget()._uiBorderRgba = [(95, 95, 95, 255), (63, 127, 255, 255)][self.widget()._shiftFlag]
        self.widget().update()
    #
    def _shiftStopAction(self):
        if self._actionFlag is True:
            self.widget().deleteLater()
        #
        self._actionFlag = False
    #
    def update(self):
        column = 0
        xPos, yPos = self._uiBasicRect.x(), self._uiBasicRect.y()
        #
        side = self._uiSide
        margin = self._uiMargin
        #
        xPos, yPos = xPos + side + margin, yPos + margin + side + self.__titleHeight()
        self._updateSubRectPos(column, xPos, yPos)
        #
        self._updateSubItemModelsPos(column)
        #
        self._updateGeometry(column)
    #
    def setTitle(self, string):
        self._uiNameText = string
        #
        self.setTearable(True)
    #
    def setTearable(self, boolean):
        self._isTearable = boolean
    #
    def setActionData(self, actionData):
        column = 0
        self._updateMain(column, actionData)
    #
    def setAcceptAction(self, action):
        self._acceptAction = action
    #
    def addItem(self, column, widget):
        itemModel = widget._itemModel
        index = self._subIndexCountDic.get(column, 0)
        #
        itemModel.setViewModel(self)
        itemModel.setIndex(index)
        #
        self._subItemDic[column].append(itemModel)
        #
        self._updateSubItemPosAt(column, index)
        #
        index += 1
        self._updateSubIndexCount(column, index)
    #
    def addSubItem(self, column, widget):
        itemModel = widget._itemModel
        index = self._subIndexCountDic[column]
        #
        itemModel.setViewModel(self)
        itemModel.setIndex(index)
        #
        self._subItemDic[column].append(itemModel)
        #
        self._updateSubItemPosAt(column, index)
        #
        index += 1
        self._updateSubIndexCount(column, index)
    #
    def subItemModelAt(self, column, index):
        if self.isContainSubIndex(column, index):
            return self._subItemDic[column][index]
    #
    def subItemAt(self, column, index):
        itemModel = self.subItemModelAt(column, index)
        if itemModel is not None:
            return itemModel.widget()
    #
    def subItemModelsAt(self, column):
        return self._subItemDic[column]
    #
    def isContainSubIndex(self, column, index):
        count = self._subIndexCountDic.get(column, 0)
        if count > 0:
            return 0 <= index <= count - 1
        else:
            return False
    #
    def setItemPressVisibleAt(self, column, index):
        nexColumn = column + 1
        #
        enable = False
        actionData = []
        #
        self._curPressChangeFlag = False
        #
        itemModel = self.subItemModelAt(column, index)
        if itemModel is not None:
            self._updateSubCurrent(column, itemModel)
            #
            enable = itemModel.isExtendEnable()
            actionData = itemModel.itemActionData()
        #
        else:
            self._clearSubCurItem(column)
        #
        if enable is True:
            if self._curPressChangeFlag is True:
                self._initAt(nexColumn)
                #
                self._updateSub(nexColumn, actionData)
        else:
            self._initAt(nexColumn)
    #
    def setSubItemCurrentAt(self, column, index):
        itemModel = self.subItemModelAt(column, index)
        if itemModel is not None:
            self._updateSubCurrent(column, itemModel)
    #
    def setSubItemPressAt(self, column, index):
        itemModel = self.subItemModelAt(column, index)
        if itemModel is not None:
            self._curPressAction = itemModel.pressAction()
            self._curPressCommand = itemModel.pressCommand()
            if itemModel.isCheckEnable():
                self._dragStartChecked = not itemModel.isChecked()
                self._curItemColumn = column
                #
                self._updateCheckItemsAt(column)
    #
    def setSubItemCheckAt(self, column, index):
        itemModel = self.subItemModelAt(column, index)
        if itemModel is not None:
            if itemModel.isCheckEnable():
                isChecked = itemModel.isChecked()
                if not isChecked == self._dragStartChecked:
                    itemModel.setChecked(self._dragStartChecked)
                    #
                    self._updateCheckItemsAt(column)
            #
            self._updateSubCurrent(column, itemModel)
    #
    def setScrollBar(self, widget):
        self._vScrollBar = widget._vScrollBar
    #
    def setButton(self, widget):
        self._separateButton = widget._separateButton


# Choose Drop View
class QtAbc_ChooseDropviewModel(qtDefinition.QtDef_Widget):
    def _initAbcChooseDropviewModel(self):
        self._initDefWidget()
        #
        self._initAbcChooseDropviewModelAttr()
        self._initAbcChooseDropviewModelUi()
        self._initAbcChooseDropviewModelRect()
        self._initAbcChooseDropviewModelAction()
        self._initAbcChooseDropviewModelVar()
    #
    def _initAbcChooseDropviewModelAttr(self):
        self._itemClass = None
        #
        self._filterViewWidget, self._separateButton = None, None
        #
        self._isTearable = True
    #
    def _initAbcChooseDropviewModelUi(self):
        self._uiMainWidth, self._uiMainHeight = 240, 20
        #
        self._uiItemHeight = 20
        #
        self._uiMenuHeight = 24
        #
        self._uiButtonWidth, self._uiButtonHeight = 20, 20
        #
        self._uiIconKeyword = None
        #
        self._uiMaxItemCount = 10
        #
        self._uiMaxWidth, self._uiMinWidth = 480, 240
        self._uiMaxHeight, self._uiMinHeight = self._uiMaxItemCount*self._uiItemHeight + self._uiMenuHeight, self._uiMenuHeight
        #
        self._uiSide = 2
        self._gap = 16
        self._uiMargin = 8
        self._uiShadowRadius = 4
        #
        self._uiSpacing = 2
    #
    def _initAbcChooseDropviewModelRect(self):
        self._uiBasicRect, self._titleRect, self._uiCentralRect = QtCore.QRect(), QtCore.QRect(), QtCore.QRect()
    #
    def _initAbcChooseDropviewModelAction(self):
        self._curPressChangeFlag = False
    #
    def __connectUi(self, widget):
        self.setWidget(widget)
        self.setViewport(widget)
        self.setButton(widget)
    #
    def _initAbcChooseDropviewModelVar(self):
        self._region = 0
        #
        self._names = []
        #
        self._curPressItemIndex = -1
    #
    def _getUiWidth(self, strings):
        item = self._itemClass()
        texts = [i for i in strings if i]
        #
        widths = [item.fontMetrics().width(i) for i in texts]
        if widths:
            width = max(min(max(widths) + 48, self._uiMaxWidth), self._uiMinWidth)
        else:
            width = self._uiMinWidth
        return width
    #
    def _getUiHeight(self, strings):
        count = len(strings)
        if count:
            height = max(min(count*self._uiItemHeight + (count - 1)*self._uiSpacing + self._uiMenuHeight + 2, self._uiMaxHeight), self._uiMinHeight)
        else:
            height = self._uiMinHeight
        return height
    #
    def _updateViewportGeometry(self):
        xPos, yPos = self._pos
        #
        self._viewport.setGeometry(
            xPos + 1, yPos + 1,
            self._uiMainWidth, self._uiMainHeight - self._uiMenuHeight
        )
    #
    def _updateChildrenGeometry(self):
        if self._isTearable is True:
            xPos, yPos = self._pos
            w, h = self._uiMainWidth, self._uiMenuHeight
            #
            buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
            side, spacing = self._uiSide, self._uiSpacing
            #
            xPos += side
            yPos -= (h - 2)
            #
            self._filterViewWidget.show()
            w_ = w - buttonWidth - side
            self._filterViewWidget.setGeometry(
                xPos, yPos,
                w_, h
            )
            #
            xPos += (w_ + spacing)
            #
            self._separateButton.show()
            self._separateButton.setGeometry(
                xPos + (h - buttonWidth)/2, yPos + (h - buttonHeight)/2,
                buttonWidth, buttonHeight
            )
        #
        self._filterViewWidget.setNameText(str(len(self._names)).zfill(4))
    #
    def _updateGeometry(self):
        self._updateViewportGeometry()
        self._updateChildrenGeometry()
    #
    def _updateCurrent(self):
        self._viewport._viewModel.setCurrentVisibleIndex(self._curPressItemIndex)
        #
        self._viewport._viewModel.setVisibleCurrent()
        self._viewport._viewModel.setCurrentVisibleCeiling()
        #
        self._viewport._viewModel._curPressChangeFlag = False
    #
    def _setupItems(self):
        if self._names:
            for index, string in enumerate(self._names):
                item = self._itemClass()
                self.addItem(item)
                #
                item.setName(string)
                item.setIcon(self._uiIconKeyword)
    #
    def _drop(self, worldPos, deskRect):
        xPos, yPos = worldPos.x(), worldPos.y()
        #
        maxWidth = deskRect.width()
        maxHeight = deskRect.height()
        #
        width = self._getUiWidth(self._names)
        self._uiMainWidth = width
        height = self._getUiHeight(self._names)
        self._uiMainHeight = height
        #
        side = self._uiSide
        margin = self._uiMargin
        shadowRadius = self._uiShadowRadius
        #
        xOffset = 0
        yOffset = 0
        #
        width_ = width + margin*2 + side*2 + shadowRadius + 1
        height_ = height + margin*2 + side*2 + shadowRadius + 1
        #
        xP, yP, region = self.mtd_raw_position_2d.regionTo(
            position=(xPos, yPos),
            size=(width_, height_),
            maximumSize=(maxWidth, maxHeight),
            offset=(xOffset, yOffset)
        )
        self._region = region
        #
        if region == 0 or region == 1:
            _yP = yP - side
        else:
            _yP = yP + side + shadowRadius
        if region == 0 or region == 2:
            _xP = xP - margin*3
        else:
            _xP = xP + margin*3 + side + shadowRadius
        #
        self._uiBasicRect.setRect(
            _xP, _yP,
            width_, height_
        )
        self.widget().setGeometry(deskRect)
        #
        self.widget().show()
        #
        self.update()
    #
    def update(self):
        xPos, yPos = self._uiBasicRect.x(), self._uiBasicRect.y()
        #
        side = self._uiSide
        margin = self._uiMargin
        #
        self._pos = xPos + side + margin, yPos + margin + side + self._uiMenuHeight
        #
        self._setupItems()
        #
        self._updateGeometry()
        #
        self._updateCurrent()
        #
        self._viewport.viewModel()._updateVisibleItemsPos()
        self._viewport.viewModel().update()
    #
    def addItems(self, strings, iconKeyword):
        self._names = strings
        self._uiIconKeyword = iconKeyword
    #
    def addItem(self, widget):
        self._viewport.addItem(widget)
    #
    def item(self):
        return self._viewport._viewModel.currentItem()
    #
    def index(self):
        return self._viewport._viewModel._curPressItemIndex
    #
    def name(self):
        item = self.item()
        if item is not None:
            return item.name()
    #
    def setCurrentIndex(self, index):
        self._curPressItemIndex = int(index)
    #
    def setViewport(self, widget):
        self._viewport = widget._viewport
    #
    def setButton(self, widget):
        self._filterViewWidget, self._separateButton = widget._filterViewWidget, widget._separateButton
        self._viewport.setFilterConnect(self._filterViewWidget)


#
class QtAbc_TabitemModel(qtDefinition.QtDef_ItemModel):
    def _initAbcTabitemModel(self):
        self._initItemModelDef()
        self._initAbcTabitemModelAttr()
    #
    def _initAbcTabitemModelAttr(self):
        self._tabBar = None
        self._tabWidget = None
        #
        self._menuButton = None
        self._closeButton = None
        #
        self._tabDir = qtCore.Vertical
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._menuButton = widget._menuButton
        self._closeButton = widget._closeButton
    #
    def setTabBar(self, tabBar):
        self._tabBar = tabBar
    #
    def tabBar(self):
        return self._tabBar
    #
    def tabPosition(self):
        return self.tabBar().viewModel().tabPosition()
    #
    def tabWidget(self):
        return self._tabWidget
    #
    def setActionData(self, actionData):
        self._menuButton.setActionData(actionData)
    #
    def setIcon(self, iconKeyword, iconWidth=24, iconHeight=24, frameWidth=32, frameHeight=32):
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


# Tab Bar
class QtAbc_TabbarModel(
    qtDefinition.QtDef_ViewModel,
    qtDefinition.QtDef_TabbarWidget,
):
    def _initAbcTabbarModel(self):
        self._initDefViewModel()
        self._initDefTabbarWidget()
    #
    def _updateLayoutAttr(self):
        if self.tabPosition() == qtCore.South or self.tabPosition() == qtCore.North:
            self.setItemRowCount(1)
            self.setItemColumnCount(self._getRowCount(self._itemIndexCount, self._itemRowCount))
        else:
            self.setItemColumnCount(1)
            self.setItemRowCount(self._getRowCount(self._itemIndexCount, self._itemColumnCount))
    #
    def _updateAbsSize(self):
        w, h = self._gridSize()
        self._absWidth, self._absHeight = self._itemColumnCount*w, self._itemRowCount*h
    # View
    def _updateViewSize(self):
        self._viewWidth = [self._absWidth, self._viewportWidth][self.isHScrollable()]
        self._viewHeight = [self._absHeight, self._viewportHeight][self.isVScrollable()]
    #
    def _updateScrollState(self):
        width, height = self.width(), self.height()
        absWidth, absHeight = self._absWidth, self._absHeight
        #
        if self.tabPosition() == qtCore.South or self.tabPosition() == qtCore.North:
            self.setHScrollable(absWidth > width)
            self._hScrollMaximum = absWidth - width
        else:
            self.setVScrollable(absHeight > height)
            self._vScrollMaximum = absHeight - height
        #
        self._hScrollValue, self._vScrollValue = self.getClampScrollValue(self._hScrollValue, self._vScrollValue)
    #
    def setWidget(self, widget):
        self._widget = widget
    #
    def setScrollValue(self, x, y):
        xValue, yValue = self.getClampScrollValue(x, y)
        #
        self._hScrollValue, self._vScrollValue = xValue, yValue
        #
        self._widget.valueChanged.emit()
        #
        self.update()
    #
    def itemIndexLoc(self, x, y):
        w, h = self.itemSize()
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            return self._columnLoc(x, w)
        else:
            return self._rowLoc(y, h)


# Tab View
class QtAbc_TabviewModel(qtDefinition.QtDef_TabviewWidget):
    def _initAbcTabviewModel(self):
        self._initDefTabviewWidget()


# Window
class QtAbc_WindowModel(qtDefinition.QtDef_WindowModel):
    def _initAbcWindowModel(self):
        self._initDefWindowModel()
        #
        self._initAbcWindowModelAttr()
        self._initAbcWindowModelAction()
        self._initAbcWindowModelRect()
        self._initAbcWindowModelUi()
        self._initAbcWindowModelVar()
    #
    def _initAbcWindowModelAttr(self):
        pass
    #
    def _initAbcWindowModelAction(self):
        pass
    #
    def _initAbcWindowModelRect(self):
        pass
    #
    def _initAbcWindowModelUi(self):
        pass
    #
    def _initAbcWindowModelVar(self):
        pass
    #
    def _updateWindowActiveState(self):
        self._uiResizeIcon = self._toLxOsIconFile(self._uiResizeIconKeyword + ['', 'Active'][self.isWindowActive()])
        self._updateWidgetState()
    #
    def _progressValueChangeAction(self):
        pass
    #
    def _addQuitConnectMethod(self, method):
        self._quitConnectMethodLis.append(method)
    #
    def setMaxProgressValue(self, value):
        if value > 0:
            self.setPercentEnable(True)
            self._uiMaxProgressValue = value
            self._uiProgressValue = 0
            #
            self._progressBar.setRange(0, 10)
        else:
            self.setPercentEnable(False)
    #
    def maxProgressValue(self):
        return self._uiMaxProgressValue
    #
    def setProgressValue(self, value, maxValue=None):
        if maxValue is not None:
            self.setMaxProgressValue(maxValue)
        #
        self._uiProgressValue = value
        #
        self._progressBar.setProperty(
            'value',
            int((float(value) / float(self._uiMaxProgressValue)) * 10)
        )
        #
        self._progressValueChangeAction()
    #
    def progressValue(self):
        return self._uiProgressValue
    #
    def updateProgress(self):
        value = self._uiProgressValue
        value += 1
        #
        self.setProgressValue(value)
    #
    def uiShow(self, pos=None, size=None):
        if size is not None:
            width, height = size
        else:
            width, height = self.defaultSize()

        parent = self.widget().parent()
        if parent:
            parentWidth, parentHeight = parent.width(), parent.height()
            xOf, yOf = parent.pos().x(), parent.pos().y()
        else:
            deskRect = qtCore.getDesktopPrimaryRect()
            parentWidth, parentHeight = deskRect.width(), deskRect.height()
            xOf, yOf = 0, 0

        if pos is not None:
            xPos, yPos = pos[0] + xOf, pos[1] + yOf
        else:
            xPos, yPos = (parentWidth - width)/2 + xOf, (parentHeight - height)/2 + yOf

        self.widget().setGeometry(
            max(xPos, 0), max(yPos, 0), width, height
        )
        self.widget().show()
    #
    def uiQuit(self):
        self.widget().closed.emit()
        #
        self._countdownCloseTimer.stop()
        self._progressTimer.stop()
        #
        if self._quitConnectMethodLis:
            for i in self._quitConnectMethodLis:
                i()
        #
        self._widget.close()
        self._widget.deleteLater()
        #
        qtCore.quitUi()
    #
    def setCountdownClose(self, value=5):
        self.setProgressValue(
            self._uiMaxProgressValue, self._uiMaxProgressValue
        )
        self._countdownStep = value + 1
        self._countdownCloseTimer.start(1000)
    #
    def setCountdownCloseStop(self):
        self._countdownCloseTimer.stop()
        self.setStatusText(None)
    #
    def _countdownCloseStartAction(self):
        self._countdownStep -= 1
        if self._countdownStep == 0:
            self.uiQuit()
        else:
            string = 'Close Window in {} Second'.format(self._countdownStep)
            self.setStatusText(string)


#
class QtAbc_ChartModel(qtDefinition.QtDef_PressWidget):
    def _initAbcChartModel(self):
        self._initDefPressWidget()
        #
        self._initAbcChartModelAttr()
        self._initAbcChartModelRect()
        self._initAbcChartModelUi()
    #
    def _initAbcChartModelAttr(self):
        self._chartDatum = None
        self._drawDatum = None
        #
        self._uiMargins = 0, 0, 0, 0
        #
        self._hAlign = qtCore.AlignHCenter
        self._vAlign = qtCore.AlignVCenter
    #
    def _initAbcChartModelRect(self):
        self._uiImageRect = QtCore.QRect(-20, -20, 1, 1)
        self._uiImageClipPath = None
    #
    def _initAbcChartModelUi(self):
        self._uiSide = 32
        #
        self._uiImage = None
        #
        self._uiImageWidget, self._uiImageHeight = 32, 32
    #
    def _clearHover(self):
        self._pressHoverPos = 0, 0
        #
        self._updateWidgetState()
    #
    def _updateHoverLoc(self, x, y):
        self._pressHoverPos = x, y
        #
        self._updateWidgetState()
    #
    def _updatePressLoc(self, x, y):
        pass
    #
    def _updateDragPressLoc(self, x, y):
        pass
    #
    def _hoverStartAction(self, event):
        event.ignore()
    #
    def _hoverExecuteAction(self, event):
        x, y = self._getEventPos(event)
        self._updateHoverLoc(x, y)
        event.ignore()
    #
    def _hoverStopAction(self, event):
        self._clearHover()
        event.ignore()
    #
    def _pressStartAction(self, event):
        event.ignore()
    #
    def _pressExecuteAction(self, event):
        event.ignore()
    #
    def _pressStopAction(self, event):
        event.ignore()
    #
    def setChartDatum(self, datum):
        self._chartDatum = datum
        self.update()
    #
    def chartDatum(self):
        return self._chartDatum
    #
    def setDrawDatum(self, datum):
        self._drawDatum = datum
    #
    def drawDatum(self):
        return self._drawDatum
    #
    def setImage(self, image):
        if self.isOsExistsFile(image):
            self._uiImage = image
        else:
            self._uiImage = None
    #
    def image(self):
        return self._uiImage
    #
    def imageRect(self):
        return self._uiImageRect
    #
    def imageClipPath(self):
        return self._uiImageClipPath
    #
    def setImageSize(self, w, h):
        self._uiImageWidget, self._uiImageHeight = w, h
    #
    def imageSize(self):
        return self._uiImageWidget, self._uiImageHeight
    #
    def setHAlign(self, align):
        self._hAlign = align
        self.update()
    #
    def setVAlign(self, align):
        self._vAlign = align
        self.update()
    #
    def setSide(self, value):
        self._uiSide = value
