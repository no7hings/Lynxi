# coding:utf-8
from LxCore import lxBasic, lxConfigure

from LxCore.definition import abstract


class Language(abstract._AbcLanguage):
    def __init__(self, languageName, languageVersion):
        self._initAbcLanguage(languageName, languageVersion)


class Lan_Python(abstract._AbcLanguage):
    Key_Environ_Bin_Path = 'LYNXI_PYTHON_BIN_PATH'
    Bin_Path_Default = r'E:\myworkspace\td\lynxi\bin\python\2.7x64'
    def __init__(self, languageVersion):
        self._initAbcLanguage(self.Language_Python, languageVersion)


class Platform(abstract._AbcPlatform):
    def __init__(self, platformName, platformVersion):
        self._initAbcPlatform(platformName, platformVersion)


class Plf_Windows(abstract._AbcPlatform):
    def __init__(self, platformVersion):
        self._initAbcPlatform(self.Platform_Windows, platformVersion)


class Win_Python(abstract._AbcApplication):
    PLATFORM_CLS = Plf_Windows
    LANGUAGE_CLS = Lan_Python

    def __init__(self, platformVersion, pythonVersion):
        self._initAbcApplication(
            self.Platform_Windows, platformVersion,
            self.Language_Python, pythonVersion,
            self.Language_Python, pythonVersion
        )


class Win_Application(abstract._AbcApplication):
    PLATFORM_CLS = Plf_Windows
    LANGUAGE_CLS = Lan_Python

    def __init__(self, appName, appVersion):
        self._initAbcApplication(
            self.Platform_Windows, self.Version_Share,
            appName, appVersion,
            self.Language_Python, self.Python_Version_27
        )


class Win_Maya(abstract._AbcApplication):
    LANGUAGE_CLS = Lan_Python

    def __init__(self, mayaVersion):
        self._initAbcWindowsMaya(mayaVersion)

    def environFile(self):
        return lxBasic.getMayaAppsEnvFile(self.version())

