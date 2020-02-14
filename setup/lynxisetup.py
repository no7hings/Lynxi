# coding:utf-8
import platform

import sys

import os

import json

import time


class Basic(object):
    DEF_key_environ_path_develop = 'LYNXI_PATH_DEVELOP'
    VAR_path_default_develop = 'e:/myworkspace/td/lynxi'

    DEF_key_environ_path_product = 'LYNXI_PATH_PRODUCT'
    VAR_path_default_product = 'e:/myworkspace/td/lynxi'

    DEF_key_environ_path_local = 'LYNXI_PATH_LOCAL'
    VAR_path_default_local = 'c:/.lynxi'

    DEF_key_environ_path_toolkit = 'LYNXI_PATH_TOOLKIT'

    environ_key_name_scheme = 'LYNXI_NAME_SCHEME'
    environ_key_version_scheme = 'LYNXI_VERSION_SCHEME'
    environ_key_file_scheme = 'LYNXI_FILE_SCHEME'
    environ_key_config_file_scheme = 'LYNXI_CONFIG_FILE_SCHEME'

    DEF_key_environ_enable_develop = 'LYNXI_ENABLE_DEVELOP'
    DEF_key_environ_enable_trace = 'LYNXI_ENABLE_TRACE'

    enable_default_develop = 'FALSE'

    @classmethod
    def _isDevelop(cls):
        return [False, True][os.environ.get(cls.DEF_key_environ_enable_develop, cls.enable_default_develop).lower() == 'true']

    @classmethod
    def isTraceEnable(cls):
        return [False, True][os.environ.get(cls.DEF_key_environ_enable_trace, cls.enable_default_develop).lower() == 'true']


class Method(object):
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
    def _getOsActiveViewTime():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    @classmethod
    def traceMessage(cls, text):
        if Basic.isTraceEnable():
            print u'@lynxi <{}>'.format(cls._getOsActiveViewTime())
            print u'    {}'.format(text)

    @classmethod
    def traceResult(cls, text):
        cls.traceMessage(
            u'''@result {}'''.format(text)
        )

    @classmethod
    def traceWarning(cls, text):
        cls.traceMessage(
            u'''@warning {}'''.format(text)
        )

    @classmethod
    def traceError(cls, text):
        cls.traceMessage(
            u'''@error {}'''.format(text)
        )

    @classmethod
    def addEnviron(cls, key, value):
        lowerKeys = [i.lower() for i in os.environ.keys()]
        if key.lower() in lowerKeys:
            lowerLis = [i.lower() for i in os.environ[key].split(os.pathsep)]
            if value.lower() not in lowerLis:
                os.environ[key] += os.pathsep + value
                cls.traceResult(
                    u'Add Environ "{}": "{}"'.format(key, value)
                )
        else:
            os.environ[key.upper()] = str(value)
            cls.traceResult(
                u'Set Environ "{}": "{}"'.format(key, value)
            )

    @classmethod
    def setEnviron(cls, key, value):
        lowerKeys = [i.lower() for i in os.environ.keys()]
        if key.lower() in lowerKeys:
            lowerValue = os.environ[key].lower()
            if value.lower() != lowerValue:
                os.environ[key] = value
                cls.traceResult(
                    u'Override Environ "{}": "{}"'.format(key, value)
                )
        else:
            os.environ[key.upper()] = str(value)
            cls.traceResult(
                u'Set Environ "{}": "{}"'.format(key, value)
            )

    @classmethod
    def addPythonPath(cls, value):
        lowerLis = [i.lower() for i in sys.path]
        if value.lower() not in lowerLis:
            sys.path.insert(0, value)
            cls.traceResult(
                u'Add Python Path: "{}"'.format(value)
            )

    @staticmethod
    def readOsJsonFile(fileString):
        if os.path.exists(fileString):
            with open(fileString) as j:
                data = json.load(j)
                return data


