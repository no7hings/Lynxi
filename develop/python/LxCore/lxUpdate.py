# coding=utf-8
from LxCore import lxBasic, lxConfigure
reload(lxBasic)
reload(lxConfigure)
#
none = ''


#
def setUpdate(force=0):
    module = lxConfigure.Lynxi_Module_Python()
    ui = lxConfigure.Ui()

    localVersion = module.localVersion()
    serverVersion = module.localVersion()

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

        module.reloadBasic()
        module.reloadAll()

        module.setLocalRefresh()

        lxTip.viewMessage(
            u'Lynxi Tool(s) Update to',
            u'{}'.format(serverVersion)
        )

