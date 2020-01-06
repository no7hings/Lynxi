# coding:utf-8
from LxUi.qt import qtCommands
#
from LxMaya.command import maUtils
#
selObjects = maUtils.getSelectedObjects()
#
if selObjects:
    [maUtils.setClearConstraintByRoot(i) for i in selObjects]
#
qtCommands.setMessageWindowShow('Clean Constraint', 'Complete')
