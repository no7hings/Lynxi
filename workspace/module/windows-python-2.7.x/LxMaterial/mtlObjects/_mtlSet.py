# coding:utf-8
from LxMaterial import mtlAbstract


class Set_Assign(mtlAbstract.Abc_ObjectSet):
    def __init__(self, *args):
        self._initAbcObjectSet(*args)


class Set_Dag(mtlAbstract.Abc_ObjectSet):
    def __init__(self, *args):
        self._initAbcObjectSet(*args)


class Set_Geometry(mtlAbstract.Abc_ObjectSet):
    xml_key_attribute = 'geom'

    def __init__(self, *args):
        self._initAbcObjectSet(*args)


class Set_Port(mtlAbstract.Abc_ObjectSet):
    def __init__(self, *args):
        self._initAbcObjectSet(*args)
