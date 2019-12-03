# coding=utf-8
from LxCore.preset.prod import projectPr
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
