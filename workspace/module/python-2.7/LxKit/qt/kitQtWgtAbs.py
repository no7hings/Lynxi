# coding:utf-8
from LxBasic import bscCfg, bscMethods

from LxScheme import shmOutput

from LxPreset import prsMethods
#
from LxGui.qt import qtWidgets_, guiQtWidgets, qtCore
#
from . import kitQtObjAbs
#
none = ''


#
class AbsKitQtWgtShelf(
    guiQtWidgets.QtVShelfTabgroup,
    kitQtObjAbs.AbsKitQtShelfObj
):
    ShelfWidth = 800
    VAR_kit__qt_wgt__unit__side_width = 320
    def _initAbsKitQtWgtShelf(self):
        self._initAbsKitQtShelfObj()
        #
        self._initAbsKitQtWgtShelfAttr()
        self._initAbsKitQtWgtShelfUi()
        # Tool Box
        self.initToolBox()
        self._kit__unit__set_build_Widgets()
    #
    def _initAbsKitQtWgtShelfAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initAbsKitQtWgtShelfUi(self):
        self._mainLayout = qtCore.QVBoxLayout_(self)
        self._mainLayout.setContentsMargins(0, 0, 0, 0)
        self._mainLayout.setSpacing(0)
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
    #
    def mainLayout(self):
        return self._mainLayout
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def _kit__unit__set_build_Widgets(self):
        pass


#
class AbsKitQtWgtGroup(
    guiQtWidgets.QtHShelfTabgroup,
    kitQtObjAbs.AbsKitQtGroupObj
):
    GroupWidth = 800
    VAR_kit__qt_wgt__unit__side_width = 320
    def _initAbsKitQtWgtGroup(self):
        self._initAbsKitQtGroupObj()
        #
        self._initAbsKitQtWgtGroupAttr()
        # Tool Box
        self.initToolBox()
        self._kit__unit__set_build_Widgets()
    #
    def _initAbsKitQtWgtGroupAttr(self):
        self._mainWindow = None
        #
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        #
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
    #
    def mainWindow(self):
        return self._mainWindow
    #
    def mainLayout(self):
        return self._mainLayout
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def _kit__unit__set_build_Widgets(self):
        pass


