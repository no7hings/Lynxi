# coding=utf-8
from LxCore import lxScheme
#
from LxUi import uiCore
#
from LxUi.qt import qtWidgets
#
from LxInterface.qt.ifWidgets import ifShelf


#
class QtIf_DevelopWindow(qtWidgets.QtWindow):
    _Title = 'Develop Manager'
    _Version = lxScheme.Shm_Resource().version
    def __init__(self):
        super(QtIf_DevelopWindow, self).__init__()
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


class QtIf_SystemInformationWindow(qtWidgets.QtWindow):
    _Title = 'Develop Manager'
    _Version = lxScheme.Shm_Resource().version
    def __init__(self):
        super(QtIf_SystemInformationWindow, self).__init__()
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setDefaultSize(*uiCore.Lynxi_Ui_Window_Size_Default)
        #
        self.setupWindow()

    def setupWindow(self):
        pass