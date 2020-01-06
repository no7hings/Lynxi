# coding:utf-8
import collections

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


class Basic(object):
    Key_Label = 'label'
    Key_Category = 'category'
    Key_Category_String = 'categoryString'
    Key_Type = 'type'
    Key_Type_String = 'typeString'
    Key_Value_String = 'valueString'
    Key_Attribute = 'attribute'
    Key_Children = 'children'
    Key_Element = 'element'

    Key_Name = 'name'
    Key_FullpathName = 'fullpathName'

    Atr_Xml_Name = 'name'
    Atr_Xml_Node = 'node'
    Atr_Xml_Type = 'type'
    Atr_Xml_Material = 'material'
    Atr_Xml_Geom = 'geom'

    Atr_Xml_Value = 'value'

    Atr_Xml_Shader_Output_Type = 'context'

    cls_order_dic = collections.OrderedDict

    def _xmlStrRaw(self):
        return {
            self.Key_Label: 'basic_label',
            self.Key_Attribute: {
                self.Atr_Xml_Name: 'basic_name'
            },
            self.Key_Children: []
        }

    @classmethod
    def _toXmlStringMethod(cls, raw, indent=4):
        def addCategoryFnc_(raw_, lString, rString):
            lis.append(u'{}<{}{}'.format(lString, raw_, rString))

        def addAttributeFnc_(raw_, lString, rString):
            if raw_:
                for k, v in raw_.items():
                    lis.append(u'{}{}="{}"{}'.format(lString, k, v, rString))

        def addChildrenFnc_(raw_, lString, rString):
            if raw_:
                for i in raw_:
                    if hasattr(i, '_xmlStrRaw'):
                        addRawFnc_(i._xmlStrRaw(), lString, rString)

        def addRawFnc_(raw_, lString, rString):
            lString += defIndentString
            label = raw_[cls.Key_Label]

            addCategoryFnc_(
                raw_[cls.Key_Label], lString=lString, rString=' '
            )
            addAttributeFnc_(
                raw_[cls.Key_Attribute], lString='', rString=' '
            )
            children = raw_.get(cls.Key_Children)
            if children:
                lis.append(u'>\r\n')
                addChildrenFnc_(
                    raw_[cls.Key_Children], lString, rString
                )
                lis.append(u'{}</{}>\r\n'.format(lString, label))
            else:
                lis.append(u'/>\r\n')

            elements = raw_.get(cls.Key_Element)
            if elements:
                [addRawFnc_(i._xmlStrRaw(), lString='', rString='') for i in elements]

        defIndentString = ' ' * indent

        lis = [
            u'<?xml version="1.0"?>\r\n',
            u'<materialx version="1.36">\r\n',
            u'{}<xi:include href="materialx/arnold/nodedefs.mtlx" />\r\n'.format(defIndentString)
        ]
        addRawFnc_(raw, lString='', rString='')
        lis.append(
            u'</materialx>'
        )
        return ''.join(lis)

    @classmethod
    def _toJsonStringMethod(cls, raw, indent=4):
        def addNoneFnc_(lString, rString):
            lis.append(u'{}null{}'.format(lString, rString))

        def addStringFnc_(raw_, lString, rString):
            lis.append(u'{}"{}"{}'.format(lString, raw_, rString))

        def addUnicodeFnc_(raw_, lString, rString):
            lis.append(u'{}"{}"{}'.format(lString, raw_, rString))

        def addNumberFnc_(raw_, lString, rString):
            lis.append(u'{}{}{}'.format(lString, raw_, rString))

        def addBooleanFnc_(raw_, lString, rString):
            lis.append(u'{}{}{}'.format(lString, str(raw_).lower(), rString))

        def addMemberFnc_(raw_, lString, rString):
            if isinstance(raw_, bool):
                addBooleanFnc_(raw_, lString, rString)

            elif isinstance(raw_, int) or isinstance(raw_, float):
                addNumberFnc_(raw_, lString, rString)

            elif isinstance(raw_, str):
                addStringFnc_(raw_, lString, rString)

            elif isinstance(raw_, unicode):
                addUnicodeFnc_(raw_, lString, rString)

        def addValueFnc_(raw_, lString, rString, rawType=None):
            if raw_ is None:
                addNoneFnc_(lString=lString, rString='\r\n')

            elif isinstance(raw_, list) or isinstance(raw_, tuple):
                lString += defIndentString
                addListFnc_(raw_, lString=lString, rString=rString)

            elif isinstance(raw_, dict):
                lString += defIndentString
                addDictionaryFnc_(raw_, lString=lString, rString=rString)

            else:
                if rawType == dict:
                    addMemberFnc_(raw_, lString='', rString=rString)
                else:
                    addMemberFnc_(raw_, lString=lString+defIndentString, rString=rString)

        def addListFnc_(raw_, lString, rString):
            if raw_:
                lis.append(u'{lString}[{rString}'.format(lString='', rString='\r\n'))

                c = len(raw_)
                for seq, i in enumerate(raw_):
                    if seq < c - 1:
                        addValueFnc_(i, lString=lString, rString=',\r\n', rawType=list)
                    else:
                        addValueFnc_(i, lString=lString, rString='\r\n', rawType=list)

                lis.append(u'{lString}]{rString}'.format(lString=lString, rString=rString))

            else:
                lis.append(u'{lString}[]{rString}\r\n'.format(lString=lString, rString=rString))

        def addDictionaryFnc_(raw_, lString, rString):
            if raw_:
                lis.append(u'{lString}{{{rString}'.format(lString='', rString='\r\n'))

                c = len(raw_)
                for seq, (k, v) in enumerate(raw_.items()):
                    addMemberFnc_(k, lString=lString + defIndentString, rString=': ')

                    if seq < c - 1:
                        addValueFnc_(v, lString=lString, rString=',\r\n', rawType=dict)
                    else:
                        addValueFnc_(v, lString=lString, rString='\r\n', rawType=dict)

                lis.append(u'{lString}}}{rString}'.format(lString=lString, rString=rString))

            else:
                lis.append(u'{lString}{{}}{rString}'.format(lString='', rString=rString))

        def addRawFnc_(raw_):
            if raw_ is None:
                addNoneFnc_(lString='', rString='\r\n')

            elif isinstance(raw_, list) or isinstance(raw_, tuple):
                addListFnc_(raw_, lString='', rString='\r\n')

            elif isinstance(raw_, dict):
                addDictionaryFnc_(raw_, lString='', rString='\r\n')

        defIndentString = ' ' * indent

        lis = [
            u'{} = '.format(cls.__name__)
        ]

        addRawFnc_(raw)

        return ''.join(lis)

    def __str__(self):
        return self._toXmlStringMethod(self._xmlStrRaw())


