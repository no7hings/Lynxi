# coding=utf-8
import threading
#
from LxBasic import bscMtdCore, bscMethods, bscObjects

from LxPreset import prsConfigure, prsMethods, prsOutputs
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr, sceneryPr
#
from LxGui.qt import qtWidgets_, guiQtWidgets, qtCore
#
from LxKit.qt import kitQtWgtAbs
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
class IfScnAssemblyLoadedUnit(kitQtWgtAbs.AbsKitQtWgtUnit_):
    VAR_kit__qt_wgt__unit__uiname = 'Assembly Load Unit'
    VAR_kit__qt_wgt__unit__icon = 'window/sceneryToolPanel'
    VAR_kit__qt_wgt__unit__tip = u'''组装加载工具'''
    VAR_kit__qt_wgt__unit__side_width = 320
    #
    panelWidth = 800
    panelHeight = 800
    #
    widthSet = 800
    #
    projectName = currentProjectName
    def __init__(self, *args, **kwargs):
        super(IfScnAssemblyLoadedUnit, self).__init__(*args, **kwargs)
        self._initAbsKitQtWgtUnit()
        #
        self._kit__unit__set_build_()
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
    def _kit__unit__set_left_build_(self, layout):
        pass
    #
    def _kit__unit__set_central_build_(self, layout):
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
                ('Load Assembly(s)', ('svg_basic/file', 'svg_basic/load_action'), assembliesLoadEnable, assembliesLoadCmds)
            ]
            self._gridView.setActionData(actionData)
        #
        width, height = 240, 240
        #
        self._gridView = guiQtWidgets.QtGridview()
        self._gridView.setCheckEnable(True)
        self._gridView.setItemSize(240, 240 + 40)
        layout.addWidget(self._gridView)
        self._gridView.setKeywordFilterWidgetConnect(self.filterEnterLabel())
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
                        prsConfigure.Utility.DEF_value_root_server,
                        projectName, assetCategory, assetName
                    )
                    if bscMethods.OsFile.isExist(osPath):
                        bscMethods.OsDirectory.open(osPath)
                #
                subActionData = [
                    ('Basic', ),
                    ('Load Current Assembly', ('svg_basic/file', 'svg_basic/load_action'), True, assemblyLoadCmd),
                    ('Extend', ),
                    ('Open Current Assembly Folder', 'svg_basic/folder', True, assemblyFolderOpenCmd)
                ]
                gridItem.setActionData(subActionData, title=viewExplain)
            #
            def getBuildData(data):
                for keyword, fileString_ in data:
                    mtimestamp = bscMethods.OsFile.mtimestamp(fileString_)
                    exists = mtimestamp is not None
                    rgba = [(255, 255, 64, 255), (63, 255, 127, 255)][exists]
                    iconKeywordStr = [None, 'svg_basic/time'][exists]
                    messageLis.append((messageWidget.DrawColor, (rgba, iconKeywordStr, bscMethods.OsTimestamp.toChnPrettify(mtimestamp))))
            #
            assetIndex = key
            assetCategory = assetPr.getAssetClass(assetIndex)
            assetName, viewName = value
            assetVariant = prsOutputs.Util.astDefaultVariant
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
            gridItem = guiQtWidgets.QtGridViewitem()
            gridView.addItem(gridItem)
            viewExplain = assetPr.getAssetViewInfo(assetIndex, assetCategory, '{} - {}'.format(assetName, assetVariant))
            gridItem.setNameString(viewExplain)
            gridItem.setIcon('svg_basic/assembly_object')
            r, g, b = qtCore.str2rgb(assetName)
            gridItem.setFilterColor((r, g, b, 255))
            #
            preview = dbGet.getDbAstPreviewFile(assetIndex, assetVariant)
            #
            messageWidget = guiQtWidgets.QtMessageWidget()
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
                prsConfigure.Utility.DEF_value_root_server,
                projectName,
                assetCategory, assetName, assetVariant, prsMethods.Asset.assemblyLinkName()
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
            assetLinkFilter=prsMethods.Asset.assemblyLinkName()
        )
        #
        gridView.cleanItems()
        if uiData:
            # View Progress
            explain = '''Build Assembly Unit(s)'''
            maxValue = len(uiData)
            progressBar = bscObjects.ProgressWindow(explain, maxValue)
            for s, (k, v) in enumerate(uiData.items()):
                progressBar.update()
                setBranch(s, k, v)
        #
        gridView.setRefresh()
        gridView.setSortByName()
        #
        self._kit__unit__set_tag_filter_action_build_(gridView)
    #
    def _kit__unit__set_build_(self):
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
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        leftExpandWidget.setExpanded(False)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self._kit__unit__set_left_build_(leftScrollArea)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        centralLayout = qtCore.QVBoxLayout_(widget)
        centralLayout.setContentsMargins(0, 0, 0, 0)
        centralLayout.setSpacing(0)
        self._kit__unit__set_central_build_(centralLayout)


