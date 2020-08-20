# coding:utf-8
from LxGraphic import grhCfg

from LxMtx import mtxCfg, mtxObjects

from LxMaBasic import maBscObjects

from .. import ma2mtxObjAbs

from ..ma2mtxObjects import _ma2mtxObjQuery


class ObjTranslator(ma2mtxObjAbs.AbsMa2mtxObjTranslator):
    VAR_grh__obj_translator__channel_convert_dict = {
        mtxCfg.MtxUtility.DEF_mtx__datatype__color3: {
            grhCfg.GrhNodeQuery.typepath: u'float_to_rgb'
        },
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector3: {
            grhCfg.GrhNodeQuery.typepath: u'float_to_rgb'
        },
        mtxCfg.MtxUtility.DEF_mtx__datatype__color4: {
            grhCfg.GrhNodeQuery.typepath: u'float_to_rgba'
        },
        mtxCfg.MtxUtility.DEF_mtx__datatype__vector4: {
            grhCfg.GrhNodeQuery.typepath: u'float_to_rgba'
        },
    }

    VAR_grh__obj_translator__src_node_pathsep = mtxCfg.MtxUtility.DEF_mya_node_pathsep
    VAR_grh__obj_translator__tgt_node_pathsep = mtxCfg.MtxUtility.DEF_mtx__node_pathsep

    def __init__(self, *args):
        self._initAbsMa2mtxObjTranslator(*args)


class Node(ma2mtxObjAbs.AbsMa2mtxNode):
    CLS_grh__trs_node__src_node = maBscObjects.Node
    CLS_grh__trs_node__tgt_node = mtxObjects.Node

    CLS_grh__trs_node__obj_translator = ObjTranslator

    IST_grh__trs_node__obj_query_builder = _ma2mtxObjQuery.GRH_TRS_OBJ_QUERY_BUILDER

    IST_grh__trs_node__obj_cache = _ma2mtxObjQuery.GRH_TRS_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsMa2mtxNode(*args)


class Geometry(ma2mtxObjAbs.AbsMa2mtxGeometry):
    CLS_grh__trs_node__tgt_node = mtxObjects.Node
    CLS_grh__trs_node__src_node = maBscObjects.Geometry

    CLS_grh__trs_node__obj_translator = ObjTranslator

    IST_grh__trs_node__obj_query_builder = _ma2mtxObjQuery.GRH_TRS_OBJ_QUERY_BUILDER

    IST_grh__trs_node__obj_cache = _ma2mtxObjQuery.GRH_TRS_OBJ_QUEUE

    def __init__(self, *args):
        self._initAbsMa2mtxGeometry(*args)


# proxy ************************************************************************************************************** #
class ShaderProxy(ma2mtxObjAbs.AbsMa2mtxShaderProxy):
    CLS_grh__trs_node_proxy__trs_node = Node

    CLS_grh__trs_node_proxy__tgt_node_proxy = mtxObjects.ShaderProxy

    def __init__(self, *args, **kwargs):
        self._initAbsMa2mtxShaderProxy(*args, **kwargs)


class MaterialProxy(ma2mtxObjAbs.AbsMa2mtxMaterialProxy):
    CLS_grh__trs_node_proxy__trs_node = Node

    CLS_grh__trs_node_proxy__tgt_node_proxy = mtxObjects.MaterialProxy

    CLS_grh__trs_input_node_proxy = ShaderProxy

    VAR_grh__trs_src_source_portpath_list = [
        [u'aiSurfaceShader', u'surfaceShader'],
        u'displacementShader',
        [u'aiVolumeShader', u'volumeShader']
    ]

    def __init__(self, *args, **kwargs):
        self._initAbsMa2mtxMaterialProxy(*args, **kwargs)


class GeometryProxy(ma2mtxObjAbs.AbsMa2mtxGeometryProxy):
    CLS_grh__trs_node_proxy__trs_node = Geometry

    CLS_grh__trs_node_proxy__tgt_node_proxy = mtxObjects.GeometryProxy

    CLS_grh__trs_input_node_proxy = MaterialProxy

    def __init__(self, *args, **kwargs):
        self._initAbsMa2mtxGeometryProxy(*args, **kwargs)
