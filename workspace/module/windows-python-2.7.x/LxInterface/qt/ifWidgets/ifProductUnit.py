# coding:utf-8
from LxBasic import bscMethods, bscObjects, bscCommands

from LxCore import lxConfigure, lxScheme
#
from LxCore.config import assetCfg, sceneryCfg, sceneCfg
#
from LxUi import uiCore
#
from LxInterface.qt.ifBasic import _qtIfAbcWidget
#
from LxInterface.qt.ifWidgets import ifUnit, ifProductToolWindow
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import assetPr, sceneryPr, scenePr
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore
#
from LxDatabase import dbGet
#
serverBasicPath = lxScheme.Root().basic.server
#
none = ''


#
def setAssetToolBar(layout):
    if bscCommands.isMayaApp():
        toolBar = qtWidgets_.xToolBar()
        layout.addWidget(toolBar)
        buildData = [
            ('window#productionTool', u'提示：点击显示资产生产面板',
             'import LxMaya.interface.ifMaAssetProductWindow as uiPanel;uiPanel.tableShow()'),
            ('window#toolKit', u'提示：点击显示通用工具面板',
             'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.QtIf_ToolkitWindow();w.windowShow()')
        ]
        for i in buildData:
            iconKeyword, uiTip, command = i
            toolButton = qtWidgets.QtIconbutton()
            toolBar.addWidget(toolButton)
            toolButton.setIcon(iconKeyword, 32, 32, 32, 32)
            toolButton.setTooltip(uiTip)
            toolButton.setPressCommand(command)


#
def setSceneryToolBar(layout):
    if bscCommands.isMayaApp():
        toolBar = qtWidgets_.xToolBar()
        layout.addWidget(toolBar)
        buildData = [
            ('window#productionTool', u'提示：点击显示场景生产面板',
             'import LxMaya.interface.ifMaSceneryProductWindow as uiPanel;uiPanel.tableShow()'),
            ('window#toolKit', u'提示：点击显示通用工具面板',
             'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.QtIf_ToolkitWindow();w.windowShow()')
        ]
        for i in buildData:
            iconKeyword, uiTip, command = i
            toolButton = qtWidgets.QtIconbutton()
            toolBar.addWidget(toolButton)
            toolButton.setIcon(iconKeyword, 32, 32, 32, 32)
            toolButton.setTooltip(uiTip)
            toolButton.setPressCommand(command)


#
def setSceneToolBar(layout):
    if bscCommands.isMayaApp():
        toolBar = qtWidgets_.xToolBar()
        layout.addWidget(toolBar)
        buildData = [
            ('window#productionTool', u'提示：点击显示场景生产面板',
             'import LxMaya.interface.ifMaSceneProductWindow as uiPanel;uiPanel.tableShow()'),
            ('window#toolKit', u'提示：点击显示通用工具面板',
             'from LxInterface.qt.ifWidgets import ifProductWindow;w=ifProductWindow.QtIf_ToolkitWindow();w.windowShow()')
        ]
        for i in buildData:
            iconKeyword, uiTip, command = i
            toolButton = qtWidgets.QtIconbutton()
            toolBar.addWidget(toolButton)
            toolButton.setIcon(iconKeyword, 32, 32, 32, 32)
            toolButton.setTooltip(uiTip)
            toolButton.setPressCommand(command)


