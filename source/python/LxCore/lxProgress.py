# coding=utf-8


#
def viewSubProgress(explain, maxValue):
    from LxUi import uiCore
    #
    from LxUi.qt import uiWidgets
    #
    w = uiWidgets.UiMessageWindow()
    if maxValue > 0:
        if uiCore.getAppWindow():
            parent = uiCore.getAppWindow()
            w.setParent(parent)
            #
            w.startProgress(explain, maxValue)
            w.uiShow()
    #
    return w


#
def runSubProgress(explain, methodData):
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
    maxValue = len(methodData)
    progressBar = viewSubProgress(explain, maxValue)
    # Run Method
    runMain(methodData)
