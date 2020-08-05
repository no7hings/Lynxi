# coding:utf-8
from LxGraphic.grhObjects import _grhObjStack

from .. import maBscObjAbs

from ..maBscObjects import _maBscObjNode


class GeomAssign(maBscObjAbs.Abs_MaGeomAssign):
    CLS_grh__assign__obj = _maBscObjNode.Node

    def __init__(self, *args):
        self._initAbsMaGeomAssign(*args)
