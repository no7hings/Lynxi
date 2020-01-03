# coding=utf-8
from LxUi.qt import qtWidgets_, qtWidgets, qtCore, qtProgress, qtTip
#
from LxInterface.qt.ifBasic import ifWidgetBasic
#
from LxCore.method import _dbMethod
#
from LxMaya.method import _maMethod, _maProductMethod
#
none = ''


#
class IfScLightLinkUpdateUnit(ifWidgetBasic.IfToolUnitBasic):
    rnd_node_method = _maMethod.MaRenderNodeMethod
    app_node_method = _maMethod.MaLightNodeMethod
    app_prd_unit_method = _maProductMethod.MaProductUnitMethod
    dtb_user_method = _dbMethod.Mtd_DbUser

    UnitTitle = 'Light Rig Upload / Update'
    UnitIcon = 'window#geometryPanel'
    UnitWidth = 800
    #
    UnitScriptJobWindowName = 'scLightLinkViewerWindow'
    #
    W = 120
    #
    ToolLayoutDic_ScLightLinkUpload = {
        'ignoreUnused': [0, 0, 0, 1, 2, 'Ignore Unused'],
        1: 'Database Config',
        'lightLinkName': [W, 2, 0, 1, 4, 'Name Label(s)'],
        'branchName': [W, 3, 0, 1, 4, 'Branch Label(s)'],
        'versionName': [W, 4, 0, 1, 4, 'Version Label(s)'],
        5: 'Operation',
        'withRenderOption': [0, 6, 0, 1, 2, 'Render Option'],
        'update': [0, 7, 0, 1, 4, 'Upload / Update Light Link(s)', 'svg_basic@svg#update']
    }
    def __init__(self, *args, **kwargs):
        super(IfScLightLinkUpdateUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._overrideVar()
        #
        self.setupUnit()
    #
    def _overrideVar(self):
        self._dbUnitType = 'maya.lightLink'
        #
        self._localLightLinkDic = {}
        self._serverLightLinkDic = {}
        #
        self._localRenderOptionDic = {}
        #
        self._isRefreshTreeViewEnable = True
    #
    def refreshMethod(self):
        if self.connectObject():
            self._updateNameLabel()
            #
            self._updateLocalDatum()
            #
            self._initInfo()
            self._initView()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setScriptJob(self):
        pass
    #
    def delScriptJob(self):
        pass
    #
    def setupLeftWidget(self, layout):
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Information')
        self.setupInfoToolBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Upload')
        self.setupModifyToolBox(toolBox)
    #
    def setupRightWidget(self, layout):
        self.setupTreeViewBox(layout)
    #
    def setupInfoToolBox(self, toolBox):
        self._radarChart = qtWidgets.QtRadarchart()
        toolBox.addWidget(self._radarChart)
    #
    def setupModifyToolBox(self, toolBox):
        toolBox.setUiData(self.ToolLayoutDic_ScLightLinkUpload)
        #
        self._ignoreUnusedButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('ignoreUnused', self._ignoreUnusedButton)
        self._ignoreUnusedButton.setChecked(True)
        self._ignoreUnusedButton.setTooltip(
            '''Ignore "Illuminates by Default" is "True" and Non Link(s)'''
        )
        self._ignoreUnusedButton.checked.connect(self._initInfo)
        self._ignoreUnusedButton.checked.connect(self._initView)
        #
        self._lightLinkNameLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('lightLinkName', self._lightLinkNameLabel)
        self._lightLinkNameLabel.setEnterEnable(True)
        self._lightLinkNameLabel.chooseChanged.connect(self._initInfo)
        #
        self._branchNameLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('branchName', self._branchNameLabel)
        self._branchNameLabel.setChooseEnable(True)
        self._branchNameLabel.chooseChanged.connect(self._initInfo)
        self._branchNameLabel.setDatumLis(self.dtb_user_method.dbUserLocalUnitBranchLis())
        #
        self._versionNameLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('versionName', self._versionNameLabel)
        #
        self._withRenderOptionButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('withRenderOption', self._withRenderOptionButton)
        self._withRenderOptionButton.setChecked(True)
        #
        self._updateButton = qtWidgets.QtPressbutton()
        toolBox.addButton('update', self._updateButton)
        self._updateButton.clicked.connect(self._updateLightLinkCmd)
        self._updateButton.clicked.connect(self._updateRenderOptionCmd)
        #
        toolBox.addSeparators()
    #
    def setupTreeViewBox(self, layout):
        self._treeView = qtWidgets.QtTreeview()
        layout.addWidget(self._treeView)
        self._treeView.setSelectEnable(True)
        self._treeView.setColorEnable(True)
        #
        self._treeView.selectedChanged.connect(self.setAppObjectSelect)
        self._treeView.setFilterConnect(self.filterEnterLabel())
    #
    def _initInfo(self):
        self._updateServerDatum()
        self._updateLocalDatum()
        #
        chartDatum = self.app_node_method.getLightLinkUpdateConstantDatumLis(
            self._localLightLinkDic, self._serverLightLinkDic
        )
        #
        self._radarChart.setChartDatum(chartDatum)
        #
        self._updateVersionLabel()
    #
    def _updateNameLabel(self):
        dbUnitType = self.dtb_user_method.LxDb_Unit_Type_LightLink
        #
        nameLis = self.dtb_user_method.dbGetUserJsonUnitNameLis(dbUnitType)
        if nameLis:
            nameString = self._lightLinkNameLabel.datum()
            #
            self._lightLinkNameLabel.setChooseEnable(True)
            self._lightLinkNameLabel.setDatumLis(nameLis)
            #
            self._lightLinkNameLabel.setChoose(nameString)
        else:
            self._lightLinkNameLabel.setChooseEnable(False)
    #
    def _updateVersionLabel(self):
        entryLabel = self._versionNameLabel
        #
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = self.dtb_user_method.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        #
        versionUiDic, currentIndex = self.dtb_user_method.dbGetUserServerJsonUnitIncludeVersionUiDic(
            nameString, dbUnitType, dbUnitBranch
        )
        if versionUiDic:
            entryLabel.setDatum(versionUiDic[currentIndex][1])
    #
    def _initView(self):
        def setLightBranch(searchDatum, useDefaultSet):
            nodeType, pathDatum, namespaceDatum = eval(searchDatum)
            treeItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(treeItem)
            #
            nodeName = self.app_node_method._toNodeNameBySearchDatum(pathDatum, namespaceDatum)
            nodePath = self.app_node_method._toNodePathBySearchDatum(pathDatum, namespaceDatum)
            #
            treeItem.setNamespaceText(self.app_node_method._toNamespaceByNodeName(nodeName))
            treeItem.setNameText(self.app_node_method._toNameByNodeName(nodeName))
            treeItem.setIcon(self._lxMayaSvgIconKeyword(nodeType))
            if self.isAppExist(nodePath):
                treeItem.path = nodePath
            else:
                treeItem._setQtPressStatus(qtCore.OffStatus)
            #
            return treeItem
        #
        def setObjectBranch(linkItem, searchDatum, mainAttrName):
            nodeType, pathDatum, namespaceDatum = eval(searchDatum)
            treeItem = qtWidgets.QtTreeviewItem()
            linkItem.addChild(treeItem)
            #
            nodeName = self.app_node_method._toNodeNameBySearchDatum(pathDatum, namespaceDatum)
            nodePath = self.app_node_method._toNodePathBySearchDatum(pathDatum, namespaceDatum)
            treeItem.setNamespaceText(self.app_node_method._toNamespaceByNodeName(nodeName))
            treeItem.setNameText(self.app_node_method._toNameByNodeName(nodeName))
            treeItem.setIcon(self._lxMayaSvgIconKeyword(nodeType))
            #
            subIconKeyword = 'svg_basic@svg#unlink' if mainAttrName.lower().endswith('ignore') else 'svg_basic@svg#link'
            treeItem.setSubIcon(subIconKeyword)
            if self.isAppExist(nodePath):
                treeItem.path = nodePath
            else:
                print searchDatum, nodePath
                treeItem._setQtPressStatus(qtCore.OffStatus)
        #
        def setMain():
            datumDic = self.orderedDict(self._localLightLinkDic)
            #
            treeView.cleanItems()
            if datumDic:
                # View Progress
                explain = '''View Light Link(s)'''
                maxValue = len(datumDic)
                progressBar = qtProgress.viewSubProgress(explain, maxValue)
                for k, v in datumDic.items():
                    progressBar.updateProgress()
                    #
                    useDefaultSet = v[self.app_node_method.MaNodeName_DefaultLightSet]
                    #
                    lightItem = setLightBranch(
                        k, useDefaultSet
                    )
                    #
                    for i in searchDatumLis:
                        mainAttrName = i[0]
                        if mainAttrName in v:
                            objectDatumLis = v[mainAttrName]
                            for j in objectDatumLis:
                                setObjectBranch(lightItem, j, mainAttrName)
            #
            treeView.setRefresh()
        #
        treeView = self._treeView
        #
        searchDatumLis = [
            self.app_node_method.MaAttrNameLis_LightLink,
            self.app_node_method.MaAttrNameLis_LightLink_Ignore,
            self.app_node_method.MaAttrNameLis_ShadowLink,
            self.app_node_method.MaAttrNameLis_ShadowLink_Ignore
        ]
        #
        if self._isRefreshTreeViewEnable is True:
            setMain()
            #
            treeView.setExtendExpanded(True)
        else:
            treeView.cleanItems()
    #
    def _updateLocalDatum(self):
        isIgnoreUnused = self._ignoreUnusedButton.isChecked()
        self._localLightLinkDic = self.app_node_method.getLightLinkDic(ignoreUnused=isIgnoreUnused)
        self._localRenderOptionDic = self.rnd_node_method.getRenderOptionDic()
    #
    def _updateServerDatum(self):
        productUnit = None
        productUnitDatumDic = self.app_prd_unit_method.getProductUnitDatumDic()
        if productUnitDatumDic:
            moduleUnitDatumLis = productUnitDatumDic[self.app_prd_unit_method.LynxiProduct_Module_Asset]
            if moduleUnitDatumLis:
                productUnit = moduleUnitDatumLis[0]
        #
        if productUnit:
            pass
        #
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = self.dtb_user_method.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        self._serverLightLinkDic = self.dtb_user_method.dbReadUserJsonUnit(
            nameString, dbUnitType, dbUnitBranch
        )
    #
    def _updateLightLinkCmd(self):
        nameString = self._lightLinkNameLabel.datum()
        jsonDatum = self._localLightLinkDic
        dbUnitType = self.dtb_user_method.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        #
        if nameString and jsonDatum:
            self.dtb_user_method.dbWriteUserJsonUnit(
                nameString, dict(jsonDatum), dbUnitType, dbUnitBranch
            )
            #
            self._updateNameLabel()
            #
            qtTip.viewMessage(
                'Upload / Update Light Link(s)',
                'Complete'
            )
        #
        self._initInfo()
    #
    def _updateRenderOptionCmd(self):
        nameString = self._lightLinkNameLabel.datum()
        jsonDatum = self._localRenderOptionDic
        dbUnitType = self.LxDb_Unit_Type_RenderOption
        dbUnitBranch = self._branchNameLabel.datum()
        #
        if nameString and jsonDatum:
            self.dtb_user_method.dbWriteUserJsonUnit(
                nameString, dict(jsonDatum), dbUnitType, dbUnitBranch
            )
            #
            self._updateNameLabel()
            #
            qtTip.viewMessage(
                'Upload / Update Render Option(s)',
                'Complete'
            )
        #
    #
    def setAppObjectSelect(self):
        treeView = self._treeView
        selectedItemLis = treeView.selectedItems()
        if selectedItemLis:
            lis = []
            for i in selectedItemLis:
                if hasattr(i, 'path'):
                    lis.append(i.path)
            self.setNodeSelect(self._toNodeLis(lis))
        else:
            self.setSelectClear()
    #
    def setupUnit(self):
        def isRefreshTreeViewEnable():
            return self._isRefreshTreeViewEnable
        #
        def setRefreshTreeViewEnable():
            self._isRefreshTreeViewEnable = not self._isRefreshTreeViewEnable
        #
        self.filterButton().setActionData(
            [
                ('Config', ),
                ('Refresh View', 'checkBox', isRefreshTreeViewEnable, setRefreshTreeViewEnable)
            ]
        )
        #
        self.mainLayout().setContentsMargins(2, 2, 2, 2)
        #
        self.topToolBar().show()
        self.refreshButton().clicked.connect(self.refreshMethod)
        #
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        leftExpandWidget.setUiWidth(self.SideWidth)
        layout.addWidget(leftExpandWidget)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self.setupLeftWidget(leftScrollArea)
        #
        rightScrollBox = qtCore.QScrollArea_()
        layout.addWidget(rightScrollBox)
        self.setupRightWidget(rightScrollBox)


#
class IfScLightLinkLoadUnit(ifWidgetBasic.IfToolUnitBasic):
    app_node_method = _maMethod.MaLightNodeMethod
    app_prd_unit_method = _maProductMethod.MaProductUnitMethod
    dtb_user_method = _dbMethod.Mtd_DbUser

    UnitTitle = 'Scene Light Link Load'
    UnitIcon = 'window#geometryPanel'
    UnitWidth = 800
    #
    UnitScriptJobWindowName = 'scLightLinkViewerWindow'
    #
    W = 120
    #
    ToolLayoutDic_ScLightLinkUpload = {
        'ignorePath': [0, 0, 0, 1, 2, 'Ignore Path'], 'ignoreNamespace': [0, 0, 2, 1, 2, 'Ignore Namespace'],
        1: 'Database Config',
        'lightLinkName': [W, 2, 0, 1, 4, 'Name(s)'],
        'branchName': [W, 3, 0, 1, 4, 'Branch(s)'],
        'versionName': [W, 4, 0, 1, 4, 'Version(s)'],
        5: 'Operation',
        'load': [0, 6, 0, 1, 4, 'Load Light Link(s)', 'svg_basic@svg#load']
    }
    def __init__(self, *args, **kwargs):
        super(IfScLightLinkLoadUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._overrideVar()
        #
        self.setupUnit()
    #
    def _overrideVar(self):
        self._dbUnitType = 'maya.lightLink'
        #
        self._serverLightLinkDic = {}
        #
        self._defaultSetDatumLis = []
        self._lightLinkDatumLis = []
        #
        self._isRefreshTreeViewEnable = True
    #
    def refreshMethod(self):
        if self.connectObject():
            self._updateNameLabel()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setScriptJob(self):
        pass
    #
    def delScriptJob(self):
        pass
    #
    def setupLeftWidget(self, layout):
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Information')
        self.setupInfoToolBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Load')
        self.setupModifyToolBox(toolBox)
    #
    def setupRightWidget(self, layout):
        self.setupTreeViewBox(layout)
    #
    def setupInfoToolBox(self, toolBox):
        self._sectorChart = qtWidgets.QtSectorchart()
        toolBox.addWidget(self._sectorChart)
    #
    def setupModifyToolBox(self, toolBox):
        toolBox.setUiData(self.ToolLayoutDic_ScLightLinkUpload)
        #
        self._ignorePathButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('ignorePath', self._ignorePathButton)
        self._ignorePathButton.setChecked(True)
        self._ignorePathButton.setTooltip(
            u'''Ignore Path'''
        )
        self._ignorePathButton.checked.connect(self._initInfo)
        self._ignorePathButton.checked.connect(self._initView)
        #
        self._ignoreNamespaceButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('ignoreNamespace', self._ignoreNamespaceButton)
        self._ignoreNamespaceButton.setChecked(True)
        self._ignoreNamespaceButton.setTooltip(
            u'''Ignore Namespace'''
        )
        self._ignoreNamespaceButton.checked.connect(self._initInfo)
        self._ignoreNamespaceButton.checked.connect(self._initView)
        #
        self._lightLinkNameLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('lightLinkName', self._lightLinkNameLabel)
        self._lightLinkNameLabel.setChooseEnable(True)
        self._lightLinkNameLabel.chooseChanged.connect(self._updateBranchLabel)
        #
        self._branchNameLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('branchName', self._branchNameLabel)
        self._branchNameLabel.setChooseEnable(True)
        self._branchNameLabel.chooseChanged.connect(self._updateVersionLabel)
        #
        self._versionNameLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('versionName', self._versionNameLabel)
        self._versionNameLabel.setChooseEnable(True)
        self._versionNameLabel.chooseChanged.connect(self._initInfo)
        self._versionNameLabel.chooseChanged.connect(self._initView)
        #
        self._loadButton = qtWidgets.QtPressbutton()
        toolBox.addButton('load', self._loadButton)
        self._loadButton.clicked.connect(self._loadLightLinkCmd)
        #
        toolBox.addSeparators()
    #
    def setupTreeViewBox(self, layout):
        self._treeView = qtWidgets.QtTreeview()
        layout.addWidget(self._treeView)
        self._treeView.setSelectEnable(True)
        self._treeView.setColorEnable(True)
        #
        self._treeView.selectedChanged.connect(self.setAppObjectSelect)
        self._treeView.setFilterConnect(self.filterEnterLabel())
    #
    def _updateNameLabel(self):
        entryLabel = self._lightLinkNameLabel
        dbUnitType = self.dtb_user_method.LxDb_Unit_Type_LightLink
        #
        datumLis = self.dtb_user_method.dbGetUserJsonUnitNameLis(dbUnitType)
        if datumLis:
            entryLabel.setDatumLis(datumLis)
    #
    def _updateBranchLabel(self):
        entryLabel = self._branchNameLabel
        #
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = self.dtb_user_method.LxDb_Unit_Type_LightLink
        #
        branchLis = self.dtb_user_method.dbGetUserServerJsonUnitBranchLis(nameString, dbUnitType)
        if branchLis:
            entryLabel.setDatumLis(branchLis)
    #
    def _updateVersionLabel(self):
        entryLabel = self._versionNameLabel
        #
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = self.dtb_user_method.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        #
        versionUiDic, currentIndex = self.dtb_user_method.dbGetUserServerJsonUnitIncludeVersionUiDic(
            nameString, dbUnitType, dbUnitBranch
        )
        if versionUiDic:
            entryLabel.setExtendDatumDic(versionUiDic)
    #
    def _updateServerDatum(self):
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = self.dtb_user_method.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        #
        self._serverLightLinkDic = self.dtb_user_method.dbReadUserJsonUnit(
            nameString, dbUnitType, dbUnitBranch
        )
    #
    def _initInfo(self):
        self._updateServerDatum()
        #
        isIgnorePath, isIgnoreNamespace = self._ignorePathButton.isChecked(), self._ignoreNamespaceButton.isChecked()
        chartDatum = self.app_node_method.getLightLinkLoadConstantDatumLis(
            self._serverLightLinkDic,
            ignorePath=isIgnorePath, ignoreNamespace=isIgnoreNamespace
        )
        #
        self._sectorChart.setChartDatum(
            chartDatum
        )
    #
    def _initView(self):
        def setLightBranch(searchDatum, serverDefaultSet, defaultSetLis):
            lis = []
            nodeType, pathDatum, namespaceDatum = eval(searchDatum)
            #
            nodeName = self.app_node_method._toNodeNameBySearchDatum(pathDatum, namespaceDatum)
            localNodeLis = self.app_node_method.getNodeLisBySearchDatum(
                nodeType, pathDatum, namespaceDatum,
                ignorePath=isIgnorePath, ignoreNamespace=isIgnoreNamespace
            )
            if localNodeLis:
                for seq, nodePath in enumerate(localNodeLis):
                    localDefaultSet = nodePath in defaultSetLis
                    treeItem = qtWidgets.QtTreeviewItem()
                    treeView.addItem(treeItem)
                    treeItem.setNamespaceText(self.app_node_method._toNamespaceByNodeName(nodeName))
                    treeItem.setNameText(self.app_node_method._toNameByNodeName(nodeName))
                    treeItem.setIcon(self._lxMayaSvgIconKeyword(nodeType))
                    treeItem.path = nodePath
                    #
                    if seq > 0:
                        treeItem._setQtPressStatus(qtCore.WarningStatus)
                    #
                    if localDefaultSet == serverDefaultSet:
                        treeItem.setFilterColor((63, 255, 127, 255))
                    else:
                        self._defaultSetDatumLis.append(
                            (nodePath, serverDefaultSet)
                        )
                    #
                    lis.append(treeItem)
            else:
                treeItem = qtWidgets.QtTreeviewItem()
                treeView.addItem(treeItem)
                treeItem.setNamespaceText(self.app_node_method._toNamespaceByNodeName(nodeName))
                treeItem.setNameText(self.app_node_method._toNameByNodeName(nodeName))
                treeItem.setIcon(self._lxMayaSvgIconKeyword(nodeType))
                treeItem._setQtPressStatus(qtCore.OffStatus)
                #
                lis.append(treeItem)
            #
            return lis
        #
        def setObjectBranch(parentItem, searchDatum, mainAttrName, lightNodePath, localLightLinkObjectLis):
            nodeType, pathDatum, namespaceDatum = eval(searchDatum)
            #
            nodeName = self.app_node_method._toNodeNameBySearchDatum(pathDatum, namespaceDatum)

            localNodeLis = self.app_node_method.getNodeLisBySearchDatum(
                nodeType, pathDatum, namespaceDatum,
                ignorePath=isIgnorePath, ignoreNamespace=isIgnoreNamespace
            )
            if localNodeLis:
                for seq, nodePath in enumerate(localNodeLis):
                    treeItem = qtWidgets.QtTreeviewItem()
                    parentItem.addChild(treeItem)
                    treeItem.setNamespaceText(self.app_node_method._toNamespaceByNodeName(nodeName))
                    treeItem.setNameText(self.app_node_method._toNameByNodeName(nodeName))
                    treeItem.setIcon(self._lxMayaSvgIconKeyword(nodeType))
                    subIconKeyword = 'svg_basic@svg#unlink' if mainAttrName.lower().endswith('ignore') else 'svg_basic@svg#link'
                    treeItem.setSubIcon(subIconKeyword)
                    #
                    treeItem.path = nodePath
                    #
                    if seq > 0:
                        treeItem._setQtPressStatus(qtCore.WarningStatus)
                    #
                    if lightNodePath is not None:
                        if nodePath in localLightLinkObjectLis:
                            treeItem.setFilterColor((63, 255, 127, 255))
                        else:
                            self._lightLinkDatumLis.append(
                                (mainAttrName, lightNodePath, nodePath)
                            )
            else:
                treeItem = qtWidgets.QtTreeviewItem()
                parentItem.addChild(treeItem)
                treeItem.setNamespaceText(self.app_node_method._toNamespaceByNodeName(nodeName))
                treeItem.setNameText(self.app_node_method._toNameByNodeName(nodeName))
                treeItem.setIcon(self._lxMayaSvgIconKeyword(nodeType))
                subIconKeyword = 'svg_basic@svg#unlink' if mainAttrName.lower().endswith('ignore') else 'svg_basic@svg#link'
                treeItem.setSubIcon(subIconKeyword)
                #
                treeItem._setQtPressStatus(qtCore.OffStatus)
        #
        def setMain():
            dataDic = self._serverLightLinkDic
            #
            treeView.cleanItems()
            if dataDic:
                # View Progress
                explain = '''View Light Link(s)'''
                maxValue = len(dataDic)
                progressBar = qtProgress.viewSubProgress(explain, maxValue)
                #
                defaultSetLis = self.app_node_method.getLightDefaultSetLis()
                for k, v in dataDic.items():
                    progressBar.updateProgress()
                    #
                    serverDefaultSet = v[self.app_node_method.MaNodeName_DefaultLightSet]
                    #
                    lightItemLis = setLightBranch(k, serverDefaultSet, defaultSetLis)
                    for lightItem in lightItemLis:
                        for i in searchDatumLis:
                            mainAttrName = i[0]
                            if mainAttrName in v:
                                if hasattr(lightItem, 'path'):
                                    lightNodePath = lightItem.path
                                    localLightLinkObjectLis = self.app_node_method.getLightLinkObjectLis(
                                        lightNodePath, *i[1:]
                                    )
                                else:
                                    lightNodePath = None
                                    localLightLinkObjectLis = []
                                #
                                objectSearchDatumLis = v[mainAttrName]
                                for objectSearchDatum in objectSearchDatumLis:
                                    setObjectBranch(
                                        lightItem, objectSearchDatum,
                                        mainAttrName, lightNodePath, localLightLinkObjectLis
                                    )
                #
                self._jsonDatum = dataDic
            #
            treeView.setRefresh()
        #
        self._defaultSetDatumLis = []
        self._lightLinkDatumLis = []
        #
        treeView = self._treeView
        #
        isIgnoreNamespace = self._ignoreNamespaceButton.isChecked()
        isIgnorePath = self._ignorePathButton.isChecked()
        #
        searchDatumLis = [
            self.app_node_method.MaAttrNameLis_LightLink,
            self.app_node_method.MaAttrNameLis_LightLink_Ignore,
            self.app_node_method.MaAttrNameLis_ShadowLink,
            self.app_node_method.MaAttrNameLis_ShadowLink_Ignore
        ]
        #
        if self._isRefreshTreeViewEnable is True:
            setMain()
            #
            treeView.setExtendExpanded(True)
        else:
            treeView.cleanItems()
    #
    def _loadLightLinkCmd(self):
        defaultSetDatum = self._defaultSetDatumLis
        if defaultSetDatum:
            self.setLightDefaultSet(defaultSetDatum)
            qtTip.viewMessage(
                'Load Light Default Set(s)',
                'Complete'
            )
        #
        lightLinkDatum = self._lightLinkDatumLis
        if lightLinkDatum:
            self.setLightLink(lightLinkDatum)
            #
            qtTip.viewMessage(
                'Load Light Link(s)',
                'Complete'
            )
        #
        self._initInfo()
        self._initView()
    #
    def setAppObjectSelect(self):
        treeView = self._treeView
        selectedItemLis = treeView.selectedItems()
        if selectedItemLis:
            lis = []
            for i in selectedItemLis:
                if hasattr(i, 'path'):
                    lis.append(i.path)
            #
            self.setNodeSelect(self._toNodeLis(lis))
        else:
            self.setSelectClear()
    #
    def setupUnit(self):
        def isRefreshTreeViewEnable():
            return self._isRefreshTreeViewEnable
        #
        def setRefreshTreeViewEnable():
            self._isRefreshTreeViewEnable = not self._isRefreshTreeViewEnable
        #
        self.filterButton().setActionData(
            [
                ('Config', ),
                ('Refresh View', 'checkBox', isRefreshTreeViewEnable, setRefreshTreeViewEnable)
            ]
        )
        #
        self.mainLayout().setContentsMargins(2, 2, 2, 2)
        #
        self.topToolBar().show()
        self.refreshButton().clicked.connect(self.refreshMethod)
        #
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        leftExpandWidget.setUiWidth(self.SideWidth)
        layout.addWidget(leftExpandWidget)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self.setupLeftWidget(leftScrollArea)
        #
        rightScrollBox = qtCore.QScrollArea_()
        layout.addWidget(rightScrollBox)
        self.setupRightWidget(rightScrollBox)
