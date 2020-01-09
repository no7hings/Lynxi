# coding:utf-8
from LxInterface.qt.ifBasic import _qtIfAbcWidget
#
from LxMaya.interface.ifWidgets import ifMaGroup


#
class IfScLightShelf(
    _qtIfAbcWidget.QtIfAbc_Shelf
):
    def __init__(self, mainWindow=None):
        super(IfScLightShelf, self).__init__()
        self._initIfAbcShelf()
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
class IfProductComposeShelf(_qtIfAbcWidget.QtIfAbc_Shelf):
    def __init__(self, mainWindow=None):
        super(IfProductComposeShelf, self).__init__()
        self._initIfAbcShelf()
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
