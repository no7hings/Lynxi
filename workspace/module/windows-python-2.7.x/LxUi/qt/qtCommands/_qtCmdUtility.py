# coding:utf-8
from LxBasic import bscMethods

from LxUi.qt import qtCore

from LxUi.qt import qtWidgets


def setProgressWindowShow(title, maxValue):
    w = qtWidgets.QtMessageWindow()
    w.setParent(qtCore.getAppWindow())

    if maxValue > 0:
        w.setNameText(title)
        w.startProgress(maxValue)
        w._messageShow()

    return w


def setProgressRun(title, methods):
    def branch_(subData):
        enabled, subExplain, function, args = subData
        if enabled is True:
            function(*args)

        progressBar.update(subExplain)

    def main_(data):
        for i in data:
            branch_(i)

    maxValue = len(methods)
    progressBar = setProgressWindowShow(title, maxValue)

    main_(methods)


def setMessageWindowShow(text, keyword=None):
    method_html = bscMethods.HtmlText()

    fontSize = 10

    w = qtWidgets.QtMessageWindow()
    w.setParent(qtCore.getAppWindow())

    w.setNameText('Tip(s)')

    # noinspection PyArgumentEqualDefault
    w.setDatum(
        method_html.toHtml(text, fontColor='white', fontSize=fontSize) + method_html.toHtml(keyword, fontColor='yellow', fontSize=fontSize)
    )
    w._messageShow()
    return w


def setTipWindowShow(title, text):
    w = qtWidgets.QtTipWindow()

    w.setNameText(title)

    w.addHtml(text)
    w.uiShow()
    return w


def setTextToClipboard(text):
    # noinspection PyArgumentList
    clipboard = qtCore.QApplication.clipboard()
    clipboard.setText(text)


def setExistInterfaceQuit(*args):
    lis = []
    #
    self = args[0]

    className = self.__class__.__name__
    parent = self.parent()
    if parent:
        cs = parent.children()
        if cs:
            for c in cs:
                if className == c.__class__.__name__:
                    lis.append(c)
    #
    if len(lis) > 1:
        lis[0].uiQuit()


def getLogWindow(title=None):
    existsWidgets = qtCore.getAppWidgetFilterByClassName(u'QtLogWindow')
    if existsWidgets:
        w = existsWidgets[0]
        return w
    else:
        from LxUi.qt import qtWidgets
        #
        w = qtWidgets.QtLogWindow()
        #
        if title is not None:
            w.setNameText(title)
        else:
            if w.nameText() is None:
                w.setNameText(u'Log Window')
        return w


def setLogWindowShow(title=None):
    existsWidgets = qtCore.getAppWidgetFilterByClassName(u'QtLogWindow')
    if existsWidgets:
        w = existsWidgets[0]
        w.uiShow((10, 10), (720, 320))
        return w
    else:
        from LxUi.qt import qtWidgets
        #
        w = qtWidgets.QtLogWindow()
        #
        if title is not None:
            w.setNameText(title)
        else:
            if w.nameText() is None:
                w.setNameText(u'Log Window')
        #
        w.uiShow((10, 10), (720, 320))
        return w
