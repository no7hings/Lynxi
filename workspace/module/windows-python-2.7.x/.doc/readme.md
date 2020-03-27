[TOC]

# project

## structure

- project
    - basic
    - scheme
    - preset
    - graphic

- maya project
    - maya basic
    - maya graphic
    
 - houdini project
    - houdini basic
    - houdini graphic

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

basic("basic") --> graphic("graphic")

basic --> maya_basic("maya basic")

maya_basic --> maya_graphic("maya graphic")

scheme --> preset

preset --> graphic

preset --> maya_graphic

basic --> houdini_basic("houdini basic")

houdini_basic --> houdini_material("houdini graphic")

graphic --> maya_graphic

graphic --> houdini_material

class maya_basic red_0
class maya_graphic red_0

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

nodepathString: "|namespace:name_0|namespace:name_1"

attrpathString: "|namespace:name_0|namespace:name_1.portname_0.portname_1"

namespacesep: ":"

nodesep: "|"

portsep: "."

name: "namespace:name_1"

portpathString: "portname_0.portname_1"

portname: "portname_1"

# graph

## object

### relation

