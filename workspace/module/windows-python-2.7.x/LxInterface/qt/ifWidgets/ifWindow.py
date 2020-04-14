# coding=utf-8
from LxScheme import shmOutput
#
from LxUi import guiCore
#
from LxUi.qt import qtWidgets
#
from LxInterface.qt.ifWidgets import ifShelf


#
class QtIf_DevelopWindow(qtWidgets.QtWindow):
    _Title = 'Develop Manager'
    _Version = shmOutput.Resource().version
    def __init__(self):
        self._initWindow()

        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        #
        self.setupWindow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfDevelopShelf(self)
        self.addWidget(shelf)


class QtIf_SystemInformationWindow(qtWidgets.QtWindow):
    _Title = 'Develop Manager'
    _Version = shmOutput.Resource().version
    def __init__(self):
        self._initWindow()

        self.setNameText(self._Title)
        self.setIndexText(self._Version)
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        #
        self.setupWindow()

    def setupWindow(self):
        pass