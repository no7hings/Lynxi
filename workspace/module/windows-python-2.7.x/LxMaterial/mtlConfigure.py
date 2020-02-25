# coding:utf-8


class Utility(object):
    DEF_mtl_data_separator = u','
    DEF_mtl_data_array_separator = u', '

    DEF_mya_separator_node = u'|'
    DEF_mtl_namespace_separator = u':'
    DEF_mtl_node_separator = u'/'
    DEF_mtl_file_separator = u'/'
    DEF_mtl_attribute_separator = u'.'

    DEF_mtl_key_type = u'datatypeString'
    DEF_mtl_key_value = u'valueString'
    DEF_mtl_key_port = u'port'

    DEF_mtl_key_name = u'name'

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
                    "name": "camera",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "shadow",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "diffuse_reflection",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "diffuse_transmission",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "specular_reflection",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "specular_transmission",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "volume",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                }
            ]
        },
        "ray_switch_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "camera",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "shadow",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "diffuse_reflection",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "diffuse_transmission",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "specular_reflection",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "specular_transmission",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "volume",
                    "datatypeString": "closure",
                    "valueString": ""
                }
            ]
        },
        "image": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "filename",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "color_space",
                    "datatypeString": "string",
                    "valueString": "auto"
                },
                {
                    "name": "filter",
                    "datatypeString": "string",
                    "valueString": "smart_bicubic"
                },
                {
                    "name": "mipmap_bias",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "single_channel",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "start_channel",
                    "datatypeString": "integer",
                    "valueString": "-401153280"
                },
                {
                    "name": "swrap",
                    "datatypeString": "string",
                    "valueString": "periodic"
                },
                {
                    "name": "twrap",
                    "datatypeString": "string",
                    "valueString": "periodic"
                },
                {
                    "name": "sscale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "tscale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "sflip",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "tflip",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "soffset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "toffset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "swap_st",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "uvcoords",
                    "datatypeString": "vector2",
                    "valueString": "0, 0"
                },
                {
                    "name": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "multiply",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "offset",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "ignore_missing_textures",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "missing_texture_color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                }
            ]
        },
        "noise": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "octaves",
                    "datatypeString": "integer",
                    "valueString": "1"
                },
                {
                    "name": "distortion",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "lacunarity",
                    "datatypeString": "float",
                    "valueString": "1.92"
                },
                {
                    "name": "amplitude",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "scale",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "coord_space",
                    "datatypeString": "string",
                    "valueString": "object"
                },
                {
                    "name": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "P",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "time",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "color1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "color2",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "scalar"
                }
            ]
        },
        "cell_noise": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "pattern",
                    "datatypeString": "string",
                    "valueString": "noise1"
                },
                {
                    "name": "additive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "octaves",
                    "datatypeString": "integer",
                    "valueString": "1"
                },
                {
                    "name": "randomness",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "lacunarity",
                    "datatypeString": "float",
                    "valueString": "1.92"
                },
                {
                    "name": "amplitude",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "scale",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "coord_space",
                    "datatypeString": "string",
                    "valueString": "object"
                },
                {
                    "name": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "P",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "time",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "palette",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "density",
                    "datatypeString": "float",
                    "valueString": "0.5"
                }
            ]
        },
        "utility": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "color_mode",
                    "datatypeString": "string",
                    "valueString": "color"
                },
                {
                    "name": "shade_mode",
                    "datatypeString": "string",
                    "valueString": "ndoteye"
                },
                {
                    "name": "overlay_mode",
                    "datatypeString": "string",
                    "valueString": "none"
                },
                {
                    "name": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "ao_distance",
                    "datatypeString": "float",
                    "valueString": "100"
                },
                {
                    "name": "roughness",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "wireframe": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "line_width",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "fill_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "line_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "raster_space",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "edge_type",
                    "datatypeString": "string",
                    "valueString": "triangles"
                }
            ]
        },
        "motion_vector": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "raw",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "time0",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "time1",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "max_displace",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "ambient_occlusion": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "samples",
                    "datatypeString": "integer",
                    "valueString": "3"
                },
                {
                    "name": "spread",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "near_clip",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "far_clip",
                    "datatypeString": "float",
                    "valueString": "100"
                },
                {
                    "name": "falloff",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "black",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "white",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "invert_normals",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "self_only",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "round_corners": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "samples",
                    "datatypeString": "integer",
                    "valueString": "6"
                },
                {
                    "name": "radius",
                    "datatypeString": "float",
                    "valueString": "0.01"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "self_only",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "object_space",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "flat": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "toon": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "mask_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "edge_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "edge_tonemap",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "edge_opacity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "edge_width_scale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "silhouette_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "silhouette_tonemap",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "silhouette_opacity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "silhouette_width_scale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "priority",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "enable_silhouette",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "ignore_throughput",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "enable",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "id_difference",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "shader_difference",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "uv_threshold",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "angle_threshold",
                    "datatypeString": "float",
                    "valueString": "180"
                },
                {
                    "name": "normal_type",
                    "datatypeString": "string",
                    "valueString": "shading normal"
                },
                {
                    "name": "base",
                    "datatypeString": "float",
                    "valueString": "0.8"
                },
                {
                    "name": "base_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "base_tonemap",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "specular_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "specular_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "specular_tonemap",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "lights",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "highlight_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "highlight_size",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "aov_highlight",
                    "datatypeString": "string",
                    "valueString": "highlight"
                },
                {
                    "name": "rim_light",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "rim_light_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "rim_light_width",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "aov_rim_light",
                    "datatypeString": "string",
                    "valueString": "rim_light"
                },
                {
                    "name": "transmission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transmission_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "sheen",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "sheen_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "sheen_roughness",
                    "datatypeString": "float",
                    "valueString": "0.3"
                },
                {
                    "name": "emission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "IOR",
                    "datatypeString": "float",
                    "valueString": "1.52"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "indirect_diffuse",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "indirect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "bump_mode",
                    "datatypeString": "string",
                    "valueString": "both"
                },
                {
                    "name": "energy_conserving",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "user_id",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "lambert": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "Kd",
                    "datatypeString": "float",
                    "valueString": "0.7"
                },
                {
                    "name": "Kd_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "standard": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "Kd",
                    "datatypeString": "float",
                    "valueString": "0.7"
                },
                {
                    "name": "Kd_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "diffuse_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Ks",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Ks_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.466905"
                },
                {
                    "name": "specular_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "specular_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "specular_distribution",
                    "datatypeString": "string",
                    "valueString": "ggx"
                },
                {
                    "name": "Kr",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Kr_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "reflection_exit_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "reflection_exit_use_environment",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "Kt",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Kt_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transmittance",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "refraction_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "refraction_exit_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "refraction_exit_use_environment",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "IOR",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "dispersion_abbe",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Kb",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Fresnel",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "Krn",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "specular_Fresnel",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "Ksn",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Fresnel_use_IOR",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "Fresnel_affect_diff",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "emission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "direct_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "indirect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "direct_diffuse",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "indirect_diffuse",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable_glossy_caustics",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "enable_reflective_caustics",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "enable_refractive_caustics",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "enable_internal_reflections",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "Ksss",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Ksss_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "sss_radius",
                    "datatypeString": "color3",
                    "valueString": "0.1, 0.1, 0.1"
                },
                {
                    "name": "bounce_factor",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "standard_surface": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "base",
                    "datatypeString": "float",
                    "valueString": "0.8"
                },
                {
                    "name": "base_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "diffuse_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "name": "specular_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "name": "specular_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "specular_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "metalness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transmission_depth",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission_scatter",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "transmission_scatter_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission_dispersion",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission_extra_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmit_aovs",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "subsurface",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "subsurface_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "subsurface_radius",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "subsurface_scale",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "subsurface_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "subsurface_type",
                    "datatypeString": "string",
                    "valueString": "randomwalk"
                },
                {
                    "name": "sheen",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "sheen_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "sheen_roughness",
                    "datatypeString": "float",
                    "valueString": "0.3"
                },
                {
                    "name": "thin_walled",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "coat",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "coat_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "coat_roughness",
                    "datatypeString": "float",
                    "valueString": "0.1"
                },
                {
                    "name": "coat_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "name": "coat_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "coat_rotation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "coat_normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "coat_affect_color",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "coat_affect_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "thin_film_thickness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "thin_film_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "name": "emission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "caustics",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "internal_reflections",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "exit_to_background",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "indirect_diffuse",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "indirect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "aov_id1",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id2",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id3",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id3",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id4",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id4",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id5",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id5",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id6",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id6",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id7",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id7",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id8",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id8",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "hair": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "rootcolor",
                    "datatypeString": "color3",
                    "valueString": "0.1, 0.1, 0.1"
                },
                {
                    "name": "tipcolor",
                    "datatypeString": "color3",
                    "valueString": "0.5, 0.5, 0.5"
                },
                {
                    "name": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "ambdiff",
                    "datatypeString": "float",
                    "valueString": "0.6"
                },
                {
                    "name": "spec",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "spec_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "spec_shift",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "spec_gloss",
                    "datatypeString": "float",
                    "valueString": "10"
                },
                {
                    "name": "spec2",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "spec2_color",
                    "datatypeString": "color3",
                    "valueString": "1, 0.4, 0.1"
                },
                {
                    "name": "spec2_shift",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "spec2_gloss",
                    "datatypeString": "float",
                    "valueString": "7"
                },
                {
                    "name": "transmission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transmission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 0.4, 0.1"
                },
                {
                    "name": "transmission_spread",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "kd_ind",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "standard_hair": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "base",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "base_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "melanin",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "melanin_redness",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "melanin_randomize",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "roughness",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "name": "roughness_azimuthal",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "name": "roughness_anisotropic",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "ior",
                    "datatypeString": "float",
                    "valueString": "1.55"
                },
                {
                    "name": "shift",
                    "datatypeString": "float",
                    "valueString": "3"
                },
                {
                    "name": "specular_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular2_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transmission_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "diffuse",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "diffuse_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "emission",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "indirect_diffuse",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "indirect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "extra_depth",
                    "datatypeString": "integer",
                    "valueString": "16"
                },
                {
                    "name": "extra_samples",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "aov_id1",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id2",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id3",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id3",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id4",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id4",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id5",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id5",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id6",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id6",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id7",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id7",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_id8",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "id8",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "car_paint": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "base",
                    "datatypeString": "float",
                    "valueString": "0.8"
                },
                {
                    "name": "base_color",
                    "datatypeString": "color3",
                    "valueString": "1, 0, 0"
                },
                {
                    "name": "base_roughness",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular_flip_flop",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular_light_facing",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular_falloff",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.05"
                },
                {
                    "name": "specular_IOR",
                    "datatypeString": "float",
                    "valueString": "1.52"
                },
                {
                    "name": "transmission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "flake_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "flake_flip_flop",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "flake_light_facing",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "flake_falloff",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "flake_roughness",
                    "datatypeString": "float",
                    "valueString": "0.4"
                },
                {
                    "name": "flake_IOR",
                    "datatypeString": "float",
                    "valueString": "100"
                },
                {
                    "name": "flake_scale",
                    "datatypeString": "float",
                    "valueString": "0.001"
                },
                {
                    "name": "flake_density",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "flake_layers",
                    "datatypeString": "integer",
                    "valueString": "1"
                },
                {
                    "name": "flake_normal_randomize",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "flake_coord_space",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "coat",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "coat_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "coat_roughness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "coat_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "name": "coat_normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "bump2d": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "bump_map",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "bump_height",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "bump3d": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "bump_map",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "bump_height",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "epsilon",
                    "datatypeString": "float",
                    "valueString": "1e-05"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "mix_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "blend"
                },
                {
                    "name": "mix",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "shader1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "shader2",
                    "datatypeString": "closure",
                    "valueString": ""
                }
            ]
        },
        "sky": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "visibility",
                    "datatypeString": "integer",
                    "valueString": "-940211969"
                },
                {
                    "name": "opaque_alpha",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "format",
                    "datatypeString": "string",
                    "valueString": "angular"
                },
                {
                    "name": "X_angle",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Y_angle",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "Z_angle",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "X",
                    "datatypeString": "vector3",
                    "valueString": "1, 0, 0"
                },
                {
                    "name": "Y",
                    "datatypeString": "vector3",
                    "valueString": "0, 1, 0"
                },
                {
                    "name": "Z",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 1"
                }
            ]
        },
        "physical_sky": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "turbidity",
                    "datatypeString": "float",
                    "valueString": "3"
                },
                {
                    "name": "ground_albedo",
                    "datatypeString": "color3",
                    "valueString": "0.1, 0.1, 0.1"
                },
                {
                    "name": "use_degrees",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "elevation",
                    "datatypeString": "float",
                    "valueString": "45"
                },
                {
                    "name": "azimuth",
                    "datatypeString": "float",
                    "valueString": "90"
                },
                {
                    "name": "sun_direction",
                    "datatypeString": "vector3",
                    "valueString": "0, 1, 0"
                },
                {
                    "name": "enable_sun",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "sun_size",
                    "datatypeString": "float",
                    "valueString": "0.51"
                },
                {
                    "name": "sun_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "sky_tint",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "X",
                    "datatypeString": "vector3",
                    "valueString": "1, 0, 0"
                },
                {
                    "name": "Y",
                    "datatypeString": "vector3",
                    "valueString": "0, 1, 0"
                },
                {
                    "name": "Z",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 1"
                }
            ]
        },
        "atmosphere_volume": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "density",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "samples",
                    "datatypeString": "integer",
                    "valueString": "5"
                },
                {
                    "name": "eccentricity",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "attenuation",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "affect_camera",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "affect_diffuse",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "affect_specular",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "rgb_density",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "rgb_attenuation",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "fog": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "distance",
                    "datatypeString": "float",
                    "valueString": "0.02"
                },
                {
                    "name": "height",
                    "datatypeString": "float",
                    "valueString": "5"
                },
                {
                    "name": "color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "ground_point",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "ground_normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 1"
                }
            ]
        },
        "standard_volume": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "density",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "density_channel",
                    "datatypeString": "string",
                    "valueString": "density"
                },
                {
                    "name": "scatter",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "scatter_color",
                    "datatypeString": "color3",
                    "valueString": "0.5, 0.5, 0.5"
                },
                {
                    "name": "scatter_color_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "scatter_anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "transparent",
                    "datatypeString": "color3",
                    "valueString": "0.367879, 0.367879, 0.367879"
                },
                {
                    "name": "transparent_depth",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "transparent_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "emission_mode",
                    "datatypeString": "string",
                    "valueString": "blackbody"
                },
                {
                    "name": "emission",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "emission_channel",
                    "datatypeString": "string",
                    "valueString": "heat"
                },
                {
                    "name": "temperature",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "temperature_channel",
                    "datatypeString": "string",
                    "valueString": "temperature"
                },
                {
                    "name": "blackbody_kelvin",
                    "datatypeString": "float",
                    "valueString": "5000"
                },
                {
                    "name": "blackbody_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "displacement",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "interpolation",
                    "datatypeString": "string",
                    "valueString": "trilinear"
                }
            ]
        },
        "abs": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "add": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "input2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "aov_read_float": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_read_int": {
            "datatypeString": "integer",
            "port": [
                {
                    "name": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_read_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_read_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_write_float": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "aov_input",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "blend_opacity",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "aov_write_int": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "aov_input",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "aov_write_rgb": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "aov_input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "blend_opacity",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "aov_write_rgba": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "aov_input",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "aov_name",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "blend_opacity",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "atan": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "y",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "x",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "units",
                    "datatypeString": "string",
                    "valueString": "radians"
                }
            ]
        },
        "blackbody": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "temperature",
                    "datatypeString": "float",
                    "valueString": "6500"
                },
                {
                    "name": "normalize",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "cache": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "camera_projection": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "projection_color",
                    "datatypeString": "color4",
                    "valueString": "1, 1, 1, 1"
                },
                {
                    "name": "offscreen_color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mask",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "camera",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "aspect_ratio",
                    "datatypeString": "float",
                    "valueString": "1.333"
                },
                {
                    "name": "front_facing",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "back_facing",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "use_shading_normal",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "coord_space",
                    "datatypeString": "string",
                    "valueString": "world"
                },
                {
                    "name": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "P",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "checkerboard": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "color1",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "color2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "u_frequency",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "v_frequency",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "u_offset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "v_offset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "filter_strength",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "filter_offset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "clamp": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "scalar"
                },
                {
                    "name": "min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "min_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "max_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "clip_geo": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "intersection",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "color_convert": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "from",
                    "datatypeString": "string",
                    "valueString": "RGB"
                },
                {
                    "name": "to",
                    "datatypeString": "string",
                    "valueString": "HSV"
                }
            ]
        },
        "color_correct": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "alpha_is_luminance",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "alpha_multiply",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "alpha_add",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "invert",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "invert_alpha",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "gamma",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "hue_shift",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "saturation",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "contrast_pivot",
                    "datatypeString": "float",
                    "valueString": "0.18"
                },
                {
                    "name": "exposure",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "multiply",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "add",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "mask",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "color_jitter": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "data_input",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "data_gain_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "data_gain_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "data_hue_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "data_hue_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "data_saturation_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "data_saturation_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "data_seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "proc_gain_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "proc_gain_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "proc_hue_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "proc_hue_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "proc_saturation_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "proc_saturation_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "proc_seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "obj_gain_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "obj_gain_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "obj_hue_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "obj_hue_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "obj_saturation_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "obj_saturation_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "obj_seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "face_gain_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "face_gain_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "face_hue_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "face_hue_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "face_saturation_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "face_saturation_max",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "face_seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "face_mode",
                    "datatypeString": "string",
                    "valueString": "face id"
                }
            ]
        },
        "compare": {
            "datatypeString": "boolean",
            "port": [
                {
                    "name": "test",
                    "datatypeString": "string",
                    "valueString": "=="
                },
                {
                    "name": "input1",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input2",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "complement": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "complex_ior": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "material",
                    "datatypeString": "string",
                    "valueString": "custom"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "artistic"
                },
                {
                    "name": "reflectivity",
                    "datatypeString": "color3",
                    "valueString": "0.925952, 0.720887, 0.504154"
                },
                {
                    "name": "edgetint",
                    "datatypeString": "color3",
                    "valueString": "0.995524, 0.957415, 0.822776"
                },
                {
                    "name": "n",
                    "datatypeString": "vector3",
                    "valueString": "0.27105, 0.67693, 1.3164"
                },
                {
                    "name": "k",
                    "datatypeString": "vector3",
                    "valueString": "3.6092, 2.6247, 2.2921"
                }
            ]
        },
        "composite": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "A",
                    "datatypeString": "color4",
                    "valueString": "1, 0, 0, 1"
                },
                {
                    "name": "B",
                    "datatypeString": "color4",
                    "valueString": "0, 1, 0, 1"
                },
                {
                    "name": "operation",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation",
                    "datatypeString": "string",
                    "valueString": "same"
                }
            ]
        },
        "cross": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "input2",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "curvature": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "output",
                    "datatypeString": "string",
                    "valueString": "convex"
                },
                {
                    "name": "samples",
                    "datatypeString": "integer",
                    "valueString": "3"
                },
                {
                    "name": "radius",
                    "datatypeString": "float",
                    "valueString": "0.1"
                },
                {
                    "name": "spread",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "threshold",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "bias",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "multiply",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "self_only",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "divide": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "input2",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "dot": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "input2",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "exp": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "facing_ratio": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "bias",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "gain",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "linear",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "invert",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "flakes": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "scale",
                    "datatypeString": "float",
                    "valueString": "0.1"
                },
                {
                    "name": "density",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "step",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "depth",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "IOR",
                    "datatypeString": "float",
                    "valueString": "1.52"
                },
                {
                    "name": "normal_randomize",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "coord_space",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "output_space",
                    "datatypeString": "string",
                    "valueString": "world"
                }
            ]
        },
        "float_to_int": {
            "datatypeString": "integer",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "round"
                }
            ]
        },
        "float_to_matrix": {
            "datatypeString": "matrix44",
            "port": [
                {
                    "name": "input_00",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "input_01",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_02",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_03",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_10",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_11",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "input_12",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_13",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_20",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_21",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_22",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "input_23",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_30",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_31",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_32",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_33",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "float_to_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "r",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "g",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "b",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "a",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "float_to_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "r",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "g",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "b",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "fraction": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "is_finite": {
            "datatypeString": "boolean",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "layer_float": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "enable1",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name1",
                    "datatypeString": "string",
                    "valueString": "layer1"
                },
                {
                    "name": "input1",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mix1",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable2",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name2",
                    "datatypeString": "string",
                    "valueString": "layer2"
                },
                {
                    "name": "input2",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mix2",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "enable3",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name3",
                    "datatypeString": "string",
                    "valueString": "layer3"
                },
                {
                    "name": "input3",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mix3",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "enable4",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name4",
                    "datatypeString": "string",
                    "valueString": "layer4"
                },
                {
                    "name": "input4",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mix4",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "enable5",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name5",
                    "datatypeString": "string",
                    "valueString": "layer5"
                },
                {
                    "name": "input5",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mix5",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "enable6",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name6",
                    "datatypeString": "string",
                    "valueString": "layer6"
                },
                {
                    "name": "input6",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mix6",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "enable7",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name7",
                    "datatypeString": "string",
                    "valueString": "layer7"
                },
                {
                    "name": "input7",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mix7",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "enable8",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name8",
                    "datatypeString": "string",
                    "valueString": "layer8"
                },
                {
                    "name": "input8",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "mix8",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "layer_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "enable1",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name1",
                    "datatypeString": "string",
                    "valueString": "layer1"
                },
                {
                    "name": "input1",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mix1",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "operation1",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation1",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "name": "enable2",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name2",
                    "datatypeString": "string",
                    "valueString": "layer2"
                },
                {
                    "name": "input2",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mix2",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "operation2",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation2",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "name": "enable3",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name3",
                    "datatypeString": "string",
                    "valueString": "layer3"
                },
                {
                    "name": "input3",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mix3",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "operation3",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation3",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "name": "enable4",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name4",
                    "datatypeString": "string",
                    "valueString": "layer4"
                },
                {
                    "name": "input4",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mix4",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "operation4",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation4",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "name": "enable5",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name5",
                    "datatypeString": "string",
                    "valueString": "layer5"
                },
                {
                    "name": "input5",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mix5",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "operation5",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation5",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "name": "enable6",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name6",
                    "datatypeString": "string",
                    "valueString": "layer6"
                },
                {
                    "name": "input6",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mix6",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "operation6",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation6",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "name": "enable7",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name7",
                    "datatypeString": "string",
                    "valueString": "layer7"
                },
                {
                    "name": "input7",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mix7",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "operation7",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation7",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "name": "enable8",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name8",
                    "datatypeString": "string",
                    "valueString": "layer8"
                },
                {
                    "name": "input8",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "mix8",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "operation8",
                    "datatypeString": "string",
                    "valueString": "over"
                },
                {
                    "name": "alpha_operation8",
                    "datatypeString": "string",
                    "valueString": "result"
                },
                {
                    "name": "clamp",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "layer_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "enable1",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name1",
                    "datatypeString": "string",
                    "valueString": "layer1"
                },
                {
                    "name": "input1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "mix1",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable2",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name2",
                    "datatypeString": "string",
                    "valueString": "layer2"
                },
                {
                    "name": "input2",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "mix2",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable3",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name3",
                    "datatypeString": "string",
                    "valueString": "layer3"
                },
                {
                    "name": "input3",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "mix3",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable4",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name4",
                    "datatypeString": "string",
                    "valueString": "layer4"
                },
                {
                    "name": "input4",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "mix4",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable5",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name5",
                    "datatypeString": "string",
                    "valueString": "layer5"
                },
                {
                    "name": "input5",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "mix5",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable6",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name6",
                    "datatypeString": "string",
                    "valueString": "layer6"
                },
                {
                    "name": "input6",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "mix6",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable7",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name7",
                    "datatypeString": "string",
                    "valueString": "layer7"
                },
                {
                    "name": "input7",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "mix7",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "enable8",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "name8",
                    "datatypeString": "string",
                    "valueString": "layer8"
                },
                {
                    "name": "input8",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "mix8",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "length": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "euclidian"
                }
            ]
        },
        "log": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "base",
                    "datatypeString": "color3",
                    "valueString": "2.71828, 2.71828, 2.71828"
                }
            ]
        },
        "matrix_interpolate": {
            "datatypeString": "matrix44",
            "port": [
                {
                    "name": "type",
                    "datatypeString": "string",
                    "valueString": "time"
                },
                {
                    "name": "value",
                    "datatypeString": "float",
                    "valueString": "0.5"
                }
            ]
        },
        "matrix_multiply_vector": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "type",
                    "datatypeString": "string",
                    "valueString": "point"
                },
                {
                    "name": "matrix",
                    "datatypeString": "matrix44",
                    "valueString": ""
                }
            ]
        },
        "matrix_transform": {
            "datatypeString": "matrix44",
            "port": [
                {
                    "name": "transform_order",
                    "datatypeString": "string",
                    "valueString": "srt"
                },
                {
                    "name": "rotation_type",
                    "datatypeString": "string",
                    "valueString": "euler"
                },
                {
                    "name": "units",
                    "datatypeString": "string",
                    "valueString": "degrees"
                },
                {
                    "name": "rotation_order",
                    "datatypeString": "string",
                    "valueString": "xyz"
                },
                {
                    "name": "rotation",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "axis",
                    "datatypeString": "vector3",
                    "valueString": "1, 0, 0"
                },
                {
                    "name": "angle",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "translate",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "scale",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "pivot",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "matte": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "opacity",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "max": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "input2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "min": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "input2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "mix_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input2",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "mix",
                    "datatypeString": "float",
                    "valueString": "0.5"
                }
            ]
        },
        "modulo": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "divisor",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "multiply": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "input2",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "negate": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "normalize": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "normal_map": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "order",
                    "datatypeString": "string",
                    "valueString": "XYZ"
                },
                {
                    "name": "invert_x",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "invert_y",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "invert_z",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "color_to_signed",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "tangent_space",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "strength",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "passthrough": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval2",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval3",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval4",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval5",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval6",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval7",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval8",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval9",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval10",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval11",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval12",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval13",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval14",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval15",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval16",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval17",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval18",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval19",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "eval20",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "pow": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "base",
                    "datatypeString": "color3",
                    "valueString": "2.71828, 2.71828, 2.71828"
                },
                {
                    "name": "exponent",
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
                    "name": "type",
                    "datatypeString": "string",
                    "valueString": "custom"
                },
                {
                    "name": "input",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "position",
                    "datatypeString": "floatarray",
                    "valueString": "0.0, 1.0"
                },
                {
                    "name": "value",
                    "datatypeString": "floatarray",
                    "valueString": "0.0, 1.0"
                },
                {
                    "name": "interpolation",
                    "datatypeString": "integerarray",
                    "valueString": "2, 2"
                },
                {
                    "name": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "use_implicit_uvs",
                    "datatypeString": "string",
                    "valueString": "off"
                },
                {
                    "name": "wrap_uvs",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "ramp_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "type",
                    "datatypeString": "string",
                    "valueString": "custom"
                },
                {
                    "name": "input",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "position",
                    "datatypeString": "floatarray",
                    "valueString": "0.0, 1.0"
                },
                {
                    "name": "color",
                    "datatypeString": "floatarray",
                    "valueString": "0.0, 0.0, 0.0, 1.0, 1.0, 1.0"
                },
                {
                    "name": "interpolation",
                    "datatypeString": "integerarray",
                    "valueString": "2, 2"
                },
                {
                    "name": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "use_implicit_uvs",
                    "datatypeString": "string",
                    "valueString": "off"
                },
                {
                    "name": "wrap_uvs",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "random": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input_type",
                    "datatypeString": "string",
                    "valueString": "int"
                },
                {
                    "name": "input_int",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "input_float",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "seed",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "grayscale",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "range": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "input_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "output_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "output_max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "smoothstep",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "contrast_pivot",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "bias",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "gain",
                    "datatypeString": "float",
                    "valueString": "0.5"
                }
            ]
        },
        "reciprocal": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                }
            ]
        },
        "rgba_to_float": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "average"
                }
            ]
        },
        "rgb_to_float": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "average"
                }
            ]
        },
        "rgb_to_vector": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "raw"
                }
            ]
        },
        "shadow_matte": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "background",
                    "datatypeString": "string",
                    "valueString": "scene_background"
                },
                {
                    "name": "shadow_color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "shadow_opacity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "background_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "diffuse_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "diffuse_use_background",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "diffuse_intensity",
                    "datatypeString": "float",
                    "valueString": "0.7"
                },
                {
                    "name": "backlighting",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "indirect_diffuse_enable",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "indirect_specular_enable",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.2"
                },
                {
                    "name": "specular_IOR",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "name": "alpha_mask",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "aov_group",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "aov_shadow",
                    "datatypeString": "string",
                    "valueString": "shadow"
                },
                {
                    "name": "aov_shadow_diff",
                    "datatypeString": "string",
                    "valueString": "shadow_diff"
                },
                {
                    "name": "aov_shadow_mask",
                    "datatypeString": "string",
                    "valueString": "shadow_mask"
                }
            ]
        },
        "shuffle": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "color",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "alpha",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "channel_r",
                    "datatypeString": "string",
                    "valueString": "R"
                },
                {
                    "name": "channel_g",
                    "datatypeString": "string",
                    "valueString": "G"
                },
                {
                    "name": "channel_b",
                    "datatypeString": "string",
                    "valueString": "B"
                },
                {
                    "name": "channel_a",
                    "datatypeString": "string",
                    "valueString": "A"
                },
                {
                    "name": "negate_r",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "negate_g",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "negate_b",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "negate_a",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "sign": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "skin": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "sss_weight",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "shallow_scatter_color",
                    "datatypeString": "color3",
                    "valueString": "1, 0.909, 0.769"
                },
                {
                    "name": "shallow_scatter_weight",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "shallow_scatter_radius",
                    "datatypeString": "float",
                    "valueString": "0.15"
                },
                {
                    "name": "mid_scatter_color",
                    "datatypeString": "color3",
                    "valueString": "0.949, 0.714, 0.56"
                },
                {
                    "name": "mid_scatter_weight",
                    "datatypeString": "float",
                    "valueString": "0.25"
                },
                {
                    "name": "mid_scatter_radius",
                    "datatypeString": "float",
                    "valueString": "0.25"
                },
                {
                    "name": "deep_scatter_color",
                    "datatypeString": "color3",
                    "valueString": "0.7, 0.1, 0.1"
                },
                {
                    "name": "deep_scatter_weight",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "deep_scatter_radius",
                    "datatypeString": "float",
                    "valueString": "0.6"
                },
                {
                    "name": "specular_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "specular_weight",
                    "datatypeString": "float",
                    "valueString": "0.8"
                },
                {
                    "name": "specular_roughness",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "specular_ior",
                    "datatypeString": "float",
                    "valueString": "1.44"
                },
                {
                    "name": "sheen_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "sheen_weight",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "sheen_roughness",
                    "datatypeString": "float",
                    "valueString": "0.35"
                },
                {
                    "name": "sheen_ior",
                    "datatypeString": "float",
                    "valueString": "1.44"
                },
                {
                    "name": "global_sss_radius_multiplier",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "specular_in_secondary_rays",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "fresnel_affect_sss",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "opacity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "opacity_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 1, 0"
                }
            ]
        },
        "space_transform": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "type",
                    "datatypeString": "string",
                    "valueString": "point"
                },
                {
                    "name": "from",
                    "datatypeString": "string",
                    "valueString": "world"
                },
                {
                    "name": "to",
                    "datatypeString": "string",
                    "valueString": "world"
                },
                {
                    "name": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "normalize",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "scale",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "sqrt": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "state_float": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "variable",
                    "datatypeString": "string",
                    "valueString": "sx"
                }
            ]
        },
        "state_int": {
            "datatypeString": "integer",
            "port": [
                {
                    "name": "variable",
                    "datatypeString": "string",
                    "valueString": "x"
                }
            ]
        },
        "state_vector": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "variable",
                    "datatypeString": "string",
                    "valueString": "Ro"
                }
            ]
        },
        "subtract": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input1",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "input2",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "switch_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "index",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "input0",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input1",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input2",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input3",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input4",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input5",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input6",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input7",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input8",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input9",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input10",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input11",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input12",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input13",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input14",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input15",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input16",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input17",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input18",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "input19",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                }
            ]
        },
        "switch_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "index",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "input0",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input2",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input3",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input4",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input5",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input6",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input7",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input8",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input9",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input10",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input11",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input12",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input13",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input14",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input15",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input16",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input17",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input18",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "input19",
                    "datatypeString": "closure",
                    "valueString": ""
                }
            ]
        },
        "thin_film": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "thickness_min",
                    "datatypeString": "float",
                    "valueString": "250"
                },
                {
                    "name": "thickness_max",
                    "datatypeString": "float",
                    "valueString": "400"
                },
                {
                    "name": "thickness",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "ior_medium",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "ior_film",
                    "datatypeString": "float",
                    "valueString": "1.5"
                },
                {
                    "name": "ior_internal",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "trace_set": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "passthrough",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "trace_set",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "inclusive",
                    "datatypeString": "boolean",
                    "valueString": "true"
                }
            ]
        },
        "trigo": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "function",
                    "datatypeString": "string",
                    "valueString": "cos"
                },
                {
                    "name": "units",
                    "datatypeString": "string",
                    "valueString": "radians"
                },
                {
                    "name": "frequency",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "phase",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "triplanar": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "scale",
                    "datatypeString": "vector3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "rotate",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "coord_space",
                    "datatypeString": "string",
                    "valueString": "object"
                },
                {
                    "name": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "blend",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "cell",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "cell_rotate",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "cell_blend",
                    "datatypeString": "float",
                    "valueString": "0.1"
                }
            ]
        },
        "two_sided": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "front",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "back",
                    "datatypeString": "closure",
                    "valueString": ""
                }
            ]
        },
        "user_data_float": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "port",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "default",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "user_data_int": {
            "datatypeString": "integer",
            "port": [
                {
                    "name": "port",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "default",
                    "datatypeString": "integer",
                    "valueString": "0"
                }
            ]
        },
        "user_data_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "port",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "default",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                }
            ]
        },
        "user_data_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "port",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "default",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                }
            ]
        },
        "user_data_string": {
            "datatypeString": "string",
            "port": [
                {
                    "name": "port",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "default",
                    "datatypeString": "string",
                    "valueString": ""
                }
            ]
        },
        "uv_transform": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "passthrough",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "unit",
                    "datatypeString": "string",
                    "valueString": "degrees"
                },
                {
                    "name": "uvset",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "coverage",
                    "datatypeString": "vector2",
                    "valueString": "1, 1"
                },
                {
                    "name": "scale_frame",
                    "datatypeString": "vector2",
                    "valueString": "1, 1"
                },
                {
                    "name": "translate_frame",
                    "datatypeString": "vector2",
                    "valueString": "0, 0"
                },
                {
                    "name": "rotate_frame",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "pivot_frame",
                    "datatypeString": "vector2",
                    "valueString": "0.5, 0.5"
                },
                {
                    "name": "wrap_frame_u",
                    "datatypeString": "string",
                    "valueString": "periodic"
                },
                {
                    "name": "wrap_frame_v",
                    "datatypeString": "string",
                    "valueString": "periodic"
                },
                {
                    "name": "wrap_frame_color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "repeat",
                    "datatypeString": "vector2",
                    "valueString": "1, 1"
                },
                {
                    "name": "offset",
                    "datatypeString": "vector2",
                    "valueString": "0, 0"
                },
                {
                    "name": "rotate",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "pivot",
                    "datatypeString": "vector2",
                    "valueString": "0.5, 0.5"
                },
                {
                    "name": "noise",
                    "datatypeString": "vector2",
                    "valueString": "0, 0"
                },
                {
                    "name": "mirror_u",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "mirror_v",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "flip_u",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "flip_v",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "swap_uv",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "stagger",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "uv_projection": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "projection_color",
                    "datatypeString": "color4",
                    "valueString": "1, 1, 1, 1"
                },
                {
                    "name": "projection_type",
                    "datatypeString": "string",
                    "valueString": "planar"
                },
                {
                    "name": "coord_space",
                    "datatypeString": "string",
                    "valueString": "world"
                },
                {
                    "name": "pref_name",
                    "datatypeString": "string",
                    "valueString": "Pref"
                },
                {
                    "name": "P",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "u_angle",
                    "datatypeString": "float",
                    "valueString": "180"
                },
                {
                    "name": "v_angle",
                    "datatypeString": "float",
                    "valueString": "90"
                },
                {
                    "name": "clamp",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "default_color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 0"
                },
                {
                    "name": "matrix",
                    "datatypeString": "matrix44",
                    "valueString": ""
                }
            ]
        },
        "vector_map": {
            "datatypeString": "vector3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "tangent",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "normal",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "order",
                    "datatypeString": "string",
                    "valueString": "XYZ"
                },
                {
                    "name": "invert_x",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "invert_y",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "invert_z",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "color_to_signed",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "tangent_space",
                    "datatypeString": "boolean",
                    "valueString": "true"
                },
                {
                    "name": "scale",
                    "datatypeString": "float",
                    "valueString": "1"
                }
            ]
        },
        "vector_to_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "input",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "mode",
                    "datatypeString": "string",
                    "valueString": "raw"
                }
            ]
        },
        "volume_collector": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "scattering_source",
                    "datatypeString": "string",
                    "valueString": "parameter"
                },
                {
                    "name": "scattering",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "scattering_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "scattering_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "scattering_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "anisotropy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "attenuation_source",
                    "datatypeString": "string",
                    "valueString": "parameter"
                },
                {
                    "name": "attenuation",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "attenuation_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "attenuation_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "attenuation_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "attenuation_mode",
                    "datatypeString": "string",
                    "valueString": "absorption"
                },
                {
                    "name": "emission_source",
                    "datatypeString": "string",
                    "valueString": "parameter"
                },
                {
                    "name": "emission",
                    "datatypeString": "color3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "emission_channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "emission_color",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "emission_intensity",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "position_offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "interpolation",
                    "datatypeString": "string",
                    "valueString": "trilinear"
                }
            ]
        },
        "volume_sample_float": {
            "datatypeString": "float",
            "port": [
                {
                    "name": "channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "position_offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "interpolation",
                    "datatypeString": "string",
                    "valueString": "trilinear"
                },
                {
                    "name": "volume_type",
                    "datatypeString": "string",
                    "valueString": "fog"
                },
                {
                    "name": "sdf_offset",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "sdf_blend",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "sdf_invert",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "input_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "input_max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "contrast_pivot",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "bias",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "gain",
                    "datatypeString": "float",
                    "valueString": "0.5"
                },
                {
                    "name": "output_min",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "output_max",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "clamp_min",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "clamp_max",
                    "datatypeString": "boolean",
                    "valueString": "false"
                }
            ]
        },
        "volume_sample_rgb": {
            "datatypeString": "color3",
            "port": [
                {
                    "name": "channel",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "position_offset",
                    "datatypeString": "vector3",
                    "valueString": "0, 0, 0"
                },
                {
                    "name": "interpolation",
                    "datatypeString": "string",
                    "valueString": "trilinear"
                },
                {
                    "name": "gamma",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "hue_shift",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "saturation",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "contrast",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "contrast_pivot",
                    "datatypeString": "float",
                    "valueString": "0.18"
                },
                {
                    "name": "exposure",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "multiply",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "add",
                    "datatypeString": "float",
                    "valueString": "0"
                }
            ]
        },
        "c4d_texture_tag": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "color",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "proj",
                    "datatypeString": "string",
                    "valueString": "spherical"
                },
                {
                    "name": "lenx",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "leny",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "ox",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "oy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "tilex",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "tiley",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "m",
                    "datatypeString": "matrix44",
                    "valueString": ""
                },
                {
                    "name": "camera",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "aspect_ratio",
                    "datatypeString": "float",
                    "valueString": "1.33333"
                },
                {
                    "name": "use_pref",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "side",
                    "datatypeString": "integer",
                    "valueString": "0"
                }
            ]
        },
        "c4d_texture_tag_rgba": {
            "datatypeString": "color4",
            "port": [
                {
                    "name": "color",
                    "datatypeString": "color4",
                    "valueString": "0, 0, 0, 1"
                },
                {
                    "name": "proj",
                    "datatypeString": "string",
                    "valueString": "spherical"
                },
                {
                    "name": "lenx",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "leny",
                    "datatypeString": "float",
                    "valueString": "1"
                },
                {
                    "name": "ox",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "oy",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "tilex",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "tiley",
                    "datatypeString": "float",
                    "valueString": "0"
                },
                {
                    "name": "m",
                    "datatypeString": "matrix44",
                    "valueString": ""
                },
                {
                    "name": "camera",
                    "datatypeString": "string",
                    "valueString": ""
                },
                {
                    "name": "aspect_ratio",
                    "datatypeString": "float",
                    "valueString": "1.33333"
                },
                {
                    "name": "use_pref",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "side",
                    "datatypeString": "integer",
                    "valueString": "0"
                }
            ]
        },
        "maya_layered_shader": {
            "datatypeString": "closure",
            "port": [
                {
                    "name": "compositingFlag",
                    "datatypeString": "string",
                    "valueString": "shader"
                },
                {
                    "name": "numInputs",
                    "datatypeString": "integer",
                    "valueString": "0"
                },
                {
                    "name": "color0",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color1",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color2",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color3",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color4",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color5",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color6",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color7",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color8",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color9",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color10",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color11",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color12",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color13",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color14",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "color15",
                    "datatypeString": "closure",
                    "valueString": ""
                },
                {
                    "name": "transparency0",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency1",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency2",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency3",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency4",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency5",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency6",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency7",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency8",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency9",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency10",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency11",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency12",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency13",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency14",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "transparency15",
                    "datatypeString": "color3",
                    "valueString": "1, 1, 1"
                },
                {
                    "name": "useTransparency0",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency1",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency2",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency3",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency4",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency5",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency6",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency7",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency8",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency9",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency10",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency11",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency12",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency13",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency14",
                    "datatypeString": "boolean",
                    "valueString": "false"
                },
                {
                    "name": "useTransparency15",
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
