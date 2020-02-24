# coding:utf-8
from LxBasic import bscMtdCore, bscObjects

from LxScheme import shmObjCore

from LxScheme.shmObjects import _shmObjPath


class Fle_RscBin(shmObjCore.Abc_ShmFile):
    CLS_shm_directory = _shmObjPath.OsDirectory
    CLS_shm_file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbcShmFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args)
        workspaceBaseName = self._toSubNameMethod(*args[:-1])

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/bin/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/bin/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/bin/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/bin/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/bin/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/bin/' + workspaceBaseName,
        }


class Fle_RscPackage(shmObjCore.Abc_ShmFile):
    CLS_shm_directory = _shmObjPath.OsDirectory
    CLS_shm_file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbcShmFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args)
        workspaceBaseName = self._toSubNameMethod(*args[:-1])

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/package/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/package/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/package/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/package/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/package/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/package/' + workspaceBaseName,
        }


class Fle_RscPlug(shmObjCore.Abc_ShmFile):
    CLS_shm_directory = _shmObjPath.OsDirectory
    CLS_shm_file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbcShmFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args)
        workspaceBaseName = self._toSubNameMethod(*args[:-1])

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/plug/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/plug/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/plug/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/plug/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/plug/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/plug/' + workspaceBaseName,
        }


class Fle_RscModule(shmObjCore.Abc_ShmFile):
    CLS_shm_directory = _shmObjPath.OsDirectory
    CLS_shm_file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbcShmFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args)
        workspaceBaseName = self._toSubNameMethod(*args[:-1])

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/module/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/module/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/module/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/module/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/module/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/module/' + workspaceBaseName,
        }


class Fle_RscScheme(shmObjCore.Abc_ShmFile):
    CLS_shm_directory = _shmObjPath.OsDirectory
    CLS_shm_file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbcShmFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args)
        workspaceBaseName = self._toSubNameMethod(*args[:-1])

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/scheme/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/scheme/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/scheme/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/scheme/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/scheme/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/scheme/' + workspaceBaseName,
        }


class Fle_RscTool(shmObjCore.Abc_ShmFile):
    CLS_shm_directory = _shmObjPath.OsDirectory
    CLS_shm_file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbcShmFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args)
        workspaceBaseName = self._toSubNameMethod(*args[:-1])

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/resource/tool/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/resource/tool/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/resource/tool/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/resource/tool/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/resource/tool/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/workspace/tool/' + workspaceBaseName,
        }


class Fle_PrsUser(shmObjCore.Abc_ShmFile):
    CLS_shm_directory = _shmObjPath.OsDirectory
    CLS_shm_file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbcShmFile(args, 'config', '.json')

        baseName = self._toSubNameMethod(*args)
        workspaceBaseName = self._toSubNameMethod(*args[:-1])

        self.directory.pathFormatString = {
            self.Path_Key_Active: u'{self.root.active}/preset/' + baseName,
            self.Path_Key_Server: u'{self.root.server}/preset/' + baseName,
            self.Path_Key_Local: u'{self.root.local}/preset/' + baseName,
            self.Path_Key_Develop: u'{self.root.develop}/preset/' + baseName,
            self.Path_Key_Product: u'{self.root.product}/preset/' + baseName,
            self.Path_Key_Workspace: u'{self.root.workspace}/preset/' + workspaceBaseName,
        }
