# coding:utf-8


class Utility(object):
    DEF_mtl_data_separator = u','
    DEF_mtl_data_array_separator = u', '

    DEF_mya_separator_node = u'|'
    DEF_mtl_namespace_separator = u':'
    DEF_mtl_node_separator = u'/'
    DEF_mtl_file_separator = u'/'
    DEF_mtl_port_separator = u'.'

    DEF_mtl_key_type = u'datatypeString'
    DEF_mtl_key_value = u'valueString'
    DEF_mtl_key_port = u'port'

    DEF_mtl_key_port_string = u'portString'

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

    DEF_mtl_geometry_def_dict = {
        'property': [
            {
                "name": "opaque",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "matte",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "use_shadow_group",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "motion_start",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "name": "motion_end",
                "datatypeString": "float",
                "valueString": "1"
            },
            {
                "name": "id",
                "datatypeString": "integer",
                "valueString": "0"
            },
            {
                "name": "smoothing",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "subdiv_type",
                "datatypeString": "string",
                "valueString": "none"
            },
            {
                "name": "subdiv_iterations",
                "datatypeString": "integer",
                "valueString": "0"
            },
            {
                "name": "subdiv_adaptive_error",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "name": "subdiv_adaptive_metric",
                "datatypeString": "string",
                "valueString": "auto"
            },
            {
                "name": "subdiv_adaptive_space",
                "datatypeString": "string",
                "valueString": "raster"
            },
            {
                "name": "subdiv_uv_smoothing",
                "datatypeString": "string",
                "valueString": "pin_corners"
            },
            {
                "name": "subdiv_frustum_ignore",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "subdiv_smooth_derivs",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "disp_padding",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "name": "disp_height",
                "datatypeString": "float",
                "valueString": "1"
            },
            {
                "name": "disp_zero_value",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "name": "disp_autobump",
                "datatypeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "autobump_visibility",
                "datatypeString": "integer",
                "valueString": "1"
            },
            {
                "name": "step_size",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "name": "volume_padding",
                "datatypeString": "float",
                "valueString": "0"
            },
            {
                "name": "invert_normals",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "self_shadows",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "receive_shadows",
                "datatypeString": "boolean",
                "valueString": "true"
            }
        ],
        'visibility': [
            {
                "name": "camera",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "shadow",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "diffuse_transmit",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "specular_transmit",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "volume",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "diffuse_reflect",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "specular_reflect",
                "datatypeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "subsurface",
                "datatypeString": "boolean",
                "valueString": "true"
            },
        ]
    }

    DEF_mtl_node_def_dict = {
        "ray_switch_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "camera",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "shadow",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "diffuse_reflection",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "diffuse_transmission",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "specular_reflection",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "specular_transmission",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "volume",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                }
            ]
        },
        "ray_switch_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "camera",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "shadow",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "diffuse_reflection",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "diffuse_transmission",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "specular_reflection",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "specular_transmission",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "volume",
                    "datatypeString": "closure",
                    "valueString": ""
                }
            ]
        },
        "image": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "filename",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "color_space",
                    "datatypeString": "string",
                    "valueString": "auto"
                },
                {
                    "portString": "filter",
                    "datatypeString": "string",
                    "valueString": "smart_bicubic"
                },
                {
                    "portString": "mipmap_bias",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "single_channel",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "start_channel",
                    "datatypeString": "integer",
                    "valueString": "-401153280"
                },
                {
                    "portString": "swrap",
                    "datatypeString": "string",
                    "valueString": "periodic"
                },
                {
                    "portString": "twrap",
                    "datatypeString": "string",
                    "valueString": "periodic"
                },
                {
                    "portString": "sscale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "tscale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "sflip",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "tflip",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "soffset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "toffset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "swap_st",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "uvcoords",
                    "datatypeString": "vector2",
                    "valueString": "0, 0"
                },
                {
                    "portString": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "multiply",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "offset",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "ignore_missing_textures",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "missing_texture_color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                }
            ]
        },
        "noise": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "octaves",
                    "datatypeString": "integer",
                    "valueString": "1"
                },
                {
                    "portString": "distortion",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "lacunarity",
                    "datatypeString": "float",
                    "valueString": "1.92"
                },
                {
                    "portString": "amplitude",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "scale",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "coord_space",
                    "datatypeString": "string",
                    "valueString": "object"
                },
                {
                    "portString": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "P",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "time",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "color1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "color2",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "scalar"
                }
            ]
        },
        "cell_noise": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "pattern",
                    "datatypeString": "string",
                    "valueString": "noise1"
                },
                {
                    "portString": "additive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "octaves",
                    "datatypeString": "integer",
                    "valueString": "1"
                },
                {
                    "portString": "randomness",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "lacunarity",
                    "datatypeString": "float",
                    "valueString": "1.92"
                },
                {
                    "portString": "amplitude",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "scale",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "coord_space",
                    "datatypeString": "string",
                    "valueString": "object"
                },
                {
                    "portString": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "P",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "time",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "palette",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "density",
                    "datatypeString": "float",
                    "valueString": "0.5"
                }
            ]
        },
        "utility": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "color_mode",
                    "datatypeString": "string",
                    "valueString": "color"
                },
                {
                    "portString": "shade_mode",
                    "datatypeString": "string",
                    "valueString": "ndoteye"
                },
                {
                    "portString": "overlay_mode",
                    "datatypeString": "string",
                    "valueString": "none"
                },
                {
                    "portString": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "ao_distance",
                    "datatypeString": "float",
                    "valueString": "100"
                },
                {
                    "portString": "roughness",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "wireframe": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "line_width",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "fill_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "line_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "raster_space",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "edge_type",
                    "datatypeString": "string",
                    "valueString": "triangles"
                }
            ]
        },
        "motion_vector": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "raw",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "time0",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "time1",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "max_displace",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "ambient_occlusion": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "samples",
                    "datatypeString": "integer",
                    "valueString": "3"
                },
                {
                    "portString": "spread",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "near_clip",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "far_clip",
                    "datatypeString": "float",
                    "valueString": "100"
                },
                {
                    "portString": "falloff",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "black",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "white",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "invert_normals",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "self_only",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "round_corners": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "samples",
                    "datatypeString": "integer",
                    "valueString": "6"
                },
                {
                    "portString": "radius",
                    "datatypeString": "float",
                    "valueString": "0.01"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "self_only",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "object_space",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "flat": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "toon": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "mask_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "edge_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "edge_tonemap",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "edge_opacity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "edge_width_scale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "silhouette_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "silhouette_tonemap",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "silhouette_opacity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "silhouette_width_scale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "priority",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "enable_silhouette",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "ignore_throughput",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "enable",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "id_difference",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "shader_difference",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "uv_threshold",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "angle_threshold",
                    "datatypeString": "float",
                    "valueString": "180"
                },
                {
                    "portString": "normal_type",
                    "datatypeString": "string",
                    "valueString": "shading normal"
                },
                {
                    "portString": "base",
                    "datatypeString": "float",
                    "valueString": "0.8"
                },
                {
                    "portString": "base_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "base_tonemap",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "specular_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "specular_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "specular_tonemap",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "lights",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "highlight_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "highlight_size",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "aov_highlight",
                    "datatypeString": "string",
                    "valueString": "highlight"
                },
                {
                    "portString": "rim_light",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "rim_light_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "rim_light_width",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "aov_rim_light",
                    "datatypeString": "string",
                    "valueString": "rim_light"
                },
                {
                    "portString": "transmission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transmission_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "sheen",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "sheen_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "sheen_roughness",
                    "datatypeString": "float",
                    "valueString": "0.3"
                },
                {
                    "portString": "emission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "IOR",
                    "datatypeString": "float",
                    "valueString": "1.52"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "indirect_diffuse",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "indirect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "bump_mode",
                    "datatypeString": "string",
                    "valueString": "both"
                },
                {
                    "portString": "energy_conserving",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "user_id",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "lambert": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "Kd",
                    "datatypeString": "float",
                    "valueString": "0.7"
                },
                {
                    "portString": "Kd_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "standard": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "Kd",
                    "datatypeString": "float",
                    "valueString": "0.7"
                },
                {
                    "portString": "Kd_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "diffuse_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Ks",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Ks_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.466905"
                },
                {
                    "portString": "specular_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "specular_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "specular_distribution",
                    "datatypeString": "string",
                    "valueString": "ggx"
                },
                {
                    "portString": "Kr",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Kr_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "reflection_exit_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "reflection_exit_use_environment",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "Kt",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Kt_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transmittance",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "refraction_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "refraction_exit_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "refraction_exit_use_environment",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "IOR",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "dispersion_abbe",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Kb",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Fresnel",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "Krn",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "specular_Fresnel",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "Ksn",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Fresnel_use_IOR",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "Fresnel_affect_diff",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "emission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "direct_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "indirect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "direct_diffuse",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "indirect_diffuse",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable_glossy_caustics",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "enable_reflective_caustics",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "enable_refractive_caustics",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "enable_internal_reflections",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "Ksss",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Ksss_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "sss_radius",
                    "datatypeString": "color3",
                    "valueString": "0.1, 0.1, 0.1"
                },
                {
                    "portString": "bounce_factor",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "standard_surface": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "base",
                    "datatypeString": "float",
                    "valueString": "0.8"
                },
                {
                    "portString": "base_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "diffuse_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "portString": "specular_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "portString": "specular_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "specular_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "metalness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transmission_depth",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission_scatter",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "transmission_scatter_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission_dispersion",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission_extra_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmit_aovs",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "subsurface",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "subsurface_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "subsurface_radius",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "subsurface_scale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "subsurface_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "subsurface_type",
                    "datatypeString": "string",
                    "valueString": "randomwalk"
                },
                {
                    "portString": "sheen",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "sheen_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "sheen_roughness",
                    "datatypeString": "float",
                    "valueString": "0.3"
                },
                {
                    "portString": "thin_walled",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "coat",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "coat_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "coat_roughness",
                    "datatypeString": "float",
                    "valueString": "0.1"
                },
                {
                    "portString": "coat_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "portString": "coat_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "coat_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "coat_normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "coat_affect_color",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "coat_affect_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "thin_film_thickness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "thin_film_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "portString": "emission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "caustics",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "internal_reflections",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "exit_to_background",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "indirect_diffuse",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "indirect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "aov_id1",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id2",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id3",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id3",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id4",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id4",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id5",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id5",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id6",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id6",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id7",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id7",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id8",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id8",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "hair": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "rootcolor",
                    "datatypeString": "color3",
                    "valueString": "0.1, 0.1, 0.1"
                },
                {
                    "portString": "tipcolor",
                    "datatypeString": "color3",
                    "valueString": "0.5, 0.5, 0.5"
                },
                {
                    "portString": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "ambdiff",
                    "datatypeString": "float",
                    "valueString": "0.6"
                },
                {
                    "portString": "spec",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "spec_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "spec_shift",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "spec_gloss",
                    "datatypeString": "float",
                    "valueString": "10"
                },
                {
                    "portString": "spec2",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "spec2_color",
                    "datatypeString": "color3",
                    "valueString": "1, 0.4, 0.1"
                },
                {
                    "portString": "spec2_shift",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "spec2_gloss",
                    "datatypeString": "float",
                    "valueString": "7"
                },
                {
                    "portString": "transmission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transmission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 0.4, 0.1"
                },
                {
                    "portString": "transmission_spread",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "kd_ind",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "standard_hair": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "base",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "base_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "melanin",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "melanin_redness",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "melanin_randomize",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "roughness",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "portString": "roughness_azimuthal",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "portString": "roughness_anisotropic",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "ior",
                    "datatypeString": "float",
                    "valueString": "1.55"
                },
                {
                    "portString": "shift",
                    "datatypeString": "float",
                    "valueString": "3"
                },
                {
                    "portString": "specular_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular2_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transmission_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "diffuse",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "diffuse_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "emission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "indirect_diffuse",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "indirect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "extra_depth",
                    "datatypeString": "integer",
                    "valueString": "16"
                },
                {
                    "portString": "extra_samples",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "aov_id1",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id2",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id3",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id3",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id4",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id4",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id5",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id5",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id6",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id6",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id7",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id7",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_id8",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "id8",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "car_paint": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "base",
                    "datatypeString": "float",
                    "valueString": "0.8"
                },
                {
                    "portString": "base_color",
                    "datatypeString": "color3",
                    "valueString": "1, 0, 0"
                },
                {
                    "portString": "base_roughness",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular_flip_flop",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular_light_facing",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular_falloff",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.05"
                },
                {
                    "portString": "specular_IOR",
                    "datatypeString": "float",
                    "valueString": "1.52"
                },
                {
                    "portString": "transmission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "flake_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "flake_flip_flop",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "flake_light_facing",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "flake_falloff",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "flake_roughness",
                    "datatypeString": "float",
                    "valueString": "0.4"
                },
                {
                    "portString": "flake_IOR",
                    "datatypeString": "float",
                    "valueString": "100"
                },
                {
                    "portString": "flake_scale",
                    "datatypeString": "float",
                    "valueString": "0.001"
                },
                {
                    "portString": "flake_density",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "flake_layers",
                    "datatypeString": "integer",
                    "valueString": "1"
                },
                {
                    "portString": "flake_normal_randomize",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "flake_coord_space",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "coat",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "coat_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "coat_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "coat_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "portString": "coat_normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "bump2d": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "bump_map",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "bump_height",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "bump3d": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "bump_map",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "bump_height",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "epsilon",
                    "datatypeString": "float",
                    "valueString": "1e-05"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "mix_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "blend"
                },
                {
                    "portString": "mix",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "shader1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "shader2",
                    "datatypeString": "closure",
                    "valueString": ""
                }
            ]
        },
        "sky": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "visibility",
                    "datatypeString": "integer",
                    "valueString": "-940211969"
                },
                {
                    "portString": "opaque_alpha",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "format",
                    "datatypeString": "string",
                    "valueString": "angular"
                },
                {
                    "portString": "X_angle",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Y_angle",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "Z_angle",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "X",
                    "datatypeString": "vector3",
                    "valueString": "1, 0, 0"
                },
                {
                    "portString": "Y",
                    "datatypeString": "vector3",
                    "valueString": "0, 1, 0"
                },
                {
                    "portString": "Z",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 1"
                }
            ]
        },
        "physical_sky": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "turbidity",
                    "datatypeString": "float",
                    "valueString": "3"
                },
                {
                    "portString": "ground_albedo",
                    "datatypeString": "color3",
                    "valueString": "0.1, 0.1, 0.1"
                },
                {
                    "portString": "use_degrees",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "elevation",
                    "datatypeString": "float",
                    "valueString": "45"
                },
                {
                    "portString": "azimuth",
                    "datatypeString": "float",
                    "valueString": "90"
                },
                {
                    "portString": "sun_direction",
                    "datatypeString": "vector3",
                    "valueString": "0, 1, 0"
                },
                {
                    "portString": "enable_sun",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "sun_size",
                    "datatypeString": "float",
                    "valueString": "0.51"
                },
                {
                    "portString": "sun_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "sky_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "X",
                    "datatypeString": "vector3",
                    "valueString": "1, 0, 0"
                },
                {
                    "portString": "Y",
                    "datatypeString": "vector3",
                    "valueString": "0, 1, 0"
                },
                {
                    "portString": "Z",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 1"
                }
            ]
        },
        "atmosphere_volume": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "density",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "samples",
                    "datatypeString": "integer",
                    "valueString": "5"
                },
                {
                    "portString": "eccentricity",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "attenuation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "affect_camera",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "affect_diffuse",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "affect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "rgb_density",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "rgb_attenuation",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "fog": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "distance",
                    "datatypeString": "float",
                    "valueString": "0.02"
                },
                {
                    "portString": "height",
                    "datatypeString": "float",
                    "valueString": "5"
                },
                {
                    "portString": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "ground_point",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "ground_normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 1"
                }
            ]
        },
        "standard_volume": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "density",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "density_channel",
                    "datatypeString": "string",
                    "valueString": "density"
                },
                {
                    "portString": "scatter",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "scatter_color",
                    "datatypeString": "color3",
                    "valueString": "0.5, 0.5, 0.5"
                },
                {
                    "portString": "scatter_color_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "scatter_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "transparent",
                    "datatypeString": "color3",
                    "valueString": "0.367879, 0.367879, 0.367879"
                },
                {
                    "portString": "transparent_depth",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "transparent_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "emission_mode",
                    "datatypeString": "string",
                    "valueString": "blackbody"
                },
                {
                    "portString": "emission",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "emission_channel",
                    "datatypeString": "string",
                    "valueString": "heat"
                },
                {
                    "portString": "temperature",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "temperature_channel",
                    "datatypeString": "string",
                    "valueString": "temperature"
                },
                {
                    "portString": "blackbody_kelvin",
                    "datatypeString": "float",
                    "valueString": "5000"
                },
                {
                    "portString": "blackbody_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "displacement",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "interpolation",
                    "datatypeString": "string",
                    "valueString": "trilinear"
                }
            ]
        },
        "abs": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "add": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "aov_read_float": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_read_int": {
            "datatypeString": "integer",
            "port": [
                {
                    "portString": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_read_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_read_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_write_float": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "aov_input",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "blend_opacity",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "aov_write_int": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "aov_input",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_write_rgb": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "aov_input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "blend_opacity",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "aov_write_rgba": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "aov_input",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "blend_opacity",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "atan": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "y",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "x",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "units",
                    "datatypeString": "string",
                    "valueString": "radians"
                }
            ]
        },
        "blackbody": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "temperature",
                    "datatypeString": "float",
                    "valueString": "6500"
                },
                {
                    "portString": "normalize",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "cache": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "camera_projection": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "projection_color",
                    "datatypeString": "color4",
                    "valueString": "1, 1, 1, 1"
                },
                {
                    "portString": "offscreen_color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mask",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "camera",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "aspect_ratio",
                    "datatypeString": "float",
                    "valueString": "1.333"
                },
                {
                    "portString": "front_facing",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "back_facing",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "use_shading_normal",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "coord_space",
                    "datatypeString": "string",
                    "valueString": "world"
                },
                {
                    "portString": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "P",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "checkerboard": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "color1",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "color2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "u_frequency",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "v_frequency",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "u_offset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "v_offset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "filter_strength",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "filter_offset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "clamp": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "scalar"
                },
                {
                    "portString": "min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "min_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "max_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "clip_geo": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "intersection",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "color_convert": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "from",
                    "datatypeString": "string",
                    "valueString": "RGB"
                },
                {
                    "portString": "to",
                    "datatypeString": "string",
                    "valueString": "HSV"
                }
            ]
        },
        "color_correct": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "alpha_is_luminance",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "alpha_multiply",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "alpha_add",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "invert",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "invert_alpha",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "gamma",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "hue_shift",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "saturation",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "contrast_pivot",
                    "datatypeString": "float",
                    "valueString": "0.18"
                },
                {
                    "portString": "exposure",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "multiply",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "add",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "mask",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "color_jitter": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "data_input",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "data_gain_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "data_gain_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "data_hue_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "data_hue_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "data_saturation_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "data_saturation_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "data_seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "proc_gain_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "proc_gain_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "proc_hue_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "proc_hue_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "proc_saturation_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "proc_saturation_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "proc_seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "obj_gain_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "obj_gain_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "obj_hue_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "obj_hue_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "obj_saturation_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "obj_saturation_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "obj_seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "face_gain_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "face_gain_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "face_hue_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "face_hue_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "face_saturation_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "face_saturation_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "face_seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "face_mode",
                    "datatypeString": "string",
                    "valueString": "face id"
                }
            ]
        },
        "compare": {
            "datatypeString": "boolean",
            "port": [
                {
                    "portString": "test",
                    "datatypeString": "string",
                    "valueString": "=="
                },
                {
                    "portString": "input1",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input2",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "complement": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "complex_ior": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "material",
                    "datatypeString": "string",
                    "valueString": "custom"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "artistic"
                },
                {
                    "portString": "reflectivity",
                    "datatypeString": "color3",
                    "valueString": "0.925952, 0.720887, 0.504154"
                },
                {
                    "portString": "edgetint",
                    "datatypeString": "color3",
                    "valueString": "0.995524, 0.957415, 0.822776"
                },
                {
                    "portString": "n",
                    "datatypeString": "vector3",
                    "valueString": "0.27105, 0.67693, 1.3164"
                },
                {
                    "portString": "k",
                    "datatypeString": "vector3",
                    "valueString": "3.6092, 2.6247, 2.2921"
                }
            ]
        },
        "composite": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "A",
                    "datatypeString": "color4",
                    "valueString": "1, 0, 0, 1"
                },
                {
                    "portString": "B",
                    "datatypeString": "color4",
                    "valueString": "0, 1, 0, 1"
                },
                {
                    "portString": "operation",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation",
                    "datatypeString": "string",
                    "valueString": "same"
                }
            ]
        },
        "cross": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "input2",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "curvature": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "output",
                    "datatypeString": "string",
                    "valueString": "convex"
                },
                {
                    "portString": "samples",
                    "datatypeString": "integer",
                    "valueString": "3"
                },
                {
                    "portString": "radius",
                    "datatypeString": "float",
                    "valueString": "0.1"
                },
                {
                    "portString": "spread",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "threshold",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "bias",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "multiply",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "self_only",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "divide": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "dot": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "input2",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "exp": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "facing_ratio": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "bias",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "gain",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "linear",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "invert",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "flakes": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "scale",
                    "datatypeString": "float",
                    "valueString": "0.1"
                },
                {
                    "portString": "density",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "step",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "depth",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "IOR",
                    "datatypeString": "float",
                    "valueString": "1.52"
                },
                {
                    "portString": "normal_randomize",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "coord_space",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "output_space",
                    "datatypeString": "string",
                    "valueString": "world"
                }
            ]
        },
        "float_to_int": {
            "datatypeString": "integer",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "round"
                }
            ]
        },
        "float_to_matrix": {
            "datatypeString": "matrix44",
            "port": [
                {
                    "portString": "input_00",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "input_01",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_02",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_03",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_10",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_11",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "input_12",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_13",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_20",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_21",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_22",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "input_23",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_30",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_31",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_32",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_33",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "float_to_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "r",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "g",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "b",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "a",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "float_to_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "r",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "g",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "b",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "fraction": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "is_finite": {
            "datatypeString": "boolean",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "layer_float": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "enable1",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name1",
                    "datatypeString": "string",
                    "valueString": "layer1"
                },
                {
                    "portString": "input1",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mix1",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable2",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name2",
                    "datatypeString": "string",
                    "valueString": "layer2"
                },
                {
                    "portString": "input2",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mix2",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "enable3",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name3",
                    "datatypeString": "string",
                    "valueString": "layer3"
                },
                {
                    "portString": "input3",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mix3",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "enable4",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name4",
                    "datatypeString": "string",
                    "valueString": "layer4"
                },
                {
                    "portString": "input4",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mix4",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "enable5",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name5",
                    "datatypeString": "string",
                    "valueString": "layer5"
                },
                {
                    "portString": "input5",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mix5",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "enable6",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name6",
                    "datatypeString": "string",
                    "valueString": "layer6"
                },
                {
                    "portString": "input6",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mix6",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "enable7",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name7",
                    "datatypeString": "string",
                    "valueString": "layer7"
                },
                {
                    "portString": "input7",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mix7",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "enable8",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name8",
                    "datatypeString": "string",
                    "valueString": "layer8"
                },
                {
                    "portString": "input8",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "mix8",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "layer_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "enable1",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name1",
                    "datatypeString": "string",
                    "valueString": "layer1"
                },
                {
                    "portString": "input1",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mix1",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "operation1",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation1",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "portString": "enable2",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name2",
                    "datatypeString": "string",
                    "valueString": "layer2"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mix2",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "operation2",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation2",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "portString": "enable3",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name3",
                    "datatypeString": "string",
                    "valueString": "layer3"
                },
                {
                    "portString": "input3",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mix3",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "operation3",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation3",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "portString": "enable4",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name4",
                    "datatypeString": "string",
                    "valueString": "layer4"
                },
                {
                    "portString": "input4",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mix4",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "operation4",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation4",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "portString": "enable5",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name5",
                    "datatypeString": "string",
                    "valueString": "layer5"
                },
                {
                    "portString": "input5",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mix5",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "operation5",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation5",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "portString": "enable6",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name6",
                    "datatypeString": "string",
                    "valueString": "layer6"
                },
                {
                    "portString": "input6",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mix6",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "operation6",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation6",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "portString": "enable7",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name7",
                    "datatypeString": "string",
                    "valueString": "layer7"
                },
                {
                    "portString": "input7",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mix7",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "operation7",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation7",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "portString": "enable8",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name8",
                    "datatypeString": "string",
                    "valueString": "layer8"
                },
                {
                    "portString": "input8",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "mix8",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "operation8",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "portString": "alpha_operation8",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "portString": "clamp",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "layer_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "enable1",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name1",
                    "datatypeString": "string",
                    "valueString": "layer1"
                },
                {
                    "portString": "input1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "mix1",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable2",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name2",
                    "datatypeString": "string",
                    "valueString": "layer2"
                },
                {
                    "portString": "input2",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "mix2",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable3",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name3",
                    "datatypeString": "string",
                    "valueString": "layer3"
                },
                {
                    "portString": "input3",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "mix3",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable4",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name4",
                    "datatypeString": "string",
                    "valueString": "layer4"
                },
                {
                    "portString": "input4",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "mix4",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable5",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name5",
                    "datatypeString": "string",
                    "valueString": "layer5"
                },
                {
                    "portString": "input5",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "mix5",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable6",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name6",
                    "datatypeString": "string",
                    "valueString": "layer6"
                },
                {
                    "portString": "input6",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "mix6",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable7",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name7",
                    "datatypeString": "string",
                    "valueString": "layer7"
                },
                {
                    "portString": "input7",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "mix7",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "enable8",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "name8",
                    "datatypeString": "string",
                    "valueString": "layer8"
                },
                {
                    "portString": "input8",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "mix8",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "length": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "euclidian"
                }
            ]
        },
        "log": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "base",
                    "datatypeString": "color3",
                    "valueString": "2.71828, 2.71828, 2.71828"
                }
            ]
        },
        "matrix_interpolate": {
            "datatypeString": "matrix44",
            "port": [
                {
                    "portString": "type",
                    "datatypeString": "string",
                    "valueString": "time"
                },
                {
                    "portString": "value",
                    "datatypeString": "float",
                    "valueString": "0.5"
                }
            ]
        },
        "matrix_multiply_vector": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "type",
                    "datatypeString": "string",
                    "valueString": "point"
                },
                {
                    "portString": "matrix",
                    "datatypeString": "matrix44",
                    "valueString": ""
                }
            ]
        },
        "matrix_transform": {
            "datatypeString": "matrix44",
            "port": [
                {
                    "portString": "transform_order",
                    "datatypeString": "string",
                    "valueString": "srt"
                },
                {
                    "portString": "rotation_type",
                    "datatypeString": "string",
                    "valueString": "euler"
                },
                {
                    "portString": "units",
                    "datatypeString": "string",
                    "valueString": "degrees"
                },
                {
                    "portString": "rotation_order",
                    "datatypeString": "string",
                    "valueString": "xyz"
                },
                {
                    "portString": "rotation",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "axis",
                    "datatypeString": "vector3",
                    "valueString": "1, 0, 0"
                },
                {
                    "portString": "angle",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "translate",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "scale",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "pivot",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "matte": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "max": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "min": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "mix_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "mix",
                    "datatypeString": "float",
                    "valueString": "0.5"
                }
            ]
        },
        "modulo": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "divisor",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "multiply": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "negate": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "normalize": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "normal_map": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "order",
                    "datatypeString": "string",
                    "valueString": "XYZ"
                },
                {
                    "portString": "invert_x",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "invert_y",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "invert_z",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "color_to_signed",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "tangent_space",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "strength",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "passthrough": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval2",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval3",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval4",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval5",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval6",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval7",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval8",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval9",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval10",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval11",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval12",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval13",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval14",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval15",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval16",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval17",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval18",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval19",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "eval20",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "pow": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "base",
                    "datatypeString": "color3",
                    "valueString": "2.71828, 2.71828, 2.71828"
                },
                {
                    "portString": "exponent",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "query_shape": {
            "datatypeString": "boolean",
            "port": []
        },
        "ramp_float": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "type",
                    "datatypeString": "string",
                    "valueString": "custom"
                },
                {
                    "portString": "input",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "position",
                    "datatypeString": "floatarray",
                    "valueString": "0.0, 1.0"
                },
                {
                    "portString": "value",
                    "datatypeString": "floatarray",
                    "valueString": "0.0, 1.0"
                },
                {
                    "portString": "interpolation",
                    "datatypeString": "integerarray",
                    "valueString": "2, 2"
                },
                {
                    "portString": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "use_implicit_uvs",
                    "datatypeString": "string",
                    "valueString": "off"
                },
                {
                    "portString": "wrap_uvs",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "ramp_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "type",
                    "datatypeString": "string",
                    "valueString": "custom"
                },
                {
                    "portString": "input",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "position",
                    "datatypeString": "floatarray",
                    "valueString": "0.0, 1.0"
                },
                {
                    "portString": "color",
                    "datatypeString": "floatarray",
                    "valueString": "0.0, 0.0, 0.0, 1.0, 1.0, 1.0"
                },
                {
                    "portString": "interpolation",
                    "datatypeString": "integerarray",
                    "valueString": "2, 2"
                },
                {
                    "portString": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "use_implicit_uvs",
                    "datatypeString": "string",
                    "valueString": "off"
                },
                {
                    "portString": "wrap_uvs",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "random": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input_type",
                    "datatypeString": "string",
                    "valueString": "int"
                },
                {
                    "portString": "input_int",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "input_float",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "grayscale",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "range": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "input_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "output_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "output_max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "smoothstep",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "contrast_pivot",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "bias",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "gain",
                    "datatypeString": "float",
                    "valueString": "0.5"
                }
            ]
        },
        "reciprocal": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "rgba_to_float": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "average"
                }
            ]
        },
        "rgb_to_float": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "average"
                }
            ]
        },
        "rgb_to_vector": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "raw"
                }
            ]
        },
        "shadow_matte": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "background",
                    "datatypeString": "string",
                    "valueString": "scene_background"
                },
                {
                    "portString": "shadow_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "shadow_opacity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "background_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "diffuse_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "diffuse_use_background",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "diffuse_intensity",
                    "datatypeString": "float",
                    "valueString": "0.7"
                },
                {
                    "portString": "backlighting",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "indirect_diffuse_enable",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "indirect_specular_enable",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "portString": "specular_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "portString": "alpha_mask",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "aov_group",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "aov_shadow",
                    "datatypeString": "string",
                    "valueString": "shadow"
                },
                {
                    "portString": "aov_shadow_diff",
                    "datatypeString": "string",
                    "valueString": "shadow_diff"
                },
                {
                    "portString": "aov_shadow_mask",
                    "datatypeString": "string",
                    "valueString": "shadow_mask"
                }
            ]
        },
        "shuffle": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "alpha",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "channel_r",
                    "datatypeString": "string",
                    "valueString": "R"
                },
                {
                    "portString": "channel_g",
                    "datatypeString": "string",
                    "valueString": "G"
                },
                {
                    "portString": "channel_b",
                    "datatypeString": "string",
                    "valueString": "B"
                },
                {
                    "portString": "channel_a",
                    "datatypeString": "string",
                    "valueString": "A"
                },
                {
                    "portString": "negate_r",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "negate_g",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "negate_b",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "negate_a",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "sign": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "skin": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "sss_weight",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "shallow_scatter_color",
                    "datatypeString": "color3",
                    "valueString": "1, 0.909, 0.769"
                },
                {
                    "portString": "shallow_scatter_weight",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "shallow_scatter_radius",
                    "datatypeString": "float",
                    "valueString": "0.15"
                },
                {
                    "portString": "mid_scatter_color",
                    "datatypeString": "color3",
                    "valueString": "0.949, 0.714, 0.56"
                },
                {
                    "portString": "mid_scatter_weight",
                    "datatypeString": "float",
                    "valueString": "0.25"
                },
                {
                    "portString": "mid_scatter_radius",
                    "datatypeString": "float",
                    "valueString": "0.25"
                },
                {
                    "portString": "deep_scatter_color",
                    "datatypeString": "color3",
                    "valueString": "0.7, 0.1, 0.1"
                },
                {
                    "portString": "deep_scatter_weight",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "deep_scatter_radius",
                    "datatypeString": "float",
                    "valueString": "0.6"
                },
                {
                    "portString": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "specular_weight",
                    "datatypeString": "float",
                    "valueString": "0.8"
                },
                {
                    "portString": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "specular_ior",
                    "datatypeString": "float",
                    "valueString": "1.44"
                },
                {
                    "portString": "sheen_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "sheen_weight",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "sheen_roughness",
                    "datatypeString": "float",
                    "valueString": "0.35"
                },
                {
                    "portString": "sheen_ior",
                    "datatypeString": "float",
                    "valueString": "1.44"
                },
                {
                    "portString": "global_sss_radius_multiplier",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "specular_in_secondary_rays",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "fresnel_affect_sss",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "opacity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "opacity_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 1, 0"
                }
            ]
        },
        "space_transform": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "type",
                    "datatypeString": "string",
                    "valueString": "point"
                },
                {
                    "portString": "from",
                    "datatypeString": "string",
                    "valueString": "world"
                },
                {
                    "portString": "to",
                    "datatypeString": "string",
                    "valueString": "world"
                },
                {
                    "portString": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "normalize",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "scale",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "sqrt": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "state_float": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "variable",
                    "datatypeString": "string",
                    "valueString": "sx"
                }
            ]
        },
        "state_int": {
            "datatypeString": "integer",
            "port": [
                {
                    "portString": "variable",
                    "datatypeString": "string",
                    "valueString": "x"
                }
            ]
        },
        "state_vector": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "variable",
                    "datatypeString": "string",
                    "valueString": "Ro"
                }
            ]
        },
        "subtract": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "switch_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "index",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "input0",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input1",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input2",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input3",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input4",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input5",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input6",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input7",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input8",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input9",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input10",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input11",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input12",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input13",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input14",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input15",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input16",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input17",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input18",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "input19",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                }
            ]
        },
        "switch_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "index",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "input0",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input2",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input3",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input4",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input5",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input6",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input7",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input8",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input9",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input10",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input11",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input12",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input13",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input14",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input15",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input16",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input17",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input18",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "input19",
                    "datatypeString": "closure",
                    "valueString": ""
                }
            ]
        },
        "thin_film": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "thickness_min",
                    "datatypeString": "float",
                    "valueString": "250"
                },
                {
                    "portString": "thickness_max",
                    "datatypeString": "float",
                    "valueString": "400"
                },
                {
                    "portString": "thickness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "ior_medium",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "ior_film",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "portString": "ior_internal",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "trace_set": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "trigo": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "function",
                    "datatypeString": "string",
                    "valueString": "cos"
                },
                {
                    "portString": "units",
                    "datatypeString": "string",
                    "valueString": "radians"
                },
                {
                    "portString": "frequency",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "phase",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "triplanar": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "scale",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "rotate",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "coord_space",
                    "datatypeString": "string",
                    "valueString": "object"
                },
                {
                    "portString": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "blend",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "cell",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "cell_rotate",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "cell_blend",
                    "datatypeString": "float",
                    "valueString": "0.1"
                }
            ]
        },
        "two_sided": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "front",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "back",
                    "datatypeString": "closure",
                    "valueString": ""
                }
            ]
        },
        "user_data_float": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "attribute",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "default",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "user_data_int": {
            "datatypeString": "integer",
            "port": [
                {
                    "portString": "attribute",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "default",
                    "datatypeString": "integer",
                    "valueString": "0"
                }
            ]
        },
        "user_data_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "attribute",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "default",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                }
            ]
        },
        "user_data_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "attribute",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "default",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "user_data_string": {
            "datatypeString": "string",
            "port": [
                {
                    "portString": "attribute",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "default",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "uv_transform": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "passthrough",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "unit",
                    "datatypeString": "string",
                    "valueString": "degrees"
                },
                {
                    "portString": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "coverage",
                    "datatypeString": "vector2",
                    "valueString": "1, 1"
                },
                {
                    "portString": "scale_frame",
                    "datatypeString": "vector2",
                    "valueString": "1, 1"
                },
                {
                    "portString": "translate_frame",
                    "datatypeString": "vector2",
                    "valueString": "0, 0"
                },
                {
                    "portString": "rotate_frame",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "pivot_frame",
                    "datatypeString": "vector2",
                    "valueString": "0.5, 0.5"
                },
                {
                    "portString": "wrap_frame_u",
                    "datatypeString": "string",
                    "valueString": "periodic"
                },
                {
                    "portString": "wrap_frame_v",
                    "datatypeString": "string",
                    "valueString": "periodic"
                },
                {
                    "portString": "wrap_frame_color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "repeat",
                    "datatypeString": "vector2",
                    "valueString": "1, 1"
                },
                {
                    "portString": "offset",
                    "datatypeString": "vector2",
                    "valueString": "0, 0"
                },
                {
                    "portString": "rotate",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "pivot",
                    "datatypeString": "vector2",
                    "valueString": "0.5, 0.5"
                },
                {
                    "portString": "noise",
                    "datatypeString": "vector2",
                    "valueString": "0, 0"
                },
                {
                    "portString": "mirror_u",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "mirror_v",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "flip_u",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "flip_v",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "swap_uv",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "stagger",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "uv_projection": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "projection_color",
                    "datatypeString": "color4",
                    "valueString": "1, 1, 1, 1"
                },
                {
                    "portString": "projection_type",
                    "datatypeString": "string",
                    "valueString": "planar"
                },
                {
                    "portString": "coord_space",
                    "datatypeString": "string",
                    "valueString": "world"
                },
                {
                    "portString": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "portString": "P",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "u_angle",
                    "datatypeString": "float",
                    "valueString": "180"
                },
                {
                    "portString": "v_angle",
                    "datatypeString": "float",
                    "valueString": "90"
                },
                {
                    "portString": "clamp",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "default_color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "portString": "matrix",
                    "datatypeString": "matrix44",
                    "valueString": ""
                }
            ]
        },
        "vector_map": {
            "datatypeString": "vector3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "order",
                    "datatypeString": "string",
                    "valueString": "XYZ"
                },
                {
                    "portString": "invert_x",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "invert_y",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "invert_z",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "color_to_signed",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "tangent_space",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "portString": "scale",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "vector_to_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "mode",
                    "datatypeString": "string",
                    "valueString": "raw"
                }
            ]
        },
        "volume_collector": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "scattering_source",
                    "datatypeString": "string",
                    "valueString": "parameter"
                },
                {
                    "portString": "scattering",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "scattering_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "scattering_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "scattering_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "attenuation_source",
                    "datatypeString": "string",
                    "valueString": "parameter"
                },
                {
                    "portString": "attenuation",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "attenuation_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "attenuation_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "attenuation_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "attenuation_mode",
                    "datatypeString": "string",
                    "valueString": "absorption"
                },
                {
                    "portString": "emission_source",
                    "datatypeString": "string",
                    "valueString": "parameter"
                },
                {
                    "portString": "emission",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "emission_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "emission_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "position_offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "interpolation",
                    "datatypeString": "string",
                    "valueString": "trilinear"
                }
            ]
        },
        "volume_sample_float": {
            "datatypeString": "float",
            "port": [
                {
                    "portString": "channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "position_offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "interpolation",
                    "datatypeString": "string",
                    "valueString": "trilinear"
                },
                {
                    "portString": "volume_type",
                    "datatypeString": "string",
                    "valueString": "fog"
                },
                {
                    "portString": "sdf_offset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "sdf_blend",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "sdf_invert",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "input_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "input_max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "contrast_pivot",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "bias",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "gain",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "portString": "output_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "output_max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "clamp_min",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "clamp_max",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "volume_sample_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "portString": "channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "position_offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "portString": "interpolation",
                    "datatypeString": "string",
                    "valueString": "trilinear"
                },
                {
                    "portString": "gamma",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "hue_shift",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "saturation",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "contrast_pivot",
                    "datatypeString": "float",
                    "valueString": "0.18"
                },
                {
                    "portString": "exposure",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "multiply",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "add",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "c4d_texture_tag": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "color",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "proj",
                    "datatypeString": "string",
                    "valueString": "spherical"
                },
                {
                    "portString": "lenx",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "leny",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "ox",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "oy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "tilex",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "tiley",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "m",
                    "datatypeString": "matrix44",
                    "valueString": ""
                },
                {
                    "portString": "camera",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "aspect_ratio",
                    "datatypeString": "float",
                    "valueString": "1.33333"
                },
                {
                    "portString": "use_pref",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "side",
                    "datatypeString": "integer",
                    "valueString": "0"
                }
            ]
        },
        "c4d_texture_tag_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "portString": "color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "portString": "proj",
                    "datatypeString": "string",
                    "valueString": "spherical"
                },
                {
                    "portString": "lenx",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "leny",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "portString": "ox",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "oy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "tilex",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "tiley",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "portString": "m",
                    "datatypeString": "matrix44",
                    "valueString": ""
                },
                {
                    "portString": "camera",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "portString": "aspect_ratio",
                    "datatypeString": "float",
                    "valueString": "1.33333"
                },
                {
                    "portString": "use_pref",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "side",
                    "datatypeString": "integer",
                    "valueString": "0"
                }
            ]
        },
        "maya_layered_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "portString": "compositingFlag",
                    "datatypeString": "string",
                    "valueString": "shader"
                },
                {
                    "portString": "numInputs",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "portString": "color0",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color2",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color3",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color4",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color5",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color6",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color7",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color8",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color9",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color10",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color11",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color12",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color13",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color14",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "color15",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "portString": "transparency0",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency1",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency2",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency3",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency4",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency5",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency6",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency7",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency8",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency9",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency10",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency11",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency12",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency13",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency14",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "transparency15",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "portString": "useTransparency0",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency1",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency2",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency3",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency4",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency5",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency6",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency7",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency8",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency9",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency10",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency11",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency12",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency13",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency14",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "portString": "useTransparency15",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        }
    }

    DEF_mtl_material_def_list = [
            {
                u'name': u'surface_shader',
                u'datatypeString': u'closure',
                u'valueString': u''
            },
            {
                u'name': u'displacement_shader',
                u'datatypeString': u'closure',
                u'valueString': u''
            },
            {
                u'name': u'volume_shader',
                u'datatypeString': u'closure',
                u'valueString': u''
            }
        ]

    DEF_mtl_output_def_dict = {
        u'geometry': [],
        u'closure': [
            {
                u'name': u'out_color',
                u'datatypeString': u'color3',
                u'valueString': u'0, 0, 0'
            },
            {
                u'name': u'out_transparency',
                u'datatypeString': u'color3',
                u'valueString': u'0, 0, 0'
            }
        ],
        u'color3': [
            {
                u'name': u'out_color',
                u'datatypeString': u'color3',
                u'valueString': u'0, 0, 0'
            },
            {
                u'name': u'out_transparency',
                u'datatypeString': u'color3',
                u'valueString': u'0, 0, 0'
            }
        ],
        u'color4': [
            {
                u'name': u'out_color',
                u'datatypeString': u'color3',
                u'valueString': u'0, 0, 0'
            },
            {
                u'name': u'out_transparency',
                u'datatypeString': u'color3',
                u'valueString': u'0, 0, 0'
            },
            {
                u'name': u'out_alpha',
                u'datatypeString': u'float',
                u'valueString': u'0'
            }
        ]
    }

    DEF_mtl_maya_node_transfer_dict = {
        'sky': {
            'opaque_alpha': None,
            'Y_angle': None,
            'Z_angle': None,
            'X_angle': None,
            'Y': None,
            'X': None,
            'Z': None
        },
        'standard': {
            'Kd_color': 'color'
        },
        'standard_surface': {
            'coat_affect_roughness': None,
            'coat_affect_color': None,
            'normal': 'coatNormal'
        },
        'uv_projection': {
            'matrix': 'placementMatrix'
        },
        'ramp_float': {
            'position': 'ramp.ramp_Position',
            'value': 'ramp.ramp_FloatValue',
            'interpolation': 'ramp.ramp_Interp'
        },
        'ramp_rgb': {
            'position': 'ramp.ramp_Position',
            'color': 'ramp.ramp_Color',
            'interpolation': 'ramp.ramp_Interp'
        },
    }

    DEF_mtl_maya_porttype_transfer_dict = {
        u'enum': 'string',
        u'typed': 'string',
        u'float': 'float',
        u'long': 'integer',
        u'bool': 'boolean',
        u'fltMatrix': 'matrix44',
        u'byte': 'integer',
        u'message': 'string',
        u'float2': 'vector2',
        u'float3': 'vector3'
    }

