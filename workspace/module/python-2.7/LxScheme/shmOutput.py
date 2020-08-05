# coding:utf-8
from LxBasic import bscMtdCore, bscObjects, bscMethods

from LxScheme import shmCfg

from LxScheme.shmObjects import _shmObjPath


class Scheme(shmCfg.ShmUtility):
    def __init__(self):
        self._initScheme()

    def _initScheme(self):
        configRaw = bscObjects.OsJsonFile(self.config_file).read()
        if configRaw:
            self._activeVersion = configRaw[self.DEF_shm__key__version][self.Key_Active]
        else:
            self._activeVersion = '0.0.0'

        setupRaw = bscObjects.OsJsonFile(self.setup_file).read()
        if setupRaw:
            self._moduleNameStrList = setupRaw[self.Key_Module]
        else:
            self._moduleNameStrList = []

    @property
    def name(self):
        return bscMethods.OsEnviron.get(
            self.DEF_util__environ_key__name_scheme
        )

    @property
    def version(self):
        return bscMethods.OsEnviron.get(
            self.Environ_KeyVAR_kit__window__version_Scheme
        )

    @version.setter
    def version(self, versionString):
        bscMethods.OsEnviron.get(
            self.Environ_KeyVAR_kit__window__version_Scheme,
            versionString
        )
        bscMethods.PyMessage.traceResult(
            u'Set Scheme: {} ( {} )'.format(self.name, self.activeVersion)
        )

    @property
    def config_file(self):
        return bscMethods.OsEnviron.get(
            self.Environ_Key_Config_File_Scheme
        )

    @property
    def setup_file(self):
        return bscMethods.OsEnviron.get(
            self.Environ_Key_File_Scheme
        )

    @property
    def module_names(self):
        return self._moduleNameStrList

    @property
    def activeVersion(self):
        return self._activeVersion

    def loadActiveModules(self):
        bscMethods.PyReloader.reload(self.module_names)

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

    def toString(self):
        return self.__str__()

    def __str__(self):
        return u'{}-{}'.format(self.name, self.version)


class Gui(shmCfg.ShmUtility):
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
        from LxGui.qt import qtCore  # import in Method
        #
        w = qtCore.getAppWindow()
        if w is not None:
            cs = w.children()
            if cs:
                for i in cs:
                    moduleName = i.__class__.__module__
                    if moduleName.startswith('LxKit.qt') or moduleName.startswith('LxGui.qt'):
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
    def kit(self):
        return _shmObjPath.Pth_KitRoot()

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
