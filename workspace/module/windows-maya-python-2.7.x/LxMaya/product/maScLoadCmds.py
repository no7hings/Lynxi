# coding=utf-8
import os

from LxBasic import bscMethods, bscModifiers, bscObjects

from LxCore.config import appCfg

from LxPreset import prsConfigure, prsVariants, prsMethods

from LxCore.preset.prod import assetPr, scenePr

from LxMaya.command import maUtils, maFile, maHier, maPreference, maFur, maCacheConnect, maRender

from LxMaya.product.data import datScene

from LxMaya.product.op import sceneOp, sceneryOp

astDefaultVersion = prsVariants.Util.astDefaultVersion

none = ''


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def scUnitSceneCreateMainCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        withCamera=False, withScenery=False,
        withFrame=False, withSize=False,
        withAstModel=False, withModelCache=False,
        withAstCfx=False, withAstCfxFurCache=False,
        withAstSolver=False, withAstSolverCache=False,
        withExtraCache=False
):
    sceneStagePrettify = sceneStage.capitalize()
    #
    logWin_ = bscObjects.LogWindow(u'{} Create'.format(sceneStagePrettify))
    logWin_.showUi()
    #
    maUtils.setDisplayMode(5)
    #
    maPreference.setAnimationTimeUnit(projectName)
    # Layout
    if scenePr.isLayoutLinkName(sceneStage):
        maHier.setCreateScLinkHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage)
    # Animation
    elif scenePr.isAnimationLinkName(sceneStage):
        serverProductFile = scenePr.sceneUnitProductFile(
            prsConfigure.Utility.DEF_value_root_server,
            projectName, 
            sceneCategory, sceneName, sceneVariant, prsMethods.Scene.layoutLinkName()
        )[1]
        localSourceFile = scenePr.sceneUnitSourceFile(
            prsConfigure.Utility.DEF_value_root_local,
            projectName, 
            sceneCategory, sceneName, sceneVariant, prsMethods.Scene.VAR_product_scene_animation_stage_list[0]
        )[1]
        maFile.openMayaFileToLocal(serverProductFile, localSourceFile)
    # Simulation
    elif scenePr.isSimulationLinkName(sceneStage):
        maHier.setCreateScLinkHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage)
        # Asset Model Cache
        scUnitAstModelCachesLoadCmd(
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage
        )
        # Asset Mode Pose Cache
        scUnitAstModelPoseCachesLoadCmd(
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage
        )
    # Solver
    elif scenePr.isSolverLinkName(sceneStage):
        # Load Animation
        maHier.setCreateScLinkHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage)
        #
        scUnitAssetsLoadCmd(
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            withAstModel=withAstModel, withModelCache=withModelCache,
            withAstCfx=withAstCfx, withAstCfxFurCache=withAstCfxFurCache,
            withAstSolver=withAstSolver, withAstSolverCache=withAstSolverCache,
            withExtraCache=withExtraCache,
        )
    # Light
    elif scenePr.isLightLinkName(sceneStage):
        maHier.setCreateScLinkHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage)
        #
        scUnitAssetsLoadCmd(
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            withAstModel=withAstModel, withModelCache=withModelCache,
            withAstCfx=withAstCfx, withAstCfxFurCache=withAstCfxFurCache,
            withAstSolver=withAstSolver, withAstSolverCache=withAstSolverCache,
            withExtraCache=withExtraCache,
        )
    #
    maHier.refreshScRoot(sceneCategory, sceneName, sceneVariant, sceneStage, sceneIndex)
    # is Used Default Camera
    if withCamera:
        logWin_.addStartProgress(u'Camera Create')
        if scenePr.isLayoutLinkName(sceneStage):
            sceneCamera = scenePr.scSceneCameraName(sceneName, sceneVariant)
            if not maUtils._isNodeExist(sceneCamera):
                sceneOp.setCreateSceneCamera(sceneName, sceneVariant)
            #
            sceneOp.setAddSceneCameras(sceneName, [maUtils._getNodePathString(sceneCamera)])
        # Simulation and Light
        elif scenePr.isSolverLinkName(sceneStage) or scenePr.isSimulationLinkName(sceneStage) or scenePr.isLightLinkName(sceneStage):
            scUnitCameraCachesLoadCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage
            )
            if scenePr.isLightLinkName(sceneStage):
                scOutputCameras = scenePr.getOutputCameras(
                    projectName,
                    sceneCategory, sceneName, sceneVariant
                )
                maRender.setRenderCamera(scOutputCameras)
        #
        logWin_.addCompleteProgress()
    # Load Scenery
    if withScenery:
        if scenePr.isSimulationLinkName(sceneStage) or scenePr.isSolverLinkName(sceneStage) or scenePr.isLightLinkName(sceneStage):
            scUnitSceneryExtraLoadLoadCmd(
                projectName,
                sceneCategory, sceneName, sceneVariant, sceneStage
            )
    # Frame
    if withFrame:
        logWin_.addStartProgress(u'Render Frame Create')
        #
        if scenePr.isLayoutLinkName(sceneStage):
            startFrame, endFrame = withFrame
            maUtils.setAnimationFrameRange(startFrame, endFrame)
        #
        elif scenePr.isSimulationLinkName(sceneStage) or scenePr.isSolverLinkName(sceneStage) or scenePr.isLightLinkName(sceneStage):
            startFrame, endFrame = scenePr.getScUnitFrameRange(
                projectName, sceneCategory, sceneName, sceneVariant
            )
            if scenePr.isSimulationLinkName(sceneStage) or scenePr.isSolverLinkName(sceneStage):
                startFrame -= 50
            # Frame Range
            maUtils.setAnimationFrameRange(startFrame, endFrame)
            # Current Frame
            maUtils.setCurrentFrame(startFrame)
            #
            if scenePr.isLightLinkName(sceneStage):
                maRender.setRenderTime(startFrame, endFrame)
                maRender.setAnimationFrameMode()
        #
        logWin_.addCompleteProgress()
    # Size
    if withSize:
        logWin_.addStartProgress(u'Render Size Create')
        #
        if scenePr.isLayoutLinkName(sceneStage):
            width, height = withSize
            maUtils.setRenderSize(width, height)
        #
        elif scenePr.isSolverLinkName(sceneStage) or scenePr.isSimulationLinkName(sceneStage) or scenePr.isLightLinkName(sceneStage):
            width = prsVariants.Util.rndrImageWidth
            height = prsVariants.Util.rndrImageHeight
            #
            maUtils.setRenderSize(width, height)
        #
        logWin_.addCompleteProgress()
    # Set Workspace
    if scenePr.isLightLinkName(sceneStage):
        workspaceRoot = scenePr.scUnitRenderFolder(
            prsConfigure.Utility.DEF_value_root_local,
            projectName,
            sceneCategory, sceneName, sceneVariant, sceneStage, prsVariants.Util.scDefaultCustomizeLabel
        )
        maRender.setCreateWorkspace(workspaceRoot)
        #
        maRender.setImagePath(maRender.MaRender_DefaultImageFilePrefix)
    # TD Command
    tdCommand = scenePr.getScTdLoadCommand(
        projectName,
        prsMethods.Scene.stageName2linkName(sceneStage)
    )
    if tdCommand:
        maUtils.runMelCommand(tdCommand)
    # Save to Local
    scUnitSourceSaveCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage
    )
    logWin_.addCompleteTask()


