# coding:utf-8
from LxMtx import mtxObjects

from .. import usd2mtxObjAbs

from ..usd2mtxObjects import _usd2mtxObjQuery, _usd2mtxObjElement


class File(usd2mtxObjAbs.AbsUsd2mtxFile):
    CLS_mtx__trs_file__tgt_file = mtxObjects.File
    CLS_mtx__trs_file__trs_look = _usd2mtxObjElement.Look

    IST_mtx__trs_file__trs_obj_queue = _usd2mtxObjQuery.GRH_TRS_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsUsd2mtxFile(*args)
