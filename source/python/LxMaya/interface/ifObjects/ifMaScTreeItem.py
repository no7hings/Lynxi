# coding:utf-8
import types
#
from LxCore import lxBasic, lxConfigure
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr, scenePr
#
from LxUi.command import uiHtml
#
from LxUi.qt import uiWidgets_, uiWidgets
#
#
from LxDatabase import dbGet
#
from LxMaya.command import maUtils, maAttr, maFur, maAbc
#
from LxMaya.product import maScLoadCmds
#
from LxMaya.product.op import sceneOp
#
from LxMaya.database import maDbAstCmds


#
class IfScObjectAbs(object):
    _tip0 = u'{0} 未载入：\n1，在右击菜单点击“Reload / Load {0} ( Active )”加载。'
    _tip1 = u'{0} 不存在于镜头场景：\n1，如果资源是“Cache”，可能“Cache”无动画数据，可忽略，或者联系制片。'
    _tip2 = u'{0} 有更新：\n1，在右击菜单点击“Reload / Load {0} ( Active )”更新。'
    _tip3 = u'{0} 不存在于服务器：\n1，可忽略，或者联系制片。'
    _tip4 = u'{0} 操作已经禁用：\n1，请先更新上层“Tree Item”。'


#
class _IfScCameraItemBasic(uiWidgets_.QTreeWidgetItem_, IfScObjectAbs):
    def _initItemBasic(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        branchInfo, connectMethod, subLabel,
    ):
        self._projectName = projectName
        #
        self._sceneIndex, self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage = sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage
        #
        self._startFrame, self._endFrame = startFrame, endFrame
        self._localStartFrame, self._localEndFrame = None, None
        #
        self._itemWidget = None
        self._itemTooltip = None
        self._itemLocalTimeTag = None
        self._itemServerTimeTag = None
        #
        self._itemIconState0 = None
        self._itemIcon1 = 'svg_basic@svg#local'
        self._itemIconState1 = None
        self._itemText1 = None
        self._itemIcon2 = 'svg_basic@svg#server'
        self._itemIconState2 = None
        self._itemText2 = None
        self._itemIcon3 = 'svg_basic@svg#time'
        self._itemIconState3 = None
        self._itemText3 = None
        #
        self._path = None
        self._namespace = None
        #
        self._vars = None
        #
        self._branchInfo = branchInfo
        #
        if isinstance(connectMethod, types.FunctionType) or isinstance(connectMethod, types.MethodType):
            self._connectMethod = connectMethod
        else:
            self._connectMethod = None
        #
        self._subLabel = subLabel
        #
        if parentItem is not None:
            self._parentItem = parentItem
            if hasattr(self._parentItem, 'localTimeTag'):
                if self._parentItem.localTimeTag is not None:
                    self.setupItem()
            else:
                self.setupItem()
    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, string):
        self._path = string
    @property
    def namespace(self):
        return self._namespace
    @namespace.setter
    def namespace(self, string):
        self._namespace = string
    @property
    def serverTimeTag(self):
        return self._itemServerTimeTag
    @serverTimeTag.setter
    def serverTimeTag(self, string):
        self._itemServerTimeTag = string
    @property
    def localTimeTag(self):
        return self._itemLocalTimeTag
    @localTimeTag.setter
    def localTimeTag(self, string):
        self._itemLocalTimeTag = string
    @property
    def vars(self):
        return self._vars
    @vars.setter
    def vars(self, tup):
        self._vars = tup
    #
    def _updateItemAction(self):
        pass
    #
    def _updateItemWidget(self):
        self._itemWidget = self.setItemIconWidget(
            0,
            self._itemIcon0,
            u'{}'.format(self._itemText0, self._subLabel),
            self._itemIconState0
        )
        self._updateItemAction()
        #
        self.setText(2, lxBasic.translateRecordViewTime(self._itemLocalTimeTag))
        self.setItemIcon_(2, self._itemIcon1, self._itemIconState1)
        #
        self._itemWidget.setTooltip(self._itemTooltip)
        #
        self._refreshItemLocalState()
        self._refreshItemLocalFrameState()
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = None
    #
    def _updateLocalFrameRange(self):
        if self._objectType == appCfg.MaNodeType_Alembic:
            self._localStartFrame, self._localEndFrame = maAbc.getAlembicNodeFrameRange(self._path)
    #
    def _refreshItemLocalState(self):
        self._itemIconState1 = 'off' if self._itemLocalTimeTag is None else None
        #
        self.setText(2, lxBasic.translateRecordViewTime(self._itemLocalTimeTag))
        self.setItemIcon_(2, self._itemIcon1, self._itemIconState1)
    #
    def _refreshItemServerState(self):
        self._itemIconState2 = 'off' if self._itemServerTimeTag is None else None
        #
        self.setText(3, lxBasic.translateRecordViewTime(self._itemServerTimeTag))
        self.setItemIcon_(3, self._itemIcon2, self._itemIconState2)
    #
    def _refreshItemLocalFrameState(self):
        if self._localStartFrame is not None and self._localEndFrame is not None:
            self.setText(1, '{} - {}'.format(self._localStartFrame, self._localEndFrame))
            self.setItemIcon_(1, self._itemIcon3, self._itemIconState3)
    #
    def _refreshItemState(self, timeTag=None):
        if timeTag is not None:
            self._itemLocalTimeTag = timeTag
        else:
            self._itemLocalTimeTag = self._itemServerTimeTag
        #
        if self._itemLocalTimeTag == self._itemServerTimeTag:
            self._itemTooltip = None
            state = None
        else:
            state = 'warning'
        #
        self._itemIconState0 = state
        #
        self._updateItemWidget()
    #
    def _refreshChildItemsState(self):
        pass
    #
    def _refreshVars(self):
        self._vars = (
            self._projectName,
            self._sceneIndex,
            self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
            self._startFrame, self._endFrame,
            self._subLabel
        )
    #
    def setupItem(self):
        self._updateServerTimeTag()
        self._refreshItemServerState()
        if self._branchInfo is not None:
            self._parentItem.addChild(self)
            #
            expandEnable = False
            if self._branchInfo is not False:
                nodePath, namespace, timeTag = self._branchInfo
                #
                self._path = nodePath
                self._namespace = namespace
                self._itemLocalTimeTag = timeTag
                #
                self._objectType = maUtils.getShapeType(self._path)
                #
                self._updateLocalFrameRange()
                #
                if self._itemServerTimeTag is not None:
                    if self._itemLocalTimeTag is None:
                        self._itemTooltip = self._tip0.format(self._itemText0)
                        self._itemIconState0 = 'error'
                        #
                        expandEnable = True
                    elif self._itemLocalTimeTag is False:
                        self._itemIconState0 = 'off'
                        self._itemTooltip = self._tip1.format(self._itemText0)
                        #
                        expandEnable = True
                    else:
                        if not self._itemServerTimeTag == self._itemLocalTimeTag:
                            self._itemIconState0 = 'warning'
                            #
                            self._itemTooltip = self._tip2.format(self._itemText0)
                            #
                            expandEnable = True
                        else:
                            self._itemIconState0 = None
                            self._itemTooltip = None
                else:
                    self._itemIconState0 = 'wait'
                    self._itemTooltip = self._tip3.format(self._itemText0)
                    #
                    expandEnable = True
            else:
                self._itemTooltip = self._tip0.format(self._itemText0)
                self._itemIconState0 = 'error'
                #
                expandEnable = True
            #
            if expandEnable is True:
                parentItemLis = self.parentItems()
                if parentItemLis:
                    [i.setExpanded(True) for i in parentItemLis]
            #
            self._updateItemWidget()
            self._refreshVars()


