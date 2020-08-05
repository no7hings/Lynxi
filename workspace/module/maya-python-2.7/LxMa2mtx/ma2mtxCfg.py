# coding:utf-8
# noinspection PyUnresolvedReferences
from maya import cmds, OpenMaya, OpenMayaUI

import os


class Ma2mtxUtility(object):
    MOD_maya_cmds = cmds
    MOD_maya_api = OpenMaya

    DEF_ma_mtx_material_def_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-material.json'
    DEF_ma_mtx_geometry_def_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-geometry.json'
    DEF_ma_mtx_node_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-node.json'
    DEF_ma_mtx_port_child_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-port_child.json'
    DEF_ma_mtx_output_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-output.json'

    DEF_ma_mtx_custom_category_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-custom_category.json'
    DEF_ma_mtx_custom_node_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-custom_node.json'
