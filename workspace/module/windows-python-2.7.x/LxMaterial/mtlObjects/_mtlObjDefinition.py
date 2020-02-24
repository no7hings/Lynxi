# coding:utf-8
from LxMaterial import mtlObjCore


class Definition(mtlObjCore.Abc_MtlDef):
    def __init__(self):
        self._initAbcMtlDef()


class Def_Type(mtlObjCore.Abc_MtlTypeDef):
    def __init__(self, typeString):
        pass


class GeometryDefinition(mtlObjCore.Abc_MtlGeometryDef):
    def __init__(self):
        self._initAbcMtlGeometryDef()


class Def_Node(mtlObjCore.Abc_MtlNodeDef):
    def __init__(self, categoryString):
        self._initAbcMtlNodeDef(categoryString)
