# coding:utf-8
from LxCore import lxConfigure


class ApplicationRoot(lxConfigure._AbcPath):
    ROOT_CLS = lxConfigure.Root

    def __init__(self, *args):
        self._initAbcPath(*args)

        self._overrideFormatString()

    def _overrideFormatString(self):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.root.active}/resource/application',
            self.Attr_Key_Server: u'{self.root.server}/resource/application',
            self.Attr_Key_Local: u'{self.root.local}/resource/application',
            self.Attr_Key_Develop: u'{self.root.develop}/resource/application',
            self.Attr_Key_Product: u'{self.root.product}/resource/application'
        }


class ModuleRoot(lxConfigure._AbcPath):
    ROOT_CLS = lxConfigure.Root

    def __init__(self, *args):
        self._initAbcPath(*args)

        self._overrideFormatString()

    def _overrideFormatString(self):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.root.active}/resource/module',
            self.Attr_Key_Server: u'{self.root.server}/resource/module',
            self.Attr_Key_Local: u'{self.root.local}/resource/module',
            self.Attr_Key_Develop: u'{self.root.develop}/resource/module',
            self.Attr_Key_Product: u'{self.root.product}/resource/module'
        }


class PackageRoot(lxConfigure._AbcPath):
    ROOT_CLS = lxConfigure.Root

    def __init__(self, *args):
        self._initAbcPath(*args)

        self._overrideFormatString()

    def _overrideFormatString(self):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.root.active}/resource/package',
            self.Attr_Key_Server: u'{self.root.server}/resource/package',
            self.Attr_Key_Local: u'{self.root.local}/resource/package',
            self.Attr_Key_Develop: u'{self.root.develop}/resource/package',
            self.Attr_Key_Product: u'{self.root.product}/resource/package'
        }


class AppPlugRoot(lxConfigure._AbcPath):
    ROOT_CLS = lxConfigure.Root

    def __init__(self, *args):
        self._initAbcPath(*args)

        self._overrideFormatString()

    def _overrideFormatString(self):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.root.active}/resource/plug',
            self.Attr_Key_Server: u'{self.root.server}/resource/plug',
            self.Attr_Key_Local: u'{self.root.local}/resource/plug',
            self.Attr_Key_Develop: u'{self.root.develop}/resource/plug',
            self.Attr_Key_Product: u'{self.root.product}/resource/plug'
        }


class SchemeRoot(lxConfigure._AbcPath):
    ROOT_CLS = lxConfigure.Root

    def __init__(self, *args):
        self._initAbcPath(*args)

        self._overrideFormatString()

    def _overrideFormatString(self):
        self._formatStringDic = {
            self.Attr_Key_Active: u'{self.root.active}/resource/scheme',
            self.Attr_Key_Server: u'{self.root.server}/resource/scheme',
            self.Attr_Key_Local: u'{self.root.local}/resource/scheme',
            self.Attr_Key_Develop: u'{self.root.develop}/resource/scheme',
            self.Attr_Key_Product: u'{self.root.product}/resource/scheme'
        }


class ApplicationDirectory(lxConfigure._AbcPath):
    ROOT_CLS = ApplicationRoot

    def __init__(self, *args):
        self._initAbcPath(*args)


class ModuleDirectory(lxConfigure._AbcPath):
    ROOT_CLS = ModuleRoot

    def __init__(self, *args):
        self._initAbcPath(*args)


class PackagePath(lxConfigure._AbcPath):
    ROOT_CLS = PackageRoot

    def __init__(self, *args):
        self._initAbcPath(*args)


class AppPlugPath(lxConfigure._AbcPath):
    ROOT_CLS = AppPlugRoot

    def __init__(self, *args):
        self._initAbcPath(*args)


class SchemePath(lxConfigure._AbcPath):
    ROOT_CLS = SchemeRoot

    def __init__(self, *args):
        self._initAbcPath(*args)