#
def scUnitFrameLoadCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscObjects.LogWindow()
    #
    startFrame, endFrame = scenePr.getScUnitFrameRange(
        projectName,
        sceneCategory, sceneName, sceneVariant
    )
    # Time Unit
    maPreference.setAnimationTimeUnit(projectName)
    #
    if scenePr.isSimulationLinkName(sceneStage) or scenePr.isSolverLinkName(sceneStage):
        maUtils.setAnimationFrameRange(startFrame - 50, endFrame)
    else:
        maUtils.setAnimationFrameRange(startFrame, endFrame)
    # Current Frame
    maUtils.setCurrentFrame(startFrame)
    #
    maRender.setRenderTime(startFrame, endFrame)
    maRender.setAnimationFrameMode()


@bscModifiers.fncExceptionCatch
def scUnitSceneLoadMainCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        withFrame=False, withSize=False
):
    sceneStagePrettify = sceneStage.capitalize()

    logWin_ = bscObjects.LogWindow(u'{} Load'.format(sceneStagePrettify))
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'{} Load'.format(sceneStagePrettify))
    logWin_.showUi()
    #
    maUtils.setDisplayMode(5)
    #
    serverProductFile = scenePr.sceneUnitProductFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, sceneCategory, sceneName, sceneVariant, sceneStage
    )[1]
    localSourceFile = scenePr.sceneUnitSourceFile(
        prsConfigure.Utility.DEF_value_root_local,
        projectName, sceneCategory, sceneName, sceneVariant, sceneStage
    )[1]
    logWin_.addStartProgress(u'Source Load')
    #
    maFile.openMayaFileToLocal(serverProductFile, localSourceFile)
    #
    if not scenePr.isAnimationLinkName(sceneStage):
        maHier.setCreateScLinkHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage)
    #
    maHier.refreshScRoot(sceneCategory, sceneName, sceneVariant, sceneStage, sceneIndex)
    #
    logWin_.addCompleteProgress()
    #
    if withFrame:
        logWin_.addStartProgress(u'Render Frame Load')
        #
        startFrame, endFrame = withFrame
        maUtils.setAnimationFrameRange(startFrame, endFrame)
        #
        logWin_.addCompleteProgress()
    #
    if withSize:
        logWin_.addStartProgress(u'Render Size Load')
        #
        width, height = withSize
        maUtils.setRenderSize(width, height)
        #
        logWin_.addCompleteProgress()
    # Complete
    logWin_.addCompleteTask()


#
def scUnitSourceSaveCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscObjects.LogWindow()
    
    localSourceFile = scenePr.sceneUnitSourceFile(
        prsConfigure.Utility.DEF_value_root_local,
        projectName, sceneCategory, sceneName, sceneVariant, sceneStage
    )[1]
    #
    maUtils.setVisiblePanelsDelete()
    maUtils.setCleanUnknownNodes()
    #
    logWin_.addStartProgress(u'Source ( Local ) Save')
    #
    maFile.saveMayaFileToLocal(localSourceFile)
    #
    logWin_.addCompleteProgress()


# Camera Cache
def scUnitCameraCachesLoadCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscObjects.LogWindow()
    
    datumDic = scenePr.getSceneCameraIndexDataDic(
        projectName, sceneCategory, sceneName, sceneVariant
    )
    if datumDic:
        for k, v in datumDic.items():
            progressExplain = u'''Load Scene Camera Cache'''
            maxValue = len(v)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for seq, i in enumerate(v):
                progressBar.update()
                #
                timestamp, cacheStage, startFrame, endFrame, scCameraCache = i
                #
                if timestamp is not None:
                    subLabelString = bscMethods.OsFile.seqLabel(seq)
                    scUnitCameraCacheLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage, subLabelString,
                        withCameraCache=True
                    )


