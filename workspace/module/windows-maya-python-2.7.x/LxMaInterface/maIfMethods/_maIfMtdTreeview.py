# coding:utf-8
from LxUi.qt import qtWidgets_


class SceneAssetTreeitem(object):
    @classmethod
    def setMeshCheck(cls, treeitem, column, checkResults):
        pathCheck = ['error', 'on'][checkResults[0]]
        geomCheck = ['error', 'on'][checkResults[1]]
        geomShapeCheck = ['error', 'on'][checkResults[2]]
        mapCheck = ['error', 'on'][checkResults[3]]
        mapShapeCheck = ['error', 'on'][checkResults[4]]
        #
        statusBar = qtWidgets_.xTreeLabelBar()
        statusBar.addItem('object#meshPath', pathCheck)
        statusBar.addItem('object#meshGeo', geomCheck)
        statusBar.addItem('object#meshGeoShape', geomShapeCheck)
        statusBar.addItem('object#meshMap', mapCheck)
        statusBar.addItem('object#meshMapShape', mapShapeCheck)
        #
        treeitem.setItemWidget(column, statusBar)


