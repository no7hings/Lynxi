# coding:utf-8
from LxScheme import shmOutput

from LxApp import appObjects

from LxGui import guiObjects, guiCore

from LxGui.qt import qtCore, guiQtWidgets

from .. import kitQtWgtAbs
#
from ..kitQtWidgets import ifDevelopGroup, ifProductGroup, ifGroup


class QtAppkitShelf(kitQtWgtAbs.AbsKitQtWgtShelf):
    def __init__(self, mainWindow=None):
        super(QtAppkitShelf, self).__init__()
        self._initAbsKitQtWgtShelf()
        #
        self._mainWindow = mainWindow

        self._groupWgtObjDict = {}
        #
        self._kit__appkit__set__build_()

    def _kit__appkit__set__build_(self):
        self._iconLoaderObj = guiObjects.GUI_OBJ_ICON_LOADER

        self._appkitObj = appObjects.APP_OBJ_APPKIT

        rootTagObj = self._appkitObj.tag(0)
        for mainTagObj in rootTagObj.children():
            mainTagpath = mainTagObj.path()
            # category
            if self._appkitObj.hasTools(filter=mainTagpath + u'/*'):
                mainUinameStr = mainTagObj.uiname
                if mainTagpath in self._groupWgtObjDict:
                    vShelfTabgroupWgt = self._groupWgtObjDict[mainTagpath]
                else:
                    vShelfTabgroupWgt = guiQtWidgets.QtHShelfTabgroup()
                    vShelfTabgroupWgt.chooseTab().setDatumLis(
                        [shmOutput.Scheme().toString()]
                    )
                    #
                    iconKeyStr = mainTagObj.icon
                    tooltipStr = mainTagObj.tip
                    self.addTab(vShelfTabgroupWgt, mainUinameStr, iconKeyStr, tooltipStr)

                    self._groupWgtObjDict[mainTagpath] = vShelfTabgroupWgt

                childTagObjList = mainTagObj.children()
                for subTagObj in childTagObjList:
                    subTagpath = subTagObj.path()
                    if self._appkitObj.hasTools(filter=subTagpath + u'/*'):
                        subUinameStr = subTagObj.uiname
                        if subTagpath in self._groupWgtObjDict:
                            layout = self._groupWgtObjDict[subTagpath]
                        else:
                            widget = qtCore.QWidget_()
                            subUinameStr = u'{} - {}'.format(mainUinameStr, subUinameStr)
                            iconKeyStr = subTagObj.icon
                            tooltipStr = subTagObj.tip
                            vShelfTabgroupWgt.addTab(widget, subUinameStr, iconKeyStr, tooltipStr)
                            layout = qtCore.QVBoxLayout_(widget)
                            layout.setContentsMargins(2, 2, 2, 2)

                            self._groupWgtObjDict[subTagpath] = layout
                        #
                        gridView = guiQtWidgets.QtGridview()
                        layout.addWidget(gridView)
                        gridView.setItemSize(56, 56)

                        toolObjList = self._appkitObj.tools(filter=subTagpath + u'/*')
                        for toolObj in toolObjList:
                            guiObjects.GUI_OBJ_ICON_LOADER.addIconBySourcePath(toolObj.sourcepath)

                            buttonWgtObj = guiQtWidgets.QtIconViewitem()
                            gridView.addItem(buttonWgtObj)
                            buttonWgtObj.setName(toolObj.uiname)
                            buttonWgtObj.setIcon(toolObj.icon, 40, 40, 56, 56)
                            buttonWgtObj.setTooltip(toolObj.tip)
                            buttonWgtObj.setPressCommand(toolObj.python_setup_command)
