# coding:utf-8
import sys

import os

import socket

import getpass

import json

import time

import shutil

import pkgutil

import importlib

import types

import imp

import copy


class Basic(object):
    Os_Path_Sep = '/'

    module_getpass = getpass

    module_socket = socket

    module_time = time

    module_os = os

    method_os_path = os.path

    method_shutil = shutil

    method_json = json

    module_pkgutil = pkgutil

    module_imp = imp

    module_sys = sys

    module_types = types

    module_importlib = importlib

    module_copy = copy

    environ_key_path_develop = 'LYNXI_PATH_DEVELOP'
    path_default_develop = 'e:/myworkspace/td/lynxi'

    environ_key_path_product = 'LYNXI_PATH_PRODUCT'
    path_default_product = 'e:/myworkspace/td/lynxi'

    environ_key_enable_develop = 'LYNXI_ENABLE_DEVELOP'

    @classmethod
    def _getEnvironValue(cls, environKeyString):
        return cls.module_os.environ.get(environKeyString)

    @classmethod
    def _getUserName(cls):
        return cls.module_getpass.getuser()

    @classmethod
    def _getHostName(cls):
        return cls.module_socket.getfqdn(cls.module_socket.gethostname())

    @classmethod
    def _getHost(cls):
        return cls.module_socket.gethostbyname(cls.module_socket.gethostname())

    @classmethod
    def _setCreateDirectory(cls, directoryString):
        if cls.method_os_path.exists(directoryString) is False:
            cls.module_os.makedirs(directoryString)

    @classmethod
    def _setCreateFileDirectory(cls, fileString):
        directoryString = cls.method_os_path.dirname(fileString)
        cls._setCreateDirectory(directoryString)

    @classmethod
    def _getActiveTimeStamp(cls):
        return cls.module_time.time()

    @classmethod
    def _toDatetag(cls, timestamp):
        return cls.module_time.strftime('%Y_%m%d', cls.module_time.localtime(timestamp))

    @classmethod
    def _getActiveDatetag(cls):
        return cls._toDatetag(cls._getActiveTimeStamp())

    @classmethod
    def _toTimetag(cls, timestamp):
        return cls.module_time.strftime('%Y_%m%d_%H%M', cls.module_time.localtime(timestamp))

    @classmethod
    def _getActiveTimetag(cls):
        return cls._toTimetag(cls._getActiveTimeStamp())

    @classmethod
    def _toPrettify(cls, timestamp):
        return cls.module_time.strftime('%Y-%m-%d %H:%M:%S', cls.module_time.localtime(timestamp))

    @classmethod
    def _getActivePrettifyTime(cls):
        return cls._toPrettify(cls._getActiveTimeStamp())

    @classmethod
    def _toStringList(cls, string, stringLimits=None):
        lis = []
        if isinstance(string, str) or isinstance(string, unicode):
            if stringLimits:
                if string in stringLimits:
                    lis = [string]
            else:
                lis = [string]
        elif isinstance(string, tuple) or isinstance(string, list):
            for i in string:
                if stringLimits:
                    if i in stringLimits:
                        lis.append(i)
                else:
                    lis.append(i)
        return lis
    
    @classmethod
    def _isDevelop(cls):
        return [False, True][os.environ.get(cls.environ_key_enable_develop, 'FALSE').lower() == 'true']

    @classmethod
    def _getPath(cls, key, defaultPath):
        data = cls._getEnvironValue(key)
        if data is not None:
            return data.replace('\\', '/')
        return defaultPath
    @classmethod
    def _getDevelopPath(cls):
        return cls._getPath(cls.environ_key_path_develop, cls.path_default_develop)

    @classmethod
    def _getProductPath(cls):
        return cls._getPath(cls.environ_key_path_product, cls.path_default_product)

    @classmethod
    def _getServerPath(cls):
        if cls._isDevelop():
            return cls._getDevelopPath()
        return cls._getProductPath()

    @classmethod
    def _setLoadPythonModule(cls, moduleName):
        loader = cls.module_pkgutil.find_loader(moduleName)
        if loader:
            return cls.module_importlib.import_module(moduleName)

    @classmethod
    def _toHtmlLogFileString(cls, fileString):
        base = cls.method_os_path.splitext(fileString)[0]
        return u'{}.log.html'.format(base)


