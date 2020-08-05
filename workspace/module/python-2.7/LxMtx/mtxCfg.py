# coding:utf-8
import os

import re

import collections


class MtxUtility(object):
    DEF_mtx___graphic_name = u'material'

    MOD_re = re
    CLS_ordered_dict = collections.OrderedDict

    DEF_mtx__data_separator = u','
    DEF_mtx__data_array_separator = u', '

    DEF_mya_node_pathsep = u'|'
    DEF_mtx__namespace_pathsep = u':'
    DEF_mtx__node_pathsep = u'/'
    DEF_mtx__file_pathsep = u'/'
    DEF_mtx__node_port_pathsep = u'.'

    DEF_mtx__category_material = u'material'
    DEF_mtx__maya_category_material = u'shadingEngine'
    DEF_mtx__category_mesh = u'mesh'
    DEF_mtx__maya_category_geometry = u'mesh'

    DEF_mtx__datatype__closure = u'closure'
    DEF_mtx__datatype__shader = u'shader'
    DEF_mtx__datatype__visibility = u'visibility'

    DEF_mtx__datatype__boolean = u'boolean'
    DEF_mtx__datatype__booleanarray = u'booleanarray'

    DEF_mtx__datatype__Integer = u'integer'
    DEF_mtx__datatype__integerarray = u'integerarray'
    DEF_mtx__datatype__float = u'float'
    DEF_mtx__datatype__floatarray = u'floatarray'

    DEF_mtx__datatype__string = u'string'
    DEF_mtx__datatype__stringarray = u'stringarray'

    DEF_mtx__datatype__color2 = u'color2'
    DEF_mtx__datatype__color2array = u'color2array'
    DEF_mtx__datatype__color3 = u'color3'
    DEF_mtx__datatype__color3array = u'color3array'
    DEF_mtx__datatype__color4 = u'color4'
    DEF_mtx__datatype__color4array = u'color4array'

    DEF_mtx__datatype__vector2 = u'vector2'
    DEF_mtx__datatype__vector2array = u'vector2array'
    DEF_mtx__datatype__vector3 = u'vector3'
    DEF_mtx__datatype__vector3array = u'vector3array'
    DEF_mtx__datatype__vector4 = u'vector4'
    DEF_mtx__datatype__vector4array = u'vector4array'

    DEF_mtx__datatype__matrix33 = u'matrix33'
    DEF_mtx__datatype__matrix44 = u'matrix44'

    DEF_mtx__datatype__filename = u'filename'
    DEF_mtx__datatype__geomname = u'geomname'
    DEF_mtx__datatype__geomnamearray = u'geomnamearray'

    DEF_mtx__datatype_member_list = [
        DEF_mtx__datatype__closure,
        DEF_mtx__datatype__shader,
        DEF_mtx__datatype__visibility,

        DEF_mtx__datatype__boolean,

        DEF_mtx__datatype__Integer,
        DEF_mtx__datatype__integerarray,
        DEF_mtx__datatype__float,
        DEF_mtx__datatype__floatarray,

        DEF_mtx__datatype__string,
        DEF_mtx__datatype__stringarray,

        DEF_mtx__datatype__color2,
        DEF_mtx__datatype__color2array,
        DEF_mtx__datatype__color3,
        DEF_mtx__datatype__color3array,
        DEF_mtx__datatype__color4,
        DEF_mtx__datatype__color4array,

        DEF_mtx__datatype__vector2,
        DEF_mtx__datatype__vector2array,
        DEF_mtx__datatype__vector3,
        DEF_mtx__datatype__vector3array,
        DEF_mtx__datatype__vector4,
        DEF_mtx__datatype__vector4array,

        DEF_mtx__datatype__matrix33,
        DEF_mtx__datatype__matrix44,

        DEF_mtx__datatype__filename,
        DEF_mtx__datatype__geomname,
        DEF_mtx__datatype__geomnamearray
    ]

    DEF_mtx__arnold_material_def_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-material.json'
    DEF_mtx__arnold_geometry_def_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-geometry.json'
    DEF_mtx__arnold_node_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-node.json'
    DEF_mtx__arnold_output_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-output.json'
    DEF_mtx__arnold_port_child_defs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-port_child.json'
