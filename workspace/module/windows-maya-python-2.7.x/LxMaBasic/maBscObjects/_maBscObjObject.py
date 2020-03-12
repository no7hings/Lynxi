# coding:utf-8
from LxMaBasic import maBscObjCore

from LxMaBasic.maBscObjects import _maBscObjCache, _maBscObjRaw, _maBscObjAttribute


class Node(maBscObjCore.Abc_MyaNode):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaNode(nodeString)


class NodeGraph(maBscObjCore.Abc_MyaNodeGraph):
    CLS_mya_node = Node
    CLS_mya_connection = _maBscObjAttribute.Connection

    def __init__(self, shaderObject):
        self._initAbcMyaNodeGraph(shaderObject)


class Shader(maBscObjCore.Abc_MyaShader):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    CLS_mya_node_graph = NodeGraph

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaShader(nodeString)


class Material(maBscObjCore.Abc_MyaMaterial):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    CLS_mya_shader = Shader

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaMaterial(nodeString)


class Dag(maBscObjCore.Abc_MyaDag):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaDag(nodeString)


class Transform(maBscObjCore.Abc_MyaTransform):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaTransform(nodeString)


class Compose(maBscObjCore.Abc_MyaCompoundDag):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaCompoundDag(nodeString)


class Geometry(maBscObjCore.Abc_MyaGeometry):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    CLS_mya_material = Material

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaGeometry(nodeString)


class Mesh(maBscObjCore.Abc_MyaGeometry):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    CLS_mya_transform = Transform
    CLS_mya_dag = Dag
    CLS_mya_node = Node

    CLS_mya_material = Material

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaGeometry(nodeString)


class Group(maBscObjCore.Abc_MyaGroup):
    CLS_mya_node_string = _maBscObjRaw.NodeName
    CLS_mya_port = _maBscObjAttribute.Attribute

    CLS_mya_port_set = _maBscObjRaw.ObjectSet

    OBJ_mya_query_cache = _maBscObjCache.OBJ_mya_query_cache

    def __init__(self, nodeString):
        self._initAbcMyaGroup(nodeString)


class NodeRoot(maBscObjCore.Abc_MyaNodeRoot):
    CLS_group = Group
    CLS_node = Node

    def __init__(self, groupString):
        self._initAbcMyaNodeRoot(groupString)


class GeometryRoot(maBscObjCore.Abc_MyaGeometryRoot):
    CLS_group = Group
    CLS_node = Node

    CLS_geometry = Geometry

    def __init__(self, groupString):
        self._initAbcMyaGeometryRoot(groupString)
