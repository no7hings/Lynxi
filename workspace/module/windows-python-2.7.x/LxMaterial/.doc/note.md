
# maya node category

## in maya and not in materialx
```json
[
    "aiAOV",
    "aiAOVDriver",
    "aiAOVFilter",
    "aiAreaLight",
    "aiBarndoor",
    "aiCollection",
    "aiColorToFloat",
    "aiCurveCollector",
    "aiDisable",
    "aiGobo",
    "aiIncludeGraph",
    "aiLightBlocker",
    "aiLightDecay",
    "aiLightPortal",
    "aiMaterialx",
    "aiMerge",
    "aiMeshLight",
    "aiOptions",
    "aiOslShader",
    "aiPhotometricLight",
    "aiRaySwitch",
    "aiReadFloat",
    "aiReadInt",
    "aiReadRGB",
    "aiReadRGBA",
    "aiSetParameter",
    "aiSetTransform",
    "aiSkyDomeLight",
    "aiStandIn",
    "aiSwitch",
    "aiSwitchOperator",
    "aiUserDataBool",
    "aiUserDataColor",
    "aiUserDataVec2",
    "aiUserDataVector",
    "aiViewRegion",
    "aiVolume",
    "aiWriteColor",
    "aiWriteFloat",
    "aiWriteInt",
    "aiWriteRgba",
    "aimConstraint",
    "airField",
    "airManip"
]
```

## in materialx and not in maya
```json
[
    "aiRaySwitchShader",
    "aiAovReadInt",
    "aiLambert",
    "aiAovWriteRgb",
    "aiUserDataRgb",
    "aiRgbToVector",
    "aiUserDataRgba",
    "aiAovWriteRgba",
    "aiFloatToMatrix",
    "aiMixRgba",
    "aiMayaLayeredShader",
    "aiQueryShape",
    "aiC4dTextureTagRgba",
    "aiAovWriteInt",
    "aiAovReadRgba",
    "aiRgbToFloat",
    "aiVectorToRgb",
    "aiAovReadFloat",
    "aiSwitchShader",
    "aiAovReadRgb",
    "aiSwitchRgba",
    "aiAovWriteFloat",
    "aiRaySwitchRgba",
    "aiC4dTextureTag",
    "aiFloatToRgb",
    "aiCheckerboard"
]
```

## port constant
```
aiSky1 sky opaque_alpha aiSky opaqueAlpha
aiSky1 sky X_angle aiSky XAngle
aiSky1 sky Y_angle aiSky YAngle
aiSky1 sky Z_angle aiSky ZAngle
aiSky1 sky X aiSky X
aiSky1 sky Y aiSky Y
aiSky1 sky Z aiSky Z
aiStandard1 standard Kd_color aiStandard KdColor
aiStandardSurface1 standard_surface normal aiStandardSurface normal
aiStandardSurface1 standard_surface coat_affect_color aiStandardSurface coatAffectColor
aiStandardSurface1 standard_surface coat_affect_roughness aiStandardSurface coatAffectRoughness
aiUvProjection1 uv_projection matrix aiUvProjection matrix
aiRampFloat1 ramp_float position aiRampFloat position
aiRampFloat1 ramp_float value aiRampFloat value
aiRampFloat1 ramp_float interpolation aiRampFloat interpolation
aiRampRgb1 ramp_rgb position aiRampRgb position
aiRampRgb1 ramp_rgb color aiRampRgb color
aiRampRgb1 ramp_rgb interpolation aiRampRgb interpolation
```

