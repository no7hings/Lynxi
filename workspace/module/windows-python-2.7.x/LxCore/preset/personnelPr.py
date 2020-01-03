# coding=utf-8
from LxCore import lxBasic, lxCore_
#
from LxCore.preset import basicPr
#
guidePresetKey = lxCore_.LynxiPersonnelPresetKey

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
    mainPresetKey = lxCore_.LynxiTeamPresetKey
    mainSchemeKey = team
    return basicPr.getPresetSetDic((guidePresetKey, mainPresetKey), mainSchemeKey)


#
def getPersonnelPosts():
    return basicPr.getPersonnelPosts()


#
def getPersonnelPostDataDic(post):
    mainPresetKey = lxCore_.LynxiPostPresetKey
    mainSchemeKey = post
    return basicPr.getPresetSetDic((guidePresetKey, mainPresetKey), mainSchemeKey)


#
def getPersonnelUserLis():
    mainPresetKey = lxCore_.LynxiUserPresetKey
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
    mainPresetKey = lxCore_.LynxiUserPresetKey
    mainSchemeKey = user
    return basicPr.getPresetSetDic((guidePresetKey, mainPresetKey), mainSchemeKey)


#
def getPersonnelUserCnName(user=none):
    string = lxCore_.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxCore_.LynxiUserCnNameKey]
    return string


#
def getPersonnelUserEnName(user=none):
    string = lxCore_.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxCore_.LynxiUserEnNameKey]
    return string


#
def getPersonnelUserMail(user=none):
    string = lxCore_.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxCore_.LynxiUserMailKey]
    return string


#
def getPersonnelUserTeam(user=none):
    string = lxCore_.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxCore_.LynxiTeamPresetKey]
    return string


#
def getPersonnelUserPost(user=none):
    string = lxCore_.LynxiValue_Unspecified
    if not user:
        user = lxBasic.getOsUser()
    #
    if user in lxCore_.LynxiPipelineTds:
        return lxCore_.LynxiPipelineTdPost
    #
    data = getPersonnelUserDataDic(user)
    if data:
        string = data[lxCore_.LynxiPostPresetKey]
    return string


#
def getPersonnelSendMailEnabled(user=none):
    boolean = False
    if not user:
        user = lxBasic.getOsUser()
    #
    data = getPersonnelUserDataDic(user)
    if data:
        boolean = data[lxCore_.LynxiUserSendMailEnabledKey]
    return boolean


#
def getPostLevel(post):
    mainPresetKey = lxCore_.LynxiPostPresetKey
    #
    if post == lxCore_.LynxiPipelineTdPost:
        return lxCore_.LynxiPipelineTdLevel
    #
    mainSchemeKey = post
    return basicPr.getMainPresetSetValue(guidePresetKey, mainPresetKey, mainSchemeKey, lxCore_.LynxiPostLevelKey)


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
    mainPresetKey = lxCore_.LynxiUserPresetKey
    mainSchemeKey = user
    users = getPersonnelUserLis()
    if not user in users:
        userIndexFile = basicPr.presetIndexFileMethod((guidePresetKey, mainPresetKey))
        data = lxBasic.readOsJson(userIndexFile)
        if data is None:
            data = []
        userSchemeData = basicPr.defaultSchemeConfig()
        userSchemeData.insert(0, user)
        data.append(userSchemeData)
        lxBasic.writeOsJson(data, userIndexFile)
    #
    userSetFile = basicPr.presetSetFileMethod((guidePresetKey, mainPresetKey), mainSchemeKey)
    data = lxBasic.readOsJson(userSetFile)
    if not data:
        data = {}
    data[lxCore_.LynxiUserCnNameKey] = cnName
    data[lxCore_.LynxiUserEnNameKey] = enName
    data[lxCore_.LynxiUserMailKey] = mail
    data[lxCore_.LynxiTeamPresetKey] = team
    data[lxCore_.LynxiPostPresetKey] = post
    #
    lxBasic.writeOsJson(data, userSetFile)
