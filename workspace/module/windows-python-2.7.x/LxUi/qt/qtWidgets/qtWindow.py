# coding:utf-8
from LxBasic import bscMethods

from LxCore import lxScheme

from LxUi import uiCore

from LxUi.qt import qtCore

from LxUi.qt.qtObjects import qtAbcWidget
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
none = ''


#
class QtWindow(qtAbcWidget.QtAbcObj_Window):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjWindow()
        #
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#window')
        self.setDialogEnable(False)


#
class QtToolWindow(qtAbcWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initAbcObjWindow()
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#window')
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMinimizeEnable(False)


#
class QtSubWindow(qtAbcWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initAbcObjWindow()
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self._uiBackgroundRgba = 63, 63, 63, 223
        #
        self.windowModel().setViewportLayoutMargins(2, 2, 2, 2)
        #
        self.setIcon('svg_basic@svg#window')
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)


#
class QtDialogWindow(qtAbcWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initAbcObjWindow()
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#dialog')
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)


#
class QtTipWindow(qtAbcWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initAbcObjWindow()
        self._initTipWindow()
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#dialog')
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self.setMargins(2, 2, 2, 2)
        #
        self._textBrower = qtAbcWidget._QtTextbrower()
        self._textBrower.setFontSize(10)
        self.addWidget(self._textBrower)

    def _initTipWindow(self):
        self._logFile = None

    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = self.html_method.toHtml(datum, inuse=5)
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrower.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrower.textEdit().append(datum)

    def html(self):
        return self._textBrower.textEdit().toHtml()

    def addMessage(self, html):
        self.addHtml(html)

    def datum(self):
        return self.html()

    def setLogFile(self, osFile):
        self._logFile = osFile

    def logFile(self):
        return self._logFile


#
class QtLogWindow(qtAbcWidget.QtAbcObj_Window):
    html_method = bscMethods.Mtd_Html
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initAbcObjWindow()
        self._initLogWindow()
        #
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint), self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#dialog')
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self.setMargins(2, 2, 2, 2)
        #
        self._textBrower = qtAbcWidget._QtTextbrower()
        self._textBrower.setFontSize(10)
        #
        self.addWidget(self._textBrower)

    def _initLogWindow(self):
        self._logFile = None

    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = self.html_method.toHtml(datum, inuse=5)
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrower.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrower.textEdit().append(datum)

    def html(self):
        return self._textBrower.textEdit().toHtml()

    def addMessage(self, html):
        self.addHtml(html)

    def datum(self):
        return self.html()

    def setLogFile(self, osFile):
        self._logFile = osFile

    def logFile(self):
        return self._logFile


#
class QtFloatWindow(qtAbcWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initAbcObjWindow()
        #
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint), self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self._uiBackgroundRgba = 63, 63, 63, 127
        #
        self.viewModel().setDirection(qtCore.Vertical)
        #
        self.setIcon('svg_basic@svg#window')
        self.setDialogEnable(False)
        self.setStatusEnable(True)
        self.setMaximizeEnable(True), self.setMinimizeEnable(True)


#
class QtMessageWindow(qtAbcWidget.QtAbcObj_Window):
    html_method = bscMethods.Mtd_Html

    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjWindow()
        self._initProgressWindow()
        #
        self.setWindowFlags(QtCore.Qt.ToolTip | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self.windowModel()._isMessageWindow = True
        #
        self._uiBackgroundRgba = 63, 63, 63, 127
        #
        self.setDefaultSize(320, 96)
        #
        self.setIcon('svg_basic@svg#dialog')
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self.setMargins(2, 2, 2, 2)
        #
        self._textBrower = qtAbcWidget._QtTextbrower()
        self._textBrower.setFontSize(10)

        self.addWidget(self._textBrower)
        self._textBrower.setEnterEnable(False)

    def _initProgressWindow(self):
        self.normalWidth = 320
        self.normalHeight = 96
        #
        self.quitTime = 3000

    @staticmethod
    def _setMessageCount(value):
        lxScheme.Interface().setMessageCount(value)

    def uiShow(self, *args):
        self._messageShow()

    @staticmethod
    def _messageCount():
        return lxScheme.Interface().messageCount()

    def _messageShow(self):
        width, height = self.windowModel().defaultSize()

        if qtCore.getAppWindow():
            parent = qtCore.getAppWindow()
            parentWidth, parentHeight = parent.width(), parent.height()
            parentXPos, parentYPos = 0, 0
        else:
            deskRect = qtCore.getDesktopPrimaryRect()
            parentWidth, parentHeight = deskRect.width(), deskRect.height()
            parentXPos, parentYPos = deskRect.x(), deskRect.y()

        maxVCount = 960
        count = self._messageCount()

        hCount = int(count / maxVCount)
        vCount = count % maxVCount - height

        xPos = (parentWidth - width + parentXPos) - width * hCount
        yPos = (parentHeight - height + parentYPos) - vCount

        self.setGeometry(
            xPos, yPos,
            width, height
        )

        self.show()

    def _quitLater(self):
        self.inTimer = QtCore.QTimer()
        self.inTimer.start(self.quitTime)
        #
        self.inTimer.timeout.connect(self.uiQuit)

    def uiQuit(self):
        width, height = self.windowModel().defaultSize()
        self._setMessageCount(-height)
        #
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
        self._textBrower.setDatum(datum)
        #
        if self.windowModel().progressValue() == self.windowModel().maxProgressValue():
            self.uiQuit()

    def setDatum(self, string):
        width, height = self.windowModel().defaultSize()

        self._textBrower.setDatum(string)

        self._setMessageCount(+height)

        self._quitLater()

    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = self.html_method.toHtml(datum, inuse=5)
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrower.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrower.textEdit().append(datum)
