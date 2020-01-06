# coding=utf-8
from LxBasic import bscMethods

from LxCore import lxBasic
#
from LxUi.qt import qtCore
#
html_method = bscMethods.Mtd_Html
#
none = ''
#
startLabel = ''
endLabel = ''
midLabel = ''
indentLabel = '>'
#
indentStart = html_method.toHtml(u'{}'.format(startLabel), inuse=7)
indentEnd = html_method.toHtml(u'{}'.format(endLabel), inuse=7)
#
indentTimeStartIndent = html_method.toHtml(u'{0}{1}'.format(midLabel, indentLabel), inuse=7)
indentTimeEndIndent = html_method.toHtml(u'{0}{1}{1}{1}'.format(midLabel, indentLabel), inuse=7)
indentResultIndent = html_method.toHtml(u'{0}{1}{1}'.format(midLabel, indentLabel), inuse=7)
indentSubResultIndent = html_method.toHtml(u'{0}{1}{1}{1}'.format(midLabel, indentLabel), inuse=7)


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
        logHtml = html_method.toHtml(
            indentStart + u'Start Load' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % html_method.toHtmlSpanTime(inuse=4),
            inuse=2
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteLoadMessage(win):
    if win:
        logHtml = html_method.toHtml(
            indentEnd + u'Complete Load' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % html_method.toHtmlSpanTime(inuse=3),
            inuse=2
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartProcessMessage(win, progressExplain, progressSuper=none):
    if win:
        logHtml = html_method.toHtml(
            indentStart + u'Start Process ' + [progressExplain, progressExplain + u' ( %s ) ' % html_method.toHtmlSpan(progressSuper, inuse=6)][progressSuper != none] + u' @ %s' % lxBasic.getOsUser(),
            inuse=2
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteProcessMessage(win):
    if win:
        logHtml = html_method.toHtml(
            indentEnd + u'Complete Process' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % html_method.toHtmlSpanTime(inuse=3),
            inuse=2
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartUploadMessage(win):
    if win:
        logHtml = html_method.toHtml(
            indentStart + u'Start Upload' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % html_method.toHtmlSpanTime(inuse=4),
            inuse=2
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteUploadMessage(win):
    if win:
        logHtml = html_method.toHtml(
            indentEnd + u'Complete Upload' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % html_method.toHtmlSpanTime(inuse=3),
            inuse=2
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
        stepMessage = html_method.toHtml(
            indentStart + u'Progress - %s' % progressStep,
            inuse=2
        )
        win.addHtml(stepMessage)
        #
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=4) + html_method.toHtmlSpanSuper(u'Start', inuse=4)
        win.addHtml(timeHtml)
        #
        logHtml = html_method.toHtml(
            indentResultIndent + html_method.toHtmlSpan(u'Run', inuse=2) + u'Load - ' + osFile + html_method.toHtmlSpanSuper('Process', inuse=2),
            inuse=5
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteLoadFile(win):
    if win:
        timeHtml = indentTimeEndIndent + html_method.toHtmlSpanTime(inuse=3) + html_method.toHtmlSpanSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartUploadFile(win, osFile):
    if win:
        progressStep = win.progressValue()
        stepMessage = html_method.toHtml(
            indentStart + u'Progress - %s' % progressStep,
            inuse=2
        )
        win.addHtml(stepMessage)
        #
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=4) + html_method.toHtmlSpanSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = html_method.toHtml(
            indentResultIndent + html_method.toHtmlSpan(u'Run', inuse=2) + u'Upload - ' + osFile + html_method.toHtmlSpanSuper('Process', 2),
            inuse=5
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteUploadFile(win):
    if win:
        timeHtml = indentTimeEndIndent + html_method.toHtmlSpanTime(inuse=3) + html_method.toHtmlSpanSuper(u'Complete', 3)
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
        stepMessage = html_method.toHtml(
            indentStart + u'Progress - %s' % progressStep, inuse=2
        )
        win.addHtml(stepMessage)
        #
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=4) + html_method.toHtmlSpanSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = html_method.toHtml(
            indentResultIndent + html_method.toHtmlSpan(u'Run', inuse=2) + [progressExplain, progressExplain + ' ( %s ) ' % html_method.toHtmlSpan(subExplain, inuse=6)][subExplain != none] + html_method.toHtmlSpanSuper('Process', inuse=2),
            inuse=5
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteProcess(win):
    if win:
        timeHtml = indentTimeEndIndent + html_method.toHtmlSpanTime(inuse=3) + html_method.toHtmlSpanSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewFailProcess(win, progressExplain):
    if win:
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=1) + html_method.toHtmlSpanSuper(u'Fail', 1)
        win.addHtml(timeHtml)
        #
        logHtml = html_method.toHtml(indentResultIndent + progressExplain, 1)
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartSubProcess(win, progressExplain, subExplain=none):
    if win:
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=4) + html_method.toHtmlSpanSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = html_method.toHtml(
            indentResultIndent + [progressExplain, progressExplain + ' ( %s ) ' % html_method.toHtmlSpan(subExplain, inuse=6)][subExplain != none],
            inuse=2
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewCompleteSubProcess(win):
    if win:
        timeHtml = indentTimeEndIndent + html_method.toHtmlSpanTime(inuse=3) + html_method.toHtmlSpanSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewFailSubProcess(win):
    if win:
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=0) + html_method.toHtmlSpanSuper(u'Fail', 0)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewResult(win, result, subResult=none):
    if win:
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=7) + html_method.toHtmlSpanSuper(u'Result', 2)
        win.addHtml(timeHtml)
        #
        logHtml = html_method.toHtml(
            indentResultIndent + result, 5
        )
        win.addHtml(logHtml)
        if subResult:
            subLog = html_method.toHtml(
                indentSubResultIndent + subResult, 5
            )
            win.addHtml(subLog)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewError(win, error, errorSuper=none):
    if win:
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=0) + html_method.toHtmlSpanSuper(u'Error', 0)
        win.addHtml(timeHtml)
        #
        logHtml = html_method.toHtml(indentResultIndent + [error, error + html_method.toHtmlSpanSuper(errorSuper, 0)][errorSuper != none], 5)
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewWarning(win, warring, warringSuper=none):
    if win:
        timeHtml = indentTimeStartIndent + html_method.toHtmlSpanTime(inuse=1) + html_method.toHtmlSpanSuper(u'Warning', 1)
        win.addHtml(timeHtml)
        #
        logHtml = html_method.toHtml(
            indentResultIndent + [warring, warring + html_method.toHtmlSpanSuper(warringSuper, 1)][warringSuper != none], 5
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
