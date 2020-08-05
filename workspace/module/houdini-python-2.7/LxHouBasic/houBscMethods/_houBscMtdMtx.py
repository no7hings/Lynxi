# coding:utf-8
from .. import houBscCfg

from . import _houBscMtdNode


class _Cfg(houBscCfg.HouBscUtility):
    DEF_attrname__geometrypath = u'path'
    DEF_attrname__materialpath = u'shop_materialpath'

    DEF_typename__geometry = u'Object/geo'
    DEF_typename__material_assign = u'Sop/material'


class _Fnc(_Cfg):
    @classmethod
    def getInputObjsFnc(cls, *args):
        nodeObj = args[0]
        return nodeObj.inputs()

    @classmethod
    def findInputFnc(cls, *args, **kwargs):
        lis = []
        nodeObj = args[0]
        inputNodeList = cls.getInputObjsFnc(nodeObj)
        for i in inputNodeList:
            nodeObjList = _houBscMtdNode.HouObj.findAllChildNodeObjPaths(
                i, **kwargs
            )
            if nodeObjList:
                lis.extend(nodeObjList)
        return lis

    @classmethod
    def getHipFilepathString(cls):
        return cls.MOD_hou.hipFile.path()

    @classmethod
    def getObjIsVisible(cls, *args):
        pass


# ******************************************************************************************************************** #
class _GeometryObjFnc(_Cfg):
    def __init__(self, *args):
        _ = args[0]
        if isinstance(_, (str, unicode)):
            self._houObj = self.MOD_hou.node(_)
        else:
            self._houObj = _
        self._houGeometry = self._houObj.renderNode().geometry()

    def getGeometry(self):
        return self._houGeometry

    def getPropertyDict(self):
        dic = self.CLS_ordered_dict()
        for p in self._houObj.parms():
            parmNameStr = p.name()
            if parmNameStr.startswith(u'ar_'):
                dic[parmNameStr] = p.eval()
        return dic

    def getGeometryPathStrings(self):
        return _GeometryFnc(self.getGeometry()).getGeometryPathStrings()


class _GeometryFnc(_Cfg):
    def __init__(self, *args):
        self._houGeometry = args[0]

    def getPrim(self, *args):
        return self._houGeometry.prim(args[0])

    def getPrimGroups(self):
        return self._houGeometry.primGroups()

    def getPrimGroup(self, *args):
        return self._houGeometry.findPrimGroup(args[0])

    def getGeometryPathStrings(self):
        houAttr = self._houGeometry.findPrimAttrib(self.DEF_attrname__geometrypath)
        if houAttr is not None:
            return list(houAttr.strings())
        return []

    def getMaterialSops(self):
        houAttr = self._houGeometry.findPrimAttrib(self.DEF_attrname__materialpath)
        if houAttr:
            return [self.MOD_hou.node(i) for i in houAttr.strings()]
        return []


class _PrimGroupFnc(_Cfg):
    def __init__(self, *args):
        self._houPrimGroup = args[0]

    def getPrims(self):
        return self._houPrimGroup.iterPrims()

    def getPrimIndexes(self):
        return [i.number() for i in self.getPrims()]

    def getPrimIndexRange(self):
        prims = self.getPrims()
        if prims:
            return prims[0].number(), prims[-1].number()
        return ()

    def getGeometryPathStrings(self):
        lis = []
        for i in self.getPrims():
            pathStr = i.stringAttribValue(self.DEF_attrname__geometrypath)
            if pathStr not in lis:
                lis.append(pathStr)
        return lis

    def getMaterialSops(self):
        pass


class _PrimFnc(_Cfg):
    def __init__(self, *args):
        self._hoPrim = args[0]

    def getGeometryPathString(self):
        return self._hoPrim.stringAttribValue(self.DEF_attrname__geometrypath)

    def getMaterialSop(self, asString=False):
        rawString = self._hoPrim.stringAttribValue(self.DEF_attrname__materialpath)
        if rawString:
            if asString is True:
                return rawString
            return self.MOD_hou.node(rawString)


# ******************************************************************************************************************** #
class _MaterialSopFnc(_Fnc):
    def __init__(self, *args):
        _ = args[0]
        if isinstance(_, (str, unicode)):
            self._houSop = self.MOD_hou.node(_)
        else:
            self._houSop = args[0]

    def hasGeometry(self):
        geometry = self._houSop.geometry()
        return geometry is not None

    def getMaterialAssignRelationDict(self):
        dic = {}
        geometry = self._houSop.geometry()
        geometryFnc = _GeometryFnc(geometry)
        primGroupList = geometryFnc.getPrimGroups()
        for j in primGroupList:
            primGroupFnc = _PrimGroupFnc(j)
            primIndexRange = primGroupFnc.getPrimIndexRange()
            if primIndexRange:
                startIndex, endIndex = primIndexRange
                primFnc = _PrimFnc(geometryFnc.getPrim(startIndex))
                geometryPathStr = primFnc.getGeometryPathString()
                shaderNetworkSop = primFnc.getMaterialSop()
                if shaderNetworkSop is not None:
                    _ = _houBscMtdNode.HouObj.findAllChildNodeObjPaths(
                        shaderNetworkSop, include=u'Vop/arnold_material'
                    )
                    if _:
                        materialVop = _[0]
                        if geometryPathStr not in dic:
                            dic[geometryPathStr] = materialVop.path()
        return dic


class _AssetFnc(_Fnc):
    def __init__(self, *args):
        _ = args[0]
        if isinstance(_, (str, unicode)):
            self._houObj = self.MOD_hou.node(_)
        else:
            self._houObj = _

    def getGeometryObjs(self):
        return _houBscMtdNode.HouObj.findAllChildNodeObjPaths(
            self._houObj, include=self.DEF_typename__geometry
        )

    def getVisibleGeometryObjs(self):
        return [i for i in self.getGeometryObjs() if i.isObjectDisplayed()]

    def getMaterialAssignSops(self):
        return _houBscMtdNode.HouObj.findAllChildNodeObjPaths(
            self._houObj, include=self.DEF_typename__material_assign
        )

    @classmethod
    def getVirtualRelationDict(cls, *args):
        dic = {}
        geometryObjList = args[0]
        for geometryObj in geometryObjList:
            geometryObjFnc = _GeometryObjFnc(geometryObj)
            geometryPathStrList = geometryObjFnc.getGeometryPathStrings()
            for geometryPathStr in geometryPathStrList:
                dic[geometryPathStr] = geometryObj.path()
        return dic

    @classmethod
    def getMaterialAssignRelationDict(cls, *args):
        return _MaterialSopFnc(*args).getMaterialAssignRelationDict()

    @classmethod
    def getPropertyAssignRelationDict(cls, *args):
        dic = {}
        geometryObjList = args[0]
        for geometryObj in geometryObjList:
            geometryObjFnc = _GeometryObjFnc(geometryObj)
            geometryPathStrList = geometryObjFnc.getGeometryPathStrings()
            for geometryPathStr in geometryPathStrList:
                dic[geometryPathStr] = geometryObjFnc.getPropertyDict()
        return dic
