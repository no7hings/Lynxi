# coding:utf-8
from LxBasic import bscMethods

from LxGui.qt import qtCommands


def gui_qt__mdf__set_gui_exclusive_show(mtd):
    def subMtd(*args, **kwargs):
        qtCommands.setExistGuiQuit(*args)

        return mtd(*args, **kwargs)

    return subMtd


def gui_qt__mdf__set_app_gui_exclusive_show(fnc):
    def subMtd(*args, **kwargs):
        if bscMethods.MayaApp.isActive():
            from LxMaya import maScheme

            maScheme.Scheme().loadPlugs()

        qtCommands.setExistGuiQuit(*args)

        return fnc(*args, **kwargs)

    return subMtd
