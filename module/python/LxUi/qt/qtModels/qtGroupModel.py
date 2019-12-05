# coding:utf-8
from LxUi.qt import qtCore
#
from LxUi.qt.qtBasic import qtModelBasic


#
class QtToolboxGroupModel(qtModelBasic._QtGroupModelBasic):
    def __init__(self, widget):
        self._initGroupModelBasic(widget)
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
    def _updateRectGeometry(self):
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
            self.widget().setFont(self.widget()._uiNameTextFont)
            textWidth = self.widget().fontMetrics().width(self._uiNameText)

            drawTextWidth = min(textWidth, self._xMenuPos - xPos)
            self.nameTextRect().setRect(
                xPos, yPos,
                drawTextWidth, frameHeight
            )
            xPos += drawTextWidth + spacing
        # Index
        if self.indexText() is not None:
            self.widget().setFont(self.widget()._uiIndexTextFont)
            textWidth = self.widget().fontMetrics().width(self._uiIndexText)
            self.indexTextRect().setRect(
                xPos, yPos,
                textWidth, frameHeight
            )
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
            self._uiExpandIcon = self._uiMethod._toLxOsIconFile('svg_basic@svg#toolGroupCloseOff')
        else:
            r1, g1, b1, a1 = 143, 143, 143, 255
            r2, g2, b2, a2 = 223, 223, 223, 255
            if state is qtCore.ExpandedState:
                self._uiExpandIconKeyword = 'svg_basic@svg#toolGroupOpen'
                #
                self.widget()._uiBackgroundRgba = 71, 71, 71, 255
                self.widget()._uiBorderRgba = [(r1*.75, g1*.75, b1*.75, a1), (r1, g1, b1, a1)][self.isExpandHovered()]
                #
                self.widget()._uiNameRgba = [(r2*.75, g2*.75, b2*.75, a1), (r2, g2, b2, a2)][self.isExpandHovered()]
            elif state is qtCore.UnexpandState:
                self._uiExpandIconKeyword = 'svg_basic@svg#toolGroupClose'
                #
                self.widget()._uiBackgroundRgba = 0, 0, 0, 0
                self.widget()._uiBorderRgba = [(r1*.5, g1*.5, b1*.5, a1), (r1*.75, g1*.75, b1*.75, a1)][self.isExpandHovered()]
                #
                self.widget()._uiNameRgba = [(r2*.5, g2*.5, b2*.5, a1), (r2 * .75, g2 * .75, b2 * .75, a1)][self.isExpandHovered()]
            #
            self._uiExpandIcon = qtCore._toLxOsIconFile(self._uiExpandIconKeyword + ['', 'on'][self.isExpandHovered()])


#
class QtToolboxModel(qtModelBasic._QtGroupModelBasic):
    def __init__(self, widget):
        self._initGroupModelBasic(widget)
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
            self._uiExpandIcon = self._uiMethod._toLxOsIconFile('svg_basic@svg#expandCloseOff')
        else:
            r, g, b, a = self.widget()._uiColorBackgroundRgba
            r1, g1, b1, a1 = 143, 143, 143, 255
            r2, g2, b2, a2 = 223, 223, 223, 255
            if state is qtCore.ExpandedState:
                self._uiExpandIconKeyword = 'svg_basic@svg#expandOpen'
                #
                self.widget()._uiBackgroundRgba = [(0, 0, 0, 0), (r * .25, g * .25, b * .25, a)][self.isExpandHovered()]
                self.widget()._uiBorderRgba = [(r * .5, g * .5, b * .5, a), (r * .75, g * .75, b * .75, a)][self.isExpandHovered()]
                #
                self.widget()._uiNameRgba = [(r2*.75, g2*.75, b2*.75, a1), (r2, g2, b2, a2)][self.isExpandHovered()]
            elif state is qtCore.UnexpandState:
                self._uiExpandIconKeyword = 'svg_basic@svg#expandClose'
                #
                self.widget()._uiBackgroundRgba = 0, 0, 0, 0
                self.widget()._uiBorderRgba = 0, 0, 0, 0
                #
                self.widget()._uiNameRgba = [(r2*.5, g2*.5, b2*.5, a1), (r2 * .75, g2 * .75, b2 * .75, a1)][self.isExpandHovered()]
            #
            self._uiExpandIcon = qtCore._toLxOsIconFile(self._uiExpandIconKeyword + ['', 'on'][self.isExpandHovered()])
            #
            self.widget()._uiViewportBorderRgba = self.widget()._uiBorderRgba


