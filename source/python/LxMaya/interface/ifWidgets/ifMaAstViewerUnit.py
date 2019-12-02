# coding=utf-8
from LxCore import lxProgress
#
from LxUi.qt import uiWidgets
#
from LxInterface.qt.ifBasic import ifWidgetBasic
#
from LxCore.method import _uiMethod
#
from LxMaya.method import _maMethod
#
from LxMaya.interface.ifObjects import ifMaItemBasic
#
none = ''


#
class IfAstModelCheckViewerUnit(ifWidgetBasic.IfToolUnitBasic):
    widthSet = 400
    UnitTitle = 'Model Check'
    UnitIcon = 'window#geometryPanel'
    UnitWidth = 400
    UnitHeight = 800
    #
    UnitScriptJobWindowName = 'astModelMeshGeomCheckWindow'
    #
    _MaCheckMethod = _maMethod.MaCheckMethod
    _UiViewMethod = _uiMethod.UiViewMethod
    def __init__(self, *args, **kwargs):
        super(IfAstModelCheckViewerUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnit()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setScriptJob(self):
        pass
    #
    def delScriptJob(self):
        pass
    #
    def setupTreeView(self, layout):
        self._treeView = uiWidgets.UiTreeView()
        layout.addWidget(self._treeView)
        self._treeView.setSelectEnable(True)
        self._treeView.setColorEnable(True)
        self._treeView.setExpandEnable(True)
        self._treeView.selectedChanged.connect(self.setAppObjectSelect)
        #
        self._treeView.setFilterConnect(self.filterEnterLabel())
    #
    def setArgs(self, keyword, args):
        pass
    #
    def refreshMethod(self):
        self.setListInspection()
    #
    def setListInspection(self):
        def setAction():
            actionDatumLis = [
                ('Action(s)',),
                ('Recheck All', 'svg_basic@svg#checkAction', True, self.setListInspection),
                ('Fix All', 'svg_basic@svg#fixAction', False)
            ]
            #
            treeView.setActionData(actionDatumLis)
        #
        groupLis = self._MaCheckMethod.filterSelectedGroupLis()
        transformLis = self._MaCheckMethod.filterSelectedTransformLis()
        geometryObjectLis = self._MaCheckMethod.filterSelectedNodeTransformLis(nodeTypeString=['mesh'])
        treeView = self._treeView
        #
        methodDatumLis = [
            (self.setTreeViewListInspection, ('Check Group(s)', treeView, self._MaCheckMethod.maAstModelGroupCheckConfigDic(), groupLis)),
            (self.setTreeViewListInspection, ('Check Transform(s)', treeView, self._MaCheckMethod.maAstModelTransformCheckConfigDic(), transformLis)),
            (self.setTreeViewListInspection, ('Check Mesh(s)', treeView, self._MaCheckMethod.maAstModelGeometryCheckConfigDic(), geometryObjectLis))
        ]
        #
        treeView.cleanItems()
        [method(*args) for method, args in methodDatumLis]
        treeView.setRefresh()
        setAction()
    #
    def setTreeViewListInspection(self, explain, treeView, checkConfigDic, checkObjectLis):
        # noinspection PyUnusedLocal
        def setInspectionBranch(seq, key, value):
            def setErrorSubBranch(errorData):
                def setObjectBranch(objectPath, compLis):
                    def setCompBranch(compPath):
                        compItem = ifMaItemBasic.IfMaNodeTreeItem()
                        objectItem.addChild(compItem)
                        #
                        compItem.load(compPath)
                    #
                    objectItem = ifMaItemBasic.IfMaNodeTreeItem()
                    objectItem.loadNode(objectPath)
                    inspectionItem.addChild(objectItem)
                    #
                    inspectionItem.setFilterColor(self.LynxiUi_ErrorRgba)
                    objectItem.setFilterColor(self.LynxiUi_ErrorRgba)
                    if compLis:
                        for c in compLis:
                            setCompBranch(c)
                #
                if isinstance(errorData, dict):
                    for ik, iv in errorData.items():
                        setObjectBranch(ik, iv)
                elif isinstance(errorData, list):
                    for i in errorData:
                        setObjectBranch(i, None)
            #
            def setInspectionBranchAction():
                actionDatumLis = [
                    ('Action(s)', ),
                    ('Recheck Current', 'svg_basic@svg#checkAction', False),
                    ('Fix Current', 'svg_basic@svg#fixAction', False)
                ]
                inspectionItem.setActionData(actionDatumLis, title=enExplain)
            #
            enable, enExplain, tooltip, filterMethod, fixMethod = value
            if enable is True:
                inspectionItem = uiWidgets.UiTreeItem()
                treeView.addItem(inspectionItem)
                #
                inspectionItem.setName(key)
                inspectionItem.setNameText(enExplain)
                inspectionItem.setTooltip(tooltip)
                if checkObjectLis:
                    setInspectionBranchAction()
                    if filterMethod is not None:
                        errorDic = filterMethod(checkObjectLis)
                        if errorDic:
                            setErrorSubBranch(errorDic)
                            #
                            subIconKeyword = 'svg_basic@svg#checkError'
                        else:
                            subIconKeyword = 'svg_basic@svg#checkAdopt'
                    else:
                        inspectionItem.setPressable(False)
                        subIconKeyword = 'svg_basic@svg#checkDisable'
                else:
                    inspectionItem.setPressable(False)
                    subIconKeyword = 'svg_basic@svg#checkDisable'
                #
                inspectionItem.setIcon('svg_basic@svg#checklist')
                inspectionItem.setSubIcon(subIconKeyword)
        #
        self._MaCheckMethod.setUndoChunkOpen()
        maxValue = len(checkConfigDic)
        progressBar = lxProgress.viewSubProgress(explain, maxValue)
        for s, (k, v) in enumerate(checkConfigDic.items()):
            progressBar.updateProgress(k)
            setInspectionBranch(s, k, v)
        #
        self._MaCheckMethod.setUndoChunkClose()
    #
    def setAppObjectSelect(self):
        treeView = self._treeView
        selectedItemLis = treeView.selectedItems()
        if selectedItemLis:
            lis = []
            for i in selectedItemLis:
                if hasattr(i, 'appPath'):
                    lis.append(i.appPath)
            #
            self._MaCheckMethod.setNodeSelect(self._MaCheckMethod._toNodeLis(lis), noExpand=True)
        else:
            self._MaCheckMethod.setSelectClear()
    #
    def setupUnit(self):
        self.topToolBar().show()
        self.setupTreeView(self.mainLayout())
