# coding:utf-8
from LxUi.qt import qtTip
#
from LxMaya.command import maUtils
#
selObjects = maUtils.getSelectedObjects()
#
if selObjects:
    [maUtils.setClearConstraintByRoot(i) for i in selObjects]
#
qtTip.viewMessage('Clean Constraint', 'Complete')
