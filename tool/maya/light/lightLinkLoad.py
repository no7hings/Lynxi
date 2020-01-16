# coding=utf-8
from LxUi.qt import qtModifiers, qtWidgets

from LxMaya.interface.ifWidgets import ifMaSceneUnit


class IfToolWindow(qtWidgets.QtToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()

        self.tool = ifMaSceneUnit.IfScLightLinkLoadUnit()
        self.addWidget(self.tool)
        self.tool.setConnectObject(self)
        self.setQuitConnect(self.tool.delScriptJob)
        self.setActionData(
            [
                ('Basic', ),
                ('Refresh', 'svg_basic@svg#refresh', True, self.tool.refreshMethod)
            ]
        )
        #
        self.tool.refreshMethod()
        self.setDefaultSize(self.tool.UnitWidth, 800)
        self.setNameText(self.tool.UnitTitle)

    @qtModifiers.mtdInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()


w = IfToolWindow()
w.windowShow()
