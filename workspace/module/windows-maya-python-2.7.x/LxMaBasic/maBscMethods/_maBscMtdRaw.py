# coding:utf-8
from ..import myaBscMtdCore


class Nodename(object):
    @classmethod
    def toExistList(cls, nodepathString):
        return myaBscMtdCore.Mtd_MaUtility._toAppExistStringList(nodepathString)
