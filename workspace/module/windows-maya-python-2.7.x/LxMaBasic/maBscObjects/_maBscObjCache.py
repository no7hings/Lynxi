# coding:utf-8
from LxMaBasic import maBscObjCore


class MyaQueryCache(maBscObjCore.Abc_MyaQueryCache):
    def __init__(self):
        self._initAbcMyaQueryCache()


OBJ_mya_query_cache = MyaQueryCache()
