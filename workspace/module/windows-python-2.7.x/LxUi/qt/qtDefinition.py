# coding:utf-8
from LxBasic import bscMethods

from LxUi import uiCore
#
from LxUi.qt import qtCore

#
QtCore = qtCore.QtCore


# Widget
class QtDef_Widget(uiCore.UiMtdBasic):
    ui_method = uiCore.UiMtdBasic

    def _initDefWidget(self):
        self._initDefWidgetAttr()
        self._initDefWidgetAction()
        self._initDefWidgetRect()
        self._initDefWidgetUi()
        self._initDefWidgetVar()
    #
    def _initDefWidgetAttr(self):
        self._widget, self._viewport = [None] * 2
        #
        self._widgetLayout, self._viewportLayout = [None] * 2
        #
        self._viewModel = None
        #
        self._graphModelWidget = None
    #
    def _initDefWidgetAction(self):
        self._pressHoverPos = 0, 0
        self._pressClickPos = 0, 0
    #
    def _initDefWidgetRect(self):
        self._uiBasicRect, self._uiViewportRect, self._uiFrameRect = (
            QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1)
        )
        self._uiBasicPath = None
    #
    def _initDefWidgetUi(self):
        self._uiXPos, self._uiYPos = 0, 0
        self._uiWidth, self._uiHeight = 0, 0
        #
        self._uiWidthRecord, self._uiHeightRecord = 0, 0
        #
        self._uiOffset, self._uiSide, self._uiSpacing, self._uiShadowRadius = 0, 2, 2, 4
        #
        self._uiMargins = 0, 0, 0, 0
        #
        self._uiLayoutMargins = 0, 0, 0, 0
        self._uiLayoutSpacing = 0
    #
    def _initDefWidgetVar(self):
        self._isMultiFilterVisible = True
        #
        self._multiFilterDic = {}
    #
    def _updateWidgetState(self):
        self.widget().update()
    #
    def _toDrawText(self, rect, text):
        return self.widget().fontMetrics().elidedText(
            text, QtCore.Qt.ElideRight, rect.width(), QtCore.Qt.TextShowMnemonic
        )
    #
    def _textWidth(self, string):
        return self.widget().fontMetrics().width(string)
    #
    def _textHeight(self):
        return self.widget().fontMetrics().height()
    #
    def _isSizeChanged(self):
        width, height = self.size()
        if width == self._uiWidthRecord and height == self._uiHeightRecord:
            return False
        else:
            self._uiWidthRecord, self._uiHeightRecord = width, height
            return True
    #
    def _updateSizeRecord(self):
        self._uiWidthRecord, self._uiHeightRecord = self.size()
    #
    def _getEventPos(self, event):
        point = event.pos()
        x, y = point.x(), point.y()
        return x, y
    #
    def _clearHover(self):
        pass
    #
    def _updateHoverLoc(self, x, y):
        pass
    #
    def _updatePressLoc(self, x, y):
        pass
    #
    def _updateDragPressLoc(self, x, y):
        pass
    #
    def _hoverStartAction(self, event):
        pass
    #
    def _hoverExecuteAction(self, event):
        pass
    #
    def _hoverStopAction(self, event):
        pass
    #
    def _pressStartAction(self, event):
        pass
    #
    def _pressExecuteAction(self, event):
        pass
    #
    def _pressStopAction(self, event):
        pass
    #
    def _updateAction(self):
        pass
    #
    def _updateViewportGeometry(self):
        pass
    # Override
    def update(self):
        pass
    # Override
    def setWidget(self, widget):
        self._widget = widget
    #
    def widget(self):
        return self._widget
    #
    def widgetLayout(self):
        return self._widgetLayout
    #
    def setWidgetLayoutMargins(self, l, t, r, b):
        self._widgetLayout.setContentsMargins(l, t, r, b)
    #
    def setWidgetLayoutSpacing(self, px):
        self._widgetLayout.setSpacing(px)
    #
    def setMargins(self, l, t, r, b):
        self._uiMargins = l, t, r, b
    #
    def margins(self):
        return self._uiMargins
    #
    def setLayoutMargins(self, l, t, r, b):
        self._uiLayoutMargins = l, t, r, b
    #
    def layoutMargins(self):
        return self._uiLayoutMargins
    #
    def setLayoutSpacing(self, px):
        self._uiLayoutSpacing = px
    #
    def layoutSpacing(self):
        return self._uiLayoutSpacing
    #
    def setViewport(self, widget):
        if hasattr(widget, '_viewport'):
            self._viewport = widget._viewport
        else:
            self._viewport = qtCore.QWidget(self.widget())
        #
        self._viewport.setGeometry(0, 0, 0, 0)

        if qtCore.LOAD_INDEX is 0:
            self._viewport.setAttribute(QtCore.Qt.WA_TranslucentBackground | QtCore.Qt.WA_TransparentForMouseEvents)
        else:
            self._viewport.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self._viewport.setMouseTracking(True)
        #
        self._viewport.setFocusProxy(self.widget())
    #
    def viewport(self):
        return self._viewport
    #
    def setConnectViewport(self, widget):
        self._viewport = widget
        self._viewport.setParent(self.widget())
        self._viewport.setFocusProxy(self.widget())
    #
    def setViewportLayout(self, widget):
        if hasattr(widget, '_viewportLayout'):
            self._viewportLayout = widget._viewportLayout
        else:
            self._viewportLayout = qtCore.QVBoxLayout(self._viewport)
        #
        self._viewportLayout.setAlignment(QtCore.Qt.AlignTop)
        self._viewportLayout.setContentsMargins(0, 0, 0, 0)
        self._viewportLayout.setSpacing(0)
    #
    def viewportLayout(self):
        return self._viewportLayout
    #
    def setViewportLayoutMargins(self, l, t, r, b):
        self._viewportLayout.setContentsMargins(l, t, r, b)
    #
    def setViewportLayoutSpacing(self, px):
        self._viewportLayout.setSpacing(px)
    #
    def setVisible(self, boolean):
        self.widget().setVisible(boolean)
    #
    def isVisible(self):
        return self.widget().isVisible()
    #
    def size(self):
        return self.widget().width(), self.widget().height()
    #
    def width(self):
        return self.widget().width()
    #
    def height(self):
        return self.widget().height()
    #
    def pos(self):
        return self.widget().pos()
    #
    def x(self):
        return self.widget().x()
    #
    def y(self):
        return self.widget().y()
    #
    def basicRect(self):
        return self._uiBasicRect
    #
    def basicPath(self):
        return self._uiBasicPath
    #
    def viewportRect(self):
        return self._uiViewportRect
    #
    def viewportWidth(self):
        return self.widget().width() - self._uiMargins[0] - self._uiMargins[2]
    #
    def viewportHeight(self):
        return self.widget().height() - self._uiMargins[1] - self._uiMargins[3]
    #
    def pressClickPos(self):
        return self._pressClickPos
    #
    def pressHoverPos(self):
        return self._pressHoverPos


# Expand
class QtDef_ExpandWidget(QtDef_Widget):
    ui_method = uiCore.UiMtdBasic
    def _initDefExpandWidget(self):
        self._initDefWidget()
        #
        self._initDefExpandWidgetAttr()
        self._initDefExpandWidgetAction()
        self._initExpandAbsRect()
        self._initExpandAbsUi()
    #
    def _initDefExpandWidgetAttr(self):
        self._isExpandButton = False
        #
        self._isExpandEnable = False
        self._isExpandable = False
        self._isExpanded = False
        #
        self._isExpandHovered = False
        #
        self._expandTimer = qtCore.CLS_timer()
    #
    def _initDefExpandWidgetAction(self):
        self._expandFlag = False
    #
    def _initExpandAbsRect(self):
        self._uiExpandRect, self._uiExpandPressRect = QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1)
    #
    def _initExpandAbsUi(self):
        self._uiExpandFrameWidth, self._uiExpandFrameHeight = 20, 20
        self._uiExpandIconWidth, self._uiExpandIconHeight = 16, 16
        #
        self._uiExpandFrameWidth, self._uiExpandFrameHeight = 20.0, 20.0
        self._uiExpandIconKeyword = 'svg_basic@svg#expandClose'
        self._uiExpandIcon = qtCore._toLxOsIconFile(self._uiExpandIconKeyword)
        #
        self._uiUnexpandedSizePolicy = qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Fixed
        self._uiExpandedSizePolicy = qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Fixed
    # noinspection PyUnusedLocal
    def _updateExpandRect(self, xPos, yPos, width, height):
        frameWidth, frameHeight = self.expandFrameSize()
        w, h = self.expandIconSize()
        self.expandRect().setRect(
            xPos + (frameWidth - w) / 2, yPos + (frameHeight - h) / 2,
            w, h
        )
        if self.isExpandButton():
            self.expandPressRect().setRect(
                xPos, yPos,
                width - xPos, h
            )
        else:
            self.expandPressRect().setRect(
                xPos, yPos,
                w, h
            )
    # Override
    def _updateQtExpandStyle(self):
        if self.isExpandEnable():
            if self.isExpandable():
                self._setQtExpandStyle([qtCore.UnexpandState, qtCore.ExpandedState][self.isExpanded()])
            else:
                self._setQtExpandStyle(qtCore.UnexpandableState)
            #
            self._updateWidgetState()
    #
    def _setQtExpandStyle(self, state):
        if state is qtCore.UnexpandableState:
            self._uiExpandIcon = self.ui_method._toLxOsIconFile('svg_basic@svg#expandCloseOff')
        else:
            if state is qtCore.ExpandedState:
                self._uiExpandIconKeyword = 'svg_basic@svg#expandOpen'
            elif state is qtCore.UnexpandState:
                self._uiExpandIconKeyword = 'svg_basic@svg#expandClose'
            #
            self._uiExpandIcon = qtCore._toLxOsIconFile(self._uiExpandIconKeyword + ['', 'on'][self.isExpandHovered()])
    #
    def _expandClickSwitchAction(self):
        if self.isExpandable():
            self.setExpanded(not self._isExpanded)
    #
    def _expandClickAction(self):
        pass
    #
    def setExpandButton(self, boolean):
        self._isExpandButton = boolean
    #
    def isExpandButton(self):
        return self._isExpandButton
    #
    def setExpandEnable(self, boolean):
        self._isExpandEnable = boolean
    #
    def isExpandEnable(self):
        return self._isExpandEnable
    #
    def setExpandable(self, boolean):
        self._isExpandable = boolean
        #
        self._updateQtExpandStyle()
    #
    def setExpanded(self, boolean, ignoreAction=False):
        if not boolean == self._isExpanded:
            self._isExpanded = boolean
            if ignoreAction is False:
                self._expandClickAction()
        #
        self._updateQtExpandStyle()
    #
    def isExpanded(self):
        if self.isExpandable():
            return self._isExpanded
        else:
            return False
    #
    def isExpandable(self):
        if self.isExpandEnable():
            return self._isExpandable
        else:
            return False
    #
    def setExpandHovered(self, boolean):
        self._isExpandHovered = boolean
        #
        self._updateQtExpandStyle()
    #
    def isExpandHovered(self):
        return self._isExpandHovered
    #
    def expandIconKeyword(self):
        return self._uiExpandIconKeyword
    #
    def expandIcon(self):
        return self._uiExpandIcon
    #
    def expandFrameSize(self):
        return self._uiExpandFrameWidth, self._uiExpandFrameHeight
    #
    def expandIconSize(self):
        return self._uiExpandIconWidth, self._uiExpandIconHeight
    #
    def expandRect(self):
        return self._uiExpandRect
    #
    def expandPressRect(self):
        return self._uiExpandPressRect
    #
    def isExpandPressRectContain(self, pos):
        return qtCore.isRectContainPos(self.expandPressRect(), pos)
    #
    def setExpandedSizePolicy(self, *args):
        self._uiExpandedSizePolicy = args
    #
    def expandedSizePolicy(self):
        return self._uiExpandedSizePolicy
    #
    def setUnexpandedSizePolicy(self, *args):
        self._uiUnexpandedSizePolicy = args
    #
    def unexpandedSizePolicy(self):
        return self._uiUnexpandedSizePolicy


