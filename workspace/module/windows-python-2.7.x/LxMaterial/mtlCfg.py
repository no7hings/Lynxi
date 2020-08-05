# coding:utf-8
import os

import re

import collections


class Utility(object):
    MOD_re = re
    CLS_ordered_dict = collections.OrderedDict

    DEF_mtl_data_separator = u','
    DEF_mtl_data_array_separator = u', '

    DEF_mya_node_pathsep = u'|'
    DEF_mtl_namespace_pathsep = u':'
    DEF_mtl_node_pathsep = u'/'
    DEF_mtl_file_pathsep = u'/'
    DEF_mtl_port_pathsep = u'.'

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
