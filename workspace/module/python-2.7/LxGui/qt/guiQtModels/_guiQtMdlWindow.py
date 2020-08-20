# coding:utf-8
from LxBasic import bscMethods

from ...qt import qtCore, guiQtMdlAbs


# Window Model
class QtWindowModel(guiQtMdlAbs.AbsGuiQtWindowMdl):
    CLS_gui_qt__mdl_obj__point = qtCore.QtCore.QPoint
    CLS_gui_qt__mdl_obj__line = qtCore.QtCore.QLine
    CLS_gui_qt__mdl_obj__size = qtCore.QtCore.QSize
    CLS_gui_qt__mdl_obj__rect = qtCore.QtCore.QRect
    CLS_gui_qt__mdl_obj__polygon = qtCore.QtGui.QPolygon

    def __init__(self, widget):
        self._initAbsGuiQtWindowMdl(widget)

