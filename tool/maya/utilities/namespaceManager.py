# coding=utf-8
from LxUi import uiCore
#
from LxUi.qt import uiWidgets
#
from LxMaya.interface.ifWidgets import ifMaUtilToolUnit
reload(ifMaUtilToolUnit)


#
class IfToolWindow(uiWidgets.UiToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()
        self.tool = ifMaUtilToolUnit.IfNamespaceManagerUnit()
        self.addWidget(self.tool)
        self.tool.setConnectObject(self)
        self.setQuitConnect(self.tool.delScriptJob)
        self.setActionData(
            [
                ('Basic',),
                ('Refresh', 'svg_basic@svg#refresh', True, self.tool.refreshMethod)
            ]
        )
        #
        self.tool.refreshMethod()
        self.setDefaultSize(self.tool.widthSet, 800)
        self.setNameText(self.tool.UnitTitle)
    @uiCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()


#
w = IfToolWindow()
w.windowShow()
