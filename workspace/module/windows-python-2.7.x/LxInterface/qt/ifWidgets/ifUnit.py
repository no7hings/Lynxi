# coding:utf-8
from LxBasic import bscConfigure, bscCore, bscObjects, bscMethods

from LxScheme import shmOutput

from LxPreset import prsVariants, prsMethods

from LxCore import lxConfigure
#
from LxCore.preset.prod import assetPr, sceneryPr, scenePr
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore, qtCommands
#
from LxInterface.qt.qtIfBasic import _qtIfAbcWidget
#
from LxInterface.qt._qtIfModels import ifUnitModel
#
from LxDatabase import dbGet
#
serverBasicPath = shmOutput.Root().basic.server
#
none = ''


class IfAstModelRadarUnit(qtCore.QWidget):
    evaluateItems = [
        'worldArea',
        'shell',
        'vertex',
        'edge',
        'face',
        'triangle'
    ]

    def __init__(self):
        super(IfAstModelRadarUnit, self).__init__()
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setEvaluateData(self, mainData, subData=none):
        evaluateData = []
        #
        serverDatumDic = {}
        if subData:
            serverDatumDic = subData
        #
        if mainData:
            for i in self.evaluateItems:
                if i in mainData:
                    explain = i
                    localValue = mainData[i]
                    serverValue = 0
                    if i in serverDatumDic:
                        serverValue = serverDatumDic[i]
                    evaluateData.append(
                        (explain, serverValue, localValue)
                    )
        #
        if not mainData:
            self.setDef()
        #
        if evaluateData:
            self._astModelRadarChart.setChartDatum(evaluateData)
    #
    def setUiSize(self, width, height):
        self._astModelRadarChart.setUiSize(width, height)
    #
    def setBackground(self, picture=none):
        self._astModelRadarChart.setImage(picture)
    #
    def setDef(self):
        defValue = [6, 1, 8, 12, 6, 12]
        evaluateData = [(i, defValue[seq], defValue[seq]) for seq, i in enumerate(self.evaluateItems)]
        #
        self._astModelRadarChart.setChartDatum(evaluateData)
    #
    def setupUnit(self):
        layout = qtCore.QVBoxLayout_(self)
        # Radar
        self._astModelRadarChart = qtWidgets.QtRadarchart()
        layout.addWidget(self._astModelRadarChart)


class IfScIndexManagerUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    W = 120

    ConfigUiDic = {
        'startFrame': [W, 0, 0, 1, 1, 'Start Frame'],
        'endFrame': [W, 1, 0, 1, 1, 'End Frame']
    }

    def __init__(self):
        super(IfScIndexManagerUnit, self).__init__()
        self._initIfAbcUnit()
        #
        self.initUnit()
        self.setupUnit()
    #
    def refreshMethod(self):
        if self._args is not None:
            self.setListRecord()
            self.setListAvailableUnit()
    #
    def setArgs(self, keyword, args):
        self._args = args
    #
    def setupLeftWidget(self, layout):
        groupBox = qtWidgets.QtToolboxGroup()
        layout.addWidget(groupBox)
        groupBox.setTitle('Record')
        groupBox.setExpanded(True)
        #
        self._recordTreeView = qtWidgets.QtTreeview()
        groupBox.addWidget(self._recordTreeView)
        self._recordTreeView.setCheckEnable(True)
        self._recordTreeView.setColorEnable(True)
        self._recordTreeView.currentChanged.connect(self.setListAssignUnit)
        self._recordTreeView.currentChanged.connect(self.setConfigRefresh)
    #
    def setupCentralWidget(self, layout):
        groupBox = qtWidgets.QtToolboxGroup()
        layout.addWidget(groupBox)
        groupBox.setTitle('Assign Unit(s)')
        groupBox.setExpanded(True)
        #
        self._composeTreeView = qtWidgets.QtTreeview()
        groupBox.addWidget(self._composeTreeView)
        self._composeTreeView.setFilterConnect(self.filterEnterLabel())
        #
        toolBox = qtWidgets.QtToolbox()
        groupBox.addWidget(toolBox)
        toolBox.setTitle('Config(s)')
        self.setupConfigBox(toolBox)
    #
    def setupConfigBox(self, toolBox):
        toolBox.setUiData(self.ConfigUiDic)
        #
        self._startFrameLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('startFrame', self._startFrameLabel)
        self._startFrameLabel.setEnterEnable(True)
        self._startFrameLabel.setIntValidator()
        #
        self._endFrameLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('endFrame', self._endFrameLabel)
        self._endFrameLabel.setEnterEnable(True)
        self._endFrameLabel.setIntValidator()
    #
    def setupRightBox(self, layout):
        groupBox = qtWidgets.QtToolboxGroup()
        layout.addWidget(groupBox)
        groupBox.setTitle('Available Unit(s)')
        groupBox.setExpanded(True)
        #
        self._rightTreeView = qtWidgets.QtTreeview()
        groupBox.addWidget(self._rightTreeView)
    #
    def setListRecord(self):
        def setBranch(key, value):
            def setAction():
                def setActiveCmd():
                    pass
                #
                actionDatumLis = [
                    ('Basic', ),
                    ('Set Active', ('svg_basic@svg#file', 'action#upload'), False, setActiveCmd)
                ]
                #
                treeItem.setActionData(actionDatumLis)
            #
            timeTag = key
            osJsonFile = value
            #
            
            user = bscMethods.OsJson.getValue(osJsonFile, lxConfigure.DEF_key_info_username)
            personnel = prsMethods.Personnel.userChnname(user)
            #
            treeItem = qtWidgets.QtTreeviewItem()
            activeItem.addChild(treeItem)
            treeItem.setNameText(u'{} @ {}'.format(bscMethods.OsTimetag.toChnPrettify(timeTag), personnel))
            treeItem.setIcon('svg_basic@svg#history')
            #
            treeItem.timeTag = timeTag
            #
            setAction()
            #
            treeItem.startFrame = bscMethods.OsJson.getValue(osJsonFile, lxConfigure.Lynxi_Key_Info_StartFrame)
            treeItem.endFrame = bscMethods.OsJson.getValue(osJsonFile, lxConfigure.Lynxi_Key_Info_EndFrame)
            #
            curIndexLis = bscMethods.OsJson.getValue(
                osJsonFile,
                prsMethods.Asset.moduleName()
            )
            if curIndexLis == activeIndexLis:
                treeItem.setFilterColor((63, 127, 255, 255))
            treeItem.assetIndexLis = curIndexLis
            treeItem.sceneryIndexLis = bscMethods.OsJson.getValue(
                serverSceneIndexFile,
                prsMethods.Scenery.moduleName()
            )
        #
        if self._args is not None:
            (
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant
            ) = self._args
            #
            treeView = self._recordTreeView
            #
            serverSceneIndexFile = scenePr.scUnitIndexFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName, sceneCategory, sceneName, sceneVariant
            )[1]
            #
            backupSceneIndexFile = scenePr.scUnitIndexFile(
                lxConfigure.LynxiRootIndex_Backup,
                projectName, sceneCategory, sceneName, sceneVariant
            )[1]
            #
            activeItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(activeItem)
            activeItem.setNameText('Scene Index')
            activeItem.setIcon('svg_basic@svg#branch_main')
            #
            activeItem.isActive = True
            #
            activeItem.startFrame = bscMethods.OsJson.getValue(serverSceneIndexFile, lxConfigure.Lynxi_Key_Info_StartFrame)
            activeItem.endFrame = bscMethods.OsJson.getValue(serverSceneIndexFile, lxConfigure.Lynxi_Key_Info_EndFrame)
            #
            activeIndexLis = bscMethods.OsJson.getValue(
                serverSceneIndexFile, prsMethods.Asset.moduleName()
            )
            activeItem.assetIndexLis = activeIndexLis
            activeItem.sceneryIndexLis = bscMethods.OsJson.getValue(
                serverSceneIndexFile,
                prsMethods.Scenery.moduleName()
            )
            #
            indexRecordDic = bscMethods.OsFile.backupNameDict(backupSceneIndexFile)
            if indexRecordDic:
                progressExplain = '''List Record'''
                maxValue = len(indexRecordDic)
                progressBar = bscObjects.If_Progress(progressExplain, maxValue)
                for k, v in indexRecordDic.items():
                    progressBar.update()
                    setBranch(k, v)
            #
            self._activeItem = activeItem
            self._serverFile = serverSceneIndexFile
            self._backupFile = backupSceneIndexFile
            #
            if self._activeItem is not None:
                treeView.setCurrentIndex(treeView.itemIndex(self._activeItem))
                #
                self.setListAssignUnit()
                self.setConfigRefresh()
    #
    def _addClassItem(self, treeView):
        def setModuleBranch(moduleKey, datumText):
            treeItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(treeItem)
            #
            enViewName, chViewName = datumText
            treeItem.setNameText(u'{} ( {} )'.format(chViewName, enViewName))
            treeItem.setIcon('svg_basic@svg#branch_main')
            treeItem.setFilterColor((71, 71, 71, 255))
            #
            treeItem.setPressable(False)
            #
            return treeItem
        #
        def setClassBranch(classKey, datumText, parentItem):
            treeItem = qtWidgets.QtTreeviewItem()
            parentItem.addChild(treeItem)
            #
            enViewName, chViewName = datumText
            treeItem.setNameText(u'{} ( {} )'.format(chViewName, enViewName))
            treeItem.setIcon('svg_basic@svg#tag')
            treeItem.setFilterColor((71, 71, 71, 255))
            #
            treeItem.setPressable(False)
            #
            return treeItem
        #
        classItemDic = {}

        for productModuleString in prsMethods.Product.moduleNames():
            v = prsMethods.Product.moduleShowname(productModuleString)
            moduleItem = setModuleBranch(productModuleString, v)
            #
            classKeyLis = prsMethods.Product.moduleCategoryNames(productModuleString)
            classUiDic = prsMethods.Product.moduleClassShownames(productModuleString)
            #
            for unitClass in classKeyLis:
                iv = classUiDic[unitClass]
                classItem = setClassBranch(unitClass, iv, moduleItem)
                classItemDic[unitClass] = classItem
        #
        return classItemDic
    #
    def setListAssignUnit(self):
        def setAssetModuleBranch(indexes):
            def setAssetUnitSubBranch(seq, value):
                def setUnitAction():
                    def setActionBranch(variant):
                        def isActiveVariant():
                            return variant == treeItem.assetVariant
                        #
                        def setVariantCmd():
                            activeVariant = treeItem.assetVariant
                            if not variant == activeVariant:
                                newViewExplain = assetPr.getAssetViewInfo(assetIndex, assetCategory, '{} - {}'.format(assetName, variant))
                                treeItem.setNameText(newViewExplain)
                                #
                                self._assetDatumLis[seq][4] = variant
                                #
                                treeItem.setFilterColor([(71, 71, 71, 255), (255, 255, 64, 255)][variant != assetVariant])
                                #
                                treeItem.assetVariant = variant
                        #
                        actionDatumLis.append(
                            ('{}'.format(variant), 'checkBox', isActiveVariant, setVariantCmd)
                        )
                    assetVariantLis = assetPr.getAssetVariantLis(assetIndex)
                    #
                    actionDatumLis, actionTitle = (
                        [
                            ('Change Variant', ),
                        ],
                        assetPr.getAssetViewInfo(assetIndex, assetCategory)
                    )
                    for j in assetVariantLis:
                        setActionBranch(j)
                    #
                    treeItem.setActionData(actionDatumLis, actionTitle)
                #
                assetIndex, assetCategory, assetName, number, assetVariant = value
                self._assetIndexLis.append(assetIndex)
                #
                treeItem = qtWidgets.QtTreeviewItem()
                classItem = classItemDic[assetCategory]
                classItem.addChild(treeItem)
                #
                viewName = assetPr.getAssetViewName(assetIndex)
                viewExplain = u'{} ( {} - {} - {} )'.format(viewName, assetName, number, assetVariant)
                treeItem.setNameText(viewExplain)
                treeItem.setIcon('svg_basic@svg#package_object')
                if not value in repeatCheckLis:
                    treeItem.setFilterColor((71, 71, 71, 255))
                    repeatCheckLis.append(value)
                else:
                    treeItem.setFilterColor((255, 0, 63, 255))
                #
                treeItem.assetVariant = assetVariant
                #
                setUnitAction()
            #
            repeatCheckLis = []
            if indexes:
                for s, v in enumerate(indexes):
                    setAssetUnitSubBranch(s, v)
                    self._assetDatumLis.append(list(v))
        #
        def setSceneryModuleBranch(indexes):
            def setUnitSubBranch(seq, value):
                sceneryIndex, sceneryCategory, sceneryName, sceneryVariant, sceneryStage = value
                if prsMethods.Product.isValidSceneryCategoryName(sceneryCategory):
                    treeItem = qtWidgets.QtTreeviewItem()
                    classItem = classItemDic[sceneryCategory]
                    classItem.addChild(treeItem)
                    #
                    viewName = sceneryPr.getSceneryViewName(sceneryIndex)
                    viewExplain = u'{} ( {} - {} )'.format(viewName, sceneryName, sceneryVariant)
                    treeItem.setNameText(viewExplain)
                    treeItem.setIcon('svg_basic@svg#package_object')
                    treeItem.setFilterColor((71, 71, 71, 255))
                    #
                    treeItem.sceneryVariant = sceneryVariant
                else:
                    treeItem = qtWidgets.QtTreeviewItem()
                    classItem = classItemDic[prsMethods.Asset.assemblyCategoryName()]
                    classItem.addChild(treeItem)
                    #
                    viewName = assetPr.getAssetViewName(sceneryIndex)
                    viewExplain = u'{} ( {} - {} )'.format(viewName, sceneryName, sceneryVariant)
                    treeItem.setNameText(viewExplain)
                    treeItem.setIcon('svg_basic@svg#package_object')
                    treeItem.setFilterColor((71, 71, 71, 255))
                    #
                    treeItem.assetVariant = sceneryVariant
            #
            if indexes:
                for s, i in enumerate(indexes):
                    setUnitSubBranch(s, i)
                    self._sceneryDatumLis.append(list(i))
        #
        self._assetDatumLis = []
        self._sceneryDatumLis = []
        #
        treeView = self._composeTreeView
        #
        indexItem = self._recordTreeView.currentItem()
        #
        treeView.cleanItems()
        #
        if indexItem:
            classItemDic = self._addClassItem(treeView)
            #
            assetIndexLis = indexItem.assetIndexLis
            setAssetModuleBranch(assetIndexLis)
            #
            sceneryIndexLis = indexItem.sceneryIndexLis
            setSceneryModuleBranch(sceneryIndexLis)
            #
            for ik, iv in classItemDic.items():
                if iv.hasChildren():
                    iv.setPressable(True)
                    iv.setExpanded(True)
                    parentItems = iv.parentItems()
                    [j.setPressable(True) for j in parentItems]
                    [j.setExpanded(True) for j in parentItems]
        #
        treeView.setRefresh()
    #
    def setConfigRefresh(self):
        indexItem = self._recordTreeView.currentItem()
        if indexItem:
            startFrame, endFrame = indexItem.startFrame, indexItem.endFrame
            #
            if hasattr(indexItem, 'isActive'):
                self._startFrameLabel.setDefaultDatum(startFrame)
                self._endFrameLabel.setDefaultDatum(endFrame)
            #
            self._startFrameLabel.setDatum(startFrame)
            self._endFrameLabel.setDatum(endFrame)
            #
            self._startFrame, self._endFrame = startFrame, endFrame
    #
    def setListAvailableUnit(self):
        def setAssetModuleBranch():
            def setAssetUnitSubBranch(seq, key, value):
                assetIndex = key
                assetCategory = assetPr.getAssetClass(assetIndex)
                assetName, assetViewName = value
                assetVariant = prsVariants.Util.astDefaultVariant
                #
                treeItem = qtWidgets.QtTreeviewItem()
                classItem = classItemDic[assetCategory]
                classItem.addChild(treeItem)
                #
                viewExplain = u'{} ( {} - {} )'.format(assetViewName, assetName, assetVariant)
                treeItem.setNameText(viewExplain)
                treeItem.setIcon('svg_basic@svg#package_object')
                #
                if assetIndex in self._assetIndexLis:
                    treeItem.setFilterColor((63, 255, 127, 255))
                else:
                    treeItem.setFilterColor((71, 71, 71, 255))
            #
            def setAssemblyUnitSubBranch(seq, key, value):
                assetIndex = key
                assetCategory = assetPr.getAssetClass(assetIndex)
                assetName, assetViewName = value
                assetVariant = prsVariants.Util.astDefaultVariant
                #
                treeItem = qtWidgets.QtTreeviewItem()
                classItem = classItemDic[prsMethods.Asset.assemblyCategoryName()]
                classItem.addChild(treeItem)
                #
                viewExplain = u'{} ( {} - {} )'.format(assetViewName, assetName, assetVariant)
                treeItem.setNameText(viewExplain)
                treeItem.setIcon('svg_basic@svg#package_object')
                #
                if assetIndex in self._assetIndexLis:
                    treeItem.setFilterColor((63, 255, 127, 255))
                else:
                    treeItem.setFilterColor((71, 71, 71, 255))
            # Rig
            setDic = assetPr.getUiAssetMultMsgDic(projectName, assetLinkFilter=lxConfigure.VAR_product_asset_link_rig)
            if setDic:
                for s, (k, v) in enumerate(setDic.items()):
                    setAssetUnitSubBranch(s, k, v)
            # Assembly
            setDic = assetPr.getUiAssetMultMsgDic(projectName, assetLinkFilter=lxConfigure.VAR_product_asset_link_assembly)
            if setDic:
                for s, (k, v) in enumerate(setDic.items()):
                    setAssemblyUnitSubBranch(s, k, v)
        #
        def setSceneryModuleBranch():
            def setSceneryUnitBranch(seq, key, value):
                sceneryIndex = key
                sceneryCategory = assetPr.getAssetClass(sceneryIndex)
                sceneryName, sceneryViewName = value
                sceneryVariant = prsVariants.Util.astDefaultVariant
            #
            setDic = sceneryPr.getUiSceneryMultMsgs(projectName, sceneryClassFilters=lxConfigure.VAR_product_scenery_link_scenery)
            if setDic:
                for s, (k, v) in enumerate(setDic.items()):
                    setSceneryUnitBranch(s, k, v)
        #
        treeView = self._rightTreeView
        #
        projectName = prsMethods.Project.mayaActiveName()
        #
        classItemDic = self._addClassItem(treeView)
        #
        setAssetModuleBranch()
        setSceneryModuleBranch()
        #
        if classItemDic:
            for ik, iv in classItemDic.items():
                if iv.hasChildren():
                    iv.setPressable(True)
                    parentItems = iv.parentItems()
                    [j.setPressable(True) for j in parentItems]
        #
        treeView.setRefresh()
    #
    def confirmCmd(self):
        if self._assetDatumLis:
            if bscMethods.OsFile.isExist(self._serverFile):
                serverAssetDatum = bscMethods.OsJson.getValue(
                    self._serverFile,
                    prsMethods.Asset.moduleName()
                )
                if not self._assetDatumLis == serverAssetDatum:
                    bscMethods.OsJson.setValue(
                        self._serverFile,
                        {
                            lxConfigure.DEF_key_info_time: bscMethods.OsTimestamp.active(),
                            lxConfigure.DEF_key_info_username: bscMethods.OsSystem.username(),
                            #
                            prsMethods.Asset.moduleName(): self._assetDatumLis
                        }
                    )
                    #
                    bscMethods.OsFile.backupTo(
                        self._serverFile, self._backupFile,
                        bscMethods.OsTimetag.active()
                    )
                    #
                    bscObjects.If_Message(
                        u'提示',
                        u'修改镜头配置成功！！！'
                    )
        #
        startFrame, endFrame = self._startFrameLabel.datum(), self._endFrameLabel.datum()
        if startFrame is not None and endFrame is not None:
            if bscMethods.OsFile.isExist(self._serverFile):
                serverStartFrame, serverEndFrame = (
                    bscMethods.OsJson.getValue(self._serverFile, lxConfigure.Lynxi_Key_Info_StartFrame),
                    bscMethods.OsJson.getValue(self._serverFile, lxConfigure.Lynxi_Key_Info_EndFrame)
                )
                if not startFrame == serverStartFrame or not endFrame == serverEndFrame:
                    bscMethods.OsJson.setValue(
                        self._serverFile,
                        {
                            lxConfigure.DEF_key_info_time: bscMethods.OsTimestamp.active(),
                            lxConfigure.DEF_key_info_username: bscMethods.OsSystem.username(),
                            #
                            lxConfigure.Lynxi_Key_Info_StartFrame: startFrame,
                            lxConfigure.Lynxi_Key_Info_EndFrame: endFrame
                        }
                    )
                    #
                    bscMethods.OsFile.backupTo(self._serverFile, self._backupFile, bscMethods.OsTimetag.active())
                    #
                    bscObjects.If_Message(
                        u'提示',
                        u'修改镜头配置成功！！！'
                    )
    #
    def initUnit(self):
        self._args = None
        #
        self._activeItem = None
        #
        self._startFrame, self._endFrame = None, None
        #
        self._assetDatumLis = []
        self._sceneryDatumLis = []
        #
        self._assetIndexLis = []
        self._assemblyIndexLis = []
        self._sceneryIndexLis = []
        #
        self._serverFile = None
        self._backupFile = None
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        leftExpandWidget.setUiWidth(self.SideWidth)
        layout.addWidget(leftExpandWidget)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self.setupLeftWidget(leftScrollArea)
        #
        self.setupCentralWidget(layout)
        #
        rightExpandWidget = qtWidgets_.QtExpandWidget()
        rightExpandWidget.setUiWidth(self.SideWidth*2)
        rightExpandWidget.setExpandDir(qtCore.LeftDir)
        layout.addWidget(rightExpandWidget)
        rightExpandWidget.setExpanded(False)
        #
        rightScrollBox = qtCore.QScrollArea_()
        rightExpandWidget.addWidget(rightScrollBox)
        self.setupRightBox(rightScrollBox)


class IfScCacheManagerUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    def __init__(self):
        super(IfScCacheManagerUnit, self).__init__()
        self._initIfAbcUnit()
        #
        self.initUnit()
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setArgs(self, string, args):
        self._cacheType = string
        self._args = args
    #
    def setupTopToolBar(self, layout):
        self._fileStringLabel = qtWidgets.QtEnterlabel()
        self._fileStringLabel.setEnterEnable(True)
        self._fileStringLabel.setEnterable(True)
        #
        layout.addWidget(self._fileStringLabel)
    #
    def setupLeftToolUiBox(self, layout):
        def setModelCacheGeometryEvaluateCmd():
            if self._cacheType == lxConfigure.LynxiScAstModelCacheType:
                selectedItems = treeBox.selectedItems()
                if selectedItems:
                    treeItem = selectedItems[0]
                    sourceData = treeItem.sourceData
                    targetData = treeItem.targetData
                    self.meshEvaluateBox.setEvaluateData(sourceData, targetData)
        #
        def setViewFileStringCmd():
            selectedItems = treeBox.selectedItems()
            if selectedItems:
                treeItem = selectedItems[0]
                if hasattr(treeItem, 'cacheFile'):
                    cacheFile = treeItem.cacheFile
                    self._fileStringLabel.setDatum(cacheFile)
        #
        self.treeViewBox = qtWidgets_.QTreeWidget_()
        layout.addWidget(self.treeViewBox)
        #
        treeBox = self.treeViewBox
        treeBox.setSingleSelection()
        treeBox.setColumns(
            ['Time', 'Stage', 'State', 'Personnel', 'Frame Range', 'Order'],
            [4, 2, 2, 2, 2, 1],
            630
        )
        treeBox.setUiStyle('C')
        #
        treeBox.itemSelectionChanged.connect(setModelCacheGeometryEvaluateCmd)
        treeBox.itemSelectionChanged.connect(setViewFileStringCmd)
    #
    def confirmCmd(self):
        treeBox = self.treeViewBox
        #
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            if selectedItems:
                treeItem = selectedItems[0]
                indexFile = treeItem.indexFile
                cacheFile = treeItem.cacheFile
                if bscMethods.OsFile.isExist(cacheFile):
                    # Index
                    cacheIndex = {
                        lxConfigure.LynxiCacheInfoKey: cacheFile
                    }
                    #
                    bscMethods.OsJson.setValue(
                        indexFile,
                        cacheIndex
                    )
                    #
                    bscObjects.If_Message(
                        'Changer Active Cache is', 'Complete'
                    )
                    #
                    if self._connectObject:
                        self._connectObject.uiQuit()
                else:
                    bscObjects.If_Message(
                        'Cache File is', 'Non - Exists'
                    )
    #
    def setListCache(self):
        def setSubActionData(treeItem, itemWidget, timeTag, indexFile, cacheFile):
            def setCacheImportCmd():
                if bscMethods.MayaApp.isActive():
                    from LxMaya.command import maUtils, maFile
                    #
                    groupName = 'import_{}'.format(timeTag)
                    if not maUtils.isAppExist(groupName):
                        maFile.setFileImportWithGroup(cacheFile, groupName)
            #
            def setCacheActiveCmd():
                cacheIndex = {
                    lxConfigure.LynxiCacheInfoKey: cacheFile
                }
                #
                bscMethods.OsJson.setValue(
                    indexFile,
                    cacheIndex
                )
                #
                bscObjects.If_Message(
                    'Changer Active Cache is', 'Complete'
                )
                #
                treeItem.setText(2, 'Active')
                treeItems = treeBox.treeItems()
                for i in treeItems:
                    if not i == treeItem:
                        i.setText(2, '')
            #
            actionDatumLis = [
                ('Basic',),
                ('Load Current Cache', 'svg_basic@svg#Import', True, setCacheImportCmd),
                ('Set Current Cache Active', 'svg_basic@svg#modify', True, setCacheActiveCmd)
            ]
            #
            itemWidget.setActionData(actionDatumLis)
        #
        def setScCameraCacheBranch(data):
            (
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant,
                subLabelString
            ) = data
            #
            cacheDic = scenePr.getScCameraCacheDic(
                projectName,
                sceneName, sceneVariant,
                subLabelString
            )
            #
            indexFile = scenePr.scCameraCacheIndexFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                sceneName, sceneVariant
            )[1]
            #
            activeTimeTag = scenePr.getScCameraCacheActiveTimeTag(
                projectName,
                sceneName, sceneVariant,
                subLabelString
            )
            #
            timeTags = []
            #
            cacheFileDic = {}
            for seq, (cacheSceneStage, cacheFiles) in enumerate(cacheDic.items()):
                for cacheFile in cacheFiles:
                    currentTimeTag = bscMethods.OsFile.findTimetag(cacheFile)
                    if not currentTimeTag == bscConfigure.MtdBasic.DEF_time_tag_default:
                        timeTags.append((currentTimeTag, cacheSceneStage))
                        cacheFileDic[(currentTimeTag, cacheSceneStage)] = cacheFile
            #
            if timeTags:
                timeTags.sort()
                for seq, (currentTimeTag, cacheSceneStage) in enumerate(timeTags):
                    cacheFile = cacheFileDic[(currentTimeTag, cacheSceneStage)]
                    #
                    isActive = currentTimeTag == activeTimeTag
                    #
                    cacheFileItem_ = qtWidgets_.QTreeWidgetItem_()
                    treeBox.addItem(cacheFileItem_)
                    #
                    cacheFileItem_.indexFile = indexFile
                    cacheFileItem_.cacheFile = cacheFile
                    #
                    cacheItemWidget = cacheFileItem_.setItemIconWidget(
                        0, 'svg_basic@svg#file',
                        bscMethods.OsTimetag.toChnPrettify(currentTimeTag)
                    )
                    #
                    cacheFileItem_.setItemIcon_(1, 'link#{}'.format(cacheSceneStage))
                    cacheFileItem_.setText(1, bscObjects.Str_Camelcase(cacheSceneStage).toPrettify())
                    if isActive:
                        cacheFileItem_.setSelected(True)
                        cacheFileItem_.setText(2, 'Active')
                    #
                    infoFile = bscMethods.OsFile.infoJsonName(cacheFile)
                    if bscMethods.OsFile.isExist(infoFile):
                        osUser = bscMethods.OsJson.getValue(infoFile, lxConfigure.DEF_key_info_username)
                        if osUser:
                            cacheFileItem_.setItemIcon_(3, 'svg_basic@svg#user')
                            cacheFileItem_.setText(3, prsMethods.Personnel.userChnname(osUser))
                        #
                        startFrame_ = bscMethods.OsJson.getValue(infoFile, lxConfigure.Lynxi_Key_Info_StartFrame)
                        endFrame_ = bscMethods.OsJson.getValue(infoFile, lxConfigure.Lynxi_Key_Info_EndFrame)
                        #
                        if startFrame_ is not None and endFrame_ is not None:
                            cacheFileItem_.setText(4, '{} - {}'.format(startFrame_, endFrame_))
                            cacheFileItem_.setItemIcon_(4, 'svg_basic@svg#time')
                    #
                    cacheFileItem_.setText(5, str(seq + 1))
                    setSubActionData(cacheFileItem_, cacheItemWidget, currentTimeTag, indexFile, cacheFile)
        #
        def setScAstModelCacheBranch(data):
            def setSubBranch():
                cacheFile_ = cacheFileDic[(currentTimeTag, cacheSceneStage)]
                #
                checkResult = dbGet.getScModelCacheMeshCheck(assetIndex, cacheFile_)
                #
                isActive = currentTimeTag == activeTimeTag
                #
                cacheFileItem_ = qtWidgets_.QTreeWidgetItem_()
                treeBox.addItem(cacheFileItem_)
                #
                cacheFileItem_.indexFile = indexFile
                cacheFileItem_.cacheFile = cacheFile_
                #
                cacheItemWidget = cacheFileItem_.setItemIconWidget(
                    0, 'svg_basic@svg#file',
                    bscMethods.OsTimetag.toChnPrettify(currentTimeTag),
                    checkResult
                )
                #
                cacheFileItem_.setItemIcon_(1, 'link#{}'.format(cacheSceneStage))
                cacheFileItem_.setText(1, bscObjects.Str_Camelcase(cacheSceneStage).toPrettify())
                sourceData, targetData = dbGet.getScModelCacheMeshEvaluateData(assetIndex, cacheFile_)
                #
                cacheFileItem_.sourceData = sourceData
                cacheFileItem_.targetData = targetData
                if isActive:
                    cacheFileItem_.setSelected(True)
                    cacheFileItem_.setText(2, 'Active')
                #
                infoFile = bscMethods.OsFile.infoJsonName(cacheFile_)
                if bscMethods.OsFile.isExist(infoFile):
                    osUser = bscMethods.OsJson.getValue(infoFile, lxConfigure.DEF_key_info_username)
                    if osUser:
                        cacheFileItem_.setItemIcon_(3, 'svg_basic@svg#user')
                        cacheFileItem_.setText(3, prsMethods.Personnel.userChnname(osUser))
                    #
                    startFrame_ = bscMethods.OsJson.getValue(infoFile, lxConfigure.Lynxi_Key_Info_StartFrame)
                    endFrame_ = bscMethods.OsJson.getValue(infoFile, lxConfigure.Lynxi_Key_Info_EndFrame)
                    #
                    if startFrame_ is not None and endFrame_ is not None:
                        cacheFileItem_.setText(4, '{} - {}'.format(startFrame_, endFrame_))
                        cacheFileItem_.setItemIcon_(4, 'svg_basic@svg#time')
                #
                cacheFileItem_.setText(5, str(seq + 1))
                setSubActionData(cacheFileItem_, cacheItemWidget, currentTimeTag, indexFile, cacheFile_)
            #
            self.rightScrollBox.show()
            (
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant,
                startFrame, endFrame,
                assetIndex, assetCategory, assetName, number, assetVariant
            ) = data
            #
            cacheDic = scenePr.getScAstModelCacheDic(
                projectName,
                sceneName, sceneVariant,
                assetName, number
            )
            #
            preview = dbGet.getDbAstPreviewFile(assetIndex, assetVariant)
            #
            self.meshEvaluateBox.setBackground(preview)
            #
            indexFile = scenePr.scAstCacheIndexFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                sceneName, sceneVariant, assetName, number
            )[1]
            #
            activeTimeTag = scenePr.getScAstModelCacheActiveTimeTag(
                projectName,
                sceneName, sceneVariant,
                assetName, number
            )
            timeTags = []
            #
            cacheFileDic = {}
            for seq, (cacheSceneStage, cacheFiles) in enumerate(cacheDic.items()):
                for cacheFile in cacheFiles:
                    currentTimeTag = bscMethods.OsFile.findTimetag(cacheFile)
                    if not currentTimeTag == bscConfigure.MtdBasic.DEF_time_tag_default:
                        timeTags.append((currentTimeTag, cacheSceneStage))
                        cacheFileDic[(currentTimeTag, cacheSceneStage)] = cacheFile
            #
            if timeTags:
                timeTags.sort()
                for seq, (currentTimeTag, cacheSceneStage) in enumerate(timeTags):
                    setSubBranch()
        #
        def setMain():
            cacheType = self._cacheType
            args = self._args
            #
            treeBox.clear()
            if cacheType is not None and args is not None:
                if cacheType == lxConfigure.LynxiScCameraCacheType:
                    setScCameraCacheBranch(args)
                elif cacheType == lxConfigure.LynxiScAstModelCacheType:
                    setScAstModelCacheBranch(args)
                #
                elif cacheType == lxConfigure.LynxiScAstCfxFurCacheType:
                    pass
                #
                elif cacheType == lxConfigure.LynxiScAstExtraCacheType:
                    pass
        #
        treeBox = self.treeViewBox
        setMain()
    #
    def initUnit(self):
        self._cacheType = None
        self._args = None
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        self.topToolBar().hide()
        #
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        #
        toolBar = qtWidgets_.xToolBar()
        layout.addWidget(toolBar)
        self.setupTopToolBar(toolBar)
        #
        centralWidget = qtCore.QWidget_()
        layout.addWidget(centralWidget)
        centralLayout = qtCore.QHBoxLayout_(centralWidget)
        centralLayout.setContentsMargins(0, 0, 0, 0)
        centralLayout.setSpacing(2)
        #
        self.leftScrollArea = qtCore.QScrollArea_()
        centralLayout.addWidget(self.leftScrollArea)
        self.setupLeftToolUiBox(self.leftScrollArea)
        #
        self.rightScrollBox = qtCore.QScrollArea_()
        self.rightScrollBox.hide()
        self.rightScrollBox.setUiSize(320, 320)
        centralLayout.addWidget(self.rightScrollBox)
        #
        self.meshEvaluateBox = IfAstModelRadarUnit()
        self.rightScrollBox.addWidget(self.meshEvaluateBox)
        self.meshEvaluateBox.setDef()


class IfProductUnitRegisterUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    def __init__(self):
        super(IfProductUnitRegisterUnit, self).__init__()
        self._initIfAbcUnit()
        #
        self.setupUnit()
    #
    def setConnectObject(self, classObject):
        self._connectObject = classObject
        #
        self._projectName = self.connectObject().activeName()
        #
        self._presetViewModel = ifUnitModel.IfProductPresetViewModel(
            self, self._presetView, self._productModuleString
        )
        #
        self._toolGroup.setTitle('{} Unit(s)'.format(bscMethods.StrCamelcase.toPrettify(self._productModuleString)))
        self._presetViewModel.setMainAction(self._toolGroup)
    #
    def refreshMethod(self):
        if self.connectObject():
            pass
    #
    def setProductModule(self, productModuleString):
        self._productModuleString = productModuleString
    #
    def setupCentralWidget(self, layout):
        self._toolGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(self._toolGroup)
        self._toolGroup.setExpanded(True)
        #
        self._presetView = qtWidgets.QtPresetview()
        self._toolGroup.addWidget(self._presetView)
        self._presetView.setFilterConnect(self.filterEnterLabel())
    #
    def setCentralRefresh(self):
        self._presetViewModel._initUnitItems()
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        layout = qtCore.QHBoxLayout_(widget)
        self.mainLayout().addWidget(widget)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(leftExpandWidget)
        leftExpandWidget.setUiWidth(self.SideWidth)
        leftExpandWidget.setExpanded(False)
        #
        self._leftScrollLayout = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(self._leftScrollLayout)
        #
        self._centralScrollLayout = qtCore.QScrollArea_()
        layout.addWidget(self._centralScrollLayout)
        self.setupCentralWidget(self._centralScrollLayout)


class IfProductUnitRecordUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    w = 80
    dicMain = {
        0: 'Date',
        lxConfigure.DEF_key_info_time: [w, 1, 0, 1, 4, ('Update', u'日期')],
        2: 'Information(s)',
        lxConfigure.DEF_key_info_username: [w, 3, 0, 1, 4, ('Artist', u'人员')],
        lxConfigure.DEF_key_info_hostname: [w, 4, 0, 1, 4, ('PC', u'计算机')],
        lxConfigure.DEF_key_info_host: [w, 5, 0, 1, 4, ('IP', u'IP地址')],
        lxConfigure.Lynxi_Key_Info_Stage: [w, 6, 0, 1, 4, ('Stage', u'阶段')],
        lxConfigure.DEF_key_info_note: [w, 7, 0, 1, 4, ('Note', u'备注')],
        8: 'Action(s)',
        'sourceFile': [0, 9, 0, 1, 2, None], 'loadSource': [0, 9, 2, 1, 2, 'Load Source File', 'svg_basic@svg#fileOpen'],
        'productFile': [0, 10, 0, 1, 2, None], 'loadProduct': [0, 10, 2, 1, 2, 'Load Product File', 'svg_basic@svg#fileOpen']
    }
    #
    keywords = [lxConfigure.DEF_key_info_username, lxConfigure.DEF_key_info_hostname, lxConfigure.DEF_key_info_host, lxConfigure.DEF_key_info_note]
    #
    def __init__(self, *args, **kwargs):
        super(IfProductUnitRecordUnit, self).__init__(*args, **kwargs)
        self._initIfAbcUnit()
        #
        self._sourceFileDic = {}
        self._productFileDic = {}
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setTitle(self, string):
        self._mainToolBox.setTitle(string, 1)
    #
    def setupMainToolUiBox(self, toolBox):
        inData = self.dicMain
        #
        self._timeChooseLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, lxConfigure.DEF_key_info_time, self._timeChooseLabel)
        self._timeChooseLabel.setChooseEnable(True)
        self._timeChooseLabel.setIconKeyword('svg_basic@svg#history')
        #
        self._timeChooseLabel.chooseChanged.connect(self.setInfoRefreshCmd)
        self._timeChooseLabel.chooseChanged.connect(self.setBtnState)
        #
        self._uiInfoItemDic = {}
        for k, v in inData.items():
            if k in self.keywords:
                if k == lxConfigure.DEF_key_info_note:
                    infoLabel = qtWidgets.QtEnterbox()
                    self._uiInfoItemDic[lxConfigure.DEF_key_info_note] = infoLabel
                    self._uiInfoItemDic[lxConfigure.Lynxi_Key_Info_Notes] = infoLabel
                else:
                    infoLabel = qtWidgets.QtEnterlabel()
                    self._uiInfoItemDic[k] = infoLabel
                #
                toolBox.setInfo(inData, k, infoLabel)
        #
        self._sourceFileLabel = qtWidgets.QtEnterlabel()
        toolBox.setButton(inData, 'sourceFile', self._sourceFileLabel)
        self._sourceFileLabel.setEnterEnable(True)
        #
        self._loadSourceButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'loadSource', self._loadSourceButton)
        self._loadSourceButton.setPressable(False)
        self._loadSourceButton.setTooltip('Load Source ( History ) File')
        self._loadSourceButton.clicked.connect(self.loadSourceFile)
        #
        self._productFileLabel = qtWidgets.QtEnterlabel()
        toolBox.setButton(inData, 'productFile', self._productFileLabel)
        self._productFileLabel.setEnterEnable(True)
        #
        self._loadProductButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'loadProduct', self._loadProductButton)
        self._loadProductButton.setPressable(False)
        self._loadProductButton.setTooltip('Load Integration ( History ) File')
        self._loadProductButton.clicked.connect(self.loadProductFile)
        #
        toolBox.setSeparators(inData)
    #
    def setInfoRefreshCmd(self):
        update = self.getUpdate()
        #
        sourceRecordDic = self._sourceFileDic
        uiDatumDic = self._uiInfoItemDic
        if update:
            sourceFile = sourceRecordDic[update]
            infoFile = bscMethods.OsFile.infoJsonName(sourceFile)
            infoDatumDic = bscMethods.OsJson.read(infoFile)
            if infoDatumDic:
                for k, v in uiDatumDic.items():
                    infoLabel = v
                    if k in infoDatumDic:
                        info = infoDatumDic[k]
                        if k == lxConfigure.DEF_key_info_username:
                            cnName = prsMethods.Personnel.userChnname(info)
                            if cnName:
                                viewInfo = u'{} ( {} )'.format(cnName, info)
                            else:
                                viewInfo = info
                            #
                            infoLabel.setDatum(viewInfo)
                        else:
                            infoLabel.setDatum(info)
            else:
                [v.setEnterClear() for k, v in uiDatumDic.items()]
        else:
            [v.setEnterClear() for k, v in uiDatumDic.items()]
    #
    def setBtnState(self):
        update = self.getUpdate()
        #
        sourceFileDic = self._sourceFileDic
        productFileDic = self._productFileDic
        #
        if update:
            sourceFile = none
            productFile = none
            if update in sourceFileDic:
                sourceFile = sourceFileDic[update]
                self._sourceFileLabel.setDatum(sourceFile)
            else:
                self._sourceFileLabel.setEnterClear()
            #
            if update in productFileDic:
                productFile = productFileDic[update]
                self._productFileLabel.setDatum(productFile)
            else:
                self._productFileLabel.setEnterClear()
            #
            booleanA = bscMethods.OsFile.isExist(sourceFile)
            self._loadSourceButton.setPressable(booleanA)
            booleanB = bscMethods.OsFile.isExist(productFile)
            self._loadProductButton.setPressable(booleanB)
        else:
            self._sourceFileLabel.setEnterClear()
            self._productFileLabel.setEnterClear()
            self._loadSourceButton.setPressable(False)
            self._loadProductButton.setPressable(False)
    #
    def setUpdateLabelConnect(self, method):
        self._timeChooseLabel.chooseChanged.connect(method)
    #
    def setRecordConnect(self, sourceKeyFile, productKeyFile=none):
        self._sourceFileDic = {}
        self._productFileDic = {}
        #
        if sourceKeyFile:
            sourceFileDic = bscMethods.OsFile.backupNameDict(sourceKeyFile)
            productRecordDic = bscMethods.OsFile.backupNameDict(productKeyFile)
            timeTagLis = []
            if sourceFileDic:
                for timeTag, sourceFile in sourceFileDic.items():
                    if not timeTag == bscConfigure.MtdBasic.DEF_time_tag_default:
                        showUpdate = bscMethods.OsTimetag.toChnPrettify(timeTag)
                        if timeTag in productRecordDic:
                            timeTagLis.append(showUpdate)
                            #
                            self._sourceFileDic[showUpdate] = sourceFile
                            #
                            productFile = productRecordDic[timeTag]
                            self._productFileDic[showUpdate] = productFile
                #
                self._timeChooseLabel.setDatumLis(timeTagLis)
                self._timeChooseLabel.setChoose(timeTagLis[-1])
            else:
                self._timeChooseLabel.setChooseClear()
        else:
            self._timeChooseLabel.setChooseClear()
    #
    def getUpdate(self):
        datum = self._timeChooseLabel.datum()
        if datum:
            return datum
    #
    def loadSourceFile(self):
        update = self.getUpdate()
        #
        sourceFileDic = self._sourceFileDic
        if update:
            if update in sourceFileDic:
                sourceFile = sourceFileDic[update]
                if bscMethods.OsFile.isExist(sourceFile):
                    if bscMethods.MayaApp.isActive():
                        print 'Load File : {}'.format(sourceFile)
                        from LxMaya.command import maFile
                        maFile.openFileToTemp(sourceFile)
    #
    def loadProductFile(self):
        update = self.getUpdate()
        #
        productRecordDic = self._productFileDic
        if update:
            if update in productRecordDic:
                productFile = productRecordDic[update]
                if bscMethods.OsFile.isExist(productFile):
                    if bscMethods.MayaApp.isActive():
                        print 'Load File : {}'.format(productFile)
                        from LxMaya.command import maFile
                        maFile.openFileToTemp(productFile)
    #
    def setupUnit(self):
        self.topToolBar().hide()
        #
        self._mainToolBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._mainToolBox)
        self._mainToolBox.setTitle('Record')
        self.setupMainToolUiBox(self._mainToolBox)


class IfProductUnitRecordUnit_(_qtIfAbcWidget.QtIfAbc_Unit):
    def __init__(self, *args, **kwargs):
        super(IfProductUnitRecordUnit_, self).__init__(*args, **kwargs)
        self._initIfAbcUnit()
        #
        self.setupUnit()


