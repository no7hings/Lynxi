# coding=utf-8
import os

from LxBasic import bscMethods, bscModifiers

from LxCore import lxBasic, lxCore_

from LxCore.config import appCfg
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import assetPr, scenePr
#
from LxCore.product.op import messageOp
#
from LxMaya.command import maUtils, maFile, maFur, maPrv, maRender, maDir
#
from LxMaya.product.data import datScene
#
from LxMaya.product.op import sceneOp
#
from LxDeadline.command import ddlUtil

#
astDefaultVersion = appVariant.astDefaultVersion
#
animAlembicStep = appVariant.animAlembicStep
#
isSendMail = lxCore_.LynxiIsSendMail
isSendDingTalk = lxCore_.LynxiIsSendDingTalk
#
none = ''


@bscModifiers.fncCatchException
def scUnitAnimationUploadMainCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        description, notes,
        #
        withIndex=False,
        withPreview=False, withCamera=False, withAsset=False, withScenery=False,
):
    # Set Log Window
    logWin_ = bscMethods.If_Log(title=u'Animation Upload')
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Animation Upload')
    maUtils.setDisplayMode(5)
    #
    methodDatumLis = [
        (
            'Upload / Update Source', True, scUnitSourceUploadCmd, (
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                timeTag,
                description, notes
            )
        ),
        (
            'Upload / Update Product', True, scUnitProductUploadCmd, (
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                timeTag
            )
        ),
        (
            'Upload / Update Index', withIndex, scUnitIndexUploadCmd, (
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame, frameOffset,
                timeTag,
                withIndex
            )
        ),
        (
            'Upload / Update Camera(s)', withCamera, scUnitCamerasUploadCmd, (
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame, frameOffset,
                timeTag,
                withCamera
            )
        ),
        (
            'Upload / Update Preview(s)', withPreview, scUnitPreviewsUploadCmd, (
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame, frameOffset,
                timeTag,
                withPreview
            )
        ),
        (
            'Upload / Update Asset(s)', withAsset, scUnitAssetCachesUploadCmd, (
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame, frameOffset,
                timeTag,
                description, notes,
                withAsset
            )
        ),
        (
            'Upload / Update Scenery(s)', withScenery, scUnitSceneriesUploadCmd,(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                timeTag,
                withScenery
            )
        ),
        (
            'Open Source', True, scUnitSourceOpenCmd, (
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                timeTag
            )
        )
    ]
    maxValue = len(methodDatumLis) + 1
    logWin_.setMaxProgressValue(maxValue)
    maUtils.setVisiblePanelsDelete()
    for i in methodDatumLis:
        explain, enable, method, args = i
        logWin_.addStartProgress(u'{} Upload'.format(explain))
        if enable is not False:
            method(*args)
            logWin_.addCompleteProgress()
        else:
            logWin_.addWarning(u'{} is Upload Ignore'.format(explain))
    # Complete
    logWin_.addCompleteTask()
    htmlLog = logWin_.htmlLog
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            htmlLog,
            sceneIndex,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage,
            description, notes
        )
    # Send Ding Talk
    if isSendDingTalk:
        messageOp.sendProductMessageByDingTalk(
            sceneIndex,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage,
            timeTag,
            description, notes
        )


@bscModifiers.fncCatchException
def scUnitLightUploadMainCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize,
        timeTag,
        description, notes,
        #
        withRender=False, withDeadline=False
):
    # Set Log Window
    logWin_ = bscMethods.If_Log(title=u'Light Upload')
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Light Upload')
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    # Source
    scUnitSourceUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
        description, notes
    )
    #
    scUnitProductUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag
    )
    #
    if withRender is not False:
        startFrame, endFrame, width, height = withRender
        scUnitRenderUploadCmd(
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            customize,
            timeTag
        )
        scUnitRenderIndexUploadCmd(
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            width, height,
            customize,
            timeTag
        )
        if withDeadline is not False:
            deadlineVars = withDeadline
            #
            scUnitRenderDeadlineSubmitMainCmd(
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                startFrame, endFrame,
                width, height,
                timeTag,
                customize,
                deadlineVars,
                renderLayerOverride=False,
                frameOverride=False,
                melCommand=None
            )
    #
    scUnitSourceOpenCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag
    )
    # Complete
    logWin_.addCompleteTask()
    htmlLog = logWin_.htmlLog
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            htmlLog,
            sceneIndex,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage,
            description, notes
        )
    # Send Ding Talk
    if isSendDingTalk:
        messageOp.sendProductMessageByDingTalk(
            sceneIndex,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage,
            timeTag,
            description, notes
        )


