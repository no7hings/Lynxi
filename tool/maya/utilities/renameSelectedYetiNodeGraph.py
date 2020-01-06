# coding:utf-8
from LxUi.qt import qtCommands
#
from LxMaya.command import maUtils, maFur
#
selObj = maUtils.getSelectedObjectsFilter('pgYetiMaya')
#
if selObj:
    for i in selObj:
        maFur.setRenameYetiGraph(i)
#
qtCommands.setMessageWindowShow('Rename Yeti - Graph ( Selected )', 'Complete')
