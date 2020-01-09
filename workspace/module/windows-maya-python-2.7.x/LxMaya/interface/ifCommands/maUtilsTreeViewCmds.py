# coding=utf-8
from LxBasic import bscMethods

from LxCore import lxBasic
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import scenePr
#
from LxUi.qt import qtWidgets_, qtWidgets
#
from LxMaya.interface.ifObjects import ifMaScTreeItem
#
from LxMaya.command import maUtils
#
from LxMaya.product.data import datScene
#
#
none = ''


#
def setLisObjects(treeBox, objectPaths, expandedDic):
    def branchView(treeItem):
        path = treeItem.path
        #
        objectType = maUtils.getShapeType(path)
        #
        treeItem.setItemMayaIcon(0, objectType)
        #
        treeItem.setText(0, maUtils._toNodeName(path, 1))
        treeItem.setText(1, maUtils.getNodeType(path))
    #
    if objectPaths:
        subObjectPaths = treeBox.getGraphPaths(objectPaths, appCfg.Ma_Separator_Node)
        hierDic = treeBox.getGraphDatumDic(subObjectPaths, appCfg.Ma_Separator_Node)
        if hierDic:
            treeBox.setupGraph(hierDic, branchView, expandedDic)


#
def setListNodes(treeBox, nodes):
    def setBranch(node):
        nodeName = maUtils._toNodeName(node, 1)
        nodeType = maUtils.getNodeType(node)
        #
        treeItem = qtWidgets_.QTreeWidgetItem_()
        treeBox.addItem(treeItem)
        #
        treeItem.setItemMayaIcon(0, nodeType)
        #
        treeItem.setText(0, nodeName)
        treeItem.setText(1, nodeType)
        #
        treeItem.name = nodeName
        treeItem.path = node
    #
    if nodes:
        [setBranch(i) for i in nodes]


#
def setListDirectory(
        treeBox,
        osPaths,
        osFileLinkDic,
        expandedDic=None,
        connectMethod=None
):
    # Sub Method
    def setBranchView(treeItem):
        def getFileDataArray(dirKey):
            lis = []
            if dirKey in osFileLinkDic:
                lis = osFileLinkDic[dirKey]
            return lis
        #
        def setEnabled():
            treeItems = [treeItem]
            treeItems.extend(treeItem.childItems())
            #
            boolean = checkBox.isChecked()
            childCheckBoxs = [treeBox.itemWidget(i, column) for i in treeItems]
            [childCheckBox.setChecked(boolean) for childCheckBox in childCheckBoxs]
            #
            if connectMethod:
                connectMethod()
        #
        def setActionData():
            def setOpenFolder():
                lxBasic.setOsFolderOpen(filePath)
            #
            openFolderEnabled = lxBasic.isOsExist(filePath)
            #
            actionExplain = 'Open Source Folder ( %s )' % folderName
            #
            branchActionData = [
                (actionExplain, 'svg_basic@svg#folder', openFolderEnabled, setOpenFolder)
            ]
            #
            treeItemWidget.setActionData(branchActionData)
        #
        iconLabel = 'svg_basic@svg#folder'
        stateLabel = none
        filePath = treeItem.path[1:]
        folderName = treeItem.name
        if ':' in folderName:
            iconLabel = 'svg_basic@svg#server_root'
        count = 0
        fileDataArray = getFileDataArray(filePath)
        #
        if fileDataArray:
            count = len(fileDataArray)
        #
        if not lxBasic.isOsExist(filePath):
            stateLabel = 'off'
        #
        parentItem = treeItem.parent()
        if parentItem:
            parentItem.setExpanded(True)
        #
        showExplain = '%s ( %s )' % (folderName, count)
        treeItemWidget = treeItem.setItemIconWidget(0, iconLabel, showExplain, stateLabel)
        setActionData()
        # Check Box
        checkBox = qtWidgets.QtCheckbutton()
        checkBox.setNameText('Enable')
        checkBox.setChecked(True)
        column = 1
        treeBox.setItemWidget(treeItem, column, checkBox)
        checkBox.clicked.connect(setEnabled)
        #
        treeItem.checkBox = checkBox
        #
        treeItem.setToolTip(0, filePath)
    #
    treeBox.clear()
    if osPaths:
        osPaths.sort()
        #
        pathsep = appCfg.OsFilePathSep
        #
        explain = '''Read File'''
        maxValue = len(osPaths)
        progressBar = bscMethods.If_Progress(explain, maxValue)
        #
        hierarchyData = treeBox.getGraphDatumDic(
            osPaths,
            pathsep=pathsep,
            progressBar=progressBar
        )
        #
        if hierarchyData:
            treeBox.setupGraph(hierarchyData, setBranchView, expandedDic)


