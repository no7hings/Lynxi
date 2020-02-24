# coding:utf-8
from LxBasic import bscMtdCore, bscObjects
#
from LxMaya.command import maUtils
#
selObj = maUtils.getSelectedObjects()
attrName = 'ai_aov'
if selObj:
    for i in selObj:
        objectName = maUtils._nodeString2nodename_(i)
        if maUtils._isAppExist(objectName + '.' + attrName):
            maUtils.setAttrStringDatum(i, attrName, objectName)
#
bscObjects.MessageWindow('Refresh Light AOV Attribute', 'Complete')
