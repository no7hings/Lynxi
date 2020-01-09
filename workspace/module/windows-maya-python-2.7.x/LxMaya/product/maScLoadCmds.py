# coding=utf-8
import os

from LxBasic import bscMethods, bscModifiers

from LxCore import lxBasic, lxCore_

from LxCore.config import appCfg

from LxCore.preset import appVariant

from LxCore.preset.prod import assetPr, scenePr

from LxCore.method._osMethod import OsMultFileMethod

from LxMaya.command import maUtils, maFile, maHier, maPreference, maFur, maCacheConnect, maRender

from LxMaya.product.data import datScene

from LxMaya.product.op import sceneOp, sceneryOp

astDefaultVersion = appVariant.astDefaultVersion

none = ''


@bscModifiers.fncCatchException
@bscModifiers.fncCatchCostTime
def scUnitSceneCreateMainCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        withCamera=False, withScenery=False,
        withFrame=False, withSize=False,
        withAstModel=False, withModelCache=False,
        withAstCfx=False, withAstCfxFurCache=False,
        withAstSolver=False, withAstSolverCache=False,
        withExtraCache=False
):
    sceneStagePrettify = sceneStage.capitalize()
    #
    logWin_ = bscMethods.If_Log(u'{} Create'.format(sceneStagePrettify))
    logWin_.showUi()
    #
    maUtils.setDisplayMode(5)
    #
    maPreference.setAnimationTimeUnit(projectName)
    # Layout
    if scenePr.isScLayoutLink(sceneStage):
        maHier.setCreateScLinkHierarchy(sceneClass, sceneName, sceneVariant, sceneStage)
    # Animation
    elif scenePr.isScAnimationLink(sceneStage):
        serverProductFile = scenePr.sceneUnitProductFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, sceneClass, sceneName, sceneVariant, lxCore_.LynxiProduct_Scene_Link_layout
        )[1]
        localSourceFile = scenePr.sceneUnitSourceFile(
            lxCore_.LynxiRootIndex_Local,
            projectName, sceneClass, sceneName, sceneVariant, lxCore_.LynxiScAnimationStages[0]
        )[1]
        maFile.openMayaFileToLocal(serverProductFile, localSourceFile)
    # Simulation
    elif scenePr.isScSimulationLink(sceneStage):
        maHier.setCreateScLinkHierarchy(sceneClass, sceneName, sceneVariant, sceneStage)
        # Asset Model Cache
        scUnitAstModelCachesLoadCmd(
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage
        )
        # Asset Mode Pose Cache
        scUnitAstModelPoseCachesLoadCmd(
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage
        )
    # Solver
    elif scenePr.isScSolverLink(sceneStage):
        # Load Animation
        maHier.setCreateScLinkHierarchy(sceneClass, sceneName, sceneVariant, sceneStage)
        #
        scUnitAssetsLoadCmd(
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            withAstModel=withAstModel, withModelCache=withModelCache,
            withAstCfx=withAstCfx, withAstCfxFurCache=withAstCfxFurCache,
            withAstSolver=withAstSolver, withAstSolverCache=withAstSolverCache,
            withExtraCache=withExtraCache,
        )
    # Light
    elif scenePr.isScLightLink(sceneStage):
        maHier.setCreateScLinkHierarchy(sceneClass, sceneName, sceneVariant, sceneStage)
        #
        scUnitAssetsLoadCmd(
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            withAstModel=withAstModel, withModelCache=withModelCache,
            withAstCfx=withAstCfx, withAstCfxFurCache=withAstCfxFurCache,
            withAstSolver=withAstSolver, withAstSolverCache=withAstSolverCache,
            withExtraCache=withExtraCache,
        )
    #
    maHier.refreshScRoot(sceneClass, sceneName, sceneVariant, sceneStage, sceneIndex)
    # is Used Default Camera
    if withCamera:
        logWin_.addStartProgress(u'Camera Create')
        if scenePr.isScLayoutLink(sceneStage):
            sceneCamera = scenePr.scSceneCameraName(sceneName, sceneVariant)
            if not maUtils.isAppExist(sceneCamera):
                sceneOp.setCreateSceneCamera(sceneName, sceneVariant)
            #
            sceneOp.setAddSceneCameras(sceneName, [maUtils._getNodePathString(sceneCamera)])
        # Simulation and Light
        elif scenePr.isScSolverLink(sceneStage) or scenePr.isScSimulationLink(sceneStage) or scenePr.isScLightLink(sceneStage):
            scUnitCameraCachesLoadCmd(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage
            )
            if scenePr.isScLightLink(sceneStage):
                scOutputCameras = scenePr.getOutputCameras(
                    projectName,
                    sceneClass, sceneName, sceneVariant
                )
                maRender.setRenderCamera(scOutputCameras)
        #
        logWin_.addCompleteProgress()
    # Load Scenery
    if withScenery:
        if scenePr.isScSimulationLink(sceneStage) or scenePr.isScSolverLink(sceneStage) or scenePr.isScLightLink(sceneStage):
            scUnitSceneryExtraLoadLoadCmd(
                projectName,
                sceneClass, sceneName, sceneVariant, sceneStage
            )
    # Frame
    if withFrame:
        logWin_.addStartProgress(u'Render Frame Create')
        #
        if scenePr.isScLayoutLink(sceneStage):
            startFrame, endFrame = withFrame
            maUtils.setAnimationFrameRange(startFrame, endFrame)
        #
        elif scenePr.isScSimulationLink(sceneStage) or scenePr.isScSolverLink(sceneStage) or scenePr.isScLightLink(sceneStage):
            startFrame, endFrame = scenePr.getScUnitFrameRange(
                projectName, sceneClass, sceneName, sceneVariant
            )
            if scenePr.isScSimulationLink(sceneStage) or scenePr.isScSolverLink(sceneStage):
                startFrame -= 50
            # Frame Range
            maUtils.setAnimationFrameRange(startFrame, endFrame)
            # Current Frame
            maUtils.setCurrentFrame(startFrame)
            #
            if scenePr.isScLightLink(sceneStage):
                maRender.setRenderTime(startFrame, endFrame)
                maRender.setAnimationFrameMode()
        #
        logWin_.addCompleteProgress()
    # Size
    if withSize:
        logWin_.addStartProgress(u'Render Size Create')
        #
        if scenePr.isScLayoutLink(sceneStage):
            width, height = withSize
            maUtils.setRenderSize(width, height)
        #
        elif scenePr.isScSolverLink(sceneStage) or scenePr.isScSimulationLink(sceneStage) or scenePr.isScLightLink(sceneStage):
            width = appVariant.rndrImageWidth
            height = appVariant.rndrImageHeight
            #
            maUtils.setRenderSize(width, height)
        #
        logWin_.addCompleteProgress()
    # Set Workspace
    if scenePr.isScLightLink(sceneStage):
        workspaceRoot = scenePr.scUnitRenderFolder(
            lxCore_.LynxiRootIndex_Local,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage, appVariant.scDefaultCustomizeLabel
        )
        maRender.setCreateWorkspace(workspaceRoot)
        #
        maRender.setImagePath(maRender.MaRender_DefaultImageFilePrefix)
    # TD Command
    tdCommand = scenePr.getScTdLoadCommand(projectName, scenePr.getSceneLink(sceneStage))
    if tdCommand:
        maUtils.runMelCommand(tdCommand)
    # Save to Local
    scUnitSourceSaveCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage
    )
    logWin_.addCompleteTask()


