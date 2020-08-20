# coding:utf-8
from .. import guiQtMdlAbs, qtCore


class QtItemModel(guiQtMdlAbs.AbsGuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)


class QtIconbuttonModel(guiQtMdlAbs.AbsGuiQtIconbuttonMdl):
    def __init__(self, *args):
        self._initAbsGuiQtIconbuttonMdl(*args)


# Text Brower Model
class QtTextbrowerModel(guiQtMdlAbs.AbsGuiQtTextbrowerMdl):
    def __init__(self, widget):
        self._initAbsGuiQtTextbrowerMdl(widget)


class QtActionViewportModel(guiQtMdlAbs.AbsGuiQtActionViewportMdl):
    CLS_gui_qt__mdl_obj__rect = qtCore.QtCore.QRect

    def __init__(self, *args):
        self._initAbsQtActionDropviewMdl(*args)


class QtEnablebuttonModel(guiQtMdlAbs.AbsGuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideItemAttr()
    #
    def __overrideItemAttr(self):
        self._isCheckEnable = True
        self._isCheckButton = True
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
            self._updateQtCheckStyle()


class QtCheckbuttonModel(guiQtMdlAbs.AbsGuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideItemAttr()
    #
    def __overrideItemAttr(self):
        self._isCheckEnable = True
        self._isCheckButton = True
        self._isOverrideIconEnable = False
        #
        self._uiCheckIconKeyword = 'svg_basic/filterunchecked'
        self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
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
            self._gui_qt__mdl__name_str_Rect.setRect(
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
        self._updateQtCheckStyle()
        self._gui_qt__set_press_style_update_()
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
            self._updateQtCheckStyle()
    #
    def setCheckIcon(self, iconKeywordStr):
        self._isOverrideIconEnable = True
        self._uiCheckIconKeyword = iconKeywordStr
        self._uiCheckIcon = qtCore._toLxOsIconFile(iconKeywordStr)
    #
    def _setQtCheckStyle(self, state):
        if state is qtCore.UncheckableState:
            if self._isOverrideIconEnable is False:
                self._uiCheckIconKeyword = ['svg_basic/filteruncheckable', 'svg_basic/radiobuttonuncheckable'][self._isAutoExclusive]
                self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
            else:
                self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword + 'off')
            #
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
            self.widget()._uiFontItalic = True
        else:
            r, g, b, a = 255, 255, 255, 255
            if state is qtCore.CheckedState:
                if self._isOverrideIconEnable is False:
                    self._uiCheckIconKeyword = ['svg_basic/filterchecked', 'svg_basic/radiouuttonchecked'][self._isAutoExclusive]
                else:
                    self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword + 'cur')
                #
                self.widget()._wgt__name_rgba = [(r*.75, g*.75, b*.75, a), (r, g, b, a)][self.isCheckHovered()]
            elif state is qtCore.UncheckedState:
                if self._isOverrideIconEnable is False:
                    self._uiCheckIconKeyword = ['svg_basic/filterunchecked', 'svg_basic/radiobuttonunchecked'][self._isAutoExclusive]
                else:
                    self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
                #
                self.widget()._wgt__name_rgba = [(r*.5, g*.5, b*.5, a), (r*.75, g*.75, b*.75, a)][self.isCheckHovered()]
            #
            if self._isOverrideIconEnable is False:
                self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])
            #
            self.widget()._uiFontItalic = False


# Filter Enter Label Model
class QtFilterLineModel(guiQtMdlAbs.AbsGuiQtFilterLineMdl):
    CLS_gui_qt__mdl_obj__line = qtCore.QtCore.QLine
    CLS_gui_qt__mdl_obj__rect = qtCore.QtCore.QRect

    def __init__(self, *args):
        self._initAbsGuiQtFilterLineMdl(*args)
