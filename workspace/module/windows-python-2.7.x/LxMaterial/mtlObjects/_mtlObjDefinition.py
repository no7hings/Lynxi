# coding:utf-8
from LxMaterial import mtlObjAbstract


class Definition(mtlObjAbstract.Abc_Def):
    def __init__(self):
        self._initAbcDef()


class Def_Type(mtlObjAbstract.Abc_TypeDef):
    def __init__(self, typeString):
        pass


class GeometryDefinition(mtlObjAbstract.Abc_GeometryDef):
    def __init__(self):
        self._initAbcGeometryDef()


class Def_Node(mtlObjAbstract.Abc_DagDef):
    def __init__(self, categoryString):
        self._initAbcDagDef(categoryString)
