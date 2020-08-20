# coding:utf-8
from LxGraphic.grhObjects import _grhObjStack

from .. import mtxObjAbs

from . import _mtxObjRaw, _mtxObjStack, _mtxObjAssign


class Look(mtxObjAbs.AbsMtxLook):
    CLS_mtx__look__name = _mtxObjRaw.Name
    CLS_mtx__look__namespace = _mtxObjRaw.ObjProxyNamespace

    CLS_mtx__look__assign_stack = _grhObjStack.ObjStack

    CLS_mtx__look__material_assign = _mtxObjAssign.MaterialAssign
    CLS_mtx__look__material_assign_stack = _grhObjStack.ObjStack

    CLS_mtx__look__propertyset_assign = _mtxObjAssign.PropertysetAssign
    CLS_mtx__look__propertyset_assign_stack = _grhObjStack.ObjStack

    CLS_mtx__look__visibility_assign = _mtxObjAssign.VisibilityAssign
    CLS_mtx__look__visibility_assign_stack = _grhObjStack.ObjStack

    CLS_mtx__look__geometry_proxy_stack = _mtxObjStack.GeometryProxySet

    VAR_dat__xml_obj__element_prefix_str = u'look'
    VAR_dat__xml_obj__attribute_attach_str = u'look'

    def __init__(self, *args):
        self._initAbsMtxLook(*args)


class Collection(mtxObjAbs.AbsMtxCollection):
    CLS_mtx__name = _mtxObjRaw.Name

    CLS_mtx__look__geometry_proxy_stack = _grhObjStack.ObjStack
    CLS_mtx__collection_set = _grhObjStack.ObjStack

    DEF_geometry_separator = u','

    VAR_dat__xml_obj__element_prefix_str = u'collection'
    VAR_dat__xml_obj__attribute_attach_str = u'collection'

    def __init__(self, *args):
        self._initAbsMtxCollection(*args)