#
class AbsKitQtWgtUnit_(
    qtCore.QWidget__,
    kitQtObjAbs.AbsKitQtUnitObj
):
    VAR_kit__qt_wgt__unit__side_width = 320
    def _initAbsKitQtWgtUnit(self):
        self._initAbsKitQtUnitObj()
        #
        self._initAbsKitQtWgtUnitAttr()
        self._initAbsKitQtWgtUnitUi()
        # Tool Box
        self.initToolBox()
        self._kit__unit__set_build_Widgets()
    #
    def _initAbsKitQtWgtUnitAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initAbsKitQtWgtUnitUi(self):
        self._mainLayout = qtCore.QVBoxLayout_(self)
        self._mainLayout.setContentsMargins(2, 2, 2, 2)
        self._mainLayout.setSpacing(2)
        #
        self._topToolBar = qtWidgets_.xToolBar()
        self._mainLayout.addWidget(self._topToolBar)
        self.setupTopToolBar(self._topToolBar)
    #
    def _kit__unit__set_tag_filter_config_build_(self):
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        self._tagFilterSubExplainDic = {}
        #
        self._userTagFilterFilepathStr = None
        self._userTagFilterEnableDic = {}
        #
        if self.VAR_kit__qt_wgt__unit__name is not None:
            self._userTagFilterFilepathStr = shmOutput.UserPreset().tagFilterConfigFile(self.VAR_kit__qt_wgt__unit__name)

            if bscMethods.OsFile.isExist(self._userTagFilterFilepathStr):
                self._userTagFilterEnableDic = bscMethods.OsJsonFile.read(self._userTagFilterFilepathStr)
    #
    def _kit__unit__set_tag_filter_action_build_(self, gridView):
        def loadUserFilter():
            for k, v in self._userTagFilterEnableDic.items():
                if k in self._tagFilterEnableDic:
                    self._tagFilterEnableDic[k] = self._userTagFilterEnableDic[k]
        #
        def updateEnableAt(tag, boolean):
            self._tagFilterEnableDic[tag] = boolean
            #
            if self._userTagFilterFilepathStr is not None:
                bscMethods.OsJsonFile.write(self._userTagFilterFilepathStr, self._tagFilterEnableDic)
            #
            indexLis = self._tagFilterIndexDic[tag]
            filterRow = self._tagLis.index(tag)
            gridView.viewModel().setItemMultiFilterIn(indexLis, filterColumn, filterRow, boolean)
        #
        def enableAll():
            boolean = True
            for k, v in self._tagFilterEnableDic.items():
                updateEnableAt(k, boolean)
        #
        def enableClear():
            boolean = False
            for k, v in self._tagFilterEnableDic.items():
                self._tagFilterEnableDic[k] = boolean
                updateEnableAt(k, boolean)
        #
        def addActionBranch(tag):
            def isEnable():
                return self._tagFilterEnableDic[tag]
            #
            def setEnable():
                boolean = not self._tagFilterEnableDic[tag]
                #
                updateEnableAt(tag, boolean)
            #
            if tag in self._tagFilterSubExplainDic:
                subExplain = self._tagFilterSubExplainDic[tag]
                actionExplain = '{} ( {} )'.format(tag, subExplain)
            else:
                actionExplain = tag
            actionDatumLis.append(
                (actionExplain, 'checkBox', isEnable, setEnable)
            )
        #
        def refreshFilter():
            for k, v in self._tagFilterEnableDic.items():
                updateEnableAt(k, v)
            #
            gridView.setRefresh()
        #
        loadUserFilter()
        #
        filterColumn = 100
        #
        actionDatumLis = [
            ('Basic',),
            ('Enable All', 'svg_basic/checkedall', True, enableAll),
            ('Enable None', 'svg_basic/uncheckedall', True, enableClear),
            ('Tag',)
        ]
        #
        if self._tagLis:
            for i in self._tagLis:
                addActionBranch(i)
        #
        self._filterButton.setActionData(actionDatumLis)
        #
        refreshFilter()
    #
    def setWidgetMargins(self, *args):
        self.mainLayout().setContentsMargins(*args)
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
    #
    def setupTopToolBar(self, layout):
        self._filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = guiQtWidgets.QtFilterLine()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        self._refreshButton.setTooltip(u'点击刷新')
        layout.addWidget(self._refreshButton)
        self._refreshButton.clicked.connect(self.setCentralRefresh)
    #
    def topToolBar(self):
        return self._topToolBar
    #
    def filterButton(self):
        return self._filterButton
    #
    def filterEnterLabel(self):
        return self._filterEnterLabel
    #
    def refreshButton(self):
        return self._refreshButton
    # for Override
    def setCentralRefresh(self):
        pass
    #
    def mainLayout(self):
        return self._mainLayout
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def _kit__unit__set_build_Widgets(self):
        pass


