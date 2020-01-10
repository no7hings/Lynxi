# coding:utf-8
from LxBasic import bscCore


class PyLoader(bscCore.Basic):
    @classmethod
    def loadModule(cls, moduleName):
        return cls._loadPythonModule(moduleName)


class PyReloader(bscCore.Basic):
    Enable_Print = False

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
        progressBar = cls._getQtProgressBar('Update Python Module(s)', count)
        for i in moduleNames:
            module = PyLoader.loadModule(i)
            if module:
                nameString = module.__name__
                if not nameString == '__main__':
                    if hasattr(module, '__file__'):
                        fileString = module.__file__
                        if cls.mtd_os_path.isfile(fileString):
                            if cls.Enable_Print is True:
                                print '# result >> reload "{}"'.format(nameString)
                                print '    <{}>'.format(fileString)
                            cls.module_imp.reload(module)

                cls._setQtProgressBarUpdate(progressBar, nameString)
            else:
                cls._setQtProgressBarUpdate(progressBar)

    @classmethod
    def setPrintEnable(cls, boolean):
        cls.Enable_Print = boolean

    @classmethod
    def loadModule(cls, moduleName):
        cls._setModulesReload(
            cls._getModules(
                cls.module_sys.modules, moduleName
            )
        )


class PyMessage(bscCore.Basic):
    Enable_Print = True

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

    @classmethod
    def trace(cls, text):
        if cls.isEnable() is True:
            cls._setAddMessage(text)

    @classmethod
    def traceResult(cls, text):
        cls.trace(
            u'''@result {}'''.format(text)
        )

    @classmethod
    def traceWarning(cls, text):
        cls.trace(
            u'''@warning {}'''.format(text)
        )

    @classmethod
    def traceError(cls, text):
        cls.trace(
            u'''@error {}'''.format(text)
        )
