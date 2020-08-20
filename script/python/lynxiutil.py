# coding:utf-8
import platform

import sys

import os

import json

import time

import types

import getpass


class LxUtilBasic(object):
    MOD_platform = platform
    MOD_getpass = getpass

    DEF_util__environ_key__path = u'LYNXI_PATH'
    DEF_util__root__default = u'e:/myworkspace/td/lynxi' if MOD_platform.system() == u'Windows' else u'/data/e/myworkspace/td/lynxi'

    DEF_util__environ_key__scheme_var = u'LYNXI_SCHEME_VAR'

    DEF_util__environ_key__path_develop = u'LYNXI_PATH_DEVELOP'
    DEF_util__root__default_develop = u'e:/myworkspace/td/lynxi' if MOD_platform.system() == u'Windows' else u'/data/e/myworkspace/td/lynxi'

    DEF_util__environ_key__path_product = u'LYNXI_PATH_PRODUCT'
    DEF_util__root__default_product = u'e:/myworkspace/td/lynxi' if MOD_platform.system() == u'Windows' else u'/data/e/myworkspace/td/lynxi'

    DEF_util__environ_key__path_local = u'LYNXI_PATH_LOCAL'
    DEF_util__root__default_local = u'c:/.lynxi' if MOD_platform.system() == u'Windows' else u'/linux_home/{}'.format(MOD_getpass.getuser())

    DEF_util__environ_key__path_kit = u'LYNXI_PATH_KIT'
    DEF_util__environ_key__path_appkit = u'LYNXI_PATH_APPKIT'
    DEF_util__environ_key__path_toolkit = u'LYNXI_PATH_TOOLKIT'

    DEF_util__environ_key__paths_source = u'LYNXI_PATHS_SOURCE'

    DEF_util__environ_key__name_scheme = u'LYNXI_NAME_SCHEME'
    environ_key_version_scheme = u'LYNXI_VERSION_SCHEME'
    environ_key_file_scheme = u'LYNXI_SETUP_FILE_SCHEME'
    environ_key_config_file_scheme = u'LYNXI_CONFIG_FILE_SCHEME'

    DEF_util__environ_key__enable_develop = u'LYNXI_ENABLE_DEVELOP'
    enable_default_develop = u'FALSE'
    DEF_util__environ_key__enable_trace = u'LYNXI_ENABLE_TRACE'
    enable_default_trace = u'FALSE'

    DEF_util__folder__resource = u'resource'
    DEF_util__folder__workspace = u'workspace'

    DEF_util__folder__scheme = u'scheme'

    DEF_sep = os.sep
    DEF_path_sep = os.pathsep

    @classmethod
    def _isDevelop(cls):
        return [False, True][os.environ.get(cls.DEF_util__environ_key__enable_develop, cls.enable_default_develop).lower() == 'true']

    @classmethod
    def isTraceEnable(cls):
        return [False, True][os.environ.get(cls.DEF_util__environ_key__enable_trace, cls.enable_default_trace).lower() == 'true']


