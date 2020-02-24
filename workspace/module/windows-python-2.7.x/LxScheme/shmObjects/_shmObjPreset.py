# coding:utf-8
from LxScheme import shmConfigure, shmObjCore

from LxScheme.shmObjects import _shmObjSystem, _shmObjFile, _shmObjRaw


class Prs_Project(shmObjCore.Abc_ShmPreset):
    CLS_shm_system = _shmObjSystem.Sys_PltLanguage
    CLS_shm_file = _shmObjFile.Fle_PrsUser
    CLS_shm_raw = _shmObjRaw.Raw_Preset

    VAR_shm_object_category = shmConfigure.Utility.Category_Project

    def __init__(self, *args):
        self._initAbcShmPreset(*args)
