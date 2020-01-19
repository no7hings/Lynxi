[TOC]

# MaterialX

## Element - Hierarchy

-   look
    -   materialassign
    -   propertysetassign
    -   <u>propertyassign</u>
    -   <u>variantassign</u>
    -   <u>visibleassign</u>

-   material
    -   shaderref
        -   bindinput

-   nodegraph
    -   node
        -   input
    -   output

-   propertyset
    -   property

-   <u>collection</u>

-   <u>typedef</u>

-   <u>nodedef</u>

```mermaid
graph RL
classDef style_element_main fill:#f55,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_branch fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_input fill:#ff5,stroke:#000,stroke-width:px,fill-opacity:1
classDef style_element_leaf fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_ref fill:#99f,stroke:#000,stroke-width:1px,fill-opacity:1

materialx((materialx)); class materialx style_element_main
    include(include); class include style_element_ref
    include --- materialx
    
    look(look); class look style_element_branch
    look === materialx
        materialassign(materialassign); class materialassign style_element_input
        materialassign === look
        propertyassign(propertyassign); class propertyassign style_element_input
        propertyassign --- look
        propertysetassign(propertysetassign); class propertysetassign style_element_input
        propertysetassign --- look
        variantassign(variantassign); class variantassign style_element_input
        variantassign --- look
        visibilityassign(visibilityassign); class visibilityassign style_element_input
        visibilityassign --- look
    
    lookgroup(lookgroup); class lookgroup style_element_input
    lookgroup --- materialx
    
    material(material); class material style_element_branch
    material === materialx
        shaderref(shaderref); class shaderref style_element_branch
        shaderref === material
            bindinput(bindinput); class bindinput style_element_leaf
            bindinput --- shaderref
    
    nodegraph(nodegraph); class nodegraph style_element_branch
    nodegraph === materialx
        node(node); class node style_element_branch
        node === nodegraph
            input(input); class input style_element_leaf
            input --- node
        output(output); class output style_element_input
        output --- nodegraph
            
    prepertyset(prepertyset); class prepertyset style_element_branch
    prepertyset === materialx
        property(property); class property style_element_leaf
        property --- prepertyset
    
    collection(collection); class collection style_element_input
    collection --- materialx
    
    typedef(typedef); class typedef style_element_input
    typedef --- materialx
    
    nodedef(nodedef); class nodedef style_element_branch
    nodedef === materialx
        nodedefinput(input); class nodedefinput style_element_leaf
        nodedefinput --- nodedef
```

## Element

```mermaid
graph RL
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

materialx((materialx)); class materialx style_element_cur
subgraph attribute
    materialx.version(version); class materialx.version style_attribute_def
end
materialx.version ===|"required"| materialx

collection((collection)); class collection style_element_1
collection ---|"optional"| materialx
include((include)); class include style_element_1
include ---|"optional"| materialx
look((look)); class look style_element_1
look ---|"optional"| materialx
material((material)); class material style_element_1
material ---|"optional"| materialx
nodegraph((nodegraph)); class nodegraph style_element_1
nodegraph ---|"optional"| materialx
propertyset((propertyset)); class propertyset style_element_1
propertyset ---|"optional"| materialx

typedef((typedef)); class typedef style_element_1
typedef ---|"optional"| materialx
nodedef((nodedef)); class nodedef style_element_1
nodedef ---|"optional"| materialx
subgraph float
    data.float["major . minor"]; class data.float style_data_custom
end
    data.float -.- materialx.version
```

### include

```mermaid
graph RL
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

include((xi:include)); class include style_element_cur
    include.href(href); class include.href style_attribute_input
    include.href ===|"required"| include

subgraph filename
    data.filename["includedfile.mtlx"]; class data.filename style_data_custom
end
    data.filename -.- include.href
```

### look

```mermaid
graph RL
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

look((look)); class look style_element_cur
look.name(name); class look.name style_attribute_output
look.inherit(inherit); class look.inherit style_attribute_input
    look.name ===|"required"| look
    look.inherit ---|"optional"| look
    materialassign((materialassign)); class materialassign style_element_1
    materialassign ---|"optional"| look
    propertyassign((propertyassign)); class propertyassign style_element_1
    propertyassign ---|"optional"| look
    propertysetassign((propertysetassign)); class propertysetassign style_element_1
    propertysetassign ---|"optional"| look

subgraph string
    node.namestring["lookname"]; class node.namestring style_data_custom
end
    node.namestring -.- look.name

subgraph string
    data0.value.string["looktoinheritfrom"]; class data0.value.string style_data_optional
end
    data0.value.string -.- look.inherit
```

