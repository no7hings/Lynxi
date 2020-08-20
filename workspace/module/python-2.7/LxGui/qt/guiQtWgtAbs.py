# coding:utf-8
import chardet

from LxBasic import bscMethods

from LxScheme import shmOutput
#
from LxGui import guiCore
#
from LxGui.qt import qtCore, guiQtMdlAbs
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
_families = guiCore.Lynxi_Ui_Family_Lis
#
none = ''


# Item
class AbsGuiQtItemWgt(qtCore.QWidget):
    CLS_gui_qt__item_wgt__model = None

    toggled = qtCore.qtSignal(bool)
    clicked = qtCore.qtSignal()
    doubleClicked = qtCore.qtSignal()
    #
    expanded = qtCore.qtSignal()
    checked = qtCore.qtSignal()
    #
    pressed = qtCore.qtSignal()
    released = qtCore.qtSignal()
    #
    visibleToggled = qtCore.qtSignal(bool)
    def _initAbsGuiQtItemWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self.setFocusPolicy(qtCore.QtCore.Qt.NoFocus)
        #
        self._initAbsGuiQtItemWgtAttr()
        self._initAbsGuiQtItemWgtUi()
    #
    def _initAbsGuiQtItemWgtAttr(self):
        self.actionTitle = None
        self.actionData = []
    #
    def _initAbsGuiQtItemWgtUi(self):
        self._uiFont = qtCore.qtFont()
        self.setFont(self._uiFont)
        #
        self._uiFontItalic = False
        self._uiFontStrikeOut = False
        #
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 0, 0, 0, 0
        #
        self._uiPercentValueRgba = 47, 47, 47, 255
        #
        self._uiIndexRgba = 127, 127, 127, 255
        self._wgt__name_rgba = 191, 191, 191, 255
        self._uiSubNameColor = 191, 191, 191, 255
        #
        self._uiNamespaceRgba = 95, 95, 95, 255
        #
        self._uiDatumRgba = 191, 191, 191, 255
        #
        self._wgt__color__background_rgba = 71, 71, 71, 255
        self._wgt__color__border_rgba = 127, 127, 127, 255
        #
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 127, 127, 127, 255
        #
        self._wgt__menu__background_rgba = 0, 0, 0, 0
        self._wgt__menu__border_rgba = 0, 0, 0, 0
        #
        self._uiCentralBackgroundRgba = 71, 71, 71, 255
        self._uiCentralBorderRgba = 95, 95, 95, 255
        #
        self._wgt__border_style = 'outset'

    @qtCore.gui_qt_mdf__set_tooltip_start
    def enterEvent(self, event):
        self.itemModel()._gui_qt__set_enter_event_update_(event)

    @qtCore.gui_qt_mdf__set_tooltip_stop
    def leaveEvent(self, event):
        self.itemModel()._gui_qt__set_leave_event_update_(event)

    @qtCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()

    @qtCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()

    @qtCore.uiTooltipClearMethod
    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.itemModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.itemModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
            else:
                event.ignore()
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # Background
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        painter.drawRect(self.itemModel()._uiBasicRect)
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter._gui_qt__set_image_draw_(
                self.itemModel()._uiCheckRect, self.itemModel()._uiCheckIcon
            )
        # Filter Color
        if self.itemModel()._isColorEnable is True:
            painter.setBackgroundRgba(self._wgt__color__background_rgba)
            painter.setBorderRgba(self._wgt__color__border_rgba)
            painter.drawRect(self.itemModel()._uiColorRect)
        # Expand
        if self.itemModel().isExpandable() is True:
            painter._gui_qt__set_image_draw_(
                self.itemModel()._uiExpandRect,
                self.itemModel()._uiExpandIcon
            )
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(), self.itemModel().icon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            rect = self.itemModel()._gui_qt__mdl__name_str_Rect
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            if self.itemModel()._filterKeyword is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    self.itemModel()._gui_qt__mdl__name_str_, self.itemModel()._filterKeyword,
                    self._wgt__name_rgba
                )
            else:
                painter.setBorderRgba(self._wgt__name_rgba)
                painter.drawText(rect, textOption, self.itemModel()._gui_qt__mdl__name_str_)
        # Index
        if self.itemModel()._gui_qt__mdl__index_str_ is not None:
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(
                self.itemModel()._gui_qt__mdl__index_str_Rect,
                qtCore.QtCore.Qt.AlignRight | qtCore.QtCore.Qt.AlignVCenter,
                str(self.itemModel()._gui_qt__mdl__index_str_)
            )

        # painter.end()  # for pyside2
    #
    def setIndex(self, number):
        self.itemModel().setIndex(number)
    #
    def index(self):
        return self.itemModel().index()
    #
    def setIndexString(self, number):
        self.itemModel().setIndexString(number)
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
    def setIconKeyword(self, iconKeywordStr):
        self.itemModel().setIconKeyword(iconKeywordStr)
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
    #
    def setIconText(self, text):
        self.itemModel().setIconText(text)
    #
    def iconText(self):
        return self.itemModel().iconText()
    #
    def setSubIcon(self, iconKeywordStr):
        self.itemModel().setSubIcon(iconKeywordStr)
    #
    def setNameString(self, string):
        self.itemModel().setNameString(string)
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
    def _setQtPressStyle(self, state):
        self.itemModel()._setQtPressStyle(state)
    #
    def _setQtPressStatus(self, status):
        self.itemModel()._setQtPressStatus(status)
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._itemModel = self.CLS_gui_qt__item_wgt__model(self)


# Tree Item
class AbsGuiQtTreeitemWgt(AbsGuiQtItemWgt):
    def _initAbsGuiQtTreeitemWgt(self):
        self._initAbsGuiQtItemWgt()
        self.setupUi()
    # noinspection PyArgumentList
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            if self.itemModel()._isPressable:
                self.clicked.emit()
            #
            event.ignore()
        elif event.button() == qtCore.QtCore.Qt.RightButton:
            if self.actionData:
                self._menuDropAction()
            #
            event.accept()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # Background
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        painter.drawRect(self.itemModel()._uiBasicRect)
        # Check
        if self.itemModel().isCheckEnable():
            painter._gui_qt__set_image_draw_(self.itemModel()._uiCheckRect, self.itemModel()._uiCheckIcon)
        # Filter Color
        if self.itemModel().isColorEnable():
            painter.setBackgroundRgba(self._wgt__color__background_rgba)
            painter.setBorderRgba(self._wgt__color__border_rgba)
            painter.drawRect(self.itemModel()._uiColorRect)
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
            if self.itemModel().subIcon() is not None:
                painter._gui_qt__set_image_draw_(
                    self.itemModel().subIconRect(),
                    self.itemModel().subIcon()
                )
        # Menu
        if self.itemModel().isPressMenuEnable():
            painter._gui_qt__set_image_draw_(
                self.itemModel().menuIconRect(),
                self.itemModel().menuIcon()
            )
        # Namespace
        if self.itemModel().namespaceText() is not None:
            painter.setBorderRgba(self._uiNamespaceRgba)
            rect = self.itemModel()._uiNamespaceRect
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
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
            rect = self.itemModel()._gui_qt__mdl__name_str_Rect
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            string = self.itemModel().drawNameText()
            if self.itemModel()._filterKeyword is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    string, self.itemModel()._filterKeyword,
                    self._wgt__name_rgba
                )
            else:
                painter.setBorderRgba(self._wgt__name_rgba)
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
                qtCore.QtCore.Qt.AlignRight | qtCore.QtCore.Qt.AlignVCenter,
                str(self.itemModel().indexText())
            )

        # painter.end()  # for pyside2
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


# Icon Button
class AbsGuiQtQtIconbuttonWgt(AbsGuiQtItemWgt):
    upScrolled = qtCore.qtSignal()
    downScrolled = qtCore.qtSignal()

    def _initAbsGuiQtQtIconbuttonWgt(self, iconKeywordStr=None):
        self._initAbsGuiQtItemWgt()

        self._initUiVar()

        self.setupUi()
        if iconKeywordStr is not None:
            self.setIcon(iconKeywordStr)

        self.setUiSize()

    @qtCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
            #
            self._toolActionDropAction()
        else:
            event.ignore()

    @qtCore.uiTooltipClearMethod
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
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHint(painter.SmoothPixmapTransform)
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
            if self.itemModel().subIcon() is not None:
                painter._gui_qt__set_image_draw_(
                    self.itemModel().subIconRect(),
                    self.itemModel().subIcon()
                )
        # Extend Icon
        if self.itemModel().extendIcon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().extendIconRect(),
                self.itemModel().extendIcon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBackgroundRgba(self._wgt__background_rgba)
            painter.setBorderRgba(self._wgt__name_rgba)
            #
            font = self.font()
            font.setItalic(self._uiFontItalic)
            painter.setFont(
                font
            )
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel()._gui_qt__mdl__name_str_Rect,
                textOption,
                self.itemModel().nameText()
            )

        # painter.end()  # for pyside2
    #
    def setActionData(self, actionData):
        self.actionData = actionData
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
        self.setUiSize()
    #
    def setExtendIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setExtendIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
    #
    def setNameString(self, string):
        self.itemModel().setNameString(string)
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

    def _initUiVar(self):
        self.actionData = []


