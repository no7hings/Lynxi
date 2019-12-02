# coding=utf-8
import os
#
from LxCore import lxBasic, lxConfigure, lxProgress, lxLog, lxTip
#
from LxCore.config import appCfg
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import projectPr, assetPr, sceneryPr, scenePr
#
from LxCore.product.op import messageOp
#
from LxMaya.command import maUtils, maFile, maFur, maKeyframe, maMshBox, maAsb, maPrv, maAnim, maRender, maDir
#
from LxMaya.product.data import datAsset, datScenery, datScene, datAnim
#
from LxMaya.product.op import sceneryOp, sceneOp
#
from LxDeadline import deadlineOp
#
astDefaultVersion = appVariant.astDefaultVersion
#
animAlembicStep = appVariant.animAlembicStep
#
isSendMail = lxConfigure.LynxiIsSendMail
isSendDingTalk = lxConfigure.LynxiIsSendDingTalk
#
none = ''


@lxTip.viewExceptionMethod
def scUnitAnimationUploadMainCmd(
        logWin,
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
    logWin.setNameText(description)
    # Start
    lxLog.viewStartUploadMessage(logWin)
    maUtils.setDisplayMode(5)
    #
    methodDatumLis = [
        (
            'Upload / Update Source', True, scUnitSourceUploadCmd, (
                logWin,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                timeTag,
                description, notes
            )
        ),
        (
            'Upload / Update Product', True, scUnitProductUploadCmd, (
                logWin,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                timeTag
            )
        ),
        (
            'Upload / Update Index', withIndex, scUnitIndexUploadCmd, (
                logWin,
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
                logWin,
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
                logWin,
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
                logWin,
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
                logWin,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                timeTag,
                withScenery
            )
        ),
        (
            'Open Source', True, scUnitSourceOpenCmd, (
                logWin,
                projectName,
                sceneIndex,
                sceneClass, sceneName, sceneVariant, sceneStage,
                timeTag
            )
        )
    ]
    maxValue = len(methodDatumLis) + 1
    logWin.setMaxProgressValue(maxValue)
    maUtils.setVisiblePanelsDelete()
    for i in methodDatumLis:
        explain, enable, method, args = i
        lxLog.viewStartProcess(logWin, '''{} ( {} )'''.format(explain, lxBasic._toStringPrettify(sceneStage)))
        if enable is not False:
            method(*args)
            lxLog.viewCompleteProcess(logWin)
        else:
            lxLog.viewWarning(logWin, '''{} is Ignore'''.format(explain))
    # Complete
    lxLog.viewCompleteUploadMessage(logWin)
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            logWin,
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


@lxTip.viewExceptionMethod
def scUnitLightUploadMainCmd(
        logWin,
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
    logWin.setNameText(description)
    # Start
    lxLog.viewStartUploadMessage(logWin)
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    # Source
    scUnitSourceUploadCmd(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
        description, notes
    )
    #
    scUnitProductUploadCmd(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag
    )
    #
    if withRender is not False:
        startFrame, endFrame, width, height = withRender
        scUnitRenderUploadCmd(
            logWin,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            customize,
            timeTag
        )
        scUnitRenderIndexUploadCmd(
            logWin,
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
                logWin,
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
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag
    )
    # Complete
    lxLog.viewCompleteUploadMessage(logWin)
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            logWin,
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


@lxTip.viewExceptionMethod
def scUnitAssetsUploadMainCmd_(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        description, notes,
        #
        withAsset
):
    logWin.setNameText(description)
    # Start
    lxLog.viewStartUploadMessage(logWin)
    maUtils.setDisplayMode(5)
    #
    scUnitAssetCachesUploadCmd(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame, frameOffset,
        timeTag,
        description, notes,
        withAsset,
    )
    # Complete
    lxLog.viewCompleteUploadMessage(logWin)
    # Close Log Window
    logWin.setCountdownClose(5)
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            logWin,
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
        logWin,
        root,
        indexKey,
        indexFile, cacheFile,
        sceneStage,
        startFrame, endFrame,
        timeTag,
        description=None, notes=None,
        alembicAttrs=None
):
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
            lxConfigure.Lynxi_Key_Info_Update: lxBasic.getOsActiveTimestamp(),
            lxConfigure.Lynxi_Key_Info_Artist: lxBasic.getOsUser(),
            #
            lxConfigure.Lynxi_Key_Info_Stage: sceneStage,
            #
            indexKey: multLineCacheFile
        }
        #
        lxBasic.writeOsJsonDic(cacheIndex, indexFile)
        #
        lxBasic.setOsFileCopy(multLineCacheFile, mainLineCacheFile)
    #
    lxLog.viewResult(logWin, multLineCacheFile)


