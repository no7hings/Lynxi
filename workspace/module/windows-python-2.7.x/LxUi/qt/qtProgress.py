# coding=utf-8


#
def viewSubProgress(explain, maxValue):
    from LxUi.qt import qtCore
    #
    from LxUi.qt import qtWidgets
    #
    w = qtWidgets.QtMessageWindow()
    if maxValue > 0:
        if qtCore.getAppWindow():
            parent = qtCore.getAppWindow()
            w.setParent(parent)
            #
            w.startProgress(explain, maxValue)
            w.uiShow()
    #
    return w


#
def runSubProgress(explain, methods):
    def runBranch(subData):
        enabled, subExplain, function, args = subData
        if enabled is True:
            function(*args)
        # Update Progress
        progressBar.updateProgress(subExplain)
    #
    def runMain(data):
        for i in data:
            runBranch(i)
    # View Progress
    maxValue = len(methods)
    progressBar = viewSubProgress(explain, maxValue)
    # Run Method
    runMain(methods)
