# coding:utf-8
import os

import copy


class DatUtility(object):
    MOD_os = os
    MOD_copy = copy

    DEF_dat__datatype_pathsep = u'/'

    DEF_dat__node_namespace_pathsep = u':'
    DEF_dat__node_type_pathsep = u'/'
    DEF_dat__node_pathsep = u'/'
    DEF_dat__node_port_pathsep = u'.'

    DEF_dat__node_variant_pathsep = u'@'

    DEF_dat__file_extsep = u'.'
    DEF_dat__file_pathsep = u'/'

    DEF_dat__raw_strsep = u','
    DEF_dat__compraw_strsep = u', '

    DEF_dat__datatype__boolean = u'boolean'
    DEF_dat__datatype__booleanarray = u'booleanarray'

    DEF_dat__datatype__Integer = u'integer'
    DEF_dat__datatype__integerarray = u'integerarray'

    DEF_dat__datatype__float = u'float'
    DEF_dat__datatype__floatarray = u'floatarray'
    DEF_dat__datatype__float2 = u'float2'
    DEF_dat__datatype__float2array = u'float2array'
    DEF_dat__datatype__float3 = u'float3'
    DEF_dat__datatype__float3array = u'float3array'
    DEF_dat__datatype__float4 = u'float4'
    DEF_dat__datatype__float4array = u'float4array'

    DEF_dat__datatype__color2 = u'color2'
    DEF_dat__datatype__color2array = u'color2array'
    DEF_dat__datatype__color3 = u'color3'
    DEF_dat__datatype__color3array = u'color3array'
    DEF_dat__datatype__color4 = u'color4'
    DEF_dat__datatype__color4array = u'color4array'

    DEF_dat__datatype__vector2 = u'vector2'
    DEF_dat__datatype__vector2array = u'vector2array'
    DEF_dat__datatype__vector3 = u'vector3'
    DEF_dat__datatype__vector3array = u'vector3array'
    DEF_dat__datatype__vector4 = u'vector4'
    DEF_dat__datatype__vector4array = u'vector4array'

    DEF_dat__datatype__matrix33 = u'matrix33'
    DEF_dat__datatype__matrix44 = u'matrix44'

    DEF_dat__datatype__string = u'string'
    DEF_dat__datatype__stringarray = u'stringarray'

    DEF_dat__datatype__category_digit = u'digit'
    DEF_dat__datatype__category_digitarray = u'digitarray'
    DEF_dat__datatype__category_digit2array = u'digit2array'
    DEF_dat__datatype__category_digit3array = u'digit3array'
    DEF_dat__datatype__category_digit4array = u'digit4array'

    DEF_dat__datatype__role__color = u'color'
    DEF_dat__datatype__role__vector = u'vector'
    DEF_dat__datatype__role__matrix = u'matrix'

    DEF_dat__datatype__category_dict = {
        DEF_dat__datatype__color2: DEF_dat__datatype__float2,
        DEF_dat__datatype__color2array: DEF_dat__datatype__float2array,
        DEF_dat__datatype__color3: DEF_dat__datatype__float3,
        DEF_dat__datatype__color3array: DEF_dat__datatype__float3array,
        DEF_dat__datatype__color4: DEF_dat__datatype__float4,
        DEF_dat__datatype__color4array: DEF_dat__datatype__float4array,

        DEF_dat__datatype__vector2: DEF_dat__datatype__float2,
        DEF_dat__datatype__vector2array: DEF_dat__datatype__float2array,
        DEF_dat__datatype__vector3: DEF_dat__datatype__float3,
        DEF_dat__datatype__vector3array: DEF_dat__datatype__float3array,
        DEF_dat__datatype__vector4: DEF_dat__datatype__float4,
        DEF_dat__datatype__vector4array: DEF_dat__datatype__float4array
    }
    DEF_dat__datatype__role_dict = {
        DEF_dat__datatype__color2: DEF_dat__datatype__role__color,
        DEF_dat__datatype__color2array: DEF_dat__datatype__role__color,
        DEF_dat__datatype__color3: DEF_dat__datatype__role__color,
        DEF_dat__datatype__color3array: DEF_dat__datatype__role__color,
        DEF_dat__datatype__color4: DEF_dat__datatype__role__color,
        DEF_dat__datatype__color4array: DEF_dat__datatype__role__color,

        DEF_dat__datatype__vector2: DEF_dat__datatype__role__vector,
        DEF_dat__datatype__vector2array: DEF_dat__datatype__role__vector,
        DEF_dat__datatype__vector3: DEF_dat__datatype__role__vector,
        DEF_dat__datatype__vector3array: DEF_dat__datatype__role__vector,
        DEF_dat__datatype__vector4: DEF_dat__datatype__role__vector,
        DEF_dat__datatype__vector4array: DEF_dat__datatype__role__vector
    }

    DEF_dat__datatype__rawtype_pattern_dict = {
        DEF_dat__datatype__float: float,
        DEF_dat__datatype__floatarray: (list, float),
        DEF_dat__datatype__float2array: (list, tuple, float),
        DEF_dat__datatype__float3array: (list, tuple, float),
        DEF_dat__datatype__float4array: (list, tuple, float)
    }
    DEF_dat__datatype__rawsize_pattern_dict = {
        DEF_dat__datatype__float: 1,
        DEF_dat__datatype__floatarray: (float(u'inf'), 1),
        DEF_dat__datatype__float2array: (float(u'inf'), 2, 1),
        DEF_dat__datatype__float3array: (float(u'inf'), 3, 1),
        DEF_dat__datatype__float4array: (float(u'inf'), 4, 1)
    }


class DatDatatype(object):
    boolean = DatUtility.DEF_dat__datatype__boolean
    booleanarray = DatUtility.DEF_dat__datatype__booleanarray

    integer = DatUtility.DEF_dat__datatype__Integer
    integerarray = DatUtility.DEF_dat__datatype__integerarray

    float = DatUtility.DEF_dat__datatype__float
    floatarray = DatUtility.DEF_dat__datatype__floatarray
    float2 = DatUtility.DEF_dat__datatype__float2
    float2array = DatUtility.DEF_dat__datatype__float2array
    float3 = DatUtility.DEF_dat__datatype__float3
    float3array = DatUtility.DEF_dat__datatype__float3array
    float4 = DatUtility.DEF_dat__datatype__float4
    float4array = DatUtility.DEF_dat__datatype__float4array

    color2 = DatUtility.DEF_dat__datatype__color2
    color2array = DatUtility.DEF_dat__datatype__color2array
    color3 = DatUtility.DEF_dat__datatype__color3
    color3array = DatUtility.DEF_dat__datatype__color3array
    color4 = DatUtility.DEF_dat__datatype__color4
    color4array = DatUtility.DEF_dat__datatype__color4array

    vector2 = DatUtility.DEF_dat__datatype__vector2
    vector2array = DatUtility.DEF_dat__datatype__vector2array
    vector3 = DatUtility.DEF_dat__datatype__vector3
    vector3array = DatUtility.DEF_dat__datatype__vector3array
    vector4 = DatUtility.DEF_dat__datatype__vector4
    vector4array = DatUtility.DEF_dat__datatype__vector4array

    matrix33 = DatUtility.DEF_dat__datatype__matrix33
    matrix44 = DatUtility.DEF_dat__datatype__matrix44

    string = DatUtility.DEF_dat__datatype__string
    stringarray = DatUtility.DEF_dat__datatype__stringarray
