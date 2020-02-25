# coding:utf-8
from LxMaterial import mtlObjCore


class Set_Assign(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Dag(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Geometry(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_key = u'geom'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_ViewerGeometry(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_key = u'viewergeom'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Collection(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_key = u'collection'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class Set_Attribute(mtlObjCore.Abc_MtlObjectSet):
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
