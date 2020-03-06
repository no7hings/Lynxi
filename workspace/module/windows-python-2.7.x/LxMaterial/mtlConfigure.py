# coding:utf-8
import os

import collections


class Utility(object):
    CLS_ordered_dict = collections.OrderedDict

    DEF_mtl_data_separator = u','
    DEF_mtl_data_array_separator = u', '

    DEF_mya_node_separator = u'|'
    DEF_mtl_namespace_separator = u':'
    DEF_mtl_node_separator = u'/'
    DEF_mtl_file_separator = u'/'
    DEF_mtl_port_separator = u'.'

    DEF_mtl_key_category_string = u'categoryString'
    DEF_mtl_key_type = u'type'

    DEF_mtl_key_port = u'port'
    DEF_mtl_key_dcc_portname = u'dccPortname'
    DEF_mtl_key_portname = u'portname'
    DEF_mtl_key_porttype = u'porttype'
    DEF_mtl_key_portdata = u'portdata'
    DEF_mtl_key_assign = u'assign'
    DEF_mtl_key_parent = u'parent'

    DEF_mtl_key_input = u'input'
    DEF_mtl_key_format = u'format'
    DEF_mtl_key_target = u'target'

    DEF_mtl_keyword_input = u'input'
    DEF_mtl_keyword_output = u'output'
    DEF_mtl_keyword_channel = u'channel'
    DEF_mtl_keyword_property = u'property'
    DEF_mtl_keyword_visibility = u'visibility'

    DEF_mtl_category_material = u'material'
    DEF_mtl_maya_category_material = u'shadingEngine'
    DEF_mtl_category_geometry = u'geometry'
    DEF_mtl_maya_category_geometry = u'mesh'

    DEF_mtl_datatype_closure = u'closure'

    DEF_mtl_datatype_boolean = u'boolean'
    DEF_mtl_datatype_Integer = u'integer'
    DEF_mtl_datatype_integer_array = u'integerarray'
    DEF_mtl_datatype_float = u'float'
    DEF_mtl_datatype_float_array = u'floatarray'

    DEF_mtl_datatype_color2 = u'color2'
    DEF_mtl_datatype_color2_array = u'color2array'
    DEF_mtl_datatype_color3 = u'color3'
    DEF_mtl_datatype_color3_array = u'color3array'
    DEF_mtl_datatype_color4 = u'color4'
    DEF_mtl_datatype_color4_array = u'color4array'

    DEF_mtl_datatype_vector2 = u'vector2'
    DEF_mtl_datatype_vector2_array = u'vector2array'
    DEF_mtl_datatype_vector3 = u'vector3'
    DEF_mtl_datatype_vector3_array = u'vector3array'
    DEF_mtl_datatype_vector4 = u'vector4'
    DEF_mtl_datatype_vector4_array = u'vector4array'

    DEF_mtl_datatype_matrix33 = u'matrix33'
    DEF_mtl_datatype_matrix44 = u'matrix44'

    DEF_mtl_datatype_string = u'string'
    DEF_mtl_datatype_string_array = u'stringarray'
    DEF_mtl_datatype_file_name = u'filename'
    DEF_mtl_datatype_geometry_name = u'geomname'
    DEF_mtl_datatype_geometry_name_array = u'geomnamearray'

    DEF_mtl_arnold_material_def_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-material_def.json'
    DEF_mtl_arnold_geometry_def_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-geometry_def.json'
    DEF_mtl_arnold_node_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-node_defs.json'
    DEF_mtl_arnold_output_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-output_defs.json'
    DEF_mtl_arnold_port_child_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-port_child_defs.json'

    DEF_mtl_maya_arnold_material_def_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-material_def.json'
    DEF_mtl_maya_arnold_geometry_def_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-geometry_def.json'
    DEF_mtl_maya_arnold_node_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-node_defs.json'
    DEF_mtl_maya_arnold_port_child_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-port_child_defs.json'
    DEF_mtl_maya_arnold_output_defs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-output_defs.json'
