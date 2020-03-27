# coding:utf-8
from LxMaBasic import myaBscMtdCore


class NodeName(object):
    @classmethod
    def toExistList(cls, nodepathString):
        return myaBscMtdCore.Mtd_MaUtility._toAppExistStringList(nodepathString)
