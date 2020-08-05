# coding=utf-8
from LxBasic import bscMethods, bscObjects

from LxScheme import shmOutput

from LxPreset import prsConfigure, prsMtdCore

from LxGui import guiCore

from LxGui.qt import qtModifiers, qtWidgets_, guiQtWidgets, qtCore


#
class IfPresetWindow(guiQtWidgets.QtToolWindow):
    leftBoxWidth = 320
    widthSet = 55
    VAR_kit__qt_wgt__unit__side_width = 480
    #
    VAR_gui_qt__window_wgt__title = 'Preset'
    VAR_kit__window__version = shmOutput.Scheme().version
    def __init__(self):
        super(IfPresetWindow, self).__init__()

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Default)
        self.setWidgetMargins(0, 0, 0, 0)
        #
        self.setNameString(self.VAR_gui_qt__window_wgt__title)
        self.setIndexString(self.VAR_kit__window__version)
        #
        self.guideTreeBoxDic = {}
        self.scrollBoxDic = {}
        #
        self.chooseBoxDic = {}
        self.refreshMethodDic = {}
        #
        self.setupWindow()
    #
    def setupPresetUnit(self, key, layout):
        topToolBar = qtWidgets_.xToolBar()
        self.setupTopToolBar(key, topToolBar)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(leftExpandWidget)
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self._kit__unit__set_left_build_(key, leftScrollArea)
        #
        rightWidget = qtCore.QWidget_()
        rightLayout = qtCore.QVBoxLayout_(rightWidget)
        rightLayout.setContentsMargins(0, 0, 0, 0)
        self.setupRightBox(key, rightLayout)
        #
        layout.addWidget(topToolBar, 0, 0, 1, 2)
        layout.addWidget(leftExpandWidget, 1, 0, 1, 1)
        layout.addWidget(rightWidget, 1, 1, 1, 1)
        #
        self.setBuildPreset(key)
    #
    def setupTopToolBar(self, key, layout):
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
    def _kit__unit__set_left_build_(self, key, layout):
        def setRefresh():
            treeItems = guideTreeBox.treeItems()
            for treeItem in treeItems:
                toolGroupBox = treeItem.toolGroupBox
                toolGroupBox.setVisible(treeItem.isSelected())
        #
        guideTreeBox = qtWidgets_.QTreeWidget_()
        guideTreeBox.setColumns(
            ['Preset', 'Scheme'],
            [2, 2],
            self.VAR_kit__qt_wgt__unit__side_width - 20
        )
        guideTreeBox.setHeaderHidden(True)
        guideTreeBox.setSingleSelection()
        layout.addWidget(guideTreeBox)
        #
        guideTreeBox.itemSelectionChanged.connect(setRefresh)
        #
        self.guideTreeBoxDic[key] = guideTreeBox
    #
    def setupRightBox(self, key, layout):
        scrollBox = qtCore.QScrollArea_()
        layout.addWidget(scrollBox)
        scrollBox.setScrollBarVisible('off', 'normal')
        scrollBox.setContentsMargins(0, 0, 0, 0)
        self.scrollBoxDic[key] = scrollBox
    #
    def setBuildPreset(self, key):
        def setBranch(keypath):
            def setTreeItem():
                if explainKey:
                    treeItem.setText(0, bscMethods.StrCamelcase.toPrettify(explainKey))
                    iconKeywordStr = ['svg_basic/project', 'svg_basic/branch_main', 'svg_basic/tag'][len(keypath) - 1]
                    treeItem.setItemIcon_(0, iconKeywordStr)
                #
                if parentKey:
                    if parentKey in treeItemDic:
                        parentItem = treeItemDic[parentKey]
                        parentItem.addChild(treeItem)
                        parentItem.setExpanded(True)
                elif not parentKey:
                    guideTreeBox.addItem(treeItem)
            #
            def setChooseBox():
                treeItem.setItemWidget(1, chooseBox)
                chooseBox.setChooseEnable(True)
                chooseBox.setNameTextWidth(0)
            #
            def setToolGroup():
                toolGroupBox.hide()
                toolGroupBox.setExpanded(True)
                scrollBox.addWidget(toolGroupBox)
            #
            parentKey = None
            explainKey = None
            #
            treeItem = qtWidgets_.QTreeWidgetItem_()
            treeItemDic[keypath] = treeItem
            #
            chooseBox = guiQtWidgets.QtValueLine()
            #
            toolGroupBox = guiQtWidgets.QtToolboxGroup()
            treeItem.toolGroupBox = toolGroupBox
            treeItem.chooseBox = chooseBox
            treeItem.keypath = keypath
            # Guide
            if len(keypath) == 1:
                guideKeyString = keypath[0]
                explainKey = guideKeyString
                setTreeItem()
                setChooseBox()
                setToolGroup()
                self.setBuildGuidePreset(treeItem)
            # Main
            elif len(keypath) == 2:
                guideKeyString, mainPresetKey = keypath
                parentKey = (guideKeyString,)
                explainKey = mainPresetKey
                setTreeItem()
                if keypath in prsMtdCore.Mtd_PrsUtility._mainKeyPathList():
                    setChooseBox()
                setToolGroup()
                self.setBuildMainPreset(treeItem)
            # Sub
            elif len(keypath) == 3:
                guideKeyString, mainPresetKey, subPresetKey = keypath
                parentKey = (guideKeyString, mainPresetKey)
                explainKey = subPresetKey
                setTreeItem()
                setToolGroup()
                self.setBuildSubPreset(treeItem)
        #
        def setHierarchy(data):
            if data:
                for i in data:
                    setBranch(i)
        #
        treeItemDic = {}
        guideTreeBox = self.guideTreeBoxDic[key]
        scrollBox = self.scrollBoxDic[key]
        #
        basicData = prsMtdCore.Mtd_PrsUtility._keyTreeDict(key)
        setHierarchy(basicData)
        if guideTreeBox.topItems():
            guideTreeBox.topItems()[0].setSelected(True)
    #
    def setBuildGuidePreset(self, treeItem):
        self.setGuidePresetChooseBox(treeItem)
        self.setGuidePresetToolboxGroup(treeItem)
        self.setToolboxGroupTitle(treeItem)
    # Guide
    def setGuidePresetChooseBox(self, treeItem):
        def setRefresh():
            guideSchemeKey = chooseBox.datum()
            mainSchemeData = prsMtdCore.Mtd_PrsUtility.getPresetSetDic((guideKeyString,), guideSchemeKey)
            self.setMaxProgressValue(len(mainSchemeData))
            for k, v in mainSchemeData.items():
                self.updateProgress()
                mainPresetKey = k
                mainSchemeKey = v
                mainChooseBox = self.chooseBoxDic[(guideKeyString, mainPresetKey)]
                message = mainChooseBox.datum()
                if not message == mainSchemeKey:
                    mainChooseBox.setChoose(mainSchemeKey)
            #
            self.setSubPresetToolboxGroupTitle(treeItem)
        #
        guideKeyString = treeItem.keypath[0]
        chooseBox = treeItem.chooseBox
        #
        messages = prsMtdCore.Mtd_PrsUtility._getEnabledSchemes((guideKeyString,))
        chooseBox.setDatumLis(messages)
        #
        self.chooseBoxDic[(guideKeyString, )] = chooseBox
        #
        chooseBox.chooseChanged.connect(setRefresh)
    #
    def setGuidePresetToolboxGroup(self, treeItem):
        def getExpandedMethod():
            presetItems = presetBox.items()
            if presetItems:
                for i in presetItems:
                    index = i.datum()
                    #
                    isExpanded = i.isExpanded()
                    expandedDic[index] = isExpanded
        #
        def refreshMethod():
            getExpandedMethod()
            schemesData = prsMtdCore.Mtd_PrsUtility._getSchemeUiDatumDic((guideKeyString,))
            presetBox.clearItems()
            if schemesData:
                for guideScheme, schemeData in schemesData.items():
                    isExpanded = True
                    if guideScheme in expandedDic:
                        isExpanded = expandedDic[guideScheme]
                    self.addGuidePresetItem(presetBox, guideKeyString, guideScheme, schemeData, isExpanded)
        #
        def saveMethod():
            presetItems = presetBox.items()
            if presetItems:
                indexLis = []
                indexFile = prsMtdCore.Mtd_PrsUtility.indexFile((guideKeyString,))
                for i in presetItems:
                    schemeKey, enable, description = i.getMainData()
                    indexLis.append((schemeKey, enable, description))
                    #
                    setFile = prsMtdCore.Mtd_PrsUtility.setFile((guideKeyString,), schemeKey)
                    setData = i.getSubData()
                    bscMethods.OsJsonFile.write(setFile, setData)
                #
                bscMethods.OsJsonFile.write(indexFile, indexLis)
            #
            refreshMethod()
            self.setGuidePresetChooseBox(treeItem)
            bscObjects.MessageWindow(
                u'保存 [ %s ] 预设' % bscMethods.StrCamelcase.toPrettify(guideKeyString),
                u'成功'
            )
        #
        guideKeyString = treeItem.keypath[0]
        toolGroupBox = treeItem.toolGroupBox
        #
        expandedDic = {}
        #
        widget = qtCore.QWidget_()
        toolGroupBox.addWidget(widget)
        toolLayout = qtCore.QHBoxLayout_(widget)
        toolLayout.setContentsMargins(4, 4, 4, 4)
        #
        widget = qtCore.QWidget_()
        toolGroupBox.addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(4, 4, 4, 4)
        presetBox = qtWidgets_.xRegisterListViewBox()
        layout.addWidget(presetBox)
        #
        self.setGuidePresetToolBar(guideKeyString, toolLayout, presetBox, (refreshMethod, saveMethod))
        refreshMethod()
    #
    def setGuidePresetToolBar(self, guideKeyString, toolLayout, presetBox, methods):
        def addMethod():
            existsSchemes = presetBox.itemNames()
            schemeKey = entryLabel.datum()
            if schemeKey and not schemeKey in existsSchemes:
                schemeData = prsMtdCore.Mtd_PrsUtility._defaultSchemeDatum()
                self.addGuidePresetItem(presetBox, guideKeyString, schemeKey, schemeData)
            #
            entryLabel.setEnterClear()
        #
        refreshMethod, saveMethod = methods
        filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        toolLayout.addWidget(filterButton)
        #
        entryLabel = guiQtWidgets.QtValueLine()
        entryLabel.setEnterEnable(True)
        entryLabel.setEnterable(True)
        entryLabel.setNameString('%s Name / Scheme' % bscMethods.StrCamelcase.toPrettify(guideKeyString))
        entryLabel.setNameTextWidth(0)
        entryLabel.setTextValidator(48)
        toolLayout.addWidget(entryLabel)
        #
        addButton = guiQtWidgets.QtIconbutton('svg_basic/add')
        toolLayout.addWidget(addButton)
        addButton.clicked.connect(addMethod)
        addButton.setTooltip(u'点击添加方案')
        #
        _refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        toolLayout.addWidget(_refreshButton)
        _refreshButton.clicked.connect(refreshMethod)
        _refreshButton.setTooltip(u'点击刷新方案')
        #
        saveButton = guiQtWidgets.QtIconbutton('svg_basic/save')
        toolLayout.addWidget(saveButton)
        saveButton.clicked.connect(saveMethod)
        saveButton.setTooltip(u'点击保存方案')
    @staticmethod
    def addGuidePresetItem(presetBox, guideKeyString, guideSchemeKey, schemeData, isExpanded=True):
        presetWidget = qtWidgets_.xPresetItemWidget()
        presetBox.addItem(presetWidget)
        #
        presetWidget.setMainData(guideSchemeKey, schemeData)
        #
        setsData = prsMtdCore.Mtd_PrsUtility._getSetUiDatumList((guideKeyString,), guideSchemeKey)
        if setsData:
            presetWidget.setSubData(setsData, isExpanded)
    # Main
    def setBuildMainPreset(self, treeItem):
        self.setMainPresetChooseBox(treeItem)
        self.setMainPresetToolboxGroup(treeItem)
        self.setToolboxGroupTitle(treeItem)
    #
    def setMainPresetChooseBox(self, treeItem):
        def setRefresh():
            refreshMethodDic = self.refreshMethodDic
            if refreshMethodDic:
                if (guideKeyString, mainPresetKey) in refreshMethodDic:
                    methods = refreshMethodDic[(guideKeyString, mainPresetKey)]
                    for i in methods:
                        i()
            #
            self.setSubPresetToolboxGroupTitle(treeItem)
        #
        guideKeyString, mainPresetKey = treeItem.keypath
        chooseBox = treeItem.chooseBox
        #
        messages = prsMtdCore.Mtd_PrsUtility._getEnabledSchemes((guideKeyString, mainPresetKey))
        chooseBox.setDatumLis(messages)
        #
        self.chooseBoxDic[(guideKeyString, mainPresetKey)] = chooseBox
        #
        chooseBox.chooseChanged.connect(setRefresh)
    #
    def setMainPresetToolboxGroup(self, treeItem):
        def getExpandedMethod():
            presetItems = presetBox.items()
            if presetItems:
                for i in presetItems:
                    index = i.datum()
                    #
                    isExpanded = i.isExpanded()
                    expandedDic[index] = isExpanded
        #
        def refreshMethod():
            getExpandedMethod()
            guideScheme = guideChooseBox.datum()
            indexData = prsMtdCore.Mtd_PrsUtility._getSchemeUiDatumDic((guideKeyString, mainPresetKey))
            presetBox.clearItems()
            if indexData:
                for index, schemeData in indexData.items():
                    isExpanded = True
                    if index in expandedDic:
                        isExpanded = expandedDic[index]
                    self.addMainPresetItem(presetBox, guideKeyString, mainPresetKey, index, schemeData, isExpanded)
        #
        def saveMethod():
            presetItems = presetBox.items()
            if presetItems:
                indexLis = []
                indexFile = prsMtdCore.Mtd_PrsUtility.indexFile((guideKeyString, mainPresetKey))
                for i in presetItems:
                    schemeKey, enable, description = i.getMainData()
                    indexLis.append((schemeKey, enable, description))
                    #
                    setFile = prsMtdCore.Mtd_PrsUtility.setFile((guideKeyString, mainPresetKey), schemeKey)
                    setData = i.getSubData()
                    bscMethods.OsJsonFile.write(setFile, setData)
                #
                bscMethods.OsJsonFile.write(indexFile, indexLis)
            #
            refreshMethod()
            self.setMainPresetChooseBox(treeItem)
            bscObjects.MessageWindow(
                u'保存 [ %s ] 预设' % bscMethods.StrCamelcase.toPrettify(mainPresetKey),
                u'成功'
            )
        #
        guideKeyString, mainPresetKey = treeItem.keypath
        chooseBox = treeItem.chooseBox
        toolGroupBox = treeItem.toolGroupBox
        #
        guideChooseBox = self.chooseBoxDic[(guideKeyString,)]
        #
        expandedDic = {}
        #
        widget = qtCore.QWidget_()
        toolGroupBox.addWidget(widget)
        toolLayout = qtCore.QHBoxLayout_(widget)
        toolLayout.setContentsMargins(4, 4, 4, 4)
        #
        widget = qtCore.QWidget_()
        toolGroupBox.addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(4, 4, 4, 4)
        presetBox = qtWidgets_.xRegisterListViewBox()
        layout.addWidget(presetBox)
        #
        self.setMainPresetToolBar(guideKeyString, mainPresetKey, toolLayout, presetBox, (refreshMethod, saveMethod))
        #
        refreshMethod()
    #
    def setMainPresetToolBar(self, guideKeyString, mainPresetKey, toolLayout, presetBox, methods):
        def addMethod():
            existsSchemes = presetBox.itemNames()
            schemeKey = entryLabel.datum()
            if schemeKey and not schemeKey in existsSchemes:
                schemeData = prsMtdCore.Mtd_PrsUtility._defaultSchemeDatum()
                self.addMainPresetItem(presetBox, guideKeyString, mainPresetKey, schemeKey, schemeData)
            #
            entryLabel.setEnterClear()
        #
        refreshMethod, saveMethod = methods
        filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        toolLayout.addWidget(filterButton)
        #
        entryLabel = guiQtWidgets.QtValueLine()
        entryLabel.setEnterEnable(True)
        entryLabel.setEnterable(True)
        entryLabel.setNameString('%s Name / Scheme' % bscMethods.StrCamelcase.toPrettify(mainPresetKey))
        entryLabel.setNameTextWidth(0)
        entryLabel.setTextValidator(48)
        toolLayout.addWidget(entryLabel)
        #
        addButton = guiQtWidgets.QtIconbutton('svg_basic/add')
        toolLayout.addWidget(addButton)
        addButton.clicked.connect(addMethod)
        addButton.setTooltip(u'点击添加方案')
        #
        _refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        toolLayout.addWidget(_refreshButton)
        _refreshButton.clicked.connect(refreshMethod)
        _refreshButton.setTooltip(u'点击刷新方案')
        #
        saveButton = guiQtWidgets.QtIconbutton('svg_basic/save')
        toolLayout.addWidget(saveButton)
        saveButton.clicked.connect(saveMethod)
        saveButton.setTooltip(u'点击保存方案')
    @staticmethod
    def addMainPresetItem(presetBox, guideKeyString, mainPresetKey, mainSchemeKey, schemeData, isExpanded=True):
        presetWidget = qtWidgets_.xPresetItemWidget()
        presetBox.addItem(presetWidget)
        #
        presetWidget.setMainData(mainSchemeKey, schemeData)
        #
        setsData = prsMtdCore.Mtd_PrsUtility._getSetUiDatumList((guideKeyString, mainPresetKey), mainSchemeKey)
        if setsData:
            presetWidget.setSubData(setsData, isExpanded)
    # Sub
    def setBuildSubPreset(self, treeItem):
        self.setSubPresetToolboxGroup(treeItem)
        #
        self.setToolboxGroupTitle(treeItem)
    #
    def setSubPresetToolboxGroup(self, treeItem):
        def getExpandedMethod():
            presetItems = presetBox.items()
            if presetItems:
                for i in presetItems:
                    index = i.datum()
                    #
                    isExpanded = i.isExpanded()
                    expandedDic[index] = isExpanded
        #
        def refreshMethod():
            getExpandedMethod()
            #
            mainScheme = schemeChooseBox.datum()
            setsData = prsMtdCore.Mtd_PrsUtility.getUiSubPresetSetDataDic(guideKeyString, mainPresetKey, subPresetKey, mainScheme)
            presetBox.clearItems()
            if setsData:
                for index, setData in setsData.items():
                    isExpanded = True
                    if index in expandedDic:
                        isExpanded = expandedDic[index]
                    self.addSubPresetItem(presetBox, guideKeyString, mainPresetKey, subPresetKey, mainScheme, index, setData, isExpanded)
            #
            schemeKey = schemeChooseBox.datum()
            # print (guideKeyString, mainPresetKey, subPresetKey), schemeKey
            # print prsCore.Mtd_PrsUtility.indexFile((guideKeyString, mainPresetKey, subPresetKey), schemeKey)
        #
        def saveMethod():
            schemeKey = schemeChooseBox.datum()
            presetItems = presetBox.items()
            if presetItems:
                indexLis = []
                setDic = {}
                indexFile = prsMtdCore.Mtd_PrsUtility.indexFile((guideKeyString, mainPresetKey, subPresetKey), schemeKey)
                setFile = prsMtdCore.Mtd_PrsUtility.setFile((guideKeyString, mainPresetKey, subPresetKey), schemeKey)
                for i in presetItems:
                    mainSetKey, enable, description = i.getMainData()
                    indexLis.append((mainSetKey, enable, description))
                    setData = i.getSubData()
                    setDic[mainSetKey] = setData
                #
                bscMethods.OsJsonFile.write(indexFile, indexLis)
                bscMethods.OsJsonFile.write(setFile, setDic)
            #
            refreshMethod()
            bscObjects.MessageWindow(
                u'保存 [ %s ] 预设' % bscMethods.StrCamelcase.toPrettify(subPresetKey),
                u'成功'
            )
        #
        guideKeyString, mainPresetKey, subPresetKey = treeItem.keypath
        toolGroupBox = treeItem.toolGroupBox
        #
        schemeChooseBox = self.chooseBoxDic[(guideKeyString, mainPresetKey)]
        #
        expandedDic = {}
        #
        widget = qtCore.QWidget_()
        toolGroupBox.addWidget(widget)
        toolLayout = qtCore.QHBoxLayout_(widget)
        toolLayout.setContentsMargins(4, 4, 4, 4)
        #
        widget = qtCore.QWidget_()
        toolGroupBox.addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(4, 4, 4, 4)
        presetBox = qtWidgets_.xRegisterListViewBox()
        layout.addWidget(presetBox)
        #
        self.setSubPresetToolBar(guideKeyString, mainPresetKey, subPresetKey, schemeChooseBox, toolLayout, presetBox, (refreshMethod, saveMethod))
        #
        refreshMethod()
        self.refreshMethodDic.setdefault((guideKeyString, mainPresetKey), []).append(refreshMethod)
    #
    def setSubPresetToolboxGroupTitle(self, parentItem):
        childItems = parentItem.childItems()
        for treeItem in childItems:
            keypath = treeItem.keypath
            if len(keypath) == 3:
                self.setToolboxGroupTitle(treeItem)
    #
    def setSubPresetToolBar(self, guideKeyString, mainPresetKey, subPresetKey, mainChooseBox, toolLayout, presetBox, methods):
        def addMethod():
            mainScheme = mainChooseBox.datum()
            existsSchemes = presetBox.itemNames()
            count = len(existsSchemes)
            preset = 'Variant_{}'.format(str(count).zfill(4))
            if preset and not preset in existsSchemes:
                setData = prsMtdCore.Mtd_PrsUtility._defaultSetDatum(subSetDatumList)
                self.addSubPresetItem(presetBox, guideKeyString, mainPresetKey, subPresetKey, mainScheme, preset, setData)
        #
        refreshMethod, saveMethod = methods
        filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        toolLayout.addWidget(filterButton)
        #
        subSetDatumList = prsMtdCore.Mtd_PrsUtility.basicSubPresetSchemeConfig((guideKeyString, mainPresetKey, subPresetKey))
        if subSetDatumList is not None:
            entryLabel = guiQtWidgets.QtValueLine()
            entryLabel.setEnterEnable(True)
            entryLabel.setEnterable(True)
            entryLabel.setNameString('Add Variant_####...')
            entryLabel.setNameTextWidth(0)
            #
            toolLayout.addWidget(entryLabel)
            addButton = guiQtWidgets.QtIconbutton('svg_basic/add')
            toolLayout.addWidget(addButton)
            addButton.clicked.connect(addMethod)
            addButton.setTooltip(u'点击添加预设')
        else:
            toolLayout.addWidget(qtWidgets_.xSpacer())
        #
        _refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        toolLayout.addWidget(_refreshButton)
        _refreshButton.clicked.connect(refreshMethod)
        _refreshButton.setTooltip(u'点击刷新预设')
        #
        saveButton = guiQtWidgets.QtIconbutton('svg_basic/save')
        toolLayout.addWidget(saveButton)
        saveButton.clicked.connect(saveMethod)
        saveButton.setTooltip(u'点击保存预设')
    @staticmethod
    def addSubPresetItem(presetBox, guideKeyString, mainPresetKey, subPresetKey, mainSchemeKey, setKey, setData, isExpanded=True):
        presetWidget = qtWidgets_.xPresetItemWidget()
        presetBox.addItem(presetWidget)
        #
        mainData, subData = setData
        presetWidget.setMainData(setKey, mainData, True)
        #
        if subData:
            presetWidget.setSubData(subData, isExpanded)
    #
    def setToolboxGroupTitle(self, treeItem):
        keypath = treeItem.keypath
        scheme = None
        toolGroupBox = treeItem.toolGroupBox
        if len(keypath) == 3:
            schemeChooseBox = self.chooseBoxDic[keypath[:2]]
            scheme = schemeChooseBox.datum()
        explains = [bscMethods.StrCamelcase.toPrettify(i) for i in keypath]
        title = bscMethods.StrCamelcase.toUiPath(explains)
        toolGroupBox.setTitle(title + ['', ' ( {} )'.format(scheme)][scheme is not None])
    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        tabView = guiQtWidgets.QtVShelfTabgroup()
        self.addWidget(tabView)
        buildData = [
            (prsConfigure.Utility.DEF_key_preset_project, 'svg_basic/project', u'项目预设'),
            (prsConfigure.Utility.DEF_key_preset_personnel, 'svg_basic/personnel', u'人员预设'),
            (prsConfigure.Utility.DEF_key_preset_pipeline, 'svg_basic/pipeline', u'流程预设'),
            (prsConfigure.Utility.DEF_key_preset_maya, 'svg_basic/maya', u'Maya预设'),
            (prsConfigure.Utility.DEF_key_preset_software, 'svg_basic/software', u'软件预设'),
            (prsConfigure.Utility.DEF_key_preset_variant, 'svg_basic/variant', u'基础预设')
        ]
        explain = '''Build Preset Panel'''
        maxValue = len(buildData)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for i in buildData:
            keyword, iconKeywordStr, tooltip = i
            progressBar.update(keyword)
            #
            widget = qtCore.QWidget_()
            tabView.addTab(widget, keyword, iconKeywordStr, tooltip)
            #
            layout = qtCore.QGridLayout_(widget)
            layout.setContentsMargins(4, 4, 4, 4)
            layout.setSpacing(2)
            self.setupPresetUnit(keyword, layout)


#
def tableShow():
    ui = IfPresetWindow()
    ui.uiShow()


#
def helpShow():
    pass
