# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore import lxBasic, lxConfigure, lxProgress
#
from LxCore.preset import pipePr, appVariant
#
from LxCore.preset.prod import projectPr, sceneryPr
#
from LxUi import uiCore
#
from LxUi.qt import uiWidgets_, uiWidgets
#
from LxMaya.interface.ifWidgets import ifMaSceneryToolUnit
#
from LxMaya.product.data import datScenery
#
from LxMaya.interface.ifCommands import maAstTreeViewCmds
#
currentProjectName = projectPr.getMayaProjectName()
#
none = ''
#
_header = 'window#productionWin'
_title = 'Scenery Production'
_version = lxConfigure.Version().active()


#
class IfSceneryProductToolWindow(uiWidgets.UiToolWindow):
    widthSet = 400
    def __init__(self, parent=uiCore.getAppWindow()):
        super(IfSceneryProductToolWindow, self).__init__(parent)
        self.setDefaultSize(self.widthSet, 875)
        #
        self.setNameText(_title)
        self.setIndexText(_version)
        # Scenery Information
        self.projectName = projectPr.getMayaProjectName()
        self.sceneryIndex = None
        self.sceneryClass = None
        self.sceneryName = None
        self.sceneryVariant = None
        self.sceneryStage = None
        #
        self.name = None
        self.variant = None
        #
        self.setupPanel()
        #
        self.setTreeViewBox()
        #
        self.getSceneryInfo()
    # Create Panel
    def setScnCreateBoxShow(self):
        pass
    #
    def setScnCreateBoxHide(self):
        self.createWidget.hide()
    #
    def setScnTopToolBar(self, layout):
        self._filterButton = uiWidgets.UiIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._infoLabel = uiWidgets.UiEnterlabel()
        layout.addWidget(self._infoLabel)
        self._infoLabel.setNameTextWidth(0)
        #
        self.filterEnterLabel = uiWidgets.UiFilterEnterlabel()
        layout.addWidget(self.filterEnterLabel)
        self.treeBox.setFilterConnect(self.filterEnterLabel)
        #
        self._refreshButton = uiWidgets.UiIconbutton('svg_basic@svg#refresh')
        layout.addWidget(self._refreshButton)
        # self._refreshButton.clicked.connect(self.setRefresh)
    #
    def setupLeftWidget(self, toolBoxLayout, toolBarLayout):
        uiDatumLis = [
            ('scnUtilityTool', ifMaSceneryToolUnit.IfScnUtilityToolUnit, True, []),
            ('scnAssemblyInfoTool', ifMaSceneryToolUnit.IfScnAssemblyInfoToolUnit, True, []),
            ('scnUploadTool', ifMaSceneryToolUnit.IfScnUploadToolUnit, True, [])
        ]
        # View Progress
        explain = '''Build Asset Interface Unit(s)'''
        maxValue = len(uiDatumLis)
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        for i in uiDatumLis:
            progressBar.updateProgress()
            #
            key, toolUnitClass, visible, connectMethodLis = i
            # Unit
            toolUnit = None
            toolUnitCreateCmd = 'self.{0}Unit = toolUnitClass();toolUnit = self.{0}Unit'.format(key)
            exec toolUnitCreateCmd
            toolUnit.setConnectObject(self)
            toolUnit.refreshMethod()
            #
            links = toolUnit.UnitConnectLinks
            title = toolUnit.UnitTitle
            iconKeyword = toolUnit.UnitIcon
            tooltip = toolUnit.UnitTooltip
            # Toggle Button
            toggleButton = None
            toggleButtonCreateCmd = 'self.{0}ToggleButton = uiWidgets_.QRadioButton_();toggleButton = self.{0}ToggleButton'.format(key)
            exec toggleButtonCreateCmd
            toggleButton.setIconExplain(iconKeyword, 32, 32)
            #
            if connectMethodLis:
                for j in connectMethodLis:
                    toggleButton.clicked.connect(j)
            toggleButton.setTooltip(tooltip)
            # Tool Group
            toolGroupBox = None
            toolGroupBoxCreateCmd = 'self.{0}GroupBox = uiWidgets.UiToolGroupBox();toolGroupBox = self.{0}GroupBox'.format(key)
            exec toolGroupBoxCreateCmd
            toolGroupBox.hide()
            toolGroupBox.setExpanded(True)
            toolGroupBox.setTitle(title)
            toolBoxLayout.addWidget(toolGroupBox)
            toolGroupBox.addWidget(toolUnit)
            #
            toggleButton.toggled.connect(toolGroupBox.setVisible)
            toggleButton.clicked.connect(toolUnit.refreshMethod)
            toolBarLayout.addWidget(toggleButton)
        #
        self.toolWidget.show()
    #
    def setScnRightToolBox(self):
        self.scnHierarchyToggleButton = uiWidgets_.QRadioButton_()
        #
        uiData = [
            (self.scnHierarchyToggleButton, 'window#hierarchyPanel', u'点击显示场景层级', True, (self.setScnHierarchyView,))
        ]
        for i in uiData:
            toggleButton, iconKeyword, uiTip, visible, commands = i
            toggleButton.setIconExplain(iconKeyword, 32, 32)
            if visible is False:
                toggleButton.hide()
            if commands:
                for command in commands:
                    toggleButton.clicked.connect(command)
            toggleButton.setTooltip(uiTip)
            self.rightBottomToolBar.addWidget(toggleButton)
    #
    def setScnRightToolBoxShow(self):
        self.setScnRightToolBox()
    #
    def setTreeViewBox(self):
        self.treeItem = ()
        self.selectedGroupItem = ()
        #
        self.treeBox.itemSelectionChanged.connect(self.setSel)
    #
    def setSel(self):
        data = self.getSelAsb()
        if data:
            cmds.select(data)
    #
    def setScnHierarchyViewBox(self):
        maxWidth = self.widthSet * 2
        columnNameData = ['Group : Assemble', 'Active', 'Explain']
        self.treeBox.setColumns_(columnNameData, maxWidth)
        self.rightToolGroupBox.setTitle('Scenery Hierarchy')
    #
    def setScnHierarchyView(self):
        self.searchDic = {}
        #
        sceneryName = self.sceneryName
        sceneryVariant = self.sceneryVariant
        sceneryStage = self.sceneryStage
        #
        root = none
        if sceneryPr.isScnSceneryLink(sceneryStage):
            root = sceneryPr.scnAssemblyGroupName(sceneryName)
        elif sceneryPr.isScnLayoutLink(sceneryStage):
            root = sceneryPr.scnAssemblyGroupName(sceneryName)
        elif sceneryPr.isScnLightLink(sceneryStage):
            root = sceneryPr.scnLightGroupName(sceneryName)
        #
        treeBox = self.treeBox
        #
        self.setScnHierarchyViewBox()
        #
        self.expandedDic = treeBox.getGraphExpandDic()
        treeBox.clear()
        #
        if root:
            maAstTreeViewCmds.setAstHierarchyView(treeBox, root, self.searchDic, self.expandedDic)
    @staticmethod
    def assembleToolPanelShow():
        from LxMaya.interface.ifWidgets import ifMaToolWindow
        w = ifMaToolWindow.IfAssemblyManagerWindow()
        w.windowShow()
    #
    def getSceneryInfo(self):
        sceneryInfoLis = datScenery.getSceneryInfo(printEnable=True)
        if sceneryInfoLis:
            self.setPlaceholderEnable(False)
            #
            sceneryInfo = sceneryInfoLis[0]
            sceneryIndex, sceneryClass, sceneryName, sceneryVariant, sceneryStage = sceneryInfo
            self.sceneryIndex = sceneryIndex
            self.sceneryClass = sceneryClass
            self.sceneryName = sceneryName
            self.sceneryVariant = sceneryVariant
            self.sceneryStage = sceneryStage
            #
            self.setSceneryInfo(sceneryIndex, sceneryClass, sceneryName, sceneryVariant)
            #
            self.leftBottomToolBar.show()
            #
            self.setScnRightToolBoxShow()
            self.setupLeftWidget(self.leftToolScrollBox, self.leftBottomToolBar)
            self.setScnHierarchyView()
            #
            self.scnAssemblyInfoToolToggleButton.setChecked(True)
            self.scnHierarchyToggleButton.setChecked(True)
        else:
            self.setPlaceholderEnable(True)
            #
            self.setScnCreateBoxShow()
    #
    def setSceneryInfo(self, sceneryIndex, sceneryClass, sceneryName, sceneryVariant):
        message = sceneryPr.getSceneryViewInfo(sceneryIndex, sceneryClass, sceneryVariant)
        self._infoLabel.setDatum(message)
        #
        self.sceneryClass = sceneryClass
        self.sceneryName = sceneryName
        self.sceneryVariant = sceneryVariant
    #
    def getSelAsb(self):
        selLis = []
        if self.treeBox.selectedItems():
            [selLis.append(str(i.text(0))) for i in self.treeBox.selectedItems() if not appVariant.basicGroupLabel in str(i.text(0)) and cmds.objExists(str(i.text(0)))]
        return selLis
    #
    def setupPanel(self):
        widget = uiCore.QWidget_()
        self.addWidget(widget)
        mainLayout = uiCore.QHBoxLayout_(widget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        #
        self.createWidget = uiCore.QWidget_()
        self.createWidget.hide()
        mainLayout.addWidget(self.createWidget)
        #
        createLayout = uiCore.QHBoxLayout_(self.createWidget)
        createLayout.setContentsMargins(0, 0, 0, 0)
        createLayout.setSpacing(0)
        #
        self.leftCreateWidget = uiCore.QWidget_()
        createLayout.addWidget(self.leftCreateWidget)
        self.leftCreateWidget.setMinimumWidth(self.widthSet)
        self.leftCreateWidget.setMaximumWidth(self.widthSet)
        #
        leftCreateLayout = uiCore.QVBoxLayout_(self.leftCreateWidget)
        leftCreateLayout.setContentsMargins(0, 0, 0, 0)
        leftCreateLayout.setSpacing(0)
        #
        self.rightCreateWidget = uiCore.QWidget_()
        self.rightCreateWidget.hide()
        createLayout.addWidget(self.rightCreateWidget)
        #
        self.toolWidget = uiCore.QWidget_()
        self.toolWidget.hide()
        mainLayout.addWidget(self.toolWidget)
        #
        toolLayout = uiCore.QGridLayout_(self.toolWidget)
        toolLayout.setContentsMargins(4, 4, 4, 4)
        toolLayout.setSpacing(2)
        #
        self.topToolBar = uiWidgets_.xToolBar()
        toolLayout.addWidget(self.topToolBar, 0, 0, 1, 2)
        #
        self.expandBox = uiWidgets_.UiExpandWidget()
        toolLayout.addWidget(self.expandBox, 1, 0, 1, 1)
        self.expandBox.setUiWidth(self.widthSet)
        #
        self.leftToolWidget = uiCore.QWidget_()
        self.expandBox.addWidget(self.leftToolWidget)
        #
        leftToolLayout = uiCore.QVBoxLayout_(self.leftToolWidget)
        leftToolLayout.setContentsMargins(0, 0, 0, 0)
        leftToolLayout.setSpacing(0)
        #
        self.leftToolScrollBox = uiCore.QScrollArea_()
        leftToolLayout.addWidget(self.leftToolScrollBox)
        #
        self.leftBottomToolBar = uiWidgets_.xToolBar()
        leftToolLayout.addWidget(self.leftBottomToolBar)
        #
        self.rightToolWidget = uiCore.QWidget_()
        toolLayout.addWidget(self.rightToolWidget, 1, 1, 1, 1)
        self.rightToolWidget.setMinimumWidth(self.widthSet)
        #
        rightToolLayout = uiCore.QVBoxLayout_(self.rightToolWidget)
        rightToolLayout.setContentsMargins(0, 0, 0, 0)
        rightToolLayout.setSpacing(0)
        #
        self.rightToolScrollBox = uiCore.QScrollArea_()
        rightToolLayout.addWidget(self.rightToolScrollBox)
        #
        self.rightToolGroupBox = uiWidgets.UiToolGroupBox()
        self.rightToolGroupBox.setExpanded(True)
        self.rightToolScrollBox.addWidget(self.rightToolGroupBox)
        #
        self.treeBox = uiWidgets_.QTreeWidget_()
        self.rightToolGroupBox.addWidget(self.treeBox)
        self.treeBox.itemSelectionChanged.connect(self.setSel)
        #
        self.rightBottomToolBar = uiWidgets_.xToolBar()
        rightToolLayout.addWidget(self.rightBottomToolBar)
        #
        self.setScnTopToolBar(self.topToolBar)


@uiCore.uiSetupShowMethod
def tableShow():
    w = IfSceneryProductToolWindow()
    w.uiShow()


#
def helpShow():
    helpDirectory = pipePr.mayaHelpDirectory('scenery')
    lxBasic.setOsFolderOpen(helpDirectory)