#
def scUnitCameraCacheLoadSubCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage, subLabelString,
        withCameraCache
):
    def getFile():
        fileString = None
        if isinstance(withCameraCache, bool):
            if withCameraCache is True:
                fileString = scenePr.getScCameraCacheActive(
                    projectName,
                    sceneName, sceneVariant,
                    subLabelString
                )
        elif isinstance(withCameraCache, str) or isinstance(withCameraCache, unicode):
            fileString = withCameraCache
        #
        if fileString is not None:
            if bscMethods.OsFile.isExist(fileString):
                return fileString
    #
    logWin_ = bscObjects.LogWindow()
    
    scCameraCacheFile = getFile()
    #
    if scCameraCacheFile is not None:
        #
        linkCameraPath = scenePr.scCameraSubGroupPath(sceneName, sceneVariant, sceneStage)
        scCameraNamespace = scenePr.scCameraNamespace(
            sceneName, sceneVariant
        ) + subLabelString
        #
        scOutputCameraLocator = scenePr.scOutputCameraLocatorName(sceneName, sceneVariant, scCameraNamespace) + subLabelString
        if maUtils._isNodeExist(scOutputCameraLocator):
            maUtils.setNodesClearByNamespace(scCameraNamespace)
            #
            logWin_.addResult(u'Remove Exists', )
        #
        logWin_.addStartProgress(u'Camera Cache Load', scCameraCacheFile)
        #
        maFile.setAlembicCacheImport(scCameraCacheFile, scCameraNamespace)
        #
        logWin_.addCompleteProgress()
        #
        if maUtils._isNodeExist(linkCameraPath):
            maUtils.setObjectParent(scOutputCameraLocator, linkCameraPath)
        #
        scCamera = scenePr.scOutputCameraName(sceneName, sceneVariant, scCameraNamespace) + subLabelString
        if maUtils._isNodeExist(scCamera):
            maUtils.setDisplayMode(5)
            maUtils.setCameraView(scCamera)
            maUtils.setObjectLockTransform(scCamera, boolean=True)
            bscObjects.MessageWindow(u'''Set Camera View''', u'''Complete''')
    else:
        logWin_.addWarning(u'Scene Camera ( Cache ) is Non - Exists')


# Model Cache
def scUnitAstModelCachesLoadCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        withAstCfx=False, withAstCfxFurCache=False
):
    logWin_ = bscObjects.LogWindow()
    
    datumDic = scenePr.getSceneAssetIndexDataDic(
        projectName,
        sceneCategory, sceneName, sceneVariant
    )
    if datumDic:
        for k, v in datumDic.items():
            progressExplain = u'''Load Scene Asset Model Cache'''
            maxValue = len(v)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for i in v:
                progressBar.update()
                #
                (
                    timestamp, cacheStage, startFrame, endFrame, cache,
                    assetIndex, assetCategory, assetName, number, assetVariant
                 ) = i
                #
                if timestamp is not None:
                    scUnitAstModelCacheLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneCategory, sceneName, sceneVariant, sceneStage,
                        assetIndex,
                        assetCategory, assetName, number, assetVariant,
                        withModelCache=True
                    )


#
def scUnitAstModelCacheLoadSubCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withModelCache
):
    def getFile():
        fileString = None
        if isinstance(withModelCache, bool):
            if withModelCache is True:
                fileString = scenePr.getScAstModelCacheActive(
                    projectName,
                    sceneName, sceneVariant,
                    assetName, number
                )
        elif isinstance(withModelCache, str) or isinstance(withModelCache, unicode):
            fileString = withModelCache
        #
        if fileString is not None:
            if bscMethods.OsFile.isExist(fileString):
                return fileString
    #
    logWin_ = bscObjects.LogWindow()
    
    scAstModelCacheFile = getFile()
    if scAstModelCacheFile is not None:
        # Create Scene Root
        scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
        if not maUtils._isNodeExist(scUnitRoot):
            maHier.setCreateScLinkHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage)
            maHier.refreshScRoot(sceneCategory, sceneName, sceneVariant, sceneStage, sceneIndex)
        #
        scAstSubPath = scenePr.scAssetSubGroupPath(sceneName, sceneVariant, sceneStage)
        #
        scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        scAstUnitRootGroup = prsMethods.Asset.rootName(assetName)
        #
        astModelGroup = prsMethods.Asset.modelLinkGroupName(assetName)
        scAstModelGroup = scenePr.scAstModelGroupName(sceneName, sceneVariant, assetName, number)
        if maUtils._isNodeExist(scAstModelGroup):
            maUtils.setNodeDelete(scAstModelGroup)
            #
            logWin_.addWarning(u'Remove Exists',)
        #
        logWin_.addStartProgress(u'Model Cache Load', scAstModelCacheFile)
        #
        maFile.setAlembicCacheImport(scAstModelCacheFile)
        #
        logWin_.addCompleteProgress()
        # Create Group
        maUtils.setAppPathCreate(scAstRootGroup)
        maUtils.setAppPathCreate(scAstUnitRootGroup)
        #
        maUtils.setObjectParent('|' + astModelGroup, scAstUnitRootGroup)
        maUtils.setObjectParent(scAstUnitRootGroup, scAstRootGroup)
        #
        maUtils.setNodeOutlinerRgb(scAstRootGroup, 0, 1, 1)
        #
        timetag = bscMethods.OsTimetag.active()
        maHier.refreshScAstUnitBranch(
            scAstRootGroup,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            timetag
        )
        #
        if maUtils._isNodeExist(scAstSubPath):
            maUtils.setObjectParent(scAstRootGroup, scAstSubPath)
    else:
        logWin_.addWarning(u'Scene Model ( Cache ) is Non - Exists')


