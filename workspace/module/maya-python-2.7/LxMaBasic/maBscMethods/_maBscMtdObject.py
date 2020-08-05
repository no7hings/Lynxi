# coding:utf-8
from .. import maBscMtdCore


class Node(maBscMtdCore.Mtd_MaBasic):
    @classmethod
    def isExist(cls, nodepathString):
        return maBscMtdCore.Mtd_MaObject._isAppExist(nodepathString)

    @classmethod
    def category(cls, nodepathString):
        return maBscMtdCore.Mtd_MaObject._getNodeCategoryString(nodepathString)

    @classmethod
    def isDag(cls, nodepathString):
        return maBscMtdCore.Mtd_MaObject._isNodeDag(nodepathString)

    @classmethod
    def toFullpathName(cls, nodepathString):
        return maBscMtdCore.Mtd_MaObject._dcc_getNodFullpathNodepathStr(nodepathString)

    @classmethod
    def transformName(cls, nodepathString, fullpath=False):
        return maBscMtdCore.Mtd_MaObject._dcc_getNodTransformNodepathStr(nodepathString, fullpath)

    @classmethod
    def shapeName(cls, nodepathString, fullpath=False):
        return maBscMtdCore.Mtd_MaObject._dcc_getNodShapeNodepathStr(nodepathString, fullpath)
