# coding=utf-8
import collections, threading
#
from LxBasic import bscMethods, bscObjects
#
from LxCore import lxConfigure
#
from LxCore.config import appCfg

from LxPreset import prsVariants, prsMethods
#
from LxCore.preset.prod import projectPr, assetPr
#
from LxUi.qt import qtWidgets_, qtWidgets, qtCore
#
from LxInterface.qt.qtIfBasic import _qtIfAbcWidget
#
from LxDatabase import dbGet
#
from LxMaya.command import maUtils, maFile, maUuid, maAttr, maGeom, maShdr, maHier, maFur, maRender
#
from LxMaya.product.data import datAsset
#
from LxMaya.product.op import assetOp
#
from LxMaya.product import maAstUploadCmds
#
from LxMaya.product import maAstLoadCmds
#
from LxMaya.interface.ifCommands import maAstTreeViewCmds
#
from LxMaya.database import maDbAstCmds
#
astYetiNodeGroupLabel = prsVariants.Util.astYetiNodeGroupLabel
astYetiGroomGroupLabel = prsVariants.Util.astYetiGroomGroupLabel
astYetiGrowGroupLabel = prsVariants.Util.astYetiGrowGroupLabel
astYetiReferenceGroupLabel = prsVariants.Util.astYetiReferenceGroupLabel
#
none = ''


#
class IfAstModelCharToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Model
    ]
    UnitClassLimit = [
        prsMethods.Asset.characterCategory()
    ]
    UnitTitle = 'Model ( Character ) Tool Unit'
    UnitIcon = 'window#charToolPanel'
    UnitTooltip = u'''模型角色工具模块'''
    def __init__(self, *args, **kwargs):
        super(IfAstModelCharToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.initToolBox()
        self.setupUnitWidgets()
    #
    def refreshMethod(self):
        if self.connectObject():
            if prsMethods.Asset.isModelStageName(self.connectObject().assetStage):
                if prsMethods.Asset.isCharacterCategory(self.connectObject().assetCategory):
                    self._initObjectPathDic()
                    #
                    self._updateBtnStateCmd()
    #
    def _initButtonDic(self):
        # Upper
        self.dicUp = {
            'headAss': [1, 0, 2, 1, 1, 'Head\r\nAss'],
            'hair': [1, 1, 2, 1, 1, 'Hair'],
            'head': [4, 2, 2, 5, 1, 'Head'],
            'R_brow': [0, 2, 1, 1, 1, 'Brow'],
            'L_brow': [0, 2, 3, 1, 1, 'Brow'],
            'R_upLash': [0, 3, 1, 1, 1, 'Lash'],
            'L_upLash': [0, 3, 3, 1, 1, 'Lash'],
            'R_eyeIn': [0, 4, 1, 1, 1, 'Eye-In'],
            'R_eyeOut': [0, 5, 1, 1, 1, 'Eye-Out'],
            'L_eyeIn': [0, 4, 3, 1, 1, 'Eye-In'],
            'L_eyeOut': [0, 5, 3, 1, 1, 'Eye-Out'],
            'R_ear': [0, 4, 0, 1, 1, 'Ear'],
            'R_earring': [0, 5, 0, 1, 1, 'Earring'],
            'L_ear': [0, 4, 4, 1, 1, 'Ear'],
            'L_earring': [0, 5, 4, 1, 1, 'Earring'],
            'R_tearGland': [0, 6, 1, 1, 1, 'Tear-Gland'],
            'L_tearGland': [0, 6, 3, 1, 1, 'Tear-Gland'],
            'R_lowLash': [0, 7, 1, 1, 1, 'Lash'],
            'L_lowLash': [0, 7, 3, 1, 1, 'Lash'],
            'upTeeth': [0, 7, 2, 1, 1, 'Teeth'],
            'tongue': [0, 8, 2, 1, 1, 'Tongue'],
            'lowTeeth': [0, 9, 2, 1, 1, 'Teeth'],
            'beard': [0, 10, 2, 1, 1, 'Beard'],
            'openEye': [1, 10, 0, 2, 1, 'Open\r\nEye'],
            'closeEye': [1, 10, 4, 2, 1, 'Close\r\nEye']
        }
        # Lower
        self.dicDown = {
            'bodyAss': [1, 0, 2, 1, 1, 'Body\r\nAss'],
            'upCloth': [1, 1, 2, 1, 1, 'Cloth\r\nUpper'],
            'body': [1, 2, 2, 1, 1, 'Body'],
            'R_arm': [1, 1, 1, 1, 1, 'Arm'],
            'L_arm': [1, 1, 3, 1, 1, 'Arm'],
            'R_hand': [1, 1, 0, 1, 1, 'Hand'],
            'L_hand': [1, 1, 4, 1, 1, 'Hand'],
            'R_glove': [1, 2, 0, 1, 1, 'Glove'],
            'L_glove': [1, 2, 4, 1, 1, 'Glove'],
            'lowCloth': [1, 3, 2, 1, 1, 'Cloth\r\nLower'],
            'R_leg': [1, 4, 1, 1, 1, 'Leg'],
            'L_leg': [1, 4, 3, 1, 1, 'Leg'],
            'R_foot': [1, 5, 1, 1, 1, 'Foot'],
            'L_foot': [1, 5, 3, 1, 1, 'Foot'],
            'R_shoe': [1, 6, 1, 1, 1, 'Shoe'],
            'L_shoe': [1, 6, 3, 1, 1, 'Shoe']
        }
    #
    def _initObjectPathDic(self):
        self._objectPathDic.clear()
        if self.connectObject() is not None:
            assetName = self.connectObject().assetName
            #

            hierarchyData = assetPr.astModelCharHierarchyConfig(assetName)
            dic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
            self._objectPathDic.update(dic)
            #
            subHierarchyData = assetPr.astModelSolverHierarchyConfig(assetName)
            subDic = bscMethods.MayaPath.covertToPathCreateDic(subHierarchyData)
            self._objectPathDic.update(subDic)
    #
    def setupUpToolUiBox(self, toolBox):
        uiData = self.dicUp
        self._setupToolUiBoxMethod(uiData, toolBox, self._buttonDic)
    #
    def setupDownToolUiBox(self, toolBox):
        uiData = self.dicDown
        self._setupToolUiBoxMethod(uiData, toolBox, self._buttonDic)
    #
    def _setupToolUiBoxMethod(self, uiData, toolBox, dic):
        def setBranch(key, ui):
            def command():
                addGeometryObjectCmd(key)
            #
            ui.clicked.connect(command)
            ui.clicked.connect(self._updateBtnStateCmd)
            toolBox.setButton(uiData, k, ui)
        #
        def addGeometryObjectCmd(keyword):
            if self.connectObject() is not None:
                assetName = self.connectObject().assetName
                #
                parentName = assetPr.astBasicGroupNameSet(assetName, '_' + keyword)
                parentPath = None
                if parentName in self._objectPathDic:
                    parentPath = self._objectPathDic[parentName]
                    if not maUtils.isAppExist(parentPath):
                        objectPathLis = maUtils.getSelectedNodeLis()
                        maUtils.setAppPathCreate(parentPath)
                        maUtils.setNodeSelect(objectPathLis)
                #
                maHier.addHierarchyObject(
                    parentPath,
                    assetName,
                    [appCfg.MaNodeType_Mesh, appCfg.MaNodeType_NurbsSurface, appCfg.MaNodeType_NurbsCurve]
                )
                #
                self.connectObject().setAstHierarchyView()
                self.connectObject().astHierarchyToggleButton.setChecked(True)
        #
        for k, v in uiData.items():
            button = qtWidgets.QtPressbutton()
            button.setTextAlignment(qtCore.QtCore.Qt.AlignHCenter | qtCore.QtCore.Qt.AlignVCenter)
            size = v[0]
            button.setMinimumHeight(20 + 22 * size)
            button.setMaximumHeight(20 + 22 * size)
            dic[k] = button
            # button.setSize(size)
            setBranch(k, button)
    #
    def _updateBtnStateCmd(self):
        assetName = self.connectObject().assetName
        #
        uiData = self._buttonDic
        for k, v in uiData.items():
            keyword = '_' + k
            button = v
            groupName = assetPr.astBasicGroupNameSet(assetName, keyword)
            if groupName in self._objectPathDic:
                groupPath = self._objectPathDic[groupName]
                #
                boolean = maUtils.isAppExist(groupPath)
                button._setQtPressStatus([qtCore.OffStatus, qtCore.NormalStatus][boolean])
                if boolean is True:
                    childObjects = maUtils.getObjectChildObjects(
                        groupName,
                        [appCfg.MaNodeType_Mesh, appCfg.MaNodeType_NurbsSurface, appCfg.MaNodeType_NurbsCurve],
                        fullPath=1
                    )
                    subBoolean = len(childObjects) > 0
                    button._setQtPressStatus([qtCore.NormalStatus, qtCore.OnStatus][subBoolean])
                    if subBoolean is True:
                        childNames = [maUtils._toNodeName(i) for i in childObjects]
                        button.setTooltip('\r\n'.join(childNames[:10]))
                    elif subBoolean is False:
                        button.setTooltip(u'点击加入当前组（ %s ）' % groupName)
                elif boolean is False:
                    button.setTooltip(u'点击创建当前组（ %s ）' % groupName)
    #
    def initToolBox(self):
        self._buttonDic = {}
        self._objectPathDic = {}
        #
        self._initButtonDic()
    #
    def setupUnitWidgets(self):
        self._upToolUiBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._upToolUiBox)
        self._upToolUiBox.setTitle('Upper Body')
        self._upToolUiBox.setBackground(
            qtCore.iconRoot() + '/utils/modelArrangeUp.png',
            360, 300
        )
        self.setupUpToolUiBox(self._upToolUiBox)
        #
        self._downToolUiBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._downToolUiBox)
        self._downToolUiBox.setTitle('Lower Body')
        self._downToolUiBox.setBackground(
            qtCore.iconRoot() + '/utils/modelArrangeLow.png',
            360, 300
        )
        self.setupDownToolUiBox(self._downToolUiBox)


