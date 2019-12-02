# coding=utf-8
from LxCore import lxConfigure
#
from LxUi.qt import uiWidgets
#
from LxInterface.qt.ifWidgets import ifShelf


#
class IfDevelopWindow(uiWidgets.UiWindow):
    _Title = 'Develop Manager'
    _Version = lxConfigure.Version().active()
    def __init__(self):
        super(IfDevelopWindow, self).__init__()
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setDefaultSize(*lxConfigure.LynxiWindow_Size_Default)
        #
        self.setupWindow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfDevelopShelf(self)
        self.addWidget(shelf)
