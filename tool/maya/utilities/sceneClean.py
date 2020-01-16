# coding=utf-8
from LxUi.qt import qtModifiers, qtWidgets

from LxMaya.interface.ifWidgets import ifMaUtilToolUnit


class IfToolWindow(qtWidgets.QtToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()

        self.windowModel().setViewportLayoutMargins(2, 2, 2, 2)
        #
        self.tool = ifMaUtilToolUnit.IfSceneCleanToolUnit()
        self.addWidget(self.tool)
        self.tool.setConnectObject(self)
        self.setQuitConnect(self.tool.delScriptJob)
        #
        self.tool.refreshMethod()
        #
        self.setDefaultSize(self.tool.panelWidth, self.tool.panelHeight)
        self.setTitle(self.tool.UnitTitle)

    @qtModifiers.mtdInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()


w = IfToolWindow()
w.windowShow()
