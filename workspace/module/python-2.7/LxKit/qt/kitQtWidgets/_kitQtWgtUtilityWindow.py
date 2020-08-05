# coding=utf-8
from LxBasic import bscObjects

from LxScheme import shmOutput
#
from LxGui.qt import qtModifiers, guiQtWidgets, qtCore

from LxKit.qt.kitQtWidgets import _kitQtWgtUtilityShelf, ifShelf


class LynxiMainWindow(guiQtWidgets.QtFloatWindow):
    VAR_gui_qt__window_wgt__title = 'Lynxi'
    VAR_kit__window__version = shmOutput.Scheme().version

    def __init__(self, parent=qtCore.getAppWindow()):
        super(LynxiMainWindow, self).__init__(parent)

        self.setDefaultSize(480, 640)
        self.setWidgetMargins(0, 0, 0, 0)

        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)

        self.setupWindow()
        self.setupMenu()

    def windowShow(self):
        self.uiShow()

    def setupWindow(self):
        shelf = _kitQtWgtUtilityShelf.QtAppkitShelf()
        self.addWidget(shelf)

    def setupMenu(self):
        def setLogWindowOpenFnc_():
            _l = bscObjects.LogWindow()
            _l.showUi()
            bscObjects.connectPrint()

        self.setActionData(
            [
                ('Basic', ),
                ('Log Window', 'svg_basic/dialog', True, setLogWindowOpenFnc_)
            ]
        )


class LynxiToolkitWindow(guiQtWidgets.QtToolWindow):
    leftBoxWidth = 160
    #
    VAR_gui_qt__window_wgt__title = 'Toolkit'
    def __init__(self, parent=qtCore.getAppWindow()):
        super(LynxiToolkitWindow, self).__init__(parent)

        self.setDefaultSize(600, 800)
        self.setWidgetMargins(0, 0, 0, 0)
        self.widthSet = 60

        self.setNameString(self.VAR_gui_qt__window_wgt__title)

        self.setupWindow()

    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        shelf = ifShelf.IfToolKitShelf(self)
        self.addWidget(shelf)
