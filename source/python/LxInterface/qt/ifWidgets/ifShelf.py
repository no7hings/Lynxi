# coding:utf-8
from LxInterface.qt.ifBasic import ifWidgetBasic
#
from LxInterface.qt.ifWidgets import ifDevelopGroup, ifProductGroup
#
from LxInterface.qt.ifWidgets import ifGroup

#
none = ''


#
class IfProjectShelf(ifWidgetBasic.IfShelfBasic_):
    def __init__(self, mainWindow=None):
        super(IfProjectShelf, self).__init__()
        self._initShelfBasic()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            group = ifGroup.IfProjectGroup(self._mainWindow)
            self.addTab(
                group, 'Project Group', 'svg_basic@svg#project', u'Project Group （项目组件）'
            )


#
class IfPersonnelShelf(ifWidgetBasic.IfShelfBasic_):
    def __init__(self, mainWindow=None):
        super(IfPersonnelShelf, self).__init__()
        self._initShelfBasic()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            group = ifGroup.IfPersonnelGroup(self._mainWindow)
            self.addTab(
                group, 'Personnel Group', 'svg_basic@svg#personnel', u'Personnel Group （用户组件）'
            )


#
class IfProductShelf(ifWidgetBasic.IfShelfBasic_):
    def __init__(self, mainWindow=None):
        super(IfProductShelf, self).__init__()
        self._initShelfBasic()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            shelfDatumLis = [
                (ifProductGroup.IfAssetProductGroup, 'assetGroup', 'svg_basic@svg#asset', u'Asset Manager Panel ( 资产管理面板 )', True),
                (ifProductGroup.IfSceneryProductGroup, 'sceneryGroup', 'svg_basic@svg#scenery', u'Scenery Manager Panel ( 场景管理面板 )', False),
                (ifProductGroup.IfSceneProductGroup, 'sceneGroup', 'svg_basic@svg#scene', u'Scene Manager Panel ( 镜头管理面板 )', False)
            ]
            self.setTabAction(shelfDatumLis)
            #
            group = ifProductGroup.IfAssetProductGroup(self._mainWindow)
            self.addTab(
                group, 'assetGroup', 'svg_basic@svg#asset', u'Asset Product Group ( 资产生产组件 )'
            )
            #
            group = ifProductGroup.IfSceneryProductGroup(self._mainWindow)
            self.addTab(
                group, 'sceneryGroup', 'svg_basic@svg#scenery', u'Scenery Product Group ( 资产生产组件 )'
            )
            #
            group = ifProductGroup.IfSceneProductGroup(self._mainWindow)
            self.addTab(
                group, 'sceneGroup', 'svg_basic@svg#scene', u'Scene Manager Product Group ( 资产生产组件 )'
            )


#
class IfToolKitShelf(ifWidgetBasic.IfShelfBasic_):
    def __init__(self, mainWindow=None):
        super(IfToolKitShelf, self).__init__()
        self._initShelfBasic()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            group = ifGroup.IfToolkitGroup(self._mainWindow)
            self.addTab(
                group, 'Toolkit Group', 'svg_basic@svg#toolshelf', u'Toolkit Group （工具组件）'
            )


#
class IfDevelopShelf(ifWidgetBasic.IfShelfBasic_):
    def __init__(self, mainWindow=None):
        super(IfDevelopShelf, self).__init__()
        self._initShelfBasic()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            group = ifDevelopGroup.IfDevelopGroup(self._mainWindow)
            self.addTab(
                group, 'Develop Group', 'svg_basic@svg#pipeline', u'Develop Group （流程组件）'
            )
