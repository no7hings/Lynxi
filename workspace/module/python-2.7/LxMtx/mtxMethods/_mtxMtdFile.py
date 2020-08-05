# coding:utf-8
from .. import mtxMtdCore


class File(mtxMtdCore.Mtd_MtxFile):
    @classmethod
    def objectDef(cls, fileString):
        return cls._getNodeDefDict(fileString)
