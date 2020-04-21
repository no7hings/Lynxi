# coding:utf-8
from LxGraphic import grhCfg, grhObjAbs

from LxGraphic.grhObjects import _grhObjSet, _grhObjQuery

from ..import mtlCfg, mtlObjAbs


class QueryrawCache(mtlObjAbs.Abs_MtlObjQueryCache):
    CLS_grh_node_queryraw = _grhObjQuery.NodeQueryraw

    CLS_grh_node_queryraw_set = _grhObjSet.NodeQueryrawSet

    VAR_grh_node_file = mtlCfg.Utility.DEF_mtl_arnold_node_defs_file
    VAR_grh_geometry_file = mtlCfg.Utility.DEF_mtl_arnold_geometry_def_file
    VAR_grh_material_file = mtlCfg.Utility.DEF_mtl_arnold_material_def_file
    VAR_grh_output_file = mtlCfg.Utility.DEF_mtl_arnold_output_defs_file
    VAR_grh_port_child_file = mtlCfg.Utility.DEF_mtl_arnold_port_child_defs_file

    def __init__(self, *args):
        self._initAbsMtlObjQueryCache(*args)


GRH_QUERYRAW_CACHE = QueryrawCache()


class ObjCache(mtlObjAbs.Abs_MtlObjCache):
    CLS_cache_obj_set = _grhObjSet.CacheObjSet

    def __init__(self, *args):
        self._initAbsMtlObjCache(*args)


GRH_OBJ_CACHE = ObjCache()


class PortQuery(grhObjAbs.Abs_GrhPortQuery):
    VAR_grh_portsep = grhCfg.Utility.DEF_grh_port_pathsep

    OBJ_grh_queryraw_cache = GRH_QUERYRAW_CACHE

    def __init__(self, *args):
        self._initAbsGrhPortQuery(*args)


class NodeQuery(grhObjAbs.Abs_GrhNodeQuery):
    CLS_grh_port_query_set = _grhObjSet.PortQuerySet
    CLS_grh_port_query = PortQuery

    VAR_grh_param_assign_keyword_list = grhCfg.Utility.DEF_grh_param_assign_keyword_list
    VAR_grh_inparm_assign_keyword_list = grhCfg.Utility.DEF_grh_inparm_assign_keyword_list
    VAR_grh_otparm_assign_keyword_list = grhCfg.Utility.DEF_grh_otparm_assign_keyword_list

    OBJ_grh_queryraw_cache = GRH_QUERYRAW_CACHE

    def __init__(self, *args):
        self._initAbsGrhNodeQuery(*args)