#
class IfScCameraCacheItem(_IfScCameraItemBasic):
    def __init__(
            self,
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            branchInfo, connectMethod, subLabel
    ):
        self._overrideAttr()
        #
        self.clsSuper = super(IfScCameraCacheItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            branchInfo, connectMethod, subLabel
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic@svg#cache'
        self._itemText0 = u'Camera Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                logWin = None
                #
                maScLoadCmds.scUnitCameraCacheLoadSubCmd(
                    logWin,
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                    self._subLabel,
                    cacheFile
                )
                #
                self._refreshItemState(currentTimeTag)
                #
                if self._connectMethod:
                    self._connectMethod()
            #
            currentTimeTag = lxBasic.getOsFileTimeTag(cacheFile)
            if not currentTimeTag == '0000_0000_0000':
                actionExplain = lxBasic.translateRecordViewTime(currentTimeTag)
                #
                iconKeyword = 'link#%s' % stage
                #
                iconExplain = iconKeyword, 'svg_basic@svg#load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeyword, 'state@svg#active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            logWin = None
            #
            maScLoadCmds.scUnitCameraCacheLoadSubCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._subLabel,
                withCameraCache=True
            )
            #
            self._refreshItemState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def showCacheManagerWindowCmd():
            from LxInterface.qt.ifWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                lxConfigure.LynxiScAstModelCacheType,
                (
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant,
                    self._startFrame, self._endFrame,
                    self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant
                )
            )
            w.setListCache()
            w.windowShow()
        #
        osFileDic = scenePr.getScCameraCacheDic(
            self._projectName,
            self._sceneName, self._sceneVariant,
            self._subLabel
        )
        #
        actionDatumLis = []
        for seq, (cacheSceneStage, cacheFileLis) in enumerate(osFileDic.items()):
            actionDatumLis.append(
                (lxBasic._toStringPrettify(scenePr.getSceneLink(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic@svg#subWindow', True, showCacheManagerWindowCmd)
            ]
        )
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = scenePr.getScCameraCacheActiveTimeTag(
            self._projectName,
            self._sceneName, self._sceneVariant
        )


# Asset
class IfScAssetUnitItem(uiWidgets_.QTreeWidgetItem_, IfScObjectAbs):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        connectMethod
    ):
        self.clsSuper = super(IfScAssetUnitItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            connectMethod
        )
    def _initItemBasic(
            self,
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            connectMethod
    ):
        self._projectName = projectName
        #
        self._sceneIndex, self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage = sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage
        #
        self._startFrame, self._endFrame = startFrame, endFrame
        self._localStartFrame, self._localEndFrame = None, None
        #
        self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant = assetIndex, assetClass, assetName, number, assetVariant
        #
        self._vars = None
        #
        self._connectMethod = connectMethod
        #
        self._itemWidget = None
        self._itemTooltip = None
        self._itemLocalTimeTag = None
        self._itemServerTimeTag = None
        #
        self._itemIcon0 = 'svg_basic@svg#package_object'
        self._itemIconState0 = None
        self._itemText0 = assetPr.getAssetViewInfo(
            assetIndex, assetClass
        )
        self._itemIcon1 = 'svg_basic@svg#name'
        self._itemIconState1 = None
        self._itemText1 = u'{} - {} ( {} )'.format(assetName, number, assetVariant)
        #
        if parentItem is not None:
            self._parentItem = parentItem
            self.setupItem()
    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, string):
        self._path = string
    @property
    def namespace(self):
        return self._namespace
    @namespace.setter
    def namespace(self, string):
        self._namespace = string
    @property
    def serverTimeTag(self):
        return self._itemServerTimeTag
    @serverTimeTag.setter
    def serverTimeTag(self, string):
        self._itemServerTimeTag = string
    @property
    def localTimeTag(self):
        return self._itemLocalTimeTag
    @localTimeTag.setter
    def localTimeTag(self, string):
        self._itemLocalTimeTag = string
    @property
    def vars(self):
        return self._vars
    #
    def _refreshChildItemsState(self):
        childItemLis = self.childItems()
        if childItemLis:
            for i in childItemLis:
                i._itemIconState0 = None
                i._itemLocalTimeTag = i._itemServerTimeTag
                i._updateItemWidget()
    #
    def _updateItemAction(self):
        def assetLoadActiveCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAssetLoadSubCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant,
                withAstModel=True, withModelCache=True,
                withAstCfx=True, withAstCfxFurCache=True,
                withExtraCache=True
            )
            #
            self._updateItemWidget()
            #
            self._refreshChildItemsState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        isLoadEnable = self._itemLocalTimeTag is None
        #
        actionDatumLis = [
            (u'Basic Action(s)',),
            (u'Reload / Load {} ( Active )'.format('Asset'), 'svg_basic@svg#timeRefresh', isLoadEnable, assetLoadActiveCmd)
        ]
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateItemWidget(self):
        scAssetGroup = scenePr.scAstRootGroupName(
            self._sceneName, self._sceneVariant,
            self._assetName, self._number
        )
        if maUtils.isAppExist(scAssetGroup):
            self._path = scAssetGroup
            #
            self._itemLocalTimeTag = maUtils.getAttrDatum(self._path, 'tag')
            #
            self._itemIconState0 = None
            self._itemTooltip = None
        else:
            self._itemIconState0 = 'error'
            self._itemTooltip = self._tip0.format('Asset')
        #
        self._itemWidget = self.setItemIconWidget(
            0,
            self._itemIcon0,
            u'{}'.format(self._itemText0),
            self._itemIconState0
        )
        self._updateItemAction()
        #
        self._itemWidget.setTooltip(self._itemTooltip)
        #
        self.setText(1, self._itemText1)
        self.setItemIcon(1, self._itemIcon1, self._itemIconState1)
    #
    def _refreshVars(self):
        self._vars = (
            self._projectName,
            self._sceneIndex,
            self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
            self._startFrame, self._endFrame,
            self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant
        )
    #
    def setupItem(self):
        self._parentItem.addChild(self)
        #
        self._updateItemWidget()
        self._refreshVars()


