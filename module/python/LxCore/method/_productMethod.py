# coding:utf-8
#
from LxCore.method import _dbMethod
from LxCore.method.basic import _methodBasic


#
class LxProductUnitMethod(_methodBasic.LxProductMethodBasic, _dbMethod.LxDbProductUnitMethod):
    @classmethod
    def getProductUnitViewName(cls, productModule, productUnitId):
        return cls.dbGetProductUnitName(productModule, productUnitId)
    @classmethod
    def getProductUnitViewInfo(cls, productModule, productUnitId):
        viewName = cls.getProductUnitViewName(productModule, productUnitId)