#### materialassign

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

materialassign((materialassign)); class materialassign style_element_cur
materialassign.name(name); class materialassign.name style_attribute_output
materialassign.material(material); class materialassign.material style_attribute_input
materialassign.exclusive(exclusive); class materialassign.exclusive style_attribute_input
materialassign.geom(geom); class materialassign.geom style_attribute_input
materialassign.collection(collection); class materialassign.collection style_attribute_input
materialassign_branch_0(("or")); class materialassign_branch_0 style_branch_0
    materialassign.name ===|"required"| materialassign
    materialassign.material ===|"required"| materialassign
    materialassign.exclusive ---|"optional"| materialassign
    materialassign_branch_0 ===|"required"| materialassign
    materialassign.geom ---|"optional"| materialassign_branch_0
    materialassign.collection ---|"optional"| materialassign_branch_0

subgraph string
    node.namestring["materialassign.name"]; class node.namestring style_data_custom
end
    node.namestring -.- materialassign.name

subgraph boolean
    data0.value.boolean["true/false"]; class data0.value.boolean style_data_optional
end
    data0.value.boolean -.- materialassign.exclusive
subgraph string
    data0.value.string["material.name"]; class data0.value.string style_data_output
end
    data0.value.string -.- materialassign.material
subgraph string
    data1.value.string["collection.name"]; class data1.value.string style_data_output
end
    data1.value.string -.- materialassign.collection
subgraph geomname
    data0.value.geomname["geom.name"]; class data0.value.geomname style_data_dcc
end
    data0.value.geomname -.- materialassign.geom
subgraph geomnamearray
    data0.value.geomnamearray["geom_0.name, geom_1.name"]; class data0.value.geomnamearray style_data_dcc
end
    data0.value.geomnamearray -.- materialassign.geom

```

```
<materialassign name=" maname " material=" materialname "
[geom=" geomexpr1[,geomexpr2...] "] [collection=" collectionname "]
[exclusive=true|false]>
...optional variantassign elements...
</materialassign>
```

#### propertyassign

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

propertyassign((propertyassign)); class propertyassign style_element_cur
propertyassign.name(name); class propertyassign.name style_attribute_output
propertyassign.type(type); class propertyassign.type style_attribute_input
propertyassign.value(value); class propertyassign.value style_attribute_input
propertyassign.property(property); class propertyassign.property style_attribute_input
propertyassign.target(target); class propertyassign.target style_attribute_input
propertyassign.geom(geom); class propertyassign.geom style_attribute_input
propertyassign.collection(collection); class propertyassign.collection style_attribute_input
propertyassign_branch_0(("or")); class propertyassign_branch_0 style_branch_0
    propertyassign.name ===|"required"| propertyassign
    propertyassign.type ===|"required"| propertyassign
    propertyassign.value ===|"required"| propertyassign
    propertyassign.property ===|"required"| propertyassign
    propertyassign.target ---|"optional"| propertyassign
    propertyassign_branch_0 ===|"required"| propertyassign
    propertyassign.geom ---|"optional"| propertyassign_branch_0
    propertyassign.collection ---|"optional"| propertyassign_branch_0

subgraph string
    node.namestring["propertyassign.name"]; class node.namestring style_data_custom
end
    node.namestring -.- propertyassign.name

subgraph geomname
    data0.value.geomname["geom.name"]; class data0.value.geomname style_data_dcc
end
    data0.value.geomname -.- propertyassign.geom
subgraph geomnamearray
    data0.value.geomnamearray["geom_0.name, geom_1.name"]; class data0.value.geomnamearray style_data_dcc
end
    data0.value.geomnamearray -.- propertyassign.geom
subgraph string
    data1.value.string["collection.name"]; class data1.value.string style_data_output
end
    data1.value.string -.- propertyassign.collection
subgraph string
    data2.value.string["targetname"]; class data2.value.string style_data_optional
end
    data2.value.string -.- propertyassign.target

subgraph string
    data.type.string["data.type"]; class data.type.string style_data_materialx
end
    data.type.string -.- propertyassign.type
subgraph data.value
    data.value.rawdata["data.value"]; class data.value.rawdata style_data_materialx
end
    data.value.rawdata -.- propertyassign.value
subgraph string
    geom.property.name["geom.attribute.name"]; class geom.property.name style_data_dcc
end
    geom.property.name -.- propertyassign.property
```

