# coding:utf-8
from LxScheme import shmCore, shmAbstract

from LxScheme.shmObjects import _shmObjSystem, _shmObjFile, _shmObjRaw


class Prs_Project(shmAbstract.Abc_Preset):
    SYSTEM_CLS = _shmObjSystem.Sys_PltLanguage
    FILE_CLS = _shmObjFile.Fle_PrsUser
    RAW_CLS = _shmObjRaw.Raw_Preset

    object_category = shmCore.Basic.Category_Project

    def __init__(self, *args):
        self._initAbcPreset(*args)
