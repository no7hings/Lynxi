# coding:utf-8
# noinspection PyUnresolvedReferences
import pxr.Usd

from LxData import datCfg


class UsdUtility(object):
    MOD_pxr_Usd = pxr.Usd
    MOD_pxr_Sdf = pxr.Sdf

    DEF_usd__graphic_name = u'usd'

    DEF_usd__node_namespace_pathsep = u':'
    DEF_usd__node_port_pathsep = u'.'
    DEF_usd__node_pathsep = u'/'

    DEF_usd__node_type_transform = u'Xform'

    DEF_usd__datatype_dict = {
        u'bool': datCfg.DatDatatype.boolean,
        u'bool[]': datCfg.DatDatatype.booleanarray,
        u'int': datCfg.DatDatatype.integer,
        u'int[]': datCfg.DatDatatype.integerarray,
        u'float': datCfg.DatDatatype.float,
        u'float[]': datCfg.DatDatatype.floatarray,
        u'string': datCfg.DatDatatype.string,
        u'string[]': datCfg.DatDatatype.stringarray,

        u'color2f': datCfg.DatDatatype.color2,
        u'color2f[]': datCfg.DatDatatype.color2array,
        u'color3f': datCfg.DatDatatype.color3,
        u'color3f[]': datCfg.DatDatatype.color3array,
        u'color4f': datCfg.DatDatatype.color4,
        u'color4f[]': datCfg.DatDatatype.color4array,

        u'float2': datCfg.DatDatatype.vector2,
        u'float2[]': datCfg.DatDatatype.vector2array,
        u'vector3f': datCfg.DatDatatype.vector3,
        u'vector3f[]': datCfg.DatDatatype.vector3array,
        u'vector4f': datCfg.DatDatatype.vector4,
        u'vector4f[]': datCfg.DatDatatype.vector4array,

        u'matrix3d': datCfg.DatDatatype.matrix33,
        u'matrix4d': datCfg.DatDatatype.matrix44,
    }
