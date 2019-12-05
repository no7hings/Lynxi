# coding=utf-8
import os
#
import sys
# noinspection PyUnresolvedReferences
import shiboken2
# noinspection PyUnresolvedReferences
import maya.OpenMayaUI as openMayaUI
# noinspection PyUnresolvedReferences
from PySide2 import QtGui, QtCore, QtWidgets
#
DefMenuName = '&Lynxi Tool(s)'


#
def isMayaApp():
    boolean = False
    data = os.path.basename(sys.argv[0])
    if data.lower() == 'maya.exe':
        boolean = True
    return boolean


#
def getMainWindow():
    if isMayaApp():
        mainWindowPtr = openMayaUI.MQtUtil.mainWindow()
        if mainWindowPtr is not None:
            mainWindow = shiboken2.wrapInstance(long(mainWindowPtr), QtWidgets.QMainWindow)
            return mainWindow


#
def getMayaMenuBar():
    mayaWindow = getMainWindow()
    if mayaWindow:
        children = mayaWindow.children()
        for child in children:
            if type(child) == QtWidgets.QMenuBar:
                return child


#
def getDefMenu():
    mayaMenuBar = getMayaMenuBar()
    if mayaMenuBar:
        children = mayaMenuBar.children()
        for child in children:
            if type(child) == QtWidgets.QMenu:
                menuTitle = child.title()
                if menuTitle.startswith(DefMenuName):
                    return child


#
def setupMenu():
    def createMeshByCurveCmd():
        import lxCommand.cmds as ctomcmds
        ctomcmds.setMeshCreateByCurve()

    def createMeshByCurveCmd_():
        import lxCommand.cmds as ctomcmds
        ctomcmds.setMeshCreateByCurve(False)
    #
    def createMeshByBonusCurveCmd():
        import lxCommand.cmds as ctomcmds
        ctomcmds.setCreateByBonusCurve()
    #
    def createSurfaceByMeshCmd():
        import lxCommand.cmds as ctomcmds
        ctomcmds.setSurfaceCreateByMesh()
    #
    menuDatumLis = [
        ('Create Mesh by Curve(s)(Auto)', createMeshByCurveCmd),
        ('Create Mesh by Curve(s)', createMeshByCurveCmd_),
        ('Create Mesh by Bonus Curve(s)', createMeshByBonusCurveCmd),
        (),
        ('Create Surface by Mesh(s)', createSurfaceByMeshCmd),
        (),
        ('About', None)
    ]
    #
    mayaMenuBar = getMayaMenuBar()
    if mayaMenuBar:
        defMenu = getDefMenu()
        if defMenu is not None:
            defMenu.deleteLater()
        #
        defMenu = mayaMenuBar.addMenu(DefMenuName)
        defMenu.setTearOffEnabled(True)
        defMenu.setWindowTitle(DefMenuName[1:])
        defMenu.setObjectName(DefMenuName)
        #
        for i in menuDatumLis:
            if i:
                explain, command = i
                #
                action = defMenu.addAction(explain)
                if command is not None:
                    action.triggered.connect(command)
            else:
                defMenu.addSeparator()
