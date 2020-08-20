# coding:utf-8
from LxMtx import mtxObjects

from .. import hou2mtxObjAbs

from ..hou2mtxObjects import _hou2mtxObjQuery, _hou2mtxObjElement


class File(hou2mtxObjAbs.AbsHou2mtxFile):
    CLS_mtx__trs_file__tgt_file = mtxObjects.File
    CLS_mtx__trs_file__trs_look = _hou2mtxObjElement.Look

    IST_mtx__trs_file__trs_obj_queue = _hou2mtxObjQuery.GRH_TRS_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsHou2mtxFile(*args)
