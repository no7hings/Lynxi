# coding:utf-8
from LxMaterial import mtlAbstract


class Definition(mtlAbstract.Abc_Def):
    def __init__(self):
        self._initAbcDef()


class Def_Type(mtlAbstract.Abc_TypeDef):
    def __init__(self, typeString):
        pass


class Def_Node(mtlAbstract.Abc_DagDef):
    def __init__(self, categoryString):
        self._initAbcDagDef(categoryString)
