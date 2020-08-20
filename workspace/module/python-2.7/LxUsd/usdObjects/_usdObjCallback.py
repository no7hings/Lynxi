# coding:utf-8
from .. import usdObjAbs


class ObjSceneLoader(usdObjAbs.AbsUsdObjSceneLoader):
    def __init__(self, *args, **kwargs):
        self._initAbsUsdObjScene(*args, **kwargs)


GRH_OBJ_SCENE_LOADER = ObjSceneLoader()
