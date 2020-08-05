# coding:utf-8
from LxBasic import bscMethods, bscObjects

from LxScheme import shmOutput

from LxMaya.command import maUtils


class Scheme(shmOutput.Scheme):
    def __init__(self):
        self._initScheme()

    @property
    def plugNames(self):
        return bscMethods.OsEnviron.getAsList(self.Environ_Key_Loadname_Plug)

    def loadPlugs(self):
        plugNameLis = self.plugNames
        
        unloadPlugLis = []
        # Get Unload Plugs
        for i in plugNameLis:
            if maUtils.isPlugLoaded(i) is False:
                unloadPlugLis.append(i)
        # Load Unload Plugs
        if unloadPlugLis:
            # View Progress
            progressBar = bscObjects.ProgressWindow(u'Load Plug(s)', len(unloadPlugLis))
            for plug in unloadPlugLis:
                progressBar.update(plug)
                maUtils.setPlugLoad(plug)
            #
            bscObjects.MessageWindow(u'Plug(s) Load', u'Complete')
