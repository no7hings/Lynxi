# coding:utf-8
from LxMaterial import mtlObjects

from .. import myaMtlObjCore

from ..maMtlObjects import _myaMtlObjObject


class Look(myaMtlObjCore.Abc_MyaMtlLook):
    CLS_mtl_look = mtlObjects.Look

    CLS_mtl_trs_geometry_proxy = _myaMtlObjObject.GeometryProxy

    def __init__(self, *args):
        self._initAbcMyaMtlLook(*args)
