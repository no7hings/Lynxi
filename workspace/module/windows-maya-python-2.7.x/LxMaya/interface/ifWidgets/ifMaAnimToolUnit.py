# coding=utf-8
import os, threading
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscCore, bscMethods, bscObjects

from LxCore import lxConfigure, lxScheme

from LxCore.config import appCfg, sceneCfg

from LxPreset import prsVariants, prsMethods

from LxCore.preset.prod import projectPr, assetPr, scenePr

from LxUi.qt import qtWidgets_, qtWidgets, qtCore

from LxInterface.qt.qtIfBasic import _qtIfAbcWidget

from LxDatabase import dbGet

from LxMaya.command import maUtils, maFile, maFur, maKeyframe, maCam, maRender, maPreference

from LxMaya.product import maAstLoadCmds

from LxMaya.product.data import datAsset, datScene, datAnim

from LxMaya.product.op import animOp, sceneOp

from LxMaya.product import maScUploadCmds

from LxMaInterface import maIfMethods

from LxDeadline import ddlCommands

# Project Data
currentProjectName = projectPr.getMayaProjectName()
# File Label
astLayoutRigFileLabel = prsVariants.Util.astLayoutRigFileLabel
astAnimationRigFileLabel = prsVariants.Util.astAnimationRigFileLabel
astSimulationRigFileLabel = prsVariants.Util.astSimulationRigFileLabel
#
none = ''


#
class IfScRigLoadedUnit(_qtIfAbcWidget.QtIfAbc_Unit_):
    UnitTitle = 'Asset Rig Load'
    SideWidth = 320
    #
    projectName = currentProjectName
    #
    panelWidth = 800
    panelHeight = 800
    #
    widthSet = 800
    #
    dicFilter = bscCore.orderedDict()
    dicFilter['withCharacter'] = [0, 0, 0, 1, 2, 'Character ( 0000 )']
    dicFilter['withProp'] = [0, 0, 2, 1, 2, 'Prop ( 0000 )']
    #
    dicTool = bscCore.orderedDict()
    dicTool['usePoolAsset'] = [0, 0, 0, 1, 3, 'Ignore Asset ( Rig ) Update']
    # 1
    dicTool['multiple'] = [0, 2, 0, 1, 1, none]
    dicTool['load'] = [0, 2, 1, 1, 3, 'Load Asset ( Rig ) [ 0000 ]']
    dicTool['version'] = [0, 2, 4, 1, 2, none]
    # 3
    dicTool['animationManager'] = [0, 4, 0, 1, 6, 'Animation Manager']
    def __init__(self, *args, **kwargs):
        super(IfScRigLoadedUnit, self).__init__(*args, **kwargs)
        self._initIfAbcUnit()
        #
        self.classify = none
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        self.setupConnection()
        self.setCentralRefresh()
    #
    def delScriptJob(self):
        pass
    #
    def setupLeftWidget(self, layout):
        pass
    #
    def setupCentralWidget(self, layout):
        def setActions():
            def isLoadAstRigEnable():
                return self._gridView.checkedItems() != []
            #
            def loadAstRigCmd():
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
                        maAstLoadCmds.astUnitRigLoadForAnimationCmd(
                            projectName,
                            assetIndex,
                            assetCategory, assetName, assetVariant
                        )
            #
            actionDatumLis = [
                ('Basic', ),
                ('Load Asset(s) - Rig', ('svg_basic@svg#file', 'svg_basic@svg#load_action'), isLoadAstRigEnable, loadAstRigCmd)
            ]
            self._gridView.setActionData(actionDatumLis)

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
    def setupConnection(self):
        self._gridView.setFilterConnect(self.filterEnterLabel())
        #
        self.refreshButton().clicked.connect(self.setCentralRefresh)
    #
    def setCentralRefresh(self):
        def setBranch(seq, key, value):
            def setSubActions():
                def rigLoadCmd():
                    maAstLoadCmds.astUnitRigLoadForAnimationCmd(
                        projectName,
                        assetIndex,
                        assetCategory, assetName, assetVariant
                    )
                #
                def rigFolderOpenCmd():
                    fileString_ = assetPr.astUnitProductFile(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName,
                        assetCategory, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
                    )[1]

                    bscMethods.OsFile.openDirectory(fileString_)
                #
                subActionData = [
                    ('Basic',),
                    ('Load Current Rig', ('svg_basic@svg#file', 'svg_basic@svg#load_action'), True, rigLoadCmd),
                    ('Extend',),
                    ('Open Current Rig Folder', 'svg_basic@svg#folder', True, rigFolderOpenCmd)
                ]
                gridItem.setActionData(subActionData, title=viewExplain)
            #
            assetIndex = key
            assetCategory = None
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
            viewExplain = assetPr.getAssetViewInfo(assetIndex, assetCategory, '{} - {}'.format(assetName, assetVariant))
            gridItem = qtWidgets.QtGridviewItem()
            gridView.addItem(gridItem)
            #
            gridItem.setName(viewExplain)
            gridItem.setIcon('svg_basic@svg#rig')
            #
            preview = dbGet.getDbAstPreviewFile(assetIndex, assetVariant)
            #
            messageWidget = qtWidgets.QtMessageWidget()
            messageWidget.setExplainWidth(20)
            gridItem.addWidget(messageWidget, 0, 0, 1, 1)
            #
            productFile = assetPr.astUnitProductFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                assetCategory, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
            )[1]
            mtimestamp = bscMethods.OsFile.mtimestamp(productFile)
            exists = mtimestamp is not None
            rgba = [(255, 255, 64, 255), (63, 255, 127, 255)][exists]
            iconKeyword = [None, 'svg_basic@svg#time'][exists]
            #
            messages = [
                (messageWidget.DrawImage1, preview),
                (messageWidget.DrawColor, (rgba, iconKeyword, bscMethods.OsTimestamp.toChnPrettify(mtimestamp)))
            ]
            messageWidget.setDatumLis(messages, 240, 240)
            #
            gridItem.assetIndex = assetIndex
            gridItem.assetCategory = None
            gridItem.assetName = assetName
            gridItem.assetVariant = assetVariant
            #
            setSubActions()
        #
        projectName = self.projectName
        #
        gridView = self._gridView
        #
        uiData = assetPr.getUiAssetMultMsgDic(
            projectName,
            assetLinkFilter=lxConfigure.LynxiProduct_Asset_Link_Rig
        )
        #
        gridView.cleanItems()
        if uiData:
            # View Progress
            explain = '''Build Rig Unit(s)'''
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
    @staticmethod
    def setOpenAnimationManager():
        IfToolWindow = qtWidgets.QtToolWindow()
        toolBox = IfScAnimManagerUnit()
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
    #
    def setupUnit(self):
        self.topToolBar().show()
        #
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
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
class IfScLayoutToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    widthSet = 400
    #
    projectName = currentProjectName
    #
    UnitTitle = 'Layout Unit'
    #
    UnitScriptJobWindowName = 'cameraManagerWindow'
    #
    w = 80
    # Tool
    dicScCamTool = {
        'cameraSearch': [1, 0, 0, 1, 4, 'Camera'],
        'placeholderB': [1, 1, 2, 1, 4, 'Placeholder'],
        'addCamera': [1, 2, 0, 1, 2, 'Add Camera [ 000 ]', 'svg_basic@svg#add'], 'removeCamera': [1, 2, 2, 1, 2, 'Remove Camera [ 000 ]', 'svg_basic@svg#remove'],
        3: 'Modify',
        'createCamera': [1, 4, 0, 1, 2, 'Create Default Camera', 'svg_basic@svg#camera'], 'setCameraView': [1, 4, 2, 1, 2, 'Set Camera View', 'svg_basic@svg#modify'],
        5: 'HUD',
        'openHud': [1, 6, 0, 1, 2, 'Open HUD', 'svg_basic@svg#buttonOpen'], 'closeHud': [1, 6, 2, 1, 2, 'Close HUD', 'svg_basic@svg#buttonClose'],
        7: 'Update',
        'updateCamera': [1, 8, 0, 1, 4, 'Update Camera(s) [ 000 ]', 'svg_basic@svg#update']
    }
    #
    dicScPrvTool = {
        'frame': [w, 0, 0, 1, 4, 'Frame'],
        'size': [w, 1, 0, 1, 4, 'Size'],
        'quality': [w, 2, 0, 1, 4, 'Quality'],
        'percent': [w, 3, 0, 1, 4, 'Percent'],
        'aviFormat': [1, 5, 0, 1, 1, '.avi'], 'movFormat': [1, 5, 1, 1, 1, '.mov'], 'openFolder': [1, 5, 2, 1, 2, 'Open Folder'],
        'updatePreview': [1, 6, 0, 1, 4, 'Update Preview [ 000 ]', 'svg_basic@svg#camera']
    }
    # Import
    dicScCamImportTool = {
        'classify': [w, 0, 0, 1, 4, 'Classify'],
        'name': [w, 1, 0, 1, 4, 'Name'],
        'variant': [w, 2, 0, 1, 4, 'Variant'],
        'mayaFile': [0, 4, 0, 1, 1, 'Maya Ascii'], 'fbxFile': [0, 4, 1, 1, 1, 'FBX'],
        'importCamera': [0, 5, 0, 1, 4, 'Import Camera']
    }
    def __init__(self, *args, **kwargs):
        super(IfScLayoutToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnit()
        #
        self.setScriptJob()
    #
    def setConnectObject(self, method):
        self._connectObject = method
        self._connectObject.setQuitConnect(self.delScriptJob)
    #
    def refreshMethod(self):
        if self._connectObject:
            self._initCameraTool()
            self._initPreviewTool()
            self._initCameraImportTool()
    #
    def setScriptJob(self):
        scriptJobEvn = 'cameraChange'
        methods = [self.setListScCamera]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupModifyTab(self, layout):
        # Camera Box
        self._cameraToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self._cameraToolBox)
        self._cameraToolBox.setTitle('Scene ( Camera ) Modify')
        self.setupCameraToolUiBox(self._cameraToolBox)
        # Preview Box
        self._previewToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self._previewToolBox)
        self._previewToolBox.setTitle('Scene ( Preview ) Modify')
        self.setupPreviewToolUiBox(self._previewToolBox)
    #
    def setupCameraToolUiBox(self, toolBox):
        inData = self.dicScCamTool
        #
        self._scCameraFilterLabel = qtWidgets.QtFilterEnterlabel()
        toolBox.setButton(inData, 'cameraSearch', self._scCameraFilterLabel)
        #
        self._availableCameraTreeViewBox = qtWidgets_.QTreeWidget_()
        toolBox.addWidget(self._availableCameraTreeViewBox, 1, 0, 1, 2)
        self._availableCameraTreeViewBox.setColumns(['Available Camera'], [4], self.widthSet / 2 - 32)
        self._availableCameraTreeViewBox.itemSelectionChanged.connect(self.setModifyBtnState)
        self._availableCameraTreeViewBox.itemSelectionChanged.connect(self.setRefreshMayaSceneSelection)
        self._availableCameraTreeViewBox.setFilterConnect(self._scCameraFilterLabel)
        #
        self._activeCameraTreeViewBox = qtWidgets_.QTreeWidget_()
        toolBox.addWidget(self._activeCameraTreeViewBox, 1, 2, 1, 2)
        self._activeCameraTreeViewBox.setColumns(['Active Camera'], [4], self.widthSet / 2 - 32)
        self._activeCameraTreeViewBox.itemSelectionChanged.connect(self.setModifyBtnState)
        self._activeCameraTreeViewBox.itemSelectionChanged.connect(self.setRefreshMayaSceneSelection)
        self._activeCameraTreeViewBox.setFilterConnect(self._scCameraFilterLabel)
        #
        self._addCameraButton = qtWidgets.QtPressbutton()
        self._addCameraButton.setPressable(False)
        toolBox.setButton(inData, 'addCamera', self._addCameraButton)
        self._addCameraButton.clicked.connect(self.setAddSceneCameras)
        #
        self._removeCameraButton = qtWidgets.QtPressbutton()
        self._removeCameraButton.setPressable(False)
        toolBox.setButton(inData, 'removeCamera', self._removeCameraButton)
        self._removeCameraButton.clicked.connect(self.setRemoveSceneCameras)
        #
        self._setCameraViewButton = qtWidgets.QtPressbutton()
        self._setCameraViewButton.setPressable(False)
        toolBox.setButton(inData, 'setCameraView', self._setCameraViewButton)
        self._setCameraViewButton.clicked.connect(self.setCameraView)
        #
        self.openHudButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'openHud', self.openHudButton)
        self.openHudButton.clicked.connect(self.setOpenHud)
        #
        self.closeHudButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'closeHud', self.closeHudButton)
        self.closeHudButton.clicked.connect(self.setCloseHud)
        #
        self.createCameraButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'createCamera', self.createCameraButton)
        self.createCameraButton.clicked.connect(self.setCreateCamera)
        #
        self.updateCameraButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'updateCamera', self.updateCameraButton)
        self.updateCameraButton.setPressable(False)
        self.updateCameraButton.clicked.connect(self.setUpdateCamera)
        #
        toolBox.setSeparators(inData)
    #
    def setupPreviewToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScPrvTool)
        #
        self._previewFrameBox = qtWidgets.QtValueEnterlabel()
        toolBox.addInfo('frame', self._previewFrameBox)
        self._previewFrameBox.setEnterEnable(True)
        #
        self._previewSizeBox = qtWidgets.QtValueEnterlabel()
        toolBox.addInfo('size', self._previewSizeBox)
        self._previewSizeBox.setEnterEnable(True)
        #
        self._previewQualityLabel = qtWidgets.QtValueEnterlabel()
        toolBox.addInfo('quality', self._previewQualityLabel)
        self._previewQualityLabel.setEnterEnable(True)
        self._previewQualityLabel.setDefaultValue(100)
        self._previewQualityLabel.setValueRange(0, 100)
        #
        self._previewPercentLabel = qtWidgets.QtValueEnterlabel()
        toolBox.addInfo('percent', self._previewPercentLabel)
        self._previewPercentLabel.setEnterEnable(True)
        self._previewPercentLabel.setDefaultValue(100)
        self._previewPercentLabel.setValueRange(0, 100)
        #
        self.aviFormatButton = qtWidgets.QtRadioCheckbutton()
        toolBox.addButton('aviFormat', self.aviFormatButton)
        self.aviFormatButton.setChecked(True)
        #
        self.movFormatButton = qtWidgets.QtRadioCheckbutton()
        toolBox.addButton('movFormat', self.movFormatButton)
        #
        self.openFolderButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('openFolder', self.openFolderButton)
        self.openFolderButton.setChecked(True)
        #
        self._updateScenePreviewButton = qtWidgets.QtPressbutton()
        self._updateScenePreviewButton.setPressable(False)
        toolBox.addButton('updatePreview', self._updateScenePreviewButton)
        self._updateScenePreviewButton.clicked.connect(self._updateScPreviewCmd)
        #
        toolBox.addSeparators()
    #
    def setupImportTab(self, layout):
        self._importCameraBox = qtWidgets.QtToolbox()
        layout.addWidget(self._importCameraBox)
        self._importCameraBox.setTitle('Scene ( Camera ) Import')
        self.setupCameraImportToolUiBox(self._importCameraBox)
    #
    def setupCameraImportToolUiBox(self, toolBox):
        inData = self.dicScCamImportTool
        #
        self._scClassLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'classify', self._scClassLabel)
        self._scClassLabel.setChooseEnable(True)
        self._scClassLabel.chooseChanged.connect(self.setSceneNameUiLabelShow)
        #
        self._scNameLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'name', self._scNameLabel)
        self._scNameLabel.setChooseEnable(True)
        self._scNameLabel.chooseChanged.connect(self.setSceneVariantUiLabelShow)
        #
        self._scVariantLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'variant', self._scVariantLabel)
        self._scVariantLabel.setChooseEnable(True)
        self._scVariantLabel.chooseChanged.connect(self.setImportBtnState)
        #
        self._useMayaFileButton = qtWidgets.QtRadioCheckbutton()
        toolBox.setButton(inData, 'mayaFile', self._useMayaFileButton)
        self._useMayaFileButton.setChecked(True)
        self._useMayaFileButton.toggled.connect(self.setImportBtnState)
        #
        self._useFbxFileButton = qtWidgets.QtRadioCheckbutton()
        toolBox.setButton(inData, 'fbxFile', self._useFbxFileButton)
        self._useFbxFileButton.toggled.connect(self.setImportBtnState)
        #
        self._importCameraButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'importCamera', self._importCameraButton)
        self._importCameraButton.setPressable(False)
        self._importCameraButton.clicked.connect(self.setImportCameraCmd)
        #
        toolBox.setSeparators(inData)
    #
    def setListScCamera(self):
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        #
        availableTreeBox = self._availableCameraTreeViewBox
        activeTreeBox = self._activeCameraTreeViewBox
        #
        defCameras = sceneCfg.MayaDefaultCameras
        availableCameraLis = maUtils.getCameras(0)
        #
        activeCameraLis = datScene.getScCameraLis(sceneName, sceneVariant, sceneStage)
        #
        availableTreeBox.clear()
        if availableCameraLis:
            for cameraPath in availableCameraLis:
                if not cameraPath in activeCameraLis:
                    cameraName = maUtils._toNodeName(cameraPath)
                    #
                    cameraItem = qtWidgets_.QTreeWidgetItem_([cameraName])
                    availableTreeBox.addItem(cameraItem)
                    cameraItem.setItemMayaIcon(0, appCfg.MaCameraType)
                    #
                    cameraItem.assetName = cameraName
                    cameraItem.path = cameraPath
                    if cameraName in defCameras:
                        cameraItem.setItemMayaIcon(0, appCfg.MaCameraType, 'off')
        #
        activeTreeBox.clear()
        if activeCameraLis:
            for cameraPath in activeCameraLis:
                cameraName = maUtils._toNodeName(cameraPath)
                #
                cameraItem = qtWidgets_.QTreeWidgetItem_([cameraName])
                activeTreeBox.addItem(cameraItem)
                cameraItem.setItemMayaIcon(0, appCfg.MaCameraType)
                #
                cameraItem.assetName = cameraName
                cameraItem.path = cameraPath
                if cameraName in defCameras:
                    cameraItem.setItemMayaIcon(0, appCfg.MaCameraType, 'off')
        #
        availableTreeBox.setFilterExplainRefresh()
    #
    def setSelSwitch(self):
        availableTreeBox = self._availableCameraTreeViewBox
        activeTreeBox = self._activeCameraTreeViewBox
        if availableTreeBox.hasFocus():
            activeTreeBox.clearSelection()
        elif activeTreeBox.hasFocus():
            availableTreeBox.clearSelection()
    #
    def _initCameraTool(self):
        self.setListScCamera()
    #
    def _initPreviewTool(self):
        def setFrameBox():
            if self._connectObject:
                projectName = self._connectObject.projectName
                sceneCategory = self._connectObject.sceneCategory
                sceneName = self._connectObject.sceneName
                sceneVariant = self._connectObject.sceneVariant
                sceneStage = self._connectObject.sceneStage
                #
                if scenePr.isLayoutLinkName(sceneStage):
                    startFrame, endFrame = maUtils.getFrameRange()
                else:
                    startFrame, endFrame = scenePr.getScUnitFrameRange(projectName, sceneCategory, sceneName, sceneVariant)
                self._previewFrameBox.setDefaultValue((startFrame, endFrame))
        #
        def setSizeBox():
            width, height = scenePr.scRenderSize()
            self._previewSizeBox.setDefaultValue((width, height))
        #
        setFrameBox()
        setSizeBox()
    #
    def _initCameraImportTool(self):
        self.setSceneClassUiLabelShow()
    #
    def setModifyBtnState(self):
        availableCameraLis = self._availableCameraTreeViewBox.selectedItems()
        self._addCameraButton.setPressable([False, True][availableCameraLis != []])
        self._addCameraButton.setNameText('Add Camera [ %s ]' % str(len(availableCameraLis)).zfill(3))
        #
        activeCameraLis = self._activeCameraTreeViewBox.selectedItems()
        subBoolean = activeCameraLis != []
        #
        self._removeCameraButton.setPressable([False, True][subBoolean])
        self._removeCameraButton.setNameText('Remove Camera [ %s ]' % str(len(activeCameraLis)).zfill(3))
        #
        self._setCameraViewButton.setPressable([False, True][subBoolean])
        #
        self.updateCameraButton.setPressable([False, True][subBoolean])
        self.updateCameraButton.setNameText('Update Camera(s) [ %s ]' % str(len(activeCameraLis)).zfill(3))
        #
        self._updateScenePreviewButton.setPressable([False, True][subBoolean])
        self._updateScenePreviewButton.setNameText('Update Preview [ %s ]' % str(len(activeCameraLis)).zfill(3))
        #
        self.setSelSwitch()
    #
    def setImportBtnState(self):
        if self._connectObject:
            projectName = self.projectName
            sceneCategory = self.getSceneClass()
            sceneName = self.getSceneName()
            sceneVariant = self.getSceneVariant()
            #
            if self._useMayaFileButton.isChecked():
                serverCameraFile = scenePr.scUnitCameraProductFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    sceneCategory, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_layout
                )[1]
            else:
                serverCameraFile = scenePr.scUnitCameraFbxFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    sceneCategory, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_layout
                )[1]
            #
            boolean = bscMethods.OsFile.isExist(serverCameraFile)
            #
            self._importCameraButton.setPressable([False, True][boolean])
    #
    def setCreateCamera(self):
        if self._connectObject:
            sceneName = self._connectObject.sceneName
            sceneVariant = self._connectObject.sceneVariant
            #
            sceneCamera = scenePr.scSceneCameraName(sceneName, sceneVariant)
            if maUtils.isAppExist(sceneCamera):
                bscObjects.If_Message(
                    u'''Camera : %s''' % sceneCamera, u'''is Exists'''
                )
            if not maUtils.isAppExist(sceneCamera):
                sceneOp.setCreateSceneCamera(sceneName, sceneVariant)
            #
            sceneOp.setAddSceneCameras(sceneName, [maUtils._getNodePathString(sceneCamera)])
    #
    def setAddSceneCameras(self):
        if self._connectObject:
            sceneName = self._connectObject.sceneName
            #
            availableTreeBox = self._availableCameraTreeViewBox

            cameras = availableTreeBox.selectedItemNames()
            if cameras:
                sceneOp.setAddSceneCameras(sceneName, cameras)
                self.setListScCamera()
    #
    def setRemoveSceneCameras(self):
        if self._connectObject:
            sceneName = self._connectObject.sceneName
            #
            availableTreeBox = self._activeCameraTreeViewBox
            cameraData = availableTreeBox.selectedItemNames()
            if cameraData:
                sceneOp.setRemoveSceneCameras(sceneName, cameraData)
                self.setListScCamera()
    #
    def setRefreshMayaSceneSelection(self):
        data = self.getSelCam()
        if data:
            maUtils.setNodeSelect(data)
        else:
            pass
    #
    def setCameraView(self):
        def getCameraPaths(treeBox):
            lis = []
            selectedItems = treeBox.selectedItems()
            if selectedItems:
                for i in selectedItems:
                    path = i.path
                    lis.append(path)
            return lis
        #
        availableTreeBox = self._activeCameraTreeViewBox
        cameraPaths = getCameraPaths(availableTreeBox)
        if cameraPaths:
            usedCamera = cameraPaths[0]
            if maUtils.isAppExist(usedCamera):
                maUtils.setDisplayMode(5)
                maUtils.setCameraView(usedCamera)
                bscObjects.If_Message(
                    u'''Set Camera View''', u'''Complete'''
                )
    @staticmethod
    def setOpenHud():
        maCam.setCameraCloseHud()
        maCam.setCameraHud('large')
        maUtils.setMessageWindowShow(u'Camera HUD is', u'Open', position='midCenterTop', fade=1, dragKill=0)
    @staticmethod
    def setCloseHud():
        maCam.setCameraCloseHud()
        maUtils.setMessageWindowShow(u'Camera HUD is', u'Closed', position='midCenterTop', fade=1, dragKill=0)
    #
    def setUpdateCamera(self):
        if self._connectObject:
            sceneIndex = self._connectObject.sceneIndex
            projectName = self.projectName
            sceneCategory = self._connectObject.sceneCategory
            sceneName = self._connectObject.sceneName
            sceneVariant = self._connectObject.sceneVariant
            sceneStage = self._connectObject.sceneStage
            #
            startFrame = self._connectObject.startFrame
            endFrame = self._connectObject.endFrame
            #
            availableTreeBox = self._activeCameraTreeViewBox
            progressButton = self.updateCameraButton
            #
            sceneCameras = datScene.getScActiveCameraLis(sceneName)
            usedCameras = availableTreeBox.selectedItemNames()
            if usedCameras:
                cameraData = sceneCameras, usedCameras
                zAdjust = 0.0
                cameraConfig = (zAdjust, )
                #
                withCamera = cameraData, cameraConfig
                #
                maUtils.setCurrentFrame(startFrame)
                #
                timeTag = bscMethods.OsTimetag.active()
                #
                maScUploadCmds.scUnitCamerasUploadCmd(
                    projectName,
                    sceneIndex,
                    sceneCategory, sceneName, sceneVariant, sceneStage,
                    startFrame, endFrame, prsVariants.Util.animKeyFrameOffset,
                    timeTag,
                    withCamera
                )
                bscObjects.If_Message(
                    u'Animation Camera Upload', u'Complete'
                )
    #
    def _updateScPreviewCmd(self):
        if self._connectObject:
            sceneIndex = self._connectObject.sceneIndex
            projectName = self.projectName
            sceneCategory = self._connectObject.sceneCategory
            sceneName = self._connectObject.sceneName
            sceneVariant = self._connectObject.sceneVariant
            sceneStage = self._connectObject.sceneStage
            #
            startFrame, endFrame = self._previewFrameBox.value()
            width, height = self._previewSizeBox.value()
            #
            activeTreeBox = self._activeCameraTreeViewBox
            progressButton = self._updateScenePreviewButton
            #
            quality = self._previewQualityLabel.value()
            percent = self._previewPercentLabel.value()
            #
            vedioFormat = [prsVariants.Util.aviExt, prsVariants.Util.movExt][self.movFormatButton.isChecked()]

            isOpenFolder = self.openFolderButton.isChecked()
            #
            scCameraLis = datScene.getScCameraLis(sceneName, sceneVariant, sceneStage)
            #
            selCameraLis = activeTreeBox.selectedItemPaths()
            if selCameraLis:
                displayMode = 6
                useMode = 1
                #
                timeTag = bscMethods.OsTimetag.active()
                #
                cameraData = scCameraLis, selCameraLis
                previewConfig = percent, quality, width, height, vedioFormat, displayMode, useMode
                #
                maUtils.setCurrentFrame(startFrame)
                #
                withPreview = cameraData, previewConfig
                #
                maScUploadCmds.scUnitPreviewsUploadCmd(
                    projectName,
                    sceneIndex,
                    sceneCategory, sceneName, sceneVariant, sceneStage,
                    startFrame, endFrame, prsVariants.Util.animKeyFrameOffset,
                    timeTag,
                    withPreview
                )
                #
                if isOpenFolder:
                    localPreviewFile = scenePr.scenePreviewFile(
                        lxConfigure.LynxiRootIndex_Local,
                        projectName, sceneCategory, sceneName, sceneVariant, sceneStage
                    )[1]
                    previewFolder = bscMethods.OsFile.dirname(localPreviewFile)
                    if bscMethods.OsFile.isExist(previewFolder):
                        bscMethods.OsDirectory.open(previewFolder)
                #
                bscObjects.If_Message(
                    u'Animation Preview Upload', u'Complete'
                )
    #
    def setSceneClassUiLabelShow(self):
        self._scClassLabel.setExtendDatumDic(prsMethods.Scene.classShownameDic())
        self._scClassLabel.sendChooseChangedEmit()
    #
    def setSceneNameUiLabelShow(self):
        projectName = self._connectObject.projectName
        sceneCategory = self.getSceneClass()
        #
        datumDic = scenePr.getUiSceneMultMsgs(projectName, [sceneCategory])
        self._scNameLabel.setExtendDatumDic(datumDic)
        self._scNameLabel.sendChooseChangedEmit()
    #
    def setSceneVariantUiLabelShow(self):
        sceneIndex = self.getSceneIndex()
        #
        messages = scenePr.getSceneVariants(sceneIndex)
        self._scVariantLabel.setDatumLis(messages)
        self._scVariantLabel.sendChooseChangedEmit()
    #
    def setImportCameraCmd(self):
        if self._connectObject:
            projectName = self.projectName
            sceneCategory = self.getSceneClass()
            sceneName = self.getSceneName()
            sceneVariant = self.getSceneVariant()
            #
            if self._useMayaFileButton.isChecked():
                serverCameraFile = scenePr.scUnitCameraProductFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    sceneCategory, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_layout
                )[1]
            else:
                serverCameraFile = scenePr.scUnitCameraFbxFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    sceneCategory, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_layout
                )[1]
            if bscMethods.OsFile.isExist(serverCameraFile):
                cameraLocator = scenePr.scOutputCameraLocatorName(sceneName, sceneVariant)
                if not maUtils.isAppExist(cameraLocator):
                    maFile.setFileImport(serverCameraFile)
                    bscObjects.If_Message(
                        'Camera Import', 'Complete'
                    )
                else:
                    bscObjects.If_Message(
                        'Camera', 'is Exists'
                    )

    def getSelCam(self):
        def getBranch(treeBox):
            lis = []
            selectedItems = treeBox.selectedItems()
            if selectedItems:
                for i in selectedItems:
                    path = i.path
                    lis.append(path)
            return lis
        #
        availableTreeBox = self._availableCameraTreeViewBox
        activeTreeBox = self._activeCameraTreeViewBox
        #
        nameData = getBranch(availableTreeBox)
        subNameData = getBranch(activeTreeBox)
        nameData.extend(subNameData)
        return nameData
    #
    def getSceneIndex(self):
        multMsg = self._scNameLabel.extendDatum()
        if multMsg:
            return multMsg[0]
    #
    def getSceneClass(self):
        chooseLabel = self._scClassLabel
        #
        return chooseLabel.datum()
    #
    def getSceneName(self):
        multMsg = self._scNameLabel.extendDatum()
        if multMsg:
            return multMsg[1]
    #
    def getSceneVariant(self):
        chooseLabel = self._scVariantLabel
        #
        return chooseLabel.datum()
    #
    def initUnit(self):
        pass
    #
    def setupUnit(self):
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        self.mainLayout().addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Modify', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupModifyTab(layout)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Import', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupImportTab(layout)


