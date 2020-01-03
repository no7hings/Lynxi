# coding:utf-8
from LxCore.config import appConfig, basicCfg
#
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore
#
from LxInterface.qt import ifAbstract
#
from LxCore.method import _presetMethod
#
none = ''


#
class IfShelfBasic_(
    qtWidgets.QtVShelfTabGroup,
    ifAbstract.IfShelfAbs
):
    ShelfWidth = 800
    SideWidth = 320
    def _initShelfBasic(self):
        self._initShelfAbs()
        #
        self._initShelfBasicAttr()
        self._initShelfBasicUi()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def _initShelfBasicAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initShelfBasicUi(self):
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
    def setupUnitWidgets(self):
        pass


#
class IfGroupBasic_(
    qtWidgets.QtHShelfTabGroup,
    ifAbstract.IfGroupModelAbs
):
    GroupWidth = 800
    SideWidth = 320
    def _initBasicGroup(self):
        self._initGroupModelAbs()
        #
        self._initBasicGroupAttr()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def _initBasicGroupAttr(self):
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
    def setupUnitWidgets(self):
        pass


#
class IfUnitBasic(
    qtCore.UiMainWidget,
    ifAbstract.IfUnitAbs,
    _presetMethod.LxPresetMethod
):
    SideWidth = 320
    def _initUnitBasic(self):
        self._initUnitAbs()
        #
        self._initUnitBasicAttr()
        self._initUnitBasicUi()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def _initUnitBasicAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initUnitBasicUi(self):
        self._mainLayout = qtCore.QVBoxLayout_(self)
        self._mainLayout.setContentsMargins(2, 2, 2, 2)
        self._mainLayout.setSpacing(2)
        #
        self._topToolBar = qtWidgets_.xToolBar()
        self._mainLayout.addWidget(self._topToolBar)
        self.setupTopToolBar(self._topToolBar)
    #
    def _initTagFilterVar(self):
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        self._tagFilterSubExplainDic = {}
        #
        self._userTagFilterFile = None
        self._userTagFilterEnableDic = {}
        #
        if self.UnitName is not None:
            self._userTagFilterFile = self.lxOsTagFilterFile(self.UnitName)
            if self.isOsExistsFile(self._userTagFilterFile):
                self._userTagFilterEnableDic = self.readOsJson(self._userTagFilterFile)
    #
    def _initTagFilterAction(self, gridView):
        def loadUserFilter():
            for k, v in self._userTagFilterEnableDic.items():
                if k in self._tagFilterEnableDic:
                    self._tagFilterEnableDic[k] = self._userTagFilterEnableDic[k]
        #
        def updateEnableAt(tag, boolean):
            self._tagFilterEnableDic[tag] = boolean
            #
            if self._userTagFilterFile is not None:
                self.writeOsJson(self._tagFilterEnableDic, self._userTagFilterFile)
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
            ('Enable All', 'svg_basic@svg#checkedAll', True, enableAll),
            ('Enable None', 'svg_basic@svg#uncheckedAll', True, enableClear),
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
    def setMargins(self, *args):
        self.mainLayout().setContentsMargins(*args)
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
    #
    def setupTopToolBar(self, layout):
        self._filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
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
    def setupUnitWidgets(self):
        pass


#
class IfUnitBasic_(
    qtCore.UiMainWidget,
    ifAbstract.IfUnitAbs,
    _presetMethod.LxPresetMethod
):
    SideWidth = 320
    def _initUnitBasic(self):
        self._initUnitAbs()
        #
        self._initUnitBasicAttr()
        self._initUnitBasicUi()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def _initUnitBasicAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initUnitBasicUi(self):
        self._mainLayout = qtCore.QVBoxLayout_(self)
        self._mainLayout.setContentsMargins(2, 2, 2, 2)
        self._mainLayout.setSpacing(2)
        #
        self._topToolBar = qtWidgets_.xToolBar()
        self._mainLayout.addWidget(self._topToolBar)
        self.setupTopToolBar(self._topToolBar)
    #
    def _initTagFilterVar(self):
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        self._tagFilterSubExplainDic = {}
        #
        self._userTagFilterFile = None
        self._userTagFilterEnableDic = {}
        #
        if self.UnitName is not None:
            self._userTagFilterFile = self.lxOsTagFilterFile(self.UnitName)
            if self.isOsExistsFile(self._userTagFilterFile):
                self._userTagFilterEnableDic = self.readOsJson(self._userTagFilterFile)
    #
    def _initTagFilterAction(self, gridView):
        def loadUserFilter():
            for k, v in self._userTagFilterEnableDic.items():
                if k in self._tagFilterEnableDic:
                    self._tagFilterEnableDic[k] = self._userTagFilterEnableDic[k]
        #
        def updateEnableAt(tag, boolean):
            self._tagFilterEnableDic[tag] = boolean
            #
            if self._userTagFilterFile is not None:
                self.writeOsJson(self._tagFilterEnableDic, self._userTagFilterFile)
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
            ('Enable All', 'svg_basic@svg#checkedAll', True, enableAll),
            ('Enable None', 'svg_basic@svg#uncheckedAll', True, enableClear),
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
    def setMargins(self, *args):
        self.mainLayout().setContentsMargins(*args)
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
    #
    def setupTopToolBar(self, layout):
        self._filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
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
    def setupUnitWidgets(self):
        pass


