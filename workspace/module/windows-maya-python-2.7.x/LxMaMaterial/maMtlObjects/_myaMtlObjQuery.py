# coding:utf-8
from LxGraphic import grhObjDef

from LxMaterial.mtlObjects import _mtlObjCache, _mtlObjQuery

from ..import myaMtlCfg


class TrsObjQueryCache(grhObjDef.Def_GrhTrsObjQueryCache):
    VAR_mtl_dcc_node_file = myaMtlCfg.Utility.DEF_mya_arnold_node_defs_file
    VAR_mtl_dcc_geometry_file = myaMtlCfg.Utility.DEF_mya_arnold_geometry_def_file
    VAR_mtl_dcc_material_file = myaMtlCfg.Utility.DEF_mya_arnold_material_def_file
    VAR_mtl_dcc_output_file = myaMtlCfg.Utility.DEF_mya_arnold_output_defs_file
    VAR_mtl_dcc_port_child_file = myaMtlCfg.Utility.DEF_mya_arnold_port_child_defs_file

    VAR_mtl_dcc_custom_category_file = myaMtlCfg.Utility.DEF_mya_arnold_custom_category_file
    VAR_mtl_dcc_custom_node_file = myaMtlCfg.Utility.DEF_mya_arnold_custom_node_file

    CLS_mtl_dcc_object_def = _mtlObjCache.MtlDccObjectDef

    OBJ_grh_query_cache = _mtlObjQuery.OBJ_grh_query_cache_

    def __init__(self, *args):
        self._initDefGrhTrsObjQueryCache(*args)
