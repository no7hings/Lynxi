# coding:utf-8
from LxBasic import bscMethods

from .. import qtCore, guiQtWgtAbs

from .. guiQtModels import _guiQtMdlBasic, _guiQtMdlViewport, _guiQtMdlWindow


# noinspection PyProtectedMember
def gui_qt__mdf__set_chooseview_drop(method):
    def subFnc_(*args):
        # Class
        self = args[0]
        chooseNameLis = self.itemModel()._uiDatumTextLis
        if chooseNameLis:
            widget = QtChooseWindow(self)
            widget.setFocusProxy(self)
            widget.installEventFilter(self)
            widget.setFocus(qtCore.QtCore.Qt.PopupFocusReason)
            #
            widget.viewModel().setCurrentIndex(self.itemModel().chooseIndex())
            widget.viewModel().addItems(chooseNameLis, self.itemModel()._uiIconKeyword)
            widget.setDrop()
        #
        return method(*args)
    return subFnc_


def gui_qt__mdf__set_chooseview_event_filter(method):
    def subFnc_(*args):
        self = args[0]
        widget = args[1]
        event = args[2]
        # Filter by Widget is Press
        if type(widget) == QtChooseWindow:
            if event.type() == qtCore.QtCore.QEvent.MouseButtonPress:
                widget.close()
                #
                self.chooseChanged.emit()
            # Filter by Widget is Activate
            elif event.type() == qtCore.QtCore.QEvent.WindowDeactivate:
                widget.close()
        #
        return method(*args)
    return subFnc_


def gui_qt__mdf__set_actionview_drop(method):
    def subFnc_(*args):
        # Class
        self = args[0]
        if hasattr(self, 'actionData'):
            actionData = self.actionData
            if actionData:
                widget = QtActionViewport(self)
                widget.setFocusProxy(self)
                widget.installEventFilter(self)
                widget.setFocus(qtCore.QtCore.Qt.PopupFocusReason)
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
    return subFnc_


def gui_qt__mdf__set_actionview_event_filter(method):
    def subFnc_(*args):
        widget = args[1]
        event = args[2]
        # Filter by Widget is Press
        if type(widget) == QtActionViewport:
            if event.type() == qtCore.QtCore.QEvent.WindowDeactivate:
                widget.close()
        #
        return method(*args)
    return subFnc_


class QtIconbutton(guiQtWgtAbs.AbsGuiQtQtIconbuttonWgt):
    CLS_gui_qt__item_wgt__model = _guiQtMdlBasic.QtIconbuttonModel

    def __init__(self, iconKeywordStr=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtIconbutton, self)
            self._clsSuper.__init__(*args, **kwargs)

        self._initAbsGuiQtQtIconbuttonWgt(iconKeywordStr)

    @gui_qt__mdf__set_actionview_event_filter
    def eventFilter(self, *args):
        return False

    @gui_qt__mdf__set_actionview_drop
    def _toolActionDropAction(self):
        pass


class QtEnablebutton(guiQtWgtAbs.AbsGuiQtItemWgt):
    CLS_gui_qt__item_wgt__model = _guiQtMdlBasic.QtEnablebuttonModel

    def __init__(self, iconKeywordStr=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtEnablebutton, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtItemWgt()
        #
        self.setupUi()
        #
        if iconKeywordStr:
            self.setIcon(iconKeywordStr)
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter._gui_qt__set_image_draw_(
                self.itemModel().checkRect(),
                self.itemModel()._uiCheckIcon
            )

        # painter.end()  # for pyside2
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=24, frameHeight=24):
        self.itemModel().setIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
        #
        self.setUiSize()
    #
    def setUiSize(self):
        self.setMaximumSize(*self.itemModel().frameSize())
        self.setMinimumSize(*self.itemModel().frameSize())


