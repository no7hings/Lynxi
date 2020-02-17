# coding:utf-8
from LxBasic import bscCore, bscObjects
#
from LxMaya.command import maUtils, maFur
#
selObj = maUtils.getSelectedObjectsFilter('pgYetiMaya')
#
if selObj:
    for i in selObj:
        maFur.setRenameYetiGraph(i)
#
bscObjects.MessageWindow('Rename Yeti - Graph ( Selected )', 'Complete')