#
class IfScAnimationLinkToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    projectName = currentProjectName
    # Utilities Tool
    dicUtilsTool = {
        'rigLoaded': [0, 0, 0, 1, 4, 'Asset ( Rig ) Loaded', 'svg_basic@svg#subWindow'],
        #
        'animationManager': [0, 2, 0, 1, 2, 'Scene ( Animation ) Manager', 'svg_basic@svg#subWindow'],  'simulationManager': [0, 2, 2, 1, 2, 'Scene ( Simulation ) Manager', 'svg_basic@svg#subWindow']
    }
    def __init__(self, *args, **kwargs):
        super(IfScAnimationLinkToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
        #
        treeBox = self._connectObject.treeBox
        treeBox.itemSelectionChanged.connect(self.setBtnState)
    #
    def refreshMethod(self):
        pass
    #
    def setupUtilToolUiBox(self, toolBox):
        inData = self.dicUtilsTool
        #
        self.rigLoadedButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'rigLoaded', self.rigLoadedButton)
        self.rigLoadedButton.clicked.connect(self.setRigLoadedShow)
        #
        self.animationManagerButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'animationManager', self.animationManagerButton)
        self.animationManagerButton.clicked.connect(self.setOpenAnimationManager)
        #
        self.simulationManagerButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'simulationManager', self.simulationManagerButton)
        self.simulationManagerButton.clicked.connect(self.setOpenSimulationManager)
        #
        toolBox.setSeparators(inData)
    #
    def setBtnState(self):
        if self._connectObject:
            selectedData = []
            #
            treeBox = self._connectObject.treeBox
            usedData = self._connectObject.rigUsedData
            #
            selectedItems = treeBox.selectedItems()
            #
            isUsed = False
            if selectedItems:
                for i in selectedItems:
                    if i in usedData:
                        isUsed = True
                        selectedData.append(i)
    @staticmethod
    def setRigLoadedShow():
        IfToolWindow = qtWidgets.QtToolWindow()
        toolBox = IfScRigLoadedUnit()
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
    def setOpenAnimationManager():
        IfToolWindow = qtWidgets.QtToolWindow()
        toolBox = IfScAnimManagerUnit()
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
    def setOpenSimulationManager():
        IfToolWindow = qtWidgets.QtToolWindow()
        toolBox = IfSimManagerUnit()
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
    #
    def setupUnit(self):
        self._utilsToolUiBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._utilsToolUiBox)
        self._utilsToolUiBox.setTitle('Scene ( Animation ) Utilities')
        self.setupUtilToolUiBox(self._utilsToolUiBox)


#
class IfScUtilToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    projectName = currentProjectName
    # Utilities Tool
    dicUtils = bscCore.orderedDict()
    dicUtils['astUnitClearScene'] = [1, 0, 0, 1, 4, 'Clean Maya Scene']
    dicUtils['placeholder'] = [1, 1, 0, 1, 4, 'Placeholder']
    def __init__(self, *args, **kwargs):
        super(IfScUtilToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUtilitiesToolPanel()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        pass
    #
    def setupUtilsToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicUtils)
        #
        self._cleanSceneButton = qtWidgets.QtPressbutton()
        toolBox.addButton('astUnitClearScene', self._cleanSceneButton)
        #
        toolBox.addSeparators()
    #
    def setupUtilitiesToolPanel(self):
        self.utilsBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self.utilsBox)
        self.utilsBox.setTitle('Animation Utilities')
        self.setupUtilsToolUiBox(self.utilsBox)