#
def setListFile(
        treeBox,
        osPaths,
        osFileDic,
        fileItemLis=None,
        needCollectionFileItemLis=None,
        needRepathFileItemLis=None,
        filterServerRootPathLis=None,
        filterLocalRootPathLis=None,
        expandedDic=None,
        connectMethod=None
):
    # Sub Method
    def setBranchView(folderItem):
        def serverRootFilter(osPath, rootPaths):
            boolean = False
            rootPath = None
            if rootPaths:
                for p in rootPaths:
                    p = p.lower()
                    if osPath.startswith(p):
                        boolean = True
                        rootPath = p
                        break
            return boolean, rootPath
        #
        def localRootFilter(osPath, rootPaths):
            boolean = False
            rootPath = None
            if rootPaths:
                for p in rootPaths:
                    p = p.lower()
                    osPath = osPath.lower()
                    rootDrive = p.split('/')[0]
                    projectName = p.split('/')[-1]
                    if osPath.startswith(rootDrive) and '/' + projectName in osPath:
                        boolean = True
                        rootPath = osPath.split(projectName)[0] + projectName
                        break
            return boolean, rootPath
        #
        def getFileDataArray(dirKey):
            lis = []
            if dirKey in osFileDic:
                lis = osFileDic[dirKey]
            return lis
        #
        iconKeyword = 'svg_basic@svg#folder'
        stateLabel = none
        folderName = folderItem.name
        filePath = folderItem.path[1:]
        #
        if ':' in folderName:
            iconKeyword = 'svg_basic@svg#server_root'
        count = 0
        fileDataArray = getFileDataArray(filePath)
        #
        if not lxBasic.isOsExist(filePath):
            stateLabel = 'off'
        #
        if fileDataArray:
            isServerRoot, serverRoot = serverRootFilter(filePath, filterServerRootPathLis)
            isLocalRoot, localRoot = localRootFilter(filePath, filterLocalRootPathLis)
            #
            if isServerRoot:
                stateLabel = 'on'
            else:
                if isLocalRoot:
                    stateLabel = 'warning'
                else:
                    stateLabel = 'error'
            #
            count = len(fileDataArray)
            for fileData in fileDataArray:
                fileItem = setListFileBranch(
                    folderItem,
                    fileData
                )
                fileItem.localRoot = localRoot
                if isinstance(fileItemLis, list):
                    fileItemLis.append(fileItem)
                #
                if not isServerRoot:
                    if not isLocalRoot:
                        if isinstance(needCollectionFileItemLis, list):
                            needCollectionFileItemLis.append(fileItem)
                    else:
                        if isinstance(needRepathFileItemLis, list):
                            needRepathFileItemLis.append(fileItem)
        #
        parentItem = folderItem.parent()
        if parentItem:
            parentItem.setExpanded(True)
        #
        showExplain = '%s ( %s )' % (folderName, count)
        folderItem.setText(0, showExplain)
        folderItem.setItemIcon_(0, iconKeyword, stateLabel)
        #
        folderItem.setToolTip(0, filePath)
    #
    treeBox.clear()
    if osPaths:
        osPaths.sort()
        #
        pathsep = appCfg.OsFilePathSep
        #
        explain = '''Read File'''
        maxValue = len(osPaths)
        progressBar = bscMethods.If_Progress(explain, maxValue)
        #
        hierarchyData = treeBox.getGraphDatumDic(
            osPaths,
            pathsep=pathsep,
            progressBar=progressBar
        )
        #
        if hierarchyData:
            treeBox.setupGraph(hierarchyData, setBranchView, expandedDic)


