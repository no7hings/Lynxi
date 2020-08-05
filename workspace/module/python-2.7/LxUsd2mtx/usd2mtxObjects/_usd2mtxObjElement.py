# coding:utf-8
from LxMtx import mtxObjects

from .. import usd2mtxObjAbs

from ..usd2mtxObjects import _usd2mtxObjNode


class Look(usd2mtxObjAbs.Abs_Usd2mtxLook):
    CLS_mtx__trs_look__tgt_look = mtxObjects.Look

    CLS_mtx__trs_look__trs_geometry_proxy = _usd2mtxObjNode.GeometryProxy

    def __init__(self, *args):
        self._initAbsUsd2mtxLook(*args)