class LxSetupMethod(LxUtilBasic):
    platform_dic = {
        'Windows': 'windows',
        'Linux': 'linux'
    }
    application_dic = {
        'maya.exe': 'maya',
        'maya': 'maya'
    }

    @classmethod
    def getPlatform(cls):
        return cls.platform_dic.get(platform.system())

    @classmethod
    def getApplication(cls):
        return cls.application_dic.get(os.path.basename(sys.argv[0]))

    @classmethod
    def getLanguage(cls):
        return 'python', platform.python_version()

    @staticmethod
    def _getActivePrettifyTime():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    @classmethod
    def trace(cls, text):
        if LxUtilBasic.isTraceEnable():
            print u'        |{}'.format(cls._getActivePrettifyTime())
            print u'{}'.format(text)

    @classmethod
    def traceResult(cls, text):
        cls.trace(
            u''' result |{}'''.format(text)
        )

    @classmethod
    def traceWarning(cls, text):
        cls.trace(
            u'''warning |{}'''.format(text)
        )

    @classmethod
    def traceError(cls, text):
        cls.trace(
            u''' error |{}'''.format(text)
        )

    @classmethod
    def setEnvironAppend(cls, key, value):
        lowerKeys = [i.lower() for i in os.environ.keys()]
        if key.lower() in lowerKeys:
            lowerLis = [i.lower() for i in os.environ[key].split(cls.DEF_path_sep)]
            if value.lower() not in lowerLis:
                os.environ[key] += cls.DEF_path_sep + value
                cls.traceResult(
                    u'append environ "{}": "{}"'.format(key, value)
                )
            else:
                cls.traceWarning(
                    u'''exist environ "{}": "{}"'''.format(key, value)
                )
        else:
            os.environ[key] = str(value)
            cls.traceResult(
                u'add environ "{}": "{}"'.format(key, value)
            )

    @classmethod
    def setEnvironPrepend(cls, key, value):
        lowerKeys = [i.lower() for i in os.environ.keys()]
        if key.lower() in lowerKeys:
            lowerLis = [i.lower() for i in os.environ[key].split(cls.DEF_path_sep)]
            if value.lower() not in lowerLis:
                _ = os.environ[key]
                os.environ[key] = value + cls.DEF_path_sep + _
                cls.traceResult(
                    u'prepend environ "{}": "{}"'.format(key, value)
                )
            else:
                cls.traceWarning(
                    u'''exist environ "{}": "{}"'''.format(key, value)
                )
        else:
            os.environ[key] = str(value)
            cls.traceResult(
                u'add environ "{}": "{}"'.format(key, value)
            )

    @classmethod
    def setEnvironOverride(cls, key, value):
        lowerKeys = [i.lower() for i in os.environ.keys()]
        if key.lower() in lowerKeys:
            lowerValue = os.environ[key].lower()
            if value.lower() != lowerValue:
                os.environ[key] = value
                cls.traceResult(
                    u'override environ "{}": "{}"'.format(key, value)
                )
            else:
                cls.traceWarning(
                    u'''exist environ "{}": "{}"'''.format(key, value)
                )
        else:
            os.environ[key] = str(value)
            cls.traceResult(
                u'add environ "{}": "{}"'.format(key, value)
            )

    @classmethod
    def setPythonModuleAdd(cls, key, value):
        if os.path.exists(value):
            lowerLis = [i.lower() for i in sys.path]
            if value.lower() not in lowerLis:
                if cls.getPythonModuleExist(key) is False:
                    sys.path.insert(0, value)
                    cls.traceResult(
                        u'add python module: "{}"'.format(key)
                    )
                    cls.traceResult(
                        u'append python path : "{}"'.format(value)
                    )
                else:
                    cls.traceWarning(
                        u'''exist python module: "{}"'''.format(key)
                    )
            else:
                cls.traceWarning(
                    u'''exist python path: "{}"'''.format(value)
                )
        else:
            cls.traceWarning(
                u'''non-exist path: "{}"'''.format(value)
            )

    @classmethod
    def getPythonModuleExist(cls, moduleNameStr):
        if moduleNameStr in sys.modules:
            module = sys.modules[moduleNameStr]
            if isinstance(module, types.ModuleType):
                if getattr(module, u'__path__', None) is not None:
                    return True
        return False

    @staticmethod
    def readOsJsonFile(fileString):
        if os.path.exists(fileString):
            with open(fileString) as j:
                data = json.load(j)
                return data


class LxRoot(LxUtilBasic):
    basic_method = LxSetupMethod

    @property
    def basic(self):
        return os.environ.get(
            self.DEF_util__environ_key__path,
            self.DEF_util__root__default_develop
        ).replace(u'\\', self.DEF_sep)

    @property
    def active(self):
        return self.server

    @property
    def server(self):
        if LxUtilBasic()._isDevelop():
            return self.develop
        return self.product

    @property
    def develop(self):
        return os.environ.get(
            self.DEF_util__environ_key__path_develop,
            self.DEF_util__root__default_develop
        ).replace(u'\\', self.DEF_sep)

    @property
    def product(self):
        return os.environ.get(
            self.DEF_util__environ_key__path_product,
            self.DEF_util__root__default_product
        ).replace(u'\\', self.DEF_sep)

    @property
    def local(self):
        return os.environ.get(
            self.DEF_util__environ_key__path_local,
            self.DEF_util__root__default_local
        ).replace(u'\\', self.DEF_sep)


