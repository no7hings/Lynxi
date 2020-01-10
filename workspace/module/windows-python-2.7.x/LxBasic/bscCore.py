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

import platform

import re

import datetime

import math

import hashlib

import collections

import locale


class Basic(object):
    Os_Path_Sep = '/'

    module_getpass = getpass

    module_socket = socket

    module_time = time

    module_datetime = datetime

    module_os = os

    mtd_os_path = os.path

    method_shutil = shutil

    method_json = json

    module_pkgutil = pkgutil

    module_imp = imp

    module_sys = sys

    module_types = types

    module_importlib = importlib

    module_copy = copy

    module_platform = platform

    module_re = re
    
    module_math = math

    module_locale = locale

    cls_dic_order = collections.OrderedDict

    environ_key_path_develop = 'LYNXI_PATH_DEVELOP'
    path_default_develop = 'e:/myworkspace/td/lynxi'

    environ_key_path_product = 'LYNXI_PATH_PRODUCT'
    path_default_product = 'e:/myworkspace/td/lynxi'

    environ_key_enable_develop = 'LYNXI_ENABLE_DEVELOP'

    module_hashlib = hashlib

    @classmethod
    def _getSystemUsername(cls):
        return cls.module_getpass.getuser()

    @classmethod
    def _getSystemHostname(cls):
        return cls.module_socket.getfqdn(cls.module_socket.gethostname())

    @classmethod
    def _getSystemHost(cls):
        return cls.module_socket.gethostbyname(cls.module_socket.gethostname())

    @classmethod
    def _setOsDirectoryCreate(cls, directoryString):
        if cls.mtd_os_path.exists(directoryString) is False:
            cls.module_os.makedirs(directoryString)

    @classmethod
    def _setOsFileDirectoryCreate(cls, fileString):
        directoryString = cls.mtd_os_path.dirname(fileString)
        cls._setOsDirectoryCreate(directoryString)

    @classmethod
    def _getActiveTimestamp(cls):
        return cls.module_time.time()

    @classmethod
    def _timestampToDatetag(cls, timestamp):
        return cls.module_time.strftime('%Y_%m%d', cls.module_time.localtime(timestamp))

    @classmethod
    def _getActiveDatetag(cls):
        return cls._timestampToDatetag(cls._getActiveTimestamp())

    @classmethod
    def _timestampToTimetag(cls, timestamp):
        return cls.module_time.strftime('%Y_%m%d_%H%M', cls.module_time.localtime(timestamp))

    @classmethod
    def _getActiveTimetag(cls):
        return cls._timestampToTimetag(cls._getActiveTimestamp())

    @classmethod
    def _timestampToPrettify(cls, timestamp):
        return cls.module_time.strftime('%Y-%m-%d %H:%M:%S', cls.module_time.localtime(timestamp))

    @classmethod
    def _getActivePrettifyTime(cls):
        return cls._timestampToPrettify(cls._getActiveTimestamp())

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
        return [False, True][cls._getOsEnvironValue(cls.environ_key_enable_develop, 'FALSE').lower() == 'true']

    @classmethod
    def _getOsEnvironValue(cls, key, failobj=None):
        return cls.module_os.environ.get(key, failobj)

    @classmethod
    def _getOsEnvironValueAsPath(cls, key, failobj=None):
        if key in cls.module_os.environ:
            return cls._getOsEnvironValue(key).replace('\\', '/')
        elif failobj is not None:
            return failobj
        return ''

    @classmethod
    def _getOsEnvironValueAsList(cls, key, failobj=None):
        if key in cls.module_os.environ:
            return cls._getOsEnvironValue(key).split(cls.module_os.pathsep)
        elif failobj is not None:
            return failobj
        return []

    @staticmethod
    def _osPathToPythonStyle(pathString):
        return pathString.replace('\\', '/')

    @classmethod
    def _isOsSameFile(cls, sourceFileString, targetFileString):
        return cls.mtd_os_path.normpath(sourceFileString) == cls.mtd_os_path.normpath(targetFileString)
    
    @classmethod
    def _getOsFileDirectory(cls, fileString):
        return cls.mtd_os_path.dirname(fileString)

    @classmethod
    def _getOsFileBasename(cls, fileString):
        return cls.mtd_os_path.basename(fileString)
    
    @classmethod
    def _getOsFileExt(cls, fileString):
        return cls.mtd_os_path.splitext(fileString)[1]
    
    @classmethod
    def _toOsFileReplaceFileName(cls, fileString, newFileName):
        osPath = cls._getOsFileDirectory(fileString)
        osExt = cls._getOsFileExt(fileString)
        newFileString = u'{0}/{1}{2}'.format(osPath, newFileName, osExt)
        return newFileString

    @classmethod
    def _isOsPathExist(cls, pathString):
        return cls.mtd_os_path.exists(pathString)

    @classmethod
    def _isOsDirectoryExist(cls, directoryString):
        return cls.mtd_os_path.isdir(directoryString)

    @classmethod
    def _isOsFileExist(cls, fileString):
        return cls.mtd_os_path.isfile(fileString)

    @classmethod
    def _setOsPathOpen(cls, pathString):
        if cls._isOsPathExist(pathString) is True:
            cls.module_os.startfile(pathString.replace('/', cls.module_os.sep))

    @classmethod
    def _setOsFileOpen(cls, pathString):
        if cls._isOsFileExist(pathString) is True:
            cls.module_os.startfile(pathString.replace('/', cls.module_os.sep))

    @classmethod
    def _setOsDirectoryOpen(cls, pathString):
        if cls._isOsFileExist(pathString) is True:
            cls.module_os.startfile(pathString.replace('/', cls.module_os.sep))

    @classmethod
    def _getOsFileMtimestamp(cls, fileString):
        if cls._isOsFileExist(fileString):
            return cls.module_os.stat(fileString).st_mtime
        
    @classmethod
    def _isOsFileTimeChanged(cls, sourceFileString, targetFileString):
        if cls._isOsFileExist(sourceFileString) and cls._isOsFileExist(targetFileString):
            if str(cls._getOsFileMtimestamp(sourceFileString)) != str(cls._getOsFileMtimestamp(targetFileString)):
                return True
            return False
        return False

    @classmethod
    def _textToHash(cls, text):
        md5Obj = cls.module_hashlib.md5()
        md5Obj.update(text)
        return str(md5Obj.hexdigest()).upper()

    @classmethod
    def _getOsFileHash(cls, fileString):
        if cls._isOsFileExist(fileString):
            with open(fileString, 'rb') as f:
                md5Obj = cls.module_hashlib.md5()
                md5Obj.update(f.read())

                f.close()
                return cls._textToHash(f.read())
        return u'D41D8CD98F00B204E9800998ECF8427E'

    @classmethod
    def _getOsFileHash_(cls, fileString):
        if cls._isOsFileExist(fileString):
            with open(fileString, 'rb') as f:
                md5Obj = cls.module_hashlib.md5()
                while True:
                    d = f.read(8096)
                    if not d:
                        break
                    md5Obj.update(d)

                f.close()
                return str(md5Obj.hexdigest()).upper()
        return u'D41D8CD98F00B204E9800998ECF8427E'

    @classmethod
    def _isOsFileHashChanged(cls, sourceFileString, targetFileString):
        if cls._isOsFileExist(sourceFileString) and cls._isOsFileExist(targetFileString):
            if cls._getOsFileHash(sourceFileString) != cls._getOsFileHash(targetFileString):
                return True
            return False
        return False

    @classmethod
    def _setOsFileRename(cls, fileString, newFileName):
        if cls._isOsFileExist(fileString):
            newFileString = cls._toOsFileReplaceFileName(fileString, newFileName)
            if cls._isOsSameFile(fileString, newFileString) is False:
                os.rename(fileString, newFileString)
            
    @classmethod
    def _setOsFileRename_(cls, fileString, newFileString):
        if cls._isOsSameFile(fileString, newFileString) is False:
            os.rename(fileString, newFileString)

    @classmethod
    def _setOsFileCopy(cls, sourceFileString, targetFileString, force=True):
        if cls.mtd_os_path.isfile(sourceFileString):
            cls._setOsFileDirectoryCreate(targetFileString)
            # Check Same File
            if not cls._isOsSameFile(sourceFileString, targetFileString):
                if force is True:
                    cls.method_shutil.copy2(sourceFileString, targetFileString)
                elif force is False:
                    try:
                        cls.method_shutil.copy2(sourceFileString, targetFileString)
                    except IOError:
                        print sourceFileString, targetFileString

    @classmethod
    def _setOsPathRemove(cls, pathString):
        if cls.mtd_os_path.isfile(pathString):
            cls.module_os.remove(pathString)
        elif cls.mtd_os_path.isdir(pathString):
            cls.module_os.removedirs(pathString)

    @classmethod
    def _toOsRelativeName(cls, rootString, fullpathName):
        return fullpathName[len(rootString) + 1:]
    
    @classmethod
    def _toOsFileString(cls, osPath, osFileBasename):
        return cls.mtd_os_path.join(osPath, osFileBasename).replace('\\', '/')

    @classmethod
    def _getOsPathNamesByDirectory(cls, rootString, extString, isFile, isFullpath):
        def extFilterFnc_(fullpathName_):
            if filterExtStringLis is not None:
                for i in filterExtStringLis:
                    if fullpathName_.endswith(i):
                        return True
                return False
            return True

        def addFnc_(fullpathName_):
            if extFilterFnc_(fullpathName_) is True:
                if isFullpath is True:
                    lis.append(fullpathName_)
                else:
                    relativeName = cls._toOsRelativeName(rootString, fullpathName_)
                    lis.append(relativeName)

        def recursionFnc_(directoryString_):
            children = cls.module_os.listdir(directoryString_)
            if children:
                for i in children:
                    fullpathName = cls._toOsFileString(directoryString_, i)
                    if cls.mtd_os_path.isfile(fullpathName):
                        addFnc_(fullpathName)
                    else:
                        if isFile is False:
                            addFnc_(fullpathName)

                        recursionFnc_(fullpathName)

        lis = []

        if extString is not None:
            filterExtStringLis = cls._toStringList(extString)
        else:
            filterExtStringLis = None

        if cls.mtd_os_path.exists(rootString):
            recursionFnc_(rootString)

        return lis

    @classmethod
    def _getOsFileTemporary(cls, fileString):
        datetag = cls._getActiveDatetag()
        temporaryDirectory = 'D:/.lynxi.temporary/' + datetag
        temporaryFileString = cls._toOsFileString(temporaryDirectory, cls.mtd_os_path.basename(fileString))
        cls._setOsDirectoryCreate(temporaryDirectory)
        return temporaryFileString

    @classmethod
    def _getOsFileJoinTimetag(cls, fileString, timetag=None, useMode=0):
        if timetag is None:
            timetag = cls._getActiveTimetag()

        if useMode == 0:
            return (u'_{}'.format(timetag)).join(os.path.splitext(fileString))
        elif useMode == 1:
            return u'{}/{}/'.format(cls._getOsFileDirectory(fileString), timetag, cls._getOsFileBasename(fileString))
        return fileString

    @classmethod
    def _setOsFileBackup(cls, fileString, backupFileString, timetag=None, useMode=0):
        if cls._isOsFileExist(fileString):
            backupFileString_ = cls._getOsFileJoinTimetag(backupFileString, timetag, useMode)
            #
            cls._setOsFileCopy(fileString, backupFileString_)

    @classmethod
    def _getDevelopPath(cls):
        return cls._getOsEnvironValueAsPath(cls.environ_key_path_develop, cls.path_default_develop)

    @classmethod
    def _getProductPath(cls):
        return cls._getOsEnvironValueAsPath(cls.environ_key_path_product, cls.path_default_product)

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
        base = cls.mtd_os_path.splitext(fileString)[0]
        return u'{}.log.html'.format(base)

    @classmethod
    def _loadPythonModule(cls, moduleName):
        loader = cls.module_pkgutil.find_loader(moduleName)
        if loader:
            return cls.module_importlib.import_module(moduleName)

    @classmethod
    def _logDirectory(cls):
        return u'{}/.log'.format(cls._getServerPath())

    @classmethod
    def _exceptionLogFile(cls):
        return u'{}/{}.exception.log'.format(
            cls._logDirectory(), cls._getActiveDatetag()
        )

    @classmethod
    def _errorLogFile(cls):
        return u'{}/{}.error.log'.format(
            cls._logDirectory(), cls._getActiveDatetag()
        )

    @classmethod
    def _resultLogFile(cls):
        return u'{}/{}.result.log'.format(
            cls._logDirectory(), cls._getActiveDatetag()
        )

    @classmethod
    def _getQtProgressBar(cls, title, maxValue):
        module = cls._setLoadPythonModule('LxUi.qt.qtCommands')
        if module is not None:
            return module.setProgressWindowShow(title, maxValue)

    @classmethod
    def _setQtProgressBarUpdate(cls, progressBar, text=None):
        if progressBar is not None:
            progressBar.updateProgress(text)


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