#
class IfAstModelToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Model
    ]
    UnitTitle = 'Model Tool Unit'
    UnitIcon = 'window#modelToolPanel'
    UnitTooltip = u'''模型工具模块'''
    #
    widthSet = 400
    # Model Utilities Tool
    ToolLayoutDic_AstModelRepair = dict(
        withTransformation=[1, 0, 0, 1, 2, 'Transformation'], repairUnlockNormal=[1, 0, 2, 1, 2, 'Unlock Normal'],
        repairHistory=[1, 1, 0, 1, 2, 'History'], repairSoftNormal=[1, 1, 2, 1, 2, 'Soft Normal'],
        repairUv=[1, 2, 0, 1, 2, 'Uv ( Map )'],
        astRepairMesh=[1, 3, 0, 1, 4, 'Repair Mesh', 'svg_basic@svg#mesh'],
        # 4
        withMaterial=[1, 5, 0, 1, 2, 'Material'], withTexture=[1, 5, 2, 1, 2, 'Texture'],
        withAov=[1, 6, 0, 1, 2, 'AOV'],
        repairShader=[1, 7, 0, 1, 4, 'Repair Nde_ShaderRef', 'svg_basic@svg#shader']
    )
    #
    ToolLayoutDic_AstModelUtils = {
        'addSolverHierarchy': [1, 0, 0, 1, 2, 'Add Solver Hierarchy', 'svg_basic@svg#addTab'], 'addReferenceHierarchy': [1, 0, 2, 1, 2, 'Add Reference Hierarchy', 'svg_basic@svg#addTab'],
        # 1
        'collectionReferenceObject': [1, 2, 0, 1, 4, 'Collection Reference Object(s)', 'svg_basic@svg#addTab']
    }
    def __init__(self, *args, **kwargs):
        super(IfAstModelToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnitWidgets()
    #
    def refreshMethod(self):
        if self.connectObject() is not None:
            if prsMethods.Asset.isModelStageName(self.connectObject().assetStage):
                pass
            self.connectObject().withTransformationButton = self.withTransformationButton
            self.connectObject().withHistoryButton = self.withHistoryButton
            self.connectObject().withUnlockNormalButton = self.withUnlockNormalButton
            self.connectObject().withSoftNormalButton = self.withSoftNormalButton
            self.connectObject().withUvButton = self.withUvButton
            #
            self.connectObject().withMaterialButton = self.withMaterialButton
            self.connectObject().withTextureButton = self.withTextureButton
            self.connectObject().withAovButton = self.withAovButton
            #
            self.setAddSubGrpBtnState()
    #
    def setupAstModelRepairToolUiBox(self, toolBox):
        inData = self.ToolLayoutDic_AstModelRepair
        #
        self.withTransformationButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withTransformation', self.withTransformationButton)
        self.withTransformationButton.setChecked(True)
        self.withTransformationButton.setTooltip(
            u'''1. Clean Mesh's Transformation Keyframe\r\n2. Unlock Mesh's Transformation\r\n3. Freeze and Rest Mesh's Transformation'''
        )
        #
        self.withUnlockNormalButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'repairUnlockNormal', self.withUnlockNormalButton)
        self.withUnlockNormalButton.setTooltip(
            u'''1. Unlock Mesh's Normal'''
        )
        self.withSoftNormalButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'repairSoftNormal', self.withSoftNormalButton)
        self.withSoftNormalButton.setTooltip(
            u'''1. Soft ( Smooth ) Mesh's Edge'''
        )
        #
        self.withUvButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'repairUv', self.withUvButton)
        self.withUvButton.setChecked(True)
        self.withUvButton.setTooltip(
            u'''1. Repair Mesh's Uv ( Map )'''
        )
        #
        self.withHistoryButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'repairHistory', self.withHistoryButton)
        self.withHistoryButton.setChecked(True)
        self.withHistoryButton.setTooltip(
            u'''1. Clean Mesh's History'''
        )
        #
        self._modelMeshRepairButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'astRepairMesh', self._modelMeshRepairButton)
        self._modelMeshRepairButton.clicked.connect(self.setRepairMeshCmd)
        #
        self.withMaterialButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withMaterial', self.withMaterialButton)
        self.withMaterialButton.setChecked(True)
        self.withMaterialButton.setTooltip(
            u'''1. Repair Material's Object - Set\r\n2. Repair Material's Color - Space ( Texture Nde_Node )'''
        )
        #
        self.withTextureButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withTexture', self.withTextureButton)
        self.withTextureButton.setTooltip(
            u'''1. Repair Texture's Tx ( Arnold )'''
        )
        #
        self.withAovButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withAov', self.withAovButton)
        self.withAovButton.setChecked(True)
        self.withAovButton.setTooltip(
            u'''1. Repair AOV's Driver and Filter ( Arnold )\r\n2. Repair AOV's Option ( Arnold )'''
        )
        #
        self._modelShaderRepairButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'repairShader', self._modelShaderRepairButton)
        self._modelShaderRepairButton.clicked.connect(self.setRepairShaderCmd)
        #
        toolBox.setSeparators(inData)
    #
    def setupAstModelUtilsToolUiBox(self, toolBox):
        inData = self.ToolLayoutDic_AstModelUtils
        #
        self._addModelSolverHierarchyButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'addSolverHierarchy', self._addModelSolverHierarchyButton)
        self._addModelSolverHierarchyButton.clicked.connect(self.setAddSolverHierarchyCmd)
        #
        self._addModelReferenceHierarchyButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'addReferenceHierarchy', self._addModelReferenceHierarchyButton)
        self._addModelReferenceHierarchyButton.clicked.connect(self.setAddReferenceHierarchyCmd)
        #
        self._collectionReferenceObjectButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'collectionReferenceObject', self._collectionReferenceObjectButton)
        self._collectionReferenceObjectButton.clicked.connect(self.setCollectionReferenceObjectCmd)
        #
        toolBox.setSeparators(inData)
    #
    def setAddSolverHierarchyCmd(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        maHier.setCreateAstUnitModelSolverHierarchy(assetCategory, assetName)
        #
        self.setAddSubGrpBtnState()
    #
    def setAddReferenceHierarchyCmd(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        maHier.setCreateAstUnitModelReferenceHierarchy(assetCategory, assetName)
        #
        self.setAddSubGrpBtnState()
    #
    def setCollectionReferenceObjectCmd(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        astUnitModelReferenceGroup = assetPr.astUnitModelReferenceGroupName(assetName)
        if not maUtils.isAppExist(astUnitModelReferenceGroup):
            self.setAddReferenceHierarchyCmd()
        #
        meshPathLis = datAsset.getAstMeshObjects(assetName)
        #
        lis = []
        #
        for meshPath in meshPathLis:
            referenceObject = maGeom.getMeshReferenceObject(meshPath)
            if referenceObject:
                lis.append(referenceObject)
        #
        if lis:
            [maUtils.setObjectParent(i, astUnitModelReferenceGroup) for i in lis]
    #
    def setAddSubGrpBtnState(self):
        pass
    #
    def setRepairMeshCmd(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        meshObjects = datAsset.getAstMeshObjects(assetName, 0)
        if meshObjects:
            isRepairWithTrans = self.withTransformationButton.isChecked()
            isRepairWithHistory = self.withHistoryButton.isChecked()
            isRepairWithUnlockNormal = self.withUnlockNormalButton.isChecked()
            isRepairWithSoftNormal = self.withSoftNormalButton.isChecked()
            isRepairWithUv = self.withUvButton.isChecked()
            #
            maAstUploadCmds.astUnitMeshRepairCmd_(
                assetName,
                repairTrans=isRepairWithTrans, repairHistory=isRepairWithHistory,
                repairUnlockNormal=isRepairWithUnlockNormal,
                repairSoftNormal=isRepairWithSoftNormal,
                repairUv=isRepairWithUv
            )
            #
            self.withUnlockNormalButton.setChecked(False)
            #
            bscObjects.If_Message(
                u'修复模型', u'成功'
            )
    #
    def setRepairShaderCmd(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        meshObjects = datAsset.getAstMeshObjects(assetName, 0)
        if meshObjects:
            isRepairWithMaterial = self.withMaterialButton.isChecked()
            isRepairWithTexture = self.withTextureButton.isChecked()
            isRepairWithAov = self.withAovButton.isChecked()
            #
            maAstUploadCmds.astUnitShaderRepairCmd_(
                assetName,
                repairMatl=isRepairWithMaterial, repairTexture=isRepairWithTexture, repairAov=isRepairWithAov
            )
            #
            self.withTextureButton.setChecked(False)
            #
            bscObjects.If_Message(
                u'修复材质', u'成功'
            )
    #
    def setupUnitWidgets(self):
        self._repairToolBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._repairToolBox)
        self._repairToolBox.setTitle('Asset Model Repair')
        self.setupAstModelRepairToolUiBox(self._repairToolBox)
        #
        self._utilitiesToolBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._utilitiesToolBox)
        self._utilitiesToolBox.setTitle('Asset Model Utilities')
        self.setupAstModelUtilsToolUiBox(self._utilitiesToolBox)


#
class IfAstRigToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Rig
    ]
    UnitTitle = 'Rig Tool Unit'
    UnitIcon = 'window#rigToolPanel'
    UnitTooltip = u'''绑定工具模块'''
    #
    widthSet = 400
    #
    _groupCreateTip = u'''提示：请输入名字...'''
    # Graph
    def __init__(self, *args, **kwargs):
        super(IfAstRigToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.setupUnitWidgets()
    #
    def refreshMethod(self):
        if self.connectObject() is not None:
            pass
    #
    def setupAstRigGraphToolUiBox(self, toolBox):
        pass
    #
    def setupUnitWidgets(self):
        toolBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(toolBox)
        toolBox.setTitle('Asset ( Rig ) Graph')
        #
        self.setupAstRigGraphToolUiBox(toolBox)


#
class IfAstCfxGroomToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Groom,
        lxConfigure.LynxiProduct_Asset_Link_Solver
    ]
    UnitTitle = 'Character FX Tool Unit'
    UnitIcon = 'window#cfxToolPanel'
    UnitTooltip = u'''角色特效工具模块'''
    #
    UnitScriptJobWindowName = 'astCfxToolScriptJobWindow'
    #
    widthSet = 400
    # Tips
    addNodeTips = u'''提示：选择一个"Yeti / Pfx Hair / Nurbs Hair Nde_Node"...'''
    addNodeSubTips1 = u'''提示：点击"Add Nde_Node"添加...'''
    addNodeSubTips2 = u'''提示：输入"Nde_Node Name "...'''
    nodeNameTips1 = u'''错误：输入"Nde_Node Name"已经存...'''
    nodeNameTips2 = u'''错误：输入的"Nde_Node Name"超过12个字符...'''
    createGrowSourceTips = u'''提示：选择一个"Mesh"...'''
    createGrowSourceSubTips1 = u'''提示：点击"Create Source"创建...'''
    createGrowSourceSubTips2 = u'''错误：选择的"Mesh"已经存"Grow Source"...'''
    # CFX Graph Tool
    ToolLayoutDic_AstCfxGraph = dict(
        deleteHistory=[0, 0, 0, 1, 2, 'Delete History ( Local Curve )'], updateHierarchy=[0, 0, 2, 1, 2, 'Update Hierarchy'],
        childNode=[0, 1, 0, 1, 3, u'Nde_Node ( Yeti / Pfx Hair / Nurbs Hair )...'], addNode=[0, 1, 3, 1, 1, 'Add Nde_Node', 'svg_basic@svg#addTab'],
        # 2
        nodeName=[0, 3, 0, 1, 4, 'Nde_Node Name'],
        tips=[0, 4, 0, 1, 4, none],
        # 5
        placeholder=[0, 6, 0, 1, 4, 'Placeholder']
    )
    # CFX Utilities Tool
    ToolLayoutDic_AstCfxUtils = dict(
        growSourceSearch=[0, 0, 0, 1, 2, none], createGrowSource=[0, 0, 2, 1, 2, 'Create Source ( Grow )', 'svg_basic@svg#addTab'],
        tips=[0, 1, 0, 1, 4, none],
        # 2
        placeholder=[1, 3, 0, 1, 4, 'Placeholder'],
        # 4
        addGrowTarget=[1, 5, 0, 1, 2, 'Add Target', 'svg_basic@svg#addTab'], addGrowDeform=[1, 5, 2, 1, 2, 'Add Deform', 'svg_basic@svg#addTab'],
        addCollision=[1, 6, 0, 1, 4, 'Add Collision', 'svg_basic@svg#addTab']
    )
    def __init__(self, *args, **kwargs):
        super(IfAstCfxGroomToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._astCfxFurObjectDic = {}
        self._astModelGeometryObjectDic = {}
        #
        self.setupUnitWidgets()
    #
    def refreshMethod(self):
        if self.connectObject() is not None:
            if prsMethods.Asset.isGroomStageName(self.connectObject().assetStage):
                self._astCfxHirToolUiBox.show()
                self._astCfxUtilsToolUiBox.show()
                #
                self.setListAstCfxFur()
                self.setListAstModelGeometryObjects()
                #
                self.setScriptJob()
            elif prsMethods.Asset.isSolverStageName(self.connectObject().assetStage):
                self._astCfxUtilsToolUiBox.show()
                #
                self.setListAstModelGeometryObjects()
                #
                self.setScriptJob()
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methods = [self.setRefreshTreeViewBoxSelection]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        scriptJobEvn = 'NameChanged'
        methods = [self.setRefreshTreeViewBoxSelection]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        # #
        # scriptJobEvn = 'DagObjectCreated'
        # methods = [self.setListTreeItem, self.setRefreshTreeViewBoxSelection]
        # maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupAstCfxGraphToolUiBox(self, toolBox):
        def setSelObject():
            data = self._astCfxFurObjectsTreeViewBox.selectedItemPaths()
            if data:
                maUtils.setNodeSelect(data)
            else:
                pass
        #
        self.yetiObjects = []
        self.pfxHairObjects = []
        #
        inData = self.ToolLayoutDic_AstCfxGraph
        #
        self._nodeFullNameUiLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'childNode', self._nodeFullNameUiLabel)
        #
        self._addNodeButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'addNode', self._addNodeButton)
        self._addNodeButton.setPressable(False)
        self._addNodeButton.setTooltip('Add Nde_Node ( Yeti / pfxHair ) to Group')
        self._addNodeButton.clicked.connect(self.setAddAstCfxFur)
        #
        self._furNodeKeywordEntryLabel = qtWidgets.QtEnterlabel()
        self._furNodeKeywordEntryLabel.setNameText(0)
        self._furNodeKeywordEntryLabel.setTextValidator(24)
        self._furNodeKeywordEntryLabel.setEnterEnable(True)
        self._furNodeKeywordEntryLabel.setEnterable(True)
        toolBox.setInfo(inData, 'nodeName', self._furNodeKeywordEntryLabel)
        self._furNodeKeywordEntryLabel.entryChanged.connect(self.setAstFurNodeName)
        self._furNodeKeywordEntryLabel.entryChanged.connect(self.setAddNodeBtnState)
        #
        self._addNFurNodeTipLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'tips', self._addNFurNodeTipLabel)
        self._addNFurNodeTipLabel.setDatum(self.addNodeTips)
        #
        self.updateHierarchyButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'updateHierarchy', self.updateHierarchyButton)
        self.updateHierarchyButton.setChecked(True)
        #
        self.deleteHistoryButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'deleteHistory', self.deleteHistoryButton)
        self.deleteHistoryButton.setChecked(True)
        #
        self._astCfxFurObjectsTreeViewBox = qtWidgets_.QTreeWidget_()
        toolBox.addWidget(self._astCfxFurObjectsTreeViewBox, 6, 0, 1, 4)
        self._astCfxFurObjectsTreeViewBox.setColumns(['Nde_Node', 'Nde_Node Type'], [4, 1], self.widthSet - 60)
        self._astCfxFurObjectsTreeViewBox.itemSelectionChanged.connect(setSelObject)
        self._astCfxFurObjectsTreeViewBox.itemSelectionChanged.connect(self.setAddNodeBtnState)
        self._astCfxFurObjectsTreeViewBox.itemSelectionChanged.connect(self.setAstFurNodeName)
        #
        toolBox.setSeparators(inData)
    #
    def setupAstCfxUtilsToolUiBox(self, toolBox):
        def setSelObject():
            data = self._astModelGeometryObjectTreeViewBox.selectedItemPaths()
            if data:
                maUtils.setNodeSelect(data)
            else:
                pass
        #
        self.growSourceSearchDic = {}
        #
        inData = self.ToolLayoutDic_AstCfxUtils
        #
        self._astModelGeometryFilterLabel = qtWidgets.QtFilterEnterlabel()
        toolBox.setButton(inData, 'growSourceSearch', self._astModelGeometryFilterLabel)
        #
        self.createGrowSourceButton = qtWidgets.QtPressbutton()
        self.createGrowSourceButton.setPressable(False)
        toolBox.setButton(inData, 'createGrowSource', self.createGrowSourceButton)
        self.createGrowSourceButton.setTooltip('Create Grow ( Mesh ) Source')
        self.createGrowSourceButton.clicked.connect(self.astCreateGrowSourceCmd)
        #
        self._growSourceCreateTipLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'tips', self._growSourceCreateTipLabel)
        self._growSourceCreateTipLabel.setDatum(self.createGrowSourceTips)
        #
        self._astModelGeometryObjectTreeViewBox = qtWidgets_.QTreeWidget_()
        toolBox.addWidget(self._astModelGeometryObjectTreeViewBox, 3, 0, 1, 4)
        self._astModelGeometryObjectTreeViewBox.setSingleSelection()
        self._astModelGeometryObjectTreeViewBox.setColumns(['Nde_Node', 'Nde_Node Type'], [4, 1], self.widthSet - 60)
        self._astModelGeometryObjectTreeViewBox.itemSelectionChanged.connect(setSelObject)
        self._astModelGeometryObjectTreeViewBox.itemSelectionChanged.connect(self.setGrowSourceName)
        self._astModelGeometryObjectTreeViewBox.setFilterConnect(self._astModelGeometryFilterLabel)
        #
        self.addGrowTargetButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'addGrowTarget', self.addGrowTargetButton)
        self.addGrowTargetButton.clicked.connect(self.astAddGrowTargetCmd)
        #
        self.addGrowDeformButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'addGrowDeform', self.addGrowDeformButton)
        self.addGrowDeformButton.clicked.connect(self.astAddGrowDeformCmd)
        #
        self.addCollisionButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'addCollision', self.addCollisionButton)
        self.addCollisionButton.clicked.connect(self.astAddGrowCollisionCmd)
        #
        toolBox.setSeparators(inData)
    # Yeti Tree
    def setListAstCfxFur(self):
        def setListAstFurYeti(inData):
            for yetiObjectPath in inData:
                yetiObjectName = maUtils._toNodeName(yetiObjectPath)
                yetiItem = qtWidgets_.QTreeWidgetItem_([yetiObjectName, 'Yeti'])
                yetiItem.name = yetiObjectName
                yetiItem.path = yetiObjectPath
                yetiItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_Yeti)
                #
                yetiObjectGroup = assetPr.astBasicGroupNameSet(assetName, astYetiNodeGroupLabel)
                if maUtils.isChild(yetiObjectGroup, yetiObjectPath):
                    yetiItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_Yeti, 'off')
                #
                if not maUtils.isAppExist(yetiObjectPath):
                    yetiItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_Yeti, 'error')
                #
                groomObjects = maUtils.getYetiGroomDic(yetiObjectPath)
                if groomObjects:
                    for groomObject in groomObjects:
                        groomItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(groomObject), 'Groom'])
                        groomItem.setItemMayaIcon(0, appCfg.MaNodeType_YetiGroom)
                        #
                        groomObjectGroup = assetPr.astBasicGroupNameSet(assetName, astYetiGroomGroupLabel)
                        if maUtils.isChild(groomObjectGroup, groomObject):
                            groomItem.setItemMayaIcon(0, appCfg.MaNodeType_YetiGroom, 'off')
                        #
                        if not maUtils.isAppExist(groomObject):
                            groomItem.setItemMayaIcon(0, appCfg.MaNodeType_YetiGroom, 'error')
                            #
                            yetiItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_Yeti, 'error')
                            yetiItem.setExpanded(True)
                        #
                        yetiItem.addChild(groomItem)
                # Grow Object
                growObjects = maUtils.getYetiGrowDic(yetiObjectPath)
                if growObjects:
                    for growObject in growObjects:
                        growItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(growObject), 'Grow'])
                        growItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
                        #
                        growObjectGroup = assetPr.astBasicGroupNameSet(assetName, astYetiGrowGroupLabel)
                        if maUtils.isChild(growObjectGroup, growObject):
                            growItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'off')
                        #
                        if not maUtils.isAppExist(growObject):
                            growItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'error')
                            yetiItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_Yeti, 'error')
                            #
                            yetiItem.setExpanded(True)
                        #
                        yetiItem.addChild(growItem)
                        # Reference Object
                        referenceObjects = maUtils.getYetiRefObject(growObject)
                        if referenceObjects:
                            for referenceObject in referenceObjects:
                                referenceItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(referenceObject), 'Reference'])
                                referenceItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh)
                                #
                                referenceObjectGroup = assetPr.astBasicGroupNameSet(assetName, astYetiReferenceGroupLabel)
                                if maUtils.isChild(referenceObjectGroup, referenceObject):
                                    referenceItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'off')
                                #
                                growItem.addChild(referenceItem)
                #
                guideSystemData = []
                guideNucleusData = []
                guideData = maUtils.getYetiGuideData(yetiObjectPath)
                if guideData:
                    guideSystemGroup = assetPr.guideSystemGroupName(assetName)
                    #
                    follicleGroup = assetPr.guideFollicleGroupName(assetName)
                    #
                    guideCurveGroup = assetPr.guideCurveGroupName(assetName)
                    for guideSet, data in guideData.items():
                        setCheck = True
                        guideSetItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(guideSet), 'Set'])
                        guideSetItem.setItemMayaIcon(0, 'list')
                        yetiItem.addChild(guideSetItem)
                        for k, v in data.items():
                            guideCurve = k
                            #
                            guideCurveItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(guideCurve), 'Guide Curve'])
                            guideCurveItem.setItemMayaIcon(0, appCfg.MaNodeType_NurbsCurve)
                            #
                            if maUtils.isChild(guideCurveGroup, guideCurve):
                                guideCurveItem.setItemMayaIcon(0, appCfg.MaNodeType_NurbsCurve, 'off')
                            #
                            if not maUtils.isChild(guideCurveGroup, guideCurve):
                                setCheck = False
                            #
                            guideSetItem.addChild(guideCurveItem)
                            #
                            follicle, localCurve, hairSystem, nucleus = v
                            #
                            if follicle:
                                follicleItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(follicle), 'Follicle'])
                                follicleItem.setItemMayaIcon(0, appCfg.MaFollicleType)
                                guideCurveItem.addChild(follicleItem)
                                #
                                if maUtils.isChild(follicleGroup, follicle):
                                    follicleItem.setItemMayaIcon(0, appCfg.MaFollicleType, 'Off')
                                #
                                if not maUtils.isChild(follicleGroup, follicle):
                                    setCheck = False
                            #
                            if localCurve:
                                localCurveItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(localCurve), 'Local Curve'])
                                localCurveItem.setItemMayaIcon(0, appCfg.MaNodeType_NurbsCurve)
                                guideCurveItem.addChild(localCurveItem)
                                #
                                if maUtils.isChild(follicleGroup, localCurve):
                                    localCurveItem.setItemMayaIcon(0, appCfg.MaNodeType_NurbsCurve, 'Off')
                                #
                                if not maUtils.isChild(follicleGroup, localCurve):
                                    setCheck = False
                            #
                            if hairSystem:
                                guideSystemData.append(hairSystem)
                            #
                            if nucleus:
                                guideNucleusData.append(nucleus)
                        #
                        if guideSystemData:
                            guideSystems = maUtils.getReduceList(guideSystemData)
                            for guideSystem in guideSystems:
                                guideSystemItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(guideSystem), 'System'])
                                guideSystemItem.setItemMayaIcon(0, appCfg.MaHairSystemType)
                                guideSetItem.addChild(guideSystemItem)
                                #
                                if maUtils.isChild(guideSystemGroup, guideSystem):
                                    guideSystemItem.setItemMayaIcon(0, appCfg.MaHairSystemType, 'off')
                                #
                                if not maUtils.isChild(guideSystemGroup, guideSystem):
                                    setCheck = False
                        #
                        if guideNucleusData:
                            guideNuclei = maUtils.getReduceList(guideNucleusData)
                            for guideNucleus in guideNuclei:
                                guideNucleusItem = qtWidgets_.QTreeWidgetItem_([maUtils._toNodeName(guideNucleus), 'Nucleus'])
                                guideNucleusItem.setItemMayaIcon(0, appCfg.MaNucleusType)
                                guideSetItem.addChild(guideNucleusItem)
                                #
                                if maUtils.isChild(guideSystemGroup, guideNucleus):
                                    guideNucleusItem.setItemMayaIcon(0, appCfg.MaNucleusType, 'Off')
                                #
                                if not maUtils.isChild(guideSystemGroup, guideNucleus):
                                    setCheck = False
                        #
                        if setCheck:
                            guideSetItem.setItemMayaIcon(0, 'list', 'off')
                #
                treeBox.addItem(yetiItem)
                #
                self.yetiObjects.append(yetiObjectPath)
        #
        def setListAsrFurPfx(inData):
            def listBranch(objects, rootItem, explain, nodeType, objectGroup=False, subRootItem=False):
                notInGroup = []
                if subRootItem:
                    subRootItem = qtWidgets_.QTreeWidgetItem_([explain, 'Nodes'])
                    subRootItem.setItemMayaIcon(0, 'list')
                    rootItem.addChild(subRootItem)
                for maObj in objects:
                    showObject = maUtils._toNodeName(maObj)
                    objectItem = qtWidgets_.QTreeWidgetItem_([showObject, explain])
                    objectItem.setItemMayaIcon(0, nodeType)
                    if subRootItem:
                        subRootItem.addChild(objectItem)
                    elif not subRootItem:
                        rootItem.addChild(objectItem)
                    if objectGroup:
                        boolean = maUtils.isChild(objectGroup, maObj)
                        objectItem.setItemMayaIcon(0, nodeType, [none, 'off'][boolean])
                        if not boolean:
                            notInGroup.append(objectItem)
                if subRootItem:
                    subRootBoolean = notInGroup == []
                    subRootItem.setItemMayaIcon(0, 'list', [none, 'off'][subRootBoolean])
            #
            maxValue = len(inData)
            for seq, pfxHairObjectPath in enumerate(inData):
                if self.connectObject() is not None:
                    self.connectObject().setProgressValue(seq + 1, maxValue)
                #
                pfxHairObjectName = maUtils._toNodeName(pfxHairObjectPath)
                pfxHairItem = qtWidgets_.QTreeWidgetItem_([pfxHairObjectName, 'Pfx Hair'])
                pfxHairItem.name = pfxHairObjectName
                pfxHairItem.path = pfxHairObjectPath
                pfxHairItem.setItemMayaIcon(0, appCfg.MaPfxHairType)
                #
                growObjects, shaders, textures, maps, systemObjects, nucleusObjects, follicleData = maUtils.getPfxHairConnectionData(
                    pfxHairObjectPath)
                # Grow
                if growObjects:
                    growGroup = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astPfxHairGrowGroupLabel)
                    listBranch(growObjects, pfxHairItem, 'Grow', 'poly', objectGroup=growGroup)
                # System
                if systemObjects:
                    systemGroup = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astPfxHairSolverNodeGroupLabel)
                    listBranch(systemObjects, pfxHairItem, 'System', 'hairSystem', objectGroup=systemGroup)
                # Nucleus
                if nucleusObjects:
                    nucleusGroup = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astPfxHairSolverNodeGroupLabel)
                    listBranch(nucleusObjects, pfxHairItem, 'Nucleus', 'nucleus', objectGroup=nucleusGroup)
                # Follicle
                if follicleData:
                    follicleObjects = []
                    localCurveObjects = []
                    outputCurveObjects = []
                    for follicleObject, (subLocalCurveObjects, subOutputCurveObjects) in follicleData.items():
                        follicleObjects.append(follicleObject)
                        localCurveObjects.extend(subLocalCurveObjects)
                        outputCurveObjects.extend(subOutputCurveObjects)
                    if follicleObjects:
                        follicleGroup = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astPfxHairFollicleGroupLabel)
                        listBranch(follicleObjects, pfxHairItem, 'Follicle', 'follicle', objectGroup=follicleGroup,
                                   subRootItem=True)
                    if localCurveObjects:
                        localCurveGroup = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astPfxHairFollicleGroupLabel)
                        listBranch(localCurveObjects, pfxHairItem, 'Local Curve', 'inputCurve',
                                   objectGroup=localCurveGroup, subRootItem=True)
                    if outputCurveObjects:
                        outputCurveGroup = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astPfxHairCurveGroupLabel)
                        listBranch(outputCurveObjects, pfxHairItem, 'Output Curve', 'outputCurve',
                                   objectGroup=outputCurveGroup, subRootItem=True)
                #
                treeBox.addItem(pfxHairItem)
                pfxHairGroup = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astPfxHairGroupLabel)
                boolean = maUtils.isChild(pfxHairGroup, pfxHairObjectPath)
                pfxHairItem.setItemMayaIcon(0, appCfg.MaPfxHairType, [none, 'off'][boolean])
                #
                self.pfxHairObjects.append(pfxHairObjectPath)
        #
        def setListAstFurNhr(inData):
            def setObjectBranch(objectPath, parentItem=None):
                objectName = maUtils._toNodeName(objectPath)
                objectType = maUtils.getShapeType(objectPath)
                objectUuid = maUuid.getNodeUniqueId(objectPath)
                #
                objectItem = qtWidgets_.QTreeWidgetItem_([objectName, objectType])
                stateLabel = none
                if astCfxRoot in objectPath:
                    stateLabel = 'off'
                objectItem.setItemMayaIcon(0, objectType, stateLabel)
                objectItem.name = objectName
                objectItem.path = objectPath
                objectItem.uuid = objectUuid
                if parentItem:
                    parentItem.addChild(objectItem)
                else:
                    treeBox.addItem(objectItem)
                return objectItem
            #
            def setMain():
                maxValue = len(inData)
                for seq, objectPath in enumerate(inData):
                    if self.connectObject():
                        self.connectObject().setProgressValue(seq + 1, maxValue)
                    #
                    parentItem = setObjectBranch(objectPath)
                    graphObjects, graphNodes, graphGrowGeometries, graphGuideGeometries = maFur.getNurbsHairConnectObjectData(objectPath)
                    #
                    needCollectionObjects = graphObjects
                    needCollectionObjects.extend(graphGrowGeometries)
                    needCollectionObjects.extend(graphGuideGeometries)
                    if needCollectionObjects:
                        for childObjectPath in needCollectionObjects:
                            setObjectBranch(childObjectPath, parentItem)
                    #
                    self.nurbsHairObjects.append(objectPath)
                    objectUuid = maUuid.getNodeUniqueId(objectPath)
                    self._astCfxFurObjectDic[objectUuid] = parentItem
            #
            setMain()
        #
        self.astFurNodeNameLabel = none
        self.nodeNameLabel = none
        #
        self.cfxObjects = []
        #
        self.yetiObjects = []
        self.pfxHairObjects = []
        self.nurbsHairObjects = []
        #
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        hierarchyData = assetPr.astCfxHierarchyConfig(assetName)
        self.pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
        #
        astCfxRoot = prsMethods.Asset.groomLinkGroupName(assetName)
        #
        treeBox = self._astCfxFurObjectsTreeViewBox
        #
        yetiObjects = maUtils.getYetiObjects()
        pfxHairObjects = maUtils.getPfxHairObjects()
        nurbsHairObjects = maFur.getNurbsHairObjects(True)
        #
        self._astCfxFurObjectDic.clear()
        treeBox.clear()
        if yetiObjects:
            setListAstFurYeti(yetiObjects)
        if pfxHairObjects:
            setListAsrFurPfx(pfxHairObjects)
        if nurbsHairObjects:
            setListAstFurNhr(nurbsHairObjects)
        #
        self.cfxObjects.extend(self.yetiObjects)
        self.cfxObjects.extend(self.pfxHairObjects)
        self.cfxObjects.extend(self.nurbsHairObjects)
    # Grow Tree
    def setListAstModelGeometryObjects(self):
        def setMain():
            meshObjectLis = datAsset.getAstMeshObjects(assetName, 1)
            if meshObjectLis:
                for meshObject in meshObjectLis:
                    meshObjectItem = maAstTreeViewCmds.setObjectBranch(self._astModelGeometryObjectDic, treeBox, meshObject)
                    meshName = maUtils._toNodeName(meshObject)
                    growSourceMesh = meshName + prsVariants.Util.astCfxGrowSourceGroupLabel
                    if maUtils.isAppExist(growSourceMesh):
                        meshObjectItem.setItemMayaIcon(0, appCfg.MaNodeType_Mesh, 'on')
        #
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        treeBox = self._astModelGeometryObjectTreeViewBox
        #
        setMain()
        #
        treeBox.setFilterExplainRefresh()
    #
    def setAddAstCfxFur(self):
        def setAddAstFurYeti(yetiObject, nodeLabel=none):
            yetiObjectName = nodeName
            yetiObjectShapeName = nodeName + appCfg.MaKeyword_Shape
            yetiObjectGroup = assetPr.astBasicGroupNameSet(assetName, astYetiNodeGroupLabel)
            #
            groomData = maUtils.getYetiGroomDic(yetiObject)
            # Use All Yeti Nde_Node's Data for Rebuild
            connectionData = maUtils.getYetiImportConnectionDic()
            #
            if groomData:
                for seq, groomObject in enumerate(groomData.keys()):
                    groomObjectName = yetiObjectName.replace(astYetiNodeGroupLabel, astYetiGroomGroupLabel) + '_' + str(seq + 1)
                    groomObjectShapeName = groomObjectName + appCfg.MaKeyword_Shape
                    groomObjectGroup = assetPr.astBasicGroupNameSet(assetName, astYetiGroomGroupLabel)
                    # Rename
                    maUtils.setNodeRename(groomObject, groomObjectName)
                    maUtils.setObjectShapeRename(groomObjectName, groomObjectShapeName)
                    maUtils.setObjectParent(groomObjectName, groomObjectGroup)
                    #
                    groomConnectionData = connectionData[groomObject]
                    # Repath Yeti Nde_Node Link
                    for i in groomConnectionData:
                        yetiNode, node = i
                        maUtils.setYetiNodeAttr(yetiNode, node, 'geometry', groomObjectShapeName)
                    # Hide
                    maUtils.setHide(groomObjectName)
            #
            growData = maUtils.getYetiGrowDic(yetiObject)
            if growData:
                for seq, growObject in enumerate(growData.keys()):
                    growObjectName = yetiObjectName.replace(astYetiNodeGroupLabel, astYetiGrowGroupLabel) + '_' + str(seq + 1)
                    growObjectShapeName = growObjectName + appCfg.MaKeyword_Shape
                    growObjectGroup = assetPr.astBasicGroupNameSet(assetName, astYetiGrowGroupLabel)
                    #
                    maUtils.setNodeRename(growObject, growObjectName)
                    maUtils.setObjectShapeRename(growObjectName, growObjectShapeName)
                    maUtils.setObjectParent(growObjectName, growObjectGroup)
                    #
                    growConnectionData = connectionData[growObject]
                    for i in growConnectionData:
                        yetiNode, node = i
                        maUtils.setYetiNodeAttr(yetiNode, node, 'geometry', growObjectShapeName)
                    #
                    maUtils.setNodeDefaultShader(growObjectName)
                    maUtils.setHide(growObjectName)
                    #
                    referenceObjects = maUtils.getYetiRefObject(growObjectName)
                    if referenceObjects:
                        for referenceObject in referenceObjects:
                            referenceObjectName = growObjectName.replace(astYetiGrowGroupLabel, astYetiReferenceGroupLabel)
                            referenceObjectShapeName = referenceObjectName + appCfg.MaKeyword_Shape
                            referenceObjectGroup = assetPr.astBasicGroupNameSet(assetName, astYetiReferenceGroupLabel)
                            #
                            maUtils.setNodeRename(referenceObject, referenceObjectName)
                            maUtils.setObjectShapeRename(referenceObjectName, referenceObjectShapeName)
                            maUtils.setObjectParent(referenceObjectName, referenceObjectGroup)
                            #
                            maUtils.setNodeDefaultShader(referenceObjectName)
                            maUtils.setHide(referenceObjectName)
            #
            guideSystemData = []
            guideNucleusData = []
            guideData = maUtils.getYetiGuideData(yetiObject)
            if guideData:
                cfxSetName = assetPr.cfxSetName(assetName)
                #
                guideSystemGroup = assetPr.guideSystemGroupName(assetName)
                #
                guideFollicleGroup = assetPr.guideFollicleGroupName(assetName)
                #
                guideFollicleSubGroup = yetiObjectName.replace(astYetiNodeGroupLabel, prsVariants.Util.astYetiGuideFollicleGroupLabel) + prsVariants.Util.basicGroupLabel
                #
                maUtils.setObjectAddChildGroup(guideFollicleSubGroup, guideFollicleGroup)
                #
                guideCurveGroup = assetPr.guideCurveGroupName(assetName)
                #
                guideCurveSubGroup = yetiObjectName.replace(astYetiNodeGroupLabel, prsVariants.Util.astYetiGuideCurveGroupLabel) + prsVariants.Util.basicGroupLabel
                #
                maUtils.setObjectAddChildGroup(guideCurveSubGroup, guideCurveGroup)
                #
                for seq, (guideSet, data) in enumerate(guideData.items()):
                    # Guide Set
                    guideSetName = yetiObjectName.replace(astYetiNodeGroupLabel, prsVariants.Util.astYetiGuideSetNodeLabel) + '_' + str(seq + 1)
                    #
                    maUtils.setNodeRename(guideSet, guideSetName)
                    maUtils.setElementSet(guideSetName, cfxSetName)
                    #
                    yetiGuideConnectionData = connectionData[guideSet]
                    #
                    for i in yetiGuideConnectionData:
                        yetiNode, node = i
                        maUtils.setYetiNodeAttr(yetiNode, node, 'geometry', guideSetName)
                    #
                    for subSeq, (k, v) in enumerate(data.items()):
                        guideCurve = k
                        #
                        guideCurveName = yetiObjectName.replace(
                            astYetiNodeGroupLabel,
                            prsVariants.Util.astYetiGuideOutputCurveNodeLabel
                        ) + '_' + str(seq + 1) + '_' + str(subSeq + 1)
                        guideCurveShapeName = guideCurveName + appCfg.MaKeyword_Shape
                        #
                        maUtils.setNodeRename(guideCurve, guideCurveName)
                        maUtils.setObjectShapeRename(guideCurveName, guideCurveShapeName)
                        maUtils.setObjectParent(guideCurveName, guideCurveSubGroup)
                        #
                        follicle, localCurve, hairSystem, nucleus = v
                        #
                        follicleName = yetiObjectName.replace(
                            astYetiNodeGroupLabel,
                            prsVariants.Util.astYetiGuideFollicleNodeLabel
                        ) + '_' + str(seq + 1) + '_' + str(subSeq + 1)
                        #
                        follicleShapeName = follicleName + appCfg.MaKeyword_Shape
                        #
                        localCurveName = yetiObjectName.replace(
                            astYetiNodeGroupLabel,
                            prsVariants.Util.astYetiGuideLocalCurveNodeLabel
                        ) + '_' + str(seq + 1) + '_' + str(subSeq + 1)
                        localCurveShapeName = localCurveName + appCfg.MaKeyword_Shape
                        # Rename Local Curve First
                        if localCurve:
                            maUtils.setNodeRename(localCurve, localCurveName)
                            maUtils.setObjectShapeRename(localCurveName, localCurveShapeName)
                            maUtils.setObjectParent(localCurveName, follicle)
                        #
                        if follicle:
                            maUtils.setNodeRename(follicle, follicleName)
                            maUtils.setObjectShapeRename(follicleName, follicleShapeName)
                            maUtils.setObjectParent(follicleName, guideFollicleSubGroup)
                        #
                        if hairSystem:
                            guideSystemData.append(hairSystem)
                        #
                        if nucleus:
                            guideNucleusData.append(nucleus)
                # Collection Guide System
                if guideSystemData:
                    guideSystems = maUtils.getReduceList(guideSystemData)
                    for seq, guideSystem in enumerate(guideSystems):
                        guideSystemName = yetiObjectName.replace(astYetiNodeGroupLabel, prsVariants.Util.astYetiGuideSystemNodeLabel) + '_' + str(seq + 1)
                        guideSystemShapeName = guideSystemName + appCfg.MaKeyword_Shape
                        #
                        maUtils.setNodeRename(guideSystem, guideSystemName)
                        maUtils.setObjectShapeRename(guideSystemName, guideSystemShapeName)
                        maUtils.setObjectParent(guideSystemName, guideSystemGroup)
                #
                if guideNucleusData:
                    guideNuclei = maUtils.getReduceList(guideNucleusData)
                    for seq, guideNucleus in enumerate(guideNuclei):
                        guideNucleusName = yetiObjectName.replace(astYetiNodeGroupLabel, prsVariants.Util.astYetiGuideNucleusNodeLabel) + '_' + str(seq + 1)
                        maUtils.setNodeRename(guideNucleus, guideNucleusName)
                        maUtils.setObjectParent(guideNucleusName, guideSystemGroup)
            # Debug ( Rename in Final )
            maUtils.setNodeRename(yetiObject, yetiObjectName)
            maUtils.setObjectShapeRename(yetiObjectName, yetiObjectShapeName)
            maUtils.setObjectParent(yetiObjectName, yetiObjectGroup)
        #
        def setAddAstFurPfx(pfxHairObjectPath, nodeLabel=none):
            def addBranch(objects, rootName, rootNameLabel, groupNameLabel, objectNameLabel, renameShape=False, subGroup=none, hide=False, childNameLabel=none, repairShape=False, delHistory=False):
                nameSet = rootName.replace(rootNameLabel, objectNameLabel)
                childNameSet = rootName.replace(rootNameLabel, childNameLabel)
                objectGroup = assetPr.astBasicGroupNameSet(assetName, groupNameLabel)
                if subGroup:
                    subGroup = nameSet + prsVariants.Util.basicGroupLabel
                    maUtils.setObjectAddChildGroup(subGroup, objectGroup)
                maxValue = len(objects)
                for seq, maObj in enumerate(objects):
                    if self.connectObject():
                        self.connectObject().setProgressValue(seq + 1, maxValue)
                    objectName = nameSet + '_' + str(seq)
                    objectShapeName = objectName + appCfg.MaKeyword_Shape
                    # Rename Object
                    maUtils.setNodeRename(maObj, objectName)
                    # Rename Shape
                    if renameShape:
                        maUtils.setObjectShapeRename(objectName, objectShapeName)
                        # Debug ( Yeti and PfxHair Share Grow )
                        if maUtils.getShapeType(objectName) == 'mesh':
                            maFur.setRefreshYetiGrow(objectName)
                    #
                    if subGroup:
                        maUtils.setObjectParent(objectName, subGroup)
                    # Add Sub Group
                    if not subGroup:
                        maUtils.setObjectParent(objectName, objectGroup)
                    # Hide
                    if hide:
                        maUtils.setHide(objectName)
                    # With Children
                    if childNameLabel:
                        childObjects = maUtils.getObjectChildObjectLis(objectName)
                        if childObjects:
                            childObjectName = childNameSet + '_' + str(seq)
                            childShapeName = childObjectName + appCfg.MaKeyword_Shape
                            for childObject in childObjects:
                                if repairShape:
                                    maUtils.setRepairShape(childObject)
                                shapes = maUtils.getMainShapes(childObject)
                                if shapes:
                                    for shape in shapes:
                                        if delHistory:
                                            maUtils.setCleanHistory(shape)
                                            maUtils.setNodeRename(shape, childShapeName)
                                maUtils.setNodeRename(childObject, childObjectName)
            #
            isDelHistory = self.deleteHistoryButton.isChecked()
            isUpdateHierarchy = self.updateHierarchyButton.isChecked()
            # Pfx Hair
            pfxHairObjectName = nodeName
            pfxHairShapeName = nodeName + appCfg.MaKeyword_Shape
            pfxHairObjectGroup = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astPfxHairGroupLabel)
            #
            growObjects, shaders, textures, maps, systemObjects, nucleusObjects, follicleData = maUtils.getPfxHairConnectionData(pfxHairObjectPath)
            # Grow
            if growObjects:
                addBranch(
                    growObjects, pfxHairObjectName, prsVariants.Util.astPfxHairGroupLabel, prsVariants.Util.astPfxHairGrowGroupLabel, prsVariants.Util.astPfxHairGrowGroupLabel,
                    renameShape=True, subGroup=False, hide=True
                )
            # Nde_ShaderRef
            if shaders:
                for seq, shader in enumerate(shaders):
                    shaderName = pfxHairObjectName.replace(prsVariants.Util.astPfxHairGroupLabel, prsVariants.Util.astPfxHairShaderNodeLabel) + '_' + str(seq)
                    maUtils.setNodeRename(shader, shaderName)
            # Texture
            if textures:
                for seq, texture in enumerate(textures):
                    textureName = pfxHairObjectName.replace(prsVariants.Util.astPfxHairGroupLabel, prsVariants.Util.astPfxHairTextureNodeLabel) + '_' + str(seq)
                    maUtils.setNodeRename(texture, textureName)
            # Map
            if maps:
                for seq, map in enumerate(maps):
                    mapName = pfxHairObjectName.replace(prsVariants.Util.astPfxHairGroupLabel, prsVariants.Util.astPfxHairMapNodeLabel) + '_' + str(seq)
                    maUtils.setNodeRename(map, mapName)
            # System
            if systemObjects:
                addBranch(
                    systemObjects, pfxHairObjectName, prsVariants.Util.astPfxHairGroupLabel, prsVariants.Util.astPfxHairSolverNodeGroupLabel,
                    prsVariants.Util.astPfxHairSystemNodeLabel,
                    renameShape=True, subGroup=False, hide=False)
            # Nucleus
            if nucleusObjects:
                addBranch(
                    nucleusObjects, pfxHairObjectName, prsVariants.Util.astPfxHairGroupLabel, prsVariants.Util.astPfxHairSolverNodeGroupLabel,
                    prsVariants.Util.astPfxHairNucleusNodeLabel,
                    renameShape=False, subGroup=False, hide=False
                )
            #
            if follicleData:
                follicleObjects = []
                outputCurveObjects = []
                for follicleObject, (subLocalCurveObjects, subOutputCurveObjects) in follicleData.items():
                    follicleObjects.append(follicleObject)
                    outputCurveObjects.extend(subOutputCurveObjects)
                # Follicle
                if follicleObjects:
                    addBranch(
                        follicleObjects,
                        pfxHairObjectName,
                        prsVariants.Util.astPfxHairGroupLabel,
                        prsVariants.Util.astPfxHairFollicleGroupLabel,
                        prsVariants.Util.astPfxHairFollicleNodeLabel,
                        renameShape=True,
                        subGroup=True,
                        hide=True,
                        childNameLabel=prsVariants.Util.astPfxHairLocalCurveNodeLabel,
                        repairShape=True,
                        delHistory=isDelHistory
                    )
                # Output Curve
                if outputCurveObjects:
                    addBranch(
                        outputCurveObjects,
                        pfxHairObjectName,
                        prsVariants.Util.astPfxHairGroupLabel,
                        prsVariants.Util.astPfxHairCurveGroupLabel,
                        prsVariants.Util.astPfxHairOutputCurveNodeLabel,
                        renameShape=True,
                        subGroup=True,
                        hide=False
                    )
            # Debug ( Rename in Final )
            maUtils.setNodeRename(pfxHairObjectPath, pfxHairObjectName)
            maUtils.setObjectShapeRename(pfxHairObjectName, pfxHairShapeName)
            maUtils.setObjectParent(pfxHairObjectName, pfxHairObjectGroup)
            if isUpdateHierarchy:
                self.connectObject().setAstCfxHierarchyView()
        #
        def setAddAstFurNurbs(nurbsHairObjectPath, nodeLabel=none):
            def addObjectBranch(objectPath, mainGroupLabel, groupNameLabel=False, subLabelString=none, isUseLeafGroup=False):
                if maUtils.isAppExist(objectPath):
                    objectType = maUtils.getTransformType(objectPath)
                    objectParentName = assetPr.astBasicGroupNameSet(assetName, mainGroupLabel)
                    #
                    parentPath = None
                    if objectParentName in self.pathDic:
                        # Main Group
                        parentPath = self.pathDic[objectParentName]
                        # Branch Group
                        parentPath += '|' + assetPr.astBasicGroupNameSet(assetName, groupNameLabel)
                        # Leaf Group
                        parentPath += '|' + assetPr.astNodeGroupNameSet(assetName, groupNameLabel, objectNameLabel)
                        if isUseLeafGroup:
                            if nodeLabel:
                                parentPath += '|' + assetPr.astNodeGroupNameSet(assetName, groupNameLabel, objectNameLabel) + nodeLabel
                        if not maUtils.isAppExist(parentPath):
                            maUtils.setAppPathCreate(parentPath)
                    #
                    if parentPath is not None:
                        newObjectName = assetPr.astBasicNodeNameSet(assetName, objectType, objectNameLabel) + subLabelString
                        shape = maUtils.getNodeShape(objectPath)
                        #
                        origParentPath = maUtils._toNodeParentPath(objectPath)
                        maUtils.setObjectShapeRename(shape, newObjectName + 'Shape')
                        maUtils.setNodeRename(objectPath, newObjectName)
                        newObjectPath = origParentPath + '|' + newObjectName
                        maUtils.setObjectParent(newObjectPath, parentPath)
            #
            def addNodeBranch(node, subLabelString):
                if maUtils.isAppExist(node):
                    nodeType = maUtils.getNodeType(node)
                    newNodeName = assetPr.astBasicNodeNameSet(assetName, nodeType, objectNameLabel) + subLabelString
                    maUtils.setNodeRename(node, newNodeName)
            #
            def setMain(objectPath):
                graphObjects, graphNodes, graphGrowGeometries, graphGuideGeometries = maFur.getNurbsHairConnectObjectData(objectPath)
                #
                if graphObjects:
                    for seq, childObjectPath in enumerate(graphObjects):
                        addObjectBranch(
                            childObjectPath, prsVariants.Util.astCfxFurNhrFieldGroupLabel, groupNameLabel=prsVariants.Util.astCfxFurNhrObjectGroupLabel,
                            subLabelString=nodeLabel + '_' + str(seq)
                        )
                #
                if graphGrowGeometries:
                    for seq, childObjectPath in enumerate(graphGrowGeometries):
                        addObjectBranch(
                            childObjectPath, prsVariants.Util.astCfxFurNhrFieldGroupLabel, groupNameLabel=prsVariants.Util.astCfxFurNhrGrowGroupLabel,
                            subLabelString=nodeLabel + '_' + str(seq)
                        )
                #
                if graphGuideGeometries:
                    for seq, childObjectPath in enumerate(graphGuideGeometries):
                        addObjectBranch(
                            childObjectPath, prsVariants.Util.astCfxFurNhrFieldGroupLabel, groupNameLabel=prsVariants.Util.astCfxFurNhrGuideGroupLabel,
                            subLabelString=nodeLabel + '_' + str(seq),
                            isUseLeafGroup=True
                        )
                #
                if graphNodes:
                    for seq, childNode in enumerate(graphNodes):
                        addNodeBranch(childNode, subLabelString=nodeLabel + '_' + str(seq))
                #
                addObjectBranch(
                    objectPath, prsVariants.Util.astCfxFurNhrFieldGroupLabel, groupNameLabel=prsVariants.Util.astCfxFurNhrObjectGroupLabel,
                    subLabelString=nodeLabel
                )
            #
            setMain(nurbsHairObjectPath)
        #
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        nodeName = self.getChildNodeName()
        objectNameLabel = self.nodeNameLabel
        objectPathLis = self.getSelFurObjectPaths()
        #
        yetiObjects = self.yetiObjects
        pfxHairObjects = self.pfxHairObjects
        nurbsHairObjects = self.nurbsHairObjects
        #
        if nodeName and objectPathLis:
            if len(objectPathLis) == 1:
                selObjectPath = objectPathLis[0]
                if selObjectPath in yetiObjects:
                    setAddAstFurYeti(selObjectPath)
                elif selObjectPath in pfxHairObjects:
                    setAddAstFurPfx(selObjectPath)
                elif selObjectPath in nurbsHairObjects:
                    setAddAstFurNurbs(selObjectPath)
            else:
                for mainSeq, selObjectPath in enumerate(objectPathLis):
                    mainLabel = '_' + str(mainSeq)
                    if selObjectPath in nurbsHairObjects:
                        setAddAstFurNurbs(selObjectPath, mainLabel)
            #
            nurbsHairGroup = assetPr.astUnitCfxNhrFieldGroupName(assetName)
            maUtils.setEmptyGroupClear(nurbsHairGroup)
            #
            self._furNodeKeywordEntryLabel.setDatum(none)
            self.setListAstCfxFur()
            # self.connectObject().setAstCfxHierarchyView()
            # self.connectObject().astHierarchyToggleButton.setChecked(True)
    #
    def astCreateGrowSourceCmd(self):
        def setMain():
            meshObjectLis = treeBox.selectedItemPaths()
            if meshObjectLis:
                meshObject = meshObjectLis[0]
                #
                meshName = maUtils._toNodeName(meshObject)
                #
                if not maUtils.isAppExist(objectGroupPath):
                    maUtils.setAppPathCreate(objectGroupPath)
                #
                growSourceObjectName = meshName + prsVariants.Util.astCfxGrowSourceGroupLabel
                if not maUtils.isAppExist(growSourceObjectName):
                    maUtils.setCopyNode(meshObject, growSourceObjectName)
                    #
                    maAttr.setNodeUnrenderable(growSourceObjectName)
                    maUtils.setAttrStringDatumForce(growSourceObjectName, prsVariants.Util.astCfxGrowSourceAttrLabel, meshName)
                    #
                    maUtils.setNodeOutlinerRgb(growSourceObjectName, 1, .5, 1)
                    #
                    self.setListAstModelGeometryObjects()
                #
                maUtils.setObjectParent(growSourceObjectName, objectGroupPath)
        #
        treeBox = self._astModelGeometryObjectTreeViewBox
        #
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetStage = self.connectObject().assetStage
        #
        objectGroupPath = None
        if prsMethods.Asset.isGroomStageName(assetStage):
            objectGroupPath = assetPr.astUnitCfxGroupSourceGroupPath(assetName)
        elif prsMethods.Asset.isSolverStageName(assetStage):
            objectGroupPath = assetPr.astUnitSolverGrowSourceObjectGroupPath(assetName)
        if objectGroupPath:
            setMain()
    #
    def astAddGrowTargetCmd(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetStage = self.connectObject().assetStage
        #
        groupName = None
        if prsMethods.Asset.isGroomStageName(assetStage):
            groupName = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astCfxFurGrowTargetGroupLabel)
        elif prsMethods.Asset.isSolverStageName(assetStage):
            groupName = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astRigSolGrowTargetGroupLabel)
        if groupName:
            self._addObjectCmd(groupName)
    #
    def astAddGrowDeformCmd(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetStage = self.connectObject().assetStage
        #
        groupPath = None
        if prsMethods.Asset.isGroomStageName(assetStage):
            groupPath = assetPr.astUnitCfxGrowDeformObjectGroupPath(assetName)
        elif prsMethods.Asset.isSolverStageName(assetStage):
            groupPath = assetPr.astUnitSolverGrowDeformObjectGroupPath(assetName)
        if groupPath:
            self._addObjectCmd(groupPath)
    #
    def astAddGrowCollisionCmd(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetStage = self.connectObject().assetStage
        #
        groupPath = None
        if prsMethods.Asset.isGroomStageName(assetStage):
            groupPath = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astCfxFurCollisionSubGroupLabel)
        elif prsMethods.Asset.isSolverStageName(assetStage):
            groupPath = assetPr.astBasicGroupNameSet(assetName, prsVariants.Util.astRigSolCollisionSubGroupLabel)
        if groupPath:
            self._addObjectCmd(groupPath)
    @staticmethod
    def _addObjectCmd(groupPath):
        selObjectLis = maUtils.getSelectedObjects(1)
        #
        maUtils.setAppPathCreate(groupPath)
        #
        if maUtils.isAppExist(groupPath):
            [maUtils.setObjectParent(i, groupPath) for i in selObjectLis]
            [maUtils.setHide(i) for i in maUtils.getSelectedObjects(1)]
    # UI State
    def setAddNodeBtnState(self):
        self.astFurNodeNameLabel = 'unknown'
        #
        objectPathLis = self.getSelFurObjectPaths()
        cfxObjects = self.cfxObjects
        #
        yetiObjects = self.yetiObjects
        pfxHairObjects = self.pfxHairObjects
        nurbsHairObjects = self.nurbsHairObjects
        #
        boolean = self.getChildNodeName() != none
        button = self._addNodeButton
        #
        if objectPathLis:
            selObjectPath = objectPathLis[0]
            if selObjectPath in cfxObjects:
                if boolean:
                    self._addNFurNodeTipLabel.setDatum(self.addNodeSubTips1)
                #
                button.setPressable(boolean)
                #
                if selObjectPath in yetiObjects:
                    self.astFurNodeNameLabel = prsVariants.Util.astYetiNodeGroupLabel[1:]
                elif selObjectPath in pfxHairObjects:
                    self.astFurNodeNameLabel = prsVariants.Util.astPfxHairGroupLabel[1:]
                elif selObjectPath in nurbsHairObjects:
                    self.astFurNodeNameLabel = prsVariants.Util.maNurbsHairNode
            else:
                button.setPressable(False)
                self._addNFurNodeTipLabel.setDatum(self.addNodeTips)
        else:
            button.setPressable(False)
            self._addNFurNodeTipLabel.setDatum(self.addNodeTips)
    #
    def setAstFurNodeName(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        entryUiLabel = self._furNodeKeywordEntryLabel
        #
        var = entryUiLabel.datum()
        #
        lenLimit = 24
        furObjects = datAsset.getFurObjects(assetName)
        existNodes = []
        if furObjects:
            existNodes = [maUtils._toNodeName(i) for i in furObjects]
        #
        nodeName = var
        newNode = assetPr.astBasicNodeNameSet(assetName, self.astFurNodeNameLabel, nodeName)
        if nodeName:
            if len(nodeName) < lenLimit:
                if not newNode in existNodes:
                    self._nodeFullNameUiLabel.setDatum(newNode)
                    #
                    self.nodeNameLabel = nodeName
                else:
                    self._addNFurNodeTipLabel.setDatum(self.nodeNameTips1)
                    self._nodeFullNameUiLabel.setDatum(none)
            else:
                self._addNFurNodeTipLabel.setDatum(self.addNodeSubTips2)
                self._nodeFullNameUiLabel.setDatum(none)
        else:
            self._addNFurNodeTipLabel.setDatum(self.addNodeSubTips2)
            self._nodeFullNameUiLabel.setDatum(none)
    #
    def setGrowSourceName(self):
        treeBox = self._astModelGeometryObjectTreeViewBox
        #
        button = self.createGrowSourceButton
        #
        selectedMeshes = treeBox.selectedItemPaths()
        if selectedMeshes:
            meshPath = selectedMeshes[0]
            meshName = maUtils._toNodeName(meshPath)
            growSourceMesh = meshName + prsVariants.Util.astCfxGrowSourceGroupLabel
            boolean = not maUtils.isAppExist(growSourceMesh)
            self._growSourceCreateTipLabel.setDatum([self.createGrowSourceSubTips2, self.createGrowSourceSubTips1][boolean])
            button.setPressable([False, True][boolean])
        else:
            self._growSourceCreateTipLabel.setDatum(self.createGrowSourceTips)
    #
    def setRefreshTreeViewBoxSelection(self):
        def setBranch(treeViewBox, uiData):
            if not treeViewBox.hasFocus():
                selectedUuids = maUuid.getSelUniqueIds()
                for k, v in uiData.items():
                    if k in selectedUuids:
                        v.setSelected(True)
                    else:
                        v.setSelected(False)
        #
        def setMain(data):
            [setBranch(*i) for i in data]
        #
        refreshData = [
            (self._astCfxFurObjectsTreeViewBox, self._astCfxFurObjectDic),
            (self._astModelGeometryObjectTreeViewBox, self._astModelGeometryObjectDic)
        ]
        #
        setMain(refreshData)
    #
    def getChildNodeName(self):
        data = self._nodeFullNameUiLabel.nameText()
        return data
    #
    def getSelFurObjectPaths(self):
        treeBox = self._astCfxFurObjectsTreeViewBox
        return treeBox.selectedItemPaths()
    #
    def setupUnitWidgets(self):
        self._astCfxHirToolUiBox = qtWidgets.QtToolbox()
        self._astCfxHirToolUiBox.hide()
        self.mainLayout().addWidget(self._astCfxHirToolUiBox)
        self._astCfxHirToolUiBox.setTitle('Asset ( Groom ) Graph')
        self.setupAstCfxGraphToolUiBox(self._astCfxHirToolUiBox)
        #
        self._astCfxUtilsToolUiBox = qtWidgets.QtToolbox()
        self._astCfxUtilsToolUiBox.hide()
        self.mainLayout().addWidget(self._astCfxUtilsToolUiBox)
        self._astCfxUtilsToolUiBox.setTitle('Asset ( Groom ) Utilities')
        self.setupAstCfxUtilsToolUiBox(self._astCfxUtilsToolUiBox)


#
class IfAstSolverToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Solver
    ]
    UnitTitle = 'Character FX Tool Unit'
    UnitIcon = 'window#solverToolPanel'
    UnitTooltip = u'''角色特效工具模块'''
    #
    UnitScriptJobWindowName = 'astSolverToolScriptJobWindow'
    #
    widthSet = 400
    # Nde_Node
    dicSolverNodeTool = collections.OrderedDict()
    dicSolverNodeTool['placeholder'] = [1, 0, 0, 1, 4, 'Placeholder']
    # 1
    dicSolverNodeTool['nhrGuideObjectModify'] = [1, 2, 0, 1, 4, 'Collection Guide Object ( Nurbs Hair ) ']
    #
    dicSolverGuideTool = collections.OrderedDict()
    dicSolverGuideTool['placeholder'] = [1, 0, 0, 1, 4, 'Placeholder']
    # 1
    dicSolverGuideTool['connectNurbsHairGuide'] = [1, 2, 0, 1, 4, 'Connect Guide ( Nurbs Hair )']
    def __init__(self, *args, **kwargs):
        super(IfAstSolverToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._nhrGuideLis = []
        self._nhrGuideCheckLis = []
        #
        self._astCfxFurObjectDic = {}
        self.furGuideDic = {}
        #
        self.setupUnitWidgets()
    #
    def refreshMethod(self):
        if self.connectObject() is not None:
            if prsMethods.Asset.isGroomStageName(self.connectObject().assetStage) or prsMethods.Asset.isSolverStageName(self.connectObject().assetStage):
                self.setupAstRigSolFurSolGuideQtToolbox()
                self.setupAstRigSolSolGuideConnectQtToolbox()
                #
                self.setAstListFurObjects()
                self.setAstListGuideObjects()
                self.setButtonState()
                #
                self.setScriptJob()
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methods = [self.setRefreshTreeViewBoxSelection]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
        #
        scriptJobEvn = 'NameChanged'
        methods = [self.setAstListFurObjects, self.setAstListGuideObjects]
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methods)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupAstRigSolFurSolGuideQtToolbox(self):
        def setSelObject():
            data = self.astSolverFurNodeTreeViewBox.selectedItemPaths()
            if data:
                maUtils.setNodeSelect(data)
            else:
                pass
        #
        toolBox = self._astCfxRigGuideToolUiBox
        uiData = self.dicSolverNodeTool
        #
        widget = qtCore.QWidget_()
        toolBox.addWidget(widget, 0, 0, 1, 4)
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        #
        self.astSolverFurNodeTreeViewBox = qtWidgets_.QTreeWidget_()
        self.astSolverFurNodeTreeViewBox.setUiStyle('B')
        layout.addWidget(self.astSolverFurNodeTreeViewBox)
        self.astSolverFurNodeTreeViewBox.setColumns(['Nde_Node', 'Nde_Node Type'], [4, 4], self.widthSet * 2)
        #
        self.astSolverFurNodeTreeViewBox.itemSelectionChanged.connect(setSelObject)
        self.astSolverFurNodeTreeViewBox.itemSelectionChanged.connect(self.setButtonState)
        #
        self.nhrGuideObjectModifyButton = qtWidgets.QtPressbutton()
        toolBox.setButton(uiData, 'nhrGuideObjectModify', self.nhrGuideObjectModifyButton)
        self.nhrGuideObjectModifyButton.setPercentEnable(True)
        self.nhrGuideObjectModifyButton.clicked.connect(self.nhrGuideObjectModifyCmd)
        #
        toolBox.setSeparators(uiData)
    #
    def setupAstRigSolSolGuideConnectQtToolbox(self):
        def setSelObject():
            data = self.astSolverFurGuideTreeViewBox.selectedItemPaths()
            if data:
                maUtils.setNodeSelect(data)
            else:
                pass
        #
        toolBox = self._astCfxRigConnectToolUiBox
        uiData = self.dicSolverGuideTool
        #
        widget = qtCore.QWidget_()
        toolBox.addWidget(widget, 0, 0, 1, 4)
        layout = qtCore.QVBoxLayout_(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        #
        self.astSolverFurGuideTreeViewBox = qtWidgets_.QTreeWidget_()
        self.astSolverFurGuideTreeViewBox.setUiStyle('B')
        layout.addWidget(self.astSolverFurGuideTreeViewBox)
        self.astSolverFurGuideTreeViewBox.setColumns(['Nde_Node', 'Nde_Node Type'], [4, 4], self.widthSet * 2)
        #
        self.astSolverFurGuideTreeViewBox.itemSelectionChanged.connect(setSelObject)
        #
        self.connectNurbsHairGuideButton = qtWidgets.QtPressbutton()
        toolBox.setButton(uiData, 'connectNurbsHairGuide', self.connectNurbsHairGuideButton)
        self.connectNurbsHairGuideButton.clicked.connect(self.setCreateNurbsHairSolverConnection)
        #
        toolBox.setSeparators(uiData)
    #
    def setAstListFurObjects(self):
        def setMain():
            nhrObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
            if nhrObjects:
                nhrGuideGroup = assetPr.astUnitRigSolNhrGuideObjectGroupName(assetName)
                for nhrObject in nhrObjects:
                    self._nhrGuideLis.append(nhrObject)
                    #
                    nhrObjectItem = maAstTreeViewCmds.setObjectBranch(self._astCfxFurObjectDic, treeBox, nhrObject)
                    nhrGuideObjects = maFur.getNhrGuideObjects(nhrObject)
                    if nhrGuideObjects:
                        for nhrGuideObject in nhrGuideObjects:
                            nhrGuideObjectPath = maUtils._getNodePathString(nhrGuideObject)
                            maAstTreeViewCmds.setObjectBranch(self._astCfxFurObjectDic, treeBox, nhrGuideObject, nhrObjectItem)
                            if nhrGuideGroup in nhrGuideObjectPath:
                                self._nhrGuideCheckLis.append(nhrObject)
                                nhrObjectItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_NurbsHair, 'on')
                                nhrObjectItem.setExpanded(False)
                            else:
                                nhrObjectItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_NurbsHair, 'error')
                                nhrObjectItem.setExpanded(True)
                    else:
                        nhrObjectItem.setItemMayaIcon(0, appCfg.MaNodeType_Plug_NurbsHair, 'off')
        #
        self._nhrGuideLis = []
        self._nhrGuideCheckLis = []
        #
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        treeBox = self.astSolverFurNodeTreeViewBox
        #
        setMain()
    #
    def setAstListGuideObjects(self):
        def setMain():
            nhrGuideObjects = datAsset.getAstUnitSolverNhrGuideObjects(assetName)
            if nhrGuideObjects:
                for nhrGuideObject in nhrGuideObjects:
                    nhrGuideObjectItem = maAstTreeViewCmds.setObjectBranch(self.furGuideDic, treeBox, nhrGuideObject)
                    nhrObjects = maFur.getNhrObjectsByGuide(nhrGuideObject)
                    if nhrObjects:
                        for nhrObject in nhrObjects:
                            maAstTreeViewCmds.setObjectBranch(self.furGuideDic, treeBox, nhrObject, nhrGuideObjectItem)
                        #
                        nhrGuideObjectItem.setItemMayaIcon(0, appCfg.MaNurbsHairInGuideCurvesType, 'on')
                    else:
                        nhrGuideObjectItem.setItemMayaIcon(0, appCfg.MaNurbsHairInGuideCurvesType, 'off')
        #
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        treeBox = self.astSolverFurGuideTreeViewBox

        #
        setMain()
    #
    def setButtonState(self):
        assetName = self.connectObject().assetName
        self.nhrGuideObjectModifyButton.setPercent(len(self._nhrGuideLis), len(self._nhrGuideCheckLis))
    #
    def nhrGuideObjectModifyCmd(self):
        def setMain():
            nhrObjects = datAsset.getAstCfxNurbsHairObjects(assetName)
            if nhrObjects:
                nhrGuideGroup = assetPr.astUnitRigSolNhrGuideObjectGroupName(assetName)
                for nhrObject in nhrObjects:
                    nhrObjectName = maUtils._toNodeName(nhrObject)
                    nhrGuideObjects = maFur.getNhrGuideObjects(nhrObject)
                    if nhrGuideObjects:
                        for nhrGuideObject in nhrGuideObjects:
                            nhrGuideObjectPath = maUtils._getNodePathString(nhrGuideObject)
                            nhrGuideObjectShape = maUtils.getNodeShape(nhrGuideObject)
                            nhrGuideObjectName = maUtils._toNodeName(nhrGuideObject)
                            if not nhrGuideGroup in nhrGuideObjectPath:
                                nhrGuideObjectNewName = nhrObjectName.replace(appCfg.MaNodeType_Plug_NurbsHair, appCfg.MaNurbsHairInGuideCurvesType)
                                nhrGuideObjectShapeNewName = nhrGuideObjectNewName + 'Shape'
                                if not nhrGuideObjectName == nhrGuideObjectNewName:
                                    maUtils.setObjectRename(nhrGuideObjectShape, nhrGuideObjectShapeNewName)
                                    maUtils.setObjectRename(nhrGuideObject, nhrGuideObjectNewName)
                                #
                                maUtils.setObjectParent(nhrGuideObjectNewName, nhrGuideGroup)
                                maUtils.setNodeOutlinerRgb(nhrGuideObjectNewName, 1, .5, 1)
        #
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        setMain()
        #
        self.setAstListFurObjects()
        self.setAstListGuideObjects()
        #
        self.setButtonState()
    #
    def setCreateNurbsHairSolverConnection(self):
        assetName = self.connectObject().assetName
        #
        nurbsHairSolverObjects = datAsset.getAstUnitSolverNhrGuideObjects(assetName)
        if nurbsHairSolverObjects:
            for nurbsHairSolverObject in nurbsHairSolverObjects:
                currentGuideGroup = maUtils.getAttrDatum(nurbsHairSolverObject, prsVariants.Util.astRigSolGuideSourceAttrLabel)
                if currentGuideGroup:
                    if maUtils.isAppExist(currentGuideGroup):
                        maFur.setConnectNurbsHairSolver(nurbsHairSolverObject, currentGuideGroup)
    #
    def setRefreshTreeViewBoxSelection(self):
        def setBranch(treeViewBox, uiData):
            if not treeViewBox.hasFocus():
                selectedUuids = maUuid.getSelUniqueIds()
                for k, v in uiData.items():
                    if k in selectedUuids:
                        v.setSelected(True)
                    else:
                        v.setSelected(False)
        #
        def setMain(data):
            [setBranch(*i) for i in data]
        #
        refreshData = [
            (self.astSolverFurNodeTreeViewBox, self._astCfxFurObjectDic),
            (self.astSolverFurGuideTreeViewBox, self.furGuideDic)
        ]
        #
        setMain(refreshData)
    #
    def setupUnitWidgets(self):
        self._astCfxRigGuideToolUiBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._astCfxRigGuideToolUiBox)
        self._astCfxRigGuideToolUiBox.setTitle('Asset ( Solver Rig ) Guide')
        #
        self._astCfxRigConnectToolUiBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._astCfxRigConnectToolUiBox)
        self._astCfxRigConnectToolUiBox.setTitle('Asset ( Solver Rig ) Connection')


