# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjCache, _mtlObjValue, _mtlObjRaw, _mtlObjSet


class ShadersetAssign(mtlObjCore.Abc_MtlShadersetAssign):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_set_geometry = _mtlObjSet.GeometrySet

    DEF_geometry_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_file_element_key = u'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlShadersetAssign(*args)


class PropertysetAssign(mtlObjCore.Abc_MtlPropertysetAssign):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_set_geometry = _mtlObjSet.GeometrySet

    VAR_mtl_file_element_key = u'propertysetAssign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlPropertysetAssign(*args)


class VisibilityAssign(mtlObjCore.Abc_MtlVisibilityAssign):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_type = _mtlObjRaw.VistypeString
    CLS_set_geometry = _mtlObjSet.GeometrySet
    CLS_set_geometry_viewer = _mtlObjSet.ViewerGeometrySet

    CLS_value_visibility = _mtlObjValue.Val_Visibility

    OBJ_mtl_def_cache = _mtlObjCache.OBJ_mtl_def_cache

    VAR_mtl_file_element_key = u'visibility'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlVisibilityAssign(*args)