#
class IfScAnimUploadToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    projectName = currentProjectName
    #
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Model
    ]
    UnitTitle = 'Upload Tool Unit'
    UnitIcon = 'window#uploadToolPanel'
    UnitTooltip = u'''上传工具模块'''
    uploadTips = [
        u"提示： ",
        u"1：确认不存在错误的 Asset ； ",
        u"2：确认配置了正确的 动画帧范围 ； ",
        u"3：点击 Upload ！！！ 上传... ",
    ]
    #
    w = 80
    # Tip Box
    dicScTip = {
        'tips': [0, 0, 0, 1, 4, none],
        'notes': [0, 1, 0, 1, 4, 'Note']
    }
    # Range
    dicScRange = {
        'animFrame': [w, 0, 0, 1, 4, 'Frame'],
        'renderSize': [w, 1, 0, 1, 4, 'Size']
    }
    # Upload
    dicScUpload = {
        0: 'Index',
        'withIndex': [0, 1, 0, 1, 1, 'Scene Index'], 'indexSub': [0, 1, 1, 1, 3, none],
        2: 'Config(s)',
        'withPreview': [0, 3, 0, 1, 1, 'Preview(s)'], 'withLight': [0, 3, 1, 1, 1, 'Light'], 'previewSub': [1, 3, 2, 1, 2, none],
        'withCamera': [0, 4, 0, 1, 2, 'Camera(s)'],
        'withAsset': [0, 5, 0, 1, 1, 'Asset(s)'], 'assetSub': [0, 5, 1, 1, 3, none],
        'withScenery': [0, 6, 0, 1, 1, 'Scenery(s)'],
        7: 'Action(s)',
        'uploadAnimation': [0, 8, 0, 1, 4, u'Upload ！！！', 'svg_basic@svg#upload']
    }
    #
    dicScExtendUpload = {
        'assemblyComposeUpload': [0, 0, 1, 1, 4, 'Upload / Update Assembly Compose', 'svg_basic@svg#update']
    }
    def __init__(self, *args, **kwargs):
        super(IfScAnimUploadToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnit()
        #
        self.assetCheckResult = False
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        if self._connectObject:
            sceneStage = self._connectObject.sceneStage
            #
            self._scAnimUploadButton.setNameText(
                u'Upload {} ！！！'.format(
                    bscMethods.StrCamelcase.toPrettify(
                        prsMethods.Scene.stageName2linkName(sceneStage)
                    )
                )
            )
            #
            self._initScRangeConfig()
            self._initScUploadConfig()
            #
            self._connectObject._scNoteUiLabel = self._scNoteUiLabel
    #
    def setupBasicTab(self, layout):
        self._scTipToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._scTipToolUiBox)
        self._scTipToolUiBox.setTitle('Tip & Note')
        self.setupTipToolUiBox(self._scTipToolUiBox)
        #
        self._scRangeQtToolbox = qtWidgets.QtToolbox()
        layout.addWidget(self._scRangeQtToolbox)
        self._scRangeQtToolbox.setTitle('Frame & Size')
        self.setupRangeToolUiBox(self._scRangeQtToolbox)
        #
        self._scAnimUploadUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._scAnimUploadUiBox)
        self._scAnimUploadUiBox.setTitle('Upload / Update')
        self.setupScUploadUiBox(self._scAnimUploadUiBox)
    #
    def setupExtendTab(self, layout):
        self._scExtendUploadToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._scExtendUploadToolUiBox)
        self._scExtendUploadToolUiBox.setTitle('Upload / Update')
        self.setupScnExtendUploadToolUiBox(self._scExtendUploadToolUiBox)
    #
    def setupTipToolUiBox(self, toolBox):
        inData = self.dicScTip
        #
        self._scTipUiLabel = qtWidgets.QtTextbrower()
        toolBox.setInfo(inData, 'tips', self._scTipUiLabel)
        self._scTipUiLabel.setEnterEnable(False)
        self._scTipUiLabel.setRule(self.uploadTips)
        #
        self._scNoteUiLabel = qtWidgets.QtTextbrower()
        toolBox.setButton(inData, 'notes', self._scNoteUiLabel)
    #
    def setupRangeToolUiBox(self, toolBox):
        inData = self.dicScRange
        #
        self._scFrameValueLabel = qtWidgets.QtValueEnterlabel()
        toolBox.setInfo(inData, 'animFrame', self._scFrameValueLabel)
        #
        self._scRenderValueLabel = qtWidgets.QtValueEnterlabel()
        toolBox.setInfo(inData, 'renderSize', self._scRenderValueLabel)
    #
    def setupScUploadUiBox(self, toolBox):
        def setupIndexBranch():
            def subRefreshCmd():
                mainCheckButton = self._scWithIndexButton
                checkButtonLis = [self._scIndexWithCameraSubButton, self._scIndexWithAssetSubButton, self._scIndexWithScenerySubButton]
                boolean = mainCheckButton.isChecked()
                for i in checkButtonLis:
                    i.setCheckable(boolean)
                    i.setChecked(boolean)
            #
            self._scWithIndexButton = qtWidgets.QtCheckbutton()
            self._scWithIndexButton.setTooltip(
                u'''是/否更新镜头索引'''
            )
            toolBox.setButton(inData, 'withIndex', self._scWithIndexButton)
            self._scWithIndexButton.clicked.connect(subRefreshCmd)
            #
            indexSubWidget = qtCore.QWidget_()
            indexSubLayout = qtCore.QHBoxLayout_(indexSubWidget)
            toolBox.setButton(inData, 'indexSub', indexSubWidget)
            #
            self._scIndexWithCameraSubButton = qtWidgets.QtCheckbutton()
            indexSubLayout.addWidget(self._scIndexWithCameraSubButton)
            self._scIndexWithCameraSubButton.setNameText('Camera')
            self._scIndexWithCameraSubButton.setChecked(True)
            #
            self._scIndexWithAssetSubButton = qtWidgets.QtCheckbutton()
            indexSubLayout.addWidget(self._scIndexWithAssetSubButton)
            self._scIndexWithAssetSubButton.setNameText('Asset')
            self._scIndexWithAssetSubButton.setChecked(True)
            #
            self._scIndexWithScenerySubButton = qtWidgets.QtCheckbutton()
            indexSubLayout.addWidget(self._scIndexWithScenerySubButton)
            self._scIndexWithScenerySubButton.setNameText('Scenery')
            self._scIndexWithScenerySubButton.setChecked(True)
            #
            subRefreshCmd()
        #
        def setupPreviewBranch():
            def subRefreshCmd():
                mainCheckButton = self._scWithPreviewButton
                checkButtonLis = [self._withLightSubButton, self._aviFormatSubButton, self._movFormatSubButton]
                for i in checkButtonLis:
                    i.setCheckable(mainCheckButton.isChecked())
            #
            self._scWithPreviewButton = qtWidgets.QtCheckbutton()
            self._scWithPreviewButton.setTooltip(
                u'''是/否更新镜头预览'''
            )
            toolBox.setButton(inData, 'withPreview', self._scWithPreviewButton)
            self._scWithPreviewButton.setChecked(True)
            self._scWithPreviewButton.clicked.connect(subRefreshCmd)
            #
            self._withLightSubButton = qtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'withLight', self._withLightSubButton)
            #
            previewSubWidget = qtCore.QWidget_()
            previewSubLayout = qtCore.QHBoxLayout_(previewSubWidget)
            toolBox.setButton(inData, 'previewSub', previewSubWidget)
            #
            self._aviFormatSubButton = qtWidgets.QtRadioCheckbutton()
            previewSubLayout.addWidget(self._aviFormatSubButton)
            self._aviFormatSubButton.setNameText('.avi')
            #
            self._movFormatSubButton = qtWidgets.QtRadioCheckbutton()
            previewSubLayout.addWidget(self._movFormatSubButton)
            self._movFormatSubButton.setNameText('.mov')
            self._movFormatSubButton.setChecked(True)
            #
            subRefreshCmd()
        #
        def setupCameraBranch():
            self._scWithCameraButton = qtWidgets.QtCheckbutton()
            self._scWithCameraButton.setTooltip(
                u'''是/否更新镜头相机'''
            )
            toolBox.setButton(inData, 'withCamera', self._scWithCameraButton)
        #
        def setupAssetBranch():
            def subRefreshCmd():
                mainCheckButton = self._scWithAssetButton
                checkButtonLis = [self._scAstWithModelCacheSubButton, self._scAstWithSolverCacheSubButton, self._scAstWithRigExtraCacheSubButton]
                for i in checkButtonLis:
                    i.setCheckable(mainCheckButton.isChecked())
            #
            self._scWithAssetButton = qtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'withAsset', self._scWithAssetButton)
            self._scWithAssetButton.setTooltip(
                u'''是/否更新镜头资产'''
            )
            #
            assetSubWidget = qtCore.QWidget_()
            assetSubLayout = qtCore.QHBoxLayout_(assetSubWidget)
            toolBox.setButton(inData, 'assetSub', assetSubWidget)
            self._scWithAssetButton.toggled.connect(subRefreshCmd)
            #
            self._scAstWithModelCacheSubButton = qtWidgets.QtCheckbutton()
            assetSubLayout.addWidget(self._scAstWithModelCacheSubButton)
            self._scAstWithModelCacheSubButton.setNameText('Model Cache')
            self._scAstWithModelCacheSubButton.setChecked(True)
            #
            self._scAstWithSolverCacheSubButton = qtWidgets.QtCheckbutton()
            assetSubLayout.addWidget(self._scAstWithSolverCacheSubButton)
            self._scAstWithSolverCacheSubButton.setNameText('Solver Cache')
            self._scAstWithSolverCacheSubButton.setChecked(True)
            #
            self._scAstWithRigExtraCacheSubButton = qtWidgets.QtCheckbutton()
            assetSubLayout.addWidget(self._scAstWithRigExtraCacheSubButton)
            self._scAstWithRigExtraCacheSubButton.setNameText('Extra Cache')
            self._scAstWithRigExtraCacheSubButton.setChecked(True)
            #
            subRefreshCmd()
        #
        inData = self.dicScUpload
        # Index
        setupIndexBranch()
        # Preview
        setupPreviewBranch()
        # Camera
        setupCameraBranch()
        # Asset
        setupAssetBranch()
        #
        self._scWithSceneryButton = qtWidgets.QtCheckbutton()
        self._scWithSceneryButton.setTooltip(
            u'''是/否更新镜头场景'''
        )
        toolBox.setButton(inData, 'withScenery', self._scWithSceneryButton)
        self._scWithSceneryButton.setChecked(True)
        #
        self._scAnimUploadButton = qtWidgets.QtPressbutton()
        self._scAnimUploadButton._setQtPressStatus(qtCore.OnStatus)
        toolBox.setButton(inData, 'uploadAnimation', self._scAnimUploadButton)
        self._scAnimUploadButton.clicked.connect(self._scAnimUploadCmd)
        #
        toolBox.setSeparators(inData)
    #
    def setupScnExtendUploadToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScExtendUpload)
        #
        self._assemblyComposeUploadButton = qtWidgets.QtPressbutton()
        toolBox.addButton('assemblyComposeUpload', self._assemblyComposeUploadButton)
        self._assemblyComposeUploadButton.clicked.connect(self._scAssemblyComposeUploadCmd)
        self._assemblyComposeUploadButton.setTooltip(
            u'''点击 上传 / 更新 组装（场景）构成 数据'''
        )
    #
    def _initScRangeConfig(self):
        projectName = self.projectName
        sceneCategory = self._connectObject.sceneCategory
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        #
        if scenePr.isLayoutLinkName(sceneStage):
            startFrame, endFrame = maUtils.getFrameRange()
            self._scFrameValueLabel.setEnterEnable(True), self._scRenderValueLabel.setEnterEnable(True)
        else:
            self._scFrameValueLabel.setEnterEnable(False), self._scRenderValueLabel.setEnterEnable(False)
            #
            startFrame, endFrame = scenePr.getScUnitFrameRange(
                projectName,
                sceneCategory, sceneName, sceneVariant
            )
        self._scFrameValueLabel.setDefaultValue((startFrame, endFrame))
        self._scRenderValueLabel.setDefaultValue((prsVariants.Util.rndrImageWidth, prsVariants.Util.rndrImageHeight))
    #
    def _initScUploadConfig(self):
        sceneStage = self._connectObject.sceneStage
        if scenePr.isLayoutLinkName(sceneStage) or scenePr.isAnimationLinkName(sceneStage):
            # Camera
            self._scWithCameraButton.setChecked(False), self._scWithCameraButton.setCheckable(True)
            #
            self._scWithAssetButton.setChecked(False), self._scWithAssetButton.setCheckable(True)
            #
            self._scWithSceneryButton.setChecked(True), self._scWithSceneryButton.setCheckable(True)
            #
            if scenePr.isLayoutLinkName(sceneStage):
                self._scWithIndexButton.setChecked(False)
            else:
                self._scWithIndexButton.setChecked(False)
            self._scWithIndexButton.setCheckable(True)
        elif scenePr.isSimulationLinkName(sceneStage):
            self._scWithCameraButton.setChecked(False), self._scWithCameraButton.setCheckable(False)
            #
            self._scWithAssetButton.setChecked(False), self._scWithAssetButton.setCheckable(False)
            #
            self._scWithSceneryButton.setChecked(False), self._scWithSceneryButton.setCheckable(False)
            #
            self._scWithIndexButton.setChecked(False), self._scWithIndexButton.setCheckable(False)
        elif scenePr.isSolverLinkName(sceneStage):
            self._scWithCameraButton.setChecked(False), self._scWithCameraButton.setCheckable(False)
            #
            self._scWithAssetButton.setChecked(False), self._scWithAssetButton.setCheckable(False)
            #
            self._scWithSceneryButton.setChecked(False), self._scWithSceneryButton.setCheckable(False)
            #
            self._scWithIndexButton.setChecked(False), self._scWithIndexButton.setCheckable(False)
        elif scenePr.isLightLinkName(sceneStage):
            self._scWithCameraButton.setChecked(False), self._scWithCameraButton.setCheckable(False)
            #
            self._scWithAssetButton.setChecked(False), self._scWithAssetButton.setCheckable(False)
            #
            self._scWithSceneryButton.setChecked(False), self._scWithSceneryButton.setCheckable(False)
            #
            self._scWithIndexButton.setChecked(False), self._scWithIndexButton.setCheckable(False)
    #
    def _scAnimUploadCmd(self):
        def getIndexUploadDatum():
            mainBoolean = self._scWithIndexButton.isChecked()
            if mainBoolean is True:
                return self._scIndexWithCameraSubButton.isChecked(), self._scIndexWithAssetSubButton.isChecked(), self._scIndexWithScenerySubButton.isChecked()
            else:
                return False
        #
        def getCameraUploadDatum():
            mainBoolean = self._scWithCameraButton.isChecked()
            if mainBoolean is True:
                # Camera Data
                if scenePr.isLayoutLinkName(sceneStage) or scenePr.isAnimationLinkName(sceneStage):
                    sceneCameraLis = datScene.getScActiveCameraLis(sceneName)
                else:
                    sceneCameraLis = datScene.getScOutputCameraLis(sceneName, sceneVariant)
                cameraData = sceneCameraLis, sceneCameraLis
                #
                zAdjust = .0
                cameraConfig = (zAdjust, )
                return cameraData, cameraConfig
            else:
                return False
        #
        def getPreviewUploadDatum():
            mainBoolean = self._scWithPreviewButton.isChecked()
            if mainBoolean is True:
                # Camera Data
                if scenePr.isLayoutLinkName(sceneStage) or scenePr.isAnimationLinkName(sceneStage):
                    sceneCameraLis = datScene.getScActiveCameraLis(sceneName)
                else:
                    sceneCameraLis = datScene.getScOutputCameraLis(sceneName, sceneVariant)
                cameraData = sceneCameraLis, sceneCameraLis
                # Preview Config
                vedioFormat = [prsVariants.Util.aviExt, prsVariants.Util.movExt][self._movFormatSubButton.isChecked()]
                displayMode = [6, 7][self._withLightSubButton.isChecked()]
                useMode = 0
                previewConfig = 100, 100, width, height, vedioFormat, displayMode, useMode
                return cameraData, previewConfig
            else:
                return False
        #
        def getAssetUploadDatum():
            mainBoolean = self._scWithAssetButton.isChecked()
            if mainBoolean is True:
                assetData = self._connectObject._inspectAssetDatumLis
                #
                isAstWithModel = self._scAstWithModelCacheSubButton.isChecked()
                isAstWithSolver = self._scAstWithSolverCacheSubButton.isChecked()
                isAstWithExtra = self._scAstWithRigExtraCacheSubButton.isChecked()
                assetConfig = isAstWithModel, isAstWithSolver, isAstWithExtra
                return assetData, assetConfig
            else:
                return False
        #
        def getSceneryUploadDatum():
            mainBoolean = self._scWithSceneryButton.isChecked()
            if mainBoolean is True:
                return True,
            else:
                return False
        #
        sceneIndex = self._connectObject.sceneIndex
        projectName = self._connectObject.projectName
        sceneCategory = self._connectObject.sceneCategory
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        #
        startFrame, endFrame = self._scFrameValueLabel.value()
        frameOffset = prsVariants.Util.animKeyFrameOffset
        #
        width, height = self._scRenderValueLabel.value()
        #
        description = u'镜头 - 动画 上传/更新'
        notes = self._scNoteUiLabel.datum()
        #
        timeTag = bscMethods.OsTimetag.active()
        #
        isWithIndex = getIndexUploadDatum()
        # Preview
        isWithPreview = getPreviewUploadDatum()
        # Camera
        isWithCamera = getCameraUploadDatum()
        # Asset
        isWithAsset = getAssetUploadDatum()
        # Scenery
        isWithScenery = getSceneryUploadDatum()
        # Log Window
        self._connectObject.hide()
        #
        maScUploadCmds.scUnitAnimationUploadMainCmd(
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame, frameOffset,
            timeTag,
            description, notes,
            withIndex=isWithIndex,
            withPreview=isWithPreview, withCamera=isWithCamera, withAsset=isWithAsset, withScenery=isWithScenery
        )
        #
        timer = threading.Timer(5, self._connectObject.close)
        timer.start()
    #
    def _scAssemblyComposeUploadCmd(self):
        sceneIndex = self._connectObject.sceneIndex
        projectName = self._connectObject.projectName
        sceneCategory = self._connectObject.sceneCategory
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        #
        timeTag = bscMethods.OsTimetag.active()
        #
        maScUploadCmds.scUnitSceneryComposeUploadCmd_(
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            timeTag,
        )
        bscObjects.If_Message(
            u'Upload / Update Assembly Compose Data', u'Complete'
        )
    #
    def setupUnit(self):
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        self.mainLayout().addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Basic', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupBasicTab(layout)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Extend', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupExtendTab(layout)


