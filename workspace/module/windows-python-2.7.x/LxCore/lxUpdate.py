# coding=utf-8
from LxCore import lxCore_, lxScheme
#
none = ''


#
def setUpdate(force=0):
    schemeLoader = lxScheme.Python()

    ui = lxScheme.Ui()

    localVersion = schemeLoader.version
    serverVersion = schemeLoader.activeVersion

    ui.restMessageCount()

    isUpdate = False

    isDevelop = lxCore_.Basic().isDevelop()

    if isDevelop is True:
        isUpdate = True
    else:
        if localVersion is None or localVersion != serverVersion:
            isUpdate = True

    if force is True or isUpdate is True:
        if isDevelop is False:
            ui.closeAll()

        # module.reloadBasic()
        schemeLoader.loadActiveModules()

        schemeLoader.version = serverVersion

