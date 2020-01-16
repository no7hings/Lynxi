# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjElement


class ShadersetAssign(mtlAbstract.Abc_ShadersetAssign):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    CLS_shaderset = _mtlObjElement.ShadersetElement

    separator_geometry = mtlConfigure.Separator_Raw_Basic

    STR_mtlx_key_element = 'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcShadersetAssign(*args)


class GeomPortsetAssign(mtlAbstract.Abc_GeomPortsetAssign):
    CLS_raw_name = _mtlObjRaw.Raw_Name
    CLS_set_geometry = _mtlObjSet.Set_Geometry

    STR_mtlx_key_element = 'propertyset'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcGeomPortsetAssign(*args)
