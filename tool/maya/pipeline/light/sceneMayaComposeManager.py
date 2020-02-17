# coding=utf-8
from LxPreset import prsMethods
#
from LxUi.qt import qtWidgets
#
from LxMaya.interface.ifWidgets import ifMaSceneToolUnit


#
class IfToolWindow(qtWidgets.QtToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()

        self.tool = ifMaSceneToolUnit.IfScMayaComposeToolUnit()
        self.addWidget(self.tool)
        #
        self.projectName = prsMethods.Project.mayaActiveName()
        self.sceneStage = prsMethods.Scene.lightLinkName()
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
        self.setDefaultSize(self.tool.panelWidth, 800)
        self.setNameText(self.tool.UnitTitle)


#
w = IfToolWindow()
w.uiShow()
