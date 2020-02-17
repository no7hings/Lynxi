# coding=utf-8
from LxPreset import prsConfigure, prsVariants, prsMethods
#
from LxCore.config import appCfg
#
from LxMaya.command import maUtils
#
none = ''


#
def getMayaTimeUnit(timeUnit):
    dic = appCfg.MaUnit_UiDic_Time
    if timeUnit in dic:
        return dic[timeUnit]
    else:
        return timeUnit


#
def setAnimationTimeUnit(projectName=none):
    timeUnit = prsMethods.Project.mayaTimeUnit(projectName=projectName)
    if not timeUnit == prsConfigure.Utility.DEF_value_preset_unspecified:
        defineUnit = getMayaTimeUnit(timeUnit)
        currentUnit = maUtils.getTimeUnit()
        if defineUnit != currentUnit:
            maUtils.setTimeUnit(defineUnit)
            maUtils.setMessageWindowShow(
                u'Time - Unit has Switch to',
                u'%s' % timeUnit
            )


#
def setAnimationTime():
    startFrame = prsVariants.Util.animStartFrame
    maUtils.setAnimationFrameRange(startFrame, startFrame + 100)
    maUtils.setCurrentFrame(startFrame)
