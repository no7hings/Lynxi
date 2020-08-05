# coding:utf-8
from LxData.datObjects import _datObjRaw

from LxGraphic.grhObjects import _grhObjStack

from .. import maBscObjAbs

from ..maBscObjects import _maBscObjRaw, _maBscObjQuery


class Connector(maBscObjAbs.Abs_MaConnector):
    def __init__(self, *args):
        self._initAbsMaConnector(*args)


class Gnport(maBscObjAbs.Abs_MaPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _maBscObjRaw.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _maBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _maBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsMaPort(*args, **kwargs)


class Inport(maBscObjAbs.Abs_MaPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _maBscObjRaw.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _maBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _maBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsMaPort(*args, **kwargs)


class Otport(maBscObjAbs.Abs_MaPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _maBscObjRaw.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _maBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _maBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsMaPort(*args, **kwargs)


class Asport(maBscObjAbs.Abs_MaPort):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _maBscObjRaw.Attrpath

    CLS_grh__port__porttype = _datObjRaw.Porttype
    CLS_grh__port__datatype = _datObjRaw.Datatype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _maBscObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _maBscObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args, **kwargs):
        self._initAbsMaPort(*args, **kwargs)
