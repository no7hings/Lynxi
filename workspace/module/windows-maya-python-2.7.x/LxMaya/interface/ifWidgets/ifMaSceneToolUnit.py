# coding=utf-8
from LxBasic import bscMtdCore, bscObjects, bscMethods

from LxCore.config import appCfg

from LxPreset import prsConfigure, prsOutputs, prsMethods

from LxCore.preset.prod import assetPr, scenePr

from LxUi.qt import qtWidgets_, qtWidgets, qtCore

from LxInterface.qt.qtIfBasic import _qtIfAbcWidget

from LxDatabase import dbGet

from LxMaya.command import maUtils, maDir

from LxMaya.product.data import datScene

from LxMaya.interface.ifCommands import maUtilsTreeViewCmds

from LxMaya.interface.ifWidgets import ifMaAnimToolUnit

from LxMaya.product import maScLoadCmds, maScUploadCmds
# Project Data
currentProjectName = prsMethods.Project.mayaActiveName()
#
none = ''


#
class IfScLightLinkToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    projectName = currentProjectName
    # Utilities Tool
    dicScLightUtilsTool = bscMtdCore.orderedDict()
    dicScLightUtilsTool['sceneAssetManager'] = [0, 0, 0, 1, 4, 'Scene Compose', 'svg_basic@svg#subWindow']
    def __init__(self, *args, **kwargs):
        super(IfScLightLinkToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnit()
        #
        self.setScLightUtilsToolUiBox()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        pass
    #
    def setScLightUtilsToolUiBox(self):
        toolBox = self.scLightUtilsToolUiBox
        inData = self.dicScLightUtilsTool
        #
        self.sceneAssetManagerButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'sceneAssetManager', self.sceneAssetManagerButton)
        self.sceneAssetManagerButton.clicked.connect(self.setOpenScAstManager)
    #
    def setOpenScAstManager(self):
        pass
    #
    def setupUnit(self):
        self.scLightUtilsToolUiBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self.scLightUtilsToolUiBox)
        self.scLightUtilsToolUiBox.setTitle('Scene ( Light ) Utilities')


