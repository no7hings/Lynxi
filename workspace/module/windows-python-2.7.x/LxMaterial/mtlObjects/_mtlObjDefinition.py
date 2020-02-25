# coding:utf-8
from LxMaterial import mtlObjCore


class TypeDef(mtlObjCore.Abc_MtlTypeDef):
    def __init__(self, datatypeString):
        pass


class GeometryDef(mtlObjCore.Abc_MtlGeometryDef):
    def __init__(self):
        self._initAbcMtlGeometryDef()


class NodeDef(mtlObjCore.Abc_MtlNodeDef):
    def __init__(self, categoryString):
        self._initAbcMtlNodeDef(categoryString)


class MaterialDef(mtlObjCore.Abc_MtlMaterialDef):
    def __init__(self):
        self._initAbcMtlMaterialDef()
