# coding:utf-8
from .. import myaBscMtdCore


class Node(myaBscMtdCore.Mtd_MaBasic):
    @classmethod
    def isExist(cls, nodepathString):
        return myaBscMtdCore.Mtd_MaObject._isAppExist(nodepathString)

    @classmethod
    def category(cls, nodepathString):
        return myaBscMtdCore.Mtd_MaObject._getNodeCategoryString(nodepathString)

    @classmethod
    def isDag(cls, nodepathString):
        return myaBscMtdCore.Mtd_MaObject._isNodeDag(nodepathString)

    @classmethod
    def toFullpathName(cls, nodepathString):
        return myaBscMtdCore.Mtd_MaObject._getNodeFullpathNameString(nodepathString)

    @classmethod
    def transformName(cls, nodepathString, fullpath=False):
        return myaBscMtdCore.Mtd_MaObject._getNodeTransformNodeString(nodepathString, fullpath)

    @classmethod
    def shapeName(cls, nodepathString, fullpath=False):
        return myaBscMtdCore.Mtd_MaObject._getNodeShapeNodeString(nodepathString, fullpath)
