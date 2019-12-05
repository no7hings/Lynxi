# coding=utf-8
from LxCore import lxBasic, lxConfigure, lxLog, lxTip
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import sceneryPr
#
from LxCore.product.op import messageOp
#
from LxMaya.command import maUtils, maFile, maAsb
#
from LxDatabase import dbBasic, dbGet
#
from LxMaya.product import maAstUploadCmds, maScnLoadCmds
#
from LxMaya.product.data import datScenery
#
#
isSendMail = lxConfigure.LynxiIsSendMail
isSendDingTalk = lxConfigure.LynxiIsSendDingTalk
#
none = ''


@lxTip.viewExceptionMethod
@lxTip.viewTimeMethod
def scnUnitAssemblyUploadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        description, notes
):
    #
    timeTag = lxBasic.getOsActiveTimeTag()
    # Set Log Window
    logWin.setNameText(u'场景上传')
    # Start
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    #
    methodDatumLis = [
        (
            'Upload / Update Source', True, scnUnitAssemblySourceUploadCmd, (
                logWin,
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag,
                description, notes
            )
         ),
        (
            'Clear Scene', True, maAstUploadCmds.astUnitSceneClearCmd, (
                logWin,
            )
        ),
        (
            'Upload / Update Preview', True, scnUnitAssemblyPreviewUploadCmd, (
                logWin,
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
        (
            'Upload / Update Compose Data', True, scnUnitAssemblyComposeUploadCmd, (
                logWin,
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
        (
            'Upload / Update Product', True, scnUnitAssemblyProductUploadCmd, (
                logWin,
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
        (
            'Upload / Update Assembly Definition', True, scnUnitAssemblyDefinitionUploadCmd, (
                logWin,
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
        (
            'Open Source', True, scnUnitAssemblySourceOpenCmd, (
                logWin,
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
    ]
    #
    maxValue = len(methodDatumLis) + 1
    logWin.setMaxProgressValue(maxValue)
    lxLog.viewStartUploadMessage(logWin)
    for i in methodDatumLis:
        explain, enable, method, args = i
        lxLog.viewStartProcess(logWin, '''{} ( {} )'''.format(explain, lxBasic._toStringPrettify(sceneryStage)))
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
            sceneryIndex,
            projectName,
            sceneryClass, sceneryName, sceneryVariant, sceneryStage,
            description, notes
        )
    # Send Ding Talk
    if isSendDingTalk:
        messageOp.sendProductMessageByDingTalk(
            sceneryIndex,
            projectName,
            sceneryClass, sceneryName, sceneryVariant, sceneryStage,
            timeTag,
            description, notes
        )


#
def scnUnitAssemblySourceUploadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag,
        description, notes
):
    backSourceFile = sceneryPr.scnUnitSourceFile(
        lxConfigure.LynxiRootIndex_Backup, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    linkFile = lxBasic.getOsFileJoinTimeTag(backSourceFile, timeTag)
    maFile.saveMayaFile(linkFile)
    lxLog.viewResult(logWin, linkFile)
    #
    sceneryUnitIndex = dbGet.getDbSceneryUnitIndex(sceneryIndex, sceneryVariant)
    #
    dbBasic.writeDbSceneryUnitHistory(sceneryUnitIndex, linkFile)
    # Update Data >>> 02
    updateData = lxConfigure.lxProductRecordDatumDic(
        linkFile,
        sceneryStage,
        description, notes
    )
    updateFile = lxConfigure._toLxProductRecordFile(linkFile)
    lxBasic.writeOsJson(updateData, updateFile)


#
def scnUnitAssemblyComposeUploadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag
):
    serverFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    datumLis = datScenery.getScnAssemblyComposeDatumLis(projectName, sceneryName)
    #
    lxBasic.writeOsJson(datumLis, serverFile)
    lxLog.viewResult(logWin, serverFile)
    #
    lxBasic.backupOsFile(serverFile, backupFile, timeTag)


#
def scnUnitAssemblyProductUploadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag
):
    serverFile = sceneryPr.scnUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitProductFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    maFile.new()
    maScnLoadCmds.scnUnitMaAssemblyLoadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        withAssembly=True
    )
    #
    maFile.saveMayaFile(serverFile)
    lxLog.viewResult(logWin, serverFile)
    #
    maFile.backupFile(serverFile, backupFile, timeTag)


#
def scnUnitAssemblyPreviewUploadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag,
        useDefaultMaterial=0
):
    serverFile = sceneryPr.scnUnitPreviewFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitPreviewFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    root = sceneryPr.scnAssemblyGroupName(sceneryName)
    #
    maFile.makeSnapshot(
        root,
        serverFile,
        useDefaultMaterial=useDefaultMaterial,
        width=appVariant.rndrImageWidth/2, height=appVariant.rndrImageHeight/2
    )
    lxLog.viewResult(logWin, serverFile)
    #
    lxBasic.backupOsFile(serverFile, backupFile, timeTag)


#
def scnUnitAssemblyDefinitionUploadCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag
):
    serverFile = sceneryPr.scnUnitDefinitionFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitDefinitionFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    serverProductFile = sceneryPr.scnUnitProductFile(
        lxConfigure.LynxiRootIndex_Server,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    sceneryAdName = sceneryPr.scnAssemblyAdName(
        sceneryClass, sceneryName, sceneryVariant
    )
    #
    maFile.new()
    maAsb.setAssemblySceneDefinitionCreate(sceneryAdName, serverProductFile)
    #
    maFile.saveMayaFile(serverFile)
    lxLog.viewResult(logWin, serverFile)
    #
    maFile.backupFile(serverFile, backupFile, timeTag)
    maFile.new()


#
def scnUnitAssemblySourceOpenCmd(
        logWin,
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag
):
    localFile = sceneryPr.scnUnitSourceFile(
        lxConfigure.LynxiRootIndex_Local,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitSourceFile(
        lxConfigure.LynxiRootIndex_Backup,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    maFile.openMayaFileToLocal(
        lxBasic.getOsFileJoinTimeTag(backupFile, timeTag),
        localFile,
        timeTag
    )
    lxLog.viewResult(logWin, localFile)