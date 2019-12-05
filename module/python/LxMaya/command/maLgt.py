# coding=utf-8
# noinspection PyUnresolvedReferences
import maya.cmds as cmds
#
from LxCore.config import appCfg
#
from LxMaya.command import maUtils


#
def getLightObjectLis(root=None):
    if root is not None:
        filterTypes = maUtils.getNodeTypeLisByFilter(appCfg.MaNodeType_Light)
        lis = maUtils.getChildObjectsByRoot(root, filterTypes)
    else:
        lis = cmds.ls(lights=1, noIntermediate=1, long=1) or []
    return lis


#
def getLightGraphData(lightObject):
    def getBranch(mNode):
        if not mNode in transforms and not mNode in nodes:
            if maUtils.isTransform(mNode):
                objectPath = maUtils._getNodePathString(mNode)
                mNode = maUtils.getNodeShape(objectPath)
                #
                transforms.append(objectPath)
            else:
                nodes.append(mNode)
            #
            branchNodes = maUtils.getInputShapeLis(mNode)
            if branchNodes:
                [getBranch(i) for i in branchNodes]
    #
    transforms = []
    nodes = []
    #
    getBranch(lightObject)
    return transforms, nodes