# Color
class QtDef_ColorWidget(QtDef_Widget):
    def _initDefColorWidget(self):
        self._initDefWidget()
        #
        self._initDefColorWidgetAttr()
        self._initColorAbsRect()
        self._initColorAbsUi()
    #
    def _initDefColorWidgetAttr(self):
        self._isColorEnable = False
        self._isColorable = False
        #
        self._isColorHovered = False
    #
    def _initColorAbsRect(self):
        self._uiColorRect = QtCore.QRect(-20, -20, 1, 1)
    #
    def _initColorAbsUi(self):
        self._uiColorFrameWidth, self._uiColorFrameHeight = 20, 20
        self._uiColorWidth, self._uiColorHeight = 12.0, 12.0
    #
    def _updateColorRect(self, xPos, yPos):
        frameWidth, frameHeight = self.colorFrameSize()
        w, h = self.colorSize()
        _w, _h = (frameWidth - w) / 2, (frameHeight - h) / 2
        self.colorRect().setRect(
            xPos + _w, yPos + _h,
            w, h
        )
    #
    def setColorEnable(self, boolean):
        self._isColorEnable = boolean
    #
    def isColorEnable(self):
        return self._isColorEnable
    #
    def setColorable(self, boolean):
        if not boolean == self._isColorable:
            self._isColorable = boolean
    #
    def isColorable(self):
        if self.isColorEnable():
            return self._isColorable
        else:
            return False
    #
    def setFilterColor(self, rgba):
        if rgba is not None:
            self.setColorEnable(True)
            #
            self.widget()._uiColorBackgroundRgba = rgba
        else:
            self.setColorEnable(False)
    #
    def colorFrameSize(self):
        return self._uiColorFrameWidth, self._uiColorFrameHeight
    #
    def colorSize(self):
        return self._uiColorWidth, self._uiColorHeight
    #
    def colorRect(self):
        return self._uiColorRect


# Press
class QtDef_PressWidget(QtDef_Widget):
    def _initDefPressWidget(self):
        self._initDefWidget()
        #
        self._initDefPressWidgetAttr()
        self._initDefPressWidgetAction()
        self._initDefPressWidgetRect()
        self._initDefPressWidgetUi()
        self._initDefPressWidgetVar()
    #
    def _initDefPressWidgetAttr(self):
        self._index, self._type, self._name = [None] * 3
        #
        self._isPressButton = False
        #
        self._isPressEnable = True
        self._isPressable = True
        self._isPressed = False
        #
        self._isPressHovered = False
        #
        self._isPressCurrent = False
        #
        self._isPressMenuEnable = False
    #
    def _initDefPressWidgetAction(self):
        self._clickedFlag, self._pressFlag, self._dragFlag, self._trackFlag = [False]*4
        #
        self._extendPressFlag = False
        #
        self._curPressChangeFlag, self._curHoverChangeFlag = [False]*2
        #
        self._separateSelectFlag, self._extraSelectFlag = False, False
    #
    def _initDefPressWidgetRect(self):
        self._uiIndexTextRect, self._uiTypeTextRect, self._uiNameTextRect = QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1)
        self._uiIconRect, self._uiSubIconRect, self._uiMenuIconRect = QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1)
    #
    def _initDefPressWidgetUi(self):
        self._uiIndexText, self._uiTypeText, self._uiNameText = [None] * 3
        #
        self._uiFrameWidth, self._uiFrameHeight = 20.0, 20.0
        #
        self._uiIndexTextWidth, self._uiTypeWidth, self._uiNameTextWidth = 32.0, 32.0, 32.0
        #
        self._uiIconKeyword, self._uiIcon = [None] * 2
        self._uiSubIconKeyword, self._uiSubIcon = [None] * 2
        self._uiMenuIconKeyword = 'svg_basic@svg#menu_mark'
        self._uiMenuIcon = self._toLxOsIconFile(self._uiMenuIconKeyword)
        #
        self._uiIconText = None
        #
        self._uiBasicIconWidth, self._uiBasicIconHeight = 16.0, 16.0
        self._uiIconWidth, self._uiIconHeight = 16.0, 16.0
        #
        self._uiPressStatus = qtCore.NormalStatus
        #
        self._uiMargins = 0, 0, 0, 0
    #
    def _initDefPressWidgetVar(self):
        self._filterKeyword = None
    #
    def _updateIconRect(self, xPos, yPos):
        frameWidth, frameHeight = self.frameSize()
        w, h = self.iconSize()
        self.iconRect().setRect(
            xPos + (frameWidth - w) / 2, yPos + (frameHeight - h) / 2,
            w, h
        )
    #
    def _updateMenuIconRect(self, xPos, yPos):
        w, h = self.iconSize()
        self.menuIconRect().setRect(
            xPos, yPos,
            w*.5, h*.5
        )
    # noinspection PyUnusedLocal
    def _updateNameTextRect(self, xPos, yPos, width, height):
        frameWidth, frameHeight = self.frameSize()
        self.nameTextRect().setRect(
            xPos, yPos,
            width - xPos, frameHeight
        )
    #
    def _updateViewportRect(self, xPos, yPos, width, height):
        l, t, r, b = self.margins()
        self.viewportRect().setRect(
            xPos + l, yPos + t,
            width - xPos - l - r, height - yPos - t - b
        )
    #
    def _toViewportGeometryArgs(self, x, y, w, h):
        l, t, r, b = self.margins()
        return x + l, y + t, w - l - r, h - t - b
    #
    def _updateQtPressStyle(self):
        if self.isPressEnable():
            if self.isPressable():
                if self.isPressed():
                    self._setQtPressStyle(qtCore.PressedState)
                else:
                    self._setQtPressStyle(qtCore.UnpressedState)
            else:
                self._setQtPressStyle(qtCore.UnpressableState)
        #
        self._updateWidgetState()
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            self.widget()._uiBackgroundRgba = 0, 0, 0, 0
            self.widget()._uiBorderRgba = 0, 0, 0, 0
            #
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            if state is qtCore.PressedState:
                self.widget()._uiBackgroundRgba = 0, 0, 0, 0
                self.widget()._uiBorderRgba = 0, 0, 0, 0
                #
                self.widget()._uiNameRgba = 255, 255, 255, 255
            elif state is qtCore.UnpressedState:
                self.widget()._uiBackgroundRgba = 0, 0, 0, 0
                self.widget()._uiBorderRgba = 0, 0, 0, 0
                #
                self.widget()._uiNameRgba = [(191, 191, 191, 255), (255, 255, 255, 255)][self.isPressHovered()]
            #
            self.widget()._uiFontItalic = False
    #
    def _updateQtPressStatus(self):
        status = self._uiPressStatus
        if status is qtCore.OffStatus:
            self.widget()._uiNameRgba = 95, 95, 95, 255
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
            self.widget()._uiNameRgba = [(r * .75, g * .75, b * .75, 255), (r, g, b, 255)][self.isPressHovered()]
    #
    def _setQtPressStatus(self, status):
        self._uiPressStatus = status
        #
        self._updateQtPressStyle()
    #
    def setIndex(self, number):
        self._index = int(number)
        #
        self.setIndexText(self._index + 1)
    #
    def index(self):
        return self._index
    #
    def setType(self, string):
        self._type = string
        #
        self.setTypeText(string)
    #
    def type(self):
        return self._type
    #
    def setName(self, string):
        self._name = string
        #
        self.setNameText(string)
    #
    def name(self):
        return self._name
    #
    def setIndexText(self, number):
        if number is not None:
            self._uiIndexText = unicode(number)
        #
        self._updateWidgetState()
    #
    def indexText(self):
        return self._uiIndexText
    #
    def indexTextRect(self):
        return self._uiIndexTextRect
    #
    def setIndexTextWidth(self, value):
        self._uiIndexTextWidth = value
    #
    def indexTextWidth(self):
        return self._uiIndexTextWidth
    #
    def setTypeText(self, string):
        if string is not None:
            self._uiTypeText = unicode(string)
        #
        self._updateWidgetState()
    #
    def typeText(self):
        return self._uiTypeText
    #
    def typeTextRect(self):
        return self._uiTypeTextRect
    #
    def setNameText(self, string):
        if string is not None:
            self._uiNameText = unicode(string)
        #
        self.update()
    #
    def nameText(self):
        return self._uiNameText
    #
    def nameTextRect(self):
        return self._uiNameTextRect
    #
    def setNameTextWidth(self, value):
        self._uiNameTextWidth = value
        self.update()
    #
    def nameTextWidth(self):
        return self._uiNameTextWidth
    #
    def drawNameText(self):
        return self._toDrawText(self.nameTextRect(), self.nameText())
    #
    def setFrameSize(self, w, h):
        self._uiFrameWidth, self._uiFrameHeight = w, h
    #
    def frameSize(self):
        return self._uiFrameWidth, self._uiFrameHeight
    #
    def setIconKeyword(self, iconKeyword):
        self._uiIconKeyword = iconKeyword
        #
        self.setIcon(self._uiIconKeyword)
    #
    def iconKeyword(self):
        return self._uiIconKeyword
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self._uiIconKeyword = iconKeyword
        if self._uiIconKeyword is not None:
            self._uiIcon = self._toLxOsIconFile(self._uiIconKeyword)
        else:
            self._uiIcon = None
        #
        self.setFrameSize(frameWidth, frameHeight)
        self.setIconSize(iconWidth, iconHeight)
        #
        self.update()
    #
    def icon(self):
        return self._uiIcon
    #
    def setIconText(self, text):
        self._uiIconText = text
    #
    def iconText(self):
        return self._uiIconText
    #
    def iconRect(self):
        return self._uiIconRect
    #
    def setSubIcon(self, iconKeyword):
        self._uiSubIconKeyword = iconKeyword
        if self._uiSubIconKeyword is not None:
            self._uiSubIcon = self._toLxOsIconFile(self._uiSubIconKeyword)
        else:
            self._uiSubIcon = None
        #
        self.update()
    #
    def subIcon(self):
        return self._uiSubIcon
    #
    def subIconRect(self):
        return self._uiSubIconRect
    #
    def menuIcon(self):
        return self._uiMenuIcon
    #
    def menuIconRect(self):
        return self._uiMenuIconRect
    #
    def setPressMenuEnable(self, boolean):
        self._isPressMenuEnable = boolean
    #
    def isPressMenuEnable(self):
        return self._isPressMenuEnable
    #
    def setIconSize(self, w, h):
        self._uiIconWidth, self._uiIconHeight = w, h
    #
    def iconSize(self):
        return self._uiIconWidth, self._uiIconHeight
    #
    def filterKeyword(self):
        return self._filterKeyword
    #
    def setPressEnable(self, boolean):
        self._isPressEnable = boolean
    #
    def isPressEnable(self):
        return self._isPressEnable
    #
    def setPressable(self, boolean):
        self._isPressable = boolean
        #
        self._updateQtPressStyle()
    #
    def isPressable(self):
        if self.isPressEnable():
            return self._isPressable
        else:
            return False
    #
    def setPressed(self, boolean):
        self._isPressed = boolean
    #
    def isPressed(self):
        if self.isPressable():
            return self._isPressed
        else:
            return False
    #
    def setPressHovered(self, boolean, *args):
        if not boolean == self._isPressHovered:
            self._isPressHovered = boolean
        #
        self._updateQtPressStyle()
    #
    def isPressHovered(self):
        return self._isPressHovered


