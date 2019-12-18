# coding:utf-8
from LxUi.qt import qtTip
#
from LxMaya.command import maUtils
reload(maUtils)
#
selObj = maUtils.getSelectedObjects()
attrName = 'ai_aov'
if selObj:
    for i in selObj:
        objectName = maUtils._toNodeName(i)
        if maUtils.isAppExist(objectName + '.' + attrName):
            maUtils.setAttrStringDatum(i, attrName, objectName)
#
qtTip.viewMessage('Refresh Light AOV Attribute', 'Complete')
