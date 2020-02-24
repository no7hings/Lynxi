# coding:utf-8
from LxMaterial import mtlObjCore


class Set_Assign(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Dag(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Geometry(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtlx_key_attribute = u'geom'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_ViewerGeometry(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtlx_key_attribute = u'viewergeom'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Collection(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtlx_key_attribute = u'collection'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Port(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Input(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Output(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Property(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Visibility(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Reference(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Look(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)