#
class AbsKitQtWgtUnit(
    qtCore.QWidget__,
    kitQtObjAbs.AbsKitQtUnitObj
):
    VAR_kit__qt_wgt__unit__side_width = 240
    def _initAbsKitQtWgtUnit(self):
        self._initAbsKitQtUnitObj()
        #
        self._initAbsKitQtWgtUnitAttr()
        self._initAbsKitQtWgtUnitUi()
        # Tool Box
        self.initToolBox()
        self._kit__unit__set_build_Widgets()
    #
    def _initAbsKitQtWgtUnitAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initAbsKitQtWgtUnitUi(self):
        self._mainLayout = qtCore.QVBoxLayout_(self)
        self._mainLayout.setContentsMargins(2, 2, 2, 2)
        self._mainLayout.setSpacing(2)
        #
        self._topToolBar = qtWidgets_.xToolBar()
        self._mainLayout.addWidget(self._topToolBar)
        self.setupTopToolBar(self._topToolBar)
    #
    def _kit__unit__set_tag_filter_config_build_(self):
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        self._tagFilterSubExplainDic = {}
        #
        self._userTagFilterFilepathStr = None
        self._userTagFilterEnableDic = {}
        #
        if self.VAR_kit__qt_wgt__unit__name is not None:
            self._userTagFilterFilepathStr = shmOutput.UserPreset().tagFilterConfigFile(self.VAR_kit__qt_wgt__unit__name)
            if bscMethods.OsFile.isExist(self._userTagFilterFilepathStr):
                self._userTagFilterEnableDic = bscMethods.OsJsonFile.read(self._userTagFilterFilepathStr)
    #
    def _kit__unit__set_tag_filter_action_build_(self, gridView):
        def loadUserFilter():
            for k, v in self._userTagFilterEnableDic.items():
                if k in self._tagFilterEnableDic:
                    self._tagFilterEnableDic[k] = self._userTagFilterEnableDic[k]
        #
        def updateEnableAt(tag, boolean):
            self._tagFilterEnableDic[tag] = boolean
            #
            if self._userTagFilterFilepathStr is not None:
                bscMethods.OsJsonFile.write(self._userTagFilterFilepathStr, self._tagFilterEnableDic)
            #
            if tag in self._tagFilterIndexDic:
                indexLis = self._tagFilterIndexDic[tag]
                filterRow = self._tagLis.index(tag)
                gridView.viewModel().setItemMultiFilterIn(indexLis, filterColumn, filterRow, boolean)
        #
        def enableAll():
            boolean = True
            for k, v in self._tagFilterEnableDic.items():
                updateEnableAt(k, boolean)
        #
        def enableClear():
            boolean = False
            for k, v in self._tagFilterEnableDic.items():
                self._tagFilterEnableDic[k] = boolean
                updateEnableAt(k, boolean)
        #
        def addActionBranch(tag):
            def isEnable():
                return self._tagFilterEnableDic[tag]
            #
            def setEnable():
                boolean = not self._tagFilterEnableDic[tag]
                #
                updateEnableAt(tag, boolean)
            #
            if tag in self._tagFilterSubExplainDic:
                subExplain = self._tagFilterSubExplainDic[tag]
                actionExplain = '{} ( {} )'.format(tag, subExplain)
            else:
                actionExplain = tag
            actionDatumLis.append(
                (actionExplain, 'checkBox', isEnable, setEnable)
            )
        #
        def refreshFilter():
            for k, v in self._tagFilterEnableDic.items():
                updateEnableAt(k, v)
            #
            gridView.setRefresh()
        #
        loadUserFilter()
        #
        filterColumn = 100
        #
        actionDatumLis = [
            ('Basic',),
            ('Enable All', 'svg_basic/checkedall', True, enableAll),
            ('Enable None', 'svg_basic/uncheckedall', True, enableClear),
            ('Tag',)
        ]
        #
        if self._tagLis:
            for i in self._tagLis:
                addActionBranch(i)
        #
        self._filterButton.setActionData(actionDatumLis)
        #
        refreshFilter()
    #
    def setWidgetMargins(self, *args):
        self.mainLayout().setContentsMargins(*args)
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
    #
    def setupTopToolBar(self, layout):
        self._filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = guiQtWidgets.QtFilterLine()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        self._refreshButton.setTooltip(u'点击刷新')
        layout.addWidget(self._refreshButton)
        self._refreshButton.clicked.connect(self.setCentralRefresh)
    #
    def topToolBar(self):
        return self._topToolBar
    # for Override
    def setCentralRefresh(self):
        pass
    #
    def filterButton(self):
        return self._filterButton
    #
    def filterEnterLabel(self):
        return self._filterEnterLabel
    #
    def mainLayout(self):
        return self._mainLayout
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def _kit__unit__set_build_Widgets(self):
        pass


