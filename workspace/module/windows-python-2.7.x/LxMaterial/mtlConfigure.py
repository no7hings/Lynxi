# coding:utf-8
Separator_String_File = '/'
Separator_String_Node = '/'
Separator_String_Attribute = '.'
Separator_Raw_Basic = ','
Separator_Raw_String = ','
Separator_Raw_String_Array = ', '

Value_Type_Closure = 'closure'

Value_Type_Boolean = 'boolean'
Value_Type_Integer = 'integer'
Value_Type_Integer_Array = 'integerarray'
Value_Type_Float = 'float'
Value_Type_Float_Array = 'floatarray'

Value_Type_Color2 = 'color2'
Value_Type_Color2_Array = 'color2array'
Value_Type_Color3 = 'color3'
Value_Type_Color3_Array = 'color3array'
Value_Type_Color4 = 'color4'
Value_Type_Color4_Array = 'color4array'

Value_Type_Vector2 = 'vector2'
Value_Type_Vector2_Array = 'vector2array'
Value_Type_Vector3 = 'vector3'
Value_Type_Vector3_Array = 'vector3array'
Value_Type_Vector4 = 'vector4'
Value_Type_Vector4_Array = 'vector4array'

Value_Type_Matrix33 = 'matrix33'
Value_Type_Matrix44 = 'matrix44'

Value_Type_String = 'string'
Value_Type_String_Array = 'stringarray'
Value_Type_FileName = 'filename'
Value_Type_GeometryName = 'geomname'
Value_Type_GeometryName_Array = 'geomnamearray'

