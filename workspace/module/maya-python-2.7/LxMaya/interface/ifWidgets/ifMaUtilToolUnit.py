# coding=utf-8
from itertools import product
#
from LxBasic import bscMtdCore, bscMethods, bscObjects

from LxPreset import prsMethods
#
from LxCore.config import appCfg
#
from LxGui.qt import qtWidgets_, guiQtWidgets, qtCore
#
from LxKit.qt import kitQtWgtAbs
#
from LxMaya.interface.ifCommands import maUtilsTreeViewCmds
#
from LxMaya.method import _maUiMethod
#
from LxMaya.command import maUtils, maUuid, maGeom, maDir
#
from LxMaya.product.op import animOp
#
none = ''


#
class IfAttributeManagerUnit(kitQtWgtAbs.IfToolUnitBasic):
    projectName = prsMethods.Project.mayaActiveName()
    #
    VAR_kit__qt_wgt__unit__uiname = 'Attribute Manager'
    UnitWidth = 800
    UnitHeight = 800
    #
    UnitScriptJobWindowName = 'utilsAttributeManagerWindow'
    #
    widthSet = 800
    #
    w = 80
    # Utilities Tool
    dic_config = {
        0: 'Config',
        'useShape': [0, 1, 0, 1, 2, 'Use Shape'],
        'nodeType': [0, 2, 0, 1, 2, '0000'], 'getAttr': [0, 2, 2, 1, 1, 'List Attribute(s)', 'svg_basic/list'], 'getNode': [0, 2, 3, 1, 1, 'List Nde_Node(s)', 'svg_basic/list'],
        3: 'Available',
        'availableSearch': [0, 4, 0, 1, 2, None], 'addAttr': [0, 4, 2, 1, 2, 'Add Attribute(s)', 'svg_basic/add'],
        'treeView': [0, 5, 0, 1, 4, None],
    }
    #
    dic_action = {
        'activeSearch': [0, 0, 0, 1, 2, None], 'removeAttr': [1, 0, 2, 1, 2, 'Remove Attribute(s)', 'svg_basic/remove'],
        'treeView': [0, 1, 0, 1, 4, None],
        'setAttr': [0, 2, 0, 1, 4, 'Set Attribute(s)', 'svg_basic/modify']
    }

    def __init__(self, *args, **kwargs):
        super(IfAttributeManagerUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._kit__unit__set_build_()
        #
        self.setNodeTreeViewBox()
        self.setAttrTreeViewBox()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        if self._connectObject:
            self.setListNodeTypes()
            self.setSelectedNodeType()
            #
            self.setScriptJob()
            self.connectObject().setQuitConnect(self.delScriptJob)
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        method = [self.setSelectedNodeType, self.setRefreshTreeViewBoxSelection]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, method)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupConnection(self):
        self.refreshButton().clicked.connect(self.setListNode)
    #
    def _kit__unit__set_left_build_(self, layout):
        toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Config(s)')
        self.setupConfigToolUiBox(toolBox)
        #
        toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Actions(s)')
        self.setupActionToolUiBox(toolBox)
    #
    def setupConfigToolUiBox(self, toolBox):
        toolBox.setUiData(self.dic_config)
        #
        self._useShapeButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('useShape', self._useShapeButton)
        self._useShapeButton.setChecked(True)
        #
        self.nodeTypeLabel = guiQtWidgets.QtValueLine()
        toolBox.addInfo('nodeType', self.nodeTypeLabel)
        self.nodeTypeLabel.setChooseEnable(True)
        #
        self.getAttrButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('getAttr', self.getAttrButton)
        self.getAttrButton.clicked.connect(self.setListAvailableAttr)
        #
        self.getNodeButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('getNode', self.getNodeButton)
        self.getNodeButton.clicked.connect(self.setListNode)
        #
        self.availableSearchBar = guiQtWidgets.QtFilterLine()
        toolBox.addButton('availableSearch', self.availableSearchBar)
        #
        self.addAttrButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('addAttr', self.addAttrButton)
        self.addAttrButton.setPressable(False)
        self.addAttrButton.clicked.connect(self.setListActiveAttr)
        #
        self._availableAttrTreeView = qtWidgets_.QTreeWidget_()
        toolBox.addButton('treeView', self._availableAttrTreeView)
        #
        toolBox.addSeparators()
    #
    def setupActionToolUiBox(self, toolBox):
        toolBox.setUiData(self.dic_action)
        #
        self.activeSearchBar = guiQtWidgets.QtFilterLine()
        toolBox.addButton('activeSearch', self.activeSearchBar)
        #
        self.removeAttrButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('removeAttr', self.removeAttrButton)
        self.removeAttrButton.setPressable(False)
        self.removeAttrButton.clicked.connect(self.setRemoveAttr)
        #
        self._activeAttrTreeView = qtWidgets_.QTreeWidget_()
        toolBox.addButton('treeView', self._activeAttrTreeView)
        #
        self.setAttrButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('setAttr', self.setAttrButton)
        self.setAttrButton.setPressable(False)
        self.setAttrButton.clicked.connect(self.setAttr)
        #
        toolBox.addSeparators()
    #
    def setupRightWidget(self, layout):
        self.nodeTreeViewBox = qtWidgets_.QTreeWidget_()
        layout.addWidget(self.nodeTreeViewBox)
        #
        self.nodeTreeViewBox.itemSelectionChanged.connect(self.setSetAttrBtnState)
    #
    def setNodeTreeViewBox(self):
        def setActionData():
            actions = [
                ('Refresh', 'svg_basic/refresh', True, self.setListNode),
                (),
                ('Select All', 'svg_basic/checkedall', True, self.setNodeSelectAll),
                ('Select Clear', 'svg_basic/uncheckedall', True, self.setNodeSelectClear),
            ]
            treeBox.setActionData(actions)
        #
        self._nodeTreeItemDic = {}
        #
        treeBox = self.nodeTreeViewBox
        #
        maxWidth = self.widthSet / 2 - 40
        #
        treeBox.setColumns(
            ['Nde_Node', 'Lock State'],
            [3, 1],
            maxWidth
        )
        #
        treeBox.itemSelectionChanged.connect(self.setNodeSelCmd)
        treeBox.setKeywordFilterWidgetConnect(self.filterEnterLabel())
        #
        setActionData()
    #
    def setAttrTreeViewBox(self):
        self._availableAttrDatumDic = {}
        #
        self.availableAttrTreeItemDic = {}
        self.activeAttrTreeItemDic = {}
        #
        self._availableAttrTreeView.setColumns(
            ['Name', 'Type'],
            [3, 1],
            self.widthSet / 2 - 80
        )
        self._availableAttrTreeView.itemSelectionChanged.connect(self.setAddAttrBtnState)
        self._availableAttrTreeView.setKeywordFilterWidgetConnect(self.availableSearchBar)
        #
        self._activeAttrTreeView.setColumns(
            ['Name', 'Value'],
            [3, 1],
            self.widthSet / 2 - 80
        )
        self._activeAttrTreeView.itemSelectionChanged.connect(self.setRmvAttrBtnState)
        self._activeAttrTreeView.itemSelectionChanged.connect(self.setSetAttrBtnState)
        self._activeAttrTreeView.setKeywordFilterWidgetConnect(self.activeSearchBar)
    #
    def setListNodeTypes(self):
        chooseLabel = self.nodeTypeLabel
        #
        nodeTypes = maUtils.getNodeTypes()
        nodeTypes.sort()
        chooseLabel.setDatumLis(nodeTypes)
    #
    def setSelectedNodeType(self):
        chooseLabel = self.nodeTypeLabel
        #
        isUseShape = self._useShapeButton.isChecked()
        selectedNodes = maUtils.getSelectedObjects(1)
        if selectedNodes:
            node = selectedNodes[0]
            if isUseShape:
                shapePath = maUtils._dcc_getNodShapeNodepathStr(node, 1)
                if maUtils._isAppExist(shapePath):
                    node = shapePath
            nodeType = maUtils._getNodeCategoryString(node)
            chooseLabel.setChoose(nodeType)
    #
    def setListNode(self):
        treeBox = self.nodeTreeViewBox
        nodeType = self._getNodeCategoryString()
        nodes = maUtils.getNodeLisByType(nodeType, 1)
        #
        self._nodeTreeItemDic = {}
        #
        treeBox.clear()
        if nodes:
            maxValue = len(nodes)
            for seq, node in enumerate(nodes):
                if self._connectObject:
                    self._connectObject.setProgressValue(seq + 1, maxValue)
                #
                nodeName = maUtils._nodeString2nodename_(node, useMode=1)
                #
                nodeItem = qtWidgets_.QTreeWidgetItem_([node])
                treeBox.addItem(nodeItem)
                #
                nodeItem.name = nodeName
                nodeItem.path = node
                #
                isLock = maUtils.isNodeLocked(node)
                state = ['Normal', 'Lock'][isLock]
                #
                nodeItem.setItemMayaIcon(0, nodeType)
                nodeItem.setText(0, nodeName)
                nodeItem.setText(1, state)
                #
                self._nodeTreeItemDic[node] = nodeItem
        #
        treeBox.setFilterExplainRefresh()
    #
    def setListAvailableAttr(self):
        self._availableAttrDatumDic = {}
        #
        self.availableAttrTreeItemDic = {}
        self.activeAttrTreeItemDic = {}
        #
        treeBox = self._availableAttrTreeView
        subTreeBox = self._activeAttrTreeView
        #
        isUseShape = self._useShapeButton.isChecked()
        selectedNodes = maUtils.getSelectedObjects(1)
        if selectedNodes:
            node = selectedNodes[0]
            if isUseShape:
                shapePath = maUtils._dcc_getNodShapeNodepathStr(node, 1)
                if maUtils._isAppExist(shapePath):
                    node = shapePath
            #
            datumLis = maUtils.getNodeAttrModifyDatumLis(node)
            treeBox.clear()
            subTreeBox.clear()
            if datumLis:
                datumLis.sort()
                for seq, attrData in enumerate(datumLis):
                    attrName, value, dataType = attrData
                    if self._connectObject:
                        self._connectObject.updateProgress()
                    #
                    treeItem = qtWidgets_.QTreeWidgetItem_()
                    treeBox.addItem(treeItem)
                    #
                    treeItem.name = attrName
                    #
                    treeItem.setItemIcon_(0, 'svg_basic/attribute')
                    treeItem.setText(0, attrName)
                    treeItem.setText(1, dataType)
                    #
                    self._availableAttrDatumDic[treeItem] = attrName, value, dataType
                    #
                    self.availableAttrTreeItemDic[attrName] = treeItem
        #
        treeBox.setFilterExplainRefresh()
    #
    def setListActiveAttr(self):
        treeBox = self._activeAttrTreeView
        #
        activeTreeItemDic = self.activeAttrTreeItemDic
        #
        selItemLis = self.getAvailableSelItemLis()
        if selItemLis:
            for treeItem_ in selItemLis:
                attrName, value, dataType = self._availableAttrDatumDic[treeItem_]
                if not attrName in activeTreeItemDic:
                    treeItem = qtWidgets_.QTreeWidgetItem_()
                    treeBox.addItem(treeItem)
                    #
                    if dataType == 'int':
                        itemWidget = guiQtWidgets.QtValueArrayLine()
                        itemWidget.setEnterEnable(True)
                        itemWidget.setDefaultValue(int(value))
                        treeBox.setItemWidget(treeItem, 1, itemWidget)
                    elif dataType == 'float':
                        itemWidget = guiQtWidgets.QtValueArrayLine()
                        itemWidget.setEnterEnable(True)
                        itemWidget.setDefaultValue(float(value))
                        treeBox.setItemWidget(treeItem, 1, itemWidget)
                    elif dataType == 'bool':
                        itemWidget = guiQtWidgets.QtValueLine()
                        itemWidget.setCheckEnable(True)
                        itemWidget.setChecked(bool(value))
                        treeBox.setItemWidget(treeItem, 1, itemWidget)
                    #
                    treeItem.name = attrName
                    #
                    treeItem.setItemIcon_(0, 'svg_basic/attribute')
                    treeItem.setText(0, attrName)
                    #
                    activeTreeItemDic[attrName] = treeItem
                else:
                    treeItem = activeTreeItemDic[attrName]
                    treeItem.setHidden(False)
                #
                treeItem_.setItemIcon_(0, 'svg_basic/attribute', 'on')
        #
        treeBox.setFilterExplainRefresh()
    #
    def setRemoveAttr(self):
        treeBox = self._activeAttrTreeView
        availableAttrTreeItemDic = self.availableAttrTreeItemDic
        #
        items = self.getActiveSelItemLis()
        if items:
            for i in items:
                attrName = i.name
                i.setHidden(True)
                if attrName in availableAttrTreeItemDic:
                    treeItem = availableAttrTreeItemDic[attrName]
                    treeItem.setItemIcon_(0, 'svg_basic/attribute', none)
        #
        treeBox.clearSelection()
    #
    def setAttr(self):
        attrDatumDic = self.getActiveAttrDatumDic()
        #
        nodeLis = self.getSelNode()
        attrNameLis = self.getSelAttr()
        if nodeLis and attrNameLis:
            maxValue = len(nodeLis) * len(attrNameLis)
            for seq, (nodeName, attrName) in enumerate(product(nodeLis, attrNameLis)):
                if self._connectObject:
                    self._connectObject.setProgressValue(seq + 1, maxValue)
                if attrName in attrDatumDic:
                    attrName, attrDatum = attrDatumDic[attrName]
                    maUtils.setAttrDatumForce_(nodeName, attrName, attrDatum)
    #
    def setNodeSelectAll(self):
        treeBox = self.nodeTreeViewBox
        treeBox.setSelectAll()
        #
        self.setSelObjForAction()
    #
    def setNodeSelectClear(self):
        treeBox = self.nodeTreeViewBox
        treeBox.clearSelection()
        #
        self.setSelObjForAction()
    #
    def setNodeSelCmd(self):
        treeBox = self.nodeTreeViewBox
        #
        if treeBox.hasFocus():
            data = treeBox.selectedItemPaths()
            if data:
                maUtils.setNodeSelect(data, noExpand=True)
            else:
                maUtils.setSelClear()
    #
    def setSelObjForAction(self):
        treeBox = self.nodeTreeViewBox
        #
        data = treeBox.selectedItemPaths()
        if data:
            maUtils.setUpdateSel(data)
        else:
            maUtils.setSelClear()
    #
    def setGetAttrBtnState(self):
        button = self.getAttrButton
        boolean = maUtils.getSelectedObjects(1) != []
        #
        button.setState(['off', 'normal'][boolean])
    #
    def setGetNodeBtnState(self):
        button = self.getNodeButton
        boolean = self._getNodeCategoryString() != none
        #
        button.setState(['off', 'normal'][boolean])
    #
    def setAddAttrBtnState(self):
        inData = self.getAvailableSelItemLis()
        button = self.addAttrButton
        #
        button.setPressable([False, True][len(inData) > 0])
        button.setNameString('Add Attribute(s) [ %s ]' % str(len(inData)).zfill(4))
    #
    def setRmvAttrBtnState(self):
        inData = self.getActiveSelItemLis()
        button = self.removeAttrButton
        #
        button.setPressable([False, True][len(inData) > 0])
        button.setNameString('Remove Attribute(s) [ %s ]' % str(len(inData)).zfill(4))
    #
    def setSetAttrBtnState(self):
        inData = self.getSelNode()
        subData = self.getSelAttr()
        #
        button = self.setAttrButton
        boolean = len(inData) > 0 and len(subData) > 0
        #
        button.setPressable([False, True][boolean])
        button.setNameString('Set Attribute(s) [ %s * %s ]' % (str(len(inData)).zfill(4), str(len(subData)).zfill(4)))
    #
    def setRefreshTreeViewBoxSelection(self):
        if not self.nodeTreeViewBox.hasFocus():
            isUseShape = self._useShapeButton.isChecked()
            #
            treeItemDic = self._nodeTreeItemDic
            selNodeLis = maUtils.getSelectedObjects(1)
            if isUseShape:
                selNodeLis = maUtils.getSelectedObjects(fullPath=1, useShape=1)
            #
            if treeItemDic:
                for k, v in treeItemDic.items():
                    if k in selNodeLis:
                        v.setSelected(True)
                    else:
                        v.setSelected(False)
    #
    def getActiveAttrDatumDic(self):
        dic = {}
        datumDic = self._activeAttrTreeView.itemWidgetDatumDic(column=(0, 2))
        if datumDic:
            for k, v in datumDic.items():
                dic[k.text(0)] = v
        return dic
    #
    def getSelNode(self):
        treeBox = self.nodeTreeViewBox
        #
        nodes = treeBox.selectedItemPaths()
        return nodes
    #
    def getAvailableSelItemLis(self):
        return self._availableAttrTreeView.selectedItems()
    #
    def getActiveSelItemLis(self):
        return self._activeAttrTreeView.selectedItems()
    #
    def getSelAttr(self):
        return self._activeAttrTreeView.selectedItemTexts()
    #
    def _getNodeCategoryString(self):
        chooseLabel = self.nodeTypeLabel
        #
        message = chooseLabel.datum()
        return str(message)
    #
    def _kit__unit__set_build_(self):
        self.topToolBar().show()
        #
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        #
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(leftExpandWidget)
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self._kit__unit__set_left_build_(leftScrollArea)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        rightWidgetLayout = qtCore.QVBoxLayout_(widget)
        rightWidgetLayout.setContentsMargins(0, 0, 0, 0)
        rightWidgetLayout.setSpacing(2)
        self.setupRightWidget(rightWidgetLayout)


