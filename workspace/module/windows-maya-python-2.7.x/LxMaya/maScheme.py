# coding:utf-8
from LxBasic import bscMethods

from LxCore import lxScheme

from LxMaya.command import maUtils


class Shm_Resource(lxScheme.Shm_Resource):
    def __init__(self):
        self._initResource()

    @property
    def plugNameLis(self):
        return self.method_environ.getAsList(self.Environ_Key_Loadname_Plug)

    def loadPlugs(self):
        plugNameLis = self.plugNameLis
        
        unloadPlugLis = []
        # Get Unload Plugs
        for i in plugNameLis:
            print i
            if maUtils.isPlugLoaded(i) is False:
                unloadPlugLis.append(i)
        # Load Unload Plugs
        if unloadPlugLis:
            # View Progress
            progressBar = bscMethods.If_Progress(u'Load Plug(s)', len(unloadPlugLis))
            for plug in unloadPlugLis:
                progressBar.update(plug)
                maUtils.setPlugLoad(plug)
            #
            bscMethods.If_Message(u'Plug(s) Load', u'Complete')