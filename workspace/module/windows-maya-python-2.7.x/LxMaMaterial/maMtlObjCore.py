# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxMaterial import mtlObjCore


class Abc_MaMtlBasic(object):
    MOD_maya_cmds = cmds


class Abc_MaMtlGeometry(mtlObjCore.Abc_DccMtlGeometry):
    def _initAbcMaMtlGeometry(self, *args):
        self._initAbcDccMtlGeometry(*args)


class Abc_MaMtlMaterial(mtlObjCore.Abc_DccMtlMaterial):
    def _initAbcMaMtlMaterial(self, *args):
        self._initAbcDccMtlMaterial(*args)


class Abc_MaMtlNode(mtlObjCore.Abc_DccMtlNode):
    def _initAbcMaMtlNode(self, *args):
        self._initAbcDccMtlNode(*args)
