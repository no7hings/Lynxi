# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjAttribute, _mtlObjObject, _mtlObjCache


class Reference(mtlObjCore.Abc_MtlFileReference):
    CLS_mtl_file = _mtlObjRaw.ReferenceFile

    VAR_mtl_file_element_key = u'xi:include'

    def __init__(self, *args):
        self._initAbcMtlFileReference(*args)


class Look(mtlObjCore.Abc_MtlLook):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_set_assign = _mtlObjSet.AssignSet

    CLS_set_assign_shaderset = _mtlObjSet.AssignSet
    ClS_set_assign_propertyset = _mtlObjSet.AssignSet
    CLS_mtl_visibility_set = _mtlObjSet.VisibilitySet

    VAR_mtl_file_element_key = u'look'
    VAR_mtl_file_attribute_key = u'look'

    def __init__(self, *args):
        self._initAbcMtlLook(*args)


class GeometryPropertyset(mtlObjCore.Abc_MtlPropertyset):
    CLS_mtl_name = _mtlObjRaw.NameString

    CLS_mtl_port_set = _mtlObjSet.PortSet
    
    VAR_mtl_file_element_key = u'propertyset'
    VAR_mtl_file_attribute_key = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry dagpath)
        """
        self._initAbcMtlPropertyset(*args)


class Collection(mtlObjCore.Abc_MtlGeometryCollection):
    CLS_mtl_name = _mtlObjRaw.NameString

    CLS_set_geometry = _mtlObjSet.GeometrySet
    CLS_set_collection = _mtlObjSet.Set_Collection

    DEF_geometry_separator = u','

    VAR_mtl_file_element_key = u'collection'
    VAR_mtl_file_attribute_key = u'collection'

    def __init__(self, *args):
        self._initAbcMtlGeometryCollection(*args)
