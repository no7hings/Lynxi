# coding=utf-8
from LxBasic import bscMethods

from LxDatabase import dtbConfigure, dtbMethods

from LxGui.qt import guiQtWidgets, qtCore, qtMethod

from .. import kitQtWgtAbs


#
class ifDevelopOverviewUnit(kitQtWgtAbs.IfOverviewUnitBasic):
    ui_method = qtMethod.QtViewMethod
    #
    dbClass = 'develop'
    dbUnitType = dtbConfigure.DtbBasic.LxDb_Type_Unit_Python
    dbUnitBranch = 'main'
    def __init__(self, parent=qtCore.getAppWindow()):
        super(ifDevelopOverviewUnit, self).__init__(parent)
        self._initOverviewUnitBasic()
    #
    def refreshMethod(self):
        if self.connectObject():
            self.setLeftRefresh()
    #
    def _kit__unit__set_left_build_(self, layout):
        toolGroup = guiQtWidgets.QtToolboxGroup()
        layout.addWidget(toolGroup)
        toolGroup.setTitle('Python(s)')
        toolGroup.setExpanded(True)
        self._leftTreeView = guiQtWidgets.QtTreeview()
        toolGroup.addWidget(self._leftTreeView)
        self._leftTreeView.currentChanged.connect(self.setCentralRefresh)
        #
        toolGroup = guiQtWidgets.QtToolboxGroup()
        layout.addWidget(toolGroup)
        toolGroup.setTitle('Note(s)')
        toolGroup.setExpanded(True)
        self._noteEnterBox = guiQtWidgets.QtTextbrower()
        toolGroup.addWidget(self._noteEnterBox)
        self._noteEnterBox.setNameString('Note(s)')
        #
        self._backupButton = guiQtWidgets.QtPressbutton()
        toolGroup.addWidget(self._backupButton)
        self._backupButton.setPercentEnable(True)
        self._backupButton.setNameString('Backup')
        self._backupButton.setIcon('svg_basic/backup')
        self._backupButton.clicked.connect(self._backupCmd)
    #
    def _kit__unit__set_central_build_(self, layout):
        self._centralTopTooGroup = guiQtWidgets.QtToolboxGroup()
        layout.addWidget(self._centralTopTooGroup)
        self._centralTopTooGroup.setTitle('File(s)')
        self._centralTopTooGroup.setExpanded(True)
        #
        self._centralTreeView = guiQtWidgets.QtTreeview()
        self._centralTopTooGroup.addWidget(self._centralTreeView)
        self._centralTreeView.setColorEnable(True)
        self._centralTreeView.setKeywordFilterWidgetConnect(self._filterEnterLabel)
        self._centralTreeView.currentChanged.connect(self.setDatumRefresh)
        #
        self._centralBottomTooGroup = guiQtWidgets.QtToolboxGroup()
        layout.addWidget(self._centralBottomTooGroup)
        self._centralBottomTooGroup.setTitle('Datum')
        #
        self._datumEnterBox = guiQtWidgets.QtTextbrower()
        self._centralBottomTooGroup.addWidget(self._datumEnterBox)
        self.highlighter = qtCore.xPythonHighlighter(self._datumEnterBox.textEdit().document())
    #
    def setupRightWidget(self, layout):
        pass
    #
    def setLeftRefresh(self):
        treeView = self._leftTreeView
        #
        datumDic = dtbMethods.DtbUnit.dbGetOsUnitIncludeFileDic(
            self.dbClass,
            self.dbUnitType, self.dbUnitBranch
        )
        if datumDic:
            treeView.cleanItems()
            #
            for dbUnitSource, (dbDatumIndexUiDic, currentIndex) in datumDic.items():
                branchItem = guiQtWidgets.QtTreeItem()
                treeView.addItem(branchItem)
                branchItem.setNameString(dbUnitSource)
                branchItem.setIcon('svg_basic/branch_main')
                #
                branchItem.dbUnitSource = dbUnitSource
                branchItem.dbDatumIndex = dbDatumIndexUiDic[currentIndex][0]
                for seq, (dbDatumIndex, versionText) in dbDatumIndexUiDic.items():
                    versionItem = guiQtWidgets.QtTreeItem()
                    branchItem.addChild(versionItem)
                    versionItem.setNameString(versionText)
                    versionItem.setIcon('svg_basic/tag')
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
                    osCmdExe = 'sublime_text.exe'

                    tempOsFile = '{}/{}/{}/{}'.format(bscMethods.OsFile.DEF_path_temporary_local, dbDatumType, dbDatumId, osRelativeFile)
                    if not bscMethods.OsFile.isExist(tempOsFile):
                        bscMethods.OsFile.copyTo(dbDatumFile, tempOsFile)
                    #
                    osCmd = '''"{}" "{}"'''.format(osCmdExe, tempOsFile)
                    bscMethods.OsPlatform.runCommand(osCmd)
                #
                actionDatumLis = [
                    ('Basic', ),
                    ('Open Database File', 'svg_basic/fileOpen', True, openDatumFileCmd)
                ]
                treeItem.setActionData(actionDatumLis)
            #
            dbDatumType, dbDatumId, osRelativeFile = eval(value)
            treeItem = guiQtWidgets.QtTreeItem()
            treeView.addItem(treeItem)
            treeItem.setNameString(osRelativeFile)
            treeItem.setIcon('svg_basic/{}'.format(dbDatumType))
            ext = bscMethods.OsFile.ext(osRelativeFile)
            #
            osSourceFile = bscMethods.OsFile.composeBy(sourcePath, osRelativeFile)
            if bscMethods.OsFile.isExist(osSourceFile):

                sourceDatumId = bscMethods.OsFile.raw2hash(osSourceFile)
                if not sourceDatumId == dbDatumId:
                    treeItem.setFilterColor((255, 255, 64, 255))
                    self._changedCount += 1
            else:
                treeItem._setQtPressStatus(qtCore.OffStatus)
            #
            dbDatumFile = dtbMethods.DtbData.osUnitDatumFile(self.dbClass, dbDatumType, dbDatumId, ext)
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
                dbUnitIncludeFileLis = dtbMethods.DtbData._lxDbLoadJsonDatumFileSub(
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

                datum = bscMethods.OsFile.read(dbDatumFile)
                self._datumEnterBox.setDatum(datum)
    #
    def _updateBackupButtonState(self):
        self._backupButton.setPercent(self._maxCount, self._maxCount - self._changedCount)
    #
    def _backupCmd(self):
        pythonPathLis = ['e:/myworkspace/td/lynxi/source/python', 'e:/myworkspace/td/lynxi/tool/maya']
        for pythonPath in pythonPathLis:
            dbClass = 'develop'
            dbUnitType = dtbConfigure.DtbBasic.LxDb_Type_Unit_Python
            dbUnitBranch = 'main'
            note = self._noteEnterBox.datum()
            dtbMethods.DtbUnit.dbUpdateOsUnit(
                pythonPath, '.py', dbClass, dbUnitType, dbUnitBranch, note
            )
            self.setLeftRefresh()
    #
    def _kit__unit__set_build_Action(self):
        def loadCmd():
            pass
        #
        tabIndex = self.connectObject().tabIndex(self)
        tab = self.connectObject().tabAt(tabIndex)
        tab.setActionData(
            [
                ('Basic',),
                ('Refresh', 'svg_basic/refresh', True, self.setCentralRefresh),
                ('Backup', 'svg_basic/backup', True, self._backupCmd),
                ('Extend',),
                ('Load to', 'svg_basic/load_action', True, loadCmd),
                ('About',),
                ('Help', 'svg_basic/help', True)
            ]
        )
    #
    def _kit__unit__set_build_Widgets(self):
        self._kit__unit__set_left_build_(self._leftScrollLayout)
        self._kit__unit__set_central_build_(self._centralScrollLayout)
        self.setupRightWidget(self._rightScrollLayout)
