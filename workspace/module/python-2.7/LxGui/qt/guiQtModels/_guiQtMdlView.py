# coding:utf-8
from LxBasic import bscMethods
#
from LxGui.qt import qtCore, guiQtMdlAbs

#

#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
CLS_point = QtCore.QPoint
CLS_line = QtCore.QLine
CLS_rect = QtCore.QRect


#
class QtScrollareaModel(guiQtMdlAbs.AbsGuiQtScrollareaMdl):
    def __init__(self, widget):
        self._initAbsGuiQtScrollareaMdl(widget)


#
class QtPresetviewModel(guiQtMdlAbs.AbsQtWgtViewModel):
    def __init__(self, widget):
        self._initAbsQtWgtViewModel(widget)
        #
        self.__overrideItemAttr()
    #
    def __overrideItemAttr(self):
        self._itemMode = qtCore.TreeMode
        self._wgt__margins = 2, 2, 2, 2
        self._uiSpacing = 2
        #
        self._uiExpandFrameWidth, self._uiExpandFrameHeight = 20.0, 20.0
        #
        self.setPressEnable(False)
        self.setCheckEnable(True)
        #
        self._isHScrollEnable, self._isVScrollEnable = True, True
        #
        self.setItemSize(20, 20)


#
class QtTreeviewModel(guiQtMdlAbs.AbsQtWgtViewModel):
    def __init__(self, widget):
        self._initAbsQtWgtViewModel(widget)
        #
        self.__overrideItemAttr()
    #
    def __overrideItemAttr(self):
        self._itemMode = qtCore.TreeMode
        self._wgt__margins = 2, 2, 2, 2
        self._uiSpacing = 2
        #
        self._uiExpandFrameWidth, self._uiExpandFrameHeight = 20.0, 20.0
        #
        self._isHScrollEnable, self._isVScrollEnable = True, True
        #
        self.setItemSize(20, 20)


#
class QtCheckviewModel(guiQtMdlAbs.AbsQtWgtViewModel):
    def __init__(self, widget):
        self._initAbsQtWgtViewModel(widget)
        #
        self.__overrideItemAttr()
    #
    def __overrideItemAttr(self):
        self._itemMode = qtCore.FormMode
        self._isCheckEnable = True
    #
    def _updateWidgetGeometry(self):
        w, h = self._gridSize()
        self._widget.setMinimumHeight(self._visibleRowCount*h + self._wgt__margins[1] + self._wgt__margins[3])
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._updateWidgetGeometry()
        self._gui_qt__mdl__set_viewport_geometry_update_()
        self._updateVisibleItemsGeometry()


