# coding=utf-8
from LxBasic import bscMethods

from LxCore import lxConfigure
#
from LxCore.preset import basicPr


class Personnel(object):
    STR_preset_guide = lxConfigure.Lynxi_Key_Preset_Personnel

    @classmethod
    def teams(cls):
        return basicPr._getPersonnelTeamLis()

    @classmethod
    def posts(cls):
        return basicPr._getPersonnelPostLis()

    @classmethod
    def usernames(cls):
        return basicPr.getPresetSchemes(
            (cls.STR_preset_guide, lxConfigure.Lynxi_Key_Preset_User)
        )

    @classmethod
    def teamDatumDic(cls, team):
        mainPresetKey = lxConfigure.Lynxi_Key_Preset_Team
        mainSchemeKey = team
        return basicPr.getPresetSetDic(
            (cls.STR_preset_guide, mainPresetKey),
            mainSchemeKey
        )

    @classmethod
    def postDatumDic(cls, post):
        mainPresetKey = lxConfigure.Lynxi_Key_Preset_Post
        mainSchemeKey = post
        return basicPr.getPresetSetDic((cls.STR_preset_guide, mainPresetKey), mainSchemeKey)

    @classmethod
    def isUserExist(cls, username=None):
        boolean = False
        if username is None:
            username = bscMethods.OsSystem.username()
        usernames = cls.usernames()
        if username in usernames:
            boolean = True
        return boolean

    @classmethod
    def usernameDatumDic(cls, username):
        mainPresetKey = lxConfigure.Lynxi_Key_Preset_User
        mainSchemeKey = username
        return basicPr.getPresetSetDic((cls.STR_preset_guide, mainPresetKey), mainSchemeKey)

    @classmethod
    def userChnname(cls, username=None):
        string = lxConfigure.LynxiValue_Unspecified
        if username is None:
            username = bscMethods.OsSystem.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[lxConfigure.LynxiUserCnNameKey]
        return string

    @classmethod
    def userEngname(cls, username=None):
        string = lxConfigure.LynxiValue_Unspecified
        if username is None:
            username = bscMethods.OsSystem.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[lxConfigure.LynxiUserEnNameKey]
        return string

    @classmethod
    def userMail(cls, username=None):
        string = lxConfigure.LynxiValue_Unspecified
        if username is None:
            username = bscMethods.OsSystem.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[lxConfigure.LynxiUserMailKey]
        return string

    @classmethod
    def userTeam(cls, username=None):
        string = lxConfigure.LynxiValue_Unspecified
        if username is None:
            username = bscMethods.OsSystem.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[lxConfigure.Lynxi_Key_Preset_Team]
        return string

    @classmethod
    def userPost(cls, username=None):
        string = lxConfigure.LynxiValue_Unspecified
        if username is None:
            username = bscMethods.OsSystem.username()
        #
        if username in lxConfigure.Lynxi_Name_Td_Lis:
            return lxConfigure.LynxiPipelineTdPost
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[lxConfigure.Lynxi_Key_Preset_Post]
        return string

    @classmethod
    def isUserMailSendEnable(cls, username=None):
        boolean = False
        if username is None:
            username = bscMethods.OsSystem.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            boolean = data[lxConfigure.LynxiUserSendMailEnabledKey]
        return boolean

    @classmethod
    def postLevel(cls, post):
        mainPresetKey = lxConfigure.Lynxi_Key_Preset_Post
        #
        if post == lxConfigure.LynxiPipelineTdPost:
            return lxConfigure.LynxiPipelineTdLevel
        #
        mainSchemeKey = post
        return basicPr.getMainPresetSetValue(
            cls.STR_preset_guide, mainPresetKey,
            mainSchemeKey,
            lxConfigure.LynxiPostLevelKey
        )

    @classmethod
    def usernamesFilterByPost(cls, post):
        lis = []
        usernames = cls.usernames()
        for username in usernames:
            post_ = cls.userPost(username)
            if post_ == post:
                lis.append(username)
        return lis

    @classmethod
    def usernamesFilterByMailSendEnable(cls):
        lis = []
        usernames = cls.usernames()
        for username in usernames:
            sendMailEnabled = cls.isUserMailSendEnable(username)
            if sendMailEnabled is True:
                lis.append(username)
        return lis

    @classmethod
    def userMailsFilterByUsernames(cls, usernames):
        lis = []
        for username in usernames:
            mail = cls.userMail(username)
            lis.append(mail)
        return lis

    @classmethod
    def userLevel(cls, username=None):
        post = cls.userPost(username)
        return cls.postLevel(post)

    @classmethod
    def updateUserDatum(cls, username, userChnname, userEngname, mail, team, post):
        if username is None:
            username = bscMethods.OsSystem.username()

        mainPresetKey = lxConfigure.Lynxi_Key_Preset_User
        mainSchemeKey = username
        usernames = cls.usernames()
        if not username in usernames:
            userIndexFile = basicPr.presetIndexFileMethod((cls.STR_preset_guide, mainPresetKey))
            data = bscMethods.OsJson.read(userIndexFile)
            if data is None:
                data = []
            userSchemeData = basicPr.defaultSchemeConfig()
            userSchemeData.insert(0, username)
            data.append(userSchemeData)
            bscMethods.OsJson.write(userIndexFile, data)

        userSetFile = basicPr.presetSetFileMethod((cls.STR_preset_guide, mainPresetKey), mainSchemeKey)

        data = bscMethods.OsJson.read(userSetFile)
        if not data:
            data = {}

        data[lxConfigure.LynxiUserCnNameKey] = userChnname
        data[lxConfigure.LynxiUserEnNameKey] = userEngname
        data[lxConfigure.LynxiUserMailKey] = mail
        data[lxConfigure.Lynxi_Key_Preset_Team] = team
        data[lxConfigure.Lynxi_Key_Preset_Post] = post

        bscMethods.OsJson.write(userSetFile, data)


class Pipeline(object):
    pass


class Project(object):
    pass
