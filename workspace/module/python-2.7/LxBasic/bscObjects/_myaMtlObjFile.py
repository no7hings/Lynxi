# coding:utf-8
from LxMaterial import mtlObjects

from ..import myaMtlObjCore

from ..maMtlObjects import _myaMtlObjQuery, _myaMtlObjElement


class File(myaMtlObjCore.Abc_MyaMtlFile):
    CLS_mtl_file = mtlObjects.File
    CLS_trs_look = _myaMtlObjElement.Look

    OBJ_grh_trs_obj_cache = _myaMtlObjQuery.GRH_TRS_OBJ_CACHE

    def __init__(self, *args):
        self._initAbcMyaMtlFile(*args)
