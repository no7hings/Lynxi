# coding:utf-8
from LxMaBasic import maBscMtdCore


class Node(maBscMtdCore.Mtd_MaBasic):
    @classmethod
    def isExist(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._isAppExist(nodeString)

    @classmethod
    def category(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodeCategoryString(nodeString)

    @classmethod
    def fullpathPortnames(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodeAttributeFullpathPortnameList(nodeString)

    @classmethod
    def inputFullpathPortname(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodeInputFullpathPortnameList(nodeString)

    @classmethod
    def outputFullpathPortname(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodeOutputFullpathPortnameList(nodeString)

    @classmethod
    def isDag(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._isNodeDag(nodeString)

    @classmethod
    def toFullpathName(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodeFullpathNameString(nodeString)

    @classmethod
    def transformName(cls, nodeString, fullpath=False):
        return maBscMtdCore.Mtd_MaNode._getNodeTransformNodeString(nodeString, fullpath)

    @classmethod
    def shapeName(cls, nodeString, fullpath=False):
        return maBscMtdCore.Mtd_MaNode._getNodeShapeNodeString(nodeString, fullpath)