class AbsGuiQtIconViewitemWgt(AbsGuiQtItemWgt):
    upScrolled = qtCore.qtSignal()
    downScrolled = qtCore.qtSignal()

    def _initAbsGuiQtIconViewitemWgt(self, iconKeywordStr=None):
        self._initAbsGuiQtItemWgt()

        self._initUiVar()

        self.setupUi()
        if iconKeywordStr is not None:
            self.setIcon(iconKeywordStr)

        self.setUiSize()

    @qtCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
            #
            self._toolActionDropAction()
        else:
            event.ignore()

    @qtCore.uiTooltipClearMethod
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
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHint(painter.SmoothPixmapTransform)
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(),
                self.itemModel().icon(),
                self.itemModel().isPressHovered()
            )
            if self.itemModel().subIcon() is not None:
                painter._gui_qt__set_image_draw_(
                    self.itemModel().subIconRect(),
                    self.itemModel().subIcon()
                )
        # Extend Icon
        if self.itemModel().extendIcon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().extendIconRect(),
                self.itemModel().extendIcon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBackgroundRgba(self._wgt__background_rgba)
            painter.setBorderRgba(self._wgt__name_rgba)
            #
            font = self.font()
            font.setItalic(self._uiFontItalic)
            painter.setFont(
                font
            )
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel()._gui_qt__mdl__name_str_Rect,
                textOption,
                self.itemModel().nameText()
            )

        # painter.end()  # for pyside2
    #
    def setActionData(self, actionData):
        self.actionData = actionData
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
        self.setUiSize()
    #
    def setExtendIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setExtendIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
    #
    def setNameString(self, string):
        self.itemModel().setNameString(string)
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

    def _initUiVar(self):
        self.actionData = []


# Action Icon Button
class AbsGuiQtActionIconbuttonWgt(AbsGuiQtItemWgt):
    def _initAbsGuiQtActionIconbuttonWgt(self, iconKeywordStr=None):
        # self.setSizePolicy(qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Preferred)
        self._initAbsGuiQtItemWgt()

        self._initUiVar()

        self.setupUi()

        if iconKeywordStr:
            self.setIcon(iconKeywordStr)

        self.setUiSize()

    @qtCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
            #
            self._toolActionDropAction()
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        painter.setBorderRgba(self._wgt__border_rgba)
        painter.setBackgroundRgba(self._wgt__background_rgba)
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
            if self.itemModel().subIcon() is not None:
                painter._gui_qt__set_image_draw_(
                    self.itemModel().subIconRect(),
                    self.itemModel().subIcon()
                )
            if self.itemModel().extendIcon() is not None:
                painter._gui_qt__set_image_draw_(
                    self.itemModel().extendIconRect(),
                    self.itemModel().extendIcon()
                )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBorderRgba(self._wgt__name_rgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(qtCore.qtFont(size=8, weight=50, italic=self._uiFontItalic, family=_families[0]))
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel().nameTextRect(),
                textOption,
                self.itemModel().nameText()
            )

        # painter.end()  # for pyside2
    #
    def setActionData(self, actionData):
        self.actionData = actionData
        #
        self._updatePressable()
    #
    def _updatePressable(self):
        self.setPressable(self.actionData != [])
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
        #
        self._updatePressable()
        self.setUiSize()
    #
    def setExtendIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setExtendIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
    #
    def setNameString(self, string):
        self.itemModel().setNameString(string)
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

    def _initUiVar(self):
        self.actionData = []


