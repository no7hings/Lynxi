# coding:utf-8
from LxMtx import mtxObjects

from .. import ma2mtxObjAbs

from ..ma2mtxObjects import _ma2mtxObjNode


class Look(ma2mtxObjAbs.AbsMa2mtxLook):
    CLS_mtx__trs_look__tgt_look = mtxObjects.Look

    CLS_mtx__trs_look__trs_geometry_proxy = _ma2mtxObjNode.GeometryProxy

    def __init__(self, *args):
        self._initAbsMa2mtxLook(*args)
