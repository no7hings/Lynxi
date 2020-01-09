# coding:utf-8
from LxBasic import bscMethods

from LxUi.qt import qtCommands


def showInterfaceExclusive(mtd):
    def subMtd(*args, **kwargs):
        from LxCore import lxUpdate
        lxUpdate.setUpdate()

        qtCommands.setExistInterfaceQuit(*args)

        return mtd(*args, **kwargs)
    return subMtd


def showAppInterfaceExclusive(mtd):
    def subMtd(*args, **kwargs):
        from LxCore import lxUpdate
        lxUpdate.setUpdate()

        application = bscMethods.PythonApplication()
        if application.isMaya:
            from LxMaya import maScheme

            maScheme.Shm_Resource().loadPlugs()

        qtCommands.setExistInterfaceQuit(*args)

        return mtd(*args, **kwargs)

    return subMtd
