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

    path_method = os.path

    copy_method = shutil

    json_method = json

    environ_key_path_develop = 'LYNXI_DEVELOP_PATH'
    path_default_develop = 'e:/myworkspace/td/lynxi'

    environ_key_path_product = 'LYNXI_PATH'
    path_default_product = 'e:/myworkspace/td/lynxi'

    environ_key_enable_develop = 'LYNXI_DEVELOP'

    @classmethod
    def _getOsEnvironValue(cls, environKeyString):
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
        if cls.path_method.exists(directoryString) is False:
            cls.os_method.makedirs(directoryString)

    @classmethod
    def _setCreateFileDirectory(cls, fileString):
        directoryString = cls.path_method.dirname(fileString)
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
        data = cls._getOsEnvironValue(key)
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


class Py_Loader(object):
    def __init__(self, moduleName):
        self._moduleName = moduleName

    def loadModule(self):
        loader = pkgutil.find_loader(self._moduleName)
        if loader:
            return importlib.import_module(self._moduleName)


class Py_Reload(object):
    Enable_Print = False

    def __init__(self, moduleName):
        self._moduleName = moduleName

    @classmethod
    def setPrintEnable(cls, boolean):
        cls.Enable_Print = boolean

    @staticmethod
    def _getMethod(moduleNames, filterModuleName=None):
        def filterFnc_(moduleName, keyword):
            if keyword is not None:
                if isinstance(keyword, tuple) or isinstance(keyword, list):
                    for k in keyword:
                        if moduleName.startswith(k):
                            return True
                    return False
                else:
                    return moduleName.startswith(keyword)
            return True

        def recursionFnc_(module, child=None):
            moduleName = module.__name__

            if filterFnc_(moduleName, filterModuleName) is True:
                if not moduleName in lis:
                    modules = [j for j in module.__dict__.values() if isinstance(j, types.ModuleType)]
                    if modules:
                        if not moduleName in lis:
                            lis.append(moduleName)

                        for m in modules:
                            recursionFnc_(m, child=module)
                    else:
                        if not moduleName in lis:
                            lis.insert(0, moduleName)

                if child is not None:
                    moduleIndex = lis.index(moduleName)
                    childName = child.__name__
                    childIndex = lis.index(childName)
                    if moduleIndex > childIndex:
                        lis.remove(childName)
                        lis.insert(moduleIndex, childName)

        lis = []

        for i in moduleNames:
            loader = pkgutil.find_loader(i)
            if loader:
                recursionFnc_(importlib.import_module(i))

        return lis

    @classmethod
    def _setMethod(cls, moduleNames):
        count = len(moduleNames)
        progressBar = If_Progress('Update Python Module(s)', count)
        for i in moduleNames:
            module = Py_Loader(i).loadModule()
            if module:
                nameString = module.__name__
                progressBar.update(nameString)
                if not nameString == '__main__':
                    if hasattr(module, '__file__'):
                        fileString = module.__file__
                        if os.path.isfile(fileString):
                            if cls.Enable_Print is True:
                                print '# result >> reload "{}"'.format(nameString)
                            # print '    <{}>'.format(fileString)
                            imp.reload(module)
            else:
                progressBar.update()

    def run(self):
        self._setMethod(self._getMethod(sys.modules, self._moduleName))


class Py_Message(Basic):
    Lynxi_Message_Enable = True

    def __init__(self):
        pass

    @classmethod
    def setEnable(cls, boolean):
        cls.Lynxi_Message_Enable = boolean

    @classmethod
    def isEnable(cls):
        return cls.Lynxi_Message_Enable

    def trace(self, text):
        if self.isEnable() is True:
            print u'# Lynxi <{}>'.format(self._getActiveViewTime())
            print u'    {}'.format(text)

    def traceResult(self, text):
        self.trace(
            u'''# Result {}'''.format(text)
        )

    def traceWarning(self, text):
        self.trace(
            u'''# Warning {}'''.format(text)
        )

    def traceError(self, text):
        self.trace(
            u'''# Error {}'''.format(text)
        )


class Py_Log(Basic):
    def __init__(self):
        self._serverRootString = self._getServerPath()

    @classmethod
    def _addLogMethod(cls, text, logFileString):
        cls._setCreateFileDirectory(logFileString)
        with open(logFileString, 'a') as log:
            log.writelines(u'{} @ {}\n'.format(cls._getActiveViewTime(), cls._getUserName()))
            log.writelines(u'{}\n'.format(text))
            log.close()

    @property
    def directoryString(self):
        return u'{}/.log'.format(self._serverRootString)

    @property
    def exceptionFile(self):
        return u'{}/{}.exception.log'.format(
            self.directoryString, self._getActiveDatetag()
        )

    @property
    def errorFile(self):
        return u'{}/{}.error.log'.format(
            self.directoryString, self._getActiveDatetag()
        )

    @property
    def resultFile(self):
        return u'{}/{}.result.log'.format(
            self.directoryString, self._getActiveDatetag()
        )

    def addException(self, text):
        self._addLogMethod(
            text,
            self.exceptionFile
        )

    def addError(self, text):
        self._addLogMethod(
            text,
            self.errorFile
        )

    def addResult(self, text):
        print self.resultFile
        self._addLogMethod(
            text,
            self.resultFile
        )


class If_Progress(object):
    module_full_path_name = 'LxUi.qt.qtProgress'

    def __init__(self, explain, maxValue):
        self._progressBar = self.__loadUi(explain, maxValue)

    @classmethod
    def __loadUi(cls, explain, maxValue):
        module = Py_Loader(cls.module_full_path_name).loadModule()
        if module is not None:
            return module.viewSubProgress(explain, maxValue)

    def update(self, subExplain=None):
        if self._progressBar is not None:
            self._progressBar.updateProgress(subExplain)


class If_Message(object):
    module_full_path_name = 'LxUi.qt.qtTip'

    def __init__(self, text, keyword=None):
        self._tip = self.__loadUi(text, keyword)

    @classmethod
    def __loadUi(cls, text, keyword):
        module = Py_Loader(cls.module_full_path_name).loadModule()
        if module is not None:
            return module.viewMessage(text, keyword)


class If_Tip(object):
    module_full_path_name = 'LxUi.qt.qtTip'

    def __init__(self, title, text):
        self._tip = self.__loadUi(title, text)

    @classmethod
    def __loadUi(cls, title, text):
        module = Py_Loader(cls.module_full_path_name).loadModule()
        if module is not None:
            return module.viewTip(title, text)

    def add(self, text):
        pass