#
def scUnitFrameLoadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscMethods.If_Log()
    #
    startFrame, endFrame = scenePr.getScUnitFrameRange(
        projectName,
        sceneClass, sceneName, sceneVariant
    )
    # Time Unit
    maPreference.setAnimationTimeUnit(projectName)
    #
    if scenePr.isScSimulationLink(sceneStage) or scenePr.isScSolverLink(sceneStage):
        maUtils.setAnimationFrameRange(startFrame - 50, endFrame)
    else:
        maUtils.setAnimationFrameRange(startFrame, endFrame)
    # Current Frame
    maUtils.setCurrentFrame(startFrame)
    #
    maRender.setRenderTime(startFrame, endFrame)
    maRender.setAnimationFrameMode()


@bscModifiers.fncCatchException
def scUnitSceneLoadMainCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        withFrame=False, withSize=False
):
    sceneStagePrettify = sceneStage.capitalize()

    logWin_ = bscMethods.If_Log(u'{} Load'.format(sceneStagePrettify))
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'{} Load'.format(sceneStagePrettify))
    logWin_.showUi()
    #
    maUtils.setDisplayMode(5)
    #
    serverProductFile = scenePr.sceneUnitProductFile(
        lxCore_.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    localSourceFile = scenePr.sceneUnitSourceFile(
        lxCore_.LynxiRootIndex_Local,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    logWin_.addStartProgress(u'Source Load')
    #
    maFile.openMayaFileToLocal(serverProductFile, localSourceFile)
    #
    if not scenePr.isScAnimationLink(sceneStage):
        maHier.setCreateScLinkHierarchy(sceneClass, sceneName, sceneVariant, sceneStage)
    #
    maHier.refreshScRoot(sceneClass, sceneName, sceneVariant, sceneStage, sceneIndex)
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
        sceneClass, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscMethods.If_Log()
    
    localSourceFile = scenePr.sceneUnitSourceFile(
        lxCore_.LynxiRootIndex_Local,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
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
        sceneClass, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscMethods.If_Log()
    
    datumDic = scenePr.getSceneCameraIndexDataDic(
        projectName, sceneClass, sceneName, sceneVariant
    )
    if datumDic:
        for k, v in datumDic.items():
            progressExplain = u'''Load Scene Camera Cache'''
            maxValue = len(v)
            progressBar = bscMethods.If_Progress(progressExplain, maxValue)
            for seq, i in enumerate(v):
                progressBar.update()
                #
                timestamp, cacheStage, startFrame, endFrame, scCameraCache = i
                #
                if timestamp is not None:
                    subLabel = lxBasic.getSubLabel(seq)
                    scUnitCameraCacheLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant, sceneStage, subLabel,
                        withCameraCache=True
                    )


#
def scUnitCameraCacheLoadSubCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage, subLabel,
        withCameraCache
):
    def getFile():
        fileString = None
        if isinstance(withCameraCache, bool):
            if withCameraCache is True:
                fileString = scenePr.getScCameraCacheActive(
                    projectName,
                    sceneName, sceneVariant,
                    subLabel
                )
        elif isinstance(withCameraCache, str) or isinstance(withCameraCache, unicode):
            fileString = withCameraCache
        #
        if fileString is not None:
            if lxBasic.isOsExist(fileString):
                return fileString
    #
    logWin_ = bscMethods.If_Log()
    
    scCameraCacheFile = getFile()
    #
    if scCameraCacheFile is not None:
        #
        linkCameraPath = scenePr.scCameraSubGroupPath(sceneName, sceneVariant, sceneStage)
        scCameraNamespace = scenePr.scCameraNamespace(
            sceneName, sceneVariant
        ) + subLabel
        #
        scOutputCameraLocator = scenePr.scOutputCameraLocatorName(sceneName, sceneVariant, scCameraNamespace) + subLabel
        if maUtils.isAppExist(scOutputCameraLocator):
            maUtils.setNodesClearByNamespace(scCameraNamespace)
            #
            logWin_.addResult(u'Remove Exists', )
        #
        logWin_.addStartProgress('Camera Cache Load', scCameraCacheFile)
        #
        maFile.setAlembicCacheImport(scCameraCacheFile, scCameraNamespace)
        #
        logWin_.addCompleteProgress()
        #
        if maUtils.isAppExist(linkCameraPath):
            maUtils.setObjectParent(scOutputCameraLocator, linkCameraPath)
        #
        scCamera = scenePr.scOutputCameraName(sceneName, sceneVariant, scCameraNamespace) + subLabel
        if maUtils.isAppExist(scCamera):
            maUtils.setDisplayMode(5)
            maUtils.setCameraView(scCamera)
            maUtils.setObjectLockTransform(scCamera, boolean=True)
            bscMethods.If_Message(u'''Set Camera View''', u'''Complete''')
    else:
        logWin_.addWarning(u'Scene Camera ( Cache ) is Non - Exists')


# Model Cache
def scUnitAstModelCachesLoadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        withAstCfx=False, withAstCfxFurCache=False
):
    logWin_ = bscMethods.If_Log()
    
    datumDic = scenePr.getSceneAssetIndexDataDic(
        projectName,
        sceneClass, sceneName, sceneVariant
    )
    if datumDic:
        for k, v in datumDic.items():
            progressExplain = u'''Load Scene Asset Model Cache'''
            maxValue = len(v)
            progressBar = bscMethods.If_Progress(progressExplain, maxValue)
            for i in v:
                progressBar.update()
                #
                (
                    timestamp, cacheStage, startFrame, endFrame, cache,
                    assetIndex, assetClass, assetName, number, assetVariant
                 ) = i
                #
                if timestamp is not None:
                    scUnitAstModelCacheLoadSubCmd(
                        projectName,
                        sceneIndex,
                        sceneClass, sceneName, sceneVariant, sceneStage,
                        assetIndex,
                        assetClass, assetName, number, assetVariant,
                        withModelCache=True
                    )