#
def setListFileBranch(
        parentUi,
        fileData
):
    def setBranch(treeItem, parentItem, osFile, iconKeyword_, iconState, explain):
        if type(parentItem) == qtWidgets_.QTreeWidget_:
            parentItem.addItem(treeItem)
        elif type(parentItem) == qtWidgets_.QTreeWidgetItem_:
            parentItem.addChild(treeItem)
            #
            parentItem.setExpanded(True)
        #
        treeItem.path = osFile
        treeItem.name = fileName
        #
        treeItem.type = fileType
        treeItem.nodes = nodes
        #
        treeItem.setItemIcon_(0, iconKeyword_, iconState)
        treeItem.setText(0, explain)
        #
        treeItem.setText(1, fileType)
        #
        return treeItem
    #
    fileType, sourceFile, nodes = fileData
    #
    iconKeyword = 'svg_basic@svg#file'
    #
    state = none
    #
    fileName = lxBasic.getOsFileBasename(sourceFile)
    count = len(nodes)
    showExplain = '{0} ( {1} )'.format(fileName, count)
    #
    existsSourceFiles = lxBasic.getOsMultFileLis(sourceFile)
    existsSourceCount = len(existsSourceFiles)
    #
    fileItem = qtWidgets_.QTreeWidgetItem_()
    #
    if existsSourceFiles > 0:
        if existsSourceCount > 1:
            iconKeyword = 'svg_basic@svg#files'
            #
            subIconKeyword = 'svg_basic@svg#file'
            #
            subState = none
            #
            subSourceFiles = existsSourceFiles[1:]
            for subSourceFile in subSourceFiles:
                subFileItem = qtWidgets_.QTreeWidgetItem_()
                subShowExplain = lxBasic.getOsFileBasename(subSourceFile)
                setBranch(subFileItem, fileItem, subSourceFile, subIconKeyword, subState, subShowExplain)
    else:
        state = 'off'
    #
    setBranch(fileItem, parentUi, sourceFile, iconKeyword, state, showExplain)
    #
    return fileItem


