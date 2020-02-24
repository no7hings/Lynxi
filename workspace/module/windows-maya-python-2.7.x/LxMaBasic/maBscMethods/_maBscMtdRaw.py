# coding:utf-8
from LxMaBasic import maBscMtdCore


class NodeName(object):
    @classmethod
    def toExistList(cls, nodeString):
        return maBscMtdCore.Mtd_MaUtility._toAppExistStringList(nodeString)