# Enter Label
class AbsGuiQtValueLineWgt(AbsGuiQtItemWgt):
    CLS_gui_qt__value_line_wgt__line_edit = None
    CLS_gui_qt__value_line_wgt__iconbutton = None

    entryChanged = qtCore.qtSignal()
    chooseChanged = qtCore.qtSignal()
    checkChanged = qtCore.qtSignal()
    #
    datumChanged = qtCore.qtSignal()

    def _initAbsGuiQtValueLineWgt(self):
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Minimum
        )
        self.setMouseTracking(True)

        self._initAbsGuiQtItemWgt()
        self._initAbsGuiQtValueLineWgtAttr()
        self._initAbsGuiQtValueLineWgtUi()

        self.setupUi()

        self.setUiSize()

    def _initAbsGuiQtValueBoxWgt(self):
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding
        )
        self.setMouseTracking(True)

        self._initAbsGuiQtItemWgt()
        self._initAbsGuiQtValueLineWgtAttr()
        self._initAbsGuiQtValueLineWgtUi()

        self._wordWarp = True

        self.setupUi()
    #
    def _initAbsGuiQtValueLineWgtAttr(self):
        self._wordWarp = False
    #
    def _initAbsGuiQtValueLineWgtUi(self):
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 95, 95, 95, 255
        #
        self._wgt__name_rgba = 191, 191, 191, 255
        #
        self._wgt__border_style = 'solid'
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        painter.setRenderHint(painter.Antialiasing)
        painter.setFont(self.font())
        # Name
        if self.itemModel().nameText() is not None:
            rect = self.itemModel()._gui_qt__mdl__name_str_Rect
            textOption = qtCore.QtCore.Qt.AlignRight | qtCore.QtCore.Qt.AlignVCenter
            if self.itemModel()._filterKeyword is not None:
                painter.setDrawFilterString(
                    rect,
                    True,
                    self.itemModel().nameText() + ' : ', self.itemModel()._filterKeyword,
                    self._wgt__name_rgba
                )
            else:
                painter.setBorderRgba(self._wgt__name_rgba)
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
                    self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._wgt__border_style
                )
            else:
                painter.setDrawButtonBasic(
                    self.itemModel().basicRect(),
                    borderWidth, borderRadius,
                    self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._wgt__border_style
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
                    textOption = QtGui.QTextOption(qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignTop)
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
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            painter.setBorderRgba(self._uiIndexRgba)
            text = '{}/{}'.format(self.itemModel().chooseIndex() + 1, self.itemModel().chooseCount())
            painter.drawText(
                rect,
                textOption,
                text
            )
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter._gui_qt__set_image_draw_(
                self.itemModel()._uiCheckRect, self.itemModel()._uiCheckIcon
            )

        # painter.end()  # for pyside2
    #
    def setNameString(self, string):
        self.itemModel().setNameString(string)
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
        clipboard = qtCore.QApplication.clipboard()
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
    def _setQtPressStyle(self, state):
        self.itemModel()._setQtPressStyle(state)
    #
    def setUiSize(self):
        # noinspection PyArgumentList
        self.setMaximumSize(166667, 20)
        # noinspection PyArgumentList
        self.setMinimumSize(0, 20)
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._chooseButton = self.CLS_gui_qt__value_line_wgt__iconbutton('svg_basic/choose', self)
        self._chooseButton.clicked.connect(self._chooseDropAction)
        self._chooseButton.setTooltip(
            u'1.左键点击：查看/选择更多选项\r\n2.中键滚动：向上/向下选择'
        )
        #
        self._entryButton = self.CLS_gui_qt__value_line_wgt__iconbutton('svg_basic/edit', self)
        self._entryButton.setTooltip(
            u'点击启用/关闭输入锁定'
        )
        #
        self._enterWidget = self.CLS_gui_qt__value_line_wgt__line_edit(self)
        self._enterWidget.setParent(self)
        self._enterWidget.setReadOnly(True)
        self._enterWidget.setAlignment(qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter)
        # noinspection PyArgumentEqualDefault
        self._enterWidget.setFont(
            self.font()
        )
        self._enterWidget.entryChanged.connect(self.entryEvent)
        # Copy
        self._copyButton = self.CLS_gui_qt__value_line_wgt__iconbutton('svg_basic/copy')
        self._copyButton.setParent(self)
        self._copyButton.hide()
        self._copyButton.setTooltip(
            u'点击复制输入'
        )
        self._copyButton.clicked.connect(self.setEntryCopy)
        # Clear
        self._clearButton = self.CLS_gui_qt__value_line_wgt__iconbutton('svg_basic/clear')
        self._clearButton.setParent(self)
        self._clearButton.clicked.connect(self.entryEvent)
        #
        self._itemModel = self.CLS_gui_qt__item_wgt__model(self)
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


# Attribute Item
class _QtAttributeitem(AbsGuiQtItemWgt):
    CLS_gui_qt__item_wgt__model = guiQtMdlAbs._QtAttributeitemModel

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(_QtAttributeitem, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtItemWgt()
        #
        self.__overrideItemUi()
        self.setupUi()
    #
    def __overrideItemUi(self):
        self._wgt__color__background_rgba = 95, 95, 95, 255
        self._wgt__color__border_rgba = 127, 127, 127, 255
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        painter.setRenderHint(painter.Antialiasing)
        # Background
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        painter.drawRect(self._itemModel._uiBasicRect)
        # Check
        if self._itemModel.isCheckEnable() is True:
            painter._gui_qt__set_image_draw_(
                self._itemModel._uiCheckRect,
                self._itemModel._uiCheckIcon
            )
        # Filter Color
        if self._itemModel._isColorEnable is True:
            painter.setBackgroundRgba(self._wgt__color__background_rgba)
            painter.setBorderRgba(self._wgt__color__border_rgba)
            painter.drawEllipse(self._itemModel._uiColorRect)
        # Icon
        if self._itemModel._uiIcon is not None:
            painter._gui_qt__set_image_draw_(
                self._itemModel._uiIconRect,
                self._itemModel._uiIcon
            )
        # Name
        if self._itemModel._gui_qt__mdl__name_str_ is not None:
            painter.setBorderRgba(self._wgt__name_rgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(qtCore.qtFont(size=8, weight=50, italic=self._uiFontItalic, family=_families[0]))
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            painter.drawText(
                self._itemModel._gui_qt__mdl__name_str_Rect,
                textOption,
                self._itemModel._gui_qt__mdl__name_str_
            )

        # painter.end()  # for pyside2


# View
class AbsGuiQtViewWgt(qtCore.QWidget):
    CLS_gui_qt__view_wgt__model = None

    CLS_gui_qt__view_wgt__scrollbar = None

    clicked = qtCore.qtSignal()
    itemClicked = qtCore.qtSignal()
    currentChanged = qtCore.qtSignal()
    selectedChanged = qtCore.qtSignal()
    #
    itemExpanded = qtCore.qtSignal()
    itemChecked = qtCore.qtSignal()
    def _initAbsGuiQtViewWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding
        )
        #
        self.setFocusPolicy(qtCore.QtCore.Qt.ClickFocus)
        #
        self._initAbsGuiQtViewWgtAttr()
        self._initAbsGuiQtViewWgtDraw()
    #
    def _initAbsGuiQtViewWgtAttr(self):
        self.actionTitle = None
        self.actionData = []
        self._uiPreActions = []
        #
        self._vTempScrollPercent = 0
    #
    def _initAbsGuiQtViewWgtDraw(self):
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 63, 127, 255, 255
        #
        self._uiWidthRound, self._uiHeightRound = 5, 5
    #
    def enterEvent(self, event):
        self.viewModel()._gui_qt__set_enter_event_update_(event)
    #
    def leaveEvent(self, event):
        self.viewModel()._gui_qt__set_leave_event_update_(event)
    #
    def keyPressEvent(self, event):
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(True)
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(True)
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(True)
        # Focus
        elif event.key() == qtCore.QtCore.Qt.Key_F:
            self.viewModel().setCurrentVisibleCeiling()
        # Column Move
        elif event.key() == qtCore.QtCore.Qt.Key_Left:
            self.viewModel()._columnTraceAction(-1)
        elif event.key() == qtCore.QtCore.Qt.Key_Right:
            self.viewModel()._columnTraceAction(+1)
        # Row Move
        elif event.key() == qtCore.QtCore.Qt.Key_Up:
            self.viewModel()._rowTraceAction(-1)
        elif event.key() == qtCore.QtCore.Qt.Key_Down:
            self.viewModel()._rowTraceAction(+1)
    #
    def keyReleaseEvent(self, event):
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(False)
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(False)
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(False)
        else:
            event.ignore()
    #
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        elif event.button() == qtCore.QtCore.Qt.MidButton:
            self.setCursor(qtCore.QtCore.Qt.OpenHandCursor)
            #
            self.viewModel()._trackStartAction(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
        elif event.button() == qtCore.QtCore.Qt.MidButton:
            self.setCursor(qtCore.QtCore.Qt.ArrowCursor)
            #
            self.viewModel()._trackStopAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.viewModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.viewModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
            elif event.buttons() == qtCore.QtCore.Qt.MidButton:
                self.setCursor(qtCore.QtCore.Qt.ClosedHandCursor)
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
    def setWidgetMargins(self, *args):
        self.viewModel().setWidgetMargins(*args)
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

    def addWidget(self, widget):
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
    def setKeywordFilterWidgetConnect(self, widget):
        self.viewModel().setKeywordFilterWidgetConnect(widget)
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
        self._viewModel = self.CLS_gui_qt__view_wgt__model(self)


# window
class AbsGuiQtWindowWgt(qtCore.QWidget):
    CLS_gui_qt__window_wgt__model = None
    CLS_gui_qt__window_wgt__iconbutton = None
    CLS_gui_qt__window_wgt__action_iconbutton = None

    VAR_gui_qt__window_wgt__title = None

    closed = qtCore.qtSignal()
    confirmClicked = qtCore.qtSignal()

    def _initAbsGuiQtWindowWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        self.setFocusPolicy(qtCore.QtCore.Qt.NoFocus)
        self.setMouseTracking(True)
        #
        self._initAbsGuiQtWindowWgtAttr()
        self._initAbsGuiQtWindowWgtUi()
    #
    def _initAbsGuiQtWindowWgtAttr(self):
        pass
    #
    def _initAbsGuiQtWindowWgtUi(self):
        self._uiIndexRgba = 95, 95, 95, 255
        self._wgt__name_rgba = 223, 223, 223, 255
        self._uiSubNameColor = 223, 223, 223, 255
        #
        self._wgt__background_rgba = 63, 63, 63, 255
        self._wgt__border_rgba = 95, 95, 95, 255
        #
        self._wgt__menu__background_rgba = 63, 63, 63, 255
        self._wgt__menu__border_rgba = 95, 95, 95, 255
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
        self.setFont(qtCore.qtFont(
            size=12, weight=75, family=_families[1])
        )
        # noinspection PyArgumentEqualDefault
        self._wgt__index_font = qtCore.qtFont(
            size=8, weight=50, family=_families[0]
        )
        #
        self._gui_qt___gui_qt__wgt__name_font = qtCore.qtFont(
            size=12, weight=75, family=_families[1]
        )
        # noinspection PyArgumentEqualDefault
        self._gui_qt___gui_qt__wgt__help_font = qtCore.qtFont(
            size=8, weight=50, family=_families[0]
        )
    #
    def enterEvent(self, event):
        self.windowModel()._gui_qt__set_enter_event_update_(event)
    #
    def leaveEvent(self, event):
        self.windowModel()._gui_qt__set_leave_event_update_(event)
    #
    def keyPressEvent(self, event):
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            self.windowModel()._setCtrlFlag(True)
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            self.windowModel()._setShiftFlag(True)
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            self.windowModel()._setAltFlag(True)
    #
    def keyReleaseEvent(self, event):
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            self.windowModel()._setCtrlFlag(False)
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            self.windowModel()._setShiftFlag(False)
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            self.windowModel()._setAltFlag(False)
        else:
            event.ignore()
    #
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.windowModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.windowModel()._gui_qt__mdl__set_mouse_press_event_update_(event, isDoubleClick=True)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.windowModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.windowModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
            if self.windowModel().isResizeable():
                if self.windowModel().basicRect().contains(event.pos()) is False:
                    if self.windowModel()._win_resize_region in [0, 4]:
                        self.setCursor(qtCore.QtCore.Qt.SizeFDiagCursor)
                    elif self.windowModel()._win_resize_region in [1, 5]:
                        self.setCursor(qtCore.QtCore.Qt.SizeVerCursor)
                    elif self.windowModel()._win_resize_region in [2, 6]:
                        self.setCursor(qtCore.QtCore.Qt.SizeBDiagCursor)
                    elif self.windowModel()._win_resize_region in [3, 7]:
                        self.setCursor(qtCore.QtCore.Qt.SizeHorCursor)
                    else:
                        self.setCursor(qtCore.QtCore.Qt.ArrowCursor)
                else:
                    self.setCursor(qtCore.QtCore.Qt.ArrowCursor)
            else:
                self.setCursor(qtCore.QtCore.Qt.ArrowCursor)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.windowModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
            else:
                event.ignore()
    #
    def resizeEvent(self, event):
        self.windowModel().update()
    #
    def showEvent(self, event):
        self.windowModel()._updateWidgetSize()
        #
        self.windowModel().update()
    #
    def showMinimized(self):
        qtCore.QMainWindow.showMinimized(self)
    #
    def showMaximized(self):
        qtCore.QMainWindow.showMaximized(self)
    #
    def showNormal(self):
        qtCore.QMainWindow.showNormal(self)
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        if self.isShadowEnable() is True:
            if self.isMaximized() is False:
                painter.setDrawShadow(
                    self.windowModel()._uiBasicRect,
                    self.windowModel()._uiShadowRadius, self.windowModel()._uiShadowRadius
                )
        if self.windowModel().isWindowActive() is True:
            frameBorderRgba = 63, 127, 255, 255
        elif self.windowModel().isExpanded() is False:
            frameBorderRgba = 255, 0, 63, 255
        else:
            frameBorderRgba = self._wgt__border_rgba
        # Background
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(frameBorderRgba)
        painter.drawRect(self.windowModel().basicRect())
        #
        if self.windowModel().isExpanded() and self.isMenuEnable():
            painter.setBackgroundRgba(frameBorderRgba)
            #
            painter.setBorderRgba(frameBorderRgba)
            painter.drawPath(self.windowModel()._uiFocusPath)
        #
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        # Placeholder
        if self.windowModel().isPlaceholderEnable():
            painter._gui_qt__set_image_draw_(
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
                textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
                painter.setFont(self._gui_qt___gui_qt__wgt__help_font)
                painter.setBorderRgba(self._wgt__name_rgba)
                painter.drawText(self.windowModel().statusTextRect(), textOption, self.windowModel().statusText())
        #
        if self.windowModel().isPercentEnable():
            if self.windowModel().layoutDirection() is qtCore.Horizontal:
                gradient = QtGui.QLinearGradient(self.windowModel()._uiPercentValueRect.topLeft(), self.windowModel()._uiPercentValueRect.topRight())
            else:
                gradient = QtGui.QLinearGradient(self.windowModel()._uiPercentValueRect.topRight(), self.windowModel()._uiPercentValueRect.bottomRight())
            #
            rect = self.windowModel()._uiPercentValueRect
            w = rect.width()
            gradient.setColorAt(0, qtCore.CLS_color(*self._uiProgressStartBackgroundRgba))
            gradient.setColorAt(
                bscMethods.Value.mapTo(
                    value=max(16, w - 16),
                    sourceValueRange=(0, w), targetValueRange=(0, 1.0)
                ),
                qtCore.CLS_color(*self._uiProgressStartBackgroundRgba)
            )
            gradient.setColorAt(1, qtCore.CLS_color(*self._uiProgressEndBackgroundRgba))
            brush = qtCore.CLS_brush(gradient)
            painter.setBrush(brush)
            painter.setBorderRgba(self._uiProgressBorderRgba)
            painter.drawRect(rect)
        #
        if self.windowModel().isResizeable():
            painter._gui_qt__set_image_draw_(
                self.windowModel()._uiResizeRect,
                self.windowModel()._uiResizeIcon
            )
        # Menu
        if self.windowModel().isMenuEnable():
            if self.windowModel().isExpanded():
                painter.setBackgroundRgba(self._wgt__menu__background_rgba)
                painter.setBorderRgba(self._wgt__menu__border_rgba)
                rect = self.windowModel().menuRect()
                if self.windowModel().layoutDirection() is qtCore.Horizontal:
                    p0, p1 = rect.bottomLeft(), rect.bottomRight()
                    painter.drawLine(rect.bottomLeft(), rect.bottomRight())
                elif self.windowModel().layoutDirection() is qtCore.Vertical:
                    p0, p1 = rect.topLeft(), rect.bottomLeft()
                else:
                    raise
                #
                painter.drawLine(p0, p1)
            #
            if self.windowModel().layoutDirection() is qtCore.Horizontal:
                pass
            elif self.windowModel().layoutDirection() is qtCore.Vertical:
                painter.translate(self.windowModel()._xTranslate, self.windowModel()._yTranslate)
                painter.rotate(-90)
            # Icon
            if self.windowModel().icon() is not None:
                painter._gui_qt__set_image_draw_(
                    self.windowModel().iconRect(),
                    self.windowModel().icon()
                )
            # Name
            if self.windowModel().nameText() is not None:
                rect = self.windowModel().nameTextRect()
                painter.setBorderRgba(self._wgt__name_rgba)
                painter.setFont(self._gui_qt___gui_qt__wgt__name_font)
                textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
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
                painter.setFont(self._wgt__index_font)
                textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
                string = self.windowModel().indexText()
                painter.drawText(
                    rect,
                    textOption,
                    string
                )
        # resize
        if self.windowModel().isResizeable():
            resizeRegion = self.windowModel()._win_resize_region
            if resizeRegion is not None:
                rect = self.windowModel()._win_resize_rect_list[resizeRegion]
                painter.setBackgroundRgba(
                    255, 0, 63, 255
                )
                painter.setBorderRgba(
                    255, 255, 255, 255
                )
                painter.drawRect(
                    rect
                )
        # painter.end()  # for pyside2
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

    def winEvent(self, message):
        def getParamX(param):
            return param & 0xffff

        def getParamY(param):
            return param >> 16

        ui = self
        pixel = 8
        width = ui.width()
        height = ui.height()
        if message.message == 0x84:
            xPos = getParamX(message.lParam) - ui.frameGeometry().x()
            yPos = getParamY(message.lParam) - ui.frameGeometry().y()
            if xPos < pixel and pixel < yPos < (height - pixel):
                return True, 10
            if (width - pixel) < xPos < (width + pixel) and pixel < yPos < (height - pixel):
                return True, 11
            if pixel < xPos < (width - pixel) and yPos < pixel:
                return True, 12
            if xPos < pixel and yPos < pixel:
                return True, 13
            if (width - pixel) < xPos < (width + pixel) and yPos < pixel:
                return True, 14
            if pixel < xPos < (width - pixel) and (height - pixel) < yPos < (height + pixel):
                return True, 15
            if xPos < pixel and (height - pixel) < yPos:
                return True, 0x10
            if (width - pixel) < xPos and (height - pixel) < yPos:
                return True, 17
        return False, 0
    #
    def confirmAction(self):
        self.confirmClicked.emit()
    #
    def setDefaultSize(self, width, height):
        self.windowModel().setDefaultSize(width, height)
    #
    def setIndexString(self, number):
        self.windowModel().setIndexString(number)
    #
    def setVersion(self, number):
        self.setIndexString(number)
    #
    def setIcon(self, iconKeywordStr, iconWidth=24, iconHeight=24):
        self.windowModel().setIcon(iconKeywordStr, iconWidth, iconHeight)
        #
        iconFile = qtCore._toLxOsIconFile(iconKeywordStr)
        pixmap = QtGui.QPixmap(iconFile)
        #
        icon = QtGui.QIcon()
        icon.addPixmap(
            pixmap,
            QtGui.QIcon.Normal,
            QtGui.QIcon.On)
        #
        self.setWindowIcon(icon)

    def setNameString(self, string):
        self.windowModel().setNameString(string)

        self.setWindowTitle(string)

    def nameText(self):
        return self.windowModel().nameText()

    def setTitle(self, string):
        self.setNameString(string)

    def setWidgetMargins(self, *args):
        self.windowModel().setViewportLayoutMargins(*args)

    def setSpacing(self, value):
        self.windowModel().setSpacing(value)

    def setMenuEnable(self, boolean):
        self.windowModel().setMenuEnable(boolean)

    def isMenuEnable(self):
        return self.windowModel().isMenuEnable()

    def setStatusEnable(self, boolean):
        self.windowModel().setStatusEnable(boolean)

    def setDialogEnable(self, boolean):
        self.windowModel().setDialogEnable(boolean)

    def setShadowEnable(self, boolean):
        self.windowModel().setShadowEnable(boolean)

    def isShadowEnable(self):
        return self.windowModel().isShadowEnable()

    def setMaximizeEnable(self, boolean):
        self.windowModel().setMaximizeEnable(boolean)

    def setMinimizeEnable(self, boolean):
        self.windowModel().setMinimizeEnable(boolean)

    def setExpandEnable(self, boolean):
        self.windowModel().setExpandEnable(boolean)

    def isExpandEnable(self):
        return self.windowModel().isExpandEnable()

    def setMaxProgressValue(self, value):
        self.windowModel().setMaxProgressValue(value)

    def maxProgressValue(self):
        return self.windowModel().maxProgressValue()

    def setProgressValue(self, value, maxValue=None):
        self.windowModel().setProgressValue(value, maxValue)

    def progressValue(self):
        return self.windowModel().progressValue()

    def setProgressStatus(self, status):
        pass

    def updateProgress(self, *args):
        self.windowModel().updateProgress()

    def addWidget(self, widget):
        self.windowModel().addWidget(widget)

    def uiShow(self, *args):
        self.windowModel().uiShow(*args)

    def uiQuit(self):
        self.windowModel().uiQuit()

    def setQuitConnect(self, method):
        self.windowModel()._addQuitConnectMethod(method)

    def setCountdownClose(self, value=5):
        self.windowModel().setCountdownClose(value)

    def setCountdownCloseStop(self):
        self.windowModel().setCountdownCloseStop()

    def setPlaceholderEnable(self, boolean):
        self.windowModel().setPlaceholderEnable(boolean)

    def viewModel(self):
        return self._viewModel

    def windowModel(self):
        return self._viewModel

    def setActionData(self, actionData):
        self._menuButton.setActionData(actionData)
        if actionData:
            self._menuButton.setPressable(True)
        else:
            self._menuButton.setPressable(False)

    def setupUi(self):
        self.installEventFilter(self)
        #
        self._menuButton = self.CLS_gui_qt__window_wgt__iconbutton('svg_basic/menu', self)
        self._menuButton.setPressable(False)
        #
        self._closeButton = self.CLS_gui_qt__window_wgt__iconbutton('svg_basic/close', self)
        self._closeButton.setTooltip(u'关闭窗口\nClose Window')
        #
        self._maximizeButton = self.CLS_gui_qt__window_wgt__iconbutton('svg_basic/maximize', self)
        self._maximizeButton.hide()
        self._maximizeButton.setTooltip(u'最大化 / 正常化窗口\nMaximized / Normalize Window')
        #
        self._minimizeButton = self.CLS_gui_qt__window_wgt__iconbutton('svg_basic/minimize', self)
        self._minimizeButton.hide()
        self._minimizeButton.setTooltip(u'最小化 / 正常化窗口\nMinimized / Normalize Window')
        #
        self._expandButton = self.CLS_gui_qt__window_wgt__iconbutton('svg_basic/fold', self)
        self._expandButton.hide()
        self._expandButton.setTooltip(u'点击展开 / 收起主面板\nExpand / Contract Window')
        #
        self._helpButton = self.CLS_gui_qt__window_wgt__iconbutton('svg_basic/help', self)
        self._helpButton.hide()
        #
        self._confirmButton = self.CLS_gui_qt__window_wgt__iconbutton('svg_basic/confirm', self)
        self._confirmButton.hide()
        self._confirmButton.setNameString('Confirm')
        self._confirmButton.setTooltip(u'确认操作 / 修改\nConfirm Operated / Changed')
        self._confirmButton.clicked.connect(self.confirmAction)
        self._confirmButton.clicked.connect(self.uiQuit)
        #
        self._cancelButton = self.CLS_gui_qt__window_wgt__iconbutton('svg_basic/cancel', self)
        self._cancelButton.hide()
        self._cancelButton.setNameString('Cancel')
        self._cancelButton.setTooltip(u'取消操作 / 修改\nCancel Operated / Changed')
        self._cancelButton.clicked.connect(self.uiQuit)
        #
        # noinspection PyArgumentList
        self._progressBar = qtCore.QProgressBar()
        self._progressBar.setParent(self)
        #
        self._viewModel = self.CLS_gui_qt__window_wgt__model(self)
        #
        self._closeButton.clicked.connect(self.uiQuit)
        #
        self._maximizeButton.clicked.connect(self._viewModel._maximizeButtonPressAction)
        self._minimizeButton.clicked.connect(self._viewModel._minimizeButtonPressAction)
        self._expandButton.clicked.connect(self._viewModel._expandButtonPressAction)


# Chart
class AbsGuiQtChartWgt(qtCore.QWidget):
    MODEL_CHART_CLS = None

    def _initAbsGuiQtChartWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding
        )
        # noinspection PyArgumentEqualDefault
        self.setFont(
            qtCore.qtFont(size=8, weight=50, family=qtCore._families[1])
        )
        #
        self._initAbsGuiQtChartWgtUi()
    #
    def _initAbsGuiQtChartWgtUi(self):
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 0, 0, 0, 0
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
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.chartModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.chartModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.chartModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.chartModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
            else:
                event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.chartModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
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
        self._chartModel = self.MODEL_CHART_CLS(self)


class AbsGuiQtScrollbarWgt(qtCore.QWidget):
    CLS_gui_qt__scrollbar_wgt_iconbutton = None

    valueChanged = qtCore.qtSignal()
    stop = qtCore.qtSignal()

    def _initAbsGuiQtScrollbarWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
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
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(True)
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(True)
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(True)
        else:
            event.ignore()
    #
    def keyReleaseEvent(self, event):
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            self.viewModel()._setCtrlFlag(False)
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            self.viewModel()._setShiftFlag(False)
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            self.viewModel()._setAltFlag(False)
        else:
            event.ignore()
    #
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
            #
            self.viewModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.viewModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.viewModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
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
            painter.setBackgroundRgba(self._wgt__background_rgba)
            painter.setBorderRgba(self._wgt__border_rgba)
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
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        #
        if self.viewModel().isScrollable():
            setDrawBaseArea()
            # Scroll
            setDrawBaseArea()
            # Click
            setDrawClickArea()
            # Slider
            setDrawSlider()

        # painter.end()  # for pyside2
    #
    def setLayoutDirection(self, value):
        self.viewModel().setLayoutDirection(value)
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
        self._wgt__background_rgba = 56, 56, 56, 255
        self._wgt__border_rgba = 95, 95, 95, 255
        #
        self._wgt__name_rgba = 223, 223, 223, 255
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
        self._menuButton = self.CLS_gui_qt__scrollbar_wgt_iconbutton('svg_basic/menu', self)
        self._subScrollButton = self.CLS_gui_qt__scrollbar_wgt_iconbutton('svg_basic/vscrollsub', self)
        self._subScrollButton.setTooltip(u'''单击：向上翻页\n按住：向上滚动''')
        self._addScrollButton = self.CLS_gui_qt__scrollbar_wgt_iconbutton('svg_basic/vscrolladd', self)
        self._addScrollButton.setTooltip(u'''单击：向下翻页\n按住：向下滚动''')
        self._tooltipWidget = qtCore.QtTooltipWidget_(self)
        #
        self._viewModel = guiQtMdlAbs._QtScrollbarModel(self)


# Value Enter Label
class AbsGuiQtValueArrayLineWgt(qtCore.QWidget):
    CLS_gui_qt__value_array_line_wgt__line_edit = None

    def _initAbsQtWgtValueEnterlabel(self):
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Minimum
        )
        self.setFocusPolicy(qtCore.QtCore.Qt.ClickFocus)

        self._initAbsQtWgtValueEnterlabelAttr()
        self._initAbsQtWgtValueEnterlabelUi()

        self.setupUi()

        self.setUiSize()
    #
    def _initAbsQtWgtValueEnterlabelAttr(self):
        pass
    #
    def _initAbsQtWgtValueEnterlabelUi(self):
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 95, 95, 95, 255
        self._uiEnterBackgroundRgbaLis = [(47, 47, 47, 255)]
        self._uiEnterBorderRgbaLis = [(95, 95, 95, 255)]
        #
        self._wgt__name_rgba = 191, 191, 191, 255
        #
        self._wgt__border_style = 'solid'
        #
        self.setFont(
            qtCore.qtFont()
        )
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHint(painter.Antialiasing)
        painter.setFont(self.font())
        # Name
        if self.itemModel().nameText() is not None:
            rect = self.itemModel().nameTextRect()
            textOption = qtCore.QtCore.Qt.AlignRight | qtCore.QtCore.Qt.AlignVCenter
            painter.setBorderRgba(self._wgt__name_rgba)
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
                        self._wgt__border_style
                    )

        # painter.end()  # for pyside2
    #
    def setEnterEnable(self, boolean):
        self.itemModel().setEnterEnable(boolean)
    #
    def setNameString(self, text):
        self.itemModel().setNameString(text)
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
        self._itemModel = guiQtMdlAbs._QtValueArrayLineModel(self)
        self._itemModel.setEnterWidgetClass(self.CLS_gui_qt__value_array_line_wgt__line_edit)


# Filter Enter Label
class AbsGuiQtFilterLineWgt(qtCore.QWidget):
    CLS_gui_qt__filter_line_wgt__model = None

    CLS_gui_qt__filter_line_wgt__line_edit = None

    CLS_gui_qt__filter_line_wgt_iconbutton = None
    CLS_gui_qt__filter_line_wgt_checkbutton = None

    entryChanged = qtCore.qtSignal()

    def _initAbsGuiQtFilterLineWgt(self):
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Preferred
        )
        self.setFocusPolicy(qtCore.QtCore.Qt.ClickFocus)
        #
        self._initAbsGuiQtFilterLineWgtAttr()
        self._initAbsGuiQtFilterLineWgtUi()
        #
        self.setupUi()
        #
        self.setUiSize()
        #
        self.readHistory()
        self._loadHistoryAction()
    #
    def _initAbsGuiQtFilterLineWgtAttr(self):
        self._historyLis = []
        self._filterCount = 0
    #
    def _initAbsGuiQtFilterLineWgtUi(self):
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 95, 95, 95, 255
        #
        self._wgt__name_rgba = 191, 191, 191, 255
        #
        self._wgt__border_style = 'solid'
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

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
                self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._wgt__border_style
            )
        else:
            painter.setDrawButtonBasic(
                self.itemModel().basicRect(),
                borderWidth, borderRadius,
                self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._wgt__border_style
            )
        painter.setBorderRgba(self._uiEnterBorderRgba)
        painter.drawLine(
            self.itemModel()._toolLine
        )
        painter.setFont(
            qtCore.qtFont(size=10, weight=50, family=qtCore._families[0])
        )
        painter.drawText(
            self.itemModel()._occurrenceCounterRect,
            qtCore.QtCore.Qt.AlignRight | qtCore.QtCore.Qt.AlignVCenter,
            self.itemModel()._occurrenceCounterText
        )
        # painter.end()  # for pyside2
    #
    def setNameString(self, string):
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
                (keywordFilterString, 'svg_basic/history', True, setMethod)
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
        self._historyBtnWgt.setActionData(actionDatumLis)
    #
    def readHistory(self):
        filterHistoryFile = shmOutput.UserPreset().uiFilterConfigFile
        data = bscMethods.OsJsonFile.read(filterHistoryFile)
        if data:
            self._historyLis = data
    #
    def writeHistory(self):
        filterHistoryFile = shmOutput.UserPreset().uiFilterConfigFile
        data = self._historyLis[-10:]
        bscMethods.OsJsonFile.write(filterHistoryFile, data)
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
    def setFocusIn(self):
        # noinspection PyArgumentList
        self.setFocus(qtCore.QtCore.Qt.ClickFocus)
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
    def _setQtEnterStyle(self, state):
        self.itemModel()._setQtEnterStyle(state)
    #
    def addFilterTarget(self, widget):
        self.itemModel().addFilterTarget(widget)
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
    def _entryChangedEmit(self):
        self.entryChanged.emit()
    #
    def isMatchCase(self):
        return self._matchCaseBtnWgt.isChecked()
    #
    def isMatchWord(self):
        return self._matchWordBtnWgt.isChecked()
    #
    def setupUi(self):
        self._historyBtnWgt = self.CLS_gui_qt__filter_line_wgt_iconbutton('svg_basic/search')
        self._historyBtnWgt.setParent(self)

        #
        self._enterWidget = self.CLS_gui_qt__filter_line_wgt__line_edit()
        self._enterWidget.setParent(self)
        # noinspection PyArgumentEqualDefault
        self._enterWidget.setFont(qtCore.qtFont(size=8, weight=50))
        self._enterWidget.setAlignment(qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter)
        self._enterWidget.entryChanged.connect(self.enterChangedEmit)
        # Copy
        self._copyButton = self.CLS_gui_qt__filter_line_wgt_iconbutton('svg_basic/copy')
        self._copyButton.setParent(self)
        self._copyButton.hide()
        self._copyButton.setTooltip(
            u'点击复制输入'
        )
        self._copyButton.setFocusProxy(self._enterWidget)
        #
        self._clearButton = self.CLS_gui_qt__filter_line_wgt_iconbutton('svg_basic/clear')
        self._clearButton.setParent(self)
        self._clearButton.hide()
        self._clearButton.setFocusProxy(self._enterWidget)

        self._matchCaseBtnWgt = self.CLS_gui_qt__filter_line_wgt_checkbutton('svg_basic/matchcase')
        self._matchCaseBtnWgt.setParent(self)
        self._matchCaseBtnWgt.setTooltip(
            u'''Enable/Disable Match Case.'''
        )
        self._matchCaseBtnWgt.setFocusProxy(self._enterWidget)

        self._matchWordBtnWgt = self.CLS_gui_qt__filter_line_wgt_checkbutton('svg_basic/matchword')
        self._matchWordBtnWgt.setParent(self)
        self._matchWordBtnWgt.setTooltip(
            u'''Enable/Disable Match Word.'''
        )
        self._matchWordBtnWgt.setFocusProxy(self._enterWidget)

        self._preOccurrenceBtnWgt = self.CLS_gui_qt__filter_line_wgt_iconbutton('svg_basic/preoccurrence')
        self._preOccurrenceBtnWgt.setParent(self)
        self._preOccurrenceBtnWgt.setTooltip(
            u'''Previous Occurrence.'''
        )
        self._preOccurrenceBtnWgt.setPressable(False)
        self._preOccurrenceBtnWgt.setFocusProxy(self._enterWidget)

        self._nextOccurrenceBtnWgt = self.CLS_gui_qt__filter_line_wgt_iconbutton('svg_basic/nextoccurrence')
        self._nextOccurrenceBtnWgt.setParent(self)
        self._nextOccurrenceBtnWgt.setTooltip(
            u'''Next Occurrence.'''
        )
        self._nextOccurrenceBtnWgt.setPressable(False)
        self._nextOccurrenceBtnWgt.setFocusProxy(self._enterWidget)
        #
        self._itemModel = self.CLS_gui_qt__filter_line_wgt__model(self)
        #
        self._historyBtnWgt.clicked.connect(self._loadHistoryAction)
        #
        self._enterWidget.focusChanged.connect(self._itemModel._updateUiEnterState)
        self._enterWidget.focusOut.connect(self._uploadHistoryAction)
        self._clearButton.clicked.connect(self.setEnterClear)

        self._matchCaseBtnWgt.clicked.connect(self._entryChangedEmit)
        self._matchWordBtnWgt.clicked.connect(self._entryChangedEmit)


