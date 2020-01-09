# coding:utf-8
from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlSet


class Elm_Look(mtlAbstract.Abc_Look):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_NAME_CLS = _mtlRaw.Raw_Name
    SET_ASSIGN_CLS = _mtlSet.Set_Assign

    xml_key_element = 'look'
    xml_key_attribute = 'look'

    def __init__(self, *args):
        self._initAbcLook(*args)


class Elm_Shaderset(mtlAbstract.Abc_Shaderset):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_SHADER_CLS = _mtlSet.Set_Dag

    xml_key_element = 'material'
    xml_key_attribute = 'material'

    xml_name_label_suffix = '_MAT'

    def __init__(self, *args):
        """
        :param args: str(materialName)
        """
        self._initAbcShaderset(*args)


class Elm_Portset(mtlAbstract.Abc_Portset):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_PORT_INPUT_CLS = _mtlSet.Set_Dag

    xml_key_element = 'propertyset'
    xml_key_attribute = 'propertyset'

    xml_name_label_suffix = '_PRT'

    def __init__(self, *args):
        """
        :param args: str(materialName)
        """
        self._initAbcPortset(*args)