# Check
class QtDef_CheckWidget(QtDef_Widget):
    def _initDefCheckWidget(self):
        self._initDefWidget()
        #
        self._initDefCheckWidgetAttr()
        self._initDefCheckWidgetAction()
        self._initDefCheckWidgetRect()
        self._initDefCheckWidgetUi()
        self._initDefCheckWidgetVar()
    #
    def _initDefCheckWidgetAttr(self):
        self._isCheckButton = False
        #
        self._isCheckEnable = False
        self._isCheckHovered = False
        self._isCheckable = True
        self._isChecked = False
        #
        self._isAutoExclusive = False
        self._isCheckStarted = False
        # Filter
        self._isViewFilterEnable = False
        self._isViewFilterable = False
        #
        self._itemFilterColumn = -1
        self._itemFilterRow = -1
        #
        self._filterViewWidget = None
        #
        self._viewFilterItemModelIndexLis = []
        self._viewFilterItemModelIndexCount = 0
    #
    def _initDefCheckWidgetAction(self):
        self._checkFlag = False
    #
    def _initDefCheckWidgetRect(self):
        self._uiCheckRect, self._uiCheckPressRect = QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1)
    #
    def _initDefCheckWidgetUi(self):
        self._uiCheckIconKeyword = 'svg_basic@svg#boxUnchecked'
        self._uiCheckIcon = self._toLxOsIconFile(self._uiCheckIconKeyword)
        #
        self._uiCheckFrameWidth, self._uiCheckFrameHeight = 16, 16
        self._uiCheckIconWidth, self._uiCheckIconHeight = 16, 16
    #
    def _initDefCheckWidgetVar(self):
        pass
    # For Override
    def _checkClickAction(self):
        pass
    # For Override
    def _checkExtendClickAction(self):
        pass
    #
    def _checkClickSwitchAction(self, isExtend=False):
        if self.isCheckable():
            if isExtend:
                self.setExtendCheck(not self._isChecked)
            else:
                self.setChecked(not self._isChecked)
    # For Override
    def _toggleClickAction(self):
        pass
    # For Override
    def _filterAction(self):
        pass
    # noinspection PyUnusedLocal
    def _updateCheckRect(self, xPos, yPos, width, height):
        frameWidth, frameHeight = self.checkFrameSize()
        w, h = self.checkIconSize()
        self.checkRect().setRect(
            xPos + (frameWidth - w) / 2, yPos + (frameHeight - h) / 2,
            w, h
        )
        if self.isCheckButton():
            self.checkPressRect().setRect(
                xPos, yPos,
                width - xPos, h
            )
        else:
            self.checkPressRect().setRect(
                xPos, yPos,
                w, h
            )
    #
    def _updateQtCheckStyle(self):
        if self.isCheckEnable():
            if self.isCheckable():
                self._setQtCheckStyle([qtCore.UncheckedState, qtCore.CheckedState][self.isChecked()])
            else:
                self._setQtCheckStyle(qtCore.UncheckableState)
        #
        self._updateWidgetState()
    #
    def _setQtCheckStyle(self, state):
        if state is qtCore.UncheckableState:
            self._uiCheckIconKeyword = ['svg_basic@svg#boxUncheckable', 'svg_basic@svg#radioUncheckable'][self.isAutoExclusive()]
            self._uiCheckIcon = self._toLxOsIconFile(self._uiCheckIconKeyword)
        else:
            if state is qtCore.CheckedState:
                self._uiCheckIconKeyword = ['svg_basic@svg#boxChecked', 'svg_basic@svg#radioChecked'][self.isAutoExclusive()]
            elif state is qtCore.UncheckedState:
                self._uiCheckIconKeyword = ['svg_basic@svg#boxUnchecked', 'svg_basic@svg#radioUnchecked'][self.isAutoExclusive()]
            #
            self._uiCheckIcon = self._toLxOsIconFile(self._uiCheckIconKeyword + ['', 'on'][self.isCheckHovered()])
    #
    def _updateViewFilterItemModelIndexCount(self):
        self._viewFilterItemModelIndexCount = len(self._viewFilterItemModelIndexLis)
        self.setViewFilterable(self._viewFilterItemModelIndexCount > 0)
    #
    def _updateViewMultiFilterVisible(self):
        filterViewWidget = self.filterViewWidget()
        if filterViewWidget is not None:
            filterViewWidget.viewModel().setItemMultiFilterIn(
                self.viewFilterItemIndexes(),
                self.itemFilterColumn(), self.itemFilterRow(),
                self.isChecked()
            )
    #
    def isCheckButton(self):
        return self._isCheckButton
    #
    def setCheckEnable(self, boolean):
        self._isCheckEnable = boolean
    #
    def isCheckEnable(self):
        return self._isCheckEnable
    #
    def setCheckable(self, boolean):
        self._isCheckable = boolean
        #
        self._updateQtCheckStyle()
    #
    def isCheckable(self):
        if self.isCheckEnable():
            return self._isCheckable
        else:
            return False
    #
    def setAutoExclusive(self, boolean):
        self._isAutoExclusive = boolean
        #
        self._updateQtCheckStyle()
    #
    def isAutoExclusive(self):
        if self.isCheckable():
            return self._isAutoExclusive
        else:
            return False
    #
    def setCheckHovered(self, boolean):
        self._isCheckHovered = boolean
        #
        self._updateQtCheckStyle()
    #
    def isCheckHovered(self):
        return self._isCheckHovered
    #
    def setChecked(self, boolean, ignoreAction=False):
        if not boolean == self._isChecked:
            self._isChecked = boolean
            if ignoreAction is False:
                # Check Action
                self._checkClickAction()
                # Toggle Action
                self._toggleClickAction()
                # Filter Action
                self._filterAction()
            #
            self._updateQtCheckStyle()
        #
        if boolean is True:
            if self.viewModel() is not None:
                itemIndex = self.viewModel().itemModelIndex(self)
                self.viewModel()._addCheckItemAt(itemIndex)
    #
    def isChecked(self):
        if self.isCheckable():
            return self._isChecked
        else:
            return False
    #
    def setExtendCheck(self, boolean, ignoreAction=False):
        if not boolean == self._isChecked:
            self._isChecked = boolean
            if ignoreAction is False:
                self._checkExtendClickAction()
            #
            self._updateQtCheckStyle()
    #
    def setCheckStarted(self, boolean):
        if not boolean == self._isCheckStarted:
            self._isCheckStarted = boolean
            #
            self._updateWidgetState()
    #
    def isCheckStarted(self):
        if self.isCheckable():
            return self._isCheckStarted
        else:
            return False
    #
    def setCheckFrameSize(self, w, h):
        self._uiCheckFrameWidth, self._uiCheckIconHeight = w, h
    #
    def checkFrameSize(self):
        return self._uiCheckFrameWidth, self._uiCheckIconHeight
    #
    def setCheckIconSize(self, w, h):
        self._uiCheckIconWidth, self._uiCheckIconHeight = w, h
    #
    def checkIconSize(self):
        return self._uiCheckIconWidth, self._uiCheckIconHeight
    #
    def checkRect(self):
        return self._uiCheckRect
    #
    def checkPressRect(self):
        return self._uiCheckPressRect
    #
    def isCheckRectContain(self, pos):
        if self.isCheckButton():
            return True
        else:
            if self.checkRect() is not None:
                return self.isRectContainPos(self.checkRect(), pos)
            else:
                return False
    #
    def setViewFilterEnable(self, boolean):
        if not boolean == self._isViewFilterEnable:
            self._isViewFilterEnable = boolean
    #
    def isViewFilterEnable(self):
        return self._isViewFilterEnable
    #
    def setViewFilterable(self, boolean):
        if not boolean == self._isViewFilterable:
            self._isViewFilterable = boolean
    #
    def isViewFilterable(self):
        if self.isViewFilterEnable():
            return self._isViewFilterable
        else:
            return False
    #
    def setFilterViewWidget(self, widget):
        self._filterViewWidget = widget
    #
    def filterViewWidget(self):
        return self._filterViewWidget
    #
    def setItemFilterColumn(self, number):
        self._itemFilterColumn = int(number)
    #
    def itemFilterColumn(self):
        return self._itemFilterColumn
    #
    def setItemFilterRow(self, number):
        self._itemFilterRow = int(number)
    #
    def itemFilterRow(self):
        return self._itemFilterRow
    #
    def setViewFilterItemIndexes(self, itemIndexes):
        self._viewFilterItemModelIndexLis = itemIndexes
        #
        self._updateViewFilterItemModelIndexCount()
    #
    def viewFilterItemIndexes(self):
        return self._viewFilterItemModelIndexLis
    #
    def viewFilterIndexCount(self):
        return self._viewFilterItemModelIndexCount
    #
    def viewModel(self):
        return self._viewModel


#
class QtDef_GraphitemWidget(QtDef_Widget):
    def _initDefGraphitemWidget(self):
        self._initDefWidget()
        #
        self._initDefGraphitemWidgetAttr()
        self._initDefGraphitemWidgetAction()
        self._initDefGraphitemWidgetRect()
        self._initDefGraphitemWidgetUi()
    #
    def _initDefGraphitemWidgetAttr(self):
        self._isDragEnable = False
        self._isDragable = True
    #
    def _initDefGraphitemWidgetAction(self):
        pass
    #
    def _initDefGraphitemWidgetRect(self):
        pass
    #
    def _initDefGraphitemWidgetUi(self):
        pass
    #
    def setDragEnable(self, boolean):
        self._isDragEnable = boolean
    #
    def isDragEnable(self):
        return self._isDragEnable
    #
    def setDragable(self, boolean):
        self._isDragable = boolean
    #
    def isDragable(self):
        if self.isDragEnable():
            return self._isDragable
        else:
            return False


#
class QtDef_GroupWidget(QtDef_Widget):
    def _initDefGroupWidget(self):
        self._initDefWidget()
        #
        self._initDefGroupWidgetAttr()
        self._initDefGroupWidgetRect()
        self._initDefGroupWidgetUi()
        self._initDefGroupWidgetVar()
    #
    def _initDefGroupWidgetAttr(self):
        self._isEventOverrideEnable = False
        self._isSeparated = False
    #
    def _initDefGroupWidgetRect(self):
        self._uiImageRect = QtCore.QRect(-20, -20, 1, 1)
    #
    def _initDefGroupWidgetUi(self):
        self._uiGroupWidth, self._uiGroupHeight = 20, 20
        #
        self._uiImage = None
        #
        self._uiImageWidget, self._uiImageHeight = 32, 32
        #
        self._uiButtonWidth, self._uiButtonHeight = 20, 20
        #
        self._uiGroupSpacing = 2
    #
    def _initDefGroupWidgetVar(self):
        self._childVisibleDic = {}
        self._childSizeDic = {}
    #
    def setButtonSize(self, w, h):
        self._uiButtonWidth, self._uiButtonHeight = w, h
    #
    def buttonSize(self):
        return self._uiButtonWidth, self._uiButtonHeight
    #
    def setImage(self, image):
        if bscMethods.OsFile.isExist(image):
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
    def setImageSize(self, w, h):
        self._uiImageWidget, self._uiImageHeight = w, h
    #
    def imageSize(self):
        return self._uiImageWidget, self._uiImageHeight
    #
    def setGroupSpacing(self, px):
        self._uiGroupSpacing = px
    #
    def groupSpacing(self):
        return self._uiGroupSpacing
    #
    def setSeparated(self, boolean):
        self._isSeparated = boolean
    #
    def isSeparated(self):
        return self._isSeparated