#
def setListScMayaComposeCmdMain(
        projectName,
        sceneStage,
        treeBox,
        connectMethods
):
    def setSceneBranch(key, dataLis):
        def setScCameraBranch():
            def setScCameraActions():
                pass
            #
            def setRefreshScCameraItem(state):
                scCameraItemWidget = scCameraComposeItem.setItemIconWidget(
                    0,
                    scCameraIcon,
                    '{}'.format(scCameraShowExplain),
                    state
                )
            #
            scCameraIcon = 'svg_basic@svg#branch_main'
            scCameraComposeItem = qtWidgets_.QTreeWidgetItem_()
            sceneItem.addChild(scCameraComposeItem)
            setRefreshScCameraItem('')
            scCameraComposeItem.setExpanded(True)
            #
            setListScCameraComposeCmdSub(
                scCameraComposeItem,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                scCameraDatumLis,
                connectVariants=[
                    scCameraUnitItemLis,
                    (
                        scCameraCacheItemLis
                    )
                ],
                connectMethods=[
                    scCacheUpdateCheckMethod
                ]
            )
        #
        def setScAssetBranch():
            def setScAssetActions():
                pass
            #
            def setRefreshScAssetItem(state):
                scCameraItemWidget = scAssetComposeItem.setItemIconWidget(
                    0,
                    scAssetIcon,
                    '{}'.format(scAssetShowExplain),
                    state
                )
            #
            scAssetIcon = 'svg_basic@svg#branch_main'
            scAssetComposeItem = qtWidgets_.QTreeWidgetItem_()
            sceneItem.addChild(scAssetComposeItem)
            setRefreshScAssetItem('')
            scAssetComposeItem.setExpanded(True)
            #
            setListScAssetComposeCmdSub(
                scAssetComposeItem,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                scAssetDatumLis,
                connectVariants=[
                    scAssetUnitItemLis,
                    (
                        scAstModelProductItemLis, scAstModelCacheItemLis, scAstExtraCacheItemLis,
                        scAstCfxProductItemLis, scAstCfxFurCacheItemLis,
                        scAstSolverProductItemLis, scAstSolverCacheItemLis
                    )
                ],
                connectMethods=[
                    scCacheUpdateCheckMethod, scCacheUpdateCheckMethod, scCacheUpdateCheckMethod,
                    scCacheUpdateCheckMethod, scCacheUpdateCheckMethod,
                    scCacheUpdateCheckMethod, scCacheUpdateCheckMethod,
                ]
            )
        #
        sceneIndex, sceneClass, sceneName, sceneVariant = key
        scCameraDatumLis, scAssetDatumLis = dataLis
        #
        startFrame, endFrame = scenePr.getScUnitFrameRange(
            projectName,
            sceneClass, sceneName, sceneVariant
        )
        #
        sceneItem = qtWidgets_.QTreeWidgetItem_()
        treeBox.addItem(sceneItem)
        #
        itemIcon0 = 'svg_basic@svg#package_object'
        itemIconState0 = None
        itemIcon1 = 'svg_basic@svg#time'
        itemIconState1 = None
        #
        sceneShowName = scenePr.getSceneViewInfo(sceneIndex, sceneClass, '{} - {}'.format(sceneName, sceneVariant))
        #
        sceneItem.setItemIconWidget(
            0, itemIcon0, sceneShowName, itemIconState0
        )
        sceneItem.setText(1, '{} - {}'.format(startFrame, endFrame))
        sceneItem.setItemIcon_(1, itemIcon1, itemIconState1)
        # Cameras
        setScCameraBranch()
        # Assets
        setScAssetBranch()
        #
        sceneItem.setExpanded(True)
    #
    scCameraShowExplain = 'Camera(s)'
    scAssetShowExplain = 'Asset(s)'
    #
    scUnitLoadCheckMethod, scCacheUpdateCheckMethod = connectMethods
    #
    scCameraUnitItemLis = []
    #
    scCameraCacheItemLis = []
    #
    scAssetUnitItemLis = []
    #
    scAstModelProductItemLis = []
    scAstModelCacheItemLis = []
    #
    scAstCfxProductItemLis = []
    scAstCfxFurCacheItemLis = []
    #
    scAstSolverProductItemLis = []
    scAstSolverCacheItemLis = []
    #
    scAstExtraCacheItemLis = []
    #
    inData = datScene.getScComposeInfoDic(projectName)
    #
    treeBox.clear()
    if inData:
        explain = '''List Scene Compose'''
        maxValue = len(inData)
        progressBar = bscMethods.If_Progress(explain, maxValue)
        for k, v in inData.items():
            progressBar.update()
            #
            setSceneBranch(k, v)
    #
    return [
        (
            scCameraUnitItemLis,
            (
                scCameraCacheItemLis
             )
        ),
        (
            scAssetUnitItemLis,
            (
                scAstModelProductItemLis, scAstModelCacheItemLis, scAstExtraCacheItemLis,
                scAstCfxProductItemLis, scAstCfxFurCacheItemLis,
                scAstSolverProductItemLis, scAstSolverCacheItemLis
            )
        )
    ]


#
def setListScCameraComposeCmdSub(
        scCameraComposeItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        scCameraDatumLis,
        connectVariants,
        connectMethods
):
    def setScCameraBranch(args):
        # Args
        (
            scCameraSubLabel,
            scCameraBranchInfo
        ) = args
        #
        scCameraCacheItem = ifMaScTreeItem.IfScCameraCacheItem(
            scCameraComposeItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            scCameraBranchInfo, scCameraCacheConnectMethod, scCameraSubLabel
        )
        scCameraCacheItemLis.append(scCameraCacheItem)
    #
    [
        scCameraUnitItemLis,
        (
            scCameraCacheItemLis
        )
    ] = connectVariants
    scCameraCacheConnectMethod, = connectMethods
    #
    if scCameraDatumLis:
        progressExplain = u'''List Scene Camera(s)'''
        maxValue = len(scCameraDatumLis)
        progressBar = bscMethods.If_Progress(progressExplain, maxValue)
        for scCameraData in scCameraDatumLis:
            progressBar.update()
            setScCameraBranch(scCameraData)


