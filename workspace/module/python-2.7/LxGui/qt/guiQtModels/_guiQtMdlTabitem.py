# coding:utf-8
from LxGui.qt import qtCore, guiQtMdlAbs


class _QtButtontabModel(guiQtMdlAbs.Abs_GuiQtTabWgtModel):
    def __init__(self, widget):
        self._initTabModelBasic(widget)
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self._uiIconKeyword = iconKeywordStr
        if self._uiIconKeyword is not None:
            self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword)
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
            self.widget()._wgt__name_rgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            r1, g1, b1, a1 = 143, 143, 143, 255
            r2, g2, b2, a2 = 255, 255, 255, 255
            if state is qtCore.CurrentState:
                self.widget()._wgt__background_rgba = 71, 71, 71, 255
                self.widget()._wgt__border_rgba = [(r1 * .75, g1 * .75, b1 * .75, a1), (r1, g1, b1, a1)][self.isPressHovered()]
                self.widget()._wgt__name_rgba = [(63, 127, 255, 255), (r2, g2, b2, a2)][self.isPressHovered()]
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + ['cur', 'on'][self.isPressHovered()])
            elif state is qtCore.NormalState:
                self.widget()._wgt__background_rgba = 63, 63, 63, 255
                self.widget()._wgt__border_rgba = [(r1 * .5, g1 * .5, b1 * .5, a1), (r1 * .75, g1 * .75, b1 * .75, a1)][self.isPressHovered()]
                self.widget()._wgt__name_rgba = [(r2*.75, g2*.75, b2*.75, a2), (r2, g2, b2, a2)][self.isPressHovered()]
                #
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + ['', 'on'][self.isPressHovered()])
            #
            self.widget()._uiFontItalic = False


class _QtShelftabModel(guiQtMdlAbs.Abs_GuiQtTabWgtModel):
    def __init__(self, widget):
        self._initTabModelBasic(widget)
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
                self.widget().setFont(qtCore.qtFont(size=8, weight=50, family=qtCore._families[2]))
            else:
                # noinspection PyArgumentEqualDefault
                self.widget().setFont(qtCore.qtFont(size=10, weight=50, family=qtCore._families[2]))
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
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
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
            self._menuButton.setIcon('svg_basic/tabmenu_h')
        else:
            self._closeButton.setGeometry(
                xPos + 2, yPos + 2,
                10, 10
            )
            self._menuButton.setGeometry(
                xPos + (w - frameWidth)/2, yPos + w,
                frameWidth, frameHeight
            )
            self._menuButton.setIcon('svg_basic/menu_d')
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
            r2, g2, b2, a2 = 223, 223, 223, 255
            if state is qtCore.CurrentState:
                self.widget()._wgt__name_rgba = [(63, 127, 255, 255), (r2, g2, b2, a2)][self.isPressHovered()]
                self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + ['cur', 'on'][self.isPressHovered()])
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + ['cur', 'on'][self.isPressHovered()])
            elif state is qtCore.NormalState:
                self.widget()._wgt__name_rgba = [(r2*.5, g2*.5, b2*.5, a2), (r2 * .75, g2 * .75, b2 * .75, a2)][self.isPressHovered()]
                if self._uiIconKeyword is not None:
                    self._uiIcon = qtCore._toLxOsIconFile(self._uiIconKeyword + ['', 'on'][self.isPressHovered()])
            #
            self.widget()._uiFontItalic = False