Def_Node_Dic = {
    "geometry": {
        "typeString": "geometry",
    },
    "ray_switch_rgba": {
        "typeString": "color4",
        "port": [
            {
                "name": "camera",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "shadow",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "diffuse_reflection",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "diffuse_transmission",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "specular_reflection",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "specular_transmission",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "volume",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            }
        ]
    },
    "ray_switch_shader": {
        "typeString": "closure",
        "port": [
            {
                "name": "camera",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "shadow",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "diffuse_reflection",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "diffuse_transmission",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "specular_reflection",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "specular_transmission",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "volume",
                "typeString": "closure",
                "valueString": ""
            }
        ]
    },
    "image": {
        "typeString": "color4",
        "port": [
            {
                "name": "filename",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "color_space",
                "typeString": "string",
                "valueString": "auto"
            },
            {
                "name": "filter",
                "typeString": "string",
                "valueString": "smart_bicubic"
            },
            {
                "name": "mipmap_bias",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "single_channel",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "start_channel",
                "typeString": "integer",
                "valueString": "-401153280"
            },
            {
                "name": "swrap",
                "typeString": "string",
                "valueString": "periodic"
            },
            {
                "name": "twrap",
                "typeString": "string",
                "valueString": "periodic"
            },
            {
                "name": "sscale",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "tscale",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "sflip",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "tflip",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "soffset",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "toffset",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "swap_st",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "uvcoords",
                "typeString": "vector2",
                "valueString": "0, 0"
            },
            {
                "name": "uvset",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "multiply",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "offset",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "ignore_missing_textures",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "missing_texture_color",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            }
        ]
    },
    "noise": {
        "typeString": "color3",
        "port": [
            {
                "name": "octaves",
                "typeString": "integer",
                "valueString": "1"
            },
            {
                "name": "distortion",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "lacunarity",
                "typeString": "float",
                "valueString": "1.92"
            },
            {
                "name": "amplitude",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "scale",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "offset",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "coord_space",
                "typeString": "string",
                "valueString": "object"
            },
            {
                "name": "pref_name",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "P",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "time",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "color1",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "color2",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "scalar"
            }
        ]
    },
    "cell_noise": {
        "typeString": "color3",
        "port": [
            {
                "name": "pattern",
                "typeString": "string",
                "valueString": "noise1"
            },
            {
                "name": "additive",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "octaves",
                "typeString": "integer",
                "valueString": "1"
            },
            {
                "name": "randomness",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "lacunarity",
                "typeString": "float",
                "valueString": "1.92"
            },
            {
                "name": "amplitude",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "scale",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "offset",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "coord_space",
                "typeString": "string",
                "valueString": "object"
            },
            {
                "name": "pref_name",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "P",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "time",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "palette",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "density",
                "typeString": "float",
                "valueString": "0.5"
            }
        ]
    },
    "utility": {
        "typeString": "color3",
        "port": [
            {
                "name": "color_mode",
                "typeString": "string",
                "valueString": "color"
            },
            {
                "name": "shade_mode",
                "typeString": "string",
                "valueString": "ndoteye"
            },
            {
                "name": "overlay_mode",
                "typeString": "string",
                "valueString": "none"
            },
            {
                "name": "color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "ao_distance",
                "typeString": "float",
                "valueString": "100"
            },
            {
                "name": "roughness",
                "typeString": "float",
                "valueString": "0.2"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "wireframe": {
        "typeString": "color3",
        "port": [
            {
                "name": "line_width",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "fill_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "line_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "raster_space",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "edge_type",
                "typeString": "string",
                "valueString": "triangles"
            }
        ]
    },
    "motion_vector": {
        "typeString": "color3",
        "port": [
            {
                "name": "raw",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "time0",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "time1",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "max_displace",
                "typeString": "float",
                "valueString": "0"
            }
        ]
    },
    "ambient_occlusion": {
        "typeString": "color3",
        "port": [
            {
                "name": "samples",
                "typeString": "integer",
                "valueString": "3"
            },
            {
                "name": "spread",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "near_clip",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "far_clip",
                "typeString": "float",
                "valueString": "100"
            },
            {
                "name": "falloff",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "black",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "white",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "invert_normals",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "trace_set",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "inclusive",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "self_only",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "round_corners": {
        "typeString": "vector3",
        "port": [
            {
                "name": "samples",
                "typeString": "integer",
                "valueString": "6"
            },
            {
                "name": "radius",
                "typeString": "float",
                "valueString": "0.01"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "trace_set",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "inclusive",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "self_only",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "object_space",
                "typeString": "boolean",
                "valueString": "true"
            }
        ]
    },
    "flat": {
        "typeString": "color3",
        "port": [
            {
                "name": "color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "toon": {
        "typeString": "color3",
        "port": [
            {
                "name": "mask_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "edge_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "edge_tonemap",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "edge_opacity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "edge_width_scale",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "silhouette_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "silhouette_tonemap",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "silhouette_opacity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "silhouette_width_scale",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "priority",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "enable_silhouette",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "ignore_throughput",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "enable",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "id_difference",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "shader_difference",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "uv_threshold",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "angle_threshold",
                "typeString": "float",
                "valueString": "180"
            },
            {
                "name": "normal_type",
                "typeString": "string",
                "valueString": "shading normal"
            },
            {
                "name": "base",
                "typeString": "float",
                "valueString": "0.8"
            },
            {
                "name": "base_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "base_tonemap",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "specular_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular_roughness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "specular_anisotropy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "specular_rotation",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "specular_tonemap",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "lights",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "highlight_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "highlight_size",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "aov_highlight",
                "typeString": "string",
                "valueString": "highlight"
            },
            {
                "name": "rim_light",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "rim_light_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "rim_light_width",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "aov_rim_light",
                "typeString": "string",
                "valueString": "rim_light"
            },
            {
                "name": "transmission",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transmission_roughness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission_anisotropy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission_rotation",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "sheen",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "sheen_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "sheen_roughness",
                "typeString": "float",
                "valueString": "0.3"
            },
            {
                "name": "emission",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "emission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "IOR",
                "typeString": "float",
                "valueString": "1.52"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "tangent",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "indirect_diffuse",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "indirect_specular",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "bump_mode",
                "typeString": "string",
                "valueString": "both"
            },
            {
                "name": "energy_conserving",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "user_id",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "lambert": {
        "typeString": "closure",
        "port": [
            {
                "name": "Kd",
                "typeString": "float",
                "valueString": "0.7"
            },
            {
                "name": "Kd_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "opacity",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "standard": {
        "typeString": "closure",
        "port": [
            {
                "name": "Kd",
                "typeString": "float",
                "valueString": "0.7"
            },
            {
                "name": "Kd_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "diffuse_roughness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Ks",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Ks_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular_roughness",
                "typeString": "float",
                "valueString": "0.466905"
            },
            {
                "name": "specular_anisotropy",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "specular_rotation",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "specular_distribution",
                "typeString": "string",
                "valueString": "ggx"
            },
            {
                "name": "Kr",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Kr_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "reflection_exit_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "reflection_exit_use_environment",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "Kt",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Kt_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transmittance",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "refraction_roughness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "refraction_exit_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "refraction_exit_use_environment",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "IOR",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "dispersion_abbe",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Kb",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Fresnel",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "Krn",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "specular_Fresnel",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "Ksn",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Fresnel_use_IOR",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "Fresnel_affect_diff",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "emission",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "emission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "direct_specular",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "indirect_specular",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "direct_diffuse",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "indirect_diffuse",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable_glossy_caustics",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "enable_reflective_caustics",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "enable_refractive_caustics",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "enable_internal_reflections",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "Ksss",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Ksss_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "sss_radius",
                "typeString": "color3",
                "valueString": "0.1, 0.1, 0.1"
            },
            {
                "name": "bounce_factor",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "opacity",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "standard_surface": {
        "typeString": "closure",
        "port": [
            {
                "name": "base",
                "typeString": "float",
                "valueString": "0.8"
            },
            {
                "name": "base_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "diffuse_roughness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "specular",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "specular_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular_roughness",
                "typeString": "float",
                "valueString": "0.2"
            },
            {
                "name": "specular_IOR",
                "typeString": "float",
                "valueString": "1.5"
            },
            {
                "name": "specular_anisotropy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "specular_rotation",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "metalness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transmission_depth",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission_scatter",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "transmission_scatter_anisotropy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission_dispersion",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission_extra_roughness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmit_aovs",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "subsurface",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "subsurface_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "subsurface_radius",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "subsurface_scale",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "subsurface_anisotropy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "subsurface_type",
                "typeString": "string",
                "valueString": "randomwalk"
            },
            {
                "name": "sheen",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "sheen_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "sheen_roughness",
                "typeString": "float",
                "valueString": "0.3"
            },
            {
                "name": "thin_walled",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "tangent",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "coat",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "coat_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "coat_roughness",
                "typeString": "float",
                "valueString": "0.1"
            },
            {
                "name": "coat_IOR",
                "typeString": "float",
                "valueString": "1.5"
            },
            {
                "name": "coat_anisotropy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "coat_rotation",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "coat_normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "coat_affect_color",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "coat_affect_roughness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "thin_film_thickness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "thin_film_IOR",
                "typeString": "float",
                "valueString": "1.5"
            },
            {
                "name": "emission",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "emission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "opacity",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "caustics",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "internal_reflections",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "exit_to_background",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "indirect_diffuse",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "indirect_specular",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "aov_id1",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id1",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id2",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id2",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id3",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id3",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id4",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id4",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id5",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id5",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id6",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id6",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id7",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id7",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id8",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id8",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "hair": {
        "typeString": "closure",
        "port": [
            {
                "name": "rootcolor",
                "typeString": "color3",
                "valueString": "0.1, 0.1, 0.1"
            },
            {
                "name": "tipcolor",
                "typeString": "color3",
                "valueString": "0.5, 0.5, 0.5"
            },
            {
                "name": "opacity",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "ambdiff",
                "typeString": "float",
                "valueString": "0.6"
            },
            {
                "name": "spec",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "spec_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "spec_shift",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "spec_gloss",
                "typeString": "float",
                "valueString": "10"
            },
            {
                "name": "spec2",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "spec2_color",
                "typeString": "color3",
                "valueString": "1, 0.4, 0.1"
            },
            {
                "name": "spec2_shift",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "spec2_gloss",
                "typeString": "float",
                "valueString": "7"
            },
            {
                "name": "transmission",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transmission_color",
                "typeString": "color3",
                "valueString": "1, 0.4, 0.1"
            },
            {
                "name": "transmission_spread",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "kd_ind",
                "typeString": "float",
                "valueString": "0"
            }
        ]
    },
    "standard_hair": {
        "typeString": "closure",
        "port": [
            {
                "name": "base",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "base_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "melanin",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "melanin_redness",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "melanin_randomize",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "roughness",
                "typeString": "float",
                "valueString": "0.2"
            },
            {
                "name": "roughness_azimuthal",
                "typeString": "float",
                "valueString": "0.2"
            },
            {
                "name": "roughness_anisotropic",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "ior",
                "typeString": "float",
                "valueString": "1.55"
            },
            {
                "name": "shift",
                "typeString": "float",
                "valueString": "3"
            },
            {
                "name": "specular_tint",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular2_tint",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transmission_tint",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "diffuse",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "diffuse_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "emission",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "emission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "opacity",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "indirect_diffuse",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "indirect_specular",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "extra_depth",
                "typeString": "integer",
                "valueString": "16"
            },
            {
                "name": "extra_samples",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "aov_id1",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id1",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id2",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id2",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id3",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id3",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id4",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id4",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id5",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id5",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id6",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id6",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id7",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id7",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_id8",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "id8",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "car_paint": {
        "typeString": "closure",
        "port": [
            {
                "name": "base",
                "typeString": "float",
                "valueString": "0.8"
            },
            {
                "name": "base_color",
                "typeString": "color3",
                "valueString": "1, 0, 0"
            },
            {
                "name": "base_roughness",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "specular",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "specular_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular_flip_flop",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular_light_facing",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular_falloff",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "specular_roughness",
                "typeString": "float",
                "valueString": "0.05"
            },
            {
                "name": "specular_IOR",
                "typeString": "float",
                "valueString": "1.52"
            },
            {
                "name": "transmission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "flake_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "flake_flip_flop",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "flake_light_facing",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "flake_falloff",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "flake_roughness",
                "typeString": "float",
                "valueString": "0.4"
            },
            {
                "name": "flake_IOR",
                "typeString": "float",
                "valueString": "100"
            },
            {
                "name": "flake_scale",
                "typeString": "float",
                "valueString": "0.001"
            },
            {
                "name": "flake_density",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "flake_layers",
                "typeString": "integer",
                "valueString": "1"
            },
            {
                "name": "flake_normal_randomize",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "flake_coord_space",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "pref_name",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "coat",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "coat_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "coat_roughness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "coat_IOR",
                "typeString": "float",
                "valueString": "1.5"
            },
            {
                "name": "coat_normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "bump2d": {
        "typeString": "vector3",
        "port": [
            {
                "name": "bump_map",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "bump_height",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "bump3d": {
        "typeString": "vector3",
        "port": [
            {
                "name": "bump_map",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "bump_height",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "epsilon",
                "typeString": "float",
                "valueString": "1e-05"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "mix_shader": {
        "typeString": "closure",
        "port": [
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "blend"
            },
            {
                "name": "mix",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "shader1",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "shader2",
                "typeString": "closure",
                "valueString": ""
            }
        ]
    },
    "sky": {
        "typeString": "closure",
        "port": [
            {
                "name": "color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "intensity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "visibility",
                "typeString": "integer",
                "valueString": "-940211969"
            },
            {
                "name": "opaque_alpha",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "format",
                "typeString": "string",
                "valueString": "angular"
            },
            {
                "name": "X_angle",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Y_angle",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "Z_angle",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "X",
                "typeString": "vector3",
                "valueString": "1, 0, 0"
            },
            {
                "name": "Y",
                "typeString": "vector3",
                "valueString": "0, 1, 0"
            },
            {
                "name": "Z",
                "typeString": "vector3",
                "valueString": "0, 0, 1"
            }
        ]
    },
    "physical_sky": {
        "typeString": "color4",
        "port": [
            {
                "name": "turbidity",
                "typeString": "float",
                "valueString": "3"
            },
            {
                "name": "ground_albedo",
                "typeString": "color3",
                "valueString": "0.1, 0.1, 0.1"
            },
            {
                "name": "use_degrees",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "elevation",
                "typeString": "float",
                "valueString": "45"
            },
            {
                "name": "azimuth",
                "typeString": "float",
                "valueString": "90"
            },
            {
                "name": "sun_direction",
                "typeString": "vector3",
                "valueString": "0, 1, 0"
            },
            {
                "name": "enable_sun",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "sun_size",
                "typeString": "float",
                "valueString": "0.51"
            },
            {
                "name": "sun_tint",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "sky_tint",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "intensity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "X",
                "typeString": "vector3",
                "valueString": "1, 0, 0"
            },
            {
                "name": "Y",
                "typeString": "vector3",
                "valueString": "0, 1, 0"
            },
            {
                "name": "Z",
                "typeString": "vector3",
                "valueString": "0, 0, 1"
            }
        ]
    },
    "atmosphere_volume": {
        "typeString": "closure",
        "port": [
            {
                "name": "density",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "samples",
                "typeString": "integer",
                "valueString": "5"
            },
            {
                "name": "eccentricity",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "attenuation",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "affect_camera",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "affect_diffuse",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "affect_specular",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "rgb_density",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "rgb_attenuation",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "fog": {
        "typeString": "closure",
        "port": [
            {
                "name": "distance",
                "typeString": "float",
                "valueString": "0.02"
            },
            {
                "name": "height",
                "typeString": "float",
                "valueString": "5"
            },
            {
                "name": "color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "ground_point",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "ground_normal",
                "typeString": "vector3",
                "valueString": "0, 0, 1"
            }
        ]
    },
    "standard_volume": {
        "typeString": "closure",
        "port": [
            {
                "name": "density",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "density_channel",
                "typeString": "string",
                "valueString": "density"
            },
            {
                "name": "scatter",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "scatter_color",
                "typeString": "color3",
                "valueString": "0.5, 0.5, 0.5"
            },
            {
                "name": "scatter_color_channel",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "scatter_anisotropy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "transparent",
                "typeString": "color3",
                "valueString": "0.367879, 0.367879, 0.367879"
            },
            {
                "name": "transparent_depth",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "transparent_channel",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "emission_mode",
                "typeString": "string",
                "valueString": "blackbody"
            },
            {
                "name": "emission",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "emission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "emission_channel",
                "typeString": "string",
                "valueString": "heat"
            },
            {
                "name": "temperature",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "temperature_channel",
                "typeString": "string",
                "valueString": "temperature"
            },
            {
                "name": "blackbody_kelvin",
                "typeString": "float",
                "valueString": "5000"
            },
            {
                "name": "blackbody_intensity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "displacement",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "interpolation",
                "typeString": "string",
                "valueString": "trilinear"
            }
        ]
    },
    "abs": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "add": {
        "typeString": "color3",
        "port": [
            {
                "name": "input1",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "input2",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "aov_read_float": {
        "typeString": "float",
        "port": [
            {
                "name": "aov_name",
                "typeString": "string",
                "valueString": ""
            }
        ]
    },
    "aov_read_int": {
        "typeString": "integer",
        "port": [
            {
                "name": "aov_name",
                "typeString": "string",
                "valueString": ""
            }
        ]
    },
    "aov_read_rgb": {
        "typeString": "color3",
        "port": [
            {
                "name": "aov_name",
                "typeString": "string",
                "valueString": ""
            }
        ]
    },
    "aov_read_rgba": {
        "typeString": "color4",
        "port": [
            {
                "name": "aov_name",
                "typeString": "string",
                "valueString": ""
            }
        ]
    },
    "aov_write_float": {
        "typeString": "closure",
        "port": [
            {
                "name": "passthrough",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "aov_input",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "aov_name",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "blend_opacity",
                "typeString": "boolean",
                "valueString": "true"
            }
        ]
    },
    "aov_write_int": {
        "typeString": "closure",
        "port": [
            {
                "name": "passthrough",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "aov_input",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "aov_name",
                "typeString": "string",
                "valueString": ""
            }
        ]
    },
    "aov_write_rgb": {
        "typeString": "closure",
        "port": [
            {
                "name": "passthrough",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "aov_input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "aov_name",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "blend_opacity",
                "typeString": "boolean",
                "valueString": "true"
            }
        ]
    },
    "aov_write_rgba": {
        "typeString": "closure",
        "port": [
            {
                "name": "passthrough",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "aov_input",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "aov_name",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "blend_opacity",
                "typeString": "boolean",
                "valueString": "true"
            }
        ]
    },
    "atan": {
        "typeString": "color3",
        "port": [
            {
                "name": "y",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "x",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "units",
                "typeString": "string",
                "valueString": "radians"
            }
        ]
    },
    "blackbody": {
        "typeString": "color4",
        "port": [
            {
                "name": "temperature",
                "typeString": "float",
                "valueString": "6500"
            },
            {
                "name": "normalize",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "intensity",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "cache": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "camera_projection": {
        "typeString": "color4",
        "port": [
            {
                "name": "projection_color",
                "typeString": "color4",
                "valueString": "1, 1, 1, 1"
            },
            {
                "name": "offscreen_color",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mask",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "camera",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "aspect_ratio",
                "typeString": "float",
                "valueString": "1.333"
            },
            {
                "name": "front_facing",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "back_facing",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "use_shading_normal",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "coord_space",
                "typeString": "string",
                "valueString": "world"
            },
            {
                "name": "pref_name",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "P",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "checkerboard": {
        "typeString": "color3",
        "port": [
            {
                "name": "color1",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "color2",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "u_frequency",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "v_frequency",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "u_offset",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "v_offset",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "contrast",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "filter_strength",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "filter_offset",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "uvset",
                "typeString": "string",
                "valueString": ""
            }
        ]
    },
    "clamp": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "scalar"
            },
            {
                "name": "min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "max",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "min_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "max_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "clip_geo": {
        "typeString": "closure",
        "port": [
            {
                "name": "intersection",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "trace_set",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "inclusive",
                "typeString": "boolean",
                "valueString": "true"
            }
        ]
    },
    "color_convert": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "from",
                "typeString": "string",
                "valueString": "RGB"
            },
            {
                "name": "to",
                "typeString": "string",
                "valueString": "HSV"
            }
        ]
    },
    "color_correct": {
        "typeString": "color4",
        "port": [
            {
                "name": "input",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "alpha_is_luminance",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "alpha_multiply",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "alpha_add",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "invert",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "invert_alpha",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "gamma",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "hue_shift",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "saturation",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "contrast",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "contrast_pivot",
                "typeString": "float",
                "valueString": "0.18"
            },
            {
                "name": "exposure",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "multiply",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "add",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "mask",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "color_jitter": {
        "typeString": "color4",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "data_input",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "data_gain_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "data_gain_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "data_hue_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "data_hue_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "data_saturation_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "data_saturation_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "data_seed",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "proc_gain_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "proc_gain_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "proc_hue_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "proc_hue_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "proc_saturation_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "proc_saturation_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "proc_seed",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "obj_gain_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "obj_gain_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "obj_hue_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "obj_hue_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "obj_saturation_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "obj_saturation_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "obj_seed",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "face_gain_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "face_gain_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "face_hue_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "face_hue_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "face_saturation_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "face_saturation_max",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "face_seed",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "face_mode",
                "typeString": "string",
                "valueString": "face id"
            }
        ]
    },
    "compare": {
        "typeString": "boolean",
        "port": [
            {
                "name": "test",
                "typeString": "string",
                "valueString": "=="
            },
            {
                "name": "input1",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input2",
                "typeString": "float",
                "valueString": "0"
            }
        ]
    },
    "complement": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "complex_ior": {
        "typeString": "color3",
        "port": [
            {
                "name": "material",
                "typeString": "string",
                "valueString": "custom"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "artistic"
            },
            {
                "name": "reflectivity",
                "typeString": "color3",
                "valueString": "0.925952, 0.720887, 0.504154"
            },
            {
                "name": "edgetint",
                "typeString": "color3",
                "valueString": "0.995524, 0.957415, 0.822776"
            },
            {
                "name": "n",
                "typeString": "vector3",
                "valueString": "0.27105, 0.67693, 1.3164"
            },
            {
                "name": "k",
                "typeString": "vector3",
                "valueString": "3.6092, 2.6247, 2.2921"
            }
        ]
    },
    "composite": {
        "typeString": "color4",
        "port": [
            {
                "name": "A",
                "typeString": "color4",
                "valueString": "1, 0, 0, 1"
            },
            {
                "name": "B",
                "typeString": "color4",
                "valueString": "0, 1, 0, 1"
            },
            {
                "name": "operation",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation",
                "typeString": "string",
                "valueString": "same"
            }
        ]
    },
    "cross": {
        "typeString": "vector3",
        "port": [
            {
                "name": "input1",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "input2",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "curvature": {
        "typeString": "color3",
        "port": [
            {
                "name": "output",
                "typeString": "string",
                "valueString": "convex"
            },
            {
                "name": "samples",
                "typeString": "integer",
                "valueString": "3"
            },
            {
                "name": "radius",
                "typeString": "float",
                "valueString": "0.1"
            },
            {
                "name": "spread",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "threshold",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "bias",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "multiply",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "trace_set",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "inclusive",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "self_only",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "divide": {
        "typeString": "color3",
        "port": [
            {
                "name": "input1",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "input2",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "dot": {
        "typeString": "float",
        "port": [
            {
                "name": "input1",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "input2",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "exp": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "facing_ratio": {
        "typeString": "float",
        "port": [
            {
                "name": "bias",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "gain",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "linear",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "invert",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "flakes": {
        "typeString": "color4",
        "port": [
            {
                "name": "scale",
                "typeString": "float",
                "valueString": "0.1"
            },
            {
                "name": "density",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "step",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "depth",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "IOR",
                "typeString": "float",
                "valueString": "1.52"
            },
            {
                "name": "normal_randomize",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "coord_space",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "pref_name",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "output_space",
                "typeString": "string",
                "valueString": "world"
            }
        ]
    },
    "float_to_int": {
        "typeString": "integer",
        "port": [
            {
                "name": "input",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "round"
            }
        ]
    },
    "float_to_matrix": {
        "typeString": "matrix44",
        "port": [
            {
                "name": "input_00",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "input_01",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_02",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_03",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_10",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_11",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "input_12",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_13",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_20",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_21",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_22",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "input_23",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_30",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_31",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_32",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_33",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "float_to_rgba": {
        "typeString": "color4",
        "port": [
            {
                "name": "r",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "g",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "b",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "a",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "float_to_rgb": {
        "typeString": "color3",
        "port": [
            {
                "name": "r",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "g",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "b",
                "typeString": "float",
                "valueString": "0"
            }
        ]
    },
    "fraction": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "is_finite": {
        "typeString": "boolean",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "layer_float": {
        "typeString": "float",
        "port": [
            {
                "name": "enable1",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name1",
                "typeString": "string",
                "valueString": "layer1"
            },
            {
                "name": "input1",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mix1",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable2",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name2",
                "typeString": "string",
                "valueString": "layer2"
            },
            {
                "name": "input2",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mix2",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "enable3",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name3",
                "typeString": "string",
                "valueString": "layer3"
            },
            {
                "name": "input3",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mix3",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "enable4",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name4",
                "typeString": "string",
                "valueString": "layer4"
            },
            {
                "name": "input4",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mix4",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "enable5",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name5",
                "typeString": "string",
                "valueString": "layer5"
            },
            {
                "name": "input5",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mix5",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "enable6",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name6",
                "typeString": "string",
                "valueString": "layer6"
            },
            {
                "name": "input6",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mix6",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "enable7",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name7",
                "typeString": "string",
                "valueString": "layer7"
            },
            {
                "name": "input7",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mix7",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "enable8",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name8",
                "typeString": "string",
                "valueString": "layer8"
            },
            {
                "name": "input8",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "mix8",
                "typeString": "float",
                "valueString": "0"
            }
        ]
    },
    "layer_rgba": {
        "typeString": "color4",
        "port": [
            {
                "name": "enable1",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name1",
                "typeString": "string",
                "valueString": "layer1"
            },
            {
                "name": "input1",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mix1",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "operation1",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation1",
                "typeString": "string",
                "valueString": "result"
            },
            {
                "name": "enable2",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name2",
                "typeString": "string",
                "valueString": "layer2"
            },
            {
                "name": "input2",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mix2",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "operation2",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation2",
                "typeString": "string",
                "valueString": "result"
            },
            {
                "name": "enable3",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name3",
                "typeString": "string",
                "valueString": "layer3"
            },
            {
                "name": "input3",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mix3",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "operation3",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation3",
                "typeString": "string",
                "valueString": "result"
            },
            {
                "name": "enable4",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name4",
                "typeString": "string",
                "valueString": "layer4"
            },
            {
                "name": "input4",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mix4",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "operation4",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation4",
                "typeString": "string",
                "valueString": "result"
            },
            {
                "name": "enable5",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name5",
                "typeString": "string",
                "valueString": "layer5"
            },
            {
                "name": "input5",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mix5",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "operation5",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation5",
                "typeString": "string",
                "valueString": "result"
            },
            {
                "name": "enable6",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name6",
                "typeString": "string",
                "valueString": "layer6"
            },
            {
                "name": "input6",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mix6",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "operation6",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation6",
                "typeString": "string",
                "valueString": "result"
            },
            {
                "name": "enable7",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name7",
                "typeString": "string",
                "valueString": "layer7"
            },
            {
                "name": "input7",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mix7",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "operation7",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation7",
                "typeString": "string",
                "valueString": "result"
            },
            {
                "name": "enable8",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name8",
                "typeString": "string",
                "valueString": "layer8"
            },
            {
                "name": "input8",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "mix8",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "operation8",
                "typeString": "string",
                "valueString": "over"
            },
            {
                "name": "alpha_operation8",
                "typeString": "string",
                "valueString": "result"
            },
            {
                "name": "clamp",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "layer_shader": {
        "typeString": "closure",
        "port": [
            {
                "name": "enable1",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name1",
                "typeString": "string",
                "valueString": "layer1"
            },
            {
                "name": "input1",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "mix1",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable2",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name2",
                "typeString": "string",
                "valueString": "layer2"
            },
            {
                "name": "input2",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "mix2",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable3",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name3",
                "typeString": "string",
                "valueString": "layer3"
            },
            {
                "name": "input3",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "mix3",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable4",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name4",
                "typeString": "string",
                "valueString": "layer4"
            },
            {
                "name": "input4",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "mix4",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable5",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name5",
                "typeString": "string",
                "valueString": "layer5"
            },
            {
                "name": "input5",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "mix5",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable6",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name6",
                "typeString": "string",
                "valueString": "layer6"
            },
            {
                "name": "input6",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "mix6",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable7",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name7",
                "typeString": "string",
                "valueString": "layer7"
            },
            {
                "name": "input7",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "mix7",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "enable8",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "name8",
                "typeString": "string",
                "valueString": "layer8"
            },
            {
                "name": "input8",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "mix8",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "length": {
        "typeString": "float",
        "port": [
            {
                "name": "input",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "euclidian"
            }
        ]
    },
    "log": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "base",
                "typeString": "color3",
                "valueString": "2.71828, 2.71828, 2.71828"
            }
        ]
    },
    "matrix_interpolate": {
        "typeString": "matrix44",
        "port": [
            {
                "name": "type",
                "typeString": "string",
                "valueString": "time"
            },
            {
                "name": "value",
                "typeString": "float",
                "valueString": "0.5"
            }
        ]
    },
    "matrix_multiply_vector": {
        "typeString": "vector3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "type",
                "typeString": "string",
                "valueString": "point"
            },
            {
                "name": "matrix",
                "typeString": "matrix44",
                "valueString": ""
            }
        ]
    },
    "matrix_transform": {
        "typeString": "matrix44",
        "port": [
            {
                "name": "transform_order",
                "typeString": "string",
                "valueString": "srt"
            },
            {
                "name": "rotation_type",
                "typeString": "string",
                "valueString": "euler"
            },
            {
                "name": "units",
                "typeString": "string",
                "valueString": "degrees"
            },
            {
                "name": "rotation_order",
                "typeString": "string",
                "valueString": "xyz"
            },
            {
                "name": "rotation",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "axis",
                "typeString": "vector3",
                "valueString": "1, 0, 0"
            },
            {
                "name": "angle",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "translate",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "scale",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "pivot",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "matte": {
        "typeString": "closure",
        "port": [
            {
                "name": "passthrough",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "opacity",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "max": {
        "typeString": "color3",
        "port": [
            {
                "name": "input1",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "input2",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "min": {
        "typeString": "color3",
        "port": [
            {
                "name": "input1",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "input2",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "mix_rgba": {
        "typeString": "color4",
        "port": [
            {
                "name": "input1",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input2",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "mix",
                "typeString": "float",
                "valueString": "0.5"
            }
        ]
    },
    "modulo": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "divisor",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "multiply": {
        "typeString": "color3",
        "port": [
            {
                "name": "input1",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "input2",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "negate": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "normalize": {
        "typeString": "vector3",
        "port": [
            {
                "name": "input",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "normal_map": {
        "typeString": "vector3",
        "port": [
            {
                "name": "input",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "tangent",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "order",
                "typeString": "string",
                "valueString": "XYZ"
            },
            {
                "name": "invert_x",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "invert_y",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "invert_z",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "color_to_signed",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "tangent_space",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "strength",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "passthrough": {
        "typeString": "closure",
        "port": [
            {
                "name": "passthrough",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval1",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval2",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval3",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval4",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval5",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval6",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval7",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval8",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval9",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval10",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval11",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval12",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval13",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval14",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval15",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval16",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval17",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval18",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval19",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "eval20",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "pow": {
        "typeString": "color3",
        "port": [
            {
                "name": "base",
                "typeString": "color3",
                "valueString": "2.71828, 2.71828, 2.71828"
            },
            {
                "name": "exponent",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "query_shape": {
        "typeString": "boolean",
        "port": []
    },
    "ramp_float": {
        "typeString": "float",
        "port": [
            {
                "name": "type",
                "typeString": "string",
                "valueString": "custom"
            },
            {
                "name": "input",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "position",
                "typeString": "floatarray",
                "valueString": "0.0, 1.0"
            },
            {
                "name": "value",
                "typeString": "floatarray",
                "valueString": "0.0, 1.0"
            },
            {
                "name": "interpolation",
                "typeString": "integerarray",
                "valueString": "2, 2"
            },
            {
                "name": "uvset",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "use_implicit_uvs",
                "typeString": "string",
                "valueString": "off"
            },
            {
                "name": "wrap_uvs",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "ramp_rgb": {
        "typeString": "color3",
        "port": [
            {
                "name": "type",
                "typeString": "string",
                "valueString": "custom"
            },
            {
                "name": "input",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "position",
                "typeString": "floatarray",
                "valueString": "0.0, 1.0"
            },
            {
                "name": "color",
                "typeString": "floatarray",
                "valueString": "0.0, 0.0, 0.0, 1.0, 1.0, 1.0"
            },
            {
                "name": "interpolation",
                "typeString": "integerarray",
                "valueString": "2, 2"
            },
            {
                "name": "uvset",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "use_implicit_uvs",
                "typeString": "string",
                "valueString": "off"
            },
            {
                "name": "wrap_uvs",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "random": {
        "typeString": "color3",
        "port": [
            {
                "name": "input_type",
                "typeString": "string",
                "valueString": "int"
            },
            {
                "name": "input_int",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "input_float",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "seed",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "grayscale",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "range": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "input_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_max",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "output_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "output_max",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "smoothstep",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "contrast",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "contrast_pivot",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "bias",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "gain",
                "typeString": "float",
                "valueString": "0.5"
            }
        ]
    },
    "reciprocal": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        ]
    },
    "rgba_to_float": {
        "typeString": "float",
        "port": [
            {
                "name": "input",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "average"
            }
        ]
    },
    "rgb_to_float": {
        "typeString": "float",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "average"
            }
        ]
    },
    "rgb_to_vector": {
        "typeString": "vector3",
        "port": [
            {
                "name": "input",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "raw"
            }
        ]
    },
    "shadow_matte": {
        "typeString": "color4",
        "port": [
            {
                "name": "background",
                "typeString": "string",
                "valueString": "scene_background"
            },
            {
                "name": "shadow_color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "shadow_opacity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "background_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "diffuse_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "diffuse_use_background",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "diffuse_intensity",
                "typeString": "float",
                "valueString": "0.7"
            },
            {
                "name": "backlighting",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "indirect_diffuse_enable",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "indirect_specular_enable",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "specular_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular_intensity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "specular_roughness",
                "typeString": "float",
                "valueString": "0.2"
            },
            {
                "name": "specular_IOR",
                "typeString": "float",
                "valueString": "1.5"
            },
            {
                "name": "alpha_mask",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "aov_group",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "aov_shadow",
                "typeString": "string",
                "valueString": "shadow"
            },
            {
                "name": "aov_shadow_diff",
                "typeString": "string",
                "valueString": "shadow_diff"
            },
            {
                "name": "aov_shadow_mask",
                "typeString": "string",
                "valueString": "shadow_mask"
            }
        ]
    },
    "shuffle": {
        "typeString": "color4",
        "port": [
            {
                "name": "color",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "alpha",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "channel_r",
                "typeString": "string",
                "valueString": "R"
            },
            {
                "name": "channel_g",
                "typeString": "string",
                "valueString": "G"
            },
            {
                "name": "channel_b",
                "typeString": "string",
                "valueString": "B"
            },
            {
                "name": "channel_a",
                "typeString": "string",
                "valueString": "A"
            },
            {
                "name": "negate_r",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "negate_g",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "negate_b",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "negate_a",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "sign": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "skin": {
        "typeString": "closure",
        "port": [
            {
                "name": "sss_weight",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "shallow_scatter_color",
                "typeString": "color3",
                "valueString": "1, 0.909, 0.769"
            },
            {
                "name": "shallow_scatter_weight",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "shallow_scatter_radius",
                "typeString": "float",
                "valueString": "0.15"
            },
            {
                "name": "mid_scatter_color",
                "typeString": "color3",
                "valueString": "0.949, 0.714, 0.56"
            },
            {
                "name": "mid_scatter_weight",
                "typeString": "float",
                "valueString": "0.25"
            },
            {
                "name": "mid_scatter_radius",
                "typeString": "float",
                "valueString": "0.25"
            },
            {
                "name": "deep_scatter_color",
                "typeString": "color3",
                "valueString": "0.7, 0.1, 0.1"
            },
            {
                "name": "deep_scatter_weight",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "deep_scatter_radius",
                "typeString": "float",
                "valueString": "0.6"
            },
            {
                "name": "specular_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "specular_weight",
                "typeString": "float",
                "valueString": "0.8"
            },
            {
                "name": "specular_roughness",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "specular_ior",
                "typeString": "float",
                "valueString": "1.44"
            },
            {
                "name": "sheen_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "sheen_weight",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "sheen_roughness",
                "typeString": "float",
                "valueString": "0.35"
            },
            {
                "name": "sheen_ior",
                "typeString": "float",
                "valueString": "1.44"
            },
            {
                "name": "global_sss_radius_multiplier",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "specular_in_secondary_rays",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "fresnel_affect_sss",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "opacity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "opacity_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 1, 0"
            }
        ]
    },
    "space_transform": {
        "typeString": "vector3",
        "port": [
            {
                "name": "input",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "type",
                "typeString": "string",
                "valueString": "point"
            },
            {
                "name": "from",
                "typeString": "string",
                "valueString": "world"
            },
            {
                "name": "to",
                "typeString": "string",
                "valueString": "world"
            },
            {
                "name": "tangent",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "normalize",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "scale",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "sqrt": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "state_float": {
        "typeString": "float",
        "port": [
            {
                "name": "variable",
                "typeString": "string",
                "valueString": "sx"
            }
        ]
    },
    "state_int": {
        "typeString": "integer",
        "port": [
            {
                "name": "variable",
                "typeString": "string",
                "valueString": "x"
            }
        ]
    },
    "state_vector": {
        "typeString": "vector3",
        "port": [
            {
                "name": "variable",
                "typeString": "string",
                "valueString": "Ro"
            }
        ]
    },
    "subtract": {
        "typeString": "color3",
        "port": [
            {
                "name": "input1",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "input2",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "switch_rgba": {
        "typeString": "color4",
        "port": [
            {
                "name": "index",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "input0",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input1",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input2",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input3",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input4",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input5",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input6",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input7",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input8",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input9",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input10",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input11",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input12",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input13",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input14",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input15",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input16",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input17",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input18",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "input19",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            }
        ]
    },
    "switch_shader": {
        "typeString": "closure",
        "port": [
            {
                "name": "index",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "input0",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input1",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input2",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input3",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input4",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input5",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input6",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input7",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input8",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input9",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input10",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input11",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input12",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input13",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input14",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input15",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input16",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input17",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input18",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "input19",
                "typeString": "closure",
                "valueString": ""
            }
        ]
    },
    "thin_film": {
        "typeString": "color3",
        "port": [
            {
                "name": "thickness_min",
                "typeString": "float",
                "valueString": "250"
            },
            {
                "name": "thickness_max",
                "typeString": "float",
                "valueString": "400"
            },
            {
                "name": "thickness",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "ior_medium",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "ior_film",
                "typeString": "float",
                "valueString": "1.5"
            },
            {
                "name": "ior_internal",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "trace_set": {
        "typeString": "closure",
        "port": [
            {
                "name": "passthrough",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "trace_set",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "inclusive",
                "typeString": "boolean",
                "valueString": "true"
            }
        ]
    },
    "trigo": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "function",
                "typeString": "string",
                "valueString": "cos"
            },
            {
                "name": "units",
                "typeString": "string",
                "valueString": "radians"
            },
            {
                "name": "frequency",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "phase",
                "typeString": "float",
                "valueString": "0"
            }
        ]
    },
    "triplanar": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "scale",
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "rotate",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "offset",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "coord_space",
                "typeString": "string",
                "valueString": "object"
            },
            {
                "name": "pref_name",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "blend",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "cell",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "cell_rotate",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "cell_blend",
                "typeString": "float",
                "valueString": "0.1"
            }
        ]
    },
    "two_sided": {
        "typeString": "closure",
        "port": [
            {
                "name": "front",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "back",
                "typeString": "closure",
                "valueString": ""
            }
        ]
    },
    "user_data_float": {
        "typeString": "float",
        "port": [
            {
                "name": "port",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "default",
                "typeString": "float",
                "valueString": "0"
            }
        ]
    },
    "user_data_int": {
        "typeString": "integer",
        "port": [
            {
                "name": "port",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "default",
                "typeString": "integer",
                "valueString": "0"
            }
        ]
    },
    "user_data_rgba": {
        "typeString": "color4",
        "port": [
            {
                "name": "port",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "default",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            }
        ]
    },
    "user_data_rgb": {
        "typeString": "color3",
        "port": [
            {
                "name": "port",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "default",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        ]
    },
    "user_data_string": {
        "typeString": "string",
        "port": [
            {
                "name": "port",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "default",
                "typeString": "string",
                "valueString": ""
            }
        ]
    },
    "uv_transform": {
        "typeString": "color4",
        "port": [
            {
                "name": "passthrough",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "unit",
                "typeString": "string",
                "valueString": "degrees"
            },
            {
                "name": "uvset",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "coverage",
                "typeString": "vector2",
                "valueString": "1, 1"
            },
            {
                "name": "scale_frame",
                "typeString": "vector2",
                "valueString": "1, 1"
            },
            {
                "name": "translate_frame",
                "typeString": "vector2",
                "valueString": "0, 0"
            },
            {
                "name": "rotate_frame",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "pivot_frame",
                "typeString": "vector2",
                "valueString": "0.5, 0.5"
            },
            {
                "name": "wrap_frame_u",
                "typeString": "string",
                "valueString": "periodic"
            },
            {
                "name": "wrap_frame_v",
                "typeString": "string",
                "valueString": "periodic"
            },
            {
                "name": "wrap_frame_color",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "repeat",
                "typeString": "vector2",
                "valueString": "1, 1"
            },
            {
                "name": "offset",
                "typeString": "vector2",
                "valueString": "0, 0"
            },
            {
                "name": "rotate",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "pivot",
                "typeString": "vector2",
                "valueString": "0.5, 0.5"
            },
            {
                "name": "noise",
                "typeString": "vector2",
                "valueString": "0, 0"
            },
            {
                "name": "mirror_u",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "mirror_v",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "flip_u",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "flip_v",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "swap_uv",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "stagger",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "uv_projection": {
        "typeString": "color4",
        "port": [
            {
                "name": "projection_color",
                "typeString": "color4",
                "valueString": "1, 1, 1, 1"
            },
            {
                "name": "projection_type",
                "typeString": "string",
                "valueString": "planar"
            },
            {
                "name": "coord_space",
                "typeString": "string",
                "valueString": "world"
            },
            {
                "name": "pref_name",
                "typeString": "string",
                "valueString": "Pref"
            },
            {
                "name": "P",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "u_angle",
                "typeString": "float",
                "valueString": "180"
            },
            {
                "name": "v_angle",
                "typeString": "float",
                "valueString": "90"
            },
            {
                "name": "clamp",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "default_color",
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            {
                "name": "matrix",
                "typeString": "matrix44",
                "valueString": ""
            }
        ]
    },
    "vector_map": {
        "typeString": "vector3",
        "port": [
            {
                "name": "input",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "tangent",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "normal",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "order",
                "typeString": "string",
                "valueString": "XYZ"
            },
            {
                "name": "invert_x",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "invert_y",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "invert_z",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "color_to_signed",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "tangent_space",
                "typeString": "boolean",
                "valueString": "true"
            },
            {
                "name": "scale",
                "typeString": "float",
                "valueString": "1"
            }
        ]
    },
    "vector_to_rgb": {
        "typeString": "color3",
        "port": [
            {
                "name": "input",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "mode",
                "typeString": "string",
                "valueString": "raw"
            }
        ]
    },
    "volume_collector": {
        "typeString": "closure",
        "port": [
            {
                "name": "scattering_source",
                "typeString": "string",
                "valueString": "parameter"
            },
            {
                "name": "scattering",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "scattering_channel",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "scattering_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "scattering_intensity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "anisotropy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "attenuation_source",
                "typeString": "string",
                "valueString": "parameter"
            },
            {
                "name": "attenuation",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "attenuation_channel",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "attenuation_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "attenuation_intensity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "attenuation_mode",
                "typeString": "string",
                "valueString": "absorption"
            },
            {
                "name": "emission_source",
                "typeString": "string",
                "valueString": "parameter"
            },
            {
                "name": "emission",
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "emission_channel",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "emission_color",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "emission_intensity",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "position_offset",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "interpolation",
                "typeString": "string",
                "valueString": "trilinear"
            }
        ]
    },
    "volume_sample_float": {
        "typeString": "float",
        "port": [
            {
                "name": "channel",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "position_offset",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "interpolation",
                "typeString": "string",
                "valueString": "trilinear"
            },
            {
                "name": "volume_type",
                "typeString": "string",
                "valueString": "fog"
            },
            {
                "name": "sdf_offset",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "sdf_blend",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "sdf_invert",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "input_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "input_max",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "contrast",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "contrast_pivot",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "bias",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "gain",
                "typeString": "float",
                "valueString": "0.5"
            },
            {
                "name": "output_min",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "output_max",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "clamp_min",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "clamp_max",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    },
    "volume_sample_rgb": {
        "typeString": "color3",
        "port": [
            {
                "name": "channel",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "position_offset",
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            {
                "name": "interpolation",
                "typeString": "string",
                "valueString": "trilinear"
            },
            {
                "name": "gamma",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "hue_shift",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "saturation",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "contrast",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "contrast_pivot",
                "typeString": "float",
                "valueString": "0.18"
            },
            {
                "name": "exposure",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "multiply",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "add",
                "typeString": "float",
                "valueString": "0"
            }
        ]
    },
    "c4d_texture_tag": {
        "typeString": "closure",
        "port": [
            {
                "name": "color",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "proj",
                "typeString": "string",
                "valueString": "spherical"
            },
            {
                "name": "lenx",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "leny",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "ox",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "oy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "tilex",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "tiley",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "m",
                "typeString": "matrix44",
                "valueString": ""
            },
            {
                "name": "camera",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "aspect_ratio",
                "typeString": "float",
                "valueString": "1.33333"
            },
            {
                "name": "use_pref",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "side",
                "typeString": "integer",
                "valueString": "0"
            }
        ]
    },
    "c4d_texture_tag_rgba": {
        "typeString": "color4",
        "port": [
            {
                "name": "color",
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            {
                "name": "proj",
                "typeString": "string",
                "valueString": "spherical"
            },
            {
                "name": "lenx",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "leny",
                "typeString": "float",
                "valueString": "1"
            },
            {
                "name": "ox",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "oy",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "tilex",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "tiley",
                "typeString": "float",
                "valueString": "0"
            },
            {
                "name": "m",
                "typeString": "matrix44",
                "valueString": ""
            },
            {
                "name": "camera",
                "typeString": "string",
                "valueString": ""
            },
            {
                "name": "aspect_ratio",
                "typeString": "float",
                "valueString": "1.33333"
            },
            {
                "name": "use_pref",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "side",
                "typeString": "integer",
                "valueString": "0"
            }
        ]
    },
    "maya_layered_shader": {
        "typeString": "closure",
        "port": [
            {
                "name": "compositingFlag",
                "typeString": "string",
                "valueString": "shader"
            },
            {
                "name": "numInputs",
                "typeString": "integer",
                "valueString": "0"
            },
            {
                "name": "color0",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color1",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color2",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color3",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color4",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color5",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color6",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color7",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color8",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color9",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color10",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color11",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color12",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color13",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color14",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "color15",
                "typeString": "closure",
                "valueString": ""
            },
            {
                "name": "transparency0",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency1",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency2",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency3",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency4",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency5",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency6",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency7",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency8",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency9",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency10",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency11",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency12",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency13",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency14",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "transparency15",
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            {
                "name": "useTransparency0",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency1",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency2",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency3",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency4",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency5",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency6",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency7",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency8",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency9",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency10",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency11",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency12",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency13",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency14",
                "typeString": "boolean",
                "valueString": "false"
            },
            {
                "name": "useTransparency15",
                "typeString": "boolean",
                "valueString": "false"
            }
        ]
    }
}
