# coding:utf-8
from .. import qtCore, guiQtWgtAbs

from ..guiQtModels import _guiQtMdlViewitem

from . import _guiQtWgtBasic


class QtIconViewitem(guiQtWgtAbs.AbsGuiQtIconViewitemWgt):
    CLS_gui_qt__item_wgt__model = _guiQtMdlViewitem.QtIconViewitemModel

    def __init__(self, iconKeywordStr=None, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtIconViewitem, self)
            self._clsSuper.__init__(*args, **kwargs)

        self._initAbsGuiQtIconViewitemWgt(iconKeywordStr)

    @_guiQtWgtBasic.gui_qt__mdf__set_actionview_event_filter
    def eventFilter(self, *args):
        return False

    @_guiQtWgtBasic.gui_qt__mdf__set_actionview_drop
    def _toolActionDropAction(self):
        pass
