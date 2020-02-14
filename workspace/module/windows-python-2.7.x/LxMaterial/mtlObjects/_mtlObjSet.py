# coding:utf-8
from LxMaterial import mtlObjAbstract


class Set_Assign(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Dag(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Geometry(mtlObjAbstract.Abc_Set):
    DEF_mtlx_key_attribute = u'geom'

    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_ViewerGeometry(mtlObjAbstract.Abc_Set):
    DEF_mtlx_key_attribute = u'viewergeom'

    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Collection(mtlObjAbstract.Abc_Set):
    DEF_mtlx_key_attribute = u'collection'

    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Port(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Input(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Output(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Property(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Visibility(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Reference(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Look(mtlObjAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)
