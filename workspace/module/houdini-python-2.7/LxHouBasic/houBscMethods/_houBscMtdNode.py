# coding:utf-8
# noinspection PyUnresolvedReferences
import hou

from .. import houBscCfg


class HouObj(houBscCfg.HouBscUtility):
    DEF_ho__typepath_subnet = u'Object/subnet'
    DEF_ho__typepath_geo = u'Object/geo'

    @classmethod
    def findAllChildNodeObjPaths(cls, *args, **kwargs):
        def getKwargsFnc_(kwargs_):
            _includeArg = None
            if kwargs_:
                if u'include' in kwargs_:
                    _ = kwargs_[u'include']
                    if isinstance(_, (str, unicode)):
                        _includeArg = [_]
                    elif isinstance(_, (tuple, list)):
                        _includeArg = list(_)
            return _includeArg

        def addFnc_(lis_, nodeObj_, includeArg_):
            if includeArg_ is not None:
                if nodeObj_.type().nameWithCategory() in includeArg_:
                    lis.append(nodeObj_)
            else:
                lis_.append(nodeObj_)

        def rcsFnc_(lis_, nodeObj_, includeArg_):
            addFnc_(lis_, nodeObj_, includeArg_)
            _childObjList = nodeObj_.children()
            for _nodeObj in _childObjList:
                rcsFnc_(lis_, _nodeObj, includeArg_)

        lis = []
        _ = args[0]
        if isinstance(_, (str, unicode)):
            nodeObj = hou.node(_)
        else:
            nodeObj = args[0]
        includeArg = getKwargsFnc_(kwargs)
        rcsFnc_(lis, nodeObj, includeArg)
        return lis


class HouShaderNetworkSop(houBscCfg.HouBscUtility):
    @classmethod
    def _fnc__get_shader_path_str_(cls, *args):
        _, keywordStr = args
        if isinstance(_, (str, unicode)):
            n = cls.MOD_hou.node(_)
        else:
            n = _
        connections = n.inputConnections()
        if connections:
            for i in connections:
                if i.outputName() == keywordStr:
                    return i.inputNode().path()

    @classmethod
    def _fnc__get_surface_shader_path_str_(cls, nodepathString):
        return cls._fnc__get_shader_path_str_(
            nodepathString, u'surface'
        )

    @classmethod
    def _fnc__get_displacement_shader_path_str_(cls, nodepathString):
        return cls._fnc__get_shader_path_str_(
            nodepathString, u'displacement'
        )

    @classmethod
    def _fnc__get_volume_shader_path_str_(cls, nodepathString):
        return cls._fnc__get_shader_path_str_(
            nodepathString, u'volume'
        )

    @classmethod
    def _fnc__get_shader_port_raw_list_(cls, *args):
        _ = args[0]
        if isinstance(_, (str, unicode)):
            n = cls.MOD_hou.node(_)
        else:
            n = _
        for i in n.inputNames():
            print i


class HoGeometryObj(houBscCfg.HouBscUtility):
    @classmethod
    def findAllShapes(cls, *args, **kwargs):
        pass
