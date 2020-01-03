# coding:utf-8
from LxCore.config import appConfig

from LxCore.method import _dbMethod

from LxCore.method.basic import _methodBasic


#
class LxProductUnitMethod(appConfig.LxDbConfig):
    prd_method = _methodBasic.LxProductMethodBasic
    dtb_prd_method = _dbMethod.Mtd_DbProdUnit
    @classmethod
    def getProductUnitViewName(cls, productModule, productUnitId):
        return cls.dtb_prd_method.dbGetProductUnitName(productModule, productUnitId)
    @classmethod
    def getProductUnitViewInfo(cls, productModule, productUnitId):
        pass
