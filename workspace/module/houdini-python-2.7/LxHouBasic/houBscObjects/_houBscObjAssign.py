# coding:utf-8
from .. import houBscObjAbs

from ..houBscObjects import _houBscObjNode


class GeomAssign(houBscObjAbs.AbsHouGeomAssign):
    CLS_grh__assign__obj = _houBscObjNode.Node
    VAR_grh__assign__mesh_typepath_str = 'Object/geo'

    def __init__(self, *args):
        self._initAbsHoGeomAssign(*args)
