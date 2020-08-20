# coding:utf-8
from .. import mtxCfg, mtxObjAbs


class GeometryProxySet(mtxObjAbs.AbsMtxObjSet):
    VAR_grh__obj_stack__objsep = mtxCfg.MtxUtility.DEF_mtx__data_separator

    VAR_dat__xml_obj__attribute_attach_str = u'geom'

    def __init__(self, *args):
        self._initAbsMtxObjSet(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.bindPathString()


class ViewerGeometrySet(mtxObjAbs.AbsMtxObjSet):
    VAR_grh__obj_stack__objsep = mtxCfg.MtxUtility.DEF_mtx__data_separator

    VAR_dat__xml_obj__attribute_attach_str = u'viewergeom'

    def __init__(self, *args):
        self._initAbsMtxObjSet(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.bindPathString()
