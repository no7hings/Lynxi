# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxGraphic import grhObjAbs

from LxMaterial import mtlObjAbs


class Abc_MyaMtlBasic(object):
    MOD_maya_cmds = cmds


class Abs_MyaNodeTranslator(grhObjAbs.Abs_GrhNodeTranslator):
    def _initAbsMyaNodeTranslator(self, *args):
        self._initAbsGrhNodeTranslator(*args)


class Abc_MyaMtlNode(grhObjAbs.Abs_GrhTrsNode):
    def _initAbcMyaMtlNode(self, *args):
        self._initAbsGrhTrsNode(*args)


class Abc_MyaMtlGeometry(grhObjAbs.Abs_GrhTrsNode):
    def _initAbcMyaMtlGeometry(self, *args):
        self._initAbsGrhTrsNode(*args)


class Abc_MyaMtlMaterialProxy(mtlObjAbs.Abc_MtlTrsMaterialProxy):
    def _initAbcMyaMtlMaterialProxy(self, *args):
        self._initAbcMtlTrsMaterialProxy(*args)


class Abc_MyaMtlGeometryProxy(mtlObjAbs.Abc_MtlTrsGeometryProxy):
    def _initAbcMyaMtlGeometryProxy(self, *args):
        self._initAbcMtlTrsGeometryProxy(*args)


class Abc_MyaMtlShaderProxy(mtlObjAbs.Abc_MtlTrsShaderProxy):
    def _initAbcMyaMtlShaderProxy(self, *args):
        self._initAbcMtlTrsShaderProxy(*args)


class Abc_MyaMtlLook(mtlObjAbs.Abc_MtlTrsLook):
    def _initAbcMyaMtlLook(self, *args):
        self._initAbcMtlTrsLook(*args)


class Abc_MyaMtlFile(mtlObjAbs.Abc_MtlTrsFile):
    def _initAbcMyaMtlFile(self, *args):
        self._initAbcMtlTrsFile(*args)


class Abc_MyaAsset(object):
    pass
