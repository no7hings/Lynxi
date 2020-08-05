# coding:utf-8
from .. import qtCore, guiQtWgtAbs

from ..guiQtModels import _guiQtMdlValueitem

from . import _guiQtWgtBasic


# Choose Tab
class QtChooseTabbutton(qtCore.QWidget):
    CLS_gui_qt__valueitem_wgt__model = _guiQtMdlValueitem.QtChooseTabbuttonModel

    CLS_gui_qt__valueitem_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton

    chooseChanged = qtCore.qtSignal()

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtChooseTabbutton, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsQtWgtChoosetab()

    def _initAbsQtWgtChoosetab(self):
        self.setAttribute(qtCore.QtCore.Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        # noinspection PyArgumentEqualDefault
        self.setFont(qtCore.qtFont(size=10, weight=50, family=qtCore._families[2]))
        #
        self._initUiVar()
        #
        self.setupUi()

    def _initUiVar(self):
        self._uiDatumRgba = 191, 191, 191, 255

    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHint(painter.Antialiasing)
        painter.setFont(self.font())
        if self.itemModel().datumText() is not None:
            rect = self.itemModel().datumRect()
            textOption = qtCore.QtCore.Qt.AlignHCenter | qtCore.QtCore.Qt.AlignVCenter
            painter.setBorderRgba(self._uiDatumRgba)
            painter.drawText(
                rect,
                textOption,
                self.itemModel().drawDatumText()
            )

        # painter.end()  # for pyside2

    def resizeEvent(self, event):
        if self.itemModel()._isSizeChanged():
            self.itemModel().update()

    @_guiQtWgtBasic.gui_qt__mdf__set_chooseview_event_filter
    def eventFilter(self, *args):
        return False

    @_guiQtWgtBasic.gui_qt__mdf__set_chooseview_drop
    def _chooseDropAction(self):
        pass

    def setDatumLis(self, lis):
        self.itemModel().setDatumLis(lis)

    def setExtendDatumDic(self, dic):
        self.itemModel().setExtendDatumDic(dic)

    def setDefaultDatum(self, datum):
        self.itemModel().setDefaultDatum(datum)

    def setChoose(self, string):
        self.itemModel().setChoose(string)

    def setChooseIndex(self, index):
        self.itemModel().setChooseIndex(index)

    def chooseIndex(self):
        return self.itemModel().chooseIndex()

    def setChooseClear(self):
        pass

    def datum(self):
        return self.itemModel().datum()

    def datumText(self):
        return self.itemModel().datumText()

    def setIcon(self, *args, **kwargs):
        self.itemModel().setIcon(*args, **kwargs)

    def itemModel(self):
        return self._itemModel

    def setupUi(self):
        self._chooseButton = self.CLS_gui_qt__valueitem_wgt__iconbutton('svg_basic/choose', self)
        self._chooseButton.setTooltip(
            u'1.左键点击：查看/选择更多选项\r\n2.中键滚动：向上/向下选择'
        )
        self._chooseButton.clicked.connect(self._chooseDropAction)
        #
        self._itemModel = self.CLS_gui_qt__valueitem_wgt__model(self)
        #
        self._chooseButton.upScrolled.connect(self._itemModel._chooseScrollUpAction)
        self._chooseButton.downScrolled.connect(self._itemModel._chooseScrollDownAction)

