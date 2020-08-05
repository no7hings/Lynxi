# coding:utf-8
#
from LxGui.qt import qtCore

#
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore
#
CLS_point = QtCore.QPoint
CLS_line = QtCore.QLine
CLS_rect = QtCore.QRect


#
class QtGraphviewModel(object):
    def __init__(self, widget, args):
        self.__initBasicAttr()
        self.__initBasicUi()
        #
        self.__initBasicAction()
        #
        self._initBasicVar()
        #
        self.__connectUi(widget)
        self.__setClass(*args)
    #
    def __connectUi(self, widget):
        self.setWidget(widget)
        self.setViewport(widget)
        self.setTimer(widget)
    #
    def __setClass(self, *args):
        (
            self._nodeClass, self._connectionClass, self._groupClass,
            self._explainClass, self._attributeClass,
            self._actionClass,
            self.cls_pointClass, self.cls_pointFClass,
            self.cls_rectClass, self.cls_rectFClass,
            self._pathClass
        ) = args
    #
    def __initBasicAttr(self):
        self._widget = None
        self._viewport = None
        #
        self._timer = None
        #
        self._mBasicViewportWidth, self._mBasicViewportHeight = 512.0, 512.0
        #
        self._startPos = 0, 0
    #
    def __initBasicUi(self):
        self._uiBasicViewportWidth, self._uiBasicViewportHeight = 800.0*16, 800.0*16
        #
        self._uiBasicNodeWidth, self._uiBasicNodeHeight = 240.0, 40.0
        #
        self._uiBasicGridSize = 80
        #
        self._uiGridSize = 40.0, 40.0
        #
        self._wgt__border_rgba = 255, 0, 63, 255
        self._wgt__background_rgba = 0, 0, 255, 64
    #
    def _initBasicVar(self):
        self._nodeModelItemLis = []
        self._connectionLis = []
        self._groupModelItemLis = []
        #
        self._nodeRectDic = {}
        self._nodeGroupIndexDic = {}
        #
        self._nodeIndexCount = 0
        self._connectionIndexCount = 0
        self._groupIndexCount = 0
        #
        self._curNodeIndex = -1
        self._curNodeItemModel = None
        #
        self._curGroupIndex = -1
        self._curGroupItemModel = None
        #
        self.cls_rectSelectStartPoint = CLS_point()
        self.cls_rectSelectEndPoint = CLS_point()
        self._selectRect = CLS_rect()
        #
        self._mTranslate = 0, 0
        self._mScale = .5, .5
        #
        self._selectedNodeIndexLis = []
        self._selectedNodeModelLis = []
        self._selectedConnectionIndexLis = []
        #
        self._matComposite = qtCore.setMatrix3x3Identity(qtCore.matrix3x3())
        self._mTrackPoint = CLS_point()
        self._mViewportPoint = CLS_point()
        #
        self.cls_points = [
            CLS_point(),
            CLS_point(self._mBasicViewportWidth*self._mScale[0], self._mBasicViewportHeight*self._mScale[1])
        ]
        #
        self._mRect = CLS_rect()
        self._updateMRect()
    #
    def __initBasicAction(self):
        self._zoomFlag = True
        self._trackFlag = False
        self.cls_rectSelectionFlag = False
        #
        self._extendSelectFlag = False
        self._selectMode = qtCore.ExtendSelectMode
    #
    def __translateMatrix(self, tx, ty):
        m = self._matComposite
        #
        mTranslate = qtCore.matrix3x3()
        qtCore.setMatrix3x3Identity(mTranslate)
        #
        mTranslate[0][2] = tx
        mTranslate[1][2] = ty
        #
        self._matComposite = qtCore.matrix3x3Multiply(mTranslate, m)
    #
    def __scaleMatrix(self, x, y, sx, sy):
        m = self._matComposite
        #
        mScale = qtCore.matrix3x3()
        qtCore.setMatrix3x3Identity(mScale)
        #
        mScale[0][0] = sx
        mScale[0][2] = (1 - sx)*x
        #
        mScale[1][1] = sy
        mScale[1][2] = (1 - sy)*y
        #
        self._matComposite = qtCore.matrix3x3Multiply(mScale, m)
    #
    def __transformMatrix(self):
        m = self._matComposite
        #
        count = len(self.cls_points)
        for seq in range(count):
            x = m[0][0]*self.cls_points[seq].x() + m[0][1]*self.cls_points[seq].y() + m[0][2]
            y = m[1][0]*self.cls_points[seq].x() + m[1][1]*self.cls_points[seq].y() + m[1][2]
            #
            self.cls_points[seq] = CLS_point(x, y)
        #
        self._matComposite = qtCore.setMatrix3x3Identity(m)
    #
    def _getRectByIndexLis(self, indexLis):
        if indexLis:
            xs1, ys1, xs2, ys2 = [], [], [], []
            for i in indexLis:
                rect = self._nodeRectDic[i]
                x1, y1, x2, y2 = rect.getCoords()
                xs1.append(x1), ys1.append(y1), xs2.append(x2), ys2.append(y2)
            #
            x, y = min(xs1), min(ys1)
            w, h = max(xs2) - x, max(ys2) - y
        else:
            x, y, w, h = 0, 0, 0, 0
        #
        return x, y, w, h
    #
    def _setSelectedIndexLis(self, indices):
        if self._selectedNodeModelLis:
            [i.setSelected(False) for i in self._selectedNodeModelLis]
        #
        self._selectedNodeIndexLis = []
        self._selectedNodeModelLis = []
        #
        for index in indices:
            self.addSelectedIndex(index)
    #
    def _updateCurNode(self, nodeIndex):
        self._curNodeIndex = nodeIndex
        self._curNodeItemModel = self._nodeModelItemLis[nodeIndex]
    #
    def _updateCurGroup(self, groupIndex):
        group = self.groupAt(groupIndex)
        #
        if self._curGroupItemModel is not None:
            self._curGroupItemModel.stackUnder(group)
            self._curGroupItemModel._itemModel._isPressCurrent = False
            self._curGroupItemModel._itemModel.setPressCurrent(False)
        else:
            for g in self._groupModelItemLis:
                if not g == group:
                    g.stackUnder(group)
        #
        group._itemModel.setPressCurrent(True)
        #
        self._curGroupIndex = groupIndex
        self._curGroupItemModel = group
    #
    def _updateSelectState(self):
        def setBranch(itemLis, selectedNodeIndexLis):
            if itemLis:
                for node in itemLis:
                    itemModel = node._itemModel
                    index = itemModel.index()
                    if index in selectedNodeIndexLis:
                        itemModel.setSelected(True)
                    else:
                        itemModel.setSelected(False)
        #
        setBranch(self._nodeModelItemLis, self._selectedNodeIndexLis)
    #
    def _updateNodeSeparateMoveBy(self, itemModel, pressPoint):
        itemModel._dragMoveBy(pressPoint)
        self._updateNodeRect(itemModel)
        #
        self._updateGroupGeometryBy([itemModel])
    #
    def _updateNodesExtendMoveBy(self, itemModel, point):
        selectedNodeModels = self._selectedNodeModelLis
        #
        itemModels = [itemModel]
        #
        if itemModel.isSelected():
            p1 = itemModel._widget.pos()
            for subItemModel in selectedNodeModels:
                p2 = subItemModel.pos()
                #
                offsetPoint = p1 - p2
                subItemModel._dragMoveBy(point, offsetPoint)
                self._updateNodeRect(subItemModel)
                #
                itemModels.append(subItemModel)
        #
        self._updateGroupGeometryBy(itemModels)
    #
    def _updateNodesGroupMoveBy(self, itemModel, point):
        indexLis = itemModel._nodeIndexLis
        if indexLis:
            p1 = itemModel._widget.pos()
            for i in indexLis:
                node = self._nodeModelItemLis[i]
                p2 = node.pos()
                #
                offsetPoint = p1 - p2
                #
                node._itemModel._dragMoveBy(point, offsetPoint)
                self._updateNodeRect(node._itemModel)
    #
    def _updateNodeGroupIndexDic(self, groupIndex, nodeIndexLis):
        for i in nodeIndexLis:
            self._nodeGroupIndexDic[i] = groupIndex
    #
    def _updateGroupGeometryBy(self, itemModels):
        lis = []
        for itemModel in itemModels:
            nodeIndex = itemModel._index
            if nodeIndex in self._nodeGroupIndexDic:
                groupIndex = self._nodeGroupIndexDic[nodeIndex]
                if not groupIndex in lis:
                    lis.append(groupIndex)
        #
        if lis:
            [self.groupModelAt(i).update() for i in lis]
    #
    def _updateNodeRect(self, itemModel):
        node = itemModel._widget
        index = itemModel._index
        #
        rect = CLS_rect(
            node._itemModel.x(), node._itemModel.y() - 20,
            node._itemModel.width_(), node._itemModel.height_() + 20
        )
        self._nodeRectDic[index] = rect
    # Nde_Geometry
    def _gui_qt__mdl__set_viewport_geometry_update_(self):
        xPos, yPos = self._mTranslate
        #
        width = self._uiBasicViewportWidth*self._mScale[0]
        height = self._uiBasicViewportHeight*self._mScale[1]
        #
        self._viewport.setGeometry(
            xPos, yPos, width, height
        )
    #
    def _updateVisibleNodesGeometry(self):
        count = self._nodeIndexCount
        if count > 0:
            for index in range(count):
                node = self._nodeModelItemLis[index]
                node._itemModel._updateTranslate(self._mTranslate)
                # node._itemModel._updateScale(self._mScale)
                node._itemModel.update()
                #
                self._updateNodeRect(node._itemModel)
    #
    def _updateGroupsGeometry(self):
        count = self._groupIndexCount
        if count > 0:
            for index in range(count):
                group = self.groupAt(index)
                group._itemModel.update()
    #
    def _gui_qt__mdl__set_geometry_update_(self):
        self._updateVisibleNodesGeometry()
        self._updateGroupsGeometry()
    #
    def _updateSelectMode(self, boolean, selectMode):
        self._extendSelectFlag = boolean
        self._selectMode = selectMode
        #
        self._widget.update()
    #
    def _updateSelectRect(self):
        xPos, yPos = self.cls_rectSelectStartPoint.x(), self.cls_rectSelectStartPoint.y()
        width, height = self.cls_rectSelectEndPoint.x() - xPos, self.cls_rectSelectEndPoint.y() - yPos
        #
        self._selectRect.setRect(
            xPos, yPos,
            width, height
        )
    #
    def _updateGridSize(self):
        self._uiGridSize = int(self._uiBasicGridSize*self._mScale[0]), int(self._uiBasicGridSize*self._mScale[1])
    #
    def _updateMRect(self):
        self._mRect.setCoords(self.cls_points[0].x(), self.cls_points[0].y(), self.cls_points[1].x(), self.cls_points[1].y())
    #
    def _updateVar(self):
        self._updateMRect()
        #
        self._mViewportPoint = self._mRect.topLeft()
        #
        self._mScale = self._mRect.width()/self._mBasicViewportWidth, self._mRect.height()/self._mBasicViewportHeight
        #
        self._mTranslate = self._mViewportPoint.x(), self._mViewportPoint.y()
    # Rect Selection
    def _updateRectSelectBy(self, selectRect):
        def setBranch(rectDic):
            intersections = []
            for k, v in rectDic.items():
                nodeRect = v
                if selectRect.intersects(nodeRect):
                    intersections.append(k)
            #
            if intersections:
                selectedNodeIndexLis = self._selectedNodeIndexLis
                for index in intersections:
                    if self.selectMode() is qtCore.ExtendSelectMode:
                        if index in selectedNodeIndexLis:
                            self.subSelectedIndex(index)
                        else:
                            self.addSelectedIndex(index)
                    elif self.selectMode() is qtCore.SubSelectMode:
                        self.subSelectedIndex(index)
            #
            self._updateSelectState()
        #
        setBranch(self._nodeRectDic)
    #
    def _trackStartAction(self, event):
        self._mTrackPoint = event.pos()
        # Flag
        self._trackFlag = True
    #
    def _trackExecuteAction(self, event):
        if self._trackFlag is True:
            point = event.pos()
            #
            p = point - self._mTrackPoint
            tx, ty = p.x(), p.y()
            self.__translateMatrix(tx, ty)
            self.__transformMatrix()
            #
            self._mTrackPoint = point
            #
            self.update()
    #
    def _trackStopAction(self, event):
        self._mTrackPoint = event.pos()
        # Flag
        self._trackFlag = False
    #
    def cls_rectSelectStartAction(self, event):
        point = event.pos()
        #
        self.cls_rectSelectionFlag = True
        #
        self.cls_rectSelectStartPoint = self.cls_rectSelectEndPoint = point
        self._updateSelectRect()
        #
        self._widget.update()
    #
    def cls_rectSelectExecuteAction(self, event):
        point = event.pos()
        if self.cls_rectSelectionFlag is True:
            self.cls_rectSelectEndPoint = point
            self._updateSelectRect()
            #
            self._widget.update()
    #
    def cls_rectSelectStopAction(self):
        if self.cls_rectSelectionFlag is True:
            self._updateRectSelectBy(self._selectRect)
            #
            self.cls_rectSelectionFlag = False
            #
            self._widget.update()
    #
    def _selectClearAction(self):
        if self.isExtendSelect() is False:
            self.setSelectedClear()
    #
    def _zoomStartAction(self, event):
        pass
    #
    def _zoomAction(self, event):
        if self._zoomFlag is True:
            delta = event.angleDelta().y()
            point = event.pos()
            #
            if delta > 0:
                sx, sy = 1 + .25, 1 + .25
            else:
                sx, sy = 1/(1 + .25), 1/(1 + .25)
            #
            tx, ty = point.x(), point.y()
            #
            self.__scaleMatrix(tx, ty, sx, sy)
            self.__transformMatrix()
            #
            self._mTrackPoint = point
            #
            self.update()
    #
    def update(self):
        self._updateVar()
        #
        self._updateGridSize()
        self._gui_qt__mdl__set_geometry_update_()
        #
        self._widget.update()
    #
    def separateSelectAt(self, index):
        if self.isExtendSelect():
            if self.selectMode() != qtCore.SubSelectMode:
                self._setSelectedIndexLis([index])
        else:
            self._setSelectedIndexLis([index])
    #
    def extendSelectAt(self, index):
        selectedNodeIndexLis = self._selectedNodeIndexLis
        #
        if self.isExtendSelect():
            if self.selectMode() == qtCore.ExtendSelectMode:
                if index in selectedNodeIndexLis:
                    self.subSelectedIndex(index)
                else:
                    self.addSelectedIndex(index)
            elif self.selectMode() == qtCore.SubSelectMode:
                self.subSelectedIndex(index)
    #
    def setSelectedClear(self):
        def setBranch(itemLis):
            if itemLis:
                [i.setSelected(False) for i in itemLis]
        #
        self._selectedNodeIndexLis = []
        self._selectedNodeModelLis = []
        #
        setBranch(self.nodes())
    #
    def addSelectedIndex(self, index):
        itemModel = self.nodeModelAt(index)
        if itemModel.isVisible():
            if not index in self._selectedNodeIndexLis:
                self._selectedNodeIndexLis.append(index)
                self._selectedNodeModelLis.append(itemModel)
                #
                itemModel.setSelected(True)
    #
    def subSelectedIndex(self, index):
        itemModel = self.nodeModelAt(index)
        if index in self._selectedNodeIndexLis:
            self._selectedNodeIndexLis.remove(index)
            self._selectedNodeModelLis.remove(itemModel)
            #
            itemModel.setSelected(False)
    #
    def selectedCount(self):
        return len(self._selectedNodeIndexLis)
    #
    def addNode(self, nodeName, nodeType, x=0, y=0):
        node = self._nodeClass(self._widget)
        node._itemModel.setViewModel(self)
        #
        node._itemModel.setIndex(self._nodeIndexCount)
        node._itemModel.setType(nodeType)
        node._itemModel.setName(nodeName)
        #
        node._itemModel.setNameString(nodeName)
        #
        node._itemModel.setAttributes(['input1', 'input2', 'input3'], ['output1', 'output2', 'output3'])
        #
        node._itemModel._updateGlobalPos(x, y)
        node._itemModel.update()
        #
        self._nodeModelItemLis.append(node)
        self._nodeIndexCount += 1
        #
        return node
    #
    def addGroup(self, groupName, groupType, nodeIndexLis):
        group = self._groupClass(self._widget)
        group._itemModel.setViewModel(self)
        #
        group.lower()
        #
        group._itemModel.setIndex(self._groupIndexCount)
        group._itemModel.setType(groupType)
        group._itemModel.setName(groupName)
        group._itemModel.setNameString(groupName)
        #
        group._itemModel.setIndexes(nodeIndexLis)
        self._updateNodeGroupIndexDic(self._groupIndexCount, nodeIndexLis)
        #
        self._groupModelItemLis.append(group)
        self._groupIndexCount += 1
        return group
    #
    def addConnection(self, sourceNode, targetNode):
        connection = self._connectionClass(self._widget)
        connection._itemModel.setViewModel(self)
        #
        connection._itemModel.setIndex(
            sourceNode.index(),
            targetNode.index(),
            self._connectionIndexCount
        )
        connection.lower()
        #
        connection._itemModel.setOutputNode(sourceNode)
        connection._itemModel.setInputNode(targetNode)
        #
        sourceNode._itemModel._addOutputConnection(connection)
        targetNode._itemModel._addInputConnection(connection)
        #
        connection._itemModel.update()
        #
        self._connectionLis.append(connection)
        self._connectionIndexCount += 1
        return connection
    #
    def connectAttr(self, sourceAttr, targetAttr):
        pass
    #
    def nodes(self):
        return self._nodeModelItemLis
    #
    def nodeAt(self, index):
        return self._nodeModelItemLis[index]
    #
    def nodeModelAt(self, index):
        return self._nodeModelItemLis[index]._itemModel
    #
    def groupAt(self, index):
        return self._groupModelItemLis[index]
    #
    def groupModelAt(self, index):
        return self._groupModelItemLis[index]._itemModel
    #
    def connections(self):
        return self._connectionLis
    #
    def setViewport(self, widget):
        self._viewport = widget._viewport
    #
    def setTimer(self, widget):
        self._timer = widget._timer
    #
    def isExtendSelect(self):
        return self._extendSelectFlag
    #
    def isAddSelectMode(self):
        return self._selectMode == qtCore.AddSelectMode
    #
    def selectMode(self):
        return self._selectMode
    #
    def isSubSelectMode(self):
        return self._selectMode == qtCore.SubSelectMode
    #
    def isExtendSelectMode(self):
        return self._selectMode == qtCore.ExtendSelectMode
    #
    def isNonSelected(self):
        return self._selectedNodeIndexLis == []
    #
    def isHasSelected(self):
        return self._selectedNodeIndexLis != []
    #
    def selectedNodeIndexLis(self):
        return self._selectedNodeIndexLis
    #
    def selectedNodeModels(self):
        return self._selectedNodeModelLis
    #
    def setWidget(self, widget):
        self._widget = widget
    #
    def widget(self):
        return self._widget
    #
    def setVisible(self, boolean):
        self._widget.setVisible(boolean)
    #
    def isVisible(self):
        return self._widget.isVisible()
    #
    def size(self):
        return self._widget.width(), self._widget.height()
    #
    def width(self):
        return self._widget.width()
    #
    def height(self):
        return self._widget.height()
    #
    def pos(self):
        return self._widget.pos()
    #
    def x(self):
        return self._widget.x()
    #
    def y(self):
        return self._widget.y()