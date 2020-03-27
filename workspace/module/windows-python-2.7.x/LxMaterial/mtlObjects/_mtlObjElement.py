# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjObject, _mtlObjAssign


class Look(mtlObjCore.Abc_MtlLook):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_assign_set = _mtlObjSet.AssignSet

    CLS_mtl_visibility = _mtlObjAssign.VisibilityAssign
    CLS_mtl_visibility_set = _mtlObjSet.VisibilitySet

    CLS_mtl_material_assign = _mtlObjAssign.MaterialAssign
    CLS_mtl_material_assign_set = _mtlObjSet.AssignSet

    CLS_mtl_propertyset_assign = _mtlObjAssign.PropertysetAssign
    CLS_mtl_propertyset_assign_set = _mtlObjSet.AssignSet

    CLS_mtl_geometry = _mtlObjObject.Geometry
    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet

    VAR_mtl_file_element_key = u'look'
    VAR_mtl_file_attribute_attach_key = u'look'

    def __init__(self, *args):
        self._initAbcMtlLook(*args)


class Collection(mtlObjCore.Abc_MtlCollection):
    CLS_mtl_name = _mtlObjRaw.NameString

    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet
    CLS_set_collection = _mtlObjSet.CollectionSet

    DEF_geometry_separator = u','

    VAR_mtl_file_element_key = u'collection'
    VAR_mtl_file_attribute_attach_key = u'collection'

    def __init__(self, *args):
        self._initAbcMtlCollection(*args)