class Root(Basic):
    def_path = u'e:/myworkspace/td/lynxi'
    def_local_path = u'c:/.lynxi'
    def_develop_path = u'e:/myworkspace/td/lynxi'

    basic_method = Method

    @property
    def active(self):
        return self.server

    @property
    def server(self):
        if Basic()._isDevelop():
            return self.develop
        return self.product

    @property
    def develop(self):
        return os.environ.get(
            self.DEF_key_environ_path_develop,
            self.VAR_path_default_develop
        ).replace('\\', '/')

    @property
    def product(self):
        return os.environ.get(
            self.DEF_key_environ_path_product,
            self.VAR_path_default_product
        ).replace('\\', '/')

    @property
    def local(self):
        return os.environ.get(
            self.DEF_key_environ_path_local,
            self.VAR_path_default_local
        ).replace('\\', '/')


class Abc_Scheme(Basic):
    scheme_subpath_string = None

    def _initAbcScheme(self, schemeName, schemeVersion):
        method = Method()

        self._schemeName = schemeName

        self.schemePathString = u'{}/{}-{}'.format(
            Root().server, self.scheme_subpath_string, schemeName
        )

        if schemeVersion == u'active':
            self._schemeVersion = self._getCurrentVersion()
        else:
            self._schemeVersion = schemeVersion

        self._systemRaw = self._getSystemRaw()

        method.setEnviron(
            self.environ_key_name_scheme, self.name
        )
        method.setEnviron(
            self.environ_key_version_scheme, self.version
        )
        method.setEnviron(
            self.environ_key_config_file_scheme, self.configFile
        )
        method.setEnviron(
            self.environ_key_file_scheme, self.setupFile
        )

    def _getCurrentVersion(self):
        data = Method.readOsJsonFile(self.configFile)
        if data:
            return str(data[u'version'][u'active'])

    def _getSystemRaw(self):
        data = Method.readOsJsonFile(self.configFile)
        if data:
            return str(data[u'system'])

    @staticmethod
    def _formatDic():
        return {
            'root': Root()
        }

    @classmethod
    def _setValueCovert(cls, value):
        if not value.startswith(u'#'):
            resourceName, environValue = value.split(u':')
            environValue = environValue.rstrip().lstrip().format(**cls._formatDic())

            if u'|' in environValue:
                if Basic()._isDevelop():
                    return environValue.split(u'|')[0]
                return environValue.split(u'|')[1]
            return environValue

    def _addEnvirons(self, environDic):
        def add(key, value, operate):
            if value is not None:
                if key == u'SYSTEM_PATH':
                    Method.addPythonPath(value)
                else:
                    if operate == u'+':
                        Method.addEnviron(key, value)
                    elif operate == u'=':
                        Method.setEnviron(key, value)
        def main():
            for k, v in environDic.items():
                operate = v[u'operate']
                value = v[u'value']
                if isinstance(value, list):
                    [add(k, self._setValueCovert(i), operate) for i in value]
                else:
                    add(k, self._setValueCovert(value), operate)

        main()

    @property
    def name(self):
        return self._schemeName

    @property
    def version(self):
        return self._schemeVersion

    @property
    def configFile(self):
        return u'{}/config.json'.format(self.schemePathString)

    @property
    def setupFile(self):
        return u'{}/{}/source/setup.json'.format(self.schemePathString, self._schemeVersion)

    def environSetup(self):
        fileString = self.setupFile
        if os.path.exists(fileString):
            with open(fileString) as j:
                datumDic = json.load(j) or {}
                environDic = datumDic.get(u'environ')

                if environDic:
                    self._addEnvirons(environDic)

    def setup(self):
        Method.traceResult(
            u'Start Setup Scheme "{}": "{}"'.format(self.name, self.version)
        )
        self.environSetup()
        Method.traceResult(
            u'Complete Setup Scheme "{}": "{}"'.format(self.name, self.version)
        )


class WindowsPython27Scheme(Abc_Scheme):
    scheme_subpath_string = u'resource/scheme/windows-python-2.7.x'

    def __init__(self, schemeName, schemeVersion):
        self._initAbcScheme(schemeName, schemeVersion)


class WindowsMayaPython27Scheme(Abc_Scheme):
    scheme_subpath_string = u'resource/scheme/windows-maya-python-2.7.x'

    def __init__(self, schemeName, schemeVersion):
        self._initAbcScheme(schemeName, schemeVersion)


class WindowsMaya2019Python27Scheme(Abc_Scheme):
    scheme_subpath_string = u'resource/scheme/windows-maya-2019-python-2.7.x'

    def __init__(self, schemeName, schemeVersion):
        self._initAbcScheme(schemeName, schemeVersion)