#
class IfScMayaComposeToolUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    projectName = currentProjectName
    #
    UnitTitle = 'Scene Maya Compose Manager'
    panelWidth = 800
    panelHeight = 800
    #
    UnitScriptJobWindowName = 'scConstantWindow'
    #
    widthSet = 400
    w = 100
    #
    dicScAstLoad = {
        0: 'Camera Unit(s)',
        'scLoadCameraUnit': [0, 1, 0, 1, 4, 'Load Camera Unit(s)', 'svg_basic@svg#load'],
        2: 'Asset Unit(s)',
        'scLoadAssetUnit': [0, 3, 0, 1, 4, 'Load Asset Unit(s)', 'svg_basic@svg#load'],
    }
    #
    dicScAstUpdate = {
        0: 'Cache Config(s)',
        'scUpdateIgnoreNonExists': [0, 1, 0, 1, 2, 'Ignore Non - Exists ( Server )'], 'scUpdateIgnoreNonAnimation': [0, 1, 2, 1, 2, 'Ignore Non - Animation'],
        'scUpdateIgnoreUnload': [0, 2, 0, 1, 2, 'Ignore Unload'],
        3: 'Camera Cache(s)',
        'scUpdateCameraCache': [0, 4, 0, 1, 4, 'Update Camera Cache(s)', 'svg_basic@svg#timeRefresh'],
        5: 'Asset Cache(s)',
        'scUpdateAstModelCache': [0, 6, 0, 1, 2, 'Update Model Cache(s)', 'svg_basic@svg#timeRefresh'], 'scUpdateAstExtraCache': [0, 6, 2, 1, 2, 'Update Extra Cache(s)', 'svg_basic@svg#timeRefresh'],
        'scUpdateAstCfxFurCache': [0, 7, 0, 1, 4, 'Update Groom Fur Cache(s)', 'svg_basic@svg#timeRefresh'],
    }
    def __init__(self, *args, **kwargs):
        super(IfScMayaComposeToolUnit, self).__init__(*args, **kwargs)
        self._initIfAbcUnit()
        #
        self._initUnitVar()
        #
        self.setupUnit()
        #
        self.setTreeViewBox()
    #
    def _initUnitVar(self):
        self._scCameraUnitItemLis = []
        self._scCameraCacheItemLis = []
        #
        self._scAssetUnitItemLis = []
        #
        self._scAstModelProductItemLis = []
        self._scAstModelCacheItemLis = []
        self._scAstExtraCacheItemLis = []
        #
        self._scAstCfxProductItemLis = []
        self._scAstCfxFurCacheItemLis = []
        #
        self._scAstCfxSolverProductItemLis = []
        self._scAstSolverCacheItemLis = []
        # Load
        self._scNeedLoadCameraUnitItemLis = []
        self._scNeedLoadAssetUnitItemLis = []
        # Update
        self._scNeedUpdateCameraCacheItemLis = []
        #
        self._scNeedUpdateAstModelCacheItemLis = []
        self._scNeedUpdateAstExtraCacheItemLis = []
        #
        self._scNeedUpdateAstCfxFurCacheItemLis = []
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        if self._connectObject:
            self.setListSceneCompose()
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methods = []
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setTreeViewBox(self):
        def setNodeSelCmd():
            selPath = treeBox.selectedItemPaths()
            #
            maUtils.setNodeSelect(selPath, noExpand=1)
        #
        def setActionData():
            actions = [
                ('Basic', ),
                ('Refresh', 'svg_basic@svg#refresh', True, self.setListSceneCompose),
                ('Extend', ),
                ('Select All', 'svg_basic@svg#checkedAll', True, treeBox.selectAll),
                ('Select Clear', 'svg_basic@svg#uncheckedAll', True, treeBox.clearSelection),
            ]
            treeBox.setActionData(actions)
        #
        treeBox = self.treeViewBox
        #
        maxWidth = self.widthSet * 2
        treeBox.setColumns(
            ['Asset', 'Frame Range', 'Local', 'Server'], [3, 1, 1, 1], maxWidth
        )
        #
        treeBox.itemSelectionChanged.connect(setNodeSelCmd)
        #
        setActionData()
    #
    def setupScLoadToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScAstLoad)
        #
        self._scLoadCameraUnitButton = qtWidgets.QtPressbutton()
        self._scLoadCameraUnitButton.setPercentEnable(True)
        toolBox.addButton('scLoadCameraUnit', self._scLoadCameraUnitButton)
        self._scLoadCameraUnitButton.setTooltip(
            u'''点击 加载 相机'''
        )
        #
        self._scLoadAssetUnitButton = qtWidgets.QtPressbutton()
        self._scLoadAssetUnitButton.setPercentEnable(True)
        toolBox.addButton('scLoadAssetUnit', self._scLoadAssetUnitButton)
        self._scLoadAssetUnitButton.clicked.connect(self._scAssetUnitUpdateCmd)
        self._scLoadAssetUnitButton.setTooltip(
            u'''点击 加载 资产'''
        )
        #
        toolBox.addSeparators()
    #
    def setupScUpdateToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicScAstUpdate)
        #
        self._scUpdateIgnoreNonExistsCheckbutton = qtWidgets.QtCheckbutton()
        toolBox.addButton('scUpdateIgnoreNonExists', self._scUpdateIgnoreNonExistsCheckbutton)
        self._scUpdateIgnoreNonExistsCheckbutton.setChecked(True)
        self._scUpdateIgnoreNonExistsCheckbutton.setTooltip(
            u'''启用 / 关闭 忽略 不存在的 缓存（Server）：\n1，启用此选项将会忽略该项检查。'''
        )
        self._scUpdateIgnoreNonExistsCheckbutton.clicked.connect(self.refreshMethod)
        #
        self._scUpdateIgnoreNonAnimationCheckbutton = qtWidgets.QtCheckbutton()
        toolBox.addButton('scUpdateIgnoreNonAnimation', self._scUpdateIgnoreNonAnimationCheckbutton)
        self._scUpdateIgnoreNonAnimationCheckbutton.setChecked(True)
        self._scUpdateIgnoreNonAnimationCheckbutton.setTooltip(
            u'''启用 / 关闭 忽略 无动画的 缓存（Maya Local）：\n1，启用此选项将会忽略该项检查。'''
        )
        self._scUpdateIgnoreNonAnimationCheckbutton.clicked.connect(self.refreshMethod)
        #
        self._scUpdateIgnoreUnloadCheckbutton = qtWidgets.QtCheckbutton()
        toolBox.addButton('scUpdateIgnoreUnload', self._scUpdateIgnoreUnloadCheckbutton)
        self._scUpdateIgnoreUnloadCheckbutton.setTooltip(
            u'''启用 / 关闭 忽略 未加载的 缓存（Maya Local）：\n1，启用此选项将会忽略该项检查。'''
        )
        self._scUpdateIgnoreUnloadCheckbutton.clicked.connect(self.refreshMethod)
        # Camera Cache
        self._scUpdateCameraCacheButton = qtWidgets.QtPressbutton()
        self._scUpdateCameraCacheButton.setPercentEnable(True)
        toolBox.addButton('scUpdateCameraCache', self._scUpdateCameraCacheButton)
        self._scUpdateCameraCacheButton.setTooltip(
            u'''点击 更新 相机 缓存：\n1，更新前请确认依赖的“Tree Item”已经被载入。'''
        )
        self._scUpdateCameraCacheButton.clicked.connect(self._scCameraCacheUpdateCmd)
        # Model Cache
        self._scUpdateAstModelCacheButton = qtWidgets.QtPressbutton()
        self._scUpdateAstModelCacheButton.setPercentEnable(True)
        toolBox.addButton('scUpdateAstModelCache', self._scUpdateAstModelCacheButton)
        self._scUpdateAstModelCacheButton.setTooltip(
            u'''点击 更新 模型 缓存：\n1，更新前请确认依赖的“Tree Item”已经被载入。'''
        )
        self._scUpdateAstModelCacheButton.clicked.connect(self._scAstModelCacheUpdateCmd)
        # Cfx Fur Cache(s)
        self._scUpdateAstCfxCacheButton = qtWidgets.QtPressbutton()
        self._scUpdateAstCfxCacheButton.setPercentEnable(True)
        toolBox.addButton('scUpdateAstCfxFurCache', self._scUpdateAstCfxCacheButton)
        self._scUpdateAstCfxCacheButton.setTooltip(
            u'''点击 更新 角色特效 缓存：\n1，更新前请确认依赖的“Tree Item”已经被载入。'''
        )
        self._scUpdateAstCfxCacheButton.clicked.connect(self._scAstCfxFurCacheUpdateCmd)
        # Extra Cache
        self._updateScAstExtraCacheButton = qtWidgets.QtPressbutton()
        self._updateScAstExtraCacheButton.setPercentEnable(True)
        toolBox.addButton('scUpdateAstExtraCache', self._updateScAstExtraCacheButton)
        self._updateScAstExtraCacheButton.setTooltip(
            u'''点击 更新 扩展 缓存：\n1，更新前请确认依赖的“Tree Item”已经被载入。'''
        )
        self._updateScAstExtraCacheButton.clicked.connect(self._scAstExtraCacheUpdateCmd)
        #
        toolBox.addSeparators()
    #
    def setListSceneCompose(self):
        treeBox = self.treeViewBox
        projectName = self._connectObject.projectName
        sceneStage = self._connectObject.sceneStage
        #
        connectMethods = [
            self._scUnitLoadCheckMethod, self._scCacheUpdateCheckMethod
        ]
        [
            (
                self._scCameraUnitItemLis,
                (
                    self._scCameraCacheItemLis
                )
            ),
            (
                self._scAssetUnitItemLis,
                (
                    self._scAstModelProductItemLis, self._scAstModelCacheItemLis, self._scAstExtraCacheItemLis,
                    self._scAstCfxProductItemLis, self._scAstCfxFurCacheItemLis,
                    self._scAstCfxSolverProductItemLis, self._scAstSolverCacheItemLis
                )
            )
        ] = maUtilsTreeViewCmds.setListScMayaComposeCmdMain(
            projectName,
            sceneStage,
            treeBox,
            connectMethods
        )
        #
        self._scUnitLoadCheckMethod()
        self._scCacheUpdateCheckMethod()
    #
    def _scUnitLoadCheckMethod(self):
        def _cacheCheckBranch(button, treeItemLis, needUpdateItemLis):
            def _updateNeedUpdateSubBranch(treeItem):
                serverTimeTag, localTimeTag = treeItem.serverTimeTag, treeItem.localTimeTag
                if localTimeTag is None:
                    needUpdateItemLis.append(treeItem)
                else:
                    correctLis.append(True)
            #
            correctLis = []
            #
            if treeItemLis:
                for i in treeItemLis:
                    _updateNeedUpdateSubBranch(i)
            #
            maxCount = len(treeItemLis)
            correctCount = len(correctLis)
            button.setPercent(maxCount, correctCount)
        #
        def setMain():
            for button, treeItemLis, needUpdateItemLis in checkArgLis:
                [needUpdateItemLis.remove(i) for i in needUpdateItemLis]
                _cacheCheckBranch(button, treeItemLis, needUpdateItemLis)
        #
        checkArgLis = [
            (self._scLoadCameraUnitButton, self._scCameraUnitItemLis, self._scNeedLoadCameraUnitItemLis),
            (self._scLoadAssetUnitButton, self._scAssetUnitItemLis, self._scNeedLoadAssetUnitItemLis)
        ]
        #
        setMain()
    #
    def _scCacheUpdateCheckMethod(self):
        def _cacheCheckBranch(button, treeItemLis, needUpdateItemLis):
            def _updateNeedUpdateSubBranch(treeItem):
                serverTimeTag, localTimeTag = treeItem.serverTimeTag, treeItem.localTimeTag
                #
                if serverTimeTag is None:
                    if isIgnoreNonExists is True:
                        correctLis.append(True)
                else:
                    if localTimeTag is None:
                        if isIgnoreUnload is True:
                            correctLis.append(True)
                        else:
                            needUpdateItemLis.append(treeItem)
                    elif localTimeTag is False:
                        if isIgnoreAnimation is True:
                            correctLis.append(True)
                        else:
                            needUpdateItemLis.append(treeItem)
                    else:
                        if localTimeTag == serverTimeTag:
                            correctLis.append(True)
                        else:
                            needUpdateItemLis.append(treeItem)
            #
            correctLis = []
            #
            if treeItemLis:
                for i in treeItemLis:
                    _updateNeedUpdateSubBranch(i)
            #
            maxCount = len(treeItemLis)
            correctCount = len(correctLis)
            button.setPercent(maxCount, correctCount)
        #
        def setMain():
            for button, treeItemLis, needUpdateItemLis in checkArgLis:
                [needUpdateItemLis.remove(i) for i in needUpdateItemLis]
                _cacheCheckBranch(button, treeItemLis, needUpdateItemLis)
        #
        isIgnoreNonExists = self._scUpdateIgnoreNonExistsCheckbutton.isChecked()
        isIgnoreAnimation = self._scUpdateIgnoreNonAnimationCheckbutton.isChecked()
        isIgnoreUnload = self._scUpdateIgnoreUnloadCheckbutton.isChecked()
        #
        checkArgLis = [
            (self._scUpdateCameraCacheButton, self._scCameraCacheItemLis, self._scNeedUpdateCameraCacheItemLis),
            #
            (self._scUpdateAstModelCacheButton, self._scAstModelCacheItemLis, self._scNeedUpdateAstModelCacheItemLis),
            (self._updateScAstExtraCacheButton, self._scAstExtraCacheItemLis, self._scNeedUpdateAstExtraCacheItemLis),
            (self._scUpdateAstCfxCacheButton, self._scAstCfxFurCacheItemLis, self._scNeedUpdateAstCfxFurCacheItemLis),
        ]
        #
        setMain()
    #
    def _scAssetUnitUpdateCmd(self):
        treeItemLis = self._scNeedLoadAssetUnitItemLis
        if treeItemLis:
            for treeItem in treeItemLis:
                _vars = treeItem.vars
                if _vars is not None:
                    (
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex, assetCategory, assetName, number, assetVariant
                    ) = _vars
                    #
                    maScLoadCmds.scUnitAssetLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex, assetCategory, assetName, number, assetVariant,
                        withAstModel=True, withModelCache=True,
                        withAstCfx=True, withAstCfxFurCache=True,
                        withExtraCache=True
                    )
            #
            self.refreshMethod()
    # Camera Cache
    def _scCameraCacheUpdateCmd(self):
        treeItemLis = self._scNeedUpdateCameraCacheItemLis
        if treeItemLis:
            for treeItem in treeItemLis:
                _vars = treeItem.vars
                if _vars is not None:
                    (
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        subLabelString
                    ) = _vars
                    #
                    maScLoadCmds.scUnitCameraCacheLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage, subLabelString,
                        withCameraCache=True
                    )
            #
            self.refreshMethod()
    # Asset Cache
    def _scAstModelCacheUpdateCmd(self):
        treeItemLis = self._scNeedUpdateAstModelCacheItemLis
        if treeItemLis:
            for treeItem in treeItemLis:
                _vars = treeItem.vars
                if _vars is not None:
                    (
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex, assetCategory, assetName, number, assetVariant
                    ) = _vars
                    #
                    maScLoadCmds.scUnitAstModelCacheConnectCmd(
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex,
                        assetCategory, assetName, number, assetVariant,
                        withModelCache=True
                    )
            #
            self.refreshMethod()
    #
    def _scAstExtraCacheUpdateCmd(self):
        treeItemLis = self._scNeedUpdateAstExtraCacheItemLis
        if treeItemLis:
            for treeItem in treeItemLis:
                _vars = treeItem.vars
                if _vars is not None:
                    (
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex, assetCategory, assetName, number, assetVariant
                    ) = _vars
                    #
                    maScLoadCmds.scUnitAstExtraCacheConnectCmd(
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex,
                        assetCategory, assetName, number, assetVariant,
                        withAstRigExtraCache=True
                    )
            #
            self.refreshMethod()
    #
    def _scAstCfxFurCacheUpdateCmd(self):
        treeItemLis = self._scNeedUpdateAstCfxFurCacheItemLis
        if treeItemLis:
            for treeItem in treeItemLis:
                _vars = treeItem.vars
                if _vars is not None:
                    (
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex, assetCategory, assetName, number, assetVariant,
                        furObject
                    ) = _vars
                    #
                    maScLoadCmds.scUnitAstCfxFurCacheConnectSubCmd(
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame,
                        assetIndex,
                        assetCategory, assetName, number, assetVariant,
                        furObject,
                        withAstCfxFurCache=True
                    )
            #
            self.refreshMethod()
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        layout = qtCore.QVBoxLayout_(widget)
        #
        self.treeViewBox = qtWidgets_.QTreeWidget_()
        layout.addWidget(self.treeViewBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Load')
        #
        self.setupScLoadToolUiBox(toolBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Update')
        #
        self.setupScUpdateToolUiBox(toolBox)


#
class IfScOsComposeToolUnit(_qtIfAbcWidget.QtIfAbc_Unit):
    projectName = currentProjectName
    #
    UnitTitle = 'Scene Os Compose Manager'
    UnitWidth = 800
    UnitHeight = 800
    #
    UnitScriptJobWindowName = 'scFileManagerWindow'
    #
    widthSet = 400
    w = 100
    dicModifyTool = dict(
        ignoreProject=[0, 0, 0, 1, 2, 'Ignore Project Root'],
        collectionFile=[0, 1, 0, 1, 4, 'Collection File(s)', 'svg_basic@svg#info']
    )
    def __init__(self, *args, **kwargs):
        super(IfScOsComposeToolUnit, self).__init__(*args, **kwargs)
        self._initIfAbcUnit()
        #
        self.initUnit()
        #
        self.setupUnit()
        #
        self.setTreeViewBox()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        if self._connectObject:
            self.setListFile()
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methods = []
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setTreeViewBox(self):
        def setSelNode():
            selectedItems = treeBox.selectedItems()
            if selectedItems:
                nodeArray = []
                for treeItem in selectedItems:
                    if hasattr(treeItem, 'nodes'):
                        nodes = treeItem.nodes
                        for node in nodes:
                            if not ' - ' in node:
                                nodeArray.append(node)
                            if ' - ' in node:
                                nodeArray.append(node.split(' - ')[0])
                #
                maUtils.setNodeSelect(nodeArray)
        #
        treeBox = self.treeViewBox
        #
        maxWidth = self.widthSet * 2
        #
        treeBox.setColumns(
            ['File', 'Type'], [3, 1], maxWidth
        )
        #
        treeBox.itemSelectionChanged.connect(setSelNode)
    #
    def setupModifyToolUiBox(self, toolBox):
        inData = self.dicModifyTool
        #
        self._ignoreProjectButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'ignoreProject', self._ignoreProjectButton)
        self._ignoreProjectButton.clicked.connect(self.setListFile)
        #
        self._scOsFileCollectionButton = qtWidgets.QtPressbutton()
        self._scOsFileCollectionButton.setPercentEnable(True)
        toolBox.setButton(inData, 'collectionFile', self._scOsFileCollectionButton)
        self._scOsFileCollectionButton.clicked.connect(self.setCollectionFile)
    #
    def setListFile(self):
        def getPathFilterRoot(filterPaths):
            lis = []
            if projectServerRootPathLis:
                for rootPath in projectServerRootPathLis:
                    rootPath = rootPath.lower()
                    for i in filterPaths:
                        if not i.startswith(rootPath):
                            lis.append(i)
            return lis
        #
        self._scOsFileItemLis = []
        self._scNeedCollectionFileItemLis = []
        self._scNeedRepathFileItemLis = []
        #
        self.collectionDic = {}
        #
        projectName = self._connectObject.projectName
        sceneStage = self._connectObject.sceneStage
        #
        pathsep = appCfg.OsFilePathSep
        #
        treeBox = self.treeViewBox
        #
        isWithTexture = True
        isWithMap = True
        #
        isWithReference = True
        isWithAssemblyReference = True
        #
        isWithVolumeCache = True
        isWithProxyCache = True
        #
        isWithGpuCache = True
        isWithAlembicCache = True
        #
        isWithFurCache = True
        isWithGeomCache = True
        #
        isIgnoreProject = self._ignoreProjectButton.isChecked()
        #
        osPaths, osFileDic = maDir.getDirData(
            withTexture=isWithTexture,
            withFurMap=isWithMap,
            withReference=isWithReference,
            withAssemblyReference=isWithAssemblyReference,
            withProxyCache=isWithProxyCache,
            withVolumeCache=isWithVolumeCache,
            withGpuCache=isWithGpuCache,
            withAlembicCache=isWithAlembicCache,
            withFurCache=isWithFurCache,
            withGeomCache=isWithGeomCache
        )
        projectServerRootPathLis = prsMethods.Project.serverRoots(projectName)
        projectLocalRootPathLis = prsMethods.Project.localRoots(projectName)
        #
        if isIgnoreProject:
            osPaths = getPathFilterRoot(osPaths)
        #
        osPathsArray = treeBox.getGraphPaths(osPaths, pathsep)
        #
        maUtilsTreeViewCmds.setListFile(
            treeBox,
            osPathsArray,
            osFileDic,
            filterServerRootPathLis=projectServerRootPathLis,
            filterLocalRootPathLis=projectLocalRootPathLis,
            fileItemLis=self._scOsFileItemLis,
            needCollectionFileItemLis=self._scNeedCollectionFileItemLis,
            needRepathFileItemLis=self._scNeedRepathFileItemLis,
            expandedDic=None, connectMethod=None
        )
        #
        self.setCollectionBtnState()
    #
    def setCollectionBtnState(self):
        button = self._scOsFileCollectionButton
        #
        maxCount = len(self._scOsFileItemLis)*2
        errorCount = len(self._scNeedCollectionFileItemLis) + len(self._scNeedRepathFileItemLis)
        #
        button.setPercent(maxCount, maxCount - errorCount)
    #
    def getCollectionDataLis(self):
        def getSceneFile(sourceFileString):
            targetFileString = bscMethods.OsPath.composeBy(sceneDirectory, bscMethods.OsFile.basename(sourceFileString))
            return targetFileString
        #
        def getServerFile(sourceFileString, localRoot):
            targetFileString = None
            for i in projectServerRootPathLis:
                guessFile = i + sourceFileString[len(localRoot):]
                if bscMethods.OsMultifile.existFiles(guessFile):
                    targetFileString = guessFile
                    break
            if targetFileString is None:
                targetFileString = bscMethods.OsPath.composeBy(sceneDirectory, bscMethods.OsFile.basename(sourceFileString))
            return targetFileString
        #
        def getOsFileCollectionDataLis(treeItemLis):
            if treeItemLis:
                for treeItem in treeItemLis:
                    osFileCollectionDataLis = []
                    #
                    fileType = treeItem.type
                    nodes = treeItem.nodes
                    sourceFile = treeItem.path
                    #
                    targetFile = getSceneFile(sourceFile)
                    osFileCollectionDataLis.append((sourceFile, targetFile))
                    #

                    existsSourceOsFileLis = bscMethods.OsMultifile.existFiles(sourceFile)
                    if existsSourceOsFileLis:
                        for subSourceFile in existsSourceOsFileLis:
                            subTargetFile = getSceneFile(subSourceFile)
                            osFileCollectionDataLis.append((subSourceFile, subTargetFile))
                    #
                    lis.append((fileType, nodes, osFileCollectionDataLis))
        #
        def getOsFileRepathDataLis(treeItemLis):
            if treeItemLis:
                for treeItem in treeItemLis:
                    osFileCollectionDataLis = []
                    #
                    fileType = treeItem.type
                    nodes = treeItem.nodes
                    sourceFile = treeItem.path
                    localRoot = treeItem.localRoot
                    #
                    targetFile = getServerFile(sourceFile, localRoot)
                    osFileCollectionDataLis.append((sourceFile, targetFile))
                    #
                    existsSourceOsFileLis = bscMethods.OsMultifile.existFiles(sourceFile)
                    if existsSourceOsFileLis:
                        for subSourceFile in existsSourceOsFileLis:
                            subTargetFile = getServerFile(subSourceFile, localRoot)
                            osFileCollectionDataLis.append((subSourceFile, subTargetFile))
                    #
                    lis.append((fileType, nodes, osFileCollectionDataLis))
        #
        lis = []
        #
        projectName = self._connectObject.projectName
        sceneCategory = self._connectObject.sceneCategory
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        #
        sceneDirectory = scenePr.sceneExtraFolder(
            prsConfigure.Utility.DEF_value_root_server,
            projectName, sceneCategory, sceneName, sceneVariant, sceneStage
        )
        projectServerRootPathLis = prsMethods.Project.serverRoots(projectName)
        getOsFileCollectionDataLis(self._scNeedCollectionFileItemLis)
        getOsFileRepathDataLis(self._scNeedRepathFileItemLis)
        #
        return lis
    #
    def setCollectionFile(self):
        collectionDataLis = self.getCollectionDataLis()
        if collectionDataLis:
            maDir.setDirectoryModifyCmd(
                collectionDataLis,
                isCollection=True,
                isIgnoreExists=True, isIgnoreTimeChanged=False,
                isWithTx=True,
                isAutoCache=False,
                isRepath=True
            )
            # Refresh
            self.setListFile()
    #
    def initUnit(self):
        self._scOsFileItemLis = []
        self._scNeedCollectionFileItemLis = []
        self._scNeedRepathFileItemLis = []
        #
        self.collectionDic = {}
    #
    def setupUnit(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        layout = qtCore.QVBoxLayout_(widget)
        #
        self.treeViewBox = qtWidgets_.QTreeWidget_()
        layout.addWidget(self.treeViewBox)
        #
        toolBox = qtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Modify')
        self.setupModifyToolUiBox(toolBox)


#
class IfScAssetToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    def __init__(self, *args, **kwargs):
        super(IfScAssetToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._inspectAssetDatumLis = []
        #
        self.initUi()
        self.setupUi()
    #
    def setConnectObject(self, method):
        self._connectObject = method
        if self._connectObject:
            sceneStage = self._connectObject.sceneStage
            if scenePr.isLayoutLinkName(sceneStage) or scenePr.isAnimationLinkName(sceneStage):
                self._isWithScAstModelCache = True
                self._isWithScAstSolverCache = True
                self._isWithScAstExtraCache = True
                #
                self._isWithScAstModelCacheEnable = True
                self._isWithScAstSolverCacheEnable = True
                self._isWithScAstExtraCacheEnable = True
            elif scenePr.isSimulationLinkName(sceneStage):
                self._isWithScAstModelCache = True
                self._isWithScAstSolverCache = False
                self._isWithScAstExtraCache = False
                #
                self._isWithScAstModelCacheEnable = True
                self._isWithScAstSolverCacheEnable = False
                self._isWithScAstExtraCacheEnable = False
            elif scenePr.isSolverLinkName(sceneStage):
                self._isWithScAstModelCache = False
                self._isWithScAstSolverCache = False
                self._isWithScAstExtraCache = False
                #
                self._isWithScAstModelCacheEnable = False
                self._isWithScAstSolverCacheEnable = False
                self._isWithScAstExtraCacheEnable = False
            elif scenePr.isLightLinkName(sceneStage):
                self._isWithScAstModelCache = False
                self._isWithScAstSolverCache = False
                self._isWithScAstExtraCache = False
                #
                self._isWithScAstModelCacheEnable = False
                self._isWithScAstSolverCacheEnable = False
                self._isWithScAstExtraCacheEnable = False
    #
    def refreshMethod(self):
        if self._connectObject:
            self.setListAsset()
            #
            lis = []
            if self._inspectAssetDatumLis:
                for i in self._inspectAssetDatumLis:
                    lis.append(i[1:])
            #
            self._connectObject._inspectAssetDatumLis = lis
    #
    def setListAsset(self):
        def setBranch(key, value, assetNumberKeys):
            keyNode = key
            #
            assetIndex, assetCategory, assetName, number, assetVariant = value
            #
            gridItem = qtWidgets.QtGridviewItem()
            listBox.addItem(gridItem)
            #
            showExplain = assetPr.getAssetViewInfo(assetIndex, assetCategory, number)
            gridItem.setName(showExplain)
            gridItem.setIcon('svg_basic@svg#package')
            #
            preview = dbGet.getDbAstPreviewFile(assetIndex, assetVariant)
            #
            astModelSectorChart = qtWidgets.QtSectorchart()
            astModelSectorChart.setImage(preview)
            #
            if maUtils._getNodeCategoryString(keyNode) == 'reference':
                namespace = maUtils.getReferenceNamespace(keyNode)
            else:
                namespace = maUtils._toNamespaceByNodePath(keyNode)
            #
            constantData = datScene.getScAstModelMeshConstantData(
                sceneName, sceneVariant, sceneStage,
                assetIndex,
                assetCategory, assetName, number, namespace
            )
            geometryCheck = True
            numberCheck = True
            if constantData:
                totalArray, pathChangedArray, geoChangedArray, geoShapeChangedArray, mapChangedArray, mapShapeChangedArray = constantData
                totalCount = len(totalArray)
                pathChangedCount = 0
                geomChangedCount = 0
                geoShapeChangedCount = 0
                mapChangedCount = 0
                mapShapeChangedCount = 0
                #
                if totalCount:
                    pathChangedCount = len(pathChangedArray)
                    geomChangedCount = len(geoChangedArray)
                    geoShapeChangedCount = len(geoShapeChangedArray)
                    mapChangedCount = len(mapChangedArray)
                    mapShapeChangedCount = len(mapShapeChangedArray)
                #
                if pathChangedCount != 0 or geomChangedCount != 0:
                    geometryCheck = False
                #
                data = [
                    ('Obj - Path', totalCount, totalCount - pathChangedCount),
                    ('Geom - Topo', totalCount, totalCount - geomChangedCount),
                    ('Geom - Shape', totalCount, totalCount - geoShapeChangedCount),
                    ('Map - Topo', totalCount, totalCount - mapChangedCount),
                    ('Map - Shape', totalCount, totalCount - mapShapeChangedCount)
                ]
                astModelSectorChart.setChartDatum(data)
            #os.evrion
            assetNumberKey = '{} - {}'.format(assetName, number)
            if assetNumberKey in assetNumberKeys:
                numberCheck = False
            #
            if geometryCheck is False or numberCheck is False:
                gridItem._setQtPressStatus(qtCore.ErrorStatus)
                # gridItem.setSelectable(False)
            elif geometryCheck is True and numberCheck is True:
                gridItem._setQtPressStatus(qtCore.OnStatus)
                # gridItem.setSelectable(True)
            assetNumberKeys.append(assetNumberKey)
            #
            self._inspectAssetDatumLis.append((
                gridItem,
                assetCategory, assetName, number, assetVariant,
                keyNode
            ))
            #
            gridItem.addWidget(astModelSectorChart, 0, 1, 1, 1)
        #
        def setActionData():
            def isScUploadAstCacheEnable():
                if scenePr.isLayoutLinkName(sceneStage) or scenePr.isAnimationLinkName(sceneStage) or scenePr.isSimulationLinkName(sceneStage):
                    boolean = True
                else:
                    boolean = False
                return boolean
            #
            def isScAstModelCacheEnable():
                if self._isWithScAstModelCacheEnable:
                    return self._isWithScAstModelCache
                else:
                    return None
            #
            def isScAstSolverCacheEnable():
                if self._isWithScAstSolverCacheEnable:
                    return self._isWithScAstSolverCache
                else:
                    return None
            #
            def isScAstRigExtendCacheEnable():
                if self._isWithScAstExtraCacheEnable:
                    return self._isWithScAstExtraCache
                else:
                    return None
            #
            def setScAstModelCacheEnableCmd():
                self._isWithScAstModelCache = not self._isWithScAstModelCache
            #
            def setScAstSolverCacheEnableCmd():
                if self._isWithScAstSolverCacheEnable:
                    self._isWithScAstSolverCache = not self._isWithScAstSolverCache
            #
            def setScAstRigExtendCacheEnableCmd():
                if self._isWithScAstExtraCacheEnable:
                    self._isWithScAstExtraCache = not self._isWithScAstExtraCache
            #
            def isScAstCacheUseForSolverEnable():
                if isScUploadAstCacheEnable():
                    return self._isScAstModelCacheUseForSolver
                else:
                    return False
            #
            def setScAstCacheUseForSolverEnableCmd():
                self._isScAstModelCacheUseForSolver = not self._isScAstModelCacheUseForSolver
            #
            def scAssetCacheUploadCmd():
                assetData = []
                if self._inspectAssetDatumLis:
                    for i in self._inspectAssetDatumLis:
                        if i[0].isChecked():
                            assetData.append(i[1:])
                #
                if assetData:
                    timeTag = bscMethods.OsTimetag.active()
                    description = u'镜头 - 资产（模型缓存）上传/更新'
                    notes = self._connectObject._scNoteUiLabel.datum()
                    #
                    assetConfig = (self._isWithScAstModelCache, self._isWithScAstSolverCache, self._isWithScAstExtraCache), self._isScAstModelCacheUseForSolver
                    withAsset = assetData, assetConfig
                    maScUploadCmds.scUnitAssetsUploadMainCmd_(
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        startFrame, endFrame, frameOffset,
                        timeTag,
                        description, notes,
                        withAsset
                    )
                    #
                    bscObjects.MessageWindow('Scene Asset Cache Upload', 'Complete')
            #
            def setRigLoadWindowShowCmd():
                IfToolWindow = qtWidgets.QtToolWindow(self)
                toolBox = ifMaAnimToolUnit.IfScRigLoadedUnit()
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
            listBox.setActionData(
                [
                    ('Window',),
                    ('Rig Load Window', 'svg_basic@svg#subWindow', True, setRigLoadWindowShowCmd),
                    ('Animation / Simulation Config',),
                    ('Model Cache', 'checkBox', isScAstModelCacheEnable, setScAstModelCacheEnableCmd),
                    ('Solver Cache', 'checkBox', isScAstSolverCacheEnable, setScAstSolverCacheEnableCmd),
                    ('Extra Cache', 'checkBox', isScAstRigExtendCacheEnable, setScAstRigExtendCacheEnableCmd),
                    ('Solver Config',),
                    ('Model Cache Use for Solver', 'checkBox', isScAstCacheUseForSolverEnable, setScAstCacheUseForSolverEnableCmd),
                    ('Action', ),
                    ('Upload Asset Cache', ('svg_basic@svg#file', 'svg_basic@svg#upload_action'), isScUploadAstCacheEnable, scAssetCacheUploadCmd)

                ]
            )
        #
        def setMain():
            inData = None
            if scenePr.isLayoutLinkName(sceneStage) or scenePr.isAnimationLinkName(sceneStage):
                inData = datScene.getScAnimAssetRefDic()
            elif scenePr.isSimulationLinkName(sceneStage) or scenePr.isSolverLinkName(sceneStage) or scenePr.isLightLinkName(sceneStage):
                inData = datScene.getScAstUnitDic(
                    projectName,
                    sceneCategory, sceneName, sceneVariant, sceneStage
                )
            #
            listBox.cleanItems()
            if inData:
                assetNumberKeys = []
                # View Progress
                progressExplain = '''Load Asset Unit(s)'''
                maxValue = len(inData)
                progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
                for k, v in inData.items():
                    progressBar.update()
                    setBranch(k, v, assetNumberKeys)
            #
            listBox.setRefresh()
        #
        self._inspectAssetDatumLis = []
        #
        sceneIndex = self._connectObject.sceneIndex
        #
        projectName = self._connectObject.projectName
        sceneCategory = self._connectObject.sceneCategory
        sceneName = self._connectObject.sceneName
        sceneVariant = self._connectObject.sceneVariant
        sceneStage = self._connectObject.sceneStage
        #
        startFrame, endFrame = scenePr.getScUnitFrameRange(
            projectName, sceneCategory, sceneName, sceneVariant
        )
        #
        frameOffset = prsOutputs.Util.animKeyFrameOffset
        #
        listBox = self._scAstGridview
        #
        setMain()
        setActionData()
    #
    def initUi(self):
        self._isScAstModelCacheUseForSolver = False
        #
        self._isWithScAstModelCache = True
        self._isWithScAstSolverCache = True
        self._isWithScAstExtraCache = True
        #
        self._isWithScAstModelCacheEnable = True
        self._isWithScAstSolverCacheEnable = True
        self._isWithScAstExtraCacheEnable = True
        #
        self._uiItemWidth = 300
        self._uiItemHeight = 320
    #
    def setupUi(self):
        self._scAstGridview = qtWidgets.QtGridview()
        self.mainLayout().addWidget(self._scAstGridview)
        self._scAstGridview.setCheckEnable(True)
        #
        self._scAstGridview.setItemSize(self._uiItemWidth, self._uiItemHeight)
        self._scAstGridview.setItemListModeSize(self._uiItemWidth, 20)
