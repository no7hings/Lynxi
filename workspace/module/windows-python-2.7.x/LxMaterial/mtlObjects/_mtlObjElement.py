# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet

from ..import mtlObjAbs

from ..mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjNode, _mtlObjAssign


class Look(mtlObjAbs.Abc_MtlLook):
    CLS_mtl_name = _mtlObjRaw.Name
    CLS_mtl_assign_set = _grhObjSet.ObjSet

    CLS_mtl_visibility = _mtlObjAssign.VisibilityAssign
    CLS_mtl_visibility_set = _grhObjSet.ObjSet

    CLS_mtl_material_assign = _mtlObjAssign.MaterialAssign
    CLS_mtl_material_assign_set = _grhObjSet.ObjSet

    CLS_mtl_propertyset_assign = _mtlObjAssign.PropertysetAssign
    CLS_mtl_propertyset_assign_set = _grhObjSet.ObjSet

    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet

    VAR_mtl_file_element_key = u'look'
    VAR_mtl_file_attribute_attach_key = u'look'

    def __init__(self, *args):
        self._initAbcMtlLook(*args)


class Collection(mtlObjAbs.Abc_MtlCollection):
    CLS_mtl_name = _mtlObjRaw.Name

    CLS_mtl_geometry_set = _grhObjSet.ObjSet
    CLS_mtl_collection_set = _grhObjSet.ObjSet

    DEF_geometry_separator = u','

    VAR_mtl_file_element_key = u'collection'
    VAR_mtl_file_attribute_attach_key = u'collection'

    def __init__(self, *args):
        self._initAbcMtlCollection(*args)
