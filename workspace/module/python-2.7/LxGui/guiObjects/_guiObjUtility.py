# coding:utf-8
from LxBasic import bscObjAbs

from LxScheme import shmCfg

from .. import guiObjAbs


class GuiIconStack(bscObjAbs.AbsBscObjStack):
    def __init__(self, *args):
        self._initAbsBscObjStack(*args)

    def _obj_stack__get_obj_key_str_(self, obj):
        return obj.key


class GuiIcon(guiObjAbs.AbsGuiIcon):
    def __init__(self, *args):
        self._initAbsGuiIcon(*args)


class GuiIconLoader(guiObjAbs.AbsGuiIconLoader):
    CLS_gui__icon_loader__icon = GuiIcon
    CLS_gui__icon_loader__icon_stack = GuiIconStack

    VAR_gui__icon_loader__environ_key = shmCfg.ShmUtility.DEF_util__environ_key__paths_source
    def __init__(self, *args):
        self._initAbsGuiIconLoader(*args)