#
class QtDef_ViewWidget(QtDef_Widget):
    def _initDefViewWidget(self):
        self._initDefWidget()
        #
        self._initDefViewWidgetAttr()
        self._initDefViewWidgetAction()
        self._initDefViewWidgetRect()
        self._initDefViewWidgetUi()
        self._initDefViewWidgetVar()
    #
    def _initDefViewWidgetAttr(self):
        self._viewport, self._viewframe = [None] * 2
        #
        self._isHScrollEnable, self._isVScrollEnable = False, False
        self._isHScrollable, self._isVScrollable = False, False
        #
        self._isItemShowNamespace = False
        #
        self._isPlaceholderEnable = False
    #
    def _initDefViewWidgetAction(self):
        pass
    #
    def _initDefViewWidgetRect(self):
        self._uiScrollRect = QtCore.QRect(-20, -20, 1, 1)
        #
        self._uiPlaceholderRect = QtCore.QRect(-20, -20, 1, 1)
    #
    def _initDefViewWidgetUi(self):
        self._uiScale = 1.0
        #
        self._uiBasicGridWidth, self._uiBasicGridHeight = 20.0, 20.0
        self._uiGridWidth, self._uiGridHeight = 20.0, 20.0
        #
        self._uiBasicItemWidth, self._uiBasicItemHeight = 20.0, 20.0
        #
        self._uiItemWidth, self._uiItemHeight = 20.0, 20.0
        #
        self._uiButtonWidth, self._uiButtonHeight = 20, 20
        #
        self._uiHScrollWidth, self._uiHScrollHeight = 20, 20
        self._uiVScrollWidth, self._uiVScrollHeight = 20, 20
        #
        self._uiPlaceholderWidth, self._uiPlaceholderHeight = 240, 240
        self._uiPlaceholderImage = qtCore._toLxOsIconFile('svg_basic@svg#empty')
    #
    def _initDefViewWidgetVar(self):
        # Scroll
        self._hScrollValue, self._vScrollValue = 0, 0
        self._hScrollTempValue, self._vScrollTemValue = 0, 0
        #
        self._hScrollMaximum, self._hScrollMinimum = 0, 1
        self._vScrollMaximum, self._vScrollMinimum = 0, 1
        # Item Model
        self._itemModelLis = []
        self._visibleItemModelIndexLis = []
        # Item Pos
        self._itemModelPosDic = {}
        self._itemModelVisiblePosDic = {}
        # Item Size
        self._itemModelSizeDic = {}
        self._itemModelVisibleSizeDic = {}
        # Index
        self._itemIndexCount = 0
        self._minItemIndex, self._maxItemIndex = 0, 0
        #
        self._visibleIndexCount = 0
        self._minVisibleIndex, self._maxVisibleIndex = 0, 0
        #
        self._pressVisibleIndex = -1
        #
        self._hoverItemIndex = -1
        self._curHoverVisibleIndex = -1
        #
        self._curPressItemIndex = -1
        self._curPressVisibleIndex = -1
        # Column
        self._itemColumnCount = 1
        self._minItemColumn, self._maxItemColumn = 0, 1
        self._visibleColumnCount = 1
        self._minVisibleColumn, self._maxVisibleColumn = 0, 1
        self._curItemColumn = -1
        self._hoveredVisibleColumn = -1
        self._pressVisibleColumn = -1
        self._curVisibleColumn = -1
        # Row
        self._itemRowCount = 1
        self._minItemRow, self._maxItemRow = 0, 1
        self._visibleRowCount = 1
        self._minVisibleRow, self._maxVisibleRow = 0, 1
        self._curItemRow = -1
        self._hoveredVisibleRow = -1
        self._pressVisibleRow = -1
        self._curVisibleRow = -1
        #
        self._hoverItemModel = None
        self._curPressItemModel = None
        #
        self._itemHoverPos = 0, 0
        self._itemPressPos = 0, 0
        #
        self._absWidth, self._absHeight = 20, 20
        self._viewportWidth, self._viewportHeight = 0, 0
        self._viewWidth, self._viewHeight = 20, 20
        #
        self._trackWidth, self._trackHeight = 20, 20
    #
    def setPlaceholderEnable(self, boolean):
        self._isPlaceholderEnable = boolean
        self.update()
    #
    def isPlaceholderEnable(self):
        return self._isPlaceholderEnable
    #
    def placeholderImage(self):
        return self._uiPlaceholderImage
    #
    def placeholderSize(self):
        return self._uiPlaceholderWidth, self._uiPlaceholderHeight
    #
    def placeholderRect(self):
        return self._uiPlaceholderRect


#
class QtDef_TabbarWidget(QtDef_Widget):
    def _initDefTabbarWidget(self):
        self._initDefTabbarWidgetAttr()
        self._initDefTabbarWidgetRect()
        self._initDefTabbarWidgetUi()
        self._initDefTabbarWidgetVar()
    #
    def _initDefTabbarWidgetAttr(self):
        self._tabDir = qtCore.Vertical
        self._tabPos = qtCore.West
        #
        self._isItemAutoResizeEnable = False
        self._isItemAutoResizeable = False
    #
    def _initDefTabbarWidgetRect(self):
        self._uiTabBarPath = None
        #
        self._uiTabPathLis = []
    #
    def _initDefTabbarWidgetUi(self):
        self._uiItemWidth, self._uiItemHeight = 32, 64
    #
    def _initDefTabbarWidgetVar(self):
        self._itemIndexCount = 0
        self._minItemIndex, self._maxItemIndex = 0, 0
        #
        self._hoverItemIndex = -1
        #
        self._curPressItemIndex = 0
    #
    def setTabSize(self, w, h):
        self._uiItemWidth, self._uiItemHeight = w, h
    #
    def tabSize(self):
        return self._uiItemWidth, self._uiItemHeight
    #
    def setTabPosition(self, value):
        self._tabPos = value
    #
    def tabPosition(self):
        return self._tabPos
    #
    def setItemAutoResizeEnable(self, boolean):
        self._isItemAutoResizeEnable = boolean
    #
    def isItemAutoResizeEnable(self):
        return self._isItemAutoResizeEnable
    #
    def isItemAutoResizeable(self):
        if self.isItemAutoResizeEnable():
            return self._isItemAutoResizeable
        else:
            return False
    #
    def setItemAutoResizeable(self, boolean):
        self._isItemAutoResizeable = boolean


#
class QtDef_TabviewWidget(QtDef_Widget):
    def _initDefTabviewWidget(self):
        self._initDefWidget()
        #
        self._initDefTabviewWidgetAttr()
        self._initDefTabviewWidgetAction()
        self._initDefTabviewWidgetRect()
        self._initDefTabviewWidgetUi()
        self._initDefTabviewWidgetVar()
    #
    def _initDefTabviewWidgetAttr(self):
        self._tabBar = None
        #
        self._addButton = None
        #
        self._subScrollButton, self._addScrollButton = None, None
        self._scrollAddTimer, self._scrollSubTimer = None, None
        #
        self._itemClass = None
        #
        self._tabItemModelLis = []
        self._tabWidgetLis = []
        self._tabWidgetDic = {}
    #
    def _initDefTabviewWidgetAction(self):
        pass
    #
    def _initDefTabviewWidgetRect(self):
        self._uiScrollRect = QtCore.QRect(-20, -20, 1, 1)
    #
    def _initDefTabviewWidgetUi(self):
        self._uiTabBarWidth, self._uiTabBarHeight = 32, 32
        #
        self._uiButtonWidth, self._uiButtonHeight = 20, 20
    #
    def _initDefTabviewWidgetVar(self):
        pass
    #
    def scrollRect(self):
        return self._uiScrollRect
    #
    def buttonSize(self):
        return self._uiButtonWidth, self._uiButtonHeight
    #
    def tabBarSize(self):
        return self._uiTabBarWidth, self._uiTabBarHeight
    #
    def setItemClass(self, cls):
        self._itemClass = cls
    #
    def itemClass(self):
        return self._itemClass()
    #
    def setTabBar(self, widget):
        self._tabBar = widget._tabBar
    #
    def tabBar(self):
        return self._tabBar
    #
    def setTabPosition(self, value):
        if value in [qtCore.South, qtCore.North]:
            w, h = self.tabSize()
            self.setTabSize(w, h)
        else:
            w, h = self.tabSize()
            self.setTabSize(h, w)
        self.tabBar().viewModel().setTabPosition(value)
    #
    def tabPosition(self):
        return self.tabBar().viewModel().tabPosition()
    #
    def tabSize(self):
        return self.tabBar().viewModel().itemSize()
    #
    def setTabSize(self, w, h):
        if self.tabPosition() == qtCore.South or self.tabPosition() == qtCore.North:
            self._uiTabBarWidth, self._uiTabBarHeight = w, h
            self.tabBar().viewModel().setItemSize(w, h)
        else:
            self._uiTabBarWidth, self._uiTabBarHeight = h, w
            self.tabBar().viewModel().setItemSize(h, w)
    #
    def tabWidgets(self):
        return self._tabWidgetLis
    #
    def tabModelAt(self, tabIndex):
        return self._tabItemModelLis[tabIndex]
    #
    def tabAt(self, tabIndex):
        return self.tabModelAt(tabIndex).widget()
    #
    def tabIndex(self, widget):
        return self.tabWidgets().index(widget)
    #
    def addTab(self, widget, name=None, iconKeyword=None, tooltip=None):
        widget.setParent(self.viewport())
        self._tabWidgetLis.append(widget)
        self._tabWidgetDic[name] = widget
        #
        tabBarViewModel = self.tabBar().viewModel()
        #
        tab = self.itemClass()
        tabItemModel = tab.itemModel()
        self._tabItemModelLis.append(tabItemModel)
        #
        tabItemModel.setTabBar(self.tabBar())
        #
        if name is not None:
            tabItemModel.setNameText(name)
        if iconKeyword is not None:
            tabItemModel.setIcon(iconKeyword)
        if tooltip is not None:
            tab.setTooltip(tooltip)
        #
        if self.tabPosition() == qtCore.South or self.tabPosition() == qtCore.North:
            tabItemModel._menuButton.setIcon('svg_basic@svg#tabMenu_h')
        else:
            tabItemModel._menuButton.setIcon('svg_basic@svg#tabMenu_v')
        #
        tabBarViewModel.addItem(tab)
        #
        widget.setVisible(tabItemModel.isPressCurrent())
        tab.currentToggled.connect(widget.setVisible)
        #
        tabBarViewModel.setItemPressAt(0, ignoreFlag=True)