#### propertysetassign

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

propertysetassign((propertysetassign)); class propertysetassign style_element_cur
propertysetassign.name(name); class propertysetassign.name style_attribute_output
propertysetassign.propertyset(propertyset); class propertysetassign.propertyset style_attribute_input
propertysetassign.geom(geom); class propertysetassign.geom style_attribute_input
propertysetassign.collection(collection); class propertysetassign.collection style_attribute_input
propertysetassign_branch_0(("or")); class propertysetassign_branch_0 style_branch_0
    propertysetassign.name ===|"required"| propertysetassign
    propertysetassign.propertyset ===|"required"| propertysetassign
    propertysetassign_branch_0 ===|"required"| propertysetassign
    propertysetassign.geom ---|"optional"| propertysetassign_branch_0
    propertysetassign.collection ---|"optional"| propertysetassign_branch_0

subgraph string
    node.namestring["propertyassign.name"]; class node.namestring style_data_custom
end
    node.namestring -.- propertysetassign.name

subgraph string
    data0.value.string["propertyset.name"]; class data0.value.string style_data_output
end
    data0.value.string -.- propertysetassign.propertyset
subgraph geomname
    data0.value.geomname["geom.name"]; class data0.value.geomname style_data_dcc
end
    data0.value.geomname -.- propertysetassign.geom
subgraph geomnamearray
    data0.value.geomnamearray["geom_0.name, geom_1.name"]; class data0.value.geomnamearray style_data_dcc
end
    data0.value.geomnamearray -.- propertysetassign.geom
subgraph string
    data1.value.string["collection.name"]; class data1.value.string style_data_output
end
    data1.value.string -.- propertysetassign.collection
```

#### <u>variantassign</u>

#### <u>visibilityassign</u>

### <u>lookgroup</u>

### material

```mermaid
graph RL
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

material((material)); class material style_element_cur
material_branch_0(("or")); class material_branch_0 style_branch_0
    material_branch_0 ===|"required"| material
material.name(name); class material.name style_attribute_output
    material.name ===|"required"| material
material.inherit(inherit); class material.inherit style_attribute_input
    material.inherit ---|"optional"| material_branch_0
shaderref((shaderref)); class shaderref style_element_cur
    shaderref ---|"optional"| material_branch_0

subgraph string
    node.namestring["material.name"]; class node.namestring style_data_custom
end
    node.namestring -.- material.name

subgraph string
    data0.value.string["materialtoinheritfrom"]; class data0.value.string style_data_output
end
    data0.value.string -.- material.inherit
```

#### shaderref

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_sep fill:#99f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_bound fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

shaderref((shaderref)); class shaderref style_element_cur
shaderref_branch(("or")); class shaderref_branch style_branch_0
shaderref_bound((" ")); class shaderref_bound style_branch_bound
shaderref.name(name); class shaderref.name style_attribute_sep
shaderref.node(node); class shaderref.node style_attribute_input
shaderref.type(type); class shaderref.type style_attribute_input
shaderref.version(version); class shaderref.version style_attribute_input
shaderref.nodedef(nodedef); class shaderref.nodedef style_attribute_input
shaderref.target(target); class shaderref.target style_attribute_input

shaderref_branch ===|"required"| shaderref
shaderref_bound ---|"optional"| shaderref_branch
shaderref.name ===|"required"| shaderref
shaderref.node ---|"optional"| shaderref_bound
shaderref.type ---|"optional"| shaderref
shaderref.version ---|"optional"| shaderref_bound
shaderref.nodedef ---|"optional"| shaderref_branch
shaderref.target ---|"optional"| shaderref

subgraph string
    node.namestring["shaderref.name"]; class node.namestring style_data_custom
end
    node.namestring -.- shaderref.name

subgraph string
    data5.value.string["nodedef.node"]; class data5.value.string style_data_output
end
    data5.value.string -.- shaderref.node
subgraph string
    data3.value.string["nodedef.type"]; class data3.value.string style_data_output
end
    data3.value.string -.- shaderref.type
subgraph string
    data2.value.string["nodedef.version"]; class data2.value.string style_data_optional
end
    data2.value.string -.- shaderref.version
subgraph string
    data1.value.string["nodedef.name"]; class data1.value.string style_data_output
end
    data1.value.string -.- shaderref.nodedef
subgraph string
    data4.value.string["nodedef.target"]; class data4.value.string style_data_optional
end
    data4.value.string -.- shaderref.target

bindinput((bindinput)); class bindinput style_element_cur

bindinput ---|"optional"| shaderref
```

