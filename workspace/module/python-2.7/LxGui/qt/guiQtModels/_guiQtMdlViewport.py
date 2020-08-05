# coding:utf-8
from ...qt import guiQtMdlAbs


# Choose View
class QtChooseViewportModel(guiQtMdlAbs.Abs_QtWgtViewModel):
    def __init__(self, widget):
        self._initAbsQtWgtViewModel(widget)
        #
        self.__overrideViewAttr()
    #
    def __overrideViewAttr(self):
        self._isHScrollEnable, self._isVScrollEnable = False, True


# Choose Drop View Model
class QtChooseWindowModel(guiQtMdlAbs.Abs_GuiQtChooseWindowMdl):
    def __init__(self, *args):
        self._initAbsGuiQtChooseWindowMdl(*args)
