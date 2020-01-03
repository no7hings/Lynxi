# coding=utf-8
from LxCore import lxCore_
#
from LxCore.config import appCfg
#
from LxCore.preset import appVariant
#
from LxCore.preset.prod import projectPr
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
    timeUnit = projectPr.getProjectMayaTimeUnit(projectName=projectName)
    if not timeUnit == lxCore_.LynxiValue_Unspecified:
        defineUnit = getMayaTimeUnit(timeUnit)
        currentUnit = maUtils.getTimeUnit()
        if defineUnit != currentUnit:
            maUtils.setTimeUnit(defineUnit)
            maUtils.viewMessage(
                u'Time - Unit has Switch to',
                u'%s' % timeUnit
            )


#
def setAnimationTime():
    startFrame = appVariant.animStartFrame
    maUtils.setAnimationFrameRange(startFrame, startFrame + 100)
    maUtils.setCurrentFrame(startFrame)
