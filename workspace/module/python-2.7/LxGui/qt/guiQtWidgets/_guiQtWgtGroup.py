# coding:utf-8
from . import qtCore, guiQtWgtAbs
#
from ..guiQtModels import _guiQtMdlGroup

from . import _guiQtWgtBasic, _guiQtWgtItem


#
class QtToolboxGroup(guiQtWgtAbs.AbsGuiQtGroupWgt):
    CLS_gui_qt__group_wgt__model = _guiQtMdlGroup.QtToolboxGroupModel

    CLS_gui_qt__group_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__group_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    CLS_gui_qt__group_wgt_separate_window = _guiQtWgtBasic.QtSeparateWindow

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtToolboxGroup, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtGroupWgt()
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
        self._wgt__background_rgba = 0, 0, 0, 0
        self._wgt__border_rgba = 71, 71, 71, 255
        #
        self._wgt__name_rgba = 191, 191, 191, 191
        self._uiIndexRgba = 95, 95, 95, 255
        #
        # noinspection PyArgumentEqualDefault
        self._gui_qt___gui_qt__wgt__name_font = qtCore.qtFont(size=10, weight=75, family=qtCore._families[1])
        # noinspection PyArgumentEqualDefault
        self._gui_qt__mdl__index_str_Font = qtCore.qtFont(size=8, weight=50, family=qtCore._families[0])
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2
        #
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        painter.drawRect(self.groupModel().expandPressRect())
        # Expand
        if self.groupModel().isExpandEnable():
            painter._gui_qt__set_image_draw_(
                self.groupModel().expandRect(),
                self.groupModel().expandIcon()
            )
        # Name
        if self.groupModel().nameText() is not None:
            painter.setFont(self._gui_qt___gui_qt__wgt__name_font)
            rect = self.groupModel().nameTextRect()
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            if self.groupModel().filterKeyword() is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    self.groupModel().drawNameText(), self.groupModel().filterKeyword(),
                    self._wgt__name_rgba
                )
            else:
                painter.setBorderRgba(self._wgt__name_rgba)
                painter.drawText(rect, textOption, self.groupModel().drawNameText())
        # Index
        if self.groupModel().indexText() is not None:
            painter.setFont(self._gui_qt__mdl__index_str_Font)
            rect = self.groupModel().indexTextRect()
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            painter.setBorderRgba(self._uiIndexRgba)
            painter.drawText(rect, textOption, self.groupModel().indexText())

        # painter.end()  # for pyside2
    #
    def setupUi(self):
        self._menuButton = self.CLS_gui_qt__group_wgt__action_iconbutton('svg_basic/tabmenu_h', self)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._separateButton = self.CLS_gui_qt__group_wgt__iconbutton('svg_basic/separatewindow', self)
        self._separateButton.setTooltip(
            u'''点击分离 / 附着工具组面板'''
        )
        #
        self._separateWindow = self.CLS_gui_qt__group_wgt_separate_window(self)
        self._separateWindow.hide()
        #
        self._groupModel = self.CLS_gui_qt__group_wgt__model(self)
        #
        self._separateButton.clicked.connect(self.groupModel()._separateSwitchAction)
        self._separateWindow.closed.connect(self.groupModel().setPin)