# Asset
class IfAssetOverviewUnit(_qtIfAbcWidget.IfProductUnitOverviewUnitBasic):
    LinkLis = assetCfg.basicAssetLinks()
    MessageWidth = 240
    MessageHeight = 240
    LeftWidth = 320
    index = 0
    def __init__(self):
        super(IfAssetOverviewUnit, self).__init__()
        self._initOverviewUnitBasic()
    #
    def setConnectObject(self, classObject):
        self._connectObject = classObject
    #
    def refreshMethod(self):
        if self._connectObject:
            self.setCentralRefresh()
    #
    def setupLeftWidget(self, layout):
        productModule = self.Cfg_Product.LynxiProduct_Module_Asset
        self._setupLinkFilter(productModule, layout)
        self._setupClassFilter(productModule, layout)
        self._setupStageFilter(productModule, layout)
        #
        setAssetToolBar(layout)
    #
    def setupCentralWidget(self, layout):
        def centralCurrentChangedMethod():
            currentItem = self._centralUpGridview.currentItem()
            if currentItem:
                self._curUnitIndex = currentItem.assetIndex
                self._curProjectName = currentItem.projectName
                self._curUnitClass = currentItem.assetClass
                self._curUnitName = currentItem.assetName
                self._curUnitVariant = currentItem.assetVariant
                #
                self._centralUpToolboxGroup.setTitle('Asset>{}>{}'.format(self._curUnitName, self._curUnitVariant))
                #
                self.setRecordRefresh()
        #
        self._centralUpToolboxGroup = qtWidgets.QtToolboxGroup()
        self._centralUpToolboxGroup.setTitle('Asset(s)')
        self._centralUpToolboxGroup.setExpanded(True)
        layout.addWidget(self._centralUpToolboxGroup)
        #
        self._centralUpGridview = qtWidgets.QtGridview()
        self._centralUpToolboxGroup.addWidget(self._centralUpGridview)
        self._centralUpGridview.setCheckEnable(True)
        #
        width, height = self.MessageWidth, self.MessageWidth
        self._uiItemWidth, self._uiItemHeight = width, height
        self._centralUpGridview.setItemSize(width, height + 20 + 20*len(self.LinkLis))
        self._centralUpGridview.setItemListModeSize(width, 20)
        self._centralUpGridview.setItemIconModeSize(width, height + 20)
        #
        self._centralUpGridview.setFilterConnect(self._filterEnterLabel)
        #
        self._centralUpGridview.currentChanged.connect(centralCurrentChangedMethod)
        #
        if self._filterItemDic:
            [i.setFilterViewWidget(self._centralUpGridview) for i in self._filterItemDic.values()]
    #
    def setupRightWidget(self, layout):
        def setLinkButtonBranch(button, link):
            def setCurrentStage():
                self._curUnitStage = link
            button.clicked.connect(setCurrentStage)
            button.clicked.connect(self.setRecordRefresh)
        #
        self.assetRightToolboxGroup = qtWidgets.QtToolboxGroup()
        self.assetRightToolboxGroup.setTitle('Asset Record>{}'.format(self.LinkLis[0]))
        self.assetRightToolboxGroup.setExpanded(True)
        layout.addWidget(self.assetRightToolboxGroup)
        #
        linkToolBar = qtWidgets_.xToolBar()
        self.assetRightToolboxGroup.addWidget(linkToolBar)
        for seq, i in enumerate(self.LinkLis):
            linkButton = qtWidgets.QtEnablebutton('link#{}'.format(i))
            linkToolBar.addWidget(linkButton)
            linkButton.setAutoExclusive(True)
            if seq == 0:
                linkButton.setChecked(True)
            #
            setLinkButtonBranch(linkButton, i)
        #
        self.recordBox = ifUnit.IfProductUnitRecordUnit()
        self.assetRightToolboxGroup.addWidget(self.recordBox)
    #
    def setCentralRefresh(self):
        def setBranch(seq, key, value, gridItem, messageWidget):
            def getBuildData(data):
                for linkClass, linkActionDataLis in data:
                    branchActionData.append((linkClass,))
                    for linkActionData in linkActionDataLis:
                        unitLink, explain, enable, update, loadMethod, createMethod = linkActionData
                        #
                        exists = [False, True][update != appVariant.infoNonExistsLabel]
                        state = ['wait', dbGet.getDbAssetMeshCheck(assetIndex, assetVariant, unitLink)][update != appVariant.infoNonExistsLabel]
                        # Statistics
                        self._statisticsDic.setdefault(unitLink, []).append(
                            (assetIndex, assetVariant, enable, exists)
                        )
                        # Message
                        if enable:
                            rgba = [(255, 255, 64, 255), (63, 255, 127, 255)][exists]
                            messageLis.append((5, (rgba, ('link#{}'.format(unitLink), state), update)))
                        else:
                            rgba = 95, 95, 95, 255
                            messageLis.append((5, (rgba, None, 'Non - Need')))
                        # Action
                        if enable is True:
                            # Link Filter
                            self._filterIndexDic.setdefault(unitLink, []).append(seq)
                            if exists:
                                if loadMethod is not None:
                                    branchActionData.append(
                                        ('Load {}'.format(explain), ('basic#{}Link'.format(unitLink), 'svg_basic@svg#load_action'), exists, loadMethod)
                                    )
                                    if assetPr.isAstRigLink(unitLink):
                                        branchActionData.append(
                                            ('Load for Animation', ('basic#AnimationLink', 'svg_basic@svg#reference_action'), True, astLoadRigForAnimationCmd)
                                        )
                                    if assetPr.isAstSolverLink(unitLink):
                                        branchActionData.append(
                                            ('Load for Animation', ('basic#AnimationLink', 'svg_basic@svg#reference_action'), True, loadSolverForAnimation)
                                        )
                            else:
                                if createMethod is not None:
                                    branchActionData.append(
                                        ('Create {}'.format(explain), ('basic#{}Link'.format(unitLink), 'svg_basic@svg#create_action'), True, createMethod)
                                    )
                                else:
                                    branchActionData.append(
                                        ('Non - Exists', 'basic#', False)
                                    )
                        else:
                            branchActionData.append(('Non - Need', 'basic#', False))
                #
                branchActionData.extend(
                    [
                        ('Folder', ),
                        (
                            'Open Folder', 'svg_basic@svg#folder',
                            [
                                ('Asset Folder', 'svg_basic@svg#folder', True, openAssetFolder),
                                ('Assembly Folder', 'svg_basic@svg#folder', True, openAssemblyFolder)
                            ]
                        ),
                        ('Other', ),
                        ('Refresh', 'svg_basic@svg#refresh', False),
                        ('Help', 'svg_basic@svg#help', True)
                    ]
                )
            # Model
            def astModelLoadCmd():
                from LxMaya.product import maAstLoadCmds
                #
                isLockTransform = True
                #
                isCollectionTexture = self._localizationTexture
                isForce = self._isForce
                #
                assetStage = dbGet.getDbModelStage(assetIndex, assetVariant)
                #
                maAstLoadCmds.astUnitModelLoadMainCmd(
                    projectName,
                    assetIndex,
                    assetClass, assetName, assetVariant, assetStage,
                    force=isForce,
                    lockTransform=isLockTransform, collectionTexture=isCollectionTexture
                )
            #
            def astModelCreateCmd():
                from LxMaya.product import maAstLoadCmds
                #
                maAstLoadCmds.astUnitModelCreateMainCmd(
                    projectName,
                    assetIndex,
                    assetClass, assetName, assetVariant, lxConfigure.LynxiAstModelStages[0]
                )
            #
            def loadForRig():
                from LxMaya.product import maAstLoadCmds
                #
                isForce = self._isForce
                #
                assetStage = dbGet.getDbRigStage(assetIndex, assetVariant)
                #
                maAstLoadCmds.astUnitRigLoadMainCmd(
                    assetIndex, projectName, assetClass, assetName, assetVariant, assetStage,
                    force=isForce
                )
            #
            def createForRig():
                from LxMaya.product import maAstLoadCmds
                #
                maAstLoadCmds.astUnitRigCreateMainCmd(
                    projectName,
                    assetIndex,
                    assetClass, assetName, assetVariant, lxConfigure.LynxiAstRigStages[0]
                )
            #
            def loadForCfx():
                from LxMaya.product import maAstLoadCmds
                #
                isCollectionTexture = self._localizationTexture
                isCollectionMap = self._localizationTexture
                isUseServerTexture = False
                isUseServerMap = False
                #
                assetStage = dbGet.getDbCfxStage(assetIndex, assetVariant)
                #
                maAstLoadCmds.astUnitCfxLoadMainCmd(
                    projectName,
                    assetIndex,
                    assetClass, assetName, assetVariant, assetStage,
                    collectionTexture=isCollectionTexture, useServerTexture=isUseServerTexture,
                    collectionMap=isCollectionMap, useServerMap=isUseServerMap
                )
            #
            def createForCfx():
                from LxMaya.product import maAstLoadCmds
                #
                maAstLoadCmds.astUnitCreateCfxMain(
                    assetIndex,
                    projectName,
                    assetClass, assetName, assetVariant, lxConfigure.LynxiAstCfxStages[0]
                )
            # Solver
            def loadForSolver():
                from LxMaya.product import maAstLoadCmds
                #
                isForce = self._isForce
                isCollectionTexture = self._localizationTexture
                #
                assetStage = lxConfigure.LynxiAstRigSolStages[0]
                #
                maAstLoadCmds.astUnitLoadMainCmd(
                    assetIndex,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage,
                    collectionTexture=isCollectionTexture,
                    force=isForce
                )
            #
            def createForSolver():
                from LxMaya.product import maAstLoadCmds
                #
                isForce = self._isForce
                #
                assetStage = lxConfigure.LynxiAstRigSolStages[0]
                #
                maAstLoadCmds.astUnitSolverCreateMainCmd(
                    assetIndex, projectName, assetClass, assetName, assetVariant, assetStage,
                    force=isForce
                )
            #
            def loadForLight():
                from LxMaya.product import maAstLoadCmds
                #
                isForce = self._isForce
                isCollectionTexture = self._localizationTexture
                #
                assetStage = lxConfigure.LynxiScLightStages[1]
                #
                maAstLoadCmds.astUnitLoadMainCmd(
                    assetIndex,
                    projectName,
                    assetClass, assetName, assetVariant, assetStage,
                    collectionTexture=isCollectionTexture,
                    force=isForce
                )
            #
            def createForLight():
                from LxMaya.product import maAstLoadCmds
                #
                isForce = self._isForce
                #
                maAstLoadCmds.astUnitLightCreateMainCmd(
                    assetIndex, projectName, assetClass, assetName, assetVariant, lxConfigure.LynxiScLightStages[1],
                    force=isForce
                )
            #
            def astLoadRigForAnimationCmd():
                from LxMaya.product import maAstLoadCmds
                #
                maAstLoadCmds.astUnitRigLoadForAnimationCmd(
                    projectName,
                    assetIndex,
                    assetClass, assetName, assetVariant
                )
            #
            def loadSolverForAnimation():
                from LxMaya.product import maAstLoadCmds
                #
                maAstLoadCmds.astAssetSolverLoadForAnimation(
                    assetIndex, projectName, assetClass, assetName, assetVariant
                )
            #
            def loadForAssembly():
                from LxMaya.product import maAstLoadCmds
                # noinspection PyArgumentEqualDefault
                maAstLoadCmds.astUnitAssemblyLoadForScenery(
                    assetIndex,
                    projectName,
                    assetClass, assetName, assetVariant,
                    isWithAnnotation=False, isWithHandle=True
                )
            #
            def openAssetFolder():
                osPath = assetPr.basicUnitFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName, assetClass, assetName
                )
                bscMethods.OsDirectory.open(osPath)
            #
            def openAssemblyFolder():
                osPath = assetPr.astUnitAssemblyFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName, assetClass, assetName
                )
                bscMethods.OsDirectory.open(osPath)
            #
            assetIndex, assetVariant = key
            #
            (
                viewName,
                assetClass, assetName, assetPriority,
                astModelEnable, astRigEnable, astCfxEnable, astSolverEnable, astLightEnable, astAssemblyEnable
            ) = value
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
            modelUpdate = dbGet.getDbModelUpdate(assetIndex, assetVariant)
            #
            rigUpdate = dbGet.getDbRigUpdate(assetIndex)
            #
            cfxUpdate = dbGet.getDbCfxUpdate(assetIndex, assetVariant)
            #
            solverUpdate = assetPr.getAssetUnitProductUpdate(
                projectName,
                assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Solver
            )
            #
            lightUpdate = assetPr.getAssetUnitProductUpdate(
                projectName,
                assetClass, assetName, assetVariant, lxConfigure.LynxiProduct_Asset_Link_Light
            )
            #
            assemblyUpdate = dbGet.getAstUnitDbAssemblyUpdate(projectName, assetClass, assetName, assetVariant)
            #
            viewportPreview = dbGet.dbAstViewportPreviewFile(assetIndex)
            renderPreview = dbGet.dbAstRenderPreviewFile(assetIndex, assetVariant)
            #
            messageLis = [
                (4, [(viewportPreview, ('Model', 'Viewport ( {} - {} )'.format(assetName, assetVariant))), (renderPreview, ('Model', 'Render ( {} - {} )'.format(assetName, assetVariant)))])
            ]
            branchActionData = []
            #
            getBuildData(
                [
                    (
                        'Model',
                        [
                            (lxConfigure.LynxiProduct_Asset_Link_Model, 'for Model', astModelEnable, modelUpdate, astModelLoadCmd, astModelCreateCmd)
                        ]
                    ),
                    (
                        'Rig',
                        [
                            (lxConfigure.LynxiProduct_Asset_Link_Rig, 'for Rig', astRigEnable, rigUpdate, loadForRig, createForRig)
                        ]
                    ),
                    (
                        'FX',
                        [
                            (lxConfigure.LynxiProduct_Asset_Link_Cfx, 'for Groom', astCfxEnable, cfxUpdate, loadForCfx, createForCfx),
                            (lxConfigure.LynxiProduct_Asset_Link_Solver, 'for Solver Rig', astSolverEnable, solverUpdate, loadForSolver, createForSolver)
                        ]
                    ),
                    (
                        'Light',
                        [
                            (lxConfigure.LynxiProduct_Asset_Link_Light, 'for Light', astLightEnable, lightUpdate, loadForLight, createForLight)
                        ]
                    ),
                    (
                        'Scenery',
                        [
                            (lxConfigure.LynxiProduct_Asset_Link_Assembly, 'for Scenery', astAssemblyEnable, assemblyUpdate, loadForAssembly, None)
                        ]
                    )
                ]
            )
            #
            viewExplain = assetPr.getAssetViewInfo(assetIndex, assetClass, '{} - {}'.format(assetName, assetVariant))
            gridItem.setNameText(viewExplain)
            gridItem.setIcon('svg_basic@svg#package_object')
            #
            gridItem.assetIndex = assetIndex
            gridItem.projectName = projectName
            gridItem.assetClass = assetClass
            gridItem.assetName = assetName
            gridItem.assetVariant = assetVariant
            # Message
            messageWidget.setExplainWidth(20)
            imageIndex = [0, 1][renderPreview is not none]
            messageWidget.setImageIndex(imageIndex)
            messageWidget.setDatumLis(messageLis, self._uiItemWidth, self._uiItemHeight)
            # Action
            gridItem.setActionData(
                branchActionData, viewExplain
            )
            # Filter
            classFilterKey = (assetClass, assetPriority)
            self._filterIndexDic.setdefault(classFilterKey, []).append(seq)
        #
        def setFilterRefresh(maxCount):
            for k, v in self._filterItemDic.items():
                filterButton = v
                if k in self._filterIndexDic:
                    filterIndexLis = self._filterIndexDic[k]
                    #
                    filterButton.setViewFilterItemIndexes(filterIndexLis)
                    filterButton.setMaxFilterCount(maxCount)
                else:
                    filterButton.setViewFilterItemIndexes([])
                #
                filterButton.setRefresh()
        #
        def setMain():
            setData = assetPr.getUiAssetSetDataDic(projectName)
            gridView.cleanItems()
            if setData:
                maxCount = len(setData)
                if self.connectObject():
                    self.connectObject().mainWindow().setMaxProgressValue(maxCount)
                #
                for seq, (k, v) in enumerate(setData.items()):
                    if self.connectObject():
                        self.connectObject().mainWindow().updateProgress()
                    #
                    gridItem = qtWidgets.QtGridviewItem()
                    messageWidget = qtWidgets.QtMessageWidget()
                    #
                    gridView.addItem(gridItem)
                    gridItem.addWidget(messageWidget, 0, 0, 1, 1)
                    #
                    setBranch(seq, k, v, gridItem, messageWidget)
                #
                setFilterRefresh(maxCount)
                #
                gridView.setRefresh()
                gridView.setSortByName()
                #
                self._maxIndexCount = maxCount
            else:
                setFilterRefresh(0)
                gridView.setRefresh()
        #
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        #
        self._filterIndexDic.clear()
        self._statisticsDic.clear()
        #
        projectName = self._connectObject.getProjectName()
        #
        gridView = self._centralUpGridview
        #
        setMain()
        self._initTagFilterAction(gridView)
    #
    def setRecordRefresh(self):
        assetIndex = self._curUnitIndex
        #
        projectName = self._curProjectName
        #
        assetClass = self._curUnitClass
        assetName = self._curUnitName
        assetVariant = self._curUnitVariant
        assetStage = self._curUnitStage
        #
        backupSourceFile = assetPr.astUnitSourceFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        backupProductFile = assetPr.astUnitProductFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName, assetClass, assetName, assetVariant, assetStage
        )[1]
        #
        if self._rightRefreshEnable is True:
            self.recordBox.setRecordConnect(backupSourceFile, backupProductFile)
            if assetStage:
                self.assetRightToolboxGroup.setTitle('Asset Record>{}'.format(assetStage))
    #
    def setupUnitAction(self):
        def isForce():
            return self._isForce
        #
        def setForceSwitch():
            self._isForce = not self._isForce
        #
        def isLocalTexture():
            return self._localizationTexture
        #
        def setLocalTextureSwitch():
            self._localizationTexture = not self._localizationTexture
        #
        if self.connectObject():
            tabIndex = self.connectObject().tabIndex(self)
            tab = self.connectObject().tabAt(tabIndex)
            tab.setActionData(
                [
                    ('Basic',),
                    ('Refresh', 'svg_basic@svg#refresh', True, self.setCentralRefresh),
                    ('Config',),
                    ('New Scene', 'checkBox', isForce, setForceSwitch),
                    ('Localization Texture', 'checkBox', isLocalTexture, setLocalTextureSwitch),
                    ('About',),
                    ('Help', 'svg_basic@svg#help', True)
                ]
            )
    #
    def initToolBox(self):
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        #
        self._uiItemWidth = 200
        self._uiItemHeight = 200
        #
        self._statisticsUiDic = {}
        self._statisticsDic = {}
        #
        self._isForce = True
        self._localizationTexture = True
        #
        self._curProjectName = None
        #
        self._curUnitIndex = None
        self._curUnitClass = None
        self._curUnitName = None
        self._curUnitVariant = None
        self._curUnitStage = None
        #
        self._rightRefreshEnable = False
        #
        self._listItemWidgetDic = {}
        #
        self._maxIndexCount = 0
    #
    def setupUnitWidgets(self):
        self.setupLeftWidget(self._leftScrollLayout)
        self.setupCentralWidget(self._centralScrollLayout)
        self.setupRightWidget(self._rightScrollLayout)