@bscModifiers.fncCatchException
def scUnitAssetsUploadMainCmd_(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        description, notes,
        #
        withAsset
):
    logWin_ = bscMethods.If_Log(title=u'Asset Upload')
    logWin_.showUi()
    # Start
    logWin_.addStartTask(u'Asset Upload')
    maUtils.setDisplayMode(5)
    #
    scUnitAssetCachesUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        description, notes,
        withAsset,
    )
    # Complete
    logWin_.addCompleteTask()
    htmlLog = logWin_.htmlLog
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            htmlLog,
            sceneIndex,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage,
            description, notes
        )
    # Send Ding Talk
    if isSendDingTalk:
        messageOp.sendProductMessageByDingTalk(
            sceneIndex,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage,
            timeTag,
            description, notes
        )


#
def scUnitAstAlembicCacheUploadCmd(
        root,
        indexKey,
        indexFile, cacheFile,
        sceneStage,
        startFrame, endFrame,
        timeTag,
        description=None, notes=None,
        alembicAttrs=None
):
    logWin_ = bscMethods.If_Log()

    startFrame = scenePr.scStartFrame(startFrame)
    endFrame = scenePr.scEndFrame(endFrame)
    #
    step = appVariant.animAlembicStep
    #
    mainLineCacheFile = lxBasic.getOsFileJoinTimeTag(
        cacheFile,
        '0000_0000_0000'
    )
    #
    multLineCacheFile = lxBasic.getOsFileJoinTimeTag(
        cacheFile,
        timeTag
    )
    # Alembic
    maFile.abcExport(
        root,
        multLineCacheFile,
        startFrame, endFrame, step,
        alembicAttrs
    )
    # Information
    infoDic = scenePr.alembicCacheInfoDic(sceneStage, startFrame, endFrame, step, description, notes)
    infoFile = lxBasic.getInfoFile(multLineCacheFile)
    lxBasic.writeOsJson(infoDic, infoFile)
    # Index
    if indexKey is not None:
        cacheIndex = {
            lxCore_.Lynxi_Key_Info_Update: lxBasic.getOsActiveTimestamp(),
            lxCore_.Lynxi_Key_Info_Artist: lxBasic.getOsUser(),
            #
            lxCore_.Lynxi_Key_Info_Stage: sceneStage,
            #
            indexKey: multLineCacheFile
        }
        #
        lxBasic.writeOsJsonDic(cacheIndex, indexFile)
        #
        lxBasic.setOsFileCopy(multLineCacheFile, mainLineCacheFile)
    #
    logWin_.addResult(multLineCacheFile)


#
def uploadScAlembicCache(
        root,
        cacheFile,
        currentFrame,
        timeTag
):
    logWin_ = bscMethods.If_Log()

    step = appVariant.animAlembicStep
    currentFrame = scenePr.scStartFrame(currentFrame)
    #
    mainLineCacheFile = lxBasic.getOsFileJoinTimeTag(
        cacheFile,
        '0000_0000_0000'
    )
    #
    multLineCacheFile = lxBasic.getOsFileJoinTimeTag(
        cacheFile,
        timeTag
    )
    # Alembic
    maFile.abcExport(
        root,
        multLineCacheFile,
        currentFrame, currentFrame, step,
    )
    #
    lxBasic.setOsFileCopy(multLineCacheFile, mainLineCacheFile)
    #
    logWin_.addResult(multLineCacheFile)


#
def uploadScAstMeshData(
        sceneName, sceneVariant, assetName,
        number,
        namespace,
        cache,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    meshDataFile = scenePr.getMeshDataFile(cache)
    #
    mainLineMeshDataFile = lxBasic.getOsFileJoinTimeTag(
        meshDataFile,
        '0000_0000_0000'
    )
    #
    multLineMeshDataFile = lxBasic.getOsFileJoinTimeTag(
        meshDataFile,
        timeTag
    )
    #
    constantData = datScene.getMeshConstantDataByRoot(
        sceneName, sceneVariant,
        assetName, number,
        namespace
    )
    #
    maFile.writeOsJson(constantData, multLineMeshDataFile)
    #
    lxBasic.setOsFileCopy(multLineMeshDataFile, mainLineMeshDataFile)


#
def scUnitSourceUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
        description, notes
):
    logWin_ = bscMethods.If_Log()
    # Source File >>> 01
    backupSourceFile = scenePr.sceneUnitSourceFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    linkFile = lxBasic.getOsFileJoinTimeTag(backupSourceFile, timeTag)
    logWin_.addResult(linkFile)
    #
    maFile.updateMayaFile(linkFile)
    # Update File >>> 02
    updateData = lxCore_.lxProductRecordDatumDic(
        linkFile,
        sceneStage,
        description, notes
    )
    recordFile = lxBasic.getRecordFile(linkFile)
    maFile.writeOsJson(updateData, recordFile, 4)


#
def scUnitSourceOpenCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    # Open Source
    backupFile = scenePr.sceneUnitSourceFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    localFile = scenePr.sceneUnitSourceFile(
        lxCore_.LynxiRootIndex_Local,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    backupSourceFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backupFile, timeTag)
    maFile.openMayaFileToLocal(backupSourceFileJoinUpdateTag, localFile, timeTag)
    logWin_.addResult(localFile)


