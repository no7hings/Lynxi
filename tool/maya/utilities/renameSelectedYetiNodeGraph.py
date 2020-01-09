# coding:utf-8
from LxBasic import bscMethods
#
from LxMaya.command import maUtils, maFur
#
selObj = maUtils.getSelectedObjectsFilter('pgYetiMaya')
#
if selObj:
    for i in selObj:
        maFur.setRenameYetiGraph(i)
#
bscMethods.If_Message('Rename Yeti - Graph ( Selected )', 'Complete')
