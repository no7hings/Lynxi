# coding=utf-8
from LxBasic import bscCfg, bscObjects
#
from LxGui.qt import guiQtWidgets, qtMethod
#
from LxKit.qt import kitQtWgtAbs
#
from LxMaya.method import _maMethod
#
from LxMaya.interface.ifObjects import ifMaItemBasic
#
none = ''


#
class IfAstModelCheckViewerUnit(kitQtWgtAbs.IfToolUnitBasic):
    widthSet = 400
    VAR_kit__qt_wgt__unit__uiname = 'Model Check'
    VAR_kit__qt_wgt__unit__icon = 'window/geometryPanel'
    UnitWidth = 400
    UnitHeight = 800
    #
    UnitScriptJobWindowName = 'astModelMeshGeomCheckWindow'
    #
    app_check_method = _maMethod.MaCheckMethod
    ui_qt_method = qtMethod.QtViewMethod
    def __init__(self, *args, **kwargs):
        super(IfAstModelCheckViewerUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._kit__unit__set_build_()
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
        self._treeView = guiQtWidgets.QtTreeview()
        layout.addWidget(self._treeView)
        self._treeView.setSelectEnable(True)
        self._treeView.setColorEnable(True)
        self._treeView.setExpandEnable(True)
        self._treeView.selectedChanged.connect(self.setAppObjectSelect)
        #
        self._treeView.setKeywordFilterWidgetConnect(self.filterEnterLabel())
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
                ('Recheck All', 'svg_basic/checkaction', True, self.setListInspection),
                ('Fix All', 'svg_basic/fixaction', False)
            ]
            #
            treeView.setActionData(actionDatumLis)
        #
        groupLis = self.app_check_method.filterSelectedGroupLis()
        transformLis = self.app_check_method.filterSelectedTransformLis()
        geometryObjectLis = self.app_check_method.filterSelectedNodeTransformLis(nodeTypeString=['mesh'])
        treeView = self._treeView
        #
        methodDatumLis = [
            (self.setTreeViewListInspection, ('Check Group(s)', treeView, self.app_check_method.maAstModelGroupCheckConfigDic(), groupLis)),
            (self.setTreeViewListInspection, ('Check Transform(s)', treeView, self.app_check_method.maAstModelTransformCheckConfigDic(), transformLis)),
            (self.setTreeViewListInspection, ('Check Mesh(s)', treeView, self.app_check_method.maAstModelGeometryCheckConfigDic(), geometryObjectLis))
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
                    inspectionItem.setFilterColor(bscCfg.BscUtility.LynxiUi_ErrorRgba)
                    objectItem.setFilterColor(bscCfg.BscUtility.LynxiUi_ErrorRgba)
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
                    ('Recheck Current', 'svg_basic/checkaction', False),
                    ('Fix Current', 'svg_basic/fixaction', False)
                ]
                inspectionItem.setActionData(actionDatumLis, title=enExplain)
            #
            enable, enExplain, tooltip, filterMethod, fixMethod = value
            if enable is True:
                inspectionItem = guiQtWidgets.QtTreeItem()
                treeView.addItem(inspectionItem)
                #
                inspectionItem.setName(key)
                inspectionItem.setNameString(enExplain)
                inspectionItem.setTooltip(tooltip)
                if checkObjectLis:
                    setInspectionBranchAction()
                    if filterMethod is not None:
                        errorDic = filterMethod(checkObjectLis)
                        if errorDic:
                            setErrorSubBranch(errorDic)
                            #
                            subIconKeyword = 'svg_basic/checkerror'
                        else:
                            subIconKeyword = 'svg_basic/checkadopt'
                    else:
                        inspectionItem.setPressable(False)
                        subIconKeyword = 'svg_basic/checkdisable'
                else:
                    inspectionItem.setPressable(False)
                    subIconKeyword = 'svg_basic/checkdisable'
                #
                inspectionItem.setIcon('svg_basic/checklist')
                inspectionItem.setSubIcon(subIconKeyword)
        #
        self.app_check_method.setUndoChunkOpen()
        maxValue = len(checkConfigDic)
        progressBar = bscObjects.ProgressWindow(explain, maxValue)
        for s, (k, v) in enumerate(checkConfigDic.items()):
            progressBar.update(k)
            setInspectionBranch(s, k, v)
        #
        self.app_check_method.setUndoChunkClose()
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
            self.app_check_method.setNodeSelect(self.app_check_method._toAppExistStringList(lis), noExpand=True)
        else:
            self.app_check_method.setSelectClear()
    #
    def _kit__unit__set_build_(self):
        self.topToolBar().show()
        self.setupTreeView(self.mainLayout())