#
def scUnitAstModelCacheLoadSubCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        assetIndex,
        assetClass, assetName, number, assetVariant,
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
            if lxBasic.isOsExist(fileString):
                return fileString
    #
    logWin_ = bscMethods.If_Log()
    
    scAstModelCacheFile = getFile()
    if scAstModelCacheFile is not None:
        # Create Scene Root
        scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
        if not maUtils.isAppExist(scUnitRoot):
            maHier.setCreateScLinkHierarchy(sceneClass, sceneName, sceneVariant, sceneStage)
            maHier.refreshScRoot(sceneClass, sceneName, sceneVariant, sceneStage, sceneIndex)
        #
        scAstSubPath = scenePr.scAssetSubGroupPath(sceneName, sceneVariant, sceneStage)
        #
        scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        scAstUnitRootGroup = assetPr.astUnitRootGroupName(assetName)
        #
        astModelGroup = assetPr.astUnitModelLinkGroupName(assetName)
        scAstModelGroup = scenePr.scAstModelGroupName(sceneName, sceneVariant, assetName, number)
        if maUtils.isAppExist(scAstModelGroup):
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
        timeTag = lxBasic.getOsActiveTimeTag()
        maHier.refreshScAstUnitBranch(
            scAstRootGroup,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            timeTag
        )
        #
        if maUtils.isAppExist(scAstSubPath):
            maUtils.setObjectParent(scAstRootGroup, scAstSubPath)
    else:
        logWin_.addWarning(u'Scene Model ( Cache ) is Non - Exists')


