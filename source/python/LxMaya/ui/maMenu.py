# coding=utf-8
from LxUi import uiCore
# noinspection PyUnresolvedReferences
import shiboken2
# noinspection PyUnresolvedReferences
import maya.OpenMayaUI as openMayaUI
# noinspection PyUnresolvedReferences
from PySide2 import QtGui, QtCore, QtWidgets
#
Lynxi_Key_Maya_Menu = '&Lynxi'


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
    def addActionBranch(actionItem, actionData):
        explain, iconKeyword, command = actionData
        #
        actionItem.setText(explain)
        #
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(uiCore._toLxOsIconFile(iconKeyword)),
            QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        actionItem.setIcon(icon)
        if command is not None:
            actionItem.triggered.connect(command)
    #
    def toolShelfCmd():
        from LxInterface.qt.ifWidgets import ifProductWindow
        #
        w = ifProductWindow.IfToolFloatWindow()
        w.windowShow()
    #
    def toolKitControlCmd():
        from LxMaya.operation import maUiBuild
        toolKit = maUiBuild.MaToolKitBuild()
        toolKit.show()
    #
    def toolKitCmd():
        from LxInterface.qt.ifWidgets import ifProductWindow
        #
        w = ifProductWindow.IfToolkitWindow()
        w.windowShow()
    #
    def setMain():
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
            lynxiMenu.setTitle(Lynxi_Key_Maya_Menu)
            for i in menuDatumLis:
                if i:
                    if len(i) > 0:
                        if isinstance(i, tuple):
                            if i:
                                explain = i[0]
                                actionItem = lynxiMenu.addAction(explain)
                                addActionBranch(actionItem, i)
                        elif isinstance(i, list):
                            suTitle, iconKeyword, subActionData = i
                            actionItem = lynxiMenu.addAction(suTitle)
                            icon = QtGui.QIcon()
                            icon.addPixmap(
                                QtGui.QPixmap(uiCore._toLxOsIconFile(iconKeyword)),
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
                                    addActionBranch(subActionItem, j)
                                else:
                                    lynxiMenu.addSeparator()
                else:
                    lynxiMenu.addSeparator()
    #
    from LxCore.preset.prod import projectPr
    currentProject = projectPr.getMayaProjectName()
    #
    menuDatumLis = [
        ('Project [ {} ]'.format(currentProject), 'svg_basic@svg#menu', toolShelfCmd),
        (),
        ('Tool Kit', 'svg_basic@svg#toolkit', toolKitCmd),
        (),
        ('Help', 'svg_basic@svg#help', None)
    ]
    #
    setMain()