# coding:utf-8
from LxGraphic import grhCfg, grhObjAbs

from LxGraphic.grhObjects import _grhObjSet, _grhObjQuery

from LxMaterial.mtlObjects import _mtlObjQuery

from LxMaBasic.maBscObjects import _myaBscObjQuery

from ..import myaMtlCfg


class TrsObjQueryrawCache(grhObjAbs.Abs_GrhTrsObjQueryCache):
    CLS_grh_trs_node_queryraw_set = _grhObjSet.TrsNodeQueryrawSet
    CLS_grh_trs_node_queryraw = _grhObjQuery.TrsNodeQueryraw

    VAR_grh_trs_node_file = myaMtlCfg.Utility.DEF_mya_arnold_node_defs_file
    VAR_grh_trs_geometry_file = myaMtlCfg.Utility.DEF_mya_arnold_geometry_def_file
    VAR_grh_trs_material_file = myaMtlCfg.Utility.DEF_mya_arnold_material_def_file
    VAR_grh_trs_output_file = myaMtlCfg.Utility.DEF_mya_arnold_output_defs_file
    VAR_grh_trs_port_child_file = myaMtlCfg.Utility.DEF_mya_arnold_port_child_defs_file

    VAR_grh_trs_custom_category_file = myaMtlCfg.Utility.DEF_mya_arnold_custom_category_file
    VAR_grh_trs_custom_node_file = myaMtlCfg.Utility.DEF_mya_arnold_custom_node_file

    OBJ_grh_src_queryraw_cache = _myaBscObjQuery.GRH_QUERYRAW_CACHE
    OBJ_grh_tgt_queryraw_cache = _mtlObjQuery.GRH_QUERYRAW_CACHE

    def __init__(self, *args):
        self._initAbsGrhTrsObjQueryCache(*args)


GRH_TRS_QUERYRAW_CACHE = TrsObjQueryrawCache()


class TrsPortQuery(grhObjAbs.Abs_GrhTrsPortQuery):
    OBJ_grh_trs_queryraw_cache = GRH_TRS_QUERYRAW_CACHE

    def __init__(self, *args):
        self._initAbsGrhTrsPortQuery(*args)


class TrsNodeQuery(grhObjAbs.Abs_GrhTrsNodeQuery):
    CLS_grh_trs_port_query_set = _grhObjSet.TrsPortQuerySet
    CLS_grh_trs_port_query = TrsPortQuery

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    OBJ_grh_trs_queryraw_cache = GRH_TRS_QUERYRAW_CACHE

    def __init__(self, *args):
        self._initAbsGrhTrsNodeQuery(*args)


class TrsObjCache(grhObjAbs.Abs_GrhObjCache):
    CLS_cache_obj_set = _grhObjSet.CacheTrsObjSet

    def __init__(self, *args):
        self._initAbsGrhObjCache(*args)


GRH_TRS_OBJ_CACHE = TrsObjCache()
