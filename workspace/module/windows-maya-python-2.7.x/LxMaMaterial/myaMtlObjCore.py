# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

from LxMaterial import mtlObjAbs


class Abc_MyaMtlBasic(object):
    MOD_maya_cmds = cmds


class Abc_MyaTranslator(mtlObjAbs.Abc_MtlDccTranslator):
    def _initAbcMyaTranslator(self, *args):
        self._initAbcMtlDccTranslator(*args)


class Abc_MyaMtlNode(mtlObjAbs.Abc_MtlTrsNode):
    def _initAbcMyaMtlNode(self, *args):
        self._initAbcMtlTrsNode(*args)


class Abc_MyaMtlGeometry(mtlObjAbs.Abc_MtlTrsNode):
    def _initAbcMyaMtlGeometry(self, *args):
        self._initAbcMtlTrsNode(*args)


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
