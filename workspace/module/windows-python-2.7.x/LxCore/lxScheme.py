# coding:utf-8
from LxBasic import bscCore, bscObjects, bscMethods

from LxScheme import shmCore

from LxScheme.shmObjects import _shmPath


class Shm_Resource(shmCore.Basic):
    def __init__(self):
        self._initResource()

    def _initResource(self):
        configRaw = bscObjects.JsonFile(self.configFile).read()
        if configRaw:
            self._activeVersion = configRaw[self.Key_Version][self.Key_Active]
        else:
            self._activeVersion = '0.0.0'

        setupRaw = bscObjects.JsonFile(self.setupFile).read()
        if setupRaw:
            self._moduleNames = setupRaw[self.Key_Module]
        else:
            self._moduleNames = []

    @property
    def name(self):
        return self.method_environ.get(
            self.Environ_Key_Name_Scheme
        )

    @property
    def version(self):
        return self.method_environ.get(
            self.Environ_Key_Version_Scheme
        )

    @version.setter
    def version(self, versionString):
        self.method_environ.get(
            self.Environ_Key_Version_Scheme,
            versionString
        )
        bscMethods.PythonMessage().traceResult(
            u'Set Scheme: {} ( {} )'.format(self.name, self.activeVersion)
        )

    @property
    def configFile(self):
        return self.method_environ.get(
            self.Environ_Key_Config_File_Scheme
        )

    @property
    def setupFile(self):
        return self.method_environ.get(
            self.Environ_Key_File_Scheme
        )

    @property
    def moduleNames(self):
        return self._moduleNames

    @property
    def activeVersion(self):
        return self._activeVersion

    def loadActiveModules(self):
        pythonReload = bscMethods.PythonReloader(self.moduleNames)
        pythonReload.run()

        bscMethods.If_Message(
            u'Load Scheme: ',
            u'{} ( {} )'.format(self.name, self.activeVersion)
        )


class Shm_Interface(shmCore.Basic):
    Environ_Key_Message_Count = 'LYNXI_VALUE_MESSAGE_COUNT'
    Environ_Key_Enable_Tooltip_Auto = 'LYNXI_ENABLE_TOOLTIP_AUTO_SHOW'
    def __init__(self):
        pass

    @classmethod
    def restMessageCount(cls):
        cls.method_environ.set(cls.Environ_Key_Message_Count, '0')

    @classmethod
    def setMessageCount(cls, delta):
        value = cls.messageCount()
        #
        value += delta
        #
        cls.method_environ.set(cls.Environ_Key_Message_Count, str(value))
        return value

    @classmethod
    def messageCount(cls):
        data = cls.method_environ.get(cls.Environ_Key_Message_Count)
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
        cls.method_environ.set(cls.Environ_Key_Enable_Tooltip_Auto, envValue)

    @classmethod
    def isTooltipAutoShow(cls):
        boolean = False
        envData = cls.method_environ.get(cls.Environ_Key_Enable_Tooltip_Auto)
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
