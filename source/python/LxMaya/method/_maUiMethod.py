# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds
#
from LxCore.method import _uiMethod
#
from LxMaya.method.basic import _maMethodBasic


#
class MaUiMenuMethod(_maMethodBasic.MaUiMethodBasic):
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
class MaUiControlMethod(_maMethodBasic.MaUiMethodBasic):
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
                label=cls._toStringPrettify(controlName),
                dockToMainWindow=['right', False],
                initialWidth=width, initialHeight=height,
                widthProperty='free', heightProperty='free'
            )
    @classmethod
    def setControlCreateTo(cls):
        pass


#
class MaUiViewMethod(_maMethodBasic.MaNodeMethodBasic, _uiMethod.UiViewMethod):
    @classmethod
    def setTreeViewListNamespace(cls, treeView, pathString, branchViewMethod):
        pathsep = cls.Ma_Separator_Namespace
        #
        treeViewPathLis = cls._toTreeViewPathLis(pathString, pathsep)
        treeViewBuildDic = cls.getTreeViewBuildDic(treeViewPathLis, pathsep)
        #
        if treeViewBuildDic:
            cls.setTreeView(treeView, treeViewBuildDic, branchViewMethod)
    @classmethod
    def setTreeViewListNode(cls, treeView, pathString, branchViewMethod):
        pathsep = cls.Ma_Separator_Node
        #
        treeViewPathLis = cls._toTreeViewPathLis(pathString, pathsep)
        treeViewBuildDic = cls.getTreeViewBuildDic(treeViewPathLis, pathsep)
        #
        if treeViewBuildDic:
            cls.setTreeView(treeView, treeViewBuildDic, branchViewMethod)