# Model Pose Cache(s)
def scUnitAstModelPoseCachesLoadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscMethods.If_Log()
    
    datumDic = scenePr.getSceneAssetIndexDataDic(
        projectName, sceneClass, sceneName, sceneVariant
    )
    if datumDic:
        for k, v in datumDic.items():
            progressExplain = u'''Load Scene Asset Model ( Pose Cache )'''
            maxValue = len(v)
            progressBar = bscMethods.If_Progress(progressExplain, maxValue)
            for i in v:
                progressBar.update()
                #
                (
                    timestamp, cacheStage, startFrame, endFrame, _,
                    assetIndex, assetClass, assetName, number, assetVariant
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
                    assetClass, assetName, number, assetVariant,
                    cache
                )


# Model Pose Cache Sub
def scUnitAstModelPoseCacheLoadSubCmd(
        projectName,
        sceneIndex,
        sceneName, sceneVariant, sceneStage,
        assetIndex,
        assetClass, assetName, number, assetVariant,
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
            if lxBasic.isOsExist(fileString):
                return fileString
    logWin_ = bscMethods.If_Log()
    #
    scAstModelPoseCacheFile = getFile()
    if scAstModelPoseCacheFile is not None:
        scAstSimNamespace = scenePr.scAstSimulationNamespace(sceneName, sceneVariant, assetName, number)
        scAstModelGroup = assetPr.astUnitModelLinkGroupName(assetName, scAstSimNamespace)
        if maUtils.isAppExist(scAstModelGroup):
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
        sceneClass, sceneName, sceneVariant, sceneStage,
        withAstModel=False, withModelCache=False,
        withAstCfx=False, withAstCfxFurCache=False,
        withAstSolver=False, withAstSolverCache=False,
        withExtraCache=False
):
    logWin_ = bscMethods.If_Log()
    
    datumDic = scenePr.getSceneAssetIndexDataDic(
        projectName, sceneClass, sceneName, sceneVariant
    )
    if datumDic:
        for k, v in datumDic.items():
            progressExplain = u'''Load Scene Asset(s)'''
            maxValue = len(v)
            progressBar = bscMethods.If_Progress(progressExplain, maxValue)
            for i in v:
                progressBar.update()
                #
                (
                    timestamp, cacheStage,
                    startFrame, endFrame, scAstModelCache,
                    assetIndex,
                    assetClass, assetName, number, assetVariant
                ) = i
                #
                scUnitAssetLoadSubCmd(
                    projectName,
                    sceneIndex,
                    sceneClass, sceneName, sceneVariant, sceneStage,
                    startFrame, endFrame,
                    assetIndex, assetClass, assetName, number, assetVariant,
                    withAstModel=withAstModel, withModelCache=withModelCache,
                    withAstCfx=withAstCfx, withAstCfxFurCache=withAstCfxFurCache,
                    withAstSolver=withAstSolver, withAstSolverCache=withAstSolverCache,
                    withExtraCache=withExtraCache
                )


