# coding:utf-8
from .. import mtlObjAbs


class AssignSet(mtlObjAbs.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class GeometrySet(mtlObjAbs.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_attach_key = u'geom'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class MaterialSet(mtlObjAbs.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_attach_key = u'material'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class ViewerGeometrySet(mtlObjAbs.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_attach_key = u'viewergeom'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class CollectionSet(mtlObjAbs.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_attach_key = u'collection'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class ReferenceSet(mtlObjAbs.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class LookSet(mtlObjAbs.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)
