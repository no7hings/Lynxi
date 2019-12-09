# coding=utf-8
from LxCore import lxBasic, lxConfigure, lxProgress
#
from LxInterface.qt.ifWidgets import ifUnit
#
from LxCore.preset.prod import projectPr, scenePr
#
from LxUi import uiConfigure
#
from LxUi.qt import qtWidgets_, qtChart_, qtWidgets, qtCore
#
from LxInterface.qt.ifCommands import treeViewCmds
#
none = ''


#
class IfCacheManagerWindow(qtWidgets.UiToolWindow):
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfCacheManagerWindow, self).__init__(parent)
        self.setDefaultSize(*uiConfigure.Lynxi_Ui_Window_Size_Dialog)
        #
        self.setupWindow()
    #
    def setArgs(self, string, args):
        self._managerUnit.setArgs(string, args)
    #
    def setListCache(self):
        self._managerUnit.setListCache()
    @qtCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        mainWidget = qtCore.QWidget_()
        self.addWidget(mainWidget)
        mainLayout = qtCore.QVBoxLayout_(mainWidget)
        mainLayout.setContentsMargins(2, 2, 2, 2)
        mainLayout.setSpacing(2)
        #
        self._managerUnit = ifUnit.IfScCacheManagerUnit()
        mainLayout.addWidget(self._managerUnit)
        self._managerUnit.setConnectObject(self)


#
class IfScIndexManagerWindow(qtWidgets.UiDialogWindow):
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfScIndexManagerWindow, self).__init__(parent)
        self.setDefaultSize(960, 480)
        self.setIndexText(lxConfigure.Lynxi_Module_Python().localVersion())
        #
        self.setupWindow()
    #
    def setupCentralToolBox(self, layout):
        pass
    #
    def setArgs(self, keyword, args):
        self._unit.setArgs(keyword, args)
    #
    def refreshMethod(self):
        reload(ifUnit)
        self._unit.refreshMethod()
    @qtCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        reload(ifUnit)
        self._unit = ifUnit.IfScIndexManagerUnit()
        self.addWidget(self._unit)
        #
        self.confirmClicked.connect(self._unit.confirmCmd)


