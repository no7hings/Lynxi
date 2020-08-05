# coding:utf-8
from LxBasic import bscObjects

from ..import houBscCfg


class HoAlembicFile(houBscCfg.HouBscUtility):
    @classmethod
    def getDagTreeObj(cls, *args):
        def rscFnc_(pathStr_, typeStr_, childRaws_):
            if dagTreeObj.hasNode(pathStr_) is False:
                dagTreeObj.addNode(pathStr_)
                dagTreeObj.node(pathStr_).setType(typeStr_)
            #
            for i in childRaws_:
                _nameStr, _typeStr, _childRaws = i
                if pathStr_ == nodesep:
                    _pathStr = nodesep + _nameStr
                else:
                    _pathStr = pathStr_ + nodesep + _nameStr
                rscFnc_(_pathStr, _typeStr, _childRaws)

        dagTreeObj = bscObjects.DagTree()

        nodesep = '/'
        _ = args[0]
        if isinstance(_, (str, unicode)):
            filepathStrList = [_]
        elif isinstance(_, (tuple, list)):
            filepathStrList = _
        else:
            raise

        for filepathStr in filepathStrList:
            raw = cls.MOD_hou_alembic.alembicGetSceneHierarchy(filepathStr, "/")
            _, _, childRaws = raw
            rscFnc_('/', 'cxform', childRaws)

        return dagTreeObj
