# coding:utf-8
from LxCore import lxTip
#
from LxMaya.command import maUtils
#
selObjects = maUtils.getSelectedObjects()
#
if selObjects:
    [maUtils.setClearConstraintByRoot(i) for i in selObjects]
#
lxTip.viewMessage('Clean Constraint', 'Complete')
