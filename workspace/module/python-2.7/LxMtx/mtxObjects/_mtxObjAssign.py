# coding:utf-8
from .. import mtxCfg, mtxObjAbs

from . import _mtxObjValue, _mtxObjRaw, _mtxObjStack, _mtxObjPort


class MaterialAssign(mtxObjAbs.AbsMtxMaterialAssign):
    CLS_mtx__name = _mtxObjRaw.Name
    CLS_mtx__look__geometry_proxy_stack = _mtxObjStack.GeometryProxySet

    DEF_geometry_separator = mtxCfg.MtxUtility.DEF_mtx__data_separator

    VAR_dat__xml_obj__element_prefix_str = u'materialassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbsMtxMaterialAssign(*args)


class PropertysetAssign(mtxObjAbs.AbsMtxPropertysetAssign):
    CLS_mtx__name = _mtxObjRaw.Name
    CLS_mtx__look__geometry_proxy_stack = _mtxObjStack.GeometryProxySet

    CLS_mtx__propertyset = _mtxObjPort.Propertyset

    VAR_dat__xml_obj__element_prefix_str = u'propertysetassign'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbsMtxPropertysetAssign(*args)


class VisibilityAssign(mtxObjAbs.AbsMtxVisibilityAssign):
    CLS_grh__type = _mtxObjRaw.VistypeString
    CLS_mtx__name = _mtxObjRaw.Name

    CLS_mtx__look__geometry_proxy_stack = _mtxObjStack.GeometryProxySet
    CLS_mtx__geometry_viewer_set = _mtxObjStack.ViewerGeometrySet

    CLS_mtx__value_visibility = _mtxObjValue.Val_Visibility

    VAR_dat__xml_obj__element_prefix_str = u'visibility'

    def __init__(self, *args):
        """
        :param args: nameString
        """
        self._initAbsMtxVisibilityAssign(*args)
