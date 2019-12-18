# coding:utf-8
from LxUi.qt import qtLog
#
from LxMaya.command import maUtils
#
nodes = maUtils.getNodeLisByType('renderSetupLayer')
logLis = []
logWin = qtLog.viewLogWin_()
if nodes:
    for node in nodes:
        if not maUtils.isNodeLocked(node):
            if not maUtils.isReferenceNode(node):
                maUtils.setNodeDelete(node)
                qtLog.viewResult(logWin, 'Result : Delete "{}"'.format(node))
            else:
                qtLog.viewWarning(logWin, 'Warning : "{}" is From Reference'.format(node))
        else:
            qtLog.viewWarning(logWin, 'Warning : "{}" is Locked'.format(node))
    #
    qtLog.viewResult(logWin, 'Render - Setup Layer is All - Clear')
else:
    qtLog.viewWarning(logWin, 'Render - Setup Layer is Non - Exists')
