# coding:utf-8
from LxBasic import bscMethods

from LxScheme import shmOutput

from .. import qtCore, guiQtWgtAbs

from ..guiQtModels import _guiQtMdlWindow

from . import _guiQtWgtBasic, _guiQtWgtItem


#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
none = ''


#
class QtWindow(guiQtWgtAbs.AbsGuiQtWindowWgt):
    CLS_gui_qt__window_wgt__model = _guiQtMdlWindow.QtWindowModel

    CLS_gui_qt__window_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__window_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(parent)
        else:
            self._clsSuper = super(QtWindow, self)
            self._clsSuper.__init__(parent)

        self.setWindowFlags(qtCore.QtCore.Qt.Window | qtCore.QtCore.Qt.FramelessWindowHint)

        self._initWindow()

    def _initWindow(self):
        self._initAbsGuiQtWindowWgt()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic/window')
        self.setDialogEnable(False)


#
class QtToolWindow(guiQtWgtAbs.AbsGuiQtWindowWgt):
    CLS_gui_qt__window_wgt__model = _guiQtMdlWindow.QtWindowModel

    CLS_gui_qt__window_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__window_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(parent)
        else:
            self._clsSuper = super(QtToolWindow, self)
            self._clsSuper.__init__(parent)

        self.setWindowFlags(qtCore.QtCore.Qt.Window | qtCore.QtCore.Qt.FramelessWindowHint)
        self._initToolWindow()

    def _initToolWindow(self):
        self._initAbsGuiQtWindowWgt()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic/window')
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMinimizeEnable(False)


#
class QtDialogWindow(guiQtWgtAbs.AbsGuiQtWindowWgt):
    CLS_gui_qt__window_wgt__model = _guiQtMdlWindow.QtWindowModel

    CLS_gui_qt__window_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__window_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(parent)
        else:
            self._clsSuper = super(QtDialogWindow, self)
            self._clsSuper.__init__(parent)

        self.setWindowFlags(qtCore.QtCore.Qt.Window | qtCore.QtCore.Qt.FramelessWindowHint | qtCore.QtCore.Qt.WindowStaysOnTopHint)
        self._initDialogWindow()

    def _initDialogWindow(self):
        self._initAbsGuiQtWindowWgt()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic/dialog')
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)


