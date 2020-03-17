# coding:utf-8
from LxMaterial import mtlObjCore


class AssignSet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class ObjectSet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class GeometrySet(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_key = u'geom'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class MaterialSet(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_key = u'material'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class ViewerGeometrySet(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_key = u'viewergeom'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class CollectionSet(mtlObjCore.Abc_MtlObjectSet):
    VAR_mtl_file_attribute_key = u'collection'

    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class PortSet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class OutputSet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class PropertySet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class VisibilitySet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class ReferenceSet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class LookSet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)


class NodeGraphSet(mtlObjCore.Abc_MtlObjectSet):
    def __init__(self, *args):
        self._initAbcMtlObjectSet(*args)
