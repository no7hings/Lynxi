# coding=utf-8
from LxBasic import bscMethods

from LxCore import lxConfigure
#
from LxCore.config import basicCfg, assetCfg, sceneryCfg, sceneCfg
#
from LxCore.preset import personnelPr
#
from LxCore.preset.prod import projectPr, assetPr, sceneryPr, scenePr
#
from LxCore.operation import mailOp, dingTalkOp
#
none = ''


#
def getShowInfo(dbUnitId, moduleClass, moduleVariant, moduleStage):
    viewModule = none
    viewLink = none
    viewUnit = none
    viewClass = none
    viewName = none
    if moduleClass in assetCfg.astBasicClass():
        viewModule = basicCfg.basicModuleDic(lxConfigure.LynxiProduct_Module_Asset)[1]
        viewLink = assetCfg.astBasicViewLinkDic(assetPr.getAssetLink(moduleStage))[1]
        viewUnit = assetPr.getAssetViewInfo(dbUnitId, moduleClass, moduleVariant)
        viewClass = assetCfg.astBasicViewClassDic(moduleClass)[1]
        viewName = assetPr.getAssetViewName(dbUnitId)
    elif moduleClass in sceneryCfg.scnBasicClass():
        viewModule = basicCfg.basicModuleDic(lxConfigure.LynxiProduct_Module_Scenery)[1]
        viewLink = sceneryCfg.scnBasicViewLinkDic()[sceneryPr.getSceneryLink(moduleStage)][1]
        viewUnit = sceneryPr.getSceneryViewInfo(dbUnitId, moduleClass, moduleVariant)
        viewClass = sceneryCfg.scnBasicViewClassDic(moduleClass)[1]
        viewName = sceneryPr.getSceneryViewName(dbUnitId)
    elif moduleClass in sceneCfg.scBasicClass():
        viewModule = basicCfg.basicModuleDic(lxConfigure.LynxiProduct_Module_Scene)[1]
        viewLink = sceneCfg.scBasicViewLinkDic()[scenePr.getSceneLink(moduleStage)][1]
        viewUnit = scenePr.getSceneViewInfo(dbUnitId, moduleClass, moduleVariant)
        viewClass = sceneCfg.scBasicViewClassDic(moduleClass)[1]
        viewName = scenePr.getSceneViewName(dbUnitId)
    return viewModule, viewLink, viewUnit, viewClass, viewName


#
def sendProductMessageByDingTalk(
        dbUnitId,
        projectName,
        moduleClass, moduleName, moduleVariant, moduleStage,
        timeTag,
        description, note
):
    projectNameData = projectPr.getMayaProjectNameDic()
    viewProject = projectName
    if projectName in projectNameData:
        viewProject = projectNameData[projectName][1]
    #
    timeString = bscMethods.OsTime.getCnPrettifyByTimetag(timeTag, useMode=1)
    #
    viewModule, viewLink, viewUnit, viewClass, viewName = getShowInfo(dbUnitId, moduleClass, moduleVariant, moduleStage)
    #
    userName = personnelPr.getUser()
    userCnName = personnelPr.getPersonnelUserCnName()
    #
    if not note:
        note = u'N/a'
    #
    mainBody = u'''制作更新\n\n  项目：{}\n  环节：{}\n  元素：{} # {}\n\n  用户：{} # {}\n  日期：{}\n\n  描述：{}\n  备注：{}'''.format(
        viewProject,
        viewLink,
        viewUnit, moduleName,
        userCnName, userName,
        timeString,
        description,
        note
    )
    dingTalkRobot = dingTalkOp.DingTalkRobotMethod(mainBody)
    dingTalkRobot.send()


#
def sendProductMessageByMail(
        htmlLog,
        dbUnitId,
        projectName,
        moduleClass, moduleName, moduleVariant, moduleStage,
        description, note
):
    toMails = personnelPr.getPersonnelUsersEmails(personnelPr.getUserFilterBySendMailEnabled())
    #
    projectNameData = projectPr.getMayaProjectNameDic()
    viewProject = projectName
    if projectName in projectNameData:
        viewProject = projectNameData[projectName][1]
    #
    viewModule, viewLink, viewUnit, viewClass, viewName = getShowInfo(dbUnitId, moduleClass, moduleVariant, moduleStage)
    #
    summary = u'''项目更新【{0} - {1} - {2}】'''.format(viewProject, viewModule, viewUnit)
    subject = u'''{0} - {1} - {2}'''.format(viewProject, viewModule, viewUnit)
    #
    userCnName = personnelPr.getPersonnelUserCnName()
    #
    if not description:
        description = u'N/a'
    #
    if not note:
        note = u'N/a'
    #
    if htmlLog is None:
        u'N/a'u'无更新日志'
    #
    mainBody = u'''
        <html>
        <body style=";background:#ffffff;">
        <h1><span style="font-family:'Arial';font-size:12pt;font-weight:600;color:#000000;">更新信息</span></h1>
        <p>用户：{}</p>
        <p>项目：{}</p>
        <p>环节：{}</p>
        <p>名字：{}</p>
        <p>描述：{}</p>
        <p>备注：{}</p>
        <p>日志：</p>
        <p>{}</p>
        </body>
        </html>'''.format(
        userCnName,
        viewProject,
        viewLink,
        viewName,
        description,
        note,
        htmlLog
    )
    mailOp.sendMail(
        toMails, summary, subject, mainBody
    )
