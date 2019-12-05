[TOC]

# 1. Definition

- Asset
- Look
- Query
    - TypeQuery
    - NodeQuery
    - AttributeQuery
- Assign
    - AttributeSetAssign
    - ShaderSetAssign
- Node
    - Shader
    - Geometry
- Attribute
- Output
- Graph
- ObjectSet
- ShaderSet
- AttributeSet
- Raw
    - Type
        - ValueType
        - Category
    - Name
    - Path
        - FilePath
        - NamespacePath
        - NodePath
        - GeometryPath
        - AttributePath
    - DagPath
        - DagNodePath
        - DagGeometryPath
        - DagAttributePath
    - Data
        - DataBoolean
        - DataFileString
        - DataFloat
        - DataInteger
        - DataDagPathString
        - DataString
    - DataN
        - DataFloatN
        - DataIntegerN
        - DataDagPathStringN
        - DataStringN
    - DataNN
        - DataFloatNN
        - DataIntegerNN
- Value
    - ValueInteger
    - ValueIntegerArray
    - ValueFloat
    - ValueFloatArray
    - ValueBoolean
    - ValueColor2
    - ValueColor2Array
    - ValueColor3
    - ValueColor3Array
    - ValueColor4
    - ValueColor4Array
    - ValueString
    - ValueStringArray
    - ValueFileString
    - ValueDagPathString
    - ValueDagPathStringArray
    - ValueVector2
    - ValueVector2Array
    - ValueVector3
    - ValueVector3Array
    - ValueVector4
    - ValueVector4Array
    - ValueMatrix33
    - ValueMatrix44
- Collection

| Module | Description | Day Use |
| ---- | ---- | ---- |
| Asset | 资产：实现材质资源管理， 扩展方法。 | 待定 |
| Look | 材质变体：实现材质资源的变体管理，扩展方法。 | 3 |
| Query > * | 查询：实现预设管理（优化读取、存储）， 核心方法。 | 5 |
| Assign | 材质分配：实现模型、材质的关系管理， 基础方法。 | 2 |
| Node > * | 节点：实现通用节点、材质节点和模型节点管理， 基础方法。 | 5 |
| Attribute | 通道：实现节点的通道管理，基础方法。 | 3 |
| Output | 输出：实现节点、通道输出管理， 基础方法。 | 2 |
| Graph | 节点图：实现节点图管理， 基础方法。 | 3 |
| ObjectSet | 对象集合：实现多节点、通道、集合管理， 基础方法。 | 2 |
| ShaderSet | 材质集合：实现多材质节点管理， 基础方法。 | 2 |
| AttributeSet | 通道集合：实现多通道管理， 基础方法。 | 2 |
| Raw > Type > * | 类型数据：实现类型管理， 基础方法。 | 2 |
| Raw > Name | 名字数据：实现名字管理， 基础方法。 | 1 |
| Raw > Path > * | 路径：实现路径管理， 基础方法。 | 3 |
| Raw > DagPath > * | 节点路径：实现节点路径管理， 基础方法。 | 2 |
| Raw > Data > *| 数据：实现数据管理（输入、输出、转化）， 核心方法。 | 5 |
| Value > * | 数值：实现特定类型数据管理， 核心方法。 | 3 |
| Collection | 容器；实现节点之间的关系的优化管理，扩展方法。 | 3 |

# 2. DCC ( Maya ) Analysis & Build

- DccPath
    - MaNamespacePath
    - MaNodePath
    - MaAttributePath
- DccDagPath
    - MaDagNodePath
    - MaDagGeometryPath
    - MaDagAttributePath
- DccNode
    - MaNode
    - MaShader
    - MaGeometry
- DccAttribute
    - MaAttribute
- DccData
    - MayaData

| Module | Description | Day Use for Analysis | Day Use for Build |
| ---- | ---- | ---- | ---- |
| DccPath > * | 实现Maya路径管理， 基础方法。 | 2 | 1 |
| DccDagPath > * | 实现Maya节点路径管理， 基础方法。 | 3 | 2 |
| DccNode > MaNode | 实现Maya通用节点、材质节点和模型节点管理， 基础方法。 | 5 | 3 |
| DccAttribute > MaAttribute | 实现Maya节点的通道管理，基础方法。 | 5 | 3 |
| DccData > MayaData | M实现Maya数据管理（输入、输出、转化）， 核心方法。 | 5 | 3 |

# 3. MaterialX

- Read & Write
- Analysis
    - Include
    - Look
    - MaterialAssign
    - PropertySetAssign
    - Material
    - ShaderRef
    - BindInput
    - NodeGraph
    - Node
    - Input
    - Output
    - PropertySet
    - Property
- Manager

| Module | Description | Day Use |
| ---- | ---- | ---- |
| Read & Write | 用于MaterialX文件读取和写入 | 1 |
| Analysis | 用于MaterialX文件解析、修改 | 5 |
| Manager | 用于MaterialX文件管理 | 待定 |