# porttype constant
```
aiSpaceTransform input vector3 float3
aiSpaceTransform type string enum
aiSpaceTransform from string enum
aiSpaceTransform to string enum
aiSpaceTransform tangent vector3 float3
aiSpaceTransform normal vector3 float3
aiSpaceTransform normalize boolean bool
aiSpaceTransform scale float float
aiVectorMap input vector3 float3
aiVectorMap tangent vector3 float3
aiVectorMap normal vector3 float3
aiVectorMap order string enum
aiVectorMap invert_x boolean bool
aiVectorMap invert_y boolean bool
aiVectorMap invert_z boolean bool
aiVectorMap color_to_signed boolean bool
aiVectorMap tangent_space boolean bool
aiVectorMap scale float float
aiRandom input_type string enum
aiRandom input_int integer long
aiRandom input_float float float
aiRandom input_color color3 float3
aiRandom seed integer long
aiRandom grayscale boolean bool
aiColorJitter input color3 float3
aiColorJitter data_input integer long
aiColorJitter data_gain_min float float
aiColorJitter data_gain_max float float
aiColorJitter data_hue_min float float
aiColorJitter data_hue_max float float
aiColorJitter data_saturation_min float float
aiColorJitter data_saturation_max float float
aiColorJitter data_seed integer long
aiColorJitter proc_gain_min float float
aiColorJitter proc_gain_max float float
aiColorJitter proc_hue_min float float
aiColorJitter proc_hue_max float float
aiColorJitter proc_saturation_min float float
aiColorJitter proc_saturation_max float float
aiColorJitter proc_seed integer long
aiColorJitter obj_gain_min float float
aiColorJitter obj_gain_max float float
aiColorJitter obj_hue_min float float
aiColorJitter obj_hue_max float float
aiColorJitter obj_saturation_min float float
aiColorJitter obj_saturation_max float float
aiColorJitter obj_seed integer long
aiColorJitter face_gain_min float float
aiColorJitter face_gain_max float float
aiColorJitter face_hue_min float float
aiColorJitter face_hue_max float float
aiColorJitter face_saturation_min float float
aiColorJitter face_saturation_max float float
aiColorJitter face_seed integer long
aiColorJitter face_mode string enum
aiSkin sss_weight float float
aiSkin shallow_scatter_color color3 float3
aiSkin shallow_scatter_weight float float
aiSkin shallow_scatter_radius float float
aiSkin mid_scatter_color color3 float3
aiSkin mid_scatter_weight float float
aiSkin mid_scatter_radius float float
aiSkin deep_scatter_color color3 float3
aiSkin deep_scatter_weight float float
aiSkin deep_scatter_radius float float
aiSkin specular_color color3 float3
aiSkin specular_weight float float
aiSkin specular_roughness float float
aiSkin specular_ior float float
aiSkin sheen_color color3 float3
aiSkin sheen_weight float float
aiSkin sheen_roughness float float
aiSkin sheen_ior float float
aiSkin global_sss_radius_multiplier float float
aiSkin specular_in_secondary_rays boolean bool
aiSkin fresnel_affect_sss boolean bool
aiSkin opacity float float
aiSkin opacity_color color3 float3
aiSkin normal vector3 float3
aiRange input color3 float3
aiRange input_min float float
aiRange input_max float float
aiRange output_min float float
aiRange output_max float float
aiRange smoothstep boolean bool
aiRange contrast float float
aiRange contrast_pivot float float
aiRange bias float float
aiRange gain float float
aiFacingRatio bias float float
aiFacingRatio gain float float
aiFacingRatio linear boolean bool
aiFacingRatio invert boolean bool
aiNormalMap input vector3 float3
aiNormalMap tangent vector3 float3
aiNormalMap normal vector3 float3
aiNormalMap order string enum
aiNormalMap invert_x boolean bool
aiNormalMap invert_y boolean bool
aiNormalMap invert_z boolean bool
aiNormalMap color_to_signed boolean bool
aiNormalMap tangent_space boolean bool
aiNormalMap strength float float
aiCache input color3 float3
aiSky color color3 float3
aiSky intensity float float
aiSky visibility integer bool
aiSky format string enum
aiLayerShader enable1 boolean bool
aiLayerShader name1 string typed
aiLayerShader input1 closure float3
aiLayerShader mix1 float float
aiLayerShader enable2 boolean bool
aiLayerShader name2 string typed
aiLayerShader input2 closure float3
aiLayerShader mix2 float float
aiLayerShader enable3 boolean bool
aiLayerShader name3 string typed
aiLayerShader input3 closure float3
aiLayerShader mix3 float float
aiLayerShader enable4 boolean bool
aiLayerShader name4 string typed
aiLayerShader input4 closure float3
aiLayerShader mix4 float float
aiLayerShader enable5 boolean bool
aiLayerShader name5 string typed
aiLayerShader input5 closure float3
aiLayerShader mix5 float float
aiLayerShader enable6 boolean bool
aiLayerShader name6 string typed
aiLayerShader input6 closure float3
aiLayerShader mix6 float float
aiLayerShader enable7 boolean bool
aiLayerShader name7 string typed
aiLayerShader input7 closure float3
aiLayerShader mix7 float float
aiLayerShader enable8 boolean bool
aiLayerShader name8 string typed
aiLayerShader input8 closure float3
aiLayerShader mix8 float float
aiAdd input1 color3 float3
aiAdd input2 color3 float3
aiFog distance float float
aiFog height float float
aiFog color color3 float3
aiFog ground_point vector3 float3
aiFog ground_normal vector3 float3
aiPow base color3 float3
aiPow exponent color3 float3
aiVolumeSampleRgb channel string typed
aiVolumeSampleRgb position_offset vector3 float3
aiVolumeSampleRgb interpolation string enum
aiVolumeSampleRgb gamma float float
aiVolumeSampleRgb hue_shift float float
aiVolumeSampleRgb saturation float float
aiVolumeSampleRgb contrast float float
aiVolumeSampleRgb contrast_pivot float float
aiVolumeSampleRgb exposure float float
aiVolumeSampleRgb multiply float float
aiVolumeSampleRgb add float float
aiTrigo input color3 float3
aiTrigo function string enum
aiTrigo units string enum
aiTrigo frequency float float
aiTrigo phase float float
aiLayerRgba enable1 boolean bool
aiLayerRgba name1 string typed
aiLayerRgba input1 color4 float3
aiLayerRgba mix1 float float
aiLayerRgba operation1 string enum
aiLayerRgba alpha_operation1 string enum
aiLayerRgba enable2 boolean bool
aiLayerRgba name2 string typed
aiLayerRgba input2 color4 float3
aiLayerRgba mix2 float float
aiLayerRgba operation2 string enum
aiLayerRgba alpha_operation2 string enum
aiLayerRgba enable3 boolean bool
aiLayerRgba name3 string typed
aiLayerRgba input3 color4 float3
aiLayerRgba mix3 float float
aiLayerRgba operation3 string enum
aiLayerRgba alpha_operation3 string enum
aiLayerRgba enable4 boolean bool
aiLayerRgba name4 string typed
aiLayerRgba input4 color4 float3
aiLayerRgba mix4 float float
aiLayerRgba operation4 string enum
aiLayerRgba alpha_operation4 string enum
aiLayerRgba enable5 boolean bool
aiLayerRgba name5 string typed
aiLayerRgba input5 color4 float3
aiLayerRgba mix5 float float
aiLayerRgba operation5 string enum
aiLayerRgba alpha_operation5 string enum
aiLayerRgba enable6 boolean bool
aiLayerRgba name6 string typed
aiLayerRgba input6 color4 float3
aiLayerRgba mix6 float float
aiLayerRgba operation6 string enum
aiLayerRgba alpha_operation6 string enum
aiLayerRgba enable7 boolean bool
aiLayerRgba name7 string typed
aiLayerRgba input7 color4 float3
aiLayerRgba mix7 float float
aiLayerRgba operation7 string enum
aiLayerRgba alpha_operation7 string enum
aiLayerRgba enable8 boolean bool
aiLayerRgba name8 string typed
aiLayerRgba input8 color4 float3
aiLayerRgba mix8 float float
aiLayerRgba operation8 string enum
aiLayerRgba alpha_operation8 string enum
aiLayerRgba clamp boolean bool
aiMixShader mode string enum
aiMixShader mix float float
aiMixShader shader1 closure float3
aiMixShader shader2 closure float3
aiClamp input color3 float3
aiClamp mode string enum
aiClamp min float float
aiClamp max float float
aiClamp min_color color3 float3
aiClamp max_color color3 float3
aiModulo input color3 float3
aiModulo divisor color3 float3
aiStateVector variable string enum
aiSign input color3 float3
aiHair rootcolor color3 float3
aiHair tipcolor color3 float3
aiHair opacity color3 float3
aiHair ambdiff float float
aiHair spec float float
aiHair spec_color color3 float3
aiHair spec_shift float float
aiHair spec_gloss float float
aiHair spec2 float float
aiHair spec2_color color3 float3
aiHair spec2_shift float float
aiHair spec2_gloss float float
aiHair transmission float float
aiHair transmission_color color3 float3
aiHair transmission_spread float float
aiHair kd_ind float float
aiRgbaToFloat input color4 float3
aiRgbaToFloat mode string enum
aiMatrixMultiplyVector input color3 float3
aiMatrixMultiplyVector type string enum
aiMatrixMultiplyVector matrix matrix44 fltMatrix
aiWireframe line_width float float
aiWireframe fill_color color3 float3
aiWireframe line_color color3 float3
aiWireframe raster_space boolean bool
aiWireframe edge_type string enum
aiVolumeSampleFloat channel string typed
aiVolumeSampleFloat position_offset vector3 float3
aiVolumeSampleFloat interpolation string enum
aiVolumeSampleFloat volume_type string enum
aiVolumeSampleFloat sdf_offset float float
aiVolumeSampleFloat sdf_blend float float
aiVolumeSampleFloat sdf_invert boolean bool
aiVolumeSampleFloat input_min float float
aiVolumeSampleFloat input_max float float
aiVolumeSampleFloat contrast float float
aiVolumeSampleFloat contrast_pivot float float
aiVolumeSampleFloat bias float float
aiVolumeSampleFloat gain float float
aiVolumeSampleFloat output_min float float
aiVolumeSampleFloat output_max float float
aiVolumeSampleFloat clamp_min boolean bool
aiVolumeSampleFloat clamp_max boolean bool
aiAbs input color3 float3
aiCellNoise pattern string enum
aiCellNoise additive boolean bool
aiCellNoise octaves integer long
aiCellNoise randomness float float
aiCellNoise lacunarity float float
aiCellNoise amplitude float float
aiCellNoise scale vector3 float3
aiCellNoise offset vector3 float3
aiCellNoise coord_space string enum
aiCellNoise pref_name string typed
aiCellNoise P vector3 float3
aiCellNoise time float float
aiCellNoise color color3 float3
aiCellNoise palette color3 float3
aiCellNoise density float float
aiNoise octaves integer long
aiNoise distortion float float
aiNoise lacunarity float float
aiNoise amplitude float float
aiNoise scale vector3 float3
aiNoise offset vector3 float3
aiNoise coord_space string enum
aiNoise pref_name string typed
aiNoise P vector3 float3
aiNoise time float float
aiNoise color1 color3 float3
aiNoise color2 color3 float3
aiNoise mode string enum
aiUserDataFloat attribute string typed
aiUserDataFloat default float float
aiComplement input color3 float3
aiStandard Kd float float
aiStandard diffuse_roughness float float
aiStandard Ks float float
aiStandard Ks_color color3 float3
aiStandard specular_roughness float float
aiStandard specular_anisotropy float float
aiStandard specular_rotation float float
aiStandard specular_distribution string enum
aiStandard Kr float float
aiStandard Kr_color color3 float3
aiStandard reflection_exit_color color3 float3
aiStandard reflection_exit_use_environment boolean bool
aiStandard Kt float float
aiStandard Kt_color color3 float3
aiStandard transmittance color3 float3
aiStandard refraction_roughness float float
aiStandard refraction_exit_color color3 float3
aiStandard refraction_exit_use_environment boolean bool
aiStandard IOR float float
aiStandard dispersion_abbe float float
aiStandard Kb float float
aiStandard Fresnel boolean bool
aiStandard Krn float float
aiStandard specular_Fresnel boolean bool
aiStandard Ksn float float
aiStandard Fresnel_use_IOR boolean bool
aiStandard Fresnel_affect_diff boolean bool
aiStandard emission float float
aiStandard emission_color color3 float3
aiStandard direct_specular float float
aiStandard indirect_specular float float
aiStandard direct_diffuse float float
aiStandard indirect_diffuse float float
aiStandard enable_glossy_caustics boolean bool
aiStandard enable_reflective_caustics boolean bool
aiStandard enable_refractive_caustics boolean bool
aiStandard enable_internal_reflections boolean bool
aiStandard Ksss float float
aiStandard Ksss_color color3 float3
aiStandard sss_radius color3 float3
aiStandard bounce_factor float float
aiStandard opacity color3 float3
aiStandard normal vector3 float3
aiMotionVector raw boolean bool
aiMotionVector time0 float float
aiMotionVector time1 float float
aiMotionVector max_displace float float
aiSubtract input1 color3 float3
aiSubtract input2 color3 float3
aiRoundCorners samples integer long
aiRoundCorners radius float float
aiRoundCorners normal vector3 float3
aiRoundCorners trace_set string typed
aiRoundCorners inclusive boolean bool
aiRoundCorners self_only boolean bool
aiRoundCorners object_space boolean bool
aiStandardHair base float float
aiStandardHair base_color color3 float3
aiStandardHair melanin float float
aiStandardHair melanin_redness float float
aiStandardHair melanin_randomize float float
aiStandardHair roughness float float
aiStandardHair roughness_azimuthal float float
aiStandardHair roughness_anisotropic boolean bool
aiStandardHair ior float float
aiStandardHair shift float float
aiStandardHair specular_tint color3 float3
aiStandardHair specular2_tint color3 float3
aiStandardHair transmission_tint color3 float3
aiStandardHair diffuse float float
aiStandardHair diffuse_color color3 float3
aiStandardHair emission float float
aiStandardHair emission_color color3 float3
aiStandardHair opacity color3 float3
aiStandardHair indirect_diffuse float float
aiStandardHair indirect_specular float float
aiStandardHair extra_depth integer long
aiStandardHair extra_samples integer long
aiStandardHair aov_id1 string typed
aiStandardHair id1 color3 float3
aiStandardHair aov_id2 string typed
aiStandardHair id2 color3 float3
aiStandardHair aov_id3 string typed
aiStandardHair id3 color3 float3
aiStandardHair aov_id4 string typed
aiStandardHair id4 color3 float3
aiStandardHair aov_id5 string typed
aiStandardHair id5 color3 float3
aiStandardHair aov_id6 string typed
aiStandardHair id6 color3 float3
aiStandardHair aov_id7 string typed
aiStandardHair id7 color3 float3
aiStandardHair aov_id8 string typed
aiStandardHair id8 color3 float3
aiPhysicalSky turbidity float float
aiPhysicalSky ground_albedo color3 float3
aiPhysicalSky use_degrees boolean bool
aiPhysicalSky elevation float float
aiPhysicalSky azimuth float float
aiPhysicalSky sun_direction vector3 float3
aiPhysicalSky enable_sun boolean bool
aiPhysicalSky sun_size float float
aiPhysicalSky sun_tint color3 float3
aiPhysicalSky sky_tint color3 float3
aiPhysicalSky intensity float float
aiPhysicalSky X vector3 float3
aiPhysicalSky Y vector3 float3
aiPhysicalSky Z vector3 float3
aiUserDataString attribute string typed
aiUserDataString default string typed
aiLength input vector3 float3
aiLength mode string enum
aiAtmosphereVolume density float float
aiAtmosphereVolume samples integer long
aiAtmosphereVolume eccentricity float float
aiAtmosphereVolume attenuation float float
aiAtmosphereVolume affect_camera float float
aiAtmosphereVolume affect_diffuse float float
aiAtmosphereVolume affect_specular float float
aiAtmosphereVolume rgb_density color3 float3
aiAtmosphereVolume rgb_attenuation color3 float3
aiFloatToInt input float float
aiFloatToInt mode string enum
aiTriplanar input color3 float3
aiTriplanar scale vector3 float3
aiTriplanar rotate vector3 float3
aiTriplanar offset vector3 float3
aiTriplanar coord_space string enum
aiTriplanar pref_name string typed
aiTriplanar blend float float
aiTriplanar cell boolean bool
aiTriplanar cell_rotate float float
aiTriplanar cell_blend float float
aiBlackbody temperature float float
aiBlackbody normalize boolean bool
aiBlackbody intensity float float
aiShuffle color color3 float3
aiShuffle alpha float float
aiShuffle channel_r string enum
aiShuffle channel_g string enum
aiShuffle channel_b string enum
aiShuffle channel_a string enum
aiShuffle negate_r boolean bool
aiShuffle negate_g boolean bool
aiShuffle negate_b boolean bool
aiShuffle negate_a boolean bool
aiDivide input1 color3 float3
aiDivide input2 color3 float3
aiPassthrough passthrough closure float3
aiPassthrough eval1 closure float3
aiPassthrough eval2 closure float3
aiPassthrough eval3 closure float3
aiPassthrough eval4 closure float3
aiPassthrough eval5 closure float3
aiPassthrough eval6 closure float3
aiPassthrough eval7 closure float3
aiPassthrough eval8 closure float3
aiPassthrough eval9 closure float3
aiPassthrough eval10 closure float3
aiPassthrough eval11 closure float3
aiPassthrough eval12 closure float3
aiPassthrough eval13 closure float3
aiPassthrough eval14 closure float3
aiPassthrough eval15 closure float3
aiPassthrough eval16 closure float3
aiPassthrough eval17 closure float3
aiPassthrough eval18 closure float3
aiPassthrough eval19 closure float3
aiPassthrough eval20 closure float3
aiPassthrough normal vector3 float3
aiImage filename string typed
aiImage color_space string typed
aiImage filter string enum
aiImage mipmap_bias integer long
aiImage single_channel boolean bool
aiImage start_channel integer byte
aiImage swrap string enum
aiImage twrap string enum
aiImage sscale float float
aiImage tscale float float
aiImage sflip boolean bool
aiImage tflip boolean bool
aiImage soffset float float
aiImage toffset float float
aiImage swap_st boolean bool
aiImage uvcoords vector2 float2
aiImage uvset string typed
aiImage multiply color3 float3
aiImage offset color3 float3
aiImage ignore_missing_textures boolean bool
aiImage missing_texture_color color4 float3
aiMatte passthrough closure float3
aiMatte color color4 float3
aiMatte opacity color3 float3
aiVolumeCollector scattering_source string enum
aiVolumeCollector scattering color3 float3
aiVolumeCollector scattering_channel string typed
aiVolumeCollector scattering_color color3 float3
aiVolumeCollector scattering_intensity float float
aiVolumeCollector anisotropy float float
aiVolumeCollector attenuation_source string enum
aiVolumeCollector attenuation color3 float3
aiVolumeCollector attenuation_channel string typed
aiVolumeCollector attenuation_color color3 float3
aiVolumeCollector attenuation_intensity float float
aiVolumeCollector attenuation_mode string enum
aiVolumeCollector emission_source string enum
aiVolumeCollector emission color3 float3
aiVolumeCollector emission_channel string typed
aiVolumeCollector emission_color color3 float3
aiVolumeCollector emission_intensity float float
aiVolumeCollector position_offset vector3 float3
aiVolumeCollector interpolation string enum
aiNegate input color3 float3
aiUtility color_mode string enum
aiUtility shade_mode string enum
aiUtility overlay_mode string enum
aiUtility color color3 float3
aiUtility ao_distance float float
aiUtility roughness float float
aiUtility normal vector3 float3
aiBump2d bump_map float float
aiBump2d bump_height float float
aiBump2d normal vector3 float3
aiUserDataInt attribute string typed
aiUserDataInt default integer long
aiUvTransform passthrough color4 float3
aiUvTransform unit string enum
aiUvTransform uvset string typed
aiUvTransform coverage vector2 float2
aiUvTransform scale_frame vector2 float2
aiUvTransform translate_frame vector2 float2
aiUvTransform rotate_frame float float
aiUvTransform pivot_frame vector2 float2
aiUvTransform wrap_frame_u string enum
aiUvTransform wrap_frame_v string enum
aiUvTransform wrap_frame_color color4 float3
aiUvTransform repeat vector2 float2
aiUvTransform offset vector2 float2
aiUvTransform rotate float float
aiUvTransform pivot vector2 float2
aiUvTransform noise vector2 float2
aiUvTransform mirror_u boolean bool
aiUvTransform mirror_v boolean bool
aiUvTransform flip_u boolean bool
aiUvTransform flip_v boolean bool
aiUvTransform swap_uv boolean bool
aiUvTransform stagger boolean bool
aiLog input color3 float3
aiLog base color3 float3
aiShadowMatte background string enum
aiShadowMatte shadow_color color3 float3
aiShadowMatte shadow_opacity float float
aiShadowMatte background_color color3 float3
aiShadowMatte diffuse_color color3 float3
aiShadowMatte diffuse_use_background boolean bool
aiShadowMatte diffuse_intensity float float
aiShadowMatte backlighting float float
aiShadowMatte indirect_diffuse_enable boolean bool
aiShadowMatte indirect_specular_enable boolean bool
aiShadowMatte specular_color color3 float3
aiShadowMatte specular_intensity float float
aiShadowMatte specular_roughness float float
aiShadowMatte specular_IOR float float
aiShadowMatte alpha_mask boolean bool
aiShadowMatte aov_group string typed
aiShadowMatte aov_shadow string typed
aiShadowMatte aov_shadow_diff string typed
aiShadowMatte aov_shadow_mask string typed
aiMatrixInterpolate type string enum
aiMatrixInterpolate value float float
aiStandardSurface base float float
aiStandardSurface base_color color3 float3
aiStandardSurface diffuse_roughness float float
aiStandardSurface specular float float
aiStandardSurface specular_color color3 float3
aiStandardSurface specular_roughness float float
aiStandardSurface specular_IOR float float
aiStandardSurface specular_anisotropy float float
aiStandardSurface specular_rotation float float
aiStandardSurface metalness float float
aiStandardSurface transmission float float
aiStandardSurface transmission_color color3 float3
aiStandardSurface transmission_depth float float
aiStandardSurface transmission_scatter color3 float3
aiStandardSurface transmission_scatter_anisotropy float float
aiStandardSurface transmission_dispersion float float
aiStandardSurface transmission_extra_roughness float float
aiStandardSurface transmit_aovs boolean bool
aiStandardSurface subsurface float float
aiStandardSurface subsurface_color color3 float3
aiStandardSurface subsurface_radius color3 float3
aiStandardSurface subsurface_scale float float
aiStandardSurface subsurface_anisotropy float float
aiStandardSurface subsurface_type string enum
aiStandardSurface sheen float float
aiStandardSurface sheen_color color3 float3
aiStandardSurface sheen_roughness float float
aiStandardSurface thin_walled boolean bool
aiStandardSurface tangent vector3 float3
aiStandardSurface coat float float
aiStandardSurface coat_color color3 float3
aiStandardSurface coat_roughness float float
aiStandardSurface coat_IOR float float
aiStandardSurface coat_anisotropy float float
aiStandardSurface coat_rotation float float
aiStandardSurface coat_normal vector3 float3
aiStandardSurface thin_film_thickness float float
aiStandardSurface thin_film_IOR float float
aiStandardSurface emission float float
aiStandardSurface emission_color color3 float3
aiStandardSurface opacity color3 float3
aiStandardSurface caustics boolean bool
aiStandardSurface internal_reflections boolean bool
aiStandardSurface exit_to_background boolean bool
aiStandardSurface indirect_diffuse float float
aiStandardSurface indirect_specular float float
aiStandardSurface aov_id1 string typed
aiStandardSurface id1 color3 float3
aiStandardSurface aov_id2 string typed
aiStandardSurface id2 color3 float3
aiStandardSurface aov_id3 string typed
aiStandardSurface id3 color3 float3
aiStandardSurface aov_id4 string typed
aiStandardSurface id4 color3 float3
aiStandardSurface aov_id5 string typed
aiStandardSurface id5 color3 float3
aiStandardSurface aov_id6 string typed
aiStandardSurface id6 color3 float3
aiStandardSurface aov_id7 string typed
aiStandardSurface id7 color3 float3
aiStandardSurface aov_id8 string typed
aiStandardSurface id8 color3 float3
aiFraction input color3 float3
aiMatrixTransform transform_order string enum
aiMatrixTransform rotation_type string enum
aiMatrixTransform units string enum
aiMatrixTransform rotation_order string enum
aiMatrixTransform rotation vector3 float3
aiMatrixTransform axis vector3 float3
aiMatrixTransform angle float float
aiMatrixTransform translate vector3 float3
aiMatrixTransform scale vector3 float3
aiMatrixTransform pivot vector3 float3
aiFlat color color3 float3
aiUvProjection projection_color color4 float3
aiUvProjection projection_type string enum
aiUvProjection coord_space string enum
aiUvProjection pref_name string typed
aiUvProjection P vector3 float3
aiUvProjection u_angle float float
aiUvProjection v_angle float float
aiUvProjection clamp boolean bool
aiUvProjection default_color color4 float3
aiToon mask_color color3 float3
aiToon edge_color color3 float3
aiToon edge_tonemap color3 float3
aiToon edge_opacity float float
aiToon edge_width_scale float float
aiToon silhouette_color color3 float3
aiToon silhouette_tonemap color3 float3
aiToon silhouette_opacity float float
aiToon silhouette_width_scale float float
aiToon priority integer long
aiToon enable_silhouette boolean bool
aiToon ignore_throughput boolean bool
aiToon enable boolean bool
aiToon id_difference boolean bool
aiToon shader_difference boolean bool
aiToon uv_threshold float float
aiToon angle_threshold float float
aiToon normal_type string enum
aiToon base float float
aiToon base_color color3 float3
aiToon base_tonemap color3 float3
aiToon specular float float
aiToon specular_color color3 float3
aiToon specular_roughness float float
aiToon specular_anisotropy float float
aiToon specular_rotation float float
aiToon specular_tonemap color3 float3
aiToon lights string typed
aiToon highlight_color color3 float3
aiToon highlight_size float float
aiToon aov_highlight string typed
aiToon rim_light string typed
aiToon rim_light_color color3 float3
aiToon rim_light_width float float
aiToon aov_rim_light string typed
aiToon transmission float float
aiToon transmission_color color3 float3
aiToon transmission_roughness float float
aiToon transmission_anisotropy float float
aiToon transmission_rotation float float
aiToon sheen float float
aiToon sheen_color color3 float3
aiToon sheen_roughness float float
aiToon emission float float
aiToon emission_color color3 float3
aiToon IOR float float
aiToon normal vector3 float3
aiToon tangent vector3 float3
aiToon indirect_diffuse float float
aiToon indirect_specular float float
aiToon bump_mode string enum
aiToon energy_conserving boolean bool
aiToon user_id boolean bool
aiStateInt variable string enum
aiCurvature output string enum
aiCurvature samples integer long
aiCurvature radius float float
aiCurvature spread float float
aiCurvature threshold float float
aiCurvature bias float float
aiCurvature multiply float float
aiCurvature trace_set string typed
aiCurvature inclusive boolean bool
aiCurvature self_only boolean bool
aiComplexIor material string enum
aiComplexIor mode string enum
aiComplexIor reflectivity color3 float3
aiComplexIor edgetint color3 float3
aiComplexIor n vector3 float3
aiComplexIor k vector3 float3
aiReciprocal input color3 float3
aiLayerFloat enable1 boolean bool
aiLayerFloat name1 string typed
aiLayerFloat input1 float float
aiLayerFloat mix1 float float
aiLayerFloat enable2 boolean bool
aiLayerFloat name2 string typed
aiLayerFloat input2 float float
aiLayerFloat mix2 float float
aiLayerFloat enable3 boolean bool
aiLayerFloat name3 string typed
aiLayerFloat input3 float float
aiLayerFloat mix3 float float
aiLayerFloat enable4 boolean bool
aiLayerFloat name4 string typed
aiLayerFloat input4 float float
aiLayerFloat mix4 float float
aiLayerFloat enable5 boolean bool
aiLayerFloat name5 string typed
aiLayerFloat input5 float float
aiLayerFloat mix5 float float
aiLayerFloat enable6 boolean bool
aiLayerFloat name6 string typed
aiLayerFloat input6 float float
aiLayerFloat mix6 float float
aiLayerFloat enable7 boolean bool
aiLayerFloat name7 string typed
aiLayerFloat input7 float float
aiLayerFloat mix7 float float
aiLayerFloat enable8 boolean bool
aiLayerFloat name8 string typed
aiLayerFloat input8 float float
aiLayerFloat mix8 float float
aiStandardVolume density float float
aiStandardVolume density_channel string typed
aiStandardVolume scatter float float
aiStandardVolume scatter_color color3 float3
aiStandardVolume scatter_color_channel string typed
aiStandardVolume scatter_anisotropy float float
aiStandardVolume transparent color3 float3
aiStandardVolume transparent_depth float float
aiStandardVolume transparent_channel string typed
aiStandardVolume emission_mode string enum
aiStandardVolume emission float float
aiStandardVolume emission_color color3 float3
aiStandardVolume emission_channel string typed
aiStandardVolume temperature float float
aiStandardVolume temperature_channel string typed
aiStandardVolume blackbody_kelvin float float
aiStandardVolume blackbody_intensity float float
aiStandardVolume displacement vector3 float3
aiStandardVolume interpolation string enum
aiColorConvert input color3 float3
aiColorConvert from string enum
aiColorConvert to string enum
aiCompare test string enum
aiCompare input1 float float
aiCompare input2 float float
aiClipGeo intersection closure float3
aiClipGeo trace_set string typed
aiClipGeo inclusive boolean bool
aiThinFilm thickness_min float float
aiThinFilm thickness_max float float
aiThinFilm thickness float float
aiThinFilm ior_medium float float
aiThinFilm ior_film float float
aiThinFilm ior_internal float float
aiAmbientOcclusion samples integer long
aiAmbientOcclusion spread float float
aiAmbientOcclusion near_clip float float
aiAmbientOcclusion far_clip float float
aiAmbientOcclusion falloff float float
aiAmbientOcclusion black color3 float3
aiAmbientOcclusion white color3 float3
aiAmbientOcclusion normal vector3 float3
aiAmbientOcclusion invert_normals boolean bool
aiAmbientOcclusion trace_set string typed
aiAmbientOcclusion inclusive boolean bool
aiAmbientOcclusion self_only boolean bool
aiStateFloat variable string enum
aiCameraProjection projection_color color4 float3
aiCameraProjection offscreen_color color4 float3
aiCameraProjection mask float float
aiCameraProjection camera string message
aiCameraProjection aspect_ratio float float
aiCameraProjection front_facing boolean bool
aiCameraProjection back_facing boolean bool
aiCameraProjection use_shading_normal boolean bool
aiCameraProjection coord_space string enum
aiCameraProjection pref_name string typed
aiCameraProjection P vector3 float3
aiTraceSet passthrough closure float3
aiTraceSet trace_set string typed
aiTraceSet inclusive boolean bool
aiNormalize input vector3 float3
aiMin input1 color3 float3
aiMin input2 color3 float3
aiCross input1 vector3 float3
aiCross input2 vector3 float3
aiSqrt input color3 float3
aiComposite A color4 float3
aiComposite B color4 float3
aiComposite operation string enum
aiComposite alpha_operation string enum
aiFloatToRgba r float float
aiFloatToRgba g float float
aiFloatToRgba b float float
aiFloatToRgba a float float
aiColorCorrect input color4 float3
aiColorCorrect alpha_is_luminance boolean bool
aiColorCorrect alpha_multiply float float
aiColorCorrect alpha_add float float
aiColorCorrect invert boolean bool
aiColorCorrect invert_alpha boolean bool
aiColorCorrect gamma float float
aiColorCorrect hue_shift float float
aiColorCorrect saturation float float
aiColorCorrect contrast float float
aiColorCorrect contrast_pivot float float
aiColorCorrect exposure float float
aiColorCorrect multiply color3 float3
aiColorCorrect add color3 float3
aiColorCorrect mask float float
aiAtan y color3 float3
aiAtan x color3 float3
aiAtan units string enum
aiMax input1 color3 float3
aiMax input2 color3 float3
aiIsFinite input color3 float3
aiRampFloat type string enum
aiRampFloat input float float
aiRampFloat uvset string typed
aiRampFloat use_implicit_uvs string enum
aiRampFloat wrap_uvs boolean bool
aiMultiply input1 color3 float3
aiMultiply input2 color3 float3
aiCarPaint base float float
aiCarPaint base_color color3 float3
aiCarPaint base_roughness float float
aiCarPaint specular float float
aiCarPaint specular_color color3 float3
aiCarPaint specular_flip_flop color3 float3
aiCarPaint specular_light_facing color3 float3
aiCarPaint specular_falloff float float
aiCarPaint specular_roughness float float
aiCarPaint specular_IOR float float
aiCarPaint transmission_color color3 float3
aiCarPaint flake_color color3 float3
aiCarPaint flake_flip_flop color3 float3
aiCarPaint flake_light_facing color3 float3
aiCarPaint flake_falloff float float
aiCarPaint flake_roughness float float
aiCarPaint flake_IOR float float
aiCarPaint flake_scale float float
aiCarPaint flake_density float float
aiCarPaint flake_layers integer long
aiCarPaint flake_normal_randomize float float
aiCarPaint flake_coord_space string enum
aiCarPaint pref_name string typed
aiCarPaint coat float float
aiCarPaint coat_color color3 float3
aiCarPaint coat_roughness float float
aiCarPaint coat_IOR float float
aiCarPaint coat_normal vector3 float3
aiBump3d bump_map float float
aiBump3d bump_height float float
aiBump3d epsilon float float
aiBump3d normal vector3 float3
aiTwoSided front closure float3
aiTwoSided back closure float3
aiFlakes scale float float
aiFlakes density float float
aiFlakes step float float
aiFlakes depth float float
aiFlakes IOR float float
aiFlakes normal_randomize float float
aiFlakes coord_space string enum
aiFlakes pref_name string typed
aiFlakes output_space string enum
aiExp input color3 float3
aiRampRgb type string enum
aiRampRgb input float float
aiRampRgb uvset string typed
aiRampRgb use_implicit_uvs string enum
aiRampRgb wrap_uvs boolean bool
aiDot input1 vector3 float3
aiDot input2 vector3 float3
```

