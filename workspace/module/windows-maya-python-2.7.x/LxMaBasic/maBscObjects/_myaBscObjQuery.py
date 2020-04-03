# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet, _grhObjQuery

from .. import myaBscObjCore


class QueryCache(myaBscObjCore.Abs_MyaQueryCache):
    CLS_grh_node_query_set = _grhObjSet.NodeQuerySet
    CLS_grh_node_query = _grhObjQuery.NodeQuery

    def __init__(self, *args):
        self._initAbsMyaQueryCache(*args)


class ObjCache(myaBscObjCore.Abs_MyaObjCache):
    CLS_cache_obj_set = _grhObjSet.CacheObjSet

    def __init__(self, *args):
        self._initAbsMayObjCache(*args)


OBJ_grh_query_cache = QueryCache()
OBJ_grh_obj_cache = ObjCache()
