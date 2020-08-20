# coding:utf-8
from LxKit.qt import kitQtWgtAbs
#
from LxMaya.interface.ifWidgets import ifMaGroup


#
class IfScLightShelf(
    kitQtWgtAbs.AbsKitQtWgtShelf
):
    def __init__(self, mainWindow=None):
        super(IfScLightShelf, self).__init__()
        self._initAbsKitQtWgtShelf()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            group = ifMaGroup.IfScLightRigGroup(self._mainWindow)
            self.addTab(
                group, 'Light Group', 'svg_basic/lightLink', u'Light Rig Group （灯光组件）'
            )


#
class IfProductComposeShelf(kitQtWgtAbs.AbsKitQtWgtShelf):
    def __init__(self, mainWindow=None):
        super(IfProductComposeShelf, self).__init__()
        self._initAbsKitQtWgtShelf()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            group = ifMaGroup.IfScComposeGroup(self._mainWindow)
            self.addTab(
                group, 'Scene Group', 'svg_basic/lightLink', u'Light Rig Group （灯光组件）'
            )
