# coding=utf-8
from LxScheme import shmOutput
#
from LxGui import guiCore
#
from LxGui.qt import guiQtWidgets
#
from ..kitQtWidgets import ifShelf


#
class QtIf_DevelopWindow(guiQtWidgets.QtWindow):
    VAR_gui_qt__window_wgt__title = 'Develop Manager'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self):
        self._initWindow()

        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        #
        self.setupWindow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfDevelopShelf(self)
        self.addWidget(shelf)


class QtIf_SystemInformationWindow(guiQtWidgets.QtWindow):
    VAR_gui_qt__window_wgt__title = 'Develop Manager'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self):
        self._initWindow()

        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        #
        self.setupWindow()

    def setupWindow(self):
        pass

