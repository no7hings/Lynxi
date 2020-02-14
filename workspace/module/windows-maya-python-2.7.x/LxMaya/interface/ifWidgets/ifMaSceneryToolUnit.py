# coding=utf-8
import threading
#
from LxBasic import bscCore, bscMethods, bscObjects

from LxPreset import prsMethods, prsVariants
#
from LxCore import lxConfigure
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr, sceneryPr
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore
#
from LxInterface.qt.qtIfBasic import _qtIfAbcWidget
#
from LxDatabase import dbGet
#
from LxMaya.command import maUtils, maFile, maHier, maRender
#
from LxMaya.product import maAstLoadCmds, maAstUploadCmds, maScnUploadCmds
# Project Data
currentProjectName = prsMethods.Project.mayaActiveName()
#
none = ''


# Assembly Loaded
class IfScnAssemblyLoadedUnit(_qtIfAbcWidget.QtIfAbc_Unit_):
    UnitTitle = 'Assembly Load Unit'
    UnitIcon = 'window#sceneryToolPanel'
    UnitTooltip = u'''组装加载工具'''
    SideWidth = 320
    #
    panelWidth = 800
    panelHeight = 800
    #
    widthSet = 800
    #
    projectName = currentProjectName
    def __init__(self, *args, **kwargs):
        super(IfScnAssemblyLoadedUnit, self).__init__(*args, **kwargs)
        self._initIfAbcUnit()
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        self.setupConnection()
        #
        self.setCentralRefresh()
    #
    def delScriptJob(self):
        pass
    #
    def setupConnection(self):
        self.refreshButton().clicked.connect(self.setCentralRefresh)
    #
    def setupLeftWidget(self, layout):
        pass
    #
    def setupCentralWidget(self, layout):
        def setActions():
            def assembliesLoadEnable():
                return self._gridView.checkedItems() != []
            #
            def assembliesLoadCmds():
                projectName = self.projectName
                #
                gridView = self._gridView
                #
                checkedItems = gridView.checkedItems()
                if checkedItems:
                    for gridItem in checkedItems:
                        assetIndex = gridItem.assetIndex
                        assetCategory = None
                        assetName = gridItem.assetName
                        assetVariant = gridItem.assetVariant
                        #
                        # noinspection PyArgumentEqualDefault
                        maAstLoadCmds.astUnitAssemblyLoadForScenery(
                            assetIndex,
                            projectName,
                            assetCategory, assetName, assetVariant,
                            isWithAnnotation=False, isWithHandle=True
                        )
            #
            actionData = [
                ('Extend Action(s)', ),
                ('Load Assembly(s)', ('svg_basic@svg#file', 'svg_basic@svg#load_action'), assembliesLoadEnable, assembliesLoadCmds)
            ]
            self._gridView.setActionData(actionData)
        #
        width, height = 240, 240
        #
        self._gridView = qtWidgets.QtGridview()
        self._gridView.setCheckEnable(True)
        self._gridView.setItemSize(240, 240 + 40)
        layout.addWidget(self._gridView)
        self._gridView.setFilterConnect(self.filterEnterLabel())
        #
        self._gridView.setItemListModeSize(width, 20)
        self._gridView.setItemIconModeSize(width, height + 20)
        #
        setActions()
    #
    def setCentralRefresh(self):
        def setBranch(seq, key, value):
            def setSubActions():
                def assemblyLoadCmd():
                    # noinspection PyArgumentEqualDefault
                    maAstLoadCmds.astUnitAssemblyLoadForScenery(
                        assetIndex,
                        projectName,
                        assetCategory, assetName, assetVariant,
                        isWithAnnotation=False, isWithHandle=True
                    )
                #
                def assemblyFolderOpenCmd():
                    osPath = assetPr.astUnitAssemblyFolder(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName, assetCategory, assetName
                    )
                    if bscMethods.OsFile.isExist(osPath):
                        bscMethods.OsDirectory.open(osPath)
                #
                subActionData = [
                    ('Basic', ),
                    ('Load Current Assembly', ('svg_basic@svg#file', 'svg_basic@svg#load_action'), True, assemblyLoadCmd),
                    ('Extend', ),
                    ('Open Current Assembly Folder', 'svg_basic@svg#folder', True, assemblyFolderOpenCmd)
                ]
                gridItem.setActionData(subActionData, title=viewExplain)
            #
            def getBuildData(data):
                for keyword, fileString_ in data:
                    mtimestamp = bscMethods.OsFile.mtimestamp(fileString_)
                    exists = mtimestamp is not None
                    rgba = [(255, 255, 64, 255), (63, 255, 127, 255)][exists]
                    iconKeyword = [None, 'svg_basic@svg#time'][exists]
                    messageLis.append((messageWidget.DrawColor, (rgba, iconKeyword, bscMethods.OsTimestamp.toChnPrettify(mtimestamp))))
            #
            assetIndex = key
            assetCategory = assetPr.getAssetClass(assetIndex)
            assetName, viewName = value
            assetVariant = prsVariants.Util.astDefaultVariant
            # Tag
            if ' - ' in viewName:
                tag, _ = viewName.split(' - ')[:2]
            else:
                tag = 'Others'
            #
            if not tag in self._tagLis:
                self._tagLis.append(tag)
            if not tag in self._tagFilterEnableDic:
                self._tagFilterEnableDic[tag] = True
            #
            self._tagFilterIndexDic.setdefault(tag, []).append(seq)
            #
            gridItem = qtWidgets.QtGridviewItem()
            gridView.addItem(gridItem)
            viewExplain = assetPr.getAssetViewInfo(assetIndex, assetCategory, '{} - {}'.format(assetName, assetVariant))
            gridItem.setNameText(viewExplain)
            gridItem.setIcon('svg_basic@svg#assembly_object')
            r, g, b = qtCore.str2rgb(assetName)
            gridItem.setFilterColor((r, g, b, 255))
            #
            preview = dbGet.getDbAstPreviewFile(assetIndex, assetVariant)
            #
            messageWidget = qtWidgets.QtMessageWidget()
            messageWidget.setExplainWidth(20)
            gridItem.addWidget(messageWidget, 0, 0, 1, 1)
            #
            productFile = assetPr.astUnitAssemblyProductFile(projectName, assetName, assetVariant)[1]
            #
            messageLis = [
                (messageWidget.DrawImage1, preview)
            ]
            getBuildData(
                [
                    ('product', productFile)
                ]
            )
            messageWidget.setDatumLis(messageLis, 240, 240)
            #
            gridItem.assetIndex = assetIndex
            gridItem.assetCategory = None
            gridItem.assetName = assetName
            gridItem.assetVariant = assetVariant
            #
            definitionFile = assetPr.astUnitAssemblyDefinitionFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                assetCategory, assetName, assetVariant, lxConfigure.VAR_product_asset_link_assembly
            )[1]
            #
            if not bscMethods.OsFile.isExist(definitionFile):
                gridItem.setPressable(False)
                gridItem.setCheckable(False)
            else:
                setSubActions()
        #
        projectName = self.projectName
        #
        gridView = self._gridView
        # noinspection PyArgumentEqualDefault
        uiData = assetPr.getUiAssetMultMsgDic(
            projectName,
            assetClassFilters=None,
            assetLinkFilter=lxConfigure.VAR_product_asset_link_assembly
        )
        #
        gridView.cleanItems()
        if uiData:
            # View Progress
            explain = '''Build Assembly Unit(s)'''
            maxValue = len(uiData)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for s, (k, v) in enumerate(uiData.items()):
                progressBar.update()
                setBranch(s, k, v)
        #
        gridView.setRefresh()
        gridView.setSortByName()
        #
        self._initTagFilterAction(gridView)
    #
    def setupUnit(self):
        self.topToolBar().show()
        #
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(leftExpandWidget)
        leftExpandWidget.setUiWidth(self.SideWidth)
        leftExpandWidget.setExpanded(False)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self.setupLeftWidget(leftScrollArea)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        centralLayout = qtCore.QVBoxLayout_(widget)
        centralLayout.setContentsMargins(0, 0, 0, 0)
        centralLayout.setSpacing(0)
        self.setupCentralWidget(centralLayout)


