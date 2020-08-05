# coding:utf-8
import types
#
import math
#
from LxBasic import bscMethods
#
from LxGui.qt import guiQtObjAbs, qtAction, qtCore

#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore


# Item Model
class Abs_GuiQtItemMdl(
    guiQtObjAbs.Abs_GuiQtItemObj,
    guiQtObjAbs.Abs_GuiQtValueLineObj
):
    def _initAbsGuiQtItemMdl(self, widget):
        self._initAbsGuiQtItemObj()
        self._initAbsGuiQtValueLineObj()
        #
        self.setWidget(widget)
    #
    def _updateWidgetGeometry(self):
        pass
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
        indexWidth = self._gui_qt__mdl__index_str_Width
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
            self._gui_qt__mdl__set_color_rect_update_(xPos, yPos)
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
            self._gui_qt__mdl__index_str_Rect.setRect(
                width - indexWidth - self._uiShadowRadius - self._uiSide, yPos,
                indexWidth, frameHeight
            )
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._gui_qt__mdl__set_rect_geometry_update_()
        #
        self._updateWidgetState()
    # Hover
    def _gui_qt__set_enter_event_update_(self, event):
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
    def _gui_qt__set_leave_event_update_(self, event):
        if self._isEventOverrideEnable is True:
            self.update()
            event.ignore()
        else:
            self.setPressHovered(False)
            #
            if self.isCheckButton():
                self.setCheckHovered(False)
            #
            self.update()
            event.ignore()
    #
    def _gui_qt__mdl__set_mouse_move_event_update_(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            event.ignore()
    #
    def _gui_qt__mdl__set_mouse_press_event_update_(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            x, y = self._gui_qt__get_event_pos_(event)
            # Flag
            self._pressFlag, self._dragFlag = True, False
            # Check ( Check Emit Send First )
            self._checkClickSwitchAction()
            # Click
            self._clickedAction()
            #
            self._gui_qt__mdl__set_geometry_update_()
            self._gui_qt__set_press_style_update_()
            #
            if self.isIconRectContain((x, y)):
                event.accept()
            else:
                event.ignore()
    #
    def _gui_qt__mdl__set_mouse_press_move_event_update_(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            x, y = self._gui_qt__get_event_pos_(event)
            # Flag
            self._pressFlag, self._dragFlag = False, True
            #
            self._gui_qt__mdl__set_geometry_update_()
            self._gui_qt__set_press_style_update_()
            #
            if self.isIconRectContain((x, y)):
                event.accept()
            else:
                event.ignore()
    #
    def _gui_qt__mdl__set_mouse_release_event_update_(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            x, y = self._gui_qt__get_event_pos_(event)
            # Action
            self._releasedAction()
            # Flag
            self._pressFlag, self._dragFlag = False, False
            #
            self._gui_qt__mdl__set_geometry_update_()
            self._gui_qt__set_press_style_update_()
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

    # override
    def _extendPressCurrentAction(self):
        parentItemModels = self.parentItemModels()
        if parentItemModels:
            [i.setSubSelected(self.isPressCurrent()) for i in parentItemModels]

    # override
    def _extendPressSelectAction(self):
        parentItemModels = self.parentItemModels()
        if parentItemModels:
            if self.isSelected():
                [i.setSubSelected(True) for i in parentItemModels]
            else:
                [i.setSubSelected(False) for i in parentItemModels if not i.hasSelectedChildren()]
    #
    def _updateUiStyle(self):
        self._gui_qt__set_press_style_update_()
        self._updateQtExpandStyle()
        self._updateQtCheckStyle()
    #
    def update(self):
        self._gui_qt__mdl__set_geometry_update_()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._pressedTimer = qtCore.CLS_timer(self._widget)
        self._pressedTimer.timeout.connect(self._pressedAction)
    #
    def filterColor(self):
        if self.isColorEnable():
            return self.widget()._wgt__color__background_rgba
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


class Abs_GuiQtValueLineMdl(Abs_GuiQtItemMdl):
    def _initAbsGuiQtValueLineMdl(self, *args):
        widget = args[0]

        self._initAbsGuiQtItemMdl(widget)
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
        self._uiCheckIconKeyword = 'svg_basic/boxunchecked'
        self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
        explainWidth = self._gui_qt__mdl__name_str_Width
        if self.nameText() is not None:
            self._gui_qt__mdl__name_str_Rect.setRect(
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
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
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
            xPos += self._gui_qt__mdl__name_str_Width
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
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
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
                self._setQtEnterStyle(qtCore.EnterState)
            else:
                self._setQtEnterStyle(qtCore.UnenterState)
        else:
            self._setQtEnterStyle(qtCore.NormalState)
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
        self._gui_qt__mdl__set_rect_geometry_update_()
        #
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
        self._updateButtonVisible()
        #
        self._updateWidgetState()
    #
    def setNameString(self, string):
        if string is not None:
            self._gui_qt__mdl__name_str_ = unicode(string)
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
        self._pressedTimer = qtCore.CLS_timer(self._widget)
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
    def _setQtEnterStyle(self, state):
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
            self._uiCheckIconKeyword = ['svg_basic/boxuncheckable', 'svg_basic/radiouncheckable'][self.isAutoExclusive()]
            self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword)
        else:
            if state is qtCore.CheckedState:
                self._uiCheckIconKeyword = ['svg_basic/boxchecked', 'svg_basic/radiochecked'][self.isAutoExclusive()]
            elif state is qtCore.UncheckedState:
                self._uiCheckIconKeyword = ['svg_basic/boxunchecked', 'svg_basic/radiounchecked'][self.isAutoExclusive()]
            #
            self._uiCheckIcon = qtCore._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])


class Abs_GuiQtIconbuttonMdl(Abs_GuiQtItemMdl):
    def _initAbsGuiQtIconbuttonMdl(self, *args):
        widget = args[0]

        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        pass
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
            self._gui_qt__mdl__name_str_Rect.setRect(
                xPos, yPos,
                width - xPos, self._uiFrameHeight
            )
    #
    def _gui_qt__set_press_style_update_(self):
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
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
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
    #
    def acceptPressCommand(self):
        if self._pressCommand is not None:
            if bscMethods.MayaApp.isActive():
                # noinspection PyUnresolvedReferences
                import maya.mel as mel
                mel.eval(self._pressCommand)
            else:
                if bscMethods.OsPath.isFile(self._pressCommand):
                    pass
                else:
                    exec eval(self._pressCommand)
        #
        self.setPressHovered(False)


class Abs_GuiQtIconViewitemMdl(Abs_GuiQtItemMdl):
    def _initAbsGuiQtIconViewitemMdl(self, *args):
        widget = args[0]

        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        pass
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
            boolean = self.isPressed()
            self.iconRect().setRect(
                xPos + (self._uiFrameWidth - self._uiIconWidth)/2 + [0, 1][boolean], yPos + (self._uiFrameHeight - self._uiIconHeight)/2 + [0, 1][boolean],
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
            self._gui_qt__mdl__name_str_Rect.setRect(
                xPos, yPos,
                width - xPos, self._uiFrameHeight
            )
    #
    def _gui_qt__set_press_style_update_(self):
        if self.isPressEnable():
            if self.isPressable():
                self._setQtPressStyle(qtCore.NormalState)
                #
                self._updateQtPressStatus()
            else:
                self._setQtPressStyle(qtCore.UnpressableState)
        #
        self._gui_qt__mdl__set_rect_geometry_update_()

        self._updateWidgetState()
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            if self._uiIconKeyword is not None:
                self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + 'off')
            #
            self.widget().update()
            #
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
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
    #
    def acceptPressCommand(self):
        if self._pressCommand is not None:
            if bscMethods.MayaApp.isActive():
                # noinspection PyUnresolvedReferences
                import maya.mel as mel
                mel.eval(self._pressCommand)
            else:
                if bscMethods.OsPath.isFile(self._pressCommand):
                    mod = bscMethods.PyLoader.loadFile(self._pressCommand)
                    # mod.run()
                else:
                    exec eval(self._pressCommand)
        #
        self.setPressHovered(False)


class Abs_GuiQtPressbuttonMdl(Abs_GuiQtItemMdl):
    def _initAbsGuiQtPressbuttonMdl(self, *args):
        widget = args[0]
        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        self._uiSide = 4
        self._uiFrameWidth, self._uiFrameHeight = 24, 24
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side = self._uiSide
        #
        frameWidth, frameHeight = self.frameSize()
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
        if self.isColorEnable():
            self._gui_qt__mdl__set_color_rect_update_(xPos, yPos, frameSize=(frameWidth, frameHeight), offset=(xOffset, yOffset))
            xPos += frameWidth
        else:
            xPos += side
        # Icon
        if self.icon() is not None:
            self._gui_qt__mdl__set_icon_rect_update_(xPos, yPos, frameSize=(frameWidth, frameHeight), offset=(xOffset, yOffset))
            if self.extendIcon() is not None:
                self.extendIconRect().setRect(
                    xPos + (self._uiExtendFrameWidth - self._uiExtendIconWidth)/2, yPos + (self._uiExtendFrameHeight - self._uiExtendIconHeight)/2,
                    self._uiExtendIconWidth, self._uiExtendIconHeight
                )
            xPos += frameWidth
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
                self.widget()._wgt__background_rgba = 55, 55, 55, 255
            else:
                if status is qtCore.NormalStatus:
                    self.widget()._wgt__background_rgba = [(79, 79, 79, 255), (119, 119, 119, 255)][self.isPressHovered()]
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
                    self.widget()._wgt__background_rgba = [(r*.5, g*.5, b*.5, 255), (r*.75, g*.75, b*.75, 255)][self.isPressHovered()]
    #
    def _setUiPercentStatus(self, percent):
        if self.isPercentable():
            if self._valueMaximum > 0:
                if percent == 1:
                    r, g, b = 64, 255, 127
                else:
                    r, g, b = bscMethods.Color.hsv2rgb(45 * percent, 1, 1)
                #
                self.widget()._uiPercentValueRgba = [(r * .5, g * .5, b * .5, 255), (r * .75, g * .75, b * .75, 255)][self.isPressHovered()]
        else:
            self.widget()._uiPercentValueRgba = 79, 79, 79, 255
    #
    def _gui_qt__set_press_style_update_(self):
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
            self.widget()._wgt__background_rgba = 55, 55, 55, 255
            self.widget()._wgt__border_rgba = 63, 63, 63, 255
            #
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
            #
            self.widget()._wgt__border_style = 'inset'
            #
            self.widget()._uiFontItalic = True
        else:
            if state is qtCore.NormalState:
                self.widget()._wgt__background_rgba = [(79, 79, 79, 255), (119, 119, 119, 255)][self.isPressHovered()]
                self.widget()._wgt__border_rgba = [(127, 127, 127, 255), (159, 159, 159, 255)][self.isPressHovered()]
                self.widget()._wgt__name_rgba = [(191, 191, 191, 255), (255, 255, 255, 255)][self.isPressHovered()]
                #
                self.widget()._wgt__border_style = 'outset'
            elif state is qtCore.PressedState:
                self.widget()._wgt__background_rgba = 47, 47, 47, 255
                #
                self.widget()._wgt__border_rgba = 63, 127, 255, 255
                self.widget()._wgt__name_rgba = 255, 255, 255, 255
                #
                self.widget()._wgt__border_style = 'inset'
            #
            self.widget()._uiFontItalic = False

    def acceptPressCommand(self):
        if self._pressCommand is not None:
            if bscMethods.MayaApp.isActive():
                # noinspection PyUnresolvedReferences
                import maya.mel as mel
                mel.eval(self._pressCommand)
            else:
                if bscMethods.OsPath.isFile(self._pressCommand):
                    mod = bscMethods.PyLoader.loadFile(self._pressCommand)
                    # mod.run()
                else:
                    exec eval(self._pressCommand)
        #
        self.setPressHovered(False)


# Attribute Item Model
class _QtAttributeitemModel(Abs_GuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        self._isPressEnable = False
        self._isExpandEnable = True
        self._isColorEnable = True


# Action Item Model
class Abs_GuiQtActionViewitemWgtModel(Abs_GuiQtItemMdl):
    def __init__(self, widget):
        self._initAbsGuiQtItemMdl(widget)
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
        self._uiIconRect, self._gui_qt__mdl__name_str_Rect, self._uiSubNameRect, self._uiExtendRect = QtCore.QRect(), QtCore.QRect(), QtCore.QRect(), QtCore.QRect()
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
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        self._updateUiStyle()
        #
        xPos, yPos = 0, 0
        #
        side, spacing, sdr = self._uiSide, self._uiSpacing, self._uiShadowRadius
        #
        width, height = self._uiItemWidth, self._uiItemHeight
        #
        frameWidth, frameHeight = self.frameSize()
        iconWidth, iconHeight = self.iconSize()
        #
        if self._isSeparator is True:
            xP1, yP1 = xPos, yPos + self._uiItemHeight/2
            xP2, yP2 = width - 1, yPos + self._uiItemHeight/2
            if self._gui_qt__mdl__name_str_ is not None:
                textWidth = self.widget().fontMetrics().width(self._gui_qt__mdl__name_str_)
                #
                self._gui_qt__mdl__name_str_Rect.setRect(
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
            if self._gui_qt__mdl__name_str_ is not None:
                self._gui_qt__mdl__name_str_Rect.setRect(
                    xPos, yPos,
                    width, self._uiItemHeight
                )
            if self._uiSubNameText is not None:
                self._uiSubNameRect.setRect(
                    0, yPos,
                    width - [0, self._uiFrameWidth][self._isExtendEnable] - side - sdr, self._uiItemHeight
                )
            if self._uiExtendIcon is not None:
                self._uiExtendRect.setRect(
                    width - self._uiFrameWidth + (self._uiFrameWidth - self._uiIconWidth)/2 - side, yPos + (self._uiFrameWidth - self._uiIconHeight)/2,
                    self._uiIconWidth, self._uiIconHeight
                )
    #
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
        xPos, yPos = self._uiItemWidth - self._uiFrameWidth, 0
        self._extendButton.setGeometry(
            xPos, yPos,
            self._uiFrameWidth, self._uiFrameHeight
        )
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._gui_qt__mdl__set_rect_geometry_update_()
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
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
                self._uiIcon = qtCore._toLxOsIconFile('svg_basic/unused')
            if self._uiSubIconKeyword is not None:
                self._uiSubIcon = None
            if self._uiExtendIconKeyword is not None:
                self._uiExtendIcon = None
            #
            self.widget()._wgt__background_rgba = 0, 0, 0, 0
            self.widget()._wgt__border_rgba = 0, 0, 0, 0
            #
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            if state is qtCore.UnpressedState:
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword)
                if self._uiExtendIconKeyword is not None:
                    self._uiExtendIcon = qtCore._toLxOsIconFile(self._uiExtendIconKeyword)
                #
                self.widget()._wgt__background_rgba = 0, 0, 0, 0
                self.widget()._wgt__border_rgba = 0, 0, 0, 0
                #
                self.widget()._wgt__name_rgba = 191, 191, 191, 255
                #
                self.widget()._uiFontItalic = False
            elif state is qtCore.PressedState:
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + 'on')
                if self._uiExtendIconKeyword is not None:
                    self._uiExtendIcon = qtCore._toLxOsIconFile(self._uiExtendIconKeyword + 'on')
                #
                self.widget()._wgt__background_rgba = 71, 71, 71, 255
                self.widget()._wgt__border_rgba = 71, 71, 71, 255
                #
                self.widget()._wgt__name_rgba = 63, 255, 255, 255
                #
                self.widget()._uiFontItalic = False
            #
            if self._uiSubIconKeyword is not None:
                self._uiSubIcon = qtCore._toLxOsIconFile(self._uiSubIconKeyword)
        #
        self._updateWidgetState()
    #
    def update(self):
        self._gui_qt__mdl__set_geometry_update_()
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
            name, iconKeywordStr, enable = data[:3]
            #
            if isinstance(name, str) or isinstance(name, unicode):
                pass
            elif isinstance(name, tuple) or isinstance(name, list):
                pass
            if '#' in name:
                name, subName = name.split('#')
                self._uiSubNameText = subName
            #
            self._gui_qt__mdl__name_str_ = name
            self._isCheckEnable = iconKeywordStr == 'checkBox'
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
                if isinstance(iconKeywordStr, tuple) or isinstance(iconKeywordStr, list):
                    iconKeywordStr, subIconKeyword = iconKeywordStr
                else:
                    subIconKeyword = None
                #
                if iconKeywordStr:
                    self._uiIconKeyword = iconKeywordStr
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
                    self._uiExtendIconKeyword = 'svg_basic/tabmenu_h'
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
                self._gui_qt__mdl__name_str_ = data[0]
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


# View Model
class Abs_QtWgtViewModel(
    guiQtObjAbs.Abs_QtViewObj,
    guiQtObjAbs.Abs_QtScrollareaObj
):
    def _initAbsQtWgtViewModel(self, widget):
        self._initAbsGuiQtViewObj()
        self._initAbsQtScrollareaObj()
        #
        self._initAbsQtWgtViewModelAction()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setScrollBar(widget)
    #
    def _initAbsQtWgtViewModelAction(self):
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
    def _gui_qt__mdl__set_viewport_geometry_update_(self):
        xPos, yPos = self._wgt__margins[0], self._wgt__margins[1]
        width, height = self._viewportWidth, self._viewportHeight
        # Viewport
        self._viewport.setGeometry(
            xPos, yPos,
            width - self._vScrollWidth(), height
        )
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        # Placeholder
        if self.isPlaceholderEnable():
            x, y, w, h = bscMethods.Size2d.mapToRect(self.placeholderSize(), self.size())
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
    def _gui_qt__mdl__set_item_visible_press_start_(self):
        visibleIndex = self._pressVisibleIndex
        # expand
        if self._expandFlag is True:
            pass
        # check
        elif self._checkFlag is True:
            self.setItemCheckVisibleAt(visibleIndex)
        # press
        elif self._expandFlag is False and self._checkFlag is False:
            # Update Change Flag
            self._updateItemPressChangeFlagVisibleAt(visibleIndex)
            #
            self._gui_qt__mdl__set_item_visible_press_start_at_(visibleIndex)
    #
    def _gui_qt__mdl__set_item_visible_press_start_at_(self, visibleIndex):
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
                    self._gui_qt__mdl__set_item_visible_press_at_(visibleIndex)
    #
    def _gui_qt__mdl__set_item_visible_press_at_(self, visibleIndex):
        # press
        def updatePressFnc_(itemModel_):
            itemModel_.setPressed(True)
        # current
        def updateCurrentFnc_(itemModel_):
            isChanged = False
            preItemModel = self._curPressItemModel
            #
            if itemModel_.isPressable():
                if not itemModel_ == preItemModel:
                    isChanged = True
            #
            if isChanged is True:
                # Clear First
                if preItemModel is not None:
                    preItemModel.setPressCurrent(False)
                #
                itemModel_.setPressCurrent(True)
                #
                self._curPressItemModel = itemModel_
                self._curPressItemIndex = self.itemModelIndex(itemModel_)
                self._curPressVisibleIndex = visibleIndex
            #
            if self._dragStartVisibleIndex != self._curPressVisibleIndex:
                isChanged = True
            #
            self._curPressChangeFlag = isChanged
        # command
        def updateCommandFnc_(itemModel_):
            if self._expandFlag is True:
                pass
            elif self._checkFlag is True:
                pass
            else:
                if self._pressFlag is True:
                    if self._extendPressFlag is True:
                        itemModel_.acceptExtendPressCommand()
                    else:
                        itemModel_.acceptPressCommand()
        #
        itemModel = self.itemModelVisibleAt(visibleIndex)
        #
        updatePressFnc_(itemModel)
        updateCurrentFnc_(itemModel)
        updateCommandFnc_(itemModel)
    #
    def _gui_qt__mdl__set_item_visible_press_end_(self):
        itemModel = self._curPressItemModel
        if itemModel is not None:
            itemModel.setPressed(False)
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
        x += self._wgt__margins[0]
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
                    self._gui_qt__mdl__set_item_visible_press_start_()
            elif width < x:
                if self.isHScrollable() is True and not self.isHMaximum():
                    self._hAutoScrollFlag = True
                    self._hAutoScrollRegion = 1
                    #
                    self.hScrollBar().viewModel().setTimerInterval(max(5, 500/(abs(y - height) + 1)))
                    self.hScrollBar().viewModel()._startAutoAddAction()
                else:
                    self._clearHover()
                    self._gui_qt__mdl__set_item_visible_press_start_()
            else:
                self.hScrollBar().viewModel()._autoScrollStopAction()
                self.hScrollBar().viewModel().setTimerInterval(50)
                #
                self._hAutoScrollFlag = False
        #
        y += self._wgt__margins[1]
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
                    self._gui_qt__mdl__set_item_visible_press_start_()
            elif height <= y:
                if self.isVScrollable() is True and not self.isVMaximum():
                    self._vAutoScrollFlag = True
                    self._vAutoScrollRegion = 1
                    #
                    self.vScrollBar().viewModel().setTimerInterval(max(5, 500/(abs(y - height) + 1)))
                    self.vScrollBar().viewModel()._startAutoAddAction()
                else:
                    self._clearHover()
                    self._gui_qt__mdl__set_item_visible_press_start_()
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
                    self._gui_qt__mdl__set_item_visible_press_start_at_(visibleIndex)
            elif self._absHeight < y:
                if self.visibleIndexes():
                    visibleIndex = self.visibleIndexes()[-1]
                    self.setItemHoveredVisibleAt(visibleIndex)
                    self._gui_qt__mdl__set_item_visible_press_start_at_(visibleIndex)
    #
    def _hoverScrollAction(self):
        self._updateHoverLoc(*self._pressHoverPos)
    # environ ******************************************************************************************************** #
    # noinspection PyMethodMayBeStatic
    def _gui_qt__set_enter_event_update_(self, event):
        event.ignore()
    #
    def _gui_qt__mdl__set_mouse_move_event_update_(self, event):
        x, y = self._gui_qt__get_event_pos_(event)
        #
        self._updateHoverLoc(x, y)
        # Tree Connection
        if self._itemMode is qtCore.TreeMode:
            if self._shiftFlag is True:
                self.widget().update()
        #
        event.ignore()
    #
    def _gui_qt__set_leave_event_update_(self, event):
        self._clearHover()
        #
        event.ignore()
    #
    def _gui_qt__mdl__set_mouse_press_event_update_(self, event):
        x, y = self._gui_qt__get_event_pos_(event)
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
            self._gui_qt__mdl__set_item_visible_press_start_()
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
    def _gui_qt__mdl__set_mouse_press_move_event_update_(self, event):
        x, y = self._gui_qt__get_event_pos_(event)
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
                self._gui_qt__mdl__set_item_visible_press_start_()
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
    def _gui_qt__mdl__set_mouse_release_event_update_(self, event):
        x, y = self._gui_qt__get_event_pos_(event)
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
        #
        self._gui_qt__mdl__set_item_visible_press_end_()
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
                self._gui_qt__mdl__set_item_visible_press_start_()
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
    def _gui_qt__mdl__set_geometry_update_(self):
        self._updateWidgetGeometry()
        self._gui_qt__mdl__set_viewport_geometry_update_()
        #
        self._gui_qt__mdl__set_rect_geometry_update_()
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
        self._gui_qt__mdl__set_geometry_update_()
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
        self._gui_qt__mdl__set_item_visible_press_start_at_(self._curPressVisibleIndex)
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
            self._initAbsGuiQtViewObjVar()
            #
            self.update()
    #
    def setFilterExplainRefresh(self):
        if self._filterEntryWidget is not None:
            self._filterEntryWidget.setNameString(str(len(self._itemModelLis)).zfill(4))
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


# Choose Drop View Model
class Abs_GuiQtChooseWindowMdl(guiQtObjAbs.Abs_GuiQtChooseWindowObj):
    def _initAbsGuiQtChooseWindowMdl(self, *args):
        widget, itemClass = args
        self._initAbsGuiQtChooseWindowObj()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setButton(widget)
        self._itemClass = itemClass


# Scroll Model
class Abs_GuiQtScrollareaMdl(guiQtObjAbs.Abs_QtScrollareaObj):
    def _initAbsGuiQtScrollareaMdl(self, widget):
        self._initAbsQtScrollareaObj()
        #
        self._initAbsGuiQtScrollareaMdlAttr()
        self._initAbsGuiQtScrollareaMdlAction()
        self._initAbsGuiQtScrollareaMdlVar()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setScrollBar(widget)
    #
    def _initAbsGuiQtScrollareaMdlVar(self):
        self._pressFlag, self._dragFlag, self._trackFlag = False, False, False
        #
        self._miniWidth, self._miniHeight = 60, 60
    #
    def _initAbsGuiQtScrollareaMdlAttr(self):
        pass
    #
    def _initAbsGuiQtScrollareaMdlAction(self):
        pass
    #
    def _gui_qt__mdl__set_viewport_geometry_update_(self):
        hValue, vValue = self.value()
        #
        xPos, yPos = self._wgt__margins[0] - hValue, self._wgt__margins[1] - vValue
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
        xPos, yPos = self._wgt__margins[0], self._wgt__margins[1]
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
    def _gui_qt__mdl__set_geometry_update_(self):
        self._gui_qt__mdl__set_viewport_geometry_update_()
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
        self._gui_qt__mdl__set_geometry_update_()
        #
        self._updateAction()
    #
    def isMaximum(self):
        return self._vScrollBar._viewModel.isMaximum()
    #
    def isMinimum(self):
        return self._vScrollBar._viewModel.isMinimum()


# Value Enter Label Model
class _QtValueArrayLineModel(guiQtObjAbs.Abs_GuiQtValueArrayLineObj):
    def __init__(self, widget):
        self._initAbsGuiQtValueArrayLineObj()
        self.setWidget(widget)
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.size()
        #
        side, spacing = self._uiSide, self._uiSpacing
        frameWidth, frameHeight = self.frameSize()
        #
        xPos += side
        #
        explainWidth = self._gui_qt__mdl__name_str_Width
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
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
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
            xPos += self._gui_qt__mdl__name_str_Width
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
        self._gui_qt__mdl__set_rect_geometry_update_()
        self._gui_qt__mdl__set_child_wgts_geometry_update_()


# Filter Enter Label Model
class Abs_GuiQtFilterLineMdl(guiQtObjAbs.Abs_GuiQtValueLineObj):
    def _initAbsGuiQtFilterLineMdl(self, *args):
        widget = args[0]
        self._initAbsGuiQtValueLineObj()
        #
        self._initAbsGuiQtFilterLineVar()
        self._initAbsGuiQtFilterLineDraw()
        #
        self.__overrideAttr()
        #
        self.setWidget(widget)
    #
    def _initAbsGuiQtFilterLineVar(self):
        self._occurrenceCount = 0
        self._curOccurrenceIndex = 0
        self._occurrenceCounterText = '0/0'
        self._occurrenceSpanList = []

        self._filterTargetWgt = None
    #
    def _initAbsGuiQtFilterLineDraw(self):
        self._toolLine = self.CLS_gui_qt__mdl_obj__line()
        self._occurrenceCounterRect = self.CLS_gui_qt__mdl_obj__rect()
    #
    def __overrideAttr(self):
        self._filter_line__main_width = 240

        self._isEnterEnable = True
        self._isEnterable = True
        #
        self._xLeftPos = 0
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side = 2
        spacing = 2
        frameWidth, frameHeight = self.frameSize()
        #
        xPos = max(0, width - self._filter_line__main_width)
        #
        xPos += side
        #
        self._xLeftPos = xPos
        self._uiBasicRect.setRect(
            xPos, yPos,
            width - xPos, frameHeight
        )
        xPos = max(0, width - self._filter_line__main_width)
        self._occurrenceCounterRect.setRect(
            xPos - (frameWidth*6 + spacing), yPos,
            frameWidth*4, frameHeight
        )
    #
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
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
        xPos = max(0, width - self._filter_line__main_width)
        #
        self._preOccurrenceBtnWgt.setGeometry(
            xPos - frameWidth*2, yPos,
            frameWidth, frameHeight
        )
        self._nextOccurrenceBtnWgt.setGeometry(
            xPos - frameWidth, yPos,
            frameWidth, frameHeight
        )
        #
        xPos += side*2
        #
        self._historyBtnWgt.setGeometry(
            xPos, yPos,
            frameWidth, frameHeight
        )
        #
        self._enterWidget.setGeometry(
            xPos + frameWidth, yPos,
            width - xPos - side - (frameWidth*3), frameHeight
        )
        #
        toolWidth = frameWidth*2 + side

        self._toolLine.setLine(
            width - toolWidth, yPos,
            width - toolWidth, yPos + frameHeight
        )
        #
        self._copyButton.setGeometry(
            width - frameWidth*4 - side, yPos,
            frameWidth, frameHeight
        )
        self._clearButton.setGeometry(
            width - frameWidth*3 - side, yPos,
            frameWidth, frameHeight
        )
        self._matchCaseBtnWgt.setGeometry(
            width - frameWidth*2 - side, yPos,
            frameWidth, frameHeight
        )
        self._matchWordBtnWgt.setGeometry(
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
    def _gui_qt__filter_line__filter_action_(self):
        if self._filterTargetWgt is not None:
            keywordStr = self._enterWidget.text()
            contentStr = self._filterTargetWgt.toPlainText()

            self._occurrenceSpanList = bscMethods.String.findSpans(
                contentStr, keywordStr,
                matchCaseFlag=self.isMatchCase(), matchWordFlag=self.isMatchWord()
            )

            self._occurrenceCount = len(self._occurrenceSpanList)
            if self._occurrenceCount > 0:
                self._curOccurrenceIndex = min((self._occurrenceCount - 1), self._curOccurrenceIndex)
            else:
                self._curOccurrenceIndex = 0

            self._gui_qt__filter_line__set_occurrence_counter_update_()
            self._gui_qt__filter_line__set_occurrence_btn_state_update_()

            self._gui_qt__mtd__text_edit__set_filter_(
                self._filterTargetWgt,
                len(contentStr),
                self._occurrenceSpanList
            )
            self._gui_qt__filter_line__set_filter_target_selected_update_()

    @classmethod
    def _gui_qt__mtd__text_edit__set_custom_format_update_at_(cls, *args):
        textEdit, startIndex, endIndex = args

        textCursor = qtCore.QtGui.QTextCursor(textEdit.textCursor())
        chartFormat = qtCore.QtGui.QTextCharFormat(textCursor.charFormat())
        chartFormat.setBackground(qtCore.QtGui.QBrush(qtCore.QtCore.Qt.transparent))

        textCursor.setPosition(startIndex)
        textCursor.setPosition(endIndex, qtCore.QtGui.QTextCursor.KeepAnchor)
        textCursor.mergeCharFormat(chartFormat)
        return textCursor

    @classmethod
    def _gui_qt__mtd__text_edit__set_highlight_format_update_at_(cls, *args):
        textEdit, startIndex, endIndex = args

        textCursor = qtCore.QtGui.QTextCursor(textEdit.textCursor())
        chartFormat = qtCore.QtGui.QTextCharFormat(textCursor.charFormat())
        chartFormat.setBackground(qtCore.QtGui.QBrush(qtCore.QtGui.QColor(255, 127, 63, 255)))

        textCursor.setPosition(startIndex)
        textCursor.setPosition(endIndex, qtCore.QtGui.QTextCursor.KeepAnchor)
        textCursor.mergeCharFormat(chartFormat)
        return textCursor

    @classmethod
    def _gui_qt__mtd__text_edit__set_filter_(cls, *args):
        textEdit, maxCount, spanList = args
        selectedIndex = 1
        customStartIndex = 0
        endIndex = maxCount
        if spanList:
            for seq, span in enumerate(spanList):
                curStartIndex, curEndIndex = span

                cls._gui_qt__mtd__text_edit__set_custom_format_update_at_(textEdit, customStartIndex, curStartIndex)
                customStartIndex = curEndIndex
                #
                highlightTextCursor = cls._gui_qt__mtd__text_edit__set_highlight_format_update_at_(textEdit, curStartIndex, curEndIndex)
                if seq == selectedIndex:
                    textEdit.setTextCursor(highlightTextCursor)

            cls._gui_qt__mtd__text_edit__set_custom_format_update_at_(textEdit, customStartIndex, endIndex)
        else:
            cls._gui_qt__mtd__text_edit__set_custom_format_update_at_(textEdit, customStartIndex, endIndex)

    def _gui_qt__filter_line__set_filter_target_selected_update_(self):
        if self._occurrenceSpanList:
            textEdit, (startIndex, endIndex) = self._filterTargetWgt, self._occurrenceSpanList[self._curOccurrenceIndex]
            textCursor = qtCore.QtGui.QTextCursor(textEdit.textCursor())
            textCursor.setPosition(startIndex)
            textCursor.setPosition(endIndex, qtCore.QtGui.QTextCursor.KeepAnchor)
            textEdit.setTextCursor(textCursor)
        else:
            self._filterTargetWgt.moveCursor(qtCore.QtGui.QTextCursor.End)
    #
    def _gui_qt__filter_line__set_occurrence_counter_update_(self):
        count, index = self._occurrenceCount, self._curOccurrenceIndex
        if count:
            self._occurrenceCounterText = u'{}/{}'.format(
                index + 1, count
            )
        else:
            self._occurrenceCounterText = u'0/0'
        self._updateWidgetState()
    #
    def _gui_qt__filter_line__set_occurrence_btn_state_update_(self):
        count, index = self._occurrenceCount, self._curOccurrenceIndex
        if count > 0:
            if index == 0:
                self._preOccurrenceBtnWgt.setPressable(False)
            else:
                self._preOccurrenceBtnWgt.setPressable(True)

            if index == (count - 1):
                self._nextOccurrenceBtnWgt.setPressable(False)
            else:
                self._nextOccurrenceBtnWgt.setPressable(True)
        else:
            self._preOccurrenceBtnWgt.setPressable(False)
            self._nextOccurrenceBtnWgt.setPressable(False)
    #
    def _gui_qt__filter_line__set_occurrence_index_add_(self):
        if self._occurrenceCount > 0:
            if self._curOccurrenceIndex < (self._occurrenceCount - 1):
                if self._preOccurrenceBtnWgt.isPressable() is False:
                    self._preOccurrenceBtnWgt.setPressable(True)

                self._curOccurrenceIndex += 1
                self._gui_qt__filter_line__set_occurrence_counter_update_()
                self._gui_qt__filter_line__set_filter_target_selected_update_()
            else:
                self._preOccurrenceBtnWgt.setPressable(True)
                self._nextOccurrenceBtnWgt.setPressable(False)
    #
    def _gui_qt__filter_line__set_occurrence_index_sub_(self):
        if self._occurrenceCount > 0:
            if self._curOccurrenceIndex > 0:
                if self._nextOccurrenceBtnWgt.isPressable() is False:
                    self._nextOccurrenceBtnWgt.setPressable(True)

                self._curOccurrenceIndex -= 1
                self._gui_qt__filter_line__set_occurrence_counter_update_()
                self._gui_qt__filter_line__set_filter_target_selected_update_()
            else:
                self._preOccurrenceBtnWgt.setPressable(False)
                self._nextOccurrenceBtnWgt.setPressable(True)
    #
    def addFilterTarget(self, widget):
        self._filterTargetWgt = widget
        self.widget().entryChanged.connect(self._gui_qt__filter_line__filter_action_)
    #
    def isMatchCase(self):
        return self._matchCaseBtnWgt.isChecked()
    #
    def isMatchWord(self):
        return self._matchWordBtnWgt.isChecked()
    #
    def update(self):
        self._gui_qt__mdl__set_rect_geometry_update_()
        #
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
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
        self._historyBtnWgt = self._widget._historyBtnWgt
        #
        self._copyButton = self._widget._copyButton
        self._clearButton = self._widget._clearButton
        #
        self._enterWidget = self._widget._enterWidget

        self._matchCaseBtnWgt = self.widget()._matchCaseBtnWgt
        self._matchWordBtnWgt = self.widget()._matchWordBtnWgt

        self._preOccurrenceBtnWgt = self.widget()._preOccurrenceBtnWgt
        self._preOccurrenceBtnWgt.clicked.connect(self._gui_qt__filter_line__set_occurrence_index_sub_)

        self._nextOccurrenceBtnWgt = self.widget()._nextOccurrenceBtnWgt
        self._nextOccurrenceBtnWgt.clicked.connect(self._gui_qt__filter_line__set_occurrence_index_add_)


# Choose Tab Item
class Abs_GuiQtChooseTabbuttonMdl(guiQtObjAbs.Abs_GuiQtValueLineObj):
    def __init__(self, widget):
        self._initAbsGuiQtChooseTabbuttonMdl(widget)

    def _initAbsGuiQtChooseTabbuttonMdl(self, *args):
        widget = args[0]

        self._initAbsGuiQtValueLineObj()
        #
        self.setWidget(widget)
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
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
        self._gui_qt__mdl__set_rect_geometry_update_()
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
    #
    def setWidget(self, widget):
        self._widget = widget


# Text Brower Model
class Abs_GuiQtTextbrowerMdl(guiQtObjAbs.Abs_GuiQtValueLineObj):
    def _initAbsGuiQtTextbrowerMdl(self, widget):
        self._initAbsGuiQtValueLineObj()
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
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        side = 0
        #
        xPos += side
        #
        yPos += 32
        #
        self.basicRect().setRect(
            xPos, yPos,
            width - xPos - side, height - yPos - side
        )
        self._uiLineCounterRect.setRect(
            xPos + 1, yPos + 1,
            self._counterWidth, height - yPos - side - 2
        )
        #
        xPos += self._counterWidth
        #
        self._uiEnterRect.setRect(
            xPos + 1, yPos + 1,
            width - xPos - side - 2, height - yPos - side - 2
        )
    #
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        toolbarHeight = 32
        buttonHeight = 20
        #
        side = 0
        #
        xPos += side
        #
        self._filterLineWgt.setGeometry(
            xPos, (toolbarHeight - buttonHeight)/2,
            width - xPos - side - 2, buttonHeight
        )
        #
        yPos += toolbarHeight
        #
        xPos += self._counterWidth
        #
        self._enterWidget.setGeometry(
            xPos + 2, yPos + 2,
            width - xPos - side - 3, height - yPos - side - 3
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
                self._setQtEnterStyle(qtCore.EnterState)
            else:
                self._setQtEnterStyle(qtCore.UnenterState)
        else:
            self._setQtEnterStyle(qtCore.NormalState)
        #
        self._updateWidgetState()
    #
    def update(self):
        self._gui_qt__mdl__set_rect_geometry_update_()
        #
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
    #
    def setNameString(self, string):
        if string is not None:
            self._gui_qt__mdl__name_str_ = unicode(string)
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
        self._enterWidget.setPlainText('')
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._filterLineWgt = self.widget()._filterLineWgt
        self._enterWidget = self.widget()._textEditWgt
    #
    def _setQtEnterStyle(self, state):
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


# Scroll Bar Model
class _QtScrollbarModel(guiQtObjAbs.Abs_QtScrollbarObj):
    def __init__(self, widget):
        self._initAbsQtScrollbarObj()
        #
        self.setWidget(widget)


# Tab Model
class Abs_GuiQtTabWgtModel(guiQtObjAbs.QtAbc_TabitemModel):
    def _initTabModelBasic(self, widget):
        self._initAbcTabitemModel()
        #
        self.setWidget(widget)
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
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
            self._menuButton.setIcon('svg_basic/menu_tab_h')
        else:
            self._menuButton.setGeometry(
                xPos + _h, w - frameWidth - side + _w - 2,
                frameWidth, frameHeight
            )
            self._menuButton.setIcon('svg_basic/menu_tab_v')
        #
        if self.isPressCurrent():
            self._menuButton.show()
        else:
            self._menuButton.hide()
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._gui_qt__mdl__set_rect_geometry_update_()
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
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
        self._gui_qt__mdl__set_geometry_update_()
        #
        self._updateWidgetState()
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            if state is qtCore.CurrentState:
                self.widget()._wgt__name_rgba = [(63, 127, 255, 255), (63, 255, 255, 255)][self.isPressHovered()]
                self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + ['cur', 'on'][self.isPressHovered()])
            elif state is qtCore.NormalState:
                self.widget()._wgt__name_rgba = [(191, 191, 191, 255), (223, 223, 223, 255)][self.isPressHovered()]
                self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + ['', 'on'][self.isPressHovered()])
            #
            self.widget()._uiFontItalic = False


# Tab Bar Model
class Abs_GuiQtTabbarWgtModel(guiQtObjAbs.QtAbc_TabbarModel):
    def _initTabBarModelBasic(self, widget):
        self._initAbcTabbarModel()
        #
        self.setWidget(widget)
        self.setViewport(widget)
    #
    def _gui_qt__mdl__set_viewport_geometry_update_(self):
        xPos, yPos = self._wgt__margins[0], self._wgt__margins[1]
        #
        w, h = self.viewSize()
        #
        self._viewport.setGeometry(
            xPos, yPos,
            w, h
        )
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        self._uiBasicRect.setRect(
            xPos, yPos,
            width, height
        )
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._gui_qt__mdl__set_viewport_geometry_update_()
        #
        self._gui_qt__mdl__set_rect_geometry_update_()
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
        self._gui_qt__mdl__set_geometry_update_()
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


# Tab Group Model
class Abs_GuiQtTabgroupMdl(guiQtObjAbs.Abs_GuiQtTabviewObj):
    def _initAbsGuiQtTabgroupMdl(self, widget):
        self._initAbsGuiQtTabviewObj()
        #
        self.setWidget(widget)
        self.setViewport(widget)
    #
    def _gui_qt__mdl__set_viewport_geometry_update_(self):
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
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
        pass
    #
    def _updateScrollButtonState(self):
        pass
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._gui_qt__mdl__set_viewport_geometry_update_()
        #
        self._gui_qt__mdl__set_rect_geometry_update_()
        #
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
    #
    def update(self):
        self._gui_qt__mdl__set_geometry_update_()
        #
        self._updateWidgetState()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._tabBar = self.widget()._tabBar


# Action Drop View
class Abs_GuiQtActionViewportMdl(guiQtObjAbs.Abs_GuiQtActionViewportObj):
    def _initAbsQtActionDropviewMdl(self, *args):
        widget, itemClass = args
        self._initAbsQtActionDropviewObj()
        #
        self.setWidget(widget)
        self.setScrollBar(widget)
        self.setButton(widget)
        #
        self._itemClass = itemClass


# Chart Model
class Abs_GuiQtChartMdl(guiQtObjAbs.Abs_GuiQtChartObj):
    fnc_angle = math.radians
    fnc_sin = math.sin
    fnc_cos = math.cos
    fnc_tan = math.tan
    #
    CLS_pen = QtGui.QPen
    CLS_color = QtGui.QColor
    CLS_brush = QtGui.QBrush
    CLS_point = QtCore.QPoint
    CLS_pointF = QtCore.QPointF
    CLS_line = QtCore.QLine
    CLS_rect = QtCore.QRect
    CLS_rectF = QtCore.QRectF
    CLS_polygon = QtGui.QPolygon
    CLS_polygonF = QtGui.QPolygonF
    CLS_painterPath = QtGui.QPainterPath
    def _initAbsGuiQtChartMdl(self):
        self._initAbsGuiQtChartObj()
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
        self._gui_qt__mdl__set_rect_geometry_update_()
        self._updateDrawDatum()


# Group Model
class Abs_GuiQtGroupMdl(guiQtObjAbs.Abs_GuiQtGroupObj):
    def _initAbsGuiQtGroupMdl(self, widget):
        self._initAbsGuiQtGroupObj()
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
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
        # Expand
        if self.isExpandEnable():
            self._updateExpandRect(xPos, yPos, width, height)
            xPos += frameWidth + self._uiSpacing
        # Name
        if self.nameText() is not None:
            self._updateNameTextRect(xPos, yPos, width-(buttonWidth+spacing)-side, height)
    #
    def _gui_qt__mdl__set_viewport_geometry_update_(self):
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
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
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
        self.widget()._separateWindow.setNameString(self.nameText())
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
        iconKeywordStr = ['svg_basic/separatewindow', 'svg_basic/unseparatewindow'][self.isSeparated()]
        self.widget()._separateButton.setIcon(iconKeywordStr)
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

        # noinspection PyArgumentList
        self._widgetLayout = qtCore.QVBoxLayout(self.widget())
        self._widgetLayout.setContentsMargins(0, 0, 0, 0)
        self._widgetLayout.setSpacing(0)

        self._widgetLayout.addWidget(self._viewport)

        # noinspection PyArgumentList
        self._viewport.setGeometry(0, 0, 0, 0)

        if qtCore.LOAD_INDEX is 0:
            self._viewport.setAttribute(QtCore.Qt.WA_TranslucentBackground | QtCore.Qt.WA_TransparentForMouseEvents)
        else:
            self._viewport.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self._viewport.setMouseTracking(True)

        self._viewport.setFocusProxy(self.widget())
    #
    def update(self):
        self._updateWidgetSizePolicy()
        self._updateWidgetSize()
        #
        self._gui_qt__mdl__set_viewport_geometry_update_()
        self._gui_qt__mdl__set_child_wgts_geometry_update_()
        self._gui_qt__mdl__set_rect_geometry_update_()
        #
        self._updateWidgetState()
    #
    def setFilterColor(self, rgba):
        if rgba is not None:
            self.setColorEnable(True)
            #
            self.widget()._wgt__color__background_rgba = rgba
        else:
            self.setColorEnable(False)
        #
        self._gui_qt__set_press_style_update_()
        self._updateQtExpandStyle()


class GuiQtGroupModel(Abs_GuiQtGroupMdl):
    def __init__(self, widget):
        self._initAbsGuiQtGroupMdl(widget)


# Window Model
class Abs_GuiQtWindowMdl(guiQtObjAbs.Abs_GuiQtWindowObj):
    def _overrideAttr(self):
        self._isExpandEnable = True
        self._isExpandable = True
        self._isExpanded = True

        self._wgt__margins = 8, 8, 8, 8
    #
    def _initAbsGuiQtWindowMdl(self, *args):
        widget = args[0]
        self._initAbsGuiQtWindowObj()

        self._initAbsGuiQtWindowMdlAttr()
        self._initAbsGuiQtWindowMdlUi()
        self._initAbsGuiQtWindowMdlRect()
        self._initAbsGuiQtWindowMdlAction()
        self._initAbsGuiQtWindowMdlVar()
        #
        self._overrideAttr()
        #
        self.setWidget(widget)
        self.setViewport(widget)
        self.setViewportLayout(widget)
    #
    def _initAbsGuiQtWindowMdlAttr(self):
        self._xMenuPos, self._yMenuPos = 0, 0
        self._xTranslate, self._yTranslate = 0, 0
    #
    def _initAbsGuiQtWindowMdlUi(self):
        pass
    #
    def _initAbsGuiQtWindowMdlRect(self):
        pass
    #
    def _initAbsGuiQtWindowMdlAction(self):
        self._progressTimer.timeout.connect(self.setProgressZero)
    #
    def _initAbsGuiQtWindowMdlVar(self):
        pass
    #
    def _updateWidgetSize(self):
        width, height = self.width(), self.height()
        if self.isExpanded():
            minimumSize = self.viewport().layout().minimumSize()
            w, h = minimumSize.width(), minimumSize.height()
            #
            if self.isMenuEnable():
                h += self._wgt__menu_height
            if self.isStatusEnable():
                h += self._wgt__status_height
            #
            sdr = self._shadowRadius()
            l, t, r, b = self.widgetMargins()
            #
            width_, height_ = w + l + r + sdr, h + t + b + sdr
        else:
            width_, height_ = 0, self._wgt__menu_height
        #
        self.widget().resize(max(width, width_), max(height, height_))
    #
    def _gui_qt__get_event_pos_(self, event):
        point = event.pos()
        x, y = point.x(), point.y()
        return x - self._wgt__margins[0], y - self._wgt__margins[1]
    #
    def _gui_qt__get_resize_region_(self, event):
        point = event.pos()

        cursor_x, cursor_y = point.x(), point.y()

        (x_0, x_1, x_1_a, x_2, x_2_a, x_3), (y_0, y_1, y_1_a, y_2, y_2_a, y_3) = self._gui_qt__get_resize_var_(
            gap=self._win_resize_gap*2
        )

        cnd_x_0, cnd_x_0_a, cnd_x_1, cnd_x_1_a, cnd_x_2, cnd_x_2_a = (
            x_0 < cursor_x < x_1,
            x_0 < cursor_x < x_1_a,
            x_1 < cursor_x < x_2,
            x_1_a < cursor_x < x_2_a,
            x_2 < cursor_x < x_3,
            x_2_a < cursor_x < x_3
        )
        cnd_y_0, cnd_y_0_a, cnd_y_1, cnd_y_1_a, cnd_y_2, cnd_y_2_a = (
                y_0 < cursor_y < y_1,
                y_0 < cursor_y < y_1_a,
                y_1 < cursor_y < y_2,
                y_1_a < cursor_y < y_2_a,
                y_2 < cursor_y < y_3,
                y_2_a < cursor_y < y_3
        )
        # ↖
        if cnd_x_0_a and cnd_y_0_a:
            return 0
        # ↑
        elif cnd_x_1_a and cnd_y_0:
            return 1
        # ↗
        elif cnd_x_2_a and cnd_y_0_a:
            return 2
        # →
        elif cnd_x_2 and cnd_y_1_a:
            return 3
        # ↘
        elif cnd_x_2_a and cnd_y_2_a:
            return 4
        # ↓
        elif cnd_x_1_a and cnd_y_2:
            return 5
        # ↙
        elif cnd_x_0_a and cnd_y_2_a:
            return 6
        # ←
        elif cnd_x_0 and cnd_y_1_a:
            return 7
    #
    def _gui_qt__get_resize_var_(self, gap):
        xPos, yPos = 0, 0
        w, h = self.size()

        sdr = self._uiShadowRadius
        x_0, x_1, x_1_a, x_2, x_2_a, x_3 = (
            xPos,
            xPos + gap,
            xPos + gap*2,
            xPos + (w - (gap + sdr)),
            xPos + (w - (gap*2 + sdr)),
            xPos + (w - sdr)
        )
        y_0, y_1, y_1_a, y_2, y_2_a, y_3 = (
            yPos,
            yPos + gap,
            yPos + gap*2,
            yPos + (h - (gap + sdr)),
            yPos + (h - (gap*2 + sdr)),
            yPos + (h - sdr)
        )
        return (x_0, x_1, x_1_a, x_2, x_2_a, x_3), (y_0, y_1, y_1_a, y_2, y_2_a, y_3)
    #
    def _updateHoverLoc(self, x, y):
        pass
    #
    def _updatePressLoc(self, x, y):
        pass
    # Hover
    def _gui_qt__set_enter_event_update_(self, event):
        self._updateWidgetState()
    #
    def _gui_qt__set_leave_event_update_(self, event):
        self._win_resize_region = None
        self._updateWidgetState()
        event.ignore()
    #
    def _hoverScrollAction(self):
        pass
    # event ********************************************************************************************************** #
    def _gui_qt__mdl__set_mouse_press_event_update_(self, event, isDoubleClick=False):
        x, y = self._gui_qt__get_event_pos_(event)
        # Flag
        self._pressFlag, self._dragFlag = True, False
        # Action
        self._gui_qt__mdl__set_drag_start_(event)
        #
        self._updatePressLoc(x, y)
        #
        if isDoubleClick:
            if self.isMenuRectContainPos((x, y)):
                if self.isExpanded():
                    self._maximizeButtonPressAction()
    #
    def _gui_qt__mdl__set_mouse_move_event_update_(self, event):
        self._win_resize_region = self._gui_qt__get_resize_region_(event)
        self._gui_qt__mdl__set_resize_rect_geometry_update_()
        self._updateWidgetState()
    #
    def _gui_qt__mdl__set_mouse_press_move_event_update_(self, event):
        x, y = self._gui_qt__get_event_pos_(event)
        # Flag
        self._pressFlag, self._dragFlag = False, True
        # Action
        self._gui_qt__mdl__set_drag_execute_(event)
        #
        self._updatePressLoc(x, y)
    #
    def _gui_qt__mdl__set_mouse_release_event_update_(self, event):
        self._pressFlag, self._dragFlag = False, False
        #
        if self._resizeStartSize != self.widget().size():
            self.update()
        #
        self.widget().setCursor(qtCore.QtCore.Qt.ArrowCursor)
    #
    def _gui_qt__mdl__set_event_filter_update_(self, *args):
        event = args[1]
        if event.type() == QtCore.QEvent.WindowDeactivate:
            self._win_resize_region = None
            #
            self._isWindowActive = False
            self._updateWindowActiveState()
        elif event.type() == QtCore.QEvent.WindowActivate:
            self._win_resize_region = self._gui_qt__get_resize_region_(event)
            #
            self._isWindowActive = True
            self._updateWindowActiveState()
        return False
    #
    def _gui_qt__mdl__set_drag_start_(self, event):
        self._moveStartCursorPos = event.globalPos() - self.pos()
        #
        self._resizeStartCursorPos = event.globalPos()
        #
        self._resizeStartPos = self.widget().pos()
        self._resizeStartSize = self.widget().size()
    #
    def _gui_qt__mdl__set_drag_execute_(self, event):
        if self.isResizeable():
            if self._win_resize_region is not None:
                mw, mh = self._gui_qt__window__get_minimum_size_()
                startPosObj = self._resizeStartPos
                startSizeObj = self._resizeStartSize

                changePosObj = event.globalPos() - self._resizeStartCursorPos
                #
                p_x_0, p_x_1, p_x_2 = (
                    startPosObj.x(),
                    startPosObj.x() + changePosObj.x(),
                    startPosObj.x() - changePosObj.x()
                )
                p_y_0, p_y_1, p_y_2 = (
                    startPosObj.y(),
                    startPosObj.y() + changePosObj.y(),
                    startPosObj.y() - changePosObj.y()
                )
                s_w_0, s_w_1, s_w_2 = (
                    startSizeObj.width(),
                    startSizeObj.width() + changePosObj.x(),
                    startSizeObj.width() - changePosObj.x()
                )
                s_h_0, s_h_1, s_h_2 = (
                    startSizeObj.height(),
                    startSizeObj.height() + changePosObj.y(),
                    startSizeObj.height() - changePosObj.y()
                )
                # set window minimum size
                s_w_0, s_w_1, s_w_2 = max(s_w_0, mw), max(s_w_1, mw), max(s_w_2, mw)
                s_h_0, s_h_1, s_h_2 = max(s_h_0, mh), max(s_h_1, mh), max(s_h_2, mh)
                # ↖
                if self._win_resize_region == 0:
                    self.widget().setGeometry(
                        p_x_1, p_y_1,
                        s_w_2, s_h_2
                    )
                # ↑
                elif self._win_resize_region == 1:
                    self.widget().setGeometry(
                        p_x_0, p_y_1,
                        s_w_0, s_h_2
                    )
                # ↗
                elif self._win_resize_region == 2:
                    self.widget().setGeometry(
                        p_x_0, p_y_1,
                        s_w_1, s_h_2
                    )
                # →
                elif self._win_resize_region == 3:
                    self.widget().setGeometry(
                        p_x_0, p_y_0,
                        s_w_1, s_h_0
                    )
                # ↘
                elif self._win_resize_region == 4:
                    self.widget().setGeometry(
                        p_x_0, p_y_0,
                        s_w_1, s_h_1
                    )
                # ↓
                elif self._win_resize_region == 5:
                    self.widget().setGeometry(
                        p_x_0, p_y_0,
                        s_w_0, s_h_1
                    )
                # ↙
                elif self._win_resize_region == 6:
                    self.widget().setGeometry(
                        p_x_1, p_y_0,
                        s_w_2, s_h_1
                    )
                # ←
                elif self._win_resize_region == 7:
                    self.widget().setGeometry(
                        p_x_1, p_y_0,
                        s_w_2, s_h_0
                    )
        if self.isMoveable():
            if self._win_resize_region is None:
                self.widget().move(event.globalPos() - self._moveStartCursorPos)
                if not self.widget().cursor() == qtCore.QtCore.Qt.DragMoveCursor:
                    self.widget().setCursor(qtCore.QtCore.Qt.DragMoveCursor)

    # geometry ******************************************************************************************************* #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        x_0, y_0, w_0, h_0 = self._gui_qt__mdl__get_widget_geometry_args_(xPos, yPos, width, height)
        #
        w_0 -= 1
        h_0 -= 1
        #
        frameWidth, frameHeight = self._uiFrameWidth, self._uiFrameHeight
        buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
        sdr = self._shadowRadius()
        #
        self.basicRect().setRect(
            x_0, y_0,
            w_0 - sdr, h_0 - sdr
        )
        # resize
        if self.isResizeable():
            self.resizeRect().setRect(
                x_0 + (w_0 - (frameWidth + sdr + 2)), y_0 + (h_0 - (frameHeight + sdr + 2)),
                buttonWidth, buttonHeight
            )
        # placeholder
        if self.isPlaceholderEnable():
            x, y, w, h = bscMethods.Size2d.mapToRect(self.placeholderSize(), self.size())
            self.placeholderRect().setRect(
                x, y, w, h
            )
        # header
        if self.layoutDirection() is qtCore.Horizontal:
            w, h = (w_0 - sdr) / 4, 4
            pointLis = [
                (x_0 + w, y_0),
                (w_0 - w - sdr, y_0),
                (w_0 - w - h - sdr, y_0 + h),
                (x_0 + w + h, y_0 + h),
                (x_0 + w, y_0)
            ]
            path = qtCore.QPainterPath_()
            path._addPoints(pointLis)
            self._uiFocusPath = path
        else:
            w, h = 4, (h_0 - sdr) / 4
            pointLis = [
                (w_0 - sdr, y_0 + h),
                (w_0 - sdr, h_0 - h - sdr),
                (w_0 - w - sdr, h_0 - w - h - sdr),
                (w_0 - w - sdr, y_0 + w + h),
                (w_0 - sdr, y_0 + h)
            ]
            path = qtCore.QPainterPath_()
            path._addPoints(pointLis)
            self._uiFocusPath = path
    #
    def _gui_qt__mdl__set_resize_rect_geometry_update_(self):
        (x_0, x_1, x_1_a, x_2, x_2_a, x_3), (y_0, y_1, y_1_a, y_2, y_2_a, y_3) = self._gui_qt__get_resize_var_(
            gap=self._win_resize_gap
        )
        w_0, w_0_a, w_1, w_1_a = x_1 - x_0, x_1_a - x_0, x_2 - x_1, x_2_a - x_1_a
        h_0, h_0_a, h_1, h_1_a = y_1 - y_0, y_1_a - y_0, y_2 - y_1, y_2_a - y_1_a,
        # ↖
        self._win_resize_rect_l_t.setRect(
            x_0, y_0,
            w_0_a, h_0_a
        )
        # ↑
        self._win_resize_rect_t.setRect(
            x_1_a, y_0,
            w_1_a, h_0
        )
        # ↗
        self._win_resize_rect_r_t.setRect(
            x_2_a, y_0,
            w_0_a, h_0_a
        )
        # →
        self._win_resize_rect_r.setRect(
            x_2, y_1_a,
            w_0, h_1_a
        )
        # ↘
        self._win_resize_rect_r_b.setRect(
            x_2_a, y_2_a,
            w_0_a, h_0_a
        )
        # ↓
        self._win_resize_rect_b.setRect(
            x_1_a, y_2,
            w_1_a, h_0
        )
        # ↙
        self._win_resize_rect_l_b.setRect(
            x_0, y_2_a,
            w_0_a, h_0_a
        )
        # ←
        self._win_resize_rect_l.setRect(
            x_0, y_1_a,
            w_0, h_1_a
        )
    #
    def _gui_qt__mdl__set_menu_objs_geometry_update_(self):
        if self.isMenuEnable():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()
            x_0, y_0, w_0, h_0 = self._gui_qt__mdl__get_widget_geometry_args_(xPos, yPos, width, height)
            #
            w_0 -= 1
            h_0 -= 1
            #
            menuWidth, menuHeight = self._wgt__menu_width, self._wgt__menu_height
            buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
            #
            isHorizontal = self.layoutDirection() is qtCore.Horizontal
            #
            side, spacing, sdr = self._uiSide, self._uiSpacing, self._shadowRadius()
            if isHorizontal:
                x_1, y_1 = x_0 + (w_0 - buttonWidth - side - sdr), y_0 + (menuHeight - buttonHeight)/2
            else:
                x_1, y_1 = x_0 + (w_0 - menuHeight + (menuHeight - buttonWidth)/2 - sdr), y_0 + (menuHeight - buttonWidth)/2
            #
            self._closeButton.setGeometry(
                x_1, y_1,
                buttonWidth, buttonHeight
            )
            # Maximize
            if self.isMaximizeable():
                if isHorizontal:
                    x_1 -= (buttonWidth + spacing)
                else:
                    y_1 += (buttonWidth + spacing)
                #
                self._maximizeButton.setGeometry(
                    x_1, y_1,
                    buttonWidth, buttonHeight
                )
                #
                if self.isExpanded():
                    self._maximizeButton.setIconKeyword(['svg_basic/maximize', 'svg_basic/normmize'][self.isMaximized()])
                #
                self._maximizeButton.show()
            else:
                self._maximizeButton.hide()
            # Minimize
            if self.isMinimizeable():
                if isHorizontal:
                    x_1 -= (buttonWidth + spacing)
                else:
                    y_1 += (buttonWidth + spacing)
                #
                self._minimizeButton.setGeometry(
                    x_1, y_1,
                    buttonWidth, buttonHeight
                )
                #
                self._minimizeButton.show()
            else:
                self._minimizeButton.hide()
            # Expand
            if self.isExpandable():
                if isHorizontal:
                    x_1 -= (buttonWidth + spacing)
                else:
                    y_1 += (buttonWidth + spacing)
                #
                self._expandButton.setGeometry(
                    x_1, y_1,
                    buttonWidth, buttonHeight
                )
                #
                if not self.isMaximized():
                    iconKeywordStr = ['svg_basic/unfold', 'svg_basic/fold'][self.isExpanded()]
                    self._expandButton.setIconKeyword(iconKeywordStr)
                #
                self._expandButton.show()
            else:
                self._expandButton.hide()
            # Menu
            if isHorizontal:
                x_1 -= (buttonWidth + spacing)
            else:
                y_1 += (buttonWidth + spacing)
            #
            self._menuButton.setGeometry(
                x_1, y_1,
                buttonWidth, buttonHeight
            )
            #
            self._xMenuPos, self._yMenuPos = x_1, y_1
            #
            self._progressBar.setGeometry(
                0, -2,
                w_0 - sdr, 1
            )
        else:
            for i in [self._menuButton, self._minimizeButton, self._maximizeButton, self._expandButton, self._closeButton]:
                i.hide()
    #
    def _gui_qt__mdl__set_menu_rect_geometry_update_(self):
        if self.isMenuEnable():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()
            x_0, y_0, w_0, h_0 = self._gui_qt__mdl__get_widget_geometry_args_(xPos, yPos, width, height)
            w_0 -= 1
            h_0 -= 1
            #
            menuWidth, menuHeight = self._wgt__menu_width, self._wgt__menu_height
            _statusWidth, _statusHeight = self._wgt__status_width, self._wgt__status_height
            #
            side, spacing, sdr = self._uiSide, self._uiSpacing, self._shadowRadius()
            #
            iconWidth, iconHeight = self._uiIconWidth, self._uiIconHeight
            frameWidth, frameHeight = self._wgt__menu_height, self._wgt__menu_height
            _w, _h = (frameWidth - iconWidth) / 2, (frameHeight - iconHeight) / 2
            if self.layoutDirection() == qtCore.Horizontal:
                x, y = x_0, y_0
                w, h = w_0 - sdr, menuHeight
                #
                x_0 += side
                # Icon
                if self.icon() is not None:
                    self.iconRect().setRect(
                        x_0 + _w, y_0 + _h,
                        iconWidth, iconHeight
                    )
                    #
                    x_0 += (frameWidth + spacing)
                # Name
                if self.nameText() is not None:
                    textMaxWidth = self._xMenuPos - x_0
                    self.widget().setFont(self.widget()._gui_qt___gui_qt__wgt__name_font)
                    textWidth = self._textWidth(self.nameText())
                    rectWidth = min(textMaxWidth, textWidth)
                    self.nameTextRect().setRect(
                        x_0, y_0,
                        rectWidth, frameWidth
                    )
                    x_0 += (rectWidth + spacing)
                # Index
                if self.indexText() is not None:
                    textMaxWidth = self._xMenuPos - x_0
                    self.widget().setFont(self.widget()._wgt__index_font)
                    textWidth = self._textWidth(self.indexText())
                    rectWidth = min(textMaxWidth, textWidth)
                    self.indexTextRect().setRect(
                        x_0, y_0,
                        rectWidth, frameWidth
                    )
            else:
                x, y = w_0 - menuHeight - sdr, y_0
                w, h = menuHeight, h_0 - sdr
                #
                x_0 += side
                # Icon
                if self.icon() is not None:
                    self.iconRect().setRect(
                        x_0 + _w, y_0 + _h,
                        iconWidth, iconHeight
                    )
                    x_0 += (frameWidth + spacing)
                # Name
                if self.nameText() is not None:
                    self.widget().setFont(self.widget()._gui_qt___gui_qt__wgt__name_font)
                    textWidth = self._textWidth(self.nameText())
                    rectWidth = textWidth
                    self.nameTextRect().setRect(
                        x_0, y_0,
                        rectWidth, frameWidth
                    )
                    x_0 += (rectWidth + spacing)
                # Index
                if self.indexText() is not None:
                    self.widget().setFont(self.widget()._wgt__index_font)
                    textWidth = self._textWidth(self.indexText())
                    rectWidth = textWidth
                    self.indexTextRect().setRect(
                        x_0, y_0,
                        rectWidth, frameWidth
                    )
                    x_0 += (textWidth + spacing)
                #
                self._xTranslate, self._yTranslate = w_0 - menuHeight - sdr, h_0 - sdr
            #
            self._uiMenuRect.setRect(
                x, y,
                w, h
            )
        else:
            self._uiMenuRect.setRect(0, 0, 0, 0)
    #
    def _gui_qt__mdl__set_status_objs_geometry_update_(self):
        if self.isStatusEnable() and self.isExpanded():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()
            x_0, y_0, w_0, h_0 = self._gui_qt__mdl__get_widget_geometry_args_(xPos, yPos, width, height)
            w_0 -= 1
            h_0 -= 1
            #
            buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
            #
            spacing = self._uiSpacing
            sdr = self._shadowRadius()
            #
            x_0 += self._uiSide
            y_1 = y_0 + (h_0 - self._wgt__menu_height - sdr + (self._wgt__menu_height - buttonHeight)/2)
            self._helpButton.show()
            #
            self._helpButton.setGeometry(
                x_0, y_1,
                buttonWidth, buttonHeight
            )
            #
            if self.isDialogEnable():
                statusWidth, statusHeight = w_0 - sdr, self._wgt__status_height
                if self._layoutDirection == qtCore.Vertical:
                    statusWidth -= self._wgt__menu_height

                dialogButtonWidth = 96
                x_0 = statusWidth - dialogButtonWidth - self._uiSide
                #
                self._cancelButton.show()
                self._cancelButton.setGeometry(
                    x_0, y_1,
                    dialogButtonWidth, buttonHeight
                )
                #
                x_0 -= (dialogButtonWidth + spacing)
                #
                self._confirmButton.show()
                self._confirmButton.setGeometry(
                    x_0, y_1,
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
    def _gui_qt__mdl__set_status_rect_geometry_update_(self):
        if self.isStatusEnable() and self.isExpanded():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()

            x_0, y_0, w_0, h_0 = self._gui_qt__mdl__get_widget_geometry_args_(xPos, yPos, width, height)
            w_0 -= 1
            h_0 -= 1

            std_h = self._wgt__status_height
            #
            buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
            sdr = self._shadowRadius()
            #
            y_1 = y_0 + (h_0 - (std_h + sdr))
            #
            buttonWidth, buttonHeight = buttonWidth, buttonHeight
            #
            statusWidth, statusHeight = w_0 - sdr, std_h
            if self._layoutDirection == qtCore.Vertical:
                statusWidth -= self._wgt__menu_height
            #
            self.statusRect().setRect(
                x_0, y_1,
                statusWidth, std_h
            )
            #
            self.statusTextRect().setRect(
                x_0 + buttonWidth, y_1 + (statusHeight - buttonHeight)/2,
                self._uiStatusTextWidth, buttonHeight
            )
    #
    def _updatePercentRectGeometry(self):
        if self.isPercentEnable():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()
            x_0, y_0, w_0, h_0 = self._gui_qt__mdl__get_widget_geometry_args_(xPos, yPos, width, height)
            #
            w_0 -= 1
            h_0 -= 1
            #
            menuWidth, menuHeight = self._wgt__menu_width, self._wgt__menu_height
            #
            sdr = self._shadowRadius()
            #
            if self.layoutDirection() == qtCore.Horizontal:
                maxWidth = w_0 - sdr
                percent = min(float(self._uiProgressValue) / float(self._uiMaxProgressValue), 1)
                #
                self._uiPercentValueRect.setRect(
                    x_0 + 1, y_0 + self._wgt__menu_height - 2,
                    maxWidth * percent, 1
                )
            else:
                maxHeight = h_0 - sdr
                percent = min(float(self._uiProgressValue) / float(self._uiMaxProgressValue), 1)
                #
                self._uiPercentValueRect.setRect(
                    x_0 + (w_0 - (menuHeight + sdr)), y_0,
                    1, maxHeight * percent
                )
    #
    def _gui_qt__mdl__set_viewport_geometry_update_(self):
        if self.isExpanded():
            xPos, yPos = 0, 0
            width, height = self.width(), self.height()
            #
            menuWidth, menuHeight = self._wgt__menu_width, self._menuHeight()
            statusWidth, statusHeight = self._wgt__status_width, self._wgt__status_height
            #
            sdr = self._shadowRadius()
            self.viewport().show()

            if self.layoutDirection() is qtCore.Horizontal:
                x, y = xPos, yPos + menuHeight
                w = width - sdr
                #
                if self.isStatusEnable():
                    h = height - (menuHeight + statusHeight) - sdr
                else:
                    h = height - menuHeight - sdr
            else:
                x, y = xPos, yPos
                w = width - menuHeight - sdr
                #
                if self.isStatusEnable():
                    h = height - statusHeight - sdr
                else:
                    h = height - sdr

            self.viewport().setGeometry(*self._gui_qt__mdl__get_viewport_geometry_args_(x, y, w, h))
        else:
            self.viewport().hide()
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._gui_qt__mdl__set_rect_geometry_update_()
        self._gui_qt__mdl__set_resize_rect_geometry_update_()
        #
        self._gui_qt__mdl__set_menu_objs_geometry_update_()
        self._gui_qt__mdl__set_menu_rect_geometry_update_()
        #
        self._gui_qt__mdl__set_status_objs_geometry_update_()
        self._gui_qt__mdl__set_status_rect_geometry_update_()
        #
        self._gui_qt__mdl__set_viewport_geometry_update_()
        #
        self._updatePercentRectGeometry()
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
        self.setMoveable(not boolean)
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
            wl, wt, wr, wb = self.widgetMargins()
            if self._isExpanded is True:
                sdr = self._shadowRadius()
                #
                if self.layoutDirection() is qtCore.Horizontal:
                    width, height = self._wgt__menu_width + wl + wr, self._wgt__menu_height + wt + wb + sdr + 1
                else:
                    width, height = self._wgt__menu_height + wt + wb + sdr + 1, self._wgt__menu_width + wl + wr
                #
                self._wgt__frame_w_, self._wgt__frame_h_ = currentWidth, currentHeight
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
                width, height = self._wgt__frame_w_, self._wgt__frame_h_
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
    def _menuHeight(self):
        if self.isMenuEnable():
            return self._wgt__menu_height
        return 0
    #
    def _shadowRadius(self):
        if self.isMaximized():
            return 0
        elif self.isShadowEnable():
            return 4
        return 0
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
        self._gui_qt__mdl__set_geometry_update_()
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