#
class IfOverviewUnitBasic(
    qtCore.QWidget__,
    kitQtObjAbs.AbsKitQtUnitObj
):
    VAR_kit__qt_wgt__unit__side_width = 320
    def _initOverviewUnitBasic(self):
        self._initAbsKitQtUnitObj()
        #
        self._initOverviewUnitBasicAttr()
        self._initOverviewUnitBasicUi()
        # Unit
        self._kit__unit__set_build_Ui()
        # Tool Box
        self.initToolBox()
        self._kit__unit__set_build_Widgets()
    #
    def _initOverviewUnitBasicAttr(self):
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        self._tagFilterSubExplainDic = {}
        #
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initOverviewUnitBasicUi(self):
        self._mainLayout = qtCore.QVBoxLayout_(self)
        self._mainLayout.setContentsMargins(2, 2, 2, 2)
        self._mainLayout.setSpacing(2)
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
    #
    def setupTopToolBar(self, layout):
        self._filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = guiQtWidgets.QtFilterLine()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        self._refreshButton.setTooltip(u'点击刷新')
        layout.addWidget(self._refreshButton)
        self._refreshButton.clicked.connect(self.setCentralRefresh)
    # for Override
    def setCentralRefresh(self):
        pass
    #
    def mainLayout(self):
        return self._mainLayout
    #
    def _kit__unit__set_build_Ui(self):
        def setRightRefreshEnable():
            self._rightRefreshEnable = self._rightExpandBox.isExpanded()
        #
        toolBar = qtWidgets_.xToolBar()
        self._mainLayout.addWidget(toolBar)
        self.setupTopToolBar(toolBar)
        #
        widget = qtCore.QWidget_()
        layout = qtCore.QHBoxLayout_(widget)
        self._mainLayout.addWidget(widget)
        #
        self._leftExpandBox = qtWidgets_.QtExpandWidget()
        layout.addWidget(self._leftExpandBox)
        self._leftExpandBox.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        #
        self._leftScrollLayout = qtCore.QScrollArea_()
        self._leftExpandBox.addWidget(self._leftScrollLayout)
        #
        self._centralScrollLayout = qtCore.QScrollArea_()
        layout.addWidget(self._centralScrollLayout)
        #
        self._rightExpandBox = qtWidgets_.QtExpandWidget()
        layout.addWidget(self._rightExpandBox)
        self._rightExpandBox.setExpandDir(qtCore.LeftDir)
        self._rightExpandBox.setExpanded(False)
        self._rightExpandBox.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        self._rightExpandBox.expanded.connect(setRightRefreshEnable)
        #
        self._rightScrollLayout = qtCore.QScrollArea_()
        self._rightExpandBox.addWidget(self._rightScrollLayout)
    #
    def _kit__unit__set_build_Action(self):
        pass
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def _kit__unit__set_build_Widgets(self):
        pass


