# coding=utf-8
from LxBasic import bscCore, bscObjects, bscMethods

from LxCore import lxConfigure

from LxCore.preset import plugPr

from LxCore.preset.prod import projectPr

IsMayaPlugLoadKey = 'IsMayaPlugLoaded'


def setMayaPlugSetup():
    if bscMethods.MayaApp.isActive():
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
                progressBar = bscObjects.If_Progress(progressExplain, maxValue)
                for plug in unloadPlugLis:
                    progressBar.update(plug)
                    maUtils.setPlugLoad(plug)
                #
                bscObjects.If_Message(u'Plug(s) Load', u'Complete')
            #
            currentRenderer = projectPr.getProjectMayaRenderer()
            maRender.setCurrentRenderer(currentRenderer)
        #
        lxConfigure.setLxVariantValue(IsMayaPlugLoadKey, True)
