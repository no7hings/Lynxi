# coding:utf-8
from LxMaterial import mtlConfigure

from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlSet, _mtlElement


class Asn_Shaderset(mtlAbstract.Abc_AsnShaderset):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_NAME_CLS = _mtlRaw.Raw_Name
    SET_GEOMETRY_CLS = _mtlSet.Set_Geometry

    SHADERSET_CLS = _mtlElement.Elm_Shaderset

    separator_geometry = mtlConfigure.Separator_Raw_Basic

    xml_key_element = 'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMaterialAssign(*args)


class Asn_Portset(mtlAbstract.Abc_AsnPortset):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_NAME_CLS = _mtlRaw.Raw_Name
    SET_GEOMETRY_CLS = _mtlSet.Set_Geometry

    xml_key_element = 'propertyset'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcPortsetAssign(*args)
