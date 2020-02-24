# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjDefinition, _mtlObjValue, _mtlObjRaw, _mtlObjSet, _mtlObjPort


class ShadersetAssign(mtlObjCore.Abc_MtlShadersetAssign):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    DEF_geometry_separator = mtlConfigure.Separator_Raw_Basic

    VAR_mtlx_key_element = 'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlShadersetAssign(*args)


class PropertysetAssign(mtlObjCore.Abc_MtlPropertysetAssign):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    VAR_mtlx_key_element = 'propertysetAssign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlPropertysetAssign(*args)


class VisibilityAssign(mtlObjCore.Abc_MtlVisibilityAssign):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_raw_type = _mtlObjRaw.Raw_VisibilityType
    CLS_set_geometry = _mtlObjSet.Set_Geometry
    CLS_set_geometry_viewer = _mtlObjSet.Set_ViewerGeometry

    CLS_value_visibility = _mtlObjValue.Val_Visibility
    CLS_def_geometry = _mtlObjDefinition.GeometryDefinition

    VAR_mtlx_key_element = 'visibility'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlVisibilityAssign(*args)
