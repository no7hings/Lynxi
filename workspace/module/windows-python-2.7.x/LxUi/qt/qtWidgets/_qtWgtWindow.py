# coding:utf-8
from LxBasic import bscMethods

from LxScheme import shmOutput

from LxUi.qt import qtCore

from LxUi.qt.qtObjects import qtObjWidget
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
none = ''


#
class QtWindow(qtObjWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        else:
            self.clsSuper = super(QtWindow, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Window)

        self._initWindow()

    def _initWindow(self):
        self._initAbcObjWindow()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#window')
        if qtCore.LOAD_INDEX is 0:
            pass
        else:
            self.setShadowEnable(False)
            self.setMenuEnable(False)
        self.setDialogEnable(False)


#
class QtToolWindow(qtObjWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        else:
            self.clsSuper = super(QtToolWindow, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Window)

        self._initToolWindow()

    def _initToolWindow(self):
        self._initAbcObjWindow()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#window')
        if qtCore.LOAD_INDEX is 0:
            pass
        else:
            self.setShadowEnable(False)
            self.setMenuEnable(False)
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMinimizeEnable(False)


#
class QtDialogWindow(qtObjWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.clsSuper = super(QtDialogWindow, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)

        self._initDialogWindow()

    def _initDialogWindow(self):
        self._initAbcObjWindow()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#dialog')
        if qtCore.LOAD_INDEX is 0:
            pass
        else:
            self.setShadowEnable(False)
            self.setMenuEnable(False)
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)


#
class QtTipWindow(qtObjWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.clsSuper = super(QtTipWindow, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self._initTipWindow()

    def _initTipWindow(self):
        self._initAbcObjWindow()
        self._initTipWindowVar()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#dialog')
        if qtCore.LOAD_INDEX is 0:
            pass
        else:
            self.setShadowEnable(False)
            self.setMenuEnable(False)
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self.setMargins(2, 2, 2, 2)
        #
        self._textBrower = qtObjWidget._QtTextbrower(self)
        self._textBrower.setFontSize(10)
        self.addWidget(self._textBrower)

    def _initTipWindowVar(self):
        self._logFile = None

    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = self.method_html.toHtml(datum, fontColor=u'white')
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

    def setLogFile(self, fileString_):
        self._logFile = fileString_

    def logFile(self):
        return self._logFile


#
class QtLogWindow(qtObjWidget.QtAbcObj_Window):
    method_html = bscMethods.TxtHtml
    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        else:
            self.clsSuper = super(QtLogWindow, self)
            self.clsSuper.__init__(parent)

            self.setWindowFlags(QtCore.Qt.Window)

        self._initLogWindow()

    def _initLogWindow(self):
        self._initAbcObjWindow()
        self._initLogWindowVar()
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#dialog')
        if qtCore.LOAD_INDEX is 0:
            pass
        else:
            self.setShadowEnable(False)
            self.setMenuEnable(False)

        self.setMaximizeEnable(False), self.setMinimizeEnable(False)
        #
        self.setMargins(2, 2, 2, 2)
        #
        self._textBrower = qtObjWidget._QtTextbrower(self)
        self._textBrower.setFontSize(10)
        #
        self.addWidget(self._textBrower)

    def _initLogWindowVar(self):
        self._logFile = None

    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = self.method_html.toHtml(datum, fontColor=u'white')
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

    def setLogFile(self, fileString_):
        self._logFile = fileString_

    def logFile(self):
        return self._logFile


#
class QtFloatWindow(qtObjWidget.QtAbcObj_Window):
    def __init__(self, parent=qtCore.getAppWindow()):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(parent)
        else:
            self.clsSuper = super(QtFloatWindow, self)
            self.clsSuper.__init__(parent)

        self._initFloatWindow()

    def _initFloatWindow(self):
        self._initAbcObjWindow()
        #
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
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
class QtMessageWindow(qtObjWidget.QtAbcObj_Window):
    method_html = bscMethods.TxtHtml

    def __init__(self, parent=None):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(parent)
        else:
            self.clsSuper = super(QtMessageWindow, self)
            self.clsSuper.__init__(parent)

        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        self._initMessageWindow()

    def _initMessageWindow(self):
        self._initAbcObjWindow()
        self._initMessageWindowVar()
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
        self._textBrower = qtObjWidget._QtTextbrower(self)
        self._textBrower.setFontSize(10)

        self.addWidget(self._textBrower)
        self._textBrower.setEnterEnable(False)

    def _initMessageWindowVar(self):
        self._quitTimer = qtCore.CLS_timer(self)

        self._quitTime = 3000

    @staticmethod
    def _setMessageCount(value):
        shmOutput.Interface().setMessageCount(value)

    def uiShow(self, *args):
        self._messageShow()

    @staticmethod
    def _messageCount():
        return shmOutput.Interface().messageCount()

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
        self._quitTimer.start(self._quitTime)
        #
        self._quitTimer.timeout.connect(self.uiQuit)

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
            datum = self.method_html.toHtml(datum, fontColor=u'white')
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrower.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrower.textEdit().append(datum)
