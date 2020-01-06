# coding:utf-8
from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlSet


class Prt_Shaderinput(mtlAbstract.Abc_Port):
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_CHILD_CLS = _mtlSet.Set_Attribute

    xml_prefix_label = 'bindinput'

    def __init__(self, *args):
        self._initAbcPort(*args)

    def _xmlStrRaw(self):
        return {
            self.Key_Label: self.xml_prefix_label,
            self.Key_Attribute: {
                self.Atr_Xml_Name: self.attributeFullpathName(),
                self.Atr_Xml_Type: self.valueTypeString(),
                self.Atr_Xml_Value: self.valueString()
            }
        }


class Prt_Nodeinput(mtlAbstract.Abc_Port):

    xml_prefix_label = 'input'

    def __init__(self, *args):
        self._initAbcPort(*args)


class Prt_Geometryinput(mtlAbstract.Abc_Port):
    def __init__(self, *args):
        self._initAbcPort(*args)


class Prt_Output(mtlAbstract.Abc_Port):
    def __init__(self, *args):
        self._initAbcPort(*args)