##### bindinput

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_bound fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

bindinput((bindinput)); class bindinput style_element_cur
bindinput_branch(("or")); class bindinput_branch style_branch_0
bindinput_bound((" ")); class bindinput_bound style_branch_bound
bindinput.name(name); class bindinput.name style_attribute_input
bindinput.type(type); class bindinput.type style_attribute_input
bindinput.value(value); class bindinput.value style_attribute_input
bindinput.nodegraph(nodegraph); class bindinput.nodegraph style_attribute_input
bindinput.output(output); class bindinput.output style_attribute_input
    bindinput_branch ===|"required"| bindinput
    bindinput.name ===|"required"| bindinput
    bindinput.type ===|"required"| bindinput
    bindinput.value ---|"optional"| bindinput_branch
    bindinput_bound ---|"optional"| bindinput_branch
    bindinput.nodegraph ---|"optional"| bindinput_bound
    bindinput.output ---|"optional"| bindinput_bound

subgraph string
    data0.value.string["nodegraph.name"]; class data0.value.string style_data_output
end
    data0.value.string -.- bindinput.nodegraph
subgraph string
    data1.value.string["nodegraph.output.name"]; class data1.value.string style_data_output
end
    data1.value.string -.- bindinput.output

subgraph string
    data.type.string["data.type"]; class data.type.string style_data_materialx
end
    data.type.string -.- bindinput.type
subgraph data.value
    data.value.rawdata["data.value"]; class data.value.rawdata style_data_materialx
end
    data.value.rawdata -.- bindinput.value
subgraph string
    geom.property.name["geom.attribute.name"]; class geom.property.name style_data_dcc
end
    geom.property.name -.- bindinput.name
```


```
<material name="steel">
    <shaderref name="sref4" node="simplesrf">
        <bindinput name="diffColor" type="color3" nodegraph="DiffNoise output="o_diffColor"/>
        <bindinput name="specColor" type="color3" output="o_specColor"/>
        <bindinput name="roughness" type="float" value="0.02"/>
    </shaderref>
</material>
```

### nodegraph

```mermaid
graph RL
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_bound fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

nodegraph((nodegraph)); class nodegraph style_element_cur
nodegraph.name(name); class nodegraph.name style_attribute_output
    nodegraph.name ===|"required"| nodegraph

node((node)); class node style_element_cur
    node ===|"required"| nodegraph

output((output)); class output style_element_cur
    output ===|"required"| nodegraph

subgraph string
    node.namestring["nodegraph.name"]; class node.namestring style_data_custom
end
    node.namestring -.- nodegraph.name
```

```
<nodegraph name=" graphname ">
...node element(s)...
...output element(s)...
</nodegraph>
```

#### node

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_bound fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

node((node)); class node style_element_cur
node.name(name); class node.name style_attribute_output
node.type(type); class node.type style_attribute_input
node.version(version); class node.version style_attribute_input

node.name ===|"required"| node
node.type ===|"required"| node
node.version ---|"optional"| node

subgraph string
    node.namestring["node.name"]; class node.namestring style_data_custom
end
    node.namestring -.- node.name

subgraph string
    data0.value.string["nodedef.node"]; class data0.value.string style_data_output
end
    data0.value.string -.- node

subgraph string
    data3.value.string["nodedef.type"]; class data3.value.string style_data_output
end
    data3.value.string -.- node.type

subgraph string
    data2.value.string["nodedef.version"]; class data2.value.string style_data_optional
end
    data2.value.string -.- node.version
```

```
< nodecategory name=" nodename " type=" outputdatatype " [version=" version "]>
	<input name=" paramname " type=" type " [nodename=" nodename "] [value=" value "]/>
	<parameter name=" paramname " type=" type " value=" value "/>
	...additional input or parameter elements...
</ nodecategory >
```