# Model Pose Cache(s)
def scUnitAstModelPoseCachesLoadCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscObjects.LogWindow()
    
    datumDic = scenePr.getSceneAssetIndexDataDic(
        projectName, sceneCategory, sceneName, sceneVariant
    )
    if datumDic:
        for k, v in datumDic.items():
            progressExplain = u'''Load Scene Asset Model ( Pose Cache )'''
            maxValue = len(v)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for i in v:
                progressBar.update()
                #
                (
                    timestamp, cacheStage, startFrame, endFrame, _,
                    assetIndex, assetCategory, assetName, number, assetVariant
                ) = i
                #
                cache = scenePr.getScAstModelPoseCacheActive(
                    projectName,
                    sceneName, sceneVariant, assetName, number
                )
                scUnitAstModelPoseCacheLoadSubCmd(
                    projectName,
                    sceneIndex,
                    sceneName, sceneVariant, sceneStage,
                    assetIndex,
                    assetCategory, assetName, number, assetVariant,
                    cache
                )


# Model Pose Cache Sub
def scUnitAstModelPoseCacheLoadSubCmd(
        projectName,
        sceneIndex,
        sceneName, sceneVariant, sceneStage,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withModelPoseCache
):
    def getFile():
        fileString = None
        if isinstance(withModelPoseCache, bool):
            if withModelPoseCache is True:
                fileString = scenePr.getScAstModelPoseCacheActive(
                    projectName,
                    sceneName, sceneVariant,
                    assetName, number
                )
        elif isinstance(withModelPoseCache, str) or isinstance(withModelPoseCache, unicode):
            fileString = withModelPoseCache
        #
        if fileString is not None:
            if bscMethods.OsFile.isExist(fileString):
                return fileString
    logWin_ = bscObjects.LogWindow()
    #
    scAstModelPoseCacheFile = getFile()
    if scAstModelPoseCacheFile is not None:
        scAstSimNamespace = scenePr.scAstSimulationNamespace(sceneName, sceneVariant, assetName, number)
        scAstModelGroup = prsMethods.Asset.modelLinkGroupName(assetName, scAstSimNamespace)
        if maUtils._isNodeExist(scAstModelGroup):
            maUtils.setNodeDelete(scAstModelGroup)
            #
            logWin_.addWarning(u'Remove Exists')
        #
        logWin_.addStartProgress(u'Model Pose Cache Load', scAstModelPoseCacheFile)
        #
        maFile.setAlembicCacheImport(scAstModelPoseCacheFile, scAstSimNamespace)
        #
        logWin_.addCompleteProgress()
    else:
        logWin_.addWarning(u'Scene Asset Model ( Pose Cache ) is Non - Exists')


# Asset(s)
def scUnitAssetsLoadCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        withAstModel=False, withModelCache=False,
        withAstCfx=False, withAstCfxFurCache=False,
        withAstSolver=False, withAstSolverCache=False,
        withExtraCache=False
):
    logWin_ = bscObjects.LogWindow()
    
    datumDic = scenePr.getSceneAssetIndexDataDic(
        projectName, sceneCategory, sceneName, sceneVariant
    )
    if datumDic:
        for k, v in datumDic.items():
            progressExplain = u'''Load Scene Asset(s)'''
            maxValue = len(v)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for i in v:
                progressBar.update()
                #
                (
                    timestamp, cacheStage,
                    startFrame, endFrame, scAstModelCache,
                    assetIndex,
                    assetCategory, assetName, number, assetVariant
                ) = i
                #
                scUnitAssetLoadSubCmd(
                    projectName,
                    sceneIndex,
                    sceneCategory, sceneName, sceneVariant, sceneStage,
                    startFrame, endFrame,
                    assetIndex, assetCategory, assetName, number, assetVariant,
                    withAstModel=withAstModel, withModelCache=withModelCache,
                    withAstCfx=withAstCfx, withAstCfxFurCache=withAstCfxFurCache,
                    withAstSolver=withAstSolver, withAstSolverCache=withAstSolverCache,
                    withExtraCache=withExtraCache
                )


