[TOC]

# materialx

## what?

- 基于XML格式的一种数据标准（扩展名“.mtlx”），用于记录“Graphics”（节点图， 主要是“Material”）的数据；
- MTLX文件可以是完全独立的，或拆分成多个文件以实现共用和复用。

## why?

- 解决不同生产环节/DCC软件/渲染器间的“Graphics”的数据传递；
- 解决不同部门和供应商之间的“Graphics”数据传输。

## element

- 定义了处理节点图数据的标准节点；
- 使用<nodedef>定义和扩展“BxDF Shader”（基于“BSDF”和“BRDF”算法的材质或者节点）标准节点集；
- 使用<material>定义“Shader”（材质， 如Surface Shader， Displacement Shader）实例引用的数据流；
- 使用<geominfo>定义可从节点图中引用的“Geometry”的属性；
- 使用<look>定义与“Geometry”绑定的“Material”和“Property”（特定属性， 如细分等）组合。

# reference

- [github](https://github.com/materialx)

- [arnold](https://docs.arnoldrenderer.com/display/A5AFMUG/MaterialX)

- [houdini - export](https://docs.arnoldrenderer.com/display/A5AFHUG/MaterialX+Export)

# progress

- 完成了Basic，Material（Graphic）模块的设计和实现，实现创建，读取和修改Node的数据和连接并统一管理，转化成特定格式（现在只有MaterialX）
的数据并输出；
- 完成了Maya - Basic，Maya - Material（Graphic）模块的设计和实现，实现读取Maya中“Arnold - Node”（以及部分的“Maya - Node”， 需要完善转化
规则）的数据和连接，转化成特定格式（现在只有MaterialX）的数据并输出；

# note
- **Arnold**
    - **Node**：不支持“Maya - Node”；
        - Maya：存在使用“Maya - Node”的情况
            - 解决方案：
                - 导出的时候会自动转化成支持的一个“Arnold - Node”或者多个“Arnold - Node”
                    - 目前支持的“DCC - Node”：
                        1.  “displacementShader”
                        2.  “file”
                        3.  “place2dTexture”
                        4.  “samplerInfo”
                        5.  “ramp”
                        6.  “bump2d > normal_map”
                        7.  “blinn”
                        8.  “lambert”

        - Houdini：待测试
        
    - **Port**：“Array”类型的“Port”无法被连接（待补充）。

    - **Output**：“Node”的“Output”为“唯一”复合型输出。
        - Maya：存在多个“Output”输出。
            - 解决方案：
                - 导出的时候会转化为支持的“Output”。

        - Houdini：符合规则

    - **Channel**：不支持“Channel”之间的直接连接。
        - Maya：支持并存这种连接方式。
            - 解决方案：
                - 导出时会自动转化为支持的连接方式

        - Houdini：符合规则

    - **Color Space**：需要统一色彩空间
        - 现在Maya和Houdini的色彩空间存在问题，需要统一色彩空间的标准。

# schedule

- 完成Houdini - Basic，Houdini - Material模块的设计和实现，实现读取Houdini中Arnold - Node的数据和连接，转化成特定格式MaterialX
的数据并输出， 导入；

