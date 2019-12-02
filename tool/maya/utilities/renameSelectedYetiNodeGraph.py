# coding:utf-8
from LxCore import lxTip
#
from LxMaya.command import maUtils, maFur
#
selObj = maUtils.getSelectedObjectsFilter('pgYetiMaya')
#
if selObj:
    for i in selObj:
        maFur.setRenameYetiGraph(i)
#
lxTip.viewMessage('Rename Yeti - Graph ( Selected )', 'Complete')
