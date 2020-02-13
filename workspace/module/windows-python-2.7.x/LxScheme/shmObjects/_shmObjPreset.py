# coding:utf-8
from LxScheme import shmCore, shmObjAbstract

from LxScheme.shmObjects import _shmObjSystem, _shmObjFile, _shmObjRaw


class Prs_Project(shmObjAbstract.Abc_Preset):
    CLS_system = _shmObjSystem.Sys_PltLanguage
    CLS_path_file = _shmObjFile.Fle_PrsUser
    CLS_raw = _shmObjRaw.Raw_Preset

    object_category = shmCore.Basic.Category_Project

    def __init__(self, *args):
        self._initAbcPreset(*args)
