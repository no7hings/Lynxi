# coding:utf-8
from LxInterface.qt.ifBasic import ifWidgetBasic
#
from LxMaya.interface.ifWidgets import ifMaGroup


#
class IfScLightShelf(
    ifWidgetBasic.IfShelfBasic_
):
    def __init__(self, mainWindow=None):
        super(IfScLightShelf, self).__init__()
        self._initShelfBasic()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            group = ifMaGroup.IfScLightRigGroup(self._mainWindow)
            self.addTab(
                group, 'Light Group', 'svg_basic@svg#lightLink', u'Light Rig Group （灯光组件）'
            )


#
class IfProductComposeShelf(ifWidgetBasic.IfShelfBasic_):
    def __init__(self, mainWindow=None):
        super(IfProductComposeShelf, self).__init__()
        self._initShelfBasic()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            group = ifMaGroup.IfScComposeGroup(self._mainWindow)
            self.addTab(
                group, 'Scene Group', 'svg_basic@svg#lightLink', u'Light Rig Group （灯光组件）'
            )
