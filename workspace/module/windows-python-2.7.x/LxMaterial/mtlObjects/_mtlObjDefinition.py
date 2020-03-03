# coding:utf-8
from LxMaterial import mtlObjCore


class MtlTypeDef(mtlObjCore.Abc_MtlTypeDef):
    def __init__(self):
        pass


class MtlGeometryDef(mtlObjCore.Abc_MtlGeometryDef):
    def __init__(self):
        self._initAbcMtlGeometryDef()


class MtlNodeDef(mtlObjCore.Abc_MtlNodeDef):
    def __init__(self, categoryString):
        self._initAbcMtlNodeDef(categoryString)


class MtlMaterialDef(mtlObjCore.Abc_MtlMaterialDef):
    def __init__(self):
        self._initAbcMtlMaterialDef()
