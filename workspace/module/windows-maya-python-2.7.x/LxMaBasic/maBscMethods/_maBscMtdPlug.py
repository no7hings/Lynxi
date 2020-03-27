# coding:utf-8
from LxMaBasic import myaBscMtdCore


class Plug(myaBscMtdCore.Mtd_MaBasic):
    @classmethod
    def names(cls):
        return cls.MOD_maya_cmds.pluginInfo(query=1, listPlugins=1)

    @classmethod
    def isLoaded(cls, plugName):
        return cls.MOD_maya_cmds.pluginInfo(plugName, query=1, loaded=1)

    @classmethod
    def load(cls, plugName):
        cls.MOD_maya_cmds.loadPlugin(plugName, quiet=1)
