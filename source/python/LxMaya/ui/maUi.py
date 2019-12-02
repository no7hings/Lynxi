# coding=utf-8
# noinspection PyUnresolvedReferences
import shiboken2
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMayaUI
# noinspection PyUnresolvedReferences
from PySide2 import QtGui, QtCore, QtWidgets


#
def toMaObject(ptr, base=QtWidgets.QWidget):
    return shiboken2.wrapInstance(long(ptr), base)


#
def getUiMainWindow():
    mainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
    return toMaObject(mainWindowPtr, QtWidgets.QMainWindow)


#
def getMaWidget(mayaUI, base):
    ptr = OpenMayaUI.MQtUtil.findControl(mayaUI)
    return toMaObject(ptr, base)


#
def getUiMenuBar():
    for eachChild in getUiMainWindow().children():
        if type(eachChild) == QtWidgets.QMenuBar:
            return eachChild


#
def getMaAttributePanel():
    return getMaWidget('AttributeEditor', QtWidgets.QWidget)


#
def setAddMaControl(controlName, width, height, script=None):
    if cmds.workspaceControl(controlName, exists=True):
        cmds.deleteUI(controlName)
    #
    cmds.workspaceControl(
        controlName,
        label='Lynxi Test',
        uiScript=script,
        dockToControl=['MainPane', 'right'],
        initialWidth=width, initialHeight=height,
    )
