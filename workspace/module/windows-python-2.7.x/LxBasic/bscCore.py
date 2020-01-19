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

import glob

import gzip

import tarfile

import threading


class Basic(object):
    MOD_getpass = getpass
    MOD_socket = socket
    MOD_time = time
    MOD_datetime = datetime
    MOD_os = os
    MOD_shutil = shutil
    MOD_json = json
    MOD_pkgutil = pkgutil
    MOD_imp = imp
    MOD_sys = sys
    MOD_types = types
    MOD_importlib = importlib
    MOD_copy = copy
    MOD_platform = platform
    MOD_re = re
    MOD_math = math
    MOD_locale = locale
    MOD_hashlib = hashlib
    MOD_glob = glob
    MOD_gzip = gzip
    MOD_tarfile = tarfile
    MOD_threading = threading

    MTD_os_path = os.path

    CLS_dic_order = collections.OrderedDict

    def_os_separator_string = '/'

    environ_key_path_develop = 'LYNXI_PATH_DEVELOP'
    path_default_develop = 'e:/myworkspace/td/lynxi'

    environ_key_path_product = 'LYNXI_PATH_PRODUCT'
    path_default_product = 'e:/myworkspace/td/lynxi'

    environ_key_enable_develop = 'LYNXI_ENABLE_DEVELOP'
    environ_key_enable_trace = 'LYNXI_ENABLE_TRACE'

    def_time_month_lis = [
        (u'一月', 'January'),
        (u'二月', 'February'),
        (u'三月', 'March'),
        (u'四月', 'April'),
        (u'五月', 'May'),
        (u'六月', 'June'),
        (u'七月', 'July'),
        (u'八月', 'August'),
        (u'九月', 'September'),
        (u'十月', 'October'),
        (u'十一月', 'November'),
        (u'十二月', 'December')
    ]
    def_time_day_lis = [
        (u'一日', '1st'),
        (u'二日', '2nd'),
        (u'三日', '3rd'),
        (u'四日', '4th'),
        (u'五日', '5th'),
        (u'六日', '6th'),
        (u'七日', '7th'),
        (u'八日', '8th'),
        (u'九日', '9th'),
        (u'十日', '10th'),
    ]
    def_time_week_lis = [
        (u'周一', 'Monday'),
        (u'周二', 'Tuesday'),
        (u'周三', 'Wednesday'),
        (u'周四', 'Thursday'),
        (u'周五', 'Friday'),
        (u'周六', 'Saturday'),
        (u'周天', 'Sunday'),
    ]

    STR_time_tag_format = '%Y_%m%d_%H%M_%S'
    STR_time_prettify_format = '%Y-%m-%d %H:%M:%S'
    def_time_tag_search_string = '[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]_[0-9][0-9]'

    STR_key_source = 'source'
    STR_key_username = 'username'
    STR_key_hostname = 'hostname'
    STR_key_host = 'host'
    STR_key_timestamp = 'timestamp'
    STR_key_stage = 'stage'
    STR_key_description = 'description'
    STR_key_note = 'note'

    @classmethod
    def _getSystemUsername(cls):
        return cls.MOD_getpass.getuser()

    @classmethod
    def _getSystemHostname(cls):
        return cls.MOD_socket.getfqdn(cls.MOD_socket.gethostname())

    @classmethod
    def _getSystemHost(cls):
        return cls.MOD_socket.gethostbyname(cls.MOD_socket.gethostname())

    @classmethod
    def _setOsDirectoryCreate(cls, directoryString):
        if cls.MTD_os_path.exists(directoryString) is False:
            cls.MOD_os.makedirs(directoryString)

    @classmethod
    def _setOsFileDirectoryCreate(cls, fileString):
        directoryString = cls.MTD_os_path.dirname(fileString)
        cls._setOsDirectoryCreate(directoryString)

    @classmethod
    def _getSystemActiveTimestamp(cls):
        return cls.MOD_time.time()

    @classmethod
    def _timestampToDatetag(cls, timestamp):
        return cls.MOD_time.strftime('%Y_%m%d', cls.MOD_time.localtime(timestamp))

    @classmethod
    def _getActiveDatetag(cls):
        return cls._timestampToDatetag(cls._getSystemActiveTimestamp())

    @classmethod
    def _timestampToTimetag(cls, timestamp):
        return cls.MOD_time.strftime(
            cls.STR_time_tag_format,
            cls.MOD_time.localtime(timestamp)
        )

    @classmethod
    def _getActiveTimetag(cls):
        return cls._timestampToTimetag(cls._getSystemActiveTimestamp())

    @classmethod
    def _timestampToPrettify(cls, timestamp):
        return cls.MOD_time.strftime(
            cls.STR_time_prettify_format,
            cls.MOD_time.localtime(timestamp)
        )

    @classmethod
    def _getActivePrettifyTime(cls):
        return cls._timestampToPrettify(cls._getSystemActiveTimestamp())

    @classmethod
    def toStringList(cls, string, includes=None):
        lis = []
        if isinstance(string, str) or isinstance(string, unicode):
            if includes:
                if string in includes:
                    lis = [string]
            else:
                lis = [string]
        elif isinstance(string, tuple) or isinstance(string, list):
            for i in string:
                if includes:
                    if i in includes:
                        lis.append(i)
                else:
                    lis.append(i)
        return lis
    
    @classmethod
    def _isDevelop(cls):
        return [False, True][cls._getOsEnvironRawWithKey(cls.environ_key_enable_develop, 'FALSE').lower() == 'true']

    @classmethod
    def _isTraceEnable(cls):
        return [False, True][cls._getOsEnvironRawWithKey(cls.environ_key_enable_trace, 'FALSE').lower() == 'true']

    @classmethod
    def _getOsEnvironRawWithKey(cls, key, failobj=None):
        return cls.MOD_os.environ.get(key, failobj)

    @classmethod
    def _getOsEnvironRawAsPath(cls, key, failobj=None):
        if key in cls.MOD_os.environ:
            return cls._getOsEnvironRawWithKey(key).replace('\\', '/')
        elif failobj is not None:
            return failobj
        return ''

    @classmethod
    def _getOsEnvironRawAsList(cls, key, failobj=None):
        if key in cls.MOD_os.environ:
            return cls._getOsEnvironRawWithKey(key).split(cls.MOD_os.pathsep)
        elif failobj is not None:
            return failobj
        return []

    @staticmethod
    def _osPathToPythonStyle(pathString):
        return pathString.replace('\\', '/')

    @classmethod
    def _isOsSameFile(cls, sourceFileString, targetFileString):
        return cls.MTD_os_path.normpath(sourceFileString) == cls.MTD_os_path.normpath(targetFileString)
    
    @classmethod
    def _getOsFileDirectoryName(cls, fileString):
        return cls.MTD_os_path.dirname(fileString)

    @classmethod
    def _getOsFileBasename(cls, fileString):
        return cls.MTD_os_path.basename(fileString)
    
    @classmethod
    def _getOsFileExt(cls, fileString):
        return cls.MTD_os_path.splitext(fileString)[1]
    
    @classmethod
    def _toOsFileStringReplaceFileName(cls, fileString, newFileName):
        osPath = cls._getOsFileDirectoryName(fileString)
        osExt = cls._getOsFileExt(fileString)
        newFileString = u'{0}/{1}{2}'.format(osPath, newFileName, osExt)
        return newFileString

    @classmethod
    def _isOsPathExist(cls, pathString):
        return cls.MTD_os_path.exists(pathString)

    @classmethod
    def _isOsDirectoryExist(cls, directoryString):
        return cls.MTD_os_path.isdir(directoryString)

    @classmethod
    def _isOsFileExist(cls, fileString):
        return cls.MTD_os_path.isfile(fileString)

    @classmethod
    def _setOsPathOpen(cls, pathString):
        if cls._isOsPathExist(pathString) is True:
            cls.MOD_os.startfile(pathString.replace('/', cls.MOD_os.sep))

    @classmethod
    def _setOsFileOpen(cls, pathString):
        if cls._isOsFileExist(pathString) is True:
            cls.MOD_os.startfile(pathString.replace('/', cls.MOD_os.sep))

    @classmethod
    def _setOsDirectoryOpen(cls, pathString):
        if cls._isOsFileExist(pathString) is True:
            cls.MOD_os.startfile(pathString.replace('/', cls.MOD_os.sep))

    @classmethod
    def _getOsFileMtimestamp(cls, fileString):
        if cls._isOsFileExist(fileString):
            return cls.MOD_os.stat(fileString).st_mtime

    @classmethod
    def _getOsFileSize(cls, fileString):
        if cls._isOsFileExist(fileString):
            return cls.MTD_os_path.getsize(fileString)
        return 0
        
    @classmethod
    def _isOsFileTimeChanged(cls, sourceFileString, targetFileString):
        if cls._isOsFileExist(sourceFileString) and cls._isOsFileExist(targetFileString):
            if str(cls._getOsFileMtimestamp(sourceFileString)) != str(cls._getOsFileMtimestamp(targetFileString)):
                return True
            return False
        return False

    @classmethod
    def _textToHash(cls, text):
        md5Obj = cls.MOD_hashlib.md5()
        md5Obj.update(text)
        return str(md5Obj.hexdigest()).upper()

    @classmethod
    def _getOsFileHash(cls, fileString):
        if cls._isOsFileExist(fileString):
            with open(fileString, 'rb') as f:
                md5Obj = cls.MOD_hashlib.md5()
                md5Obj.update(f.read())

                f.close()
                return cls._textToHash(f.read())
        return u'D41D8CD98F00B204E9800998ECF8427E'

    @classmethod
    def _getOsFileHash_(cls, fileString):
        if cls._isOsFileExist(fileString):
            with open(fileString, 'rb') as f:
                md5Obj = cls.MOD_hashlib.md5()
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
            newFileString = cls._toOsFileStringReplaceFileName(fileString, newFileName)
            if cls._isOsSameFile(fileString, newFileString) is False:
                os.rename(fileString, newFileString)
            
    @classmethod
    def _setOsFileRename_(cls, fileString, newFileString):
        if cls._isOsSameFile(fileString, newFileString) is False:
            os.rename(fileString, newFileString)

    @classmethod
    def _setOsFileCopy(cls, sourceFileString, targetFileString, force=True):
        cls._setOsFileDirectoryCreate(targetFileString)
        # Check Same File
        if not cls._isOsSameFile(sourceFileString, targetFileString):
            if force is True:
                cls.MOD_shutil.copy2(sourceFileString, targetFileString)
            elif force is False:
                try:
                    cls.MOD_shutil.copy2(sourceFileString, targetFileString)
                except IOError:
                    print sourceFileString, targetFileString

    @classmethod
    def _setOsPathRemove(cls, pathString):
        if cls.MTD_os_path.isfile(pathString):
            cls.MOD_os.remove(pathString)
        elif cls.MTD_os_path.isdir(pathString):
            cls.MOD_os.removedirs(pathString)

    @classmethod
    def _osPathString2RelativeName(cls, rootString, fullpathName):
        return fullpathName[len(rootString) + 1:]
    
    @classmethod
    def _toOsFileString(cls, osPath, osFileBasename):
        return cls.MTD_os_path.join(osPath, osFileBasename).replace('\\', '/')

    @classmethod
    def _getOsPathNameLisByDirectory(cls, rootString, extString, isFile, isFullpath):
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
                    relativeName = cls._osPathString2RelativeName(rootString, fullpathName_)
                    lis.append(relativeName)

        def recursionFnc_(directoryString_):
            children = cls.MOD_os.listdir(directoryString_)
            if children:
                for i in children:
                    fullpathName = cls._toOsFileString(directoryString_, i)
                    if cls.MTD_os_path.isfile(fullpathName):
                        addFnc_(fullpathName)
                    else:
                        if isFile is False:
                            addFnc_(fullpathName)

                        recursionFnc_(fullpathName)

        lis = []

        if extString is not None:
            filterExtStringLis = cls.toStringList(extString)
        else:
            filterExtStringLis = None

        if cls.MTD_os_path.exists(rootString):
            recursionFnc_(rootString)

        return lis

    @classmethod
    def _getOsFileTemporaryName(cls, fileString, timetag=None):
        if timetag is None:
            timetag = cls._getActiveTimetag()

        temporaryDirectory = u'D:/.lynxi.temporary/{}'.format(timetag)

        temporaryFileString = cls._toOsFileString(temporaryDirectory, cls._getOsFileBasename(fileString))
        cls._setOsDirectoryCreate(temporaryDirectory)
        return temporaryFileString

    @classmethod
    def _toOsFileJoinTimetag(cls, fileString, timetag=None, useMode=0):
        if timetag is None:
            timetag = cls._getActiveTimetag()

        if useMode == 0:
            return (u'.{}'.format(timetag)).join(os.path.splitext(fileString))
        elif useMode == 1:
            return u'{}/{}/{}'.format(cls._getOsFileDirectoryName(fileString), timetag, cls._getOsFileBasename(fileString))
        return fileString

    @classmethod
    def _setOsFileBackup(cls, fileString, backupFileString, timetag=None, useMode=0):
        backupFileString_ = cls._toOsFileJoinTimetag(backupFileString, timetag, useMode)
        cls._setOsFileCopy(fileString, backupFileString_)

    @classmethod
    def _getOsFileMtimetag(cls, fileString):
        return cls._timestampToTimetag(cls._getOsFileMtimestamp(fileString))

    @classmethod
    def _toOsFileInfoJsonFileString(cls, fileString):
        base = cls.MTD_os_path.splitext(fileString)[0]
        return base + u'.info.json'

    @classmethod
    def _infoDict(cls, fileString):
        return {
            cls.STR_key_source: fileString,
            cls.STR_key_timestamp: cls._getSystemActiveTimestamp(),
            cls.STR_key_username: cls._getSystemUsername(),
            cls.STR_key_hostname: cls._getSystemHostname(),
            cls.STR_key_host: cls._getSystemHost()
        }

    @classmethod
    def _toOsFileResultFileString(cls, fileString):
        base = cls.MTD_os_path.splitext(fileString)[0]
        return base + u'.result.log'

    @classmethod
    def _getDevelopPath(cls):
        return cls._getOsEnvironRawAsPath(cls.environ_key_path_develop, cls.path_default_develop)

    @classmethod
    def _getProductPath(cls):
        return cls._getOsEnvironRawAsPath(cls.environ_key_path_product, cls.path_default_product)

    @classmethod
    def _getServerPath(cls):
        if cls._isDevelop():
            return cls._getDevelopPath()
        return cls._getProductPath()

    @classmethod
    def _toPathString(cls, strings, separator):
        if isinstance(strings, (str, unicode)):
            strings = cls.toStringList(strings)

        string = separator.join(strings)
        return string

    @classmethod
    def _setLoadPythonModule(cls, moduleName):
        loader = cls.MOD_pkgutil.find_loader(moduleName)
        if loader:
            return cls.MOD_importlib.import_module(moduleName)

    @classmethod
    def _toHtmlLogFileString(cls, fileString):
        base = cls.MTD_os_path.splitext(fileString)[0]
        return u'{}.log.html'.format(base)

    @classmethod
    def _loadPythonModule(cls, moduleName):
        loader = cls.MOD_pkgutil.find_loader(moduleName)
        if loader:
            return cls.MOD_importlib.import_module(moduleName)

    @classmethod
    def _getQtProgressBar(cls, title, maxValue):
        module = cls._setLoadPythonModule('LxUi.qt.qtCommands')
        if module is not None:
            return module.setProgressWindowShow(title, maxValue)

    @classmethod
    def _setQtProgressBarUpdate(cls, progressBar, text=None):
        if progressBar is not None:
            progressBar.updateProgress(text)

    @classmethod
    def _timetagToChnPrettify(cls, timetag, useMode=0):
        if timetag:
            if cls._getOsFileTimetag(timetag) is not None:
                year = int(timetag[:4])
                month = int(timetag[5:7])
                date = int(timetag[7:9])
                hour = int(timetag[10:12])
                minute = int(timetag[12:14])
                second = int(timetag[15:16])
                if year > 0:
                    timetuple = cls.MOD_datetime.datetime(year=year, month=month, day=date, hour=hour, minute=minute, second=second).timetuple()
                    return cls._timetupleToChnPrettify(timetuple, useMode)
                return u'{0}{0}年{0}月{0}日{0}点分'.format('??')
        return u'无记录'

    @classmethod
    def _getOsFileTimetag(cls, backupFileString):
        lis = cls.MOD_re.findall(cls.def_time_tag_search_string, backupFileString)
        if lis:
            return lis[0]

    @classmethod
    def _getOsFileBackupNameDict(cls, fileString):
        dic = {}
        if fileString:
            directoryName = cls._getOsFileDirectoryName(fileString)
            if cls._isOsDirectoryExist(directoryName):
                backupFilename = cls._toOsFileJoinTimetag(fileString, cls.def_time_tag_search_string)
                stringLis = glob.glob(backupFilename)
                if stringLis:
                    for i in stringLis:
                        dic[cls._getOsFileTimetag(i)] = i.replace('\\', '/')
        return dic

    @classmethod
    def _timestampToChnPrettify(cls, timestamp, useMode=0):
        if isinstance(timestamp, float):
            return cls._timetupleToChnPrettify(cls.MOD_time.localtime(timestamp), useMode)
        else:
            return u'无记录'

    @classmethod
    def _timetupleToChnPrettify(cls, timetuple, useMode=0):
        year, month, date, hour, minute, second, week, dayCount, isDst = timetuple
        if useMode == 0:
            timetuple_ = cls.MOD_time.localtime(cls.MOD_time.time())
            year_, month_, date_, hour_, minute_, second_, week_, dayCount_, isDst_ = timetuple_
            #
            monday = date - week
            monday_ = date_ - week_
            if timetuple_[:1] == timetuple[:1]:
                dateString = u'{}月{}日'.format(str(month).zfill(2), str(date).zfill(2))
                weekString = u''
                subString = u''
                if timetuple_[:2] == timetuple[:2]:
                    if monday_ == monday:
                        dateString = ''
                        weekString = u'{0}'.format(cls.def_time_week_lis[int(week)][0])
                        if date_ == date:
                            subString = u'（今天）'
                        elif date_ == date + 1:
                            subString = u'（昨天）'
                #
                timeString = u'{}点{}分'.format(str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
                #
                string = u'{}{}{} {}'.format(dateString, weekString, subString, timeString)
                return string
            else:
                return u'{}年{}月{}日'.format(str(year).zfill(4), str(month).zfill(2), str(date).zfill(2))
        else:
            dateString = u'{}年{}月{}日'.format(str(year).zfill(4), str(month).zfill(2), str(date).zfill(2))
            timeString = u'{}点{}分{}秒'.format(str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))
            return u'{} {}'.format(dateString, timeString)

    # Log
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


