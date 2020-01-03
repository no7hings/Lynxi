# coding:utf-8
from LxInterface.qt.ifWidgets import ifUnit
#
from LxMaya.method import _maUiMethod


#
class MaUiMenuBuild(_maUiMethod.Mtd_MaUiMenu):
    pass


#
class MaToolKitBuild(_maUiMethod.Mtd_MaUiControl):
    def __init__(self):
        self._controlName = self.LynxiUiName_ToolKitPanel
    #
    def currentControl(self):
        return self._toQtWidget(self._controlName)
    #
    def close(self):
        self.setControlDelete(self._controlName)
    #
    def show(self):
        self.setControlCreate(self._controlName, 400, 400)
        #
        widget = self._toQtWidget(self._controlName)
        layout = widget.layout()
        layout.setContentsMargins(0, 0, 0, 0)
        #
        children = widget.children()
        for i in children[1:]:
            i.deleteLater()
        #
        unit = ifUnit.IfToolkitUnit()
        layout.addWidget(unit)
        #
        unit.setDrawFrameEnable(True)
        unit.setMargins(2, 2, 8, 8)
        #
        unit.refreshMethod()

