# coding:utf-8
from LxCore import lxConfigure
#
from LxUi import uiConfigure
#
from LxUi.qt import qtCore
#
from LxUi.command import uiHtml
#
from LxUi.qt.qtBasic import qtWidgetBasic
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
_families = uiConfigure.Lynxi_Ui_Family_Lis
#
none = ''


#
class QtWindow(qtWidgetBasic._QtWindowBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initWindowBasic()
        #
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#window')
        self.setDialogEnable(False)


#
class UiToolWindow(qtWidgetBasic._QtWindowBasic):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initWindowBasic()
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
class UiSubWindow(qtWidgetBasic._QtWindowBasic):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initWindowBasic()
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
class UiDialogWindow(qtWidgetBasic._QtWindowBasic):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initWindowBasic()
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self.setIcon('svg_basic@svg#dialog')
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)


#
class UiTipWindow(qtWidgetBasic._QtWindowBasic):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initWindowBasic()
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
        self._textBrower = qtWidgetBasic.QtTextBrower()
        self._textBrower.setFontSize(10)
        self.addWidget(self._textBrower)
    #
    def _initTipWindow(self):
        self._logFile = None
    #
    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = uiHtml.getHtml(datum, inuse=5)
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrower.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrower.textEdit().append(datum)
    #
    def html(self):
        return self._textBrower.textEdit().toHtml()
    #
    def addMessage(self, html):
        self.addHtml(html)
    #
    def datum(self):
        return self.html()
    #
    def setLogFile(self, osFile):
        self._logFile = osFile
    #
    def logFile(self):
        return self._logFile


#
class UiLogWindow(qtWidgetBasic._QtWindowBasic):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initWindowBasic()
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
        self._textBrower = qtWidgetBasic.QtTextBrower()
        self._textBrower.setFontSize(10)
        #
        self.addWidget(self._textBrower)
    #
    def _initLogWindow(self):
        self._logFile = None
    #
    def addHtml(self, datum, isHtml=True):
        if isHtml is False:
            # noinspection PyArgumentEqualDefault
            datum = uiHtml.getHtml(datum, inuse=5)
        #
        if isinstance(datum, str) or isinstance(datum, unicode):
            self._textBrower.textEdit().append(datum)
        elif isinstance(datum, tuple) or isinstance(datum, list):
            self._textBrower.textEdit().append(datum)
    #
    def html(self):
        return self._textBrower.textEdit().toHtml()
    #
    def addMessage(self, html):
        self.addHtml(html)
    #
    def datum(self):
        return self.html()
    #
    def setLogFile(self, osFile):
        self._logFile = osFile
    #
    def logFile(self):
        return self._logFile


#
class UiFloatWindow(qtWidgetBasic._QtWindowBasic):
    def __init__(self, parent=qtCore.getAppWindow(), *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(parent, *args, **kwargs)
        #
        self._initWindowBasic()
        #
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint), self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setupUi()
        #
        self._uiBackgroundRgba = 63, 63, 63, 127
        #
        self.viewModel().setDirection(qtCore.Vertical)
        #
        self.setDialogEnable(False)
        self.setStatusEnable(False)
        self.setMaximizeEnable(False), self.setMinimizeEnable(False)


#
class QtMessageWindow(qtWidgetBasic._QtWindowBasic):
    def __init__(self, *args, **kwargs):
        self.clsSuper = super(qtCore.QMainWindow, self)
        self.clsSuper.__init__(*args, **kwargs)
        #
        self._initWindowBasic()
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
        self.uiHeightCount = 0
        #
        self._textBrower = qtWidgetBasic.QtTextBrower()
        self._textBrower.setFontSize(10)
        self.addWidget(self._textBrower)
        self._textBrower.setEnterEnable(False)
    #
    def _initProgressWindow(self):
        self.normalWidth = 320
        self.normalHeight = 96
        #
        self.quitTime = 3000
    #
    def setUiHeightCount(self, value):
        self.uiHeightCount = lxConfigure.Ui().setMessageCount(value)
    #
    def uiShow(self, *args):
        width, height = self.windowModel().defaultSize()
        offset = 0
        #
        deskRect = qtCore.getDesktopPrimaryRect()
        maxWidth = deskRect.width()
        maxHeight = deskRect.height()
        if qtCore.getAppWindow():
            parent = qtCore.getAppWindow()
            maxWidth = parent.width()
            maxHeight = parent.height()
        #
        maxVCount = 960
        count = self.uiHeightCount
        vCount = count % maxVCount
        hCount = int(count / maxVCount)
        #
        xPos = maxWidth - width + offset - width * hCount
        yPos = maxHeight - height + offset - vCount + height
        #
        self.setGeometry(QtCore.QRect(xPos, yPos, width, height))
        #
        self.show()
    #
    def uiShow_(self):
        width = self.normalWidth
        height = self.normalHeight
        offset = 0
        #
        deskRect = qtCore.getDesktopPrimaryRect()
        maxWidth, maxHeight = deskRect.width(), deskRect.height()
        if qtCore.getAppWindow():
            parent = qtCore.getAppWindow()
            maxWidth, maxHeight = parent.width(), parent.height()
        #
        maxVCount = 960
        count = int(self.uiHeightCount)
        #
        hCount = int(count / maxVCount)
        vCount = count % maxVCount
        #
        xPos = maxWidth - width + offset - width * hCount
        yPos = maxHeight - height + offset - vCount + self.normalHeight
        #
        self.setGeometry(
            xPos, yPos,
            width, height
        )
        #
        self.show()
        #
        self.quitMethod()
    #
    def quitMethod(self):
        self.inTimer = QtCore.QTimer()
        self.inTimer.start(self.quitTime)
        #
        self.inTimer.timeout.connect(self.uiQuit)
    #
    def uiQuit(self):
        width, height = self.windowModel().defaultSize()
        self.setUiHeightCount(-height)
        #
        self.windowModel().uiQuit()
    #
    def startProgress(self, explain, maxValue):
        width, height = self.windowModel().defaultSize()
        #
        self.windowModel().setNameText(explain)
        self.setUiHeightCount(+height)
        #
        self.windowModel().setMaxProgressValue(maxValue)
    #
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
    #
    def setDatum(self, string):
        width, height = self.windowModel().defaultSize()
        #
        self._textBrower.setDatum(string)
        #
        self.setUiHeightCount(+height)
        #
        self.uiShow_()
