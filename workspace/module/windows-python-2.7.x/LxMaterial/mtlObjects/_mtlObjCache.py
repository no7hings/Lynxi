# coding:utf-8
from ..import mtlCfg, mtlObjDef

from ..mtlObjects import _mtlObjQuery


class MtlDccRawTranslator(mtlObjDef.Def_GrhTrsNodeRaw):
    OBJ_grh_query_cache = _mtlObjQuery.OBJ_grh_query_cache_

    VAR_mtl_def_key_list = [
        mtlCfg.Utility.DEF_mtl_key_mtl_port,
        mtlCfg.Utility.DEF_mtl_key_mtl_portdata,
        mtlCfg.Utility.DEF_mtl_key_custom_node,
        mtlCfg.Utility.DEF_mtl_key_create_expression,
        mtlCfg.Utility.DEF_mtl_key_after_expression
    ]

    def __init__(self, dccObjectRaw, dccOutputRaw, dccPortChildRaw):
        self._initDefGrhTrsNodeRaw(dccObjectRaw, dccOutputRaw, dccPortChildRaw)


class MtlDccPortDef(mtlObjDef.Def_GrhTrsPortQuery):
    def __init__(self, dccPortString, portRaw):
        self._initDefGrhTrsPortQuery(dccPortString, portRaw)


class MtlDccObjectDef(mtlObjDef.Def_GrhTrsNodeQuery):
    CLS_mtl_dcc_port_def = MtlDccPortDef

    CLS_mtl_dcc_raw_translator = MtlDccRawTranslator

    VAR_mtl_def_key_list = [
        mtlCfg.Utility.DEF_mtl_key_mtl_port,
        mtlCfg.Utility.DEF_mtl_key_custom_node,
        mtlCfg.Utility.DEF_mtl_key_create_expression,
        mtlCfg.Utility.DEF_mtl_key_after_expression
    ]

    def __init__(self, dccCategoryString, objectRaw, outputRaw, childRaw):
        self._initDefGrhTrsNodeQuery(dccCategoryString, objectRaw, outputRaw, childRaw)
