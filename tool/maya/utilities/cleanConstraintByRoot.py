# coding:utf-8
from LxBasic import bscCore, bscObjects
#
from LxMaya.command import maUtils
#
selObjects = maUtils.getSelectedObjects()
#
if selObjects:
    [maUtils.setClearConstraintByRoot(i) for i in selObjects]
#
bscObjects.If_Message('Clean Constraint', 'Complete')
