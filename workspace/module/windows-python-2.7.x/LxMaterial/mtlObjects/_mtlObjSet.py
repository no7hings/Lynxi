# coding:utf-8
from LxMaterial import mtlAbstract


class Set_Assign(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Dag(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Geometry(mtlAbstract.Abc_Set):
    STR_mtlx_key_attribute = u'geom'

    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_ViewerGeometry(mtlAbstract.Abc_Set):
    STR_mtlx_key_attribute = u'viewergeom'

    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Collection(mtlAbstract.Abc_Set):
    STR_mtlx_key_attribute = u'collection'

    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Port(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Input(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Output(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Property(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Visibility(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Reference(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)


class Set_Look(mtlAbstract.Abc_Set):
    def __init__(self, *args):
        self._initAbcSet(*args)