#
class QtDef_WindowWidget(QtDef_Widget):
    def _initDefWindowWidget(self):
        self._initDefWidget()
        #
        self._initDefWindowWidgetAttr()
        self._initDefWindowWidgetAction()
        self._initDefWindowWidgetRect()
        self._initDefWindowWidgetUi()
        self._initDefWindowWidgetVar()
    #
    def _initDefWindowWidgetAttr(self):
        self._widget = None
        self._viewport = None
        self._progressBar = None
        #
        self._direction = qtCore.Horizontal
        #
        self._menuWidget = None
        self._centralWidget = None
        self._statusWidget = None
        #
        self._isMenuEnable = True
        self._isStatusEnable = True
        #
        self._isDragEnable = True
        self._isDragable = True
        #
        self._isResizeEnable = True
        self._isResizeable = True
        #
        self._isMaximizeEnable = True
        self._isMaximizeable = True
        self._isMaximized = False
        #
        self._isMinimizeEnable = True
        self._isMinimizeable = True
        self._isMinimized = False
        #
        self._isDialogEnable = True
        self._isShadowEnable = True
        #
        self._isPercentEnable = False
        #
        self._isSubWindow = False
        #
        self._progressTimer = qtCore.CLS_timer(self._widget)
        #
        self._countdownStep = 0
        #
        self._countdownCloseTimer = qtCore.CLS_timer(self._widget)
        # noinspection PyUnresolvedReferences
        self._countdownCloseTimer.timeout.connect(self._countdownCloseStartAction)
        #
        self._isWindowActive = False
        #
        self._isPlaceholderEnable = False
        #
        self._quitConnectMethodLis = []
        #
        self._isMessageWindow = False
    #
    def _initDefWindowWidgetAction(self):
        self._progressThread = qtCore.QThread_()
    #
    def _initDefWindowWidgetRect(self):
        self._uiMenuRect, self._uiCentralRect, self._uiStatusRect = (
            QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1), QtCore.QRect(-20, -20, 1, 1)
        )
        #
        self._uiPercentValueRect = QtCore.QRect(-20, -20, 1, 1)
        self._uiPercentTextRect = QtCore.QRect(-20, -20, 1, 1)
        #
        self._uiStatusTextRect = QtCore.QRect(-20, -20, 1, 1)
        #
        self._uiResizeRect = QtCore.QRect(-20, -20, 1, 1)
        #
        self._uiPlaceholderRect = QtCore.QRect(-20, -20, 1, 1)
        #
        self._uiFocusPath = None
    #
    def _initDefWindowWidgetUi(self):
        self._uiStatusText = None
        #
        self._uiStatusTextWidth = 480
        #
        self._uiItemWidth, self._uiItemHeight = 20, 20
        #
        self._uiDefaultWidth, self._uiDefaultHeight = 1280, 720
        #
        self._uiWidthRound, self._uiHeightRound = 2, 2
        #
        self._uiBasicWidth, self._uiBasicHeight = 800, 600
        #
        self._uiXPos, self._uiYPos = 0, 0
        self._uiWidth, self._uiHeight = 20, 20
        #
        self._uiMenuWidth, self._uiMenuHeight = 320, 32
        self._uiStatusWidth, self._uiStatusHeight = 320, 32
        #
        self._uiButtonWidth, self._uiButtonHeight = 20, 20
        #
        self._uiResizeIconKeyword = 'svg_basic@svg#resize'
        self._uiResizeIcon = self._toLxOsIconFile(self._uiResizeIconKeyword)
        #
        self._uiPlaceholderWidth, self._uiPlaceholderHeight = 240, 240
        self._uiPlaceholderImage = qtCore._toLxOsIconFile('svg_basic@svg#empty')
    #
    def _initDefWindowWidgetVar(self):
        self._dragStartPoint = QtCore.QPoint()
        #
        self._uiMaxProgressValue = 1
        self._uiProgressValue = 0
    # for Override
    def _progressValueChangeAction(self):
        pass
    #
    def addWidget(self, widget):
        self.viewportLayout().addWidget(widget)
    #
    def isWindowActive(self):
        return self._isWindowActive
    #
    def setDefaultSize(self, width, height):
        self._uiDefaultWidth, self._uiDefaultHeight = width, height
    #
    def defaultSize(self):
        return self._uiDefaultWidth, self._uiDefaultHeight
    #
    def setDirection(self, direction):
        self._direction = direction
    #
    def direction(self):
        return self._direction
    #
    def isMenuRectContainPos(self, pos):
        if self.menuRect() is not None:
            return self.isRectContainPos(self.menuRect(), pos)
        else:
            return False
    #
    def setMenuEnable(self, boolean):
        self._isMenuEnable = boolean
    #
    def isMenuEnable(self):
        return self._isMenuEnable
    #
    def setStatusEnable(self, boolean):
        self._isStatusEnable = boolean
    #
    def isStatusEnable(self):
        return self._isStatusEnable
    #
    def setDialogEnable(self, boolean):
        self._isDialogEnable = boolean
    #
    def isDialogEnable(self):
        if self.isStatusEnable():
            return self._isDialogEnable
        else:
            return False

    def setShadowEnable(self, boolean):
        self._isShadowEnable = boolean

    def isShadowEnable(self):
        return self._isShadowEnable
    #
    def setDragEnable(self, boolean):
        self._isDragEnable = boolean
    #
    def isDragEnable(self):
        return self._isDragEnable
    #
    def setDragable(self, boolean):
        self._isDragable = boolean
    #
    def isDragable(self):
        if self.isDragEnable():
            return self._isDragable
        else:
            return False
    #
    def setResizeEnable(self, boolean):
        self._isResizeEnable = boolean
    #
    def isResizeEnable(self):
        return self._isResizeEnable
    #
    def setResizeable(self, boolean):
        self._isResizeable = boolean
    #
    def isResizeable(self):
        if self.isResizeEnable():
            return self._isResizeable
        else:
            return False
    #
    def setMaximizeEnable(self, boolean):
        self._isMaximizeEnable = boolean
    #
    def isMaximizeEnable(self):
        return self._isMaximizeEnable
    #
    def setMaximizeable(self, boolean):
        self._isMaximizeable = boolean
    #
    def isMaximizeable(self):
        if self.isMaximizeEnable():
            return self._isMaximizeable
        else:
            return False
    #
    def setMaximized(self, boolean):
        if not boolean == self._isMaximized:
            self._isMaximized = boolean
    #
    def isMaximized(self):
        if self.isMaximizeable():
            return self._isMaximized
        else:
            return False
    #
    def setMinimizeEnable(self, boolean):
        self._isMinimizeEnable = boolean
    #
    def isMinimizeEnable(self):
        return self._isMinimizeEnable
    #
    def setMinimizeable(self, boolean):
        self._isMinimizeable = boolean
    #
    def isMinimizeable(self):
        if self.isMinimizeEnable():
            return self._isMinimizeable
        else:
            return False
    #
    def setMinimized(self, boolean):
        if not boolean == self._isMinimized:
            self._isMinimized = boolean
    #
    def isMinimized(self):
        if self.isMinimizeable():
            return self._isMinimized
        else:
            return False
    #
    def setPlaceholderEnable(self, boolean):
        self._isPlaceholderEnable = boolean
        self.update()
    #
    def isPlaceholderEnable(self):
        return self._isPlaceholderEnable
    #
    def placeholderImage(self):
        return self._uiPlaceholderImage
    #
    def placeholderSize(self):
        return self._uiPlaceholderWidth, self._uiPlaceholderHeight
    #
    def placeholderRect(self):
        return self._uiPlaceholderRect
    #
    def setPercentEnable(self, boolean):
        self._isPercentEnable = boolean
    #
    def isPercentEnable(self):
        return self._isPercentEnable
    #
    def menuRect(self):
        return self._uiMenuRect
    #
    def statusRect(self):
        return self._uiStatusRect
    #
    def setStatusText(self, string):
        self._uiStatusText = string
        #
        self._updateWidgetState()
    #
    def statusText(self):
        return self._uiStatusText
    #
    def resizeRect(self):
        return self._uiResizeRect
    #
    def statusTextRect(self):
        return self._uiStatusTextRect
    #
    def isMessageWindow(self):
        return self._isMessageWindow


#
class QtDef_ScrollbarWidget(QtDef_Widget):
    def _initDefScrollbarWidget(self):
        self._initDefWidget()
        #
        self._initDefScrollbarWidgetAttr()
        self._initDefScrollbarWidgetAction()
        self._initDefScrollbarWidgetRect()
        self._initDefScrollbarWidgetUi()
        self._initDefScrollbarWidgetVar()
    #
    def _initDefScrollbarWidgetAttr(self):
        self._addScrollButton = None
        self._subScrollButton = None
        #
        self._menuButton = None
        self._tooltipWidget = None
        #
        self._isPressMenuEnable = False
        self._isTooltipEnable = False
        #
        self._unionFlag = False
        #
        self._dir = qtCore.Vertical
        #
        self._widget = None
        #
        self._isSliderHover = False
        self._isSliderPress = False
        self._isClick = False
        #
        self._basicValue = 5
        self._rowValue = 5
        self._pageValue = 5
        #
        self._addScrollTimer = qtCore.CLS_timer(self._widget)
        self._subScrollTimer = qtCore.CLS_timer(self._widget)
    #
    def _initDefScrollbarWidgetAction(self):
        self._pressFlag, self._dragFlag, self._clickFlag = False, False, False
        #
        self._addScrollFlag, self._subScrollFlag = False, False
        #
        self._autoScrollFlag = False
        #
        self._altFlag, self._shiftFlag, self._ctrlFlag = False, False, False
    #
    def _initDefScrollbarWidgetRect(self):
        self._uiBasicRect, self._uiSliderRect, self._clickRect = QtCore.QRect(), QtCore.QRect(), QtCore.QRect()
    #
    def _initDefScrollbarWidgetUi(self):
        self._uiScrollBarWidth = 20
    #
    def _initDefScrollbarWidgetVar(self):
        self._absHeight = 0
        #
        self._itemColumnCount = 1
        self._itemRowCount = 0
        #
        self._isScrollable = False
        #
        self._sliderHeight = 0
        #
        self._minSliderHeight, self._maxSliderHeight = 10, 10
        #
        self._sliderPos = 0
        self._sliderPercent = 0.0
        #
        self._dragPercent = 0.0
        #
        self._curVisibleRow = 0
        self._minItemRow = 0
        self._maxItemRow = 0
        #
        self._tempValue = 0
        #
        self._value = 0
        self._maximum = 1
        self._minimum = 0
        #
        self._percent = 0.0
        self._maxPercent = 1.0
        self._minPercent = 0.0
        #
        self._timerInterval = 50
        #
        self._yPressStartPos = 0
        self._clickPos = 0
        self._pressHoverPos = 0, 0
        #
        self._pos = 0, 0
    #
    def _updateValueByRow(self):
        pass
    #
    def _updatePercent(self):
        pass
    #
    def _updateTempValue(self):
        pass
    #
    def _initScrollBarConnect(self):
        pass
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
    def getClampValue(self, value):
        return max(min(int(value), self._maximum), self._minimum)
    #
    def setValue(self, value, isRow=False):
        self._value = self.getClampValue(value)
        #
        if self._shiftFlag is True or isRow is True:
            self._updateValueByRow()
        #
        self._updatePercent()
        #
        self.update()
        #
        self.widget().update()
        #
        self.widget().valueChanged.emit()
    #
    def setRow(self, row):
        if self._isScrollable:
            value = row*self._rowValue
            self.setValue(value)
    #
    def setPage(self, page):
        if self._isScrollable:
            value = page*self._pageValue
            self.setValue(value)
    #
    def setAbsHeight(self, value):
        self._absHeight = int(value)
    #
    def setDirection(self, value):
        self._dir = value
        #
        if self._dir == qtCore.Vertical:
            self._subScrollButton.setIcon(
                'svg_basic@svg#vScrollSub',
                16, 16, self._uiScrollBarWidth, self._uiScrollBarWidth
            )
            self._addScrollButton.setIcon(
                'svg_basic@svg#vScrollAdd',
                16, 16, self._uiScrollBarWidth, self._uiScrollBarWidth
            )
        else:
            self._subScrollButton.setIcon(
                'svg_basic@svg#hScrollSub',
                16, 16, self._uiScrollBarWidth, self._uiScrollBarWidth
            )
            self._addScrollButton.setIcon(
                'svg_basic@svg#hScrollAdd',
                16, 16, self._uiScrollBarWidth, self._uiScrollBarWidth
            )
    #
    def direction(self):
        return self._dir
    #
    def setPressMenuEnable(self, boolean):
        self._isPressMenuEnable = boolean
    #
    def scrollToMaximum(self):
        self.setValue(self._maximum)
        #
        self._updateTempValue()
    #
    def scrollToMinimum(self):
        self.setValue(self._minimum)
        #
        self._updateTempValue()
    #
    def value(self):
        return self._value
    #
    def scrollBarWidth(self):
        return self._uiScrollBarWidth
    #
    def setBasicScrollValue(self, value):
        self._basicValue = int(value)
    #
    def setRowScrollValue(self, value):
        self._rowValue = int(value)
        #
        self._isTooltipEnable = True
    #
    def setTimerInterval(self, value):
        self._timerInterval = int(value)
    #
    def setItemColumnCount(self, value):
        self._itemColumnCount = int(value)
    #
    def itemColumnCount(self):
        return self._itemColumnCount
    #
    def setMaximum(self, value):
        self._maximum = int(value)
    #
    def setMinimum(self, value):
        self._minimum = int(value)
    #
    def setScrollable(self, boolean):
        if not boolean == self._isScrollable:
            self._isScrollable = boolean
            #
            if boolean is False:
                self.setValue(0)
    #
    def isScrollable(self):
        return self._isScrollable
    #
    def isMaximum(self):
        if self._isScrollable:
            return self._value == self._maximum
        else:
            return True
    #
    def isMinimum(self):
        if self._isScrollable:
            return self._value == self._minimum
        else:
            return True
    #
    def maximum(self):
        return self._maximum
    #
    def minimum(self):
        return self._minimum
    #
    def tooltipWidget(self):
        return self._tooltipWidget
    #
    def sliderRect(self):
        return self._uiSliderRect
    #
    def isTooltipEnable(self):
        return self._isTooltipEnable


