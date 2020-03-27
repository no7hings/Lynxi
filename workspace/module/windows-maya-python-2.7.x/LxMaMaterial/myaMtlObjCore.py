# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxMaterial import mtlObjCore


class Abc_MyaMtlBasic(object):
    MOD_maya_cmds = cmds


class Abc_MyaTranslator(mtlObjCore.Abc_MtlDccTranslator):
    def _initAbcMyaTranslator(self, *args):
        self._initAbcMtlDccTranslator(*args)


class Abc_MyaMtlNode(mtlObjCore.Abc_MtlTrsNode):
    def _initAbcMyaMtlNode(self, *args):
        self._initAbcMtlTrsNode(*args)


class Abc_MyaMtlGeometry(mtlObjCore.Abc_MtlTrsNode):
    def _initAbcMyaMtlGeometry(self, *args):
        self._initAbcMtlTrsNode(*args)


class Abc_MyaMtlMaterialProxy(mtlObjCore.Abc_MtlTrsMaterialProxy):
    def _initAbcMyaMtlMaterialProxy(self, *args):
        self._initAbcMtlTrsMaterialProxy(*args)


class Abc_MyaMtlGeometryProxy(mtlObjCore.Abc_MtlTrsGeometryProxy):
    def _initAbcMyaMtlGeometryProxy(self, *args):
        self._initAbcMtlTrsGeometryProxy(*args)


class Abc_MyaMtlShaderProxy(mtlObjCore.Abc_MtlTrsShaderProxy):
    def _initAbcMyaMtlShaderProxy(self, *args):
        self._initAbcMtlTrsShaderProxy(*args)


class Abc_MyaMtlLook(mtlObjCore.Abc_MtlTrsLook):
    def _initAbcMyaMtlLook(self, *args):
        self._initAbcMtlTrsLook(*args)


class Abc_MyaMtlFile(mtlObjCore.Abc_MtlTrsFile):
    def _initAbcMyaMtlFile(self, *args):
        self._initAbcMtlTrsFile(*args)


class Abc_MyaAsset(object):
    pass
