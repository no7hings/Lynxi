# coding:utf-8
from LxMaBasic import maBscMtdCore


class Node(maBscMtdCore.Mtd_MaBasic):
    @classmethod
    def isExist(cls, nodeString):
        return maBscMtdCore.Mtd_MaObject._isAppExist(nodeString)

    @classmethod
    def category(cls, nodeString):
        return maBscMtdCore.Mtd_MaObject._getNodeCategoryString(nodeString)

    @classmethod
    def isDag(cls, nodeString):
        return maBscMtdCore.Mtd_MaObject._isNodeDag(nodeString)

    @classmethod
    def toFullpathName(cls, nodeString):
        return maBscMtdCore.Mtd_MaObject._getNodeFullpathNameString(nodeString)

    @classmethod
    def transformName(cls, nodeString, fullpath=False):
        return maBscMtdCore.Mtd_MaObject._getNodeTransformNodeString(nodeString, fullpath)

    @classmethod
    def shapeName(cls, nodeString, fullpath=False):
        return maBscMtdCore.Mtd_MaObject._getNodeShapeNodeString(nodeString, fullpath)
