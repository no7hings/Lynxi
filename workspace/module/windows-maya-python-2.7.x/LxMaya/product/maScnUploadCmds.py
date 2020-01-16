# coding=utf-8
from LxBasic import bscMethods, bscModifiers, bscObjects, bscCommands

from LxCore import lxConfigure

from LxCore.preset import appVariant

from LxCore.preset.prod import sceneryPr

from LxCore.product.op import messageOp

from LxMaya.command import maUtils, maFile, maAsb

from LxDatabase import dbBasic, dbGet

from LxMaya.product import maAstUploadCmds, maScnLoadCmds

from LxMaya.product.data import datScenery

isSendMail = lxConfigure.LynxiIsSendMail
isSendDingTalk = lxConfigure.LynxiIsSendDingTalk

none = ''


@bscModifiers.fncExceptionCatch
@bscModifiers.fncCostTimeCatch
def scnUnitAssemblyUploadCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        description, notes
):
    timeTag = bscMethods.OsTime.activeTimetag()
    # Set Log Window
    logWin_ = bscObjects.If_Log(title=u'Scenery Upload')
    # Start
    maUtils.setDisplayMode(5)
    maUtils.setVisiblePanelsDelete()
    #
    methodDatumLis = [
        (
            'Upload / Update Source', True, scnUnitAssemblySourceUploadCmd, (
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag,
                description, notes
            )
         ),
        (
            'Clear Scene', True, maAstUploadCmds.astUnitSceneClearCmd, ()
        ),
        (
            'Upload / Update Preview', True, scnUnitAssemblyPreviewUploadCmd, (
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
        (
            'Upload / Update Compose Data', True, scnUnitAssemblyComposeUploadCmd, (
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
        (
            'Upload / Update Product', True, scnUnitAssemblyProductUploadCmd, (
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
        (
            'Upload / Update Assembly Definition', True, scnUnitAssemblyDefinitionUploadCmd, (
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
        (
            'Open Source', True, scnUnitAssemblySourceOpenCmd, (
                projectName,
                sceneryIndex,
                sceneryClass, sceneryName, sceneryVariant, sceneryStage,
                timeTag
            )
        ),
    ]
    #
    maxValue = len(methodDatumLis) + 1
    logWin_.setMaxProgressValue(maxValue)
    logWin_.addStartTask(u'Scenery Upload')
    for i in methodDatumLis:
        explain, enable, method, args = i
        logWin_.addStartProgress(u'{} Upload'.format(explain))
        if enable is not False:
            method(*args)
            logWin_.addCompleteProgress()
        else:
            logWin_.addWarning(u'{} Upload is Ignore'.format(explain))
    # Complete
    logWin_.addCompleteTask()
    htmlLog = logWin_.htmlLog
    # Send Mail
    if isSendMail:
        messageOp.sendProductMessageByMail(
            htmlLog,
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
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag,
        description, notes
):
    logWin_ = bscObjects.If_Log()

    backSourceFile = sceneryPr.scnUnitSourceFile(
        lxConfigure.LynxiRootIndex_Backup, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]

    linkFile = bscMethods.OsFile.toJoinTimetag(backSourceFile, timeTag)
    maFile.saveMayaFile(linkFile)

    sceneryUnitIndex = dbGet.getDbSceneryUnitIndex(sceneryIndex, sceneryVariant)

    dbBasic.writeDbSceneryUnitHistory(sceneryUnitIndex, linkFile)

    updateData = bscMethods.OsFile.productInfoDict(
        linkFile,
        sceneryStage,
        description, notes
    )

    infoJsonFilename = bscMethods.OsFile.infoJsonFilename(linkFile)

    bscMethods.OsJson.write(infoJsonFilename, updateData)

    logWin_.addResult(linkFile)


#
def scnUnitAssemblyComposeUploadCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag
):
    logWin_ = bscObjects.If_Log()

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

    datumLis = datScenery.getScnAssemblyComposeDatumLis(projectName, sceneryName)

    bscMethods.OsJson.write(serverFile, datumLis)

    bscMethods.OsFile.backupTo(serverFile, backupFile, timeTag)

    logWin_.addResult(serverFile)


#
def scnUnitAssemblyProductUploadCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag
):
    logWin_ = bscObjects.If_Log()

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

    maFile.new()
    maScnLoadCmds.scnUnitMaAssemblyLoadCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        withAssembly=True
    )

    maFile.saveMayaFile(serverFile)

    bscMethods.OsFile.backupTo(serverFile, backupFile, timeTag)

    logWin_.addResult(serverFile)


#
def scnUnitAssemblyPreviewUploadCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag,
        useDefaultMaterial=0
):
    logWin_ = bscObjects.If_Log()

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

    bscMethods.OsFile.backupTo(serverFile, backupFile, timeTag)

    logWin_.addResult(serverFile)


#
def scnUnitAssemblyDefinitionUploadCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag
):
    logWin_ = bscObjects.If_Log()

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

    maFile.new()
    maAsb.setAssemblySceneDefinitionCreate(sceneryAdName, serverProductFile)

    maFile.saveMayaFile(serverFile)

    bscMethods.OsFile.backupTo(serverFile, backupFile, timeTag)
    maFile.new()

    logWin_.addResult(serverFile)


#
def scnUnitAssemblySourceOpenCmd(
        projectName,
        sceneryIndex,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage,
        timeTag
):
    logWin_ = bscObjects.If_Log()

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
        bscMethods.OsFile.toJoinTimetag(backupFile, timeTag),
        localFile,
        timeTag
    )
    logWin_.addResult(localFile)
