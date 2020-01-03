# coding:utf-8
from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlObjectSet, _mtlDefinition


class Elt_Look(mtlAbstract.Abc_Look):
    RAW_NAME_CLS = _mtlRaw.Raw_Name

    def __init__(self, lookNameString):
        self._initAbcLook(lookNameString)


class Elt_Shaderset(mtlAbstract.Abc_Shaderset):
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_SHADER_CLS = _mtlObjectSet.Set_Dag

    xml_prefix_label = 'material'
    xml_name_suffix_label = '_MAT'

    def __init__(self, *args):
        """
        :param args: str(material_name)
        """
        self._initAbcShaderset(*args)

    def _xmlStrRaw(self):
        return {
            self.Key_Label: self.xml_prefix_label,
            self.Key_Attribute: {
                self.Atr_Xml_Name: '{}{}'.format(self.fullpathName(), self.xml_name_suffix_label)
            },
            self.Key_Children: self.shaders()
        }
