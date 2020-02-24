# coding:utf-8
from LxMaterial import mtlObjCore

from LxMaterial.mtlObjects import _mtlObjRaw, _mtlObjSet


class XmlDocument(mtlObjCore.Abc_MtlFile):
    CLS_raw_file = _mtlObjRaw.Raw_Reference
    CLS_raw_version = _mtlObjRaw.Raw_Version

    CLS_set_reference = _mtlObjSet.Set_Reference
    CLS_set_look = _mtlObjSet.Set_Look

    VAR_mtlx_key_element = u'materialx'
    DEF_mtlx_version = u'1.36'

    def __init__(self, *args):
        self._initAbcMtlFile(*args)
