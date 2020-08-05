# coding:utf-8
from LxGui.qt import qtCore
#
QtGui = qtCore.QtGui
QtCore = qtCore.QtCore


#
class QtTrackactionModel(object):
    def __init__(self, model):
        self._model = model
        #
        self.__initActionVar()
    #
    def __initActionVar(self):
        self._startPos = 0, 0
        self._stopPos = 0, 0
        #
        self._pos = 0, 0
        #
        self._isHTrackable, self._isVTrackable = True, True
        #
        self._minimumPos = -166667, -166667
        self._maxPos = 166667, 166667
    #
    def _getClampPos(self, x, y):
        return max(min(x, self._maxPos[0]), self._minimumPos[0]), max(min(y, self._maxPos[1]), self._minimumPos[1])
    #
    def _getFilterPos(self, xPos, yPos):
        if self._isHTrackable is False:
            xPos = 0
        if self._isVTrackable is False:
            yPos = 0
        return xPos, yPos
    #
    def _updateTrackable(self, hBoolean, vBoolean):
        self._isHTrackable, self._isVTrackable = hBoolean, vBoolean
    #
    def _updateStartLoc(self, x, y):
        self._startPos = x, y
    #
    def _updateExecuteLoc(self, x, y):
        x_, y_ = x - self._model._wgt__margins[0], y - self._model._wgt__margins[1]
        #
        xPos, yPos = self._stopPos
        #
        xPos -= x_
        yPos -= y_
        #
        xPos, yPos = self._getFilterPos(xPos, yPos)
        #
        self._pos = self._getClampPos(xPos, yPos)
    #
    def _startAction(self, event):
        point = event.globalPos()
        #
        x, y = point.x(), point.y()
        #
        self._updateStartLoc(x, y)
    #
    def _executeAction(self, event):
        point = event.globalPos()
        x, y = point.x(), point.y()
        #
        x -= self._startPos[0]
        y -= self._startPos[1]
        #
        self._updateExecuteLoc(x, y)
    #
    def _stopAction(self):
        self._stopPos = self._pos
    #
    def setPos(self, xPos, yPos):
        self._pos = self._stopPos = self._getFilterPos(xPos, yPos)
    #
    def setMinimumPos(self, xPos, yPos):
        self._minimumPos = xPos, yPos
    #
    def setMaximumPos(self, xPos, yPos):
        self._maxPos = xPos, yPos
    #
    def pos(self):
        return self._pos