#
class IfScnAssemblyManagerUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitTitle = 'Assembly Manager'
    UnitIcon = 'window#sceneryToolPanel'
    UnitTooltip = u'''组装管理工具'''


#
class IfScnComposeManagerUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitTitle = 'Scenery Compose Manager'
    UnitIcon = 'window#sceneryToolPanel'
    UnitTooltip = u'''场景管理工具'''


# Scenery Tool
class IfScnLinkToolUnit(qtCore.QWidget_):
    UnitTitle = 'Scenery Tool Unit'
    UnitIcon = 'window#sceneryToolPanel'
    #
    projectName = currentProjectName
    #
    w = 80
    dicImport = bscCore.orderedDict()
    dicImport['episode'] = [w, 0, 0, 1, 4, 'Episode']
    dicImport['sequence'] = [w, 1, 0, 1, 4, 'Sequence']
    dicImport['shot'] = [w, 2, 0, 1, 4, 'Shot']
    # 3
    dicImport['loadSeqScn'] = [0, 4, 0, 1, 2, 'Load Sequence Scenery']
    dicImport['loadShotScn'] = [0, 4, 2, 1, 2, 'Load Shot Scenery']
    #
    dicTool = {
        'assemblyLoaded': [1, 0, 0, 1, 2, 'Assembly Loaded', 'svg_basic@svg#subWindow'],
        'assemblyManager': [1, 0, 2, 1, 2, 'Assembly Manager', 'svg_basic@svg#subWindow']
    }

    def __init__(self, *args, **kwargs):
        super(IfScnLinkToolUnit, self).__init__(*args, **kwargs)
        self._connectObject = None
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        pass
    #
    def setupModifyTab(self, layout):
        def setupUtilsToolUiBox(toolBox):
            inData = self.dicTool
            #
            self.assemblyLoadedButton = qtWidgets.QtPressbutton()
            toolBox.setButton(inData, 'assemblyLoaded', self.assemblyLoadedButton)
            self.assemblyLoadedButton.clicked.connect(self.setAssemblyLoadedShow)
            #
            self.assemblyManagerButton = qtWidgets.QtPressbutton()
            toolBox.setButton(inData, 'assemblyManager', self.assemblyManagerButton)
            self.assemblyManagerButton.clicked.connect(self.setOpenAssemblyManager)
            #
            toolBox.setSeparators(inData)
        #
        self._utilsToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._utilsToolUiBox)
        self._utilsToolUiBox.setTitle('Scenery Utilities')
        setupUtilsToolUiBox(self._utilsToolUiBox)
    @staticmethod
    def setAssemblyLoadedShow():
        IfToolWindow = qtWidgets.QtToolWindow()
        toolBox = IfScnAssemblyLoadedUnit()
        #
        IfToolWindow.addWidget(toolBox)
        toolBox.setConnectObject(IfToolWindow)
        IfToolWindow.setQuitConnect(toolBox.delScriptJob)
        #
        toolBox.refreshMethod()
        IfToolWindow.setDefaultSize(toolBox.widthSet, 800)
        IfToolWindow.setTitle(toolBox.UnitTitle)
        #
        IfToolWindow.uiShow()
    @staticmethod
    def setOpenAssemblyManager():
        from LxMaya.interface.ifWidgets import ifMaToolWindow
        w = ifMaToolWindow.IfAssemblyManagerWindow()
        w.windowShow()
    #
    def setupUnit(self):
        mainLayout = qtCore.QVBoxLayout_(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        #
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        mainLayout.addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Modify', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupModifyTab(layout)


#
class IfScnAssemblyInfoToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitTitle = 'Information Tool Unit'
    UnitIcon = 'window#infoToolPanel'
    UnitTooltip = u'''信息工具模块'''
    #
    AssemblyRadarChartConfig = ['Asset', 'Assembly', 'LOD00', 'LOD01', 'LOD02', 'Visible']
    AssemblySectorChartConfig = ['Asb - Path', 'Asb - Visible', 'Asb - LOD', 'Asb - Matrix']
    def __init__(self, *args, **kwargs):
        super(IfScnAssemblyInfoToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnit()
    #
    def refreshMethod(self):
        if self.connectObject():
            self._setAssemblyChartRefresh()
    #
    def setupAssemblyQtTab(self, layout):
        self._scnAssemblyRadarChart = qtWidgets.QtRadarchart()
        layout.addWidget(self._scnAssemblyRadarChart)
        #
        self._scnAssemblySectorChart = qtWidgets.QtSectorchart()
        layout.addWidget(self._scnAssemblySectorChart)
    #
    def setupLightQtTab(self, layout):
        pass
    #
    def _setAssemblyChartRefresh(self):
        self._scnAssemblyRadarChart.setChartDatum(self._getAssemblyRadarChartDatum())
    #
    def _getAssemblyRadarChartDatum(self):
        lis = []
        chartConfig = self.AssemblyRadarChartConfig
        #
        projectName = self.connectObject().projectName
        #
        sceneryIndex = self.connectObject().sceneryIndex
        sceneryCategory = self.connectObject().sceneryCategory
        sceneryName = self.connectObject().sceneryName
        sceneryVariant = self.connectObject().sceneryVariant
        sceneryStage = self.connectObject().sceneryStage
        #
        previewFile = sceneryPr.getScnUnitPreviewFile(
            projectName,
            sceneryCategory, sceneryName, sceneryVariant, sceneryStage
        )
        #
        self._scnAssemblyRadarChart.setImage(previewFile)
        self._scnAssemblyRadarChart.setImageSize(prsVariants.Util.rndrImageWidth, prsVariants.Util.rndrImageHeight)
        #
        serverDatumDic = {}
        localDatumDic = {}
        #
        if localDatumDic:
            for i in chartConfig:
                if i in serverDatumDic:
                    serverCount = len(serverDatumDic[i])
                else:
                    serverCount = 0
                if i in localDatumDic:
                    localCount = len(localDatumDic[i])
                else:
                    localCount = 0
                lis.append(
                    (i, serverCount, localCount)
                )
        else:
            lis = [
                (i, 0, 0) for i in chartConfig
            ]
        return lis
    #
    def _getAssemblySectorChartDatum(self):
        pass
    #
    def setupUnit(self):
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        self.mainLayout().addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        # Assembly
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Assembly', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupAssemblyQtTab(layout)
        # Light
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Light', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupLightQtTab(layout)


#
class IfScnUtilityToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitTitle = 'Utilities Tool Unit'
    UnitIcon = 'window#utilsToolPanel'
    UnitTooltip = u'''通用工具模块'''
    #
    projectName = currentProjectName
    #
    _groupCreateTip = u'''提示：请输入名字...'''
    #
    UnitScriptJobWindowName = 'scnGeneralToolScriptJobWindow'
    dicUtilsHier = {
        'autoRename': [1, 0, 0, 1, 2, 'Auto Rename'],
        'parentGroup': [0, 1, 0, 1, 3, ''], 'addObject': [1, 1, 3, 1, 1, 'Add Object', 'svg_basic@svg#addTab'],
        'childGroup': [0, 2, 0, 1, 3, ''], 'addGroup': [1, 2, 3, 1, 1, 'Add Group', 'svg_basic@svg#addTab'],
        # 3
        'groupName': [0, 4, 0, 1, 4, 'Group Name'],
        'tips': [0, 5, 0, 1, 4, 'Tip(s)']
    }
    #
    dicScnUtils = {
        'assemblyLoaded': [1, 0, 0, 1, 2, 'Assembly Loaded', 'svg_basic@svg#subWindow'], 'assemblyManager': [1, 0, 2, 1, 2, 'Assembly Manager', 'svg_basic@svg#subWindow'],
        # 1
        'astUnitClearScene': [1, 2, 0, 1, 4, 'Clean Maya Scene']
    }
    def __init__(self, *args, **kwargs):
        super(IfScnUtilityToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.filterTypes = ['assemblyReference']
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
        if self._connectObject:
            sceneryStage = self._connectObject.sceneryStage
            #
            self._rootGroup = sceneryPr.scnUnitRootGroupName(self.connectObject().sceneryName)
            self._linkGroup = sceneryPr.scnAssemblyGroupName(self.connectObject().sceneryName)
            #
            self.setupScnGraphToolUiBox(self._scnGraphToolUiBox)
            self.filterTypes = [appCfg.MaNodeType_AssemblyReference]
            #
            self.setupScnUtilToolBox(self._scnUtilTooUiBox)
            #
            if sceneryPr.isLightLinkName(sceneryStage):
                self._addObjectButton.setNameText('Add Light')
            #
            self.setScriptJob()
            self.connectObject().setQuitConnect(self.delScriptJob)
    #
    def refreshMethod(self):
        pass
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methodLis = self._scriptJobMethodLis
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methodLis)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupScnGraphToolUiBox(self, toolBox):
        def getParentGroupName():
            data = self._parentGroupLabel.datum()
            return data
        #
        def getChildGroupName():
            data = self._childGroupLabel.datum()
            return data
        #
        def setParentGroupName():
            objectPathLis = maUtils.getSelectedNodeLis()
            if objectPathLis:
                objectPath = objectPathLis[0]
                if not objectPath.endswith(self._rootGroup) and not objectPath.endswith(self._linkGroup) and objectPath.startswith(appCfg.Ma_Separator_Node + self._rootGroup):
                    if objectPath.endswith(prsVariants.Util.basicGroupLabel):
                        objectName = maUtils._toNodeName(objectPath)
                        self._parentGroupLabel.setDatum(objectName)
        #
        def setChildGroupName():
            var = self._groupKeywordEntryLabel.datum()
            if var:
                linkGroup = self._linkGroup
                existsGroups = maUtils.getGroupLisByRoot(linkGroup, 0)
                groupName = var
                #
                newGroup = sceneryPr.scnBasicGroupNameSet(unitName, '_' + groupName)
                if groupName:
                    if len(groupName) < lenLimit:
                        if newGroup not in existsGroups:
                            self._childGroupLabel.setDatum(newGroup)
                            self._groupNameTipsLabel.setDatum(u'提示：名字可以使用...')
                        else:
                            self._childGroupLabel.setEnterClear()
                            self._groupNameTipsLabel.setDatum(u'错误：名字已经存在于文件中...')
                    else:
                        self._childGroupLabel.setEnterClear()
                        self._groupNameTipsLabel.setDatum(u'错误：名字不能超过%s个字符...' % lenLimit)
                else:
                    self._childGroupLabel.setEnterClear()
                    self._groupNameTipsLabel.setDatum(self._groupCreateTip)
            else:
                self._childGroupLabel.setEnterClear()
                self._groupNameTipsLabel.setDatum(self._groupCreateTip)
        #
        def setAddGroup():
            parent = getParentGroupName()
            child = getChildGroupName()
            if parent and child:
                maHier.setCreateBranchGroup(parent, child)
                #
                self._childGroupLabel.setEnterClear()
                self._groupKeywordEntryLabel.setEnterClear()
                #
                self._groupNameTipsLabel.setDatum(self._groupCreateTip)
        #
        def setAddObject():
            parent = getParentGroupName()
            isAutoRename = self._autoRenameCheckbutton.isChecked()
            if parent:
                parentPath = maUtils._getNodePathString(parent)
                if maUtils.isAppExist(parentPath):
                    maHier.addHierarchyObject(
                        parentPath, unitName, self.filterTypes, autoRename=isAutoRename
                    )
        #
        def setAddGrpBtnState():
            parent = getParentGroupName()
            child = getChildGroupName()
            button = self._addGroupButton
            #
            button.setPressable([False, True][parent is not None and child is not None])
        #
        def setAddNodeBtnState():
            button = self._addObjectButton
            parent = getParentGroupName()
            objectPathLis = maUtils.getSelectedNodeLis()
            button.setPressable([False, True][parent is not None and objectPathLis != []])
        #
        inData = self.dicUtilsHier
        #
        unitName = self.connectObject().sceneryName
        #
        lenLimit = 12
        #
        self._autoRenameCheckbutton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'autoRename', self._autoRenameCheckbutton)
        #
        self._parentGroupLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'parentGroup', self._parentGroupLabel)
        #
        self._addObjectButton = qtWidgets.QtPressbutton()
        self._addObjectButton.setPressable(False)
        toolBox.setButton(inData, 'addObject', self._addObjectButton)
        self._addObjectButton.clicked.connect(setAddObject)
        #
        self._childGroupLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'childGroup', self._childGroupLabel)
        #
        self._addGroupButton = qtWidgets.QtPressbutton()
        self._addGroupButton.setPressable(False)
        toolBox.setButton(inData, 'addGroup', self._addGroupButton)
        self._addGroupButton.clicked.connect(setAddGroup)
        #
        self._groupKeywordEntryLabel = qtWidgets.QtEnterlabel()
        self._groupKeywordEntryLabel.setTextValidator(48)
        self._groupKeywordEntryLabel.setEnterEnable(True)
        self._groupKeywordEntryLabel.setEnterable(True)
        toolBox.setInfo(inData, 'groupName', self._groupKeywordEntryLabel)
        self._groupKeywordEntryLabel.entryChanged.connect(setChildGroupName)
        self._groupKeywordEntryLabel.entryChanged.connect(setAddGrpBtnState)
        #
        self._groupNameTipsLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'tips', self._groupNameTipsLabel)
        self._groupNameTipsLabel.setDatum(self._groupCreateTip)
        #
        toolBox.setSeparators(inData)
        #
        self._scriptJobMethodLis = [
            setParentGroupName,
            setAddGrpBtnState,
            setAddNodeBtnState
        ]
    #
    def setupScnUtilToolBox(self, toolBox):
        toolBox.setUiData(self.dicScnUtils)
        #
        self.assemblyLoadedButton = qtWidgets.QtPressbutton()
        toolBox.addButton('assemblyLoaded', self.assemblyLoadedButton)
        self.assemblyLoadedButton.clicked.connect(self._assemblyLoadWindowShowCmd)
        #
        self.assemblyManagerButton = qtWidgets.QtPressbutton()
        toolBox.addButton('assemblyManager', self.assemblyManagerButton)
        self.assemblyManagerButton.clicked.connect(self._assemblyManagerWindowShowCmd)
        #
        self.sceneClearButton = qtWidgets.QtPressbutton()
        toolBox.addButton('astUnitClearScene', self.sceneClearButton)
        self.sceneClearButton.clicked.connect(self.setCleanScene)
        #
        toolBox.addSeparators()
    @staticmethod
    def _assemblyLoadWindowShowCmd():
        win = qtWidgets.QtToolWindow()
        #
        unit = IfScnAssemblyLoadedUnit()
        #
        win.addWidget(unit)
        unit.setConnectObject(win)
        win.setQuitConnect(unit.delScriptJob)
        #
        unit.refreshMethod()
        win.setDefaultSize(unit.panelWidth, 800)
        win.setNameText(unit.UnitTitle)
        #
        win.uiShow()
    @staticmethod
    def _assemblyManagerWindowShowCmd():
        from LxMaya.interface.ifWidgets import ifMaToolWindow
        w = ifMaToolWindow.IfAssemblyManagerWindow()
        w.windowShow()
    @staticmethod
    def setCleanScene():
        maAstUploadCmds.astUnitSceneClearCmd()
        maUtils.setMessageWindowShow(
            u'Clean Maya Scene', u'Complete',
            position='topCenter', fade=1, dragKill=0
        )
    #
    def getParentGroupName(self):
        data = self.parentGroupLabel.datum()
        if data:
            sceneryName = data
            return sceneryName
    #
    def getChildGroupName(self):
        sceneryName = none
        data = self.childGroupLabel.datum()
        if data:
            sceneryName = data
        return sceneryName
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        self._scnGraphToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._scnGraphToolUiBox)
        self._scnGraphToolUiBox.setTitle('Assembly Graph')
        #
        self._scnUtilTooUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._scnUtilTooUiBox)
        self._scnUtilTooUiBox.setTitle('Assembly Utilities')


