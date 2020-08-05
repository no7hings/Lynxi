# coding:utf-8
import os


class Usd2mtxUtility(object):
    MOD_os = os

    DEF_usd2mtx__material_file = MOD_os.path.dirname(__file__) + '/.data/usd_1.0-arnold_5.1.1-material.json'
    DEF_usd2mtx__geometry_file = MOD_os.path.dirname(__file__) + '/.data/usd_1.0-arnold_5.1.1-geometry.json'
    DEF_usd2mtx__node_file = MOD_os.path.dirname(__file__) + '/.data/usd_1.0-arnold_5.1.1-node.json'
    DEF_usd2mtx_port_child_defs_file = MOD_os.path.dirname(__file__) + '/.data/usd_1.0-arnold_5.1.1-port_child.json'
    DEF_usd2mtx_output_defs_file = MOD_os.path.dirname(__file__) + '/.data/usd_1.0-arnold_5.1.1-output.json'

    DEF_usd2mtx_custom_category_file = MOD_os.path.dirname(
        __file__) + '/.data/usd_1.0-arnold_5.1.1-custom_category.json'
    DEF_usd2mtx_custom_node_file = MOD_os.path.dirname(__file__) + '/.data/usd_1.0-arnold_5.1.1-custom_node.json'
