# coding=utf-8
from LxBasic import bscCore, bscModifier

from LxCore import lxScheme
#
none = ''


@bscModifier.catchCostTime
def setUpdate(force=0):
    schemeLoader = lxScheme.Resource()

    ui = lxScheme.Interface()

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

