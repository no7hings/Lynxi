# coding:utf-8
from .. import kitQtWgtAbs
#
from ..kitQtWidgets import ifDevelopGroup, ifProductGroup, ifGroup

#
none = ''


#
class QtIf_ProjectShelf(kitQtWgtAbs.AbsKitQtWgtShelf):
    def __init__(self, mainWindow=None):
        super(QtIf_ProjectShelf, self).__init__()
        self._initAbsKitQtWgtShelf()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            _groupWgtObj = ifGroup.QtIf_ProjectGroup(self._mainWindow)
            self.addTab(
                _groupWgtObj, 'Project Group', 'svg_basic/project', u'Project Group （项目组件）'
            )


#
class IfPersonnelShelf(kitQtWgtAbs.AbsKitQtWgtShelf):
    def __init__(self, mainWindow=None):
        super(IfPersonnelShelf, self).__init__()
        self._initAbsKitQtWgtShelf()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            _groupWgtObj = ifGroup.IfPersonnelGroup(self._mainWindow)
            self.addTab(
                _groupWgtObj, 'Personnel Group', 'svg_basic/personnel', u'Personnel Group （用户组件）'
            )


#
class IfProductShelf(kitQtWgtAbs.AbsKitQtWgtShelf):
    def __init__(self, mainWindow=None):
        super(IfProductShelf, self).__init__()
        self._initAbsKitQtWgtShelf()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            shelfDatumLis = [
                (ifProductGroup.IfAssetProductGroup, 'assetGroup', 'svg_basic/asset', u'Asset Manager Panel ( 资产管理面板 )', True),
                (ifProductGroup.IfSceneryProductGroup, 'sceneryGroup', 'svg_basic/scenery', u'Scenery Manager Panel ( 场景管理面板 )', False),
                (ifProductGroup.IfSceneProductGroup, 'sceneGroup', 'svg_basic/scene', u'Scene Manager Panel ( 镜头管理面板 )', False)
            ]
            self.setTabAction(shelfDatumLis)
            #
            _groupWgtObj = ifProductGroup.IfAssetProductGroup(self._mainWindow)
            self.addTab(
                _groupWgtObj, 'assetGroup', 'svg_basic/asset', u'Asset Product Group ( 资产生产组件 )'
            )
            #
            _groupWgtObj = ifProductGroup.IfSceneryProductGroup(self._mainWindow)
            self.addTab(
                _groupWgtObj, 'sceneryGroup', 'svg_basic/scenery', u'Scenery Product Group ( 资产生产组件 )'
            )
            #
            _groupWgtObj = ifProductGroup.IfSceneProductGroup(self._mainWindow)
            self.addTab(
                _groupWgtObj, 'sceneGroup', 'svg_basic/scene', u'Scene Manager Product Group ( 资产生产组件 )'
            )


#
class IfToolKitShelf(kitQtWgtAbs.AbsKitQtWgtShelf):
    def __init__(self, mainWindow=None):
        super(IfToolKitShelf, self).__init__()
        self._initAbsKitQtWgtShelf()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            _groupWgtObj = ifGroup.IfToolkitGroup(self._mainWindow)
            self.addTab(
                _groupWgtObj,
                _groupWgtObj.VAR_kit__qt_wgt__group__uiname,
                _groupWgtObj.VAR_kit__qt_wgt__group__icon,
                _groupWgtObj.VAR_kit__qt_wgt__group__tip
            )


#
class IfDevelopShelf(kitQtWgtAbs.AbsKitQtWgtShelf):
    def __init__(self, mainWindow=None):
        super(IfDevelopShelf, self).__init__()
        self._initAbsKitQtWgtShelf()
        #
        self._mainWindow = mainWindow
        #
        self.setupShelf()
    #
    def setupShelf(self):
        if self._mainWindow is not None:
            _groupWgtObj = ifDevelopGroup.IfDevelopGroup(self._mainWindow)
            self.addTab(
                _groupWgtObj, 'Develop Group', 'svg_basic/pipeline', u'Develop Group （流程组件）'
            )
