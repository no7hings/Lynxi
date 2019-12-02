# coding=utf-8
from LxCore import lxBasic, lxConfigure
#
from LxCore.preset.prod import projectPr
#
_pipelinePath = lxConfigure._getLxBasicPath()
#
_mayaVersion = lxBasic.getMayaAppVersion()
#
configExt = '.config'
#
none = ''


#
def getAutoLoadMayaPlugs():
    lis = []
    # Common Plugs
    commonPlugLis = projectPr.getProjectMayaCommonPlugLoadNames()
    lis.extend(commonPlugLis)
    # Custom Plugs
    customPlugLis = projectPr.getProjectMayaCustomPlugLoadNames()
    if customPlugLis:
        lis.extend(customPlugLis)
    return lis


def getMayaPlugSetupCommands():
    return projectPr.getProjectMayaCustomPlugSetupCommands()
