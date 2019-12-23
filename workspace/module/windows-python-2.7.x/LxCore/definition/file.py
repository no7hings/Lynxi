# coding:utf-8
from LxCore.definition import method, abstract, path


class Fle_ResourcePreset(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args).lower()
        workspaceBaseName = self._toSubNameMethod(*args[:-1]).lower()
        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/' + workspaceBaseName,
        }


class Fle_BinConfigure(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args).lower()
        workspaceBaseName = self._toSubNameMethod(*args[:-1]).lower()
        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/bin/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/bin/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/bin/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/bin/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/bin/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/bin/' + workspaceBaseName,
        }


class Fle_PackageConfigure(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args).lower()
        workspaceBaseName = self._toSubNameMethod(*args[:-1]).lower()
        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/package/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/package/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/package/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/package/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/package/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/package/' + workspaceBaseName,
        }


class Fle_CfgModuleConfigure(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args).lower()
        workspaceBaseName = self._toSubNameMethod(*args[:-1]).lower()
        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/module/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/module/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/module/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/module/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/module/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/module/' + workspaceBaseName,
        }


class Fle_SchemeConfigure(abstract.Abc_File):
    DIRECTORY_CLS = path.Pth_Directory
    METHOD_CLS = method.JsonFile

    def __init__(self, *args):
        self._initAbcFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args).lower()
        workspaceBaseName = self._toSubNameMethod(*args[:-1]).lower()
        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/scheme/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/scheme/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/scheme/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/scheme/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/scheme/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/scheme/' + workspaceBaseName,
        }
