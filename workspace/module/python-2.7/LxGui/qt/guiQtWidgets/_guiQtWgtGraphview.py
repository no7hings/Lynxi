# coding=utf-8
import sys
#
from LxGui.qt import qtCore, guiQtWgtAbs
#
#
from LxGui.qt.guiQtModels import _guiQtMdlGraphview
#
from LxGui.qt.guiQtWidgets import _guiQtWgtGraphitem
#
QtCore = qtCore.QtCore
#
ExtendSelectMode = 0
AddSelectMode = 1
SubSelectMode = 2


#
def setDrawConnectionFrame(painter, xPos, yPos, width, height, backgroundRgba, borderRgba):
    painter.setBackgroundRgba(backgroundRgba)
    color = qtCore.CLS_color(borderRgba[0], borderRgba[1], borderRgba[2], borderRgba[3])
    pen = qtCore.CLS_pen(color)
    painter.setPen(pen)
    uiShadowRadius = 0
    points = [
        (xPos, yPos),
        (width + xPos - uiShadowRadius, yPos),
        (width + xPos - uiShadowRadius, height + yPos - uiShadowRadius),
        (xPos, height + yPos - uiShadowRadius)
    ]
    #
    l_ = 8
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = points
    lines = (
        ((x1, y1 + l_), (x1, y1), (x1 + l_, y1)),
        ((x2 - l_, y2), (x2, y2), (x2, y2 + l_)),
        ((x3, y3 - l_), (x3, y3), (x3 - l_, y3)),
        ((x4 + l_, y4), (x4, y4), (x4, y4 - l_))
    )
    [painter.setDrawPath(i) for i in lines]


#
def setDrawPositionMark(painter, width, height, string, borderRgba):
    rect = qtCore.CLS_rect(4, 0, width, height - 4)
    #
    painter.setBorderRgba(borderRgba)
    painter.setFont(qtCore.qtFont(size=10, weight=75, family=qtCore._families[1]))
    painter.drawText(rect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, string)


#
def setDrawKeyPressMark(painter, width, height, key, borderRgba):
    rect = qtCore.CLS_rect(width - 120 - 4, 0, 120, height - 4)
    #
    painter.setBorderRgba(borderRgba)
    painter.setFont(qtCore.qtFont(size=10, weight=75, family=qtCore._families[1]))
    painter.drawText(rect, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom, key)


