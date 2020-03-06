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
    def portStrings(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodePortStringList(nodeString)

    @classmethod
    def inputPortStrings(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodeInputPortStringList(nodeString)

    @classmethod
    def outputPortStrings(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodeOutputPortStringList(nodeString)

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

    @classmethod
    def portDict(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodePortDict_(
            nodeString,
            cls.portStrings(nodeString)
        )

    @classmethod
    def portIndexesDict(cls, nodeString):
        return maBscMtdCore.Mtd_MaNode._getNodePortIndexesDict_(
            nodeString,
            cls.portStrings(nodeString)
        )

    @classmethod
    def _getPortDict_(cls, nodeString, portStringList):
        return maBscMtdCore.Mtd_MaNode._getNodePortDict_(
            nodeString,
            portStringList
        )
