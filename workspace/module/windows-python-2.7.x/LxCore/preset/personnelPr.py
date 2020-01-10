# coding=utf-8
from LxBasic import bscMethods

from LxCore import lxBasic, lxConfigure
#
from LxCore.preset import basicPr
#
guidePresetKey = lxConfigure.LynxiPersonnelPresetKey

#
none = ''


# Get Artist
def getUser():
    return lxBasic.getOsUser()


#
def getHostName():
    return lxBasic.getOsHostName()


#
def getHost():
    return lxBasic.getOsHost()


#
def getPersonnelTeamLis():
    return basicPr.getPersonnelTeamLis()


#
def getPersonnelTeamDataDic(team):
    mainPresetKey = lxConfigure.LynxiTeamPresetKey
    mainSchemeKey = team
    return basicPr.getPresetSetDic((guidePresetKey, mainPresetKey), mainSchemeKey)


#
def getPersonnelPosts():
    return basicPr.getPersonnelPosts()


#
def getPersonnelPostDataDic(post):
    mainPresetKey = lxConfigure.LynxiPostPresetKey
    mainSchemeKey = post
    return basicPr.getPresetSetDic((guidePresetKey, mainPresetKey), mainSchemeKey)


#
def getPersonnelUserLis():
    mainPresetKey = lxConfigure.LynxiUserPresetKey
    return basicPr.getPresetSchemes((guidePresetKey, mainPresetKey))


#
def getPersonnelUserExists(user=none):
    boolean = False
    if not user:
        user = lxBasic.getOsUser()
    users = getPersonnelUserLis()
    if user in users:
        boolean = True
    return boolean


#
def getPersonnelUserDataDic(user):
    mainPresetKey = lxConfigure.LynxiUserPresetKey
    mainSchemeKey = user
    return basicPr.getPresetSetDic((guidePresetKey, mainPresetKey), mainSchemeKey)


#
def getPersonnelUserCnName(user=none):
    string = lxConfigure.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxConfigure.LynxiUserCnNameKey]
    return string


#
def getPersonnelUserEnName(user=none):
    string = lxConfigure.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxConfigure.LynxiUserEnNameKey]
    return string


#
def getPersonnelUserMail(user=none):
    string = lxConfigure.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxConfigure.LynxiUserMailKey]
    return string


#
def getPersonnelUserTeam(user=none):
    string = lxConfigure.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxConfigure.LynxiTeamPresetKey]
    return string


#
def getPersonnelUserPost(user=none):
    string = lxConfigure.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    if user in lxConfigure.Lynxi_Name_Td_Lis:
        return lxConfigure.LynxiPipelineTdPost
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxConfigure.LynxiPostPresetKey]
    return string


#
def getPersonnelSendMailEnabled(user=none):
    boolean = False
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        boolean = data[lxConfigure.LynxiUserSendMailEnabledKey]
    return boolean


#
def getPostLevel(post):
    mainPresetKey = lxConfigure.LynxiPostPresetKey
    #
    if post == lxConfigure.LynxiPipelineTdPost:
        return lxConfigure.LynxiPipelineTdLevel
    #
    mainSchemeKey = post
    return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxConfigure.LynxiPostLevelKey)


#
def getUsersFilterByPost(postFilter):
    lis = []
    users = getPersonnelUserLis()
    for user in users:
        post = getPersonnelUserPost(user)
        if post == postFilter:
            lis.append(user)
    return lis


#
def getUserFilterBySendMailEnabled():
    lis = []
    users = getPersonnelUserLis()
    for user in users:
        sendMailEnabled = getPersonnelSendMailEnabled(user)
        if sendMailEnabled is True:
            lis.append(user)
    return lis


#
def getPersonnelUsersEmails(users):
    lis = []
    for user in users:
        mail = getPersonnelUserMail(user)
        lis.append(mail)
    return lis


#
def getPersonnelUserLevel(user=none):
    post = getPersonnelUserPost(user)
    return getPostLevel(post)


#
def setUpdatePersonnelUserSetData(user, cnName, enName, mail, team, post):
    if not user:
        user = lxBasic.getOsUser()
    mainPresetKey = lxConfigure.LynxiUserPresetKey
    mainSchemeKey = user
    users = getPersonnelUserLis()
    if not user in users:
        userIndexFile = basicPr.presetIndexFileMethod((guidePresetKey, mainPresetKey))
        data = bscMethods.OsJson.read(userIndexFile)
        if data is None:
            data = []
        userSchemeData = basicPr.defaultSchemeConfig()
        userSchemeData.insert(0, user)
        data.append(userSchemeData)
        lxBasic.writeOsJson(data, userIndexFile)
    #
    userSetFile = basicPr.presetSetFileMethod((guidePresetKey, mainPresetKey), mainSchemeKey)
    data = bscMethods.OsJson.read(userSetFile)
    if not data:
        data = {}
    data[lxConfigure.LynxiUserCnNameKey] = cnName
    data[lxConfigure.LynxiUserEnNameKey] = enName
    data[lxConfigure.LynxiUserMailKey] = mail
    data[lxConfigure.LynxiTeamPresetKey] = team
    data[lxConfigure.LynxiPostPresetKey] = post
    #
    lxBasic.writeOsJson(data, userSetFile)
