# coding:utf-8
from .. import maBscMtdCore


class ObjName(object):
    @classmethod
    def toExistList(cls, nodepathString):
        return maBscMtdCore.Mtd_MaUtility._toAppExistStringList(nodepathString)
