# coding:utf-8
import types
#
from LxCore.config import appConfig

from LxCore.method.basic import _methodBasic

from LxUi import uiConfigure

from LxUi.qt import qtWidgets, qtCore


class QtViewMethod(
    uiConfigure.Basic,
    _methodBasic.LxPathMethodBasic,
    appConfig.LxUiConfig
):
    @classmethod
    def setTreeView(cls, treeBox, treeViewBuildDic, branchViewMethod=None, expandedDic=None):
        def setBranch(parentData):
            parent, parentPath = parentData
            if parentData in treeViewBuildDic:
                branchArray = treeViewBuildDic[parentData]
                for branchData in branchArray:
                    nameString, pathString = branchData
                    treeItem = qtWidgets.QtTreeviewItem()
                    treeItem.path = pathString
                    treeItem.name = nameString
                    #
                    isExistsParent = parent is not None
                    if isExistsParent:
                        parentItem = treeItemDic[parentPath]
                        parentItem.addChild(treeItem)
                        if parentPath in expandedDic:
                            isExpand = expandedDic[parentPath]
                            parentItem.setExpanded(isExpand)
                    else:
                        if hasattr(treeBox, 'addItem'):
                            treeBox.addItem(treeItem)
                        elif hasattr(treeBox, 'addChild'):
                            treeBox.addChild(treeItem)
                    #
                    treeItemDic[pathString] = treeItem
                    if isinstance(branchViewMethod, types.FunctionType) or isinstance(branchViewMethod, types.ClassType):
                        # noinspection PyCallingNonCallable
                        branchViewMethod(treeItem)
                    #
                    setBranch(branchData)
        #
        treeItemDic = {}
        #
        if not isinstance(expandedDic, dict):
            expandedDic = {}
        #
        rootData = treeViewBuildDic.keys()[0]
        if rootData:
            setBranch(rootData)
    @classmethod
    def setTreeViewListOsFile(cls, treeView, pathString):
        def branchViewMethod(*args):
            treeItem = args[0]
            osPath = treeItem.path[1:]
            osName = treeItem.name
            #
            if cls.isOsExist(osPath):
                if cls.isOsPath(osPath):
                    if ':' in osName:
                        iconKeyword = 'svg_basic@svg#server_root'
                    else:
                        iconKeyword = 'svg_basic@svg#folder'
                else:
                    iconKeyword = 'svg_basic@svg#file'
            else:
                treeItem._setQtPressStatus(qtCore.OffStatus)
                iconKeyword = 'object#unknown'
            #
            treeItem.setName(osName)
            treeItem.setIcon(iconKeyword)
        #
        pathsep = cls.OsFileSep
        #
        treeViewPathLis = cls._toTreeViewPathLis(pathString, pathsep)
        treeViewBuildDic = cls.getTreeViewBuildDic(treeViewPathLis, pathsep)
        #
        if treeViewBuildDic:
            cls.setTreeView(treeView, treeViewBuildDic, branchViewMethod)

    @classmethod
    def setTreeViewListInspection(cls, treeView, checkConfigDic, methodDic, checkObjectLis):
        def setBranch(seq, key, value):
            def setErrorObject():
                pass
            #
            enable, enExplain, chExplain = value
            treeItem = qtWidgets.QtTreeviewItem()
            treeView.addItem(treeItem)
            #
            treeItem.setName(key)
            treeItem.setNameText(u'{} ( {} )'.format(chExplain, enExplain))
            #
            if enable is True:
                iconKeyword = 'check#check'
                method = methodDic[k]
                errorDic = method(checkObjectLis)
                print errorDic
            else:
                treeItem.setPressable(False)
                iconKeyword = 'check#checkOff'
            #
            treeItem.setIcon(iconKeyword)
            # treeItem.setIcon(cls._lxMayaSvgIconKeyword('mesh'), iconWidth=20, iconHeight=20)
        #
        def setAction():
            actionDatumLis = [
                ('Extend', ),
                ('Recheck Inspection(s)', 'action#refreshMain', True),
                ('Fix Inspection(s)', 'action#fix', True)
            ]
            #
            treeView.setActionData(actionDatumLis)
        #
        treeView.setColorEnable(True)
        #
        for s, (k, v) in enumerate(checkConfigDic.items()):
            setBranch(s, k, v)
        #
        setAction()
