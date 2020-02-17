# coding:utf-8
from LxBasic import bscConfigure, bscMethods

from LxScheme import shmOutput

from LxPreset import prsMethods
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore
#
from LxInterface.qt import qtIfAbstract
#
none = ''


#
class QtIfAbc_Shelf(
    qtWidgets.QtVShelfTabgroup,
    qtIfAbstract.IfShelfAbs
):
    ShelfWidth = 800
    SideWidth = 320
    def _initIfAbcShelf(self):
        self._initShelfAbs()
        #
        self._initIfAbcShelfAttr()
        self._initIfAbcShelfUi()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def _initIfAbcShelfAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initIfAbcShelfUi(self):
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
class QtIfAbc_Group(
    qtWidgets.QtHShelfTabgroup,
    qtIfAbstract.IfAbcGroupModel
):
    GroupWidth = 800
    SideWidth = 320
    def _initIfAbcGroup(self):
        self._initAbcGroupModel()
        #
        self._initIfAbcGroupAttr()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def _initIfAbcGroupAttr(self):
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
class QtIfAbc_Unit_(
    qtCore.QWidget__,
    qtIfAbstract.IfUnitAbs
):
    SideWidth = 320
    def _initIfAbcUnit(self):
        self._initUnitAbs()
        #
        self._initIfAbcUnitAttr()
        self._initIfAbcUnitUi()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def _initIfAbcUnitAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initIfAbcUnitUi(self):
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
            self._userTagFilterFile = shmOutput.UserPreset().tagFilterConfigFile(self.UnitName)

            if bscMethods.OsFile.isExist(self._userTagFilterFile):
                self._userTagFilterEnableDic = bscMethods.OsJson.read(self._userTagFilterFile)
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
                bscMethods.OsJson.write(self._userTagFilterFile, self._tagFilterEnableDic)
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
class QtIfAbc_Unit(
    qtCore.QWidget__,
    qtIfAbstract.IfUnitAbs
):
    SideWidth = 320
    def _initIfAbcUnit(self):
        self._initUnitAbs()
        #
        self._initIfAbcUnitAttr()
        self._initIfAbcUnitUi()
        # Tool Box
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def _initIfAbcUnitAttr(self):
        self._filterItemDic = {}
        self._filterIndexDic = {}
        #
        self._filterFrameDic = {}
    #
    def _initIfAbcUnitUi(self):
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
            self._userTagFilterFile = shmOutput.UserPreset().tagFilterConfigFile(self.UnitName)
            if bscMethods.OsFile.isExist(self._userTagFilterFile):
                self._userTagFilterEnableDic = bscMethods.OsJson.read(self._userTagFilterFile)
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
                bscMethods.OsJson.write(self._userTagFilterFile, self._tagFilterEnableDic)
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
    qtCore.QWidget__,
    qtIfAbstract.IfUnitAbs
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
    qtCore.QWidget__,
    qtIfAbstract.IfUnitAbs
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
    def setRecordRefresh(self):
        pass
    #
    def _setupLinkFilter(self, productModuleString, layout):
        uiSetDic = prsMethods.Product.moduleLinkShownameDic(productModuleString)
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
            filterItem.setNameText(explainLis[bscConfigure.Utility.LynxiUiIndex_Language])
            filterItem.setChecked(True)
            #
            filterItem.setItemFilterColumn(filterColumn)
            filterItem.setItemFilterRow(filterRow)
            #
            self._filterItemDic[keyword] = filterItem
    #
    def _setupClassFilter(self, productModuleString, layout):
        uiSetDic = prsMethods.Product.moduleClassShownames(productModuleString)
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
            mainFilterButton.setNameText(explainLis[bscConfigure.Utility.LynxiUiIndex_Language])
            mainFilterButton.setChecked(True)
            mainFilterButton.setItemFilterColumn(filterColumn)
            mainFilterButton.setItemFilterRow(filterRow)
            #
            filterRow += 1
            #
            subFilterConfigDic = prsMethods.Product.modulePriorityShownameDic(productModuleString)
            for subSeq, (subKeyword, subExplainLis) in enumerate(subFilterConfigDic.items()):
                subFilterButton = qtWidgets.QtFilterCheckbutton('svg_basic@svg#{}'.format(subKeyword))
                checkView.addWidget(subFilterButton)
                #
                subFilterButton.setNameText(subExplainLis[bscConfigure.Utility.LynxiUiIndex_Language])
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
        uiSetDic = prsMethods.Product.moduleStepShownameDic(productModuleString)
        checkView.setMargins(2, 2, 2, 2)
        checkView.setSpacing(2)
        #
        filterColumn = 0
        filterRow = 0
        for seq, (mainFilterKey, explainLis) in enumerate(uiSetDic.items()):
            filterItem = qtWidgets.QtFilterCheckbutton()
            checkView.addWidget(filterItem)
            #
            filterItem.setNameText(explainLis[bscConfigure.Utility.LynxiUiIndex_Language])
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
        filterConfigDic = prsMethods.Product.stepShownamesDic()
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
    qtCore.QWidget__,
    qtIfAbstract.IfUnitAbs
):
    pass


#
class IfToolUnitBasic(
    qtCore.QWidget__,
    qtIfAbstract.IfToolUnitAbs
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