class QtIf_ProjectOverviewUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    def __init__(self):
        super(QtIf_ProjectOverviewUnit, self).__init__()
        self._initIfAbcUnit()
        #
        self.setupUnit()
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setCentralRefresh()
            self.setRightRefresh()
    #
    def setupCentralWidget(self, layout):
        def setToolGroupTitleSwitch():
            currentItem = self._centralGridview.currentItem()
            if currentItem:
                toolGroup.setTitle('Project > {}'.format(currentItem.name()))
        #
        toolGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(toolGroup)
        toolGroup.setTitle('Project')
        toolGroup.setExpanded(True)
        #
        self._centralGridview = qtWidgets.QtGridview()
        toolGroup.addWidget(self._centralGridview)
        self._centralGridview.setCheckEnable(True)
        #
        width = 320
        height = int(width * (float(1080) / float(1920)))
        #
        self._uiItemWidth, self._uiItemHeight = width, height
        #
        self._centralGridview.setItemSize(self._uiItemWidth, self._uiItemHeight + 20)
        self._centralGridview.setItemListModeSize(self._uiItemWidth, 20)
        self._centralGridview.setItemIconModeSize(self._uiItemWidth, self._uiItemHeight + 20)
        #
        self._centralGridview.setFilterConnect(self.filterEnterLabel())
        #
        self._centralGridview.currentChanged.connect(setToolGroupTitleSwitch)
    #
    def setupRightWidget(self, layout):
        toolGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(toolGroup)
        toolGroup.setTitle('Preset & Information')
        toolGroup.setExpanded(True)
        #
        self._rightTreeView = qtWidgets.QtTreeview()
        toolGroup.addWidget(self._rightTreeView)
        self._rightTreeView.setFilterConnect(self.filterEnterLabel())
    #
    def setCentralRefresh(self):
        def setBranch(seq, key, value):
            def setBranchAction():
                def loadProjectCmd():
                    if bscMethods.MayaApp.isActive():
                        from LxCore.setup import appSetup
                        #
                        from LxInterface.qt.ifWidgets import ifProductWindow
                        #
                        from LxCore import shmOutput
                        #
                        mayaVersion = bscMethods.MayaApp.version()
                        #
                        sourceProjectName = prsMethods.Project.mayaActiveName()
                        targetProjectName = projectName
                        #
                        prsMethods.Project._setMayaLocalConfig(targetProjectName, mayaVersion)
                        prsMethods.Project._setMayaProjectEnviron(targetProjectName)
                        isCloseMaya = prsMethods.Project.isMayaPlugPresetSame(sourceProjectName, targetProjectName)
                        # Switch Pipeline
                        appSetup.setLynxiSetup(
                            showProgress=True, isCloseMaya=isCloseMaya
                        )
                        # Update Method
                        shmOutput.Resource().loadActive(force=True)
                        # Switch Panel
                        w = ifProductWindow.QtIf_ToolFloatWindow()
                        w.windowShow()
                        #
                        bscObjects.If_Message(
                            u'Project is Switch to ',
                            u'{}'.format(targetProjectName)
                        )
                        #
                        if self.connectObject() is not None:
                            mainWindow = self.connectObject()._mainWindow
                            if hasattr(mainWindow, 'uiQuit'):
                                mainWindow.uiQuit()
                #
                actionDatumLis = [
                    ('Basic', ),
                    ('Load Project', ('svg_basic@svg#project', 'svg_basic@svg#load_action'), True, loadProjectCmd)
                ]
                #
                gridItem.setActionData(actionDatumLis, title=projectViewName)
            #
            projectName = key
            #
            enabled, projectViewName = value
            if enabled is True:
                gridItem = qtWidgets.QtGridviewItem()
                gridView.addItem(gridItem)
                #
                gridItem.setName(projectName)
                gridItem.setNameText(u'{} ( {} )'.format(projectViewName, projectName))
                gridItem.setIcon('svg_basic@svg#project')
                #
                messageWidget = qtWidgets.QtMessageWidget()
                gridItem.addWidget(messageWidget, 0, 0, 1, 1)
                #
                messageLis = [
                    (2, 'a')
                ]
                messageWidget.setExplainWidth(20)
                #
                messageWidget.setDatumLis(messageLis, self._uiItemWidth, self._uiItemHeight)
                #
                if projectName == currentProjectName:
                    gridItem.setFilterColor((63, 255, 127, 255))
                else:
                    gridItem.setFilterColor((95, 95, 95, 255))
                #
                setBranchAction()
        #
        def setMain():
            gridView.cleanItems()
            if projectNameData:
                maxCount = len(projectNameData)
                if self.connectObject():
                    self.connectObject()._mainWindow.setMaxProgressValue(maxCount)
                for seq, (k, v) in enumerate(projectNameData.items()):
                    if self.connectObject():
                        self.connectObject()._mainWindow.updateProgress()
                    setBranch(seq, k, v)
        #
        gridView = self._centralGridview
        #
        if bscMethods.MayaApp.isActive():
            projectNameData = prsMethods.Project.mayaDatumDict()
            currentProjectName = prsMethods.Project.mayaActiveName()
        else:
            projectNameData = prsMethods.Project.schemeDatumDic()
            currentProjectName = prsMethods.Project.activeName()
        #
        setMain()
        #
        gridView.setRefresh()
        gridView.setSortByName()
    #
    def setRightRefresh(self):
        def setAction(treeItem):
            def copyCmd():
                qtCommands.setTextToClipboard(treeItem.nameText())

            treeItem.setActionData(
                [
                    ('Basic',),
                    ('Copy', 'svg_basic@svg#copy', True, copyCmd)
                ]
            )

        def setVariantPresetBranch(parentItem):
            data = prsMethods.Project.variantPresetDict()
            if data:
                for k, v in data.items():
                    mainPresetItem = qtWidgets.QtTreeviewItem()
                    parentItem.addChild(mainPresetItem)
                    #
                    mainPresetItem.setNameText('{} ( {} )'.format(k, len(v)))
                    for ik, iv in v.items():
                        subPresetItem = qtWidgets.QtTreeviewItem()
                        mainPresetItem.addChild(subPresetItem)
                        #
                        if isinstance(iv, tuple) or isinstance(iv, list):
                            iv_ = u'; '.join(iv)
                        else:
                            iv_ = iv
                        #
                        if iv_ is not None:
                            subPresetItem.setNameText(u'{} = {}'.format(ik, iv_))
            return len(data)
        #
        def setSoftwarePresetBranch(parentItem):
            def setSubBranch(key, value):
                if value:
                    mainPresetItem = qtWidgets.QtTreeviewItem()
                    parentItem.addChild(mainPresetItem)
                    #
                    mainPresetItem.setNameText(u'{} ( {} )'.format(key, len(value)))
                    for ik, iv in value.items():
                        subPresetItem = qtWidgets.QtTreeviewItem()
                        mainPresetItem.addChild(subPresetItem)
                        #
                        if isinstance(iv, str) or isinstance(iv, unicode):
                            subPresetItem.setNameText(u'{} = {}'.format(ik, iv))
                        elif isinstance(iv, tuple) or isinstance(iv, list):
                            subPresetItem.setNameText(u'{} ( {} )'.format(ik, len(iv)))
                            for i in iv:
                                branchPresetItem = qtWidgets.QtTreeviewItem()
                                subPresetItem.addChild(branchPresetItem)
                                branchPresetItem.setNameText(i)
                        elif isinstance(iv, dict):
                            subPresetItem.setNameText(u'{} ( {} )'.format(ik, len(iv)))
                            for jk, jv in iv.items():
                                branchPresetItem = qtWidgets.QtTreeviewItem()
                                subPresetItem.addChild(branchPresetItem)
                                branchPresetItem.setNameText('{} = {}'.format(jk, jv))
            #
            if bscMethods.MayaApp.isActive():
                setSubBranch('Maya Tool', prsMethods.Project.mayaToolDatumDict())
                setSubBranch('Maya Script', prsMethods.Project.mayaScriptDatumDict())
            return 3
        #
        def setOsEnvironBranch(parentItem):
            data = bscMethods.OsEnviron.getEnvironDict()
            if data:
                for k, v in data.items():
                    mainPresetItem = qtWidgets.QtTreeviewItem()
                    parentItem.addChild(mainPresetItem)
                    #
                    mainPresetItem.setNameText('{} ( {} )'.format(k, len(v)))
                    for i in v:
                        subPresetItem = qtWidgets.QtTreeviewItem()
                        mainPresetItem.addChild(subPresetItem)
                        #
                        subPresetItem.setNameText(i)
                        setAction(subPresetItem)
            return len(data)
        #
        def setMayaModuleBranch(parentItem):
            if bscMethods.MayaApp.isActive():
                from LxMaya.command import maUtils
                data = maUtils.getModuleInfo()
                if data:
                    for k, v in data.items():
                        mainPresetItem = qtWidgets.QtTreeviewItem()
                        parentItem.addChild(mainPresetItem)
                        #
                        mainPresetItem.setNameText('{} ( {} )'.format(k, len(v)))
                        for ik, iv in v.items():
                            subPresetItem = qtWidgets.QtTreeviewItem()
                            mainPresetItem.addChild(subPresetItem)
                            #
                            subPresetItem.setNameText(u'{} = {}'.format(ik, iv))
        #
        dataLis = [
            ('Variant Preset', setVariantPresetBranch),
            ('Software Preset', setSoftwarePresetBranch),
            ('Os Environ', setOsEnvironBranch),
            ('Maya Module', setMayaModuleBranch),
        ]
        #
        treeView = self._rightTreeView
        #
        for mainExplain, method in dataLis:
            mainItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(mainItem)
            #
            if method is not None:
                count = method(mainItem)
            else:
                count = 0
            #
            mainItem.setNameText('{} ( {} )'.format(mainExplain, count))
    #
    def confirmCmd(self):
        if bscMethods.MayaApp.isActive():
            targetProjectItem = self._centralGridview.currentItem()
            if targetProjectItem is not None:
                from LxCore.setup import appSetup
                #
                from LxInterface.qt.ifWidgets import ifProductWindow
                #
                from LxCore import shmOutput
                #
                mayaVersion = bscMethods.MayaApp.version()
                #
                sourceProjectName = prsMethods.Project.mayaActiveName()
                targetProjectName = targetProjectItem.name()
                #
                prsMethods.Project._setMayaLocalConfig(targetProjectName, mayaVersion)
                prsMethods.Project._setMayaProjectEnviron(targetProjectName)
                isCloseMaya = prsMethods.Project.isMayaPlugPresetSame(sourceProjectName, targetProjectName)
                # Switch Pipeline
                appSetup.setLynxiSetup(
                    showProgress=True, isCloseMaya=isCloseMaya
                )
                # Update Method
                shmOutput.Resource().loadActive(force=True)
                # Switch Panel
                w = ifProductWindow.QtIf_ToolFloatWindow()
                w.windowShow()
                #
                bscObjects.If_Message(
                    u'Project is Switch to ',
                    u'{}'.format(targetProjectName)
                )
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        centralScrollBox = qtCore.QScrollArea_()
        layout.addWidget(centralScrollBox)
        self.setupCentralWidget(centralScrollBox)
        #
        rightExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(rightExpandWidget)
        rightExpandWidget.setExpandDir(qtCore.LeftDir)
        rightExpandWidget.setUiWidth(self.SideWidth*2)
        rightExpandWidget.setExpanded(False)
        #
        rightScrollBox = qtCore.QScrollArea_()
        rightExpandWidget.addWidget(rightScrollBox)
        self.setupRightWidget(rightScrollBox)


class IfPersonnelRegisterUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    tips = [
        u"提示：",
        u"1：输入 中文名（ CH - Name ） ；",
        u"2：输入 英文名（ EN - Name ） ；",
        u"3：输入 邮箱（ e - Mail ） ；",
        u"4：选择 工作组（ Team ） ；",
        u"4：点击 Confirm 确认设置...",
    ]
    #
    errorTip1 = [
        u"提示：请输入 中文名（ CH - Name ）...",
    ]
    errorTips2 = [
        u"提示：请输入 英文名（ EN - Name ）...",
    ]
    errorTips3 = [
        u"提示：请输入 邮箱（ e - Mail ）...",
    ]
    errorTips4 = [
        u"提示：请输入 工作组（ Team ）...",
    ]
    #
    w = 100
    dicRegister = dict(
        user=[w, 0, 0, 1, 1, 'Os User'],
        chName=[w, 1, 0, 1, 1, 'Ch - Name'],
        enName=[w, 2, 0, 1, 1, 'En - Name'],
        mail=[w, 3, 0, 1, 1, 'Mail'],
        team=[w, 4, 0, 1, 1, 'Team'],
        post=[w, 5, 0, 1, 1, 'Post'],
        pc=[w, 6, 0, 1, 1, 'PC'],
        ip=[w, 7, 0, 1, 1, 'IP'],
        tip=[w, 0, 1, 8, 1, 'Tip']
    )
    def __init__(self):
        super(IfPersonnelRegisterUnit, self).__init__()
        self._initIfAbcUnit()
        #
        self.setupUnit()
    #
    def refreshMethod(self):
        self.setCentralRefresh()
    #
    def setupCentralWidget(self, layout):
        toolGroup = qtWidgets.QtToolboxGroup()
        toolGroup.setTitle('Register')
        toolGroup.setExpanded(True)
        layout.addWidget(toolGroup)
        #
        toolBox = qtWidgets.QtToolbox()
        toolGroup.addWidget(toolBox)
        self.setupRegisterToolUiBox(toolBox)
    #
    def setupRegisterToolUiBox(self, toolBox):
        inData = self.dicRegister
        # User Name
        self._osUserNameLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'user', self._osUserNameLabel)
        #
        self._chNameLabel = qtWidgets.QtEnterlabel()
        self._chNameLabel.setEnterEnable(True)
        toolBox.setInfo(inData, 'chName', self._chNameLabel)
        #
        self._enNameLabel = qtWidgets.QtEnterlabel()
        self._enNameLabel.setEnterEnable(True)
        toolBox.setInfo(inData, 'enName', self._enNameLabel)
        #
        self._mailLabel = qtWidgets.QtEnterlabel()
        self._mailLabel.setEnterEnable(True)
        toolBox.setInfo(inData, 'mail', self._mailLabel)
        #
        self._teamLabel = qtWidgets.QtEnterlabel()
        self._teamLabel.setChooseEnable(True)
        toolBox.setInfo(inData, 'team', self._teamLabel)
        #
        self._postLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'post', self._postLabel)
        #
        self._pcLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'pc', self._pcLabel)
        #
        self._ipLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'ip', self._ipLabel)
        #
        self._tipLabel = qtWidgets.QtTextbrower()
        self._tipLabel.setEnterEnable(False)
        toolBox.setInfo(inData, 'tip', self._tipLabel)
    #
    def setCentralRefresh(self):
        osUser = bscMethods.OsSystem.username()
        # Os User
        self._osUserNameLabel.setDatum(osUser)
        # CH - Name
        chName = prsMethods.Personnel.userChnname(osUser)
        self._chNameLabel.setDatum(chName)
        self._chNameLabel.setDefaultDatum(chName)
        # En - Name
        enName = prsMethods.Personnel.userEngname(osUser)
        self._enNameLabel.setDatum(enName)
        self._enNameLabel.setDefaultDatum(enName)
        #
        teamLis = prsMethods.Personnel.teams()
        team = prsMethods.Personnel.userTeam(osUser)
        self._teamLabel.setDatumLis(teamLis)
        self._teamLabel.setChoose(team)
        #
        post = prsMethods.Personnel.userPost(osUser)
        self._postLabel.setDatum(post)
        mail = prsMethods.Personnel.userMail(osUser)
        self._mailLabel.setDatum(mail)
        # PC Data
        self._pcLabel.setDatum(bscMethods.OsSystem.hostname())
        # IP Data
        self._ipLabel.setDatum(bscMethods.OsSystem.host())
        # Tip Data
        self._tipLabel.setRule(self.tips)
    #
    def confirmMethod(self):
        isChecked = True
        #
        user = self._osUserNameLabel.datum()
        chName = self._chNameLabel.datum()
        #
        if not chName:
            isChecked = False
            self._tipLabel.setRule(self.errorTip1)
        #
        enName = self._enNameLabel.datum()
        if not enName:
            isChecked = False
            self._tipLabel.setRule(self.errorTips2)
        #
        mail = self._mailLabel.datum()
        if not mail:
            isChecked = False
            self._tipLabel.setRule(self.errorTips3)
        #
        team = self._teamLabel.datum()
        if team == lxConfigure.LynxiValue_Unspecified:
            isChecked = False
            self._tipLabel.setRule(self.errorTips4)
        #
        post = self._postLabel.datum()
        #
        if isChecked:
            prsMethods.Personnel.updateUserDatum(user, chName, enName, mail, team, post)
            if bscMethods.MayaApp.isActive():
                from LxInterface.qt.ifWidgets import ifProductWindow
                #
                w = ifProductWindow.QtIf_ToolFloatWindow()
                w.windowShow()
            #
            bscObjects.If_Message(u'提示：', u'设置用户信息成功')
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        self.setupCentralWidget(layout)


class IfPersonnelOverviewUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    def __init__(self):
        super(IfPersonnelOverviewUnit, self).__init__()
        self._initIfAbcUnit()
        #
        self.setupUnit()
    #
    def refreshMethod(self):
        self.setCentralRefresh()
    #
    def setupLeftWidget(self, layout):
        pass
    #
    def setupCentralWidget(self, layout):
        toolGroup = qtWidgets.QtToolboxGroup()
        toolGroup.setTitle('Personnel')
        toolGroup.setExpanded(True)
        layout.addWidget(toolGroup)
        #
        self._treeView = qtWidgets.QtTreeview()
        self._treeView.setCheckEnable(True)
        self._treeView.setColorEnable(True)
        toolGroup.addWidget(self._treeView)
        self._treeView.setFilterConnect(self.filterEnterLabel())
    #
    def setCentralRefresh(self):
        def setTeamBranch(parentItem):
            teamLis = prsMethods.Personnel.teams()
            if teamLis:
                count = len(teamLis)
                for seq, teamName in enumerate(teamLis):
                    treeItem = qtWidgets.QtTreeviewItem()
                    parentItem.addChild(treeItem)
                    treeItem.setName(teamName)
                    treeItem.setIcon('object#mainBranch')
                    treeItem.setExpanded(True)
                    #
                    r, g, b = qtCore.hsv2rgb(360 * (float(seq) / float(count)), 1, 1)
                    treeItem.setFilterColor((r, g, b, 255))
                    #
                    self._teamItemDic[teamName] = treeItem
        #
        def setUserBranch():
            userLis = prsMethods.Personnel.usernames()
            #
            if userLis:
                for userName in userLis:
                    userDataDic = prsMethods.Personnel.usernameDatumDic(userName)
                    if userDataDic:
                        chName = userDataDic[lxConfigure.LynxiUserCnNameKey]
                        enName = userDataDic[lxConfigure.LynxiUserEnNameKey]
                        mail = userDataDic[lxConfigure.LynxiUserMailKey]
                        team = userDataDic[lxConfigure.DEF_preset_key_Team]
                        post = userDataDic[lxConfigure.DEF_preset_key_Post]
                        #
                        treeItem = qtWidgets.QtTreeviewItem()
                        treeItem.setName(u'{} ( {} )'.format(chName, userName))
                        treeItem.setIcon('object#character')
                        #
                        if team in self._teamItemDic:
                            parentItem = self._teamItemDic[team]
                            parentItem.addChild(treeItem)
                            #
                            treeItem.setFilterColor(parentItem.filterColor())
        #
        self._teamItemDic = {}
        treeView = self._treeView
        #
        treeView.cleanItems()
        #
        personnelItem = qtWidgets.QtTreeviewItem()
        treeView.addItem(personnelItem)
        personnelItem.setName('All')
        personnelItem.setIcon('object#guideBranch')
        #
        personnelItem.setExpanded(True)
        #
        setTeamBranch(personnelItem)
        #
        setUserBranch()
        #
        treeView.setRefresh()
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        self.setupCentralWidget(layout)


class IfToolkitUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    UnitConnectLinks = [
    ]
    UnitName = 'utilsTool'
    UnitTitle = 'Utilities Tool Unit'
    UnitIcon = 'toolBar#utils'
    UnitTooltip = u'''公用工具'''
    #
    SideWidth = 240
    def __init__(self):
        super(IfToolkitUnit, self).__init__()
        self._initIfAbcUnit()
        #
        self.setupUnit()
    #
    def refreshMethod(self):
        self._initMethod()
    #
    def setupLeftWidget(self, layout):
        self._treeView = qtWidgets.QtTreeview()
        layout.addWidget(self._treeView)
        self._treeView.setSelectEnable(True)
        self._treeView.setExpandEnable(False)
        #
        self._treeView.selectedChanged.connect(self.setToolboxGroupExpandedRefresh)
        self._treeView.setFilterConnect(self.filterEnterLabel())
    #
    def setupCentralWidget(self, layout):
        self._toolGroupDic = {}
        # Scroll Bar
        self._centralScrollBox = qtCore.QScrollArea_()
        layout.addWidget(self._centralScrollBox)
    #
    def _initMethod(self):
        currentProjectName = prsMethods.Project.appActiveName()
        self._toolGroupDic = {}
        self._toolFilterDic = {}
        #
        treeView = self._treeView
        #
        self._initTagFilterVar()
        #
        if bscMethods.MayaApp.isActive():
            buildData = prsMethods.Project.mayaToolDatumDict()
            for seq, (k, v) in enumerate(buildData.items()):
                mainToolSearchDic = {}
                subToolSearchDic = {}
                #
                showExplain = v['nameText']
                pipeToolPath = v[lxConfigure.LynxiServerPathKey]
                mainToolDatumLis = prsMethods.Project._getProjectMayaToolDatumDictByDirectory(pipeToolPath)
                utilsToolPath = v[lxConfigure.LynxiUtilitiesPathKey]
                subToolDatumLis = prsMethods.Project._getProjectMayaToolDatumDictByDirectory(utilsToolPath)
                #
                projectCount, utilitiesCount = len(mainToolDatumLis), len(subToolDatumLis)
                #
                toolGroupBox = qtWidgets.QtToolboxGroup()
                self._centralScrollBox.addWidget(toolGroupBox)
                toolGroupBox.setNameText(showExplain)
                toolGroupBox.setIndexText('( {} + {} )'.format(projectCount, utilitiesCount))
                self._toolGroupDic[k] = toolGroupBox
                #
                tagItem = qtWidgets.QtTreeviewItem()
                treeView.addItem(tagItem)
                tagItem.setName(k)
                tagItem.setNameText(showExplain)
                tagItem.setIcon('svg_basic@svg#branch_main')
                #
                tagItem.visibleToggled.connect(toolGroupBox.setVisible)
                #
                tag = showExplain
                if not tag in self._tagLis:
                    self._tagLis.append(tag)
                if not tag in self._tagFilterEnableDic:
                    self._tagFilterEnableDic[tag] = True
                #
                if not currentProjectName.startswith(lxConfigure.Lynxi_Keyword_Project_Default):
                    self.setupToolUiBox(mainToolDatumLis, treeView, tag, tagItem, toolGroupBox, mainToolSearchDic, keyword='Project')

                self._toolFilterDic[k] = mainToolSearchDic
                #
                self.setupToolUiBox(subToolDatumLis, treeView, tag, tagItem, toolGroupBox, subToolSearchDic, keyword='Utilities')
                self._toolFilterDic[k] = subToolSearchDic
                #
                self.setToolGroupAction(toolGroupBox, pipeToolPath, utilsToolPath)
                #
                itemIndex = treeView.itemIndex(tagItem)
                self._tagFilterIndexDic.setdefault(tag, []).append(itemIndex)
        #
        self._initTagFilterAction(self._treeView)
    @staticmethod
    def setToolGroupAction(widget, path1, path2):
        def openPipelineFolderCmd():
            bscMethods.OsDirectory.open(path1)
        #
        def openPipelineFolderEnable():
            return bscMethods.OsDirectory.isExist(path1)
        #
        def openUtilitiesFolderCmd():
            bscMethods.OsDirectory.open(path2)
        #
        def openUtilitiesFolderEnable():
            return bscMethods.OsDirectory.isExist(path2)
        #
        actions = [
            ('Basic', ),
            ('Open Tool Folder ( Project )', 'svg_basic@svg#folder', openPipelineFolderEnable, openPipelineFolderCmd),
            ('Open Tool Folder ( Utilities )', 'svg_basic@svg#folder', openUtilitiesFolderEnable, openUtilitiesFolderCmd)
        ]
        widget.setActionData(actions)
    # Util Method
    def setupToolUiBox(self, data, treeView, tag, tagItem, toolGroupBox, itemData, keyword):
        def setBranch(seq, k, subToolBox):
            def openCommandCmd():
                osCmdExe = 'sublime_text.exe'
                osCmd = '''"{}" "{}"'''.format(osCmdExe, commandFile)
                bscMethods.OsSystem.runCommand(osCmd)
            #
            toolName = k
            commandFile, command, toolTip = data[k]
            #
            viewExplain = bscMethods.StrCamelcase.toPrettify(toolName)
            #
            toolItem = qtWidgets.QtTreeviewItem()
            tagItem.addChild(toolItem)
            toolItem.setNameText(viewExplain)
            toolItem.setIcon('svg_basic@svg#tag')
            itemIndex = treeView.itemIndex(toolItem)
            self._tagFilterIndexDic.setdefault(tag, []).append(itemIndex)
            #
            button = qtWidgets.QtPressbutton()
            button.setPressCommand(command)
            if toolTip:
                button.setTooltip(toolTip)
            #
            button.setIcon('svg_basic@svg#subWindow')
            #
            width = 80
            x1 = seq
            x2 = 0
            if seq % 2:
                x1 = seq - 1
                x2 = 2
            #
            uiData = [width, x1, x2, 1, 2, viewExplain]
            subToolBox.setTool(uiData, button)
            #
            if self.connectObject():
                pass
            #
            button.setActionData(
                [
                    ('Basic', ),
                    ('Edit Command', 'svg_basic@svg#modify', True, openCommandCmd),
                    ('Extend', ),
                    ('Help', 'svg_basic@svg#help', True)
                ]
            )
            #
            itemData[toolName] = button
        #
        def setMain():
            dicStep01 = bscCore.orderedDict(
                [
                    ('{} - Create'.format(keyword), []),
                    ('{} - Loaded'.format(keyword), []),
                    ('{} - Manager'.format(keyword), []),
                    ('{} - Other'.format(keyword), [])
                ]
            )
            if data:
                for i in data:
                    if i.endswith('Create'):
                        dicStep01.setdefault('{} - Create'.format(keyword), []).append(i)
                    elif i.endswith('Loaded'):
                        dicStep01.setdefault('{} - Loaded'.format(keyword), []).append(i)
                    elif i.endswith('Manager'):
                        dicStep01.setdefault('{} - Manager'.format(keyword), []).append(i)
                    else:
                        dicStep01.setdefault('{} - Other'.format(keyword), []).append(i)
                #
                for k, v in dicStep01.items():
                    if v:
                        subToolBox = qtWidgets.QtToolbox()
                        subToolBox.setTitle(k)
                        toolGroupBox.addWidget(subToolBox)
                        for seq, i in enumerate(v):
                            setBranch(seq, i, subToolBox)
        #
        setMain()
    #
    def setToolboxGroupExpandedRefresh(self):
        itemModels = self._treeView.itemModels()
        for itemModel in itemModels:
            key = itemModel.name()
            if key in self._toolGroupDic:
                toolGroupBox = self._toolGroupDic[key]
                toolGroupBox.setExpanded(itemModel.isSelected() or itemModel.isSubSelected())
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        layout = qtCore.QHBoxLayout_(widget)
        self.mainLayout().addWidget(widget)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(leftExpandWidget)
        leftExpandWidget.setExpanded(False)
        leftExpandWidget.setUiWidth(self.SideWidth)
        #
        leftWidget = qtCore.QWidget_()
        leftExpandWidget.addWidget(leftWidget)
        leftLayout = qtCore.QVBoxLayout_(leftWidget)
        self.setupLeftWidget(leftLayout)
        #
        centralWidget = qtCore.QWidget_()
        layout.addWidget(centralWidget)
        centralLayout = qtCore.QVBoxLayout_(centralWidget)
        self.setupCentralWidget(centralLayout)


class QtIf_SystemInformationUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    def __init__(self):
        super(QtIf_SystemInformationUnit, self).__init__()
        self._initIfAbcUnit()
        #
        self.setupUnit()

    def setupUnit(self):
        pass
