# coding:utf-8
from LxMaterial import mtlObjects

from LxMaBasic import maBscObjects

from .. import maMtlObjCore

OBJ_mtl_dcc_query_cache = mtlObjects.MyaMtlQueryCache()


class Node(maMtlObjCore.Abc_MyaMtlNode):
    CLS_mtl_object = mtlObjects.Node
    CLS_mtl_dcc_object = maBscObjects.Node

    OBJ_mtl_query_cache = mtlObjects.OBJ_mtl_query_cache
    OBJ_mtl_dcc_query_cache = OBJ_mtl_dcc_query_cache

    OBJ_mtl_obj_cache = mtlObjects.OBJ_mtl_obj_cache

    def __init__(self, *args):
        self._initAbcMyaMtlNode(*args)


class NodeGraph(maMtlObjCore.Abc_MyaMtlNodeGraph):
    CLS_mtl_node_graph = mtlObjects.NodeGraph
    CLS_mtl_dcc_node_graph = maBscObjects.NodeGraph

    CLS_mtl_trs_node = Node

    OBJ_mtl_query_cache = mtlObjects.OBJ_mtl_query_cache
    OBJ_mtl_dcc_query_cache = OBJ_mtl_dcc_query_cache

    OBJ_mtl_obj_cache = mtlObjects.OBJ_mtl_obj_cache

    def __init__(self, *args):
        self._initAbcMyaMtlNodeGraph(*args)


class Shader(maMtlObjCore.Abc_MyaMtlShader):
    CLS_mtl_object = mtlObjects.Shader
    CLS_mtl_dcc_object = maBscObjects.Shader

    CLS_mtl_node_graph = mtlObjects.NodeGraph
    CLS_mtl_dcc_node_graph = maBscObjects.NodeGraph

    CLS_mtl_trs_node_graph = NodeGraph

    OBJ_mtl_query_cache = mtlObjects.OBJ_mtl_query_cache
    OBJ_mtl_dcc_query_cache = OBJ_mtl_dcc_query_cache

    OBJ_mtl_obj_cache = mtlObjects.OBJ_mtl_obj_cache

    def __init__(self, *args):
        self._initAbcMyaMtlShader(*args)


class Material(maMtlObjCore.Abc_MyaMtlMaterial):
    CLS_mtl_object = mtlObjects.Material
    CLS_mtl_dcc_object = maBscObjects.Material

    CLS_mtl_trs_shader = Shader

    OBJ_mtl_query_cache = mtlObjects.OBJ_mtl_query_cache
    OBJ_mtl_dcc_query_cache = OBJ_mtl_dcc_query_cache

    OBJ_mtl_obj_cache = mtlObjects.OBJ_mtl_obj_cache

    def __init__(self, *args):
        self._initAbcMyaMtlMaterial(*args)


class Geometry(maMtlObjCore.Abc_MyaMtlGeometry):
    CLS_mtl_object = mtlObjects.Geometry
    CLS_mtl_dcc_object = maBscObjects.Geometry

    CLS_mtl_trs_material = Material

    OBJ_mtl_query_cache = mtlObjects.OBJ_mtl_query_cache
    OBJ_mtl_dcc_query_cache = OBJ_mtl_dcc_query_cache

    OBJ_mtl_obj_cache = mtlObjects.OBJ_mtl_obj_cache

    def __init__(self, *args):
        self._initAbcMyaMtlGeometry(*args)