#
class QtButtonTabBarModel(qtModelBasic._QtTabBarModelBasic):
    def __init__(self, widget):
        self._initTabBarModelBasic(widget)


# Tab Bar
class QtShelfTabBarModel(qtModelBasic._QtTabBarModelBasic):
    def __init__(self, widget):
        self._initTabBarModelBasic(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        self._isHScrollEnable, self._isVScrollEnable = True, True
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
        self._uiTabPathLis = []
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            xPos0, xPos1 = w*currentItemIndex - xValue, w*(currentItemIndex + 1) - xValue
            yPos0 = [0, h][currentItemIndex > 0]
            #
            pointLis = (
                (xPos, yPos - 1),
                (xPos + h, yPos0 - 1),
                (xPos0 - h, yPos0 - 1),
                (xPos0, -1),
                (xPos1, -1),
                (xPos1 + h, h - 1),
                (width, h)
            )
            path = qtCore.QPainterPath_()
            path._addPoints(pointLis)
            self._uiTabBarPath = path
            #
            if self.itemIndexes():
                for itemIndex in self.itemIndexes():
                    xPos0, xPos1 = w*itemIndex - xValue, w*(itemIndex + 1) - xValue
                    if itemIndex > currentItemIndex:
                        pointLis = [
                            (xPos0 + h, h - 1),
                            (xPos0, yPos - 1),
                            (xPos1, yPos - 1),
                            (xPos1 + h, h - 1)
                        ]
                    elif itemIndex < currentItemIndex:
                        if itemIndex == 0:
                            pointLis = [
                                (xPos0 + h, h - 1),
                                (xPos0, yPos - 1),
                                (xPos1, yPos - 1),
                                (xPos1 - h, h - 1)
                            ]
                        else:
                            pointLis = [
                                (xPos0 - h, h - 1),
                                (xPos0, yPos - 1),
                                (xPos1, yPos - 1),
                                (xPos1 - h, h - 1)
                            ]
                    else:
                        if itemIndex == 0:
                            pointLis = [
                                (xPos0 + h, h - 1),
                                (xPos0, yPos - 1),
                                (xPos1, yPos - 1),
                                (xPos1 + h, h - 1)
                            ]
                        else:
                            pointLis = [
                                (xPos0 - h, h - 1),
                                (xPos0, yPos - 1),
                                (xPos1, yPos - 1),
                                (xPos1 + h, h - 1)
                            ]
                    #
                    if pointLis:
                        path = qtCore.QPainterPath_()
                        path._addPoints(pointLis)
                        #
                        self._uiTabPathLis.append(path)
        else:
            yPos0, yPos1 = h * currentItemIndex - yValue + 2, h * (currentItemIndex + 1) - yValue + 2
            #
            pointLis = [
                (w - 1, yPos - 1),
                (w - 1, yPos0 - w),
                (xPos - 1, yPos0),
                (xPos - 1, yPos1 - w),
                (w - 1, yPos1),
                (w - 1, height)
            ]
            path = qtCore.QPainterPath_()
            path._addPoints(pointLis)
            self._uiTabBarPath = path
            #
            if self.itemIndexes():
                for itemIndex in self.itemIndexes():
                    yPos0, yPos1 = h * itemIndex - yValue + 2, h * (itemIndex + 1) - yValue + 2
                    if itemIndex > currentItemIndex:
                        pointLis = [
                            (w - 1, yPos0),
                            (xPos - 1, yPos0 - w),
                            (xPos - 1, yPos1 - w),
                            (w - 1, yPos1)
                        ]
                    elif itemIndex < currentItemIndex:
                        pointLis = [
                            (w - 1, yPos0 - w),
                            (xPos - 1, yPos0),
                            (xPos - 1, yPos1),
                            (w - 1, yPos1 - w)
                        ]
                    else:
                        pointLis = [
                            (w - 1, yPos0 - w),
                            (xPos - 1, yPos0),
                            (xPos - 1, yPos1 - w),
                            (w - 1, yPos1)
                        ]
                    #
                    if pointLis:
                        path = qtCore.QPainterPath_()
                        path._addPoints(pointLis)
                        #
                        self._uiTabPathLis.append(path)


# Tab View
class QtButtonTabGroupModel(qtModelBasic._QtTabGroupModelBasic):
    def __init__(self, widget):
        self._initTabViewModelBasic(widget)


#
class QtShelfTabGroupModel(qtModelBasic._QtTabGroupModelBasic):
    def __init__(self, widget):
        self._initTabViewModelBasic(widget)
    #
    def _updateViewportGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        w, h = self._uiTabBarWidth, self._uiTabBarHeight
        buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            _w = (h - buttonWidth)/2
            scrollWidth, scrollHeight = buttonWidth * 3 + _w * 2, h
            # Choose Tab
            self.widget()._chooseTab.setGeometry(
                xPos, yPos,
                min(w, width - scrollWidth), h
            )
            # Tab Bar
            self.tabBar().setGeometry(
                xPos + w, yPos,
                width - w - scrollWidth, h
            )
            #
            self.viewport().setGeometry(
                xPos, yPos + h,
                width, height - h
            )
            #
            if self.tabWidgets():
                for i in self.tabWidgets():
                    i.setGeometry(
                        0, 0,
                        width - 1, height - h - 1
                    )
        else:
            _h = (w - buttonHeight) / 2
            scrollWidth, scrollHeight = w, buttonHeight * 3 + _h * 2
            # Tab Bar
            self.tabBar().setGeometry(
                xPos, yPos,
                w, height - scrollHeight
            )
            #
            self.viewport().setGeometry(
                xPos + w, yPos,
                width - w, height
            )
            #
            if self.tabWidgets():
                for i in self.tabWidgets():
                    i.setGeometry(
                        0, 0,
                        width - w - 1, height - 1
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
            _h = (w - buttonHeight)/2
            scrollWidth, scrollHeight = w, buttonHeight*3 + _h*2
            #
            self.scrollRect().setRect(
                xPos - 1, yPos + height - scrollHeight,
                scrollWidth, scrollHeight
            )
    #
    def _updateChildrenGeometry(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        w, h = self._uiTabBarWidth,  self._uiTabBarHeight
        buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            _w = (h - buttonWidth)/2
            _h = (h - buttonHeight)/2
            #
            self._addButton.setGeometry(
                xPos + width - buttonWidth*3 - _w, yPos + _h,
                buttonWidth, buttonWidth
            )
            #
            self._subScrollButton.setGeometry(
                xPos + width - buttonWidth*2 - _w, yPos + _h,
                buttonWidth, buttonWidth
            )
            #
            self._addScrollButton.setGeometry(
                xPos + width - buttonWidth - _w, yPos + _h,
                buttonWidth, buttonWidth
            )
        else:
            _w = (w - buttonWidth)/2
            _h = (w - buttonHeight)/2
            #
            self._addButton.setGeometry(
                xPos + _w, yPos + height - buttonHeight*3 - _h,
                buttonWidth, buttonWidth
            )
            #
            self._subScrollButton.setGeometry(
                xPos + _w, yPos + height - buttonHeight*2 - _h,
                buttonWidth, buttonWidth
            )
            #
            self._addScrollButton.setGeometry(
                xPos + _w, yPos + height - buttonHeight - _h,
                buttonWidth, buttonWidth
            )
    #
    def _updateScrollButtonState(self):
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            self._subScrollButton.setPressable(not self.tabBar().viewModel().isVMinimum()), self._addScrollButton.setPressable(not self.tabBar().viewModel().isVMaximum())
        else:
            self._subScrollButton.setPressable(not self.tabBar().viewModel().isHMinimum()), self._addScrollButton.setPressable(not self.tabBar().viewModel().isHMaximum())
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
        self._updateScrollButtonState()
        #
        self._updateWidgetState()
    #
    def setWidget(self, widget):
        self._widget = widget
        #
        self._tabBar = self.widget()._tabBar
        #
        self._addButton = widget._addButton
        #
        self._subScrollButton, self._addScrollButton = self.widget()._subScrollButton, self.widget()._addScrollButton
        self._scrollSubTimer, self._scrollAddTimer = qtCore.QtCore.QTimer(self._widget), qtCore.QtCore.QTimer(self._widget)
    #
    def setTabPosition(self, value):
        self.tabBar().viewModel().setTabPosition(value)
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            self._subScrollButton.setIcon('svg_basic@svg#hScrollSub'), self._addScrollButton.setIcon('svg_basic@svg#hScrollAdd')
        else:
            self._subScrollButton.setIcon('svg_basic@svg#vScrollSub'), self._addScrollButton.setIcon('svg_basic@svg#vScrollAdd')
