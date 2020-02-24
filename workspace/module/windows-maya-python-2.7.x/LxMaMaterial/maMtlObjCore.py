# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxMaterial import mtlConfigure, mtlObjects


class Abc_MaMtlBasic(object):
    MOD_maya_cmds = cmds


class Abc_MaMtlNodeDef(object):
    pass


class Abc_MaMtlMaterialDef(Abc_MaMtlBasic):
    def _initAbcMaMtlMaterial(self, categoryString):
        print mtlObjects.NodeDef(categoryString).attributeRaw()

        self._attributeRaw = {}

    def attributeRaw(self):
        pass


