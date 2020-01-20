# coding:utf-8
from LxPreset import prsConfigure

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
        if moduleString in prsConfigure.Product.LynxiProduct_ModuleLis:
            searchKey = cls.mtd_app_node.lxNodeGroupName('*', prsConfigure.Product.LynxiUnit_Label_Root)
            nodeLis = cls.mtd_app_node.getNodeLisBySearchKey(searchKey, cls.mtd_app_node.MaNodeType_Transform)
            if nodeLis:
                for nodePath in nodeLis:
                    if cls.mtd_app_node.isAppExist(nodePath):
                        nodeName = cls.mtd_app_node._toNodeName(nodePath)
                        if nodeName.startswith(prsConfigure.Product.modulePrefixname(moduleString)):
                            unitDatum = []
                            for attrName in prsConfigure.Product.LynxiProduct_Unit_AttrNameLis:
                                attrDatum = cls.mtd_app_node.getNodeAttrValue(nodePath, attrName)
                                unitDatum.append(attrDatum)
                            #
                            unitIndex, unitClass, unitName, unitVariant, unitStage = unitDatum
                            if unitClass in prsConfigure.Product.moduleClassnames(moduleString):
                                lis.append(
                                    (unitIndex, unitClass, unitName, unitVariant, unitStage)
                                )
        return lis
    @classmethod
    def getProductUnitDatumDic(cls):
        dic = cls.mtd_app_node.orderedDict()
        for moduleString in prsConfigure.Product.LynxiProduct_ModuleLis:
            dic[moduleString] = cls.getProductUnitDatumLis(moduleString)
        return dic
    @classmethod
    def getAssetUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(prsConfigure.Asset.name())
    @classmethod
    def getSceneryUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(prsConfigure.Scenery.name())
    @classmethod
    def getSceneUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(prsConfigure.Scene.name())