#
def scUnitProductUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
):
    logWin_ = bscMethods.If_Log()
    # Main Method
    serverProductFile = scenePr.sceneUnitProductFile(
        lxCore_.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    backupProductFile = scenePr.sceneUnitProductFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    maFile.updateMayaFile(serverProductFile)
    logWin_.addResult(serverProductFile)
    # Back File
    lxBasic.backupOsFile(
        serverProductFile, backupProductFile,
        timeTag
    )


# Upload Animation Data
def scUnitIndexUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        withIndex,
):
    def getData(arg):
        data, config = [None] * 2
        if isinstance(arg, bool):
            if arg is True:
                pass
        else:
            data, config = arg
        #
        return data, config

    logWin_ = bscMethods.If_Log()
    #
    if withIndex is not False:
        withCamera, withAsset, withScenery = withIndex
        # Main Method
        serverIndexFile = scenePr.scUnitIndexFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, sceneClass, sceneName, sceneVariant
        )[1]
        backupIndexFile = scenePr.scUnitIndexFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName, sceneClass, sceneName, sceneVariant
        )[1]
        #
        sceneIndexDic = scenePr.scUnitIndexDic(
            sceneIndex, projectName, sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
        )
        #
        cameraIndexDic = scenePr.scUnitCameraIndexDic(
            datScene.getSceneCameraIndexData(sceneName)
        )
        assetIndexDic = scenePr.scUnitAssetIndexDic(
            datScene.getSceneAssetIndexData()
        )
        sceneryIndexDic = scenePr.scUnitSceneryIndexDic(
            datScene.getScSceneryIndexLis(sceneName, sceneVariant, sceneStage)
        )
        #
        lxBasic.writeOsJsonDic(sceneIndexDic, serverIndexFile)
        #
        if withCamera is True:
            lxBasic.writeOsJsonDic(cameraIndexDic, serverIndexFile)
        #
        if withAsset is True:
            lxBasic.writeOsJsonDic(assetIndexDic, serverIndexFile)
        #
        if withScenery is True:
            lxBasic.writeOsJsonDic(sceneryIndexDic, serverIndexFile)
        # Backup File
        lxBasic.backupOsFile(
            serverIndexFile, backupIndexFile,
            timeTag
        )
        #
        logWin_.addResult(serverIndexFile)


# Upload Animation Camera
def scUnitCamerasUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        withCamera
):
    def getData(arg):
        data, config = [None] * 2
        if isinstance(arg, bool):
            if arg is True:
                pass
        else:
            data, config = arg
        #
        return data, config

    def setBranch(cameraObject, subLabel, zAdjust):
        # Camera Locator
        cameraLocator = scenePr.scOutputCameraLocatorName(sceneName, sceneVariant)
        subCameraLocator = cameraLocator + subLabel
        # Camera Product File
        serverProductFile = scenePr.scUnitCameraProductFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        subServerProductFile = lxBasic.getOsSubFile(serverProductFile, subLabel)
        # FBX
        serverCameraFbxFile = scenePr.scUnitCameraFbxFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        subServerCameraFbxFile = lxBasic.getOsSubFile(serverCameraFbxFile, subLabel)
        # Alembic Cache
        serverCameraAlembicCacheFile = scenePr.scUnitCameraAlembicCacheFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant, sceneStage
        )[1]
        subServerCameraAlembicCacheFile = lxBasic.getOsSubFile(serverCameraAlembicCacheFile, subLabel)
        # Cache Index
        cameraCacheIndexFile = scenePr.scCameraCacheIndexFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant
        )[1]
        subCameraCacheIndexFile = lxBasic.getOsSubFile(
            cameraCacheIndexFile, subLabel
        )
        # Bake Camera
        sceneOp.setScCreateOutputCameraMain(
            cameraObject, subLabel,
            sceneClass, sceneName, sceneVariant,
            startFrame, endFrame, frameOffset,
            zAdjust=zAdjust
        )
        maFile.fileExport(subCameraLocator, subServerProductFile)
        logWin_.addResult(subServerProductFile)
        #
        maFile.fbxExport(subCameraLocator, subServerCameraFbxFile)
        logWin_.addResult(subServerProductFile)
        #
        scUnitAstAlembicCacheUploadCmd(
            subCameraLocator,
            lxCore_.LynxiCacheInfoKey,
            subCameraCacheIndexFile, subServerCameraAlembicCacheFile,
            sceneStage,
            startFrame, endFrame,
            timeTag,
        )
    #
    def setMain():
        cameraData, uploadConfig = getData(withCamera)
        sceneCameraLis, usedCameraLis = cameraData
        if cameraData is not None:
            if sceneCameraLis and usedCameraLis:
                zAdjust,  = uploadConfig
                # View Progress
                progressExplain = '''Upload Camera(s)'''
                maxValue = len(usedCameraLis)
                progressBar = bscMethods.If_Progress(progressExplain, maxValue)
                for seq, cameraObject in enumerate(sceneCameraLis):
                    if cameraObject in usedCameraLis:
                        # Sub Progress
                        progressBar.update()
                        #
                        subLabel = lxBasic.getSubLabel(seq)
                        setBranch(cameraObject, subLabel, zAdjust)
            else:
                logWin_.addWarning(u'Camera is Non - Exists')

    logWin_ = bscMethods.If_Log()
    #
    setMain()


