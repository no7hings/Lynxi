# coding:utf-8
from LxBasic import bscMethods
#
from LxMaya.command import maUtils
#
selObjects = maUtils.getSelectedObjects()
#
if selObjects:
    [maUtils.setClearConstraintByRoot(i) for i in selObjects]
#
bscMethods.If_Message('Clean Constraint', 'Complete')