#
class IfScRenderManagerWindow(qtWidgets.UiToolWindow):
    SideWidth = 320
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfScRenderManagerWindow, self).__init__(parent)
        #
        self.setNameText('Scene Render ( Image ) Manager')
        self.setDefaultSize(*uiConfigure.Lynxi_Ui_Window_SubSize_Default)
        #
        self.initializationPanel()
        #
        self.setupWindow()
    #
    def refreshMethod(self):
        self.setListTreeItem()
    #
    def setupRightWidget(self, scrollLayout):
        self._recordUnit = ifUnit.IfProductUnitRecordUnit()
        scrollLayout.addWidget(self._recordUnit)
    #
    def setArgs(self, *args):
        sceneIndex, projectName, sceneClass, sceneName, sceneVariant, sceneStage, startFrame, endFrame = args
        #
        self.projectName = projectName
        #
        self.sceneIndex = sceneIndex
        self.sceneClass = sceneClass
        self.sceneName = sceneName
        self.sceneVariant = sceneVariant
        self.sceneStage = sceneStage
        #
        self.startFrame = startFrame
        self.endFrame = endFrame
        #
        self.setupRightWidget(self._rightScrollLayout)
    @staticmethod
    def setTreeViewBox(treeBox):
        treeBox.setColumns(
            ['File', 'Time', 'Completion'],
            [4, 2, 2],
            800 - 20
        )
    #
    def setListTreeItem(self):
        projectName = self.projectName
        #
        sceneIndex = self.sceneIndex
        sceneClass = self.sceneClass
        sceneName = self.sceneName
        sceneVariant = self.sceneVariant
        sceneStage = self.sceneStage
        #
        startFrame = self.startFrame
        endFrame = self.endFrame
        #
        treeBox = self.treeViewBox
        treeBox.clear()
        #
        customizes = scenePr.getScRenderCustomizes(
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage
        )
        #
        viewExplain = scenePr.getSceneViewInfo(
            sceneIndex, sceneClass, '{} - {}'.format(sceneName, sceneVariant)
        )
        #
        sceneItem = qtWidgets_.QTreeWidgetItem_()
        treeBox.addItem(sceneItem)
        sceneItem.setText(0, viewExplain)
        sceneItem.setItemIcon_(0, 'svg_basic@svg#package_object')
        #
        self._methodLis = treeViewCmds.setListScRenderImageCustomize(
            sceneItem,
            customizes,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame
        )
        #
        self.setStartThread()
    #
    def setRecordRefresh(self):
        selectedItems = self.treeViewBox.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0]
            if hasattr(selectedItem, 'customize'):
                customize = selectedItem.customize
                projectName = self.projectName
                #
                sceneIndex = self.sceneIndex
                sceneClass = self.sceneClass
                sceneName = self.sceneName
                sceneVariant = self.sceneVariant
                sceneStage = self.sceneStage
                #
                backupSourceFile = scenePr.sceneUnitSourceFile(
                    lxConfigure.LynxiRootIndex_Backup,
                    projectName, sceneClass, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_Light,
                )[1]
                #
                backupProductFile = scenePr.scUnitRenderFile(
                    lxConfigure.LynxiRootIndex_Backup,
                    projectName, sceneClass, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_Light,
                    customize
                )[1]
                #
                self._recordUnit.setRecordConnect(backupSourceFile, backupProductFile)
            else:
                self._recordUnit.setRecordConnect(None, None)
        else:
            self._recordUnit.setRecordConnect(None, None)
    #
    def setTimerClear(self):
        if self._timerLis:
            for i in self._timerLis:
                i.stop()
                i.deleteLater()
    #
    def setStartThread(self):
        def setBranch(index, method):
            def threadMethod():
                def timerMethod():
                    thread.setThreadEnable(True)
                    #
                    thread.start()
                    timer.stop()
                #
                if thread.isStarted() is False:
                    timer.start(10000 + index * 100)
                    timer.timeout.connect(timerMethod)
                else:
                    timer.start(10000)
                #
                thread.setStarted(True)
                #
                method()
                #
                thread.setThreadEnable(False)
                #
                thread.wait()
            #
            timer = qtWidgets_.QtCore.QTimer(self)
            self._timerLis.append(timer)
            #
            thread = qtCore.QThread_(self)
            thread.setThreadIndex(index)
            thread.started.connect(threadMethod)
            thread.start()
        #
        self._timerLis = []
        #
        if self._methodLis:
            for seq, i in enumerate(self._methodLis):
                i()
                setBranch(seq, i)
    #
    def initializationPanel(self):
        self._timerLis = []
        self._methodLis = []
    @qtCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        mainWidget = qtCore.QWidget_()
        self.addWidget(mainWidget)
        mainLayout = qtCore.QHBoxLayout_(mainWidget)
        mainLayout.setContentsMargins(2, 2, 2, 2)
        mainLayout.setSpacing(0)
        #
        self.treeViewBox = qtWidgets_.QTreeWidget_()
        mainLayout.addWidget(self.treeViewBox)
        self.setTreeViewBox(self.treeViewBox)
        self.treeViewBox.itemSelectionChanged.connect(self.setRecordRefresh)
        #
        self._rightExpandBox = qtWidgets_.QtExpandWidget()
        mainLayout.addWidget(self._rightExpandBox)
        self._rightExpandBox.setExpandDir(qtCore.LeftDir)
        self._rightExpandBox.setExpanded(False)
        self._rightExpandBox.setUiWidth(self.SideWidth)
        #
        self._rightScrollLayout = qtCore.QScrollArea_()
        self._rightExpandBox.addWidget(self._rightScrollLayout)


