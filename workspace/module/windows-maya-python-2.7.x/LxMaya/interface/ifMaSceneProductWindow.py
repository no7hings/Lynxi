# coding=utf-8
from LxCore import lxBasic, lxScheme
#
from LxCore.preset import pipePr, appVariant
#
from LxCore.preset.prod import projectPr, assetPr, scenePr
#
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore, qtLog, qtProgress
#
#
from LxMaya.interface.ifWidgets import ifMaSceneryToolUnit, ifMaSceneToolUnit, ifMaAnimToolUnit
#
from LxMaya.command import maUtils
#
from LxMaya.product.data import datScene, datAnim
#
currentProjectName = projectPr.getMayaProjectName()
# Type Config
typeSet = appVariant.astBasicClassifications
typeLabel = appVariant.assetClassifyAbbDic
typeDic = appVariant.assetClassifyFullDic
# Utilities Label
infoNonExistsLabel = appVariant.infoNonExistsLabel
astDefaultVersion = appVariant.astDefaultVersion
# Animation Config
animStages = appVariant.animStages
#
none = ''
#
_header = 'window#productionWin'
_title = 'Scene Production'
_version = lxScheme.Python().version


#
class IfSceneProductToolWindow(qtWidgets.QtToolWindow):
    widthSet = 400
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfSceneProductToolWindow, self).__init__(parent)
        #
        self.setNameText(_title)
        self.setIndexText(_version)
        #
        self.setDefaultSize(self.widthSet, 875)
        # Animation Information
        self.projectName = projectPr.getMayaProjectName()
        self.episode = None
        self.sequence = None
        self.shot = None
        self.stage = 'layout'
        #
        self.sceneIndex = None
        self.sceneClass = None
        self.sceneName = None
        self.sceneVariant = None
        self.sceneStage = None
        #
        self.startFrame = 0
        self.endFrame = 0
        # Animation Camera
        self.animationCamera = None
        #
        self.assetItemDic = {}
        self.selectedItemDic = {}
        self.unknownReferenceDic = {}
        self.sceneryDataDic = {}
        #
        self.variantBoxWidth = ()
        #
        self.cacheData = []
        self.rigError = []
        #
        self.rigDataDic = {}
        self.rigErrorData = []
        self.rigUsedData = []
        #
        self.setupUnit()
        #
        self.sceneAssetData = []
        self._inspectAssetDatumLis = []
        #
        self._initPanel()
    #
    def setTreeBoxHeaderHiddenSwitch(self):
        self.treeBox.setHeaderHidden(self.expandBox.isExpanded())
    # Create Panel
    def setScCreateBoxShow(self):
        pass
    #
    def setScCreateBoxHide(self):
        self.createWidget.hide()
    #
    def setScTopToolBar(self, layout):
        self._filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._infoLabel = qtWidgets.QtEnterlabel()
        layout.addWidget(self._infoLabel)
        self._infoLabel.setNameTextWidth(0)
        #
        self.filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        layout.addWidget(self.filterEnterLabel)
        # self.treeBox.setFilterConnect(self.filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
        layout.addWidget(self._refreshButton)
        # self._refreshButton.clicked.connect(self.setRefresh)
    #
    def setScLeftToolBox(self):
        uiData = [
            ('scSceneryTool', 'window#sceneryToolPanel', 'Scenery Unit', u'''场景工具模块''', True, ()),
            ('scLayoutTool', 'toolBar#layout', 'Layout Unit', u'''布景工具模块''', True, ()),
            ('scAnimationTool', 'toolBar#animation', 'Animation Unit', u'''动画工具模块''', True, ()),
            ('scLightTool', 'toolBar#light', 'Light Unit', u'''灯光工具模块''', True, ()),
            ('scUtilsTool', 'window#utilsToolPanel', 'Utilities Unit', u'''通用工具模块''', True, ()),
            ('scAnimUploadTool', 'window#uploadToolPanel', 'Upload Unit', u'''上传工具模块''', False, ()),
            ('scLightUploadTool', 'window#renderToolPanel', 'Upload Unit', u'''上传工具模块''', False, ())
        ]
        for i in uiData:
            key, iconKeyword, title, uiTip, visible, commands = i
            toggleButton = None
            toggleButtonCreateCmd = 'self.{0}ToggleButton = qtWidgets_.QRadioButton_();toggleButton = self.{0}ToggleButton'.format(key)
            exec toggleButtonCreateCmd
            toggleButton.setIconExplain(iconKeyword, 32, 32)
            if visible is False:
                toggleButton.hide()
            if commands:
                for j in commands:
                    toggleButton.clicked.connect(j)
            toggleButton.setTooltip(uiTip)
            #
            toolGroupBox = None
            toolGroupBoxCreateCmd = 'self.{0}GroupBox = qtWidgets.QtToolboxGroup();toolGroupBox = self.{0}GroupBox'.format(key)
            exec toolGroupBoxCreateCmd
            toolGroupBox.hide()
            toolGroupBox.setExpanded(True)
            toolGroupBox.setTitle(title)
            toggleButton.toggled.connect(toolGroupBox.setVisible)
            self.leftToolScrollBox.addWidget(toolGroupBox)
            self.leftBottomToolBar.addWidget(toggleButton)
    #
    def setScLeftToolBoxShow(self):
        def setScLayoutToolBox():
            self.IfScLayoutToolUnit = ifMaAnimToolUnit.IfScLayoutToolUnit()
            self.scLayoutToolboxGroup.addWidget(self.IfScLayoutToolUnit)
            self.IfScLayoutToolUnit.setConnectObject(self)
            #
            self.IfScLayoutToolUnit.refreshMethod()
        #
        def setScAnimationToolBox():
            unit = ifMaAnimToolUnit.IfScAnimationLinkToolUnit()
            self.scAnimationToolboxGroup.addWidget(unit)
            unit.setConnectObject(self)
            #
            unit.refreshMethod()
        #
        def setScSceneryToolBox():
            unit = ifMaSceneryToolUnit.IfScnLinkToolUnit()
            self.scSceneryToolboxGroup.addWidget(unit)
            unit.setConnectObject(self)
            #
            unit.refreshMethod()
        #
        def setScLightToolBox():
            unit = ifMaSceneToolUnit.IfScLightLinkToolUnit()
            self.scLightToolboxGroup.addWidget(unit)
            unit.setConnectObject(self)
            #
            unit.refreshMethod()
        #
        def setScUtilsToolBox():
            unit = ifMaAnimToolUnit.IfScUtilToolUnit()
            self.scUtilsToolboxGroup.addWidget(unit)
            unit.setConnectObject(self)
            #
            unit.refreshMethod()
        #
        def setScAnimUploadToolBox():
            unit = ifMaAnimToolUnit.IfScAnimUploadToolUnit()
            self.scAnimUploadToolboxGroup.addWidget(unit)
            unit.setConnectObject(self)
            #
            unit.refreshMethod()
        #
        def setScLightUploadToolBox():
            unit = ifMaAnimToolUnit.IfScLightUploadToolUnit()
            self.scLightUploadToolboxGroup.addWidget(unit)
            unit.setConnectObject(self)
            #
            unit.refreshMethod()
            #
            self.scLightUploadToolToggleButton.clicked.connect(unit.refreshMethod)
            self.setQuitConnect(unit.delScriptJob)
        #
        methods = [
            setScLayoutToolBox,
            setScAnimationToolBox,
            setScSceneryToolBox,
            setScLightToolBox,
            setScUtilsToolBox,
            setScAnimUploadToolBox,
            setScLightUploadToolBox
        ]
        # View Progress
        explain = '''Build Scene Tool Unit(s)'''
        maxValue = len(methods)
        progressBar = qtProgress.viewSubProgress(explain, maxValue)
        for i in methods:
            progressBar.updateProgress()
            i()
        #
        self.toolWidget.show()
    #
    def setScRightToolBox(self):
        uiData = [
            ('scAstViewer', 'window#referencePanel', 'Scene ( Asset ) Viewer', u'''点击显示镜头（资产）查看器''', True, ()),
            ('scAssemblyViewer', 'window#sceneryToolPanel', 'Scene ( Assembly ) Viewer', u'''点击显示镜头（组装）查看器''', True, ()),
            ('scMayaComposeViewer', 'window#constantToolPanel', 'Scene ( Maya - Compose ) Viewer', u'''点击显示镜头（组成）查看器''', True, ()),
            ('scFileComposeViewer', 'window#fileToolPanel', 'Scene ( File - Compose ) Viewer', u'''点击显示镜头（文件）查看器''', True, ())
        ]
        for i in uiData:
            key, iconKeyword, title, uiTip, visible, commands = i
            toggleButton = None
            toggleButtonCreateCmd = 'self.{0}ToggleButton = qtWidgets_.QRadioButton_();toggleButton = self.{0}ToggleButton'.format(
                key)
            exec toggleButtonCreateCmd
            #
            toggleButton.setIconExplain(iconKeyword, 32, 32)
            if visible is False:
                toggleButton.hide()
            if commands:
                for j in commands:
                    toggleButton.clicked.connect(j)
            toggleButton.setTooltip(uiTip)
            #
            toolGroupBox = None
            toolGroupBoxCreateCmd = 'self.{0}GroupBox = qtWidgets.QtToolboxGroup();toolGroupBox = self.{0}GroupBox'.format(
                key)
            exec toolGroupBoxCreateCmd
            #
            toolGroupBox.hide()
            toolGroupBox.setExpanded(True)
            toolGroupBox.setTitle(title)
            toggleButton.toggled.connect(toolGroupBox.setVisible)
            #
            self.rightToolScrollBox.addWidget(toolGroupBox)
            self.rightBottomToolBar.addWidget(toggleButton)
    #
    def setScRightToolBoxShow(self):
        def setScAstViewer():
            self.scAstViewer = ifMaSceneToolUnit.IfScAssetToolUnit()
            self.scAstViewerGroupBox.addWidget(self.scAstViewer)
            self.scAstViewer.setConnectObject(self)
            #
            self.scAstViewerToggleButton.clicked.connect(self.scAstViewer.refreshMethod)
        #
        def setScMayaComposeViewer():
            self.scMayaComposeViewer = ifMaSceneToolUnit.IfScMayaComposeToolUnit()
            self.scMayaComposeViewerGroupBox.addWidget(self.scMayaComposeViewer)
            self.scMayaComposeViewer.setConnectObject(self)
            #
            self.scMayaComposeViewerToggleButton.clicked.connect(self.scMayaComposeViewer.refreshMethod)
        #
        def setScFileComposeViewer():
            self.scFileComposeViewer = ifMaSceneToolUnit.IfScOsComposeToolUnit()
            self.scFileComposeViewerGroupBox.addWidget(self.scFileComposeViewer)
            self.scFileComposeViewer.setConnectObject(self)
            #
            self.scFileComposeViewerToggleButton.clicked.connect(self.scFileComposeViewer.refreshMethod)
        #
        methods = [
            setScAstViewer,
            setScMayaComposeViewer,
            setScFileComposeViewer
        ]
        # View Progress
        explain = '''Build Scene Viewer Unit(s)'''
        maxValue = len(methods)
        progressBar = qtProgress.viewSubProgress(explain, maxValue)
        for i in methods:
            progressBar.updateProgress()
            i()
        #
        self.toolWidget.show()
    #
    def setSel(self):
        treeBox = self.treeBox
        if treeBox.hasFocus():
            objects = self.getSelAsset()
            if objects:
                maUtils.setNodeSelect(objects)
            if not objects:
                maUtils.setSelClear()
    #
    def setSelSceneAsset(self):
        pass
    #
    def _initScAnimTool(self):
        self.scAnimUploadToolToggleButton.show()
        self.scAnimUploadToolToggleButton.setChecked(True)
        #
        self.scAstViewerToggleButton.setChecked(True)
        self.scAstViewer.refreshMethod()
    #
    def _initScFxTool(self):
        self.scAnimUploadToolToggleButton.show()
        self.scAnimUploadToolToggleButton.setChecked(True)
        #
        self.scAstViewerToggleButton.setChecked(True)
        self.scAstViewer.refreshMethod()
    #
    def _initScLightTool(self):
        self.scLightUploadToolToggleButton.show()
        self.scLightUploadToolToggleButton.setChecked(True)
        #
        self.scMayaComposeViewerToggleButton.setChecked(True)
        self.scMayaComposeViewer.refreshMethod()
    #
    def setSceneInfo(self, sceneIndex, sceneClass, sceneName, sceneVariant):
        message = scenePr.getSceneViewInfo(sceneIndex, sceneClass, sceneVariant)
        self._infoLabel.setDatum(message)
        #
        self.sceneClass = sceneClass
        self.sceneName = sceneName
        self.sceneVariant = sceneVariant
        #
        startFrame, endFrame = maUtils.getFrameRange()
        print 'startFrame = {}\nendFrame = {}\n'.format(startFrame, endFrame)
        #
        self.startFrame = startFrame
        self.endFrame = endFrame
    #
    def _initPanel(self):
        sceneInfoLis = datScene.getSceneInfo(printEnable=True)
        if sceneInfoLis:
            self.setPlaceholderEnable(False)
            #
            sceneInfo = sceneInfoLis[0]
            sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage = sceneInfo
            #
            self.sceneIndex = sceneIndex
            self.sceneClass = sceneClass
            self.sceneName = sceneName
            self.sceneVariant = sceneVariant
            self.sceneStage = sceneStage
            #
            self.animationCamera = scenePr.scSceneCameraName(sceneName, sceneVariant)
            self.setSceneInfo(sceneIndex, sceneClass, sceneName, sceneVariant)
            #
            self.setScRightToolBox()
            self.setScRightToolBoxShow()
            #
            self.setScLeftToolBox()
            self.setScLeftToolBoxShow()
            #
            if scenePr.isScSimulationLink(sceneStage) or scenePr.isScSolverLink(sceneStage):
                self._initScFxTool()
            elif scenePr.isScLightLink(sceneStage):
                self._initScLightTool()
            else:
                self._initScAnimTool()
            #
            title = 'Scene ( {} ) Upload'.format(lxBasic.str_camelcase2prettify(scenePr.getSceneLink(sceneStage)))
            self.setTitle(title)
        else:
            self.setPlaceholderEnable(True)
            #
            self.setScCreateBoxShow()
    #
    def getAssetStatisticsData(self):
        projectName = self.projectName
        #
        self.assetStatisticsData = datAnim.getAssetStatisticsData(projectName)
    #
    def getRigError(self):
        return self.rigError
    #
    def getSelAsset(self):
        lis = []
        rigData = self.rigDataDic
        #
        treeBox = self.treeBox
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            for i in selectedItems:
                if i in rigData:
                    type, name, subNumber, variant, astUnitModelProductGroup, referenceNode = rigData[i]
                    namespace = maUtils.getReferenceNamespace(referenceNode)
                    astUnitModelProductGroup = '%s:%s' % (namespace, assetPr.astUnitModelProductGroupName(name))
                    lis.append(astUnitModelProductGroup)
        return lis
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.addWidget(widget)
        mainLayout = qtCore.QHBoxLayout_(widget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        #
        self.createWidget = qtCore.QWidget_()
        self.createWidget.hide()
        mainLayout.addWidget(self.createWidget)
        #
        createLayout = qtCore.QHBoxLayout_(self.createWidget)
        createLayout.setContentsMargins(0, 0, 0, 0)
        createLayout.setSpacing(0)
        #
        self.leftCreateWidget = qtCore.QWidget_()
        createLayout.addWidget(self.leftCreateWidget)
        self.leftCreateWidget.setMinimumWidth(self.widthSet)
        self.leftCreateWidget.setMaximumWidth(self.widthSet)
        #
        leftCreateLayout = qtCore.QVBoxLayout_(self.leftCreateWidget)
        leftCreateLayout.setContentsMargins(0, 0, 0, 0)
        leftCreateLayout.setSpacing(0)
        #
        self.rightCreateWidget = qtCore.QWidget_()
        self.rightCreateWidget.hide()
        createLayout.addWidget(self.rightCreateWidget)
        #
        self.toolWidget = qtCore.QWidget_()
        self.toolWidget.hide()
        mainLayout.addWidget(self.toolWidget)
        #
        toolLayout = qtCore.QGridLayout_(self.toolWidget)
        toolLayout.setContentsMargins(4, 4, 4, 4)
        toolLayout.setSpacing(2)
        #
        self.topToolBar = qtWidgets_.xToolBar()
        toolLayout.addWidget(self.topToolBar, 0, 0, 1, 2)
        #
        self.expandBox = qtWidgets_.QtExpandWidget()
        toolLayout.addWidget(self.expandBox, 1, 0, 1, 1)
        self.expandBox.setUiWidth(self.widthSet)
        self.expandBox.expanded.connect(self.setTreeBoxHeaderHiddenSwitch)
        #
        self.leftToolWidget = qtCore.QWidget_()
        self.expandBox.addWidget(self.leftToolWidget)
        #
        leftToolLayout = qtCore.QVBoxLayout_(self.leftToolWidget)
        leftToolLayout.setContentsMargins(0, 0, 0, 0)
        leftToolLayout.setSpacing(0)
        #
        self.leftToolScrollBox = qtCore.QScrollArea_()
        leftToolLayout.addWidget(self.leftToolScrollBox)
        #
        self.leftBottomToolBar = qtWidgets_.xToolBar()
        leftToolLayout.addWidget(self.leftBottomToolBar)
        # Right
        self.rightToolWidget = qtCore.QWidget_()
        toolLayout.addWidget(self.rightToolWidget, 1, 1, 1, 1)
        self.rightToolWidget.setMinimumWidth(self.widthSet)
        #
        rightToolLayout = qtCore.QVBoxLayout_(self.rightToolWidget)
        rightToolLayout.setContentsMargins(0, 0, 0, 0)
        rightToolLayout.setSpacing(0)
        #
        self.rightToolScrollBox = qtCore.QScrollArea_()
        rightToolLayout.addWidget(self.rightToolScrollBox)
        #
        self.rightToolboxGroup = qtWidgets.QtToolboxGroup()
        self.rightToolboxGroup.hide()
        self.rightToolboxGroup.setExpanded(True)
        self.rightToolScrollBox.addWidget(self.rightToolboxGroup)
        #
        self.treeBox = qtWidgets_.QTreeWidget_()
        self.rightToolboxGroup.addWidget(self.treeBox)
        self.treeBox.setHeaderHidden(True)
        self.treeBox.itemSelectionChanged.connect(self.setSel)
        #
        self.rightBottomToolBar = qtWidgets_.xToolBar()
        rightToolLayout.addWidget(self.rightBottomToolBar)
        #
        self.logWindow = qtLog.logWin_()
        #
        self.setScTopToolBar(self.topToolBar)


@qtCore.uiSetupShowMethod
def tableShow():
    w = IfSceneProductToolWindow()
    w.uiShow()


#
def helpShow():
    helpDirectory = pipePr.mayaHelpDirectory('animation')
    lxBasic.setOsFolderOpen(helpDirectory)