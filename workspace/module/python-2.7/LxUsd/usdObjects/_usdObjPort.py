# coding:utf-8
from LxData.datObjects import _datObjRaw

from LxGraphic.grhObjects import _grhObjStack

from .. import usdObjAbs

from ..usdObjects import _usdObjRaw, _usdObjQuery


class Connector(usdObjAbs.Abs_UsdConnector):
    def __init__(self, *args):
        self._initAbsUsdConnector(*args)


class Gnport(usdObjAbs.Abs_UsdPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _usdObjRaw.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    CLS_grh__obj__loader = _usdObjQuery.ObjLoader
    IST_grh__obj__query_builder = _usdObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _usdObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsUsdPort(*args)


class Inport(usdObjAbs.Abs_UsdPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _usdObjRaw.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    CLS_grh__obj__loader = _usdObjQuery.ObjLoader
    IST_grh__obj__query_builder = _usdObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _usdObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsUsdPort(*args)


class Otport(usdObjAbs.Abs_UsdPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _usdObjRaw.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    CLS_grh__obj__loader = _usdObjQuery.ObjLoader
    IST_grh__obj__query_builder = _usdObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _usdObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsUsdPort(*args)


class Asport(usdObjAbs.Abs_UsdPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _usdObjRaw.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    CLS_grh__obj__loader = _usdObjQuery.ObjLoader
    IST_grh__obj__query_builder = _usdObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _usdObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsUsdPort(*args)


