# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
from LxCore.method import _dbMethod
#
from LxUi.qt import qtWidgets, qtCore, qtMethod
#
from LxInterface.qt.ifBasic import ifWidgetBasic
#
serverBasicPath = lxConfigure.Root()._serverDirectory()


#
class ifDevelopOverviewUnit(ifWidgetBasic.IfOverviewUnitBasic):
    _dbMethod = _dbMethod.DbOsUnitMethod
    _uiMethod = qtMethod.QtViewMethod
    #
    dbClass = 'develop'
    dbUnitType = _dbMethod.LxDb_Type_Unit_Python
    dbUnitBranch = 'main'
    def __init__(self, parent=qtCore.getAppWindow()):
        super(ifDevelopOverviewUnit, self).__init__(parent)
        self._initOverviewUnitBasic()
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setLeftRefresh()
    #
    def setupLeftWidget(self, layout):
        toolGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(toolGroup)
        toolGroup.setTitle('Python(s)')
        toolGroup.setExpanded(True)
        self._leftTreeView = qtWidgets.QtTreeview()
        toolGroup.addWidget(self._leftTreeView)
        self._leftTreeView.currentChanged.connect(self.setCentralRefresh)
        #
        toolGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(toolGroup)
        toolGroup.setTitle('Note(s)')
        toolGroup.setExpanded(True)
        self._noteEnterBox = qtWidgets.QtTextBrower()
        toolGroup.addWidget(self._noteEnterBox)
        self._noteEnterBox.setNameText('Note(s)')
        #
        self._backupButton = qtWidgets.QtPressbutton()
        toolGroup.addWidget(self._backupButton)
        self._backupButton.setPercentEnable(True)
        self._backupButton.setNameText('Backup')
        self._backupButton.setIcon('svg_basic@svg#backup')
        self._backupButton.clicked.connect(self._backupCmd)
    #
    def setupCentralWidget(self, layout):
        self._centralTopTooGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(self._centralTopTooGroup)
        self._centralTopTooGroup.setTitle('File(s)')
        self._centralTopTooGroup.setExpanded(True)
        #
        self._centralTreeView = qtWidgets.QtTreeview()
        self._centralTopTooGroup.addWidget(self._centralTreeView)
        self._centralTreeView.setColorEnable(True)
        self._centralTreeView.setFilterConnect(self._filterEnterLabel)
        self._centralTreeView.currentChanged.connect(self.setDatumRefresh)
        #
        self._centralBottomTooGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(self._centralBottomTooGroup)
        self._centralBottomTooGroup.setTitle('Datum')
        #
        self._datumEnterBox = qtWidgets.QtTextBrower()
        self._centralBottomTooGroup.addWidget(self._datumEnterBox)
        self.highlighter = qtCore.xPythonHighlighter(self._datumEnterBox.textEdit().document())
    #
    def setupRightWidget(self, layout):
        pass
    #
    def setLeftRefresh(self):
        treeView = self._leftTreeView
        #
        datumDic = self._dbMethod.dbGetOsUnitIncludeFileDic(
            self.dbClass,
            self.dbUnitType, self.dbUnitBranch
        )
        if datumDic:
            treeView.cleanItems()
            #
            for dbUnitSource, (dbDatumIndexUiDic, currentIndex) in datumDic.items():
                branchItem = qtWidgets.QtTreeviewItem()
                treeView.addItem(branchItem)
                branchItem.setNameText(dbUnitSource)
                branchItem.setIcon('svg_basic@svg#branch_main')
                #
                branchItem.dbUnitSource = dbUnitSource
                branchItem.dbDatumIndex = dbDatumIndexUiDic[currentIndex][0]
                for seq, (dbDatumIndex, versionText) in dbDatumIndexUiDic.items():
                    versionItem = qtWidgets.QtTreeviewItem()
                    branchItem.addChild(versionItem)
                    versionItem.setNameText(versionText)
                    versionItem.setIcon('svg_basic@svg#tag')
                    #
                    versionItem.dbDatumIndex = dbDatumIndex
                    versionItem.dbUnitSource = dbUnitSource
            #
            treeView.setRefresh()
    #
    def _fileRefreshMethod(self, sourcePath, datumLis):
        def setBranch(value):
            def setBranchActions():
                def openDatumFileCmd():
                    osCmdExe = '{}/Sublime Text 3/sublime_text.exe'.format(lxConfigure.BinSubRoot()._serverDirectory())
                    if lxBasic.isOsExistsFile(osCmdExe):
                        tempOsFile = '{}/{}/{}/{}'.format(self._dbMethod.LynxiOsPath_LocalTemporary, dbDatumType, dbDatumId, osRelativeFile)
                        if not self._dbMethod.isOsExistsFile(tempOsFile):
                            self._dbMethod.setOsFileCopy(dbDatumFile, tempOsFile)
                        #
                        osCmd = '''"{}" "{}"'''.format(osCmdExe, tempOsFile)
                        lxBasic.setOsCommandRun_(osCmd)
                #
                actionDatumLis = [
                    ('Basic', ),
                    ('Open Database File', 'svg_basic@svg#fileOpen', True, openDatumFileCmd)
                ]
                treeItem.setActionData(actionDatumLis)
            #
            dbDatumType, dbDatumId, osRelativeFile = eval(value)
            treeItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(treeItem)
            treeItem.setNameText(osRelativeFile)
            treeItem.setIcon('svg_basic@svg#{}'.format(dbDatumType))
            ext = self._dbMethod.getOsFileExt(osRelativeFile)
            #
            osSourceFile = self._dbMethod._toOsFile(sourcePath, osRelativeFile)
            if self._dbMethod.isOsExistsFile(osSourceFile):
                sourceDatumId = self._dbMethod.getOsFileHashString(osSourceFile)
                if not sourceDatumId == dbDatumId:
                    treeItem.setFilterColor((255, 255, 64, 255))
                    self._changedCount += 1
            else:
                treeItem._setQtPressStatus(qtCore.OffStatus)
            #
            dbDatumFile = self._dbMethod._lxDbOsUnitDatumFile(
                    self.dbClass,
                    dbDatumType, dbDatumId, ext
                )
            treeItem.dbDatumFile = dbDatumFile
            #
            setBranchActions()
        #
        def setMain():
            treeView.cleanItems()
            if datumLis:
                maxCount = len(datumLis)
                self.connectObject().mainWindow().setMaxProgressValue(maxCount)
                for i in datumLis:
                    self.connectObject().mainWindow().updateProgress()
                    #
                    setBranch(i)
                #
                self._maxCount = maxCount
            #
            treeView.setRefresh()
        #
        self._maxCount = 0
        self._changedCount = 0
        #
        treeView = self._centralTreeView
        #
        setMain()
    #
    def setCentralRefresh(self):
        currentItem = self._leftTreeView.currentItem()
        if currentItem:
            if hasattr(currentItem, 'dbDatumIndex'):
                dbUnitSource = currentItem.dbUnitSource
                dbDatumIndex = currentItem.dbDatumIndex
                dbDatumType, dbDatumId = eval(dbDatumIndex)
                dbUnitIncludeFileLis = self._dbMethod._lxDbLoadJsonDatumFileSub(
                    self.dbClass,
                    dbDatumType, dbDatumId
                )
                self._fileRefreshMethod(dbUnitSource, dbUnitIncludeFileLis)
            #
            self._updateBackupButtonState()
    #
    def setDatumRefresh(self):
        currentItem = self._centralTreeView.currentItem()
        if currentItem:
            if hasattr(currentItem, 'dbDatumFile'):
                dbDatumFile = currentItem.dbDatumFile
                datum = self._dbMethod.readOsData(dbDatumFile)
                self._datumEnterBox.setDatum(datum)
    #
    def _updateBackupButtonState(self):
        self._backupButton.setPercent(self._maxCount, self._maxCount - self._changedCount)
    #
    def _backupCmd(self):
        pythonPathLis = ['e:/myworkspace/td/lynxi/source/python', 'e:/myworkspace/td/lynxi/tool/maya']
        for pythonPath in pythonPathLis:
            dbClass = 'develop'
            dbUnitType = self._dbMethod.LxDb_Type_Unit_Python
            dbUnitBranch = 'main'
            note = self._noteEnterBox.datum()
            self._dbMethod.dbUpdateOsUnit(
                pythonPath, '.py', dbClass, dbUnitType, dbUnitBranch, note
            )
            self.setLeftRefresh()
    #
    def setupUnitAction(self):
        def loadCmd():
            pass
        #
        tabIndex = self.connectObject().tabIndex(self)
        tab = self.connectObject().tabAt(tabIndex)
        tab.setActionData(
            [
                ('Basic',),
                ('Refresh', 'svg_basic@svg#refresh', True, self.setCentralRefresh),
                ('Backup', 'svg_basic@svg#backup', True, self._backupCmd),
                ('Extend',),
                ('Load to', 'svg_basic@svg#load_action', True, loadCmd),
                ('About',),
                ('Help', 'svg_basic@svg#help', True)
            ]
        )
    #
    def setupUnitWidgets(self):
        self.setupLeftWidget(self._leftScrollLayout)
        self.setupCentralWidget(self._centralScrollLayout)
        self.setupRightWidget(self._rightScrollLayout)
