# coding:utf-8
from LxGui.qt import qtCore, guiQtWgtAbs
#
from LxGui.qt.guiQtModels import _guiQtMdlTabview
#
from ..guiQtWidgets import _guiQtWgtBasic, _guiQtWgtValueitem, _guiQtWgtTabitem, _guiQtWgtItem


class _QtButtonTabbar(guiQtWgtAbs.AbsGuiQtTabbarWgt):
    CLS_gui_qt__tabbar_wgt_model = _guiQtMdlTabview.QtButtonTabbarModel

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(_QtButtonTabbar, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtTabbarWgt()
        #
        self.setupUi()
    #
    def setupUi(self):
        self._viewModel = self.CLS_gui_qt__tabbar_wgt_model(self)


#
class QtButtonTabgroup(guiQtWgtAbs.AbsGuiQtTabgroupWgt):
    CLS_gui_qt__tabgroup_wgt__model = _guiQtMdlTabview.QtButtonTabGroupModel
    CLS_gui_qt__tabgroup_wgt__tabbutton = _guiQtWgtTabitem.QtTabbutton

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtButtonTabgroup, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtTabgroupWgt()
        #
        self.setupUi()
        #
        self.viewModel().setTabPosition(qtCore.West)
        self.viewModel().setTabSize(128, 24)
    #
    def setupUi(self):
        self._tabBar = _QtButtonTabbar(self)
        self._tabBar.currentChanged.connect(self._currentChangedEmit)
        #
        self._viewModel = self.CLS_gui_qt__tabgroup_wgt__model(self)
        self._viewModel.setItemClass(
            self.CLS_gui_qt__tabgroup_wgt__tabbutton
        )
        #
        self._tabBar.valueChanged.connect(self.viewModel()._updateScrollButtonState)


# Shelf Tab Bar
class _QtShelfTabbar(guiQtWgtAbs.AbsGuiQtTabbarWgt):
    CLS_gui_qt__tabbar_wgt_model = _guiQtMdlTabview.QtShelfTabbarModel

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(_QtShelfTabbar, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtTabbarWgt()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        #
        if self.viewModel()._uiTabBarPath:
            painter.setBackgroundRgba(self._wgt__background_rgba)
            painter.setBorderRgba(self._wgt__border_rgba)
            painter.drawPath(self.viewModel()._uiTabBarPath)
        if self.viewModel()._uiTabPathLis:
            for seq, i in enumerate(self.viewModel()._uiTabPathLis):
                if not seq == self.viewModel().currentItemIndex() and seq == self.viewModel().hoverItemIndex():
                    if self.viewModel().tabPosition() == qtCore.South or self.viewModel().tabPosition() == qtCore.North:
                        gradient = qtCore.QtGui.QLinearGradient(self.viewModel().basicRect().topLeft(), self.viewModel().basicRect().bottomLeft())
                    else:
                        gradient = qtCore.QtGui.QLinearGradient(self.viewModel().basicRect().topLeft(), self.viewModel().basicRect().topRight())
                    #
                    gradient.setColorAt(0, qtCore.CLS_color(*self._uiTabHoverBackgroundRgba))
                    gradient.setColorAt(1, qtCore.CLS_color(0, 0, 0, 0))
                    brush = qtCore.CLS_brush(gradient)
                    painter.setBrush(brush)
                    painter.setBorderRgba((0, 0, 0, 0))
                    #
                    painter.drawPath(i)

        # painter.end()  # for pyside2
    #
    def setupUi(self):
        self._viewModel = self.CLS_gui_qt__tabbar_wgt_model(self)


# Shelf Tab Group
class QtVShelfTabgroup(guiQtWgtAbs.AbsGuiQtTabgroupWgt):
    CLS_gui_qt__tabgroup_wgt__model = _guiQtMdlTabview.QtShelfTabGroupModel

    CLS_gui_qt__tabgroup_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__tabgroup_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    CLS_gui_qt__tabgroup_wgt__tabbar = _QtShelfTabbar

    CLS_gui_qt__tabgroup_wgt__tabbutton = _guiQtWgtTabitem.QtShelfTabbutton

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtVShelfTabgroup, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtTabgroupWgt()
        #
        self.setupUi()
        #
        self.viewModel().setTabPosition(qtCore.West)
        self.viewModel().setTabSize(64, 32)
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # Background
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        #
        painter.drawRect(self.viewModel().scrollRect())

        # painter.end()  # for pyside2
    #
    def setupUi(self):
        self._tabBar = self.CLS_gui_qt__tabgroup_wgt__tabbar(self)
        self._tabBar.currentChanged.connect(self._currentChangedEmit)
        #
        self._addButton = self.CLS_gui_qt__tabgroup_wgt__action_iconbutton('svg_basic/addtab', self)
        #
        self._subScrollButton, self._addScrollButton = (
            self.CLS_gui_qt__tabgroup_wgt__iconbutton('svg_basic/vscrollsub', self),
            self.CLS_gui_qt__tabgroup_wgt__iconbutton('svg_basic/vscrolladd', self)
        )
        #
        self._viewModel = self.CLS_gui_qt__tabgroup_wgt__model(self)
        self._viewModel.setItemClass(self.CLS_gui_qt__tabgroup_wgt__tabbutton)
        #
        self._tabBar.valueChanged.connect(self.viewModel()._updateScrollButtonState)
        self._subScrollButton.clicked.connect(self._tabBar.viewModel()._hScrollSubAction)
        self._subScrollButton.clicked.connect(self._tabBar.viewModel()._vScrollSubAction)
        self._subScrollButton.clicked.connect(self.viewModel()._updateScrollButtonState)
        self._addScrollButton.clicked.connect(self._tabBar.viewModel()._hScrollAddAction)
        self._addScrollButton.clicked.connect(self._tabBar.viewModel()._vScrollAddAction)
        self._addScrollButton.clicked.connect(self.viewModel()._updateScrollButtonState)


# Shelf Tab Group
class QtHShelfTabgroup(guiQtWgtAbs.AbsGuiQtTabgroupWgt):
    CLS_gui_qt__tabgroup_wgt__model = _guiQtMdlTabview.QtShelfTabGroupModel

    CLS_gui_qt__tabgroup_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__tabgroup_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    CLS_gui_qt__tabgroup_wgt__tabbar = _QtShelfTabbar

    CLS_gui_qt__tabgroup_wgt__tabbutton = _guiQtWgtTabitem.QtShelfTabbutton
    CLS_gui_qt__tabgroup_wgt__choose_tabbutton = _guiQtWgtValueitem.QtChooseTabbutton

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtHShelfTabgroup, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtTabgroupWgt()
        #
        self.setupUi()
        #
        self.viewModel().setTabPosition(qtCore.North)
        self.viewModel().setTabSize(192, 24)
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        # Background
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        #
        painter.drawRect(self.viewModel().scrollRect())

        # painter.end()  # for pyside2
    #
    def chooseTab(self):
        return self._chooseTabbuttonWgtObj
    #
    def setupUi(self):
        self._tabBar = self.CLS_gui_qt__tabgroup_wgt__tabbar(self)
        self._tabBar.currentChanged.connect(self._currentChangedEmit)
        #
        self._addButton = self.CLS_gui_qt__tabgroup_wgt__action_iconbutton('svg_basic/addtab', self)
        #
        self._subScrollButton, self._addScrollButton = (
            self.CLS_gui_qt__tabgroup_wgt__iconbutton('svg_basic/vscrollsub', self),
            self.CLS_gui_qt__tabgroup_wgt__iconbutton('svg_basic/vscrolladd', self)
        )
        #
        self._viewModel = self.CLS_gui_qt__tabgroup_wgt__model(self)
        self._viewModel.setItemClass(self.CLS_gui_qt__tabgroup_wgt__tabbutton)
        #
        self._tabBar.valueChanged.connect(self.viewModel()._updateScrollButtonState)
        self._subScrollButton.clicked.connect(self._tabBar.viewModel()._hScrollSubAction)
        self._subScrollButton.clicked.connect(self._tabBar.viewModel()._vScrollSubAction)
        self._subScrollButton.clicked.connect(self.viewModel()._updateScrollButtonState)
        self._addScrollButton.clicked.connect(self._tabBar.viewModel()._hScrollAddAction)
        self._addScrollButton.clicked.connect(self._tabBar.viewModel()._vScrollAddAction)
        self._addScrollButton.clicked.connect(self.viewModel()._updateScrollButtonState)

        self._chooseTabbuttonWgtObj = self.CLS_gui_qt__tabgroup_wgt__choose_tabbutton(self)