##### input

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_bound fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

input((input)); class input style_element_cur

input_branch(("or")); class input_branch style_branch_0
input_bound((" ")); class input_bound style_branch_bound
input.name(name); class input.name style_attribute_input
input.type(type); class input.type style_attribute_input
input.value(value); class input.value style_attribute_input
input.nodename(nodename); class input.nodename style_attribute_input
input.member(member); class input.member style_attribute_input
input.channels(channels); class input.channels style_attribute_input

input_branch ===|"required"| input
input.name ===|"required"| input
input.type ===|"required"| input
input.value ---|"optional"| input_branch
input_bound ---|"optional"| input_branch
input.nodename ---|"optional"| input_bound
input.member ---|"optional"| input_bound
input.channels ---|"optional"| input_bound

subgraph string
    data.value.string["node.name"]; class data.value.string style_data_output
end
    data.value.string -.- input.nodename

subgraph string
    nodedef.input.name["nodedef.input.name"]; class nodedef.input.name style_data_output
end
    nodedef.input.name -.- input.name
subgraph string
    nodedef.input.type["nodedef.input.type"]; class nodedef.input.type style_data_output
end
    nodedef.input.type -.- input.type
subgraph data.value
    data.value["data.value"]; class data.value style_data_materialx
end
    data.value -.- input.value

subgraph string
    data0.value.string["channel.name"]; class data0.value.string style_data_output
end
    data0.value.string -.- input.channels
```
```
<input name=" paramname " type=" type " [nodename=" nodename " member=" membername " channels=" channels "] [value=" value "]/>
```

#### output

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_bound fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

output((output)); class output style_element_cur
output.name(name); class output.name style_attribute_output
output.type(type); class output.type style_attribute_input
output.nodename(nodename); class output.nodename style_attribute_input
output.channels(channels); class output.channels style_attribute_input

output.name ===|"required"| output
output.type ===|"required"| output
output.nodename ---|"optional"| output
output.channels ---|"optional"| output

subgraph string
    data.value.string["output.name"]; class data.value.string style_data_custom
end
    data.value.string -.- output.name

subgraph string
    data.type.string["data.type"]; class data.type.string style_data_output
end
    data.type.string -.- output.type
subgraph string
    node.name["node.name"]; class node.name style_data_output
end
    node.name -.- output.nodename

subgraph string
    data0.value.string["channel.name"]; class data0.value.string style_data_output
end
    data0.value.string -.- output.channels
```

### propertyset

```mermaid
graph RL
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_bound fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

propertyset((propertyset)); class propertyset style_element_cur
propertyset.name(name); class propertyset.name style_attribute_input
    propertyset.name ===|"required"| propertyset

property((property)); class property style_element_cur
    property ===|"required"| propertyset

subgraph string
    property.name.string["propertyset.name"]; class property.name.string style_data_custom
end
    property.name.string -.- propertyset.name
```

#### property

```mermaid
graph BT
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_materialx fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

property((property)); class property style_element_cur
property.name(name); class property.name style_attribute_output
property.type(type); class property.type style_attribute_input
property.value(value); class property.value style_attribute_input
property.target(target); class property.target style_attribute_input
    property.name ===|"required"| property
    property.type ===|"required"| property
    property.value ===|"required"| property
    property.target ---|"optional"| property

subgraph string
    node.namestring["property.name"]; class node.namestring style_data_dcc
end
    node.namestring -.- property.name

subgraph string
    data2.value.string["targetname"]; class data2.value.string style_data_optional
end
    data2.value.string -.- property.target

subgraph string
    data.type.string["data.type"]; class data.type.string style_data_materialx
end
    data.type.string -.- property.type
subgraph data.value
    data.value.rawdata["data.value"]; class data.value.rawdata style_data_materialx
end
    data.value.rawdata -.- property.value
```

### collection

