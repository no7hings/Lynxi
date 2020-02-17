# coding:utf-8
from LxBasic import bscCore, bscObjects
#
from LxMaya.command import maUtils
#
selObj = maUtils.getSelectedObjects()
attrName = 'ai_aov'
if selObj:
    for i in selObj:
        objectName = maUtils._getNodeNameString(i)
        if maUtils._isNodeExist(objectName + '.' + attrName):
            maUtils.setAttrStringDatum(i, attrName, objectName)
#
bscObjects.MessageWindow('Refresh Light AOV Attribute', 'Complete')