#
class QtDef_ScrollareaWidget(QtDef_Widget):
    def _initDefScrollarea(self):
        self._initDefWidget()
        #
        self._initDefScrollareaAttr()
        self._initDefScrollareaAction()
        self._initDefScrollareaUi()
        self._initDefScrollareaVar()
    #
    def _initDefScrollareaAttr(self):
        self._viewport, self._viewframe, self._layout = None, None, None
        #
        self._hScrollBar, self._vScrollBar = None, None
        #
        self._uiItemWidth, self._uiItemHeight = 20, 20
        #
        self._uiHScrollWidth, self._uiVScrollWidth = 20, 20
        #
        self._trackWidth, self._trackHeight = 20, 20
        #
        self._absWidth, self._absHeight = 20, 20
        #
        self._isHScrollable, self._isVScrollable = False, False
    #
    def _initDefScrollareaAction(self):
        self._hAutoScrollFlag, self._vAutoScrollFlag = False, False
        self._hAutoScrollRegion, self._vAutoScrollRegion = -1, -1
    #
    def _initDefScrollareaUi(self):
        self._uiHScrollWidth, self._uiHScrollHeight = 20, 20
        self._uiVScrollWidth, self._uiVScrollHeight = 20, 20
    #
    def _initDefScrollareaVar(self):
        self._xValue, self._yValue = 0, 0
    # for Override
    def _scrollValueChangeAction(self):
        self._updateViewportGeometry()
    #
    def _hScrollWidth(self):
        pass
    #
    def _hScrollHeight(self):
        return [0, self._uiHScrollHeight][self.isHScrollable()]
    #
    def _vScrollWidth(self):
        return [0, self._uiVScrollWidth][self.isVScrollable()]
    #
    def vScrollHeight(self):
        pass
    #
    def setScrollBar(self, widget):
        if hasattr(widget, '_hScrollBar'):
            self._hScrollBar = widget._hScrollBar
            self._uiHScrollWidth = self.hScrollBar().viewModel().scrollBarWidth()
            #
            self.hScrollBar().viewModel().setDirection(qtCore.Horizontal)
            self.hScrollBar().setFocusProxy(self._widget)
            #
            self.hScrollBar().valueChanged.connect(self._scrollValueChangeAction)
            self.hScrollBar().stop.connect(self._updateAction)
        if hasattr(widget, '_vScrollBar'):
            self._vScrollBar = widget._vScrollBar
            self._uiVScrollWidth = self.vScrollBar().viewModel().scrollBarWidth()
            #
            self.vScrollBar().viewModel().setDirection(qtCore.Vertical)
            self.vScrollBar().setFocusProxy(self._widget)
            #
            self.vScrollBar().valueChanged.connect(self._scrollValueChangeAction)
            self.vScrollBar().stop.connect(self._updateAction)
    #
    def setHScrollEnable(self, boolean):
        self._isHScrollEnable = boolean
    #
    def isHScrollEnable(self):
        return self._isHScrollEnable
    #
    def setVScrollEnable(self, boolean):
        self._isVScrollEnable = boolean
    #
    def isVScrollEnable(self):
        return self._isVScrollEnable
    #
    def setHScrollable(self, boolean):
        self._isHScrollable = boolean
    #
    def isHScrollable(self):
        if self.isHScrollEnable():
            return self._isHScrollable
        else:
            return False
    #
    def setVScrollable(self, boolean):
        self._isVScrollable = boolean
    #
    def isVScrollable(self):
        if self.isVScrollEnable():
            return self._isVScrollable
        else:
            return False
    #
    def hScrollBar(self):
        return self._hScrollBar
    #
    def vScrollBar(self):
        return self._vScrollBar
    #
    def scrollBar(self):
        return self.hScrollBar(), self.vScrollBar()
    #
    def hValue(self):
        if self.isHScrollable():
            value = self.hScrollBar().viewModel().value()
        else:
            value = 0
        return value
    #
    def vValue(self):
        if self.isVScrollable():
            value = self.vScrollBar().viewModel().value()
        else:
            value = 0
        return value
    #
    def setValue(self, x, y):
        self.hScrollBar().viewModel().setValue(x), self.vScrollBar().viewModel().setValue(y)
    #
    def value(self):
        return self.hValue(), self.vValue()
    #
    def isHMaximum(self):
        if self.isHScrollable():
            return self.hScrollBar().viewModel().isMaximum()
        else:
            return True
    #
    def isHMinimum(self):
        if self.isHScrollable():
            return self.hScrollBar().viewModel().isMinimum()
        else:
            return True
    #
    def isMaximum(self):
        return self.isHMaximum(), self.isVMaximum()
    #
    def isVMaximum(self):
        if self.isVScrollable():
            return self.vScrollBar().viewModel().isMaximum()
        else:
            return True
    #
    def isVMinimum(self):
        if self.isVScrollable():
            return self.vScrollBar().viewModel().isMinimum()
        else:
            return True
    #
    def isMinimum(self):
        return self.isHMinimum(), self.isVMinimum()


#
class QtDef_SplitterWidget(QtDef_Widget):
    def _initDefSplitter(self):
        self._initDefWidget()
        #
        self._initDefSplitterAttr()
        self._initDefSplitterAction()
        self._initDefSplitterRect()
        self._initDefSplitterUi()
        self._initDefSplitterVar()
    #
    def _initDefSplitterAttr(self):
        pass
    #
    def _initDefSplitterAction(self):
        pass
    #
    def _initDefSplitterRect(self):
        pass
    #
    def _initDefSplitterUi(self):
        pass
    #
    def _initDefSplitterVar(self):
        pass


#
class QtDef_Layout(object):
    def _initDefLayout(self):
        self._initDefLayoutAttr()
        self._initDefLayoutVar()
    #
    def _initDefLayoutAttr(self):
        self._minSize = 0
    #
    def _initDefLayoutVar(self):
        self._itemLis = []
        self._visibleItemLis = []
        #
        self._itemSizePolicyLis = []
        self._itemMiniSizeLis = []
    #
    def setSizePolicyAt(self, index, sizePolicy):
        self._itemSizePolicyLis[index] = sizePolicy
    #
    def sizePolicyAt(self, index):
        return self._itemSizePolicyLis[index]
    #
    def minimumSize(self):
        return self._minSize
    #
    def addItem(self, widget):
        self._itemLis.append(widget)
        self._itemSizePolicyLis.append(
            (widget.sizePolicy().horizontalPolicy(), widget.sizePolicy().verticalPolicy())
        )
        self._itemMiniSizeLis.append(
            widget.minimumSize()
        )


