# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet, _mtlObjElement


class Reference(mtlObjCore.Abc_MtlReference):
    CLS_mtl_filepath = _mtlObjRaw.ReferenceFileName
    CLS_mtl_version = _mtlObjRaw.VersionString

    CLS_mtl_reference = None
    CLS_mtl_reference_set = _mtlObjSet.ReferenceSet

    CLS_mtl_look = _mtlObjElement.Look
    CLS_mtl_look_set = _mtlObjSet.LookSet

    VAR_mtl_file_element_key = u'xi:include'
    VAR_mtlx_version = u'1.36'

    def __init__(self, *args):
        self._initAbcMtlReference(*args)


class File(mtlObjCore.Abc_MtlFile):
    CLS_mtl_filepath = _mtlObjRaw.FileName
    CLS_mtl_version = _mtlObjRaw.VersionString

    CLS_mtl_reference = Reference
    CLS_mtl_reference_set = _mtlObjSet.ReferenceSet

    CLS_mtl_look = _mtlObjElement.Look
    CLS_mtl_look_set = _mtlObjSet.LookSet

    VAR_mtl_file_element_key = u'materialx'
    VAR_mtlx_version = u'1.36'

    def __init__(self, *args):
        self._initAbcMtlFile(*args)
