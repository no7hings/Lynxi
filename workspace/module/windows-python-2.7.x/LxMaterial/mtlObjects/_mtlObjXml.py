# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


class XmlDocument(mtlObjCore.Abc_MtlFile):
    CLS_mtl_file = _mtlObjRaw.Raw_Reference
    CLS_mtl_version = _mtlObjRaw.VersionString

    CLS_mtl_reference_file_set = _mtlObjSet.Set_Reference
    CLS_mtl_look_set = _mtlObjSet.Set_Look

    VAR_mtl_file_element_key = u'materialx'
    VAR_mtlx_version = u'1.36'

    def __init__(self, *args):
        self._initAbcMtlFile(*args)