#
class QtGridviewModel(guiQtMdlAbs.AbsQtWgtViewModel):
    def __init__(self, widget):
        self._initAbsQtWgtViewModel(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        self._isHScrollEnable, self._isVScrollEnable = False, True
        #
        self._itemMode = qtCore.IconMode
        #
        self._isSingleSelection = True
        #
        self._isListMode, self._isIconMode, self._isDetailMode = False, False, True
        self._isListModeEnable, self._isIconModeEnable, self._isDetailModeEnable = False, False, True
        #
        self._isIndexSort, self._isNameSort = True, False
        #
        self._trackWidth, self._trackHeight = 20, 20
        #
        self._itemListModeSize = 32, 32
        self._itemIconModeSize = 32, 32
        self._itemDetailSize = 32, 32
        #
        self._wgt__margins = 2, 2, 2, 2
        self._uiSpacing = 2
    #
    def _updateFilterColorBy(self, indices, color):
        if indices:
            for i in indices:
                itemModel = self.itemModelAt(i)
                if itemModel is not None:
                    itemModel.setFilterColor(color)
    #
    def _setItemSize(self, width, height):
        # Width & Height Minimum 1
        self._uiItemWidth, self._uiItemHeight = max(int(width), 1), max(int(height), 1)
        w, h = self._gridSize()
        #
        self._vScrollBar._viewModel.setBasicScrollValue(h)
        self._vScrollBar._viewModel.setRowScrollValue(h)
        #
        self.update(force=True)
        #
        self._vScrollBar.viewModel()._updateValueByPercent()
        #
        self._updateCurVisibleColumn(), self._updateCurVisibleRow()
        #
        [i.setItemSize(self._uiItemWidth, self._uiItemHeight) for i in self.itemModels()]
        [i.setItemMode(self._itemMode) for i in self.itemModels()]
    #
    def _getItemPosLoc(self, x, y, v, column, row):
        w, h = self._gridSize()
        return x - column*w, y + v - row*h
    #
    def _updateSortLis(self, index, reverse=False, force=False):

        self._topItemModelSortKeyLis.sort(key=lambda x: bscMethods.String.toNumberEmbeddedList(x[index]), reverse=reverse)
        #
        self._updateTopItemModelIndexSortLis()
        self._updateVisibleItemModelIndexLisByVisible(ignoreHidden=force)
        #
        self.update()
    #
    def isListMode(self):
        if self._isListModeEnable:
            return self._isListMode
        else:
            return None
    #
    def setListMode(self):
        if self._isListModeEnable:
            self._itemMode = qtCore.ListMode
            #
            self._setItemSize(*self._itemListModeSize)
            self._isListMode, self._isIconMode, self._isDetailMode = True, False, False
    #
    def isIconMode(self):
        if self._isIconModeEnable:
            return self._isIconMode
        else:
            return None
    #
    def setIconMode(self):
        if self._isIconModeEnable:
            self._itemMode = qtCore.IconMode
            #
            self._setItemSize(*self._itemIconModeSize)
            self._isListMode, self._isIconMode, self._isDetailMode = False, True, False
    #
    def isDetailMode(self):
        if self._isDetailModeEnable:
            return self._isDetailMode
        else:
            return None
    #
    def setDetailMode(self):
        if self._isDetailModeEnable:
            self._itemMode = qtCore.IconMode
            #
            self._setItemSize(*self._itemDetailSize)
            self._isListMode, self._isIconMode, self._isDetailMode = False, False, True
    #
    def isSortByIndex(self):
        return self._isIndexSort
    #
    def setSortByIndex(self, force=False):
        self._isIndexSort, self._isNameSort = True, False
        #
        self._updateSortLis(0, force=force)
    #
    def isSortByName(self):
        return self._isNameSort
    #
    def setSortByName(self, force=False):
        self._isIndexSort, self._isNameSort = False, True
        #
        self._updateSortLis(1, force=force)
    #
    def setSelectAll(self):
        if not self._isSingleSelection:
            [i.setChecked(True) for i in self.itemModels()]
    #
    def setSelectClear(self):
        if not self._isSingleSelection:
            [i.setChecked(False) for i in self.itemModels()]
    #
    def setSingleSelectionEnable(self, boolean):
        itemModels = self.itemModels()
        #
        self._isSingleSelection = boolean
        #
        if itemModels:
            [i.setCheckEnable(not self._isSingleSelection) for i in itemModels if i is not None]
    # Width & Height Minimum 1
    def setAbcObjItemWidgetSize(self, width, height):
        self._itemDetailSize = max(int(width), 1), max(int(height), 1)
    # Width & Height Minimum 1
    def setItemListModeSize(self, width, height):
        self._itemListModeSize = max(int(width), 1), max(int(height), 1)
        #
        self._isListModeEnable = True
    # Width & Height Minimum 1
    def setItemIconModeSize(self, width, height):
        self._itemIconModeSize = max(int(width), 1), max(int(height), 1)
        #
        self._isIconModeEnable = True
    #
    def setViewframe(self, widget):
        self._viewframe = widget._viewframe
    #
    def setItemSelectAt(self, index):
        pass
    #
    def setListModeEnable(self, boolean):
        self._itemMode = [qtCore.IconMode, qtCore.ListMode][boolean]
    #
    def isMaximum(self):
        return self._vScrollBar._viewModel.isMaximum()
    #
    def isMinimum(self):
        return self._vScrollBar._viewModel.isMinimum()
