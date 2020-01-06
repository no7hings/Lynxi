# coding:utf-8
from LxBasic import bscCore, bscMethods

from LxCore import lxBasic

from LxScheme import shmConfigure

from LxScheme.shmObjects import _shmPath, _shmResource


class Resource(shmConfigure.Basic):
    def __init__(self):
        self._resource_cls_dic = {
            self.Category_Plf_Language: _shmResource.Rsc_PltLanScheme,
            self.Category_Plf_App_Language: _shmResource.Rsc_PltAppLanScheme
        }
        self._resource = self._getResource()

    @property
    def name(self):
        return lxBasic.getOsEnvironValue(
            self.Environ_Key_Scheme_Name
        )

    @property
    def version(self):
        return lxBasic.getOsEnvironValue(
            self.Environ_Key_Scheme_Version
        )

    @version.setter
    def version(self, versionString):
        lxBasic.setOsEnvironValue(
            self.Environ_Key_Scheme_Version,
            versionString
        )
        bscMethods.PythonMessage().traceResult(
            u'Set Scheme: {} ( {} )'.format(self.name, self.activeVersion)
        )

    @property
    def resource(self):
        return self._resource

    def _getResource(self):
        data = lxBasic.getOsEnvironValue(
            self.Environ_Key_Scheme_System
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

        pythonReload = bscMethods.PythonReloader(modules)
        pythonReload.run()

        bscMethods.If_Message(
            u'Load Scheme: ',
            u'{} ( {} )'.format(self.name, self.activeVersion)
        )


class Interface(object):
    Environ_Key_Message_Count = 'LYNXI_VALUE_MESSAGE_COUNT'
    Environ_Key_Enable_Tooltip_Auto = 'LYNXI_ENABLE_TOOLTIP_AUTO_SHOW'
    def __init__(self):
        pass

    @classmethod
    def restMessageCount(cls):
        lxBasic.setOsEnvironValue(cls.Environ_Key_Message_Count, '0')

    @classmethod
    def setMessageCount(cls, delta):
        value = cls.messageCount()
        #
        value += delta
        #
        lxBasic.setOsEnvironValue(cls.Environ_Key_Message_Count, str(value))
        return value

    @classmethod
    def messageCount(cls):
        data = lxBasic.getOsEnvironValue(cls.Environ_Key_Message_Count)
        if data:
            return int(data)
        return 0

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
        lxBasic.setOsEnvironValue(cls.Environ_Key_Enable_Tooltip_Auto, envValue)

    @classmethod
    def isTooltipAutoShow(cls):
        boolean = False
        envData = lxBasic.getOsEnvironValue(cls.Environ_Key_Enable_Tooltip_Auto)
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
    def preset(self):
        return _shmPath.Pth_PresetRoot()

    @property
    def toolkit(self):
        return _shmPath.Pth_ToolkitRoot()

    @property
    def icon(self):
        return _shmPath.Pth_IconRoot()


class Directory(object):
    def __init__(self):
        pass

    @property
    def toolkit(self):
        return None

    @property
    def icon(self):
        return _shmPath.Pth_IconDirectory()


class UserPreset(object):
    def __init__(self):
        self._userName = bscCore.Basic()._getUserName()
        self._localPathString = u'{}/user/{}'.format(Root().basic.local, self._userName)

    @property
    def renderCommandDirectory(self):
        return u'{}/command/render'.format(self._localPathString)

    @property
    def projectConfigFile(self):
        return u'{}/project/config.json'.format(self._localPathString)

    def applicationProjectConfigFile(self, applicationName, applicationVersion):
        return u'{}/project/{}-{}.config.json'.format(self._localPathString, applicationName, applicationVersion)

    @property
    def uiFilterConfigFile(self):
        return u'{}/ui/filter.config.json'.format(self._localPathString)
