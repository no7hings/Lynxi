# coding:utf-8
from LxMaterial import mtlObjects

from .. import maMtlObjCore

from ..maMtlObjects import _myaMtlObjObject, _myaMtlObjElement


class File(maMtlObjCore.Abc_MyaMtlFile):
    CLS_mtl_file = mtlObjects.File
    CLS_trs_look = _myaMtlObjElement.Look

    CLS_trs_geometry = _myaMtlObjObject.Geometry

    def __init__(self, *args):
        self._initAbcMyaMtlFile(*args)
