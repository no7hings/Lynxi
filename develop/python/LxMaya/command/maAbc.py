# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore.config import appCfg
#
from LxMaya.command import maUtils


#
def getGpuCacheFile(nodeSting):
    attr = nodeSting + '.cacheFileName'
    return cmds.getAttr(attr)


#
def getAlembicCacheFile(nodeSting):
    attr = nodeSting + '.abc_File'
    return cmds.getAttr(attr)


#
def getConnectAlembicNode(objectPath):
    return maUtils.getInputNodesFilterByType(objectPath, appCfg.MaNodeType_Alembic)


#
def getAlembicNodeFrameRange(alembicNode):
    return maUtils.getAttrDatum(alembicNode, 'startFrame'), maUtils.getAttrDatum(alembicNode, 'endFrame')
