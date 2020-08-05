# coding:utf-8
import types
#
from LxBasic import bscCfg, bscMethods

from LxPreset import prsConfigure, prsMethods
#
from LxCore.config import appCfg
#
from LxCore.preset.prod import assetPr, scenePr
#
from LxGui.qt import qtWidgets_, guiQtWidgets
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
class IfCfg_ScProductItem(object):
    _tip0 = u'{0} 未载入：\n1，在右击菜单点击“Reload / Load {0} ( Active )”加载。'
    _tip1 = u'{0} 不存在于镜头场景：\n1，如果资源是“Cache”，可能“Cache”无动画数据，可忽略，或者联系制片。'
    _tip2 = u'{0} 有更新：\n1，在右击菜单点击“Reload / Load {0} ( Active )”更新。'
    _tip3 = u'{0} 不存在于服务器：\n1，可忽略，或者联系制片。'
    _tip4 = u'{0} 操作已经禁用：\n1，请先更新上层“Tree Item”。'


#
class IfAbc_ScCameraProductItem(
    qtWidgets_.QTreeWidgetItem_, 
    IfCfg_ScProductItem
):
    def _initScCameraProductItem(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        branchInfo, connectMethod, subLabelString,
    ):
        self._projectName = projectName
        #
        self._sceneIndex, self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage = sceneIndex, sceneCategory, sceneName, sceneVariant, sceneStage
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
        self._itemIcon1 = 'svg_basic/local'
        self._itemIconState1 = None
        self._itemText1 = None
        self._itemIcon2 = 'svg_basic/server'
        self._itemIconState2 = None
        self._itemText2 = None
        self._itemIcon3 = 'svg_basic/time'
        self._itemIconState3 = None
        self._itemText3 = None
        #
        self.CLS_painterPath = None
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
        self._subLabel = subLabelString
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
        return self.CLS_painterPath
    @path.setter
    def path(self, string):
        self.CLS_painterPath = string
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
        self.setText(2, bscMethods.OsTimetag.toChnPrettify(self._itemLocalTimeTag))
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
        if self._objectType == appCfg.DEF_mya_type_alembic:
            self._localStartFrame, self._localEndFrame = maAbc.getAlembicNodeFrameRange(self.CLS_painterPath)
    #
    def _refreshItemLocalState(self):
        self._itemIconState1 = 'off' if self._itemLocalTimeTag is None else None
        #
        self.setText(2, bscMethods.OsTimetag.toChnPrettify(self._itemLocalTimeTag))
        self.setItemIcon_(2, self._itemIcon1, self._itemIconState1)
    #
    def _refreshItemServerState(self):
        self._itemIconState2 = 'off' if self._itemServerTimeTag is None else None
        #
        self.setText(3, bscMethods.OsTimetag.toChnPrettify(self._itemServerTimeTag))
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
                self.CLS_painterPath = nodePath
                self._namespace = namespace
                self._itemLocalTimeTag = timeTag
                #
                self._objectType = maUtils._getNodeShapeCategoryString(self.CLS_painterPath)
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
class IfScCameraCacheItem(IfAbc_ScCameraProductItem):
    def __init__(
            self,
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            branchInfo, connectMethod, subLabelString
    ):
        self._overrideAttr()
        #
        self._clsSuper = super(IfScCameraCacheItem, self)
        self._clsSuper.__init__()
        #
        self._initScCameraProductItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            branchInfo, connectMethod, subLabelString
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic/cache'
        self._itemText0 = u'Camera Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                #
                maScLoadCmds.scUnitCameraCacheLoadSubCmd(
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
            currentTimeTag = bscMethods.OsFile.findTimetag(cacheFile)
            if not currentTimeTag == bscCfg.BscUtility.DEF_time_tag_default:
                actionExplain = bscMethods.OsTimetag.toChnPrettify(currentTimeTag)
                #
                iconKeywordStr = 'link/%s' % stage
                #
                iconExplain = iconKeywordStr, 'svg_basic/load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeywordStr, 'state/active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            maScLoadCmds.scUnitCameraCacheLoadSubCmd(
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
            from LxKit.qt.kitQtWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                prsConfigure.Product.DEF_key_type_modelcache,
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
                (
                    bscMethods.StrCamelcase.toPrettify(
                        prsMethods.Scene.stageName2linkName(cacheSceneStage)
                    ),
                )
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic/timerefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic/subwindow', True, showCacheManagerWindowCmd)
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
class IfScAssetProductItem(
    qtWidgets_.QTreeWidgetItem_, 
    IfCfg_ScProductItem
):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        connectMethod
    ):
        self._clsSuper = super(IfScAssetProductItem, self)
        self._clsSuper.__init__()
        #
        self._initScAssetProductItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            connectMethod
        )
    def _initScAssetProductItem(
            self,
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            connectMethod
    ):
        self._projectName = projectName
        #
        self._sceneIndex, self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage = sceneIndex, sceneCategory, sceneName, sceneVariant, sceneStage
        #
        self._startFrame, self._endFrame = startFrame, endFrame
        self._localStartFrame, self._localEndFrame = None, None
        #
        self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant = assetIndex, assetCategory, assetName, number, assetVariant
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
        self._itemIcon0 = 'svg_basic/package_object'
        self._itemIconState0 = None
        self._itemText0 = assetPr.getAssetViewInfo(
            assetIndex, assetCategory
        )
        self._itemIcon1 = 'svg_basic/name'
        self._itemIconState1 = None
        self._itemText1 = u'{} - {} ( {} )'.format(assetName, number, assetVariant)
        #
        if parentItem is not None:
            self._parentItem = parentItem
            self.setupItem()
    @property
    def path(self):
        return self.CLS_painterPath
    @path.setter
    def path(self, string):
        self.CLS_painterPath = string
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
            maScLoadCmds.scUnitAssetLoadSubCmd(
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
            (u'Reload / Load {} ( Active )'.format('Asset'), 'svg_basic/timerefresh', isLoadEnable, assetLoadActiveCmd)
        ]
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateItemWidget(self):
        scAssetGroup = scenePr.scAstRootGroupName(
            self._sceneName, self._sceneVariant,
            self._assetName, self._number
        )
        if maUtils._isAppExist(scAssetGroup):
            self.CLS_painterPath = scAssetGroup
            #
            self._itemLocalTimeTag = maUtils.getAttrDatum(self.CLS_painterPath, 'tag')
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
class IfAbc_ScAstBranchItem(
    qtWidgets_.QTreeWidgetItem_, 
    IfCfg_ScProductItem
):
    def _initScAstBranchItem(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        branchInfo, connectMethod, objectLabel=None
    ):
        self._projectName = projectName
        #
        self._sceneIndex, self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage = sceneIndex, sceneCategory, sceneName, sceneVariant, sceneStage
        #
        self._startFrame, self._endFrame = startFrame, endFrame
        self._localStartFrame, self._localEndFrame = None, None
        #
        self._assetIndex, self._assetClass, self._assetName, self._number, self._assetVariant = assetIndex, assetCategory, assetName, number, assetVariant
        #
        self._itemWidget = None
        self._itemTooltip = None
        self._itemLocalTimeTag = None
        self._itemServerTimeTag = None
        #
        self._itemIconState0 = None
        self._itemIcon1 = 'svg_basic/local'
        self._itemIconState1 = None
        self._itemText1 = None
        self._itemIcon2 = 'svg_basic/server'
        self._itemIconState2 = None
        self._itemText2 = None
        self._itemIcon3 = 'svg_basic/time'
        self._itemIconState3 = None
        self._itemText3 = None
        #
        self.CLS_painterPath = None
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
        return self.CLS_painterPath
    @path.setter
    def path(self, string):
        self.CLS_painterPath = string
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
        if self._objectType == appCfg.DEF_mya_type_alembic:
            self._localStartFrame, self._localEndFrame = maAbc.getAlembicNodeFrameRange(self.CLS_painterPath)
        elif self._objectType == appCfg.MaNodeType_Plug_Yeti:
            self._localStartFrame, self._localEndFrame = maFur.getYetiCacheFrameRange(self.CLS_painterPath)
        elif self._objectType == appCfg.MaNodeType_Plug_NurbsHair:
            self._localStartFrame, self._localEndFrame = maFur.getNhrCacheFrameRange(self.CLS_painterPath)
    #
    def _refreshItemLocalState(self):
        self._itemIconState1 = 'off' if self._itemLocalTimeTag is None else None
        #
        self.setText(2, bscMethods.OsTimetag.toChnPrettify(self._itemLocalTimeTag))
        self.setItemIcon_(2, self._itemIcon1, self._itemIconState1)
    #
    def _refreshItemServerState(self):
        self._itemIconState2 = 'off' if self._itemServerTimeTag is None else None
        #
        self.setText(3, bscMethods.OsTimetag.toChnPrettify(self._itemServerTimeTag))
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
                self.CLS_painterPath = nodePath
                self._namespace = namespace
                self._itemLocalTimeTag = timeTag
                #
                self._objectType = maUtils._getNodeShapeCategoryString(self.CLS_painterPath)
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
class IfScAstModelProductItem(IfAbc_ScAstBranchItem):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self._clsSuper = super(IfScAstModelProductItem, self)
        self._clsSuper.__init__()
        #
        self._initScAstBranchItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic/caches'
        self._itemText0 = u'Model'
    #
    def _updateItemAction(self):
        def productLoadActiveCmd():
            maScLoadCmds.scUnitAstModelProductLoadCmd(
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
            # Model Cache
            maScLoadCmds.scUnitAstModelCacheConnectCmd(
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
            tipWin = guiQtWidgets.QtTipWindow()
            tipWin.setNameString(u'{} Connection'.format(self._itemText0))
            #
            connections = maAttr.getConnectionFilterByNamespace(self._namespace)
            if connections:
                for i in connections:
                    sourceAttr, targetAttr = i
                    
                    html = bscMethods.TxtHtml.toHtmlMayaConnection(sourceAttr, targetAttr, self._namespace)
                    tipWin.addHtml(html)
            #
            tipWin.uiShow()
        #
        actionDatumLis = [
            (u'Basic Action(s)',),
            (u'Reload / Load {} Product'.format(self._itemText0), 'svg_basic/timeRefresh', True, productLoadActiveCmd),
            (u'Reload / Load {} Cache(s)'.format(self._itemText0), 'svg_basic/timeRefresh', True, cacheLoadActiveCmd),
            (u'Extend Action(s)',),
            (u'Refresh Connection(s)', 'svg_basic/refresh', False, connectionRefreshCmd),
            (u'Refresh Display', 'svg_basic/refresh', True, displayRefreshCmd),
            (u'Database Action(s)', ),
            (u'Refresh Object Attribute(s)', 'svg_basic/refresh', True, objectAttributeRefreshCmd),
            (u'Refresh Object Set(s)', 'svg_basic/refresh', True, objectSetRefreshCmd),
            (u'Window',),
            (u'Show {} Connection'.format(self._itemText0), 'svg_basic/subwindow', True,
             connectionWindowShowCmd)
        ]
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = assetPr.getAstUnitProductActiveTimeTag(
            self._projectName,
            self._assetClass, self._assetName, self._assetVariant, prsMethods.Asset.modelLinkName()
        )


#
class IfScAstModelCacheItem(IfAbc_ScAstBranchItem):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self._clsSuper = super(IfScAstModelCacheItem, self)
        self._clsSuper.__init__()
        #
        self._initScAstBranchItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic/cache'
        self._itemText0 = u'Model Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                maScLoadCmds.scUnitAstModelCacheConnectCmd(
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
            currentTimeTag = bscMethods.OsFile.findTimetag(cacheFile)
            if not currentTimeTag == bscCfg.BscUtility.DEF_time_tag_default:
                actionExplain = bscMethods.OsTimetag.toChnPrettify(currentTimeTag)
                #
                iconKeywordStr = 'link/%s' % stage
                #
                iconExplain = iconKeywordStr, 'svg_basic/load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeywordStr, 'state/active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            maScLoadCmds.scUnitAstModelCacheConnectCmd(
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
            from LxKit.qt.kitQtWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                prsConfigure.Product.DEF_key_type_modelcache,
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
                (bscMethods.StrCamelcase.toPrettify(prsMethods.Scene.stageName2linkName(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic/timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic/subwindow', True, showCacheManagerWindowCmd)
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
class IfScAstExtraCacheItem(IfAbc_ScAstBranchItem):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self._clsSuper = super(IfScAstExtraCacheItem, self)
        self._clsSuper.__init__()
        #
        self._initScAstBranchItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic/cache'
        self._itemText0 = u'Extra Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                maScLoadCmds.scUnitAstExtraCacheConnectCmd(
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
            currentTimeTag = bscMethods.OsFile.findTimetag(cacheFile)
            if not currentTimeTag == bscCfg.BscUtility.DEF_time_tag_default:
                actionExplain = bscMethods.OsTimetag.toChnPrettify(currentTimeTag)
                #
                iconKeywordStr = 'link/%s' % stage
                #
                iconExplain = iconKeywordStr, 'svg_basic/load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeywordStr, 'state/active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            maScLoadCmds.scUnitAstExtraCacheConnectCmd(
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
            from LxKit.qt.kitQtWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                prsConfigure.Product.DEF_key_type_rigcache,
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
                (bscMethods.StrCamelcase.toPrettify(prsMethods.Scene.stageName2linkName(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic/timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic/subwindow', True, showCacheManagerWindowCmd)
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
class IfScAstCfxProductItem(IfAbc_ScAstBranchItem):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self._clsSuper = super(IfScAstCfxProductItem, self)
        self._clsSuper.__init__()
        #
        self._initScAstBranchItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic/caches'
        self._itemText0 = u'Groom'
    #
    def _updateItemAction(self):
        def productLoadActiveCmd():
            maScLoadCmds.scUnitAstCfxProductLoadCmd(
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
            # Cfx Fur Cache
            maScLoadCmds.scUnitAstCfxFurCachesConnectCmd(
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
            tipWin = guiQtWidgets.QtTipWindow()
            tipWin.setNameString(u'{} Connection'.format(self._itemText0))
            #
            connections = maAttr.getConnectionFilterByNamespace(self._namespace)
            if connections:
                for i in connections:
                    sourceAttr, targetAttr = i
                    html = bscMethods.TxtHtml.toHtmlMayaConnection(sourceAttr, targetAttr, self._namespace)
                    tipWin.addHtml(html)
            #
            tipWin.uiShow()
        #
        actionDatumLis = [
            (u'Basic Action(s)',),
            (u'Reload / Load {} Product'.format(self._itemText0), 'svg_basic/timeRefresh', True, productLoadActiveCmd),
            (u'Reload / Load {} Cache(s)'.format(self._itemText0), 'svg_basic/timeRefresh', True, cacheLoadActiveCmd),
            (u'Extend Action(s)',),
            (u'Refresh Connection', 'svg_basic/refresh', True, connectionRefreshCmd),
            (u'Refresh Display', 'svg_basic/refresh', True, displayRefreshCmd),
            (u'Window',),
            (u'Show {} Connection'.format(self._itemText0), 'svg_basic/subwindow', True,
             connectionWindowShowCmd)
        ]
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = assetPr.getAstUnitProductActiveTimeTag(
            self._projectName,
            self._assetClass, self._assetName, self._assetVariant, prsMethods.Asset.groomLinkName()
        )


# CFX Cache
class IfScAstCfxFurCacheItem(IfAbc_ScAstBranchItem):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        branchInfo, connectMethod, objectLabel
    ):
        self._overrideAttr()
        #
        self._clsSuper = super(IfScAstCfxFurCacheItem, self)
        self._clsSuper.__init__()
        #
        self._initScAstBranchItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            branchInfo, connectMethod, objectLabel
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic/cache'
        self._itemText0 = u'Fur Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                maScLoadCmds.scUnitAstCfxFurCacheConnectSubCmd(
                    self._projectName,
                    self._sceneIndex,
                    self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                    self._startFrame, self._endFrame,
                    self._assetIndex,
                    self._assetClass, self._assetName, self._number, self._assetVariant,
                    self.CLS_painterPath,
                    withAstCfxFurCache=cacheFile
                )
                #
                self._refreshItemState(currentTimeTag)
                #
                if self._connectMethod:
                    self._connectMethod()
            #
            currentTimeTag = bscMethods.OsFile.findTimetag(cacheFile)
            if not currentTimeTag == bscCfg.BscUtility.DEF_time_tag_default:
                actionExplain = bscMethods.OsTimetag.toChnPrettify(currentTimeTag)
                #
                iconKeywordStr = 'link/%s' % stage
                #
                iconExplain = iconKeywordStr, 'svg_basic/load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeywordStr, 'state/active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            maScLoadCmds.scUnitAstCfxFurCacheConnectSubCmd(
                self._projectName,
                self._sceneIndex,
                self._sceneClass, self._sceneName, self._sceneVariant, self._sceneStage,
                self._startFrame, self._endFrame,
                self._assetIndex,
                self._assetClass, self._assetName, self._number, self._assetVariant,
                self.CLS_painterPath,
                withAstCfxFurCache=True
            )
            #
            self._refreshItemState()
            #
            if self._connectMethod:
                self._connectMethod()
        #
        def showCacheManagerWindowCmd():
            from LxKit.qt.kitQtWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                prsConfigure.Product.DEF_key_type_rigcache,
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
                (bscMethods.StrCamelcase.toPrettify(prsMethods.Scene.stageName2linkName(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic/timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic/subwindow', True, showCacheManagerWindowCmd)
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
            self.CLS_painterPath
        )


#
class IfScAstSolverProductItem(IfAbc_ScAstBranchItem):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self._clsSuper = super(IfScAstSolverProductItem, self)
        self._clsSuper.__init__()
        #
        self._initScAstBranchItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic/caches'
        self._itemText0 = u'Solver'
    #
    def _updateItemAction(self):
        def productLoadActiveCmd():
            maScLoadCmds.scUnitAstSolverProductLoadCmd(
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
            maScLoadCmds.scUnitAstSolverCacheConnectCmd(
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
            tipWin = guiQtWidgets.QtTipWindow()
            tipWin.setNameString(u'{} Connection'.format(self._itemText0))
            #
            connections = maAttr.getConnectionFilterByNamespace(self._namespace)
            if connections:
                for i in connections:
                    sourceAttr, targetAttr = i
                    html = bscMethods.TxtHtml.toHtmlMayaConnection(sourceAttr, targetAttr, self._namespace)
                    tipWin.addHtml(html)
            #
            tipWin.uiShow()
        #
        isProductLoadEnable = self._itemLocalTimeTag is None
        #
        actionDatumLis = [
            (u'Basic Action(s)',),
            (u'Reload / Load {} Product'.format(self._itemText0), 'svg_basic/timeRefresh', isProductLoadEnable, productLoadActiveCmd),
            (u'Reload / Load {} Cache(s)'.format(self._itemText0), 'svg_basic/timeRefresh', True, cacheLoadActiveCmd),
            (u'Window',),
            (u'Show {} Connection'.format(self._itemText0), 'svg_basic/subwindow', True,
             connectionWindowShowCmd)
        ]
        self._itemWidget.setActionData(actionDatumLis)
    #
    def _updateServerTimeTag(self):
        self._itemServerTimeTag = assetPr.getAstUnitProductActiveTimeTag(
            self._projectName,
            self._assetClass, self._assetName, self._assetVariant, prsMethods.Asset.solverLinkName()
        )


#
class IfScAstSolverCacheItem(IfAbc_ScAstBranchItem):
    def __init__(
        self,
        parentItem,
        projectName,
        sceneIndex,
        sceneCategory, sceneName, sceneVariant, sceneStage,
        startFrame, endFrame,
        assetIndex,
        assetCategory, assetName, number, assetVariant,
        branchInfo, connectMethod
    ):
        self._overrideAttr()
        #
        self._clsSuper = super(IfScAstSolverCacheItem, self)
        self._clsSuper.__init__()
        #
        self._initScAstBranchItem(
            parentItem,
            projectName,
            sceneIndex,
            sceneCategory, sceneName, sceneVariant, sceneStage,
            startFrame, endFrame,
            assetIndex,
            assetCategory, assetName, number, assetVariant,
            branchInfo, connectMethod
        )
    #
    def _overrideAttr(self):
        self._itemIcon0 = 'svg_basic/cache'
        self._itemText0 = u'Solver Cache'
    #
    def _updateItemAction(self):
        def setCacheLoadActionCmdBranch(stage, cacheFile):
            def scLoadCacheCmd():
                maScLoadCmds.scUnitAstSolverCacheConnectCmd(
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
            currentTimeTag = bscMethods.OsFile.findTimetag(cacheFile)
            if not currentTimeTag == bscCfg.BscUtility.DEF_time_tag_default:
                actionExplain = bscMethods.OsTimetag.toChnPrettify(currentTimeTag)
                #
                iconKeywordStr = 'link/%s' % stage
                #
                iconExplain = iconKeywordStr, 'svg_basic/load_action'
                if currentTimeTag == self._itemServerTimeTag:
                    iconExplain = iconKeywordStr, 'state/active'
                #
                isLoadEnable = currentTimeTag != self._itemLocalTimeTag
                #
                actionDatumLis.append(
                    (actionExplain, iconExplain, isLoadEnable, scLoadCacheCmd)
                )
        #
        def loadActiveCacheCmd():
            maScLoadCmds.scUnitAstModelCacheConnectCmd(
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
            from LxKit.qt.kitQtWidgets import ifProductToolWindow
            #
            w = ifProductToolWindow.IfCacheManagerWindow()
            w.setTitle(u'{} Manager'.format(self._itemText0))
            w.setArgs(
                prsConfigure.Product.DEF_key_type_modelcache,
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
                (bscMethods.StrCamelcase.toPrettify(prsMethods.Scene.stageName2linkName(cacheSceneStage)),)
            )
            for currentCacheFile in cacheFileLis[-5:]:
                setCacheLoadActionCmdBranch(cacheSceneStage, currentCacheFile)
        #
        actionDatumLis.extend(
            [
                (u'Basic Action(s)',),
                (u'Reload / Load {} ( Active )'.format(self._itemText0), 'svg_basic/timeRefresh', True, loadActiveCacheCmd),
                (u'Window',),
                (u'{} Manager'.format(self._itemText0), 'svg_basic/subwindow', True, showCacheManagerWindowCmd)
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