class LxSchemeBasic(LxUtilBasic):
    VAR_util__shm__subpath = None

    def _initAbsLxSchemeBasic(self, schemeNameStr, schemeVersionStr):
        method = LxSetupMethod()

        self._schemeNameStr = schemeNameStr
        if self._isDevelop():
            self._schemePathStr = u'{}/{}/{}/{}-{}'.format(
                LxRoot().server,
                self.DEF_util__folder__resource,
                self.DEF_util__folder__scheme,
                self.VAR_util__shm__subpath,
                schemeNameStr
            )
        else:
            self._schemePathStr = u'{}/{}/{}/{}-{}'.format(
                LxRoot().server,
                self.DEF_util__folder__resource,
                self.DEF_util__folder__scheme,
                self.VAR_util__shm__subpath,
                schemeNameStr
            )
        if schemeVersionStr == u'active':
            self._schemeVersionStr = self._getCurrentVersion()
        else:
            self._schemeVersionStr = schemeVersionStr

        method.setEnvironOverride(
            self.DEF_util__environ_key__name_scheme, self.name
        )
        method.setEnvironOverride(
            self.environ_key_version_scheme, self.version
        )
        method.setEnvironOverride(
            self.environ_key_config_file_scheme, self.config_file
        )
        method.setEnvironOverride(
            self.environ_key_file_scheme, self.setup_file
        )

    def _getCurrentVersion(self):
        data = LxSetupMethod.readOsJsonFile(self.config_file)
        if data:
            return unicode(data[u'version'][u'active'])

    @staticmethod
    def _formatDic():
        return {
            'root': LxRoot()
        }

    @classmethod
    def _lx_scheme_setup__set_environ_value_covert_(cls, value):
        if not value.startswith(u'#'):
            resourceNameStr, environValueStr = value.split(u'>')
            environValueStr = environValueStr.rstrip().lstrip().format(
                **cls._formatDic()
            )

            if u'|' in environValueStr:
                if LxUtilBasic()._isDevelop():
                    return resourceNameStr[1:], environValueStr.split(u'|')[0]
                return resourceNameStr[1:], environValueStr.split(u'|')[1]
            return resourceNameStr[1:], environValueStr

    def _lx_scheme_setup__set_environ_add_(self, environDic):
        def subFnc_(environKeyStr_, environValueArgs_, environOperateStr_):
            if environValueArgs_ is not None:
                _resourceNameStr, _environValueStr = environValueArgs_
                if environKeyStr_ == u'LYNXI_PYTHONPATH':
                    LxSetupMethod.setPythonModuleAdd(_resourceNameStr, _environValueStr)
                else:
                    if environOperateStr_ == u'+':
                        LxSetupMethod.setEnvironAppend(environKeyStr_, _environValueStr)
                    elif environOperateStr_ == u';&':
                        LxSetupMethod.setEnvironPrepend(environKeyStr_, _environValueStr)
                    elif environOperateStr_ == u'=':
                        LxSetupMethod.setEnvironOverride(environKeyStr_, _environValueStr)

        def main():
            for k, v in environDic.items():
                operate = v[u'operate']
                value = v[u'value']
                if isinstance(value, (tuple, list)):
                    [subFnc_(k, self._lx_scheme_setup__set_environ_value_covert_(i), operate) for i in value]
                else:
                    subFnc_(k, self._lx_scheme_setup__set_environ_value_covert_(value), operate)

        main()

    @property
    def name(self):
        return self._schemeNameStr

    @property
    def version(self):
        return self._schemeVersionStr

    @property
    def config_file(self):
        return u'{}/config.json'.format(
            self._schemePathStr
        )

    @property
    def setup_file(self):
        return u'{}/{}/source/{}/setup.json'.format(
            self._schemePathStr,
            self._schemeVersionStr,
            self.name
        )

    def environSetup(self):
        fileString = self.setup_file
        if os.path.exists(fileString):
            with open(fileString) as j:
                datumDic = json.load(j) or {}
                environDic = datumDic.get(u'environ')
                if environDic:
                    self._lx_scheme_setup__set_environ_add_(environDic)

    def setup(self):
        LxSetupMethod.traceResult(
            u'Start Setup Scheme "{}": "{}"'.format(self.name, self.version)
        )
        self.environSetup()
        LxSetupMethod.traceResult(
            u'Complete Setup Scheme "{}": "{}"'.format(self.name, self.version)
        )


# windows
class LxWindowsScheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'windows'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)


# linux
class LxLinux64Scheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'linux-x64'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)


# maya
class LxWindowsMayaScheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'windows-maya'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)


class LxLinuxMayaScheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'linux-maya'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)


class LxLinux64MayaScheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'linux-x64-maya'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)


# maya_2019
class LxWindowsMaya2019Scheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'windows-maya-2019'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)


# houdini-python_27
class LxWindowsHoudiniScheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'windows-houdini'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)


class LxWindowsHoudini18Scheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'windows-houdini-18'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)


class LxLinux64Houdini18Scheme(LxSchemeBasic):
    VAR_util__shm__subpath = u'linux-x64-houdini-18'

    def __init__(self, schemeNameStr, schemeVersionStr):
        self._initAbsLxSchemeBasic(schemeNameStr, schemeVersionStr)
