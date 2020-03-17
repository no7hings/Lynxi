# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjCache, _mtlObjValue, _mtlObjRaw, _mtlObjSet, _mtlObjPort


class MaterialAssign(mtlObjCore.Abc_MtlMaterialAssign):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet

    DEF_geometry_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_file_element_key = u'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlMaterialAssign(*args)


class PropertysetAssign(mtlObjCore.Abc_MtlPropertysetAssign):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet

    CLS_mtl_propertyset = _mtlObjPort.Propertyset

    VAR_mtl_file_element_key = u'propertysetAssign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlPropertysetAssign(*args)


class Visibility(mtlObjCore.Abc_MtlVisibility):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_type = _mtlObjRaw.VistypeString
    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet
    CLS_set_geometry_viewer = _mtlObjSet.ViewerGeometrySet

    CLS_value_visibility = _mtlObjValue.Val_Visibility

    OBJ_mtl_query_cache = _mtlObjCache.OBJ_mtl_query_cache

    VAR_mtl_file_element_key = u'visibility'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlVisibility(*args)
