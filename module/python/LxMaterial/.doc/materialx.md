[TOC]

# Reference

## github

[https://github.com/materialx]: 

## arnold

[https://docs.arnoldrenderer.com/display/A5AFMUG/MaterialX]: 

# Command

-   资源导出

>   ```python
>   from lxrender.maya import method
>   
>   groupString = 'geom_group_name_0'
>   
>   abcFile = 'file_path'
>   matlFile = 'file_path'
>   shaderVariant = 'look_name'
>   
>   renderAsset = method.MaRenderAsset(groupString)
>   
>   renderAsset.modelExport(abcFile)
>   renderAsset.shaderExport(matlFile, shaderVariant)
>   ```
>

-   获取node信息

>   ```powershell
>   cmd
>   cd c:\_pipe\plug\maya\2019\arnold\3.3.0.1\deploy\bin
>   kick -info polymesh
>   ```

# Geometry

# Shader

# example

## 	material

>   ```xml
>   <material name="look_name_ray_switch_shader_name_0_material_shader">
>       <shaderref name="ray_switch_shader_name_0" node="ray_switch_shader">
>       	<bindinput name="camera" type="color3" nodegraph="NG_look_name_ray_switch_shader_name_0_camera" output="out" />
>       </shaderref>
>   </material>
>   
>   <nodegraph name="NG_look_name_ray_switch_shader_name_0_camera">
>       <mix_shader name="mix_shader_name_0" type="closure">
>           <input name="mix" type="float" nodename="ramp_node_name0" />
>           <input name="shader1" type="closure" nodename="standard_surface_name_0" />
>           <input name="shader2" type="closure" nodename="standard_surface_name_1" />
>       </mix_shader>
>       <ramp_rgb name="ramp_node_name0" type="color3">
>           <input name="type" type="string" value="v" />
>           <input name="position" type="floatarray" value="0, 1" />
>           <input name="color" type="floatarray" value="0, 0, 0, 1, 1, 1" />
>           <input name="interpolation" type="integerarray" value="1, 1" />
>           <input name="use_implicit_uvs" type="string" value="curves_only" />
>           <input name="wrap_uvs" type="boolean" value="true" />
>       </ramp_rgb>
>       <standard_surface name="standard_surface_name_0" type="closure">
>       	<input name="base_color" type="color3" value="1, 0, 0" />
>       </standard_surface>
>       <standard_surface name="standard_surface_name_1" type="closure">
>       	<input name="base_color" type="color3" value="0, 1, 0" />
>       </standard_surface>
>       <output name="out" type="color3" nodename="mix_shader_name_0" />
>   </nodegraph>
>   ```
>

## 	property

>   ```xml
>   <look name="look_name">
>   	<propertysetassign name="/geom_group_name_0/geom_name_0/geom_name_0Shape_look_name_propertyset" geom="/geom_group_name_0/geom_name_0/geom_name_0Shape" />
>   </look>
>   
>   <propertyset name="/geom_group_name_0/geom_name_1/geom_name_1Shape_look_name_propertyset">
>   	<property name="subdiv_type" value="catclark" type="string" />
>   	<property name="subdiv_iterations" value="2" type="integer" />
>   </propertyset>
>   ```
>

## 	aov

>   ```xml
>   <material name="look_name_standard_surface_name_0SG_material_shader">
>       <shaderref name="standard_surface_name_0SG" node="aov_write_rgb">
>           <bindinput name="passthrough" type="color3" nodegraph="NG_look_name_standard_surface_name_0SG_passthrough" output="out" />
>           <bindinput name="aov_input" type="color3" nodegraph="NG_look_name_standard_surface_name_0SG_aov_input" output="out" />
>           <bindinput name="aov_name" type="string" value="aov_name_0" />
>       </shaderref>
>   </material>
>   
>   <nodegraph name="NG_look_name_standard_surface_name_0SG_passthrough">
>       <aov_write_rgb name="standard_surface_name_0SG@aov4" type="closure">
>           <input name="passthrough" type="closure" nodename="standard_surface_name_0" />
>           <input name="aov_input" type="color3" nodename="aov_shader_name_1" />
>           <input name="aov_name" type="string" value="aov_name_1" />
>       </aov_write_rgb>
>       <standard_surface name="standard_surface_name_0" type="closure">
>       	<input name="base_color" type="color3" value="1, 0, 0" />
>       </standard_surface>
>       <utility name="aov_shader_name_1" type="color3">
>           <input name="shade_mode" type="string" value="flat" />
>           <input name="color" type="color3" value="1, 0, 0" />
>       </utility>
>       <output name="out" type="color3" nodename="standard_surface_name_0SG@aov4" />
>   </nodegraph>
>   
>   <nodegraph name="NG_look_name_standard_surface_name_0SG_aov_input">
>       <utility name="aov_shader_name_0" type="color3">
>           <input name="shade_mode" type="string" value="flat" />
>           <input name="color" type="color3" value="0, 1, 0" />
>       </utility>
>       <output name="out" type="color3" nodename="aov_shader_name_0" />
>   </nodegraph>
>   ```
>

# DEBUG

## type

-   aiLayerShader, aiMixShader,aiRaySwitchShader

>   ```xml
>   <standard_surface name="shader_name" type="closure">
>   <mix_shader name="shader_name" type="closure">
>   <ray_switch_shader name="shader_name" type="closure">
>   <aov_write_rgb name="shader_name" type="closure">
>   ```
>

-   存在重复写入：如aiRaySwitchShader的camera和shadow通道的连接是同一个材质， 会重复写入这个材质。
