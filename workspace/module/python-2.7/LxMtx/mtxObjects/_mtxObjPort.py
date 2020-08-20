# coding:utf-8
from LxData.datObjects import _datObjRaw

from LxGraphic.grhObjects import _grhObjStack

from .. import mtxCfg, mtxObjAbs

from . import _mtxObjRaw, _mtxObjValue, _mtxObjQuery


class Connector(mtxObjAbs.AbsMtxConnector):
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsMtxConnector(*args)


# port *************************************************************************************************************** #
class __PortDef__(object):
    VAR_grh__value_cls_dict = {
        mtxCfg.MtxUtility.DEF_mtx__datatype__closure: _mtxObjValue.Val_Closure,

        mtxCfg.MtxUtility.DEF_mtx__datatype__shader: _mtxObjValue.Val_Closure,
        mtxCfg.MtxUtility.DEF_mtx__datatype__visibility: _mtxObjValue.Val_Visibility,

        mtxCfg.MtxUtility.DEF_mtx__datatype__boolean: _mtxObjValue.Val_Boolean,
        mtxCfg.MtxUtility.DEF_mtx__datatype__Integer: _mtxObjValue.Val_Integer,
        mtxCfg.MtxUtility.DEF_mtx__datatype__integerarray: _mtxObjValue.Val_IntegerArray,
        mtxCfg.MtxUtility.DEF_mtx__datatype__float: _mtxObjValue.Val_Float,
        mtxCfg.MtxUtility.DEF_mtx__datatype__floatarray: _mtxObjValue.Val_FloatArray,

        mtxCfg.MtxUtility.DEF_mtx__datatype__color2: _mtxObjValue.Val_Color2,
        mtxCfg.MtxUtility.DEF_mtx__datatype__color2array: _mtxObjValue.Val_Color2Array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__color3: _mtxObjValue.Val_Color3,
        mtxCfg.MtxUtility.DEF_mtx__datatype__color3array: _mtxObjValue.Val_Color3Array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__color4: _mtxObjValue.Val_Color4,
        mtxCfg.MtxUtility.DEF_mtx__datatype__color4array: _mtxObjValue.Val_Color4Array,

        mtxCfg.MtxUtility.DEF_mtx__datatype__vector2: _mtxObjValue.Val_Vector2,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector2array: _mtxObjValue.Val_Vector2Array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector3: _mtxObjValue.Val_Vector3,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector3array: _mtxObjValue.Val_Vector3Array,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector4: _mtxObjValue.Val_Vector4,
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector4array: _mtxObjValue.Val_Vector4Array,

        mtxCfg.MtxUtility.DEF_mtx__datatype__matrix33: _mtxObjValue.Val_Matrix33,
        mtxCfg.MtxUtility.DEF_mtx__datatype__matrix44: _mtxObjValue.Val_Matrix44,

        mtxCfg.MtxUtility.DEF_mtx__datatype__string: _mtxObjValue.Val_String,
        mtxCfg.MtxUtility.DEF_mtx__datatype__stringarray: _mtxObjValue.Val_StringArray,
        mtxCfg.MtxUtility.DEF_mtx__datatype__filename: _mtxObjValue.Val_Filepath,
        mtxCfg.MtxUtility.DEF_mtx__datatype__geomname: _mtxObjValue.Val_Nodename,
        mtxCfg.MtxUtility.DEF_mtx__datatype__geomnamearray: _mtxObjValue.Val_NodenameArray
    }


class Gnport(
    __PortDef__,
    mtxObjAbs.AbsMtxPort
):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _mtxObjRaw.Attrpath

    CLS_grh__port__datatype = _mtxObjRaw.Datatype
    CLS_grh__port__porttype = _mtxObjRaw.Porttype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _mtxObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'input'
    VAR_dat__xml_obj__attribute_attach_str = u'member'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPort(*args, **kwargs)


class Gnchannel(
    __PortDef__,
    mtxObjAbs.AbsMtxPort
):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _mtxObjRaw.Attrpath

    CLS_grh__port__datatype = _mtxObjRaw.Datatype
    CLS_grh__port__porttype = _mtxObjRaw.Porttype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _mtxObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'input'
    VAR_dat__xml_obj__attribute_attach_str = u'channels'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPort(*args, **kwargs)


class Inport(
    __PortDef__,
    mtxObjAbs.AbsMtxPort
):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _mtxObjRaw.Attrpath

    CLS_grh__port__datatype = _mtxObjRaw.Datatype
    CLS_grh__port__porttype = _mtxObjRaw.Porttype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _mtxObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    VAR_dat__xml_obj__element_prefix_str = u'input'
    VAR_dat__xml_obj__attribute_attach_str = u'member'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPort(*args, **kwargs)


