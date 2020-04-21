# coding:utf-8
from ..import mtlCfg, mtlObjAbs

from ..mtlObjects import _mtlObjQuery, _mtlObjValue, _mtlObjRaw, _mtlObjSet, _mtlObjPort


class MaterialAssign(mtlObjAbs.Abc_MtlMaterialAssign):
    CLS_mtl_name = _mtlObjRaw.Name
    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet

    DEF_geometry_separator = mtlCfg.Utility.DEF_mtl_data_separator

    VAR_dat_xml_file_element_tag = u'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlMaterialAssign(*args)


class PropertysetAssign(mtlObjAbs.Abc_MtlPropertysetAssign):
    CLS_mtl_name = _mtlObjRaw.Name
    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet

    CLS_mtl_propertyset = _mtlObjPort.Propertyset

    VAR_dat_xml_file_element_tag = u'propertysetassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlPropertysetAssign(*args)


class VisibilityAssign(mtlObjAbs.Abc_MtlVisibilityAssign):
    CLS_mtl_name = _mtlObjRaw.Name
    CLS_grh_type = _mtlObjRaw.VistypeString
    CLS_mtl_geometry_set = _mtlObjSet.GeometrySet
    CLS_set_geometry_viewer = _mtlObjSet.ViewerGeometrySet

    CLS_value_visibility = _mtlObjValue.Val_Visibility

    VAR_dat_xml_file_element_tag = u'visibility'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbcMtlVisibilityAssign(*args)
