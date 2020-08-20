# coding:utf-8
from LxBasic import bscObjAbs, bscObjects

from .. import appCfg, appObjAbs


class AppToolStack(appObjAbs.AbsAppObjStack):
    def __init__(self, *args):
        self._initAbsAppObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.path


class AppTagObj(bscObjAbs.AbsBscNode):
    CLS_bsc__node__port = bscObjects.Port
    CLS_bsc__node__port_stack = bscObjects.ObjStack

    VAR_bsc__node__port_default_dict = appCfg.AppUtility.DEF_app__tag__property_default_dict

    def __init__(self, *args, **kwargs):
        self._initAbsBscNode(*args, **kwargs)


class AppTagTree(bscObjAbs.AbsBscDagTree):
    CLS_bsc__node_tree__node = AppTagObj
    CLS_bsc__node_tree__node_stack = bscObjects.ObjStack

    def __init__(self, *args):
        self._initAbsBscDagTree(*args)