```mermaid
graph RL
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_dcc fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

collection((collection)); class collection style_element_cur
collection.name(name); class collection.name style_attribute_output
collection.includegeom(includegeom); class collection.includegeom style_attribute_input
collection.includecollection(includecollection); class collection.includecollection style_attribute_input
collection.excludegeom(excludegeom); class collection.excludegeom style_attribute_input
collection_branch_0(("and/or")); class collection_branch_0 style_branch_0
    collection.name ===|"required"| collection
    collection_branch_0 ===|"required"| collection
    collection.includegeom ---|"optional"| collection_branch_0
    collection.includecollection ---|"optional"| collection_branch_0
    collection.excludegeom ---|"optional"| collection
    
subgraph string
    node.namestring["collection.name"]; class node.namestring style_data_custom
end
    node.namestring -.- collection.name

subgraph string
    data0.value.string["collection.name"]; class data0.value.string style_data_output
end
    data0.value.string -.- collection.includecollection
subgraph stringarray
    data0.value.stringarray["collection_0.name, collection_1.name"]; class data0.value.stringarray style_data_output
end
    data0.value.stringarray -.- collection.includecollection
subgraph geomname
    data0.value.geomname["geom.name"]; class data0.value.geomname style_data_dcc
end
    data0.value.geomname -.- collection.includegeom
subgraph geomnamearray
    data0.value.geomnamearray["geom_0.name, geom_1.name"]; class data0.value.geomnamearray style_data_dcc
end
    data0.value.geomnamearray -.- collection.includegeom
subgraph geomname
    data1.value.geomname["geom.name"]; class data1.value.geomname style_data_output
end
    data1.value.geomname -.- collection.excludegeom
subgraph geomnamearray
    data1.value.geomnamearray["geom_0.name, geom_1.name"]; class data1.value.geomnamearray style_data_output
end
    data1.value.geomnamearray -.- collection.excludegeom
```

```
<collection name=" collectionname " [includegeom="geomexpr1[,geomexpr2]..."]
[includecollection="collectionname1[,collectionname2]..."]
[excludegeom="geomexpr3[,geomexpr4]..."]/>
```

### typedef

### nodedef

## Data

### type

#### base

-   integer

-   boolean

-   float

-   color2

-   color3

-   color4

-   vector2

-   vector3

-   vector4

-   matrix33

-   matrix44

-   string

-   filename

-   geomname

#### array

-   integerarray

-   floatarray

-   color2array

-   color3array

-   color4array

-   vector2array

-   vector3array

-   vector4array

-   stringarray

-   geomnamearray

### value

## Property

## Flow

### read

-   look --> material --> nodegraph

```mermaid
graph LR
classDef style_element_cur fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_element_1 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_input fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_materialx fill:#95f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_attribute_def fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_optional fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_output fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_data_custom fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef style_branch_0 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1

subgraph look
    look.name(name); class look.name style_attribute_output
    subgraph materialassign
        materialassign.material(material); class materialassign.material style_attribute_input
    end
end

subgraph material
    material.name(name); class material.name style_attribute_output
    subgraph shaderref
        subgraph bindinput
            bindinput_0.nodegraph(nodegraph); class bindinput_0.nodegraph style_attribute_input
            bindinput_0.output(output); class bindinput_0.output style_attribute_input
        end
        subgraph bindinput
            bindinput_1.nodegraph(nodegraph); class bindinput_1.nodegraph style_attribute_input
            bindinput_1.output(output); class bindinput_1.output style_attribute_input
        end
    end
end

materialassign.material -.-> material.name

subgraph nodegraph
    nodegraph.name(name); class nodegraph.name style_attribute_output
    subgraph output
        output_0.name(name); class output_0.name style_attribute_output
        output_0.nodename(nodename); class output_0.nodename style_attribute_input
    end
    subgraph output
        output_1.name(name); class output_1.name style_attribute_output
        output_1.nodename(nodename); class output_1.nodename style_attribute_input
    end
    subgraph node_0
        node_0.name(name); class node_0.name style_attribute_output
        subgraph input
            input_0.nodename(nodename); class input_0.nodename style_attribute_input
        end
    end
    subgraph node
        node_1.name(name); class node_1.name style_attribute_output
        subgraph input_1
            input_1.value(value); class input_1.value style_attribute_input
        end
    end
    output_0.nodename -.-> node_0.name
    output_1.nodename -.-> node_1.name
    
    input_0.nodename -.-> node_1.name
end

bindinput_0.nodegraph -.-> nodegraph.name
bindinput_0.output -.-> output_0.name
bindinput_1.output -.-> output_1.name
```