# Choose View
class AbsGuiQtChooseViewportWgt(AbsGuiQtViewWgt):
    CLS_gui_qt__view_wgt__model = None

    CLS_gui_qt__view_wgt__scrollbar = None
    # noinspection PyUnusedLocal
    def _initAbsGuiQtChooseViewportWgt(self, *args):
        self._initAbsGuiQtViewWgt()
        self._gui_qt__choose_viewport__set_build_()

    def _gui_qt__choose_viewport__set_build_(self):
        self._hScrollBar = self.CLS_gui_qt__view_wgt__scrollbar(self)
        self._vScrollBar = self.CLS_gui_qt__view_wgt__scrollbar(self)
        #
        self._viewModel = self.CLS_gui_qt__view_wgt__model(self)


class AbsGuiQtChooseWindowWgt(qtCore.QWidget):
    CLS_gui_qt__choose_window_wgt__model = None

    CLS_gui_qt__choose_window_wgt__viewport = None
    CLS_gui_qt__choose_window_wgt__viewitem = None

    CLS_gui_qt__choose_window_wgt__iconbutton = None

    CLS_gui_qt__choose_window_wgt__filter_line = None

    currentChanged = qtCore.qtSignal()

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(AbsGuiQtChooseWindowWgt, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self.setWindowFlags(qtCore.QtCore.Qt.Drawer | qtCore.QtCore.Qt.FramelessWindowHint)
        #
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        #
        self.initUi()
        #
        self.setupUi()
    #
    def _initAbsGuiQtChooseWindowWgt(self, *args):
        self.initUi()
        self.setupUi()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # noinspection PyArgumentEqualDefault
        painter.setFont(qtCore.qtFont(size=8, weight=50, family=_families[1]))
        #
        side = self.viewModel()._uiSide
        margin = self.viewModel()._uiMargin
        shadowRadius = self.viewModel()._uiShadowRadius
        #
        painter.setDrawMenuFrame(
            self.viewModel()._uiBasicRect,
            margin, side, shadowRadius, self.viewModel()._region,
            self._wgt__background_rgba, self._wgt__border_rgba
        )
        #
        if self.viewModel()._isTearable is True:
            xPos, yPos = self.viewModel()._pos
            painter.setBorderRgba(self._wgt__border_rgba)
            painter.drawLine(
                QtCore.QLine(xPos, yPos, xPos + self.viewModel()._uiMainWidth, yPos - 1)
            )

        # painter.end()  # for pyside2
    #
    def setCurrentIndex(self, index):
        self.viewModel().setCurrentIndex(index)
    #
    def setDrop(self):
        worldPos = qtCore.getCursorPos()
        desktopRect = qtCore.getDesktopRect()
        #
        self.viewModel()._drop(worldPos, desktopRect)
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
        self._wgt__background_rgba = 63, 63, 63, 255
        self._wgt__border_rgba = 95, 95, 95, 255
        self._wgt__name_rgba = 223, 223, 223, 255
    #
    def viewModel(self):
        return self._viewModel
    #
    def setupUi(self):
        self._viewport = self.CLS_gui_qt__choose_window_wgt__viewport(self)
        self._viewport.setContentsMargins(0, 0, 0, 0)
        self._viewport.setSpacing(2)
        self._viewport.itemClicked.connect(self.currentChangedEvent)
        #
        self._separateButton = self.CLS_gui_qt__choose_window_wgt__iconbutton('svg_basic/unpinwindow', self)
        self._separateButton.hide()
        #
        self._filterViewWidget = self.CLS_gui_qt__choose_window_wgt__filter_line(self)
        self._filterViewWidget.hide()
        #
        self._viewModel = self.CLS_gui_qt__choose_window_wgt__model(
            self,
            self.CLS_gui_qt__choose_window_wgt__viewitem
        )


class AbsGuiQtActionViewitemWgt(qtCore.QWidget):
    CLS_gui_qt__action_viewitem_wgt__iconbutton = None

    clicked = qtCore.qtSignal()
    itemHeight = 20

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(AbsGuiQtActionViewitemWgt, self)
            self._clsSuper.__init__(*args, **kwargs)

        self._initAbsGuiQtActionViewitemWgt()

    def _initAbsGuiQtActionViewitemWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)

        self.initUi()

        self.setupUi()
    #
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._clickAction(event)
        else:
            event.ignore()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setFont(self.font())
        #
        if self.itemModel().isSeparator():
            if self.itemModel()._gui_qt__mdl__name_str_ is not None:
                textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
                painter.setBorderRgba(127, 127, 127, 255)
                painter.drawText(self.itemModel()._gui_qt__mdl__name_str_Rect, textOption, self.itemModel()._gui_qt__mdl__name_str_)
            painter.setBorderRgba(95, 95, 95, 255)
            painter.drawLine(self.itemModel()._basicLine)
        else:
            painter.setBackgroundRgba(self._wgt__background_rgba)
            painter.setBorderRgba(self._wgt__border_rgba)
            painter.drawRect(self.itemModel()._uiBasicRect)
            if self.itemModel().isCheckEnable() is True:
                painter._gui_qt__set_image_draw_(
                    self.itemModel()._uiIconRect, self.itemModel()._uiCheckIcon
                )
            else:
                if self.itemModel()._uiIcon is not None:
                    painter._gui_qt__set_image_draw_(
                        self.itemModel()._uiIconRect,
                        self.itemModel()._uiIcon
                    )
                    if self.itemModel()._uiSubIcon is not None:
                        painter._gui_qt__set_image_draw_(
                            self.itemModel()._uiSubIconRect,
                            self.itemModel()._uiSubIcon
                        )
            #
            if self.itemModel()._gui_qt__mdl__name_str_ is not None:
                font = painter.font()
                font.setItalic(self._uiFontItalic)
                painter.setFont(font)
                painter.setBorderRgba(self._wgt__name_rgba)
                textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
                painter.drawText(self.itemModel()._gui_qt__mdl__name_str_Rect, textOption, self.itemModel()._gui_qt__mdl__name_str_)
            if self.itemModel()._uiSubNameText is not None:
                painter.setBorderRgba(self._wgt__name_rgba)
                textOption = qtCore.QtCore.Qt.AlignRight | qtCore.QtCore.Qt.AlignVCenter
                painter.drawText(self.itemModel()._uiSubNameRect, textOption, self.itemModel()._uiSubNameText)
            if self.itemModel()._uiExtendIcon is not None:
                painter._gui_qt__set_image_draw_(
                    self.itemModel()._uiExtendRect, self.itemModel()._uiExtendIcon
                )

        # painter.end()  # for pyside2
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
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 63, 63, 63, 255
        #
        self._wgt__name_rgba = 191, 191, 191, 255
        self._uiIndexRgba = 191, 191, 191, 255
        # noinspection PyArgumentEqualDefault
        self.setFont(qtCore.qtFont(size=8, weight=50))
        #
        self._uiFontItalic = False
    #
    def itemModel(self):
        return self._itemModel
    #
    def setupUi(self):
        self._extendButton = self.CLS_gui_qt__action_viewitem_wgt__iconbutton('svg_basic/subwindow', self)
        self._extendButton.hide()
        #
        self._itemModel = guiQtMdlAbs.AbsGuiQtActionViewitemWgtModel(self)


