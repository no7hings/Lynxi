# coding=utf-8
from LxBasic import bscCfg, bscMtdCore, bscMethods

from LxScheme import shmOutput

from LxPreset import prsConfigure, prsMtdCore
# do not delete and rename
serverBasicPath = shmOutput.Root().basic.server
localBasicPath = shmOutput.Root().basic.local


class Personnel(prsConfigure.Utility):
    VAR_key_preset_guide = prsConfigure.Utility.DEF_key_preset_personnel

    @classmethod
    def teams(cls):
        return prsMtdCore.Mtd_PrsUtility._getPersonnelTeamLis()

    @classmethod
    def posts(cls):
        return prsMtdCore.Mtd_PrsUtility._getPersonnelPostLis()

    @classmethod
    def usernames(cls):
        return prsMtdCore.Mtd_PrsUtility._getEnabledSchemes(
            (cls.VAR_key_preset_guide, cls.DEF_key_preset_user)
        )

    @classmethod
    def teamDatumDic(cls, team):
        mainPresetKey = cls.DEF_key_preset_team
        mainSchemeKey = team
        return prsMtdCore.Mtd_PrsUtility.getPresetSetDic(
            (cls.VAR_key_preset_guide, mainPresetKey),
            mainSchemeKey
        )

    @classmethod
    def postDatumDic(cls, post):
        mainPresetKey = cls.DEF_key_preset_post
        mainSchemeKey = post
        return prsMtdCore.Mtd_PrsUtility.getPresetSetDic((cls.VAR_key_preset_guide, mainPresetKey), mainSchemeKey)

    @classmethod
    def isUserExist(cls, username=None):
        boolean = False
        if username is None:
            username = bscMethods.OsPlatform.username()
        usernames = cls.usernames()
        if username in usernames:
            boolean = True
        return boolean

    @classmethod
    def usernameDatumDic(cls, username):
        mainPresetKey = cls.DEF_key_preset_user
        mainSchemeKey = username
        return prsMtdCore.Mtd_PrsUtility.getPresetSetDic((cls.VAR_key_preset_guide, mainPresetKey), mainSchemeKey)

    @classmethod
    def userChnname(cls, username=None):
        string = cls.DEF_value_preset_unspecified
        if username is None:
            username = bscMethods.OsPlatform.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[cls.DEF_key_info_chnname]
        return string

    @classmethod
    def userEngname(cls, username=None):
        string = cls.DEF_value_preset_unspecified
        if username is None:
            username = bscMethods.OsPlatform.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[cls.DEF_key_info_engname]
        return string

    @classmethod
    def userMail(cls, username=None):
        string = cls.DEF_value_preset_unspecified
        if username is None:
            username = bscMethods.OsPlatform.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[cls.DEF_key_info_mail]
        return string

    @classmethod
    def userTeam(cls, username=None):
        string = cls.DEF_value_preset_unspecified
        if username is None:
            username = bscMethods.OsPlatform.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[cls.DEF_key_preset_team]
        return string

    @classmethod
    def userPost(cls, username=None):
        string = cls.DEF_value_preset_unspecified
        if username is None:
            username = bscMethods.OsPlatform.username()
        #
        if username in cls.Lynxi_Name_Td_Lis:
            return cls.LynxiPipelineTdPost
        #
        data = cls.usernameDatumDic(username)
        if data:
            string = data[cls.DEF_key_preset_post]
        return string

    @classmethod
    def isUserMailSendEnable(cls, username=None):
        boolean = False
        if username is None:
            username = bscMethods.OsPlatform.username()
        #
        data = cls.usernameDatumDic(username)
        if data:
            boolean = data[cls.DEF_key_info_sendmail]
        return boolean

    @classmethod
    def postLevel(cls, post):
        mainPresetKey = cls.DEF_key_preset_post
        #
        if post == cls.LynxiPipelineTdPost:
            return cls.LynxiPipelineTdLevel
        #
        mainSchemeKey = post
        return prsMtdCore.Mtd_PrsUtility.getMainPresetSetValue(
            cls.VAR_key_preset_guide, mainPresetKey,
            mainSchemeKey,
            cls.DEF_key_info_level
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
            username = bscMethods.OsPlatform.username()

        mainPresetKey = cls.DEF_key_preset_user
        mainSchemeKey = username
        usernames = cls.usernames()
        if not username in usernames:
            userIndexFile = prsMtdCore.Mtd_PrsUtility.indexFile((cls.VAR_key_preset_guide, mainPresetKey))
            data = bscMethods.OsJsonFile.read(userIndexFile)
            if data is None:
                data = []
            userSchemeData = prsMtdCore.Mtd_PrsUtility._defaultSchemeDatum()
            userSchemeData.insert(0, username)
            data.append(userSchemeData)
            bscMethods.OsJsonFile.write(userIndexFile, data)

        userSetFile = prsMtdCore.Mtd_PrsUtility.setFile((cls.VAR_key_preset_guide, mainPresetKey), mainSchemeKey)

        data = bscMethods.OsJsonFile.read(userSetFile)
        if not data:
            data = {}

        data[cls.DEF_key_info_chnname] = userChnname
        data[cls.DEF_key_info_engname] = userEngname
        data[cls.DEF_key_info_mail] = mail
        data[cls.DEF_key_info_team] = team
        data[cls.DEF_key_info_post] = post

        bscMethods.OsJsonFile.write(userSetFile, data)


class Pipeline(prsConfigure.Utility):
    pass


class Project(prsConfigure.Utility):
    VAR_key_preset_guide = prsConfigure.Utility.DEF_key_preset_project

    @classmethod
    def _getProjectMayaToolDatumDictByDirectory(cls, toolPath):
        dic = bscMtdCore.orderedDict()
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
                            commandReduce = 'python({0});'.format(bscMethods.OsJsonFile.dump(command))
                        else:
                            commandReduce = bscMethods.OsJsonFile.dump(command)

                        dic[commandName] = fileString_, commandReduce, toolTip
                    #
                    if fileString_.endswith('.mel'):
                        dic[commandName] = fileString_, command, toolTip
        return dic

    @classmethod
    def _getMayaProjectEnviron(cls):
        environKey = bscCfg.BscUtility.DEF_util__environ_key__project
        return bscMethods.OsEnviron.get(environKey)

    @classmethod
    def _setMayaProjectEnviron(cls, projectName):
        if bscMethods.MayaApp.isActive():
            environKey = bscCfg.BscUtility.DEF_util__environ_key__project
            bscMethods.OsEnviron.set(environKey, projectName)

    @classmethod
    def mayaShelfPresetDict(cls, projectName):
        mainPresetKey = cls.DEF_key_preset_maya
        subPresetKey = cls.DEF_key_preset_shelf
        guideSchemeKey = projectName

        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return prsMtdCore.Mtd_PrsUtility.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

    @classmethod
    def variantPresetDict(cls, projectName=None):
        if projectName is None:
            projectName = cls.appActiveName()

        if projectName is not None:
            return prsMtdCore.Mtd_PrsUtility.getGuidePresetVariantDic(cls.VAR_key_preset_guide, projectName)
        return {}

    @classmethod
    def mayaShelfDatumDict(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        dic = bscMtdCore.orderedDict()
        data = cls.mayaShelfPresetDict(projectName)
        if data:
            isTd = cls.isLxPipelineTd()
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
        mainPresetKey = cls.DEF_key_preset_maya
        subPresetKey = cls.DEF_key_preset_toolkit
        guideSchemeKey = projectName
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(
            cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey
        )
        return prsMtdCore.Mtd_PrsUtility.getSubPresetEnabledSetDataDic(
            cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey
        )

    @classmethod
    def mayaToolDatumDict(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        dic = bscMtdCore.orderedDict()
        datumDict = cls.mayaToolPresetDict(projectName)
        if datumDict:
            for k, v in datumDict.items():
                if v:
                    subDic = bscMtdCore.orderedDict()
                    for ik, iv in v.items():
                        var = str
                        pathCmd = bscMethods.Variant.covertTo('var', iv)
                        exec pathCmd
                        subDic[ik] = var
                    dic[k] = subDic
        return dic

    @classmethod
    def mayaScriptPresetDict(cls, projectName):
        mainPresetKey = cls.DEF_key_preset_maya
        subPresetKey = cls.DEF_key_preset_script
        guideSchemeKey = projectName
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return prsMtdCore.Mtd_PrsUtility.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

    # noinspection PyShadowingNames
    @classmethod
    def mayaScriptDatumDict(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        dic = bscMtdCore.orderedDict()
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
        mainPresetKey = cls.DEF_key_preset_maya
        subPresetKey = cls.DEF_key_preset_td
        guideSchemeKey = projectName
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return prsMtdCore.Mtd_PrsUtility.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

    @classmethod
    def mayaTdPackageDirectories(cls, projectName):
        lis = []
        #
        dataDic = cls.mayaTdPresetDict(projectName)
        if dataDic:
            for k, v in dataDic.items():
                if v:
                    mayaPackageStr = v[cls.LynxiMayaPackageKey]
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
        mainPresetKey = cls.DEF_key_preset_maya
        subPresetKey = cls.DEF_key_preset_plug
        guideSchemeKey = projectName
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return prsMtdCore.Mtd_PrsUtility.getSubPresetEnabledSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)

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
        mainPresetKey = cls.DEF_key_preset_basic
        guideSchemeKey = projectName
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return prsMtdCore.Mtd_PrsUtility.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, cls.DEF_key_renderer)

    @classmethod
    def mayaTimeUnit(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = cls.DEF_key_preset_basic
        guideSchemeKey = projectName
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return prsMtdCore.Mtd_PrsUtility.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, cls.DEF_key_timeunit)

    @classmethod
    def isMayaUsedArnoldRenderer(cls):
        boolean = False
        renderer = cls.mayaRenderer()
        if renderer == cls.DEF_value_renderer_arnold:
            boolean = True
        return boolean

    @classmethod
    def episodes(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = cls.DEF_key_preset_basic
        guideSchemeKey = projectName
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return prsMtdCore.Mtd_PrsUtility.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, cls.DEF_key_preset_episode)

    @classmethod
    def mayaVersion(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        if projectName.startswith(cls.VAR_value_project_default):
            return projectName.split('_')[-1]
        else:
            mainPresetKey = cls.DEF_key_preset_maya
            guideSchemeKey = projectName
            #
            mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
            return prsMtdCore.Mtd_PrsUtility.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, cls.LynxiMayaVersionKey)

    @classmethod
    def mayaCommonPlugLoadNames(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        mainPresetKey = cls.DEF_key_preset_maya
        guideSchemeKey = projectName
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        return prsMtdCore.Mtd_PrsUtility.getMainPresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, mainSchemeKey, cls.LynxiMayaCommonPlugsKey)

    @classmethod
    def mayaCustomPlugLoadNames(cls, projectName=None):
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        lis = []
        data = cls.mayaCustomPlugPresetDict(projectName)
        if data:
            for k, v in data.items():
                autoLoad = v[cls.DEF_key_plug_autoload]
                if autoLoad is True:
                    loadNames = v[cls.DEF_key_plug_loadname]
                    if loadNames:
                        lis.extend(loadNames)
        return lis

    @classmethod
    def names(cls):
        return prsMtdCore.Mtd_PrsUtility._getEnabledSchemes((cls.VAR_key_preset_guide,))

    @classmethod
    def schemeDatumDic(cls):
        return prsMtdCore.Mtd_PrsUtility._getSchemeUiDatumDic((cls.VAR_key_preset_guide,))

    @classmethod
    def showname(cls, projectName):
        data = prsMtdCore.Mtd_PrsUtility._getSchemeUiDatumDic((cls.VAR_key_preset_guide,))
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
        dic = bscMtdCore.orderedDict()
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
        dic = bscMtdCore.orderedDict()

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
        string = cls.VAR_value_project_default

        fileString_ = shmOutput.UserPreset().projectConfigFile
        if not bscMethods.OsFile.isExist(fileString_):
            cls._setLocalConfig(string)
        else:
            data = bscMethods.OsJsonFile.read(fileString_)
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
            string = '{}_{}'.format(cls.VAR_value_project_default, mayaVersion)
            #
            environValue = cls._getMayaProjectEnviron()
            if environValue is not None:
                string = environValue
            else:
                currentMayaVersion = bscMethods.MayaApp.version()
                fileString_ = shmOutput.UserPreset().applicationProjectConfigFile(bscCfg.BscUtility.DEF_bsc__app_name__maya, mayaVersion)
                if not bscMethods.OsFile.isExist(fileString_):
                    cls._setMayaLocalConfig(string, currentMayaVersion)
                #
                data = bscMethods.OsJsonFile.read(fileString_)
                if data:
                    string = data[cls.VAR_key_preset_guide]
        else:
            string = cls.VAR_value_project_default
        #
        cls._setMayaProjectEnviron(string)
        return string

    @classmethod
    def mayaProxyExt(cls, projectName=None):
        usedRenderer = cls.mayaRenderer(projectName)
        osExt = '.prx'
        if usedRenderer == cls.DEF_value_renderer_arnold:
            osExt = '.ass'
        if usedRenderer == cls.DEF_value_renderer_redshift:
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
        bscMethods.OsJsonFile.write(fileString_, data)

    @classmethod  # Set Project Config
    def _setMayaLocalConfig(cls, projectName, mayaVersion):
        if bscMethods.MayaApp.isActive():
            fileString_ = shmOutput.UserPreset().applicationProjectConfigFile(bscCfg.BscUtility.DEF_bsc__app_name__maya, mayaVersion)
            bscMethods.OsFile.createDirectory(fileString_)
            data = dict(project=projectName)
            bscMethods.OsJsonFile.write(fileString_, data)

    @classmethod
    def serverRoots(cls, projectName=None):
        lis = []
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        guideSchemeKey = projectName
        mainPresetKey = cls.DEF_key_preset_storage
        subPresetKey = cls.DEF_key_preset_root
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        dic = prsMtdCore.Mtd_PrsUtility.getSubPresetSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)
        #
        key = cls.LynxiServerRootKey
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
        mainPresetKey = cls.DEF_key_preset_storage
        subPresetKey = cls.DEF_key_preset_root
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        dic = prsMtdCore.Mtd_PrsUtility.getSubPresetSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)
        #
        key = cls.LynxiLocalRootKey
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
        outDic = bscMtdCore.orderedDict()
        #
        if not projectName:
            projectName = cls.mayaActiveName()
        #
        guideSchemeKey = projectName
        mainPresetKey = cls.DEF_key_preset_storage
        subPresetKey = cls.DEF_key_preset_root
        #
        mainSchemeKey = prsMtdCore.Mtd_PrsUtility.getGuidePresetSetValue(cls.VAR_key_preset_guide, mainPresetKey, guideSchemeKey)
        dic = prsMtdCore.Mtd_PrsUtility.getSubPresetSetDataDic(cls.VAR_key_preset_guide, mainPresetKey, subPresetKey, mainSchemeKey)
        if dic:
            for k, v in dic.items():
                for ik, iv in v.items():
                    outDic.setdefault(ik, []).append(iv)
        #
        return outDic

    @classmethod
    def isCacheUseMultiline(cls):
        return False
