# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds

from LxBasic import bscMethods

from LxUi.qt import qtMethod

from LxMaya.method.basic import _maMethodBasic


#
class Mtd_MaUiMenu(_maMethodBasic.Mtd_MaUiBasic):
    @staticmethod
    def isMenuExists(menuName):
        pass
    @staticmethod
    def setMenuDelete(menuName):
        pass
    @classmethod
    def setMenuCreate(cls, menuName):
        pass


#
class Mtd_MaUiControl(_maMethodBasic.Mtd_MaUiBasic):
    @staticmethod
    def isControlExists(controlName):
        return cmds.workspaceControl(controlName, exists=True)
    @classmethod
    def setControlVisible(cls, controlName, boolean):
        if cls.isControlExists(controlName):
            cmds.workspaceControl(
                controlName,
                edit=True,
                visible=boolean,
            )
    @classmethod
    def setControlRestore(cls, controlName):
        cmds.workspaceControl(
            controlName,
            edit=True,
            restore=True,
        )
    @classmethod
    def setControlDelete(cls, controlName):
        if cmds.workspaceControl(controlName, exists=True):
            #
            widget = cls._toQtWidget(controlName)
            if widget is not None:
                widget.deleteLater()
            #
            cmds.workspaceControl(
                controlName,
                edit=True,
                close=True
            )
            #
            cmds.deleteUI(controlName)
    @classmethod
    def setControlScript(cls, controlName, script):
        cmds.workspaceControl(
            controlName,
            edit=True,
            uiScript=script
        )
    @classmethod
    def setControlCreate(cls, controlName, width, height):
        if cls.isControlExists(controlName):
            cls.setControlRestore(controlName)
            # cls.setControlVisible(controlName, True)
        else:
            cmds.workspaceControl(
                controlName,
                label=bscMethods.StrCamelcase.toPrettify(controlName),
                dockToMainWindow=['right', False],
                initialWidth=width, initialHeight=height,
                widthProperty='free', heightProperty='free'
            )
    @classmethod
    def setControlCreateTo(cls):
        pass


#
class Mtd_MaQtView(
    qtMethod.QtViewMethod
):
    mtd_app_node = _maMethodBasic.MaNodeMethodBasic
    @classmethod
    def setTreeViewListNamespace(cls, treeView, pathString, branchViewMethod):
        treeViewBuildDic = bscMethods.MayaPath.namespaceTreeViewBuildDic(pathString)
        #
        if treeViewBuildDic:
            cls.setTreeView(treeView, treeViewBuildDic, branchViewMethod)
    @classmethod
    def setTreeViewListNode(cls, treeView, pathString, branchViewMethod):
        treeViewBuildDic = bscMethods.MayaPath.nodeTreeViewBuildDic(pathString)
        #
        if treeViewBuildDic:
            cls.setTreeView(treeView, treeViewBuildDic, branchViewMethod)
