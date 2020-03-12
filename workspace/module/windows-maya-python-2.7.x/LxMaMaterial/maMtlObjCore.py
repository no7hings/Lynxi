# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxMaterial import mtlObjCore


class Abc_MyaMtlBasic(object):
    MOD_maya_cmds = cmds


class Abc_MyaMtlTrsGeometry(mtlObjCore.Abc_MtlTrsGeometry):
    def _initAbcMyaMtlTrsGeometry(self, *args):
        self._initAbcMtlTrsGeometry(*args)


class Abc_MyaMtlTrsMaterial(mtlObjCore.Abc_MtlTrsMaterial):
    def _initAbcMyaMtlTrsMaterial(self, *args):
        self._initAbcMtlTrsMaterial(*args)


class Abc_MyaMtlTrsNode(mtlObjCore.Abc_MtlTrsNode):
    def _initAbcMyaMtlTrsNode(self, *args):
        self._initAbcMtlTrsNode(*args)


class Abc_MyaMtlTrsNodeGraph(mtlObjCore.Abc_MtlTrsNodeGraph):
    def _initAbcMyaMtlTrsNodeGraph(self, *args):
        self._initAbcMtlTrsNodeGraph(*args)


class Abc_MyaMtlTrsShader(mtlObjCore.Abc_MtlTrsShader):
    def _initAbcMyaMtlTrsShader(self, *args):
        self._initAbcMtlTrsShader(*args)
