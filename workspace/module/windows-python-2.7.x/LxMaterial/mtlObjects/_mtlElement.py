# coding:utf-8
from LxMaterial import mtlAbstract

from LxMaterial.mtlObjects import _mtlRaw, _mtlSet, _mtlDefinition


class Elt_Look(mtlAbstract.Abc_Look):
    RAW_NAME_CLS = _mtlRaw.Raw_Name
    SET_ASSIGN_CLS = _mtlSet.Set_Assign

    xml_prefix_label = 'look'

    def __init__(self, lookNameString):
        self._initAbcLook(lookNameString)


class Elt_Material(mtlAbstract.Abc_Material):
    RAW_DAGPATH_CLS = _mtlRaw.Raw_Dagpath
    SET_SHADER_CLS = _mtlSet.Set_Dag

    xml_prefix_label = 'material'
    xml_name_suffix_label = '_MAT'

    def __init__(self, *args):
        """
        :param args: str(materialName)
        """
        self._initAbcMaterial(*args)

    def _xmlStrRaw(self):
        return {
            self.Key_Label: self.xml_prefix_label,
            self.Key_Attribute: {
                self.Atr_Xml_Name: u'{}{}'.format(self.fullpathName(), self.xml_name_suffix_label)
            },
            self.Key_Children: self.shaders()
        }
