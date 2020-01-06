# coding=utf-8
from LxBasic import bscModifier

from LxCore import lxBasic, lxCore_

from LxUi.qt import qtLog
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
isSendMail = lxCore_.LynxiIsSendMail
isSendDingTalk = lxCore_.LynxiIsSendDingTalk
#
none = ''


@bscModifier.catchException
@bscModifier.catchCostTime
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
    qtLog.viewStartUploadMessage(logWin)
    for i in methodDatumLis:
        explain, enable, method, args = i
        qtLog.viewStartProcess(logWin, '''{} ( {} )'''.format(explain, lxBasic.str_camelcase2prettify(sceneryStage)))
        if enable is not False:
            method(*args)
            qtLog.viewCompleteProcess(logWin)
        else:
            qtLog.viewWarning(logWin, '''{} is Ignore'''.format(explain))
    # Complete
    qtLog.viewCompleteUploadMessage(logWin)
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
        lxCore_.LynxiRootIndex_Backup, projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    linkFile = lxBasic.getOsFileJoinTimeTag(backSourceFile, timeTag)
    maFile.saveMayaFile(linkFile)
    qtLog.viewResult(logWin, linkFile)
    #
    sceneryUnitIndex = dbGet.getDbSceneryUnitIndex(sceneryIndex, sceneryVariant)
    #
    dbBasic.writeDbSceneryUnitHistory(sceneryUnitIndex, linkFile)
    # Update Data >>> 02
    updateData = lxCore_.lxProductRecordDatumDic(
        linkFile,
        sceneryStage,
        description, notes
    )
    updateFile = lxCore_._toLxProductRecordFile(linkFile)
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
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitAssemblyComposeFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    datumLis = datScenery.getScnAssemblyComposeDatumLis(projectName, sceneryName)
    #
    lxBasic.writeOsJson(datumLis, serverFile)
    qtLog.viewResult(logWin, serverFile)
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
        lxCore_.LynxiRootIndex_Server,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitProductFile(
        lxCore_.LynxiRootIndex_Backup,
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
    qtLog.viewResult(logWin, serverFile)
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
        lxCore_.LynxiRootIndex_Server,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitPreviewFile(
        lxCore_.LynxiRootIndex_Backup,
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
    qtLog.viewResult(logWin, serverFile)
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
        lxCore_.LynxiRootIndex_Server,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitDefinitionFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName, sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    serverProductFile = sceneryPr.scnUnitProductFile(
        lxCore_.LynxiRootIndex_Server,
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
    qtLog.viewResult(logWin, serverFile)
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
        lxCore_.LynxiRootIndex_Local,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    backupFile = sceneryPr.scnUnitSourceFile(
        lxCore_.LynxiRootIndex_Backup,
        projectName,
        sceneryClass, sceneryName, sceneryVariant, sceneryStage
    )[1]
    #
    maFile.openMayaFileToLocal(
        lxBasic.getOsFileJoinTimeTag(backupFile, timeTag),
        localFile,
        timeTag
    )
    qtLog.viewResult(logWin, localFile)