#
class IfScLightUploadToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    projectName = currentProjectName
    #
    UnitTitle = 'Scene Light Upload'
    panelWidth = 800
    panelHeight = 800
    #
    UnitScriptJobWindowName = 'scLightUploadScriptJobWindow'
    #
    widthSet = 400
    #
    uploadTips = [
        u"提示：",
        u"1：确认不存在错误的 Asset & Cache ；",
        u"2：确认不存在错误的 Render Option ；",
        u"3：点击 Upload ！！！ 上传...",
    ]
    #
    w = 120
    # Tip
    dicScTip = {
        'tips': [10, 0, 0, 1, 4, none],
        'notes': [w, 1, 0, 1, 4, 'Note']
    }
    #
    dicScRenderInfo = {
        'renderer': [w, 0, 0, 1, 4, 'Render Using'],
        'timeUnit': [w, 1, 0, 1, 4, 'FPS'],
        'renderImage': [w, 2, 0, 1, 4, 'Image'],
        'renderCamera': [w, 3, 0, 1, 4, 'Camera(s)'],
        'renderFrame': [w, 4, 0, 1, 4, 'Frame'],
        'renderSize': [w, 5, 0, 1, 4, 'Size']
    }
    #
    dicScWorkspace = {
        'renderPath': [w, 0, 0, 1, 4, 'Render Path'],
        'customize': [w, 1, 0, 1, 4, 'Customize'],
        # 2
        'useLocal': [0, 3, 0, 1, 2, 'Local Root'], 'useServer': [0, 3, 2, 1, 2, 'Server Root'],
        'setRenderPath': [0, 4, 0, 1, 2, 'Set Path', 'svg_basic@svg#refresh'], 'openRenderPath': [0, 4, 2, 1, 2, 'Open Path', 'svg_basic@svg#fileOpen'],
        # 5
        'updateRenderIndex': [0, 6, 0, 1, 4, 'Update Render Index', 'svg_basic@svg#upload']
    }
    # Deadline
    dicDeadlineOption = {
        'ddlJobType': [w, 0, 0, 1, 4, 'Job Type'],
        'ddlJobPool': [w, 1, 0, 1, 4, 'Pool Using'],
        'ddlJobPriority': [w, 2, 0, 1, 4, 'Priority'],
        'ddlJobTimeout': [w, 3, 0, 1, 4, 'Timeout( Minute )'],
        'ddlJobMachineLimit': [w, 4, 0, 1, 4, 'Machine Limit'],
        'ddlJobAbortError': [w, 5, 0, 1, 4, 'Abort Error'],
        'ddlJobWithEachLayer': [w, 6, 0, 1, 2, 'Each Layer'],
        'ddlJobSizePercent': [w, 7, 0, 1, 4, 'Size Percent']
    }
    #
    dicDeadlineSubmit = {
        'submitDeadline': [0, 1, 0, 1, 4, 'Submit Deadline', 'svg_basic@svg#upload']
    }
    #
    dicScUpload = {
        'withLight': [0, 0, 0, 1, 1, 'Light File'], 'withRender': [0, 0, 2, 1, 1, 'Render File'], 'withDeadline': [0, 0, 3, 1, 1, 'Deadline'],
        'updateScene': [0, 1, 0, 1, 4, 'Update Scene', 'svg_basic@svg#upload']
    }
    #
    dicMelCommand = {
        'addToMayaFile': [0, 0, 0, 1, 2, 'Add to Maya'],
        'placeholder': [1, 1, 0, 1, 4, ''],
        # 2
        'save': [0, 3, 0, 1, 2, 'Save', 'maya#savePreset'], 'load': [0, 3, 2, 1, 2, 'Load', 'svg_basic@svg#load']
    }
    #
    percentLis = ['100 %', '75 %', '50 %', '25%']
    percentDic = {'100 %': 1, '75 %': .75, '50 %': .5, '25%': .25}
    def __init__(self, *args, **kwargs):
        super(IfScLightUploadToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.initUnit()
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        if self._connectObject:
            sceneStage = self._connectObject.sceneStage
            if scenePr.isLightLinkName(sceneStage):
                self._initRenderOptionToolUiBox()
                self._initCustomizeToolUiBox()
                self._initDdlOptionToolUiBox()
                self._initDdlSubmitToolUiBox()
                #
                self.setListRenderLayer()
                self.setListFrame()
                #
                self.setScriptJob()
            #
            self._connectObject._scNoteUiLabel = self._scNoteUiLabel
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methods = []
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        self._initRenderOptionScriptJob()
        self._initDdlFrameScriptJob()
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupTipToolUiBox(self, toolBox):
        inData = self.dicScTip
        #
        self._scTipUiLabel = qtWidgets.QtTextbrower()
        toolBox.setInfo(inData, 'tips', self._scTipUiLabel)
        self._scTipUiLabel.setEnterEnable(False)
        self._scTipUiLabel.setRule(self.uploadTips)
        #
        self._scNoteUiLabel = qtWidgets.QtTextbrower()
        toolBox.setButton(inData, 'notes', self._scNoteUiLabel)
    #
    def setupRenderOptionToolUiBox(self, toolBox):
        inData = self.dicScRenderInfo
        #
        self._scRendererLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'renderer', self._scRendererLabel)
        #
        self._scTimeUnitLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'timeUnit', self._scTimeUnitLabel)
        #
        self._scRenderImageLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'renderImage', self._scRenderImageLabel)
        #
        self._scRenderCameraLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'renderCamera', self._scRenderCameraLabel)
        #
        self._scRenderFrameLabel = qtWidgets.QtValueEnterlabel()
        toolBox.setInfo(inData, 'renderFrame', self._scRenderFrameLabel)
        # self._scRenderFrameLabel.setEnterEnable(False)
        #
        self._scRenderSizeBox = qtWidgets.QtValueEnterlabel()
        toolBox.setInfo(inData, 'renderSize', self._scRenderSizeBox)
        # self._scRenderSizeBox.setEnterEnable(False)
    #
    def _initRenderOptionToolUiBox(self):
        projectName = self._connectObject.projectName
        sceneIndex = self._connectObject.sceneIndex
        sceneCategory = self._connectObject.sceneIndex
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        if sceneIndex:
            # Renderer
            renderer = projectPr.getProjectMayaRenderer(projectName)
            self._scRendererLabel.setDefaultDatum(maRender.MaRendererDic[renderer])
            # Time Unit
            timeUnit = projectPr.getProjectMayaTimeUnit(projectName)
            self._scTimeUnitLabel.setDefaultDatum(maPreference.getMayaTimeUnit(timeUnit))
            # Image Path
            imagePrefix = maRender.getImagePrefix()
            self._scRenderImageLabel.setDefaultDatum(imagePrefix)
            # Camera
            outputCameras = scenePr.getOutputCameras(
                projectName,
                sceneCategory, sceneName, sceneVariant
            )
            self._scRenderCameraLabel.setDefaultDatum(outputCameras)
            # Frame
            sceneFrameRange = scenePr.getScUnitFrameRange(
                projectName,
                sceneCategory, sceneName, sceneVariant
            )
            startFrame, endFrame = sceneFrameRange
            self._scRenderFrameLabel.setDefaultValue((startFrame, endFrame))
            # Size
            width = prsVariants.Util.rndrImageWidth
            height = prsVariants.Util.rndrImageHeight
            self._scRenderSizeBox.setDefaultValue((width, height))
    #
    def setupCustomizeToolUiBox(self, toolBox):
        inData = self.dicScWorkspace
        #
        self._scRenderPathLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'renderPath', self._scRenderPathLabel)
        #
        self._scCustomizeLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'customize', self._scCustomizeLabel)
        self._scCustomizeLabel.setEnterEnable(True)
        self._scCustomizeLabel.setChooseEnable(True)
        self._scCustomizeLabel.setTextValidator(48)
        #
        self._scProjectUseLocalButton = qtWidgets.QtRadioCheckbutton()
        toolBox.setButton(inData, 'useLocal', self._scProjectUseLocalButton)
        self._scProjectUseLocalButton.setChecked(True)
        #
        self._scProjectUseServerButton = qtWidgets.QtRadioCheckbutton()
        toolBox.setButton(inData, 'useServer', self._scProjectUseServerButton)
        #
        self.setRenderPathButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'setRenderPath', self.setRenderPathButton)
        #
        self.openRenderPathButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'openRenderPath', self.openRenderPathButton)
        #
        self.updateRenderIndexButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'updateRenderIndex', self.updateRenderIndexButton)
        #
        toolBox.setSeparators(inData)
    #
    def _initCustomizeToolUiBox(self):
        def setWorkSpace():
            customize = datScene.getSceneCustomizeLabel(sceneName)
            #
            rootIndex = [0, 1][self._scProjectUseLocalButton.isChecked()]
            renderPath = scenePr.scUnitRenderFolder(
                rootIndex,
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                customize
            )
            #
            maRender.setCreateWorkspace(renderPath)
        #
        def setUpdateCustomizeLabel():
            string = self._scCustomizeLabel.datum()
            sceneOp.setSceneCustomizeLabel(sceneName, string)
        #
        def setCustomizeLabel():
            serverCustomizes = scenePr.getScRenderCustomizes(
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage
            )
            currentCustomize = datScene.getSceneCustomizeLabel(sceneName)
            #
            if not currentCustomize in serverCustomizes:
                serverCustomizes.insert(0, currentCustomize)
            #
            self._scCustomizeLabel.setDatumLis(serverCustomizes)
            #
            self._scCustomizeLabel.setChoose(currentCustomize)
        #
        def setRenderPath():
            customize = datScene.getSceneCustomizeLabel(sceneName)
            #
            rootIndex = [0, 1][self._scProjectUseLocalButton.isChecked()]
            serverRenderPath = scenePr.scUnitRenderFolder(
                rootIndex,
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                customize
            )
            #
            self._scRenderPathLabel.setDatum(serverRenderPath)
        #
        def openRenderPath():
            renderPath = self._scRenderPathLabel.datum()
            bscMethods.OsDirectory.open(renderPath)
        #
        def setUpdateRenderIndex():
            customize = datScene.getSceneCustomizeLabel(sceneName)
            timeTag = bscMethods.OsTimetag.active()
            #
            startFrame, endFrame = maRender.getRenderTime()
            width, height = maRender.getRenderSize()
            #
            maScUploadCmds.scUnitRenderIndexUploadCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                width, height,
                customize,
                timeTag
            )
            #
            bscObjects.If_Message(
                'Update Scene Render Index',
                'Complete'
            )
        #
        projectName = self._connectObject.projectName
        sceneIndex = self._connectObject.sceneIndex
        sceneCategory = self._connectObject.sceneCategory
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        if sceneIndex:
            setWorkSpace()
            #
            setCustomizeLabel()
            self._scCustomizeLabel.datumChanged.connect(setUpdateCustomizeLabel)
            self._scCustomizeLabel.datumChanged.connect(self._initDdlSubmitToolUiBox)
            #
            setRenderPath()
            self.setRenderPathButton.clicked.connect(setRenderPath)
            self.setRenderPathButton.clicked.connect(setWorkSpace)
            self.setRenderPathButton.clicked.connect(setUpdateCustomizeLabel)
            self.updateRenderIndexButton.clicked.connect(setUpdateRenderIndex)
            #
            self.openRenderPathButton.clicked.connect(openRenderPath)
    #
    def setupUploadToolUiBox(self, toolBox):
        def setUpdateRender():
            projectName = self._connectObject.projectName
            sceneIndex = self._connectObject.sceneIndex
            sceneCategory = self._connectObject.sceneCategory
            sceneName = self._connectObject.sceneName
            sceneVariant = self._connectObject.sceneVariant
            sceneStage = self._connectObject.sceneStage
            if sceneIndex:
                isWithRender = self.withRenderLabel.isChecked()
                isWithDeadline = self.withDeadlineLabel.isChecked()
                #
                if isWithRender:
                    startFrame, endFrame = maRender.getRenderTime()
                    width, height = maRender.getRenderSize()
                    isWithRender = startFrame, endFrame, width, height
                #
                if isWithDeadline is True:
                    ddlJobType = self._ddlJobTypeLabel.datum()
                    ddlJobPool = self._ddlJobPoolLabel.datum()
                    ddlJobPriority = self._ddlJobPriorityLabel.datum()
                    ddlJobTimeout = self._ddlJobTimeoutLabel.datum()
                    ddlJobMachineLimit = self._ddlJobMachineLimitLabel.datum()
                    ddlJobAbortError = self._ddlJobAbortErrorLabel.datum()
                    ddlJobSizePercent = self.percentDic[self._ddlJobSizePercentLabel.datum()]
                    #
                    isWithDeadline = ddlJobType, ddlJobPool, ddlJobPriority, ddlJobTimeout, ddlJobMachineLimit, ddlJobAbortError, ddlJobSizePercent
                #
                customize = datScene.getSceneCustomizeLabel(sceneName)
                timeTag = bscMethods.OsTimetag.active()
                #
                description = u'镜头 - 灯光 / 渲染 上传'
                notes = self._scNoteUiLabel.datum()
                #
                maScUploadCmds.scUnitLightUploadMainCmd(
                    projectName,
                    sceneIndex,
                    sceneCategory, sceneName, sceneVariant, sceneStage,
                    customize,
                    timeTag,
                    description, notes,
                    withRender=isWithRender,
                    withDeadline=isWithDeadline
                )
        #
        inData = self.dicScUpload
        #
        self.withLightLabel = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withLight', self.withLightLabel)
        self.withLightLabel.setTooltip(u'''启用 / 关闭 ：更新 镜头 - 灯光 文件''')
        self.withLightLabel.setChecked(True)
        #
        self.withRenderLabel = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withRender', self.withRenderLabel)
        self.withRenderLabel.setTooltip(u'''启用 / 关闭 ：更新 镜头 - 渲染 文件''')
        self.withRenderLabel.setChecked(True)
        #
        self.withDeadlineLabel = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withDeadline', self.withDeadlineLabel)
        self.withDeadlineLabel.setTooltip(u'''启用 / 关闭 ：发布 镜头 - 渲染（Deadline）任务''')
        self.withRenderLabel.toggled.connect(self.withDeadlineLabel.setCheckable)
        #
        self._scLightUpdateButton = qtWidgets.QtPressbutton()
        self._scLightUpdateButton._setQtPressStatus(qtCore.OnStatus)
        toolBox.setButton(inData, 'updateScene', self._scLightUpdateButton)
        self._scLightUpdateButton.clicked.connect(setUpdateRender)
    #
    def _initRenderOptionScriptJob(self):
        def setRenderer():
            renderer = maRender.getCurrentRenderer()
            self._scRendererLabel.setDatum(renderer)
        #
        def setRendererScriptJob():
            maUtils.setCreateAttrChangedScriptJob(
                self.UnitScriptJobWindowName,
                maRender.MaNodeAttrRenderOptionDic['renderer'],
                setRenderer
            )
        #
        def setTimeUnit():
            timeUnit = maUtils.getTimeUnit()
            self._scTimeUnitLabel.setDatum(timeUnit)
        #
        def setTimeUnitScriptJob():
            maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, 'timeUnitChanged', [setTimeUnit, setRenderTime])
        #
        def setRenderCamera():
            def subMethod():
                renderCameras = maRender.getRenderableCameraLis(fullPath=False)
                self._scRenderCameraLabel.setDatum(renderCameras)
            #
            maRender.setCreateRenderCameraScriptJob(self.UnitScriptJobWindowName, subMethod)
            #
            subMethod()
        #
        def setRenderCameraScriptJob():
            maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, 'cameraChange', setRenderCamera)
        #
        def setRenderTime():
            startFrame, endFrame = maRender.getRenderTime()
            self._scRenderFrameLabel.setValue((startFrame, endFrame))
        #
        def setRenderTimeScriptJob():
            maUtils.setCreateAttrChangedScriptJob(
                self.UnitScriptJobWindowName,
                maRender.MaNodeAttrRenderOptionDic['startFrame'],
                setRenderTime
            )
            maUtils.setCreateAttrChangedScriptJob(
                self.UnitScriptJobWindowName,
                maRender.MaNodeAttrRenderOptionDic['endFrame'],
                setRenderTime
            )
        #
        def setRenderSize():
            width, height = maRender.getRenderSize()
            self._scRenderSizeBox.setValue((width, height))
        #
        def setRenderSizeScriptJob():
            maUtils.setCreateAttrChangedScriptJob(
                self.UnitScriptJobWindowName,
                maRender.MaNodeAttrRenderOptionDic['imageWidth'],
                setRenderSize
            )
            maUtils.setCreateAttrChangedScriptJob(
                self.UnitScriptJobWindowName,
                maRender.MaNodeAttrRenderOptionDic['imageHeight'],
                setRenderSize
            )
        #
        setRendererScriptJob()
        setRenderer()
        #
        setTimeUnitScriptJob()
        setTimeUnit()
        #
        setRenderCameraScriptJob()
        setRenderCamera()
        #
        setRenderTimeScriptJob()
        setRenderTime()
        #
        setRenderSizeScriptJob()
        setRenderSize()
    #
    def setupDdlOptionToolUiBox(self, toolBox):
        inData = self.dicDeadlineOption
        #
        self._ddlJobTypeLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'ddlJobType', self._ddlJobTypeLabel)
        self._ddlJobTypeLabel.setChooseEnable(True)
        #
        self._ddlJobPoolLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'ddlJobPool', self._ddlJobPoolLabel)
        self._ddlJobPoolLabel.setChooseEnable(True)
        #
        self._ddlJobPriorityLabel = qtWidgets.QtValueEnterlabel()
        toolBox.setInfo(inData, 'ddlJobPriority', self._ddlJobPriorityLabel)
        self._ddlJobPriorityLabel.setEnterEnable(True)
        self._ddlJobPriorityLabel.setDefaultValue(50)
        self._ddlJobPriorityLabel.setValueRange(0, 100)
        #
        self._ddlJobTimeoutLabel = qtWidgets.QtValueEnterlabel()
        toolBox.setInfo(inData, 'ddlJobTimeout', self._ddlJobTimeoutLabel)
        self._ddlJobTimeoutLabel.setEnterEnable(True)
        self._ddlJobTimeoutLabel.setDefaultValue(4000)
        self._ddlJobTimeoutLabel.setValueRange(0, 5000)
        #
        self._ddlJobMachineLimitLabel = qtWidgets.QtValueEnterlabel()
        toolBox.setInfo(inData, 'ddlJobMachineLimit', self._ddlJobMachineLimitLabel)
        self._ddlJobMachineLimitLabel.setEnterEnable(True)
        self._ddlJobMachineLimitLabel.setDefaultValue(20)
        self._ddlJobMachineLimitLabel.setValueRange(0, 100)
        #
        self._ddlJobAbortErrorLabel = qtWidgets.QtValueEnterlabel()
        toolBox.setInfo(inData, 'ddlJobAbortError', self._ddlJobAbortErrorLabel)
        self._ddlJobAbortErrorLabel.setEnterEnable(True)
        self._ddlJobAbortErrorLabel.setDefaultValue(1)
        self._ddlJobAbortErrorLabel.setValueRange(0, 2)
        #
        self._ddlJobWithEachLayerButton = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'ddlJobWithEachLayer', self._ddlJobWithEachLayerButton)
        self._ddlJobWithEachLayerButton.setCheckEnable(True)
        self._ddlJobWithEachLayerButton.setChecked(True)
        #
        self._ddlJobSizePercentLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'ddlJobSizePercent', self._ddlJobSizePercentLabel)
        self._ddlJobSizePercentLabel.setChooseEnable(True)
        #
        toolBox.setSeparators(inData)
    #
    def _initDdlOptionToolUiBox(self):
        renderPools = ddlCommands.getDdlPools()
        #
        self._ddlJobTypeLabel.setDatumLis(appCfg.DdlJobs)
        self._ddlJobTypeLabel.setChoose(appCfg.DdlMaCmdJob)
        #
        self._ddlJobPoolLabel.setDatumLis(renderPools)
        self._ddlJobPoolLabel.setChoose('all')
        #
        self._ddlJobPriorityLabel.setValue(50)
        #
        self._ddlJobTimeoutLabel.setValue(4000)
        #
        self._ddlJobMachineLimitLabel.setValue(20)
        #
        self._ddlJobAbortErrorLabel.setValue(1)
        #
        self._ddlJobSizePercentLabel.setDatumLis(self.percentLis)
        self._ddlJobSizePercentLabel.setChoose(self.percentLis[0])
    #
    def setupDdlRenderLayerToolUiBox(self, toolBox):
        self._renderLayerTreeView = qtWidgets.QtTreeview()
        self._renderLayerTreeView.setCheckEnable(True)
        toolBox.addWidget(self._renderLayerTreeView)
    #
    def setupDdlFrameTooUiBox(self, toolBox):
        def setActionData():
            def checkOddFrameCmd():
                treeView.setUncheckAll()
                [i.setChecked(True) for i in treeView.items() if int(i.name()) % 2 == 0]
            #
            def checkEvenFrameCmd():
                treeView.setUncheckAll()
                [i.setChecked(True) for i in treeView.items() if int(i.name()) % 2 == 1]
            #
            def checkKeyFrameCmd():
                treeView.setUncheckAll()
                #
                startFrame, endFrame = maRender.getRenderTime()
                midFrame = int((endFrame - startFrame) / 2 + startFrame)
                frameRange = [startFrame, midFrame, endFrame]
                #
                [i.setChecked(True) for i in treeView.items() if int(i.name()) in frameRange]

            #
            actionDatumLis = [
                ('Extend Check', ),
                ('Check Odd Frame', 'svg_basic@svg#checkedAll', True, checkOddFrameCmd),
                ('Check Even Frame', 'svg_basic@svg#checkedAll', True, checkEvenFrameCmd),
                (),
                ('Check Key Frame', 'svg_basic@svg#checkedAll', True, checkKeyFrameCmd)
            ]
            #
            treeView = self._frameTreeView
            #
            treeView.setActionData(actionDatumLis)
        #
        self._frameTreeView = qtWidgets.QtTreeview()
        self._frameTreeView.setCheckEnable(True)
        toolBox.addWidget(self._frameTreeView)
        #
        setActionData()
    #
    def _initDdlFrameScriptJob(self):
        maUtils.setCreateAttrChangedScriptJob(
            self.UnitScriptJobWindowName,
            maRender.MaNodeAttrRenderOptionDic['startFrame'],
            self.setListFrame
        )
        maUtils.setCreateAttrChangedScriptJob(
            self.UnitScriptJobWindowName,
            maRender.MaNodeAttrRenderOptionDic['endFrame'],
            self.setListFrame
        )
    #
    def setupDdlMelCommandToolUiBox(self, toolBox):
        def saveCmd():
            fileString_ = self._melCommandFile
            data = self._commandEditBox.text()
            bscMethods.OsFile.write(self._melCommandFile, data)
            #
            subOsFile = bscMethods.OsFile.toJoinTimetag(fileString_)
            bscMethods.OsFile.copyTo(fileString_, subOsFile)
            #
            setLoadAction()
            #
            bscObjects.If_Message('Save Mel Command', 'Complete !!!')
        #
        def loadCmd():
            fileString_ = self._melCommandFile
            if bscMethods.OsFile.isExist(fileString_):
                data = bscMethods.OsFile.read(fileString_)
                #
                self._commandEditBox.setText(data)
        #
        def setLoadAction():
            def setActionBranch(timeTag, subOsFile):
                def subLoadCmd():
                    if bscMethods.OsFile.isExist(subOsFile):
                        subData = bscMethods.OsFile.read(subOsFile)
                        #
                        self._commandEditBox.setText(subData)
                #
                actionExplain = bscMethods.OsTimetag.toChnPrettify(timeTag)
                actionDatumLis.append(
                    (actionExplain, 'svg_basic@svg#file', True, subLoadCmd)
                )
            #
            actionDatumLis = [
                ('Basic', ),
                ('Save', 'menu#saveMenu', True, saveCmd),
                ('Load ( Last Save )', 'menu#loadMenu', True, loadCmd),
                ('History', )
            ]
            fileString_ = self._melCommandFile
            #
            recordDic = bscMethods.OsFile.backupNameDict(fileString_)
            if recordDic:
                for k, v in recordDic.items()[-5:]:
                    setActionBranch(k, v)
            #
            toolBox.setActionData(
                actionDatumLis
            )
        #
        def setRenderPreMelCommand():
            if self._addToMayaButton.isChecked():
                data = self._commandEditBox.text()
                maRender.setRenderPreMelCommand(data)
        #
        self._melCommandFile = '{}/{}/maya.mel/deadline.mel'.format(
            lxScheme.UserPreset().renderCommandDirectory, self.projectName
        )
        #
        inData = self.dicMelCommand
        #
        self._addToMayaButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'addToMayaFile', self._addToMayaButton)
        self._addToMayaButton.setChecked(False)
        self._addToMayaButton.clicked.connect(setRenderPreMelCommand)
        #
        self._commandEditBox = qtWidgets.QtTextbrower()
        toolBox.addWidget(self._commandEditBox, 1, 0, 1, 4)
        self._commandEditBox.textEdit().entryChanged.connect(setRenderPreMelCommand)
        #
        self._commandSaveButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'save', self._commandSaveButton)
        self._commandSaveButton.clicked.connect(saveCmd)
        #
        self._commandLoadButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'load', self._commandLoadButton)
        self._commandLoadButton.clicked.connect(loadCmd)
        #
        toolBox.setSeparators(inData)
        #
        loadCmd()
        setLoadAction()
    #
    def _initDdlMelCommandScriptJob(self):
        pass
    #
    def setupDdlSubmitToolUiBox(self, toolBox):
        def scSubmitDeadlineCmd():
            projectName = self._connectObject.projectName
            sceneIndex = self._connectObject.sceneIndex
            sceneCategory = self._connectObject.sceneCategory
            sceneName = self._connectObject.sceneName
            sceneVariant = self._connectObject.sceneVariant
            sceneStage = self._connectObject.sceneStage
            #
            customize = datScene.getSceneCustomizeLabel(sceneName)
            timeTag = bscMethods.OsTimetag.active()
            #
            startFrame, endFrame = maRender.getRenderTime()
            width, height = maRender.getRenderSize()
            #
            ddlJobType = self._ddlJobTypeLabel.datum()
            ddlJobPool = self._ddlJobPoolLabel.datum()
            ddlJobPriority = self._ddlJobPriorityLabel.datum()
            ddlJobTimeout = self._ddlJobTimeoutLabel.datum()
            ddlJobMachineLimit = self._ddlJobMachineLimitLabel.datum()
            ddlJobAbortError = self._ddlJobAbortErrorLabel.datum()
            ddlJobSizePercent = self.percentDic[self._ddlJobSizePercentLabel.datum()]
            #
            deadlineVars = ddlJobType, ddlJobPool, ddlJobPriority, ddlJobTimeout, ddlJobMachineLimit, ddlJobAbortError, ddlJobSizePercent
            overrideRenderLayerLis = self.getOverrideRenderLayerLis()
            overrideFrameLis = self.getOverrideFrameLis()
            melCommandString = [self.getMelCommandString(), None][self._addToMayaButton.isChecked()]
            #
            maScUploadCmds.scUnitRenderDeadlineSubmitMainCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                width, height,
                timeTag,
                customize,
                deadlineVars,
                renderLayerOverride=overrideRenderLayerLis, frameOverride=overrideFrameLis, melCommand=melCommandString
             )
            #
            bscObjects.If_Message(
                'Update Scene Render Index',
                'Complete'
            )
        inData = self.dicDeadlineSubmit
        #
        self._ddlSubmitButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'submitDeadline', self._ddlSubmitButton)
        self._ddlSubmitButton.clicked.connect(scSubmitDeadlineCmd)
    #
    def _initDdlSubmitToolUiBox(self):
        if self._connectObject:
            projectName = self._connectObject.projectName
            sceneIndex = self._connectObject.sceneIndex
            sceneCategory = self._connectObject.sceneCategory
            sceneName = self._connectObject.sceneName
            sceneVariant = self._connectObject.sceneVariant
            sceneStage = self._connectObject.sceneStage
            #
            customize = self._scCustomizeLabel.datum()
            #
            renderFile = scenePr.scUnitRenderFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage, customize
            )[1]
            #
            self._ddlSubmitButton.setPressable([False, True][bscMethods.OsFile.isExist(renderFile)])
    #
    def setListRenderLayer(self):
        def setBranch(renderLayer):
            def updateRenderable():
                boolean = maUtils.getAttrDatum(renderLayer, enabledAttrName)
                rgba = [(95, 95, 95, 255), (63, 255, 127, 255)][boolean]
                #
                treeItem.setIcon('svg_basic@svg#render')
                #
                treeItem.setFilterColor(rgba)
                treeItem.setCheckable(boolean)
                treeItem.setChecked(boolean)
            #
            treeItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(treeItem)
            treeItem.setName(renderLayer)
            treeItem.setNameText([renderLayer, 'masterLayer'][renderLayer == 'defaultRenderLayer'])
            #
            treeItem.path = renderLayer
            #
            enabledAttr = renderLayer + '.' + enabledAttrName
            #
            maUtils.setCreateAttrChangedScriptJob(
                self.UnitScriptJobWindowName,
                enabledAttr,
                updateRenderable
            )
            #
            updateRenderable()
        #
        enabledAttrName = 'renderable'
        #
        treeView = self._renderLayerTreeView
        renderLayers = maRender.getRenderLayers()
        #
        treeView.cleanItems()
        if renderLayers:
            [setBranch(i) for i in renderLayers]
        treeView.setRefresh()
    #
    def setListFrame(self):
        def setBranch(frame):
            treeItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(treeItem)
            treeItem.setName(str(frame))
            treeItem.setChecked(True)
            treeItem.setIcon('object#pictureFile')
            #
            if frame in sceneFrameLis and frame in renderFrameLis:
                treeItem.setFilterColor((63, 255, 127, 255))
            elif frame in sceneFrameLis and not frame in renderFrameLis:
                treeItem.setFilterColor((255, 0, 63, 255))
            else:
                treeItem.setFilterColor((95, 95, 95, 255))
        #
        projectName = self._connectObject.projectName
        sceneIndex = self._connectObject.sceneIndex
        sceneCategory = self._connectObject.sceneIndex
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        #
        treeView = self._frameTreeView
        #
        sceneStartFrame, sceneEndFrame = scenePr.getScUnitFrameRange(
            projectName,
            sceneCategory, sceneName, sceneVariant
        )
        renderStartFrame, renderEndFrame = maRender.getRenderTime()
        #
        sceneFrameLis = range(sceneStartFrame, sceneEndFrame + 1)
        renderFrameLis = range(renderStartFrame, renderEndFrame + 1)
        #
        frameLis = []
        [frameLis.append(i) for i in sceneFrameLis if i not in frameLis]
        [frameLis.append(i) for i in renderFrameLis if i not in frameLis]
        #
        frameLis.sort()
        #
        treeView.cleanItems()
        for i in frameLis:
            setBranch(i)
        #
        treeView.setRefresh()
    #
    def getOverrideRenderLayerLis(self):
        lis = []
        treeBox = self._renderLayerTreeView
        checkedItems = treeBox.checkedItems()
        if checkedItems:
            lis = [i.name() for i in checkedItems]
        return lis
    #
    def getOverrideFrameLis(self):
        lis = []
        treeBox = self._frameTreeView
        checkedItems = treeBox.checkedItems()
        if checkedItems:
            lis = [i.name() for i in checkedItems]
        return lis
    #
    def getMelCommandString(self):
        return self._commandEditBox.text()
    #
    def initUnit(self):
        pass
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        layout.addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        #
        self._tabWidget.currentChanged.connect(self._initDdlSubmitToolUiBox)
        #
        renderScrollBox = qtCore.QScrollArea_()
        self._tabWidget.addTab(renderScrollBox, 'Render', 'svg_basic@svg#tab')
        renderScrollBox.setSpacing(2)
        #
        deadlineScrollBox = qtCore.QScrollArea_()
        self._tabWidget.addTab(deadlineScrollBox, 'Deadline', 'svg_basic@svg#tab')
        deadlineScrollBox.setSpacing(2)
        #
        toolBox = qtWidgets.QtToolbox()
        renderScrollBox.addWidget(toolBox)
        toolBox.setTitle('Tip & Note', 1)
        self.setupTipToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        renderScrollBox.addWidget(toolBox)
        toolBox.setTitle('Render Option')
        self.setupRenderOptionToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        renderScrollBox.addWidget(toolBox)
        toolBox.setTitle('Customize')
        self.setupCustomizeToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        renderScrollBox.addWidget(toolBox)
        toolBox.setTitle('Upload / Update')
        self.setupUploadToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        deadlineScrollBox.addWidget(toolBox)
        toolBox.setTitle('Option')
        self.setupDdlOptionToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        deadlineScrollBox.addWidget(toolBox)
        toolBox.setTitle('Render Layer')
        toolBox.setExpanded(False)
        self.setupDdlRenderLayerToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        deadlineScrollBox.addWidget(toolBox)
        toolBox.setTitle('Frame')
        toolBox.setExpanded(False)
        self.setupDdlFrameTooUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        deadlineScrollBox.addWidget(toolBox)
        toolBox.setTitle('Mel Command')
        self.setupDdlMelCommandToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        deadlineScrollBox.addWidget(toolBox)
        toolBox.setTitle('Submit')
        self.setupDdlSubmitToolUiBox(toolBox)


