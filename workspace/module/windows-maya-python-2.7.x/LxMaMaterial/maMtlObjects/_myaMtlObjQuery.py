# coding:utf-8
from LxGraphic import grhObjAbs

from LxGraphic.grhObjects import _grhObjSet, _grhObjQuery

from LxMaterial.mtlObjects import _mtlObjQuery

from ..import myaMtlCfg


class TrsObjQueryCache(grhObjAbs.Abs_GrhTrsObjQueryCache):
    CLS_grh_trs_node_raw = _grhObjQuery.TrsNodeQueryraw

    CLS_grh_trs_node_query_set = _grhObjSet.TrsNodeQuerySet
    CLS_grh_trs_node_query = _grhObjQuery.TrsNodeQuery

    VAR_grh_trs_node_file = myaMtlCfg.Utility.DEF_mya_arnold_node_defs_file
    VAR_grh_trs_geometry_file = myaMtlCfg.Utility.DEF_mya_arnold_geometry_def_file
    VAR_grh_trs_material_file = myaMtlCfg.Utility.DEF_mya_arnold_material_def_file
    VAR_grh_trs_output_file = myaMtlCfg.Utility.DEF_mya_arnold_output_defs_file
    VAR_grh_trs_port_child_file = myaMtlCfg.Utility.DEF_mya_arnold_port_child_defs_file

    VAR_grh_trs_custom_category_file = myaMtlCfg.Utility.DEF_mya_arnold_custom_category_file
    VAR_grh_trs_custom_node_file = myaMtlCfg.Utility.DEF_mya_arnold_custom_node_file

    OBJ_grh_query_cache = _mtlObjQuery.GRH_QUERY_CACHE

    def __init__(self, *args):
        self._initAbsGrhTrsObjQueryCache(*args)


GRH_TRS_QUERY_CACHE = TrsObjQueryCache()


class TrsObjCache(grhObjAbs.Abs_GrhObjCache):
    CLS_cache_obj_set = _grhObjSet.CacheTrsObjSet

    def __init__(self, *args):
        self._initAbsGrhObjCache(*args)


GRH_TRS_OBJ_CACHE = TrsObjCache()
