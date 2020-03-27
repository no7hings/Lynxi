# coding:utf-8


class Utility(object):
    DEF_category_node_covert_dict = {
        'displacementShader': 'range'
    }

    DEF_porttype_covert_dict = {
        'bool': 'boolean',
        'long': 'integer',
        'short': 'integer',
        'float': 'float',
        'double': 'float',
        'byte': 'integer',
        'char': 'string',
        'enum': 'string',
        'doubleAngle': 'float',
        'doubleLinear': 'float',
        'string': 'string',
        'stringArray': 'stringarray',
        'time': 'float',
        'matrix': 'matrix',
        'fltMatrix': 'matrix',

        'long2': None,
        'long3': None,
        'short2': None,
        'short3': None,
        'float2': 'color2',
        'float3': 'color3',
        'double2': 'color2',
        'double3': 'color3',

        'doubleArray': 'floatarray',
        'floatArray': 'floatarray',
        'Int32Array': 'integerarray',
        'vectorArray': 'vector3array',

        'reflectanceRGB': 'color3',
        'reflectance': None,
        'spectrumRGB': 'color3',
        'spectrum': None,

        'compound': None,
        'message': None,

        'nurbsCurve': None,
        'nurbsSurface': None,
        'mesh': None,
        'lattice': None,
        'pointArray': None,
    }
