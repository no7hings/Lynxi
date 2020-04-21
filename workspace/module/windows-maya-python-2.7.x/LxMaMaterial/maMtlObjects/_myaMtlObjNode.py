# coding:utf-8
from LxMaterial import mtlCfg, mtlObjects

from LxMaBasic import maBscObjects

from ..import myaMtlObjCore

from ..maMtlObjects import _myaMtlObjQuery


class NodeTranslator(myaMtlObjCore.Abs_MyaNodeTranslator):
    VAR_mtl_channel_convert_dict = {
        mtlCfg.Utility.DEF_mtl_porttype_color3: {
            u'category': u'float_to_rgb'
        },
        mtlCfg.Utility.DEF_mtl_porttype_vector3: {
            u'category': u'float_to_rgb'
        },
        mtlCfg.Utility.DEF_mtl_porttype_color4: {
            u'category': u'float_to_rgba'
        },
        mtlCfg.Utility.DEF_mtl_porttype_vector4: {
            u'category': u'float_to_rgba'
        },
    }

    VAR_grh_trs_src_node_pathsep = mtlCfg.Utility.DEF_mya_node_pathsep
    VAR_grh_trs_tgt_node_pathsep = mtlCfg.Utility.DEF_mtl_node_pathsep

    def __init__(self, *args):
        self._initAbsMyaNodeTranslator(*args)


class Node(myaMtlObjCore.Abc_MyaMtlNode):
    CLS_grh_trs_node_query = _myaMtlObjQuery.TrsNodeQuery

    CLS_grh_src_node = maBscObjects.Node
    CLS_grh_tgt_node = mtlObjects.Node

    CLS_grh_node_translator = NodeTranslator

    OBJ_grh_trs_obj_cache = _myaMtlObjQuery.GRH_TRS_OBJ_CACHE
    OBJ_grh_src_obj_cache = maBscObjects.GRH_OBJ_CACHE
    OBJ_grh_tgt_obj_cache = mtlObjects.GRH_OBJ_CACHE

    def __init__(self, *args):
        self._initAbcMyaMtlNode(*args)


class Geometry(myaMtlObjCore.Abc_MyaMtlGeometry):
    CLS_grh_trs_node_query = _myaMtlObjQuery.TrsNodeQuery

    CLS_grh_tgt_node = mtlObjects.Node
    CLS_grh_src_node = maBscObjects.Geometry

    CLS_grh_node_translator = NodeTranslator

    OBJ_grh_trs_obj_cache = _myaMtlObjQuery.GRH_TRS_OBJ_CACHE
    OBJ_grh_src_obj_cache = maBscObjects.GRH_OBJ_CACHE
    OBJ_grh_tgt_obj_cache = mtlObjects.GRH_OBJ_CACHE

    def __init__(self, *args):
        self._initAbcMyaMtlGeometry(*args)


# proxy ************************************************************************************************************** #
class ShaderProxy(myaMtlObjCore.Abc_MyaMtlShaderProxy):
    CLS_grh_trs_node = Node

    CLS_grh_tgt_node_proxy = mtlObjects.ShaderProxy

    def __init__(self, *args):
        self._initAbcMyaMtlShaderProxy(*args)


class MaterialProxy(myaMtlObjCore.Abc_MyaMtlMaterialProxy):
    CLS_grh_trs_node = Node

    CLS_grh_tgt_node_proxy = mtlObjects.MaterialProxy

    CLS_grh_trs_shader_proxy = ShaderProxy

    VAR_grh_trs_src_shader_portpath_list = [
        [u'aiSurfaceShader', u'surfaceShader'],
        u'displacementShader',
        [u'aiVolumeShader', u'volumeShader']
    ]

    def __init__(self, *args):
        self._initAbcMyaMtlMaterialProxy(*args)


class GeometryProxy(myaMtlObjCore.Abc_MyaMtlGeometryProxy):
    CLS_grh_trs_node = Geometry

    CLS_grh_tgt_node_proxy = mtlObjects.GeometryProxy

    CLS_grh_trs_material_proxy = MaterialProxy

    def __init__(self, *args):
        self._initAbcMyaMtlGeometryProxy(*args)