#
def setListScAssetComposeCmdSub(
        scAssetComposeItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        scAssetDatumLis,
        connectVariants,
        connectMethods
):
    def setScAstBranch(args):
        (
            assetIndex,
            assetClass, assetName, number, assetVariant,
            #
            scAstModelProductBranchInfo, scAstModelCacheBranchInfo,
            scAstCfxProductBranchInfo, scAstCfxCacheBranchInfoLis,
            scAstSolverProductBranchInfo, scAstSolverCacheBranchInfo,
            scAstExtraCacheBranchInfo
        ) = args
        #
        scAssetUnitItem = ifMaScTreeItem.IfScAssetProductItem(
            scAssetComposeItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            scAstModelProductConnectMethod
        )
        scAssetUnitItemLis.append(scAssetUnitItem)
        # Model
        scAstModelProductItem = ifMaScTreeItem.IfScAstModelProductItem(
            scAssetUnitItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            scAstModelProductBranchInfo, scAstModelProductConnectMethod
        )
        scAstModelProductItemLis.append(scAstModelProductItem)
        # Mode Cache
        scAstModelCacheItem = ifMaScTreeItem.IfScAstModelCacheItem(
            scAstModelProductItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            scAstModelCacheBranchInfo, scAstModelCacheConnectMethod
        )
        scAstModelCacheItemLis.append(scAstModelCacheItem)
        # Extra Cache
        if scenePr.isScLightLink(sceneStage):
            # Rig Extra
            scAstExtraCacheItem = ifMaScTreeItem.IfScAstExtraCacheItem(
                scAssetUnitItem,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                scAstExtraCacheBranchInfo, scAstExtraCacheConnectMethod
            )
            scAstExtraCacheItemLis.append(scAstExtraCacheItem)
        # CFX
        scAstCfxProductItem = ifMaScTreeItem.IfScAstCfxProductItem(
            scAssetUnitItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            scAstCfxProductBranchInfo, scAstCfxProductConnectMethod
        )
        scAstCfxProductItemLis.append(scAstCfxProductItem)
        # CFX Fur Cache(s)
        if scAstCfxCacheBranchInfoLis:
            for furObjectLabel, scAstCfxCacheBranchInfo in scAstCfxCacheBranchInfoLis:
                scAstCfxFurCacheItem = ifMaScTreeItem.IfScAstCfxFurCacheItem(
                    scAstCfxProductItem,
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage,
                    startFrame, endFrame,
                    assetIndex,
                    assetClass, assetName, number, assetVariant,
                    scAstCfxCacheBranchInfo, scAstCfxFurCacheConnectMethod, furObjectLabel
                )
                scAstCfxFurCacheItemLis.append(scAstCfxFurCacheItem)
        # Solver
        if scenePr.isScSolverLink(sceneStage):
            # Solver Product
            scAstSolverProductItem = ifMaScTreeItem.IfScAstSolverProductItem(
                scAssetUnitItem,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                scAstSolverProductBranchInfo, scAstSolverProductConnectMethod
            )
            scAstSolverProductItemLis.append(scAstSolverProductItem)
            # Solver Cache
            scAstSolverCacheItem = ifMaScTreeItem.IfScAstSolverCacheItem(
                scAstSolverProductItem,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                scAstSolverCacheBranchInfo, scAstSolverCacheConnectMethod
            )
            scAstSolverCacheItemLis.append(scAstSolverCacheItem)
    #
    [
        scAssetUnitItemLis,
        (
            scAstModelProductItemLis, scAstModelCacheItemLis, scAstExtraCacheItemLis,
            scAstCfxProductItemLis, scAstCfxFurCacheItemLis,
            scAstSolverProductItemLis, scAstSolverCacheItemLis
        )
    ] = connectVariants
    [
        scAstModelProductConnectMethod, scAstModelCacheConnectMethod, scAstExtraCacheConnectMethod,
        scAstCfxProductConnectMethod, scAstCfxFurCacheConnectMethod,
        scAstSolverProductConnectMethod, scAstSolverCacheConnectMethod,

    ] = connectMethods
    #
    if scAssetDatumLis:
        progressExplain = u'''List Scene Asset(s)'''
        maxValue = len(scAssetDatumLis)
        progressBar = bscMethods.If_Progress(progressExplain, maxValue)
        for scAssetDatum in scAssetDatumLis:
            progressBar.update()
            setScAstBranch(scAssetDatum)
