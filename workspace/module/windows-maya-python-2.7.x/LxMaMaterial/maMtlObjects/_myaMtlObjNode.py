# coding:utf-8
from LxMaterial import mtlObjects

from LxMaBasic import maBscObjects

from ..import myaMtlObjCore

from ..maMtlObjects import _myaMtlObjQuery

OBJ_mtl_trs_query_cache = _myaMtlObjQuery.TrsObjQueryCache()


class Translator(myaMtlObjCore.Abc_MyaTranslator):
    OBJ_mtl_trs_query_cache = OBJ_mtl_trs_query_cache

    def __init__(self, *args):
        self._initAbcMyaTranslator(*args)


class Node(myaMtlObjCore.Abc_MyaMtlNode):
    CLS_mtl_object = mtlObjects.Node
    CLS_mtl_dcc_object = maBscObjects.Node

    CLS_mtl_translator = Translator

    OBJ_mtl_trs_query_cache = OBJ_mtl_trs_query_cache

    OBJ_grh_obj_cache = mtlObjects.OBJ_grh_obj_cache_
    OBJ_mtl_trs_obj_cache = mtlObjects.OBJ_grh_trs_obj_cache_

    def __init__(self, *args):
        self._initAbcMyaMtlNode(*args)


class Geometry(myaMtlObjCore.Abc_MyaMtlGeometry):
    CLS_mtl_object = mtlObjects.Node
    CLS_mtl_dcc_object = maBscObjects.Geometry

    CLS_mtl_translator = Translator

    OBJ_mtl_trs_query_cache = OBJ_mtl_trs_query_cache

    OBJ_grh_obj_cache = mtlObjects.OBJ_grh_obj_cache_
    OBJ_mtl_trs_obj_cache = mtlObjects.OBJ_grh_trs_obj_cache_

    def __init__(self, *args):
        self._initAbcMyaMtlGeometry(*args)


class ShaderProxy(myaMtlObjCore.Abc_MyaMtlShaderProxy):
    CLS_mtl_node_proxy = mtlObjects.ShaderProxy

    CLS_mtl_trs_node = Node

    def __init__(self, *args):
        self._initAbcMyaMtlShaderProxy(*args)


class MaterialProxy(myaMtlObjCore.Abc_MyaMtlMaterialProxy):
    CLS_mtl_node_proxy = mtlObjects.MaterialProxy

    CLS_mtl_trs_node = Node

    CLS_mtl_trs_shader_proxy = ShaderProxy

    VAR_mtl_dcc_shader_portname_list = [
        [u'aiSurfaceShader', u'surfaceShader'],
        u'displacementShader',
        [u'aiVolumeShader', u'volumeShader']
    ]

    def __init__(self, *args):
        self._initAbcMyaMtlMaterialProxy(*args)


class GeometryProxy(myaMtlObjCore.Abc_MyaMtlGeometryProxy):
    CLS_mtl_node_proxy = mtlObjects.GeometryProxy

    CLS_mtl_trs_node = Geometry

    CLS_mtl_trs_material_proxy = MaterialProxy

    def __init__(self, *args):
        self._initAbcMyaMtlGeometryProxy(*args)
