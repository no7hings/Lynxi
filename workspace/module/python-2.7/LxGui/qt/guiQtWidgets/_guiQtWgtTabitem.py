# coding:utf-8
from .. import qtCore, guiQtWgtAbs

from ..guiQtModels import _guiQtMdlTabitem

from ..guiQtWidgets import _guiQtWgtBasic, _guiQtWgtItem


class QtTabbutton(guiQtWgtAbs.AbsGuiQtTabitemWgt):
    CLS_gui_qt__tabitem_wgt__model = _guiQtMdlTabitem._QtButtontabModel

    CLS_gui_qt__tabitem_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__tabitem_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtTabbutton, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtTabitemWgt()
        #
        self.setupUi()
    #
    def setupUi(self):
        self._menuButton = self.CLS_gui_qt__tabitem_wgt__action_iconbutton('svg_basic/menu_tab_v', self)
        self._menuButton.setPressable(False)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._closeButton = self.CLS_gui_qt__tabitem_wgt__iconbutton(parent=self)
        self._closeButton.hide()
        self._closeButton.setIcon('svg_basic/closetab', 8, 8, 10, 10)
        #
        self._itemModel = self.CLS_gui_qt__tabitem_wgt__model(self)


class QtShelfTabbutton(guiQtWgtAbs.AbsGuiQtTabitemWgt):
    CLS_gui_qt__tabitem_wgt__model = _guiQtMdlTabitem._QtShelftabModel

    CLS_gui_qt__tabitem_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__tabitem_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtShelfTabbutton, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtTabitemWgt()
        self._overrideUi()
        #
        self.setupUi()

    def _overrideUi(self):
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 0, 0, 0, 0

    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setFont(self.font())
        # Icon
        if self.itemModel().tabPosition() == qtCore.South or self.itemModel().tabPosition() == qtCore.North:
            if self.itemModel().nameText() is not None:
                rect = self.itemModel().nameTextRect()
                textOption = qtCore.QtCore.Qt.AlignHCenter | qtCore.QtCore.Qt.AlignVCenter
                painter.setBorderRgba(self._wgt__name_rgba)
                painter.drawText(rect, textOption, self.itemModel().nameText())
        else:
            if self.itemModel().icon() is not None:
                painter._gui_qt__set_image_draw_(
                    self.itemModel().iconRect(), self.itemModel().icon()
                )

        # painter.end()  # for pyside2

    def setupUi(self):
        self._menuButton = self.CLS_gui_qt__tabitem_wgt__action_iconbutton('svg_basic/menu_d', self)
        self._menuButton.setPressable(False)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._closeButton = self.CLS_gui_qt__tabitem_wgt__iconbutton(parent=self)
        self._closeButton.hide()
        self._closeButton.setIcon('svg_basic/closetab', 8, 8, 10, 10)
        #
        self._itemModel = self.CLS_gui_qt__tabitem_wgt__model(self)
