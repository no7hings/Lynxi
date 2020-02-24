[TOC]

# project

## structure

- project
    - basic
    - scheme
    - preset
    - material

- maya project
    - maya basic
    - maya material
    
 - houdini project
    - houdini basic
    - houdini material

## relation

```mermaid

graph LR

classDef red_0 fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef orange_0 fill:#fc9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef yellow_0 fill:#ff9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef green_0 fill:#9fc,stroke:#000,stroke-width:1px,fill-opacity:1
classDef blue_0 fill:#9cf,stroke:#000,stroke-width:1px,fill-opacity:1
classDef violet_0 fill:#ccf,stroke:#000,stroke-width:1px,fill-opacity:1
classDef pink_0 fill:#f9c,stroke:#000,stroke-width:1px,fill-opacity:1
classDef white_0 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

basic("basic") --> scheme("scheme")

basic("basic") --> preset("preset")

basic("basic") --> material("material")

basic --> maya_basic("maya basic")

maya_basic --> maya_material("maya material")

scheme --> preset

preset --> material

preset --> maya_material

basic --> houdini_basic("houdini basic")

houdini_basic --> houdini_material("houdini material")

material --> maya_material

material --> houdini_material

class maya_basic red_0
class maya_material red_0

class houdini_basic green_0
class houdini_material green_0
```

# module

## structure

- module
    - methods
        - sub method
        - ...
    - objects
        - sub object
        - ...
    - configure
    - method core
    - object core
    
### relation

```mermaid

graph TD

configure("configure") --> method_core("method core")

configure --> object_core("object core")

object_core --> objects("objects")

method_core --> object_core

method_core --> methods("methods")

methods --> objects
```

### etc

- LxBasic
    - bscMethods
        - _bscMtdUtility
        - ...
    - bscObjects
        - _bscObjUtility
        - ...
    - bscConfigure
    - bscMtdCore
    - bscObjCore
    
## name

nodeString: "|namespace:name_0|namespace:name_1"

attributeString: "|namespace:name_0|namespace:name_1.portname_0.portname_1"

fullpathName: "|namespace:name_0|namespace:name_1.portname_0.portname_1"

namespacesep: ":"

nodesep: "|"

portsep: "."

name: "namespace:name_1"

fullpathPortname: "portname_0.portname_1"

portname: "portname_1"

# maya

## object

### relation

```mermaid

graph TB

meterial_0["list([Material, ...])"] ---|"materials()"| geometry("Geometry")

surface_shader_0("Shader") ---|"surfaceShader()"| meterial_0

displacement_shader_0("Shader") ---|"displacementShader()"| meterial_0

volume_shader_0("Shader") ---|"volumeShader()"| meterial_0

node_graph_0("NodeGraph") ---|"nodeGraph()"| surface_shader_0

node_0["list([Node, ...])"] ---|"nodes()"| node_graph_0

attribute_0["list([Attribute, ...])"] ---|"attributes()"| node_0

value_0("Value") ---|"value()"| attribute_0

attribute_0 ---|"attributes()"| surface_shader_0
attribute_0 ---|"attributes()"| displacement_shader_0
attribute_0 ---|"attributes()"| volume_shader_0

data_0["python: bool/int/float/unicode/list/None"] ---|"data()"| value_0
```
