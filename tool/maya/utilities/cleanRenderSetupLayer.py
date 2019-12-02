# coding:utf-8
from LxCore import lxTip, lxLog
#
from LxMaya.command import maUtils
#
nodes = maUtils.getNodeLisByType('renderSetupLayer')
logLis = []
logWin = lxLog.viewLogWin_()
if nodes:
    for node in nodes:
        if not maUtils.isNodeLocked(node):
            if not maUtils.isReferenceNode(node):
                maUtils.setNodeDelete(node)
                lxLog.viewResult(logWin, 'Result : Delete "{}"'.format(node))
            else:
                lxLog.viewWarning(logWin, 'Warning : "{}" is From Reference'.format(node))
        else:
            lxLog.viewWarning(logWin, 'Warning : "{}" is Locked'.format(node))
    #
    lxLog.viewResult(logWin, 'Render - Setup Layer is All - Clear')
else:
    lxLog.viewWarning(logWin, 'Render - Setup Layer is Non - Exists')
