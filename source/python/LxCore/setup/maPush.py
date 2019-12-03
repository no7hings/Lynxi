# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
from LxCore.preset.prod import projectPr
#
none = ''


#
def setMaCustomPlugFilePushCmd(datumDic, showProgress):
    # Plug
    root = lxConfigure.PlugRoot().mayaRoot()
    # Push
    userRoot = lxConfigure.PlugRoot().userMayaRoot()
    #
    if datumDic:
        # View Progress
        if showProgress is True:
            from LxCore import lxProgress
            explain = '''Push Plug File(s)'''
            maxValue = len(datumDic)
            progressBar = lxProgress.viewSubProgress(explain, maxValue)
        else:
            progressBar = None
        #
        for plugName, localOsPlugPath in datumDic.items():
            # In Progress
            if progressBar is not None:
                progressBar.updateProgress(plugName)
            #
            serverOsPath = root + localOsPlugPath[len(userRoot):]
            targetOsPath = localOsPlugPath
            #
            sourceCheckJson = serverOsPath + '/timestamp.json'
            targetCheckJson = targetOsPath + '/timestamp.json'
            #  Constant Plug - In
            if lxBasic.isOsExist(targetOsPath):
                changedRelativeFiles = lxBasic.getChangedOsFiles(serverOsPath, targetOsPath)
                if not changedRelativeFiles:
                    traceMessage = u'Exists Plug "{}" : "{}"'.format(plugName, targetOsPath)
                    lxConfigure.Message().traceResult(traceMessage)
                else:
                    for relativeFilePath in changedRelativeFiles:
                        sourceFile = serverOsPath + relativeFilePath
                        targetFile = targetOsPath + relativeFilePath
                        lxBasic.setOsFileCopy(sourceFile, targetFile, force=False)
                        #
                        traceMessage = u'Update Plug "{}" : "{}" > "{}"'.format(plugName, sourceFile, targetFile)
                        lxConfigure.Message().traceResult(traceMessage)
                    #
                    if lxBasic.isOsExist(sourceCheckJson):
                        lxBasic.setOsFileCopy(sourceCheckJson, targetCheckJson)
            else:
                lxBasic.setOsFolderCopy(serverOsPath, targetOsPath)
                #
                if lxBasic.isOsExist(sourceCheckJson):
                    lxBasic.setOsFileCopy(sourceCheckJson, targetCheckJson)
                #
                traceMessage = u'Push Plug "{}" : "{}" > "{}"'.format(plugName, serverOsPath, targetOsPath)
                lxConfigure.Message().traceResult(traceMessage)


#
def setMaCustomPlugModulePushCmd(datumDic, mayaVersion):
    def isMaModulePushEnable(sourceFile, targetFile):
        boolean = False
        if lxBasic.isOsExistsFile(targetFile):
            sourceData = lxBasic.readOsFileLines(sourceFile)
            targetData = lxBasic.readOsFileLines(targetFile)
            if sourceData != targetData:
                boolean = True
        else:
            boolean = True
        return boolean
    #
    def getLocalModuleLis():
        lis = []
        osFiles = lxBasic.getOsFilesByPath(localModPath)
        if osFiles:
            for osFile in osFiles:
                if osFile.endswith('.mod'):
                    lis.append(osFile.lower())
        return lis
    #
    def getPushDataArray(osPathLis):
        if osPathLis:
            for osPath in osPathLis:
                sourceModPath = osPath + '/module'
                osFileBasenameLis = lxBasic.getOsFileBasenameLisByPath(sourceModPath)
                if osFileBasenameLis:
                    for osFileBasename in osFileBasenameLis:
                        if osFileBasename.endswith('.mod'):
                            sourceOsFile = lxBasic._toOsFile(sourceModPath, osFileBasename)
                            targetOsFile = lxBasic._toOsFile(localModPath, osFileBasename)
                            #
                            usedModuleFileLis.append(targetOsFile.lower())
                            # Filter is Push
                            isPush = isMaModulePushEnable(sourceOsFile, targetOsFile)
                            if isPush is True:
                                pushModDataArray.append((sourceOsFile, targetOsFile))
                            else:
                                lxConfigure.Message().traceResult(u'Exists Plug Module : "{}"'.format(targetOsFile))
    #
    localModPath = lxBasic.getMayaAppOsModPath(mayaVersion)
    #
    localModuleLis = getLocalModuleLis()
    #
    usedModuleFileLis = []
    pushModDataArray = []
    #
    folders = datumDic.values()
    getPushDataArray(folders)
    # Clean Unused Mod
    if localModuleLis:
        if usedModuleFileLis:
            for modFile in localModuleLis:
                if not modFile in usedModuleFileLis:
                    lxBasic.setOsFileRemove(modFile)
                    lxConfigure.Message().traceResult(u'Remove Invalid Plug Module : "{}"'.format(modFile))
        #
        else:
            for modFile in localModuleLis:
                lxBasic.setOsFileRemove(modFile)
                lxConfigure.Message().traceResult(u'Remove Invalid Plug Module : "{}"'.format(modFile))
    # Push Non - Exists Mod
    if pushModDataArray:
        for sourcePlugModuleFile, targetPlugModuleFile in pushModDataArray:
            lxBasic.setOsFileCopy(sourcePlugModuleFile, targetPlugModuleFile)
            #
            lxConfigure.Message().traceResult(u'Push Plug Module : "{}" > "{}"'.format(sourcePlugModuleFile, targetPlugModuleFile))