# Asset Sub
def scUnitAssetLoadSubCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withAstModel=False, withModelCache=False,
        withAstCfx=False, withAstCfxFurCache=False,
        withAstSolver=False, withAstSolverCache=False,
        withExtraCache=False,
        usePoolAsset=False,
        isOffset=False, isLoop=False
):
    logWin_ = bscObjects.LogWindow()
    
    # Create Scene Root
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if not maUtils._isNodeExist(scUnitRoot):
        maHier.setCreateScLinkHierarchy(sceneCategory, sceneName, sceneVariant, sceneStage)
        maHier.refreshScRoot(sceneCategory, sceneName, sceneVariant, sceneStage, sceneIndex)
    #
    scAstSubPath = scenePr.scAssetSubGroupPath(sceneName, sceneVariant, sceneStage)
    #
    scAstRootPath = scenePr.scAstRootGroupPath(sceneName, sceneVariant, assetName, number)
    if not maUtils._isNodeExist(scAstRootPath):
        # Create Group
        maUtils.setAppPathCreate(scAstRootPath)
        #
        timetag = bscMethods.OsTimetag.active()
        #
        maHier.refreshScAstUnitBranch(
            scAstRootPath,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            timetag
        )
        #
        maUtils.setNodeOutlinerRgb(scAstRootPath, 0, 1, 1)
        #
        logWin_.addStartProgress(u'Asset Load')
        # Model
        if withAstModel:
            scUnitAstModelProductLoadCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                withAstModel=withAstModel, withModelCache=withModelCache,
                usePoolAsset=usePoolAsset
            )
        # CFX
        if withAstCfx is True:
            scUnitAstCfxProductLoadCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                withAstCfxFurCache=withAstCfxFurCache,
                usePoolAsset=usePoolAsset
            )
        #
        if withAstSolver is True:
            scUnitAstSolverProductLoadCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                withAstSolverCache=withAstSolverCache
            )
        # Extra
        if withExtraCache:
            scUnitAstExtraCacheConnectCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                withAstRigExtraCache=True
            )
        #
        logWin_.addCompleteProgress()
    else:
        assetShowName = prsVariants.Util.assetTreeViewName(assetName, number, assetVariant)
        logWin_.addWarning(assetShowName, u'Asset is Exists')
    #
    maUtils.setObjectParent(scAstRootPath, scAstSubPath)


#
def scUnitAstModelProductLoadCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withAstModel=False, withModelCache=False,
        usePoolAsset=False
):
    def getProductFile():
        fileString = None
        if isinstance(withAstModel, bool):
            if withAstModel is True:
                fileString = assetPr.astUnitProductFile(
                    prsConfigure.Utility.DEF_value_root_server,
                    projectName, assetCategory, assetName, assetVariant, assetStage
                )[1]
        elif isinstance(withAstModel, str) or isinstance(withAstModel, unicode):
            fileString = withAstModel
        #
        if fileString is not None:
            if bscMethods.OsFile.isExist(fileString):
                return fileString
    logWin_ = bscObjects.LogWindow()
    #
    maPreference.setAnimationTimeUnit(projectName)
    #
    assetStage = prsMethods.Asset.modelLinkName()
    #
    astModelProductFile = getProductFile()
    if astModelProductFile is not None:
        timetag = bscMethods.OsFile.mtimetag(astModelProductFile)
        #
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        scAstModelGroup = prsMethods.Asset.modelLinkGroupName(assetName, scAstModelNamespace)
        scAstModelContainer = assetPr.astModelContainerName(assetName, scAstModelNamespace)
        # Clean Exists
        if maUtils._isNodeExist(scAstModelGroup):
            if prsVariants.Util.rndrUseReference is True:
                scAstModelReferenceNode = scenePr.scAstModelReferenceNode(sceneName, sceneVariant, assetName, number)
                #
                maUtils.setReferenceRemove(scAstModelReferenceNode)
                maUtils.setNamespaceRemove(scAstModelNamespace)
            else:
                maUtils.setNodesClearByNamespace(scAstModelNamespace)
            #
            logWin_.addResult(u'Clean Exists',)
        # Load Product
        logWin_.addStartProgress(u'Model Product Load', astModelProductFile)
        #
        if prsVariants.Util.rndrUseReference is True:
            maFile.setMaFileReference(astModelProductFile, scAstModelNamespace)
        else:
            maFile.setAlembicCacheImport(astModelProductFile, scAstModelNamespace)
        #
        logWin_.addCompleteProgress()
        # Refresh Root
        maHier.scUnitRefreshRoot(
            assetIndex,
            assetCategory, assetName, assetVariant, assetStage,
            timetag,
            scAstModelNamespace
        )
        # Load Cache
        if withModelCache is not False:
            scUnitAstModelCacheConnectCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                withModelCache=withModelCache,
                isOffset=False, isLoop=False
            )
        #
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        scAstModelDisplayLayer = scenePr.scAstModelDisplayLayer(sceneName, sceneVariant, assetName, number)
        sceneOp.setScAstModelDisplayLayer(
            assetName, scAstModelNamespace, scAstModelDisplayLayer
        )
        #
        if maUtils._isNodeExist(scAstRootGroup):
            maUtils.setObjectParent(scAstModelGroup, scAstRootGroup)
            maUtils.setObjectParent(scAstModelContainer, scAstRootGroup)
        #
        else:
            logWin_.addWarning(u'Asset Model ( Root ) is Non - Exists')
    else:
        logWin_.addWarning(u'Asset Model ( Product File ) is Non - Exists')


