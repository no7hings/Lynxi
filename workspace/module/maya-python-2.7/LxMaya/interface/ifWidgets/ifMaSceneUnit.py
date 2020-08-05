# coding=utf-8
from LxBasic import bscMtdCore, bscMethods, bscObjects

from LxPreset import prsMethods

from LxGui.qt import qtWidgets_, guiQtWidgets, qtCore
#
from LxKit.qt import kitQtWgtAbs
#
from LxDatabase import dtbMethods
#
from LxMaya.method import _maMethod, _maProductMethod
#
none = ''


#
class IfScLightLinkUpdateUnit(kitQtWgtAbs.IfToolUnitBasic):
    mtd_app_rnd_node = _maMethod.MaRenderNodeMethod
    mtd_app_node = _maMethod.MaLightNodeMethod
    mtd_app_prd_unit = _maProductMethod.MaProductUnitMethod

    VAR_kit__qt_wgt__unit__uiname = 'Light Rig Upload / Update'
    VAR_kit__qt_wgt__unit__icon = 'window/geometryPanel'
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
        'update': [0, 7, 0, 1, 4, 'Upload / Update Light Link(s)', 'svg_basic/update']
    }
    def __init__(self, *args, **kwargs):
        super(IfScLightLinkUpdateUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._overrideVar()
        #
        self._kit__unit__set_build_()
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
    def _kit__unit__set_left_build_(self, layout):
        toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Information')
        self.setupInfoToolBox(toolBox)
        #
        toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Upload')
        self.setupModifyToolBox(toolBox)
    #
    def setupRightWidget(self, layout):
        self.setupTreeViewBox(layout)
    #
    def setupInfoToolBox(self, toolBox):
        self._radarChart = guiQtWidgets.QtRadarchart()
        toolBox.addWidget(self._radarChart)
    #
    def setupModifyToolBox(self, toolBox):
        toolBox.setUiData(self.ToolLayoutDic_ScLightLinkUpload)
        #
        self._ignoreUnusedButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('ignoreUnused', self._ignoreUnusedButton)
        self._ignoreUnusedButton.setChecked(True)
        self._ignoreUnusedButton.setTooltip(
            '''Ignore "Illuminates by Default" is "True" and Non Link(s)'''
        )
        self._ignoreUnusedButton.checked.connect(self._initInfo)
        self._ignoreUnusedButton.checked.connect(self._initView)
        #
        self._lightLinkNameLabel = guiQtWidgets.QtValueLine()
        toolBox.addInfo('lightLinkName', self._lightLinkNameLabel)
        self._lightLinkNameLabel.setEnterEnable(True)
        self._lightLinkNameLabel.chooseChanged.connect(self._initInfo)
        #
        self._branchNameLabel = guiQtWidgets.QtValueLine()
        toolBox.addInfo('branchName', self._branchNameLabel)
        self._branchNameLabel.setChooseEnable(True)
        self._branchNameLabel.chooseChanged.connect(self._initInfo)
        self._branchNameLabel.setDatumLis(dtbMethods.DtbUser.dbUserLocalUnitBranchLis())
        #
        self._versionNameLabel = guiQtWidgets.QtValueLine()
        toolBox.addInfo('versionName', self._versionNameLabel)
        #
        self._withRenderOptionButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('withRenderOption', self._withRenderOptionButton)
        self._withRenderOptionButton.setChecked(True)
        #
        self._updateButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('update', self._updateButton)
        self._updateButton.clicked.connect(self._updateLightLinkCmd)
        self._updateButton.clicked.connect(self._updateRenderOptionCmd)
        #
        toolBox.addSeparators()
    #
    def setupTreeViewBox(self, layout):
        self._treeView = guiQtWidgets.QtTreeview()
        layout.addWidget(self._treeView)
        self._treeView.setSelectEnable(True)
        self._treeView.setColorEnable(True)
        #
        self._treeView.selectedChanged.connect(self.setAppObjectSelect)
        self._treeView.setKeywordFilterWidgetConnect(self.filterEnterLabel())
    #
    def _initInfo(self):
        self._updateServerDatum()
        self._updateLocalDatum()
        #
        chartDatum = self.mtd_app_node.getLightLinkUpdateConstantDatumLis(
            self._localLightLinkDic, self._serverLightLinkDic
        )
        #
        self._radarChart.setChartDatum(chartDatum)
        #
        self._updateVersionLabel()
    #
    def _updateNameLabel(self):
        dbUnitType = dtbMethods.DtbUser.LxDb_Unit_Type_LightLink
        #
        nameLis = dtbMethods.DtbUser.dbGetUserJsonUnitNameLis(dbUnitType)
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
        dbUnitType = dtbMethods.DtbUser.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        #
        versionUiDic, currentIndex = dtbMethods.DtbUser.dbGetUserServerJsonUnitIncludeVersionUiDic(
            nameString, dbUnitType, dbUnitBranch
        )
        if versionUiDic:
            entryLabel.setDatum(versionUiDic[currentIndex][1])
    #
    def _initView(self):
        def setLightBranch(searchDatum, useDefaultSet):
            nodeType, pathDatum, namespaceDatum = eval(searchDatum)
            treeItem = guiQtWidgets.QtTreeItem()
            treeView.addItem(treeItem)
            #
            nodeName = self.mtd_app_node._toNodeNameBySearchDatum(pathDatum, namespaceDatum)
            nodePath = self.mtd_app_node._toNodePathBySearchDatum(pathDatum, namespaceDatum)
            #
            treeItem.setNamespaceText(self.mtd_app_node._toNamespaceByNodeName(nodeName))
            treeItem.setNameString(self.mtd_app_node._toNameByNodeName(nodeName))
            treeItem.setIcon(bscMethods.IconKeyword.mayaSvg(nodeType))
            if self._isAppExist(nodePath):
                treeItem.path = nodePath
            else:
                treeItem._setQtPressStatus(qtCore.OffStatus)
            #
            return treeItem
        #
        def setObjectBranch(linkItem, searchDatum, mainAttrName):
            nodeType, pathDatum, namespaceDatum = eval(searchDatum)
            treeItem = guiQtWidgets.QtTreeItem()
            linkItem.addChild(treeItem)
            #
            nodeName = self.mtd_app_node._toNodeNameBySearchDatum(pathDatum, namespaceDatum)
            nodePath = self.mtd_app_node._toNodePathBySearchDatum(pathDatum, namespaceDatum)
            treeItem.setNamespaceText(self.mtd_app_node._toNamespaceByNodeName(nodeName))
            treeItem.setNameString(self.mtd_app_node._toNameByNodeName(nodeName))
            treeItem.setIcon(bscMethods.IconKeyword.mayaSvg(nodeType))
            #
            subIconKeyword = 'svg_basic/unlink' if mainAttrName.lower().endswith('ignore') else 'svg_basic/link'
            treeItem.setSubIcon(subIconKeyword)
            if self._isAppExist(nodePath):
                treeItem.path = nodePath
            else:
                print searchDatum, nodePath
                treeItem._setQtPressStatus(qtCore.OffStatus)
        #
        def setMain():
            datumDic = bscMtdCore.orderedDict(self._localLightLinkDic)
            #
            treeView.cleanItems()
            if datumDic:
                # View Progress
                explain = '''View Light Link(s)'''
                maxValue = len(datumDic)
                progressBar = bscObjects.ProgressWindow(explain, maxValue)
                for k, v in datumDic.items():
                    progressBar.update()
                    #
                    useDefaultSet = v[self.mtd_app_node.MaNodeName_DefaultLightSet]
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
            self.mtd_app_node.MaAttrNameLis_LightLink,
            self.mtd_app_node.MaAttrNameLis_LightLink_Ignore,
            self.mtd_app_node.MaAttrNameLis_ShadowLink,
            self.mtd_app_node.MaAttrNameLis_ShadowLink_Ignore
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
        self._localLightLinkDic = self.mtd_app_node.getLightLinkDic(ignoreUnused=isIgnoreUnused)
        self._localRenderOptionDic = self.mtd_app_rnd_node.getRenderOptionDic()
    #
    def _updateServerDatum(self):
        productUnit = None
        productUnitDatumDic = self.mtd_app_prd_unit.getProductUnitDatumDic()
        if productUnitDatumDic:
            moduleUnitDatumLis = productUnitDatumDic[prsMethods.Asset.moduleName()]
            if moduleUnitDatumLis:
                productUnit = moduleUnitDatumLis[0]
        #
        if productUnit:
            pass
        #
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = dtbMethods.DtbUser.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        self._serverLightLinkDic = dtbMethods.DtbUser.dbReadUserJsonUnit(
            nameString, dbUnitType, dbUnitBranch
        )
    #
    def _updateLightLinkCmd(self):
        nameString = self._lightLinkNameLabel.datum()
        jsonDatum = self._localLightLinkDic
        dbUnitType = dtbMethods.DtbUser.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        #
        if nameString and jsonDatum:
            dtbMethods.DtbUser.dbWriteUserJsonUnit(
                nameString, dict(jsonDatum), dbUnitType, dbUnitBranch
            )
            #
            self._updateNameLabel()
            #
            bscObjects.MessageWindow(
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
            dtbMethods.DtbUser.dbWriteUserJsonUnit(
                nameString, dict(jsonDatum), dbUnitType, dbUnitBranch
            )
            #
            self._updateNameLabel()
            #
            bscObjects.MessageWindow(
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
            self.mtd_app_node.setNodeSelect(self.mtd_app_node._toAppExistStringList(lis))
        else:
            self.mtd_app_node.setSelectClear()
    #
    def _kit__unit__set_build_(self):
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
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        layout.addWidget(leftExpandWidget)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self._kit__unit__set_left_build_(leftScrollArea)
        #
        rightScrollBox = qtCore.QScrollArea_()
        layout.addWidget(rightScrollBox)
        self.setupRightWidget(rightScrollBox)


#
class IfScLightLinkLoadUnit(kitQtWgtAbs.IfToolUnitBasic):
    mtd_app_node = _maMethod.MaLightNodeMethod
    mtd_app_prd_unit = _maProductMethod.MaProductUnitMethod

    VAR_kit__qt_wgt__unit__uiname = 'Scene Light Link Load'
    VAR_kit__qt_wgt__unit__icon = 'window/geometryPanel'
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
        'load': [0, 6, 0, 1, 4, 'Load Light Link(s)', 'svg_basic/load']
    }

    def __init__(self, *args, **kwargs):
        super(IfScLightLinkLoadUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._overrideVar()
        #
        self._kit__unit__set_build_()
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
    def _kit__unit__set_left_build_(self, layout):
        toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Information')
        self.setupInfoToolBox(toolBox)
        #
        toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Load')
        self.setupModifyToolBox(toolBox)
    #
    def setupRightWidget(self, layout):
        self.setupTreeViewBox(layout)
    #
    def setupInfoToolBox(self, toolBox):
        self._sectorChart = guiQtWidgets.QtSectorchart()
        toolBox.addWidget(self._sectorChart)
    #
    def setupModifyToolBox(self, toolBox):
        toolBox.setUiData(self.ToolLayoutDic_ScLightLinkUpload)
        #
        self._ignorePathButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('ignorePath', self._ignorePathButton)
        self._ignorePathButton.setChecked(True)
        self._ignorePathButton.setTooltip(
            u'''Ignore Path'''
        )
        self._ignorePathButton.checked.connect(self._initInfo)
        self._ignorePathButton.checked.connect(self._initView)
        #
        self._ignoreNamespaceButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('ignoreNamespace', self._ignoreNamespaceButton)
        self._ignoreNamespaceButton.setChecked(True)
        self._ignoreNamespaceButton.setTooltip(
            u'''Ignore Namespace'''
        )
        self._ignoreNamespaceButton.checked.connect(self._initInfo)
        self._ignoreNamespaceButton.checked.connect(self._initView)
        #
        self._lightLinkNameLabel = guiQtWidgets.QtValueLine()
        toolBox.addInfo('lightLinkName', self._lightLinkNameLabel)
        self._lightLinkNameLabel.setChooseEnable(True)
        self._lightLinkNameLabel.chooseChanged.connect(self._updateBranchLabel)
        #
        self._branchNameLabel = guiQtWidgets.QtValueLine()
        toolBox.addInfo('branchName', self._branchNameLabel)
        self._branchNameLabel.setChooseEnable(True)
        self._branchNameLabel.chooseChanged.connect(self._updateVersionLabel)
        #
        self._versionNameLabel = guiQtWidgets.QtValueLine()
        toolBox.addInfo('versionName', self._versionNameLabel)
        self._versionNameLabel.setChooseEnable(True)
        self._versionNameLabel.chooseChanged.connect(self._initInfo)
        self._versionNameLabel.chooseChanged.connect(self._initView)
        #
        self._loadButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('load', self._loadButton)
        self._loadButton.clicked.connect(self._loadLightLinkCmd)
        #
        toolBox.addSeparators()
    #
    def setupTreeViewBox(self, layout):
        self._treeView = guiQtWidgets.QtTreeview()
        layout.addWidget(self._treeView)
        self._treeView.setSelectEnable(True)
        self._treeView.setColorEnable(True)
        #
        self._treeView.selectedChanged.connect(self.setAppObjectSelect)
        self._treeView.setKeywordFilterWidgetConnect(self.filterEnterLabel())
    #
    def _updateNameLabel(self):
        entryLabel = self._lightLinkNameLabel
        dbUnitType = dtbMethods.DtbUser.LxDb_Unit_Type_LightLink
        #
        datumLis = dtbMethods.DtbUser.dbGetUserJsonUnitNameLis(dbUnitType)
        if datumLis:
            entryLabel.setDatumLis(datumLis)
    #
    def _updateBranchLabel(self):
        entryLabel = self._branchNameLabel
        #
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = dtbMethods.DtbUser.LxDb_Unit_Type_LightLink
        #
        branchLis = dtbMethods.DtbUser.dbGetUserServerJsonUnitBranchLis(nameString, dbUnitType)
        if branchLis:
            entryLabel.setDatumLis(branchLis)
    #
    def _updateVersionLabel(self):
        entryLabel = self._versionNameLabel
        #
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = dtbMethods.DtbUser.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        #
        versionUiDic, currentIndex = dtbMethods.DtbUser.dbGetUserServerJsonUnitIncludeVersionUiDic(
            nameString, dbUnitType, dbUnitBranch
        )
        if versionUiDic:
            entryLabel.setExtendDatumDic(versionUiDic)
    #
    def _updateServerDatum(self):
        nameString = self._lightLinkNameLabel.datum()
        dbUnitType = dtbMethods.DtbUser.LxDb_Unit_Type_LightLink
        dbUnitBranch = self._branchNameLabel.datum()
        #
        self._serverLightLinkDic = dtbMethods.DtbUser.dbReadUserJsonUnit(
            nameString, dbUnitType, dbUnitBranch
        )
    #
    def _initInfo(self):
        self._updateServerDatum()
        #
        isIgnorePath, isIgnoreNamespace = self._ignorePathButton.isChecked(), self._ignoreNamespaceButton.isChecked()
        chartDatum = self.mtd_app_node.getLightLinkLoadConstantDatumLis(
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
            nodeName = self.mtd_app_node._toNodeNameBySearchDatum(pathDatum, namespaceDatum)
            localNodeLis = self.mtd_app_node.getNodeLisBySearchDatum(
                nodeType, pathDatum, namespaceDatum,
                ignorePath=isIgnorePath, ignoreNamespace=isIgnoreNamespace
            )
            if localNodeLis:
                for seq, nodePath in enumerate(localNodeLis):
                    localDefaultSet = nodePath in defaultSetLis
                    treeItem = guiQtWidgets.QtTreeItem()
                    treeView.addItem(treeItem)
                    treeItem.setNamespaceText(self.mtd_app_node._toNamespaceByNodeName(nodeName))
                    treeItem.setNameString(self.mtd_app_node._toNameByNodeName(nodeName))
                    treeItem.setIcon(bscMethods.IconKeyword.mayaSvg(nodeType))
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
                treeItem = guiQtWidgets.QtTreeItem()
                treeView.addItem(treeItem)
                treeItem.setNamespaceText(self.mtd_app_node._toNamespaceByNodeName(nodeName))
                treeItem.setNameString(self.mtd_app_node._toNameByNodeName(nodeName))
                treeItem.setIcon(bscMethods.IconKeyword.mayaSvg(nodeType))
                treeItem._setQtPressStatus(qtCore.OffStatus)
                #
                lis.append(treeItem)
            #
            return lis
        #
        def setObjectBranch(parentItem, searchDatum, mainAttrName, lightNodePath, localLightLinkObjectLis):
            nodeType, pathDatum, namespaceDatum = eval(searchDatum)
            #
            nodeName = self.mtd_app_node._toNodeNameBySearchDatum(pathDatum, namespaceDatum)

            localNodeLis = self.mtd_app_node.getNodeLisBySearchDatum(
                nodeType, pathDatum, namespaceDatum,
                ignorePath=isIgnorePath, ignoreNamespace=isIgnoreNamespace
            )
            if localNodeLis:
                for seq, nodePath in enumerate(localNodeLis):
                    treeItem = guiQtWidgets.QtTreeItem()
                    parentItem.addChild(treeItem)
                    treeItem.setNamespaceText(self.mtd_app_node._toNamespaceByNodeName(nodeName))
                    treeItem.setNameString(self.mtd_app_node._toNameByNodeName(nodeName))
                    treeItem.setIcon(bscMethods.IconKeyword.mayaSvg(nodeType))
                    subIconKeyword = 'svg_basic/unlink' if mainAttrName.lower().endswith('ignore') else 'svg_basic/link'
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
                treeItem = guiQtWidgets.QtTreeItem()
                parentItem.addChild(treeItem)
                treeItem.setNamespaceText(self.mtd_app_node._toNamespaceByNodeName(nodeName))
                treeItem.setNameString(self.mtd_app_node._toNameByNodeName(nodeName))
                treeItem.setIcon(bscMethods.IconKeyword.mayaSvg(nodeType))
                subIconKeyword = 'svg_basic/unlink' if mainAttrName.lower().endswith('ignore') else 'svg_basic/link'
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
                progressBar = bscObjects.ProgressWindow(explain, maxValue)
                #
                defaultSetLis = self.mtd_app_node.getLightDefaultSetLis()
                for k, v in dataDic.items():
                    progressBar.update()
                    #
                    serverDefaultSet = v[self.mtd_app_node.MaNodeName_DefaultLightSet]
                    #
                    lightItemLis = setLightBranch(k, serverDefaultSet, defaultSetLis)
                    for lightItem in lightItemLis:
                        for i in searchDatumLis:
                            mainAttrName = i[0]
                            if mainAttrName in v:
                                if hasattr(lightItem, 'path'):
                                    lightNodePath = lightItem.path
                                    localLightLinkObjectLis = self.mtd_app_node.getLightLinkObjectLis(
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
            self.mtd_app_node.MaAttrNameLis_LightLink,
            self.mtd_app_node.MaAttrNameLis_LightLink_Ignore,
            self.mtd_app_node.MaAttrNameLis_ShadowLink,
            self.mtd_app_node.MaAttrNameLis_ShadowLink_Ignore
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
            bscObjects.MessageWindow(
                'Load Light Default Set(s)',
                'Complete'
            )
        #
        lightLinkDatum = self._lightLinkDatumLis
        if lightLinkDatum:
            self.setLightLink(lightLinkDatum)
            #
            bscObjects.MessageWindow(
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
            self.mtd_app_node.setNodeSelect(self.mtd_app_node._toAppExistStringList(lis))
        else:
            self.setSelectClear()
    #
    def _kit__unit__set_build_(self):
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
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        layout.addWidget(leftExpandWidget)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self._kit__unit__set_left_build_(leftScrollArea)
        #
        rightScrollBox = qtCore.QScrollArea_()
        layout.addWidget(rightScrollBox)
        self.setupRightWidget(rightScrollBox)
