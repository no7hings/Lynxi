# coding:utf-8
from LxMaterial import mtlObjects

from LxMaBasic import maBscObjects

from .. import maMtlObjCore

OBJ_dcc_query = mtlObjects.MyaMtlDefCache()


class Geometry(maMtlObjCore.Abc_MyaMtlTrsGeometry):
    CLS_mtl_object = mtlObjects.Geometry
    CLS_mtl_dcc_object = maBscObjects.Geometry

    OBJ_mtl_def_cache = mtlObjects.OBJ_mtl_def_cache
    OBJ_mtl_dcc_def_cache = OBJ_dcc_query

    def __init__(self, *args):
        self._initAbcMyaMtlTrsGeometry(*args)


class Material(maMtlObjCore.Abc_MyaMtlTrsMaterial):
    CLS_mtl_object = mtlObjects.Material
    CLS_mtl_dcc_object = maBscObjects.Material

    OBJ_mtl_def_cache = mtlObjects.OBJ_mtl_def_cache
    OBJ_mtl_dcc_def_cache = OBJ_dcc_query

    def __init__(self, *args):
        self._initAbcMyaMtlTrsMaterial(*args)


class Node(maMtlObjCore.Abc_MyaMtlTrsNode):
    CLS_mtl_object = mtlObjects.Node
    CLS_mtl_dcc_object = maBscObjects.Node

    OBJ_mtl_def_cache = mtlObjects.OBJ_mtl_def_cache
    OBJ_mtl_dcc_def_cache = OBJ_dcc_query

    def __init__(self, *args):
        self._initAbcMyaMtlTrsNode(*args)


class NodeGraph(maMtlObjCore.Abc_MyaMtlTrsNodeGraph):
    CLS_mtl_node_graph = mtlObjects.NodeGraph
    CLS_mtl_dcc_node_graph = maBscObjects.NodeGraph

    CLS_mtl_trs_node = Node

    OBJ_mtl_def_cache = mtlObjects.OBJ_mtl_def_cache
    OBJ_mtl_dcc_def_cache = OBJ_dcc_query

    def __init__(self, *args):
        self._initAbcMyaMtlTrsNodeGraph(*args)


class Shader(maMtlObjCore.Abc_MyaMtlTrsShader):
    CLS_mtl_object = mtlObjects.Shader
    CLS_mtl_dcc_object = maBscObjects.Shader

    CLS_mtl_node_graph = mtlObjects.NodeGraph
    CLS_mtl_dcc_node_graph = maBscObjects.NodeGraph

    CLS_mtl_trs_node_graph = NodeGraph

    OBJ_mtl_def_cache = mtlObjects.OBJ_mtl_def_cache
    OBJ_mtl_dcc_def_cache = OBJ_dcc_query

    def __init__(self, *args):
        self._initAbcMyaMtlTrsShader(*args)
