# coding=utf-8
from LxBasic import bscMethods

from LxPreset import prsConfigure

from LxCore import lxConfigure
#
from LxCore.config import basicCfg, assetCfg, sceneryCfg, sceneCfg
#
from LxCore.preset import prsMethod
#
from LxCore.preset.prod import projectPr, assetPr, sceneryPr, scenePr
#
from LxCore.operation import mailOp, dingTalkOp
#
none = ''


#
def getShowInfo(dbUnitId, classString, variantString, stageString):
    viewModule = none
    viewLink = none
    viewUnit = none
    viewClass = none
    viewName = none
    
    if classString in prsConfigure.Product.LynxiProduct_Asset_Class_Lis:
        viewModule = prsConfigure.Asset.showname()
        viewLink = prsConfigure.Asset.linkShowname_(stageString)
        viewUnit = assetPr.getAssetViewInfo(dbUnitId, classString, variantString)
        viewClass = prsConfigure.Asset.classShowname(classString)
        viewName = assetPr.getAssetViewName(dbUnitId)
    elif classString in sceneryCfg.scnBasicClass():
        viewModule = prsConfigure.Scenery.showname()
        viewLink = prsConfigure.Scenery.linkShowname_(stageString)
        viewUnit = sceneryPr.getSceneryViewInfo(dbUnitId, classString, variantString)
        viewClass = prsConfigure.Scenery.classShowname(classString)
        viewName = sceneryPr.getSceneryViewName(dbUnitId)
    elif classString in sceneCfg.scBasicClass():
        viewModule = prsConfigure.Scene.showname()
        viewLink = prsConfigure.Scene.linkShowname_(stageString)
        viewUnit = scenePr.getSceneViewInfo(dbUnitId, classString, variantString)
        viewClass = prsConfigure.Scene.classShowname(classString)
        viewName = scenePr.getSceneViewName(dbUnitId)
    return viewModule, viewLink, viewUnit, viewClass, viewName


#
def sendProductMessageByDingTalk(
        dbUnitId,
        projectName,
        classString, moduleName, variantString, stageString,
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
    viewModule, viewLink, viewUnit, viewClass, viewName = getShowInfo(dbUnitId, classString, variantString, stageString)
    #
    userName = bscMethods.OsSystem.username()
    userCnName = prsMethod.Personnel.userChnname()
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
        classString, moduleName, variantString, stageString,
        description, note
):
    toMails = prsMethod.Personnel.userMailsFilterByUsernames(
        prsMethod.Personnel.usernamesFilterByMailSendEnable()
    )
    #
    projectNameData = projectPr.getMayaProjectNameDic()
    viewProject = projectName
    if projectName in projectNameData:
        viewProject = projectNameData[projectName][1]
    #
    viewModule, viewLink, viewUnit, viewClass, viewName = getShowInfo(dbUnitId, classString, variantString, stageString)
    #
    summary = u'''项目更新【{0} - {1} - {2}】'''.format(viewProject, viewModule, viewUnit)
    subject = u'''{0} - {1} - {2}'''.format(viewProject, viewModule, viewUnit)
    #
    userCnName = prsMethod.Personnel.userChnname()
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