#
class QtToolbox(guiQtWgtAbs.AbsGuiQtGroupWgt):
    CLS_gui_qt__group_wgt__model = _guiQtMdlGroup.QtToolboxModel

    CLS_gui_qt__group_wgt__iconbutton = _guiQtWgtBasic.QtIconbutton
    CLS_gui_qt__group_wgt__action_iconbutton = _guiQtWgtBasic.QtActionIconbutton

    CLS_gui_qt__group_wgt_separate_window = _guiQtWgtBasic.QtSeparateWindow

    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtToolbox, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self._initAbsGuiQtGroupWgt()
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
        # painter.begin(self)  # for pyside2
        # Image
        if self.groupModel().isExpanded():
            if self.groupModel().image() is not None:
                painter._gui_qt__set_image_draw_(
                    self.groupModel().imageRect(),
                    self.groupModel().image()
                )
        # Expand
        if self.groupModel().isExpandEnable():
            painter._gui_qt__set_image_draw_(
                self.groupModel().expandRect(),
                self.groupModel().expandIcon()
            )
        # Name
        if self.groupModel().nameText() is not None:
            rect = self.groupModel().nameTextRect()
            textOption = qtCore.QtCore.Qt.AlignLeft | qtCore.QtCore.Qt.AlignVCenter
            if self.groupModel().filterKeyword() is not None:
                painter.setDrawFilterString(
                    rect,
                    False,
                    self.groupModel().drawNameText(), self.groupModel().filterKeyword(),
                    self._wgt__name_rgba
                )
            else:
                painter.setBorderRgba(self._wgt__name_rgba)
                painter.drawText(rect, textOption, self.groupModel().drawNameText())
        # Viewport
        if self.groupModel().isExpandable():
            if self.groupModel().isExpanded() is True:
                painter.setBackgroundRgba(self._uiViewportBackgroundRgba)
                painter.setBorderRgba(self._uiViewportBorderRgba)
                painter.drawRect(self.groupModel().viewportRect())
                #
                self._paintSeparators(painter)

        # painter.end()  # for pyside2
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
                    painter.setFont(qtCore.qtFont(size=8, weight=50, family=qtCore._families[0]))
                    explain = widget.explain
                    sw = painter.fontMetrics().width(explain) + side * 2
                    sy = y + yo
                    #
                    rect = qtCore.QtCore.QRect(x_, sy - 2, sw, h + 4)
                    #
                    textOption = qtCore.QtCore.Qt.AlignHCenter | qtCore.QtCore.Qt.AlignVCenter
                    painter.drawText(rect, textOption, explain)
                    #
                    x_ += sw + side
                #
                line = qtCore.QtCore.QLine(x_, ly, lw, ly)
                painter.drawLine(line)
    #
    def setTitle(self, text, useMode=0):
        if useMode == 0:
            self.groupModel().setNameString('{} Tool(s)'.format(text))
        else:
            self.groupModel().setNameString(text)
    #
    def addWidget(self, widget, x=0, y=0, w=1, h=1):
        verticalSizePolicy = widget.sizePolicy().verticalPolicy()
        if verticalSizePolicy == qtCore.QSizePolicy.Expanding:
            self.groupModel().setExpandedSizePolicy(qtCore.QSizePolicy.Expanding, qtCore.QSizePolicy.Expanding)
            self.groupModel()._updateWidgetSizePolicy()
        #
        self.viewportLayout().addWidget(widget, x, y, w, h)

    def childWidgetsCount(self):
        return self.viewportLayout().count()
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
        if hasattr(widget, 'setNameString'):
            if isinstance(explain, str) or isinstance(explain, unicode):
                widget.setNameString(explain)
            elif isinstance(explain, tuple) or isinstance(explain, list):
                enExplain, cnExplain = explain
                widget.setNameString(cnExplain)
        #
        self.addWidget(widget, xPos, yPos, width, height)
    #
    def setButton(self, uiData, key, widget):
        subUiData = uiData[key]
        widthSet, xPos, yPos, width, height, explain = subUiData[:6]
        if hasattr(widget, 'setNameString'):
            if isinstance(explain, str) or isinstance(explain, unicode):
                widget.setNameString(explain)
            elif isinstance(explain, tuple) or isinstance(explain, list):
                enExplain, cnExplain = explain
                widget.setNameString(cnExplain)
        if len(subUiData) == 7:
            iconKeywordStr = subUiData[6]
            if hasattr(widget, 'setIcon'):
                widget.setIcon(iconKeywordStr)
        #
        self.addWidget(widget, xPos,  yPos, width, height)
    #
    def setTool(self, uiData, widget):
        widthSet, xPos, yPos, width, height, explain = uiData
        if explain:
            widget.setNameString(explain)
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
        self._menuButton = self.CLS_gui_qt__group_wgt__action_iconbutton('svg_basic/tabmenu_h', self)
        self._menuButton.setTooltip(
            u'''点击显示更多操作'''
        )
        #
        self._separateButton = self.CLS_gui_qt__group_wgt__iconbutton('svg_basic/unpinwindow', self)
        self._separateButton.setPressable(False)
        self._separateButton.setTooltip(
            u'''点击分离 / 附着工具组面板'''
        )
        #
        self._groupModel = self.CLS_gui_qt__group_wgt__model(self)