#
class IfScAstBranchItemBasic(uiWidgets_.QTreeWidgetItem_, IfScObjectAbs):
    def _initItemBasic(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        branchInfo, connectMethod, objectLabel=None
    ):
        self._projectName = projectName
        #
        self._sceneIndex, self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage = sceneIndex, sceneClass, sceneName, sceneVariant, sceneStage
        #
        self._startFrame, self._endFrame = startFrame, endFrame
        self._localStartFrame, self._localEndFrame = None, None
        #
        self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant = assetIndex, assetClass, assetName, number, assetVariant
        #
        self._itemWidget = None
        self._itemTooltip = None
        self._itemLocalTimeTag = None
        self._itemServerTimeTag = None
        #
        self._itemIconState0 = None
        self._itemIcon1 = 'svg_basic@svg#local'
        self._itemIconState1 = None
        self._itemText1 = None
        self._itemIcon2 = 'svg_basic@svg#server'
        self._itemIconState2 = None
        self._itemText2 = None
        self._itemIcon3 = 'svg_basic@svg#time'
        self._itemIconState3 = None
        self._itemText3 = None
        #
        self._path = None
        self._namespace = None
        #
        self._vars = None
        #
        self._branchInfo = branchInfo
        if isinstance(connectMethod, types.FunctionType) or isinstance(connectMethod, types.MethodType):
            self._connectMethod = connectMethod
        else:
            self._connectMethod = None
        #
        if objectLabel is not None:
            self._objectLabel = objectLabel
        else:
            self._objectLabel = None
        #
        if parentItem is not None:
            self._parentItem = parentItem
            self.setupItem()
    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, string):
        self._path = string
    @property
    def namespace(self):
        return self._namespace
    @namespace.setter
    def namespace(self, string):
        self._namespace = string
    @property
    def serverTimeTag(self):
        return self._itemServerTimeTag
    @serverTimeTag.setter
    def serverTimeTag(self, string):
        self._itemServerTimeTag = string
    @property
    def localTimeTag(self):
        return self._itemLocalTimeTag
    @localTimeTag.setter
    def localTimeTag(self, string):
        self._itemLocalTimeTag = string
    @property
    def vars(self):
        return self._vars
    @vars.setter
    def vars(self, tup):
        self._vars = tup
    #
    def _updateItemAction(self):
        pass
    #
    def _updateItemWidget(self):
        if self._objectLabel is not None:
            text0 = self._objectLabel
        else:
            text0 = self._itemText0
        #
        isEnable = self._isItemEnable()
        #
        if isEnable is False:
            self._itemIconState0 = 'disable'
            self._itemTooltip = self._tip4.format(self._itemText0)
        #
        self._itemWidget = self.setItemIconWidget(
            0,
            self._itemIcon0,
            u'{}'.format(text0),
            self._itemIconState0
        )
        #
        if self._isItemEnable():
            self._updateItemAction()
        #
        self._itemWidget.setTooltip(self._itemTooltip)
        #
        self._refreshItemLocalState()
        self._refreshItemLocalFrameState()
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = None
    #
    def _updateLocalFrameRange(self):
        if self._objectType == appCfg.MaNodeType_Alembic:
            self._localStartFrame, self._localEndFrame = maAbc.getAlembicNodeFrameRange(self._path)
        elif self._objectType == appCfg.MaNodeType_Plug_Yeti:
            self._localStartFrame, self._localEndFrame = maFur.getYetiCacheFrameRange(self._path)
        elif self._objectType == appCfg.MaNodeType_Plug_NurbsHair:
            self._localStartFrame, self._localEndFrame = maFur.getNhrCacheFrameRange(self._path)
    #
    def _refreshItemLocalState(self):
        self._itemIconState1 = 'off' if self._itemLocalTimeTag is None else None
        #
        self.setText(2, lxBasic.translateRecordViewTime(self._itemLocalTimeTag))
        self.setItemIcon_(2, self._itemIcon1, self._itemIconState1)
    #
    def _refreshItemServerState(self):
        self._itemIconState2 = 'off' if self._itemServerTimeTag is None else None
        #
        self.setText(3, lxBasic.translateRecordViewTime(self._itemServerTimeTag))
        self.setItemIcon_(3, self._itemIcon2, self._itemIconState2)
    #
    def _refreshItemLocalFrameState(self):
        if self._localStartFrame is not None and self._localEndFrame is not None:
            self.setText(1, '{} - {}'.format(self._localStartFrame, self._localEndFrame))
            self.setItemIcon_(1, self._itemIcon3, self._itemIconState3)
    #
    def _refreshItemState(self, timeTag=None):
        if timeTag is not None:
            self._itemLocalTimeTag = timeTag
        else:
            self._itemLocalTimeTag = self._itemServerTimeTag
        #
        if self._itemLocalTimeTag == self._itemServerTimeTag:
            self._itemTooltip = None
            state = None
        else:
            state = 'warning'
        #
        self._itemIconState0 = state
        #
        self._updateItemWidget()
    #
    def _refreshChildItemsState(self):
        childItemLis = self.childItems()
        if childItemLis:
            for i in childItemLis:
                i._itemIconState0 = None
                i._itemLocalTimeTag = i._itemServerTimeTag
                i._updateItemWidget()
    #
    def _refreshVars(self):
        self._vars = (
            self._projectName,
            self._sceneIndex,
            self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
            self._startFrame, self._endFrame,
            self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant
        )
    #
    def _isItemEnable(self):
        if hasattr(self._parentItem, 'localTimeTag'):
            return self._parentItem.localTimeTag is not None
        else:
            return True
    #
    def setupItem(self):
        self._updateServerTimeTag()
        self._refreshItemServerState()
        if self._branchInfo is not None:
            self._parentItem.addChild(self)
            #
            expandEnable = False
            if self._branchInfo is not False:
                nodePath, namespace, timeTag = self._branchInfo
                #
                self._path = nodePath
                self._namespace = namespace
                self._itemLocalTimeTag = timeTag
                #
                self._objectType = maUtils.getShapeType(self._path)
                #
                self._updateLocalFrameRange()
                #
                if self._itemServerTimeTag is not None:
                    if self._itemLocalTimeTag is None:
                        self._itemTooltip = self._tip0.format(self._itemText0)
                        self._itemIconState0 = 'error'
                        #
                        expandEnable = True
                    elif self._itemLocalTimeTag is False:
                        self._itemIconState0 = 'off'
                        self._itemTooltip = self._tip1.format(self._itemText0)
                        #
                        expandEnable = True
                    else:
                        if not self._itemServerTimeTag == self._itemLocalTimeTag:
                            self._itemIconState0 = 'warning'
                            #
                            self._itemTooltip = self._tip2.format(self._itemText0)
                            #
                            expandEnable = True
                        else:
                            self._itemIconState0 = None
                            self._itemTooltip = None
                else:
                    self._itemIconState0 = 'wait'
                    self._itemTooltip = self._tip3.format(self._itemText0)
                    #
                    expandEnable = True
            else:
                self._itemTooltip = self._tip0.format(self._itemText0)
                self._itemIconState0 = 'error'
                #
                expandEnable = True
            #
            if expandEnable is True:
                parentItemLis = self.parentItems()
                if parentItemLis:
                    [i.setExpanded(True) for i in parentItemLis]
            #
            self._updateItemWidget()
            self._refreshVars()


