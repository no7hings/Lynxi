# coding:utf-8
from LxBasic import bscMethods, bscObjects

from LxScheme import shmOutput

from LxMaya.command import maUtils


class Resource(shmOutput.Resource):
    def __init__(self):
        self._initResource()

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
            progressBar = bscObjects.If_Progress(u'Load Plug(s)', len(unloadPlugLis))
            for plug in unloadPlugLis:
                progressBar.update(plug)
                maUtils.setPlugLoad(plug)
            #
            bscObjects.If_Message(u'Plug(s) Load', u'Complete')
