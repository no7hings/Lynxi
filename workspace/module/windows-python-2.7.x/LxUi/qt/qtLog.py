# coding=utf-8
from LxBasic import bscMethods

from LxCore import lxBasic
#
from LxUi.qt import qtCore
#
method_html = bscMethods.Mtd_Html
#
none = ''
#
_lString = ''
_indentString = '>'
#
_indent_0 = method_html.toHtml(u'{}'.format(_lString), fontColor=u'gray')
_indent_1 = method_html.toHtml(u'{0}{1}'.format(_lString, _indentString), fontColor=u'gray')
_indent_2 = method_html.toHtml(u'{0}{1}{1}{1}'.format(_lString, _indentString), fontColor=u'gray')
_indent_3 = method_html.toHtml(u'{0}{1}{1}'.format(_lString, _indentString), fontColor=u'gray')
_indent_4 = method_html.toHtml(u'{0}{1}{1}{1}'.format(_lString, _indentString), fontColor=u'gray')


#
def setLogWindowShow(title=None):
    existsWin = qtCore.getLogWindow()
    if existsWin:
        existsWin.uiShow((10, 10), (720, 320))
        return existsWin
    else:
        from LxUi.qt import qtWidgets
        #
        win = qtWidgets.QtLogWindow()
        #
        if title:
            win.setNameText(title)
        else:
            win.setNameText('Log Window')
        #
        win.uiShow((10, 10), (720, 320))
        return win


#
def getLogWindow_(title=None):
    from LxUi.qt import qtCore
    existsWin = qtCore.getLogWindow()
    if existsWin:
        return existsWin
    else:
        from LxUi.qt import qtWidgets
        #
        win = qtWidgets.QtLogWindow()
        #
        if title:
            win.setNameText(title)
        else:
            win.setNameText('Log Window')
        return win


#
def viewBatchMessage(win, message):
    if win:
        message = u'''[ %s ]''' % message
        win.addHtml(message)


