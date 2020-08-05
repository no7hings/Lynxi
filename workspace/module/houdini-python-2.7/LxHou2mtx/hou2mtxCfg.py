# coding:utf-8
import os
# noinspection PyUnresolvedReferences
import hou


class Hou2mtxUtility(object):
    MOD_os = os
    MOD_hou = hou

    DEF_usd2mtx__material_file = MOD_os.path.dirname(__file__) + '/.data/houdini_18.0-htoa_5.1.1-material.json'
    DEF_usd2mtx__geometry_file = MOD_os.path.dirname(__file__) + '/.data/houdini_18.0-htoa_5.1.1-geometry.json'
    DEF_usd2mtx__node_file = MOD_os.path.dirname(__file__) + '/.data/houdini_18.0-htoa_5.1.1-node.json'
