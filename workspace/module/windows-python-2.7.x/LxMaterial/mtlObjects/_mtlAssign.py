# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlSet, _mtlElement


class Asn_Shaderset(mtlAbstract.Abc_MaterialAssign):
    RAW_NAME_CLS = _mtlRaw.Raw_Name
    SET_GEOMETRY_CLS = _mtlSet.Set_Dag

    MATERIAL_CLS = _mtlElement.Elt_Material

    separator_geometry = mtlConfigure.Separator_Raw_Basic

    xml_prefix_label = 'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMaterialAssign(*args)


class Asn_Portset(mtlAbstract.Abc_PortsetAssign):
    RAW_NAME_CLS = _mtlRaw.Raw_Name
    SET_GEOMETRY_CLS = _mtlSet.Set_Dag

    xml_prefix_label = 'propertyset'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcPortsetAssign(*args)