# Scenery
class IfSceneryOverviewUnit(_qtIfAbcWidget.IfProductUnitOverviewUnitBasic):
    LinkLis = sceneryCfg.basicSceneryLinks()
    MessageWidth = 280
    MessageHeight = 160
    LeftWidth = 320
    index = 0
    def __init__(self):
        super(IfSceneryOverviewUnit, self).__init__()
        self._initOverviewUnitBasic()
    #
    def setupLeftWidget(self, layout):
        productModule = self.Cfg_Product.LynxiProduct_Module_Scenery
        self._setupLinkFilter(productModule, layout)
        self._setupClassFilter(productModule, layout)
        self._setupStageFilter(productModule, layout)
        setSceneryToolBar(layout)
    #
    def setupCentralWidget(self, layout):
        def centralCurrentChangedMethod():
            currentItem = self._centralUpGridview.currentItem()
            if currentItem:
                self._curUnitIndex = currentItem.sceneryIndex
                self._curProjectName = currentItem.projectName
                self._curUnitClass = currentItem.sceneryClass
                self._curUnitName = currentItem.sceneryName
                self._curUnitVariant = currentItem.sceneryVariant
                #
                self._centralUpToolboxGroup.setTitle('Scenery>{}>{}'.format(self._curUnitName, self._curUnitVariant))
                #
                self.setRecordRefresh()
        #
        self._centralUpToolboxGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(self._centralUpToolboxGroup)
        self._centralUpToolboxGroup.setTitle('Scenery(s)')
        self._centralUpToolboxGroup.setExpanded(True)
        #
        self._centralUpGridview = qtWidgets.QtGridview()
        self._centralUpToolboxGroup.addWidget(self._centralUpGridview)
        self._centralUpGridview.setCheckEnable(True)
        #
        renderWidth, renderHeight = appVariant.rndrImageWidth, appVariant.rndrImageHeight
        width = self.MessageWidth
        height = int(width * (float(renderHeight) / float(renderWidth)))
        self._uiItemWidth = width
        self._uiItemHeight = height
        self._centralUpGridview.setItemSize(width, height + 20 + 20*len(self.LinkLis))
        self._centralUpGridview.setItemListModeSize(width, 20)
        self._centralUpGridview.setItemIconModeSize(width, height + 20)
        #
        self._centralUpGridview.setFilterConnect(self._filterEnterLabel)
        #
        self._centralUpGridview.currentChanged.connect(centralCurrentChangedMethod)
        #
        if self._filterItemDic:
            [i.setFilterViewWidget(self._centralUpGridview) for i in self._filterItemDic.values()]
        #
        self._centralDownToolboxGroup = qtWidgets.QtToolboxGroup()
        layout.addWidget(self._centralDownToolboxGroup)
        self._centralDownToolboxGroup.setTitle('Compose(s)')
        #
        self._centralDownTreeView = qtWidgets.QtTreeview()
        self._centralDownToolboxGroup.addWidget(self._centralDownTreeView)
    #
    def setupRightWidget(self, layout):
        def setLinkButtonBranch(button, link):
            def setCurrentStage():
                self._curUnitStage = link
            #
            button.clicked.connect(setCurrentStage)
            button.clicked.connect(self.setRecordRefresh)
        #
        self.assetRightToolboxGroup = qtWidgets.QtToolboxGroup()
        self.assetRightToolboxGroup.setTitle('Asset Record>{}'.format(self.LinkLis[0]))
        self.assetRightToolboxGroup.setExpanded(True)
        layout.addWidget(self.assetRightToolboxGroup)
        #
        linkToolBar = qtWidgets_.xToolBar()
        self.assetRightToolboxGroup.addWidget(linkToolBar)
        for seq, i in enumerate(self.LinkLis):
            linkButton = qtWidgets.QtEnablebutton('link#{}'.format(i))
            linkToolBar.addWidget(linkButton)
            linkButton.setAutoExclusive(True)
            if seq == 0:
                linkButton.setChecked(True)
            #
            setLinkButtonBranch(linkButton, i)
        #
        self.recordBox = ifUnit.IfProductUnitRecordUnit()
        self.assetRightToolboxGroup.addWidget(self.recordBox)
    #
    def setCentralRefresh(self):
        def setBranch(seq, key, value):
            def getBuildData(data):
                for i in data:
                    unitLink, explain, enable, loadMethod, createMethod = i
                    actionDatumLis.append((bscMethods.StrCamelcase.toPrettify(unitLink),))
                    #
                    update = sceneryPr.getSceneryUnitProductUpdate(
                        projectName, sceneryClass, sceneryName, sceneryVariant, unitLink
                    )
                    exists = [False, True][update != appVariant.infoNonExistsLabel]
                    state = ['wait', None][update != appVariant.infoNonExistsLabel]
                    # Message
                    if enable:
                        rgba = [(255, 255, 64, 255), (63, 255, 127, 255)][exists]
                        messageLis.append((5, (rgba, ('link#{}'.format(unitLink), state), update)))
                    else:
                        rgba = 95, 95, 95, 255
                        messageLis.append((5, (rgba, None, 'Non - Need')))
                    # Action
                    if enable is True:
                        # Link Filter
                        self._filterIndexDic.setdefault(unitLink, []).append(seq)
                        if exists:
                            if loadMethod is not None:
                                actionDatumLis.append(('Load {}'.format(explain), ('link#{}'.format(unitLink), 'svg_basic@svg#load_action'), exists, loadMethod))
                        else:
                            if createMethod is not None:
                                actionDatumLis.append(('Create {}'.format(explain), ('link#{}'.format(unitLink), 'svg_basic@svg#create_action'), True, createMethod))
                            else:
                                actionDatumLis.append(('Non - Exists', 'basic#', False))
                    else:
                        actionDatumLis.append(('Non - Need', 'basic#', False))
                #
                actionDatumLis.extend(
                    [
                        ('Assembly Reference', ),
                        ('Reference for Animation', ('svg_basic@svg#assembly_object', 'svg_basic@svg#reference_action'), True, scnAssemblyLoadByReferenceForAnimationCmd),
                        ('Reference for Light', ('svg_basic@svg#assembly_object', 'svg_basic@svg#reference_action'), True, scnAssemblyLoadByReferenceForLightCmd),
                        ('Assembly Load',),
                        ('Load Assembly', ('svg_basic@svg#assembly_object', 'svg_basic@svg#load_action'), True, scnUnitAssemblyLoad),
                        ('Folder',),
                        ('Open Assembly Folder', 'svg_basic@svg#folder', True, openSceneryFolder),
                        ('Other',),
                        ('Help', 'svg_basic@svg#help', True)
                    ]
                )
            #
            def scnAssemblyCreateCmd():
                from LxMaya.product import maScnLoadCmds
                #
                maScnLoadCmds.scnUnitCreateMainCmd(
                    sceneryIndex,
                    projectName,
                    sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiScnSceneryStages[0]
                )
            #
            def scnAssemblyLoadCmd():
                from LxMaya.product import maScnLoadCmds
                #
                maScnLoadCmds.scnUnitLoadMainCmd(
                    projectName,
                    sceneryIndex,
                    sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiScnSceneryStages[0]
                )
            #
            def scnAssemblyLoadByReferenceForAnimationCmd():
                from LxMaya.product import maScnLoadCmds
                maScnLoadCmds.scnUnitAssemblyLoadByReferenceCmd(
                    projectName,
                    sceneryIndex,
                    sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiProduct_Module_Scenery, active='GPU'
                )
            #
            def scnAssemblyLoadByReferenceForLightCmd():
                from LxMaya.product import maScnLoadCmds
                maScnLoadCmds.scnUnitAssemblyLoadByReferenceCmd(
                    projectName,
                    sceneryIndex,
                    sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiProduct_Module_Scenery, active='Proxy'
                )
            #
            def scnUnitAssemblyLoad():
                from LxMaya.product import maScnLoadCmds
                maScnLoadCmds.scnUnitAssemblyLoadCmd(
                    projectName,
                    sceneryIndex,
                    sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiProduct_Scenery_Link_Scenery
                )
            #
            def openSceneryFolder():
                osPath = sceneryPr.sceneryUnitFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName, sceneryClass, sceneryName
                )
                bscMethods.OsDirectory.open(osPath)
            #
            sceneryIndex, sceneryVariant = key
            #
            viewName, sceneryClass, sceneryName, assetPriority, sceneryEnabled, scLayoutEnable, scAnimationEnable, scSimulationEnable, scLightEnable = value
            #
            gridItem = qtWidgets.QtGridviewItem()
            gridView.addItem(gridItem)
            #
            viewExplain = sceneryPr.getSceneryViewInfo(sceneryIndex, sceneryClass, '{} - {}'.format(sceneryName, sceneryVariant))
            gridItem.setName(viewExplain)
            gridItem.setIcon('svg_basic@svg#package_object')
            # gridItem.setTooltip(viewExplain)
            #
            gridItem.sceneryIndex = sceneryIndex
            gridItem.projectName = projectName
            gridItem.sceneryClass = sceneryClass
            gridItem.sceneryName = sceneryName
            gridItem.sceneryVariant = sceneryVariant
            #
            viewportPreview = sceneryPr.scnUnitPreviewFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiProduct_Scenery_Link_Scenery
            )[1]
            #
            renderPreview = sceneryPr.scnUnitPreviewFile(
                lxConfigure.LynxiRootIndex_Server,
                projectName,
                sceneryClass, sceneryName, sceneryVariant, lxConfigure.LynxiProduct_Scenery_Link_Scenery,
                appVariant.pngExt
            )[1]
            #
            messageLis = [
                (4, [(viewportPreview, ('Scenery ( {} )'.format(sceneryVariant), 'Viewport')), (renderPreview, ('Scenery ( {} )'.format(sceneryVariant), 'Render'))])
            ]
            actionDatumLis = []
            #
            getBuildData(
                [
                    ('scenery', 'for Scenery', sceneryEnabled, scnAssemblyLoadCmd, scnAssemblyCreateCmd),
                    ('layout', 'for Layout', scLayoutEnable, None, None),
                    ('animation', 'for Animation', scAnimationEnable, None, None),
                    ('simulation', 'for Simulation', scSimulationEnable, None, None),
                    ('light', 'for Light', scLightEnable, None, None),
                ]
            )
            gridItem.setActionData(
                actionDatumLis
            )
            #
            messageWidget = qtWidgets.QtMessageWidget()
            messageWidget.setExplainWidth(20)
            messageWidget.setDefaultHeight(self.MessageHeight)
            imageIndex = [0, 1][bscCommands.isOsExist(renderPreview)]
            messageWidget.setImageIndex(imageIndex)
            gridItem.addWidget(messageWidget, 0, 0, 1, 1)
            messageWidget.setDatumLis(messageLis, self._uiItemWidth, self._uiItemHeight)
            #
            classFilterKey = (sceneryClass, assetPriority)
            self._filterIndexDic.setdefault(classFilterKey, []).append(seq)
        #
        def setFilterRefresh(maxCount):
            for k, v in self._filterItemDic.items():
                filterButton = v
                if k in self._filterIndexDic:
                    filterIndexLis = self._filterIndexDic[k]
                    #
                    filterButton.setViewFilterItemIndexes(filterIndexLis)
                    filterButton.setMaxFilterCount(maxCount)
                else:
                    filterButton.setViewFilterItemIndexes([])
                #
                filterButton.setRefresh()
        #
        def setMain():
            setData = sceneryPr.getUiScenerySetDataDic(projectName)
            gridView.cleanItems()
            if setData:
                maxCount = len(setData)
                if self.connectObject():
                    self.connectObject().mainWindow().setMaxProgressValue(maxCount)
                for seq, (k, v) in enumerate(setData.items()):
                    if self.connectObject():
                        self.connectObject().mainWindow().updateProgress()
                    setBranch(seq, k, v)
                #
                setFilterRefresh(maxCount)
            #
            gridView.setRefresh()
            gridView.setSortByName()
        #
        self._filterIndexDic.clear()
        self._statisticsDic.clear()
        #
        projectName = self._connectObject.getProjectName()
        #
        gridView = self._centralUpGridview
        setMain()
    #
    def setComposeRefresh(self):
        pass
    #
    def setRecordRefresh(self):
        unitIndex = self._curUnitIndex
        #
        projectName = self._curProjectName
        #
        unitClass = self._curUnitClass
        unitName = self._curUnitName
        unitVariant = self._curUnitVariant
        unitStage = self._curUnitStage
        #
        backupSourceFile = sceneryPr.scnUnitSourceFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName, unitClass, unitName, unitVariant, unitStage
        )[1]
        #
        backupProductFile = sceneryPr.scnUnitProductFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName, unitClass, unitName, unitVariant, unitStage
        )[1]
        #
        if self._rightRefreshEnable is True:
            self.recordBox.setRecordConnect(backupSourceFile, backupProductFile)
            if unitStage:
                self.assetRightToolboxGroup.setTitle('Asset Record>{}'.format(unitStage))
    #
    def setupUnitAction(self):
        if self.connectObject():
            tabIndex = self.connectObject().tabIndex(self)
            tab = self.connectObject().tabAt(tabIndex)
            tab.setActionData(
                [
                    ('Basic', ),
                    ('Refresh', 'svg_basic@svg#refresh', True, self.setCentralRefresh),
                    ('About', ),
                    ('Help', 'svg_basic@svg#help', True)
                ]
            )
    #
    def initToolBox(self):
        self._uiItemWidth = 200
        self._uiItemHeight = 200
        #
        self._statisticsDic = bscCommands.orderedDict()
        #
        self._statisticsUiDic = {}
        #
        self._curProjectName = None
        #
        self._curUnitIndex = None
        self._curUnitClass = None
        self._curUnitName = None
        self._curUnitVariant = None
        self._curUnitStage = None
        #
        self._rightRefreshEnable = False
    #
    def setupUnitWidgets(self):
        self.setupLeftWidget(self._leftScrollLayout)
        self.setupCentralWidget(self._centralScrollLayout)
        self.setupRightWidget(self._rightScrollLayout)


