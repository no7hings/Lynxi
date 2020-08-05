# coding=utf-8
from LxBasic import bscMtdCore, bscMethods, bscObjects

from LxScheme import shmOutput

from LxPreset import prsConfigure, prsMethods
#
from LxCore.preset.prod import scenePr
#
from LxDatabase import dtbMtdCore
#
from LxGui import guiCore
#
from LxGui.qt import qtModifiers, qtWidgets_, qtChart_, guiQtWidgets, qtCore
#
from ..kitQtCommands import treeViewCmds
#
from ..kitQtWidgets import ifUnit
#
none = ''


class IfCacheManagerWindow(guiQtWidgets.QtToolWindow):
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfCacheManagerWindow, self).__init__(parent)

        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_Size_Dialog)
        #
        self.setupWindow()
    #
    def setArgs(self, string, args):
        self._managerUnit.setArgs(string, args)
    #
    def setListCache(self):
        self._managerUnit.setListCache()
    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
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


class IfScIndexManagerWindow(guiQtWidgets.QtDialogWindow):
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfScIndexManagerWindow, self).__init__(parent)

        self.setDefaultSize(960, 480)
        self.setIndexString(shmOutput.Scheme().version)
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
        self._unit.refreshMethod()
    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        self._unit = ifUnit.IfScIndexManagerUnit()
        self.addWidget(self._unit)
        #
        self.confirmClicked.connect(self._unit.confirmCmd)


class IfScRenderManagerWindow(guiQtWidgets.QtToolWindow):
    VAR_kit__qt_wgt__unit__side_width = 320
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfScRenderManagerWindow, self).__init__(parent)

        self.setNameString('Scene Render ( Image ) Manager')
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_SubSize_Default)
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
        sceneIndex, projectName, sceneCategory, sceneName, sceneVariant, sceneStage, startFrame, endFrame = args
        #
        self.projectName = projectName
        #
        self.sceneIndex = sceneIndex
        self.sceneCategory = sceneCategory
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
        sceneCategory = self.sceneCategory
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
            sceneCategory, sceneName, sceneVariant, sceneStage
        )
        #
        viewExplain = scenePr.getSceneViewInfo(
            sceneIndex, sceneCategory, '{} - {}'.format(sceneName, sceneVariant)
        )
        #
        sceneItem = qtWidgets_.QTreeWidgetItem_()
        treeBox.addItem(sceneItem)
        sceneItem.setText(0, viewExplain)
        sceneItem.setItemIcon_(0, 'svg_basic/package_object')
        #
        self._methodLis = treeViewCmds.setListScRenderImageCustomize(
            sceneItem,
            customizes,
            projectName,
            sceneCategory, sceneName, sceneVariant, sceneStage,
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
                sceneCategory = self.sceneCategory
                sceneName = self.sceneName
                sceneVariant = self.sceneVariant
                sceneStage = self.sceneStage
                #
                backupSourceFile = scenePr.sceneUnitSourceFile(
                    prsConfigure.Utility.DEF_value_root_backup,
                    projectName, sceneCategory, sceneName, sceneVariant, prsMethods.Scene.lightLinkName(),
                )[1]
                #
                backupProductFile = scenePr.scUnitRenderFile(
                    prsConfigure.Utility.DEF_value_root_backup,
                    projectName, sceneCategory, sceneName, sceneVariant, prsMethods.Scene.lightLinkName(),
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
            timer = qtCore.CLS_timer(self)
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
    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
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
        self._rightExpandBox.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        #
        self._rightScrollLayout = qtCore.QScrollArea_()
        self._rightExpandBox.addWidget(self._rightScrollLayout)


class IfRenderImageComposeWindow(guiQtWidgets.QtToolWindow):
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfRenderImageComposeWindow, self).__init__(parent)

        self.setNameString('Scene Render ( Image ) Manager')
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_SubSize_Default)
        #
        self.initializationPanel()
        #
        self.setupWindow()
    #
    def refreshMethod(self):
        self.setListTreeItem()
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
        # self._refreshButton.clicked.connect(self.setCentralRefresh)
    #
    def _kit__unit__set_central_build_(self, layout):
        def setTreeViewBox(treeBox):
            treeBox.setColumns(
                ['File', 'Time', 'Completion'],
                [4, 2, 2],
                800 - 20
            )
            #
            treeBox.setKeywordFilterWidgetConnect(self._filterEnterLabel)
        #
        splitterLayout = qtCore.QSplitter_()
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
            progressBar.update()
            #
            sceneIndex, sceneVariant = key
            #
            (
                description,
                sceneCategory, sceneName, scenePriority, scLayoutEnable,
                scAnimationEnable, scSolverEnable, scSimulationEnable, scLightEnable
            ) = value
            #
            sceneStage = prsMethods.Scene.lightLinkName()
            #
            startFrame, endFrame = scenePr.getScUnitFrameRange(
                projectName,
                sceneCategory, sceneName, sceneVariant
            )
            #
            customizes = scenePr.getScRenderCustomizes(
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage
            )
            sceneItem = qtWidgets_.QTreeWidgetItem_()
            treeBox.addItem(sceneItem)
            #
            sceneItem.setItemIcon(0, 'object/scene')
            sceneItemLis.append(sceneItem)
            #
            showExplain = scenePr.getSceneViewInfo(sceneIndex, sceneCategory, sceneName)
            sceneItem.setText(0, showExplain)
            #
            subMethods = treeViewCmds.setListScRenderImageCustomize(
                sceneItem,
                customizes,
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame
            )
            #
            self._methodLis.extend(subMethods)
        #
        self._methodLis = []
        #
        sceneItemLis = []
        #
        projectName = prsMethods.Project.mayaActiveName()
        #
        treeBox = self.treeViewBox
        inData = scenePr.getUiSceneSetDataDic(projectName)
        #
        treeBox.clear()
        if inData:
            explain = '''List Scene Render'''
            maxValue = len(inData)
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
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
            timer = qtCore.CLS_timer(self)
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
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for seq, i in enumerate(self._methodLis):
                progressBar.update()
                i()
                setBranch(seq, i)
    #
    def initializationPanel(self):
        self._timerLis = []
        self._methodLis = []
    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
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
        self._kit__unit__set_central_build_(centralLayout)


