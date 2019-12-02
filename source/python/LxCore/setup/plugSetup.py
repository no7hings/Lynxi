# coding=utf-8
from LxCore import lxBasic, lxConfigure, lxTip
#
from LxCore.preset import plugPr
#
from LxCore.preset.prod import projectPr
#
IsMayaPlugLoadKey = 'IsMayaPlugLoaded'


#
def setMayaPlugSetup():
    if lxBasic.isMayaApp():
        isMayaPlugLoaded = lxConfigure.getLxVariantValue(IsMayaPlugLoadKey)
        # Value is True, False or None
        if isMayaPlugLoaded is not True:
            from LxMaya.command import maUtils, maRender
            # Load Plug
            unloadPlugLis = []
            mayaPlugLoadNames = plugPr.getAutoLoadMayaPlugs()
            # Get Unload Plugs
            for plugLoadName in mayaPlugLoadNames:
                if plugLoadName:
                    if not maUtils.isPlugLoaded(plugLoadName):
                        unloadPlugLis.append(plugLoadName)
            # Load Unload Plugs
            if unloadPlugLis:
                # View Progress
                progressExplain = '''Load Plug(s)'''
                maxValue = len(unloadPlugLis)
                progressBar = maUtils.MaProgressBar().viewProgress(progressExplain, maxValue)
                for plug in unloadPlugLis:
                    progressBar.updateProgress(plug)
                    maUtils.setPlugLoad(plug)
                #
                lxTip.viewMessage(u'加载插件', u'成功')
            # Setup Plug
            mayaPlugSetupCommandLis = plugPr.getMayaPlugSetupCommands()
            if mayaPlugSetupCommandLis:
                progressExplain = '''Setup Plug(s)'''
                maxValue = len(mayaPlugSetupCommandLis)
                progressBar = maUtils.MaProgressBar().viewProgress(progressExplain, maxValue)
                for command in mayaPlugSetupCommandLis:
                    progressBar.updateProgress()
                    maUtils.runMelCommand(command)
                #
                lxTip.viewMessage(u'启动插件', u'成功')
            #
            currentRenderer = projectPr.getProjectMayaRenderer()
            maRender.setCurrentRenderer(currentRenderer)
            #
            setMayaPlugCheck()
        #
        lxConfigure.setLxVariantValue(IsMayaPlugLoadKey, True)


#
def setMayaPlugCheck(projectName=None):
    mayaPlugDatumDic = projectPr.getProjectMayaCustomPlugCheckDic(projectName)
    if mayaPlugDatumDic:
        from LxMaya.command import maUtils
        for plugName, (plugLoadNames, plugPath) in mayaPlugDatumDic.items():
            if plugLoadNames:
                for plugLoadName in plugLoadNames:
                    if plugLoadName:
                        if maUtils.isPlugRegistered(plugLoadName) is True:
                            lxConfigure.traceResult('{} ( {} ) Registered is Successful'.format(plugName, plugLoadName))
                            #
                            plugFile = maUtils.getPlugPath(plugLoadName)
                            if plugFile.lower().startswith(plugPath.lower()):
                                lxConfigure.traceResult('{} ( {} ) Path is Available'.format(plugName, plugFile))
                            else:
                                errorMessage = '{} ( {} ) Path is Unavailable'.format(plugName, plugFile)
                                lxConfigure.traceError(errorMessage)
                                lxConfigure.setErrorLogAdd(errorMessage)
                        else:
                            errorMessage = '{} ( {} ) Registered is Failed'.format(plugName, plugLoadName)
                            lxConfigure.traceError(errorMessage)
                            lxConfigure.setErrorLogAdd(errorMessage)
