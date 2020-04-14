# coding:utf-8
from LxBasic import bscMtdCore, bscObjects, bscMethods

from LxScheme import shmConfigure

from LxScheme.shmObjects import _shmObjPath


class Resource(shmConfigure.Utility):
    def __init__(self):
        self._initResource()

    def _initResource(self):
        configRaw = bscObjects.OsJsonFile(self.configFile).read()
        if configRaw:
            self._activeVersion = configRaw[self.Key_Version][self.Key_Active]
        else:
            self._activeVersion = '0.0.0'

        setupRaw = bscObjects.OsJsonFile(self.setupFile).read()
        if setupRaw:
            self._moduleNames = setupRaw[self.Key_Module]
        else:
            self._moduleNames = []

    @property
    def name(self):
        return bscMethods.OsEnviron.get(
            self.Environ_Key_Name_Scheme
        )

    @property
    def version(self):
        return bscMethods.OsEnviron.get(
            self.Environ_Key_Version_Scheme
        )

    @version.setter
    def version(self, versionString):
        bscMethods.OsEnviron.get(
            self.Environ_Key_Version_Scheme,
            versionString
        )
        bscMethods.PyMessage.traceResult(
            u'Set Scheme: {} ( {} )'.format(self.name, self.activeVersion)
        )

    @property
    def configFile(self):
        return bscMethods.OsEnviron.get(
            self.Environ_Key_Config_File_Scheme
        )

    @property
    def setupFile(self):
        return bscMethods.OsEnviron.get(
            self.Environ_Key_File_Scheme
        )

    @property
    def moduleNames(self):
        return self._moduleNames

    @property
    def activeVersion(self):
        return self._activeVersion

    def loadActiveModules(self):
        bscMethods.PyReloader.reload(self.moduleNames)

    def loadActive(self, force=False):
        ui = Gui()
        ui.restMessageCount()

        localVersion = self.version
        serverVersion = self.activeVersion

        isUpdate = False

        isDevelop = self.isDevelop()

        if isDevelop is True:
            isUpdate = True
        else:
            if localVersion is None or localVersion != serverVersion:
                isUpdate = True

        if force is True or isUpdate is True:
            if isDevelop is False:
                ui.closeAll()

            self.loadActiveModules()

            self.version = serverVersion


class Gui(shmConfigure.Utility):
    Environ_Key_Message_Count = 'LYNXI_VALUE_MESSAGE_COUNT'
    Environ_Key_Enable_Tooltip_Auto = 'LYNXI_ENABLE_TOOLTIP_AUTO_SHOW'

    def __init__(self):
        pass

    @classmethod
    def restMessageCount(cls):
        bscMethods.OsEnviron.set(cls.Environ_Key_Message_Count, '0')

    @classmethod
    def setMessageCount(cls, delta):
        value = cls.messageCount()
        #
        value += delta
        #
        bscMethods.OsEnviron.set(cls.Environ_Key_Message_Count, str(value))
        return value

    @classmethod
    def messageCount(cls):
        data = bscMethods.OsEnviron.get(cls.Environ_Key_Message_Count)
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
        bscMethods.OsEnviron.set(cls.Environ_Key_Enable_Tooltip_Auto, envValue)

    @classmethod
    def isTooltipAutoShow(cls):
        boolean = False
        envData = bscMethods.OsEnviron.get(cls.Environ_Key_Enable_Tooltip_Auto)
        if envData:
            if envData == str(True).upper():
                boolean = True
        return boolean


class Root(object):
    def __init__(self):
        pass

    @property
    def basic(self):
        return _shmObjPath.Pth_Root()

    @property
    def preset(self):
        return _shmObjPath.Pth_PresetRoot()

    @property
    def toolkit(self):
        return _shmObjPath.Pth_ToolkitRoot()

    @property
    def icon(self):
        return _shmObjPath.Pth_IconRoot()


class Directory(object):
    def __init__(self):
        pass

    @property
    def toolkit(self):
        return None

    @property
    def icon(self):
        return _shmObjPath.Pth_IconDirectory()


class UserPreset(object):
    def __init__(self):
        self._userName = bscMtdCore.Mtd_BscUtility()._getSystemUsername()
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

    def tagFilterConfigFile(self, unitName):
        return u'{}/ui/tag/{}-filter.config.json'.format(self._localPathString, unitName)