#
class IfScAstModelProductItem(IfScAstBranchItemBasic):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self.clsSuper = super(IfScAstModelProductItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic@svg#caches'
        self._itemText0 = u'Model'
    #
    def _updateItemAction(self):
        def productLoadActiveCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAstModelProductLoadCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withAstModel=True, withModelCache=True
            )
            #
            scAstModelNamespace = scenePr.scAstModelNamespace(self._sceneName, self._sceneVariant, self._assetName, self._number)
            scAstCfxNamespace = scenePr.scAstCfxNamespace(self._sceneName, self._sceneVariant, self._assetName, self._number)
            #
            maFur.setScAstCfxGrowSourceConnectToModel(
                self._assetName, scAstModelNamespace, scAstCfxNamespace
            )
            #
            self._refreshItemState()
            self._refreshChildItemsState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def cacheLoadActiveCmd():
            logWin = None
            # Model Cache
            maScLoadCmds.scUnitAstModelCacheConnectCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withModelCache=True
            )
            #
            self._refreshChildItemsState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def connectionRefreshCmd():
            pass
        #
        def objectAttributeRefreshCmd():
            assetIndex = self._assetIndex
            assetVariant = self._assetVariant
            assetSubIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
            compObjectIndexes = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
            maDbAstCmds.dbAstMaterialCompObjectAttrsLoadCmd(assetSubIndex, compObjectIndexes)
        #
        def objectSetRefreshCmd():
            assetIndex = self._assetIndex
            assetVariant = self._assetVariant
            assetSubIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
            compObjectIndexes = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
            maDbAstCmds.dbAstMaterialCompObjectSetsLoadCmd(assetSubIndex, compObjectIndexes)
        #
        def displayRefreshCmd():
            scAstModelNamespace = scenePr.scAstModelNamespace(
                self._sceneName, self._sceneVariant,
                self._assetName, self._number
            )
            scAstModelDisplayLayer = scenePr.scAstModelDisplayLayer(
                self._sceneName, self._sceneVariant,
                self._assetName, self._number
            )
            sceneOp.setScAstModelDisplayLayer(
                self._assetName, scAstModelNamespace, scAstModelDisplayLayer
            )
        #
        def connectionWindowShowCmd():
            tipWin = uiWidgets.UiTipWindow()
            tipWin.setNameText(u'{} Connection'.format(self._itemText0))
            #
            connections = maAttr.getConnectionFilterByNamespace(self._namespace)
            if connections:
                for i in connections:
                    sourceAttr, targetAttr = i
                    html = uiHtml.getHtmlConnection(sourceAttr, targetAttr, self._namespace)
                    tipWin.addHtml(html)
            #
            tipWin.uiShow()
        #
        actionDatumLis = [
            (u'Basic Action(s)',),
            (u'Reload / Load {} Product'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, productLoadActiveCmd),
            (u'Reload / Load {} Cache(s)'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, cacheLoadActiveCmd),
            (u'Extend Action(s)',),
            (u'Refresh Connection(s)', 'svg_basic@svg#refresh', False, connectionRefreshCmd),
            (u'Refresh Display', 'svg_basic@svg#refresh', True, displayRefreshCmd),
            (u'Database Action(s)', ),
            (u'Refresh Object Attribute(s)', 'svg_basic@svg#refresh', True, objectAttributeRefreshCmd),
            (u'Refresh Object Set(s)', 'svg_basic@svg#refresh', True, objectSetRefreshCmd),
            (u'Window',),
            (u'Show {} Connection'.format(self._itemText0), 'svg_basic@svg#subWindow', True,
             connectionWindowShowCmd)
        ]
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = assetPr.getAstUnitProductActiveTimeTag(
            self._projectName,
            self._assetClass, self._assetName, self._assetVariant, lxConfigure.LynxiProduct_Asset_Link_Model
        )


