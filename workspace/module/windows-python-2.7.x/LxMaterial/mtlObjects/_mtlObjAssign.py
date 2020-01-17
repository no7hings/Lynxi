# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjElement


class ShadersetAssign(mtlAbstract.Abc_ShadersetAssign):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    STR_geometry_separator = mtlConfigure.Separator_Raw_Basic

    STR_mtlx_key_element = 'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcShadersetAssign(*args)


class PropertysetAssign(mtlAbstract.Abc_PropertysetAssign):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    STR_mtlx_key_element = 'propertysetAssign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initPropertysetAssign(*args)


class VisibilityAssign(mtlAbstract.Abc_VisibilityAssign):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    STR_mtlx_key_element = 'visibility'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcVisibilityAssign(*args)
