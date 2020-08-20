# coding:utf-8
from LxGui.qt import qtCore, guiQtMdlAbs


class QtButtonTabbarModel(guiQtMdlAbs.AbsGuiQtTabbarWgtModel):
    def __init__(self, widget):
        self._initTabBarModelBasic(widget)


# Tab Bar
class QtShelfTabbarModel(guiQtMdlAbs.AbsGuiQtTabbarWgtModel):
    def __init__(self, widget):
        self._initTabBarModelBasic(widget)
        #
        self.__overrideAttr()
    #
    def __overrideAttr(self):
        self._isHScrollEnable, self._isVScrollEnable = True, True
    #
    def _gui_qt__mdl__set_rect_geometry_update_(self):
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
class QtButtonTabGroupModel(guiQtMdlAbs.AbsGuiQtTabgroupMdl):
    def __init__(self, widget):
        self._initAbsGuiQtTabgroupMdl(widget)


#
class QtShelfTabGroupModel(guiQtMdlAbs.AbsGuiQtTabgroupMdl):
    def __init__(self, widget):
        self._initAbsGuiQtTabgroupMdl(widget)
    #
    def _gui_qt__mdl__set_viewport_geometry_update_(self):
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        w, h = self._uiTabBarWidth, self._uiTabBarHeight
        buttonWidth, buttonHeight = self._uiButtonWidth, self._uiButtonHeight
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            _w = (h - buttonWidth)/2
            scrollWidth, scrollHeight = buttonWidth * 3 + _w * 2, h
            # Choose Tab
            self.widget()._chooseTabbuttonWgtObj.setGeometry(
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
            _h = (w - buttonHeight)/2
            scrollWidth, scrollHeight = w, buttonHeight*3 + _h*2
            #
            self.scrollRect().setRect(
                xPos - 1, yPos + height - scrollHeight,
                scrollWidth, scrollHeight
            )
    #
    def _gui_qt__mdl__set_child_wgts_geometry_update_(self):
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
        self._scrollSubTimer, self._scrollAddTimer = qtCore.CLS_timer(self._widget), qtCore.CLS_timer(self._widget)
    #
    def setTabPosition(self, value):
        self.tabBar().viewModel().setTabPosition(value)
        if self.tabPosition() is qtCore.South or self.tabPosition() is qtCore.North:
            self._subScrollButton.setIcon('svg_basic/hscrollsub'), self._addScrollButton.setIcon('svg_basic/hscrolladd')
        else:
            self._subScrollButton.setIcon('svg_basic/vscrollsub'), self._addScrollButton.setIcon('svg_basic/vscrolladd')