#
class IfScAstModelCacheItem(IfScAstBranchItemBasic):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self.clsSuper = super(IfScAstModelCacheItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic@svg#cache'
        self._itemText0 = u'Model Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                logWin = None
                #
                maScLoadCmds.scUnitAstModelCacheConnectCmd(
                    logWin,
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                    self._startFrame, self._endFrame,
                    self._assetIndex,
                    self._assetClass, self._assetName, self._number, self._assetVariant,
                    withModelCache=cacheFile
                )
                #
                self._refreshItemState(currentTimeTag)
                #
                if self._connectMethod:
                    self._connectMethod()
            #
            currentTimeTag = lxBasic.getOsFileTimeTag(cacheFile)
            if not currentTimeTag == '0000_0000_0000':
                actionExplain = lxBasic.translateRecordViewTime(currentTimeTag)
                #
                iconKeyword = 'link#%s' % stage
                #
                iconExplain = iconKeyword, 'svg_basic@svg#load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeyword, 'state@svg#active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAstModelCacheConnectCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withModelCache=True
            )
            #
            self._refreshItemState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def showCacheManagerWindowCmd():
            from LxInterface.qt.ifWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                lxConfigure.LynxiScAstModelCacheType,
                (
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant,
                    self._startFrame, self._endFrame,
                    self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant
                )
            )
            w.setListCache()
            w.windowShow()
        #
        osFileDic = scenePr.getScAstModelCacheDic(
            self._projectName,
            self._sceneName, self._sceneVariant,
            self._assetName, self._number
        )
        #
        actionDatumLis = []
        for seq, (cacheSceneStage, cacheFileLis) in enumerate(osFileDic.items()):
            actionDatumLis.append(
                (lxBasic._toStringPrettify(scenePr.getSceneLink(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic@svg#subWindow', True, showCacheManagerWindowCmd)
            ]
        )
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = scenePr.getScAstModelCacheActiveTimeTag(
                self._projectName,
                self._sceneName, self._sceneVariant,
                self._assetName, self._number
            )


# Extra Cache
class IfScAstExtraCacheItem(IfScAstBranchItemBasic):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self.clsSuper = super(IfScAstExtraCacheItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic@svg#cache'
        self._itemText0 = u'Extra Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                logWin = None
                #
                maScLoadCmds.scUnitAstExtraCacheConnectCmd(
                    logWin,
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                    self._startFrame, self._endFrame,
                    self._assetIndex,
                    self._assetClass, self._assetName, self._number, self._assetVariant,
                    withAstRigExtraCache=cacheFile
                )
                #
                self._refreshItemState(currentTimeTag)
                #
                if self._connectMethod:
                    self._connectMethod()
            #
            currentTimeTag = lxBasic.getOsFileTimeTag(cacheFile)
            if not currentTimeTag == '0000_0000_0000':
                actionExplain = lxBasic.translateRecordViewTime(currentTimeTag)
                #
                iconKeyword = 'link#%s' % stage
                #
                iconExplain = iconKeyword, 'svg_basic@svg#load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeyword, 'state@svg#active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAstExtraCacheConnectCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withAstRigExtraCache=True
            )
            #
            self._refreshItemState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def showCacheManagerWindowCmd():
            from LxInterface.qt.ifWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                lxConfigure.LynxiScAstExtraCacheType,
                (
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant,
                    self._startFrame, self._endFrame,
                    self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant
                )
            )
            w.setListCache()
            w.windowShow()
        #
        osFileDic = scenePr.getScAstExtraCacheDic(
            self._projectName,
            self._sceneName, self._sceneVariant,
            self._assetName, self._number
        )
        #
        actionDatumLis = []
        for seq, (cacheSceneStage, cacheFileLis) in enumerate(osFileDic.items()):
            actionDatumLis.append(
                (lxBasic._toStringPrettify(scenePr.getSceneLink(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic@svg#subWindow', True, showCacheManagerWindowCmd)
            ]
        )
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = scenePr.getScAstRigExtraCacheActiveTimeTag(
                self._projectName,
                self._sceneName, self._sceneVariant,
                self._assetName, self._number
            )


# CFX Product
class IfScAstCfxProductItem(IfScAstBranchItemBasic):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self.clsSuper = super(IfScAstCfxProductItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic@svg#caches'
        self._itemText0 = u'Groom'
    #
    def _updateItemAction(self):
        def productLoadActiveCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAstCfxProductLoadCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withAstCfxFurCache=True
            )
            #
            self._refreshItemState()
            self._refreshChildItemsState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def cacheLoadActiveCmd():
            logWin = None
            # Cfx Fur Cache
            maScLoadCmds.scUnitAstCfxFurCachesConnectCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withAstCfxFurCache=True
            )
            #
            self._refreshChildItemsState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def connectionRefreshCmd():
            scAstModelNamespace = scenePr.scAstModelNamespace(self._sceneName, self._sceneVariant, self._assetName, self._number)
            scAstCfxNamespace = scenePr.scAstCfxNamespace(self._sceneName, self._sceneVariant, self._assetName, self._number)
            #
            maFur.setScAstCfxGrowSourceConnectToModel(
                self._assetName, scAstModelNamespace, scAstCfxNamespace
            )
        #
        def displayRefreshCmd():
            scAstCfxNamespace = scenePr.scAstCfxNamespace(self._sceneName, self._sceneVariant, self._assetName, self._number)
            scAstCfxDisplayLayer = scenePr.scAstCfxDisplayLayer(self._sceneName, self._sceneVariant, self._assetName, self._number)
            #
            maFur.setScAstCfxDisplayLayer(
                self._assetName, scAstCfxNamespace, scAstCfxDisplayLayer
            )
        #
        def connectionWindowShowCmd():
            tipWin = uiWidgets.UiTipWindow()
            tipWin.setNameText(u'{} Connection'.format(self._itemText0))
            #
            connections = maAttr.getConnectionFilterByNamespace(self._namespace)
            if connections:
                for i in connections:
                    sourceAttr, targetAttr = i
                    html = uiHtml.getHtmlConnection(sourceAttr, targetAttr, self._namespace)
                    tipWin.addHtml(html)
            #
            tipWin.uiShow()
        #
        actionDatumLis = [
            (u'Basic Action(s)',),
            (u'Reload / Load {} Product'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, productLoadActiveCmd),
            (u'Reload / Load {} Cache(s)'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, cacheLoadActiveCmd),
            (u'Extend Action(s)',),
            (u'Refresh Connection', 'svg_basic@svg#refresh', True, connectionRefreshCmd),
            (u'Refresh Display', 'svg_basic@svg#refresh', True, displayRefreshCmd),
            (u'Window',),
            (u'Show {} Connection'.format(self._itemText0), 'svg_basic@svg#subWindow', True,
             connectionWindowShowCmd)
        ]
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = assetPr.getAstUnitProductActiveTimeTag(
            self._projectName,
            self._assetClass, self._assetName, self._assetVariant, lxConfigure.LynxiProduct_Asset_Link_Cfx
        )


# CFX Cache
class IfScAstCfxFurCacheItem(IfScAstBranchItemBasic):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        branchInfo, connectMethod, objectLabel
    ):
        self._overrideAttr()
        #
        self.clsSuper = super(IfScAstCfxFurCacheItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            branchInfo, connectMethod, objectLabel
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic@svg#cache'
        self._itemText0 = u'Fur Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                logWin = None
                #
                maScLoadCmds.scUnitAstCfxFurCacheConnectSubCmd(
                    logWin,
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                    self._startFrame, self._endFrame,
                    self._assetIndex,
                    self._assetClass, self._assetName, self._number, self._assetVariant,
                    self._path,
                    withAstCfxFurCache=cacheFile
                )
                #
                self._refreshItemState(currentTimeTag)
                #
                if self._connectMethod:
                    self._connectMethod()
            #
            currentTimeTag = lxBasic.getOsFileTimeTag(cacheFile)
            if not currentTimeTag == '0000_0000_0000':
                actionExplain = lxBasic.translateRecordViewTime(currentTimeTag)
                #
                iconKeyword = 'link#%s' % stage
                #
                iconExplain = iconKeyword, 'svg_basic@svg#load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeyword, 'state@svg#active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAstCfxFurCacheConnectSubCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                self._path,
                withAstCfxFurCache=True
            )
            #
            self._refreshItemState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def showCacheManagerWindowCmd():
            from LxInterface.qt.ifWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                lxConfigure.LynxiScAstExtraCacheType,
                (
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant,
                    self._startFrame, self._endFrame,
                    self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant
                )
            )
            w.setListCache()
            w.windowShow()
        #
        osFileDic = scenePr.getScAstCfxFurCacheDic(
            self._projectName,
            self._sceneName, self._sceneVariant,
            self._assetName, self._number, self._assetVariant,
            self._objectLabel, self._objectType
        )
        #
        actionDatumLis = []
        for seq, (cacheSceneStage, cacheFileLis) in enumerate(osFileDic.items()):
            actionDatumLis.append(
                (lxBasic._toStringPrettify(scenePr.getSceneLink(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic@svg#subWindow', True, showCacheManagerWindowCmd)
            ]
        )
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = scenePr.getScAstCfxFurCacheTimeTag(
            self._projectName,
            self._sceneName, self._sceneVariant,
            self._assetName, self._number, self._assetVariant,
            self._objectLabel
        )
    #
    def _refreshVars(self):
        self._vars = (
            self._projectName,
            self._sceneIndex,
            self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
            self._startFrame, self._endFrame,
            self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant,
            self._path
        )


#
class IfScAstSolverProductItem(IfScAstBranchItemBasic):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self.clsSuper = super(IfScAstSolverProductItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic@svg#caches'
        self._itemText0 = u'Solver'
    #
    def _updateItemAction(self):
        def productLoadActiveCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAstSolverProductLoadCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withAstSolverCache=True
            )
            #
            self._refreshItemState()
            self._refreshChildItemsState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def cacheLoadActiveCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAstSolverCacheConnectCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withAstSolverCache=True
            )
            #
            self._refreshChildItemsState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def connectionWindowShowCmd():
            tipWin = uiWidgets.UiTipWindow()
            tipWin.setNameText(u'{} Connection'.format(self._itemText0))
            #
            connections = maAttr.getConnectionFilterByNamespace(self._namespace)
            if connections:
                for i in connections:
                    sourceAttr, targetAttr = i
                    html = uiHtml.getHtmlConnection(sourceAttr, targetAttr, self._namespace)
                    tipWin.addHtml(html)
            #
            tipWin.uiShow()
        #
        isProductLoadEnable = self._itemLocalTimeTag is None
        #
        actionDatumLis = [
            (u'Basic Action(s)',),
            (u'Reload / Load {} Product'.format(self._itemText0), 'svg_basic@svg#timeRefresh', isProductLoadEnable, productLoadActiveCmd),
            (u'Reload / Load {} Cache(s)'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, cacheLoadActiveCmd),
            (u'Window',),
            (u'Show {} Connection'.format(self._itemText0), 'svg_basic@svg#subWindow', True,
             connectionWindowShowCmd)
        ]
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = assetPr.getAstUnitProductActiveTimeTag(
            self._projectName,
            self._assetClass, self._assetName, self._assetVariant, lxConfigure.LynxiProduct_Asset_Link_Solver
        )


#
class IfScAstSolverCacheItem(IfScAstBranchItemBasic):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneClass, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetClass, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self.clsSuper = super(IfScAstSolverCacheItem, self)
        self.clsSuper.__init__()
        #
        self._initItemBasic(
            parentItem,
            projectName,
            sceneIndex,
            sceneClass, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetClass, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic@svg#cache'
        self._itemText0 = u'Solver Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                logWin = None
                #
                maScLoadCmds.scUnitAstSolverCacheConnectCmd(
                    logWin,
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                    self._startFrame, self._endFrame,
                    self._assetIndex,
                    self._assetClass, self._assetName, self._number, self._assetVariant,
                    withAstSolverCache=cacheFile
                )
                #
                self._refreshItemState(currentTimeTag)
                #
                if self._connectMethod:
                    self._connectMethod()
            #
            currentTimeTag = lxBasic.getOsFileTimeTag(cacheFile)
            if not currentTimeTag == '0000_0000_0000':
                actionExplain = lxBasic.translateRecordViewTime(currentTimeTag)
                #
                iconKeyword = 'link#%s' % stage
                #
                iconExplain = iconKeyword, 'svg_basic@svg#load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeyword, 'state@svg#active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            logWin = None
            #
            maScLoadCmds.scUnitAstModelCacheConnectCmd(
                logWin,
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                withModelCache=True
            )
            #
            self._refreshItemState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def showCacheManagerWindowCmd():
            from LxInterface.qt.ifWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                lxConfigure.LynxiScAstModelCacheType,
                (
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant,
                    self._startFrame, self._endFrame,
                    self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant
                )
            )
            w.setListCache()
            w.windowShow()
        #
        osFileDic = scenePr.getScAstSolverCacheDic(
            self._projectName,
            self._sceneName, self._sceneVariant,
            self._assetName, self._number
        )
        #
        actionDatumLis = []
        for seq, (cacheSceneStage, cacheFileLis) in enumerate(osFileDic.items()):
            actionDatumLis.append(
                (lxBasic._toStringPrettify(scenePr.getSceneLink(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic@svg#timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic@svg#subWindow', True, showCacheManagerWindowCmd)
            ]
        )
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = scenePr.getScAstSolverCacheActiveTimeTag(
                self._projectName,
                self._sceneName, self._sceneVariant,
                self._assetName, self._number
            )