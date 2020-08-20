# coding:utf-8
from LxGui.qt import qtCore, guiQtMdlAbs


#
class QtToolboxGroupModel(guiQtMdlAbs.AbsGuiQtGroupMdl):
    def __init__(self, widget):
        self._initAbsGuiQtGroupMdl(widget)
        self._overrideAttr()
    #
    def _overrideAttr(self):
        self.setGroupSpacing(0)
        #
        self.setExpandButton(True)
        self.setExpandEnable(True)
        self.setExpandable(True)
        #
        self.setFrameSize(24, 24)
        #
        self.setWidgetLayoutMargins(0, 24, 0, 0)
        #
        self.setViewportLayoutMargins(0, 0, 0, 0)
        self.setViewportLayoutSpacing(0)
        #
        self.setExpandedSizePolicy(qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding)
        self.setUnexpandedSizePolicy(qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Fixed)
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.size()
        width -= 1
        height -= 1
        #
        self.basicRect().setRect(
            xPos, yPos,
            width, height - self._uiGroupSpacing
        )
        #
        side, spacing = self._uiSide, self._uiSpacing
        frameWidth, frameHeight = self.frameSize()
        buttonWidth, buttonHeight = self.buttonSize()
        iconWidth, iconHeight = self.iconSize()
        # Expand
        if self.isExpandable():
            _w, _h = (frameWidth - iconWidth) / 2, (frameHeight - iconHeight) / 2
            self.expandRect().setRect(
                xPos + _w, yPos + _h,
                iconWidth, iconHeight
            )
            self.expandPressRect().setRect(
                xPos, yPos,
                width, frameHeight - 1
            )
            xPos += buttonWidth + spacing
        # Name
        if self.nameText() is not None:
            self.widget().setFont(self.widget()._gui_qt___gui_qt__wgt__name_font)
            textWidth = self.widget().fontMetrics().width(self._gui_qt__mdl__name_str_)

            drawTextWidth = min(textWidth, self._xMenuPos - xPos)
            self.nameTextRect().setRect(
                xPos, yPos,
                drawTextWidth, frameHeight
            )
            xPos += drawTextWidth + spacing
        # Index
        if self.indexText() is not None:
            self.widget().setFont(self.widget()._gui_qt__mdl__index_str_Font)
            textWidth = self.widget().fontMetrics().width(self._gui_qt__mdl__index_str_)
            self.indexTextRect().setRect(
                xPos, yPos,
                textWidth, frameHeight
            )
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
        _w, _h = (frameWidth - buttonWidth)/2, (frameHeight - buttonHeight)/2
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
        self._xMenuPos = xPos
    #
    def _setQtExpandStyle(self, state):
        if state is qtCore.UnexpandableState:
            self._uiExpandIcon = qtCore._toLxOsIconFile('svg_basic/toolgroupcloseoff')
        else:
            r1, g1, b1, a1 = 143, 143, 143, 255
            r2, g2, b2, a2 = 223, 223, 223, 255
            if state is qtCore.ExpandedState:
                self._uiExpandIconKeyword = 'svg_basic/toolgroupopen'
                #
                self.widget()._wgt__background_rgba = 71, 71, 71, 255
                self.widget()._wgt__border_rgba = [(r1*.75, g1*.75, b1*.75, a1), (r1, g1, b1, a1)][self.isExpandHovered()]
                #
                self.widget()._wgt__name_rgba = [(r2*.75, g2*.75, b2*.75, a1), (r2, g2, b2, a2)][self.isExpandHovered()]
            elif state is qtCore.UnexpandState:
                self._uiExpandIconKeyword = 'svg_basic/toolgroupclose'
                #
                self.widget()._wgt__background_rgba = 0, 0, 0, 0
                self.widget()._wgt__border_rgba = [(r1*.5, g1*.5, b1*.5, a1), (r1*.75, g1*.75, b1*.75, a1)][self.isExpandHovered()]
                #
                self.widget()._wgt__name_rgba = [(r2*.5, g2*.5, b2*.5, a1), (r2 * .75, g2 * .75, b2 * .75, a1)][self.isExpandHovered()]
            #
            self._uiExpandIcon = qtCore._toLxOsIconFile(self._uiExpandIconKeyword + ['', 'on'][self.isExpandHovered()])


#
class QtToolboxModel(guiQtMdlAbs.AbsGuiQtGroupMdl):
    def __init__(self, widget):
        self._initAbsGuiQtGroupMdl(widget)
        self._overrideAttr()
    #
    def _overrideAttr(self):
        self.setGroupSpacing(0)
        #
        self.setColorEnable(True)
        #
        self.setExpandButton(True)
        self.setExpandEnable(True)
        self.setExpandable(True)
        self.setExpanded(True)
        #
        self.setWidgetLayoutMargins(0, 20, 0, 0)
        #
        self.setViewportLayoutMargins(4, 4, 4, 4)
        self.setViewportLayoutSpacing(4)
    #
    def setViewportLayout(self, widget):
        if hasattr(widget, '_viewportLayout'):
            self._viewportLayout = widget._viewportLayout
        else:
            self._viewportLayout = qtCore.QGridLayout(self._viewport)
        #
        self._viewportLayout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self._viewportLayout.setContentsMargins(0, 0, 0, 0)
        self._viewportLayout.setSpacing(0)
    #
    def _setQtExpandStyle(self, state):
        if state is qtCore.UnexpandableState:
            self._uiExpandIcon = qtCore._toLxOsIconFile('svg_basic/expandcloseoff')
        else:
            r, g, b, a = self.widget()._wgt__color__background_rgba
            r1, g1, b1, a1 = 143, 143, 143, 255
            r2, g2, b2, a2 = 223, 223, 223, 255
            if state is qtCore.ExpandedState:
                self._uiExpandIconKeyword = 'svg_basic/expandopen'
                #
                self.widget()._wgt__background_rgba = [(0, 0, 0, 0), (r * .25, g * .25, b * .25, a)][self.isExpandHovered()]
                self.widget()._wgt__border_rgba = [(r * .5, g * .5, b * .5, a), (r * .75, g * .75, b * .75, a)][self.isExpandHovered()]
                #
                self.widget()._wgt__name_rgba = [(r2*.75, g2*.75, b2*.75, a1), (r2, g2, b2, a2)][self.isExpandHovered()]
            elif state is qtCore.UnexpandState:
                self._uiExpandIconKeyword = 'svg_basic/expandclose'
                #
                self.widget()._wgt__background_rgba = 0, 0, 0, 0
                self.widget()._wgt__border_rgba = 0, 0, 0, 0
                #
                self.widget()._wgt__name_rgba = [(r2*.5, g2*.5, b2*.5, a1), (r2 * .75, g2 * .75, b2 * .75, a1)][self.isExpandHovered()]
            #
            self._uiExpandIcon = qtCore._toLxOsIconFile(self._uiExpandIconKeyword + ['', 'on'][self.isExpandHovered()])
            #
            self.widget()._uiViewportBorderRgba = self.widget()._wgt__border_rgba