#
class IfScAnimManagerUnit(_qtIfAbcWidget.IfToolUnitBasic):
    projectName = currentProjectName
    #
    UnitTitle = 'Scene Animation Manager'
    panelWidth = 800
    panelHeight = 800
    #
    UnitScriptJobWindowName = 'animationManageScriptJobWindow'
    #
    animExportTips = [
        u"提示： ",
        u"1：选择（ 单个 ） Asset ( Rig ) ； ",
        u"2：点击 Export / Import Animation ( Keys ) 导出 / 导入... ",
    ]
    #
    widthSet = 800
    #
    w = 80
    # Scene
    dicScene = {
        'project': [w, 0, 0, 1, 4, 'Project'],
        'classify': [w, 1, 0, 1, 4, 'Classify'],
        'name': [w, 2, 0, 1, 4, 'Name'],
        'variant': [w, 3, 0, 1, 4, 'Variant'],
        'stage': [w, 4, 0, 1, 4, 'State']
    }
    # View
    dicView = {
        'namespace': [w, 0, 0, 1, 4, 'Namespace'],
        'file': [w, 1, 0, 1, 4, 'File'],
        'placeholder': [1, 3, 0, 1, 4, 'Placeholder']
    }
    # 2
    # Namespace
    dicNamespace = {
        'reduceAssetNamespaceHierarchy': [1, 0, 0, 1, 4, 'Assets ( Rig ) Namespace - Hierarchy']
    }
    # Constant
    dicCheck = {
        'reduceAssetFile': [0, 0, 0, 1, 4, 'Rig(s) Directory'],
        'reduceAssetNumber': [1, 1, 0, 1, 4, 'Rig(s) Number'],
        'reduceAssetNamespaceNaming': [0, 2, 0, 1, 4, 'Rig(s) Namespace - Naming'],
        'clearAssetHierarchy': [0, 3, 0, 1, 4, 'Rig(s) Hierarchy']
    }
    #
    dicModify = {
        0: 'Variant',
        'variant': [0, 1, 0, 1, 2, 'Variant'], 'setVariant': [1, 1, 2, 1, 2, 'Set Variant', 'svg_basic@svg#switch'],
        2: 'Number',
        'number': [0, 3, 0, 1, 2, 'Number'], 'setNumber': [0, 3, 2, 1, 2, 'Set Number', 'svg_basic@svg#switch'],
        'placeholder': [0, 4, 0, 1, 4, 'Placeholder']
    }
    #
    dicSwitch = {
        'switchToLow': [0, 0, 0, 1, 2, 'Low - Quality [ 0000 ]', 'svg_basic@svg#switch'], 'switchToHigh': [0, 0, 2, 1, 2, 'High - Quality [ 0000 ]', 'svg_basic@svg#switch'],
        #
        'switchToGpu': [0, 2, 0, 1, 2, 'GPU [ 0000 ]', 'svg_basic@svg#switch'], 'switchToRig': [0, 2, 2, 1, 2, 'Rig [ 0000 ]', 'svg_basic@svg#switch'],
        'placeholder': [0, 3, 0, 1, 4, 'Placeholder']
    }
    #
    dicAnim = {
        'root': [0, 0, 0, 1, 4, u'  Root...'],
        'tips': [0, 1, 0, 1, 4, None],
        'autoRoot': [0, 2, 0, 1, 2, 'Automatic Root'],
        'exportAnimation': [0, 3, 0, 1, 2, 'Export Animation Key(s)'], 'importAnimation': [0, 3, 2, 1, 2, 'Import Animation Key(s)'],
        'transferAnimation': [1, 4, 0, 1, 4, 'Transfer Animation'],
        'from': [w, 5, 0, 1, 4, 'From'],
        'to': [w, 6, 0, 1, 4, 'To']
    }
    #
    statisticsConfig = ['worldArea', 'shell', 'vertex', 'edge', 'face', 'triangle']
    def __init__(self, *args, **kwargs):
        super(IfScAnimManagerUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.selectedAsset = []
        #
        self.sceneFullName = none
        #
        self.sceneIndex = None
        self.sceneCategory = None
        self.sceneName = None
        self.sceneVariant = None
        self.sceneStage = None
        #
        self.setupUnit()
        #
        self.getSceneInfo()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        if self._connectObject:
            #
            self.setViewConstant()
            self.setScriptJob()
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methods = [self.getSelRig, self.setAnimExpBtnState]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupLeftWidget(self, layout):
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        layout.addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        #
        self.modifyToolRefreshEnable = False
        self.switchToolRefreshEnable = False
        self.actToolRefreshEnable = False
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Basic', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupConstantTab(layout)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Extend', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupModifyTab(layout)
        #
        self._tabWidget.currentChanged.connect(self.setRefreshEnableSwitch)
        self._tabWidget.currentChanged.connect(self.setRefreshUiState)
    # Constant Tab
    def setupConstantTab(self, layout):
        toolBox = qtWidgets.QtToolbox()
        #
        layout.addWidget(toolBox)
        toolBox.setTitle('Assets ( Rig ) Constant')
        self.setupChartToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Assets ( Rig ) Namespace')
        self.setupNamespaceToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Assets ( Rig ) Check')
        self.setupCheckToolUiBox(toolBox)
    #
    def setupChartToolUiBox(self, toolBox):
        self._astModelSectorChart = qtWidgets.QtSectorchart()
        toolBox.addWidget(self._astModelSectorChart, 0, 0, 1, 4)
    #
    def setupCheckToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicCheck)
        #
        self.reduceAssetFileButton = qtWidgets.QtPressbutton()
        self.reduceAssetFileButton.setPercentEnable(True)
        toolBox.addButton('reduceAssetFile', self.reduceAssetFileButton)
        self.reduceAssetFileButton.setTooltip('''Reduce Assets's ( Rig ) Directory''')
        self.reduceAssetFileButton.clicked.connect(self.setReduceAssetDirectory)
        #
        self.reduceAssetNumberButton = qtWidgets.QtPressbutton()
        self.reduceAssetNumberButton.setPercentEnable(True)
        toolBox.addButton('reduceAssetNumber', self.reduceAssetNumberButton)
        self.reduceAssetNumberButton.setTooltip('''Reduce Assets's ( Rig ) Number''')
        self.reduceAssetNumberButton.clicked.connect(self.setAssetNumbers)
        #
        self.reduceAssetNamespaceNamingButton = qtWidgets.QtPressbutton()
        self.reduceAssetNamespaceNamingButton.setPercentEnable(True)
        toolBox.addButton('reduceAssetNamespaceNaming', self.reduceAssetNamespaceNamingButton)
        self.reduceAssetNamespaceNamingButton.setTooltip('''Reduce Assets's ( Rig ) Namespace Naming''')
        self.reduceAssetNamespaceNamingButton.clicked.connect(self.setReduceAssetNamespaceNaming)
        #
        self.clearAssetHierarchyButton = qtWidgets.QtPressbutton()
        self.clearAssetHierarchyButton.setPercentEnable(True)
        toolBox.addButton('clearAssetHierarchy', self.clearAssetHierarchyButton)
        self.clearAssetHierarchyButton.setTooltip('''Clear Assets's ( Rig ) Hierarchy''')
        #
        toolBox.addSeparators()
    #
    def setupNamespaceToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicNamespace)
        #
        self.reduceAssetNamespaceHierarchyButton = qtWidgets.QtPressbutton()
        self.reduceAssetNamespaceHierarchyButton.setPercentEnable(True)
        toolBox.addButton('reduceAssetNamespaceHierarchy', self.reduceAssetNamespaceHierarchyButton)
        self.reduceAssetNamespaceHierarchyButton.setTooltip('''Reduce Assets's ( Rig ) Namespace Hierarchy''')
        self.reduceAssetNamespaceHierarchyButton.clicked.connect(self.setReduceAssetNamespaceHierarchy)
        #
        toolBox.addSeparators()
    # Modify Tab
    def setupModifyTab(self, layout):
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Modify')
        self.setupModifyToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Switch')
        self.setupSwitchToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Animation Key(s) Export')
        self.setupAnimExportToolUiBox(toolBox)
    #
    def setupModifyToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicModify)
        #
        self.variantLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('variant', self.variantLabel)
        self.variantLabel.setChooseEnable(True)
        self.variantLabel.setDatum(prsVariants.Util.astDefaultVersion)
        #
        self.setVariantButton = qtWidgets.QtPressbutton()
        toolBox.addButton('setVariant', self.setVariantButton)
        self.setVariantButton.clicked.connect(self.setAssetVariant)
        #
        self.numberLabel = qtWidgets.QtValueEnterlabel()
        toolBox.addInfo('number', self.numberLabel)
        self.numberLabel.setDefaultValue(0)
        self.numberLabel.setValue(0)
        #
        self.setNumberButton = qtWidgets.QtPressbutton()
        toolBox.addButton('setNumber', self.setNumberButton)
        self.setNumberButton.clicked.connect(self.setAssetNumber)
        #
        toolBox.addSeparators()
    #
    def setupSwitchToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicSwitch)
        #
        self.switchToLowButton = qtWidgets.QtPressbutton()
        toolBox.addButton('switchToLow', self.switchToLowButton)
        self.switchToLowButton.setTooltip('''Switch Rig to Low - Quality''')
        self.switchToLowButton.clicked.connect(self.setRigSwitchToLow)
        #
        self.switchToHighButton = qtWidgets.QtPressbutton()
        toolBox.addButton('switchToHigh', self.switchToHighButton)
        self.switchToHighButton.setTooltip('''Switch Rig to High - Quality''')
        self.switchToHighButton.clicked.connect(self.setRigSwitchToHigh)
        #
        self.switchToGpuButton = qtWidgets.QtPressbutton()
        toolBox.addButton('switchToGpu', self.switchToGpuButton)
        self.switchToGpuButton.setTooltip('''Switch Rig to GPU''')
        self.switchToGpuButton.clicked.connect(self.setRigSwitchToGpu)
        #
        self.switchToRigButton = qtWidgets.QtPressbutton()
        toolBox.addButton('switchToRig', self.switchToRigButton)
        self.switchToRigButton.setTooltip('''Switch GPU to Rig''')
        self.switchToRigButton.clicked.connect(self.setGpuSwitchToRig)
        #
        toolBox.addSeparators()
    #
    def setRefreshEnableSwitch(self):
        tabWidget = self._tabWidget
        self.modifyToolRefreshEnable = tabWidget.currentIndex() == 1
        self.switchToolRefreshEnable = tabWidget.currentIndex() == 1
    #
    def setupAnimExportToolUiBox(self, toolBox):
        self.root = None
        #
        toolBox.setUiData(self.dicAnim)
        #
        self.rootLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('root', self.rootLabel)
        #
        self.animExportTipsLabel = qtWidgets.QtTextbrower()
        toolBox.addInfo('tips', self.animExportTipsLabel)
        self.animExportTipsLabel.setEnterEnable(False)
        self.animExportTipsLabel.setRule(self.animExportTips)
        #
        self.autoRootButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('autoRoot', self.autoRootButton)
        self.autoRootButton.setChecked(True)
        self.autoRootButton.toggled.connect(self.setAnimExpBtnState)
        #
        self.exportAnimationButton = qtWidgets.QtPressbutton()
        toolBox.addButton('exportAnimation', self.exportAnimationButton)
        self.exportAnimationButton.clicked.connect(self.setExportAnimation)
        #
        self.importAnimationButton = qtWidgets.QtPressbutton()
        toolBox.addButton('importAnimation', self.importAnimationButton)
        self.importAnimationButton.clicked.connect(self.setImportAnimation)
        #
        self.transferAnimationButton = qtWidgets.QtPressbutton()
        # toolBox.addButton('transferAnimation', self.transferAnimationButton)
        self.transferAnimationButton.clicked.connect(self.setTransferAnimation)
        #
        self.fromLabel = qtWidgets.QtEnterlabel()
        # toolBox.addInfo('from', self.fromLabel)
        #
        self.toLabel = qtWidgets.QtEnterlabel()
        # toolBox.addInfo('to', self.toLabel)
    #
    def setupRightWidget(self, layout):
        self._rightTreeView = qtWidgets_.QTreeWidget_()
        layout.addWidget(self._rightTreeView)
        self.setupRightTreeWidget(self._rightTreeView)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Information')
        self.setupRightBottomToolUiBox(toolBox)
    #
    def setupRightBottomToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicView)
        #
        self.namespaceLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('namespace', self.namespaceLabel)
        #
        self.fileLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('file', self.fileLabel)
    #
    def setupRightTreeWidget(self, treeBox):
        self.selectedAssetItem = None
        self.assetTreeItems = []
        #
        self.assetDataDic = {}
        self.gpuDataDic = {}
        #
        self.animRigItems = []
        self.layRigItems = []
        #
        self.rigItems = []
        self.gpuItems = []
        #
        maxWidth = self.widthSet
        treeBox.setColumns(['Asset ( Rig )', 'State', 'Status'], [4, 2, 2], maxWidth)
        #
        treeBox.itemSelectionChanged.connect(self.setAssetSelect)
        #
        treeBox.itemSelectionChanged.connect(self.setBtnState)
        treeBox.itemSelectionChanged.connect(self.setMdfBtnState)
        treeBox.itemSelectionChanged.connect(self.setSwtBtnState)
    # UI View
    def getSceneInfo(self):
        sceneInfoLis = datScene.getSceneInfo()
        if sceneInfoLis:
            sceneInfo = sceneInfoLis[0]
            sceneIndex, sceneCategory, sceneName, sceneVariant, sceneStage = sceneInfo
            #
            self.sceneIndex = sceneIndex
            self.sceneCategory = sceneCategory
            self.sceneName = sceneName
            self.sceneVariant = sceneVariant
            self.sceneStage = sceneStage
            #
            self.sceneFullName = scenePr.sceneFullName(sceneName, sceneVariant)
    #
    def setListAsset(self):
        self.assetTreeItems = []
        #
        self.assetDataDic = {}
        #
        numberKeyArray = []
        #
        treeBox = self._rightTreeView
        #
        projectName = self.projectName
        inData = datAnim.getReferenceDic(projectName)
        #
        treeBox.clear()
        if inData:
            maxValue = len(inData)
            for seq, (k, v) in enumerate(inData.items()):
                if self._connectObject:
                    self._connectObject.setProgressValue(seq + 1, maxValue)
                referenceNode = k
                assetCategory, assetName, number, assetVariant, state = v
                assetItem = qtWidgets_.QTreeWidgetItem_()
                #
                treeBox.addItem(assetItem)
                #
                assetIcon = 'treeBox#rig'
                stateIcon = 'treeBox#reference'
                assetSubLabel = none
                stateSubLabel = none
                #
                if state == 'Unloaded':
                    assetSubLabel = 'off'
                    stateSubLabel = 'off'
                #
                if state == 'Loaded':
                    assetCheck = True
                    #
                    namespace = maUtils.getReferenceNamespace(referenceNode)
                    fileString_ = maUtils.getReferenceFile(referenceNode)
                    astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
                    if astAnimationRigFileLabel in fileString_:
                        showLabel = astAnimationRigFileLabel
                        if maUtils.isAppExist(astUnitModelProductGroup):
                            localMeshData = datAsset.getMeshObjectsConstantDic(assetName, namespace)
                            #
                            serverMeshData = {}
                            #
                            checkResults = datAnim.getAnimationSceneMeshConstant(localMeshData, serverMeshData)
                            maIfMethods.SceneAssetTreeitem.setMeshCheck(
                                treeitem=assetItem, column=2, checkResults=checkResults
                            )
                            geometryCheck = datAnim.getGeometryCheck(localMeshData, serverMeshData)
                            assetSubLabel = ['Error', 'On'][geometryCheck]
                    #
                    state = 'High - Quality'
                    if astLayoutRigFileLabel in fileString_:
                        state = 'Low - Quality'
                        showLabel = astLayoutRigFileLabel
                    #
                    existNumber = maUtils.getAttrDatum(referenceNode, prsVariants.Util.basicNumberAttrLabel)
                    if not existNumber:
                        assetSubLabel = 'Error'
                        stateSubLabel = 'Error'
                    numberKey = '%s - %s - %s' % (assetCategory, assetName, number)
                    if numberKey in numberKeyArray:
                        assetSubLabel = 'Error'
                        stateSubLabel = 'Error'
                    numberKeyArray.append(numberKey)
                    #
                    self.assetDataDic[assetItem] = referenceNode, assetCategory, assetName, number, assetVariant
                #
                showName = prsVariants.Util.assetTreeViewName(assetName, number, assetVariant)
                #
                assetItem.assetIndex = None
                assetItem.assetCategory = assetCategory
                assetItem.assetName = assetName
                assetItem.number = number
                assetItem.assetVariant = assetVariant
                assetItem.state = state
                assetItem.node = referenceNode
                #
                assetItem.setText(0, showName)
                assetItem.setText(1, state)
                assetItem.setItemIcon(0, assetIcon, assetSubLabel)
                assetItem.setItemIcon(1, stateIcon, stateSubLabel)
                #
                self.assetTreeItems.append(assetItem)
        #
        self.setViewConstant()
    # UI State
    def setRefreshUiState(self):
        self.setBtnState()
        self.setMdfBtnState()
        self.setSwtBtnState()
        self.setAnimExpBtnState()
    #
    def setBtnState(self):
        projectName = self.projectName
        #
        treeBox = self._rightTreeView
        #
        selectedItems = treeBox.selectedItems()
        #
        namespaceLabel = self.namespaceLabel
        fileLabel = self.fileLabel
        #
        boolean = len(selectedItems) == 1
        if boolean:
            assetItem = selectedItems[0]
            assetCategory = assetItem.assetCategory
            assetName = assetItem.assetName
            number = assetItem.number
            assetVariant = assetItem.assetVariant
            state = assetItem.state
            referenceNode = assetItem.node
            if state == 'High - Quality':
                namespace = maUtils.getReferenceNamespace(referenceNode)
                namespaceLabel.setDatum(namespace)
                #
                fileString_ = maUtils.getReferenceFile(referenceNode)
                fileLabel.setDatum(fileString_)
            else:
                namespaceLabel.setDatum(none)
                fileLabel.setDatum(none)
        else:
            namespaceLabel.setDatum(none)
            fileLabel.setDatum(none)
    #
    def setMdfBtnState(self):
        if self.modifyToolRefreshEnable:
            projectName = self.projectName
            #
            treeBox = self._rightTreeView
            #
            variantLabel = self.variantLabel
            variantButton = self.setVariantButton
            #
            numberLabel = self.numberLabel
            numberButton = self.setNumberButton
            #
            selectedItems = treeBox.selectedItems()
            #
            boolean = len(selectedItems) == 1
            variantButton.setPressable([False, True][boolean])
            numberButton.setPressable([False, True][boolean])
            if boolean:
                assetItem = selectedItems[0]
                assetIndex = assetItem.assetIndex
                assetCategory = assetItem.assetCategory
                assetName = assetItem.assetName
                number = assetItem.number
                assetVariant = assetItem.assetVariant
                state = assetItem.state
                referenceNode = assetItem.node
                if state == 'High - Quality':
                    variants = assetPr.getAssetVariantLis(assetIndex)
                    variantLabel.setDatumLis(variants)
                    variantLabel.setChoose(assetVariant)
                    #
                    numberLabel.setDefaultValue(int(number))
                    numberLabel.setValue(int(number))
                else:
                    variantLabel.setDatum(prsVariants.Util.astDefaultVersion)
                    #
                    numberLabel.setDefaultValue(0)
                    numberLabel.setValue(0)
            else:
                variantLabel.setDatum(prsVariants.Util.astDefaultVersion)
                #
                numberLabel.setDefaultValue(0)
                numberLabel.setValue(0)
    #
    def setSwtBtnState(self):
        def setBranch(button, explain, statisticalData):
            count = len(statisticalData)
            button.setPressable([False, True][count > 0])
            button.setNameText('%s [ %s ]' % (explain, str(count).zfill(4)))
        # Enable Switch
        if self.switchToolRefreshEnable:
            self.animRigItems = []
            self.layRigItems = []
            #
            self.rigItems = []
            self.gpuItems = []
            #
            self.enableCfxs = []
            self.disableCfxs = []
            #
            treeBox = self._rightTreeView
            #
            buttonDic = {
                self.switchToLowButton: ('Low - Quality', self.layRigItems),
                self.switchToHighButton: ('High - Quality', self.animRigItems),
                self.switchToGpuButton: ('GPU', self.gpuItems),
                self.switchToRigButton: ('Rig', self.rigItems),
            }
            #
            selectedItems = treeBox.selectedItems()
            if selectedItems:
                for assetItem in selectedItems:
                    assetCategory = assetItem.assetCategory
                    assetName = assetItem.assetName
                    number = assetItem.number
                    assetVariant = assetItem.assetVariant
                    state = assetItem.state
                    referenceNode = assetItem.node
                    if state == 'High - Quality':
                        self.animRigItems.append(assetItem)
                    if state == 'Low - Quality':
                        self.layRigItems.append(assetItem)
                    if state == 'High - Quality' or state == 'Low - Quality':
                        self.rigItems.append(assetItem)
                    if state == 'GPU':
                        self.gpuItems.append(assetItem)
                    #
                    namespace = maUtils.getReferenceNamespace(referenceNode)
                    tempCfxGroup = assetPr.scAstCfxTempGroupName(assetName, namespace)
                    if maUtils.isAppExist(tempCfxGroup):
                        children = maUtils.getNodeChildLis(tempCfxGroup, 1)
                        if children:
                            self.enableCfxs.append(assetItem)
                        if not children:
                            self.disableCfxs.append(assetItem)
                    #
                    if not maUtils.isAppExist(tempCfxGroup):
                        self.disableCfxs.append(assetItem)
                #
                for button, (explain, statisticalData) in buttonDic.items():
                    setBranch(button, explain, statisticalData)
            #
            if not selectedItems:
                [i.setPressable(False) for i in buttonDic.keys()]
    #
    def setAnimExpBtnState(self):
        self.root = ()
        #
        buttonA = self.exportAnimationButton
        buttonB = self.importAnimationButton
        buttonC = self.transferAnimationButton
        rootLabel = self.rootLabel
        formLabel = self.fromLabel
        toLabel = self.toLabel
        isAutoRoot = self.autoRootButton.isChecked()
        #
        selectedObjects = maUtils.getSelectedObjects(1)
        boolean = len(selectedObjects) == 1
        if boolean:
            object = selectedObjects[0]
            root = object
            if isAutoRoot:
                root = maUtils.getRoot(object, True)
            self.root = root
            rootLabel.setDatum(root.split('|')[-1])
        else:
            rootLabel.setDatum(none)
        buttonA.setPressable([False, True][boolean])
        buttonB.setPressable([False, True][boolean])
        #
        subBoolean = len(selectedObjects) == 2
        buttonC.setPressable([False, True][subBoolean])
        if subBoolean:
            formLabel.setDatum(selectedObjects[0].split('|')[-1])
            toLabel.setDatum(selectedObjects[1].split('|')[-1])
        else:
            formLabel.setDatum(none)
            toLabel.setDatum(none)
    # Asset Constant
    def setViewConstant(self):
        projectName = self.projectName
        sceneName = self.sceneName
        sceneVariant = self.sceneVariant
        #
        inData = datAnim.getReferenceDic(projectName)
        #
        explain = '''Read Assets's Constant - Data'''
        maxValue = len(inData)
        progressBar = bscObjects.If_Progress(explain, maxValue)
        #
        (
            assetArray, assetNumCortArray, assetDirCortArray, assNsHirCortArray, assNsNmCortArray, assetHirClrArray,
            assetHierCortArray, assetGeoCortArray, assetGeoShapeCortArray, assetMapCortArray, assetMapShapeCortArray,
         ) = datAnim.getAssetConstantData(projectName, sceneName, sceneVariant, inData, progressBar)
        totalCount = len(assetArray)
        assetNumCortCount = 0
        assetDirCortCount = 0
        assetNsHirCortCount = 0
        assetNsNmCortCount = 0
        assetHirClrCount = 0
        assetHierCortCount = 0
        assetGeomCortCount = 0
        assetGeomShapeCortCount = 0
        assetMapCortCount = 0
        assetMapShapeCortCount = 0
        boolean = totalCount > 0
        if totalCount:
            assetNumCortCount = len(assetNumCortArray)
            assetDirCortCount = len(assetDirCortArray)
            assetNsHirCortCount = len(assNsHirCortArray)
            assetNsNmCortCount = len(assNsNmCortArray)
            assetHirClrCount = len(assetHirClrArray)
            assetHierCortCount = len(assetHierCortArray)
            assetGeomCortCount = len(assetGeoCortArray)
            assetGeomShapeCortCount = len(assetGeoShapeCortArray)
            assetMapCortCount = len(assetMapCortArray)
            assetMapShapeCortCount = len(assetMapShapeCortArray)
        #
        data = [
            ('Obj - Path', totalCount, assetHierCortCount),
            ('Geom - Topo', totalCount, assetGeomCortCount),
            ('Geom - Shape', totalCount, assetGeomShapeCortCount),
            ('Map - Topo', totalCount, assetMapCortCount),
            ('Map - Shape', totalCount, assetMapShapeCortCount)
        ]
        #
        self._astModelSectorChart.setChartDatum(data)
        self._astModelSectorChart.update()
        #
        self.reduceAssetNumberButton.setPercent(totalCount, assetNumCortCount)
        #
        self.reduceAssetFileButton.setPercent(totalCount, assetDirCortCount)
        #
        self.reduceAssetNamespaceHierarchyButton.setPercent(totalCount, assetNsHirCortCount)
        #
        self.reduceAssetNamespaceNamingButton.setPercent(totalCount, assetNsNmCortCount)
        #
        self.clearAssetHierarchyButton.setPercent(totalCount, assetHirClrCount)
    #
    def setUpdateButtonState(self):
        selectedData = []
        #
        treeBox = self._rightTreeView
        usedData = self._connectObject.rigUsedData
        #
        selectedItems = treeBox.selectedItems()
        #
        isUsed = False
        if selectedItems:
            for i in selectedItems:
                if i in usedData:
                    isUsed = True
                    selectedData.append(i)
    #
    def setReduceAssetNamespaceHierarchy(self):
        projectName = self.projectName
        #
        inData = datAnim.getAssetNamespaceDic(projectName)
        maxValue = len(inData)
        if self._connectObject:
            self._connectObject.setMaxProgressValue(maxValue)
        #
        animOp.setRepairReferenceNamespace(inData, self._connectObject)
        #
        self.setViewConstant()
    #
    def setAssetVariant(self):
        projectName = self.projectName
        #
        assetItem = self.selectedAssetItem
        if assetItem:
            assetCategory = assetItem.assetCategory
            assetName = assetItem.assetName
            number = assetItem.number
            assetVariant = assetItem.assetVariant
            state = assetItem.state
            referenceNode = assetItem.node
            newVariant = self.variantLabel.datum()
            if not newVariant == assetVariant:
                maUtils.setAttrStringDatumForce_(referenceNode, prsVariants.Util.basicVariantAttrLabel, newVariant)
                assetItem.assetVariant = newVariant
                newShowName = prsVariants.Util.assetTreeViewName(assetName, number, newVariant)
                assetItem.setText(0, newShowName)
                maUtils.setMessageWindowShow(
                    u'Set Asset Variant', u'is Complete',
                    position='midCenterTop', fade=1, dragKill=0)
    #
    def setAssetNumber(self):
        assetItem = self.selectedAssetItem
        if assetItem:
            assetCategory = assetItem.assetCategory
            assetName = assetItem.assetName
            number = assetItem.number
            assetVariant = assetItem.assetVariant
            state = assetItem.state
            referenceNode = assetItem.node
            newNumber = self.numberLabel.value()
            if not newNumber == number:
                maUtils.setAttrStringDatumForce_(referenceNode, prsVariants.Util.basicNumberAttrLabel, str(newNumber).zfill(4))
                newShowName = prsVariants.Util.assetTreeViewName(assetName, str(newNumber).zfill(4), assetVariant)
                assetItem.setText(0, newShowName)
                maUtils.setMessageWindowShow(
                    u'Set Asset Number', u'is Complete',
                    position='midCenterTop', fade=1, dragKill=0)
    #
    def setAssetNumbers(self):
        projectName = self.projectName
        inData = datAnim.getAssetNumberReduceData(projectName)
        if inData:
            isRefresh = False
            attrName = prsVariants.Util.basicNumberAttrLabel
            maxValue = len(inData)
            for seq, (k, v) in enumerate(inData.items()):
                if self._connectObject:
                    self._connectObject.setProgressValue(seq + 1, maxValue)
                existsNumberArray = []
                errorReferenceNode = []
                correctNumberArray = []
                for referenceNode in v:
                    guessNumber = maUtils.getReferenceNumber(referenceNode)
                    existsNumber = maUtils.getAttrDatum(referenceNode, attrName)
                    if not existsNumber:
                        if not guessNumber in existsNumberArray:
                            isRefresh = True
                            maUtils.setAttrStringDatumForce_(referenceNode, attrName, str(guessNumber).zfill(4))
                            correctNumberArray.append(guessNumber)
                        if guessNumber in existsNumberArray:
                            errorReferenceNode.append(referenceNode)
                    if existsNumber:
                        correctNumberArray.append(int(existsNumber))
                    existsNumberArray.append(guessNumber)

                badNumberArray = bscMethods.Array.getDefects(correctNumberArray, 1)
                badNumberCount = len(badNumberArray)

                if errorReferenceNode:
                    isRefresh = True
                    numberAdd = 0
                    for num, referenceNode in enumerate(errorReferenceNode):
                        guessNumber = None
                        if num + 1 <= badNumberCount:
                            guessNumber = badNumberArray[num]
                        if num + 1 > badNumberCount:
                            numberAdd += 1
                            guessNumber = max(correctNumberArray) + numberAdd
                        if guessNumber:
                            maUtils.setAttrStringDatumForce_(referenceNode, attrName, str(guessNumber).zfill(4))
            #
            if isRefresh:
                maUtils.setMessageWindowShow(
                    u'Asset ( Rig ) Number Error is', u'Reduce',
                    position='midCenterTop', fade=1, dragKill=0)
                self.setViewConstant()
            if not isRefresh:
                maUtils.setMessageWindowShow(
                    u'Asset ( Rig ) Number Error is', u'Non-Exists',
                    position='midCenterTop', fade=1, dragKill=0)
    #
    def setReduceAssetDirectory(self):
        projectName = self.projectName
        inData = datAnim.getAssetDirectoryReduceData(projectName)
        if inData:
            isRefresh = False
            maxValue = len(inData)
            for seq, (k, v) in enumerate(inData.items()):
                if self._connectObject:
                    self._connectObject.setProgressValue(seq + 1, maxValue)
                referenceNode = k
                currentFile, correctFile = v
                if currentFile.lower() != correctFile.lower():
                    isRefresh = True
                    maUtils.setLoadReferenceFile(referenceNode, correctFile)
            #
            if isRefresh:
                maUtils.setMessageWindowShow(
                    u'Asset ( Rig ) Directory Error is', u'Reduce',
                    position='midCenterTop', fade=1, dragKill=0)
                self.setViewConstant()
            if not isRefresh:
                maUtils.setMessageWindowShow(
                    u'Asset ( Rig ) Directory Error is', u'Non-Exists',
                    position='midCenterTop', fade=1, dragKill=0)
    # Namespace Naming
    def setReduceAssetNamespaceNaming(self):
        projectName = self.projectName
        sceneName = self.sceneName
        sceneVariant = self.sceneVariant
        #
        inData = datAnim.getAssetNamespaceReduceData(projectName, sceneName, sceneVariant)
        if inData:
            isRefresh = False
            maxValue = len(inData)
            for seq, (k, v) in enumerate(inData.items()):
                if self._connectObject:
                    self._connectObject.setProgressValue(seq + 1, maxValue)
                referenceNode = k
                currentNamespace, correctNamespace = v
                if not ':' in currentNamespace:
                    if currentNamespace != correctNamespace:
                        isRefresh = True
                        maUtils.setReferenceNamespace(referenceNode, correctNamespace)
                if ':' in currentNamespace:
                    maUtils.setMessageWindowShow(
                        u'Click [ Reduce Namespace Hierarchy ] to', u'Reduce Namespace Hierarchy',
                        position='midCenterTop', fade=1, dragKill=0)
            #
            if isRefresh:
                maUtils.setMessageWindowShow(
                    u'Asset ( Rig ) Namespace Naming Error is', u'Reduce',
                    position='midCenterTop', fade=1, dragKill=0)
                self.setViewConstant()
            #
            if not isRefresh:
                maUtils.setMessageWindowShow(
                    u'Asset ( Rig ) Namespace Naming Error is', u'Non-Exists',
                    position='midCenterTop', fade=1, dragKill=0)
    #
    def setClearAssetHierarchy(self):
        projectName = self.projectName
        inData = datAnim.getAssetDirectoryReduceData(projectName)
    #
    def setAssetSelect(self):
        treeBox = self._rightTreeView
        if treeBox.hasFocus():
            selectedObjects = self.getSelAsset()
            if selectedObjects:
                maUtils.setNodeSelect(selectedObjects)
            if not selectedObjects:
                maUtils.setSelClear()
    #
    def setSelectReferenceNode(self):
        treeBox = self._rightTreeView
        assetItem = self.selectedAssetItem
        if assetItem:
            referenceNode = assetItem.node
            treeBox.clearSelection()
            maUtils.setSelObject(referenceNode)
    #
    def setSelectAll(self):
        treeBox = self._rightTreeView
        return treeBox.selectAll()
    #
    def setSelectClear(self):
        treeBox = self._rightTreeView
        return treeBox.clearSelection()
    #
    def setFrame(self):
        frameRange = maUtils.getFrameRange()
        self._frameValueLabel.setDefaultRange(*frameRange)
    #
    def setRigSwitch(self, keyword):
        def setBranch(assetItem):
            assetCategory = assetItem.assetCategory
            assetName = assetItem.assetName
            number = assetItem.number
            assetVariant = assetItem.assetVariant
            referenceNode = assetItem.node
            #
            if keyword == 'Low - Quality':
                showLabel = astLayoutRigFileLabel
                rigAssetFile = assetPr.astUnitProductFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetCategory, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
                )[1]
            else:
                showLabel = astAnimationRigFileLabel
                rigAssetFile = assetPr.astUnitProductFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    assetCategory, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Rig
                )[1]
            #
            if os.path.isfile(rigAssetFile):
                maUtils.setLoadReferenceFile(referenceNode, rigAssetFile)
                #
                assetItem.state = keyword
                assetItem.setText(1, keyword)
                #
                maUtils.viewResult(
                    u'Load %s Rig ( %s )' % (keyword, assetName), 'Complete',
                    position='botLeft', fade=1, dragKill=0
                )
            else:
                maUtils.setMessageWindowShow(
                    u'%s Rig is' % keyword, u'Non - Exists',
                    position='botLeft', fade=1, dragKill=0)
        #
        projectName = self.projectName
        #
        assetItems = [self.layRigItems, self.animRigItems][keyword == 'Low - Quality']
        if assetItems:
            for assetItem in assetItems:
                setBranch(assetItem)
    #
    def setRigSwitchToLow(self):
        keyword = 'Low - Quality'
        self.setRigSwitch(keyword)
    #
    def setRigSwitchToHigh(self):
        keyword = 'High - Quality'
        self.setRigSwitch(keyword)
    #
    def setRigSwitchToGpu(self):
        pass
    #
    def setGpuSwitchToRig(self):
        def setBranch(assetItem):
            assetCategory = assetItem.assetCategory
            assetName = assetItem.assetName
            number = assetItem.number
            assetVariant = assetItem.assetVariant
            state = assetItem.state
            referenceNode = assetItem.node
            #
            animOp.setSwitchAssetRig(projectName, referenceNode, assetCategory, assetName, number)
            #
            namespace = maUtils.getReferenceNamespace(referenceNode)
            astUnitModelProductGroup = assetPr.astUnitModelProductGroupName(assetName, namespace)
            localMeshData = datAsset.getMeshObjectsConstantDic(assetName, namespace)
            serverMeshData = {}
            #
            assetItem.state = keyword
            assetItem.setText(1, keyword)
            #
            checkResults = datAnim.getAnimationSceneMeshConstant(localMeshData, serverMeshData)
            maIfMethods.SceneAssetTreeitem.setMeshCheck(
                treeitem=assetItem, column=2, checkResults=checkResults
            )
            #
            maUtils.setMessageWindowShow(
                u'%s Switch to Rig' % assetName, u'Complete',
                position='botLeft', fade=1, dragKill=0)
        #
        projectName = self.projectName
        #
        keyword = 'High - Quality'
        #
        assetItems = self.gpuItems
        if assetItems:
            for assetItem in assetItems:
                setBranch(assetItem)
    #
    def setTransferAnimation(self):
        selectedObjects = maUtils.getSelectedObjects(1)
        boolean = len(selectedObjects) == 2
        if boolean:
            sourceObject = selectedObjects[0]
            targetObject = selectedObjects[1]
            fileString_ = 'D:/animTemp/%s' % (sourceObject.split('|')[-1].split(':')[-1] + '_' + bscMethods.OsTimetag.active())
            maFile.animExport(fileString_, sourceObject)
            maFile.animImport(fileString_, targetObject)
    #
    def setExportAnimation(self):
        fileString_ = 'D:/animTemp/tempAnim.key'
        root = self.root
        if root:
            data = maKeyframe.getKeyDatas(root)

            bscMethods.OsJson.write(fileString_, data)
            #
            maUtils.setMessageWindowShow(
                u'Animation ( Keys ) Export', u'Complete',
                position='topCenter', fade=1, dragKill=0
            )
    #
    def setImportAnimation(self):
        fileString_ = 'D:/animTemp/tempAnim.key'
        root = self.root
        if root:
            data = bscMethods.OsJson.read(fileString_)
            maKeyframe.setKeys(root, data)
            #
            maUtils.setMessageWindowShow(
                u'Animation ( Keys ) Import', u'Complete',
                position='topCenter', fade=1, dragKill=0
            )
    #
    def setExportActAnimation(self):
        pass
    #
    def getSelAsset(self):
        lis = []
        assetData = self.assetDataDic
        gpuData = self.gpuDataDic
        #
        treeBox = self._rightTreeView
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            for i in selectedItems:
                if i in assetData:
                    referenceNode, assetCategory, assetName, number, assetVariant = assetData[i]
                    namespace = \
                        maUtils.getReferenceNamespace(referenceNode)
                    astUnitModelProductGroup = \
                        [namespace + ':', none][namespace is none] + assetPr.astUnitModelProductGroupName(assetName)
                    lis.append(astUnitModelProductGroup)
                if i in gpuData:
                    referenceNode, assetCategory, assetName, number, assetVariant = gpuData[i]
                    gpuName = assetPr.astGpuName(assetName, number)
                    lis.append(gpuName)
        return lis
    # Script Job Connection
    def getSelRig(self):
        self.selectedAsset = []
        #
        data = maUtils.getSelObjParentFilter(prsVariants.Util.basicGeometryGroupLabel)
        if data:
            for i in data:
                self.selectedAsset.append(i)
        #
        subData = maUtils.getSelectedObjectsFilter('gpuCache')
        if subData:
            for i in subData:
                self.selectedAsset.append(i)
    #
    def getSceneClass(self):
        chooseLabel = self._scClassLabel
        #
        return chooseLabel.datum()
    #
    def getSceneName(self):
        chooseLabel = self._scNameLabel
        #
        return chooseLabel.datum()
    #
    def getSceneVariant(self):
        entryLabel = self._scVariantLabel
        #
        return entryLabel.datum()
    #
    def setupUnit(self):
        self.topToolBar().show()
        #
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(leftExpandWidget)
        leftExpandWidget.setUiWidth(self.panelWidth / 2)
        widget = qtCore.QWidget_()
        leftExpandWidget.addWidget(widget)
        self._leftScrollLayout = qtCore.QVBoxLayout_(widget)
        self.setupLeftWidget(self._leftScrollLayout)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        self._rightScrollLayout = qtCore.QVBoxLayout_(widget)
        self.setupRightWidget(self._rightScrollLayout)