# Upload Preview
def scUnitPreviewsUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        withPreview,
):
    def getData(arg):
        data, config = [None] * 2
        if isinstance(arg, bool):
            if arg is True:
                pass
        else:
            data, config = arg
        #
        return data, config

    def setBranch(cameraObject, subLabel, percent, quality, width, height, vedioFormat, displayMode, useMode):
        # Get Camera
        outputCamera = scenePr.scOutputCameraName(sceneName, sceneVariant) + subLabel
        previewCamera = cameraObject
        if maUtils.isAppExist(outputCamera):
            previewCamera = outputCamera
        # Preview File
        servePreviewFile = scenePr.scenePreviewFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, sceneClass, sceneName, sceneVariant, sceneStage, vedioFormat
        )[1]
        backupPreviewFile = scenePr.scenePreviewFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName, sceneClass, sceneName, sceneVariant, sceneStage, vedioFormat
        )[1]
        if useMode == 1:
            localPreviewFile = scenePr.scenePreviewFile(
                lxCore_.LynxiRootIndex_Local,
                projectName, sceneClass, sceneName, sceneVariant, sceneStage, vedioFormat
            )[1]
            servePreviewFile = lxBasic.getOsFileJoinTimeTag(localPreviewFile)
        # Index File
        serverPreviewIndexFile = scenePr.scenePreviewIndexFile(
            lxCore_.LynxiRootIndex_Server,
            projectName, sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        subSeverPreviewFile = lxBasic.getOsSubFile(servePreviewFile, subLabel)
        subBackupPreviewFile = lxBasic.getOsSubFile(backupPreviewFile, subLabel)
        subServerPreviewIndexFile = lxBasic.getOsSubFile(serverPreviewIndexFile, subLabel)
        #
        imagePreviews = maPrv.makePreview(
            osFile=subSeverPreviewFile,
            camera=previewCamera,
            useDefaultMaterial=1,
            percent=percent,
            quality=quality,
            startFrame=startFrame,
            endFrame=endFrame,
            widthHeight=(width, height),
            displayMode=displayMode
        )
        if useMode == 0:
            lxBasic.backupOsFile(
                subSeverPreviewFile, subBackupPreviewFile,
                timeTag
            )
        #
        logWin_.addResult(subSeverPreviewFile)

    def setMain():
        cameraData, uploadConfig = getData(withPreview)
        if cameraData is not None:
            sceneCameraLis, usedCameraLis = cameraData
            if sceneCameraLis and usedCameraLis:
                percent, quality, width, height, vedioFormat, displayMode, useMode = uploadConfig
                # View Progress
                progressExplain = '''Upload Preview(s)'''
                maxValue = len(usedCameraLis)
                progressBar = bscMethods.If_Progress(progressExplain, maxValue)
                #
                maUtils.setDefaultShaderColor(.5, .5, .5)
                for seq, cameraObject in enumerate(sceneCameraLis):
                    if cameraObject in usedCameraLis:
                        # Sub Progress
                        progressBar.update()
                        #
                        subLabel = lxBasic.getSubLabel(seq)
                        setBranch(cameraObject, subLabel, percent, quality, width, height, vedioFormat, displayMode, useMode)
            else:
                logWin_.addWarning(u'Camera is Non - Exists')

    logWin_ = bscMethods.If_Log()

    setMain()


#
def scUnitSoundUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
):
    logWin_ = bscMethods.If_Log()

    serverFile = scenePr.sceneSoundFile(
        lxCore_.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    backupFile = scenePr.sceneSoundFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    #
    sounds = datScene.getSceneSounds()
    if sounds:
        for seq, i in enumerate(sounds):
            pass


#
def scUnitAssetCachesUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        description, notes,
        withAsset
):
    def getData(arg):
        data, config = [None] * 2
        if isinstance(arg, bool):
            if arg is True:
                pass
        else:
            data, config = arg
        #
        return data, config
    #
    def setBranch(value):
        assetClass, assetName, number, assetVariant, keyNode = value
        #
        if maUtils.getNodeType(keyNode) == appCfg.MaReferenceType:
            namespace = maUtils.getReferenceNamespace(keyNode)
        else:
            namespace = maUtils._toNamespaceByNodePath(keyNode)
        # Render
        astModelLinkRoot, astExtraSubRoot, astSolverSubRoot = [None]*3
        if scenePr.isScLayoutLink(sceneStage) or scenePr.isScAnimationLink(sceneStage):
            astModelLinkRoot = assetPr.astUnitModelLinkGroupName(assetName, namespace)
            #
            astExtraSubRoot = assetPr.astUnitRigBridgeGroupName(assetName, namespace)
            astSolverSubRoot = assetPr.astUnitSolverBridgeGroupName(assetName, namespace)
        elif scenePr.isScSimulationLink(sceneStage):
            astModelLinkRoot = scenePr.scAstModelGroupName(sceneName, sceneVariant, assetName, number, namespace)
        #
        astCacheIndexFile = scenePr.scAstCacheIndexFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant, assetName, number
        )[1]
        # Model Cache
        if astModelLinkRoot is not None:
            if isWithModelCache is True:
                if maUtils.isAppExist(astModelLinkRoot):
                    # Use for Solver
                    if isModelCacheUseForSolver is True:
                        scAstModelCacheFile = scenePr.scAstModelAlembicCacheFile(
                            lxCore_.LynxiRootIndex_Server,
                            projectName,
                            sceneName, sceneVariant, lxCore_.LynxiProduct_Scene_Link_Solver,
                            assetName, number
                        )[1]
                        scAstModelCacheIndexKey = None
                    else:
                        scAstModelCacheFile = scenePr.scAstModelAlembicCacheFile(
                            lxCore_.LynxiRootIndex_Server,
                            projectName,
                            sceneName, sceneVariant, sceneStage,
                            assetName, number
                        )[1]
                        scAstModelCacheIndexKey = lxCore_.LynxiCacheInfoKey
                    # Alembic Cache Sequence
                    scUnitAstAlembicCacheUploadCmd(
                        astModelLinkRoot,
                        scAstModelCacheIndexKey,
                        astCacheIndexFile, scAstModelCacheFile,
                        sceneStage,
                        startFrame, endFrame,
                        timeTag,
                        description, notes
                    )
                    # Upload Data
                    uploadScAstMeshData(
                        sceneName, sceneVariant,
                        assetName, number,
                        namespace,
                        scAstModelCacheFile,
                        timeTag
                    )
                    #
                    scAstModelPoseCache = scenePr.scAstModelPoseAlembicCacheFile(
                        lxCore_.LynxiRootIndex_Server,
                        projectName,
                        sceneName, sceneVariant,
                        assetName, number
                    )[1]
                    # Alembic Cache
                    uploadScAlembicCache(
                        astModelLinkRoot,
                        scAstModelPoseCache,
                        startFrame,
                        timeTag
                    )
                else:
                    logWin_.addError(u'Asset Model ( Mesh Root ) is Non - Exists')
        # Extra Cache
        if astExtraSubRoot is not None:
            if isWithRigExtraCache is True and isModelCacheUseForSolver is False:
                if maUtils.isAppExist(astExtraSubRoot):
                    astRigExtraCacheFile = scenePr.scAstRigExtraAlembicCacheFile(
                        lxCore_.LynxiRootIndex_Server,
                        projectName,
                        sceneName, sceneVariant,
                        assetName, number
                    )[1]
                    #
                    alembicAttrs = datScene.getScAstRigAlembicAttrData(
                        projectName,
                        assetClass, assetName, assetVariant
                    )
                    scUnitAstAlembicCacheUploadCmd(
                        astExtraSubRoot,
                        lxCore_.LynxiExtraCacheInfoKey,
                        astCacheIndexFile, astRigExtraCacheFile,
                        sceneStage,
                        startFrame, endFrame,
                        timeTag,
                        description, notes,
                        alembicAttrs=alembicAttrs
                    )
                else:
                    logWin_.addError(u'Asset Rig ( Extra Root ) is Non - Exists')
        # Solver Cache
        if astSolverSubRoot is not None:
            if isWithSolverCache is True:
                if maUtils.isAppExist(astSolverSubRoot):
                    assetSolverCacheFile = scenePr.scAstSolverAlembicCacheFile(
                        lxCore_.LynxiRootIndex_Server,
                        projectName,
                        sceneName, sceneVariant, lxCore_.LynxiProduct_Scene_Link_Solver,
                        assetName, number
                    )[1]
                    # Alembic Cache Sequence
                    scUnitAstAlembicCacheUploadCmd(
                        astSolverSubRoot,
                        lxCore_.LynxiSolverCacheInfoKey,
                        astCacheIndexFile, assetSolverCacheFile,
                        sceneStage,
                        startFrame, endFrame,
                        timeTag,
                        description, notes
                    )
                else:
                    logWin_.addError(u'Asset Rig ( Solver Root ) is Non - Exists')
    #
    logWin_ = bscMethods.If_Log()

    assetData, uploadConfig = getData(withAsset)
    if assetData:
        if len(uploadConfig) == 2:
            (isWithModelCache, isWithSolverCache, isWithRigExtraCache), isModelCacheUseForSolver = uploadConfig
        else:
            isWithModelCache, isWithSolverCache, isWithRigExtraCache = uploadConfig
            isModelCacheUseForSolver = False
        #
        startFrame -= 80
        # View Progress
        progressExplain = '''Upload Asset Cache(s)'''
        maxValue = len(assetData)
        progressBar = bscMethods.If_Progress(progressExplain, maxValue)
        for seq, i in enumerate(assetData):
            # Progress
            progressBar.update()
            #
            setBranch(i)
    else:
        logWin_.addWarning(u'Asset is Non - Exists')


