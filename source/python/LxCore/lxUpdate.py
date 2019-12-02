# coding=utf-8
from LxCore import lxBasic, lxConfigure
reload(lxBasic)
reload(lxConfigure)
#
none = ''


#
def setMessageCountRest():
    key = lxConfigure.Lynxi_Key_Environ_MessageCount
    lxBasic.setOsEnvironValue(key, '0')


#
def _getLxLocalVersion():
    return lxBasic.getOsEnvironValue(lxConfigure.Lynxi_Key_Environ_Version)


#
def _getLxServerVersion():
    keyword = 'update'
    osFile = lxConfigure._getLxDevelopVersionFile()
    info = none
    if lxBasic.isOsExistsFile(osFile):
        data = lxBasic.readOsJson(osFile)
        if keyword in data:
            info = data[keyword][0]
    return info


#
def setLocalUpdateTagRefresh():
    serverUpdate = _getLxServerVersion()
    lxBasic.setOsEnvironValue(lxConfigure.Lynxi_Key_Environ_Version, serverUpdate)


#
def getPythonModuleLis(modulePath, moduleString):
    def getBranch(directory, keywordFilterString=none):
        osFileNames = lxBasic.getOsFileBasenameLisByPath(directory)
        if osFileNames:
            if keywordFilterString:
                if isinstance(keywordFilterString, list):
                    osFileNames = [j for j in osFileNames if j in keywordFilterString]
                if isinstance(keywordFilterString, str) or isinstance(keywordFilterString, unicode):
                    osFileNames = [j for j in osFileNames if j in [keywordFilterString]]
            #
            for name in osFileNames:
                osFile = lxBasic._toOsFile(directory, name)
                if osFile.endswith(ext):
                    pycFile = osFile[:-len(ext)] + '.pyc'
                    if lxBasic.isOsExistsFile(pycFile):
                        timestamp = lxBasic.getOsFileMtimestamp(osFile)
                        module_ = osFile[len(modulePath) + 1:-len(ext)].replace('/', '.')
                        #
                        lis.append(timestamp)
                        if module_.endswith('__init__'):
                            dic[timestamp] = module_[:(-len('__init__') - 1)]
                        else:
                            dic[timestamp] = module_
                #
                getBranch(osFile)
    #
    if lxConfigure.isLxDevelop():
        ext = '.py'
    else:
        ext = '.pyc'
    #
    moduleDatumLis = []
    #
    lis = []
    dic = {}
    #
    getBranch(modulePath, moduleString)
    #
    if lis:
        lis.sort()
        lis.reverse()
        for i in lis:
            if i in dic:
                module = dic[i]
                moduleDatumLis.append(module)
    #
    return moduleDatumLis


#
def setPythonModuleUpdate(modulePath, moduleString=none):
    moduleDatumLis = getPythonModuleLis(modulePath, moduleString)
    if moduleDatumLis:
        from LxCore import lxProgress
        # View Progress
        explain = '''Update Python Module(s)'''
        maxValue = len(moduleDatumLis)
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        for i in moduleDatumLis:
            modulePath = '.'.join(i.split('.')[:-1])
            moduleName = i.split('.')[-1]
            #
            progressBar.updateProgress(moduleName)
            #
            if modulePath:
                command = '''from {0} import {1};reload({1})'''.format(modulePath, moduleName)
            else:
                command = '''import {0};reload({0})'''.format(moduleName)
            #
            exec command


#
def setBasicPythonModuleUpdate():
    moduleLis = lxConfigure.LynxiPythonModule_Basic_Lis
    if lxBasic.isMayaApp():
        moduleLis += lxConfigure.LynxiPythonModule_Maya_Lis
    #
    if moduleLis:
        from LxCore import lxProgress
        # View Progress
        explain = '''Update Python Module(s)'''
        maxValue = len(moduleLis)
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        for i in moduleLis:
            modulePath = '.'.join(i.split('.')[:-1])
            moduleName = i.split('.')[-1]
            #
            progressBar.updateProgress(moduleName)
            #
            if modulePath:
                command = '''from {0} import {1};reload({1})'''.format(modulePath, moduleName)
            else:
                command = '''import {0};reload({0})'''.format(moduleName)
            #
            exec command


#
def setUpdate(force=0):
    localUpdate = _getLxLocalVersion()
    serverUpdate = _getLxServerVersion()
    #
    setMessageCountRest()
    #
    isUpdate = False
    #
    isLxPipelineTd = lxConfigure.isLxDevelop()
    #
    if not isLxPipelineTd:
        # Check Maya Version
        mayaFullVersion = lxBasic.getMayaAppFullVersion()
        if mayaFullVersion:
            if not mayaFullVersion == '201780':
                from LxCore import lxTip
                message01 = u'''您使用的 Maya 版本不是 2017 Update 5，'''
                message02 = u'''请联系 IT 升级你的 Maya 版本。'''
                lxTip.viewMessage(message01, message02)
        #
        if not localUpdate or localUpdate != serverUpdate:
            isUpdate = True
    #
    elif isLxPipelineTd:
        isUpdate = True
    #
    if force or isUpdate is True:
        from LxCore import lxTip
        #
        if not isLxPipelineTd:
            lxTip.deleteLynxiUi()
        #
        setBasicPythonModuleUpdate()
        #
        modulePath = lxConfigure.BasicPath().pythonRoot
        moduleLis = lxConfigure.getLxRelatedPythonModuleLis()
        setPythonModuleUpdate(modulePath, moduleLis)
        #
        setLocalUpdateTagRefresh()
        #
        lxTip.viewMessage(
            u'流程工具更新',
            u'成功'
        )