# Main
class xNodeViewport(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(xNodeViewport, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setMouseTracking(True)
        #
        self.initUi()
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHint(painter.Antialiasing)
        # Background
        if self._drawBackgroundEnable is True:
            xPos = 0
            yPos = 0
            width = self.width()
            height = self.height()
            #
            painter.setBackgroundRgba(self._wgt__background_rgba)
            painter.setBorderRgba(self._wgt__border_rgba)
            rect = qtCore.CLS_rect(xPos, yPos, width, height)
            painter.drawRect(rect)

        # painter.end()  # for pyside2
    #
    def initUi(self):
        self._wgt__border_rgba = 255, 0, 63, 255
        self._wgt__background_rgba = 0, 0, 0, 0
        #
        self._drawBackgroundEnable = False
        #
        self._selectRect = qtCore.CLS_rectF()


#
class QtGraphview(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        if qtCore.LOAD_INDEX is 0:
            self._clsSuper = super(qtCore.QWidget, self)
            self._clsSuper.__init__(*args, **kwargs)
        else:
            self._clsSuper = super(QtGraphview, self)
            self._clsSuper.__init__(*args, **kwargs)
        #
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        #
        self.setMouseTracking(True)
        #
        self.initUi()
        #
        self.setupUi()
        #
        self.addNodes_()
    #
    def keyPressEvent(self, event):
        if event.modifiers() == QtCore.Qt.Key_Control:
            self._ctrlFlag = True
            self._viewModel._updateSelectMode(True, SubSelectMode)
        elif event.modifiers() == QtCore.Qt.Key_Shift:
            self._shiftFlag = True
            self._viewModel._updateSelectMode(True, ExtendSelectMode)
        elif event.modifiers() == QtCore.Qt.Key_Alt:
            self._altFlag = True
        elif event.modifiers() == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier):
            self._viewModel._updateSelectMode(True, AddSelectMode)
        else:
            event.ignore()
    #
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self._ctrlFlag = False
            self._viewModel._updateSelectMode(False, ExtendSelectMode)
        elif event.key() == QtCore.Qt.Key_Shift:
            self._shiftFlag = False
            self._viewModel._updateSelectMode(False, ExtendSelectMode)
        elif event.key() == QtCore.Qt.Key_Alt:
            self._altFlag = False
        elif event.modifiers() == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier):
            self._viewModel._updateSelectMode(False, ExtendSelectMode)
        else:
            event.ignore()
    #
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            # Select Clear
            self._viewModel._selectClearAction()
            # Rect Select
            self._viewModel.cls_rectSelectStartAction(event)
        elif event.button() == QtCore.Qt.RightButton:
            event.ignore()
        elif event.button() == QtCore.Qt.MidButton:
            # Track
            self._viewModel._trackStartAction(event)
        else:
            event.ignore()
    #
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._viewModel.cls_rectSelectStopAction()
        elif event.button() == QtCore.Qt.RightButton:
            event.ignore()
        elif event.button() == QtCore.Qt.MidButton:
            self._viewModel._trackStopAction(event)
        else:
            event.ignore()
    #
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            event.ignore()
        else:
            if event.buttons() == QtCore.Qt.LeftButton:
                # Rect Select
                self._viewModel.cls_rectSelectExecuteAction(event)
            elif event.buttons() == QtCore.Qt.RightButton:
                event.ignore()
            elif event.buttons() == QtCore.Qt.MidButton:
                # Track
                self._viewModel._trackExecuteAction(event)
            else:
                event.ignore()
    #
    def wheelEvent(self, event):
        self._viewModel._zoomAction(event)
    #
    def paintEvent(self, event):
        painter = qtCore.QPainter_(self)
        # painter.begin(self)  # for pyside2

        painter.setRenderHint(painter.Antialiasing)
        #
        xPos, yPos = 0, 0
        width, height = self.width(), self.height()
        #
        gridSize = self._viewModel._uiGridSize[0]
        #
        painter.setBackgroundRgba(self._wgt__background_rgba)
        painter.setBorderRgba(self._wgt__border_rgba)
        if self._drawBackgroundEnable is True:
            rect = qtCore.CLS_rect(xPos, yPos, width, height)
            painter.drawRect(rect)
        if self._drawGridEnable is True:
            painter.setDrawGrid(
                width, height, (1, 1), gridSize, self._viewModel._mTranslate, (0, 0),
                self._gridBorderRgba
            )
        if self._drawGridMarkEnable is True:
            painter.setDrawGridMark(
                width, height, (1, 1), gridSize, self._viewModel._mTranslate, (0, 0), (1, 1), (0, 0),
                self._markBorderRgba,
                0
            )
        if self._drawPositionEnable is True:
            string = 'Position: {}, {}'.format(
                -self._viewModel._mViewportPoint.x(), -self._viewModel._mViewportPoint.y()
            )
            setDrawPositionMark(
                painter,
                width, height,
                string,
                self._zoomBorderRgba
            )
        if self._shiftFlag or self._ctrlFlag is True:
            painter.setDrawKeyPressMark(
                width, height,
                ['Shift', 'Ctrl + Shift', 'Ctrl'][self._viewModel.selectMode()],
                self._zoomBorderRgba
            )
        if self._viewModel.cls_rectSelectionFlag is True:
            painter.setDrawDottedFrame(
                self._viewModel._selectRect,
                self._selectBackgroundRgba,
                self._selectBorderRgba
            )

        # painter.end()  # for pyside2
    #
    def addNodes_(self):
        xScale, yScale = self._viewModel._mScale
        nodes = self.addNodes__()
        xs = [i.x() for i in nodes]
        ys = [i.y() for i in nodes]
        node0 = self.addNode('scenery0', 'scenery', (max(xs) + 480*xScale), (min(ys) + (max(ys) - min(ys))/2 - 40*yScale))
        node1 = self.addNode('scenery1', 'scenery', (max(xs) + 480*xScale), (min(ys) + (max(ys) - min(ys))/2 + 40*yScale))
        #
        [(self.addConnection(i, node0), self.addConnection(i, node1)) for i in nodes]
        #
        group0 = self._viewModel.addGroup('group0', 'group', range(10))
        group0.setColor(0, 64, 255)
        group1 = self._viewModel.addGroup('group1', 'group', range(10, 20))
        group1.setColor(255, 0, 64)
        group2 = self._viewModel.addGroup('group0', 'group', range(20, 22))
        group2.setColor(127, 64, 255)
    #
    def addNodes__(self):
        xScale, yScale = self._viewModel._mScale
        lis = []
        for i in range(20):
            xPos = (self._viewModel._startPos[0] + 80*(i % 5))*xScale
            yPos = (self._viewModel._startPos[1] + 80*i)*yScale
            node = self.addNode('asset' + str(i), 'asset', xPos, yPos)
            lis.append(node)
        return lis
    #
    def addNode(self, nodeName, nodeType, xPos, yPos):
        return self._viewModel.addNode(nodeName, nodeType, xPos, yPos)
    #
    def addConnection(self, sourceNode, targetNode):
        return self._viewModel.addConnection(sourceNode, targetNode)
    #
    def uiShow(self):
        width, height = self._uiDefaultWidth, self._uiDefaultHeight
        #
        xOf = 0
        yOf = 0
        #
        desktopRect = qtCore.getDesktopPrimaryRect()
        maxWidth = desktopRect.width()
        maxHeight = desktopRect.height()
        if qtCore.getAppWindow():
            parent = qtCore.getAppWindow()
            maxWidth = parent.width()
            maxHeight = parent.height()
            xOf = parent.x()
            yOf = parent.y()
        #
        xPosition = maxWidth / 2 - width / 2 + xOf
        yPosition = maxHeight / 2 - height / 2 + yOf
        #
        self.setGeometry(
            QtCore.QRect(xPosition, yPosition, width, height)
        )
        self.show()
    #
    def setUiSize(self, width, height):
        self._uiDefaultWidth = width
        self._uiDefaultHeight = height
        # self.setMaximumSize(self._uiDefaultWidth, self._uiDefaultHeight)
        self.setMinimumSize(self._uiDefaultWidth, self._uiDefaultHeight)
        #
        self.update()
    #
    def viewModel(self):
        return self._viewModel
    #
    def initUi(self):
        self._uiDefaultWidth, self._uiDefaultHeight = 800, 800
        #
        self._altFlag = False
        self._shiftFlag = False
        self._ctrlFlag = False
        #
        self._wgt__border_rgba = 95, 95, 95, 255
        self._wgt__background_rgba = 56, 56, 56, 255
        #
        self._gridBorderRgba = 63, 63, 63, 255
        self._markBorderRgba = 127, 127, 127, 255
        self._zoomBorderRgba = 223, 223, 223, 255
        self._selectBackgroundRgba = 0, 0, 0, 0
        self._selectBorderRgba = 255, 127, 0, 255
        #
        self._groupBackgroundRgba = 0, 0, 0, 0
        self._groupBorderRgba = 127, 127, 127, 255
        #
        self._drawBackgroundEnable = True
        self._drawGridEnable = True
        self._drawGridMarkEnable = False
        self._drawPositionEnable = False
    #
    def setupUi(self):
        self._timer = qtCore.CLS_timer(self)
        #
        self._viewport = xNodeViewport(self)
        #
        self._viewModel = _guiQtMdlGraphview.QtGraphviewModel(
            self,
            (
                _guiQtWgtGraphitem.xGraphNodeItem, _guiQtWgtGraphitem.xGraphConnectionItem, _guiQtWgtGraphitem.xGraphGroupItem,
                _guiQtWgtGraphitem.xGraphExplainItem, _guiQtWgtGraphitem.xGraphAttributePortItem,
                guiQtWgtAbs.AbsGuiQtActionViewportWgt,
                qtCore.CLS_point, qtCore.CLS_pointF,
                qtCore.CLS_rect, qtCore.CLS_rectF,
                qtCore.CLS_painterPath
            )
        )


#
class xNodeAddCommand(qtCore.QUndoCommand):
    def __init__(self, *args):
        super(xNodeAddCommand, self).__init__(*args)


#
class xNodeBox(qtCore.QWidget):
    def __init__(self, *args, **kwargs):
        super(xNodeBox, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    #
    def setupUi(self):
        layout = qtCore.QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.zoomArea.setGeometry(0, 0, 400, 400)
        self._viewport = xNodeViewport(self)


#
if __name__ == '__main__':
    app = qtCore.QApplication(sys.argv)
    a = QtGraphview()
    a.uiShow()
    a._viewModel.update()
    sys.exit(app.exec_())
