# coding=utf-8
from LxPreset import prsMethods
#
none = ''


#
def getAutoLoadMayaPlugs():
    lis = []
    # Common Plugs
    commonPlugLis = prsMethods.Project.mayaCommonPlugLoadNames()
    lis.extend(commonPlugLis)
    # Custom Plugs
    customPlugLis = prsMethods.Project.mayaCustomPlugLoadNames()
    if customPlugLis:
        lis.extend(customPlugLis)
    return lis
