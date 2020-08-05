# coding=utf-8
from LxBasic import bscObjects, bscMethods

from LxPreset import prsMethods

from LxCore import lxConfigure

from LxCore.preset import plugPr

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
                progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
                for plug in unloadPlugLis:
                    progressBar.update(plug)
                    maUtils.setPlugLoad(plug)
                #
                bscObjects.MessageWindow(u'Plug(s) Load', u'Complete')
            #
            currentRenderer = prsMethods.Project.mayaRenderer()
            maRender.setCurrentRenderer(currentRenderer)
        #
        lxConfigure.setLxVariantValue(IsMayaPlugLoadKey, True)