class PathBasic(Basic):
    @classmethod
    def _toTreeViewPathLis(cls, pathString, pathsep):
        def addItem(item):
            if not item in lis:
                lis.append(item)
        #
        def getBranch(subPathString):
            if not subPathString in lis:
                stringLis = subPathString.split(pathsep)
                #
                dataCount = len(stringLis)
                for seq, data in enumerate(stringLis):
                    if data:
                        if seq + 1 < dataCount:
                            subPath = pathsep.join(stringLis[:seq + 1])
                            addItem(subPath)
                #
                addItem(subPathString)
        #
        lis = []
        pathStringLis = cls.toStringList(pathString)
        for i in pathStringLis:
            # Debug add root
            if not i.startswith(pathsep):
                i = pathsep + i
            #
            getBranch(i)
        return lis

    @classmethod
    def _getTreeViewBuildDic(cls, pathString, pathsep):
        def addItem(item):
            if not item in lis:
                lis.append(item)
        #
        def getRootBranch(subPathString, nodeArray):
            node = nodeArray[-1]
            dic.setdefault((None, None), []).append((node, subPathString))
        #
        def getBranch(subPathString, nodeArray):
            parent = nodeArray[-2]
            parentPath = pathsep.join(nodeArray[:-1])
            node = nodeArray[-1]
            addItem(((parent, parentPath), (node, subPathString)))
        #
        def getMain():
            # Get Dict
            pathStringLis = cls.toStringList(pathString)
            if pathStringLis:
                for i in pathStringLis:
                    nodeArray = i.split(pathsep)
                    isRoot = len(nodeArray) == 2
                    # Filter is Root
                    if isRoot:
                        getRootBranch(i, nodeArray)
                    else:
                        getBranch(i, nodeArray)
            # Reduce Dict
            if lis:
                covertToDict_(dic, lis)

        def covertToDict_(dic_, lis_):
            [dic_.setdefault(p, []).append(c) for p, c in lis_]
        #
        lis = []
        dic = cls.CLS_dic_order()
        #
        getMain()
        return dic

    @classmethod
    def _getNamespace(cls, pathString, nodeSep, namespaceSep):
        if namespaceSep in pathString:
            return namespaceSep.join(pathString.split(nodeSep)[-1].split(namespaceSep)[:-1])
        return ''

    @classmethod
    def _getName(cls, pathString, nodeSep, namespaceSep):
        return pathString.split(nodeSep)[-1].split(namespaceSep)[-1]

    @classmethod
    def _getAttributeName(cls, attrString, attributeSep):
        return attributeSep.join(attrString.split(attributeSep)[1:])


