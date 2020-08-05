# coding:utf-8
from LxUsd.usdObjects import _usdObjCallback


def loadScene(*args):
    objSceneObj = _usdObjCallback.ObjSceneLoader(*args)
    _usdObjCallback.__dict__['GRH_OBJ_SCENE_LOADER'] = objSceneObj
    return objSceneObj
