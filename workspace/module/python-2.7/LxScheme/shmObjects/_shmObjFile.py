# coding:utf-8
from LxBasic import bscObjects

from .. import shmObjAbs

from . import _shmObjPath


class Fle_RscBin(shmObjAbs.AbsShmFile):
    CLS_shm__directory = _shmObjPath.OsDirectory
    CLS_shm__file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbsShmFile(args, 'config', '.json')

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


class Fle_RscPackage(shmObjAbs.AbsShmFile):
    CLS_shm__directory = _shmObjPath.OsDirectory
    CLS_shm__file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbsShmFile(args, 'config', '.json')

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


class Fle_RscPlug(shmObjAbs.AbsShmFile):
    CLS_shm__directory = _shmObjPath.OsDirectory
    CLS_shm__file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbsShmFile(args, 'config', '.json')

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


class Fle_RscModule(shmObjAbs.AbsShmFile):
    CLS_shm__directory = _shmObjPath.OsDirectory
    CLS_shm__file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbsShmFile(args, 'config', '.json')

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


class Fle_RscScheme(shmObjAbs.AbsShmFile):
    CLS_shm__directory = _shmObjPath.OsDirectory
    CLS_shm__file = bscObjects.OsJsonFile

    def __init__(self, *args):
        self._initAbsShmFile(args, 'config', '.json')

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
