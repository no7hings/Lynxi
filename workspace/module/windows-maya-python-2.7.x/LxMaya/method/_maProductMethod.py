# coding:utf-8
from LxCore.config import appConfig

from LxCore.method.basic import _methodBasic

from LxCore.method import _productMethod

from LxMaya.method.basic import _maMethodBasic


#
class MaProductUnitMethod(_productMethod.LxProductUnitMethod, appConfig.Cfg_Product):
    prd_method = _methodBasic.LxProductMethodBasic
    mtd_app_node = _maMethodBasic.MaNodeMethodBasic
    @classmethod
    def getProductUnitDatumLis(cls, productModule):
        lis = []
        if productModule in cls.prd_method.LynxiProduct_ModuleLis:
            searchKey = cls.mtd_app_node.lxNodeGroupName('*', cls.prd_method.LynxiUnit_Label_Root)
            nodeLis = cls.mtd_app_node.getNodeLisBySearchKey(searchKey, cls.mtd_app_node.MaNodeType_Transform)
            if nodeLis:
                for nodePath in nodeLis:
                    if cls.mtd_app_node.isAppExist(nodePath):

                        nodeName = cls.mtd_app_node._toNodeName(nodePath)
                        if nodeName.startswith(cls.prd_method.LynxiProduct_Module_PrefixDic[productModule]):
                            unitDatum = []
                            for attrName in cls.prd_method.LynxiProduct_Unit_AttrNameLis:
                                attrDatum = cls.mtd_app_node.getNodeAttrValue(nodePath, attrName)
                                unitDatum.append(attrDatum)
                            #
                            unitIndex, unitClass, unitName, unitVariant, unitStage = unitDatum
                            if unitClass in cls.prd_method.LynxiProduct_Module_Class_Dic[productModule]:
                                lis.append(
                                    (unitIndex, unitClass, unitName, unitVariant, unitStage)
                                )
        return lis
    @classmethod
    def getProductUnitDatumDic(cls):
        dic = cls.mtd_app_node.orderedDict()
        for productModule in cls.prd_method.LynxiProduct_ModuleLis:
            dic[productModule] = cls.getProductUnitDatumLis(productModule)
        return dic
    @classmethod
    def getAssetUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(cls.prd_method.LynxiProduct_Module_Asset)
    @classmethod
    def getSceneryUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(cls.prd_method.LynxiProduct_Module_Scenery)
    @classmethod
    def getSceneUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(cls.prd_method.LynxiProduct_Module_Scene)
