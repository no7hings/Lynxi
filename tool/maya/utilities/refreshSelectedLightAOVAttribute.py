# coding:utf-8
from LxBasic import bscMethods
#
from LxMaya.command import maUtils
#
selObj = maUtils.getSelectedObjects()
attrName = 'ai_aov'
if selObj:
    for i in selObj:
        objectName = maUtils._toNodeName(i)
        if maUtils.isAppExist(objectName + '.' + attrName):
            maUtils.setAttrStringDatum(i, attrName, objectName)
#
bscMethods.If_Message('Refresh Light AOV Attribute', 'Complete')