#
class QtTipWindow(guiQtWgtAbs.AbsGuiQtWindowWgt):
    CLS_gui_qt__window_wgt__model = _guiQtMdlWindow.QtWindowModel

    CLS_gui_qt__window_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__window_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(parent)
        else:
            self._clsSuper = super(QtTipWindow, self)
            self._clsSuper.__init__(parent)

        self.setWindowFlags(qtCore.QtCore.Qt.Window | qtCore.QtCore.Qt.FramelessWindowHint | qtCore.QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowModality(qtCore.QtCore.Qt.ApplicationModal)
        self._initTipWindow()

    def _initTipWindow(self):
        self._initAbsGuiQtWindowWgt()
        self._initTipWindowVar()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic/dialog')
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self.setWidgetMargins(2, 2, 2, 2)
        #
        self._textBrowerWgt = _guiQtWgtItem.QtTextbrower(self)
        self._textBrowerWgt.setFontSize(10)
        self.addWidget(self._textBrowerWgt)

    def _initTipWindowVar(self):
        self._logFile = None

    def addText(self, *args):
        self._textBrowerWgt.addText(*args)

    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = self.method_html.toHtml(datum, fontColor=u'white')
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrowerWgt.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrowerWgt.textEdit().append(datum)

    def html(self):
        return self._textBrowerWgt.textEdit().toHtml()

    def addMessage(self, html):
        self.addHtml(html)

    def datum(self):
        return self.html()

    def setLogFile(self, fileString_):
        self._logFile = fileString_

    def logFile(self):
        return self._logFile


#
class QtLogWindow(guiQtWgtAbs.AbsGuiQtWindowWgt):
    CLS_gui_qt__window_wgt__model = _guiQtMdlWindow.QtWindowModel

    CLS_gui_qt__window_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__window_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    method_html = bscMethods.TxtHtml
    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(parent)
        else:
            self._clsSuper = super(QtLogWindow, self)
            self._clsSuper.__init__(parent)

        self.setWindowFlags(qtCore.QtCore.Qt.Window | qtCore.QtCore.Qt.FramelessWindowHint)
        self._initLogWindow()
        self._initLogWindowMenu()

    def _initLogWindow(self):
        self._initAbsGuiQtWindowWgt()
        self._initLogWindowVar()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic/dialog')
        # self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self.setWidgetMargins(2, 2, 2, 2)
        #
        wgt = qtCore.QWidget_()
        self.addWidget(wgt)
        lot = qtCore.QHBoxLayout_(wgt)
        #
        self._textBrowerWgt = _guiQtWgtItem.QtTextbrower(self)
        self._textBrowerWgt.textEdit().setReadOnly(True)
        self._textBrowerWgt.setFontSize(10)
        #
        lot.addWidget(self._textBrowerWgt)

        tolWgt = qtCore.QWidget_()
        lot.addWidget(tolWgt)
        tolLot = qtCore.QVBoxLayout_(tolWgt)

        self._cleanupBtnWgt = _guiQtWgtBasic.QtIconbutton('svg_basic/cleanup')
        tolLot.addWidget(self._cleanupBtnWgt)

    def _initLogWindowVar(self):
        self._logFile = None

    def _initLogWindowMenu(self):
        def cleanupFnc_():
            self._textBrowerWgt.textEdit().clear()

        self.setActionData(
            [
                ('Basic', ),
                ('Cleanup', 'svg_basic/cleanup', True, cleanupFnc_)
            ]
        )

        self._cleanupBtnWgt.clicked.connect(cleanupFnc_)

    def addText(self, *args):
        self._textBrowerWgt.addText(*args)

    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = self.method_html.toHtml(datum, fontColor=u'white')
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrowerWgt.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrowerWgt.textEdit().append(datum)

    def html(self):
        return self._textBrowerWgt.textEdit().toHtml()

    def addMessage(self, html):
        self.addHtml(html)

    def datum(self):
        return self.html()

    def setLogFile(self, fileString_):
        self._logFile = fileString_

    def logFile(self):
        return self._logFile

    def uiQuit(self):
        from LxBasic import bscCfg
        bscCfg.sys.stdout = bscCfg.SYS_STDOUT
        self.windowModel().uiQuit()


#
class QtFloatWindow(guiQtWgtAbs.AbsGuiQtWindowWgt):
    CLS_gui_qt__window_wgt__model = _guiQtMdlWindow.QtWindowModel

    CLS_gui_qt__window_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__window_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(parent)
        else:
            self._clsSuper = super(QtFloatWindow, self)
            self._clsSuper.__init__(parent)

        self.setWindowFlags(qtCore.QtCore.Qt.Window | qtCore.QtCore.Qt.FramelessWindowHint)
        self._initQtFloatWindow()

    def _initQtFloatWindow(self):
        self._initAbsGuiQtWindowWgt()
        #
        self.setupUi()
        #
        self._wgt__background_rgba = 63, 63, 63, 127
        #
        self.viewModel().setLayoutDirection(qtCore.Horizontal)
        #
        self.setIcon('svg_basic/window')
        self.setDialogEnable(False)
        self.setStatusEnable(True)
        self.setMaximizeEnable(True), self.setMinimizeEnable(True)


#
class QtMessageWindow(guiQtWgtAbs.AbsGuiQtWindowWgt):
    CLS_gui_qt__window_wgt__model = _guiQtMdlWindow.QtWindowModel

    CLS_gui_qt__window_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__window_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    method_html = bscMethods.TxtHtml

    def __init__(self, parent=None):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(parent)

        else:
            self._clsSuper = super(QtMessageWindow, self)
            self._clsSuper.__init__(parent)

        self.setWindowFlags(qtCore.QtCore.Qt.Tool | qtCore.QtCore.Qt.FramelessWindowHint | qtCore.QtCore.Qt.WindowStaysOnTopHint)
        self._initMessageWindow()

    def _initMessageWindow(self):
        self._initAbsGuiQtWindowWgt()
        self._initMessageWindowVar()
        self._initMessageWindowAction()
        #
        self.setupUi()
        #
        self.windowModel()._isMessageWindow = True
        #
        self._wgt__background_rgba = 63, 63, 63, 127
        #
        self.setDefaultSize(320, 96)
        #
        self.setIcon('svg_basic/dialog')
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self.setWidgetMargins(2, 2, 2, 2)
        #
        self._textBrowerWgt = _guiQtWgtItem.QtTextbrower(self)
        self._textBrowerWgt.setFontSize(10)

        self.addWidget(self._textBrowerWgt)
        self._textBrowerWgt.setEnterEnable(False)

    def _initMessageWindowVar(self):
        self._quitTimer = qtCore.CLS_timer(self)

        self._quitTime = 3000

    def _initMessageWindowAction(self):
        self._quitTimer.timeout.connect(self.uiQuit)

    @staticmethod
    def _setMessageCount(value):
        shmOutput.Gui().setMessageCount(value)

    def uiShow(self, *args):
        self._messageShow()

    @staticmethod
    def _messageCount():
        return shmOutput.Gui().messageCount()

    def _messageShow(self):
        width, height = self.windowModel().defaultSize()

        if qtCore.getAppWindow():
            parent = qtCore.getAppWindow()
            parentWidth, parentHeight = parent.width(), parent.height()
            parentXPos, parentYPos = 0, 0
        else:
            desktopRect = qtCore.getDesktopPrimaryRect()
            parentWidth, parentHeight = desktopRect.width(), desktopRect.height()
            parentXPos, parentYPos = desktopRect.x(), desktopRect.y()

        maxVCount = 960
        count = self._messageCount()

        hCount = int(count / maxVCount)
        vCount = count % maxVCount - height

        xPos = (parentWidth - width + parentXPos) - width * hCount
        yPos = (parentHeight - height + parentYPos) - vCount

        # noinspection PyArgumentList
        self.setGeometry(
            xPos, yPos,
            width, height
        )

        self.show()

    def _quitLater(self):
        self._quitTimer.start(self._quitTime)

    def uiQuit(self):
        # debug must stop first
        self._quitTimer.stop()

        width, height = self.windowModel().defaultSize()
        self._setMessageCount(-height)

        self.windowModel().uiQuit()

    def startProgress(self, maxValue):
        width, height = self.windowModel().defaultSize()

        self.windowModel().setMaxProgressValue(maxValue)

        self._setMessageCount(+height)

    def updateProgress(self, subExplain=None):
        self.windowModel().updateProgress()
        #
        maxValue, value = self.windowModel().maxProgressValue(), self.windowModel().progressValue()
        #
        if subExplain is not None:
            datum = u'{} - {} / {} ( {} % )'.format(subExplain, value, maxValue, qtCore.toShowPercent(maxValue, value))
        else:
            datum = u'{} / {} ( {} % )'.format(value, maxValue, qtCore.toShowPercent(maxValue, value))
        #
        self._textBrowerWgt.setDatum(datum)
        #
        if self.windowModel().progressValue() == self.windowModel().maxProgressValue():
            self.uiQuit()

    def setDatum(self, string):
        width, height = self.windowModel().defaultSize()

        self._textBrowerWgt.setDatum(string)

        self._setMessageCount(+height)

        self._quitLater()

    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = self.method_html.toHtml(datum, fontColor=u'white')
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrowerWgt.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrowerWgt.textEdit().append(datum)
