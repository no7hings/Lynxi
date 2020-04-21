# coding:utf-8
from LxGraphic import grhCfg, grhObjAbs

from LxGraphic.grhObjects import _grhObjSet, _grhObjQuery

from ..import myaBscObjAbs


class QueryrawCache(myaBscObjAbs.Abs_MyaObjQueryCache):
    CLS_grh_node_queryraw = _grhObjQuery.NodeQueryraw

    CLS_grh_node_queryraw_set = _grhObjSet.NodeQueryrawSet

    def __init__(self, *args):
        self._initAbsMyaObjQueryCache(*args)


GRH_QUERYRAW_CACHE = QueryrawCache()


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


# object cache ******************************************************************************************************* #
class ObjCache(myaBscObjAbs.Abs_MyaObjCache):
    CLS_cache_obj_set = _grhObjSet.CacheObjSet

    def __init__(self, *args):
        self._initAbsMayObjCache(*args)


GRH_OBJ_CACHE = ObjCache()
