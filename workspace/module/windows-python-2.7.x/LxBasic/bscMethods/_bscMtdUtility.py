# coding:utf-8
from LxBasic import bscCore


class PythonLoader(bscCore.Basic):
    def __init__(self, moduleName):
        self._moduleName = moduleName

    def loadModule(self):
        loader = self.pkgutil_method.find_loader(self._moduleName)
        if loader:
            return self.importlib_method.import_module(self._moduleName)


class PythonReloader(bscCore.Basic):
    Enable_Print = False

    def __init__(self, moduleName):
        self._moduleName = moduleName

    @classmethod
    def setPrintEnable(cls, boolean):
        cls.Enable_Print = boolean

    @classmethod
    def _getModules(cls, moduleNames, filterModuleName=None):
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
                    modules = [j for j in module.__dict__.values() if isinstance(j, cls.types_method.ModuleType)]
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
            loader = cls.pkgutil_method.find_loader(i)
            if loader:
                recursionFnc_(cls.importlib_method.import_module(i))

        return lis

    @classmethod
    def _setModulesReload(cls, moduleNames):
        count = len(moduleNames)
        progressBar = If_Progress('Update Python Module(s)', count)
        for i in moduleNames:
            module = PythonLoader(i).loadModule()
            if module:
                nameString = module.__name__
                progressBar.update(nameString)
                if not nameString == '__main__':
                    if hasattr(module, '__file__'):
                        fileString = module.__file__
                        if cls.os_path_method.isfile(fileString):
                            if cls.Enable_Print is True:
                                print '# result >> reload "{}"'.format(nameString)
                            # print '    <{}>'.format(fileString)
                            cls.imp_method.reload(module)
            else:
                progressBar.update()

    def run(self):
        self._setModulesReload(
            self._getModules(
                self.sys_method.modules, self._moduleName
            )
        )


class PythonMessage(bscCore.Basic):
    Enable_Print = True

    def __init__(self):
        pass

    @classmethod
    def _setAddMessage(cls, text):
        print u'@lynxi <{}>'.format(cls._getActiveViewTime())
        print u'    {}'.format(text)

    @classmethod
    def setEnable(cls, boolean):
        cls.Enable_Print = boolean

    @classmethod
    def isEnable(cls):
        return cls.Enable_Print

    def trace(self, text):
        if self.isEnable() is True:
            self._setAddMessage(text)

    def traceResult(self, text):
        self.trace(
            u'''@result {}'''.format(text)
        )

    def traceWarning(self, text):
        self.trace(
            u'''@warning {}'''.format(text)
        )

    def traceError(self, text):
        self.trace(
            u'''@error {}'''.format(text)
        )


class PythonLog(bscCore.Basic):
    def __init__(self):
        self._serverRootString = self._getServerPath()

    @classmethod
    def _setAddLog(cls, text, logFileString):
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
        self._setAddLog(
            text,
            self.exceptionFile
        )

    def addError(self, text):
        self._setAddLog(
            text,
            self.errorFile
        )

    def addResult(self, text):
        print self.resultFile
        self._setAddLog(
            text,
            self.resultFile
        )


class PythonApplication(bscCore.Basic):
    def __init__(self):
        self._applicationName = self.os_path_method.basename(self.sys_method.argv[0])

    @property
    def isMaya(self):
        if self._applicationName.lower() in ['maya.exe', 'maya']:
            return True
        return False


class If_Progress(object):
    module_fullpath_name = 'LxUi.qt.qtCommands'

    def __init__(self, explain, maxValue):
        self._progressBar = self.__loadUi(explain, maxValue)

    @classmethod
    def __loadUi(cls, explain, maxValue):
        module = PythonLoader(cls.module_fullpath_name).loadModule()
        if module is not None:
            return module.setProgressWindowShow(explain, maxValue)

    def update(self, subExplain=None):
        if self._progressBar is not None:
            self._progressBar.updateProgress(subExplain)


class If_Message(object):
    module_fullpath_name = 'LxUi.qt.qtCommands'

    def __init__(self, text, keyword=None):
        self._ui = self.__loadUi(text, keyword)

    @property
    def ui(self):
        return self._ui

    @classmethod
    def __loadUi(cls, text, keyword):
        module = PythonLoader(cls.module_fullpath_name).loadModule()
        if module is not None:
            return module.setMessageWindowShow(text, keyword)


class If_Tip(object):
    module_fullpath_name = 'LxUi.qt.qtCommands'

    def __init__(self, title, text):
        self._ui = self.__loadUi(title, text)

    @property
    def ui(self):
        return self._ui

    @classmethod
    def __loadUi(cls, title, text):
        module = PythonLoader(cls.module_fullpath_name).loadModule()
        if module is not None:
            return module.setTipWindowShow(title, text)

    def add(self, text):
        self._ui.addHtml(text)