#
def scUnitAstModelCacheConnectCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withModelCache,
        isOffset=False, isLoop=False
):
    def getFile():
        fileString = None
        if isinstance(withModelCache, bool):
            if withModelCache is True:
                fileString = scenePr.getScAstModelCacheActive(
                    projectName,
                    sceneName, sceneVariant,
                    assetName, number
                )
        elif isinstance(withModelCache, str) or isinstance(withModelCache, unicode):
            fileString = withModelCache
        #
        if fileString is not None:
            if bscMethods.OsFile.isExist(fileString):
                return fileString
    logWin_ = bscObjects.LogWindow()
    
    cacheFile = getFile()
    #
    if cacheFile is not None:
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        scAstModelCacheNamespace = scenePr.scAstModelCacheNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstModelGroup = prsMethods.Asset.modelLinkGroupName(assetName, scAstModelNamespace)
        if maUtils._isNodeExist(scAstModelGroup):
            scAstModelCacheGroup = prsMethods.Asset.modelLinkGroupName(assetName, scAstModelCacheNamespace)
            if not maUtils._isNodeExist(scAstModelCacheGroup):
                # Clear Cache Nde_Node
                connectMethod = maCacheConnect.LxAstModelCacheConnectMethod(assetName, scAstModelCacheNamespace, scAstModelNamespace)
                #
                connectMethod.setSourceClear()
                #
                logWin_.addStartProgress(u'Model Cache Load', cacheFile)
                #
                maFile.setAlembicCacheImport(cacheFile, scAstModelCacheNamespace)
                #
                logWin_.addCompleteProgress()
                #
                logWin_.addStartProgress(u'Cache Connect')
                #
                connectMethod.connect()
                #
                connectionLis = connectMethod.connectionLis
                if connectionLis:
                    scAstModelReferenceNode = scenePr.scAstModelReferenceNode(sceneName, sceneVariant, assetName, number)
                    if maUtils._isNodeExist(scAstModelReferenceNode):
                        maUtils.setReloadReferenceFile(scAstModelReferenceNode)
                    #
                    for sourceAttr, targetAttr in connectionLis:
                        maUtils.setAttrDisconnect(sourceAttr, targetAttr)
                        maUtils.setAttrConnect(sourceAttr, targetAttr)
                        #
                        logWin_.addResult(sourceAttr, targetAttr)
                #
                errorObjectLis = connectMethod.errorObjectLis
                if errorObjectLis:
                    for i in errorObjectLis:
                        logWin_.addError(i, u'Mesh is Error ( Topo Non - Match )')
                #
                logWin_.addCompleteProgress()
                # Offset Act Start Frame to Start Frame
                currentStartFrame, currentEndFrame = maUtils.getFrameRange()
                #
                alembicNode = bscMethods.OsFile.name(cacheFile) + '_AlembicNode'
                # Frame Offset
                if isOffset:
                    offset = currentStartFrame - startFrame
                    maUtils.setAttrDatumForce_(alembicNode, 'offset', offset)
                    maUtils.setAnimationFrameRange(currentStartFrame, endFrame - startFrame + currentStartFrame)
                # Frame Loop
                if isLoop:
                    maUtils.setAttrDatumForce_(alembicNode, 'cycleType', 1)
        else:
            logWin_.addWarning(u'Asset Model ( Root ) is Non - Exists')
    else:
        logWin_.addWarning(u'Asset Model ( Cache File ) is Non - Exists')


#
def scUnitAstExtraCacheConnectCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withAstRigExtraCache
):
    def getFile():
        fileString = None
        if isinstance(withAstRigExtraCache, bool):
            if withAstRigExtraCache is True:
                fileString = scenePr.getScAstRigExtraCacheActive(
                    projectName,
                    sceneName, sceneVariant,
                    assetName, number
                )
        elif isinstance(withAstRigExtraCache, str) or isinstance(withAstRigExtraCache, unicode):
            fileString = withAstRigExtraCache
        #
        if fileString is not None:
            if bscMethods.OsFile.isExist(fileString):
                return fileString
    logWin_ = bscObjects.LogWindow()
    #
    scAstRigExtraCacheFile = getFile()
    if scAstRigExtraCacheFile is not None:
        scAstExtraCacheNamespace = scenePr.scAstExtraNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        astRigBridgeGroup = assetPr.astUnitRigBridgeGroupName(assetName, scAstExtraCacheNamespace)
        #
        if maUtils._isNodeExist(astRigBridgeGroup):
            maUtils.setNodesClearByNamespace(scAstExtraCacheNamespace)
            #
            logWin_.addResult(u'Clean Exists', )
        #
        logWin_.addStartProgress(u'Extra Cache Load', scAstRigExtraCacheFile)
        #
        maFile.setAlembicCacheImport(scAstRigExtraCacheFile, scAstExtraCacheNamespace)
        #
        logWin_.addCompleteProgress()
        #
        if maUtils._isNodeExist(scAstRootGroup):
            maUtils.setObjectParent(astRigBridgeGroup, scAstRootGroup)
    else:
        logWin_.addWarning(scenePr.scAstName(assetName, number, assetVariant), u'Asset Extra Cache is Non - Exists')


