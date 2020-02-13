# coding:utf-8
from LxDatabase import dtbMethods

from LxInterface.qt.qtIfBasic import _qtIfAbcWidget
#
from LxMaya.method import _maProductMethod
#
from LxMaya.interface.ifWidgets import ifMaSceneUnit, ifMaSceneToolUnit


#
class IfScLightRigGroup(_qtIfAbcWidget.QtIfAbc_Group):
    app_prd_unt_method = _maProductMethod.MaProductUnitMethod

    def __init__(self, mainWindow=None):
        super(IfScLightRigGroup, self).__init__(mainWindow)
        self._initIfAbcGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def setupGroup(self):
        self._productUnitTab = self.chooseTab()
        #
        extendDatumDic = {}
        productUnitDatumDic = self.getProductUnitDatumDic()
        if productUnitDatumDic:
            for k, v in productUnitDatumDic.items():
                productModuleString = k
                for i in v:
                    unitId, unitClass, unitName, unitVariant, unitStage = i

                    unitViewName = dtbMethods.DtbProductUnit.getProductUnitViewName(productModuleString, unitId)
                    extendDatumDic[unitId] = unitName, unitViewName
        #
        self._productUnitTab.setExtendDatumDic(extendDatumDic)
        #
        unit = ifMaSceneUnit.IfScLightLinkUpdateUnit()
        self.addTab(
            unit, 'Light Rig', 'svg_basic@svg#lightLink', u'Light Rig Unit'
        )
        unit.setConnectObject(self)
        unit.refreshMethod()


#
class IfScComposeGroup(_qtIfAbcWidget.QtIfAbc_Group):
    app_prd_unt_method = _maProductMethod.MaProductUnitMethod

    def __init__(self, mainWindow=None):
        super(IfScComposeGroup, self).__init__(mainWindow)
        self._initIfAbcGroup()
        self._mainWindow = mainWindow
        #
        self.setupGroup()
    #
    def setupGroup(self):
        self._productUnitTab = self.chooseTab()
        #
        extendDatumDic = {}
        productUnitDatumDic = self.getProductUnitDatumDic()
        if productUnitDatumDic:
            for k, v in productUnitDatumDic.items():
                productModuleString = k
                for i in v:
                    unitId, unitClass, unitName, unitVariant, unitStage = i
                    unitViewName = self.getProductUnitViewName(productModuleString, unitId)
                    extendDatumDic[unitId] = unitName, unitViewName
        #
        self._productUnitTab.setExtendDatumDic(extendDatumDic)
        #
        unit = ifMaSceneToolUnit.IfScMayaComposeToolUnit()
        self.addTab(
            unit, 'Light Rig', 'svg_basic@svg#lightLink', u'Light Rig Unit'
        )
        unit.setConnectObject(self)
        unit.refreshMethod()