class Inchannel(
    __PortDef__,
    mtxObjAbs.AbsMtxPort
):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _mtxObjRaw.Attrpath

    CLS_grh__port__datatype = _mtxObjRaw.Datatype
    CLS_grh__port__porttype = _mtxObjRaw.Porttype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _mtxObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'input'
    VAR_dat__xml_obj__attribute_attach_str = u'channels'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPort(*args, **kwargs)


class Otport(
    __PortDef__,
    mtxObjAbs.AbsMtxPort
):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _mtxObjRaw.Attrpath

    CLS_grh__port__datatype = _mtxObjRaw.Datatype
    CLS_grh__port__porttype = _mtxObjRaw.Porttype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _mtxObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'output'
    VAR_dat__xml_obj__attribute_attach_str = u'member'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPort(*args, **kwargs)


class Otchannel(
    __PortDef__,
    mtxObjAbs.AbsMtxPort
):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _mtxObjRaw.Attrpath

    CLS_grh__port__datatype = _mtxObjRaw.Datatype
    CLS_grh__port__porttype = _mtxObjRaw.Porttype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _mtxObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'output'
    VAR_dat__xml_obj__attribute_attach_str = u'channels'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPort(*args, **kwargs)


class Asport(
    __PortDef__,
    mtxObjAbs.AbsMtxPort
):
    CLS_grh__cache_obj__variant = _datObjRaw.ObjVariant
    CLS_grh__cache_obj__variant_obj_stack = _grhObjStack.VariantObjStack

    CLS_grh__obj__obj_stack = _grhObjStack.ObjStack
    CLS_grh__obj__obj_proxy_stack = _grhObjStack.ObjProxyStack
    CLS_grh__obj__path = _mtxObjRaw.Attrpath

    CLS_grh__port__datatype = _mtxObjRaw.Datatype
    CLS_grh__port__porttype = _mtxObjRaw.Porttype
    CLS_grh__port__assign = _datObjRaw.Name

    IST_grh__obj__query_builder = _mtxObjQuery.GRH_OBJ_QUERY_BUILDER
    IST_grh__obj__queue = _mtxObjQuery.GRH_OBJ_QUEUE

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'assign'
    VAR_dat__xml_obj__attribute_attach_str = u'member'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPort(*args, **kwargs)


# port proxy ********************************************************************************************************* #
class GnportProxy(mtxObjAbs.AbsMtxPortProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Attrpath

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'bindparam'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPortProxy(*args, **kwargs)


class InportProxy(mtxObjAbs.AbsMtxPortProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Attrpath

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'bindinput'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPortProxy(*args, **kwargs)


class OtportProxy(mtxObjAbs.AbsMtxPortProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Attrpath

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'bindoutput'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPortProxy(*args, **kwargs)


class AsportProxy(mtxObjAbs.AbsMtxPortProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Attrpath

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'bindassign'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPortProxy(*args, **kwargs)


class NodeGraphOtportProxy(mtxObjAbs.AbsMtxNodeGraphOtportProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Attrpath

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'output'
    VAR_dat__xml_obj__attribute_attach_str = u'output'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxNodeGraphOtportProxy(*args, **kwargs)


# geometry port proxy ************************************************************************************************ #
class Property(mtxObjAbs.AbsMtxPortProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Attrpath

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'property'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPortProxy(*args, **kwargs)


class Visibility(mtxObjAbs.AbsMtxPortProxy):
    CLS_grh__obj_proxy__obj_namespace = _mtxObjRaw.ObjProxyNamespace
    CLS_grh__obj_proxy__obj_path = _mtxObjRaw.Attrpath

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'visibility'

    def __init__(self, *args, **kwargs):
        self._initAbsMtxPortProxy(*args, **kwargs)


# ******************************************************************************************************************** #
class Propertyset(mtxObjAbs.AbsMtxPortset):
    CLS_mtx__name = _mtxObjRaw.Name

    CLS_grh__node__port_stack = _grhObjStack.ObjStack

    # xml ************************************************************************************************************ #
    VAR_dat__xml_obj__element_prefix_str = u'propertyset'
    VAR_dat__xml_obj__attribute_attach_str = u'propertyset'

    def __init__(self, *args):
        """
        :param args: str(geometry dagpath)
        """
        self._initAbsMtxPortset(*args)