#
def setMaCustomPlugEnvironPushCmd(datumDic, mayaVersion):
    dic = lxBasic.orderedDict()
    envFile = lxBasic.getMayaAppsEnvFile(mayaVersion)
    #
    folders = datumDic.values()
    for folder in folders:
        splitKey = '='
        environFile = folder + '/_.env'
        envData = lxBasic.readOsFileLines(environFile)
        if envData:
            for data in envData:
                if data:
                    reduceData = data.strip().replace(' ', '')
                    if splitKey in reduceData:
                        splitData = reduceData.split(splitKey)
                        if len(splitData) > 1:
                            envKey = splitData[0]
                            envPaths = splitData[1].split(lxBasic.osPathsep())
                            for envPath in envPaths:
                                if envPath:
                                    dic.setdefault(envKey, []).append(envPath)
        #
        pathFile = folder + '/_.path'
        pathData = lxBasic.readOsFileLines(pathFile)
        if pathData:
            for data in pathData:
                if data:
                    lxBasic.createOsPath(data)
    if dic:
        envData = []
        for k, v in dic.items():
            data = '%s = %s' % (k, lxBasic.osPathsep().join(v))
            envData.append(data)
            #
            traceMessage = u'Write Maya Environ "{}" : "{}"'.format(k, lxBasic.osPathsep().join(v))
            lxConfigure.Message().traceResult(traceMessage)
        #
        if envData:
            reduceData = '\r\n'.join(envData)
            lxBasic.writeOsData(reduceData, envFile)


#
def setMaCustomPlugRlmPushCmd(datumDic):
    folders = datumDic.values()
    for folder in folders:
        plugName = folder.split('/')[-2]
        #
        rlmBat = folder + '/rlm.bat'
        if lxBasic.isOsExistsFile(rlmBat):
            lxBasic.setOsCommandRun(rlmBat)
            #
            traceMessage = u'Set RLM "{}" : "{}"'.format(plugName, folder)
            lxConfigure.Message().traceResult(traceMessage)


#
def setMaCustomPlugPushCmd(projectName=None, showProgress=False, isCloseMaya=False):
    def appCloseCmd():
        if lxBasic.isMayaApp():
            from LxMaya.command import maUtils
            #
            return maUtils.setMayaAppClose(force=1)
    #
    datumDic = projectPr.getMaCustomPlugPathDic(projectName)
    if datumDic:
        traceMessage = u'Setup Maya Plug(s)"'
        lxConfigure.Message().trace(traceMessage)
        #
        projectMayaVersion = projectPr.getProjectMayaVersion(projectName)
        #
        methodDatumLis = [
            ('Push Plug File(s)', True, setMaCustomPlugFilePushCmd, (datumDic, showProgress)),
            ('Push Plug Module(s)', True, setMaCustomPlugModulePushCmd, (datumDic, projectMayaVersion)),
            ('Push Plug Environ(s)', True, setMaCustomPlugEnvironPushCmd, (datumDic, projectMayaVersion)),
            ('Push Plug RLM(s)', True, setMaCustomPlugRlmPushCmd, (datumDic, ))
        ]
        # View Progress
        if showProgress is True:
            from LxCore import lxProgress
            explain = '''Push Plug(s)'''
            maxValue = len(methodDatumLis)
            progressBar = lxProgress.viewSubProgress(explain, maxValue)
        else:
            progressBar = None
        #
        for explain, enable, method, args in methodDatumLis:
            # In Progress
            if progressBar is not None:
                progressBar.updateProgress()
            #
            if enable is True:
                lxConfigure.Message().trace(explain)
                method(*args)
        #
        if isCloseMaya:
            from LxCore import lxTip
            #
            from LxUi.command import uiHtml
            tipWindow = lxTip.viewTip('Pipeline Tip', uiHtml.getHtml(u'''需要关闭 Maya 以完成插件推送（ 点击“Confirm”关闭 Maya ）；''', 1))
            tipWindow.confirmClicked.connect(appCloseCmd)
    else:
        lxConfigure.Message().traceWarning(u'Project "{}" is Non - Register'.format(projectName))
