# coding:utf-8
from ..import mtlCfg, mtlObjAbs


class GeometrySet(mtlObjAbs.Abs_MtlObjSet):
    VAR_dat_xml_file_attribute_attach_tag = u'geom'

    VAR_grh_objectsep = mtlCfg.Utility.DEF_mtl_data_separator

    def __init__(self, *args):
        self._initAbsMtlObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.node().nodepathString()


class ViewerGeometrySet(mtlObjAbs.Abs_MtlObjSet):
    VAR_dat_xml_file_attribute_attach_tag = u'viewergeom'

    VAR_grh_objectsep = mtlCfg.Utility.DEF_mtl_data_separator

    def __init__(self, *args):
        self._initAbsMtlObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.node().nodepathString()