# Asset Sub
def scUnitAssetLoadSubCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        withAstModel=False, withModelCache=False,
        withAstCfx=False, withAstCfxFurCache=False,
        withAstSolver=False, withAstSolverCache=False,
        withExtraCache=False,
        usePoolAsset=False,
        isOffset=False, isLoop=False
):
    logWin_ = bscMethods.If_Log()
    
    # Create Scene Root
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if not maUtils.isAppExist(scUnitRoot):
        maHier.setCreateScLinkHierarchy(sceneClass, sceneName, sceneVariant, sceneStage)
        maHier.refreshScRoot(sceneClass, sceneName, sceneVariant, sceneStage, sceneIndex)
    #
    scAstSubPath = scenePr.scAssetSubGroupPath(sceneName, sceneVariant, sceneStage)
    #
    scAstRootPath = scenePr.scAstRootGroupPath(sceneName, sceneVariant, assetName, number)
    if not maUtils.isAppExist(scAstRootPath):
        # Create Group
        maUtils.setAppPathCreate(scAstRootPath)
        #
        timeTag = lxBasic.getOsActiveTimeTag()
        #
        maHier.refreshScAstUnitBranch(
            scAstRootPath,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            timeTag
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
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                withAstModel=withAstModel, withModelCache=withModelCache,
                usePoolAsset=usePoolAsset
            )
        # CFX
        if withAstCfx is True:
            scUnitAstCfxProductLoadCmd(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                withAstCfxFurCache=withAstCfxFurCache,
                usePoolAsset=usePoolAsset
            )
        #
        if withAstSolver is True:
            scUnitAstSolverProductLoadCmd(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                withAstSolverCache=withAstSolverCache
            )
        # Extra
        if withExtraCache:
            scUnitAstExtraCacheConnectCmd(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                withAstRigExtraCache=True
            )
        #
        logWin_.addCompleteProgress()
    else:
        assetShowName = appVariant.assetTreeViewName(assetName, number, assetVariant)
        logWin_.addWarning(assetShowName, u'Asset is Exists')
    #
    maUtils.setObjectParent(scAstRootPath, scAstSubPath)


