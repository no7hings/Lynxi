# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjDefinition, _mtlObjValue, _mtlObjRaw, _mtlObjSet, _mtlObjAttribute


class ShadersetAssign(mtlObjCore.Abc_MtlShadersetAssign):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    DEF_geometry_separator = mtlConfigure.Utility.DEF_mtl_data_separator

    VAR_mtl_file_element_key = 'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlShadersetAssign(*args)


class PropertysetAssign(mtlObjCore.Abc_MtlPropertysetAssign):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    VAR_mtl_file_element_key = 'propertysetAssign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlPropertysetAssign(*args)


class VisibilityAssign(mtlObjCore.Abc_MtlVisibilityAssign):
    CLS_mtl_name = _mtlObjRaw.NameString
    CLS_mtl_type = _mtlObjRaw.VistypeString
    CLS_set_geometry = _mtlObjSet.Set_Geometry
    CLS_set_geometry_viewer = _mtlObjSet.Set_ViewerGeometry

    CLS_value_visibility = _mtlObjValue.Val_Visibility
    CLS_mtl_object_def = _mtlObjDefinition.GeometryDef

    VAR_mtl_file_element_key = 'visibility'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlVisibilityAssign(*args)
