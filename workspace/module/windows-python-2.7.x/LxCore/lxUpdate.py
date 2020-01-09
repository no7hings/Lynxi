# coding=utf-8
from LxBasic import bscCore, bscModifiers

from LxCore import lxScheme
#
none = ''


@bscModifiers.fncCatchCostTime
def setUpdate(force=0):
    schemeLoader = lxScheme.Shm_Resource()

    ui = lxScheme.Shm_Interface()

    localVersion = schemeLoader.version
    serverVersion = schemeLoader.activeVersion

    ui.restMessageCount()

    isUpdate = False

    isDevelop = bscCore.Basic()._isDevelop()

    if isDevelop is True:
        isUpdate = True
    else:
        if localVersion is None or localVersion != serverVersion:
            isUpdate = True

    if force is True or isUpdate is True:
        if isDevelop is False:
            ui.closeAll()

        schemeLoader.loadActiveModules()

        schemeLoader.version = serverVersion

