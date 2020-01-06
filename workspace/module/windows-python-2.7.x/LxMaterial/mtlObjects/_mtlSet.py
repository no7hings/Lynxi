# coding:utf-8
from LxMaterial import mtlAbstract


class Set_Assign(mtlAbstract.Abc_ObjectSet):
    def __init__(self, *args):
        self._initAbcObjectSet(*args)


class Set_Dag(mtlAbstract.Abc_ObjectSet):
    def __init__(self, *args):
        self._initAbcObjectSet(*args)


class Set_Attribute(mtlAbstract.Abc_ObjectSet):
    def __init__(self, *args):
        self._initAbcObjectSet(*args)