Def_Node_Dic = {
    "geometry": {
        "typeString": "geometry",
    },
    "ray_switch_rgba": {
        "typeString": "color4",
        "attribute": {
            "camera": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "shadow": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "diffuse_reflection": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "diffuse_transmission": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "specular_reflection": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "specular_transmission": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "volume": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            }
        }
    },
    "ray_switch_shader": {
        "typeString": "closure",
        "attribute": {
            "camera": {
                "typeString": "closure",
                "valueString": ""
            },
            "shadow": {
                "typeString": "closure",
                "valueString": ""
            },
            "diffuse_reflection": {
                "typeString": "closure",
                "valueString": ""
            },
            "diffuse_transmission": {
                "typeString": "closure",
                "valueString": ""
            },
            "specular_reflection": {
                "typeString": "closure",
                "valueString": ""
            },
            "specular_transmission": {
                "typeString": "closure",
                "valueString": ""
            },
            "volume": {
                "typeString": "closure",
                "valueString": ""
            }
        }
    },
    "image": {
        "typeString": "color4",
        "attribute": {
            "filename": {
                "typeString": "string",
                "valueString": ""
            },
            "color_space": {
                "typeString": "string",
                "valueString": "auto"
            },
            "filter": {
                "typeString": "string",
                "valueString": "smart_bicubic"
            },
            "mipmap_bias": {
                "typeString": "integer",
                "valueString": "0"
            },
            "single_channel": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "start_channel": {
                "typeString": "integer",
                "valueString": "-401153280"
            },
            "swrap": {
                "typeString": "string",
                "valueString": "periodic"
            },
            "twrap": {
                "typeString": "string",
                "valueString": "periodic"
            },
            "sscale": {
                "typeString": "float",
                "valueString": "1"
            },
            "tscale": {
                "typeString": "float",
                "valueString": "1"
            },
            "sflip": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "tflip": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "soffset": {
                "typeString": "float",
                "valueString": "0"
            },
            "toffset": {
                "typeString": "float",
                "valueString": "0"
            },
            "swap_st": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "uvcoords": {
                "typeString": "vector2",
                "valueString": "0, 0"
            },
            "uvset": {
                "typeString": "string",
                "valueString": ""
            },
            "multiply": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "offset": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "ignore_missing_textures": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "missing_texturecls_color": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            }
        }
    },
    "noise": {
        "typeString": "color3",
        "attribute": {
            "octaves": {
                "typeString": "integer",
                "valueString": "1"
            },
            "distortion": {
                "typeString": "float",
                "valueString": "0"
            },
            "lacunarity": {
                "typeString": "float",
                "valueString": "1.92"
            },
            "amplitude": {
                "typeString": "float",
                "valueString": "1"
            },
            "scale": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            "offset": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "coord_space": {
                "typeString": "string",
                "valueString": "object"
            },
            "pref_name": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "P": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "time": {
                "typeString": "float",
                "valueString": "0"
            },
            "color1": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "color2": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "mode": {
                "typeString": "string",
                "valueString": "scalar"
            }
        }
    },
    "cell_noise": {
        "typeString": "color3",
        "attribute": {
            "pattern": {
                "typeString": "string",
                "valueString": "noise1"
            },
            "additive": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "octaves": {
                "typeString": "integer",
                "valueString": "1"
            },
            "randomness": {
                "typeString": "float",
                "valueString": "1"
            },
            "lacunarity": {
                "typeString": "float",
                "valueString": "1.92"
            },
            "amplitude": {
                "typeString": "float",
                "valueString": "1"
            },
            "scale": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            "offset": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "coord_space": {
                "typeString": "string",
                "valueString": "object"
            },
            "pref_name": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "P": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "time": {
                "typeString": "float",
                "valueString": "0"
            },
            "color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "palette": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "density": {
                "typeString": "float",
                "valueString": "0.5"
            }
        }
    },
    "utility": {
        "typeString": "color3",
        "attribute": {
            "color_mode": {
                "typeString": "string",
                "valueString": "color"
            },
            "shade_mode": {
                "typeString": "string",
                "valueString": "ndoteye"
            },
            "overlay_mode": {
                "typeString": "string",
                "valueString": "none"
            },
            "color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "ao_distance": {
                "typeString": "float",
                "valueString": "100"
            },
            "roughness": {
                "typeString": "float",
                "valueString": "0.2"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "wireframe": {
        "typeString": "color3",
        "attribute": {
            "line_width": {
                "typeString": "float",
                "valueString": "1"
            },
            "fillcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "linecls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "raster_space": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "edge_type": {
                "typeString": "string",
                "valueString": "triangles"
            }
        }
    },
    "motion_vector": {
        "typeString": "color3",
        "attribute": {
            "raw": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "time0": {
                "typeString": "float",
                "valueString": "0"
            },
            "time1": {
                "typeString": "float",
                "valueString": "1"
            },
            "max_displace": {
                "typeString": "float",
                "valueString": "0"
            }
        }
    },
    "ambient_occlusion": {
        "typeString": "color3",
        "attribute": {
            "samples": {
                "typeString": "integer",
                "valueString": "3"
            },
            "spread": {
                "typeString": "float",
                "valueString": "1"
            },
            "near_clip": {
                "typeString": "float",
                "valueString": "0"
            },
            "far_clip": {
                "typeString": "float",
                "valueString": "100"
            },
            "falloff": {
                "typeString": "float",
                "valueString": "0"
            },
            "black": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "white": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "invert_normals": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "trace_set": {
                "typeString": "string",
                "valueString": ""
            },
            "inclusive": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "self_only": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "round_corners": {
        "typeString": "vector3",
        "attribute": {
            "samples": {
                "typeString": "integer",
                "valueString": "6"
            },
            "radius": {
                "typeString": "float",
                "valueString": "0.01"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "trace_set": {
                "typeString": "string",
                "valueString": ""
            },
            "inclusive": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "self_only": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "object_space": {
                "typeString": "boolean",
                "valueString": "true"
            }
        }
    },
    "flat": {
        "typeString": "color3",
        "attribute": {
            "color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "toon": {
        "typeString": "color3",
        "attribute": {
            "maskcls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "edgecls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "edge_tonemap": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "edge_opacity": {
                "typeString": "float",
                "valueString": "1"
            },
            "edge_width_scale": {
                "typeString": "float",
                "valueString": "1"
            },
            "silhouettecls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "silhouette_tonemap": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "silhouette_opacity": {
                "typeString": "float",
                "valueString": "1"
            },
            "silhouette_width_scale": {
                "typeString": "float",
                "valueString": "1"
            },
            "priority": {
                "typeString": "integer",
                "valueString": "0"
            },
            "enable_silhouette": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "ignore_throughput": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "enable": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "id_difference": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "shader_difference": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "uv_threshold": {
                "typeString": "float",
                "valueString": "0"
            },
            "angle_threshold": {
                "typeString": "float",
                "valueString": "180"
            },
            "normal_type": {
                "typeString": "string",
                "valueString": "shading normal"
            },
            "base": {
                "typeString": "float",
                "valueString": "0.8"
            },
            "basecls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "base_tonemap": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular": {
                "typeString": "float",
                "valueString": "0"
            },
            "specularcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular_roughness": {
                "typeString": "float",
                "valueString": "0"
            },
            "specular_anisotropy": {
                "typeString": "float",
                "valueString": "0"
            },
            "specular_rotation": {
                "typeString": "float",
                "valueString": "0"
            },
            "specular_tonemap": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "lights": {
                "typeString": "string",
                "valueString": ""
            },
            "highlightcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "highlight_size": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "aov_highlight": {
                "typeString": "string",
                "valueString": "highlight"
            },
            "rim_light": {
                "typeString": "string",
                "valueString": ""
            },
            "rim_lightcls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "rim_light_width": {
                "typeString": "float",
                "valueString": "1"
            },
            "aov_rim_light": {
                "typeString": "string",
                "valueString": "rim_light"
            },
            "transmission": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transmission_roughness": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmission_anisotropy": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmission_rotation": {
                "typeString": "float",
                "valueString": "0"
            },
            "sheen": {
                "typeString": "float",
                "valueString": "0"
            },
            "sheencls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "sheen_roughness": {
                "typeString": "float",
                "valueString": "0.3"
            },
            "emission": {
                "typeString": "float",
                "valueString": "0"
            },
            "emissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "IOR": {
                "typeString": "float",
                "valueString": "1.52"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "tangent": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "indirect_diffuse": {
                "typeString": "float",
                "valueString": "0"
            },
            "indirect_specular": {
                "typeString": "float",
                "valueString": "1"
            },
            "bump_mode": {
                "typeString": "string",
                "valueString": "both"
            },
            "energy_conserving": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "user_id": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "lambert": {
        "typeString": "closure",
        "attribute": {
            "Kd": {
                "typeString": "float",
                "valueString": "0.7"
            },
            "Kdcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "opacity": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "standard": {
        "typeString": "closure",
        "attribute": {
            "Kd": {
                "typeString": "float",
                "valueString": "0.7"
            },
            "Kdcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "diffuse_roughness": {
                "typeString": "float",
                "valueString": "0"
            },
            "Ks": {
                "typeString": "float",
                "valueString": "0"
            },
            "Kscls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular_roughness": {
                "typeString": "float",
                "valueString": "0.466905"
            },
            "specular_anisotropy": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "specular_rotation": {
                "typeString": "float",
                "valueString": "0"
            },
            "specular_distribution": {
                "typeString": "string",
                "valueString": "ggx"
            },
            "Kr": {
                "typeString": "float",
                "valueString": "0"
            },
            "Krcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "reflection_exitcls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "reflection_exit_use_environment": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "Kt": {
                "typeString": "float",
                "valueString": "0"
            },
            "Ktcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transmittance": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "refraction_roughness": {
                "typeString": "float",
                "valueString": "0"
            },
            "refraction_exitcls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "refraction_exit_use_environment": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "IOR": {
                "typeString": "float",
                "valueString": "1"
            },
            "dispersion_abbe": {
                "typeString": "float",
                "valueString": "0"
            },
            "Kb": {
                "typeString": "float",
                "valueString": "0"
            },
            "Fresnel": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "Krn": {
                "typeString": "float",
                "valueString": "0"
            },
            "specular_Fresnel": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "Ksn": {
                "typeString": "float",
                "valueString": "0"
            },
            "Fresnel_use_IOR": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "Fresnel_affect_diff": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "emission": {
                "typeString": "float",
                "valueString": "0"
            },
            "emissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "direct_specular": {
                "typeString": "float",
                "valueString": "1"
            },
            "indirect_specular": {
                "typeString": "float",
                "valueString": "1"
            },
            "direct_diffuse": {
                "typeString": "float",
                "valueString": "1"
            },
            "indirect_diffuse": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable_glossy_caustics": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "enable_reflective_caustics": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "enable_refractive_caustics": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "enable_internal_reflections": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "Ksss": {
                "typeString": "float",
                "valueString": "0"
            },
            "Kssscls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "sss_radius": {
                "typeString": "color3",
                "valueString": "0.1, 0.1, 0.1"
            },
            "bounce_factor": {
                "typeString": "float",
                "valueString": "1"
            },
            "opacity": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "standard_surface": {
        "typeString": "closure",
        "attribute": {
            "base": {
                "typeString": "float",
                "valueString": "0.8"
            },
            "basecls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "diffuse_roughness": {
                "typeString": "float",
                "valueString": "0"
            },
            "specular": {
                "typeString": "float",
                "valueString": "1"
            },
            "specularcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular_roughness": {
                "typeString": "float",
                "valueString": "0.2"
            },
            "specular_IOR": {
                "typeString": "float",
                "valueString": "1.5"
            },
            "specular_anisotropy": {
                "typeString": "float",
                "valueString": "0"
            },
            "specular_rotation": {
                "typeString": "float",
                "valueString": "0"
            },
            "metalness": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmission": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transmission_depth": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmission_scatter": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "transmission_scatter_anisotropy": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmission_dispersion": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmission_extra_roughness": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmit_aovs": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "subsurface": {
                "typeString": "float",
                "valueString": "0"
            },
            "subsurfacecls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "subsurface_radius": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "subsurface_scale": {
                "typeString": "float",
                "valueString": "1"
            },
            "subsurface_anisotropy": {
                "typeString": "float",
                "valueString": "0"
            },
            "subsurface_type": {
                "typeString": "string",
                "valueString": "randomwalk"
            },
            "sheen": {
                "typeString": "float",
                "valueString": "0"
            },
            "sheencls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "sheen_roughness": {
                "typeString": "float",
                "valueString": "0.3"
            },
            "thin_walled": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "tangent": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "coat": {
                "typeString": "float",
                "valueString": "0"
            },
            "coatcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "coat_roughness": {
                "typeString": "float",
                "valueString": "0.1"
            },
            "coat_IOR": {
                "typeString": "float",
                "valueString": "1.5"
            },
            "coat_anisotropy": {
                "typeString": "float",
                "valueString": "0"
            },
            "coat_rotation": {
                "typeString": "float",
                "valueString": "0"
            },
            "coat_normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "coat_affectcls_color": {
                "typeString": "float",
                "valueString": "0"
            },
            "coat_affect_roughness": {
                "typeString": "float",
                "valueString": "0"
            },
            "thin_film_thickness": {
                "typeString": "float",
                "valueString": "0"
            },
            "thin_film_IOR": {
                "typeString": "float",
                "valueString": "1.5"
            },
            "emission": {
                "typeString": "float",
                "valueString": "0"
            },
            "emissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "opacity": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "caustics": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "internal_reflections": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "exit_to_background": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "indirect_diffuse": {
                "typeString": "float",
                "valueString": "1"
            },
            "indirect_specular": {
                "typeString": "float",
                "valueString": "1"
            },
            "aov_id1": {
                "typeString": "string",
                "valueString": ""
            },
            "id1": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id2": {
                "typeString": "string",
                "valueString": ""
            },
            "id2": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id3": {
                "typeString": "string",
                "valueString": ""
            },
            "id3": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id4": {
                "typeString": "string",
                "valueString": ""
            },
            "id4": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id5": {
                "typeString": "string",
                "valueString": ""
            },
            "id5": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id6": {
                "typeString": "string",
                "valueString": ""
            },
            "id6": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id7": {
                "typeString": "string",
                "valueString": ""
            },
            "id7": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id8": {
                "typeString": "string",
                "valueString": ""
            },
            "id8": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "hair": {
        "typeString": "closure",
        "attribute": {
            "rootcolor": {
                "typeString": "color3",
                "valueString": "0.1, 0.1, 0.1"
            },
            "tipcolor": {
                "typeString": "color3",
                "valueString": "0.5, 0.5, 0.5"
            },
            "opacity": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "ambdiff": {
                "typeString": "float",
                "valueString": "0.6"
            },
            "spec": {
                "typeString": "float",
                "valueString": "1"
            },
            "speccls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "spec_shift": {
                "typeString": "float",
                "valueString": "0"
            },
            "spec_gloss": {
                "typeString": "float",
                "valueString": "10"
            },
            "spec2": {
                "typeString": "float",
                "valueString": "0"
            },
            "spec2cls_color": {
                "typeString": "color3",
                "valueString": "1, 0.4, 0.1"
            },
            "spec2_shift": {
                "typeString": "float",
                "valueString": "0"
            },
            "spec2_gloss": {
                "typeString": "float",
                "valueString": "7"
            },
            "transmission": {
                "typeString": "float",
                "valueString": "0"
            },
            "transmissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 0.4, 0.1"
            },
            "transmission_spread": {
                "typeString": "float",
                "valueString": "1"
            },
            "kd_ind": {
                "typeString": "float",
                "valueString": "0"
            }
        }
    },
    "standard_hair": {
        "typeString": "closure",
        "attribute": {
            "base": {
                "typeString": "float",
                "valueString": "1"
            },
            "basecls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "melanin": {
                "typeString": "float",
                "valueString": "1"
            },
            "melanin_redness": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "melanin_randomize": {
                "typeString": "float",
                "valueString": "0"
            },
            "roughness": {
                "typeString": "float",
                "valueString": "0.2"
            },
            "roughness_azimuthal": {
                "typeString": "float",
                "valueString": "0.2"
            },
            "roughness_anisotropic": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "ior": {
                "typeString": "float",
                "valueString": "1.55"
            },
            "shift": {
                "typeString": "float",
                "valueString": "3"
            },
            "specular_tint": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular2_tint": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transmission_tint": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "diffuse": {
                "typeString": "float",
                "valueString": "0"
            },
            "diffusecls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "emission": {
                "typeString": "float",
                "valueString": "0"
            },
            "emissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "opacity": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "indirect_diffuse": {
                "typeString": "float",
                "valueString": "1"
            },
            "indirect_specular": {
                "typeString": "float",
                "valueString": "1"
            },
            "extra_depth": {
                "typeString": "integer",
                "valueString": "16"
            },
            "extra_samples": {
                "typeString": "integer",
                "valueString": "0"
            },
            "aov_id1": {
                "typeString": "string",
                "valueString": ""
            },
            "id1": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id2": {
                "typeString": "string",
                "valueString": ""
            },
            "id2": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id3": {
                "typeString": "string",
                "valueString": ""
            },
            "id3": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id4": {
                "typeString": "string",
                "valueString": ""
            },
            "id4": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id5": {
                "typeString": "string",
                "valueString": ""
            },
            "id5": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id6": {
                "typeString": "string",
                "valueString": ""
            },
            "id6": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id7": {
                "typeString": "string",
                "valueString": ""
            },
            "id7": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_id8": {
                "typeString": "string",
                "valueString": ""
            },
            "id8": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "car_paint": {
        "typeString": "closure",
        "attribute": {
            "base": {
                "typeString": "float",
                "valueString": "0.8"
            },
            "basecls_color": {
                "typeString": "color3",
                "valueString": "1, 0, 0"
            },
            "base_roughness": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "specular": {
                "typeString": "float",
                "valueString": "1"
            },
            "specularcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular_flip_flop": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular_light_facing": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular_falloff": {
                "typeString": "float",
                "valueString": "1"
            },
            "specular_roughness": {
                "typeString": "float",
                "valueString": "0.05"
            },
            "specular_IOR": {
                "typeString": "float",
                "valueString": "1.52"
            },
            "transmissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "flakecls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "flake_flip_flop": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "flake_light_facing": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "flake_falloff": {
                "typeString": "float",
                "valueString": "1"
            },
            "flake_roughness": {
                "typeString": "float",
                "valueString": "0.4"
            },
            "flake_IOR": {
                "typeString": "float",
                "valueString": "100"
            },
            "flake_scale": {
                "typeString": "float",
                "valueString": "0.001"
            },
            "flake_density": {
                "typeString": "float",
                "valueString": "0"
            },
            "flake_layers": {
                "typeString": "integer",
                "valueString": "1"
            },
            "flake_normal_randomize": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "flake_coord_space": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "pref_name": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "coat": {
                "typeString": "float",
                "valueString": "1"
            },
            "coatcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "coat_roughness": {
                "typeString": "float",
                "valueString": "0"
            },
            "coat_IOR": {
                "typeString": "float",
                "valueString": "1.5"
            },
            "coat_normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "bump2d": {
        "typeString": "vector3",
        "attribute": {
            "bump_map": {
                "typeString": "float",
                "valueString": "0"
            },
            "bump_height": {
                "typeString": "float",
                "valueString": "1"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "bump3d": {
        "typeString": "vector3",
        "attribute": {
            "bump_map": {
                "typeString": "float",
                "valueString": "0"
            },
            "bump_height": {
                "typeString": "float",
                "valueString": "1"
            },
            "epsilon": {
                "typeString": "float",
                "valueString": "1e-05"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "mix_shader": {
        "typeString": "closure",
        "attribute": {
            "mode": {
                "typeString": "string",
                "valueString": "blend"
            },
            "mix": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "shader1": {
                "typeString": "closure",
                "valueString": ""
            },
            "shader2": {
                "typeString": "closure",
                "valueString": ""
            }
        }
    },
    "sky": {
        "typeString": "closure",
        "attribute": {
            "color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "intensity": {
                "typeString": "float",
                "valueString": "1"
            },
            "visibility": {
                "typeString": "integer",
                "valueString": "-940211969"
            },
            "opaque_alpha": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "format": {
                "typeString": "string",
                "valueString": "angular"
            },
            "Xfnc_angle": {
                "typeString": "float",
                "valueString": "0"
            },
            "Yfnc_angle": {
                "typeString": "float",
                "valueString": "0"
            },
            "Zfnc_angle": {
                "typeString": "float",
                "valueString": "0"
            },
            "X": {
                "typeString": "vector3",
                "valueString": "1, 0, 0"
            },
            "Y": {
                "typeString": "vector3",
                "valueString": "0, 1, 0"
            },
            "Z": {
                "typeString": "vector3",
                "valueString": "0, 0, 1"
            }
        }
    },
    "physical_sky": {
        "typeString": "color4",
        "attribute": {
            "turbidity": {
                "typeString": "float",
                "valueString": "3"
            },
            "ground_albedo": {
                "typeString": "color3",
                "valueString": "0.1, 0.1, 0.1"
            },
            "use_degrees": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "elevation": {
                "typeString": "float",
                "valueString": "45"
            },
            "azimuth": {
                "typeString": "float",
                "valueString": "90"
            },
            "sun_direction": {
                "typeString": "vector3",
                "valueString": "0, 1, 0"
            },
            "enable_sun": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "sun_size": {
                "typeString": "float",
                "valueString": "0.51"
            },
            "sun_tint": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "sky_tint": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "intensity": {
                "typeString": "float",
                "valueString": "1"
            },
            "X": {
                "typeString": "vector3",
                "valueString": "1, 0, 0"
            },
            "Y": {
                "typeString": "vector3",
                "valueString": "0, 1, 0"
            },
            "Z": {
                "typeString": "vector3",
                "valueString": "0, 0, 1"
            }
        }
    },
    "atmosphere_volume": {
        "typeString": "closure",
        "attribute": {
            "density": {
                "typeString": "float",
                "valueString": "0"
            },
            "samples": {
                "typeString": "integer",
                "valueString": "5"
            },
            "eccentricity": {
                "typeString": "float",
                "valueString": "0"
            },
            "attenuation": {
                "typeString": "float",
                "valueString": "0"
            },
            "affect_camera": {
                "typeString": "float",
                "valueString": "1"
            },
            "affect_diffuse": {
                "typeString": "float",
                "valueString": "0"
            },
            "affect_specular": {
                "typeString": "float",
                "valueString": "1"
            },
            "rgb_density": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "rgb_attenuation": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "fog": {
        "typeString": "closure",
        "attribute": {
            "distance": {
                "typeString": "float",
                "valueString": "0.02"
            },
            "height": {
                "typeString": "float",
                "valueString": "5"
            },
            "color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "groundcls_point": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "ground_normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 1"
            }
        }
    },
    "standard_volume": {
        "typeString": "closure",
        "attribute": {
            "density": {
                "typeString": "float",
                "valueString": "1"
            },
            "density_channel": {
                "typeString": "string",
                "valueString": "density"
            },
            "scatter": {
                "typeString": "float",
                "valueString": "1"
            },
            "scattercls_color": {
                "typeString": "color3",
                "valueString": "0.5, 0.5, 0.5"
            },
            "scattercls_color_channel": {
                "typeString": "string",
                "valueString": ""
            },
            "scatter_anisotropy": {
                "typeString": "float",
                "valueString": "0"
            },
            "transparent": {
                "typeString": "color3",
                "valueString": "0.367879, 0.367879, 0.367879"
            },
            "transparent_depth": {
                "typeString": "float",
                "valueString": "1"
            },
            "transparent_channel": {
                "typeString": "string",
                "valueString": ""
            },
            "emission_mode": {
                "typeString": "string",
                "valueString": "blackbody"
            },
            "emission": {
                "typeString": "float",
                "valueString": "1"
            },
            "emissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "emission_channel": {
                "typeString": "string",
                "valueString": "heat"
            },
            "temperature": {
                "typeString": "float",
                "valueString": "1"
            },
            "temperature_channel": {
                "typeString": "string",
                "valueString": "temperature"
            },
            "blackbody_kelvin": {
                "typeString": "float",
                "valueString": "5000"
            },
            "blackbody_intensity": {
                "typeString": "float",
                "valueString": "1"
            },
            "displacement": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "interpolation": {
                "typeString": "string",
                "valueString": "trilinear"
            }
        }
    },
    "abs": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "add": {
        "typeString": "color3",
        "attribute": {
            "input1": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "input2": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "aov_read_float": {
        "typeString": "float",
        "attribute": {
            "aov_name": {
                "typeString": "string",
                "valueString": ""
            }
        }
    },
    "aov_read_int": {
        "typeString": "integer",
        "attribute": {
            "aov_name": {
                "typeString": "string",
                "valueString": ""
            }
        }
    },
    "aov_read_rgb": {
        "typeString": "color3",
        "attribute": {
            "aov_name": {
                "typeString": "string",
                "valueString": ""
            }
        }
    },
    "aov_read_rgba": {
        "typeString": "color4",
        "attribute": {
            "aov_name": {
                "typeString": "string",
                "valueString": ""
            }
        }
    },
    "aov_write_float": {
        "typeString": "closure",
        "attribute": {
            "passthrough": {
                "typeString": "closure",
                "valueString": ""
            },
            "aov_input": {
                "typeString": "float",
                "valueString": "0"
            },
            "aov_name": {
                "typeString": "string",
                "valueString": ""
            },
            "blend_opacity": {
                "typeString": "boolean",
                "valueString": "true"
            }
        }
    },
    "aov_write_int": {
        "typeString": "closure",
        "attribute": {
            "passthrough": {
                "typeString": "closure",
                "valueString": ""
            },
            "aov_input": {
                "typeString": "integer",
                "valueString": "0"
            },
            "aov_name": {
                "typeString": "string",
                "valueString": ""
            }
        }
    },
    "aov_write_rgb": {
        "typeString": "closure",
        "attribute": {
            "passthrough": {
                "typeString": "closure",
                "valueString": ""
            },
            "aov_input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "aov_name": {
                "typeString": "string",
                "valueString": ""
            },
            "blend_opacity": {
                "typeString": "boolean",
                "valueString": "true"
            }
        }
    },
    "aov_write_rgba": {
        "typeString": "closure",
        "attribute": {
            "passthrough": {
                "typeString": "closure",
                "valueString": ""
            },
            "aov_input": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "aov_name": {
                "typeString": "string",
                "valueString": ""
            },
            "blend_opacity": {
                "typeString": "boolean",
                "valueString": "true"
            }
        }
    },
    "atan": {
        "typeString": "color3",
        "attribute": {
            "y": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "x": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "units": {
                "typeString": "string",
                "valueString": "radians"
            }
        }
    },
    "blackbody": {
        "typeString": "color4",
        "attribute": {
            "temperature": {
                "typeString": "float",
                "valueString": "6500"
            },
            "normalize": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "intensity": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "cache": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "camera_projection": {
        "typeString": "color4",
        "attribute": {
            "projectioncls_color": {
                "typeString": "color4",
                "valueString": "1, 1, 1, 1"
            },
            "offscreencls_color": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mask": {
                "typeString": "float",
                "valueString": "1"
            },
            "camera": {
                "typeString": "string",
                "valueString": ""
            },
            "aspect_ratio": {
                "typeString": "float",
                "valueString": "1.333"
            },
            "front_facing": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "back_facing": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "use_shading_normal": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "coord_space": {
                "typeString": "string",
                "valueString": "world"
            },
            "pref_name": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "P": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "checkerboard": {
        "typeString": "color3",
        "attribute": {
            "color1": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "color2": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "u_frequency": {
                "typeString": "float",
                "valueString": "1"
            },
            "v_frequency": {
                "typeString": "float",
                "valueString": "1"
            },
            "u_offset": {
                "typeString": "float",
                "valueString": "0"
            },
            "v_offset": {
                "typeString": "float",
                "valueString": "0"
            },
            "contrast": {
                "typeString": "float",
                "valueString": "1"
            },
            "filter_strength": {
                "typeString": "float",
                "valueString": "1"
            },
            "filter_offset": {
                "typeString": "float",
                "valueString": "0"
            },
            "uvset": {
                "typeString": "string",
                "valueString": ""
            }
        }
    },
    "clamp": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "mode": {
                "typeString": "string",
                "valueString": "scalar"
            },
            "min": {
                "typeString": "float",
                "valueString": "0"
            },
            "max": {
                "typeString": "float",
                "valueString": "1"
            },
            "mincls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "maxcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "clip_geo": {
        "typeString": "closure",
        "attribute": {
            "intersection": {
                "typeString": "closure",
                "valueString": ""
            },
            "trace_set": {
                "typeString": "string",
                "valueString": ""
            },
            "inclusive": {
                "typeString": "boolean",
                "valueString": "true"
            }
        }
    },
    "color_convert": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "from": {
                "typeString": "string",
                "valueString": "RGB"
            },
            "to": {
                "typeString": "string",
                "valueString": "HSV"
            }
        }
    },
    "color_correct": {
        "typeString": "color4",
        "attribute": {
            "input": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "alpha_is_luminance": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "alpha_multiply": {
                "typeString": "float",
                "valueString": "1"
            },
            "alpha_add": {
                "typeString": "float",
                "valueString": "0"
            },
            "invert": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "invert_alpha": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "gamma": {
                "typeString": "float",
                "valueString": "1"
            },
            "hue_shift": {
                "typeString": "float",
                "valueString": "0"
            },
            "saturation": {
                "typeString": "float",
                "valueString": "1"
            },
            "contrast": {
                "typeString": "float",
                "valueString": "1"
            },
            "contrast_pivot": {
                "typeString": "float",
                "valueString": "0.18"
            },
            "exposure": {
                "typeString": "float",
                "valueString": "0"
            },
            "multiply": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "add": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "mask": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "color_jitter": {
        "typeString": "color4",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "data_input": {
                "typeString": "integer",
                "valueString": "0"
            },
            "data_gain_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "data_gain_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "data_hue_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "data_hue_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "data_saturation_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "data_saturation_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "data_seed": {
                "typeString": "integer",
                "valueString": "0"
            },
            "proc_gain_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "proc_gain_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "proc_hue_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "proc_hue_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "proc_saturation_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "proc_saturation_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "proc_seed": {
                "typeString": "integer",
                "valueString": "0"
            },
            "obj_gain_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "obj_gain_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "obj_hue_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "obj_hue_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "obj_saturation_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "obj_saturation_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "obj_seed": {
                "typeString": "integer",
                "valueString": "0"
            },
            "face_gain_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "face_gain_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "face_hue_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "face_hue_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "face_saturation_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "face_saturation_max": {
                "typeString": "float",
                "valueString": "0"
            },
            "face_seed": {
                "typeString": "integer",
                "valueString": "0"
            },
            "face_mode": {
                "typeString": "string",
                "valueString": "face id"
            }
        }
    },
    "compare": {
        "typeString": "boolean",
        "attribute": {
            "test": {
                "typeString": "string",
                "valueString": "=="
            },
            "input1": {
                "typeString": "float",
                "valueString": "0"
            },
            "input2": {
                "typeString": "float",
                "valueString": "0"
            }
        }
    },
    "complement": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "complex_ior": {
        "typeString": "color3",
        "attribute": {
            "material": {
                "typeString": "string",
                "valueString": "custom"
            },
            "mode": {
                "typeString": "string",
                "valueString": "artistic"
            },
            "reflectivity": {
                "typeString": "color3",
                "valueString": "0.925952, 0.720887, 0.504154"
            },
            "edgetint": {
                "typeString": "color3",
                "valueString": "0.995524, 0.957415, 0.822776"
            },
            "n": {
                "typeString": "vector3",
                "valueString": "0.27105, 0.67693, 1.3164"
            },
            "k": {
                "typeString": "vector3",
                "valueString": "3.6092, 2.6247, 2.2921"
            }
        }
    },
    "composite": {
        "typeString": "color4",
        "attribute": {
            "A": {
                "typeString": "color4",
                "valueString": "1, 0, 0, 1"
            },
            "B": {
                "typeString": "color4",
                "valueString": "0, 1, 0, 1"
            },
            "operation": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation": {
                "typeString": "string",
                "valueString": "same"
            }
        }
    },
    "cross": {
        "typeString": "vector3",
        "attribute": {
            "input1": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            "input2": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "curvature": {
        "typeString": "color3",
        "attribute": {
            "output": {
                "typeString": "string",
                "valueString": "convex"
            },
            "samples": {
                "typeString": "integer",
                "valueString": "3"
            },
            "radius": {
                "typeString": "float",
                "valueString": "0.1"
            },
            "spread": {
                "typeString": "float",
                "valueString": "1"
            },
            "threshold": {
                "typeString": "float",
                "valueString": "0"
            },
            "bias": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "multiply": {
                "typeString": "float",
                "valueString": "1"
            },
            "trace_set": {
                "typeString": "string",
                "valueString": ""
            },
            "inclusive": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "self_only": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "divide": {
        "typeString": "color3",
        "attribute": {
            "input1": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "input2": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "dot": {
        "typeString": "float",
        "attribute": {
            "input1": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            "input2": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "exp": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "facing_ratio": {
        "typeString": "float",
        "attribute": {
            "bias": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "gain": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "linear": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "invert": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "flakes": {
        "typeString": "color4",
        "attribute": {
            "scale": {
                "typeString": "float",
                "valueString": "0.1"
            },
            "density": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "step": {
                "typeString": "float",
                "valueString": "0"
            },
            "depth": {
                "typeString": "float",
                "valueString": "0"
            },
            "IOR": {
                "typeString": "float",
                "valueString": "1.52"
            },
            "normal_randomize": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "coord_space": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "pref_name": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "output_space": {
                "typeString": "string",
                "valueString": "world"
            }
        }
    },
    "float_to_int": {
        "typeString": "integer",
        "attribute": {
            "input": {
                "typeString": "float",
                "valueString": "0"
            },
            "mode": {
                "typeString": "string",
                "valueString": "round"
            }
        }
    },
    "float_to_matrix": {
        "typeString": "matrix44",
        "attribute": {
            "input_00": {
                "typeString": "float",
                "valueString": "1"
            },
            "input_01": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_02": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_03": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_10": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_11": {
                "typeString": "float",
                "valueString": "1"
            },
            "input_12": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_13": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_20": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_21": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_22": {
                "typeString": "float",
                "valueString": "1"
            },
            "input_23": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_30": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_31": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_32": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_33": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "float_to_rgba": {
        "typeString": "color4",
        "attribute": {
            "r": {
                "typeString": "float",
                "valueString": "0"
            },
            "g": {
                "typeString": "float",
                "valueString": "0"
            },
            "b": {
                "typeString": "float",
                "valueString": "0"
            },
            "a": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "float_to_rgb": {
        "typeString": "color3",
        "attribute": {
            "r": {
                "typeString": "float",
                "valueString": "0"
            },
            "g": {
                "typeString": "float",
                "valueString": "0"
            },
            "b": {
                "typeString": "float",
                "valueString": "0"
            }
        }
    },
    "fraction": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "is_finite": {
        "typeString": "boolean",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "layer_float": {
        "typeString": "float",
        "attribute": {
            "enable1": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name1": {
                "typeString": "string",
                "valueString": "layer1"
            },
            "input1": {
                "typeString": "float",
                "valueString": "0"
            },
            "mix1": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable2": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name2": {
                "typeString": "string",
                "valueString": "layer2"
            },
            "input2": {
                "typeString": "float",
                "valueString": "0"
            },
            "mix2": {
                "typeString": "float",
                "valueString": "0"
            },
            "enable3": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name3": {
                "typeString": "string",
                "valueString": "layer3"
            },
            "input3": {
                "typeString": "float",
                "valueString": "0"
            },
            "mix3": {
                "typeString": "float",
                "valueString": "0"
            },
            "enable4": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name4": {
                "typeString": "string",
                "valueString": "layer4"
            },
            "input4": {
                "typeString": "float",
                "valueString": "0"
            },
            "mix4": {
                "typeString": "float",
                "valueString": "0"
            },
            "enable5": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name5": {
                "typeString": "string",
                "valueString": "layer5"
            },
            "input5": {
                "typeString": "float",
                "valueString": "0"
            },
            "mix5": {
                "typeString": "float",
                "valueString": "0"
            },
            "enable6": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name6": {
                "typeString": "string",
                "valueString": "layer6"
            },
            "input6": {
                "typeString": "float",
                "valueString": "0"
            },
            "mix6": {
                "typeString": "float",
                "valueString": "0"
            },
            "enable7": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name7": {
                "typeString": "string",
                "valueString": "layer7"
            },
            "input7": {
                "typeString": "float",
                "valueString": "0"
            },
            "mix7": {
                "typeString": "float",
                "valueString": "0"
            },
            "enable8": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name8": {
                "typeString": "string",
                "valueString": "layer8"
            },
            "input8": {
                "typeString": "float",
                "valueString": "0"
            },
            "mix8": {
                "typeString": "float",
                "valueString": "0"
            }
        }
    },
    "layer_rgba": {
        "typeString": "color4",
        "attribute": {
            "enable1": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name1": {
                "typeString": "string",
                "valueString": "layer1"
            },
            "input1": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mix1": {
                "typeString": "float",
                "valueString": "1"
            },
            "operation1": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation1": {
                "typeString": "string",
                "valueString": "result"
            },
            "enable2": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name2": {
                "typeString": "string",
                "valueString": "layer2"
            },
            "input2": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mix2": {
                "typeString": "float",
                "valueString": "1"
            },
            "operation2": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation2": {
                "typeString": "string",
                "valueString": "result"
            },
            "enable3": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name3": {
                "typeString": "string",
                "valueString": "layer3"
            },
            "input3": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mix3": {
                "typeString": "float",
                "valueString": "1"
            },
            "operation3": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation3": {
                "typeString": "string",
                "valueString": "result"
            },
            "enable4": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name4": {
                "typeString": "string",
                "valueString": "layer4"
            },
            "input4": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mix4": {
                "typeString": "float",
                "valueString": "1"
            },
            "operation4": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation4": {
                "typeString": "string",
                "valueString": "result"
            },
            "enable5": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name5": {
                "typeString": "string",
                "valueString": "layer5"
            },
            "input5": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mix5": {
                "typeString": "float",
                "valueString": "1"
            },
            "operation5": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation5": {
                "typeString": "string",
                "valueString": "result"
            },
            "enable6": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name6": {
                "typeString": "string",
                "valueString": "layer6"
            },
            "input6": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mix6": {
                "typeString": "float",
                "valueString": "1"
            },
            "operation6": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation6": {
                "typeString": "string",
                "valueString": "result"
            },
            "enable7": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name7": {
                "typeString": "string",
                "valueString": "layer7"
            },
            "input7": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mix7": {
                "typeString": "float",
                "valueString": "1"
            },
            "operation7": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation7": {
                "typeString": "string",
                "valueString": "result"
            },
            "enable8": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name8": {
                "typeString": "string",
                "valueString": "layer8"
            },
            "input8": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "mix8": {
                "typeString": "float",
                "valueString": "1"
            },
            "operation8": {
                "typeString": "string",
                "valueString": "over"
            },
            "alpha_operation8": {
                "typeString": "string",
                "valueString": "result"
            },
            "clamp": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "layer_shader": {
        "typeString": "closure",
        "attribute": {
            "enable1": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name1": {
                "typeString": "string",
                "valueString": "layer1"
            },
            "input1": {
                "typeString": "closure",
                "valueString": ""
            },
            "mix1": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable2": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name2": {
                "typeString": "string",
                "valueString": "layer2"
            },
            "input2": {
                "typeString": "closure",
                "valueString": ""
            },
            "mix2": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable3": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name3": {
                "typeString": "string",
                "valueString": "layer3"
            },
            "input3": {
                "typeString": "closure",
                "valueString": ""
            },
            "mix3": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable4": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name4": {
                "typeString": "string",
                "valueString": "layer4"
            },
            "input4": {
                "typeString": "closure",
                "valueString": ""
            },
            "mix4": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable5": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name5": {
                "typeString": "string",
                "valueString": "layer5"
            },
            "input5": {
                "typeString": "closure",
                "valueString": ""
            },
            "mix5": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable6": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name6": {
                "typeString": "string",
                "valueString": "layer6"
            },
            "input6": {
                "typeString": "closure",
                "valueString": ""
            },
            "mix6": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable7": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name7": {
                "typeString": "string",
                "valueString": "layer7"
            },
            "input7": {
                "typeString": "closure",
                "valueString": ""
            },
            "mix7": {
                "typeString": "float",
                "valueString": "1"
            },
            "enable8": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "name8": {
                "typeString": "string",
                "valueString": "layer8"
            },
            "input8": {
                "typeString": "closure",
                "valueString": ""
            },
            "mix8": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "length": {
        "typeString": "float",
        "attribute": {
            "input": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "mode": {
                "typeString": "string",
                "valueString": "euclidian"
            }
        }
    },
    "log": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "base": {
                "typeString": "color3",
                "valueString": "2.71828, 2.71828, 2.71828"
            }
        }
    },
    "matrix_interpolate": {
        "typeString": "matrix44",
        "attribute": {
            "type": {
                "typeString": "string",
                "valueString": "time"
            },
            "value": {
                "typeString": "float",
                "valueString": "0.5"
            }
        }
    },
    "matrix_multiply_vector": {
        "typeString": "vector3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "type": {
                "typeString": "string",
                "valueString": "point"
            },
            "matrix": {
                "typeString": "matrix44",
                "valueString": ""
            }
        }
    },
    "matrix_transform": {
        "typeString": "matrix44",
        "attribute": {
            "transform_order": {
                "typeString": "string",
                "valueString": "srt"
            },
            "rotation_type": {
                "typeString": "string",
                "valueString": "euler"
            },
            "units": {
                "typeString": "string",
                "valueString": "degrees"
            },
            "rotation_order": {
                "typeString": "string",
                "valueString": "xyz"
            },
            "rotation": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "axis": {
                "typeString": "vector3",
                "valueString": "1, 0, 0"
            },
            "angle": {
                "typeString": "float",
                "valueString": "0"
            },
            "translate": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "scale": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            "pivot": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "matte": {
        "typeString": "closure",
        "attribute": {
            "passthrough": {
                "typeString": "closure",
                "valueString": ""
            },
            "color": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "opacity": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "max": {
        "typeString": "color3",
        "attribute": {
            "input1": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "input2": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "min": {
        "typeString": "color3",
        "attribute": {
            "input1": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "input2": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "mix_rgba": {
        "typeString": "color4",
        "attribute": {
            "input1": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input2": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "mix": {
                "typeString": "float",
                "valueString": "0.5"
            }
        }
    },
    "modulo": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "divisor": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "multiply": {
        "typeString": "color3",
        "attribute": {
            "input1": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "input2": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "negate": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "normalize": {
        "typeString": "vector3",
        "attribute": {
            "input": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "normal_map": {
        "typeString": "vector3",
        "attribute": {
            "input": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "tangent": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "order": {
                "typeString": "string",
                "valueString": "XYZ"
            },
            "invert_x": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "invert_y": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "invert_z": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "color_to_signed": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "tangent_space": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "strength": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "passthrough": {
        "typeString": "closure",
        "attribute": {
            "passthrough": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval1": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval2": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval3": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval4": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval5": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval6": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval7": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval8": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval9": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval10": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval11": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval12": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval13": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval14": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval15": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval16": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval17": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval18": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval19": {
                "typeString": "closure",
                "valueString": ""
            },
            "eval20": {
                "typeString": "closure",
                "valueString": ""
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "pow": {
        "typeString": "color3",
        "attribute": {
            "base": {
                "typeString": "color3",
                "valueString": "2.71828, 2.71828, 2.71828"
            },
            "exponent": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "query_shape": {
        "typeString": "boolean",
        "attribute": {}
    },
    "ramp_float": {
        "typeString": "float",
        "attribute": {
            "type": {
                "typeString": "string",
                "valueString": "custom"
            },
            "input": {
                "typeString": "float",
                "valueString": "0"
            },
            "position": {
                "typeString": "floatarray",
                "valueString": "0.0, 1.0"
            },
            "value": {
                "typeString": "floatarray",
                "valueString": "0.0, 1.0"
            },
            "interpolation": {
                "typeString": "integerarray",
                "valueString": "2, 2"
            },
            "uvset": {
                "typeString": "string",
                "valueString": ""
            },
            "use_implicit_uvs": {
                "typeString": "string",
                "valueString": "off"
            },
            "wrap_uvs": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "ramp_rgb": {
        "typeString": "color3",
        "attribute": {
            "type": {
                "typeString": "string",
                "valueString": "custom"
            },
            "input": {
                "typeString": "float",
                "valueString": "0"
            },
            "position": {
                "typeString": "floatarray",
                "valueString": "0.0, 1.0"
            },
            "color": {
                "typeString": "floatarray",
                "valueString": "0.0, 0.0, 0.0, 1.0, 1.0, 1.0"
            },
            "interpolation": {
                "typeString": "integerarray",
                "valueString": "2, 2"
            },
            "uvset": {
                "typeString": "string",
                "valueString": ""
            },
            "use_implicit_uvs": {
                "typeString": "string",
                "valueString": "off"
            },
            "wrap_uvs": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "random": {
        "typeString": "color3",
        "attribute": {
            "input_type": {
                "typeString": "string",
                "valueString": "int"
            },
            "input_int": {
                "typeString": "integer",
                "valueString": "0"
            },
            "input_float": {
                "typeString": "float",
                "valueString": "0"
            },
            "inputcls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "seed": {
                "typeString": "integer",
                "valueString": "0"
            },
            "grayscale": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "range": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "input_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_max": {
                "typeString": "float",
                "valueString": "1"
            },
            "output_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "output_max": {
                "typeString": "float",
                "valueString": "1"
            },
            "smoothstep": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "contrast": {
                "typeString": "float",
                "valueString": "1"
            },
            "contrast_pivot": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "bias": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "gain": {
                "typeString": "float",
                "valueString": "0.5"
            }
        }
    },
    "reciprocal": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            }
        }
    },
    "rgba_to_float": {
        "typeString": "float",
        "attribute": {
            "input": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "mode": {
                "typeString": "string",
                "valueString": "average"
            }
        }
    },
    "rgb_to_float": {
        "typeString": "float",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "mode": {
                "typeString": "string",
                "valueString": "average"
            }
        }
    },
    "rgb_to_vector": {
        "typeString": "vector3",
        "attribute": {
            "input": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "mode": {
                "typeString": "string",
                "valueString": "raw"
            }
        }
    },
    "shadow_matte": {
        "typeString": "color4",
        "attribute": {
            "background": {
                "typeString": "string",
                "valueString": "scene_background"
            },
            "shadowcls_color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "shadow_opacity": {
                "typeString": "float",
                "valueString": "1"
            },
            "backgroundcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "diffusecls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "diffuse_use_background": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "diffuse_intensity": {
                "typeString": "float",
                "valueString": "0.7"
            },
            "backlighting": {
                "typeString": "float",
                "valueString": "0"
            },
            "indirect_diffuse_enable": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "indirect_specular_enable": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "specularcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular_intensity": {
                "typeString": "float",
                "valueString": "1"
            },
            "specular_roughness": {
                "typeString": "float",
                "valueString": "0.2"
            },
            "specular_IOR": {
                "typeString": "float",
                "valueString": "1.5"
            },
            "alpha_mask": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "aov_group": {
                "typeString": "string",
                "valueString": ""
            },
            "aov_shadow": {
                "typeString": "string",
                "valueString": "shadow"
            },
            "aov_shadow_diff": {
                "typeString": "string",
                "valueString": "shadow_diff"
            },
            "aov_shadow_mask": {
                "typeString": "string",
                "valueString": "shadow_mask"
            }
        }
    },
    "shuffle": {
        "typeString": "color4",
        "attribute": {
            "color": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "alpha": {
                "typeString": "float",
                "valueString": "1"
            },
            "channel_r": {
                "typeString": "string",
                "valueString": "R"
            },
            "channel_g": {
                "typeString": "string",
                "valueString": "G"
            },
            "channel_b": {
                "typeString": "string",
                "valueString": "B"
            },
            "channel_a": {
                "typeString": "string",
                "valueString": "A"
            },
            "negate_r": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "negate_g": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "negate_b": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "negate_a": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "sign": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "skin": {
        "typeString": "closure",
        "attribute": {
            "sss_weight": {
                "typeString": "float",
                "valueString": "1"
            },
            "shallow_scattercls_color": {
                "typeString": "color3",
                "valueString": "1, 0.909, 0.769"
            },
            "shallow_scatter_weight": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "shallow_scatter_radius": {
                "typeString": "float",
                "valueString": "0.15"
            },
            "mid_scattercls_color": {
                "typeString": "color3",
                "valueString": "0.949, 0.714, 0.56"
            },
            "mid_scatter_weight": {
                "typeString": "float",
                "valueString": "0.25"
            },
            "mid_scatter_radius": {
                "typeString": "float",
                "valueString": "0.25"
            },
            "deep_scattercls_color": {
                "typeString": "color3",
                "valueString": "0.7, 0.1, 0.1"
            },
            "deep_scatter_weight": {
                "typeString": "float",
                "valueString": "1"
            },
            "deep_scatter_radius": {
                "typeString": "float",
                "valueString": "0.6"
            },
            "specularcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "specular_weight": {
                "typeString": "float",
                "valueString": "0.8"
            },
            "specular_roughness": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "specular_ior": {
                "typeString": "float",
                "valueString": "1.44"
            },
            "sheencls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "sheen_weight": {
                "typeString": "float",
                "valueString": "0"
            },
            "sheen_roughness": {
                "typeString": "float",
                "valueString": "0.35"
            },
            "sheen_ior": {
                "typeString": "float",
                "valueString": "1.44"
            },
            "global_sss_radius_multiplier": {
                "typeString": "float",
                "valueString": "1"
            },
            "specular_in_secondary_rays": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "fresnel_affect_sss": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "opacity": {
                "typeString": "float",
                "valueString": "1"
            },
            "opacitycls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 1, 0"
            }
        }
    },
    "space_transform": {
        "typeString": "vector3",
        "attribute": {
            "input": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "type": {
                "typeString": "string",
                "valueString": "point"
            },
            "from": {
                "typeString": "string",
                "valueString": "world"
            },
            "to": {
                "typeString": "string",
                "valueString": "world"
            },
            "tangent": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "normalize": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "scale": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "sqrt": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "state_float": {
        "typeString": "float",
        "attribute": {
            "variable": {
                "typeString": "string",
                "valueString": "sx"
            }
        }
    },
    "state_int": {
        "typeString": "integer",
        "attribute": {
            "variable": {
                "typeString": "string",
                "valueString": "x"
            }
        }
    },
    "state_vector": {
        "typeString": "vector3",
        "attribute": {
            "variable": {
                "typeString": "string",
                "valueString": "Ro"
            }
        }
    },
    "subtract": {
        "typeString": "color3",
        "attribute": {
            "input1": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "input2": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "switch_rgba": {
        "typeString": "color4",
        "attribute": {
            "index": {
                "typeString": "integer",
                "valueString": "0"
            },
            "input0": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input1": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input2": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input3": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input4": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input5": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input6": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input7": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input8": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input9": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input10": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input11": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input12": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input13": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input14": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input15": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input16": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input17": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input18": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "input19": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            }
        }
    },
    "switch_shader": {
        "typeString": "closure",
        "attribute": {
            "index": {
                "typeString": "integer",
                "valueString": "0"
            },
            "input0": {
                "typeString": "closure",
                "valueString": ""
            },
            "input1": {
                "typeString": "closure",
                "valueString": ""
            },
            "input2": {
                "typeString": "closure",
                "valueString": ""
            },
            "input3": {
                "typeString": "closure",
                "valueString": ""
            },
            "input4": {
                "typeString": "closure",
                "valueString": ""
            },
            "input5": {
                "typeString": "closure",
                "valueString": ""
            },
            "input6": {
                "typeString": "closure",
                "valueString": ""
            },
            "input7": {
                "typeString": "closure",
                "valueString": ""
            },
            "input8": {
                "typeString": "closure",
                "valueString": ""
            },
            "input9": {
                "typeString": "closure",
                "valueString": ""
            },
            "input10": {
                "typeString": "closure",
                "valueString": ""
            },
            "input11": {
                "typeString": "closure",
                "valueString": ""
            },
            "input12": {
                "typeString": "closure",
                "valueString": ""
            },
            "input13": {
                "typeString": "closure",
                "valueString": ""
            },
            "input14": {
                "typeString": "closure",
                "valueString": ""
            },
            "input15": {
                "typeString": "closure",
                "valueString": ""
            },
            "input16": {
                "typeString": "closure",
                "valueString": ""
            },
            "input17": {
                "typeString": "closure",
                "valueString": ""
            },
            "input18": {
                "typeString": "closure",
                "valueString": ""
            },
            "input19": {
                "typeString": "closure",
                "valueString": ""
            }
        }
    },
    "thin_film": {
        "typeString": "color3",
        "attribute": {
            "thickness_min": {
                "typeString": "float",
                "valueString": "250"
            },
            "thickness_max": {
                "typeString": "float",
                "valueString": "400"
            },
            "thickness": {
                "typeString": "float",
                "valueString": "0"
            },
            "ior_medium": {
                "typeString": "float",
                "valueString": "1"
            },
            "ior_film": {
                "typeString": "float",
                "valueString": "1.5"
            },
            "ior_internal": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "trace_set": {
        "typeString": "closure",
        "attribute": {
            "passthrough": {
                "typeString": "closure",
                "valueString": ""
            },
            "trace_set": {
                "typeString": "string",
                "valueString": ""
            },
            "inclusive": {
                "typeString": "boolean",
                "valueString": "true"
            }
        }
    },
    "trigo": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "function": {
                "typeString": "string",
                "valueString": "cos"
            },
            "units": {
                "typeString": "string",
                "valueString": "radians"
            },
            "frequency": {
                "typeString": "float",
                "valueString": "1"
            },
            "phase": {
                "typeString": "float",
                "valueString": "0"
            }
        }
    },
    "triplanar": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "scale": {
                "typeString": "vector3",
                "valueString": "1, 1, 1"
            },
            "rotate": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "offset": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "coord_space": {
                "typeString": "string",
                "valueString": "object"
            },
            "pref_name": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "blend": {
                "typeString": "float",
                "valueString": "0"
            },
            "cell": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "cell_rotate": {
                "typeString": "float",
                "valueString": "0"
            },
            "cell_blend": {
                "typeString": "float",
                "valueString": "0.1"
            }
        }
    },
    "two_sided": {
        "typeString": "closure",
        "attribute": {
            "front": {
                "typeString": "closure",
                "valueString": ""
            },
            "back": {
                "typeString": "closure",
                "valueString": ""
            }
        }
    },
    "user_data_float": {
        "typeString": "float",
        "attribute": {
            "attribute": {
                "typeString": "string",
                "valueString": ""
            },
            "default": {
                "typeString": "float",
                "valueString": "0"
            }
        }
    },
    "user_data_int": {
        "typeString": "integer",
        "attribute": {
            "attribute": {
                "typeString": "string",
                "valueString": ""
            },
            "default": {
                "typeString": "integer",
                "valueString": "0"
            }
        }
    },
    "user_data_rgba": {
        "typeString": "color4",
        "attribute": {
            "attribute": {
                "typeString": "string",
                "valueString": ""
            },
            "default": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            }
        }
    },
    "user_data_rgb": {
        "typeString": "color3",
        "attribute": {
            "attribute": {
                "typeString": "string",
                "valueString": ""
            },
            "default": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            }
        }
    },
    "user_data_string": {
        "typeString": "string",
        "attribute": {
            "attribute": {
                "typeString": "string",
                "valueString": ""
            },
            "default": {
                "typeString": "string",
                "valueString": ""
            }
        }
    },
    "uv_transform": {
        "typeString": "color4",
        "attribute": {
            "passthrough": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "unit": {
                "typeString": "string",
                "valueString": "degrees"
            },
            "uvset": {
                "typeString": "string",
                "valueString": ""
            },
            "coverage": {
                "typeString": "vector2",
                "valueString": "1, 1"
            },
            "scale_frame": {
                "typeString": "vector2",
                "valueString": "1, 1"
            },
            "translate_frame": {
                "typeString": "vector2",
                "valueString": "0, 0"
            },
            "rotate_frame": {
                "typeString": "float",
                "valueString": "0"
            },
            "pivot_frame": {
                "typeString": "vector2",
                "valueString": "0.5, 0.5"
            },
            "wrap_frame_u": {
                "typeString": "string",
                "valueString": "periodic"
            },
            "wrap_frame_v": {
                "typeString": "string",
                "valueString": "periodic"
            },
            "wrap_framecls_color": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "repeat": {
                "typeString": "vector2",
                "valueString": "1, 1"
            },
            "offset": {
                "typeString": "vector2",
                "valueString": "0, 0"
            },
            "rotate": {
                "typeString": "float",
                "valueString": "0"
            },
            "pivot": {
                "typeString": "vector2",
                "valueString": "0.5, 0.5"
            },
            "noise": {
                "typeString": "vector2",
                "valueString": "0, 0"
            },
            "mirror_u": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "mirror_v": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "flip_u": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "flip_v": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "swap_uv": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "stagger": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "uv_projection": {
        "typeString": "color4",
        "attribute": {
            "projectioncls_color": {
                "typeString": "color4",
                "valueString": "1, 1, 1, 1"
            },
            "projection_type": {
                "typeString": "string",
                "valueString": "planar"
            },
            "coord_space": {
                "typeString": "string",
                "valueString": "world"
            },
            "pref_name": {
                "typeString": "string",
                "valueString": "Pref"
            },
            "P": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "ufnc_angle": {
                "typeString": "float",
                "valueString": "180"
            },
            "vfnc_angle": {
                "typeString": "float",
                "valueString": "90"
            },
            "clamp": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "defaultcls_color": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 0"
            },
            "matrix": {
                "typeString": "matrix44",
                "valueString": ""
            }
        }
    },
    "vector_map": {
        "typeString": "vector3",
        "attribute": {
            "input": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "tangent": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "normal": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "order": {
                "typeString": "string",
                "valueString": "XYZ"
            },
            "invert_x": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "invert_y": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "invert_z": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "color_to_signed": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "tangent_space": {
                "typeString": "boolean",
                "valueString": "true"
            },
            "scale": {
                "typeString": "float",
                "valueString": "1"
            }
        }
    },
    "vector_to_rgb": {
        "typeString": "color3",
        "attribute": {
            "input": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "mode": {
                "typeString": "string",
                "valueString": "raw"
            }
        }
    },
    "volume_collector": {
        "typeString": "closure",
        "attribute": {
            "scattering_source": {
                "typeString": "string",
                "valueString": "parameter"
            },
            "scattering": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "scattering_channel": {
                "typeString": "string",
                "valueString": ""
            },
            "scatteringcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "scattering_intensity": {
                "typeString": "float",
                "valueString": "1"
            },
            "anisotropy": {
                "typeString": "float",
                "valueString": "0"
            },
            "attenuation_source": {
                "typeString": "string",
                "valueString": "parameter"
            },
            "attenuation": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "attenuation_channel": {
                "typeString": "string",
                "valueString": ""
            },
            "attenuationcls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "attenuation_intensity": {
                "typeString": "float",
                "valueString": "1"
            },
            "attenuation_mode": {
                "typeString": "string",
                "valueString": "absorption"
            },
            "emission_source": {
                "typeString": "string",
                "valueString": "parameter"
            },
            "emission": {
                "typeString": "color3",
                "valueString": "0, 0, 0"
            },
            "emission_channel": {
                "typeString": "string",
                "valueString": ""
            },
            "emissioncls_color": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "emission_intensity": {
                "typeString": "float",
                "valueString": "1"
            },
            "position_offset": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "interpolation": {
                "typeString": "string",
                "valueString": "trilinear"
            }
        }
    },
    "volume_sample_float": {
        "typeString": "float",
        "attribute": {
            "channel": {
                "typeString": "string",
                "valueString": ""
            },
            "position_offset": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "interpolation": {
                "typeString": "string",
                "valueString": "trilinear"
            },
            "volume_type": {
                "typeString": "string",
                "valueString": "fog"
            },
            "sdf_offset": {
                "typeString": "float",
                "valueString": "0"
            },
            "sdf_blend": {
                "typeString": "float",
                "valueString": "0"
            },
            "sdf_invert": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "input_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "input_max": {
                "typeString": "float",
                "valueString": "1"
            },
            "contrast": {
                "typeString": "float",
                "valueString": "1"
            },
            "contrast_pivot": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "bias": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "gain": {
                "typeString": "float",
                "valueString": "0.5"
            },
            "output_min": {
                "typeString": "float",
                "valueString": "0"
            },
            "output_max": {
                "typeString": "float",
                "valueString": "1"
            },
            "clamp_min": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "clamp_max": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    },
    "volume_sample_rgb": {
        "typeString": "color3",
        "attribute": {
            "channel": {
                "typeString": "string",
                "valueString": ""
            },
            "position_offset": {
                "typeString": "vector3",
                "valueString": "0, 0, 0"
            },
            "interpolation": {
                "typeString": "string",
                "valueString": "trilinear"
            },
            "gamma": {
                "typeString": "float",
                "valueString": "1"
            },
            "hue_shift": {
                "typeString": "float",
                "valueString": "0"
            },
            "saturation": {
                "typeString": "float",
                "valueString": "1"
            },
            "contrast": {
                "typeString": "float",
                "valueString": "1"
            },
            "contrast_pivot": {
                "typeString": "float",
                "valueString": "0.18"
            },
            "exposure": {
                "typeString": "float",
                "valueString": "0"
            },
            "multiply": {
                "typeString": "float",
                "valueString": "1"
            },
            "add": {
                "typeString": "float",
                "valueString": "0"
            }
        }
    },
    "c4d_texture_tag": {
        "typeString": "closure",
        "attribute": {
            "color": {
                "typeString": "closure",
                "valueString": ""
            },
            "proj": {
                "typeString": "string",
                "valueString": "spherical"
            },
            "lenx": {
                "typeString": "float",
                "valueString": "1"
            },
            "leny": {
                "typeString": "float",
                "valueString": "1"
            },
            "ox": {
                "typeString": "float",
                "valueString": "0"
            },
            "oy": {
                "typeString": "float",
                "valueString": "0"
            },
            "tilex": {
                "typeString": "float",
                "valueString": "0"
            },
            "tiley": {
                "typeString": "float",
                "valueString": "0"
            },
            "m": {
                "typeString": "matrix44",
                "valueString": ""
            },
            "camera": {
                "typeString": "string",
                "valueString": ""
            },
            "aspect_ratio": {
                "typeString": "float",
                "valueString": "1.33333"
            },
            "use_pref": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "side": {
                "typeString": "integer",
                "valueString": "0"
            }
        }
    },
    "c4d_texture_tag_rgba": {
        "typeString": "color4",
        "attribute": {
            "color": {
                "typeString": "color4",
                "valueString": "0, 0, 0, 1"
            },
            "proj": {
                "typeString": "string",
                "valueString": "spherical"
            },
            "lenx": {
                "typeString": "float",
                "valueString": "1"
            },
            "leny": {
                "typeString": "float",
                "valueString": "1"
            },
            "ox": {
                "typeString": "float",
                "valueString": "0"
            },
            "oy": {
                "typeString": "float",
                "valueString": "0"
            },
            "tilex": {
                "typeString": "float",
                "valueString": "0"
            },
            "tiley": {
                "typeString": "float",
                "valueString": "0"
            },
            "m": {
                "typeString": "matrix44",
                "valueString": ""
            },
            "camera": {
                "typeString": "string",
                "valueString": ""
            },
            "aspect_ratio": {
                "typeString": "float",
                "valueString": "1.33333"
            },
            "use_pref": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "side": {
                "typeString": "integer",
                "valueString": "0"
            }
        }
    },
    "maya_layered_shader": {
        "typeString": "closure",
        "attribute": {
            "compositingFlag": {
                "typeString": "string",
                "valueString": "shader"
            },
            "numInputs": {
                "typeString": "integer",
                "valueString": "0"
            },
            "color0": {
                "typeString": "closure",
                "valueString": ""
            },
            "color1": {
                "typeString": "closure",
                "valueString": ""
            },
            "color2": {
                "typeString": "closure",
                "valueString": ""
            },
            "color3": {
                "typeString": "closure",
                "valueString": ""
            },
            "color4": {
                "typeString": "closure",
                "valueString": ""
            },
            "color5": {
                "typeString": "closure",
                "valueString": ""
            },
            "color6": {
                "typeString": "closure",
                "valueString": ""
            },
            "color7": {
                "typeString": "closure",
                "valueString": ""
            },
            "color8": {
                "typeString": "closure",
                "valueString": ""
            },
            "color9": {
                "typeString": "closure",
                "valueString": ""
            },
            "color10": {
                "typeString": "closure",
                "valueString": ""
            },
            "color11": {
                "typeString": "closure",
                "valueString": ""
            },
            "color12": {
                "typeString": "closure",
                "valueString": ""
            },
            "color13": {
                "typeString": "closure",
                "valueString": ""
            },
            "color14": {
                "typeString": "closure",
                "valueString": ""
            },
            "color15": {
                "typeString": "closure",
                "valueString": ""
            },
            "transparency0": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency1": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency2": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency3": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency4": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency5": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency6": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency7": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency8": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency9": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency10": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency11": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency12": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency13": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency14": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "transparency15": {
                "typeString": "color3",
                "valueString": "1, 1, 1"
            },
            "useTransparency0": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency1": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency2": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency3": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency4": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency5": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency6": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency7": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency8": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency9": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency10": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency11": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency12": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency13": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency14": {
                "typeString": "boolean",
                "valueString": "false"
            },
            "useTransparency15": {
                "typeString": "boolean",
                "valueString": "false"
            }
        }
    }
}