class AbsGuiQtActionViewportWgt(qtCore.QWidget):
    CLS_gui_qt__action_viewport_wgt__model = None

    CLS_gui_qt__action_viewport_wgt__viewitem = None

    CLS_gui_qt__action_viewport_wgt__iconbutton = None

    actionAccepted = qtCore.qtSignal()

    def _initAbsGuiQtActionViewportWgt(self):
        self.setWindowFlags(qtCore.QtCore.Qt.Drawer | qtCore.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        #
        self._initAbsGuiQtActionViewportWgtAction()
        self._initAbsGuiQtActionViewportWgtUi()
        #
        self.setupUi()

    def _initAbsGuiQtActionViewportWgtAction(self):
        self._altFlag, self._shiftFlag, self._ctrlFlag = False, False, False

    def _initAbsGuiQtActionViewportWgtUi(self):
        self._wgt__background_rgba = 63, 63, 63, 255
        self._wgt__border_rgba = 95, 95, 95, 255
        #
        self._uiSeparatorBorderRgba = 95, 95, 95, 255
        self._wgt__name_rgba = 223, 223, 223, 255

    def enterEvent(self, event):
        pass

    def leaveEvent(self, event):
        self.viewModel()._clearHover()

    def keyPressEvent(self, event):
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            self._ctrlFlag = True
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            self._shiftFlag = True
            self.viewModel()._updateShiftMode()
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            self._altFlag = True
        else:
            event.ignore()

    def keyReleaseEvent(self, event):
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            self._ctrlFlag = False
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            self._shiftFlag = False
            self.viewModel()._updateShiftMode()
            self.viewModel()._shiftStopAction()
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            self._altFlag = False
        else:
            event.ignore()

    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()

    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
        else:
            event.ignore()

    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.viewModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.viewModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
            else:
                event.ignore()

    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # noinspection PyArgumentEqualDefault
        painter.setFont(qtCore.qtFont(size=8, weight=50, family=_families[1]))
        #
        side = self.viewModel()._uiSide
        margin = self.viewModel()._uiMargin
        shadowRadius = self.viewModel()._uiShadowRadius
        #
        painter.setDrawMenuFrame(
            self.viewModel()._uiBasicRect,
            margin, side, shadowRadius, self.viewModel()._region,
            self._wgt__background_rgba, self._wgt__border_rgba
        )
        #
        if self.viewModel()._isTearable is True:
            painter.setBorderRgba(self._uiSeparatorBorderRgba)
            painter.drawLine(self.viewModel()._titleLine)
            #
            if self.viewModel()._gui_qt__mdl__name_str_ is not None:
                painter.setBorderRgba(self._wgt__name_rgba)
                textOption = qtCore.QtCore.Qt.AlignHCenter | qtCore.QtCore.Qt.AlignVCenter
                painter.drawText(self.viewModel()._titleRect, textOption, self.viewModel()._gui_qt__mdl__name_str_)
        #
        for k, v in self.viewModel()._subRectDic.items():
            if k > 0:
                if v is not None:
                    subRect = v
                    enable = self.viewModel()._subEnableDic[k]
                    if enable is True:
                        painter.setDrawShadow(subRect, shadowRadius, shadowRadius)
                        #
                        painter.setBackgroundRgba(self._wgt__background_rgba)
                        painter.setBorderRgba(self._wgt__border_rgba)
                        painter.drawRect(subRect)

        # painter.end()  # for pyside2

    def setTitle(self, string):
        self.viewModel().setTitle(string)

    def setTearable(self, boolean):
        self.viewModel().setTearable(boolean)

    def setActionData(self, actions):
        self.viewModel().setActionData(actions)

    # noinspection PyUnusedLocal
    def setDrop(self, point=None):
        worldPos = qtCore.getCursorPos()
        desktopRect = qtCore.getDesktopRect()
        #
        self.viewModel()._drop(worldPos, desktopRect)

    def viewModel(self):
        return self._viewModel

    def setupUi(self):
        self._separateButton = self.CLS_gui_qt__action_viewport_wgt__iconbutton('svg_basic/unpin_', self)
        self._separateButton.hide()
        #
        self._vScrollBar = None
        #
        self._viewModel = self.CLS_gui_qt__action_viewport_wgt__model(
            self,
            self.CLS_gui_qt__action_viewport_wgt__viewitem
        )


class AbsGuiQtTabitemWgt(qtCore.QWidget):
    CLS_gui_qt__tabitem_wgt__model = None

    CLS_gui_qt__tabitem_wgt__iconbutton = None
    CLS_gui_qt__tabitem_wgt__action_iconbutton = None

    clicked = qtCore.qtSignal()
    currentToggled = qtCore.qtSignal(bool)

    def _initAbsGuiQtTabitemWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)

        self.setMouseTracking(True)

        self._initAbsGuiQtTabitemWgtUi()
    #
    def _initAbsGuiQtTabitemWgtUi(self):
        self._wgt__background_rgba = 63, 63, 63, 255
        self._wgt__border_rgba = 71, 71, 71, 255
        #
        self._wgt__name_rgba = 191, 191, 191, 255
        # noinspection PyArgumentEqualDefault
        self._gui_qt___gui_qt__wgt__name_font = qtCore.qtFont(size=8, weight=75, family=_families[1])

    @qtCore.gui_qt_mdf__set_tooltip_start
    def enterEvent(self, event):
        self.itemModel()._gui_qt__set_enter_event_update_(event)

    @qtCore.gui_qt_mdf__set_tooltip_stop
    def leaveEvent(self, event):
        self.itemModel()._gui_qt__set_leave_event_update_(event)

    @qtCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()

    @qtCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.itemModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.itemModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
            else:
                event.ignore()

    @qtCore.uiTooltipClearMethod
    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.itemModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
        else:
            event.ignore()

    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHint(painter.Antialiasing)
        #
        borderWidth, borderRadius = 1, 12
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        # noinspection PyArgumentEqualDefault
        painter.setDrawTab(
            self.itemModel().basicRect(),
            borderWidth, borderRadius,
            self._wgt__background_rgba, self._wgt__border_rgba,
            tabRegion=self.itemModel().tabRegion(), tabPosition=self.itemModel().tabPosition()
        )
        #
        if self.itemModel().tabPosition() == qtCore.East:
            painter.rotate(90)
            painter.translate(0, -self.width())
        elif self.itemModel().tabPosition() == qtCore.West:
            painter.rotate(-90)
            painter.translate(-self.height(), 0)
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(), self.itemModel().icon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            rect = self.itemModel().nameTextRect()
            if self.itemModel().tabPosition() == qtCore.West:
                textOption = qtCore.QtCore.Qt.AlignHCenter | qtCore.QtCore.Qt.AlignVCenter
            else:
                textOption = qtCore.QtCore.Qt.AlignHCenter | qtCore.QtCore.Qt.AlignVCenter
            #
            self.setFont(self._gui_qt___gui_qt__wgt__name_font)
            painter.setFont(self._gui_qt___gui_qt__wgt__name_font)
            painter.setBorderRgba(self._wgt__name_rgba)
            painter.drawText(
                rect,
                textOption,
                self.itemModel().drawNameText()
            )

        # painter.end()  # for pyside2

    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()

    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)

    def setActionData(self, actionData):
        self.itemModel().setActionData(actionData)

    def setTooltip(self, string):
        if string:
            self.uiTip = string

    def itemModel(self):
        return self._itemModel

    def setupUi(self):
        self._menuButton = self.CLS_gui_qt__tabitem_wgt__action_iconbutton('svg_basic/tabMenu_v', self)
        self._menuButton.setPressable(False)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._closeButton = self.CLS_gui_qt__tabitem_wgt__iconbutton(parent=self)
        self._closeButton.hide()
        self._closeButton.setIcon('svg_basic/closeTab', 8, 8, 10, 10)
        #
        self._itemModel = self.CLS_gui_qt__tabitem_wgt__model(self)