class QtCheckbutton(guiQtWgtAbs.AbsGuiQtItemWgt):
    CLS_gui_qt__item_wgt__model = _guiQtMdlBasic.QtCheckbuttonModel

    def __init__(self, iconKeywordStr=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtCheckbutton, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtItemWgt()
        #
        self._overrideUi()
        #
        self.setupUi()
        #
        if iconKeywordStr:
            self.itemModel().setCheckIcon(iconKeywordStr)
        else:
            self.setUiSize()
    #
    def _overrideUi(self):
        self._wgt__name_rgba = 127, 127, 127, 255
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter._gui_qt__set_image_draw_(
                self.itemModel().checkRect(),
                self.itemModel()._uiCheckIcon
            )
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBorderRgba(self._wgt__name_rgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(
                qtCore.qtFont(size=8, weight=50, italic=self._uiFontItalic, family=qtCore._families[0])
            )
            #
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel()._gui_qt__mdl__name_str_Rect,
                textOption,
                self.itemModel().drawNameText()
            )

        # painter.end()  # for pyside2
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
        #
        self.setUiSize()
    #
    def setUiSize(self):
        w, h = self.itemModel().frameSize()
        self.setMaximumSize(166667, h)
        self.setMinimumSize(0, h)


class QtRadioCheckbutton(guiQtWgtAbs.AbsGuiQtItemWgt):
    CLS_gui_qt__item_wgt__model = _guiQtMdlBasic.QtCheckbuttonModel

    def __init__(self, iconKeywordStr=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtRadioCheckbutton, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtItemWgt()
        #
        self._overrideAttr()
        self._overrideUi()
        #
        self.setupUi()
        #
        self.setAutoExclusive(True)
        #
        if iconKeywordStr:
            self.setIcon(iconKeywordStr)
        else:
            self.setUiSize()
    #
    def _overrideAttr(self):
        pass
    #
    def _overrideUi(self):
        self._wgt__name_rgba = 127, 127, 127, 255
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # Check
        if self.itemModel().isCheckEnable() is True:
            painter._gui_qt__set_image_draw_(
                self.itemModel().checkRect(),
                self.itemModel()._uiCheckIcon
            )
        # Icon
        if self.itemModel().icon() is not None:
            painter._gui_qt__set_image_draw_(
                self.itemModel().iconRect(),
                self.itemModel().icon()
            )
        # Name
        if self.itemModel().nameText() is not None:
            painter.setBorderRgba(self._wgt__name_rgba)
            # noinspection PyArgumentEqualDefault
            painter.setFont(
                qtCore.qtFont(size=8, weight=50, italic=self._uiFontItalic, family=qtCore._families[0])
            )
            #
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            painter.drawText(
                self.itemModel()._gui_qt__mdl__name_str_Rect,
                textOption,
                self.itemModel().drawNameText()
            )

        # painter.end()  # for pyside2
    #
    def setIcon(self, iconKeywordStr, iconWidth=16, iconHeight=16, frameWidth=20, frameHeight=20):
        self.itemModel().setIcon(iconKeywordStr, iconWidth, iconHeight, frameWidth, frameHeight)
        #
        self.setUiSize()
    #
    def setUiSize(self):
        w, h = self.itemModel().frameSize()
        self.setMaximumSize(166667, h)
        self.setMinimumSize(0, h)


class QtActionIconbutton(guiQtWgtAbs.AbsGuiQtActionIconbuttonWgt):
    CLS_gui_qt__item_wgt__model = _guiQtMdlBasic.QtIconbuttonModel

    def __init__(self, iconKeywordStr=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtActionIconbutton, self)
            self._clsSuper.__init__(*args, **kwargs)

        self._initAbsGuiQtActionIconbuttonWgt(iconKeywordStr)
    # noinspection PyUnusedLocal
    @gui_qt__mdf__set_actionview_event_filter
    def eventFilter(self, *args):
        return False

    @gui_qt__mdf__set_actionview_drop
    def _toolActionDropAction(self):
        pass


class QtLineEdit_(qtCore.QLineEdit):
    entryChanged = qtCore.qtSignal()
    valueChanged = qtCore.qtSignal()
    focusChanged = qtCore.qtSignal()
    #
    focusOut = qtCore.qtSignal()
    focusIn = qtCore.qtSignal()
    #
    clicked = qtCore.qtSignal()
    doubleClicked = qtCore.qtSignal()
    def __init__(self, *args):
        self._clsSuper = super(QtLineEdit_, self)
        self._clsSuper.__init__(*args)
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
        self._clsSuper.mousePressEvent(event)
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            self.clicked.emit()
    #
    def mouseDoubleClickEvent(self, event):
        self._clsSuper.mouseDoubleClickEvent(event)
        if event.button() == qtCore.QtCore.Qt.LeftButton:
            return self.doubleClicked.emit()
    #
    def keyPressEvent(self, event):
        self._clsSuper.keyPressEvent(event)
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            pass
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            pass
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            pass
        else:
            event.ignore()
    #
    def keyReleaseEvent(self, event):
        self._clsSuper.keyReleaseEvent(event)
        if event.key() == qtCore.QtCore.Qt.Key_Control:
            pass
        elif event.key() == qtCore.QtCore.Qt.Key_Shift:
            pass
        elif event.key() == qtCore.QtCore.Qt.Key_Alt:
            pass
        else:
            event.ignore()
    #
    def wheelEvent(self, event):
        if type(self.validator()) is qtCore.QtGui.QIntValidator or type(self.validator()) is qtCore.QtGui.QDoubleValidator:
            if not self.hasFocus():
                self.setFocus(qtCore.QtCore.Qt.MouseFocusReason)
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
        self._clsSuper.focusInEvent(event)
        self.focusChanged.emit()
        self.focusIn.emit()
    #
    def focusOutEvent(self, event):
        self._clsSuper.focusOutEvent(event)
        self.focusChanged.emit()
        self.focusOut.emit()
    @gui_qt__mdf__set_actionview_event_filter
    def eventFilter(self, *args):
        return False
    #
    def contextMenuEvent(self, event):
        actions = [
            ('Basic', ),
            ('Copy#Ctrl + C', 'svg_basic/copy', self.isSelected(), self.copy),
            ('Paste#Ctrl + V', 'svg_basic/copy', True, self.paste),
            ('Cut#Ctrl + X', 'svg_basic/copy', self.isSelected(), self.cut),
            ('Extend', ),
            ('Undo#Ctrl + Z', 'svg_basic/undo', True, self.undo),
            ('Redo#Ctrl + Y', 'svg_basic/redo', True, self.redo),
            ('Select All#Ctrl + A', 'svg_basic/copy', True, self.selectAll)
        ]
        #
        if self.isReadOnly():
            actions = [
                ('Basic',),
                ('Copy#Ctrl + C', 'svg_basic/copy', True, self.copy),
                ('Extend', ),
                ('Select All#Ctrl + A', 'svg_basic/copy', True, self.selectAll)
            ]
        #
        if actions:
            self.contextMenu = QtActionViewport(self)
            self.contextMenu.setFocusProxy(self)
            self.contextMenu.installEventFilter(self)
            self.contextMenu.setActionData(actions)
            self.contextMenu.setDrop()
    #
    def paste(self):
        self._clsSuper.paste()
        self.entryChanged.emit()
    #
    def del_(self):
        self._clsSuper.del_()
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
        self.setValidator(qtCore.QtGui.QIntValidator())
    #
    def setFloatValidator(self):
        self.setValidator(qtCore.QtGui.QDoubleValidator())
    #
    def setTextValidator(self, limit):
        reg = qtCore.QtCore.QRegExp('[a-zA-Z]' + '[a-zA-Z0-9_]'*limit)
        validator = qtCore.QtGui.QRegExpValidator(reg, self)
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
        if type(self.validator()) is qtCore.QtGui.QIntValidator:
            if text:
                return int(text)
            else:
                return 0
        elif type(self.validator()) is qtCore.QtGui.QDoubleValidator:
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
            self.setFocus(qtCore.QtCore.Qt.MouseFocusReason)
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


class QtTextEdit_(qtCore.QTextEdit):
    entryChanged = qtCore.qtSignal()
    focusChanged = qtCore.qtSignal()
    filtered = qtCore.qtSignal()
    #
    focusIn = qtCore.qtSignal()
    focusOut = qtCore.qtSignal()
    #
    menuWidth = 160
    # noinspection PyArgumentList
    def __init__(self, parent=None, *args, **kwargs):
        self._clsSuper = super(QtTextEdit_, self)
        self._clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
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
                if hasattr(parent, '_setQtPressStyle'):
                    # noinspection PyCallingNonCallable
                    parent._setQtPressStyle(qtCore.HoverState)
    #
    def leaveEvent(self, event):
        if not self.hasFocus() and not self.isReadOnly():
            parent = self._parent
            if parent:
                if hasattr(parent, '_updateUiStyle'):
                    # noinspection PyCallingNonCallable
                    parent._updateUiStyle()
    #
    def keyPressEvent(self, event):
        self._clsSuper.keyPressEvent(event)
        if event.key() == qtCore.QtCore.Qt.Key_F and event.modifiers() == qtCore.QtCore.Qt.ControlModifier:
            self.filtered.emit()
        else:
            self.entryChanged.emit()
    #
    def focusInEvent(self, event):
        self._clsSuper.focusInEvent(event)
        self.focusChanged.emit()
        self.focusIn.emit()
    #
    def focusOutEvent(self, event):
        self._clsSuper.focusOutEvent(event)
        self.focusChanged.emit()
        self.focusOut.emit()

    @gui_qt__mdf__set_actionview_event_filter
    def eventFilter(self, *args):
        return False

    # noinspection PyArgumentList
    def contextMenuEvent(self, event):
        if self.isPressMenuEnable:
            actions = [
                ('Basic',),
                ('Copy#Ctrl + C', 'svg_basic/copy', True, self.copy),
                ('Paste#Ctrl + V', 'svg_basic/copy', True, self.paste),
                ('Cut#Ctrl + X', 'svg_basic/copy', True, self.cut),
                ('Extend',),
                ('Undo#Ctrl + Z', 'svg_basic/undo', True, self.undo),
                ('Redo#Ctrl + Y', 'svg_basic/redo', True, self.redo),
                ('Select All#Ctrl + A', 'svg_basic/copy', True, self.selectAll)
            ]
            #
            if self.isReadOnly():
                actions = [
                    ('Basic',),
                    ('Copy#Ctrl + C', 'svg_basic/copy', True, self.copy),
                    ('Extend',),
                    ('Select All#Ctrl + A', 'svg_basic/copy', True, self.selectAll),
                    ('Select All#Ctrl + A', 'svg_basic/copy', True, self.selectAll)
                ]
            #
            if actions:
                self.contextMenu = QtActionViewport(self)
                self.contextMenu.setFocusProxy(self)
                self.contextMenu.installEventFilter(self)
                self.contextMenu.setActionData(actions)
                self.contextMenu.setDrop()

    # noinspection PyArgumentList
    def paste(self):
        self._clsSuper.paste()
        #
        self.entryChanged.emit()
    #
    def insertFromMimeData(self, source):
        if source.hasText():
            textCursor = self.textCursor()
            textCursor.insertText(source.text())
        else:
            self._clsSuper.insertFromMimeData(source)
    #
    def setText(self, *args):
        self._clsSuper.setText(*args)
        self.entryChanged.emit()
    #
    def selectAll(self):
        self._clsSuper.selectAll()
    #
    def setTextSelect(self, *args):
        pass
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
            self.setTextInteractionFlags(qtCore.QtCore.Qt.NoTextInteraction)
    #
    def setUiStyle(self):
        self.setStyleSheet(
            'QTextEdit{background: rgba(0, 0, 0, 0) ; color: rgba(223, 223, 223, 255)}'
            'QTextEdit{border: none}'
            'QTextEdit{selection-color: rgba(255, 255, 255, 255) ; selection-background-color: rgba(0, 127, 127, 255)}'
        )
        qtCore.setScrollBarStyle(self)


class QtFilterLine(guiQtWgtAbs.AbsGuiQtFilterLineWgt):
    CLS_gui_qt__filter_line_wgt__model = _guiQtMdlBasic.QtFilterLineModel
    CLS_gui_qt__filter_line_wgt__line_edit = QtLineEdit_

    CLS_gui_qt__filter_line_wgt_iconbutton = QtIconbutton
    CLS_gui_qt__filter_line_wgt_checkbutton = QtCheckbutton

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtFilterLine, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtFilterLineWgt()


# Scroll Bar
class QtScrollBar(guiQtWgtAbs.AbsGuiQtScrollbarWgt):
    CLS_gui_qt__scrollbar_wgt_iconbutton = QtIconbutton

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtScrollBar, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtScrollbarWgt()


# choose ************************************************************************************************************* #
class QtChooseViewitem(guiQtWgtAbs.AbsGuiQtItemWgt):
    CLS_gui_qt__item_wgt__model = _guiQtMdlBasic.QtItemModel

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtChooseViewitem, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtItemWgt()
        #
        self.setupUi()


class QtChooseViewport(guiQtWgtAbs.AbsGuiQtChooseViewportWgt):
    CLS_gui_qt__view_wgt__model = _guiQtMdlViewport.QtChooseViewportModel

    CLS_gui_qt__view_wgt__scrollbar = QtScrollBar

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtChooseViewport, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtChooseViewportWgt()


class QtChooseWindow(guiQtWgtAbs.AbsGuiQtChooseWindowWgt):
    CLS_gui_qt__choose_window_wgt__model = _guiQtMdlViewport.QtChooseWindowModel

    CLS_gui_qt__choose_window_wgt__viewport = QtChooseViewport
    CLS_gui_qt__choose_window_wgt__viewitem = QtChooseViewitem

    CLS_gui_qt__choose_window_wgt__iconbutton = QtIconbutton

    CLS_gui_qt__choose_window_wgt__filter_line = QtFilterLine

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtChooseWindow, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self.setWindowFlags(qtCore.QtCore.Qt.Drawer | qtCore.QtCore.Qt.FramelessWindowHint)
        #
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        #
        self._initAbsGuiQtChooseWindowWgt()


class QtSeparateWindow(guiQtWgtAbs.AbsGuiQtWindowWgt):
    CLS_gui_qt__window_wgt__model = _guiQtMdlWindow.QtWindowModel
    CLS_gui_qt__window_wgt__iconbutton = QtIconbutton
    CLS_gui_qt__window_wgt__action_iconbutton = QtActionIconbutton

    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(parent)
        else:
            self._clsSuper = super(QtSeparateWindow, self)
            self._clsSuper.__init__(parent)
        #
        self._initAbsGuiQtWindowWgt()
        #
        self.setWindowFlags(qtCore.QtCore.Qt.Tool | qtCore.QtCore.Qt.FramelessWindowHint | qtCore.QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self._wgt__background_rgba = 63, 63, 63, 223
        #
        self.viewModel().setWidgetMargins(2, 2, 2, 2)
        #
        self.setIcon('svg_basic/subwindow', 16, 16)
        #
        self._gui_qt___gui_qt__wgt__name_font = qtCore.qtFont(size=10, weight=75, family=qtCore._families[1])
        #
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self._closeButton.setIcon('svg_basic/unseparatewindow')

    # Override
    def uiQuit(self):
        self.closed.emit()


# action ************************************************************************************************************* #
class QtActionViewitem(guiQtWgtAbs.AbsGuiQtActionViewitemWgt):
    CLS_gui_qt__action_viewitem_wgt__iconbutton = QtIconbutton

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtActionViewitem, self)
            self._clsSuper.__init__(*args, **kwargs)

        self._initAbsGuiQtActionViewitemWgt()


class QtActionViewport(guiQtWgtAbs.AbsGuiQtActionViewportWgt):
    CLS_gui_qt__action_viewport_wgt__model = _guiQtMdlBasic.QtActionViewportModel

    CLS_gui_qt__action_viewport_wgt__viewitem = QtActionViewitem

    CLS_gui_qt__action_viewport_wgt__iconbutton = QtIconbutton

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtActionViewport, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtActionViewportWgt()
