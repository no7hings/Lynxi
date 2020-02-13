# coding:utf-8
import types

from LxBasic import bscMethods

from LxUi import uiCore

from LxUi.qt import qtWidgets, qtCore


class QtViewMethod(uiCore.UiMtdBasic):
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
            
            if bscMethods.OsPath.isExist(osPath):
                if bscMethods.OsPath.isDirectory(osPath):
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
        treeViewBuildDic = bscMethods.OsPath.treeViewBuildDic(pathString)
        #
        if treeViewBuildDic:
            cls.setTreeView(treeView, treeViewBuildDic, branchViewMethod)

    @classmethod
    def setTreeViewListInspection(cls, treeView, checkConfigDic, methodDic, checkObjectLis):
        def setBranch(key, value):
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
            setBranch(k, v)
        #
        setAction()
