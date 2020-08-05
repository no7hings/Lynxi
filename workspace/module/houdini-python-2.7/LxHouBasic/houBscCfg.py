# coding:utf-8
# noinspection PyUnresolvedReferences
import hou
# noinspection PyUnresolvedReferences
import _alembic_hom_extensions

import re

import collections

from LxData import datCfg

from LxGraphic import grhCfg


class HouBscUtility(object):
    MOD_re = re
    MOD_hou = hou
    MOD_hou_alembic = _alembic_hom_extensions

    CLS_ordered_dict = collections.OrderedDict

    DEF_hou__graphic_name = u'houdini'

    DEF_hou__node_namespace_pathsep = u'::'
    DEF_hou__node_pathsep = u'/'
    DEF_hou__node_port_pathsep = u'/'

    DEF_hou__port_child_dict = {
        u'Base1': u'{portpath}{index}',
        u'XYZW': [
            u'{portpath}x',
            u'{portpath}y',
            u'{portpath}z',
            u'{portpath}w'
        ],
        u'XYWH': [
            u'{portpath}x',
            u'{portpath}y',
            u'{portpath}z',
            u'{portpath}h'
        ],
        u'UVW': [
            u'{portpath}u',
            u'{portpath}v',
            u'{portpath}w'
        ],
        u'RGBA': [
            u'{portpath}r',
            u'{portpath}g',
            u'{portpath}b',
            u'{portpath}a'
        ],
        u'MinMax': [
            u'{portpath}min',
            u'{portpath}max',
        ],
        u'StartEnd': [
            u'{portpath}start',
            u'{portpath}end'
        ],
        u'MaxMin': [
            u'{portpath}max',
            u'{portpath}min'
        ],
        u'BeginEnd': [
            u'{portpath}begin',
            u'{portpath}end'
        ]
    }

    DEF_hou__port_ramp_child_dict = {
        u'Color': [
            {
                grhCfg.GrhUtility.DEF_grh__key_format: u'{portpath}_position',
                grhCfg.GrhUtility.DEF_grh__key_porttype: u'floatarray'
            },
            {
                grhCfg.GrhUtility.DEF_grh__key_format: u'{portpath}_color',
                grhCfg.GrhUtility.DEF_grh__key_porttype: u'color3array'
            },
            {
                grhCfg.GrhUtility.DEF_grh__key_format: u'{portpath}_interpolation',
                grhCfg.GrhUtility.DEF_grh__key_porttype: u'integerarray'
            }
        ],
        u'Float': [
            {
                grhCfg.GrhUtility.DEF_grh__key_format: u'{portpath}_position',
                grhCfg.GrhUtility.DEF_grh__key_porttype: u'floatarray'
            },
            {
                grhCfg.GrhUtility.DEF_grh__key_format: u'{portpath}_value',
                grhCfg.GrhUtility.DEF_grh__key_porttype: u'floatarray'
            },
            {
                grhCfg.GrhUtility.DEF_grh__key_format: u'{portpath}_interpolation',
                grhCfg.GrhUtility.DEF_grh__key_porttype: u'integerarray'
            }
        ]
    }

    DEF_hou__port_datatype_dict_0 = {
        u'Int': datCfg.DatDatatype.integer,
        u'Float': datCfg.DatDatatype.float,
        u'Toggle': datCfg.DatDatatype.boolean,
        u'String': datCfg.DatDatatype.string,
        # enumeration
        u'Menu': datCfg.DatDatatype.string,
        # ramp
        u'Ramp': u'ramp'
    }

    DEF_hou__port_datatype_dict_1 = {
        u'Int': datCfg.DatDatatype.integer,
        u'Float': datCfg.DatDatatype.float,
        u'String': datCfg.DatDatatype.string,
        u'Ramp': u'ramp'
    }

    DEF_hou__port_datatype_dict_2 = {
        u'Base1': u'{porttype}array',
        u'XYZW': u'vector{portsize}',
        u'XYWH': u'vector{portsize}',
        u'UVW': u'vector{portsize}',
        u'RGBA': u'color{portsize}',
        u'MinMax': u'vector{portsize}',
        u'StartEnd': u'vector{portsize}',
        u'MaxMin': u'vector{portsize}',
        u'BeginEnd': u'vector{portsize}'
    }

    DEF_hou__compound_port_datatype_dict_0 = {
        u'Int': datCfg.DatDatatype.integerarray,
        u'Float': datCfg.DatDatatype.floatarray,
        u'Toggle': datCfg.DatDatatype.integerarray,
        u'String': datCfg.DatDatatype.stringarray,
        # enumeration
        u'Menu': datCfg.DatDatatype.stringarray,
        # ramp
        u'Ramp': u'ramp'
    }

    DEF_hou__port_ramp_interpolation_dict = {
        u'Constant': 0,
        u'Linear': 1,
        u'CatmullRom': 2,
        u'MonotoneCubic': 3,
        u'Bezier': 4,
        u'BSpline': 5,
        u'Hermite': 6
    }

    DEF_hou__port_otport_dict_0 = {
        u'shader': {
            grhCfg.GrhPortQuery.portpath: u'shader',
            grhCfg.GrhPortQuery.porttype: u'closure',
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },

        u'boolean': {
            grhCfg.GrhPortQuery.portpath: u'boolean',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.boolean,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'int': {
            grhCfg.GrhPortQuery.portpath: u'int',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.integer,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'float': {
            grhCfg.GrhPortQuery.portpath: u'float',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.float,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'string': {
            grhCfg.GrhPortQuery.portpath: u'string',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.string,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },

        u'rgb': {
            grhCfg.GrhPortQuery.portpath: u'rgb',
            grhCfg.GrhPortQuery.porttype: u'color3',
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [
                u'r', u'g', u'b'
            ],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'rgba': {
            grhCfg.GrhPortQuery.portpath: u'rgba',
            grhCfg.GrhPortQuery.porttype: u'color4',
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [
                u'r', u'g', u'b', u'a'
            ],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },

        u'vector': {
            grhCfg.GrhPortQuery.portpath: u'vector',
            grhCfg.GrhPortQuery.porttype: u'vector3',
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [
                u'x', u'y', u'z'
            ],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'matrix': {
            grhCfg.GrhPortQuery.portpath: u'matrix',
            grhCfg.GrhPortQuery.porttype: u'matrix44',
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        }
    }

    DEF_hou__port_otport_dict_1 = {
        u'r': {
            grhCfg.GrhPortQuery.portpath: u'r',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.float,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'g': {
            grhCfg.GrhPortQuery.portpath: u'g',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.float,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'b': {
            grhCfg.GrhPortQuery.portpath: u'b',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.float,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'a': {
            grhCfg.GrhPortQuery.portpath: u'a',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.float,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },

        u'x': {
            grhCfg.GrhPortQuery.portpath: u'x',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.float,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'y': {
            grhCfg.GrhPortQuery.portpath: u'y',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.float,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
        u'z': {
            grhCfg.GrhPortQuery.portpath: u'z',
            grhCfg.GrhPortQuery.porttype: datCfg.DatDatatype.float,
            grhCfg.GrhPortQuery.assign: grhCfg.GrhPortAssignQuery.otport,
            grhCfg.GrhPortQuery.children: [],
            grhCfg.GrhPortQuery.parent: None,
            grhCfg.GrhPortQuery.portraw: None
        },
    }
