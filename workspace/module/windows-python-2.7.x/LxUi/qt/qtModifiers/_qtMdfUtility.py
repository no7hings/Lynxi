# coding:utf-8
from LxBasic import bscCore, bscObjects

from LxUi.qt import qtCommands


def mtdInterfaceShowExclusive(mtd):
    def subMtd(*args, **kwargs):
        from LxScheme import shmOutput
        shmOutput.Resource().loadActive()

        qtCommands.setExistInterfaceQuit(*args)

        return mtd(*args, **kwargs)

    return subMtd


def mtdAppInterfaceShowExclusive(mtd):
    def subMtd(*args, **kwargs):
        from LxScheme import shmOutput
        shmOutput.Resource().loadActive()

        system = bscObjects.System()
        if system.isMaya:
            from LxMaya import maScheme

            maScheme.Resource().loadPlugs()

        qtCommands.setExistInterfaceQuit(*args)

        return mtd(*args, **kwargs)

    return subMtd