#
def scUnitSceneriesUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
        withScenery
):
    logWin_ = bscMethods.If_Log()
    # Main Method
    if withScenery is not False:
        withExtra,  = withScenery
        if withExtra is True:
            sceneryExtraData = datScene.getScSceneryExtraData(sceneName, sceneVariant, sceneStage)
            if sceneryExtraData:
                sceneryExtraFile = scenePr.scUnitSceneryExtraFile(
                    lxCore_.LynxiRootIndex_Server,
                    projectName, sceneClass, sceneName, sceneVariant, sceneStage
                )[1]
                backupExtraFile = scenePr.scUnitSceneryExtraFile(
                    lxCore_.LynxiRootIndex_Backup,
                    projectName, sceneClass, sceneName, sceneVariant, sceneStage
                )[1]
                lxBasic.writeOsJsonDic(
                    sceneryExtraData,
                    sceneryExtraFile
                )
                lxBasic.backupOsFile(
                    sceneryExtraFile, backupExtraFile,
                    timeTag
                )
            else:
                logWin_.addWarning(u'Scenery is Non - Exists')


#
def scUnitSceneryComposeUploadCmd_(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
):
    logWin_ = bscMethods.If_Log()

    data = datScene.getScAssemblyComposeDatumLis(sceneName, sceneVariant, sceneStage)
    if data:
        serverFile = scenePr.scUnitAssemblyComposeFile(
            lxCore_.LynxiRootIndex_Server,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        backupFile = scenePr.scUnitAssemblyComposeFile(
            lxCore_.LynxiRootIndex_Backup,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        #
        lxBasic.writeOsJson(
            data,
            serverFile
        )
        lxBasic.backupOsFile(
            serverFile, backupFile,
            timeTag
        )


@bscModifiers.fncCatchException
def uploadScAstCfxFurCache(
        furCacheDataArray,
        useExistsCache=True
):
    logWin_ = bscMethods.If_Log()

    cacheType = 'OneFile'
    cacheFormat = 'mcx'
    if furCacheDataArray:
        # View Progress
        progressExplain = '''Uploading Asset ( CFX ) Cache'''
        maxValue = len(furCacheDataArray)
        progressBar = bscMethods.If_Progress(progressExplain, maxValue)
        yetiObjects = []
        yetiCaches = []
        yetiStartFrame = None
        yetiEndFrame = None
        yetiSample = None
        for seq, data in enumerate(furCacheDataArray):
            #
            furObject, furObjectName, furObjectType, furCacheFile, furCacheIndex, furCacheIndexFile, startFrame, endFrame, sample, solverMode = data
            # Progress
            progressBar.update(furObjectName)
            #
            startFrame = scenePr.scStartFrame(startFrame)
            endFrame = scenePr.scEndFrame(endFrame)
            # Yeti
            if furObjectType == appCfg.MaNodeType_Plug_Yeti:
                yetiObjects.append(furObject)
                yetiCaches.append(furCacheFile)
                yetiStartFrame = startFrame
                yetiEndFrame = endFrame
                yetiSample = sample
            # Hair System
            elif furObjectType == appCfg.MaHairSystemType:
                shapePath = maUtils.getNodeShape(furObject)
                #
                cachePath = os.path.dirname(furCacheFile)
                cacheName = furObjectName
                #
                if not useExistsCache:
                    maFur.setOutGeometryCache(
                        cachePath, cacheName, shapePath,
                        startFrame, endFrame, sample,
                        cacheType=cacheType, cacheFormat=cacheFormat
                    )
                    #
                    maFur.setGeometryObjectInCache(
                        cachePath, cacheName, shapePath, solverMode
                    )
                #
                else:
                    maFur.setUploadExistsGeometryCache(
                        cachePath, cacheName,
                        shapePath
                    )
                #
                if os.path.isfile(furCacheFile):
                    maFur.setGeometryObjectInCache(
                        cachePath, cacheName,
                        shapePath, solverMode
                    )
            # Nurbs Hair Solver
            elif furObjectType == appCfg.MaNodeType_Plug_NurbsHair:
                shapePath = maUtils.getNodeShape(furObject)
                #
                cachePath = os.path.dirname(furCacheFile)
                cacheName = furObjectName
                #
                if not useExistsCache:
                    pass
                else:
                    maFur.setUploadExistsNurbsHairCache(
                        cachePath, cacheName,
                        shapePath
                    )
            #
            lxBasic.writeOsJson(furCacheIndex, furCacheIndexFile, 4)
        # Concurrent
        if yetiObjects:
            if not useExistsCache:
                maFur.setYetiObjectsWriteCache(
                    yetiObjects, yetiCaches,
                    yetiStartFrame, yetiEndFrame, yetiSample,
                    isUpdateViewport=False, isGeneratePreview=False
                )
            else:
                maFur.setYetiObjectsWriteCache(
                    yetiObjects, yetiCaches,
                    yetiStartFrame, yetiEndFrame, yetiSample,
                    isUpdateViewport=False, isGeneratePreview=False
                )


#
def scUnitRenderUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize,
        timeTag,
):
    logWin_ = bscMethods.If_Log()

    serverRenderFile = scenePr.scUnitRenderFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage, customize
    )[1]
    backupRenderFile = scenePr.scUnitRenderFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage, customize
    )[1]
    #
    logWin_.addStartProgress(u'Upload / Update Scene Render ( {} ) File'.format(
        lxBasic.str_camelcase2prettify(sceneStage)))
    #
    maFile.saveMayaFile(serverRenderFile)
    # Back File
    lxBasic.backupOsFile(
        serverRenderFile, backupRenderFile,
        timeTag
    )
    #
    logWin_.addResult(serverRenderFile)
    #
    logWin_.addCompleteProgress()


