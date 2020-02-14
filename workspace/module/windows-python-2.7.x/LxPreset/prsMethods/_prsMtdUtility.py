# coding=utf-8
from LxBasic import bscConfigure, bscCore, bscMethods

from LxScheme import shmOutput

from LxCore.preset import basicPr

from LxCore import lxConfigure
# do not delete and rename
serverBasicPath = shmOutput.Root().basic.server
localBasicPath = shmOutput.Root().basic.local


class Personnel(object):
    VAR_key_preset_guide = lxConfigure.DEF_preset_key_personnel

    @classmethod
    def teams(cls):
        return basicPr._getPersonnelTeamLis()

    @classmethod
    def posts(cls):
        return basicPr._getPersonnelPostLis()

    @classmethod
    def usernames(cls):
        return basicPr.getPresetSchemes(
            (cls.VAR_key_preset_guide, lxConfigure.DEF_preset_key_User)
        )

    @classmethod
    def teamDatumDic(cls, team):
        mainPresetKey = lxConfigure.DEF_preset_key_Team
        mainSchemeKey = team
        return basicPr.getPresetSetDic(
            (cls.VAR_key_preset_guide, mainPresetKey),
            mainSchemeKey
        )

    @classmethod
    def postDatumDic(cls, post):
        mainPresetKey = lxConfigure.DEF_preset_key_Post
        mainSchemeKey = post
        return basicPr.getPresetSetDic((cls.VAR_key_preset_guide, mainPresetKey), mainSchemeKey)

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
        mainPresetKey = lxConfigure.DEF_preset_key_User
        mainSchemeKey = username
        return basicPr.getPresetSetDic((cls.VAR_key_preset_guide, mainPresetKey), mainSchemeKey)

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
            string = data[lxConfigure.DEF_preset_key_Team]
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
            string = data[lxConfigure.DEF_preset_key_Post]
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
        mainPresetKey = lxConfigure.DEF_preset_key_Post
        #
        if post == lxConfigure.LynxiPipelineTdPost:
            return lxConfigure.LynxiPipelineTdLevel
        #
        mainSchemeKey = post
        return basicPr.getMainPresetSetValue(
            cls.VAR_key_preset_guide, mainPresetKey,
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

        mainPresetKey = lxConfigure.DEF_preset_key_User
        mainSchemeKey = username
        usernames = cls.usernames()
        if not username in usernames:
            userIndexFile = basicPr.presetIndexFileMethod((cls.VAR_key_preset_guide, mainPresetKey))
            data = bscMethods.OsJson.read(userIndexFile)
            if data is None:
                data = []
            userSchemeData = basicPr.defaultSchemeConfig()
            userSchemeData.insert(0, username)
            data.append(userSchemeData)
            bscMethods.OsJson.write(userIndexFile, data)

        userSetFile = basicPr.presetSetFileMethod((cls.VAR_key_preset_guide, mainPresetKey), mainSchemeKey)

        data = bscMethods.OsJson.read(userSetFile)
        if not data:
            data = {}

        data[lxConfigure.LynxiUserCnNameKey] = userChnname
        data[lxConfigure.LynxiUserEnNameKey] = userEngname
        data[lxConfigure.LynxiUserMailKey] = mail
        data[lxConfigure.DEF_preset_key_Team] = team
        data[lxConfigure.DEF_preset_key_Post] = post

        bscMethods.OsJson.write(userSetFile, data)


class Pipeline(object):
    pass


class Project(object):
    VAR_key_preset_guide = lxConfigure.DEF_preset_key_Project

    @classmethod
    def _getProjectMayaToolDatumDictByDirectory(cls, toolPath):
        dic = bscCore.orderedDict()
        #
        osFiles = bscMethods.OsDirectory.fileFullpathnames(toolPath)
        if osFiles:
            for fileString_ in osFiles:
                command = bscMethods.OsFile.read(fileString_)
                if command:
                    commandName = bscMethods.OsFile.name(fileString_)
                    #
                    toolTip = ''
                    #
                    toolTipFile = bscMethods.OsFile.renameExtTo(fileString_, '.tip')
                    tipData = bscMethods.OsFile.readlines(toolTipFile)
                    if tipData:
                        toolTip = [unicode(i, "gbk").replace('\r\n', '') for i in tipData]
                    #
                    if fileString_.endswith('.py'):
                        if bscMethods.MayaApp.isActive():
                            commandReduce = 'python({0});'.format(bscMethods.OsJson.dump(command))
                        else:
                            commandReduce = bscMethods.OsJson.dump(command)

                        dic[commandName] = fileString_, commandReduce, toolTip
                    #
                    if fileString_.endswith('.mel'):
                        dic[commandName] = fileString_, command, toolTip
        return dic

    @classmethod
    def _getMayaProjectEnviron(cls):
        environKey = bscConfigure.MtdBasic.DEF_key_environ_project
        return bscMethods.OsEnviron.get(environKey)

    @classmethod
    def _setMayaProjectEnviron(cls, projectName):
        if bscMethods.MayaApp.isActive():
            environKey = bscConfigure.MtdBasic.DEF_key_environ_project
            bscMethods.OsEnviron.set(environKey, projectName)

    @classmethod
    def variantPresetDict(cls, projectName=None):
        if projectName is None:
            projectName = cls.mayaActiveName()
        return basicPr.getGuidePresetVariantDic(cls.VAR_key_preset_guide, projectName)

    @classmethod
    def mayaShelfPresetDict(cls, projectName):
        mainPresetKey = lxConfigure.DEF_preset_key_Maya
        subPresetKey = lxConfigure.DEF_preset_key_Shelf
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

    @classmethod
    def mayaShelfDatumDict(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        dic = bscCore.orderedDict()
        data = cls.mayaShelfPresetDict(projectName)
        if data:
            isTd = lxConfigure.isLxPipelineTd()
            if isTd:
                isAdmin = True
            else:
                isAdmin = False
            #
            for k, v in data.items():
                if k.endswith('PresetTool'):
                    if isAdmin:
                        dic[k] = v
                elif not k.endswith('PresetTool'):
                    dic[k] = v
        #
        return dic

    @classmethod
    def mayaToolPresetDict(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = lxConfigure.DEF_preset_key_Maya
        subPresetKey = lxConfigure.DEF_preset_key_Kit
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

    @classmethod
    def mayaToolDatumDict(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        dic = bscCore.orderedDict()
        data = cls.mayaToolPresetDict(projectName)
        if data:
            for k, v in data.items():
                if v:
                    subDic = bscCore.orderedDict()
                    for ik, iv in v.items():
                        var = str
                        pathCmd = bscMethods.Variant.covertTo('var', iv)
                        exec pathCmd
                        subDic[ik] = var
                    dic[k] = subDic
        return dic

    @classmethod
    def mayaScriptPresetDict(cls, projectName):
        mainPresetKey = lxConfigure.DEF_preset_key_Maya
        subPresetKey = lxConfigure.DEF_preset_key_Script
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

    # noinspection PyShadowingNames
    @classmethod
    def mayaScriptDatumDict(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        dic = bscCore.orderedDict()
        #
        data = cls.mayaScriptPresetDict(projectName)
        if data:
            for k, v in data.items():
                if v:
                    for ik, iv in v.items():
                        var = ''
                        scriptText = bscMethods.Variant.covertTo('var', iv)
                        exec scriptText
                        if var:
                            dic.setdefault(k, []).append(var)
        return dic

    @classmethod
    def mayaTdPresetDict(cls, projectName):
        mainPresetKey = lxConfigure.DEF_preset_key_Maya
        subPresetKey = lxConfigure.DEF_preset_key_Td
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

    @classmethod
    def mayaTdPackageDirectories(cls, projectName):
        lis = []
        #
        dataDic = cls.mayaTdPresetDict(projectName)
        if dataDic:
            for k, v in dataDic.items():
                if v:
                    mayaPackageStr = v[lxConfigure.LynxiMayaPackageKey]
                    #
                    var = ''
                    scriptText = bscMethods.Variant.covertTo('var', mayaPackageStr)
                    exec scriptText
                    #
                    if var:
                        lis.append(var)
        return lis

    @classmethod
    def mayaCustomPlugPresetDict(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = lxConfigure.DEF_preset_key_Maya
        subPresetKey = lxConfigure.DEF_preset_key_Plug
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

    @classmethod
    def isMayaPlugPresetSame(cls, sourceProjectName, targetProjectName):
        boolean = False
        sourcePlugData = cls.mayaCustomPlugPresetDict(sourceProjectName)
        targetPlugData = cls.mayaCustomPlugPresetDict(targetProjectName)
        if not targetPlugData == sourcePlugData:
            boolean = True
        return boolean

    @classmethod
    def mayaRenderer(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = lxConfigure.DEF_preset_key_Basic
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaRendererKey)

    @classmethod
    def mayaTimeUnit(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = lxConfigure.DEF_preset_key_Basic
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaTimeUnitKey)

    @classmethod
    def isMayaUsedArnoldRenderer(cls):
        boolean = False
        renderer = cls.mayaRenderer()
        if renderer == lxConfigure.LynxiArnoldRendererValue:
            boolean = True
        return boolean

    @classmethod
    def episodes(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = lxConfigure.DEF_preset_key_Basic
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, lxConfigure.DEF_preset_key_Episode)

    @classmethod
    def mayaVersion(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        if projectName.startswith(lxConfigure.Lynxi_Keyword_Project_Default):
            return projectName.split('_')[-1]
        else:
            mainPresetKey = lxConfigure.DEF_preset_key_Maya
            guideSchemeKey = projectName
            #
            mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
            return basicPr.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaVersionKey)

    @classmethod
    def mayaCommonPlugLoadNames(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = lxConfigure.DEF_preset_key_Maya
        guideSchemeKey = projectName
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return basicPr.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, lxConfigure.LynxiMayaCommonPlugsKey)

    @classmethod
    def mayaCustomPlugLoadNames(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        lis = []
        data = cls.mayaCustomPlugPresetDict(projectName)
        if data:
            for k, v in data.items():
                autoLoad = v[lxConfigure.Lynxi_Key_Plug_Load_Enable_Auto]
                if autoLoad is True:
                    loadNames = v[lxConfigure.Lynxi_Key_Plug_Load_Names]
                    if loadNames:
                        lis.extend(loadNames)
        return lis

    @classmethod
    def names(cls):
        return basicPr.getPresetSchemes((cls.VAR_key_preset_guide,))

    @classmethod
    def schemeDatumDic(cls):
        return basicPr.getUiPresetSchemeDataDic((cls.VAR_key_preset_guide,))

    @classmethod
    def showname(cls, projectName):
        data = basicPr.getUiPresetSchemeDataDic((cls.VAR_key_preset_guide,))
        if data:
            if projectName in data:
                return data[projectName][1]
            return ''
        return ''

    @classmethod
    def showinfo(cls, projectName):
        string = u'项目 : {0}'.format(cls.showname(projectName))
        return string

    @classmethod
    def appNames(cls):
        if bscMethods.MayaApp.isActive():
            lis = cls.mayaNames()
        else:
            lis = cls.names()
        return lis

    @classmethod
    def mayaNames(cls, mayaVersion=None):
        lis = []
        if bscMethods.MayaApp.isActive():
            projectNameLis = cls.names()
            if projectNameLis:
                for projectName in projectNameLis:
                    projectMayaVersion = cls.mayaVersion(projectName)
                    if mayaVersion is None:
                        currentMayaVersion = bscMethods.MayaApp.version()
                    else:
                        currentMayaVersion = mayaVersion
                    #
                    if str(projectMayaVersion) == currentMayaVersion:
                        lis.append(projectName)
        return lis

    @classmethod
    def uidatumDict(cls, projectNameFilter=None):
        dic = bscCore.orderedDict()
        #
        data = cls.schemeDatumDic()
        if data:
            for projectName, (enable, description) in data.items():
                filterEnable = False
                if projectNameFilter is not None:
                    if projectName == projectNameFilter:
                        filterEnable = True
                else:
                    filterEnable = True
                #
                if filterEnable is True and (enable is True or enable is None):
                    projectIndex = bscMethods.UniqueId.getByString(projectName)
                    dic[projectIndex] = projectName, description
        return dic

    @classmethod
    def mayaDatumDict(cls):
        dic = bscCore.orderedDict()

        if bscMethods.MayaApp.isActive():
            data = cls.schemeDatumDic()
            if data:
                for projectName, (enabled, description) in data.items():
                    mayaVersion = cls.mayaVersion(projectName)
                    currentMayaVersion = bscMethods.MayaApp.version()
                    if str(mayaVersion) == currentMayaVersion:
                        dic[projectName] = enabled, description
        else:
            pass
        return dic

    @classmethod  # Get Project's Name
    def activeName(cls):
        # String <Project Name>
        string = lxConfigure.LynxiDefaultProjectValue

        fileString_ = shmOutput.UserPreset().projectConfigFile
        if not bscMethods.OsFile.isExist(fileString_):
            cls._setLocalConfig(string)
        else:
            data = bscMethods.OsJson.read(fileString_)
            if data:
                string = data[cls.VAR_key_preset_guide]
        #
        return string

    @classmethod
    def appActiveName(cls):
        if bscMethods.MayaApp.isActive():
            return cls.mayaActiveName()
        return cls.activeName()

    @classmethod  # Get Project's Name
    def mayaActiveName(cls):
        if bscMethods.MayaApp.isActive():
            mayaVersion = bscMethods.MayaApp.version()
            string = '{}_{}'.format(lxConfigure.Lynxi_Keyword_Project_Default, mayaVersion)
            #
            environValue = cls._getMayaProjectEnviron()
            if environValue is not None:
                string = environValue
            else:
                currentMayaVersion = bscMethods.MayaApp.version()
                fileString_ = shmOutput.UserPreset().applicationProjectConfigFile(bscConfigure.MtdBasic.DEF_app_maya, mayaVersion)
                if not bscMethods.OsFile.isExist(fileString_):
                    cls._setMayaLocalConfig(string, currentMayaVersion)
                #
                data = bscMethods.OsJson.read(fileString_)
                if data:
                    string = data[cls.VAR_key_preset_guide]
        else:
            string = lxConfigure.LynxiDefaultProjectValue
        #
        cls._setMayaProjectEnviron(string)
        return string

    @classmethod
    def mayaProxyExt(cls, projectName=None):
        usedRenderer = cls.mayaRenderer(projectName)
        osExt = '.prx'
        if usedRenderer == lxConfigure.LynxiArnoldRendererValue:
            osExt = '.ass'
        if usedRenderer == lxConfigure.LynxiRedshiftRendererValue:
            osExt = '.rs'
        return osExt

    @classmethod
    def _setAppLocalConfig(cls, projectName):
        if bscMethods.MayaApp.isActive():
            cls._setMayaLocalConfig(projectName, bscMethods.MayaApp.version())
        else:
            cls._setLocalConfig(projectName)

    @classmethod  # Set Project Config
    def _setLocalConfig(cls, projectName):
        fileString_ = shmOutput.UserPreset().projectConfigFile
        bscMethods.OsFile.createDirectory(fileString_)
        data = dict(project=projectName)
        bscMethods.OsJson.write(fileString_, data)

    @classmethod  # Set Project Config
    def _setMayaLocalConfig(cls, projectName, mayaVersion):
        if bscMethods.MayaApp.isActive():
            fileString_ = shmOutput.UserPreset().applicationProjectConfigFile(bscConfigure.MtdBasic.DEF_app_maya, mayaVersion)
            bscMethods.OsFile.createDirectory(fileString_)
            data = dict(project=projectName)
            bscMethods.OsJson.write(fileString_, data)

    @classmethod
    def serverRoots(cls, projectName=None):
        lis = []
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        guideSchemeKey = projectName
        mainPresetKey = lxConfigure.DEF_preset_key_Storage
        subPresetKey = lxConfigure.DEF_preset_key_Root
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        dic = basicPr.getSubPresetSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)
        #
        key = lxConfigure.LynxiServerRootKey
        if dic:
            if key in dic:
                data = dic[key]
                if data:
                    for k, v in data.items():
                        projectRoot = '{0}/{1}'.format(v, projectName)
                        if not projectRoot in lis:
                            lis.append(projectRoot)
        #
        return lis

    @classmethod
    def localRoots(cls, projectName=None):
        lis = []
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        guideSchemeKey = projectName
        mainPresetKey = lxConfigure.DEF_preset_key_Storage
        subPresetKey = lxConfigure.DEF_preset_key_Root
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        dic = basicPr.getSubPresetSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)
        #
        key = lxConfigure.LynxiLocalRootKey
        if dic:
            if key in dic:
                data = dic[key]
                if data:
                    for subKey, root in data.items():
                        projectRoot = '{0}/{1}'.format(root, projectName)
                        if not projectRoot in lis:
                            lis.append(projectRoot)
        #
        return lis

    @classmethod
    def rootDict(cls, projectName=None):
        outDic = bscCore.orderedDict()
        #
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        guideSchemeKey = projectName
        mainPresetKey = lxConfigure.DEF_preset_key_Storage
        subPresetKey = lxConfigure.DEF_preset_key_Root
        #
        mainSchemeKey = basicPr.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        dic = basicPr.getSubPresetSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)
        if dic:
            for k, v in dic.items():
                for ik, iv in v.items():
                    outDic.setdefault(ik, []).append(iv)
        #
        return outDic

    @classmethod
    def isCacheUseMultiline(cls):
        return False
