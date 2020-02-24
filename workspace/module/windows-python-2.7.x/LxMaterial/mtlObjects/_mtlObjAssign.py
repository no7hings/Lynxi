# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjDefinition, _mtlObjValue, _mtlObjRaw, _mtlObjSet, _mtlObjPort


class ShadersetAssign(mtlObjCore.Abc_MtlShadersetAssign):
    CLS_mtl_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    DEF_geometry_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_key_element = 'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlShadersetAssign(*args)


class PropertysetAssign(mtlObjCore.Abc_MtlPropertysetAssign):
    CLS_mtl_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    VAR_mtl_key_element = 'propertysetAssign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlPropertysetAssign(*args)


class VisibilityAssign(mtlObjCore.Abc_MtlVisibilityAssign):
    CLS_mtl_name = _mtlObjRaw.Raw_Name
    CLS_mtl_type = _mtlObjRaw.Raw_VisibilityType
    CLS_set_geometry = _mtlObjSet.Set_Geometry
    CLS_set_geometry_viewer = _mtlObjSet.Set_ViewerGeometry

    CLS_value_visibility = _mtlObjValue.Val_Visibility
    CLS_mtl_geometry_def = _mtlObjDefinition.GeometryDef

    VAR_mtl_key_element = 'visibility'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlVisibilityAssign(*args)
