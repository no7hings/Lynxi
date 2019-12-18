# coding:utf-8
from LxUi.qt import qtTip
#
from LxMaya.command import maUtils, maFur
#
selObj = maUtils.getSelectedObjectsFilter('pgYetiMaya')
#
if selObj:
    for i in selObj:
        maFur.setRenameYetiGraph(i)
#
qtTip.viewMessage('Rename Yeti - Graph ( Selected )', 'Complete')
