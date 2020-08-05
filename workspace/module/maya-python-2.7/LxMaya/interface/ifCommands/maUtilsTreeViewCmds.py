# coding=utf-8
from LxBasic import bscMethods, bscObjects
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import scenePr
#
from LxGui.qt import qtWidgets_, guiQtWidgets
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
        objectType = maUtils._getNodeShapeCategoryString(path)
        #
        treeItem.setItemMayaIcon(0, objectType)
        #
        treeItem.setText(0, maUtils._nodeString2nodename_(path, 1))
        treeItem.setText(1, maUtils._getNodeCategoryString(path))
    #
    if objectPaths:
        subObjectPaths = treeBox.getGraphPaths(objectPaths, appCfg.DEF_mya_node_pathsep)
        hierDic = treeBox.getGraphDatumDic(subObjectPaths, appCfg.DEF_mya_node_pathsep)
        if hierDic:
            treeBox.setupGraph(hierDic, branchView, expandedDic)


#
def setListNodes(treeBox, nodes):
    def setBranch(node):
        nodeName = maUtils._nodeString2nodename_(node, 1)
        nodeType = maUtils._getNodeCategoryString(node)
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
                bscMethods.OsDirectory.open(filePath)
            #
            openFolderEnabled = bscMethods.OsDirectory.isExist(filePath)
            #
            actionExplain = 'Open Source Folder ( %s )' % folderName
            #
            branchActionData = [
                (actionExplain, 'svg_basic/folder', openFolderEnabled, setOpenFolder)
            ]
            #
            treeItemWidget.setActionData(branchActionData)
        #
        iconLabel = 'svg_basic/folder'
        stateLabel = none
        filePath = treeItem.path[1:]
        folderName = treeItem.name
        if ':' in folderName:
            iconLabel = 'svg_basic/server_root'
        count = 0
        fileDataArray = getFileDataArray(filePath)
        #
        if fileDataArray:
            count = len(fileDataArray)
        #
        if not bscMethods.OsDirectory.isExist(filePath):
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
        checkBox = guiQtWidgets.QtCheckbutton()
        checkBox.setNameString('Enable')
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
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
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
        iconKeywordStr = 'svg_basic/folder'
        stateLabel = none
        folderName = folderItem.name
        filePath = folderItem.path[1:]
        #
        if ':' in folderName:
            iconKeywordStr = 'svg_basic/server_root'
        count = 0
        fileDataArray = getFileDataArray(filePath)
        #
        if not bscMethods.OsDirectory.isExist(filePath):
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
        folderItem.setItemIcon_(0, iconKeywordStr, stateLabel)
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
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
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
    def setBranch(treeItem, parentItem, fileString_, iconKeyword_, iconState, explain):
        if type(parentItem) == qtWidgets_.QTreeWidget_:
            parentItem.addItem(treeItem)
        elif type(parentItem) == qtWidgets_.QTreeWidgetItem_:
            parentItem.addChild(treeItem)
            #
            parentItem.setExpanded(True)
        #
        treeItem.path = fileString_
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
    iconKeywordStr = 'svg_basic/file'
    #
    state = none
    #
    fileName = bscMethods.OsFile.basename(sourceFile)
    count = len(nodes)
    showExplain = '{0} ( {1} )'.format(fileName, count)
    #

    existsSourceFiles = bscMethods.OsMultifile.existFiles(sourceFile)
    #
    fileItem = qtWidgets_.QTreeWidgetItem_()
    #
    if existsSourceFiles:
        iconKeywordStr = 'svg_basic/files'

        subIconKeyword = 'svg_basic/file'

        subState = none

        subSourceFiles = existsSourceFiles
        for subSourceFile in subSourceFiles:
            subFileItem = qtWidgets_.QTreeWidgetItem_()

            subShowExplain = bscMethods.OsFile.basename(subSourceFile)
            setBranch(
                subFileItem,
                fileItem,
                subSourceFile,
                subIconKeyword,
                subState,
                subShowExplain
            )
    else:
        state = 'off'

    setBranch(fileItem, parentUi, sourceFile, iconKeywordStr, state, showExplain)

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
            scCameraIcon = 'svg_basic/branch_main'
            scCameraComposeItem = qtWidgets_.QTreeWidgetItem_()
            sceneItem.addChild(scCameraComposeItem)
            setRefreshScCameraItem('')
            scCameraComposeItem.setExpanded(True)
            #
            setListScCameraComposeCmdSub(
                scCameraComposeItem,
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
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
            scAssetIcon = 'svg_basic/branch_main'
            scAssetComposeItem = qtWidgets_.QTreeWidgetItem_()
            sceneItem.addChild(scAssetComposeItem)
            setRefreshScAssetItem('')
            scAssetComposeItem.setExpanded(True)
            #
            setListScAssetComposeCmdSub(
                scAssetComposeItem,
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
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
        sceneIndex, sceneCategory, sceneName, sceneVariant = key
        scCameraDatumLis, scAssetDatumLis = dataLis
        #
        startFrame, endFrame = scenePr.getScUnitFrameRange(
            projectName,
            sceneCategory, sceneName, sceneVariant
        )
        #
        sceneItem = qtWidgets_.QTreeWidgetItem_()
        treeBox.addItem(sceneItem)
        #
        itemIcon0 = 'svg_basic/package_object'
        itemIconState0 = None
        itemIcon1 = 'svg_basic/time'
        itemIconState1 = None
        #
        sceneShowName = scenePr.getSceneViewInfo(sceneIndex, sceneCategory, '{} - {}'.format(sceneName, sceneVariant))
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
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
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
        sceneCategory, sceneName, sceneVariant, sceneStage,
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
            sceneCategory, sceneName, sceneVariant, sceneStage,
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
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for scCameraData in scCameraDatumLis:
            progressBar.update()
            setScCameraBranch(scCameraData)


#
def setListScAssetComposeCmdSub(
        scAssetComposeItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        scAssetDatumLis,
        connectVariants,
        connectMethods
):
    def setScAstBranch(args):
        (
            assetIndex,
            assetCategory, assetName, number, assetVariant,
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
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            scAstModelProductConnectMethod
        )
        scAssetUnitItemLis.append(scAssetUnitItem)
        # Model
        scAstModelProductItem = ifMaScTreeItem.IfScAstModelProductItem(
            scAssetUnitItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            scAstModelProductBranchInfo, scAstModelProductConnectMethod
        )
        scAstModelProductItemLis.append(scAstModelProductItem)
        # Mode Cache
        scAstModelCacheItem = ifMaScTreeItem.IfScAstModelCacheItem(
            scAstModelProductItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            scAstModelCacheBranchInfo, scAstModelCacheConnectMethod
        )
        scAstModelCacheItemLis.append(scAstModelCacheItem)
        # Extra Cache
        if scenePr.isLightLinkName(sceneStage):
            # Rig Extra
            scAstExtraCacheItem = ifMaScTreeItem.IfScAstExtraCacheItem(
                scAssetUnitItem,
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                scAstExtraCacheBranchInfo, scAstExtraCacheConnectMethod
            )
            scAstExtraCacheItemLis.append(scAstExtraCacheItem)
        # CFX
        scAstCfxProductItem = ifMaScTreeItem.IfScAstCfxProductItem(
            scAssetUnitItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
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
                    sceneCategory, sceneName, sceneVariant, sceneStage,
                    startFrame, endFrame,
                    assetIndex,
                    assetCategory, assetName, number, assetVariant,
                    scAstCfxCacheBranchInfo, scAstCfxFurCacheConnectMethod, furObjectLabel
                )
                scAstCfxFurCacheItemLis.append(scAstCfxFurCacheItem)
        # Solver
        if scenePr.isSolverLinkName(sceneStage):
            # Solver Product
            scAstSolverProductItem = ifMaScTreeItem.IfScAstSolverProductItem(
                scAssetUnitItem,
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                scAstSolverProductBranchInfo, scAstSolverProductConnectMethod
            )
            scAstSolverProductItemLis.append(scAstSolverProductItem)
            # Solver Cache
            scAstSolverCacheItem = ifMaScTreeItem.IfScAstSolverCacheItem(
                scAstSolverProductItem,
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
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
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for scAssetDatum in scAssetDatumLis:
            progressBar.update()
            setScAstBranch(scAssetDatum)
