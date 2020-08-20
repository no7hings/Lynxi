# coding:utf-8
from LxGraphic.grhObjects import _grhObjStack

from .. import mtxObjAbs

from . import _mtxObjRaw, _mtxObjElement


class Reference(mtxObjAbs.AbsMtxReference):
    CLS_mtx__file__path = _mtxObjRaw.RefFilepath
    CLS_mtx__file__version = _mtxObjRaw.Version

    CLS_mtx__file__reference_stack = _grhObjStack.ObjStack
    CLS_mtx__file__reference = None

    CLS_mtx__file__look_stack = _grhObjStack.ObjStack
    CLS_mtx__file__look = _mtxObjElement.Look

    VAR_dat__xml_obj__element_prefix_str = u'xi:include'
    VAR_mtx__file__version = u'1.36'

    def __init__(self, *args):
        self._initAbsMtxReference(*args)


class File(mtxObjAbs.AbsMtxFile):
    CLS_mtx__file__path = _mtxObjRaw.Filepath
    CLS_mtx__file__version = _mtxObjRaw.Version

    CLS_mtx__file__reference = Reference
    CLS_mtx__file__reference_stack = _grhObjStack.ObjStack

    CLS_mtx__file__look_stack = _grhObjStack.ObjStack
    CLS_mtx__file__look = _mtxObjElement.Look

    VAR_dat__xml_obj__element_prefix_str = u'materialx'
    VAR_mtx__file__version = u'1.36'

    def __init__(self, *args):
        self._initAbsMtxFile(*args)
