# coding:utf-8
from LxMaterial import mtlAbstract


class Def_Node(mtlAbstract.Abc_DagDef):
    def __init__(self, categoryString):
        self._initAbcDagDef(categoryString)
