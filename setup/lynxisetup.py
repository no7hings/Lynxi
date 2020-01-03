# coding:utf-8
import platform

import sys

import os

import json

import time


def _isDevelop():
    return [False, True][os.environ.get('LYNXI_DEVELOP', 'FALSE').lower() == 'true']


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
    def getOsActiveViewTime():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    @classmethod
    def traceMessage(cls, text):
        print u'# Lynxi <{}>'.format(cls.getOsActiveViewTime())
        print u'    {}'.format(text)

    @classmethod
    def traceResult(cls, text):
        cls.traceMessage(
            u'''# Result {}'''.format(text)
        )

    @classmethod
    def traceWarning(cls, text):
        cls.traceMessage(
            u'''# Warning {}'''.format(text)
        )

    @classmethod
    def traceError(cls, text):
        cls.traceMessage(
            u'''# Error {}'''.format(text)
        )

    @classmethod
    def addEnviron(cls, key, value):
        if key in os.environ:
            lowerLis = [i.lower() for i in os.environ[key].split(os.pathsep)]
        else:
            lowerLis = []

        if value.lower() not in lowerLis:
            os.environ[key] += os.pathsep + value
            cls.traceResult(
                'Add Environ "{}": "{}"'.format(key, value)
            )

    @classmethod
    def setEnviron(cls, key, value):
        if key in os.environ:
            lowerValue = os.environ[key].lower()
        else:
            lowerValue = ''

        if value.lower() != lowerValue:
            os.environ[key] = value
            cls.traceResult(
                'Set Environ "{}": "{}"'.format(key, value)
            )

    @classmethod
    def addPythonPath(cls, value):
        lowerLis = [i.lower() for i in sys.path]
        if value.lower() not in lowerLis:
            sys.path.insert(0, value)
            cls.traceResult(
                'Add Python Path: "{}"'.format(value)
            )

    @staticmethod
    def readOsJsonFile(fileString):
        if os.path.exists(fileString):
            with open(fileString) as j:
                data = json.load(j)
                return data


class Root(object):
    def_path = 'e:/myworkspace/td/lynxi'
    def_local_path = 'c:/.lynxi'
    def_develop_path = 'e:/myworkspace/td/lynxi'

    @property
    def active(self):
        return self.server

    @property
    def server(self):
        if _isDevelop():
            return self.develop
        return self.product

    @property
    def local(self):
        return os.environ.get('LYNXI_LOCAL_PATH', self.def_local_path).replace('\\', '/')

    @property
    def product(self):
        return os.environ.get('LYNXI_PATH', self.def_path).replace('\\', '/')

    @property
    def develop(self):
        return os.environ.get('LYNXI_DEVELOP_PATH', self.def_develop_path).replace('\\', '/')


class Abc_Scheme(object):
    scheme_subpath_string = None

    def _initAbcScheme(self, schemeName, schemeVersion):
        method = Method()

        self._schemeName = schemeName

        self.schemePathString = '{}/{}-{}'.format(
            Root().server, self.scheme_subpath_string, schemeName
        )

        if schemeVersion == 'active':
            self._schemeVersion = self._getCurrentVersion()
        else:
            self._schemeVersion = schemeVersion

        self._systemRaw = self._getSystemRaw()

        method.setEnviron(
            'LYNXI_SCHEME_NAME', schemeName
        )
        method.setEnviron(
            'LYNXI_SCHEME_VERSION', self._schemeVersion
        )
        method.setEnviron(
            'LYNXI_SCHEME_SYSTEM', self._systemRaw
        )

    def _getCurrentVersion(self):
        data = Method.readOsJsonFile(self.configJsonFile)
        if data:
            return str(data['version']['active'])

    def _getSystemRaw(self):
        data = Method.readOsJsonFile(self.configJsonFile)
        if data:
            return str(data['system'])

    @staticmethod
    def _formatDic():
        return {
            'root': Root()
        }

    @classmethod
    def _covertValue(cls, value):
        value = value.format(**cls._formatDic())
        if '|' in value:
            if _isDevelop():
                return value.split('|')[0]
            return value.split('|')[1]
        return value

    def _addEnvironMethod(self, environDic):
        def add(key, value, operate):
            if key == 'SYSTEM_PATH':
                Method.addPythonPath(value)
            else:
                if operate == '+':
                    Method.addEnviron(key, value)
                elif operate == '=':
                    Method.setEnviron(key, value)
        def main():
            for k, v in environDic.items():
                operate = v['operate']
                value = v['value']
                if isinstance(value, list):
                    [add(k, self._covertValue(i), operate) for i in value]
                else:
                    add(k, self._covertValue(value), operate)

        main()

    @property
    def name(self):
        return self._schemeName

    @property
    def version(self):
        return self._schemeVersion

    @property
    def configJsonFile(self):
        return u'{}/config.json'.format(self.schemePathString)

    def setupJsonFile(self):
        return u'{}/{}/source/setup.json'.format(self.schemePathString, self._schemeVersion)

    def environSetup(self):
        fileString = self.setupJsonFile()
        if os.path.exists(fileString):
            with open(fileString) as j:
                datumDic = json.load(j) or {}
                environDic = datumDic.get('environ')

                if environDic:
                    self._addEnvironMethod(environDic)

    def setup(self):
        Method.traceResult(
            'Start Setup Scheme "{}": "{}"'.format(self.name, self.version)
        )
        self.environSetup()
        Method.traceResult(
            'Complete Setup Scheme "{}": "{}"'.format(self.name, self.version)
        )


class WindowsPython27Scheme(Abc_Scheme):
    scheme_subpath_string = 'resource/scheme/windows-python-2.7.x'

    def __init__(self, schemeName, schemeVersion):
        self._initAbcScheme(schemeName, schemeVersion)


class WindowsMayaPython27Scheme(Abc_Scheme):
    scheme_subpath_string = 'resource/scheme/windows-maya-python-2.7.x'

    def __init__(self, schemeName, schemeVersion):
        self._initAbcScheme(schemeName, schemeVersion)