#
class IfSimManagerUnit(_qtIfAbcWidget.IfToolUnitBasic):
    projectName = currentProjectName
    #
    UnitTitle = 'Scene Simulation Manager'
    #
    panelWidth = 800
    panelHeight = 800
    #
    widthSet = 800
    #
    SideWidth = 400
    #
    UnitScriptJobWindowName = 'simulationManageScriptJobWindow'
    #
    furCacheTips = [
        u"提示：",
        u"1：点击 刷新（Refresh） 列出所有的毛发节点...",
    ]
    #
    writeFurCacheTips1 = [
        u"提示：",
        u"1：引导 Yeti Nde_Node 的 Hair System 需要先指定缓存；",
        u"2：点击 Upload Fur Cache 上传（继续）所有节点的缓存...",
    ]
    #
    writeFurCacheTips2 = [
        u"提示：",
        u"1：引导 Yeti Nde_Node 的 Hair System 需要先指定缓存；",
        u"2：点击 Upload Fur Cache 上传（覆盖）所有节点的缓存...",
    ]
    #
    writeFurCacheTips3 = [
        u"提示：",
        u"1：引导 Yeti Nde_Node 的 Hair System 需要先指定缓存；",
        u"2：选择 毛发节点（Fur Nde_Node） ；",
        u"3：点击 Upload Fur Cache 上传（继续）选择节点的缓存...",
    ]
    #
    writeFurCacheTips4 = [
        u"提示：",
        u"1：引导 Yeti Nde_Node 的 Hair System 需要先指定缓存；",
        u"2：选择 毛发节点（Fur Nde_Node） ；",
        u"3：点击 Upload Fur Cache 上传（覆盖）选择节点的缓存...",
    ]
    #
    readFurCacheTips1 = [
        u"提示：",
        u"1：点击 Load Fur Cache 加载所有节点的缓存...",
    ]
    #
    readFurCacheTips2 = [
        u"提示：",
        u"1：选择 毛发节点（Fur Nde_Node） ；",
        u"2：点击 Load Fur Cache 加载选择节点的缓存...",
    ]
    w = 80
    # Write
    dicFurCacheWrite = {
        0: 'Config(s)',
        'writeAllNode': [1, 1, 0, 1, 2, '''All Nodes'''], 'continueWrite': [1, 1, 2, 1, 2, 'Continue Write'],
        'overrideFrame': [1, 2, 0, 1, 2, 'Override Frame ( Yeti )'], 'overrideSample': [1, 2, 2, 1, 2, 'Override Sample'],
        'frame': [1, 3, 0, 1, 4, 'Frame'],
        'sample': [1, 4, 0, 1, 4, 'Sample'],
        5: 'Action(s)',
        'writeFurCache': [1, 6, 0, 1, 4, 'Upload Fur Cache'],
        'tip': [0, 7, 0, 1, 4, 'Tip']
    }
    # Read
    dicFurCacheRead = {
        0: 'Config(s)',
        'readAllNode': [1, 1, 0, 1, 2, '''All Nodes'''],
        'ignoreExists': [1, 2, 0, 1, 2, 'Ignore Exists ( Local )'], 'ignoreStatic': [1, 2, 2, 1, 2, '''Ignore Static ( Hair System )'''],
        3: 'Action(s)',
        'readFurCache': [1, 4, 0, 1, 4, 'Load Fur Cache'],
        'tip': [0, 5, 0, 1, 4, 'Tip']
    }
    #
    dicBottomTool = {
        'openLocalFolder': [1, 0, 0, 1, 2, '''Open Local Folder''', 'svg_basic@svg#fileOpen'], 'openServerFolder': [1, 0, 2, 1, 2, '''Open Server Folder''', 'svg_basic@svg#fileOpen'],
        1: 'Cache(s) Check',
        'checkAllNode': [1, 2, 0, 1, 2, '''All Nodes'''],
        'nurbsHairCacheCheck': [1, 3, 0, 1, 4, '''Nurbs Hair Cache''']
    }
    def __init__(self, *args, **kwargs):
        super(IfSimManagerUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.initUnit()
        #
        self.setupUnit()
        #
        self.setRightTreeViewBox()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        if self._connectObject:
            pass
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methods = []
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupLeftWidget(self, layout):
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        self._tabWidget.setTabPosition(qtCore.South)
        layout.addWidget(self._tabWidget)
        self.setupLeftTabWidget(self._tabWidget)
    #
    def setupLeftTabWidget(self, tabWidget):
        self.modifyToolRefreshEnable = False
        self.switchToolRefreshEnable = False
        self.actToolRefreshEnable = False
        #
        scrollBox = qtCore.QScrollArea_()
        tabWidget.addTab(scrollBox, 'Fur Cache(s)', 'svg_basic@svg#tab')
        self.setupScAstCfxFurCacheTab(scrollBox)
    #
    def setupScAstCfxFurCacheTab(self, layout):
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Upload')
        self.setupScAstCfxFurCacheWriteToolBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Load')
        self.setupScAstCfxFurCacheLoadToolBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Modify')
        #
        self.setupScAstCfxFurCacheModifyToolBox(toolBox)
    #
    def setupScAstCfxFurCacheWriteToolBox(self, toolBox):
        inData = self.dicFurCacheWrite
        #
        self.writeAllNodeButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'writeAllNode', self.writeAllNodeButton)
        self.writeAllNodeButton.setChecked(True)
        self.writeAllNodeButton.toggled.connect(self.setUploadBtnState)
        self.writeAllNodeButton.toggled.connect(self.setWriteFurCacheTip)
        #
        self.continueWriteButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'continueWrite', self.continueWriteButton)
        self.continueWriteButton.setChecked(True)
        self.continueWriteButton.toggled.connect(self.setUploadBtnState)
        self.continueWriteButton.toggled.connect(self.setWriteFurCacheTip)
        #
        self.overrideFrameButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'overrideFrame', self.overrideFrameButton)
        #
        self._frameValueLabel = qtWidgets.QtValueEnterlabel()
        self._frameValueLabel.hide()
        toolBox.setInfo(inData, 'frame', self._frameValueLabel)
        startFrame, endFrame = maUtils.getFrameRange()
        self._frameValueLabel.setDefaultValue([startFrame, endFrame])
        self.overrideFrameButton.toggled.connect(self._frameValueLabel.setVisible)
        #
        self.overrideSampleButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'overrideSample', self.overrideSampleButton)
        #
        self._sampleValueLabel = qtWidgets.QtValueEnterlabel()
        self._sampleValueLabel.hide()
        toolBox.setInfo(inData, 'sample', self._sampleValueLabel)
        self._sampleValueLabel.setDefaultValue(3)
        self.overrideSampleButton.toggled.connect(self._sampleValueLabel.setVisible)
        #
        self._writeScAstCfxFurCacheButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'writeFurCache', self._writeScAstCfxFurCacheButton)
        self._writeScAstCfxFurCacheButton.setPercentEnable(True)
        self._writeScAstCfxFurCacheButton.setTooltip('''Upload Asset Character FX Fur Cache(s) to Server''')
        self._writeScAstCfxFurCacheButton.clicked.connect(self.setUploadScAstCfxFurCache)
        #
        self.writeFurCacheTipLabel = qtWidgets.QtTextbrower()
        toolBox.setInfo(inData, 'tip', self.writeFurCacheTipLabel)
        self.writeFurCacheTipLabel.setEnterEnable(False)
        self.writeFurCacheTipLabel.setRule(self.furCacheTips)
        #
        toolBox.setSeparators(inData)
    #
    def setupScAstCfxFurCacheLoadToolBox(self, toolBox):
        inData = self.dicFurCacheRead
        #
        self.readAllNodeButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'readAllNode', self.readAllNodeButton)
        self.readAllNodeButton.setChecked(True)
        self.readAllNodeButton.toggled.connect(self.setLoadBtnState)
        self.readAllNodeButton.toggled.connect(self.setReadFurCacheTip)
        #
        self.ignoreExistsButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'ignoreExists', self.ignoreExistsButton)
        self.ignoreExistsButton.setChecked(True)
        self.ignoreExistsButton.toggled.connect(self.setLoadBtnState)
        self.ignoreExistsButton.toggled.connect(self.setReadFurCacheTip)
        #
        self.ignoreStaticButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'ignoreStatic', self.ignoreStaticButton)
        self.ignoreStaticButton.setChecked(True)
        self.ignoreStaticButton.toggled.connect(self.setLoadBtnState)
        self.ignoreStaticButton.toggled.connect(self.setReadFurCacheTip)
        #
        self._readScAstCfxFurCacheButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'readFurCache', self._readScAstCfxFurCacheButton)
        self._readScAstCfxFurCacheButton.setPercentEnable(True)
        self._readScAstCfxFurCacheButton.setTooltip('''Load Asset Character FX Fur Cache(s) from Server''')
        self._readScAstCfxFurCacheButton.clicked.connect(self.setLoadScAstCfxFurCache)
        #
        self.readFurCacheTipLabel = qtWidgets.QtTextbrower()
        toolBox.setInfo(inData, 'tip', self.readFurCacheTipLabel)
        self.readFurCacheTipLabel.setEnterEnable(False)
        self.readFurCacheTipLabel.setRule(self.furCacheTips)
        #
        toolBox.setSeparators(inData)
    #
    def setupRightWidget(self, layout):
        self.topToolBar = qtWidgets_.xToolBar()
        layout.addWidget(self.topToolBar)
        self.setupTopToolBar(self.topToolBar)
        #
        self._rightTreeView = qtWidgets_.QTreeWidget_()
        layout.addWidget(self._rightTreeView)
        self._rightTreeView.setFilterConnect(self._filterEnterLabel)
    #
    def setupTopToolBar(self, toolBar):
        def setSelectAll():
            treeBox = self._rightTreeView
            return treeBox.selectAll()
        #
        def setSelectClear():
            treeBox = self._rightTreeView
            return treeBox.clearSelection()
        #
        self._selectAllButton = qtWidgets.QtIconbutton('svg_basic@svg#checkedAll')
        toolBar.addWidget(self._selectAllButton)
        self._selectAllButton.clicked.connect(setSelectAll)
        #
        self._selectClearButton = qtWidgets.QtIconbutton('svg_basic@svg#uncheckedAll')
        toolBar.addWidget(self._selectClearButton)
        self._selectClearButton.clicked.connect(setSelectClear)
        #
        self._filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        toolBar.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
        toolBar.addWidget(self._refreshButton)
        self._refreshButton.clicked.connect(self.setListScAstCfxFurNode)
    #
    def setupScAstCfxFurCacheModifyToolBox(self, toolBox):
        inData = self.dicBottomTool
        self.openCacheLocalFolderButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'openLocalFolder', self.openCacheLocalFolderButton)
        self.openCacheLocalFolderButton.clicked.connect(self.setOpenCacheLocalFolder)
        #
        self.openCacheServerFolderButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'openServerFolder', self.openCacheServerFolderButton)
        self.openCacheServerFolderButton.clicked.connect(self.setOpenCacheServerFolder)
        #
        self.checkAllNodeButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'checkAllNode', self.checkAllNodeButton)
        #
        self.nurbsHairCacheCheckButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'nurbsHairCacheCheck', self.nurbsHairCacheCheckButton)
        self.nurbsHairCacheCheckButton.setPercentEnable(True)
        #
        toolBox.setSeparators(inData)
    #
    def setRightTreeViewBox(self):
        self.furNodeItemDic = {}
        self.furNodeDataDic = {}
        self.needWriteFurNodes = []
        self._needLoadScAstCfxFurNodes = []
        #
        treeBox = self._rightTreeView
        #
        treeBox.setColumns(['Scene > Asset > Fur', 'Local Status', 'Server Status'], [4, 2, 2], self.panelWidth)
        #
        treeBox.itemSelectionChanged.connect(self.setSelNodes)
        #
        treeBox.itemSelectionChanged.connect(self.setUploadBtnState)
        treeBox.itemSelectionChanged.connect(self.setLoadBtnState)
        #
        treeBox.itemSelectionChanged.connect(self.setBottomBtnState)
    #
    def setListScAstCfxFurNode(self):
        def setSceneBranch(sceneDataDic):
            def setSceneActions(treeItem, itemWidget):
                pass
            #
            def setScAstBranch(assetDataLis):
                def setAstCfxFurBranch(nodeDataLis):
                    def setAstCfxFurSubBranch(furObjectPath):
                        cfxFurItem = qtWidgets_.QTreeWidgetItem_()
                        assetItem.addChild(cfxFurItem)
                        #
                        cfxFurLabel = maFur.getFurObjectLabel(furObjectPath, assetName)
                        cfxFurItem.setText(0, cfxFurLabel)
                        furObjectType = maUtils.getShapeType(furObjectPath)
                        #
                        cacheItemIcon1 = 'svg_basic@svg#local'
                        cacheItemIcon2 = 'svg_basic@svg#server'
                        #
                        nodeIconSubLabel = none
                        nodeLocalStateSubLabel = none
                        nodeServerStateSubLabel = none
                        #
                        cfxFurItem.isServerExists = False
                        cfxFurItem.isServer = False
                        cfxFurItem.isLocal = False
                        #
                        cfxFurItem.serverCacheFile = None
                        cfxFurItem.localCacheFile = None
                        #
                        if furObjectType == appCfg.MaNodeType_Plug_Yeti:
                            # Local
                            existLocalCacheFile, localSolverMode, localCacheStartFrame, localCacheEndFrame = maFur.getYetiCacheInfo(furObjectPath)
                            # Server
                            existServerCacheFile, serverSolverMode, serverCacheStartFrame, serverCacheEndFrame = scenePr.getScAstCfxYetiCacheExists(
                                projectName,
                                sceneName, sceneVariant, assetName, number,
                                assetVariant,
                                cfxFurLabel
                            )
                            #
                            localCacheExists = existLocalCacheFile != none
                            serverCacheExists = existServerCacheFile != none
                            #
                            if not localCacheExists:
                                nodeLocalStateSubLabel = 'off'
                            #
                            if localCacheExists:
                                localStartFrameCheck = localCacheStartFrame <= sceneStartFrame
                                localEndFrameCheck = localCacheEndFrame >= sceneEndFrame
                                #
                                if localStartFrameCheck and localEndFrameCheck:
                                    cfxFurItem.isLocalExists = True
                                    if localSolverMode == 'On':
                                        nodeLocalStateSubLabel = 'on'
                                elif not localStartFrameCheck or not localEndFrameCheck:
                                    nodeIconSubLabel = 'warning'
                                    nodeLocalStateSubLabel = 'warning'
                            #
                            localStatusExplain = '{1} - {2} ( {0} )'.format(
                                localSolverMode,
                                str(localCacheStartFrame).zfill(4), str(localCacheEndFrame).zfill(4)
                            )
                            #
                            cfxFurItem.setText(1, localStatusExplain)
                            cfxFurItem.setToolTip(1, existLocalCacheFile)
                            #

                            if not serverCacheExists:
                                nodeServerStateSubLabel = 'off'
                            #
                            elif serverCacheExists:
                                serverStartFrameCheck = serverCacheStartFrame <= sceneStartFrame
                                serverEndFrameCheck = serverCacheEndFrame >= sceneEndFrame
                                #
                                if serverStartFrameCheck and serverEndFrameCheck:
                                    cfxFurItem.isServerExists = True
                                    nodeServerStateSubLabel = 'on'
                                #
                                if not serverStartFrameCheck or not serverEndFrameCheck:
                                    nodeServerStateSubLabel = 'warning'
                            #
                            serverStatusExplain = '{1} - {2} ( {0} )'.format(
                                serverSolverMode,
                                str(serverCacheStartFrame).zfill(4), str(serverCacheEndFrame).zfill(4)
                            )
                            #
                            cfxFurItem.setText(2, serverStatusExplain)
                            cfxFurItem.setToolTip(2, existServerCacheFile)
                            if existLocalCacheFile:
                                cfxFurItem.isLocal = True
                            # Check Exists
                            if existServerCacheFile:
                                if existLocalCacheFile == existServerCacheFile:
                                    cfxFurItem.isServer = True
                                    if localCacheStartFrame == serverCacheStartFrame and localCacheEndFrame == serverCacheEndFrame:
                                        if localSolverMode == 'On':
                                            nodeIconSubLabel = 'on'
                                else:
                                    cfxFurItem.isServer = False
                                    nodeIconSubLabel = 'warning'
                            #
                            cfxFurItem.solverMode = localSolverMode
                        #
                        elif furObjectType == appCfg.MaHairSystemType:
                            # Local
                            existLocalCacheFile, localSolverMode, localCacheStartFrame, localCacheEndFrame = maFur.getGeomCacheExists(furObjectPath)
                            # Server
                            existServerCacheFile, serverSolverMode, serverCacheStartFrame, serverCacheEndFrame = scenePr.getScAstCfxGeomCacheExists(
                                projectName,
                                sceneName, sceneVariant,
                                assetName, number, assetVariant,
                                cfxFurLabel
                            )
                            #
                            cfxFurItem.solverMode = localSolverMode
                            #
                            localCacheExists = existLocalCacheFile != none
                            serverCacheExists = existServerCacheFile != none
                            #
                            if not localCacheExists:
                                nodeLocalStateSubLabel = 'off'
                            #
                            if localCacheExists:
                                localStartFrameCheck = localCacheStartFrame <= sceneStartFrame
                                localEndFrameCheck = localCacheEndFrame >= sceneEndFrame
                                #
                                if localStartFrameCheck and localEndFrameCheck:
                                    cfxFurItem.isLocalExists = True
                                    nodeLocalStateSubLabel = 'on'
                                #
                                if not localStartFrameCheck or not localEndFrameCheck:
                                    nodeIconSubLabel = 'warning'
                                    nodeLocalStateSubLabel = 'warning'
                            #
                            localStatusExplain = '{1} - {2} ( {0} )'.format(
                                localSolverMode,
                                str(localCacheStartFrame).zfill(4), str(localCacheEndFrame).zfill(4)
                            )
                            cfxFurItem.setText(1, localStatusExplain)
                            cfxFurItem.setToolTip(1, existLocalCacheFile)
                            #
                            if not serverCacheExists:
                                nodeServerStateSubLabel = 'off'
                            #
                            if serverCacheExists:
                                serverStartFrameCheck = serverCacheStartFrame <= sceneStartFrame
                                serverEndFrameCheck = serverCacheEndFrame >= sceneEndFrame
                                #
                                if serverStartFrameCheck and serverEndFrameCheck:
                                    cfxFurItem.isServerExists = True
                                    nodeServerStateSubLabel = 'on'
                                #
                                if not serverStartFrameCheck or not serverEndFrameCheck:
                                    nodeServerStateSubLabel = 'warning'
                            #
                            serverStatusExplain = '{1} - {2} ( {0} )'.format(
                                serverSolverMode,
                                str(serverCacheStartFrame).zfill(4), str(serverCacheEndFrame).zfill(4)
                            )
                            cfxFurItem.setText(2, serverStatusExplain)
                            cfxFurItem.setToolTip(2, existServerCacheFile)
                            if existLocalCacheFile:
                                cfxFurItem.isLocal = True
                            # Check Exists
                            if existServerCacheFile:
                                if existLocalCacheFile == existServerCacheFile:
                                    cfxFurItem.isServer = True
                                    if localCacheStartFrame == serverCacheStartFrame and localCacheEndFrame == serverCacheEndFrame:
                                        nodeIconSubLabel = 'on'
                                else:
                                    cfxFurItem.isServer = False
                                    nodeIconSubLabel = 'warning'
                            #
                            cfxFurItem.solverMode = localSolverMode
                            cfxFurItem.cache = existServerCacheFile
                        #
                        elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
                            # Local
                            existLocalCacheFile, localSolverMode, localCacheStartFrame, localCacheEndFrame = maFur.getNhrCacheInfo(furObjectPath)
                            #
                            existServerCacheFile, serverSolverMode, serverCacheStartFrame, serverCacheEndFrame = scenePr.getScAstCfxNurbsHairCacheExists(
                                projectName,
                                sceneName, sceneVariant,
                                assetName, number, assetVariant,
                                cfxFurLabel
                            )
                            localCacheExists = existLocalCacheFile != none
                            serverCacheExists = existServerCacheFile != none
                            #
                            if not localCacheExists:
                                nodeLocalStateSubLabel = 'off'
                            #
                            elif localCacheExists:
                                cfxFurItem.localCacheFile = existLocalCacheFile
                                #
                                localStartFrameCheck = localCacheStartFrame <= sceneStartFrame
                                localEndFrameCheck = localCacheEndFrame >= sceneEndFrame
                                #
                                if localStartFrameCheck and localEndFrameCheck:
                                    cfxFurItem.isLocalExists = True
                                    if localSolverMode == 'Read':
                                        nodeLocalStateSubLabel = 'on'
                                elif not localStartFrameCheck or not localEndFrameCheck:
                                    nodeIconSubLabel = 'warning'
                                    nodeLocalStateSubLabel = 'warning'
                            #
                            localStatusExplain = '{1} - {2} ( {0} )'.format(
                                localSolverMode,
                                str(localCacheStartFrame).zfill(4), str(localCacheEndFrame).zfill(4)
                            )
                            #
                            cfxFurItem.setText(1, localStatusExplain)
                            cfxFurItem.setToolTip(1, existLocalCacheFile)
                            #
                            if not serverCacheExists:
                                nodeServerStateSubLabel = 'off'
                            #
                            elif serverCacheExists:
                                cfxFurItem.serverCacheFile = existServerCacheFile
                                #
                                serverStartFrameCheck = serverCacheStartFrame <= sceneStartFrame
                                serverEndFrameCheck = serverCacheEndFrame >= sceneEndFrame
                                #
                                if serverStartFrameCheck and serverEndFrameCheck:
                                    cfxFurItem.isServerExists = True
                                    nodeServerStateSubLabel = 'on'
                                #
                                if not serverStartFrameCheck or not serverEndFrameCheck:
                                    nodeServerStateSubLabel = 'warning'
                            #
                            serverStatusExplain = '{1} - {2} ( {0} )'.format(
                                serverSolverMode,
                                str(serverCacheStartFrame).zfill(4), str(serverCacheEndFrame).zfill(4)
                            )
                            #
                            cfxFurItem.setText(2, serverStatusExplain)
                            cfxFurItem.setToolTip(2, existServerCacheFile)
                            if existLocalCacheFile:
                                cfxFurItem.isLocal = True
                            # Check Exists
                            if existServerCacheFile:
                                if existLocalCacheFile == existServerCacheFile:
                                    cfxFurItem.isServer = True
                                    if localCacheStartFrame == serverCacheStartFrame and localCacheEndFrame == serverCacheEndFrame:
                                        if localSolverMode == 'Read':
                                            nodeIconSubLabel = 'on'
                                else:
                                    cfxFurItem.isServer = False
                                    nodeIconSubLabel = 'warning'
                            #
                            cfxFurItem.solverMode = localSolverMode
                        #
                        cfxFurItem.sceneCategory = sceneCategory
                        cfxFurItem.sceneName = sceneName
                        cfxFurItem.sceneVariant = sceneVariant
                        cfxFurItem.startFrame = sceneStartFrame
                        cfxFurItem.endFrame = sceneEndFrame
                        cfxFurItem.assetCategory = assetCategory
                        cfxFurItem.assetName = assetName
                        cfxFurItem.number = number
                        cfxFurItem.assetVariant = assetVariant
                        cfxFurItem.timeTag = timeTag
                        #
                        cfxFurItem.cfxFurObject = furObjectPath
                        cfxFurItem.cfxFurLabel = cfxFurLabel
                        cfxFurItem.furObjectType = furObjectType
                        #
                        cfxFurItem.furNodes = [furObjectPath]
                        #
                        cfxFurItem.setItemMayaIcon(0, furObjectType, nodeIconSubLabel)
                        cfxFurItem.setItemIcon_(1, cacheItemIcon1, nodeLocalStateSubLabel)
                        cfxFurItem.setItemIcon_(2, cacheItemIcon2, nodeServerStateSubLabel)
                        #
                        self.furNodeItemDic[furObjectPath] = cfxFurItem
                    #
                    for i in nodeDataLis:
                        setAstCfxFurSubBranch(i)
                # Assets
                for assetIndex, assetCategory, assetName, number, assetVariant, furNodesInAsset in assetDataLis:
                    furNodesInScene.extend(furNodesInAsset)
                    #
                    assetItem = qtWidgets_.QTreeWidgetItem_()
                    sceneItem.addChild(assetItem)
                    #
                    assetIcon = 'svg_basic@svg#package_object'
                    assetIconSubLabel = none
                    #
                    assetShowName = assetPr.getAssetViewInfo(assetIndex, assetCategory, assetVariant)
                    #
                    assetItem.setItemIconWidget(0, assetIcon, assetShowName, assetIconSubLabel)
                    #
                    timeTag = scenePr.getScAstModelCacheActiveTimeTag(
                        projectName,
                        sceneName, sceneVariant,
                        assetName, number
                    )
                    if furNodesInAsset:
                        setAstCfxFurBranch(furNodesInAsset)
                    #
                    assetItem.furNodes = furNodesInAsset
                    #
                    assetItem.setExpanded(True)
            #
            for (sceneIndex, sceneCategory, sceneName, sceneVariant), assetDataArray in sceneDataDic.items():
                if self._connectObject:
                    self._connectObject.updateProgress()
                #
                sceneStartFrame, sceneEndFrame = scenePr.getScUnitFrameRange(
                    projectName, sceneCategory, sceneName, sceneVariant
                )
                #
                sceneItemIcon0 = 'svg_basic@svg#package_object'
                sceneIconSubLabel = None
                sceneItemIcon1 = 'svg_basic@svg#time'
                #
                sceneShowName = scenePr.getSceneViewInfo(sceneIndex, sceneCategory, sceneVariant)
                #
                sceneItem = qtWidgets_.QTreeWidgetItem_()
                treeBox.addItem(sceneItem)
                #
                sceneItemWidget = sceneItem.setItemIconWidget(0, sceneItemIcon0, sceneShowName, sceneIconSubLabel)
                setSceneActions(sceneItem, sceneItemWidget)
                #
                sceneItem.setText(1, '{} - {}'.format(str(sceneStartFrame).zfill(4), str(sceneEndFrame).zfill(4)))
                sceneItem.setItemIcon_(1, sceneItemIcon1)
                #
                furNodesInScene = []
                #
                setScAstBranch(assetDataArray)
                #
                sceneItem.furNodes = furNodesInScene
                sceneItem.setExpanded(True)
        #
        self.furNodeItemDic = {}
        self.furNodeDataDic = {}
        #
        treeBox = self._rightTreeView
        #
        projectName = self.projectName
        #
        inData = datScene.getScAstCfxFurDic_(projectName)
        #
        treeBox.clear()
        if inData:
            maxValue = len(inData)
            if self._connectObject:
                self._connectObject.setMaxProgressValue(maxValue)
            setSceneBranch(inData)
        #
        self.setUploadBtnState()
        self.setWriteFurCacheTip()
        self.setLoadBtnState()
        self.setReadFurCacheTip()
        #
        self.getCfxNurbsHairItems()
        #
        self.setBottomBtnState()
    #
    def getCfxNurbsHairItems(self):
        self._cfxNurbsHairItems = []
        #
        treeBox = self._rightTreeView
        treeItems = treeBox.treeItems()
        if treeItems:
            for treeItem in treeItems:
                if hasattr(treeItem, 'furObjectType'):
                    furObjectType = treeItem.furObjectType
                    if furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
                        self._cfxNurbsHairItems.append(treeItem)
    #
    def setOpenCacheLocalFolder(self):
        treeBox = self._rightTreeView
        selectedTreeItems = treeBox.selectedItems()
        if selectedTreeItems:
            treeItem = selectedTreeItems[0]
            if hasattr(treeItem, 'cfxFurObject'):
                fileString_ = treeItem.localCacheFile
                bscMethods.OsFile.openDirectory(fileString_)
    #
    def setOpenCacheServerFolder(self):
        treeBox = self._rightTreeView
        selectedTreeItems = treeBox.selectedItems()
        if selectedTreeItems:
            treeItem = selectedTreeItems[0]
            if hasattr(treeItem, 'cfxFurObject'):
                fileString_ = treeItem.serverCacheFile
                bscMethods.OsFile.openDirectory(fileString_)
    #
    def setUploadBtnState(self):
        self.needWriteFurNodes = []
        #
        isUseAll = self.writeAllNodeButton.isChecked()
        isContinue = self.continueWriteButton.isChecked()
        #
        furNodes = []
        existsCacheNodes = []
        if isUseAll:
            furNodes = self.getAllNodes()
        if not isUseAll:
            furNodes = self.getSelNodes()
        #
        if furNodes:
            for furObjectPath in furNodes:
                if furObjectPath in self.furNodeItemDic:
                    cfxFurItem = self.furNodeItemDic[furObjectPath]
                    isServerExists = cfxFurItem.isServerExists
                    if isContinue:
                        if cfxFurItem.isServerExists:
                            existsCacheNodes.append(furObjectPath)
                        if not cfxFurItem.isServerExists:
                            self.needWriteFurNodes.append(furObjectPath)
                    #
                    if not isContinue:
                        self.needWriteFurNodes.append(furObjectPath)
        #
        maxCount = len(furNodes)
        existsCacheCount = len(existsCacheNodes)
        #
        self._writeScAstCfxFurCacheButton.setPercent(maxCount, existsCacheCount)
    #
    def setWriteFurCacheTip(self):
        isUseAll = self.writeAllNodeButton.isChecked()
        isContinue = self.continueWriteButton.isChecked()
        #
        if isUseAll:
            if isContinue:
                self.writeFurCacheTipLabel.setRule(self.writeFurCacheTips1)
            elif not isContinue:
                self.writeFurCacheTipLabel.setRule(self.writeFurCacheTips2)
        #
        elif not isUseAll:
            if isContinue:
                self.writeFurCacheTipLabel.setRule(self.writeFurCacheTips3)
            elif not isContinue:
                self.writeFurCacheTipLabel.setRule(self.writeFurCacheTips4)
    #
    def setLoadBtnState(self):
        self._needLoadScAstCfxFurNodes = []
        #
        isUseAll = self.readAllNodeButton.isChecked()
        isIgnoreExists = self.ignoreExistsButton.isChecked()
        isIgnoreStatic = self.ignoreStaticButton.isChecked()
        #
        furNodes = []
        existsCacheNodes = []
        if isUseAll:
            furNodes = self.getAllNodes()
        if not isUseAll:
            furNodes = self.getSelNodes()
        #
        if furNodes:
            for furObjectPath in furNodes:
                if furObjectPath in self.furNodeItemDic:
                    cfxFurItem = self.furNodeItemDic[furObjectPath]
                    furObjectType = cfxFurItem.furObjectType
                    solverMode = cfxFurItem.solverMode
                    #
                    isServerExists = cfxFurItem.isServerExists
                    isServer = cfxFurItem.isServer
                    #
                    if isIgnoreStatic:
                        if furObjectType == appCfg.MaHairSystemType:
                            if solverMode == 'Static':
                                if not isServer:
                                    existsCacheNodes.append(furObjectPath)
                        #
                        if isServer:
                            existsCacheNodes.append(furObjectPath)
                    #
                    elif not isIgnoreStatic:
                        if isServer:
                            existsCacheNodes.append(furObjectPath)
                    #
                    if isServerExists:
                        if not isServer:
                            self._needLoadScAstCfxFurNodes.append(furObjectPath)
        #
        maxCount = len(furNodes)
        existsCacheCount = len(existsCacheNodes)
        #
        self._readScAstCfxFurCacheButton.setPercent(maxCount, existsCacheCount)
    #
    def setBottomBtnState(self):
        if self.checkAllNodeButton.isChecked():
            cfxNurbsHairMaxCount = len(self._cfxNurbsHairItems)
            correctCfxNurbsHairCount = len(self._correctCfxNurbsHairItems)
        else:
            cfxNurbsHairMaxCount = len([i for i in self._cfxNurbsHairItems if i.isSelected()])
            correctCfxNurbsHairCount = len([i for i in self._correctCfxNurbsHairItems if i.isSelected()])
        #
        self.nurbsHairCacheCheckButton.setPercent(cfxNurbsHairMaxCount, correctCfxNurbsHairCount)
    #
    def setReadFurCacheTip(self):
        isUseAll = self.readAllNodeButton.isChecked()
        #
        if isUseAll:
            self.readFurCacheTipLabel.setRule(self.readFurCacheTips1)
        elif not isUseAll:
            self.readFurCacheTipLabel.setRule(self.readFurCacheTips2)
    #
    def setUploadScAstCfxFurCache(self):
        projectName = self.projectName
        nodes = self.needWriteFurNodes
        nodeItemDic = self.furNodeItemDic
        #
        isOverrideFrame = self.overrideFrameButton.isChecked()
        isOverrideSample = self.overrideSampleButton.isChecked()
        #
        dataArray = []
        if nodes:
            for furObjectPath in nodes:
                if furObjectPath in nodeItemDic:
                    furNodeName = maUtils._toNodeName(furObjectPath)
                    #
                    cfxFurItem = nodeItemDic[furObjectPath]
                    sceneCategory = cfxFurItem.sceneCategory
                    sceneName = cfxFurItem.sceneName
                    sceneVariant = cfxFurItem.sceneVariant
                    #
                    startFrame = cfxFurItem.startFrame
                    endFrame = cfxFurItem.endFrame
                    #
                    assetCategory = cfxFurItem.assetCategory
                    assetName = cfxFurItem.assetName
                    number = cfxFurItem.number
                    assetVariant = cfxFurItem.assetVariant
                    #
                    timeTag = cfxFurItem.timeTag
                    #
                    cfxFurLabel = cfxFurItem.cfxFurLabel
                    furObjectType = cfxFurItem.furObjectType
                    #
                    sample = 3
                    solverMode = cfxFurItem.solverMode
                    furCacheFile = none
                    #
                    if isOverrideFrame:
                        startFrame, endFrame = self._frameValueLabel.value()
                    #
                    if isOverrideSample:
                        sample = self._sampleValueLabel.value()
                    #
                    if furObjectType == appCfg.MaNodeType_Plug_Yeti:
                        furCacheFile = scenePr.scAstCfxYetiCacheFile(
                            lxConfigure.LynxiRootIndex_Server,
                            projectName,
                            sceneName, sceneVariant,
                            assetName, number, assetVariant,
                            cfxFurLabel,
                            timeTag
                        )[1]
                    #
                    elif furObjectType == appCfg.MaHairSystemType:
                        furCacheFile = scenePr.scAstCfxGeomCacheFile(
                            lxConfigure.LynxiRootIndex_Server,
                            projectName,
                            sceneName, sceneVariant,
                            assetName, number, assetVariant,
                            cfxFurLabel,
                            timeTag
                        )[1]
                    #
                    elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
                        furCacheFile = scenePr.scAstCfxNurbsHairCacheFile(
                            lxConfigure.LynxiRootIndex_Server,
                            projectName,
                            sceneName, sceneVariant,
                            assetName, number, assetVariant,
                            cfxFurLabel,
                            timeTag
                        )[1]
                    #
                    furCacheIndexData = scenePr.furCacheIndexData(
                        furNodeName, furObjectType,
                        furCacheFile,
                        startFrame, endFrame, sample, solverMode, timeTag
                    )
                    #
                    nodeIndexFile = scenePr.scAstCfxFurCacheIndexFile(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName,
                        sceneName, sceneVariant,
                        assetName, number, assetVariant,
                        cfxFurLabel
                    )[1]
                    if furCacheFile:
                        dataArray.append((
                            furObjectPath,
                            cfxFurLabel, furObjectType,
                            furCacheFile, furCacheIndexData, nodeIndexFile,
                            startFrame, endFrame, sample, solverMode
                        ))
        #
        if dataArray:
            self._connectObject.hide()
            maScUploadCmds.uploadScAstCfxFurCache(
                dataArray
            )
            self._connectObject.show()
        #
        self.setListScAstCfxFurNode()
    #
    def setLoadScAstCfxFurCache(self):
        projectName = self.projectName
        #
        objectlis = self._needLoadScAstCfxFurNodes
        nodeItemDic = self.furNodeItemDic
        if objectlis:
            # View Progress
            explain = '''Load Asset ( CFX ) Cache'''
            maxValue = len(objectlis)
            progressBar = bscObjects.If_Progress(explain, maxValue)
            for furObject in objectlis:
                progressBar.update()
                #
                cfxFurItem = nodeItemDic[furObject]
                sceneName = cfxFurItem.sceneName
                sceneVariant = cfxFurItem.sceneVariant
                #
                assetName = cfxFurItem.assetName
                number = cfxFurItem.number
                assetVariant = cfxFurItem.assetVariant
                #
                cfxFurLabel = cfxFurItem.cfxFurLabel
                furObjectType = cfxFurItem.furObjectType
                #
                if furObjectType == appCfg.MaNodeType_Plug_Yeti:
                    cacheFile, solverMode, startFrame, endFrame = scenePr.getScAstCfxYetiCacheExists(
                        projectName,
                        sceneName, sceneVariant, assetName, number,
                        assetVariant,
                        cfxFurLabel
                    )
                    #
                    if cacheFile:
                        maFur.setYetiConnectCache(
                            furObject,
                            cacheFile
                        )
                #
                elif furObjectType == appCfg.MaHairSystemType:
                    cacheFile, solverMode, startFrame, endFrame = scenePr.getScAstCfxGeomCacheExists(
                        projectName,
                        sceneName, sceneVariant, assetName, number,
                        assetVariant,
                        cfxFurLabel
                    )
                    #
                    if cacheFile:
                        cachePath = os.path.dirname(cacheFile)
                        cacheName = cfxFurLabel
                        maFur.setGeometryObjectInCache(
                            cachePath, cacheName, furObject, solverMode
                        )
                #
                elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
                    cacheFile, solverMode, startFrame, endFrame = scenePr.getScAstCfxNurbsHairCacheExists(
                        projectName,
                        sceneName, sceneVariant, assetName, number,
                        assetVariant,
                        cfxFurLabel
                    )
                    if cacheFile:
                        maFur.setNurbsHairConnectCache(
                            furObject, cacheFile
                        )
        #
        self.setListScAstCfxFurNode()
    #
    def setAssetSelect(self):
        pass
    #
    def setSelNodes(self):
        nodes = self.getSelNodes()
        if nodes:
            maUtils.setNodeSelect(nodes)
        if not nodes:
            maUtils.setSelClear()
    #
    def getAllNodes(self):
        lis = []
        #
        treeBox = self._rightTreeView
        treeItems = treeBox.topItems()
        if treeItems:
            for treeItem in treeItems:
                if hasattr(treeItem, 'furNodes'):
                    nodes = treeItem.furNodes
                    if nodes:
                        [lis.append(i) for i in nodes if i not in lis]
        #
        return lis
    #
    def getSelNodes(self):
        lis = []
        #
        treeBox = self._rightTreeView
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            for treeItem in selectedItems:
                if hasattr(treeItem, 'furNodes'):
                    nodes = treeItem.furNodes
                    if nodes:
                        [lis.append(i) for i in nodes if i not in lis]
        #
        return lis
    #
    def initUnit(self):
        self._cfxNurbsHairItems = []
        self._correctCfxNurbsHairItems = []
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(leftExpandWidget)
        leftExpandWidget.setUiWidth(self.SideWidth)
        widget = qtCore.QWidget_()
        leftExpandWidget.addWidget(widget)
        self._leftScrollLayout = qtCore.QVBoxLayout_(widget)
        self.setupLeftWidget(self._leftScrollLayout)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        self._rightScrollLayout = qtCore.QVBoxLayout_(widget)
        self.setupRightWidget(self._rightScrollLayout)