@bscModifiers.fncCatchException
def scUnitRenderIndexUploadCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        width, height,
        customize,
        timeTag,
):
    logWin_ = bscMethods.If_Log()

    serverRenderFile = scenePr.scUnitRenderFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    #
    serverRenderIndexFile = scenePr.sceUnitRenderIndexFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    backupRenderIndexFile = scenePr.sceUnitRenderIndexFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    #
    serverRenderPath = scenePr.scUnitRenderFolder(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )
    #
    imagePrefix = maRender.getImagePrefix()
    #
    maUtils.setCurrentFrame(startFrame)
    #
    composeFileLis = maDir.getComposeFileLis(
        withCurrent=False,
        withTexture=True,
        withFurMap=True,
        withReference=True,
        withAssemblyReference=True,
        withProxyCache=True,
        withVolumeCache=True,
        withGpuCache=True,
        withAlembicCache=True,
        withFurCache=True,
        withGeomCache=True,
        withTx=True
    )
    composeFileLis.insert(0, serverRenderFile)
    imageFileLis = maRender.getImageFileLis(sceneRoot=serverRenderPath, sceneNameOverride=lxBasic.getOsFileName(serverRenderFile))
    #
    renderData = scenePr.getScRenderIndexData(
        sceneIndex,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        width, height,
        imagePrefix,
        composeFileLis,
        imageFileLis
    )
    logWin_.addStartProgress(u'Upload / Update Scene Render ( {} ) Index'.format(
        lxBasic.str_camelcase2prettify(sceneStage)))
    #
    lxBasic.writeOsJson(renderData, serverRenderIndexFile, 4)
    lxBasic.backupOsFile(serverRenderIndexFile, backupRenderIndexFile, timeTag)
    #
    logWin_.addCompleteProgress()