#
class QtDef_ItemModel(
    QtDef_PressWidget,
    QtDef_CheckWidget,
    QtDef_ExpandWidget,
    QtDef_ColorWidget,
    QtDef_GraphitemWidget,
):
    def _initItemModelDef(self):
        self._initDefPressWidget()
        self._initDefCheckWidget()
        self._initDefExpandWidget()
        self._initDefColorWidget()
        self._initDefGraphitemWidget()
        #
        self._initItemModelDefAttr()
        self._initItemModelDefAction()
        self._initItemModelDefRect()
        self._initItemModelDefUi()
        self._initItemModelDefVar()
    #
    def _initItemModelDefAttr(self):
        self._isSelectEnable = False
        self._isSelectable = True
        self._isSelected = False
        self._isSubSelected = False
        self._isSelectExclusive = False
        #
        self._namespace = None
        self._namespaceSep = ':'
        #
        self._isShowNamespace = False
        #
        self._isFilterEnable = True
        self._isKeywordFilterable = True
        #
        self._isEventOverrideEnable = False
    #
    def _initItemModelDefAction(self):
        pass
    #
    def _initItemModelDefRect(self):
        self._uiDatumRect = QtCore.QRect(-20, -20, 1, 1)
        self._uiNamespaceRect = QtCore.QRect(-20, -20, 1, 1)
    #
    def _initItemModelDefUi(self):
        self._uiNamespaceText = None
        #
        self._uiWidthRecord, self._uiHeightRecord = 0, 0
        #
        self._uiItemWidth, self._uiItemHeight = 20, 20
        #
        self._uiPressStatus = qtCore.NormalStatus
    #
    def _initItemModelDefVar(self):
        pass
    # Need Override
    def _updateWidgetGeometry(self):
        pass
    # Need Override
    def _updateRectGeometry(self):
        pass
    # Need Override
    def _hoverAction(self):
        pass
    # Need Override
    def _pressClickAction(self):
        pass
    #
    def _updateQtPressStyle(self):
        if self.isPressEnable():
            if self.isPressable():
                if self.isPressCurrent():
                    self._setQtPressStyle(qtCore.CurrentState)
                else:
                    self._setQtPressStyle(qtCore.NormalState)
            else:
                self._setQtPressStyle(qtCore.UnpressableState)
        #
        self._updateWidgetState()
    #
    def _setQtPressStyle(self, state):
        if state is qtCore.UnpressableState:
            self.widget()._uiBackgroundRgba = 0, 0, 0, 0
            self.widget()._uiBorderRgba = 0, 0, 0, 0
            #
            self.widget()._uiNameRgba = 95, 95, 95, 255
            #
            self.widget()._uiFontItalic = True
        else:
            if self.isSelectEnable():
                if state is qtCore.SelectedState:
                    self.widget()._uiBackgroundRgba = [(63, 127, 255, 127), (63, 127, 255, 191)][self.isPressHovered()]
                    self.widget()._uiBorderRgba = 0, 0, 0, 0
                elif state is qtCore.UnselectedState:
                    self.widget()._uiBackgroundRgba = [(0, 0, 0, 0), (127, 127, 127, 64)][self.isPressHovered()]
                    self.widget()._uiBorderRgba = 0, 0, 0, 0
                elif state is qtCore.SubSelectedState:
                    self.widget()._uiBackgroundRgba = [(64, 127, 255, 32), (64, 127, 255, 64)][self.isPressHovered()]
                    self.widget()._uiBorderRgba = 0, 0, 0, 0
            else:
                if state is qtCore.CurrentState:
                    self.widget()._uiBackgroundRgba = [(63, 127, 255, 127), (63, 127, 255, 191)][self.isPressHovered()]
                    self.widget()._uiBorderRgba = 0, 0, 0, 0
                elif state is qtCore.NormalState:
                    self.widget()._uiBackgroundRgba = [(0, 0, 0, 0), (127, 127, 127, 64)][self.isPressHovered()]
                    self.widget()._uiBorderRgba = 0, 0, 0, 0
            #
            self.widget()._uiFontItalic = False
            #
            self._updateQtPressStatus()
    #
    def _hoverStartAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            pass
    #
    def _hoverExecuteAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            pass
    #
    def _hoverStopAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            pass
    #
    def _pressStartAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            pass
    #
    def _pressExecuteAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            pass
    #
    def _pressStopAction(self, event):
        if self._isEventOverrideEnable is True:
            event.ignore()
        else:
            pass
    #
    def setSelectEnable(self, boolean):
        self._isSelectEnable = boolean
    #
    def isSelectEnable(self):
        return self._isSelectEnable
    #
    def setSelectable(self, boolean):
        self._isSelectable = boolean
        #
        self._updateQtPressStyle()
    #
    def isSelectable(self):
        if self.isSelectEnable():
            return self._isSelectable
        else:
            return False
    #
    def setSelected(self, boolean):
        if not boolean == self._isSelected:
            self._isSelected = boolean
            #
            self._updateQtPressStyle()
    #
    def isSelected(self):
        if self.isSelectable():
            return self._isSelected
        else:
            return False
    #
    def update(self):
        pass
    #
    def setNamespace(self, string):
        self._namespace = string
        self.setNamespaceText(self._namespace)
    #
    def namespace(self):
        return self._namespace
    #
    def setNamespaceText(self, string):
        if string is not None:
            self._uiNamespaceText = unicode(string)
        #
        self._updateWidgetState()
    #
    def namespaceText(self):
        if self._isShowNamespace:
            if self._uiNamespaceText != self._namespaceSep:
                return self._uiNamespaceText
        else:
            if self._uiNamespaceText is not None and self._uiNamespaceText != self._namespaceSep:
                return '...' + self._namespaceSep
    #
    def setFilterEnable(self, boolean):
        self._isFilterEnable = boolean
    #
    def isFilterEnable(self):
        return self._isFilterEnable
    #
    def setItemSize(self, w, h):
        self._uiItemWidth, self._uiItemHeight = max(int(w), 1), max(int(h), 1)
    #
    def itemSize(self):
        return self._uiItemWidth, self._uiItemHeight
    #
    def setPressHovered(self, boolean, ignoreAction=False):
        if not boolean == self._isPressHovered:
            self._isPressHovered = boolean
            #
            if ignoreAction is False:
                self._hoverAction()
        #
        self._updateQtPressStyle()
    #
    def setPressCurrent(self, boolean, ignoreAction=False):
        if not boolean == self._isPressCurrent:
            self._isPressCurrent = boolean
            #
            if ignoreAction is False:
                self._pressClickAction()
            #
            self._updateQtPressStyle()
    #
    def isPressCurrent(self):
        if self.isPressable():
            return self._isPressCurrent
        else:
            return False
    #
    def setViewModel(self, model):
        self._viewModel = model
        self._graphModelWidget = model.widget()
        #
        self.widget().setParent(model.viewport())
    #
    def viewModel(self):
        return self._viewModel
    #
    def setEventOverrideEnable(self, boolean):
        self._isEventOverrideEnable = boolean
    #
    def isEventOverrideEnable(self):
        return self._isEventOverrideEnable


#
class QtDef_GroupModel(
    QtDef_GroupWidget,
    QtDef_PressWidget,
    QtDef_ExpandWidget,
    QtDef_ColorWidget
):
    def _initGroupModelDef(self):
        self._initDefGroupWidget()
        #
        self._initDefPressWidget()
        self._initDefExpandWidget()
        self._initDefColorWidget()
        #
        self._initGroupModelDefVar()
    #
    def _initGroupModelDefVar(self):
        self._xMenuPos, self._yMenuPos = 0, 0
    #
    def _clearHover(self):
        self.setExpandHovered(False)
    #
    def _updateHoverLoc(self, x, y):
        _x, _y = self._pressHoverPos
        #
        self._pressHoverPos = x, y
        #
        if self.isExpandPressRectContain((x, y)):
            self.setExpandHovered(True)
        else:
            self.setExpandHovered(False)
    #
    def _updatePressLoc(self, x, y):
        if self.isExpandPressRectContain((x, y)):
            if self._pressFlag is True:
                self._expandClickSwitchAction()
    #
    def _updateByChildChanged(self):
        if self._isChildChanged() is True:
            self._updateWidgetSize()
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
        x, y = self._getEventPos(event)
        self._pressClickPos = x, y
        #
        self._pressFlag, self._dragFlag = True, False
        #
        self._updateByChildChanged()
        #
        event.ignore()
    #
    def _pressExecuteAction(self, event):
        self._pressFlag, self._dragFlag = False, True
        event.ignore()
    #
    def _pressStopAction(self, event):
        self._updatePressLoc(*self.pressClickPos())
        #
        self._updateByChildChanged()
        #
        self._pressFlag, self._dragFlag = False, False
        #
        event.ignore()
    #
    def _setWidgetSizePolicy(self, args):
        self.widget().setSizePolicy(*args)
    # for Override
    def _updateWidgetSize(self):
        pass
    #
    def _isChildChanged(self):
        if self.isSeparated() is False:
            if self.isExpanded():
                layout = self.viewport().layout()
                count = layout.count()
                if count:
                    for index in range(0, count):
                        item = layout.itemAt(index)
                        if item:
                            widget = item.widget()
                            curVisible = widget.isVisible()
                            preVisible = self._childVisibleDic.get(index, True)
                            self._childVisibleDic[index] = curVisible
                            if not curVisible == preVisible:
                                return True
    #
    def _updateWidgetSizePolicy(self):
        if self.isSeparated() is False:
            if self.isExpanded():
                self._setWidgetSizePolicy(self.expandedSizePolicy())
            else:
                self._setWidgetSizePolicy(self.unexpandedSizePolicy())
        else:
            self._setWidgetSizePolicy(self.unexpandedSizePolicy())
    #
    def addWidget(self, widget):
        verticalSizePolicy = widget.sizePolicy().verticalPolicy()
        if verticalSizePolicy == qtCore.QSizePolicy.Expanding:
            self.setExpandedSizePolicy(qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding)
            #
            self._updateWidgetSizePolicy()
        #
        self.viewportLayout().addWidget(widget)


