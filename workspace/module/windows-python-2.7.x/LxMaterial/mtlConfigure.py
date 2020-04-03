# coding:utf-8
import os

import re

import collections


class Utility(object):
    MOD_re = re
    CLS_ordered_dict = collections.OrderedDict

    DEF_mtl_data_separator = u','
    DEF_mtl_data_array_separator = u', '

    DEF_mya_node_separator = u'|'
    DEF_mtl_nodename_namesep = u':'
    DEF_mtl_node_pathsep = u'/'
    DEF_mtl_file_pathsep = u'/'
    DEF_mtl_port_pathsep = u'.'

    DEF_mtl_key_category = u'category'
    DEF_mtl_key_type = u'type'

    DEF_mtl_key_port = u'port'
    DEF_mtl_key_mtl_port = u'mtl_port'
    DEF_mtl_key_mtl_portdata = u'mtl_portdata'
    DEF_mtl_key_dcc_port = u'dcc_port'

    DEF_mtl_key_mtl_category = u'mtl_category'
    DEF_mtl_key_mtl_portname = u'mtl_portname'
    DEF_mtl_key_dcc_porttype = u'dcc_porttype'

    DEF_mtl_key_custom_node = u'custom_node'
    DEF_mtl_key_portpath = u'portpath'
    DEF_mtl_key_porttype = u'porttype'
    DEF_mtl_key_portdata = u'portdata'
    DEF_mtl_key_assign = u'assign'
    DEF_mtl_key_parent = u'parent'
    DEF_mtl_key_children = u'children'
    DEF_mtl_key_create_expression = u'create_expression'
    DEF_mtl_key_after_expression = u'after_expression'
    DEF_mtl_key_command = u'command'

    DEF_mtl_key_input = u'input'
    DEF_mtl_key_format = u'format'

    DEF_mtl_keyword_input = u'input'
    DEF_mtl_keyword_input_channel = u'input_channel'
    DEF_mtl_keyword_output = u'output'
    DEF_mtl_keyword_output_channel = u'output_channel'
    DEF_mtl_keyword_property = u'property'
    DEF_mtl_keyword_visibility = u'visibility'

    DEF_mtl_keyword_porttype_uv_0 = u'uv_0'
    DEF_mtl_keyword_porttype_uv_1 = u'uv_1'

    DEF_mtl_category_material = u'material'
    DEF_mtl_maya_category_material = u'shadingEngine'
    DEF_mtl_category_mesh = u'mesh'
    DEF_mtl_maya_category_geometry = u'mesh'

    DEF_mtl_porttype_closure = u'closure'
    DEF_mtl_porttype_shader = u'shader'
    DEF_mtl_porttype_visibility = u'visibility'

    DEF_mtl_porttype_boolean = u'boolean'
    DEF_mtl_porttype_Integer = u'integer'
    DEF_mtl_porttype_integerarray = u'integerarray'
    DEF_mtl_porttype_float = u'float'
    DEF_mtl_porttype_floatarray = u'floatarray'

    DEF_mtl_porttype_color2 = u'color2'
    DEF_mtl_porttype_color2array = u'color2array'
    DEF_mtl_porttype_color3 = u'color3'
    DEF_mtl_porttype_color3array = u'color3array'
    DEF_mtl_porttype_color4 = u'color4'
    DEF_mtl_porttype_color4array = u'color4array'

    DEF_mtl_porttype_vector2 = u'vector2'
    DEF_mtl_porttype_vector2array = u'vector2array'
    DEF_mtl_porttype_vector3 = u'vector3'
    DEF_mtl_porttype_vector3array = u'vector3array'
    DEF_mtl_porttype_vector4 = u'vector4'
    DEF_mtl_porttype_vector4array = u'vector4array'

    DEF_mtl_porttype_matrix33 = u'matrix33'
    DEF_mtl_porttype_matrix44 = u'matrix44'

    DEF_mtl_porttype_string = u'string'
    DEF_mtl_porttype_stringarray = u'stringarray'
    DEF_mtl_porttype_filename = u'filename'
    DEF_mtl_porttype_nodename = u'geomname'
    DEF_mtl_porttype_nodenamearray = u'geomnamearray'

    DEF_mtl_arnold_material_def_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-material.json'
    DEF_mtl_arnold_geometry_def_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-geometry.json'
    DEF_mtl_arnold_node_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-node.json'
    DEF_mtl_arnold_output_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-output.json'
    DEF_mtl_arnold_port_child_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-port_child.json'

    DEF_mtl_maya_arnold_material_def_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-material.json'
    DEF_mtl_maya_arnold_geometry_def_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-geometry.json'
    DEF_mtl_maya_arnold_node_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-node.json'
    DEF_mtl_maya_arnold_port_child_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-port_child.json'
    DEF_mtl_maya_arnold_output_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-output.json'

    DEF_mtl_maya_arnold_custom_category_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-custom_category.json'
    DEF_mtl_maya_arnold_custom_node_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-custom_node.json'