# Scene
class IfSceneOverviewUnit(_qtIfAbcWidget.IfProductUnitOverviewUnitBasic):
    LinkLis = sceneCfg.basicSceneLinkLis()
    MessageWidth = 280
    MessageHeight = 160
    LeftWidth = 320
    index = 0
    def __init__(self):
        super(IfSceneOverviewUnit, self).__init__()
        self._initOverviewUnitBasic()
    #
    def setupLeftWidget(self, layout):
        productModule = self.Cfg_Product.LynxiProduct_Module_Scene
        self._setupLinkFilter(productModule, layout)
        self._setupClassFilter(productModule, layout)
        self._setupStageFilter(productModule, layout)
        setSceneToolBar(layout)
    #
    def setupCentralWidget(self, layout):
        def setDownRefreshEnable():
            self._downRefreshEnable = downToolboxGroup.isExpanded() or downToolboxGroup.isSeparated()
            #
            if self._downRefreshEnable is True:
                self.setCameraRefresh()
                self.setAssetRefresh()
        #
        def centralCurrentChangedMethod():
            currentItem = self._scGridview.currentItem()
            if currentItem:
                self._curSceneIndex = currentItem.sceneIndex
                self._curProjectName = currentItem.projectName
                self._curSceneClass = currentItem.sceneClass
                self._curSceneName = currentItem.sceneName
                self._curSceneVariant = currentItem.sceneVariant
                #
                self._scUpToolboxGroup.setTitle('Scene>{}>{}'.format(self._curSceneName, self._curSceneVariant))
                #
                self.setCameraRefresh()
                self.setAssetRefresh()
                self.setSceneryRefresh()
                #
                self.setRecordRefresh()
        #
        self._scUpToolboxGroup = qtWidgets.QtToolboxGroup()
        self._scUpToolboxGroup.setTitle('Scene(s)')
        self._scUpToolboxGroup.setExpanded(True)
        layout.addWidget(self._scUpToolboxGroup)
        self._scUpToolboxGroup.setTooltip(
            u'''镜头单元\n1，显示当前项目所有镜头信息；\n2，显示当前项目所有镜头各环节的预览视频；\n3，显示当前项目所有镜头各环节的更新时间。'''
        )
        #
        self._scGridview = qtWidgets.QtGridview()
        self._scUpToolboxGroup.addWidget(self._scGridview)
        self._scGridview.setCheckEnable(True)
        #
        renderWidth, renderHeight = appVariant.rndrImageWidth, appVariant.rndrImageHeight
        width = self.MessageWidth
        height = int(width*(float(renderHeight) / float(renderWidth)))
        self._uiItemWidth = width
        self._uiItemHeight = height
        self._scGridview.setItemSize(width, height + 20 + 20*len(self.LinkLis))
        self._scGridview.setItemListModeSize(width, 20)
        self._scGridview.setItemIconModeSize(width, height + 20)
        #
        self._scGridview.setFilterConnect(self._filterEnterLabel)
        #
        self._scGridview.currentChanged.connect(centralCurrentChangedMethod)
        #
        if self._filterItemDic:
            [i.setFilterViewWidget(self._scGridview) for i in self._filterItemDic.values()]
        #
        downToolboxGroup = qtWidgets.QtToolboxGroup()
        downToolboxGroup.setTitle('Compose(s)')
        layout.addWidget(downToolboxGroup)
        #
        tabWidget = qtWidgets.QtButtonTabgroup()
        downToolboxGroup.addWidget(tabWidget)
        tabWidget.setTabPosition(qtCore.South)
        #
        widget = qtCore.QWidget_()
        downToolboxGroup.addWidget(widget)
        downToolboxGroup.expanded.connect(setDownRefreshEnable)
        downToolboxGroup.separated.connect(setDownRefreshEnable)
        # Camera
        self._cameraListViewBox = qtWidgets.QtGridview()
        tabWidget.addTab(self._cameraListViewBox, 'Camera(s)', 'svg_basic@svg#tab')
        self._cameraListViewBox.setCheckEnable(True)
        #
        renderWidth, renderHeight = appVariant.rndrImageWidth, appVariant.rndrImageHeight
        height = self.MessageHeight
        width = int(height*(float(renderWidth) / float(renderHeight)))
        self._cameraItemWidth = width
        self._cameraItemHeight = height
        self._cameraListViewBox.setItemSize(width, height + 20 + 20)
        self._cameraListViewBox.setItemListModeSize(width, 20)
        self._cameraListViewBox.setItemIconModeSize(width, height + 20)
        # Asset
        self._scAstGridview = qtWidgets.QtGridview()
        tabWidget.addTab(self._scAstGridview, 'Asset(s)', 'svg_basic@svg#tab')
        self._scAstGridview.setCheckEnable(True)
        #
        height = 240
        width = 240
        self._assetItemWidth = width
        self._assetItemHeight = height
        self._scAstGridview.setItemSize(width + 32, height + 20*3 + 20)
        self._scAstGridview.setItemListModeSize(width + 32, 20)
        self._scAstGridview.setItemIconModeSize(width + 32, height + 20)
        # Scenery
        self._sceneryTreeView = qtWidgets.QtTreeview()
        tabWidget.addTab(self._sceneryTreeView, 'Scenery(s)', 'svg_basic@svg#tab')
        self._sceneryTreeView.setCheckEnable(True)
        #
        tabWidget.setCurrentIndex(1)
    #
    def setupRightWidget(self, layout):
        def setRemarkGroup():
            self.scRemarkToolboxGroup = qtWidgets.QtToolboxGroup()
            self.scRemarkToolboxGroup.setTitle('Remark')
            #
            layout.addWidget(self.scRemarkToolboxGroup)
        #
        def setRecordGroup():
            def setLinkButtonBranch(button, link):
                def setCurrentStage():
                    self._curSceneStage = link

                button.clicked.connect(setCurrentStage)
                button.clicked.connect(self.setRecordRefresh)
            #
            self.scRecordToolboxGroup = qtWidgets.QtToolboxGroup()
            self.scRecordToolboxGroup.setTitle('Record>{}'.format(self.LinkLis[0]))
            self.scRecordToolboxGroup.setExpanded(True)
            layout.addWidget(self.scRecordToolboxGroup)
            #
            linkToolBar = qtWidgets_.xToolBar()
            self.scRecordToolboxGroup.addWidget(linkToolBar)
            for seq, i in enumerate(self.LinkLis):
                linkButton = qtWidgets.QtEnablebutton('link#{}'.format(i))
                linkToolBar.addWidget(linkButton)
                linkButton.setAutoExclusive(True)
                if seq == 0:
                    linkButton.setChecked(True)
                #
                setLinkButtonBranch(linkButton, i)
            #
            self.recordBox = ifUnit.IfProductUnitRecordUnit()
            self.scRecordToolboxGroup.addWidget(self.recordBox)
        #
        def setBatchTool():
            def setLinkToolBar():
                linkToolBar = qtWidgets_.xToolBar()
                toolGroupBox.addWidget(linkToolBar)
                for seq, i in enumerate(self.LinkLis):
                    linkButton = qtWidgets.QtEnablebutton('link#{}'.format(i))
                    linkToolBar.addWidget(linkButton)
                    linkButton.setAutoExclusive(True)
                    if seq == 0:
                        linkButton.setChecked(True)
                    #
                    self._batchLinkButtonLis.append(linkButton)
            #
            def setToolBox():
                toolBox = qtWidgets.QtToolbox()
                toolBox.setTitle('Command Batch')
                #
                toolGroupBox.addWidget(toolBox)
                self.setScBatchTool(toolBox)
            #
            self._batchLinkButtonLis = []
            #
            toolGroupBox = qtWidgets.QtToolboxGroup()
            toolGroupBox.setTitle('Batch Tool')
            #
            layout.addWidget(toolGroupBox)
            #
            setLinkToolBar()
            setToolBox()
        #
        def setCheckTool():
            def setLinkToolBar():
                linkToolBar = qtWidgets_.xToolBar()
                toolGroupBox.addWidget(linkToolBar)
                for seq, i in enumerate(self.LinkLis):
                    linkButton = qtWidgets.QtRadioCheckbutton('basic#{}'.format(i))
                    linkToolBar.addWidget(linkButton)
                    #
                    if seq == 0:
                        linkButton.setChecked(True)
                    #
                    self._checkLinkButtonLis.append(linkButton)
            #
            def setToolBox():
                toolBox = qtWidgets.QtToolbox()
                toolBox.setTitle('Common Check')
                #
                toolGroupBox.addWidget(toolBox)
                self.setScBatchCheckTool(toolBox)
            #
            self._checkLinkButtonLis = []
            #
            toolGroupBox = qtWidgets.QtToolboxGroup()
            toolGroupBox.setTitle('Batch Check Tool')
            #
            layout.addWidget(toolGroupBox)
            #
            setLinkToolBar()
            setToolBox()
        #
        setRemarkGroup()
        setRecordGroup()
        setBatchTool()
        setCheckTool()
    # Scene
    def setCentralRefresh(self):
        def setBranch(seq, key, value):
            def getPreviewLis(linkLis):
                previewFileLis = []
                #
                index = 0
                for sceneLink in linkLis:
                    previewFile = scenePr.getScUnitPreviewServerFile(
                        projectName, sceneClass, sceneName, sceneVariant, sceneLink
                    )
                    if sceneLink == lxConfigure.LynxiProduct_Scene_Link_Animation:
                        if previewFile:
                            index = 1
                    #
                    viewFileName = scenePr.getSceneViewInfo(sceneIndex, sceneClass, sceneName)
                    tempPreviewFile = bscCommands.getOsTempVedioFile(
                        bscCommands.toOsFileReplaceFileName(previewFile, viewFileName))
                    #
                    previewFileLis.append(
                        ((previewFile, tempPreviewFile), (
                            bscMethods.StrCamelcase.toPrettify(sceneLink), 'Viewport ( {} )'.format(sceneVariant), (startFrame, endFrame)))
                    )
                #
                messageLis.append((4, previewFileLis))
                return index
            #
            def getBuildData(data):
                for linkClass, linkActionDataLis in data:
                    actionDatumLis.append((linkClass,))
                    for linkActionData in linkActionDataLis:
                        sceneLink, enable, explain, iconKeyword, createMethod, createOption, loadMethod, loadOption, productAction = linkActionData
                        #
                        update = scenePr.getSceneUnitProductUpdate(
                            projectName, sceneClass, sceneName, sceneVariant, sceneLink
                        )
                        exists = [False, True][update != appVariant.infoNonExistsLabel]
                        state = ['wait', None][update != appVariant.infoNonExistsLabel]
                        # Statistics
                        self._statisticsDic.setdefault(sceneLink, []).append(
                            (sceneIndex, sceneVariant, enable, exists)
                        )
                        #
                        if enable is True:
                            rgba = [(255, 255, 64, 255), (63, 255, 127, 255)][exists]
                            messageLis.append(
                                (5, (rgba, ('link#{}'.format(sceneLink), state), update))
                            )
                        else:
                            rgba = 95, 95, 95, 255
                            messageLis.append((5, (rgba, None, 'Non - Need')))
                        # Link Filter
                        self._filterIndexDic.setdefault(sceneLink, []).append(seq)
                        self._filterFrameDic.setdefault(sceneLink, []).append(frameCount)
                        #
                        if enable is True:
                            if exists is True:
                                if loadMethod is not None:
                                    if sceneLink == lxConfigure.LynxiProduct_Scene_Link_Light:
                                        loadExplain = 'Render File'
                                        loadIconKeyword = 'svg_basic@svg#render'
                                    else:
                                        loadExplain = explain
                                        loadIconKeyword = iconKeyword
                                    #
                                    actionDatumLis.append(
                                        ('Load {}'.format(loadExplain), (loadIconKeyword, 'svg_basic@svg#load_action'), True, loadMethod, loadOption)
                                    )
                                if productAction is True:
                                    if createMethod is not None:
                                        actionDatumLis.append(
                                            ('Create {}'.format(explain), (iconKeyword, 'svg_basic@svg#create_action'), True, createMethod, createOption)
                                        )
                            else:
                                if createMethod is not None:
                                    actionDatumLis.append(
                                        ('Create {}'.format(explain), (iconKeyword, 'svg_basic@svg#create_action'), True, createMethod, createOption)
                                    )
                                else:
                                    actionDatumLis.append(
                                        ('Non - Exists', 'basic#', False)
                                    )
                        else:
                            actionDatumLis.append(('Non - Need', 'basic#', False))
            # Layout
            def scCreateForLayoutCmd():
                from LxMaya.product import maScLoadCmds
                #
                from LxMaya.command import maFile
                #
                sceneStage = lxConfigure.LynxiScLayoutStages[0]
                #
                if self._isForce:
                    maFile.new()
                #
                maScLoadCmds.scUnitSceneCreateMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage
                )
            #
            def scLoadForLayoutCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScLayoutStages[0]
                #
                maScLoadCmds.scUnitSceneLoadMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage
                )
            # Animation
            def scCreateForAnimationCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScAnimationStages[0]
                #
                maScLoadCmds.scUnitSceneCreateMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage
                )
            #
            def scLoadForAnimationCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScAnimationStages[0]
                #
                maScLoadCmds.scUnitSceneLoadMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage
                )
            # Simulation
            def scCreateForSimulationCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScSimulationStages[0]
                #
                maScLoadCmds.scUnitSceneCreateMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage,
                    withCamera=True, withScenery=True, withFrame=True, withSize=True
                )
            #
            def scLoadForSimulationCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScSimulationStages[0]
                #
                maScLoadCmds.scUnitSceneLoadMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage
                )
            # Solver
            def scCreateForSolverCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScSolverStages[0]
                #
                maScLoadCmds.scUnitSceneCreateMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage,
                    withCamera=True, withScenery=True, withFrame=True, withSize=True,
                    withAstModel=True, withModelCache=True,
                    withAstCfx=True, withAstCfxFurCache=False,
                    withAstSolver=True, withAstSolverCache=True
                )
            #
            def scLoadForSolverCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScSolverStages[0]
                #
                maScLoadCmds.scUnitSceneLoadMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage
                )
            # Light
            def scCreateForLightCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScLightStages[1]
                #
                maScLoadCmds.scUnitSceneCreateMainCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage,
                    withCamera=True, withScenery=True, withFrame=True, withSize=True,
                    withAstModel=True, withModelCache=True,
                    withAstCfx=True, withAstCfxFurCache=True,
                    withExtraCache=True
                )
            #
            def lightLoadOption():
                args = sceneIndex, projectName, sceneClass, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_Light, startFrame, endFrame
                w = ifProductToolWindow.IfScRenderManagerWindow(parent=self)
                #
                w.setArgs(*args)
                #
                w.refreshMethod()
                w.windowShow()
            #
            def openScProductFolder():
                osPath = scenePr.sceneUnitFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    sceneClass, sceneName
                )
                bscMethods.OsDirectory.open(osPath)
            #
            def openScCacheFolder():
                osPath = scenePr.sceneCacheFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    sceneName, sceneVariant
                )
                bscMethods.OsDirectory.open(osPath)
            #
            def openScRenderFolder():
                osPath = scenePr.scUnitRenderBasicFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName, sceneClass, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_Light
                )
                bscMethods.OsDirectory.open(osPath)
            #
            def setScIndexWindowShowCmd():
                from LxInterface.qt.ifWidgets import ifProductToolWindow
                #
                w = ifProductToolWindow.IfScIndexManagerWindow(parent=self)
                w.setDefaultSize(*uiCore.Lynxi_Ui_Window_SubSize_Default)
                w.setNameText(viewExplain)
                w.setArgs(
                    '',
                    (
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant,
                    )
                )
                w.refreshMethod()
                w.windowShow()
            #
            sceneIndex, sceneVariant = key
            #
            (
                viewName,
                sceneClass, sceneName, scenePriority,
                scLayoutEnable, scAnimationEnable, scSolverEnable, scSimulationEnable, scLightEnable
             ) = value
            #
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
            startFrame, endFrame = scenePr.getScUnitFrameRange(
                projectName,
                sceneClass, sceneName, sceneVariant
            )
            # Count
            self._maxIndexCount += 1
            # Frame Count
            frameCount = endFrame - startFrame + 1
            self._maxFrameCount += frameCount
            if not tag in self._tagFilterSubExplainDic:
                self._tagFilterSubExplainDic[tag] = bscMethods.Frame.toTimeString(
                    frameValue=frameCount,
                    fpsValue=30
                )
            #
            gridItem = qtWidgets.QtGridviewItem()
            viewExplain = scenePr.getSceneViewInfo(sceneIndex, sceneClass, '{} - {}'.format(sceneName, sceneVariant))
            gridView.addItem(gridItem)
            #
            gridItem.setName(viewExplain)
            gridItem.setIcon('object#{}'.format(sceneClass))
            # gridItem.setTooltip(viewExplain)
            #
            gridItem.viewName = viewName
            gridItem.sceneIndex = sceneIndex
            gridItem.projectName = projectName
            gridItem.sceneClass = sceneClass
            gridItem.sceneName = sceneName
            gridItem.sceneVariant = sceneVariant
            #
            messageLis = []
            actionDatumLis = []
            imageIndex = getPreviewLis(self.LinkLis)
            getBuildData(
                [
                    (
                        'Layout',
                        [
                            (lxConfigure.LynxiProduct_Scene_Link_layout, scLayoutEnable, 'for Layout', 'link#layout', scCreateForLayoutCmd, None, scLoadForLayoutCmd, None, False)
                        ]
                    ),
                    (
                        'Animation',
                        [
                            (lxConfigure.LynxiProduct_Scene_Link_Animation, scAnimationEnable, 'for Animation', 'link#animation', scCreateForAnimationCmd, None, scLoadForAnimationCmd, None, True)
                        ]
                    ),
                    (
                        'FX',
                        [
                            (lxConfigure.LynxiProduct_Scene_Link_Simulation, scSimulationEnable, 'for Cloth Simulation', 'link#simulation', scCreateForSimulationCmd, None, scLoadForSimulationCmd, None, True),
                            (
                                lxConfigure.LynxiProduct_Scene_Link_Solver, scSolverEnable, 'for Hair Solver', 'link#solver', scCreateForSolverCmd, None, scLoadForSolverCmd, None, True)
                        ]
                    ),
                    (
                        'Light',
                        [
                            (lxConfigure.LynxiProduct_Scene_Link_Light, scLightEnable, 'for Light', 'svg_basic@svg#lightLink', scCreateForLightCmd, None, lightLoadOption, None, True)
                        ]
                    )
                ]
            )
            #
            actionDatumLis.extend([
                ('Extend Action', ),
                (
                    'Folder', 'svg_basic@svg#folder',
                    [
                        ('Open Product Folder', 'svg_basic@svg#folder', True, openScProductFolder),
                        ('Open Cache Folder', 'svg_basic@svg#folder', True, openScCacheFolder),
                        ('Open Render Folder', 'svg_basic@svg#folder', True, openScRenderFolder)
                    ]
                ),
                (
                    'Window', 'svg_basic@svg#subWindow',
                    [
                        ('Open Scene Index Window', 'svg_basic@svg#subWindow', True, setScIndexWindowShowCmd)
                    ]
                ),
                ('Other', ),
                ('Help', 'svg_basic@svg#help', True)
            ])
            #
            gridItem.setActionData(
                actionDatumLis, viewExplain
            )
            #
            messageWidget = qtWidgets.QtMessageWidget()
            messageWidget.setExplainWidth(20)
            messageWidget.setDefaultHeight(self.MessageHeight)
            messageWidget.setImageIndex(imageIndex)
            gridItem.addWidget(messageWidget, 0, 0, 1, 1)
            messageWidget.setDatumLis(messageLis, self._uiItemWidth, self._uiItemHeight)
            #
            classFilterKey = (sceneClass, scenePriority)
            self._filterIndexDic.setdefault(classFilterKey, []).append(seq)
            self._filterFrameDic.setdefault(classFilterKey, []).append(frameCount)
        #
        def setActionData():
            def openVedioCmd(osFiles):
                fileCmd = '" "'.join(osFiles)
                osCmdExe = 'KMPlayer.exe'
                if bscCommands.isOsExistsFile(osCmdExe):
                    osCmd = '''"{}" "{}"'''.format(osCmdExe, fileCmd)
                    bscCommands.setOsCommandRun_(osCmd.replace('/', '\\'))
            #
            def getVedio(sceneStage=None):
                lis = []
                #
                checkedItems = gridView.checkedItems()
                if checkedItems:
                    for i in checkedItems:
                        viewName = i.viewName
                        currentProjectName = i.projectName
                        sceneClass = i.sceneClass
                        sceneName = i.sceneName
                        sceneVariant = i.sceneVariant
                        #
                        if sceneStage is not None:
                            previewFile = scenePr.getScUnitPreviewServerFile(
                                currentProjectName,
                                sceneClass, sceneName, sceneVariant,
                                sceneStage
                            )
                            if previewFile:
                                lis.append(previewFile)
                        else:
                            animationPreviewFile = scenePr.getScUnitPreviewServerFile(
                                currentProjectName,
                                sceneClass, sceneName, sceneVariant,
                                lxConfigure.LynxiProduct_Scene_Link_Animation
                            )
                            if animationPreviewFile:
                                lis.append(animationPreviewFile)
                            else:
                                layoutPreviewFile = scenePr.getScUnitPreviewServerFile(
                                    currentProjectName,
                                    sceneClass, sceneName, sceneVariant,
                                    lxConfigure.LynxiProduct_Scene_Link_layout
                                )
                                if layoutPreviewFile:
                                    lis.append(layoutPreviewFile)
                return lis
            #
            def setCheckedLayoutVedioPlayCmd():
                previewLis = getVedio(lxConfigure.LynxiProduct_Scene_Link_layout)
                if previewLis:
                    openVedioCmd(previewLis)
            #
            def setCheckedAnimationVedioPlayCmd():
                previewLis = getVedio(lxConfigure.LynxiProduct_Scene_Link_Animation)
                if previewLis:
                    openVedioCmd(previewLis)
            #
            def setCheckedActiveVedioPalyCmd():
                previewLis = getVedio()
                if previewLis:
                    openVedioCmd(previewLis)
            #
            gridView.setActionData([
                ('Extend Action', ),
                ('Play Layout Vedio(s)', 'svg_basic@svg#play', True, setCheckedLayoutVedioPlayCmd),
                ('Play Animation Vedio(s)', 'svg_basic@svg#play', True, setCheckedAnimationVedioPlayCmd),
                ('Play Active Vedio(s)', 'svg_basic@svg#play', True, setCheckedActiveVedioPalyCmd)
            ])
        #
        def setMain():
            self._scUpToolboxGroup.setTitle('Scene')
            #
            setData = scenePr.getUiSceneSetDataDic(projectName)
            gridView.cleanItems()
            if setData:
                maxCount = len(setData)
                if self.connectObject():
                    self.connectObject().mainWindow().setMaxProgressValue(maxCount)
                for seq, (k, v) in enumerate(setData.items()):
                    if self.connectObject():
                        self.connectObject().mainWindow().updateProgress()
                    #
                    setBranch(seq, k, v)
                #
                self.setFilterItemRefresh()
                #
                gridView.setRefresh()
                gridView.setSortByName()
                #
                self._maxIndexCount = maxCount
            else:
                self.setFilterItemRefresh()
                #
                gridView.setRefresh()
        #
        self._tagLis = []
        self._tagFilterEnableDic = {}
        self._tagFilterIndexDic = {}
        #
        self._filterIndexDic.clear()
        self._filterFrameDic.clear()
        #
        self._statisticsDic.clear()
        #
        self._maxIndexCount = 0
        self._maxFrameCount = 0
        #
        projectName = self._connectObject.getProjectName()
        #
        gridView = self._scGridview
        #
        setMain()
        setActionData()
        self._initTagFilterAction(gridView)
    #
    def setCameraRefresh(self):
        def getScCameraLoadData():
            lis = []
            if self._cameraDatas:
                for i in self._cameraDatas:
                    if i[0].isChecked():
                        lis.append(i[1])
            #
            return lis
        #
        def setBranch(seq, key, value):
            def setSubActions():
                def scSubLoadCameraCacheCmd():
                    from LxMaya.command import maFile, maPreference
                    #
                    maPreference.setAnimationTimeUnit(projectName)
                    maFile.setAlembicCacheImport(scCameraFile)
                #
                def scSubShowScCameraCacheManagerWinCmd():
                    from LxInterface.qt.ifWidgets import ifProductToolWindow
                    #
                    w = ifProductToolWindow.IfCacheManagerWindow(self)
                    w.setNameText(viewExplain)
                    w.setArgs(
                        lxConfigure.LynxiScCameraCacheType,
                        (
                            projectName,
                            sceneIndex,
                            sceneClass, sceneName, sceneVariant,
                            subLabel
                        )
                    )
                    w.setListCache()
                    w.windowShow()
                #
                gridItem.setActionData([
                    ('Basic', ),
                    ('Load Current Camera ( Cache )', ('svg_basic@svg#file', 'svg_basic@svg#load_action'), True, scSubLoadCameraCacheCmd),
                    ('Extend Action',),
                    ('Scene Camera Cache Manager', 'svg_basic@svg#subWindow', True, scSubShowScCameraCacheManagerWinCmd)
                ])
            #
            timestamp, sceneStage, startFrame, endFrame, scCameraFile = value
            subLabel = bscCommands.getSubLabel(seq)
            #
            if subLabel:
                viewExplain = '{} - {}'.format(key.capitalize(), subLabel)
            else:
                viewExplain = key.capitalize()
            #
            gridItem = qtWidgets.QtGridviewItem()
            gridItem.setName(viewExplain)
            gridItem.setIcon('basic#camera')
            gridView.addItem(gridItem)
            #
            sceneLink = scenePr.getSceneLink(sceneStage)
            #
            messageLis = []
            preview = scenePr.getScUnitPreviewServerFile(
                projectName, sceneClass, sceneName, sceneVariant, sceneStage
            )
            subPreviewFile = bscCommands.getOsSubFile(preview, subLabel)
            previewFileLis = [
                (
                    subPreviewFile,
                    (
                        bscMethods.StrCamelcase.toPrettify(scenePr.getSceneLink(sceneStage)),
                        'Viewport',
                        (startFrame, endFrame)
                     )
                 )
            ]
            messageLis.append((4, previewFileLis))
            messageLis.append((1, ('link#{}'.format(sceneLink), bscMethods.OsTime.getCnPrettifyByTimestamp(timestamp))))
            #
            messageWidget = qtWidgets.QtMessageWidget()
            messageWidget.setExplainWidth(20)
            gridItem.addWidget(messageWidget, 0, 0, 1, 1)
            messageWidget.setDatumLis(messageLis, self._cameraItemWidth, self._cameraItemHeight)
            #
            self._cameraDatas.append(
                (gridItem, scCameraFile)
            )
            #
            setSubActions()
        #
        def setActionData():
            def scLoadCameraCmd():
                from LxMaya.command import maPreference
                #
                from LxMaya.product import maScLoadCmds
                #
                loadDatumLis = getScCameraLoadData()
                #
                if loadDatumLis:
                    maPreference.setAnimationTimeUnit(projectName)
                    for seq, i in enumerate(loadDatumLis):
                        subLabel = bscCommands.getSubLabel(seq)
                        maScLoadCmds.scUnitCameraCacheLoadSubCmd(
                            projectName,
                            sceneIndex,
                            sceneClass, sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_Light, subLabel,
                            withCameraCache=i
                        )
            #
            def scOpenCameraCacheFolderCmd():
                osPath = scenePr.scCameraCacheFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    sceneName, sceneVariant
                )
                bscMethods.OsDirectory.open(osPath)
            #
            gridView.setActionData([
                ('Config',),
                ('Load Frame', 'checkBox', self.isLoadScAnimFrameEnable, self.setLoadScAnimFrameEnable),
                ('Action', ),
                ('Load Camera(s) for Light', ('svg_basic@svg#file', 'svg_basic@svg#load_action'), True, scLoadCameraCmd),
                ('Folder', ),
                ('Open Camera Cache Folder', 'svg_basic@svg#folder', True, scOpenCameraCacheFolderCmd)
            ])
        #
        def setMain():
            inData = scenePr.getSceneCameraIndexDataDic(
                projectName, sceneClass, sceneName, sceneVariant
            )
            gridView.cleanItems()
            if inData:
                for k, v in inData.items():
                    for seq, i in enumerate(v):
                        setBranch(seq, k, i)
            #
            gridView.setRefresh()
            gridView.setSortByName()
        #
        self.listViewBoxItemDic = {}
        #
        self._cameraDatas = []
        #
        projectName = self._curProjectName
        #
        sceneIndex = self._curSceneClass
        sceneClass = self._curSceneClass
        sceneName = self._curSceneName
        sceneVariant = self._curSceneVariant
        #
        gridView = self._cameraListViewBox
        #
        if self._downRefreshEnable is True:
            setMain()
            setActionData()
    #
    def setAssetRefresh(self):
        def setBranch(seq, key, value):
            def getSubBuildData(data):
                for subIconKeyword, subAstCheckState, subAstEnable, subAstTimeTag in data:
                    if subAstEnable:
                        exists = [False, True][subAstTimeTag is not None]
                        rgba = [(255, 255, 64, 255), (63, 255, 127, 255)][exists]
                        if exists:
                            messageLis.append((5, (rgba, (subIconKeyword, subAstCheckState), bscMethods.OsTime.getCnPrettifyByTimetag(subAstTimeTag))))
                        else:
                            messageLis.append((5, (rgba, (subIconKeyword, 'wait'), appVariant.infoNonExistsLabel)))
                    else:
                        rgba = 95, 95, 95, 255
                        messageLis.append(
                            (5, (rgba, None, 'Non - Need'))
                        )
            #
            def setSubActions():
                def isScSubLoadAstModelCacheEnable():
                    return scAstModelCacheTimeTag is not None
                #
                def scSubLoadAstModelCacheCmd():
                    from LxMaya.command import maFile, maPreference
                    #
                    maPreference.setAnimationTimeUnit(projectName)
                    maFile.setAlembicCacheImport(scAstModelCacheFile)
                #
                def scSubShowAstModelCacheManagerWinCmd():
                    from LxInterface.qt.ifWidgets import ifProductToolWindow
                    #
                    w = ifProductToolWindow.IfCacheManagerWindow(self)
                    w.setNameText(viewExplain)
                    w.setArgs(
                        lxConfigure.LynxiScAstModelCacheType,
                        (
                            projectName,
                            sceneIndex,
                            sceneClass, sceneName, sceneVariant,
                            startFrame, endFrame,
                            assetIndex, assetClass, assetName, number, assetVariant
                        )
                    )
                    w.setListCache()
                    w.windowShow()
                #
                subActions = [
                    ('Basic',),
                    ('Load Current Asset Model ( Cache )', ('svg_basic@svg#file', 'svg_basic@svg#load_action'), isScSubLoadAstModelCacheEnable, scSubLoadAstModelCacheCmd),
                    ('Extend Action', ),
                    ('Asset Model Cache Manager', 'svg_basic@svg#subWindow', isScSubLoadAstModelCacheEnable, scSubShowAstModelCacheManagerWinCmd)
                ]
                #
                gridItem.setActionData(subActions, viewExplain)
            #
            (
                scAstModelCacheTimestamp,
                cacheSceneStage,
                startFrame, endFrame,
                scAstModelCacheFile,
                assetIndex,
                assetClass, assetName, number, assetVariant
            ) = value
            #
            gridItem = qtWidgets.QtGridviewItem()
            viewExplain = assetPr.getAssetViewInfo(assetIndex, assetClass, '{} - {} - {}'.format(assetName, number, assetVariant))
            gridItem.setName(viewExplain)
            gridItem.setIcon('svg_basic@svg#package')
            # gridItem.setTooltip(viewExplain)
            gridView.addItem(gridItem)
            #
            isAstModelEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Model)
            isAstRigEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Rig)
            isAstCfxEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Cfx)
            isAstSolverEnable = assetPr.getAssetIsLinkEnable(assetIndex, lxConfigure.LynxiProduct_Asset_Link_Solver)
            #
            viewportPreview = dbGet.dbAstViewportPreviewFile(assetIndex)
            renderPreview = dbGet.dbAstRenderPreviewFile(assetIndex, assetVariant)
            messageLis = [
                (4, [(viewportPreview, ('Model', 'Viewport ( {} )'.format(assetVariant))), (renderPreview, ('Model', 'Render ( {} )'.format(assetVariant)))])
            ]
            #
            scAstModelCacheTimeTag = scenePr.getScAstModelCacheActiveTimeTag(
                projectName,
                sceneName, sceneVariant,
                assetName, number
            )
            #
            scAstSolverCacheTimeTag = scenePr.getScAstSolverCacheActiveTimeTag(
                projectName,
                sceneName, sceneVariant,
                assetName, number
            )
            #
            scAstRigExtraCacheTimeTag = scenePr.getScAstRigExtraCacheActiveTimeTag(
                projectName,
                sceneName, sceneVariant,
                assetName, number
            )
            #
            getSubBuildData(
                [
                    ('link#model', dbGet.getScModelCacheMeshCheck(assetIndex, scAstModelCacheFile), isAstModelEnable, scAstModelCacheTimeTag),
                    ('link#solver', None, isAstSolverEnable, scAstSolverCacheTimeTag),
                    ('link#rig', None, isAstRigEnable, scAstRigExtraCacheTimeTag)
                ]
            )
            if scAstModelCacheTimestamp is None:
                gridItem.setPressable(False)
                gridItem.setCheckable(False)
            #
            messageWidget = qtWidgets.QtMessageWidget()
            messageWidget.setExplainWidth(20)
            imageIndex = [0, 1][renderPreview is not none]
            messageWidget.setImageIndex(imageIndex)
            gridItem.addWidget(messageWidget, 0, 0, 1, 1)
            #
            widget = qtCore.QWidget_()
            widget.setMaximumWidth(32)
            gridItem.addWidget(widget, 0, 1, 1, 1)
            operationLayout = qtCore.QVBoxLayout_(widget)
            operationLayout.setAlignment(qtCore.QtCore.Qt.AlignTop)
            operationLayout.setContentsMargins(4, 4, 4, 4)
            # CFX Product
            scWithCfxProdSubButton = qtWidgets.QtEnablebutton('link#cfx')
            scWithCfxProdSubButton.setCheckable(isAstCfxEnable)
            scWithCfxProdSubButton.setTooltip(
                'Clicked to Enable / Disable Load Asset with CFX'
            )
            operationLayout.addWidget(scWithCfxProdSubButton)
            scWithCfxProdSubButton.setChecked(True)
            #
            scWithCfxCacheSubButton = qtWidgets.QtEnablebutton('basic#cacheFile')
            scWithCfxCacheSubButton.setCheckable(isAstCfxEnable)
            scWithCfxCacheSubButton.setTooltip(
                'Clicked to Enable / Disable Load Asset with CFX Cache'
            )
            operationLayout.addWidget(scWithCfxCacheSubButton)
            scWithCfxCacheSubButton.setChecked(True)
            #
            scWithSolverCacheSubButton = qtWidgets.QtEnablebutton('link#solver')
            scWithSolverCacheSubButton.setCheckable(isAstSolverEnable)
            operationLayout.addWidget(scWithSolverCacheSubButton)
            scWithSolverCacheSubButton.setChecked(True)
            #
            scWithExtraSubButton = qtWidgets.QtEnablebutton('link#rig')
            scWithExtraSubButton.setCheckable(isAstRigEnable)
            scWithExtraSubButton.setTooltip(
                'Clicked to Enable / Disable Load Asset with Extra'
            )
            operationLayout.addWidget(scWithExtraSubButton)
            scWithExtraSubButton.setChecked(True)
            #
            messageWidget.setDatumLis(messageLis, self._assetItemWidth, self._assetItemHeight)
            #
            self._assetDatas.append(
                (gridItem, scAstModelCacheFile, assetIndex, assetClass, assetName, number, assetVariant)
            )
            #
            setSubActions()
        #
        def setActionData():
            def getCheckedScAstDataLis():
                lis = []
                if self._assetDatas:
                    for j in self._assetDatas:
                        gridItem, scAstModelCacheFile, assetIndex, assetClass, assetName, number, assetVariant = j
                        if gridItem.isChecked():
                            lis.append(
                                (scAstModelCacheFile, assetIndex, assetClass, assetName, number, assetVariant)
                            )
                return lis
            #
            def scLoadAstForSimulationCmd():
                def scLoadAssetBranch(value):
                    scAstModelCacheFile, assetIndex, assetClass, assetName, number, assetVariant = value
                    #
                    maScLoadCmds.scUnitAstModelCacheLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant, lxConfigure.LynxiScSimulationStages[0],
                        assetIndex,
                        assetClass, assetName, number, assetVariant,
                        withModelCache=True
                    )
                    #
                    maScLoadCmds.scUnitAstModelPoseCacheLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneName, sceneVariant, lxConfigure.LynxiScSimulationStages[0],
                        assetIndex,
                        assetClass, assetName, number, assetVariant,
                        withModelPoseCache=True
                    )
                #
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScSimulationStages[0]
                #
                if self._isLoadScAnimFrame is True:
                    maScLoadCmds.scUnitFrameLoadCmd(
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant, sceneStage
                    )
                #
                assetDatumLis = getCheckedScAstDataLis()
                #
                if assetDatumLis:
                    startFrame, endFrame = scenePr.getScUnitFrameRange(
                        projectName, sceneClass, sceneName, sceneVariant
                    )
                    #
                    progressExplain = u'''Load Scene Asset(s)'''
                    maxValue = len(assetDatumLis)
                    progressBar = bscObjects.If_Progress(progressExplain, maxValue)
                    #
                    for i in assetDatumLis:
                        progressBar.update()
                        scLoadAssetBranch(i)
            #
            def scLoadAstForSolverCmd():
                def scLoadAssetBranch(value):
                    scAstModelCacheFile, assetIndex, assetClass, assetName, number, assetVariant = value
                    maScLoadCmds.scUnitAssetLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex, assetClass, assetName, number, assetVariant,
                        withAstModel=True, withModelCache=scAstModelCacheFile,
                        withAstCfx=True, withAstCfxFurCache=True,
                        withAstSolver=True, withAstSolverCache=True,
                    )
                #
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScSolverStages[0]
                #
                if self._isLoadScAnimFrame is True:
                    maScLoadCmds.scUnitFrameLoadCmd(
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant, sceneStage
                    )
                #
                assetDatumLis = getCheckedScAstDataLis()
                #
                if assetDatumLis:
                    startFrame, endFrame = scenePr.getScUnitFrameRange(
                        projectName, sceneClass, sceneName, sceneVariant
                    )
                    #
                    progressExplain = u'''Load Scene Asset(s)'''
                    maxValue = len(assetDatumLis)
                    progressBar = bscObjects.If_Progress(progressExplain, maxValue)
                    #
                    for i in assetDatumLis:
                        progressBar.update()
                        scLoadAssetBranch(i)
            #
            def scLoadAstForLightCmd():
                def scLoadAssetBranch(value):
                    scAstModelCacheFile, assetIndex, assetClass, assetName, number, assetVariant = value
                    #
                    maScLoadCmds.scUnitAssetLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex, assetClass, assetName, number, assetVariant,
                        withAstModel=True, withModelCache=scAstModelCacheFile,
                        withAstCfx=True, withAstCfxFurCache=True,
                        withExtraCache=True
                    )
                #
                from LxMaya.command import maUtils
                #
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiScLightStages[1]
                #
                if self._isLoadScAnimFrame is True:
                    maScLoadCmds.scUnitFrameLoadCmd(
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant, sceneStage
                    )
                #
                assetDatumLis = getCheckedScAstDataLis()
                #
                if assetDatumLis:
                    startFrame, endFrame = scenePr.getScUnitFrameRange(
                        projectName, sceneClass, sceneName, sceneVariant
                    )
                    #
                    progressExplain = u'''Load Scene Asset(s)'''
                    maxValue = len(assetDatumLis)
                    progressBar = bscObjects.If_Progress(progressExplain, maxValue)
                    #
                    for i in assetDatumLis:
                        progressBar.update()
                        scLoadAssetBranch(i)
                    # TD Command
                    tdCommand = scenePr.getScTdLoadCommand(projectName, scenePr.getSceneLink(sceneStage))
                    if tdCommand:
                        maUtils.runMelCommand(tdCommand)
            #
            def scOpenAssetCacheFolderCmd():
                osPath = scenePr.scAstAlembicCacheFolder(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName,
                    sceneName, sceneVariant
                )
                bscMethods.OsDirectory.open(osPath)
            #
            gridView.setActionData(
                [
                    ('Config',),
                    ('Load Frame', 'checkBox', self.isLoadScAnimFrameEnable, self.setLoadScAnimFrameEnable),
                    ('FX',),
                    ('Load Asset(s) for Cloth Simulation', ('link#simulation', 'svg_basic@svg#load_action'), True, scLoadAstForSimulationCmd),
                    ('Load Asset(s) for Hair Solver', ('link#solver', 'svg_basic@svg#load_action'), True, scLoadAstForSolverCmd),
                    ('Light',),
                    ('Load Asset(s) for Light', ('svg_basic@svg#lightLink', 'svg_basic@svg#load_action'), True, scLoadAstForLightCmd),
                    ('Extend Action', ),
                    ('Open Asset(s) Alembic Cache Folder', 'svg_basic@svg#folder', True, scOpenAssetCacheFolderCmd)
                ]
            )
        #
        def setMain():
            inData = scenePr.getSceneAssetIndexDataDic(
                projectName, sceneClass, sceneName, sceneVariant
            )
            gridView.cleanItems()
            if inData:
                for k, v in inData.items():
                    for seq, i in enumerate(v):
                        setBranch(seq, k, i)
            #
            gridView.setRefresh()
            gridView.setSortByName()
        #
        self.listViewBoxItemDic = {}
        #
        self._assetDatas = []
        #
        sceneIndex = self._curSceneIndex
        #
        projectName = self._curProjectName
        #
        sceneClass = self._curSceneClass
        sceneName = self._curSceneName
        sceneVariant = self._curSceneVariant
        #
        gridView = self._scAstGridview
        #
        if self._downRefreshEnable is True:
            setMain()
            setActionData()
    #
    def setSceneryRefresh(self):
        def setBranch(arg):
            objectPath, definition, namespace = arg
            #
            treeItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(treeItem)
            treeItem.setIcon('svg_basic@svg#assembly_object')
            treeItem.setNameText(definition)
        #
        def setActionData():
            def scLoadSceneryForSolver():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiProduct_Scene_Link_Solver
                #
                maScLoadCmds.scUnitSceneryExtraLoadLoadCmd(
                    projectName,
                    sceneClass, sceneName, sceneVariant, sceneStage
                )

            #
            def scLoadSceneryForLightCmd():
                from LxMaya.product import maScLoadCmds
                #
                sceneStage = lxConfigure.LynxiProduct_Scene_Link_Light
                #
                maScLoadCmds.scUnitSceneryExtraLoadLoadCmd(
                    projectName,
                    sceneClass, sceneName, sceneVariant, sceneStage
                )

            #
            treeView.setActionData([
                ('FX',),
                ('Reference Scenery(s) for Solver', ('svg_basic@svg#file', 'svg_basic@svg#reference_action'), True,
                 scLoadSceneryForSolver),
                ('Light',),
                ('Reference Scenery(s) for Light', ('svg_basic@svg#file', 'svg_basic@svg#reference_action'), True,
                 scLoadSceneryForLightCmd)
            ])
        #
        def setMain():
            datumDic = scenePr.getScSceneryExtraData(
                projectName,
                sceneClass, sceneName, sceneVariant
            )
            #
            treeView.cleanItems()
            if datumDic:
                if lxConfigure.LynxiAssemblyReferenceDataKey in datumDic:
                    assemblyDataLis = datumDic[lxConfigure.LynxiAssemblyReferenceDataKey]
                    if assemblyDataLis:
                        for i in assemblyDataLis:
                            setBranch(i)
            #
            treeView.setRefresh()
        #
        projectName = self._curProjectName
        #
        sceneIndex = self._curSceneIndex
        sceneClass = self._curSceneClass
        sceneName = self._curSceneName
        sceneVariant = self._curSceneVariant
        #
        treeView = self._sceneryTreeView
        #
        if self._downRefreshEnable is True:
            setMain()
            setActionData()
    #
    def isLoadScAnimFrameEnable(self):
        return self._isLoadScAnimFrame
    #
    def setLoadScAnimFrameEnable(self):
        self._isLoadScAnimFrame = not self._isLoadScAnimFrame
    #
    def setScBatchTool(self, layout):
        def setFileBatch():
            def getLinks():
                lis = []
                for seq, link in enumerate(self.LinkLis):
                    enableButton = self._batchLinkButtonLis[seq]
                    if enableButton.isChecked():
                        lis.append(link)
                #
                return lis
            #
            def setBranch(progressBar, gridItem, sceneStages, pythonCommandString):
                logWin_ = bscObjects.If_Log()
                progressBar.update()
                #
                sceneIndex = gridItem.sceneIndex
                #
                projectName = gridItem.projectName
                #
                sceneClass = gridItem.sceneClass
                sceneName = gridItem.sceneName
                sceneVariant = gridItem.sceneVariant
                #
                for sceneStage in sceneStages:
                    serverProductFile = scenePr.sceneUnitProductFile(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName, sceneClass, sceneName, sceneVariant, sceneStage
                    )[1]
                    localSourceFile = scenePr.sceneUnitSourceFile(
                        lxConfigure.LynxiRootIndex_Local,
                        projectName, sceneClass, sceneName, sceneVariant, sceneStage
                    )[1]
                    #
                    if bscCommands.isOsExist(serverProductFile):
                        logWin_.addStartProgress(u'Open', serverProductFile)
                        #
                        maFile.openMayaFileToLocal(serverProductFile, localSourceFile)
                        #
                        try:
                            self.runPythonCommand(pythonCommandString)
                        except:
                            logWin_.addError(serverProductFile)
                        #
                        maFile.new()
                        #
                        logWin_.addCompleteProgress()
            #
            def setMain():
                enableLinks = getLinks()
                checkedGridItems = self._scGridview.checkedItems()
                pythonCommandString = commandEditBox.text()
                if checkedGridItems and enableLinks and pythonCommandString:
                    # View Progress
                    explain = '''Batch File by Command'''
                    maxValue = len(checkedGridItems)
                    progressBar = bscObjects.If_Progress(explain, maxValue)
                    #
                    logWin_ = bscObjects.If_Log(title='Scene Batch')
                    logWin_.showUi()

                    logWin_.addStartTask('Start Batch')
                    [setBranch(progressBar, i, enableLinks, pythonCommandString) for i in checkedGridItems]
                    logWin_.addStartTask('Complete Batch')
            #
            if bscCommands.isMayaApp():
                from LxMaya.command import maFile
                setMain()
        #
        commandEditBox = qtWidgets.QtTextbrower()
        layout.addWidget(commandEditBox, 0, 0, 1, 1)
        self.highlighter = qtCore.xPythonHighlighter(commandEditBox.textEdit().document())
        #
        pressButton = qtWidgets.QtPressbutton()
        layout.addWidget(pressButton, 1, 0, 1, 1)
        pressButton.setNameText('File Command Batch')
        pressButton.setIcon('svg_basic@svg#python')
        pressButton.clicked.connect(setFileBatch)
    #
    def setScBatchCheckTool(self, layout):
        def setSceneryCheck():
            def getSceneStage():
                return self.LinkLis[[seq for seq, i in enumerate(self._checkLinkButtonLis) if i.isChecked()][0]]
            #
            def setMain():
                def setMainBranch(gridItem):
                    progressBar.update()
                    #
                    sceneIndex = gridItem.sceneIndex
                    #
                    projectName = gridItem.projectName
                    #
                    sceneClass = gridItem.sceneClass
                    sceneName = gridItem.sceneName
                    sceneVariant = gridItem.sceneVariant
                    #
                    sceneryExtraDataFile = scenePr.scUnitSceneryExtraFile(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName, sceneClass, sceneName, sceneVariant, sceneStage
                    )[1]
                    #
                    if bscCommands.isOsExist(sceneryExtraDataFile):
                        extraData = bscMethods.OsJson.read(sceneryExtraDataFile)
                        if extraData:
                            asbRefDatas = extraData[lxConfigure.LynxiAssemblyReferenceDataKey]
                            asbTransDatas = extraData[lxConfigure.LynxiTransformationDataKey]
                            if asbRefDatas:
                                for seq, j in enumerate(asbRefDatas):
                                    asbTransData = asbTransDatas[seq]
                                    mainObject, mainAbsTrans = asbTransData[0]
                                    mainName = mainObject.split('_')[1]
                                    if mainName in sceneryIndexDic:
                                        mainIndex = sceneryIndexDic[mainName]
                                        mainViewInfo = sceneryPr.getSceneryViewInfo(mainIndex)
                                    else:
                                        mainViewInfo = '?'
                                    #
                                    isMatch = mainAbsTrans == defTrans
                                    if isMatch is False:
                                        print scenePr.getSceneViewInfo(sceneIndex, sceneClass, sceneVariant), sceneName
                                        print '>', mainViewInfo, mainName, mainObject
                                        for j_ in mainAbsTrans:
                                            print j_[0], j_[1]
                                    #
                                    mainAsbObjPath, mainAsbDefFile, mainAsbNs = asbRefDatas[seq]
                                    if mainAsbObjPath.startswith('|'):
                                        mainAsbObjPath = mainAsbObjPath[1:]
                                    sourceExtraFile = mainAsbDefFile[:-10] + '.extra'
                                    #
                                    sourceDic = {}
                                    if bscCommands.isOsExist(sourceExtraFile):
                                        sourceExtraData = bscMethods.OsJson.read(sourceExtraFile)
                                        if sourceExtraData:
                                            sourceTransData = sourceExtraData['transformation'][0]
                                            for i_ in sourceTransData:
                                                sourceDic[i_[0]] = i_[1]
                                    #
                                    lis = []
                                    if sourceDic:
                                        for i_ in asbTransData:
                                            objPath, transData = i_
                                            if objPath.startswith('|'):
                                                objPath = objPath[1:]
                                            #
                                            objPath_ = objPath.replace(mainAsbNs + ':', '')[len(mainAsbObjPath) + 1:]
                                            if objPath_ in sourceDic:
                                                sourceTrans = sourceDic[objPath_]
                                                if not sourceTrans == transData:
                                                    subObjectName = objPath_.split('|')[-1]
                                                    assetName = subObjectName.split('_')[1]
                                                    if assetName in assetIndexDic:
                                                        assetIndex = assetIndexDic[assetName]
                                                        assetViewInfo = assetPr.getAssetViewInfo(assetIndex)
                                                    else:
                                                        assetViewInfo = '?'
                                                    #
                                                    lis.append((assetViewInfo, assetName, subObjectName))
                                    # if lis:
                                    #     print scenePr.getSceneViewInfo(sceneIndex, sceneVariant), sceneName
                                    #     print '>', mainViewInfo, mainName, mainObject
                                    #     for j_ in lis:
                                    #         print '>>', j_[0], j_[1], j_[2]
                #
                checkedGridItems = self._scGridview.checkedItems()
                if checkedGridItems:
                    assetIndexDic = assetPr.getAssetIndexDic()
                    sceneryIndexDic = sceneryPr.getSceneryDescriptionDic()
                    # View Progress
                    explain = '''Read Mesh Information'''
                    maxValue = len(checkedGridItems)
                    progressBar = bscObjects.If_Progress(explain, maxValue)
                    #
                    [setMainBranch(i) for i in checkedGridItems]
            #
            defTrans = [
                [u'.translateX', 0.0],
                [u'.translateY', 0.0],
                [u'.translateZ', 0.0],
                [u'.rotateX', 0.0],
                [u'.rotateY', 0.0],
                [u'.rotateZ', 0.0],
                [u'.scaleX', 1.0],
                [u'.scaleY', 1.0],
                [u'.scaleZ', 1.0],
                [u'.rotatePivotX', 0.0],
                [u'.rotatePivotY', 0.0],
                [u'.rotatePivotZ', 0.0],
                [u'.scalePivotX', 0.0],
                [u'.scalePivotY', 0.0],
                [u'.scalePivotZ', 0.0],
                [u'.visibility', True]
            ]
            #
            sceneStage = getSceneStage()
            #
            setMain()
        #
        noteBox = qtWidgets.QtTextbrower()
        layout.addWidget(noteBox, 0, 0, 1, 1)
        #
        pressButton = qtWidgets.QtPressbutton()
        layout.addWidget(pressButton, 1, 0, 1, 1)
        pressButton.setNameText('Scenery Check')
        pressButton.setIcon('svg_basic@svg#python')
        pressButton.clicked.connect(setSceneryCheck)
    #
    def setRecordRefresh(self):
        sceneIndex = self._curSceneIndex
        #
        projectName = self._curProjectName
        #
        sceneClass = self._curSceneClass
        sceneName = self._curSceneName
        sceneVariant = self._curSceneVariant
        sceneStage = self._curSceneStage
        #
        backupSourceFile = scenePr.sceneUnitSourceFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName, sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        #
        backupProductFile = scenePr.sceneUnitProductFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName, sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        #
        if self._rightRefreshEnable is True:
            self.recordBox.setRecordConnect(backupSourceFile, backupProductFile)
            if sceneStage:
                self.scRecordToolboxGroup.setTitle('Record>{}'.format(bscMethods.StrCamelcase.toPrettify(sceneStage)))
    #
    def setFilterItemRefresh(self, ignoreRefresh=False):
        for filterKey, filterItem in self._filterItemDic.items():
            if filterKey in self._filterIndexDic:
                filterIndexLis = self._filterIndexDic[filterKey]
                frameLis = self._filterFrameDic[filterKey]
                #
                filterItem.setViewFilterItemIndexes(filterIndexLis)
                filterItem.setMaxFilterCount(self._maxIndexCount)
            else:
                frameLis = []
                filterItem.setViewFilterItemIndexes([])
            #
            if ignoreRefresh is False:
                filterItem.setRefresh()
            #
            if self._isShowTimeEnable is True:
                frameCount = sum(frameLis)
                fpsValue = 30
                if frameCount:
                    uiSubName = '{} / {}'.format(
                        bscMethods.Frame.toTimeString(frameValue=frameCount, fpsValue=fpsValue),
                        bscMethods.Frame.toTimeString(frameValue=self._maxFrameCount, fpsValue=fpsValue)
                    )
                    filterItem.setUiSubName(uiSubName)
    #
    def setupUnitAction(self):
        def isForce():
            return self._isForce
        #
        def setForceSwitch():
            self._isForce = not self._isForce
        #
        def isShowTime():
            return self._isShowTimeEnable
        #
        def setShowTimeEnable():
            self._isShowTimeEnable = not self._isShowTimeEnable
            #
            self.setFilterItemRefresh(ignoreRefresh=True)
        #
        if self.connectObject():
            tabIndex = self.connectObject().tabIndex(self)
            tab = self.connectObject().tabAt(tabIndex)
            tab.setActionData(
                [
                    ('Basic Action', ),
                    ('Refresh', 'svg_basic@svg#refresh', True, self.setCentralRefresh),
                    ('Load Config', ),
                    ('New Scene', 'checkBox', isForce, setForceSwitch),
                    ('Filter Config',),
                    ('Show Time', 'checkBox', isShowTime, setShowTimeEnable),
                    ('About', ),
                    ('Help', 'svg_basic@svg#help', True)
                ]
            )
    #
    def initToolBox(self):
        self._uiItemWidth = 200
        self._uiItemHeight = 200
        #
        self._cameraItemWidth = 200
        self._cameraItemHeight = 200
        #
        self._assetItemWidth = 200
        self._assetItemHeight = 200
        #
        self._sceneryItemWidth = 200
        self._sceneryItemHeight = 200
        #
        self._statisticsDic = {}
        #
        self._isForce = True
        #
        self._curSceneIndex = None
        self._curProjectName = None
        self._curSceneClass = None
        self._curSceneName = None
        self._curSceneVariant = None
        self._curSceneStage = None
        #
        self._rightRefreshEnable = False
        #
        self._downRefreshEnable = False
        #
        self._cameraDatas = []
        self._assetDatas = []
        self._sceneryDatas = []
        #
        self._isLoadScAnimFrame = True
        #
        self._statisticsUiDic = {}
        #
        self._maxIndexCount = 0
        self._maxFrameCount = 0
        #
        self._isShowTimeEnable = False
    #
    def setupUnitWidgets(self):
        self.setupLeftWidget(self._leftScrollLayout)
        self.setupCentralWidget(self._centralScrollLayout)
        self.setupRightWidget(self._rightScrollLayout)
