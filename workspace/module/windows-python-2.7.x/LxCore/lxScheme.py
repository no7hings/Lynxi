# coding:utf-8
from LxBasic import bscCore

from LxCore import lxBasic, lxCore_

from LxScheme.shmObjects import _shmPath, _shmResource


class Python(lxCore_.Basic):
    def __init__(self):
        self._resource_cls_dic = {
            self.Category_Plf_Language: _shmResource.Rsc_PltLanScheme,
            self.Category_Plf_App_Language: _shmResource.Rsc_PltAppLanScheme
        }
        self._resource = self._getResource()

    @property
    def name(self):
        return lxBasic.getOsEnvironValue(
            self.Key_Environ_Scheme_Name
        )

    @property
    def version(self):
        return lxBasic.getOsEnvironValue(
            self.Key_Environ_Scheme_Version
        )

    @version.setter
    def version(self, versionString):
        lxBasic.setOsEnvironValue(
            self.Key_Environ_Scheme_Version,
            versionString
        )

    @property
    def resource(self):
        return self._resource

    def _getResource(self):
        data = lxBasic.getOsEnvironValue(
            self.Key_Environ_Scheme_System
        )
        if data:
            systemRaw = eval(data)
            category = systemRaw[self.Key_Category]
            resourceCls = self._resource_cls_dic[category]

            return resourceCls(self.name, systemRaw)

    @property
    def activeVersion(self):
        if self.resource is not None:
            return self.resource.version.active

    def loadActiveModules(self):
        activeOperate = self.resource.operateAt(
            self.activeVersion
        )
        modules = activeOperate.dependentModules()

        pythonReload = bscCore.Py_Reload(modules)
        pythonReload.run()

        bscCore.If_Message(
            u'Load Scheme: ',
            u'{} ( {} )'.format(self.name, self.activeVersion)
        )


class Ui(object):
    Lynxi_Key_Environ_Message_Count = 'LYNXI_MESSAGE_COUNT'
    Lynxi_Key_Environ_Enable_Tooltip_Auto = 'LYNXI_TOOLTIP_AUTO_SHOW'
    def __init__(self):
        pass

    @classmethod
    def restMessageCount(cls):
        lxBasic.setOsEnvironValue(cls.Lynxi_Key_Environ_Message_Count, '0')

    @classmethod
    def setMessageCount(cls, value):
        data = lxBasic.getOsEnvironValue(cls.Lynxi_Key_Environ_Message_Count)
        #
        if data:
            value_ = str(int(data) + value)
        else:
            value_ = str(0)
        #
        lxBasic.setOsEnvironValue(cls.Lynxi_Key_Environ_Message_Count, value_)
        return int(value_)

    @staticmethod
    def closeAll():
        from LxUi.qt import qtCore  # import in Method
        #
        w = qtCore.getAppWindow()
        if w is not None:
            cs = w.children()
            if cs:
                for i in cs:
                    moduleName = i.__class__.__module__
                    if moduleName.startswith('LxInterface.qt') or moduleName.startswith('LxUi.qt'):
                        i.deleteLater()

    @classmethod
    def setTooltipAutoShow(cls, boolean):
        envValue = str(boolean).upper()
        lxBasic.setOsEnvironValue(cls.Lynxi_Key_Environ_Enable_Tooltip_Auto, envValue)

    @classmethod
    def isTooltipAutoShow(cls):
        boolean = False
        envData = lxBasic.getOsEnvironValue(cls.Lynxi_Key_Environ_Enable_Tooltip_Auto)
        if envData:
            if envData == str(True).upper():
                boolean = True
        return boolean


class Root(object):
    def __init__(self):
        pass

    @property
    def basic(self):
        return _shmPath.Pth_Root()

    @property
    def toolkit(self):
        return _shmPath.Pth_ToolkitRoot()

    @property
    def icon(self):
        return _shmPath.Pth_IconRoot()


class File(object):
    def __init__(self):
        self._userName = bscCore.Basic()._getUserName()

    def projectFile(self):
        pass