# Tab Bar
class AbsGuiQtTabbarWgt(qtCore.QWidget):
    CLS_gui_qt__tabbar_wgt_model = None
    # Scroll
    valueChanged = qtCore.qtSignal()
    stop = qtCore.qtSignal()
    # Click
    currentChanged = qtCore.qtSignal()
    def _initAbsGuiQtTabbarWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding
        )
        self.setFocusPolicy(qtCore.QtCore.Qt.NoFocus)
        self.setMouseTracking(True)
        #
        self._initAbsGuiQtTabbarWgtUi()
        #
        self.setupUi()
    #
    def _initAbsGuiQtTabbarWgtUi(self):
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 95, 95, 95, 255
        #
        self._uiTabHoverBackgroundRgba = 63, 127, 255, 255
        self._uiTabBorderRgba = 95, 95, 95, 255
        #
        self._uiScrollBackgroundRgba = 80, 80, 80, 255
        self._uiScrollBorderRgba = 95, 95, 95, 255
    #
    def enterEvent(self, event):
        self.viewModel()._gui_qt__set_enter_event_update_(event)
    #
    def leaveEvent(self, event):
        self.viewModel()._gui_qt__set_leave_event_update_(event)
    #
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseDoubleClickEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.viewModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.viewModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.viewModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
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
        self._viewModel = self.CLS_gui_qt__tabbar_wgt_model(self)


