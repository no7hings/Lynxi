# coding:utf-8
import chardet
#
from LxCore import lxBasic, lxConfigure
#
from LxUi import uiCore
#
from LxUi.qt.uiBasic import uiModelBasic
#
QtGui = uiCore.QtGui
QtCore = uiCore.QtCore
#
_families = lxConfigure.Lynxi_Ui_Family_Lis
#
none = ''


# noinspection PyProtectedMember
def uiChooseViewDropMethod(method):
    def subFn(*args):
        # Class
        self = args[0]
        chooseNameLis = self.itemModel()._uiDatumTextLis
        if chooseNameLis:
            widget = _UiChooseDropView(self)
            widget.setFocusProxy(self)
            widget.installEventFilter(self)
            widget.setFocus(QtCore.Qt.PopupFocusReason)
            #
            widget.viewModel().setCurrentIndex(self.itemModel().chooseIndex())
            widget.viewModel().addItems(chooseNameLis, self.itemModel()._uiIconKeyword)
            widget.setDrop()
        #
        return method(*args)
    return subFn


#
def uiChooseBoxEventFilterMethod(method):
    def subFn(*args):
        self = args[0]
        widget = args[1]
        event = args[2]
        # Filter by Widget is Press
        if type(widget) == _UiChooseDropView:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                widget.close()
                #
                self.chooseChanged.emit()
            # Filter by Widget is Activate
            elif event.type() == QtCore.QEvent.WindowDeactivate:
                widget.close()
        #
        return method(*args)
    return subFn


#
def uiActionViewDropMethod(method):
    def subFn(*args):
        # Class
        self = args[0]
        if hasattr(self, 'actionData'):
            actionData = self.actionData
            if actionData:
                widget = _UiActionDropView(self)
                widget.setFocusProxy(self)
                widget.installEventFilter(self)
                widget.setFocus(QtCore.Qt.PopupFocusReason)
                # Set Title
                if hasattr(self, 'actionTitle'):
                    menuTitle = self.actionTitle
                    if menuTitle:
                        widget.setTitle(menuTitle)
                # Set Action First
                widget.setActionData(actionData)
                #
                widget.setDrop()
        #
        return method(*args)
    return subFn


#
def uiActionEventFilterMethod(method):
    def subFn(*args):
        widget = args[1]
        event = args[2]
        # Filter by Widget is Press
        if type(widget) == _UiActionDropView:
            if event.type() == QtCore.QEvent.WindowDeactivate:
                widget.close()
        #
        return method(*args)
    return subFn


# Basic Item
class _UiItemBasic(uiCore.QWidget):
    toggled = uiCore.uiSignal(bool)
    clicked = uiCore.uiSignal()
    doubleClicked = uiCore.uiSignal()
    #
    expanded = uiCore.uiSignal()
    checked = uiCore.uiSignal()
    #
    pressed = uiCore.uiSignal()
    released = uiCore.uiSignal()
    #
    visibleToggled = uiCore.uiSignal(bool)
    def _initItemBasic(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        #
        self._initItemNBasicAttr()
        self._initItemBasicUi()
    #
    def _initItemNBasicAttr(self):
        self.actionTitle = None
        self.actionData = []
    #
    def _initItemBasicUi(self):
        self._uiFont = uiCore.xFont()
        self.setFont(self._uiFont)
        #
        self._uiFontItalic = False
        self._uiFontStrikeOut = False
        #
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 0, 0, 0, 0
        #
        self._uiPercentValueRgba = 47, 47, 47, 255
        #
        self._uiIndexRgba = 127, 127, 127, 255
        self._uiNameRgba = 191, 191, 191, 255
        self._uiSubNameColor = 191, 191, 191, 255
        #
        self._uiNamespaceRgba = 95, 95, 95, 255
        #
        self._uiDatumRgba = 191, 191, 191, 255
        #
        self._uiColorBackgroundRgba = 71, 71, 71, 255
        self._uiColorBorderRgba = 127, 127, 127, 255
        #
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 127, 127, 127, 255
        #
        self._uiMenuBackgroundRgba = 0, 0, 0, 0
        self._uiMenuBorderRgba = 0, 0, 0, 0
        #
        self._uiCentralBackgroundRgba = 71, 71, 71, 255
        self._uiCentralBorderRgba = 95, 95, 95, 255
        #
        self._uiBorderStyle = 'outset'
    @uiCore.uiTooltipStartMethod
    def enterEvent(self, event):
        self.itemModel()._hoverStartAction(event)
    @uiCore.uiTooltipStopMethod
    def leaveEvent(self, event):
        self.itemModel()._hoverStopAction(event)
    @uiCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStartAction(event)
        else:
            event.ignore()
    @uiCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStartAction(event)
        else:
            event.ignore()
    @uiCore.uiTooltipClearMethod
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStopAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.itemModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.itemModel()._pressExecuteAction(event)
            else:
                event.ignore()
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        # Background
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRect(self.itemModel()._uiBasicRect)
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter.setDrawImage(
                self.itemModel()._uiCheckRect, self.itemModel()._uiCheckIcon
            )
        # Filter Color
        if self.itemModel()._isColorEnable is True:
            painter.setBackgroundRgba(self._uiColorBackgroundRgba)
            painter.setBorderRgba(self._uiColorBorderRgba)
            painter.drawRect(self.itemModel()._uiColorRect)
        # Expand
        if self.itemModel().isExpandable() is True:
            painter.setDrawImage(
                self.itemModel()._uiExpandRect,
                self.itemModel()._uiExpandIcon
            )
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(), self.itemModel().icon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            rect = self.itemModel()._uiNameTextRect
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            if self.itemModel()._filterKeyword is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    self.itemModel()._uiNameText, self.itemModel()._filterKeyword,
                    self._uiNameRgba
                )
            else:
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(rect, textOption, self.itemModel()._uiNameText)
        # Index
        if self.itemModel()._uiIndexText is not None:
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(
                self.itemModel()._uiIndexTextRect,
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter,
                str(self.itemModel()._uiIndexText)
            )
    #
    def setIndex(self, number):
        self.itemModel().setIndex(number)
    #
    def index(self):
        return self.itemModel().index()
    #
    def setIndexText(self, number):
        self.itemModel().setIndexText(number)
    #
    def indexText(self):
        return self.itemModel().indexText()
    #
    def setType(self, string):
        self.itemModel().setType(string)
    #
    def type(self):
        return self.itemModel().type()
    #
    def setName(self, string):
        self.itemModel().setName(string)
    #
    def name(self):
        return self.itemModel().name()
    #
    def setNamespace(self, string):
        self.itemModel().setNamespace(string)
    #
    def namespace(self):
        return self.itemModel().namespace()
    #
    def setIconKeyword(self, iconKeyword):
        self.itemModel().setIconKeyword(iconKeyword)
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
    #
    def setIconText(self, text):
        self.itemModel().setIconText(text)
    #
    def iconText(self):
        return self.itemModel().iconText()
    #
    def setSubIcon(self, iconKeyword):
        self.itemModel().setSubIcon(iconKeyword)
    #
    def setNameText(self, string):
        self.itemModel().setNameText(string)
    #
    def nameText(self):
        return self.itemModel().nameText()
    #
    def setNamespaceText(self, string):
        self.itemModel().setNamespaceText(string)
    #
    def namespaceText(self):
        return self.itemModel().namespaceText()
    #
    def setNameTextWidth(self, value):
        self.itemModel().setNameTextWidth(value)
    #
    def setFilterColor(self, color):
        self.itemModel().setFilterColor(color)
    #
    def filterColor(self):
        return self.itemModel().filterColor()
    #
    def setPressEnable(self, boolean):
        self.itemModel().setPressEnable(boolean)
    #
    def setPressable(self, boolean):
        self.itemModel().setPressable(boolean)
    #
    def isPressable(self):
        return self.itemModel().isPressable()
    #
    def setPressHovered(self, boolean):
        self.itemModel().setPressHovered(boolean)
    #
    def setPressCurrent(self, boolean):
        self.itemModel().setPressCurrent(boolean)
    #
    def setExpandEnable(self, boolean):
        self.itemModel().setExpandEnable(boolean)
    #
    def setExpanded(self, boolean):
        self.itemModel().setExpanded(boolean)
    #
    def setCheckEnable(self, boolean):
        self.itemModel().setCheckEnable(boolean)
    #
    def isCheckEnable(self):
        return self.itemModel().isCheckEnable()
    #
    def setCheckable(self, boolean):
        self.itemModel().setCheckable(boolean)
    #
    def isCheckable(self):
        return self.itemModel().isCheckable()
    #
    def setChecked(self, boolean, ignoreAction=False):
        self.itemModel().setChecked(boolean, ignoreAction)
    #
    def isChecked(self):
        return self.itemModel().isChecked()
    #
    def setPercentEnable(self, boolean):
        self.itemModel().setPercentEnable(boolean)
    #
    def setAutoExclusive(self, boolean):
        self.itemModel().setAutoExclusive(boolean)
    #
    def isAutoExclusive(self):
        return self.itemModel().isAutoExclusive()
    #
    def addChild(self, widget):
        self.itemModel().addChild(widget)
    #
    def hasChildren(self):
        return self.itemModel().hasChildren()
    #
    def childItems(self):
        return self.itemModel().childItems()
    #
    def childItemNames(self):
        return self.itemModel().childItemNames()
    #
    def parentItem(self):
        return self.itemModel().parentItem()
    #
    def parentItems(self):
        return self.itemModel().parentItems()
    #
    def setPressAction(self, action):
        self.itemModel().setPressAction(action)
    #
    def acceptPressAction(self):
        self.itemModel().acceptPressAction()
    #
    def setPressCommand(self, command):
        self.itemModel().setPressCommand(command)
    #
    def acceptPressCommand(self):
        self.itemModel().acceptPressCommand()
    #
    def setExtendPressCommand(self, command):
        self.itemModel().setExtendPressCommand(command)
    #
    def _setUiPressStyle(self, state):
        self.itemModel()._setUiPressStyle(state)
    #
    def _setUiPressStatus(self, status):
        self.itemModel()._setUiPressStatus(status)
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._itemModel = uiModelBasic._UiItemModel(self)