#
def scUnitAstModelProductLoadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        withAstModel=False, withModelCache=False,
        usePoolAsset=False
):
    def getProductFile():
        fileString = None
        if isinstance(withAstModel, bool):
            if withAstModel is True:
                fileString = assetPr.astUnitProductFile(
                    lxCore_.LynxiRootIndex_Server,
                    projectName, assetClass, assetName, assetVariant, assetStage
                )[1]
        elif isinstance(withAstModel, str) or isinstance(withAstModel, unicode):
            fileString = withAstModel
        #
        if fileString is not None:
            if lxBasic.isOsExist(fileString):
                return fileString
    logWin_ = bscMethods.If_Log()
    #
    maPreference.setAnimationTimeUnit(projectName)
    #
    assetStage = lxCore_.LynxiProduct_Asset_Link_Model
    #
    astModelProductFile = getProductFile()
    if astModelProductFile is not None:
        timeTag = lxBasic.getOsFileMtimeTag(astModelProductFile)
        #
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        scAstModelGroup = assetPr.astUnitModelLinkGroupName(assetName, scAstModelNamespace)
        scAstModelContainer = assetPr.astModelContainerName(assetName, scAstModelNamespace)
        # Clean Exists
        if maUtils.isAppExist(scAstModelGroup):
            if appVariant.rndrUseReference is True:
                scAstModelReferenceNode = scenePr.scAstModelReferenceNode(sceneName, sceneVariant, assetName, number)
                #
                maUtils.setReferenceRemove(scAstModelReferenceNode)
                maUtils.setNamespaceRemove(scAstModelNamespace)
            else:
                maUtils.setNodesClearByNamespace(scAstModelNamespace)
            #
            logWin_.addResult(u'Clean Exists',)
        # Load Product
        logWin_.addStartProgress('Model Product Load', astModelProductFile)
        #
        if appVariant.rndrUseReference is True:
            maFile.setMaFileReference(astModelProductFile, scAstModelNamespace)
        else:
            maFile.setAlembicCacheImport(astModelProductFile, scAstModelNamespace)
        #
        logWin_.addCompleteProgress()
        # Refresh Root
        maHier.scUnitRefreshRoot(
            assetIndex,
            assetClass, assetName, assetVariant, assetStage,
            timeTag,
            scAstModelNamespace
        )
        # Load Cache
        if withModelCache is not False:
            scUnitAstModelCacheConnectCmd(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
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
        if maUtils.isAppExist(scAstRootGroup):
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
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
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
            if lxBasic.isOsExist(fileString):
                return fileString
    logWin_ = bscMethods.If_Log()
    
    cacheFile = getFile()
    #
    if cacheFile is not None:
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        scAstModelCacheNamespace = scenePr.scAstModelCacheNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstModelGroup = assetPr.astUnitModelLinkGroupName(assetName, scAstModelNamespace)
        if maUtils.isAppExist(scAstModelGroup):
            scAstModelCacheGroup = assetPr.astUnitModelLinkGroupName(assetName, scAstModelCacheNamespace)
            if not maUtils.isAppExist(scAstModelCacheGroup):
                # Clear Cache Nde_Node
                connectMethod = maCacheConnect.LxAstModelCacheConnectMethod(assetName, scAstModelCacheNamespace, scAstModelNamespace)
                #
                connectMethod.setSourceClear()
                #
                logWin_.addStartProgress('Model Cache Load', cacheFile)
                #
                maFile.setAlembicCacheImport(cacheFile, scAstModelCacheNamespace)
                #
                logWin_.addCompleteProgress()
                #
                logWin_.addStartProgress('Cache Connect')
                #
                connectMethod.connect()
                #
                connectionLis = connectMethod.connectionLis
                if connectionLis:
                    scAstModelReferenceNode = scenePr.scAstModelReferenceNode(sceneName, sceneVariant, assetName, number)
                    if maUtils.isAppExist(scAstModelReferenceNode):
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
                alembicNode = lxBasic.getOsFileName(cacheFile) + '_AlembicNode'
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
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
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
            if lxBasic.isOsExist(fileString):
                return fileString
    logWin_ = bscMethods.If_Log()
    #
    scAstRigExtraCacheFile = getFile()
    if scAstRigExtraCacheFile is not None:
        scAstExtraCacheNamespace = scenePr.scAstExtraNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        astRigBridgeGroup = assetPr.astUnitRigBridgeGroupName(assetName, scAstExtraCacheNamespace)
        #
        if maUtils.isAppExist(astRigBridgeGroup):
            maUtils.setNodesClearByNamespace(scAstExtraCacheNamespace)
            #
            logWin_.addResult(u'Clean Exists', )
        #
        logWin_.addStartProgress('Extra Cache Load', scAstRigExtraCacheFile)
        #
        maFile.setAlembicCacheImport(scAstRigExtraCacheFile, scAstExtraCacheNamespace)
        #
        logWin_.addCompleteProgress()
        #
        if maUtils.isAppExist(scAstRootGroup):
            maUtils.setObjectParent(astRigBridgeGroup, scAstRootGroup)
    else:
        logWin_.addWarning(scenePr.scAstName(assetName, number, assetVariant), u'Asset Extra Cache is Non - Exists')


# Character FX
def scUnitAstCfxProductLoadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        withAstCfxFurCache=False,
        usePoolAsset=False
):
    logWin_ = bscMethods.If_Log()
    
    maPreference.setAnimationTimeUnit(projectName)
    #
    assetStage = lxCore_.LynxiProduct_Asset_Link_Cfx
    #
    astCfxProductFile = assetPr.astUnitProductFile(
        lxCore_.LynxiRootIndex_Server,
        projectName, assetClass, assetName, assetVariant, assetStage
    )[1]
    if lxBasic.isOsExistsFile(astCfxProductFile):
        timeTag = lxBasic.getOsFileMtimeTag(astCfxProductFile)
        #
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        scAstCfxNamespace = scenePr.scAstCfxNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstRootGroup = scenePr.scAstRootGroupName(sceneName, sceneVariant, assetName, number)
        astCfxGroup = assetPr.astUnitCfxLinkGroupName(assetName, scAstCfxNamespace)
        scAstCfxContainer = assetPr.astCfxContainerName(assetName, scAstCfxNamespace)
        if not maUtils.isAppExist(astCfxGroup):
            logWin_.addStartProgress(u'Groom Product Load', astCfxProductFile)
            #
            if appVariant.rndrUseReference is True:
                maFile.setMaFileReference(astCfxProductFile, scAstCfxNamespace)
            else:
                maFile.setAlembicCacheImport(astCfxProductFile, scAstCfxNamespace)
            #
            logWin_.addCompleteProgress()
            # Refresh Root
            maHier.scUnitRefreshRoot(
                assetIndex,
                assetClass, assetName, assetVariant, assetStage,
                timeTag,
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
                    sceneClass, sceneName, sceneVariant, sceneStage,
                    startFrame, endFrame,
                    assetIndex,
                    assetClass, assetName, number, assetVariant,
                    withAstCfxFurCache=withAstCfxFurCache
                )
        #
        if maUtils.isAppExist(scAstRootGroup):
            maUtils.setObjectParent(astCfxGroup, scAstRootGroup)
            maUtils.setObjectParent(scAstCfxContainer, scAstRootGroup)
        #
        else:
            logWin_.addWarning(u'Asset CFX is Exists' )


