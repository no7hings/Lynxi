# coding:utf-8
from LxBasic import bscMethods

from LxUi.qt import qtCore

from LxUi.qt import qtWidgets


def setProgressWindowShow(title, maxValue):
    w = qtWidgets.QtMessageWindow()
    if maxValue > 0:
        parent = qtCore.getAppWindow()
        w.setParent(parent)

        w.setNameText(title)
        w.startProgress(maxValue)
        w._messageShow()

    return w


def setProgressRun(title, methods):
    def branch_(subData):
        enabled, subExplain, function, args = subData
        if enabled is True:
            function(*args)

        progressBar.updateProgress(subExplain)

    def main_(data):
        for i in data:
            branch_(i)

    maxValue = len(methods)
    progressBar = setProgressWindowShow(title, maxValue)

    main_(methods)


def setMessageWindowShow(text, keyword=None):
    html_method = bscMethods.Mtd_Html()

    fontSize = 10

    w = qtWidgets.QtMessageWindow()
    if qtCore.getAppWindow():
        parent = qtCore.getAppWindow()
        w.setParent(parent)

    w.setNameText('Tip(s)')

    w.setDatum(
        html_method.toHtml(text, inuse=6, fontSize=fontSize) + html_method.toHtml(keyword, inuse=1, fontSize=fontSize)
    )
    w._messageShow()
    return w


def setTipWindowShow(title, text):
    w = qtWidgets.QtTipWindow()

    w.setNameText(title)

    w.addHtml(text)
    w.uiShow()
    return w
