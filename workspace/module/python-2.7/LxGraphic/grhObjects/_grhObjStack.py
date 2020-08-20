# coding:utf-8
from .. import grhObjAbs


# ******************************************************************************************************************** #
class PortQueryrawStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.portpath


class NodeQueryrawStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.typepath


# ******************************************************************************************************************** #
class PortQueryStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.portpath


class NodeQueryStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.typepath


# ******************************************************************************************************************** #
class TrsPortQueryrawStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.source_portpath


class TrsNodeQueryrawStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.source_typepath


# ******************************************************************************************************************** #
class TrsPortQueryStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.source_portpath


class TrsNodeQueryStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.source_typepath


# ******************************************************************************************************************** #
class VariantObjStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.variantString()


class PortStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.portpathString()


class PortStackSite(grhObjAbs.AbsGrhObjStackSite):
    CLS_grh__variant_set__obj_stack = PortStack

    def __init__(self, *args):
        self._initAbsGrhObjStackSite(*args)


class NodeStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.pathString()


# ******************************************************************************************************************** #
class TrsPortStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.srcPort().pathString()


class TrsNodeStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.srcNode().pathString()


# ******************************************************************************************************************** #
class ObjProxyStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.namespaceString()


class PortProxyStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.bindObject().portpathString()


class NodeGraphOtportProxyStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.bindPathString()


class CacheObjStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.pathString()


class CacheTrsObjStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.srcNode().pathString()


class ObjStack(grhObjAbs.AbsGrhObjStack):
    def __init__(self, *args):
        self._initAbsGrhObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.nameString()