# coding:utf-8
from LxBasic import bscCore

from LxBasic.bscMethods import _bscMtdRaw, _bscMtdUtility


class If_Progress(bscCore.Basic):
    module_fullpath_name = 'LxUi.qt.qtCommands'

    def __init__(self, explain, maxValue):
        self._progressBar = self.__loadUi(explain, maxValue)

    @classmethod
    def __loadUi(cls, explain, maxValue):
        module = cls._setLoadPythonModule(cls.module_fullpath_name)
        if module is not None:
            return module.setProgressWindowShow(explain, maxValue)

    def update(self, subExplain=None):
        if self._progressBar is not None:
            self._progressBar.updateProgress(subExplain)


class If_Message(bscCore.Basic):
    module_fullpath_name = 'LxUi.qt.qtCommands'

    def __init__(self, text, keyword=None):
        self._ui = self.__loadUi(text, keyword)

    @property
    def ui(self):
        return self._ui

    @classmethod
    def __loadUi(cls, text, keyword):
        module = cls._setLoadPythonModule(cls.module_fullpath_name)
        if module is not None:
            return module.setMessageWindowShow(text, keyword)


class If_Tip(bscCore.Basic):
    module_fullpath_name = 'LxUi.qt.qtCommands'

    def __init__(self, title, text):
        self._ui = self.__loadUi(title, text)

    @property
    def ui(self):
        return self._ui

    @classmethod
    def __loadUi(cls, title, text):
        module = cls._setLoadPythonModule(cls.module_fullpath_name)
        if module is not None:
            return module.setTipWindowShow(title, text)

    def add(self, text):
        if self._ui is not None:
            self._ui.addHtml(text)

    def addHtml(self, htmlText):
        pass


class If_Log(bscCore.Basic):
    module_fullpath_name = 'LxUi.qt.qtCommands'

    method_html = _bscMtdRaw.TxtHtml

    def __init__(self, title=None, logTargetFile=None):
        self._ui = self.__loadUi(title)
        if logTargetFile is not None:
            self._logFileString = logTargetFile
        else:
            self._logFileString = None

        self._taskString = None

        self._progressString = None

        self._defIdtStr = u'&nbsp;' * 4

        self._idtStr = u''

    @property
    def ui(self):
        return self._ui

    @property
    def htmlLog(self):
        return self.ui.html().encode(u'utf-8')

    @classmethod
    def __loadUi(cls, title):
        module = cls._setLoadPythonModule(cls.module_fullpath_name)
        if module is not None:
            return module.getLogWindow(title)

    def add(self, text):
        if self._ui is not None:
            self._ui.addHtml(text)

    def addStartTask(self, text, subText=None):
        self._taskString = text

        lStr = self._idtStr
        self.add(self.method_html.toHtmlSpanTime(lString=self._idtStr) + self.method_html.toHtmlSpanSuper(u'Task'))

        lStr += self._defIdtStr
        self.add(self.method_html.toHtml(u'{}Start: {}'.format(lStr, text)))

        if subText is not None:
            lStr += self._defIdtStr
            self.add(self.method_html.toHtml(lStr + subText))

        self._idtStr += self._defIdtStr

        self._setLogToFileUpdate()

    def addCompleteTask(self):
        self._idtStr = ''

        lStr = self._idtStr

        self.add(self.method_html.toHtmlSpanTime(lString=lStr) + self.method_html.toHtmlSpanSuper(u'Task', fontColor=u'green'))

        lStr += self._defIdtStr
        self.add(self.method_html.toHtml(u'{}Complete: {}'.format(lStr, self._taskString)))

        self._setLogToFileUpdate()

        self.countdownCloseUi()

    def addStartProgress(self, text, subText=None):
        self._progressString = text

        self._idtStr += self._defIdtStr

        lStr = self._idtStr
        self.add(self.method_html.toHtmlSpanTime(lString=lStr) + self.method_html.toHtmlSpanSuper(u'Progress'))

        lStr += self._defIdtStr
        self.add(self.method_html.toHtml(u'{}Start: {}'.format(lStr, text)))

        if subText is not None:
            lStr += self._defIdtStr
            self.add(self.method_html.toHtml(lStr + subText))

        self._setLogToFileUpdate()

    def addCompleteProgress(self):
        lStr = self._idtStr
        self.add(self.method_html.toHtmlSpanTime(lString=lStr) + self.method_html.toHtmlSpanSuper(u'Progress', fontColor=u'green'))

        lStr += self._defIdtStr
        self.add(self.method_html.toHtml(u'{}Complete: {}'.format(lStr, self._progressString)))

        self._idtStr = self._idtStr[:-len(self._defIdtStr)]

        self._setLogToFileUpdate()

    def addResult(self, text, subText=None):
        lStr = self._idtStr + self._defIdtStr
        self.add(self.method_html.toHtmlSpanTime(lString=lStr) + self.method_html.toHtmlSpanSuper(u'Result', fontColor=u'blue'))

        lStr += self._defIdtStr
        self.add(self.method_html.toHtml(u'{}{}'.format(lStr, text)))

        if subText is not None:
            lStr += self._defIdtStr
            self.add(self.method_html.toHtml(lStr + subText))

        self._setLogToFileUpdate()

    def addWarning(self, text, subText=None):
        lStr = self._idtStr + self._defIdtStr

        self.add(self.method_html.toHtmlSpanTime(lString=lStr) + self.method_html.toHtmlSpanSuper(u'Warning', fontColor=u'yellow'))

        lStr += self._defIdtStr
        self.add(self.method_html.toHtml(u'{}{}'.format(lStr, text)))

        if subText is not None:
            lStr += self._defIdtStr
            self.add(self.method_html.toHtml(lStr + subText))

        self._setLogToFileUpdate()

    def addError(self, text, subText=None):
        lStr = self._idtStr + self._defIdtStr

        self.add(self.method_html.toHtmlSpanTime(lString=lStr) + self.method_html.toHtmlSpanSuper(u'Error', fontColor=u'red'))

        lStr += self._defIdtStr
        self.add(self.method_html.toHtml(u'{}{}'.format(lStr, text)))

        if subText is not None:
            lStr += self._defIdtStr
            self.add(self.method_html.toHtml(lStr + subText))

        self._setLogToFileUpdate()

    def _setLogToFileUpdate(self):
        if self._logFileString is not None:
            _bscMtdUtility.OsFile.write(self._logFileString, self.htmlLog)

    def countdownCloseUi(self, time=10):
        self.ui.setCountdownClose(time)

    def showUi(self):
        self.ui.uiShow((10, 10), (720, 320))

    def closeUi(self):
        self.ui.quitUi()

    def setMaxProgressValue(self, value):
        if self._ui is not None:
            self._ui.setMaxProgressValue(value)

    def updateProgress(self):
        if self._ui is not None:
            self._ui.updateProgress()
