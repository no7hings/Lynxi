# coding:utf-8
from LxBasic import bscCore

from LxBasic.bscMethods import _bscMtdInterface


class PythonLoader(bscCore.Basic):
    def __init__(self, moduleName):
        self._moduleName = moduleName

    def loadModule(self):
        loader = self.module_pkgutil.find_loader(self._moduleName)
        if loader:
            return self.module_importlib.import_module(self._moduleName)


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
                    modules = [j for j in module.__dict__.values() if isinstance(j, cls.module_types.ModuleType)]
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
            loader = cls.module_pkgutil.find_loader(i)
            if loader:
                recursionFnc_(cls.module_importlib.import_module(i))

        return lis

    @classmethod
    def _setModulesReload(cls, moduleNames):
        count = len(moduleNames)
        progressBar = _bscMtdInterface.If_Progress('Update Python Module(s)', count)
        for i in moduleNames:
            module = PythonLoader(i).loadModule()
            if module:
                nameString = module.__name__
                progressBar.update(nameString)
                if not nameString == '__main__':
                    if hasattr(module, '__file__'):
                        fileString = module.__file__
                        if cls.method_os_path.isfile(fileString):
                            if cls.Enable_Print is True:
                                print '# result >> reload "{}"'.format(nameString)
                            # print '    <{}>'.format(fileString)
                            cls.module_imp.reload(module)
            else:
                progressBar.update()

    def run(self):
        self._setModulesReload(
            self._getModules(
                self.module_sys.modules, self._moduleName
            )
        )


class PythonMessage(bscCore.Basic):
    Enable_Print = True

    def __init__(self):
        pass

    @classmethod
    def _setAddMessage(cls, text):
        print u'@lynxi <{}>'.format(cls._getActivePrettifyTime())
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
            log.writelines(u'<{}> @ {}\n'.format(cls._getActivePrettifyTime(), cls._getUserName()))
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
        self._applicationName = self.method_os_path.basename(self.module_sys.argv[0])

    @property
    def isMaya(self):
        if self._applicationName.lower() in ['maya.exe', 'maya']:
            return True
        return False


class Mtd_Environ(bscCore.Basic):
    @classmethod
    def get(cls, key, failobj=None):
        return cls.module_os.environ.get(key, failobj)

    @classmethod
    def set(cls, key, value):
        cls.module_os.environ[key] = value

    @classmethod
    def getAsList(cls, key):
        if key in cls.module_os.environ:
            return cls.get(key).split(cls.module_os.pathsep)
        return []

