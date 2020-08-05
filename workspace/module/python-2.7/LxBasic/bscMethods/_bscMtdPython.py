# coding:utf-8
from LxBasic import bscMtdCore


class __PyMethod__(bscMtdCore.Mtd_BscUtility):
    @classmethod
    def _py__get_module_exist_(cls, moduleNameStr):
        moduleDict = cls.MOD_sys.modules
        if moduleNameStr in moduleDict:
            module = moduleDict[moduleNameStr]
            if isinstance(module, cls.MOD_types.ModuleType):
                if getattr(module, u'__path__', None) is not None:
                    return True
        return False


class PyLoader(__PyMethod__):
    @classmethod
    def load(cls, moduleName):
        return cls._bsc_mtd__set_python_module_load_(moduleName)

    @classmethod
    def loadFile(cls, filepathStr):
        moduleDirectoryStr = bscMtdCore.Mtd_BscFile.dirname(filepathStr)
        moduleNameStr = bscMtdCore.Mtd_BscFile.name(filepathStr)
        fn_, path, desc = cls.MOD_imp.find_module(
            moduleNameStr,
            [moduleDirectoryStr]
        )
        return cls.MOD_imp.load_module(moduleNameStr, fn_, path, desc)

    @classmethod
    def reload(cls, moduleName):
        return cls._bsc_mtd__set_python_module_reload_(moduleName)


class PyReloader(__PyMethod__):
    @classmethod
    def _getModuleLis(cls, moduleNameStrList, filterModuleName=None):
        def fltFnc_(moduleName_, filterModuleName_):
            if filterModuleName_ is not None:
                if isinstance(filterModuleName_, (tuple, list)):
                    for _moduleName in filterModuleName_:
                        if moduleName_.startswith(_moduleName):
                            return True
                    return False
                return moduleName_.startswith(filterModuleName_)
            return True

        def rcsFnc_(module_, childModule_=None):
            _moduleName = module_.__name__
            if fltFnc_(_moduleName, filterModuleName) is True:
                if _moduleName not in lis:
                    _childModules = [j for j in module_.__dict__.values() if isinstance(j, cls.MOD_types.ModuleType)]
                    if _childModules:
                        if _moduleName not in lis:
                            lis.append(_moduleName)

                        for _childModule in _childModules:
                            rcsFnc_(_childModule, childModule_=module_)
                    # top module
                    else:
                        if _moduleName not in lis:
                            lis.insert(0, _moduleName)

                if childModule_ is not None:
                    _moduleIndex = lis.index(_moduleName)
                    _childModuleName = childModule_.__name__
                    _childModuleIndex = lis.index(_childModuleName)
                    if _moduleIndex > _childModuleIndex:
                        lis.remove(_childModuleName)
                        lis.insert(_moduleIndex, _childModuleName)

        lis = []
        for moduleNameStr in moduleNameStrList:
            if fltFnc_(moduleNameStr, filterModuleName) is True:
                if cls.MOD_pkgutil.find_loader(moduleNameStr) is not None:
                    rcsFnc_(
                        cls.MOD_importlib.import_module(moduleNameStr)
                    )

        return lis

    @classmethod
    def _setModulesReload(cls, moduleNameStrList):
        for moduleNameStr in moduleNameStrList:
            module = PyLoader.load(moduleNameStr)
            if module is not None:
                moduleNameStr = module.__name__
                if not moduleNameStr == '__main__':
                    if hasattr(module, '__file__'):
                        filepathStr = module.__file__
                        if cls.MTD_os_path.isfile(filepathStr):
                            if cls._isTraceEnable() is True:
                                cls._setAddResult('reload module "{}" > "{}"'.format(moduleNameStr, filepathStr))
                                # print u'reload <module = {}>'.format(moduleNameStr)
                                # print u'    <file = {}>'.format(filepathStr)
                            cls.MOD_imp.reload(module)

    @classmethod
    def reload(cls, filterModuleNameArg):
        cls._setModulesReload(
            cls._getModuleLis(
                cls.MOD_sys.modules, filterModuleNameArg
            )
        )


class PyMessage(__PyMethod__):
    Enable_Print = True

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
        if cls.isEnable() is True:
            cls._setAddResult(text)

    @classmethod
    def traceWarning(cls, text):
        if cls.isEnable() is True:
            cls._setAddWarning(text)

    @classmethod
    def traceError(cls, text):
        if cls.isEnable() is True:
            cls._setAddError(text)
