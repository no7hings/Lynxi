# coding:utf-8
from LxMaya.command import maUtils, maAttr
#
groupStringLis = maUtils.getSelectedNodeLis()
#
if groupStringLis:
    groupString = groupStringLis[0]
    datumLis = maUtils.getMeshShapeDeformDatumLis(groupString)
    if datumLis:
        progressBar = maUtils.MaProgressBar()
        maxValue = len(datumLis)
        progressBar.viewProgress('Transfer Attribute(s)', maxValue)
        for sourceNode, targetNode in datumLis:
            progressBar.updateProgress()
            #
            maAttr.setNodeRenderAttrTransfer(sourceNode, targetNode)
            maAttr.setNodePlugAttrTransfer(sourceNode, targetNode)
