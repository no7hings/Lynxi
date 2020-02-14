# coding=utf-8
from LxCore import lxConfigure

from LxPreset import prsMethods
#
from LxUi.qt import qtWidgets
#
from LxMaya.interface.ifWidgets import ifMaSceneToolUnit


#
class IfToolWindow(qtWidgets.QtToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()

        self.tool = ifMaSceneToolUnit.IfScOsComposeToolUnit()
        self.addWidget(self.tool)
        #
        self.projectName = prsMethods.Project.mayaActiveName()
        self.sceneStage = lxConfigure.VAR_product_scene_link_light
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
