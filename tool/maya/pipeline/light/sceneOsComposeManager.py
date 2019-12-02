# coding=utf-8
from LxCore import lxConfigure
#
from LxCore.preset.prod import projectPr
#
from LxUi.qt import uiWidgets
#
from LxMaya.interface.ifWidgets import ifMaSceneToolUnit


#
class IfToolWindow(uiWidgets.UiToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()
        self.tool = ifMaSceneToolUnit.IfScOsComposeToolUnit()
        self.addWidget(self.tool)
        #
        self.projectName = projectPr.getMayaProjectName()
        self.sceneStage = lxConfigure.LynxiProduct_Scene_Link_Light
        #
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
        self.setDefaultSize(self.tool.UnitWidth, self.tool.UnitHeight)
        self.setNameText(self.tool.UnitTitle)


#
w = IfToolWindow()
w.uiShow()