#
def uploadScAlembicCache(
        logWin,
        root,
        cacheFile,
        currentFrame,
        timeTag
):
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
    lxLog.viewResult(logWin, multLineCacheFile)


#
def uploadScAstMeshData(
        sceneName, sceneVariant, assetName,
        number,
        namespace,
        cache,
        timeTag):
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
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
        description, notes
):
    # Source File >>> 01
    backupSourceFile = scenePr.sceneUnitSourceFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    linkFile = lxBasic.getOsFileJoinTimeTag(backupSourceFile, timeTag)
    lxLog.viewResult(logWin, linkFile)
    #
    maFile.updateMayaFile(linkFile)
    # Update File >>> 02
    updateData = lxConfigure.lxProductRecordDatumDic(
        linkFile,
        sceneStage,
        description, notes
    )
    recordFile = lxBasic.getRecordFile(linkFile)
    maFile.writeOsJson(updateData, recordFile, 4)


#
def scUnitSourceOpenCmd(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag
):
    # Open Source
    backupFile = scenePr.sceneUnitSourceFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    localFile = scenePr.sceneUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    backupSourceFileJoinUpdateTag = lxBasic.getOsFileJoinTimeTag(backupFile, timeTag)
    maFile.openMayaFileToLocal(backupSourceFileJoinUpdateTag, localFile, timeTag)
    lxLog.viewResult(logWin, localFile)


#
def scUnitProductUploadCmd(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
):
    # Main Method
    serverProductFile = scenePr.sceneUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    backupProductFile = scenePr.sceneUnitProductFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    maFile.updateMayaFile(serverProductFile)
    lxLog.viewResult(logWin, serverProductFile)
    # Back File
    lxBasic.backupOsFile(
        serverProductFile, backupProductFile,
        timeTag
    )


