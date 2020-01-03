# coding=utf-8
from LxBasic import bscCore

from LxCore import lxBasic, lxCore_
#
none = ''


#
def viewMessage(message, keyword=none):
    if lxBasic.isMayaApp():
        fontSize = 10
        from LxUi.command import uiHtml

        from LxUi.qt import qtCore
        #
        from LxUi.qt import qtWidgets
        #
        w = qtWidgets.QtMessageWindow()
        if qtCore.getAppWindow():
            parent = qtCore.getAppWindow()
            w.setParent(parent)
        #
        w.setNameText('Tip(s)')
        #
        w.setDatum(
            uiHtml.getHtml(message, inuse=6, fontSize=fontSize) + uiHtml.getHtml(keyword, inuse=1, fontSize=fontSize)
        )
        return w


#
def viewTip(title, message):
    from LxUi.qt import qtWidgets
    #
    tipWin = qtWidgets.QtTipWindow()
    #
    tipWin.setNameText(title)
    tipWin.addHtml(message)
    tipWin.uiShow()
    return tipWin


#
def setAddTip(tipWin, message):
    tipWin.addHtml(message)


#
def viewTips(title, messages):
    from LxUi.qt import qtCore
    #
    from LxUi.qt import qtWidgets
    #
    tipWin = qtWidgets.QtTipWindow(parent=qtCore.getAppWindow())
    #
    tipWin.setNameText(title)
    if isinstance(messages, tuple) or isinstance(messages, list):
        [tipWin.addHtml(i) for i in messages]
    tipWin.uiShow()
    return tipWin


#
def viewTimeMethod(fn):
    def subMethod(*args, **kwargs):
        startTime = lxBasic.getOsActiveTimestamp()
        traceMessage = 'Start [ %s ] in %s' % (fn.__name__, (lxBasic.getOsActiveViewTime()))
        bscCore.Py_Message().traceResult(traceMessage)
        #
        _connectObject = fn(*args, **kwargs)
        #
        endTime = lxBasic.getOsActiveTimestamp()
        traceMessage = 'Call [ %s ] in %fs' % (fn.__name__, (endTime - startTime))
        bscCore.Py_Message().traceResult(traceMessage)
        return _connectObject
    return subMethod


#
def viewExceptionMethod(fn):
    from LxUi.command import uiHtml
    def subMethod(*args, **kw):
        # noinspection PyBroadException
        try:
            return fn(*args, **kw)
        except Exception:
            functionName = fn.__name__
            exceptionModule = uiHtml.getHtml('Python Error', 0)
            tipWin = viewTip('Exception Tip', exceptionModule)
            tipWin.addHtml(uiHtml.getHtmlTime())
            excStr = lxBasic.toExceptionString()
            #
            text = functionName + '(%s) is Error ' % ', '.join(fn.__code__.co_varnames) + excStr.split('fn(*args, **kw)')[-1]
            messages = text.split('\n')
            tipWin.addHtml(uiHtml.getHtmls(messages[0], 4))
            [tipWin.addHtml(uiHtml.getHtmls(i, 1)) for i in messages[1:-1]]
            tipWin.addHtml(uiHtml.getHtmls(u'@ %s' % lxBasic.getOsUser(), 2))
            return bscCore.Py_Log().addException(text)
    return subMethod


#
def viewConnections(connections, explain, namespaceFilter):
    from LxUi.command import uiHtml

    from LxUi.qt import qtWidgets
    #
    tipWin = qtWidgets.QtTipWindow()
    tipWin.setTitle(
        '{} Connection(s)'.format(explain)
    )
    #
    if connections:
        for i in connections:
            sourceAttr, targetAttr = i
            string = uiHtml.getHtmlConnection(sourceAttr, targetAttr, namespaceFilter)
            tipWin.addHtml(string)
    #
    tipWin.uiShow()