class IfRenderFileComposeWindow(guiQtWidgets.QtToolWindow):
    w = 80
    dicTool = bscMtdCore.orderedDict()
    dicTool['sourceDirectory'] = [w, 0, 0, 1, 4, 'Source']
    dicTool['targetDirectory'] = [w, 1, 0, 1, 4, 'Target']
    dicTool['collectionFile'] = [w, 2, 0, 1, 4, 'Collection']
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfRenderFileComposeWindow, self).__init__(parent)

        self.setNameString('Scene Render ( Compose ) Manager')
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_SubSize_Default)
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
                        if bscMethods.OsFile.isExist(serverRenderFile):
                            from LxMaBasic import maBscMethods
                            maBscMethods.File.openFrom(serverRenderFile)
                    #
                    def openRenderFolder():
                        bscMethods.OsDirectory.open(renderFolder)
                    #
                    renderFolder = scenePr.scUnitRenderFolder(
                        prsConfigure.Utility.DEF_value_root_server,
                        projectName,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        customize
                    )
                    #
                    actions = [
                        ('Open Render File', 'menu/maFile', True, openRenderFile),
                        (),
                        ('Open Render Folder', 'svg_basic/folder', True, openRenderFolder)
                    ]
                    itemWidget.setActionData(actions)
                #
                serverRenderFile = scenePr.scUnitRenderFile(
                    prsConfigure.Utility.DEF_value_root_server,
                    projectName, sceneCategory, sceneName, sceneVariant, sceneStage, customize
                )[1]
                #
                customizeItem = qtWidgets_.QTreeWidgetItem_()
                sceneItem.addChild(customizeItem)
                #
                itemWidget = customizeItem.setItemIconWidget(0, 'object/mayaFile', customize)
                setActionData()
                showTimeTag = bscMethods.OsFile.mtimeChnPrettify(serverRenderFile)
                #
                customizeItem.setText(1, showTimeTag)
                #
                composeFiles = scenePr.getScRenderCompose(
                    projectName,
                    sceneCategory, sceneName, sceneVariant, sceneStage,
                    customize
                )
                #
                customizeItem.compose = composeFiles or []
                customizeItem.showExplain = u'{1}@{0}'.format(showExplain, customize)
            #
            progressBar.update()
            #
            sceneIndex, sceneVariant = key
            #
            description, sceneCategory, sceneName = value[:3]
            #
            sceneStage = prsMethods.Scene.lightLinkName()
            #
            sceneItem = qtWidgets_.QTreeWidgetItem_()
            projectItem.addChild(sceneItem)
            #
            customizes = scenePr.getScRenderCustomizes(
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage
            )
            #
            sceneItem.setItemIcon(0, 'object/scene', ['off', none][customizes != []])
            #
            showExplain = scenePr.getSceneViewInfo(sceneIndex, sceneCategory, sceneName)
            sceneItem.setText(0, showExplain)
            #
            sceneItem.setExpanded(True)
            [setCustomizeBranch(i) for i in customizes]
        #
        self._methodLis = []
        #
        projectName = prsMethods.Project.mayaActiveName()
        #
        treeBox = self.leftTreeViewBox
        inData = scenePr.getUiSceneSetDataDic(projectName)
        #
        treeBox.clear()
        #
        projectItem = qtWidgets_.QTreeWidgetItem_()
        projectItem.setItemIcon(0, 'svg_basic/project')
        treeBox.addItem(projectItem)
        #
        projectShowExplain = prsMethods.Project.showinfo(projectName)
        projectItem.setText(0, projectShowExplain)
        #
        projectItem.setExpanded(True)
        #
        if inData:
            progressExplain = '''List Scene Render'''
            maxValue = len(inData)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            [setSceneBranch(k, v) for k, v in inData.items()]
    #
    def setListRightTreeItem(self):
        def setBranch(index, fileString_):
            def getTargetFile(sourceFileString):
                return targetPath + sourceFileString[len(sourcePath):]
            #
            ext = bscMethods.OsFile.ext(fileString_)
            #
            self.setProgressValue(index + 1, maxValue)
            #
            treeItem = qtWidgets_.QTreeWidgetItem_()
            treeBox.addItem(treeItem)
            state = none
            if not bscMethods.OsFile.isExist(fileString_):
                state = 'off'
            else:
                if not fileString_.startswith(sourcePath):
                    state = 'error'
            #
            treeItem.setItemIcon(0, 'treeBox/file', state)
            treeItem.setText(0, fileString_)
            #
            targetFile = getTargetFile(fileString_)
            if not bscMethods.OsFile.isExist(targetFile):
                subExplain = 'Target is Non - Exists'
                subState = 'error'
                #
                self._needCollectionFileArray.append((fileString_, targetFile))
                #
                self._fileConstantStatisticsDic.setdefault('Non - Exists', []).append(fileString_)
            else:
                isMtimeChanged = bscMethods.OsFile.isFileTimeChanged(fileString_, targetFile)
                if isMtimeChanged:
                    if ext == '.tx':
                        subExplain = 'Collection ( .tx )'
                        subState = none
                    else:
                        subExplain = 'Source is Time - Changed'
                        subState = 'warning'
                        #
                        self._needCollectionFileArray.append((fileString_, targetFile))
                        #
                        self._fileConstantStatisticsDic.setdefault('Time - Changed', []).append(fileString_)
                else:
                    subExplain = 'Collection'
                    subState = 'on'
                    #
                    self._fileConstantStatisticsDic.setdefault('Collection', []).append(fileString_)
            #
            treeItem.setItemIcon(1, 'treeBox/check', subState)
            treeItem.setText(1, subExplain)
            #
            showExplains = showExplainDic[fileString_]
            treeItem.setToolTip(0, ','.join(showExplains))
            #
            treeItem.setText(2, str(len(showExplains)))
            #
            self._fileTypeCountStatisticsDic.setdefault(ext, []).append(fileString_)
            #
            fileSize = bscMethods.OsFile.size(fileString_)
            #
            self._fileTypeSizeStatisticsDic.setdefault(ext, []).append(fileSize)
            #
            self._fileSizes.append(fileSize)
            #
            self._files.append((fileString_, targetFile))
        #
        def getProxyCompose(fileString_, lis, _showExplain):
            if fileString_.endswith('_prx.ass'):
                filePath = bscMethods.OsFile.dirname(fileString_)
                texturePath = filePath + '/' + 'texture'
                textures = bscMethods.OsDirectory.fileFullpathnames(texturePath)
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
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for i in customizeItems:
                progressBar.update()
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
        @dtbMtdCore.fncThreadSemaphoreModifier
        def copyFileThreadMethod(sourceFile, targetFile):
            bscMethods.OsFile.copyTo(sourceFile, targetFile)
        #
        collectionDataArray = self._needCollectionFileArray
        if collectionDataArray:
            copyThreads = []
            #
            for i, j in collectionDataArray:
                t = guiCore.UiThread(copyFileThreadMethod, i, j)
                copyThreads.append(t)
                t.start()
            # View Progress
            progressExplain = u'''Collection File(s)'''
            maxValue = len(copyThreads)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            if copyThreads:
                for i in copyThreads:
                    progressBar.update()
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
                r, g, b = qtCore.hsv2rgb(dv * seq, 1, 1)
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
                r, g, b = qtCore.hsv2rgb(dv * seq, 1, 1)
                lis.append(
                    (
                        '{0} ( {1} / {2} )'.format(
                            k,
                            bscMethods.Value.toFileSizePrettify(count),
                            bscMethods.Value.toFileSizePrettify(maxCount)
                        ),
                        count, (r, g, b, 255)
                    )
                )
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

    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
    def windowShow(self):
        self.uiShow()
    #
    def setupWindow(self):
        def setupTopToolBar(layout):
            self._filterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
            layout.addWidget(self._filterButton)
            #
            self._filterEnterLabel = guiQtWidgets.QtFilterLine()
            layout.addWidget(self._filterEnterLabel)
            #
            self._refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
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
            treeBox.setKeywordFilterWidgetConnect(self._filterEnterLabel)
        #
        def setupBottomToolBox(toolBox):
            inData = self.dicTool
            self._sourceDirectoryLabel = guiQtWidgets.QtValueLine()
            toolBox.setInfo(inData, 'sourceDirectory', self._sourceDirectoryLabel)
            self._sourceDirectoryLabel.setDatum('l:')
            #
            self._targetDirectoryLabel = guiQtWidgets.QtValueLine()
            toolBox.setInfo(inData, 'targetDirectory', self._targetDirectoryLabel)
            self._targetDirectoryLabel.setDatum('l:/forRender_L/forRender_L')
            #
            self.collectionFileButton = guiQtWidgets.QtPressbutton()
            toolBox.setButton(inData, 'collectionFile', self.collectionFileButton)
            self.collectionFileButton.setPercentEnable(True)
            self.collectionFileButton.clicked.connect(self.setCollection)
            #
            toolBox.setSeparators(inData)
        #
        def setupStatisticsBox(scrollBox):
            self.fileTypeCountPieChart = qtChart_.QtPiechart_()
            self.fileTypeCountPieChart.setNameString('Count')
            scrollBox.addWidget(self.fileTypeCountPieChart)
            self.fileTypeCountPieChart.setUiSize(sideWidth-40, sideWidth-40)
            #
            self.fileTypeSizePieChart = qtChart_.QtPiechart_()
            self.fileTypeSizePieChart.setNameString('Size')
            scrollBox.addWidget(self.fileTypeSizePieChart)
            self.fileTypeSizePieChart.setUiSize(sideWidth-40, sideWidth-40)
            #
            self.fileConstantPieChart = qtChart_.QtPiechart_()
            self.fileConstantPieChart.setNameString('Constant')
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
        splitterLayout = qtCore.QSplitter_()
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
        bottomToolBox = guiQtWidgets.QtToolbox()
        mainLayout.addWidget(bottomToolBox)
        bottomToolBox.setTitle('Modify')
        setupBottomToolBox(bottomToolBox)


class IfArnoldStandaloneRenderWindow(guiQtWidgets.QtToolWindow):
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfArnoldStandaloneRenderWindow, self).__init__(parent)

        self.setNameString('Arnold Render ( standalone )')
        #
        self.setDefaultSize(*guiCore.Lynxi_Ui_Window_SubSize_Default)

    @qtModifiers.gui_qt__mdf__set_gui_exclusive_show
    def windowShow(self):
        self.uiShow()
