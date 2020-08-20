# coding:utf-8
from LxBasic import bscMethods

from LxScheme import shmOutput

from LxApp import appObjects
#
from LxGui import guiObjects
#
from LxGui.qt import qtWidgets_, guiQtWidgets, qtCore
#
from .. import kitQtWgtAbs
#
serverBasicPath = shmOutput.Root().basic.server


class IfToolkitOverviewUnit(kitQtWgtAbs.AbsKitQtWgtUnit):
    UnitConnectLinks = [
    ]

    VAR_kit__qt_wgt__unit__name = 'toolkit_overview_unit'
    VAR_kit__qt_wgt__unit__uiname = 'Overview'

    VAR_kit__qt_wgt__unit__icon = 'svg_basic/toolkit'
    VAR_kit__qt_wgt__unit__tip = u'Toolkit Overview Unit ( 工具总览 )'
    #
    VAR_kit__qt_wgt__unit__side_width = 240
    def __init__(self):
        super(IfToolkitOverviewUnit, self).__init__()
        self._initAbsKitQtWgtUnit()
        #
        self._kit__unit__set_build_()

    def refreshMethod(self):
        self._kit__toolkit_overview_unit__set_build_()
        self._kit__unit__set_tag_filter_action_build_(self._treeviewWgtObj)

    def _kit__unit__set_left_build_(self, layout):
        self._treeviewWgtObj = guiQtWidgets.QtTreeview()
        layout.addWidget(self._treeviewWgtObj)
        self._treeviewWgtObj.setSelectEnable(True)
        self._treeviewWgtObj.setExpandEnable(False)
        #
        self._treeviewWgtObj.selectedChanged.connect(self._kit__toolkit_overview_unit__set_expand_refresh_)
        self._treeviewWgtObj.setKeywordFilterWidgetConnect(self.filterEnterLabel())

    def _kit__unit__set_central_build_(self, layout):
        self._groupWgtObjDict = {}
        self._treeitemWgtObjDict = {}
        self._buttonWgtObjDict = {}
        # Scroll Bar
        self._centralScrollBox = qtCore.QScrollArea_()
        layout.addWidget(self._centralScrollBox)

    def _kit__toolkit_overview_unit__set_build_(self):
        self._toolkitObj = appObjects.APP_OBJ_TOOLKIT

        rootTagObj = self._toolkitObj.tag(0)
        for mainTagObj in rootTagObj.children():
            mainTagpath = mainTagObj.path()
            # category
            if self._toolkitObj.hasTools(filter=mainTagpath + '/*'):
                if mainTagpath in self._groupWgtObjDict:
                    toolboxGroupWgtObj = self._groupWgtObjDict[mainTagpath]
                else:
                    toolboxGroupWgtObj = guiQtWidgets.QtToolboxGroup()
                    self._centralScrollBox.addWidget(toolboxGroupWgtObj)
                    toolboxGroupWgtObj.setNameString(mainTagObj.uiname)
                    # toolboxGroupWgtObj.setTooltip(mainTagObj.tip)
                    self._groupWgtObjDict[mainTagpath] = toolboxGroupWgtObj
                    #
                    self._kit__toolkit_overview_unit__set_tag_tree_create_(
                        (mainTagpath, mainTagObj.uiname),
                        self._treeviewWgtObj,
                        toolboxGroupWgtObj,
                        connectVisible=True, addToTag=True
                    )
                #
                childTagObjList = mainTagObj.children()
                for subTagObj in childTagObjList:
                    subTagpath = subTagObj.path()
                    if self._toolkitObj.hasTools(filter=subTagpath + '/*'):
                        if subTagpath in self._groupWgtObjDict:
                            toolboxWgtObj = self._groupWgtObjDict[subTagpath]
                        else:
                            toolboxWgtObj = guiQtWidgets.QtToolbox()
                            toolboxGroupWgtObj.addWidget(toolboxWgtObj)
                            toolboxWgtObj.setNameString(subTagObj.uiname)
                            self._groupWgtObjDict[subTagpath] = toolboxWgtObj
                            #
                            treeWgtObj = self._treeitemWgtObjDict[mainTagpath]
                            self._kit__toolkit_overview_unit__set_tag_tree_create_(
                                (subTagpath, subTagObj.uiname),
                                treeWgtObj,
                                toolboxWgtObj
                            )

                        toolObjList = self._toolkitObj.tools(filter=subTagpath + '/*')
                        for toolObj in toolObjList:
                            count = toolboxWgtObj.childWidgetsCount()
                            x = count
                            y = 0
                            if count % 2:
                                x = count - 1
                                y = 2
                            #
                            uinameStr = toolObj.uiname
                            toolpath = toolObj.path
                            if toolpath in self._buttonWgtObjDict:
                                _buttonWgtObj = self._buttonWgtObjDict[toolpath]
                            else:
                                buttonWgtObj = guiQtWidgets.QtPressbutton()
                                toolboxWgtObj.addWidget(buttonWgtObj, x=x, y=y)
                                buttonWgtObj.setTooltip(toolObj.tip)
                                buttonWgtObj.setName(toolpath)
                                buttonWgtObj.setNameString(toolObj.uiname)
                                buttonWgtObj.setIcon(toolObj.icon)
                                buttonWgtObj.setFilterColor(toolObj.color)
                                buttonWgtObj.setPressCommand(toolObj.python_main_command)
                                self._buttonWgtObjDict[toolpath] = buttonWgtObj
                                #
                                treeWgtObj = self._treeitemWgtObjDict[subTagpath]

                                self._kit__toolkit_overview_unit__set_tag_tree_create_(
                                    (toolpath, uinameStr),
                                    treeWgtObj,
                                    buttonWgtObj,
                                    icon=toolObj.icon
                                )

                                self._kit__toolkit_overview_unit_cls__set_action_create_(buttonWgtObj, toolObj)

    def _kit__toolkit_overview_unit__set_tag_tree_create_(self, nameArgs, treeWgtObj, groupWgtObj, icon=None, connectVisible=False, addToTag=False):
        pathStr, uinameStr = nameArgs
        # tag filter
        tagItem = guiQtWidgets.QtTreeItem()
        if isinstance(treeWgtObj, guiQtWidgets.QtTreeview):
            treeWgtObj.addItem(tagItem)
        elif isinstance(treeWgtObj, guiQtWidgets.QtTreeItem):
            treeWgtObj.addChild(tagItem)
        #
        tagItem.setName(pathStr)
        tagItem.setNameString(uinameStr)
        if icon is not None:
            tagItem.setIcon(icon)
        else:
            tagItem.setIcon('svg_basic/tag')
        if connectVisible is True:
            tagItem.visibleToggled.connect(groupWgtObj.setVisible)
        #
        self._treeitemWgtObjDict[pathStr] = tagItem
        #
        if addToTag is True:
            tag = pathStr
            if tag not in self._tagLis:
                self._tagLis.append(tag)
            if tag not in self._tagFilterEnableDic:
                self._tagFilterEnableDic[tag] = True

            itemIndex = self._treeviewWgtObj.itemIndex(tagItem)
            self._tagFilterIndexDic.setdefault(tag, []).append(itemIndex)

    @staticmethod
    def _kit__toolkit_overview_unit_cls__set_action_create_(widget, toolObj):
        def setSourceFolderOpenFnc_():
            bscMethods.OsDirectory.open(toolObj.sourcepath)

        def getSourceFolderEnableFnc_():
            return bscMethods.OsDirectory.isExist(toolObj.sourcepath)

        def setMainFileOpenFnc_():
            osCmdExe = 'sublime_text.exe'
            osCmd = '''"{}" "{}"'''.format(osCmdExe, toolObj.python_main_filepath)
            bscMethods.OsPlatform.runCommand(osCmd)

        def getMainFileOpenEnableFnc_():
            return bscMethods.OsFile.isExist(toolObj.python_main_filepath)

        actions = [
            ('Basic', ),
            ('Open Source Folder', 'svg_basic/folder', getSourceFolderEnableFnc_, setSourceFolderOpenFnc_),
            ('Open Main File', 'svg_basic/fileOpen', getMainFileOpenEnableFnc_, setMainFileOpenFnc_)
        ]
        widget.setActionData(actions)

    def _kit__toolkit_overview_unit__set_expand_refresh_(self):
        itemModels = self._treeviewWgtObj.itemModels()
        for itemModel in itemModels:
            key = itemModel.name()
            if key in self._groupWgtObjDict:
                groupWgtObj = self._groupWgtObjDict[key]
                groupWgtObj.setExpanded(
                    itemModel.isSelected() or itemModel.isSubSelected()
                )
    #
    def _kit__unit__set_build_(self):
        widget = qtCore.QWidget_()
        layout = qtCore.QHBoxLayout_(widget)
        self.mainLayout().addWidget(widget)
        #
        leftExpandWidget = qtWidgets_.QtExpandWidget()
        layout.addWidget(leftExpandWidget)
        leftExpandWidget.setExpanded(False)
        leftExpandWidget.setUiWidth(self.VAR_kit__qt_wgt__unit__side_width)
        #
        leftWidget = qtCore.QWidget_()
        leftExpandWidget.addWidget(leftWidget)
        leftLayout = qtCore.QVBoxLayout_(leftWidget)
        self._kit__unit__set_left_build_(leftLayout)
        #
        centralWidget = qtCore.QWidget_()
        layout.addWidget(centralWidget)
        centralLayout = qtCore.QVBoxLayout_(centralWidget)
        self._kit__unit__set_central_build_(centralLayout)