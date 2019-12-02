# coding:utf-8
from LxCore.method import _productMethod
#
from LxMaya.method.basic import _maMethodBasic


#
class MaProductUnitMethod(_productMethod.LxProductUnitMethod, _maMethodBasic.MaNodeMethodBasic):
    @classmethod
    def getProductUnitDatumLis(cls, productModule):
        lis = []
        if productModule in cls.LynxiProduct_ModuleLis:
            searchKey = cls.lxNodeGroupName('*', cls.LynxiUnit_Label_Root)
            nodeLis = cls.getNodeLisBySearchKey(searchKey, cls.MaNodeType_Transform)
            if nodeLis:
                for nodePath in nodeLis:
                    if cls.isAppExist(nodePath):
                        nodeName = cls._toNodeName(nodePath)
                        if nodeName.startswith(cls.LynxiProduct_Module_PrefixDic[productModule]):
                            unitDatum = []
                            for attrName in cls.LynxiProduct_Unit_AttrNameLis:
                                attrDatum = cls.getNodeAttrValue(nodePath, attrName)
                                unitDatum.append(attrDatum)
                            #
                            unitIndex, unitClass, unitName, unitVariant, unitStage = unitDatum
                            if unitClass in cls.LynxiProduct_Module_Class_Dic[productModule]:
                                lis.append(
                                    (unitIndex, unitClass, unitName, unitVariant, unitStage)
                                )
        return lis
    @classmethod
    def getProductUnitDatumDic(cls):
        dic = cls.orderedDict()
        for productModule in cls.LynxiProduct_ModuleLis:
            dic[productModule] = cls.getProductUnitDatumLis(productModule)
        return dic
    @classmethod
    def getAssetUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(cls.LynxiProduct_Module_Asset)
    @classmethod
    def getSceneryUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(cls.LynxiProduct_Module_Scenery)
    @classmethod
    def getSceneUnitDatumLis(cls):
        return cls.getProductUnitDatumLis(cls.LynxiProduct_Module_Scene)