#
class IfScnUploadToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitTitle = 'Upload Tool Unit'
    UnitIcon = 'window#uploadToolPanel'
    UnitTooltip = u'''上传工具模块'''
    #
    projectName = currentProjectName
    #
    uploadTips = [
        u'提示：',
        u'1：确认所有场景集合整理进组',
        u'2：点击 Upload ！！！ 上传...'
    ]
    #
    w = 80
    #
    dicScnTip = {
        0: 'Tip(s)',
        'tip': [0, 1, 0, 1, 4, none],
        2: 'Note(s)',
        'note': [0, 3, 0, 1, 4, 'Notes']
    }
    #
    dicScnPreview = {
        0: 'Config(s)',
        'useDefaultView': [1, 1, 0, 1, 2, 'Default View'], 'useDefaultLight': [1, 1, 2, 1, 2, 'Default Light'],
        2: 'Action(s)',
        'makeViewportSnapshot': [1, 3, 0, 1, 2, 'Make Snapshot ( Viewport )', 'svg_basic@svg#camera'],
        'makeRenderSnapshot': [1, 3, 2, 1, 2, 'Make Snapshot ( Render )', 'svg_basic@svg#render']
    }
    #
    dicScnUpload = {
        0: 'Action(s)',
        'upload': [0, 1, 0, 1, 4, u'Upload ！！！', 'svg_basic@svg#update']
    }
    #
    dicScnExtendUpload = {
        'assemblyComposeUpload': [0, 0, 1, 1, 4, 'Upload / Update Assembly Compose', 'svg_basic@svg#upload']
    }
    def __init__(self, *args, **kwargs):
        super(IfScnUploadToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
        #
        self._initToolUiBox()
    #
    def refreshMethod(self):
        pass
    #
    def _initToolUiBox(self):
        sceneryStage = self._connectObject.sceneryStage
        if sceneryPr.isSceneryLinkName(sceneryStage) or sceneryPr.isLayoutLinkName(sceneryStage):
            self._scnUploadToolUiBox.show()
            self.setupScnUploadToolUiBox(self._scnUploadToolUiBox)
        elif sceneryPr.isLightLinkName(sceneryStage):
            pass
    #
    def setupBasicTab(self, layout):
        self._scnTipToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._scnTipToolUiBox)
        self._scnTipToolUiBox.setTitle('Tip & Note')
        self.setupScnTipToolUiBox(self._scnTipToolUiBox)
        #
        self._scnSnapToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._scnSnapToolUiBox)
        self._scnSnapToolUiBox.setTitle('Snapshot')
        self.setupScnSnapshotToolUiBox(self._scnSnapToolUiBox)
        #
        self._scnUploadToolUiBox = qtWidgets.QtToolbox()
        self._scnUploadToolUiBox.setTitle('Upload / Update')
        self._scnUploadToolUiBox.hide()
        layout.addWidget(self._scnUploadToolUiBox)
    #
    def setupExtendTab(self, layout):
        self._scnExtendUploadToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._scnExtendUploadToolUiBox)
        self._scnExtendUploadToolUiBox.setTitle('Upload / Update')
        self.setupScnExtendUploadToolUiBox(self._scnExtendUploadToolUiBox)
    #
    def setupScnTipToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScnTip)
        #
        self._scnTipLabel = qtWidgets.QtTextbrower()
        toolBox.addInfo('tip', self._scnTipLabel)
        self._scnTipLabel.setEnterEnable(False)
        self._scnTipLabel.setRule(self.uploadTips)
        #
        self._scnNoteTextBrower = qtWidgets.QtTextbrower()
        toolBox.addButton('note', self._scnNoteTextBrower)
        self._scnNoteTextBrower.setTooltip(
            u'''输入 备注信息'''
        )
        #
        toolBox.addSeparators()
    #
    def setupScnSnapshotToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScnPreview)
        #
        self._useDefaultViewButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('useDefaultView', self._useDefaultViewButton)
        self._useDefaultViewButton.setChecked(True)
        self._useDefaultViewButton.setTooltip(
            u'''启用 / 关闭 截屏的时候 是否使用 默认摄像机视角'''
        )
        #
        self._useDefaultLightButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('useDefaultLight', self._useDefaultLightButton)
        self._useDefaultLightButton.setChecked(True)
        self._useDefaultLightButton.setTooltip(
            u'''启用 / 关闭 截屏（渲染）的时候 是否创建 默认灯光'''
        )
        #
        self._makeViewportSnapshotButton = qtWidgets.QtPressbutton()
        toolBox.addButton('makeViewportSnapshot', self._makeViewportSnapshotButton)
        self._makeViewportSnapshotButton.released.connect(self._scnViewportSnapshotCmd)
        self._makeViewportSnapshotButton.setTooltip(
            u'''点击 上传视窗截屏'''
        )
        #
        self._makeRenderSnapshotButton = qtWidgets.QtPressbutton()
        toolBox.addButton('makeRenderSnapshot', self._makeRenderSnapshotButton)
        self._makeRenderSnapshotButton.clicked.connect(self._scnRenderSnapshotCmd)
        self._makeRenderSnapshotButton.setTooltip(
            u'''点击 上传渲染截屏'''
        )
        #
        toolBox.addSeparators()
    #
    def setupScnUploadToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScnUpload)
        #
        self._uploadButton = qtWidgets.QtPressbutton()
        toolBox.addButton('upload', self._uploadButton)
        self._uploadButton.clicked.connect(self._scnAssemblyUploadCmd)
        #
        toolBox.addSeparators()
    #
    def setupScnExtendUploadToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScnExtendUpload)
        #
        self._assemblyComposeUploadButton = qtWidgets.QtPressbutton()
        toolBox.addButton('assemblyComposeUpload', self._assemblyComposeUploadButton)
        self._assemblyComposeUploadButton.clicked.connect(self._scnAssemblyComposeUploadCmd)
    #
    def _scnViewportSnapshotCmd(self):
        projectName = self.projectName
        sceneryCategory = self._connectObject.sceneryCategory
        sceneryName = self._connectObject.sceneryName
        sceneryVariant = self._connectObject.sceneryVariant
        sceneryStage = self._connectObject.sceneryStage
        root = None
        #
        if sceneryPr.isSceneryLinkName(sceneryStage) or sceneryPr.isLayoutLinkName(sceneryStage):
            root = sceneryPr.scnAssemblyGroupName(sceneryName)
        elif sceneryPr.isLightLinkName(sceneryStage):
            root = sceneryPr.scnAssemblyArName(sceneryCategory, sceneryName, sceneryVariant)
        #
        isUseDefaultView = self._useDefaultViewButton.isChecked()
        #
        if root:
            viewportPreview = sceneryPr.scnUnitPreviewFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage
            )[1]
            #
            maFile.makeSnapshot(
                root, viewportPreview,
                useDefaultMaterial=0,
                width=prsVariants.Util.rndrImageWidth / 2, height=prsVariants.Util.rndrImageHeight / 2,
                useDefaultView=isUseDefaultView
            )
            #
            bscObjects.If_Message(
                u'Make Snapshot ( View Port )', u'Complete'
            )
    #
    def _scnRenderSnapshotCmd(self):
        projectName = self.projectName
        sceneryCategory = self._connectObject.sceneryCategory
        sceneryName = self._connectObject.sceneryName
        sceneryVariant = self._connectObject.sceneryVariant
        sceneryStage = self._connectObject.sceneryStage
        #
        root = None
        #
        if sceneryPr.isSceneryLinkName(sceneryStage) or sceneryPr.isLayoutLinkName(sceneryStage):
            root = sceneryPr.scnAssemblyGroupName(sceneryName)
        elif sceneryPr.isLightLinkName(sceneryStage):
            root = sceneryPr.scnAssemblyArName(sceneryCategory, sceneryName, sceneryVariant)
        #
        isUseDefaultView = self._useDefaultViewButton.isChecked()
        isUseDefaultLight = self._useDefaultLightButton.isChecked()
        #
        if root:
            renderPreview = sceneryPr.scnUnitPreviewFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
                prsVariants.Util.pngExt
            )[1]
            renderer = prsMethods.Project.mayaRenderer(projectName)
            #
            maRender.setRenderSnapshot(
                root, renderPreview, renderer,
                width=prsVariants.Util.rndrImageWidth / 2, height=prsVariants.Util.rndrImageHeight / 2,
                useDefaultView=isUseDefaultView, useDefaultLight=isUseDefaultLight
            )
            #
            bscObjects.If_Message(
                u'Make Snapshot ( Render )', u'Complete'
            )
    #
    def _scnAssemblyUploadCmd(self):
        sceneryIndex = self._connectObject.sceneryIndex
        projectName = self._connectObject.projectName
        sceneryCategory = self._connectObject.sceneryCategory
        sceneryName = self._connectObject.sceneryName
        sceneryVariant = self._connectObject.sceneryVariant
        sceneryStage = self._connectObject.sceneryStage
        #
        description = u'场景 - 组装 上传 / 更新'
        notes = self._scnNoteTextBrower.datum()
        #
        self._connectObject.hide()
        #
        if sceneryName:
            maScnUploadCmds.scnUnitAssemblyUploadCmd(
                projectName,
                sceneryIndex,
                sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
                description, notes
            )
            #
            closeTimer = threading.Timer(5, self._connectObject.uiQuit)
            closeTimer.start()
    #
    def _scnAssemblyComposeUploadCmd(self):
        sceneryIndex = self._connectObject.sceneryIndex
        projectName = self._connectObject.projectName
        sceneryCategory = self._connectObject.sceneryCategory
        sceneryName = self._connectObject.sceneryName
        sceneryVariant = self._connectObject.sceneryVariant
        sceneryStage = self._connectObject.sceneryStage
        #
        timeTag = bscMethods.OsTimetag.active()
        #
        maScnUploadCmds.scnUnitAssemblyComposeUploadCmd(
            projectName,
            sceneryIndex,
            sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
            timeTag
        )
        bscObjects.If_Message(
            u'Upload / Update Assembly Compose Data', u'Complete'
        )
    #
    def setUploadScnLight(self):
        pass
    #
    def setupUnit(self):
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        self.mainLayout().addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        # Upload
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Basic', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupBasicTab(layout)
        # Extend
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Extend', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupExtendTab(layout)
