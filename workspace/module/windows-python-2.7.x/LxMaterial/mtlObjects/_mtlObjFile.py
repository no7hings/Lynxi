# coding:utf-8
from LxGraphic.grhObjects import _grhObjSet

from ..import mtlObjAbs

from ..mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjElement


class Reference(mtlObjAbs.Abc_MtlReference):
    CLS_mtl_filepath = _mtlObjRaw.RefFilepath
    CLS_mtl_version = _mtlObjRaw.Version

    CLS_mtl_reference_set = _grhObjSet.ObjSet
    CLS_mtl_reference = None

    CLS_mtl_look_set = _grhObjSet.ObjSet
    CLS_mtl_look = _mtlObjElement.Look

    VAR_mtl_file_element_key = u'xi:include'
    VAR_mtlx_version = u'1.36'

    def __init__(self, *args):
        self._initAbcMtlReference(*args)


class File(mtlObjAbs.Abc_MtlFile):
    CLS_mtl_filepath = _mtlObjRaw.Filepath
    CLS_mtl_version = _mtlObjRaw.Version

    CLS_mtl_reference = Reference
    CLS_mtl_reference_set = _grhObjSet.ObjSet

    CLS_mtl_look_set = _grhObjSet.ObjSet
    CLS_mtl_look = _mtlObjElement.Look

    VAR_mtl_file_element_key = u'materialx'
    VAR_mtlx_version = u'1.36'

    def __init__(self, *args):
        self._initAbcMtlFile(*args)