#
def scUnitRenderDeadlineSubmitMainCmd(
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        width, height,
        timeTag,
        customize,
        deadlineVars,
        renderLayerOverride=False,
        frameOverride=False,
        melCommand=None,
):
    logWin_ = bscMethods.If_Log()
    # Render File
    serverRenderFile = scenePr.scUnitRenderFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    # Info
    serverDeadlineInfoFile = scenePr.scDeadlineInfoFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    # Job
    serverDeadlineJobFile = scenePr.scDeadlineJobFile(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    #
    serverRenderPath = scenePr.scUnitRenderFolder(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )
    serverRenderImagePath = scenePr.scUnitRenderImageFolder(
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )
    #
    renderer = maRender.getCurrentRenderer()
    # Render Layer
    if renderLayerOverride is not False:
        renderLayerLis = renderLayerOverride
    else:
        renderLayerLis = maRender.getRenderableRenderLayers()
    # Frame
    if frameOverride is not False:
        frameLis = frameOverride
    else:
        frameLis = range(startFrame, endFrame + 1)
    #
    imagePrefix = maRender.getImagePrefix()
    #
    composeFileLis = maDir.getComposeFileLis(
        withCurrent=False,
        withTexture=True,
        withFurMap=True,
        withReference=True,
        withAssemblyReference=True,
        withProxyCache=True,
        withVolumeCache=True,
        withGpuCache=True,
        withAlembicCache=True,
        withFurCache=True,
        withGeomCache=True,
        withTx=True
    )
    #
    ddlJobType, ddlJobPool, ddlJobPriority, ddlJobTimeout, ddlJobMachineLimit, ddlJobAbortError, ddlJobSizePercent = deadlineVars
    # Reduce Size
    logWin_.addStartProgress(u'Submit Deadline Job(s) ( {} ) '.format(lxBasic.str_camelcase2prettify(sceneStage)))
    if renderLayerLis:
        batchName = scenePr.scDeadlineBatchName(
            projectName,
            sceneName, sceneVariant,
            customize, ddlJobType
        )
        # View Progress
        progressExplain = u'''Submit Deadline Job(s)'''
        maxValue = len(renderLayerLis)
        progressBar = bscMethods.If_Progress(progressExplain, maxValue)
        for seq, currentRenderLayer in enumerate(renderLayerLis):
            progressBar.update(currentRenderLayer)
            # Switch Render Layer First
            maRender.setCurrentRenderLayer(currentRenderLayer)
            # Get Render Size Override
            width, height = maRender.getRenderSize()
            width, height = int(width * ddlJobSizePercent), int(height * ddlJobSizePercent)
            # Get Camera Override
            renderableCameraLis = maRender.getRenderableCameraLis()
            #
            subLabel = '.' + currentRenderLayer
            #
            jobName = scenePr.scDeadlineJobName(currentRenderLayer, startFrame, endFrame, width, height, timeTag)
            imageFileLis = maRender.getImageFileLis(sceneRoot=serverRenderPath, renderLayerOverride=currentRenderLayer)
            #
            subInfoData, subJobData = ddlUtil.getDdlMayaBatchData(
                batchName=batchName, jobName=jobName,
                scenePath=serverRenderPath, sceneFile=serverRenderFile,
                composeFiles=composeFileLis,
                imagePath=serverRenderImagePath, imageFiles=imageFileLis,
                imagePrefix=imagePrefix,
                isAnimationEnable=maRender.isAnimationEnable(), isRenderLayerEnable=maRender.isRenderLayerEnable(), isRenderSetupEnable=maRender.isRenderSetupEnable(),
                renderer=renderer,
                frames=frameLis,
                width=width, height=height,
                mayaVersion=maUtils.getMayaVersion(), is64=maUtils.is64(),
                batchType=ddlJobType,
                pool=ddlJobPool, jobPriority=ddlJobPriority, taskTimeout=ddlJobTimeout, machineLimit=ddlJobMachineLimit,
                currentCamera='', cameras=maUtils.getCameras(), renderableCameras=renderableCameraLis,
                currentRenderLayer=currentRenderLayer,
                arnoldVerbose=ddlJobAbortError,
                melCommand=melCommand
            )
            serverSubDeadlineInfoFile = lxBasic.getOsSubFile(serverDeadlineInfoFile, subLabel)
            serverSubDeadlineJobFile = lxBasic.getOsSubFile(serverDeadlineJobFile, subLabel)
            #
            logWin_.addStartProgress(u'Submit Deadline Job for Layer : {}'.format(currentRenderLayer))
            #
            scUnitDeadlineJobSubmitCmd(
                subInfoData,
                subJobData,
                serverSubDeadlineInfoFile,
                serverSubDeadlineJobFile,
                timeTag
            )
            #
            logWin_.addCompleteProgress()
    #
    logWin_.addCompleteProgress()


#
def scUnitDeadlineJobSubmitCmd(
        infoData, jobData,
        infoFile, jobFile,
        timeTag
):
    logWin_ = bscMethods.If_Log()
    # Info
    mainLineInfoFile = lxBasic.getOsFileJoinTimeTag(infoFile, lxCore_.LynxiMainTimeTag, useMode=1)
    multLineInfoFile = lxBasic.getOsFileJoinTimeTag(infoFile, timeTag, useMode=1)
    lxBasic.writeOsData(infoData, multLineInfoFile)
    lxBasic.backupOsFile(multLineInfoFile, mainLineInfoFile)
    logWin_.addResult(multLineInfoFile)
    # Job
    mainLineJobFile = lxBasic.getOsFileJoinTimeTag(jobFile, lxCore_.LynxiMainTimeTag, useMode=1)
    multLineJobFile = lxBasic.getOsFileJoinTimeTag(jobFile, timeTag, useMode=1)
    lxBasic.writeOsData(jobData, multLineJobFile)
    lxBasic.backupOsFile(multLineJobFile, mainLineJobFile)
    logWin_.addResult(multLineJobFile)
    #
    if multLineInfoFile and multLineJobFile:
        # Test Boolean
        enable = True
        if enable is True:
            result = ddlUtil.runDdlJob(multLineInfoFile, multLineJobFile)
            if result:
                for i in result:
                    if not i.startswith('\r\n'):
                        logWin_.addResult(i)
            #
            resultFile = lxCore_._toLxProductResultFile(multLineJobFile)
            #
            lxBasic.writeOsData(result, resultFile)
    else:
        logWin_.addError('Write Deadline Info and Job Error')

