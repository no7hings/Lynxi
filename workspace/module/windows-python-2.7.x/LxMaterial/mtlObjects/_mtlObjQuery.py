# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet, _grhObjQuery

from ..import mtlCfg, mtlObjAbs


class QueryCache(mtlObjAbs.Abs_MtlObjQueryCache):
    CLS_mtl_node_raw = _grhObjQuery.NodeRaw

    CLS_grh_node_query_set = _grhObjSet.NodeQuerySet
    CLS_grh_node_query = _grhObjQuery.NodeQuery

    VAR_mtl_node_file = mtlCfg.Utility.DEF_mtl_arnold_node_defs_file
    VAR_mtl_geometry_file = mtlCfg.Utility.DEF_mtl_arnold_geometry_def_file
    VAR_mtl_material_file = mtlCfg.Utility.DEF_mtl_arnold_material_def_file
    VAR_mtl_output_file = mtlCfg.Utility.DEF_mtl_arnold_output_defs_file
    VAR_mtl_port_child_file = mtlCfg.Utility.DEF_mtl_arnold_port_child_defs_file

    def __init__(self, *args):
        self._initAbsMtlObjQueryCache(*args)


OBJ_grh_query_cache_ = QueryCache()


class ObjCache(mtlObjAbs.Abs_MtlObjCache):
    CLS_cache_obj_set = _grhObjSet.CacheObjSet

    def __init__(self, *args):
        self._initAbsMtlObjCache(*args)


OBJ_grh_obj_cache_ = ObjCache()


class TrsObjCache(mtlObjAbs.Abs_MtlObjCache):
    CLS_cache_obj_set = _grhObjSet.CacheTrsObjSet

    def __init__(self, *args):
        self._initAbsMtlObjCache(*args)


OBJ_grh_trs_obj_cache_ = TrsObjCache()
