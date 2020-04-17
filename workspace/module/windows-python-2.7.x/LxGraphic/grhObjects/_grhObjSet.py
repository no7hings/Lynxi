# coding:utf-8
from ..import grhObjAbs


class PortQuerySet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.portpath


class NodeQuerySet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.category


class TrsPortQuerySet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.source_portpath


class TrsNodeQuerySet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.source_category


class PortSet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.portpathString()


class PortProxySet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.port().attrpathString()


class NodeSet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.nodepathString()


class CacheObjSet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.pathString()


class CacheTrsObjSet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.tgtNode().nodepathString()


class ObjSet(grhObjAbs.Abs_GrhObjSet):
    def __init__(self, *args):
        self._initAbsGrhObjSet(*args)

    def _get_object_key_string_(self, obj):
        return obj.nameString()
