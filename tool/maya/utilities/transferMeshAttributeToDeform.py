# coding:utf-8
from LxBasic import bscMethods

from LxMaya.command import maUtils, maAttr
#
groupStringLis = maUtils.getSelectedNodeLis()
#
if groupStringLis:
    groupString = groupStringLis[0]
    datumLis = maUtils.getMeshShapeDeformDatumLis(groupString)
    if datumLis:
        maxValue = len(datumLis)
        progressBar = bscMethods.If_Progress('Transfer Attribute(s)', maxValue)
        for sourceNode, targetNode in datumLis:
            progressBar.update()
            #
            maAttr.setNodeRenderAttrTransfer(sourceNode, targetNode)
            maAttr.setNodePlugAttrTransfer(sourceNode, targetNode)
