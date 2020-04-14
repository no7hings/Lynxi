# coding:utf-8
from LxMaterial import mtlObjects

from ..import myaMtlObjCore

from ..maMtlObjects import _myaMtlObjElement


class File(myaMtlObjCore.Abc_MyaMtlFile):
    CLS_mtl_file = mtlObjects.File
    CLS_trs_look = _myaMtlObjElement.Look

    OBJ_mtl_trs_obj_cache = mtlObjects.OBJ_grh_trs_obj_cache_

    def __init__(self, *args):
        self._initAbcMyaMtlFile(*args)
