# coding:utf-8
from LxMaterial import mtlMethods, mtlObjects

from LxMaBasic import maBscObjects

from .. import maMtlObjCore


class Geometry(maMtlObjCore.Abc_MaMtlGeometry):
    CLS_mtl_object = mtlObjects.Geometry
    CLS_mtl_dcc_object = maBscObjects.Geometry

    CLS_mtl_dcc_object_def = mtlObjects.MayaGeometryDef

    def __init__(self, *args):
        self._initAbcMaMtlGeometry(*args)


class Material(maMtlObjCore.Abc_MaMtlMaterial):
    CLS_mtl_object = mtlObjects.Material
    CLS_mtl_dcc_object = maBscObjects.Material

    CLS_mtl_dcc_object_def = mtlObjects.MayaGeometryDef

    def __init__(self, *args):
        self._initAbcMaMtlMaterial(*args)


class Node(maMtlObjCore.Abc_MaMtlNode):
    CLS_mtl_object = mtlObjects.Node
    CLS_mtl_dcc_object = maBscObjects.Node

    CLS_mtl_dcc_object_def = mtlObjects.MayaNodeDef

    def __init__(self, *args):
        self._initAbcMaMtlNode(*args)
