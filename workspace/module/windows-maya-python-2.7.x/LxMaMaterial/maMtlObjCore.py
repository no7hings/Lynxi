# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxMaterial import mtlObjCore


class Abc_MyaMtlBasic(object):
    MOD_maya_cmds = cmds


class Abc_MyaMtlNode(mtlObjCore.Abc_MtlTrsNode):
    def _initAbcMyaMtlNode(self, *args):
        self._initAbcMtlTrsNode(*args)


class Abc_MyaMtlNodeGraph(mtlObjCore.Abc_MtlTrsNodeGraph):
    def _initAbcMyaMtlNodeGraph(self, *args):
        self._initAbcMtlTrsNodeGraph(*args)


class Abc_MyaMtlShader(mtlObjCore.Abc_MtlTrsShader):
    def _initAbcMyaMtlShader(self, *args):
        self._initAbcMtlTrsShader(*args)


class Abc_MyaMtlGeometry(mtlObjCore.Abc_MtlTrsGeometry):
    def _initAbcMyaMtlGeometry(self, *args):
        self._initAbcMtlTrsGeometry(*args)


class Abc_MyaMtlMaterial(mtlObjCore.Abc_MtlTrsMaterial):
    def _initAbcMyaMtlMaterial(self, *args):
        self._initAbcMtlTrsMaterial(*args)


class Abc_MyaMtlLook(mtlObjCore.Abc_MtlTrsLook):
    def _initAbcMyaMtlLook(self, *args):
        self._initAbcMtlTrsLook(*args)


class Abc_MyaMtlFile(mtlObjCore.Abc_MtlTrsFile):
    def _initAbcMyaMtlFile(self, *args):
        self._initAbcMtlTrsFile(*args)


class Abc_MyaAsset(object):
    pass
