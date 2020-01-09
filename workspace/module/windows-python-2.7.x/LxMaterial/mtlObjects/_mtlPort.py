# coding:utf-8
from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlSet


class Prt_Shaderinput(mtlAbstract.Abc_Port):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlSet.Set_Port

    xml_key_element = 'bindinput'

    def __init__(self, *args):
        self._initAbcPort(*args)


class Prt_Shaderoutput(mtlAbstract.Abc_Port):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlSet.Set_Port

    xml_key_attribute = 'context'

    def __init__(self, *args):
        self._initAbcPort(*args)


class Prt_Nodeinput(mtlAbstract.Abc_Port):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath

    xml_key_element = 'input'

    def __init__(self, *args):
        self._initAbcPort(*args)


class Prt_Geometryinput(mtlAbstract.Abc_Port):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath

    xml_key_element = 'property'

    def __init__(self, *args):
        self._initAbcPort(*args)


class Prt_Output(mtlAbstract.Abc_Port):
    PROXY_XML_CLS = _mtlRaw.Raw_Xml

    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath

    xml_key_element = 'output'

    def __init__(self, *args):
        self._initAbcPort(*args)
