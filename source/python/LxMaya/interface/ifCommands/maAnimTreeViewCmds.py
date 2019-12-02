# coding=utf-8
from LxCore.preset import appVariant
#
from LxUi.qt import uiWidgets_
#
from LxMaya.product.data import datAnim
# File Label
astLayoutRigFileLabel = appVariant.astLayoutRigFileLabel
astAnimationRigFileLabel = appVariant.astAnimationRigFileLabel
astSimulationRigFileLabel = appVariant.astSimulationRigFileLabel
# Utilities Label
infoNonExistsLabel = appVariant.infoNonExistsLabel
# Type Config
typeSet = appVariant.astBasicClassifications
typeLabel = appVariant.assetClassifyAbbDic
typeDic = appVariant.assetClassifyFullDic
#
none = ''


#
def setAnimationAssetMeshCheck(treeItem, localData, serverData, columnSet):
    checkResults = datAnim.getAnimationSceneMeshConstant(localData, serverData)
    pathCheck = ['Error', 'On'][checkResults[0]]
    geomCheck = ['Error', 'On'][checkResults[1]]
    geomShapeCheck = ['Error', 'On'][checkResults[2]]
    mapCheck = ['Error', 'On'][checkResults[3]]
    mapShapeCheck = ['Error', 'On'][checkResults[4]]
    #
    statusBar = uiWidgets_.xTreeLabelBar()
    statusBar.addItem('object#meshPath', pathCheck)
    statusBar.addItem('object#meshGeo', geomCheck)
    statusBar.addItem('object#meshGeoShape', geomShapeCheck)
    statusBar.addItem('object#meshMap', mapCheck)
    statusBar.addItem('object#meshMapShape', mapShapeCheck)
    #
    treeItem.setItemWidget(columnSet, statusBar)
