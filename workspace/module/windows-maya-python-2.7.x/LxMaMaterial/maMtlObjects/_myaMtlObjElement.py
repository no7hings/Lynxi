# coding:utf-8
from LxMaterial import mtlObjects

from .. import maMtlObjCore

from ..maMtlObjects import _myaMtlObjObject


class Look(maMtlObjCore.Abc_MyaMtlLook):
    CLS_mtl_look = mtlObjects.Look

    CLS_trs_geometry = _myaMtlObjObject.Geometry

    def __init__(self, *args):
        self._initAbcMyaMtlLook(*args)