#
class IfProductUnitOverviewUnitBasic(
    qtCore.QWidget__,
    kitQtObjAbs.AbsKitQtUnitObj
):
    VAR_kit__qt_wgt__unit__side_width = 320
    def _initOverviewUnitBasic(self):
        self._initAbsKitQtUnitObj()
        #
        self._initOverviewUnitBasicAttr()
        self._initOverviewUnitBasicUi()
        # Unit
        self._kit__unit__set_build_Ui()
        # Tool Box
        self.initToolBox()
        self._kit__unit__set_build_Widgets()
    #
    def _initOverviewUnitBasicAttr(self):
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        self._tagFilterSubExplainDic = {}
        #
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initOverviewUnitBasicUi(self):
        self._mainLayout = qtCore.QVBoxLayout_(self)
        self._mainLayout.setContentsMargins(2, 2, 2, 2)
        self._mainLayout.setSpacing(2)
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
    #
    def setupTopToolBar(self, layout):
        self._filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = guiQtWidgets.QtFilterLine()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        self._refreshButton.setTooltip(u'点击刷新')
        layout.addWidget(self._refreshButton)
        self._refreshButton.clicked.connect(self.setCentralRefresh)
    # for Override
    def setRecordRefresh(self):
        pass
    #
    def _setupLinkFilter(self, productModuleString, layout):
        uiSetDic = prsMethods.Product.moduleLinkShownameDic(productModuleString)
        toolGroupBox = guiQtWidgets.QtToolboxGroup()
        toolGroupBox.setTitle('Link Filter')
        toolGroupBox.setExpanded(True)
        layout.addWidget(toolGroupBox)
        #
        checkView = guiQtWidgets.QtCheckview()
        toolGroupBox.addWidget(checkView)
        checkView.setWidgetMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 0
        for filterRow, (keyword, explainLis) in enumerate(uiSetDic.items()):
            filterItem = guiQtWidgets.QtFilterCheckbutton('link/{}'.format(keyword))
            checkView.addWidget(filterItem)
            #
            filterItem.setNameString(explainLis[bscCfg.BscUtility.LynxiUiIndex_Language])
            filterItem.setChecked(True)
            #
            filterItem.setItemFilterColumn(filterColumn)
            filterItem.setItemFilterRow(filterRow)
            #
            self._filterItemDic[keyword] = filterItem
    #
    def _setupClassFilter(self, productModuleString, layout):
        uiSetDic = prsMethods.Product.moduleClassShownames(productModuleString)
        toolGroupBox = guiQtWidgets.QtToolboxGroup()
        toolGroupBox.setTitle('Class Filter')
        toolGroupBox.setExpanded(True)
        layout.addWidget(toolGroupBox)
        #
        checkView = guiQtWidgets.QtCheckview()
        toolGroupBox.addWidget(checkView)
        checkView.setWidgetMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 1
        filterRow = 0
        for seq, (keyword, explainLis) in enumerate(uiSetDic.items()):
            mainFilterButton = guiQtWidgets.QtFilterCheckbutton('object/{}'.format(keyword))
            checkView.addWidget(mainFilterButton)
            #
            mainFilterButton.setNameString(explainLis[bscCfg.BscUtility.LynxiUiIndex_Language])
            mainFilterButton.setChecked(True)
            mainFilterButton.setItemFilterColumn(filterColumn)
            mainFilterButton.setItemFilterRow(filterRow)
            #
            filterRow += 1
            #
            subFilterConfigDic = prsMethods.Product.modulePriorityShownameDic(productModuleString)
            for subSeq, (subKeyword, subExplainLis) in enumerate(subFilterConfigDic.items()):
                subFilterButton = guiQtWidgets.QtFilterCheckbutton('svg_basic/{}'.format(subKeyword))
                checkView.addWidget(subFilterButton)
                #
                subFilterButton.setNameString(subExplainLis[bscCfg.BscUtility.LynxiUiIndex_Language])
                #
                subFilterButton.setChecked(True)
                subFilterButton.setItemFilterColumn(filterColumn)
                subFilterButton.setItemFilterRow(filterRow)
                #
                r, g, b = qtCore.hsv2rgb(60 * seq, 1 / float(subSeq + 1), 1)
                subFilterButton.setFilterColor((r, g, b, 255))
                #
                mainFilterButton.addFilterChild(subFilterButton)
                #
                self._filterItemDic[(keyword, subKeyword)] = subFilterButton
                #
                filterRow += 1
    #
    def _setupStageFilter(self, productModuleString, layout):
        linkLis = prsMethods.Product._lxProductLinkLis(productModuleString)
        #
        toolGroupBox = guiQtWidgets.QtToolboxGroup()
        toolGroupBox.setTitle('Stage Filter')
        layout.addWidget(toolGroupBox)
        #
        toolBar = qtWidgets_.xToolBar()
        toolGroupBox.addWidget(toolBar)
        #
        for seq, i in enumerate(linkLis):
            enableItem = guiQtWidgets.QtEnablebutton('basic/{}Link'.format(i))
            enableItem.setAutoExclusive(True)
            toolBar.addWidget(enableItem)
            #
            if seq == 0:
                enableItem.setChecked(True)
        #
        checkView = guiQtWidgets.QtCheckview()
        toolGroupBox.addWidget(checkView)
        uiSetDic = prsMethods.Product.moduleStepShownameDic(productModuleString)
        checkView.setWidgetMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 0
        filterRow = 0
        for seq, (mainFilterKey, explainLis) in enumerate(uiSetDic.items()):
            filterItem = guiQtWidgets.QtFilterCheckbutton()
            checkView.addWidget(filterItem)
            #
            filterItem.setNameString(explainLis[bscCfg.BscUtility.LynxiUiIndex_Language])
            filterItem.setChecked(True)
            #
            r, g, b = qtCore.hsv2rgb(180 + 24 * filterRow, 1, 1)
            filterItem.setFilterColor((r, g, b, 255))
            #
            filterItem.setItemFilterColumn(filterColumn)
            filterItem.setItemFilterRow(filterRow)
            #
            self._filterItemDic[mainFilterKey] = filterItem
            #
            filterRow += 1
    @staticmethod
    def setupStageFilterBox(linkLis, filterItemDic, layout):
        toolGroupBox = guiQtWidgets.QtToolboxGroup()
        toolGroupBox.setTitle('Stage Filter')
        layout.addWidget(toolGroupBox)
        #
        toolBar = qtWidgets_.xToolBar()
        toolGroupBox.addWidget(toolBar)
        #
        for seq, i in enumerate(linkLis):
            enableItem = guiQtWidgets.QtEnablebutton('basic/{}Link'.format(i))
            enableItem.setAutoExclusive(True)
            toolBar.addWidget(enableItem)
            #
            if seq == 0:
                enableItem.setChecked(True)
        #
        checkView = guiQtWidgets.QtCheckview()
        toolGroupBox.addWidget(checkView)
        filterConfigDic = prsMethods.Product.stepShownamesDic()
        checkView.setWidgetMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 0
        filterRow = 0
        for seq, (mainFilterKey, (keyword, enExplain, cnExplain)) in enumerate(filterConfigDic.items()):
            filterItem = guiQtWidgets.QtFilterCheckbutton()
            checkView.addWidget(filterItem)
            #
            filterItem.setName(u'{} ( {} )'.format(enExplain, cnExplain))
            filterItem.setChecked(True)
            #
            r, g, b = qtCore.hsv2rgb(180 + 24 * filterRow, 1, 1)
            filterItem.setFilterColor((r, g, b, 255))
            #
            filterItem.setItemFilterColumn(filterColumn)
            filterItem.setItemFilterRow(filterRow)
            #
            filterItemDic[keyword] = filterItem
            #
            filterRow += 1
    #
    def _kit__unit__set_tag_filter_action_build_(self, gridView):
        def setEnableAt(tag, boolean):
            indices = self._tagFilterIndexDic[tag]
            filterRow = self._tagLis.index(tag)
            gridView.viewModel().setItemMultiFilterIn(indices, filterColumn, filterRow, boolean)
        #
        def enableAll():
            boolean = True
            for k, v in self._tagFilterEnableDic.items():
                self._tagFilterEnableDic[k] = boolean
                setEnableAt(k, boolean)
        #
        def enableClear():
            boolean = False
            for k, v in self._tagFilterEnableDic.items():
                self._tagFilterEnableDic[k] = boolean
                setEnableAt(k, boolean)
        #
        def addActionBranch(tag):
            def isEnable():
                return self._tagFilterEnableDic[tag]
            #
            def setEnable():
                boolean = not self._tagFilterEnableDic[tag]
                #
                self._tagFilterEnableDic[tag] = boolean
                setEnableAt(tag, boolean)
            #
            if tag in self._tagFilterSubExplainDic:
                subExplain = self._tagFilterSubExplainDic[tag]
                actionExplain = '{} ( {} )'.format(tag, subExplain)
            else:
                actionExplain = tag
            actionDatumLis.append(
                (actionExplain, 'checkBox', isEnable, setEnable)
            )
        #
        filterColumn = 100
        #
        actionDatumLis = [
            ('Basic',),
            ('Enable All', 'svg_basic/checkedall', True, enableAll),
            ('Enable None', 'svg_basic/uncheckedall', True, enableClear),
            ('Tag',)
        ]
        #
        if self._tagLis:
            for i in self._tagLis:
                addActionBranch(i)
        #
        self._filterButton.setActionData(actionDatumLis)
    # for Override
    def setCentralRefresh(self):
        pass
    #
    def mainLayout(self):
        return self._mainLayout
    #
    def _kit__unit__set_build_Ui(self):
        def setRightRefreshEnable():
            self._rightRefreshEnable = self._rightExpandBox.isExpanded()
            #
            self.setRecordRefresh()
        #
        toolBar = qtWidgets_.xToolBar()
        self._mainLayout.addWidget(toolBar)
        self.setupTopToolBar(toolBar)
        #
        widget = qtCore.QWidget_()
        layout = qtCore.QHBoxLayout_(widget)
        self._mainLayout.addWidget(widget)
        #
        self._leftExpandBox = qtWidgets_.QtExpandWidget()
        layout.addWidget(self._leftExpandBox)
        self._leftExpandBox.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        #
        self._leftScrollLayout = qtCore.QScrollArea_()
        self._leftExpandBox.addWidget(self._leftScrollLayout)
        #
        self._centralScrollLayout = qtCore.QScrollArea_()
        layout.addWidget(self._centralScrollLayout)
        #
        self._rightExpandBox = qtWidgets_.QtExpandWidget()
        layout.addWidget(self._rightExpandBox)
        self._rightExpandBox.setExpandDir(qtCore.LeftDir)
        self._rightExpandBox.setExpanded(False)
        self._rightExpandBox.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        self._rightExpandBox.expanded.connect(setRightRefreshEnable)
        #
        self._rightScrollLayout = qtCore.QScrollArea_()
        self._rightExpandBox.addWidget(self._rightScrollLayout)
    #
    def _kit__unit__set_build_Action(self):
        pass
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def _kit__unit__set_build_Widgets(self):
        pass


