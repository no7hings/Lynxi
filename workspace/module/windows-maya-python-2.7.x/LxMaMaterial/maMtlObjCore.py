# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxMaterial import mtlConfigure, mtlObjects

from LxMaBasic import maBscObjCore


class Abc_MaMtlBasic(object):
    MOD_maya_cmds = cmds


class Abc_MaMtlNode(maBscObjCore.Abc_MaObject):
    pass
