# coding=utf-8
import os
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from random import choice
#
from LxCore import lxBasic, lxCore_
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import projectPr, assetPr, sceneryPr
#
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore
#
from LxMaya.command import maUtils, maFile, maAsb, maScnAsb
#
from LxMaya.product.data import datScenery
#
from LxMaya.product.op import sceneryOp
#
currentProjectName = projectPr.getMayaProjectName()
#
icon = '/shelf/productionWin.png'
title = 'Assembly Manager'
#
none = ''


#
class IfAssemblyManagerWindow(qtWidgets.QtToolWindow):
    UnitScriptJobWindowName = 'assemblyManagerScriptJobWindow'
    # Scene Box
    dicSwitch = {
        'none': [1, 0, 0, 1, 3, 'None', 'svg_basic@svg#switch'], 'box': [1, 0, 3, 1, 3, 'Box', 'svg_basic@svg#switch'],
        'gpu': [1, 1, 0, 1, 2, 'GPU', 'svg_basic@svg#switch'], 'gpuLodA': [1, 1, 2, 1, 2, 'LOD - 01', 'svg_basic@svg#switch'], 'gpuLodB': [1, 1, 4, 1, 2, 'LOD - 02', 'svg_basic@svg#switch'],
        'proxy': [1, 2, 0, 1, 2, 'Proxy', 'svg_basic@svg#switch'], 'proxyLodA': [1, 2, 2, 1, 2, 'LOD - 01', 'svg_basic@svg#switch'], 'proxyLodB': [1, 2, 4, 1, 2, 'LOD - 02', 'svg_basic@svg#switch'],
        'asset': [1, 3, 0, 1, 6, 'Asset', 'svg_basic@svg#switch'],
        'placeholder': [1, 4, 0, 1, 6, 'Placeholder']
    }
    #
    dicSelect = {
        'keywordFilter': [0, 0, 0, 1, 3, ''], 'keywordFilterSelect': [1, 0, 3, 1, 3, 'Select'],
        'levelFilter': [0, 1, 0, 1, 3, ''], 'levelFilterSelect': [1, 1, 3, 1, 3, 'Select']
    }
    #
    dicVariant = {
        'variant': [0, 0, 0, 1, 2, 'Variant'], 'switchVariant': [1, 0, 2, 1, 2, 'Switch Variant', 'svg_basic@svg#switch']
    }
    #
    dicLevel = {
        0: 'Config(s)',
        'keepSelected': [1, 1, 0, 1, 3, 'Keep Selected'], 'autoSelected': [1, 1, 3, 1, 3, 'Auto Select Assembly'],
        2: 'Action(s)',
        'useGpu': [1, 3, 0, 1, 3, 'GPU', 'svg_basic@svg#switch'], 'useDso': [1, 3, 3, 1, 3, 'Proxy', 'svg_basic@svg#switch'],
        'levelOrig': [1, 4, 0, 1, 2, 'LOD - 00', 'svg_basic@svg#switch'], 'levelA': [1, 4, 2, 1, 2, 'LOD - 01', 'svg_basic@svg#switch'], 'levelB': [1, 4, 4, 1, 2, 'LOD - 02', 'svg_basic@svg#switch'],
        'placeholder': [1, 5, 4, 1, 6, 'Placeholder']
    }
    #
    dicAttr = {
        'visibilityOn': [1, 0, 0, 1, 3, 'Visibility On'], 'visibilityOff': [1, 0, 3, 1, 3, 'Visibility Off'],
        #
        'primaryVisibilityOn': [1, 2, 0, 1, 3, 'Primary Visibility On'], 'primaryVisibilityOff': [1, 2, 3, 1, 3, 'Primary Visibility Off'],
        'castsShadowsOn': [1, 3, 0, 1, 3, 'Casts Shadows On'], 'castsShadowsOff': [1, 3, 3, 1, 3, 'Casts Shadows Off'],
        'receiveShadowsOn': [1, 4, 0, 1, 3, 'Receive Shadows On'], 'receiveShadowsOff': [1, 4, 3, 1, 3, 'Receive Shadows Off'],
        'overrideOn': [1, 6, 0, 1, 3, 'Nde_ShaderRef Override On'], 'overrideOff': [1, 6, 3, 1, 3, 'Nde_ShaderRef Override Off'],
        'useRed': [1, 7, 0, 1, 2, 'Red'], 'useGreen': [1, 7, 2, 1, 2, 'Green'], 'useBlue': [1, 7, 4, 1, 2, 'Blue'],
        #
        'lowQualityDisplayOn': [1, 9, 0, 1, 3, 'Low Quality Display On'],
        'lowQualityDisplayOff': [1, 9, 3, 1, 3, 'Low Quality Display Off'],
        'placeholder': [1, 10, 0, 1, 6, 'Placeholder']
    }
    #
    dicImport = {
        0: 'Config(s)',
        'ignoreHide': [1, 1, 0, 1, 2, 'Ignore Hide'],
        'isHide': [1, 2, 0, 1, 2, 'Hide Assembly'], 'isWithAnimation': [1, 2, 2, 1, 2, 'Animation ( Bake Key )'],
        'isProxyRemoveGpu': [1, 3, 0, 1, 2, 'Remove Gpu ( Proxy )'],
        'isAssetUseReference': [1, 4, 0, 1, 2, 'Reference ( Import Asset )'], 'isAssetWithCfx': [1, 4, 2, 1, 2, 'Fur ( Import Asset )'],
        5: 'Action(s)',
        'importAssemblyBox': [1, 6, 0, 1, 2, 'Import Box [ 0000 ]', 'svg_basic@svg#import'], 'importAssemblyGpu': [1, 6, 2, 1, 2, 'Import GPU [ 0000 ]', 'svg_basic@svg#import'],
        'importAssemblyDso': [1, 7, 0, 1, 2, 'Import Proxy [ 0000 ]', 'svg_basic@svg#import'], 'importAssemblyAsset': [1, 7, 2, 1, 2, 'Import Asset [ 0000 ]', 'svg_basic@svg#import'],
        'importAssemblyCurrent': [1, 8, 0, 1, 4, 'Import Current [ 0000 ]', 'svg_basic@svg#import'],
        9: 'Extend Action(s)',
        'importAssemblyLight': [1, 10, 0, 1, 4, 'Import Light [ 0000 ]', 'svg_basic@svg#import']
    }
    def __init__(self):
        super(IfAssemblyManagerWindow, self).__init__()
        self.widthSet = 800
        self.setDefaultSize(800, 800)
        self.setTitle(title)
        #
        self.assembleTreeBoxItems = []
        #
        self.setupUnit()
        self.setTopToolBar()
        self.setScriptJob()
        #
        self.setLeftToolUiBoxShow()
        self.getAssemblyFilterData()
        self.setListAr()
        self.setListLayer()
        self.setListSet()
        #
        self.getSelectedAssembly()
        #
        self.setQuitConnect(self.delScriptJob)
    #
    def setScriptJob(self):
        self._selectedItemLevelDic = {}
        self._selectedItemVariantDic = {}
        self.selectedAssemblyActiveDic = {}
        self.selectedAssemblyAttrDic = {}
        #
        scriptJobEvn = 'SelectionChanged'
        methods = [self.getSelectedAssembly, self.setAutoSelectAssembly]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        scriptJobEvn = 'displayLayerChange'
        methods = [self.setListLayer]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        scriptJobEvn = 'displayLayerVisibilityChanged'
        methods = [self.setListLayer]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        scriptJobEvn = 'displayLayerManagerChange'
        methods = [self.setListLayer]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        scriptJobEvn = 'SetModified'
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setTopToolBar(self):
        toolBar = self.topToolBar
        #
        self._selectAllButton = qtWidgets.QtIconbutton('svg_basic@svg#checkedAll')
        toolBar.addWidget(self._selectAllButton)
        self._selectAllButton.clicked.connect(self.setSelectAll)
        #
        self._selectClearButton = qtWidgets.QtIconbutton('svg_basic@svg#uncheckedAll')
        toolBar.addWidget(self._selectClearButton)
        self._selectClearButton.clicked.connect(self.setSelectClear)
        #
        self._filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        toolBar.addWidget(self._filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
        toolBar.addWidget(self._refreshButton)
        self._refreshButton.clicked.connect(self.setListAr)
    #
    def setupLeftUiBox(self, toolBoxLayout):
        self._tabWidget = qtWidgets.QtButtonTabGroup()
        toolBoxLayout.addWidget(self._tabWidget)
        #
        scrollBox = qtCore.QScrollArea_()
        self._tabWidget.addTab(scrollBox, 'Switch', 'svg_basic@svg#tab')
        self.setupSwitchTab(scrollBox)
        #
        scrollBox = qtCore.QScrollArea_()
        self._tabWidget.addTab(scrollBox, 'Render', 'svg_basic@svg#tab')
        self.setupRenderTab(scrollBox)
        #
        scrollBox = qtCore.QScrollArea_()
        self._tabWidget.addTab(scrollBox, 'Modify', 'svg_basic@svg#tab')
        self.setupModifyTab(scrollBox)
        #
        scrollBox = qtCore.QScrollArea_()
        self._tabWidget.addTab(scrollBox, 'Import', 'svg_basic@svg#tab')
        self.setupImportTab(scrollBox)
    #
    def setupSwitchTab(self, layout):
        self.levelToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self.levelToolBox)
        self.levelToolBox.setTitle('Level')
        self.setupLevelToolUiBox(self.levelToolBox)
        #
        self.switchToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self.switchToolBox)
        self.switchToolBox.setTitle('Active')
        self.setupActiveToolUiBox(self.switchToolBox)
    #
    def setupRenderTab(self, layout):
        self.variantToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self.variantToolBox)
        self.variantToolBox.setTitle('Variant')
        self.setupVariantToolBox(self.variantToolBox)
        #
        self.selectToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self.selectToolBox)
        self.selectToolBox.setTitle('Select')
        self.setupSelectToolUiBox(self.selectToolBox)
        #
        self.attrToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self.attrToolBox)
        self.attrToolBox.setTitle('Attribute')
        self.setupAttrToolUiBox(self.attrToolBox)
    #
    def setupModifyTab(self, layout):
        self.transformationToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self.transformationToolBox)
        self.transformationToolBox.setTitle('Transformation')
        self.setupTransformationToolBox(self.transformationToolBox)
        #
        self.setModifyToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self.setModifyToolUiBox)
        self.setModifyToolUiBox.setTitle('Set')
        #
        self.layerModifyToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self.layerModifyToolUiBox)
        self.layerModifyToolUiBox.setTitle('Layer')
    #
    def setupImportTab(self, layout):
        self.importToolBox = qtWidgets.QtToolbox()
        layout.addWidget(self.importToolBox)
        self.importToolBox.setTitle('Import')
    #
    def setupRightUiBox(self, toolBoxLayout):
        self.assembleTreeItemDic = {}
        self.arTreeItemLis = []
        #
        self._treeView = qtWidgets_.QTreeWidget_()
        toolBoxLayout.addWidget(self._treeView)
    #
    def setupLevelToolUiBox(self, toolBox):
        self._uiItemLevelDic = {}
        #
        toolBox.setUiData(self.dicLevel)
        self.keepSelectedButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('keepSelected', self.keepSelectedButton)
        self.keepSelectedButton.setChecked(True)
        #
        self.autoSelectedButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('autoSelected', self.autoSelectedButton)
        #
        uiDatumDic = {
            'useGpu': ('GPU', self.setActiveToGpuKeepLevel), 'useDso': ('Proxy', self.setActiveToDsoKeepLevel),
            'levelOrig': ('LOD00', self.setLevelToOrig), 'levelA': ('LOD01', self.setLevelToLodA), 'levelB': ('LOD02', self.setLevelToLodB)

        }
        for k, v in uiDatumDic.items():
            keyword, method = v
            button = qtWidgets.QtPressbutton()
            button.setPercentEnable(True)
            toolBox.addButton(k, button)
            button.setPressable(False)
            self._uiItemLevelDic[keyword] = button
            if method is not None:
                button.clicked.connect(method)
        #
        toolBox.addSeparators()
    #
    def setupActiveToolUiBox(self, toolBox):
        self._selectedItemLis = []
        self._uiItemActiveDic = {}
        #
        toolBox.setUiData(self.dicSwitch)
        uiDatumDic = {
            'none': ('None', self.setActiveToNone), 'box': ('Box', self.setActiveToBox),
            'gpu': ('GPU', self.setActiveToGpu), 'gpuLodA': ('GPU-LOD01', self.setActiveToGpuLodA), 'gpuLodB': ('GPU-LOD02', self.setActiveToGpuLodB),
            'proxy': ('Proxy', self.setActiveToDso), 'proxyLodA': ('Proxy-LOD01', self.setActiveToDsoLodA), 'proxyLodB': ('Proxy-LOD02', self.setActiveToDsoLodB),
            'asset': ('Asset', self.setActiveToAsset)
        }
        for k, v in uiDatumDic.items():
            keyword, method = v
            button = qtWidgets.QtPressbutton()
            button.setPercentEnable(True)
            toolBox.addButton(k, button)
            button.setPressable(False)
            self._uiItemActiveDic[keyword] = button
            if method is not None:
                button.clicked.connect(method)
        #
        toolBox.addSeparators()
    #
    def setupAttrToolUiBox(self, toolBox):
        self._uiItemAttrDic = {}
        #
        toolBox.setUiData(self.dicAttr)
        uiDatumDic = {
            'visibilityOn': self.setVisibilityOn, 'visibilityOff': self.setVisibilityOff,
            'primaryVisibilityOn': self.setProxyPrimaryVisibilityOn, 'primaryVisibilityOff': self.setProxyPrimaryVisibilityOff,
            'castsShadowsOn': self.setDsoCastsShadowsOff, 'castsShadowsOff': self.setDsoCastsShadowsOff,
            'receiveShadowsOn': self.setDsoReceiveShadowsOn, 'receiveShadowsOff': self.setDsoReceiveShadowsOff,
            'overrideOn': self.setProxyAovOverrideOn, 'overrideOff': self.setProxyAovOverrideOff,
            'useRed': None, 'useGreen': None, 'useBlue': None,
            'lowQualityDisplayOn': self.setProxyLowQualityDisplayOn,'lowQualityDisplayOff': self.setProxyLowQualityDisplayOff
        }
        for k, v in uiDatumDic.items():
            button = qtWidgets.QtPressbutton()
            button.setPercentEnable(True)
            toolBox.addButton(k, button)
            button.setPressable(False)
            self._uiItemAttrDic[k] = button
            if v is not None:
                button.clicked.connect(v)
        #
        toolBox.addSeparators()
    #
    def setupSelectToolUiBox(self, toolBox):
        self.asbInScKeywordFilterDic = {}
        self.asbInScLevelFilterDic = {}
        #
        inData = self.dicSelect
        toolBox.setUiData(inData)
        #
        self.keywordFilterLabel = qtWidgets.QtEnterlabel()
        self.keywordFilterLabel.setChooseEnable(True)
        toolBox.addInfo('keywordFilter', self.keywordFilterLabel)
        representations = sceneryPr.assemblyRepresentationsConfig()
        self.keywordFilterLabel.setDatumLis(representations)
        self.keywordFilterLabel.chooseChanged.connect(self.getAssemblyFilterData)
        #
        self.keywordFilterSelBtn = qtWidgets.QtPressbutton()
        self.keywordFilterSelBtn.setPercentEnable(True)
        toolBox.addButton('keywordFilterSelect', self.keywordFilterSelBtn)
        self.keywordFilterSelBtn.setPressable(False)
        self.keywordFilterSelBtn.clicked.connect(self.setSelAsbFilterByKeyword)
        #
        self.levelFilterLabel = qtWidgets.QtEnterlabel()
        self.levelFilterLabel.setChooseEnable(True)
        toolBox.addInfo('levelFilter', self.levelFilterLabel)
        representations = sceneryPr.assembleLodConfig()
        self.levelFilterLabel.setDatumLis(representations)
        self.levelFilterLabel.chooseChanged.connect(self.getAssemblyFilterData)
        #
        self.levelFilterSelBtn = qtWidgets.QtPressbutton()
        self.levelFilterSelBtn.setPercentEnable(True)
        toolBox.addButton('levelFilterSelect', self.levelFilterSelBtn)
        self.levelFilterSelBtn.setPressable(False)
        self.levelFilterSelBtn.clicked.connect(self.setSelAsbFilterByLevel)
        #
        toolBox.addSeparators()
    #
    def setupVariantToolBox(self, toolBox):
        self.variantSwitchData = ()
        #
        toolBox.setUiData(self.dicVariant)
        #
        self.variantLabel = qtWidgets.QtEnterlabel()
        toolBox.addInfo('variant', self.variantLabel)
        self.variantLabel.setChooseEnable(True)
        self.variantLabel.setDatumLis([appVariant.astDefaultVersion])
        #
        self.switchVariantButton = qtWidgets.QtPressbutton()
        self.switchVariantButton.setPercentEnable(True)
        toolBox.addButton('switchVariant', self.switchVariantButton)
        self.switchVariantButton.setPressable(False)
        self.switchVariantButton.clicked.connect(self.setSwitchVariant)
        #
        toolBox.addSeparators()
    #
    def setupTransformationToolBox(self, toolBox):
        self.objectPoseDic = {}
        #
        self._translateLabel = qtWidgets.QtValueEnterlabel()
        toolBox.addWidget(self._translateLabel, 0, 0, 1, 3)
        self._translateLabel.setDefaultValue((0.0, 0.0, 0.0))
        self._translateLabel.setNameText('Translate')
        self._translateLabel.setNameTextWidth(80)
        #
        self._rotateLabel = qtWidgets.QtValueEnterlabel()
        toolBox.addWidget(self._rotateLabel, 1, 0, 1, 3)
        self._rotateLabel.setDefaultValue((0.0, 0.0, 0.0))
        self._rotateLabel.setNameText('Rotate')
        self._rotateLabel.setNameTextWidth(80)
        #
        self._scaleLabel = qtWidgets.QtValueEnterlabel()
        toolBox.addWidget(self._scaleLabel, 2, 0, 1, 3)
        self._scaleLabel.setDefaultValue((1.0, 1.0, 1.0))
        self._scaleLabel.setNameText('Scale')
        self._scaleLabel.setNameTextWidth(80)
        #
        self.getPoseButton = qtWidgets.QtPressbutton()
        toolBox.addWidget(self.getPoseButton, 3, 0, 1, 1)
        self.getPoseButton.setNameText('Get Pose [ 0000 ]')
        self.getPoseButton.setPressable(False)
        self.getPoseButton.clicked.connect(self.getPose)
        #
        self.restPoseButton = qtWidgets.QtPressbutton()
        toolBox.addWidget(self.restPoseButton, 3, 1, 1, 1)
        self.restPoseButton.setNameText('Rest Pose')
        self.restPoseButton.clicked.connect(self.restPose)
        #
        self.trnRandomButton = qtWidgets.QtPressbutton()
        toolBox.addWidget(self.trnRandomButton, 3, 2, 1, 1)
        self.trnRandomButton.setNameText('Random Pose [ 0000 ]')
        self.trnRandomButton.setPressable(False)
        self.trnRandomButton.clicked.connect(self.setRandom)
    #
    def setSetToolUiBox(self):
        toolBox = self.setModifyToolUiBox
        #
        self.setTreeViewBox = qtWidgets_.QTreeWidget_()
        toolBox.addWidget(self.setTreeViewBox, 0, 0, 1, 2)
    #
    def setLayerToolUiBox(self):
        toolBox = self.layerModifyToolUiBox
        #
        self.layerTreeViewBox = qtWidgets_.QTreeWidget_()
        toolBox.addWidget(self.layerTreeViewBox, 0, 0, 1, 2)
        self.layerTreeViewBox.setSingleSelection()
        #
        self.addLayerButton = qtWidgets.QtPressbutton()
        toolBox.addWidget(self.addLayerButton, 1, 0, 1, 1)
        self.addLayerButton.setNameText('Add Assembly  [ 0000 ]')
        self.addLayerButton.setPressable(False)
        self.addLayerButton.clicked.connect(self.setLayerConnectOn)
        #
        self.removeLayerButton = qtWidgets.QtPressbutton()
        toolBox.addWidget(self.removeLayerButton, 1, 1, 1, 1)
        self.removeLayerButton.setNameText('Remove Assembly  [ 0000 ]')
        self.removeLayerButton.setPressable(False)
        self.removeLayerButton.clicked.connect(self.setLayerConnectOff)
        #
        self.selectAssemblyInLayerButton = qtWidgets.QtPressbutton()
        toolBox.addWidget(self.selectAssemblyInLayerButton, 2, 0, 1, 2)
        self.selectAssemblyInLayerButton.setNameText('Select Assembly in Layer [ 0000 ]')
        self.selectAssemblyInLayerButton.setPressable(False)
        self.selectAssemblyInLayerButton.clicked.connect(self.setSelectAssemblyInLayer)
    #
    def setImportToolBox(self):
        inData = self.dicImport
        toolBox = self.importToolBox
        #
        self.ignoreHideButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'ignoreHide', self.ignoreHideButton)
        self.ignoreHideButton.setChecked(True)
        #
        self.isHideButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'isHide', self.isHideButton)
        self.isHideButton.setChecked(True)
        #
        self.isWithAnimationButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'isWithAnimation', self.isWithAnimationButton)
        #
        self.isProxyRemoveGpuButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'isProxyRemoveGpu', self.isProxyRemoveGpuButton)
        self.isProxyRemoveGpuButton.setChecked(True)
        #
        self.isAssetUseReferenceButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'isAssetUseReference', self.isAssetUseReferenceButton)
        self.isAssetUseReferenceButton.setChecked(True)
        #
        self.isAssetWithCfxButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'isAssetWithCfx', self.isAssetWithCfxButton)
        self.isAssetWithCfxButton.setChecked(True)
        #
        self.importAssemblyBoxButton = qtWidgets.QtPressbutton()
        self.importAssemblyBoxButton.setPressable(False)
        toolBox.setButton(inData, 'importAssemblyBox', self.importAssemblyBoxButton)
        self.importAssemblyBoxButton.clicked.connect(self.setImportAssemblyBox)
        #
        self.importAssemblyGpuButton = qtWidgets.QtPressbutton()
        self.importAssemblyGpuButton.setPressable(False)
        toolBox.setButton(inData, 'importAssemblyGpu', self.importAssemblyGpuButton)
        self.importAssemblyGpuButton.clicked.connect(self.setImportAssemblyGpu)
        #
        self.importAssemblyDsoButton = qtWidgets.QtPressbutton()
        self.importAssemblyDsoButton.setPressable(False)
        toolBox.setButton(inData, 'importAssemblyDso', self.importAssemblyDsoButton)
        self.importAssemblyDsoButton.clicked.connect(self.setImportAssemblyDso)
        #
        self.importAssemblyAssetButton = qtWidgets.QtPressbutton()
        self.importAssemblyAssetButton.setPressable(False)
        toolBox.setButton(inData, 'importAssemblyAsset', self.importAssemblyAssetButton)
        self.importAssemblyAssetButton.clicked.connect(self.setImportAssemblyAsset)
        #
        self.importAssemblyCurrentButton = qtWidgets.QtPressbutton()
        self.importAssemblyCurrentButton.setPressable(False)
        toolBox.setButton(inData, 'importAssemblyCurrent', self.importAssemblyCurrentButton)
        self.importAssemblyCurrentButton.clicked.connect(self.setImportAssemblyCurrent)
        #
        self.importAssemblyLightButton = qtWidgets.QtPressbutton()
        self.importAssemblyLightButton.setPressable(False)
        toolBox.setButton(inData, 'importAssemblyLight', self.importAssemblyLightButton)
        self.importAssemblyLightButton.clicked.connect(self.setImportLight)
        #
        toolBox.setSeparators(inData)
    #                                                                                        <<<<<< Tree Box - [ Build ]
    def setAssembleTreeViewBox(self):
        def setActionData():
            actions = [
                ('Refresh', 'svg_basic@svg#refresh', True, self.setListAr),
                (),
                ('Select All', 'svg_basic@svg#checkedAll', True, self.setSelectAll),
                ('Select Clear', 'svg_basic@svg#uncheckedAll', True, self.setSelectClear),
            ]
            treeBox.setActionData(actions)
        #
        treeBox = self._treeView
        #
        maxWidth = self.widthSet
        #
        treeBox.setColumns(
            ['Assembly Reference', 'Name', 'Variant', 'Active', 'Level'],
            [4, 2, 2, 2, 2],
            maxWidth
        )
        #
        treeBox.itemSelectionChanged.connect(self.setNodeSelCmd)
        treeBox.focusIn.connect(self.setAssembleViewBoxRefresh)
        treeBox.setFilterConnect(self._filterEnterLabel)
        #
        setActionData()
    #
    def setListAr(self):
        self.assembleTreeBoxItems = []
        self.assembleTreeItemDic = {}
        self.arTreeItemLis = []
        #
        self.assembleSearchDic = {}
        assemblyData = datScenery.getAssemblyReferenceActiveDatumDic()
        self._treeView.clear()
        if assemblyData:
            maxValue = len(assemblyData)
            self.setMaxProgressValue(maxValue)
            for k, v in assemblyData.items():
                self.updateProgress()
                for seq, i in enumerate(v):
                    assemblyReferencePath, assetName = i
                    activeItem = maAsb.getAssemblyActive(assemblyReferencePath)
                    #
                    arItem = qtWidgets_.QTreeWidgetItem_()
                    #
                    self._treeView.addItem(arItem)
                    #
                    self.setAssemblyTreeItem(arItem, assemblyReferencePath, activeItem, assetName)
                    #
                    self.assembleTreeBoxItems.append(arItem)
                    #
                    self.assembleTreeItemDic[assemblyReferencePath] = arItem
                    self.arTreeItemLis.append(arItem)
                    #
                    searchKey = assetName + str(seq)
                    self.assembleSearchDic[searchKey] = arItem
        #
        self._treeView.setFilterExplainRefresh()
        #
        self.setSelectButtonState()
    #
    def setSetTreeViewBox(self):
        def setActionData():
            actions = [
                ('Refresh', 'svg_basic@svg#refresh', True, self.setListSet),
                (),
                ('Add Proxy', 'menu#addMenu', True),
                ('Remove Proxy', 'menu#deleteMenu', True),
                (),
                ('Select Proxy', 'svg_basic@svg#uncheckedAll', True),
                (),
                ('Clear Set', 'menu#deleteMenu', True),
            ]
            treeBox.setActionData(actions)
        #
        maxWidth = 400 - 60
        treeBox = self.setTreeViewBox
        treeBox.setColumns(
            ['Set', 'Count'],
            [4, 1],
            maxWidth
        )
        setActionData()
        # treeBox.itemSelectionChanged.connect(self.setSelectAssemblyButtonState)
    #
    def setLayerTreeViewBox(self):
        maxWidth = 400 - 60
        treeBox = self.layerTreeViewBox
        treeBox.setColumns(
            ['Layer', 'Count', 'State'],
            [2, 1, 1],
            maxWidth
        )
        treeBox.itemSelectionChanged.connect(self.setSelectAssemblyButtonState)
    #
    def setListSet(self):
        treeBox = self.setTreeViewBox
        inData = maUtils.getSets()
        treeBox.clear()
        if inData:
            for mSet in inData:
                showExplain = maUtils._toNodeName(mSet, useMode=1)
                setItem = qtWidgets_.QTreeWidgetItem_([showExplain])
                treeBox.addItem(setItem)
                setItem.setItemMayaIcon(0, 'set', none)
                #
                setItem.name = mSet
                setItem.path = mSet
    #
    def setListLayer(self):
        treeBox = self.layerTreeViewBox
        inData = maUtils.getDisplayLayers()
        treeBox.clear()
        if inData:
            for i in inData:
                layerName = i
                layerItem = qtWidgets_.QTreeWidgetItem_([layerName])
                layerItem.setItemMayaIcon(0, 'displayLayer')
                layerItem.setText(1, str(len(maUtils.getConnectAttrData(layerName, 'visibility'))))
                layerItem.setText(2, ['Off', 'On'][maUtils.getAttrDatum(layerName, 'visibility')])
                treeBox.addItem(layerItem)
    #
    def setAssemblyTreeItem(self, treeItem, objectPath, activeItem, assetName=None):
        objectName = maUtils._toNodeName(objectPath, useMode=1)
        #
        visible = maUtils.getAttrDatum(objectPath, 'visibility')
        #
        treeItem.setItemMayaIcon(0, 'assemblyReference', ['off', none][visible])
        treeItem.setText(0, objectName)
        if assetName:
            treeItem.setText(1, assetName)
        # Variant
        assetVariant = datScenery.getAssemblyActiveVariant(objectPath)
        treeItem.setText(2, assetVariant)
        # Active
        active = [activeItem, activeItem.split('-LOD')[0]]['-LOD' in activeItem]
        treeItem.setText(3, active)
        # Level
        level = maAsb.getAssemblyLodLevel(objectPath)[3:]
        treeItem.setText(4, level)
        #
        if activeItem == 'None':
            treeItem.setItemMayaIcon(0, 'assemblyReference', 'warning')
        #
        adData = maUtils.getAttrDatum(objectPath, 'definition')
        if not os.path.isfile(adData):
            treeItem.setItemMayaIcon(0, 'assemblyReference', 'error')
        #
        treeItem.name = objectName
        treeItem.path = objectPath
        #
        self.setAttrScriptJob(treeItem, objectPath)
    #
    def setAttrScriptJob(self, treeItem, objectPath):
        def setIndexRefresh1():
            if treeItem in self.arTreeItemLis:
                boolean = maUtils.getAttrDatum(objectPath, 'visibility')
                treeItem.setItemMayaIcon(0, 'assemblyReference', ['off', none][boolean])
        #
        def setIndexRefresh2():
            if treeItem in self.arTreeItemLis:
                assetVariant = datScenery.getAssemblyActiveVariant(objectPath)
                treeItem.setText(2, assetVariant)
        #
        def setIndexRefresh3():
            if treeItem in self.arTreeItemLis:
                activeItem = maAsb.getAssemblyActive(objectPath)
                active = [activeItem, activeItem.split('-LOD')[0]]['-LOD' in activeItem]
                treeItem.setText(3, active)
        #
        def setIndexRefresh4():
            if treeItem in self.arTreeItemLis:
                level = maAsb.getAssemblyLodLevel(objectPath)[3:]
                treeItem.setText(4, level)
        #
        attr = objectPath + '.' + 'visibility'
        maUtils.setCreateAttrChangedScriptJob(self.UnitScriptJobWindowName, attr, setIndexRefresh1)
        #
        attr = objectPath + '.' + 'representations'
        maUtils.setCreateAttrChangedScriptJob(self.UnitScriptJobWindowName, attr, setIndexRefresh2)
        #
        attr = objectPath + '.' + 'representations'
        maUtils.setCreateAttrChangedScriptJob(self.UnitScriptJobWindowName, attr, [setIndexRefresh3, setIndexRefresh4])
    #
    def setAssembleViewBoxRefresh(self):
        assemblyObjectCount = len(datScenery.getAssetAssemblyReferenceLis())
        assembleViewBoxItemCount = self._treeView.topLevelItemCount()
        if assemblyObjectCount != assembleViewBoxItemCount:
            self.setListAr()
    #
    def setLeftToolUiBoxShow(self):
        self.setSetToolUiBox()
        self.setLayerToolUiBox()
        self.setImportToolBox()
        #
        self.setAssembleTreeViewBox()
        #
        self.setSetTreeViewBox()
        self.setLayerTreeViewBox()
    # UI State
    def setTreeItemState(self):
        _selectedItemLis = self._selectedItemLis
        treeItemData = self.assembleTreeItemDic
        for k, v in treeItemData.items():
            if k in _selectedItemLis:
                v.setSelected(True)
            else:
                v.setSelected(False)
    #
    def _refreshButtonMethod(self, uiDatumDic, selectedDatumDic):
        if selectedDatumDic:
            maxCount = len(self._selectedItemLis)
            for k, v in uiDatumDic.items():
                item = v
                if k in selectedDatumDic:
                    count = len(selectedDatumDic[k])
                else:
                    count = 0
                #
                item.setPressable(True)
                item.setPercent(maxCount, count)
        else:
            for k, v in uiDatumDic.items():
                item = v
                item.setPressable(False)
                item.setPercentRest()
    #
    def setLevelButtonState(self):
        uiDatumDic = self._uiItemLevelDic
        selectedDatumDic = self._selectedItemLevelDic
        self._refreshButtonMethod(uiDatumDic, selectedDatumDic)
    #
    def setSwitchButtonState(self):
        uiDatumDic = self._uiItemActiveDic
        selectedDatumDic = self.selectedAssemblyActiveDic
        self._refreshButtonMethod(uiDatumDic, selectedDatumDic)
    @staticmethod
    def getAssetVariantLis(projectName, assetClass, assetName):
        lis = []
        osPath = assetPr.astUnitAssemblyFolder(
            lxCore_.LynxiRootIndex_Server, projectName, assetClass, assetName
        )
        if lxBasic.isOsExist(osPath):
            textLis = lxBasic.getOsFileBasenameLisByPath(osPath)
            if textLis:
                for i in textLis:
                    adFile = assetPr.astUnitAssemblyDefinitionFile(
                        lxCore_.LynxiRootIndex_Server,
                        projectName,
                        assetClass, assetName, i, lxCore_.LynxiProduct_Asset_Link_Assembly
                    )[1]
                    #
                    if lxBasic.isOsExist(adFile):
                        lis.append(i)
        return lis
    #
    def setVariantButtonState(self):
        self.variantSwitchData = ()
        #
        projectName = currentProjectName
        #
        chooseLabel = self.variantLabel
        button = self.switchVariantButton
        inData = self._selectedItemVariantDic
        if inData:
            maxCount = len(self._selectedItemLis)
            enable = len(inData) == 1
            if enable:
                variantLis = []
                assetVariant = appVariant.astDefaultVersion
                count = 0
                for k, v in inData.items():
                    assetName, assetVariant = k.split(' - ')
                    assetClass = None
                    self.variantSwitchData = projectName, assetName, v
                    count = len(v)
                    variantLis = self.getAssetVariantLis(projectName, assetClass, assetName)
                #
                chooseLabel.setDatumLis(variantLis)
                chooseLabel.setChoose(assetVariant)
                #
                button.setPressable(True)
                button.setPercent(maxCount, count)
            else:
                chooseLabel.setChooseClear()
                chooseLabel.setDatumLis([appVariant.astDefaultVersion])
                #
                button.setPercentRest()
                button.setPressable(False)
    #
    def setSelectButtonState(self):
        keywordFilterData = self.asbInScKeywordFilterDic
        levelFilterData = self.asbInScLevelFilterDic
        keyword = self.keywordFilterLabel.datum()
        showLevel = self.levelFilterLabel.datum()
        if keywordFilterData:
            maxCount = len(self.assembleTreeBoxItems)
            if keyword in keywordFilterData:
                count = len(keywordFilterData[keyword])
                self.keywordFilterSelBtn.setPressable(True)
                self.keywordFilterSelBtn.setPercent(maxCount, count)
            else:
                self.keywordFilterSelBtn.setPressable(True)
                self.keywordFilterSelBtn.setPercentRest()
        else:
            self.keywordFilterSelBtn.setPressable(True)
            self.keywordFilterSelBtn.setPercentRest()
        #
        level = none.join(showLevel.split(' - '))
        if levelFilterData:
            maxCount = len(self.assembleTreeBoxItems)
            if level in levelFilterData:
                count = len(levelFilterData[level])
                self.levelFilterSelBtn.setPressable(True)
                self.levelFilterSelBtn.setPercent(maxCount, count)
            else:
                self.levelFilterSelBtn.setPressable(False)
                self.levelFilterSelBtn.setPercentRest()
        else:
            self.levelFilterSelBtn.setPressable(False)
            self.levelFilterSelBtn.setPercentRest()
    #
    def setAttributeButtonState(self):
        uiDatumDic = self._uiItemAttrDic
        selectedData = self.selectedAssemblyAttrDic
        subSelectedData = self._selectedItemLevelDic
        if selectedData:
            maxCount = len(self._selectedItemLis)
            for k, v in uiDatumDic.items():
                item = v
                item.setPressable(True)
                if k in selectedData:
                    count = len(selectedData[k])
                    item.setPercent(maxCount, count)
                else:
                    item.setPercentRest()
                    if not 'Proxy' in subSelectedData:
                        if (
                                k.startswith('primaryVisibility')
                                or k.startswith('castsShadows')
                                or k.startswith('receiveShadows')
                                or k.startswith('override')
                                or k.startswith('lowQualityDisplay')
                        ):
                            item.setPressable(False)
                            item.setPercentRest()
        else:
            for k, v in uiDatumDic.items():
                item = v
                item.setPercentRest()
                item.setPressable(False)
    #
    def setChannelButtonState(self):
        selectedData = self._selectedItemLis
        self.getPoseButton.setNameText('Get Pose [ %s ]' % str(len(selectedData)).zfill(4))
        self.getPoseButton.setPressable([False, True][len(selectedData) > 0])
        self.trnRandomButton.setNameText('Random Pose [ %s ]' % str(len(self.objectPoseDic)).zfill(4))
        self.trnRandomButton.setPressable([False, True][len(self.objectPoseDic) > 0])
        #
        self.addLayerButton.setNameText('Add Assembly [ %s ]' % str(len(selectedData)).zfill(4))
        self.addLayerButton.setPressable([False, True][len(selectedData) > 0])
        self.removeLayerButton.setNameText('Remove Assembly [ %s ]' % str(len(selectedData)).zfill(4))
        self.removeLayerButton.setPressable([False, True][len(selectedData) > 0])
    #
    def setSelectAssemblyButtonState(self):
        connectData = self.getAssemblyInLayer()
        button = self.selectAssemblyInLayerButton
        button.setNameText('Select Assembly in Layer [ %s ]' % str(len(connectData)).zfill(4))
        button.setPressable([False, True][len(connectData) > 0])
    #
    def setImportButtonState(self):
        selectedData = self._selectedItemLis
        keyword = 'Box'
        self.importAssemblyBoxButton.setNameText('Import %s [ %s ]' % (keyword, str(len(selectedData)).zfill(4)))
        self.importAssemblyBoxButton.setPressable([False, True][len(selectedData) > 0])
        keyword = 'GPU'
        self.importAssemblyGpuButton.setNameText('Import %s [ %s ]' % (keyword, str(len(selectedData)).zfill(4)))
        self.importAssemblyGpuButton.setPressable([False, True][len(selectedData) > 0])
        keyword = 'Proxy'
        self.importAssemblyDsoButton.setNameText('Import %s [ %s ]' % (keyword, str(len(selectedData)).zfill(4)))
        self.importAssemblyDsoButton.setPressable([False, True][len(selectedData) > 0])
        keyword = 'Asset'
        self.importAssemblyAssetButton.setNameText('Import %s [ %s ]' % (keyword, str(len(selectedData)).zfill(4)))
        self.importAssemblyAssetButton.setPressable([False, True][len(selectedData) > 0])
        keyword = 'Current'
        self.importAssemblyCurrentButton.setNameText('Import %s [ %s ]' % (keyword, str(len(selectedData)).zfill(4)))
        self.importAssemblyCurrentButton.setPressable([False, True][len(selectedData) > 0])
        keyword = 'Light'
        self.importAssemblyLightButton.setNameText('Import %s [ %s ]' % (keyword, str(len(selectedData)).zfill(4)))
        self.importAssemblyLightButton.setPressable([False, True][len(selectedData) > 0])
    # Script Job Connection
    def getSelectedAssembly(self):
        self._selectedItemLis = []
        self._selectedItemLevelDic = {}
        self._selectedItemVariantDic = {}
        self.selectedAssemblyActiveDic = {}
        self.selectedAssemblyAttrDic = {}
        assemblyObjects = maAsb.getSelSceneryObject(objects=cmds.ls(selection=True, long=1))
        if assemblyObjects:
            for assemblyReferencePath in assemblyObjects:
                self._selectedItemLis.append(assemblyReferencePath)
                activeItem = maAsb.getAssemblyActive(assemblyReferencePath)
                # Level ( GPU )
                if activeItem.startswith('GPU'):
                    self._selectedItemLevelDic.setdefault('GPU', []).append(assemblyReferencePath)
                # Level ( Proxy )
                elif activeItem.startswith('Proxy'):
                    self._selectedItemLevelDic.setdefault('Proxy', []).append(assemblyReferencePath)
                    #
                    isOverrideData = datScenery.getProxyIsOverrideAov(assemblyReferencePath)
                    if isOverrideData:
                        self.selectedAssemblyAttrDic.setdefault('overrideOn', []).append(assemblyReferencePath)
                    if not isOverrideData:
                        self.selectedAssemblyAttrDic.setdefault('overrideOff', []).append(assemblyReferencePath)
                    #
                    isPrimaryVisibility = datScenery.getProxyIsPrimaryVisibility(assemblyReferencePath)
                    if isPrimaryVisibility:
                        self.selectedAssemblyAttrDic.setdefault('primaryVisibilityOn', []).append(assemblyReferencePath)
                    else:
                        self.selectedAssemblyAttrDic.setdefault('primaryVisibilityOff', []).append(assemblyReferencePath)
                    isLowQualityDisplay = datScenery.getProxyIsLowQualityDisplay(assemblyReferencePath)
                    if isLowQualityDisplay:
                        self.selectedAssemblyAttrDic.setdefault('lowQualityDisplayOn', []).append(assemblyReferencePath)
                    isHighQualityDisplay = datScenery.getProxyIsHighQualityDisplay(assemblyReferencePath)
                    if isHighQualityDisplay:
                        self.selectedAssemblyAttrDic.setdefault('lowQualityDisplayOff', []).append(assemblyReferencePath)
                    #
                    isCastsShadows = datScenery.getProxyIsCastsShadows(assemblyReferencePath)
                    if isCastsShadows:
                        self.selectedAssemblyAttrDic.setdefault('castsShadowsOn', []).append(assemblyReferencePath)
                    else:
                        self.selectedAssemblyAttrDic.setdefault('castsShadowsOff', []).append(assemblyReferencePath)
                    #
                    isReceiveShadows = datScenery.getProxyIsReceiveShadows(assemblyReferencePath)
                    if isReceiveShadows:
                        self.selectedAssemblyAttrDic.setdefault('receiveShadowsOn', []).append(assemblyReferencePath)
                    else:
                        self.selectedAssemblyAttrDic.setdefault('receiveShadowsOff', []).append(assemblyReferencePath)
                # Level ( Box and Asset )
                else:
                    self._selectedItemLevelDic.setdefault(activeItem, []).append(assemblyReferencePath)
                #
                lodLevel = maAsb.getAssemblyLodLevel(assemblyReferencePath)
                self._selectedItemLevelDic.setdefault(lodLevel, []).append(assemblyReferencePath)
                # Variant
                assetName, assetVariant = datScenery.getAssemblyUnitInfo(assemblyReferencePath)
                variantKey = '%s - %s' % (assetName, assetVariant)
                self._selectedItemVariantDic.setdefault(variantKey, []).append(assemblyReferencePath)
                # Active
                self.selectedAssemblyActiveDic.setdefault(activeItem, []).append(assemblyReferencePath)
                # Visibility
                isVisibleData = maUtils.getAttrDatum(assemblyReferencePath, 'visibility')
                if isVisibleData:
                    self.selectedAssemblyAttrDic.setdefault('visibilityOn', []).append(assemblyReferencePath)
                if not isVisibleData:
                    self.selectedAssemblyAttrDic.setdefault('visibilityOff', []).append(assemblyReferencePath)
        # UI State
        self.setLevelButtonState()
        self.setVariantButtonState()
        self.setSwitchButtonState()
        self.setAttributeButtonState()
        #
        self.setTreeItemState()
        self.setChannelButtonState()
        self.setImportButtonState()
    #
    def setAutoSelectAssembly(self):
        if self.autoSelectedButton.isChecked():
            assemblyObjects = maAsb.getSelSceneryObject(objects=cmds.ls(selection=True, long=1))
            cmds.select(assemblyObjects)
    # Util Method
    def setActive(self, keyword):
        colorConfig = sceneryPr.assemblyColorConfig()
        toSelect = []
        selectedData = self.selectedAssemblyActiveDic
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k != keyword:
                    for i in v:
                        assemblyReferencePath = i
                        toSelect.append(assemblyReferencePath)
                        targetItem = keyword
                        if keyword == 'None':
                            targetItem = none
                        maAsb.setAssemblyActive(assemblyReferencePath, targetItem)
                        if keyword in colorConfig:
                            color = colorConfig[keyword]
                            maUtils.setNodeOverrideColor(assemblyReferencePath, color)
        if self.keepSelectedButton.isChecked():
            if keyword.startswith('Proxy') or keyword == 'Asset':
                cmds.select(toSelect)
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setLodLevel(self, lodLevel):
        colorConfig = sceneryPr.assemblyColorConfig()
        toSelect = []
        isSelect = False
        selectedData = self._selectedItemLevelDic
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k.startswith('LOD'):
                    if k != lodLevel:
                        for i in v:
                            assemblyReferencePath = i
                            toSelect.append(assemblyReferencePath)
                            activeItem = maAsb.getAssemblyActive(assemblyReferencePath)
                            # Set Active Item and Color
                            if activeItem.startswith('GPU') or activeItem.startswith('Proxy'):
                                activeKey = ['GPU', 'Proxy'][activeItem.startswith('Proxy')]
                                levelLabel = [none, lodLevel][lodLevel != 'LOD00']
                                targetItem = [activeKey, activeKey + '-' + lodLevel][levelLabel != none]
                                maAsb.setAssemblyActive(assemblyReferencePath, targetItem)
                                color = colorConfig[targetItem]
                                maUtils.setNodeOverrideColor(assemblyReferencePath, color)
                                if activeKey == 'Proxy':
                                    isSelect = True
                            # Set Color
                            else:
                                defaultKeyword = 'GPU'
                                levelLabel = [none, lodLevel][lodLevel != 'LOD00']
                                targetItem = [defaultKeyword, defaultKeyword + '-' + lodLevel][levelLabel != none]
                                color = colorConfig[targetItem]
                                maUtils.setNodeOverrideColor(assemblyReferencePath, color)
        if self.keepSelectedButton.isChecked():
            if isSelect:
                cmds.select(toSelect)
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setActiveKeepLevel(self, mainKeyword):
        selectedData = self._selectedItemLevelDic
        toSelect = []
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k != mainKeyword:
                    for i in v:
                        assemblyReferencePath = i
                        toSelect.append(assemblyReferencePath)
                        lodLevel = maAsb.getAssemblyLodLevel(assemblyReferencePath)
                        levelLabel = [none, lodLevel][lodLevel != 'LOD00']
                        targetItem = [mainKeyword, mainKeyword + '-' + lodLevel][levelLabel != none]
                        maAsb.setAssemblyActive(assemblyReferencePath, targetItem)
        if self.keepSelectedButton.isChecked():
            if mainKeyword == 'Proxy':
                cmds.select(toSelect)
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setVisibility(self, boolean):
        treeItemData = self.assembleTreeItemDic
        selectedData = self.selectedAssemblyAttrDic
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k.startswith('visibility'):
                    for i in v:
                        assemblyReferencePath = i
                        maUtils.setAttrBooleanDatum(assemblyReferencePath, 'visibility', boolean)
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setProxyPrimaryVisibility(self, boolean):
        selectedData = self.selectedAssemblyAttrDic
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k.startswith('primaryVisibility'):
                    for i in v:
                        assemblyReferencePath = i
                        proxyNode = datScenery.getAssemblyReferenceProxyNode(assemblyReferencePath)
                        maUtils.setAttrBooleanDatum(proxyNode, 'primaryVisibility', boolean)
        #
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setProxyCastsShadows(self, boolean):
        selectedData = self.selectedAssemblyAttrDic
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k.startswith('castsShadows'):
                    for i in v:
                        assemblyReferencePath = i
                        proxyNode = datScenery.getAssemblyReferenceProxyNode(assemblyReferencePath)
                        maUtils.setAttrBooleanDatum(proxyNode, 'castsShadows', boolean)
        #
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setDsoReceiveShadows(self, boolean):
        selectedData = self.selectedAssemblyAttrDic
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k.startswith('receiveShadows'):
                    for i in v:
                        assemblyReferencePath = i
                        proxyNode = datScenery.getAssemblyReferenceProxyNode(assemblyReferencePath)
                        maUtils.setAttrBooleanDatum(proxyNode, 'receiveShadows', boolean)
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setProxyAovOverride(self, boolean):
        selectedData = self.selectedAssemblyAttrDic
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k.startswith('override'):
                    for i in v:
                        assemblyReferencePath = i
                        proxyObject = datScenery.getAssemblyReferenceProxyObject(assemblyReferencePath)
                        maUtils.setAttrBooleanDatum(proxyObject, 'override', boolean)
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setProxyLowQualityDisplay(self, boolean):
        selectedData = self.selectedAssemblyAttrDic
        attrName = 'cacheFileName'
        if selectedData:
            maxValue = len(selectedData)
            for seq, (k, v) in enumerate(selectedData.items()):
                self.setProgressValue(seq + 1, maxValue)
                if k.startswith('lowQualityDisplay'):
                    for i in v:
                        assemblyReferencePath = i
                        proxyObject = datScenery.getAssemblyReferenceProxyObject(assemblyReferencePath)
                        useBoxAttr = proxyObject + '.box'
                        useGpuAttr = proxyObject + '.gpu'
                        if boolean:
                            cmds.setAttr(useBoxAttr, 1)
                            cmds.setAttr(useGpuAttr, 0)
                        if not boolean:
                            cmds.setAttr(useBoxAttr, 0)
                            cmds.setAttr(useGpuAttr, 1)
        #
        self.getSelectedAssembly()
        self.getAssemblyFilterData()
    #
    def setLayerConnect(self, boolean):
        layer = self.getLayer()
        selectedData = self._selectedItemLis
        if selectedData:
            maxValue = len(selectedData)
            for seq, i in enumerate(selectedData):
                self.setProgressValue(seq + 1, maxValue)
                assemblyReferencePath = i
                if layer:
                    if boolean:
                        maUtils.setAttrConnect(layer + '.visibility', assemblyReferencePath + '.visibility')
                    if not boolean:
                        maUtils.setAttrDisconnect(layer + '.visibility', assemblyReferencePath + '.visibility')
    #
    def _assemblyImportMethod(self, keyword):
        projectName = currentProjectName
        #
        selectedData = self._selectedItemLis
        treeItemData = self.assembleTreeItemDic
        #
        isIgnoreHide = self.ignoreHideButton.isChecked()
        #
        isHide = self.isHideButton.isChecked()
        isWithAnimation = self.isWithAnimationButton.isChecked()
        isRemoveGpu = self.isProxyRemoveGpuButton.isChecked()
        isUseReference = self.isAssetUseReferenceButton.isChecked()
        isWithCfxAsset = self.isAssetWithCfxButton.isChecked()
        if selectedData:
            maxValue = len(selectedData)
            for seq, i in enumerate(selectedData):
                assemblyReference = i
                #
                asbNamespace = maAsb.getAssemblyNamespace(assemblyReference)
                asbNamespace += '_import'
                #
                self.setProgressValue(seq + 1, maxValue)
                #
                importEnabled = True
                if isIgnoreHide is True:
                    isObjectVisible = maUtils.isNodeVisible(assemblyReference)
                    if not isObjectVisible:
                        importEnabled = False
                #
                if importEnabled is True:
                    if keyword == 'Current':
                        keyword = maAsb.getAssemblyCurrentItem(assemblyReference)
                    #
                    asbName = maUtils._toNodeName(assemblyReference, useMode=1)
                    importObjectName = asbNamespace + ':' + asbName + '_' + 'in' + keyword.capitalize()
                    #
                    assetClass = None
                    assetName, assetVariant = datScenery.getAssemblyUnitInfo(assemblyReference)
                    osFile = none
                    if keyword == 'Asset':
                        osFile = assetPr.astUnitAssemblyProductFile(
                            projectName, assetName, assetVariant
                        )[1]
                    elif keyword == 'Box':
                        osFile = assetPr.astUnitAssemblyBoxCacheFile(
                            projectName, assetName
                        )[1]
                    elif keyword == 'GPU':
                        osFile = assetPr.astUnitAssemblyGpuCacheFile(
                            projectName, assetName
                        )[1]
                    elif keyword == 'Proxy':
                        osFile = assetPr.astUnitAssemblyProxyCacheFile(
                            projectName, assetName, assetVariant
                        )[1]
                    #
                    if os.path.isfile(osFile):
                        if keyword == 'Proxy':
                            importObjectName = asbName + '_' + 'in' + keyword.capitalize()
                        else:
                            importObjectName = asbNamespace + ':' + asbName + '_' + 'in' + keyword.capitalize()
                        #
                        if not maUtils.isAppExist(importObjectName):
                            if keyword == 'Proxy':
                                if isRemoveGpu:
                                    maScnAsb.setCreateArnoldProxy(importObjectName, osFile)
                                else:
                                    maFile.setFileImport(osFile)
                            elif keyword == 'Asset':
                                if isUseReference:
                                    maFile.setMaFileReference(osFile, asbNamespace)
                                else:
                                    maFile.setFileImport(osFile, asbNamespace)
                            else:
                                maFile.setFileImport(osFile, asbNamespace)
                            # Asset
                            if keyword == 'Asset':
                                assetUnitRoot = '|' + assetPr.astUnitRootGroupName(assetName, asbNamespace)
                                if maUtils.isAppExist(assetUnitRoot):
                                    maUtils.setObjectAddParentGroup(assetUnitRoot, importObjectName)
                                else:
                                    modelGroupName = '|' + assetPr.astUnitModelLinkGroupName(assetName, asbNamespace)
                                    if maUtils.isAppExist(modelGroupName):
                                        maUtils.setObjectAddParentGroup(modelGroupName, importObjectName)
                            # Box and GPU
                            elif keyword == 'Box' or keyword == 'GPU':
                                modelGroupName = '|' + assetPr.astUnitModelLinkGroupName(assetName, asbNamespace)
                                if maUtils.isAppExist(modelGroupName):
                                    maUtils.setObjectAddParentGroup(modelGroupName, importObjectName)
                                else:
                                    geometryGroupName = '|' + assetPr.astUnitModelProductGroupName(assetName, asbNamespace)
                                    if maUtils.isAppExist(geometryGroupName):
                                        maUtils.setObjectAddParentGroup(geometryGroupName, importObjectName)
                            # Proxy
                            elif keyword == 'Proxy':
                                if not isRemoveGpu:
                                    astAssemblyProxyObject = assetPr.astAssemblyProxyObjectName(assetName)
                                    if maUtils.isAppExist(astAssemblyProxyObject):
                                        maUtils.setNodeRename(astAssemblyProxyObject, importObjectName)
                                        maUtils.setObjectLockTransform(importObjectName, 0)
                            #
                            if maUtils.isAppExist(importObjectName):
                                maObj = importObjectName
                                targetObject = assemblyReference
                                #
                                # maUtils.getPos_(importObjectName, targetObject)
                                matrix = maUtils.getNodeWorldMatrix(targetObject)
                                maUtils.setNodeWorldMatrix(importObjectName, matrix)
                                #
                                if isWithAnimation:
                                    startFrame, endFrame = maUtils.getFrameRange()
                                    maUtils.getAnimationKey(importObjectName, assemblyReference, startFrame, endFrame)
                            #
                            if isHide:
                                maUtils.setHide(assemblyReference)
    #
    def setImportLight(self):
        projectName = currentProjectName
        #
        selectedData = self._selectedItemLis
        #
        if selectedData:
            maxValue = len(selectedData)
            for seq, i in enumerate(selectedData):
                self.setProgressValue(seq + 1, maxValue)
                assemblyReferencePath = i
                importObjectName = maUtils._toNodeName(assemblyReferencePath, useMode=1) + '_' + 'inLight'
                #
                assetName, assetVariant = datScenery.getAssemblyUnitInfo(assemblyReferencePath)
                osFile = assetPr.astUnitProductFile(
                    lxCore_.LynxiRootIndex_Server,
                    projectName, None, assetName, assetVariant, lxCore_.LynxiProduct_Scene_Link_Light
                )[1]
                #
                if os.path.isfile(osFile):
                    if not maUtils.isAppExist(importObjectName):
                        maFile.setFileImport(osFile)
                        lightGroup = assetPr.astUnitLightLinkGroupName(assetName)
                        if maUtils.isAppExist(lightGroup):
                            maUtils.setObjectLockTransform(lightGroup)
                            maUtils.setObjectAddParentGroup('|' + lightGroup, importObjectName)
                        #
                        if maUtils.isAppExist(importObjectName):
                            targetObject = assemblyReferencePath
                            #
                            # maUtils.getPos_(importObjectName, targetObject)
                            matrix = maUtils.getNodeWorldMatrix(targetObject)
                            maUtils.setNodeWorldMatrix(importObjectName, matrix)
                            #
                            maUtils.getPosition(importObjectName, targetObject, keepConstraint=True)
                            maUtils.getScale(importObjectName, targetObject, keepConstraint=True)
                            #
                            lightGroupPath = '|' + importObjectName + '|' + lightGroup
                            lightGroupScaleAttr = lightGroupPath + '.' + 'lightScale'
                            #
                            if maUtils.isAppExist(lightGroupScaleAttr):
                                sourceAttr = assemblyReferencePath + '.' + 'scaleY'
                                if not maUtils.isAttrDestination(lightGroupScaleAttr):
                                    maUtils.setAttrConnect(sourceAttr, lightGroupScaleAttr)
    #
    def setActiveToNone(self):
        keyword = 'None'
        self.setActive(keyword)
    #
    def setActiveToBox(self):
        keyword = 'Box'
        self.setActive(keyword)
    #
    def setActiveToGpu(self):
        keyword = 'GPU'
        self.setActive(keyword)
    #
    def setActiveToGpuLodA(self):
        keyword = 'GPU-LOD01'
        self.setActive(keyword)
    #
    def setActiveToGpuLodB(self):
        keyword = 'GPU-LOD02'
        self.setActive(keyword)
    #
    def setActiveToDso(self):
        keyword = 'Proxy'
        self.setActive(keyword)
    #
    def setActiveToDsoLodA(self):
        keyword = 'Proxy-LOD01'
        self.setActive(keyword)
    #
    def setActiveToDsoLodB(self):
        keyword = 'Proxy-LOD02'
        self.setActive(keyword)
    #
    def setActiveToAsset(self):
        keyword = 'Asset'
        self.setActive(keyword)
    #
    def setLevelToOrig(self):
        lodLevel = 'LOD00'
        self.setLodLevel(lodLevel)
    #
    def setLevelToLodA(self):
        lodLevel = 'LOD01'
        self.setLodLevel(lodLevel)
    #
    def setLevelToLodB(self):
        lodLevel = 'LOD02'
        self.setLodLevel(lodLevel)
    #
    def setActiveToGpuKeepLevel(self):
        mainKeyword = 'GPU'
        self.setActiveKeepLevel(mainKeyword)
    #
    def setActiveToDsoKeepLevel(self):
        mainKeyword = 'Proxy'
        self.setActiveKeepLevel(mainKeyword)
    #
    def setSwitchVariant(self):
        switchData = self.variantSwitchData
        assetVariant = self.variantLabel.datum()
        if switchData:
            assetClass = None
            projectName, assetName, assemblyObjectArray = switchData
            if assemblyObjectArray:
                maxValue = len(assemblyObjectArray)
                self.setMaxProgressValue(maxValue)
                for assemblyReferencePath in assemblyObjectArray:
                    self.updateProgress()
                    sceneryOp.setAssemblyVariantSwitch(
                        assemblyReferencePath, projectName, assetClass, assetName, assetVariant
                    )
                    #
                    assemblyAnnotation = appVariant.assemblyUnitShowName(assetName, assetVariant)
                    sceneryOp.setAssemblyAnnotationSwitch(assemblyReferencePath, assemblyAnnotation)
    #
    def setVisibilityOn(self):
        self.setVisibility(True)
    #
    def setVisibilityOff(self):
        self.setVisibility(False)
    #
    def setProxyPrimaryVisibilityOn(self):
        self.setProxyPrimaryVisibility(True)
    #
    def setProxyPrimaryVisibilityOff(self):
        self.setProxyPrimaryVisibility(False)
    #
    def setDsoCastsShadowsOn(self):
        self.setProxyCastsShadows(True)
    #
    def setDsoCastsShadowsOff(self):
        self.setProxyCastsShadows(False)
    #
    def setDsoReceiveShadowsOn(self):
        self.setDsoReceiveShadows(True)
    #
    def setDsoReceiveShadowsOff(self):
        self.setDsoReceiveShadows(False)
    #
    def setProxyAovOverrideOn(self):
        self.setProxyAovOverride(True)
    #
    def setProxyAovOverrideOff(self):
        self.setProxyAovOverride(False)
    #
    def setProxyLowQualityDisplayOn(self):
        self.setProxyLowQualityDisplay(True)
    #
    def setProxyLowQualityDisplayOff(self):
        self.setProxyLowQualityDisplay(False)
    #
    def restPose(self):
        objectPoseData = self.objectPoseDic
        selectedData = self._selectedItemLis
        if objectPoseData:
            for k, v in objectPoseData.items():
                object = k
                if object in selectedData:
                    trnData, rotData, sclData = v
                    trnX, trnY, trnZ = trnData
                    cmds.setAttr(object + '.translate', trnX, trnY, trnZ)
                    rotX, rotY, rotZ = rotData
                    cmds.setAttr(object + '.rotate', rotX, rotY, rotZ)
                    sclX, sclY, sclZ = sclData
                    cmds.setAttr(object + '.scale', sclX, sclY, sclZ)
    #
    def getPose(self):
        self.objectPoseDic = {}
        selectedData = self._selectedItemLis
        if selectedData:
            for object in selectedData:
                trnData = cmds.getAttr(object + '.translate')
                rotData = cmds.getAttr(object + '.rotate')
                sclData = cmds.getAttr(object + '.scale')
                self.objectPoseDic[object] = trnData[0], rotData[0], sclData[0]
        self.setChannelButtonState()
    @staticmethod
    def floatRange(minimum, maximum):
        return [i/100.0 for i in range(int(minimum*100), int(maximum*100))]
    #
    def setRandom(self):
        objectPoseData = self.objectPoseDic
        selectedData = self._selectedItemLis
        if objectPoseData:
            for k, v in objectPoseData.items():
                node = k
                if node in selectedData:
                    trnData, rotData, sclData = v
                    #
                    trnX, trnY, trnZ = trnData
                    trnValueX, trnValueY, trnValueZ = self._translateLabel.value()
                    trnRandX = [(0, 0), self.floatRange(-trnValueX, trnValueX)][trnValueX != 0]
                    trnRandY = [(0, 0), self.floatRange(-trnValueY, trnValueY)][trnValueY != 0]
                    trnRandZ = [(0, 0), self.floatRange(-trnValueZ, trnValueZ)][trnValueZ != 0]
                    cmds.setAttr(
                        node + '.translate',
                        trnX + choice(trnRandX),
                        trnY + choice(trnRandY),
                        trnZ + choice(trnRandZ))
                    #
                    rotX, rotY, rotZ = rotData
                    rotValueX, rotValueY, rotValueZ = self._rotateLabel.value()
                    rotRandX = [(0, 0), self.floatRange(-rotValueX, rotValueX)][rotValueX != 0]
                    rotRandY = [(0, 0), self.floatRange(-rotValueY, rotValueY)][rotValueY != 0]
                    rotRandZ = [(0, 0), self.floatRange(-rotValueZ, rotValueZ)][rotValueZ != 0]
                    cmds.setAttr(
                        node + '.rotate',
                        rotX + choice(rotRandX),
                        rotY + choice(rotRandY),
                        rotZ + choice(rotRandZ))
                    #
                    sclX, sclY, sclZ = sclData
                    sclValueX, sclValueY, sclValueZ = self._scaleLabel.value()
                    sclRandX = [(1, 1), self.floatRange(1.0, sclValueX)][sclValueX > 1]
                    sclRandY = [(1, 1), self.floatRange(1.0, sclValueY)][sclValueY > 1]
                    sclRandZ = [(1, 1), self.floatRange(1.0, sclValueZ)][sclValueZ > 1]
                    randomValue = choice(sclRandX)
                    cmds.setAttr(
                        node + '.scale',
                        sclX * randomValue,
                        sclY * randomValue,
                        sclZ * randomValue)
    #
    def setLayerConnectOn(self):
        self.setLayerConnect(True)
    #
    def setLayerConnectOff(self):
        self.setLayerConnect(False)
    #
    def setSelectAssemblyInLayer(self):
        connectData = self.getAssemblyInLayer()
        maUtils.setNodeSelect(connectData)
    #
    def setImportAssemblyBox(self):
        keyword = 'Box'
        self._assemblyImportMethod(keyword)
    #
    def setImportAssemblyGpu(self):
        keyword = 'GPU'
        self._assemblyImportMethod(keyword)
    #
    def setImportAssemblyDso(self):
        keyword = 'Proxy'
        self._assemblyImportMethod(keyword)
    #
    def setImportAssemblyAsset(self):
        keyword = 'Asset'
        self._assemblyImportMethod(keyword)
    #
    def setImportAssemblyCurrent(self):
        keyword = 'Current'
        self._assemblyImportMethod(keyword)
    #
    def getAssemblyFilterData(self):
        self.asbInScKeywordFilterDic = {}
        self.asbInScLevelFilterDic = {}
        assemblyData = datScenery.getAssetAssemblyReferenceLis()
        for i in assemblyData:
            assemblyReferencePath = i
            # Keyword Filter
            activeItem = maAsb.getAssemblyActive(assemblyReferencePath)
            self.asbInScKeywordFilterDic.setdefault(activeItem, []).append(assemblyReferencePath)
            # Level Filter
            lodLevel = maAsb.getAssemblyLodLevel(assemblyReferencePath)
            self.asbInScLevelFilterDic.setdefault(lodLevel, []).append(assemblyReferencePath)
        #
        self.setSelectButtonState()
    #
    def setSelAsbFilterByKeyword(self):
        filterData = self.asbInScKeywordFilterDic
        keyword = self.keywordFilterLabel.datum()
        for k, v in filterData.items():
            if k == keyword:
                cmds.select(v)
    #
    def setSelAsbFilterByLevel(self):
        filterData = self.asbInScLevelFilterDic
        keyword = none.join(self.levelFilterLabel.datum().split(' - '))
        for k, v in filterData.items():
            if k == keyword:
                cmds.select(v)
    #
    def setNodeSelCmd(self):
        treeBox = self._treeView
        if treeBox.hasFocus():
            data = treeBox.selectedItemPaths()
            if data:
                cmds.select(data)
            else:
                cmds.select(clear=1)
    #
    def setSelObjForAction(self):
        treeBox = self._treeView
        data = treeBox.selectedItemPaths()
        if data:
            cmds.select(data)
        else:
            cmds.select(clear=1)
    #
    def getLayer(self):
        selectedTreeItemNames = self.layerTreeViewBox.selectedItemTexts()
        if selectedTreeItemNames:
            return selectedTreeItemNames[0]
    #
    def getAssemblyInLayer(self):
        layer = self.getLayer()
        connectData = []
        if layer:
            connectData = maUtils.getConnectAttrData(layer, 'visibility')
        return connectData
    #
    def setSelectAll(self):
        treeBox = self._treeView
        treeBox.selectAll()
        #
        self.setSelObjForAction()
    #
    def setSelectClear(self):
        treeBox = self._treeView
        treeBox.clearSelection()
        #
        self.setSelObjForAction()
    @qtCore.uiShowMethod_
    def windowShow(self):
        self.uiShow()
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.addWidget(widget)
        mainLayout = qtCore.QGridLayout_(widget)
        mainLayout.setContentsMargins(2, 2, 2, 2)
        mainLayout.setSpacing(2)
        #
        self.topToolBar = qtWidgets_.xToolBar()
        mainLayout.addWidget(self.topToolBar, 0, 0, 1, 2)
        #
        self.topToolBar = qtWidgets_.xToolBar()
        mainLayout.addWidget(self.topToolBar, 0, 0, 1, 2)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        mainLayout.addWidget(leftExpandWidget, 1, 0, 1, 1)
        leftExpandWidget.setUiWidth(self.widthSet / 2)
        #
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        #
        leftWidget = qtCore.QWidget_()
        leftScrollArea.addWidget(leftWidget)
        self.leftLayout = qtCore.QVBoxLayout_(leftWidget)
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setSpacing(0)
        self.setupLeftUiBox(self.leftLayout)
        #
        rightWidget = qtCore.QWidget_()
        self.treeViewLayout = qtCore.QVBoxLayout_(rightWidget)
        self.treeViewLayout.setContentsMargins(0, 0, 5, 5)
        self.treeViewLayout.setSpacing(0)
        self.setupRightUiBox(self.treeViewLayout)
        #
        mainLayout.addWidget(rightWidget, 1, 1, 1, 1)


@qtCore.uiSetupShowMethod
def tableShow():
    ui = IfAssemblyManagerWindow()
    ui.uiShow()