#
class IfProductToolUnitBasic(
    qtCore.QWidget__,
    kitQtObjAbs.AbsKitQtUnitObj
):
    pass


#
class IfToolUnitBasic(
    qtCore.QWidget__,
    kitQtObjAbs.IfToolUnitAbs
):
    VAR_kit__qt_wgt__unit__side_width = 400
    UnitScriptJobWindowName = None
    def _initToolUnitBasic(self):
        self._initToolUnitAbs()
        #
        self._initBasicToolUnitAttr()
        self._initBasicToolUnitUi()
    #
    def _initBasicToolUnitAttr(self):
        pass
    #
    def _initBasicToolUnitUi(self):
        self._mainLayout = qtCore.QVBoxLayout_(self)
        self._mainLayout.setContentsMargins(0, 0, 0, 0)
        self._mainLayout.setSpacing(2)
        #
        self._topToolBar = qtWidgets_.xToolBar()
        self._topToolBar.hide()
        self._mainLayout.addWidget(self._topToolBar)
        self.setupTopToolBar(self._topToolBar)
    #
    def setupTopToolBar(self, layout):
        self._filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = guiQtWidgets.QtFilterLine()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        self._refreshButton.setTooltip(u'点击刷新')
        layout.addWidget(self._refreshButton)
    #
    def topToolBar(self):
        return self._topToolBar
    #
    def filterButton(self):
        return self._filterButton
    #
    def filterEnterLabel(self):
        return self._filterEnterLabel
    #
    def refreshButton(self):
        return self._refreshButton
    #
    def mainLayout(self):
        return self._mainLayout
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def _kit__unit__set_build_Widgets(self):
        pass


# custom tool unit *************************************************************************************************** #
class AbsKitQtCustomToolUnitWgt(qtCore.QWidget__):
    CLS_kit__qt__custom_unit__model = None

    def _initAbsKitQtCustomToolUnitWgt(self, *args):
        pass
