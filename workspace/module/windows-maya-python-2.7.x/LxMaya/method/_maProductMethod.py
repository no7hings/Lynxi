# coding:utf-8
from LxPreset import prsCore, prsMethods

from LxCore.method.basic import _methodBasic

from LxCore.method import _productMethod

from LxMaya.method.basic import _maMethodBasic


#
class MaProductUnitMethod(_productMethod.LxProductUnitMethod):
    prd_method = _methodBasic.LxProductMethodBasic
    mtd_app_node = _maMethodBasic.MaNodeMethodBasic
    @classmethod
    def getProductUnitDatumLis(cls, moduleString):
        lis = []
        if moduleString in prsMethods.Product.moduleNames():
            searchKey = cls.mtd_app_node.lxNodeGroupName('*', prsMethods.Product.rootLabel())
            nodeLis = cls.mtd_app_node.getNodeLisBySearchKey(searchKey, cls.mtd_app_node.MaNodeType_Transform)
            if nodeLis:
                for nodePath in nodeLis:
                    if cls.mtd_app_node.isAppExist(nodePath):
                        nodeName = cls.mtd_app_node._toNodeName(nodePath)
                        if nodeName.startswith(prsMethods.Product.modulePrefixname(moduleString)):
                            unitDatum = []
                            for attrName in prsMethods.Product.attributeNames():
                                attrDatum = cls.mtd_app_node.getNodeAttrValue(nodePath, attrName)
                                unitDatum.append(attrDatum)
                            #
                            unitIndex, categoryString, unitName, unitVariant, unitStage = unitDatum
                            if categoryString in prsMethods.Product.moduleCategoryNames(moduleString):
                                lis.append(
                                    (unitIndex, categoryString, unitName, unitVariant, unitStage)
                                )
        return lis
    @classmethod
    def getProductUnitDatumDic(cls):
        dic = cls.mtd_app_node.orderedDict()
        for moduleString in prsMethods.Product.moduleNames():
            dic[moduleString] = cls.getProductUnitDatumLis(moduleString)
        return dic
    @classmethod
    def getAssetUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(prsMethods.Asset.moduleName())
    @classmethod
    def getSceneryUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(prsMethods.Scenery.moduleName())
    @classmethod
    def getSceneUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(prsMethods.Scene.moduleName())