#
class IfNamespaceManagerUnit(
    kitQtWgtAbs.IfToolUnitBasic,
    _maUiMethod.Mtd_MaQtView
):
    projectName = prsMethods.Project.mayaActiveName()
    VAR_kit__qt_wgt__unit__uiname = 'Namespace Manager'
    panelWidth = 800
    panelHeight = 800
    #
    UnitScriptJobWindowName = 'namespaceManagerScriptJobWindow'
    widthSet = 800
    w = 120
    # View
    dicNs = {
        'namespacePath': [w, 0, 0, 1, 4, 'Namespace Path'],
        # 1
        'repairReferenceNodeError': [0, 2, 0, 1, 4, 'Reference Nde_Node'],
        'repairNamespaceError': [0, 3, 0, 1, 4, 'Namespace'],
        'cleanupNamespace': [0, 4, 0, 1, 4, 'Cleanup Namespace']
    }
    # View
    dicNd = {
        'nodePath': [w, 0, 0, 1, 4, 'Nde_Node Path']
    }
    def __init__(self, *args, **kwargs):
        super(IfNamespaceManagerUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._kit__unit__set_build_()
        #
        self.setScriptJob()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        method = []
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, method)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def _kit__unit__set_left_build_(self, layout):
        _toolBar = qtWidgets_.xToolBar()
        layout.addWidget(_toolBar)
        self.setupLeftToolBar(_toolBar)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        #
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        #
        self.namespaceTreeViewBox = guiQtWidgets.QtTreeview()
        layout.addWidget(self.namespaceTreeViewBox)
        self.setupLeftViewBox(self.namespaceTreeViewBox)
        #
        _toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(_toolBox)
        _toolBox.setTitle('Modify')
        self.setupLeftBottomToolUiBox(_toolBox)
    #
    def setupLeftToolBar(self, toolBar):
        self._namespaceFilterLabel = guiQtWidgets.QtFilterLine()
        toolBar.addWidget(self._namespaceFilterLabel)
        #
        refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        toolBar.addWidget(refreshButton)
        refreshButton.clicked.connect(self.setListNamespace)
    #
    def setupLeftViewBox(self, treeBox):
        self.namespaceSearchDic = {}
        self.nodeInNamespaceDic = {}
        #
        self._namespaceCount = 0
        self.emptyNamespaceLis = []
        self.errorNamespaceLis = []
        #
        self._errorReferenceNodeLis = []
        self.referenceNamespaceLis = []
        self.fileNamespaceArray = []
        #
        self.referenceNamespaceDic = {}
        self.errorReferenceNodeDic = {}
        #
        treeBox.setExpandEnable(True)
        #
        treeBox.setKeywordFilterWidgetConnect(self._namespaceFilterLabel)
        #
        treeBox.currentChanged.connect(self.setViewNamespacePath)
        treeBox.currentChanged.connect(self.setListNode)
    #
    def setupLeftBottomToolUiBox(self, toolBox):
        inData = self.dicNs
        #
        self.namespacePathLabel = guiQtWidgets.QtValueLine()
        toolBox.setInfo(inData, 'namespacePath', self.namespacePathLabel)

        #
        self._referenceNodeRepairButton = guiQtWidgets.QtPressbutton()
        self._referenceNodeRepairButton.setPercentEnable(True)
        toolBox.setButton(inData, 'repairReferenceNodeError', self._referenceNodeRepairButton)
        self._referenceNodeRepairButton.setTooltip('''Repair Reference Nde_Node Error''')
        self._referenceNodeRepairButton.clicked.connect(self.setReferenceNodeRepairCmd)
        #
        self._namespaceRepairButton = guiQtWidgets.QtPressbutton()
        self._namespaceRepairButton.setPercentEnable(True)
        toolBox.setButton(inData, 'repairNamespaceError', self._namespaceRepairButton)
        self._namespaceRepairButton.setTooltip('''Repair Namespace Error''')
        self._namespaceRepairButton.clicked.connect(self.setReduceNamespaceHierarchy)
        #
        toolBox.setSeparators(inData)
    #
    def setupRightWidget(self, layout):
        _toolBar = qtWidgets_.xToolBar()
        layout.addWidget(_toolBar)
        self.setupRightTopToolBar(_toolBar)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        #
        self.nodeTreeViewBox = guiQtWidgets.QtTreeview()
        layout.addWidget(self.nodeTreeViewBox)
        self.setupRightViewBox(self.nodeTreeViewBox)
        #
        _toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(_toolBox)
        _toolBox.setTitle('Modify')
        #
        self.setNodeBottomToolBox(_toolBox)
    #
    def setupRightTopToolBar(self, toolBar):
        self._nodeFilterLabel = guiQtWidgets.QtFilterLine()
        toolBar.addWidget(self._nodeFilterLabel)
        #
        refreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        toolBar.addWidget(refreshButton)
        refreshButton.clicked.connect(self.setListNode)
    #
    def setupRightViewBox(self, treeBox):
        treeBox.setExpandEnable(True)
        treeBox.setSelectEnable(True)
        #
        treeBox.setKeywordFilterWidgetConnect(self._nodeFilterLabel)
        #
        treeBox.selectedChanged.connect(self.setViewNodePath)
        treeBox.selectedChanged.connect(self.setSelNodes)
    #
    def setNodeBottomToolBox(self, toolBox):
        inData = self.dicNd
        #
        self.nodePathLabel = guiQtWidgets.QtValueLine()
        toolBox.setInfo(inData, 'nodePath', self.nodePathLabel)
    #
    def setViewNamespacePath(self):
        infoLabel = self.namespacePathLabel
        #
        treeBox = self.namespaceTreeViewBox
        currentItem = treeBox.currentItem()
        if currentItem:
            namespacePath = currentItem.path
            infoLabel.setDatum(namespacePath)
        else:
            infoLabel.setDatum(none)
    #
    def setReferenceNodeErrorCheckCmd(self):
        errorCount = len(self._errorReferenceNodeLis)
        #
        maxCount = len(self.referenceNamespaceDic)
        correctCount = maxCount - errorCount
        self._referenceNodeRepairButton.setPercent(maxCount, correctCount)
    #
    def setNamespaceErrorCheckCmd(self):
        referenceCount = len(self.referenceNamespaceDic)
        errorCount = len(self.errorNamespaceLis)
        #
        maxCount = self._namespaceCount - referenceCount
        correctCount = maxCount - errorCount
        self._namespaceRepairButton.setPercent(maxCount, correctCount)
    #
    def setViewNodePath(self):
        infoLabel = self.nodePathLabel
        #
        treeBox = self.nodeTreeViewBox
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0]
            namespacePath = selectedItem.path
            infoLabel.setDatum(namespacePath)
        else:
            infoLabel.setDatum(none)
    #
    def setListNamespace(self):
        # Branch View Method
        def setBranchView(treeItem):
            self.connectObject().updateProgress()
            #
            iconKeyword0 = 'maya/default'
            #
            namespacePath = treeItem.path
            namespace = treeItem.name
            nodeLis = maUtils.getDependNodesByNamespace(namespacePath)
            count = 0
            if not nodeLis:
                treeItem._setQtPressStatus(qtCore.OffStatus)
                self.emptyNamespaceLis.append(namespacePath)
            if nodeLis:
                count = len(nodeLis)
                parentItem = treeItem.parentItem()
                isReferenceNode = setReferenceNodeCheck(nodeLis)
                isAssemblyNode = setAssemblyNodeCheck(nodeLis)
                if parentItem:
                    parentItem.setExpanded(True)
                    if not isAssemblyNode:
                        treeItem._setQtPressStatus(qtCore.WarningStatus)
                        self.errorNamespaceLis.append(namespacePath)
                # Reference
                elif isReferenceNode:
                    self.referenceNamespaceLis.append(namespacePath)
                    if not namespacePath in self.referenceNamespaceDic:
                        treeItem._setQtPressStatus(qtCore.ErrorStatus)
                        self.fileNamespaceArray.append(namespacePath)
                #
                if isReferenceNode:
                    iconKeyword0 = 'maya/reference'
                elif isAssemblyNode:
                    iconKeyword0 = 'maya/assemblyReference'
                else:
                    iconKeyword0 = 'maya/default'
                #
                self.nodeInNamespaceDic[treeItem] = nodeLis
            #
            treeItem.setNameString('{} ( {} )'.format(namespace, count))
            treeItem.setIcon(iconKeyword0)
        #
        def setReferenceNodeCheck(nodeLis):
            for node in nodeLis:
                if maUtils.isReferenceNode(node):
                    return True
        #
        def setAssemblyNodeCheck(nodeLis):
            for node in nodeLis:
                if maUtils._getNodeCategoryString(node) == 'assemblyReference':
                    return True
                else:
                    parentNode = maUtils.getObjectParent(node, 1)
                    if maUtils._getNodeCategoryString(parentNode) == 'assemblyReference':
                        return True
        #
        def updateError():
            dataDic = maUtils.getReferenceNamespaceDic()
            for namespacePath, referenceNode in dataDic.items():
                self.referenceNamespaceDic[':' + namespacePath] = referenceNode
                if ':' in referenceNode:
                    parentNamespace = ':'.join(referenceNode.split(':')[:-1])
                    # Delete & Rename
                    self.errorReferenceNodeDic.setdefault(parentNamespace, []).append(referenceNode)
                if ':' in namespacePath:
                    self._errorReferenceNodeLis.append(namespacePath)
        #
        self.namespaceSearchDic = {}
        self.nodeInNamespaceDic = {}
        #
        self._namespaceCount = 0
        self.emptyNamespaceLis = []
        self.errorNamespaceLis = []
        self._errorReferenceNodeLis = []
        self.referenceNamespaceLis = []
        self.fileNamespaceArray = []
        #
        self.referenceNamespaceDic = {}
        self.errorReferenceNodeDic = {}
        #
        treeBox = self.namespaceTreeViewBox
        #
        updateError()
        #
        namespacePathLis = maUtils.getNamespaces()
        #
        maxValue = len(namespacePathLis)
        self._namespaceCount = maxValue
        #
        treeBox.cleanItems()
        if namespacePathLis:
            self.connectObject().setMaxProgressValue(maxValue)
            self.setTreeViewListNamespace(
                treeBox, namespacePathLis, setBranchView
            )
        #
        treeBox.setRefresh()
        #
        self.setReferenceNodeErrorCheckCmd()
        self.setNamespaceErrorCheckCmd()
    #
    def setListNode(self):
        # Branch View Method
        def setBranchView(treeItem):
            self.connectObject().updateProgress()
            #
            objectPath = treeItem.path
            objectName = maUtils._nodeString2nodename_(objectPath, useMode=1)
            nodeType = maUtils._getNodeCategoryString(objectPath)
            treeItem.setNameString(objectName)
            treeItem.setIcon('maya/{}'.format(nodeType))
        #
        treeBox = self.namespaceTreeViewBox
        currentItem = treeBox.currentItem()
        #
        subTreeBox = self.nodeTreeViewBox
        dataDic = self.nodeInNamespaceDic
        #
        subTreeBox.cleanItems()
        if currentItem:
            if currentItem in dataDic:
                nodeLis = dataDic[currentItem]
                objectPathLis = []
                subNodeArray = []
                for node in nodeLis:

                    if node.startswith(appCfg.DEF_mya_node_namespace_pathsep):
                        objectPathLis.append(node)
                    else:
                        subNodeArray.append(node)
                #
                if objectPathLis:
                    maxValue = len(objectPathLis)
                    self.connectObject().setMaxProgressValue(maxValue)
                    self.setTreeViewListNode(
                        subTreeBox, objectPathLis, setBranchView
                    )
                #
                if subNodeArray:
                    for node in subNodeArray:
                        nodeItem = guiQtWidgets.QtTreeItem()
                        subTreeBox.addItem(nodeItem)
                        nodeItem.path = node
                        nodeItem.name = node
                        setBranchView(nodeItem)
        #
        subTreeBox.setRefresh()
    #
    def setReduceNamespaceHierarchy(self):
        errorNamespaces = self.errorNamespaceLis
        referenceNamespaces = self.referenceNamespaceLis
        #
        if errorNamespaces:
            errorNamespaces.reverse()
            maxValue = len(errorNamespaces)
            if self._connectObject:
                self._connectObject.setMaxProgressValue(maxValue)
            for seq, namespacePath in enumerate(errorNamespaces):
                if self._connectObject:
                    self._connectObject.updateProgress()
                tempNamespace = '_'.join(namespacePath[1:].split(':')) + '_reduce_' + str(seq)
                # Local Namespace
                if not namespacePath in referenceNamespaces:
                    maUtils.setNamespaceRename(namespacePath, tempNamespace)
            #
            self.setListNamespace()
    #
    def setReferenceNodeRepairCmd(self):
        inData = maUtils.getReferenceNamespaceDic()
        maxValue = len(inData)
        if self._connectObject:
            self._connectObject.setMaxProgressValue(maxValue)
        #
        animOp.setRepairReferenceNamespace(inData, self._connectObject)
        #
        self.setListNamespace()
    #
    def setSelNodes(self):
        nodePaths = self.getSelNodes()
        if nodePaths:
            maUtils.setNodeSelect(nodePaths)
    #
    def getSelNodes(self):
        nodePaths = []
        treeBox = self.nodeTreeViewBox
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            nodePaths = [i.path for i in selectedItems]
        return nodePaths
    #
    def _kit__unit__set_build_(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        self.mainLayout().setContentsMargins(2, 2, 2, 2)
        #
        layout = qtCore.QHBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        layout.addWidget(leftExpandWidget)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self._kit__unit__set_left_build_(leftScrollArea)
        #
        self.rightViewBox = qtCore.QWidget_()
        layout.addWidget(self.rightViewBox)
        self.leftViewBoxLayout = qtCore.QVBoxLayout_(self.rightViewBox)
        #
        self.setupRightWidget(self.leftViewBoxLayout)


#
class IfUtilsDirectoryManagerUnit(kitQtWgtAbs.IfToolUnitBasic):
    projectName = prsMethods.Project.mayaActiveName()
    #
    VAR_kit__qt_wgt__unit__uiname = 'Directory Manager'
    panelWidth = 800
    panelHeight = 800
    #
    UnitScriptJobWindowName = 'utilsDirectoryManagerWindow'
    #
    widthSet = 800
    w = 80
    dicFilter = {
        'enableAll': [0, 0, 0, 1, 1, none], 'enableClear': [0, 0, 2, 1, 1, none],
        # 1
        'withTexture': [0, 2, 0, 1, 2, u'Texture(s)'],
        'withReference': [0, 3, 0, 1, 2, u'Reference(s)'], 'withAssembly': [0, 3, 2, 1, 2, u'Assembly(s)'],
        'withProxyCache': [0, 4, 0, 1, 2, u'Proxy Cache(s)'], 'withVolumeCache': [0, 4, 2, 1, 2, u'Volume Cache(s)'],
        'withGpu': [0, 5, 0, 1, 2, u'GPU Cache(s)'], 'withAbc': [0, 5, 2, 1, 2, u'Alembic Cache(s)'],
        'withGeometryCache': [0, 6, 0, 1, 2, u'Nde_Geometry Cache(s)'],
        'withAstCfxFurCache': [0, 7, 0, 1, 2, u'Fur Cache(s)'], 'withMap': [0, 7, 2, 1, 2, u'Fur Map(s)'],
        'placeholder': [0, 8, 0, 1, 4, u'Placeholder']
    }
    #
    dic_config = bscMtdCore.orderedDict()
    dic_config['collection'] = [0, 0, 0, 1, 1, u'Collection']
    dic_config['ignoreExists'] = [0, 1, 0, 1, 1, u'Ignore Exists']
    dic_config['ignoreMtimeChanged'] = [0, 1, 1, 1, 1, u'Ignore Time Changed']
    dic_config['withTx'] = [0, 1, 2, 1, 1, u'With Tx ( Arnold Texture )']
    dic_config['autoCache'] = [0, 1, 3, 1, 1, u'Auto Cache ( yeti )']
    # 2
    dic_config['isRepath'] = [0, 3, 0, 1, 1, u'Repath']
    dic_config['isExistsOnly'] = [0, 4, 0, 1, 1, u'Exists Only']
    dic_config['placeholder'] = [0, 5, 0, 1, 4, u'Placeholder']
    #
    dicTool = bscMtdCore.orderedDict()
    dicTool['ignoreStructure'] = [w, 0, 0, 1, 4, 'Ignore Structure']
    # 1
    dicTool['sourceDirectory'] = [w, 2, 0, 1, 4, 'Source']
    dicTool['targetDirectory'] = [w, 3, 0, 1, 4, 'Target']
    # 4
    dicTool['directoryModify'] = [w, 5, 0, 1, 4, 'Collection and Repath', 'svg_basic/info']
    def __init__(self, *args, **kwargs):
        super(IfUtilsDirectoryManagerUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._kit__unit__set_build_()
        #
        self.setRightTreeViewBox()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        pass
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        method = []
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, method)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def _kit__unit__set_left_build_(self, layout):
        toolBar = qtWidgets_.xToolBar()
        layout.addWidget(toolBar)
        self.setLeftTopToolBar(toolBar)
        #
        self.leftTreeViewBox = qtWidgets_.QTreeWidget_()
        layout.addWidget(self.leftTreeViewBox)
        self.leftTreeViewBox.setSingleSelection()
        self.setLeftTreeViewBox()
    #
    def setLeftTopToolBar(self, layout):
        self._leftFilterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        layout.addWidget(self._leftFilterButton)
        #
        self._leftFilterLabel = guiQtWidgets.QtFilterLine()
        layout.addWidget(self._leftFilterLabel)
        #
        self._leftRefreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        layout.addWidget(self._leftRefreshButton)
        self._leftRefreshButton.clicked.connect(self.setListDir)
    #
    def setLeftTreeViewBox(self):
        self.directoryArray = []
        #
        self.fileLinkDic = {}
        #
        self.sourceArray = []
        self.existsSourceArray = []
        self.existsTargetArray = []
        #
        self.collectionDataLis = []
        #
        treeBox = self.leftTreeViewBox
        #
        maxWidth = self.widthSet / 2 - 20
        treeBox.setColumns(
            ['Folder', 'Enable'],
            [6, 2],
            maxWidth
        )
        #
        treeBox.setKeywordFilterWidgetConnect(self._leftFilterLabel)
        treeBox.itemSelectionChanged.connect(self.setDirectoryLabelShow)
        treeBox.itemSelectionChanged.connect(self.setListFile)
    #
    def setupRightWidget(self, layout):
        toolBar = qtWidgets_.xToolBar()
        layout.addWidget(toolBar)
        self.setupRightTopToolBar(toolBar)
        #
        self.rightTreeViewBox = qtWidgets_.QTreeWidget_()
        layout.addWidget(self.rightTreeViewBox)
        self.rightTreeViewBox.setSingleSelection()
    #
    def setupRightTopToolBar(self, layout):
        self._rightFilterButton = guiQtWidgets.QtActionIconbutton('svg_basic/filter')
        layout.addWidget(self._rightFilterButton)
        #
        self.rightSearchBar = guiQtWidgets.QtFilterLine()
        layout.addWidget(self.rightSearchBar)
        #
        self.rightRefreshButton = guiQtWidgets.QtIconbutton('svg_basic/refresh')
        layout.addWidget(self.rightRefreshButton)
        self.rightRefreshButton.clicked.connect(self.setListFile)
    #
    def setRightTreeViewBox(self):
        treeBox = self.rightTreeViewBox
        #
        maxWidth = self.widthSet / 2 - 20
        #
        treeBox.setColumns(
            ['File Name', 'File Type'],
            [6, 2],
            maxWidth
        )
        #
        treeBox.setKeywordFilterWidgetConnect(self.rightSearchBar)
        treeBox.itemSelectionChanged.connect(self.setNodeSelCmd)
    #
    def setupBottomWidget(self, toolBoxLayout):
        toolBox = guiQtWidgets.QtToolbox()
        toolBoxLayout.addWidget(toolBox)
        toolBox.setTitle('Filter(s)', useMode=1)
        toolBox.setExpanded(False)
        self.setupFilterToolUiBox(toolBox)
        #
        toolBox = guiQtWidgets.QtToolbox()
        toolBoxLayout.addWidget(toolBox)
        toolBox.setTitle('Config(s)', useMode=1)
        self.setupConfigToolUiBox(toolBox)
        toolBox.setExpanded(False)
        #
        toolBox = guiQtWidgets.QtToolbox()
        toolBoxLayout.addWidget(toolBox)
        toolBox.setTitle('Action(s)', useMode=1)
        self.setupModifyToolUiBox(toolBox)
    #
    def setupConfigToolUiBox(self, toolBox):
        def setupCollectionBranch():
            def subRefreshCmd():
                mainCheckButton = self._isCollectionButton
                checkButtonLis = [self.ignoreExistsButton, self.ignoreTimeChangedButton, self.withTxButton, self.autoFurCacheButton]
                for i in checkButtonLis:
                    i.setCheckable(mainCheckButton.isChecked())
            #
            self._isCollectionButton = guiQtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'collection', self._isCollectionButton)
            self._isCollectionButton.setChecked(True)
            self._isCollectionButton.clicked.connect(subRefreshCmd)
            #
            self.ignoreExistsButton = guiQtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'ignoreExists', self.ignoreExistsButton)
            self.ignoreExistsButton.setChecked(True)
            #
            self.ignoreTimeChangedButton = guiQtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'ignoreMtimeChanged', self.ignoreTimeChangedButton)
            self.ignoreExistsButton.toggled.connect(self.ignoreTimeChangedButton.setCheckable)
            #
            self.withTxButton = guiQtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'withTx', self.withTxButton)
            self.withTxButton.setChecked(True)
            #
            self.autoFurCacheButton = guiQtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'autoCache', self.autoFurCacheButton)
            #
            subRefreshCmd()
        #
        def setupRepathBranch():
            def subRefreshCmd():
                mainCheckButton = self._isRepathButton
                checkButtonLis = [self.isExistsOnlyButton]
                for i in checkButtonLis:
                    i.setCheckable(mainCheckButton.isChecked())
            #
            self._isRepathButton = guiQtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'isRepath', self._isRepathButton)
            self._isRepathButton.setChecked(True)
            self._isRepathButton.clicked.connect(subRefreshCmd)
            #
            self.isExistsOnlyButton = guiQtWidgets.QtCheckbutton()
            toolBox.setButton(inData, 'isExistsOnly', self.isExistsOnlyButton)
            self.isExistsOnlyButton.setChecked(True)
            #
            subRefreshCmd()
        #
        inData = self.dic_config
        #
        setupCollectionBranch()
        # Repath
        setupRepathBranch()
        #
        toolBox.setSeparators(inData)
    #
    def setupFilterToolUiBox(self, toolBox):
        self.filterItemArray = []
        #
        inData = self.dicFilter
        #
        self._enableAllButton = guiQtWidgets.QtIconbutton('svg_basic/checkedall')
        toolBox.setButton(inData, 'enableAll', self._enableAllButton)
        self._enableAllButton.clicked.connect(self.setFilterEnableAll)
        #
        self._enableClearButton = guiQtWidgets.QtIconbutton('svg_basic/uncheckedall')
        toolBox.setButton(inData, 'enableClear', self._enableClearButton)
        self._enableClearButton.clicked.connect(self.setFilterEnableClear)
        #
        self.withTextureButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withTexture', self.withTextureButton)
        self.withTextureButton.setChecked(True)
        self.filterItemArray.append(self.withTextureButton)
        #
        self.withReferenceButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withReference', self.withReferenceButton)
        self.withReferenceButton.setChecked(True)
        self.filterItemArray.append(self.withReferenceButton)
        #
        self.withAssemblyButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withAssembly', self.withAssemblyButton)
        self.withAssemblyButton.setChecked(True)
        self.filterItemArray.append(self.withAssemblyButton)
        #
        self._withProxyCacheButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withProxyCache', self._withProxyCacheButton)
        self._withProxyCacheButton.setChecked(True)
        self.filterItemArray.append(self._withProxyCacheButton)
        #
        self._withVolumeCacheButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withVolumeCache', self._withVolumeCacheButton)
        self._withVolumeCacheButton.setChecked(True)
        self.filterItemArray.append(self._withVolumeCacheButton)
        #
        self.withGpuButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withGpu', self.withGpuButton)
        self.withGpuButton.setChecked(True)
        self.filterItemArray.append(self.withGpuButton)
        #
        self.withAbcButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withAbc', self.withAbcButton)
        self.withAbcButton.setChecked(True)
        self.filterItemArray.append(self.withAbcButton)
        #
        self.withGeometryCacheButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withGeometryCache', self.withGeometryCacheButton)
        self.withGeometryCacheButton.setChecked(True)
        self.filterItemArray.append(self.withGeometryCacheButton)
        #
        self.withFurCacheButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withAstCfxFurCache', self.withFurCacheButton)
        self.withFurCacheButton.setChecked(True)
        self.filterItemArray.append(self.withFurCacheButton)
        #
        self.withMapButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withMap', self.withMapButton)
        self.withMapButton.setChecked(True)
        self.filterItemArray.append(self.withMapButton)
        #
        toolBox.setSeparators(inData)
    #
    def setupModifyToolUiBox(self, toolBox):
        inData = self.dicTool
        #
        self.ignoreStructureButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'ignoreStructure', self.ignoreStructureButton)
        #
        self._sourceDirectoryLabel = guiQtWidgets.QtValueLine()
        toolBox.setInfo(inData, 'sourceDirectory', self._sourceDirectoryLabel)
        #
        self._targetDirectoryLabel = guiQtWidgets.QtValueLine()
        self._targetDirectoryLabel.setEnterEnable(True)
        toolBox.setInfo(inData, 'targetDirectory', self._targetDirectoryLabel)
        self._targetDirectoryLabel.entryChanged.connect(self.setListFile)
        #
        self._directoryModifyButton = guiQtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'directoryModify', self._directoryModifyButton)
        self._directoryModifyButton.setPercentEnable(True)
        self._directoryModifyButton.clicked.connect(self.setDirectoryModify)
        #
        toolBox.setSeparators(inData)
    #
    def setFilterEnableAll(self):
        [i.setChecked(True) for i in self.filterItemArray]
    #
    def setFilterEnableClear(self):
        [i.setChecked(False) for i in self.filterItemArray]
    #
    def setListDir(self):
        treeBox = self.leftTreeViewBox
        #
        self.getDirectoryDic()
        #
        pathsep = appCfg.OsFilePathSep
        #
        treeBox.clear()
        #
        osPathsArray = treeBox.getGraphPaths(self.directoryArray, pathsep)
        #
        maUtilsTreeViewCmds.setListDirectory(
            treeBox, osPathsArray, self.fileLinkDic,
            connectMethod=self.setListFile
        )
    #
    def setListFile(self):
        def getFileDataArray(osFolder):
            lis = []
            if osFolder in self.fileLinkDic:
                lis = self.fileLinkDic[osFolder]
            return lis
        #
        def getTargetFile(sourceFileString):
            if self.ignoreStructureButton.isChecked():
                targetFileString = bscMethods.OsPath.composeBy(targetDirectory, bscMethods.OsFile.basename(sourceFileString))
            else:
                targetFileString = targetDirectory + sourceFileString[len(sourceDirectory):]
            return targetFileString
        #
        self.sourceArray = []
        self.existsSourceArray = []
        self.existsTargetArray = []
        #
        self.collectionDataLis = []
        # Used Data
        fileDataArray = []
        #
        sourceDirectory = self._sourceDirectoryLabel.datum()
        targetDirectory = self._targetDirectoryLabel.datum()
        #
        if targetDirectory:
            targetDirectory = targetDirectory.replace('\\', '/')
        #
        treeBox = self.leftTreeViewBox
        subTreeBox = self.rightTreeViewBox
        #
        selectedItemLis = treeBox.selectedItems()
        # Step 01 ( Get Used Data )
        subTreeBox.clear()
        if selectedItemLis:
            treeItem = selectedItemLis[0]
            childItemLis = [treeItem]
            childItemLis.extend(treeItem.childItems())
            progressExplain = u'''Read File(s)'''
            maxValue = len(childItemLis)
            progressBar = bscObjects.ProgressWindow(progressExplain, maxValue)
            for treeItem in childItemLis:
                progressBar.update()
                checkBox = treeItem.checkBox
                if checkBox.isChecked():
                    directory = treeItem.path[1:]
                    subFileDataArray = getFileDataArray(directory)
                    fileDataArray.extend(subFileDataArray)
        # Step 02
        if fileDataArray:
            for fileType, fileString_, nodes in fileDataArray:
                osFileCollectionDataLis = []
                iconKeyword0 = 'svg_basic/file'
                #
                stateLabel = none
                #
                iconKeyword1 = 'svg_basic/name'
                checkState = none
                checkToolTip = none
                #
                fileName = bscMethods.OsFile.basename(fileString_)
                nodeCount = len(nodes)
                fileItem = qtWidgets_.QTreeWidgetItem_()
                subTreeBox.addItem(fileItem)
                #
                fileItem.path = fileString_
                fileItem.type = fileType
                fileItem.name = fileName
                fileItem.nodes = nodes
                #
                sourceFile = fileString_
                targetFile = getTargetFile(sourceFile)
                #
                osFileCollectionDataLis.append((sourceFile, targetFile))
                #
                existsSourceFiles = bscMethods.OsMultifile.existFiles(sourceFile)
                existsSourceCount = len(existsSourceFiles)
                #
                self.sourceArray.append(sourceFile)
                #
                textureCount = 0
                # Source Exists Check
                if existsSourceCount == 0:
                    stateLabel = 'off'
                    #
                    checkState = 'off'
                    checkToolTip = 'Source is Non - Exists'
                #
                elif existsSourceCount > 0:
                    subTargetExistsFiles = []
                    sourceFile = existsSourceFiles[0]
                    targetFile = getTargetFile(sourceFile)
                    #
                    subSourceFiles = existsSourceFiles
                    textureCount = len(subSourceFiles)
                    # Sub File
                    subCheckToolTip = none
                    for subSourceFile in subSourceFiles:
                        iconKeyword0 = 'svg_basic/files'
                        #
                        subIconKeyword = 'svg_basic/file'
                        #
                        subFileItem = qtWidgets_.QTreeWidgetItem_()
                        fileItem.addChild(subFileItem)
                        #
                        subTargetFile = getTargetFile(subSourceFile)
                        #
                        subTargetExists = bscMethods.OsFile.isExist(subTargetFile)
                        if subTargetExists:
                            isSubChanged = bscMethods.OsFile.isFileTimeChanged(subSourceFile, subTargetFile)
                            if isSubChanged:
                                subCheckStateLabel = 'warning'
                                subCheckToolTip = 'Target is Time Changed'
                            else:
                                subCheckStateLabel = 'on'
                                subTargetExistsFiles.append(subTargetFile)
                        else:
                            subCheckStateLabel = 'error'
                            subCheckToolTip = 'Target is Non - Exists'
                        #
                        subFileName = bscMethods.OsFile.basename(subSourceFile)
                        subFileItem.setItemIcon_(0, subIconKeyword, stateLabel)
                        subFileItem.setText(0, subFileName)
                        #
                        subFileItem.setItemIcon_(1, iconKeyword1, subCheckStateLabel)
                        subFileItem.setText(1, bscMethods.StrCamelcase.toPrettify(fileType))
                        #
                        subFileItem.setToolTip(1, subCheckToolTip)
                        #
                        subFileItem.path = subSourceFile
                        subFileItem.name = subFileName
                        #
                        osFileCollectionDataLis.append((subSourceFile, subTargetFile))
                    #
                    subTargetExistsCheck = len(subTargetExistsFiles) == len(subSourceFiles)
                    if subTargetExistsCheck:
                        checkState = 'on'
                        self.existsTargetArray.append(targetFile)
                    else:
                        checkState = 'error'
                        checkToolTip = 'Sub Target is Non - Exists / Time Changed'
                        #
                        fileItem.setExpanded(True)
                #
                text0 = fileName
                fileItem.setItemIcon_(0, iconKeyword0, stateLabel)
                fileItem.setText(0, text0)
                #
                text1 = '{} ( {} * {} )'.format(bscMethods.StrCamelcase.toPrettify(fileType), nodeCount, textureCount)
                fileItem.setItemIcon_(1, iconKeyword1, checkState)
                fileItem.setText(1, text1)
                #
                fileItem.setToolTip(1, checkToolTip)
                #
                self.collectionDataLis.append((fileType, nodes, osFileCollectionDataLis))
        #
        self.setDirModifyBtnState()
    #
    def setDirectoryLabelShow(self):
        treeBox = self.leftTreeViewBox
        infoLabel = self._sourceDirectoryLabel
        subInfoLabel = self._targetDirectoryLabel
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0]
            directory = selectedItem.path[1:]
            infoLabel.setDatum(directory)
            subInfoLabel.setDatum(directory)
        else:
            infoLabel.setDatum(none)
            subInfoLabel.setDatum(none)
    #
    def setDirModifyBtnState(self):
        maxCount = len(self.sourceArray)
        correctCount = len(self.existsTargetArray)
        self._directoryModifyButton.setPercent(maxCount, correctCount)
    #
    def setDirectoryModify(self):
        collectionDataLis = self.collectionDataLis
        if collectionDataLis:
            isCollection = self._isCollectionButton.isChecked()
            isRepath = self._isRepathButton.isChecked()
            if isCollection or isRepath:
                isIgnoreExists = self.ignoreExistsButton.isChecked()
                isIgnoreTimeChanged = self.ignoreTimeChangedButton.isChecked()
                #
                isWithTx = self.withTxButton.isChecked()
                isAutoCache = self.autoFurCacheButton.isChecked()
                #
                self._connectObject.hide()
                #
                maDir.setDirectoryModifyCmd(
                    collectionDataLis,
                    isCollection=isCollection,
                    isIgnoreExists=isIgnoreExists, isIgnoreTimeChanged=isIgnoreTimeChanged,
                    isWithTx=isWithTx,
                    isAutoCache=isAutoCache,
                    isRepath=isRepath
                )
                #
                self._connectObject.show()
                # Refresh
                self.setListDir()
    #
    def setNodeSelCmd(self):
        treeBox = self.rightTreeViewBox
        selectedItems = treeBox.selectedItems()
        if selectedItems:
            nodeArray = []
            for treeItem in selectedItems:
                if hasattr(treeItem, 'nodes'):
                    nodes = treeItem.nodes
                    for node in nodes:
                        if not ' - ' in node:
                            nodeArray.append(node)
                        if ' - ' in node:
                            nodeArray.append(node.split(' - ')[0])
            #
            maUtils.setNodeSelect(nodeArray)
    #
    def getDirectoryDic(self):
        isWithTexture = self.withTextureButton.isChecked()
        isWithMap = self.withMapButton.isChecked()
        #
        isWithReference = self.withReferenceButton.isChecked()
        isWithAssemblyReference = self.withAssemblyButton.isChecked()
        #
        isWithProxy = self._withProxyCacheButton.isChecked()
        isWithVolumeCache = self._withVolumeCacheButton.isChecked()
        #
        isWithGpuCache = self.withGpuButton.isChecked()
        isWithAlembicCache = self.withAbcButton.isChecked()
        #
        isWithFurCache = self.withFurCacheButton.isChecked()
        isWithGeomCache = self.withGeometryCacheButton.isChecked()
        #
        self.directoryArray, self.fileLinkDic = maDir.getDirData(
            withTexture=isWithTexture,
            withFurMap=isWithMap,
            withReference=isWithReference,
            withAssemblyReference=isWithAssemblyReference,
            withProxyCache=isWithProxy,
            withVolumeCache=isWithVolumeCache,
            withGpuCache=isWithGpuCache,
            withAlembicCache=isWithAlembicCache,
            withFurCache=isWithFurCache,
            withGeomCache=isWithGeomCache
        )
    #
    def _kit__unit__set_build_(self):
        scrollArea = qtCore.QScrollArea_()
        self.mainLayout().addWidget(scrollArea)
        #
        widget = qtCore.QWidget_()
        scrollArea.addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        layout.addWidget(leftExpandWidget)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self._kit__unit__set_left_build_(leftScrollArea)
        #
        rightWidget = qtCore.QWidget_()
        layout.addWidget(rightWidget)
        rightLayout = qtCore.QVBoxLayout_(rightWidget)
        self.setupRightWidget(rightLayout)
        #
        bottomWidget = qtCore.QWidget_()
        scrollArea.addWidget(bottomWidget)
        bottomLayout = qtCore.QVBoxLayout_(bottomWidget)
        self.setupBottomWidget(bottomLayout)


