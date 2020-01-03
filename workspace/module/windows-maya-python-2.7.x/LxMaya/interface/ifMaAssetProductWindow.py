# coding=utf-8
from LxCore import lxBasic, lxScheme
#
from LxCore.config import appCfg, assetCfg
#
from LxCore.preset import pipePr
#
from LxCore.preset.prod import projectPr, assetPr
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore, qtProgress
#
from LxMaya.interface.ifCommands import maAstTreeViewCmds
#
from LxMaya.interface.ifWidgets import ifMaAssetToolUnit
#
from LxDatabase import dbGet
#
from LxMaya.command import maUtils, maGeom, maMshGeomCheck
#
from LxMaya.product.data import datAsset
#
none = ''
#
_header = 'window#productionWin'
_title = 'Asset Production'
_version = lxScheme.Python().version


#
class IfAssetProductToolWindow(qtWidgets.QtToolWindow):
    widthSet = 400
    def __init__(self, parent=qtCore.getAppWindow()):
        super(IfAssetProductToolWindow, self).__init__(parent)
        #
        self.setNameText(_title)
        self.setIndexText(_version)
        #
        self.setDefaultSize(self.widthSet, 875)
        #
        self.assetIndex = none
        self.projectName = none
        self.assetClass = none
        self.assetName = none
        self.assetVariant = none
        self.assetStage = none
        #
        self.assetLink = none
        #
        self.assetNamespace = none
        self.referenceNode = none
        #
        self.geometries = []
        #
        self.headBoxDic = {}
        #
        self.searchDic = {}
        #
        self.astMeshTransErrorData = []
        self.astMeshGeomErrorData = []
        self.astMeshHistoryErrorData = []
        #
        self.astModelMeshData = []
        self.astModelMeshErrorData = []
        #
        self.astCfxFurData = []
        self.astCfxFurErrorData = []
        #
        self._astSolverCheckItemLis = []
        self._astSolverErrorItemLis = []
        #
        self.astTextureData = []
        self.astTextureErrorData = []
        #
        self.isMeshChanged = False
        #
        self.setupWindow()
        #
        self.getAssetInfo()
        #
        self.meshDescription = []
        self.materialDescription = []
    #
    def setTreeBoxHeaderHiddenSwitch(self):
        self.treeBox.setHeaderHidden(self.leftExpandWidget.isExpanded())
    # Create Panel
    def setAstCreateBoxShow(self):
        pass
    #
    def setAstCreateBoxHide(self):
        self.createWidget.hide()
    # Hierarchy
    def setAstHierarchyBox(self, treeBox, explain):
        treeBox.setColumns_(
            ['Group : Nde_Node', 'Nde_Node Type', 'Explain'],
            self.widthSet * 2
        )
        self.rightToolboxGroup.setTitle('%s' % explain)
    #
    def setAstHierarchyView(self):
        assetName = self.assetName
        assetVariant = self.assetVariant
        #
        assetNamespace = self.assetNamespace
        #
        assetStage = self.assetStage
        #
        linkGroup = None
        if assetPr.isAstModelLink(assetStage):
            linkGroup = assetPr.astUnitModelLinkGroupName(assetName)
        elif assetPr.isAstRigLink(assetStage):
            linkGroup = assetPr.astUnitRigLinkGroupName(assetName)
        elif assetPr.isAstCfxLink(assetStage):
            linkGroup = assetPr.astUnitCfxLinkGroupName(assetName)
        elif assetPr.isAstSolverLink(assetStage):
            linkGroup = assetPr.astUnitSolverLinkGroupName(assetName)
        elif assetPr.isAstLightLink(assetStage):
            linkGroup = assetPr.astUnitLightLinkGroupName(assetName)
            #
        treeBox = self.treeBox
        explain = '{} Hierarchy'.format(lxBasic.str_camelcase2prettify(assetPr.getAssetLink(assetStage)))
        #
        self.setAstHierarchyBox(treeBox, explain)
        #
        self.expandedDic = treeBox.getGraphExpandDic()
        #
        treeBox.clear()
        if linkGroup:
            maAstTreeViewCmds.setAstHierarchyView(
                treeBox,
                linkGroup,
                self.searchDic, self.expandedDic
            )
    #
    def setAstMeshConstantBox(self, treeBox, explain):
        treeBox.setColumns_(
            ['Class : Mesh', 'Status', 'Unique ID'],
            self.widthSet * 2
        )
        self.rightToolboxGroup.setTitle('%s' % explain)
    #
    def setAstGeometryConstantMain(self):
        projectName = self.projectName
        #
        assetIndex = self.assetIndex
        #
        assetClass = self.assetClass
        assetName = self.assetName
        assetVariant = self.assetVariant
        #
        treeBox = self.treeBox
        explain = 'Nde_Geometry ( Contrast )'
        #
        self.setAstMeshConstantBox(treeBox, explain)
        # Use Model Group
        astModelLinkGroup = assetPr.astUnitModelLinkGroupName(assetName)
        #
        localInfoDic = maGeom.getGeometryObjectsInfoDic(astModelLinkGroup)
        localPathDic = maGeom.getGeometryObjectsPathDic(astModelLinkGroup)
        #
        serverInfoDic = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        serverPathDic = dbGet.getDbGeometryUnitsPathDic(assetIndex)
        #
        maAstTreeViewCmds.setAstGeometryConstantMain(
            self,
            treeBox,
            assetIndex, assetName, assetVariant,
            localPathDic, localInfoDic,
            serverPathDic, serverInfoDic
        )
    #
    def setAstMeshTopoConstantBox(self, treeBox, explain):
        treeBox.setColumns_(['Group : Nde_Node', 'Unique ID'], self.widthSet * 2)
        self.rightToolboxGroup.setTitle('%s' % explain)
    #
    def setAstMeshTopoConstantView(self):
        assetIndex = self.assetIndex
        projectName = self.projectName
        assetClass = self.assetClass
        assetName = self.assetName
        assetVariant = self.assetVariant
        #
        treeBox = self.treeBox
        explain = 'Mesh ( Topology - Contrast )'
        #
        self.setAstMeshTopoConstantBox(treeBox, explain)
        #
        maAstTreeViewCmds.setAstMeshTopoConstantView(treeBox, assetIndex, assetName)
    #
    def setCheckInfoLabel(self, inCheck, outGeo, checkType):
        inCheckCount = len(inCheck)
        outGeoCount = len(outGeo)
        self.rightToolboxGroup.setTitle(
            'Mesh ( %s [ %s + %s ] )' % (checkType, outGeoCount, (inCheckCount - outGeoCount))
        )
    #
    def setAssetCheckList(self):
        checkConfig = {}
        #
        assetStage = self.assetStage
        #
        treeBox = self.treeBox
        #
        treeBox.clear()
        #
        if assetPr.isAstModelLink(assetStage):
            checkConfig = assetCfg.astModelCheckConfig()
        elif assetPr.isAstCfxLink(assetStage):
            checkConfig = assetCfg.astCfxGroomCheckConfig()
        elif assetPr.isAstRigLink(assetStage):
            checkConfig = assetCfg.astRigCheckConfig()
        elif assetPr.isAstSolverLink(assetStage):
            checkConfig = assetCfg.astSolverCheckConfig()
        elif assetPr.isAstLightLink(assetStage):
            checkConfig = assetCfg.astLightCheckConfig()
        #
        self.rightToolboxGroup.setTitle('Check List')
        treeBox.setColumns_(
            ['Inspection Item', 'Explain'],
            self.widthSet*2
        )
        #
        if checkConfig:
            for k, v in checkConfig.items():
                enable, enExplain, cnExplain = v
                inspectionItem = qtWidgets_.QTreeWidgetItem_([enExplain, cnExplain])
                self.treeBox.addItem(inspectionItem)
                if enable is True:
                    inspectionItem.setItemIcon(0, 'svg_basic@svg#check')
                else:
                    inspectionItem.setItemIcon(0, 'svg_basic@svg#checkDisable')
    #
    def setAstModelCheckBox(self):
        assetClass = self.assetClass
        assetName = self.assetName
        #
        treeBox = self.treeBox
        #
        inCheck = datAsset.getAstMeshObjects(assetName, 0)
        outGeo = datAsset.getAstMeshObjects(assetName, 1)
        #
        self.treeBox.clear()
        if inCheck:
            treeBox.setColumns_(
                ['Inspection Item : Nde_Geometry', 'Explain'],
                self.widthSet*2
            )
            self.setCheckInfoLabel(inCheck, outGeo, 'Model')
            #
            self.setViewAstModelCheckResult()
        else:
            self.setAssetCheckList()
    #
    def setAstMeshTransCheck(self):
        assetClass = self.assetClass
        assetName = self.assetName
        #
        self.astMeshTransErrorData = []
        #
        checkObjectLis = datAsset.getAstMeshObjects(assetName, 0)
        outGeo = datAsset.getAstMeshObjects(assetName, 1)
        #
        treeBox = self.treeBox
        treeBox.clear()
        inData = datAsset.getObjectNonZeroTransAttrDic(checkObjectLis)
        errorData = self.astMeshTransErrorData
        treeBox.setColumns_(
            ['Nde_Geometry : Transformation', 'Channel - X', 'Channel - Y', 'Channel - Z'],
            self.widthSet*2
        )
        self.setCheckInfoLabel(checkObjectLis, outGeo, 'Transformation')
        #
        maAstTreeViewCmds.setAstMeshTransCheckView(self, treeBox, inData, checkObjectLis, errorData)
    #
    def setAstMeshGeomCheck(self):
        assetClass = self.assetClass
        assetName = self.assetName
        #
        self.astMeshGeomErrorData = []
        #
        checkObjectLis = datAsset.getAstMeshObjects(assetName)
        outGeo = datAsset.getAstMeshObjects(assetName, 1)
        #
        treeBox = self.treeBox
        treeBox.clear()
        errorData = self.astMeshGeomErrorData
        #
        treeBox.setColumns_(
            ['Nde_Geometry : Component', 'Explain'],
            self.widthSet*2
        )
        self.setCheckInfoLabel(checkObjectLis, outGeo, 'Nde_Geometry')
        inData = maMshGeomCheck.getAstMeshGeomCheckDataDic(checkObjectLis)
        #
        maAstTreeViewCmds.setAstMeshGeomCheckView(self, treeBox, inData, checkObjectLis, errorData)
    #
    def setAstMeshHistCheck(self):
        assetClass = self.assetClass
        assetName = self.assetName
        #
        self.astMeshHistoryErrorData = []
        #
        checkObjectLis = datAsset.getAstMeshObjects(assetName, 0)
        outGeo = datAsset.getAstMeshObjects(assetName, 1)
        #
        treeBox = self.treeBox
        treeBox.clear()
        inData = datAsset.filterObjectHistoryNodeDic(checkObjectLis)
        errorData = self.astMeshHistoryErrorData
        #
        treeBox.setColumns_(
            ['Nde_Geometry : Nde_Node', 'Nde_Node Type', 'Explain'],
            self.widthSet * 2
        )
        self.setCheckInfoLabel(checkObjectLis, outGeo, 'History')
        #
        maAstTreeViewCmds.setAstMeshHistCheckView(self, treeBox, inData, checkObjectLis, errorData)
    #
    def setViewAstModelCheckResult(self):
        def getCheckData():
            dic = {
                'meshMatrixNonDefaultCheck': self.astMeshTransErrorData,
                'meshGeometryCheck': self.astMeshGeomErrorData,
                'meshHistoryCheck': self.astMeshHistoryErrorData
            }
            return dic
        #
        assetName = self.assetName
        #
        inCheck = datAsset.getAstMeshObjects(assetName, 0)
        outGeo = datAsset.getAstMeshObjects(assetName, 1)
        #
        self.astModelMeshErrorData = []
        tempErrorData = []
        checkConfig = assetCfg.astModelCheckConfig()
        #
        inData = getCheckData()
        inData['meshInstanceCheck'] = datAsset.getInstanceObjectLis(inCheck)
        inData['meshVertexNormalLockCheck'] = datAsset.getMeshesIsNormalLock(inCheck)
        inData['meshOverlapNameCheck'] = maUtils.getNameOverlappingObjectLis(inCheck)
        for seq, (k, v) in enumerate(checkConfig.items()):
            enable, enExplain, cnExplain = v
            #
            self.setProgressValue(seq + 1, len(checkConfig))
            #
            inspectionItem = qtWidgets_.QTreeWidgetItem_([enExplain, cnExplain])
            inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check')
            self.treeBox.addItem(inspectionItem)
            #
            if k in inData:
                errorData = inData[k]
                if errorData:
                    isError = False
                    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'warning')
                    for i in inCheck:
                        geomObjectName = maUtils._toNodeName(i)
                        if i in errorData:
                            geomItem = qtWidgets_.QTreeWidgetItem_([geomObjectName])
                            inspectionItem.addChild(geomItem)
                            tempErrorData.append(i)
                            if i in outGeo:
                                isError = True
                                geomItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'error')
                            else:
                                geomItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'warning')
                    #
                    if isError:
                        inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'Error')
                        inspectionItem.setExpanded(True)
                else:
                    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'on')
            #
            if k == 'meshTransformCheck':
                errorData = datAsset.getErrorTransforms(assetName)
                if errorData:
                    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'error')
                    inspectionItem.setExpanded(True)
                    for i in errorData:
                        transformName = maUtils._toNodeName(i)
                        transformItem = qtWidgets_.QTreeWidgetItem_([transformName])
                        transformItem.setItemMayaIcon(0, appCfg.MaNodeType_Transform, 'error')
                        inspectionItem.addChild(transformItem)
                else:
                    inspectionItem.setItemCheckIcon(0, 'svg_basic@svg#check', 'on')
        #
        [self.astModelMeshErrorData.append(i) for i in tempErrorData if i in outGeo and i not in self.astModelMeshErrorData]
    #
    def setAstTextureCheckBox(self, treeBox, explain):
        treeBox.setColumns_(
            ['Folder > File > Nde_Node', 'Nde_Node Type', 'Local Time', 'Local Time ( tx )'],
            self.widthSet * 2
        )
        self.rightToolboxGroup.setTitle(explain)
    #
    def setAstTextureCheckView(self):
        self.astTextureData = []
        self.astTextureErrorData = []
        #
        projectName = self.projectName
        assetClass = self.assetClass
        assetName = self.assetName
        assetVariant = self.assetVariant
        assetStage = self.assetStage
        #
        usedObjects = []
        if assetPr.isAstModelLink(assetStage) or assetPr.isAstRigLink(assetStage):
            usedObjects = datAsset.getAstMeshObjects(assetName, 1)
        elif assetPr.isAstCfxLink(assetStage):
            yetiObjects = datAsset.getYetiObjects(assetName)
            nurbsHairObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
            #
            usedObjects = yetiObjects
            usedObjects.extend(nurbsHairObjects)
        elif assetPr.isAstLightLink(assetStage):
            linkBranch = assetPr.astUnitLightLinkGroupName(assetName)
            usedObjects = maUtils.getChildrenByRoot(linkBranch)
        #
        treeBox = self.treeBox
        explain = 'Texture Check'
        #
        self.setAstTextureCheckBox(treeBox, explain)
        #
        inData = datAsset.getTextureStatisticsDic(usedObjects)
        #
        checkData = self.astTextureData
        errorData = self.astTextureErrorData
        #
        treeBox.clear()
        maAstTreeViewCmds.setAstTextureCheckView(
            projectName,
            assetClass, assetName, assetVariant, assetStage,
            treeBox, inData, checkData, errorData
        )
    #
    def setAstCfxGroomCheckBox(self, treeBox, explain):
        treeBox.setColumns_(
            ['Inspection Item : Object', 'Type', 'Explain'],
            self.widthSet * 2
        )
        self.rightToolboxGroup.setTitle(explain)
    #
    def setAstCfxCheckCmd(self):
        self.astCfxFurData = []
        self.astCfxFurErrorData = []
        #
        assetClass = self.assetClass
        assetName = self.assetName
        #
        treeBox = self.treeBox
        explain = '''Character FX ( Groom ) Check'''
        checkData = self.astCfxFurData
        errorData = self.astCfxFurErrorData
        #
        self.setAstCfxGroomCheckBox(treeBox, explain)
        #
        treeBox.clear()
        maAstTreeViewCmds.setAstCfxFurCheckTreeView(self, assetClass, assetName, treeBox, checkData, errorData)
    #
    def setAstSolverCheckCmd(self):
        self._astSolverCheckItemLis = []
        self._astSolverErrorItemLis = []
        #
        assetClass = self.assetClass
        assetName = self.assetName
        #
        treeBox = self.treeBox
        explain = 'Asset Character FX ( Solver ) Check'
        checkData = self._astSolverCheckItemLis
        errorData = self._astSolverErrorItemLis
        #
        self.setAstCfxGroomCheckBox(treeBox, explain)
        #
        treeBox.clear()
        maAstTreeViewCmds.setAstSolverGuideCheckSub(self, assetClass, assetName, treeBox, checkData, errorData)
        maAstTreeViewCmds.setAstSolverGrowSourceCheckSub(self, assetClass, assetName, treeBox, checkData, errorData)
    #
    def setViewAstLightCheckResult(self):
        pass
    #
    def setShaderCheckBox(self, treeBox, explain):
        treeBox.setColumns_(
            ['Shading Group : Nde_Node', 'Nde_Node Type', 'Explain'],
            self.widthSet * 2
        )
        self.rightToolboxGroup.setTitle(explain)
    #
    def setShaderCheckView(self):
        assetClass = self.assetClass
        assetName = self.assetName
        #
        treeBox = self.treeBox
        explain = 'Material Check'
        #
        self.setShaderCheckBox(treeBox, explain)
        #
        if self.assetStage != 'cfx':
            maAstTreeViewCmds.setAstShaderCheckView(assetClass, assetName, treeBox)
    #
    def setupToolUnits(self):
        self.setupLeftWidget(self.leftToolScrollBox, self.leftBottomToolBar)
        self.setupRightWidget(self.rightBottomToolBar)
    #
    def setAstTopToolBar(self, layout):
        self._filterButton = qtWidgets.QtMenuIconbutton('svg_basic@svg#filter')
        layout.addWidget(self._filterButton)
        #
        self._infoLabel = qtWidgets.QtEnterlabel()
        layout.addWidget(self._infoLabel)
        self._infoLabel.setNameTextWidth(0)
        #
        self.filterEnterLabel = qtWidgets.QtFilterEnterlabel()
        layout.addWidget(self.filterEnterLabel)
        self.treeBox.setFilterConnect(self.filterEnterLabel)
        #
        self._refreshButton = qtWidgets.QtIconbutton('svg_basic@svg#refresh')
        layout.addWidget(self._refreshButton)
        self._refreshButton.clicked.connect(self.setRefresh)
    # Tool Panel
    def setupLeftWidget(self, toolBoxLayout, toolBarLayout):
        assetLink = self.assetLink
        assetClass = self.assetClass
        #
        uiDatumLis = [
            ('astCharTool', ifMaAssetToolUnit.IfAstModelCharToolUnit, False, []),
            ('astModelTool', ifMaAssetToolUnit.IfAstModelToolUnit, False, []),
            ('astRigTool', ifMaAssetToolUnit.IfAstRigToolUnit, False, []),
            ('astCfxTool', ifMaAssetToolUnit.IfAstCfxGroomToolUnit, False, []),
            ('astSolverTool', ifMaAssetToolUnit.IfAstSolverToolUnit, False, []),
            ('astGnlTool', ifMaAssetToolUnit.IfAstGeneralToolUnit, True, []),
            ('astInfoTool', ifMaAssetToolUnit.IfAstModelInfoToolUnit, True, [self.setInformationShow]),
            ('astUploadTool', ifMaAssetToolUnit.IfAstUploadToolUnit, True, [])
        ]
        # View Progress
        explain = '''Build Asset Interface Unit(s)'''
        maxValue = len(uiDatumLis)
        progressBar = qtProgress.viewSubProgress(explain, maxValue)
        for i in uiDatumLis:
            progressBar.updateProgress()
            #
            key, toolUnitClass, visible, connectMethodLis = i
            # Unit
            toolUnit = None
            toolUnitCreateCmd = 'self.{0}Unit = toolUnitClass();toolUnit = self.{0}Unit'.format(key)
            exec toolUnitCreateCmd
            toolUnit.setConnectObject(self)
            toolUnit.refreshMethod()
            #
            links = toolUnit.UnitConnectLinks
            title = toolUnit.UnitTitle
            iconKeyword = toolUnit.UnitIcon
            tooltip = toolUnit.UnitTooltip
            # Toggle Button
            toggleButton = None
            toggleButtonCreateCmd = 'self.{0}ToggleButton = qtWidgets_.QRadioButton_();toggleButton = self.{0}ToggleButton'.format(key)
            exec toggleButtonCreateCmd
            toggleButton.setIconExplain(iconKeyword, 32, 32)
            #
            if not assetLink in links:
                toggleButton.hide()
            if hasattr(toolUnitClass, 'UnitClassLimit'):
                if not assetClass in toolUnitClass.UnitClassLimit:
                    toggleButton.hide()
            #
            if connectMethodLis:
                for j in connectMethodLis:
                    toggleButton.clicked.connect(j)
            toggleButton.setTooltip(tooltip)
            # Tool Group
            toolGroupBox = None
            toolGroupBoxCreateCmd = 'self.{0}GroupBox = qtWidgets.QtToolboxGroup();toolGroupBox = self.{0}GroupBox'.format(key)
            exec toolGroupBoxCreateCmd
            toolGroupBox.hide()
            toolGroupBox.setExpanded(True)
            toolGroupBox.setTitle(title)
            toolBoxLayout.addWidget(toolGroupBox)
            toolGroupBox.addWidget(toolUnit)
            #
            toggleButton.toggled.connect(toolGroupBox.setVisible)
            toolBarLayout.addWidget(toggleButton)
        #
        self.toolWidget.show()
    #
    def setupRightWidget(self, toolBarLayout):
        uiDatumLis = [
            ('astCheck', 'window#checkPanel', u'点击显示/刷新检查列表', True, (self.setAssetCheckList,)),
            ('astHierarchy', 'window#hierarchyPanel', u'点击显示/刷新资产层级', False, (self.setAstHierarchyView,)),
            ('astMeshConstant', 'window#constantToolPanel', u'点击显示/刷新模型对比', False, (self.setAstGeometryConstantMain,)),
            ('astMeshTopoConstant', 'window#topoConstantPanel', u'点击显示/刷新拓扑对比', False, (self.setAstMeshTopoConstantView,)),
            ('astTransCheck', 'window#transformationPanel', u'点击显示/刷新位置信息检查', False, (self.setAstMeshTransCheck,)),
            #
            ('astGeomCheck', 'window#geometryPanel', u'点击显示/刷新拓扑检查', False, (self.setAstMeshGeomCheck,)),
            ('astHistCheck', 'window#historyPanel', u'点击显示/刷新历史记录检查', False, (self.setAstMeshHistCheck,)),
            ('astCfxCheck', 'window#cfxCheckPanel', u'点击显示/刷新角色特效检查', False, (self.setAstCfxCheckCmd,)),
            ('astSolverCheck', 'window#solverCheckPanel', u'点击显示/刷新模拟检查', False, (self.setAstSolverCheckCmd, )),
            ('astTxtrCheck', 'window#texturePanel', u'点击显示/刷新贴图检查', False, (self.setAstTextureCheckView,)),
            ('astShdrCheck', 'window#texturePanel', u'点击显示/刷新材质检查', False, (self.setShaderCheckView,))
        ]
        for i in uiDatumLis:
            key, iconKeyword, tooltip, visible, connectMethodLis = i
            toggleButton = None
            toggleButtonCreateCmd = 'self.{0}ToggleButton = qtWidgets_.QRadioButton_();toggleButton = self.{0}ToggleButton'.format(key)
            exec toggleButtonCreateCmd
            toggleButton.setIconExplain(iconKeyword, 32, 32)
            #
            if visible is False:
                toggleButton.hide()
            #
            if connectMethodLis:
                for command in connectMethodLis:
                    toggleButton.clicked.connect(command)
            toggleButton.setTooltip(tooltip)
            #
            toolBarLayout.addWidget(toggleButton)
    #
    def getSelGeo(self):
        treeBox = self.treeBox
        return treeBox.selectedItemPaths()
    #
    def setInformationShow(self):
        self.astInfoToolUnit.setTabSwitch()
        self.isMeshChanged = self.astInfoToolUnit.isMeshChanged
        #
        self.astUploadToolUnit._updateAstUploadState()
    #
    def _initAstModelToolBar(self):
        self.astCheckToggleButton.setChecked(True)
        #
        self.astTransCheckToggleButton.show()
        self.astGeomCheckToggleButton.show()
        self.astHistCheckToggleButton.show()
        #
        self.astMeshConstantToggleButton.show()
        self.astTxtrCheckToggleButton.show()
    #
    def _initAstRigToolBar(self):
        self.astCheckToggleButton.setChecked(True)
        #
        self.astMeshConstantToggleButton.show()
        self.astTxtrCheckToggleButton.show()
    #
    def _initAstCfxToolBar(self):
        self.astCheckToggleButton.setChecked(True)
        #
        self.astMeshConstantToggleButton.show()
        #
        self.astCfxCheckToggleButton.show()
        self.astTxtrCheckToggleButton.show()
    #
    def _initAstSolverToolBar(self):
        self.astCheckToggleButton.setChecked(True)
        #
        self.astMeshConstantToggleButton.show()
        #
        self.astSolverCheckToggleButton.show()
    #
    def _initAstLightToolBar(self):
        self.astCheckToggleButton.setChecked(True)
        #
        self.astMeshConstantToggleButton.show()
        self.astTxtrCheckToggleButton.show()
    #
    def setSel(self):
        data = self.getSelGeo()
        if data:
            maUtils.setNodeSelect(data)
        else:
            pass
    #
    def getAssetInfo(self):
        projectName = projectPr.getMayaProjectName()
        self.projectName = projectName
        #
        assetInfoLis = datAsset.getAssetInfo()
        if assetInfoLis:
            self.setPlaceholderEnable(False)
            #
            assetInfo = assetInfoLis[0]
            assetIndex, assetClass, assetName, assetVariant, assetStage = assetInfo
            self.assetIndex = assetIndex
            self.assetClass = assetClass
            self.assetName = assetName
            self.assetVariant = assetVariant
            self.assetStage = assetStage
            #
            self.assetLink = assetPr.getAssetLink(assetStage)
            #
            if assetPr.isAssetLink(assetStage):
                isAssetLink = True
                #
                self.setAssetInfo(assetIndex, assetClass, assetName, assetVariant)
                #
                self.setupToolUnits()
                #
                self.astInfoToolToggleButton.setChecked(True)
                self.setInformationShow()
                #
                self.setAssetCheckList()
                if assetPr.isAstModelLink(assetStage):
                    self._initAstModelToolBar()
                elif assetPr.isAstRigLink(assetStage):
                    self._initAstRigToolBar()
                elif assetPr.isAstCfxLink(assetStage):
                    self._initAstCfxToolBar()
                elif assetPr.isAstSolverLink(assetStage):
                    self._initAstSolverToolBar()
                elif assetPr.isAstLightLink(assetStage):
                    self._initAstLightToolBar()
                #
                title = 'Asset {} Production'.format(lxBasic.str_camelcase2prettify(self.assetLink))
                self.setNameText(title)
            else:
                self.setPlaceholderEnable(True)
                #
                isAssetLink = False
        else:
            self.setPlaceholderEnable(True)
            #
            isAssetLink = False
        #
        if isAssetLink is False:
            self.setAstCreateBoxShow()
    #
    def setRefresh(self):
        pass
    #
    def setAssetInfo(self, assetIndex, assetClass, assetName, assetVariant):
        if assetClass and assetName and assetVariant:
            showName = assetPr.getAssetViewInfo(
                assetIndex, assetClass, assetVariant
            )
            self._infoLabel.setDatum(showName)
            #
            self.assetClass = assetClass
            self.assetName = assetName
            self.assetVariant = assetVariant
    #
    def setupWindow(self):
        widget = qtCore.QWidget_()
        self.addWidget(widget)
        mainLayout = qtCore.QHBoxLayout_(widget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        #
        self.createWidget = qtCore.QWidget_()
        self.createWidget.hide()
        mainLayout.addWidget(self.createWidget)
        #
        createLayout = qtCore.QHBoxLayout_(self.createWidget)
        createLayout.setContentsMargins(0, 0, 0, 0)
        createLayout.setSpacing(0)
        #
        self.leftCreateWidget = qtCore.QWidget_()
        createLayout.addWidget(self.leftCreateWidget)
        #
        leftCreateLayout = qtCore.QVBoxLayout_(self.leftCreateWidget)
        leftCreateLayout.setContentsMargins(0, 0, 0, 0)
        leftCreateLayout.setSpacing(0)
        #
        self.rightCreateWidget = qtCore.QWidget_()
        self.rightCreateWidget.hide()
        createLayout.addWidget(self.rightCreateWidget)
        #
        self.toolWidget = qtCore.QWidget_()
        self.toolWidget.hide()
        mainLayout.addWidget(self.toolWidget)
        #
        toolLayout = qtCore.QGridLayout_(self.toolWidget)
        toolLayout.setContentsMargins(4, 4, 4, 4)
        toolLayout.setSpacing(2)
        #
        self.topToolBar = qtWidgets_.xToolBar()
        toolLayout.addWidget(self.topToolBar, 0, 0, 1, 2)
        #
        self.leftExpandWidget = qtWidgets_.QtExpandWidget()
        toolLayout.addWidget(self.leftExpandWidget, 1, 0, 1, 1)
        self.leftExpandWidget.setUiWidth(self.widthSet)
        #
        self.leftToolWidget = qtCore.QWidget_()
        self.leftExpandWidget.addWidget(self.leftToolWidget)
        #
        leftToolLayout = qtCore.QVBoxLayout_(self.leftToolWidget)
        leftToolLayout.setContentsMargins(0, 0, 0, 0)
        leftToolLayout.setSpacing(0)
        #
        self.leftToolScrollBox = qtCore.QScrollArea_()
        leftToolLayout.addWidget(self.leftToolScrollBox)
        #
        self.leftBottomToolBar = qtWidgets_.xToolBar()
        leftToolLayout.addWidget(self.leftBottomToolBar)
        #
        self._rightWidget = qtCore.QWidget_()
        toolLayout.addWidget(self._rightWidget, 1, 1, 1, 1)
        self._rightWidget.setMinimumWidth(self.widthSet)
        #
        rightToolLayout = qtCore.QVBoxLayout_(self._rightWidget)
        rightToolLayout.setContentsMargins(0, 0, 0, 0)
        rightToolLayout.setSpacing(0)
        #
        self.rightToolScrollBox = qtCore.QScrollArea_()
        rightToolLayout.addWidget(self.rightToolScrollBox)
        #
        self.rightToolboxGroup = qtWidgets.QtToolboxGroup()
        self.rightToolboxGroup.setExpanded(True)
        self.rightToolScrollBox.addWidget(self.rightToolboxGroup)
        #
        self.treeBox = qtWidgets_.QTreeWidget_()
        self.rightToolboxGroup.addWidget(self.treeBox)
        self.treeBox.itemSelectionChanged.connect(self.setSel)
        #
        self.rightBottomToolBar = qtWidgets_.xToolBar()
        rightToolLayout.addWidget(self.rightBottomToolBar)
        #
        self.setAstTopToolBar(self.topToolBar)


@qtCore.uiSetupShowMethod
def tableShow():
    ui = IfAssetProductToolWindow()
    ui.uiShow()


#
def helpShow():
    helpDirectory = pipePr.mayaHelpDirectory('asset')
    lxBasic.setOsFolderOpen(helpDirectory)
