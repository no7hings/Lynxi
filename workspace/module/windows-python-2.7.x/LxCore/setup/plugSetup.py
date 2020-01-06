# coding=utf-8
from LxCore import lxBasic, lxCore_
#
from LxCore.preset import plugPr
#
from LxCore.preset.prod import projectPr
#
IsMayaPlugLoadKey = 'IsMayaPlugLoaded'


#
def setMayaPlugSetup():
    if lxBasic.isMayaApp():
        from LxUi.qt import qtCommands  # import in Method

        isMayaPlugLoaded = lxCore_.getLxVariantValue(IsMayaPlugLoadKey)
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
                qtCommands.setMessageWindowShow(u'Plug(s) Load', u'Complete')
            #
            currentRenderer = projectPr.getProjectMayaRenderer()
            maRender.setCurrentRenderer(currentRenderer)
        #
        lxCore_.setLxVariantValue(IsMayaPlugLoadKey, True)
