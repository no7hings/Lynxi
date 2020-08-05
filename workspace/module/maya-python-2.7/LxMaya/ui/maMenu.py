# coding=utf-8
from LxGui.qt import qtCore
# noinspection PyUnresolvedReferences
import shiboken2
# noinspection PyUnresolvedReferences
import maya.OpenMayaUI as openMayaUI
# noinspection PyUnresolvedReferences
from PySide2 import QtGui, QtCore, QtWidgets
#
Lynxi_Key_Maya_Menu = 'Lynxi'


def getMaMainWindow():
    mainWindowPtr = openMayaUI.MQtUtil.mainWindow()
    mainWindow = shiboken2.wrapInstance(long(mainWindowPtr), QtWidgets.QMainWindow)
    return mainWindow


#
def getMaMenuBar():
    mayaWindow = getMaMainWindow()
    if mayaWindow:
        children = mayaWindow.children()
        for child in children:
            if child:
                if type(child) == QtWidgets.QMenuBar:
                    return child


#
def getMaExistMenu():
    mayaMenuBar = getMaMenuBar()
    if mayaMenuBar:
        children = mayaMenuBar.children()
        for child in children:
            if type(child) == QtWidgets.QMenu:
                menuTitle = child.title()
                if menuTitle.startswith(Lynxi_Key_Maya_Menu):
                    return child


#
def setMayaMenu():
    def addActionFnc_(actionItem, actionData):
        explain, iconKeywordStr, command = actionData
        #
        actionItem.setText(explain)
        #
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(qtCore._toLxOsIconFile(iconKeywordStr)),
            QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        actionItem.setIcon(icon)
        if command is not None:
            actionItem.triggered.connect(command)
    #
    def setToolkitWindowOpenFnc_():
        from LxKit.qt.kitQtWidgets import _kitQtWgtUtilityWindow
        #
        w = _kitQtWgtUtilityWindow.LynxiToolkitWindow()
        w.windowShow()

    def setLogWindowOpenFnc_():
        from LxBasic import bscObjects
        _l = bscObjects.LogWindow()
        _l.showUi()
        bscObjects.connectPrint()

    def setModuleReloadFnc_():
        from LxScheme import shmOutput
        shmOutput.Scheme().loadActiveModules()
    #
    def mainFnc_():
        mayaMenuBar = getMaMenuBar()
        if mayaMenuBar:
            existsMenu = getMaExistMenu()
            if existsMenu is not None:
                existsMenu.close()
                existsMenu.deleteLater()
            #
            lynxiMenu = mayaMenuBar.addMenu(Lynxi_Key_Maya_Menu)
            lynxiMenu.setTearOffEnabled(True)
            #
            lynxiMenu.setObjectName('Lynxi')
            lynxiMenu.setTitle(Lynxi_Key_Maya_Menu)
            for i in menuDatumLis:
                if i:
                    if len(i) > 0:
                        if isinstance(i, tuple):
                            if i:
                                explain = i[0]
                                actionItem = lynxiMenu.addAction(explain)
                                addActionFnc_(actionItem, i)
                        elif isinstance(i, list):
                            suTitle, iconKeywordStr, subActionData = i
                            actionItem = lynxiMenu.addAction(suTitle)
                            icon = QtGui.QIcon()
                            icon.addPixmap(
                                QtGui.QPixmap(qtCore._toLxOsIconFile(iconKeywordStr)),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off
                            )
                            actionItem.setIcon(icon)
                            #
                            subMenu = QtWidgets.QMenu()
                            actionItem.setMenu(subMenu)
                            for j in subActionData:
                                if j:
                                    subExplain = j[0]
                                    subActionItem = subMenu.addAction(subExplain)
                                    addActionFnc_(subActionItem, j)
                                else:
                                    lynxiMenu.addSeparator()
                else:
                    lynxiMenu.addSeparator()
    #
    menuDatumLis = [
        ('Toolkit', 'svg_basic/toolkit', setToolkitWindowOpenFnc_),
        ('Log Window', 'svg_basic/dialog', setLogWindowOpenFnc_),
        (),
        [
            'Extend',
            'svg_basic/menu',
            [
                ('Reload Module(s)', 'svg_basic/update', setModuleReloadFnc_)
            ]
        ],
        ('Help', 'svg_basic/help', None)
    ]
    #
    mainFnc_()
