# coding:utf-8
from LxData.datObjects import _datObjRaw

from LxGraphic.grhObjects import _grhObjStack

from .. import houBscObjAbs

from ..houBscObjects import _houBscObjData, _houBscObjQuery


class Connector(houBscObjAbs.AbsHouConnector):
    def __init__(self, *args):
        self._initAbsHoConnector(*args)


class Gnport(houBscObjAbs.AbsHouPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _houBscObjData.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _houBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _houBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsHoPort(*args, **kwargs)


class Inport(houBscObjAbs.AbsHouPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _houBscObjData.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _houBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _houBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsHoPort(*args, **kwargs)


class Otport(houBscObjAbs.AbsHouPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack

    CLS_grh__obj__path = _houBscObjData.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _houBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _houBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsHoPort(*args, **kwargs)


class Asport(houBscObjAbs.AbsHouPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack

    CLS_grh__obj__path = _houBscObjData.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _houBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _houBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsHoPort(*args, **kwargs)
