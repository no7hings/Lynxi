# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet, _grhObjQuery

from ..import myaBscObjAbs


class QueryCache(myaBscObjAbs.Abs_MyaObjQueryCache):
    CLS_grh_node_query_set = _grhObjSet.NodeQuerySet
    CLS_grh_node_query = _grhObjQuery.NodeQuery

    def __init__(self, *args):
        self._initAbsMyaObjQueryCache(*args)


GRH_QUERY_CACHE = QueryCache()


class ObjCache(myaBscObjAbs.Abs_MyaObjCache):
    CLS_cache_obj_set = _grhObjSet.CacheObjSet

    def __init__(self, *args):
        self._initAbsMayObjCache(*args)


GRH_OBJ_CACHE = ObjCache()
