# coding=utf-8
from LxUi import uiCore
#
from LxUi.qt import uiWidgets
#
from LxMaya.interface.ifWidgets import ifMaSceneryToolUnit
reload(ifMaSceneryToolUnit)


#
class IfToolWindow(uiWidgets.UiToolWindow):
    def __init__(self):
        super(IfToolWindow, self).__init__()
        self.windowModel().setViewportLayoutMargins(2, 2, 2, 2)
        #
        win = self
        #
        unit = ifMaSceneryToolUnit.IfScnAssemblyLoadedUnit()
        #
        win.addWidget(unit)
        unit.setConnectObject(win)
        win.setQuitConnect(unit.delScriptJob)
        #
        unit.refreshMethod()
        win.setDefaultSize(unit.panelWidth, 800)
        win.setNameText(unit.UnitTitle)
    @uiCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()


#
w = IfToolWindow()
w.windowShow()
