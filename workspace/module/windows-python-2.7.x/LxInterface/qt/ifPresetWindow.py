# coding=utf-8
from LxBasic import bscMethods, bscObjects

from LxScheme import shmOutput

from LxCore import lxConfigure

from LxCore.preset import basicPr

from LxUi import uiCore

from LxUi.qt import qtModifiers, qtWidgets_, qtWidgets, qtCore


#
class IfPresetWindow(qtWidgets.QtToolWindow):
    leftBoxWidth = 320
    widthSet = 55
    SideWidth = 480
    #
    _Title = 'Preset'
    _Version = shmOutput.Resource().version
    def __init__(self):
        super(IfPresetWindow, self).__init__()

        self.setDefaultSize(*uiCore.Lynxi_Ui_Window_Size_Default)
        self.setMargins(0, 0, 0, 0)
        #
        self.setNameText(self._Title)
        self.setIndexText(self._Version)
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
        leftExpandWidget.setUiWidth(self.SideWidth)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self.setupLeftWidget(key, leftScrollArea)
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
    def setupLeftWidget(self, key, layout):
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
            self.SideWidth - 20
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
        def setBranch(presetKeys):
            def setTreeItem():
                if explainKey:
                    treeItem.setText(0, bscMethods.StrCamelcase.toPrettify(explainKey))
                    iconKeyword = ['svg_basic@svg#project', 'svg_basic@svg#branch_main', 'svg_basic@svg#tag'][len(presetKeys) - 1]
                    treeItem.setItemIcon_(0, iconKeyword)
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
            treeItemDic[presetKeys] = treeItem
            #
            chooseBox = qtWidgets.QtEnterlabel()
            #
            toolGroupBox = qtWidgets.QtToolboxGroup()
            treeItem.toolGroupBox = toolGroupBox
            treeItem.chooseBox = chooseBox
            treeItem.presetKeys = presetKeys
            # Guide
            if len(presetKeys) == 1:
                guidePresetKey = presetKeys[0]
                explainKey = guidePresetKey
                setTreeItem()
                setChooseBox()
                setToolGroup()
                self.setBuildGuidePreset(treeItem)
            # Main
            elif len(presetKeys) == 2:
                guidePresetKey, mainPresetKey = presetKeys
                parentKey = (guidePresetKey,)
                explainKey = mainPresetKey
                setTreeItem()
                if presetKeys in basicPr.basicMainPresetKeySchemeConfig():
                    setChooseBox()
                setToolGroup()
                self.setBuildMainPreset(treeItem)
            # Sub
            elif len(presetKeys) == 3:
                guidePresetKey, mainPresetKey, subPresetKey = presetKeys
                parentKey = (guidePresetKey, mainPresetKey)
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
        basicData = basicPr.basicPresetConfig(key)
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
            mainSchemeData = basicPr.getPresetSetDic((guidePresetKey, ), guideSchemeKey)
            self.setMaxProgressValue(len(mainSchemeData))
            for k, v in mainSchemeData.items():
                self.updateProgress()
                mainPresetKey = k
                mainSchemeKey = v
                mainChooseBox = self.chooseBoxDic[(guidePresetKey, mainPresetKey)]
                message = mainChooseBox.datum()
                if not message == mainSchemeKey:
                    mainChooseBox.setChoose(mainSchemeKey)
            #
            self.setSubPresetToolboxGroupTitle(treeItem)
        #
        guidePresetKey = treeItem.presetKeys[0]
        chooseBox = treeItem.chooseBox
        #
        messages = basicPr.getPresetSchemes((guidePresetKey, ))
        chooseBox.setDatumLis(messages)
        #
        self.chooseBoxDic[(guidePresetKey, )] = chooseBox
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
            schemesData = basicPr.getUiPresetSchemeDataDic((guidePresetKey, ))
            presetBox.clearItems()
            if schemesData:
                for guideScheme, schemeData in schemesData.items():
                    isExpanded = True
                    if guideScheme in expandedDic:
                        isExpanded = expandedDic[guideScheme]
                    self.addGuidePresetItem(presetBox, guidePresetKey, guideScheme, schemeData, isExpanded)
        #
        def saveMethod():
            presetItems = presetBox.items()
            if presetItems:
                indexLis = []
                indexFile = basicPr.presetIndexFileMethod((guidePresetKey, ))
                for i in presetItems:
                    schemeKey, enable, description = i.getMainData()
                    indexLis.append((schemeKey, enable, description))
                    #
                    setFile = basicPr.presetSetFileMethod((guidePresetKey, ), schemeKey)
                    setData = i.getSubData()
                    bscMethods.OsJson.write(setFile, setData)
                #
                bscMethods.OsJson.write(indexFile, indexLis)
            #
            refreshMethod()
            self.setGuidePresetChooseBox(treeItem)
            bscObjects.If_Message(
                u'保存 [ %s ] 预设' % bscMethods.StrCamelcase.toPrettify(guidePresetKey),
                u'成功'
            )
        #
        guidePresetKey = treeItem.presetKeys[0]
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
        self.setGuidePresetToolBar(guidePresetKey, toolLayout, presetBox, (refreshMethod, saveMethod))
        refreshMethod()
    #
    def setGuidePresetToolBar(self, guidePresetKey, toolLayout, presetBox, methods):
        def addMethod():
            existsSchemes = presetBox.itemNames()
            schemeKey = entryLabel.datum()
            if schemeKey and not schemeKey in existsSchemes:
                schemeData = basicPr.defaultSchemeConfig()
                self.addGuidePresetItem(presetBox, guidePresetKey, schemeKey, schemeData)
            #
            entryLabel.setEnterClear()
        #
        refreshMethod, saveMethod = methods
        filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        toolLayout.addWidget(filterButton)
        #
        entryLabel = qtWidgets.QtEnterlabel()
        entryLabel.setEnterEnable(True)
        entryLabel.setEnterable(True)
        entryLabel.setNameText('%s Name / Scheme' % bscMethods.StrCamelcase.toPrettify(guidePresetKey))
        entryLabel.setNameTextWidth(0)
        entryLabel.setTextValidator(48)
        toolLayout.addWidget(entryLabel)
        #
        addButton = qtWidgets.QtIconbutton('svg_basic@svg#add')
        toolLayout.addWidget(addButton)
        addButton.clicked.connect(addMethod)
        addButton.setTooltip(u'点击添加方案')
        #
        _refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
        toolLayout.addWidget(_refreshButton)
        _refreshButton.clicked.connect(refreshMethod)
        _refreshButton.setTooltip(u'点击刷新方案')
        #
        saveButton = qtWidgets.QtIconbutton('svg_basic@svg#save')
        toolLayout.addWidget(saveButton)
        saveButton.clicked.connect(saveMethod)
        saveButton.setTooltip(u'点击保存方案')
    @staticmethod
    def addGuidePresetItem(presetBox, guidePresetKey, guideSchemeKey, schemeData, isExpanded=True):
        presetWidget = qtWidgets_.xPresetItemWidget()
        presetBox.addItem(presetWidget)
        #
        presetWidget.setMainData(guideSchemeKey, schemeData)
        #
        setsData = basicPr.getUiPresetSetDataLis((guidePresetKey, ), guideSchemeKey)
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
                if (guidePresetKey, mainPresetKey) in refreshMethodDic:
                    methods = refreshMethodDic[(guidePresetKey, mainPresetKey)]
                    for i in methods:
                        i()
            #
            self.setSubPresetToolboxGroupTitle(treeItem)
        #
        guidePresetKey, mainPresetKey = treeItem.presetKeys
        chooseBox = treeItem.chooseBox
        #
        messages = basicPr.getPresetSchemes((guidePresetKey, mainPresetKey))
        chooseBox.setDatumLis(messages)
        #
        self.chooseBoxDic[(guidePresetKey, mainPresetKey)] = chooseBox
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
            indexData = basicPr.getUiPresetSchemeDataDic((guidePresetKey, mainPresetKey))
            presetBox.clearItems()
            if indexData:
                for index, schemeData in indexData.items():
                    isExpanded = True
                    if index in expandedDic:
                        isExpanded = expandedDic[index]
                    self.addMainPresetItem(presetBox, guidePresetKey, mainPresetKey, index, schemeData, isExpanded)
        #
        def saveMethod():
            presetItems = presetBox.items()
            if presetItems:
                indexLis = []
                indexFile = basicPr.presetIndexFileMethod((guidePresetKey, mainPresetKey))
                for i in presetItems:
                    schemeKey, enable, description = i.getMainData()
                    indexLis.append((schemeKey, enable, description))
                    #
                    setFile = basicPr.presetSetFileMethod((guidePresetKey, mainPresetKey), schemeKey)
                    setData = i.getSubData()
                    bscMethods.OsJson.write(setFile, setData)
                #
                bscMethods.OsJson.write(indexFile, indexLis)
            #
            refreshMethod()
            self.setMainPresetChooseBox(treeItem)
            bscObjects.If_Message(
                u'保存 [ %s ] 预设' % bscMethods.StrCamelcase.toPrettify(mainPresetKey),
                u'成功'
            )
        #
        guidePresetKey, mainPresetKey = treeItem.presetKeys
        chooseBox = treeItem.chooseBox
        toolGroupBox = treeItem.toolGroupBox
        #
        guideChooseBox = self.chooseBoxDic[(guidePresetKey,)]
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
        self.setMainPresetToolBar(guidePresetKey, mainPresetKey, toolLayout, presetBox, (refreshMethod, saveMethod))
        #
        refreshMethod()
    #
    def setMainPresetToolBar(self, guidePresetKey, mainPresetKey, toolLayout, presetBox, methods):
        def addMethod():
            existsSchemes = presetBox.itemNames()
            schemeKey = entryLabel.datum()
            if schemeKey and not schemeKey in existsSchemes:
                schemeData = basicPr.defaultSchemeConfig()
                self.addMainPresetItem(presetBox, guidePresetKey, mainPresetKey, schemeKey, schemeData)
            #
            entryLabel.setEnterClear()
        #
        refreshMethod, saveMethod = methods
        filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        toolLayout.addWidget(filterButton)
        #
        entryLabel = qtWidgets.QtEnterlabel()
        entryLabel.setEnterEnable(True)
        entryLabel.setEnterable(True)
        entryLabel.setNameText('%s Name / Scheme' % bscMethods.StrCamelcase.toPrettify(mainPresetKey))
        entryLabel.setNameTextWidth(0)
        entryLabel.setTextValidator(48)
        toolLayout.addWidget(entryLabel)
        #
        addButton = qtWidgets.QtIconbutton('svg_basic@svg#add')
        toolLayout.addWidget(addButton)
        addButton.clicked.connect(addMethod)
        addButton.setTooltip(u'点击添加方案')
        #
        _refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
        toolLayout.addWidget(_refreshButton)
        _refreshButton.clicked.connect(refreshMethod)
        _refreshButton.setTooltip(u'点击刷新方案')
        #
        saveButton = qtWidgets.QtIconbutton('svg_basic@svg#save')
        toolLayout.addWidget(saveButton)
        saveButton.clicked.connect(saveMethod)
        saveButton.setTooltip(u'点击保存方案')
    @staticmethod
    def addMainPresetItem(presetBox, guidePresetKey, mainPresetKey, mainSchemeKey, schemeData, isExpanded=True):
        presetWidget = qtWidgets_.xPresetItemWidget()
        presetBox.addItem(presetWidget)
        #
        presetWidget.setMainData(mainSchemeKey, schemeData)
        #
        setsData = basicPr.getUiPresetSetDataLis((guidePresetKey, mainPresetKey), mainSchemeKey)
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
            setsData = basicPr.getUiSubPresetSetDataDic(guidePresetKey, mainPresetKey, subPresetKey, mainScheme)
            presetBox.clearItems()
            if setsData:
                for index, setData in setsData.items():
                    isExpanded = True
                    if index in expandedDic:
                        isExpanded = expandedDic[index]
                    self.addSubPresetItem(presetBox, guidePresetKey, mainPresetKey, subPresetKey, mainScheme, index, setData, isExpanded)
            #
            schemeKey = schemeChooseBox.datum()
            # print (guidePresetKey, mainPresetKey, subPresetKey), schemeKey
            # print basicPr.presetIndexFileMethod((guidePresetKey, mainPresetKey, subPresetKey), schemeKey)
        #
        def saveMethod():
            schemeKey = schemeChooseBox.datum()
            presetItems = presetBox.items()
            if presetItems:
                indexLis = []
                setDic = {}
                indexFile = basicPr.presetIndexFileMethod((guidePresetKey, mainPresetKey, subPresetKey), schemeKey)
                setFile = basicPr.presetSetFileMethod((guidePresetKey, mainPresetKey, subPresetKey), schemeKey)
                for i in presetItems:
                    mainSetKey, enable, description = i.getMainData()
                    indexLis.append((mainSetKey, enable, description))
                    setData = i.getSubData()
                    setDic[mainSetKey] = setData
                #
                bscMethods.OsJson.write(indexFile, indexLis)
                bscMethods.OsJson.write(setFile, setDic)
            #
            refreshMethod()
            bscObjects.If_Message(
                u'保存 [ %s ] 预设' % bscMethods.StrCamelcase.toPrettify(subPresetKey),
                u'成功'
            )
        #
        guidePresetKey, mainPresetKey, subPresetKey = treeItem.presetKeys
        toolGroupBox = treeItem.toolGroupBox
        #
        schemeChooseBox = self.chooseBoxDic[(guidePresetKey, mainPresetKey)]
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
        self.setSubPresetToolBar(guidePresetKey, mainPresetKey, subPresetKey, schemeChooseBox, toolLayout, presetBox, (refreshMethod, saveMethod))
        #
        refreshMethod()
        self.refreshMethodDic.setdefault((guidePresetKey, mainPresetKey), []).append(refreshMethod)
    #
    def setSubPresetToolboxGroupTitle(self, parentItem):
        childItems = parentItem.childItems()
        for treeItem in childItems:
            presetKeys = treeItem.presetKeys
            if len(presetKeys) == 3:
                self.setToolboxGroupTitle(treeItem)
    #
    def setSubPresetToolBar(self, guidePresetKey, mainPresetKey, subPresetKey, mainChooseBox, toolLayout, presetBox, methods):
        def addMethod():
            mainScheme = mainChooseBox.datum()
            existsSchemes = presetBox.itemNames()
            count = len(existsSchemes)
            preset = 'Variant_{}'.format(str(count).zfill(4))
            if preset and not preset in existsSchemes:
                setData = basicPr.defaultSetConfig(subSetDatas)
                self.addSubPresetItem(presetBox, guidePresetKey, mainPresetKey, subPresetKey, mainScheme, preset, setData)
        #
        refreshMethod, saveMethod = methods
        filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        toolLayout.addWidget(filterButton)
        #
        subSetDatas = basicPr.basicSubPresetSchemeConfig((guidePresetKey, mainPresetKey, subPresetKey))
        if subSetDatas is not None:
            entryLabel = qtWidgets.QtEnterlabel()
            entryLabel.setEnterEnable(True)
            entryLabel.setEnterable(True)
            entryLabel.setNameText('Add Variant_####...')
            entryLabel.setNameTextWidth(0)
            #
            toolLayout.addWidget(entryLabel)
            addButton = qtWidgets.QtIconbutton('svg_basic@svg#add')
            toolLayout.addWidget(addButton)
            addButton.clicked.connect(addMethod)
            addButton.setTooltip(u'点击添加预设')
        else:
            toolLayout.addWidget(qtWidgets_.xSpacer())
        #
        _refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
        toolLayout.addWidget(_refreshButton)
        _refreshButton.clicked.connect(refreshMethod)
        _refreshButton.setTooltip(u'点击刷新预设')
        #
        saveButton = qtWidgets.QtIconbutton('svg_basic@svg#save')
        toolLayout.addWidget(saveButton)
        saveButton.clicked.connect(saveMethod)
        saveButton.setTooltip(u'点击保存预设')
    @staticmethod
    def addSubPresetItem(presetBox, guidePresetKey, mainPresetKey, subPresetKey, mainSchemeKey, setKey, setData, isExpanded=True):
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
        presetKeys = treeItem.presetKeys
        scheme = None
        toolGroupBox = treeItem.toolGroupBox
        if len(presetKeys) == 3:
            schemeChooseBox = self.chooseBoxDic[presetKeys[:2]]
            scheme = schemeChooseBox.datum()
        explains = [bscMethods.StrCamelcase.toPrettify(i) for i in presetKeys]
        title = bscMethods.StrCamelcase.toUiPath(explains)
        toolGroupBox.setTitle(title + ['', ' ( {} )'.format(scheme)][scheme is not None])
    @qtModifiers.mtdInterfaceShowExclusive
    def windowShow(self):
        self.uiShow()
    @staticmethod
    def helpShow():
        pass
    #
    def setupWindow(self):
        tabView = qtWidgets.QtVShelfTabgroup()
        self.addWidget(tabView)
        buildData = [
            (lxConfigure.DEF_preset_key_Project, 'svg_basic@svg#project', u'项目预设'),
            (lxConfigure.DEF_preset_key_personnel, 'svg_basic@svg#personnel', u'人员预设'),
            (lxConfigure.Lynxi_Key_Pipeline, 'svg_basic@svg#pipeline', u'流程预设'),
            (lxConfigure.DEF_preset_key_Maya, 'svg_basic@svg#maya', u'Maya预设'),
            (lxConfigure.DEF_preset_key_Software, 'svg_basic@svg#software', u'软件预设'),
            (lxConfigure.DEF_preset_key_variant, 'svg_basic@svg#variant', u'基础预设')
        ]
        explain = '''Build Preset Panel'''
        maxValue = len(buildData)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        for i in buildData:
            keyword, iconKeyword, tooltip = i
            progressBar.update(keyword)
            #
            widget = qtCore.QWidget_()
            tabView.addTab(widget, keyword, iconKeyword, tooltip)
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
