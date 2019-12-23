# coding=utf-8
from LxCore import lxConfigure
#
from LxUi import uiConfigure
#
from LxUi.qt import qtWidgets
#
from LxInterface.qt.ifWidgets import ifShelf


#
class IfDevelopWindow(qtWidgets.QtWindow):
    _Title = 'Develop Manager'
    _Version = lxConfigure.Lynxi_Scheme_Python().localVersion()
    def __init__(self):
        super(IfDevelopWindow, self).__init__()
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setDefaultSize(*uiConfigure.Lynxi_Ui_Window_Size_Default)
        #
        self.setupWindow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfDevelopShelf(self)
        self.addWidget(shelf)
