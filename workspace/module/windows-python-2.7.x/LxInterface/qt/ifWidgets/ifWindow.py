# coding=utf-8
from LxCore import lxScheme
#
from LxUi import uiCore
#
from LxUi.qt import qtWidgets
#
from LxInterface.qt.ifWidgets import ifShelf


#
class IfDevelopWindow(qtWidgets.QtWindow):
    _Title = 'Develop Manager'
    _Version = lxScheme.Resource().version
    def __init__(self):
        super(IfDevelopWindow, self).__init__()
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setDefaultSize(*uiCore.Lynxi_Ui_Window_Size_Default)
        #
        self.setupWindow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfDevelopShelf(self)
        self.addWidget(shelf)