# Basic View
class _UiViewBasic(uiCore.QWidget):
    clicked = uiCore.uiSignal()
    itemClicked = uiCore.uiSignal()
    currentChanged = uiCore.uiSignal()
    selectedChanged = uiCore.uiSignal()
    #
    itemExpanded = uiCore.uiSignal()
    itemChecked = uiCore.uiSignal()
    def _initViewBasic(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding,
            uiCore.QSizePolicy.Expanding
        )
        #
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        #
        self._initViewBasicAttr()
        self._initViewBasicUi()
    #
    def _initViewBasicAttr(self):
        self.actionTitle = None
        self.actionData = []
        self._uiPreActions = []
        #
        self._vTempScrollPercent = 0
    #
    def _initViewBasicUi(self):
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 63, 127, 255, 255
        #
        self._uiWidthRound, self._uiHeightRound = 5, 5
    #
    def enterEvent(self, event):
        self.viewModel()._hoverStartAction(event)
    #
    def leaveEvent(self, event):
        self.viewModel()._hoverStopAction(event)
    #
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(True)
        elif event.key() == QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(True)
        elif event.key() == QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(True)
        # Focus
        elif event.key() == QtCore.Qt.Key_F:
            self.viewModel().setCurrentVisibleCeiling()
        # Column Move
        elif event.key() == QtCore.Qt.Key_Left:
            self.viewModel()._columnTraceAction(-1)
        elif event.key() == QtCore.Qt.Key_Right:
            self.viewModel()._columnTraceAction(+1)
        # Row Move
        elif event.key() == QtCore.Qt.Key_Up:
            self.viewModel()._rowTraceAction(-1)
        elif event.key() == QtCore.Qt.Key_Down:
            self.viewModel()._rowTraceAction(+1)
    #
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(False)
        elif event.key() == QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(False)
        elif event.key() == QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(False)
        else:
            event.ignore()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        elif event.button() == QtCore.Qt.MidButton:
            self.setCursor(QtCore.Qt.OpenHandCursor)
            #
            self.viewModel()._trackStartAction(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStopAction(event)
        elif event.button() == QtCore.Qt.MidButton:
            self.setCursor(QtCore.Qt.ArrowCursor)
            #
            self.viewModel()._trackStopAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.viewModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.viewModel()._pressExecuteAction(event)
            elif event.buttons() == QtCore.Qt.MidButton:
                self.setCursor(QtCore.Qt.ClosedHandCursor)
                #
                self.viewModel()._trackExecuteAction(event)
            else:
                event.ignore()
    #
    def wheelEvent(self, event):
        self.viewModel()._wheelAction(event)
    #
    def resizeEvent(self, event):
        if self.viewModel()._isSizeChanged():
            self.viewModel().update()
    #
    def showEvent(self, event):
        self.viewModel().update()
    #
    def setMargins(self, *args):
        self.viewModel().setMargins(*args)
    #
    def setSpacing(self, value):
        self.viewModel().setSpacing(value)
    #
    def setItemColumnCount(self, value):
        self.viewModel().setItemColumnCount(value)
        self.viewModel().setVisibleColumnCount(value)
    #
    def addItem(self, widget):
        self.viewModel().addItem(widget)
    #
    def removeItem(self, widget):
        self.viewModel().removeItem(widget)
    #
    def setCurrentIndex(self, itemIndex):
        self.viewModel().setCurrentIndex(itemIndex)
    #
    def setSelectEnable(self, boolean):
        self.viewModel().setSelectEnable(boolean)
    #
    def setExpandEnable(self, boolean):
        self.viewModel().setExpandEnable(boolean)
    #
    def setCheckEnable(self, boolean):
        self.viewModel().setCheckEnable(boolean)
    #
    def setColorEnable(self, boolean):
        self.viewModel().setColorEnable(boolean)
    #
    def setFocusFrameEnable(self, boolean):
        self.viewModel().setFocusFrameEnable(boolean)
    #
    def setFilterConnect(self, widget):
        self.viewModel().setFilterConnect(widget)
    #
    def setExtendExpanded(self, boolean):
        self.viewModel().setExtendExpanded(boolean)
    #
    def items(self):
        return self.viewModel().items()
    #
    def itemCount(self):
        return self.viewModel().itemIndexCount()
    #
    def cleanItems(self):
        self._vTempScrollPercent = self._vScrollBar.viewModel().valuePercent()
        self.viewModel().cleanItems()
    #
    def visibleItems(self):
        return self.viewModel().visibleItems()
    #
    def currentItem(self):
        return self.viewModel().currentItem()
    #
    def setRefresh(self):
        self.viewModel().update()
        #
        self.viewModel().setFilterExplainRefresh()
        #
        self._vScrollBar.viewModel().setValueByPercent(self._vTempScrollPercent)
        #
        if self.itemModels():
            self.viewModel().setPlaceholderEnable(False)
        else:
            self.viewModel().setPlaceholderEnable(True)
    #
    def setCheckAll(self):
        self.viewModel().setCheckAll()
    #
    def setUncheckAll(self):
        self.viewModel().setUncheckAll()
    #
    def checkedItems(self):
        return self.viewModel().checkedItems()
    #
    def selectedItemModels(self):
        return self.viewModel().selectedItemModels()
    #
    def selectedItems(self):
        return self.viewModel().selectedItems()
    #
    def itemModels(self):
        return self.viewModel().itemModels()
    #
    def itemIndex(self, widget):
        return self.viewModel().itemIndex(widget)
    #
    def itemAt(self, index):
        return self.viewModel().itemAt(index)
    #
    def viewModel(self):
        return self._viewModel
    #
    def setupUi(self):
        self._viewModel = uiModelBasic._UiViewModel(self)


# Window Basic
class _UiWindowBasic(uiCore.QMainWindow):
    closed = uiCore.uiSignal()
    confirmClicked = uiCore.uiSignal()
    def _initWindowBasic(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setMouseTracking(True)
        #
        self._initWindowBasicAttr()
        self._initWindowBasicUi()
    #
    def _initWindowBasicAttr(self):
        pass
    #
    def _initWindowBasicUi(self):
        self._uiIndexRgba = 95, 95, 95, 255
        self._uiNameRgba = 223, 223, 223, 255
        self._uiSubNameColor = 223, 223, 223, 255
        #
        self._uiBackgroundRgba = 63, 63, 63, 255
        self._uiBorderRgba = 95, 95, 95, 255
        #
        self._uiMenuBackgroundRgba = 63, 63, 63, 255
        self._uiMenuBorderRgba = 95, 95, 95, 255
        #
        self._uiProgressStartBackgroundRgba = 63, 127, 255, 255
        self._uiProgressEndBackgroundRgba = 255, 255, 255, 255
        self._uiProgressBorderRgba = 0, 0, 0, 0
        #
        self._uiCentralBackgroundRgba = 63, 63, 63, 255
        self._uiCentralBorderRgba = 95, 95, 95, 255
        #
        self._uiStatusBackgroundRgba = 63, 63, 63, 255
        self._uiStatusBorderRgba = 95, 95, 95, 255
        #
        self.setFont(uiCore.xFont(
            size=12, weight=75, family=_families[1])
        )
        # noinspection PyArgumentEqualDefault
        self._uiIndexFont = uiCore.xFont(
            size=8, weight=50, family=_families[0]
        )
        #
        self._uiNameTextFont = uiCore.xFont(
            size=12, weight=75, family=_families[1]
        )
        # noinspection PyArgumentEqualDefault
        self._uiHelpFont = uiCore.xFont(
            size=8, weight=50, family=_families[0]
        )
    #
    def enterEvent(self, event):
        self.windowModel()._hoverStartAction(event)
    #
    def leaveEvent(self, event):
        self.windowModel()._hoverStopAction(event)
    #
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.windowModel()._setCtrlFlag(True)
        elif event.key() == QtCore.Qt.Key_Shift:
            self.windowModel()._setShiftFlag(True)
        elif event.key() == QtCore.Qt.Key_Alt:
            self.windowModel()._setAltFlag(True)
    #
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.windowModel()._setCtrlFlag(False)
        elif event.key() == QtCore.Qt.Key_Shift:
            self.windowModel()._setShiftFlag(False)
        elif event.key() == QtCore.Qt.Key_Alt:
            self.windowModel()._setAltFlag(False)
        else:
            event.ignore()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.windowModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.windowModel()._pressStartAction(event, isDoubleClick=True)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.windowModel()._pressStopAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.windowModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.windowModel()._pressExecuteAction(event)
            else:
                event.ignore()
    #
    def nativeEvent(self, event, message):
        return self.windowModel()._resizeAction(event, message)
    #
    def resizeEvent(self, event):
        if self.windowModel()._isSizeChanged():
            self.windowModel().update()
    #
    def showEvent(self, event):
        self.windowModel()._updateWidgetSize()
        #
        self.windowModel().update()
    #
    def showMinimized(self):
        uiCore.QMainWindow.showMinimized(self)
    #
    def showMaximized(self):
        uiCore.QMainWindow.showMaximized(self)
    #
    def showNormal(self):
        uiCore.QMainWindow.showNormal(self)
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        #
        if not self.isMaximized():
            painter.setDrawShadow(
                self.windowModel()._uiBasicRect,
                self.windowModel()._uiShadowRadius, self.windowModel()._uiShadowRadius
            )
        if self.windowModel().isWindowActive() is True:
            frameBorderRgba = 63, 127, 255, 255
        elif self.windowModel().isExpanded() is False:
            frameBorderRgba = 255, 0, 63, 255
        else:
            frameBorderRgba = self._uiBorderRgba
        # Background
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(frameBorderRgba)
        painter.drawRect(self.windowModel()._uiBasicRect)
        #
        if self.windowModel().isExpanded():
            painter.setBackgroundRgba(frameBorderRgba)
            #
            painter.setBorderRgba(frameBorderRgba)
            painter.drawPath(self.windowModel()._uiFocusPath)
        #
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        # Placeholder
        if self.windowModel().isPlaceholderEnable():
            painter.setDrawImage(
                self.windowModel().placeholderRect(),
                self.windowModel().placeholderImage()
            )
        # Status
        if self.windowModel().isStatusEnable() and self.windowModel().isExpanded():
            painter.setBackgroundRgba(self._uiStatusBackgroundRgba)
            painter.setBorderRgba(self._uiStatusBorderRgba)
            rect = self.windowModel().statusRect()
            painter.drawLine(rect.topLeft(), rect.topRight())
            #
            if self.windowModel().statusText():
                textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                painter.setFont(self._uiHelpFont)
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(self.windowModel().statusTextRect(), textOption, self.windowModel().statusText())
        #
        if self.windowModel().isPercentEnable():
            if self.windowModel().direction() is uiCore.Horizontal:
                gradient = QtGui.QLinearGradient(self.windowModel()._uiPercentValueRect.topLeft(), self.windowModel()._uiPercentValueRect.topRight())
            else:
                gradient = QtGui.QLinearGradient(self.windowModel()._uiPercentValueRect.topRight(), self.windowModel()._uiPercentValueRect.bottomRight())
            #
            rect = self.windowModel()._uiPercentValueRect
            w = rect.width()
            gradient.setColorAt(0, QtGui.QColor(*self._uiProgressStartBackgroundRgba))
            gradient.setColorAt(lxBasic.mapRangeValue((0, w), (0, 1.0), max(16, w - 16)), QtGui.QColor(*self._uiProgressStartBackgroundRgba))
            gradient.setColorAt(1, QtGui.QColor(*self._uiProgressEndBackgroundRgba))
            brush = QtGui.QBrush(gradient)
            painter.setBrush(brush)
            painter.setBorderRgba(self._uiProgressBorderRgba)
            painter.drawRect(rect)
        #
        if self.windowModel().isResizeable():
            painter.setDrawImage(
                self.windowModel()._uiResizeRect,
                self.windowModel()._uiResizeIcon
            )
        # Menu
        if self.windowModel().isMenuEnable():
            if self.windowModel().isExpanded():
                painter.setBackgroundRgba(self._uiMenuBackgroundRgba)
                painter.setBorderRgba(self._uiMenuBorderRgba)
                rect = self.windowModel().menuRect()
                if self.windowModel().direction() is uiCore.Horizontal:
                    p0, p1 = rect.bottomLeft(), rect.bottomRight()
                    painter.drawLine(rect.bottomLeft(), rect.bottomRight())
                else:
                    p0, p1 = rect.topLeft(), rect.bottomLeft()
                #
                painter.drawLine(p0, p1)
            #
            if self.windowModel().direction() is uiCore.Horizontal:
                pass
            else:
                painter.translate(self.windowModel()._xTranslate, self.windowModel()._yTranslate)
                painter.rotate(-90)
            # Icon
            if self.windowModel().icon() is not None:
                painter.setDrawImage(
                    self.windowModel().iconRect(),
                    self.windowModel().icon()
                )
            # Name
            if self.windowModel().nameText() is not None:
                rect = self.windowModel().nameTextRect()
                painter.setBorderRgba(self._uiNameRgba)
                painter.setFont(self._uiNameTextFont)
                textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                string = self.windowModel().drawNameText()
                painter.drawText(
                    rect,
                    textOption,
                    string
                )
            # Index
            if self.windowModel().indexText() is not None:
                rect = self.windowModel().indexTextRect()
                painter.setBorderRgba(self._uiIndexRgba)
                painter.setFont(self._uiIndexFont)
                textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                string = self.windowModel().indexText()
                painter.drawText(
                    rect,
                    textOption,
                    string
                )
    #
    def eventFilter(self, *args):
        event = args[1]
        if event.type() == QtCore.QEvent.WindowDeactivate:
            self.windowModel()._isWindowActive = False
            self.windowModel()._updateWindowActiveState()
        elif event.type() == QtCore.QEvent.WindowActivate:
            self.windowModel()._isWindowActive = True
            self.windowModel()._updateWindowActiveState()
        return False
    #
    def closeEvent(self, event):
        pass
    #
    def confirmAction(self):
        self.confirmClicked.emit()
    #
    def setDefaultSize(self, width, height):
        self.windowModel().setDefaultSize(width, height)
    #
    def setIndexText(self, number):
        self.windowModel().setIndexText(number)
    #
    def setVersion(self, number):
        self.setIndexText(number)
    #
    def setIcon(self, iconKeyword, iconWidth=24, iconHeight=24):
        self.windowModel().setIcon(iconKeyword, iconWidth, iconHeight)
        #
        iconFile = uiCore._toLxOsIconFile(iconKeyword)
        pixmap = QtGui.QPixmap(iconFile)
        #
        icon = QtGui.QIcon()
        icon.addPixmap(
            pixmap,
            QtGui.QIcon.Normal,
            QtGui.QIcon.On)
        #
        self.setWindowIcon(icon)
    #
    def setNameText(self, string):
        self.windowModel().setNameText(string)
        #
        self.setWindowTitle(string)
    #
    def setTitle(self, string):
        self.windowModel().setNameText(string)
        #
        self.setWindowTitle(string)
    #
    def setMargins(self, *args):
        self.windowModel().setViewportLayoutMargins(*args)
    #
    def setSpacing(self, value):
        self.windowModel().setSpacing(value)
    #
    def setStatusEnable(self, boolean):
        self.windowModel().setStatusEnable(boolean)
    #
    def setDialogEnable(self, boolean):
        self.windowModel().setDialogEnable(boolean)
    #
    def setMaximizeEnable(self, boolean):
        self.windowModel().setMaximizeEnable(boolean)
    #
    def setMinimizeEnable(self, boolean):
        self.windowModel().setMinimizeEnable(boolean)
    #
    def setExpandEnable(self, boolean):
        self.windowModel().setExpandEnable(boolean)
    #
    def isExpandEnable(self):
        return self.windowModel().isExpandEnable()
    #
    def setMaxProgressValue(self, value):
        self.windowModel().setMaxProgressValue(value)
    #
    def maxProgressValue(self):
        return self.windowModel().maxProgressValue()
    #
    def setProgressValue(self, value, maxValue=None):
        self.windowModel().setProgressValue(value, maxValue)
    #
    def progressValue(self):
        return self.windowModel().progressValue()
    #
    def setProgressStatus(self, status):
        pass
    #
    def updateProgress(self, *args):
        self.windowModel().updateProgress()
    #
    def addWidget(self, widget):
        self.windowModel().addWidget(widget)
    #
    def uiShow(self, pos=None, size=None):
        self.windowModel().uiShow(pos, size)
        #
        self.setFocus(QtCore.Qt.ActiveWindowFocusReason)
    #
    def uiQuit(self):
        self.windowModel().uiQuit()
    #
    def setQuitConnect(self, method):
        self.windowModel()._addQuitConnectMethod(method)
    #
    def setCountdownClose(self, value=5):
        self.windowModel().setCountdownClose(value)
    #
    def setCountdownCloseStop(self):
        self.windowModel().setCountdownCloseStop()
    #
    def setPlaceholderEnable(self, boolean):
        self.windowModel().setPlaceholderEnable(boolean)
    #
    def viewModel(self):
        return self._viewModel
    #
    def windowModel(self):
        return self._viewModel
    #
    def setActionData(self, actionData):
        self._menuButton.setActionData(actionData)
        if actionData:
            self._menuButton.setPressable(True)
        else:
            self._menuButton.setPressable(False)
    #
    def setupUi(self):
        self.installEventFilter(self)
        #
        self._menuButton = UiIconbutton('svg_basic@svg#menu', self)
        self._menuButton.setPressable(False)
        #
        self._closeButton = UiIconbutton('svg_basic@svg#close', self)
        self._closeButton.setTooltip(u'关闭窗口\nClose Window')
        #
        self._maximizeButton = UiIconbutton('svg_basic@svg#maximize', self)
        self._maximizeButton.hide()
        self._maximizeButton.setTooltip(u'最大化 / 正常化窗口\nMaximized / Normalize Window')
        #
        self._minimizeButton = UiIconbutton('svg_basic@svg#minimize', self)
        self._minimizeButton.hide()
        self._minimizeButton.setTooltip(u'最小化 / 正常化窗口\nMinimized / Normalize Window')
        #
        self._expandButton = UiIconbutton('svg_basic@svg#fold', self)
        self._expandButton.hide()
        self._expandButton.setTooltip(u'点击展开 / 收起主面板\nExpand / Contract Window')
        #
        self._helpButton = UiIconbutton('svg_basic@svg#help', self)
        self._helpButton.hide()
        #
        self._confirmButton = UiIconbutton('svg_basic@svg#confirm', self)
        self._confirmButton.hide()
        self._confirmButton.setNameText('Confirm')
        self._confirmButton.setTooltip(u'确认操作 / 修改\nConfirm Operated / Changed')
        self._confirmButton.clicked.connect(self.confirmAction)
        self._confirmButton.clicked.connect(self.uiQuit)
        #
        self._cancelButton = UiIconbutton('svg_basic@svg#cancel', self)
        self._cancelButton.hide()
        self._cancelButton.setNameText('Cancel')
        self._cancelButton.setTooltip(u'取消操作 / 修改\nCancel Operated / Changed')
        self._cancelButton.clicked.connect(self.uiQuit)
        #
        self._progressBar = uiCore.QProgressBar()
        self._progressBar.setParent(self)
        #
        self._viewModel = uiModelBasic.UiWindowModel(self)
        #
        self._closeButton.clicked.connect(self.uiQuit)
        #
        self._maximizeButton.clicked.connect(self._viewModel._maximizeButtonPressAction)
        self._minimizeButton.clicked.connect(self._viewModel._minimizeButtonPressAction)
        self._expandButton.clicked.connect(self._viewModel._expandButtonPressAction)


#
class _UiSeparateWindow(_UiWindowBasic):
    def __init__(self, parent=uiCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(uiCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initWindowBasic()
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint), self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self._uiBackgroundRgba = 63, 63, 63, 223
        #
        self.viewModel().setMargins(2, 2, 2, 2)
        #
        self.setIcon('svg_basic@svg#subWindow', 16, 16)
        #
        self._uiNameTextFont = uiCore.xFont(size=10, weight=75, family=_families[1])
        #
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self._closeButton.setIcon('svg_basic@svg#unseparateWindow')
    # Override
    def uiQuit(self):
        self.closed.emit()


#
class _UiChartBasic(uiCore.QWidget):
    def _initChartBasic(self):
        self.setAttribute(uiCore.QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding,
            uiCore.QSizePolicy.Expanding
        )
        # noinspection PyArgumentEqualDefault
        self.setFont(
            uiCore.xFont(size=8, weight=50, family=uiCore._families[1])
        )
        #
        self._initChartBasicUi()
    #
    def _initChartBasicUi(self):
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 0, 0, 0, 0
        #
        self._uiImageBackgroundRgba = 0, 0, 0, 0
        self._uiImageBorderRgba = 95, 95, 95, 255
        #
        self._uiRimBackgroundRgba = 39, 39, 39, 255
        self._uiRimBorderRgba = 95, 95, 95, 255
        #
        self._uiTextRgba = 191, 191, 191, 255
    #
    def mousePressEvent(self, event):
        if event.button() == uiCore.QtCore.Qt.LeftButton:
            self.chartModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == uiCore.QtCore.Qt.LeftButton:
            self.chartModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == uiCore.QtCore.Qt.NoButton:
            self.chartModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == uiCore.QtCore.Qt.LeftButton:
                self.chartModel()._pressExecuteAction(event)
            else:
                event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == uiCore.QtCore.Qt.LeftButton:
            self.chartModel()._pressStopAction(event)
        else:
            event.ignore()
    #
    def resizeEvent(self, event):
        if self.chartModel()._isSizeChanged():
            self.chartModel().update()
    #
    def setChartDatum(self, datum):
        self.chartModel().setChartDatum(datum)
    #
    def setImage(self, image):
        self.chartModel().setImage(image)
    #
    def setImageSize(self, w, h):
        self.chartModel().setImageSize(w, h)
    #
    def setHAlign(self, align):
        self.chartModel().setHAlign(align)
    #
    def setVAlign(self, align):
        self.chartModel().setVAlign(align)
    #
    def setSide(self, value):
        self.chartModel().setSide(value)
    #
    def chartModel(self):
        return self._chartModel
    #
    def setupUi(self):
        self._chartModel = None


#
class _UiTreeItemBasic(_UiItemBasic):
    # noinspection PyArgumentList
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.itemModel()._isPressable:
                self.clicked.emit()
            #
            event.ignore()
        elif event.button() == QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
            #
            event.accept()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        # Background
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRect(self.itemModel()._uiBasicRect)
        # Check
        if self.itemModel().isCheckEnable():
            painter.setDrawImage(self.itemModel()._uiCheckRect, self.itemModel()._uiCheckIcon)
        # Filter Color
        if self.itemModel().isColorEnable():
            painter.setBackgroundRgba(self._uiColorBackgroundRgba)
            painter.setBorderRgba(self._uiColorBorderRgba)
            painter.drawRect(self.itemModel()._uiColorRect)
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
            if self.itemModel().subIcon() is not None:
                painter.setDrawImage(
                    self.itemModel().subIconRect(),
                    self.itemModel().subIcon()
                )
        # Menu
        if self.itemModel().isPressMenuEnable():
            painter.setDrawImage(
                self.itemModel().menuIconRect(),
                self.itemModel().menuIcon()
            )
        # Namespace
        if self.itemModel().namespaceText() is not None:
            painter.setBorderRgba(self._uiNamespaceRgba)
            rect = self.itemModel()._uiNamespaceRect
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.drawText(
                rect,
                textOption,
                self.itemModel().namespaceText()
            )
        # Name
        if self.itemModel().nameText() is not None:
            font = self.font()
            font.setItalic(self._uiFontItalic)
            painter.setFont(font)
            rect = self.itemModel()._uiNameTextRect
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            string = self.itemModel().drawNameText()
            if self.itemModel()._filterKeyword is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    string, self.itemModel()._filterKeyword,
                    self._uiNameRgba
                )
            else:
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(
                    rect,
                    textOption,
                    string
                )
        # Index
        if self.itemModel().indexText() is not None:
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(
                self.itemModel().indexTextRect(),
                QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter,
                str(self.itemModel().indexText())
            )
    # noinspection PyUnusedLocal
    @uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiActionViewDropMethod
    def _menuDropAction(self):
        pass
    #
    def setActionData(self, actions, title=None):
        self.actionData = actions
        #
        if self.actionData:
            self.itemModel().setPressMenuEnable(True)
        else:
            self.itemModel().setPressMenuEnable(False)
        if title:
            self.actionTitle = title
    #
    def setupUi(self):
        self._itemModel = uiModelBasic.UiTreeItemModel(self)


# Scroll Bar
class UiScrollBar(uiCore.QWidget):
    valueChanged = uiCore.uiSignal()
    stop = uiCore.uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(UiScrollBar, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setMouseTracking(True)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def enterEvent(self, event):
        pass
    #
    def leaveEvent(self, event):
        self.viewModel()._clearHover()
    #
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(True)
        elif event.key() == QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(True)
        elif event.key() == QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(True)
        else:
            event.ignore()
    #
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(False)
        elif event.key() == QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(False)
        elif event.key() == QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(False)
        else:
            event.ignore()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStopAction(event)
            #
            self.viewModel()._hoverExecuteAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.clsSuper.mouseMoveEvent(event)
            #
            self.viewModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.viewModel()._pressExecuteAction(event)
            else:
                event.ignore()
    #
    def resizeEvent(self, event):
        self.viewModel().update()
        #
        self.viewModel()._updateTempValue()
    #
    def paintEvent(self, event):
        def setDrawBaseArea():
            painter.setBackgroundRgba(self._uiBackgroundRgba)
            painter.setBorderRgba(self._uiBorderRgba)
            painter.drawRect(self.viewModel()._uiBasicRect)
        #
        def setDrawClickArea():
            if self.viewModel()._clickFlag is True:
                painter.setBackgroundRgba(0, 127, 127, 255)
                painter.setBorderRgba(0, 0, 0, 0)
                #
                painter.drawRect(self.viewModel()._clickRect)
        #
        def setDrawSlider():
            if self.viewModel().maximum() > 0:
                if self.viewModel()._pressFlag is True:
                    backgroundRgba = self._uiSliderPressBackgroundRgba
                    borderRgba = self._uiSliderPressBorderRgba
                else:
                    if self.viewModel()._isSliderHover:
                        backgroundRgba = self._uiSliderHoverBackgroundRgba
                        borderRgba = self._uiSliderHoverBorderRgba
                    else:
                        backgroundRgba = self._uiSliderBackgroundRgba
                        borderRgba = self._uiSliderBorderRgba
                #
                painter.setBackgroundRgba(backgroundRgba)
                painter.setBorderRgba(borderRgba)
                #
                painter.drawRect(self.viewModel()._uiSliderRect)
        #
        painter = uiCore.QPainter_(self)
        #
        if self.viewModel().isScrollable():
            setDrawBaseArea()
            # Scroll
            setDrawBaseArea()
            # Click
            setDrawClickArea()
            # Slider
            setDrawSlider()
    #
    def setDirection(self, value):
        self.viewModel().setDirection(value)
    #
    def isScrollable(self):
        return self.viewModel().isScrollable()
    #
    def value(self):
        return self.viewModel().value()
    #
    def maximum(self):
        return self.viewModel().maximum()
    #
    def minimum(self):
        return self.viewModel().minimum()
    #
    def scrollToMaximum(self):
        self.viewModel().scrollToMaximum()
    #
    def scrollToMinimum(self):
        self.viewModel().scrollToMinimum()
    #
    def setValue(self, value, isRow=False):
        self.viewModel().setValue(value, isRow)
    #
    def setRow(self, row):
        self.viewModel().setRow(row)
    #
    def setPage(self, page):
        self.viewModel().setPage(page)
    #
    def setAbsHeight(self, value):
        self.viewModel().setAbsHeight(value)
    #
    def setBasicScrollValue(self, value):
        self.viewModel().setBasicScrollValue(value)
    #
    def setRowScrollValue(self, value):
        self.viewModel().setRowScrollValue(value)
    #
    def setTimerInterval(self, value):
        self.viewModel().setTimerInterval(value)
    #
    def setItemColumnCount(self, value):
        self.viewModel().setItemColumnCount(value)
    #
    def setActionData(self, actions):
        self._menuButton.setActionData(actions)
        self.viewModel().setPressMenuEnable(True)
    #
    def viewModel(self):
        return self._viewModel
    #
    def initUi(self):
        self._uiScrollBarWidth = 20
        #
        self._clickFlag = False
        #
        self._pressFlag = False
        self._dragFlag = False
        #
        self._altFlag = False
        self._shiftFlag = False
        self._ctrlFlag = False
        #
        self._uiBackgroundRgba = 56, 56, 56, 255
        self._uiBorderRgba = 95, 95, 95, 255
        #
        self._uiNameRgba = 223, 223, 223, 255
        #
        self._uiScrollBackgroundRgba = 0, 0, 0, 0
        self._uiScrollBorderRgba = 0, 0, 0, 0
        #
        self._uiSliderBackgroundRgba = 71, 71, 71, 255
        self._uiSliderBorderRgba = 95, 95, 95, 255
        #
        self._uiSliderHoverBackgroundRgba = 95, 95, 95, 255
        self._uiSliderHoverBorderRgba = 127, 127, 127, 255
        #
        self._uiSliderPressBackgroundRgba = 127, 127, 127, 255
        self._uiSliderPressBorderRgba = 191, 191, 191, 255
    #
    def setupUi(self):
        self._menuButton = UiIconbutton('svg_basic@svg#menu', self)
        self._subScrollButton = UiIconbutton('svg_basic@svg#vScrollSub', self)
        self._subScrollButton.setTooltip(u'''单击：向上翻页\n按住：向上滚动''')
        self._addScrollButton = UiIconbutton('svg_basic@svg#vScrollAdd', self)
        self._addScrollButton.setTooltip(u'''单击：向下翻页\n按住：向下滚动''')
        self._tooltipWidget = uiCore.UiTooltipWidget(self)
        #
        self._viewModel = uiModelBasic.UiScrollBarModel(self)


#
class _UiIconbuttonBasic(_UiItemBasic):
    upScrolled = uiCore.uiSignal()
    downScrolled = uiCore.uiSignal()
    @uiCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStartAction(event)
            #
            self._toolActionDropAction()
        else:
            event.ignore()
    @uiCore.uiTooltipClearMethod
    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        if delta > 0:
            self.upScrolled.emit()
        if delta < 0:
            self.downScrolled.emit()
        #
        event.accept()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.SmoothPixmapTransform)
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
            if self.itemModel().subIcon() is not None:
                painter.setDrawImage(
                    self.itemModel().subIconRect(),
                    self.itemModel().subIcon()
                )
        # Extend Icon
        if self.itemModel().extendIcon() is not None:
            painter.setDrawImage(
                self.itemModel().extendIconRect(),
                self.itemModel().extendIcon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBackgroundRgba(self._uiBackgroundRgba)
            painter.setBorderRgba(self._uiNameRgba)
            #
            font = self.font()
            font.setItalic(self._uiFontItalic)
            painter.setFont(
                font
            )
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel()._uiNameTextRect,
                textOption,
                self.itemModel().nameText()
            )
    @uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiActionViewDropMethod
    def _toolActionDropAction(self):
        pass
    #
    def setActionData(self, actionData):
        self.actionData = actionData
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
        self.setUiSize()
    #
    def setExtendIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setExtendIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
    #
    def setNameText(self, string):
        self.itemModel().setNameText(string)
        w, h = self.itemModel().frameSize()
        self.setMaximumSize(QtCore.QSize(166667, h))
        self.setMinimumSize(QtCore.QSize(0, h))
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    #
    def setUiSize(self):
        # self.setMaximumSize(*self.itemModel().frameSize())
        self.setMinimumSize(*self.itemModel().frameSize())
    #
    def setupUi(self):
        self._itemModel = uiModelBasic.UiIconButtonModel(self)
        #
        self.actionData = []


#
class UiIconbutton(_UiIconbuttonBasic):
    def __init__(self, iconKeyword=None, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initItemBasic()
        #
        self.setupUi()
        #
        if iconKeyword is not None:
            self.setIcon(iconKeyword)
        #
        self.setUiSize()


#
class _UiMenuIconbuttonBasic(_UiItemBasic):
    @uiCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStartAction(event)
            #
            self._toolActionDropAction()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
            if self.itemModel().subIcon() is not None:
                painter.setDrawImage(
                    self.itemModel().subIconRect(),
                    self.itemModel().subIcon()
                )
            if self.itemModel().extendIcon() is not None:
                painter.setDrawImage(
                    self.itemModel().extendIconRect(),
                    self.itemModel().extendIcon()
                )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBorderRgba(self._uiNameRgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(uiCore.xFont(size=8, weight=50, italic=self._uiFontItalic, family=_families[0]))
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel().nameTextRect(),
                textOption,
                self.itemModel().nameText()
            )
    # noinspection PyUnusedLocal
    @uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiActionViewDropMethod
    def _toolActionDropAction(self):
        pass
    #
    def setActionData(self, actionData):
        self.actionData = actionData
        #
        self._updatePressable()
    #
    def _updatePressable(self):
        self.setPressable(self.actionData != [])
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
        #
        self._updatePressable()
        self.setUiSize()
    #
    def setExtendIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setExtendIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
    #
    def setNameText(self, string):
        self.itemModel().setNameText(string)
        w, h = self.itemModel().frameSize()
        self.setMaximumSize(QtCore.QSize(166667, h))
        self.setMinimumSize(QtCore.QSize(0, h))
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    #
    def setUiSize(self):
        # self.setMaximumSize(*self.itemModel().frameSize())
        self.setMinimumSize(*self.itemModel().frameSize())
    #
    def setupUi(self):
        self._itemModel = uiModelBasic.UiIconButtonModel(self)
        #
        self.actionData = []


#
class UiMenuIconbutton(_UiMenuIconbuttonBasic):
    def __init__(self, iconKeyword=None, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        # self.setSizePolicy(uiCore.QSizePolicy.Expanding, uiCore.QSizePolicy.Preferred)
        #
        self._initItemBasic()
        #
        self.setupUi()
        #
        if iconKeyword:
            self.setIcon(iconKeyword)
        #
        self.setUiSize()


#
class QLineEdit_(uiCore.QLineEdit):
    entryChanged = uiCore.uiSignal()
    valueChanged = uiCore.uiSignal()
    focusChanged = uiCore.uiSignal()
    #
    focusOut = uiCore.uiSignal()
    focusIn = uiCore.uiSignal()
    #
    clicked = uiCore.uiSignal()
    doubleClicked = uiCore.uiSignal()
    def __init__(self, *args):
        self.clsSuper = super(QLineEdit_, self)
        self.clsSuper.__init__(*args)
        # noinspection PyUnresolvedReferences
        self.textChanged.connect(self.enterChangedEmit)
        # noinspection PyUnresolvedReferences
        self.returnPressed.connect(self.enterChangedEmit)
        #
        self._initWidget()
        #
        self.contextMenu = None
        #
        self.setUiStyle()
        self.setUiSize()
    #
    def _initWidget(self):
        self._initItemAttr()
    #
    def _initItemAttr(self):
        self._maxValue, self._miniValue = None, None
    #
    def mousePressEvent(self, event):
        self.clsSuper.mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
    #
    def mouseDoubleClickEvent(self, event):
        self.clsSuper.mouseDoubleClickEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            return self.doubleClicked.emit()
    #
    def keyPressEvent(self, event):
        self.clsSuper.keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Control:
            pass
        elif event.key() == QtCore.Qt.Key_Shift:
            pass
        elif event.key() == QtCore.Qt.Key_Alt:
            pass
        else:
            event.ignore()
    #
    def keyReleaseEvent(self, event):
        self.clsSuper.keyReleaseEvent(event)
        if event.key() == QtCore.Qt.Key_Control:
            pass
        elif event.key() == QtCore.Qt.Key_Shift:
            pass
        elif event.key() == QtCore.Qt.Key_Alt:
            pass
        else:
            event.ignore()
    #
    def wheelEvent(self, event):
        if type(self.validator()) is QtGui.QIntValidator or type(self.validator()) is QtGui.QDoubleValidator:
            if not self.hasFocus():
                self.setFocus(QtCore.Qt.MouseFocusReason)
            #
            delta = event.angleDelta().y()
            #
            p = self.cursorPosition()
            value = self.value()
            if delta > 0:
                newValue = value + 1
            else:
                newValue = value - 1
            #
            self.setValue(newValue)
            self.setCursorPosition(p)
            #
            self.entryChanged.emit()
    #
    def focusInEvent(self, event):
        self.clsSuper.focusInEvent(event)
        self.focusChanged.emit()
        self.focusIn.emit()
    #
    def focusOutEvent(self, event):
        self.clsSuper.focusOutEvent(event)
        self.focusChanged.emit()
        self.focusOut.emit()
    @uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    #
    def contextMenuEvent(self, event):
        actions = [
            ('Basic', ),
            ('Copy#Ctrl + C', 'svg_basic@svg#copy', self.isSelected(), self.copy),
            ('Paste#Ctrl + V', 'svg_basic@svg#copy', True, self.paste),
            ('Cut#Ctrl + X', 'svg_basic@svg#copy', self.isSelected(), self.cut),
            ('Extend', ),
            ('Undo#Ctrl + Z', 'svg_basic@svg#undo', True, self.undo),
            ('Redo#Ctrl + Y', 'svg_basic@svg#redo', True, self.redo),
            ('Select All#Ctrl + A', 'svg_basic@svg#copy', True, self.selectAll)
        ]
        #
        if self.isReadOnly():
            actions = [
                ('Basic',),
                ('Copy#Ctrl + C', 'svg_basic@svg#copy', True, self.copy),
                ('Extend', ),
                ('Select All#Ctrl + A', 'svg_basic@svg#copy', True, self.selectAll)
            ]
        #
        if actions:
            self.contextMenu = _UiActionDropView(self)
            self.contextMenu.setFocusProxy(self)
            self.contextMenu.installEventFilter(self)
            self.contextMenu.setActionData(actions)
            self.contextMenu.setDrop()
    #
    def paste(self):
        self.clsSuper.paste()
        self.entryChanged.emit()
    #
    def del_(self):
        self.clsSuper.del_()
        self.entryChanged.emit()
    #
    def isSelected(self):
        boolean = False
        if self.selectedText():
            boolean = True
        return boolean
    #
    def enterChangedEmit(self):
        self.entryChanged.emit()
    #
    def setIntValidator(self):
        self.setValidator(QtGui.QIntValidator())
    #
    def setFloatValidator(self):
        self.setValidator(QtGui.QDoubleValidator())
    #
    def setTextValidator(self, limit):
        reg = QtCore.QRegExp('[a-zA-Z]' + '[a-zA-Z0-9_]'*limit)
        validator = QtGui.QRegExpValidator(reg, self)
        self.setValidator(validator)
    #
    def setValue(self, value):
        if self._maxValue is not None:
            if value > self._maxValue:
                value = self._maxValue
        if self._miniValue is not None:
            if value < self._miniValue:
                value = self._miniValue
        #
        self.setText(str(value))
    #
    def value(self):
        text = self.text()
        if type(self.validator()) is QtGui.QIntValidator:
            if text:
                return int(text)
            else:
                return 0
        elif type(self.validator()) is QtGui.QDoubleValidator:
            if text:
                return float(text)
            else:
                return 0.0
        else:
            return 0
    #
    def setValueRange(self, minimum, maximum):
        self._miniValue, self._maxValue,  = minimum, maximum
        if self._maxValue is not None:
            self.validator().setTop(self._maxValue)
        if self._miniValue is not None:
            self.validator().setBottom(self._miniValue)
    #
    def setEnterable(self, boolean):
        self.setReadOnly(not boolean)
        #
        if boolean is True:
            self.setFocus(QtCore.Qt.MouseFocusReason)
        else:
            self.clearFocus()
    #
    def setUiStyle(self):
        self.setStyleSheet(
            'QLineEdit{background: rgba(0, 0, 0, 0) ; color: rgba(191, 191, 191, 255)}'
            'QLineEdit{border: none}'
            'QLineEdit{selection-color: rgba(255, 255, 255, 255) ; selection-background-color: rgba(0, 127, 127, 255)}'
        )
    #
    def setUiSize(self):
        self.setMaximumSize(166667, 20)
        self.setMinimumSize(0, 20)


#
class QTextEdit_(uiCore.QTextEdit):
    entryChanged = uiCore.uiSignal()
    focusChanged = uiCore.uiSignal()
    #
    focusIn = uiCore.uiSignal()
    focusOut = uiCore.uiSignal()
    #
    menuWidth = 160
    # noinspection PyArgumentList
    def __init__(self, parent=None, *args, **kwargs):
        self.clsSuper = super(QTextEdit_, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self._parent = parent
        #
        self.isPressMenuEnable = True
        #
        self.contextMenu = None
        #
        self.setUiStyle()
    #
    def enterEvent(self, event):
        if not self.hasFocus() and not self.isReadOnly():
            parent = self._parent
            if parent:
                if hasattr(parent, '_setUiPressStyle'):
                    parent._setUiPressStyle(uiCore.HoverState)
    #
    def leaveEvent(self, event):
        if not self.hasFocus() and not self.isReadOnly():
            parent = self._parent
            if parent:
                if hasattr(parent, '_updateUiStyle'):
                    parent._updateUiStyle()
    #
    def keyPressEvent(self, event):
        self.clsSuper.keyPressEvent(event)
        self.entryChanged.emit()
    #
    def focusInEvent(self, event):
        self.clsSuper.focusInEvent(event)
        self.focusChanged.emit()
        self.focusIn.emit()
    #
    def focusOutEvent(self, event):
        self.clsSuper.focusOutEvent(event)
        self.focusChanged.emit()
        self.focusOut.emit()
    @uiActionEventFilterMethod
    def eventFilter(self, *args):
        return False
    # noinspection PyArgumentList
    def contextMenuEvent(self, event):
        if self.isPressMenuEnable:
            actions = [
                ('Basic',),
                ('Copy#Ctrl + C', 'svg_basic@svg#copy', True, self.copy),
                ('Paste#Ctrl + V', 'svg_basic@svg#copy', True, self.paste),
                ('Cut#Ctrl + X', 'svg_basic@svg#copy', True, self.cut),
                ('Extend',),
                ('Undo#Ctrl + Z', 'svg_basic@svg#undo', True, self.undo),
                ('Redo#Ctrl + Y', 'svg_basic@svg#redo', True, self.redo),
                ('Select All#Ctrl + A', 'svg_basic@svg#copy', True, self.selectAll)
            ]
            #
            if self.isReadOnly():
                actions = [
                    ('Basic',),
                    ('Copy#Ctrl + C', 'svg_basic@svg#copy', True, self.copy),
                    ('Extend',),
                    ('Select All#Ctrl + A', 'svg_basic@svg#copy', True, self.selectAll)
                ]
            #
            if actions:
                self.contextMenu = _UiActionDropView(self)
                self.contextMenu.setFocusProxy(self)
                self.contextMenu.installEventFilter(self)
                self.contextMenu.setActionData(actions)
                self.contextMenu.setDrop()
    # noinspection PyArgumentList
    def paste(self):
        self.clsSuper.paste()
        #
        self.entryChanged.emit()
    #
    def insertFromMimeData(self, source):
        if source.hasText():
            cursor = self.textCursor()
            cursor.insertText(source.text())
        else:
            self.clsSuper.insertFromMimeData(source)
    #
    def setText(self, *args):
        self.clsSuper.setText(*args)
        self.entryChanged.emit()
    #
    def setEnterEnable(self, boolean):
        self.setReadOnly(not boolean)
    #
    def setEditEnable(self, boolean):
        self.setReadOnly(not boolean)
        self.isPressMenuEnable = boolean
    #
    def setSelectionEnable(self, boolean):
        if boolean is False:
            self.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
    #
    def setUiStyle(self):
        self.setStyleSheet(
            'QTextEdit{background: rgba(0, 0, 0, 0) ; color: rgba(223, 223, 223, 255)}'
            'QTextEdit{border: none}'
            'QTextEdit{selection-color: rgba(255, 255, 255, 255) ; selection-background-color: rgba(0, 127, 127, 255)}'
        )
        uiCore.setScrollBarStyle(self)


#
class _UiValueEnterlabelBasic(uiCore.QWidget):
    def _initItemBasic(self):
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding, uiCore.QSizePolicy.Minimum
        )
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        #
        self._initItemBasicAttr()
        self._initItemBasicUi()
        #
        self.setUiSize()
    #
    def _initItemBasicAttr(self):
        pass
    #
    def _initItemBasicUi(self):
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 95, 95, 95, 255
        self._uiEnterBackgroundRgbaLis = [(47, 47, 47, 255)]
        self._uiEnterBorderRgbaLis = [(95, 95, 95, 255)]
        #
        self._uiNameRgba = 191, 191, 191, 255
        #
        self._uiBorderStyle = 'solid'
        #
        self.setFont(
            uiCore.xFont()
        )
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        painter.setFont(self.font())
        # Name
        if self.itemModel().nameText() is not None:
            rect = self.itemModel().nameTextRect()
            textOption = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
            painter.setBorderRgba(self._uiNameRgba)
            painter.drawText(rect, textOption, self.itemModel().nameText() + ' : ')
        #
        if self.itemModel().value() is not None:
            if self.itemModel().isEnterable():
                for index, rect in enumerate(self.itemModel().enterRects()):
                    isEntered = self.itemModel().isEntered(index)
                    if isEntered:
                        borderWidth = 2
                        borderRadius = 10
                    else:
                        borderWidth = 1
                        borderRadius = 10
                    #
                    painter.setDrawButtonBasic(
                        rect,
                        borderWidth, borderRadius,
                        self._uiEnterBackgroundRgbaLis[index], self._uiEnterBorderRgbaLis[index],
                        self._uiBorderStyle
                    )
    #
    def setEnterEnable(self, boolean):
        self.itemModel().setEnterEnable(boolean)
    #
    def setNameText(self, text):
        self.itemModel().setNameText(text)
    #
    def nameText(self):
        return self.itemModel().nameText()
    #
    def setNameTextWidth(self, value):
        self.itemModel().setNameTextWidth(value)
    #
    def setSpacerLabel(self, text):
        pass
    #
    def setValueRange(self, minimum, maximum):
        self.itemModel().setValueRange(minimum, maximum)
    #
    def setValue(self, value):
        self.itemModel().setValue(value)
    #
    def value(self):
        return self.itemModel().value()
    #
    def datum(self):
        return self.itemModel().value()
    #
    def setDefaultValue(self, value):
        self.itemModel().setDefaultValue(value)
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(166667, 20))
        self.setMinimumSize(QtCore.QSize(0, 20))
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._itemModel = uiModelBasic.UiValueEnterItemModel(self)
        self._itemModel.setEnterWidgetClass(QLineEdit_)


#
class _UiFilterEnterlabelBasic(uiCore.QWidget):
    entryChanged = uiCore.uiSignal()
    def _initItemBasic(self):
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding, uiCore.QSizePolicy.Preferred
        )
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        #
        self._initItemBasicAttr()
        self._initItemBasicUi()
    #
    def _initItemBasicAttr(self):
        self._historyLis = []
    #
    def _initItemBasicUi(self):
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 95, 95, 95, 255
        #
        self._uiNameRgba = 191, 191, 191, 255
        #
        self._uiBorderStyle = 'solid'
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        painter.setFont(self.font())
        # Background
        painter.setBackgroundRgba(self._uiEnterBackgroundRgba)
        #
        borderWidth = 1
        borderRadius = 10
        if self.itemModel().isEntered():
            painter.setDrawButtonBasic(
                self.itemModel().basicRect(),
                borderWidth + 1, borderRadius,
                self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._uiBorderStyle
            )
        else:
            painter.setDrawButtonBasic(
                self.itemModel().basicRect(),
                borderWidth, borderRadius,
                self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._uiBorderStyle
            )
    #
    def setNameText(self, string):
        if string is not None:
            self._enterWidget.setPlaceholderText(u'Enter Filter Keyword ( {} ) ...'.format(string))
    #
    def setWidth(self, width):
        self.entryWidget.setMinimumWidth(width)
        self.entryWidget.setMaximumWidth(width)
    #
    def setDatum(self, data):
        self.itemModel().setDatum(data)
    #
    def _uploadHistoryAction(self):
        string = self._enterWidget.text()
        if string:
            if not string in self._historyLis:
                self._historyLis.append(string)
            #
            self.writeHistory()
    #
    def _loadHistoryAction(self):
        def setBranch(keywordFilterString):
            def setMethod():
                self._enterWidget.setText(keywordFilterString)
                #
                self.enterChangedEmit()
            #
            actionDatumLis.append(
                (keywordFilterString, 'svg_basic@svg#history', True, setMethod)
            )
        #
        self._uploadHistoryAction()
        #
        actionDatumLis = []
        #
        if self._historyLis:
            for i in self._historyLis[-10:]:
                setBranch(i)
        #
        self._historyButton.setActionData(actionDatumLis)
    #
    def readHistory(self):
        filterHistoryFile = lxConfigure.lxUserFilerHistoryFile()
        data = lxBasic.readOsJson(filterHistoryFile)
        if data:
            self._historyLis = data
    #
    def writeHistory(self):
        filterHistoryFile = lxConfigure.lxUserFilerHistoryFile()
        data = self._historyLis[-10:]
        lxBasic.writeOsJson(data, filterHistoryFile)
    #
    def removeHistory(self):
        string = self._enterWidget.text()
        if string:
            if string in self._historyLis:
                self._historyLis.remove(string)
    #
    def datum(self):
        searchData = unicode(self._enterWidget.text())
        if searchData:
            return searchData
    #
    def setEnterClear(self):
        self._enterWidget.clear()
    #
    def enterChangedEmit(self):
        self.entryChanged.emit()
        #
        self.itemModel()._updateButtonVisible()
    #
    def setUiEnterStatus(self, status):
        self.itemModel().setUiEnterStatus(status)
    #
    def setUiEnterState(self, state):
        self.itemModel().setUiEnterState(state)
    #
    def setUiStyle(self):
        pass
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(166667, 20))
        self.setMinimumSize(QtCore.QSize(0, 20))
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._historyButton = UiIconbutton('svg_basic@svg#search')
        self._historyButton.setParent(self)

        #
        self._enterWidget = QLineEdit_()
        self._enterWidget.setParent(self)
        # noinspection PyArgumentEqualDefault
        self._enterWidget.setFont(uiCore.xFont(size=8, weight=50))
        self._enterWidget.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self._enterWidget.entryChanged.connect(self.enterChangedEmit)
        # Copy
        self._copyButton = UiIconbutton('svg_basic@svg#copy')
        self._copyButton.setParent(self)
        self._copyButton.hide()
        self._copyButton.setTooltip(
            u'点击复制输入'
        )
        #
        self._clearButton = UiIconbutton('svg_basic@svg#clear')
        self._clearButton.setParent(self)
        self._clearButton.hide()
        #
        self._itemModel = uiModelBasic.UiFilterEnterItemModel(self)
        #
        self._historyButton.clicked.connect(self._loadHistoryAction)
        #
        self._enterWidget.focusChanged.connect(self._itemModel._updateUiEnterState)
        self._enterWidget.focusOut.connect(self._uploadHistoryAction)
        self._clearButton.clicked.connect(self.setEnterClear)


#
class UiFilterEnterlabel(_UiFilterEnterlabelBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initItemBasic()
        #
        self.setupUi()
        #
        self.setUiSize()
        #
        self.readHistory()
        self._loadHistoryAction()


#
class _UiDatumEntryItemBasic(_UiItemBasic):
    entryChanged = uiCore.uiSignal()
    chooseChanged = uiCore.uiSignal()
    checkChanged = uiCore.uiSignal()
    #
    datumChanged = uiCore.uiSignal()
    def _initEnterItemBasic(self):
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding, uiCore.QSizePolicy.Minimum
        )
        #
        self._initItemBasic()
        self._initEnterItemBasicAttr()
        self._initEnterItemBasicUi()
        #
        self.setMouseTracking(True)
    #
    def _initEnterItemBasicAttr(self):
        self._wordWarp = False
    #
    def _initEnterItemBasicUi(self):
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 95, 95, 95, 255
        #
        self._uiNameRgba = 191, 191, 191, 255
        #
        self._uiBorderStyle = 'solid'
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        painter.setFont(self.font())
        # Name
        if self.itemModel().nameText() is not None:
            rect = self.itemModel()._uiNameTextRect
            textOption = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
            if self.itemModel()._filterKeyword is not None:
                painter.setDrawFilterString(
                    rect,
                    True,
                    self.itemModel().nameText() + ' : ', self.itemModel()._filterKeyword,
                    self._uiNameRgba
                )
            else:
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(rect, textOption, self.itemModel().nameText() + ' : ')
        # Enter
        if self.itemModel().isEnterable():
            borderWidth = 1
            borderRadius = 10
            # Background
            painter.setBackgroundRgba(self._uiEnterBackgroundRgba)
            if self.itemModel().isEntered():
                painter.setDrawButtonBasic(
                    self.itemModel().basicRect(),
                    borderWidth + 1, borderRadius,
                    self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._uiBorderStyle
                )
            else:
                painter.setDrawButtonBasic(
                    self.itemModel().basicRect(),
                    borderWidth, borderRadius,
                    self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._uiBorderStyle
                )
        else:
            if self.itemModel().datumText() is not None:
                font = painter.font()
                font.setItalic(self._uiFontItalic)
                painter.setFont(font)
                rect = self.itemModel().datumRect()
                #
                if self.itemModel()._filterKeyword is not None:
                    painter.setDrawFilterString(
                        rect,
                        False,
                        self.itemModel().datumText(), self.itemModel()._filterKeyword,
                        self._uiDatumRgba
                    )
                else:
                    rectF = QtCore.QRectF(
                        rect.x(), rect.y(),
                        rect.width(), rect.height()
                    )
                    textOption = QtGui.QTextOption(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                    if self._wordWarp is True:
                        textOption.setWrapMode(textOption.WordWrap)
                        string = self.itemModel().datumText()
                    else:
                        textOption.setWrapMode(textOption.NoWrap)
                        string = self.itemModel().drawDatumText()
                    #
                    painter.setBorderRgba(self._uiDatumRgba)
                    painter.drawText(
                        rectF,
                        string,
                        textOption
                    )
        # Choose
        if self.itemModel().isChooseable():
            rect = self.itemModel().indexTextRect()
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.setBorderRgba(self._uiIndexRgba)
            text = '{}/{}'.format(self.itemModel().chooseIndex() + 1, self.itemModel().chooseCount())
            painter.drawText(
                rect,
                textOption,
                text
            )
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter.setDrawImage(
                self.itemModel()._uiCheckRect, self.itemModel()._uiCheckIcon
            )
    @uiChooseBoxEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiChooseViewDropMethod
    def _chooseDropAction(self):
        pass
    #
    def setNameText(self, string):
        self.itemModel().setNameText(string)
    #
    def setDatum(self, datum, useAsChoose=False):
        if useAsChoose is True:
            self.setChooseEnable(True)
            self.itemModel().setDatumLis(datum)
            self.itemModel().setDatum(datum[0])
        else:
            self.itemModel().setDatum(datum)
    #
    def setDatumLis(self, lis):
        self.itemModel().setDatumLis(lis)
    #
    def setExtendDatumDic(self, dic):
        self.itemModel().setExtendDatumDic(dic)
    #
    def setDefaultDatum(self, datum):
        self.itemModel().setDefaultDatum(datum)
    #
    def setIntValidator(self):
        self.itemModel().setIntValidator()
    #
    def setTextValidator(self, limit):
        self.itemModel().setTextValidator(limit)
    #
    def setEnterEnable(self, boolean):
        self.itemModel().setEnterEnable(boolean)
    #
    def isEnterEnable(self):
        return self.itemModel().isEnterEnable()
    #
    def setEnterable(self, boolean):
        self.itemModel().setEnterable(boolean)
    #
    def ieEntryable(self):
        return self.itemModel().isEnterable()
    #
    def setChooseEnable(self, boolean):
        self.itemModel().setChooseEnable(boolean)
    #
    def isChooseEnable(self):
        return self.itemModel().isChooseEnable()
    #
    def setChoose(self, string):
        self.itemModel().setChoose(string)
    #
    def setChooseIndex(self, index):
        self.itemModel().setChooseIndex(index)
    #
    def chooseIndex(self):
        return self.itemModel().chooseIndex()
    #
    def entryEvent(self):
        self.entryChanged.emit()
        #
        self.itemModel()._updateButtonVisible()
    #
    def setEnterClear(self):
        self.itemModel().setEnterClear()
    #
    def setEntryCopy(self):
        message = self.datum()
        # noinspection PyArgumentList
        clipboard = uiCore.QApplication.clipboard()
        clipboard.setText(message)
    #
    def setChooseClear(self):
        self.itemModel().setChooseClear()
    #
    def datum(self):
        return self.itemModel().datum()
    #
    def extendDatum(self):
        return self.itemModel().extendDatum()
    #
    def datumLis(self):
        return self.itemModel().datumLis()
    #
    def extendDatumDic(self):
        return self.itemModel().extendDatumDic()
    #
    def sendChooseChangedEmit(self):
        self.chooseChanged.emit()
    #
    def _setUiPressStyle(self, state):
        self.itemModel()._setUiPressStyle(state)
    #
    def setUiSize(self):
        self.setMaximumSize(166667, 20)
        self.setMinimumSize(0, 20)
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._chooseButton = UiIconbutton('svg_basic@svg#choose', self)
        self._chooseButton.clicked.connect(self._chooseDropAction)
        self._chooseButton.setTooltip(
            u'1.左键点击：查看/选择更多选项\r\n2.中键滚动：向上/向下选择'
        )
        #
        self._entryButton = UiIconbutton('svg_basic@svg#edit', self)
        self._entryButton.setTooltip(
            u'点击启用/关闭输入锁定'
        )
        #
        self._enterWidget = QLineEdit_(self)
        self._enterWidget.setParent(self)
        self._enterWidget.setReadOnly(True)
        self._enterWidget.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        # noinspection PyArgumentEqualDefault
        self._enterWidget.setFont(
            self.font()
        )
        self._enterWidget.entryChanged.connect(self.entryEvent)
        # Copy
        self._copyButton = UiIconbutton('svg_basic@svg#copy')
        self._copyButton.setParent(self)
        self._copyButton.hide()
        self._copyButton.setTooltip(
            u'点击复制输入'
        )
        self._copyButton.clicked.connect(self.setEntryCopy)
        # Clear
        self._clearButton = UiIconbutton('svg_basic@svg#clear')
        self._clearButton.setParent(self)
        self._clearButton.clicked.connect(self.entryEvent)
        #
        self._itemModel = uiModelBasic.UiDatumEnterItemModel(self)
        #
        self._chooseButton.upScrolled.connect(self._itemModel._chooseScrollUpAction)
        self._chooseButton.downScrolled.connect(self._itemModel._chooseScrollDownAction)
        #
        self._entryButton.clicked.connect(self._itemModel._entryableSwitchAction)
        #
        self._enterWidget.focusChanged.connect(self._itemModel._updateUiEnterState)
        self._enterWidget.entryChanged.connect(self._itemModel._entryAction)
        #
        self._clearButton.clicked.connect(self.setEnterClear)


#
class _UiChooseItem(_UiItemBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initItemBasic()
        #
        self.setupUi()


#
class _UiChooseView(_UiViewBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(_UiChooseView, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initViewBasic()
        #
        self.setupUi()
    #
    def setupUi(self):
        self._hScrollBar = UiScrollBar(self)
        self._vScrollBar = UiScrollBar(self)
        #
        self._viewModel = uiModelBasic.UiChooseViewModel(self)


#
class _UiChooseDropView(uiCore.QWidget):
    currentChanged = uiCore.uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setWindowFlags(QtCore.Qt.Drawer | QtCore.Qt.FramelessWindowHint)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        # noinspection PyArgumentEqualDefault
        painter.setFont(uiCore.xFont(size=8, weight=50, family=_families[1]))
        #
        side = self.viewModel()._uiSide
        margin = self.viewModel()._uiMargin
        shadowRadius = self.viewModel()._uiShadowRadius
        #
        painter.setDrawMenuFrame(
            self.viewModel()._uiBasicRect,
            margin, side, shadowRadius, self.viewModel()._region,
            self._uiBackgroundRgba, self._uiBorderRgba
        )
        #
        if self.viewModel()._isTearable is True:
            xPos, yPos = self.viewModel()._pos
            painter.setBorderRgba(self._uiBorderRgba)
            painter.drawLine(
                QtCore.QLine(xPos, yPos, xPos + self.viewModel()._uiMainWidth, yPos - 1)
            )
    #
    def setCurrentIndex(self, index):
        self.viewModel().setCurrentIndex(index)
    #
    def setDrop(self):
        worldPos = uiCore.getCursorPos()
        deskRect = uiCore.getDesktopRect()
        #
        self.viewModel()._drop(worldPos, deskRect)
    #
    def currentChangedEvent(self):
        string = self.viewModel().name()
        self.parent().setChoose(string)
        #
        self.close()
    #
    def initUi(self):
        self._string = None
        #
        self._uiBackgroundRgba = 63, 63, 63, 255
        self._uiBorderRgba = 95, 95, 95, 255
        self._uiNameRgba = 223, 223, 223, 255
    #
    def viewModel(self):
        return self._viewModel
    #
    def setupUi(self):
        self._viewport = _UiChooseView(self)
        self._viewport.setContentsMargins(0, 0, 0, 0)
        self._viewport.setSpacing(2)
        self._viewport.itemClicked.connect(self.currentChangedEvent)
        #
        self._separateButton = UiIconbutton('svg_basic@svg#unpinWindow', self)
        self._separateButton.hide()
        #
        self._filterViewWidget = UiFilterEnterlabel(self)
        self._filterViewWidget.hide()
        #
        self._viewModel = uiModelBasic.UiChooseDropViewModel(self, _UiChooseItem)


#
class _UiActionItem(uiCore.QWidget):
    clicked = uiCore.uiSignal()
    itemHeight = 20
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self.initUi()
        self.setupUi()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._clickAction(event)
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setFont(self.font())
        #
        if self.itemModel().isSeparator():
            if self.itemModel()._uiNameText is not None:
                textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                painter.setBorderRgba(127, 127, 127, 255)
                painter.drawText(self.itemModel()._uiNameTextRect, textOption, self.itemModel()._uiNameText)
            painter.setBorderRgba(95, 95, 95, 255)
            painter.drawLine(self.itemModel()._basicLine)
        else:
            painter.setBackgroundRgba(self._uiBackgroundRgba)
            painter.setBorderRgba(self._uiBorderRgba)
            painter.drawRect(self.itemModel()._uiBasicRect)
            if self.itemModel().isCheckEnable() is True:
                painter.setDrawImage(
                    self.itemModel()._uiIconRect, self.itemModel()._uiCheckIcon
                )
            else:
                if self.itemModel()._uiIcon is not None:
                    painter.setDrawImage(
                        self.itemModel()._uiIconRect,
                        self.itemModel()._uiIcon
                    )
                    if self.itemModel()._uiSubIcon is not None:
                        painter.setDrawImage(
                            self.itemModel()._uiSubIconRect,
                            self.itemModel()._uiSubIcon
                        )
            #
            if self.itemModel()._uiNameText is not None:
                font = painter.font()
                font.setItalic(self._uiFontItalic)
                painter.setFont(font)
                painter.setBorderRgba(self._uiNameRgba)
                textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                painter.drawText(self.itemModel()._uiNameTextRect, textOption, self.itemModel()._uiNameText)
            if self.itemModel()._uiSubNameText is not None:
                painter.setBorderRgba(self._uiNameRgba)
                textOption = QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
                painter.drawText(self.itemModel()._uiSubNameRect, textOption, self.itemModel()._uiSubNameText)
            if self.itemModel()._uiExtendIcon is not None:
                painter.setDrawImage(
                    self.itemModel()._uiExtendRect, self.itemModel()._uiExtendIcon
                )
    #
    def setActionData(self, action):
        self.itemModel().setActionData(action)
    #
    def setPressCurrent(self, boolean):
        self.itemModel().setPressCurrent(boolean)
    #
    def isExtendEnable(self):
        return self.itemModel().isExtendEnable()
    #
    def initUi(self):
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 63, 63, 63, 255
        #
        self._uiNameRgba = 191, 191, 191, 255
        self._uiIndexRgba = 191, 191, 191, 255
        # noinspection PyArgumentEqualDefault
        self.setFont(uiCore.xFont(size=8, weight=50))
        #
        self._uiFontItalic = False
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._extendButton = UiIconbutton('svg_basic@svg#subWindow', self)
        self._extendButton.hide()
        #
        self._itemModel = uiModelBasic.UiActionItemModel(self)


#
class _UiActionDropView(uiCore.QWidget):
    actionAccepted = uiCore.uiSignal()
    #
    uiShadowRadius = 4
    #
    uiGap = 8
    uiMinWidth = 240
    uiMaxWidth = 480
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initView()
        #
        self.setupUi()
    #
    def _initView(self):
        self.setWindowFlags(QtCore.Qt.Drawer | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self._initViewAction()
        self._initViewUi()
    #
    def _initViewAction(self):
        self._altFlag, self._shiftFlag, self._ctrlFlag = False, False, False
    #
    def _initViewUi(self):
        self._uiBackgroundRgba = 63, 63, 63, 255
        self._uiBorderRgba = 95, 95, 95, 255
        #
        self._uiSeparatorBorderRgba = 95, 95, 95, 255
        self._uiNameRgba = 223, 223, 223, 255
    #
    def enterEvent(self, event):
        pass
    #
    def leaveEvent(self, event):
        self.viewModel()._clearHover()
    #
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self._ctrlFlag = True
        elif event.key() == QtCore.Qt.Key_Shift:
            self._shiftFlag = True
            self.viewModel()._updateShiftMode()
        elif event.key() == QtCore.Qt.Key_Alt:
            self._altFlag = True
        else:
            event.ignore()
    #
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self._ctrlFlag = False
        elif event.key() == QtCore.Qt.Key_Shift:
            self._shiftFlag = False
            self.viewModel()._updateShiftMode()
            self.viewModel()._shiftStopAction()
        elif event.key() == QtCore.Qt.Key_Alt:
            self._altFlag = False
        else:
            event.ignore()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStopAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.viewModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.viewModel()._pressExecuteAction(event)
            else:
                event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        # noinspection PyArgumentEqualDefault
        painter.setFont(uiCore.xFont(size=8, weight=50, family=_families[1]))
        #
        side = self.viewModel()._uiSide
        margin = self.viewModel()._uiMargin
        shadowRadius = self.viewModel()._uiShadowRadius
        #
        painter.setDrawMenuFrame(
            self.viewModel()._uiBasicRect,
            margin, side, shadowRadius, self.viewModel()._region,
            self._uiBackgroundRgba, self._uiBorderRgba
        )
        #
        if self.viewModel()._isTearable is True:
            painter.setBorderRgba(self._uiSeparatorBorderRgba)
            painter.drawLine(self.viewModel()._titleLine)
            #
            if self.viewModel()._uiNameText is not None:
                painter.setBorderRgba(self._uiNameRgba)
                textOption = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
                painter.drawText(self.viewModel()._titleRect, textOption, self.viewModel()._uiNameText)
        #
        for k, v in self.viewModel()._subRectDic.items():
            if k > 0:
                if v is not None:
                    subRect = v
                    enable = self.viewModel()._subEnableDic[k]
                    if enable is True:
                        painter.setDrawShadow(subRect, shadowRadius, shadowRadius)
                        #
                        painter.setBackgroundRgba(self._uiBackgroundRgba)
                        painter.setBorderRgba(self._uiBorderRgba)
                        painter.drawRect(subRect)
    #
    def setTitle(self, string):
        self.viewModel().setTitle(string)
    #
    def setTearable(self, boolean):
        self.viewModel().setTearable(boolean)
    #
    def setActionData(self, actions):
        self.viewModel().setActionData(actions)
    # noinspection PyUnusedLocal
    def setDrop(self, point=None):
        worldPos = uiCore.getCursorPos()
        deskRect = uiCore.getDesktopRect()
        #
        self.viewModel()._drop(worldPos, deskRect)
    #
    def viewModel(self):
        return self._viewModel
    #
    def setupUi(self):
        self._separateButton = UiIconbutton('svg_basic@svg#unpin_', self)
        self._separateButton.hide()
        #
        self._vScrollBar = None
        #
        self._viewModel = uiModelBasic.UiActionDropViewModel(self, _UiActionItem)


#
class UiAttributeItem(_UiItemBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initItemBasic()
        #
        self.__overrideItemUi()
        self.setupUi()
    #
    def __overrideItemUi(self):
        self._uiColorBackgroundRgba = 95, 95, 95, 255
        self._uiColorBorderRgba = 127, 127, 127, 255
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        # Background
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRect(self._itemModel._uiBasicRect)
        # Check
        if self._itemModel.isCheckEnable() is True:
            painter.setDrawImage(
                self._itemModel._uiCheckRect,
                self._itemModel._uiCheckIcon
            )
        # Filter Color
        if self._itemModel._isColorEnable is True:
            painter.setBackgroundRgba(self._uiColorBackgroundRgba)
            painter.setBorderRgba(self._uiColorBorderRgba)
            painter.drawEllipse(self._itemModel._uiColorRect)
        # Icon
        if self._itemModel._uiIcon is not None:
            painter.setDrawImage(
                self._itemModel._uiIconRect,
                self._itemModel._uiIcon
            )
        # Name
        if self._itemModel._uiNameText is not None:
            painter.setBorderRgba(self._uiNameRgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(uiCore.xFont(size=8, weight=50, italic=self._uiFontItalic, family=_families[0]))
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.drawText(
                self._itemModel._uiNameTextRect,
                textOption,
                self._itemModel._uiNameText
            )
    #
    def setupUi(self):
        self._itemModel = uiModelBasic.UiAttributeItemModel(self)


#
class _UiTabBasic(uiCore.QWidget):
    clicked = uiCore.uiSignal()
    currentToggled = uiCore.uiSignal(bool)
    def _initTabBasic(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self._initTabBasicUi()
    #
    def _initTabBasicUi(self):
        self._uiBackgroundRgba = 63, 63, 63, 255
        self._uiBorderRgba = 71, 71, 71, 255
        #
        self._uiNameRgba = 191, 191, 191, 255
        # noinspection PyArgumentEqualDefault
        self._uiNameTextFont = uiCore.xFont(size=8, weight=75, family=_families[1])
    @uiCore.uiTooltipStartMethod
    def enterEvent(self, event):
        self.itemModel()._hoverStartAction(event)
    @uiCore.uiTooltipStopMethod
    def leaveEvent(self, event):
        self.itemModel()._hoverStopAction(event)
    @uiCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStartAction(event)
        else:
            event.ignore()
    @uiCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.itemModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.itemModel()._pressExecuteAction(event)
            else:
                event.ignore()
    @uiCore.uiTooltipClearMethod
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.itemModel()._pressStopAction(event)
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        #
        borderWidth, borderRadius = 1, 12
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        # noinspection PyArgumentEqualDefault
        painter.setDrawTab(
            self.itemModel().basicRect(),
            borderWidth, borderRadius,
            self._uiBackgroundRgba, self._uiBorderRgba,
            tabRegion=self.itemModel().tabRegion(), tabPosition=self.itemModel().tabPosition()
        )
        #
        if self.itemModel().tabPosition() == uiCore.East:
            painter.rotate(90)
            painter.translate(0, -self.width())
        elif self.itemModel().tabPosition() == uiCore.West:
            painter.rotate(-90)
            painter.translate(-self.height(), 0)
        # Icon
        if self.itemModel().icon() is not None:
            painter.setDrawImage(
                self.itemModel().iconRect(), self.itemModel().icon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            rect = self.itemModel().nameTextRect()
            if self.itemModel().tabPosition() == uiCore.West:
                textOption = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
            else:
                textOption = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
            #
            self.setFont(self._uiNameTextFont)
            painter.setFont(self._uiNameTextFont)
            painter.setBorderRgba(self._uiNameRgba)
            painter.drawText(
                rect,
                textOption,
                self.itemModel().drawNameText()
            )
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def setIcon(self, iconKeyword, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeyword, iconWidth, iconHeight, frameWidth, frameHeight)
    #
    def setActionData(self, actionData):
        self.itemModel().setActionData(actionData)
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._menuButton = UiMenuIconbutton('svg_basic@svg#tabMenu_v', self)
        self._menuButton.setPressable(False)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._closeButton = UiIconbutton(parent=self)
        self._closeButton.hide()
        self._closeButton.setIcon('svg_basic@svg#closeTab', 8, 8, 10, 10)
        #
        self._itemModel = uiModelBasic.UiTabModel(self)


#
class UiButtonTab(_UiTabBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initTabBasic()
        #
        self.setupUi()
    #
    def setupUi(self):
        self._menuButton = UiMenuIconbutton('svg_basic@svg#menu_tab_v', self)
        self._menuButton.setPressable(False)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._closeButton = UiIconbutton(parent=self)
        self._closeButton.hide()
        self._closeButton.setIcon('svg_basic@svg#closeTab', 8, 8, 10, 10)
        #
        self._itemModel = uiModelBasic.UiButtonTabModel(self)


# Tab
class UiShelfTab(_UiTabBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initTabBasic()
        self._overrideUi()
        #
        self.setupUi()
    #
    def _overrideUi(self):
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 0, 0, 0, 0
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setFont(self.font())
        # Icon
        if self.itemModel().tabPosition() == uiCore.South or self.itemModel().tabPosition() == uiCore.North:
            if self.itemModel().nameText() is not None:
                rect = self.itemModel().nameTextRect()
                textOption = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(rect, textOption, self.itemModel().nameText())
        else:
            if self.itemModel().icon() is not None:
                painter.setDrawImage(
                    self.itemModel().iconRect(), self.itemModel().icon()
                )
    #
    def setupUi(self):
        self._menuButton = UiMenuIconbutton('svg_basic@svg#menu_d', self)
        self._menuButton.setPressable(False)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._closeButton = UiIconbutton(parent=self)
        self._closeButton.hide()
        self._closeButton.setIcon('svg_basic@svg#closeTab', 8, 8, 10, 10)
        #
        self._itemModel = uiModelBasic.UiShelfTabModel(self)


# Choose Tab
class UiChooseTab(uiCore.QWidget):
    chooseChanged = uiCore.uiSignal()
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(UiChooseTab, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initItemBasic()
        #
        self.setupUi()
    #
    def _initItemBasic(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        # noinspection PyArgumentEqualDefault
        self.setFont(uiCore.xFont(size=10, weight=50, family=_families[2]))
        #
        self._initItemUi()
    #
    def _initItemUi(self):
        self._uiDatumRgba = 191, 191, 191, 255
    #
    def paintEvent(self, event):
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        painter.setFont(self.font())
        if self.itemModel().datumText() is not None:
            rect = self.itemModel().datumRect()
            textOption = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
            painter.setBorderRgba(self._uiDatumRgba)
            painter.drawText(
                rect,
                textOption,
                self.itemModel().drawDatumText()
            )
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    @uiChooseBoxEventFilterMethod
    def eventFilter(self, *args):
        return False
    @uiChooseViewDropMethod
    def _chooseDropAction(self):
        pass
    #
    def setDatumLis(self, lis):
        self.itemModel().setDatumLis(lis)
    #
    def setExtendDatumDic(self, dic):
        self.itemModel().setExtendDatumDic(dic)
    #
    def setDefaultDatum(self, datum):
        self.itemModel().setDefaultDatum(datum)
    #
    def setChoose(self, string):
        self.itemModel().setChoose(string)
    #
    def setChooseIndex(self, index):
        self.itemModel().setChooseIndex(index)
    #
    def chooseIndex(self):
        return self.itemModel().chooseIndex()
    #
    def setChooseClear(self):
        pass
    #
    def datum(self):
        return self.itemModel().datum()
    #
    def datumText(self):
        return self.itemModel().datumText()
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._chooseButton = UiIconbutton('svg_basic@svg#choose', self)
        self._chooseButton.setTooltip(
            u'1.左键点击：查看/选择更多选项\r\n2.中键滚动：向上/向下选择'
        )
        self._chooseButton.clicked.connect(self._chooseDropAction)
        #
        self._itemModel = uiModelBasic.UiChooseTabModel(self)
        #
        self._chooseButton.upScrolled.connect(self._itemModel._chooseScrollUpAction)
        self._chooseButton.downScrolled.connect(self._itemModel._chooseScrollDownAction)


#
class _UiTabBarBasic(uiCore.QWidget):
    # Scroll
    valueChanged = uiCore.uiSignal()
    stop = uiCore.uiSignal()
    # Click
    currentChanged = uiCore.uiSignal()
    def _initTabBarBasic(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding, uiCore.QSizePolicy.Expanding
        )
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.setMouseTracking(True)
        #
        self._initTabBarBasicUi()
    #
    def _initTabBarBasicUi(self):
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 95, 95, 95, 255
        #
        self._uiTabHoverBackgroundRgba = 63, 127, 255, 255
        self._uiTabBorderRgba = 95, 95, 95, 255
        #
        self._uiScrollBackgroundRgba = 80, 80, 80, 255
        self._uiScrollBorderRgba = 95, 95, 95, 255
    #
    def enterEvent(self, event):
        self.viewModel()._hoverStartAction(event)
    #
    def leaveEvent(self, event):
        self.viewModel()._hoverStopAction(event)
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStartAction(event)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.viewModel()._pressStopAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.viewModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.viewModel()._pressExecuteAction(event)
            else:
                event.ignore()
    #
    def wheelEvent(self, event):
        self.viewModel()._wheelAction(event)
    #
    def resizeEvent(self, event):
        if self.viewModel()._isSizeChanged():
            self.viewModel().update()
    #
    def addItem(self, widget):
        self.viewModel().addItem(widget)
    #
    def setCurrentIndex(self, index):
        self.viewModel().setCurrentIndex(index)
    #
    def currentIndex(self):
        return self.viewModel().currentItemIndex()
    #
    def viewModel(self):
        return self._viewModel
    #
    def setupUi(self):
        self._viewModel = uiModelBasic.UiTabBarModel(self)


#
class _UiTabBar(_UiTabBarBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initTabBarBasic()
        #
        self.setupUi()
    #
    def setupUi(self):
        self._viewModel = uiModelBasic.UiTabBarModel(self)


# Tab View
class _UiTabGroupBasic(uiCore.QWidget):
    currentChanged = uiCore.uiSignal()
    def _initTabGroupBasic(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding, uiCore.QSizePolicy.Expanding
        )
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.setMouseTracking(True)
        #
        self._initTabGroupBasicUi()
    #
    def _initTabGroupBasicUi(self):
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 95, 95, 95, 255
    #
    def resizeEvent(self, event):
        if self.viewModel()._isSizeChanged():
            self.viewModel().update()
    #
    def showEvent(self, event):
        self.viewModel().update()
    #
    def paintEvent(self, event):
        pass
    #
    def addTab(self, widget, name=None, iconKeyword=None, tooltip=None):
        self.viewModel().addTab(widget, name, iconKeyword, tooltip)
    #
    def setTabAction(self, actionData):
        pass
    #
    def setTabPosition(self, value):
        self.viewModel().setTabPosition(value)
    #
    def tabPosition(self):
        return self.viewModel().tabPosition()
    #
    def setTabSize(self, w, h):
        self.viewModel().setTabSize(w, h)
    #
    def tabSize(self):
        return self.viewModel().tabSize()
    #
    def tabIndex(self, widget):
        return self.viewModel().tabIndex(widget)
    #
    def tabAt(self, tabIndex):
        return self.viewModel().tabAt(tabIndex)
    #
    def setCurrentIndex(self, index):
        self.viewModel().tabBar().setCurrentIndex(index)
    #
    def currentIndex(self):
        return self.viewModel().tabBar().currentIndex()
    #
    def tabBar(self):
        return self.viewModel().tabBar()
    #
    def viewModel(self):
        return self._viewModel
    #
    def _currentChangedEmit(self):
        self.currentChanged.emit()
    #
    def setupUi(self):
        self._tabBar = _UiTabBar(self)
        self._tabBar.currentChanged.connect(self._currentChangedEmit)
        #
        self._viewModel = uiModelBasic.UiTabGroupModel(self)


# Group
class _UiGroupBasic(uiCore.QWidget):
    expanded = uiCore.uiSignal()
    separated = uiCore.uiSignal()
    def _initGroupBasic(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding,
            uiCore.QSizePolicy.Fixed
        )
        #
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        #
        self._initGroupBasicUi()
    #
    def _initGroupBasicUi(self):
        self._clickFlag = True
        self._isColorEnable = True
        #
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 95, 95, 95, 255
        #
        self._uiViewportBackgroundRgba = 47, 47, 47, 63
        self._uiViewportBorderRgba = 95, 95, 95, 255
        #
        self._uiNameRgba = 191, 191, 191, 255
        #
        self._uiColorBackgroundRgba = 191, 191, 191, 255
        self._uiColorBorderRgba = 127, 127, 127, 255
        # noinspection PyArgumentEqualDefault
        self.setFont(
            uiCore.xFont(size=8, weight=75, family=_families[1])
        )
        #
        self._separatorLis = []
    @uiCore.uiTooltipStartMethod
    def enterEvent(self, event):
        self.groupModel()._hoverStartAction(event)
    @uiCore.uiTooltipStopMethod
    def leaveEvent(self, event):
        self.groupModel()._hoverStopAction(event)
    @uiCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.groupModel()._pressStartAction(event)
        else:
            event.ignore()
    @uiCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.groupModel()._pressStartAction(event)
        else:
            event.ignore()
    @uiCore.uiTooltipClearMethod
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.groupModel()._pressStopAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.groupModel()._hoverExecuteAction(event)
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.groupModel()._pressExecuteAction(event)
            else:
                event.ignore()
    #
    def resizeEvent(self, event):
        if self.groupModel()._isSizeChanged():
            self.groupModel().update()
    #
    def showEvent(self, event):
        self.groupModel().update()
    #
    def setBackground(self, image, width=20, height=20):
        self.groupModel().setImage(image)
        self.groupModel().setImageSize(width, height)
    #
    def addWidget(self, widget):
        self.groupModel().addWidget(widget)
    #
    def viewportLayout(self):
        return self.groupModel().viewportLayout()
    #
    def setNameText(self, text):
        self.groupModel().setNameText(text)
    #
    def setTitle(self, text):
        self.groupModel().setNameText(text)

    def setIndexText(self, text):
        self.groupModel().setIndexText(text)
    #
    def setTooltip(self, text):
        pass
    #
    def setFilterColor(self, rgba):
        self.groupModel().setFilterColor(rgba)
    #
    def setExpanded(self, boolean):
        self.groupModel().setExpanded(boolean)
    #
    def isExpanded(self):
        return self.groupModel().isExpanded()
    #
    def setActionData(self, actionData, title=None):
        self.groupModel().setActionData(actionData, title)
    #
    def isSeparated(self):
        return self.groupModel().isSeparated()
    #
    def groupModel(self):
        return self._groupModel
    #
    def setUiWidth(self, width):
        self.setMaximumWidth(width)
        self.setMinimumWidth(width)
    #
    def setupUi(self):
        self._menuButton = UiMenuIconbutton('svg_basic@svg#tabMenu_h', self)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        self._groupModel = uiModelBasic.UiGroupModel(self)


#
class _UiTextBrowerBasic(uiCore.QWidget):
    entryChanged = uiCore.uiSignal()
    #
    counterWidth = 32
    menuHeight = 24
    def _initItemUi(self):
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 95, 95, 95, 255
        #
        self._uiNameRgba = 191, 191, 191, 255
        self._uiIndexRgba = 95, 95, 95, 255
        #
        self._uiBorderStyle = 'solid'
        #
        self._coding = None
        #
        self._index = None
    @uiCore.uiTooltipStartMethod
    def enterEvent(self, event):
        pass
    @uiCore.uiTooltipStopMethod
    def leaveEvent(self, event):
        pass
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        def paintCounter():
            _uiYPos = yPos
            # Counter
            countOffset = self.itemModel()._countOffset
            #
            _uiYPos -= countOffset % step - 5
            #
            countOffset = int(countOffset / step)
            countRange = int(height / step) + 1
            #
            painter.setBorderRgba(self._uiIndexRgba)
            for i in range(countRange):
                lineCount = i + countOffset + 1
                if lineCount <= maximumCount:
                    countRect = QtCore.QRect(
                        xPos + leftSide, _uiYPos,
                        self.counterWidth, step
                    )
                    painter.drawText(
                        countRect,
                        QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter,
                        str(i + countOffset + 1)
                    )
                #
                _uiYPos += step
        #
        painter = uiCore.QPainter_(self)
        painter.setRenderHint(painter.Antialiasing)
        # noinspection PyArgumentEqualDefault
        painter.setFont(
            self.textEdit().font()
        )
        #
        offset = 0
        #
        topSide = 1
        #
        leftSide = 1
        rightSide = [0, 16][self.textEdit().verticalScrollBar().maximum() > 0]
        #
        xPos = offset
        yPos = offset + topSide
        #
        maximumCount = self.textEdit().document().lineCount()
        step = self.textEdit().fontMetrics().height()
        #
        width = self.width() - offset*2 - rightSide - 1
        height = self.height() - offset*2 - topSide - 1
        #
        if self.itemModel().isEnterEnable():
            borderWidth = 1
            borderRadius = 2
            # Background
            painter.setBackgroundRgba(self._uiEnterBackgroundRgba)
            if self.itemModel().isEntered():
                painter.setBackgroundRgba(self._uiEnterBackgroundRgba)
                painter.setBorderRgba(self._uiEnterBorderRgba)
                painter.setPenWidth(2)
                rect = self.itemModel().basicRect()
                painter.drawRoundedRect(
                    uiCore.QtCore.QRect(rect.topLeft().x() + 1, rect.topLeft().y() + 1, rect.width() - 2, rect.height() - 2),
                    borderRadius - 2, borderRadius - 2,
                    QtCore.Qt.AbsoluteSize
                )
            else:
                painter.setDrawButtonBasic(
                    self.itemModel().basicRect(),
                    borderWidth, borderRadius,
                    self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._uiBorderStyle
                )
        #
        paintCounter()
        # Coding
        if self.itemModel().isCodingEnable():
            if self._coding is not None:
                for seq, (k, v) in enumerate(self._coding.items()):
                    codingRect = QtCore.QRect(width - 180, height - (3-seq)*12, 180, 12)
                    painter.drawText(codingRect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, '{0} : {1}'.format(k, v))
        #
        if self._index is not None:
            selRect = QtCore.QRect(
                xPos, self._index*step,
                width, step
            )
            #
            painter.setBackgroundRgba(95, 95, 95, 255)
            painter.setBorderRgba(95, 95, 95, 255)
            painter.drawRect(selRect)
    @staticmethod
    def getHtmlTip(tipString, lineHeight=8):
        keyWord = u'「'
        nameKey = u'''“'''
        warringKey = u'！！！'
        tipLines = tipString.split('\r\n')
        htmlTipArray = []
        for tipLine in tipLines:
            subHtmlTipArray = []
            splitData = tipLine.split('#')
            for i in splitData:
                subHtmlTip = u'<span style="font-size:8pt;color:#dfdfdf;">%s</span>' % i
                if keyWord in i:
                    subHtmlTip = (u'<span style="font-size:8pt;font-weight:600;color:#00bfbf;">%s</span>' % i)
                if warringKey in i:
                    subHtmlTip = u'<span style="font-size:8pt;font-weight:600;color:#40ff7f;">%s</span>' % i
                if nameKey in i:
                    subHtmlTip = u'<span style="font-size:8pt;font-weight:600;color:#ffff40;">%s</span>' % i
                subHtmlTipArray.append(subHtmlTip.replace(u'「', u' ').replace(u'」', u' '))
            htmlTip = u'<p>' + u''.join(subHtmlTipArray) + u'</p>'
            htmlTipArray.append(htmlTip)
        tipReduce = (u'''<html><style>p{line-height:%ipx}</style>''' % lineHeight) + u''.join(htmlTipArray) + u'''</html>'''
        return tipReduce
    #
    def setTooltip(self, text):
        self.uiTip = text
    #
    def textEdit(self):
        return self._textEdit
    #
    def setRule(self, html):
        if isinstance(html, list):
            self.textEdit().setText('\r\n'.join(html))
        else:
            self.textEdit().setHtml(self.getHtmlTip(html))
            #
            if self.datum():
                print '['
                for i in self.datum().split('\n'):
                    print u'''u"{}",'''.format(i)
                print ']'
    #
    def setText(self, datum):
        self.setDatum(datum)
    #
    def text(self):
        return self.textEdit().toPlainText()
    #
    def setNameText(self, string):
        self.itemModel().setNameText(string)
    #
    def nameText(self):
        return self.itemModel().nameText()
    #
    def setDatum(self, datum):
        if datum is not None:
            if isinstance(datum, str):
                self._coding = chardet.detect(datum)
            elif isinstance(datum, unicode):
                datum = datum.encode('utf-8')
                self._coding = chardet.detect(datum)
            #
            self.textEdit().setText(datum)
        #
        self.update()
    #
    def datum(self):
        return self.textEdit().toPlainText()
    #
    def setEnterEnable(self, boolean):
        self.itemModel().setEnterEnable(boolean)
        self.textEdit().setReadOnly(not boolean)
    #
    def setClear(self):
        self.textEdit().setPlainText('')
    #
    def setEnterClear(self):
        self.itemModel().setEnterClear()
    #
    def _entryChangedEmit(self):
        self.entryChanged.emit()
        self.itemModel()._updateCounter()
    #
    def setUiSize(self):
        self.setMaximumSize(QtCore.QSize(166667, 166667))
        self.setMinimumSize(QtCore.QSize(0, 0))
    #
    def itemModel(self):
        return self._itemModel
    #
    def setFontSize(self, value):
        self.textEdit().setFont(
            uiCore.xFont(size=value, family=_families[1])
        )
    #
    def setupUi(self):
        self._textEdit = QTextEdit_(self)
        self._textEdit.setParent(self)
        self._textEdit.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self._textEdit.setLineWrapMode(uiCore.QTextEdit.NoWrap)
        self._textEdit.setLineWrapColumnOrWidth(0)
        # noinspection PyArgumentEqualDefault
        self._textEdit.setFont(
            uiCore.xFont(size=8, family=_families[1])
        )
        #
        self._itemModel = uiModelBasic.UiTextBrowerItemModel(self)
        #
        self._textEdit.focusChanged.connect(self.itemModel()._updateUiEnterState)
        self._textEdit.entryChanged.connect(self._entryChangedEmit)
        #
        self._textEdit.verticalScrollBar().valueChanged.connect(self.itemModel()._updateCounter)


#
class UiTextBrower(_UiTextBrowerBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(uiCore.QWidget, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initItemUi()
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setSizePolicy(
            uiCore.QSizePolicy.Expanding,
            uiCore.QSizePolicy.Expanding
        )
        #
        self.setupUi()
        #
        self.setUiSize()