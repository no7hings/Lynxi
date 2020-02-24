# coding:utf-8
from LxMaterial import mtlMtdCore

from LxMaMaterial import maMtlMtdCore


class NodeDagPath(maMtlMtdCore.Mtd_MaMtlBasic):
    @classmethod
    def covertTo(cls, string):
        return mtlMtdCore.Mtd_MtlRaw._setMayaDagPathCovert(string)


class NodeCategory(maMtlMtdCore.Mtd_MaMtlBasic):
    @classmethod
    def covertTo(cls, string):
        return mtlMtdCore.Mtd_MtlRaw._setMayaCategoryCovert(string, cls.DEF_category_node_covert_dict)


class NodeAttribute(maMtlMtdCore.Mtd_MaMtlBasic):
    @classmethod
    def covertTo(cls, string):
        return mtlMtdCore.Mtd_MtlRaw._setMayaAttributeCovert(string)
