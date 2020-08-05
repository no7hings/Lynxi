# coding:utf-8
from .. import grhObjAbs


# ******************************************************************************************************************** #
class PortQueryrawStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.portpath


class NodeQueryrawStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.typepath


# ******************************************************************************************************************** #
class PortQueryStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.portpath


class NodeQueryStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.typepath


# ******************************************************************************************************************** #
class TrsPortQueryrawStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.source_portpath


class TrsNodeQueryrawStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.source_typepath


# ******************************************************************************************************************** #
class TrsPortQueryStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.source_portpath


class TrsNodeQueryStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.source_typepath


# ******************************************************************************************************************** #
class VariantObjStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.variantString()


class PortStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.portpathString()


class PortStackSite(grhObjAbs.Abs_GrhObjStackSite):
    CLS_grh__variant_set__obj_stack = PortStack

    def __init__(self, *args):
        self._initAbsGrhObjStackSite(*args)


class NodeStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.pathString()


# ******************************************************************************************************************** #
class TrsPortStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.srcPort().pathString()


class TrsNodeStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.srcNode().pathString()


# ******************************************************************************************************************** #
class ObjProxyStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.namespaceString()


class PortProxyStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.bindObject().portpathString()


class NodeGraphOtportProxyStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.bindPathString()


class CacheObjStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.pathString()


class CacheTrsObjStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.srcNode().pathString()


class ObjStack(grhObjAbs.Abs_GrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.nameString()