# Tab View
class AbsGuiQtTabgroupWgt(qtCore.QWidget):
    CLS_gui_qt__tabgroup_wgt__model = None

    CLS_gui_qt__tabgroup_wgt__iconbutton = None
    CLS_gui_qt__tabgroup_wgt__action_iconbutton = None

    CLS_gui_qt__tabgroup_wgt__tabbar = None

    CLS_gui_qt__tabgroup_wgt__tabbutton = None
    CLS_gui_qt__tabgroup_wgt__choose_tabbutton = None

    currentChanged = qtCore.qtSignal()
    def _initAbsGuiQtTabgroupWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding
        )
        self.setFocusPolicy(qtCore.QtCore.Qt.NoFocus)
        self.setMouseTracking(True)
        #
        self._initAbsGuiQtTabgroupWgtUi()
    #
    def _initAbsGuiQtTabgroupWgtUi(self):
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 95, 95, 95, 255

    def enterEvent(self, event):
        self.setCursor(
            qtCore.QtCore.Qt.ArrowCursor
        )
        self.viewModel()._gui_qt__set_enter_event_update_(event)
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
    def addTab(self, widget, name=None, iconKeywordStr=None, tooltip=None):
        self.viewModel().addTab(widget, name, iconKeywordStr, tooltip)
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


