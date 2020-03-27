# coding:utf-8
from LxMaBasic import myaBscObjCore


class MyaQueryCache(myaBscObjCore.Abc_MyaQueryCache):
    def __init__(self):
        self._initAbcMyaQueryCache()


OBJ_mya_query_cache = MyaQueryCache()
