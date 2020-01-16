# coding:utf-8
from LxBasic import bscObjects

from LxUi.qt import qtCommands


def mtdInterfaceShowExclusive(mtd):
    def subMtd(*args, **kwargs):
        from LxCore import lxScheme
        lxScheme.Shm_Resource().loadActive()

        qtCommands.setExistInterfaceQuit(*args)

        return mtd(*args, **kwargs)

    return subMtd


def mtdAppInterfaceShowExclusive(mtd):
    def subMtd(*args, **kwargs):
        from LxCore import lxScheme
        lxScheme.Shm_Resource().loadActive()

        system = bscObjects.System()
        if system.isMaya:
            from LxMaya import maScheme

            maScheme.Shm_Resource().loadPlugs()

        qtCommands.setExistInterfaceQuit(*args)

        return mtd(*args, **kwargs)

    return subMtd