#
class IfRenderImageComposeWindow(qtWidgets.UiToolWindow):
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfRenderImageComposeWindow, self).__init__(parent)
        #
        self.setNameText('Scene Render ( Image ) Manager')
        #
        self.setDefaultSize(*uiConfigure.Lynxi_Ui_Window_SubSize_Default)
        #
        self.initializationPanel()
        #
        self.setupWindow()
    #
    def refreshMethod(self):
        self.setListTreeItem()
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
        # self._refreshButton.clicked.connect(self.setCentralRefresh)
    #
    def setupCentralWidget(self, layout):
        def setTreeViewBox(treeBox):
            treeBox.setColumns(
                ['File', 'Time', 'Completion'],
                [4, 2, 2],
                800 - 20
            )
            #
            treeBox.setFilterConnect(self._filterEnterLabel)
        #
        splitterLayout = qtWidgets_.xSplitter()
        layout.addWidget(splitterLayout)
        #
        self.treeViewBox = qtWidgets_.QTreeWidget_()
        splitterLayout.addWidget(self.treeViewBox)
        setTreeViewBox(self.treeViewBox)
        #
        self.setQuitConnect(self.setTimerClear)
    #
    def setListTreeItem(self):
        def setSceneBranch(key, value):
            progressBar.updateProgress()
            #
            sceneIndex, sceneVariant = key
            #
            (
                description,
                sceneClass, sceneName, scenePriority, scLayoutEnable,
                scAnimationEnable, scSolverEnable, scSimulationEnable, scLightEnable
            ) = value
            #
            sceneStage = lxConfigure.LynxiProduct_Scene_Link_Light
            #
            startFrame, endFrame = scenePr.getScUnitFrameRange(
                projectName,
                sceneClass, sceneName, sceneVariant
            )
            #
            customizes = scenePr.getScRenderCustomizes(
                projectName,
                sceneClass, sceneName, sceneVariant, sceneStage
            )
            sceneItem = qtWidgets_.QTreeWidgetItem_()
            treeBox.addItem(sceneItem)
            #
            sceneItem.setItemIcon(0, 'object#scene')
            sceneItemLis.append(sceneItem)
            #
            showExplain = scenePr.getSceneViewInfo(sceneIndex, sceneClass, sceneName)
            sceneItem.setText(0, showExplain)
            #
            subMethods = treeViewCmds.setListScRenderImageCustomize(
                sceneItem,
                customizes,
                projectName,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame
            )
            #
            self._methodLis.extend(subMethods)
        #
        self._methodLis = []
        #
        sceneItemLis = []
        #
        projectName = projectPr.getMayaProjectName()
        #
        treeBox = self.treeViewBox
        inData = scenePr.getUiSceneSetDataDic(projectName)
        #
        treeBox.clear()
        if inData:
            explain = '''List Scene Render'''
            maxValue = len(inData)
            progressBar = lxProgress.viewSubProgress(explain, maxValue)
            [setSceneBranch(k, v) for k, v in inData.items()]
            #
            treeBox.setFilterLimitLis(sceneItemLis)
        #
        self.setStartThread()
    #
    def setTimerClear(self):
        if self._timerLis:
            for i in self._timerLis:
                i.stop()
                i.deleteLater()
    #
    def setStartThread(self):
        def setBranch(index, method):
            def threadMethod():
                def timerMethod():
                    thread.setThreadEnable(True)
                    #
                    thread.start()
                    timer.stop()
                #
                if thread.isStarted() is False:
                    timer.start(10000 + index * 100)
                    timer.timeout.connect(timerMethod)
                else:
                    timer.start(10000)
                #
                thread.setStarted(True)
                #
                method()
                #
                thread.setThreadEnable(False)
                #
                thread.wait()
            #
            timer = qtWidgets_.QtCore.QTimer(self)
            self._timerLis.append(timer)
            #
            thread = qtCore.QThread_(self)
            thread.setThreadIndex(index)
            thread.started.connect(threadMethod)
            thread.start()
        #
        self._timerLis = []
        #
        if self._methodLis:
            explain = '''Build Thread'''
            maxValue = len(self._methodLis)
            progressBar = lxProgress.viewSubProgress(explain, maxValue)
            for seq, i in enumerate(self._methodLis):
                progressBar.updateProgress()
                i()
                setBranch(seq, i)
    #
    def initializationPanel(self):
        self._timerLis = []
        self._methodLis = []
    @qtCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        mainWidget = qtCore.QWidget_()
        self.addWidget(mainWidget)
        mainLayout = qtCore.QVBoxLayout_(mainWidget)
        mainLayout.setContentsMargins(2, 2, 2, 2)
        mainLayout.setSpacing(0)
        #
        topToolBar = qtWidgets_.xToolBar()
        mainLayout.addWidget(topToolBar)
        self.setupTopToolBar(topToolBar)
        #
        centralWidget = qtWidgets_.QTreeWidget_()
        mainLayout.addWidget(centralWidget)
        centralLayout = qtCore.QHBoxLayout_(centralWidget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        centralLayout.setSpacing(0)
        self.setupCentralWidget(centralLayout)


#
class IfRenderFileComposeWindow(qtWidgets.UiToolWindow):
    w = 80
    dicTool = lxBasic.orderedDict()
    dicTool['sourceDirectory'] = [w, 0, 0, 1, 4, 'Source']
    dicTool['targetDirectory'] = [w, 1, 0, 1, 4, 'Target']
    dicTool['collectionFile'] = [w, 2, 0, 1, 4, 'Collection']
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfRenderFileComposeWindow, self).__init__(parent)
        #
        self.setNameText('Scene Render ( Compose ) Manager')
        #
        self.setDefaultSize(*uiConfigure.Lynxi_Ui_Window_SubSize_Default)
        #
        self.initializationPanel()
        #
        self.setupWindow()
    #
    def refreshMethod(self):
        self.setListLeftTreeItem()
    #
    def setListLeftTreeItem(self):
        def setSceneBranch(key, value):
            def setCustomizeBranch(customize):
                def setActionData():
                    def openRenderFile():
                        if lxBasic.isOsExistsFile(serverRenderFile):
                            from LxMaya.command import maFile
                            maFile.fileOpen(serverRenderFile)
                    #
                    def openRenderFolder():
                        lxBasic.setOsFolderOpen(renderFolder)
                    #
                    renderFolder = scenePr.scUnitRenderFolder(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName,
                        sceneClass, sceneName, sceneVariant, sceneStage,
                        customize
                    )
                    #
                    actions = [
                        ('Open Render File', 'menu#maFile', True, openRenderFile),
                        (),
                        ('Open Render Folder', 'svg_basic@svg#folder', True, openRenderFolder)
                    ]
                    itemWidget.setActionData(actions)
                #
                serverRenderFile = scenePr.scUnitRenderFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName, sceneClass, sceneName, sceneVariant, sceneStage, customize
                )[1]
                #
                customizeItem = qtWidgets_.QTreeWidgetItem_()
                sceneItem.addChild(customizeItem)
                #
                itemWidget = customizeItem.setItemIconWidget(0, 'object#mayaFile', customize)
                setActionData()
                showTimeTag = lxBasic.getCnViewTime(lxBasic.getOsFileMtimestamp(serverRenderFile))
                #
                customizeItem.setText(1, showTimeTag)
                #
                composeFiles = scenePr.getScRenderCompose(
                    projectName,
                    sceneClass, sceneName, sceneVariant, sceneStage,
                    customize
                )
                #
                customizeItem.compose = composeFiles or []
                customizeItem.showExplain = u'{1}@{0}'.format(showExplain, customize)
            #
            progressBar.updateProgress()
            #
            sceneIndex, sceneVariant = key
            #
            description, sceneClass, sceneName = value[:3]
            #
            sceneStage = lxConfigure.LynxiProduct_Scene_Link_Light
            #
            sceneItem = qtWidgets_.QTreeWidgetItem_()
            projectItem.addChild(sceneItem)
            #
            customizes = scenePr.getScRenderCustomizes(
                projectName,
                sceneClass, sceneName, sceneVariant, sceneStage
            )
            #
            sceneItem.setItemIcon(0, 'object#scene', ['off', none][customizes != []])
            #
            showExplain = scenePr.getSceneViewInfo(sceneIndex, sceneClass, sceneName)
            sceneItem.setText(0, showExplain)
            #
            sceneItem.setExpanded(True)
            [setCustomizeBranch(i) for i in customizes]
        #
        self._methodLis = []
        #
        projectName = projectPr.getMayaProjectName()
        #
        treeBox = self.leftTreeViewBox
        inData = scenePr.getUiSceneSetDataDic(projectName)
        #
        treeBox.clear()
        #
        projectItem = qtWidgets_.QTreeWidgetItem_()
        projectItem.setItemIcon(0, 'svg_basic@svg#project')
        treeBox.addItem(projectItem)
        #
        projectShowExplain = projectPr.getProjectViewInfo(projectName)
        projectItem.setText(0, projectShowExplain)
        #
        projectItem.setExpanded(True)
        #
        if inData:
            progressExplain = '''List Scene Render'''
            maxValue = len(inData)
            progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
            [setSceneBranch(k, v) for k, v in inData.items()]
    #
    def setListRightTreeItem(self):
        def setBranch(index, osFile):
            def getTargetFile(sourceOsFile):
                return targetPath + sourceOsFile[len(sourcePath):]
            #
            ext = lxBasic.getOsFileExt(osFile)
            #
            self.setProgressValue(index + 1, maxValue)
            #
            treeItem = qtWidgets_.QTreeWidgetItem_()
            treeBox.addItem(treeItem)
            state = none
            if not lxBasic.isOsExistsFile(osFile):
                state = 'off'
            else:
                if not osFile.startswith(sourcePath):
                    state = 'error'
            #
            treeItem.setItemIcon(0, 'treeBox#file', state)
            treeItem.setText(0, osFile)
            #
            targetFile = getTargetFile(osFile)
            if not lxBasic.isOsExistsFile(targetFile):
                subExplain = 'Target is Non - Exists'
                subState = 'error'
                #
                self._needCollectionFileArray.append((osFile, targetFile))
                #
                self._fileConstantStatisticsDic.setdefault('Non - Exists', []).append(osFile)
            else:
                isMtimeChanged = lxBasic.getOsFileIsMtimeChanged(osFile, targetFile)
                if isMtimeChanged:
                    if ext == '.tx':
                        subExplain = 'Collection ( .tx )'
                        subState = none
                    else:
                        subExplain = 'Source is Time - Changed'
                        subState = 'warning'
                        #
                        self._needCollectionFileArray.append((osFile, targetFile))
                        #
                        self._fileConstantStatisticsDic.setdefault('Time - Changed', []).append(osFile)
                else:
                    subExplain = 'Collection'
                    subState = 'on'
                    #
                    self._fileConstantStatisticsDic.setdefault('Collection', []).append(osFile)
            #
            treeItem.setItemIcon(1, 'treeBox#check', subState)
            treeItem.setText(1, subExplain)
            #
            showExplains = showExplainDic[osFile]
            treeItem.setToolTip(0, ','.join(showExplains))
            #
            treeItem.setText(2, str(len(showExplains)))
            #
            self._fileTypeCountStatisticsDic.setdefault(ext, []).append(osFile)
            #
            if lxBasic.isOsExistsFile(osFile):
                fileSize = lxBasic.getOsFileSize(osFile)
            else:
                fileSize = 0
            #
            self._fileTypeSizeStatisticsDic.setdefault(ext, []).append(fileSize)
            #
            self._fileSizes.append(fileSize)
            #
            self._files.append((osFile, targetFile))
        #
        def getProxyCompose(osFile, lis, _showExplain):
            if osFile.endswith('_prx.ass'):
                filePath = lxBasic.getOsFileDirname(osFile)
                texturePath = filePath + '/' + 'texture'
                textures = lxBasic.getOsFilesByPath(texturePath)
                if textures:
                    for t in textures:
                        if not t.endswith('.mayaSwatches'):
                            t = t.lower()
                            if not t in lis:
                                lis.append(t)
                                #
                                showExplainDic.setdefault(t, []).append(_showExplain)
        #
        self._files = []
        self._needCollectionFileArray = []
        #
        self._fileTypeCountStatisticsDic = {}
        self._fileTypeSizeStatisticsDic = {}
        self._fileConstantStatisticsDic = {}
        #
        self._fileSizes = []
        #
        treeBox = self.rightTreeViewBox
        #
        sourcePath = self._sourceDirectoryLabel.datum()
        targetPath = self._targetDirectoryLabel.datum()
        #
        customizeItems = self.getCustomizeItems()
        #
        treeBox.clear()
        if customizeItems:
            showExplainDic = {}
            composeFiles = []
            #
            progressExplain = '''List Scene Compose'''
            maxValue = len(customizeItems)
            progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
            for i in customizeItems:
                progressBar.updateProgress()
                #
                subComposeFiles = i.compose
                showExplain = i.showExplain
                for j in subComposeFiles:
                    realPath = j.lower()
                    if not realPath in composeFiles:
                        composeFiles.append(realPath)
                        getProxyCompose(realPath, composeFiles, showExplain)
                    #
                    showExplainDic.setdefault(realPath, []).append(showExplain)
            #
            if composeFiles:
                composeFiles.sort()
                maxValue = len(composeFiles)
                [setBranch(seq, i) for seq, i in enumerate(composeFiles)]
        #
        self.setCollectionBtnState()
        #
        self.setTypeCountStatistics()
        self.setTypeSizeStatistics()
        self.setFileConstantStatistics()
    #
    def setCollectionBtnState(self):
        maxCount = len(self._files)
        needCollectionCount = len(self._needCollectionFileArray)
        self.collectionFileButton.setPercent(maxCount, maxCount-needCollectionCount)
    #
    def setCollection(self):
        @lxBasic.threadSemaphoreMethod
        def copyFileThreadMethod(sourceFile, targetFile):
            lxBasic.setOsFileCopy(sourceFile, targetFile)
        #
        collectionDataArray = self._needCollectionFileArray
        if collectionDataArray:
            copyThreads = []
            #
            for i, j in collectionDataArray:
                t = lxBasic.runThread(copyFileThreadMethod, i, j)
                copyThreads.append(t)
                t.start()
            # View Progress
            progressExplain = u'''Collection File(s)'''
            maxValue = len(copyThreads)
            progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
            if copyThreads:
                for i in copyThreads:
                    progressBar.updateProgress()
                    i.join()
            #
            self.setListRightTreeItem()
    #
    def setTypeCountStatistics(self):
        lis = []
        statisticsData = self._fileTypeCountStatisticsDic
        if statisticsData:
            maxCount = len(self._files)
            dv = 255 / len(statisticsData)
            for seq, (k, v) in enumerate(statisticsData.items()):
                count = len(v)
                r, g, b = qtCore.hsvToRgb(dv * seq, 1, 1)
                lis.append(('{0} ( {1} / {2} )'.format(k, count, maxCount), count, (r, g, b, 255)))
        #
        self.fileTypeCountPieChart.setDrawData(
            lis
        )
    #
    def setTypeSizeStatistics(self):
        lis = []
        statisticsData = self._fileTypeSizeStatisticsDic
        if statisticsData:
            maxCount = sum(self._fileSizes)
            dv = 255 / len(statisticsData)
            for seq, (k, v) in enumerate(statisticsData.items()):
                count = sum(v)
                r, g, b = qtCore.hsvToRgb(dv * seq, 1, 1)
                lis.append(('{0} ( {1} / {2} )'.format(k, lxBasic.getShowNumber(count, 1), lxBasic.getShowNumber(maxCount, 1)), count, (r, g, b, 255)))
        #
        self.fileTypeSizePieChart.setDrawData(
            lis
        )
    #
    def setFileConstantStatistics(self):
        colorDic = {
            'Non - Exists': (255, 0, 64),
            'Time - Changed': (255, 255, 64),
            'Collection': (64, 255, 127),
        }
        lis = []
        statisticsData = self._fileConstantStatisticsDic
        if statisticsData:
            maxCount = len(self._files)
            for seq, (k, v) in enumerate(statisticsData.items()):
                count = len(v)
                r, g, b = colorDic[k]
                lis.append(('{0} ( {1} / {2} )'.format(k, count, maxCount), count, (r, g, b, 255)))
        #
        self.fileConstantPieChart.setDrawData(
            lis
        )
    #
    def getCustomizeItems(self):
        def getBranch(treeItem):
            if hasattr(treeItem, 'compose'):
                if not treeItem in lis:
                    lis.append(treeItem)
        #
        lis = []
        treeBox = self.leftTreeViewBox
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            for selectedItem in selectedItems:
                getBranch(selectedItem)
                #
                childItems = selectedItem.childItems()
                for childItem in childItems:
                    getBranch(childItem)
        #
        return lis
    #
    def initializationPanel(self):
        self._expandedDic = {}
        #
        self._files = []
        self._needCollectionFileArray = []
        #
        self._fileTypeCountStatisticsDic = {}
        self._fileTypeSizeStatisticsDic = {}
        self._fileConstantStatisticsDic = {}
        #
        self._fileSizes = []
    @qtCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        def setupTopToolBar(layout):
            self._filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
            layout.addWidget(self._filterButton)
            #
            self._filterEnterLabel = qtWidgets.QtFilterEnterlabel()
            layout.addWidget(self._filterEnterLabel)
            #
            self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
            self._refreshButton.setTooltip(u'点击刷新')
            layout.addWidget(self._refreshButton)
            self._refreshButton.clicked.connect(self.setListRightTreeItem)
        #
        def setupLeftTreeViewBox(treeBox):
            treeBox.setColumns(
                ['Scene', 'Update'],
                [3, 2],
                sideWidth - 20
            )
            #
            treeBox.itemSelectionChanged.connect(self.setListRightTreeItem)
        #
        def setupRightTreeViewBox(treeBox):
            treeBox.setColumns(
                ['Directory', 'Collection', 'Frequency'],
                [8, 2, 2],
                1200 - 20
            )
            #
            treeBox.setFilterConnect(self._filterEnterLabel)
        #
        def setupBottomToolBox(toolBox):
            inData = self.dicTool
            self._sourceDirectoryLabel = qtWidgets.QtEnterlabel()
            toolBox.setInfo(inData, 'sourceDirectory', self._sourceDirectoryLabel)
            self._sourceDirectoryLabel.setDatum('l:')
            #
            self._targetDirectoryLabel = qtWidgets.QtEnterlabel()
            toolBox.setInfo(inData, 'targetDirectory', self._targetDirectoryLabel)
            self._targetDirectoryLabel.setDatum('l:/forRender_L/forRender_L')
            #
            self.collectionFileButton = qtWidgets.QtPressbutton()
            toolBox.setButton(inData, 'collectionFile', self.collectionFileButton)
            self.collectionFileButton.setPercentEnable(True)
            self.collectionFileButton.clicked.connect(self.setCollection)
            #
            toolBox.setSeparators(inData)
        #
        def setupStatisticsBox(scrollBox):
            self.fileTypeCountPieChart = qtChart_.QtPiechart_()
            self.fileTypeCountPieChart.setNameText('Count')
            scrollBox.addWidget(self.fileTypeCountPieChart)
            self.fileTypeCountPieChart.setUiSize(sideWidth-40, sideWidth-40)
            #
            self.fileTypeSizePieChart = qtChart_.QtPiechart_()
            self.fileTypeSizePieChart.setNameText('Size')
            scrollBox.addWidget(self.fileTypeSizePieChart)
            self.fileTypeSizePieChart.setUiSize(sideWidth-40, sideWidth-40)
            #
            self.fileConstantPieChart = qtChart_.QtPiechart_()
            self.fileConstantPieChart.setNameText('Constant')
            scrollBox.addWidget(self.fileConstantPieChart)
            self.fileConstantPieChart.setUiSize(sideWidth-40, sideWidth-40)
        #
        mainWidget = qtCore.QWidget_()
        self.addWidget(mainWidget)
        mainLayout = qtCore.QVBoxLayout_(mainWidget)
        mainLayout.setContentsMargins(2, 2, 2, 2)
        mainLayout.setSpacing(2)
        #
        toolBar = qtWidgets_.xToolBar()
        mainLayout.addWidget(toolBar)
        setupTopToolBar(toolBar)
        #
        splitterLayout = qtWidgets_.xSplitter()
        mainLayout.addWidget(splitterLayout)
        #
        sideWidth = 320
        #
        self.leftTreeViewBox = qtWidgets_.QTreeWidget_()
        splitterLayout.addWidget(self.leftTreeViewBox)
        setupLeftTreeViewBox(self.leftTreeViewBox)
        self.leftTreeViewBox.setMaximumWidth(sideWidth)
        self.leftTreeViewBox.setMinimumWidth(sideWidth)
        #
        self.rightTreeViewBox = qtWidgets_.QTreeWidget_()
        splitterLayout.addWidget(self.rightTreeViewBox)
        setupRightTreeViewBox(self.rightTreeViewBox)
        #
        statisticsScrollBox = qtCore.QScrollArea_()
        splitterLayout.addWidget(statisticsScrollBox)
        statisticsScrollBox.setMaximumWidth(sideWidth)
        statisticsScrollBox.setMinimumWidth(sideWidth)
        setupStatisticsBox(statisticsScrollBox)
        #
        bottomToolBox = qtWidgets.QtToolbox()
        mainLayout.addWidget(bottomToolBox)
        bottomToolBox.setTitle('Modify')
        setupBottomToolBox(bottomToolBox)
