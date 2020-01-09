# coding:utf-8
from LxScheme import shmCore, shmAbstract

from LxScheme.shmObjects import _shmSystem, _shmFile, _shmRaw


class Prs_Project(shmAbstract.Abc_Preset):
    SYSTEM_CLS = _shmSystem.Sys_PltLanguage
    FILE_CLS = _shmFile.Fle_PrsUser
    RAW_CLS = _shmRaw.Raw_Preset

    object_category = shmCore.Basic.Category_Project

    def __init__(self, *args):
        self._initAbcPreset(*args)