class FileBasic(Basic):
    @classmethod
    def isExist(cls, fileString):
        return cls._isOsFileExist(fileString)

    @classmethod
    def createDirectory(cls, fileString):
        cls._setOsFileDirectoryCreate(fileString)

    @classmethod
    def isSame(cls, fileString, targetFileString):
        return cls._isOsSameFile(fileString, targetFileString)

    @classmethod
    def copyTo(cls, fileString, targetFileString, force=True):
        if cls.isExist(fileString):
            cls._setOsFileCopy(fileString, targetFileString, force)

    @classmethod
    def backupTo(cls, fileString, backupFileString, timetag=None):
        if cls.isExist(fileString):
            cls._setOsFileBackup(fileString, backupFileString, timetag)

    @classmethod
    def renameTo(cls, fileString, newFileName):
        cls._setOsFileRename(fileString, newFileName)

    @classmethod
    def renameTo_(cls, fileString, newFileString):
        cls._setOsFileRename_(fileString, newFileString)

    @classmethod
    def remove(cls, fileString):
        cls._setOsPathRemove(fileString)

    @classmethod
    def open(cls, fileString):
        cls._setOsFileOpen(fileString)

    @classmethod
    def openDirectory(cls, fileString):
        if cls._isOsFileExist(fileString):
            directoryString = cls._getOsFileDirectoryName(fileString)
            cls._setOsDirectoryOpen(directoryString)

    @classmethod
    def openAsTemporary(cls, fileString, temporaryFileString):
        if cls._isOsFileExist(fileString):
            timestamp = str(cls._getOsFileMtimestamp(fileString))
            if cls._isOsFileExist(temporaryFileString):
                tempTimestamp = str(cls._getOsFileMtimestamp(temporaryFileString))
            else:
                tempTimestamp = None

            if not timestamp == tempTimestamp:
                cls._setOsFileCopy(fileString, temporaryFileString)
            #
            cls._setOsFileOpen(temporaryFileString)

    @classmethod
    def openAsBackup(cls, fileString):
        pass

    @classmethod
    def isFileTimeChanged(cls, fileString, targetFileString):
        return cls._isOsFileTimeChanged(fileString, targetFileString)

    @classmethod
    def mtimestamp(cls, fileString):
        return cls._getOsFileMtimestamp(fileString)

    @classmethod
    def mtimetag(cls, fileString):
        return cls._getOsFileMtimetag(fileString)

    @classmethod
    def mtimeChnPrettify(cls, fileString, useMode=0):
        return cls._timestampToChnPrettify(cls._getOsFileMtimestamp(fileString), useMode)

    @classmethod
    def temporaryFilename(cls, fileString, timetag=None):
        return cls._getOsFileTemporaryName(fileString, timetag)

    @classmethod
    def backupFilename(cls, fileString, timetag=None, useMode=0):
        return cls._toOsFileJoinTimetag(fileString, timetag, useMode)

    @classmethod
    def infoJsonFilename(cls, fileString):
        return cls._toOsFileInfoJsonFileString(fileString)

    @classmethod
    def resultFilename(cls, fileString):
        return cls._toOsFileResultFileString(fileString)

    @classmethod
    def backupNameDict(cls, fileString):
        return cls._getOsFileBackupNameDict(fileString)

    @classmethod
    def toJoinTimetag(cls, fileString, timetag=None, useMode=0):
        return cls._toOsFileJoinTimetag(fileString, timetag, useMode)

    @classmethod
    def findTimetag(cls, fileString):
        return cls._getOsFileTimetag(fileString)

    @classmethod
    def infoDict(cls, fileString):
        return cls._infoDict(fileString)

    @classmethod
    def productInfoDict(cls, fileString, stage=None, description=None, note=None):
        dic = cls._infoDict(fileString)
        dic[cls.STR_key_stage] = stage
        dic[cls.STR_key_description] = description
        dic[cls.STR_key_note] = note
        return dic


