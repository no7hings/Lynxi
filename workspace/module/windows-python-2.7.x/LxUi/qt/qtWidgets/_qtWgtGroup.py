# coding:utf-8
from LxUi import uiCore
#
from LxUi.qt import qtCore
#
from LxUi.qt.qtObjects import qtObjWidget
#
from LxUi.qt._qtModels import _qtMdlGroup
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
_families = uiCore.Lynxi_Ui_Family_Lis


#
class QtToolboxGroup(qtObjWidget.QtAbcObj_Group):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtToolboxGroup, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initGroupBasic()
        self.__override()
        #
        self.setupUi()
    #
    def __override(self):
        self.__overrideAttr()
        self.__overrideUi()
    #
    def __overrideAttr(self):
        self._isSeparated = False
    #
    def __overrideUi(self):
        self._uiBackgroundRgba = 0, 0, 0, 0
        self._uiBorderRgba = 71, 71, 71, 255
        #
        self._uiNameRgba = 191, 191, 191, 191
        self._uiIndexRgba = 95, 95, 95, 255
        #
        self._uiNameTextFont = qtCore.qtFont(size=10, weight=75, family=_families[1])
        self._uiIndexTextFont = qtCore.qtFont(size=8, weight=50, family=_families[0])
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        #
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        painter.drawRect(self.groupModel().expandPressRect())
        # Expand
        if self.groupModel().isExpandEnable():
            painter.setDrawImage(
                self.groupModel().expandRect(),
                self.groupModel().expandIcon()
            )
        # Name
        if self.groupModel().nameText() is not None:
            painter.setFont(self._uiNameTextFont)
            rect = self.groupModel().nameTextRect()
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            if self.groupModel().filterKeyword() is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    self.groupModel().drawNameText(), self.groupModel().filterKeyword(),
                    self._uiNameRgba
                )
            else:
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(rect, textOption, self.groupModel().drawNameText())
        # Index
        if self.groupModel().indexText() is not None:
            painter.setFont(self._uiIndexTextFont)
            rect = self.groupModel().indexTextRect()
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(rect, textOption, self.groupModel().indexText())

        # painter.end()
    #
    def setupUi(self):
        self._menuButton = qtObjWidget._QtActionIconbutton('svg_basic@svg#tabMenu_h', self)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._separateButton = qtObjWidget._QtIconbutton('svg_basic@svg#separateWindow', self)
        self._separateButton.setTooltip(
            u'''点击分离 / 附着工具组面板'''
        )
        #
        self._separateWindow = qtObjWidget._QtSeparateWindow(self)
        self._separateWindow.hide()
        #
        self._groupModel = _qtMdlGroup.QtToolboxGroupModel(self)
        #
        self._separateButton.clicked.connect(self.groupModel()._separateSwitchAction)
        self._separateWindow.closed.connect(self.groupModel().setPin)