#
class IfScnAssemblyManagerUnit(kitQtWgtAbs.IfToolUnitBasic):
    VAR_kit__qt_wgt__unit__uiname = 'Assembly Manager'
    VAR_kit__qt_wgt__unit__icon = 'window/sceneryToolPanel'
    VAR_kit__qt_wgt__unit__tip = u'''组装管理工具'''


#
class IfScnComposeManagerUnit(kitQtWgtAbs.IfToolUnitBasic):
    VAR_kit__qt_wgt__unit__uiname = 'Scenery Compose Manager'
    VAR_kit__qt_wgt__unit__icon = 'window/sceneryToolPanel'
    VAR_kit__qt_wgt__unit__tip = u'''场景管理工具'''


# Scenery Tool
class IfScnLinkToolUnit(qtCore.QWidget_):
    VAR_kit__qt_wgt__unit__uiname = 'Scenery Tool Unit'
    VAR_kit__qt_wgt__unit__icon = 'window/sceneryToolPanel'
    #
    projectName = currentProjectName
    #
    w = 80
    dicImport = bscMtdCore.orderedDict()
    dicImport['episode'] = [w, 0, 0, 1, 4, 'Episode']
    dicImport['sequence'] = [w, 1, 0, 1, 4, 'Sequence']
    dicImport['shot'] = [w, 2, 0, 1, 4, 'Shot']
    # 3
    dicImport['loadSeqScn'] = [0, 4, 0, 1, 2, 'Load Sequence Scenery']
    dicImport['loadShotScn'] = [0, 4, 2, 1, 2, 'Load Shot Scenery']
    #
    dicTool = {
        'assemblyLoaded': [1, 0, 0, 1, 2, 'Assembly Loaded', 'svg_basic/subwindow'],
        'assemblyManager': [1, 0, 2, 1, 2, 'Assembly Manager', 'svg_basic/subwindow']
    }

    def __init__(self, *args, **kwargs):
        super(IfScnLinkToolUnit, self).__init__(*args, **kwargs)
        self._connectObject = None
        #
        self._kit__unit__set_build_()
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
            self.assemblyLoadedButton = guiQtWidgets.QtPressbutton()
            toolBox.setButton(inData, 'assemblyLoaded', self.assemblyLoadedButton)
            self.assemblyLoadedButton.clicked.connect(self.setAssemblyLoadedShow)
            #
            self.assemblyManagerButton = guiQtWidgets.QtPressbutton()
            toolBox.setButton(inData, 'assemblyManager', self.assemblyManagerButton)
            self.assemblyManagerButton.clicked.connect(self.setOpenAssemblyManager)
            #
            toolBox.setSeparators(inData)
        #
        self._utilsToolUiBox = guiQtWidgets.QtToolbox()
        layout.addWidget(self._utilsToolUiBox)
        self._utilsToolUiBox.setTitle('Scenery Utilities')
        setupUtilsToolUiBox(self._utilsToolUiBox)
    @staticmethod
    def setAssemblyLoadedShow():
        IfToolWindow = guiQtWidgets.QtToolWindow()
        toolBox = IfScnAssemblyLoadedUnit()
        #
        IfToolWindow.addWidget(toolBox)
        toolBox.setConnectObject(IfToolWindow)
        IfToolWindow.setQuitConnect(toolBox.delScriptJob)
        #
        toolBox.refreshMethod()
        IfToolWindow.setDefaultSize(toolBox.widthSet, 800)
        IfToolWindow.setTitle(toolBox.VAR_kit__qt_wgt__unit__uiname)
        #
        IfToolWindow.uiShow()
    @staticmethod
    def setOpenAssemblyManager():
        from LxMaya.interface.ifWidgets import ifMaToolWindow
        w = ifMaToolWindow.IfAssemblyManagerWindow()
        w.windowShow()
    #
    def _kit__unit__set_build_(self):
        mainLayout = qtCore.QVBoxLayout_(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        #
        self._tabWidget = guiQtWidgets.QtButtonTabgroup()
        mainLayout.addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Modify', 'svg_basic/tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupModifyTab(layout)


#
class IfScnAssemblyInfoToolUnit(kitQtWgtAbs.IfToolUnitBasic):
    VAR_kit__qt_wgt__unit__uiname = 'Information Tool Unit'
    VAR_kit__qt_wgt__unit__icon = 'window/infoToolPanel'
    VAR_kit__qt_wgt__unit__tip = u'''信息工具模块'''
    #
    AssemblyRadarChartConfig = ['Asset', 'Assembly', 'LOD00', 'LOD01', 'LOD02', 'Visible']
    AssemblySectorChartConfig = ['Asb - Path', 'Asb - Visible', 'Asb - LOD', 'Asb - Matrix']
    def __init__(self, *args, **kwargs):
        super(IfScnAssemblyInfoToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._kit__unit__set_build_()
    #
    def refreshMethod(self):
        if self.connectObject():
            self._setAssemblyChartRefresh()
    #
    def setupAssemblyQtTab(self, layout):
        self._scnAssemblyRadarChart = guiQtWidgets.QtRadarchart()
        layout.addWidget(self._scnAssemblyRadarChart)
        #
        self._scnAssemblySectorChart = guiQtWidgets.QtSectorchart()
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
        self._scnAssemblyRadarChart.setImageSize(prsOutputs.Util.rndrImageWidth, prsOutputs.Util.rndrImageHeight)
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
    def _kit__unit__set_build_(self):
        self._tabWidget = guiQtWidgets.QtButtonTabgroup()
        self.mainLayout().addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        # Assembly
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Assembly', 'svg_basic/tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupAssemblyQtTab(layout)
        # Light
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Light', 'svg_basic/tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupLightQtTab(layout)


#
class IfScnUtilityToolUnit(kitQtWgtAbs.IfToolUnitBasic):
    VAR_kit__qt_wgt__unit__uiname = 'Utilities Tool Unit'
    VAR_kit__qt_wgt__unit__icon = 'window/utilsToolPanel'
    VAR_kit__qt_wgt__unit__tip = u'''通用工具模块'''
    #
    projectName = currentProjectName
    #
    _groupCreateTip = u'''提示：请输入名字...'''
    #
    UnitScriptJobWindowName = 'scnGeneralToolScriptJobWindow'
    dicUtilsHier = {
        'autoRename': [1, 0, 0, 1, 2, 'Auto Rename'],
        'parentGroup': [0, 1, 0, 1, 3, ''], 'addObject': [1, 1, 3, 1, 1, 'Add Object', 'svg_basic/addtab'],
        'childGroup': [0, 2, 0, 1, 3, ''], 'addGroup': [1, 2, 3, 1, 1, 'Add Group', 'svg_basic/addtab'],
        # 3
        'groupName': [0, 4, 0, 1, 4, 'Group Name'],
        'tips': [0, 5, 0, 1, 4, 'Tip(s)']
    }
    #
    dicScnUtils = {
        'assemblyLoaded': [1, 0, 0, 1, 2, 'Assembly Loaded', 'svg_basic/subwindow'], 'assemblyManager': [1, 0, 2, 1, 2, 'Assembly Manager', 'svg_basic/subwindow'],
        # 1
        'astUnitClearScene': [1, 2, 0, 1, 4, 'Clean Maya Scene']
    }
    def __init__(self, *args, **kwargs):
        super(IfScnUtilityToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.filterTypes = ['assemblyReference']
        #
        self._kit__unit__set_build_()
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
            self.filterTypes = [appCfg.DEF_mya_type_assembly_reference]
            #
            self.setupScnUtilToolBox(self._scnUtilTooUiBox)
            #
            if sceneryPr.isLightLinkName(sceneryStage):
                self._addObjectButton.setNameString('Add Light')
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
                if not objectPath.endswith(self._rootGroup) and not objectPath.endswith(self._linkGroup) and objectPath.startswith(appCfg.DEF_mya_node_pathsep + self._rootGroup):
                    if objectPath.endswith(prsOutputs.Util.basicGroupLabel):
                        objectName = maUtils._nodeString2nodename_(objectPath)
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
                parentPath = maUtils._dcc_getNodFullpathNodepathStr(parent)
                if maUtils._isAppExist(parentPath):
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
        self._autoRenameCheckbutton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'autoRename', self._autoRenameCheckbutton)
        #
        self._parentGroupLabel = guiQtWidgets.QtValueLine()
        toolBox.setInfo(inData, 'parentGroup', self._parentGroupLabel)
        #
        self._addObjectButton = guiQtWidgets.QtPressbutton()
        self._addObjectButton.setPressable(False)
        toolBox.setButton(inData, 'addObject', self._addObjectButton)
        self._addObjectButton.clicked.connect(setAddObject)
        #
        self._childGroupLabel = guiQtWidgets.QtValueLine()
        toolBox.setInfo(inData, 'childGroup', self._childGroupLabel)
        #
        self._addGroupButton = guiQtWidgets.QtPressbutton()
        self._addGroupButton.setPressable(False)
        toolBox.setButton(inData, 'addGroup', self._addGroupButton)
        self._addGroupButton.clicked.connect(setAddGroup)
        #
        self._groupKeywordEntryLabel = guiQtWidgets.QtValueLine()
        self._groupKeywordEntryLabel.setTextValidator(48)
        self._groupKeywordEntryLabel.setEnterEnable(True)
        self._groupKeywordEntryLabel.setEnterable(True)
        toolBox.setInfo(inData, 'groupName', self._groupKeywordEntryLabel)
        self._groupKeywordEntryLabel.entryChanged.connect(setChildGroupName)
        self._groupKeywordEntryLabel.entryChanged.connect(setAddGrpBtnState)
        #
        self._groupNameTipsLabel = guiQtWidgets.QtValueLine()
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
        self.assemblyLoadedButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('assemblyLoaded', self.assemblyLoadedButton)
        self.assemblyLoadedButton.clicked.connect(self._assemblyLoadWindowShowCmd)
        #
        self.assemblyManagerButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('assemblyManager', self.assemblyManagerButton)
        self.assemblyManagerButton.clicked.connect(self._assemblyManagerWindowShowCmd)
        #
        self.sceneClearButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('astUnitClearScene', self.sceneClearButton)
        self.sceneClearButton.clicked.connect(self.setCleanScene)
        #
        toolBox.addSeparators()
    @staticmethod
    def _assemblyLoadWindowShowCmd():
        win = guiQtWidgets.QtToolWindow()
        #
        unit = IfScnAssemblyLoadedUnit()
        #
        win.addWidget(unit)
        unit.setConnectObject(win)
        win.setQuitConnect(unit.delScriptJob)
        #
        unit.refreshMethod()
        win.setDefaultSize(unit.panelWidth, 800)
        win.setNameString(unit.VAR_kit__qt_wgt__unit__uiname)
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
    def _kit__unit__set_build_(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        self._scnGraphToolUiBox = guiQtWidgets.QtToolbox()
        layout.addWidget(self._scnGraphToolUiBox)
        self._scnGraphToolUiBox.setTitle('Assembly Graph')
        #
        self._scnUtilTooUiBox = guiQtWidgets.QtToolbox()
        layout.addWidget(self._scnUtilTooUiBox)
        self._scnUtilTooUiBox.setTitle('Assembly Utilities')


#
class IfScnUploadToolUnit(kitQtWgtAbs.IfToolUnitBasic):
    VAR_kit__qt_wgt__unit__uiname = 'Upload Tool Unit'
    VAR_kit__qt_wgt__unit__icon = 'window/uploadToolPanel'
    VAR_kit__qt_wgt__unit__tip = u'''上传工具模块'''
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
        'makeViewportSnapshot': [1, 3, 0, 1, 2, 'Make Snapshot ( Viewport )', 'svg_basic/camera'],
        'makeRenderSnapshot': [1, 3, 2, 1, 2, 'Make Snapshot ( Render )', 'svg_basic/render']
    }
    #
    dicScnUpload = {
        0: 'Action(s)',
        'upload': [0, 1, 0, 1, 4, u'Upload ！！！', 'svg_basic/update']
    }
    #
    dicScnExtendUpload = {
        'assemblyComposeUpload': [0, 0, 1, 1, 4, 'Upload / Update Assembly Compose', 'svg_basic/upload']
    }
    def __init__(self, *args, **kwargs):
        super(IfScnUploadToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._kit__unit__set_build_()
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
        self._scnTipToolUiBox = guiQtWidgets.QtToolbox()
        layout.addWidget(self._scnTipToolUiBox)
        self._scnTipToolUiBox.setTitle('Tip & Note')
        self.setupScnTipToolUiBox(self._scnTipToolUiBox)
        #
        self._scnSnapToolUiBox = guiQtWidgets.QtToolbox()
        layout.addWidget(self._scnSnapToolUiBox)
        self._scnSnapToolUiBox.setTitle('Snapshot')
        self.setupScnSnapshotToolUiBox(self._scnSnapToolUiBox)
        #
        self._scnUploadToolUiBox = guiQtWidgets.QtToolbox()
        self._scnUploadToolUiBox.setTitle('Upload / Update')
        self._scnUploadToolUiBox.hide()
        layout.addWidget(self._scnUploadToolUiBox)
    #
    def setupExtendTab(self, layout):
        self._scnExtendUploadToolUiBox = guiQtWidgets.QtToolbox()
        layout.addWidget(self._scnExtendUploadToolUiBox)
        self._scnExtendUploadToolUiBox.setTitle('Upload / Update')
        self.setupScnExtendUploadToolUiBox(self._scnExtendUploadToolUiBox)
    #
    def setupScnTipToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScnTip)
        #
        self._scnTipLabel = guiQtWidgets.QtTextbrower()
        toolBox.addInfo('tip', self._scnTipLabel)
        self._scnTipLabel.setEnterEnable(False)
        self._scnTipLabel.setRule(self.uploadTips)
        #
        self._scnNoteTextBrower = guiQtWidgets.QtTextbrower()
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
        self._useDefaultViewButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('useDefaultView', self._useDefaultViewButton)
        self._useDefaultViewButton.setChecked(True)
        self._useDefaultViewButton.setTooltip(
            u'''启用 / 关闭 截屏的时候 是否使用 默认摄像机视角'''
        )
        #
        self._useDefaultLightButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('useDefaultLight', self._useDefaultLightButton)
        self._useDefaultLightButton.setChecked(True)
        self._useDefaultLightButton.setTooltip(
            u'''启用 / 关闭 截屏（渲染）的时候 是否创建 默认灯光'''
        )
        #
        self._makeViewportSnapshotButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('makeViewportSnapshot', self._makeViewportSnapshotButton)
        self._makeViewportSnapshotButton.released.connect(self._scnViewportSnapshotCmd)
        self._makeViewportSnapshotButton.setTooltip(
            u'''点击 上传视窗截屏'''
        )
        #
        self._makeRenderSnapshotButton = guiQtWidgets.QtPressbutton()
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
        self._uploadButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('upload', self._uploadButton)
        self._uploadButton.clicked.connect(self._scnAssemblyUploadCmd)
        #
        toolBox.addSeparators()
    #
    def setupScnExtendUploadToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScnExtendUpload)
        #
        self._assemblyComposeUploadButton = guiQtWidgets.QtPressbutton()
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
                prsConfigure.Utility.DEF_value_root_server,
                projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage
            )[1]
            #
            maFile.makeSnapshot(
                root, viewportPreview,
                useDefaultMaterial=0,
                width=prsOutputs.Util.rndrImageWidth / 2, height=prsOutputs.Util.rndrImageHeight / 2,
                useDefaultView=isUseDefaultView
            )
            #
            bscObjects.MessageWindow(
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
                prsConfigure.Utility.DEF_value_root_server,
                projectName, sceneryCategory, sceneryName, sceneryVariant, sceneryStage,
                prsOutputs.Util.pngExt
            )[1]
            renderer = prsMethods.Project.mayaRenderer(projectName)
            #
            maRender.setRenderSnapshot(
                root, renderPreview, renderer,
                width=prsOutputs.Util.rndrImageWidth / 2, height=prsOutputs.Util.rndrImageHeight / 2,
                useDefaultView=isUseDefaultView, useDefaultLight=isUseDefaultLight
            )
            #
            bscObjects.MessageWindow(
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
        bscObjects.MessageWindow(
            u'Upload / Update Assembly Compose Data', u'Complete'
        )
    #
    def setUploadScnLight(self):
        pass
    #
    def _kit__unit__set_build_(self):
        self._tabWidget = guiQtWidgets.QtButtonTabgroup()
        self.mainLayout().addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        # Upload
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Basic', 'svg_basic/tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupBasicTab(layout)
        # Extend
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Extend', 'svg_basic/tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupExtendTab(layout)
