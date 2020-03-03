# coding:utf-8
import os


class Utility(object):
    DEF_mtl_data_separator = u','
    DEF_mtl_data_array_separator = u', '

    DEF_mya_separator_node = u'|'
    DEF_mtl_namespace_separator = u':'
    DEF_mtl_node_separator = u'/'
    DEF_mtl_file_separator = u'/'
    DEF_mtl_port_separator = u'.'

    DEF_mtl_key_category_string = u'categoryString'
    DEF_mtl_key_type_string = u'typeString'
    DEF_mtl_key_datatype_string = u'datatypeString'
    DEF_mtl_key_port_string = u'portString'
    DEF_mtl_key_value_string = u'valueString'
    DEF_mtl_key_port = u'port'

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

    DEF_mtl_arnold_nodedefs_file = os.path.dirname(__file__) + '/.data/arnold_5.4.0.1-nodedefs.json'
    DEF_mtl_maya_arnold_nodedefs_file = os.path.dirname(__file__) + '/.data/maya_2019-arnold_5.4.0.1-nodedefs.json'

    DEF_mtl_geometry_def_dict = {
        u'property': [
            {
                "portString": "opaque",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "matte",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "portString": "use_shadow_group",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "portString": "motion_start",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "portString": "motion_end",
                "datatypeString": "float",
                "valueString": "1"
            },
            {
                "portString": "id",
                "datatypeString": "integer",
                "valueString": "0"
            },
            {
                "portString": "smoothing",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "portString": "subdiv_type",
                "datatypeString": "string",
                "valueString": "none"
            },
            {
                "portString": "subdiv_iterations",
                "datatypeString": "integer",
                "valueString": "0"
            },
            {
                "portString": "subdiv_adaptive_error",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "portString": "subdiv_adaptive_metric",
                "datatypeString": "string",
                "valueString": "auto"
            },
            {
                "portString": "subdiv_adaptive_space",
                "datatypeString": "string",
                "valueString": "raster"
            },
            {
                "portString": "subdiv_uv_smoothing",
                "datatypeString": "string",
                "valueString": "pin_corners"
            },
            {
                "portString": "subdiv_frustum_ignore",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "portString": "subdiv_smooth_derivs",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "portString": "disp_padding",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "portString": "disp_height",
                "datatypeString": "float",
                "valueString": "1"
            },
            {
                "portString": "disp_zero_value",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "portString": "disp_autobump",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "portString": "autobump_visibility",
                "datatypeString": "integer",
                "valueString": "1"
            },
            {
                "portString": "step_size",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "portString": "volume_padding",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "portString": "invert_normals",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "self_shadows",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "receive_shadows",
                "datatypeString": "boolean",
                "valueString": "true"
            }
        ],
        u'visibility': [
            {
                "portString": "camera",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "shadow",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "diffuse_transmit",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "specular_transmit",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "volume",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "diffuse_reflect",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "specular_reflect",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "portString": "subsurface",
                "datatypeString": "boolean",
                "valueString": "true"
            },
        ]
    }

    DEF_mtl_material_def_list = [
            {
                u'portString': u'surface_shader',
                u'datatypeString': u'closure',
                u'valueString': u''
            },
            {
                u'portString': u'displacement_shader',
                u'datatypeString': u'closure',
                u'valueString': u''
            },
            {
                u'portString': u'volume_shader',
                u'datatypeString': u'closure',
                u'valueString': u''
            }
        ]

    DEF_mtl_output_def_dict = {
        u'integer': [
            {
                u'portString': u'out_value',
                u'datatypeString': u'integer',
                u'valueString': u'0'
            }
        ],
        u'float': [
            {
                u'portString': u'out_value',
                u'datatypeString': u'float',
                u'valueString': u'0.0'
            }
        ],
        u'boolean': [
            {
                u'portString': u'out_value',
                u'datatypeString': u'boolean',
                u'valueString': u'false'
            }
        ],
        u'string': [
            {
                u'portString': u'out_value',
                u'datatypeString': u'string',
                u'valueString': u''
            }
        ],
        u'color3': [
            {
                u'portString': u'out_color',
                u'datatypeString': u'color3',
                u'valueString': u'0.0, 0.0, 0.0'
            }
        ],
        u'color4': [
            {
                u'portString': u'out_color',
                u'datatypeString': u'color4',
                u'valueString': u'0.0, 0.0, 0.0, 0.0'
            }
        ],
        u'vector3': [
            {
                u'portString': u'out_value',
                u'datatypeString': u'vector3',
                u'valueString': u'0.0, 0.0, 0.0'
            }
        ],
        u'matrix44': [
            {
                u'portString': u'out_value',
                u'datatypeString': u'matrix44',
                u'valueString': u''
            }
        ],
        u'closure': [
            {
                u'portString': u'out_color',
                u'datatypeString': u'color3',
                u'valueString': u'0.0, 0.0, 0.0'
            }
        ],
        u'geometry': []
    }

    DEF_mtl_channel_def_dict = {
        u'color3': [
            {
                u'portString': u'r',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'g',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'b',
                u'datatypeString': u'float',
            }
        ],
        u'color4': [
            {
                u'portString': u'r',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'g',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'b',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'a',
                u'datatypeString': u'float',
            }
        ],
        u'vector3': [
            {
                u'portString': u'x',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'y',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'z',
                u'datatypeString': u'float',
            }
        ],
        u'closure': [
            {
                u'portString': u'r',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'g',
                u'datatypeString': u'float',
            },
            {
                u'portString': u'b',
                u'datatypeString': u'float',
            }
        ]
    }

    DEF_mtl_maya_2019_def_dict = {
        # aov read
        "aov_read_int": {
            "categoryString": u'aiReadInt',
            "port": {
                "aov_name": {
                    "portString": u'aovName',
                    "datatypeString": {
                        "string": u'typed'
                    }
                }
            }
        },
        "aov_read_float": {
            "categoryString": u'aiReadFloat',
            "port": {
                "aov_name": {
                    "portString": u'aovName',
                    "datatypeString": {
                        "string": u'typed'
                    }
                }
            }
        },
        "aov_read_rgb": {
            "categoryString": u'aiReadRgb',
            "port": {
                "aov_name": {
                    "portString": u'aovName',
                    "datatypeString": {
                        "string": u'typed'
                    }
                }
            }
        },
        "aov_read_rgba": {
            "categoryString": u'aiReadRgba',
            "port": {
                "aov_name": {
                    "portString": u'aovName',
                    "datatypeString": {
                        "string": u'typed'
                    }
                }
            }
        },
        # aov write
        "aov_write_int": {
            "categoryString": u'aiWriteInt',
            "port": {
                "passthrough": {
                    "portString": u'beauty',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "aov_input": {
                    "portString": u'input',
                    "datatypeString": {
                        "integer": u'long'
                    }
                },
                "aov_name": {
                    "portString": u'aovName',
                    "datatypeString": {
                        "string": u'typed'
                    }
                }
            }
        },
        "aov_write_float": {
            "categoryString": u'aiWriteFloat',
            "port": {
                "passthrough": {
                    "portString": u'beauty',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "aov_input": {
                    "portString": u'input',
                    "datatypeString": {
                        "float": u'float'
                    }
                },
                "aov_name": {
                    "portString": u'aovName',
                    "datatypeString": {
                        "string": u'typed'
                    }
                },
                "blend_opacity": {
                    "portString": u'blend',
                    "datatypeString": {
                        "boolean": u'bool'
                    }
                }
            }
        },
        "aov_write_rgb": {
            "categoryString": u'aiWriteColor',
            "port": {
                "passthrough": {
                    "portString": u'beauty',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "aov_input": {
                    "portString": u'input',
                    "datatypeString": {
                        "color3": None
                    }
                },
                "aov_name": {
                    "portString": u'aovName',
                    "datatypeString": {
                        "string": u'typed'
                    }
                },
                "blend_opacity": {
                    "portString": u'blend',
                    "datatypeString": {
                        "boolean": u'bool'
                    }
                }
            }
        },
        "aov_write_rgba": {
            "categoryString": u'aiWriteRgba',
            "port": {
                "passthrough": {
                    "portString": u'beauty',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "aov_input": {
                    "portString": u'input',
                    "datatypeString": {
                        "color4": None
                    }
                },
                "aov_name": {
                    "portString": u'aovName',
                    "datatypeString": {
                        "string": u'typed'
                    }
                },
                "blend_opacity": {
                    "portString": u'blend',
                    "datatypeString": {
                        "boolean": u'bool'
                    }
                }
            }
        },
        # user data
        "user_data_string": {
            "categoryString": "aiUserDataString",
            "port": {
                "attribute": {
                    "portString": "attribute",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "default": {
                    "portString": "default",
                    "datatypeString": {
                        "string": "typed"
                    }
                }
            }
        },
        "user_data_int": {
            "categoryString": "aiUserDataInt",
            "port": {
                "attribute": {
                    "portString": "attribute",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "default": {
                    "portString": "default",
                    "datatypeString": {
                        "integer": "long"
                    }
                }
            }
        },
        "user_data_float": {
            "categoryString": "aiUserDataFloat",
            "port": {
                "attribute": {
                    "portString": "attribute",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "default": {
                    "portString": "default",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "user_data_rgb": {
            "categoryString": u'aiUserDataColor',
            "port": {
                "attribute": {
                    "portString": u'attribute',
                    "datatypeString": {
                        "string": u'typed'
                    }
                },
                "default": {
                    "portString": u'default',
                    "datatypeString": {
                        "color3": u'floatArray'
                    }
                }
            }
        },
        "user_data_rgba": {
            "categoryString": None,
            "port": {
                "attribute": {
                    "portString": None,
                    "datatypeString": {
                        "string": None
                    }
                },
                "default": {
                    "portString": None,
                    "datatypeString": {
                        "color4": None
                    }
                }
            }
        },
        # convert
        "float_to_int": {
            "categoryString": "aiFloatToInt",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mode": {
                    "portString": "mode",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "float_to_rgb": {
            "categoryString": None,
            "port": {
                "r": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "g": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "b": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                }
            }
        },
        "float_to_rgba": {
            "categoryString": "aiFloatToRgba",
            "port": {
                "r": {
                    "portString": "r",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "g": {
                    "portString": "g",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "b": {
                    "portString": "b",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "a": {
                    "portString": "a",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "float_to_matrix": {
            "categoryString": None,
            "port": {
                "input_00": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_01": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_02": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_03": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_10": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_11": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_12": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_13": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_20": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_21": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_22": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_23": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_30": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_31": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_32": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "input_33": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                }
            }
        },
        "rgb_to_float": {
            "categoryString": u'aiColorToFloat',
            "port": {
                "input": {
                    "portString": u'input',
                    "datatypeString": {
                        "color3": u'floatArray'
                    }
                },
                "mode": {
                    "portString": u'mode',
                    "datatypeString": {
                        "string": u'enum'
                    }
                }
            }
        },
        "rgba_to_float": {
            "categoryString": "aiRgbaToFloat",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mode": {
                    "portString": "mode",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "rgb_to_vector": {
            "categoryString": None,
            "port": {
                "input": {
                    "portString": None,
                    "datatypeString": {
                        "vector3": None
                    }
                },
                "mode": {
                    "portString": None,
                    "datatypeString": {
                        "string": None
                    }
                }
            }
        },
        "vector_to_rgb": {
            "categoryString": None,
            "port": {
                "input": {
                    "portString": None,
                    "datatypeString": {
                        "vector3": None
                    }
                },
                "mode": {
                    "portString": None,
                    "datatypeString": {
                        "string": None
                    }
                }
            }
        },
        # shader.surface
        "ambient_occlusion": {
            "categoryString": "aiAmbientOcclusion",
            "port": {
                "samples": {
                    "portString": "samples",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "spread": {
                    "portString": "spread",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "near_clip": {
                    "portString": "nearClip",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "far_clip": {
                    "portString": "farClip",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "falloff": {
                    "portString": "falloff",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "black": {
                    "portString": "black",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "white": {
                    "portString": "white",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "invert_normals": {
                    "portString": "invertNormals",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "trace_set": {
                    "portString": "traceSet",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "inclusive": {
                    "portString": "inclusive",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "self_only": {
                    "portString": "selfOnly",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "bump2d": {
            "categoryString": "aiBump2d",
            "port": {
                "bump_map": {
                    "portString": "bumpMap",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "bump_height": {
                    "portString": "bumpHeight",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "bump3d": {
            "categoryString": "aiBump3d",
            "port": {
                "bump_map": {
                    "portString": "bumpMap",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "bump_height": {
                    "portString": "bumpHeight",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "epsilon": {
                    "portString": "epsilon",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "car_paint": {
            "categoryString": "aiCarPaint",
            "port": {
                "base": {
                    "portString": "base",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "base_color": {
                    "portString": "baseColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "base_roughness": {
                    "portString": "baseRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular": {
                    "portString": "specular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_color": {
                    "portString": "specularColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular_flip_flop": {
                    "portString": "specularFlipFlop",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular_light_facing": {
                    "portString": "specularLightFacing",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular_falloff": {
                    "portString": "specularFalloff",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_roughness": {
                    "portString": "specularRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_IOR": {
                    "portString": "specularIOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_color": {
                    "portString": "transmissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "flake_color": {
                    "portString": "flakeColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "flake_flip_flop": {
                    "portString": "flakeFlipFlop",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "flake_light_facing": {
                    "portString": "flakeLightFacing",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "flake_falloff": {
                    "portString": "flakeFalloff",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "flake_roughness": {
                    "portString": "flakeRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "flake_IOR": {
                    "portString": "flakeIOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "flake_scale": {
                    "portString": "flakeScale",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "flake_density": {
                    "portString": "flakeDensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "flake_layers": {
                    "portString": "flakeLayers",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "flake_normal_randomize": {
                    "portString": "flakeNormalRandomize",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "flake_coord_space": {
                    "portString": "flakeCoordSpace",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "pref_name": {
                    "portString": "prefName",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "coat": {
                    "portString": "coat",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coat_color": {
                    "portString": "coatColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "coat_roughness": {
                    "portString": "coatRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coat_IOR": {
                    "portString": "coatIOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coat_normal": {
                    "portString": "coatNormal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "clip_geo": {
            "categoryString": "aiClipGeo",
            "port": {
                "intersection": {
                    "portString": "intersection",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "trace_set": {
                    "portString": "traceSet",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "inclusive": {
                    "portString": "inclusive",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "complex_ior": {
            "categoryString": "aiComplexIor",
            "port": {
                "material": {
                    "portString": "material",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "mode": {
                    "portString": "mode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "reflectivity": {
                    "portString": "reflectivity",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "edgetint": {
                    "portString": "edgetint",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "n": {
                    "portString": "n",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "k": {
                    "portString": "k",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "lambert": {
            "categoryString": u'lambert',
            "port": {
                "Kd": {
                    "portString": u'diffuse',
                    "datatypeString": {
                        "float": u'float'
                    }
                },
                "Kd_color": {
                    "portString": 'color',
                    "datatypeString": {
                        "color3": u'floatArray'
                    }
                },
                "opacity": {
                    "portString": u'transparency',
                    "datatypeString": {
                        "color3": u'floatArray'
                    }
                },
                "normal": {
                    "portString": u'normalCamera',
                    "datatypeString": {
                        "vector3": u'floatArray'
                    }
                }
            }
        },
        "round_corners": {
            "categoryString": "aiRoundCorners",
            "port": {
                "samples": {
                    "portString": "samples",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "radius": {
                    "portString": "radius",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "trace_set": {
                    "portString": "traceSet",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "inclusive": {
                    "portString": "inclusive",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "self_only": {
                    "portString": "selfOnly",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "object_space": {
                    "portString": "objectSpace",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "shadow_matte": {
            "categoryString": "aiShadowMatte",
            "port": {
                "background": {
                    "portString": "background",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "shadow_color": {
                    "portString": "shadowColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "shadow_opacity": {
                    "portString": "shadowOpacity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "background_color": {
                    "portString": "backgroundColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "diffuse_color": {
                    "portString": "diffuseColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "diffuse_use_background": {
                    "portString": "diffuseUseBackground",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "diffuse_intensity": {
                    "portString": "diffuseIntensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "backlighting": {
                    "portString": "backlighting",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "indirect_diffuse_enable": {
                    "portString": "indirectDiffuseEnable",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "indirect_specular_enable": {
                    "portString": "indirectSpecularEnable",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "specular_color": {
                    "portString": "specularColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular_intensity": {
                    "portString": "specularIntensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_roughness": {
                    "portString": "specularRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_IOR": {
                    "portString": "specularIOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "alpha_mask": {
                    "portString": "alphaMask",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "aov_group": {
                    "portString": "aovGroup",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "aov_shadow": {
                    "portString": "aovShadow",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "aov_shadow_diff": {
                    "portString": "aovShadowDiff",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "aov_shadow_mask": {
                    "portString": "aovShadowMask",
                    "datatypeString": {
                        "string": "typed"
                    }
                }
            }
        },
        "standard_surface": {
            "categoryString": "aiStandardSurface",
            "port": {
                "base": {
                    "portString": "base",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "base_color": {
                    "portString": "baseColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "diffuse_roughness": {
                    "portString": "diffuseRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular": {
                    "portString": "specular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_color": {
                    "portString": "specularColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular_roughness": {
                    "portString": "specularRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_IOR": {
                    "portString": "specularIOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_anisotropy": {
                    "portString": "specularAnisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_rotation": {
                    "portString": "specularRotation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "metalness": {
                    "portString": "metalness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission": {
                    "portString": "transmission",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_color": {
                    "portString": "transmissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "transmission_depth": {
                    "portString": "transmissionDepth",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_scatter": {
                    "portString": "transmissionScatter",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "transmission_scatter_anisotropy": {
                    "portString": "transmissionScatterAnisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_dispersion": {
                    "portString": "transmissionDispersion",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_extra_roughness": {
                    "portString": "transmissionExtraRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmit_aovs": {
                    "portString": "transmitAovs",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "subsurface": {
                    "portString": "subsurface",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "subsurface_color": {
                    "portString": "subsurfaceColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "subsurface_radius": {
                    "portString": "subsurfaceRadius",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "subsurface_scale": {
                    "portString": "subsurfaceScale",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "subsurface_anisotropy": {
                    "portString": "subsurfaceAnisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "subsurface_type": {
                    "portString": "subsurfaceType",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "sheen": {
                    "portString": "sheen",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sheen_color": {
                    "portString": "sheenColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "sheen_roughness": {
                    "portString": "sheenRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "thin_walled": {
                    "portString": "thinWalled",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "normal": {
                    "portString": None,
                    "datatypeString": {
                        "vector3": None
                    }
                },
                "tangent": {
                    "portString": "tangent",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "coat": {
                    "portString": "coat",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coat_color": {
                    "portString": "coatColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "coat_roughness": {
                    "portString": "coatRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coat_IOR": {
                    "portString": "coatIOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coat_anisotropy": {
                    "portString": "coatAnisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coat_rotation": {
                    "portString": "coatRotation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coat_normal": {
                    "portString": "coatNormal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "coat_affect_color": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "coat_affect_roughness": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "thin_film_thickness": {
                    "portString": "thinFilmThickness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "thin_film_IOR": {
                    "portString": "thinFilmIOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "emission": {
                    "portString": "emission",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "emission_color": {
                    "portString": "emissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "opacity": {
                    "portString": "opacity",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "caustics": {
                    "portString": "caustics",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "internal_reflections": {
                    "portString": "internalReflections",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "exit_to_background": {
                    "portString": "exitToBackground",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "indirect_diffuse": {
                    "portString": "indirectDiffuse",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "indirect_specular": {
                    "portString": "indirectSpecular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "aov_id1": {
                    "portString": "aovId1",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id1": {
                    "portString": "id1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id2": {
                    "portString": "aovId2",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id2": {
                    "portString": "id2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id3": {
                    "portString": "aovId3",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id3": {
                    "portString": "id3",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id4": {
                    "portString": "aovId4",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id4": {
                    "portString": "id4",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id5": {
                    "portString": "aovId5",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id5": {
                    "portString": "id5",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id6": {
                    "portString": "aovId6",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id6": {
                    "portString": "id6",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id7": {
                    "portString": "aovId7",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id7": {
                    "portString": "id7",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id8": {
                    "portString": "aovId8",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id8": {
                    "portString": "id8",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "standard_hair": {
            "categoryString": "aiStandardHair",
            "port": {
                "base": {
                    "portString": "base",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "base_color": {
                    "portString": "baseColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "melanin": {
                    "portString": "melanin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "melanin_redness": {
                    "portString": "melaninRedness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "melanin_randomize": {
                    "portString": "melaninRandomize",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "roughness": {
                    "portString": "roughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "roughness_azimuthal": {
                    "portString": "roughnessAzimuthal",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "roughness_anisotropic": {
                    "portString": "roughnessAnisotropic",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "ior": {
                    "portString": "ior",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "shift": {
                    "portString": "shift",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_tint": {
                    "portString": "specularTint",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular2_tint": {
                    "portString": "specular2Tint",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "transmission_tint": {
                    "portString": "transmissionTint",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "diffuse": {
                    "portString": "diffuse",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "diffuse_color": {
                    "portString": "diffuseColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "emission": {
                    "portString": "emission",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "emission_color": {
                    "portString": "emissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "opacity": {
                    "portString": "opacity",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "indirect_diffuse": {
                    "portString": "indirectDiffuse",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "indirect_specular": {
                    "portString": "indirectSpecular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "extra_depth": {
                    "portString": "extraDepth",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "extra_samples": {
                    "portString": "extraSamples",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "aov_id1": {
                    "portString": "aovId1",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id1": {
                    "portString": "id1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id2": {
                    "portString": "aovId2",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id2": {
                    "portString": "id2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id3": {
                    "portString": "aovId3",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id3": {
                    "portString": "id3",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id4": {
                    "portString": "aovId4",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id4": {
                    "portString": "id4",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id5": {
                    "portString": "aovId5",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id5": {
                    "portString": "id5",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id6": {
                    "portString": "aovId6",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id6": {
                    "portString": "id6",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id7": {
                    "portString": "aovId7",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id7": {
                    "portString": "id7",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "aov_id8": {
                    "portString": "aovId8",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "id8": {
                    "portString": "id8",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "toon": {
            "categoryString": "aiToon",
            "port": {
                "mask_color": {
                    "portString": "maskColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "edge_color": {
                    "portString": "edgeColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "edge_tonemap": {
                    "portString": "edgeTonemap",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "edge_opacity": {
                    "portString": "edgeOpacity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "edge_width_scale": {
                    "portString": "edgeWidthScale",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "silhouette_color": {
                    "portString": "silhouetteColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "silhouette_tonemap": {
                    "portString": "silhouetteTonemap",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "silhouette_opacity": {
                    "portString": "silhouetteOpacity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "silhouette_width_scale": {
                    "portString": "silhouetteWidthScale",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "priority": {
                    "portString": "priority",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "enable_silhouette": {
                    "portString": "enableSilhouette",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "ignore_throughput": {
                    "portString": "ignoreThroughput",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "enable": {
                    "portString": "enable",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "id_difference": {
                    "portString": "idDifference",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "shader_difference": {
                    "portString": "shaderDifference",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "uv_threshold": {
                    "portString": "uvThreshold",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "angle_threshold": {
                    "portString": "angleThreshold",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "normal_type": {
                    "portString": "normalType",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "base": {
                    "portString": "base",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "base_color": {
                    "portString": "baseColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "base_tonemap": {
                    "portString": "baseTonemap",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular": {
                    "portString": "specular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_color": {
                    "portString": "specularColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular_roughness": {
                    "portString": "specularRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_anisotropy": {
                    "portString": "specularAnisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_rotation": {
                    "portString": "specularRotation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_tonemap": {
                    "portString": "specularTonemap",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "lights": {
                    "portString": "lights",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "highlight_color": {
                    "portString": "highlightColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "highlight_size": {
                    "portString": "highlightSize",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "aov_highlight": {
                    "portString": "aovHighlight",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "rim_light": {
                    "portString": "rimLight",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "rim_light_color": {
                    "portString": "rimLightColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "rim_light_width": {
                    "portString": "rimLightWidth",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "aov_rim_light": {
                    "portString": "aovRimLight",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "transmission": {
                    "portString": "transmission",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_color": {
                    "portString": "transmissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "transmission_roughness": {
                    "portString": "transmissionRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_anisotropy": {
                    "portString": "transmissionAnisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_rotation": {
                    "portString": "transmissionRotation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sheen": {
                    "portString": "sheen",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sheen_color": {
                    "portString": "sheenColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "sheen_roughness": {
                    "portString": "sheenRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "emission": {
                    "portString": "emission",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "emission_color": {
                    "portString": "emissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "IOR": {
                    "portString": "IOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "tangent": {
                    "portString": "tangent",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "indirect_diffuse": {
                    "portString": "indirectDiffuse",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "indirect_specular": {
                    "portString": "indirectSpecular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "bump_mode": {
                    "portString": "bumpMode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "energy_conserving": {
                    "portString": "energyConserving",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "user_id": {
                    "portString": "userId",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "two_sided": {
            "categoryString": "aiTwoSided",
            "port": {
                "front": {
                    "portString": "front",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "back": {
                    "portString": "back",
                    "datatypeString": {
                        "closure": "float3"
                    }
                }
            }
        },
        # shader.old
        "standard": {
            "categoryString": "aiStandard",
            "port": {
                "Kd": {
                    "portString": "Kd",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Kd_color": {
                    "portString": u'color',
                    "datatypeString": {
                        "color3": 'floatArray'
                    }
                },
                "diffuse_roughness": {
                    "portString": "diffuseRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Ks": {
                    "portString": "Ks",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Ks_color": {
                    "portString": "KsColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular_roughness": {
                    "portString": "specularRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_anisotropy": {
                    "portString": "specularAnisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_rotation": {
                    "portString": "specularRotation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_distribution": {
                    "portString": "specularDistribution",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "Kr": {
                    "portString": "Kr",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Kr_color": {
                    "portString": "KrColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "reflection_exit_color": {
                    "portString": "reflectionExitColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "reflection_exit_use_environment": {
                    "portString": "reflectionExitUseEnvironment",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "Kt": {
                    "portString": "Kt",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Kt_color": {
                    "portString": "KtColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "transmittance": {
                    "portString": "transmittance",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "refraction_roughness": {
                    "portString": "refractionRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "refraction_exit_color": {
                    "portString": "refractionExitColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "refraction_exit_use_environment": {
                    "portString": "refractionExitUseEnvironment",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "IOR": {
                    "portString": "IOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "dispersion_abbe": {
                    "portString": "dispersionAbbe",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Kb": {
                    "portString": "Kb",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Fresnel": {
                    "portString": "Fresnel",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "Krn": {
                    "portString": "Krn",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_Fresnel": {
                    "portString": "specularFresnel",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "Ksn": {
                    "portString": "Ksn",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Fresnel_use_IOR": {
                    "portString": "FresnelUseIOR",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "Fresnel_affect_diff": {
                    "portString": "FresnelAffectDiff",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "emission": {
                    "portString": "emission",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "emission_color": {
                    "portString": "emissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "direct_specular": {
                    "portString": "directSpecular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "indirect_specular": {
                    "portString": "indirectSpecular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "direct_diffuse": {
                    "portString": "directDiffuse",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "indirect_diffuse": {
                    "portString": "indirectDiffuse",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable_glossy_caustics": {
                    "portString": "enableGlossyCaustics",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "enable_reflective_caustics": {
                    "portString": "enableReflectiveCaustics",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "enable_refractive_caustics": {
                    "portString": "enableRefractiveCaustics",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "enable_internal_reflections": {
                    "portString": "enableInternalReflections",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "Ksss": {
                    "portString": "Ksss",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "Ksss_color": {
                    "portString": "KsssColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "sss_radius": {
                    "portString": "sssRadius",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "bounce_factor": {
                    "portString": "bounceFactor",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "opacity": {
                    "portString": "opacity",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "hair": {
            "categoryString": "aiHair",
            "port": {
                "rootcolor": {
                    "portString": "rootcolor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "tipcolor": {
                    "portString": "tipcolor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "opacity": {
                    "portString": "opacity",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "ambdiff": {
                    "portString": "ambdiff",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "spec": {
                    "portString": "spec",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "spec_color": {
                    "portString": "specColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "spec_shift": {
                    "portString": "specShift",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "spec_gloss": {
                    "portString": "specGloss",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "spec2": {
                    "portString": "spec2",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "spec2_color": {
                    "portString": "spec2Color",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "spec2_shift": {
                    "portString": "spec2Shift",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "spec2_gloss": {
                    "portString": "spec2Gloss",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission": {
                    "portString": "transmission",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transmission_color": {
                    "portString": "transmissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "transmission_spread": {
                    "portString": "transmissionSpread",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "kd_ind": {
                    "portString": "kdInd",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "skin": {
            "categoryString": "aiSkin",
            "port": {
                "sss_weight": {
                    "portString": "sssWeight",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "shallow_scatter_color": {
                    "portString": "shallowScatterColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "shallow_scatter_weight": {
                    "portString": "shallowScatterWeight",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "shallow_scatter_radius": {
                    "portString": "shallowScatterRadius",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mid_scatter_color": {
                    "portString": "midScatterColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "mid_scatter_weight": {
                    "portString": "midScatterWeight",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mid_scatter_radius": {
                    "portString": "midScatterRadius",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "deep_scatter_color": {
                    "portString": "deepScatterColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "deep_scatter_weight": {
                    "portString": "deepScatterWeight",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "deep_scatter_radius": {
                    "portString": "deepScatterRadius",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_color": {
                    "portString": "specularColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "specular_weight": {
                    "portString": "specularWeight",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_roughness": {
                    "portString": "specularRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_ior": {
                    "portString": "specularIor",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sheen_color": {
                    "portString": "sheenColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "sheen_weight": {
                    "portString": "sheenWeight",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sheen_roughness": {
                    "portString": "sheenRoughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sheen_ior": {
                    "portString": "sheenIor",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "global_sss_radius_multiplier": {
                    "portString": "globalSssRadiusMultiplier",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "specular_in_secondary_rays": {
                    "portString": "specularInSecondaryRays",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "fresnel_affect_sss": {
                    "portString": "fresnelAffectSss",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "opacity": {
                    "portString": "opacity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "opacity_color": {
                    "portString": "opacityColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        # switch
        "switch_rgba": {
            "categoryString": None,
            "port": {
                "index": {
                    "portString": u'index',
                    "datatypeString": {
                        "integer": u'long'
                    }
                },
                "input0": {
                    "portString": u'input0',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input1": {
                    "portString": u'input1',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input2": {
                    "portString": u'input2',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input3": {
                    "portString": u'input3',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input4": {
                    "portString": u'input4',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input5": {
                    "portString": u'input5',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input6": {
                    "portString": u'input6',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input7": {
                    "portString": u'input7',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input8": {
                    "portString": u'input8',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input9": {
                    "portString": u'input9',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input10": {
                    "portString": u'input10',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input11": {
                    "portString": u'input11',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input12": {
                    "portString": u'input12',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input13": {
                    "portString": u'input13',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input14": {
                    "portString": u'input14',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input15": {
                    "portString": u'input15',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input16": {
                    "portString": u'input16',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input17": {
                    "portString": u'input17',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input18": {
                    "portString": u'input18',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                },
                "input19": {
                    "portString": u'input19',
                    "datatypeString": {
                        "color4": u'floatArray'
                    }
                }
            }
        },
        "switch_shader": {
            "categoryString": u'aiSwitch',
            "port": {
                "index": {
                    "portString": u'index',
                    "datatypeString": {
                        "integer": u'long'
                    }
                },
                "input0": {
                    "portString": u'input0',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input1": {
                    "portString": u'input1',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input2": {
                    "portString": u'input2',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input3": {
                    "portString": u'input3',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input4": {
                    "portString": u'input4',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input5": {
                    "portString": u'input5',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input6": {
                    "portString": u'input6',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input7": {
                    "portString": u'input7',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input8": {
                    "portString": u'input8',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input9": {
                    "portString": u'input9',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input10": {
                    "portString": u'input10',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input11": {
                    "portString": u'input11',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input12": {
                    "portString": u'input12',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input13": {
                    "portString": u'input13',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input14": {
                    "portString": u'input14',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input15": {
                    "portString": u'input15',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input16": {
                    "portString": u'input16',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input17": {
                    "portString": u'input17',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input18": {
                    "portString": u'input18',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                },
                "input19": {
                    "portString": u'input19',
                    "datatypeString": {
                        "closure": u'floatArray'
                    }
                }
            }
        },
        # math
        "abs": {
            "categoryString": "aiAbs",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "add": {
            "categoryString": "aiAdd",
            "port": {
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "atan": {
            "categoryString": "aiAtan",
            "port": {
                "y": {
                    "portString": "y",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "x": {
                    "portString": "x",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "units": {
                    "portString": "units",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "compare": {
            "categoryString": "aiCompare",
            "port": {
                "test": {
                    "portString": "test",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "complement": {
            "categoryString": "aiComplement",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "cross": {
            "categoryString": "aiCross",
            "port": {
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "divide": {
            "categoryString": "aiDivide",
            "port": {
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "dot": {
            "categoryString": "aiDot",
            "port": {
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "exp": {
            "categoryString": "aiExp",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "fraction": {
            "categoryString": "aiFraction",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "is_finite": {
            "categoryString": "aiIsFinite",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "length": {
            "categoryString": "aiLength",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "mode": {
                    "portString": "mode",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "log": {
            "categoryString": "aiLog",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "base": {
                    "portString": "base",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "modulo": {
            "categoryString": "aiModulo",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "divisor": {
                    "portString": "divisor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "multiply": {
            "categoryString": "aiMultiply",
            "port": {
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "negate": {
            "categoryString": "aiNegate",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "normalize": {
            "categoryString": "aiNormalize",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "pow": {
            "categoryString": "aiPow",
            "port": {
                "base": {
                    "portString": "base",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "exponent": {
                    "portString": "exponent",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "reciprocal": {
            "categoryString": "aiReciprocal",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "sign": {
            "categoryString": "aiSign",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "sqrt": {
            "categoryString": "aiSqrt",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "subtract": {
            "categoryString": "aiSubtract",
            "port": {
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "trigo": {
            "categoryString": "aiTrigo",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "function": {
                    "portString": "function",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "units": {
                    "portString": "units",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "frequency": {
                    "portString": "frequency",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "phase": {
                    "portString": "phase",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        # matrix
        "matrix_interpolate": {
            "categoryString": "aiMatrixInterpolate",
            "port": {
                "type": {
                    "portString": "type",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "value": {
                    "portString": "value",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "matrix_multiply_vector": {
            "categoryString": "aiMatrixMultiplyVector",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "type": {
                    "portString": "type",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "matrix": {
                    "portString": "matrix",
                    "datatypeString": {
                        "matrix44": "fltMatrix"
                    }
                }
            }
        },
        "matrix_transform": {
            "categoryString": "aiMatrixTransform",
            "port": {
                "transform_order": {
                    "portString": "transformOrder",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "rotation_type": {
                    "portString": "rotationType",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "units": {
                    "portString": "units",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "rotation_order": {
                    "portString": "rotationOrder",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "rotation": {
                    "portString": "rotation",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "axis": {
                    "portString": "axis",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "angle": {
                    "portString": "angle",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "translate": {
                    "portString": "translate",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "scale": {
                    "portString": "scale",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "pivot": {
                    "portString": "pivot",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        # texture
        "blackbody": {
            "categoryString": "aiBlackbody",
            "port": {
                "temperature": {
                    "portString": "temperature",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "normalize": {
                    "portString": "normalize",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "intensity": {
                    "portString": "intensity",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "camera_projection": {
            "categoryString": "aiCameraProjection",
            "port": {
                "projection_color": {
                    "portString": "projectionColor",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "offscreen_color": {
                    "portString": "offscreenColor",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mask": {
                    "portString": "mask",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "camera": {
                    "portString": "camera",
                    "datatypeString": {
                        "string": "message"
                    }
                },
                "aspect_ratio": {
                    "portString": "aspectRatio",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "front_facing": {
                    "portString": "frontFacing",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "back_facing": {
                    "portString": "backFacing",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "use_shading_normal": {
                    "portString": "useShadingNormal",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "coord_space": {
                    "portString": "coordSpace",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "pref_name": {
                    "portString": "prefName",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "P": {
                    "portString": "P",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "checkerboard": {
            "categoryString": u'checker',
            "port": {
                "color1": {
                    "portString": u'color1',
                    "datatypeString": {
                        "color3": u'floatArray'
                    }
                },
                "color2": {
                    "portString": u'color2',
                    "datatypeString": {
                        "color3": u'floatArray'
                    }
                },
                "u_frequency": {
                    "portString": [
                        u'place2dTexture',
                        u'repeatUV.repeatU'
                    ],
                    "datatypeString": {
                        "float": u'float'
                    }
                },
                "v_frequency": {
                    "portString": [
                        u'place2dTexture',
                        u'repeatUV.repeatV'
                    ],
                    "datatypeString": {
                        "float": u'float'
                    }
                },
                "u_offset": {
                    "portString": [
                        u'place2dTexture',
                        u'offset.offsetU'
                    ],
                    "datatypeString": {
                        "float": u'float'
                    }
                },
                "v_offset": {
                    "portString": [
                        u'place2dTexture',
                        u'offset.offsetV'
                    ],
                    "datatypeString": {
                        "float": u'float'
                    }
                },
                "contrast": {
                    "portString": u'contrast',
                    "datatypeString": {
                        "float": u'float'
                    }
                },
                "filter_strength": {
                    "portString": u'filter',
                    "datatypeString": {
                        "float": None
                    }
                },
                "filter_offset": {
                    "portString": u'filterOffset',
                    "datatypeString": {
                        "float": u'float'
                    }
                },
                "uvset": {
                    "portString": None,
                    "datatypeString": {
                        "string": None
                    }
                }
            }
        },
        "flakes": {
            "categoryString": "aiFlakes",
            "port": {
                "scale": {
                    "portString": "scale",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "density": {
                    "portString": "density",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "step": {
                    "portString": "step",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "depth": {
                    "portString": "depth",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "IOR": {
                    "portString": "IOR",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "normal_randomize": {
                    "portString": "normalRandomize",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "coord_space": {
                    "portString": "coordSpace",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "pref_name": {
                    "portString": "prefName",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "output_space": {
                    "portString": "outputSpace",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "image": {
            "categoryString": "aiImage",
            "port": {
                "filename": {
                    "portString": "filename",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "color_space": {
                    "portString": "colorSpace",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "filter": {
                    "portString": "filter",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "mipmap_bias": {
                    "portString": "mipmapBias",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "single_channel": {
                    "portString": "singleChannel",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "start_channel": {
                    "portString": "startChannel",
                    "datatypeString": {
                        "integer": "byte"
                    }
                },
                "swrap": {
                    "portString": "swrap",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "twrap": {
                    "portString": "twrap",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "sscale": {
                    "portString": "sscale",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "tscale": {
                    "portString": "tscale",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sflip": {
                    "portString": "sflip",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "tflip": {
                    "portString": "tflip",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "soffset": {
                    "portString": "soffset",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "toffset": {
                    "portString": "toffset",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "swap_st": {
                    "portString": "swapSt",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "uvcoords": {
                    "portString": "uvcoords",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "uvset": {
                    "portString": "uvset",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "multiply": {
                    "portString": "multiply",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "offset": {
                    "portString": "offset",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "ignore_missing_textures": {
                    "portString": "ignoreMissingTextures",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "missing_texture_color": {
                    "portString": "missingTextureColor",
                    "datatypeString": {
                        "color4": "float3"
                    }
                }
            }
        },
        "normal_map": {
            "categoryString": "aiNormalMap",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "tangent": {
                    "portString": "tangent",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "order": {
                    "portString": "order",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "invert_x": {
                    "portString": "invertX",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "invert_y": {
                    "portString": "invertY",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "invert_z": {
                    "portString": "invertZ",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "color_to_signed": {
                    "portString": "colorToSigned",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "tangent_space": {
                    "portString": "tangentSpace",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "strength": {
                    "portString": "strength",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "ramp_float": {
            "categoryString": "aiRampFloat",
            "port": {
                "type": {
                    "portString": "type",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "position": {
                    "portString": u'ramp.ramp_Position',
                    "datatypeString": {
                        "floatarray": u'floatArray'
                    }
                },
                "value": {
                    "portString": u'ramp.ramp_FloatValue',
                    "datatypeString": {
                        "floatarray": u'floatArray'
                    }
                },
                "interpolation": {
                    "portString": u'ramp.ramp_Interp',
                    "datatypeString": {
                        "integerarray": u'Int32Array'
                    }
                },
                "uvset": {
                    "portString": "uvset",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "use_implicit_uvs": {
                    "portString": "useImplicitUvs",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "wrap_uvs": {
                    "portString": "wrapUvs",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "ramp_rgb": {
            "categoryString": "aiRampRgb",
            "port": {
                "type": {
                    "portString": "type",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "position": {
                    "portString": u'ramp.ramp_Position',
                    "datatypeString": {
                        "floatarray": u'floatArray'
                    }
                },
                "color": {
                    "portString": u'ramp.ramp_Color',
                    "datatypeString": {
                        "floatarray": u'floatArray'
                    }
                },
                "interpolation": {
                    "portString": u'ramp.ramp_Interp',
                    "datatypeString": {
                        "integerarray": u'Int32Array'
                    }
                },
                "uvset": {
                    "portString": "uvset",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "use_implicit_uvs": {
                    "portString": "useImplicitUvs",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "wrap_uvs": {
                    "portString": "wrapUvs",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "triplanar": {
            "categoryString": "aiTriplanar",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "scale": {
                    "portString": "scale",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "rotate": {
                    "portString": "rotate",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "offset": {
                    "portString": "offset",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "coord_space": {
                    "portString": "coordSpace",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "pref_name": {
                    "portString": "prefName",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "blend": {
                    "portString": "blend",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "cell": {
                    "portString": "cell",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "cell_rotate": {
                    "portString": "cellRotate",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "cell_blend": {
                    "portString": "cellBlend",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "uv_projection": {
            "categoryString": "aiUvProjection",
            "port": {
                "projection_color": {
                    "portString": "projectionColor",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "projection_type": {
                    "portString": "projectionType",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "coord_space": {
                    "portString": "coordSpace",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "pref_name": {
                    "portString": "prefName",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "P": {
                    "portString": "P",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "u_angle": {
                    "portString": "uAngle",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "v_angle": {
                    "portString": "vAngle",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "clamp": {
                    "portString": "clamp",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "default_color": {
                    "portString": "defaultColor",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "matrix": {
                    "portString": u'placementMatrix',
                    "datatypeString": {
                        "matrix44": u'fltMatrix'
                    }
                }
            }
        },
        "uv_transform": {
            "categoryString": "aiUvTransform",
            "port": {
                "passthrough": {
                    "portString": "passthrough",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "unit": {
                    "portString": "unit",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "uvset": {
                    "portString": "uvset",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "coverage": {
                    "portString": "coverage",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "scale_frame": {
                    "portString": "scaleFrame",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "translate_frame": {
                    "portString": "translateFrame",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "rotate_frame": {
                    "portString": "rotateFrame",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "pivot_frame": {
                    "portString": "pivotFrame",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "wrap_frame_u": {
                    "portString": "wrapFrameU",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "wrap_frame_v": {
                    "portString": "wrapFrameV",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "wrap_frame_color": {
                    "portString": "wrapFrameColor",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "repeat": {
                    "portString": "repeat",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "offset": {
                    "portString": "offset",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "rotate": {
                    "portString": "rotate",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "pivot": {
                    "portString": "pivot",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "noise": {
                    "portString": "noise",
                    "datatypeString": {
                        "vector2": "float2"
                    }
                },
                "mirror_u": {
                    "portString": "mirrorU",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "mirror_v": {
                    "portString": "mirrorV",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "flip_u": {
                    "portString": "flipU",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "flip_v": {
                    "portString": "flipV",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "swap_uv": {
                    "portString": "swapUv",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "stagger": {
                    "portString": "stagger",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "vector_map": {
            "categoryString": "aiVectorMap",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "tangent": {
                    "portString": "tangent",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "order": {
                    "portString": "order",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "invert_x": {
                    "portString": "invertX",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "invert_y": {
                    "portString": "invertY",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "invert_z": {
                    "portString": "invertZ",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "color_to_signed": {
                    "portString": "colorToSigned",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "tangent_space": {
                    "portString": "tangentSpace",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "scale": {
                    "portString": "scale",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        # texture.environment
        "sky": {
            "categoryString": "aiSky",
            "port": {
                "color": {
                    "portString": "color",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "intensity": {
                    "portString": "intensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "visibility": {
                    "portString": "visibility",
                    "datatypeString": {
                        "integer": "bool"
                    }
                },
                "opaque_alpha": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "format": {
                    "portString": "format",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "X_angle": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "Y_angle": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "Z_angle": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                },
                "X": {
                    "portString": None,
                    "datatypeString": {
                        "vector3": None
                    }
                },
                "Y": {
                    "portString": None,
                    "datatypeString": {
                        "vector3": None
                    }
                },
                "Z": {
                    "portString": None,
                    "datatypeString": {
                        "vector3": None
                    }
                }
            }
        },
        "physical_sky": {
            "categoryString": "aiPhysicalSky",
            "port": {
                "turbidity": {
                    "portString": "turbidity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "ground_albedo": {
                    "portString": "groundAlbedo",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "use_degrees": {
                    "portString": "useDegrees",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "elevation": {
                    "portString": "elevation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "azimuth": {
                    "portString": "azimuth",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sun_direction": {
                    "portString": "sunDirection",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "enable_sun": {
                    "portString": "enableSun",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "sun_size": {
                    "portString": "sunSize",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sun_tint": {
                    "portString": "sunTint",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "sky_tint": {
                    "portString": "skyTint",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "intensity": {
                    "portString": "intensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "X": {
                    "portString": "X",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "Y": {
                    "portString": "Y",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "Z": {
                    "portString": "Z",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        # state
        "state_int": {
            "categoryString": "aiStateInt",
            "port": {
                "variable": {
                    "portString": "variable",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "state_float": {
            "categoryString": "aiStateFloat",
            "port": {
                "variable": {
                    "portString": "variable",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "state_vector": {
            "categoryString": "aiStateVector",
            "port": {
                "variable": {
                    "portString": "variable",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        # atmosphere
        "atmosphere_volume": {
            "categoryString": "aiAtmosphereVolume",
            "port": {
                "density": {
                    "portString": "density",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "samples": {
                    "portString": "samples",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "eccentricity": {
                    "portString": "eccentricity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "attenuation": {
                    "portString": "attenuation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "affect_camera": {
                    "portString": "affectCamera",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "affect_diffuse": {
                    "portString": "affectDiffuse",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "affect_specular": {
                    "portString": "affectSpecular",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "rgb_density": {
                    "portString": "rgbDensity",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "rgb_attenuation": {
                    "portString": "rgbAttenuation",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "fog": {
            "categoryString": "aiFog",
            "port": {
                "distance": {
                    "portString": "distance",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "height": {
                    "portString": "height",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "color": {
                    "portString": "color",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "ground_point": {
                    "portString": "groundPoint",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "ground_normal": {
                    "portString": "groundNormal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        # color
        "color_convert": {
            "categoryString": "aiColorConvert",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "from": {
                    "portString": "from",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "to": {
                    "portString": "to",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "color_correct": {
            "categoryString": "aiColorCorrect",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "alpha_is_luminance": {
                    "portString": "alphaIsLuminance",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "alpha_multiply": {
                    "portString": "alphaMultiply",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "alpha_add": {
                    "portString": "alphaAdd",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "invert": {
                    "portString": "invert",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "invert_alpha": {
                    "portString": "invertAlpha",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "gamma": {
                    "portString": "gamma",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "hue_shift": {
                    "portString": "hueShift",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "saturation": {
                    "portString": "saturation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "contrast": {
                    "portString": "contrast",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "contrast_pivot": {
                    "portString": "contrastPivot",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "exposure": {
                    "portString": "exposure",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "multiply": {
                    "portString": "multiply",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "add": {
                    "portString": "add",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "mask": {
                    "portString": "mask",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "color_jitter": {
            "categoryString": "aiColorJitter",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "data_input": {
                    "portString": "dataInput",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "data_gain_min": {
                    "portString": "dataGainMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "data_gain_max": {
                    "portString": "dataGainMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "data_hue_min": {
                    "portString": "dataHueMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "data_hue_max": {
                    "portString": "dataHueMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "data_saturation_min": {
                    "portString": "dataSaturationMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "data_saturation_max": {
                    "portString": "dataSaturationMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "data_seed": {
                    "portString": "dataSeed",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "proc_gain_min": {
                    "portString": "procGainMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "proc_gain_max": {
                    "portString": "procGainMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "proc_hue_min": {
                    "portString": "procHueMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "proc_hue_max": {
                    "portString": "procHueMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "proc_saturation_min": {
                    "portString": "procSaturationMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "proc_saturation_max": {
                    "portString": "procSaturationMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "proc_seed": {
                    "portString": "procSeed",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "obj_gain_min": {
                    "portString": "objGainMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "obj_gain_max": {
                    "portString": "objGainMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "obj_hue_min": {
                    "portString": "objHueMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "obj_hue_max": {
                    "portString": "objHueMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "obj_saturation_min": {
                    "portString": "objSaturationMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "obj_saturation_max": {
                    "portString": "objSaturationMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "obj_seed": {
                    "portString": "objSeed",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "face_gain_min": {
                    "portString": "faceGainMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "face_gain_max": {
                    "portString": "faceGainMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "face_hue_min": {
                    "portString": "faceHueMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "face_hue_max": {
                    "portString": "faceHueMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "face_saturation_min": {
                    "portString": "faceSaturationMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "face_saturation_max": {
                    "portString": "faceSaturationMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "face_seed": {
                    "portString": "faceSeed",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "face_mode": {
                    "portString": "faceMode",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        # layer
        "layer_float": {
            "categoryString": "aiLayerFloat",
            "port": {
                "enable1": {
                    "portString": "enable1",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name1": {
                    "portString": "name1",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mix1": {
                    "portString": "mix1",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable2": {
                    "portString": "enable2",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name2": {
                    "portString": "name2",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mix2": {
                    "portString": "mix2",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable3": {
                    "portString": "enable3",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name3": {
                    "portString": "name3",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input3": {
                    "portString": "input3",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mix3": {
                    "portString": "mix3",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable4": {
                    "portString": "enable4",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name4": {
                    "portString": "name4",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input4": {
                    "portString": "input4",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mix4": {
                    "portString": "mix4",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable5": {
                    "portString": "enable5",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name5": {
                    "portString": "name5",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input5": {
                    "portString": "input5",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mix5": {
                    "portString": "mix5",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable6": {
                    "portString": "enable6",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name6": {
                    "portString": "name6",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input6": {
                    "portString": "input6",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mix6": {
                    "portString": "mix6",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable7": {
                    "portString": "enable7",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name7": {
                    "portString": "name7",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input7": {
                    "portString": "input7",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mix7": {
                    "portString": "mix7",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable8": {
                    "portString": "enable8",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name8": {
                    "portString": "name8",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input8": {
                    "portString": "input8",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "mix8": {
                    "portString": "mix8",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "layer_rgba": {
            "categoryString": "aiLayerRgba",
            "port": {
                "enable1": {
                    "portString": "enable1",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name1": {
                    "portString": "name1",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mix1": {
                    "portString": "mix1",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "operation1": {
                    "portString": "operation1",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation1": {
                    "portString": "alphaOperation1",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "enable2": {
                    "portString": "enable2",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name2": {
                    "portString": "name2",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mix2": {
                    "portString": "mix2",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "operation2": {
                    "portString": "operation2",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation2": {
                    "portString": "alphaOperation2",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "enable3": {
                    "portString": "enable3",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name3": {
                    "portString": "name3",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input3": {
                    "portString": "input3",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mix3": {
                    "portString": "mix3",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "operation3": {
                    "portString": "operation3",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation3": {
                    "portString": "alphaOperation3",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "enable4": {
                    "portString": "enable4",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name4": {
                    "portString": "name4",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input4": {
                    "portString": "input4",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mix4": {
                    "portString": "mix4",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "operation4": {
                    "portString": "operation4",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation4": {
                    "portString": "alphaOperation4",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "enable5": {
                    "portString": "enable5",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name5": {
                    "portString": "name5",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input5": {
                    "portString": "input5",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mix5": {
                    "portString": "mix5",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "operation5": {
                    "portString": "operation5",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation5": {
                    "portString": "alphaOperation5",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "enable6": {
                    "portString": "enable6",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name6": {
                    "portString": "name6",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input6": {
                    "portString": "input6",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mix6": {
                    "portString": "mix6",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "operation6": {
                    "portString": "operation6",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation6": {
                    "portString": "alphaOperation6",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "enable7": {
                    "portString": "enable7",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name7": {
                    "portString": "name7",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input7": {
                    "portString": "input7",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mix7": {
                    "portString": "mix7",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "operation7": {
                    "portString": "operation7",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation7": {
                    "portString": "alphaOperation7",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "enable8": {
                    "portString": "enable8",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name8": {
                    "portString": "name8",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input8": {
                    "portString": "input8",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "mix8": {
                    "portString": "mix8",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "operation8": {
                    "portString": "operation8",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation8": {
                    "portString": "alphaOperation8",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "clamp": {
                    "portString": "clamp",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "layer_shader": {
            "categoryString": "aiLayerShader",
            "port": {
                "enable1": {
                    "portString": "enable1",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name1": {
                    "portString": "name1",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "mix1": {
                    "portString": "mix1",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable2": {
                    "portString": "enable2",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name2": {
                    "portString": "name2",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "mix2": {
                    "portString": "mix2",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable3": {
                    "portString": "enable3",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name3": {
                    "portString": "name3",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input3": {
                    "portString": "input3",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "mix3": {
                    "portString": "mix3",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable4": {
                    "portString": "enable4",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name4": {
                    "portString": "name4",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input4": {
                    "portString": "input4",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "mix4": {
                    "portString": "mix4",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable5": {
                    "portString": "enable5",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name5": {
                    "portString": "name5",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input5": {
                    "portString": "input5",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "mix5": {
                    "portString": "mix5",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable6": {
                    "portString": "enable6",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name6": {
                    "portString": "name6",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input6": {
                    "portString": "input6",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "mix6": {
                    "portString": "mix6",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable7": {
                    "portString": "enable7",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name7": {
                    "portString": "name7",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input7": {
                    "portString": "input7",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "mix7": {
                    "portString": "mix7",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "enable8": {
                    "portString": "enable8",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "name8": {
                    "portString": "name8",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "input8": {
                    "portString": "input8",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "mix8": {
                    "portString": "mix8",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        # mix
        "mix_rgba": {
            "categoryString": None,
            "port": {
                "input1": {
                    "portString": None,
                    "datatypeString": {
                        "color4": None
                    }
                },
                "input2": {
                    "portString": None,
                    "datatypeString": {
                        "color4": None
                    }
                },
                "mix": {
                    "portString": None,
                    "datatypeString": {
                        "float": None
                    }
                }
            }
        },
        "mix_shader": {
            "categoryString": "aiMixShader",
            "port": {
                "mode": {
                    "portString": "mode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "mix": {
                    "portString": "mix",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "shader1": {
                    "portString": "shader1",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "shader2": {
                    "portString": "shader2",
                    "datatypeString": {
                        "closure": "float3"
                    }
                }
            }
        },
        # volume
        "standard_volume": {
            "categoryString": "aiStandardVolume",
            "port": {
                "density": {
                    "portString": "density",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "density_channel": {
                    "portString": "densityChannel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "scatter": {
                    "portString": "scatter",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "scatter_color": {
                    "portString": "scatterColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "scatter_color_channel": {
                    "portString": "scatterColorChannel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "scatter_anisotropy": {
                    "portString": "scatterAnisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transparent": {
                    "portString": "transparent",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "transparent_depth": {
                    "portString": "transparentDepth",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "transparent_channel": {
                    "portString": "transparentChannel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "emission_mode": {
                    "portString": "emissionMode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "emission": {
                    "portString": "emission",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "emission_color": {
                    "portString": "emissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "emission_channel": {
                    "portString": "emissionChannel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "temperature": {
                    "portString": "temperature",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "temperature_channel": {
                    "portString": "temperatureChannel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "blackbody_kelvin": {
                    "portString": "blackbodyKelvin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "blackbody_intensity": {
                    "portString": "blackbodyIntensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "displacement": {
                    "portString": "displacement",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "interpolation": {
                    "portString": "interpolation",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "volume_sample_float": {
            "categoryString": "aiVolumeSampleFloat",
            "port": {
                "channel": {
                    "portString": "channel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "position_offset": {
                    "portString": "positionOffset",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "interpolation": {
                    "portString": "interpolation",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "volume_type": {
                    "portString": "volumeType",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "sdf_offset": {
                    "portString": "sdfOffset",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sdf_blend": {
                    "portString": "sdfBlend",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "sdf_invert": {
                    "portString": "sdfInvert",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "input_min": {
                    "portString": "inputMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "input_max": {
                    "portString": "inputMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "contrast": {
                    "portString": "contrast",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "contrast_pivot": {
                    "portString": "contrastPivot",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "bias": {
                    "portString": "bias",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "gain": {
                    "portString": "gain",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "output_min": {
                    "portString": "outputMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "output_max": {
                    "portString": "outputMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "clamp_min": {
                    "portString": "clampMin",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "clamp_max": {
                    "portString": "clampMax",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "volume_sample_rgb": {
            "categoryString": "aiVolumeSampleRgb",
            "port": {
                "channel": {
                    "portString": "channel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "position_offset": {
                    "portString": "positionOffset",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "interpolation": {
                    "portString": "interpolation",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "gamma": {
                    "portString": "gamma",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "hue_shift": {
                    "portString": "hueShift",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "saturation": {
                    "portString": "saturation",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "contrast": {
                    "portString": "contrast",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "contrast_pivot": {
                    "portString": "contrastPivot",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "exposure": {
                    "portString": "exposure",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "multiply": {
                    "portString": "multiply",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "add": {
                    "portString": "add",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        # utility
        "clamp": {
            "categoryString": "aiClamp",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "mode": {
                    "portString": "mode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "min": {
                    "portString": "min",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "max": {
                    "portString": "max",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "min_color": {
                    "portString": "minColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "max_color": {
                    "portString": "maxColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "cache": {
            "categoryString": "aiCache",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "curvature": {
            "categoryString": "aiCurvature",
            "port": {
                "output": {
                    "portString": "output",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "samples": {
                    "portString": "samples",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "radius": {
                    "portString": "radius",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "spread": {
                    "portString": "spread",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "threshold": {
                    "portString": "threshold",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "bias": {
                    "portString": "bias",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "multiply": {
                    "portString": "multiply",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "trace_set": {
                    "portString": "traceSet",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "inclusive": {
                    "portString": "inclusive",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "self_only": {
                    "portString": "selfOnly",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "facing_ratio": {
            "categoryString": "aiFacingRatio",
            "port": {
                "bias": {
                    "portString": "bias",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "gain": {
                    "portString": "gain",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "linear": {
                    "portString": "linear",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "invert": {
                    "portString": "invert",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "flat": {
            "categoryString": "aiFlat",
            "port": {
                "color": {
                    "portString": "color",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "matte": {
            "categoryString": "aiMatte",
            "port": {
                "passthrough": {
                    "portString": "passthrough",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "color": {
                    "portString": "color",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "opacity": {
                    "portString": "opacity",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "max": {
            "categoryString": "aiMax",
            "port": {
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "min": {
            "categoryString": "aiMin",
            "port": {
                "input1": {
                    "portString": "input1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "input2": {
                    "portString": "input2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                }
            }
        },
        "motion_vector": {
            "categoryString": "aiMotionVector",
            "port": {
                "raw": {
                    "portString": "raw",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "time0": {
                    "portString": "time0",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "time1": {
                    "portString": "time1",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "max_displace": {
                    "portString": "maxDisplace",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "space_transform": {
            "categoryString": "aiSpaceTransform",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "type": {
                    "portString": "type",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "from": {
                    "portString": "from",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "to": {
                    "portString": "to",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "tangent": {
                    "portString": "tangent",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "normalize": {
                    "portString": "normalize",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "scale": {
                    "portString": "scale",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "passthrough": {
            "categoryString": "aiPassthrough",
            "port": {
                "passthrough": {
                    "portString": "passthrough",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval1": {
                    "portString": "eval1",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval2": {
                    "portString": "eval2",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval3": {
                    "portString": "eval3",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval4": {
                    "portString": "eval4",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval5": {
                    "portString": "eval5",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval6": {
                    "portString": "eval6",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval7": {
                    "portString": "eval7",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval8": {
                    "portString": "eval8",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval9": {
                    "portString": "eval9",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval10": {
                    "portString": "eval10",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval11": {
                    "portString": "eval11",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval12": {
                    "portString": "eval12",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval13": {
                    "portString": "eval13",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval14": {
                    "portString": "eval14",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval15": {
                    "portString": "eval15",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval16": {
                    "portString": "eval16",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval17": {
                    "portString": "eval17",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval18": {
                    "portString": "eval18",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval19": {
                    "portString": "eval19",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "eval20": {
                    "portString": "eval20",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "random": {
            "categoryString": "aiRandom",
            "port": {
                "input_type": {
                    "portString": "inputType",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "input_int": {
                    "portString": "inputInt",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "input_float": {
                    "portString": "inputFloat",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "input_color": {
                    "portString": "inputColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "seed": {
                    "portString": "seed",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "grayscale": {
                    "portString": "grayscale",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "range": {
            "categoryString": "aiRange",
            "port": {
                "input": {
                    "portString": "input",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "input_min": {
                    "portString": "inputMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "input_max": {
                    "portString": "inputMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "output_min": {
                    "portString": "outputMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "output_max": {
                    "portString": "outputMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "smoothstep": {
                    "portString": "smoothstep",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "contrast": {
                    "portString": "contrast",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "contrast_pivot": {
                    "portString": "contrastPivot",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "bias": {
                    "portString": "bias",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "gain": {
                    "portString": "gain",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "trace_set": {
            "categoryString": "aiTraceSet",
            "port": {
                "passthrough": {
                    "portString": "passthrough",
                    "datatypeString": {
                        "closure": "float3"
                    }
                },
                "trace_set": {
                    "portString": "traceSet",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "inclusive": {
                    "portString": "inclusive",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "cell_noise": {
            "categoryString": "aiCellNoise",
            "port": {
                "pattern": {
                    "portString": "pattern",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "additive": {
                    "portString": "additive",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "octaves": {
                    "portString": "octaves",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "randomness": {
                    "portString": "randomness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "lacunarity": {
                    "portString": "lacunarity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "amplitude": {
                    "portString": "amplitude",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "scale": {
                    "portString": "scale",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "offset": {
                    "portString": "offset",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "coord_space": {
                    "portString": "coordSpace",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "pref_name": {
                    "portString": "prefName",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "P": {
                    "portString": "P",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "time": {
                    "portString": "time",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "color": {
                    "portString": "color",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "palette": {
                    "portString": "palette",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "density": {
                    "portString": "density",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "noise": {
            "categoryString": "aiNoise",
            "port": {
                "octaves": {
                    "portString": "octaves",
                    "datatypeString": {
                        "integer": "long"
                    }
                },
                "distortion": {
                    "portString": "distortion",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "lacunarity": {
                    "portString": "lacunarity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "amplitude": {
                    "portString": "amplitude",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "scale": {
                    "portString": "scale",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "offset": {
                    "portString": "offset",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "coord_space": {
                    "portString": "coordSpace",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "pref_name": {
                    "portString": "prefName",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "P": {
                    "portString": "P",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "time": {
                    "portString": "time",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "color1": {
                    "portString": "color1",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "color2": {
                    "portString": "color2",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "mode": {
                    "portString": "mode",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        "maya_layered_shader": {
            "categoryString": u'layeredShader',
            "port": {
                "compositingFlag": {
                    "portString": u'compositingFlag',
                    "datatypeString": {
                        "string": u'enum'
                    }
                },
                "numInputs": {
                    "portString": None,
                    "datatypeString": {
                        "integer": None
                    }
                },
                "color0": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color1": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color2": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color3": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color4": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color5": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color6": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color7": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color8": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color9": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color10": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color11": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color12": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color13": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color14": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "color15": {
                    "portString": None,
                    "datatypeString": {
                        "closure": None
                    }
                },
                "transparency0": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency1": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency2": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency3": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency4": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency5": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency6": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency7": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency8": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency9": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency10": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency11": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency12": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency13": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency14": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "transparency15": {
                    "portString": None,
                    "datatypeString": {
                        "color3": None
                    }
                },
                "useTransparency0": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency1": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency2": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency3": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency4": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency5": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency6": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency7": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency8": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency9": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency10": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency11": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency12": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency13": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency14": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                },
                "useTransparency15": {
                    "portString": None,
                    "datatypeString": {
                        "boolean": None
                    }
                }
            }
        },
        "shuffle": {
            "categoryString": "aiShuffle",
            "port": {
                "color": {
                    "portString": "color",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "alpha": {
                    "portString": "alpha",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "channel_r": {
                    "portString": "channelR",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "channel_g": {
                    "portString": "channelG",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "channel_b": {
                    "portString": "channelB",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "channel_a": {
                    "portString": "channelA",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "negate_r": {
                    "portString": "negateR",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "negate_g": {
                    "portString": "negateG",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "negate_b": {
                    "portString": "negateB",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "negate_a": {
                    "portString": "negateA",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                }
            }
        },
        "volume_collector": {
            "categoryString": "aiVolumeCollector",
            "port": {
                "scattering_source": {
                    "portString": "scatteringSource",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "scattering": {
                    "portString": "scattering",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "scattering_channel": {
                    "portString": "scatteringChannel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "scattering_color": {
                    "portString": "scatteringColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "scattering_intensity": {
                    "portString": "scatteringIntensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "anisotropy": {
                    "portString": "anisotropy",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "attenuation_source": {
                    "portString": "attenuationSource",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "attenuation": {
                    "portString": "attenuation",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "attenuation_channel": {
                    "portString": "attenuationChannel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "attenuation_color": {
                    "portString": "attenuationColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "attenuation_intensity": {
                    "portString": "attenuationIntensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "attenuation_mode": {
                    "portString": "attenuationMode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "emission_source": {
                    "portString": "emissionSource",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "emission": {
                    "portString": "emission",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "emission_channel": {
                    "portString": "emissionChannel",
                    "datatypeString": {
                        "string": "typed"
                    }
                },
                "emission_color": {
                    "portString": "emissionColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "emission_intensity": {
                    "portString": "emissionIntensity",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "position_offset": {
                    "portString": "positionOffset",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                },
                "interpolation": {
                    "portString": "interpolation",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        #
        "utility": {
            "categoryString": "aiUtility",
            "port": {
                "color_mode": {
                    "portString": "colorMode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "shade_mode": {
                    "portString": "shadeMode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "overlay_mode": {
                    "portString": "overlayMode",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "color": {
                    "portString": "color",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "ao_distance": {
                    "portString": "aoDistance",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "roughness": {
                    "portString": "roughness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "normal": {
                    "portString": "normal",
                    "datatypeString": {
                        "vector3": "float3"
                    }
                }
            }
        },
        "wireframe": {
            "categoryString": "aiWireframe",
            "port": {
                "line_width": {
                    "portString": "lineWidth",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "fill_color": {
                    "portString": "fillColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "line_color": {
                    "portString": "lineColor",
                    "datatypeString": {
                        "color3": "float3"
                    }
                },
                "raster_space": {
                    "portString": "rasterSpace",
                    "datatypeString": {
                        "boolean": "bool"
                    }
                },
                "edge_type": {
                    "portString": "edgeType",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        },
        # ray switch
        "ray_switch_rgba": {
            "categoryString": u'aiRaySwitch',
            "port": {
                "camera": {
                    "portString": u'camera',
                    "datatypeString": {
                        "color4": None
                    }
                },
                "shadow": {
                    "portString": u'shadow',
                    "datatypeString": {
                        "color4": None
                    }
                },
                "diffuse_reflection": {
                    "portString": u'diffuseReflection',
                    "datatypeString": {
                        "color4": None
                    }
                },
                "diffuse_transmission": {
                    "portString": u'diffuseTransmission',
                    "datatypeString": {
                        "color4": None
                    }
                },
                "specular_reflection": {
                    "portString": u'specularReflection',
                    "datatypeString": {
                        "color4": None
                    }
                },
                "specular_transmission": {
                    "portString": u'specularTransmission',
                    "datatypeString": {
                        "color4": None
                    }
                },
                "volume": {
                    "portString": 'volume',
                    "datatypeString": {
                        "color4": None
                    }
                }
            }
        },
        "ray_switch_shader": {
            "categoryString": u'aiRaySwitch',
            "port": {
                "camera": {
                    "portString": 'camera',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "shadow": {
                    "portString": u'shadow',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "diffuse_reflection": {
                    "portString": u'diffuseReflection',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "diffuse_transmission": {
                    "portString": u'diffuseTransmission',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "specular_reflection": {
                    "portString": u'specularReflection',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "specular_transmission": {
                    "portString": u'specularTransmission',
                    "datatypeString": {
                        "closure": None
                    }
                },
                "volume": {
                    "portString": u'volume',
                    "datatypeString": {
                        "closure": None
                    }
                }
            }
        },
        #
        "thin_film": {
            "categoryString": "aiThinFilm",
            "port": {
                "thickness_min": {
                    "portString": "thicknessMin",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "thickness_max": {
                    "portString": "thicknessMax",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "thickness": {
                    "portString": "thickness",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "ior_medium": {
                    "portString": "iorMedium",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "ior_film": {
                    "portString": "iorFilm",
                    "datatypeString": {
                        "float": "float"
                    }
                },
                "ior_internal": {
                    "portString": "iorInternal",
                    "datatypeString": {
                        "float": "float"
                    }
                }
            }
        },
        "composite": {
            "categoryString": "aiComposite",
            "port": {
                "A": {
                    "portString": "A",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "B": {
                    "portString": "B",
                    "datatypeString": {
                        "color4": "float3"
                    }
                },
                "operation": {
                    "portString": "operation",
                    "datatypeString": {
                        "string": "enum"
                    }
                },
                "alpha_operation": {
                    "portString": "alphaOperation",
                    "datatypeString": {
                        "string": "enum"
                    }
                }
            }
        }
    }