class _EnvironString(str):
    def __init__(self, value):
        self._value = value

        self._key = ''
        self._parent = None

    def _add(self, value):
        if self._value:
            lis = [i.lstrip().rstrip() for i in self._value.split(Basic.module_os.pathsep)]
            lowerLis = [i.lstrip().rstrip().lower() for i in self._value.lower().split(Basic.module_os.pathsep)]
            if value.lower() not in lowerLis:
                lis.append(value)
                self._value = Basic.module_os.pathsep.join(lis)
        else:
            self._value = value

    def _sub(self, value):
        if self._value:
            lis = [i.lstrip().rstrip() for i in self._value.split(Basic.module_os.pathsep)]
            lowerLis = [i.lstrip().rstrip().lower() for i in self._value.lower().split(Basic.module_os.pathsep)]
            if value.lower() in lowerLis:
                i = lowerLis.index(value.lower())
                lis.remove(lis[i])
                self._value = Basic.module_os.pathsep.join(lis)

    def _update(self):
        Basic.module_os.environ[self._key] = self._value

        str_ = _EnvironString(self._value)
        str_.key = self._key
        str_.parent = self._parent

        self.parent.__dict__[self._key] = str_
        return str_

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

        Basic.module_os.environ[self._key] = self._value

    def __iadd__(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            [self._add(i) for i in list(value)]
        else:
            self._add(value)

        return self._update()

    def __isub__(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            [self._sub(i) for i in list(value)]
        else:
            self._sub(value)

        return self._update()

    def append(self, value):
        self._add(value)

    def remove(self, value):
        self._sub(value)

    def __str__(self):
        # copy list
        lis = [i.replace('\\', '/') for i in self._value.split(Basic.module_os.pathsep)]
        lis.sort()
        return '\r\n'.join(lis)


class Environ(Basic):
    def __getattr__(self, key):
        self._get(key)

    def __setattr__(self, key, value):
        key = key.upper()

        str_ = _EnvironString(value)
        str_.key = key
        str_.parent = self

        self.__dict__[key] = str_

    def _get(self, key):
        key = key.upper()

        value = self.module_os.environ.get(key, '')
        if not key in self.__dict__:
            str_ = _EnvironString(value)
            str_.key = key
            str_.parent = self

            self.__dict__[key] = str_
            return str_

    @classmethod
    def isExist(cls, key, value):
        value_ = cls.module_os.environ.get(key)
        if value_ is not None:
            lowerLis = [i.lstrip().rstrip().lower() for i in value_.split(cls.module_os.pathsep)]
            return value.lower() in lowerLis
        return False


class SystemPath(Basic):
    def __init__(self):
        pass
    @classmethod
    def isExist(cls, pathString):
        pathLowerLis = [i.replace('\\', '/').lower() for i in cls.module_sys.path]
        if pathString.lower() in pathLowerLis:
            return True
        return False

    @classmethod
    def add(cls, pathString):
        if cls.isExist(pathString) is False:
            cls.module_sys.path.insert(0, pathString)

    @classmethod
    def remove(cls, pathString):
        if cls.isExist(pathString) is True:
            cls.module_sys.path.remove(pathString)

    def __iadd__(self, other):
        if isinstance(other, tuple) or isinstance(other, list):
            [self.add(i) for i in other]
        elif isinstance(other, str) or isinstance(other, unicode):
            self.add(other)

        return self

    def __radd__(self, other):
        if isinstance(other, tuple) or isinstance(other, list):
            [self.remove(i) for i in other]
        elif isinstance(other, str) or isinstance(other, unicode):
            self.remove(other)

        return self

    def __str__(self):
        # copy list
        lis = [i.replace('\\', '/') for i in self.module_sys.path]
        lis.sort()
        return '\r\n'.join(lis)