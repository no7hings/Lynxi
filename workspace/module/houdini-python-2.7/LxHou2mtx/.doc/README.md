[TOC]

# hou2mtx

## what?
- 实现HoudiniArnold的Shader Graph数据导出为MaterialX（.mtlx）格式的数据
    - 导出材质节点图(Material, Shader, Node Graph, Node)
    - 导出材质变体信息（Look）
    - 导出Geometry和Material的关系（MaterialAssign）
    - 导出Geometry的Property和Visibility（PropertysetAssign, Visibility）
    
## todo
- DCC内解析Houdini的Look-Dev的Houdini格式的文件(.hip)
- 获取Look-Dev的节点图Material, Shader, Node Graph, Node, Look, MaterialAssign, PropertysetAssign, Visibility数据
- 将Houdini是数据转化为MaterialX的数据
- 开发节点（.hda）作为MaterialX（.mtlx）格式的数据导出的接口

