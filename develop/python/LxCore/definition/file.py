# coding:utf-8
from LxCore.definition import method, abstract, path


class Fle_BinConfigure(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/bin/{self.pathname}',
            self.Path_Key_Server: u'{self.root.server}/resource/bin/{self.pathname}',
            self.Path_Key_Local: u'{self.root.local}/resource/bin/{self.pathname}',
            self.Path_Key_Develop: u'{self.root.develop}/resource/bin/{self.pathname}',
            self.Path_Key_Product: u'{self.root.product}/resource/bin/{self.pathname}',
            self.Path_Key_Workspace: u'{self.root.product}/workspace/bin/'
        }


class Fle_PackageConfigure(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/package/{self.pathname}',
            self.Path_Key_Server: u'{self.root.server}/resource/package/{self.pathname}',
            self.Path_Key_Local: u'{self.root.local}/resource/package/{self.pathname}',
            self.Path_Key_Develop: u'{self.root.develop}/resource/package/{self.pathname}',
            self.Path_Key_Product: u'{self.root.product}/resource/package/{self.pathname}',
            self.Path_Key_Workspace: u'{self.root.product}/workspace/package/'
        }


class Fle_CfgModule(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/module/{self.pathname}',
            self.Path_Key_Server: u'{self.root.server}/resource/module/{self.pathname}',
            self.Path_Key_Local: u'{self.root.local}/resource/module/{self.pathname}',
            self.Path_Key_Develop: u'{self.root.develop}/resource/module/{self.pathname}',
            self.Path_Key_Product: u'{self.root.product}/resource/module/{self.pathname}',
            self.Path_Key_Workspace: u'{self.root.product}/workspace/module/'
        }


class Fle_SchemeConfigure(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/scheme/{self.pathname}',
            self.Path_Key_Server: u'{self.root.server}/resource/scheme/{self.pathname}',
            self.Path_Key_Local: u'{self.root.local}/resource/scheme/{self.pathname}',
            self.Path_Key_Develop: u'{self.root.develop}/resource/scheme/{self.pathname}',
            self.Path_Key_Product: u'{self.root.product}/resource/scheme/{self.pathname}',
            self.Path_Key_Workspace: u'{self.root.product}/workspace/scheme/'
        }
