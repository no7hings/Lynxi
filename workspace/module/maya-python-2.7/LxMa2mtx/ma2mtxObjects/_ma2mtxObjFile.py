# coding:utf-8
from LxMtx import mtxObjects

from .. import ma2mtxObjAbs

from ..ma2mtxObjects import _ma2mtxObjQuery, _ma2mtxObjElement


class File(ma2mtxObjAbs.AbsMa2mtxFile):
    CLS_mtx__trs_file__tgt_file = mtxObjects.File
    CLS_mtx__trs_file__trs_look = _ma2mtxObjElement.Look

    IST_mtx__trs_file__trs_obj_queue = _ma2mtxObjQuery.GRH_TRS_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsMa2mtxFile(*args)