#
class QtToolbox(qtObjWidget.QtAbcObj_Group):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtToolbox, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initGroupBasic()
        self.__override()
        #
        self.setupUi()
    #
    def __override(self):
        self.__overrideUi()
    #
    def __overrideUi(self):
        pass
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Image
        if self.groupModel().isExpanded():
            if self.groupModel().image() is not None:
                painter.setDrawImage(
                    self.groupModel().imageRect(),
                    self.groupModel().image()
                )
        # Color
        if self.groupModel().isColorEnable():
            painter.setBackgroundRgba(self._uiColorBackgroundRgba)
            painter.setBorderRgba(self._uiColorBorderRgba)
            painter.drawRect(self.groupModel()._uiColorRect)
        # Expand
        if self.groupModel().isExpandEnable():
            painter.setDrawImage(
                self.groupModel().expandRect(),
                self.groupModel().expandIcon()
            )
        # Name
        if self.groupModel().nameText() is not None:
            rect = self.groupModel().nameTextRect()
            textOption = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            if self.groupModel().filterKeyword() is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    self.groupModel().drawNameText(), self.groupModel().filterKeyword(),
                    self._uiNameRgba
                )
            else:
                painter.setBorderRgba(self._uiNameRgba)
                painter.drawText(rect, textOption, self.groupModel().drawNameText())
        # Viewport
        if self.groupModel().isExpandable():
            if self.groupModel().isExpanded() is True:
                painter.setBackgroundRgba(self._uiViewportBackgroundRgba)
                painter.setBorderRgba(self._uiViewportBorderRgba)
                painter.drawRect(self.groupModel().viewportRect())
                #
                self._paintSeparators(painter)

        # painter.end()
    #
    def _paintSeparators(self, painter):
        widgetLis = self._separatorLis
        if widgetLis:
            yo = self.groupModel().viewport().y()
            width = self.width()
            side = 2
            for widget in widgetLis:
                y = widget.y()
                h = widget.height()
                #
                x_ = side
                #
                ly = y + h / 2 + yo
                lw = width - side
                if hasattr(widget, 'explain'):
                    # noinspection PyArgumentEqualDefault
                    painter.setFont(qtCore.qtFont(size=8, weight=50, family=_families[0]))
                    explain = widget.explain
                    sw = painter.fontMetrics().width(explain) + side * 2
                    sy = y + yo
                    #
                    rect = QtCore.QRect(x_, sy - 2, sw, h + 4)
                    #
                    textOption = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
                    painter.drawText(rect, textOption, explain)
                    #
                    x_ += sw + side
                #
                line = QtCore.QLine(x_, ly, lw, ly)
                painter.drawLine(line)
    #
    def setTitle(self, text, useMode=0):
        if useMode == 0:
            self.groupModel().setNameText('{} Tool(s)'.format(text))
        else:
            self.groupModel().setNameText(text)
    #
    def addWidget(self, widget, x=0, y=0, w=1, h=1):
        verticalSizePolicy = widget.sizePolicy().verticalPolicy()
        if verticalSizePolicy == qtCore.QSizePolicy.Expanding:
            self.groupModel().setExpandedSizePolicy(qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding)
            self.groupModel()._updateWidgetSizePolicy()
        #
        self.viewportLayout().addWidget(widget, x, y, w, h)
    #
    def setUiData(self, dic):
        self._uiDatumDic = dic
    #
    def setInfo(self, uiData, key, widget):
        widthSet, xPos, yPos, width, height, explain = uiData[key]
        if widthSet is not None:
            if hasattr(widget, 'setWidth'):
                widget.setWidth(widthSet)
            elif hasattr(widget, 'setNameTextWidth'):
                widget.setNameTextWidth(widthSet)
        if hasattr(widget, 'setNameText'):
            if isinstance(explain, str) or isinstance(explain, unicode):
                widget.setNameText(explain)
            elif isinstance(explain, tuple) or isinstance(explain, list):
                enExplain, cnExplain = explain
                widget.setNameText(cnExplain)
        #
        self.addWidget(widget, xPos, yPos, width, height)
    #
    def setButton(self, uiData, key, widget):
        subUiData = uiData[key]
        widthSet, xPos, yPos, width, height, explain = subUiData[:6]
        if hasattr(widget, 'setNameText'):
            if isinstance(explain, str) or isinstance(explain, unicode):
                widget.setNameText(explain)
            elif isinstance(explain, tuple) or isinstance(explain, list):
                enExplain, cnExplain = explain
                widget.setNameText(cnExplain)
        if len(subUiData) == 7:
            iconKeyword = subUiData[6]
            if hasattr(widget, 'setIcon'):
                widget.setIcon(iconKeyword)
        #
        self.addWidget(widget, xPos,  yPos, width, height)
    #
    def setTool(self, uiData, widget):
        widthSet, xPos, yPos, width, height, explain = uiData
        if explain:
            widget.setNameText(explain)
        self.addWidget(widget, xPos,  yPos, width, height)
    #
    def setSeparators(self, uiData):
        self._separatorLis = []
        #
        titleDic = {}
        yPosLis = []
        widthLis = []
        for k, v in uiData.items():
            if isinstance(v, tuple) or isinstance(v, list):
                yPosition = v[1]
                width = v[4]
                yPosLis.append(yPosition)
                widthLis.append(width)
            elif isinstance(v, str) or isinstance(v, unicode):
                titleDic[k] = v
        #
        if yPosLis:
            maxValue = max(yPosLis)
            w = max(widthLis)
            for i in range(0, maxValue):
                if i not in yPosLis:
                    widget = qtCore.QWidget_()
                    widget.setMaximumHeight(8), widget.setMinimumHeight(8)
                    if i in titleDic:
                        widget.explain = titleDic[i]
                    #
                    self.viewportLayout().addWidget(widget, i, 0, 1, w)
                    self._separatorLis.append(widget)
    #
    def addInfo(self, key, widget):
        self.setInfo(self._uiDatumDic, key, widget)
    #
    def addButton(self, key, widget):
        self.setButton(self._uiDatumDic, key, widget)
    #
    def addSeparators(self):
        self.setSeparators(self._uiDatumDic)
    #
    def addSeparator(self, x, y, w, h):
        widget = qtCore.QWidget_()
        widget.setMaximumHeight(20), widget.setMinimumHeight(20)
        self.viewportLayout().addWidget(widget, x, y, w, h)
        self._separatorLis.append(widget)
    #
    def setupUi(self):
        self._menuButton = qtObjWidget._QtActionIconbutton('svg_basic@svg#tabMenu_h', self)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._separateButton = qtObjWidget._QtIconbutton('svg_basic@svg#unpinWindow', self)
        self._separateButton.setPressable(False)
        self._separateButton.setTooltip(
            u'''点击分离 / 附着工具组面板'''
        )
        #
        self._groupModel = _qtMdlGroup.QtToolboxModel(self)


