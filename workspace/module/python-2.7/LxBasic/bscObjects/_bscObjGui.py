# coding:utf-8
from .. import bscCfg, bscMtdCore

from ..bscMethods import _bscMtdRaw, _bscMtdFile


class ProgressWindow(bscMtdCore.Mtd_BscUtility):
    module_fullpath_name = 'LxGui.qt.qtCommands'

    def __init__(self, explain, maxValue):
        self._progressBar = self.__loadUi(explain, maxValue)

    @classmethod
    def __loadUi(cls, explain, maxValue):
        module = bscMtdCore.Mtd_BscPython._bsc_mtd__set_python_module_load_(cls.module_fullpath_name)
        if module is not None:
            return module.setProgressWindowShow(explain, maxValue)

    def update(self, subExplain=None):
        if self._progressBar is not None:
            self._progressBar.updateProgress(subExplain)


class MessageWindow(bscMtdCore.Mtd_BscUtility):
    module_fullpath_name = 'LxGui.qt.qtCommands'

    def __init__(self, text, keyword=None):
        self._ui = self.__loadUi(text, keyword)

    @property
    def ui(self):
        return self._ui

    @classmethod
    def __loadUi(cls, text, keyword):
        module = bscMtdCore.Mtd_BscPython._bsc_mtd__set_python_module_load_(cls.module_fullpath_name)
        if module is not None:
            return module.setMessageWindowShow(text, keyword)


class TipWindow(bscMtdCore.Mtd_BscUtility):
    module_fullpath_name = 'LxGui.qt.qtCommands'

    def __init__(self, title, text):
        self._ui = self.__loadUi(title, text)

    @property
    def ui(self):
        return self._ui

    @classmethod
    def __loadUi(cls, title, text):
        module = bscMtdCore.Mtd_BscPython._bsc_mtd__set_python_module_load_(cls.module_fullpath_name)
        if module is not None:
            return module.setTipWindowShow(title, text)

    def add(self, text):
        if self._ui is not None:
            self._ui.addHtml(text)

    def addHtml(self, htmlText):
        pass


class LogWindow(bscMtdCore.Mtd_BscUtility):
    module_fullpath_name = 'LxGui.qt.qtCommands'

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
        module = bscMtdCore.Mtd_BscPython._bsc_mtd__set_python_module_load_(cls.module_fullpath_name)
        if module is not None:
            return module.getLogWindow(title)

    def add(self, *args):
        if self._ui is not None:
            if isinstance(args[0], (tuple, list)):
                for i in args:
                    self._ui.addHtml(i)
            else:
                self._ui.addHtml(args[0])
    #
    def addText(self, *args):
        if self._ui is not None:
            self._ui.addText(*args)

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
            _bscMtdFile.OsFile.write(
                self._logFileString,
                self.htmlLog
            )

    def countdownCloseUi(self, time=10):
        self.ui.setCountdownClose(time)

    def showUi(self):
        if self.ui.isHidden():
            self.ui.uiShow((10, 10), (720, 320))
        else:
            self.ui.show()

    def closeUi(self):
        self.ui.quitUi()

    def setMaxProgressValue(self, value):
        if self._ui is not None:
            self._ui.setMaxProgressValue(value)

    def updateProgress(self):
        if self._ui is not None:
            self._ui.updateProgress()


class __Autonomy__(object):
    def __init__(self):
        pass

    def write(self, out_stream):
        self._logWindow = LogWindow()
        self._logWindow.addText(
            out_stream
        )


def connectPrint():
    import sys
    bscCfg.__dict__['SYS_STDOUT'] = sys.stdout

    sys.stdout = __Autonomy__()