#
class IfOverviewUnitBasic(
    qtCore.UiMainWidget,
    ifAbstract.IfUnitAbs
):
    SideWidth = 320
    def _initOverviewUnitBasic(self):
        self._initUnitAbs()
        #
        self._initOverviewUnitBasicAttr()
        self._initOverviewUnitBasicUi()
        # Unit
        self.setupUnitUi()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
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
        self._filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
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
    def setupUnitUi(self):
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
        self._leftExpandBox.setUiWidth(self.SideWidth)
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
        self._rightExpandBox.setUiWidth(self.SideWidth)
        self._rightExpandBox.expanded.connect(setRightRefreshEnable)
        #
        self._rightScrollLayout = qtCore.QScrollArea_()
        self._rightExpandBox.addWidget(self._rightScrollLayout)
    #
    def setupUnitAction(self):
        pass
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def setupUnitWidgets(self):
        pass


#
class IfProductUnitOverviewUnitBasic(
    qtCore.UiMainWidget,
    ifAbstract.IfUnitAbs
):
    Cfg_Product = appConfig.Cfg_Product
    SideWidth = 320
    def _initOverviewUnitBasic(self):
        self._initUnitAbs()
        #
        self._initOverviewUnitBasicAttr()
        self._initOverviewUnitBasicUi()
        # Unit
        self.setupUnitUi()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
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
        self._filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
        self._refreshButton.setTooltip(u'点击刷新')
        layout.addWidget(self._refreshButton)
        self._refreshButton.clicked.connect(self.setCentralRefresh)
    # for Override
    def setRecordRefresh(self):
        pass
    #
    def _setupLinkFilter(self, productModule, layout):
        uiSetDic = self.Cfg_Product._lxProductLinkUiSetDic(productModule)
        toolGroupBox = qtWidgets.QtToolboxGroup()
        toolGroupBox.setTitle('Link Filter')
        toolGroupBox.setExpanded(True)
        layout.addWidget(toolGroupBox)
        #
        checkView = qtWidgets.QtCheckview()
        toolGroupBox.addWidget(checkView)
        checkView.setMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 0
        for filterRow, (keyword, explainLis) in enumerate(uiSetDic.items()):
            filterItem = qtWidgets.QtFilterCheckbutton('link#{}'.format(keyword))
            checkView.addWidget(filterItem)
            #
            filterItem.setNameText(explainLis[self.LynxiUiIndex_Language])
            filterItem.setChecked(True)
            #
            filterItem.setItemFilterColumn(filterColumn)
            filterItem.setItemFilterRow(filterRow)
            #
            self._filterItemDic[keyword] = filterItem
    #
    def _setupClassFilter(self, productModule, layout):
        uiSetDic = self.Cfg_Product._lxProductClassUiSetDic(productModule)
        toolGroupBox = qtWidgets.QtToolboxGroup()
        toolGroupBox.setTitle('Class Filter')
        toolGroupBox.setExpanded(True)
        layout.addWidget(toolGroupBox)
        #
        checkView = qtWidgets.QtCheckview()
        toolGroupBox.addWidget(checkView)
        checkView.setMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 1
        filterRow = 0
        for seq, (keyword, explainLis) in enumerate(uiSetDic.items()):
            mainFilterButton = qtWidgets.QtFilterCheckbutton('object#{}'.format(keyword))
            checkView.addWidget(mainFilterButton)
            #
            mainFilterButton.setNameText(explainLis[self.LynxiUiIndex_Language])
            mainFilterButton.setChecked(True)
            mainFilterButton.setItemFilterColumn(filterColumn)
            mainFilterButton.setItemFilterRow(filterRow)
            #
            filterRow += 1
            #
            subFilterConfigDic = self.Cfg_Product._lxProductPriorityUiSetDic(productModule)
            for subSeq, (subKeyword, subExplainLis) in enumerate(subFilterConfigDic.items()):
                subFilterButton = qtWidgets.QtFilterCheckbutton('svg_basic@svg#{}'.format(subKeyword))
                checkView.addWidget(subFilterButton)
                #
                subFilterButton.setNameText(subExplainLis[self.LynxiUiIndex_Language])
                #
                subFilterButton.setChecked(True)
                subFilterButton.setItemFilterColumn(filterColumn)
                subFilterButton.setItemFilterRow(filterRow)
                #
                r, g, b = qtCore.hsvToRgb(60 * seq, 1 / float(subSeq + 1), 1)
                subFilterButton.setFilterColor((r, g, b, 255))
                #
                mainFilterButton.addFilterChild(subFilterButton)
                #
                self._filterItemDic[(keyword, subKeyword)] = subFilterButton
                #
                filterRow += 1
    #
    def _setupStageFilter(self, productModule, layout):
        linkLis = self.Cfg_Product._lxProductLinkLis(productModule)
        #
        toolGroupBox = qtWidgets.QtToolboxGroup()
        toolGroupBox.setTitle('Stage Filter')
        layout.addWidget(toolGroupBox)
        #
        toolBar = qtWidgets_.xToolBar()
        toolGroupBox.addWidget(toolBar)
        #
        for seq, i in enumerate(linkLis):
            enableItem = qtWidgets.QtEnablebutton('basic#{}Link'.format(i))
            enableItem.setAutoExclusive(True)
            toolBar.addWidget(enableItem)
            #
            if seq == 0:
                enableItem.setChecked(True)
        #
        checkView = qtWidgets.QtCheckview()
        toolGroupBox.addWidget(checkView)
        uiSetDic = self.Cfg_Product._lxProductStageUiSetDic(productModule)
        checkView.setMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 0
        filterRow = 0
        for seq, (mainFilterKey, explainLis) in enumerate(uiSetDic.items()):
            filterItem = qtWidgets.QtFilterCheckbutton()
            checkView.addWidget(filterItem)
            #
            filterItem.setNameText(explainLis[self.LynxiUiIndex_Language])
            filterItem.setChecked(True)
            #
            r, g, b = qtCore.hsvToRgb(180 + 24 * filterRow, 1, 1)
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
        toolGroupBox = qtWidgets.QtToolboxGroup()
        toolGroupBox.setTitle('Stage Filter')
        layout.addWidget(toolGroupBox)
        #
        toolBar = qtWidgets_.xToolBar()
        toolGroupBox.addWidget(toolBar)
        #
        for seq, i in enumerate(linkLis):
            enableItem = qtWidgets.QtEnablebutton('basic#{}Link'.format(i))
            enableItem.setAutoExclusive(True)
            toolBar.addWidget(enableItem)
            #
            if seq == 0:
                enableItem.setChecked(True)
        #
        checkView = qtWidgets.QtCheckview()
        toolGroupBox.addWidget(checkView)
        filterConfigDic = basicCfg.basicProductionStageDic()
        checkView.setMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 0
        filterRow = 0
        for seq, (mainFilterKey, (keyword, enExplain, cnExplain)) in enumerate(filterConfigDic.items()):
            filterItem = qtWidgets.QtFilterCheckbutton()
            checkView.addWidget(filterItem)
            #
            filterItem.setName(u'{} ( {} )'.format(enExplain, cnExplain))
            filterItem.setChecked(True)
            #
            r, g, b = qtCore.hsvToRgb(180 + 24 * filterRow, 1, 1)
            filterItem.setFilterColor((r, g, b, 255))
            #
            filterItem.setItemFilterColumn(filterColumn)
            filterItem.setItemFilterRow(filterRow)
            #
            filterItemDic[keyword] = filterItem
            #
            filterRow += 1
    #
    def _initTagFilterAction(self, gridView):
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
            ('Enable All', 'svg_basic@svg#checkedAll', True, enableAll),
            ('Enable None', 'svg_basic@svg#uncheckedAll', True, enableClear),
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
    def setupUnitUi(self):
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
        self._leftExpandBox.setUiWidth(self.SideWidth)
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
        self._rightExpandBox.setUiWidth(self.SideWidth)
        self._rightExpandBox.expanded.connect(setRightRefreshEnable)
        #
        self._rightScrollLayout = qtCore.QScrollArea_()
        self._rightExpandBox.addWidget(self._rightScrollLayout)
    #
    def setupUnitAction(self):
        pass
    # for Override
    def initToolBox(self):
        pass
    # for Override
    def setupUnitWidgets(self):
        pass


#
class IfProductToolUnitBasic(
    qtCore.UiMainWidget,
    ifAbstract.IfUnitAbs
):
    pass


#
class IfToolUnitBasic(
    qtCore.UiMainWidget,
    ifAbstract.IfToolUnitAbs
):
    SideWidth = 400
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
        self._filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        layout.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
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
    def setupUnitWidgets(self):
        pass
