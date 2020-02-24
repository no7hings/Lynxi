# coding:utf-8
from LxScheme import shmConfigure, shmObjCore

from LxScheme.shmObjects import _shmObjSystem, _shmObjFile, _shmObjRaw


class Prs_Project(shmObjCore.Abc_ShmPreset):
    CLS_system = _shmObjSystem.Sys_PltLanguage
    CLS_path_file = _shmObjFile.Fle_PrsUser
    CLS_raw = _shmObjRaw.Raw_Preset

    object_category = shmConfigure.Utility.Category_Project

    def __init__(self, *args):
        self._initAbcPreset(*args)
