# coding:utf-8
from LxMtx import mtxObjects

from .. import hou2mtxObjAbs

from ..hou2mtxObjects import _hou2mtxObjNode


class Look(hou2mtxObjAbs.AbsHou2mtxLook):
    CLS_mtx__trs_look__tgt_look = mtxObjects.Look

    CLS_mtx__trs_look__trs_geometry_proxy = _hou2mtxObjNode.GeometryProxy

    def __init__(self, *args):
        self._initAbsHou2mtxLook(*args)