#
class _QtButtontabBar(qtObjWidget.QtAbcObj_Tabbar):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(_QtButtontabBar, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjTabbar()
        #
        self.setupUi()
    #
    def setupUi(self):
        self._viewModel = _qtMdlGroup.QtButtonTabBarModel(self)


#
class QtButtonTabgroup(qtObjWidget.QtAbcObj_Tabgroup):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtButtonTabgroup, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjTabgroup()
        #
        self.setupUi()
        #
        self.viewModel().setTabPosition(qtCore.West)
        self.viewModel().setTabSize(128, 24)
    #
    def setupUi(self):
        self._tabBar = _QtButtontabBar(self)
        self._tabBar.currentChanged.connect(self._currentChangedEmit)
        #
        self._viewModel = _qtMdlGroup.QtButtonTabGroupModel(self)
        self._viewModel.setItemClass(qtObjWidget._QtButtontab)
        #
        self._tabBar.valueChanged.connect(self.viewModel()._updateScrollButtonState)


# Button Tab Bar
class _QtShelftabBar(qtObjWidget.QtAbcObj_Tabbar):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(_QtShelftabBar, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjTabbar()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        #
        if self.viewModel()._uiTabBarPath:
            painter.setBackgroundRgba(self._uiBackgroundRgba)
            painter.setBorderRgba(self._uiBorderRgba)
            painter.drawPath(self.viewModel()._uiTabBarPath)
        if self.viewModel()._uiTabPathLis:
            for seq, i in enumerate(self.viewModel()._uiTabPathLis):
                if not seq == self.viewModel().currentItemIndex() and seq == self.viewModel().hoverItemIndex():
                    if self.viewModel().tabPosition() == qtCore.South or self.viewModel().tabPosition() == qtCore.North:
                        gradient = QtGui.QLinearGradient(self.viewModel().basicRect().topLeft(), self.viewModel().basicRect().bottomLeft())
                    else:
                        gradient = QtGui.QLinearGradient(self.viewModel().basicRect().topLeft(), self.viewModel().basicRect().topRight())
                    #
                    gradient.setColorAt(0, qtCore.CLS_color(*self._uiTabHoverBackgroundRgba))
                    gradient.setColorAt(1, qtCore.CLS_color(0, 0, 0, 0))
                    brush = qtCore.CLS_brush(gradient)
                    painter.setBrush(brush)
                    painter.setBorderRgba((0, 0, 0, 0))
                    #
                    painter.drawPath(i)

        # painter.end()
    #
    def setupUi(self):
        self._viewModel = _qtMdlGroup.QtShelfTabBarModel(self)


# Tab Shelf
class QtVShelfTabgroup(qtObjWidget.QtAbcObj_Tabgroup):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtVShelfTabgroup, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjTabgroup()
        #
        self.setupUi()
        #
        self.viewModel().setTabPosition(qtCore.West)
        self.viewModel().setTabSize(64, 32)
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Background
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        #
        painter.drawRect(self.viewModel().scrollRect())

        # painter.end()
    #
    def setupUi(self):
        self._tabBar = _QtShelftabBar(self)
        self._tabBar.currentChanged.connect(self._currentChangedEmit)
        #
        self._addButton = qtObjWidget._QtActionIconbutton('svg_basic@svg#addTab', self)
        #
        self._subScrollButton, self._addScrollButton = qtObjWidget._QtIconbutton('svg_basic@svg#vScrollSub', self), qtObjWidget._QtIconbutton('svg_basic@svg#vScrollAdd', self)
        #
        self._viewModel = _qtMdlGroup.QtShelfTabGroupModel(self)
        self._viewModel.setItemClass(qtObjWidget._QtShelftab)
        #
        self._tabBar.valueChanged.connect(self.viewModel()._updateScrollButtonState)
        self._subScrollButton.clicked.connect(self._tabBar.viewModel()._hScrollSubAction)
        self._subScrollButton.clicked.connect(self._tabBar.viewModel()._vScrollSubAction)
        self._subScrollButton.clicked.connect(self.viewModel()._updateScrollButtonState)
        self._addScrollButton.clicked.connect(self._tabBar.viewModel()._hScrollAddAction)
        self._addScrollButton.clicked.connect(self._tabBar.viewModel()._vScrollAddAction)
        self._addScrollButton.clicked.connect(self.viewModel()._updateScrollButtonState)


# Tab Group
class QtHShelfTabgroup(qtObjWidget.QtAbcObj_Tabgroup):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self.clsSuper = super(qtCore.QWidget, self)
            self.clsSuper.__init__(*args, **kwargs)
        else:
            self.clsSuper = super(QtHShelfTabgroup, self)
            self.clsSuper.__init__(*args, **kwargs)
        #
        self._initAbcObjTabgroup()
        #
        self.setupUi()
        #
        self.viewModel().setTabPosition(qtCore.North)
        self.viewModel().setTabSize(192, 24)
        #
        self._chooseTab = qtObjWidget._QtChoosetab(self)
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # fix
        # Background
        painter.setBackgroundRgba(self._uiBackgroundRgba)
        painter.setBorderRgba(self._uiBorderRgba)
        #
        painter.drawRect(self.viewModel().scrollRect())

        # painter.end()
    #
    def chooseTab(self):
        return self._chooseTab
    #
    def setupUi(self):
        self._tabBar = _QtShelftabBar(self)
        self._tabBar.currentChanged.connect(self._currentChangedEmit)
        #
        self._addButton = qtObjWidget._QtActionIconbutton('svg_basic@svg#addTab', self)
        #
        self._subScrollButton, self._addScrollButton = qtObjWidget._QtIconbutton('svg_basic@svg#vScrollSub', self), qtObjWidget._QtIconbutton('svg_basic@svg#vScrollAdd', self)
        #
        self._viewModel = _qtMdlGroup.QtShelfTabGroupModel(self)
        self._viewModel.setItemClass(qtObjWidget._QtShelftab)
        #
        self._tabBar.valueChanged.connect(self.viewModel()._updateScrollButtonState)
        self._subScrollButton.clicked.connect(self._tabBar.viewModel()._hScrollSubAction)
        self._subScrollButton.clicked.connect(self._tabBar.viewModel()._vScrollSubAction)
        self._subScrollButton.clicked.connect(self.viewModel()._updateScrollButtonState)
        self._addScrollButton.clicked.connect(self._tabBar.viewModel()._hScrollAddAction)
        self._addScrollButton.clicked.connect(self._tabBar.viewModel()._vScrollAddAction)
        self._addScrollButton.clicked.connect(self.viewModel()._updateScrollButtonState)