# Character FX
def scUnitAstCfxProductLoadCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withAstCfxFurCache=False,
        usePoolAsset=False
):
    logWin_ = bscObjects.LogWindow()
    
    maPreference.setAnimationTimeUnit(projectName)
    #
    assetStage = prsMethods.Asset.groomLinkName()
    #
    astCfxProductFile = assetPr.astUnitProductFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName, assetCategory, assetName, assetVariant, assetStage
    )[1]
    if bscMethods.OsFile.isExist(astCfxProductFile):
        timetag = bscMethods.OsFile.mtimetag(astCfxProductFile)
        #
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        scAstCfxNamespace = scenePr.scAstCfxNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        astCfxGroup = prsMethods.Asset.groomLinkGroupName(assetName, scAstCfxNamespace)
        scAstCfxContainer = assetPr.astCfxContainerName(assetName, scAstCfxNamespace)
        if not maUtils._isNodeExist(astCfxGroup):
            logWin_.addStartProgress(u'Groom Product Load', astCfxProductFile)
            #
            if prsVariants.Util.rndrUseReference is True:
                maFile.setMaFileReference(astCfxProductFile, scAstCfxNamespace)
            else:
                maFile.setAlembicCacheImport(astCfxProductFile, scAstCfxNamespace)
            #
            logWin_.addCompleteProgress()
            # Refresh Root
            maHier.scUnitRefreshRoot(
                assetIndex,
                assetCategory, assetName, assetVariant, assetStage,
                timetag,
                scAstCfxNamespace
            )
            # Grow Source
            maFur.setScAstCfxGrowSourceConnectToModel(
                assetName, scAstModelNamespace, scAstCfxNamespace
            )
            # Display
            scAstCfxDisplayLayer = scenePr.scAstCfxDisplayLayer(
                sceneName, sceneVariant, assetName, number
            )
            maFur.setScAstCfxDisplayLayer(
                assetName, scAstCfxNamespace, scAstCfxDisplayLayer
            )
            #
            if withAstCfxFurCache:
                scUnitAstCfxFurCachesConnectCmd(
                    projectName,
                    sceneIndex,
                    sceneCategory, sceneName, sceneVariant, sceneStage,
                    startFrame, endFrame,
                    assetIndex,
                    assetCategory, assetName, number, assetVariant,
                    withAstCfxFurCache=withAstCfxFurCache
                )
        #
        if maUtils._isNodeExist(scAstRootGroup):
            maUtils.setObjectParent(astCfxGroup, scAstRootGroup)
            maUtils.setObjectParent(scAstCfxContainer, scAstRootGroup)
        #
        else:
            logWin_.addWarning(u'Asset CFX is Exists' )


#
def scUnitAstSolverProductLoadCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withAstSolverCache=False
):
    logWin_ = bscObjects.LogWindow()
    
    astSolverProductFile = assetPr.astUnitProductFile(
        prsConfigure.Utility.DEF_value_root_server,
        projectName,
        assetCategory, assetName, assetVariant, prsMethods.Asset.solverLinkName()
    )[1]
    if bscMethods.OsFile.isExist(astSolverProductFile):
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstCfxNamespace = scenePr.scAstCfxNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstSolverNamespace = scenePr.scAstSolverNamespace(sceneName, sceneVariant, assetName, number)
        #
        astSolverLinkGroup = prsMethods.Asset.groomLinkGroupName(assetName, scAstSolverNamespace)
        if not maUtils._isNodeExist(astSolverLinkGroup):
            logWin_.addStartProgress(u'Solver Product Load', astSolverProductFile)
            #
            maFile.setMaFileReference(astSolverProductFile, scAstSolverNamespace)
            #
            logWin_.addCompleteProgress()
            #
            maFur.setScAstSolverGrowSourceConnectToModel(
                assetName,
                scAstModelNamespace, scAstSolverNamespace
            )
            #
            astSolverExtraFile = assetPr.astUnitExtraFile(
                prsConfigure.Utility.DEF_value_root_server,
                projectName,
                assetCategory, assetName, assetVariant, prsMethods.Asset.solverLinkName()
            )[1]
            if bscMethods.OsFile.isExist(astSolverExtraFile):
                extraDic = bscMethods.OsJson.read(astSolverExtraFile)
                if extraDic:
                    connectionDic = extraDic.get(prsConfigure.Product.DEF_key_info_connection)
                    if connectionDic:
                        maFur.setScAstSolverGuideConnectToCfx(connectionDic, scAstCfxNamespace, scAstSolverNamespace)
                    nhrConnectionDic = extraDic.get(prsConfigure.Product.DEF_key_info_nhrconnection)
                    if nhrConnectionDic:
                        maFur.setScAstCfxConnectToSolver(nhrConnectionDic, scAstCfxNamespace, scAstSolverNamespace)
            #
        if withAstSolverCache:
            scUnitAstSolverCacheConnectCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                withAstSolverCache=withAstSolverCache
            )
        #
        scAstCfxReferenceNode = scenePr.scAstCfxReferenceNode(sceneName, sceneVariant, assetName, number)
        if maUtils._isNodeExist(scAstCfxReferenceNode):
            maUtils.setUnloadReference(scAstCfxReferenceNode)


#
def scUnitAstSolverCacheConnectCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withAstSolverCache
):
    def getFile():
        fileString = None
        if isinstance(withAstSolverCache, bool):
            if withAstSolverCache is True:
                fileString = scenePr.getScAstSolverCacheActive(
                    projectName,
                    sceneName, sceneVariant,
                    assetName, number
                )
        elif isinstance(withAstSolverCache, str) or isinstance(withAstSolverCache, unicode):
            fileString = withAstSolverCache
        #
        if fileString is not None:
            if bscMethods.OsFile.isExist(fileString):
                return fileString
    logWin_ = bscObjects.LogWindow()
    #
    scAstSolverCacheFile = getFile()
    #
    if scAstSolverCacheFile is not None:
        scAstSolverNamespace = scenePr.scAstSolverNamespace(sceneName, sceneVariant, assetName, number)
        scAstSolverCacheNamespace = scenePr.scAstSolverCacheNamespace(sceneName, sceneVariant, assetName, number)
        #
        astSolverLinkGroup = prsMethods.Asset.solverLinkGroupName(assetName, scAstSolverNamespace)
        astSolverBridgeGroup = assetPr.astUnitSolverBridgeGroupName(assetName, scAstSolverCacheNamespace)
        # Load
        if not maUtils._isNodeExist(astSolverBridgeGroup):
            maFile.setCacheFileReference(scAstSolverCacheFile, scAstSolverCacheNamespace)
        else:
            scAstSolverCacheReferenceNode = scenePr.scAstSolverCacheReferenceNode(sceneName, sceneVariant, assetName, number)
            maUtils.setLoadReferenceFile(scAstSolverCacheReferenceNode, scAstSolverCacheFile)
        # Connect
        if maUtils._isNodeExist(astSolverLinkGroup) and maUtils._isNodeExist(astSolverBridgeGroup):
            errorLis = maFur.setScAstSolverCurveConnectToSolverCache(assetName, scAstSolverNamespace, scAstSolverCacheNamespace)
            if errorLis:
                [logWin_.addError(i) for i in errorLis]
    else:
        logWin_.addWarning(u'Asset Solver ( Cache ) is Non - Exists')


