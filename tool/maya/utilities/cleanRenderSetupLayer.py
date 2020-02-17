# coding:utf-8
from LxBasic import bscCore, bscObjects
#
from LxMaya.command import maUtils
#
nodes = maUtils.getNodeLisByType(u'renderSetupLayer')

logWin_ = bscObjects.LogWindow()
if nodes:
    for node in nodes:
        if not maUtils.isNodeLocked(node):
            if not maUtils.isReferenceNode(node):
                maUtils.setNodeDelete(node)
                logWin_.addResult(u'Delete "{}"'.format(node))
            else:
                logWin_.addWarning(u'"{}" is From Reference'.format(node))
        else:
            logWin_.addWarning(u'"{}" is Locked'.format(node))
    #
    logWin_.addResult(u'Render - Setup Layer is All - Clear')
else:
    logWin_.addWarning(u'Render - Setup Layer is Non - Exists')
