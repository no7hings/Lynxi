# coding:utf-8
from LxMaterial import mtlMtdCore


class File(mtlMtdCore.Mtd_MtlFile):
    @classmethod
    def objectDef(cls, fileString):
        return cls._getNodeDefDict(fileString)