#
def scUnitAstSolverProductLoadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        withAstSolverCache=False
):
    logWin_ = bscMethods.If_Log()
    
    astSolverProductFile = assetPr.astUnitProductFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Solver
    )[1]
    if lxBasic.isOsExistsFile(astSolverProductFile):
        scAstModelNamespace = scenePr.scAstModelNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstCfxNamespace = scenePr.scAstCfxNamespace(sceneName, sceneVariant, assetName, number)
        #
        scAstSolverNamespace = scenePr.scAstSolverNamespace(sceneName, sceneVariant, assetName, number)
        #
        astSolverLinkGroup = assetPr.astUnitCfxLinkGroupName(assetName, scAstSolverNamespace)
        if not maUtils.isAppExist(astSolverLinkGroup):
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
                lxCore_.LynxiRootIndex_Server,
                projectName,
                assetClass, assetName, assetVariant, lxCore_.LynxiProduct_Asset_Link_Solver
            )[1]
            if lxBasic.isOsExist(astSolverExtraFile):
                extraDic = lxBasic.readOsJson(astSolverExtraFile)
                if extraDic:
                    connectionDic = extraDic.get(lxCore_.LynxiConnectionDataKey)
                    if connectionDic:
                        maFur.setScAstSolverGuideConnectToCfx(connectionDic, scAstCfxNamespace, scAstSolverNamespace)
                    nhrConnectionDic = extraDic.get(lxCore_.LynxiNhrConnectionDataKey)
                    if nhrConnectionDic:
                        maFur.setScAstCfxConnectToSolver(nhrConnectionDic, scAstCfxNamespace, scAstSolverNamespace)
            #
        if withAstSolverCache:
            scUnitAstSolverCacheConnectCmd(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                withAstSolverCache=withAstSolverCache
            )
        #
        scAstCfxReferenceNode = scenePr.scAstCfxReferenceNode(sceneName, sceneVariant, assetName, number)
        if maUtils.isAppExist(scAstCfxReferenceNode):
            maUtils.setUnloadReference(scAstCfxReferenceNode)


