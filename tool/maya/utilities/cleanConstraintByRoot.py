# coding:utf-8
from LxBasic import bscMtdCore, bscObjects
#
from LxMaya.command import maUtils
#
selObjects = maUtils.getSelectedObjects()
#
if selObjects:
    [maUtils.setClearConstraintByRoot(i) for i in selObjects]
#
bscObjects.MessageWindow('Clean Constraint', 'Complete')
