# coding:utf-8
from LxCore.config import appConfig

from LxCore.method.basic import _methodBasic

from LxCore.method import _productMethod

from LxMaya.method.basic import _maMethodBasic


#
class MaProductUnitMethod(_productMethod.LxProductUnitMethod, appConfig.Cfg_Product):
    prd_method = _methodBasic.LxProductMethodBasic
    app_node_method = _maMethodBasic.MaNodeMethodBasic
    @classmethod
    def getProductUnitDatumLis(cls, productModule):
        lis = []
        if productModule in cls.prd_method.LynxiProduct_ModuleLis:
            searchKey = cls.app_node_method.lxNodeGroupName('*', cls.prd_method.LynxiUnit_Label_Root)
            nodeLis = cls.app_node_method.getNodeLisBySearchKey(searchKey, cls.app_node_method.MaNodeType_Transform)
            if nodeLis:
                for nodePath in nodeLis:
                    if cls.app_node_method.isAppExist(nodePath):

                        nodeName = cls.app_node_method._toNodeName(nodePath)
                        if nodeName.startswith(cls.prd_method.LynxiProduct_Module_PrefixDic[productModule]):
                            unitDatum = []
                            for attrName in cls.prd_method.LynxiProduct_Unit_AttrNameLis:
                                attrDatum = cls.app_node_method.getNodeAttrValue(nodePath, attrName)
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
        dic = cls.app_node_method.orderedDict()
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