# Group
class AbsGuiQtGroupWgt(qtCore.QWidget):
    CLS_gui_qt__group_wgt__model = None

    CLS_gui_qt__group_wgt__iconbutton = None
    CLS_gui_qt__group_wgt__action_iconbutton = None

    CLS_gui_qt__group_wgt_separate_window = None

    expanded = qtCore.qtSignal()
    separated = qtCore.qtSignal()
    def _initAbsGuiQtGroupWgt(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Fixed
        )
        #
        self.setFocusPolicy(qtCore.QtCore.Qt.NoFocus)
        #
        self._initAbsGuiQtGroupWgtDraw()
    #
    def _initAbsGuiQtGroupWgtDraw(self):
        self._clickFlag = True
        self._isColorEnable = True
        #
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 95, 95, 95, 255
        #
        self._uiViewportBackgroundRgba = 47, 47, 47, 63
        self._uiViewportBorderRgba = 95, 95, 95, 255
        #
        self._wgt__name_rgba = 191, 191, 191, 255
        #
        self._wgt__color__background_rgba = 191, 191, 191, 255
        self._wgt__color__border_rgba = 127, 127, 127, 255
        # noinspection PyArgumentEqualDefault
        self.setFont(
            qtCore.qtFont(size=8, weight=75, family=_families[1])
        )
        #
        self._separatorLis = []

    @qtCore.gui_qt_mdf__set_tooltip_start
    def enterEvent(self, event):
        self.groupModel()._gui_qt__set_enter_event_update_(event)

    @qtCore.gui_qt_mdf__set_tooltip_stop
    def leaveEvent(self, event):
        self.groupModel()._gui_qt__set_leave_event_update_(event)

    @qtCore.uiTooltipClearMethod
    def mousePressEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.groupModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()

    @qtCore.uiTooltipClearMethod
    def mouseDoubleClickEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.groupModel()._gui_qt__mdl__set_mouse_press_event_update_(event)
        else:
            event.ignore()

    @qtCore.uiTooltipClearMethod
    def mouseReleaseEvent(self, event):
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.groupModel()._gui_qt__mdl__set_mouse_release_event_update_(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == qtCore.QtCore.Qt.NoButton:
            self.groupModel()._gui_qt__mdl__set_mouse_move_event_update_(event)
        else:
            if event.buttons() == qtCore.QtCore.Qt.LeftButton:
                self.groupModel()._gui_qt__mdl__set_mouse_press_move_event_update_(event)
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
    def setNameString(self, text):
        self.groupModel().setNameString(text)
    #
    def setTitle(self, text):
        self.groupModel().setNameString(text)

    def setIndexString(self, text):
        self.groupModel().setIndexString(text)
    #
    def setTooltip(self, string):
        if string:
            self.uiTip = string

    def tooltipRect(self):
        return self._groupModel.expandPressRect()
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
        self._menuButton = self.CLS_gui_qt__group_wgt__action_iconbutton('svg_basic/tabmenu_h', self)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        self._groupModel = self.CLS_gui_qt__group_wgt__model(self)


# Text Brower
class AbsGuiQtTextbrowerWgt(qtCore.QWidget):
    CLS_gui_qt__text_brower_wgt__model = None

    CLS_gui_qt__text_brower_wgt__text_edit = None

    CLS_gui_qt__mdl_textbrower__filter_line = None

    entryChanged = qtCore.qtSignal()

    counterWidth = 32
    menuHeight = 24

    def _initAbsGuiQtTextbrowerWgt(self):
        self._initUiVar()

        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        # noinspection PyArgumentList
        self.setSizePolicy(
            qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding
        )

        self.setupUi()

        self.setUiSize()

    def _initUiVar(self):
        self._uiEnterBackgroundRgba = 47, 47, 47, 255
        self._uiEnterBorderRgba = 95, 95, 95, 255
        #
        self._wgt__name_rgba = 191, 191, 191, 255
        self._uiIndexRgba = 95, 95, 95, 255
        #
        self._wgt__border_style = 'solid'
        #
        self._coding = None
        #
        self._index = None

    @qtCore.gui_qt_mdf__set_tooltip_start
    def enterEvent(self, event):
        pass

    @qtCore.gui_qt_mdf__set_tooltip_stop
    def leaveEvent(self, event):
        pass
    #
    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()
    #
    def paintEvent(self, event):
        def paintCounterFnc_():
            _uiYPos = yPos
            # Counter
            countOffset = self.itemModel()._countOffset
            #
            _uiYPos -= countOffset % textHeight - 5
            #
            countNum = int(countOffset / textHeight)
            countRange = int(height / textHeight) + 1
            #
            painter.setBorderRgba(self._uiIndexRgba)
            for i in range(countRange):
                lineCount = i + countNum + 1
                if lineCount <= maximumCount:
                    countRect = QtCore.QRect(
                        xPos + leftSide, _uiYPos,
                        self.counterWidth, textHeight
                    )
                    painter.drawText(
                        countRect,
                        qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter,
                        str(lineCount)
                    )
                #
                _uiYPos += textHeight
        #
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

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
        textHeight = self.textEdit().fontMetrics().height()
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
                    qtCore.QtCore.QRect(rect.topLeft().x() + 1, rect.topLeft().y() + 1, rect.width() - 2, rect.height() - 2),
                    borderRadius - 2, borderRadius - 2,
                    qtCore.QtCore.Qt.AbsoluteSize
                )
            else:
                painter.setDrawButtonBasic(
                    self.itemModel().basicRect(),
                    borderWidth, borderRadius,
                    self._uiEnterBackgroundRgba, self._uiEnterBorderRgba, self._wgt__border_style
                )
        #
        # paintCounterFnc_()
        # Coding
        if self.itemModel().isCodingEnable():
            if self._coding is not None:
                for seq, (k, v) in enumerate(self._coding.items()):
                    codingRect = QtCore.QRect(width - 180, height - (3-seq)*12, 180, 12)
                    painter.drawText(codingRect, qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter, '{0} : {1}'.format(k, v))
        #
        if self._index is not None:
            selRect = QtCore.QRect(
                xPos, self._index*textHeight,
                width, textHeight
            )
            #
            painter.setBackgroundRgba(95, 95, 95, 255)
            painter.setBorderRgba(95, 95, 95, 255)
            painter.drawRect(selRect)

        # painter.end()  # for pyside2

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
        return self._textEditWgt
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
    def addText(self, *args):
        def addFnc_(text_):
            textEdit = self._textEditWgt
            textEdit.moveCursor(qtCore.QtGui.QTextCursor.End)
            textEdit.insertPlainText(text_)
            textEdit.moveCursor(qtCore.QtGui.QTextCursor.End)
        #
        if isinstance(args[0], (tuple, list)):
            [addFnc_(i) for i in args]
        else:
            addFnc_(args[0])
        #
        self.update()
    #
    def text(self):
        return self.textEdit().toPlainText()
    #
    def setNameString(self, string):
        self.itemModel().setNameString(string)
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
            qtCore.qtFont(size=value, family=_families[0])
        )
    #
    def setupUi(self):
        self._filterLineWgt = self.CLS_gui_qt__mdl_textbrower__filter_line(self)

        self._textEditWgt = self.CLS_gui_qt__text_brower_wgt__text_edit(self)
        self._textEditWgt.setParent(self)
        self._textEditWgt.setAlignment(qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter)
        self._textEditWgt.setLineWrapMode(qtCore.QTextEdit.NoWrap)
        self._textEditWgt.setLineWrapColumnOrWidth(0)

        self._filterLineWgt.addFilterTarget(self._textEditWgt)

        # add test text
        # self._textEditWgt.setText("ABCD,EFGH,ABCDEFG\nABCD,ABC\nABC")

        # noinspection PyArgumentEqualDefault
        self._textEditWgt.setFont(
            qtCore.qtFont(size=8, family=_families[1])
        )
        #
        self._itemModel = self.CLS_gui_qt__text_brower_wgt__model(self)
        #
        self._textEditWgt.focusChanged.connect(self.itemModel()._updateUiEnterState)
        self._textEditWgt.entryChanged.connect(self._entryChangedEmit)
        #
        self._textEditWgt.verticalScrollBar().valueChanged.connect(self.itemModel()._updateCounter)