#
def scUnitAstSolverCacheConnectCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
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
            if lxBasic.isOsExist(fileString):
                return fileString
    logWin_ = bscMethods.If_Log()
    #
    scAstSolverCacheFile = getFile()
    #
    if scAstSolverCacheFile is not None:
        scAstSolverNamespace = scenePr.scAstSolverNamespace(sceneName, sceneVariant, assetName, number)
        scAstSolverCacheNamespace = scenePr.scAstSolverCacheNamespace(sceneName, sceneVariant, assetName, number)
        #
        astSolverLinkGroup = assetPr.astUnitSolverLinkGroupName(assetName, scAstSolverNamespace)
        astSolverBridgeGroup = assetPr.astUnitSolverBridgeGroupName(assetName, scAstSolverCacheNamespace)
        # Load
        if not maUtils.isAppExist(astSolverBridgeGroup):
            maFile.setCacheFileReference(scAstSolverCacheFile, scAstSolverCacheNamespace)
        else:
            scAstSolverCacheReferenceNode = scenePr.scAstSolverCacheReferenceNode(sceneName, sceneVariant, assetName, number)
            maUtils.setLoadReferenceFile(scAstSolverCacheReferenceNode, scAstSolverCacheFile)
        # Connect
        if maUtils.isAppExist(astSolverLinkGroup) and maUtils.isAppExist(astSolverBridgeGroup):
            errorLis = maFur.setScAstSolverCurveConnectToSolverCache(assetName, scAstSolverNamespace, scAstSolverCacheNamespace)
            if errorLis:
                [logWin_.addError(i) for i in errorLis]
    else:
        logWin_.addWarning(u'Asset Solver ( Cache ) is Non - Exists')


# CFX Fur Cache(s) Connect
def scUnitAstCfxFurCachesConnectCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        withAstCfxFurCache
):
    logWin_ = bscMethods.If_Log()
    
    scAstCfxNamespace = scenePr.scAstCfxNamespace(sceneName, sceneVariant, assetName, number)
    #
    furObjectLis = datScene.getScAstCfxFurObjects(assetName, scAstCfxNamespace)
    #
    if furObjectLis:
        progressExplain = u'Load Scene Asset Character FX ( Fur Cache )'
        maxValue = len(furObjectLis)
        progressBar = bscMethods.If_Progress(progressExplain, maxValue)
        for furObject in furObjectLis:
            progressBar.update()
            #
            scUnitAstCfxFurCacheConnectSubCmd(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                assetIndex,
                assetClass, assetName, number, assetVariant,
                furObject,
                withAstCfxFurCache
            )


# CFX Fur Cache Sub
def scUnitAstCfxFurCacheConnectSubCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
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
            if OsMultFileMethod.isOsExistsMultiFile(fileString):
                return fileString
    logWin_ = bscMethods.If_Log()
    #
    furObjectLabel = maFur.getFurObjectLabel(furObject, assetName)
    furObjectType = maUtils.getShapeType(furObject)
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
        sceneClass, sceneName, sceneVariant, sceneStage
):
    logWin_ = bscMethods.If_Log()
    #
    extraData = scenePr.getScSceneryExtraData(
        projectName,
        sceneClass, sceneName, sceneVariant
    )
    scSceneryLinkPath = scenePr.scScenerySubGroupPath(sceneName, sceneVariant, sceneStage)
    if not maUtils.isAppExist(scSceneryLinkPath):
        maUtils.setAppPathCreate(scSceneryLinkPath)
    #
    if extraData:
        logWin_.addStartProgress(u'Scenery Extra Load')
        #
        if lxCore_.LynxiAssemblyReferenceDataKey in extraData:
            data = extraData[lxCore_.LynxiAssemblyReferenceDataKey]
            sceneOp.setCreateScSceneryAssembly(data, scSceneryLinkPath)
        #
        if lxCore_.LynxiTransformationDataKey in extraData:
            data = extraData[lxCore_.LynxiTransformationDataKey]
            sceneOp.setScSceneryAsbTransformation(data)
        #
        if scenePr.isScLightLink(sceneStage):
            sceneryOp.setAssembliesActiveSwitch('Proxy')
        #
        logWin_.addCompleteProgress()
    #
    scUnitRoot = scenePr.scUnitRootGroupName(sceneName)
    if maUtils.isAppExist(scUnitRoot):
        scLikGroupName = scenePr.scUnitLinkGroupName(sceneName, sceneVariant, sceneStage)
        maUtils.setObjectParent(scLikGroupName, scUnitRoot)
