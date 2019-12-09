# coding:utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore.config import appCfg


#
def getVolumeCacheFile(nodeSting):
    attr = nodeSting + '.filename'
    return cmds.getAttr(attr)
