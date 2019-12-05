# coding=utf-8
from LxCore import lxBasic, lxConfigure
reload(lxBasic)
reload(lxConfigure)
#
none = ''


#
def setUpdate(force=0):
    version = lxConfigure.PythonVersion()
    ui = lxConfigure.Ui()

    localVersion = version.local()
    serverVersion = version.server()

    ui.restMessageCount()

    isUpdate = False

    isDevelop = lxConfigure.Basic().isDevelop()

    if isDevelop is True:
        isUpdate = True
    else:
        if localVersion is None or localVersion != serverVersion:
            isUpdate = True

    if force is True or isUpdate is True:
        from LxCore import lxTip

        if isDevelop is False:
            ui.closeAll()

        modulePython = lxConfigure.ModulePython()
        modulePython.reloadBasic()
        modulePython.reloadAll()

        version.setLocalRefresh()

        lxTip.viewMessage(
            u'Lynxi Tool(s) Update to',
            u'{}'.format(serverVersion)
        )