class _EnvironString(str):
    def __init__(self, value):
        self._value = value

        self._key = ''
        self._parent = None

    def _add(self, value):
        if self._value:
            lis = [i.lstrip().rstrip() for i in self._value.split(Basic.MOD_os.pathsep)]
            lowerLis = [i.lstrip().rstrip().lower() for i in self._value.lower().split(Basic.MOD_os.pathsep)]
            if value.lower() not in lowerLis:
                lis.append(value)
                self._value = Basic.MOD_os.pathsep.join(lis)
        else:
            self._value = value

    def _sub(self, value):
        if self._value:
            lis = [i.lstrip().rstrip() for i in self._value.split(Basic.MOD_os.pathsep)]
            lowerLis = [i.lstrip().rstrip().lower() for i in self._value.lower().split(Basic.MOD_os.pathsep)]
            if value.lower() in lowerLis:
                i = lowerLis.index(value.lower())
                lis.remove(lis[i])
                self._value = Basic.MOD_os.pathsep.join(lis)

    def _update(self):
        Basic.MOD_os.environ[self._key] = self._value

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

        Basic.MOD_os.environ[self._key] = self._value

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
        lis = [i.replace('\\', '/') for i in self._value.split(Basic.MOD_os.pathsep)]
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

        value = self.MOD_os.environ.get(key, '')
        if not key in self.__dict__:
            str_ = _EnvironString(value)
            str_.key = key
            str_.parent = self

            self.__dict__[key] = str_
            return str_

    @classmethod
    def isExist(cls, key, value):
        value_ = cls.MOD_os.environ.get(key)
        if value_ is not None:
            lowerLis = [i.lstrip().rstrip().lower() for i in value_.split(cls.MOD_os.pathsep)]
            return value.lower() in lowerLis
        return False


class SystemPath(Basic):
    def __init__(self):
        pass
    @classmethod
    def isExist(cls, pathString):
        pathLowerLis = [i.replace('\\', '/').lower() for i in cls.MOD_sys.path]
        if pathString.lower() in pathLowerLis:
            return True
        return False

    @classmethod
    def add(cls, pathString):
        if cls.isExist(pathString) is False:
            cls.MOD_sys.path.insert(0, pathString)

    @classmethod
    def remove(cls, pathString):
        if cls.isExist(pathString) is True:
            cls.MOD_sys.path.remove(pathString)

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
        lis = [i.replace('\\', '/') for i in self.MOD_sys.path]
        lis.sort()
        return '\r\n'.join(lis)
