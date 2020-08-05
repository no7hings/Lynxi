# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds


#
def setListIcon(ext):
    return cmds.resourceManager(nameFilter='*.%s' % ext)


#
def setCopyIcon(icons, targetPath):
    for i in icons:
        iconFile = targetPath + '/' + i
        cmds.resourceManager(saveAs=(i, iconFile))