#
class IfTopologyConstantToolUnit(kitQtWgtAbs.IfToolUnitBasic):
    VAR_kit__qt_wgt__unit__uiname = 'Topology Comparison'
    UnitScriptJobWindowName = 'topologyComparisonScriptJobWindow'
    UnitWidth = 800
    UnitHeight = 800
    #
    widthSet = 400
    #
    w = 180
    dicFilter = bscMtdCore.orderedDict()
    dicFilter['enableAll'] = [0, 0, 0, 1, 1, none]
    dicFilter['enableClear'] = [0, 0, 2, 1, 1, none]
    # 1
    dicFilter['withMesh'] = [0, 2, 0, 1, 2, 'Mesh']
    dicFilter['withCurve'] = [0, 2, 2, 1, 2, 'Curve']
    dicFilter['placeholder'] = [0, 3, 0, 1, 4, 'Placeholder']
    #
    dic_config = bscMtdCore.orderedDict()
    dic_config['withShape'] = [0, 0, 0, 1, 2, 'Shape']
    dic_config['floatRound'] = [0, 0, 2, 1, 2, 'Round']
    #
    dicTool = {
        'sourceRoot': [w, 0, 0, 1, 4, 'Source Root ( Name / UUID )'],
        'targetRoot': [w, 1, 0, 1, 4, 'Target Root ( Name / UUID )'],
        #
        'constant': [0, 3, 0, 1, 4, 'Constant'],
        'cloneHierarchy': [0, 4, 0, 1, 4, 'Clone Hierarchy']
    }
    def __init__(self, *args, **kwargs):
        super(IfTopologyConstantToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._kit__unit__set_build_()
        #
        self.UnitScriptJobWindowName = 'fileManagerScriptJobWindow'
        #
        self.sourceRoot = none
        self.targetRoot = none
        #
        self.pathReduceDic = {}
        #
        self._kit__unit__set_left_build_()
        self.setLeftTopToolBar()
        self.setLeftViewBox()
        self.setBottomBox()
        self.setupConfigToolUiBox()
        self.setupConfigBox()
        self.setToolBox()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        self.setScriptJob()
        #
        self.setRoot()
        #
        self.setListObjects()
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        method = []
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, method)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def _kit__unit__set_left_build_(self):
        toolBoxLayout = self.leftBoxLayout
        #
        self.leftTopToolBar = qtWidgets_.xToolBar()
        toolBoxLayout.addWidget(self.leftTopToolBar)
        #
        widget = qtCore.QWidget_()
        toolBoxLayout.addWidget(widget)
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        #
        self.leftTreeViewBox = qtWidgets_.QTreeWidget_()
        layout.addWidget(self.leftTreeViewBox)
    #
    def setLeftTopToolBar(self):
        toolBar = self.leftTopToolBar
        #
        self.leftSelectAllButton = guiQtWidgets.QtIconbutton('svg_basic/checkedall')
        toolBar.addWidget(self.leftSelectAllButton)
        # self.leftSelectAllButton.setNameString('All')
        self.leftSelectAllButton.clicked.connect(self.setLeftSelectAll)
        #
        self.leftSelectClearButton = guiQtWidgets.QtIconbutton('svg_basic/uncheckedall')
        toolBar.addWidget(self.leftSelectClearButton)
        # self.leftSelectClearButton.setNameString('Clear')
        self.leftSelectClearButton.clicked.connect(self.setLeftSelectClear)
        #
        self._filterEnterLabel = guiQtWidgets.QtFilterLine()
        toolBar.addWidget(self._filterEnterLabel)
    #
    def setLeftViewBox(self):
        treeBox = self.leftTreeViewBox
        #
        treeBox.setColumns(['Object', 'Type'], [4, 2], self.UnitWidth - 20)
        treeBox.itemSelectionChanged.connect(self.setObjectSelection)
        #
        treeBox.setKeywordFilterWidgetConnect(self._filterEnterLabel)
    #
    def setBottomBox(self):
        toolBoxLayout = self.bottomBoxLayout
        #
        self.filterBox = guiQtWidgets.QtToolbox()
        toolBoxLayout.addWidget(self.filterBox)
        self.filterBox.setTitle('Filter', 1)
        #
        self.configBox = guiQtWidgets.QtToolbox()
        toolBoxLayout.addWidget(self.configBox)
        self.configBox.setTitle('Config', 1)
        #
        self.toolBox = guiQtWidgets.QtToolbox()
        toolBoxLayout.addWidget(self.toolBox)
        self.toolBox.setTitle('Tool')
    #
    def setupConfigToolUiBox(self):
        self.filterItemArray = []
        #
        inData = self.dicFilter
        toolBox = self.filterBox
        #
        self._enableAllButton = guiQtWidgets.QtIconbutton('svg_basic/checkedall')
        toolBox.setButton(inData, 'enableAll', self._enableAllButton)
        self._enableAllButton.clicked.connect(self.setFilterEnableAll)
        #
        self._enableClearButton = guiQtWidgets.QtIconbutton('svg_basic/uncheckedall')
        toolBox.setButton(inData, 'enableClear', self._enableClearButton)
        self._enableClearButton.clicked.connect(self.setFilterEnableClear)
        #
        self.withMeshButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withMesh', self.withMeshButton)
        self.withMeshButton.setChecked(True)
        self.filterItemArray.append(self.withMeshButton)
        #
        self.withCurveButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withCurve', self.withCurveButton)
        self.withCurveButton.setCheckable(False)
        self.filterItemArray.append(self.withCurveButton)
        #
        toolBox.setSeparators(inData)
    #
    def setupConfigBox(self):
        inData = self.dic_config
        toolBox = self.configBox
        #
        self.withShapeButton = guiQtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withShape', self.withShapeButton)
        self.withShapeButton.setChecked(True)
        #
        self.floatRoundBox = guiQtWidgets.QtValueArrayLine()
        toolBox.setInfo(inData, 'floatRound', self.floatRoundBox)
        self.floatRoundBox.setDefaultValue(8)
    #
    def setToolBox(self):
        inData = self.dicTool
        toolBox = self.toolBox
        #
        self.sourceRootLabel = guiQtWidgets.QtValueLine()
        toolBox.setInfo(inData, 'sourceRoot', self.sourceRootLabel)
        #
        self.targetRootLabel = guiQtWidgets.QtValueLine()
        toolBox.setInfo(inData, 'targetRoot', self.targetRootLabel)
        #
        self.constantButton = guiQtWidgets.QtPressbutton()
        toolBox.setInfo(inData, 'constant', self.constantButton)
        self.constantButton.clicked.connect(self.setListObjects)
        #
        self.cloneHierarchyButton = guiQtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'cloneHierarchy', self.cloneHierarchyButton)
        self.cloneHierarchyButton.clicked.connect(self.setCloneHierarchy)
        #
        toolBox.setSeparators(inData)
    #
    def setListObjects(self):
        # Use Order Dic
        self.pathReduceDic = bscMtdCore.orderedDict()
        #
        treeBox = self.leftTreeViewBox
        #
        sourceObjects = []
        matchObjects = []
        #
        sourceObjectData = self.getSourceObjectData()
        targetObjectKeyData = self.getTargetObjectKeyData()
        #
        treeBox.clear()
        lis = []
        if sourceObjectData:
            for seq, (sourceObjectPath, objectType, sourceObjectKey) in enumerate(sourceObjectData):
                sourceObjects.append(sourceObjectPath)
                objectName = maUtils._nodeString2nodename_(sourceObjectPath)
                #
                sourceObjectItem = qtWidgets_.QTreeWidgetItem_([objectName, objectType])
                sourceObjectItem.path = sourceObjectPath
                #
                treeBox.addItem(sourceObjectItem)
                #
                subLabelString = 'off'
                #
                if sourceObjectKey in targetObjectKeyData:
                    matchObjects.append(sourceObjectPath)
                    objectDataArray = targetObjectKeyData[sourceObjectKey]
                    subLabelString = none
                    if len(objectDataArray) > 1:
                        subLabelString = 'error'
                        lis.extend(objectDataArray[1:])
                    for targetObjectPath, targetObjectType in objectDataArray:
                        targetObjectName = maUtils._nodeString2nodename_(targetObjectPath)
                        targetObjectItem = qtWidgets_.QTreeWidgetItem_([targetObjectName, objectType])
                        targetObjectItem.path = targetObjectPath
                        #
                        sourceObjectItem.addChild(targetObjectItem)
                        #
                        targetObjectItem.setItemMayaIcon(0, objectType, subLabelString)
                        #
                        sourceObjectItem.setExpanded(True)
                        #
                        self.pathReduceDic[targetObjectPath] = sourceObjectPath
                #
                sourceObjectItem.setItemMayaIcon(0, objectType, subLabelString)
        #
        self.constantButton.setPercent(len(sourceObjects), len(matchObjects))
    #
    def setLeftSelectAll(self):
        treeBox = self.leftTreeViewBox
        treeBox.setSelectAll()
    #
    def setLeftSelectClear(self):
        treeBox = self.leftTreeViewBox
        treeBox.clearSelection()
    #
    def setFilterEnableAll(self):
        [i.setChecked(True) for i in self.filterItemArray]
    #
    def setFilterEnableClear(self):
        [i.setChecked(False) for i in self.filterItemArray]
    #
    def getRoot(self, rootLabel):
        message = rootLabel.datum()
        #
        root = none
        #
        if message:
            isUuid = maUuid.isUsable(message)
            if isUuid:
                root = maUuid.getObject(message, 1)
            if not isUuid:
                if maUtils._isAppExist(message):
                    root = maUtils._dcc_getNodFullpathNodepathStr(message)
        #
        return root
    #
    def setRoot(self):
        sourceRootLabel = self.sourceRootLabel
        targetRootLabel = self.targetRootLabel
        #
        selectedObjects = maUtils.getSelectedObjects(1)
        sourceRootPath = none
        targetRootPath = none
        #
        if len(selectedObjects) == 1:
            sourceRootPath = selectedObjects[0]
            sourceRootName = maUtils._nodeString2nodename_(sourceRootPath)
            sourceRootLabel.setDatum(sourceRootPath)
        #
        elif len(selectedObjects) == 2:
            sourceRootPath, targetRootPath = selectedObjects
            sourceRootName = maUtils._nodeString2nodename_(sourceRootPath)
            sourceRootLabel.setDatum(sourceRootPath)
            targetRootName = maUtils._nodeString2nodename_(targetRootPath)
            targetRootLabel.setDatum(targetRootPath)
        #
        else:
            sourceRootPath = none
            targetRootPath = none
            sourceRootLabel.setEnterClear()
            targetRootLabel.setEnterClear()
        #
        self.sourceRoot = sourceRootPath
        self.targetRoot = targetRootPath
    #
    def setObjectSelection(self):
        treeBox = self.leftTreeViewBox
        selectedItems = treeBox.selectedItems()
        objectPaths = []
        if selectedItems:
            for treeItem in selectedItems:
                objectPath = treeItem.path
                objectPaths.append(objectPath)
        #
        if objectPaths:
            maUtils.setNodeSelect(objectPaths)
    #
    def setCloneHierarchy(self):
        sourceRoot = self.sourceRoot
        pathReduceData = self.pathReduceDic
        #
        if sourceRoot and pathReduceData:
            cloneRoot = '|clone_grp'
            maUtils.setCloneHierarchy(sourceRoot, cloneRoot)
            for sourcePath, targetPath in pathReduceData.items():
                sourceName = maUtils._nodeString2nodename_(sourcePath)
                cloneTargetPath = cloneRoot + targetPath
                cloneTargetParentPath = maUtils._toNodeParentPath(cloneTargetPath)
                cloneTargetName = maUtils._nodeString2nodename_(cloneTargetPath)
                if maUtils._isAppExist(sourcePath):
                    if not maUtils._isAppExist(cloneTargetPath):
                        maUtils.setObjectParent(sourcePath, cloneTargetParentPath)
                        cloneSourcePath = cloneTargetParentPath + '|' + sourceName
                        maUtils.setNodeRename(cloneSourcePath, cloneTargetName)
    #
    def getSourceRoot(self):
        return self.getRoot(self.sourceRootLabel)
    #
    def getTargetRoot(self):
        return self.getRoot(self.targetRootLabel)
    #
    def getSourceObjectData(self):
        sourceRoot = self.getSourceRoot()
        return self.getObjectData(sourceRoot)
    #
    def getTargetObjectData(self):
        targetRoot = self.getTargetRoot()
        return self.getObjectData(targetRoot)
    #
    def getObjectData(self, root):
        def getSub(inData, objectType):
            for objectPath in inData:
                objectTopoKey, objectShapeKey = maGeom.getMeshObjectGeomInfo(objectPath, maxRound)
                if withShape:
                    objectTopoKey = objectTopoKey + objectShapeKey
                objectDatas.append((objectPath, objectType, objectTopoKey))
        #
        objectDatas = []
        withShape = self.withShapeButton.isChecked()
        maxRound = self.floatRoundBox.value()
        #
        if root:
            isWithMesh = self.withMeshButton.isChecked()
            isWithCurve = self.withCurveButton.isChecked()
            #
            if isWithMesh:
                meshObjects = maUtils.getChildObjectsByRoot(root, 'mesh')
                getSub(meshObjects, 'mesh')
        #
        return objectDatas
    #
    def getSourceObjectKeyData(self):
        sourceRoot = self.getSourceRoot()
        return self.getObjectKeyData(sourceRoot)
    #
    def getTargetObjectKeyData(self):
        targetRoot = self.getTargetRoot()
        return self.getObjectKeyData(targetRoot)
    #
    def getObjectKeyData(self, root):
        def getSub(inData, objectType):
            for objectPath in inData:
                objectTopoKey, objectShapeKey = maGeom.getMeshObjectGeomInfo(objectPath, maxRound)
                if withShape:
                    objectTopoKey = objectTopoKey + objectShapeKey
                objectKeyDic.setdefault(objectTopoKey, []).append((objectPath, objectType))
        #
        objectKeyDic = {}
        withShape = self.withShapeButton.isChecked()
        maxRound = self.floatRoundBox.value()
        #
        if root:
            isWithMesh = self.withMeshButton.isChecked()
            isWithCurve = self.withCurveButton.isChecked()
            #
            if isWithMesh:
                meshObjects = maUtils.getChildObjectsByRoot(root, 'mesh')
                getSub(meshObjects, 'mesh')
        #
        return objectKeyDic
    #
    def _kit__unit__set_build_(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QVBoxLayout_(widget)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        self.leftBoxLayout = qtCore.QVBoxLayout_(widget)
        #
        widget = qtCore.QWidget_()
        layout.addWidget(widget)
        self.bottomBoxLayout = qtCore.QVBoxLayout_(widget)


#
class IfSceneCleanToolUnit(kitQtWgtAbs.IfToolUnitBasic):
    VAR_kit__qt_wgt__unit__uiname = 'Scene Clean'
    panelWidth = 800
    panelHeight = 800
    widthSet = 800
    UnitScriptJobWindowName = 'utilsSceneCleanWindow'
    w = 180
    toolDic_Clean = {
        'enableAll': [0, 0, 0, 1, 3, 'Enable All'], 'enableClear': [0, 0, 3, 1, 3, 'Enable None'],
        1: 'Unknown(s)',
        'withUnknownPlug': [0, 2, 0, 1, 2, 'Unknown Plug(s)'],
        'listUnknownPlug': [0, 2, 4, 1, 1, 'List', 'svg_basic/list'], 'cleanUnknownPlug': [0, 2, 5, 1, 1, 'Clean', 'svg_basic/cleanup'],
        'withUnknownNode': [0, 3, 0, 1, 2, 'Unknown Nde_Node(s)'],
        'listUnknownNode': [0, 3, 4, 1, 1, 'List', 'svg_basic/list'], 'cleanUnknownNode': [0, 3, 5, 1, 1, 'Clean', 'svg_basic/cleanup'],
        4: 'Layer(s)',
        'withDisplayLayer': [0, 5, 0, 1, 2, 'Display Layer(s)'], 'withDisplayLayerConfig': [0, 5, 2, 1, 2, ''],
        'listDisplayLayer': [0, 5, 4, 1, 1, 'List', 'svg_basic/list'], 'cleanDisplayLayer': [0, 5, 5, 1, 1, 'Clean', 'svg_basic/cleanup'],
        'withRenderLayer': [0, 6, 0, 1, 2, 'Render Layer(s)'], 'withRenderLayerConfig': [0, 6, 2, 1, 2, ''],
        'listRenderLayer': [0, 6, 4, 1, 1, 'List', 'svg_basic/list'], 'cleanRenderLayer': [0, 6, 5, 1, 1, 'Clean', 'svg_basic/cleanup'],
    }
    a = {
        'withReferenceFile': [0, 2, 0, 1, 2, 'Reference - File'],
        'withReferenceNode': [0, 2, 2, 1, 2, 'Reference - Nde_Node'],
        'withUnusedNamespace': [0, 7, 0, 1, 2, 'Namespace ( Unused )'],
        'withUnusedShader': [0, 7, 2, 1, 2, 'Nde_ShaderRef ( Unused )'],
        'withUnusedSet': [0, 8, 0, 1, 2, 'Set ( Unused )'], 'withUnusedDeform': [0, 8, 2, 1, 2, 'Deform ( Unused )'],
    }
    def __init__(self, *args, **kwargs):
        super(IfSceneCleanToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._kit__unit__set_build_()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        method = []
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, method)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def _kit__unit__set_left_build_(self, layout):
        toolBox = guiQtWidgets.QtToolbox()
        layout.addWidget(toolBox)
        toolBox.setTitle('Clean')
        self.setupCleanToolUiBox(toolBox)
    #
    def setupRightWidget(self, layout):
        self._treeWidget = qtWidgets_.QTreeWidget_()
        layout.addWidget(self._treeWidget)
        self._treeWidget.setColumns(
            ['Name', 'Type'], [4, 4],
            self.panelWidth
        )
    #
    def setupCleanToolUiBox(self, toolBox):
        def setDisplayLayerSub():
            widget = qtCore.QWidget_()
            layout = qtCore.QHBoxLayout_(widget)
            toolBox.addButton('withDisplayLayerConfig', widget)
            #
            self._withUnuseDisplayLayerButton = guiQtWidgets.QtRadioCheckbutton()
            layout.addWidget(self._withUnuseDisplayLayerButton)
            self._withUnuseDisplayLayerButton.setNameString('Empty')
            self._withUnuseDisplayLayerButton.setChecked(True)
            self._withDisplayLayerButton.toggled.connect(self._withUnuseDisplayLayerButton.setCheckable)
            #
            self._withAllDisplayLayerButton = guiQtWidgets.QtRadioCheckbutton()
            layout.addWidget(self._withAllDisplayLayerButton)
            self._withAllDisplayLayerButton.setNameString('All')
            self._withDisplayLayerButton.toggled.connect(self._withAllDisplayLayerButton.setCheckable)
        #
        def setRenderLayerSub():
            widget = qtCore.QWidget_()
            layout = qtCore.QHBoxLayout_(widget)
            toolBox.addButton('withRenderLayerConfig', widget)
            #
            self._withUnuseRenderLayerButton = guiQtWidgets.QtRadioCheckbutton()
            layout.addWidget(self._withUnuseRenderLayerButton)
            self._withUnuseRenderLayerButton.setNameString('Empty')
            self._withUnuseRenderLayerButton.setChecked(True)
            self._withRenderLayerButton.toggled.connect(self._withUnuseRenderLayerButton.setCheckable)
            #
            self._withAllRenderLayerButton = guiQtWidgets.QtRadioCheckbutton()
            layout.addWidget(self._withAllRenderLayerButton)
            self._withAllRenderLayerButton.setNameString('All')
            self._withRenderLayerButton.toggled.connect(self._withAllRenderLayerButton.setCheckable)
        #
        self._configItemLis = []
        toolBox.setUiData(self.toolDic_Clean)
        #
        self._enableAllButton = guiQtWidgets.QtIconbutton('svg_basic/checkedall')
        toolBox.addButton('enableAll', self._enableAllButton)
        self._enableAllButton.clicked.connect(self.setFilterEnableAll)
        #
        self._enableClearButton = guiQtWidgets.QtIconbutton('svg_basic/uncheckedall')
        toolBox.addButton('enableClear', self._enableClearButton)
        self._enableClearButton.clicked.connect(self.setFilterEnableClear)
        # Unknown Plug(s)
        self._withUnknownPlugButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('withUnknownPlug', self._withUnknownPlugButton)
        self._withUnknownPlugButton.setChecked(True)
        self._configItemLis.append(self._withUnknownPlugButton)
        #
        self._listUnknownPlugButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('listUnknownPlug', self._listUnknownPlugButton)
        self._listUnknownPlugButton.clicked.connect(self._listUnknownPlugCmd)
        #
        self._cleanUnknownPlugButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('cleanUnknownPlug', self._cleanUnknownPlugButton)
        self._cleanUnknownPlugButton.clicked.connect(self._cleanUnknownPlugCmd)
        # Unknown Nde_Node(s)
        self._withUnknownNodeButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('withUnknownNode', self._withUnknownNodeButton)
        self._withUnknownNodeButton.setChecked(True)
        self._configItemLis.append(self._withUnknownNodeButton)
        #
        self._listUnknownNodeButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('listUnknownNode', self._listUnknownNodeButton)
        self._listUnknownNodeButton.clicked.connect(self._listUnknownNodeCmd)
        #
        self._cleanUnknownNodeButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('cleanUnknownNode', self._cleanUnknownNodeButton)
        self._cleanUnknownNodeButton.clicked.connect(self._cleanUnknownNodeCmd)
        # Display Layer(s)
        self._withDisplayLayerButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('withDisplayLayer', self._withDisplayLayerButton)
        self._withDisplayLayerButton.setChecked(True)
        self._configItemLis.append(self._withDisplayLayerButton)
        #
        setDisplayLayerSub()
        #
        self._listDisplayLayerButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('listDisplayLayer', self._listDisplayLayerButton)
        self._listDisplayLayerButton.clicked.connect(self._listDisplayLayerCmd)
        #
        self._cleanDisplayLayerButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('cleanDisplayLayer', self._cleanDisplayLayerButton)
        self._cleanDisplayLayerButton.clicked.connect(self._cleanDisplayLayerCmd)
        # Render Layer(s)
        self._withRenderLayerButton = guiQtWidgets.QtCheckbutton()
        toolBox.addButton('withRenderLayer', self._withRenderLayerButton)
        self._withRenderLayerButton.setChecked(True)
        self._configItemLis.append(self._withRenderLayerButton)
        #
        setRenderLayerSub()
        #
        self._listRenderLayerButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('listRenderLayer', self._listRenderLayerButton)
        self._listRenderLayerButton.clicked.connect(self._listRenderLayerCmd)
        #
        self._cleanRenderLayerButton = guiQtWidgets.QtPressbutton()
        toolBox.addButton('cleanRenderLayer', self._cleanRenderLayerButton)
        self._cleanRenderLayerButton.clicked.connect(self._cleanRenderLayerCmd)
        #
        toolBox.addSeparators()
    #
    def setFilterEnableAll(self):
        [i.setChecked(True) for i in self._configItemLis]
    #
    def setFilterEnableClear(self):
        [i.setChecked(False) for i in self._configItemLis]
    #
    def _listUnknownPlugCmd(self):
        pass
    #
    def _cleanUnknownPlugCmd(self):
        pass
    #
    def _listUnknownNodeCmd(self):
        pass
    #
    def _cleanUnknownNodeCmd(self):
        pass
    #
    def _listDisplayLayerCmd(self):
        pass
    #
    def _cleanDisplayLayerCmd(self):
        pass
    #
    def _listRenderLayerCmd(self):
        pass
    #
    def _cleanRenderLayerCmd(self):
        pass
    #
    def setCleanScene(self):
        pass
    #
    def _kit__unit__set_build_(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QHBoxLayout_(widget)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        layout.addWidget(leftExpandWidget)
        leftScrollArea = qtCore.QScrollArea_()
        leftExpandWidget.addWidget(leftScrollArea)
        self._kit__unit__set_left_build_(leftScrollArea)
        #
        rightWidget = qtCore.QWidget_()
        layout.addWidget(rightWidget)
        rightLayout = qtCore.QVBoxLayout_(rightWidget)
        #
        self.setupRightWidget(rightLayout)


#
class IfLightGroupManagerUnit(kitQtWgtAbs.IfToolUnitBasic):
    VAR_kit__qt_wgt__unit__uiname = 'Light Group ( Arnold ) Manager'
    panelWidth = 400
    panelHeight = 800
    UnitScriptJobWindowName = 'lightManagerScriptJobWindow'
    #
    widthSet = 400
    #
    dicLightManagerTool = bscMtdCore.orderedDict()
    dicLightManagerTool['placeholder'] = [1, 0, 0, 1, 4, 'Placeholder']
    def __init__(self, *args, **kwargs):
        super(IfLightGroupManagerUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.nodeDic = bscMtdCore.orderedDict()
        self.lightGroups = []
        #
        self._kit__unit__set_build_()
        #
        self.setTreeViewBox()
    #
    def setConnectObject(self, method):
        self._connectObject = method
    #
    def refreshMethod(self):
        self.setScriptJob()
        #
        self.setListTreeItem(True)
        self.setRefreshTreeViewBoxSelection()
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methods = [self.setRefreshTreeViewBoxSelection]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        scriptJobEvn = 'NameChanged'
        methods = [self.setRefreshTreeViewBoxName]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        scriptJobEvn = 'DagObjectCreated'
        methods = [self.setListTreeItem, self.setRefreshTreeViewBoxSelection]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupTreeView(self, layout):
        self.treeViewBox = qtWidgets_.QTreeWidget_()
        layout.addWidget(self.treeViewBox)
    #
    def setTreeViewBox(self):
        treeViewBox = self.treeViewBox
        #
        treeViewBox.setColumns(['Name', 'Light Group'], [4, 4], self.panelWidth - 20)
        #
        treeViewBox.itemSelectionChanged.connect(self.setRefreshMayaSceneSelection)
        treeViewBox.setKeywordFilterWidgetConnect(self.filterEnterLabel())
    #
    def setRefreshMayaSceneSelection(self):
        treeViewBox = self.treeViewBox
        if treeViewBox.hasFocus():
            selectedItems = treeViewBox.selectedItems()
            if selectedItems:
                for seq, i in enumerate(selectedItems):
                    uuid = i.uuid
                    if seq == 0:
                        maUuid.setSelObject(uuid)
                    else:
                        maUuid.setSelObject(uuid, add=True)
    #
    def setRefreshTreeViewBoxSelection(self):
        treeViewBox = self.treeViewBox
        nodeDic = self.nodeDic
        #
        if not treeViewBox.hasFocus():
            selectedUuids = maUuid.getSelUniqueIds()
            for k, v in nodeDic.items():
                if k in selectedUuids:
                    v.setSelected(True)
                else:
                    v.setSelected(False)
    #
    def setRefreshTreeViewBoxName(self):
        attrName = 'aiAov'
        #
        nodeDic = self.nodeDic
        #
        selectedUuids = maUuid.getSelUniqueIds()
        if selectedUuids:
            uuid = selectedUuids[0]
            if uuid in nodeDic:
                treeItem = nodeDic[uuid]
                objectPath = maUuid.getObject(uuid)
                objectName = maUtils._nodeString2nodename_(objectPath)
                treeItem.path = objectPath
                treeItem.name = objectName
                treeItem.setText(0, objectName)
                #
                self.updateNodeAttrScriptJob(uuid, attrName)
    #
    def setRefreshLightGroups(self):
        pass
    #
    def updateActions(self):
        def setByName():
            selectedUuids = maUuid.getSelUniqueIds()
            if selectedUuids:
                for uuid in selectedUuids:
                    if uuid in nodeDic:
                        objectPath = maUuid.getObject(uuid)
                        objectName = maUtils._nodeString2nodename_(objectPath)
                        objectShape = maUtils._dcc_getNodShapeNodepathStr(objectPath)
                        maUtils.setAttrStringDatum(objectShape, attrName, objectName)
                        self.updateNodeAttrScriptJob(uuid, attrName)
        #
        def setClear():
            selectedUuids = maUuid.getSelUniqueIds()
            if selectedUuids:
                for uuid in selectedUuids:
                    if uuid in nodeDic:
                        objectPath = maUuid.getObject(uuid)
                        objectShape = maUtils._dcc_getNodShapeNodepathStr(objectPath)
                        maUtils.setAttrStringDatum(objectShape, attrName, none)
                        self.updateNodeAttrScriptJob(uuid, attrName)
        #
        def setBranch(lightGroup, index):
            def setLightGroup():
                selectedUuids = maUuid.getSelUniqueIds()
                if selectedUuids:
                    for uuid in selectedUuids:
                        if uuid in nodeDic:
                            objectPath = maUuid.getObject(uuid)
                            objectShape = maUtils._dcc_getNodShapeNodepathStr(objectPath)
                            maUtils.setAttrStringDatum(objectShape, attrName, lightGroup)
                            self.updateNodeAttrScriptJob(uuid, attrName)
            #
            actions.append(
                ('{}#{}'.format(lightGroup, str(index + 1)), None, True, setLightGroup)
            )
        #
        attrName = 'aiAov'
        #
        nodeDic = self.nodeDic
        #
        treeViewBox = self.treeViewBox
        #
        actions = [
            ('Basic', ),
            ('Set by Light Name', 'svg_basic/add', True, setByName),
            ('Extend', ),
            ('Set Clear', 'svg_basic/delete', True, setClear),
        ]
        #
        lightGroups = self.getLightGroups()
        #
        if lightGroups:
            for seq, i in enumerate(lightGroups):
                setBranch(i, seq)
        #
        treeViewBox.setActionData(actions)
    #
    def updateNodeAttrScriptJob(self, uuid, attrName):
        def updateLightGroups():
            data = maUtils.getAttrDatum(objectPath, attrName)
            if uuid in nodeDic:
                treeItem = nodeDic[uuid]
                treeItem.setText(1, data)
            #
            self.updateActions()
        #
        nodeDic = self.nodeDic
        #
        objectPath = maUuid.getObject(uuid)
        objectShape = maUtils._dcc_getNodShapeNodepathStr(objectPath)
        attr = '{}.{}'.format(objectShape, attrName)
        if maUtils._isAppExist(attr):
            maUtils.setCreateAttrChangedScriptJob(self.UnitScriptJobWindowName, attr, updateLightGroups)
    #
    def updateNodeScriptJob(self, node):
        maUtils.setCreateNodeDeleteScriptJob(self.UnitScriptJobWindowName, node, self.setDeleteTreeItem)
    #
    def getLightGroups(self):
        lis = []
        #
        attrName = 'aiAov'
        #
        nodeDic = self.nodeDic
        for uuid in nodeDic:
            objectPath = maUuid.getObject(uuid)
            objectShape = maUtils._dcc_getNodShapeNodepathStr(objectPath)
            attrData = maUtils.getAttrDatum(objectShape, attrName)
            if attrData:
                if not attrData in lis:
                    lis.append(attrData)
        return lis
    #
    def setListTreeItem(self, force=False):
        treeViewBox = self.treeViewBox
        #
        lightTypes = maUtils.getNodeTypeLisByFilter('light')
        #
        if force is True:
            treeViewBox.clear()
            self.nodeDic.clear()
        #
        for lightType in lightTypes:
            lights = maUtils.getNodeTransforms(lightType)
            if lights:
                for lightPath in lights:
                    self.addTreeItem(treeViewBox, lightPath, lightType)
        #
        self.updateActions()
    #
    def addTreeItem(self, treeViewBox, nodePath, nodeType):
        attrName = 'ai_aov'
        #
        lightName = maUtils._nodeString2nodename_(nodePath)
        lightUuid = maUuid._getNodeUniqueIdString(nodePath)
        lightGroup = maUtils.getAttrDatum(nodePath, attrName)
        if lightGroup is not None:
            if not lightUuid in self.nodeDic:
                treeItem = qtWidgets_.QTreeWidgetItem_([lightName, lightGroup])
                treeItem.path = nodePath
                treeItem.name = lightName
                treeItem.uuid = lightUuid
                #
                state = None
                if maUtils.isNodeVisible(nodePath) is False:
                    state = 'off'
                #
                treeItem.setItemMayaIcon(0, nodeType, state)
                #
                treeViewBox.addItem(treeItem)
                #
                self.nodeDic[lightUuid] = treeItem
                #
                self.updateNodeAttrScriptJob(lightUuid, attrName)
                self.updateNodeScriptJob(nodePath)
    #
    def setAddTreeItem(self):
        pass
    #
    def setDeleteTreeItem(self):
        nodeDic = self.nodeDic
        #
        treeViewBox = self.treeViewBox
        count = treeViewBox.topLevelItemCount()
        #
        selectedItems = treeViewBox.selectedItems()
        if selectedItems:
            for i in range(count):
                treeItem = treeViewBox.topLevelItem(i)
                if treeItem in selectedItems:
                    treeViewBox.takeTopLevelItem(i)
                    uuid = treeItem.uuid
                    nodeDic.pop(uuid)
    #
    def _kit__unit__set_build_(self):
        widget = qtCore.QWidget_()
        self.mainLayout().addWidget(widget)
        layout = qtCore.QVBoxLayout_(widget)
        #
        self.topToolBar().show()
        #
        self.setupTreeView(layout)
