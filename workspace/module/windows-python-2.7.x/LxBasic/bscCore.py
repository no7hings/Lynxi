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


class Basic(object):
    Os_Path_Sep = '/'

    getpass_method = getpass

    socket_method = socket

    time_method = time

    os_method = os

    os_path_method = os.path

    copy_method = shutil

    json_method = json

    pkgutil_method = pkgutil

    imp_method = imp

    sys_method = sys

    types_method = types

    importlib_method = importlib

    environ_key_path_develop = 'LYNXI_PATH_DEVELOP'
    path_default_develop = 'e:/myworkspace/td/lynxi'

    environ_key_path_product = 'LYNXI_PATH_PRODUCT'
    path_default_product = 'e:/myworkspace/td/lynxi'

    environ_key_enable_develop = 'LYNXI_ENABLE_DEVELOP'

    @classmethod
    def _getEnvironValue(cls, environKeyString):
        return cls.os_method.environ.get(environKeyString)

    @classmethod
    def _getUserName(cls):
        return cls.getpass_method.getuser()

    @classmethod
    def _getHostName(cls):
        return cls.socket_method.getfqdn(cls.socket_method.gethostname())

    @classmethod
    def _getHost(cls):
        return cls.socket_method.gethostbyname(cls.socket_method.gethostname())

    @classmethod
    def _setCreateDirectory(cls, directoryString):
        if cls.os_path_method.exists(directoryString) is False:
            cls.os_method.makedirs(directoryString)

    @classmethod
    def _setCreateFileDirectory(cls, fileString):
        directoryString = cls.os_path_method.dirname(fileString)
        cls._setCreateDirectory(directoryString)

    @classmethod
    def _activeTimeStamp(cls):
        return cls.time_method.time()

    @classmethod
    def _getActiveViewTime(cls):
        return cls.time_method.strftime('%Y-%m-%d %H:%M:%S', cls.time_method.localtime(cls.time_method.time()))

    @classmethod
    def _toDatetag(cls, timestamp):
        return cls.time_method.strftime('%Y_%m%d', cls.time_method.localtime(timestamp))

    @classmethod
    def _getActiveDatetag(cls):
        return cls._toDatetag(cls._activeTimeStamp())

    @classmethod
    def _toTimetag(cls, timestamp):
        return cls.time_method.strftime('%Y_%m%d_%H%M', cls.time_method.localtime(timestamp))

    @classmethod
    def _getActiveTimetag(cls):
        return cls._toTimetag(cls._activeTimeStamp())

    @classmethod
    def _toPrettify(cls, timestamp):
        return cls.time_method.strftime('%Y-%m-%d %H:%M:%S', cls.time_method.localtime(timestamp))

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
