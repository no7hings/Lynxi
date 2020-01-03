# coding=utf-8
#
from LxUi.qt import qtWidgets, qtCore
#
from LxMaya.interface.ifWidgets import ifMaUtilToolUnit


#
class IfToolWindow(qtWidgets.QtToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()
        self.windowModel().setViewportLayoutMargins(2, 2, 2, 2)
        #
        self.tool = ifMaUtilToolUnit.IfAttributeManagerUnit()
        self.addWidget(self.tool)
        self.tool.setConnectObject(self)
        self.setQuitConnect(self.tool.delScriptJob)
        #
        self.tool.refreshMethod()
        #
        self.setDefaultSize(self.tool.UnitWidth, self.tool.UnitWidth)
        self.setTitle(self.tool.UnitTitle)
    @qtCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()


#
w = IfToolWindow()
w.windowShow()