# Message
def viewStartLoadMessage(win):
    if win:
        logHtml = method_html.toHtml(_indent_0 + u'Start Load' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % method_html.toHtmlSpanTime(fontColor=u'blue'), fontColor=u'orange')
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteLoadMessage(win):
    if win:
        logHtml = method_html.toHtml(
            _indent_0 + u'Complete Load' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % method_html.toHtmlSpanTime(fontColor=u'green'),
            fontColor=u'orange'
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartProcessMessage(win, progressExplain, progressSuper=none):
    if win:
        logHtml = method_html.toHtml(
            _indent_0 + u'Start Process ' + [progressExplain, progressExplain + u' ( %s ) ' % method_html.toHtmlSpan(progressSuper, fontColor=6)][progressSuper != none] + u' @ %s' % lxBasic.getOsUser(),
            fontColor=u'orange'
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteProcessMessage(win):
    if win:
        logHtml = method_html.toHtml(
            _indent_0 + u'Complete Process' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % method_html.toHtmlSpanTime(fontColor=u'green'),
            fontColor=u'orange'
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartUploadMessage(win):
    if win:
        logHtml = method_html.toHtml(
            _indent_0 + u'Start Upload' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % method_html.toHtmlSpanTime(fontColor=u'blue'),
            fontColor=u'orange'
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteUploadMessage(win):
    if win:
        logHtml = method_html.toHtml(
            _indent_0 + u'Complete Upload' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % method_html.toHtmlSpanTime(fontColor=u'green'),
            fontColor=u'orange'
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartLoadFile(win, osFile):
    if win:
        progressStep = win.progressValue()
        stepMessage = method_html.toHtml(_indent_0 + u'Progress - %s' % progressStep, fontColor=u'orange')
        win.addHtml(stepMessage)
        #
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=u'blue') + method_html.toHtmlSpanSuper(u'Start', fontColor=u'blue')
        win.addHtml(timeHtml)
        #
        logHtml = method_html.toHtml(
            _indent_3 + method_html.toHtmlSpan(u'Run', fontColor=u'orange') + u'Load - ' + osFile + method_html.toHtmlSpanSuper('Process', fontColor=u'orange'), fontColor=u'white'
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteLoadFile(win):
    if win:
        timeHtml = _indent_2 + method_html.toHtmlSpanTime(fontColor=u'green') + method_html.toHtmlSpanSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartUploadFile(win, osFile):
    if win:
        progressStep = win.progressValue()
        stepMessage = method_html.toHtml(
            _indent_0 + u'Progress - %s' % progressStep,
            fontColor=u'orange'
        )
        win.addHtml(stepMessage)
        #
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=u'blue') + method_html.toHtmlSpanSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = method_html.toHtml(_indent_3 + method_html.toHtmlSpan(u'Run', fontColor=u'orange') + u'Upload - ' + osFile + method_html.toHtmlSpanSuper('Process', 2), fontColor=u'white')
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteUploadFile(win):
    if win:
        timeHtml = _indent_2 + method_html.toHtmlSpanTime(fontColor=u'green') + method_html.toHtmlSpanSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartProcess(win, progressExplain, subExplain=none):
    if win:
        progressStep = win.progressValue()
        #
        stepMessage = method_html.toHtml(
            _indent_0 + u'Progress - %s' % progressStep, fontColor=u'orange'
        )
        win.addHtml(stepMessage)
        #
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=u'blue') + method_html.toHtmlSpanSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = method_html.toHtml(
            _indent_3 + method_html.toHtmlSpan(u'Run', fontColor=u'orange') + [progressExplain, progressExplain + ' ( %s ) ' % method_html.toHtmlSpan(subExplain, fontColor=6)][subExplain != none] + method_html.toHtmlSpanSuper('Process', fontColor=u'orange'),
            fontColor=u'white'
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteProcess(win):
    if win:
        timeHtml = _indent_2 + method_html.toHtmlSpanTime(fontColor=u'green') + method_html.toHtmlSpanSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewFailProcess(win, progressExplain):
    if win:
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=1) + method_html.toHtmlSpanSuper(u'Fail', 1)
        win.addHtml(timeHtml)
        #
        logHtml = method_html.toHtml(_indent_3 + progressExplain, 1)
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartSubProcess(win, progressExplain, subExplain=none):
    if win:
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=u'blue') + method_html.toHtmlSpanSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = method_html.toHtml(
            _indent_3 + [progressExplain, progressExplain + ' ( %s ) ' % method_html.toHtmlSpan(subExplain, fontColor=6)][subExplain != none],
            fontColor=u'orange'
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteSubProcess(win):
    if win:
        timeHtml = _indent_2 + method_html.toHtmlSpanTime(fontColor=u'green') + method_html.toHtmlSpanSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewFailSubProcess(win):
    if win:
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=0) + method_html.toHtmlSpanSuper(u'Fail', 0)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewResult(win, result, subResult=none):
    if win:
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=u'gray') + method_html.toHtmlSpanSuper(u'Result', 2)
        win.addHtml(timeHtml)
        #
        logHtml = method_html.toHtml(
            _indent_3 + result, 5
        )
        win.addHtml(logHtml)
        if subResult:
            subLog = method_html.toHtml(
                _indent_4 + subResult, 5
            )
            win.addHtml(subLog)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewError(win, error, errorSuper=none):
    if win:
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=0) + method_html.toHtmlSpanSuper(u'Error', 0)
        win.addHtml(timeHtml)
        #
        logHtml = method_html.toHtml(_indent_3 + [error, error + method_html.toHtmlSpanSuper(errorSuper, 0)][errorSuper != none], 5)
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewWarning(win, warring, warringSuper=none):
    if win:
        timeHtml = _indent_1 + method_html.toHtmlSpanTime(fontColor=1) + method_html.toHtmlSpanSuper(u'Warning', 1)
        win.addHtml(timeHtml)
        #
        logHtml = method_html.toHtml(
            _indent_3 + [warring, warring + method_html.toHtmlSpanSuper(warringSuper, 1)][warringSuper != none], 5
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def setLog(html, osFile):
    if html:
        lxBasic.setOsFileDirectoryCreate(osFile)
        logOsFile = lxBasic.getLogFile(osFile)
        with open(logOsFile, 'wb') as f:
            f.writelines(html + '\r\n')
            f.close()
