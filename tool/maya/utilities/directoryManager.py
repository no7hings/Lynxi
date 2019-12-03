# coding=utf-8
#
from LxUi.qt import qtWidgets, qtCore
#
from LxMaya.interface.ifWidgets import ifMaUtilToolUnit
reload(ifMaUtilToolUnit)


#
class IfToolWindow(qtWidgets.UiToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()
        self.windowModel().setViewportLayoutMargins(2, 2, 2, 2)
        #
        self.tool = ifMaUtilToolUnit.IfUtilsDirectoryManagerUnit()
        #
        self.addWidget(self.tool)
        self.tool.setConnectObject(self)
        self.setQuitConnect(self.tool.delScriptJob)
        #
        self.tool.refreshMethod()
        self.setDefaultSize(self.tool.panelWidth, 800)
        self.setNameText(self.tool.UnitTitle)
    @qtCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()


#
w = IfToolWindow()
w.windowShow()