#
class IfAstGeneralToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Model,
        lxConfigure.LynxiProduct_Asset_Link_Rig,
        lxConfigure.LynxiProduct_Asset_Link_Groom,
        lxConfigure.LynxiProduct_Asset_Link_Solver,
        lxConfigure.LynxiProduct_Asset_Link_Light
    ]
    UnitTitle = 'General Tool Unit'
    UnitIcon = 'window#utilsToolPanel'
    UnitTooltip = u'''通用工具模块'''
    #
    _groupCreateTip = u'''提示：请输入"Nde_Node Name"...'''
    #
    UnitScriptJobWindowName = 'astGeneralToolScriptJobWindow'
    #
    widthSet = 400
    # CFX Utilities Tool
    dicAstUtils = {
        'withMaterial': [1, 0, 0, 1, 2, 'Material Model '], 'withAov': [1, 0, 2, 1, 2, 'Aov Model'],
        'variant': [0, 1, 0, 1, 2, 'Variant(s)'], 'importShader': [1, 1, 2, 1, 2, 'Import Nde_ShaderRef', 'svg_basic@svg#python'],
        'usePath': [1, 3, 0, 1, 2, 'Use Path'], 'useName': [1, 3, 1, 1, 2, 'Use Name'], 'useGeom': [1, 3, 2, 1, 2, 'Use Nde_Geometry'],
        'loadMeshIndex': [1, 4, 0, 1, 4, 'Load Mesh Unique ID', 'svg_basic@svg#load'],
        # 5
        'astUnitClearScene': [1, 6, 0, 1, 2, 'Clean Maya - Scene', 'svg_basic@svg#python'], 'astUnitRenameScene': [1, 6, 2, 1, 2, 'Rename Maya - Scene', 'svg_basic@svg#python'],
        # 7
        'loadRigAsset': [1, 8, 0, 1, 4, 'Load Asset ( Rig )', 'svg_basic@svg#rig']
    }
    # Hierarchy
    dicUtilsHier = {
        0: 'Config(s)',
        'autoRename': [1, 1, 0, 1, 2, 'Auto Rename'],
        2: 'Action(s)',
        'parentGroup': [0, 3, 0, 1, 3, ''], 'addObject': [1, 3, 3, 1, 1, 'Add Object', 'svg_basic@svg#addTab'],
        'childGroup': [0, 4, 0, 1, 3, ''], 'addGroup': [1, 4, 3, 1, 1, 'Add Group', 'svg_basic@svg#addTab'],
        'groupName': [0, 5, 0, 1, 4, 'Group Name'],
        6: 'Tip(s)',
        'tips': [0, 7, 0, 1, 4, 'Tip(s)']
    }
    dicLight = collections.OrderedDict()
    dicLight['connectLightToScale'] = [1, 0, 0, 1, 4, 'Connect Light to Scale']
    def __init__(self, *args, **kwargs):
        super(IfAstGeneralToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.filterTypes = []
        self._scriptJobMethodLis = []
        #
        self.setupUnitWidgets()
    #
    def refreshMethod(self):
        if self.connectObject() is not None:
            self.setAstVariantUiLabelShow()
            #
            self._rootGroup = prsMethods.Asset.rootName(
                self.connectObject().assetName
            )
            self._linkGroup = prsMethods.Asset.toLinkGroupName(
                self.connectObject().assetName,
                self.connectObject().assetStage
            )
            #
            self.setupAstUtilsGraphToolUiBox(self._astUtilsGraphToolUiBox)
            #
            if prsMethods.Asset.isModelStageName(self.connectObject().assetStage):
                self._addObjectButton.setNameText('Add Nde_Geometry')
                self.filterTypes = [appCfg.MaNodeType_Mesh, appCfg.MaNodeType_NurbsSurface, appCfg.MaNodeType_NurbsCurve]
                #
                if prsMethods.Asset.isPropCategory(self.connectObject().assetCategory):
                    self.setupAstPropGraphToolUiBox(self._astModelPropHierToolUiBox)
                    self._astModelPropHierToolUiBox.show()
                #
                self.setupAstModelSolClothGraphToolUiBox(self._astModelSolClothHierToolUiBox)
                self._astModelSolClothHierToolUiBox.show()
                #
                self.setupAstModelSolHairGraphToolUiBox(self._astModelSolverHairGraphToolUiBox)
                self._astModelSolverHairGraphToolUiBox.show()
            elif prsMethods.Asset.isLightStageName(self.connectObject().assetStage):
                self._addObjectButton.setNameText('Add Light')
                self.filterTypes = maUtils.getNodeTypeLisByFilter('light')
                self.filterTypes.extend([appCfg.MaNodeType_Mesh])
                #
                self.setupAstLightHierToolUiBox(self.astLightHierToolUiBox)
                self.astLightHierToolUiBox.show()
                #
                self.setupAstLightToolUiBox(self._astLightToolUiBox)
                self.astLightToolUiBox.show()
            #
            self.setScriptJob()
            self.connectObject().setQuitConnect(self.delScriptJob)
    #
    def setScriptJob(self):
        scriptJobEvn = 'SelectionChanged'
        methodLis = self._scriptJobMethodLis
        maUtils.setCreateEventScriptJob(self.UnitScriptJobWindowName, scriptJobEvn, methodLis)
    #
    def delScriptJob(self):
        maUtils.setWindowDelete(self.UnitScriptJobWindowName)
    #
    def setupAstUtilsGraphToolUiBox(self, toolBox):
        def getParentGroupName():
            data = self._parentGroupLabel.datum()
            return data
        #
        def getChildGroupName():
            data = self._childGroupLabel.datum()
            return data
        #
        def setParentGroupName():
            objectPathLis = maUtils.getSelectedNodeLis()
            if objectPathLis:
                objectPath = objectPathLis[0]
                if not objectPath.endswith(self._rootGroup) and not objectPath.endswith(self._linkGroup) and objectPath.startswith(appCfg.Ma_Separator_Node + self._rootGroup):
                    if objectPath.endswith(prsVariants.Util.basicGroupLabel):
                        objectName = maUtils._toNodeName(objectPath)
                        self._parentGroupLabel.setDatum(objectName)
        #
        def setChildGroupName():
            var = self._groupKeywordEntryLabel.datum()
            if var:
                linkGroup = self._linkGroup
                existsGroups = maUtils.getGroupLisByRoot(linkGroup, 0)
                groupName = var

                newGroup = assetPr.astBasicGroupNameSet(assetName, '_' + groupName)
                if groupName:
                    if len(groupName) < lenLimit:
                        if newGroup not in existsGroups:
                            self._childGroupLabel.setDatum(newGroup)
                            self._groupNameTipsLabel.setDatum(u'提示：名字可以使用...')
                        else:
                            self._childGroupLabel.setEnterClear()
                            self._groupNameTipsLabel.setDatum(u'错误：名字已经存在于文件中...')
                    else:
                        self._childGroupLabel.setEnterClear()
                        self._groupNameTipsLabel.setDatum(u'错误：名字不能超过%s个字符...' % lenLimit)
                else:
                    self._childGroupLabel.setEnterClear()
                    self._groupNameTipsLabel.setDatum(self._groupCreateTip)
            else:
                self._childGroupLabel.setEnterClear()
                self._groupNameTipsLabel.setDatum(self._groupCreateTip)
        #
        def setAddGroup():
            parent = getParentGroupName()
            child = getChildGroupName()
            if parent and child:
                maHier.setCreateBranchGroup(parent, child)
                #
                self._childGroupLabel.setEnterClear()
                self._groupKeywordEntryLabel.setEnterClear()
                #
                self._groupNameTipsLabel.setDatum(self._groupCreateTip)
        #
        def setAddObject():
            parent = getParentGroupName()
            isAutoRename = self._autoRenameCheckbutton.isChecked()
            if parent:
                parentPath = maUtils._getNodePathString(parent)
                if maUtils.isAppExist(parentPath):
                    maHier.addHierarchyObject(
                        parentPath, assetName, self.filterTypes, autoRename=isAutoRename
                    )
        #
        def setAddGrpBtnState():
            parent = getParentGroupName()
            child = getChildGroupName()
            button = self._addGroupButton
            #
            button.setPressable([False, True][parent is not None and child is not None])
        #
        def setAddNodeBtnState():
            button = self._addObjectButton
            parent = getParentGroupName()
            objectPathLis = maUtils.getSelectedNodeLis()
            button.setPressable([False, True][parent is not None and objectPathLis != []])
        #
        inData = self.dicUtilsHier
        #
        assetName = self.connectObject().assetName
        assetStage = self.connectObject().assetStage
        #
        lenLimit = 12
        #
        self._autoRenameCheckbutton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'autoRename', self._autoRenameCheckbutton)
        self._autoRenameCheckbutton.setChecked(True)
        self._autoRenameCheckbutton.setTooltip(
            u'''启用 / 关闭 添加物件的时候 重命名物件（工具组名）'''
        )
        #
        self._parentGroupLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'parentGroup', self._parentGroupLabel)
        self._parentGroupLabel.setTooltip(
            u'''显示 父级组的名字：\n1，在“Outliner”中选中可用的组以切换父级组名'''
        )
        #
        self._addObjectButton = qtWidgets.QtPressbutton()
        self._addObjectButton.setPressable(False)
        toolBox.setButton(inData, 'addObject', self._addObjectButton)
        self._addObjectButton.clicked.connect(setAddObject)
        self._addObjectButton.setTooltip(
            u'''点击 添加选中的物体到父级组'''
        )
        #
        self._childGroupLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'childGroup', self._childGroupLabel)
        self._childGroupLabel.setTooltip(
            u'''显示 子级组的名字：\n1，在输入框中输入的关键词以生成子级组名'''
        )
        #
        self._addGroupButton = qtWidgets.QtPressbutton()
        self._addGroupButton.setPressable(False)
        toolBox.setButton(inData, 'addGroup', self._addGroupButton)
        self._addGroupButton.clicked.connect(setAddGroup)
        self._addGroupButton.setTooltip(
            u'''点击 添加子级组到父级组'''
        )
        #
        self._groupKeywordEntryLabel = qtWidgets.QtEnterlabel()
        self._groupKeywordEntryLabel.setTextValidator(48)
        self._groupKeywordEntryLabel.setEnterEnable(True)
        self._groupKeywordEntryLabel.setEnterable(True)
        toolBox.setInfo(inData, 'groupName', self._groupKeywordEntryLabel)
        self._groupKeywordEntryLabel.entryChanged.connect(setChildGroupName)
        self._groupKeywordEntryLabel.entryChanged.connect(setAddGrpBtnState)
        #
        self._groupNameTipsLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'tips', self._groupNameTipsLabel)
        self._groupNameTipsLabel.setDatum(self._groupCreateTip)
        #
        toolBox.setSeparators(inData)
        #
        self._scriptJobMethodLis = [
            setParentGroupName,
            setAddGrpBtnState,
            setAddNodeBtnState
        ]
    #
    def _setAstModelGraphTool(self, toolBox, buttonConfig, hierarchyDataFn):
        def setBranch(key, ui):
            def command():
                addCmd(key)
            #
            ui.clicked.connect(command)
        #
        def addCmd(keyword):
            parentName = assetPr.astBasicGroupNameSet(assetName, '_' + keyword)
            parentPath = None
            if parentName in pathDic:
                parentPath = pathDic[parentName]
                if not maUtils.isAppExist(parentPath):
                    maUtils.setAppPathCreate(parentPath)
                    objectPathLis = maUtils.getSelectedNodeLis()
                    maUtils.setNodeSelect(objectPathLis)
            #
            if parentPath:
                maHier.addHierarchyObject(parentPath, assetName, self.filterTypes)
                #
                self.connectObject().setAstHierarchyView()
                self.connectObject().astHierarchyToggleButton.setChecked(True)
        #
        assetName = self.connectObject().assetName
        #
        hierarchyData = hierarchyDataFn(assetName)
        pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
        #
        index = 0
        for seq, i in enumerate(buttonConfig):
            button = qtWidgets.QtPressbutton()
            explain = bscMethods.StrCamelcase.toPrettify(i)
            button.setNameText(explain)
            button.setIcon('svg_basic@svg#addTab')
            x = seq % 2
            if x == 0:
                index += 1
            #
            toolBox.addWidget(button, index, x, 1, 1)
            #
            setBranch(i, button)
    #
    def setupAstPropGraphToolUiBox(self, toolBox):
        buttonConfig = assetPr.astPropBasicLeafs()
        #
        hierarchyDataFn = assetPr.astPropHierarchyConfig
        self._setAstModelGraphTool(toolBox, buttonConfig, hierarchyDataFn)
    #
    def setupAstModelSolClothGraphToolUiBox(self, toolBox):
        buttonConfig = assetPr.astSolverClothBasicLeafs()
        #
        hierarchyDataFn = assetPr.astModelSolverHierarchyConfig
        self._setAstModelGraphTool(toolBox, buttonConfig, hierarchyDataFn)
    #
    def setupAstModelSolHairGraphToolUiBox(self, toolBox):
        buttonConfig = assetPr.astSolverHairBasicLeafs()
        #
        hierarchyDataFn = assetPr.astModelSolverHierarchyConfig
        self._setAstModelGraphTool(toolBox, buttonConfig, hierarchyDataFn)
    #
    def setupAstLightHierToolUiBox(self, toolBox):
        def setBranch(key, ui):
            def command():
                addCmd(key)
            ui.clicked.connect(command)
        #
        def addCmd(keyword):
            parentName = assetPr.astBasicGroupNameSet(assetName, '_' + keyword)
            parentPath = None
            if parentName in pathDic:
                parentPath = pathDic[parentName]
                if not maUtils.isAppExist(parentPath):
                    objectPathLis = maUtils.getSelectedNodeLis()
                    maUtils.setAppPathCreate(parentPath)
                    maUtils.setNodeSelect(objectPathLis)
            #
            if parentPath:
                maHier.addHierarchyObject(parentPath, assetName, self.filterTypes)
                #
                self.connectObject().setAstHierarchyView()
                self.connectObject().astHierarchyToggleButton.setChecked(True)
        #
        assetName = self.connectObject().assetName
        #
        hierarchyData = assetPr.astLightHierarchyConfig(assetName)
        pathDic = bscMethods.MayaPath.covertToPathCreateDic(hierarchyData)
        #
        buttonConfig = assetPr.astLightBasicLeafs()
        index = 0
        for seq, i in enumerate(buttonConfig):
            button = qtWidgets.QtPressbutton()
            explain = bscMethods.StrCamelcase.toPrettify(i)
            button.setNameText(explain)
            button.setIcon('svg_basic@svg#addTab')
            x = seq % 2
            if x == 0:
                index += 1
            #
            toolBox.addWidget(button, index, x, 1, 1)
            #
            setBranch(i, button)
    #
    def setupAstLightToolUiBox(self, toolBox):
        def setConnectLightToScale():
            root = prsMethods.Asset.lightLinkGroupName(assetName)
            maRender.setConnectLightsToScale(root)
            #
            bscObjects.If_Message('Connect Light to Scale', 'Complete')
        #
        inData = self.dicLight
        #
        assetName = self.connectObject().assetName
        #
        self.connectLightToScaleButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'connectLightToScale', self.connectLightToScaleButton)
        self.connectLightToScaleButton.clicked.connect(setConnectLightToScale)
    #
    def setupAstUtilsToolUiBox(self, toolBox):
        inData = self.dicAstUtils
        #
        self.importWithMaterialButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withMaterial', self.importWithMaterialButton)
        self.importWithMaterialButton.setChecked(True)
        #
        self.importWithAovButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withAov', self.importWithAovButton)
        self.importWithAovButton.setCheckable(False)
        #
        self._astShaderVariantLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'variant', self._astShaderVariantLabel)
        self._astShaderVariantLabel.setChooseEnable(True)
        #
        self._importShaderButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'importShader', self._importShaderButton)
        self._importShaderButton.clicked.connect(self.setImportShader)
        #
        self._cleanSceneButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'astUnitClearScene', self._cleanSceneButton)
        self._cleanSceneButton.clicked.connect(self.setCleanScene)
        #
        self._renameSceneButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'astUnitRenameScene', self._renameSceneButton)
        self._renameSceneButton.clicked.connect(self.setRenameScene)
        #
        self.usePathButton = qtWidgets.QtRadioCheckbutton()
        toolBox.setButton(inData, 'usePath', self.usePathButton)
        self.usePathButton.setChecked(True)
        #
        self.useNameButton = qtWidgets.QtRadioCheckbutton()
        toolBox.setButton(inData, 'useName', self.useNameButton)
        #
        self.useGeomButton = qtWidgets.QtRadioCheckbutton()
        toolBox.setButton(inData, 'useGeom', self.useGeomButton)
        self.useGeomButton.setCheckable(False)
        #
        self._loadMeshIndexButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'loadMeshIndex', self._loadMeshIndexButton)
        self._loadMeshIndexButton.clicked.connect(self._loadAstGeometryObjectsIndexCmd)
        #
        self._loadRigProductButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'loadRigAsset', self._loadRigProductButton)
        self._loadRigProductButton.setPressable(False)
        #
        toolBox.setSeparators(inData)
    #
    def setBtnState(self):
        assetName = self.connectObject().assetName
        #
        assetIndex = datAsset.getAssetIndex(assetName)
        self._importShaderButton.setPressable([False, True][self.getShaderVariant() is not None])
        #
        compIndexKeys = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        self._loadMeshIndexButton.setPressable([False, True][compIndexKeys != {}])
    #
    def setAstVariantUiLabelShow(self):
        assetName = self.connectObject().assetName
        #
        assetIndex = datAsset.getAssetIndex(assetName)
        variantLis = dbGet.getDbAssetVariants(assetIndex)
        #
        self._astShaderVariantLabel.setChooseClear()
        if variantLis:
            self._astShaderVariantLabel.setDatumLis(variantLis)
            self._astShaderVariantLabel.setChoose(prsVariants.Util.astDefaultVersion)
        #
        self.setBtnState()
    #
    def setImportShader(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.getShaderVariant()
        assetStage = self.connectObject().assetStage
        #
        isWithMaterial = self.importWithMaterialButton.isChecked()
        shaderGeomObjects = datAsset.getAstMeshObjects(assetName, 1)
        if shaderGeomObjects:
            maUtils.setDisplayMode(5)
            if isWithMaterial:
                isExistsMaterial = dbGet.getDbExistsAstModelMaterial(assetIndex, assetVariant)
                if isExistsMaterial:
                    [maShdr.setObjectCleanShadingEngine(i) for i in shaderGeomObjects]
                    #
                    assetOp.setUnusedShaderClear()
                    #
                    maAstLoadCmds.astUnitModelMaterialLoadCmd(
                        projectName,
                        assetIndex,
                        assetCategory, assetName, assetVariant, assetStage,
                        collectionTexture=True, useServerTexture=True
                    )
                    [maShdr.setObjectDefaultShadingEngine(i) for i in shaderGeomObjects]
                    #
                    bscObjects.If_Message(
                        u'Import Nde_ShaderRef', u'Complete'
                    )
                else:
                    bscObjects.If_Message(
                        u'Nde_ShaderRef', u'Non-Exists'
                    )
    @staticmethod
    def setCleanScene():
        maAstUploadCmds.astUnitSceneClearCmd()
    #
    def setRenameScene(self):
        projectName = self.connectObject().projectName
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        renderer = projectPr.getProjectMayaRenderer(projectName)
        #
        maAstUploadCmds.astUnitSceneRenameCmd_(
            assetName, assetVariant, assetStage,
            renderer
        )
    #
    def _loadAstGeometryObjectsIndexCmd(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetName = self.connectObject().assetName
        #
        isUsePath = self.usePathButton.isChecked()
        isUseName = self.useNameButton.isChecked()
        mode = 0
        if isUseName:
            mode = 1
        objectIndexes = dbGet.getDbGeometryObjectsIndexDic(assetIndex)
        if objectIndexes:
            maDbAstCmds.dbAstLoadGeometryObjectsIndex(
                assetIndex,
                assetName,
                objectIndexes,
                mode
            )
            #
            bscObjects.If_Message(
                u'Load Mesh Index', u'Complete'
            )
        else:
            bscObjects.If_Message(
                u'Mesh', u'Non-Exists'
            )
    #
    def getShaderVariant(self):
        return self._astShaderVariantLabel.datum()
    #
    def setupUnitWidgets(self):
        self._astUtilsGraphToolUiBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._astUtilsGraphToolUiBox)
        self._astUtilsGraphToolUiBox.setTitle('Asset Utilities Graph')
        #
        self._astModelPropHierToolUiBox = qtWidgets.QtToolbox()
        self._astModelPropHierToolUiBox.hide()
        self.mainLayout().addWidget(self._astModelPropHierToolUiBox)
        self._astModelPropHierToolUiBox.setTitle('Asset Prop Graph')
        #
        self._astModelSolClothHierToolUiBox = qtWidgets.QtToolbox()
        self._astModelSolClothHierToolUiBox.hide()
        self.mainLayout().addWidget(self._astModelSolClothHierToolUiBox)
        self._astModelSolClothHierToolUiBox.setTitle('Asset Solver - Cloth Graph')
        #
        self._astModelSolverHairGraphToolUiBox = qtWidgets.QtToolbox()
        self._astModelSolverHairGraphToolUiBox.hide()
        self.mainLayout().addWidget(self._astModelSolverHairGraphToolUiBox)
        self._astModelSolverHairGraphToolUiBox.setTitle('Asset Solver - Hair Graph')
        #
        self.astLightHierToolUiBox = qtWidgets.QtToolbox()
        self.astLightHierToolUiBox.hide()
        self.mainLayout().addWidget(self.astLightHierToolUiBox)
        self.astLightHierToolUiBox.setTitle('Asset Light Graph')
        #
        self._astLightToolUiBox = qtWidgets.QtToolbox()
        self._astLightToolUiBox.hide()
        self.mainLayout().addWidget(self._astLightToolUiBox)
        self._astLightToolUiBox.setTitle('Asset Light')
        #
        self._astUtilsToolUiBox = qtWidgets.QtToolbox()
        self.mainLayout().addWidget(self._astUtilsToolUiBox)
        self._astUtilsToolUiBox.setTitle('Asset Utilities')
        self.setupAstUtilsToolUiBox(self._astUtilsToolUiBox)


#
class IfAstModelInfoToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Model,
        lxConfigure.LynxiProduct_Asset_Link_Rig,
        lxConfigure.LynxiProduct_Asset_Link_Groom,
        lxConfigure.LynxiProduct_Asset_Link_Solver,
        lxConfigure.LynxiProduct_Asset_Link_Light
    ]
    UnitTitle = 'Information Tool Unit'
    UnitIcon = 'window#infoToolPanel'
    UnitTooltip = u'''信息工具模块'''
    #
    w = 80
    #
    geometryRadarChartConfig = ['worldArea', 'shell', 'vertex', 'edge', 'face', 'triangle']
    meshConstantConfig = ['geometry', 'geometryShape', 'map', 'mapShape']
    materialEvaluateConfig = ['material', 'node', 'connection', 'textureNode', 'texture']
    materialConstantConfig = ['Nde_Node', 'Relation']
    def __init__(self, *args, **kwargs):
        super(IfAstModelInfoToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self.isMeshChanged = False
        self.assetData = {}
        self.statisticsData = []
        #
        self.setupUnitWidgets()
    #
    def refreshMethod(self):
        pass
    #
    def setupGeometryQtTab(self, layout):
        self._astGeometryRadarChart = qtWidgets.QtRadarchart()
        layout.addWidget(self._astGeometryRadarChart)
        #
        self._astGeometrySectorChart = qtWidgets.QtSectorchart()
        layout.addWidget(self._astGeometrySectorChart)
    #
    def setupShaderQtTab(self, layout):
        self._astModelShaderRadarChart = qtWidgets.QtRadarchart()
        layout.addWidget(self._astModelShaderRadarChart)
        #
        self._astModelShaderSectorChart = qtWidgets.QtSectorchart()
        layout.addWidget(self._astModelShaderSectorChart)
    #
    def setTabSwitch(self):
        if self.connectObject() is not None:
            if self._tabWidget.currentIndex() == 0:
                self.setGeometryChartUpdate()
            if self._tabWidget.currentIndex() == 1:
                self.setShaderChartUpdate()
    #
    def setGeometryChartUpdate(self):
        self.setGeometryRadarChartUpdate()
        self.setGeometrySectorChartUpdate()
    #
    def setGeometryRadarChartUpdate(self):
        chartDatum = self.getGeometryRadarChartDatum()
        if chartDatum:
            self._astGeometryRadarChart.setChartDatum(chartDatum)
    #
    def setGeometrySectorChartUpdate(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        #
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        namespace = self.connectObject().assetNamespace
        #
        self.isMeshChanged = False
        #
        constantData = datAsset.getAstGeometryObjectsConstantData(
            assetIndex,
            assetCategory, assetName,
            namespace
        )
        if constantData:
            totalArray, pathChangedArray, geoChangedArray, geoShapeChangedArray, mapChangedArray, mapShapeChangedArray = constantData
            totalCount = len(totalArray)
            pathChangedCount = 0
            geomChangedCount = 0
            geoShapeChangedCount = 0
            mapChangedCount = 0
            mapShapeChangedCount = 0
            #
            if totalCount:
                pathChangedCount = len(pathChangedArray)
                geomChangedCount = len(geoChangedArray)
                geoShapeChangedCount = len(geoShapeChangedArray)
                mapChangedCount = len(mapChangedArray)
                mapShapeChangedCount = len(mapShapeChangedArray)
            #
            if geomChangedCount != 0:
                self.isMeshChanged = True
            #
            data = [
                ('Obj - Path', totalCount, totalCount - pathChangedCount),
                ('Geom - Topo', totalCount, totalCount - geomChangedCount),
                ('Geom - Shape', totalCount, totalCount - geoShapeChangedCount),
                ('Map - Topo', totalCount, totalCount - mapChangedCount),
                ('Map - Shape', totalCount, totalCount - mapShapeChangedCount)
            ]
            self._astGeometrySectorChart.setChartDatum(data)
    #
    def setShaderChartUpdate(self):
        self.setShaderRadarChartUpdate()
        self.setShaderSectorChartUpdate()
    #
    def setShaderRadarChartUpdate(self):
        chartDatum = self.getShaderRadarChartDatum()
        if chartDatum:
            self._astModelShaderRadarChart.setChartDatum(chartDatum)
    #
    def setShaderSectorChartUpdate(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetNamespace = self.connectObject().assetNamespace
        #
        constantData = datAsset.getMaterialsConstantData(
            assetIndex, projectName, assetCategory, assetName, assetVariant,
            assetNamespace
        )
        if constantData:
            totalArray, composeChangedArray, attributeChangedArray, relationChangedArray, objectSetChangedArray = constantData
            totalCount = len(totalArray)
            composeChangedCount = 0
            attributeChangedCont = 0
            relationChangedCount = 0
            objectSetChangerCount = 0
            #
            if totalCount:
                composeChangedCount = len(composeChangedArray)
                attributeChangedCont = len(attributeChangedArray)
                relationChangedCount = len(relationChangedArray)
                objectSetChangerCount = len(objectSetChangedArray)
            #
            data = [
                ('Matl - Component', totalCount, totalCount - composeChangedCount),
                ('Matl - Attribute', totalCount, totalCount - attributeChangedCont),
                ('Matl - Relation', totalCount, totalCount - relationChangedCount),
                ('Obj - Set', totalCount, totalCount - objectSetChangerCount)
            ]
            self._astModelShaderSectorChart.setChartDatum(data)
        self._astModelShaderSectorChart.update()
    #
    def getGeometryRadarChartDatum(self):
        lis = []
        #
        chartConfig = self.geometryRadarChartConfig
        #
        assetIndex = self.connectObject().assetIndex
        #
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        assetNamespace = self.connectObject().assetNamespace
        #
        prodGeometryObjects = datAsset.getAstMeshObjects(assetName, 1, assetNamespace)
        #
        if prodGeometryObjects:
            localDatumDic = datAsset.getMeshObjectsEvaluateDic(prodGeometryObjects, 1)
            serverDatumDic = dbGet.getDbMeshConstantData(assetIndex)
            if serverDatumDic:
                self._astGeometryRadarChart.setImage(
                    dbGet.getDbAstPreviewFile(assetIndex, assetVariant)
                )
            for i in chartConfig:
                if i in localDatumDic:
                    explain = i
                    localValue = localDatumDic[i]
                    serverValue = 0
                    if i in serverDatumDic:
                        serverValue = serverDatumDic[i]
                    lis.append(
                        (explain, serverValue, localValue)
                    )
        #
        else:
            lis = [
                (i, 0, 0) for seq, i in enumerate(chartConfig)
            ]
        return lis
    #
    def getShaderRadarChartDatum(self):
        lis = []
        #
        evaluateConfig = self.materialEvaluateConfig
        #
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetStage = self.connectObject().assetStage
        assetNamespace = self.connectObject().assetNamespace
        #
        prodGeometryObjects = datAsset.getAstMeshObjects(assetName, 1, assetNamespace)
        yetis = datAsset.getYetiObjects(assetName)
        #
        if prodGeometryObjects:
            localDatumDic = datAsset.getMaterialEvaluateData(prodGeometryObjects, 1)
            serverDatumDic = {}
            #
            for i in evaluateConfig:
                if i in localDatumDic:
                    explain = i
                    value = localDatumDic[i]
                    serverValue = 0
                    if i in serverDatumDic:
                        serverValue = serverDatumDic[i]
                    lis.append((explain, serverValue, value))
        if not prodGeometryObjects:
            lis = [(i, 0, 0) for seq, i in enumerate(evaluateConfig)]
        return lis
    #
    def setupUnitWidgets(self):
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        self.mainLayout().addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        self._tabWidget.currentChanged.connect(self.setTabSwitch)
        # Nde_Geometry
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Nde_Geometry', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupGeometryQtTab(layout)
        # Nde_ShaderRef
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Nde_ShaderRef', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupShaderQtTab(layout)


#
class IfAstUploadToolUnit(_qtIfAbcWidget.IfToolUnitBasic):
    UnitConnectLinks = [
        lxConfigure.LynxiProduct_Asset_Link_Model,
        lxConfigure.LynxiProduct_Asset_Link_Rig,
        lxConfigure.LynxiProduct_Asset_Link_Groom,
        lxConfigure.LynxiProduct_Asset_Link_Solver,
        lxConfigure.LynxiProduct_Asset_Link_Light
    ]
    UnitTitle = 'Upload Tool Unit'
    UnitIcon = 'window#uploadToolPanel'
    UnitTooltip = u'''上传工具模块'''
    #
    astModelUploadTips = [
        u"提示：",
        u"1：点击 Model [ 0000 / 0000 ] 进行模型检查；",
        u"2：点击 Texture [ 0000 / 0000 ] 进行贴图检查；",
        u"3：修改 错误项目 ；",
        u"4：点击 Upload ！！！ 上传...",
    ]
    errorTips1 = [
        u"错误：",
        u"1：当前 资产 的 变体 的 模型 与 “default” 的版本不匹配！！！",
    ]
    errorTips2 = [
        u"错误：",
        u"1：当前 资产 的 模型 与服务器的的不匹配！",
    ]
    errorTips3 = [
        u"错误：",
        u"1：当前 资产 的 版本 与服务器的“时间”不匹配！！！",
    ]
    #
    astRigUploadTips = [
        u"提示：",
        u"1：点击 Control [ 0000 / 0000 ] 进行控制器检查；",
        u"2：修改 错误项目 ；",
        u"3：点击 Upload ！！！ 上传...",
    ]
    #
    astCfxUploadTips = [
        u"提示：",
        u"1：点击 Nde_Node [ 0000 / 0000 ] 进行毛发检查；",
        u"2：点击 Texture [ 0000 / 0000 ] 进行贴图检查；",
        u"3：修改 错误项目 ；",
        u"4：点击 Upload ！！！ 上传...",
    ]
    #
    astSolverUploadTips = [
        u"提示：",
        u"1：点击 Solver - Guide [ 0000 / 0000 ] 进行模拟检查；",
        u"3：修改 错误项目 ；",
        u"4：点击 Upload ！！！ 上传...",
    ]
    #
    astLightUploadTips = [
        u"提示：",
        u"1：点击 Nde_Node [ 0000 / 0000 ] 进行灯光检查；",
        u"2：点击 Texture [ 0000 / 0000 ] 进行贴图检查；",
        u"3：修改 错误项目 ；",
        u"4：点击 Upload ！！！ 上传...",
    ]
    astCheckTips = [
        u"提示：",
        u"1：点击右边列表查看 错误项目 ；",
        u"2：修改 错误项目...",
    ]
    uploadTips = [
        u"提示：",
        u"1：请点击 Upload ！！！ 上传...",
    ]
    w = 80
    #
    dicAstTip = {
        0: 'Tip(s)',
        'tip': [0, 1, 0, 1, 4, none],
        2: 'Note(s)',
        'note': [0, 3, 0, 1, 4, 'Notes']
    }
    #
    dicAstPreview = {
        0: 'Config(s)',
        'useDefaultView': [1, 1, 0, 1, 2, 'Default View'], 'useDefaultLight': [1, 1, 2, 1, 2, 'Default Light'],
        2: 'Action(s)',
        'makeViewportSnapshot': [1, 3, 0, 1, 2, 'Make Snapshot ( Viewport )', 'svg_basic@svg#camera'],
        'makeRenderSnapshot': [1, 3, 2, 1, 2, 'Make Snapshot ( Render )', 'svg_basic@svg#render']
    }
    # Asset
    dicAstCheck = {
        'mainCheck': [0, 0, 0, 1, 2, 'Main', 'svg_basic@svg#info'], 'subCheck': [0, 0, 2, 1, 2, 'Sub', 'svg_basic@svg#info']
    }
    #
    dicAstUpload = {
        0: 'Config(s)',
        'withProduct': [0, 1, 0, 1, 1, 'Product'],  'withAssembly': [0, 1, 2, 1, 1, 'Assembly'], 'withAnimation': [0, 1, 3, 1, 1, 'Animation'],
        'percentage': [0, 2, 0, 1, 4, 'Percentage'],
        'frame': [0, 3, 0, 1, 4, 'Frame'],
        'withAov': [0, 4, 0, 1, 2, 'Aov(s)'],
        5: 'Action(s)',
        'upload': [0, 6, 0, 1, 4, u'Upload ！！！', 'svg_basic@svg#upload']
    }
    #
    dicAstModelExtend = {
        'updateSolverGeometry': [0, 0, 0, 1, 4, 'Update Solver Nde_Geometry', 'svg_basic@svg#upload']
    }
    # Variant
    dicAstVariantModify = {
        'variant': [0, 0, 0, 1, 2, 'Variant'], 'setVariant': [0, 0, 2, 1, 2, 'Set Variant ( Material )', 'svg_basic@svg#python']
    }
    def __init__(self, *args, **kwargs):
        super(IfAstUploadToolUnit, self).__init__(*args, **kwargs)
        self._initToolUnitBasic()
        #
        self._isAstMainCheckEnable = True
        self._isAstSubCheckEnable = True
        #
        self._astUpdateCheckResult = False
        #
        self._astModelMainCheckResult = False
        self._astRigMainCheckResult = False
        self._astCfxMainCheckResult = False
        self._astLightMainCheckResult = False
        self._astRigSolMainCheckResult = False
        #
        self.astTextureCheckResult = False
        #
        self.isAstUploadModel = False
        self.isAstUploadRig = True
        self.isAstUploadCfx = False
        self.isAstUploadRigSol = False
        self.isAstUploadLight = False
        #
        self.setupUnitWidgets()
    #
    def refreshMethod(self):
        if self.connectObject() is not None:
            self._initAstUploadUiBox()
    #
    def setupUploadTab(self, layout):
        self._astTipToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._astTipToolUiBox)
        self._astTipToolUiBox.setTitle('Tip & Note')
        #
        self._astSnapToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._astSnapToolUiBox)
        self._astSnapToolUiBox.setTitle('Snapshot')
        #
        self._uploadToolWidget = qtCore.QWidget_()
        layout.addWidget(self._uploadToolWidget)
        uploadLayout = qtCore.QVBoxLayout_(self._uploadToolWidget)
        #
        self._checkToolUiBox = qtWidgets.QtToolbox()
        uploadLayout.addWidget(self._checkToolUiBox)
        self._checkToolUiBox.setTitle('Check')
        #
        self._uploadToolUiBox = qtWidgets.QtToolbox()
        uploadLayout.addWidget(self._uploadToolUiBox)
        self._uploadToolUiBox.setTitle('Upload')
    #
    def setupExtendTab(self, layout):
        self._extendToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._extendToolUiBox)
        self._extendToolUiBox.setTitle('Extend')
        #
        self._variantToolUiBox = qtWidgets.QtToolbox()
        layout.addWidget(self._variantToolUiBox)
        self._variantToolUiBox.setTitle('Variant')
    #
    def setupAstTipToolUiBox(self, toolBox):
        inData = self.dicAstTip
        #
        self._tipTextBrower = qtWidgets.QtTextbrower()
        toolBox.setInfo(inData, 'tip', self._tipTextBrower)
        self._tipTextBrower.setEnterEnable(False)
        #
        self._noteTexBrower = qtWidgets.QtTextbrower()
        toolBox.setButton(inData, 'note', self._noteTexBrower)
        self._noteTexBrower.setTooltip(
            u'''输入 备注信息'''
        )
        self._noteTexBrower.entryChanged.connect(self.getIsIgnoreError)
        #
        toolBox.setSeparators(inData)
    #
    def setupAstUploadToolUiBox(self, toolBox):
        inData = self.dicAstUpload
        #
        self._astWithProductButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withProduct', self._astWithProductButton)
        self._astWithProductButton.setChecked(True)
        self._astWithProductButton.setTooltip(
            u'''启用 / 关闭 上传 资产产品文件：\n1，启用 上传时会上传该项目。'''
        )
        #
        self._astWithAssemblyButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withAssembly', self._astWithAssemblyButton)
        self._astWithAssemblyButton.setTooltip(
            u'''启用 / 关闭 上传 资产组装文件：\n1，启用 上传时会上传该项目。'''
        )
        #
        self._assemblyPercentLabel = qtWidgets.QtValueEnterlabel()
        self._assemblyPercentLabel.hide()
        toolBox.setInfo(inData, 'percentage', self._assemblyPercentLabel)
        self._assemblyPercentLabel.setEnterEnable(True)
        self._assemblyPercentLabel.setDefaultValue((50, 50))
        self._astWithAssemblyButton.toggled.connect(self._assemblyPercentLabel.setVisible)
        self._astWithAssemblyButton.clicked.connect(self.setAssemblyPercentageBoxShow)
        #
        self._astWithAnimationButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withAnimation', self._astWithAnimationButton)
        self._astWithAnimationButton.setCheckable(False)
        self._astWithAnimationButton.setTooltip(
            u'''启用 / 关闭 上传 资产动画文件：\n1，启用 上传时会上传该项目。'''
        )
        #
        self._astFrameLabel = qtWidgets.QtValueEnterlabel()
        self._astFrameLabel.hide()
        toolBox.setInfo(inData, 'frame', self._astFrameLabel)
        self._astFrameLabel.setEnterEnable(True)
        self._astFrameLabel.setDefaultValue(maUtils.getFrameRange())
        self._astWithAnimationButton.toggled.connect(self._astFrameLabel.setVisible)
        self._astWithAnimationButton.clicked.connect(self.setFrameBoxShow)
        #
        self._astWithAovButton = qtWidgets.QtCheckbutton()
        toolBox.setButton(inData, 'withAov', self._astWithAovButton)
        self._astWithAovButton.setChecked(False)
        self._astWithAovButton.setTooltip(
            u'''启用 / 关闭 上传 Aov(s)数据：\n1，启用 上传时会上传该项目。'''
        )
        #
        self._astUploadButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'upload', self._astUploadButton)
        self._astUploadButton._setQtPressStatus(qtCore.OnStatus)
        self._astUploadButton.setTooltip(
            u'点击 上传 / 更新 资产：\n1，检查通过后激活按钮。'
        )
        #
        toolBox.setSeparators(inData)
    #
    def setupAstCheckToolUiBox(self, toolBox):
        inData = self.dicAstCheck
        #
        self._astMainCheckButton = qtWidgets.QtPressbutton()
        self._astMainCheckButton.setPercentEnable(True)
        toolBox.setButton(inData, 'mainCheck', self._astMainCheckButton)
        self._astMainCheckButton.setTooltip(
            u'''点击 进行 主要项目检查（模型，节点）'''
        )
        #
        self._astSubCheckButton = qtWidgets.QtPressbutton()
        self._astSubCheckButton.setPercentEnable(True)
        toolBox.setButton(inData, 'subCheck', self._astSubCheckButton)
        self._astSubCheckButton.setTooltip(
            u'''点击 进行 次要项目检查（材质， 贴图）'''
        )
        #
        toolBox.setSeparators(inData)
    #
    def setupAstSnapshotToolUiBox(self, toolBox):
        toolBox.setUiData(self.dicAstPreview)
        #
        self._useDefaultViewButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('useDefaultView', self._useDefaultViewButton)
        self._useDefaultViewButton.setChecked(True)
        self._useDefaultViewButton.setTooltip(
            u'''启用 / 关闭 截屏的时候 是否使用 默认摄像机视角'''
        )
        #
        self._useDefaultLightButton = qtWidgets.QtCheckbutton()
        toolBox.addButton('useDefaultLight', self._useDefaultLightButton)
        self._useDefaultLightButton.setChecked(True)
        self._useDefaultLightButton.setTooltip(
            u'''启用 / 关闭 截屏（渲染）的时候 是否创建 默认灯光'''
        )
        #
        self._makeViewportSnapshotButton = qtWidgets.QtPressbutton()
        toolBox.addButton('makeViewportSnapshot', self._makeViewportSnapshotButton)
        self._makeViewportSnapshotButton.released.connect(self._astViewportSnapshotCmd)
        self._makeViewportSnapshotButton.setTooltip(
            u'''点击 上传视窗截屏'''
        )
        #
        self._makeRenderSnapshotButton = qtWidgets.QtPressbutton()
        toolBox.addButton('makeRenderSnapshot', self._makeRenderSnapshotButton)
        self._makeRenderSnapshotButton.clicked.connect(self._astRenderSnapshotCmd)
        self._makeRenderSnapshotButton.setTooltip(
            u'''点击 上传渲染截屏'''
        )
        #
        toolBox.addSeparators()
    #
    def setupAstModelExtendToolUiBox(self, toolBox):
        inData = self.dicAstModelExtend
        #
        self._withSolverGeometryButton = qtWidgets.QtPressbutton()
        toolBox.setButton(inData, 'updateSolverGeometry', self._withSolverGeometryButton)
    #
    def setupAstVariantModifyToolUiBox(self, toolBox):
        inData = self.dicAstVariantModify
        #
        self._astVariantChangeLabel = qtWidgets.QtEnterlabel()
        toolBox.setInfo(inData, 'variant', self._astVariantChangeLabel)
        self._astVariantChangeLabel.setChooseEnable(True)
        self._astVariantChangeLabel.chooseChanged.connect(self.setVarBtnState)
        #
        self._astVariantChangeButton = qtWidgets.QtPressbutton()
        self._astVariantChangeButton.setPressable(False)
        toolBox.setButton(inData, 'setVariant', self._astVariantChangeButton)
        self._astVariantChangeButton.clicked.connect(self.setAssetVariant)
    # Model
    def _initAstModelUploadTool(self):
        # Check
        self._astMainCheckButton.clicked.connect(self.setAstModelCheck)
        self._astMainCheckButton.clicked.connect(self._updateAstModelCheckResult)
        self._astSubCheckButton.clicked.connect(self.setAstTextureCheck)
        self._astSubCheckButton.clicked.connect(self._updateAstModelCheckResult)
        # Upload
        self._astUploadButton.clicked.connect(self._astModelUploadCmd)
    #
    def _initAstRigUploadTool(self):
        # Check
        self._checkToolUiBox.hide()
        # Upload
        self._astUploadButton.clicked.connect(self._uploadAstRigCmd)
    #
    def _initAstCfxUploadTool(self):
        # Check
        self._astMainCheckButton.clicked.connect(self.setAstCfxCheck)
        self._astMainCheckButton.clicked.connect(self._updateAstCfxCheckResult)
        self._astSubCheckButton.clicked.connect(self.setAstTextureCheck)
        self._astSubCheckButton.clicked.connect(self._updateAstCfxCheckResult)
        # Upload
        self._astUploadButton.clicked.connect(self._uploadAstCfxCmd)
    #
    def _initAstRigSolUploadTool(self):
        # Check
        self._astMainCheckButton.clicked.connect(self.setAstRigSolCheck)
        self._astMainCheckButton.clicked.connect(self._updateAstRigSolCheckResult)
        #
        self._astSubCheckButton.setPressable(False)
        # Upload
        self._astUploadButton.clicked.connect(self._uploadAstSolverCmd)
    #
    def _initAstLightUploadTool(self):
        # Check
        self._astMainCheckButton.clicked.connect(self.setAstLightCheck)
        self._astMainCheckButton.clicked.connect(self._updateAstLightCheckResult)
        # Upload
        self._astUploadButton.clicked.connect(self._uploadAstLightCmd)
    #
    def setupAstVariantBox(self, toolBox):
        pass
    #
    def getAssetUploadEnable(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        if prsMethods.Asset.isModelStageName(assetStage) or prsMethods.Asset.isGroomStageName(assetStage):
            isWithAssembly = assetPr.getAssetIsAssemblyEnabled(assetIndex)
            self._astWithAssemblyButton.setChecked(isWithAssembly)
        else:
            self._astWithAssemblyButton.setCheckable(False)
    #
    def setAstVariantUiLabelShow(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        chooseBox = self._astVariantChangeLabel
        #
        if chooseBox:
            variants = assetPr.getAssetVariantLis(assetIndex)
            if variants:
                chooseBox.setDatumLis(variants)
                chooseBox.setChoose(assetVariant)
            else:
                chooseBox.setLockVisible(False)
                chooseBox.setDatum(prsVariants.Util.astDefaultVersion)
    #
    def setAssemblyPercentageBoxShow(self):
        assetName = self.connectObject().assetName
        assetStage = self.connectObject().assetStage
        #
        rangeBox = self._assemblyPercentLabel
        #
        assetIndex = datAsset.getAssetIndex(assetName)
        percentage = dbGet.getDbAssemblyPercentage(assetIndex)
        #
        if percentage:
            rangeBox.setDefaultValue((percentage[0], percentage[1]))
        else:
            rangeBox.setDefaultValue((50, 50))
    #
    def setFrameBoxShow(self):
        rangeBox = self._astFrameLabel
        rangeBox.setDefaultValue(maUtils.getFrameRange())
    #
    def setAstUpdateCheck(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        serverProductFile = assetPr.astUnitProductFile(
            lxConfigure.LynxiRootIndex_Server,
            projectName,
            assetCategory, assetName, assetVariant, assetStage
        )[1]
        #
        if bscMethods.OsFile.isExist(serverProductFile):
            timestamp = bscMethods.OsFile.mtimestamp(serverProductFile)
            serverViewTime = bscMethods.OsTimestamp._timestampToPrettify(timestamp)
            #
            astUnitRootGroup = prsMethods.Asset.rootName(assetName)
            localViewTime = maUtils.getAttrDatum(astUnitRootGroup, prsVariants.Util.basicUpdateAttrLabel)
            #
            self._astUpdateCheckResult = serverViewTime < localViewTime
        else:
            self._astUpdateCheckResult = True
    # Model
    def setAstModelCheck(self):
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        #
        tipsLabel = self._tipTextBrower
        keyword = 'Nde_Geometry'
        #
        geometryObjects = datAsset.getAstMeshObjects(assetName, 1)
        #
        self.connectObject().setAstMeshTransCheck()
        self.connectObject().setAstMeshGeomCheck()
        self.connectObject().setAstMeshHistCheck()
        #
        self.connectObject().setAstModelCheckBox()
        # Debug
        errorData = self.connectObject().astModelMeshErrorData
        #
        checkResult = False
        if geometryObjects:
            maxCount = len(geometryObjects)
            checkOn = maxCount - len(errorData)
            #
            self._astMainCheckButton.setPercent(maxCount, checkOn)
            #
            tipsLabel.setRule(self.astCheckTips)
            if checkOn == maxCount:
                checkResult = True
        if not geometryObjects:
            self._astMainCheckButton.setPressable(False)
            bscObjects.If_Message(
                u'%s is' % keyword, u'Non - Exists'
            )
        #
        self._astModelMainCheckResult = checkResult
    # Rig
    def setAstRigCheck(self):
        pass
    # Cfx
    def setAstCfxCheck(self):
        tipsLabel = self._tipTextBrower
        keyword = 'Nde_Node'
        #
        self.connectObject().setAstCfxCheckCmd()
        checkData = self.connectObject().astCfxFurData
        errorData = self.connectObject().astCfxFurErrorData
        #
        checkResult = False
        #
        if checkData:
            maxCount = len(checkData)
            checkOn = maxCount - len(errorData)
            #
            self._astMainCheckButton.setPercent(maxCount, checkOn)
            #
            tipsLabel.setRule(self.astCheckTips)
            if checkOn == maxCount:
                checkResult = True
        elif not checkData:
            self._astMainCheckButton.setPressable(False)
            #
            bscObjects.If_Message(
                u'%s is' % keyword, u'Non - Exists'
            )
        #
        self._astCfxMainCheckResult = checkResult
    #
    def setAstRigSolCheck(self):
        tipsLabel = self._tipTextBrower
        keyword = 'Nde_Node'
        #
        self.connectObject().setAstSolverCheckCmd()
        #
        checkData = self.connectObject()._astSolverCheckItemLis
        errorData = self.connectObject()._astSolverErrorItemLis
        #
        checkResult = False
        #
        if checkData:
            maxCount = len(checkData)
            checkOn = maxCount - len(errorData)
            #
            self._astMainCheckButton.setPercent(maxCount, checkOn)
            #
            tipsLabel.setRule(self.astCheckTips)
            if checkOn == maxCount:
                checkResult = True
        else:
            self._astMainCheckButton.setPressable(False)
            #
            bscObjects.If_Message(
                u'%s is' % keyword, u'Non - Exists'
            )
        #
        self._astRigSolMainCheckResult = checkResult
    #
    def setAstLightCheck(self):
        tipsLabel = self._tipTextBrower
        keyword = 'Nde_Node'
        #
        self.connectObject().setViewAstLightCheckResult()
        #
        checkData = []
        errorData = []
        #
        checkResult = False
        #
        if checkData:
            maxCount = len(checkData)
            checkOn = maxCount - len(errorData)
            #
            self._astMainCheckButton.setPercent(maxCount, checkOn)
            #
            tipsLabel.setRule(self.astCheckTips)
            if checkOn == maxCount:
                checkResult = True
        else:
            self._astMainCheckButton.setPressable(False)
            #
            bscObjects.If_Message(
                u'%s is' % keyword, u'Non - Exists'
            )
        #
        self._astLightMainCheckResult = checkResult
    #
    def setAstTextureCheck(self):
        if self.connectObject() is not None:
            assetCategory = self.connectObject().assetCategory
            assetName = self.connectObject().assetName
            assetStage = self.connectObject().assetStage
            #
            shaderObjects = []
            geometryObjects = datAsset.getAstMeshObjects(assetName, 1)
            shaderObjects.extend(geometryObjects)
            yetis = datAsset.getYetiObjects(assetName)
            shaderObjects.extend(yetis)
            #
            materials = []
            shadingGroups = maShdr.getObjectsShadingEngineLis(shaderObjects)
            materials.extend(shadingGroups)
            #
            _astSubCheckButton = self._astSubCheckButton
            #
            tipsLabel = self._tipTextBrower
            #
            if _astSubCheckButton is not None:
                self.connectObject().setAstTextureCheckView()
                # Debug
                checkData = self.connectObject().astTextureData
                errorData = self.connectObject().astTextureErrorData
                #
                checkResult = False
                #
                if checkData:
                    maxCount = len(checkData)
                    checkOn = maxCount - len(errorData)
                    _astSubCheckButton.setPercent(maxCount, checkOn)
                    tipsLabel.setRule(self.astCheckTips)
                    if checkOn == maxCount:
                        checkResult = True
                #
                else:
                    checkResult = True
                    _astSubCheckButton.setPressable(False)
                    #
                    bscObjects.If_Message(
                        u'Texture ( Nde_Node ) is',
                        u'Non - Exists'
                    )
                #
                self.astTextureCheckResult = checkResult
    #
    def _astViewportSnapshotCmd(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetNamespace = self.connectObject().assetNamespace
        #
        isUseDefaultView = self._useDefaultViewButton.isChecked()
        #
        viewportPreview0 = dbGet.dbAstViewportPreviewFile(assetIndex)
        #
        root = assetPr.astUnitModelProductGroupName(assetName, assetNamespace)
        #
        overrideColor = bscMethods.String.toRgb(assetName, maximum=1.0)
        maFile.makeSnapshot(
            root, viewportPreview0,
            useDefaultMaterial=1,
            width=720, height=720,
            useDefaultView=isUseDefaultView,
            overrideColor=overrideColor
        )
        #
        bscObjects.If_Message(
            u'Make Snapshot ( Viewport )', u'Complete'
        )
    #
    def _astRenderSnapshotCmd(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetNamespace = self.connectObject().assetNamespace
        #
        isUseDefaultView = self._useDefaultViewButton.isChecked()
        isUseDefaultLight = self._useDefaultLightButton.isChecked()
        #
        root = assetPr.astUnitModelProductGroupName(assetName, assetNamespace)
        #
        modelIndex = dbGet.getDbAstModelIndex(assetIndex, assetVariant)
        #
        directory = prsVariants.Database.assetPreview
        renderPreview = directory + '/' + modelIndex + prsVariants.Util.pngExt
        #
        renderer = projectPr.getProjectMayaRenderer(projectName)
        #
        maRender.setRenderSnapshot(
            root, renderPreview, renderer,
            width=720, height=720,
            useDefaultView=isUseDefaultView, useDefaultLight=isUseDefaultLight
        )
        #
        bscObjects.If_Message(
            u'Make Snapshot ( Render )', u'Complete'
        )
    # Result
    def _updateAstModelCheckResult(self):
        if self._astModelMainCheckResult is True and self.astTextureCheckResult is True:
            self.isAstUploadModel = True
            self._tipTextBrower.setRule(self.uploadTips)
        else:
            self.isAstUploadModel = False
            self._tipTextBrower.setRule(self.astModelUploadTips)
        #
        self._astUploadButton.setPressable(self.isAstUploadModel)
    #
    def _updateAstRigCheckResult(self):
        self.isAstUploadRig = True
        #
        self._tipTextBrower.setRule(self.astRigUploadTips)
        #
        self._astUploadButton.setPressable(self.isAstUploadRig)
    #
    def _updateAstCfxCheckResult(self):
        if self._astCfxMainCheckResult is True and self.astTextureCheckResult is True:
            self.isAstUploadCfx = True
            self._tipTextBrower.setRule(self.uploadTips)
        else:
            self.isAstUploadCfx = False
            self._tipTextBrower.setRule(self.astCfxUploadTips)
        #
        self._astUploadButton.setPressable(self.isAstUploadCfx)
    #
    def _updateAstRigSolCheckResult(self):
        if self._astRigSolMainCheckResult is True:
            self.isAstUploadRigSol = True
            self._tipTextBrower.setRule(self.uploadTips)
        else:
            self.isAstUploadRigSol = False
            self._tipTextBrower.setRule(self.astSolverUploadTips)
        #
        self._astUploadButton.setPressable(self.isAstUploadRigSol)
    #
    def _updateAstLightCheckResult(self):
        self._astLightMainCheckResult = True
        #
        if self._astLightMainCheckResult is True and self.astTextureCheckResult is True:
            self.isAstUploadLight = True
            self._tipTextBrower.setRule(self.uploadTips)
        else:
            self.isAstUploadLight = False
            self._tipTextBrower.setRule(self.astLightUploadTips)
        #
        self._astUploadButton.setPressable(self.isAstUploadLight)
    #
    def getIsIgnoreError(self):
        assetStage = self.connectObject().assetStage
        message = self._noteTexBrower.datum()
        if message == '88888888':
            self._astModelMainCheckResult = True
            self._astCfxMainCheckResult = True
            self.astTextureCheckResult = True
            #
            if prsMethods.Asset.isModelStageName(assetStage):
                self._updateAstModelCheckResult()
            elif prsMethods.Asset.isRigStageName(assetStage):
                self._updateAstRigCheckResult()
            elif prsMethods.Asset.isGroomStageName(assetStage):
                self._updateAstCfxCheckResult()
            #
            self._uploadToolWidget.show()
    #
    def setVarBtnState(self):
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        chooseBox = self._astVariantChangeLabel
        button = self._astVariantChangeButton
        #
        if chooseBox is not None and button is not None:
            newVariant = chooseBox.datum()
            button.setPressable([False, True][assetVariant != newVariant])
    #
    def setAssetVariant(self):
        assetIndex = self.connectObject().assetIndex
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        chooseBox = self._astVariantChangeLabel
        #
        if chooseBox:
            newAssetVariant = chooseBox.datum()
            if newAssetVariant and assetVariant:
                if newAssetVariant != assetVariant:
                    maHier.astUnitRefreshRoot(
                        assetIndex,
                        assetCategory, assetName, newAssetVariant, assetStage
                    )
                    #
                    self.connectObject().setAssetInfo(
                        assetIndex, assetCategory, assetName, newAssetVariant
                    )
                    #
                    self.setVarBtnState()
                    #
                    bscObjects.If_Message(
                        u'Set Variant', u'Complete'
                    )
    #
    def _initAstUploadUiBox(self):
        assetStage = self.connectObject().assetStage
        #
        self.setupAstTipToolUiBox(self._astTipToolUiBox)
        self.setupAstSnapshotToolUiBox(self._astSnapToolUiBox)
        self.setupAstCheckToolUiBox(self._checkToolUiBox)
        self.setupAstUploadToolUiBox(self._uploadToolUiBox)
        if prsMethods.Asset.isModelStageName(assetStage):
            self._initAstModelUploadTool()
            #
            self.setupAstModelExtendToolUiBox(self._extendToolUiBox)
            #
            self._tipTextBrower.setRule(self.astModelUploadTips)
            #
        elif prsMethods.Asset.isRigStageName(assetStage):
            self._initAstRigUploadTool()
            #
            self._tipTextBrower.setRule(self.astRigUploadTips)
        elif prsMethods.Asset.isGroomStageName(assetStage):
            self._initAstCfxUploadTool()
            #
            self._tipTextBrower.setRule(self.astCfxUploadTips)
        elif prsMethods.Asset.isSolverStageName(assetStage):
            self._initAstRigSolUploadTool()
            #
            self._tipTextBrower.setRule(self.astSolverUploadTips)
        elif prsMethods.Asset.isLightStageName(assetStage):
            self._initAstLightUploadTool()
            #
            self._tipTextBrower.setRule(self.astLightUploadTips)
        #
        self.getAssetUploadEnable()
        #
        self.setupAstVariantModifyToolUiBox(self._variantToolUiBox)
        self.setAstVariantUiLabelShow()
    #
    def _initAstCheck(self):
        assetStage = self.connectObject().assetStage
        #
        if prsMethods.Asset.isModelStageName(assetStage):
            self._isAstMainCheckEnable, self._isAstSubCheckEnable = True, True
            #
            self._astModelMainCheckResult, self.astTextureCheckResult = False, False
            self.isAstUploadModel = False
            self._tipTextBrower.setRule(self.astModelUploadTips)
            self._updateAstModelCheckResult()
        elif prsMethods.Asset.isRigStageName(assetStage):
            self._isAstMainCheckEnable, self._isAstSubCheckEnable = False, False
            #
            self._updateAstRigCheckResult()
        elif prsMethods.Asset.isGroomStageName(assetStage):
            self._isAstMainCheckEnable, self._isAstSubCheckEnable = True, True
            #
            self._astCfxMainCheckResult, self.astTextureCheckResult = False, False
            self.isAstUploadCfx = False
            self._tipTextBrower.setRule(self.astCfxUploadTips)
            self._updateAstCfxCheckResult()
        elif prsMethods.Asset.isSolverStageName(assetStage):
            self._isAstMainCheckEnable, self._isAstSubCheckEnable = True, False
            #
            self._astRigSolMainCheckResult = False
            self.isAstUploadRigSol = False
            self._tipTextBrower.setRule(self.astSolverUploadTips)
            self._updateAstRigSolCheckResult()
        elif prsMethods.Asset.isLightStageName(assetStage):
            self._isAstMainCheckEnable, self._isAstSubCheckEnable = True, True
            #
            self._astLightMainCheckResult, self.astTextureCheckResult = False, False
            self.isAstUploadLight = False
            self._tipTextBrower.setRule(self.astLightUploadTips)
            self._updateAstLightCheckResult()
        #
        self.setAstUpdateCheck()
        #
        self._astMainCheckButton.setPressable(self._isAstMainCheckEnable), self._astSubCheckButton.setPressable(self._isAstMainCheckEnable)
        self._astMainCheckButton.setPercentRest(), self._astSubCheckButton.setPercentRest()
        self._astUploadButton.setNameText(u'Upload {} ！！！'.format(
            bscMethods.StrCamelcase.toPrettify(prsMethods.Asset.stageName2linkName(assetStage))))
    #
    def _updateAstUploadState(self):
        self._initAstCheck()
        #
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        errorTips = self.errorTips1
        #
        isMeshChanged = self.connectObject().isMeshChanged
        isUpdateChecked = self._astUpdateCheckResult
        #
        isHide = False
        if isMeshChanged:
            if prsMethods.Asset.isModelStageName(assetStage):
                if assetVariant != prsVariants.Util.astDefaultVersion:
                    isHide = True
            elif prsMethods.Asset.isGroomStageName(assetStage) or prsMethods.Asset.isRigStageName(assetStage) or prsMethods.Asset.isLightStageName(assetStage):
                isHide = True
                errorTips = self.errorTips2
        #
        if isUpdateChecked is False:
            isHide = True
            errorTips = self.errorTips3
        #
        if isHide:
            self._uploadToolWidget.hide()
            self._tipTextBrower.setRule(errorTips)
        #
        else:
            self._uploadToolWidget.show()
    #
    def _uploadAstCmd(self):
        pass
    # Model
    def _astModelUploadCmd(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        if prsMethods.Asset.isModelStageName(assetStage):
            if self.isAstUploadModel:
                isRepairWithTrans = self.connectObject().withTransformationButton.isChecked()
                isRepairWithHistory = self.connectObject().withHistoryButton.isChecked()
                isRepairWithUnlockNormal = self.connectObject().withUnlockNormalButton.isChecked()
                isRepairWithSoftNormal = self.connectObject().withSoftNormalButton.isChecked()
                isRepairWithUv = self.connectObject().withUvButton.isChecked()
                #
                isRepairWithMaterial = self.connectObject().withMaterialButton.isChecked()
                isRepairWithTexture = self.connectObject().withTextureButton.isChecked()
                isRepairWithAov = self.connectObject().withAovButton.isChecked()
                #
                isWithProduct = self._astWithProductButton.isChecked()
                lodPercentageRange = self._assemblyPercentLabel.value()
                isWithAssembly = [(), lodPercentageRange][self._astWithAssemblyButton.isChecked()]
                isWithAnimation = self._astWithAnimationButton.isChecked()
                isWithAov = self._astWithAovButton.isChecked()
                #
                description = u'资产 - 模型 上传/更新'
                note = self._noteTexBrower.datum()
                #
                self.connectObject().hide()
                #
                maAstUploadCmds.astUnitModelUploadMainCmd(
                    projectName,
                    assetIndex,
                    assetCategory, assetName, assetVariant, assetStage,
                    withProduct=isWithProduct, withAssembly=isWithAssembly, withAnimation=isWithAnimation,
                    withAov=isWithAov,
                    description=description, notes=note,
                    # Mesh
                    repairTrans=isRepairWithTrans, repairHistory=isRepairWithHistory,
                    repairUnlockNormal=isRepairWithUnlockNormal, repairSoftNormal=isRepairWithSoftNormal,
                    repairUv=isRepairWithUv,
                    # Material
                    repairMatl=isRepairWithMaterial, repairTexture=isRepairWithTexture, repairAov=isRepairWithAov
                )
                timerA = threading.Timer(5, self.connectObject().close)
                timerA.start()
    # Rig
    def _uploadAstRigCmd(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        if prsMethods.Asset.isRigStageName(assetStage):
            if self.isAstUploadRig:
                isWithProduct = self._astWithProductButton.isChecked()
                isWithAssembly = self._astWithAssemblyButton.isChecked()
                #
                description = u'资产 - 绑定 上传/更新'
                note = self._noteTexBrower.datum()
                #
                self.connectObject().hide()
                #
                maAstUploadCmds.astUnitUploadRigMain(
                    assetIndex,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage,
                    withProduct=isWithProduct,
                    description=description, notes=note
                )
                #
                timerA = threading.Timer(5, self.connectObject().close)
                timerA.start()
    # CFX
    def _uploadAstCfxCmd(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        if prsMethods.Asset.isGroomStageName(assetStage):
            if self.isAstUploadCfx:
                isWithProduct = self._astWithProductButton.isChecked()
                isWithAssembly = self._astWithAssemblyButton.isChecked()
                isWithAnimation = self._astWithAnimationButton.isChecked()
                isWithAov = self._astWithAovButton.isChecked()
                #
                description = u'资产 - 毛发塑形 上传/更新'
                note = self._noteTexBrower.datum()
                #
                self.connectObject().hide()
                #
                maAstUploadCmds.astUnitCfxUploadMainCmd(
                    assetIndex,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage,
                    withProduct=isWithProduct, withAssembly=isWithAssembly,
                    withAov=isWithAov,
                    description=description, notes=note
                )
                #
                timerA = threading.Timer(5, self.connectObject().close)
                timerA.start()
    #
    def _uploadAstSolverCmd(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        #
        if prsMethods.Asset.isSolverStageName(assetStage):
            if self.isAstUploadRigSol:
                isWithProduct = self._astWithProductButton.isChecked()
                isWithAssembly = self._astWithAssemblyButton.isChecked()
                #
                description = u'资产 - 毛发绑定 上传/更新'
                note = self._noteTexBrower.datum()
                #
                self.connectObject().hide()
                #
                maAstUploadCmds.astUnitUploadMain(
                    assetIndex,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage,
                    withProduct=isWithProduct,
                    description=description, notes=note
                )
                #
                timerA = threading.Timer(5, self.connectObject().close)
                timerA.start()
    #
    def _uploadAstLightCmd(self):
        assetIndex = self.connectObject().assetIndex
        projectName = self.connectObject().projectName
        assetCategory = self.connectObject().assetCategory
        assetName = self.connectObject().assetName
        assetVariant = self.connectObject().assetVariant
        assetStage = self.connectObject().assetStage
        if prsMethods.Asset.isLightStageName(assetStage):
            if self.isAstUploadLight:
                isWithProduct = self._astWithProductButton.isChecked()
                isWithAssembly = self._astWithAssemblyButton.isChecked()
                #
                description = u'资产 _ 灯光 上传/更新'
                note = self._noteTexBrower.datum()
                #
                self.connectObject().hide()
                #
                maAstUploadCmds.astUnitUploadMain(
                    assetIndex,
                    projectName,
                    assetCategory, assetName, assetVariant, assetStage,
                    withProduct=isWithProduct,
                    description=description, notes=note
                )
                #
                timerA = threading.Timer(5, self.connectObject().close)
                timerA.start()
    #
    def _updateAstModelCmd(self):
        pass
    #
    def setupUnitWidgets(self):
        self._tabWidget = qtWidgets.QtButtonTabgroup()
        self.mainLayout().addWidget(self._tabWidget)
        self._tabWidget.setTabPosition(qtCore.South)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Upload', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupUploadTab(layout)
        #
        widget = qtCore.QWidget_()
        self._tabWidget.addTab(widget, 'Extend', 'svg_basic@svg#tab')
        layout = qtCore.QVBoxLayout_(widget)
        layout.setAlignment(qtCore.QtCore.Qt.AlignTop)
        self.setupExtendTab(layout)

