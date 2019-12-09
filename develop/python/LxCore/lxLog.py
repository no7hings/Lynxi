# coding=utf-8
from LxCore import lxBasic
#
from LxUi.qt import qtCore
from LxUi.command import uiHtml

#
none = ''


startLabel = ''
endLabel = ''
midLabel = ''
indentLabel = '>'
#
indentStart = uiHtml.getHtml(u'{}'.format(startLabel), inuse=7)
indentEnd = uiHtml.getHtml(u'{}'.format(endLabel), inuse=7)
#
indentTimeStartIndent = uiHtml.getHtml(u'{0}{1}'.format(midLabel, indentLabel), inuse=7)
indentTimeEndIndent = uiHtml.getHtml(u'{0}{1}{1}{1}'.format(midLabel, indentLabel), inuse=7)
indentResultIndent = uiHtml.getHtml(u'{0}{1}{1}'.format(midLabel, indentLabel), inuse=7)
indentSubResultIndent = uiHtml.getHtml(u'{0}{1}{1}{1}'.format(midLabel, indentLabel), inuse=7)


#
def viewLogWin_(title=None):
    existsWin = qtCore.lxGetLogWin()
    if existsWin:
        existsWin.uiShow((10, 10), (720, 320))
        return existsWin
    else:
        from LxUi.qt import qtWidgets
        #
        win = qtWidgets.UiLogWindow()
        #
        if title:
            win.setNameText(title)
        else:
            win.setNameText('Log Window')
        #
        win.uiShow((10, 10), (720, 320))
        return win


#
def logWin_(title=None):
    from LxUi import qtCore
    existsWin = qtCore.lxGetLogWin()
    if existsWin:
        return existsWin
    else:
        from LxUi.qt import qtWidgets
        #
        win = qtWidgets.UiLogWindow()
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
        logHtml = uiHtml.getHtml(
            indentStart + u'Start Load' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % uiHtml.getHtmlTime(inuse=4),
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
        logHtml = uiHtml.getHtml(
            indentEnd + u'Complete Load' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % uiHtml.getHtmlTime(inuse=3),
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
        logHtml = uiHtml.getHtml(
            indentStart + u'Start Process ' + [progressExplain, progressExplain + u' ( %s ) ' % uiHtml.getHtmlString(progressSuper, inuse=6)][progressSuper != none] + u' @ %s' % lxBasic.getOsUser(),
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
        logHtml = uiHtml.getHtml(
            indentEnd + u'Complete Process' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % uiHtml.getHtmlTime(inuse=3),
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
        logHtml = uiHtml.getHtml(
            indentStart + u'Start Upload' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % uiHtml.getHtmlTime(inuse=4),
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
        logHtml = uiHtml.getHtml(
            indentEnd + u'Complete Upload' + u' @ %s' % lxBasic.getOsUser() + u' ( %s )' % uiHtml.getHtmlTime(inuse=3),
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
        stepMessage = uiHtml.getHtml(
            indentStart + u'Progress - %s' % progressStep,
            inuse=2
        )
        win.addHtml(stepMessage)
        #
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=4) + uiHtml.getHtmlSuper(u'Start', inuse=4)
        win.addHtml(timeHtml)
        #
        logHtml = uiHtml.getHtml(
            indentResultIndent + uiHtml.getHtmlString(u'Run', inuse=2) + u'Load - ' + osFile + uiHtml.getHtmlSuper('Process', inuse=2),
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
        timeHtml = indentTimeEndIndent + uiHtml.getHtmlTime(inuse=3) + uiHtml.getHtmlSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartUploadFile(win, osFile):
    if win:
        progressStep = win.progressValue()
        stepMessage = uiHtml.getHtml(
            indentStart + u'Progress - %s' % progressStep,
            inuse=2
        )
        win.addHtml(stepMessage)
        #
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=4) + uiHtml.getHtmlSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = uiHtml.getHtml(
            indentResultIndent + uiHtml.getHtmlString(u'Run', inuse=2) + u'Upload - ' + osFile + uiHtml.getHtmlSuper('Process', 2),
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
        timeHtml = indentTimeEndIndent + uiHtml.getHtmlTime(inuse=3) + uiHtml.getHtmlSuper(u'Complete', 3)
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
        stepMessage = uiHtml.getHtml(
            indentStart + u'Progress - %s' % progressStep, inuse=2
        )
        win.addHtml(stepMessage)
        #
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=4) + uiHtml.getHtmlSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = uiHtml.getHtml(
            indentResultIndent + uiHtml.getHtmlString(u'Run', inuse=2) + [progressExplain, progressExplain + ' ( %s ) ' % uiHtml.getHtmlString(subExplain, inuse=6)][subExplain != none] + uiHtml.getHtmlSuper('Process', inuse=2),
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
        timeHtml = indentTimeEndIndent + uiHtml.getHtmlTime(inuse=3) + uiHtml.getHtmlSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewFailProcess(win, progressExplain):
    if win:
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=1) + uiHtml.getHtmlSuper(u'Fail', 1)
        win.addHtml(timeHtml)
        #
        logHtml = uiHtml.getHtml(indentResultIndent + progressExplain, 1)
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewStartSubProcess(win, progressExplain, subExplain=none):
    if win:
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=4) + uiHtml.getHtmlSuper(u'Start', 4)
        win.addHtml(timeHtml)
        #
        logHtml = uiHtml.getHtml(
            indentResultIndent + [progressExplain, progressExplain + ' ( %s ) ' % uiHtml.getHtmlString(subExplain, inuse=6)][subExplain != none],
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
        timeHtml = indentTimeEndIndent + uiHtml.getHtmlTime(inuse=3) + uiHtml.getHtmlSuper(u'Complete', 3)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewFailSubProcess(win):
    if win:
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=0) + uiHtml.getHtmlSuper(u'Fail', 0)
        win.addHtml(timeHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewResult(win, result, subResult=none):
    if win:
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=7) + uiHtml.getHtmlSuper(u'Result', 2)
        win.addHtml(timeHtml)
        #
        logHtml = uiHtml.getHtml(
            indentResultIndent + result, 5
        )
        win.addHtml(logHtml)
        if subResult:
            subLog = uiHtml.getHtml(
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
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=0) + uiHtml.getHtmlSuper(u'Error', 0)
        win.addHtml(timeHtml)
        #
        logHtml = uiHtml.getHtml(indentResultIndent + [error, error + uiHtml.getHtmlSuper(errorSuper, 0)][errorSuper != none], 5)
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def viewWarning(win, warring, warringSuper=none):
    if win:
        timeHtml = indentTimeStartIndent + uiHtml.getHtmlTime(inuse=1) + uiHtml.getHtmlSuper(u'Warning', 1)
        win.addHtml(timeHtml)
        #
        logHtml = uiHtml.getHtml(
            indentResultIndent + [warring, warring + uiHtml.getHtmlSuper(warringSuper, 1)][warringSuper != none], 5
        )
        win.addHtml(logHtml)
        #
        logOsFile = win.logFile()
        if logOsFile:
            setLog(win.html(), logOsFile)


#
def setLog(html, osFile):
    if html:
        lxBasic.setOsFilePathCreate(osFile)
        logOsFile = lxBasic.getLogFile(osFile)
        with open(logOsFile, 'wb') as f:
            f.writelines(html + '\r\n')
            f.close()
