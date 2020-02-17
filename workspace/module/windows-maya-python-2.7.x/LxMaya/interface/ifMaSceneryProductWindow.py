# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds

from LxBasic import bscObjects

from LxScheme import shmOutput
#
from LxPreset import prsVariants, prsMethods
#
from LxCore.preset.prod import sceneryPr
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore
#
from LxMaya.interface.ifWidgets import ifMaSceneryToolUnit
#
from LxMaya.product.data import datScenery
#
from LxMaya.interface.ifCommands import maAstTreeViewCmds
#
currentProjectName = prsMethods.Project.mayaActiveName()
#
none = ''
#
_header = 'window#productionWin'
_title = 'Scenery Production'
_version = shmOutput.Resource().version


#
class IfSceneryProductToolWindow(qtWidgets.QtToolWindow):
    widthSet = 400
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfSceneryProductToolWindow, self).__init__(parent)

        self.setDefaultSize(self.widthSet, 875)
        #
        self.setNameText(_title)
        self.setIndexText(_version)
        # Scenery Information
        self.projectName = prsMethods.Project.mayaActiveName()
        self.sceneryIndex = None
        self.sceneryCategory = None
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
        self._filterButton = qtWidgets.QtIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._infoLabel = qtWidgets.QtEnterlabel()
        layout.addWidget(self._infoLabel)
        self._infoLabel.setNameTextWidth(0)
        #
        self.filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        layout.addWidget(self.filterEnterLabel)
        self.treeBox.setFilterConnect(self.filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
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
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for i in uiDatumLis:
            progressBar.update()
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
            toggleButtonCreateCmd = 'self.{0}ToggleButton = qtWidgets_.QRadioButton_();toggleButton = self.{0}ToggleButton'.format(key)
            exec toggleButtonCreateCmd
            toggleButton.setIconExplain(iconKeyword, 32, 32)
            #
            if connectMethodLis:
                for j in connectMethodLis:
                    toggleButton.clicked.connect(j)
            toggleButton.setTooltip(tooltip)
            # Tool Group
            toolGroupBox = None
            toolGroupBoxCreateCmd = 'self.{0}GroupBox = qtWidgets.QtToolboxGroup();toolGroupBox = self.{0}GroupBox'.format(key)
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
        self.scnHierarchyToggleButton = qtCore.QRadioButton_()
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
        self.rightToolboxGroup.setTitle('Scenery Hierarchy')
    #
    def setScnHierarchyView(self):
        self.searchDic = {}
        #
        sceneryName = self.sceneryName
        sceneryVariant = self.sceneryVariant
        sceneryStage = self.sceneryStage
        #
        root = none
        if sceneryPr.isSceneryLinkName(sceneryStage):
            root = sceneryPr.scnAssemblyGroupName(sceneryName)
        elif sceneryPr.isLayoutLinkName(sceneryStage):
            root = sceneryPr.scnAssemblyGroupName(sceneryName)
        elif sceneryPr.isLightLinkName(sceneryStage):
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
            sceneryIndex, sceneryCategory, sceneryName, sceneryVariant, sceneryStage = sceneryInfo
            self.sceneryIndex = sceneryIndex
            self.sceneryCategory = sceneryCategory
            self.sceneryName = sceneryName
            self.sceneryVariant = sceneryVariant
            self.sceneryStage = sceneryStage
            #
            self.setSceneryInfo(sceneryIndex, sceneryCategory, sceneryName, sceneryVariant)
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
    def setSceneryInfo(self, sceneryIndex, sceneryCategory, sceneryName, sceneryVariant):
        message = sceneryPr.getSceneryViewInfo(sceneryIndex, sceneryCategory, sceneryVariant)
        self._infoLabel.setDatum(message)
        #
        self.sceneryCategory = sceneryCategory
        self.sceneryName = sceneryName
        self.sceneryVariant = sceneryVariant
    #
    def getSelAsb(self):
        selLis = []
        if self.treeBox.selectedItems():
            [selLis.append(str(i.text(0))) for i in self.treeBox.selectedItems() if not prsVariants.Util.basicGroupLabel in str(i.text(0)) and cmds.objExists(str(i.text(0)))]
        return selLis
    #
    def setupPanel(self):
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
        #
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
        self.rightToolboxGroup.setExpanded(True)
        self.rightToolScrollBox.addWidget(self.rightToolboxGroup)
        #
        self.treeBox = qtWidgets_.QTreeWidget_()
        self.rightToolboxGroup.addWidget(self.treeBox)
        self.treeBox.itemSelectionChanged.connect(self.setSel)
        #
        self.rightBottomToolBar = qtWidgets_.xToolBar()
        rightToolLayout.addWidget(self.rightBottomToolBar)
        #
        self.setScnTopToolBar(self.topToolBar)


@qtCore.uiSetupShowMethod
def tableShow():
    w = IfSceneryProductToolWindow()
    w.uiShow()


#
def helpShow():
    pass