#
class QtDef_ViewModel(
    QtDef_ViewWidget,
    QtDef_ScrollareaWidget,
    QtDef_PressWidget
):
    def _initDefViewModel(self):
        self._initDefViewWidget()
        self._initDefScrollarea()
        #
        self._initDefPressWidget()
    #
    def _getEventPos(self, event):
        point = event.pos()
        x, y = point.x(), point.y()
        return x - self._uiMargins[0], y - self._uiMargins[1]
    @staticmethod
    def _toColumnCount(width, w):
        if w > 0:
            return max(int(width/w), 1)
        else:
            return 1
    @staticmethod
    def _toRowCount(height, h):
        if h > 0:
            return max(int(height/h), 1)
        else:
            return 1
    @staticmethod
    def _getRowCount(indexCount, columnCount):
        return int((indexCount + columnCount - 1)/columnCount)
    @staticmethod
    def _indexAt(column, row, columnCount):
        return column + row*columnCount
    @staticmethod
    def _columnLoc(x, w):
        return int(x/w)
    @staticmethod
    def _columnAt(index, columnCount):
        return int(index) % columnCount
    @staticmethod
    def _rowLoc(y, h):
        return int(y/h)
    @staticmethod
    def _rowAt(index, columnCount):
        return int(index)/columnCount
    @staticmethod
    def _mapToItemPos(x, y, w, h, xValue, yValue, column, row):
        return x + xValue - column*w, y + yValue - row*h
    #
    def _getClampItemIndex(self, itemIndex):
        return max(min(int(itemIndex), self._maxItemIndex), self._minItemIndex)
    #
    def _addItemModel(self, itemModel):
        if not itemModel in self.itemModels():
            self.itemModels().append(itemModel)
            #
            self._updateItemModelIndexCount()
    #
    def _updateItemModelIndexCount(self):
        self._itemIndexCount = len(self.itemModels())
        #
        self._updateMaxItemIndex()
    # Index
    def _updateMaxItemIndex(self):
        self._maxItemIndex = self._itemIndexCount + self._minItemIndex - 1
    #
    def _updateCurItemIndex(self):
        itemIndex = self.itemIndexAt(self._curItemColumn, self._curItemRow)
        if self.isContainItemIndex(itemIndex):
            self._curPressItemIndex = itemIndex
    # Column
    def setItemColumnCount(self, value):
        self._itemColumnCount = int(value)
        self._updateMaxItemColumn()
    #
    def itemColumnCount(self):
        return self._itemColumnCount
    #
    def setMinItemColumn(self, value):
        self._minItemColumn = int(value)
        self._updateMaxItemColumn()
    #
    def _updateCurItemColumn(self):
        self._curItemColumn = self._getClampItemColumn(self.itemColumnAt(self._curPressItemIndex))
    #
    def _updateMaxItemColumn(self):
        self._maxItemColumn = self._minItemColumn + self._itemColumnCount - 1
    #
    def _updateItemColumnCount(self):
        value = self._toColumnCount(self.viewportWidth(), self._uiItemWidth)
        self.setItemColumnCount(value)
    #
    def _updateItemRowCount(self):
        value = self._getRowCount(self._itemIndexCount, self._itemColumnCount)
        self.setItemRowCount(value)
    #
    def _updateViewportSize(self):
        self._viewportWidth, self._viewportHeight = (
            self.width() - self._uiMargins[0] - self._uiMargins[2],
            self.height() - self._uiMargins[1] - self._uiMargins[3]
        )
    #
    def _updateMaxItemRow(self):
        self._maxItemRow = self._minItemRow + self._itemRowCount - 1
    #
    def _updateCurItemRow(self):
        self._curItemRow = self._getClampItemRow(self.itemRowAt(self._curPressItemIndex))
    #
    def _gridSize(self):
        return self._uiItemWidth, self._uiItemHeight
    #
    def _itemSize(self):
        return self._uiItemWidth, self._uiItemHeight
    #
    def _updateAbsSize(self):
        w, h = self._gridSize()
        self._absWidth, self._absHeight = self._itemColumnCount*w, self._itemRowCount*h
    # View
    def _updateViewSize(self):
        self._viewWidth = [self._absWidth, self._viewportWidth - self._vScrollWidth()][self.isHScrollable()]
        self._viewHeight = [self._absHeight, self._viewportHeight - self._hScrollHeight()][self.isVScrollable()]
    #
    def getClampScrollValue(self, x, y):
        return self.getClampHScrollValue(x), self.getClampVScrollValue(y)
    #
    def getClampHScrollValue(self, value):
        return max(min(int(value), self._hScrollMaximum), self._hScrollMinimum)
    #
    def getClampVScrollValue(self, value):
        return max(min(int(value), self._vScrollMaximum), self._vScrollMinimum)
    #
    def _updateScrollState(self):
        self.setHScrollable(self._absWidth > self.width()), self.setVScrollable(self._absHeight > self.height())
    #
    def _hScrollHeight(self):
        return [0, self._uiHScrollHeight][self.isHScrollable()]
    #
    def _vScrollWidth(self):
        return [0, self._uiVScrollWidth][self.isVScrollable()]
    # Position
    def _itemModelPosAt(self, itemIndex):
        xPos, yPos = 0, 0
        w, h = self._gridSize()
        #
        column, row = self.itemColumnAt(itemIndex), self.itemRowAt(itemIndex)
        #
        x, y = xPos + column*w, yPos + row*h
        return x, y
    #
    def _updateItemModelPosAt(self, itemIndex):
        if itemIndex is not None:
            x, y = self._itemModelPosAt(itemIndex)
            self._itemModelPosDic[itemIndex] = x, y
    #
    def _updateItemModelsPos(self):
        self._itemModelVisiblePosDic = {}
        if self.itemIndexCount() > 0:
            for itemIndex in self.itemIndexes():
                self._updateItemModelPosAt(itemIndex)
    #
    def _updateItemsGeometry(self):
        if self.itemIndexCount() > 0:
            xValue, yValue = self.scrollValue()
            for itemIndex in self.itemIndexes():
                itemModel = self.itemModelAt(itemIndex)
                #
                widget = itemModel.widget()
                #
                x, y = self.itemPosAt(itemIndex)
                #
                w, h = self._itemSize()
                #
                widget.setGeometry(
                    x - xValue, y - yValue,
                    w, h
                )
    #
    def _getClampItemColumn(self, column):
        return max(min(int(column), self._maxVisibleColumn), self._minVisibleColumn)
    #
    def _getClampItemRow(self, row):
        return max(min(int(row), self._maxItemRow), self._minItemRow)
    #
    def _updateHoverLoc(self, x, y):
        self._pressHoverPos = x, y
        #
        xValue, yValue = self.scrollValue()
        #
        itemIndex = self.itemIndexLoc(x + xValue, y + yValue)
        #
        self.setItemHoverAt(itemIndex)
        #
        self.update()
    #
    def _updatePressLoc(self, x, y):
        self._itemPressPos = x, y
        #
        xValue, yValue = self.scrollValue()
        #
        itemIndex = self.itemIndexLoc(x + xValue, y + yValue)
        #
        self.setItemPressAt(itemIndex)
        #
        self.update()
    #
    def _updateDragPressLoc(self, x, y):
        pass
    #
    def _updateScrollBy(self, xDelta, yDelta):
        self._updateHScrollBy(xDelta), self._updateVScrollBy(yDelta)
    #
    def _updateHScrollBy(self, delta):
        if delta != 0:
            step = self._uiItemWidth
            #
            value = self.mtd_raw_value.stepTo(
                value=self._hScrollValue,
                delta=-delta,
                step=step,
                valueRange=(self._hScrollMinimum, self._hScrollMaximum)
            )
            #
            self.setHScrollValue(value)
    #
    def _updateVScrollBy(self, delta):
        if delta != 0:
            step = self._uiItemHeight
            #
            value = self.mtd_raw_value.stepTo(
                value=self._vScrollValue,
                delta=-delta,
                step=step,
                valueRange=(self._vScrollMinimum, self._vScrollMaximum)
            )
            #
            self.setVScrollValue(value)
    #
    def _hoverStartAction(self, event):
        event.ignore()
    #
    def _hoverExecuteAction(self, event):
        x, y = self._getEventPos(event)
        #
        if self.isContainPos(x, y):
            self._updateHoverLoc(x, y)
        else:
            self._clearHover()
        #
        event.ignore()
    #
    def _hoverStopAction(self, event):
        self._clearHover()
        #
        event.ignore()
    #
    def _pressStartAction(self, event):
        self._pressFlag, self._dragFlag, self._trackFlag = True, False, False
        #
        self._curPressChangeFlag = False
        #
        x, y = self._getEventPos(event)
        #
        if self.isContainPos(x, y):
            self._updatePressLoc(x, y)
            #
            event.ignore()
        else:
            event.ignore()
    #
    def _pressExecuteAction(self, event):
        # Flag
        self._pressFlag, self._dragFlag, self._trackFlag = False, True, False
        #
        x, y = self._getEventPos(event)
        #
        if self.isContainPos(x, y):
            self._updateDragPressLoc(x, y)
            #
            event.ignore()
        else:
            event.ignore()
    #
    def _pressStopAction(self, event):
        # Flag
        self._pressFlag, self._dragFlag, self._trackFlag = False, False, False
        #
        x, y = self._getEventPos(event)
        #
        if self.isContainPos(x, y):
            self._updatePressLoc(x, y)
            #
            if self._curPressChangeFlag is True:
                self.widget().currentChanged.emit()
            #
            event.ignore()
        else:
            event.ignore()
    #
    def _wheelAction(self, event):
        xDelta, yDelta = event.angleDelta().x(), event.angleDelta().y()
        #
        self._updateScrollBy(xDelta, yDelta)
    #
    def _hScrollSubAction(self):
        if self.isHScrollable():
            self._updateHScrollBy(+1)
    #
    def _hScrollAddAction(self):
        if self.isHScrollable():
            self._updateHScrollBy(-1)
    #
    def _vScrollSubAction(self):
        if self.isVScrollable():
            self._updateVScrollBy(+1)
    #
    def _vScrollAddAction(self):
        if self.isVScrollable():
            self._updateVScrollBy(-1)
    #
    def _updateItemHoverAt(self, itemIndex):
        itemModel = self.itemModelAt(itemIndex)
        #
        preItemModel = self._hoverItemModel
        if not itemModel == preItemModel:
            isChanged = True
        else:
            isChanged = False
        #
        if isChanged is True:
            if itemModel.isPressable():
                itemModel.setPressHovered(True)
            #
            if preItemModel is not None:
                preItemModel.setPressHovered(False)
            #
            self._hoverItemIndex = itemIndex
            self._hoverItemModel = itemModel
        #
        self._curHoverChangeFlag = isChanged
    #
    def _updateItemPressAt(self, itemIndex):
        itemModel = self.itemModelAt(itemIndex)
        #
        isChanged = False
        preItemModel = self._curPressItemModel
        #
        if itemModel.isPressable():
            if not itemModel == preItemModel:
                isChanged = True
        #
        if isChanged is True:
            # Clear First
            if preItemModel is not None:
                preItemModel.setPressCurrent(False)
            #
            itemModel.setPressCurrent(True)
            #
            self._curPressItemModel = itemModel
            self._curPressItemIndex = itemIndex
        #
        self._curPressChangeFlag = isChanged
    #
    def itemIndexLoc(self, x, y):
        column, row = self.itemColumnLoc(x), self.itemRowLoc(y)
        return self.itemIndexAt(column, row)
    #
    def setItemRowCount(self, value):
        self._itemRowCount = value
        self._updateMaxItemRow()
    #
    def setMinItemRow(self, row):
        self._minItemRow = int(row)
        self._updateMaxItemRow()
    #
    def isContainPos(self, x, y):
        return 0 < x < self._viewWidth and 0 < y < self._viewHeight
    #
    def setItemHoverAt(self, itemIndex):
        if self.isContainItemIndex(itemIndex):
            self._updateItemHoverAt(itemIndex)
        else:
            self._clearHover()
    #
    def setItemPressAt(self, itemIndex, ignoreFlag=False):
        if self._pressFlag is True or ignoreFlag is True:
            if self.isContainItemIndex(itemIndex):
                self._updateItemPressAt(itemIndex)
    #
    def update(self):
        pass
    #
    def itemColumnAt(self, itemIndex):
        return self._columnAt(itemIndex, self._itemColumnCount)
    #
    def itemRowAt(self, itemIndex):
        return self._rowAt(itemIndex, self._itemColumnCount)
    #
    def itemPosAt(self, itemIndex):
        return self._itemModelPosDic.get(itemIndex, (0, 0))
    #
    def absSize(self):
        return self._absWidth, self._absHeight
    #
    def viewSize(self):
        return self._viewWidth, self._viewHeight
    #
    def setSpacing(self, value):
        self._uiSpacing = value
    #
    def spacing(self):
        return self._uiSpacing
    #
    def maxItemIndex(self):
        return self._maxItemIndex
    #
    def minItemIndex(self):
        return self._minItemIndex
    #
    def isContainItemIndex(self, itemIndex):
        if self._itemIndexCount:
            return self._minItemIndex <= itemIndex <= self._maxItemIndex
        else:
            return False
    #
    def itemModelAt(self, itemIndex):
        if self.isContainItemIndex(itemIndex):
            return self.itemModels()[itemIndex]
    #
    def itemModelIndex(self, itemModel):
        if itemModel in self.itemModels():
            return self.itemModels().index(itemModel)
    #
    def itemIndexCount(self):
        return self._itemIndexCount
    #
    def visibleIndexCount(self):
        return self._visibleIndexCount
    #
    def itemIndexes(self):
        return range(self._minItemIndex, self._maxItemIndex + 1)
    #
    def visibleItemIndexes(self):
        return self._visibleItemModelIndexLis
    #
    def setCurrentIndex(self, itemIndex):
        self._updateItemPressAt(itemIndex)
    #
    def currentItemIndex(self):
        return self._curPressItemIndex
    #
    def hoverItemIndex(self):
        return self._hoverItemIndex
    #
    def currentItemModel(self):
        return self._curPressItemModel
    #
    def hoverItemModel(self):
        return self._hoverItemModel
    #
    def visibleIndexes(self):
        return range(self._minVisibleIndex, self._maxVisibleIndex + 1)
    #
    def itemModels(self):
        return self._itemModelLis
    #
    def visibleItemModels(self):
        return [self.itemModelAt(i) for i in self.visibleItemIndexes()]
    #
    def items(self):
        return [i.widget() for i in self.itemModels()]
    #
    def visibleItems(self):
        return [i.widget() for i in self.visibleItemModels()]
    #
    def setItemSize(self, w, h):
        self._uiItemWidth, self._uiItemHeight = max(int(w), 1), max(int(h), 1)
    #
    def setScrollValue(self, x, y):
        xValue, yValue = self.getClampScrollValue(x, y)
        #
        self._hScrollValue, self._vScrollValue = xValue, yValue
        #
        self.update()
    #
    def setHScrollValue(self, value):
        self._hScrollValue = self.getClampHScrollValue(value)
        #
        self.update()
    #
    def setVScrollValue(self, value):
        self._vScrollValue = self.getClampVScrollValue(value)
        #
        self.update()
    #
    def scrollValue(self):
        return self._hScrollValue, self._vScrollValue
    #
    def _updateTempValue(self):
        self._hScrollTempValue, self._vScrollTemValue = self._hScrollValue, self._vScrollValue
    #
    def scrollRect(self):
        return self._uiScrollRect
    #
    def itemSize(self):
        return self._uiItemWidth, self._uiItemHeight
    #
    def itemColumnLoc(self, x):
        w, h = self._gridSize()
        return self._columnLoc(x, w)
    #
    def itemRowLoc(self, y):
        w, h = self._gridSize()
        return self._rowLoc(y, h)
    #
    def itemIndexAt(self, itemColumn, itemRow):
        return self._getClampItemColumn(itemColumn) + self._getClampItemRow(itemRow)*self._itemColumnCount
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
        #
        itemModel.setEventOverrideEnable(True)
        # Item Model
        self._addItemModel(itemModel)


#
class QtDef_WindowModel(
    QtDef_WindowWidget,
    QtDef_PressWidget,
    QtDef_ExpandWidget,
):
    def _initDefWindowModel(self):
        self._initDefWindowWidget()
        self._initDefPressWidget()
        self._initDefExpandWidget()


#
class QtDef_SplitterModel(
    QtDef_SplitterWidget
):
    def _initDefSplitterModel(self):
        self._initDefSplitter()