# CFX Fur Cache(s) Connect
def scUnitAstCfxFurCachesConnectCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        withAstCfxFurCache
):
    logWin_ = bscObjects.LogWindow()
    
    scAstCfxNamespace = scenePr.scAstCfxNamespace(sceneName, sceneVariant, assetName, number)
    #
    furObjectLis = datScene.getScAstCfxFurObjects(assetName, scAstCfxNamespace)
    #
    if furObjectLis:
        progressExplain = u'Load Scene Asset Character FX ( Fur Cache )'
        maxValue = len(furObjectLis)
        progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
        for furObject in furObjectLis:
            progressBar.update()
            #
            scUnitAstCfxFurCacheConnectSubCmd(
                projectName,
                sceneIndex,
                sceneCategory, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetCategory, assetName, number, assetVariant,
                furObject,
                withAstCfxFurCache
            )


# CFX Fur Cache Sub
def scUnitAstCfxFurCacheConnectSubCmd(
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        furObject,
        withAstCfxFurCache
):
    def getFile():
        fileString = None
        if isinstance(withAstCfxFurCache, bool):
            if withAstCfxFurCache is True:
                # Yeti
                if furObjectType == appCfg.MaNodeType_Plug_Yeti:
                    _furCacheFile, _furSolverMode, _startFrame, _endFrame = scenePr.getScAstCfxYetiCacheExists(
                        projectName,
                        sceneName, sceneVariant, assetName, number,
                        assetVariant,
                        furObjectLabel
                    )
                # Hair System
                elif furObjectType == appCfg.MaHairSystemType:
                    _furCacheFile, _furSolverMode, _startFrame, _endFrame = scenePr.getScAstCfxGeomCacheExists(
                        projectName,
                        sceneName, sceneVariant, assetName, number,
                        assetVariant,
                        furObjectLabel
                    )
                # Nurbs Hair
                elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
                    _furCacheFile, _furSolverMode, _startFrame, _endFrame = scenePr.getScAstCfxNurbsHairCacheExists(
                        projectName,
                        sceneName, sceneVariant, assetName, number,
                        assetVariant,
                        furObjectLabel
                    )
                else:
                    _furCacheFile = None
                #
                fileString = _furCacheFile
        elif isinstance(withAstCfxFurCache, str) or isinstance(withAstCfxFurCache, unicode):
            fileString = withAstCfxFurCache
        #
        if fileString is not None:
            if bscMethods.OsMultifile.isExist(fileString):
                return fileString
    logWin_ = bscObjects.LogWindow()
    #
    furObjectLabel = maFur.getFurObjectLabel(furObject, assetName)
    furObjectType = maUtils._getNodeShapeTypeString(furObject)
    furCacheFile = getFile()
    if furCacheFile:
        logWin_.addStartProgress(u'Fur Cache Load', furCacheFile)
        # Yeti
        if furObjectType == appCfg.MaNodeType_Plug_Yeti:
            maFur.setYetiConnectCache(
                furObject, furCacheFile
            )
        # Hair System
        elif furObjectType == appCfg.MaHairSystemType:
            cachePath = os.path.dirname(furCacheFile)
            cacheName = furObjectLabel
            #
            maFur.setGeometryObjectInCache(
                cachePath, cacheName,
                furObject
            )
        # Nurbs Hair
        elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
            maFur.setNurbsHairConnectCache(
                furObject, furCacheFile
            )
        #
        logWin_.addCompleteProgress()


#
def scUnitSceneryExtraLoadLoadCmd(
        projectName,
        sceneCategory, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscObjects.LogWindow()
    #
    extraData = scenePr.getScSceneryExtraData(
        projectName,
        sceneCategory, sceneName, sceneVariant
    )
    scSceneryLinkPath = scenePr.scScenerySubGroupPath(sceneName, sceneVariant, sceneStage)
    if not maUtils._isNodeExist(scSceneryLinkPath):
        maUtils.setAppPathCreate(scSceneryLinkPath)
    #
    if extraData:
        logWin_.addStartProgress(u'Scenery Extra Load')
        #
        if prsConfigure.Product.DEF_key_info_asbreference in extraData:
            data = extraData[prsConfigure.Product.DEF_key_info_asbreference]
            sceneOp.setCreateScSceneryAssembly(data, scSceneryLinkPath)
        #
        if prsConfigure.Product.DEF_key_info_transformation in extraData:
            data = extraData[prsConfigure.Product.DEF_key_info_transformation]
            sceneOp.setScSceneryAsbTransformation(data)
        #
        if scenePr.isLightLinkName(sceneStage):
            sceneryOp.setAssembliesActiveSwitch('Proxy')
        #
        logWin_.addCompleteProgress()
    #
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if maUtils._isNodeExist(scUnitRoot):
        scLikGroupName = scenePr.scUnitLinkGroupName(sceneName, sceneVariant, sceneStage)
        maUtils.setObjectParent(scLikGroupName, scUnitRoot)
