# coding:utf-8
from LxMaMaterial import maMtlObjCore


class NodeDef(maMtlObjCore.Abc_MaMtlMaterialDef):
    def __init__(self, categoryString):
        self._initAbcMaMtlMaterial(categoryString)