# Upload Animation Data
def scUnitIndexUploadCmd(
        logWin,
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
    #
    if withIndex is not False:
        withCamera, withAsset, withScenery = withIndex
        # Main Method
        serverIndexFile = scenePr.scUnitIndexFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, sceneClass, sceneName, sceneVariant
        )[1]
        backupIndexFile = scenePr.scUnitIndexFile(
            lxConfigure.LynxiRootIndex_Backup,
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
        lxLog.viewResult(logWin, serverIndexFile)


# Upload Animation Camera
def scUnitCamerasUploadCmd(
        logWin,
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
    #
    def setBranch(cameraObject, subLabel, zAdjust):
        # Camera Locator
        cameraLocator = scenePr.scOutputCameraLocatorName(sceneName, sceneVariant)
        subCameraLocator = cameraLocator + subLabel
        # Camera Product File
        serverProductFile = scenePr.scUnitCameraProductFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        subServerProductFile = lxBasic.getOsSubFile(serverProductFile, subLabel)
        # FBX
        serverCameraFbxFile = scenePr.scUnitCameraFbxFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        subServerCameraFbxFile = lxBasic.getOsSubFile(serverCameraFbxFile, subLabel)
        # Alembic Cache
        serverCameraAlembicCacheFile = scenePr.scUnitCameraAlembicCacheFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneName, sceneVariant, sceneStage
        )[1]
        subServerCameraAlembicCacheFile = lxBasic.getOsSubFile(serverCameraAlembicCacheFile, subLabel)
        # Cache Index
        cameraCacheIndexFile = scenePr.scCameraCacheIndexFile(
            lxConfigure.LynxiRootIndex_Server,
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
        lxLog.viewResult(logWin, subServerProductFile)
        #
        maFile.fbxExport(subCameraLocator, subServerCameraFbxFile)
        lxLog.viewResult(logWin, subServerProductFile)
        #
        scUnitAstAlembicCacheUploadCmd(
            logWin,
            subCameraLocator,
            lxConfigure.LynxiCacheInfoKey,
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
                progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
                for seq, cameraObject in enumerate(sceneCameraLis):
                    if cameraObject in usedCameraLis:
                        # Sub Progress
                        progressBar.updateProgress()
                        #
                        subLabel = lxBasic.getSubLabel(seq)
                        setBranch(cameraObject, subLabel, zAdjust)
            else:
                lxLog.viewWarning(
                    logWin,
                    u'Camera is Non - Exists'
                )
    #
    setMain()


# Upload Preview
def scUnitPreviewsUploadCmd(
        logWin,
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
    #
    def setBranch(cameraObject, subLabel, percent, quality, width, height, vedioFormat, displayMode, useMode):
        # Get Camera
        outputCamera = scenePr.scOutputCameraName(sceneName, sceneVariant) + subLabel
        previewCamera = cameraObject
        if maUtils.isAppExist(outputCamera):
            previewCamera = outputCamera
        # Preview File
        servePreviewFile = scenePr.scenePreviewFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName, sceneClass, sceneName, sceneVariant, sceneStage, vedioFormat
        )[1]
        backupPreviewFile = scenePr.scenePreviewFile(
            lxConfigure.LynxiRootIndex_Backup,
            projectName, sceneClass, sceneName, sceneVariant, sceneStage, vedioFormat
        )[1]
        if useMode == 1:
            localPreviewFile = scenePr.scenePreviewFile(
                lxConfigure.LynxiRootIndex_Local,
                projectName, sceneClass, sceneName, sceneVariant, sceneStage, vedioFormat
            )[1]
            servePreviewFile = lxBasic.getOsFileJoinTimeTag(localPreviewFile)
        # Index File
        serverPreviewIndexFile = scenePr.scenePreviewIndexFile(
            lxConfigure.LynxiRootIndex_Server,
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
        lxLog.viewResult(logWin, subSeverPreviewFile)
    #
    def setMain():
        cameraData, uploadConfig = getData(withPreview)
        if cameraData is not None:
            sceneCameraLis, usedCameraLis = cameraData
            if sceneCameraLis and usedCameraLis:
                percent, quality, width, height, vedioFormat, displayMode, useMode = uploadConfig
                # View Progress
                progressExplain = '''Upload Preview(s)'''
                maxValue = len(usedCameraLis)
                progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
                #
                maUtils.setDefaultShaderColor(.5, .5, .5)
                for seq, cameraObject in enumerate(sceneCameraLis):
                    if cameraObject in usedCameraLis:
                        # Sub Progress
                        progressBar.updateProgress()
                        #
                        subLabel = lxBasic.getSubLabel(seq)
                        setBranch(cameraObject, subLabel, percent, quality, width, height, vedioFormat, displayMode, useMode)
            else:
                lxLog.viewWarning(
                    logWin,
                    u'Camera is Non - Exists'
                )
    #
    setMain()


#
def scUnitSoundUploadCmd(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
):
    serverFile = scenePr.sceneSoundFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    backupFile = scenePr.sceneSoundFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName, sceneClass, sceneName, sceneVariant, sceneStage
    )[1]
    #
    sounds = datScene.getSceneSounds()
    if sounds:
        for seq, i in enumerate(sounds):
            pass


#
def scUnitAssetCachesUploadCmd(
        logWin,
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
            lxConfigure.LynxiRootIndex_Server,
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
                            lxConfigure.LynxiRootIndex_Server,
                            projectName,
                            sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_Solver,
                            assetName, number
                        )[1]
                        scAstModelCacheIndexKey = None
                    else:
                        scAstModelCacheFile = scenePr.scAstModelAlembicCacheFile(
                            lxConfigure.LynxiRootIndex_Server,
                            projectName,
                            sceneName, sceneVariant, sceneStage,
                            assetName, number
                        )[1]
                        scAstModelCacheIndexKey = lxConfigure.LynxiCacheInfoKey
                    # Alembic Cache Sequence
                    scUnitAstAlembicCacheUploadCmd(
                        logWin,
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
                        lxConfigure.LynxiRootIndex_Server,
                        projectName,
                        sceneName, sceneVariant,
                        assetName, number
                    )[1]
                    # Alembic Cache
                    uploadScAlembicCache(
                        logWin,
                        astModelLinkRoot,
                        scAstModelPoseCache,
                        startFrame,
                        timeTag
                    )
                else:
                    lxLog.viewError(
                        logWin,
                        u'Asset Model ( Mesh Root ) is Non - Exists',
                        scenePr.scAstName(assetName, number, assetVariant)
                    )
        # Extra Cache
        if astExtraSubRoot is not None:
            if isWithRigExtraCache is True and isModelCacheUseForSolver is False:
                if maUtils.isAppExist(astExtraSubRoot):
                    astRigExtraCacheFile = scenePr.scAstRigExtraAlembicCacheFile(
                        lxConfigure.LynxiRootIndex_Server,
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
                        logWin,
                        astExtraSubRoot,
                        lxConfigure.LynxiExtraCacheInfoKey,
                        astCacheIndexFile, astRigExtraCacheFile,
                        sceneStage,
                        startFrame, endFrame,
                        timeTag,
                        description, notes,
                        alembicAttrs=alembicAttrs
                    )
                else:
                    lxLog.viewError(
                        logWin,
                        u'Asset Rig ( Extra Root ) is Non - Exists',
                        scenePr.scAstName(assetName, number, assetVariant)
                    )
        # Solver Cache
        if astSolverSubRoot is not None:
            if isWithSolverCache is True:
                if maUtils.isAppExist(astSolverSubRoot):
                    assetSolverCacheFile = scenePr.scAstSolverAlembicCacheFile(
                        lxConfigure.LynxiRootIndex_Server,
                        projectName,
                        sceneName, sceneVariant, lxConfigure.LynxiProduct_Scene_Link_Solver,
                        assetName, number
                    )[1]
                    # Alembic Cache Sequence
                    scUnitAstAlembicCacheUploadCmd(
                        logWin,
                        astSolverSubRoot,
                        lxConfigure.LynxiSolverCacheInfoKey,
                        astCacheIndexFile, assetSolverCacheFile,
                        sceneStage,
                        startFrame, endFrame,
                        timeTag,
                        description, notes
                    )
                else:
                    lxLog.viewError(
                        logWin,
                        u'Asset Rig ( Solver Root ) is Non - Exists',
                        scenePr.scAstName(assetName, number, assetVariant)
                    )
    #
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
        progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
        for seq, i in enumerate(assetData):
            # Progress
            progressBar.updateProgress()
            #
            setBranch(i)
    else:
        lxLog.viewWarning(
            logWin,
            u'Asset is Non - Exists'
        )


#
def scUnitSceneriesUploadCmd(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
        withScenery
):
    # Main Method
    if withScenery is not False:
        withExtra,  = withScenery
        if withExtra is True:
            sceneryExtraData = datScene.getScSceneryExtraData(sceneName, sceneVariant, sceneStage)
            if sceneryExtraData:
                sceneryExtraFile = scenePr.scUnitSceneryExtraFile(
                    lxConfigure.LynxiRootIndex_Server,
                    projectName, sceneClass, sceneName, sceneVariant, sceneStage
                )[1]
                backupExtraFile = scenePr.scUnitSceneryExtraFile(
                    lxConfigure.LynxiRootIndex_Backup,
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
                lxLog.viewWarning(
                    logWin,
                    u'Scenery is Non - Exists'
                )


#
def scUnitSceneryComposeUploadCmd_(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        timeTag,
):
    data = datScene.getScAssemblyComposeDatumLis(sceneName, sceneVariant, sceneStage)
    if data:
        serverFile = scenePr.scUnitAssemblyComposeFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            sceneClass, sceneName, sceneVariant, sceneStage
        )[1]
        backupFile = scenePr.scUnitAssemblyComposeFile(
            lxConfigure.LynxiRootIndex_Backup,
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


@lxTip.viewExceptionMethod
def uploadScAstCfxFurCache(
        furCacheDataArray,
        useExistsCache=True
):
    cacheType = 'OneFile'
    cacheFormat = 'mcx'
    if furCacheDataArray:
        # View Progress
        progressExplain = '''Uploading Asset ( CFX ) Cache'''
        maxValue = len(furCacheDataArray)
        progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
        yetiObjects = []
        yetiCaches = []
        yetiStartFrame = None
        yetiEndFrame = None
        yetiSample = None
        for seq, data in enumerate(furCacheDataArray):
            #
            furObject, furObjectName, furObjectType, furCacheFile, furCacheIndex, furCacheIndexFile, startFrame, endFrame, sample, solverMode = data
            # Progress
            progressBar.updateProgress(furObjectName)
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
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize,
        timeTag,
):
    serverRenderFile = scenePr.scUnitRenderFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage, customize
    )[1]
    backupRenderFile = scenePr.scUnitRenderFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage, customize
    )[1]
    #
    lxLog.viewStartProcess(logWin, u'Upload / Update Scene Render ( {} ) File'.format(lxBasic._toStringPrettify(sceneStage)))
    #
    maFile.saveMayaFile(serverRenderFile)
    # Back File
    lxBasic.backupOsFile(
        serverRenderFile, backupRenderFile,
        timeTag
    )
    #
    lxLog.viewResult(logWin, serverRenderFile)
    #
    lxLog.viewCompleteProcess(logWin)


@lxTip.viewExceptionMethod
def scUnitRenderIndexUploadCmd(
        logWin,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        width, height,
        customize,
        timeTag,
):
    serverRenderFile = scenePr.scUnitRenderFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    #
    serverRenderIndexFile = scenePr.sceUnitRenderIndexFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    backupRenderIndexFile = scenePr.sceUnitRenderIndexFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    #
    serverRenderPath = scenePr.scUnitRenderFolder(
        lxConfigure.LynxiRootIndex_Server,
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
    lxLog.viewStartProcess(logWin, u'Upload / Update Scene Render ( {} ) Index'.format(lxBasic._toStringPrettify(sceneStage)))
    #
    lxBasic.writeOsJson(renderData, serverRenderIndexFile, 4)
    lxBasic.backupOsFile(serverRenderIndexFile, backupRenderIndexFile, timeTag)
    #
    lxLog.viewCompleteProcess(logWin)


#
def scUnitRenderDeadlineSubmitMainCmd(
        logWin,
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
    # Render File
    serverRenderFile = scenePr.scUnitRenderFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    # Info
    serverDeadlineInfoFile = scenePr.scDeadlineInfoFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    # Job
    serverDeadlineJobFile = scenePr.scDeadlineJobFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )[1]
    #
    serverRenderPath = scenePr.scUnitRenderFolder(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneClass, sceneName, sceneVariant, sceneStage,
        customize
    )
    serverRenderImagePath = scenePr.scUnitRenderImageFolder(
        lxConfigure.LynxiRootIndex_Server,
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
    lxLog.viewStartProcess(logWin, u'Submit Deadline Job(s) ( {} ) '.format(lxBasic._toStringPrettify(sceneStage)))
    if renderLayerLis:
        batchName = scenePr.scDeadlineBatchName(
            projectName,
            sceneName, sceneVariant,
            customize, ddlJobType
        )
        # View Progress
        progressExplain = u'''Submit Deadline Job(s)'''
        maxValue = len(renderLayerLis)
        progressBar = lxProgress.viewSubProgress(progressExplain, maxValue)
        for seq, currentRenderLayer in enumerate(renderLayerLis):
            progressBar.updateProgress(currentRenderLayer)
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
            subInfoData, subJobData = deadlineOp.getDdlMayaBatchData(
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
            lxLog.viewStartSubProcess(logWin, u'Submit Deadline Job for Layer : {}'.format(currentRenderLayer))
            #
            scUnitDeadlineJobSubmitCmd(logWin, subInfoData, subJobData, serverSubDeadlineInfoFile, serverSubDeadlineJobFile, timeTag)
            #
            lxLog.viewCompleteSubProcess(logWin)
    #
    lxLog.viewCompleteProcess(logWin)


#
def scUnitDeadlineJobSubmitCmd(
        logWin,
        infoData, jobData,
        infoFile, jobFile,
        timeTag
):
    # Info
    mainLineInfoFile = lxBasic.getOsFileJoinTimeTag(infoFile, lxConfigure.LynxiMainTimeTag, useMode=1)
    multLineInfoFile = lxBasic.getOsFileJoinTimeTag(infoFile, timeTag, useMode=1)
    lxBasic.writeOsData(infoData, multLineInfoFile)
    lxBasic.backupOsFile(multLineInfoFile, mainLineInfoFile)
    lxLog.viewResult(logWin, multLineInfoFile)
    # Job
    mainLineJobFile = lxBasic.getOsFileJoinTimeTag(jobFile, lxConfigure.LynxiMainTimeTag, useMode=1)
    multLineJobFile = lxBasic.getOsFileJoinTimeTag(jobFile, timeTag, useMode=1)
    lxBasic.writeOsData(jobData, multLineJobFile)
    lxBasic.backupOsFile(multLineJobFile, mainLineJobFile)
    lxLog.viewResult(logWin, multLineJobFile)
    #
    if multLineInfoFile and multLineJobFile:
        # Test Boolean
        enable = True
        if enable is True:
            result = deadlineOp.runDdlJob(multLineInfoFile, multLineJobFile)
            if result:
                for i in result:
                    if not i.startswith('\r\n'):
                        lxLog.viewResult(logWin, i)
            #
            resultFile = lxConfigure._toLxProductResultFile(multLineJobFile)
            #
            lxBasic.writeOsData(result, resultFile)
    else:
        lxLog.viewError(logWin, 'Write Deadline Info and Job Error')

